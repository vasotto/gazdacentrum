# GazdaCentrum – projektállapot

Utolsó frissítés: 2026. július 19.

## 1. A projekt célja

A GazdaCentrum.hu teljesen vagy közel teljesen automatizált magyar agrár hírgyűjtő és gazdálkodói információs portál.

A rendszer célja:

- agrárhírek automatikus gyűjtése jogszerű RSS-, API- vagy más strukturált forrásból;
- a hírek kategorizálása;
- az azonos vagy nagyon hasonló hírek felismerése és összevonása;
- a nyilvánvalóan nem agrár témájú tartalmak kiszűrése;
- a forrás, publikálási idő és eredeti cikklink megjelenítése;
- stabil, alacsony költségű és minimális kézi munkát igénylő működés.

## 2. Infrastruktúra

### Domain

Aktív domainek:

- gazdacentrum.hu
- www.gazdacentrum.hu

Domainregisztrátor:

- WWH.hu

Mindkét domain működik HTTPS-en.

### DNS, CDN és SSL

Szolgáltató:

- Cloudflare

Állapot:

- a Cloudflare-névszerverek aktívak;
- a DNS-kezelés a Cloudflare-ben történik;
- az SSL működik;
- a fődomain és a www aldomain is elérhető.

Fontos DNS-rekordok, amelyeket védeni kell:

- MX;
- SPF;
- DKIM;
- DMARC;
- Google és más szolgáltatások igazoló TXT rekordjai.

DNS-módosítás előtt ezeket a rekordokat minden esetben ellenőrizni kell.

### Hosting

- Cloudflare Pages
- a production oldal automatikusan a GitHub `main` ágából deployolódik.

### GitHub

Felhasználó:

- vasotto

Repository:

- gazdacentrum

Production branch:

- main

A Cloudflare Pages minden `main` ágra kerülő commit után automatikusan új deployt indít.

## 3. Jelenlegi működési folyamat

    sources.csv
    → fetch_news.py
    → news.json
    → index.html
    → Cloudflare Pages
    → gazdacentrum.hu

A GitHub Actions rendszer hatóránként automatikusan lefuttatja a hírfrissítést.

## 4. Fontos repository-fájlok

### index.html

Feladata:

- a weboldal megjelenítése;
- a GazdaCentrum logó megjelenítése;
- a `news.json` betöltése JavaScripttel;
- a hírek kártyás megjelenítése;
- a forrás, kategória, publikálási idő és eredeti link megjelenítése.

### gazdacentrum_logo.png

A GazdaCentrum weboldalon használt logó.

### sources.csv

Az aktív RSS-forrásokat, kategóriákat és forrástípusokat tartalmazza.

Oszlopai:

- `name`
- `rss_url`
- `category`
- `type`

## 5. Jelenlegi aktív RSS-források

Jelenleg 13 aktív forrás szerepel a `sources.csv` fájlban.

### 1. Agrárszektor

RSS:

- https://www.agrarszektor.hu/rss

Kategória:

- Agrárgazdaság

Forrástípus:

- portál

### 2. Agro Napló

RSS:

- https://www.agronaplo.hu/rss

Kategória:

- Általános agrár

Forrástípus:

- portál

### 3. Magyar Mezőgazdaság

RSS:

- https://magyarmezogazdasag.hu/feed/

Kategória:

- Általános agrár

Forrástípus:

- portál

### 4. Mezőhír

RSS:

- https://mezohir.hu/feed/

Kategória:

- Általános agrár

Forrástípus:

- portál

### 5. Agrofórum

RSS:

- https://agroforum.hu/feed/

Kategória:

- Általános agrár

Forrástípus:

- portál

### 6. AKI

RSS:

- https://www.aki.gov.hu/feed/

Kategória:

- Agrárgazdaság

Forrástípus:

- hivatalos

### 7. ÖMKi

RSS:

- https://biokutatas.hu/feed/

Kategória:

- Ökológiai gazdálkodás

Forrástípus:

- szakmai

### 8. FruitVeB

RSS:

- https://fruitveb.hu/feed/

Kategória:

- Kertészet

Forrástípus:

- szakmai

### 9. Agrárközösség

RSS:

- https://agrarkozosseg.hu/feed/

Kategória:

- Általános agrár

Forrástípus:

- portál

### 10. Agroinform

RSS:

- https://www.agroinform.hu/rss

Kategória:

- Általános agrár

Forrástípus:

- portál

### 11. Phylazonit

RSS:

- https://phylazonit.hu/feed/

Kategória:

- Általános agrár, automatikus tartalmi kategorizálással

Forrástípus:

- ceges

Megjelenítés:

- külön „Céges és partneri szakmai tartalmak” rovatban;
- „Céges szakmai tartalom” jelöléssel;
- a független agrárhírfolyamtól elkülönítve.

### 12. Magtár Kft.

RSS:

- https://magtarkft.hu/feed/

Kategória:

- Mezőgazdasági gépek, automatikus tartalmi kategorizálással

Forrástípus:

- ceges

Megjelenítés:

- külön „Céges és partneri szakmai tartalmak” rovatban;
- külön „Magtár Kft.” választógomb mögött;
- „Céges szakmai tartalom” jelöléssel;
- az `AKCIÓK` RSS-kategóriájú bejegyzések automatikus kizárásával.

### 13. KAP portál

RSS:

- https://kap.gov.hu/rss.xml

Kategória:

- Támogatások és pályázatok

Forrástípus:

- hivatalos

A felsorolt forrásokból a hírek bekerülnek a `news.json` fájlba. A `ceges` és `partneri` típusú elemek ugyanebben az adatfájlban szerepelnek, de az `index.html` külön rovatban jeleníti meg őket.

A legutóbbi ellenőrzött workflow-futás hibamentesen fejeződött be.

## 6. fetch_news.py

A `fetch_news.py` végzi a teljes automatikus RSS-feldolgozást.

Fő feladatai:

- a `sources.csv` beolvasása;
- az RSS-források lekérése;
- a cím, link, dátum, forrás és összefoglaló feldolgozása;
- a hírek egységes adatszerkezetbe rendezése;
- a nyilvánvalóan nem releváns hírek kiszűrése;
- a duplikációk felismerése;
- a `news.json` elkészítése.

### RSS-lekérés

Egy RSS-forrás lekérése legfeljebb háromszor történik meg.

Beállítások:

- maximális próbálkozások száma: 3;
- két próbálkozás közötti várakozás: 5 másodperc.

Ha egy forrás mindhárom alkalommal sikertelen, a hiba bekerül a `news.json` `errors` mezőjébe, a többi forrás feldolgozása pedig folytatódik.

### Feldolgozási korlátok

- forrásonként legfeljebb 20 hír kerül feldolgozásra;
- a végleges `news.json` legfeljebb 200 hírt tartalmaz;
- a tartalmi duplikációszűrés időablaka 72 óra.

### Szövegtisztítás

A program:

- eltávolítja a HTML-elemeket;
- dekódolja a HTML-karaktereket;
- megszünteti a felesleges szóközöket;
- korlátozza a cím és az összefoglaló hosszát;
- eltávolítja az RSS-ben ismétlődő zárószövegeket;
- eltávolítja az „appeared first on” típusú kiegészítéseket;
- eltávolítja a magyar „bejegyzés először ... jelent meg” zárószövegeket.

### Duplán érkező címek tisztítása

Egyes RSS-források ugyanazt a címet kétszer egymás után adják át.

A `clean_title()` függvény felismeri és eltávolítja az ilyen ismétlődést.

Ez különösen az Agroinform egyes híreinél jelentkezett.

### KAP-portál összefoglalóinak tisztítása

A KAP-portál RSS-összefoglalói korábban tartalmazták az ismétlődő:

- szerkesztői nevet;
- dátumot;
- időpontot.

A `clean_kap_summary()` függvény ezt a fejlécet eltávolítja.

## 7. Relevanciaszűrés

A rendszer forrás- és linkfüggő szabályokkal kiszűri a nyilvánvalóan nem agrár témájú híreket.

Jelenlegi fő szabályok:

- ismert, nem releváns címkifejezések kizárása;
- az Agroinform Házikert rovatának kizárása;
- az Agrofórum hobbikerti és lakossági szaktanácsadási rovatainak kizárása;

A relevanciaszűrés célja nem minden határeset automatikus eldöntése, hanem a nyilvánvalóan idegen témájú tartalmak eltávolítása.

## 8. Duplikációszűrés

A rendszer több szinten szűri az ismétlődő híreket.

### Azonos link

Azonos vagy csak záró perjelben eltérő link esetén csak egy hír marad meg.

### Azonos cím

Az írásjelektől megtisztított, kisbetűsített azonos címekből csak egy marad meg.

### Azonos vagy közel azonos összefoglaló

Ha két, legalább 80 karakteres összefoglaló:

- teljesen azonos; vagy
- az egyik a másikban megtalálható;
- és a rövidebb összefoglaló hossza legalább a hosszabb 80 százaléka,

akkor a rendszer azonos hírnek tekinti őket.

Ez a szabály ugyanazon forrás eltérő URL-en megjelenő másodpéldányaira is működik.

### Tartalmi hasonlóság

Különböző források híreinél a rendszer vizsgálja:

- a cím kulcsszavait;
- a cím és összefoglaló közös kulcsszavait;
- a ritkább, jellegzetes szavakat;
- a tartalmi átfedés arányát;
- a publikálási idő különbségét.

A szemantikai összehasonlítás 72 órás időablakon belül történik.

### Láncolt duplikációk

A rendszer a már kihagyott duplikátumokat is megtartja összehasonlítási alapként.

Ez lehetővé teszi az olyan hírláncok felismerését, ahol:

- az A hír hasonlít a B hírre;
- a B hír hasonlít a C hírre;
- de az A és C címében kisebb az egyezés.

### Forrásprioritás

A megtartandó hír kiválasztásánál a rendszer a következő prioritást használja:

    hivatalos
    → szakmai
    → portál

Azonos forrástípus esetén a frissebb publikálási idő kap előnyt.

## 9. Ellenőrzött duplikációs példák

A rendszer sikeresen felismerte és összevonta többek között:

- a három, magyar szamócáról szóló hírt;
- a Velencei-tó alacsony vízállásáról szóló híreket;
- a lengyel cseresznyepiacról szóló híreket;
- az európai burgonya-termőterület csökkenéséről szóló híreket;
- az ukrán burgonyapiacról szóló FruitVeB- és Agrárszektor-hírt;
- az Agrofórum azonos kukoricás videó- és szakcikkváltozatát.

Az ukrán burgonyapiaci hírből a FruitVeB szakmai forrás maradt meg.

Az Agrofórum két azonos összefoglalójú kukoricás anyagából csak a frissebb maradt meg.

## 10. news.json

A weboldalon megjelenő hírek adatfájlja.

Tartalmazza:

- a generálás időpontját;
- a hírek számát;
- a hírek címét;
- az eredeti linket;
- az RSS-összefoglalót;
- a forrás nevét;
- a kategóriát;
- a forrás típusát;
- a publikálási időt;
- a feldolgozási hibákat.

A legutóbbi ellenőrzött futás eredménye:

- hírek száma: 148;
- RSS-hibák száma: 0;
- `errors` lista: üres.

A hírek száma minden futásnál változhat az RSS-források aktuális tartalma és a duplikációszűrés eredménye alapján.

## 11. requirements.txt

Jelenlegi Python-függőség:

    feedparser==6.0.12

## 12. GitHub Actions

Workflow-fájl:

    .github/workflows/update-news.yml

Workflow neve:

- Agrárhírek frissítése

Működése:

- kézzel elindítható;
- hatóránként automatikusan fut;
- telepíti a Python-függőségeket;
- lefuttatja a `fetch_news.py` programot;
- frissíti a `news.json` fájlt;
- a változást automatikusan visszamenti a `main` ágra.

## 13. Jelenleg működő funkciók

- a `gazdacentrum.hu` elérhető;
- a `www.gazdacentrum.hu` elérhető;
- HTTPS működik;
- a GitHub és a Cloudflare Pages kapcsolata működik;
- az automatikus deploy működik;
- a GitHub Actions kézzel és automatikusan is futtatható;
- 13 RSS-forrás hírei kerülnek feldolgozásra;
- sikertelen RSS-lekérésnél automatikus újrapróbálkozás történik;
- a `news.json` automatikusan elkészül;
- a hírek megjelennek a weboldalon;
- az ismétlődő RSS-címek megtisztításra kerülnek;
- a felesleges RSS-zárószövegek eltávolításra kerülnek;
- a KAP-portál összefoglalói megtisztításra kerülnek;
- a nyilvánvalóan nem releváns hírek kiszűrésre kerülnek;
- az azonos linkű hírek kiszűrésre kerülnek;
- az azonos című hírek kiszűrésre kerülnek;
- az azonos és közel azonos összefoglalójú hírek kiszűrésre kerülnek;
- azonos forráson belüli másodpéldányok is kiszűrésre kerülnek;
- a különböző források hasonló tartalmú hírei összevonásra kerülnek;
- a láncoltan kapcsolódó duplikációk is felismerhetők.

A híreknél jelenleg látható:

- kategória;
- cím;
- forrás;
- forrástípus;
- publikálási idő;
- az eredeti cikk linkje.

A céges rovat alapállapotban nem jelenít meg cikkeket; előbb a Phylazonit vagy a Magtár Kft. választógombjára kell kattintani.

Az RSS-összefoglaló csak belső relevanciaszűrésre, kategorizálásra és duplikációvizsgálatra használható; a nyilvános `news.json` fájlba nem kerül bele.

## 14. Tesztelt, de jelenleg inaktív források

### GÉPmax

Tesztelt feed:

- https://gepmax.hu/feed/

Státusz:

- inaktív;
- a forrás a hírek linkelését tiltja, ezért nem szerepel a `sources.csv` fájlban.

### Agrárágazat

Tesztelt feed:

- https://agraragazat.hu/feed/

Hiba:

- `undefined entity`

A forrás eltávolításra került a `sources.csv` fájlból.

### Agrotrend

Tesztelt feed:

- https://agrotrend.hu/feed/

Hiba:

- `undefined entity`

A forrás eltávolításra került a `sources.csv` fájlból.

### AgrárUnió

Tesztelt címek:

- https://www.agrarunio.hu/feed/
- https://www.agrarunio.hu/hirek?format=feed&type=rss

Nem találtunk működő nyilvános RSS-feedet.

### Agrokép

Tesztelt feed:

- https://agrokep.vg.hu/feed/

A végpont válasza:

- `feed not found or disabled`
- HTTP-státusz: 400

Az oldal hírei nem frissek, ezért jelenleg nem használjuk forrásként.

### Haszon Agrár

A tesztelt feed hibát adott, ezért nem maradt az aktív források között.

### MAGRO

A tesztelt feed hibát adott, ezért nem maradt az aktív források között.

### Farmvilág

A tesztelt feed hibát adott, ezért nem maradt az aktív források között.

## 15. Átmeneti RSS-hibák

Korábban előfordult:

- ÖMKi kapcsolódási időtúllépés;
- Agrárközösség `mismatched tag` XML-hiba.

Mindkét hiba eltűnt az ismételt lekérés után.

A program jelenleg automatikusan legfeljebb háromszor próbálkozik egy RSS-forrás lekérésével.

Egyetlen forrás hibája nem állítja le a többi forrás feldolgozását.

## 16. Tartalmi és jogi működés

Jelenlegi alapelvek:

- teljes külső cikket nem veszünk át;
- külső képet nem töltünk le automatikusan;
- minden hírnél megjelenik a forrás;
- minden hírnél megjelenik az eredeti cikk linkje;
- elsődlegesen RSS-, API- vagy más engedélyezett strukturált forrást használunk;
- scraping csak külön jogi és technikai vizsgálat után alkalmazható;
- az összefoglaló nem torzíthatja az eredeti hírt;
- az oldalon jelezni kell az automatizált tartalom-előállítást.

Támogatási, jogszabályi, pénzügyi és növényvédelmi híreknél az eredeti hivatalos forrás ellenőrzése szükséges.

A céges és partneri források csak dokumentált hozzájárulással vagy saját tartalomként kapcsolhatók be. Ezek külön rovatban, egyértelmű „Céges szakmai tartalom” vagy „Partneri szakmai tartalom” jelöléssel jelennek meg. A Phylazonit és a Magtár Kft. az aktív `ceges` típusú források. A céges rovatban vállalatonként külön választógomb jelenik meg, és a cikklista csak egy vállalat kiválasztása után töltődik be.

## 17. Facebook

A korábbi Zetorvas Facebook-oldal neve már GazdaCentrum.

Jelenlegi URL:

- facebook.com/zetorvas

A Facebook-link egyelőre nincs kitéve a weboldalra.

Csak akkor kerülhet ki, amikor sikerült a végleges felhasználónevet beállítani, például:

- gazdacentrum;
- gazdacentrum.hu;
- gazdacentrumhu.

## 18. Ismert korlátozások

- egyes szakosított források kategóriája továbbra is forrásszinten van megadva;
- az automatikus kategorizálás heurisztikus, ezért időszakos kézi ellenőrzést igényel;
- a tartalmi duplikációszűrés heurisztikus, ezért folyamatos ellenőrzést igényel;
- egyes rövid vagy általános összefoglalójú duplikációkat a rendszer nem feltétlenül ismer fel;
- egyes, azonos témájú, de eltérő információt tartalmazó hírek szándékosan külön maradnak;
- nincsenek külön kategóriaoldalak;
- nincs kereső;
- nincs hírlevél;
- nincs AI-alapú saját összefoglaló;
- nincs „Miért fontos?” mező;

## 19. Következő konkrét feladat

A jelenlegi források felhasználási feltételeinek forrásonkénti dokumentálása. A nyilvántartásban külön szerepeljen a címátvétel, linkelés, dátum, kivonat, hozzájárulási igény, bizonyíték URL-je és a végleges használati döntés.
