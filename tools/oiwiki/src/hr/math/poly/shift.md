---
title: Pomak polinoma | pomak uzastopnih vrijednosti u točkama
---

## Pomak polinoma

Pomak polinoma (Taylor shift) jednostavan je poseban slučaj kompozicije polinoma: zadani su koeficijenti polinoma $f(x)=\sum _ {i=0}^nf_ix^i$ i konstanta $c$, a treba odrediti koeficijente od $f(x+c)$, tj. $f(x)\mapsto f(x+c)$.

### Metoda podjele (divide and conquer)

Neka je

$$
f(x)=f_0(x)+x^{\left\lfloor n/2\right\rfloor}f_1(x)
$$

Tada je

$$
f(x+c)=f_0(x+c)+(x+c)^{\left\lfloor n/2\right\rfloor}f_1(x+c)
$$

Koeficijenti od $(x+c)^{\left\lfloor n/2\right\rfloor}$ binomni su koeficijenti, pa je

$$
T(n)=2T(n/2)+O(n\log n)=O(n\log^2 n)
$$

pri čemu je $O(n\log n)$ vrijeme množenja polinoma.

### Metoda Taylorove formule

Primijenimo li na $f(x)$ Taylorovu formulu u točki $c$, imamo

$$
f(x)=f(c)+\frac{f'(c)}{1!}(x-c)+\frac{f''(c)}{2!}(x-c)^2+\cdots +\frac{f^{(n)}(c)}{n!}(x-c)^n
$$

Tada je

$$
f(x+c)=f(c)+\frac{f'(c)}{1!}x+\frac{f''(c)}{2!}x^2+\cdots +\frac{f^{(n)}(c)}{n!}x^n
$$

Uočimo da za $t\geq 0$ vrijedi

$$
\begin{aligned}
t!\lbrack x^t\rbrack f(x+c)&=f^{(t)}(c)\\
&=\sum _ {i=t}^nf_ii!\frac{c^{i-t}}{(i-t)!}\\
&=\sum _ {i=0}^{n-t}f _ {i+t}(i+t)!\frac{c^i}{i!}
\end{aligned}
$$

Neka je

$$
\begin{aligned}
A_0(x)&=\sum _ {i=0}^nf _ {n-i}(n-i)!x^i\\
B_0(x)&=\sum _ {i=0}^n\frac{c^i}{i!}x^i
\end{aligned}
$$

Tada je

$$
\begin{aligned}
\lbrack x^{n-t}\rbrack (A_0(x)B_0(x))&=\sum _ {i=0}^{n-t} (\lbrack x^{n-t-i}\rbrack A_0(x))(\lbrack x^i\rbrack B_0(x))\\
&=\sum _ {i=0}^{n-t}f _ {i+t}(i+t)!\frac{c^i}{i!}\\
&=t!\lbrack x^t\rbrack f(x+c)
\end{aligned}
$$

### Metoda binomnog teorema

Promotrimo binomni teorem $\displaystyle (a+b)^n=\sum _ {i=0}^n\binom{n}{i}a^ib^{n-i}$; tada je

$$
\begin{aligned}
f(x+c)&=\sum _ {i=0}^nf_i(x+c)^i\\
&=\sum _ {i=0}^nf_i\left(\sum _ {j=0}^i\binom{i}{j}x^jc^{i-j}\right)\\
&=\sum _ {i=0}^nf_ii!\left(\sum _ {j=0}^i\frac{x^j}{j!}\frac{c^{i-j}}{(i-j)!}\right)\\
&=\sum _ {i=0}^n\frac{x^i}{i!}\left(\sum _ {j=i}^{n}f_jj!\frac{c^{j-i}}{(j-i)!}\right)
\end{aligned}
$$

Dobiveni rezultat isti je kao kod gornje metode.

## Pomak uzastopnih vrijednosti u točkama

???+ note "Primjer zadatka [LOJ 166 拉格朗日插值 2 (Lagrangeova interpolacija 2)](https://loj.ac/p/166)"
    Zadane su uzastopne vrijednosti $f(0),f(1),\dots ,f(n)$ polinoma $f$ stupnja najviše $n$; modulo $998244353$ izračunajte $f(c),f(c+1),\dots ,f(c+n)$, pri čemu je $1\leq n\leq 10^5,n < m\leq 10^8$.

### Metoda Lagrangeove interpolacijske formule

Promotrimo [Lagrangeovu interpolacijsku formulu](../numerical/interp.md#lagrange-插值法)

$$
\begin{aligned}
f(x)&=\sum _ {0\leq i\leq n}f(i)\prod _ {0\leq j\leq n\,\land \,j\neq i}\frac{x-j}{i-j}\\
&=\sum _ {0\leq i\leq n}f(i)\frac{x!}{(x-n-1)!(x-i)}\frac{(-1)^{n-i}}{i!(n-i)!}\\
&=\frac{x!}{(x-n-1)!}\sum _ {0\leq i\leq n}\frac{f(i)}{(x-i)}\frac{(-1)^{n-i}}{i!(n-i)!}
\end{aligned}
$$

Gornji izraz jest oblika konvolucije, ali ne jamči da je u nazivniku $x-i\neq 0$, pa u nastavku razmatramo samo slučaj $c > n$; ostali slučajevi (npr. kada se radi s koeficijentima modulo prost broj, treba izbjeći da se u nazivnicima koeficijenata od $B_0(x)$ pojavi nula) rješavaju se razlikovanjem slučajeva. Neka je

$$
\begin{aligned}
A_0(x)&=\sum _ {0\leq i\leq n}\frac{f(i)(-1)^{n-i}}{i!(n-i)!}x^i\\
B_0(x)&=\sum _ {i\geq 0}\frac{1}{c-n+i}x^i
\end{aligned}
$$

Tada za $t\geq 0$ vrijedi

$$
\begin{aligned}
\lbrack x^{n+t}\rbrack (A_0(x)B_0(x))&=\sum _ {i=0}^{n+t}(\lbrack x^i\rbrack A_0(x))(\lbrack x^{n+t-i}\rbrack B_0(x))\\
&=\sum _ {i=0}^{n}\frac{f(i)(-1)^{n-i}}{i!(n-i)!}\frac{1}{c+t-i}\\
&=\frac{(c+t-n-1)!}{(c+t)!}f(c+t)
\end{aligned}
$$

U implementaciji od $B_0(x)$ uzimamo samo potreban odsječak, čime možemo dobiti i više vrijednosti, a može se iskoristiti i ciklička konvolucija.

Malo izmijenimo problem: pretpostavimo da su za neki $d$ zadane vrijednosti $f(d),f(d+k),\dots ,f(d+nk)$; tada možemo izračunati $f(c+d),f(c+d+k),\dots ,f(c+d+nk)$, što promatramo kao pomak vrijednosti $g(0),g(1),\dots ,g(n)$ polinoma $g(x)=f(d+kx)$ u $g(c/k),g(c/k+1),\dots ,g(c/k+n)$.

Lagrangeova interpolacijska formula daje i način da se jedna vrijednost izračuna u linearnom vremenu održavanjem nekoliko prefiksnih i sufiksnih produkata.

## Primjene

### Stirlingovi brojevi prve vrste (bez predznaka) u istom retku

???+ note "Primjer zadatka [P5408 第一类斯特林数·行 (Stirlingovi brojevi prve vrste – redak)](https://www.luogu.com.cn/problem/P5408)"
    Modulo prost broj $167772161$ izračunajte $\displaystyle {n\brack 0},{n\brack 1},\dots ,{n\brack n}$, pri čemu je $1\leq n< 262144$.

Promotrimo

$$
x^{\overline{n}}=\sum _ {i=0}^n{n\brack i}x^i,\quad n\geq 0
$$

pri čemu je $x^{\overline{n}}=x\cdot (x+1)\cdots (x+n-1)$ rastuća faktorijelna potencija (rising factorial). Neka je $f_n(x)=x^{\overline{n}}$; tada je

$$
f_{2n}(x)=x^{\overline{n}}\cdot (x+n)^{\overline{n}}=f_n(x)f_n(x+n)
$$

Pomakom polinoma možemo u $O(n\log n)$ odrediti $f_n(x+n)$, pa se problem smanjuje na polovinu izvornoga, tj. na određivanje koeficijenata od $f_n(x)$; dakle

$$
T(n)=T(n/2)+O(n\log n)=O(n\log n)
$$

### Faktorijel modulo prost broj

???+ note "Primjer zadatka [P5282【模板】快速阶乘算法 (Predložak: brzi algoritam za faktorijel)](https://www.luogu.com.cn/problem/P5282)"
    Izračunajte $n!\bmod p$, pri čemu je $p$ prost i $1\leq n< p\leq 2^{31}-1$.

Neka je $v=\lfloor\sqrt{n}\rfloor$ i $g(x)=\prod _ {i=1}^v(x+i)$; tada je

$$
n!\equiv \left(\prod _ {i=0}^{v-1}g(iv)\right)\cdot \prod _ {i=v^2+1}^n i\pmod{p}
$$

pri čemu se $\prod _ {i=v^2+1}^n i$ može izračunati u vremenu $O(\sqrt{n})$; želimo brzo izračunati prvi dio gornjeg izraza.

#### Evaluacija polinoma u više točaka

Koeficijenti od $g(x)$ mogu se gornjim algoritmom pomaka polinoma dobiti u vremenu $O(n\log n)$, ali evaluacija u više točaka $g(0),g(v),g(2v),\dots ,g(v^2-v)$ zahtijeva vrijeme $O(\sqrt{n}\log ^2n)$.

#### Pomak uzastopnih vrijednosti u točkama

Neka je $g_d(x)=\prod _ {i=1}^d(x+i)$; pomoću $d+1$ vrijednosti $g_d(0),g_d(v),\dots ,g_d(dv)$ jednoznačno možemo odrediti taj polinom stupnja $d$, a k tome je

$$
g _ {2d}(x)=g_d(x)g_d(x+d)
$$

pa je $2d+1$ vrijednosti dovoljno da se jednoznačno odredi $g _ {2d}(x)$. Stoga pomakom uzastopnih vrijednosti izračunamo $g_d((d+1)v),g_d((d+2)v),\dots ,g_d(2dv)$ (tj. pomaknemo vrijednosti $h(0),h(1),\dots ,h(d)$ polinoma $h(x)=g_d(vx)$ u $h(d+1),h(d+2),\dots ,h(2d)$) i $g_d(d),g_d(v+d),\dots ,g_d(2dv+d)$ (tj. pomaknemo vrijednosti $h(0),h(1),\dots ,h(d)$ polinoma $h(x)=g_d(vx)$ u $h(d/v),h(d/v+1),h(d/v+2),\dots ,h(d/v+2d)$), a zatim množenjem odgovarajućih vrijednosti dobivamo $g _ {2d}(0),g _ {2d}(v),\dots ,g _ {2d}(2dv)$.

Da bismo iz $g_d(0),g_d(v),\dots ,g_d(dv)$ izračunali $g _ {d+1}(0),g _ {d+1}(v),\dots ,g _ {d+1}(dv),g _ {d+1}((d+1)v)$, promotrimo

$$
g _ {d+1}(x)=(x+d+1)\cdot g_d(x)
$$

Za jednu dodatnu vrijednost dovoljan je algoritam linearnog vremena. Dakle, na početku održavamo $g_1(0)=1,g_1(v)=v+1$, a zatim pomakom uzastopnih vrijednosti udvostručavanjem održavamo te vrijednosti; imamo

$$
T(n)=T(n/2)+O(n\log n)=O(n\log n)
$$

a treba nam samo oko $\sqrt{n}$ vrijednosti, pa je vremenska složenost $O(\sqrt{n}\log n)$.

### Prefiksne sume binomnih koeficijenata modulo prost broj

???+ note "Primjer zadatka [LOJ 6386 组合数前缀和 (Prefiksna suma binomnih koeficijenata)](https://loj.ac/p/6386)"
    Izračunajte $\displaystyle \sum _ {i=0}^m\binom{n}{i}\bmod 998244353$, pri čemu je $0\leq m\leq n\leq 9\times 10^8$.

Opišemo li korak rekurzije $n!=n\cdot (n-1)!$ matricom, imamo

$$
\begin{bmatrix}
n!
\end{bmatrix}
=\left(
\prod _ {i=0}^{n-1}
\begin{bmatrix}i+1\end{bmatrix}
\right)
\begin{bmatrix}
1
\end{bmatrix}
$$

Slično se rekurzija za prefiksnu sumu binomnih koeficijenata može opisati kao

$$
\begin{bmatrix}
\binom{n}{m+1}\\
\sum _ {i=0}^m\binom{n}{i}
\end{bmatrix}=
\begin{bmatrix}
(n-m)/(m+1)&0\\
1&1
\end{bmatrix}
\begin{bmatrix}
\binom{n}{m}\\
\sum _ {i=0}^{m-1}\binom{n}{i}
\end{bmatrix}
$$

Pazeći na redoslijed množenja matrica, imamo

$$
\begin{aligned}
\begin{bmatrix}
\binom{n}{m+1}\\
\sum _ {i=0}^m\binom{n}{i}
\end{bmatrix}
&=\left(
\prod _ {i=0}^{m}
\begin{bmatrix}
(n-i)/(i+1)&0\\1&1
\end{bmatrix}
\right)
\begin{bmatrix}
1\\0
\end{bmatrix}\\
&=
\frac{1}{(m+1)!}
\left(
\prod _ {i=0}^{m}
\begin{bmatrix}
n-i&0\\i+1&i+1
\end{bmatrix}
\right)
\begin{bmatrix}
1\\0
\end{bmatrix}
\end{aligned}
$$

Neka je $v=\lfloor\sqrt{m}\rfloor$; održavamo vrijednosti matrice

$$
\begin{aligned}
M _ d(x)&=
\prod _ {i=1}^d
\begin{bmatrix}
-x+n+1-i&0\\
x+i&x+i
\end{bmatrix}\\
&=
\begin{bmatrix}
f_d(x)&0\\
g_d(x)&h_d(x)
\end{bmatrix}
\end{aligned}
$$

u točkama $M _ d(0),M _ d(v),\dots ,M_d(dv)$, tj. $f_d(0),f_d(v),\dots ,f_d(dv)$, $h_d(0),\dots ,h_d(dv)$ i $g_d(0),\dots ,g_d(dv)$, a k tome je

$$
\begin{aligned}
M _ {2d}(x)&=
\prod _ {i=1}^{2d}
\begin{bmatrix}
-x+n+1-i&0\\
x+i&x+i
\end{bmatrix}\\
&=
\left(
\prod _ {i=1}^d
\begin{bmatrix}
-x-d+n+1-i&0\\
x+d+i&x+d+i
\end{bmatrix}
\right)
\left(
\prod _ {i=1}^d
\begin{bmatrix}
-x+n+1-i&0\\
x+i&x+i
\end{bmatrix}
\right) \\
&=
\begin{bmatrix}
f_d(x+d)&0\\
g_d(x+d)&h_d(x+d)
\end{bmatrix}
\begin{bmatrix}
f_d(x)&0\\
g_d(x)&h_d(x)
\end{bmatrix} \\
&=
\begin{bmatrix}
f_d(x+d)f_d(x)&0\\
g_d(x+d)f_d(x)+h_d(x+d)g_d(x)&h_d(x+d)h_d(x)
\end{bmatrix}
\end{aligned}
$$

pri čemu je element u donjem desnom kutu matrice upravo ono što održavamo u algoritmu za faktorijel; tada je

$$
\begin{aligned}
\prod _ {i=0}^{m}
\begin{bmatrix}
n-i&0\\i+1&i+1
\end{bmatrix}=
\left(
\prod _ {i=(k+1)v}^m
\begin{bmatrix}
n-i&0\\
i+1&i+1
\end{bmatrix}
\right)
\begin{bmatrix}
f_v(kv)&0\\
g_v(kv)&h_v(kv)
\end{bmatrix}
\cdots
\begin{bmatrix}
f_v(0)&0\\
g_v(0)&h_v(0)
\end{bmatrix}
\end{aligned}
$$

što se može izračunati u vremenu $O(\sqrt m\log m)$.

### Harmonijski brojevi modulo prost broj

???+ note "Primjer zadatka [P5702 调和级数求和 (Suma harmonijskog reda)](https://www.luogu.com.cn/problem/P5702)"
    Izračunajte $\sum _ {i=1}^ni^{-1}\bmod p$, pri čemu je $p$ prost i $1\leq n< p< 2^{30}$.

Označimo $H_n=\sum _ {k=1}^nk^{-1}$; jedan korak rekurzije glasi

$$
\begin{bmatrix}
(n+1)!\\(n+1)!H _ {n+1}
\end{bmatrix}=
\begin{bmatrix}
n+1&0\\1&n+1
\end{bmatrix}
\begin{bmatrix}
n!\\n!H_n
\end{bmatrix}
$$

Tada je

$$
\begin{bmatrix}
{n+1\brack 1}\\{n+1\brack 2}
\end{bmatrix}=
\begin{bmatrix}
n!\\n!H_n
\end{bmatrix}=
\left(
\prod _ {i=0}^{n-1}
\begin{bmatrix}
i+1&0\\1&i+1
\end{bmatrix}
\right)
\begin{bmatrix}
1\\0
\end{bmatrix}
$$

Ovdje su $\displaystyle {n+1\brack 1}$ i $\displaystyle {n+1\brack 2}$ Stirlingovi brojevi prve vrste bez predznaka. Metoda održavanja vrijednosti matrice u točkama ista je kao gore.

## Rekurzija s polinomnim koeficijentima

Kakav bismo algoritam, slično kao u gornjem primjeru brzog algoritma za faktorijel, željeli dobiti u općenitijem slučaju?

???+ note "Primjer zadatka [P6115【模板】整式递推 (Predložak: rekurzija s polinomnim koeficijentima)](https://www.luogu.com.cn/problem/P6115)"
    Niz $a$ zadovoljava $\forall n\ge m,\sum_{k=0}^ma_{n-k}P_k(n)=0$, pri čemu su $P_k$ polinomi stupnja najviše $d$.  
    Zadani su koeficijenti svih $P_k$ te $a_0,a_1,\dots,a_{m-1}$; izračunajte $a_n$.
    Rezultat je modulo $998244353$. $n\le6\times10^8$, $1\le m,d\le7$, vremensko ograničenje $7s$.

Da bismo sustavnije opisali konstrukciju matrica iz gornjih primjera, uvodimo pojam [$\lambda$-matrice](../linear-algebra/jordan.md#lambda-%E7%9F%A9%E9%98%B5).

Za implementaciju rekurzije s polinomnim koeficijentima trebamo uočiti da u brzom algoritmu za faktorijel vrijednosti koje održavamo zapravo nisu $n!$, nego $\prod_{i=0}^{T-1}(aT+i)$, tj. **odnos (množitelj) između para vrijednosti**.

Budući da red $m$ rekurzije s polinomnim koeficijentima više nije $1$, **ne možemo izravno održavati množitelj između para brojeva**; umjesto toga održavamo **linearnu transformaciju između para $m$-dimenzionalnih vektora**, tj. matricu $m\times m$, **pri čemu svaki element matrice odgovara vrijednosti nekog polinoma u točki**.

Lako se vidi da za opći problem izračuna dalekog koeficijenta rekurzije s polinomnim koeficijentima možemo konstruirati

$$
-{\frac{1}{P_0(n)}}\begin{bmatrix}P_1(n)&P_2(n)&P_3(n)&\cdots&P_{m-1}(n)&P_m(n)\\-P_0(n)\\&-P_0(n)\\&&-P_0(n)\\&&&\ddots\\&&&&-P_0(n)\\\end{bmatrix}
\begin{bmatrix}a_{n-1}\\a_{n-2}\\a_{n-3}\\\vdots\\a_{n-m+1}\\a_{n-m}\end{bmatrix}
=\begin{bmatrix}a_n\\a_{n-1}\\a_{n-2}\\\vdots\\a_{n-m+2}\\a_{n-m+1}\end{bmatrix}
$$

Neka je

$$
B(\lambda)=\begin{bmatrix}
    P_1(\lambda)&P_2(\lambda)&P_3(\lambda)&\cdots&P_{m-1}(\lambda)&P_m(\lambda)\\
    -P_0(\lambda)\\
    &-P_0(\lambda)\\
    &&-P_0(\lambda)\\
    &&&\ddots\\
    &&&&-P_0(\lambda)\\
\end{bmatrix}
$$

Zanemarimo zasad faktor $-\frac1{P_0(n)}$ sprijeda; sada želimo održavati veličine oblika $\prod_{i=0}^{T-1}B(aT+m+i)$, pri čemu se množi zdesna nalijevo.

Lako se vidi da je $B_T(\lambda)=\prod_{i=0}^{T-1}B(\lambda+i)$ $\lambda$-matrica čiji elementi imaju stupanj najviše $dT$, pa ju je dovoljno održavati pomoću $dT+1$ vrijednosti.

Stoga održavamo **vrijednosti u točkama** tih $\lambda$-matrica: $B_T(m)$, $B_T(m+T)$, $B_T(m+2T)$, $\dots$, $B_T(m+(dT-1)T)$, $B_T(m+dT^2)$, a zatim, slično kao u brzom algoritmu za faktorijel, izravno radimo pomak vrijednosti polinoma u točkama i udvostručavanje.

Konkretno, da bismo $t=\log_2T$ povećali za $1$, radimo sljedeće:

1.  U vremenu $O(m^2dT\log(dT))$ dobijemo $B_T(p+dT^2)$, $B_T(p+(dT+1)T)$, $B_T(p+(dT+2)T)$, $\cdots$, $B_T(p+(2dT-1)T)$, $B_T(p+(2dT)dT)$.
2.  U vremenu $O(m^2dT\log(dT))$ dobijemo $B_T(p+2dT^2)$, $B_T(p+(2dT+1)T)$, $B_T(p+(2dT+2)T)$, $\cdots$, $B_T(p+(3dT-1)T)$, $B_T(p+(3dT)dT)$.
3.  U vremenu $O(m^2dT\log(dT))$ dobijemo $B_T(p+3dT^2)$, $B_T(p+(3dT+1)T)$, $B_T(p+(3dT+2)T)$, $\cdots$, $B_T(p+(4dT-1)T)$, $B_T(p+(4dT)dT)$.
4.  Izračunamo $B_{2T}(v)=B_{T}(v+T)B_{T}(v)$.

U svakom krugu na pomak trošimo složenost $O(m^2dT\log(dT))$; istodobno u svakom krugu radimo samo $\Theta(dT)$ množenja matrica, čija se složenost može uzeti kao $O(m^3dT)$.

Na kraju, dovoljno je doći do $T\ge\sqrt{n/d}$.

Ranije spomenuti faktor $-\frac1{P_0(n)}$ rješava se na sličan način.

Tako je složenost pretprocesiranja $\Theta(\sqrt{nd}(m^3+m^2\log(nd)))$.

Što se tiče upita, trebamo samo $\Theta(n/T)$ množenja vektora s matricom i $O(T)$ izravnih prijelaza.

Lako se vidi da taj dio računa nije usko grlo složenosti.

Stoga je ukupna složenost algoritma $\Theta(\sqrt{nd}(m^3+m^2\log(nd)))$.

Pri implementaciji možemo trikom cikličke konvolucije smanjiti konstantu NTT-a.

U praksi najčešće izdvajamo daleki koeficijent poznate D-konačne (diferencijalno konačne) funkcije izvodnice, pa su $m,d$ konstante, čime postižemo izračun dalekog koeficijenta u $\Theta(\sqrt n\log n)$.

## Literatura

-   Alin Bostan, Pierrick Gaudry, and Eric Schost. Linear recurrences with polynomial coefficients and application to integer factorization and Cartier–Manin operator.
-   Blog Min\_25
-   [ZZQ-ov blog – 阶乘模大质数 (Faktorijel modulo velik prost broj)](https://www.cnblogs.com/zzqsblog/p/8408691.html)
