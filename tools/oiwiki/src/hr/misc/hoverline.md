---
title: Metoda viseće linije
---

## Uvod

Područje primjene metode viseće linije (engl. hanging line / hoverline) podskup je područja primjene monotonog stoga. Konkretno, metoda viseće linije primjenjiva je na zadatke koji zadovoljavaju sljedeće uvjete:

-   pri obilasku niza treba održavati monotonu informaciju;
-   mogu se riješiti monotonim stogom;
-   nije potrebno binarno pretraživanje po monotonom stogu.

Čini se da je metoda viseće linije zamjenjiva i da nije osobito korisna, ali je pojmovno jednostavnija od monotonog stoga, pa je prikladnija početnicima u OI-ju za razumijevanje i rješavanje zadataka kao što je najveća podmatrica.

## Primjeri zadataka

???+ note "[SPOJ HISTOGRA - Largest Rectangle in a Histogram](https://www.spoj.com/problems/HISTOGRA)"
    Ukratko: na vodoravnoj liniji stoji $n$ pravokutnika širine $1$; odredite površinu najvećeg podpravokutnika sadržanog u tim pravokutnicima.

Viseća linija okomita je dužina koja ima dva svojstva – početni položaj i visinu – i može se pomicati ulijevo i udesno sve dok njezin gornji kraj ne prelazi visinu pravokutnika na trenutačnom položaju.

Za jednu viseću liniju, uz uvjet da gornji kraj ne prelazi visinu pravokutnika na trenutačnom položaju i da ne izlazi iz granica, pomičemo je ulijevo i udesno i određujemo najdalje kamo se može proširiti ulijevo i udesno; površina koju je ta viseća linija pritom prebrisala najveći je mogući pravokutnik koji sadrži tu viseću liniju. Lako se vidi da najveći podpravokutnik nužno sadrži neku viseću liniju s početnim položajem $i$ i visinom $h_i$. Nabrajanjem taj proces ima vremensku složenost $O(n ^ 2)$, ali metodom viseće linije možemo ga optimizirati na $O(n)$.

Razmotrimo kako brzo pronaći krajnji lijevi položaj do kojeg viseća linija može doći.

### Postupak

Definirajmo $l_i$ kao trenutačno pronađeni krajnji lijevi položaj do kojeg se viseća linija na položaju $i$ može proširiti; lako se vidi da je $l_i$ na početku jednak $i$, a dalje treba provjeriti može li se još proširiti ulijevo.

-   Ako je trenutačno $l_i = 1$, došli smo do granice i ne može se.
-   Ako je trenutačno $a_i > a_{l_i - 1}$, s položaja do kojeg je viseća linija proširena ne može se dalje ulijevo.
-   Ako je trenutačno $a_i \le a_{l_i - 1}$, viseća linija može se još proširiti ulijevo, a kamo god se ulijevo može proširiti viseća linija na položaju $l_i - 1$, sigurno može i viseća linija na položaju $i$; stoga $l_i$ ažuriramo na $l_{l_i - 1}$ i nastavljamo s provjerom.

Amortiziranom analizom može se dokazati da će svaki $l_i$ biti posjećen najviše jednom od strane drugih $l_j$, pa je vremenska složenost $O(n)$.

### Implementacija

??? note "Primjer koda"
    ```cpp
    --8<-- "docs/misc/code/hoverline/hoverline_1.cpp"
    ```

???+ note "[UVa1619 Feel Good](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=4494)"
    Za niz duljine $n$ pronađite podinterval takav da je umnožak najmanjeg elementa podintervala i zbroja njegovih elemenata najveći; uz najveću vrijednost ugode treba minimizirati duljinu, a uz najmanju duljinu minimizirati indeks lijevog kraja.

U ovom zadatku možemo nabrajati najmanji element: broj $a_i$ na svakom položaju uzmemo kao najmanji element i razmotrimo proširivanje od $i$ ulijevo i udesno, tražeći što širi interval $[l, r]$ za koji vrijedi $\min\limits _ {j = l} ^ r a_j = a_i$. Tako se zadatak svodi na model viseće linije.

??? note "Primjer koda"
    ```cpp
    --8<-- "docs/misc/code/hoverline/hoverline_2.cpp"
    ```

## Najveća podmatrica

???+ note "[P4147 玉蟾宫 (Palača žadne žabe)](https://www.luogu.com.cn/problem/P4147)"
    Zadana je matrica $n \times m$ koja sadrži znakove `'F'` i `'R'`; odredite površinu najveće podmatrice $\times 3$, takve da je svaki element te podmatrice `'F'`.

Primjećujemo da je model ovog zadatka vrlo sličan modelu prvog zadatka. Pažljivijom analizom vidimo: ako svaki put promatramo samo sve elemente jednog retka, a kao duljinu viseće linije na položaju $(x, y)$ uzmemo udaljenost do koje se element na tom položaju može proširiti prema gore, tada je najveća podmatrica nužno jedan od najvećih pravokutnika dobivenih proširivanjem tih visećih linija ulijevo i udesno.

??? note "Primjer koda"
    ```cpp
    --8<-- "docs/misc/code/hoverline/hoverline_3.cpp"
    ```

## Zadaci za vježbu

-   [P1169「ZJOI2007」棋盘制作 (Izrada šahovske ploče)](https://www.luogu.com.cn/problem/P1169)
