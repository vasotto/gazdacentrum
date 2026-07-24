# GazdaCentrum projektprotokoll

**Fájlnév:** `GAZDACENTRUM_PROJEKT_PROTOKOLL.md`  
**Szerepe:** a GC projekt részletes működési kézikönyve és állapotátadási dokumentuma  
**Utolsó összeállítás:** 2026-07-24

## 1. Cél

Ez a dokumentum biztosítja, hogy a GazdaCentrum fejlesztése új chatben is zavartalanul folytatható legyen. A projektinstrukció erre a fájlra hivatkozik. Új chatben ezt, a legfrissebb repository ZIP-et és az aktuális dokumentációt kell elsőként áttekinteni.

## 2. Projektcél

A GazdaCentrum.hu automatizált magyar agrárinformációs portál.

Fő célok:
- hivatalos agrárhatáridők, kötelezettségek és pályázati időszakok gyűjtése;
- a teendők, érintettek, dátumok és hivatalos források közérthető megjelenítése;
- jogszerű agrárhír-gyűjtés RSS-ből, API-ból vagy engedélyezett forrásból;
- egyszerű, stabil, olcsó és kevés kézi munkát igénylő rendszer;
- válasz a fő kérdésre: „Mivel kell most foglalkoznom, és mennyi időm van rá?”

## 3. Forráselsőbbség

Project-only mód szerint dolgozzunk. Más projektek adatai nem keverhetők ide.

Sorrend:
1. felhasználó aktuális üzenete;
2. aktuálisan feltöltött fájl;
3. legfrissebb repository ZIP;
4. GitHub main ág dokumentált állapota;
5. ez a protokoll;
6. PROJECT_STATUS.md;
7. CHANGELOG.md;
8. TODO.md;
9. korábbi projektbeszélgetések.

A ZIP pillanatfelvétel. A production forrás a GitHub main ág. Nem tekinthető késznek olyan módosítás, amelynek GitHub-feltöltését és működését a felhasználó nem igazolta.

## 4. Infrastruktúra

- Domain: gazdacentrum.hu
- Másodlagos domain: www.gazdacentrum.hu
- Hosting: Cloudflare Pages
- GitHub: vasotto/gazdacentrum
- Branch: main
- Technológia: HTML, JavaScript, JSON, Python

Alapelv: egyszerű, olcsó, kevés függőséggel működő rendszer. Indokolatlan frameworkváltás, fizetős szolgáltatás vagy túlzott komplexitás nem javasolható.

## 5. Aktuális fő irány

Elsődleges funkció: **Agrárhatáridők és teendők**.

Az első stabil production változat 2026. július 24-én lezárult. A production `naptar.html` a főoldalról elérhető, mobilon és asztali gépen ellenőrzött.

A cél nem havi naptár, hanem szűrhető, időrendi, közérthető, mobilon jól használható és hivatalos forrásra visszavezethető teendőlista.

Minden tételnél lehetőleg látszódjon:
- teendő;
- nyitás;
- lejárat;
- érintettek;
- ágazat;
- határidőtípus;
- hivatalos forrás;
- ellenőrzési dátum;
- szükség esetén részletes adatlap.

Szabályok:
- a havi naptárnézetet elvetettük;
- relatív határidők ne jelenjenek meg a fő listában;
- pályázatonként csak a következő aktív vagy megnyíló szakasz jelenjen meg;
- lejárt tételek alapból rejtve legyenek;
- egynapos jövőbeli határidőnél „esedékes”, ne „nyílik” jelenjen meg.

## 6. Próbafájlok és production

### naptar-proba.html
Megőrzött fejlesztési próbafelület. Új funkciót továbbra is itt vagy külön próbafájlban kell tesztelni.

### naptar.html
Az első stabil, szűrhető production teendőlista. Mobilon és asztali gépen ellenőrzött, a főoldal `Határidők` hivatkozásáról elérhető. További cseréje ezután is csak felhasználói jóváhagyással és visszaállítható commitban történhet.

### naptar-szinproba.html
Külön vizuális próbafelület. Jelenlegi paletták:
- Grafit–petrol
- Palakék–ibolya
- Meleg grafit–bronz
- Semleges grafit

A próbafájl négy korábbi palettája nem production forrás. A productionben a jóváhagyott türkiz/petrol–tengerészkék–lime arculat működik.

## 7. Szűrőrendszer

Határidőtípus:
- Pályázat
- Kifizetés
- Adatszolgáltatás
- Kötelezettség
- Bejelentés

Ágazat:
- Szántóföld
- Kertészet
- Állattenyésztés
- Erdőgazdálkodás
- Ökológiai gazdálkodás
- Általános

Időszak:
- Most nyitott
- 30 napon belül
- 90 napon belül
- Későbbi

További működés:
- lejárt tételek külön kapcsolóval;
- „Szűrők törlése” gomb;
- azonnali frissítés;
- a találati összesítő a ténylegesen látható tételeket számolja.

## 8. deadlines.json

Aktuális séma: `schema_version: 2`

Aktuális production állapot:
- 18 rekord;
- ebből 8 új, hivatalos forrásból ellenőrzött 2026-os tétel 2026. július 24-én került productionbe;
- 6 bizonytalan jelölt és 1 duplikátum nem került productionbe;
- nincs ismétlődő rekordazonosító;
- az `Általános` ágazati elnevezés maradt.

Fontos mezők:
`id`, `title`, `action`, `affected`, `start_date`, `deadline_date`, `deadline_text`, `reference_code`, `source_name`, `source_url`, `verified_at`, `deadline_type`, `sectors`, `action_type`, `date_type`, `show_in_main_list`.

A státuszt nem tároljuk fixen; a felület számolja ki.

Relatív rekord:
```json
{
  "date_type": "relative",
  "show_in_main_list": false
}
```

Egynapos rekordnál `start_date` és `deadline_date` azonos lehet. A státuszszöveg: „Ma esedékes”, „Holnap esedékes” vagy „X nap múlva esedékes”.

Új rekord előtt ellenőrizni kell:
- hivatalos forrás;
- év;
- dátumtípus;
- kezdő és záró dátum;
- érintettek;
- teendő;
- kivételek;
- módosítások;
- ellenőrzés dátuma.

Tilos kitalálni hiányzó dátumot, jogosultságot, összeget, intenzitást, minimum pontszámot, szankciót, kötelező dokumentumot vagy érintetti kört.

## 9. Ellenőrzött példák

Az eddig kezelt tételek között szerepel:
- KAP-RD46-1-25;
- KAP-RD38-RD39-1-25;
- HMKÁ 6 minimális talajborítás;
- 2026. évi Gazdálkodási Napló eGN-rögzítése;
- 2026. évi nitrát-adatszolgáltatás;
- 2026. évi tavaszi fagykár-bejelentés;
- 2026. évi Egységes Kérelem;
- egy relatív kifizetési szabály, rejtve a fő listában.

A 2026. július 24-én productionbe került 8 új tétel:
- KAP-RD42a-1-26 – zártkerti infrastruktúra;
- KAP-RD06-1-25 – gazdaságátvevő támogatása;
- KAP-RD44-1-26 – termelői csoportok és szervezetek támogatása;
- értékesítési jelentés benyújtása;
- KAP-RD21-RD22-2-25 – természetközeli és vizes élőhelyek;
- új borszőlőültetvény telepítési engedély iránti kérelem;
- KAP-RD07-1-25 – gazdaságátadási együttműködés;
- KAP-RD09a-2-26 – mezőgazdasági kisüzemek beruházási támogatása.

Új chatben a tényleges repository és deadlines.json alapján kell ellenőrizni, mi van valóban a main ágon.

## 10. Pályázati rendszer

Jelenlegi részletes pályázatok:
- KAP-RD46-1-25;
- KAP-RD38-RD39-1-25.

A részletes oldalon szerepeljen:
- jogosultság;
- támogatási összeg;
- intenzitás;
- minimum pontszám;
- beadási szakaszok;
- kötelezettségek;
- kizárások;
- buktatók;
- dokumentumok;
- módosítások;
- ellenőrzés dátuma;
- figyelmeztetés.

Külön kell választani a hivatalos tényt és a GazdaCentrum magyarázatát.

## 11. Hírgyűjtés és jog

Folyamat:
`RSS → fetch_news.py → news.json → index.html → Cloudflare Pages`

A workflow kézzel és hatóránként fut.

Nyilvánosan csak:
- kategória;
- cím;
- forrás;
- idő;
- eredeti link.

RSS-összefoglaló csak belső feldolgozásra használható.

Új forrás csak jogi és technikai ellenőrzés után kerülhet a sources.csv fájlba. Az Agrárközösség inaktív.

Tilos teljes külső cikket vagy engedély nélküli képet átvenni. Mindig kell forrás, dátum és eredeti link. Scraping csak külön jogi és technikai vizsgálat után javasolható. A SOURCE_AUDIT.md kockázatait figyelembe kell venni.

## 12. Vizuális irány

Elfogadott production irány:
- türkiz/petrol fő márkaszín;
- tengerészkék fejlécek és sötét felületek;
- lime csak fontos kiemelésekhez;
- világos, enyhén hideg szürke oldalháttér és fehér kártyák;
- ne legyen tipikus zöld agrárportál.

Az új logó és a türkiz/petrol–tengerészkék–lime arculat productionben működik. A production `index.html` világos és sötét módban ellenőrzött. Új vizuális irány elfogadásáig továbbra is csak próbafájl vagy látványterv készülhet.

## 13. Fejlesztési sorrend

1. Agrárhatáridők, pályázati adatlapok, hivatalos közlemények, meglévő hírrendszer stabil fenntartása.
2. AI-segített hivatalos összefoglalók, hírlevél, felhasználói fiókok és értesítések.
3. Szerelői tudásbázis, szerelőközvetítés, használtgép-értékbecslő.

Későbbi szakasz nem kezdhető meg, amíg az előző alapfunkciói nem stabilak.

Az automatikus határidő-adatgyűjtő még nincs elkészítve. Később csak emberi jóváhagyási lépéssel működhet.

A következő kiválasztott különálló próbafejlesztés a használtgép-értékbecslő. Ez még nem production funkció, és a próbafejlesztés nem módosíthatja automatikusan a production oldalakat vagy adatokat.

## 14. Új ötletek kezelése

Új ötletnél előbb tisztázni kell:
1. melyik fejlesztési szakaszhoz tartozik;
2. milyen felhasználói problémát old meg;
3. érint-e hivatalos agráradatot vagy személyes adatot;
4. igényel-e fizetős szolgáltatást vagy új technológiát;
5. kell-e próbafájl;
6. kell-e Work;
7. mik az elfogadási feltételek;
8. hogyan állítható vissza.

Az új ötlet nem kerül automatikusan a fejlesztési sorrend elejére.

## 15. Chat és Work

Chat feladata:
- irány és cél meghatározása;
- hivatalos adatok egyenkénti ellenőrzése;
- képernyőképek elemzése;
- egyetlen fájl kisebb módosítása;
- lépésenkénti hibakeresés;
- Work-eredmény ellenőrzése;
- GitHub- és Cloudflare-lépések irányítása;
- production csere jóváhagyása.

Work feladata lehet:
- teljes repository vizsgálata;
- több fájlt érintő előre meghatározott módosítás;
- dokumentációszinkron;
- nagyobb forráskutatás;
- automatizált ellenőrzések;
- teljes ZIP;
- összetett próbaváltozat.

Work nem dönthet önállóan:
- projektirányról;
- prioritásról;
- production cseréről;
- adatmodell jelentős módosításáról;
- hivatalos agráradat publikálásáról;
- új forrás engedélyezéséről;
- scrapingről;
- fizetős szolgáltatásról;
- technológiaváltásról.

Work előtt Chatben rögzíteni kell:
- célt;
- kiinduló fájlt vagy ZIP-et;
- érintett és tiltott fájlokat;
- jogi és adatkorlátozásokat;
- elfogadási feltételeket;
- ellenőrzéseket;
- kimeneti fájlokat;
- emberi ellenőrzési pontokat;
- commit üzenetet.

Work után Chatben ellenőrizni kell:
- ZIP és fájlstruktúra;
- módosított fájlok;
- tiltott fájl változott-e;
- JSON és JavaScript;
- helyi hivatkozások;
- dokumentáció pontossága;
- kitalált agráradat hiánya;
- production fájl változása;
- mobil- és vizuális teszt szükségessége.

## 16. Work-prompt alapsablon

```text
A feltöltött ZIP a GazdaCentrum repository legfrissebb pillanatfelvétele.

Feladat:
[PONTOS CÉL]

Érintett fájlok:
[FÁJLOK]

Nem módosítható fájlok:
[TILTOTT FÁJLOK]

Korlátozások:
- a production forrás a GitHub main ág;
- hivatalosan nem ellenőrzött agráradatot ne találj ki;
- production fájlt csak külön engedéllyel módosíts;
- a hírrendszert és sources.csv fájlt ne módosítsd külön engedély nélkül;
- ne változtass projektirányt vagy prioritást;
- minden módosítás legyen visszaállítható.

Elfogadási feltételek:
[FELTÉTELEK]

Ellenőrizd:
- JSON-fájlok érvényességét;
- HTML és JavaScript szintaxist;
- helyi fájlhivatkozásokat;
- dokumentációk összhangját;
- próbafájlok és production fájlok elkülönítését.

Készíts:
1. teljes letölthető eredményt;
2. módosított fájlok listáját;
3. nem módosított fájlok listáját;
4. ellenőrzési jelentést;
5. emberi ellenőrzést igénylő pontokat;
6. javasolt commit üzenetet.
```

## 17. Munkamód nem programozó felhasználóval

Technikai feladatnál:
- egyszerre csak egy konkrét lépés;
- eredmény vagy képernyőkép megvárása;
- pontos fájl-, gomb- és menünevek;
- tiltott módosítások jelzése;
- minden változtatás után ellenőrzés.

Kézi kódmódosításnál:
- fájlnév;
- keresendő rész;
- cserélendő rész;
- teljes kód;
- commit üzenet;
- ellenőrzés.

Feltölthető fájl kérésénél teljes letölthető fájl készítendő.

## 18. Hibakeresési sorrend

1. commit;
2. main ág;
3. GitHub Actions;
4. kapcsolódó JSON;
5. Cloudflare Pages deploy;
6. pages.dev;
7. saját domain;
8. cache;
9. JavaScript-hiba;
10. fájlnév;
11. érvényes JSON.

Nem szabad találgatni, amíg ezek nincsenek ellenőrizve.

## 19. Dokumentáció

Karbantartandó:
- GAZDACENTRUM_PROJEKT_PROTOKOLL.md;
- PROJECT_STATUS.md;
- TODO.md;
- CHANGELOG.md;
- README.md;
- SOURCE_AUDIT.md.

Külön kell választani:
- production állapot;
- működő próbaváltozat;
- tesztelt, de nem elfogadott elem;
- későbbi terv.

## 20. AI-használat

AI használható előzetes feldolgozásra, forráskutatásra, strukturálásra, közérthető megfogalmazásra, ellenőrzőlistára, próbafájlokra, kódváltozatokra és dokumentációszinkronra.

AI nem publikálhat emberi ellenőrzés nélkül:
- határidőt;
- jogosultságot;
- pontszámot;
- támogatási összeget;
- intenzitást;
- szankciót;
- kötelező dokumentumot;
- hatósági előírást;
- hivatalos érintetti kört.

## 21. Új chat indítása

Új chatben:
1. ellenőrizni kell, hogy ugyanabban a GC projektben vagyunk;
2. el kell olvasni ezt a protokollt;
3. ellenőrizni kell a legfrissebb ZIP-et vagy aktuális fájlt;
4. át kell tekinteni a PROJECT_STATUS.md, CHANGELOG.md és TODO.md fájlokat;
5. nem szabad kizárólag korábbi beszélgetés emlékére hagyatkozni;
6. csak egy következő konkrét lépést kell adni.

Kezdőprompt:

```text
Folytassuk a GazdaCentrum projektet.

Elsőként olvasd el a projekt forrásai között található
GAZDACENTRUM_PROJEKT_PROTOKOLL.md fájlt.

Ezután állapítsd meg az aktuális állapotot:
1. az aktuálisan feltöltött fájl vagy repository ZIP;
2. PROJECT_STATUS.md;
3. CHANGELOG.md;
4. TODO.md alapján.

Ne kezdj még módosításba.
Először röviden írd le, hol tart a projekt, mi a jelenlegi fő irány,
és melyik a következő ellenőrizendő feladat.
Ezután csak egy konkrét lépést adj.
```

## 22. Chat lezárása és állapotátadás

Hosszú chat végén készíteni kell rövid állapotátadást:
- utolsó igazolt működő állapot;
- legutóbb módosított fájl;
- utolsó commit vagy tervezett commit;
- még nem ellenőrzött változtatások;
- következő konkrét feladat;
- tiltott vagy halasztott módosítások;
- szükséges feltöltendő fájlok.

A repository main ág és az aktuális fájl mindig elsődleges az állapotátadással szemben.

## 23. Napi munkamenet

1. Chat: állapot megállapítása.
2. Chat: következő feladat kiválasztása.
3. Chat: cél, korlátok és elfogadási feltételek.
4. Chat: hivatalos adat ellenőrzése.
5. Chat: döntés Chat vagy Work között.
6. Work: csak az előre meghatározott részfeladat.
7. Chat: Work-eredmény ellenőrzése.
8. Chat: GitHub-feltöltés egy lépésben.
9. Chat: Cloudflare deploy és megjelenés ellenőrzése.
10. Chat: dokumentációfrissítés vizsgálata.

## 24. Rövid döntési szabály

Chat:
- egyetlen fájl vagy hiba;
- emberi döntés;
- hivatalos adat;
- képernyőkép;
- lépésenkénti munka.

Work:
- több fájl;
- teljes repository;
- nagyobb kutatás;
- automatizált ellenőrzés;
- teljes ZIP vagy összetett próbaváltozat.

## 25. Legfontosabb alapelv

> A Chat tervezi és ellenőrzi a munkát.  
> A Work csak az előre pontosan meghatározott nagyobb részfeladatot hajtja végre.  
> Hivatalos agráradat és production módosítás emberi ellenőrzés nélkül nem publikálható.
