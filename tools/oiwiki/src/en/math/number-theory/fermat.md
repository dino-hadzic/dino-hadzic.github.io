---
title: Fermat's little theorem & Euler's theorem
---

This article discusses Fermat's little theorem, Euler's theorem and its extension. These theorems solve the problem of computing powers with arbitrarily large exponents modulo an arbitrary modulus.

## Fermat's little theorem

**Fermat's little theorem** is one of the most basic theorems in number theory. It is also the theoretical basis of the [Fermat primality test](./prime.md#fermat-素性测试).

???+ note "Fermat's little theorem"
    Let $p$ be a prime. For every integer $a$ with $p\nmid a$, we have $a^{p-1}\equiv 1\pmod p$.

???+ note "Theorem"
    Let $p$ be a prime. For every integer $a$, we have $a^{p}\equiv a\pmod p$.

These two congruences are equivalent when $p\nmid a$; and when $p\mid a$, the congruence $a^p\equiv 0\equiv a\pmod p$ holds trivially. Therefore, the two statements are equivalent. Both statements are often called Fermat's little theorem.

??? note "Proof 1"
    Let $p$ be a prime and $p\nmid a$. First we prove: for $i=1,2,\cdots,p-1$, the remainders $ia \bmod p$ are pairwise distinct. We argue by contradiction. If there were $1\le i < j < p$ such that
    
    $$
    ia \bmod p = ja \bmod p \iff (j-i)a\equiv 0.\pmod p
    $$
    
    But neither $(j-i)$ nor $a$ is a multiple of $p$, which is an obvious contradiction.
    
    In other words, these remainders form a permutation of $\{1,2,\cdots,p-1\}$. Hence
    
    $$
    \prod_{i=1}^{p-1}i = \prod_{i=1}^{p-1}(ia\bmod p) \equiv \prod_{i=1}^{p-1}ia = a^{p-1}\prod_{i=1}^{p-1}i.\pmod p
    $$
    
    This shows that
    
    $$
    (a^{p-1}-1)\prod_{i=1}^{p-1}i \equiv 0. \pmod{p}
    $$
    
    That is, the left-hand side is a multiple of $p$, but none of $i=1,2,\cdots, p-1$ is a multiple of $p$, so we must have $p\mid (a^{p-1}-1)$, which is exactly Fermat's little theorem.

??? note "Proof 2"
    Note that the second formulation of Fermat's little theorem holds for all $a\in\mathbf N$, so we may consider mathematical induction. The case of negative integers is easily reduced to the case of non-negative integers.
    
    The base case is $0^p\equiv 0\pmod p$, which obviously holds. Suppose it holds for $a\in\mathbf N$; we need to show that it also holds for $a+1$. By the binomial theorem,
    
    $$
    (a+1)^p=a^p+\binom{p}{1}a^{p-1}+\binom{p}{2}a^{p-2}+\cdots +\binom{p}{p-1}a+1.
    $$
    
    Except for the first and last terms, in the expression of the binomial coefficient $\dbinom{p}{k} = \dfrac{p!}{k!(p-k)!}$, $p$ divides the numerator but not the denominator, so these coefficients are multiples of $p$ for $k\neq 0,p$. Therefore,
    
    $$
    (a+1)^p \equiv a^p + 1\equiv a + 1. \pmod{p}
    $$
    
    Here the second step uses the induction hypothesis. Thus, by mathematical induction, Fermat's little theorem holds.

The converse of Fermat's little theorem does not hold. Even if $a^{n-1}\equiv 1\pmod n$ for all $a$ coprime to $n$, $n$ need not be prime. See the section [Fermat primality test](./prime.md#fermat-素性测试) for the related discussion.

## Euler's theorem

**Euler's theorem** generalizes Fermat's little theorem to the case of a general modulus, but it still requires the base and the modulus to be coprime.

???+ note "Euler's theorem"
    For an integer $m>0$ and an integer $a$ with $\gcd(a,m)=1$, we have $a^{\varphi(m)}\equiv 1\pmod{m}$, where $\varphi(\cdot)$ is [Euler's totient function](./euler-totient.md).

??? note "Proof"
    Similarly to Proof 1 of Fermat's little theorem, we again take a sequence of numbers coprime to $m$ and then operate on it. Consider the set
    
    $$
    R = \{r\in\mathbf N : 0 < r < m,~\gcd(r,m)=1\}.
    $$
    
    This is the [reduced residue system](./basic.md#同余类与剩余系) modulo $m$. By the definition of Euler's totient function, $|R|=\varphi(m)$. As above, multiplying them by $a$ amounts to permuting this set:
    
    $$
    R = \{ar\bmod m: r\in R\}.
    $$
    
    This is because it is easy to verify that $\gcd(ar,m)=1$ and that distinct $r_1,r_2\in R$ give distinct $ar_1\bmod m$ and $ar_2\bmod m$. Therefore,
    
    $$
    \prod_{r\in R}r \equiv \prod_{r\in R}ar = a^{\varphi(m)}\prod_{r\in R}r. \pmod{m}
    $$
    
    Repeating the previous argument and canceling $\prod_{r\in R}r$, we obtain $a^{\varphi(m)}\equiv 1\pmod m$.

For a prime $p$, we have $\varphi(p)=p-1$, so Fermat's little theorem is a special case of Euler's theorem. Moreover, the exponent $\varphi(m)$ in Euler's theorem is in general not the smallest exponent for which the congruence holds. It can be improved to $\lambda(m)$, where $\lambda(\cdot)$ is the [Carmichael function](./primitive-root.md#carmichael-函数). For the algebraic background of the related results, see the section [Multiplicative group of integers modulo n](../algebra/ring-theory.md#应用整数同余类的乘法群).

## Extended Euler's theorem

The extended Euler's theorem[^ex-euler] further generalizes the result to the case where the base and the modulus are not coprime. Thereby it completely solves the problem of computing powers of an arbitrary base modulo an arbitrary modulus: it reduces them to the case of an exponent smaller than $2\varphi(m)$, so that they can be computed by [binary exponentiation](../binary-exponentiation.md) in $O(\log\varphi(m))$ time.

???+ note "Extended Euler's theorem"
    For every positive integer $m$, integer $a$ and non-negative integer $k$, we have
    
    $$
    a^k \equiv \begin{cases}
    a^{k \bmod \varphi(m)},                &\gcd(a,m) =  1,                   \\
    a^k,                                   &\gcd(a,m)\ne 1, k <   \varphi(m), \\
    a^{(k \bmod \varphi(m)) + \varphi(m)}, &\gcd(a,m)\ne 1, k \ge \varphi(m).
    \end{cases} \pmod m
    $$

The second case says that if $k < \varphi(m)$, there is no need to reduce the exponent further; binary exponentiation can be applied directly. The main difference between the third and the first case is whether, after reducing the exponent by taking the remainder, an extra term $\varphi(m)$ has to be added. Of course, merging the first case into the second and third cases is also correct.

### Intuitive understanding

Before proving the theorem rigorously, we can first understand its meaning intuitively.

![fermat1](./images/fermat.svg)

Consider how the remainder $a^k\bmod m$ changes as $k$ grows. Since the remainder always lies in the interval $[0,m)$ while there are infinitely many $k$, regard $a^k\bmod m \mapsto a^{k+1}\bmod m$ as directed edges between these remainder nodes. Then a cycle like the one in the figure must be formed.

The extended Euler's theorem says that these cycles may be pure cycles (the first case) or mixed cycles (the second and third cases). In a pure cycle no node has two predecessors, while in a mixed cycle such a situation occurs. Therefore, in the general case it suffices to be able to determine the length of the cycle and the length of the path before entering the cycle, and then this property can be used to reduce the exponent.

### Rigorous proof

This section gives a rigorous proof of the extended Euler's theorem.

??? note "Proof"
    First we show that there exists $k_0\in\mathbf N$ such that the integer $a$ and $m':=\dfrac{m}{\gcd(a^{k_0},m)}$ are coprime. To this end, let $\nu_p(n)$ be the exponent of the prime $p$ in the prime factorization of the integer $n$; then we may take
    
    $$
    k_0 = \max\left\{\left\lceil\dfrac{\nu_p(m)}{\nu_p(a)}\right\rceil : \nu_p(a)>0\right\}.
    $$
    
    Since the exponents of all prime factors that $m$ shares with $a$ are already contained in $a^{k_0}$, $a$ is coprime to the remaining factor $m'=\dfrac{m}{\gcd(a^{k_0},m)}$ of $m$.
    
    Next, for $k\ge k_0$ consider the congruence
    
    $$
    b\equiv a^k. \pmod m
    $$
    
    Since $\gcd(a^{k_0},m)=\gcd(a^k,m)\mid b$, dividing both sides (including the modulus) by $\gcd(a^{k_0},m)$ gives
    
    $$
    \dfrac{b}{\gcd(a^{k_0},m)} \equiv \dfrac{a^{k_0}}{\gcd(a^{k_0},m)}\cdot a^{k-k_0}. \pmod{m'}
    $$
    
    Now, since $a$ is coprime to the modulus $m'$, Euler's theorem can be applied directly, yielding
    
    $$
    \dfrac{b}{\gcd(a^{k_0},m)} \equiv \dfrac{a^{k_0}}{\gcd(a^{k_0},m)}\cdot a^{(k-k_0)\bmod\varphi(m')}. \pmod{m'}
    $$
    
    Therefore, multiplying the factor $\gcd(a^{k_0},m)$ back, we get
    
    $$
    b \equiv a^{k_0}\cdot a^{(k-k_0)\bmod\varphi(m')} = a^{k_0 + (k-k_0)\bmod\varphi(m')}. \pmod{m}
    $$
    
    This gives the form of the extended Euler's theorem. The formula says that the length of the cycle is $\varphi(m')$ and the length of the path before entering the cycle is $k_0$.
    
    The parameters obtained here are tighter than those in the extended Euler's theorem, but they are relatively hard to compute. It can be shown that these parameters can be relaxed to those in the extended Euler's theorem. First, by the [formula for Euler's totient function](./euler-totient.md), since $m'\mid m$, we have $\varphi(m')\mid\varphi(m)$. That is, $\varphi(m)$ is also a cycle length. Second, $k_0$ can also be relaxed to $\varphi(m)$. This is because for all $m\in\mathbf N_+$ and every $p\mid m$, we have
    
    $$
    \begin{aligned}
    \varphi(m) &\ge \varphi(p^{\nu_p(m)}) = (p-1)p^{\nu_p(m)-1} \ge p^{\nu_p(m)-1} \\
    &= (1+(p-1))^{\nu_p(m)-1} \ge 1 + (p-1)(\nu_p(m)-1) \\
    &\ge 1 + (\nu_p(m)-1) = \nu_p(m).
    \end{aligned}
    $$
    
    Here the inequality in the second line uses the binomial expansion, keeping only the constant and linear terms. Therefore,
    
    $$
    k_0 \le \max\{\nu_p(m):p\in\mathbf P\}\le \varphi(m).
    $$
    
    This completes the proof of the stated result.

## Example problem

This section demonstrates a classic application of the extended Euler's theorem through an example problem: computing a power tower modulo an arbitrary modulus. A **power tower** is an expression of the form $A\uparrow(B\uparrow(C\uparrow(D\uparrow\cdots)))$, where $\uparrow$ is Knuth's arrow notation and $A,B,C,D,\cdots$ is a sequence of non-negative integers.

???+ example "[Library Checker - Tetration Mod](https://judge.yosupo.jp/problem/tetration_mod)"
    There are $T$ test cases. In each test case, given $A,B,M$, compute $(A\uparrow\uparrow B)\bmod M$. Here $A\uparrow\uparrow B$ denotes the power tower consisting of $B$ copies of $A$. Formally, define
    
    $$
    A \uparrow\uparrow B =
    \begin{cases}
    1 , & B = 0,\\
    A\uparrow(A\uparrow\uparrow(B-1)), & B > 0.
    \end{cases}
    $$
    
    By convention, $0^0=1$.

??? note "Solution"
    Using the definition of $A\uparrow\uparrow B$, it suffices to compute recursively. To compute $(A\uparrow\uparrow B)\bmod M$, we only need to apply the extended Euler's theorem and compute $(A\uparrow\uparrow(B-1))\bmod\varphi(M)$. Since $\varphi(\varphi(n)) \le n/2$ holds for all $n\ge 2$, the recursion is guaranteed to finish within $O(\log M)$ steps. Since the extended Euler's theorem is applied, we need to distinguish whether the current result is strictly smaller than the current modulus. For this, it suffices to perform one more check when taking the remainder. In addition, care is needed when handling the boundary cases.

??? note "Reference code"
    ```cpp
    --8<-- "docs/math/code/fermat/tetration.cpp"
    ```

??? warning "Proof of correctness of the remainder trick"
    This implementation uses
    
    $$
    r_m(v) = \begin{cases} v\bmod m, &\text{if }v < m, \\ v \bmod m + m, &\text{if }v \ge m\end{cases}
    $$
    
    instead of taking the remainder, which amounts to recording both the remainder information $v\bmod m$ and the overflow information $v \ge m$. The extended Euler's theorem only guarantees that when both the remainder information and the overflow information of the exponent are correct, exponentiation yields the correct remainder information; however, the correctness of the overflow information cannot be guaranteed. For example, when computing $r_6(2^4)$, the exponent has to be reduced modulo $\varphi(6)=2$, and $r_2(4)=2$ (i.e. the remainder is $0$ and there is an overflow), so after exponentiation we get $r_6(2^2) = 4$; compared with the correct answer $r_6(2^4) = 10$, the remainder modulo $6$ is correct, but the overflow information is lost. Nevertheless, it can be proved that although the overflow information may be lost, the remainder information is always correct. Therefore, the exponentiation algorithm based on this remainder trick is also always correct.
    
    Consider the iterative process of the algorithm. Suppose that, backtracking from the innermost level to the outer functions, the first error in the overflow information occurs when computing $r_m(a^k)$. When $k<\varphi(m)$, the exponent is exact and no error can occur, so let $k\ge\varphi(m)$; then $k\ge k\bmod\varphi(m)+\varphi(m)$, i.e. taking the remainder can only underestimate the exponent, overflow information cannot appear out of nowhere, and the only possible error is that an overflow should have been recorded but was not, i.e.
    
    $$
    a^{k\bmod\varphi(m)+\varphi(m)} < m \le a^{k}.
    $$
    
    This inequality can only hold when $a \ge 2$, so the left-hand side is at least $2^{\varphi(m)}$. But $2^{\varphi(m)} < m$ happens only when $m = 6$.[^phi-ineq] Substituting into the inequality above, we get $a^{k\bmod 2 + 2} < 6 \le a^{k}$. In the left-hand side, if $k$ is even, the exponent is $2$, so $a = 2$ and $k \ge 4$; if $k$ is odd, the exponent is $3$ and there is no solution. In summary, the overflow information is lost only when $m=6,~a=2$ and $k\ge 4$ is even.
    
    We now show that the loss of overflow information in this case does not affect the subsequent computation. We only consider the nontrivial case $a_i\ge 2$ (when $a_i\le 1$, the power does not exceed $1$ and no overflow occurs). The modulus of the inner level is $6$, so the modulus $m_1$ after backtracking one level satisfies $\varphi(m_1)=6$ and can only be one of $7,9,14,18$. When backtracking to this level, we need to compute $r_{m_1}(a_1^{k_1})$, where $k_1$ should be $10$ but is actually $4$. However, for all $a_1$ and these $m_1$, we have $a_1^{4}\equiv a_1^{10}\pmod {m_1}$. To see this, note that the [proof](#rigorous-proof) of the extended Euler's theorem above already showed: for any $a$ and $m$, the length $k_0$ of the path before the remainders $a^k\bmod m$ enter the cycle does not exceed $\nu_+(m):=\max\{\nu_p(m) : p\mid m\}$, and the cycle length divides $\varphi(m)$. Since $\nu_+(m_1)\le 2$, $k_1=4$ has already entered the cycle, and it differs from $10$ by $\varphi(m_1)=6$, so the congruence above always holds. Hence the remainder information is correct. Now consider the overflow information. Since the true value of the inner level is $2^k\ge 16>10$, we have $a_1^{2^k}\ge a_1^{10}\ge m_1$, so this level should always mark an overflow. But this level only returns whether $a_1^4$ overflows; the only possible error is $a_1^4<m_1$, i.e. only $a_1=2,~m_1=18$. In the other cases the overflow information is already marked correctly, and the subsequent backtracking is naturally correct. When $a_1=2,~m_1=18$, the level should return $34$ but actually returns $16$, and we need to backtrack one more level; now $m_2$ can only be one of $19,27,38,54$. Then we always have $\nu_+(m_2)\le 3 < 16$ and $34-16=\varphi(m_2)$, so the remainder information is correct; and $a_2^{16}\ge m_2$ always holds, so the overflow information is also correct. Therefore the result is correct at this point, and the subsequent backtracking is necessarily correct as well.
    
    Since the moduli strictly decrease from level to level, $m=6$ appears at most once. In summary, when computing multi-level powers with this remainder trick, the remainder information at every level is correct, and the overflow information is wrong at no more than two levels. Note that the proof does not assume that the bases at all levels are the same, so the conclusion also holds for the case of different bases.

## Exercises

-   [Luogu P5091【模板】扩展欧拉定理 (Template: extended Euler's theorem)](https://www.luogu.com.cn/problem/P5091)
-   [Codeforces 906 D. Power Tower](https://codeforces.com/problemset/problem/906/D)
-   [Luogu P3747 \[六省联考 2017\] 相逢是问候 (Meeting Is a Greeting)](https://www.luogu.com.cn/problem/P3747)
-   [Luogu P4139 上帝与集合的正确用法 (God and the Correct Use of Sets)](https://www.luogu.com.cn/problem/P4139)
-   [Luogu P3934 \[Ynoi Easy Round 2016\] 炸脖龙 I (Jabberwocky I)](https://www.luogu.com.cn/problem/P3934)
-   [Luogu P6736「Wdsr-2」白泽教育 (Bai Ze's Education)](https://www.luogu.com.cn/problem/P6736)

## References and notes

-   [Fermat's little theorem - Wikipedia](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem)
-   [Euler's theorem - Wikipedia](https://en.wikipedia.org/wiki/Euler%27s_theorem)
-   Hardy, Godfrey Harold, and Edward Maitland Wright. An introduction to the theory of numbers. Oxford university press, 1979.

[^ex-euler]: This name appears mainly in competitive programming circles and is not the generally accepted name of this result.

[^phi-ineq]: According to the paper Kendall, R. and Osborn, R. (1965) Two Simple Lower Bounds for the Euler ϕ-Function. Texas Journal of Science, 17, 324-326, for $m > 6$ we always have $\varphi(m)\ge\sqrt{m}$. A direct computation shows that for $m\ge 16$ we always have $\sqrt{m}\ge\log_2m$. Therefore, the inequality $\varphi(m)\ge\log_2m$ holds for all $m\ge 16$. The remaining cases can be verified one by one.
