---
title: Modularni inverz
---

U ovom se članku uvodi inverz s obzirom na množenje u modularnoj aritmetici i razmatraju se uobičajene metode njegova računanja.

## Osnovni pojmovi

Multiplikativni inverz realnog broja $a\in\mathbf R$ različitog od nule jest njegova recipročna vrijednost $a^{-1}$. Slično, u teoriji brojeva može se definirati inverz cijelog broja $a$ modulo $m$, $a^{-1}\bmod m$, ili kraće $a^{-1}$. To je **modularni inverz** (modular multiplicative inverse), koji se naziva i **teorijsko-brojevna recipročna vrijednost**.

???+ abstract "Inverz"
    Za cijeli broj $a$ i pozitivni cijeli broj $m$, ako postoji $b$ takav da je $ab\equiv 1\pmod m$, kažemo da je $b$ **inverz** (inverse) od $a$ modulo $m$.

To znači da je $b$ rješenje linearne kongruencije $ax\equiv 1\pmod m$. Prema svojstvima [linearnih kongruencija](./linear-equation.md), inverz $a^{-1}\bmod m$ postoji ako i samo ako je $\gcd(a,m)=1$, tj. ako su $a,m$ relativno prosti, i tada je jedinstven modulo $m$.

## Računanje jednog inverza

Pomoću proširenog Euklidova algoritma ili brzog potenciranja inverz jednog cijelog broja može se izračunati u vremenu $O(\log m)$.

### Prošireni Euklidov algoritam

Računanje inverza ekvivalentno je rješavanju linearne kongruencije. Stoga se inverz može izračunati [proširenim Euklidovim algoritmom](./gcd.md#扩展欧几里得算法) u vremenu $O(\log\min\{a,m\})$. Ujedno, budući da je linearna jednadžba koja odgovara inverzu posebno jednostavna, odgovarajući se koraci mogu prikladno pojednostavniti.

???+ example "Referentna implementacija"
    === "C++"
        ```cpp
        --8<-- "docs/math/code/inverse/inverse-1.cpp:core"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/math/code/inverse/inverse-1.py:core"
        ```

Ovaj je algoritam primjenjiv u svim slučajevima u kojima inverz postoji.

### Metoda brzog potenciranja

Ova se metoda uglavnom primjenjuje kad je modul prost broj $p$. Tada prema [malom Fermatovu teoremu](./fermat.md#mali-fermatov-teorem) za svaki $a\perp p$ vrijedi

$$
a\cdot a^{p-2} = a^{p-1} \equiv 1 \pmod p.
$$

Prema jedinstvenosti inverza, inverz $a^{-1}\bmod p$ jednak je $a^{p-2}\bmod p$, pa se može izravno izračunati [brzim potenciranjem](../binary-exponentiation.md) u vremenu $O(\log p)$:

???+ example "Referentna implementacija"
    === "C++"
        ```cpp
        --8<-- "docs/math/code/inverse/inverse-2.cpp:core"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/math/code/inverse/inverse-2.py:core"
        ```

Dakako, teoretski se ova metoda pomoću [Eulerova teorema](./fermat.md#eulerov-teorem) može poopćiti na slučaj općeg modula $m$, tj. inverz se može računati kao $a^{\varphi(m)-1}\bmod m$. Međutim, jednokratno računanje [Eulerove funkcije](./euler-totient.md) $\varphi(m)$ nije jednostavno, pa taj algoritam u općem slučaju nije učinkovit.

## Računanje više inverza

U nekim je situacijama potrebno brzo izračunati inverze više cijelih brojeva $a_1,a_2,\cdots,a_n$ modulo $m$. Računanje inverza jednog po jednog ukupno zahtijeva vrijeme $O(n\log m)$. Zapravo, ako ih obradimo zajedno, inverzi svih brojeva mogu se izračunati u vremenu $O(n+\log m)$.

Promotrimo prefiksne produkte niza $\{a_i\}$:

$$
S_0 = 1,~ S_i = a_iS_{i-1},~ i=1,2,\cdots,n.
$$

Ako je svaki $a_i$ relativno prost s $m$, i njihov je produkt $S_n$ relativno prost s $m$. Stoga se prethodno opisanim algoritmom može izračunati vrijednost $S_n^{-1}\bmod m$. Budući da je inverz produkta jednak produktu inverza, polazeći od $S_n^{-1}$ i prolazeći niz unatrag možemo izračunati inverz svakog $S_i$:

$$
S_{i-1}^{-1} = a_iS_i^{-1} \bmod m,~ i = n,n-1,\cdots,1.
$$

Iz toga se inverz pojedinog $a_i$ može izračunati formulom:

$$
a_i^{-1} = S_{i-1}S_i^{-1} \bmod m,~ i = 1,2,\cdots,n.
$$

Referentna implementacija slijedi:

???+ example "Referentna implementacija"
    === "C++"
        ```cpp
        --8<-- "docs/math/code/inverse/inverse-3.cpp:core"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/math/code/inverse/inverse-3.py:core"
        ```

U algoritmu se inverz pojedinog elementa računa samo jednom, pa je ukupna vremenska složenost $O(n+\log m)$.

## Predračunavanje inverza u linearnom vremenu

Ako treba predračunati inverze prvih $n$ pozitivnih cijelih brojeva modulo prost broj $p$, to se može učiniti i u vremenu $O(n)$ pomoću rekurzivne relacije koju razmatramo u ovom odjeljku. Ta se metoda često koristi pri računanju binomnih koeficijenata za predračunavanje inverza faktorijela prvih $n$ pozitivnih cijelih brojeva.

Za pozitivni cijeli broj $i$ takav da je $1< i < p$ promotrimo dijeljenje s ostatkom:

$$
p = \left\lfloor \dfrac{p}{i} \right\rfloor i + (p\bmod i).
$$

Uzimajući tu jednakost modulo prost broj $p$, dobivamo

$$
0 \equiv \left\lfloor \dfrac{p}{i} \right\rfloor i + (p\bmod i) \pmod p.
$$

Množenjem obiju strana s $i^{-1}(p\bmod i)^{-1}$ dobivamo

$$
i^{-1} \equiv - \left\lfloor \dfrac{p}{i} \right\rfloor (p\bmod i)^{-1} \pmod p.
$$

To je formula za rekurzivno računanje inverza u linearnom vremenu. Budući da je $p\bmod i < i$, ta formula svodi problem računanja $i^{-1}\bmod p$ na manji problem $(p\bmod i)^{-1}\bmod p$. Stoga, polazeći od $1^{-1}\bmod p=1$ i redom primjenjujući formulu za svaki $i$, inverzi prvih $n$ cijelih brojeva mogu se dobiti u vremenu $O(n)$.

Referentna implementacija slijedi:

???+ example "Referentna implementacija"
    === "C++"
        ```cpp
        --8<-- "docs/math/code/inverse/inverse-4.cpp:core"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/math/code/inverse/inverse-4.py:core"
        ```

Ovaj je algoritam primjenjiv samo kad je modul prost broj. Kad modul $m$ nije prost, ne može se jamčiti da je $m\bmod i$ iz rekurzivne formule i dalje relativno prost s $m$, pa $(m\bmod i)^{-1}$ koji rekurzija zahtijeva možda ne postoji. Jedan je takav primjer $m=8,i=3$. Tada je $m\bmod i = 2$, koji nema inverz modulo $m$.

Osim toga, nakon što imamo tu rekurzivnu formulu, prirodna je ideja izravno rekurzivno računati inverz proizvoljnog broja $a$. U svakom koraku rekurzije formula ga svodi na inverz manjeg ostatka $p\bmod a$, dok ostatak ne postane $1$. Složenost takvog postupka zasad nije poznata[^linear-recursion], pa se preporučuje koristiti prethodno opisane uobičajene metode.

## Zadaci za vježbu

-   [LOJ 110 乘法逆元 (Multiplikativni inverz)](https://loj.ac/problem/110)
-   [LOJ 161 乘法逆元 2 (Multiplikativni inverz 2)](https://loj.ac/problem/161)
-   [LOJ 2605「NOIP2012」同余方程 (Kongruencija)](https://loj.ac/problem/2605)
-   [Luogu P2054「AHOI2005」洗牌 (Miješanje karata)](https://www.luogu.com.cn/problem/P2054)
-   [LOJ 2034「SDOI2016」排列计数 (Prebrojavanje permutacija)](https://loj.ac/problem/2034)

## Literatura i bilješke

-   [Modular multiplicative inverse - Wikipedia](https://en.wikipedia.org/wiki/Modular_multiplicative_inverse)

[^linear-recursion]: U [riteme-ovu odgovoru na Zhihuu](https://www.zhihu.com/question/59033693/answer/323292359) navodi se da je teorijski poznata gornja ograda složenosti takvog postupka $O(p^{1/3+\varepsilon})$, dok je ponašanje na stvarnim slučajnim podatcima blizu $O(\log p)$.
