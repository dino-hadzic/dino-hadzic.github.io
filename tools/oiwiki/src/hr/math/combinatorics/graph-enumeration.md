---
title: Prebrojavanje grafova
---

U kombinatorici je prebrojavanje grafova (graph enumeration) grana koja proučava probleme prebrojavanja grafova sa zadanim svojstvima. [Funkcije izvodnice](../poly/intro.md), [Pólyin teorem prebrojavanja](./polya.md), [simbolička metoda](../poly/symbolic-method.md#%E9%9B%86%E5%90%88%E7%9A%84-cycle-%E6%9E%84%E9%80%A0) i [OEIS](https://oeis.org/) najvažniji su matematički alati za rješavanje takvih problema. Problemi prebrojavanja grafova dijele se na dvije velike skupine: označene (labeled) i neoznačene (unlabeled). U većini slučajeva[^1] označena je inačica problema jednostavnija od odgovarajuće neoznačene, pa ćemo najprije promotriti prebrojavanje označenih struktura.

[^1]: Neoznačena binarna stabla možda su protuprimjer: kad je struktura jednostavna, odgovarajuća je grupa permutacija trivijalna grupa (identity group), pa se označena inačica dobiva jednostavno množenjem s $n!$.

## Označena stabla

To je Cayleyjeva formula; vidi članak o [Prüferovu nizu](../../graph/prufer.md). Isti rezultat možemo dobiti i [Kirchhoffovim teoremom o matrici i stablima](../../graph/matrix-tree.md) ili pomoću [funkcija izvodnica](../poly/intro.md#funkcije-izvodnice) i [Lagrangeova teorema](https://codeforces.com/blog/entry/104184).

### Zadaci

-   [Hihocoder 1047. Random Tree](https://vjudge.net/problem/HihoCoder-1047)

## Označeni povezani grafovi

### Primjer zadatka „POJ 1737” Connected Graph

???+ note "Primjer zadatka [„POJ 1737” Connected Graph](http://poj.org/problem?id=1737)"
    Sažetak zadatka: odredite broj označenih povezanih grafova s $n$ vrhova ($n \leq 50$).

Ovakvi se problemi prvi put pojavljuju u seriji zadataka „男人八题” („Osam zadataka za muškarce”) Lou Tianchenga (楼教主). Neka je $g_n$ broj označenih grafova s $n$ vrhova, a $c_n$ traženi niz. Graf s $n$ vrhova ima najviše $\binom{n}{2}$ bridova, svaki brid ima dva stanja (postoji ili ne postoji) i ta su stanja međusobno neovisna, pa je $g_n = 2^{\binom{n}{2}}$. Fiksiramo jedan vrh i prebrojavamo po veličini komponente povezanosti u kojoj se nalazi: od preostalih $n-1$ vrhova treba odabrati $i-1$ vrhova koji s njim čine jednu komponentu povezanosti. Vrhovi izvan te komponente mogu biti povezani proizvoljno, pa vrijedi sljedeća rekurzivna relacija:

$$
\begin{align}
\sum_{i=1}^{n} \binom{n-1}{i-1} c_i g_{n-i} &= g_n \\
c_n &= g_n - \sum_{i=1}^{n-1} \binom{n-1}{i-1} c_i g_{n-i} 
\end{align}
$$

Prebacivanjem članova dobivamo rekurzivnu formulu za niz $c_n$ složenosti $O(n^2)$, čime se ovaj zadatak može riješiti.

### Primjer zadatka „集训队作业 2013” 城市规划

???+ note "Primjer zadatka [„集训队作业 2013” 城市规划 (Zadaća reprezentacije 2013 – Urbanističko planiranje)](https://www.luogu.com.cn/problem/P4841)"
    Sažetak zadatka: odredite broj označenih povezanih grafova s $n$ vrhova ($n \leq 130000$).

Za probleme s nizovima i većim ograničenjima obično trebamo konstruirati funkcije izvodnice tih nizova kako bismo mogli primijeniti učinkovite algoritme za polinome.

#### Metoda 1: FFT metodom podijeli pa vladaj

Gornju rekurziju možemo promatrati kao oblik samokonvolucije, pa je možemo računati FFT-om metodom podijeli pa vladaj (divide-and-conquer FFT), složenosti $O(n\log^2n)$.

#### Metoda 2: inverz polinoma

Raspišimo binomni koeficijent u gornjoj rekurziji i preuredimo je:

$$
\begin{align}
\sum_{i=1}^{n} \binom{n-1}{i-1} c_i g_{n-i} &= g_n \\
\sum_{i=1}^{n} \frac{c_i}{(i-1)!} \frac{g_{n-i}}{(n-i)!} &= \frac{g_n}{(n-1)!}
\end{align}
$$

Konstruiramo polinome:

$$
\begin{align}
C(x) &= \sum_{n=1} \frac{c_n}{(n-1)!} x^n \\
G(x) &= \sum_{n=0} \frac{g_n}{n!} x^n \\
H(x) &= \sum_{n=1} \frac{g_n}{(n-1)!} x^n
\end{align}
$$

Uvrštavanjem u gornju jednakost dobivamo $CG = H$; dovoljno je izračunati [inverz polinoma](../poly/elementary-func.md#inverz-polinoma) i zatim konvolucijom dobiti $C(x)$.

#### Metoda 3: eksponencijal polinoma

Drugi je pristup iskoristiti [kombinatorno značenje eksponencijala polinoma kod EGF-a](../poly/egf.md#egf-%E4%B8%AD%E5%A4%9A%E9%A1%B9%E5%BC%8F-exp-%E7%9A%84%E7%BB%84%E5%90%88%E6%84%8F%E4%B9%89). Neka su $C(x)$ i $G(x)$ redom EGF-ovi nizova označenih povezanih grafova i jednostavnih grafova; tada među njima vrijedi sljedeća veza:

$$
\begin{align}
\exp(C(x)) &= G(x) \\
C(x) &= \ln(G(x))
\end{align}
$$

Dovoljno je [logaritmom polinoma](../poly/elementary-func.md#logaritam-i-eksponencijalna-funkcija-polinoma) izračunati $C(x)$.

## Označeni Eulerovi i bipartitni grafovi

### Primjer zadatka „SPOJ KPGRAPHS” Counting Graphs

???+ note "Primjer zadatka [„SPOJ KPGRAPHS” Counting Graphs](http://www.spoj.com/problems/KPGRAPHS/)"
    Sažetak zadatka: odredite broj označenih grafova s $n$ vrhova koji redom zadovoljavaju sljedeća svojstva ($n \leq 1000$).
    
    -   povezani grafovi [A001187](https://oeis.org/A001187),
    -   Eulerovi grafovi [A033678](https://oeis.org/A033678),
    -   bipartitni grafovi [A047864](https://oeis.org/A047864).

Ovaj zadatak ograničava duljinu koda, pa se predlošci za polinome ne mogu izravno upotrijebiti, ali nam funkcije izvodnice i dalje pomažu u analizi.

Problem povezanih grafova riješen je u prethodnim primjerima; razmotrimo Eulerove grafove. Uočimo da se sve gore navedene metode za prebrojavanje povezanih grafova mogu poopćiti na označene povezane grafove s proizvoljnim svojstvom. Primjerice, ako u rekurziji za povezane grafove $g_n$ umjesto broja svih grafova označava broj grafova u kojima su stupnjevi svih vrhova parni, dobiveni $c_n$ upravo je broj Eulerovih grafova.

Rekurzivni postupak iz POJ 1737 zapakirajmo u funkciju „povezivanja” (prijelaza na povezane strukture):

```cpp
void ln(Int C[], Int G[]) {
  for (int i = 1; i <= n; ++i) {
    C[i] = G[i];
    for (int j = 1; j <= i - 1; ++j)
      C[i] -= binom[i - 1][j - 1] * C[j] * G[i - j];
  }
}
```

Prva se dva pitanja tada rješavaju bez poteškoća:

```cpp
for (int i = 1; i <= n; ++i) G[i] = pow(2, binom[i][2]);
ln(C, G);
for (int i = 1; i <= n; ++i) G[i] = pow(2, binom[i - 1][2]);
ln(E, G);
```

Uočimo da je ovaj rekurzivni postupak povezivanja zapravo ekvivalentan računanju logaritma polinoma na odgovarajućem EGF-u. Analogno možemo napisati i funkciju obrnutog povezivanja, koja je ekvivalentna računanju eksponencijala polinoma na EGF-u.

```cpp
void exp(Int G[], Int C[]) {
  for (int i = 1; i <= n; ++i) {
    G[i] = C[i];
    for (int j = 1; j <= i - 1; ++j)
      G[i] += binom[i - 1][j - 1] * C[j] * G[i - j];
  }
}
```

Razmotrimo sada prebrojavanje označenih bipartitnih grafova.

Neka $b_n$ označava broj bipartitnih grafova s n vrhova, a $g_n$ broj grafova s $n$ vrhova čiji su vrhovi obojeni dvjema bojama tako da između vrhova iste boje nema bridova. Prebrojavanjem po broju vrhova jedne od boja dobivamo[^2]:

$$
g_n = \sum_{i=0}^{n} \binom{n}{i}2^{i(n-i)}
$$

[^2]: [Blog korisnika 粉兔 (PinkRabbit)](https://www.luogu.com.cn/blog/PinkRabbit/solution-sp4420) pokazuje da se ovaj niz može ubrzati i [Chirp Z-transformacijom](../poly/czt.md).

Vezu između $g_n$ i $b_n$ uspostavit ćemo dvjema različitim metodama.

#### Metoda 1: dvostruko prebrojavanje

Neka $c_{n, k}$ označava broj bipartitnih grafova s k komponenata povezanosti. Lako se dobiva sljedeća veza:

$$
\begin{align}
b_n &= \sum_{i=1}^{n} c_{n, i} \\
g_n &= \sum_{i=1}^{n} c_{n, i} 2^i 
\end{align}
$$

Usporedimo dva izraza za $g_n$ i raspišimo:

$$
\begin{align}
\sum_{i=0}^{n} \binom{n}{i}2^{i(n-i)} &= \sum_{i=1}^{n} c_{n, i} 2^i \\
c_{n, i} &= \sum_{i=0}{n-1} \binom{n-1}{i-1} c_{n, 1}c_{n-i,k-1}
\end{align}
$$

Odatle se lako dobiva rekurzivna relacija za $b_n$ složenosti $O(n^3)$; primjenom formule uključivanja-isključivanja može se dodatno optimizirati na $O(n^2)$ i riješiti zadatak.

#### Metoda 2: rekurzija povezivanjem

Druga i treća metoda koriste povezane bipartitne grafove $b1_n$  [A001832](https://oeis.org/A001832) kao most između $g_n$ i $b_n$.

Uočimo da svaki povezani bipartitni graf ima točno dva različita bojenja, koja odgovaraju dvama različitim povezanim 2-obojenim grafovima,
pa je niz dobiven povezivanjem niza $g_n$ točno dvostruki $b1_n$, a $b_n$ se iz $b1_n$ dobiva obrnutim povezivanjem.

Stoga:

```cpp
for (int i = 1; i <= n; ++i) {
  G[i] = 0;
  for (int j = 0; j < i + 1; ++j) G[i] += binom[i][j] * pow(2, j * (i - j));
}
ln(B1, G);
for (int i = 1; i <= n; ++i) B1[i] /= 2;
exp(B, B1);
```

Oba rekurzivna postupka imaju složenost $O(n^2)$, čime se zadatak može riješiti.

#### Metoda 3: eksponencijal polinoma

Uočimo da se gornji rekurzivni postupak može razumjeti i preko EGF-a.

Neka je $G(x)$ EGF niza $g_n$, $B1(x)$ EGF niza $b1_n$, a $B(x)$ EGF niza $b_n$. Primjenom pristupa iz druge metode dobivamo:

$$
\begin{align}
G(x) &= \exp(2B1(x)) \\
B(x) &= \exp(B1(x))  \\
     &= \exp(\frac{\ln{G(x)}}{2}) \\
     &= \sqrt{G}
\end{align}
$$

Deriviranjem obiju strana jednakosti i usporedbom koeficijenata dobivamo rekurzivnu formulu koja se lako programira, čime se zadatak može riješiti.
Uočimo da su druga i treća metoda u biti iste, a treća u općem slučaju daje bolju vremensku složenost.

$$
\begin{align}
B_n^2 &= G  \\
2B_nB_n' &= G' 
\end{align}
$$

??? note "Referentni kôd"
    ```cpp
    --8<-- "docs/math/code/combinatorics/graph-enumeration/graph-enumeration_1.cpp"
    ```

### Zadaci

-   [UOJ Goodbye Jihai D. 新年的追逐战 (Novogodišnja potjera)](https://uoj.ac/contest/50/problem/498)
-   [BZOJ 3864. 大朋友和多叉树 (Veliki prijatelj i stablo s više grana)](https://hydro.ac/p/bzoj-P3864)
-   [BZOJ 2863. 愤怒的元首 (Bijesni vođa)](https://hydro.ac/p/bzoj-P2863)
-   [Luogu P6295. 有标号 DAG 计数 (Prebrojavanje označenih DAG-ova)](https://www.luogu.com.cn/problem/P6295)
-   [LOJ 6569. 仙人掌计数 (Prebrojavanje kaktusa)](https://loj.ac/p/6569)
-   [LOJ 6570. 毛毛虫计数 (Prebrojavanje gusjenica)](https://loj.ac/p/6570)
-   [Luogu P5434. 有标号荒漠计数 (Prebrojavanje označenih pustinja)](https://www.luogu.com.cn/problem/P5434)
-   [Luogu P3343. \[ZJOI2015\] 地震后的幻想乡 (Gensokyo nakon potresa)](https://www.luogu.com.cn/problem/P3343)
-   [HDU 5279. YJC plays Minecraft](https://acm.hdu.edu.cn/showproblem.php?pid=5279)
-   [Luogu P7364. 有标号二分图计数 (Prebrojavanje označenih bipartitnih grafova)](https://www.luogu.com.cn/problem/P7364)
-   [Luogu P5827. 点双连通图计数 (Prebrojavanje vršno 2-povezanih grafova)](https://www.luogu.com.cn/problem/P5827)
-   [Luogu P5827. 边双连通图计数 (Prebrojavanje bridno 2-povezanih grafova)](https://www.luogu.com.cn/problem/P5828)
-   [Luogu P6596. How Many of Them](https://www.luogu.com.cn/problem/P6596)
-   [Luogu U152448. 有标号强连通图计数 (Prebrojavanje označenih jako povezanih grafova)](https://www.luogu.com.cn/problem/U152448)
-   [Project Euler 434. Rigid graphs](https://projecteuler.net/problem=434)

## Riddellova formula

Gornja upotreba eksponencijala EGF-a ponekad se naziva Riddellovom formulom za označene grafove (Riddell's formula for labeled graphs), a [Eulerova transformacija](../poly/symbolic-method.md#%E9%9B%86%E5%90%88%E7%9A%84-multiset-%E6%9E%84%E9%80%A0) funkcije izvodnice ponekad Riddellovom formulom za neoznačene grafove (Riddell's formula for unlabeled graphs). Potonja se prvi put pojavila u Eulerovu proučavanju particija brojeva; osim u prebrojavanju grafova, pojavljuje se i u problemu neograničenog ruksaka (unbounded knapsack).

Za zadani niz $a_i$ i pripadnu OGF $A(x)$ Eulerova transformacija od $A(x)$ definira se kao:

$$
\begin{align}
\mathcal{E}(A(x)) &= \prod_{i} (1-x^i)^{-a_i}  \\
                  &= \exp (\sum_{i} \frac{A(x^i)}{i})  
\end{align}
$$

Neka su $b_i$ koeficijenti od $\mathcal{E}(A(x))$ i definirajmo pomoćni niz $c_i = \sum_{d|n} d a_d$; tada vrijedi rekurzivna formula

$$
n b_n = c_n + \sum_{i=1}^{n-1} c_i b_{n-i}
$$

## Neoznačena stabla

### Primjer zadatka „SPOJ PT07D” Let us count 1 2 3

???+ note "Primjer zadatka [„SPOJ PT07D” Let us count 1 2 3](https://www.spoj.com/problems/PT07D/)"
    Sažetak zadatka: odredite broj stabala s n vrhova koja redom zadovoljavaju sljedeća svojstva.
    
    -   označena korijenska stabla [A000169](https://oeis.org/A000169),
    -   označena stabla bez korijena [A000272](https://oeis.org/A000272),
    -   neoznačena korijenska stabla [A000081](https://oeis.org/A000081),
    -   neoznačena stabla bez korijena [A000055](https://oeis.org/A000055).

#### Korijenska stabla

Označeni je slučaj riješen ranije u tekstu; razmotrimo neoznačena korijenska stabla. Neka je njihova OGF $F(x)$. Primjenom Eulerove transformacije dobivamo:

$$
F(x) = x\mathcal{E}(F(x))
$$

Dovoljno je izdvojiti koeficijente.

#### Stabla bez korijena

Primijenimo uključivanje-isključivanje: od broja korijenskih stabala oduzmemo ona u kojima korijen nije centroid (težište), pri čemu razlikujemo slučajeve prema parnosti $n$.

Kad je $n$ neparan:

Nužno postoji podstablo veličine $\geq \left\lceil \frac{n}{2}\right\rceil$; prebrojavanjem po veličini tog podstabla dobivamo:

$$
g_n = f_n - \sum_{i=\left\lceil\frac{n}{2}\right\rceil}^{n-1} f_i f_{n-i}
$$

Kad je $n$ paran:

Uočimo da se u slučaju s dva centroida gornjim postupkom oduzima samo jednom, pa treba dodatno oduzeti

$$
g_n = f_n - \sum_{i=\frac{n}{2}+1}^{n-1} f_i f_{n-i} - \binom{f_{\frac{n}{2}}}{2}
$$

### Primjer zadatka „Luogu P5900” 无标号无根树计数

???+ note "Primjer zadatka [„Luogu P5900” 无标号无根树计数 (Prebrojavanje neoznačenih stabala bez korijena)](https://www.luogu.com.cn/problem/P5900)"
    Sažetak zadatka: odredite broj neoznačenih stabala bez korijena s n vrhova ($n \leq 200000$).

Za veća ograničenja postupak je isti: nakon Eulerove transformacije dovoljno je upotrijebiti predloške za polinome.

## Neoznačeni jednostavni grafovi

### Primjer zadatka „SGU 282. Isomorphism” Isomorphism

???+ note "Primjer zadatka [„SGU 282. Isomorphism” Isomorphism](https://codeforces.com/problemsets/acmsguru/problem/99999/282)"
    Sažetak zadatka: odredite broj načina bojenja bridova neoznačenog potpunog grafa s n vrhova s m boja.

Uočimo da su za m = 2 traženi objekti upravo neoznačeni jednostavni grafovi [A000088](https://oeis.org/A000088). Promotrimo Pólyin teorem prebrojavanja:

$$
\frac{1}{|G|}\sum_{g\in G} m^{c(g)}
$$

U ovom je zadatku grupa permutacija $G$ grupa permutacija bridova koju generira simetrična grupa reda $n$ na vrhovima, ali gruba sila prolazi kroz $O(n!)$ permutacija, što nije dovoljno za rješavanje zadatka.

Razvrstajmo permutacije prema njihovoj cikličkoj strukturi: svaka ciklička struktura odgovara jednoj particiji broja, a particije generiramo funkcijom dfs(). Problem se tako svodi na određivanje broja permutacija $w(p)$ koje odgovaraju svakoj particiji $p$ i broja ciklusa $c(p)$ u svakoj klasi permutacija; odgovor je

$$
\frac{1}{|G|} \sum_{p \in P} w(p) m^{c(p)}
$$

Promotrimo $w(p)$: svaki dio particije odgovara jednoj cikličkoj permutaciji, a redoslijed dijelova iste veličine nije bitan, pa imamo:

$$
w(p) = \frac{n!}{\prod_{i}(p_i)\prod_{i}(q_i!)} 
$$

Ovdje $q_i$ označava koliko se puta dio veličine $i$ pojavljuje u $p$.

Promotrimo $c(p)$: broj ciklusa na skupu vrhova na koje $p$ djeluje jednak je $|p|$, ali zadatak traži bojenje bridova, pa treba promotriti permutaciju bridova koju generira permutacija vrhova.

Ako su oba vrha nekog brida u istom ciklusu veličine $p_i$, broj ciklusa koje generiraju bridovi točno je $\left\lfloor \frac{p_i}{2} \right\rfloor$.

Ako su vrhovi brida u dvama različitim ciklusima veličina $p_i$ i $p_j$, duljina je svakog ciklusa $\operatorname{lcm}(p_i,p_j)$, pa je broj ciklusa koje generiraju bridovi točno $\frac{p_i p_j}{\operatorname{lcm}(p_i,p_j)} = \gcd(p_i, p_j)$.

??? note "Referentni kôd"
    ```cpp
    --8<-- "docs/math/code/combinatorics/graph-enumeration/graph-enumeration_2.cpp"
    ```

## Zadaci

-   [CodeForces 438 E. The Child and Binary Tree](https://codeforces.com/problemset/problem/438/E)
-   [Luogu P5448. \[THUPC2018\] 好图计数 (Prebrojavanje dobrih grafova)](https://www.luogu.com.cn/problem/P5448)
-   [Luogu P5818. \[JSOI2011\] 同分异构体计数 (Prebrojavanje izomera)](https://www.luogu.com.cn/problem/P5818)
-   [Luogu P6597. 烯烃计数 (Prebrojavanje alkena)](https://www.luogu.com.cn/problem/P6597)
-   [Luogu P6598. 烷烃计数 (Prebrojavanje alkana)](https://www.luogu.com.cn/problem/P6598)
-   [Luogu P4128. \[SHOI2006\] 有色图 (Obojeni grafovi)](https://www.luogu.com.cn/problem/P4128)
-   [Luogu P4727. \[HNOI2009\] 图的同构计数 (Prebrojavanje izomorfizama grafova)](https://www.luogu.com.cn/problem/P4727)
-   [AtCoder Beginner Contest 222 H. Binary Tree](https://atcoder.jp/contests/abc222/tasks/abc222_h)
-   [AtCoder Beginner Contest 284 Ex. Count Unlabeled Graphs](https://atcoder.jp/contests/abc284/tasks/abc284_h)
-   [Luogu P4708. 画画 (Crtanje)](https://www.luogu.com.cn/problem/P4708)
-   [Luogu P7592. 数树 (Prebrojavanje stabala) (2021 CoE-II E)](https://www.luogu.com.cn/problem/P7592)
-   [Luogu P5206. \[WC2019\] 数树 (Prebrojavanje stabala)](https://www.luogu.com.cn/problem/P5206)

## Literatura i napomene

1.  [WC2015, 顾昱洲营员交流资料 Graphical Enumeration (Gu Yuzhou, materijali za razmjenu među polaznicima: Graphical Enumeration)](https://github.com/lychees/ACM-Training/blob/master/Note/%E5%86%AC%E4%BB%A4%E8%90%A5/2015/%E9%A1%BE%E6%98%B1%E6%B4%B2%E8%90%A5%E5%91%98%E4%BA%A4%E6%B5%81%E8%B5%84%E6%96%99%20Graphical%20Enumeration.pdf)
2.  [WC2019, 生成函数，多项式算法与图的计数 (Funkcije izvodnice, algoritmi za polinome i prebrojavanje grafova)](https://github.com/lychees/ACM-Training/tree/master/Note/%E5%86%AC%E4%BB%A4%E8%90%A5/2019/d4)
3.  [Counting labeled graphs - Algorithms for Competitive Programming](https://cp-algorithms.com/combinatorics/counting_labeled_graphs.html)
4.  [Graphical Enumeration Paperback, Frank Harary, Edgar M. Palmer](https://github.com/lychees/ACM-Training/blob/master/Note/Book/)
5.  [The encyclopedia of integer sequences, N. J. A. Sloane, Simon Plouffe](https://github.com/lychees/ACM-Training/blob/master/Note/Book/The%20encyclopedia%20of%20integer%20sequences%20\(N.%20J.A.%20Sloane%2C%20Simon%20Plouffe\).pdf)
6.  [Combinatorial Problems and Exercises, László Lovász](https://github.com/lychees/ACM-Training/blob/master/Note/Book/Combinatorial%20Problems%20and%20Exercises_L%C3%A1szl%C3%B3%20Lov%C3%A1sz.pdf)
7.  [Graph Theory and Additive Combinatorics](https://yufeizhao.com/gtacbook/)
