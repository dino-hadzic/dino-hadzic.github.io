---
title: Newton iteration for polynomials
---

## Description

Given a polynomial $G\left(x, y\right)$, it is known that a polynomial $f\left(x\right)$ satisfies:

$$
G\left(x, f\left(x\right)\right)\equiv 0\pmod{x^{n}}
$$

and that there exists a value $f_1$ such that $G\left(x, y\right)$ satisfies the following conditions:

-   $G(0, f_1) = 0$;
-   $\dfrac{\partial G}{\partial y}(0, f_1) \neq 0$.

Find $f\left(x\right)$ modulo $x^{n}$.

## Newton's Method

Consider doubling.

First, for $n=1$ the solution of $\left[x^{0}\right]G\left(x, f\left(x\right)\right)=0$ has to be found separately; the $f_1$ from the assumption is exactly such a solution.

Suppose we have already obtained the solution $f_{\left\lceil\frac{n}{2}\right\rceil}\left(x\right)$ modulo $x^{\left\lceil\frac{n}{2}\right\rceil}$, and we want the solution $f\left(x\right) = f_n\left(x\right)$ modulo $x^{n}$.

Expanding $G\left(x, f(x)\right)$ as a Taylor series in $f(x)$ around $f(x)=f_{\left\lceil\frac{n}{2}\right\rceil}\left(x\right)$, we get:

$$
\sum_{i=0}^{+\infty}\frac{\frac{\partial^i G}{\partial y^i}\left(x, f_{\left\lceil\frac{n}{2}\right\rceil}\left(x\right)\right)}{i!}\left(f\left(x\right)-f_{\left\lceil\frac{n}{2}\right\rceil}\left(x\right)\right)^{i}\equiv 0\pmod{x^{n}}
$$

Since the degree of the lowest nonzero term of $f\left(x\right)-f_{\left\lceil\frac{n}{2}\right\rceil}\left(x\right)$ is at least $\left\lceil\frac{n}{2}\right\rceil$, we have:

$$
\forall 2\leqslant i:\left(f\left(x\right)-f_{\left\lceil\frac{n}{2}\right\rceil}\left(x\right)\right)^{i}\equiv 0\pmod{x^{n}}
$$

Therefore:

$$
\begin{aligned}
\sum_{i=0}^{+\infty}\frac{\frac{\partial^i G}{\partial y^i}\left(x, f_{\left\lceil\frac{n}{2}\right\rceil}\left(x\right)\right)}{i!}\left(f\left(x\right)-f_{\left\lceil\frac{n}{2}\right\rceil}\left(x\right)\right)^{i}&\equiv G\left(x, f_{\left\lceil\frac{n}{2}\right\rceil}\left(x\right)\right)+\frac{\partial G}{\partial y}\left(x, f_{\left\lceil\frac{n}{2}\right\rceil}\left(x\right)\right)\left[f\left(x\right)-f_{\left\lceil\frac{n}{2}\right\rceil}\left(x\right)\right]\\
&\equiv 0\pmod{x^{n}}
\end{aligned}
$$

$$
f_n\left(x\right)\equiv f_{\left\lceil\frac{n}{2}\right\rceil}\left(x\right)-\frac{G\left(x, f_{\left\lceil\frac{n}{2}\right\rceil}\left(x\right)\right)}{\frac{\partial G}{\partial y}\left(x, f_{\left\lceil\frac{n}{2}\right\rceil}\left(x\right)\right)}\pmod{x^{n}}
$$

or

$$
f_{2n}\left(x\right)\equiv f_n\left(x\right)-\frac{G\left(x, f_n\left(x\right)\right)}{\frac{\partial G}{\partial y}\left(x, f_n\left(x\right)\right)}\pmod{x^{2n}}
$$

## Examples

### [Polynomial inverse](./elementary-func.md#多项式求逆)

Let the given function be $h\left(x\right)$; we have:

$$
G\left(x, y\right)=\frac{1}{y}-h\left(x\right)
$$

Applying Newton's Method gives:

$$
\begin{aligned}
    f_{2n}\left(x\right)&\equiv f_{n}\left(x\right)-\frac{1/f_{n}\left(x\right)-h\left(x\right)}{-1/f_{n}^{2}\left(x\right)}&\pmod{x^{2n}}\\
    &\equiv 2f_{n}\left(x\right)-f_{n}^{2}\left(x\right)h\left(x\right)&\pmod{x^{2n}}
\end{aligned}
$$

Time complexity

$$
T\left(n\right)=T\left(\frac{n}{2}\right)+O\left(n\log{n}\right)=O\left(n\log{n}\right)
$$

### [Polynomial square root](./elementary-func.md#多项式开方)

Let the given function be $h\left(x\right)$; we have:

$$
G\left(x, y\right)=y^{2}-h\left(x\right)\equiv 0
$$

Applying Newton's Method gives:

$$
\begin{aligned}
    f_{2n}\left(x\right)&\equiv f_{n}\left(x\right)-\frac{f_{n}^{2}\left(x\right)-h\left(x\right)}{2f_{n}\left(x\right)}&\pmod{x^{2n}}\\
    &\equiv\frac{f_{n}^{2}\left(x\right)+h\left(x\right)}{2f_{n}\left(x\right)}&\pmod{x^{2n}}
\end{aligned}
$$

Time complexity

$$
T\left(n\right)=T\left(\frac{n}{2}\right)+O\left(n\log{n}\right)=O\left(n\log{n}\right)
$$

### [Polynomial exponential](./elementary-func.md#多项式对数函数--指数函数)

Let the given function be $h\left(x\right)$; we have:

$$
G\left(x, y\right)=\ln{y}-h\left(x\right)
$$

Applying Newton's Method gives:

$$
\begin{aligned}
    f_{2n}\left(x\right)&\equiv f_{n}\left(x\right)-\frac{\ln{f_{n}\left(x\right)}-h\left(x\right)}{1/f_{n}\left(x\right)}&\pmod{x^{2n}}\\
    &\equiv f_{n}\left(x\right)\left(1-\ln{f_{n}\left(x\right)+h\left(x\right)}\right)&\pmod{x^{2n}}
\end{aligned}
$$

Time complexity

$$
T\left(n\right)=T\left(\frac{n}{2}\right)+O\left(n\log{n}\right)=O\left(n\log{n}\right)
$$

## Worked examples by hand

To make things easier to understand, here we demonstrate the flow of the algorithm on a few examples.

### Square root of a complex polynomial modulo a polynomial

Suppose $h$ is a complex polynomial not divisible by $x$ (it has a constant term), and we want its square root modulo $x^n$.

We have the equation:

$$
G\left(f(x)\right) = f^2(x)-h(x) \equiv 0\pmod{x^{n}}
$$

Taylor-expanding $G$ gives the following expression. Note that this is an expansion in $f$, so the derivatives are all partial derivatives with respect to $f$, and $x$ is treated as a constant here.

$$
G(f(x)) = \sum_{i=0}^{+\infty}\frac{G^{\left(i\right)}\left(f_{0}(x)\right)}{i!}\left(f(x)-f_{0}(x)\right)^{i}
= G(f_0(x)) + 2f_0(x)(f(x)-f_0(x)) + (f(x)-f_0(x))^2
$$

We compute by doubling. Suppose the intermediate results of the doubling are $f_0(x), f_1(x), \ldots, f_j(x)$, or, mathematically rigorously, $f_j(x)$ is a complex polynomial satisfying $G(f_j(x))\equiv 0\pmod{x^{2^j}}$ which, for uniqueness, also satisfies the following two conditions:

-   the degree of $f_{j}(x)$ does not exceed $x^{2^j}$;
-   $f_{j+k}(x)-f_j(x)\equiv 0\pmod{x^{2^j}}$ for all $k$.

Substituting $f_{j+1}(x)$ and $f_j(x)$ into the expression above gives:

$$
G(f_{j+1}(x)) = G(f_j(x)) + 2f_j(f_{j+1}(x)-f_j(x)) + (f_{j+1}(x)-f_{j}(x))^2  \equiv 0 \pmod{x^{2^{j+1}}}
$$

Clearly $f_{j+1}(x)-f_j(x)$ must be a multiple of $x^{2^j}$. Thus we get

$$
f_{j+1}(x) \equiv f_j(x) - \frac{f_j^2(x)-h(x)}{2f_j(x)} \equiv \frac{f_j(x)^2 + h(x)}{2f_j(x)} \pmod{x^{2^{j+1}}}
$$

If $f_j(x)$ exists, then $2f_j(x)$ is not divisible by $x$ (it has a constant term), so it necessarily has an inverse modulo $x^{2^{j+1}}$. Therefore the sequence $f_0,f_1\ldots,f_j$ exists if and only if $f_0$ exists. A complex polynomial $h(x)$ not divisible by $x$ always has a square root modulo $x$, because $h(x)$ modulo $x$ is just an ordinary nonzero complex number, which always has two square roots. So this algorithm can be applied to every $h(x)$ with a constant term.

Taking $h(x)=x+1$ as an example, the computation goes as follows:

-   $f_0(x)=1$,$f_1(x)=\dfrac{1^2+x+1}{2\times 1}\mod x^2 = \dfrac{1}{2}x+1$,$f_2(x)=\dfrac{\left(\dfrac{1}{2}x+1\right)^2+x+1}{2\times \left(\dfrac{1}{2}x+1\right)}\mod x^4 = \dfrac{1}{16}x^3-\dfrac{1}{8}x^2+\dfrac{1}{2}x+1$,$\ldots$
-   $f_0(x)=-1$,$f_1(x)=\dfrac{(-1)^2+x+1}{2\times (-1)}\mod x^2 = -\dfrac{1}{2}x-1$,$\ldots$ (equal to the negation of the previous one)

One can verify that both are correct sequences of modular square-root polynomials.

### Square root of an integer modulo a prime power

The Newton iteration algorithm can also be carried over to integers modulo a power of a prime.
Suppose $h$ is a "convenient" integer not divisible by 3. ("Convenient" means "a solution necessarily exists"; the exact condition is given later.) Suppose we want to compute the square root $f$ of $h$ modulo $3^n$. We have the equation:

$$
G\left(f\right) = f^2-h \equiv 0\pmod{3^{n}}
$$

Taylor-expanding $G$ gives:

$$
G(f) = \sum_{i=0}^{+\infty}\frac{G^{\left(i\right)}\left(f_{0}\right)}{i!}\left(f-f_{0}\right)^{i}
= G(f_0) + 2f_0(f-f_0) + (f-f_0)^2
$$

We compute by doubling. Suppose the intermediate results obtained in the doubling are $f_0, f_1, \ldots, f_j$, or, rigorously, $f_j$ is an integer satisfying $G(f_j)\equiv 0\pmod{3^{2^j}}$ which, for uniqueness, also satisfies the following two conditions:

-   $0 < f_{j} < 3^{2^j}$;
-   $f_{j+k}-f_j\equiv 0\pmod{3^{2^j}}$ for all $k$.

Substituting $f_{j+1}$ and $f_j$ into the expression above gives:

$$
G(f_{j+1}) = G(f_j) + 2f_j(f_{j+1}-f_j) + (f_{j+1}-f_{j})^2  \equiv 0 \pmod{3^{2^{j+1}}}
$$

Clearly $f_{j+1}-f_j$ must be a multiple of $3^{2^j}$. Thus we get

$$
f_{j+1} \equiv f_j - \frac{f_j^2-h}{2f_j} \equiv \frac{f_j^2 + h}{2f_j} \pmod{3^{2^{j+1}}}
$$

If $f_j$ exists, then $2f_j$ is not divisible by $3$, so it necessarily has an inverse modulo $3^{2^{j+1}}$. Therefore the sequence $f_0,f_1\ldots,f_j$ exists if and only if $f_0$ exists. An integer $h$ not divisible by 3 either has no square root modulo $3$ or has two. So the only condition for the whole algorithm to work is that $h$ has a square root modulo $3$.

Here we take $h=46$ as a concrete computation example.

-   $f_0=1$,$f_1=\dfrac{1^2+46}{2\times 1}\mod 9 = 1$,$f_2=\dfrac{1^2+46}{2\times 1}\mod 81 = 64$,$f_3=\dfrac{64^2+46}{2\times 64}\mod 6561 = 955$,$\ldots$
-   $f_0=2$,$f_1=\dfrac{2^2+46}{2\times 2}\mod 9 = 8$,$f_2=\dfrac{8^2+46}{2\times 8}\mod 81 = 17$,$f_3=\dfrac{17^2+46}{2\times 17}\mod 6561 = 5606$,$\ldots$ (equal to the negation of the previous one)

One can verify that both are correct sequences of modular square roots.

## Algebraic proof

This section extends the preceding text: in the language of abstract algebra we prove that as long as $f$ satisfies the initial-solution condition, Newton's method gives a solution for every $n$, and that all solutions can be obtained.

### Proof that a solution exists

???+ note "Lemma 1"
    Let an [integral domain](../algebra/ring-theory.md#整环) $R$ have a polynomial or [formal power series](../algebra/ring-theory.md#形式幂级数环) $f(X) = \sum_{i\geq 0}a_iX^i$ and $r,p\in R$ such that $f(r)\in Rp$ (that is, $r$ is a root of $f(X)$ modulo $p$) and $f'(r)\in R$ is invertible modulo $p$. Here $f'(X) := \sum_{i\geq 0}(i+1)a_{i+1}X^i$ is the **formal derivative** of $f(X)$. Then $f\left(r-\dfrac{f(r)}{f'(r)}\right) \equiv 0\pmod {p^2}$.

??? note "Proof"
    For every $s\in R$,
    
    $$
    \begin{aligned}
    f(r+sp) &= \sum_{i\geq 0}a_i(r+sp)^i \\
    &= \sum_{i\geq 0}a_ir^i + sp\sum_{i\geq 1}ia_ir^{i-1} + s^2p^2\left(\ldots\right) \\
    &= f(r) + spf'(r) + s^2p^2\left(\frac{f''(r)}{2!} + \cdots\right),
    \end{aligned}
    $$
    
    so
    
    $$
    f(r+sp) \in Rp^2 \iff f(r)+f'(r)sp \in Rp^2
    $$
    
    Since $f(r)\in Rp$ and $f'(r)$ is invertible, it suffices to take $sp = -\dfrac{f(r)}{f'(r)}$, where $\dfrac{1}{f'(r)}$ is the inverse modulo $p^2$. Because $f'(r)$ is invertible modulo $p$, it necessarily also has an inverse modulo $p^2$: let $a,b,c\in R$ be such that $af'(r) = bp+1$ and $f(r)=cp$; then $\left(a^2f'(r)-2\right)f'(r) = b^2p^2+1$, so we can take $s=c(2-a^2f'(r))$.

For the polynomial ring $k[X]$ over a field $k$, let $G(X, Y)\in k[X, Y]$ and $f_n\in k[X]$ be such that $G(X, f_n(X))\in k[X]X^n$; then applying Lemma 1 gives

$$
G\left(X, f_n(X) - \frac{G(X, f_n(X))}{\frac{\partial G}{\partial Y}(X, f_n(X))} \right)\equiv 0 \pmod {X^{2n}}
$$

For the initial condition of the doubling it suffices to have $f_1\in k$ such that $G(X, f_1)\equiv 0\pmod X$ and $\dfrac{\partial G}{\partial Y}(X, f_1)\not\equiv 0\pmod X$. The latter condition guarantees that $\dfrac{\partial G}{\partial Y}$ has a nonzero constant term, and since $X\left| \dfrac{G(X, f_n(X))}{\frac{\partial G}{\partial Y}(X, f_n(X))} \right.$, for every $n$ the value $\dfrac{\partial G}{\partial Y}(X, f_n)$ is always invertible modulo $X^n$, which satisfies the condition for the next iteration.

### Proof that all solutions are obtained

???+ note "Lemma 2"
    Let $R$ be a [UFD](../algebra/ring-theory.md#唯一分解整环), with $f,r,p$ defined as in Lemma 1. Then the $r-\dfrac{f(r)}{f'(r)}$ given by Lemma 1 is the unique value of $x$ modulo $p^{2}$ satisfying the following two conditions:
    
    -   $f(x)\in Rp^{2}$
    -   $x-r\in Rp$
    
    that is,
    
    $$
    \forall x\in R,\qquad p^2\mid f(x)\wedge p\mid (x-r) \implies x\equiv r-\dfrac{f(r)}{f'(r)} \pmod {p^2}
    $$

??? note "Proof"
    Let $s = -\dfrac{f(r)}{f'(r)p}$ and $u = r+sp$; Lemma 1 guarantees that $u$ satisfies both conditions and that $f(r) + f'(r)sp \in Rp^{2}$.
    Let $v$ be a value satisfying the above conditions; then $v = r+tp$ and $f(r) + f'(r)tp \in Rp^{2}$.
    Hence $f'(r)(t-s)p\in Rp^{2}$ and $v-u\in Rp^{2}$.

Newton's method is guaranteed to obtain all solutions modulo $X^{2^n}$. Suppose $G(X, h)\equiv 0\pmod {X^{2^n}}$; let $h_{2^i} := h\pmod {X^{2^i}}$, then take $f_1 = h_1$ and apply Newton's method; by Lemma 2 we get $f_{2^i} \equiv h_{2^i}\pmod {X^{2^i}}$, so necessarily $f_{2^n} = h$.

The argument above also shows that when $\dfrac{\partial G}{\partial y}(0, y)$ is always invertible, the number of solutions of $G(X, f)\equiv 0\pmod {X^n}$ equals the number of solutions of $G(0, f)\equiv 0\pmod X$. This conclusion is not trivial. See the following example.

??? example "An example where Newton's method fails and the number of solutions grows with the degree"
    Modulo $X$ the only square root of $X^2$ is $0$, but modulo $X^4$ the square roots of $X^2$ are $X, -X, X^3+X, \ldots$
