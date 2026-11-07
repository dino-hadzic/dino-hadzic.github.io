---
title: Composition and compositional inverse of formal power series
---

Composition and compositional inversion of formal power series are also common operations on formal power series. For $f$ without special properties, to compute $f(g) \bmod{x^n}$ where $f\in\mathbb{C}\left\lbrack\left\lbrack x\right\rbrack\right\rbrack,g\in x\mathbb{C}\left\lbrack\left\lbrack x\right\rbrack\right\rbrack$ we have so far mostly used an $O\left(n^2\right)$ algorithm (which still needs FFT), but because of its low efficiency it was rarely applied. We present the $O\left(\mathsf{M}\left(n\right)\log n\right)$ algorithm of Kinoshita and Li, where $O\left(\mathsf{M}\left(n\right)\right)$ is the time needed to multiply two polynomials of degree $O\left( n\right)$.

## Composition of formal power series / polynomials

To compute $f\left(g\left(x\right)\right)\bmod{x^n}$, every coefficient of $f\left(g\left(x\right)\right)$ must be a sum of finitely many terms, which is why we previously required $f(x)\in\mathbb{C}\left\lbrack\left\lbrack x\right\rbrack\right\rbrack,g(x)\in x\mathbb{C}\left\lbrack\left\lbrack x\right\rbrack\right\rbrack$; however, $f(x),g(x)\in\mathbb{C}\left\lbrack x\right\rbrack$ also satisfies this condition. Since we need to truncate the coefficients of $f\left(g\left(x\right)\right)$ anyway, we may directly consider the case where $f(x),g(x)$ are both polynomials. For $f(x)=\sum_{j=0}^{n-1}f_jx^j$ we have

$$
f\left(g\left(x\right)\right)=\sum_{j=0}^{n-1}f_jg\left(x\right)^j
$$

We consider the rational function over the ring $\mathbb{C}\left\lbrack x\right\rbrack\left(\left( y\right)\right)$

$$
\begin{aligned}
\frac{f\left(y^{-1}\right)}{1-y\cdot g(x)}&=\sum_{j\geq 0}\left(\cdots +f_jy^{-j}+\cdots\right)g(x)^jy^j \\
f\left(g\left(x\right)\right)&=\left\lbrack y^0\right\rbrack\frac{f\left(y^{-1}\right)}{1-y\cdot g(x)}
\end{aligned}
$$

Following the Bostan–Mori algorithm mentioned in [Homogeneous linear recurrence with constant coefficients](./linear-recurrence.md), Kinoshita and Li pointed out that it can be modified into a bivariate form:

$$
\begin{aligned}
\frac{P\left(y\right)}{Q\left(x,y\right)}\bmod{x^n}&=\left(\frac{P\left(y\right)}{Q\left(x,y\right)Q\left(-x,y\right)}\bmod{x^n}\right)Q\left(-x,y\right)\bmod{x^n} \\
&=\left(\frac{P(y)}{V(x^2,y)}\bmod{x^n}\right)Q\left(-x,y\right)\bmod{x^n} \\
&=\left.\left(\frac{P(y)}{V(z,y)}\bmod{z^{\left\lceil n/2\right\rceil}}\right)\right|_{z=x^2}Q\left(-x,y\right)\bmod{x^n}
\end{aligned}
$$

In this recursive computation, when $n=1$ we only need to compute

$$
\frac{P(y)}{Q(x,y)}\bmod{x}=\frac{P(y)}{Q(0,y)}\in\mathbb{C}\left(\left( y\right)\right)
$$

When computing $\dfrac{P(y)}{V(z,y)}\bmod{z^{\left\lceil n/2\right\rceil}}\in\mathbb{C}\left\lbrack z\right\rbrack\left(\left( y\right)\right)$ we do not need to keep all coefficients in $y$: in the end we only extract the coefficient of $y^0$, so the coefficients of $y^{>0}$ are not needed, and since after computing the former we have to multiply it by several "**polynomials**" of the form $Q(-x,y)\in\mathbb{C}\left\lbrack x,y\right\rbrack$, it suffices to keep only the coefficients that contribute to $y^0$. We are ready to give the pseudocode:

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

Then we have

$$
f\left(g\left(x\right)\right)\bmod{x^n}=\operatorname{\mathsf{Comp}}\left(f\left(y^{-1}\right),1-y\cdot g(x),\max\left\lbrace 1+\deg f,n\right\rbrace ,1\right)\bmod{x^n}
$$

Note that the third argument is chosen this way because $g(0)$ may be nonzero: if $\deg f\geq n$, we cannot truncate $f(x)$ when computing $f\left(g(x)\right)$. Alternatively, we may compute $f(g)=f\circ \left(x+g(0)\right)\circ \left(g-g(0)\right)$; then we can take $F:=f\left(x+g(0)\right)\bmod{x^n}$ and $G:=g-g(0)$ and instead compute $\operatorname{\mathsf{Comp}}\left(F\left(y^{-1}\right),1-y\cdot G(x),n,1\right)$.

Moreover, because of the restrictions on the calls, $Q(0,y)^{-1}$ at the end of the recursion can be derived directly and does not need to be computed by the algorithm for the multiplicative inverse of a formal power series; we only need one multiplication and then extract the required coefficients.

## Common special forms of composition

All the commonly used [elementary functions of polynomials](./elementary-func.md) can be computed via composition:

$$
\begin{aligned}
g(0)=1&,\space g^{-1}=1+(1-g)+(1-g)^2+\cdots \\
g(0)=1&,\space \log g=-\dfrac{1-g}{1}-\dfrac{(1-g)^2}{2}-\dfrac{(1-g)^3}{3}-\cdots \\
g(0)=0&,\space \exp g=1+\dfrac{g}{1!}+\dfrac{g^2}{2!}+\dfrac{g^3}{3!}+\cdots \\
g(0)=1&,\space g^e=1+\dfrac{e}{1!}(g-1)+\dfrac{e(e-1)}{2!}(g-1)^2+\cdots
\end{aligned}
$$

We will also use the power function when computing the compositional inverse.

### Kronecker substitution

Before analyzing the time complexity, let us first consider how to multiply bivariate polynomials. One idea is to "pack" the coefficients; this method was introduced by Kronecker in 1882, reducing multiplication in $R\left\lbrack x,y\right\rbrack$ to multiplication in $R\left\lbrack x\right\rbrack$ via $y\mapsto x^N$, provided that $N$ is large enough.

Suppose $\deg_x \left(AB\right)<N$; then after computing $A\left(x,x^N\right)B\left(x,x^N\right)$ we can still recover $A(x,y)B(x,y)$, and "packing" and "unpacking" take linear time.

It suffices to apply Kronecker substitution and then perform univariate polynomial multiplication. It is easy to see that when $n$ is a power of two the above algorithm runs in $O\left(\mathsf{M}\left(n\right)\log n\right)$ time, because in every level of the recursion the degree in $y$ doubles while the degree in $x$ halves.

??? note "Template ([P5373【模板】多项式复合函数 (Template: polynomial composition)](https://www.luogu.com.cn/problem/P5373))"
    Compared with the original algorithm, the code has been somewhat simplified and modified to make it shorter.
    
    ```cpp
    --8<-- "docs/math/code/poly/comp-rev/comp_1.cpp"
    ```

## Compositional inverse of a formal power series

Given $f\in x\mathbb{C}\left\lbrack\left\lbrack x\right\rbrack\right\rbrack$ with $f'(0)\neq 0$, find $g(x)\bmod{x^n}$ such that $f(g)\equiv g(f)\equiv x\pmod{x^n}$.

By [Lagrange inversion](./lagrange-inversion.md), for $n>1,k\geq 0$ we have

$$
\left\lbrack x^{n-1}\right\rbrack f(x)^k=\frac{k}{n-1}\left\lbrack x^{n-1-k}\right\rbrack \left(\frac{g(x)}{x}\right)^{-(n-1)}
$$

That is, if we can compute $\left\lbrack x^{n-1}\right\rbrack f(x)^k$ for $k=0,1,\dots ,n-1$, then we can compute the compositional inverse.

Kinoshita and Li pointed out that we can consider the bivariate rational function

$$
\frac{1}{1-y\cdot f(x)}=\sum_{j\geq 0}f(x)^jy^j
$$

and this problem has a more general form, the Power Projection problem: we want to compute

$$
u:=\left\lbrack x^{n-1}\right\rbrack\frac{P(x,y)}{Q(x,y)}\bmod{y^m}
$$

When $n-1=0$ we obviously have $u=\dfrac{P(0,y)}{Q(0,y)}\bmod{y^m}$; otherwise we have

$$
\frac{P(x,y)}{Q(x,y)}=\frac{P(x,y)Q(-x,y)}{Q(x,y)Q(-x,y)}=\frac{U_e\left(x^2,y\right)+xU_o\left(x^2,y\right)}{V\left(x^2,y\right)}
$$

so

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

We give the pseudocode:

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

Likewise, we can derive $Q(0,y)^{-1}$ directly without computing the multiplicative inverse of a formal power series, so the algorithm for the compositional inverse is

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

??? note "Template ([P5809【模板】多项式复合逆 (Template: compositional inverse of a polynomial)](https://www.luogu.com.cn/problem/P5809))"
    Compared with the original algorithm, the code has been somewhat simplified and modified to make it shorter.
    
    ```cpp
    --8<-- "docs/math/code/poly/comp-rev/rev_1.cpp"
    ```

### Derivation from the transposition principle

The Power Projection problem is the transpose of Modular Composition; Kinoshita and Li pointed out that the composition algorithm above can be obtained directly by transposing the Power Projection algorithm. Likewise, if an optimization can be applied to the Power Projection algorithm, it can also be applied to the Modular Composition algorithm. We omit the details.

## References

1.  Yasunori Kinoshita, Baitian Li.[Power Series Composition in Near-Linear Time](https://arxiv.org/abs/2404.05177). FOCS 2024.
2.  Alin Bostan, Ryuhei Mori.[A Simple and Fast Algorithm for Computing the N-th Term of a Linearly Recurrent Sequence](https://arxiv.org/abs/2008.08822). SOSA 2021: 118-132
3.  R. P. Brent and H. T. Kung. 1978.[Fast Algorithms for Manipulating Formal Power Series](https://doi.org/10.1145/322092.322099). J. ACM 25, 4 (Oct. 1978), 581–595.
4.  Daniel J. Bernstein. "[Fast multiplication and its applications](https://cr.yp.to/papers.html#multapps)." Pages 325–384 in Algorithmic number theory: lattices, number fields, curves and cryptography, edited by Joe Buhler, Peter Stevenhagen, Cambridge University Press, 2008, ISBN 978-0521808545.
