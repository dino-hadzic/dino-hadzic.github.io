---
title: Factorial modulo a number
---

## Introduction

This article discusses results related to computing factorials modulo a given number and provides a computation method whose time complexity is linear in the size of the modulus, so the method is mainly suitable when the modulus is not too large ($\sim 10^6$). Besides the method described in this article, depending on the situation, [polynomial techniques](../poly/shift.md#模素数意义下阶乘) can also be applied for fast computation.

By the [Chinese remainder theorem](./crt.md), the problem of computing a factorial modulo a number can be reduced to the case where the modulus is a prime power $p^\alpha$. When dealing with such problems, for a prime $p$ and a positive integer $n$ one often needs to extract all factors $p$ from the factorial $n!$, obtaining the decomposition:

$$
n! = p^{\nu_p(n!)}(n!)_p.
$$

Here, $\nu_p(n!)$ denotes the exponent of $p$ in the prime factorization of the factorial $n!$, and $(n!)_p$ denotes the integer obtained by removing all powers of $p$ from the value of the factorial $n!$. This article discusses the remainder of $(n!)_p$ modulo a prime (power) and the concrete way to compute the exponent $\nu_p(n!)$.

This decomposition is especially useful when solving problems in which factorials appear simultaneously in the numerator and the denominator of the desired expression, for example when [computing binomial coefficients modulo a given number](./lucas.md). For such problems, the exponents of $p$ in the numerator and the denominator can be subtracted directly, while the parts $(n!)_p$ coprime to $p$ can be computed using the [modular inverse](./inverse.md).

This article also presents Wilson's theorem and its generalization, Legendre's formula and Kummer's theorem, which are related to the above problem.

## Wilson's theorem

Wilson's theorem gives a necessary and sufficient condition for a natural number to be prime.

???+ note "Wilson's theorem"
    For a natural number $n>1$, $(n-1)!\equiv -1\pmod n$ holds if and only if $n$ is prime.

??? note "Proof"
    First, we prove that for a prime $p$ we have $(p-1)!\equiv -1\pmod{p}$. For this, two concise proofs can be obtained using [congruences](./congruence-equation.md#congruences-modulo-a-prime) or [primitive roots](./primitive-root.md); we omit them here. Below we give a proof that requires fewer prerequisites:
    
    For $p=2$ the statement obviously holds. Now let $p\geq 3$; we need to prove that the product of all nonzero elements (i.e. residue classes) of $\mathbf{Z}_p$ equals $\overline{-1}$. Since every nonzero element $\overline{a}$ of $\mathbf{Z}_p$ has an inverse $\overline{a}^{-1}$, the product of mutually inverse elements of $\mathbf{Z}_p$ equals $\overline{1}$. However, note that $\overline{a}$ and $\overline{a}^{-1}$ may be equal: $\overline{a}=\overline{a}^{-1}$ if and only if $a^2\equiv 1\pmod p$, i.e.
    
    $$
    0\equiv a^2-1\equiv (a+1)(a-1)\pmod p,
    $$
    
    hence $a\equiv 1\pmod p$ or $a\equiv -1\pmod p$. This shows that the product of all elements of $\mathbf{Z}_p\setminus\{\overline{0},\overline{1},\overline{-1}\}$ equals $\overline{1}$, and therefore the product of all nonzero elements of $\mathbf{Z}_p$ equals $\overline{-1}$.
    
    Conversely, for a composite $n$ we need to prove that $(n-1)!\not\equiv-1\pmod{n}$. We argue by contradiction: suppose $(n-1)!\equiv -1\pmod{n}$, i.e. there exists an integer $k$ such that $(n-1)!=kn-1$. Since $n$ is composite, there necessarily exists a prime $p<n$ such that $n=pm$, so $(n-1)!=kpm-1\equiv -1\pmod{p}$. However, $p$ necessarily already appears in the product $(n-1)!$, so we must have $(n-1)!\equiv 0\pmod{p}$. This contradiction shows that $(n-1)!\not\equiv-1\pmod{n}$.

In the notation of this article, Wilson's theorem can be written as $(p!)_p\equiv -1\pmod{p}$.

### Generalization

Wilson's theorem can be generalized to the case of a general modulus.

???+ note "Theorem (Gauss)"
    For a natural number $m>1$, we have
    
    $$
    \prod_{1\le k<m,\ k\perp m} k \equiv \pm 1 \pmod{m}.
    $$
    
    Moreover, the remainder $\pm 1$ equals $-1$ if and only if [a primitive root exists](./primitive-root.md#原根存在定理) modulo $m$, i.e. when $m=2,4,p^\alpha,2p^\alpha$, where $p$ is an odd prime and $\alpha$ is a positive integer.

??? note "Proof"
    This theorem can be proved simply via the structure of the [multiplicative group of integers modulo $m$](../algebra/ring-theory.md#应用整数同余类的乘法群). Here we give a proof with a similar idea but more elementary.
    
    For $m=2$, we have $1!=1\equiv -1\pmod{2}$. For the other cases where a primitive root exists, let $g$ be a primitive root; then every positive integer $k$ less than $m$ and coprime to it can be uniquely written in the form $g^i\bmod m$, where $0\le i<\varphi(m)$ and $\varphi(m)$ is [Euler's totient function](./euler-totient.md). By direct verification, $\varphi(m)$ is necessarily even. Since $g^i$ and $g^{\varphi(m)-i}$ are multiplicative inverses of each other, pairing them up in the product gives
    
    $$
    \prod_{1\le k<m,\ k\perp m} k \equiv \prod_{i=0}^{\varphi(m)-1}g^i = g^{\varphi(m)/2}\prod_{i=1}^{\varphi(m)/2-1}g^{i}g^{\varphi(m)-i} \equiv g^{\varphi(m)/2} \pmod{m}.
    $$
    
    Since $g^{\varphi(m)/2}\bmod m$ is the only element different from $1\bmod{m}$ that is its own multiplicative inverse, it equals $-1\bmod{m}$. This shows that the remainder in this case equals $-1$.
    
    For the case where no primitive root exists modulo $m$, we need to prove that the remainder equals $1$. To this end, first take the prime factorization $m=p_1^{e_1}p_2^{e_2}\cdots p_s^{e_s}$, and then by the [Chinese remainder theorem](./crt.md) it suffices to prove that
    
    $$
    \prod_{1\le k<m,\ k\perp m} k\equiv 1\pmod{p_j^{e_j}}
    $$
    
    holds for all factors $p_j^{e_j}$. The Chinese remainder theorem states that every possible combination of remainders $(r_1,r_2,\cdots,r_s)$, where $1\le r_j<p_j^{e_j}$ and $p_j\perp r_j$, corresponds uniquely to one number with $1\le k<m$ and $k\perp m$ such that $k\equiv r_j\pmod{p_j^{e_j}}$. Therefore, for every remainder $r_j$ there are exactly ${\varphi(m)}/{\varphi(p_j^{e_j})}$ values of $k$ such that $k\equiv r_j\pmod{p_j^{e_j}}$. Using this, we can group the product and obtain
    
    $$
    \prod_{1\le k<m,\ k\perp m} k\equiv\left(\prod_{1\le r_j<p_j^{e_j},\ r_j\perp p_j} r_j\right)^{{\varphi(m)}/{\varphi(p_j^{e_j})}}\pmod{p_j^{e_j}}.
    $$
    
    For the exponent ${\varphi(m)}/{\varphi(p_j^{e_j})}=\varphi(m/p_j^{e_j})$ here to be odd, we must have $m/p_j^{e_j}=1,2$, because Euler's totient function $\varphi(n)$ is even for all $n\ge 3$. If $p_j$ is an odd prime, since no primitive root exists modulo $m$, necessarily $m/p_j^{e_j}\neq 1,2$; if $p_j^{e_j}=2,4$, since no primitive root exists modulo $m$, $m/p_j^{e_j}$ necessarily contains some odd prime factor and is therefore greater than $2$: in both cases the exponent ${\varphi(m)}/{\varphi(p_j^{e_j})}$ is even. The term in parentheses in the formula above has already been shown to be congruent to $-1$ modulo $p_j^{e_j}$, so the remainder of this power modulo $p_j^{e_j}$ must be $1$. The only remaining case is $p_j=2$ and $e_j>2$, for which we can prove directly:
    
    $$
    \prod_{1\le r_j<2^{e_j},\ r_j\perp 2}r_j \equiv 1\pmod{2^{e_j}}.
    $$
    
    Following the idea of the previous proof, all odd numbers $r_j$ with $1\le r_j<2^{e_j}$ can be paired up so that they cancel; those that cannot be paired are necessarily solutions of the equation $x^2\equiv 1\pmod{2^{e_j}}$. This equation means $2^{e_j}\mid (x-1)(x+1)$. Let $x=2y+1$; then necessarily $2^{e_j-2}\mid y(y+1)$, and since one of $y$ and $y+1$ is odd and the other even, we get $y=t2^{e_j-2}$ or $y=t2^{e_j-2}-1$. Hence $x=t2^{e_j-1}\pm 1$ where $t$ is an integer. Among the remainders modulo $2^{e_j}$ there are only four such: $\pm 1$ and $2^{e_j-1}\pm 1$. Therefore,
    
    $$
    \prod_{1\le r_j<2^{e_j},\ r_j\perp 2}r_j \equiv (-1)(2^{e_j-1}-1)(2^{e_j-1}+1) \equiv 1\pmod{2^{e_j}}.
    $$
    
    This completes the proof for all cases.

In computations, the case where the modulus is a prime power is especially important:

???+ note "Corollary"
    For a prime $p$ and a positive integer $\alpha$, we have
    
    $$
    \prod_{1\le k<p^\alpha,\ k\perp p}k \equiv 
    \begin{cases}
    1, & p=2\text{ and }\alpha\ge3,\\
    -1, &\text{otherwise}
    \end{cases}
    \pmod{p^\alpha}.
    $$

Note that the left-hand side is not $(p^\alpha!)_p$, because the latter also includes the contribution of the multiples of $p$.

## Computing the factorial remainder

This section discusses the computation of the remainder $(n!)_p\bmod p^{\alpha}$.

### The prime modulus case

The expression $(n!)_p$ has an obvious recursive structure. To notice it, let us first look at a concrete example:

???+ example "Example"
    To compute $(32!)_5 \bmod{5}$, we can perform the following recursive computation:
    
    $$
    \begin{aligned}
    (32!)_5 &= 1\times 2\times 3 \times 4\times \underbrace{1}_{5}\times 6 \times 7 \times 8\times 9 \times \underbrace{2}_{10} \\
    &\quad\times 11 \times 12 \times 13 \times 14\times \underbrace{3}_{15}\times 16 \times 17\times 18\times 19\times \underbrace{4}_{20} \\
    &\quad\times 21 \times 22 \times 23 \times 24\times \underbrace{1}_{25}\times 26 \times 27\times 28\times 29\times \underbrace{6}_{30} \times 31 \times 32 \\
    &\equiv 1\times 2\times 3 \times 4\times \underbrace{1}_{5}\times 1 \times 2 \times 3\times 4 \times \underbrace{2}_{10} \\
    &\quad\times 1 \times 2 \times 3 \times 4\times \underbrace{3}_{15}\times 1 \times 2\times 3\times 4\times \underbrace{4}_{20} \\
    &\quad\times 1 \times 2 \times 3 \times 4\times \underbrace{1}_{25}\times 1 \times 2\times 3\times 4\times \underbrace{1}_{30}\times 1\times 2\\
    &= (1\times 2\times 3\times 4)^{6}\times(1\times 2)\times(\underbrace{1}_{5}\times \underbrace{2}_{10}\times \underbrace{3}_{15} \times \underbrace{4}_{20}\times \underbrace{1}_{25}\times \underbrace{1}_{30}) \pmod{5}
    \end{aligned}
    $$
    
    We can see that, thanks to the periodicity of remainders modulo $5$, this product can be divided into several blocks of length $5$, and the only difference between the blocks is the remainder of the last element. Since dividing $32$ by $5$ gives quotient $6$ and remainder $2$, the product can be divided into $6$ complete blocks and a final incomplete block of length $2$. Therefore, we can extract from the first $6$ blocks the parts without their last elements (this part is exactly what Wilson's theorem handles), then multiply by the product of the last incomplete block, and finally multiply by the product of the last elements of the first $6$ blocks. The last element of each block is a multiple of $5$, so after removing the powers of $5$, their product is exactly $(6!)_{5}\pmod{5}$. This reduces the original problem to a problem of smaller size.

Generalizing the recursive structure of this example, we obtain the following recurrence:

???+ note "Recurrence"
    For a prime $p$ and a positive integer $n$, we have
    
    $$
    (n!)_p \equiv (-1)^{\left\lfloor n/p\right\rfloor}\cdot (n\bmod p)!\cdot\left(\left\lfloor n/p\right\rfloor!\right)_p\pmod{p}.
    $$

??? note "Proof"
    Let $(n)_p$ denote the result of removing all powers of $p$ from the prime factorization of $n$. Then we have
    
    $$
    \begin{aligned}
    (n!)_p &= \prod_{k=1}^n(k)_p = \left(\prod_{1\le k\le n,\ k\perp p}(k)_p\right)\left(\prod_{1\le k\le\lfloor n/p\rfloor}(pk)_p\right) \\
    &= \left(\prod_{i=0}^{\lfloor n/p\rfloor-1}\prod_{j=1}^{p-1}(ip+j)\right)\left(\prod_{j=1}^{n\bmod p}(\lfloor n/p\rfloor p+j)\right)\left(\prod_{1\le k\le\lfloor n/p\rfloor}(k)_p\right) \\
    &\equiv\left(\prod_{j=1}^{p-1}j\right)^{\lfloor n/p\rfloor}\left(\prod_{j=1}^{n\bmod p}j\right)(\lfloor n/p\rfloor!)_p \\
    &\equiv (-1)^{\lfloor n/p\rfloor}\cdot(n\bmod p)!\cdot(\lfloor n/p\rfloor!)_p \pmod p.
    \end{aligned}
    $$
    
    This completes the proof. Below we give a concrete explanation of this formal proof.
    
    We want to compute the value of $(n!)_p\bmod p$. Following the example above, we have
    
    $$
    \begin{aligned}
    (n!)_p &= 1 \cdot 2 \cdot 3 \cdot \ldots \cdot (p-2) \cdot (p-1) \cdot \underbrace{1}_{p} \cdot (p+1) \cdot (p+2) \cdot \ldots \cdot (2p-1) \cdot \underbrace{2}_{2p} \\
    &\quad \cdot (2p+1) \cdot \ldots \cdot (p^2-1) \cdot \underbrace{1}_{p^2} \cdot (p^2 +1) \cdot \ldots \cdot n \\
    &\equiv 1 \cdot 2 \cdot 3 \cdot \ldots \cdot (p-2) \cdot (p-1) \cdot \underbrace{1}_{p} \cdot 1 \cdot 2 \cdot \ldots \cdot (p-1) \cdot \underbrace{2}_{2p} \cdot 1 \cdot 2 \\
    &\quad \cdot \ldots \cdot (p-1) \cdot \underbrace{1}_{p^2} \cdot 1 \cdot 2 \cdot \ldots \cdot (n \bmod p) \pmod{p}.
    \end{aligned}
    $$
    
    It can be clearly seen that, except for the last block, the factorial is divided into several complete blocks of the same length.
    
    $$
    \begin{aligned}
    (n!)_p&\equiv \underbrace{1 \cdot 2 \cdot 3 \cdot \ldots \cdot (p-2) \cdot (p-1) \cdot 1}_{1\text{st}} \cdot \underbrace{1 \cdot 2 \cdot 3 \cdot \ldots \cdot (p-2) \cdot (p-1) \cdot 2}_{2\text{nd}} \cdot \ldots \\
    &\quad \cdot \underbrace{1 \cdot 2 \cdot 3 \cdot \ldots \cdot (p-2) \cdot (p-1) \cdot 1}_{p\text{th}} \cdot \ldots \cdot \quad \underbrace{1 \cdot 2 \cdot \ldots \cdot (n \bmod p)}_{\text{tail}} \pmod{p}.
    \end{aligned}
    $$
    
    The main part of a complete block, excluding its last element, i.e. $(p-1)!\bmod p$, is easy to compute: Wilson's theorem applies:
    
    $$
    (p-1)!\equiv -1\pmod p.
    $$
    
    There are $\left\lfloor \dfrac{n}{p} \right\rfloor$ complete blocks in total, so $\left\lfloor \dfrac{n}{p} \right\rfloor$ has to be put into the exponent of $-1$.
    
    The value of the last, partial block is $(n\bmod p)!\bmod p$ and can be computed separately.
    
    What remains are the last elements of each block. If we hide the already processed elements, we can see the following pattern:
    
    $$
    (n!)_p = \underbrace{ \ldots \cdot 1 } \cdot \underbrace{ \ldots \cdot 2} \cdot \ldots \cdot \underbrace{ \ldots \cdot (p-1)} \cdot \underbrace{ \ldots \cdot 1 } \cdot \underbrace{ \ldots \cdot 1} \cdot \underbrace{ \ldots \cdot 2} \cdots
    $$
    
    This is also a modified factorial, only of much shorter length. It is:
    
    $$
    \left(\left\lfloor \frac{n}{p} \right\rfloor !\right)_p.
    $$
    
    Multiplying all the parts together, we obtain the recurrence above.

When computing with this recurrence, the recursion depth is $O(\log_p n)$. If the middle term is recomputed every time, the computation at each level costs $O(p)$, and the total time complexity is $O(p\log_p n)$; if $n!\bmod p$ is precomputed for all $n=1,2,\cdots,p-1$, the precomputation costs $O(p)$, the computation at each level costs $O(1)$, and the total time complexity is $O(p+\log_p n)$.

Since the recursion is a tail recursion, the implementation can be iterative. The following implementation precomputes the first $p-1$ factorials; if the function needs to be called multiple times, the precomputation can be moved outside the function.

??? example "Reference implementation"
    ```cpp
    --8<-- "docs/math/code/factorial/fact-mod-p.cpp:core"
    ```

If memory is limited and not all factorials can be stored, one can also compute all the values $n$ of the factorials $n!\bmod p$ actually used in the function calls, then sort them, and finally compute the values of these factorials all at once and combine them into the final result, thereby avoiding storing the values of all factorials.

### The prime power modulus case

The case of a prime power modulus can be solved following the prime modulus case; it suffices to replace Wilson's theorem by its generalization. In both results of this section, $\pm 1$ refers specifically to the following definition: for $p=2$ and $\alpha\ge 3$ it is $1$, and in all other cases it is $-1$.

???+ note "Recurrence"
    For a prime $p$ and positive integers $\alpha,n$, we have
    
    $$
    (n!)_{p} \equiv (\pm 1)^{\lfloor n/p^\alpha\rfloor}\cdot\left(\prod_{1\le j\le (n\bmod p^\alpha),\ j\perp p}j\right)\cdot(\lfloor n/p\rfloor!)_p\pmod{p^\alpha}.
    $$
    
    Here, the value of $\pm 1$ is as specified in the [generalization of Wilson's theorem](#generalization).

??? note "Proof"
    The idea of the proof is exactly the same as in the prime modulus case. Let $(k)_p$ denote the result of removing all powers of $p$ from the prime factorization of $k$; then
    
    $$
    \begin{aligned}
    (n!)_p
    &= \prod_{1\le k\le n}(k)_p = \left(\prod_{1\le k\le n,\ k\perp p}(k)_p\right)\left(\prod_{1\le k\le\lfloor n/p\rfloor}(pk)_p\right) \\
    &= \left(\prod_{i=0}^{\lfloor n/p^\alpha\rfloor-1}\prod_{1\le j\le p^\alpha,\ j\perp p}(ip^\alpha+j)_p\right)\left(\prod_{1\le j\le (n\bmod p^\alpha),\ j\perp p}(\lfloor n/p^\alpha\rfloor p^\alpha+j)_p\right)\left(\prod_{1\le k\le\lfloor n/p\rfloor}(k)_p\right)\\
    &\equiv \left(\prod_{1\le j\le p^\alpha,\ j\perp p}j\right)^{\lfloor n/p^\alpha\rfloor}\cdot\left(\prod_{1\le j\le (n\bmod p^\alpha),\ j\perp p}j\right)\cdot(\lfloor n/p\rfloor!)_p\\
    &\equiv (\pm 1)^{\lfloor n/p^\alpha\rfloor}\cdot\left(\prod_{1\le j\le (n\bmod p^\alpha),\ j\perp p}j\right)\cdot(\lfloor n/p\rfloor!)_p \pmod{p^\alpha}.
    \end{aligned}
    $$

Apart from the fact that $-1$ may need to be replaced by $\pm 1$, the difference from the prime modulus case also lies in the data being precomputed. For the prime power modulus case, for all positive integers $n$ not exceeding $p^\alpha$ we need to precompute the product of all integers from $1$ to $n$ that are not multiples of $p$, i.e.

$$
\prod_{1\le k\le n,\ k\perp p} k\bmod{p^\alpha}.
$$

In the prime modulus case, for $n<p$, this degenerates to $n!\bmod p$, but this expression no longer applies in the general prime power case.

Below we give an example of computing the factorial remainder in the prime power modulus case, to help understand the method above:

???+ example "Example"
    To compute $(32!)_3\bmod 9$, we can perform the following recursive computation:
    
    $$
    \begin{aligned}
    (32!)_3 
    &= 1\times 2\times \underbrace{1}_{3} \times 4\times 5\times \underbrace{2}_{6}\times 7\times 8\times\underbrace{1}_{9}\\
    &\quad\times 10\times 11\times\underbrace{4}_{12}\times 13\times 14\times\underbrace{5}_{15}\times 16\times 17\times\underbrace{2}_{18}\\
    &\quad\times 19\times 20\times\underbrace{7}_{21}\times 22\times 23\times\underbrace{8}_{24}\times 25\times 26\times\underbrace{1}_{27}\\
    &\quad\times 28\times 29\times\underbrace{10}_{30}\times 31\times 32\\
    &\equiv 1\times 2\times \underbrace{1}_{3} \times 4\times 5\times \underbrace{2}_{6}\times 7\times 8\times\underbrace{1}_{9}\\
    &\quad\times 1\times 2\times\underbrace{4}_{12}\times 4\times 5\times\underbrace{5}_{15}\times 7\times 8\times\underbrace{2}_{18}\\
    &\quad\times 1\times 2\times\underbrace{7}_{21}\times 4\times 5\times\underbrace{8}_{24}\times 7\times 8\times\underbrace{1}_{27}\\
    &\quad\times 1\times 2\times\underbrace{1}_{30}\times 4\times 5\\
    &=(1\times 2\times 4\times 5\times 7\times 8)^{3}\times (1\times 2\times 4\times 5)\\
    &\quad\times\begin{pmatrix}\underbrace{1}_{3}\times\underbrace{2}_{6}\times\underbrace{1}_{9}\times\underbrace{4}_{12}\times\underbrace{5}_{15}\times\underbrace{2}_{18}\\\times\underbrace{7}_{21}\times\underbrace{8}_{24}\times\underbrace{1}_{27}\times\underbrace{1}_{30}\end{pmatrix}\pmod{9}.
    \end{aligned}
    $$
    
    The result of decomposing the expression $(32!)_3\bmod 9$ can likewise be divided into three parts:
    
    -   complete blocks: the product of all integers in the range $1\sim 9$ not divisible by $3$, $\lfloor 32/9\rfloor=3$ blocks in total;
    -   the incomplete tail block: the product of all integers not divisible by $3$ from $1$ up to $32\bmod 9$;
    -   the product of all integers divisible by $3$; comparing with the result after the second-to-last equals sign, we see that this is exactly its first $\lfloor 32/3\rfloor=10$ terms, i.e. $(\lfloor 32/3\rfloor!)_3\bmod 9$.
    
    The part in the last parentheses is solved recursively; this reduces the original problem to a smaller one.

From this we obtain the following recursive result:

???+ note "Recursive result"
    For a prime $p$ and positive integers $\alpha,n$, we have
    
    $$
    (n!)_p \equiv (\pm 1)^{\sum_{j\ge\alpha}\lfloor{n}/{p^j}\rfloor}\prod_{j\ge 0}F(\lfloor n/p^j\rfloor\bmod p^\alpha)\pmod{p^\alpha},
    $$
    
    where $F(m) = \prod_{1\le k\le m,\ k\perp p} k\bmod{p^\alpha}$ and the value of $\pm 1$ is as described above.

The implementation for the prime power modulus case is similar to that for the prime modulus case, differing only in some details. As above, the precomputation can be moved outside the function.

??? example "Reference implementation"
    ```cpp
    --8<-- "docs/math/code/factorial/fact-mod-pa.cpp:core"
    ```

The time complexity of the precomputation is $O(p^\alpha)$, and the time complexity of a single query is $O(\log_p n)$.

## Computing the multiplicity

This section discusses the computation of the exponent $\nu_p(n!)$ of $p$ in the factorial $n!$, which can be used to compute remainders of binomial coefficients. In a binomial coefficient, factorials appear in both the numerator and the denominator, so whether the prime $p$ in the numerator and the denominator cancels out becomes a key factor determining the final remainder.

### Legendre's formula

The exponent of a prime $p$ in the factorial $n!$ can be computed by Legendre's formula, and it is related to the representation of $n$ in base $p$.

???+ note "Legendre's formula"
    For a positive integer $n$, the exponent $\nu_p(n!)$ of the prime $p$ contained in the factorial $n!$ is
    
    $$
    \nu_p(n!) = \sum_{i=1}^{\infty} \left\lfloor \dfrac{n}{p^i} \right\rfloor = \dfrac{n-S_p(n)}{p-1},
    $$
    
    where $S_p(n)$ is the sum of the digits of $n$ in base $p$. In particular, the exponent of $2$ in the factorial is $\nu_2(n!)=n-S_2(n)$.

??? note "Proof"
    Because
    
    $$
    n! = 1\times 2\times \cdots \times p\times \cdots \times 2p\times \cdots \times \lfloor n/p\rfloor p\times \cdots \times n.
    $$
    
    Here, the product of the multiples of $p$ is $p\times 2p\times \cdots \times \lfloor n/p\rfloor p=p^{\lfloor n/p\rfloor }\lfloor n/p\rfloor !$, and $\lfloor n/p\rfloor !$ may continue to contain multiples of $p$. Therefore, for the exponent we have the recurrence relation:
    
    $$
    \nu_p(n!) = \lfloor n/p\rfloor + \nu_p(\lfloor n/p\rfloor!).
    $$
    
    Expanding it gives Legendre's formula.
    
    To prove the second equality, first expand $n$ in base $p$, which amounts to writing it as the following sum:
    
    $$
    n = n_\ell p^{\ell} + \cdots + n_1 p + n_0 = \sum_{k=0}^\ell n_kp^k.
    $$
    
    Therefore, we have
    
    $$
    \begin{aligned}
    \nu_p(n!)
    &= \sum_{i=1}^{\ell}\left\lfloor\dfrac{n}{p^i}\right\rfloor 
    = \sum_{i=1}^\ell\sum_{k=i}^{\ell}n_kp^{k-i}
    = \sum_{k=1}^\ell n_k\sum_{i=1}^kp^{k-i} \\
    &= \sum_{k=1}^\ell n_k\dfrac{p^k-1}{p-1} 
    = \dfrac{\sum_{k=0}^\ell n_kp^k - \sum_{k=0}^\ell n_k}{p-1} 
    = \dfrac{n - S_p(n)}{p-1}.
    \end{aligned}
    $$

A reference implementation for computing the exponent of a prime in a factorial is as follows:

??? example "Reference implementation"
    ```cpp
    --8<-- "docs/math/code/factorial/multiplicity.cpp:core"
    ```

Its time complexity is $O(\log n)$.

### Kummer's theorem

The remainders of binomial coefficients modulo a number often form a fractal structure; for example, the Sierpiński triangle can be obtained from binomial coefficients modulo $2$.

A careful analysis shows that whether $p$ divides a binomial coefficient is actually related to whether borrowing is needed when subtracting the lower index from the upper index in base $p$. This gives **Kummer's theorem**.

???+ note "Kummer's theorem"
    The exponent of a prime $p$ in the binomial coefficient $\dbinom{m}{n}$ is exactly the number of borrows needed when subtracting $n$ from $m$ in base $p$, i.e.
    
    $$
    \nu_p\left(\dbinom{m}{n}\right)=\frac{S_p(n)+S_p(m-n)-S_p(m)}{p-1}.
    $$
    
    In particular, the exponent of $2$ in the binomial coefficient is $\nu_2\left(\dbinom{m}{n}\right)=S_2(n)+S_2(m-n)-S_2(m)$.

??? note "Proof"
    First we prove the expression below. For this, by Legendre's formula we have
    
    $$
    \begin{aligned}
    \nu_p\left(\dbinom{m}{n}\right)
    &=\nu_p(m!)-\nu_p(n!)-\nu_p((m-n)!)\\
    &=\sum_{i=1}^\infty\left(\left\lfloor\dfrac{m}{p^i}\right\rfloor-\left\lfloor\dfrac{n}{p^i}\right\rfloor-\left\lfloor\dfrac{m-n}{p^i}\right\rfloor\right)\\
    &=\frac{S_p(n)+S_p(m-n)-S_p(m)}{p-1}.
    \end{aligned}
    $$
    
    This expression can be understood as the number of borrows needed when subtracting $n$ from $m$ in base $p$. Indeed, if when computing the $i$-th digit (the lowest digit has index $1$) the subtraction is not possible and a borrow is needed, then the number formed by the digits above the $i$-th in the result of the subtraction, $\left\lfloor\dfrac{m-n}{p^i}\right\rfloor$, is actually the difference obtained by taking the number formed by the digits above the $i$-th in $m$, $\left\lfloor\dfrac{m}{p^i}\right\rfloor$, subtracting one (namely the borrowed one), and then subtracting the number formed by the digits above the $i$-th in $n$, $\left\lfloor\dfrac{n}{p^i}\right\rfloor$; therefore, the difference
    
    $$
    \left\lfloor\dfrac{m}{p^i}\right\rfloor-\left\lfloor\dfrac{n}{p^i}\right\rfloor-\left\lfloor\dfrac{m-n}{p^i}\right\rfloor = 1
    $$
    
    if and only if a borrow occurred; otherwise, this difference is $0$. Therefore, the sum in the expression above can be understood as the number of borrows. This gives the verbal formulation of Kummer's theorem.

## Example problem

???+ example "Example problem [HDU 2973 - YAPTCHA](https://acm.hdu.edu.cn/showproblem.php?pid=2973)"
    Given $n$, compute
    
    $$
    \sum_{k=1}^n\left\lfloor\frac{(3k+6)!+1}{3k+7}-\left\lfloor\frac{(3k+6)!}{3k+7}\right\rfloor\right\rfloor
    $$

??? note "Solution idea"
    If $3k+7$ is prime, then
    
    $$
    (3k+6)!\equiv-1\pmod{3k+7}
    $$
    
    Let $(3k+6)!+1=m(3k+7)$
    
    Then
    
    $$
    \left\lfloor\frac{(3k+6)!+1}{3k+7}-\left\lfloor\frac{(3k+6)!}{3k+7}\right\rfloor\right\rfloor=\left\lfloor m-\left\lfloor m-\frac{1}{3k+7}\right\rfloor\right\rfloor=1
    $$
    
    If $3k+7$ is not prime, then it is a composite number greater than $4$, and we have $(3k+7)\mid(3k+6)!$, i.e.
    
    $$
    (3k+6)!\equiv 0\pmod{3k+7}
    $$
    
    Let $(3k+6)!=m(3k+7)$; then
    
    $$
    \left\lfloor\frac{(3k+6)!+1}{3k+7}-\left\lfloor\frac{(3k+6)!}{3k+7}\right\rfloor\right\rfloor=\left\lfloor m+\frac{1}{3k+7}-m\right\rfloor=0
    $$
    
    Therefore
    
    $$
    \sum_{k=1}^n\left\lfloor\frac{(3k+6)!+1}{3k+7}-\left\lfloor\frac{(3k+6)!}{3k+7}\right\rfloor\right\rfloor=\sum_{k=1}^n[3k+7\text{ is prime}]
    $$

??? example "Reference code"
    ```cpp
    --8<-- "docs/math/code/factorial/wilson_1.cpp"
    ```

## References

-   冯克勤 (Feng Keqin). “初等数论及其应用” (Elementary Number Theory and Its Applications).
-   [Wilson's theorem - Wikipedia](https://en.wikipedia.org/wiki/Wilson%27s_theorem)
-   [Legendre's formula - Wikipedia](https://en.wikipedia.org/wiki/Legendre%27s_formula)

**This page is mainly translated from the blog post [Вычисление факториала по модулю](http://e-maxx.ru/algo/modular_factorial) and its English translation [Factorial modulo p](https://cp-algorithms.com/algebra/factorial-modulo.html). The Russian version is licensed under Public Domain + Leave a Link; the English version under CC-BY-SA 4.0. The content has been modified.**
