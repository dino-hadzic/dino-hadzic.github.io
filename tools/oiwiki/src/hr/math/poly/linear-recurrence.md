---
title: Homogena linearna rekurzija s konstantnim koeficijentima
---

## Uvod

Homogeni linearno rekurzivni nizovi s konstantnim koeficijentima (poznati i kao C-konačni ili C-rekurzivni nizovi) česta su i osnovna klasa rekurzivnih nizova.

Za niz $\left(a_j\right)_{j\geq 0}$ i njegovu rekurziju

$$
a_n=\sum_{j=1}^{d}c_ja_{n-j},\qquad (n\geq d)
$$

u kojoj $c_j$ nisu svi nula, cilj nam je, uz zadane početne vrijednosti $a_0,\dots ,a_{d-1}$ i koeficijente rekurzije $c_1,\dots ,c_d$, izračunati $a_k$. Ako je $k\gg d$, želimo brži algoritam.

Ovdje se $\left(a_j\right)_{j\geq 0}$ naziva homogenim linearno rekurzivnim nizom s konstantnim koeficijentima reda $d$.

### Fiduccijin algoritam

Fiduccijin algoritam računa $a_k$ pomoću ostatka pri dijeljenju polinoma i brzog potenciranja, u vremenu $O(\mathsf{M}(d)\log k)$, pri čemu $O(\mathsf{M}(d))$ označava vrijeme množenja dvaju polinoma stupnja $O(d)$.

**Algoritam**: konstruiramo polinome $\Gamma(x):=x^d-\sum_{j=0}^{d-1}c_{d-j}x^j$ i $A(x):=\sum_{j=0}^{d-1}a_jx^j$; tada je

$$
a_k=\left\langle x^k\bmod{\Gamma(x)},A(x)\right\rangle
$$

gdje je skalarni produkt definiran kao $\left\langle \left(\sum_{j=0}^{n-1}f_jx^j\right),\left(\sum_{j=0}^{n-1}g_jx^j\right) \right\rangle :=\sum_{j=0}^{n-1}f_jg_j$.

**Dokaz**: definiramo pratilačku matricu (companion matrix) polinoma $\Gamma(x)$ kao

$$
C_\Gamma:=
\begin{bmatrix}
&&&c_d \\
1&&&c_{d-1} \\
&\ddots &&\vdots \\
&&1&c_1
\end{bmatrix}
$$

Definiramo polinom $b(x):=\sum_{j=0}^{d-1}b_jx^j$ i

$$
B_b:=\begin{bmatrix}b_0&b_1&\cdots &b_{d-1}\end{bmatrix}^{\intercal}
$$

Uočimo da je

$$
\underbrace{\begin{bmatrix}
&&&c_d \\
1&&&c_{d-1} \\
&\ddots &&\vdots \\
&&1&c_1
\end{bmatrix}}_{C_\Gamma}
\underbrace{\begin{bmatrix}
b_0 \\
b_1 \\
\vdots \\
b_{d-1}
\end{bmatrix}}_{B_b}=
\underbrace{\begin{bmatrix}
c_db_{d-1} \\
b_0+c_{d-1}b_{d-1} \\
\vdots \\
b_{d-2}+c_1b_{d-1}
\end{bmatrix}} _ {B_{xb\bmod{\Gamma}}}
$$

te

$$
\begin{aligned}
C_\Gamma&=\begin{bmatrix}B_{x\bmod{\Gamma}}&B_{x^2\bmod{\Gamma}}&\cdots &B_{x^d\bmod{\Gamma}}\end{bmatrix}, \\
\left(C_\Gamma\right)^2&=\begin{bmatrix}B_{x^2\bmod{\Gamma}}&B_{x^3\bmod{\Gamma}}&\cdots &B_{x^{d+1}\bmod{\Gamma}}\end{bmatrix}, \\
\cdots \\
\left(C_\Gamma\right)^k&=\begin{bmatrix}B_{x^k\bmod{\Gamma}}&B_{x^{k+1}\bmod{\Gamma}}&\cdots &B_{x^{k+d}\bmod{\Gamma}}\end{bmatrix}
\end{aligned}
$$

Zapišemo li rekurziju matrično, imamo

$$
\begin{bmatrix}
a_{k} \\
a_{k+1} \\
\vdots \\
a_{k+d-1}
\end{bmatrix}=\underbrace{\begin{bmatrix}
&1&& \\
&&\ddots & \\
&&&1 \\
c_d&c_{d-1}&\cdots &c_1
\end{bmatrix}^k} _ {\left(\left(C_\Gamma\right)^{\intercal}\right)^k=\left(\left(C_\Gamma\right)^{k}\right)^{\intercal}}
\begin{bmatrix}
a_0 \\
a_{1} \\
\vdots \\
a_{d-1}
\end{bmatrix}
$$

Vidimo da je prvi redak matrice $\left(\left(C_\Gamma\right)^{k}\right)^{\intercal}$ jednak $B_{x^k\bmod{\Gamma}}$, pa tvrdnja slijedi iz definicije množenja matrica.

### Prikaz racionalnom funkcijom

Za gornji niz $\left(a_j\right)_{j\geq 0}$ sigurno postoji racionalna funkcija

$$
\frac{P(x)}{Q(x)}=\sum_{j\geq 0}a_jx^j
$$

pri čemu je $Q(x)=x^d\Gamma\left(x^{-1}\right)$ i $\deg{P}<d$. Nazivamo je „**racionalnom funkcijom**” zato što su $P(x),Q(x)$ „**polinomi**”.

**Dokaz**: za $P(x)=\sum_{j=0}^{d-1}p_jx^j$ i $Q(x):=\sum_{j=0}^{d}q_jx^j$ promotrimo definiciju koeficijenata od $\dfrac{P(x)}{Q(x)}=\sum_{j\geq 0}\tilde{q}_jx^j$; to je gotovo upravo definicija „**dijeljenja**” formalnih redova potencija,

$$
\tilde{q}_N=
\begin{cases}
p_0q_0^{-1},&\text{ if }N=0, \\
\left(p_N-\sum_{j=1}^{N}q_j\tilde{q}_{N-j}\right)\cdot q_0^{-1},&\text{ else if }N<d, \\
-q_0^{-1}\sum_{j=1}^{d}q_j\tilde{q}_{N-j},&\text{ otherwise}.
\end{cases}
$$

Dovoljno je staviti

$$
P(x)=\left(\left(\sum_{j\geq 0}a_jx^j\right)\cdot x^d\Gamma\left(x^{-1}\right)\right)\bmod{x^d}
$$

pa po definiciji $\tilde{q}_N$ nužno vrijedi $\dfrac{P(x)}{Q(x)}=\sum_{j\geq 0}a_jx^j$.

### Bostan–Morijev algoritam

#### Računanje jednog člana

Cilj nam je i dalje, uz zadane gornje polinome $P(x),Q(x)$, izračunati $\left\lbrack x^k\right\rbrack\dfrac{P(x)}{Q(x)}$.

Bostan–Morijev algoritam temelji se na Graeffeovoj iteraciji: za gornje polinome $P(x),Q(x)$ vrijedi

$$
\frac{P(x)}{Q(x)}=\frac{P(x)Q(-x)}{Q(x)Q(-x)}=\frac{U_0(x^2)+xU_1(x^2)}{V(x^2)}
$$

Budući da je nazivnik $V(x^2)$ parna funkcija, u potproblemu treba razmotriti samo jednu stranu

$$
\left\lbrack x^k\right\rbrack\dfrac{P(x)}{Q(x)}=\left\lbrack x^{\left\lfloor k/2\right\rfloor}\right\rbrack \frac{U_{k\bmod{2}}(x)}{V(x)}
$$

Po cijeni dvaju množenja polinoma problem smanjujemo barem na polovinu izvornoga, a za $k=0$ očito je $\left\lbrack x^0\right\rbrack \dfrac{P(x)}{Q(x)}=\dfrac{P(0)}{Q(0)}$; vremenska složenost ista je kao gore.

#### Računanje više uzastopnih članova

Cilj je, uz zadane gornje polinome $P(x),Q(x)$, izračunati $\left\lbrack x^{\left\lbrack L,R\right)}\right\rbrack\dfrac{P(x)}{Q(x)}$. U računu koji slijedi razmatramo samo koeficijente koji „**utječu**” na odgovor; to je ključ Bostan–Morijeva algoritma.

Bez smanjenja općenitosti pretpostavimo $\deg{P}<\deg{Q}$; u suprotnom jednim dijeljenjem s ostatkom problem svodimo na taj slučaj.

Najprije razmotrimo jednostavniji problem:

$$
\left\lbrack x^{\left\lbrack L,R\right)}\right\rbrack\frac{1}{Q(x)}=\left\lbrack x^{\left\lbrack L,R\right)}\right\rbrack\frac{1}{Q(x)Q(-x)}\cdot Q(-x)
$$

Trebamo izračunati $\left\lbrack x^{\left\lbrack L-\deg{Q},R\right)}\right\rbrack\dfrac{1}{Q(x)Q(-x)}$, zatim obaviti jedno množenje i izdvojiti koeficijente uz $x^L,\dots ,x^{R-1}$. Neka je $V(x^2)=Q(x)Q(-x)$; tada je dovoljno izračunati

$$
\left\lbrack x^{\left\lbrack \left\lceil\frac{L-\deg{Q}}{2}\right\rceil,\left\lceil\frac{R}{2}\right\rceil\right)}\right\rbrack\frac{1}{V(x)}
$$

da bismo rekonstruirali $\left\lbrack x^{\left\lbrack L-\deg{Q},R\right)}\right\rbrack\dfrac{1}{Q(x)Q(-x)}$. Nadalje, dovoljno je izračunati $\left\lbrack x^{\left\lbrack L-\deg{P},R\right)}\right\rbrack\dfrac{1}{Q(x)}$ pa jednim množenjem s $P(x)$ dobiti $\left\lbrack x^{\left\lbrack L,R\right)}\right\rbrack\dfrac{P(x)}{Q(x)}$.

Iako gornji algoritam već radi, vremenska složenost svakog rekurzivnog poziva ovisi o $R-L$; želimo se barem u rekurzivnom računu riješiti $R-L$. Konkretnije, razmotrimo najprije računanje $\left\lbrack x^{\left\lbrack L,L+\deg Q+1\right)}\right\rbrack \dfrac{1}{Q(x)}$; promotrimo

$$
\left\lbrack x^{\left\lbrack L,L+\deg Q+1\right)}\right\rbrack \frac{1}{Q(x)}=\left\lbrack x^{\left\lbrack L,L+\deg Q+1\right)}\right\rbrack \dfrac{1}{Q(x)Q(-x)}\cdot Q(-x)
$$

Trebamo izračunati

$$
\left\lbrack x^{\left\lbrack L-\deg Q,L+\deg Q+1\right)}\right\rbrack \dfrac{1}{Q(x)Q(-x)}
$$

Za $V(x^2)=Q(x)Q(-x)$ dovoljno je izračunati

$$
\left\lbrack x^{\left\lbrack \lceil (L-\deg Q)/2 \rceil,\lceil (L+\deg Q+1)/2 \rceil\right)}\right\rbrack \frac{1}{V(x)}
$$

To je zato što je

$$
\left\lbrack x^{k}\right\rbrack\dfrac{1}{Q(x)Q(-x)}=
\begin{cases}
\left\lbrack x^{k/2}\right\rbrack\dfrac{1}{V(x)},&\text{if }k\equiv 0\pmod{2}, \\
0,&\text{otherwise}.
\end{cases}
$$

Znamo da $L+\deg Q$ i $L-\deg Q$ imaju istu parnost, pa je

$$
\left\lceil \frac{L+\deg Q+1}{2}\right\rceil -\left\lceil \frac{L-\deg Q}{2}\right\rceil =
\begin{cases}
\deg Q+1,&\text{if }L+\deg Q\equiv 0\pmod{2}, \\
\deg Q,&\text{otherwise}.
\end{cases}
$$

Tako možemo napisati pseudokod

$$
\begin{array}{ll}
&\textbf{Algorithm }\operatorname{Slice-Coefficients}(Q,L)\text{:} \\
&\textbf{Input}\text{: }Q(x)\in\mathbb{C}\left\lbrack x\right\rbrack,L\in\mathbb{Z}\text{.} \\
&\textbf{Output}\text{: }\left\lbrack x^{\left\lbrack L,L+\deg Q+1\right)}\right\rbrack Q(x)^{-1}\text{.} \\
1&\textbf{if }L\leq 1\textbf{ then return }\left\lbrack x^{\left\lbrack L,L+\deg Q+1\right)}\right\rbrack Q(x)^{-1} \\
&\text{Use other algorithm to compute }Q(x)^{-1} \\
2&V(x^2)\gets Q(x)Q(-x) \\
3&k\gets \left\lceil \frac{L-\deg Q}{2}\right\rceil \\
4&(t_k,\dots ,t_{k+\deg Q})\gets \operatorname{Slice-Coefficients}\left(V,k\right) \\
5&T(x)\gets x^{(L-\deg Q)\bmod{2}}\sum_{j=0}^{\deg Q}t_{j+k}x^{2j} \\
6&\textbf{return }\left\lbrack x^{\left\lbrack \deg Q,2\deg Q+1\right)}\right\rbrack T(x)Q(-x)
\end{array}
$$

No sam taj algoritam nije dovoljan: trebamo iznova pronaći racionalnu funkciju i izračunati više koeficijenata.

#### Pronalaženje novog prikaza racionalnom funkcijom

Znamo sam $Q(x)$ i dio uzastopnih koeficijenata od $Q(x)^{-1}$, npr. $\left\lbrack x^{\left\lbrack L,L+\deg Q\right)}\right\rbrack Q(x)^{-1}$ uz $L\geq 0$, a želimo izračunati $\left\lbrack x^{\left\lbrack L+\deg Q,L+2\deg Q\right)}\right\rbrack Q(x)^{-1}$. To je ekvivalentno traženju nekog $P(x)$ s $\deg P< \deg Q$ takvog da se prvih $\deg Q$ članova od $\dfrac{P(x)}{Q(x)}$ podudara s $\left\lbrack x^{\left\lbrack L,L+\deg Q\right)}\right\rbrack Q(x)^{-1}$. Jednostavno rečeno: rekurzivna relacija (nazivnik racionalne funkcije) ostaje nepromijenjena, mi samo mijenjamo početne vrijednosti (brojnik racionalne funkcije).

Konkretno, promotrimo

$$
\frac{P(x)}{Q(x)}=\sum_{j\geq 0}a_jx^j
$$

Želimo rekurziju pomaknuti za $n$ članova unaprijed, tj.

$$
\sum_{j\geq n}a_jx^{j-n}=\frac{P(x)}{Q(x)x^n}-\frac{Q(x)\sum_{j=0}^{n-1}a_jx^j}{Q(x)x^n}
$$

Najprije jednim pozivom $\operatorname{Slice-Coefficients}(Q,L-\deg{P})$ izračunamo $\left\lbrack x^{\left\lbrack L-\deg{P},L-\deg{P}+\deg{Q}+1\right)}\right\rbrack Q(x)^{-1}$, zatim proširivanjem i spajanjem dobijemo $\left\lbrack x^{\left\lbrack L-\deg{P},L+\deg{Q}\right)}\right\rbrack Q(x)^{-1}$, pa iznova izračunamo brojnik takav da je

$$
\frac{\widetilde{P}(x)}{Q(x)}=\sum_{j\geq 0}\left(\left\lbrack x^{L+j}\right\rbrack \frac{P(x)}{Q(x)}\right)x^j
$$

Na kraju dijeljenjem formalnih redova potencija izračunamo $\left\lbrack x^{\left\lbrack 0,R-L\right)}\right\rbrack\dfrac{\widetilde{P}(x)}{Q(x)}$; vrijeme je $O(\mathsf{M}(d)\log L+\mathsf{M}(R-L))$.

## Literatura

1.  Alin Bostan, Ryuhei Mori.[A Simple and Fast Algorithm for Computing the $N$-th Term of a Linearly Recurrent Sequence](https://arxiv.org/abs/2008.08822).
