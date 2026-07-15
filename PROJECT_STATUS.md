# GazdaCentrum – projektállapot

Utolsó frissítés: 2026. július 15.

## 1. A projekt célja

A GazdaCentrum.hu teljesen vagy közel teljesen automatizált magyar agrár hírgyűjtő és gazdálkodói információs portál.

A rendszer célja:

- agrárhírek automatikus gyűjtése;
- a hírek kategorizálása;
- az ismétlődő hírek kiszűrése;
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

- Agrárszektor  
  https://www.agrarszektor.hu/rss

- Agro Napló  
  https://www.agronaplo.hu/rss

Mindkét RSS-forrás sikeresen tesztelve lett.

### fetch_news.py

Feladata:

- a `sources.csv` beolvasása;
- az RSS-források lekérése;
- a cím, link, dátum, forrás és rövid összefoglaló feldolgozása;
- az azonos linkek és címek alapvető kiszűrése;
- a `news.json` elkészítése.

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

### PROJECT_STATUS.md

Az aktuális technikai és működési projektállapotot tartalmazza.

### TODO.md

A következő és későbbi fejlesztési feladatokat tartalmazza.

### CHANGELOG.md

A projekt jelentősebb módosításait és mérföldköveit tartalmazza.

### README.md

A projekt rövid bemutatását, technikai felépítését és fő fájljait ismerteti.

## 5. Jelenleg működő funkciók

- a `gazdacentrum.hu` elérhető;
- a `www.gazdacentrum.hu` elérhető;
- HTTPS működik;
- a GitHub és a Cloudflare Pages kapcsolata működik;
- az automatikus deploy működik;
- a GitHub Actions sikeresen lefut;
- az Agrárszektor RSS-feedje működik;
- az Agro Napló RSS-feedje működik;
- a `news.json` automatikusan elkészül;
- a hírek megjelennek a weboldalon.

A híreknél jelenleg látható:

- kategória;
- cím;
- forrás;
- publikálási idő;
- rövid RSS-összefoglaló;
- az eredeti cikk linkje.

## 6. Tartalmi és jogi működés

Jelenlegi alapelvek:

- teljes külső cikket nem veszünk át;
- külső képet nem töltünk le automatikusan;
- minden hírnél megjelenik a forrás;
- minden hírnél megjelenik az eredeti cikk linkje;
- elsődlegesen RSS-, API- vagy más engedélyezett strukturált forrást használunk;
- az oldalon jelezni kell az automatizált tartalom-előállítást.

Támogatási, jogszabályi, pénzügyi és növényvédelmi híreknél az eredeti hivatalos forrás ellenőrzése szükséges.

## 7. Facebook

A korábbi Zetorvas Facebook-oldal neve már GazdaCentrum.

Jelenlegi URL:

- facebook.com/zetorvas

A Facebook-link egyelőre nincs kitéve a weboldalra.

Csak akkor kerül ki, amikor sikerült a végleges felhasználónevet beállítani, például:

- gazdacentrum;
- gazdacentrum.hu;
- gazdacentrumhu.

## 8. Ismert hibák és korlátozások

Jelenleg nincs ismert, az élő oldal működését akadályozó hiba.

Jelenlegi korlátozások:

- jelenleg két aktív RSS-forrás van;
- a kategória jelenleg forrásszinten van megadva;
- a duplikációszűrés csak azonos link és azonos cím alapján működik;
- nincs még kategóriaszűrés;
- nincsenek külön kategóriaoldalak;
- nincs még hírlevél;
- nincs AI-alapú saját összefoglaló;
- nincs „Miért fontos?” mező;
- az impresszum és az adatkezelési tájékoztató még nem készült el.

## 9. Következő konkrét feladat

A következő feladat:

- egy új magyar agrár RSS-forrás kiválasztása;
- az RSS működésének ellenőrzése;
- a dátumok, linkek és kivonatok vizsgálata;
- csak sikeres teszt után a forrás felvétele a `sources.csv` fájlba.

Az új forrásokat egyenként teszteljük.
