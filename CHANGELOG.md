# GazdaCentrum – változásnapló

## 2026. július 15.
### Új RSS-forrás

- Az Agro Napló RSS-feedje ellenőrizve lett.
- Az új forrás bekerült a `sources.csv` fájlba.
- A GitHub Actions tesztfuttatása sikeresen, zöld jelzéssel befejeződött.
- Az Agro Napló hírei megjelentek a `news.json` fájlban.
- A `PROJECT_STATUS.md` és a `TODO.md` dokumentáció frissítve lett.

### Létrehozva

- A `gazdacentrum.hu` és a `www.gazdacentrum.hu` domain beállítása.
- Cloudflare DNS, CDN és SSL aktiválása.
- Cloudflare Pages összekapcsolása a GitHub repositoryval.
- Automatikus deploy beállítása a `main` ágról.
- A GazdaCentrum kezdőoldal és logó elhelyezése.
- Az RSS-alapú hírgyűjtő rendszer létrehozása.
- A `sources.csv`, `fetch_news.py`, `requirements.txt` és `news.json` fájlok létrehozása.
- Hatóránként futó GitHub Actions workflow beállítása.
- Az Agrárszektor RSS-forrásának sikeres tesztelése.
- Az automatikusan gyűjtött hírek megjelenítése a weboldalon.
- A `PROJECT_STATUS.md` és a `TODO.md` dokumentáció létrehozása.

### Jelenlegi állapot

- Az oldal működik HTTPS-en.
- A hírek automatikusan frissülnek.
- Jelenleg egy aktív RSS-forrás van: Agrárszektor.
- Nincs ismert, működést akadályozó hiba.
