---
title: Euler's totient function
---

## Definition

Euler's totient function, i.e., $\varphi(n)$, denotes the number of integers less than or equal to $n$ that are coprime to $n$.

For example, $\varphi(1) = 1$.

When $n$ is prime, obviously $\varphi(n) = n - 1$.

## Properties

-   Euler's totient function is a [multiplicative function](./basic.md#积性函数).

    That is, for any integers $a,b$ with $\gcd(a, b) = 1$, we have $\varphi(ab) = \varphi(a)\varphi(b)$.

    In particular, when $n$ is odd, $\varphi(2n) = \varphi(n)$.

    For a proof, see [Composition of residue systems](./basic.md#剩余系的复合).

-   $n = \sum_{d \mid n}{\varphi(d)}$.

    ???+ note "Proof"
        This can be derived using knowledge of [Möbius inversion](./mobius.md).
        
        One can also think of it this way: if $\gcd(k, n) = d$, then $\gcd(\dfrac{k}{d},\dfrac{n}{d}) = 1, ( k < n )$.
        
        If we let $f(x)$ denote the number of integers with $\gcd(k, n) = x$, then $n = \sum_{i = 1}^n{f(i)}$.
        
        By the proof above, we find that $f(x) = \varphi(\dfrac{n}{x})$, hence $n = \sum_{d \mid n}\varphi(\dfrac{n}{d})$. Note that the divisors $d$ and $\dfrac{n}{d}$ are symmetric, so the formula above becomes $n = \sum_{d \mid n}\varphi(d)$.

-   If $n = p^k$, where $p$ is prime, then $\varphi(n) = p^k - p^{k - 1}$.
    (follows from the definition)

-   By the fundamental theorem of arithmetic, let $n = \prod_{i=1}^{s}p_i^{k_i}$, where the $p_i$ are primes; then $\varphi(n) = n \times \prod_{i = 1}^s{\dfrac{p_i - 1}{p_i}}$.

    ???+ note "Proof"
        -   Lemma: let $p$ be any prime; then $\varphi(p^k)=p^{k-1}\times(p-1)$.
        
            Proof: obviously, among all the numbers from $1$ to $p^k$, all except the $p^{k-1}$ multiples of $p$ are coprime to $p^k$, so $\varphi(p^k)=p^k-p^{k-1}=p^{k-1}\times(p-1)$, which completes the proof.
        
        Next we prove $\varphi(n) = n \times \prod_{i = 1}^s{\dfrac{p_i - 1}{p_i}}$. By the fundamental theorem of arithmetic and the multiplicativity of the function $\varphi(x)$,
        
        $$
        \begin{aligned}
            \varphi(n) &= \prod_{i=1}^{s} \varphi(p_i^{k_i}) \\
            &= \prod_{i=1}^{s} (p_i-1)\times {p_i}^{k_i-1}\\
            &=\prod_{i=1}^{s} {p_i}^{k_i} \times(1 - \frac{1}{p_i})\\
            &=n~ \prod_{i=1}^{s} (1- \frac{1}{p_i})
            &\square
        \end{aligned}
        $$

-   For any positive integers $m,n$, $\varphi(mn)\varphi(\gcd(m,n))=\varphi(m)\varphi(n)\gcd(m,n)$.

    This follows by direct computation from the previous property.

## Implementation

If only the totient of a single number is needed, just compute it directly from the definition while doing the prime factorization. This process can be optimized with the [Pollard rho](./pollard-rho.md) algorithm.

???+ note "Reference implementation"
    === "C++"
        ```cpp
        #include <cmath>
        
        int euler_phi(int n) {
          int ans = n;
          for (int i = 2; i * i <= n; i++)
            if (n % i == 0) {
              ans = ans / i * (i - 1);
              while (n % i == 0) n /= i;
            }
          if (n > 1) ans = ans / n * (n - 1);
          return ans;
        }
        ```
    
    === "Python"
        ```python
        import math
        
        
        def euler_phi(n):
            ans = n
            for i in range(2, math.isqrt(n) + 1):
                if n % i == 0:
                    ans = ans // i * (i - 1)
                    while n % i == 0:
                        n = n // i
            if n > 1:
                ans = ans // n * (n - 1)
            return ans
        ```

If the totients of several numbers are needed, they can be computed with the linear sieve, which will be introduced later.

For details, see: [Computing Euler's totient function with a sieve](./sieve.md#筛法求欧拉函数)

## Applications

Euler's totient function is often used to simplify a sum of greatest common divisors. Some Chinese articles call this **Euler inversion**[^1].

Substituting $n=\gcd(a,b)$ into the result

$$
n=\sum_{d \mid n}\varphi(d)
$$

we get

$$
\gcd(a,b) = \sum_{d \mid \gcd(a,b)}\varphi(d) = \sum_d [d \mid a][d \mid b]\varphi(d),
$$

where $[\cdot]$ is the Iverson bracket. Summing the formula above, we obtain

$$
\sum_{i=1}^n\gcd(i,n)=\sum_{d}\sum_{i=1}^n[d \mid i][d \mid n]\varphi(d)=\sum_d\left\lfloor\frac{n}{d}\right\rfloor[d \mid n]\varphi(d)=\sum_{d \mid n}\left\lfloor\frac{n}{d}\right\rfloor\varphi(d).
$$

The key observation here is $\sum_{i=1}^n[d \mid i]=\lfloor\frac{n}{d}\rfloor$, i.e., the number of integers $i$ between $1$ and $n$ divisible by $d$ is $\lfloor\frac{n}{d}\rfloor$.

Using this formula, we can compute the sum by iterating over the divisors. When multiple queries are needed, we can precompute the prefix sums of Euler's totient function and answer queries with floor-division blocks (number-theoretic blocking).

???+ note "[GCD SUM](https://www.luogu.com.cn/problem/P2398)"
    Given $n\le 100000$, compute
    
    $$
    \sum_{i=1}^n\sum_{j=1}^n\gcd(i,j).
    $$
    
    ??? note "Idea"
        Following the derivation above, we obtain
        
        $$
        \sum_{i=1}^n\sum_{j=1}^n\gcd(i,j) = \sum_{d=1}^n\left\lfloor\frac{n}{d}\right\rfloor^2\varphi(d).
        $$
        
        Here we need the totients of all numbers from $1$ to $n$; using the linear sieve, the answer is obtained in $O(n)$.

## Euler's theorem

A theorem closely related to Euler's totient function is Euler's theorem. It states the following:

If $\gcd(a, m) = 1$, then $a^{\varphi(m)} \equiv 1 \pmod{m}$.

### Extended Euler's theorem

Of course, there is also the extended Euler's theorem, which handles the case of general $a$ and $m$.

$$
a^b\equiv
\begin{cases}
a^{b\bmod\varphi(m)},\,&\gcd(a,\,m)=1\\
a^b,&\gcd(a,\,m)\ne1,\,b<\varphi(m)\\
a^{b\bmod\varphi(m)+\varphi(m)},&\gcd(a,\,m)\ne1,\,b\ge\varphi(m)
\end{cases}
\pmod m
$$

For the proof and exercises, see [Euler's theorem](./fermat.md).

## Exercises

-   [SPOJ ETF. Euler Totient Function](http://www.spoj.com/problems/ETF/)
-   [UVa 10179. Irreducible Basic Fractions](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1120)
-   [UVa 10299. Relatives](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1240)
-   [UVa 11327. Enumerating Rational Numbers](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2302)
-   [TIMUS 1673. Admission to Exam](http://acm.timus.ru/problem.aspx?space=1&num=1673)
-   [Luogu P1390 公约数的和 (Sum of common divisors)](https://www.luogu.com.cn/problem/P1390)
-   [Luogu P2155 \[SDOI2008\] 沙拉公主的困惑 (Princess Salad's puzzle)](https://www.luogu.com.cn/problem/P2155)
-   [Luogu P2568 GCD](https://www.luogu.com.cn/problem/P2568)

## References and notes

[^1]: This term does not appear in academic journals or in forums outside China, so care should be taken when using it.
