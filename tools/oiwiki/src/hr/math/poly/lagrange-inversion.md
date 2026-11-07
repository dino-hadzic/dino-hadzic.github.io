---
title: Lagrangeova inverzija
---

## Formalni Laurentovi redovi

Već poznajemo prsten formalnih redova potencija $\mathbb{C}\lbrack\lbrack x\rbrack\rbrack$; definirajmo prsten formalnih Laurentovih redova:

$$
\mathbb{C}\left(\left(x\right)\right):=\left\lbrace \sum_{k\geq N}a_kx^k : N\in\mathbb{Z},a_k\in \mathbb{C}\right\rbrace
$$

Po uzoru na definiciju multiplikativnog inverza formalnog reda potencija možemo definirati multiplikativni inverz elementa iz $\mathbb{C}\left(\left(x\right)\right)$:

ako za $f:=\sum_{k\geq N}f_kx^k$ uz $f_N\neq 0$ postoji $g=\sum_{k\geq -N}g_kx^k$ takav da je $fg=1$, tada je

$$
g_k:=
\begin{cases}
f_N^{-1}, &\text{ if }k=-N\text{,} \\
-f_N^{-1}\sum_{i> N}f_ig_{k-i}, &\text{ otherwise}
\end{cases}
$$

Slično kao kod formalnih redova potencija, za $f(x)=\sum_{k\geq N}f_kx^k$ različit od nule definiramo:

$$
\operatorname{ord} f:=\min\lbrace k:f_k\neq 0\rbrace
$$

Očito za $g\neq 0$ vrijedi

$$
\operatorname{ord} (fg)=\operatorname{ord}(f)+\operatorname{ord}(g)
$$

## Formalni reziduum

Formalni reziduum formalnog Laurentova reda jest koeficijent uz $x^{-1}$. Pišemo $\operatorname{res} f:=\lbrack x^{-1}\rbrack f$.

**Lema**: Za svaki formalni Laurentov red $f$ vrijedi $\operatorname{res} f'=0$.

**Dokaz**: Promotrimo definiciju formalne derivacije $\left(x^k\right)'=kx^{k-1}$.

**Lema**: Za sve formalne Laurentove redove $f,g$ vrijedi $\operatorname{res}(f'g)=-\operatorname{res}(fg')$.

**Dokaz**: Promotrimo pravilo za derivaciju produkta $(fg)'=f'g+fg'$, pa je $0=\operatorname{res}((fg)')=\operatorname{res}(f'g)+\operatorname{res}(fg')$.

**Lema**: Za formalni Laurentov red $f(x)\neq 0$ vrijedi $\operatorname{res}(f'/f)=\operatorname{ord}f$.

**Dokaz**: Neka je $\operatorname{ord}f=k$; tada je

$$
\begin{aligned}
\operatorname{res}\left(\frac{f'}{f}\right)&=\operatorname{res}\left(\frac{kf_kx^{k-1}+\cdots}{f_kx^k+f_{k+1}x^{k+1}+\cdots}\right) \\
&=\operatorname{res}\left(\frac{kf_kx^{-1}+\cdots}{f_k+f_{k+1}x+\cdots}\right) \\
&=k
\end{aligned}
$$

**Lema**: Za formalni Laurentov red $f$ i formalni red potencija $g\neq 0$ vrijedi $\operatorname{res}(f)\operatorname{ord}(g)=\operatorname{res}(f(g)g')$.

**Dokaz**: Zbog linearnosti dovoljno je dokazati slučaj $f=x^k$, gdje je $k\in\mathbb{Z}$. Ako je $k\neq -1$, tada je

$$
\begin{aligned}
\operatorname{res}x^k&=0 \\
\operatorname{res}(g^kg')&=\operatorname{res}\left(\frac{1}{k+1}\left(g^{k+1}\right)'\right) \\
&=\frac{1}{k+1}\operatorname{res}\left(\left(g^{k+1}\right)'\right) \\
&=0
\end{aligned}
$$

Ako je $k=-1$, tada je

$$
\begin{aligned}
\operatorname{res}f&=\operatorname{res}\left(x^{-1}\right)=1 \\
\operatorname{res}(f(g)g')&=\operatorname{res}(g'/g) \\
&=\operatorname{ord}(g) \\
&=\operatorname{res}(f)\operatorname{ord}(g)
\end{aligned}
$$

## Kompozicijski inverz

Pišemo $A(x)\circ B(x):=A(B(x))$.

**Tvrdnja**: $f(x):=\sum_{k\geq 1}f_kx^k$ ima kompozicijski inverz $f^{\langle -1\rangle}(x)$ ako i samo ako je $f(0)=0\neq f'(0)$, i tada je $f^{\langle -1\rangle}(x)$ jedinstven. Štoviše, ako $g(x)=\sum_{k\geq 1}g_kx^k$ zadovoljava $f(g(x))=x$ ili $g(f(x))=x$, tada je $g(x)=f^{\langle -1\rangle}(x)$.

**Dokaz**: Promotrimo

$$
\begin{aligned}
g(f(x))&=g_1(f_1x+f_2x^2+f_3x^3+\cdots ) \\
&+g_2(f_1x+f_2x^2+\cdots )^2 \\
&+g_3(f_1x+\cdots )^3 \\
&+\cdots \\
&=g_1f_1x+(g_1f_2+g_2f_1^2)x^2+(g_1f_3+2g_2f_1f_2+g_3f_1^3)x^3+\cdots
\end{aligned}
$$

Budući da je $g(f(x))=x$, dobivamo sljedeći sustav jednadžbi

$$
\begin{cases}
g_1f_1&=1 \\
g_1f_2+g_2f_1^2&=0 \\
g_1f_3+2g_2f_1f_2+g_3f_1^3&=0 \\
\vdots
\end{cases}
$$

Prvu jednadžbu možemo riješiti samo kad je $f_1\neq 0$, a zatim redom rješavamo $g_2,\dots$.

Posebno, promotrimo $f(h(x))=x$; tada je $g(f(h(x)))=g(x)$, pa je $g(x)=g\circ f\circ h(x)=x\circ h(x)=h(x)$.

## Lagrangeova formula inverzije

Neka $f(x),g(x)\in\mathbb{C}\lbrack\lbrack x\rbrack\rbrack$ zadovoljavaju $f(g(x))=g(f(x))=x$. Uzmimo $\Phi(x)\in\mathbb{C}\lbrack\lbrack x\rbrack\rbrack$ (ili $\Phi(x)\in\mathbb{C}\left(\left(x\right)\right)$); tada je

$$
\begin{aligned}
\lbrack x^n\rbrack\Phi(f(x))&=\lbrack x^{n-1}\rbrack\Phi(x)\frac{g'(x)}{g(x)}\left(\frac{x}{g(x)}\right)^n \\
&=\lbrack x^{-1}\rbrack\frac{\Phi(x)g'(x)}{g(x)^{n+1}}
\end{aligned}
$$

**Dokaz**:

$$
\begin{aligned}
\lbrack x^n\rbrack\Phi(f(x))&=\operatorname{res}\left(\frac{\Phi(f(x))}{x^{n+1}}\right) \\
&=\operatorname{res}\left(\frac{\Phi(f(g(x)))g'(x)}{g(x)^{n+1}}\right)\cdot \left(\operatorname{ord}(g(x))\right)^{-1} \\
&=\operatorname{res}\left(\frac{\Phi(x)g'(x)}{g(x)^{n+1}}\right)
\end{aligned}
$$

Nekim je čitateljima možda poznatija sljedeća inačica: za $k\in\mathbb{Z}_{\geq 0},n\in\mathbb{Z}_{>0}$ vrijedi

$$
\lbrack x^n\rbrack f(x)^k=\frac{k}{n}\lbrack x^{n-k}\rbrack\left(\frac{x}{g(x)}\right)^n
$$

ili

$$
\begin{aligned}
\lbrack x^n\rbrack \Phi(f(x))&=\frac{1}{n}\lbrack x^{n-1}\rbrack \Phi'(x)\left(\frac{x}{g(x)}\right)^n \\
&=\frac{1}{n}\lbrack x^{-1}\rbrack\frac{\Phi'(x)}{g(x)^n}
\end{aligned}
$$

Uočimo da je

$$
\begin{aligned}
\operatorname{res}\left(\frac{\Phi'(x)}{g(x)^n}-n\frac{\Phi(x)g'(x)}{g(x)^{n+1}}\right)&=\operatorname{res}\left(\left(\frac{\Phi(x)}{g(x)^n}\right)'\right) \\
&=0
\end{aligned}
$$

što se može izvesti iz onoga što smo već dokazali.

## Literatura

1.  Richard P. Stanley and Sergey P. Fomin. Enumerative Combinatorics Volume 2 (Edition 1).
2.  Ira M. Gessel. Lagrange Inversion.
