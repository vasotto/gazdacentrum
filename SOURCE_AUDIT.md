# GazdaCentrum forrásaudit

Utolsó frissítés: 2026-07-19

## Cél

Ez a dokumentum rögzíti a GazdaCentrum aktív és kizárt forrásainak jogi, technikai és tartalmi vizsgálatát. Egy forrás csak akkor tekinthető véglegesen jóváhagyottnak, ha a felhasználási feltételei, az RSS/API működése, a megjeleníthető adatok köre és a szükséges szűrések dokumentálva vannak.

## Státuszok

- **Használható:** a dokumentált feltételek mellett aktívan használható.
- **Feltételes:** használható lehet, de megjelenítési módosítás, engedély vagy további ellenőrzés szükséges.
- **Céges forrás:** csak a külön céges szakmai tartalmak rovatban használható.
- **Függőben:** az audit még nem készült el.
- **Kizárva:** nem használható.

## Aktív források áttekintése

| Sorszám | Forrás | Típus | RSS/API | Auditállapot | Következő teendő |
|---:|---|---|---|---|---|
| 1 | Agrárszektor | portál | nyilvános RSS | **Feltételes** | Megjelenítési szabály pontosítása |
| 2 | Agro Napló | portál | RSS | Függőben | Jogi és technikai audit |
| 3 | Magyar Mezőgazdaság | portál | RSS | Függőben | Jogi és technikai audit |
| 4 | Mezőhír | portál | RSS | Függőben | Jogi és technikai audit |
| 5 | Agrofórum | portál | RSS | Függőben | Jogi és technikai audit |
| 6 | AKI | hivatalos | RSS | Függőben | Felhasználási és technikai audit |
| 7 | ÖMKi | szakmai | RSS | Függőben | Felhasználási és technikai audit |
| 8 | FruitVeB | szakmai | RSS | Függőben | Felhasználási és technikai audit |
| 9 | Agrárközösség | portál | RSS | Függőben | Jogi és technikai audit |
| 10 | Agroinform | portál | RSS | Függőben | Jogi és technikai audit |
| 11 | Phylazonit | céges | RSS | Céges forrás – technikailag tesztelve | Felhasználási feltételek dokumentálása |
| 12 | Magtár Kft. | céges | RSS | Céges forrás – technikailag tesztelve | Felhasználási feltételek dokumentálása |
| 13 | KAP portál | hivatalos | RSS | Függőben | Felhasználási és technikai audit |

## 1. Agrárszektor

### Alapadatok

- **Forrás típusa:** szerkesztőségi portál
- **Kiadó:** Net Média Zrt.
- **RSS:** a portál láblécében hivatalosan hivatkozott RSS-végpont
- **Jelenlegi GazdaCentrum-megjelenítés:** cím, forrás, dátum és közvetlen cikklink

### Jogi megállapítás

Az Agrárszektor jogi nyilatkozata szerint a tartalom a kiadó szellemi tulajdona. A lap részeinek feldolgozása, adatbázisban tárolása, tükrözése és továbbközvetítése előzetes írásos hozzájárulás nélkül korlátozott.

A részletes felhasználási feltételek a hiperhivatkozást kifejezetten az alábbi formában engedik:

> Forrás: Agrárszektor.hu

Ehhez a forrásanyagot tartalmazó aloldal közvetlen linkjét kell használni. A feltételek az ettől eltérő tartalomátvételt jogsértőként írják le.

A jogi nyilatkozat ugyanakkor megengedi az értesülések átvételét egyértelmű hivatkozással és az eredeti információ módosítása nélkül. A két szöveg együtt nem ad teljesen egyértelmű engedélyt arra, hogy egy automatizált, nyilvános adatbázis az eredeti cikkcímeket rendszeresen átvegye.

### Ideiglenes auditdöntés

- **Státusz:** Feltételes
- **Biztosan megengedett:** közvetlen hivatkozás az előírt forrásmegjelöléssel
- **Nem használható:** kivonat, kép, teljes szöveg vagy más tartalmi rész
- **Nem egyértelmű:** eredeti cikkcím rendszeres automatikus megjelenítése
- **Javasolt óvatos megoldás:** írásos engedély kérése a cím + dátum + közvetlen link automatizált megjelenítésére

### Szükséges későbbi technikai ellenőrzés

1. A GazdaCentrum forrásfeliratának pontosan „Forrás: Agrárszektor.hu” formára állítása, amennyiben a forrás aktív marad.
2. Fizetett vagy támogatott tartalmak felismerése és elkülönítése/kiszűrése.
3. Annak ellenőrzése, hogy az RSS-ben szereplő cím megjelenítése belefér-e a kiadó írásos hozzájárulása nélkül.
4. Írásos válasz vagy engedély archiválása a repository dokumentációjában.

### Vizsgált hivatalos dokumentumok

- Agrárszektor – Jogi nyilatkozat: https://www.agrarszektor.hu/info/jogi-nyilatkozat
- Agrárszektor – Felhasználási feltételek: https://cdn.portfolio.hu/files/a/agrarszektor-felhasznalasi-feltetelekk.pdf

## Kizárt források

| Forrás | Döntés | Indok |
|---|---|---|
| GÉPmax | Kizárva | A korábbi vizsgálat alapján a linkelést/felhasználást nem engedi a GazdaCentrum tervezett formájában. |

## Auditfolyamat

A forrásokat egyenként vizsgáljuk. A következő forrás auditja csak az előző eredményének rögzítése után kezdődik.
