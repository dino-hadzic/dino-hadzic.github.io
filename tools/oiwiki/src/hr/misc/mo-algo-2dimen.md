---
title: Dvodimenzionalni Mo algoritam
---

Dvodimenzionalni Mo algoritam (2D Mo's algorithm), kako mu i ime kaže, algoritam je u kojem se svako stanje može proširiti u četiri smjera.

U dvodimenzionalnom Mo algoritmu svako pomicanje pokazivača obrađuje brojeve u jednom retku ili jednom stupcu; konkretna je implementacija slična običnom jednodimenzionalnom Mo algoritmu, pa je ovdje ne ponavljamo. Ovdje se usredotočujemo na izbor veličine bloka.

## Izbor veličine bloka

Neka je broj upita $q$, neka su koordinate gornjeg lijevog kuta trenutne matrice $(x_1,\ y_1)$, a donjeg desnog kuta $(x_2,\ y_2)$, i neka je veličina bloka $B$.

Tada se pokazivač $x_1$ pomiče $\Theta(q\cdot B)$ puta, a pokazivač $y_2$ pomiče se $\Theta(n^4\cdot B^{-3})$ puta.

Stoga je dovoljno uzeti $q\cdot B=n^4\cdot B^{-3}$, tj. $B=n\cdot q^{-\frac 14}$.

Pazite: ovako izračunani $B$ **može biti $0$**, pa **taj slučaj treba posebno obraditi**.

Na kraju, vremenska složenost dijela s računanjem jest $\Theta(n^2\cdot q^{\frac 34})$; kad dodamo sortiranje upita, ukupna je vremenska složenost $\Theta(n^2\cdot q^{\frac 34}+q\log q)$.

## Primjer zadatka 1

???+ note "[BZOJ 2639 矩形计算 (Računanje na pravokutnicima)](https://hydro.ac/p/bzoj-P2639)"
    Zadana je matrica $n\times m$ čiji je svaki element cijeli broj, a zatim $q$ upita; svaki upit traži težinu neke podmatrice. Težina matrice definira se ovako: ako se cijeli broj $x$ u toj matrici pojavljuje $p$ puta, on težini te matrice doprinosi $p^2$.
    
    Ograničenja: $1\leq n,\ m\leq 200$, $0\leq q\leq 10^5$, $|$ element matrice $| \leq 2\times 10^9$.

??? note "Ideja rješenja"
    Najprije diskretiziramo vrijednosti, a u dvodimenzionalnom Mo algoritmu nizom bilježimo trenutni broj pojavljivanja svakog broja.

??? note "Primjer koda"
    ```cpp
    --8<-- "docs/misc/code/mo-algo-2dimen/mo-algo-2dimen_1.cpp"
    ```

## Primjer zadatka 2

???+ note "[Luogu P1527 \[国家集训队\] 矩阵乘法 (Množenje matrica)](https://www.luogu.com.cn/problem/P1527)"
    Zadana je matrica $n\times n$ i $q$ upita; svaki upit traži $k$-ti najmanji broj u nekoj podmatrici.
    
    Ograničenja: $1\leq n\leq 500$, $1\leq q\leq 6\times 10^4$, $0\leq a_{i,j}\leq 10^9$.

Najprije, kao i u prethodnom zadatku, treba diskretizirati cijelu matricu. No pazite: u ovom zadatku, osim podjele na blokove po pozicijama, treba podijeliti na blokove i domenu vrijednosti (value-range blocking) da bi se mogao izračunati odgovor.

Ovdje je za optimizaciju potrebno i sortiranje po parnosti bloka (odd-even sorting); detalje potražite u članku [Obični Mo algoritam](../misc/mo-algo.md#optimizacija-običnog-mo-algoritma).

U ovom zadatku vremensko ograničenje nije osobito široko, pa pazite na konstantu u kodu. Izračunana veličina bloka općenito je mala: kad su $n$ i $q$ maksimalni, veličina bloka iznosi oko $11$, pa se može izravno postaviti kao konstanta kako bi se uštedjelo vrijeme izvođenja.

??? note "Primjer koda"
    ```cpp
    --8<-- "docs/misc/code/mo-algo-2dimen/mo-algo-2dimen_2.cpp"
    ```
