---
title: LGV lema
---

## Uvod

Lindström–Gessel–Viennotova lema, skraćeno LGV lema, služi za rješavanje problema poput prebrojavanja disjunktnih puteva u usmjerenom acikličkom grafu.

Preduvjeti: osnovni dio [Pojmova iz teorije grafova](./concept.md), [matrice](../math/linear-algebra/matrix.md), [Gaussova eliminacija za determinantu](../math/numerical/gauss.md).

LGV lema vrijedi samo za **usmjerene acikličke grafove**.

## Definicije

$\omega(P)$ označava umnožak težina svih bridova na putu $P$. (Pri prebrojavanju puteva sve težine možemo postaviti na $1$.) (Zapravo, težine bridova mogu biti i funkcije izvodnice.)

$e(u, v)$ označava zbroj $\omega(P)$ po **svim** putevima $P$ od $u$ do $v$, tj. $e(u, v)=\sum\limits_{P:u\rightarrow v}\omega(P)$.

Skup početaka $A$ je podskup skupa vrhova usmjerenog acikličkog grafa veličine $n$.

Skup završetaka $B$ također je podskup skupa vrhova veličine $n$.

Skupina disjunktnih puteva $S$ iz $A$ u $B$: $S_i$ je put od $A_i$ do $B_{\sigma(S)_i}$ ($\sigma(S)$ je permutacija), a za sve $i\ne j$ putevi $S_i$ i $S_j$ nemaju zajedničkih vrhova.

$t(\sigma)$ označava broj inverzija permutacije $\sigma$.

## Lema

$$
M = \begin{bmatrix}e(A_1,B_1)&e(A_1,B_2)&\cdots&e(A_1,B_n)\\
e(A_2,B_1)&e(A_2,B_2)&\cdots&e(A_2,B_n)\\
\vdots&\vdots&\ddots&\vdots\\
e(A_n,B_1)&e(A_n,B_2)&\cdots&e(A_n,B_n)\end{bmatrix}
$$

$$
\det(M)=\sum\limits_{S:A\rightarrow B}(-1)^{t(\sigma(S))}\prod\limits_{i=1}^n \omega(S_i)
$$

Pri tome $\sum\limits_{S:A\rightarrow B}$ označava zbroj po svim skupinama disjunktnih puteva $S$ iz $A$ u $B$ koje zadovoljavaju gornje uvjete.

### Dokaz

Iz definicije determinante dobivamo

$$
\begin{align}
\det(M)&=\sum_{\sigma}(-1)^{t(\sigma)}\prod_{i=1}^n e(a_i,b_{\sigma(i)})\\
&=\sum_{\sigma}(-1)^{t(\sigma)}\prod_{i=1}^n \sum_{P:a_i\to b_{\sigma(i)}} \omega(P)
\end{align}
$$

Primijetimo da je $\prod\limits_{i=1}^n \sum\limits_{P:a_i\to b_{\sigma(i)}} \omega(P)$ zapravo zbroj $\omega(P)$ po svim skupinama puteva $P$ iz $A$ u $B$ s permutacijom $\sigma$.

$$
\begin{align}
&\sum_{\sigma}(-1)^{t(\sigma)}\prod_{i=1}^n \sum_{P:a_i\to b_{\sigma(i)}} \omega(P)\\
=&\sum_{\sigma}(-1)^{t(\sigma)}\sum_{P=\sigma}\omega(P)\\
=&\sum_{P:A\to B}(-1)^{t(\sigma)}\prod_{i=1}^n \omega(P_i)
\end{align}
$$

Ovdje je $P$ proizvoljna skupina puteva.

Neka je $U$ skupina disjunktnih puteva, a $V$ skupina puteva koji se sijeku,

$$
\begin{align}
&\sum_{P:A\to B}(-1)^{t(\sigma)}\prod_{i=1}^n \omega(P_i)\\
=&\sum_{U:A\to B}(-1)^{t(U)}\prod_{i=1}^n \omega(U_i)+\sum_{V:A\to B}(-1)^{t(V)}\prod_{i=1}^n \omega(V_i)
\end{align}
$$

Pretpostavimo da u $P$ postoji par puteva koji se sijeku, $P_i:a_1 \to u \to b_1,P_j:a_2 \to u \to b_2$. Tada nužno postoji i njemu pridružena skupina puteva koji se sijeku $P_i'=a_1\to u\to b_2,P_j'=a_2\to u\to b_1$, dok su ostali putevi u $P'$ isti kao u $P$. Dobivamo $\omega(P)=\omega(P'),t(P)=t(P')\pm 1$.

Stoga je $\sum\limits_{V:A\to B}(-1)^{t(\sigma)}\prod\limits_{i=1}^n \omega(V_i)=0$.

Dakle, $\det(M)=\sum\limits_{U:A\to B}(-1)^{t(U)}\prod\limits_{i=1}^n \omega(U_i)$.

Time je dokaz završen[^1].

## Primjeri zadataka

???+ note "Primjer 1 [CF348D Turtles](https://codeforces.com/contest/348/problem/D)"
    Zadatak: zadana je rešetkasta ploča $n\times m$ u kojoj su neka polja prohodna, a neka nisu. Kornjača s polja $(x, y)$ može prijeći samo na $(x+1, y)$ ili $(x, y+1)$. Odredite broj parova disjunktnih puteva kornjače od $(1, 1)$ do $(n, m)$ modulo $10^9+7$. $2\le n,m\le3000$.

Prilično izravna primjena LGV leme. Promatramo sve valjane puteve i primjećujemo da svaki put iz $(1,1)$ nužno prolazi kroz $A=\{(1,2), (2,1)\}$, a da do cilja nužno prolazi kroz $B=\{(n-1, m), (n, m-1)\}$, pa su $A, B$ odmah određeni. Primjenom LGV leme odgovor je:

$$
\begin{vmatrix}
f(a_1, b_1) & f(a_1, b_2) \\
f(a_2, b_1) & f(a_2, b_2)
\end{vmatrix} = f(a_1, b_1)\times f(a_2, b_2) - f(a_1, b_2)\times f(a_2, b_1)
$$

Pri tome je $f(a, b)$ broj puteva $a\rightarrow b$ na ploči; prebrojavanje puteva na rešetki s prepreka izravno je DP složenosti $O(nm)$, pa se $f$ lako računa. Ukupna složenost $O(nm)$.

??? note "Referentni kôd"
    ```cpp
    --8<-- "docs/graph/code/lgv/lgv_2.cpp"
    ```

???+ note "Primjer 2 [HDU 5852 Intersection is not allowed!](https://acm.hdu.edu.cn/showproblem.php?pid=5852)"
    Zadatak: zadana je ploča $n\times n$; figura s polja $(x, y)$ može prijeći samo na $(x, y+1)$ ili $(x + 1, y)$. Ima $k$ figura, $i$-ta figura na početku stoji na $(1, a_i)$ i mora doći do $(n, b_i)$, a putevi se u parovima ne smiju sjeći. Odredite broj načina modulo $10^9+7$. $1\le n\le 10^5$, $1\le k\le 100$, zajamčeno je $1\le a_1<a_2<\dots<a_n\le n$, $1\le b_1<b_2<\dots<b_n\le n$.

Primijetimo da, ako se putevi ne sijeku, put nužno vodi od $a_i$ do $b_i$, pa je u LGV lemi uvijek $\sigma(S)_i=i$ i ne treba razmišljati o predznaku. Težine bridova postavimo na $1$ i izravno primijenimo lemu.

Broj puteva od $(1, a_i)$ do $(n, b_j)$ jednak je broju načina da od $n-1+b_j-a_i$ koraka odaberemo $n-1$ koraka prema dolje, pa je $e(A_i, B_j)=\binom{n-1+b_j-a_i}{n-1}$.

Determinantu računamo Gaussovom eliminacijom.

Složenost je $O(n+k(k^2 + \log p))$, gdje je $\log p$ složenost računanja inverza.

??? note "Referentni kôd"
    ```cpp
    --8<-- "docs/graph/code/lgv/lgv_1.cpp"
    ```

## Literatura

[^1]: Dokaz preuzet iz [Zhihu – dokaz LGV leme](https://zhuanlan.zhihu.com/p/517819133)
