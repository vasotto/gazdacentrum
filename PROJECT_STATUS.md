# GazdaCentrum – projektállapot

Utolsó frissítés: 2026. július 20.

## 1. A projekt célja

A GazdaCentrum.hu teljesen vagy közel teljesen automatizált magyar agrár hírgyűjtő és gazdálkodói információs portál.

A rendszer célja:

- agrárhírek automatikus gyűjtése jogszerű RSS-, API- vagy más strukturált forrásból;
- a hírek kategorizálása és duplikációszűrése;
- a forrás, publikálási idő és eredeti cikklink megjelenítése;
- hivatalos pályázatok és határidők közérthető bemutatása;
- céges és partneri szakmai tartalmak egyértelmű elkülönítése;
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

DNS-módosítás előtt védeni kell:

- MX;
- SPF;
- DKIM;
- DMARC;
- szolgáltatói és domainigazoló TXT rekordok.

### Hosting

- Cloudflare Pages
- a production oldal a GitHub `main` ágából automatikusan deployolódik.

### GitHub

Felhasználó:

- vasotto

Repository:

- gazdacentrum

Production branch:

- main

A Cloudflare Pages minden `main` ágra kerülő commit után új deployt indít.

## 3. Jelenlegi működési folyamat

### Hírfolyam

```text
sources.csv
→ fetch_news.py
→ news.json
→ index.html
→ Cloudflare Pages
→ gazdacentrum.hu
```

### Pályázati tartalom

```text
hivatalos KAP-adatlap és dokumentumok
→ kézzel ellenőrzött strukturált adatok
→ grants.json
→ palyazatok.html
→ részletes pályázati adatlap
```

A GitHub Actions hatóránként automatikusan lefuttatja a hírfrissítést.

## 4. Fontos repository-fájlok

- `index.html` – főoldal, hírek, határidők és navigáció.
- `gazdacentrum_logo.png` – a weboldal logója.
- `sources.csv` – aktív RSS-források.
- `fetch_news.py` – RSS-feldolgozás, kategorizálás és duplikációszűrés.
- `requirements.txt` – Python-függőségek.
- `news.json` – a nyilvánosan megjelenő hírek adatfájlja.
- `deadlines.json` – hivatalos határidők strukturált adatai.
- `grants.json` – pályázati adatmodell.
- `palyazatok.html` – pályázati listaoldal.
- `palyazat-kap-rd46-1-25.html` – az első részletes pályázati adatlap.
- `PALYAZATI_ADATLAP_SABLON.md` – jóváhagyott pályázati adatlap-szabvány.
- `SOURCE_AUDIT.md` – források tartalmi és jogi auditja.
- `impresszum.html` – impresszum.
- `.github/workflows/update-news.yml` – automatikus hírfrissítő workflow.
- `PROJECT_STATUS.md` – aktuális projektállapot.
- `TODO.md` – következő feladatok.
- `CHANGELOG.md` – változások időrendben.
- `README.md` – projektleírás.

## 5. Jelenlegi aktív RSS-források

Jelenleg 12 aktív forrás szerepel a `sources.csv` fájlban.

| Forrás | RSS | Alapkategória | Típus |
|---|---|---|---|
| Agrárszektor | https://www.agrarszektor.hu/rss | Agrárgazdaság | portál |
| Agro Napló | https://www.agronaplo.hu/rss | Általános agrár | portál |
| Magyar Mezőgazdaság | https://magyarmezogazdasag.hu/feed/ | Általános agrár | portál |
| Mezőhír | https://mezohir.hu/feed/ | Általános agrár | portál |
| Agrofórum | https://agroforum.hu/feed/ | Általános agrár | portál |
| AKI | https://www.aki.gov.hu/feed/ | Agrárgazdaság | hivatalos |
| ÖMKi | https://biokutatas.hu/feed/ | Ökológiai gazdálkodás | szakmai |
| FruitVeB | https://fruitveb.hu/feed/ | Kertészet | szakmai |
| Agroinform | https://www.agroinform.hu/rss | Általános agrár | portál |
| Phylazonit | https://phylazonit.hu/feed/ | automatikus kategorizálás | ceges |
| Magtár Kft. | https://magtarkft.hu/feed/ | Gépesítés | ceges |
| KAP portál | https://kap.gov.hu/rss.xml | Támogatások és pályázatok | hivatalos |

### Céges források megjelenítése

A `ceges` típusú tartalmak:

- külön „Céges és partneri szakmai tartalmak” rovatban jelennek meg;
- nem keverednek a független hírfolyammal;
- alapállapotban nem láthatók;
- vállalatonként külön választógombbal nyithatók meg;
- „Céges szakmai tartalom” jelölést kapnak.

Aktív céges források:

- Phylazonit;
- Magtár Kft.

A Magtár Kft. `AKCIÓK` RSS-kategóriájú bejegyzései automatikusan kizárásra kerülnek.

## 6. Inaktív vagy kizárt források

### Agrárközösség

Feed:

- https://agrarkozosseg.hu/feed/

Státusz:

- ideiglenesen kikapcsolva;
- a feedet ellenőrző vagy védelmi oldal blokkolta;
- XML-feldolgozásra nem alkalmas válasz érkezett.

Csak akkor kapcsolható vissza, ha ismét stabil, szabványos RSS-t ad.

### GÉPmax

Feed:

- https://gepmax.hu/feed/

Státusz:

- inaktív;
- a felhasználási feltételek miatt nem használjuk linkforrásként.

### További tesztelt, de inaktív források

- Agrárágazat – XML `undefined entity` hiba.
- Agrotrend – XML `undefined entity` hiba.
- AgrárUnió – nem találtunk működő nyilvános RSS-feedet.
- Agrokép – feed letiltva vagy nem található.
- Haszon Agrár – hibás feed.
- MAGRO – hibás feed.
- Farmvilág – hibás feed.

## 7. fetch_news.py

A `fetch_news.py` fő feladatai:

- a `sources.csv` beolvasása;
- RSS-források lekérése;
- cím, link, dátum, forrás és belső összefoglaló feldolgozása;
- forrásspecifikus és kulcsszavas kategorizálás;
- nyilvánvalóan nem releváns tartalmak kiszűrése;
- fizetett vagy reklámjellegű elemek szűrése;
- duplikációk felismerése;
- a `news.json` elkészítése.

### Lekérési szabályok

- forrásonként legfeljebb 3 próbálkozás;
- két próbálkozás között 5 másodperc várakozás;
- egyetlen hibás forrás nem állítja le a teljes futást;
- a hibák a `news.json` `errors` mezőjébe kerülnek.

### Feldolgozási korlátok

- forrásonként legfeljebb 20 elem;
- a végleges `news.json` legfeljebb 200 hírt tartalmaz;
- a tartalmi duplikációszűrés időablaka 72 óra.

### Kategorizálási és szűrési fejlesztések

A rendszer:

- az Agro Napló `(x)` végződésű fizetett tartalmait kizárja;
- a `Mezőgazdasági gépek` kategóriát `Gépesítés` névre egységesíti;
- az Agrárszektor híreit forrásspecifikus szabályokkal kategorizálja;
- RSS- és URL-jelzéseket is használ;
- kiszűri a nyilvánvaló életmód- és fogyasztói tartalmakat;
- a meteorológiai és termelési híreket szövegkörnyezet alapján különíti el;
- a Magtár Kft. híreit egységesen a `Gépesítés` kategóriába rendezi.

## 8. Relevancia- és duplikációszűrés

### Relevanciaszűrés

A rendszer forrás-, cím- és linkfüggő szabályokkal kiszűri a nyilvánvalóan nem agrár témájú elemeket.

Példák:

- Agroinform Házikert rovat;
- Agrofórum hobbikerti és lakossági szaktanácsadási tartalmak;
- egyértelműen életmód-, fogyasztói vagy nem gazdálkodói témák.

### Duplikációszűrés

A rendszer vizsgálja:

- azonos vagy normalizált linket;
- azonos vagy normalizált címet;
- azonos és közel azonos belső összefoglalót;
- közös kulcsszavakat;
- tartalmi hasonlóságot;
- publikálási időt;
- láncoltan kapcsolódó duplikációkat.

Forrásprioritás:

```text
hivatalos
→ szakmai
→ portál
```

Azonos típus esetén a frissebb publikálási idő kap előnyt.

## 9. news.json állapota

A legutóbb kézzel ellenőrzött sikeres futás:

- 142 hírt tartalmazott;
- az `errors` lista üres volt;
- mind a 12 aktív forrás feldolgozása hibamentesen lefutott.

A hírek száma futásonként változik.

A nyilvános `news.json` nem tartalmazza az RSS-összefoglalót. Az összefoglaló csak belső:

- relevanciaszűrésre;
- kategorizálásra;
- duplikációvizsgálatra

használható.

## 10. A főoldal jelenlegi funkciói

A `gazdacentrum.hu` főoldalon működik:

- hírek kártyás megjelenítése;
- kategória;
- cím;
- forrás;
- forrástípus;
- publikálási idő;
- eredeti cikklink;
- határidők szakasz;
- pályázati listaoldalra vezető navigáció;
- céges forrásválasztó;
- világos és sötét mód;
- mobilra tördelődő felső menü.

A mobilmenü javítva lett, ezért a menüpontok már nem csúsznak ki vízszintesen.

## 11. Határidők

A `deadlines.json` jelenleg 4 strukturált rekordot tartalmaz:

- KAP-RD46-1-25 – 2026. október 1–28. közötti beadási időszak;
- KAP-RD38-RD39-1-25 – 5. beadási időszak;
- KAP-RD38-RD39-1-25 – 6. beadási időszak;
- 70/2026. IH – általános, relatív határidejű kötelezettség.

A határidős adatoknál mindig szerepelnie kell a hivatalos forrás ellenőrzésére vonatkozó figyelmeztetésnek.

## 12. Pályázati rendszer

### grants.json

A `grants.json` jelenleg:

- 2 pályázati entitást;
- összesen 8 benyújtási időszakot

tartalmaz.

A modell mezői többek között:

- pályázati kód és cím;
- státusz;
- ágazatok;
- jogosultsági összefoglaló;
- támogatási forma;
- keretösszeg;
- támogatási összeg;
- támogatási intenzitás;
- megvalósítási idő;
- benyújtási szakaszok;
- frissítések;
- dokumentumok;
- hivatalos forrás;
- ellenőrzési dátum;
- hivatalos ellenőrzés szükségessége.

### palyazatok.html

A pályázati listaoldal működik:

- URL: https://gazdacentrum.hu/palyazatok.html
- 2 pályázatot jelenít meg;
- 8 benyújtási időszakot kezel;
- megjeleníti a támogatási összeget és az időszakokat;
- közvetlen hivatalos linket ad;
- a KAP-RD46-1-25 kártyáján részletes összefoglaló gomb található.

### Első részletes pályázati adatlap

Fájl:

```text
palyazat-kap-rd46-1-25.html
```

Élő URL:

```text
https://gazdacentrum.hu/palyazat-kap-rd46-1-25.html
```

Tartalmazza:

- gyors áttekintést;
- jogosulti kört;
- minimum STÉ-re vonatkozó információt;
- maximális támogatást;
- 20 pontos minimumot;
- benyújtási szakaszokat;
- támogatási és kifizetési ütemezést;
- pontozási rendszert;
- kötelezettségeket;
- buktatókat;
- hivatalos dokumentumlinket;
- módosítási előzményeket;
- hivatalos forrás ellenőrzésére vonatkozó figyelmeztetést.

A részletes oldal:

- a pályázati listaoldalról elérhető;
- mobilon nem lóg ki;
- a széles táblázatokat saját keretükön belül görgeti;
- világos és sötét módban is működik.

### Pályázati adatlap-szabvány

Fájl:

```text
PALYAZATI_ADATLAP_SABLON.md
```

A szabvány rögzíti:

- a kötelező alapadatokat;
- a gyors áttekintés mezőit;
- a jogosultság, STÉ, támogatási intenzitás és pontozás kezelését;
- a támogatható és kizárt tevékenységek bemutatását;
- a géppályázatok speciális követelményeit;
- a buktatók megjelenítési szabályait;
- a dokumentum- és változáskövetést;
- a hivatalos adat és a GazdaCentrum-értelmezés elkülönítését;
- az AI használatának ellenőrzési szabályait;
- a közzététel előtti ellenőrzőlistát.

## 13. AI használatának tervezett szerepe

Az AI később használható:

- pályázati felhívások és mellékletek strukturált feldolgozására;
- jogosultsági feltételek előzetes kinyerésére;
- STÉ-, intenzitási és pontozási mezők azonosítására;
- támogatható és kizárt gépek elkülönítésére;
- közérthető összefoglalók készítésére;
- dokumentumverziók összehasonlítására;
- módosítások és buktatók jelölésére.

Kritikus adatok emberi ellenőrzés nélkül nem publikálhatók:

- jogosultsági feltételek;
- STÉ-határ;
- támogatási intenzitás;
- minimum pontszám;
- támogatható vagy kizárt géplisták;
- beadási határidők;
- visszafizetési és szankciós szabályok.

## 14. Forrásaudit és jogi állapot

A teljes forrásaudit a `SOURCE_AUDIT.md` fájlban található.

Fő döntések:

- KAP portál – korlátozott, hivatalos adatokra épülő használat;
- Phylazonit és Magtár Kft. – külön céges pilot, dokumentált hozzájárulás szükséges;
- Mezőhír – engedély szükséges;
- AKI – engedély szükséges;
- Agroinform – engedély szükséges;
- Agrárszektor, Agro Napló, Magyar Mezőgazdaság, Agrofórum, ÖMKi és FruitVeB – feltételes használat, írásos tisztázás ajánlott;
- GÉPmax – nem használjuk.

Indulás előtt különösen ellenőrizni kell a Mezőhír, AKI és Agroinform nyilvános használatának jogalapját.

## 15. Tartalmi és jogi alapelvek

- teljes külső cikket nem veszünk át;
- külső képet nem töltünk le automatikusan;
- minden hírnél megjelenik a forrás, dátum és eredeti link;
- elsődlegesen RSS-, API- vagy más engedélyezett strukturált forrást használunk;
- scraping csak külön jogi és technikai vizsgálat után alkalmazható;
- a saját összefoglaló nem torzíthatja az eredeti tartalmat;
- támogatási, jogszabályi, pénzügyi és növényvédelmi tartalomnál az eredeti hivatalos forrást ellenőrizni kell;
- az oldalon jelezni kell az automatizált tartalom-előállítást;
- a céges és partneri tartalmak nem keveredhetnek a független hírfolyammal.

## 16. GitHub Actions

Workflow:

```text
.github/workflows/update-news.yml
```

Workflow neve:

- Agrárhírek frissítése

Működése:

- kézzel indítható;
- hatóránként automatikusan fut;
- telepíti a Python-függőségeket;
- lefuttatja a `fetch_news.py` programot;
- frissíti a `news.json` fájlt;
- a változást visszamenti a `main` ágra.

Python-függőség:

```text
feedparser==6.0.12
```

## 17. Facebook

A korábbi Zetorvas Facebook-oldal neve GazdaCentrum.

Jelenlegi URL:

- facebook.com/zetorvas

A Facebook-link addig nem kerülhet ki a weboldalra, amíg nincs végleges felhasználónév, például:

- gazdacentrum;
- gazdacentrum.hu;
- gazdacentrumhu.

## 18. Ismert korlátozások

- a kategorizálás heurisztikus, ezért időszakos ellenőrzést igényel;
- a duplikációszűrés heurisztikus;
- nincsenek külön kategóriaoldalak;
- nincs kereső;
- nincs hírlevél;
- nincs automatikus AI-alapú saját hírösszefoglaló;
- nincs „Miért fontos?” mező;
- a pályázati adatok frissítése még nem automatikus;
- csak egy pályázathoz készült részletes adatlap;
- nincs automatikus dokumentumverzió- és IH-közlemény-figyelés;
- nincs pályázati jogosultsági vagy pontszám-előbecslő;
- a forrásengedélyek írásos rendezése még nem teljes.

## 19. Következő konkrét feladat

A pályázati adatlap-szabvány tesztelése egy második pályázaton:

- a KAP-RD38-RD39-1-25 hivatalos adatainak ellenőrzése;
- a szükséges dokumentumok és módosítások összegyűjtése;
- a második részletes pályázati adatlap elkészítése;
- a sablon általánosíthatóságának ellenőrzése.
