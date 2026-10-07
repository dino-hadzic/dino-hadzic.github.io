---
title: Heurističko pretraživanje
---

Ova stranica kratko predstavlja heurističko pretraživanje i njegovu primjenu.

## Definicija

Heurističko pretraživanje (heuristic search) je pretraživanje koje običnom algoritmu pretraživanja dodaje heurističku funkciju.

Uloga je heurističke funkcije da na temelju već poznatih informacija procijeni svaki izbor grane u pretrazi i prema tome odabere granu. Jednostavno rečeno, heurističko pretraživanje analizira i „uzeti” i „ne uzeti”, pa iz toga bira bolje rješenje ili odbacuje beskorisna.

## Riješeni primjer

Budući da je pojam prilično apstraktan, objasnit ćemo ga na primjeru.

???+ note "[„NOIP2005 Popularizacijska razina” Branje ljekovitog bilja](https://www.luogu.com.cn/problem/P1048)"
    Sažetak zadatka: zadano je $N$ vrsta predmeta i ruksak kapaciteta $W$. Svaka vrsta predmeta ima težinu $w_i$ i vrijednost $v_i$. Treba odabrati nekoliko predmeta (svaka vrsta najviše jednom) i staviti ih u ruksak tako da ukupna vrijednost predmeta u ruksaku bude najveća, a ukupna težina ne premaši kapacitet ruksaka.

??? note "Ideja rješenja"
    Napišemo funkciju procjene $f$ koja može odrezati sve beskorisne grane „$0$” (tj. odrezati veliku količinu beskorisnih grana „ne uzmi”).
    
    Funkcija procjene $f$ radi ovako:
    
    Kad predmet uzimamo, provjerimo je li premašen zadani kapacitet (rezanje po izvedivosti); kad ga ne uzimamo, provjerimo je li ukupna vrijednost svih preostalih biljaka + dosadašnja vrijednost veća od najboljeg do sada pronađenog rješenja (rezanje po optimalnosti).

??? note "Primjer rješenja"
    ```cpp
    --8<-- "docs/search/code/heuristic/heuristic_1.cpp"
    ```
