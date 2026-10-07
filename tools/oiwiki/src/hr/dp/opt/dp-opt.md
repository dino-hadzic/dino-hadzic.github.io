---
title: Uvod u optimizacije DP-a
---

## Uvod

Ova stranica nabraja neke uobičajene metode optimizacije dinamičkog programiranja (dynamic programming, DP). Pod optimizacijom DP-a podrazumijeva se sljedeće: za mnoge zadatke dinamičkog programiranja lako je napisati naivnu jednadžbu prijelaza stanja, ali je izravno računanje često neučinkovito, pa je potrebno posegnuti za tehnikama kojima se smanjuje vremenska složenost.

Te su metode međusobno usko povezane, često sadrže slične ideje i nerijetko ih treba kombinirati. Zato ovaj tekst daje samo grubu podjelu i usredotočuje se na najosnovnije ideje.

## Optimizacija uobičajenim tehnikama

Prijelazi u mnogim zadacima dinamičkog programiranja mogu se ubrzati uobičajenim algoritmima i strukturama podataka.

Takve se tehnike javljaju u dvije tipične situacije. U prvoj DP zadatak ima jednadžbu prijelaza stanja oblika

$$
f(i) = F(a_i,\{f(j) : j < i\}).
$$

Ovdje izračun trenutnog stanja $f(i)$ ovisi o trenutnom ulazu $a_i$ i o stanjima cijelog prethodnog niza $\{f(j):j < i\}$. Stoga možemo održavati strukturu podataka i svaki izračun $f(i)$ promatrati kao upit; nakon što dobijemo trenutno stanje $f(i)$, izvedemo još jednu operaciju izmjene kojom tu strukturu ažuriramo za kasnije prijelaze.

U drugoj situaciji DP zadatak ima jednadžbu prijelaza stanja oblika

$$
f(i,\cdot) = F(a_i,f(i-1,\cdot)).
$$

Ovdje je svaki $f(i,\cdot)$ polje ili neki drugi složeniji objekt. Dakle, iako $f(i,\cdot)$ ovisi samo o jednom prethodnom stanju, složenost jednog prijelaza je velika, pa ga treba optimizirati strukturama podataka i sličnim tehnikama.

### Optimizacija DP-a prefiksnim sumama

Povezana stranica: [prefiksne sume](../../basic/prefix-sum.md#prefiksne-sume)

Ako izračun trenutnog stanja ovisi o zbroju nekog podsegmenta prethodnih stanja, izračun se može ubrzati održavanjem prefiksnih suma. Jedna klasa zadataka s višedimenzionalnim prefiksnim sumama naziva se i [SOS DP](../../basic/prefix-sum.md#poseban-slučaj-dp-po-podskupovima-sos).

Zadaci:

-   [Luogu P2513 \[HAOI2009\] Niz s danim brojem inverzija](https://www.luogu.com.cn/problem/P2513)
-   [AtCoder Educational DP Contest M - Candies](https://atcoder.jp/contests/dp/tasks/dp_m)

### Optimizacija DP-a monotonim redom/monotonim stogom

Glavna stranica: [optimizacija monotonim redom/monotonim stogom](./monotonic-queue-stack.md)

Ako trenutno stanje ovisi o intervalnom minimumu/maksimumu ili sličnoj informaciji o prethodnim stanjima, izračun se može ubrzati održavanjem monotonog reda ili monotonog stoga.

### Optimizacija DP-a segment treejem/Fenwick treejem

Povezane stranice: [segment tree](../../ds/seg.md), [Fenwick tree](../../ds/fenwick.md)

Ako se pri svakom prijelazu stanja postavlja upit o zbroju, minimumu/maksimumu ili sličnoj informaciji na nekom intervalu, ili ako jedna operacija izmjene ažurira cijeli interval, izračun se može ubrzati održavanjem segment treeja ili Fenwick treeja.

Zadaci:

-   [AtCoder Educational DP Contest Q - Flowers](https://atcoder.jp/contests/dp/tasks/dp_q)
-   [AtCoder Educational DP Contest W - Intervals](https://atcoder.jp/contests/dp/tasks/dp_w)
-   [Codeforces 115 E. Linear Kingdom Races](https://codeforces.com/problemset/problem/115/E)

### Optimizacija DP-a CDQ podjelom

Glavna stranica: [optimizacija DP-a CDQ podjelom](../../misc/cdq-divide.md#cdq-分治优化-1d1d-动态规划的转移)

Slično kao gore, cijeli DP postupak promatramo kao niz upita i izmjena. U nekim je zadacima redoslijedno računanje presporo, pa se cijeli niz upita i izmjena može obraditi offline i ubrzati CDQ podjelom (CDQ divide and conquer).

Optimizacija DP-a CDQ podjelom česta je i u sljedećim vrstama zadataka:

-   [optimizacija nagibom temeljena na CDQ podjeli](./slope.md#optimizacija-dp-a-binarnim-pretraživanjemcdq-ombalansiranim-stablom)
-   [optimizacija DP-a s monotonošću odluka podjelom](./quadrangle.md#podijeli-pa-vladaj)

### Optimizacija DP-a binary liftingom

Povezana stranica: [binary lifting](../../basic/binary-lifting.md)

U nekim zadacima stanje $f(i)$ definiramo kao rezultat $2^i$ prijelaza iz početnog stanja. Takva preformulacija zadatka koristi ideju binary liftinga (udvostručavanja), pa se često naziva optimizacija DP-a binary liftingom.

Ponekad se i DP zadaci s jednadžbom prijelaza stanja oblika

$$
f(i,j) = f(i-1,f(i-1,j))
$$

nazivaju DP s binary liftingom (optimizacija binary liftingom).

Zadaci:

-   [Luogu P1081 \[NOIP 2012 viša razina\] Putovanje automobilom](https://www.luogu.com.cn/problem/P1081)
-   [Luogu P1613 Bijeg](https://www.luogu.com.cn/problem/P1613)
-   [Luogu P4739 \[CERC2017\] Donut Drone](https://www.luogu.com.cn/problem/P4739)

## Optimizacija pomoću strukture zadatka

Mnogi zadaci dinamičkog programiranja imaju strukturna svojstva poput konveksnosti ili monotonosti, a njihovim se razumnim iskorištavanjem zadatak može brzo riješiti.

### Optimizacija DP-a nagibom

Glavna stranica: [optimizacija nagibom](./slope.md)

Slično metodama iz prethodnog odjeljka, iskorištavanjem konveksnosti zadatka pojedini se prijelaz može ubrzati održavanjem konveksne ljuske.

### Optimizacija DP-a nejednakošću četverokuta

Glavna stranica: [optimizacija nejednakošću četverokuta](./quadrangle.md)

DP zadaci u kojima funkcije zadovoljavaju nejednakost četverokuta često imaju neku vrstu monotonosti odluka. Iskorištavanjem tog svojstva postoji mnogo specijaliziranih metoda za smanjenje složenosti izračuna. Uobičajene vrste zadataka su jednodimenzionalni zadaci s monotonošću odluka, zadaci rastavljanja intervala, zadaci spajanja intervala itd.

### Optimizacija DP-a Slope Trickom

Glavna stranica: [Slope Trick](./slope-trick.md)

U nekim je zadacima tijekom prijelaza stanja lakše održavati diferenciju (tj. nagib) funkcije stanja nego samu funkciju. I ova optimizacija obično zahtijeva konveksnost zadatka.

### WQS binarno pretraživanje/konveksna optimizacija DP-a

Glavna stranica: [WQS binarno pretraživanje](./wqs-binary-search.md)

Za optimizacijske DP zadatke s ograničenjem na broj odabranih elemenata, ako je zadatak bez tog ograničenja lakše rješiv, a optimalna je vrijednost konveksna funkcija tog ograničenja, izračun se može pojednostavniti WQS binarnim pretraživanjem.

## Optimizacija matematičkim metodama

Prijelazi u mnogim zadacima dinamičkog programiranja mogu se ubrzati matematičkim alatima.

### Optimizacija DP-a brzim potenciranjem matrica

Povezana stranica: [brzo potenciranje](../../math/binary-exponentiation.md)

Ako se jednadžba prijelaza stanja DP zadatka može zapisati u autonomnom obliku

$$
f(i) = F(f(i-1)),
$$

odnosno ako trenutno stanje $f(i)$ ovisi samo o prethodnom stanju $f(i-1)$, a ne i o drugim ulazima, tada se brzim potenciranjem izravno ubrzava izračun

$$
f(n) = F^n(f(0))
$$

kojim dobivamo konačni odgovor. Budući da se jedna operacija $F$ često može zapisati kao matrica, ova se metoda obično naziva optimizacija DP-a brzim potenciranjem matrica. Zapravo se njome može ubrzati bilo koja transformacija koja zadovoljava asocijativnost (tj. bilo koji element [monoida](../../math/algebra/basic.md#群)).

Zadaci:

-   [Luogu P1397 \[NOI2013\] Igra s matricom](https://www.luogu.com.cn/problem/P1397)
-   [Luogu P3176 \[HAOI2015\] Rastavljanje znamenkastog niza](https://www.luogu.com.cn/problem/P3176)
-   [Codeforces 576 D. Flights for Regular Customers](https://codeforces.com/problemset/problem/576/D)
-   [Luogu P6772 \[NOI2020\] Gurman](https://www.luogu.com.cn/problem/P6772)

### Optimizacija DP-a FFT-om

Povezana stranica: [FFT](../../math/poly/fft.md)

Ako jednadžba prijelaza stanja DP zadatka ima oblik konvolucije, prijelaz se može ubrzati FFT-om. Naravno, ovisno o konkretnom zadatku, mogu se upotrijebiti i druge polinomne tehnike.

Zadaci:

-   [Codeforces 553 E. Kyoya and Train](https://codeforces.com/contest/553/problem/E)
-   [Codeforces 1784 D. Wooden Spoon](https://codeforces.com/problemset/problem/1784/D)

### Optimizacija DP-a Lagrangeovom interpolacijom

Povezana stranica: [Lagrangeova interpolacija](../../math/numerical/interp.md#lagrange-插值法)

U nekim je DP zadacima funkcija stanja $f(i,j)$ polinom stupnja $k$ u varijabli $j$. Tada možemo grubom silom izračunati njezine vrijednosti u $k+1$ točaka, Lagrangeovom interpolacijom dobiti izraz za $f(i,\cdot)$ i time optimizirati prijelaz ili čak izravno dobiti odgovor.

Zadaci:

-   [Luogu P5223 Function](https://www.luogu.com.cn/problem/P5223)
-   [Luogu P4463 \[kineske IOI pripreme 2012\] calc](https://www.luogu.com.cn/problem/P4463)
-   [Luogu P5469 \[NOI2019\] Robot](https://www.luogu.com.cn/problem/P5469)

## Optimizacija pojednostavnjivanjem stanja

Osim optimizacije prijelaza, složenost izračuna može se smanjiti i pojednostavnjivanjem stanja.

### DP nad DP-om i minimizacija DFA

Glavne stranice: [DP nad DP-om](../dp-of-dp.md), [minimizacija DFA](../../misc/fsm.md#dfa-最小化)

U nekim se DP zadacima funkcija stanja može zapisati u obliku $f(i,x)$, ali je prijelaz samog $x$ složen, pa čak može ovisiti o drugom DP zadatku. Za takve zadatke možemo najprije za prijelaze stanja $x$ izgraditi automat, minimizacijom DFA smanjiti broj stanja, a zatim provesti vanjski DP.

### Optimizacija DP-a dizajnom stanja

Glavna stranica: [optimizacija dizajnom stanja](./state.md)

Neki se posebni zadaci mogu riješiti uz znatno manji broj stanja pomoću domišljato osmišljenih stanja.

## Dodatna literatura

-   [Zbirka metoda optimizacije DP-a (DP 优化方法大杂烩) by Alex Wei](https://www.cnblogs.com/alex-wei/p/DP_Involution.html)
