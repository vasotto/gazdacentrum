# GazdaCentrum – feladatlista

Utolsó frissítés: 2026. július 21.

## Következő konkrét feladat

- [ ] Döntés a Mezőhír, AKI és Agroinform átmeneti kikapcsolásáról vagy írásos engedélykéréséről.

## Kritikus jogi és tartalmi feladatok

- [ ] Egységes engedélykérő levél elkészítése a külső hírforrásokhoz.
- [ ] Agrárszektor használati feltételeinek írásos pontosítása.
- [ ] Agro Napló cím-, dátum- és linkhasználatának írásos pontosítása.
- [ ] Magyar Mezőgazdaság írásos megerősítésének kérése.
- [ ] Mezőhír engedélyének rendezése.
- [ ] Agrofórum írásos megerősítésének kérése.
- [ ] AKI engedélyének rendezése.
- [ ] ÖMKi felhasználási feltételeinek tisztázása.
- [ ] FruitVeB felhasználási feltételeinek tisztázása.
- [ ] Agroinform engedélyének rendezése.
- [ ] Phylazonit partneri hozzájárulásának archiválása.
- [ ] Magtár Kft. partneri hozzájárulásának archiválása.
- [ ] Adatkezelési tájékoztató elkészítése.
- [ ] Az impresszum hiányzó adószámának és nyilvántartási számának pótlása.

## Aktív RSS-források

- [x] 12 aktív forrás rögzítése a `sources.csv` fájlban.
- [x] Agrárközösség ideiglenes kikapcsolása a hibás vagy blokkolt feed miatt.
- [x] Phylazonit elkülönített céges forrásként.
- [x] Magtár Kft. elkülönített céges forrásként.
- [x] Magtár `AKCIÓK` kategória kizárása.
- [x] KAP portál hivatalos forrásként.
- [ ] Új forrásokat továbbra is egyenként tesztelni.

## Hírgyűjtés és kategorizálás

- [x] Háromszori RSS-újrapróbálás.
- [x] HTML- és RSS-zárószöveg-tisztítás.
- [x] Nyilvános összefoglalók eltávolítása a `news.json` fájlból.
- [x] `(x)` jelölésű Agro Napló tartalmak kizárása.
- [x] Magtár gépes híreinek `Gépesítés` kategóriába rendezése.
- [x] `Mezőgazdasági gépek` → `Gépesítés` kategóriaegységesítés.
- [x] Főoldali Gépesítés kártya partneri tartalomhoz irányítása, ha nincs független gépes hír.
- [ ] Kategóriánkénti forráseloszlás rendszeres ellenőrzése.
- [ ] Erdészeti és vadgazdálkodási kategória szükségességének vizsgálata.
- [ ] További irreleváns életmód- és fogyasztói elemek szűrése.

## Duplikációszűrés

- [x] Azonos linkek szűrése.
- [x] Azonos címek szűrése.
- [x] Azonos vagy közel azonos belső összefoglalók szűrése.
- [x] Források közötti tartalmi hasonlóság vizsgálata.
- [x] Láncolt duplikációk kezelése.
- [x] Hivatalos → szakmai → portál forrásprioritás.
- [ ] Duplikációs hibák időszakos mintavételes ellenőrzése.

## Weboldal

- [x] Reszponzív főoldal.
- [x] Mobilon tördelődő felső menü.
- [x] Kategóriaszűrők.
- [x] Elkülönített céges tartalmi rovat.
- [x] Határidők szakasz.
- [x] Pályázati listaoldal.
- [x] Lejárt, nyitott és jövőbeli benyújtási szakaszok eltérő színezése.
- [x] Két részletes pályázati adatlap.
- [x] Mobilbarát részletes pályázati oldalak.
- [x] Világos és sötét mód.
- [ ] Külön kategóriaoldalak.
- [ ] Kereső.
- [ ] Hírlevél.
- [ ] Végleges Facebook-felhasználónév után Facebook-link kihelyezése.

## Pályázati rendszer

- [x] `deadlines.json` adatmodell.
- [x] `grants.json` adatmodell.
- [x] KAP-RD46-1-25 részletes adatlap.
- [x] KAP-RD38-RD39-1-25 részletes adatlap.
- [x] Egységes `PALYAZATI_ADATLAP_SABLON.md`.
- [x] Minimum pontszám feltüntetése a részletes oldalakon.
- [x] Benyújtási szakaszok külön rekordként kezelése.
- [ ] Pályázati dokumentumok automatikus változásfigyelése.
- [ ] IH-közlemények pályázatkódhoz rendelése.
- [ ] Részletes adatlapok adatvezérelt generálása a kézi HTML helyett.
- [ ] Előzetes jogosultsági és pontszám-ellenőrző tervezése.
- [ ] Emberi jóváhagyási folyamat kialakítása AI-val készített összefoglalókhoz.


## Használtgép-értékbecslő

- [ ] A használt mezőgazdasági gépek értékbecslő funkciójának célját, célcsoportját és első kiadását meghatározni.
- [ ] Az első támogatott gépkategóriát kiválasztani; kezdetben egyetlen jól összehasonlítható kategóriával indulni.
- [ ] Strukturált gépadatlap megtervezése: márka, modell, kivitel, gyártási év, üzemóra, teljesítmény, hajtás, felszereltség, munkaszélesség, gumiabroncsok, műszaki állapot és ismert hibák.
- [ ] Fotófeltöltés és állapotfelmérési ellenőrzőlista kialakítása.
- [ ] Külön kezelni a nettó és bruttó árat, az áfaállapotot, a kereskedői és magánhirdetői árat, valamint a magyar és külföldi piacot.
- [ ] Jogszerű és fenntartható piaci adatforrásokat felkutatni: partneri adatátadás, API, engedélyezett hirdetési feed vagy kézi adatbevitel.
- [ ] Engedély nélküli hirdetésmásolás és scraping kizárása külön jogi vizsgálat nélkül.
- [ ] Összehasonlítható gépek kiválasztási szabályait kidolgozni márka, modell, kor, üzemóra, felszereltség, állapot és régió alapján.
- [ ] Az értékbecslés eredményét ársávként megjeleníteni, nem egyetlen garantált eladási árként.
- [ ] Bizalmi szint vagy adatminőségi jelzés megjelenítése a felhasznált összehasonlító adatok száma és frissessége alapján.
- [ ] Külön becslést tervezni várható hirdetési árra, reális eladási árra és kereskedői beszámítási értékre.
- [ ] Értékmódosító tényezők kidolgozása: üzemóra, szervizelőélet, dokumentált javítások, gumiállapot, korrózió, sérülés, extra felszereltség és szezonális kereslet.
- [ ] A szerelői tudásbázissal való későbbi összekapcsolás megtervezése, hogy az ismert típushibák és dokumentált javítások befolyásolhassák az értékelést.
- [ ] A szerelői állapotfelmérés vagy helyszíni értékbecslés közvetítésének későbbi lehetőségét megvizsgálni.
- [ ] Menthető értékbecslési adatlap és letölthető, dátummal ellátott tájékoztató jelentés tervezése.
- [ ] Egyértelmű jogi figyelmeztetés készítése arról, hogy az automatikus becslés tájékoztató jellegű, nem hivatalos igazságügyi vagy banki értékbecslés.
- [ ] Az AI szerepét korlátozni adatnormalizálásra, hasonló gépek csoportosítására, fotók előzetes állapotjelzéseire és magyarázó összefoglalóra; az AI önmagában ne állapítson meg garantált piaci értéket.
- [ ] Első egyszerű változat megtervezése: kézi gépadatlap, néhány ellenőrzött összehasonlító adat, becsült ársáv, adatminőségi jelzés és emberi felülvizsgálat.

## Szerelői kapu és javítási információk

- [ ] „Szerelői kapu” funkció követelményeinek és jogi kereteinek részletes felmérése.
- [ ] A mezőgazdasági gépekre és traktorokra vonatkozó uniós javítási, karbantartási és adathozzáférési szabályok összefoglalása.
- [ ] Hivatalos gyártói szervizinformációs és diagnosztikai portálok márkánkénti adatbázisa.
- [ ] Márka-, géptípus-, modell- és információtípus-alapú kereső tervezése.
- [ ] Regisztrációs, díjfizetési és jogosultsági útmutató készítése gyártónként.
- [ ] Tulajdonosi meghatalmazás és adatmegosztási kérelem mintájának megtervezése.
- [ ] Szerelői hozzáférési problémák és gyártói elutasítások naplózási lehetőségének tervezése.
- [ ] Annak rögzítése, hogy a GazdaCentrum csak hivatalos hozzáférési pontokat közvetít, és nem tárol engedély nélkül gyártói kézikönyveket, diagnosztikai programokat, firmware-t vagy licenckulcsokat.

## Szerelői tudásbázis

- [ ] A szerelői tudásbázis céljának, felhasználói körének és első kiadásának pontos meghatározása.
- [ ] Strukturált javítási eset-adatlap megtervezése: gépkategória, márka, modell, évjárat vagy széria, üzemóra, hibakód, tünet, diagnosztikai lépések, valódi hibaok, javítás, alkatrész, szerszám, munkaidő és utóellenőrzés.
- [ ] Márka-, modell-, hibakód-, tünet- és alkatrész-alapú keresés megtervezése.
- [ ] Képek, videók és mérési eredmények biztonságos feltöltésének megtervezése.
- [ ] Személyes adatok, rendszámok, teljes alvázszámok és ügyféladatok automatikus maszkolása.
- [ ] Duplikált vagy közel azonos javítási esetek felismerésének megtervezése.
- [ ] AI-segéd tervezése a szabad szöveg strukturált adatlapra alakításához és a hiányzó mezők jelzéséhez.
- [ ] Annak rögzítése, hogy az AI nem minősítheti önállóan szakmailag helyesnek a javítási megoldást.
- [ ] Többlépcsős minőségellenőrzés kialakítása: automatikus ellenőrzés, közösségi megerősítés és szakmai moderáció.
- [ ] Javítási esetenkénti minőségi pontszám kidolgozása a teljesség, bizonyíték, megerősítés és tartós eredmény alapján.
- [ ] Szerelői reputációs rendszer kidolgozása, amely nem csak a feltöltések számát, hanem azok minőségét is értékeli.
- [ ] Szakmai visszajelzési lehetőségek tervezése: „Nálam is működött”, „Más hibaok volt”, „Pontosítás szükséges”, „Biztonsági kockázat”.
- [ ] Verziókövetés és javítási előzmények megőrzése minden esetadatlapnál.
- [ ] Jutalmazási rendszer megtervezése: tudáspont, hozzáférési kredit, szakértői jelvény, jobb profilmegjelenés és későbbi bevételmegosztás.
- [ ] A gyenge, másolt vagy mesterségesen tömeges feltöltést ösztönző automatikus darabdíjas modell kizárása.
- [ ] Tiltott tartalmak szabályzatának elkészítése: kiszivárgott gyári dokumentáció, tört diagnosztikai program, licenckulcs, biztonsági vagy emissziós rendszer kiiktatása, üzemóra- és azonosító-manipuláció.
- [ ] Kiemelten veszélyes javítások külön moderációja: fék, kormányzás, nagyfeszültség, hidraulika, biztonsági reteszelés, motorvezérlés és vezérlőprogramozás.
- [ ] Első egyszerű változat megtervezése: beküldő űrlap, kézi ellenőrzés, kereshető esetlista, „Nálam is működött” visszajelzés és szerelői profil.

## Szerelőközvetítés

- [ ] A szerelőközvetítés üzleti, jogi és felelősségi modelljének megtervezése.
- [ ] Gazdálkodói hibabejelentő adatlap kialakítása: gép, modell, helyszín, tünet, hibakód, sürgősség, helyszíni vagy műhelyjavítás, fénykép és kívánt időpont.
- [ ] A pontos cím és közvetlen elérhetőség védett kezelése; csak a kiválasztott szerelő kapja meg.
- [ ] Szerelői profil kialakítása: vállalt márkák, géptípusok, régió, kiszállás, diagnosztikai eszközök, végzettség, vállalkozás, felelősségbiztosítás és rendelkezésre állás.
- [ ] A tudásbázisban elért szakmai reputáció összekapcsolása a szerelőkereső találati sorrendjével.
- [ ] Külön közvetítési módok tervezése: sürgős gépmentés, tervezett javítás, speciális diagnosztika, márkaspecialista és második szakvélemény.
- [ ] Szerelői ajánlatadás vagy vállalási időpont megadásának kialakítása.
- [ ] Csak ténylegesen közvetített munkához kapcsolódó, hitelesített értékelési rendszer megtervezése.
- [ ] Az értékelés külön szempontjai: kommunikáció, pontosság, szakmai munka, ár-átláthatóság és utókövetés.
- [ ] Panaszkezelési, vitakezelési és ideiglenes profilfelfüggesztési folyamat kidolgozása.
- [ ] Annak egyértelmű rögzítése, hogy a GazdaCentrum közvetítő, nem a javítás kivitelezője.
- [ ] Első üzleti modell vizsgálata: ingyenes próba, havi szerelői tagság, kiemelt profil és meghatározott számú ajánlatadás.
- [ ] Későbbi bevételi lehetőségek vizsgálata: sikeres közvetítési díj, online fizetés és számlázási támogatás.
- [ ] A szerelőközvetítés fejlesztését csak a tudásbázis, a profilrendszer és a minőségellenőrzés működő alapjai után megkezdeni.

## Felhasználó által kérhető AI-összefoglalók

- [ ] Az „AI-összefoglaló kérése” funkció céljának, első támogatott tartalomtípusainak és felhasználói korlátainak meghatározása.
- [ ] Első körben kizárólag hivatalos KAP-közleményekre, pályázati hírekre és más engedélyezett hivatalos forrásokra korlátozni.
- [ ] A megjelenő összefoglaló egységes szerkezetét kialakítani: mi történt, kiket érint, mi változott, mit kell tenni, milyen határidő van, miért fontos, mit kell a hivatalos forrásból ellenőrizni.
- [ ] Az eredeti forrás, dátum és közvetlen link folyamatos megjelenítését kötelezővé tenni.
- [ ] Külső híroldalaknál csak jogszerűen felhasználható RSS-kivonatból, API-adatból, partneri tartalomból vagy külön engedéllyel elérhető szövegből dolgozni.
- [ ] Engedély nélküli teljes cikkletöltést, nyilvános újraközlést és teljes szövegű AI-feldolgozást kizárni.
- [ ] Cloudflare Worker vagy Pages Function alapú háttérrendszert tervezni, hogy az AI API-kulcs ne kerüljön a böngészőbe.
- [ ] Kérésenkénti feldolgozást alkalmazni az összes hír előzetes összefoglalása helyett.
- [ ] Az elkészült összefoglalók gyorsítótárazását megtervezni, hogy ugyanahhoz a forráshoz ne kelljen minden alkalommal új AI-hívás.
- [ ] Napi és felhasználónkénti kérési limiteket, túlterhelés elleni védelmet és hibakezelést kialakítani.
- [ ] Az összefoglalóhoz rögzíteni a forrást, a dokumentumverziót, az elkészítés idejét és az ellenőrzési státuszt.
- [ ] Külön jelölni a forrásból közvetlenül következő tényeket és a GazdaCentrum magyarázó értelmezéseit.
- [ ] Megtiltani, hogy az AI hiányzó határidőt, támogatási összeget, jogosultsági feltételt vagy jogi következményt találjon ki.
- [ ] Bizonytalan adatnál kötelező szöveget használni: „A rendelkezésre álló forrásból ez nem állapítható meg biztosan.”
- [ ] Támogatási, jogszabályi, pénzügyi és növényvédelmi témánál kötelező hivatalos ellenőrzési figyelmeztetést megjeleníteni.
- [ ] Rövid és részletes összefoglaló külön funkcióként való későbbi vizsgálata.
- [ ] Regisztrált felhasználói keret, előfizetés vagy kreditrendszer későbbi lehetőségének vizsgálata.
- [ ] Első pilotként egyetlen hivatalos közleménytípussal, kézi ellenőrzéssel és alacsony napi limittel indulni.

## Dokumentáció és üzemeltetés

- [x] `README.md` aktuális állapothoz igazítása.
- [x] `PROJECT_STATUS.md` karbantartása.
- [x] `CHANGELOG.md` karbantartása.
- [x] `SOURCE_AUDIT.md` elkészítése.
- [x] GitHub Actions hatóránkénti futása.
- [x] Cloudflare Pages automatikus deploy.
- [ ] Időszakos belső link- és JSON-ellenőrzés automatizálása.
- [ ] Hiba esetén a dokumentált ellenőrzési sorrend követése.
