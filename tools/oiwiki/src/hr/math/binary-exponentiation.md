---
title: Brzo potenciranje
---

## Uvod

**Brzo potenciranje** (fast exponentiation), poznato i kao **binarno potenciranje** (binary exponentiation) ili **potenciranje kvadriranjem** (exponentiation by squaring), mali je trik kojim se $a^n$ računa u vremenu $\Theta(\log n)$, dok naivno računanje zahtijeva vrijeme $\Theta(n)$.

Trik se može primijeniti u svakoj situaciji u kojoj je množenje za $a$ asocijativno, npr. pri potenciranju u modularnoj aritmetici, potenciranju matrica itd.; pojedinosti vidi u odjeljku [Primjene](#primjene) u nastavku.

## Postupak

Računanje $n$-te potencije broja $a$ znači množenje $n$ kopija broja $a$: $a^{n} = \underbrace{a \times a \cdots \times a}_{n\text{ faktora a}}$. Međutim, kad je $n$ prevelik ili je jedno množenje preskupo, taj način nije prikladan. Ideja binarnog potenciranja jest razbiti zadatak potenciranja na manje zadatke prema **binarnom zapisu** eksponenta.

???+ example "Primjer"
    Pretpostavimo da treba izračunati $3^{13}$. Ako to raspišemo kao umnožak, treba $13-1=12$ množenja. Međutim, budući da je
    
    $$
    3^{13} = 3^{(1101)_2} = 3^8 \times 3^4 \times 3^1,
    $$
    
    dovoljno je brzo izračunati $3^{1},3^{2},3^{4},3^{8}$ pa vrijednost $3^{13}$ dobivamo s $2$ množenja. Dakle, treba samo znati brz način za računanje gornjeg niza potencija broja $3$ s eksponentima $2^k$. To je lako, jer je svaki element niza (osim prvog) kvadrat prethodnog.
    
    Iz te analize dobivamo sljedeći postupak računanja $3^{13}$:
    
    $$
    \begin{aligned}
    3^1 &= 3, \\
    3^2 &= \left(3^1\right)^2 = 3^2 = 9, \\
    3^4 &= \left(3^2\right)^2 = 9^2 = 81, \\
    3^8 &= \left(3^4\right)^2 = 81^2 = 6561, \\
    3^{13} &= 6561 \times 81 \times 3 = 1594323.
    \end{aligned}
    $$
    
    U postupku je izvedeno samo $5$ množenja.

To je osnovna ideja brzog potenciranja. Što se tiče konkretne implementacije, postoje dvije uobičajene inačice.

### Iterativna inačica

Neka je binarni zapis broja $n$ jednak $(n_tn_{t-1}\cdots n_1n_0)_2$, tj. vrijedi

$$
n = n_t2^t + n_{t-1}2^{t-1} + \cdots + n_12^1 + n_02^0,
$$

gdje je $n_i\in\{0,1\}$. Tada je

$$
\begin{aligned}
a^n & = a^{n_t2^t + n_{t-1}2^{t-1} + \cdots + n_12^1 + n_02^0}\\
& = a^{n_0 2^0} \times a^{n_1 2^1}\times \cdots \times a^{n_{t-1}2^{t-1}} \times a^{n_t2^t}.
\end{aligned}
$$

Uočimo da se u računanju umnoška zapravo pojavljuju samo članovi s $n_i=1$.

Prema tom izrazu možemo najprije u vremenu $\Theta(\log n)$ izračunati vrijednosti $\Theta(\log n)$ potencija broja $a$ s eksponentima $2^k$, a zatim u vremenu $\Theta(\log n)$ odabrati potencije koje odgovaraju bitovima jednakim $1$ i pomnožiti ih u konačni rezultat. To je iterativna implementacija brzog potenciranja.

Pseudokod je sljedeći:

$$
\begin{array}{l}
\textbf{Algorithm }\text{FastPow}(a, n): \\
\textbf{Input. }\text{Base }a\text{ and exponent }n.\\
\textbf{Output. }\text{Power }a^n.\\
\textbf{Method.}\\
\begin{array}{ll}
1 & \textit{result}\gets\mathrm{Id}\\
2 & \textbf{while }n > 0\textbf{ do}\\
3 & \qquad \textbf{if }n \bmod 2 = 1\textbf{ then}\\
4 & \qquad \qquad \textit{result} \gets \textit{result}\cdot a\\
5 & \qquad \textbf{end if}\\
6 & \qquad a \gets a \cdot a\\
7 & \qquad n \gets n / 2\\
8 & \textbf{end while}\\
9 & \textbf{return }\textit{result}
\end{array}
\end{array}
$$

Računanje brzog potenciranja tom metodom zahtijeva $\Theta(\log n)$ množenja.

### Rekurzivna inačica

Taj se postupak može implementirati i rekurzivno. Uočimo da se binarni razvoj eksponenta $n$ može rekurzivno zapisati kao

$$
(n_tn_{t-1}\cdots n_1n_0)_2 = 2 \times (n_tn_{t-1}\cdots n_1)_2 + n_0.
$$

Stoga se potencija $a^n$ može rekurzivno računati kao

$$
a^n = \begin{cases}
1, & n = 0,\\
(a^{\lfloor n/2\rfloor})^2, & n > 0 \text{ and }n\text{ is even},\\
(a^{\lfloor n/2\rfloor})^2\cdot a, & n > 0 \text{ and }n\text{ is odd}.\\
\end{cases}
$$

To je rekurzivna implementacija brzog potenciranja.

Pseudokod je sljedeći:

$$
\begin{array}{l}
\textbf{Algorithm }\text{FastPow}(a, n): \\
\textbf{Input. }\text{Base }a\text{ and exponent }n.\\
\textbf{Output. }\text{Power }a^n.\\
\textbf{Method.}\\
\begin{array}{ll}
1 & \textbf{if }n = 0\textbf{ then}\\
2 & \qquad \textbf{return }\mathrm{Id}\\
3 & \textbf{end if}\\
4 & \textit{result} \gets \text{FastPow}(a, n / 2) \\
5 & \textbf{if }n\bmod 2 = 0\textbf{ then}\\
6 & \qquad \textbf{return }\textit{result}\cdot\textit{result}\\
7 & \textbf{else}\\
8 & \qquad \textbf{return }\textit{result}\cdot\textit{result}\cdot a\\
9 & \textbf{end if}
\end{array}
\end{array}
$$

Računanje brzog potenciranja tom metodom zahtijeva $\Theta(\log n)$ rekurzivnih poziva i također $\Theta(\log n)$ množenja. Iako je složenost ista, zbog određenog troška same rekurzije iterativna je inačica u praksi brža.

## Primjene

### Modularno potenciranje

???+ example "[Luogu P1226【模板】快速幂 (Predložak: brzo potenciranje)](https://www.luogu.com.cn/problem/P1226)"
    Zadana su tri cijela broja $a,b,p$; izračunajte $a^b\bmod p$, pri čemu je $p\ge 2$.

Ovo je vrlo česta primjena; npr. može se koristiti za računanje multiplikativnog inverza u modularnoj aritmetici. Budući da znamo da uzimanje ostatka ne smeta množenju, dovoljno je uzimati ostatak tijekom računanja.

Najprije možemo izravno implementirati gornju rekurzivnu metodu:

???+ note "Referentna implementacija"
    === "C++"
        ```cpp
        --8<-- "docs/math/code/binary-exponentiation/luogu-P1226-1.cpp:core"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/math/code/binary-exponentiation/luogu-P1226-1.py:core"
        ```

Druga je implementacija nerekurzivna. Tijekom petlje potencije koje odgovaraju bitovima jednakim 1 množi u odgovor. Iako je teorijska složenost obiju implementacija ista, druga je u praksi brža od prve jer rekurzija ima određeni trošak.

???+ note "Referentna implementacija"
    === "C++"
        ```cpp
        --8<-- "docs/math/code/binary-exponentiation/luogu-P1226-2.cpp:core"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/math/code/binary-exponentiation/luogu-P1226-2.py:core"
        ```

???+ warning "Napomena"
    -   Modul je u pravilu veći od $1$. U vrlo posebnim slučajevima modul $p$ može biti jednak $1$; tada treba posebno razmotriti slučaj $b=0$.
    -   Kad je eksponent vrlo velik, treba ga smanjiti pomoću [proširenog Eulerova teorema](./number-theory/fermat.md#prošireni-eulerov-teorem) pa tek onda računati.

### Računanje Fibonaccijevih brojeva

Prema rekurziji Fibonaccijeva niza $F_n = F_{n-1} + F_{n-2}$ možemo sastaviti matricu $2\times 2$ koja opisuje prijelaz iz $F_i,F_{i+1}$ u $F_{i+1},F_{i+2}$. Pri računanju $n$-te potencije te matrice primjenjujemo ideju brzog potenciranja i rezultat dobivamo u vremenu $\Theta(\log n)$. Više pojedinosti vidi u [Fibonaccijev niz](./combinatorics/fibonacci.md), a implementaciju brzog potenciranja matrica u [Ubrzavanje rekurzija matricama](../math/linear-algebra/matrix.md#矩阵加速递推).

### Višestruka primjena permutacije

???+ note "Opis problema"
    Zadan je niz duljine $n$ i permutacija; primijenite tu permutaciju na niz $k$ puta.

Dovoljno je permutaciju potencirati na $k$-tu potenciju i zatim je primijeniti na niz. Vremenska složenost je $O(n \log k)$. Više pojedinosti vidi u [Kompozicija permutacija](./permutation.md#kompozicija).

???+ warning "Napomena"
    Ako od permutacije izgradimo graf i na svakom ciklusu zasebno izračunamo $k$-tu potenciju (što je zapravo ekvivalentno uzimanju $k$ modulo duljina ciklusa), problem se može riješiti u vremenskoj složenosti $O(n)$.

### Ubrzavanje operacija nad skupom točaka u geometriji

???+ example "[HDU 4087 A Letter to Programmers](https://acm.hdu.edu.cn/showproblem.php?pid=4087)"
    Zadano je $n$ točaka $p_i$ u trodimenzionalnom prostoru; na te točke treba primijeniti svih $m$ operacija. Postoje 3 vrste operacija:
    
    1.  pomak točke duž nekog vektora (Shift),
    2.  skaliranje koordinata točke zadanim faktorom (Scale),
    3.  rotacija oko nekog pravca (Rotate).
    
    Postoji i posebna operacija koja neki niz operacija ponavlja $k$ puta (Repeat); operacije Repeat mogu biti ugniježđene. Ispišite koordinate svake točke nakon završetka svih operacija.

Prema sadržaju stranice [Vektori i matrice](./linear-algebra/vector.md#向量与矩阵), svaka se operacija može prikazati matricom transformacije, a niz uzastopnih transformacija umnoškom matrica. Jedna operacija Repeat odgovara $k$-toj potenciji matrice. Tako u vremenu $O(m \log k)$ možemo izračunati matricu koju na kraju tvori cijeli niz transformacija. Na kraju je primijenimo na $n$ točaka; ukupna složenost je $O(n + m \log k)$.

### Prebrojavanje puteva fiksne duljine

???+ note "Opis problema"
    Zadan je usmjereni graf (težine bridova su 1); za svaki par vrhova $u,v$ odredite broj puteva duljine $k$ od $u$ do $v$.

Matricu susjedstva $M$ tog grafa potenciramo na $k$-tu potenciju; tada $M_{i,j}$ predstavlja broj puteva duljine $k$ od $i$ do $j$. Složenost tog algoritma je $O(n^3 \log k)$. Pojedinosti o algoritmu vidi na stranici [Matrice](./linear-algebra/matrix.md#定长路径统计).

### Modularno množenje cijelih brojeva

???+ note "Opis problema"
    Zadani su nenegativni cijeli brojevi $a,b$ i pozitivan cijeli broj $m$; izračunajte $a\times b\bmod m$, pri čemu je $a,b\le m\le 10^{18}$.

Istom idejom kao kod binarnog potenciranja, ovaj put jedan od faktora prikazujemo kao zbroj nekoliko cjelobrojnih potencija broja 2. Naime, množenje broja s 2 uz uzimanje ostatka možemo svesti na zbrajanje i oduzimanje te tako spriječiti prelijevanje cijelih brojeva. Tako problem rješavamo u vremenskoj složenosti $O (\log m)$. Rekurzivna metoda je sljedeća:

$$
a \cdot b = \begin{cases}
0 &\text{if }a = 0 \\
2 \cdot \frac{a}{2} \cdot b &\text{if }a > 0 \text{ and }a \text{ even} \\
2 \cdot \frac{a-1}{2} \cdot b + b &\text{if }a > 0 \text{ and }a \text{ odd}
\end{cases}
$$

No u praksi ta metoda zbog veće računske složenosti nije vremenski učinkovita. U stvarnom programiranju za množenje s modulom u rasponu `long long` obično se koristi [brzo množenje](./number-theory/mod-arithmetic.md#brzo-množenje).

### Brzo potenciranje velikih brojeva

Preduvjet: [Množenje velikih brojeva](./bignum.md#množenje)

???+ example "[Luogu P1045 \[NOIP 2003 普及组\] 麦森数 (Mersenneovi brojevi)](https://www.luogu.com.cn/problem/P1045)"
    Zadan je cijeli broj $P$ ($1000 < P < 3100000$); izračunajte broj znamenki broja $2^P−1$ i njegovih posljednjih $500$ znamenki (u dekadskom zapisu); ako ima manje od $500$ znamenki, dopunite ga nulama 0 na višim mjestima.

??? note "Implementacija"
    ```cpp
    --8<-- "docs/math/code/binary-exponentiation/luogu-P1045.cpp"
    ```

## Brzo potenciranje s fiksnom bazom i pretprocesiranjem

Kad je baza $a$ fiksna, možemo iskoristiti [ideju dekompozicije na blokove](../ds/decompose.md): nakon određenog vremena pretprocesiranja na upit o potenciji odgovaramo u vremenu $O(1)$. Taj se algoritam često naziva i „svjetlosno brzim potenciranjem” (光速幂). Postupak je sljedeći:

1.  Odaberemo broj $s$, pretprocesiranjem izračunamo vrijednosti $a^0,a^1,\cdots,a^{s-1}$ i $a^0,a^s,\cdots,a^{\lfloor p/s\rfloor s}$ te ih pohranimo u dva niza;
2.  Za svaki upit $a^b$ rastavimo $b$ na $\lfloor b/s\rfloor s+(b\bmod s)$; tada je $a^b=a^{\lfloor b/s\rfloor s}\cdot a^{b\bmod s}$, pa odgovor dobivamo u $O(1)$.

Pretpostavimo da je raspon eksponenta $b$ jednak $[0,n]$; tada se za duljinu bloka $s$ često bira $\sqrt{n}$ ili njemu bliska potencija broja $2$. Izbor $\sqrt{n}$ daje optimalnu složenost pretprocesiranja $O(\sqrt{n})$, a izbor potencije broja $2$ omogućuje pojednostavljenje računanja bitovnim operacijama.

Posebno, pri računanju potencija u modularnoj aritmetici jednaka baza $a$ implicitno zahtijeva i jednak modul $m$. Zbog [proširenog Eulerova teorema](./number-theory/fermat.md#prošireni-eulerov-teorem), za proizvoljan modul $m$ gornja granica raspona eksponenata koje treba pretprocesirati jest $n = 2\varphi(m)$; za prost modul $p$ gornja granica jest $n = p - 1$. U oba je slučaja složenost pretprocesiranja $O(\sqrt{m})$.

???+ example "Referentni kod"
    ```cpp
    --8<-- "docs/math/code/binary-exponentiation/pre-exp.cpp:core"
    ```

## Zadaci za vježbu

-   [UVa 1230 - MODEX](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=3671)
-   [UVa 374 - Big Mod](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=310)
-   [UVa 11029 - Leading and Trailing](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1970)
-   [Codeforces - Parking Lot](http://codeforces.com/problemset/problem/630/I)
-   [SPOJ - The last digit](http://www.spoj.com/problems/LASTDIG/)
-   [SPOJ - Locker](http://www.spoj.com/problems/LOCKER/)
-   [SPOJ - Just add it](http://www.spoj.com/problems/ZSUM/)

**Dio ove stranice preveden je iz članka [Бинарное возведение в степень](http://e-maxx.ru/algo/binary_pow) i njegova engleskog prijevoda [Binary Exponentiation](https://cp-algorithms.com/algebra/binary-exp.html). Ruska je inačica objavljena pod licencijom Public Domain + Leave a Link, a engleska pod CC-BY-SA 4.0.**
