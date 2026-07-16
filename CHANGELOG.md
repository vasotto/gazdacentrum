# GazdaCentrum – változásnapló

A projekt jelentősebb fejlesztéseinek és módosításainak összefoglalója.

## 2026. július 16.

### Új aktív RSS-források

Az alábbi források tesztelés után bekerültek az aktív hírforrások közé:

- Magyar Mezőgazdaság
- Mezőhír
- Agrofórum
- AKI
- ÖMKi
- FruitVeB
- Agrárközösség

Az Agrárszektorral és az Agro Naplóval együtt jelenleg kilenc aktív RSS-forrás működik.

### Kötegelt RSS-tesztelés

Több lehetséges RSS-forrás egyetlen közös tesztfuttatásban került ellenőrzésre.

A workflow-futtatások során ellenőriztük:

- a feedek feldolgozhatóságát;
- a `news.json` fájlban megjelenő forrásokat;
- az RSS-feldolgozási hibákat;
- az élő oldalon való megjelenést.

### Tesztelt, de inaktív források

Az alábbi források technikai hiba vagy hiányzó RSS miatt nem kerültek be az aktív listába:

- Agrárágazat – `undefined entity` XML-hiba;
- Agrotrend – `undefined entity` XML-hiba;
- AgrárUnió – nem található működő nyilvános RSS;
- Agrokép – a feed nem található vagy le van tiltva;
- Haszon Agrár – hibás feed;
- MAGRO – hibás feed;
- Farmvilág – hibás feed.

### Átmeneti RSS-hibák

- Az ÖMKi feedjénél egyszer kapcsolódási időtúllépés jelentkezett.
- Az Agrárközösség feedjénél egyszer `mismatched tag` XML-hiba jelentkezett.
- Mindkét hiba megszűnt az ismételt workflow-futtatás után.
- A két forrás aktív maradt.

### RSS-szövegek tisztítása

A `fetch_news.py` program kiegészült a felesleges automatikus RSS-zárószövegek eltávolításával.

A program többek között eltávolítja az ilyen részeket:

- `The post ... appeared first on ...`
- hasonló automatikus magyar zárómondatok.

### Tartalmi duplikációszűrés

A korábbi, kizárólag azonos linkre és azonos címre épülő szűrés kiegészült tartalmi hasonlóságvizsgálattal.

A rendszer jelenleg vizsgálja:

- a címek közös kulcsszavait;
- a címek és összefoglalók tartalmi átfedését;
- a publikálási idő közelségét;
- a forrás típusát;
- a láncoltan kapcsolódó duplikációkat.

A megtartási prioritás:

1. hivatalos forrás;
2. szakmai forrás;
3. hírportál.

Azonos forrástípus esetén a frissebb publikálási idő kap előnyt.

### Láncolt duplikációk javítása

A duplikációszűrés korábban csak a már megtartott hírekkel hasonlította össze az új elemeket.

Ez olyan esetben okozott problémát, amikor:

- az első hír egyezett a másodikkal;
- a második egyezett a harmadikkal;
- az első és a harmadik közvetlen hasonlósága gyengébb volt.

A javítás után a kihagyott hírek is részt vesznek a további összehasonlításban, ezért a teljes duplikációs lánc felismerhető.

### Ellenőrzött duplikációs példák

A rendszer sikeresen összevonta:

- a három magyar szamócáról szóló hírt;
- a Velencei-tó alacsony vízállásáról szóló híreket;
- a lengyel cseresznyepiacról szóló híreket;
- az európai burgonyaterület csökkenéséről szóló híreket;
- azonos bolti élelmiszertrenddel foglalkozó híreket.

A téves duplikációs párosítások csökkentése érdekében a hasonlósági feltételek többször finomításra kerültek.

### Dokumentáció

Frissítésre került:

- `PROJECT_STATUS.md`
- `TODO.md`
- `CHANGELOG.md`

## 2026. július 15.

### Projektindítás

- Létrejött a GazdaCentrum GitHub repository.
- Beállításra került a `main` production branch.
- A repository összekapcsolásra került a Cloudflare Pages szolgáltatással.
- A `gazdacentrum.hu` és a `www.gazdacentrum.hu` domain működő HTTPS-kapcsolatot kapott.

### Automatizált hírgyűjtés

- Létrejött a `sources.csv` RSS-forráslista.
- Létrejött a `fetch_news.py` hírgyűjtő program.
- Létrejött a `news.json` adatfájl.
- Beállításra került a `feedparser==6.0.12` Python-függőség.
- Létrejött az `Agrárhírek frissítése` GitHub Actions workflow.
- A workflow kézzel és hatóránként automatikusan futtatható.
- A frissített `news.json` automatikusan visszakerül a repositoryba.

### Első aktív RSS-források

- Az Agrárszektor RSS-feedje beállításra és tesztelésre került.
- Az Agro Napló RSS-feedje beállításra és tesztelésre került.

### Weboldal

- Létrejött az automatikusan frissülő híroldal.
- A GazdaCentrum logó megjelent az oldalon.
- A híreknél megjelenik:
  - a kategória;
  - a cím;
  - a forrás;
  - a publikálási idő;
  - a rövid RSS-összefoglaló;
  - az eredeti cikk linkje.

### Dokumentáció

Létrejött:

- `PROJECT_STATUS.md`
- `TODO.md`
- `CHANGELOG.md`

A `README.md` frissítésre került a projekt technikai és tartalmi bemutatásával.
