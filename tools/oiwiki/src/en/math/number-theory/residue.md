---
title: Higher-order residues & roots of unity
---

Prerequisites: [Discrete logarithm](./discrete-logarithm.md)

This article discusses higher-order residues and roots of unity in modular arithmetic, and introduces algorithms for root extraction modulo an integer.

## Higher-order residues

Higher-order residues in modular arithmetic can be thought of as the question of whether higher-order roots can be taken modulo an integer. They are a generalization of [quadratic residues](./quad-residue.md).

???+ abstract "$k$-th residue"
    Let $k\geq 2$ be an integer, and let the integer $a$ and the positive integer $m$ be coprime. If there exists an integer $x$ such that
    
    $$
    x^k\equiv a\pmod m,
    $$
    
    then $a$ is called a **$k$-th residue** modulo $m$, and $x$ is called a **$k$-th root** of $a$ modulo $m$; otherwise $a$ is called a **$k$-th nonresidue** modulo $m$.

In other words, a $k$-th root of $a$ modulo $m$ exists if and only if $a$ is a $k$-th residue modulo $m$.

### Properties

Similarly to quadratic residues, we can discuss the questions of deciding $k$-th residues, the number of roots, and the number of classes of $k$-th residues. As with other problems about [congruence equations](./congruence-equation.md), they can be reduced to the case of a prime-power modulus via the [Chinese remainder theorem](./crt.md). Depending on whether a primitive root exists, this is further divided into the case of an odd prime power and the case where the modulus is a power of $2$.

The case of an odd prime power is relatively simple. In fact, for all cases where a primitive root exists, the following conclusion holds:

???+ note "Theorem"
    Let $k\geq 2$ be an integer, and let the integer $a$ and the positive integer $m$ be coprime. Suppose a primitive root modulo $m$ exists, and let $g$ be a primitive root modulo $m$. Denote $d=\gcd(k,\varphi(m))$ and $d'=\dfrac{\varphi(m)}{d}$, where $\varphi(m)$ is [Euler's totient function](./euler-totient.md). Then:
    
    1.  $a$ is a $k$-th residue modulo $m$ if and only if
    
        $$
        a^{d'} \equiv 1 \pmod m.
        $$
    2.  When $a$ is a $k$-th residue modulo $m$, $a$ has, up to congruence, exactly $d$ pairwise distinct $k$-th roots modulo $m$, and they have the form
    
        $$
        x \equiv g^{y_0+id'}\pmod m,~0\le y_0 < d',~i=0,1,\cdots,d-1.
        $$
    3.  The number of classes of $k$-th residues modulo $m$ is $d'$, and all of them together form the set
    
        $$
        \{g^{di}\bmod m : 0 \le i < d'\}.
        $$

??? note "Proof"
    Since $a\perp m$, we have $x\perp m$. Since $g$ is a primitive root modulo $m$, both $x$ and $a$ are congruent to some power of $g$. Let $x\equiv g^y\pmod m$; the equation $x^k\equiv a\pmod m$ is then equivalent to
    
    $$
    g^{ky} \equiv g^{\operatorname{ind}_g a}\pmod m.
    $$
    
    Here, $\operatorname{ind}_g a$ is the discrete logarithm. By the [properties of the order](./primitive-root.md#幂的循环结构) and $\delta_m(g)=\varphi(m)$, this is equivalent to the congruence
    
    $$
    ky \equiv \operatorname{ind}_g a \pmod{\varphi(m)}.
    $$
    
    This is a [linear congruence](./linear-equation.md) in $y$. Applying the analysis of the structure of its solutions from that page, we know that the equation has a solution if and only if $d\mid\operatorname{ind}_g a$, and the general solution has the form
    
    $$
    y \equiv y_0 + id' \pmod{\varphi(m)},~0\le y_0 < d',~i=0,1,\cdots,d-1.
    $$
    
    From this, almost the entire content of the theorem follows; the only thing that still needs explanation is the criterion $a^{d'} \equiv 1 \pmod m$. By [property 3 of the order](./primitive-root.md#幂的循环结构), we have
    
    $$
    \delta_m(a) = \delta_m(g^{\operatorname{ind}_g a}) = \dfrac{\varphi(m)}{\gcd(\varphi(m),\operatorname{ind}_g a)}.
    $$
    
    We already know that the equation has a solution if and only if $d\mid \operatorname{ind}_g a$, that is, $\delta_m(a)\mid d'$. By [property 2 of the order](./primitive-root.md#幂的循环结构), this is equivalent to that criterion.

The case where the modulus is a power of $2$ is somewhat special. To handle this case, we need a [result](./primitive-root.md#递推公式) about the structure of the reduced residue system modulo $2^e$: every odd number $a$ is uniquely congruent to an integer of the form $(-1)^s5^r\bmod 2^e$, where $s\in\{0,1\}$ and $0\le r < 2^{e-2}$. With this result, we obtain the following conclusion:

???+ note "Theorem"
    Let $k\ge 2$ be an integer, $a$ an odd number, and $m=2^e$ a positive integer with $e \ge 2$. Then, when $k$ is odd:
    
    1.  $a$ is always a $k$-th residue modulo $m$.
    2.  $a$ has exactly one $k$-th root modulo $m$.
    3.  The number of classes of $k$-th residues modulo $m$ is $2^{e-1}$, and they are exactly all the reduced residue classes.
    
    When $k$ is even, denote $d=\gcd(k,2^{e-2})$ and $d'=\dfrac{2^{e-2}}{d}$; then:
    
    1.  $a$ is a $k$-th residue modulo $m$ if and only if $a\equiv 1\pmod 4$ and $a^{d'}\equiv 1\pmod m$.
    2.  When $a$ is a $k$-th residue modulo $m$, $a$ has, up to congruence, exactly $2d$ pairwise distinct $k$-th roots modulo $m$, and they have the form
    
        $$
        x \equiv \pm 5^{y_0 + id'} \pmod{2^e},~ 0 \le y_0 < d',~i = 0, 1,\cdots,d-1. 
        $$
    3.  The number of classes of $k$-th residues modulo $m$ is $d'$, and all of them together form the set
    
        $$
        \{5^{di}\bmod m : 0 \le i < d'\}.
        $$

??? note "Proof"
    Since $a\perp m$, we have $x\perp m$. Since $x$ and $a$ are both odd, by the result above we can write $a\equiv (-1)^s5^r\pmod{2^e}$ and $x\equiv(-1)^z5^{y}\pmod{2^e}$. Since the representation is unique, the congruence $x^k\equiv a\pmod{2^e}$ is equivalent to the system of [linear congruences](./linear-equation.md)
    
    $$
    \begin{aligned}
    kz &\equiv s \pmod{2},\\
    ky &\equiv r \pmod{2^{e-2}}.
    \end{aligned}
    $$
    
    Combined with the analysis of the solutions of linear congruences on that page, we obtain the structure of the solutions of the congruence $x^k\equiv a\pmod{2^e}$. Depending on the parity of $k$, there are two cases:
    
    -   When $k$ is odd, since $\gcd(k,2)=\gcd(k,2^{e-2})=1$, both linear congruences have solutions for all $s,r$, so the original congruence always has a solution for every odd $a$.
    -   When $k$ is even, the first equation has a solution if and only if $2\mid s$, and the second has a solution if and only if $d=\gcd(k,2^{e-2})\mid r$. Combining the two gives the form of all classes of $k$-th residues. By direct computation, the first condition is equivalent to $a\equiv 1\pmod 4$; repeating the analysis of the odd prime power case, the second condition is equivalent to $a^{d'}\equiv 1\pmod m$. Combining these two points gives the criterion in the theorem. The general solutions of the two linear congruences are also known:
    
        $$
        \begin{aligned}
        z &\equiv0,1\pmod 2, \\
        y &\equiv y_0 + id' \pmod{2^{e-2}},~ 0\le y_0 < d',~i=0,1,\cdots,d-1.
        \end{aligned}
        $$
    
        Combining them gives the general solution of the original equation.

This completely settles the problem of deciding $k$-th residues for different moduli. The Legendre symbol and the law of quadratic reciprocity from the theory of quadratic residues can also be generalized to higher-order residues, but this is not easy and requires concepts such as [cyclotomic fields](../algebra/field-theory.md#分圆域). In algebraic number theory, the law of quadratic reciprocity is ultimately generalized to the [Artin reciprocity law](https://en.wikipedia.org/wiki/Artin_reciprocity).

## Roots of unity

As a special case of $k$-th roots, this section discusses the concept of $k$-th (primitive) roots of unity. It can be seen as the counterpart, in the reduced residue system $\mathbf Z_m^*$ modulo $m$, of the concept of $k$-th [roots of unity](../complex.md#单位根) in the field of complex numbers $\mathbf C$. When the modulus $m$ is suitable, replacing the complex root $\omega_k$ by a $k$-th primitive root of unity modulo $m$ can speed up computations.

Similarly to the case of the complex numbers, we have the following definition:

???+ abstract "$k$-th root of unity modulo $m$"
    For a modulus $m$, a $k$-th root of the element $1$ is called a **$k$-th root of unity modulo $m$**. In particular, if $x$ is a $k$-th root of unity modulo $m$ and it is not a root of unity modulo $m$ of any order $k' < k$, then $x$ is also called a **$k$-th primitive root of unity modulo $m$**.

Comparing with the [definition of a primitive root](./primitive-root.md#原根), a primitive root $g$ is exactly a $\varphi(m)$-th primitive root of unity modulo $m$, where $\varphi(m)$ is [Euler's totient function](./euler-totient.md).

When a $k$-th primitive root of unity modulo $m$ exists, its algebraic properties coincide with those of the $k$-th primitive complex root of unity $\omega_k$, and it can replace $\omega_k$ in various computations. For example, applying it to the [fast Fourier transform](../poly/fft.md) yields the [number-theoretic transform](../poly/ntt.md) over a finite field[^fnnt].

### Properties

In the field of complex numbers, (primitive) roots of unity of every order exist. However, this is not the case for (primitive) roots of unity in number theory.

???+ note "Properties"
    For a modulus $m$, let $\lambda(m)$ be its [Carmichael function](./primitive-root.md#carmichael-函数). Then:
    
    1.  Every integer $a$ coprime to $m$ is a $\delta_m(a)$-th primitive root of unity modulo $m$, where $\delta_m(a)$ is the [order](./primitive-root.md#阶) of $a$ modulo $m$.
    2.  If the element $a$ is a $k$-th root of unity modulo $m$ and $k'$ is any multiple of $k$, then $a$ is also a $k'$-th root of unity modulo $m$.
    3.  If the element $a$ is a $k$-th (primitive) root of unity modulo $m$, then the element $a^{\ell}$ is a $\dfrac{k}{\gcd(k,\ell)}$-th (correspondingly, primitive) root of unity modulo $m$.
    4.  As $k'$ ranges over the divisors of $k$, all $k'$-th primitive roots of unity modulo $m$ form exactly a partition of the $k$-th roots of unity modulo $m$. Moreover, for $\ell\perp k$, the map $x\mapsto x^\ell$ gives a bijection among the $k$-th roots of unity that preserves this partition: it maps primitive roots of unity of order $k'\mid k$ again to $k'$-th primitive roots of unity.
    5.  A $k$-th primitive root of unity modulo $m$ exists if and only if $k\mid\lambda(m)$. In particular, a $\lambda(m)$-th primitive root of unity modulo $m$ exists, and it is called a **$\lambda$‑primitive root modulo $m$**.
    6.  The element $a$ is a $k$-th primitive root of unity modulo $m$ if and only if $a^k\equiv 1\pmod{m}$ and for every prime factor $p\mid k$ we have $a^{k/p}\not\equiv 1\pmod{m}$.

??? note "Proof"
    By the definition of the order, every integer $a$ coprime to $m$ is a $\delta_m(a)$-th primitive root of unity modulo $m$, where $\delta_m(a)$ is the order of $a$ modulo $m$. Conversely, if $a$ is a $k$-th root of unity modulo $m$, then $\gcd(a^k,m)=1$, so $\gcd(a,m)=1$. Therefore, $a$ is a (primitive) root of unity modulo $m$ if and only if $a$ is coprime to $m$. This is property 1.
    
    Checking the definition directly, as long as $k\mid k'$, we can deduce $a^{k'}\equiv 1\pmod m$ from $a^k\equiv 1\pmod m$; this is property 2. By the [properties of the order](./primitive-root.md#幂的循环结构), we have
    
    $$
    \delta_m(a^\ell) = \dfrac{\delta_m(a)}{\gcd(\delta_m(a),\ell)}.
    $$
    
    If $a$ is a $k$-th primitive root of unity modulo $m$, then $\delta_m(a)=k$, and substituting directly into the formula above gives that $a^\ell$ is a $\dfrac{k}{\gcd(k,\ell)}$-th primitive root of unity modulo $m$. If $a$ is only a $k$-th root of unity modulo $m$, suppose it is a primitive root of unity of order $k'\mid k$; then $a^\ell$ is a $\dfrac{k'}{\gcd(k',\ell)}$-th primitive root of unity modulo $m$. Since $k'\mid k$, we have
    
    $$
    \dfrac{k'}{\gcd(k',\ell)} \mid \dfrac{k}{\gcd(k,\ell)},
    $$
    
    and then by property 2, $a^\ell$ is a $\dfrac{k}{\gcd(k,\ell)}$-th root of unity modulo $m$. This is property 3.
    
    For $k'\mid k$, by property 2, a $k'$-th primitive root of unity modulo $m$ is necessarily a $k$-th root of unity modulo $m$; conversely, every $k$-th root of unity $a$ modulo $m$ is a $\delta_m(a)$-th primitive root of unity, with $\delta_m(a)\mid k$. These sets are pairwise disjoint, so they form a partition. Moreover, for $\ell\perp k$ we always have $\ell\perp k'$, so for a $k'$-th primitive root of unity $a$ modulo $m$, $a^\ell$ is always a $k'$-th primitive root of unity modulo $m$. Taking $\ell'=\ell^{-1}\bmod k$, one can verify that $x\mapsto x^\ell$ and $x\mapsto x^{\ell'}$ are mutually inverse maps, so $x\mapsto x^\ell$ is a bijection. This is property 4.
    
    By the properties of the Carmichael function, a $\lambda(m)$-th primitive root of unity modulo $m$ always exists; let it be $a$, so that $\delta_m(a)=\lambda(m)$. For $k\mid\lambda(m)$, let $k'=\dfrac{\lambda(m)}{k}$; we always have
    
    $$
    \delta_m(a^{k'}) = \dfrac{\lambda(m)}{\gcd(\lambda(m),k')} = \dfrac{\lambda(m)}{k'} = k.
    $$
    
    Therefore, $a^{k'}$ is a $k$-th primitive root of unity. On the other hand, by the definition of the Carmichael function, the order of every $x\perp m$ is a divisor of $\lambda(m)$. This gives property 5.
    
    Almost repeating the proof of the [primitive root criterion](./primitive-root.md#原根判定定理) gives property 6. This criterion actually verifies $\delta_m(a)=k$.

From these properties we can see that, compared to the case where a primitive root exists, the $\lambda$‑primitive root modulo $m$ plays a similar fundamental role. Unlike a primitive root, the powers of a $\lambda$‑primitive root cannot be used to generate all roots of unity modulo $m$. Nevertheless, since the density of $\lambda$‑primitive roots is not low[^lambda-density], if we really need to find a $k$-th primitive root of unity, we can first find a $\lambda$‑primitive root by random sampling, and then obtain a $k$-th primitive root of unity by taking a power.

If one $k$-th root of $a$ modulo $m$ is known, all $k$-th roots of $a$ modulo $m$ can be generated from all $k$-th roots of unity modulo $m$.

???+ note "Theorem"
    Let $x$ be a $k$-th root of $a$ modulo $m$. As $r$ ranges over all $k$-th roots of unity modulo $m$, $xr$ ranges over all $k$-th roots of $a$ modulo $m$.

??? note "Proof"
    For two $k$-th roots $x,y$ of $a$ modulo $m$, let $r=x^{-1}y\bmod m$; then $r$ satisfies $r^k\equiv 1\pmod m$, so it is a $k$-th root of unity modulo $m$. Conversely, as long as $r$ is a $k$-th root of unity modulo $m$, we have $(xr)^{k}= x^kr^k\equiv a\pmod m$, that is, $xr$ is a $k$-th root of $a$ modulo $m$.

Generating all $k$-th roots from the $k$-th roots of unity is similar to generating the general solution of a non-homogeneous system of linear equations from the solutions of the homogeneous system.

The discussion above concerns the general case. Only in the case where a primitive root exists is the structure of the roots of unity simpler:

???+ note "Theorem"
    For a modulus $m$, suppose a primitive root modulo $m$ exists, and let $a$ be a $k$-th primitive root of unity modulo $m$. Then $b$ is a $k$-th root of unity modulo $m$ if and only if it can be expressed as a power of $a$.

??? note "Proof"
    Let $g$ be a primitive root modulo $m$; then every element coprime to $m$ can be expressed as a power of $g$. Then $a$ is a $k$-th primitive root of unity modulo $m$ if and only if
    
    $$
    \delta_m(a) = \delta_m(g^{\operatorname{ind}_ga}) = \dfrac{\varphi(m)}{\gcd(\varphi(m),\operatorname{ind}_ga)} = k.
    $$
    
    Similarly, $b$ is a $k$-th root of unity modulo $m$ if and only if
    
    $$
    \delta_m(b) = \delta_m(g^{\operatorname{ind}_gb}) = \dfrac{\varphi(m)}{\gcd(\varphi(m),\operatorname{ind}_gb)} = k' \mid k.
    $$
    
    Therefore, we have
    
    $$
    \gcd(\varphi(m),\operatorname{ind}_ga) \mid \gcd(\varphi(m),\operatorname{ind}_gb)\mid \operatorname{ind}_gb.
    $$
    
    By the [analysis](./linear-equation.md) of linear congruences, this condition is equivalent to the equation
    
    $$
    (\operatorname{ind}_ga) x \equiv \operatorname{ind}_gb \pmod{\varphi(m)}
    $$
    
    having a solution. Raising $g$ to the powers in this condition, we get $a^x\equiv b\pmod{m}$, that is, $b$ can be expressed as a power of $a$.

This theorem shows that, when a primitive root exists, all $k$-th roots of unity have the structure of a [cyclic group](../algebra/group-theory.md#循环群), and the $k$-th primitive roots of unity are the generators of this cyclic group. We will see later that the Tonelli–Shanks algorithm exploits exactly this point to speed up the discrete logarithm part of root extraction.

## Root extraction in modular arithmetic

Finally, this article discusses how to compute $k$-th roots. For the case $k=2$, there are [many efficient algorithms](./quad-residue.md#模意义下开平方) for taking square roots modulo an integer. For general $k$, however, no polynomial-time algorithm is known. This section introduces two common algorithms, which find a $k$-th root in $O(m^{1/2})$ and $O(m^{1/4+\varepsilon})$ time, respectively. Using the Chinese remainder theorem, the problem can always be converted to the case of a prime-power modulus, so this section mainly discusses the solution for prime-power moduli.

### Naive algorithm

The earlier [analysis](#properties) of the properties of $k$-th residues has in fact already pointed out a method for computing $k$-th roots modulo a prime power. Strictly speaking, the case solved earlier is the one where the radicand $a$ and the modulus $m$ are coprime. The algorithm is summarized as follows:

-   When $m=p^e$ is an odd prime power, let $g$ be a primitive root modulo $m$. Then the equation $x^k\equiv a\pmod m$ can be converted to the linear congruence

    $$
    ky \equiv \operatorname{ind}_g a \pmod{\varphi(m)}.
    $$

    Here, $\operatorname{ind}_g a$ can be computed with the [BSGS algorithm](./discrete-logarithm.md#大步小步算法), and all solutions of the [linear congruence](./linear-equation.md) are easy to find. From this, we obtain all $k$-th roots $x\equiv g^y\pmod m$ of $a$.

    Besides this, there is another similar approach. Again letting $x\equiv g^y\pmod m$, we can transform

    $$
    x^k \equiv (g^k)^y \equiv a \pmod m
    $$

    into computing the discrete logarithm of $a$ with base $g^k$. This can likewise be solved with the BSGS algorithm to find a particular solution. The general solution can be obtained from the expression for the solutions given earlier, that is, by multiplying the particular solution by each of the $k$-th roots of unity in turn.

    Whichever approach is used, when the primitive root is known, the complexity of finding a single solution with this algorithm is $O(m^{1/2})$. Since a primitive root can be found in $o(m^{1/2})$ time, the total time complexity is still $O(m^{1/2})$.

-   When $m=2^e$ with $e\in\mathbf N_+$, we can first find $s,r$ in $a\equiv (-1)^s5^r\pmod m$. Of these two exponents, $s$ can be determined in $O(1)$ time:

    $$
    s = \begin{cases}0, & a\equiv 1\pmod 4, \\ 1, & a\equiv 3\pmod 4.\end{cases}
    $$

    And $r=\operatorname{ind}_5((-1)^sa)$ can be computed with the BSGS algorithm in $O(m^{1/2})$ time. Next, we only need to solve the system of linear congruences:

    $$
    \begin{aligned}
    kz &\equiv s \pmod{2},\\
    ky &\equiv r \pmod{2^{e-2}}.
    \end{aligned}
    $$

    The general solution $(z,y)$ of this system of linear congruences is easy to find, and $x=(-1)^z5^y$ is the required root. The complexity of finding a single solution with this algorithm is again $O(m^{1/2})$.

Of course, the case with no solution can in fact be quickly detected in $O(\log m)$ time using the criterion described earlier, without needing to check during the solving process.

A reference implementation for computing $k$-th roots modulo a prime is as follows: (the code is only for illustration; because its time complexity is too high, it cannot pass this problem)

??? example "Reference implementation for the template problem [Library Checker - Kth Root (Mod)](https://judge.yosupo.jp/problem/kth_root_mod)"
    ```cpp
    --8<-- "docs/math/code/residue/bsgs-mod-p.cpp"
    ```

### Improved Tonelli–Shanks algorithm

By suitably generalizing the [Tonelli–Shanks algorithm](./quad-residue.md#tonellishanks-算法) for taking square roots modulo an integer, root extraction modulo a prime power can be solved. A relatively direct way of generalizing is the Adleman–Manders–Miller algorithm[^amm], but its complexity is still not good enough[^amm-comp]. This section introduces the improved Tonelli–Shanks algorithm proposed by sugarknri, Min\_25, 37zigen and others. It can find a $k$-th root in $O(m^{1/4+\varepsilon})$ time.

The core idea of the Tonelli–Shanks algorithm is to move the computation of the discrete logarithm into a group of order $2^e$, thereby reducing the time complexity. Similarly, the discrete logarithm in a group of order an arbitrary prime power $p^e$ can also be computed fairly efficiently, but the complexity of the algorithm is $\Omega\left(\sqrt{p}\right)$. The Adleman–Manders–Miller algorithm splits the computation of a $k$-th root into several computations of discrete logarithms in groups of prime-power order, but it is limited by the size of the largest prime factor $p_\text{max}(k)$ of $k$, so the complexity of the algorithm is still $\Omega\left(\sqrt{p_\text{max}(k)}\right)$. The algorithm in this section further improves this process by avoiding the computation of discrete logarithms for larger prime factors, thereby bringing the overall complexity down to $O(m^{1/4+\varepsilon})$.

#### Procedure

Consider computing a $k$-th root of $a$ modulo a prime power $m$, i.e. solving the congruence:

$$
x^k \equiv a \pmod m.
$$

In particular, for the case $m=2^e$, we also need to ensure $a\equiv 1\pmod{4}$, so that $a$ can be written as a power of $g=5$. Similarly to the earlier discussion, the computation of $k$-th roots modulo $2^e$ can always be converted to such a case. When handling the case modulo $2^e$, every $\varphi(m)$ mentioned in this section should be replaced by $\delta_m(5)=2^{e-2}$.

First, the problem can be converted to the case where the order of the root divides $\varphi(m)$. Let $d=\gcd(k,\varphi(m))$. Then, by the properties of $k$-th residues, when $a$ is a $k$-th residue modulo $m$, $a$ is always a $\dfrac{\varphi(m)}{d}$-th root of unity modulo $m$. By the properties of roots of unity, for any $\ell\perp\dfrac{\varphi(m)}{d}$, the map $x\mapsto x^{\ell}$ is a bijection among the $\dfrac{\varphi(m)}{d}$-th roots of unity. Therefore, we can take

$$
\ell = \left(\dfrac{k}{d}\right)^{-1}\bmod\dfrac{\varphi(m)}{d}.
$$

Raising both sides of the original congruence to the $\ell$-th power, we get

$$
x^d\equiv x^{k\ell} \equiv a^{\ell} =: b \pmod{m}.
$$

The leftmost congruence uses [Euler's theorem](./fermat.md#欧拉定理) and the following congruence relation: ($c\in\mathbf Z$)

$$
k\ell = d\left(\frac{k}{d}\ell\right) = d\left(c\dfrac{\varphi(m)}{d}+1\right) \equiv d \pmod{\varphi(m)}.
$$

For the transformed problem, consider the prime factorization of $d$:

$$
d = \prod_{p\in\mathbf P}p^e.
$$

Starting from $b=a^\ell$, for each $p^e\neq 1$ we take a $p^e$-th root in turn, and in the end we obtain a $d$-th root of $b$, that is, a $k$-th root of $a$.

Finally, the problem is reduced to finding a solution of the following equation:

$$
x^{p^e} \equiv b \pmod m.
$$

Without loss of generality, let $\varphi(m)=p^sr$ with $p\perp r$. Let $q\in\mathbf N_+$ be a solution of the equation $qr\equiv -1\pmod{p^e}$. Then, since $b$ is an $rp^{s-e}$-th root of unity, $b^{qr}$ must be a $p^{s-e}$-th root of unity. Further, let $\zeta$ be a $p^s$-th primitive root of unity modulo $m$. Then $\zeta^{p^e}$ is a $p^{s-e}$-th primitive root of unity, and hence there exists $h\in\mathbf N$ such that $b^{qr}\equiv \zeta^{hp^{e}}\pmod{m}$. Therefore, by direct verification,

$$
x\equiv b^{(qr+1)/p^e}\zeta^{-h} \pmod{m}
$$

is a $p^e$-th root of $b$ modulo $m$.

To compute $x$, we need to find a $p$-th nonresidue $\eta$ modulo $m$. For this, by the properties above, it suffices to pick $\eta\perp m$ at random and verify $\eta^{\varphi(m)/p}\bmod{m}\neq 1$. The density of such numbers is

$$
\dfrac{\varphi(m)}{m}\left(1-\dfrac{1}{p}\right) \ge \dfrac{1}{4}.
$$

Therefore, in expectation, picking at most $4$ random integers suffices to find one. Note that $\eta^{rp^{s-1}}\not\equiv 1\pmod m$ and $\eta^{rp^s}\equiv 1\pmod m$, so if we set $\zeta=\eta^r\bmod m$ and $\xi=\eta^{rp^{s-1}}\bmod m$, they are a $p^s$-th and a $p$-th primitive root of unity, respectively.

Finally, we need to compute $h\in\mathbf N$. Clearly, we can take $h < p^{s-e}$. Consider the base-$p$ representation of $h$:

$$
h = \sum_{j=0}^{s-e-1}h_jp^j = h_0 + h_1p + h_2p^2 +\cdots.
$$

We compute these digits one by one. When the first $j$ digits have been computed, we necessarily have

$$
\left(b^{qr}\zeta^{-p^e(h_0+h_1p+\cdots + h_{j-1}p^{j-1})}\right)^{p^{s-e-j-1}} \equiv \zeta^{h_jp^{s-1}} \equiv \xi^{h_j} \pmod{m}.
$$

Hence, $h_j$ can be obtained by computing a discrete logarithm with respect to $\xi$. To obtain a better time complexity, the BSGS algorithm should be used. In total, $(s-e)$ discrete logarithms need to be computed; if we precompute $B$ powers of $\xi$, the time complexity of a single discrete logarithm computation is $O(p/B)$, and the total time complexity is

$$
O\left(B+(s-e)\dfrac{p}{B}\right).
$$

When $B=\sqrt{(s-e)p}$, the total time complexity is minimized, at $O\left(\sqrt{(s-e)p}\right)$. After obtaining $h$, substituting it into the expression for $x$ above gives a particular solution.

#### Time complexity

The time complexity of this algorithm is $O(m^{1/4+\varepsilon})$. When discussing complexity in this section, we always assume that a single multiplication takes $O(1)$ time, and that when computing powers, Euler's theorem is always applied to reduce the exponent, so each individual power involved can always be computed in $O(\log m)$ time.

First consider the computation of a single $p^e$-th root. Finding a $p$-th nonresidue only requires checking $O(1)$ numbers in expectation, for a total time complexity of $O(\log m)$. Computing each of $s,r,\zeta,\eta,b^{qr}$ takes only $O(\log m)$ time. When computing $h$, each digit requires $O(\log m)$ time to compute powers, and there are $(s-e)$ digits in total, so the total time complexity is $O((s-e)\log m)$. As explained above, the preprocessing and the $(s-e)$ queries of the discrete logarithm part take $O\left(\sqrt{(s-e)p}\right)$ time in total. Since $s-e\in O(\log m)$, the time complexity of computing a single $p^e$-th root is $O(p^{1/2+\varepsilon})$. In particular, when $s=e$, the time complexity can be further reduced to $O(\log m)$.

We can now consider the total time complexity of the algorithm. The time complexities of computing $\varphi(m),d,\ell$ are all $O(\log m)$. Next, the prime factorization $d=\prod_p{p^e}$ needs to be done; this step can be completed in $O(m^{1/4})$ time using the [Pollard's rho algorithm](./pollard-rho.md#pollard-rho-算法). Finally, the total time complexity of computing the $p^e$-th roots in turn is

$$
O\left(\sum_{e < s}p^{1/2+\varepsilon}\right).
$$

Since a prime factor $p$ satisfying $e < s$ appears at least $2$ times in $\varphi(m)$, we necessarily have $p < m^{1/2}$. Hence, the total time complexity is $O(m^{1/4+\varepsilon})$.

In fact, in this scenario, there is no need to use Pollard's rho algorithm for the prime factorization, and a time complexity of $O(m^{1/4+\varepsilon})$ can still be achieved. Specifically, it suffices to factor $d$ by brute-force trial division, enumerating only prime factors not exceeding $m^{1/4}$. Let $z$ be the integer obtained after removing these small prime factors. Then, for a prime factor $p > m^{1/4}$ of $z$, we necessarily have $\nu_p(\varphi(m)) < 4$, where $\nu_p(n)$ denotes the exponent of $p$ in the prime factorization of $n$. Since we only need to consider the case

$$
1 \le e = \nu_p(d) < s = \nu_p(\varphi(m)) < 4
$$

there can be at most one prime factor $p$ satisfying this condition; otherwise, their exponents in $\varphi(m)$ would all be at least $2$, and the total product would necessarily exceed $m$. To separate out this (possibly existing) unique large prime factor, it suffices to compute

$$
p^\star=\gcd\left(z,\dfrac{\varphi(m)}{z}\right) = \prod_{p\mid z,~\nu_p(d) < \nu_p(\varphi(m))}p^{\min\{\nu_p(d),\nu_p(\varphi(m))-\nu_p(d)\}}.
$$

Enumerating all possibilities for $\nu_p(d),\nu_p(\varphi(m))$ shows that the exponent of $p$ in the product is necessarily $1$, so the value computed this way is exactly the unique large prime factor $p^\star$ (if it exists). As for the remaining part $z/p^\star$, since it can only contain prime factors satisfying $e=s$, there is no need to factor it further.

A reference implementation for computing $k$-th roots modulo a prime is as follows:

??? example "Reference implementation for the template problem [Library Checker - Kth Root (Mod)](https://judge.yosupo.jp/problem/kth_root_mod)"
    ```cpp
    --8<-- "docs/math/code/residue/tonelli-shanks-mod-p.cpp"
    ```

### Handling the general case

Consider the general case: the modulus $m$ is still a prime power $p^e$, but $\gcd(a,m)>1$. If $a\equiv 0\pmod{m}$, then

$$
x \equiv p^{\lceil e/k \rceil}\ell\pmod{p^e},~\ell=0,1,\cdots,p^{e-\lceil e/k\rceil}-1
$$

are all solutions of the original equation. Next, consider the case $a\not\equiv 0\pmod{m}$. Let $a = p^sa'$ with $p\perp a'$. Then, setting $x=p^zx'$ with $p\perp x'$, we have

$$
x^k = p^{kz}(x')^k\equiv p^sa'\pmod{p^e}.
$$

Since $(x')^k\perp p$, this holds if and only if $kz = s$ and $(x')^k\equiv a'\pmod{p^{e-s}}$. The first equation has the solution $z=\dfrac{s}{k}$ if and only if $k\mid s$; and solving the second equation has already been settled. Note that since the modulus of the general solution of the second equation differs from the modulus of the general solution of the original equation, each solution $x'$ of the second equation corresponds to several solutions of the original equation:

$$
x \equiv p^{s/k}(x' + \ell p^{e-s})\pmod{p^e},~\ell = 0,1,\cdots, p^{s-s/k}-1.
$$

A reference implementation for finding all $k$-th roots modulo an arbitrary modulus is as follows:

??? example "Reference code for the template problem [Luogu P5668【模板】N 次剩余 (Template: N-th residue)](https://www.luogu.com.cn/problem/P5668)"
    === "Naive algorithm"
        ```cpp
        --8<-- "docs/math/code/residue/bsgs.cpp"
        ```
    
    === "Improved Tonelli–Shanks algorithm"
        ```cpp
        --8<-- "docs/math/code/residue/tonelli-shanks.cpp"
        ```

## References and notes

-   冯克勤．初等数论及其应用．(Feng Keqin. Elementary Number Theory and Its Applications.)
-   [Root of unity modulo n - Wikipedia](https://en.wikipedia.org/wiki/Root_of_unity_modulo_n)
-   [No.981 一般冪乗根 解説 by 37zigen (General power roots, editorial)](https://yukicoder.me/problems/no/981/editorial)

[^fnnt]: In fact, the modulus $m$ need not be prime. As long as $a$ is a $k=2^e$-th primitive root of unity modulo $m$, it can be used for the number-theoretic transform modulo $m$. However, since the $2^e$ that usually needs to be handled is fairly large, this means that every prime factor of the modulus $m$ is of the form $c2^e+1$. Therefore, a single prime factor is already large, and the modulus $m$ is usually even larger, so the case of a general modulus is not as commonly used as the case of a prime modulus.

[^lambda-density]: By the [result on the number of primitive roots](./primitive-root.md#原根个数), the number of $\lambda$‑primitive roots is exactly $\varphi(\lambda(m))$, where $\varphi(\cdot)$ and $\lambda(\cdot)$ are Euler's totient function and the Carmichael function, respectively. Since for almost all integers $m$ we have $\lambda(m)/m = \exp(-(1+o(1))\log\log m\log\log\log m)$, and there exists $C > 0$ such that for integers $m > 2$ we have $\varphi(m)/m \ge C / \log\log m$, for almost all integers $m$ we have $\varphi(\lambda(m))/m = \exp(-(1+o(1))\log\log m\log\log\log m)$. Here, the $o(1)$ in the coefficient of the exponent absorbs the contribution of the factor $\varphi(\lambda(m))/\lambda(m)$. Hence, a $\lambda$‑primitive root can be found within $\exp((1+o(1))\log\log m\log\log\log m)$ trials in expectation. For the estimate of Euler's totient function, see the paper Rosser, J. Barkley, and Lowell Schoenfeld. "Approximate formulas for some functions of prime numbers." Illinois Journal of Mathematics 6, no. 1 (1962): 64-94. For the estimate of the Carmichael function, see the paper Erdos, Paul, Carl Pomerance, and Eric Schmutz. "Carmichael’s lambda function." Acta Arith 58, no. 4 (1991): 363-385.

[^amm]: For the original paper, see Adleman, Leonard, Kenneth Manders, and Gary Miller. "On taking roots in finite fields." In 18th Annual Symposium on Foundations of Computer Science (sfcs 1977), pp. 175-178. IEEE Computer Society, 1977. A more readable introduction can be found in Cao, Zhengjun, Qian Sha, and Xiao Fan. "Adleman-Manders-Miller root extraction method revisited." In International Conference on Information Security and Cryptology, pp. 77-85. Berlin, Heidelberg: Springer Berlin Heidelberg, 2011.

[^amm-comp]: Since this algorithm requires $k$ to be prime, in the worst case it needs to compute a $p$-th root of $a$ modulo $m$ for the largest prime factor $p$ of $\varphi(m)$. In this process, the discrete logarithm of $a$ modulo $m$ with respect to a $p$-th primitive root of unity needs to be computed. Even with the BSGS algorithm, this process takes $O(\sqrt{p})$ time. However, the paper Fouvry, Étienne. "Theoreme de Brun-Titchmarsh; application au theoreme de Fermat." Inventiones mathematicae 79, no. 2 (1985): 383-407 shows that there is a set of primes $m$ of positive density for which the largest prime factor of $\varphi(m)=m-1$ is $p=\Omega(m^{2/3})$. This means that the complexity of this algorithm is at least $\Omega(m^{1/3})$, which is worse than the improved Tonelli–Shanks algorithm introduced in the text.
