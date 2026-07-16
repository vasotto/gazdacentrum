# GazdaCentrum – változásnapló

A projekt jelentősebb fejlesztéseinek és módosításainak összefoglalója.

## 2026. július 16.

### Aktív RSS-források bővítése

Az alábbi források tesztelés után bekerültek az aktív hírforrások közé:

- Magyar Mezőgazdaság
- Mezőhír
- Agrofórum
- AKI
- ÖMKi
- FruitVeB
- Agrárközösség
- Agroinform
- GÉPmax
- KAP portál

Az Agrárszektorral és az Agro Naplóval együtt jelenleg 12 aktív RSS-forrás működik.

A jelenlegi aktív források:

1. Agrárszektor
2. Agro Napló
3. Magyar Mezőgazdaság
4. Mezőhír
5. Agrofórum
6. AKI
7. ÖMKi
8. FruitVeB
9. Agrárközösség
10. Agroinform
11. GÉPmax
12. KAP portál

### RSS-források tesztelése

A lehetséges RSS-forrásoknál ellenőriztük:

- a feed elérhetőségét;
- a feed technikai feldolgozhatóságát;
- a publikálási időt;
- a hírek linkjeit;
- az összefoglalók tartalmát;
- az ismétlődő híreket;
- a `news.json` fájlban történő megjelenést;
- az élő oldalon történő megjelenést.

Új forrás csak sikeres teszt után kerülhet be a `sources.csv` fájlba.

### Tesztelt, de inaktív források

Az alábbi források technikai hiba vagy hiányzó RSS miatt nem kerültek be az aktív listába:

- Agrárágazat – `undefined entity` XML-hiba;
- Agrotrend – `undefined entity` XML-hiba;
- AgrárUnió – nem található működő nyilvános RSS;
- Agrokép – a feed nem található vagy le van tiltva;
- Haszon Agrár – hibás feed;
- MAGRO – hibás feed;
- Farmvilág – hibás feed.

### Automatikus RSS-újrapróbálás

A `fetch_news.py` program kiegészült automatikus újrapróbálási rendszerrel.

Jelenlegi működés:

- egy RSS-forrás lekérése legfeljebb háromszor történik meg;
- a próbálkozások között öt másodperc várakozás van;
- egyetlen hibás forrás nem állítja le a többi forrás feldolgozását;
- a végleg sikertelen lekérések bekerülnek a `news.json` `errors` mezőjébe.

Ez csökkenti az átmeneti kapcsolódási és XML-feldolgozási hibák hatását.

### Átmeneti RSS-hibák kezelése

Korábban előfordult:

- ÖMKi kapcsolódási időtúllépés;
- Agrárközösség `mismatched tag` XML-hiba.

Mindkét hiba megszűnt az ismételt lekérés után, ezért a két forrás aktív maradt.

A legutóbbi ellenőrzött futás hibamentesen fejeződött be.

### RSS-szövegek tisztítása

A `fetch_news.py` program kiegészült a felesleges automatikus RSS-szövegek eltávolításával.

A program:

- eltávolítja a HTML-elemeket;
- dekódolja a HTML-karaktereket;
- megszünteti a felesleges szóközöket;
- korlátozza a címek és összefoglalók hosszát;
- eltávolítja a `The post ... appeared first on ...` zárószövegeket;
- eltávolítja a magyar „bejegyzés először ... jelent meg” típusú zárószövegeket.

### Duplán érkező RSS-címek javítása

Egyes Agroinform-hírek címe az RSS-ben kétszer egymás után szerepelt.

A `clean_title()` függvény felismeri az ilyen ismétlődést, és csak egy címpéldányt tart meg.

### KAP-portál összefoglalóinak tisztítása

A KAP-portál RSS-összefoglalói korábban tartalmazták:

- a szerkesztő nevét;
- a publikálási dátumot;
- a publikálási időpontot.

A `clean_kap_summary()` függvény eltávolítja ezt az ismétlődő fejlécet.

### Relevanciaszűrés

A rendszer forrás- és linkfüggő szabályokkal kiszűri a nyilvánvalóan nem agrár témájú tartalmakat.

A jelenlegi szabályok többek között kizárják:

- az ismert, nem releváns címkifejezéseket;
- az Agroinform Házikert rovatát;
- az Agrofórum hobbikerti és lakossági szaktanácsadási rovatait;
- a GÉPmax személyautós és SUV-híreit.

A szűrés célja a nyilvánvalóan idegen témájú tartalmak eltávolítása, nem pedig minden határeset automatikus eldöntése.

### Azonos linkű hírek szűrése

Azonos vagy csak záró perjelben eltérő link esetén a rendszer egyetlen hírt tart meg.

### Azonos című hírek szűrése

A címek kisbetűsítve és írásjelektől megtisztítva kerülnek összehasonlításra.

Azonos normalizált cím esetén csak egy hír marad meg.

### Közel azonos összefoglalók felismerése

A rendszer felismeri azokat a híreket is, amelyek címe eltér, de hosszabb összefoglalójuk azonos vagy csak rövid kiegészítésben különbözik.

A jelenlegi szabály szerint az összefoglalók akkor tekinthetők azonosnak, ha:

- a rövidebb összefoglaló legalább 80 karakteres;
- a rövidebb szöveg megtalálható a hosszabb szövegben;
- a rövidebb szöveg hossza legalább a hosszabb 80 százaléka.

Ez a szabály különböző források között és ugyanazon forráson belül is működik.

### Azonos forráson belüli duplikációszűrés

Korábban a szemantikai duplikációszűrés automatikusan kihagyta az azonos forrásból érkező hírek összehasonlítását.

A módosítás után az azonos vagy közel azonos, hosszabb összefoglalójú hírek ugyanazon forráson belül is összevonásra kerülnek.

Az eltérő tartalmú, ugyanazon forrásból érkező cikkeket a rendszer továbbra sem vonja össze a tágabb szemantikai szabályok alapján.

### Tartalmi duplikációszűrés

A különböző forrásokból érkező híreknél a rendszer vizsgálja:

- a címek közös kulcsszavait;
- a cím és összefoglaló közös kulcsszavait;
- a ritka és jellegzetes kifejezéseket;
- a tartalmi átfedés arányát;
- a publikálási idő közelségét;
- a forrás típusát.

A szemantikai összehasonlítás 72 órás időablakon belül történik.

### Forrásprioritás

Duplikáció esetén a megtartási prioritás:

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

A rendszer sikeresen felismerte és összevonta többek között:

- a három magyar szamócáról szóló hírt;
- a Velencei-tó alacsony vízállásáról szóló híreket;
- a lengyel cseresznyepiacról szóló híreket;
- az európai burgonya-termőterület csökkenéséről szóló híreket;
- az ukrán burgonyapiacról szóló FruitVeB- és Agrárszektor-hírt;
- az Agrofórum azonos kukoricás videó- és szakcikkváltozatát.

Az ukrán burgonyapiaci hírből a FruitVeB szakmai forrás maradt meg.

Az Agrofórum két azonos összefoglalójú kukoricás anyagából csak a frissebb változat maradt meg.

### Ellenőrzött futási eredmény

A legutóbbi ellenőrzött workflow-futás eredménye:

- hírek száma: 148;
- RSS-hibák száma: 0;
- `errors` lista: üres;
- a workflow zöld állapottal fejeződött be;
- az eredmény az élő oldalon is megjelent.

A hírek száma minden futásnál változhat az RSS-források aktuális tartalma és a duplikációszűrés eredménye alapján.

### Dokumentáció

Frissítésre került:

- `PROJECT_STATUS.md`
- `TODO.md`
- `CHANGELOG.md`

A dokumentációban rögzítésre került:

- a 12 aktív RSS-forrás;
- az automatikus RSS-újrapróbálás;
- a relevanciaszűrés;
- a cím- és összefoglaló-tisztítás;
- a KAP-portál speciális tisztítása;
- az azonos forráson belüli duplikációszűrés;
- az ellenőrzött futási eredmény.

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
