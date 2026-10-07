---
title: Hash stabla
---

Kad provjeravamo jesu li neka stabla izomorfna, često ih pretvaramo u hash vrijednosti i te vrijednosti pohranjujemo, čime smanjujemo složenost.

Hashiranje stabala vrlo je fleksibilno i može se osmisliti mnogo načina hashiranja; no ako ga osmislimo nasumce, lako može biti pogrešno i probijeno (hackano). U nastavku opisujemo vrstu metoda koje je lako implementirati i teško probiti.

## Metoda

Ovim metodama potrebna je hash funkcija za multiskupove. Hash vrijednost podstabla s korijenom u nekom vrhu jednaka je hash vrijednosti multiskupa hash vrijednosti podstabala s korijenima u svoj njegovoj djeci, tj.:

$$
h_x = f(\{ h_i \mid i \in son(x) \})
$$

gdje je $h_x$ hash vrijednost podstabla s korijenom $x$, a $f$ hash funkcija multiskupa.

Uzmimo za primjer hash funkciju iz koda:

$$
f(S) = \left( c + \sum_{x \in S} g(x) \right) \bmod m
$$

gdje je $c$ konstanta, obično je dovoljno $1$. $m$ je modul; obično se koristi $2^{32}$ ili $2^{64}$ s prirodnim prelijevanjem (overflow), a može i veliki prosti broj. $g$ je preslikavanje cijelih brojeva u cijele brojeve; u kodu se koristi xor shift, ali može se odabrati i neka druga funkcija, no ne preporučujemo polinome. Da se zaštitimo od autora zadatka koji ciljano probija xor hash, prije i poslije preslikavanja možemo napraviti XOR s nasumičnom konstantom.

Ovaj je hash vrlo jednostavno napisati. Ako treba mijenjati korijen (rerooting), u drugom DP-u dovoljno je oduzeti hash podstabla.

## Primjeri

### [UOJ #763. 树哈希](https://uoj.ac/problem/763)

Ovo je zadatak-predložak. Bez puno riječi: pokrenemo jedan DFS s korijenom $1$ i gotovo.

??? note "Referentni kod"
    ```cpp
    --8<-- "docs/graph/code/tree-hash/tree-hash_1.cpp"
    ```

### [\[BJOI2015\] 树的同构](https://www.luogu.com.cn/problem/P5043)

Izomorfizam u ovom zadatku odnosi se na nekorijenska stabla, a gore opisana metoda vrijedi za korijenska stabla. Zato dva izomorfna nekorijenska stabla imaju jednake hash vrijednosti samo kad su im korijeni jednaki. Budući da su ograničenja mala, možemo brute-force izračunati hash vrijednost za svaki vrh kao korijen, sortirati ih i usporediti.

Ako su ograničenja veća, možemo upotrijebiti DP s promjenom korijena: dvaput obiđemo stablo i dobijemo hash vrijednost za svaki vrh kao korijen. Možemo iskoristiti i gornju hash funkciju multiskupa: hash vrijednosti za sve vrhove kao korijene stavimo u multiskup, izračunamo hash tog multiskupa i uspoređujemo (pristup 1).

Složenost se može dodatno poboljšati traženjem centroida. Stablo ima najviše dva centroida, pa je dovoljno izračunati hash vrijednosti s njima kao korijenima. Zatim ili te vrijednosti uspoređujemo zasebno (pristup 2), ili, ako je centroid jedan, njegov hash uzmemo kao hash cijelog stabla, a ako su dva, uzmemo manji (ili veći) od njihovih.

??? note "Pristup 1"
    ```cpp
    --8<-- "docs/graph/code/tree-hash/tree-hash_2.cpp"
    ```

??? note "Pristup 2"
    ```cpp
    --8<-- "docs/graph/code/tree-hash/tree-hash_3.cpp"
    ```

### [HDU 6647 Bracket Sequences on Tree](https://acm.hdu.edu.cn/showproblem.php?pid=6647)

Zadatak traži broj bitno različitih zagradnih nizova koji nastaju obilaskom nekorijenskog stabla.

Prvo uočimo da dva neizomorfna korijenska stabla nikad ne daju isti zagradni niz. Razmotrimo najprije broj bitno različitih zagradnih nizova koje daje obilazak korijenskog stabla. Neka je $u$ korijen podstabla koje trenutno promatramo i neka $f(u)$ označava broj načina za to podstablo. Iz $u$ obilazimo prema dolje, redoslijed biramo proizvoljno, što daje $|son(u)|!$ permutacija; za svako dijete $v$ podstablo vrha $v$ ima $f(v)$ načina, pa je $f(u)=|son(u)|! \cdot \prod_{v \in son(u)} f(v)$. No izomorfna podstabla stvaraju ponavljanja, pa $f(u)$ treba podijeliti umnoškom faktorijela broja pojavljivanja svake bitno različite vrste podstabla, slično permutacijama multiskupa.

Gornjim DP-om dobivamo broj načina za korijen. Zatim DP-om s promjenom korijena prenosimo hash vrijednost i podatke o broju načina s roditelja na dijete, čime dobivamo hash vrijednost i broj načina za svaki vrh kao korijen. Svaku različitu vrstu podstabla brojimo samo jednom.

??? note "Referentni kod"
    ```cpp
    --8<-- "docs/graph/code/tree-hash/tree-hash_4.cpp"
    ```

## Literatura

Metoda hashiranja u ovom članku preuzeta je i proširena iz bloga [一种好写且卡不掉的树哈希](https://peehs-moorhsum.blog.uoj.ac/blog/7891) („Hash stabla koji je lako napisati i ne može se probiti”).
