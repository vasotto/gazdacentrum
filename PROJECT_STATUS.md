# GazdaCentrum – projektállapot

Utolsó frissítés: 2026. július 20.

## 1. Projektcél

A GazdaCentrum.hu automatizált magyar agrár hírgyűjtő, pályázatfigyelő és gazdálkodói információs portál.

Fő funkciók:

- agrárhírek gyűjtése RSS-ből és más jogszerű strukturált forrásból;
- kategorizálás és duplikációszűrés;
- forrás, dátum és eredeti link megjelenítése;
- hivatalos pályázati adatok és határidők rendszerezése;
- közérthető, ellenőrzött részletes pályázati összefoglalók;
- céges és partneri tartalmak külön kezelése.

## 2. Infrastruktúra

- Domain: `gazdacentrum.hu`, `www.gazdacentrum.hu`
- Regisztrátor: WWH.hu
- DNS, CDN, SSL: Cloudflare
- Hosting: Cloudflare Pages
- GitHub: `vasotto/gazdacentrum`
- Production branch: `main`
- Deploy: automatikus minden `main` commit után

DNS-módosításnál az MX-, SPF-, DKIM-, DMARC- és igazoló TXT-rekordokat védeni kell.

## 3. Hírfrissítési folyamat

```text
sources.csv
→ fetch_news.py
→ news.json
→ index.html
→ Cloudflare Pages
```

A GitHub Actions workflow kézzel és hatóránként automatikusan fut. A workflow csak a `news.json` fájlt commitolja vissza.

## 4. Aktív RSS-források

Jelenleg 12 aktív forrás van:

1. Agrárszektor – portál
2. Agro Napló – portál
3. Magyar Mezőgazdaság – portál
4. Mezőhír – portál
5. Agrofórum – portál
6. AKI – hivatalos
7. ÖMKi – szakmai
8. FruitVeB – szakmai
9. Agroinform – portál
10. Phylazonit – ceges
11. Magtár Kft. – ceges
12. KAP portál – hivatalos

Az Agrárközösség ideiglenesen inaktív, mert a feed ellenőrzőoldalt vagy feldolgozhatatlan XML-választ adott.

## 5. Híradat és kategorizálás

A legutóbbi repositoryban található `news.json`:

- generálva: 2026. július 20.;
- hírek száma: 148;
- RSS-hibák: 0;
- aktív források: 12.

Kategóriaeloszlás:

- Általános agrár: 39;
- Kertészet: 25;
- Agrárgazdaság: 18;
- Növénytermesztés: 14;
- Időjárás és vízgazdálkodás: 13;
- Ökológiai gazdálkodás: 12;
- Támogatások és pályázatok: 10;
- Gépesítés: 9;
- Állattenyésztés: 7;
- Növényvédelem: 1.

A 9 gépesítési hír jelenleg mind a Magtár Kft. elkülönített céges rovatában található. Emiatt a főoldali `Gépesítés` kártya most partneri tartalomhoz irányít, ha nincs független gépes hír.

## 6. fetch_news.py állapota

A program:

- UTF-8 BOM-os `sources.csv` fájlt is kezel;
- forrásonként legfeljebb három lekérési kísérletet végez;
- forrásonként legfeljebb 20 elemet dolgoz fel;
- legfeljebb 200 hírt ír a `news.json` fájlba;
- eltávolítja a HTML-t és a felesleges RSS-zárószövegeket;
- nem teszi nyilvánossá az RSS-összefoglalót;
- kiszűri az Agro Napló `(x)` tartalmait;
- kiszűri a Magtár `AKCIÓK` kategóriáját;
- URL-, cím-, összefoglaló- és RSS-kategória-jeleket használ;
- egységesíti a `Mezőgazdasági gépek` megnevezést `Gépesítés` kategóriára;
- kezeli az azonos és tartalmilag hasonló híreket;
- hivatalos → szakmai → portál prioritást alkalmaz.

## 7. Főoldal

Működő elemek:

- mobilbarát felső navigáció;
- minden nyilvános oldalon automatikusan megjelenő, középre igazított vissza-a-tetejére gomb hosszabb görgetés után;
- kategóriakártyák és kategóriaszűrők;
- `Teendők és határidők` kiemelt nézet;
- friss független agrárhírek;
- külön céges és partneri rovat;
- Phylazonit- és Magtár-választógomb;
- határidők megjelenítése;
- pályázati listaoldalra vezető link;
- világos és sötét mód;
- automatizált feldolgozásról szóló tájékoztatás.

A `Gépesítés` kategóriakártya már akkor is működik, ha az adott kategóriában csak céges tartalom van: ilyenkor a külön partneri részhez navigál és kiválasztja az érintett céget.

## 8. Céges tartalmak

A céges tartalom:

- nem keveredik a független hírekkel;
- alapállapotban nincs megnyitva;
- vállalatonként választható;
- egyértelmű jelölést kap;
- teljes cikket, kivonatot és külső képet nem vesz át.

Aktív céges források:

- Phylazonit;
- Magtár Kft.

## 9. Határidők

A `deadlines.json` 5 rekordot tartalmaz:

- KAP-RD46-1-25 – 5. benyújtási szakasz;
- KAP-RD46-1-25 – 6. benyújtási szakasz;
- KAP-RD38-RD39-1-25 – 5. benyújtási szakasz;
- KAP-RD38-RD39-1-25 – 6. benyújtási szakasz;
- 70/2026. IH – relatív kifizetési kötelezettség.

A két RD46 szakasz külön rekordként szerepel, ezért a főoldali határidőlista pontosabban tükrözi a hivatalos beadási időszakokat.

## 10. Pályázati rendszer

### grants.json

A fájl 2 pályázatot és 12 benyújtási szakaszt tartalmaz.

Mindkét pályázat:

- programállapota aktív;
- 2026. július 20-án két beadási szakasz között van;
- közvetlen részletes adatlap-URL-lel rendelkezik;
- hivatalos forrásellenőrzést igényel.

### Pályázati listaoldal

URL:

```text
https://gazdacentrum.hu/palyazatok.html
```

Funkciók:

- 2 pályázat;
- 12 benyújtási szakasz;
- lejárt szakaszok szürke jelölése;
- nyitott szakasz zöld jelölése;
- jövőbeli szakasz lila jelölése;
- hivatalos pályázati link;
- mindkét pályázatnál részletes összefoglaló gomb.

### Részletes pályázati adatlapok

1. `palyazat-kap-rd46-1-25.html`
   - minimum pontszám: 20;
   - maximum támogatás: 13 000 euró / 5 év;
   - következő szakasz: 2026. október 1–14.

2. `palyazat-kap-rd38-rd39-1-25.html`
   - minimum pontszám: 30;
   - minimum terület: 0,5 ha;
   - következő szakasz: 2026. október 7. – november 4.

Mindkét oldal mobilbarát, sötét módot támogat, és közvetlen hivatalos dokumentumlinkeket tartalmaz.

### Pályázati adatlap-szabvány

A `PALYAZATI_ADATLAP_SABLON.md` rögzíti:

- a kötelező adatmezőket;
- a jogosultság, STÉ, pontozás és intenzitás kezelését;
- a támogatható és kizárt tevékenységeket;
- a buktatók bemutatását;
- a hivatalos adat és a GazdaCentrum-értelmezés elkülönítését;
- az AI használatának emberi ellenőrzési szabályait.

## 11. Impresszum

Az `impresszum.html` tartalmazza:

- az üzemeltető jelenleg ismert adatait;
- a tárhelyszolgáltatót;
- a szolgáltatás jellegét;
- az automatizált hírfeldolgozásra vonatkozó tájékoztatást;
- a hivatalos forrás ellenőrzésének szükségességét.

Nyitott feladat:

- adószám pótlása;
- egyéni vállalkozói nyilvántartási szám pótlása;
- külön adatkezelési tájékoztató elkészítése.

## 12. Forrásaudit és jogi kockázat

A `SOURCE_AUDIT.md` alapján:

- Mezőhír – csak engedéllyel;
- AKI – csak engedéllyel;
- Agroinform – csak engedéllyel;
- több további forrásnál írásos pontosítás ajánlott;
- Phylazonit és Magtár Kft. céges pilotként használható, írásos partneri megerősítés szükséges;
- KAP portál korlátozott hivatalos adatokkal használható.

A technikai működés nem helyettesíti a felhasználási engedélyek rendezését.

## 13. Ismert korlátozások

- a kategorizálás heurisztikus;
- a duplikációszűrés heurisztikus;
- nincs külön kategóriaoldal;
- nincs kereső;
- nincs hírlevél;
- a pályázatok frissítése még kézi;
- nincs automatikus dokumentumverzió-figyelés;
- nincs jogosultsági vagy pontszám-előbecslő;
- a forrásengedélyek rendezése nem teljes;
- nincs külön adatkezelési tájékoztató.

## 14. Következő konkrét feladat

Döntés a Mezőhír, AKI és Agroinform átmeneti kikapcsolásáról vagy az írásos engedélykérések azonnali elindításáról.
