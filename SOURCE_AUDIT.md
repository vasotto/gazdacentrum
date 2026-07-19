# GazdaCentrum forrásaudit

**Audit dátuma:** 2026-07-19  
**Vizsgált aktív források:** 13  
**Kizárt források:** 1  
**Technikai alap:** a 2026-07-19-én előállított `news.json` és a forrásonként elvégzett RSS-vizsgálatok  

## 1. Az audit célja

Ez a dokumentum rögzíti, hogy a GazdaCentrum jelenlegi forrásai:

- technikailag működnek-e;
- milyen típusú tartalmakat adnak;
- milyen jogi vagy felhasználási korlátozásokat közölnek;
- milyen adatokat jeleníthet meg belőlük a GazdaCentrum;
- szükséges-e írásos engedély;
- milyen forrásspecifikus szűrést kell alkalmazni.

Ez gyakorlati belső forrásaudit, nem ügyvédi jogi szakvélemény. Ha egy feltétel nem egyértelmű, a GazdaCentrum a szigorúbb, óvatosabb értelmezést alkalmazza.

## 2. A GazdaCentrum egységes megjelenítési minimuma

Külső forrásból alapértelmezetten csak az alábbi mezők kerülhetnek a nyilvános oldalra:

- eredeti cikkcím;
- forrás neve;
- közzététel dátuma;
- közvetlen eredeti cikklink;
- GazdaCentrum által meghatározott kategória és tartalomtípus.

Alapértelmezetten **nem kerülhet át**:

- RSS-leírás vagy kivonat;
- teljes cikk vagy hosszabb szövegrész;
- külső kép;
- videó;
- kapcsolati adat;
- termékár vagy ajánlat;
- hirdetés, PR-cikk, szponzorált vagy `(x)` jelölésű tartalom.

## 3. Auditállapotok

- **Használható – korlátozottan:** a dokumentált feltételek mellett cím, forrás, dátum és közvetlen link használható.
- **Feltételes:** a forrás technikailag használható, de a rendszeres automatizált címátvételhez írásos megerősítés vagy további pontosítás ajánlott.
- **Csak engedéllyel:** a közzétett feltételek alapján a tartalom felhasználása előzetes engedélyhez kötött; nyilvános indulás előtt ki kell kapcsolni, ha nincs írásos engedély.
- **Céges pilot:** csak a külön céges rovatban, egyértelmű jelöléssel használható; nyilvános indulás előtt írásos partneri megerősítés ajánlott.
- **Kizárva:** nem használható.

## 4. Összesített döntési tábla

| # | Forrás | Típus | Technikai állapot | Auditdöntés | Nyilvános indulás előtti teendő |
|---:|---|---|---|---|---|
| 1 | Agrárszektor | portál | működik | **Feltételes** | cím + dátum + link automatizált használatának írásos pontosítása |
| 2 | Agro Napló | portál | működik | **Feltételes** | engedély pontosítása; minden `(x)` tartalom kizárása |
| 3 | Magyar Mezőgazdaság | portál | működik | **Feltételes** | írásos megerősítés kérése; kivonat és kép tiltása |
| 4 | Mezőhír | portál | működik | **Csak engedéllyel** | írásos engedély nélkül kikapcsolandó |
| 5 | Agrofórum | portál | működik | **Feltételes** | pontos forrásmegjelölés; írásos megerősítés ajánlott |
| 6 | AKI | hivatalos/szakmai | működik | **Csak engedéllyel** | írásos engedély nélkül kikapcsolandó |
| 7 | ÖMKi | szakmai | működik | **Feltételes** | írásos engedély vagy egyértelmű felhasználási nyilatkozat szükséges |
| 8 | FruitVeB | szakmai | működik | **Feltételes** | írásos engedély vagy felhasználási nyilatkozat szükséges |
| 9 | Agrárközösség | szakmai/üzleti portál | működik | **Feltételes** | jogi feltételek nem voltak teljesen hozzáférhetők; engedély szükséges |
| 10 | Agroinform | portál | működik | **Csak engedéllyel** | írásos engedély nélkül kikapcsolandó |
| 11 | Phylazonit | céges | működik | **Céges pilot** | írásos partneri megerősítés; külön céges rovat megtartása |
| 12 | Magtár Kft. | céges | működik | **Céges pilot** | írásos partneri megerősítés; `AKCIÓK` kizárása |
| 13 | KAP portál | hivatalos | működik | **Használható – korlátozottan** | csak cím, dátum, forrás és hivatalos link; eredeti forrás ellenőrzési figyelmeztetés |

## 5. Technikai összesítés

A 2026-07-19-én létrehozott `news.json` szerint mind a 13 aktív forrás feldolgozása hiba nélkül befejeződött. A nyilvános adatállomány csak a szükséges mezőket tartalmazta; RSS-leírást, teljes cikket és külső képet nem tárolt.

| Forrás | Megmaradt tételek száma | Legújabb feldolgozott tétel | Fő megjegyzés |
|---|---:|---|---|
| Agrárszektor | 17 | 2026-07-18 | gyorsan frissülő vegyes agrárhír-feed |
| Agro Napló | 14 | 2026-07-17 | két `(x)` tartalom átjutott; szűrés szükséges |
| Magyar Mezőgazdaság | 9 | 2026-07-18 | vegyes hírportál; nem minden cikk szűken gazdálkodói relevanciájú |
| Mezőhír | 19 | 2026-07-18 | magas frissítési gyakoriság; partnerhírek elkülönítése indokolt |
| Agrofórum | 5 | 2026-07-18 | sok életmód- és házikerti tartalom miatt erősebb relevanciaszűrés kell |
| AKI | 10 | 2026-07-14 | piaci adatok és szakmai események |
| ÖMKi | 10 | 2026-07-17 | jól körülhatárolt ökológiai szakmai tartalom |
| FruitVeB | 19 | 2026-07-17 | kertészeti és piaci tartalom; stabil tematikus forrás |
| Agrárközösség | 10 | 2026-07-17 | jogszabályi, szakmai és képzési tartalom; ritkább frissítés |
| Agroinform | 11 | 2026-07-18 | nagy mennyiségű vegyes tartalom; erős relevanciaszűrés szükséges |
| Phylazonit | 10 | 2026-07-08 | céges szakmai tartalom; teljes cikket adó WordPress-feed |
| Magtár Kft. | 9 | 2026-04-27 | ritkább frissítés; gépes tartalom; akciós elem kizárva |
| KAP portál | 8 | 2026-07-16 | hivatalos pályázati és támogatási közlemények |

---

# 6. Forrásonkénti audit

## 6.1. Agrárszektor

### Technikai megállapítás

- Nyilvános RSS működik.
- A feldolgozás 17 releváns elemet tartott meg.
- A GazdaCentrum csak címet, forrást, dátumot és közvetlen linket tárol.

### Jogi megállapítás

A kiadó jogi nyilatkozata korlátozza a tartalom feldolgozását, adatbázisban tárolását és technikai újraközvetítését. A hiperhivatkozást az előírt forrásmegjelöléssel engedi, de az eredeti címek rendszeres automatizált megjelenítése nem teljesen egyértelmű.

### Döntés

- **Státusz:** Feltételes
- **Megengedett minimum:** közvetlen link és `Forrás: Agrárszektor.hu`
- **Nem használható:** kivonat, kép, teljes szöveg
- **Teendő:** írásos engedély vagy állásfoglalás kérése a cím + dátum + link automatizált megjelenítésére

### Hivatalos dokumentumok

- https://www.agrarszektor.hu/info/jogi-nyilatkozat
- https://cdn.portfolio.hu/files/a/agrarszektor-felhasznalasi-feltetelekk.pdf

## 6.2. Agro Napló

### Technikai megállapítás

A mentett RSS 20 elemet tartalmazott, stabil címekkel, linkekkel, dátumokkal és GUID-okkal. Két cím `(x)` jelöléssel végződött. A jelenlegi szűrő ezeket még nem zárta ki.

### Jogi megállapítás

A jogi nyilatkozat korlátozza a tartalom feldolgozását és adatbázisban tárolását. Az értesülések átvételét egyértelmű hivatkozással megengedi, de a rendszeres automatizált címátvétel nincs egyértelműen engedélyezve.

### Döntés

- **Státusz:** Feltételes
- **Kötelező szűrés:** minden `(x)` jelölésű tartalom kizárása
- **Nem használható:** RSS-leírás, kép, teljes szöveg
- **Teendő:** írásos pontosítás kérése

### Hivatalos dokumentumok

- https://www.agronaplo.hu/info/jogi-nyilatkozat
- https://www.agronaplo.hu/rss

## 6.3. Magyar Mezőgazdaság

### Technikai megállapítás

- A WordPress RSS működik.
- A 2026-07-19-i futás 9 releváns elemet tartott meg.
- A forrás széles tematikájú, ezért a hobbiállat-, kiskert-, életmód- és természetismereti cikkek erősebb szűrése szükséges.

### Jogi megállapítás

A szerzői jogi tájékoztató tiltja a lap egészének vagy részeinek engedély nélküli feldolgozását, terjesztését, adatbázisban tárolását és technikai újraközvetítését. Ugyanakkor a laptól származó értesülések átvételét hivatkozással megengedi, ha az eredeti információ nem módosul. A két szabály együtt nem ad teljesen egyértelmű engedélyt a rendszeres automatizált címátvételre.

### Döntés

- **Státusz:** Feltételes
- **Nem használható:** kivonat, kép, cikkrészlet, videó
- **Teendő:** írásos megerősítés kérése a cím + dátum + közvetlen link megjelenítésére
- **Kapcsolat:** online@magyarmezogazdasag.hu

### Hivatalos dokumentum

- https://magyarmezogazdasag.hu/szerzoi-jogok/

## 6.4. Mezőhír

### Technikai megállapítás

- Az RSS működik; a 2026-07-19-i futás 19 releváns elemet tartott meg.
- A portál külön `Partner-hírek` rovatot is működtet, ezért a fizetett vagy partneri tartalmakat külön szűrni kell.

### Jogi megállapítás

A szerzői jogi oldal szerint az oldal bármely részének másolása, utánközlése vagy reprodukálása csak a kiadó engedélyével lehetséges.

### Döntés

- **Státusz:** Csak engedéllyel
- **Nyilvános indulás:** írásos engedély hiányában kikapcsolandó
- **Nem használható:** cím, kivonat, kép vagy cikkrészlet engedély nélkül
- **Megengedett:** önmagában a közvetlen hivatkozás, saját leíró szöveggel; automatikus eredeticím-átvételhez engedély szükséges

### Hivatalos dokumentum

- https://mezohir.hu/szerzoi-jogok/

## 6.5. Agrofórum

### Technikai megállapítás

- Az RSS működik; 5 releváns elem maradt meg.
- A feed és a portál sok házikerti, életmód- és általános környezetvédelmi tartalmat is közöl, ezért szigorú relevanciaszűrés szükséges.

### Jogi megállapítás

Az ÁSZF tiltja a portál egészének vagy részeinek engedély nélküli feldolgozását és értékesítését. Az értesülések átvételét ugyanakkor megengedi, ha az eredeti információ nem módosul és minden közlésnél egyértelmű, online felületen linkelt hivatkozás szerepel.

### Döntés

- **Státusz:** Feltételes
- **Megengedett minimum:** cím, dátum, `Forrás: Agrofórum Online`, közvetlen link
- **Nem használható:** kivonat, kép, teljes cikk
- **Teendő:** írásos megerősítés ajánlott a rendszeres automatizált használathoz

### Hivatalos dokumentum

- https://agroforum.hu/aszf/

## 6.6. AKI Agrárközgazdasági Intézet

### Technikai megállapítás

- Az RSS működik; 10 elem maradt meg.
- A tartalom főként piaci adat, szakmai elemzés és esemény.

### Jogi megállapítás

Az AKI jogi nyilatkozata szerint a tartalom üzleti célú felhasználása, más honlapba építése és adatbázis-szerű feldolgozása előzetes írásos hozzájárulás nélkül nem megengedett. A képi és szöveges tartalom használata főszabály szerint írásos engedélyhez kötött.

### Döntés

- **Státusz:** Csak engedéllyel
- **Nyilvános indulás:** írásos engedély hiányában kikapcsolandó
- **Teendő:** engedélykérés az `aki@aki.gov.hu` címen a cím + dátum + közvetlen link automatizált megjelenítésére

### Hivatalos dokumentum

- https://www.aki.gov.hu/jogi-nyilatkozat/

## 6.7. ÖMKi

### Technikai megállapítás

- Az RSS működik; 10 szakmailag releváns elem maradt meg.
- A forrás tematikailag tiszta, főként ökológiai gazdálkodási, kutatási és szakmai eseménytartalmakat közöl.

### Jogi megállapítás

A weboldal `Minden jog fenntartva` jelzést tartalmaz. Nyilvánosan elérhető, egyértelmű olyan engedélyt nem találtunk, amely a címek rendszeres automatizált újraközlését kifejezetten lehetővé tenné.

### Döntés

- **Státusz:** Feltételes
- **Nem használható:** kivonat, kép, teljes szöveg
- **Teendő:** írásos engedély vagy rövid partneri megerősítés kérése az `info@biokutatas.hu` címen

### Hivatalos oldal

- https://biokutatas.hu/

## 6.8. FruitVeB

### Technikai megállapítás

- Az RSS működik; 19 releváns kertészeti és piaci elem maradt meg.
- A forrás tematikailag jól illeszkedik a kertészeti kategóriához.
- A tartalmak között külföldi piaci hírek és más szervezetektől átvett információk is vannak, ezért az eredeti forrást is ellenőrizni kell.

### Jogi megállapítás

A nyilvános impresszumban nem találtunk egyértelmű tartalom-újraközlési engedélyt vagy licencet. Az RSS technikai elérhetősége önmagában nem tekinthető felhasználási engedélynek.

### Döntés

- **Státusz:** Feltételes
- **Nem használható:** kivonat, kép, teljes szöveg
- **Teendő:** írásos engedély vagy felhasználási nyilatkozat kérése

### Hivatalos oldalak

- https://fruitveb.hu/
- https://fruitveb.hu/impresszum/

## 6.9. Agrárközösség

### Technikai megállapítás

- Az RSS működik; 10 releváns elem maradt meg.
- A forrás ritkábban frissül, de jogszabályi, gazdálkodási és képzési témákat közöl.

### Jogi megállapítás

A weboldal nyilvános böngészése automatizált ellenőrzőoldalba ütközött, ezért a jogi és felhasználási feltételek teljes szövege nem volt megbízhatóan hozzáférhető. Egyértelmű újraközlési engedélyt nem találtunk.

### Döntés

- **Státusz:** Feltételes
- **Nyilvános indulás:** írásos engedély vagy a feltételek kézi ellenőrzése nélkül nem tekinthető véglegesen jóváhagyottnak
- **Teendő:** közvetlen kapcsolatfelvétel a szolgáltatóval

### Hivatalos oldal

- https://agrarkozosseg.hu/

## 6.10. Agroinform

### Technikai megállapítás

- Az RSS működik; 11 elem maradt meg.
- A feed nagyon vegyes: szakmai agrárhírek mellett házikerti, életmód- és promóciós jellegű tartalmak is megjelenhetnek.

### Jogi megállapítás

A felhasználási feltételek szerint a portál és bármely rajta megjelenő tartalom bármilyen felhasználása a szolgáltató engedélye nélkül tilos. A feltételek nem tartalmaznak külön, a GazdaCentrum tervezett automatizált cím- és linkmegjelenítésére alkalmazható engedményt.

### Döntés

- **Státusz:** Csak engedéllyel
- **Nyilvános indulás:** írásos engedély hiányában kikapcsolandó
- **Teendő:** engedélykérés az `ugyfelszolgalat@agroinform.hu` címen

### Hivatalos dokumentum

- https://www.agroinform.hu/aszf

## 6.11. Phylazonit

### Technikai megállapítás

- A WordPress RSS működik és 10 elemet adott.
- A feed teljes cikk-HTML-t is tartalmaz, de a GazdaCentrum ezt nem tárolja és nem jeleníti meg.
- A cikkek külön, vállalati választó mögött jelennek meg.

### Jogi és tartalmi megállapítás

A weboldal `Minden jog fenntartva` jelzést használ, és nem találtunk nyilvános licencet a rendszeres automatizált újraközlésre. Mivel vállalati saját tartalomról van szó, a forrás csak egyértelmű céges jelöléssel és lehetőleg írásos partneri megerősítéssel használható.

### Döntés

- **Státusz:** Céges pilot
- **Megjelenítés:** kizárólag a `Céges és partneri szakmai tartalmak` részben
- **Nem használható:** teljes cikk, RSS-kivonat, külső kép
- **Teendő:** rövid írásos hozzájárulás kérése a cím + dátum + link megjelenítésére

### Hivatalos oldal

- https://phylazonit.hu/

## 6.12. Magtár Kft.

### Technikai megállapítás

- Az RSS működik és 10 elemet tartalmazott.
- Egy elem `AKCIÓK` kategóriájú volt, ezért 9 elem került a GazdaCentrum céges rovatába.
- A feed teljes cikk-HTML-t, képeket, telefonszámokat és e-mail-címeket is tartalmaz, de ezek nem kerülnek a GazdaCentrum nyilvános adatállományába.
- A feed frissítési gyakorisága alacsonyabb a nagy hírportálokénál.

### Jogi és tartalmi megállapítás

Nyilvános, egyértelmű tartalom-újraközlési licencet nem találtunk. A forrás ezért csak elkülönített céges tartalomként és írásos partneri megerősítéssel tekinthető véglegesen biztonságosnak.

### Döntés

- **Státusz:** Céges pilot
- **Kötelező szűrés:** `AKCIÓK`, tisztán értékesítési és készletajánlati bejegyzések kizárása
- **Megjelenítés:** kizárólag a külön Magtár-választó megnyitása után
- **Nem használható:** teljes cikk, kivonat, kép, elérhetőség
- **Teendő:** írásos partneri megerősítés kérése

### Hivatalos oldal

- https://magtarkft.hu/

## 6.13. KAP portál

### Technikai megállapítás

- A hivatalos RSS működik; 8 releváns pályázati, támogatási és közleménytétel maradt meg.
- A forrás közvetlenül illeszkedik a későbbi pályázatfigyelő rendszerhez.

### Jogi és tartalmi megállapítás

A KAP portál hivatalos tájékoztató oldal. A nyilvánosan elérhető oldalak között nem találtunk olyan egyértelmű tartalomlicencet, amely hosszabb szövegek vagy képek automatikus átvételét engedné. A hivatalos közlemények közvetlen linkelése és cím szerinti azonosítása a GazdaCentrum működéséhez szükséges, de csak minimális adattal és az eredeti dokumentum kötelező ellenőrzésére figyelmeztetve használjuk.

### Döntés

- **Státusz:** Használható – korlátozottan
- **Megjeleníthető:** cím, közlemény- vagy pályázati kód, dátum, státusz és közvetlen hivatalos link
- **Nem használható automatikusan:** hosszabb összefoglaló, dokumentumrészlet, kép
- **Kötelező figyelmeztetés:** támogatási döntés előtt mindig az eredeti hivatalos felhívást és annak legfrissebb módosítását kell ellenőrizni
- **Pályázatfigyelő:** a KAP portál frissítéseit később pályázati adatlapokhoz kell hozzárendelni, nem pusztán önálló hírekként kezelni

### Hivatalos oldalak

- https://kap.gov.hu/
- https://kap.gov.hu/rss.xml

---

# 7. Kizárt forrás

## GÉPmax

- **Státusz:** Kizárva
- **Indok:** a korábbi vizsgálat alapján a linkelést és a tartalom használatát nem engedi a GazdaCentrum tervezett formájában.
- **Teendő:** nem kerülhet vissza a `sources.csv` fájlba új, egyértelmű írásos engedély nélkül.

# 8. Kötelező technikai módosítások az audit után

Ezeket csak külön jóváhagyás és biztonsági mentés után kell végrehajtani:

1. Agro Napló: minden `(x)` végződésű cím kizárása.
2. Mezőhír: `Partner-hírek`, PR- és hirdetési tartalmak kizárása, ha a forrás engedélyt kap.
3. Magyar Mezőgazdaság, Agrofórum, Agroinform: erősebb hobbi-, életmód- és házikerti relevanciaszűrés.
4. Magtár Kft.: `AKCIÓK` és tisztán értékesítési tartalom kizárása továbbra is kötelező.
5. Minden forrás: az RSS-kivonat és kép URL-je ne kerüljön a nyilvános `news.json` fájlba.
6. A forrásmegjelölések legyenek egységesek, például `Forrás: Agrárszektor.hu` vagy `Forrás: Agrofórum Online`.
7. Az engedélyekről kapott leveleket és feltételeket dokumentáltan archiválni kell.

# 9. Nyilvános indulási döntés

A jelenlegi audit alapján a technikai működés megfelelő, de a források többségének jogi státusza még nem végleges.

**Írásos engedély nélkül biztosan kikapcsolandó a nyilvános indulás előtt:**

- Mezőhír;
- AKI;
- Agroinform.

**Írásos pontosítás vagy megerősítés erősen ajánlott:**

- Agrárszektor;
- Agro Napló;
- Magyar Mezőgazdaság;
- Agrofórum;
- ÖMKi;
- FruitVeB;
- Agrárközösség;
- Phylazonit;
- Magtár Kft.

**Korlátozottan megtartható hivatalos forrás:**

- KAP portál, kizárólag cím, dátum, azonosító és közvetlen hivatalos link formájában.

# 10. Következő projektlépés

Az audit után nem újabb források tömeges felvétele következik. A helyes sorrend:

1. az engedélykérések egységes szövegének elkészítése;
2. a három egyértelműen engedélyköteles forrás ideiglenes leállításának eldöntése;
3. a szükséges reklám- és irreleváns-tartalom szűrések beépítése;
4. a végleges, nyilvános indulási forráslista rögzítése;
5. ezután a pályázatfigyelő és támogatási naptár adatmodelljének kialakítása.
