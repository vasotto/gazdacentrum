# GazdaCentrum – projektállapot

Utolsó frissítés: 2026. július 15.

## 1. A projekt célja

A GazdaCentrum.hu egy teljesen vagy közel teljesen automatizált magyar agrár hírgyűjtő és gazdálkodói információs portál.

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
- a production oldal automatikusan a GitHub main ágából deployolódik.

### GitHub

Felhasználó:

- vasotto

Repository:

- gazdacentrum

Production branch:

- main

A Cloudflare Pages minden main ágra kerülő commit után automatikusan új deployt indít.

## 3. Jelenlegi működési folyamat

```text
RSS-forrás
→ fetch_news.py
→ news.json
→ index.html
→ Cloudflare Pages
→ gazdacentrum.hu
