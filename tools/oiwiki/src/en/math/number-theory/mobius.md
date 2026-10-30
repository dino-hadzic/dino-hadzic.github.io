---
title: Möbius inversion
---

Prerequisites: [floor-division blocks](./sqrt-decomposition.md), [Dirichlet convolution](./dirichlet.md#dirichlet-convolution)

Möbius inversion is an important topic in number theory. For some functions $f(n)$, if it is hard to compute the value directly but easy to compute the sum over multiples or the sum over divisors $g(n)$, Möbius inversion can simplify the computation and yield the value of $f(n)$.

## Möbius function

The Möbius function is defined as

$$
\mu(n)=
\begin{cases}
1,&n=1,\\
0,&n\text{ is divisible by a square }>1,\\
(-1)^k,&n\text{ is the product of }k\text{ distinct primes}.\\
\end{cases}
$$

Concretely, suppose the positive integer $n$ has the prime factorization $n=\prod_{i=1}^kp_i^{e_i}$, where the $p_i$ are primes and the $e_i$ are positive integers. Then the three cases correspond to:

1.  $\mu(1) = 1$;
2.  if there is an $i$ with $e_i > 1$, i.e. some prime factor appears more than once, then $\mu(n)=0$;
3.  otherwise, if $e_i = 1$ for all $i$, i.e. every prime factor appears exactly once, then $\mu(n)=(-1)^k$, where $k$ is the number of distinct prime factors.

### Properties

From the definition it is easy to verify that the Möbius function $\mu(n)$ is multiplicative but not completely multiplicative. Apart from that, the most important property is the following identity:

???+ note "Property"
    For a positive integer $n$,
    
    $$
    \sum_{d\mid n}\mu(d) = [n = 1] =
    \begin{cases}
    1,&n=1,\\
    0,&n\neq 1.\\
    \end{cases}
    $$
    
    Here $[\cdot]$ is the Iverson bracket.

??? note "Proof"
    Let $n=\prod_{i=1}^kp_i^{e_i}$ and set $n' = \prod_{i=1}^kp_i$. By the [binomial theorem](../combinatorics/combination.md#二项式定理),
    
    $$
    \sum_{d\mid n}\mu(d) = \sum_{d\mid n'}\mu(d) = \sum_{i=0}^k\binom{k}{i}(-1)^i = (1 + (-1))^k = [k = 0] = [n = 1].
    $$

Using the Dirichlet convolution, this expression can be written as $\varepsilon = 1 * \mu$. In other words, the Möbius function is the Dirichlet inverse of the constant function $1$.

This property has a very common application:

$$
[i\perp j] = [\gcd(i,j) = 1] = \sum_{d\mid\gcd(i,j)} \mu(d) = \sum_{d}[d\mid i][d\mid j]\mu(d).
$$

It turns the coprimality condition into a sum involving the Möbius function, which makes further derivations easier.

### Computation

If the value of the Möbius function $\mu(n)$ is needed for a single $n$, its [prime factorization](./pollard-rho.md) can be used. For example, when $n$ is not too large, $\mu(n)$ can be computed in $O(\sqrt{n})$ time.

???+ example "Reference implementation"
    === "C++"
        ```cpp
        --8<-- "docs/math/code/mobius/mobius-func-1.cpp:core"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/math/code/mobius/mobius-func-1.py:core"
        ```

If the values of $\mu(n)$ need to be precomputed for the first $n$ positive integers, one can use the fact that it is multiplicative and compute them with the [linear sieve](./sieve.md#筛法求莫比乌斯函数) in $O(n)$ time.

???+ example "Reference implementation"
    === "C++"
        ```cpp
        --8<-- "docs/math/code/mobius/mobius-func-2.cpp:core"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/math/code/mobius/mobius-func-2.py:core"
        ```

## Möbius inversion

The most important application of the Möbius function is Möbius inversion.

???+ note "Möbius inversion"
    Let $f(n),g(n)$ be two arithmetic functions. Then
    
    $$
    f(n) = \sum_{d\mid n}g(d) \iff g(n) = \sum_{d\mid n}\mu\left(\dfrac{n}{d}\right)f(d).
    $$

??? note "Proof 1"
    By direct verification:
    
    $$
    \begin{aligned}
    \sum_{d\mid n}\mu\left(\dfrac{n}{d}\right)f(d)
    &= \sum_{d\mid n}\mu\left(\dfrac{n}{d}\right)\sum_{k\mid d}g(k)\\
    &= \sum_{k\mid n}g(k)\sum_d[k\mid d\mid n]\mu\left(\dfrac{n}{d}\right)\\
    &= \sum_{k\mid n}g(k)\sum_{d\mid n}\left[\frac{n}{d}\mid\frac{n}{k}\right]\mu\left(\dfrac{n}{d}\right)\\
    &= \sum_{k\mid n}g(k)\left[\frac{n}{k} = 1\right] \\
    &= g(n).
    \end{aligned}
    $$
    
    The key to the transformation is exchanging the order of summation and noticing that $k\mid d\mid n$ is equivalent to $\dfrac{n}{d}\mid\dfrac{n}{k}$. The second-to-last equality amounts to summing the Möbius function over the divisors $\dfrac{n}{d}$ of $\dfrac{n}{k}$, so it equals $\left[\dfrac{n}{k} = 1\right]$. This expression is different from $0$ only at $n=k$, so in the end we get $g(n)$.

??? note "Proof 2"
    Using the Dirichlet convolution, the statement is equivalent to
    
    $$
    f = 1 * g \iff g = \mu * f.
    $$
    
    Using $1 * \mu = \varepsilon$ and convolving both sides of the left equation with $\mu$, we get
    
    $$
    f * \mu = (1 * g) * \mu = (1 * \mu) * g = \varepsilon * g = g.
    $$

In sums of arithmetic functions involving various divisibility relations, Möbius inversion is a powerful transformation tool.

???+ example "Examples"
    1.  [Euler's totient function](./euler-totient.md) $\varphi(n)$ satisfies the relation $n = \sum_{d\mid n}\varphi(d)$, i.e. $\mathrm{id}=1*\varphi$. Inverting it gives $\varphi = \mu * \mathrm{id}$, i.e.
    
        $$
        \varphi(n) = \sum_{d\mid n}d\mu\left(\dfrac{n}{d}\right).
        $$
    2.  The divisor function $\sigma_k(n) = \sum_{d\mid n}d^k$, i.e. $\sigma_k = 1 * \mathrm{id}_k$. Inverting it gives $\mathrm{id}_k = \mu * \sigma_k$, i.e.
    
        $$
        n^k = \sum_{d\mid n}\mu\left(\dfrac{n}{d}\right)\sigma_k(d).
        $$
    3.  The number-of-distinct-prime-factors function $\omega(n)=\sum_{d\mid n}[d\in\mathbf P]$, i.e. $\omega = 1* \mathbf{1}_{\mathbf P}$, where $\mathbf{1}_{\mathbf P}$ is the indicator function of the set of primes $\mathbf P$. Inverting it gives $\mathbf{1}_{\mathbf P} = \mu * \omega$, i.e.
    
        $$
        [n\in\mathbf P] = \sum_{d\mid n}\mu\left(\dfrac{n}{d}\right)\omega(d).
        $$
    4.  Consider the arithmetic function $\Lambda(n)$ satisfying $\log n = \sum_{d\mid n}\Lambda(d)$. It is the Möbius inversion of the logarithm function, also called the von Mangoldt function:
    
        $$
        \Lambda(n) = \sum_{d\mid n}\mu\left(\dfrac{n}{d}\right)\log d = 
        \begin{cases}
        \log p, & n = p^e,~p\in\mathbf P,~e\in\mathbf N_+, \\
        0, &\text{otherwise}.
        \end{cases}
        $$

??? note "Appendix: proof of the expression for $\Lambda(n)$"
    For a prime power $n=p^e~(e\in\mathbf N_+)$,
    
    $$
    \Lambda(n) = \sum_{i=0}^e\mu(p^{e-i})\log p^i = \log p^{e} - \log p^{e-1} = \log p.
    $$
    
    For $n=1$, clearly $\Lambda(n)=\log 1=0$. For other composite $n$,
    
    $$
    \Lambda(n) = \sum_{d\mid n}\mu(d)(\log n-\log d) = \left(\sum_{d\mid n}\mu(d)\right)\log n-\sum_{d\mid n}\mu(d)\log d.
    $$
    
    By the property of the Möbius function, the coefficient of the $\log n$ term is $[n=1]=0$. For the latter term, $d$ can be further decomposed into a product of prime factors. For any prime $p\mid n$, let $n=p^em$ with $p\perp m$ (since $n$ is not a prime power, $m>1$), and consider the coefficient of $\log p$ (only squarefree $d$ contribute):
    
    $$
    -\sum_{p\mid d\mid n}\mu(d) = -\sum_{d'\mid m}\mu(pd') = \sum_{d'\mid m}\mu(d') = [m=1]=0.
    $$
    
    Hence, for composite $n$ with more than one prime factor, $\Lambda(n)=0$.

### Extended forms

Besides the basic form above, Möbius inversion has several common extended forms. First, consider its sum-over-multiples form.

???+ note "Extension 1"
    Let $f(n),g(n)$ be two arithmetic functions. Then
    
    $$
    f(n) = \sum_{n\mid d}g(d) \iff g(n) = \sum_{n\mid d}\mu\left(\dfrac{d}{n}\right)f(d).
    $$

??? note "Proof"
    By direct verification:
    
    $$
    \begin{aligned}
    \sum_{n\mid d}\mu\left(\dfrac{d}{n}\right)f(d)
    &= \sum_{n\mid d}\mu\left(\dfrac{d}{n}\right)\sum_{d\mid k}g(k)\\
    &= \sum_{n\mid k}g(k)\sum_{d}[n\mid d\mid k]\mu\left(\dfrac{d}{n}\right)\\
    &= \sum_{n\mid k}g(k)\sum_{n\mid d}\left[\dfrac{d}{n}\mid\dfrac{k}{n}\right]\mu\left(\dfrac{d}{n}\right)\\
    &= \sum_{n\mid k}g(k)\left[\dfrac{k}{n}=1\right]\\
    &= g(n).
    \end{aligned}
    $$
    
    This is completely dual to the derivation of the basic form.

Second, Möbius inversion is not limited to addition; it actually holds for the operation of any [abelian group](../algebra/basic.md#群). For example, it has the following multiplicative form:

???+ note "Extension 2"
    Let $f(n),g(n)$ be two arithmetic functions. Then
    
    $$
    f(n) = \prod_{d\mid n}g(d) \iff g(n) = \prod_{d\mid n}f(d)^{\mu(n/d)}.
    $$

??? note "Proof"
    By direct verification:
    
    $$
    \begin{aligned}
    \prod_{d\mid n}f(d)^{\mu(n/d)}
    &= \prod_{d\mid n}\left(\prod_{k\mid d}g(k)\right)^{\mu(n/d)}\\
    &= \prod_{k\mid n}g(k)\uparrow\left(\sum_d[k\mid d\mid n]\mu\left(\dfrac{n}{d}\right)\right)\\
    &= \prod_{k\mid n}g(k)\uparrow\left(\sum_{d\mid n}\left[\frac{n}{d}\mid\frac{n}{k}\right]\mu\left(\dfrac{n}{d}\right)\right)\\
    &= \prod_{k\mid n}g(k)\uparrow\left[\frac{n}{k} = 1\right] \\
    &= g(n).
    \end{aligned}
    $$
    
    Here $a\uparrow b = a^b$ is Knuth's arrow. Comparing with the proof of the basic form, the only difference is that addition is replaced by multiplication, and multiplication by exponentiation.

From the viewpoint of the Dirichlet convolution, Möbius inversion only uses the fact that "the Möbius function is the Dirichlet inverse of the constant function". It is easy to imagine that relations similar to Möbius inversion also hold for a general [Dirichlet inverse](./dirichlet.md#dirichlet-convolution).

???+ note "Extension 3"
    Let $f(n),g(n),\alpha(n)$ be arithmetic functions, and let $\alpha^{-1}(n)$ be the Dirichlet inverse of $\alpha(n)$, i.e.
    
    $$
    [n=1] = \sum_{d\mid n}\alpha\left(\dfrac{n}{d}\right)\alpha^{-1}(d).
    $$
    
    Then
    
    $$
    f(n) = \sum_{d\mid n}\alpha\left(\dfrac{n}{d}\right)g(d) \iff g(n) = \sum_{d\mid n}\alpha^{-1}\left(\dfrac{n}{d}\right)f(d).
    $$

??? note "Proof"
    By direct verification:
    
    $$
    \begin{aligned}
    \sum_{d\mid n}\alpha^{-1}\left(\dfrac{n}{d}\right)f(d)
    &= \sum_{d\mid n}\alpha^{-1}\left(\dfrac{n}{d}\right)\sum_{k\mid d}\alpha\left(\dfrac{d}{k}\right)g(k)\\
    &= \sum_{k\mid n}g(k)\sum_d[k\mid d\mid n]\alpha\left(\dfrac{d}{k}\right)\alpha^{-1}\left(\dfrac{n}{d}\right)\\
    &= \sum_{k\mid n}g(k)\sum_{d\mid n}\left[\frac{n}{d}\mid\frac{n}{k}\right]\alpha\left(\dfrac{d}{k}\right)\alpha^{-1}\left(\dfrac{n/k}{d/k}\right)\\
    &= \sum_{k\mid n}g(k)\left[\frac{n}{k} = 1\right] \\
    &= g(n).
    \end{aligned}
    $$
    
    Compared with the proof of the basic form, one only needs to replace the second-to-last equality with the defining formula of the Dirichlet inverse.

???+ note "Corollary"
    Let $f(n),g(n)$ be arithmetic functions and let $t(n)$ be a completely multiplicative function. Then
    
    $$
    f(n) = \sum_{d\mid n}t\left(\dfrac{n}{d}\right)g(d) \iff g(n) = \sum_{d\mid n}\mu\left(\dfrac{n}{d}\right)t\left(\dfrac{n}{d}\right)f(d).
    $$

??? note "Proof"
    By the [properties](./dirichlet.md#properties) of the Dirichlet convolution, the Dirichlet inverse of a completely multiplicative function $t(n)$ is $\mu(n)t(n)$.

Finally, Möbius inversion can also be generalized to complex-valued functions on $[1,+\infty)$, not just arithmetic functions. The basic form of Möbius inversion can be viewed as the special case in which the complex-valued function is zero at all non-integer points.

???+ note "Extension 4"
    Let $F(x)$ and $G(x)$ be complex-valued functions on $[1,+\infty)$. Then
    
    $$
    F(x) = \sum_{n = 1}^{\lfloor x\rfloor}G\left(\dfrac{x}{n}\right) \iff G(x) = \sum_{n = 1}^{\lfloor x\rfloor}\mu(n)F\left(\dfrac{x}{n}\right).
    $$

??? note "Proof"
    Without loss of generality, extend the definitions of $F$ and $G$ so that $F(x)=G(x)=0$ whenever $x < 1$. Then the statement is equivalent to:
    
    $$
    F(x) = \sum_n G\left(\dfrac{x}{n}\right) \iff G(x) = \sum_n \mu(n)F\left(\dfrac{x}{n}\right).
    $$
    
    All these sums are over $n\in\mathbf N_+$.
    
    By direct verification:
    
    $$
    \begin{aligned}
    \sum_n \mu(n)F\left(\dfrac{x}{n}\right)
    &= \sum_n\mu(n)\sum_d G\left(\dfrac{x/n}{d}\right)\\
    &= \sum_k G\left(\dfrac{x}{k}\right)\sum_{n\mid k}\mu(n)\\
    &= \sum_k G\left(\dfrac{x}{k}\right)[k=1]\\
    &= G(x).
    \end{aligned}
    $$
    
    Here, to obtain the second equality, set $k = nd$.

???+ note "Corollary"
    Let $f(n),g(n)$ be arithmetic functions. Then
    
    $$
    f(n) = \sum_{k=1}^ng\left(\left\lfloor\dfrac{n}{k}\right\rfloor\right) \iff g(n)=\sum_{k=1}^n\mu(k)f\left(\left\lfloor\dfrac{n}{k}\right\rfloor\right).
    $$

??? note "Proof"
    Just take $F(x)=f(\lfloor x\rfloor)$ and $G(x)=g(\lfloor x\rfloor)$.

These extended forms can be combined with each other to obtain more complex inversion relations.

### Dirichlet prefix sums

Prerequisites: [Prefix sums and difference arrays](../../basic/prefix-sum.md)

Consider the basic form of the Möbius inversion relation:

$$
f(n) = \sum_{d\mid n}g(d) \iff g(n) = \sum_{d\mid n}\mu\left(\dfrac{n}{d}\right)f(d).
$$

In the left equation, the value $f(n)$ is the sum of the values of $g$ at all divisors of $n$. If we interpret $a\mid b$ as "$a$ comes before $b$", then $f(n)$ can be understood as a prefix sum of $g(n)$ in a certain sense. Therefore, in the Chinese competitive programming community, the process of computing $\{f(k)\}_{k=1}^n$ from $\{g(k)\}_{k=1}^n$ is also called the **Dirichlet prefix sum**, and the corresponding inverse process is called the Dirichlet difference. These methods mostly appear when the values of some arithmetic function at the first $N$ points need to be precomputed.

Next, we discuss the computation of Dirichlet prefix sums. If each prime is regarded as a dimension, this is a kind of multidimensional prefix sum. Recall the [dimension-by-dimension prefix sum algorithm](../../basic/prefix-sum.md#dimension-by-dimension-prefix-sums) for multidimensional prefix sums: iterate over all dimensions one by one, and add the value at each position to its successor position in that dimension. For arithmetic functions, this amounts to iterating over all primes $p$ from small to large and adding the function value at $n$ to the value at $np$. This is the same traversal order as in the [sieve of Eratosthenes](./sieve.md#埃拉托斯特尼筛法). Therefore, this algorithm computes the Dirichlet prefix sum of a sequence of length $n$ in $O(n\log\log n)$ time. Similarly, dimension-by-dimension differences compute the Dirichlet difference of a sequence within the same time complexity.

???+ example "Reference implementation"
    === "Dirichlet prefix sum"
        ```cpp
        --8<-- "docs/math/code/mobius/mobius-func-3.cpp:presum"
        ```
    
    === "Dirichlet difference"
        ```cpp
        --8<-- "docs/math/code/mobius/mobius-func-3.cpp:diff"
        ```

This computation method can be generalized to the sum-over-multiples form (Extension 1), the multiplicative form (Extension 2), replacing the constant function by a completely multiplicative function (the corollary of Extension 3), and other extended forms.

## Example problems

This section uses example problems to show how to apply Möbius inversion, along with some common transformation techniques. First, one example problem introduces the basic technique for handling greatest-common-divisor conditions in sums.

???+ example "[Luogu P2522 \[HAOI 2011\] Problem b](https://www.luogu.com.cn/problem/P2522)"
    $T$ test cases. For each test case, evaluate:
    
    $$
    \sum_{i=x}^{n}\sum_{j=y}^{m}[\gcd(i,j)=k].
    $$
    
    Constraints: $1\le T,x,y,n,m,k\le 5\times 10^4$.

??? note "Solution"
    By inclusion-exclusion, the original expression can be split into $4$ parts, and the expression of each part has the form
    
    $$
    f(n,m,k)=\sum_{i=1}^{n}\sum_{j=1}^{m}[\gcd(i,j)=k].
    $$
    
    For such expressions, what follows is a standard derivation procedure: factor out the common divisor, apply the property of the Möbius function, and exchange the order of summation.
    
    First, since $i,j$ can only take multiples of $k$, this factor can be extracted first – this amounts to substituting $i=ki'$ and $j=kj'$, which gives:
    
    $$
    f(n,m,k)=\sum_{i=1}^{\lfloor n/k\rfloor}\sum_{j=1}^{\lfloor m/k\rfloor}[\gcd(i,j)=1].
    $$
    
    Then, by the property of the Möbius function:
    
    $$
    [\gcd(i,j)=1] = \sum_{d\mid\gcd(i,j)}\mu(d) = \sum_d[d\mid i][d\mid j]\mu(d).
    $$
    
    Substituting this into the expression and exchanging the order of summation gives:
    
    $$
    f(n,m,k)=\sum_d\mu(d)\left(\sum_{i=1}^{\lfloor n/k\rfloor}[d\mid i]\right)\left(\sum_{j=1}^{\lfloor m/k\rfloor}[d\mid j]\right).
    $$
    
    The benefit of this manipulation is that, for fixed $d$, the terms involving $i$ and $j$ in the sum separate from each other and can be summed independently. Next, since
    
    $$
    \sum_{i=1}^{\lfloor n/k\rfloor}[d\mid i] = \left\lfloor\dfrac{\lfloor n/k\rfloor}{d}\right\rfloor,~\sum_{j=1}^{\lfloor m/k\rfloor}[d\mid j]=\left\lfloor\dfrac{\lfloor m/k\rfloor}{d}\right\rfloor,
    $$
    
    we have
    
    $$
    f(n,m,k)=\sum_d\mu(d)\left\lfloor\dfrac{\lfloor n/k\rfloor}{d}\right\rfloor\left\lfloor\dfrac{\lfloor m/k\rfloor}{d}\right\rfloor.
    $$
    
    After precomputing $\mu(d)$ with a linear sieve, together with its prefix sums, the problem can be solved with floor-division blocks. The total time complexity is $O(N + T\sqrt{N})$, where $N$ is the upper bound of $n,m$ and $T$ is the number of test cases.

??? note "Reference code"
    ```cpp
    --8<-- "docs/math/code/mobius/mobius_1.cpp"
    ```

The next two example problems show how to handle enumeration of a common divisor, and how to compute the values of general multiplicative functions with a [sieve](./sieve.md#一般的积性函数).

???+ example "[SPOJ LCMSUM](https://www.spoj.com/problems/LCMSUM/)"
    $T$ test cases. For each test case, evaluate:
    
    $$
    \sum_{i=1}^n \operatorname{lcm}(i,n).
    $$
    
    Constraints: $1\le T\le 3\times 10^5,~1\le n\le 10^6$.

??? note "Solution 1"
    The problem gives the least common multiple, but the greatest common divisor is usually easier to handle. So first transform:
    
    $$
    f(n)=\sum_{i=1}^n \operatorname{lcm}(i,n) = \sum_{i=1}^n \frac{i\cdot n}{\gcd(i,n)}.
    $$
    
    Factor out $n$ and enumerate the greatest common divisor $k$:
    
    $$
    f(n)=n\sum_{k\mid n}\sum_{i=1}^n\dfrac{i}{k}[\gcd(i,n)=k].
    $$
    
    The inner sum is the most common form involving a greatest common divisor; repeating the standard procedure gives:
    
    $$
    \begin{aligned}
    f(n) &= n\sum_{k\mid n}\sum_{i=1}^{n/k}i\left[\gcd\left(i,\dfrac{n}{k}\right)=1\right]\\
    &= n\sum_{k\mid n}\sum_{i=1}^{n/k}i\sum_d\mu(d)[d\mid i]\left[d\mid \dfrac{n}{k}\right]\\
    &= n\sum_{k\mid n}\sum_d\mu(d)\left[d\mid \dfrac{n}{k}\right]\left(\sum_{i=1}^{n/k}i[d\mid i]\right).
    \end{aligned}
    $$
    
    Once again, the sum over $i$ separates from the rest and can be handled on its own. The last sum is in fact the sum of an arithmetic progression (taking $i=di'$):
    
    $$
    \sum_{i=1}^{n/k}i[d\mid i] = d\frac{1}{2}\left(\dfrac{n}{kd}+1\right)\dfrac{n}{kd}=:dG\left(\dfrac{n}{kd}\right).
    $$
    
    This yields the following expression:
    
    $$
    f(n) = n\sum_{k\mid n}\sum_d\mu(d)\left[d\mid \dfrac{n}{k}\right]dG\left(\dfrac{n}{kd}\right).
    $$
    
    After enumerating a common divisor, double sums of this form are very common. There is likewise a fixed way to handle them: set the product as a new variable $\ell=kd$, then exchange the order of summation again. Since $d\mid(n/k)$ is equivalent to $d\mid\ell\mid n$, the original expression becomes:
    
    $$
    f(n) = n\sum_{\ell\mid n}G\left(\dfrac{n}{\ell}\right)\sum_{d\mid\ell}\mu(d)d.
    $$
    
    Let $F(\ell)=\sum_{d\mid\ell}\mu(d)d$; then the original expression has the form:
    
    $$
    f(n) = n\sum_{\ell\mid n}G\left(\dfrac{n}{\ell}\right)F(\ell).
    $$
    
    Since $\mu(d)d$ is multiplicative, its convolution $F(n)$ with the constant function $1$ is also multiplicative. Although the sum in the above expression has the form of a Dirichlet convolution, $G(n)$ is not multiplicative, so the sum as a whole is not multiplicative. However, $G(n)$ is a polynomial, so it is actually a linear combination of several completely multiplicative functions. Therefore,
    
    $$
    f(n) = \dfrac{1}{2}n\left(\sum_{\ell\mid n}\left(\dfrac{n}{\ell}\right)^2F(\ell) + \sum_{\ell\mid n}\dfrac{n}{\ell}F(\ell)\right).
    $$
    
    Both terms (without the coefficients) are multiplicative functions and can be precomputed directly with a linear sieve (or alternatively, the inner function can be computed with a linear sieve and then everything precomputed with Dirichlet prefix sums in $O(N\log\log N)$ time). Concretely, let
    
    $$
    H_s(n) = \sum_{\ell\mid n}\left(\dfrac{n}{\ell}\right)^sF(\ell),~s=1,2.
    $$
    
    To derive their expressions, it suffices to determine their values at prime powers. For a prime $p$ and a positive exponent $e$,
    
    $$
    \begin{aligned}
    F(p^e) &= \mu(1) + \mu(p)p + \sum_{j=2}^e\mu(p^j)p^j = 1-p,\\
    H_s(p^e) &= (p^e)^{s}F(1) + \sum_{j=1}^e(p^{e-j})^sF(p^j) = p^{es} + (1-p)\dfrac{1-p^{es}}{1-p^s},~s=1,2.
    \end{aligned}
    $$
    
    In particular, $H_1(p^e)=1$ is the constant function, while
    
    $$
    H_2(p^e) = p^{2e} + (1-p)\dfrac{1-p^{2e}}{1-p^2} = H_2(p^{e-1}) + p^{2e} - p^{2e-1}.
    $$
    
    This is easy to compute with a linear sieve. After precomputing $H_2(n)$ with a linear sieve, each query can be answered in $O(1)$ time via $f(n)=(n/2)(H_2(n)+1)$. The total time complexity is $O(N+T)$, where $N$ is the upper bound of $n$ and $T$ is the number of test cases.
    
    In the reference implementation, the linear sieve part is derived further using the special form of the expression in this problem; this is not necessary. Using only the values at prime powers, the precomputation can still be done in $O(N)$ time. These derivations are described in detail in Solution 2.

??? note "Solution 2"
    For this problem there is a more flexible approach. From Solution 1 we see that
    
    $$
    f(n) = n\sum_{k\mid n}\sum_{i=1}^{n/k}i\left[\gcd\left(i,\dfrac{n}{k}\right)=1\right] = n\sum_{k\mid n}F\left(\dfrac{n}{k}\right).
    $$
    
    If at this step we do not continue with Möbius inversion but observe that the subsequent sum is actually the sum of the integers not exceeding $d=n/k$ that are coprime to it. For $d>1$, since the integers coprime to $d$ come in pairs, i.e. $i$ and $d-i$ are necessarily coprime to $d$ at the same time, we have
    
    $$
    F(d)=\sum_{i=1}^{d}i[i\perp d] = \sum_{i=1}^{d}(d-i)[i\perp d] = \dfrac{1}{2}d\sum_{i=1}^{d}[i\perp d] = \dfrac{1}{2}d\varphi(d).
    $$
    
    For $d=1$, on the other hand,
    
    $$
    F(d)=1=\dfrac{1}{2}+\dfrac{1}{2}d\varphi(d).
    $$
    
    Hence, the original expression can be written as
    
    $$
    f(n) = \dfrac{1}{2}n\left(\sum_{d\mid n}d\varphi(d) + 1\right).
    $$
    
    Since $G(n)=\sum_{d\mid n}d\varphi(d)$ is the Dirichlet convolution of the multiplicative function $n\varphi(n)$ and the constant function $1$, it is also multiplicative and can be precomputed with a linear sieve. To this end, it suffices to determine its values at prime powers. For a prime $p$ and a positive exponent $e$,
    
    $$
    G(p^e) = 1 + \sum_{i=1}^ep^i\cdot p^{i-1}(p-1) = G(p^{e-1}) + p^{2e} - p^{2e-1}.
    $$
    
    We can see that this expression agrees with the result derived in Solution 1. The total time complexity of this method is still $O(N+T)$.
    
    Finally, using the expression of the multiplicative function in this problem, the computation in the linear sieve can be optimized further. For a prime $p$,
    
    $$
    G(p) = 1 - p + p^2.
    $$
    
    The key to the linear sieve is that, for a general $n$, we need to compute the value $G(pn)$. This further splits into two cases. When $p\perp n$, since $G$ is multiplicative,
    
    $$
    G(pn) = G(p)G(n).
    $$
    
    Otherwise, when $p\mid n$, let $n=p^em$ with $p\perp m$; then
    
    $$
    \begin{aligned}
    G(pn) &= G(p^{e+1})G(m)\\
    &= G(p^e)G(m) + (p^{2e+2} - p^{2e+1})G(m)\\
    &= G(n) + (p^{2e+2} - p^{2e+1})G(m).
    \end{aligned}
    $$
    
    A direct check shows that this expression also holds for the case $p\perp n$ (i.e. $e=0$). And when $p\mid n$, we also have
    
    $$
    G(n) - G\left(\dfrac{n}{p}\right) = (p^{2e}-p^{2e-1})G(m).
    $$
    
    Substituting into the above expression gives
    
    $$
    G(pn) = G(n) + p^2\left(G(n) - G\left(\dfrac{n}{p}\right)\right).
    $$
    
    This simplifies the computation in the linear sieve part. Of course, this derivation is not necessary; for multiplicative functions without special properties, the linear sieve computation can be done directly using $G(pn)=G(p^{e+1})G(m)$.

??? note "Reference code"
    ```cpp
    --8<-- "docs/math/code/mobius/mobius_2.cpp"
    ```

???+ example "[BZOJ 2154 \[国家集训队\] Crash 的数字表格 (Crash's number table)](https://hydro.ac/p/bzoj-P2154)"
    Evaluate:
    
    $$
    \sum_{i=1}^n\sum_{j=1}^m\operatorname{lcm}(i,j)\mod{20101009}.
    $$
    
    Constraints: $1\le n,m\le 10^7$.

??? note "Solution"
    We ignore the modulus during the derivation. Let
    
    $$
    f(n,m) = \sum_{i=1}^n\sum_{j=1}^m\operatorname{lcm}(i,j).
    $$
    
    As before, convert the least common multiple into the greatest common divisor, enumerate the common divisor, and apply the standard procedure, which gives
    
    $$
    \begin{aligned}
    f(n,m)
    &= \sum_k\sum_{i=1}^n\sum_{j=1}^m\dfrac{ij}{k}[\gcd(i,j)=k] \\
    &= \sum_k\sum_{i=1}^{\lfloor n/k\rfloor}\sum_{j=1}^{\lfloor m/k\rfloor} kij[\gcd(i,j)=1]\\
    &= \sum_k\sum_{i=1}^{\lfloor n/k\rfloor}\sum_{j=1}^{\lfloor m/k\rfloor} kij\sum_d\mu(d)[d\mid i][d\mid j]\\
    &= \sum_kk\sum_d\mu(d)\left(\sum_{i=1}^{\lfloor n/k\rfloor}i[d\mid i]\right)\left(\sum_{j=1}^{\lfloor m/k\rfloor}j[d\mid j]\right).
    \end{aligned}
    $$
    
    Once again, the sum separates in $i$ and $j$. First compute these inner sums; extracting the factor (i.e. taking $i=di'$) gives
    
    $$
    \sum_{i=1}^{\lfloor n/k\rfloor}i[d\mid i] = d\sum_{i=1}^{\lfloor\lfloor n/k\rfloor/d\rfloor}i = dG\left(\left\lfloor\dfrac{\lfloor n/k\rfloor}{d}\right\rfloor\right) = dG\left(\left\lfloor\dfrac{n}{kd}\right\rfloor\right).
    $$
    
    Here $G(n)=\dfrac{1}{2}n(n+1)$ is just the sum of an arithmetic progression, and the last equality uses the property of the [floor function](./basic.md#取整函数). Symmetrically, the other sum can be computed in the same way. Substituting back into the earlier expression gives
    
    $$
    f(n,m) = \sum_k k\sum_{d}\mu(d)d^2G\left(\left\lfloor\dfrac{n}{kd}\right\rfloor\right)G\left(\left\lfloor\dfrac{m}{kd}\right\rfloor\right).
    $$
    
    As before, for such expressions that enumerate a common divisor, one usually needs to enumerate the product $\ell = kd$ and exchange the order of summation again:
    
    $$
    f(n,m) = \sum_{\ell}\left(\sum_{d\mid\ell}\mu(d)d\ell\right)G\left(\left\lfloor\dfrac{n}{\ell}\right\rfloor\right)G\left(\left\lfloor\dfrac{m}{\ell}\right\rfloor\right).
    $$
    
    Let
    
    $$
    F(\ell) = \sum_{d\mid\ell}\mu(d)d\ell.
    $$
    
    This is the product of the multiplicative function $\ell$ and the multiplicative function $\sum_{d\mid\ell}\mu(d)d$, so it is also multiplicative; it can be precomputed directly with a linear sieve, along with its prefix sums. Then the value of $f(n,m)$ can be computed with floor-division blocks. The total time complexity is $O(\min\{n,m\})$.

??? note "Reference code"
    ```cpp
    --8<-- "docs/math/code/mobius/mobius_3.cpp"
    ```

The next example problem is somewhat special: it requires transforming the divisor-counting function of a product.

???+ example "[LOJ 2185. \[SDOI2015\] 约数个数和 (Sum of the number of divisors)](https://loj.ac/problem/2185)"
    $T$ test cases. For each test case, evaluate:
    
    $$
    \sum_{i=1}^n\sum_{j=1}^m\sigma_0(ij).
    $$
    
    Here $\sigma_0(n)=\sum_{d \mid n}1$ denotes the number of divisors of $n$.
    
    Constraints: $1\le n,m,T\le 5\times 10^4$.

??? note "Solution"
    The difficulty of this problem is to transform $\sigma_0(ij)$ into an expression involving the greatest common divisor. Since $\sigma_0$ is multiplicative, first consider the case of prime powers. For a prime $p$ and non-negative exponents $e_1,e_2$, let $i=p^{e_1},~j=p^{e_2}$; then
    
    $$
    \sigma_0(ij) = 1 + e_1 + e_2 = \sum_{x\mid i}\sum_{y\mid j}[x\perp y].
    $$
    
    For the general case, let $i=\prod_p i_p$ and $j=\prod_p j_p$, where $i_p,j_p$ are the prime-power factors corresponding to $p$ in the prime factorizations of $i,j$ respectively. Then
    
    $$
    \sigma_0(ij) = \prod_p\sigma_0(i_pj_p)= \prod_p\sum_{x_p\mid i_p}\sum_{y_p\mid j_p}[x_p\perp y_p].
    $$
    
    Note that enumerating the divisors $x_p$ of each prime-power factor $i_p$ of $i$ is the same as enumerating the divisors $x$ of $i$ and then decomposing each into its prime-power factors $x_p$; similarly for $j$. Therefore, by the distributive law of multiplication, the expression becomes
    
    $$
    \sigma_0(ij) = \sum_{x\mid i}\sum_{y\mid j}\prod_p[x_p\perp y_p] = \sum_{x\mid i}\sum_{y\mid j}[x\perp y].
    $$
    
    The last step uses the fact that $x\perp y$ if and only if $x_p\perp y_p$ for every prime factor $p$.
    
    Having obtained this expression, we can apply the standard procedure:
    
    $$
    \begin{aligned}
    \sigma_0(ij) 
    &= \sum_{x\mid i}\sum_{y\mid j}[x\perp y]\\
    &= \sum_{x\mid i}\sum_{y\mid j}\sum_d\mu(d)[d\mid x][d\mid y]\\
    &= \sum_d\mu(d)\left(\sum_{x}[d\mid x\mid i]\right)\left(\sum_{y}[d\mid y\mid j]\right)\\
    &= \sum_d\mu(d)[d\mid i][d\mid j]\sigma_0\left(\dfrac{i}{d}\right)\sigma_0\left(\dfrac{j}{d}\right).
    \end{aligned}
    $$
    
    The meaning of the last step is: the function is nonzero only when $d\mid i$ and $d\mid j$, and in that case enumerating $x$ with $d\mid x\mid i$ is the same as enumerating the divisors $\dfrac{x}{d}$ of $\dfrac{i}{d}$; similarly for enumerating $y$ with $d\mid y\mid j$.
    
    Substitute this expression back into the original one and exchange the order of summation:
    
    $$
    \begin{aligned}
    f(n,m)
    &= \sum_{i=1}^n\sum_{j=1}^m\sigma_0(ij)\\
    &= \sum_{i=1}^n\sum_{j=1}^m\sum_d\mu(d)[d\mid i][d\mid j]\sigma_0\left(\dfrac{i}{d}\right)\sigma_0\left(\dfrac{j}{d}\right)\\
    &= \sum_d\mu(d)\left(\sum_{i=1}^n[d\mid i]\sigma_0\left(\dfrac{i}{d}\right)\right)\left(\sum_{j=1}^m[d\mid j]\sigma_0\left(\dfrac{j}{d}\right)\right)\\
    &= \sum_d\mu(d)\left(\sum_{i=1}^{\lfloor n/d\rfloor}\sigma_0(i)\right)\left(\sum_{j=1}^{\lfloor m/d\rfloor}\sigma_0(j)\right).
    \end{aligned}
    $$
    
    Let $G(n)=\sum_{i=1}^n\sigma_0(i)$; then
    
    $$
    f(n,m)=\sum_{d}\mu(d)G\left(\left\lfloor\dfrac{n}{d}\right\rfloor\right)G\left(\left\lfloor\dfrac{m}{d}\right\rfloor\right).
    $$
    
    This can be solved with floor-division blocks. It suffices to precompute the prefix sums of $\mu(n)$ and $\sigma_0(n)$. The total time complexity is $O(N+T\sqrt{N})$, where $N$ is the upper bound of $n,m$ and $T$ is the number of test cases.

??? note "Reference code"
    ```cpp
    --8<-- "docs/math/code/mobius/mobius_4.cpp"
    ```

The last example problem shows how to apply the multiplicative version of Möbius inversion.

???+ example "[Luogu P5221 Product](https://www.luogu.com.cn/problem/P5221)"
    Evaluate:
    
    $$
    \prod_{i=1}^n\prod_{j=1}^n\dfrac{\operatorname{lcm}(i,j)}{\gcd(i,j)}\pmod{104857601}.
    $$
    
    Constraints: $1\le n\le 1\times 10^6$.

??? note "Solution 1"
    We ignore the modulus during the derivation. Let
    
    $$
    f(n) = \prod_{i=1}^n\prod_{j=1}^n\dfrac{\operatorname{lcm}(i,j)}{\gcd(i,j)}.
    $$
    
    As before, convert the least common multiple into the greatest common divisor:
    
    $$
    f(n) = \prod_{i=1}^n\prod_{j=1}^n\dfrac{ij}{(\gcd(i,j))^2}.
    $$
    
    Note that the products of these factors are independent of each other and can be computed separately. Let
    
    $$
    g(n) = \prod_{i=1}^n\prod_{j=1}^n\gcd(i,j).
    $$
    
    The original expression then equals:
    
    $$
    f(n) = \dfrac{(n!)^{2n}}{g(n)^2}.
    $$
    
    The key is to compute $g(n)$. The procedure for handling it is similar to the one described above, but it must be replaced by the corresponding multiplicative version. First, enumerate and extract the common divisor:
    
    $$
    \begin{aligned}
    g(n) &= \prod_k\prod_{i=1}^n\prod_{j=1}^nk\uparrow[\gcd(i,j)=k]\\
    &= \prod_k\prod_{i=1}^{\lfloor n/k\rfloor}\prod_{j=1}^{\lfloor n/k\rfloor}k\uparrow[\gcd(i,j)=1].
    \end{aligned}
    $$
    
    Here $a\uparrow b=a^b$ is Knuth's arrow. Then substitute $[\gcd(i,j)=1]=\sum_d\mu(d)[d\mid i][d\mid j]$ and convert the sum in the exponent into a product of powers, obtaining:
    
    $$
    g(n) = \prod_k\prod_d\prod_{i=1}^{\lfloor n/k\rfloor}\prod_{j=1}^{\lfloor n/k\rfloor}k\uparrow(\mu(d)[d\mid i][d\mid j]).
    $$
    
    Further extract the factor (i.e. set $i=di'$, $j=dj'$) and apply the property of the [floor function](./basic.md#取整函数), obtaining:
    
    $$
    g(n) = \prod_k\prod_d\prod_{i=1}^{\lfloor n/(kd)\rfloor}\prod_{j=1}^{\lfloor n/(kd)\rfloor}k\uparrow\mu(d).
    $$
    
    Then separate the products over $i,j$ and notice that the factor does not involve $i,j$, so this amounts to raising the factor to a power:
    
    $$
    g(n) = \prod_k\prod_d k\uparrow\left(\mu(d)\left\lfloor\dfrac{n}{kd}\right\rfloor^2\right).
    $$
    
    Since we enumerated a common divisor earlier, the order of the product in this expression needs to be exchanged again. Setting $\ell = kd$, we have:
    
    $$
    \begin{aligned}
    g(n) &= \prod_{\ell}\prod_{d\mid\ell}\left(\dfrac{\ell}{d}\right)\uparrow\left(\mu(d)\left\lfloor\dfrac{n}{\ell}\right\rfloor^2\right)\\
    &= \prod_\ell\left(\prod_{d\mid\ell}\left(\dfrac{\ell}{d}\right)\uparrow\mu(d)\right)\uparrow\left\lfloor\dfrac{n}{\ell}\right\rfloor^2.
    \end{aligned}
    $$
    
    Let
    
    $$
    F(n) = \prod_{d\mid n}\left(\dfrac{n}{d}\right)\uparrow\mu(d).
    $$
    
    It is easy to see that this is the multiplicative-form Möbius inversion of $\tilde F(n)=n$. Even without knowing its expression, it can be precomputed with the [Dirichlet difference](#dirichlet-prefix-sums) method in $O(n\log\log n)$ time. Of course, since the form of $\tilde F(n)$ is very simple, the expression of $F(n)$ can be found directly:
    
    $$
    F(n) = 
    \begin{cases}
    p, & n = p^e,~p\in\mathbf P,~e\in\mathbf N_+, \\
    1, &\text{otherwise}.
    \end{cases}
    $$
    
    The [von Mangoldt function](#möbius-inversion) is exactly its natural logarithm. After obtaining the values of $F(n)$, directly applying the product version of floor-division blocks computes $g(n)$ in $O(\sqrt{n})$ time, and hence $f(n)$. The total time complexity is $O(n)$.
    
    It is worth noting that computations involving products often require [Euler's theorem](./fermat.md), so the modulus used for the exponents is not the same as the modulus given in the problem.

??? note "Solution 2"
    The difficulty of the multiplicative-version derivation is that handling products and powers is relatively unfamiliar; therefore, for such problems one can also take logarithms first and then derive. For this problem, we only consider the derivation of $g(n)$. Taking logarithms gives:
    
    $$
    \log g(n) = \sum_{i=1}^n\sum_{j=1}^n\log\gcd(i,j).
    $$
    
    For such expressions involving the greatest common divisor, directly applying the standard derivation procedure gives:
    
    $$
    \begin{aligned}
    \log g(n) 
    &= \sum_k\log k\sum_{i=1}^n\sum_{j=1}^n[\gcd(i,j)=k]\\
    &= \sum_k\log k\sum_{i=1}^{\lfloor n/k\rfloor}\sum_{j=1}^{\lfloor n/k\rfloor}[\gcd(i,j)=1]\\
    &= \sum_k\log k\sum_d\mu(d)\left(\sum_{i=1}^{\lfloor n/k\rfloor}[d\mid i]\right)\left(\sum_{j=1}^{\lfloor n/k\rfloor}[d\mid j]\right)\\
    &= \sum_k\log k\sum_d\mu(d)\left\lfloor\dfrac{n}{kd}\right\rfloor^2\\
    &= \sum_{\ell}\left(\sum_{d\mid\ell}\mu(d)\log\dfrac{\ell}{d}\right)\left\lfloor\dfrac{n}{\ell}\right\rfloor^2\\
    &= \sum_{\ell}\Lambda(\ell)\left\lfloor\dfrac{n}{\ell}\right\rfloor^2.
    \end{aligned}
    $$
    
    Here $\Lambda(n)$ is the [von Mangoldt function](#möbius-inversion). Exponentiating this result gives the result of Solution 1.

??? note "Reference code"
    ```cpp
    --8<-- "docs/math/code/mobius/mobius_5.cpp"
    ```

## Exercises

-   [Luogu P3312 \[SDOI2014\] 数表 (Number table)](https://www.luogu.com.cn/problem/P3312)
-   [Luogu P3700 \[CQOI2017\] 小 Q 的表格 (Little Q's table)](https://www.luogu.com.cn/problem/P3700)
-   [Luogu P3704 \[SDOI2017\] 数字表格 (Number table)](https://www.luogu.com.cn/problem/P3704)
-   [Luogu P3768 简单的数学题 (A simple math problem)](https://www.luogu.com.cn/problem/P3768)
-   [Luogu P4464 \[国家集训队\] JZPKIL](https://www.luogu.com.cn/problem/P4464)
-   [Luogu P4619 \[SDOI2018\] 旧试题 (Old exam problem)](https://www.luogu.com.cn/problem/P4619)
-   [Luogu P5518 \[MtOI2019\] 幽灵乐团 (Ghost orchestra)](https://www.luogu.com.cn/problem/P5518)
-   [Luogu P6222 简单题 加强版 (Simple problem, hard version)](https://www.luogu.com.cn/problem/P6222)
-   [Luogu P6825「EZEC-4」求和 (Summation)](https://www.luogu.com.cn/problem/P6825)
-   [Luogu P7486「Stoi2031」彩虹 (Rainbow)](https://www.luogu.com.cn/problem/P7486)
-   [AtCoder Grand Contest 038 C - LCMs](https://atcoder.jp/contests/agc038/tasks/agc038_c)
-   [Codeforces 1139 D. Steps to One](https://codeforces.com/problemset/problem/1139/D)

## References

-   [Möbius function - Wikipedia](https://en.wikipedia.org/wiki/M%C3%B6bius_function)
-   [Möbius inversion formula - Wikipedia](https://en.wikipedia.org/wiki/M%C3%B6bius_inversion_formula)
-   [Von Mangoldt function - Wikipedia](https://en.wikipedia.org/wiki/Von_Mangoldt_function)
-   [algocode 算法博客 (algocode algorithm blog)](https://web.archive.org/web/20190523150159/https://algocode.net/2018/04/18/20180418-KB-Mobius-Inversion-Formula/)
