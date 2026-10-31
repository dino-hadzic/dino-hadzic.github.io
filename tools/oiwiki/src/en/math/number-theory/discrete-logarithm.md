---
title: Discrete logarithm
---

## Definition

Prerequisites: [Multiplicative order and primitive roots](./primitive-root.md).

The discrete logarithm is defined similarly to the logarithm. Take a positive integer modulus $m$ that has a primitive root, and let $g$ be one of its primitive roots. For an integer $a$ with $(a,m)=1$, we know that there must exist a unique integer $0\leq k<\varphi(m)$ such that

$$
g^k\equiv a\pmod m
$$

We call this $k$ the discrete logarithm to the base $g$ modulo $m$, written $k=\operatorname{ind}_g a$; when there is no risk of confusion, it may be written $\operatorname{ind} a$.

Clearly $\operatorname{ind}_g 1=0$, $\operatorname{ind}_g g=1$.

## Properties

The properties of the discrete logarithm also resemble those of the logarithm in many ways.

???+ note "Properties"
    Let $g$ be a primitive root modulo $m$ and $(a,m)=(b,m)=1$. Then:
    
    1.  $\operatorname{ind}_g(ab)\equiv\operatorname{ind}_g a+\operatorname{ind}_g b\pmod{\varphi(m)}$
    
        Furthermore, $(\forall n\in\mathbf{N}),~~\operatorname{ind}_g a^n\equiv n\operatorname{ind}_g a\pmod{\varphi(m)}$
    2.  If $g_1$ is also a primitive root modulo $m$, then $\operatorname{ind}_g a\equiv\operatorname{ind}_{g_1}a \cdot \operatorname{ind}_g g_1\pmod{\varphi(m)}$
    3.  $a\equiv b\pmod m\iff \operatorname{ind}_g a=\operatorname{ind}_g b$

???+ note "Proof"
    1.  $g^{\operatorname{ind}_g(ab)}\equiv ab\equiv g^{\operatorname{ind}_g a}g^{\operatorname{ind}_g b}\equiv g^{\operatorname{ind}_g a+\operatorname{ind}_g b}\pmod m$
    2.  Let $x=\operatorname{ind}_{g_1}a$; then $a\equiv g_1^x\pmod m$. Also let $y=\operatorname{ind}_g g_1$; then $g_1\equiv g^y\pmod m$.
    
        Hence $a\equiv g^{xy}\pmod m$, i.e. $\operatorname{ind}_g a\equiv xy\equiv\operatorname{ind}_{g_1}a \cdot \operatorname{ind}_g g_1\pmod{\varphi(m)}$
    3.  Note that
    
        $$
        \begin{aligned}
            \operatorname{ind}_g a=\operatorname{ind}_g b&\iff \operatorname{ind}_g a\equiv\operatorname{ind}_g b\pmod{\varphi(m)}\\
            &\iff g^{\operatorname{ind}_g a}\equiv g^{\operatorname{ind}_g b}\pmod m\\
            &\iff a\equiv b\pmod m
        \end{aligned}
        $$

## Baby-step giant-step algorithm

At present there is still no polynomial-time classical algorithm for the discrete logarithm problem (the input size of the discrete logarithm problem is the number of bits of the input data). In cryptography, many asymmetric encryption schemes have been designed based on this fact, such as [Ed25519](https://en.wikipedia.org/wiki/EdDSA#Ed25519).

In competitive programming, BSGS (baby-step giant-step) is commonly used to solve the discrete logarithm problem. Formally, for $a,b,m\in\mathbf{Z}^+$, the algorithm solves

$$
a^x \equiv b \pmod m
$$

in $O(\sqrt{m})$ time, where $a\perp m$. The solution $x$ of the equation satisfies $0 \le x < m$. (Note that $m$ is not necessarily prime.)

### Algorithm description

Let $x = A \left \lceil \sqrt m \right \rceil - B$, where $0\le A,B \le \left \lceil \sqrt m \right \rceil$. Then $a^{A\left \lceil \sqrt m \right \rceil -B} \equiv b \pmod m$, and after a small rearrangement, $a^{A\left \lceil \sqrt m \right \rceil} \equiv ba^B \pmod m$.

We know $a,b$, so we can first compute all values of $ba^B$ on the right-hand side by enumerating $B$ and store them in a `hash`/`map`; then we compute $a^{A\left \lceil \sqrt m \right \rceil}$ one by one, enumerating $A$, and look for an equal $ba^B$; in this way we obtain all $x$, $x=A \left \lceil \sqrt m \right \rceil - B$.

Note that $A,B$ are both less than $\left \lceil \sqrt m \right \rceil$, so the time complexity is $\Theta\left  (\sqrt m\right )$; using a `map` adds an extra $\log$ factor.

??? note "Why $a$ and $m$ must be coprime"
    Note that what we actually find are $A,B$, and we need to make sure that from $a^{A\left \lceil \sqrt m \right \rceil} \equiv ba^B \pmod m$ we can go back to $a^{A\left \lceil \sqrt m \right \rceil -B} \equiv b \pmod m$. The latter is obtained from the former by dividing both sides by $a^B$, so we must have $a^B \perp m$, i.e. $a\perp m$.

## Extended BSGS algorithm

For $a,b,m\in\mathbf{Z}^+$, solve

$$
a^x\equiv b\pmod m
$$

where $a,m$ are not necessarily coprime.

When $(a, m)=1$, $a$ has an inverse modulo $m$, so the BSGS algorithm can be used. So we try to make them coprime.

Specifically, let $d_1=(a, m)$. If $d_1\nmid b$, the original equation has no solution. Otherwise we divide the equation by $d_1$ and get

$$
\frac{a}{d_1}\cdot a^{x-1}\equiv \frac{b}{d_1}\pmod{\frac{m}{d_1}}
$$

If $a$ and $\frac{m}{d_1}$ are still not coprime, we divide again: let $d_2=\left(a, \frac{m}{d_1}\right)$. If $d_2\nmid \frac{b}{d_1}$, the equation has no solution; otherwise we divide by $d_2$ and get

$$
\frac{a^2}{d_1d_2}\cdot a^{x-2}≡\frac{b}{d_1d_2} \pmod{\frac{m}{d_1d_2}}
$$

Similarly, we keep checking in this way until $a\perp \dfrac{m}{d_1d_2\cdots d_k}$.

Let $D=\prod_{i=1}^kd_i$; the equation then becomes:

$$
\frac{a^k}{D}\cdot a^{x-k}\equiv\frac{b}{D} \pmod{\frac{m}{D}}
$$

Since $a\perp\dfrac{m}{D}$, it follows that $\dfrac{a^k}{D}\perp \dfrac{m}{D}$. So $\dfrac{a^k}{D}$ has an inverse, and we move it to the right-hand side of the equation, which gives an ordinary BSGS problem; solving for $x-k$ and adding $k$ gives the solution of the original equation.

Note that a solution less than or equal to $k$ is not ruled out, so before removing the factors we do a $\Theta(k)$ enumeration and directly check $a^i\equiv b \pmod m$; this avoids that case.

## Fast discrete logarithm with value-range preprocessing

The BSGS algorithm above has a time complexity of $O(\sqrt m)$ per query, which is inefficient when the number of queries is large. If the modulus of every query is the same fixed prime $p$, we have a fast algorithm based on preprocessing over the value range.

We already know that $\operatorname{ind}_g(ab)\equiv\operatorname{ind}_g a+\operatorname{ind}_g b\pmod{p-1}$, so we can compute discrete logarithms with the BSGS algorithm only for primes, and the discrete logarithm of a composite number can be converted by this formula into a sum of several already known discrete logarithms of primes. The complexity is still not good at this point, so we consider preprocessing only part of the discrete logarithms; specifically, we preprocess the discrete logarithms from $1$ to $L = \lfloor\sqrt p\rfloor + 1$. Note that the BSGS block length $B$ **cannot** be $O(\sqrt{L})$ here, because the preprocessing part of BSGS (inserting into the hash table) has complexity $O(B)$, while a total of $O(\pi(L))$ queries are needed, so the total time complexity is $O\left(B+\dfrac{\pi(L)p}{B}\right)$, and only $B=O(\sqrt{\pi(L)p})$ is optimal. By the [prime number theorem](./prime.md) $\pi(n)\sim\dfrac{n}{\log n}$, so the total preprocessing time complexity can be balanced to $O\left(\dfrac{p^{3/4}}{\log^{1/2} p}\right)$.

Next, how to compute the answer. Suppose we currently want $\operatorname{ind}_g y$. If $y\le L$, we return it directly; otherwise let $p=vy+r$, so $v=\left\lfloor\dfrac{p}{y}\right\rfloor<L$, $r=p\bmod y$, $y=\dfrac{p-r}{v}$, and therefore

$$
\begin{aligned}
\operatorname{ind}_g y &\equiv \operatorname{ind}_g (p-r)-\operatorname{ind}_g v\\
&\equiv \operatorname{ind}_g (-r)-\operatorname{ind}_g v\\
&\equiv \operatorname{ind}_g (p-1)+\operatorname{ind}_g r-\operatorname{ind}_g v \pmod{p-1}.
\end{aligned}
$$

Note that $\operatorname{ind}_g (p-1)=(p-1)/2$, so it suffices to recursively compute the discrete logarithm of $r$.

We can also consider another expression for $y$: note that $p=vy+r=(v+1)y+r-y$, so $y=\dfrac{p-r+y}{v+1}$, and therefore

$$
\operatorname{ind}_g y\equiv \operatorname{ind}_g (y-r)-\operatorname{ind}_g (v+1) \pmod{p-1}.
$$

We have $v+1 \le L$, so it suffices to recursively compute the discrete logarithm of $y-r$.

Combining these two ways of computing, we have $\min\{r,y-r\}\le \dfrac{y}{2}$, so recursing on the smaller one achieves a query complexity of $O(\log p)$.

Thus we have obtained an algorithm with time complexity $O\left(\dfrac{p^{3/4}}{\log^{1/2} p}\right)-O(\log p)$.

??? example "[Luogu11175【模板】基于值域预处理的快速离散对数 (Template: fast discrete logarithm with value-range preprocessing)](https://www.luogu.com.cn/problem/P11175)"
    ```cpp
    --8<-- "docs/math/code/discrete-logarithm/discrete-logarithm-1.cpp"
    ```

## Exercises

-   [SPOJ MOD](https://www.spoj.com/problems/MOD/) template
-   [SDOI2013 随机数生成器 (Random Number Generator)](https://www.luogu.com.cn/problem/P3306)
-   [SGU261 Discrete Roots](https://codeforces.com/problemsets/acmsguru/problem/99999/261) template
-   [SDOI2011 计算器 (Calculator)](https://loj.ac/problem/10214) template
-   [Luogu4195【模板】exBSGS/Spoj3105 Mod](https://www.luogu.com.cn/problem/P4195) template
-   [Codeforces - Lunar New Year and a Recursive Sequence](https://codeforces.com/contest/1106/problem/F)
-   [LOJ6542 离散对数 (Discrete Logarithm)](https://loj.ac/problem/6542) index calculus method, not a template

**Part of the content and code on this page is translated from the blog post [Дискретное извлечение корня](http://e-maxx.ru/algo/discrete_root) and its English translation [Discrete Root](https://cp-algorithms.com/algebra/discrete-root.html). The Russian version is licensed under Public Domain + Leave a Link; the English version is licensed under CC-BY-SA 4.0.**

## References

1.  [Discrete logarithm - Wikipedia](https://en.wikipedia.org/wiki/Discrete_logarithm)
2.  潘承洞, 潘承彪. 初等数论 (Elementary Number Theory).
3.  冯克勤. 初等数论及其应用 (Elementary Number Theory and Its Applications).
