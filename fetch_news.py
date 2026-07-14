from __future__ import annotations

import csv
import hashlib
import html
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import feedparser


ROOT = Path(__file__).resolve().parent
SOURCES_FILE = ROOT / "sources.csv"
OUTPUT_FILE = ROOT / "news.json"

MAX_ITEMS_PER_SOURCE = 20
MAX_TOTAL_ITEMS = 200


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


def is_valid_feed_url(url: str) -> bool:
    """Kiszűri az üres és helykitöltő RSS-címeket."""
    url = url.strip()

    if not url:
        return False

    if "IDE_JON" in url.upper():
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


def collect_news(sources: list[dict[str, str]]) -> tuple[list[dict[str, Any]], list[str]]:
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
            error_message = getattr(feed, "bozo_exception", "ismeretlen RSS-hiba")
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


def remove_duplicates(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Link és cím alapján eltávolítja az ismétlődő híreket."""
    unique_items: list[dict[str, Any]] = []
    seen_links: set[str] = set()
    seen_titles: set[str] = set()

    for item in items:
        normalized_link = item["link"].rstrip("/").lower()
        normalized_title = re.sub(
            r"[^a-záéíóöőúüű0-9]+",
            " ",
            item["title"].lower(),
        ).strip()

        if normalized_link in seen_links:
            continue

        if normalized_title in seen_titles:
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
