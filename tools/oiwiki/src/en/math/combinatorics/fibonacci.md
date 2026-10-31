---
title: Fibonacci sequence
---

The Fibonacci sequence ([OEIS A000045](http://oeis.org/A000045)) is defined as follows:

$$
F_0 = 0, F_1 = 1, F_n = F_{n-1} + F_{n-2}
$$

The first few terms of the sequence are:

$$
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, \dots
$$

## Lucas sequence

The Lucas sequence ([OEIS A000032](http://oeis.org/A000032)) is defined as follows:

$$
L_0 = 2, L_1 = 1, L_n = L_{n-1} + L_{n-2}
$$

The first few terms of the sequence are:

$$
2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, \dots
$$

When studying the Fibonacci sequence, the Lucas sequence is often needed as a tool.

## Closed form of the Fibonacci sequence

The $n$-th Fibonacci number can be computed from the recurrence in $\Theta (n)$ time. However, there are faster ways to compute it.

### Analytic solution

An analytic solution is a solution given by a formula. We have the closed form of the Fibonacci sequence (Binet's Formula):

$$
F_n = \frac{\left(\frac{1 + \sqrt{5}}{2}\right)^n - \left(\frac{1 - \sqrt{5}}{2}\right)^n}{\sqrt{5}}
$$

This formula is easily proved by induction; of course, it can also be derived using the concept of generating functions, or by solving an equation.

You may have noticed that the second term in the numerator of this formula is always less than $1$, and it decreases exponentially fast. Therefore we can write the formula as

$$
F_n = \left[\frac{\left(\frac{1 + \sqrt{5}}{2}\right)^n}{\sqrt{5}}\right]
$$

where the square brackets denote rounding to the nearest integer.

These two formulas require extremely high precision when computing, so they are rarely used in practice. But do not ignore them! Combined with the concepts of quadratic residues and modular inverses, this formula is still useful in competitive programming (OI).

### Closed form of the Lucas sequence

We have the closed form of the Lucas sequence:

$$
L_n = \left(\frac{1 + \sqrt{5}}{2}\right)^n + \left(\frac{1 - \sqrt{5}}{2}\right)^n
$$

It is very similar to that of the Fibonacci sequence. In fact, we have:

$$
\frac{L_n + F_n\sqrt{5}}{2} = \left(\frac{1 + \sqrt{5}}{2}\right)^n
$$

That is, $L_n$ and $F_n$ are exactly the coefficients in the numerator obtained by expanding $\left(\frac{1 + \sqrt{5}}{2}\right)^n$ with the binomial theorem and collecting like terms. In other words, all solutions of the Pell equation

$$
x^2-5y^2=-4
$$

are exactly

$$
\frac{x_n + y_n\sqrt{5}}{2} = \frac{L_n + F_n\sqrt{5}}{2}
$$

that is, exactly the Lucas and Fibonacci sequences. Hence

$$
{L_n}^2-5{F_n}^2=-4
$$

### Matrix form

The recurrence of the Fibonacci sequence can be expressed as a matrix multiplication:

$$
\begin{bmatrix}F_{n-1} & F_{n} \cr\end{bmatrix} = \begin{bmatrix}F_{n-2} & F_{n-1} \cr\end{bmatrix} \begin{bmatrix}0 & 1 \cr 1 & 1 \cr\end{bmatrix}
$$

Let $P = \begin{bmatrix}0 & 1 \cr 1 & 1 \cr\end{bmatrix}$; we get

$$
\begin{bmatrix}F_n & F_{n+1} \cr\end{bmatrix} = \begin{bmatrix}F_0 & F_1 \cr\end{bmatrix} P^n
$$

Thus we can compute the Fibonacci sequence in $\Theta(\log n)$ time using matrix multiplication. Moreover, the formula from the previous section can also be obtained by the technique of matrix diagonalization.

### Fast doubling method

Using the method above we can obtain the following identities:

$$
\begin{aligned}
F_{2k} &= F_k (2 F_{k+1} - F_{k}) \\
F_{2k+1} &= F_{k+1}^2 + F_{k}^2
\end{aligned}
$$

In this way we can quickly compute two adjacent Fibonacci numbers (with a smaller constant than matrix multiplication). The code is as follows; the return value is the pair $(F_n,F_{n+1})$.

```cpp
pair<int, int> fib(int n) {
  if (n == 0) return {0, 1};
  auto p = fib(n >> 1);
  int c = p.first * (2 * p.second - p.first);
  int d = p.first * p.first + p.second * p.second;
  if (n & 1)
    return {d, c + d};
  else
    return {c, d};
}
```

## Properties

The Fibonacci sequence has many interesting properties; here we list some of the simple ones:

1.  Cassini's identity: $F_{n-1} F_{n+1} - F_n^2 = (-1)^n$.
2.  Addition property: $F_{n+k} = F_k F_{n+1} + F_{k-1} F_n$.
3.  Taking $k = n$ in the previous property, we get $F_{2n} = F_n (F_{n+1} + F_{n-1})$.
4.  From the previous property one can prove by induction that $\forall k\in \mathbb{N},F_n|F_{nk}$.
5.  The converse also holds: $\forall F_a|F_b,a|b$.
6.  GCD property: $(F_m, F_n) = F_{(m, n)}$.
7.  Two adjacent terms of the Fibonacci sequence as input make the Euclidean algorithm reach its worst-case complexity (see [Wikipedia – Lamé](https://en.wikipedia.org/wiki/Gabriel_Lam%C3%A9)).

### Relationship between the Fibonacci and Lucas sequences

It is not hard to notice that the identities relating the Lucas and Fibonacci sequences are highly similar to trigonometric formulas. For example:

$$
\frac{L_n + F_n\sqrt{5}}{2} = \left(\frac{1 + \sqrt{5}}{2}\right)^n
$$

is very similar to

$$
\cos nx + i\sin nx = \left(\cos x + i\sin x\right)^n
$$

Also,

$$
{L_n}^2-5{F_n}^2=-4
$$

is very similar to

$$
\cos^2 x + \sin^2 x = 1
$$

Therefore, the Lucas sequence resembles the cosine function, while the Fibonacci sequence resembles the sine function. For example, from

$$
\left(\frac{1 + \sqrt{5}}{2}\right)^m\left(\frac{1 + \sqrt{5}}{2}\right)^n = \left(\frac{1 + \sqrt{5}}{2}\right)^{m+n}
$$

we get the identities for the sum of two indices:

$$
2L_{m+n}=5F_mF_n+L_mL_n
$$

$$
2F_{m+n}=F_mL_n+L_mF_n
$$

and as a corollary the identities for a doubled index:

$$
L_{2n}={L_n}^2-2{\left(-1\right)}^n
$$

$$
F_{2n}=F_nL_n
$$

This is also a way of quickly doubling the index. Likewise, by analogy with trigonometric formulas such as parity, sum-to-product and product-to-sum formulas, half-angle formulas, the universal substitution, etc., many more corresponding identities for the Lucas and Fibonacci sequences can be derived.

## Fibonacci coding

We can use the Fibonacci sequence to encode positive integers. By [Zeckendorf's theorem](https://en.wikipedia.org/wiki/Zeckendorf%27s_theorem), any natural number $n$ can be uniquely represented as a sum of Fibonacci numbers:

$$
N = F_{k_1} + F_{k_2} + \ldots + F_{k_r}
$$

such that $k_1 \ge k_2 + 2,\ k_2 \ge k_3 + 2,\  \ldots,\  k_r \ge 2$ (i.e., two adjacent Fibonacci numbers cannot be used).

Thus we can represent a positive integer with the code $d_0 d_1 d_2 \dots d_s 1$, where $d_i=1$ means that $F_{i+2}$ is used. We forcibly append a 1 at the end of the code (this creates two adjacent 1s), which marks the end of the code. A few examples:

$$
\begin{aligned}
1 &=& 1 &=& F_2 &=& (11)_F \\
2 &=& 2 &=& F_3 &=& (011)_F \\
6 &=& 5 + 1 &=& F_5 + F_2 &=& (10011)_F \\
8 &=& 8 &=& F_6 &=& (000011)_F \\
9 &=& 8 + 1 &=& F_6 + F_2 &=& (100011)_F \\
19 &=& 13 + 5 + 1 &=& F_7 + F_5 + F_2 &=& (1001011)_F
\end{aligned}
$$

Encoding $n$ can be done with a greedy algorithm:

1.  Iterate over the Fibonacci numbers $F_i$ from large to small until $F_i\le n$.
2.  Subtract $F_i$ from $n$ and put a 1 at position $i-2$ of the code (positions in the code are counted from left to right starting at 0).
3.  If $n$ is positive, go back to step 1.
4.  Finally, append a 1 at the end of the code to mark where the code ends.

Decoding works similarly: first remove the trailing 1, then for every position $i$ whose code digit is 1 (positions counted from left to right starting at 0), add $F_{i+2}$ to the answer. The final answer is the original number.

## Periodicity modulo m

For the Fibonacci sequence modulo $m$, it is easy to prove by the pigeonhole principle that the sequence is periodic. Since the computation of each Fibonacci number depends on the values of the previous two terms, the current state of the sequence must be described by a pair of adjacent Fibonacci numbers. Consider the first $m^2+1$ pairs of Fibonacci numbers in the modular sense:

$$
(F_0,\ F_1),\ (F_1,\ F_2),\ \ldots,\ (F_{m^2},\ F_{m^2 + 1})
$$

The residue system modulo $m$ has size $m$, which means there can be at most $m^2$ distinct pairs. Therefore, among the first $m^2+1$ pairs there must be two identical pairs, and from these two pairs the same Fibonacci sequence is generated onward. Hence, the Fibonacci sequence is periodic, and its (least positive) period does not exceed $m^2$.

### Pisano period

The least positive period of the Fibonacci sequence modulo $m$ is called the **Pisano period** ([OEIS A001175](http://oeis.org/A001175)). In this article, $\pi(m)$ denotes the Pisano period modulo $m$.

This observation can be used to compute the $n$-th Fibonacci number modulo $m$. If $n$ is very large, one needs to compute the period of the Fibonacci sequence modulo $m$. Of course, it suffices to compute some period, not necessarily the least positive one.

For this purpose, we have the following results:

1.  For coprime moduli $m_1,m_2$, we have $\pi(m_1m_2)=\operatorname{lcm}(\pi(m_1),\pi(m_2))$.
2.  For a prime $p$ and a positive integer $e$, we have $\pi(p^{e})\mid p^{e-1}\pi(p)$.
3.  For $m=2^e~(e\in\mathbf N_+)$, we have $\pi(m)=3\cdot 2^{e-1}$.
4.  For $m=5^e~(e\in\mathbf N_+)$, we have $\pi(m)=4\cdot 5^e$.
5.  Finally, for a prime $p\equiv\pm1\pmod{10}$, we have $\pi(p)\mid(p-1)$; for a prime $p\equiv\pm3\pmod{10}$, we have $\pi(p)\mid 2(p+1)$.

Combining these cases, one can show that the Pisano period modulo $m$ does not exceed $6m$, with equality if and only if $m = 2\times 5^e~(e\in\mathbf N_+)$.

Using the above results, based on a prime factorization algorithm, we obtain the following method for quickly computing the Pisano period:

??? example "Reference code"
    ```cpp
    --8<-- "docs/math/code/combinatorics/fibonacci/pisano_estimate.cpp:pisano"
    ```

The period obtained this way may only be a multiple of the Pisano period. To obtain the exact Pisano period, one can further examine the divisors of this period; alternatively, it can be computed directly with the [BSGS algorithm](../number-theory/discrete-logarithm.md#baby-step-giant-step-algorithm) in $O(\sqrt{m})$ time.

### Proof

Finally, this article briefly proves the above results on the Pisano period. It is worth noting that, using the method explained below, similar results can be generalized to arbitrary second-order homogeneous linear recurrences with constant coefficients. Although the specific constants differ, the Pisano periods of these sequences modulo $m$ are all $O(m)$.

The first observation is that, using the [Chinese remainder theorem](../number-theory/crt.md), the discussion can be restricted to the case of prime power moduli. Let $m_1,m_2$ be two coprime moduli. The periods of the Fibonacci sequence modulo $m_1$ are $\pi(m_1)$ and its multiples, and modulo $m_2$ they are $\pi(m_2)$ and its multiples, so its least positive period modulo $m_1m_2$ is exactly the least common multiple of $\pi(m_1)$ and $\pi(m_2)$. This is result 1 above.

The other observation is that the Pisano period modulo $m$ is in fact the least positive integer $k$ such that

$$
A^k = \begin{pmatrix} 1&1\\1&0 \end{pmatrix}^k \equiv I \pmod{m}.
$$

That is, it is actually the [order](../algebra/group-theory.md#阶) of the matrix $A$ modulo $m$[^mod-m].

For the case of a prime power modulus $m=p^e$, the classical lifting-the-exponent argument relates it to the case of the corresponding prime modulus. Let $k=\pi(p^e)$; then there exists a square matrix $\Lambda$ of order 2 such that

$$
A^k = p^e\Lambda + I 
$$

holds. Hence, by the [binomial theorem](./combination.md#二项式定理), we have

$$
A^{kp} = (p^e\Lambda + I)^p = I + \sum_{i=1}^p\binom{p}{i}(p^e\Lambda)^i \equiv I\pmod{p^{e+1}}. 
$$

Therefore, by the [properties of the order](../number-theory/primitive-root.md#cyclic-structure-of-powers), we have $\pi(p^{e+1})\mid kp = p\pi(p^e)$. By induction on $e$, $\pi(p^e)\mid p^{e-1}\pi(p)$ always holds.

For the case of a prime modulus $p$, this article discusses two methods of proof.

=== "Using the closed form"
    One method uses the closed form of the Fibonacci sequence:
    
    $$
    F_n = \dfrac{1}{\sqrt{5}}\left(\dfrac{1+\sqrt{5}}{2}\right)^n - \dfrac{1}{\sqrt{5}}\left(\dfrac{1-\sqrt{5}}{2}\right)^n.
    $$
    
    Expand it with the binomial theorem and cancel the radical terms:
    
    $$
    F_n = \dfrac{1}{2^{n-1}}\sum_{i=0}^{\lfloor(n-1)/2\rfloor}\binom{n}{2i+1}5^i.
    $$
    
    For $p=2$, this expression cannot be reduced modulo the prime directly, but one can verify that the corresponding Pisano period is $\pi(2)=3$. For $p=5$, we have $F_n\equiv n\cdot 3^{n-1}\pmod{p}$, and one can directly verify that the corresponding Pisano period is $\pi(5)=20$. The remaining odd prime moduli split into two cases:
    
    -   If $p\equiv 1,4\pmod{5}$, then
    
        $$
        \begin{aligned}
        F_{p} &\equiv \dfrac{1}{2^{p-1}}\binom{p}{p}5^{(p-1)/2} \equiv 1 \pmod{p},\\
        F_{p+1} &\equiv \dfrac{1}{2^p}\left(\binom{p+1}{1} + \binom{p+1}{p}5^{(p-1)/2}\right) \equiv 1 \pmod{p}.
        \end{aligned}
        $$
    
        In the simplification, the following results were used: by [Lucas's theorem](../number-theory/lucas.md), $\dbinom{p}{k}\equiv 0\pmod{p}$ for all $0 < k < p$, and $\dbinom{p+1}{k}\equiv 0\pmod{p}$ for all $1 < k < p$; by [Fermat's little theorem](../number-theory/fermat.md#fermats-little-theorem), $2^{p-1}\equiv 5^{p-1}\equiv 1\pmod{p}$; for $p\equiv 1,4\pmod{5}$, $p$ is a quadratic residue modulo $5$, so by the [law of quadratic reciprocity](../number-theory/quad-residue.md#law-of-quadratic-reciprocity), $5$ is also a quadratic residue modulo $p$, hence $5^{(p-1)/2} \equiv 1\pmod{p}$. Consequently, $(F_p,F_{p+1}) \equiv (F_1,F_2) \pmod{p}$, so $(p-1)$ is a period modulo $p$. Therefore, $\pi(p)\mid(p-1)$.
    -   If $p\equiv 2,3\pmod{5}$, then
    
        $$
        \begin{aligned}
        F_{2p} &\equiv \dfrac{1}{2^{2p-1}}\binom{2p}{p}5^{(p-1)/2} \equiv -1 \pmod{p},\\
        F_{2p+1} &\equiv \dfrac{1}{2^{2p}}\left(\binom{2p+1}{1} + \binom{2p+1}{p}5^{(p-1)/2} + \binom{2p+1}{2p+1}5^p\right) \equiv -1\pmod{p}.
        \end{aligned}
        $$
    
        In the simplification, the following results were used: by Lucas's theorem, $\dbinom{p}{k}\equiv 0\pmod{p}$ for all $0 < k < p$ and $p < k < 2p$, and $\dbinom{2p}{p}\equiv 2\pmod{p}$, while $\dbinom{p}{k}\equiv 0\pmod{p}$ for all $1 < k < p$ and $p + 1 < k < 2p$, and $\dbinom{2p+1}{p}\equiv 2\pmod{p}$; by Fermat's little theorem, $2^{p-1}\equiv 5^{p-1}\equiv 1\pmod{p}$; for $p\equiv 2,3\pmod{5}$, $p$ is a quadratic non-residue modulo $5$, so by the law of quadratic reciprocity, $5$ is also a quadratic non-residue modulo $p$, hence $5^{(p-1)/2} \equiv -1\pmod{p}$. Consequently, $(F_{2p},F_{2p+1}) \equiv (F_{-2},F_{-1}) \pmod{p}$, so $2(p+1)$ is a period modulo $p$. Therefore, $\pi(p)\mid 2(p+1)$.
    
    This completes the proof. The limitation of this method is that it relies heavily on the closed form of the Fibonacci sequence, so it is hard to generalize directly to the general case.

=== "Using a field extension"
    The other method of proof tries to compute the order of the matrix $A=\begin{pmatrix}1&1\\1&0\end{pmatrix}$ directly. Its [characteristic polynomial](../linear-algebra/char-poly.md) is $f(x) = x^2-x-1$, with discriminant $\Delta = 5$. For the modulus $p=5$, we have $\Delta\equiv 0\pmod{5}$; the matrix $A$ has two equal eigenvalues $\lambda=3$ and is not diagonalizable, so this case must be computed separately. For a modulus $p\equiv 1,4\pmod{5}$, by the law of quadratic reciprocity the discriminant $\Delta=5$ is a quadratic residue modulo $p$; the matrix $A$ has two distinct eigenvalues $\lambda_1\neq\lambda_2$ in the field $\mathbf F_p$, and the order of $A$ is $\operatorname{lcm}(\operatorname{ord}(\lambda_1),\operatorname{ord}(\lambda_2))$, which necessarily divides $|\mathbf F_p^\times|=p-1$. For a modulus $p\equiv 2,3\pmod{5}$, by the law of quadratic reciprocity the discriminant $\Delta=5$ is a quadratic non-residue modulo $p$; the matrix $A$ has no eigenvalues in the field $\mathbf F_p$ and only has two distinct eigenvalues $\lambda_1\neq\lambda_2$ in the [field extension](../algebra/field-theory.md#域的扩张) $\mathbf F_p[\sqrt{5}]$. Since the Frobenius endomorphism $x\mapsto x^p$ swaps the two roots, we have $\lambda_2=\lambda_1^p$, hence $\lambda_1^{p+1}=\lambda_2^{p+1}=\lambda_1\lambda_2=-1$, i.e., $\lambda_1^{2(p+1)}=\lambda_2^{2(p+1)}=1$. Thus the order of $A$ is $\operatorname{lcm}(\operatorname{ord}(\lambda_1),\operatorname{ord}(\lambda_2))$, which necessarily divides $2(p+1)$. This yields the same conclusion as the previous method.

In summary, for the different cases we correspondingly have:

-   $\pi(2^e)=\dfrac{3}{2}\cdot 2^e,~\dfrac{1}{4}\pi(5^e)=5^e$.
-   When $p\equiv\pm1\pmod{10}$, $\pi(p^e) \mid (p-1)p^{e-1}$, so $\pi(p^e)\le p^e$.
-   When $p\equiv\pm3\pmod{10}$, $\dfrac{1}{4}\pi(p^e) \mid \dfrac{p+1}{2}p^{e-1}$, so $\dfrac{1}{4}\pi(p^e)\le p^e$.

Therefore, using result 1, for a general modulus $m=\prod_i p_i^{e_i}$ we have

$$
\begin{aligned}
\pi(m)&=\operatorname{lcm}\{\pi(p_i^{e_i}):p_i\in\mathbf P\} \\
&\le \operatorname{lcm}\{\pi(p_i^{e_i}):p_i=2\text{ or }p_i\equiv\pm1~(\operatorname{mod}{10})\}\\
&\quad \cdot 4\cdot\operatorname{lcm}\{\pi(p_i^{e_i})/4:p_i=5\text{ or }p_i\equiv\pm3~(\operatorname{mod}{10})\}\\
&\le \prod\{\pi(p_i^{e_i}):p_i=2\text{ or }p_i\equiv\pm1~(\operatorname{mod}{10})\}\\
&\quad \cdot 4\cdot\prod\{\pi(p_i^{e_i})/4:p_i=5\text{ or }p_i\equiv\pm3~(\operatorname{mod}{10})\}\\
&\le \dfrac{3}{2}\cdot\prod\{p_i^{e_i}:p_i=2\text{ or }p_i\equiv\pm1~(\operatorname{mod}{10})\}\\
&\quad \cdot 4\cdot\prod\{p_i^{e_i}:p_i=5\text{ or }p_i\equiv\pm3~(\operatorname{mod}{10})\}\\
&= 6m.
\end{aligned}
$$

This shows that the Pisano period of the Fibonacci sequence modulo $m$ never exceeds $6m$, and equality is attained if and only if $m=2\cdot 5^e$.

## Exercises

-   [SPOJ - Euclid Algorithm Revisited](http://www.spoj.com/problems/MAIN74/)
-   [SPOJ - Fibonacci Sum](http://www.spoj.com/problems/FIBOSUM/)
-   [HackerRank - Is Fibo](https://www.hackerrank.com/challenges/is-fibo/problem)
-   [Project Euler - Even Fibonacci numbers](https://www.hackerrank.com/contests/projecteuler/challenges/euler002/problem)
-   [Luogu P4000 斐波那契数列 (Fibonacci Sequence)](https://www.luogu.com.cn/problem/P4000)

## References and notes

-   [Fibonacci sequence - Wikipedia](https://en.wikipedia.org/wiki/Fibonacci_sequence)
-   [Zeckendorf's theorem - Wikipedia](https://en.wikipedia.org/wiki/Zeckendorf%27s_theorem)
-   [Pisano period - Wikipedia](https://en.wikipedia.org/wiki/Pisano_period)

**This page is mainly translated from the blog post [Числа Фибоначчи](http://e-maxx.ru/algo/fibonacci_numbers) and its English translation [Fibonacci Numbers](https://cp-algorithms.com/algebra/fibonacci-numbers.html). The Russian version is licensed under Public Domain + Leave a Link; the English version is licensed under CC-BY-SA 4.0. The content has been modified.**

[^mod-m]: Strictly speaking, it is the order of the matrix $A$ in the general linear group $GL_2(\mathbf Z_m)$.
