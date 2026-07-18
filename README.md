# GazdaCentrum.hu

Automatizált magyar agrár hírgyűjtő és gazdálkodói információs portál.

## Élő weboldal

- https://gazdacentrum.hu
- https://www.gazdacentrum.hu

## A projekt célja

A GazdaCentrum célja magyar gazdálkodók számára releváns agrárhírek automatikus összegyűjtése és egységes megjelenítése.

A rendszer:

- RSS-forrásokból gyűjti a híreket;
- eltávolítja a felesleges RSS- és HTML-elemeket;
- kiszűri a nyilvánvalóan nem agrár témájú tartalmakat;
- felismeri az azonos vagy nagyon hasonló híreket;
- megjeleníti a forrást, a publikálási időt és az eredeti cikk linkjét;
- hatóránként automatikusan frissül.

## A rendszer működése

```text
sources.csv
→ fetch_news.py
→ news.json
→ index.html
→ Cloudflare Pages
→ gazdacentrum.hu
```

## Infrastruktúra

### Domain

- gazdacentrum.hu
- www.gazdacentrum.hu

Domainregisztrátor:

- WWH.hu

### DNS, CDN és SSL

- Cloudflare
- HTTPS aktív
- Cloudflare-névszerverek aktívak

### Hosting

- Cloudflare Pages

### Forráskód

GitHub repository:

- `vasotto/gazdacentrum`

Production branch:

- `main`

A Cloudflare Pages a `main` ágra kerülő commitok után automatikusan új deployt készít.

## Fontos fájlok

### `index.html`

A weboldal felülete.

Feladata:

- a GazdaCentrum logó megjelenítése;
- a `news.json` betöltése;
- a hírek kártyás megjelenítése;
- a kategória, cím, forrás, dátum, összefoglaló és eredeti link megjelenítése.

### `gazdacentrum_logo.png`

A weboldalon megjelenő GazdaCentrum logó.

### `sources.csv`

Az aktív RSS-forrásokat tartalmazza.

Oszlopai:

- `name`
- `rss_url`
- `category`
- `type`

### `fetch_news.py`

A hírgyűjtő és feldolgozó program.

Feladata:

- az RSS-források lekérése;
- az adatok egységesítése;
- a szövegek tisztítása;
- a relevanciaszűrés;
- a duplikációszűrés;
- a `news.json` létrehozása.

### `news.json`

A weboldalon megjelenő hírek adatfájlja.

Tartalmazza:

- a generálás időpontját;
- a hírek számát;
- a hírek adatait;
- az RSS-feldolgozás során észlelt hibákat.

### `requirements.txt`

Python-függőség:

```text
feedparser==6.0.12
```

### `.github/workflows/update-news.yml`

A GitHub Actions workflow konfigurációja.

Workflow neve:

- Agrárhírek frissítése

## Aktív RSS-források

Jelenleg 12 aktív forrás működik.

| Forrás | Kategória | Típus |
|---|---|---|
| Agrárszektor | Agrárgazdaság | portál |
| Agro Napló | Általános agrár | portál |
| Magyar Mezőgazdaság | Általános agrár | portál |
| Mezőhír | Általános agrár | portál |
| Agrofórum | Általános agrár | portál |
| AKI | Agrárgazdaság | hivatalos |
| ÖMKi | Ökológiai gazdálkodás | szakmai |
| FruitVeB | Kertészet | szakmai |
| Agrárközösség | Általános agrár | portál |
| Agroinform | Általános agrár | portál |
| Phylazonit | Általános agrár | ceges |
| KAP portál | Támogatások és pályázatok | hivatalos |

Az aktív RSS-címek a `sources.csv` fájlban találhatók.

## RSS-lekérés

A rendszer egy forrás lekérését legfeljebb háromszor próbálja meg.

Beállítások:

- próbálkozások száma: 3;
- várakozás két próbálkozás között: 5 másodperc.

Egyetlen hibás forrás nem állítja le a teljes feldolgozást.

A végleg sikertelen lekérések bekerülnek a `news.json` `errors` mezőjébe.

## Feldolgozási korlátok

- forrásonként legfeljebb 20 hír;
- a végleges adatfájlban legfeljebb 200 hír;
- tartalmi duplikációszűrési időablak: 72 óra.

## Szövegtisztítás

A rendszer:

- eltávolítja a HTML-elemeket;
- dekódolja a HTML-karaktereket;
- megszünteti a felesleges szóközöket;
- korlátozza a címek és összefoglalók hosszát;
- eltávolítja az automatikus RSS-zárószövegeket;
- javítja a kétszer egymás után érkező címeket;
- eltávolítja a KAP-portál összefoglalóinak ismétlődő szerkesztői fejlécét.

## Relevanciaszűrés

A rendszer forrás- és linkfüggő szabályokkal kiszűri a nyilvánvalóan nem agrár témájú tartalmakat.

Jelenlegi példák:

- Agroinform Házikert rovat;
- Agrofórum hobbikerti és lakossági szaktanácsadási rovatok;
- előre meghatározott, nem releváns címkifejezések.

## Duplikációszűrés

A rendszer több szinten ismeri fel az ismétlődő híreket.

### Azonos link

Azonos vagy csak záró perjelben eltérő link esetén egyetlen hír marad meg.

### Azonos cím

A normalizált, írásjelektől megtisztított címek összehasonlításra kerülnek.

### Azonos vagy közel azonos összefoglaló

A rendszer felismeri azokat a híreket is, amelyek eltérő címmel vagy URL-lel, de azonos vagy csak rövid kiegészítésben eltérő összefoglalóval jelennek meg.

Ez azonos forráson belül is működik.

### Tartalmi hasonlóság

Különböző forrásoknál a rendszer vizsgálja:

- a címkulcsszavakat;
- a cím és összefoglaló közös szavait;
- a ritkább, jellegzetes kifejezéseket;
- a tartalmi átfedést;
- a publikálási idő közelségét.

### Forrásprioritás

Duplikáció esetén a független hírfolyamon belüli megtartási sorrend:

```text
hivatalos
→ szakmai
→ portál
```

Azonos forrástípus esetén a frissebb hír kap előnyt. A `ceges` és `partneri` típusú tartalmak külön rovatba tartoznak, ezért a rendszer nem vonja össze őket a független hírfolyam elemeivel.

## Céges és partneri szakmai tartalmak

A `sources.csv` `type` oszlopában a `ceges` és `partneri` érték külön megjelenítési ágat aktivál.

Ezek az elemek:

- a „Céges és partneri szakmai tartalmak” rovatban jelennek meg;
- jól látható forrástípus-jelölést kapnak;
- nem keverednek a „Friss agrárhírek” listába;
- nem kerülnek összevonásra a független hírfolyam hasonló híreivel;
- csak címet, forrást, dátumot, kategóriát és eredeti linket tesznek közzé.

Az első aktív céges forrás a Phylazonit RSS-feedje.

## Automatikus frissítés

A GitHub Actions workflow:

- kézzel elindítható;
- hatóránként automatikusan fut;
- telepíti a Python-függőségeket;
- lefuttatja a `fetch_news.py` programot;
- frissíti a `news.json` fájlt;
- a változást visszamenti a `main` ágra.

A commit után a Cloudflare Pages automatikusan frissíti az élő weboldalt.

## Helyi futtatás

A repository letöltése után telepítsd a szükséges függőséget:

```bash
pip install -r requirements.txt
```

A hírek frissítése:

```bash
python fetch_news.py
```

A helyi weboldal megnyitásához indítható egyszerű webszerver:

```bash
python -m http.server 8000
```

Ezután a weboldal elérhető:

```text
http://localhost:8000
```

## Új RSS-forrás hozzáadása

Új forrást csak külön tesztelés után szabad a `sources.csv` fájlhoz hozzáadni.

Ellenőrizni kell:

- működik-e az RSS;
- milyen gyakran frissül;
- megfelelő-e a dátum;
- működik-e az eredeti cikk linkje;
- rövid kivonatot vagy teljes cikket ad-e;
- vannak-e hibás vagy ismétlődő elemek;
- valódi szerkesztőséghez vagy hivatalos szervezethez tartozik-e;
- releváns-e magyar gazdálkodóknak.

## Tartalmi és jogi alapelvek

- Teljes külső cikket nem veszünk át.
- Külső képet nem töltünk le automatikusan engedély nélkül.
- Minden hírnél megjelenik a forrás és az eredeti cikk linkje.
- Elsősorban RSS-, API- vagy más engedélyezett strukturált forrást használunk.
- Scraping csak külön jogi és technikai vizsgálat után alkalmazható.
- Az RSS-összefoglaló csak belső feldolgozásra használható, a nyilvános `news.json` fájlba nem kerül.
- Támogatási, jogszabályi, pénzügyi és növényvédelmi információnál az eredeti hivatalos forrás ellenőrzése szükséges.
- Az oldalon jelezni kell az automatizált tartalom-előállítást.
- A céges és partneri tartalmakat a független hírfolyamtól egyértelműen el kell különíteni.

## Dokumentáció

A projekt részletes dokumentációja:

- `PROJECT_STATUS.md` – aktuális technikai és tartalmi állapot;
- `TODO.md` – feladatlista és fejlesztési terv;
- `CHANGELOG.md` – elkészült módosítások időrendi naplója;
- `README.md` – a rendszer általános bemutatása.

## Következő fejlesztési irányok

- automatikus tartalmi kategorizálás;
- kategóriaszűrés;
- külön kategóriaoldalak;
- keresési funkció;
- impresszum;
- adatkezelési tájékoztató;
- automatizált tartalom-előállításról szóló tájékoztatás;
- hírlevél;
- később AI-alapú saját összefoglaló;
- „Miért fontos a gazdának?” mező.
