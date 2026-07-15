from __future__ import annotations

import csv
import hashlib
import html
import json
import re
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

SOURCE_TYPE_PRIORITY = {
    "hivatalos": 3,
    "szakmai": 2,
    "portál": 1,
    "portal": 1,
}

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
    """HTML-elemek és automatikus RSS-zárómondatok eltávolítása."""
    if value is None:
        return ""

    text = html.unescape(str(value))
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text).strip()

    text = re.sub(
        r"\s*The post\b.*?\bappeared first on\b.*$",
        "",
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(
        r"\s*A bejegyzés\b.*?\belőször\b.*$",
        "",
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(r"\s+", " ", text).strip()

    if len(text) > max_length:
        return text[: max_length - 1].rstrip() + "…"

    return text


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

        try:
            feed = feedparser.parse(
                rss_url,
                request_headers={
                    "User-Agent": (
                        "GazdaCentrum RSS Reader/1.0 "
                        "(https://gazdacentrum.hu)"
                    )
                },
            )
        except Exception as exc:
            errors.append(f"{source['name']}: {exc}")
            continue

        if getattr(feed, "bozo", False) and not feed.entries:
            error_message = getattr(
                feed,
                "bozo_exception",
                "ismeretlen RSS-hiba",
            )
            errors.append(f"{source['name']}: {error_message}")
            continue

        for entry in feed.entries[:MAX_ITEMS_PER_SOURCE]:
            title = clean_text(entry.get("title", ""), max_length=220)
            link = str(entry.get("link", "")).strip()

            if not title or not link:
                continue

            published = parse_entry_date(entry)

            summary = clean_text(
                entry.get("summary", entry.get("description", "")),
                max_length=500,
            )

            collected.append(
                {
                    "id": create_item_id(link, title),
                    "title": title,
                    "link": link,
                    "summary": summary,
                    "source": source["name"],
                    "category": source["category"] or "Egyéb",
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
    """Felismeri a más forrásban rövid időn belül megjelent azonos hírt."""
    if item["source"] == existing_item["source"]:
        return False

    item_date = parse_iso_datetime(item["published_at"])
    existing_date = parse_iso_datetime(existing_item["published_at"])

    if abs(item_date - existing_date) > timedelta(
        hours=SEMANTIC_DUPLICATE_WINDOW_HOURS
    ):
        return False

    item_title_tokens = keyword_tokens(item["title"])
    existing_title_tokens = keyword_tokens(existing_item["title"])

    item_content_tokens = keyword_tokens(
        f"{item['title']} {item['summary']}"
    )
    existing_content_tokens = keyword_tokens(
        f"{existing_item['title']} {existing_item['summary']}"
    )

    if not item_content_tokens or not existing_content_tokens:
        return False

    shared_title_tokens = item_title_tokens & existing_title_tokens
    shared_content_tokens = item_content_tokens & existing_content_tokens

    if not shared_content_tokens:
        return False

    overlap_ratio = len(shared_content_tokens) / min(
        len(item_content_tokens),
        len(existing_content_tokens),
    )

    rare_title_tokens = {
        token
        for token in shared_title_tokens
        if len(token) >= 6 and document_frequency[token] <= 4
    }

    rare_content_tokens = {
        token
        for token in shared_content_tokens
        if len(token) >= 5 and document_frequency[token] <= 6
    }

    same_distinct_topic = (
        len(rare_title_tokens) >= 1
        and len(rare_content_tokens) >= 2
        and overlap_ratio >= 0.12
    )

    strongly_overlapping_content = (
        len(shared_content_tokens) >= 4
        and overlap_ratio >= 0.22
    )

    return same_distinct_topic or strongly_overlapping_content


def remove_duplicates(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Pontos és tartalmi hasonlóság alapján szűri a duplikációkat."""
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

        duplicate_of = next(
            (
                existing_item
                for existing_item in unique_items
                if is_semantic_duplicate(
                    item,
                    existing_item,
                    document_frequency,
                )
            ),
            None,
        )

        if duplicate_of:
            print(
                "Hasonló hír miatt kihagyva: "
                f"{item['title']} ({item['source']}) "
                f"→ {duplicate_of['title']} "
                f"({duplicate_of['source']})"
            )
            continue

        seen_links.add(normalized_link)
        seen_titles.add(normalized_title)
        unique_items.append(item)

    return unique_items


def save_news(items: list[dict[str, Any]], errors: list[str]) -> None:
    """Elmenti a híreket JSON-formátumban."""
    items.sort(
        key=lambda item: item["published_at"],
        reverse=True,
    )

    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "item_count": len(items[:MAX_TOTAL_ITEMS]),
        "items": items[:MAX_TOTAL_ITEMS],
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
