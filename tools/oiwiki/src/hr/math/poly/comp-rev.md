---
title: Kompozicija i kompozicijski inverz formalnih redova potencija
---

Kompozicija i kompozicijski inverz formalnih redova potencija također su česte operacije nad formalnim redovima potencija. Za $f$ bez posebnih svojstava dosad smo za računanje $f(g) \bmod{x^n}$, gdje je $f\in\mathbb{C}\left\lbrack\left\lbrack x\right\rbrack\right\rbrack,g\in x\mathbb{C}\left\lbrack\left\lbrack x\right\rbrack\right\rbrack$, uglavnom koristili algoritam složenosti $O\left(n^2\right)$ (koji i dalje treba FFT), ali zbog niske učinkovitosti rijetko se primjenjivao. Predstavljamo algoritam Kinoshite i Lija složenosti $O\left(\mathsf{M}\left(n\right)\log n\right)$, gdje je $O\left(\mathsf{M}\left(n\right)\right)$ vrijeme množenja dvaju polinoma stupnja $O\left( n\right)$.

## Kompozicija formalnih redova potencija / polinoma

Želimo li izračunati $f\left(g\left(x\right)\right)\bmod{x^n}$, svaki koeficijent od $f\left(g\left(x\right)\right)$ mora biti zbroj konačno mnogo članova, pa smo prije zahtijevali $f(x)\in\mathbb{C}\left\lbrack\left\lbrack x\right\rbrack\right\rbrack,g(x)\in x\mathbb{C}\left\lbrack\left\lbrack x\right\rbrack\right\rbrack$; no taj je uvjet ispunjen i ako je $f(x),g(x)\in\mathbb{C}\left\lbrack x\right\rbrack$. Budući da koeficijente od $f\left(g\left(x\right)\right)$ ionako moramo odrezati, možemo odmah promatrati slučaj u kojem su $f(x),g(x)$ oba polinomi. Za $f(x)=\sum_{j=0}^{n-1}f_jx^j$ vrijedi

$$
f\left(g\left(x\right)\right)=\sum_{j=0}^{n-1}f_jg\left(x\right)^j
$$

Promatramo racionalnu funkciju nad prstenom $\mathbb{C}\left\lbrack x\right\rbrack\left(\left( y\right)\right)$

$$
\begin{aligned}
\frac{f\left(y^{-1}\right)}{1-y\cdot g(x)}&=\sum_{j\geq 0}\left(\cdots +f_jy^{-j}+\cdots\right)g(x)^jy^j \\
f\left(g\left(x\right)\right)&=\left\lbrack y^0\right\rbrack\frac{f\left(y^{-1}\right)}{1-y\cdot g(x)}
\end{aligned}
$$

Prema Bostan–Morijevu algoritmu spomenutom u članku [Homogena linearna rekurzija s konstantnim koeficijentima](./linear-recurrence.md), Kinoshita i Li primijetili su da ga se može preinačiti u dvovarijabilni oblik:

$$
\begin{aligned}
\frac{P\left(y\right)}{Q\left(x,y\right)}\bmod{x^n}&=\left(\frac{P\left(y\right)}{Q\left(x,y\right)Q\left(-x,y\right)}\bmod{x^n}\right)Q\left(-x,y\right)\bmod{x^n} \\
&=\left(\frac{P(y)}{V(x^2,y)}\bmod{x^n}\right)Q\left(-x,y\right)\bmod{x^n} \\
&=\left.\left(\frac{P(y)}{V(z,y)}\bmod{z^{\left\lceil n/2\right\rceil}}\right)\right|_{z=x^2}Q\left(-x,y\right)\bmod{x^n}
\end{aligned}
$$

U takvom rekurzivnom računu, kad je $n=1$, treba izračunati samo

$$
\frac{P(y)}{Q(x,y)}\bmod{x}=\frac{P(y)}{Q(0,y)}\in\mathbb{C}\left(\left( y\right)\right)
$$

Pri računanju $\dfrac{P(y)}{V(z,y)}\bmod{z^{\left\lceil n/2\right\rceil}}\in\mathbb{C}\left\lbrack z\right\rbrack\left(\left( y\right)\right)$ ne moramo čuvati sve koeficijente uz potencije od $y$: na kraju nam treba samo koeficijent uz $y^0$, pa koeficijenti uz $y^{>0}$ nisu potrebni, a budući da nakon što izračunamo prethodni izraz ga moramo pomnožiti s nekoliko „**polinoma**” oblika $Q(-x,y)\in\mathbb{C}\left\lbrack x,y\right\rbrack$, dovoljno je čuvati samo koeficijente koji doprinose koeficijentu uz $y^0$. Sada možemo dati pseudokod:

$$
\begin{array}{ll}
&\textbf{Algorithm }\operatorname{\mathsf{Comp}}\left(P(y),Q(x,y),n,m\right)\text{:} \\
&\textbf{Input}\text{: }P=\sum_{0\leq j< n}p_jy^{-j}\in\mathbb{C}((y)),Q\in\mathbb{C}\left\lbrack x,y\right\rbrack ,n,m\in\mathbb{N}_{>0}\text{.} \\
&\textbf{Output}\text{: }\left\lbrack y^{\left(-m,0\right\rbrack}\right\rbrack\dfrac{P(y)}{Q(x,y)}\bmod{x^n}\text{.} \\
&\textbf{Require}\text{: }\left\lbrack x^0y^0\right\rbrack Q=1\text{.} \\
1&\textbf{if }n=1\textbf{ then return }\left(\left\lbrack y^{-m+1}\right\rbrack\frac{P(y)}{Q(0,y)},\dots ,\left\lbrack y^0\right\rbrack\frac{P(y)}{Q(0,y)}\right) \\
2&V(x^2,y)\gets Q(x,y)Q(-x,y)\bmod{x^n} \\
3&d\gets\deg_y Q\left(-x,y\right)\\
4&\left(t_{-(m+d)+1},\dots ,t_0\right)\gets \operatorname{\mathsf{Comp}}\left(P(y),V(x,y),\left\lceil n/2\right\rceil,m+d\right) \\
5&T(x,y)\gets \sum_{j=-(m+d)+1}^0t_jy^j \\
6&U(x,y)=\sum_{j=-(m+d)+1}^d u_jy^j\gets T(x^2,y)Q(-x,y)\bmod{x^n} \\
7&\textbf{return }\left(u_{-m+1},\dots ,u_0\right)
\end{array}
$$

Tada imamo

$$
f\left(g\left(x\right)\right)\bmod{x^n}=\operatorname{\mathsf{Comp}}\left(f\left(y^{-1}\right),1-y\cdot g(x),\max\left\lbrace 1+\deg f,n\right\rbrace ,1\right)\bmod{x^n}
$$

Treći je parametar takav zato što $g(0)$ ne mora biti nula: ako je $\deg f\geq n$, tada se $f(x)$ ne smije odrezati pri računanju $f\left(g(x)\right)$. Možemo umjesto toga računati $f(g)=f\circ \left(x+g(0)\right)\circ \left(g-g(0)\right)$; tada uzmemo $F:=f\left(x+g(0)\right)\bmod{x^n}$ i $G:=g-g(0)$ te računamo $\operatorname{\mathsf{Comp}}\left(F\left(y^{-1}\right),1-y\cdot G(x),n,1\right)$.

Osim toga, zbog ograničenja u pozivima, $Q(0,y)^{-1}$ u završnom koraku rekurzije može se izravno izvesti i nije ga potrebno računati algoritmom za multiplikativni inverz formalnog reda potencija; dovoljno je jedno množenje nakon kojega izdvojimo potrebne koeficijente.

## Česti posebni oblici kompozicije

Sve često korištene [elementarne funkcije polinoma](./elementary-func.md) mogu se izračunati kompozicijom:

$$
\begin{aligned}
g(0)=1&,\space g^{-1}=1+(1-g)+(1-g)^2+\cdots \\
g(0)=1&,\space \log g=-\dfrac{1-g}{1}-\dfrac{(1-g)^2}{2}-\dfrac{(1-g)^3}{3}-\cdots \\
g(0)=0&,\space \exp g=1+\dfrac{g}{1!}+\dfrac{g^2}{2!}+\dfrac{g^3}{3!}+\cdots \\
g(0)=1&,\space g^e=1+\dfrac{e}{1!}(g-1)+\dfrac{e(e-1)}{2!}(g-1)^2+\cdots
\end{aligned}
$$

Potenciranje ćemo koristiti i pri računanju kompozicijskog inverza.

### Kroneckerova supstitucija

Prije analize vremenske složenosti razmotrimo kako množiti polinome dviju varijabli. Jedna je ideja „pakiranje” koeficijenata; tu je metodu Kronecker uveo 1882. godine: supstitucijom $y\mapsto x^N$ množenje u $R\left\lbrack x,y\right\rbrack$ svodi se na množenje u $R\left\lbrack x\right\rbrack$, uz uvjet da je $N$ dovoljno velik.

Neka je $\deg_x \left(AB\right)<N$; tada nakon što izračunamo $A\left(x,x^N\right)B\left(x,x^N\right)$ još uvijek možemo rekonstruirati $A(x,y)B(x,y)$, a „pakiranje” i „raspakiravanje” traju linearno vrijeme.

Dovoljno je primijeniti Kroneckerovu supstituciju i zatim množiti polinome jedne varijable. Lako se vidi da se, kad je $n$ potencija dvojke, gornji algoritam izvršava u vremenu $O\left(\mathsf{M}\left(n\right)\log n\right)$, jer se u svakoj razini rekurzije stupanj po $y$ udvostručuje, a stupanj po $x$ prepolavlja.

??? note "Predložak ([P5373【模板】多项式复合函数 (Predložak: kompozicija polinoma)](https://www.luogu.com.cn/problem/P5373))"
    Kôd je u odnosu na izvorni algoritam ponešto pojednostavljen i izmijenjen kako bi bio kraći.
    
    ```cpp
    --8<-- "docs/math/code/poly/comp-rev/comp_1.cpp"
    ```

## Kompozicijski inverz formalnog reda potencija

Zadan je $f\in x\mathbb{C}\left\lbrack\left\lbrack x\right\rbrack\right\rbrack$ uz $f'(0)\neq 0$; treba naći $g(x)\bmod{x^n}$ takav da je $f(g)\equiv g(f)\equiv x\pmod{x^n}$.

Prema [Lagrangeovoj inverziji](./lagrange-inversion.md), za $n>1,k\geq 0$ vrijedi

$$
\left\lbrack x^{n-1}\right\rbrack f(x)^k=\frac{k}{n-1}\left\lbrack x^{n-1-k}\right\rbrack \left(\frac{g(x)}{x}\right)^{-(n-1)}
$$

Dakle, ako za $k=0,1,\dots ,n-1$ možemo izračunati $\left\lbrack x^{n-1}\right\rbrack f(x)^k$, možemo izračunati i kompozicijski inverz.

Kinoshita i Li primijetili su da možemo promatrati racionalnu funkciju dviju varijabli

$$
\frac{1}{1-y\cdot f(x)}=\sum_{j\geq 0}f(x)^jy^j
$$

a ovaj problem ima i općenitiji oblik, problem Power Projection: želimo izračunati

$$
u:=\left\lbrack x^{n-1}\right\rbrack\frac{P(x,y)}{Q(x,y)}\bmod{y^m}
$$

Kad je $n-1=0$, očito je $u=\dfrac{P(0,y)}{Q(0,y)}\bmod{y^m}$; inače imamo

$$
\frac{P(x,y)}{Q(x,y)}=\frac{P(x,y)Q(-x,y)}{Q(x,y)Q(-x,y)}=\frac{U_e\left(x^2,y\right)+xU_o\left(x^2,y\right)}{V\left(x^2,y\right)}
$$

pa je

$$
\begin{aligned}
u&=\begin{cases}
\left\lbrack x^{n-1}\right\rbrack\dfrac{U_e\left(x^2,y\right)}{V\left(x^2,y\right)}&\text{ if }n-1\text{ is even,} \\
\left\lbrack x^{n-1}\right\rbrack\dfrac{xU_o\left(x^2,y\right)}{V\left(x^2,y\right)}&\text{ if }n-1\text{ is odd.}
\end{cases} \\
&=\begin{cases}
\left\lbrack x^{\left\lceil n/2\right\rceil-1}\right\rbrack\dfrac{U_e\left(x,y\right)}{V\left(x,y\right)}&\text{ if }n-1\text{ is even,} \\
\left\lbrack x^{\left\lceil n/2\right\rceil-1}\right\rbrack\dfrac{U_o\left(x,y\right)}{V\left(x,y\right)}&\text{ if }n-1\text{ is odd.}
\end{cases}
\end{aligned}
$$

Dajemo pseudokod:

$$
\begin{array}{ll}
&\textbf{Algorithm }\operatorname{\mathsf{PowProj}}\left(P(x,y),Q(x,y),n,m\right)\text{:} \\
&\textbf{Input}\text{: }P,Q\in\mathbb{C}\left\lbrack x,y\right\rbrack ,n,m\in\mathbb{N}_{>0}\text{.} \\
&\textbf{Output}\text{: }\left\lbrack x^{n-1}\right\rbrack\dfrac{P(x,y)}{Q(x,y)}\bmod{y^m}\text{.} \\
&\textbf{Require}\text{: }\left\lbrack x^0y^0\right\rbrack Q=1\text{.} \\
1&\textbf{while }n>1\textbf{ do} \\
2&\qquad U(x,y)\gets P(x,y)Q(-x,y)\bmod{x^n}\bmod{y^m} \\
3&\qquad \textbf{if }n-1\text{ is even }\textbf{then} \\
4&\qquad\qquad P(x,y)\gets \sum_{j=0}^{\left\lceil n/2\right\rceil +1}\left(\left\lbrack x^{2j}\right\rbrack U(x,y)\right)x^j \\
5&\qquad \textbf{else} \\
6&\qquad\qquad P(x,y)\gets \sum_{j=0}^{\left\lceil n/2\right\rceil +1}\left(\left\lbrack x^{2j+1}\right\rbrack U(x,y)\right)x^j \\
7&\qquad \textbf{end if} \\
8&\qquad V(x,y)\gets Q(x,y)Q(-x,y)\bmod{x^n}\bmod{y^m} \\
9&\qquad Q(x,y)\gets \sum_{j=0}^{\left\lceil n/2\right\rceil +1}\left(\left\lbrack x^{2j}\right\rbrack V(x,y)\right)x^j \\
10&\qquad n\gets \left\lceil n/2\right\rceil \\
11&\textbf{end while} \\
12&\textbf{return }\left(\frac{P(0,y)}{Q(0,y)}\bmod{y^m}\right)
\end{array}
$$

Isto tako, $Q(0,y)^{-1}$ možemo izvesti izravno, bez računanja multiplikativnog inverza formalnog reda potencija, pa algoritam za kompozicijski inverz glasi

$$
\begin{array}{ll} &\textbf{Algorithm }\operatorname{\mathsf{Rev}}(f(x),n)\text{:} \\
&\textbf{Input}\text{: }f\in x\mathbb{C}\left\lbrack\left\lbrack x\right\rbrack\right\rbrack, f'(0)\neq 0,n\in\mathbb{N}_{\geq 2}\text{.} \\
&\textbf{Output}\text{: }g(x)\bmod{x^n} \text{ such that }f(g)\equiv g(f)\equiv x\pmod{x^n}\text{.} \\
1&t\gets f'(0) \\
2&F(x)\gets f\left(t^{-1}x\right) \\
3&\sum_{k=0}^{n-1}a_ky^k\gets \operatorname{\mathsf{PowProj}}\left(1,1-y\cdot F(x),n,n\right) \\
4&G(x)\gets \sum_{k=1}^{n-1}\frac{n-1}{k}a_{k}x^{n-1-k} \\
5&H(x)\gets \left(G(x)^{1/(n-1)}\right)^{-1}\bmod{x^{n-1}} \\
6&\textbf{return }\left((t^{-1}x) \circ \left(x\cdot H\right)\right)
\end{array}
$$

??? note "Predložak ([P5809【模板】多项式复合逆 (Predložak: kompozicijski inverz polinoma)](https://www.luogu.com.cn/problem/P5809))"
    Kôd je u odnosu na izvorni algoritam ponešto pojednostavljen i izmijenjen kako bi bio kraći.
    
    ```cpp
    --8<-- "docs/math/code/poly/comp-rev/rev_1.cpp"
    ```

### Izvod iz principa transpozicije

Problem Power Projection transponirani je problem modularne kompozicije (Modular Composition); Kinoshita i Li primijetili su da se gornji algoritam za kompoziciju može dobiti izravnom transpozicijom algoritma za Power Projection. Isto tako, ako se neka optimizacija može primijeniti na algoritam za Power Projection, može se primijeniti i na algoritam za modularnu kompoziciju. Detalje izostavljamo.

## Literatura

1.  Yasunori Kinoshita, Baitian Li.[Power Series Composition in Near-Linear Time](https://arxiv.org/abs/2404.05177). FOCS 2024.
2.  Alin Bostan, Ryuhei Mori.[A Simple and Fast Algorithm for Computing the N-th Term of a Linearly Recurrent Sequence](https://arxiv.org/abs/2008.08822). SOSA 2021: 118-132
3.  R. P. Brent and H. T. Kung. 1978.[Fast Algorithms for Manipulating Formal Power Series](https://doi.org/10.1145/322092.322099). J. ACM 25, 4 (Oct. 1978), 581–595.
4.  Daniel J. Bernstein. "[Fast multiplication and its applications](https://cr.yp.to/papers.html#multapps)." Pages 325–384 in Algorithmic number theory: lattices, number fields, curves and cryptography, edited by Joe Buhler, Peter Stevenhagen, Cambridge University Press, 2008, ISBN 978-0521808545.
