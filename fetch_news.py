from __future__ import annotations

import csv
import hashlib
import html
import json
import re
import time
import unicodedata
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import feedparser


ROOT = Path(__file__).resolve().parent
SOURCES_FILE = ROOT / "sources.csv"
OUTPUT_FILE = ROOT / "news.json"

MAX_ITEMS_PER_SOURCE = 20
MAX_TOTAL_ITEMS = 200
SEMANTIC_DUPLICATE_WINDOW_HOURS = 72
RSS_MAX_ATTEMPTS = 3
RSS_RETRY_DELAY_SECONDS = 5

SOURCE_TYPE_PRIORITY = {
    "hivatalos": 3,
    "szakmai": 2,
    "portál": 1,
    "portal": 1,
}


IRRELEVANT_TITLE_PHRASES = (
    "balaton-atuszas",
    "beteg mosomedve",
    "dobbenetes arak a balatonon",
    "fordulat johet a horgaszatban",
    "haletetes kozben fulladt",
    "szobanoveny",
    "kek zonak a kert vegeben",
    "hosszu elet videki recept",
    "meghalt geza ur",
    "papagajok a kezben",
    "rejtelyes uzenetet helyeztek ki egy gazdasagban",
    "uj majomfajt talaltak",
    "allateledelek",
    "minden gazdinak",
    "valasztanak sort",
    "sor-virsli index",
    "ne etesd oket",
    "eletveszelyes hal lepte el",
    "szunyogok ellen",
    "nepszeru marka minden tesztaetelet",
)
CATEGORY_KEYWORDS = (
    (
        "Támogatások és pályázatok",
        (
            "tamogatas",
            "palyazat",
            "palyazh",
            "kap strategiai terv",
            "egyseges kerelem",
            "tamogatasi kerelem",
            "kifizetesi kerelem",
            "jogcim",
            "agrartamogatas",
            "vis maior",
        ),
    ),
    (
        "Állattenyésztés",
        (
            "allattenyesztes",
            "allattarto",
            "takarmany",
            "husmarha",
            "szarvasmarha",
            "sertestenyesztes",
            "sertespestis",
            "baromfi",
            "madarinfluenza",
            "juhtartas",
            "kecsketartas",
            "tejtermeles",
            "tejpiac",
            "takarmanyozas",
            "allategeszsegugy",
            "tojas",
        ),
    ),
    (
        "Gépesítés",
        (
            "traktor",
            "kombajn",
            "mezogazdasagi gep",
            "gepesites",
            "gep",
            "gepgyart",
            "erogep",
            "rakodogep",
            "munkagep",
            "vetogep",
            "permetezogep",
            "betakaritogep",
            "talajmuvelo gep",
            "precizios gep",
        ),
    ),
    (
        "Kertészet",
        (
            "kerteszet",
            "gyumolcs",
            "szamoca",
            "salata",
            "dio",
            "korte",
            "zoldseg",
            "paprika",
            "paradicsom",
            "burgonya",
            "szolo",
            "boraszat",
            "alma",
            "meggy",
            "cseresznye",
            "dinnye",
            "hagyma",
        ),
    ),
    (
        "Növényvédelem",
        (
            "novenyvedelem",
            "novenyvedo",
            "kartev",
            "korokozo",
            "gombabetegseg",
            "gyomirto",
            "rovarolo",
            "fungicid",
            "herbicid",
            "rezisztencia",
            "fertozes",
            "karantenkartevo",
        ),
    ),
    (
        "Időjárás és vízgazdálkodás",
        (
            "aszaly",
            "csapadek",
            "idojaras",
            "vizgazdalkodas",
            "arviz",
            "belviz",
            "ontozes",
            "homerseklet",
            "fagykar",
            "vizhiany",
            "vizallas",
        ),
    ),
    (
        "Ökológiai gazdálkodás",
        (
            "okologiai gazdalkodas",
            "biogazdalkodas",
            "bio minosites",
            "regenerativ gazdalkodas",
            "agrookologia",
            "talajegeszseg",
        ),
    ),
    (
        "Növénytermesztés",
        (
            "novenytermesztes",
            "buza",
            "kukorica",
            "napraforgo",
            "repce",
            "szoja",
            "arpa",
            "kalaszos",
            "vetomag",
            "vetes",
            "aratas",
            "termeshozam",
            "talajmuveles",
            "tarlohantas",
            "tarlobontas",
            "tarlokezeles",
        ),
    ),
    (
        "Agrárgazdaság",
        (
            "agrargazdasag",
            "termeloi ar",
            "felvasarlasi ar",
            "elelmiszerar",
            "piaci ar",
            "agrarpiac",
            "export",
            "import",
            "kereskedelem",
            "elelmiszeripar",
            "inflacio",
            "termelesi koltseg",
        ),
    ),
)
STOP_WORDS = set(
    """
    a az egy es hogy de is nem meg mar mint ami amely ezt ez arra alapjan
    kozott utan elott szerint lehet lett lesz van volt vannak ma most uj
    friss hirek hir magyar hazai ilyen ennek ezzel jo rossz nagy tobb sok csak
    """.split()
)

HUNGARIAN_SUFFIXES = tuple(
    """
    atoknak eteknek otoknak ainknak einknek jainak jeinek ainak einek
    atok etek otok jait jeit jain jein aink eink jaink jeink ban ben bol
    rol tol nal nel nak nek val vel gal gel ert kent abb ebb jai jei ait
    eit ain ein ai ei ra re ba be on en ig at et ot ak ek ok as es os
    t k a e i
    """.split()
)


def clean_text(value: Any, max_length: int = 500) -> str:
    """HTML-elemek eltávolítása és a szöveg megtisztítása."""
    if value is None:
        return ""

    text = html.unescape(str(value))
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text).strip()

    if len(text) > max_length:
        return text[: max_length - 1].rstrip() + "…"

    return text
    
def clean_title(value: Any, max_length: int = 220) -> str:
    """Eltávolítja az RSS-ben kétszer egymás után szereplő címeket."""
    text = clean_text(value, max_length=1000)

    if not text:
        return ""

    text_length = len(text)

    if text_length % 2 == 0:
        middle = text_length // 2
        first_half = text[:middle]
        second_half = text[middle:]

        if first_half == second_half:
            text = first_half.strip()

    return clean_text(text, max_length=max_length)

def clean_summary(
    value: Any,
    title: str,
    max_length: int = 500,
) -> str:
    """Az RSS-összefoglaló megtisztítása a forrásoldali zárószövegektől."""
    text = clean_text(value, max_length=5000)

    if not text:
        return ""

    escaped_title = re.escape(title.strip())

    patterns = [
        (
            rf"\s*The post\s+{escaped_title}\s+"
            rf"(?:appeared first on|first appeared on)\s+.*?\.?\s*$"
        ),
        (
            rf"\s*A\s+{escaped_title}\s+bejegyzés\s+először\s+"
            rf".*?\s+jelent\s+meg\.?\s*$"
        ),
    ]

    for pattern in patterns:
        text = re.sub(
            pattern,
            "",
            text,
            flags=re.IGNORECASE,
        ).strip()

    if len(text) > max_length:
        return text[: max_length - 1].rstrip() + "…"

    return text
    
def clean_kap_summary(
    value: Any,
    max_length: int = 500,
) -> str:
    """Eltávolítja a KAP-portál összefoglalóinak ismétlődő fejlécét."""
    text = clean_text(value, max_length=5000)

    if not text:
        return ""

    text = re.sub(
        r"^\s*.*?\bszerkeszt[oő]\s+"
        r"\d{4}\.\s*\d{1,2}\.\s*\d{1,2}\.,?\s*"
        r"[^–—-]{0,12}[–—-]\s*\d{1,2}:\d{2}\s*",
        "",
        text,
        count=1,
        flags=re.IGNORECASE,
    ).strip()

    return clean_text(text, max_length=max_length)

def is_valid_feed_url(url: str) -> bool:
    """Kiszűri az üres és helykitöltő RSS-címeket."""
    url = url.strip()

    if not url or "IDE_JON" in url.upper():
        return False

    return url.startswith(("https://", "http://"))


def parse_entry_date(entry: Any) -> datetime:
    """Megpróbálja meghatározni a hír közzétételi dátumát."""
    for field in ("published_parsed", "updated_parsed", "created_parsed"):
        value = entry.get(field)

        if value:
            try:
                return datetime(*value[:6], tzinfo=timezone.utc)
            except (TypeError, ValueError):
                continue

    return datetime.now(timezone.utc)


def parse_iso_datetime(value: str) -> datetime:
    """ISO-formátumú dátumot időzónás datetime objektummá alakít."""
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))

        if parsed.tzinfo is None:
            return parsed.replace(tzinfo=timezone.utc)

        return parsed
    except (TypeError, ValueError):
        return datetime.min.replace(tzinfo=timezone.utc)


def load_sources() -> list[dict[str, str]]:
    """Beolvassa a sources.csv fájlt."""
    if not SOURCES_FILE.exists():
        raise FileNotFoundError("Nem található a sources.csv fájl.")

    with SOURCES_FILE.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        required_columns = {"name", "rss_url", "category", "type"}

        if not reader.fieldnames:
            raise ValueError("A sources.csv nem tartalmaz fejlécet.")

        missing = required_columns.difference(reader.fieldnames)

        if missing:
            raise ValueError(
                "Hiányzó oszlopok a sources.csv fájlban: "
                + ", ".join(sorted(missing))
            )

        return [
            {
                "name": row.get("name", "").strip(),
                "rss_url": row.get("rss_url", "").strip(),
                "category": row.get("category", "").strip(),
                "type": row.get("type", "").strip(),
            }
            for row in reader
        ]


def create_item_id(link: str, title: str) -> str:
    """Egyedi azonosítót készít a hírekhez."""
    base = link or title.lower()
    return hashlib.sha256(base.encode("utf-8")).hexdigest()[:16]


def strip_accents(value: str) -> str:
    """Eltávolítja az ékezeteket az összehasonlításhoz."""
    normalized = unicodedata.normalize("NFKD", value)

    return "".join(
        character
        for character in normalized
        if not unicodedata.combining(character)
    )


def stem_token(token: str) -> str:
    """Egyszerű szóvég-normalizálás a hasonló magyar alakokhoz."""
    stem = token

    for _ in range(2):
        changed = False

        for suffix in HUNGARIAN_SUFFIXES:
            if stem.endswith(suffix) and len(stem) - len(suffix) >= 4:
                stem = stem[: -len(suffix)]
                changed = True
                break

        if not changed:
            break

    return stem


def keyword_tokens(value: str) -> set[str]:
    """Kulcsszavakat készít a szöveg tartalmi összevetéséhez."""
    normalized = strip_accents(value.lower())
    words = re.findall(r"[a-z0-9]+", normalized)
    tokens: set[str] = set()

    for word in words:
        if len(word) < 4 or word in STOP_WORDS:
            continue

        stem = stem_token(word)

        if len(stem) >= 4:
            tokens.add(stem)

    return tokens


def is_relevant_item(
    source_name: str,
    title: str,
    link: str,
    summary: str,
) -> bool:
    """Forrás- és címfüggő szabályokkal kiszűri a nyilvánvalóan nem agrár híreket."""
    normalized_source = strip_accents(source_name.lower())
    normalized_title = strip_accents(title.lower())
    normalized_link = strip_accents(link.lower())
    normalized_summary = strip_accents(summary.lower())

    combined_text = f"{normalized_title} {normalized_summary}"

    if any(
        phrase in combined_text
        for phrase in IRRELEVANT_TITLE_PHRASES
    ):
        return False

    # Az Agroinform Házikert rovata jellemzően lakossági,
    # hobbi- és díszkerti tartalmat közöl.
    if (
        normalized_source == "agroinform"
        and "/hazikert/" in normalized_link
    ):
        return False

    # Az Agrofórum hobbikerti és lakossági szaktanácsadási
    # rovatait nem jelenítjük meg a szakmai agrárhírfolyamban.
    if normalized_source == "agroforum" and any(
        path in normalized_link
        for path in (
            "/hazikert-2/",
            "/szaktanacsadas-kerdesek/",
        )
    ):
        return False

    # A GÉPmax személyautós és SUV-hírei nem mezőgazdasági géphírek.
    if normalized_source == "gepmax":
        passenger_vehicle_markers = (
            "suv",
            "proton x70",
            "kia seltos",
            "jeep grand cherokee",
            "renault boreal",
        )

        if any(
            marker in normalized_title
            or marker in normalized_link
            for marker in passenger_vehicle_markers
        ):
            return False

    return True
    
def category_keyword_matches(
    keyword: str,
    text: str,
) -> bool:
    """Megakadályozza a rövid kulcsszavak szavakon belüli téves találatát."""
    compact_keyword = keyword.replace(" ", "")

    # A legfeljebb négybetűs kulcsszavaknak egy szó
    # elején kell kezdődniük. Így az „alma” nem található
    # meg például az „alkalmazása” szó belsejében.
    if len(compact_keyword) <= 4:
        return re.search(
            rf"(?<![a-z0-9]){re.escape(keyword)}",
            text,
        ) is not None

    return keyword in text
    
def determine_category(
    source_category: str,
    title: str,
    summary: str,
) -> str:
    """A cím és az összefoglaló alapján meghatározza a hír kategóriáját."""
    fallback_category = source_category.strip() or "Egyéb"

    # Az első változat csak az általános források híreit
    # kategorizálja automatikusan. A szakosított források
    # eredeti kategóriáját változatlanul hagyja.
    if fallback_category != "Általános agrár":
        return fallback_category

    normalized_title = strip_accents(title.lower())
    normalized_summary = strip_accents(summary.lower())

    best_category = fallback_category
    best_score = 0

    for category, keywords in CATEGORY_KEYWORDS:
        title_matches = sum(
            1
            for keyword in keywords
            if category_keyword_matches(
                keyword,
                normalized_title,
            )
        )

        summary_matches = sum(
            1
            for keyword in keywords
            if category_keyword_matches(
                keyword,
                normalized_summary,
            )
        )

        # Egyetlen, csak az összefoglalóban előforduló szó
        # még nem elegendő a kategória felülírásához.
        if title_matches == 0 and summary_matches < 2:
            continue

        score = title_matches * 2 + summary_matches

        if (
            score > best_score
            or (
                category == "Növényvédelem"
                and best_category == "Kertészet"
                and title_matches > 0
                and score >= best_score - 1
            )
        ):
            best_category = category
            best_score = score

    return best_category
    
def collect_news(
    sources: list[dict[str, str]],
) -> tuple[list[dict[str, Any]], list[str]]:
    """Beolvassa és egységes formátumba rendezi az RSS-híreket."""
    collected: list[dict[str, Any]] = []
    errors: list[str] = []

    for source in sources:
        rss_url = source["rss_url"]

        if not is_valid_feed_url(rss_url):
            print(f"Kihagyva, nincs érvényes RSS-cím: {source['name']}")
            continue

        print(f"RSS beolvasása: {source['name']}")

        feed = None
        last_error: Any = "ismeretlen RSS-hiba"

        for attempt in range(1, RSS_MAX_ATTEMPTS + 1):
            try:
                candidate_feed = feedparser.parse(
                    rss_url,
                    request_headers={
                        "User-Agent": (
                            "GazdaCentrum RSS Reader/1.0 "
                            "(https://gazdacentrum.hu)"
                        )
                    },
                )

                feed_has_error = (
                    getattr(candidate_feed, "bozo", False)
                    and not candidate_feed.entries
                )

                if not feed_has_error:
                    feed = candidate_feed
                    break

                last_error = getattr(
                    candidate_feed,
                    "bozo_exception",
                    "ismeretlen RSS-hiba",
                )

            except Exception as exc:
                last_error = exc

            if attempt < RSS_MAX_ATTEMPTS:
                print(
                    f"Sikertelen RSS-lekérés: {source['name']} "
                    f"({attempt}/{RSS_MAX_ATTEMPTS}). "
                    "Újrapróbálkozás 5 másodperc múlva."
                )
                time.sleep(RSS_RETRY_DELAY_SECONDS)

        if feed is None:
            errors.append(f"{source['name']}: {last_error}")
            continue

        for entry in feed.entries[:MAX_ITEMS_PER_SOURCE]:
            title = clean_title(entry.get("title", ""), max_length=220)
            link = str(entry.get("link", "")).strip()

            if not title or not link:
                continue

            published = parse_entry_date(entry)

            summary = clean_summary(
                entry.get("summary", entry.get("description", "")),
                title,
                max_length=500,
            )

            if source["name"] == "KAP portál":
                summary = clean_kap_summary(
                    summary,
                    max_length=500,
                )

            if not is_relevant_item(
                source["name"],
                title,
                link,
                summary,
            ):
                print(
                    "Nem releváns hír miatt kihagyva: "
                    f"{title} ({source['name']})"
                )
                continue

            collected.append(
                {
                    "id": create_item_id(link, title),
                    "title": title,
                    "link": link,
                    "summary": summary,
                    "source": source["name"],
                    "category": determine_category(
                        source["category"],
                        title,
                        summary,
                    ),
                    "source_type": source["type"],
                    "published_at": published.isoformat(),
                }
            )

    return collected, errors

def is_semantic_duplicate(
    item: dict[str, Any],
    existing_item: dict[str, Any],
    document_frequency: Counter[str],
) -> bool:
    """Óvatosan felismeri az azonos vagy nagyon hasonló híreket."""
    same_source = item["source"] == existing_item["source"]

    item_date = parse_iso_datetime(item["published_at"])
    existing_date = parse_iso_datetime(existing_item["published_at"])

    if abs(item_date - existing_date) > timedelta(
        hours=SEMANTIC_DUPLICATE_WINDOW_HOURS
    ):
        return False

    normalized_item_summary = re.sub(
        r"[^a-z0-9]+",
        " ",
        strip_accents(item["summary"].lower()),
    ).strip()

    normalized_existing_summary = re.sub(
        r"[^a-z0-9]+",
        " ",
        strip_accents(existing_item["summary"].lower()),
    ).strip()

    shorter_summary, longer_summary = sorted(
        (
            normalized_item_summary,
            normalized_existing_summary,
        ),
        key=len,
    )

    # A közel azonos, hosszabb összefoglalókat ugyanannak
    # a hírnek tekintjük, azonos forráson belül is.
    if (
        len(shorter_summary) >= 80
        and shorter_summary in longer_summary
        and len(shorter_summary) / len(longer_summary) >= 0.80
    ):
        return True

    # Ugyanazon forrás eltérő tartalmú cikkeit a további,
    # tágabb szemantikai vizsgálat már ne vonja össze.
    if same_source:
        return False

    item_title_tokens = keyword_tokens(item["title"])
    existing_title_tokens = keyword_tokens(existing_item["title"])

    item_content_tokens = keyword_tokens(
        f"{item['title']} {item['summary']}"
    )
    existing_content_tokens = keyword_tokens(
        f"{existing_item['title']} {existing_item['summary']}"
    )

    if not item_title_tokens or not existing_title_tokens:
        return False

    if not item_content_tokens or not existing_content_tokens:
        return False

    shared_title_tokens = item_title_tokens & existing_title_tokens
    shared_content_tokens = item_content_tokens & existing_content_tokens

    # Legalább egy közös címkulcsszó nélkül nem tekintjük
    # azonos témának a két hírt.
    if not shared_title_tokens:
        return False

    title_overlap_ratio = len(shared_title_tokens) / min(
        len(item_title_tokens),
        len(existing_title_tokens),
    )

    content_overlap_ratio = len(shared_content_tokens) / min(
        len(item_content_tokens),
        len(existing_content_tokens),
    )

    generic_topic_tokens = {
        "rendszer",
        "magyar",
        "magyarorszag",
        "helyzet",
        "fontos",
        "jelentos",
        "termeszt",
        "gazdalkod",
        "mezogazdasag",
        "aktualis",
        "kerdes",
        "valtozas",
        "eredmeny",
        "vizsgalat",
    }

    rare_title_anchors = {
        token
        for token in shared_title_tokens
        if (
            len(token) >= 6
            and document_frequency[token] <= 5
            and token not in generic_topic_tokens
        )
    }

    rare_content_tokens = {
        token
        for token in shared_content_tokens
        if (
            len(token) >= 5
            and document_frequency[token] <= 7
            and token not in generic_topic_tokens
        )
    }

    # Legalább két közös címkulcsszó esetén mérsékelt
    # tartalmi hasonlóság is elegendő.
    multiple_title_match = (
        len(shared_title_tokens) >= 2
        and len(shared_content_tokens) >= 3
        and title_overlap_ratio >= 0.18
        and content_overlap_ratio >= 0.12
    )

    # Egyetlen címkulcsszó csak akkor elegendő, ha az ritka,
    # és az összefoglalók is több jellegzetes szót megosztanak.
    distinct_title_anchors = {
        token
        for token in shared_title_tokens
        if (
            len(token) >= 6
            and token not in generic_topic_tokens
        )
    }

    single_distinct_anchor_match = (
        len(rare_title_anchors) >= 1
        and len(rare_content_tokens) >= 3
        and len(shared_content_tokens) >= 4
        and content_overlap_ratio >= 0.16
    )

    strong_single_anchor_match = (
        len(distinct_title_anchors) >= 1
        and len(shared_content_tokens) >= 3
        and content_overlap_ratio >= 0.22
    )

    return (
        multiple_title_match
        or single_distinct_anchor_match
        or strong_single_anchor_match
    )


def remove_duplicates(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Pontos, tartalmi és láncolt hasonlóság alapján szűri a duplikációkat."""
    document_frequency: Counter[str] = Counter()

    for item in items:
        document_frequency.update(
            keyword_tokens(f"{item['title']} {item['summary']}")
        )

    ordered_items = sorted(
        items,
        key=lambda item: (
            SOURCE_TYPE_PRIORITY.get(
                str(item.get("source_type", "")).lower(),
                0,
            ),
            parse_iso_datetime(item["published_at"]),
        ),
        reverse=True,
    )

    unique_items: list[dict[str, Any]] = []

    # Minden korábban megvizsgált hírt eltárolunk, a kihagyottakat is.
    # Így a láncban kapcsolódó duplikációk is felismerhetők.
    comparison_items: list[
        tuple[dict[str, Any], dict[str, Any]]
    ] = []

    seen_links: set[str] = set()
    seen_titles: set[str] = set()

    for item in ordered_items:
        normalized_link = item["link"].rstrip("/").lower()

        normalized_title = re.sub(
            r"[^a-záéíóöőúüű0-9]+",
            " ",
            item["title"].lower(),
        ).strip()

        if normalized_link in seen_links:
            print(
                "Azonos link miatt kihagyva: "
                f"{item['title']} ({item['source']})"
            )
            continue

        if normalized_title in seen_titles:
            print(
                "Azonos cím miatt kihagyva: "
                f"{item['title']} ({item['source']})"
            )
            continue

        duplicate_match = next(
            (
                (candidate_item, representative_item)
                for candidate_item, representative_item in comparison_items
                if is_semantic_duplicate(
                    item,
                    candidate_item,
                    document_frequency,
                )
            ),
            None,
        )

        seen_links.add(normalized_link)
        seen_titles.add(normalized_title)

        if duplicate_match:
            _, representative_item = duplicate_match

            print(
                "Hasonló hír miatt kihagyva: "
                f"{item['title']} ({item['source']}) "
                f"→ {representative_item['title']} "
                f"({representative_item['source']})"
            )

            # A kihagyott hírt is eltároljuk összehasonlításra,
            # de ugyanahhoz a megtartott reprezentánshoz kapcsoljuk.
            comparison_items.append(
                (item, representative_item)
            )
            continue

        unique_items.append(item)
        comparison_items.append((item, item))

    return unique_items

def save_news(items: list[dict[str, Any]], errors: list[str]) -> None:
    """Elmenti a nyilvánosan megjeleníthető híradatokat JSON-formátumban."""
    items.sort(
        key=lambda item: item["published_at"],
        reverse=True,
    )

    # Az RSS-összefoglaló csak a feldolgozás közben használható
    # relevanciaszűrésre, kategorizálásra és duplikációkeresésre.
    # A forrástól átvett szöveget nem mentjük a nyilvános JSON-ba.
    public_items = [
        {
            key: value
            for key, value in item.items()
            if key != "summary"
        }
        for item in items[:MAX_TOTAL_ITEMS]
    ]

    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "item_count": len(public_items),
        "items": public_items,
        "errors": errors,
    }

    OUTPUT_FILE.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def main() -> None:
    try:
        sources = load_sources()
        collected, errors = collect_news(sources)
        unique_items = remove_duplicates(collected)
        save_news(unique_items, errors)

        print(f"Elkészült: {OUTPUT_FILE.name}")
        print(f"Hírek száma: {len(unique_items[:MAX_TOTAL_ITEMS])}")

        if errors:
            print(f"RSS-hibák száma: {len(errors)}")

    except Exception as exc:
        print(f"Hiba: {exc}")
        raise


if __name__ == "__main__":
    main()
