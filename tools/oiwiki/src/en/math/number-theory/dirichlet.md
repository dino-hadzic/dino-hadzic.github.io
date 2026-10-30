---
title: Dirichlet convolution
---

This article introduces the Dirichlet convolution and Dirichlet generating functions.

## Dirichlet convolution

The **Dirichlet convolution** of arithmetic functions $f(n)$ and $g(n)$, denoted $f \ast g$, is defined as the arithmetic function

$$
(f \ast g)(n) = \sum_{k\mid n}f(k)g\left(\dfrac{n}{k}\right) = \sum_{k\ell=n}f(k)g(\ell).
$$

The Dirichlet convolution is an important operation on arithmetic functions. Many properties of arithmetic functions are uncovered through this operation.

???+ example "Examples"
    1.  The unit function $\varepsilon$ is the Dirichlet convolution of the Möbius function $\mu$ and the constant function $1$:
    
        $$
        \varepsilon=\mu \ast 1 \iff\varepsilon(n)=\sum_{d\mid n}\mu(d).
        $$
    
    2.  The divisor-counting function $\tau$ is the Dirichlet convolution of the constant function $1$ with itself:
    
        $$
        \tau=1 \ast 1 \iff \tau(n)=\sum_{d\mid n}1.
        $$
    
    3.  The divisor-sum function $\sigma$ is the Dirichlet convolution of the identity function $\mathrm{id}$ and the constant function $1$:
    
        $$
        \sigma=\mathrm{id} \ast 1 \iff\sigma(n)=\sum_{d\mid n}d.
        $$
    
    4.  Euler's totient function $\varphi$ is the Dirichlet convolution of the identity function $\mathrm{id}$ and the Möbius function $\mu$:
    
        $$
        \varphi=\mathrm{id}\ast \mu \iff\varphi(n)=\sum_{d\mid n}d\cdot\mu\left(\frac{n}{d}\right).
        $$

[Möbius inversion](./mobius.md) is exactly the transformation of identities between arithmetic functions using $\varepsilon=\mu \ast 1$.

### Properties

The Dirichlet convolution has a series of algebraic properties.

???+ note "Theorem"
    Let $f,g,h$ be arithmetic functions. Then:
    
    1.  **Commutativity**: $f\ast g=g\ast f$.
    2.  **Associativity**: $(f\ast g)\ast h=f\ast(g\ast h)$.
    3.  **Distributivity**: $(f+g)\ast h = f\ast h + g\ast h$.
    4.  **Identity element**: $f\ast\varepsilon = \varepsilon \ast f = f$, where $\varepsilon(n) = [n=1]$ is the identity element of the convolution and $[\cdot]$ is the Iverson bracket.
    5.  **Inverse**: a $g$ with $f\ast g=g\ast f=\varepsilon$ exists if and only if $f(1)\neq 0$, and $g$ is called the **Dirichlet inverse** of $f$, which may be denoted $f^{-1}$. Moreover, the inverse $g$ satisfies the recurrence
    
        $$
        g(n) = \dfrac{\varepsilon(n) - \sum_{k\ell = n,~k\neq 1}f(k)g(\ell)}{f(1)}.
        $$

??? note "Proof"
    To verify commutativity, a direct computation gives
    
    $$
    (f\ast g)(n) = \sum_{k\ell=n}f(k)g(\ell) = (g\ast f)(n).
    $$
    
    To verify associativity, a direct computation gives
    
    $$
    ((f\ast g)\ast h)(n) = \sum_{k\ell m = n}f(k)g(\ell)h(m) = (f\ast (g\ast h))(n).
    $$
    
    To verify distributivity, a direct computation gives
    
    $$
    \begin{aligned}
    ((f+g)\ast h)(n) &= \sum_{k\ell = n}(f(k) + g(k))h(\ell) \\
    &= \sum_{k\ell=n}f(k)h(\ell) + \sum_{k\ell=n}g(k)h(\ell) = (f\ast h+g\ast h)(n).
    \end{aligned}
    $$
    
    To verify that $\varepsilon(n)$ is the identity element, a direct computation gives
    
    $$
    (f\ast\varepsilon)(n) = \sum_{k\ell = n}f(k)\varepsilon(\ell) = f(n).
    $$
    
    The second equality holds because $\varepsilon(\ell)$ is nonzero only when $\ell=1$, i.e. $k=n$.
    
    Finally, we need to prove that $f^{-1}$ exists if and only if $f(1)\neq 0$. For an arbitrary $f$, suppose there is a $g$ with $f\ast g=\varepsilon$. This means
    
    $$
    (f\ast g)(n) = \sum_{k\ell = n}f(k)g(\ell) = \varepsilon(n).
    $$
    
    This is in fact a system of equations for the values $g(n)$, from which $g(n)$ can be computed directly. In particular, for $n=1$ the equation becomes $f(1)g(1)=1$, so the existence of $g$ requires at least $f(1)\neq 0$. And as long as $f(1)\neq 0$, we can directly solve
    
    $$
    g(n) = \dfrac{\varepsilon(n) - \sum_{k\ell = n,~k\neq 1}f(k)g(\ell)}{f(1)}.
    $$
    
    This can be used to compute the values $g(n)$ recursively. Therefore, the inverse $g$ exists if and only if $f(1)\neq 0$.

In the language of abstract algebra, these algebraic properties show that all arithmetic functions, under (pointwise) addition and Dirichlet convolution, form a [commutative ring](../algebra/basic.md#环), and its invertible elements are exactly the functions that are nonzero at $n=1$. This ring is called the **Dirichlet ring**.

Multiplicative functions are a special class of arithmetic functions. They are closed under both Dirichlet convolution and Dirichlet inverse.

???+ note "Theorem"
    Let $f,g$ be multiplicative functions. Then $f\ast g$ is also a multiplicative function. Moreover, the inverse $f^{-1}$ always exists and is also a multiplicative function.

??? note "Proof"
    For the first claim, let $h=f\ast g$; a direct verification shows that for $n_1\perp n_2$ we have
    
    $$
    \begin{aligned}
    h(n_1)h(n_2) &= \left(\sum_{k_1\ell_1=n_1}f(k_1)g(\ell_1)\right)\left(\sum_{k_2\ell_2=n_2}f(k_2)g(\ell_2)\right)\\
    &= \sum_{k_1\ell_1=n_1,~k_2\ell_2=n_2}f(k_1)f(k_2)g(\ell_1)g(\ell_2)\\
    &= \sum_{k\ell = n_1n_2}f(k)g(\ell) \\
    &= h(n_1n_2).
    \end{aligned}
    $$
    
    Here the third equality uses the multiplicativity of $f,g$, and the logic behind reordering the summation is as follows: as $k$ runs over the divisors of $n_1n_2$, the prime factors of $k$ can be split into two groups according to whether they are prime factors of $n_1$ or of $n_2$; multiplying the prime factors of each group (with multiplicity) gives $k_1$ and $k_2$, which run over the divisors of $n_1$ and $n_2$ respectively; conversely, from divisors $k_1$ and $k_2$ of $n_1$ and $n_2$ we always obtain a divisor $k=k_1k_2$ of $n_1n_2$.
    
    For the second claim, let $g=f^{-1}$ and use mathematical induction. First, $g(1)=1/f(1)=1$. The recurrence for the inverse can then be written as
    
    $$
    g(n) = \varepsilon(n) - \sum_{k\ell = n,~k\neq 1} f(k)g(\ell).
    $$
    
    Therefore, for $n_1\perp n_2$ with $n_1n_2 > 1$, we have
    
    $$
    \begin{aligned}
    g(n_1n_2) &= -\sum_{k\ell=n_1n_2,~k\neq 1}f(k)g(\ell) \\
    &= -\sum_{k_1\ell_1=n_1,~k_2\ell_2=n_2,~k_1k_2\neq 1}f(k_1)f(k_2)g(\ell_1)g(\ell_2)\\
    &= f(1)f(1)g(n_1)g(n_2) - \sum_{k_1\ell_1=n_1,~k_2\ell_2=n_2}f(k_1)f(k_2)g(\ell_1)g(\ell_2)\\
    &= g(n_1)g(n_2) - \left(\sum_{k_1\ell_1=n_1}f(k_1)g(\ell_1)\right)\left(\sum_{k_2\ell_2=n_2}f(k_2)g(\ell_2)\right) \\
    &= g(n_1)g(n_2) - \varepsilon(n_1)\varepsilon(n_2)\\
    &= g(n_1)g(n_2).
    \end{aligned}
    $$
    
    Here the second equality uses the induction hypothesis, namely that for $\ell_1\ell_2 < n_1n_2$ with $\ell_1\perp\ell_2$ the condition $g(\ell_1\ell_2)=g(\ell_1)g(\ell_2)$ holds.

In the language of abstract algebra, all multiplicative functions under Dirichlet convolution form a [subgroup](../algebra/group-theory.md#子群) of the multiplicative group of the Dirichlet ring.

Even more special are completely multiplicative functions.

???+ note "Theorem"
    Let $\alpha$ be a completely multiplicative function and $f,g$ arithmetic functions. Then:
    
    1.  Distributivity: $(\alpha f)\ast(\alpha g) = \alpha\cdot(f\ast g)$.
    2.  Inverse: $(\alpha f)^{-1}=\alpha f^{-1}$, whenever $f^{-1}$ exists.
    3.  A multiplicative function $f$ is completely multiplicative if and only if $f^{-1}=\mu f$, where $\mu$ is the [Möbius function](./mobius.md#möbius-function).

??? note "Proof"
    For the first claim, a direct verification gives
    
    $$
    \begin{aligned}
    ((\alpha f)\ast(\alpha g))(n) &= \sum_{k\ell = n}(\alpha f)(k)(\alpha g)(\ell) \\
    &= \sum_{k\ell = n}\alpha(k)f(k)\alpha(\ell)g(\ell) \\
    &= \sum_{k\ell = n}\alpha(n)f(k)g(\ell) \\
    &= \alpha(n)(f\ast g)(n).
    \end{aligned}
    $$
    
    Here the third equality uses the property of completely multiplicative functions: $\alpha(n)=\alpha(k)\alpha(\ell)$ holds for all $n=k\ell$.
    
    For the second claim, by the first one we have
    
    $$
    (\alpha f)\ast(\alpha f^{-1}) = \alpha(f\ast f^{-1}) = \alpha\varepsilon = \varepsilon.
    $$
    
    Here the last equality only uses $\alpha(1)=1$. By the definition of the inverse, $(\alpha f)^{-1}=\alpha f^{-1}$.
    
    For the third claim, by the second one and $1^{-1}=\mu$, if $f$ is completely multiplicative, then
    
    $$
    f^{-1} = (1f)^{-1} = 1^{-1}\cdot f = \mu f.
    $$
    
    Here $1$ is the constant function. Conversely, if $f$ is multiplicative and $f^{-1}=\mu f$, then to prove that $f$ is completely multiplicative it suffices to show that $f(p^e)=f(p)^e$ for all primes $p$ and $e\in\mathbf N_+$. To this end, apply mathematical induction on $e\in\mathbf N_+$. The base case $e=1$ obviously holds. For any $e > 1$, applying the recurrence for the inverse gives
    
    $$
    \begin{aligned}
    f^{-1}(p^e) &= -\sum_{i=1}^{e}f(p^i)f^{-1}(p^{e-i}) \\
    &= -\sum_{i=1}^{e}f(p^i)\mu(p^{e-i})f(p^{e-i})\\
    &= -f(p^e)f(1)\mu(1) - f(p^{e-1})\mu(p)f(p)\\
    &= -f(p^e) + f(p)^e.
    \end{aligned}
    $$
    
    Here the last equality uses the induction hypothesis $f(p^{e-1})=f(p)^{e-1}$. Applying $f^{-1}=\mu f$, we get
    
    $$
    f^{-1}(p^e) = \mu(p^e)f(p^e) = 0.
    $$
    
    Substituting into the previous expression gives
    
    $$
    f(p^e) = f(p)^e.
    $$
    
    So the induction step holds, and the original claim is proved.

In the language of abstract algebra, if $\alpha$ is completely multiplicative, the map $f\mapsto \alpha f$ is an [endomorphism](../algebra/ring-theory.md#理想) of the Dirichlet ring.

## Dirichlet generating function

Closely related to the Dirichlet convolution is the Dirichlet generating function.

The **Dirichlet generating function** (Dirichlet series generating function, DGF) corresponding to an arithmetic function $f(n)$ – that is, to the sequence $\{f(n)\}$ – is defined as the formal Dirichlet series

$$
F(s) = \sum_{n=1}^{\infty}\dfrac{f(n)}{n^s}.
$$

Here $s$ is a formal variable. For common Dirichlet generating functions, $s$ can often be regarded as a complex variable, and the analytic properties of Dirichlet series can then be studied, but this is beyond the scope of algorithmic competitions.

The product of Dirichlet generating functions corresponds to the Dirichlet convolution of the corresponding arithmetic functions:

???+ note "Theorem"
    For arithmetic functions $f,g$ and their Dirichlet generating functions $F,G$, the generating function of their Dirichlet convolution $f\ast g$ equals $F\cdot G$.

??? note "Proof"
    Direct verification:
    
    $$
    \begin{aligned}
    F(s)G(s) &= \left(\sum_{k=1}^\infty\dfrac{f(k)}{k^s}\right)\left(\sum_{\ell=1}^\infty\dfrac{g(\ell)}{\ell^s}\right)= \sum_{k=1}^\infty\sum_{\ell=1}^\infty\dfrac{f(k)g(\ell)}{(k\ell)^s}\\
    &= \sum_{n=1}^{\infty}\dfrac{\sum_{k\ell = n}f(k)g(\ell)}{n^s} = \sum_{n=1}^\infty\dfrac{(f\ast g)(n)}{n^s}.
    \end{aligned}
    $$

Using the correspondence between Dirichlet convolution and products of Dirichlet generating functions, the properties of the Dirichlet convolution can be understood from the viewpoint of Dirichlet generating functions. Since multiplication of formal Dirichlet series is commutative, associative, and distributive over addition, the Dirichlet convolution of arithmetic functions satisfies the same algebraic properties.

### Euler product

The special nature of multiplicative functions is also reflected in their Dirichlet generating functions. Because of the [unique factorization theorem](./basic.md#fundamental-theorem-of-arithmetic) for integers, the generating function $F(s)$ of a multiplicative function $f(n)$ can be written in the following form:

$$
\begin{aligned}
F(s) &= \sum_{n=1}^{\infty}\dfrac{f(n)}{n^s} = \sum_{n=1}^{\infty}\prod_{p\in\mathbf P}\dfrac{f(p^{\nu_p(n)})}{p^{\nu_p(n)s}} = \prod_{p\in\mathbf P}\sum_{e=0}^{\infty}\dfrac{f(p^e)}{p^{es}}\\
&= \prod_{p\in\mathbf P}\left(1 + \dfrac{f(p)}{p^s} + \dfrac{f(p^2)}{p^{2s}} + \dfrac{f(p^3)}{p^{3s}} + \cdots\right).
\end{aligned}
$$

Here $\nu_p(n)$ denotes the exponent of $p$ in the prime factorization of $n$. This means that $F(s)$ can be factored into a product of factors $F_p(s)=\sum_{e=0}^{\infty}f(p^e)p^{-es}$, where the arithmetic function corresponding to each $F_p(s)$ can be nonzero only at powers of $p$. This infinite product is also called the **Euler product**. If both $F(s)$ and $G(s)$ can be factored in this way, then so can their product; translating this observation to arithmetic functions, the Dirichlet convolution of multiplicative functions is again multiplicative.

Furthermore, if $f(n)$ is also completely multiplicative, then $f(p^e)=f(p)^e$ and the above expression simplifies further:

$$
F(s) = \prod_{p\in\mathbf P}\sum_{e=0}^{\infty}\dfrac{f(p)^e}{p^{es}} = \prod_{p\in\mathbf P}\left(1-\dfrac{f(p)}{p^s}\right)^{-1}.
$$

Unlike for multiplicative functions, the form of the Dirichlet generating function of a completely multiplicative function is not closed under multiplication; therefore, the Dirichlet convolution and the Dirichlet inverse of completely multiplicative functions need not be completely multiplicative, but they are certainly multiplicative.

???+ example "Examples"
    1.  The unit function $\varepsilon(n)$ is completely multiplicative. Its Dirichlet generating function is the constant function in the indeterminate $s$
    
        $$
        E(s) = \sum_{n=1}^{\infty}\dfrac{\varepsilon(n)}{n^s} = 1.
        $$
    
    2.  The constant function $1(n)$ is completely multiplicative. Its Dirichlet generating function is the Riemann zeta function ζ
    
        $$
        I(s) = \sum_{n=1}^{\infty}\dfrac{1}{n^s} = \prod_{p\in\mathbf P}\dfrac{1}{1-p^{-s}} = \zeta(s).
        $$
    
    3.  The Möbius function $\mu(n)$ is the Dirichlet inverse of the constant function. Its Dirichlet generating function is the reciprocal of $\zeta(s)$:
    
        $$
        M(s) = \sum_{n=1}^{\infty}\dfrac{\mu(n)}{n^s} = \prod_{p\in\mathbf P}(1-p^{-s}) = \dfrac{1}{\zeta(s)}.
        $$
    
    4.  The power function $\operatorname{id}_k(n)=n^k$ is completely multiplicative. In particular, for $k=0$ it is the constant function, and for $k=1$ it is the identity function. Its Dirichlet generating function is
    
        $$
        I_k(s) = \sum_{n=1}^{\infty}\dfrac{n^k}{n^s} = \prod_{p\in\mathbf P}\dfrac{1}{1-p^{k-s}} = \zeta(s-k).
        $$
    
    5.  Euler's totient function $\varphi(n)$ is multiplicative. Its Dirichlet generating function is
    
        $$
        \begin{aligned}
        \Phi(s) &= \prod_{p\in\mathbf P}\left(1+\dfrac{p-1}{p^s} + \dfrac{p(p-1)}{p^{2s}} + \dfrac{p^2(p-1)}{p^{3s}}+\cdots\right)\\
        &= \prod_{p\in\mathbf P}\left(\dfrac{1}{1-p^{1-s}}-\dfrac{1}{p^s}\dfrac{1}{1-p^{1-s}}\right) = \prod_{p\in\mathbf P}\dfrac{1-p^{-s}}{1-p^{1-s}} = \dfrac{\zeta(s-1)}{\zeta(s)}.
        \end{aligned}
        $$
    
        Combined with the expression for the Dirichlet generating function of the power function, this gives $\mathrm{id} = \varphi\ast 1$.
    
    6.  The divisor function $\sigma_k(n)=\sum_{d\mid n}d^k$ is multiplicative. Its Dirichlet generating function is
    
        $$
        \begin{aligned}
        \Sigma_k(s) &= \prod_{p\in\mathbf P}\left(1+\dfrac{1+p^k}{p^s}+\dfrac{1+p^k+p^{2k}}{p^{2s}}+\dfrac{1+p^k+p^{2k}+p^{3k}}{p^{3s}}+\cdots\right) \\
        &= \prod_{p\in\mathbf P}\dfrac{1}{1-p^k}\left((1-p^k)+\dfrac{1-p^{2k}}{p^s}+\dfrac{1-p^{3k}}{p^{2s}}+\dfrac{1-p^{4k}}{p^{3s}}+\cdots\right)\\
        &= \prod_{p\in\mathbf P}\dfrac{1}{1-p^k}\left(\dfrac{1}{1-p^{-s}} - \dfrac{p^k}{1-p^{k-s}}\right)\\
        &= \prod_{p\in\mathbf P}\dfrac{1}{(1-p^{-s})(1-p^{k-s})} = \zeta(s-k)\zeta(s).
        \end{aligned}
        $$
    
        Combined with the expression for the Dirichlet generating function of the power function, this gives $\sigma_k = \mathrm{id}_k\ast 1$. This is exactly the defining formula of $\sigma_k$.
    
    7.  The indicator function of squarefree numbers $u(n)=|\mu(n)|=\mu^2(n)$ is multiplicative. Its Dirichlet generating function is
    
        $$
        U(s) = \prod_{p\in\mathbf P}(1+p^{-s}) = \prod_{p\in\mathbf P}\dfrac{1-p^{-2s}}{1-p^{-s}} = \dfrac{\zeta(s)}{\zeta(2s)}.
        $$

### Bell series

The Euler product shows that the Dirichlet generating function of a multiplicative function can be factored into a product of local factors $F_p(s)$. If we only care about the information at a single prime, we can treat $p^{-s}$ as a whole as a formal variable; this gives the Bell series.

For a multiplicative function $f$ and a prime $p$, the **Bell series** of $f$ with respect to $p$ is defined as the formal power series

$$
f_p(x) = \sum_{e=0}^{\infty} f(p^e)x^e = 1 + f(p)x + f(p^2)x^2 + \cdots.
$$

Comparing with the expression of the Euler product, $f_p(x)$ is exactly the result of replacing $p^{-s}$ in $F_p(s)$ by $x$, i.e. $F_p(s) = f_p(p^{-s})$, and hence

$$
F(s) = \prod_{p\in\mathbf P}f_p(p^{-s}).
$$

After introducing this notation, we can see that, once localized, the Dirichlet convolution is just ordinary multiplication of power series.

Translating the results on Dirichlet generating functions to Bell series yields the following properties:

1.  For multiplicative functions $f,g$ and any prime $p$, $(f\ast g)_p(x) = f_p(x)g_p(x)$.
2.  A multiplicative function $f$ is completely multiplicative if and only if $f_p(x) = \dfrac{1}{1-f(p)x}$ for every prime $p$.
3.  The Dirichlet inverse of a multiplicative function always exists, and $(f^{-1})_p(x) = \dfrac{1}{f_p(x)}$.

Since a multiplicative function is uniquely determined by its values at prime powers, multiplicative functions are in one-to-one correspondence with the collection of all their Bell series $\{f_p\}_{p\in\mathbf P}$. Thus, many problems about Dirichlet convolutions of multiplicative functions can be reduced, prime by prime, to problems about formal power series. Compared with using Dirichlet generating functions directly, this is somewhat simpler in form. For example, the third property says that to find the Dirichlet inverse one only needs to invert a formal power series prime by prime; in actual computation, since only the part with $p^e\le n$ is needed, for each prime the series is truncated at most at the term $x^{\lfloor\log_p n\rfloor}$.

???+ example "Examples"
    The Bell series corresponding to the multiplicative functions in the previous examples are as follows:
    
    |    $f$   | $\varepsilon$ |        $1$       | $\mu$ | $\operatorname{id}_k$ |      $\varphi$      |         $\sigma_k$         | $\lvert\mu\rvert=\mu^2$ |
    | :------: | :-----------: | :--------------: | :---: | :-------------------: | :-----------------: | :------------------------: | :---------------------: |
    | $f_p(x)$ |      $1$      | $\dfrac{1}{1-x}$ | $1-x$ |  $\dfrac{1}{1-p^kx}$  | $\dfrac{1-x}{1-px}$ | $\dfrac{1}{(1-x)(1-p^kx)}$ |          $1+x$          |
    
    Using the table above, common Dirichlet convolution relations can be verified directly. For example, $\mu\ast 1=\varepsilon$ corresponds to
    
    $$
    (1-x)\cdot\dfrac{1}{1-x} = 1,
    $$
    
    and $\varphi\ast 1=\operatorname{id}$ corresponds to
    
    $$
    \dfrac{1-x}{1-px}\cdot\dfrac{1}{1-x} = \dfrac{1}{1-px}.
    $$

### Applications

Dirichlet generating functions can be used to express arithmetic functions as Dirichlet convolutions.

For example, in Du's sieve, to compute the prefix sums of an arithmetic function $f$ one needs to find another arithmetic function $g$ such that the prefix sums of both $f\ast g$ and $g$ can be computed quickly. This process can be carried out using Dirichlet generating functions.

Take the example problem from the section on Du's sieve, [Luogu P3768 简单的数学题 (A simple math problem)](../number-theory/hyperbola.md#example-problems): for $f(n)=n^2\varphi(n)$ we need to construct an arithmetic function $g(n)$ satisfying the above conditions. Since $f$ is multiplicative, its Dirichlet generating function is

$$
F(s) = \prod_{p\in\mathbf P}\left(1 + \sum_{k=1}^{\infty}\dfrac{p^{3k-1}(p-1)}{p^{ks}}\right) = \prod_{p\in\mathbf P}\dfrac{1-p^{2-s}}{1-p^{3-s}} = \dfrac{\zeta(s-3)}{\zeta(s-2)}.
$$

Comparing with the Dirichlet generating function of the power function, it suffices to take $g = \mathrm{id}_2$, and then $f \ast g = \mathrm{id}_3$. The prefix sums of both can be computed quickly.

Since the arithmetic functions in common problems are all multiplicative, in practice it is often more convenient to use Bell series. For example, in the example just given, the Bell series of $f(n)$ can be derived directly from $f(p^e)=p^{3e-1}(p-1)$ as

$$
f_p(x) = 1 + \dfrac{p-1}{p}\sum_{e=1}^{\infty}(p^3x)^e = 1 + \dfrac{(p-1)p^2x}{1-p^3x} = \dfrac{1-p^2x}{1-p^3x}.
$$

Comparing with the Bell series of the power function immediately gives $f \ast \mathrm{id}_2 = \mathrm{id}_3$.

## Computing Dirichlet convolutions

This section discusses the problem of computing Dirichlet convolutions: given sequences $\{f(k)\}_{k=1}^n$ and $\{g(k)\}_{k=1}^n$, find the first several terms $\{h(k)\}_{k=1}^n$ of the Dirichlet convolution $h=f\ast g$. Depending on the properties of the functions involved, the complexity of the algorithm differs slightly.

### General case

If none of $f,g,h$ has special properties, the Dirichlet convolution can only be computed from its definition:

$$
h(n) = \sum_{k\ell = n}f(k)g(\ell).
$$

Just enumerate $k$ and $\ell$ and add the contribution $f(k)g(\ell)$ to $h(k\ell)$. The enumeration complexity is

$$
O\left(\sum_{k=1}^{n}\dfrac{n}{k}\right) = O(n\log n).
$$

A reference implementation follows:

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/math/code/dirichlet/dirichlet-1.cpp:core"
    ```

### Convolution with a multiplicative function

If $g$ is multiplicative, the Euler product can be used to speed up the computation of the Dirichlet convolution. Computing $h$ amounts to computing the coefficients of its Dirichlet generating function $H$. Since

$$
H(s) = F(s)G(s) = F(s)\prod_{p\in\mathbf P}G_p(s).
$$

Here $G_p(s)$ is the factor in the Euler product factorization of $G(s)$; it only contains the coefficients at powers of $p$:

$$
G_p(s) = \sum_{p^k\le n}\dfrac{g(p^k)}{p^{ks}} = 1 + \dfrac{g(p)}{p^s} + \dfrac{g(p^2)}{p^{2s}} + \cdots.
$$

Then, starting from $F(s)$, iterating over all primes $p$ not exceeding $n$ and multiplying by $G_p(s)$ one by one, we likewise obtain the final result $H(s)$. When multiplying by $G_p(s)$, we simply apply the brute-force enumeration algorithm from the general case. The total number of enumeration steps is

$$
\sum_{p\in\mathbf P,~p\le n}\sum_{k=1}^{\infty}\left\lfloor\dfrac{n}{p^k}\right\rfloor \le \sum_{p\in\mathbf P,~p\le n}\dfrac{n}{p-1} \le \sum_{p\in\mathbf P,~p\le n}\dfrac{2n}{p} \in O(n\log\log n).
$$

The complexity estimate in the last step is the same as in the proof of the complexity of the [sieve of Eratosthenes](./sieve.md#sieve-of-eratosthenes). So the time complexity of this algorithm is $O(n\log\log n)$.

A reference implementation follows:

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/math/code/dirichlet/dirichlet-2.cpp:core"
    ```

In particular, when the multiplicative function $g$ is completely multiplicative or the Dirichlet inverse of such a function, for example when $g = 1$ or $g = \mu$, the algorithm can be simplified further. In this case, the Dirichlet convolution $h = f\ast g$ can be computed with the [Dirichlet prefix sum/difference](./mobius.md#dirichlet-prefix-sums) algorithm, which has a smaller constant, although the time complexity is still $O(n\log\log n)$.

### Case where the result is multiplicative

Finally, consider the case where $h$ is multiplicative. In particular, when $f,g$ are both multiplicative, $h=f \ast g$ is multiplicative. To compute $h$, it suffices to determine its values at prime powers; then it can be computed in $O(n)$ time with the [linear sieve](./sieve.md#linear-sieve). The values $h(p^e)$ at prime powers $p^e$ can be computed directly by brute force:

$$
h(p^e) = \sum_{i=0}^e f(p^i)g(p^{e-i}).
$$

The number of enumeration steps required by these brute-force computations is

$$
\begin{aligned}
\sum_{p\in\mathbf P,~p\le n}\sum_{e=1}^{\lfloor\log_p n\rfloor}(e+1) &\le \sum_{p\in\mathbf P,~p\le\sqrt{n}}2\lfloor\log_p n\rfloor^2 + \sum_{p\in\mathbf P,~\sqrt{n} < p\le n}2 \\
&\le 2\sqrt{n}(\log_2 n)^2 + 2n \in O(n).
\end{aligned}
$$

Therefore, the total time complexity of this algorithm is $O(n)$.

A reference implementation follows:

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/math/code/dirichlet/dirichlet-3.cpp:core"
    ```

## References and notes

-   [Dirichlet convolution - Wikipedia](https://en.wikipedia.org/wiki/Dirichlet_convolution)
-   [Dirichlet series - Wikipedia](https://en.wikipedia.org/wiki/Dirichlet_series)
-   [Euler product - Wikipedia](https://en.wikipedia.org/wiki/Euler_product)
-   [Bell series - Wikipedia](https://en.wikipedia.org/wiki/Bell_series)
-   [Dirichlet 積と、数論関数の累積和 (Dirichlet product and prefix sums of arithmetic functions) by maspy](https://maspypy.com/dirichlet-%e7%a9%8d%e3%81%a8%e3%80%81%e6%95%b0%e8%ab%96%e9%96%a2%e6%95%b0%e3%81%ae%e7%b4%af%e7%a9%8d%e5%92%8c)
-   [杜教筛（+ 贝尔级数 + powerful number）(Du's sieve (+ Bell series + powerful number)) by command\_block - Luogu](https://www.luogu.com.cn/article/ygfzawod)
