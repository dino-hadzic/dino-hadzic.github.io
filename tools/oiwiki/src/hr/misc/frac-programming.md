---
title: Razlomačko programiranje
---

Razlomačko programiranje (fractional programming) služi za traženje ekstrema razlomka. Formalno: zadani su $a_i$ i $b_i$, treba pronaći skup $w_i\in\{0,1\}$ koji minimizira ili maksimizira

$$
\displaystyle\frac{\sum\limits_{i=1}^na_i\times w_i}{\sum\limits_{i=1}^nb_i\times w_i}
$$

Jednostavnije rečeno, takvi su zadaci slični sljedećemu: svaki predmet ima dvije težine $a$ i $b$, a treba odabrati nekoliko predmeta tako da $\displaystyle\frac{\sum a}{\sum b}$ bude minimalan ili maksimalan.

Zadaci razlomačkog programiranja obično imaju i neka posebna ograničenja, npr. „nazivnik je barem $W$”.

## Rješavanje

### Binarno pretraživanje

Opća metoda za zadatke razlomačkog programiranja jest binarno pretraživanje po odgovoru. Pretpostavimo da je trenutni kandidat za odgovor $\textit{mid}$; tada bi skup $\{w_i\}$ koji zadovoljava uvjet dao vrijednost veću ili jednaku $\textit{mid}$. Iz tog uvjeta napišemo nejednakost i preoblikujemo je:

$$
\displaystyle
\begin{aligned}
&\frac{\sum a_i\times w_i}{\sum b_i\times w_i}\ge mid\\
\Longrightarrow&\sum a_i\times w_i-mid\times \sum b_i\cdot w_i\ge 0\\
\Longrightarrow&\sum w_i\times(a_i-mid\times b_i)\ge 0
\end{aligned}
$$

Dakle, dovoljno je izračunati maksimum izraza na lijevoj strani nejednakosti. Ako je maksimum veći od $0$, $mid$ je moguć, inače nije. Glavna teškoća razlomačkog programiranja jest kako izračunati maksimum ili minimum izraza $\displaystyle \sum w_i\times(a_i-mid\times b_i)$.

### Dinkelbachov algoritam

Osnovna ideja Dinkelbachova algoritma[^note1] jest da se u svakom koraku odgovor iz prethodnog kruga koristi kao novi ulaz $L$ i da se iterira sve dok odgovor ne konvergira.

## Primjeri zadataka

???+ example "[LOJ 149 01 分数规划 (01 razlomačko programiranje)](https://loj.ac/p/149)"
    Zadano je $n$ predmeta, svaki predmet ima dvije težine $a$ i $b$. Treba pronaći skup $w_i\in\{0,1\}$ u kojem je točno $k$ vrijednosti $w_i$ jednako $1$, tako da se maksimizira vrijednost $\displaystyle\frac{\sum a_i\times w_i}{\sum b_i\times w_i}$.

??? note "Rješenje"
    Neka $a_i-mid\times b_i$ bude težina $i$-tog predmeta; pohlepno odaberemo $k$ predmeta s najvećim težinama. Ako je zbroj težina veći od $0$, $mid$ je moguć, inače nije.

??? note "Referentni kod"
    ```cpp
    --8<-- "docs/misc/code/frac-programming/frac-1.cpp"
    ```

???+ example "[Luogu 4377 Talent Show G](https://www.luogu.com.cn/problem/P4377)"
    Zadano je $n$ predmeta, svaki predmet ima dvije težine $a$ i $b$.
    
    Treba odrediti skup $w_i\in\{0,1\}$ tako da $\displaystyle\frac{\sum w_i\times a_i}{\sum w_i\times b_i}$ bude maksimalan.
    
    Zahtijeva se $\displaystyle\sum w_i\times b_i \geq W$.

??? note "Rješenje"
    U ovom zadatku postoji dodatno ograničenje da nazivnik mora biti barem $W$, pa se pohlepni algoritam iz prethodnog zadatka više ne može koristiti.
    
    Možemo razmotriti 0-1 ruksak (knapsack). Neka $b_i$ bude težina $i$-tog predmeta, a $a_i-mid\times b_i$ njegova vrijednost; time se zadatak pretvara u problem ruksaka. Tada je $dp[n][W]$ maksimum.
    
    Tijekom DP-a zbroj težina predmeta može premašiti $W$; u tom ga slučaju jednostavno smatramo jednakim $W$.

??? note "Referentni kod"
    ```cpp
    --8<-- "docs/misc/code/frac-programming/frac-2.cpp"
    ```

???+ example "[POJ2728 Desert King](http://poj.org/problem?id=2728)"
    Svaki brid ima dvije težine $a_i$ i $b_i$; treba pronaći razapinjuće stablo $T$ takvo da $\displaystyle\frac{\sum_{e\in T}a_e}{\sum_{e\in T}b_e}$ bude minimalan.

??? note "Rješenje"
    Neka $a_i-mid\times b_i$ bude težina svakog brida; tada je minimalno razapinjuće stablo upravo minimum. U ovom zadatku treba pronaći minimalno razapinjuće stablo potpunog grafa, pa valja koristiti Primov algoritam.

??? note "Referentni kod"
    ```cpp
    --8<-- "docs/misc/code/frac-programming/frac-3.cpp"
    ```

???+ example "[\[HNOI2009\] 最小圈 (Minimalni ciklus)](https://www.luogu.com.cn/problem/P3199)"
    Svaki brid ima težinu $w$; treba pronaći ciklus $C$ takav da $\displaystyle\frac{\sum_{e\in C}w}{|C|}$ bude minimalan.

??? note "Rješenje"
    Neka $a_i-mid$ bude težina brida; tada je ciklus s najmanjom težinom upravo minimum.
    
    Budući da trebamo samo provjeriti je li minimum manji od $0$, dovoljno je provjeriti postoji li u grafu negativan ciklus.
    
    Osim toga, za ovaj zadatak postoji i algoritam složenosti $O(nm)$; ako vas zanima, možete pročitati [ovaj članak](https://www.cnblogs.com/y-clever/p/7043553.html).

??? note "Referentni kod"
    ```cpp
    --8<-- "docs/misc/code/frac-programming/frac-4.cpp"
    ```

## Zadaci za vježbu

-   [JSOI2016 最佳团体 (Najbolji tim)](https://loj.ac/problem/2071)
-   [SDOI2017 新生舞会 (Ples za brucoše)](https://loj.ac/problem/2003)
-   [UVa1389 Hard Life](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=4135)
-   [Luogu P2868 \[USACO07DEC\] Sightseeing Cows G](https://www.luogu.com.cn/problem/P2868)
-   [AtCoder Beginner Contest 324 F - Beautiful Path](https://atcoder.jp/contests/abc324/tasks/abc324_f)

## Literatura i bilješke

[^note1]: [Dinkelbach, Werner. "On nonlinear fractional programming." Management science 13.7 (1967): 492-498.](https://doi.org/10.1287/mnsc.13.7.492)
