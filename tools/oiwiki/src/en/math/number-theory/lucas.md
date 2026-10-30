---
title: Lucas's theorem
---

Prerequisites: [Factorial modulo a number](./factorial.md)

## Introduction

This article discusses the computation of large binomial coefficients modulo a number. A binomial coefficient (number of combinations) is the expression:

$$
\binom{n}{k} = \dfrac{n!}{k!(n-k)!}.
$$

When the problem size is not large, binomial coefficients can be computed by the [recurrence](../combinatorics/combination.md#组合数性质--二项式推论) in $O(nk)$ time; modulo a sufficiently large prime $p>n$, they can also be computed in $O(n)$ time by computing the factorials in the numerator and the denominator. But when the problem size is very large ($n\sim 10^{18}$), these methods no longer apply.

Based on Lucas's theorem and its generalization, this article discusses a method that can compute binomial coefficients when the modulus is not too large ($m \sim 10^6$). More precisely, the method can be used as long as the sum of all prime powers in the unique factorization of the modulus $m=\prod p_i^{e_i}$ (i.e. $\sum p_i^{e_i}$) is on the order of $10^6$, because the precomputation of the algorithm is roughly of this size.

## Lucas's theorem

First we discuss the case where the modulus is a prime $p$. In this case, we have Lucas's theorem:

???+ note "Lucas's theorem"
    For a prime $p$, we have
    
    $$
    \binom{n}{k}\equiv \binom{\lfloor n/p\rfloor}{\lfloor k/p\rfloor}\binom{n\bmod p}{k\bmod p}\pmod p.
    $$
    
    Here, for $n<k$ the binomial coefficient $\dbinom{n}{k}$ is defined to be $0$.

??? note "Proof using generating functions"
    Consider the value of $\displaystyle\binom{p}{n} \bmod p$. Since
    
    $$
    \binom{p}{n} = \frac{p!}{n!(p-n)!},
    $$
    
    for $n\neq 0,p$ the denominator contains no factor $p$ while the numerator contains a factor $p$, so the fraction must be a multiple of $p$ and its remainder modulo $p$ is $0$; for $n=0,p$ the fraction equals $1$. Therefore,
    
    $$
    \binom{p}{n} \equiv [n=0\lor n=p] \pmod p.
    $$
    
    Let $f(x) = ax^n + bx^m$. In general, by the [binomial theorem](../combinatorics/combination.md#二项式定理) and [Fermat's little theorem](./fermat.md#费马小定理) we have
    
    $$
    \begin{aligned}
    (f(x))^p 
    &= \left(ax^n + bx^m\right)^p \\
    &= \sum_{k=0}^p\binom{p}{k}(ax^n)^k(bx^m)^{p-k}\\
    &\equiv a^px^{pn} + b^px^{pm} \\
    &\equiv a(x^p)^n+b(x^p)^m\\
    &= f(x^p) \pmod p.
    \end{aligned}
    $$
    
    Here, the congruence in the third line uses the conclusion shown above, namely that the binomial coefficient is not a multiple of $p$ only for $k=0,p$.
    
    Using this conclusion, consider the binomial expansion:
    
    $$
    \begin{aligned}
    (1+x)^n &= (1+x)^{p\lfloor n/p\rfloor}(1+x)^{n\bmod p} \\
    &\equiv (1+x^p)^{\lfloor n/p\rfloor}(1+x)^{n\bmod p} \pmod p.
    \end{aligned}
    $$
    
    On the left-hand side, the coefficient of the term $x^k$ is
    
    $$
    \binom{n}{k}\bmod p.
    $$
    
    Now we compute the coefficient of the term $x^k$ on the right-hand side. The degrees of the terms in the first factor are necessarily multiples of $p$, and the degrees of the terms in the second factor are necessarily less than $p$; the way to split $k$ into a sum of two such parts is unique, given by division with remainder: $k=p\lfloor k/p\rfloor +(k\bmod p)$. Therefore, the first factor can only contribute its term of degree $p\lfloor k/p\rfloor$, and the second factor can only contribute its term of degree $k\bmod p$. So the coefficient of $x^k$ on the right-hand side is the product of the coefficients of the terms contributed by the two factors:
    
    $$
    \binom{\lfloor n/p\rfloor}{\lfloor k/p\rfloor}\binom{n\bmod p}{k\bmod p}\bmod p.
    $$
    
    Equating the coefficients on both sides gives Lucas's theorem.

??? note "Proof using the results on factorials modulo a number"
    Here we give a proof based on the results on [factorials modulo a number](./factorial.md#the-prime-modulus-case), in order to establish a connection with the method of the exLucas section below. We know that the binomial coefficient is
    
    $$
    \binom{n}{k} = \dfrac{n!}{k!(n-k)!}.
    $$
    
    Separating the powers of $p$ in the factorial $n!$ from the other factors, we obtain the decomposition:
    
    $$
    n! = p^{\nu_p(n!)}(n!)_p.
    $$
    
    This gives the expression for the binomial coefficient:
    
    $$
    \binom{n}{k} = p^{\nu_p(n!)-\nu_p(k!)-\nu_p((n-k)!)}\dfrac{(n!)_p}{(k!)_p((n-k)!)_p}.
    $$
    
    Both the exponent $\nu_p(n!)$ and the factorial remainder $(n!)_p\bmod p$ satisfy recurrences:
    
    $$
    \begin{aligned}
    \nu_p(n!) &= \lfloor n/p\rfloor+\nu_p( \lfloor n/p\rfloor!),\\
    (n!)_p &\equiv (-1)^{\lfloor n/p\rfloor}\cdot (n\bmod p)!\cdot (\lfloor n/p\rfloor!)_p\pmod p.
    \end{aligned}
    $$
    
    The former is a corollary of Legendre's formula, the latter a corollary of Wilson's theorem.
    
    Substituting the recurrences into the expression for the binomial coefficient and rearranging, we obtain:
    
    $$
    \begin{aligned}
    \binom{n}{k} &\equiv (-p)^{\lfloor n/p\rfloor-\lfloor k/p\rfloor-\lfloor(n-k)/p\rfloor}\cdot\dfrac{(n\bmod p)!}{(k\bmod p)!((n-k)\bmod p)!} \\
    &\quad \cdot p^{\nu_p(\lfloor n/p\rfloor!)-\nu_p(\lfloor k/p\rfloor!)-\nu_p(\lfloor(n-k)/p\rfloor!)}\dfrac{(\lfloor n/p\rfloor!)_p}{(\lfloor k/p\rfloor!)_p(\lfloor(n-k)/p\rfloor!)_p} \pmod p.
    \end{aligned}
    $$
    
    Now consider the value of $\lfloor n/p\rfloor-\lfloor k/p\rfloor-\lfloor(n-k)/p\rfloor$. Since we have
    
    $$
    \begin{aligned}
    n &= \lfloor n/p\rfloor p + (n\bmod p),\\
    k &= \lfloor k/p\rfloor p + (k\bmod p),\\
    n-k &= \lfloor (n-k)/p\rfloor p + ((n-k)\bmod p),\\
    \end{aligned}
    $$
    
    subtracting the latter two equations from the first gives
    
    $$
    (\lfloor n/p\rfloor-\lfloor k/p\rfloor-\lfloor(n-k)/p\rfloor)p = (k\bmod p)+((n-k)\bmod p)-(n\bmod p).
    $$
    
    On the right-hand side, the sum of the first two terms is strictly less than $2p$, and the third term $n\bmod p$ is exactly the remainder of the sum of the first two terms, so the right-hand side must be nonnegative but less than $2p$; since it must also be a multiple of $p$, it can only be $0$ or $p$. This shows that $\lfloor n/p\rfloor-\lfloor k/p\rfloor-\lfloor(n-k)/p\rfloor$ can only be $0$ or $1$:
    
    -   If it is $0$, then $(n\bmod p) = (k\bmod p)+((n-k)\bmod p)$ also holds. Therefore, the exponent of the first factor in the expression above is $0$, so that factor equals one; the second factor is exactly $\dbinom{n\bmod p}{k\bmod p}$; and the third factor, by the expansion above (note that now $\lfloor(n-k)/p\rfloor=\lfloor n/p\rfloor-\lfloor k/p\rfloor$), equals $\dbinom{\lfloor n/p\rfloor}{\lfloor k/p\rfloor}$. In this case Lucas's theorem holds;
    -   If it is $1$, then the exponent of the first factor is $1$, so that factor equals zero, and hence the remainder of the binomial coefficient is zero. At the same time, $\dbinom{n\bmod p}{k\bmod p}$ on the right-hand side of the identity claimed by Lucas's theorem must also be zero, because in this case necessarily $(n\bmod p)<(k\bmod p)$; otherwise we would have
    
        $$
        ((n-k)\bmod p) = p + (n\bmod p) - (k\bmod p) \ge p.
        $$
    
        This obviously contradicts the definition of the remainder.
    
    Combining the two cases, we obtain the desired Lucas's theorem. This proof shows that, when computing binomial coefficients modulo a prime, the results obtained using Lucas's theorem and using the exLucas algorithm are equivalent.

Lucas's theorem states that, when the modulus is a prime $p$, the computation of large binomial coefficients can be reduced to the computation of binomial coefficients of smaller size. On the right-hand side, the first binomial coefficient can be computed recursively until $k=0$; the second binomial coefficient can be computed directly or precomputed in advance. Written as code:

???+ example "Sketch"
    ```cpp
    long long Lucas(long long n, long long k, long long p) {
      if (k == 0) return 1;
      return (C(n % p, k % p, p) * Lucas(n / p, k / p, p)) % p;
    }
    ```

Here, `C(n, k, p)` is used to compute small binomial coefficients.

The recursion runs at most $O(\log_p n)$ times, so the complexity of the algorithm is $O(f(p)+g(p)\log_p n)$, where $f(p)$ is the complexity of precomputing the binomial coefficients and $g(p)$ is the complexity of computing a single binomial coefficient.

### Reference implementation

The reference implementation given here precomputes the factorials up to $p$ and their inverses in $O(p)$ time, after which it can compute a single binomial coefficient in $O(1)$ time:

??? example "Reference implementation"
    ```cpp
    --8<-- "docs/math/code/lucas/lucas.cpp"
    ```

The time complexity of this implementation is $O(p+T\log_p n)$, where $T$ is the number of queries.

## The exLucas algorithm

Lucas's theorem requires the modulus $p$ to be prime; for the case where the modulus is not prime, the exLucas algorithm (extended Lucas's theorem) is needed. Despite its name, this algorithm does not actually use Lucas's theorem. Its key step is [computing factorials modulo a prime power](./factorial.md). The second proof above pointed out its connection with Lucas's theorem.

### The prime power modulus case

First consider the case where the modulus is a prime power $p^\alpha$. Separating the powers of $p$ in the factorial $n!$ from the other factors, we obtain the decomposition:

$$
n! = p^{\nu_p(n!)}(n!)_p.
$$

Here, $\nu_p(n!)$ is the exponent of $p$ in the prime factorization of $n!$, and $(n!)_p$ is obviously coprime to $p$. Therefore, the binomial coefficient can be written as:

$$
\binom{n}{k} = p^{\nu_p(n!)-\nu_p(k!)-\nu_p((n-k)!)}\dfrac{(n!)_p}{(k!)_p((n-k)!)_p}.
$$

The quantities $\nu_p(n!)$ etc. in the formula can be computed by [Legendre's formula](./factorial.md#legendres-formula), and $(n!)_p$ etc. by the [recurrence relation](./factorial.md#the-prime-power-modulus-case). Since the latter are coprime to $p^\alpha$, the inverse of the product in the denominator can be computed by the [extended Euclidean algorithm](./inverse.md#扩展欧几里得算法). This solves the problem.

Note that if the exponent $\nu_p(n!)-\nu_p(k!)-\nu_p((n-k)!)\ge\alpha$, the remainder must be zero and no further computation is needed.

### The general modulus case

For the case where $m$ is a general composite number, it suffices to first [factorize it into primes](./pollard-rho.md):

$$
m = p_1^{\alpha_1}p_2^{\alpha_2}\cdots p_s^{\alpha_s}.
$$

Then, compute separately the remainders of the binomial coefficient $\dbinom{n}{k}$ modulo $p_i^{\alpha_i}$, obtaining $s$ congruences:

$$
\begin{cases}
\dbinom{n}{k} \equiv r_1 &\pmod{p_1^{\alpha_1}}, \\
\dbinom{n}{k} \equiv r_2 &\pmod{p_2^{\alpha_2}}, \\
\quad\quad\cdots\\
\dbinom{n}{k} \equiv r_s &\pmod{p_s^{\alpha_s}}.
\end{cases}
$$

Finally, use the [Chinese remainder theorem](./crt.md) to obtain the remainder modulo $m$.

### Reference implementation

Finally, we give a reference implementation for the template problem [二项式系数 (Binomial Coefficient)](https://loj.ac/p/181).

??? example "Reference implementation"
    ```cpp
    --8<-- "docs/math/code/lucas/exlucas.cpp"
    ```

During precomputation, this algorithm factorizes the modulus $m$ into prime powers, and then for every $p^\alpha$ precomputes the product of all natural numbers from $1$ to $p^\alpha$ that are not multiples of $p$, as well as the corresponding coefficient for combining the answers with the Chinese remainder theorem. The time complexity of the precomputation is $O(\sqrt{m}+\sum_ip_i^{\alpha_i})$. The complexity of each query is $O(\log m+\sum_i\log_{p_i}n)$, where the two terms are the complexity of computing inverses and the complexity of computing the exponents and factorial remainders, respectively.

## Exercises

-   [Luogu P3807【模板】卢卡斯定理 (Template: Lucas's theorem)](https://www.luogu.com.cn/problem/P3807)
-   [SDOI2010 古代猪文 (Ancient Pig Script) – Lucas's theorem](https://loj.ac/problem/10229)
-   [Luogu P4720【模板】扩展卢卡斯 (Template: extended Lucas)](https://www.luogu.com.cn/problem/P4720)
-   [Ceizenpok’s formula](http://codeforces.com/gym/100633/problem/J)
