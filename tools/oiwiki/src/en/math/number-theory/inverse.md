---
title: Modular inverse
---

This article introduces the inverse with respect to multiplication in modular arithmetic and discusses common methods of computing it.

## Basic concepts

The multiplicative inverse of a nonzero real number $a\in\mathbf R$ is its reciprocal $a^{-1}$. Similarly, in number theory one can define the inverse of an integer $a$ modulo $m$, $a^{-1}\bmod m$, or simply $a^{-1}$. This is the **modular multiplicative inverse**, also called the **number-theoretic reciprocal**.

???+ abstract "Inverse"
    For an integer $a$ and a positive integer $m$, if there exists $b$ such that $ab\equiv 1\pmod m$, then $b$ is called the **inverse** of $a$ modulo $m$.

This amounts to saying that $b$ is a solution of the linear congruence $ax\equiv 1\pmod m$. By the properties of [linear congruences](./linear-equation.md), the inverse $a^{-1}\bmod m$ exists if and only if $\gcd(a,m)=1$, i.e. $a,m$ are coprime, and in that case it is unique modulo $m$.

## Computing a single inverse

Using the extended Euclidean algorithm or binary exponentiation, the inverse of a single integer can be computed in $O(\log m)$ time.

### Extended Euclidean algorithm

Computing an inverse is equivalent to solving a linear congruence. Therefore, the [extended Euclidean algorithm](./gcd.md#扩展欧几里得算法) can be used to compute the inverse in $O(\log\min\{a,m\})$ time. At the same time, since the linear equation corresponding to the inverse is rather special, the corresponding steps can be simplified appropriately.

???+ example "Reference implementation"
    === "C++"
        ```cpp
        --8<-- "docs/math/code/inverse/inverse-1.cpp:core"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/math/code/inverse/inverse-1.py:core"
        ```

This algorithm applies to all cases in which the inverse exists.

### Binary exponentiation method

This method mainly applies when the modulus is a prime $p$. In that case, by [Fermat's little theorem](./fermat.md#fermats-little-theorem), for every $a\perp p$ we have

$$
a\cdot a^{p-2} = a^{p-1} \equiv 1 \pmod p.
$$

By the uniqueness of the inverse, the inverse $a^{-1}\bmod p$ equals $a^{p-2}\bmod p$, so it can be computed directly by [binary exponentiation](../binary-exponentiation.md) in $O(\log p)$ time:

???+ example "Reference implementation"
    === "C++"
        ```cpp
        --8<-- "docs/math/code/inverse/inverse-2.cpp:core"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/math/code/inverse/inverse-2.py:core"
        ```

Of course, in theory this method can be generalized to the case of a general modulus $m$ using [Euler's theorem](./fermat.md#eulers-theorem), i.e. the inverse can be computed as $a^{\varphi(m)-1}\bmod m$. However, computing [Euler's totient function](./euler-totient.md) $\varphi(m)$ for a single value is not easy, so this algorithm is not efficient in the general case.

## Computing several inverses

In some scenarios, it is necessary to quickly compute the inverses of several integers $a_1,a_2,\cdots,a_n$ modulo $m$. Computing the inverses one by one takes $O(n\log m)$ time in total. In fact, if they are processed together, the inverses of all the integers can be computed in $O(n+\log m)$ time.

Consider the prefix products of the sequence $\{a_i\}$:

$$
S_0 = 1,~ S_i = a_iS_{i-1},~ i=1,2,\cdots,n.
$$

As long as every $a_i$ is coprime to $m$, their product $S_n$ is coprime to $m$. Therefore, the value $S_n^{-1}\bmod m$ can be computed by the algorithm described above. Since the inverse of a product is the product of the inverses, starting from $S_n^{-1}$ and traversing the sequence backwards, the inverse of every $S_i$ can be computed:

$$
S_{i-1}^{-1} = a_iS_i^{-1} \bmod m,~ i = n,n-1,\cdots,1.
$$

From this, the inverse of a single $a_i$ can be computed by the following formula:

$$
a_i^{-1} = S_{i-1}S_i^{-1} \bmod m,~ i = 1,2,\cdots,n.
$$

A reference implementation follows:

???+ example "Reference implementation"
    === "C++"
        ```cpp
        --8<-- "docs/math/code/inverse/inverse-3.cpp:core"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/math/code/inverse/inverse-3.py:core"
        ```

In the algorithm, the inverse of a single element is computed only once, so the total time complexity is $O(n+\log m)$.

## Precomputing inverses in linear time

If the inverses of the first $n$ positive integers modulo a prime $p$ need to be precomputed, this can also be done in $O(n)$ time through the recurrence discussed in this section. This method is often used in binomial coefficient computations to precompute the inverses of the factorials of the first $n$ positive integers.

For a positive integer $i$ with $1< i < p$, consider division with remainder:

$$
p = \left\lfloor \dfrac{p}{i} \right\rfloor i + (p\bmod i).
$$

Taking this equation modulo the prime $p$, we get

$$
0 \equiv \left\lfloor \dfrac{p}{i} \right\rfloor i + (p\bmod i) \pmod p.
$$

Multiplying both sides by $i^{-1}(p\bmod i)^{-1}$ gives

$$
i^{-1} \equiv - \left\lfloor \dfrac{p}{i} \right\rfloor (p\bmod i)^{-1} \pmod p.
$$

This is the formula used for computing inverses recursively in linear time. Since $p\bmod i < i$, this formula reduces the problem of computing $i^{-1}\bmod p$ to the smaller problem $(p\bmod i)^{-1}\bmod p$. Therefore, starting from $1^{-1}\bmod p=1$ and applying the formula to each $i$ in turn, the inverses of the first $n$ integers can be obtained in $O(n)$ time.

A reference implementation follows:

???+ example "Reference implementation"
    === "C++"
        ```cpp
        --8<-- "docs/math/code/inverse/inverse-4.cpp:core"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/math/code/inverse/inverse-4.py:core"
        ```

This algorithm applies only when the modulus is prime. When the modulus $m$ is not prime, there is no guarantee that the $m\bmod i$ obtained in the recurrence is still coprime to $m$, so the $(m\bmod i)^{-1}$ required by the recurrence may not exist. One such example is $m=8,i=3$. In that case $m\bmod i = 2$, which has no inverse modulo $m$.

Moreover, once this recurrence is obtained, a natural idea is to compute the inverse of an arbitrary number $a$ directly by recursion. At each step of the recursion, the formula reduces it to the inverse of the smaller remainder $p\bmod a$, stopping when the remainder becomes $1$. The complexity of doing so is currently unknown[^linear-recursion], so it is recommended to use the conventional methods described above.

## Exercises

-   [LOJ 110 乘法逆元 (Multiplicative Inverse)](https://loj.ac/problem/110)
-   [LOJ 161 乘法逆元 2 (Multiplicative Inverse 2)](https://loj.ac/problem/161)
-   [LOJ 2605「NOIP2012」同余方程 (Congruence Equation)](https://loj.ac/problem/2605)
-   [Luogu P2054「AHOI2005」洗牌 (Shuffling Cards)](https://www.luogu.com.cn/problem/P2054)
-   [LOJ 2034「SDOI2016」排列计数 (Counting Permutations)](https://loj.ac/problem/2034)

## References and notes

-   [Modular multiplicative inverse - Wikipedia](https://en.wikipedia.org/wiki/Modular_multiplicative_inverse)

[^linear-recursion]: [riteme's answer on Zhihu](https://www.zhihu.com/question/59033693/answer/323292359) points out that the theoretically known upper bound on the complexity of doing so is $O(p^{1/3+\varepsilon})$, while the behavior on real random data is close to $O(\log p)$.
