---
title: Interpolacija
---

## Uvod

Interpolacija je metoda kojom se iz poznatih, diskretnih podatkovnih točaka procjenjuju nove podatkovne točke unutar određenog raspona. Interpolacija se često koristi pri prilagodbi (fitting) funkcija.

Na primjer, za podatkovne točke:

| $x$    | $0$ | $1$      | $2$      | $3$      | $4$       | $5$       | $6$       |
| ------ | --- | -------- | -------- | -------- | --------- | --------- | --------- |
| $f(x)$ | $0$ | $0.8415$ | $0.9093$ | $0.1411$ | $-0.7568$ | $-0.9589$ | $-0.2794$ |

![](../images/interp-1.svg)

gdje je $f(x)$ nepoznata, interpolacijom se nepoznate podatkovne točke mogu procijeniti tako da se $f(x)$ prilagodi u nekom zadanom obliku.

Na primjer, $f(x)$ možemo prilagoditi po dijelovima linearnom funkcijom:

![](../images/interp-2.svg)

Takav se način interpolacije naziva [linearna interpolacija](https://en.wikipedia.org/wiki/Linear_interpolation).

Također možemo $f(x)$ prilagoditi polinomom:

![](../images/interp-3.svg)

Takav se način interpolacije naziva [polinomna interpolacija](https://en.wikipedia.org/wiki/Polynomial_interpolation).

Opći oblik polinomne interpolacije glasi:

???+ note "Polinomna interpolacija"
    Za poznatih $n+1$ točaka $(x_0,y_0),(x_1,y_1),\dots,(x_n,y_n)$ pronaći polinom oblika $f(x)=\sum_{i=0}^n a_ix^i$ koji zadovoljava
    
    $$
    f(x_i)=y_i,\qquad\forall i=0,1,\dots,n
    $$
    
    to jest, traženi polinom $f(x)$.

U nastavku predstavljamo dva načina polinomne interpolacije: Lagrangeovu interpolaciju i Newtonovu interpolaciju. Nije teško dokazati da obje metode daju jednake rezultate.

## Lagrangeova interpolacija

Treba konstruirati funkciju $f(x)$ koja prolazi točkama $P_1(x_1, y_1), P_2(x_2,y_2),\cdots,P_n(x_n,y_n)$. Najprije neka je projekcija $i$-te točke na os $x$ točka $P_i^{\prime}(x_i,0)$.

Razmotrimo konstrukciju $n$ funkcija $f_1(x), f_2(x), \cdots, f_n(x)$ takvih da graf $i$-te funkcije $f_i(x)$ prolazi točkama $\begin{cases}P_j^{\prime}(x_j,0),(j\neq i)\\P_i(x_i,y_i)\end{cases}$; tada je tražena funkcija $f(x)=\sum\limits_{i=1}^nf_i(x)$.

Možemo staviti $f_i(x)=a\cdot\prod_{j\neq i}(x-x_j)$; uvrštavanjem točke $P_i(x_i,y_i)$ dobivamo $a=\dfrac{y_i}{\prod_{j\neq i} (x_i-x_j)}$, pa je

$$
f_i(x)=y_i\cdot\dfrac{\prod_{j\neq i} (x-x_j)}{\prod_{j\neq i} (x_i-x_j)}=y_i\cdot\prod_{j\neq i}\dfrac{x-x_j}{x_i-x_j}
$$

Tako dobivamo oblik Lagrangeove interpolacije:

$$
f(x)=\sum_{i=1}^ny_i\cdot\prod_{j\neq i}\dfrac{x-x_j}{x_i-x_j}
$$

Vremenska složenost naivne implementacije je $O(n^2)$, a može se optimizirati na $O(n\log^2 n)$; vidi [brzu interpolaciju polinoma](../poly/multipoint-eval-interpolation.md#brza-interpolacija-polinoma).

???+ note "[Luogu P4781【模板】拉格朗日插值 (Predložak: Lagrangeova interpolacija)](https://www.luogu.com.cn/problem/P4781)"
    Zadano je $n$ parova točaka $(x_i,y_i)$ i $k$, pri čemu $\forall i,j$ vrijedi $i\neq j \iff x_i\neq x_j$, te $f(x_i)\equiv y_i\pmod{998244353}$ i $\deg(f(x)) < n$ (definiramo $\deg(0)=-\infty$). Izračunajte $f(k)\bmod{998244353}$.
    
    ??? note "Rješenje"
        U ovom zadatku treba izračunati samo vrijednost $f(k)$, pa pri računanju gornjeg izraza možemo izravno uvrstiti $k$; ponekad je pak potrebno više puta računati vrijednosti ili provoditi složenije operacije, i tada treba odrediti koeficijente polinoma $f$. Kôd daje jednu implementaciju koja računa koeficijente.
        
        $$
        f(k)=\sum_{i=1}^{n}y_i\prod_{j\neq i }\frac{k-x_j}{x_i-x_j}
        $$
        
        U ovom zadatku treba računati i inverze. Ako najprije zasebno izračunamo brojnik i nazivnik, a zatim brojnik pomnožimo inverzom nazivnika i pribrojimo konačnom odgovoru, usko grlo vremenske složenosti neće biti računanje inverza, pa je vremenska složenost $O(n^2)$.
        
        Budući da računamo uz fiksni modul $998244353$, vremensku složenost računanja multiplikativnog inverza ovdje privremeno smatramo konstantnom.
    
    ??? note "Implementacija"
        ```cpp
        --8<-- "docs/math/code/numerical/interp/interp_1.cpp"
        ```

### Lagrangeova interpolacija kad su apscise uzastopni cijeli brojevi

Ako su apscise poznatih točaka uzastopni cijeli brojevi, interpolaciju možemo provesti u $O(n)$.

Neka je traženi polinom $f(x)$ i neka su poznati $f(1),\cdots,f(n+1)$ ($1\le i\le n+1$); uvrstimo ih u gornju interpolacijsku formulu:

$$
\begin{aligned}
f(x)&=\sum\limits_{i=1}^{n+1}y_i\prod\limits_{j\ne i}\frac{x-x_j}{x_i-x_j}\\
&=\sum\limits_{i=1}^{n+1}y_i\prod\limits_{j\ne i}\frac{x-j}{i-j}
\end{aligned}
$$

U produktu na kraju brojnik i nazivnik možemo promatrati zasebno; lako se dobiva da je brojnik:

$$
\dfrac{\prod\limits_{j=1}^{n+1}(x-j)}{x-i}
$$

Produkt $i-j$ u nazivniku može se rastaviti na dva faktorijela:

$$
(-1)^{n+1-i}\cdot(i-1)!\cdot(n+1-i)!
$$

Tako dobivamo interpolacijsku formulu za apscise $1,\cdots,n+1$:

$$
f(x)=\sum\limits_{i=1}^{n+1}(-1)^{n+1-i}y_i\cdot\frac{\prod\limits_{j=1}^{n+1}(x-j)}{(i-1)!(n+1-i)!(x-i)}
$$

Unaprijed izračunamo prefiksne i sufiksne produkte od $(x-i)$, faktorijele i inverze faktorijela, zatim uvrstimo u ovu formulu; složenost je $O(n)$.

???+ note "Primjer zadatka [CF622F The Sum of the k-th Powers](https://codeforces.com/contest/622/problem/F)"
    Zadani su $n,k$; izračunajte $\sum\limits_{i=1}^ni^k$ modulo $10^9+7$.
    
    ??? note "Rješenje"
        U ovom je zadatku odgovor polinom stupnja $k+1$, pa linearnim sitom možemo izračunati vrijednosti $1^i,\cdots,(k+2)^i$ i zatim provesti interpolaciju u $O(n)$.
        
        Može se, znanjem iz kombinatorike, iz formule metode razlika izvesti i sljedeći izraz:
        
        $$
        f(x)=\sum_{i=1}^{n+1}\binom{x-1}{i-1}\sum_{j=1}^{i}(-1)^{i+j}\binom{i-1}{j-1}y_{j}=\sum\limits_{i=1}^{n+1}y_i\cdot\frac{\prod\limits_{j=1}^{n+1}(x-j)}{(x-i)\cdot(-1)^{n+1-i}\cdot(i-1)!\cdot(n+1-i)!}
        $$
    
    ??? note "Implementacija"
        ```cpp
        --8<-- "docs/math/code/numerical/interp/interp_2.cpp"
        ```

## Newtonova interpolacija

Newtonova interpolacija metoda je interpolacije zasnovana na razlikama višeg reda; njezina je prednost što podržava dodavanje nove podatkovne točke u $O(n)$.

Da bismo ostvarili dodavanje nove podatkovne točke u $O(n)$, stavimo:

$$
f(x)=\sum_{j=0}^n a_jn_j(x)
$$

gdje se $n_j(x):=\prod_{i=0}^{j-1}(x-x_i)$ naziva **Newtonova baza** (Newton basis).

Ako riješimo $a_j$, dobivamo interpolacijski polinom $f(x)$. **Podijeljene razlike unaprijed** (forward divided differences) definiramo na sljedeći način:

$$
\begin{aligned}
    \lbrack y_k\rbrack  & := y_k,                                                                & k=0,\dots,n, \\
    [y_k,\dots,y_{k+j}] & := \dfrac{[y_{k+1},\dots,y_{k+j}]-[y_k,\dots,y_{k+j-1}]}{x_{k+j}-x_k}, & k=0,\dots,n-j,~j=1,\dots,n.
\end{aligned}
$$

Tada je:

$$
\begin{aligned}
    f(x)&=[y_0]+[y_0,y_1](x-x_0)+\dots+[y_0,\dots,y_n](x-x_0)\dots(x-x_{n-1})\\
    &=\sum_{j=0}^n [y_0,\dots,y_j]n_j(x)
\end{aligned}
$$

To je oblik Newtonove interpolacije. Vremenska složenost naivne implementacije je $O(n^2)$.

Ako su uzorkovane točke jednako razmaknute (tj. $x_i=x_0+ih$, $i=1,\dots,n$), možemo izvesti

$$
[y_k,\dots,y_{k+j}]=\frac{1}{j!h^j}\Delta^{(j)}y_k,
$$

gdje su $\Delta^{(j)}y_k$ **razlike unaprijed** (forward differences), definirane ovako:

$$
\begin{aligned}
    \Delta^{(0)}y_k & := y_k,                                       & k=0,\dots,n, \\
    \Delta^{(j)}y_k & := \Delta^{(j-1)} y_{k+1}-\Delta^{(j-1)} y_k, & k=0,\dots,n-j,~j=1,\dots,n.
\end{aligned}
$$

Stavimo li $x=x_0+sh$, formula Newtonove interpolacije postaje

$$
f(x)=\sum_{j=0}^n \binom{s}{j}j!h^j[y_0,\dots,y_j]=\sum_{j=0}^n \binom{s}{j}\Delta^{(j)}y_0.
$$

??? note "Implementacija ([Luogu P4781【模板】拉格朗日插值 (Predložak: Lagrangeova interpolacija)](https://www.luogu.com.cn/problem/P4781))"
    ```cpp
    --8<-- "docs/math/code/numerical/interp/interp_3.cpp"
    ```

### Newtonova interpolacija kad su apscise uzastopni cijeli brojevi

Na primjer: odredite koeficijente polinoma $f(x)=\sum_{i=0}^{3} a_ix^i$ ako su poznate vrijednosti $f(1)$ do $f(6)$, redom $1, 5, 14, 30, 55, 91$.

$$
\begin{array}{cccccccccccc}
1 &    &  5 &    & 14 &    & 30 &    & 55 &    & 91 & \\
&  4 &    &  9 &    & 16 &    & 25  &    & 36 & \\
&    &  5 &    &  7 &    &  9 &    &  11 & \\
&    &    &  2 &    &  2 &    &  2 & \\
\end{array}
$$

Prvi redak čini prvih $n$ uzastopnih vrijednosti od $f(x)$; svaki sljedeći redak čine razlike susjednih parova članova prethodnog retka. Uočavamo da, ako taj postupak ponovimo dovoljno puta (pod uvjetom da je $f(x)$ polinom), na kraju uvijek dobijemo konstantnu vrijednost.

Izračunamo da je prvi član razlika $i-1$-og reda $\sum_{j=1}^{i}(-1)^{i+j}\binom{i-1}{j-1}f(j)$, a prvi član razlika $i-1$-og reda doprinosi vrijednosti $f(k)$ $\binom{k-1}{i-1}$ puta.

$$
f(k)=\sum_{i=1}^n\binom{k-1}{i-1}\sum_{j=1}^{i}(-1)^{i+j}\binom{i-1}{j-1}f(j)
$$

Vremenska složenost je $O(n^2)$.

## Implementacija u C++-u

Od C++20 standardna biblioteka sadrži funkcije [`std::midpoint`](https://en.cppreference.com/w/cpp/numeric/midpoint) i [`std::lerp`](https://en.cppreference.com/w/cpp/numeric/lerp), koje služe za računanje polovišta odnosno za linearnu interpolaciju.

## Zadaci za vježbu

-   [„NOIP2020” 微信步数 (Koraci na WeChatu)](https://loj.ac/p/3389)
-   [„联合省选 2022” 填树 (Zajednički pokrajinski izbor 2022: Popunjavanje stabla)](https://loj.ac/p/3701)
-   [„NOI2019” 机器人 (Robot)](https://loj.ac/p/3157)

## Literatura

1.  [Interpolation - Wikipedia](https://en.wikipedia.org/wiki/Interpolation)
2.  [Newton polynomial - Wikipedia](https://en.wikipedia.org/wiki/Newton_polynomial)
