---
title: Min_25 sieve
---

## Definition

In terms of the idea behind it, this sieve method is also called the "Extended Eratosthenes Sieve".

Since it was invented and first used by [Min\_25](https://web.archive.org/web/20211104125457/http://min-25.hatenablog.com/), it is called the "Min\_25 sieve".

## Properties

It can solve the prefix-sum problem for a class of **multiplicative functions** in $O\left(\frac{n^{\frac{3}{4}}}{\log{n}}\right)$ or $\Theta\left(n^{1 - \epsilon}\right)$ time complexity.

Requirements: $f(p)$ is a sum of completely multiplicative functions in $p$ that can be evaluated quickly (e.g., a polynomial); $f(p^{c})$ can be evaluated quickly.

## Notation

-   **Unless stated otherwise, every variable denoted by $p$ in this section takes values in the set of all primes.**
-   $x / y := \left\lfloor\frac{x}{y}\right\rfloor$
-   $\operatorname{isprime}(n) := [ |\{d : d \mid n\}| = 2 ]$, i.e., its value is $1$ when $n$ is prime and $0$ otherwise.
-   $p_{k}$: the $k$-th smallest prime among all primes (e.g., $p_{1} = 2, p_{2} = 3$). In particular, let $p_{0} = 1$.
-   $\operatorname{lpf}(n) := [1 < n] \min\{p : p \mid n\} + [1 = n]$, i.e., the least prime factor of $n$. In particular, for $n=1$ its value is $1$.
-   $F_{\mathrm{prime}}(n) := \sum_{2 \le p \le n} f(p)$
-   $F_{k}(n) := \sum_{i = 2}^{n} [p_{k} \le \operatorname{lpf}(i)] f(i)$

## Explanation

Looking at the definition of $F_{k}(n)$, we see that the answer is exactly $F_{1}(n) + f(1) = F_{1}(n) + 1$.

Consider how to compute $F_{k}(n)$. By enumerating the least prime factor of each $i$ and its exponent we obtain the recurrence:

$$
\begin{aligned}
    F_{k}(n)
    &= \sum_{i = 2}^{n} [p_{k} \le \operatorname{lpf}(i)] f(i) \\
    &= \sum_{\substack{k \le i \\ p_{i}^{2} \le n}} \sum_{\substack{c \ge 1 \\ p_{i}^{c} \le n}} f\left(p_{i}^{c}\right) ([c > 1] + F_{i + 1}\left(n / p_{i}^{c}\right)) + \sum_{\substack{k \le i \\ p_{i} \le n}} f(p_{i}) \\
    &= \sum_{\substack{k \le i \\ p_{i}^{2} \le n}} \sum_{\substack{c \ge 1 \\ p_{i}^{c} \le n}} f\left(p_{i}^{c}\right) ([c > 1] + F_{i + 1}\left(n / p_{i}^{c}\right)) + F_{\mathrm{prime}}(n) - F_{\mathrm{prime}}(p_{k - 1}) \\
    &= \sum_{\substack{k \le i \\ p_{i}^{2} \le n}} \sum_{\substack{c \ge 1 \\ p_{i}^{c + 1} \le n}} \left(f\left(p_{i}^{c}\right) F_{i + 1}\left(n / p_{i}^{c}\right) + f\left(p_{i}^{c + 1}\right)\right) + F_{\mathrm{prime}}(n) - F_{\mathrm{prime}}(p_{k - 1})
\end{aligned}
$$

The last step of the derivation is based on the following fact: for $c$ satisfying $p_{i}^{c} \le n < p_{i}^{c + 1}$ we have $p_{i}^{c + 1} > n \iff n / p_{i}^{c} < p_{i} < p_{i + 1}$, hence $F_{i + 1}\left(n / p_{i}^{c}\right) = 0$.  
The boundary value is $F_{k}(n) = 0 (p_{k} > n)$.

Suppose all $F_{\mathrm{prime}}(n)$ have already been computed; then there are two ways to compute all $F_{k}(n)$:

1.  Compute directly according to the recurrence.
2.  Enumerate $p$ from largest to smallest and perform the transitions; the contribution of a transition is nonzero only when $p^{2} < n$, so it suffices to optimize the recurrence with suffix sums.

Now consider how to compute $F_{\mathrm{prime}}{(n)}$.  
Observing the process of computing $F_{k}(n)$, it is easy to see that the only useful values of $F_{\mathrm{prime}}$ are those at the $O(\sqrt{n})$ points $1, 2, \dots, \left\lfloor\sqrt{n}\right\rfloor, n / \sqrt{n}, \dots, n / 2, n$.  
In general, $f(p)$ is a low-degree polynomial in $p$ and can be written as $f(p) = \sum a_{i} p^{c_{i}}$.  
Then for each $p^{c_{i}}$, its contribution to $F_{\mathrm{prime}}(n)$ is $a_{i} \sum_{2 \le p \le n} p^{c_{i}}$.  
Considering the contribution of each $p^{c_{i}}$ separately, the problem becomes: given $n, s, g(p) = p^{s}$, compute $\sum_{p \le m} g(p)$ for all $m = n / i$.

???+ tip "Note"
    $g(p) = p^{s}$ is a completely multiplicative function!

So let $G_{k}(n) := \sum_{i = 2}^{n} \left[p_{k} < \operatorname{lpf}(i) \lor \operatorname{isprime}(i)\right] g(i)$, i.e., the sum of the $g$ values of the numbers remaining after the $k$-th round of the sieve of Eratosthenes.  
For a composite number $x \le n$ we necessarily have $\operatorname{lpf}(x) \le \sqrt{x} \le \sqrt{n}$. Let $p_{\ell(n)}$ be the largest prime not exceeding $\sqrt{n}$; then $\sum_{2\le p\le n}g(p) = G_{\ell(n)}(n)$, i.e., after $\ell$ rounds of the sieve of Eratosthenes only primes remain.
Consider the boundary value of $G$; obviously $G_{0}(n) = \sum_{i = 2}^{n} g(i)$. (Remember? We specially agreed that $p_{0} = 1$.)  
For the transition, consider the process of the sieve of Eratosthenes and discuss the contribution of each part separately:

1.  For the part where $n < p_{k}^{2}$, the value of $G$ does not change, i.e., $G_{k}(n) = G_{k - 1}(n)$.
2.  For the part where $p_{k}^{2} \le n$, the sieved-out numbers necessarily have the prime factor $p_{k}$, i.e., $-g(p_{k}) G_{k - 1}(n / p_{k})$.
3.  In the second part, since $p_{k}^{2} \le n \iff p_{k} \le n / p_{k}$, the numbers $i$ satisfying $\operatorname{lpf}(i) < p_{k}$ are subtracted in excess. This part should be added back, i.e., $g(p_{k}) G_{k - 1}(p_{k - 1})$.

Hence:

$$
G_{k}(n) = G_{k - 1}(n) - \left[p_{k}^{2} \le n\right] g(p_{k}) (G_{k - 1}(n / p_{k}) - G_{k - 1}(p_{k - 1}))
$$

## Complexity analysis

For the computation of $F_{k}(n)$, the time complexity of the first method has been proven to be $O\left(n^{1 - \epsilon}\right)$ (see Zhu Zhenting's Chinese national training team paper [《一些特殊的数论函数求和问题》](https://github.com/OI-wiki/libs/blob/master/%E9%9B%86%E8%AE%AD%E9%98%9F%E5%8E%86%E5%B9%B4%E8%AE%BA%E6%96%87/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2018%E8%AE%BA%E6%96%87%E9%9B%86.pdf) (Some special summation problems of number-theoretic functions), section 2.3);  
the second method is essentially the second part of Zhou's sieve and is also mentioned in Ren Zhizhou's paper [《积性函数求和的几种方法》](https://github.com/OI-wiki/libs/blob/master/%E9%9B%86%E8%AE%AD%E9%98%9F%E5%8E%86%E5%B9%B4%E8%AE%BA%E6%96%87/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2016%E8%AE%BA%E6%96%87%E9%9B%86.pdf) (Several methods for summing multiplicative functions) (6.5.4); its time complexity has been proven to be $O\left(\frac{n^{\frac{3}{4}}}{\log{n}}\right)$.

As for the computation of $F_{\mathrm{prime}}(n)$, its implementation is in fact the same as the first part of Zhou's sieve.  
Note that for each $m = n / i$, only the transitions made while enumerating the $p_{k}$ satisfying $p_{k}^{2} \le m$ contribute to the time complexity, so the time complexity can be estimated as:

$$
\begin{aligned}
    T(n)
    &= \sum_{i^{2} \le n} O\left(\pi\left(\sqrt{i}\right)\right) + \sum_{i^{2} \le n} O\left(\pi\left(\sqrt{\frac{n}{i}}\right)\right) \\
    &= \sum_{i^{2} \le n} O\left(\frac{\sqrt{i}}{\ln{\sqrt{i}}}\right) + \sum_{i^{2} \le n} O\left(\frac{\sqrt{\frac{n}{i}}}{\ln{\sqrt{\frac{n}{i}}}}\right) \\
    &= O\left(\int_{1}^{\sqrt{n}} \frac{\sqrt{\frac{n}{x}}}{\log{\sqrt{\frac{n}{x}}}} \mathrm{d} x\right) \\
    &= O\left(\frac{n^{\frac{3}{4}}}{\log{n}}\right)
\end{aligned}
$$

As for the space complexity, we can see that both $F_{k}$ and $F_{\mathrm{prime}}$ take useful values only at the points $n / i$, of which there are $O(\sqrt{n})$ in total; by recording only the useful values, the space complexity can be optimized to $O(\sqrt{n})$.

First, with one pass of floor-division blocks we can obtain all useful values and record them in an array $\text{lis}$ of size $O(\sqrt{n})$. For a useful value $v$, let $\text{id}(v)$ denote the index of $v$ in $\text{lis}$; it is easy to see that for all useful values $v$, $\text{id}(v) \le \sqrt{n}$.

Then consider separately the useful values less than or equal to $\sqrt{n}$ and those greater than $\sqrt{n}$: for a useful value $v$ less than or equal to $\sqrt{n}$, record its $\text{id}(v)$ in an array $\text{le}$, i.e., $\text{le}_v = \text{id}(v)$; for a useful value $v$ greater than $\sqrt{n}$, record $\text{id}(v)$ in an array $\text{ge}$, and since $v$ is too large, record $\text{id}(v)$ using $v' = n / v < \sqrt{n}$, i.e., $\text{ge}_{v'} = \text{id}(v)$.

In this way, two arrays of size $O(\sqrt{n})$ suffice to record the $\text{id}$ of all useful values and query them in $O(1)$. When computing $F_{k}$ or $F_{\mathrm{prime}}$, use the $\text{id}$ of a useful value instead of the value itself as the index, and the space complexity is optimized to $O(\sqrt{n})$.

## Procedure

For the computation of $F_{k}(n)$, in implementations we usually choose the first method, which is easier to implement; for smaller input sizes it often performs better than the second method.

For the computation of $F_{\mathrm{prime}}(n)$, it suffices to implement the recurrence directly.

For $p_{k}^{2} \le n$, we can precompute $s_{k} := F_{\mathrm{prime}}(p_{k})$ with a linear sieve to replace $F_{\mathrm{prime}}(p_{k - 1})$ in the recurrence for $F_{k}$.  
Correspondingly, $G_{k - 1}(p_{k - 1}) = \sum_{i = 1}^{k - 1} g(p_{i})$ in the recurrence for $G$ can also be precomputed in the same way.

When using the Extended Eratosthenes Sieve to compute the prefix sums of a **multiplicative function** $f$, the following points should be clarified:

-   how to quickly (usually in linear time complexity) sieve the first $\sqrt{n}$ values of $f$;
-   the polynomial representation of $f(p)$;
-   how to quickly compute $f(p^{c})$.

Once these points are clear, it suffices to implement the following parts in order:

1.  sieve the primes in $[1, \sqrt{n}]$ and the first $\sqrt{n}$ values of $f$;
2.  for each term of the polynomial representation of $f(p)$, sieve the corresponding $G$ and merge them to obtain all $O(\sqrt{n})$ useful values of $F_{\mathrm{prime}}$;
3.  implement the recursion according to the recurrence for $F_{k}$ and compute $F_{1}(n)$.

## Example problems

???+ example "[Luogu P4213【模板】杜教筛 (Template: Du's sieve)](https://www.luogu.com.cn/problem/P4213)"
    Compute $\displaystyle \sum_{i = 1}^{n} \varphi(i)$ and $\displaystyle \sum_{i = 1}^{n} \mu(i)$.

??? note "Solution"
    For the prefix sum of $\varphi(i)$, first it is easy to see that $f(p) = p - 1$. For the linear term $(p)$ of $f(p)$ we have $g(p) = p, G_{0}(n) = \sum_{i = 2}^{n} g(i) = \frac{(n + 2) (n - 1)}{2}$; for the constant term $(-1)$ of $f(p)$ we have $g(p) = -1, G_{0}(n) = \sum_{i = 2}^{n} g(i) = -n + 1$. Sieve twice and add the results to obtain all $O(\sqrt{n})$ required values of $F_{\mathrm{prime}}$.
    
    For the prefix sum of $\mu(i)$, it is easy to see that $f(p) = -1$. Then $g(p) = -1, G_{0}(n) = \sum_{i = 2}^{n} g(i) = -n + 1$. Sieving directly gives all $O(\sqrt{n})$ required values of $F_{\mathrm{prime}}$.

???+ example "[LOJ 6053 简单的函数 (A simple function)](https://loj.ac/p/6053)"
    Given $f(n)$:
    
    $$
    f(n) = \begin{cases}
        1 & n = 1 \\
        p \operatorname{xor} c & n = p^{c} \\
        f(a)f(b) & n = ab \land a \perp b
    \end{cases}
    $$
    
    Compute $\displaystyle \sum_{i = 1}^{n} f(i)$.

??? note "Solution"
    It is easy to see that $f(p) = p - 1 + 2[p = 2]$. So sieve as in the method for sieving $\varphi$, handling $2$ as a special case.

??? note "Reference code"
    ```cpp
    --8<-- "docs/math/code/min-25/min-25_1.cpp"
    ```
