# GazdaCentrum – projektállapot

Utolsó frissítés: 2026. július 16.

## 1. A projekt célja

A GazdaCentrum.hu teljesen vagy közel teljesen automatizált magyar agrár hírgyűjtő és gazdálkodói információs portál.

A rendszer célja:

- agrárhírek automatikus gyűjtése;
- a hírek kategorizálása;
- az azonos vagy nagyon hasonló hírek összevonása;
- a forrás, publikálási idő és eredeti cikklink megjelenítése;
- stabil, alacsony költségű és minimális kézi munkát igénylő működés.

## 2. Infrastruktúra

### Domain

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

    RSS-források
    → fetch_news.py
    → news.json
    → index.html
    → Cloudflare Pages
    → gazdacentrum.hu

## 4. Fontos repository-fájlok

### index.html

Feladata:

- a weboldal megjelenítése;
- a GazdaCentrum logó megjelenítése;
- a `news.json` betöltése JavaScripttel;
- a hírek kártyás megjelenítése.

### gazdacentrum_logo.png

A GazdaCentrum weboldalon használt logó.

### sources.csv

Az aktív RSS-forrásokat tartalmazza.

Jelenlegi aktív források:

1. Agrárszektor  
   https://www.agrarszektor.hu/rss

2. Agro Napló  
   https://www.agronaplo.hu/rss

3. Magyar Mezőgazdaság  
   https://magyarmezogazdasag.hu/feed/

4. Mezőhír  
   https://mezohir.hu/feed/

5. Agrofórum  
   https://agroforum.hu/feed/

6. AKI  
   https://www.aki.gov.hu/feed/

7. ÖMKi  
   https://biokutatas.hu/feed/

8. FruitVeB  
   https://fruitveb.hu/feed/

9. Agrárközösség  
   https://agrarkozosseg.hu/feed/

A felsorolt forrásokból a hírek bekerülnek a `news.json` fájlba.

A legutóbbi ellenőrző workflow-futás hibamentesen fejeződött be.

### fetch_news.py

Feladata:

- a `sources.csv` beolvasása;
- az RSS-források lekérése;
- a cím, link, dátum, forrás és rövid összefoglaló feldolgozása;
- a HTML-elemek eltávolítása;
- a felesleges RSS-zárószövegek eltávolítása;
- az azonos linkű és című hírek kiszűrése;
- a hasonló tartalmú hírek felismerése;
- a láncoltan kapcsolódó duplikációk felismerése;
- a `news.json` elkészítése.

A duplikációszűrés a források között prioritást alkalmaz:

    hivatalos
    → szakmai
    → portál

Azonos forrástípus esetén a frissebb publikálási idő kap előnyt.

### requirements.txt

Jelenlegi Python-függőség:

    feedparser==6.0.12

### news.json

A weboldalon megjelenő hírek adatfájlja.

Tartalmazza többek között:

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

### .github/workflows/update-news.yml

GitHub Actions workflow neve:

- Agrárhírek frissítése

Működése:

- kézzel elindítható;
- hatóránként automatikusan fut;
- telepíti a Python-függőségeket;
- lefuttatja a `fetch_news.py` programot;
- frissíti a `news.json` fájlt;
- a változást automatikusan visszamenti a `main` ágra.

## 5. Jelenleg működő funkciók

- a `gazdacentrum.hu` elérhető;
- a `www.gazdacentrum.hu` elérhető;
- HTTPS működik;
- a GitHub és a Cloudflare Pages kapcsolata működik;
- az automatikus deploy működik;
- a GitHub Actions sikeresen lefut;
- kilenc RSS-forrás hírei kerülnek feldolgozásra;
- a `news.json` automatikusan elkészül;
- a hírek megjelennek a weboldalon;
- az azonos linkű hírek kiszűrésre kerülnek;
- az azonos című hírek kiszűrésre kerülnek;
- a hasonló tartalmú hírek összevonásra kerülnek;
- a láncoltan kapcsolódó duplikációk is felismerhetők;
- az RSS-ben található felesleges „appeared first on” szövegek eltávolításra kerülnek.

A híreknél jelenleg látható:

- kategória;
- cím;
- forrás;
- publikálási idő;
- rövid RSS-összefoglaló;
- az eredeti cikk linkje.

## 6. Ellenőrzött duplikációs példák

A rendszer sikeresen összevonta:

- a három, magyar szamócáról szóló hírt;
- a Velencei-tó alacsony vízállásáról szóló híreket;
- a lengyel cseresznyepiacról szóló híreket;
- az európai burgonya-termőterület csökkenéséről szóló híreket;
- az azonos bolti élelmiszertrenddel foglalkozó híreket.

A szamócás híreknél a FruitVeB szakmai forrás maradt meg az Agro Napló és az Agrárszektor változata helyett.

## 7. Tesztelt, de jelenleg inaktív források

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

## 8. Átmeneti RSS-hibák

Az ÖMKi feedjénél egyszer kapcsolódási időtúllépés jelentkezett.

Az Agrárközösség feedjénél egyszer `mismatched tag` XML-hiba jelentkezett.

Mindkét hiba eltűnt az ismételt workflow-futtatás után, ezért a források aktívak maradtak.

Jelenleg nincs automatikus újrapróbálkozás a `fetch_news.py` fájlban.

## 9. Tartalmi és jogi működés

Jelenlegi alapelvek:

- teljes külső cikket nem veszünk át;
- külső képet nem töltünk le automatikusan;
- minden hírnél megjelenik a forrás;
- minden hírnél megjelenik az eredeti cikk linkje;
- elsődlegesen RSS-, API- vagy más engedélyezett strukturált forrást használunk;
- az oldalon jelezni kell az automatizált tartalom-előállítást.

Támogatási, jogszabályi, pénzügyi és növényvédelmi híreknél az eredeti hivatalos forrás ellenőrzése szükséges.

Fizetett vállalati források később bevonhatók, de ezeket egyértelműen például „Fizetett partneri tartalom” jelöléssel kell elkülöníteni.

## 10. Facebook

A korábbi Zetorvas Facebook-oldal neve már GazdaCentrum.

Jelenlegi URL:

- facebook.com/zetorvas

A Facebook-link egyelőre nincs kitéve a weboldalra.

Csak akkor kerül ki, amikor sikerült a végleges felhasználónevet beállítani, például:

- gazdacentrum;
- gazdacentrum.hu;
- gazdacentrumhu.

## 11. Ismert korlátozások

- a kategória több forrásnál még forrásszinten van megadva;
- a tartalmi duplikációszűrés heurisztikus, ezért folyamatos ellenőrzést igényel;
- nincs automatikus újrapróbálkozás az átmeneti RSS-hibáknál;
- nincs kategóriaszűrés;
- nincsenek külön kategóriaoldalak;
- nincs kereső;
- nincs hírlevél;
- nincs AI-alapú saját összefoglaló;
- nincs „Miért fontos?” mező;
- az impresszum és az adatkezelési tájékoztató még nem készült el;
- a fizetett partneri tartalmak technikai elkülönítése még nincs kialakítva.

## 12. Következő konkrét feladat

A következő feladat az Agroinform működő RSS-feedjének megkeresése és tesztelése.

Sikeres Agroinform-teszt után külön ellenőrizzük a Phylazonit RSS-feedet:

- https://phylazonit.hu/feed/

A vállalati forrást csak megfelelő, egyértelmű vállalati vagy partneri jelöléssel szabad később megjeleníteni.
