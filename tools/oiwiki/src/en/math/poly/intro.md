---
title: Introduction to polynomials and generating functions
---

## Polynomials and generating functions

Manipulating polynomials with finitely or infinitely many terms is an important part of the mathematics used in OI, especially in generating functions.

Polynomial algorithms built on the [fast Fourier transform](./fft.md) give competitive programmers the ability to manipulate generating functions directly.

## Basic concepts

For a sum $\sum a_nx^n$: if finitely many terms are added, it is called a polynomial and written $f(x)=\sum_{n=0}^m a_nx^n$.

A sum of countably many terms is called a series. In the sum $\sum_{n=0}^\infty a_nx^n$, every term is a power with a nonnegative integer exponent multiplied by a constant coefficient; a series of this form is called a power series.

When studying polynomial arithmetic we first consider the simpler polynomials; the notion of a power series is only used to aid understanding. Mathematical analysis goes on to study the convergence of power series.

For the general definitions of rings, fields, and the structures derived from them, see [Basic concepts of abstract algebra](../algebra/basic.md).

For a general ring $R$, the **polynomial ring** $R[x]$ over $R$ is defined.

Each element $f$ is called a **polynomial** over $R$ and can be represented as

$$
f=\left<f_0,f_1,f_2,\cdots,f_n\right>\quad(f_0,f_1,f_2,\cdots,f_n\in R)
$$

In other words, we define a polynomial directly as a sequence of coefficients. It can also be written as

$$
f(x)=f_0+f_1x+f_2x^2+\cdots+f_nx^n
$$

Here we regard $x$ merely as a **formal symbol**, a marker for the position of a coefficient.

If we also allow infinitely many terms, i.e.

$$
f(x)=f_0+f_1x+f_2x^2+\cdots
$$

we obtain the **formal power series ring** $R[[x]]$, each of whose elements $f$ is called a **formal power series**, abbreviated below to power series.

### Degree of a polynomial

For a polynomial $f(x)$, the degree of its highest-degree term is called the **degree** of the polynomial, written $\operatorname{deg}{f}$.

### Polynomial multiplication

The most fundamental operation is the multiplication of two polynomials, i.e. given polynomials $f(x)$ and $g(x)$:

$$
\begin{alignedat}{3}
f(x)&=a_0+a_1x+\dots+a_nx^n\quad \quad &(1)\\
g(x)&=b_0+b_1x+\dots+b_mx^m\quad \quad &(2)
\end{alignedat}
$$

we want to compute the polynomial $Q(x)=f(x)\cdot g(x)$:

$$
\boxed {Q(x) = \sum \limits_ {i = 0} ^ n \sum \limits_ {j = 0 } ^ m a_i b_j x ^ {i + j}} = c_0 + c_1 x + \dots + c_ {n + m} x ^ {n + m}
$$

Multiplication of polynomials or power series is associative and distributive over addition. If $R$ is a commutative ring or a ring with identity, multiplication is correspondingly commutative or has an identity element.

If a $2^n$-th root of unity exists over $R$, the [fast Fourier transform](./fft.md) allows us to compute the product of two polynomials of degree $2^n$ in $O(n2^n)$ time instead of $O(2^{2n})$.

### Composition

Define the power of an element $f$ of $R[[x]]$ as

$$
f^1=f,f^k=f^{k-1}\times f
$$

On this basis, define the composition of elements $f,g$ of $R[[x]]$ as

$$
(f\circ g)(x)=f(g(x))=f_0+\sum_{k=1}^{+\infty}f_kg^k(x)
$$

We stipulate that $f\circ g$ exists if and only if $f$ has finitely many terms or $g_0=0$, so that no limits over $R$ are involved.

$\circ$ is associative (when both $(f\circ g)\circ h$ and $f\circ (g\circ h)$ exist) and not commutative. When $R$ is a ring with identity, $\circ$ has the identity element $1\times x$.

Polynomial composition (and compositional inverse) has a $\Theta(n\log^2 n)$ algorithm, proposed in 2024 by Yasunori Kinoshita and Li Baitian (李白天); see [Composition of formal power series | compositional inverse](./comp-rev.md).

### Derivative

Although limits need not even exist in a general ring,  
we can still define the **formal derivative** of a formal power series as

$$
\left(\sum_{k=0}^{+\infty}f_kx^k\right)'=\sum_{k=1}^{+\infty}kf_kx^{k-1}
$$

where

$$
kf_k=\underbrace{f_k+f_k+\cdots+f_k}_{k \text{ copies of } f_k}
$$

The basic differentiation rules — the sum rule, the product rule, and the chain rule (when composition is allowed) — remain valid.

If division is allowed over $R$, the **formal indefinite integral** of a formal power series can be defined similarly.

### Multiplicative inverse

From the example

$$
\dfrac{1}{1-x}=1+x+x^2+\cdots
$$

we can see that the reciprocal of a polynomial can be expanded into an infinite series. The reciprocal exists if and only if the constant term is not $0$, and the reciprocal's constant term is not $0$ either.

Hence we define: for a formal power series $f$ with $f_0\not=0$, its **multiplicative inverse** $f^{-1}$ is another formal power series satisfying

$$
f\times f^{-1}=f^{-1}\times f=1
$$

Expanding this identity using the definition of formal power series multiplication, we obtain a recurrence for the coefficients of $f^{-1}$

$$
f^{-1}_0=\dfrac{1}{f_0},f^{-1}_n=\dfrac{-1}{f_0}\sum_{k=0}^{n-1}f^{-1}_kf_{n-k}
$$

Computing the first $n$ terms directly with the recurrence takes $O(n^2)$; [using the FFT](./elementary-func.md#多项式求逆) gives an $O(n\log n)$ algorithm.

???+ note "Note"
    It is easy to see that the reciprocal of $f(x)$ is just the infinite Maclaurin expansion of $\frac{1}{f(x)}$ (the infinite Taylor expansion at $x=0$).

### Common power series expansions

In mathematical analysis, a univariate function that is differentiable a certain number of times at some point or on some interval can be expanded into a polynomial on the corresponding region; this is generally called a Taylor expansion, and if the expansion is at $0$, it is also called a Maclaurin expansion.

If the function is infinitely differentiable, it can be expanded into a power series. The most common case is still the expansion at $0$.

In complex analysis, some functions cannot be Taylor-expanded at singularities, but they can be expanded into Laurent series.

The following identities hold only when the power series converges, and fail when it does not. Here we only write down the expansions without discussing the region of convergence.

There are two basic expansions, the exponential function and the power function:

$$
\mathrm{e}^x=1+x+\frac{1}{2!}x^2+\ldots+\frac{1}{n!}x^n+\ldots
$$

$$
(1+x)^a=1+ax+\frac{a(a-1)}{2!}x^2+\ldots+\frac{a(a-1)\ldots(a-n+1)}{n!}x^n+\ldots
$$

More expansions are often obtained by transforming the two above. For example, cosine and sine are obtained by substituting complex numbers into the exponential function:

$$
\cos x=1-\frac{1}{2!}x^2+\frac{1}{4!}x^4+\ldots+\frac{(-1)^n}{(2n)!}x^{2n}+\ldots
$$

$$
\sin x=x-\frac{1}{3!}x^3+\frac{1}{5!}x^5+\ldots+\frac{(-1)^n}{(2n+1)!}x^{2n+1}+\ldots
$$

The logarithm, arctangent, and arcsine are obtained by integration:

$$
\frac{1}{1+x}=1-x+x^2+\ldots+{(-1)}^n x^n+\ldots
$$

$$
\ln(1+x)=x-\frac{1}{2}x^2+\frac{1}{3}x^3+\ldots+\frac{{(-1)}^{n-1}}{n}x^n+\ldots
$$

$$
\frac{1}{1+x^2}=1-x^2+x^4+\ldots+{(-1)}^n x^{2n}+\ldots
$$

$$
\arctan x=x-\frac{1}{3}x^3+\frac{1}{5}x^5+\ldots+\frac{{(-1)}^{n}}{2n+1}x^{2n+1}+\ldots
$$

$$
\frac{1}{\sqrt{1+x}}=1-\frac{1}{2}x+\frac{3}{8}x^2+\ldots+{(-1)}^n\frac{(2n)!}{{(n!)}^2 4^n} x^{n}+\ldots
$$

$$
\frac{1}{\sqrt{1-x^2}}=1+\frac{1}{2}x^2+\frac{3}{8}x^4+\ldots+\frac{(2n)!}{{(n!)}^2 4^n} x^{2n}+\ldots
$$

$$
\arcsin x=x+\frac{1}{6}x^3+\frac{3}{40}x^5+\ldots+\frac{(2n)!}{{(n!)}^2(2n+1)4^n} x^{2n+1}+\ldots
$$

### Compositional inverse

The **compositional inverse** (compound inversion) is the generalization of the notion of an inverse function to the ring of formal power series.

For a formal power series $f$ satisfying $f_0=0$ and $f_1\not=0$, its compositional inverse is the formal power series $g$ satisfying $g(f(x))=f(g(x))=x$. By Lagrange inversion, for all integers $n,k$ we have

$$
n[x^n]f^k=k[x^{n-k}]\left(\dfrac{x}{g}\right)^n
$$

where $[x^k]f(x)$ denotes the coefficient of $x^k$ in $f(x)$.

### Polynomial divisibility

For polynomials $f(x)$ and $g(x)$, if there exists a polynomial $h(x)$ such that:

$$
f(x)=g(x)h(x)
$$

then the polynomial $g(x)$ divides the polynomial $f(x)$.

Obviously, the polynomial $g(x)$ divides the polynomial $f(x)$ if and only if all roots of $g(x)$ are roots of $f(x)$ and their multiplicities in $g(x)$ do not exceed the corresponding multiplicities in $f(x)$.

### Remainder and quotient of polynomials

For polynomials $f(x), g(x)$ there exist **unique** $Q(x), R(x)$ satisfying:

$$
\begin{aligned}
    f(x) &= Q(x) g(x) + R(x) \\
    \operatorname{deg}{R} &< \operatorname{deg}{g}
\end{aligned}
$$

When $\operatorname{deg}{f} \ge \operatorname{deg}{g}$ we have $\operatorname{deg}{Q} = \operatorname{deg}{f} - \operatorname{deg}{g}$, otherwise $Q(x) = 0$. We call $Q(x)$ the **quotient** of $f(x)$ divided by $g(x)$, and $R(x)$ the **remainder** of $f(x)$ divided by $g(x)$.

## Polynomials modulo a polynomial

Polynomials modulo a polynomial form a subring of the polynomial ring, obtained by dividing the polynomial ring by the equivalence relation of congruence.

In the division with remainder mentioned above, the polynomial $f(x)$ and its remainder $R(x)$ are congruent modulo the polynomial $g(x)$.

$$
f(x) \equiv R(x) \pmod{g(x)}
$$

This congruence also means that for any root $x_0$ of the polynomial $g(x)$, substituting it into $f(x)$ and into $R(x)$ gives the same value. That is:

$$
f(x_0)=R(x_0)
$$

Moreover, if the multiplicity of the root $x_0$ in the polynomial $g(x)$ is $k$, i.e. $(x-x_0)^k$ divides $g(x)$, then for any integer $t$ greater than or equal to $0$ and less than $k$ we have:

$$
f^{t}(x_0)=R^{t}(x_0)
$$

Here the notation denotes the $t$-th derivative.

Congruence modulo a polynomial can be applied to power series. A power series with infinitely many terms can be congruent, modulo a concrete polynomial, to a polynomial with finitely many terms. For example:

$$
1+x+x^2+x^3+\ldots \equiv 1+x+\ldots+x^{n-1} \pmod{x^n}
$$

Obviously all the remaining terms are divisible by $x^n$, so the operation modulo $x^n$ is equivalent to "truncation": the power series with infinitely many terms is truncated to its first $n$ terms, and the information in the higher terms is simply lost.

In some specific situations one can also work modulo other polynomials; the corresponding situations are explained below.

### Multipoint evaluation and interpolation of polynomials

**Multipoint evaluation of a polynomial (multi-point evaluation)** means: given a polynomial $f(x)$ and $n$ points $x_{1}, x_{2}, \dots, x_{n}$, compute

$$
f(x_{1}), f(x_{2}), \dots, f(x_{n})
$$

**Polynomial interpolation (interpolation)** means: given $n+1$ points

$$
(x_{0}, y_{0}), (x_{1}, y_{1}), \dots, (x_{n}, y_{n})
$$

find a polynomial $f(x)$ of degree $n$ such that all $n+1$ points lie on $f(x)$.

The essence of these two operations is converting a polynomial between its **coefficient representation** and its **point-value representation**. Multipoint evaluation converts the coefficient representation of a polynomial into its point-value representation, and interpolation converts the point-value representation into the coefficient representation.

???+ note "Note"
    From the viewpoint of power series, multipoint evaluation amounts to "compressing" the information of infinitely many terms into a point-value representation at finitely many points, so some information is lost, while interpolation amounts to restoring the coefficient representation of the corresponding degree.
    
    The evaluation and interpolation commonly used in programming, such as the discrete Fourier transform (and its inverse), choose $n+1$ points each of multiplicity $1$, i.e. pairwise distinct, which avoids the trouble of differentiation.
    
    This "compression" only guarantees agreement at the $n+1$ points. By the explanation of congruence modulo a polynomial above, if a power series $f(x)$ is evaluated at the points $x_0$ to $x_n$ and then interpolated to obtain a polynomial $R(x)$, then forming the polynomial:
    
    $$
    g(x)=(x-x_0)\ldots(x-x_n)
    $$
    
    we have:
    
    $$
    f(x) \equiv R(x) \pmod{g(x)}
    $$
    
    Since the degree of $R(x)$ is strictly less than that of $g(x)$, the $R(x)$ obtained by evaluation and interpolation is exactly the remainder. Therefore, in this situation, if the power series can be evaluated at the roots, one can work modulo the polynomial. A counterexample:
    
    $$
    \frac{1}{1-x}=1+x+x^2+x^3+\ldots
    $$
    
    cannot be evaluated at $x=1$, so the series $1+x+x^2+x^3+\ldots$ cannot be reduced modulo the polynomial $x-1$.
    
    Since the value at $0$ of a derivative of any order of a power series always exists, reduction modulo $x^n$ can always be computed, which agrees with the meaning of "truncation" above. The discrete Fourier transform (and its inverse) corresponds to reduction modulo the polynomial $x^n-1$.

### Factorization and the Euclidean algorithm

Many results of elementary number theory can be generalized to polynomials.

Over the field of complex numbers, by the fundamental theorem of algebra, for a polynomial $f$ of degree $n$ the equation

$$
f(x)=0
$$

has exactly $n$ solutions (multiple roots counted with multiplicity).

Hence $f(x)$ can be uniquely factored over the complex numbers in the form

$$
a(x-x_1)^{c_1}(x-x_2)^{c_2}\cdots(x-x_m)^{c_m}
$$

$$
c_1+c_2+\cdots+c_m=n,x_1,x_2,\cdots,x_m \text{ pairwise distinct}
$$

Then, by analogy with the greatest common divisor of positive integers, we obtain the [**greatest common divisor**](../number-theory/gcd.md) of polynomials  
(greatest common divisor, gcd). It can be computed with the Euclidean algorithm

$$
\gcd(f,0)=f,\gcd(f,g)=\gcd(g,f\bmod g)
$$

This property can be generalized to a more general situation:

> For the polynomial ring $P[x]$ over any field $P$,  
> polynomials can be uniquely factored, and the greatest common divisor can be computed with the Euclidean algorithm.
> Note that for polynomials over a general ring, this conclusion need not hold.

When the Euclidean algorithm holds, the extended Euclidean algorithm gives a particular solution $(P(x),Q(x))$ of the indeterminate equation

$$
f(x)P(x)+g(x)Q(x)=\gcd(f(x),g(x))
$$

and [Bézout's identity](../number-theory/bezouts.md) decides the solvability of the indeterminate equation

$$
f(x)P(x)+g(x)Q(x)=h(x)
$$

[HALF-GCD](https://loj.ac/p/172) allows us to compute the polynomial Euclidean algorithm in $O(n\log^2 n)$ time.

### Multiplicative inverse modulo a polynomial

Modulo a polynomial $h(x)$, a power series $f(x)$ sometimes has an inverse. The inverse is just the remainder of the reciprocal of the power series $f(x)$ modulo the polynomial $h(x)$.

This definition is also equivalent to the following: for a polynomial $f(x)$, if there exists $g(x)$ satisfying:

$$
\begin{aligned}
    f(x) g(x) & \equiv 1 \pmod{h(x)}
\end{aligned}
$$

then $g(x)$ is called the **inverse (inverse element)** of $f(x)$ modulo $h(x)$. When the polynomial Euclidean algorithm is allowed, the inverse exists if and only if $\gcd(f,h)=1$.

The inverse modulo a polynomial $h(x)$ is always unique. If the degree of the polynomial $f(x)$ is also less than that of $h(x)$, the resulting $g(x)$ and $f(x)$ are inverses of each other.

With the notion of "truncation" in mind, the inverse modulo $x^n$ is usually written $f^{-1}(x)$; this is also the notion of inverse used by default below. Unless stated otherwise, the modulus of the inverse is $x^n$.

???+ note "Note"
    One question is whether the "inverse" can be computed directly using various interpolation transforms, for example by computing:
    
    $$
    IDFT\left(\frac{DFT(1)}{DFT(f(x))}\right)
    $$
    
    The answer is no, this cannot be done. By the explanation above, the inverse obtained directly here with the discrete Fourier transform (and its inverse) is the inverse modulo the polynomial $x^n-1$, not the usual inverse modulo the polynomial $x^n$. Moreover, since the original polynomial may take the value $0$ at some of the points, this computation may not even be possible.

## Generating functions

A generating function, also called a generatrix, is a formal power series whose coefficients provide information about a sequence.

There are many different kinds of generating functions, but most can be expressed in a single form:

$$
F(x)=\sum_n a_nk_n(x)
$$

where $k_n(x)$ is called the kernel function. Different kernel functions lead to different generating functions with different properties. For example:

1.  Ordinary generating function: $k_n(x)=x^n$.
2.  Exponential generating function: $k_n(x)=\dfrac{x^n}{n!}$.
3.  [Dirichlet generating function](../number-theory/dirichlet.md#dirichlet-生成函数): $k_n(x)=\dfrac{1}{n^x}$.

## References and further reading

-   [**Picks's Blog**](https://picks.logdown.com)
-   [**Miskcoo's Space**](https://blog.miskcoo.com)
-   [**Polynomial ring - Wikipedia**](https://en.wikipedia.org/wiki/Polynomial_ring)
-   [**Formal power series - Wikipedia**](https://en.wikipedia.org/wiki/Formal_power_series#The_ring_of_formal_power_series)
-   《信息学竞赛中的生成函数计算理论框架》 (A theoretical framework for computing generating functions in informatics competitions)
