---
title: Ideja dekompozicije na blokove
---

## Uvod

Dekompozicija na blokove (sqrt decomposition, „blokiranje”) zapravo je ideja, a ne struktura podataka.

Od NOIP-a preko NOI-ja do IOI-ja, ideja dekompozicije na blokove pojavljuje se na svim razinama težine.

Osnovna je ideja prikladno podijeliti izvorne podatke i na svakom dobivenom bloku unaprijed izračunati dio informacija, čime se postiže bolja vremenska složenost nego kod običnog brute-force algoritma.

Vremenska složenost dekompozicije ovisi ponajprije o duljini bloka; optimalnu duljinu bloka za dani problem, kao i pripadnu vremensku složenost, obično dobivamo iz nejednakosti između aritmetičke i geometrijske sredine.

Dekompozicija na blokove vrlo je fleksibilna ideja. U odnosu na Fenwick tree i segment tree, prednost joj je veća općenitost: može održavati mnoge informacije koje Fenwick tree i segment tree ne mogu.

Naravno, nedostatak je dekompozicije što joj je asimptotska složenost lošija od složenosti segment treea i Fenwick treea.

Ipak, u većini problema dekompozicija na blokove i dalje je dobar izbor.

Slijedi nekoliko primjera.

## Zbroj na intervalu

??? note "Primjer zadatka [LibreOJ 6280 Dekompozicija niza na blokove – uvod 4](https://loj.ac/problem/6280)"
    Zadan je niz $\{a_i\}$ duljine $n$ i treba izvršiti $n$ operacija. Operacije su dviju vrsta:
    
    1.  svim brojevima od $a_l$ do $a_r$ dodaj $x$;
    2.  izračunaj $\sum_{i=l}^r a_i$.
    
        $1 \leq n \leq 5 \times 10^4$

Niz podijelimo na blokove po $s$ elemenata i za svaki blok zapamtimo zbroj njegova intervala $b_i$.

$$
\underbrace{a_1, a_2, \ldots, a_s}_{b_1}, \underbrace{a_{s+1}, \ldots, a_{2s}}_{b_2}, \dots, \underbrace{a_{(s-1) \times s+1}, \dots, a_n}_{b_{\frac{n}{s}}}
$$

Posljednji blok može biti nepotpun (jer $n$ vrlo vjerojatno nije višekratnik od $s$), ali to na naše razmatranje nema većeg utjecaja.

Pogledajmo najprije upit:

-   Ako su $l$ i $r$ u istom bloku, jednostavno zbrojimo izravno (brute force); budući da je duljina bloka $s$, složenost je u najgorem slučaju $O(s)$.
-   Ako $l$ i $r$ nisu u istom bloku, odgovor se sastoji od tri dijela: nepotpunog bloka koji počinje s $l$, nekoliko potpunih blokova u sredini i nepotpunog bloka koji završava s $r$. Za nepotpune blokove i dalje računamo izravno kao gore, a za potpune blokove izravno koristimo već izračunate $b_i$. U tom je slučaju složenost u najgorem slučaju $O(\dfrac{n}{s}+s)$.

Zatim izmjena:

-   Ako su $l$ i $r$ u istom bloku, jednostavno izmijenimo izravno; budući da je duljina bloka $s$, složenost je u najgorem slučaju $O(s)$.
-   Ako $l$ i $r$ nisu u istom bloku, treba izmijeniti tri dijela: nepotpuni blok koji počinje s $l$, nekoliko potpunih blokova u sredini i nepotpuni blok koji završava s $r$. Za nepotpune blokove i dalje izravno mijenjamo vrijednost svakog elementa (ne zaboravite ažurirati zbroj intervala $b_i$), a za potpune blokove izravno izmijenimo $b_i$. U tom je slučaju složenost u najgorem slučaju i dalje $O(\dfrac{n}{s}+s)$.

Iz nejednakosti između aritmetičke i geometrijske sredine slijedi da je vremenska složenost jedne operacije optimalna kad je $\dfrac{n}{s}=s$, tj. $s=\sqrt n$, i iznosi $O(\sqrt n)$.

??? note "Referentni kôd"
    ```cpp
    --8<-- "docs/ds/code/decompose/decompose_1.cpp"
    ```

## Zbroj na intervalu 2

Složenost prethodnog pristupa je $\Omega(1) , O(\sqrt{n})$.

Ovdje predstavljamo algoritam složenosti $O(\sqrt{n}) - O(1)$.

Za upit u $O(1)$ možemo održavati razne prefiksne sume.

No uz izmjene ih nije praktično održavati; možemo održavati samo prefiksne sume unutar pojedinog bloka.

Te prefiksne sume po cijelim blokovima kao jedinicama.

Svaka izmjena košta $O(T+\frac{n}{T})$.

Upit: obuhvaća tri dijela, a svaki se dobiva izravno iz prefiksnih suma, vremenska složenost $O(1)$.

## Dekompozicija upita na blokove

Isti problem, ali sada je duljina niza $n$ i ima $m$ operacija.

Ako je operacija razmjerno malo, možemo ih zapamtiti i pri upitu pribrojiti njihov učinak.

Pretpostavimo da pamtimo najviše $T$ operacija; tada je izmjena $O(1)$, a upit $O(T)$.

Nakon $T$ operacija ponovno izračunamo prefiksne sume, $O(n)$.

Ukupna složenost: $O(mT+n\frac{m}{T})$.

Za $T=\sqrt{n}$ ukupna je složenost $O(m \sqrt{n})$.

### Ostali problemi

Ideja dekompozicije na blokove može se primijeniti i na druge probleme s cijelim brojevima: pronalaženje broja nul-elemenata, pronalaženje prvog elementa različitog od nule, brojanje elemenata s nekim svojstvom itd.

Ima i drugih problema koji se mogu riješiti dekompozicijom, primjerice održavanje skupa brojeva u koji se brojevi smiju dodavati i iz kojeg se smiju brisati, provjera pripada li broj skupu te pronalaženje $k$-tog najvećeg broja. Za rješenje brojeve treba čuvati u rastućem poretku i podijeliti ih na više blokova od po $\sqrt{n}$ brojeva. Pri svakom dodavanju ili brisanju broja blokove treba ponovno uravnotežiti premještanjem brojeva preko granica susjednih blokova.

Poznati offline algoritam [Mo-ov algoritam](../misc/mo-algo.md) također se temelji na ideji dekompozicije na blokove.

## Zadaci za vježbu

-   [UVa - 12003 - Array Transformer](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3154)
-   [UVa - 11990 Dynamic Inversion](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3141)
-   [SPOJ - Give Away](http://www.spoj.com/problems/GIVEAWAY/)
-   [Codeforces - Till I Collapse](http://codeforces.com/contest/786/problem/C)
-   [Codeforces - Destiny](http://codeforces.com/contest/840/problem/D)
-   [Codeforces - Holes](http://codeforces.com/contest/13/problem/E)
-   [Codeforces - XOR and Favorite Number](https://codeforces.com/problemset/problem/617/E)
-   [Codeforces - Powerful array](http://codeforces.com/problemset/problem/86/D)
-   [SPOJ - DQUERY](https://www.spoj.com/problems/DQUERY)

    **Ova je stranica većim dijelom prevedena prema članku [Sqrt-декомпозиция](http://e-maxx.ru/algo/sqrt_decomposition) i njegovu engleskom prijevodu [Sqrt Decomposition](https://cp-algorithms.com/data_structures/sqrt_decomposition.html). Ruska je inačica pod licencijom Public Domain + Leave a Link, a engleska pod licencijom CC-BY-SA 4.0.**
