---
title: Prefiksne sume i razlike
---

## Uvod

Prefiksne sume i razlike (difference array) tehnike su koje se često koriste na algoritamskim natjecanjima: prve služe za brzo računanje sume na intervalu, a druge za učinkovito mijenjanje cijelog intervala.

???+ tip "Dogovor"
    Radi lakšeg izlaganja, u ovom članku indeksi niza $\{a_i\}$ počinju od $1$, a dodatno definiramo $a_0 = 0$.

## Prefiksne sume

Prefiksnu sumu možemo jednostavno shvatiti kao „sumu prvih $n$ članova niza”; to je važan oblik pretprocesiranja.

### Jednodimenzionalne prefiksne sume

Ako za niz $\{a_i\}$ duljine $n$ treba više puta odgovoriti na upit o sumi brojeva na intervalu $[l,r]$, možemo razmotriti prefiksne sume. Prefiksna suma niza je

$$
S_{i} = \sum_{j=1}^i a_j.
$$

Može se izračunati član po član iz rekurzivne relacije

$$
S_0 = 0,~ S_i = S_{i-1} + a_i.
$$

Za upit o sumi niza na intervalu $[l,r]$ dovoljno je izračunati razliku

$$
S([l,r]) = S_r - S_{l-1}.
$$

Tako se pretprocesiranjem u vremenu $O(n)$ složenost jednog upita za sumu intervala spušta na $O(1)$.

???+ example "Referentna implementacija"
    === "C++"
        ```cpp
        --8<-- "docs/basic/code/prefix-sum/prefix-sum_1.cpp:core"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/basic/code/prefix-sum/prefix-sum_1.py:core"
        ```

Standardna biblioteka C++-a implementira funkciju za prefiksne sume [`std::partial_sum`](https://en.cppreference.com/w/cpp/algorithm/partial_sum), definiranu u zaglavlju `<numeric>`. Od C++17 standardna biblioteka nudi i funkcionalno jednaku funkciju za prefiksne sume [`std::inclusive_scan`](https://en.cppreference.com/w/cpp/algorithm/inclusive_scan), također definiranu u zaglavlju `<numeric>`.

### Dvodimenzionalne/višedimenzionalne prefiksne sume

Proširimo li jednodimenzionalne prefiksne sume na više dimenzija, dobivamo višedimenzionalne prefiksne sume. Postoje dvije uobičajene metode za njihovo računanje.

#### Pomoću formule uključivanja-isključivanja

Ova se metoda najčešće koristi za dvodimenzionalne prefiksne sume. Zadan je dvodimenzionalni niz $A$ veličine $m\times n$ i treba izračunati njegovu prefiksnu sumu $S$. Tada je $S$ također dvodimenzionalni niz veličine $m\times n$ i vrijedi

$$
S_{i,j} = \sum_{i'\le i}\sum_{j'\le j}A_{i',j'}.
$$

Analogno jednodimenzionalnom slučaju, $S_{i,j}$ bi se trebao moći izračunati iz $S_{i-1,j}$ ili $S_{i,j-1}$, čime izbjegavamo ponovno zbrajanje prethodnih članova. No ako jednostavno zbrojimo $S_{i-1,j}$ i $S_{i,j-1}$ te dodamo $A_{i,j}$, prefiksnu sumu preklapajućeg dijela $S_{i-1,j-1}$ brojimo dvaput, pa je taj dio treba još oduzeti. To je [formula uključivanja-isključivanja](../math/combinatorics/inclusion-exclusion-principle.md). Dobivamo sljedeću rekurzivnu relaciju:

$$
S_{i,j} = A_{i,j} + S_{i-1,j} + S_{i,j-1} - S_{i-1,j-1}. 
$$

U implementaciji je dovoljno izravno proći po svim $(i,j)$ i zbrajati.

???+ note "Primjer"
    Promotrimo konkretan primjer.
    
    ![Primjer dvodimenzionalne prefiksne sume](./images/prefix-sum-2d.svg)
    
    Ovdje je $S$ prefiksna suma matrice $A$. Po definiciji, $S_{3,3}$ je suma podmatrice u isprekidanom okviru na lijevoj slici. Nadalje, $S_{3,2}$ je suma plave podmatrice, $S_{2,3}$ suma crvene podmatrice, a suma njihova preklapanja je $S_{2,2}$. Vidimo da bismo izravnim zbrajanjem $S_{3,2}$ i $S_{2,3}$ dvaput brojili $S_{2,2}$, pa mora vrijediti
    
    $$
    S_{3,3} = A_{3,3} + S_{2,3} + S_{3,2} - S_{2,2} = 5 + 18 + 15 - 9 = 29.
    $$

Istim načelom, nakon što smo pretprocesirali dvodimenzionalne prefiksne sume, sumu podmatrice s gornjim lijevim kutom $(i_1,j_1)$ i donjim desnim kutom $(i_2,j_2)$ računamo kao

$$
S_{i_2,j_2} - S_{i_1-1,j_2} - S_{i_2,j_1-1} + S_{i_1-1,j_1-1}.
$$

To se može obaviti u vremenu $O(1)$.

U dvodimenzionalnom slučaju vremensku složenost gornjeg algoritma možemo jednostavno smatrati $O(mn)$, tj. linearnom u veličini zadanog niza. No kad dimenzija $k$ raste, broj članova u formuli uključivanja-isključivanja raste eksponencijalno, pa vremenska složenost postaje $O(2^kN)$, gdje je $k$ dimenzija niza, a $N$ veličina zadanog niza. Zato taj algoritam više nije prikladan.

???+ example "[Luogu P1387 Najveći kvadrat](https://www.luogu.com.cn/problem/P1387)"
    U matrici veličine $n\times m$ koja sadrži samo $0$ i $1$ pronađite najveći kvadrat koji ne sadrži $0$ i ispišite duljinu njegove stranice.

??? note "Referentni kod"
    === "C++"
        ```cpp
        --8<-- "docs/basic/code/prefix-sum/prefix-sum_2.cpp:full-text"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/basic/code/prefix-sum/prefix-sum_2.py:full-text"
        ```

#### Prefiksne sume dimenziju po dimenziju

U općem slučaju zadan je $k$-dimenzionalni niz $A$ veličine $N$ i također treba izračunati njegovu prefiksnu sumu $S$. Ovdje je

$$
S_{i_1,\cdots,i_k} = \sum_{i'_1\le i_1}\cdots\sum_{i'_k\le i_k} A_{i'_1,\cdots,i'_k}.
$$

Iz formule se vidi da je $k$-dimenzionalna prefiksna suma jednaka $k$ uzastopnih sumiranja. Zato je očit algoritam sljedeći: u svakom koraku promatramo samo jednu dimenziju, fiksiramo sve ostale i računamo niz jednodimenzionalnih prefiksnih suma; nakon što to napravimo za svih $k$ dimenzija, dobivamo $k$-dimenzionalnu prefiksnu sumu.

??? example "Referentna implementacija trodimenzionalne prefiksne sume"
    ```cpp
    --8<-- "docs/basic/code/prefix-sum/prefix-sum_4.cpp:core"
    ```

Budući da za svaku dimenziju prolazimo cijeli niz samo jednom, složenost je ovog algoritma $O(kN)$, što je obično prihvatljivo.

#### Poseban slučaj: DP po podskupovima (SOS)

Slučaj velike dimenzije često se pojavljuje u klasi problema zvanoj **suma po podskupovima** (sum over subsets, SOS). To je poseban slučaj višedimenzionalnih prefiksnih suma.

Problem glasi ovako. Promotrimo funkciju $f$ definiranu na svim podskupovima skupa veličine $n$; treba izračunati njezinu funkciju sume po podskupovima $g$, za koju vrijedi

$$
g(S) = \sum_{T\subseteq S}f(T).
$$

Dakle $g(S)$ jednako je sumi vrijednosti $f(T)$ po svim podskupovima $T\subseteq S$.

Najprije, problem sume po podskupovima može se zapisati kao višedimenzionalna prefiksna suma. Uočimo da se svaki podskup $S$ idejom bitmaske može prikazati kao 0-1 niz znakova $s$ duljine $n$, a podskup $T$ nizom $t$. Shvatimo li svaki bit niza znakova kao jednu dimenziju indeksa niza, $f$ je zapravo $n$-dimenzionalni niz u kojem je indeks svake dimenzije iz $\{0,1\}$. Ujedno, relacija sadržavanja podskupova ekvivalentna je odnosu veličine indeksa, tj.

$$
T\subseteq S \iff \forall i(t_i \le s_i). 
$$

Stoga je zbrajanje po podskupovima zapravo računanje prefiksne sume tog $n$-dimenzionalnog niza.

Sada možemo izravno primijeniti gore opisanu metodu prefiksnih suma dimenziju po dimenziju i dobiti sumu po podskupovima. Vremenska složenost je $O(n2^n)$.

??? example "Referentna implementacija"
    ```cpp
    --8<-- "docs/basic/code/prefix-sum/prefix-sum_5.cpp:core"
    ```

Inverzna operacija sume po podskupovima provodi se [formulom uključivanja-isključivanja](../math/combinatorics/inclusion-exclusion-principle.md). Problem sume po podskupovima također je jedan od nužnih koraka brze Möbiusove transformacije.

### Prefiksne sume na stablu

Jednodimenzionalne prefiksne sume mogu se poopćiti i na korijensko stablo (s korijenom $1$). Pretprocesiranjem prefiksnih suma možemo brzo izračunati sumu težina na putu u stablu.

#### Težine u čvorovima

Najprije razmotrimo slučaj kad su težine pohranjene u čvorovima. Neka čvor $x$ ima težinu $a_x$. Rekurzivnom relacijom

$$
S_1 = a_1,~ S_{x} = S_{\operatorname{fa}(x)} + a_x
$$

dobivamo sumu težina čvorova na putu od korijena do čvora $x$, gdje $\operatorname{fa}(x)$ označava roditelja čvora $x$. Nakon pretprocesiranja prefiksnih suma, sumu težina čvorova na putu koji spaja čvorove $x$ i $y$ računamo kao

$$
S_x + S_y - S_{\operatorname{lca}(x, y)} - S_{\operatorname{fa}(\operatorname{lca}(x, y))}.
$$

Ovdje $\operatorname{lca}(x, y)$ označava [najnižeg zajedničkog pretka](../graph/lca.md) (LCA) čvorova $x$ i $y$.

#### Težine na bridovima

Slučaj kad su težine pohranjene na bridovima gotovo se može svesti na slučaj težina u čvorovima. Za svaki čvor $x\neq 1$ koji nije korijen neka $\operatorname{edge}(x)$ označava brid koji spaja čvor $x$ s njegovim roditeljem $\operatorname{fa}(x)$. Tada možemo pretpostaviti da je težina brida pohranjena u čvoru udaljenijem od korijena. Drugim riječima, u čvoru $x$ pohranjena je težina brida $\operatorname{edge}(x)$. U korijenu je pohranjena težina $0$. Tada istom rekurzivnom relacijom iz prethodnog odjeljka možemo pretprocesirati sumu $S_x$ težina svih bridova na putu od korijena do čvora $x$.

Sumu težina bridova na putu koji spaja čvorove $x$ i $y$ tada dobivamo upitom

$$
S_x + S_y - 2S_{\operatorname{lca}(x, y)}.
$$

Uočimo razliku prema slučaju težina u čvorovima: tražena suma ne uključuje težinu pohranjenu u $\operatorname{lca}(x, y)$, jer brid čiju težinu on čuva nije na traženom putu.

#### Suma po podstablu

Za razliku od nizova, stablo nije simetrično s obzirom na početak i kraj, pa „prefiksna suma” računana odozdo prema gore (od listova prema korijenu) i odozgo prema dolje (od korijena prema listovima) ne daje isti rezultat. Pod „prefiksnom sumom na stablu” obično se podrazumijeva prefiksna suma računana odozgo prema dolje. Radi lakšeg izlaganja, „prefiksnu sumu” računanu odozdo prema gore u ovom članku zovemo **suma po podstablu**.

Suma težina čvorova u podstablu s korijenom $x$, tj. odgovarajuća suma po podstablu, jest

$$
T_x = \sum_{y\in\operatorname{desc}(x)} a_y.
$$

Ovdje $\operatorname{desc}(x)$ označava skup svih potomaka čvora $x$ (uključujući njega samog).

Za razliku od prefiksnih suma na stablu, suma po podstablu ne može se iskoristiti za računanje sume težina na putu u $O(1)$, ali pomaže u razumijevanju razlika na stablu iz nastavka.

## Razlike

Razlike (difference array) strategija su suprotna prefiksnim sumama: to je inverzna operacija prefiksne sume. Umjesto da za zadani niz tražimo njegov niz razlika, na natjecanjima je češća situacija da održavanjem niza razlika ostvarujemo više izmjena na intervalima. Nakon što izmjene intervala završe, prefiksnom sumom možemo vratiti izvorni niz i odgovarati na upite o njemu. Pazite: sve izmjene moraju doći prije upita.

Ako treba podržati miješane izmjene i upite više puta, treba koristiti [Fenwick tree](../ds/fenwick.md), no ideja je ista.

### Jednodimenzionalne razlike

Niz razlika $\{D_i\}$ niza $\{a_i\}$ definiran je kao

$$
D_i = a_i - a_{i-1},~ a_0 = 0.
$$

Standardna biblioteka C++-a implementira funkciju razlika [`std::adjacent_difference`](https://en.cppreference.com/w/cpp/algorithm/adjacent_difference), definiranu u zaglavlju `<numeric>`.

Odnos prefiksnih suma i razlika je sljedeći:

???+ note "Svojstvo"
    Neka je $\{D_i\}$ niz razlika niza $\{a_i\}$. Tada vrijedi:
    
    -   niz $\{a_i\}$ je prefiksna suma niza $\{D_i\}$, tj.
    
        $$
        a_i = \sum_{j=1}^i D_j.
        $$
    -   prefiksna suma niza $\{a_i\}$ jest
    
        $$
        S_i = \sum_{j=1}^i\sum_{k=1}^jD_k = \sum_{j=1}^i(i-j+1)D_j. 
        $$

Niz razlika često se koristi kad više puta treba dodati broj svim članovima nekog intervala niza, a zatim jednom ili više puta pitati za vrijednost nekog člana niza.

Pretpostavimo da svakom broju niza $\{a_i\}$ na intervalu $[l,r]$ treba dodati $v$. Na njegovu nizu razlika $\{D_i\}$ možemo napraviti sljedeće:

$$
D_{l} \gets D_{l} + v,~ D_{r+1}\gets D_{r+1} - v.
$$

Nakon što sve izmjene završe, prefiksnom sumom možemo vratiti ažurirane vrijednosti $\{a_i\}$. Jedna izmjena je $O(1)$. Za upite treba jednom izračunati prefiksnu sumu u $O(n)$, a zatim je svaki upit $O(1)$.

???+ example "Referentni kod"
    ```cpp
    --8<-- "docs/basic/code/prefix-sum/prefix-sum_6.cpp:core"
    ```

### Dvodimenzionalne/višedimenzionalne razlike

Razlike se također mogu poopćiti na više dimenzija. Shvatimo li višedimenzionalne razlike kao inverznu operaciju višedimenzionalnih prefiksnih suma, računanje višedimenzionalnog niza razlika odgovara računanju izvornog niza iz višedimenzionalne prefiksne sume. Prema prethodnom razmatranju možemo iskoristiti formulu uključivanja-isključivanja. Npr. dvodimenzionalne razlike definirane su kao

$$
D_{i,j} = a_{i,j} - a_{i-1,j} - a_{i,j-1} + a_{i-1,j-1}.
$$

No ako treba izračunati cijeli niz razlika, jednostavniji i učinkovitiji način su razlike dimenziju po dimenziju: prolazimo sve dimenzije i duž svake izračunamo razlike niza.

Dvodimenzionalne razlike često se koriste kad se u dvodimenzionalnom nizu više puta dodaje vrijednost cijelom pravokutniku. Npr. da bismo svakom broju u matrici s gornjim lijevim kutom $(x_1,y_1)$ i donjim desnim kutom $(x_2,y_2)$ dodali $v$, na njezinu nizu razlika $\{D_{i,j}\}$ napravimo sljedeće:

$$
\begin{aligned}
D_{x_1,y_1} &\gets D_{x_1,y_1} + v, \\
D_{x_1,y_2+1} &\gets D_{x_1,y_2+1} - v,\\
D_{x_2+1,y_1} &\gets D_{x_2+1,y_1} - v,\\
D_{x_2+1,y_2+1} &\gets D_{x_2+1,y_2+1} + v.
\end{aligned}
$$

Nakon što sve izmjene završe, dovoljno je jednom izračunati dvodimenzionalnu prefiksnu sumu da bismo brzo dobivali vrijednosti ažuriranog niza.

??? example "Referentni kod"
    ```cpp
    --8<-- "docs/basic/code/prefix-sum/prefix-sum_7.cpp:core"
    ```

Naravno, slična ideja vrijedi i za dimenzije $k>2$, ali jedna izmjena tada zahtijeva vrijeme $O(2^k)$, što s rastom $k$ prestaje biti praktično.

### Razlike na stablu

Razlike se mogu poopćiti na korijensko stablo i tako ostvariti dodavanje na cijelom putu u stablu. Ovisno o tome čuvaju li se podaci u čvorovima ili na bridovima, razlike na stablu dijelimo na **razlike po čvorovima** i **razlike po bridovima**, koje se u implementaciji malo razlikuju. Osim toga, umjesto prefiksnih suma na stablu, češće se nakon svih izmjena računa suma po podstablu, a zatim se odgovara na upite. Upravo taj slučaj razmatramo u ovom odjeljku.

#### Razlike po čvorovima

Ako svim težinama čvorova na putu između čvorova $x$ i $y$ treba dodati $v$, na nizu razlika $\{D_x\}$ napravimo sljedeće:

$$
\begin{aligned}
D_x &\gets D_x + v, \\
D_{\operatorname{lca}(x, y)} &\gets D_{\operatorname{lca}(x, y)} - v,\\
D_y &\gets D_y + v, \\
D_{\operatorname{fa}(\operatorname{lca}(x, y))} &\gets D_{\operatorname{fa}(\operatorname{lca}(x, y))} - v.
\end{aligned}
$$

Nakon što sve izmjene završe, jednim računanjem sume po podstablu dobivamo ažurirane težine čvorova.

???+ example "Primjer"
    Pri dodavanju na težine čvorova na putu između čvorova $S$ i $T$, prve dvije formule gore odgovaraju jednodimenzionalnoj operaciji razlika na putu u plavom okviru, a druge dvije jednodimenzionalnoj operaciji razlika na putu u crvenom okviru:
    
    ![](./images/prefix-sum1.svg)
    
    Zbrajanje odozdo prema gore odgovara računanju prefiksnih suma tih dvaju intervala odozdo prema gore. Usporedbom s gore opisanom jednodimenzionalnom operacijom razlika vidi se ispravnost razlika po čvorovima.

#### Razlike po bridovima

Ako svim težinama bridova na putu između čvorova $x$ i $y$ treba dodati $v$, na nizu razlika $\{D_x\}$ napravimo sljedeće:

$$
\begin{aligned}
D_x &\gets D_x + v, \\
D_y &\gets D_y + v, \\
D_{\operatorname{lca}(x, y)} &\gets D_{\operatorname{lca}(x, y)} - 2v.
\end{aligned}
$$

Nakon što sve izmjene završe, jednim računanjem sume po podstablu dobivamo ažurirane težine bridova (pohranjene u djetetu odgovarajućeg brida).

???+ example "Primjer"
    Kao na slici, razlike po bridovima mogu riješiti problem dodavanja na težine bridova na crvenom putu.
    
    ![](./images/prefix-sum2.svg)
    
    Budući da je razlike teško voditi izravno na bridovima, vrijednosti koje bi se trebale zbrajati na crvenim bridovima pomičemo prema dolje u susjedne čvorove, čime operacije postaju jednostavne. Usporedbom s formulama za razlike po čvorovima razumijemo formule za razlike po bridovima.

### Primjer zadatka

???+ example "[USACO15DEC Max Flow](https://usaco.org/index.php?page=viewproblem2&cpid=576)"
    FJ je između $N(2 \le N \le 50,000)$ pregrada u svojoj staji postavio $N-1$ cijev. Sve su pregrade povezane cijevima.
    
    FJ ima $K(1 \le K \le 100,000)$ ruta za prijevoz mlijeka; $i$-ta ruta prevozi mlijeko iz pregrade $s_i$ u pregradu $t_i$. Jedna ruta donosi jednu jedinicu pritiska objema krajnjim pregradama i svim pregradama kroz koje prolazi. Izračunajte pritisak u pregradi s najvećim pritiskom.

??? note "Ideja rješenja"
    Treba izbrojiti koliko puta je svaki čvor posjećen, pa razlikama na stablu svim čvorovima na putu svake rute dodamo jedan i brzo dobijemo broj posjeta svakog čvora. Ovdje LCA računamo binarnim podizanjem (binary lifting), a na kraju DFS-om prolazimo cijelo stablo i pri povratku zbrajamo niz razlika, čime dobivamo odgovor.

??? note "Referentni kod"
    ```cpp
    --8<-- "docs/basic/code/prefix-sum/prefix-sum_3.cpp"
    ```

## Zadaci za vježbu

Prefiksne sume:

-   [Luogu B3612 Suma intervala](https://www.luogu.com.cn/problem/B3612)
-   [Luogu U69096 Inverz prefiksne sume](https://www.luogu.com.cn/problem/U69096)
-   [AtCoder joi2007ho\_a Najveća suma](https://atcoder.jp/contests/joi2007ho/tasks/joi2007ho_a)
-   [USACO16JAN Subsequences Summing to Sevens](https://usaco.org/index.php?page=viewproblem2&cpid=595)
-   [USACO05JAN Moo Volume S](https://www.luogu.com.cn/problem/P6067)

Dvodimenzionalne/višedimenzionalne prefiksne sume:

-   [HDU 6514 Monitor](https://acm.hdu.edu.cn/showproblem.php?pid=6514)
-   [Luogu P1387 Najveći kvadrat](https://www.luogu.com.cn/problem/P1387)
-   [HNOI2003 Laserska bomba](https://www.luogu.com.cn/problem/P2280)
-   [CF 165E Compatible Numbers](https://codeforces.com/contest/165/problem/E)
-   [CF 383E Vowels](https://codeforces.com/problemset/problem/383/E)
-   [ARC 100C Or Plus Max](https://atcoder.jp/contests/arc100/tasks/arc100_c)

Prefiksne sume na stablu:

-   [LOJ 10134. Dis](https://loj.ac/problem/10134)
-   [LOJ 2491. Suma](https://loj.ac/problem/2491)

Razlike:

-   [Fenwick tree 3: izmjena intervala, upit na intervalu](https://loj.ac/problem/132)
-   [Poetize6 IncDec Sequence](https://www.luogu.com.cn/problem/P4552)
-   [Luogu P4231 Tri koraka do pobjede](https://www.luogu.com.cn/problem/P4231)

Dvodimenzionalne/višedimenzionalne razlike:

-   [Luogu P3397 Tepisi](https://www.luogu.com.cn/problem/P3397)
-   [Luogu P8228 Wdoi-5 Modularni nuklearni reaktor](https://www.luogu.com.cn/problem/P8228)

Razlike na stablu:

-   [USACO15DEC Max Flow](https://usaco.org/index.php?page=viewproblem2&cpid=576)
-   [JLOI2014 Vjeveričin novi dom](https://loj.ac/problem/2236)
-   [NOIP2015 Plan prijevoza](http://uoj.ac/problem/150)
-   [NOIP2016 Svaki dan volim trčati](http://uoj.ac/problem/261)
