---
title: Radix sort
---

???+ warning "Napomena"
    Ova stranica ne govori o [**counting sortu**](./counting-sort.md).

Ova stranica kratko predstavlja radix sort.

## Definicija

**Radix sort** neusporedbeni je algoritam sortiranja, izvorno osmišljen za sortiranje bušenih kartica. Elemente koje treba sortirati rastavlja na $k$ ključeva i sortiranjem po svakom ključu redom sortira sve elemente.

Ako se uspoređuje redom od $1.$ do $k.$ ključa, radix sort zove se MSD (Most Significant Digit first) radix sort;

ako se uspoređuje redom od $k.$ do $1.$ ključa, zove se LSD (Least Significant Digit first) radix sort.

## Usporedba elemenata s k ključeva

Neka $a_i$ označava $i$-ti ključ elementa $a$.

Ako elementi imaju $k$ ključeva, za dva elementa $a$ i $b$ zadani način usporedbe je:

-   usporedi $1.$ ključeve $a_1$ i $b_1$: ako je $a_1 < b_1$, onda je $a < b$; ako je $a_1 > b_1$, onda je $a > b$; ako je $a_1 = b_1$, idi na sljedeći korak;
-   usporedi $2.$ ključeve $a_2$ i $b_2$: ako je $a_2 < b_2$, onda je $a < b$; ako je $a_2 > b_2$, onda je $a > b$; ako je $a_2 = b_2$, idi na sljedeći korak;
-   …
-   usporedi $k.$ ključeve $a_k$ i $b_k$: ako je $a_k < b_k$, onda je $a < b$; ako je $a_k > b_k$, onda je $a > b$; ako je $a_k = b_k$, onda je $a = b$.

Primjeri:

-   pri usporedbi prirodnih brojeva, ako brojeve poravnamo po jedinicama i sprijeda nadopunimo nulama, $i$-ta znamenka slijeva može biti $i$-ti ključ;
-   pri leksikografskoj usporedbi stringova $i$-ti znak slijeva može biti $i$-ti ključ;
-   zadani način usporedbe `std::pair` i `std::tuple` u C++-u isti je kao gore opisani.

## MSD radix sort

Na temelju usporedbe elemenata s $k$ ključeva nameće se ideja: najprije usporedimo $1.$ ključeve svih elemenata i tako odredimo grubi odnos među elementima; zatim za **elemente s jednakim $1.$ ključem** usporedimo $2.$ ključeve… i tako dalje.

Budući da se uspoređuje redom od $1.$ do $k.$ ključa, algoritam izveden iz te ideje zove se MSD (Most Significant Digit first) radix sort.

### Tijek algoritma

Elemente rastavimo na $k$ ključeva; najprije stabilno sortiramo po $1.$ ključu, zatim svaku grupu **elemenata s jednakim ključem** stabilno sortiramo po $2.$ ključu (rekurzivno)… i na kraju svaku grupu **elemenata s jednakim ključem** stabilno sortiramo po $k.$ ključu.

Radix sort obično smatramo stabilnim, pa i u MSD radix sortu za unutarnje sortiranje po ključu koristimo samo **stabilan algoritam** (obično counting sort).

Ispravnost slijedi iz gore opisane usporedbe elemenata s $k$ ključeva.

### Primjer koda

#### Sortiranje prirodnih brojeva

Slijedi rekurzivni MSD radix sort koji obrađuje najviše `MAXN` cijelih brojeva iz $[0,2^{32}-1]$. Početno je `digit=10`; pri promjeni baze treba uskladiti `RADIX` i `powRADIX`.

??? example "Primjer koda"
    ```cpp
    --8<-- "docs/basic/code/radix-sort/radix-sort_1.cpp:core"
    ```

#### Sortiranje stringova

Slijedi rekurzivni MSD radix sort koji leksikografski sortira `std::string` sastavljene samo od malih slova engleske abecede:

??? example "Primjer koda"
    ```cpp
    --8<-- "docs/basic/code/radix-sort/radix-sort_2.cpp:core"
    ```

Budući da usporedba dvaju stringova lako dosegne linearnu složenost $O(n)$, pri sortiranju stringova MSD radix sort je i po složenosti i po stvarnom vremenu bolji od većine usporedbenih algoritama sortiranja.

### Veza s bucket sortom

Preduvjet: [Bucket sort](./bucket-sort.md)

Bucket sort treba neki drugi algoritam za sortiranje elemenata unutar svake košare. Zapravo možemo na svaku košaru ponovno primijeniti bucket sort, dok u nekom koraku košare nemaju $\le 1$ element.

Zato se MSD radix sort može shvatiti i kao: bucket sort implementiran bucket sortom.

Iz toga slijedi i optimizacija konstante MSD radix sorta: ako u nekom koraku košara ima $\le B$ elemenata ($B$ je konstanta po izboru), izravno izvedemo insertion sort i vratimo se, čime smanjujemo broj rekurzivnih poziva.

## LSD radix sort

MSD radix sort uspoređuje redom od $1.$ do $k.$ ključa, pa zahtijeva rekurziju ili iteraciju; konstanta je razmjerno velika, a za prirodne brojeve je pomalo nezgodan.

Obrnemo li rekurzivni postupak – uspoređujemo redom od $k.$ do $1.$ ključa – dobivamo LSD (Least Significant Digit first) radix sort, algoritam koji radi bez rekurzije.

### Tijek algoritma

Elemente rastavimo na $k$ ključeva; zatim **sve elemente** stabilno sortiramo po $k.$ ključu, pa **sve elemente** po $(k-1).$ ključu, pa **sve elemente** po $(k-2).$ ključu… i na kraju **sve elemente** po $1.$ ključu. Time je cijeli niz stabilno sortiran.

![primjer cijelog tijeka LSD radix sorta](images/radix-sort-1.svg)

I LSD radix sort za unutarnje sortiranje po ključu treba **stabilan algoritam**; obično se također koristi counting sort.

Za ispravnost LSD radix sorta vidi [rješenje zadatka 8.3-3 iz *Introduction to Algorithms* (3. izd.)](https://walkccc.github.io/CLRS/Chap08/8.3/#83-3) ili objašnjenje u nastavku:

### Ispravnost

Prisjetimo se usporedbe elemenata s $k$ ključeva:

-   da bismo samo iz $a_1$ i $b_1$ odredili odnos elemenata $a$ i $b$, trebamo unaprijed znati zaključak usporedbe $a_2$ i $b_2$ za slučaj $a_1 = b_1$;
-   da bismo samo iz $a_2$ i $b_2$ odredili odnos $a$ i $b$, trebamo unaprijed znati zaključak usporedbe $a_3$ i $b_3$ za slučaj $a_2 = b_2$;
-   …
-   da bismo samo iz $a_{k-1}$ i $b_{k-1}$ odredili odnos $a$ i $b$, trebamo unaprijed znati zaključak usporedbe $a_k$ i $b_k$ za slučaj $a_{k-1} = b_{k-1}$;
-   $a_k$ i $b_k$ mogu se usporediti izravno.

Sad obrnimo redoslijed:

-   $a_k$ i $b_k$ mogu se usporediti izravno;
-   znajući zaključak usporedbe $a_k$ i $b_k$, dobivamo zaključak usporedbe $a_{k-1}$ i $b_{k-1}$;
-   …
-   znajući zaključak usporedbe $a_2$ i $b_2$, dobivamo zaključak usporedbe $a_1$ i $b_1$;
-   znajući zaključak usporedbe $a_1$ i $b_1$, konačno dobivamo zaključak usporedbe $a$ i $b$.

Ako u tom postupku pri svakoj usporedbi ključa odmah preslagujemo elemente, dobivamo LSD radix sort.

### Pseudokod

$$
\begin{array}{ll}
1 & \textbf{Input. } \text{An array } A \text{ consisting of }n\text{ elements, where each element has }k\text{ keys.}\\
2 & \textbf{Output. } \text{Array }A\text{ will be sorted in nondecreasing order stably.} \\
3 & \textbf{Method. }  \\
4 & \textbf{for }i\gets k\textbf{ down to }1\\
5 & \qquad\text{sort }A\text{ into nondecreasing order by the }i\text{-th key stably}
\end{array}
$$

### Primjer koda

Slijedi sortiranje elemenata s $k$ ključeva LSD radix sortom.

??? example "Primjer koda"
    ```cpp
    --8<-- "docs/basic/code/radix-sort/radix-sort_lsd.cpp:core"
    ```

Zapravo stabilnost ne zahtijeva nužno prolaz odostraga; dovoljno je nad nizom `cnt` izvesti operaciju ekvivalentnu `std::exclusive_scan`.

???+ note "Primjer [Luogu P1177【模板】排序](https://www.luogu.com.cn/problem/P1177)"
    Zadano je $n$ prirodnih brojeva; ispiši ih od najmanjeg do najvećeg.
    
    ```cpp
    --8<-- "docs/basic/code/radix-sort/radix-sort_3.cpp"
    ```

## Svojstva

### Stabilnost

Ako je unutarnje sortiranje po ključu stabilno, i MSD i LSD radix sort stabilni su algoritmi sortiranja.

### Vremenska složenost

Radix sort je obično brži od usporedbenih algoritama sortiranja (npr. quick sorta). No treba dodatnu memoriju, pa kad je memorije malo, algoritam koji sortira u mjestu (npr. quick sort) može biti bolji izbor.[^ref1]

Sljedeće granice pretpostavljaju da izdvajanje jednog ključa i premještanje jednog elementa (ili njegova indeksa) stoje $O(1)$. Ako su rasponi vrijednosti ključeva mali, kao unutarnje sortiranje može se koristiti [counting sort](./counting-sort.md), pa su složenosti LSD-a i MSD-a redom

$$
O\left(kn+\sum_{i=1}^k w_i\right),\qquad O\left(kn+\sum_{i=1}^k b_iw_i\right),
$$

gdje je $b_i$ broj košara u kojima se na $i$-toj razini stvarno izvodi counting sort, a $w_i$ veličina raspona $i$-tog ključa. Ako je raspon ključeva velik, može se izravno koristiti usporedbeno sortiranje u $O(nk\log n)$ bez radix sorta.

### Prostorna složenost

Promatramo pomoćni prostor osim ulaza, uz pretpostavku da element ili njegov indeks zauzima $O(1)$. Uz counting sort LSD može ponovno koristiti privremeni niz duljine $n$ i niz brojača, pa je pomoćni prostor $O(n+\max_i w_i)$. Rekurzivni MSD koji ponovno koristi privremeni niz, ali na svakoj razini rekurzije čuva granice košara, troši $O(n+\sum_{i=1}^k w_i)$. Ako su rasponi svih znamenki fiksni, to se svodi na $O(n)$ odnosno $O(n+k)$, gdje je $k$ broj ključeva.

## Literatura i bilješke

[^ref1]: Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein.*Introduction to Algorithms*(3rd ed.). MIT Press and McGraw-Hill, 2009. ISBN 978-0-262-03384-8. "8.3 Radix sort", pp. 199.
