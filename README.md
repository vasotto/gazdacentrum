# GazdaCentrum.hu

Automatizált magyar agrár hírgyűjtő, pályázatfigyelő és gazdálkodói információs portál.

## Élő weboldal

- https://gazdacentrum.hu
- https://www.gazdacentrum.hu
- https://gazdacentrum.hu/palyazatok.html

## A projekt célja

A GazdaCentrum magyar gazdálkodók számára gyűjt és rendszerez:

- agrárhíreket jogszerű RSS- és más strukturált forrásokból;
- hivatalos pályázati és támogatási információkat;
- benyújtási és kifizetési határidőket;
- elkülönített céges és partneri szakmai tartalmakat.

A rendszer megjeleníti a forrást, a dátumot és az eredeti linket. Teljes külső cikket és külső képet nem vesz át automatikusan.

## Működési folyamatok

### Hírek

```text
sources.csv
→ fetch_news.py
→ news.json
→ index.html
→ Cloudflare Pages
→ gazdacentrum.hu
```

### Pályázatok

```text
hivatalos KAP-adatlapok és dokumentumok
→ ellenőrzött strukturált adatok
→ grants.json és deadlines.json
→ palyazatok.html és részletes pályázati adatlapok
```

## Infrastruktúra

- Domain: `gazdacentrum.hu`, `www.gazdacentrum.hu`
- Domainregisztrátor: WWH.hu
- DNS, CDN és SSL: Cloudflare
- Hosting: Cloudflare Pages
- GitHub repository: `vasotto/gazdacentrum`
- Production branch: `main`
- Automatikus deploy: minden `main` ágra kerülő commit után

DNS-módosításnál védeni kell az MX-, SPF-, DKIM-, DMARC- és igazoló TXT-rekordokat.

## Fontos fájlok

| Fájl | Feladat |
|---|---|
| `index.html` | Főoldal, hírek, kategóriák, határidők és céges rovat |
| `sources.csv` | Aktív RSS-források |
| `fetch_news.py` | RSS-lekérés, tisztítás, kategorizálás és duplikációszűrés |
| `news.json` | Nyilvánosan megjelenő híradatok |
| `deadlines.json` | Strukturált pályázati és támogatási határidők |
| `grants.json` | Pályázati adatmodell |
| `palyazatok.html` | Pályázati listaoldal |
| `palyazat-kap-rd46-1-25.html` | Minőségrendszeri pályázat részletes adatlapja |
| `palyazat-kap-rd38-rd39-1-25.html` | Erdőtelepítési pályázat részletes adatlapja |
| `PALYAZATI_ADATLAP_SABLON.md` | Egységes részletes pályázati adatlap-szabvány |
| `SOURCE_AUDIT.md` | Források technikai és jogi auditja |
| `impresszum.html` | Impresszum és szolgáltatási tájékoztatás |
| `.github/workflows/update-news.yml` | Hatóránkénti automatikus hírfrissítés |

## Aktív RSS-források

Jelenleg 12 aktív forrás szerepel a `sources.csv` fájlban.

| Forrás | Alapkategória | Típus |
|---|---|---|
| Agrárszektor | Agrárgazdaság | portál |
| Agro Napló | Általános agrár | portál |
| Magyar Mezőgazdaság | Általános agrár | portál |
| Mezőhír | Általános agrár | portál |
| Agrofórum | Általános agrár | portál |
| AKI | Agrárgazdaság | hivatalos |
| ÖMKi | Ökológiai gazdálkodás | szakmai |
| FruitVeB | Kertészet | szakmai |
| Agroinform | Általános agrár | portál |
| Phylazonit | Általános agrár | ceges |
| Magtár Kft. | Gépesítés | ceges |
| KAP portál | Támogatások és pályázatok | hivatalos |

Az Agrárközösség jelenleg inaktív, mert a feed ellenőrzőoldalt vagy hibás XML-választ adott.

## Hírgyűjtés

- Forrásonként legfeljebb 20 elem kerül feldolgozásra.
- A végleges `news.json` legfeljebb 200 hírt tartalmaz.
- Egy RSS-forrás lekérése legfeljebb háromszor ismétlődik.
- Egyetlen hibás forrás nem állítja le a teljes futást.
- A tartalmi duplikációszűrés időablaka 72 óra.
- Az RSS-összefoglaló belső feldolgozásra használható, de nem kerül a nyilvános `news.json` fájlba.

### Kategorizálás

A rendszer cím-, RSS-kategória-, URL- és forrásspecifikus jelek alapján kategorizál. A `Mezőgazdasági gépek` megnevezést egységesen `Gépesítés` kategóriára alakítja.

A főoldali `Gépesítés` kártya akkor is működik, ha az aktuális gépes hírek kizárólag a külön céges rovatban találhatók: ilyenkor a Magtár Kft. tartalmaihoz navigál, nem keveri azokat a független hírfolyamba.

### Duplikációszűrés

A rendszer vizsgálja:

- azonos vagy normalizált linket;
- azonos vagy normalizált címet;
- azonos és közel azonos belső összefoglalót;
- tartalmi kulcsszó-átfedést;
- publikálási időt;
- láncoltan kapcsolódó duplikációkat.

Forrásprioritás:

```text
hivatalos
→ szakmai
→ portál
```

A `ceges` és `partneri` típusú tartalmak külön ágon maradnak.

## Céges és partneri szakmai tartalmak

Aktív céges források:

- Phylazonit;
- Magtár Kft.

A céges rovat:

- alapállapotban nem jelenít meg cikkeket;
- vállalatonként külön választógombot használ;
- egyértelmű `Céges szakmai tartalom` jelölést ad;
- nem keveri a vállalati cikkeket a független hírekkel;
- a Magtár Kft. `AKCIÓK` kategóriájú elemeit kizárja.

## Pályázati rendszer

A `grants.json` jelenleg 2 pályázatot és összesen 12 benyújtási szakaszt tartalmaz.

Részletes adatlapok:

- `KAP-RD46-1-25` – Működő minőségrendszerhez történő csatlakozás támogatása;
- `KAP-RD38-RD39-1-25` – Erdőtelepítés és fásítás támogatása.

Mindkét felhívás aktív, de 2026. július 20-án két benyújtási időszak közötti állapotban van. A következő beadási szakaszok 2026 októberében indulnak.

A részletes oldalak elkülönítik:

- a hivatalos adatokat;
- a GazdaCentrum közérthető értelmezését;
- a jogosultságot;
- a támogatási összegeket;
- a pontozást;
- a kötelezettségeket;
- a legfontosabb buktatókat;
- a hivatalos dokumentumokat és módosításokat.

## Automatikus frissítés

A GitHub Actions workflow:

- kézzel indítható;
- hatóránként automatikusan fut;
- Python 3.12-t használ;
- telepíti a `feedparser==6.0.12` függőséget;
- lefuttatja a `fetch_news.py` programot;
- csak a `news.json` fájlt commitolja vissza.

## Helyi futtatás

```bash
pip install -r requirements.txt
python fetch_news.py
python -m http.server 8000
```

Ezután:

```text
http://localhost:8000
```

## Tartalmi és jogi alapelvek

- Teljes külső cikket nem veszünk át.
- Külső képet nem töltünk le automatikusan.
- Minden hírnél szerepel a forrás, a dátum és az eredeti link.
- Scraping csak külön jogi és technikai vizsgálat után használható.
- Támogatási, jogszabályi, pénzügyi és növényvédelmi információnál az eredeti hivatalos forrás az irányadó.
- A hírfeldolgozás részben automatizált.
- Kritikus pályázati adat AI vagy automatizmus segítségével csak emberi ellenőrzés után publikálható.
- A céges és partneri tartalmakat egyértelműen el kell különíteni.

## Dokumentáció

- `PROJECT_STATUS.md` – aktuális projektállapot;
- `TODO.md` – feladatlista;
- `CHANGELOG.md` – változásnapló;
- `SOURCE_AUDIT.md` – forrásaudit;
- `PALYAZATI_ADATLAP_SABLON.md` – pályázati tartalmi szabvány.
