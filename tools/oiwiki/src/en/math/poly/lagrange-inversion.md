---
title: Lagrange inversion
---

## Formal Laurent series

We already know the ring of formal power series $\mathbb{C}\lbrack\lbrack x\rbrack\rbrack$; let us define the ring of formal Laurent series:

$$
\mathbb{C}\left(\left(x\right)\right):=\left\lbrace \sum_{k\geq N}a_kx^k : N\in\mathbb{Z},a_k\in \mathbb{C}\right\rbrace
$$

Following the definition of the multiplicative inverse of a formal power series, we can define the multiplicative inverse of an element of $\mathbb{C}\left(\left(x\right)\right)$:

if for $f:=\sum_{k\geq N}f_kx^k$ with $f_N\neq 0$ there exists $g=\sum_{k\geq -N}g_kx^k$ such that $fg=1$, then

$$
g_k:=
\begin{cases}
f_N^{-1}, &\text{ if }k=-N\text{,} \\
-f_N^{-1}\sum_{i> N}f_ig_{k-i}, &\text{ otherwise}
\end{cases}
$$

Similarly to formal power series, for nonzero $f(x)=\sum_{k\geq N}f_kx^k$ we define:

$$
\operatorname{ord} f:=\min\lbrace k:f_k\neq 0\rbrace
$$

Obviously, for $g\neq 0$ we have

$$
\operatorname{ord} (fg)=\operatorname{ord}(f)+\operatorname{ord}(g)
$$

## Formal residue

The formal residue of a formal Laurent series is the coefficient of $x^{-1}$. We write $\operatorname{res} f:=\lbrack x^{-1}\rbrack f$.

**Lemma**: For any formal Laurent series $f$ we have $\operatorname{res} f'=0$.

**Proof**: Consider the definition of the formal derivative $\left(x^k\right)'=kx^{k-1}$.

**Lemma**: For any formal Laurent series $f,g$ we have $\operatorname{res}(f'g)=-\operatorname{res}(fg')$.

**Proof**: Consider the product rule $(fg)'=f'g+fg'$, so $0=\operatorname{res}((fg)')=\operatorname{res}(f'g)+\operatorname{res}(fg')$.

**Lemma**: For a formal Laurent series $f(x)\neq 0$ we have $\operatorname{res}(f'/f)=\operatorname{ord}f$.

**Proof**: Let $\operatorname{ord}f=k$; then

$$
\begin{aligned}
\operatorname{res}\left(\frac{f'}{f}\right)&=\operatorname{res}\left(\frac{kf_kx^{k-1}+\cdots}{f_kx^k+f_{k+1}x^{k+1}+\cdots}\right) \\
&=\operatorname{res}\left(\frac{kf_kx^{-1}+\cdots}{f_k+f_{k+1}x+\cdots}\right) \\
&=k
\end{aligned}
$$

**Lemma**: For a formal Laurent series $f$ and a formal power series $g\neq 0$ we have $\operatorname{res}(f)\operatorname{ord}(g)=\operatorname{res}(f(g)g')$.

**Proof**: By linearity, it suffices to prove the case $f=x^k$ where $k\in\mathbb{Z}$. If $k\neq -1$, then

$$
\begin{aligned}
\operatorname{res}x^k&=0 \\
\operatorname{res}(g^kg')&=\operatorname{res}\left(\frac{1}{k+1}\left(g^{k+1}\right)'\right) \\
&=\frac{1}{k+1}\operatorname{res}\left(\left(g^{k+1}\right)'\right) \\
&=0
\end{aligned}
$$

If $k=-1$, then

$$
\begin{aligned}
\operatorname{res}f&=\operatorname{res}\left(x^{-1}\right)=1 \\
\operatorname{res}(f(g)g')&=\operatorname{res}(g'/g) \\
&=\operatorname{ord}(g) \\
&=\operatorname{res}(f)\operatorname{ord}(g)
\end{aligned}
$$

## Compositional inverse

We write $A(x)\circ B(x):=A(B(x))$.

**Proposition**: $f(x):=\sum_{k\geq 1}f_kx^k$ has a compositional inverse $f^{\langle -1\rangle}(x)$ if and only if $f(0)=0\neq f'(0)$, and in that case $f^{\langle -1\rangle}(x)$ is unique. Moreover, if $g(x)=\sum_{k\geq 1}g_kx^k$ satisfies $f(g(x))=x$ or $g(f(x))=x$, then $g(x)=f^{\langle -1\rangle}(x)$.

**Proof**: Consider

$$
\begin{aligned}
g(f(x))&=g_1(f_1x+f_2x^2+f_3x^3+\cdots ) \\
&+g_2(f_1x+f_2x^2+\cdots )^2 \\
&+g_3(f_1x+\cdots )^3 \\
&+\cdots \\
&=g_1f_1x+(g_1f_2+g_2f_1^2)x^2+(g_1f_3+2g_2f_1f_2+g_3f_1^3)x^3+\cdots
\end{aligned}
$$

Since $g(f(x))=x$, we obtain the following system of equations

$$
\begin{cases}
g_1f_1&=1 \\
g_1f_2+g_2f_1^2&=0 \\
g_1f_3+2g_2f_1f_2+g_3f_1^3&=0 \\
\vdots
\end{cases}
$$

We can solve the first equation only when $f_1\neq 0$, and then solve for $g_2,\dots$ in turn.

In particular, consider $f(h(x))=x$; then $g(f(h(x)))=g(x)$, and hence $g(x)=g\circ f\circ h(x)=x\circ h(x)=h(x)$.

## Lagrange inversion formula

Let $f(x),g(x)\in\mathbb{C}\lbrack\lbrack x\rbrack\rbrack$ satisfy $f(g(x))=g(f(x))=x$. Take $\Phi(x)\in\mathbb{C}\lbrack\lbrack x\rbrack\rbrack$ (or $\Phi(x)\in\mathbb{C}\left(\left(x\right)\right)$); then

$$
\begin{aligned}
\lbrack x^n\rbrack\Phi(f(x))&=\lbrack x^{n-1}\rbrack\Phi(x)\frac{g'(x)}{g(x)}\left(\frac{x}{g(x)}\right)^n \\
&=\lbrack x^{-1}\rbrack\frac{\Phi(x)g'(x)}{g(x)^{n+1}}
\end{aligned}
$$

**Proof**:

$$
\begin{aligned}
\lbrack x^n\rbrack\Phi(f(x))&=\operatorname{res}\left(\frac{\Phi(f(x))}{x^{n+1}}\right) \\
&=\operatorname{res}\left(\frac{\Phi(f(g(x)))g'(x)}{g(x)^{n+1}}\right)\cdot \left(\operatorname{ord}(g(x))\right)^{-1} \\
&=\operatorname{res}\left(\frac{\Phi(x)g'(x)}{g(x)^{n+1}}\right)
\end{aligned}
$$

Some readers may be more familiar with the following version: for $k\in\mathbb{Z}_{\geq 0},n\in\mathbb{Z}_{>0}$ we have

$$
\lbrack x^n\rbrack f(x)^k=\frac{k}{n}\lbrack x^{n-k}\rbrack\left(\frac{x}{g(x)}\right)^n
$$

or

$$
\begin{aligned}
\lbrack x^n\rbrack \Phi(f(x))&=\frac{1}{n}\lbrack x^{n-1}\rbrack \Phi'(x)\left(\frac{x}{g(x)}\right)^n \\
&=\frac{1}{n}\lbrack x^{-1}\rbrack\frac{\Phi'(x)}{g(x)^n}
\end{aligned}
$$

Note that

$$
\begin{aligned}
\operatorname{res}\left(\frac{\Phi'(x)}{g(x)^n}-n\frac{\Phi(x)g'(x)}{g(x)^{n+1}}\right)&=\operatorname{res}\left(\left(\frac{\Phi(x)}{g(x)^n}\right)'\right) \\
&=0
\end{aligned}
$$

which can be derived from what we have already proved.

## References

1.  Richard P. Stanley and Sergey P. Fomin. Enumerative Combinatorics Volume 2 (Edition 1).
2.  Ira M. Gessel. Lagrange Inversion.
