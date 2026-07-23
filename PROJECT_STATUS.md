# GazdaCentrum – projektállapot

Utolsó frissítés: 2026. július 23.

## 1. Projektcél és aktuális fő irány

A GazdaCentrum.hu automatizált magyar agrárinformációs portál. A jelenlegi elsődleges fejlesztési irány az **Agrárhatáridők és teendők** funkció.

A fő felhasználói kérdés:

> Mivel kell most foglalkoznom, és mennyi időm van rá?

A rendszer célja:

- hivatalos agrárhatáridők, kötelezettségek és pályázati időszakok gyűjtése;
- a teendő, az érintettek, a dátum és a hivatalos forrás közérthető megjelenítése;
- agrárhírek jogszerű gyűjtése RSS-ből, API-ból vagy engedélyezett forrásból;
- egyszerű HTML-, JavaScript-, JSON- és Python-alapú, kevés kézi munkát igénylő működés.

A havi naptárnézetet elvetettük. A cél egy szűrhető, időrendi teendőlista.

## 2. Infrastruktúra

- Domain: `gazdacentrum.hu`, `www.gazdacentrum.hu`
- Regisztrátor: WWH.hu
- DNS, CDN és SSL: Cloudflare
- Hosting: Cloudflare Pages
- GitHub: `vasotto/gazdacentrum`
- Production branch: `main`
- Deploy: automatikus minden `main` commit után

A GitHub `main` ág a production forrás. A repository ZIP csak pillanatfelvétel.

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
10. Phylazonit – céges
11. Magtár Kft. – céges
12. KAP portál – hivatalos

Az Agrárközösség inaktív, mert a feed nem ad stabilan feldolgozható RSS-választ.

## 5. Híradat és kategorizálás

A repositoryban található `news.json` állapota:

- generálva: 2026. július 23.;
- hírek száma: 151;
- RSS-hibák: 0;
- aktív források: 12.

Kategóriaeloszlás:

- Általános agrár: 42;
- Kertészet: 27;
- Agrárgazdaság: 17;
- Növénytermesztés: 15;
- Időjárás és vízgazdálkodás: 15;
- Ökológiai gazdálkodás: 12;
- Gépesítés: 11;
- Támogatások és pályázatok: 9;
- Állattenyésztés: 2;
- Növényvédelem: 1.

A `Gépesítés` kategória partneri tartalomhoz is tud navigálni, ha nincs megfelelő független gépes hír.

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

## 7. Agrárhatáridők adatmodellje

A `deadlines.json`:

- `schema_version: 2`;
- 10 rekordot tartalmaz;
- a státuszt nem tárolja fixen, azt a felület számolja ki;
- a relatív határidőt külön kezeli és nem mutatja a fő listában;
- pályázatonként csak a következő aktív vagy megnyíló szakaszt jeleníti meg.

Fontos mezők:

```text
id, title, action, affected, start_date, deadline_date,
deadline_text, reference_code, source_name, source_url,
verified_at, deadline_type, sectors, action_type,
date_type, show_in_main_list
```

### Jelenlegi rekordok

1. KAP-RD46-1-25 – 5. benyújtási szakasz, 2026. október 1–14.
2. KAP-RD46-1-25 – 6. benyújtási szakasz, 2026. október 15–28.
3. KAP-RD38-RD39-1-25 – 2026. őszi szakasz, 2026. október 7. – november 4.
4. KAP-RD38-RD39-1-25 – 2027. téli szakasz, 2027. február 3. – március 3.
5. 70/2026. IH – relatív kifizetési kötelezettség, rejtve a fő listából.
6. HMKÁ 6 – minimális talajborítás, 2026. július 15. – szeptember 30.
7. 2026. évi Gazdálkodási Napló eGN-rögzítése, határidő: 2027. január 31.
8. 2026. évi nitrát-adatszolgáltatás, határidő: 2027. március 31.
9. 2026. évi tavaszi fagykár-bejelentés, határidő: 2026. június 9., lejárt.
10. 2026. évi Egységes Kérelem, 2026. április 15. – június 9., lejárt.

## 8. Határidőfelület

### Production és próbafájlok

- `naptar.html`: korábbi production naptároldal; egyelőre nem cserélhető le.
- `naptar-proba.html`: az új, szűrhető teendőlista aktuális próbafelülete.
- `naptar-szinproba.html`: négy kapcsolható sötét palettát tartalmazó külön színpróba.

### A `naptar-proba.html` működő elemei

- határidőtípus-szűrés: Pályázat, Kifizetés, Adatszolgáltatás, Kötelezettség, Bejelentés;
- ágazati szűrés;
- időszakszűrés;
- lejárt tételek alapértelmezett elrejtése és külön kapcsolója;
- szűrők törlése;
- azonnali listasfrissítés;
- pályázati szakaszok összevonása a következő releváns szakaszra;
- hivatalos forrás és ellenőrzési dátum megjelenítése a kártyán;
- `Teendő részletei` párbeszédablak;
- egynapos jövőbeli határidőknél `esedékes` megfogalmazás;
- mobilon egyoszlopos kártyák és teljes szélességű gombok;
- a részletező ablak alján biztonsági tér a telefon alsó kezelősávja fölött;
- mobil vissza-a-tetejére gomb képernyőszéli lapfül formában.

### Mobilteszt állapota

Felhasználó által ellenőrizve:

- a szűrők egy oszlopba rendeződnek;
- a kártyák nem lógnak ki vízszintesen;
- a teljes HMKÁ 6 kártya jól olvasható;
- a részletező ablak jól görgethető;
- a `Hivatalos forrás` gomb teljesen látható;
- a `Teendő részletei` átnevezés megjelent;
- az Adatszolgáltatás szűrő működik.

Még ellenőrizendő a feltöltés után:

- a képernyőszéli vissza-a-tetejére gomb már ne takarja a kártyagombokat;
- a nitrátos kártyán ténylegesen `… nap múlva esedékes` jelenjen meg;
- teljes asztali ellenőrzés;
- csak ezután döntés a `naptar.html` lecseréléséről.

## 9. Színpróba

A `naptar-szinproba.html` négy sötét palettát tartalmaz:

- Grafit–petrol;
- Palakék–ibolya;
- Meleg grafit–bronz;
- Semleges grafit.

A palettaértékelést későbbre halasztottuk. A production színvilág még nincs elfogadva.

## 10. Pályázati rendszer

A `grants.json` 2 pályázatot és 12 benyújtási szakaszt tartalmaz.

Részletes oldalak:

1. `palyazat-kap-rd46-1-25.html`
   - minimum pontszám: 20;
   - maximum támogatás: 13 000 euró / 5 év;
   - következő szakasz: 2026. október 1–14.

2. `palyazat-kap-rd38-rd39-1-25.html`
   - minimum pontszám: 30;
   - minimum terület: 0,5 ha;
   - következő szakasz: 2026. október 7. – november 4.

A `PALYAZATI_ADATLAP_SABLON.md` rögzíti a kötelező mezőket, az emberi ellenőrzést és a hivatalos tények, illetve a GazdaCentrum-magyarázat elkülönítését.

## 11. Impresszum

Az `impresszum.html` tartalmazza az üzemeltető jelenleg ismert adatait, a tárhelyszolgáltatót, a szolgáltatás jellegét és az automatizált hírfeldolgozásra vonatkozó tájékoztatást.

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

- a kategorizálás és a duplikációszűrés heurisztikus;
- nincs külön kategóriaoldal és kereső;
- nincs hírlevél;
- a pályázatok és határidők frissítése még kézi ellenőrzést igényel;
- nincs automatikus dokumentumverzió-figyelés;
- nincs felhasználói fiók vagy értesítés;
- a forrásengedélyek rendezése nem teljes;
- nincs külön adatkezelési tájékoztató.

## 14. Következő konkrét feladat

Az aktualizált repository feltöltése után mobilon ellenőrizni kell a képernyőszéli vissza-a-tetejére gombot és a nitrátos kártya `esedékes` státuszszövegét. Ezután következhet az asztali teszt és a production `naptar.html` lecserélésének előkészítése.
