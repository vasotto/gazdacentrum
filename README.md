# GazdaCentrum.hu

Automatizált magyar agrárinformációs portál agrárhatáridőkkel, pályázati összefoglalókkal és jogszerűen gyűjtött agrárhírekkel.

## Élő weboldal

- https://gazdacentrum.hu
- https://www.gazdacentrum.hu
- https://gazdacentrum.hu/palyazatok.html
- https://gazdacentrum.hu/naptar-proba.html – fejlesztési próbafelület
- https://gazdacentrum.hu/naptar-szinproba.html – külön színpróba

## Aktuális fő irány

Az elsődleges funkció az **Agrárhatáridők és teendők**.

A cél nem havi naptár, hanem szűrhető, időrendi lista, amely megmutatja:

- mi a teendő;
- mikor nyílik és mikor jár le;
- kiket érint;
- melyik ágazathoz és határidőtípushoz tartozik;
- mi a hivatalos forrás;
- mikor ellenőriztük utoljára.

A `naptar-proba.html` az új felület próbaváltozata. A `naptar.html` csak elfogadott mobil- és asztali teszt után cserélhető le.

## Működési folyamatok

### Agrárhatáridők

```text
hivatalos forrás
→ kézi ellenőrzés
→ deadlines.json
→ naptar-proba.html
→ később naptar.html
```

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

A GitHub `main` ág a production forrás. A ZIP csak pillanatfelvétel.

DNS-módosításnál védeni kell az MX-, SPF-, DKIM-, DMARC- és igazoló TXT-rekordokat.

## Fontos fájlok

| Fájl | Feladat |
|---|---|
| `index.html` | Főoldal, hírek, kategóriák, határidők és céges rovat |
| `naptar.html` | Korábbi production naptároldal; egyelőre nem cserélendő |
| `naptar-proba.html` | Új szűrhető agrárhatáridő- és teendőlista |
| `naptar-szinproba.html` | Négy kapcsolható sötét paletta próbafelülete |
| `deadlines.json` | Határidők és teendők, `schema_version: 2` |
| `grants.json` | Pályázati adatmodell |
| `palyazatok.html` | Pályázati listaoldal |
| `palyazat-kap-rd46-1-25.html` | KAP-RD46-1-25 részletes adatlapja |
| `palyazat-kap-rd38-rd39-1-25.html` | KAP-RD38-RD39-1-25 részletes adatlapja |
| `sources.csv` | Aktív RSS-források |
| `fetch_news.py` | RSS-lekérés, tisztítás, kategorizálás és duplikációszűrés |
| `news.json` | Nyilvánosan megjelenő híradatok |
| `PALYAZATI_ADATLAP_SABLON.md` | Részletes pályázati adatlap-szabvány |
| `SOURCE_AUDIT.md` | Források technikai és jogi auditja |
| `impresszum.html` | Impresszum és szolgáltatási tájékoztatás |
| `.github/workflows/update-news.yml` | Hatóránkénti automatikus hírfrissítés |

## Határidő-adatmodell

A `deadlines.json` jelenleg 10 rekordot tartalmaz.

Határidőtípusok:

- Pályázat;
- Kifizetés;
- Adatszolgáltatás;
- Kötelezettség;
- Bejelentés.

Ágazatok:

- Szántóföld;
- Kertészet;
- Állattenyésztés;
- Erdőgazdálkodás;
- Ökológiai gazdálkodás;
- Általános.

A státuszt a felület számolja ki. A relatív rekord maradhat `date_type: "relative"` és `show_in_main_list: false` értékkel.

Új tétel előtt kötelező ellenőrizni:

- a hivatalos forrást;
- az évet és a dátumtípust;
- a nyitó- és záródátumot;
- az érintetteket és a teendőt;
- a kivételeket és módosításokat;
- az ellenőrzés dátumát.

Hiányzó dátumot, jogosultságot, összeget, szankciót vagy érintetti kört nem szabad kitalálni.

## A próbafelület működése

A `naptar-proba.html`:

- az öt határidőtípus szerint szűr;
- ágazat és időszak szerint szűr;
- a lejárt tételeket alapból elrejti;
- pályázatonként csak a következő releváns szakaszt mutatja;
- megjeleníti a hivatalos forrást és az ellenőrzési dátumot;
- `Teendő részletei` ablakot nyit;
- az egynapos jövőbeli határidőket `esedékes` szöveggel kezeli;
- mobilon egyoszlopos kártyákat és biztonságosan görgethető részletező ablakot használ.

A `naptar-szinproba.html` ugyanezt a működést tartja meg, és négy később értékelendő sötét palettát kínál.

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
| Phylazonit | Általános agrár | céges |
| Magtár Kft. | Gépesítés | céges |
| KAP portál | Támogatások és pályázatok | hivatalos |

Az Agrárközösség inaktív, mert a feed nem ad stabilan feldolgozható RSS-választ.

## Hírgyűjtés

- Forrásonként legfeljebb 20 elem kerül feldolgozásra.
- A végleges `news.json` legfeljebb 200 hírt tartalmaz.
- Egy RSS-forrás lekérése legfeljebb háromszor ismétlődik.
- Egyetlen hibás forrás nem állítja le a teljes futást.
- A tartalmi duplikációszűrés időablaka 72 óra.
- Az RSS-összefoglaló belső feldolgozásra használható, de nem kerül a nyilvános `news.json` fájlba.

### Kategorizálás

A rendszer cím-, RSS-kategória-, URL- és forrásspecifikus jelek alapján kategorizál. A `Mezőgazdasági gépek` megnevezést egységesen `Gépesítés` kategóriára alakítja.

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

A `céges` és `partneri` típusú tartalmak külön ágon maradnak.

## Céges és partneri szakmai tartalmak

Aktív céges források:

- Phylazonit;
- Magtár Kft.

A céges rovat elkülönül a független hírektől, egyértelmű jelölést kap, és nem vesz át teljes cikket, kivonatot vagy külső képet.

## Pályázati rendszer

A `grants.json` 2 pályázatot és összesen 12 benyújtási szakaszt tartalmaz.

Részletes adatlapok:

- `KAP-RD46-1-25` – Működő minőségrendszerhez történő csatlakozás támogatása;
- `KAP-RD38-RD39-1-25` – Erdőtelepítés és fásítás támogatása.

A részletes oldalak elkülönítik a hivatalos adatokat és a GazdaCentrum közérthető magyarázatát.

## Automatikus frissítés

A GitHub Actions workflow:

- kézzel indítható;
- hatóránként automatikusan fut;
- Python 3.12-t használ;
- telepíti a `requirements.txt` függőségeit;
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
- Kritikus agrárinformációnál az eredeti hivatalos forrás az irányadó.
- AI vagy automatizmus kritikus adatot csak emberi ellenőrzés után publikálhat.
- A céges és partneri tartalmakat egyértelműen el kell különíteni.

## Dokumentáció

- `PROJECT_STATUS.md` – aktuális projektállapot;
- `TODO.md` – feladatlista;
- `CHANGELOG.md` – változásnapló;
- `SOURCE_AUDIT.md` – forrásaudit;
- `PALYAZATI_ADATLAP_SABLON.md` – pályázati tartalmi szabvány.
