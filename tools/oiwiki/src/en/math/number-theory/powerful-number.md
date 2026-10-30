---
title: Powerful Number sieve
---

## Definition

The Powerful Number sieve (abbreviated PN sieve below) is similar to Du's sieve, or rather it is an extension of Du's sieve, and can be used to compute the prefix sums of some multiplicative functions.

**Requirements**:

-   There exists a function $g$ satisfying:
    -   $g$ is a multiplicative function.
    -   The prefix sums of $g$ are easy to compute.
    -   For a prime $p$, $g(p) = f(p)$.

Suppose we want to compute the prefix sum of a multiplicative function $f$, $F(n) = \sum_{i=1}^{n} f(i)$.

## Powerful Number

**Definition**: For a positive integer $n$, write the prime factorization of $n$ as $n = \prod_{i=1}^{m} p_{i}^{e_{i}}$. $n$ is a PN if and only if $\forall 1 \le i \le m, e_{i} > 1$.

**Property 1**: Every PN can be written in the form $a^{2}b^{3}$.

**Proof**: If $e_i$ is even, merge $p_{i}^{e_{i}}$ into $a^{2}$; if $e_i$ is odd, first merge $p_{i}^{3}$ into $b^{3}$, then merge $p_{i}^{e_{i}-3}$ into $a^{2}$.

**Property 2**: There are at most $O(\sqrt{n})$ PNs not exceeding $n$.

**Proof**: Enumerate $a$ and then consider the number of valid $b$; the number of PNs is approximately

$$
\int_{1}^{\sqrt{n}} \sqrt[3]{\frac{n}{x^2}} \mathrm{d}x = O(\sqrt{n})
$$

So how do we find all PNs not exceeding $n$? Find all primes up to $\sqrt{n}$ with a linear sieve, then search the exponents of the individual primes with a DFS. Since there are at most $O(\sqrt{n})$ PNs up to $n$, the search takes at most $O(\sqrt{n})$ steps.

## PN sieve

First, construct a multiplicative function $g$ whose prefix sums are easy to compute and which satisfies $g(p) = f(p)$ for primes $p$. Let $G(n) = \sum_{i=1}^{n} g(i)$.

Then construct the function $h = f / g$, where $/$ denotes division in the sense of Dirichlet convolution. By the properties of Dirichlet convolution, $h$ is also a multiplicative function, hence $h(1) = 1$. We have $f = g * h$, where $*$ denotes Dirichlet convolution.

For a prime $p$, $f(p) = g(1)h(p) + g(p)h(1) = h(p) + g(p) \implies h(p) = 0$. From $h(p)=0$ and the multiplicativity of $h$ it follows that $h(n) = 0$ for any $n$ that is not a PN, i.e., $h$ takes nontrivial values only at PNs.

Now, from $f = g * h$ we have

$$
\begin{aligned}
F(n) &= \sum_{i = 1}^{n} f(i)\\
     &= \sum_{i = 1}^{n} \sum_{d|i} h(d) g\left(\frac{i}{d}\right)\\
     &= \sum_{d=1}^{n} \sum_{i=1}^{\lfloor \frac{n}{d}\rfloor} h(d) g(i)\\
     &= \sum_{d=1}^{n} h(d) \sum_{i=1}^{\lfloor \frac{n}{d}\rfloor}  g(i) \\
     &= \sum_{d=1}^{n} h(d) G\left(\left\lfloor \frac{n}{d}\right\rfloor\right)\\
     &= \sum_{\substack{d=1 \\ d \text{ is PN}}}^{n}h(d) G\left(\left\lfloor \frac{n}{d}\right\rfloor\right)
\end{aligned}
$$

Find all PNs in $O(\sqrt{n})$ and compute all nontrivial values of $h$. To compute the nontrivial values of $h$, it suffices to compute all values $h(p^c)$; all nontrivial values of $h$ then follow from the multiplicativity of $h$. Now, for each nontrivial value $d$, compute $h(d)G\left(\left\lfloor \dfrac{n}{d} \right\rfloor\right)$ and sum them up to obtain $F(n)$.

Now consider computing $h(p^c)$; there are two methods: the first is to directly derive a formula for $h(p^c)$ that depends only on $p, c$ and then compute $h(p^c)$ by the formula; the second is to use $f = g * h$ to get $f(p^c) = \sum_{i=0}^c g(p^i)h(p^{c-i})$, and rearranging gives $h(p^c) = f(p^c) - \sum_{i=1}^{c}g(p^i)h(p^{c-i})$, so now we can enumerate primes $p$ and then exponents $c$ to compute all $h(p^c)$.

### Procedure

1.  Construct $g$
2.  Construct a fast way to compute $G$
3.  Compute $h(p^c)$
4.  Search the PNs, accumulating the answer along the way
5.  Obtain the result

For step 3, we can compute directly by the formula, precompute a table by enumeration, or compute on the fly when the search reaches the number.

### Properties

We analyze using the second method of computing $h(p^c)$ as an example. The analysis can be split into two parts: computing $h(p^c)$ and the search.

For the first part: since the number of primes up to $O(\sqrt{n})$ is $O\left(\dfrac{\sqrt{n}}{\log n}\right)$, the exponent $c$ of each prime $p$ is at most $\log n$, and computing $h(p^c)$ requires $(c - 1)$ loop iterations, the time complexity of the first part is $O\left(\dfrac{\sqrt{n}}{\log n} \cdot \log n \cdot \log n\right) = O(\sqrt{n}\log{n})$, and this is a loose upper bound. Depending on the problem, various optimizations can be added to reduce the time complexity of the first part.

For the search part: since there are at most $O(\sqrt{n})$ PNs up to $n$, the search takes at most $O(\sqrt{n})$ steps. For each PN, the time complexity depends on the method used to compute $G$. For example, if the time complexity of computing $G\left(\left\lfloor \dfrac{n}{d}\right\rfloor\right)$ is $O(1)$, the complexity of the second part is $O(\sqrt{n})$.

In particular, if $G\left(\left\lfloor \dfrac{n}{d}\right\rfloor\right)$ is computed with Du's sieve, the time complexity of the second part is that of Du's sieve, i.e., $O(n^{\frac{2}{3}})$. This is because if $G(n)$ is computed once in advance, with the linear-sieve optimization and with the larger values recorded in a data structure supporting fast random access (such as `std::map` and `std::unordered_map` in C++), then every $G\left(\left\lfloor \dfrac{n}{d}\right\rfloor\right)$ used during Du's sieve is either recorded by the linear sieve or recorded in the `std::map`, which can be verified directly with a program.

As for the space complexity, the bottleneck is storing $h(p^c)$. If we use a two-dimensional array $a$ where $a_{i,j}$ denotes the value of $h(p_i^j)$, the space complexity is $O\left(\dfrac{\sqrt{n}}{\log n} \cdot \log n\right) = O(\sqrt{n})$.

## Example problems

### [Luogu P5325【模板】Min\_25 筛 (Template: Min_25 sieve)](https://www.luogu.com.cn/problem/P5325)

**Problem**: Given the multiplicative function $f(p^k) = p^k(p^k-1)$, compute $\sum_{i=1}^{n} f(i)$.

It is easy to see that $f(p) = p(p-1) = \operatorname{id}(p)\varphi(p)$, so we construct $g(n) = \operatorname{id}(n)\varphi(n)$.

We use Du's sieve to compute $G(n)$; from $(\operatorname{id}\cdot \varphi) * \operatorname{id} = \operatorname{id}_2$ we get $G(n)= \sum_{i=1}^{n} i^2 - \sum_{d=2}^{n} d \cdot G\left(\left\lfloor \dfrac{n}{d} \right\rfloor\right)$.

After that, the values $h(p^k)$ can be computed by enumeration; we do not repeat this method here.

Moreover, in this problem we can also directly derive a formula for $h(p^k)$ depending only on $p, k$, as follows:

$$
\begin{aligned}
& f(p^k) = \sum_{i=0}^{k} g(p^{k-i})h(p^i)\\
\iff & p^k(p^k-1) = \sum_{i=0}^{k} p^{k-i}\varphi(p^{k-i}) h(p^i)\\
\iff & p^k(p^k-1) = \sum_{i=0}^{k} p^{2k-2i-1}(p - 1) h(p^i)\\
\iff & p^k(p^k-1) = h(p^k) + \sum_{i=0}^{k-1} p^{2k-2i-1}(p - 1) h(p^i)\\
\iff & h(p^k) = p^k(p^k-1) - \sum_{i=0}^{k-1} p^{2k-2i-1}(p - 1) h(p^i)\\
\iff & h(p^k) - p^2h(p^{k-1}) = p^{k}(p^k-1)-p^{k+1}(p^{k-1}-1) - p(p-1)h(p^{k-1})\\
\iff & h(p^k) - ph(p^{k-1}) = p^{k+1} - p^k\\
\iff & \frac{h(p^k)}{p^k} - \frac{h(p^{k-1})}{p^{k-1}} = p - 1\\
\end{aligned}
$$

Then, using $h(p) = 0$, telescoping summation gives $h(p^k) = (k-1)(p-1)p^k$.

??? note "Reference code"
    ```cpp
    --8<-- "docs/math/code/powerful-number/powerful-number_1.cpp"
    ```

### [“LOJ #6053” 简单的函数 (A simple function)](https://loj.ac/problem/6053)

Given $f(n)$:

$$
f(n) =
\begin{cases}
1 & n = 1 \\
p \oplus c & n=p^c \\
f(a)f(b) & n=ab \text{ and } a \perp b
\end{cases}
$$

It is easy to see that:

$$
f(p) =
\begin{cases}
p + 1 & p = 2 \\
p - 1 & \text{otherwise} \\
\end{cases}
$$

Construct $g$ as

$$
g(n) =
\begin{cases}
3 \varphi(n) & 2 \mid n \\
\varphi(n) & \text{otherwise} \\
\end{cases}
$$

It is easy to prove that $g(p) = f(p)$ and that $g$ is a multiplicative function.

Now consider computing $G(n)$.

$$
\begin{aligned}
G(n)
&= \sum_{i=1}^{n}[i \bmod 2 = 1] \varphi(i) + 3 \sum_{i=1}^{n}[i \bmod 2 = 0] \varphi(i)\\
&= \sum_{i=1}^{n} \varphi(i) + 2\sum_{i=1}^{n} [i \bmod 2 = 0]\varphi(i) \\
&= \sum_{i=1}^{n} \varphi(i) + 2\sum_{i=1}^{\lfloor \frac{n}{2} \rfloor} \varphi(2i)
\end{aligned}
$$

Let $S_1(n) = \sum_{i=1}^{n} \varphi(i)$, $S_2(n) = \sum_{i=1}^{n} \varphi(2i)$; then $G(n) = S_1(n) + 2S_2\left(\left\lfloor \dfrac{n}{2} \right\rfloor\right)$.

When $2 \mid n$, we have

$$
\begin{aligned}
S_2(n)
&= \sum_{i=1}^{n} \varphi(2i) \\
&= \sum_{i=1}^{\frac{n}{2}} (\varphi(2(2i-1)) + \varphi(2(2i))) \\
&= \sum_{i=1}^{\frac{n}{2}} (\varphi(2i-1) + 2\varphi(2i)) \\
&= \sum_{i=1}^{\frac{n}{2}} (\varphi(2i-1) + \varphi(2i)) + \sum_{i=1}^{\frac{n}{2}} \varphi(2i) \\
&= \sum_{i=1}^{n} \varphi(i) + S_2\left(\frac{n}{2}\right)\\
&= S_1(n) + S_2\left(\left\lfloor \frac{n}{2} \right\rfloor\right)\\
\end{aligned}
$$

When $2 \nmid n$, we have

$$
\begin{aligned}
S_2(n)
&= S_2(n-1) + \varphi(2n) \\
&= S_2(n-1) + \varphi(n) \\
&= \sum_{i=1}^{n-1} \varphi(i) + S_2\left(\frac{n-1}{2}\right) + \varphi(n)\\
&= S_1(n) + S_2\left(\left\lfloor \frac{n}{2} \right\rfloor\right)\\
\end{aligned}
$$

In summary, $S_2(n) = S_1(n) + S_2\left(\left\lfloor \dfrac{n}{2} \right\rfloor\right)$.

$S_1$ can be computed with Du's sieve, and $S_2$ directly by the formula, so $G$ can be computed as well.

??? note "Reference code"
    ```cpp
    --8<-- "docs/math/code/powerful-number/powerful-number_2.cpp"
    ```

## Exercises

-   [PE708 Twos are all you need](https://projecteuler.net/problem=708)
-   [PE639 Summing a multiplicative function](https://projecteuler.net/problem=639)
-   [PE484 Arithmetic Derivative](https://projecteuler.net/problem=484)

## References

-   [破壁人五号 - Powerful number 筛略解 (A brief explanation of the Powerful Number sieve)](https://www.cnblogs.com/wallbreaker5th/p/13901487.html)
-   [command\_block - 杜教筛（+ 贝尔级数 + powerful number） (Du's sieve (+ Bell series + powerful number))](https://www.luogu.com.cn/blog/command-block/du-jiao-shai)
