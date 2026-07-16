# GazdaCentrum – feladatlista

Utolsó frissítés: 2026. július 16.

## Következő konkrét feladat

- [ ] A `CHANGELOG.md` frissítése a 2026. július 16-án elkészült fejlesztésekkel.

## Aktív RSS-források

- [x] Agrárszektor beállítása és tesztelése.
- [x] Agro Napló beállítása és tesztelése.
- [x] Magyar Mezőgazdaság beállítása és tesztelése.
- [x] Mezőhír beállítása és tesztelése.
- [x] Agrofórum beállítása és tesztelése.
- [x] AKI beállítása és tesztelése.
- [x] ÖMKi beállítása és tesztelése.
- [x] FruitVeB beállítása és tesztelése.
- [x] Agrárközösség beállítása és tesztelése.
- [x] Agroinform beállítása és tesztelése.
- [x] GÉPmax beállítása és tesztelése.
- [x] KAP portál beállítása és tesztelése.

Jelenlegi aktív források száma:

- 12

## Következő RSS-források

- [ ] További hivatalos agrárforrások keresése.
- [ ] További növénytermesztési források keresése.
- [ ] További állattenyésztési források keresése.
- [ ] További kertészeti források keresése.
- [ ] További támogatási és pályázati források keresése.
- [ ] Minden új forrás külön tesztelése a `sources.csv` bővítése előtt.
- [ ] A Phylazonit RSS-feed külön tesztelése partneri forrásként.
- [ ] A partneri RSS-források megjelenítési és jelölési szabályainak kialakítása a Phylazonit feed esetleges aktiválása előtt.

## Tesztelt, de inaktív források

- [x] Agrárágazat tesztelése – hibás XML-entitás miatt inaktív.
- [x] Agrotrend tesztelése – hibás XML-entitás miatt inaktív.
- [x] AgrárUnió tesztelése – nem található működő nyilvános RSS.
- [x] Agrokép tesztelése – a feed nem található vagy le van tiltva.
- [x] Haszon Agrár tesztelése – hibás feed miatt inaktív.
- [x] MAGRO tesztelése – hibás feed miatt inaktív.
- [x] Farmvilág tesztelése – hibás feed miatt inaktív.

## Hírgyűjtés és adatfeldolgozás

- [x] RSS-források beolvasása a `sources.csv` fájlból.
- [x] Legfeljebb 20 hír feldolgozása forrásonként.
- [x] Legfeljebb 200 hír mentése a `news.json` fájlba.
- [x] Cím, link, forrás, kategória és publikálási idő mentése.
- [x] Rövid RSS-összefoglalók tisztítása.
- [x] HTML-elemek eltávolítása.
- [x] HTML-karakterek dekódolása.
- [x] Az „appeared first on” zárószövegek eltávolítása.
- [x] A magyar „bejegyzés először ... jelent meg” zárószövegek eltávolítása.
- [x] Duplán érkező RSS-címek tisztítása.
- [x] Agroinform ismétlődő címeinek javítása.
- [x] KAP-portál összefoglalóinak tisztítása.
- [x] KAP-portál szerkesztői fejlécének eltávolítása.
- [x] Nyilvánvalóan nem agrár témájú hírek relevanciaszűrése.
- [x] Agroinform Házikert rovatának kizárása.
- [x] Agrofórum hobbikerti és lakossági szaktanácsadási rovatainak kizárása.
- [x] GÉPmax személyautós és SUV-híreinek kizárása.
- [x] Átmeneti RSS-hibák automatikus újrapróbálása.
- [x] Legfeljebb három RSS-lekérési kísérlet beállítása.
- [x] Öt másodperces várakozás beállítása az ismételt lekérések között.
- [x] Egyetlen hibás forrás mellett a többi forrás feldolgozásának folytatása.
- [x] RSS-hibák mentése a `news.json` `errors` mezőjébe.
- [ ] Tartósan hibás források külön, automatikus jelentése.
- [ ] A források frissességének rendszeres ellenőrzése.
- [ ] A hibás vagy elavult feedek időszakos felülvizsgálata.

## Duplikációszűrés

- [x] Azonos linkű hírek kiszűrése.
- [x] Csak záró perjelben eltérő linkek felismerése.
- [x] Azonos című hírek kiszűrése.
- [x] Címek normalizálása az összehasonlításhoz.
- [x] Különböző források hasonló tartalmú híreinek felismerése.
- [x] Azonos és közel azonos összefoglalók felismerése.
- [x] Legalább 80 karakteres összefoglalók összehasonlítása.
- [x] Rövid kiegészítésben eltérő összefoglalók felismerése.
- [x] Azonos forráson belül megjelenő másodpéldányok felismerése.
- [x] Láncoltan kapcsolódó duplikációk felismerése.
- [x] Forrástípus szerinti megtartási prioritás kialakítása.
- [x] Hivatalos forrás elsőbbségének beállítása.
- [x] Szakmai forrás elsőbbségének beállítása a portálokkal szemben.
- [x] Azonos forrástípusnál a frissebb hír előnyben részesítése.
- [x] A 72 órás duplikációs időablak beállítása.
- [x] Ukrán burgonyapiaci duplikáció tesztelése.
- [x] Agrofórum azonos kukoricás videó- és szakcikkváltozatának kiszűrése.
- [ ] A duplikációszűrés eredményeinek rendszeres ellenőrzése.
- [ ] További valós duplikációs példák dokumentálása.
- [ ] A téves összevonások időszakos ellenőrzése.
- [ ] A fel nem ismert duplikációk időszakos ellenőrzése.

## Kategorizálás

- [x] Forrásszintű kategóriák megadása a `sources.csv` fájlban.
- [x] Agrárgazdaság kategória használata.
- [x] Általános agrár kategória használata.
- [x] Kertészet kategória használata.
- [x] Gépesítés kategória használata.
- [x] Támogatások és pályázatok kategória használata.
- [x] Ökológiai gazdálkodás kategória használata.
- [ ] Cím és összefoglaló alapján automatikus kategorizálás.
- [ ] Növénytermesztés kategória.
- [ ] Állattenyésztés kategória.
- [ ] Időjárás és vízgazdálkodás kategória.
- [ ] Növényvédelem kategória.
- [ ] Egy híren belül több lehetséges kategória kezelésének szabályozása.
- [ ] A jelenlegi forrásszintű kategóriák felülvizsgálata.

## Weboldal

- [x] Cloudflare Pages hosting beállítása.
- [x] Saját domain bekötése.
- [x] A `gazdacentrum.hu` működésének ellenőrzése.
- [x] A `www.gazdacentrum.hu` működésének ellenőrzése.
- [x] HTTPS működésének ellenőrzése.
- [x] GazdaCentrum logó megjelenítése.
- [x] Hírek automatikus betöltése a `news.json` fájlból.
- [x] Kategória megjelenítése.
- [x] Forrás megjelenítése.
- [x] Publikálási idő megjelenítése.
- [x] RSS-összefoglaló megjelenítése.
- [x] Eredeti cikklink megjelenítése.
- [x] Az élő oldalon az Agrofórum-duplikáció eltávolításának ellenőrzése.
- [ ] Kategóriaszűrő kialakítása.
- [ ] Külön kategóriaoldalak kialakítása.
- [ ] Keresési funkció.
- [ ] Mobilos megjelenés részletes ellenőrzése.
- [ ] Forrásonkénti szűrés.
- [ ] Hírkártyák megjelenésének finomítása.
- [ ] Üres összefoglalóval érkező hírek megjelenésének felülvizsgálata.
- [ ] Hibaállapot megjelenítése, ha a `news.json` nem tölthető be.

## GitHub Actions és üzemeltetés

- [x] Az „Agrárhírek frissítése” workflow létrehozása.
- [x] Kézi workflow-indítás beállítása.
- [x] Hatóránkénti automatikus futás beállítása.
- [x] Python-függőségek automatikus telepítése.
- [x] A `fetch_news.py` automatikus futtatása.
- [x] A `news.json` automatikus frissítése.
- [x] A módosított `news.json` visszamentése a `main` ágra.
- [x] Cloudflare Pages automatikus deploy ellenőrzése.
- [ ] Tartós workflow-hiba esetére értesítés kialakítása.
- [ ] A workflow futási idejének és naplóinak időszakos ellenőrzése.
- [ ] A GitHub Actions jogosultságainak dokumentálása.

## Dokumentáció

- [x] `PROJECT_STATUS.md` létrehozása.
- [x] `PROJECT_STATUS.md` frissítése a 12 aktív forrással.
- [x] `TODO.md` létrehozása.
- [x] `README.md` létrehozása.
- [x] `CHANGELOG.md` létrehozása.
- [ ] `CHANGELOG.md` frissítése a legutóbbi fejlesztésekkel.
- [ ] `README.md` aktualizálása a jelenlegi működéshez.
- [ ] Az aktív és inaktív források rendszeres dokumentálása.
- [ ] A jelentős változtatások folyamatos rögzítése.

## Tartalmi és jogi feladatok

- [ ] Impresszum elkészítése.
- [ ] Adatkezelési tájékoztató elkészítése.
- [ ] Automatizált tartalom-előállításról szóló tájékoztatás.
- [ ] Hivatalos forrás ellenőrzésére figyelmeztető szöveg.
- [ ] Felhasználási feltételek elkészítése.
- [ ] Forráseltávolítási és panaszkezelési kapcsolat megadása.
- [ ] Az RSS-összefoglalók felhasználási módjának rendszeres jogi felülvizsgálata.

## Partneri és fizetett vállalati tartalmak

- [ ] A partneri RSS-források külön forrástípusának kialakítása.
- [ ] „Fizetett partneri tartalom” jelölés megjelenítése.
- [ ] A fizetett és független hírek egyértelmű elkülönítése.
- [ ] Partneri tartalmi feltételek kidolgozása.
- [ ] Partneri csomagok és árak kidolgozása.
- [ ] Partneri kattintási statisztikák kialakítása.
- [ ] A Phylazonit RSS-forrás tesztelése csak a partneri szabályok kialakítása után.

## Későbbi fejlesztések

- [ ] „Miért fontos a gazdának?” mező.
- [ ] AI-alapú saját összefoglaló.
- [ ] Napi vagy heti hírlevél.
- [ ] Támogatási határidőfigyelő.
- [ ] Személyre szabható hírfolyam.
- [ ] Kedvenc hírek mentése.
- [ ] Látogatottságmérés és forgalmi statisztikák.
- [ ] Közvetlen agrárhirdetési rendszer.

## Facebook

- [x] A Zetorvas Facebook-oldal átnevezése GazdaCentrumra.
- [ ] Végleges Facebook-felhasználónév beállítása.
- [ ] Facebook-link elhelyezése a weboldalon.
