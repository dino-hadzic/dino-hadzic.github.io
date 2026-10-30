---
title: Quadratic residue
---

## Introduction

Quadratic residues can be thought of as a discussion of whether the **square root** operation is feasible in modular arithmetic. For roots of higher degree, see [k-th residue](./residue.md).

## Definition

???+ abstract "Quadratic residue"
    Let $a$ and $p$ be integers with $(a,p)=1$. If there exists an integer $x$ such that
    
    $$
    x^2\equiv a\pmod p,
    $$
    
    then $a$ is called a quadratic residue modulo $p$; otherwise $a$ is called a quadratic non-residue modulo $p$. In what follows, when the modulus $p$ is clear, we may simply write quadratic (non-)residue.

## Euler's criterion

When the modulus is an odd prime, we have the following theorem:

???+ abstract "Euler's criterion"
    For an odd prime $p$ and an integer $a$ with $(a,p)=1$,
    
    $$
    a^{\frac{p-1}{2}}\equiv\begin{cases}
        1 \pmod p,  & (\exists x\in\mathbf{Z}),~~a\equiv x^2\pmod p,\\
        -1 \pmod p, & \text{otherwise}.\\
    \end{cases}
    $$
    
    That is, for the above $p$ and $a$:
    
    1.  $a$ is a quadratic residue modulo $p$ if and only if $a^{\frac{p-1}{2}}\equiv 1 \pmod p$.
    2.  $a$ is a quadratic non-residue modulo $p$ if and only if $a^{\frac{p-1}{2}}\equiv -1 \pmod p$.

??? note "Proof"
    First, by [Fermat's little theorem](./fermat.md#fermats-little-theorem) we have $a^{p-1}\equiv 1\pmod p$, hence
    
    $$
    \left(a^{\frac{p-1}{2}}+1\right)\left(a^{\frac{p-1}{2}}-1\right)\equiv 0\pmod p,
    $$
    
    so for every $a$ with $(a,p)=1$ we have $a^{(p-1)/2}\equiv \pm 1\pmod p.$
    
    Moreover, since $p$ is an odd prime, we have:
    
    $$
    x^{p-1}-a^{\frac{p-1}{2}}={\left(x^2\right)}^{\frac{p-1}{2}}-a^{\frac{p-1}{2}}=(x^2-a)P(x),
    $$
    
    where $P(x)$ is some polynomial with integer coefficients, and therefore:
    
    $$
    \begin{aligned}
        x^p-x&=x\left(x^{p-1}-a^{\frac{p-1}{2}}\right)+x\left(a^{\frac{p-1}{2}}-1\right)\\
        &=(x^2-a)xP(x)+\left(a^{\frac{p-1}{2}}-1\right)x.\\
    \end{aligned}
    $$
    
    By [Theorem 5 on congruence equations](./congruence-equation.md#congruences-modulo-a-prime), $a$ is a quadratic residue modulo $p$ if and only if $a^{(p-1)/2}\equiv 1\pmod p$. Consequently, $a$ is a quadratic non-residue modulo $p$ if and only if $a^{(p-1)/2}\equiv -1\pmod p$.

Based on Euler's criterion, we obtain the following corollary:

???+ note "Number of quadratic residues"
    For an odd prime $p$, there are $\dfrac{p-1}{2}$ quadratic residues and as many quadratic non-residues modulo $p$.

??? note "Proof"
    By Euler's criterion, consider $a^{\frac{p-1}{2}}\equiv 1\pmod p.$
    
    Note that $\dfrac{p-1}{2}\mid (p-1)$, so by [Theorem 6 on congruence equations](./congruence-equation.md#congruences-modulo-a-prime) the congruence $a^{\frac{p-1}{2}}\equiv 1\pmod p$ has $\dfrac{p-1}{2}$ solutions. Therefore there are $\dfrac{p-1}{2}$ quadratic residues and as many quadratic non-residues modulo $p$.

## Legendre symbol

To simplify the following discussion, we introduce the following notation:

???+ abstract "Legendre symbol"
    For an **odd prime** $p$ and an integer $a$, the Legendre symbol is defined as follows:
    
    $$
    \left(\frac{a}{p}\right)=\begin{cases}
        0,  & p\mid a,\\
        1,  & (p\nmid a) \land ((\exists x\in\mathbf{Z}),~~a\equiv x^2\pmod p),\\
        -1, & \text{otherwise}.\\
    \end{cases}
    $$

That is, for $a$ with $(a,p)=1$:

-   $a$ is a quadratic residue modulo $p$ if and only if $\left(\dfrac{a}{p}\right)=1.$
-   $a$ is a quadratic non-residue modulo $p$ if and only if $\left(\dfrac{a}{p}\right)=-1.$

The table below shows some values of the Legendre symbol (from [Wikipedia](https://en.wikipedia.org/wiki/Legendre_symbol#Table_of_values)).

![](./images/quad_residue.png)

### Properties

1.  For every integer $a$,

    $$
    a^{\frac{p-1}{2}}\equiv \left(\frac{a}{p}\right)\pmod p.
    $$

    Furthermore, we have the corollaries:

    -   $$
        \left(\dfrac{1}{p}\right)=1.
        $$
    -   $$
        \left(\dfrac{-1}{p}\right)=(-1)^{\frac{p-1}{2}}=\begin{cases}
            1,  & p\equiv 1\pmod 4,\\
            -1, & p\equiv 3\pmod 4.
            \end{cases}
        $$

2.  $a_1\equiv a_2\pmod p\implies \left(\dfrac{a_1}{p}\right)=\left(\dfrac{a_2}{p}\right).$

3.  ([Complete multiplicativity](./basic.md#multiplicative-functions)) For all integers $a_1,a_2$,

    $$
    \left(\frac{a_1a_2}{p}\right)=\left(\frac{a_1}{p}\right)\left(\frac{a_2}{p}\right).
    $$

    We have the corollary: for integers $a,b$ with $p\nmid b$,

    $$
    \left(\frac{ab^2}{p}\right)=\left(\frac{a}{p}\right).
    $$

4.  $$
    \left(\frac{2}{p}\right)=(-1)^{\frac{p^2-1}{8}}=\begin{cases}
            1,  & p\equiv \pm 1\pmod 8, \\
            -1, & p\equiv \pm 3\pmod 8. \\
        \end{cases}
    $$

??? note "Proof"
    1.  Follows directly from the [definition of the Legendre symbol](#legendre-symbol) and [Euler's criterion](#eulers-criterion).
    2.  Note that
    
        $$
        a_1\equiv a_2\pmod p\implies \left(\frac{a_1}{p}\right)\equiv\left(\frac{a_2}{p}\right)\pmod p,
        $$
    
        and since $\left|\left(\dfrac{a_1}{p}\right)-\left(\dfrac{a_2}{p}\right)\right|\leq 2$ and $p>2$, we get:
    
        $$
        a_1\equiv a_2\pmod p\implies \left(\frac{a_1}{p}\right)=\left(\frac{a_2}{p}\right).
        $$
    3.  From 1 we get
    
        $$
        \left(\frac{a_1a_2}{p}\right)\equiv a_1^{\frac{p-1}{2}}a_2^{\frac{p-1}{2}}\equiv\left(\frac{a_1}{p}\right)\left(\frac{a_2}{p}\right)\pmod p.
        $$
    
        and since $\left|\left(\dfrac{a_1a_2}{p}\right)-\left(\dfrac{a_1}{p}\right)\left(\dfrac{a_2}{p}\right)\right|\leq 2$ and $p>2$, we get
    
        $$
        \left(\frac{a_1a_2}{p}\right)=\left(\frac{a_1}{p}\right)\left(\frac{a_2}{p}\right).
        $$
    4.  See the [law of quadratic reciprocity](#law-of-quadratic-reciprocity).

Based on the properties above, if for any two odd primes $p$ and $q$ we can compute the value of $\left(\dfrac{p}{q}\right)$, then we can compute the value of the Legendre symbol in every valid case. Next we have a beautiful theorem that ingeniously establishes a connection between $\left(\dfrac{p}{q}\right)$ and $\left(\dfrac{q}{p}\right)$, allowing us to finish the computation with an idea similar to the [Euclidean algorithm](./gcd.md#euclidean-algorithm).

### Law of quadratic reciprocity

???+ note "Law of quadratic reciprocity"
    Let $p$ and $q$ be two distinct odd primes. Then
    
    $$
    \left(\frac{p}{q}\right)\left(\frac{q}{p}\right)=(-1)^{\frac{p-1}{2}\frac{q-1}{2}}.
    $$

There are many ways to prove it[^ref5]. One proof is based on the following lemma[^ref6]:

???+ note "Gauss's lemma"
    Let $p$ be an odd prime, $(n,p)=1$, and for integers $k~\left(1\leq k\leq (p-1)/2\right)$ let $r_k=nk\bmod p$. Let $A=\{r_k:r_k < p/2\}$ and $B=\{r_k:r_k > p/2\}$. Then
    
    $$
    \left(\frac{n}{p}\right)=(-1)^{|B|}.
    $$

??? note "Proof"
    Let $\lambda=|A|$ and $\mu=|B|$; clearly $\lambda+\mu=(p-1)/2$. Then
    
    $$
    n^{\frac{p-1}{2}}\left(\frac{p-1}{2}\right)!=\prod_{k=1}^{\frac{p-1}{2}} nk\equiv\prod_{a\in A}a\prod_{b\in B}b\pmod{p}.
    $$
    
    We know that for every element $b$ of $B$ we have $\dfrac{p}{2} < b < p$, so $0 < p-b < \dfrac{p}{2}$. Furthermore, for every element $b$ of $B$ we have $p-b\notin A$; otherwise, if there were elements $a,b$ in $A,B$ respectively with $a=p-b$, there would be integers $0 < k_1,k_2 < (p-1)/2$ with $a=nk_1$, $b=nk_2$ and $p\mid n(k_1+k_2)$; since $(n,p)=1$, we get $p\mid (k_1+k_2)$, and since $0 < k_1+k_2 < p$, this is a contradiction. Therefore
    
    $$
    n^{\frac{p-1}{2}}\left(\frac{p-1}{2}\right)!\equiv(-1)^{\mu}\prod_{a\in A}a\prod_{b\in B}(p-b)=(-1)^{\mu}\left(\frac{p-1}{2}\right)!\pmod{p},
    $$
    
    i.e.
    
    $$
    n^{\frac{p-1}{2}}\equiv(-1)^{\mu}\pmod{p}.
    $$
    
    The claim now follows from [Property 1](#properties) of the Legendre symbol.

??? tip "Generalization"
    Gauss's lemma can be generalized as follows[^ref7]:
    
    Let $p$ be an odd prime and let $I\subset\mathbf{Z}_p^*$ satisfy $I\cup -I=\mathbf{Z}_p^*$ and $I\cap -I=\varnothing$, where $-I:=\{-i:i\in I\}$. Then for every integer $n$ coprime to $p$,
    
    $$
    \left(\frac{n}{p}\right)=(-1)^{|J|},
    $$
    
    where $J=\{j\in I:nj\in -I\}$.
    
    It is easy to see that taking $I=\{1,2,\dots,(p-1)/2\}$ gives Gauss's lemma. The proof is essentially the same as the proof of Gauss's lemma, so it is omitted.

The following corollary is easy to obtain:

???+ note "Corollary"
    For an odd prime $p$,
    
    $$
    \left(\frac{2}{p}\right)=(-1)^{\frac{p^2-1}{8}}=\begin{cases}
            1,  & p\equiv \pm 1\pmod 8, \\
            -1, & p\equiv \pm 3\pmod 8. \\
        \end{cases}
    $$
    
    For an odd prime $p$ and an odd number $n$ with $(n,p)=1$,
    
    $$
    \left(\frac{n}{p}\right)=(-1)^{\sum_{i=1}^{(p-1)/2}\lfloor ni/p \rfloor}.
    $$

??? note "Proof"
    For $n,k,r_k,A,B,\lambda,\mu$ from Gauss's lemma we have $nk=p\left\lfloor\dfrac{nk}{p}\right\rfloor+r_k$, and therefore
    
    $$
    \begin{aligned}
        n\cdot\frac{p^2-1}{8}=\sum_{k=1}^{\frac{p-1}{2}}nk&=p\sum_{k=1}^{\frac{p-1}{2}}\left\lfloor\dfrac{nk}{p}\right\rfloor+\sum_{a\in A}a+\sum_{b\in B}b\\
        &=p\sum_{k=1}^{\frac{p-1}{2}}\left\lfloor\dfrac{nk}{p}\right\rfloor+\sum_{a\in A}a+\sum_{b\in B}(p-b)+2\sum_{b\in B}b-p\mu\\
        &=p\sum_{k=1}^{\frac{p-1}{2}}\left\lfloor\dfrac{nk}{p}\right\rfloor+\sum_{k=1}^{\frac{p-1}{2}}k+2\sum_{b\in B}b-p\mu\\
        &=p\sum_{k=1}^{\frac{p-1}{2}}\left\lfloor\dfrac{nk}{p}\right\rfloor+\frac{p^2-1}{8}+2\sum_{b\in B}b-p\mu,
    \end{aligned}
    $$
    
    hence
    
    $$
    (n-1)\frac{p^2-1}{8}=p\sum_{k=1}^{\frac{p-1}{2}}\left\lfloor\dfrac{nk}{p}\right\rfloor+2\sum_{b\in B}b-p\mu.
    $$
    
    If $n=2$, then $0 < \dfrac{nk}{p}\leq\dfrac{p-1}{p} < 1$, so
    
    $$
    \frac{p^2-1}{8}\equiv\mu\pmod{2}.
    $$
    
    If $2\nmid n$, then
    
    $$
    \sum_{k=1}^{\frac{p-1}{2}}\left\lfloor\dfrac{nk}{p}\right\rfloor\equiv\mu\pmod{2}.
    $$

By the corollary above, to prove the law of quadratic reciprocity it suffices to verify

$$
\frac{p-1}{2}\frac{q-1}{2}=\sum_{k=1}^{\frac{p-1}{2}}\left\lfloor\dfrac{qk}{p}\right\rfloor+\sum_{k=1}^{\frac{q-1}{2}}\left\lfloor\dfrac{pk}{q}\right\rfloor.
$$

Consider the set $S$ formed by the points $(px,qy)$, $1\leq x\leq \dfrac{q-1}{2},1\leq y\leq \dfrac{p-1}{2}$, and split it into two parts according to the order of $px$ and $qy$ (clearly $px\neq qy$); it suffices to verify the sizes of the three sets.

The law of quadratic reciprocity can be used not only to decide whether a number $n$ is a quadratic residue modulo $p$, but also to determine the structure of the moduli for which the number $n$ is a quadratic residue.

???+ example "Example"
    -   The odd primes $p$ for which $5$ is a quadratic residue satisfy $p\equiv \pm 1\pmod 5.$
    -   The odd primes $p$ for which $-3$ is a quadratic residue satisfy $p\equiv 1\pmod 3.$
    -   The odd primes $p$ for which $-2$ and $3$ are both quadratic residues satisfy $p\equiv 11\pmod{24}.$

In addition, we can prove statements such as "there are infinitely many primes of the form $4k+1$"; such statements are in fact simple corollaries of [Dirichlet's theorem](https://en.wikipedia.org/wiki/Dirichlet%27s_theorem_on_arithmetic_progressions).

## Jacobi symbol

By the law of quadratic reciprocity, a way to generalize the Legendre symbol naturally comes to mind:

???+ abstract "Jacobi symbol"
    For a **positive odd number** $m=p_1^{\alpha_1}\dots p_k^{\alpha_k}$ and an integer $a$, where $p_1,\dots,p_k$ are primes and $\alpha_1,\dots,\alpha_k$ are positive integers, the Jacobi symbol is defined as follows:
    
    $$
    \left(\frac{a}{m}\right):=\prod_{i=1}^k\left(\frac{a}{p_i}\right)^{\alpha_i}.
    $$
    
    Here the $\left(\frac{a}{p_i}\right)$ on the right-hand side are [Legendre symbols](#legendre-symbol). In addition, for an integer $a$ we have $\left(\dfrac{a}{1}\right)=1.$

???+ warning "Warning"
    We usually do not distinguish between the Legendre symbol and the Jacobi symbol, because by complete multiplicativity the Jacobi symbol has the same properties as the Legendre symbol, so both symbols are computed in the same way. However, one thing needs attention: when $m$ **is not an odd prime**, the value of $\left(\dfrac{a}{m}\right)$ is **unrelated** to whether $a$ is a quadratic residue modulo $m$; but if $\left(\dfrac{a}{m}\right)=-1$, then $m$ has at least one (in fact an odd number of) prime factor $p$ such that $a$ is a quadratic non-residue modulo $p$, and hence $a$ is a quadratic non-residue modulo $m$.

We can further generalize the modulus to **integers** (we only need to add the definitions of $\left(\dfrac{a}{-1}\right)$, $\left(\dfrac{a}{0}\right)$ and $\left(\dfrac{a}{2}\right)$), which gives the [Kronecker symbol](https://en.wikipedia.org/wiki/Kronecker_symbol).

## Square roots in modular arithmetic

This section discusses algorithms for taking square roots in modular arithmetic. In particular, this section mainly covers the case of a prime modulus. For the case of a general modulus, see the discussion in [higher-order roots in modular arithmetic](./residue.md#root-extraction-in-modular-arithmetic).

### Algorithm for special cases

For the congruence $x^2\equiv a\pmod p$, where $p$ is an odd prime and $a$ is a quadratic residue, there is a simpler solution when $p\bmod 4=3$; consider

$$
\begin{aligned}
\left(a^{(p+1)/4}\right)^2&\equiv a^{(p+1)/2}&\pmod p\\
&\equiv x^{p+1}&\pmod p\\
&\equiv \left(x^2\right)\left(x^{p-1}\right)&\pmod p\\
&\equiv x^2&\pmod p&\quad (\because{\text{Fermat's little theorem}})
\end{aligned}
$$

Then $a^{(p+1)/4}\bmod p$ is a solution.

#### Atkin's algorithm

Still consider the congruence above, now with $p\bmod 8=5$. Let $b\equiv (2a)^{(p-5)/8}\pmod p$ and $\mathrm{i}\equiv 2ab^2\pmod p$. Then $\mathrm{i}^2\equiv -1\pmod p$, and $ab(\mathrm{i}-1)\bmod p$ is a solution.

???+ note "Proof"
    $$
    \begin{aligned}
    \mathrm{i}^2&\equiv\left(2ab^2\right)^2&\pmod p\\
    &\equiv \left(2a\cdot \left(2a\right)^{(p-5)/4}\right)^2&\pmod p\\
    &\equiv \left(\left(2a\right)^{(p-1)/4}\right)^2&\pmod p\\
    &\equiv \left(2a\right)^{\frac{p-1}{2}}&\pmod p\\
    &\equiv -1&\pmod p
    \end{aligned}
    $$
    
    Then
    
    $$
    \begin{aligned}
    \left(ab(\mathrm{i}-1)\right)^2&\equiv a^2\cdot \left(2a\right)^{(p-5)/4}\cdot (-2\mathrm{i})&\pmod p\\
    &\equiv a\cdot (-\mathrm{i})\cdot \left(2a\right)^{(p-1)/4}&\pmod p\\
    &\equiv a&\pmod p
    \end{aligned}
    $$

### Cipolla's algorithm

Cipolla's algorithm solves the congruence $y^2\equiv a\pmod p$, where $p$ is an odd prime and $a$ is a quadratic residue.

In this section we consider arithmetic in $\mathbf{F}_p\lbrack x\rbrack /(x^2-g)$, where $g \in \mathbf{F}_p$.

??? note "How to compute"
    Readers unfamiliar with [polynomial rings](../algebra/ring-theory.md#多项式环) can simply think of it this way: the elements of this set all have the form $a_0+a_1x$ with $a_0,a_1\in\mathbf F_p$, and they obey the following arithmetic rules:
    
    $$
    \begin{aligned}
    (a_0+a_1x)+(b_0+b_1x) &\equiv (a_0+b_0)+(a_1+b_1)x &\pmod{(x^2-g)}\\
    (a_0+a_1x)(b_0+b_1x) &\equiv (a_0b_0+a_1b_1g)+(a_1b_0+a_0b_1)x &\pmod{(x^2-g)}
    \end{aligned}
    $$
    
    Note that $x$ here is not a concrete number but a formal symbol in the polynomial. A key point of the computation is to use $x^2 \equiv g \pmod{(x^2-g)}$ to turn the quadratic term into a linear term and a constant term. In addition, all integer operations are done modulo $p$.
    
    For more on this structure, see the pages [Polynomials](../poly/intro.md), [Field theory](../algebra/field-theory.md) and others.

The first step of the algorithm is to find an $r$ such that $r^2-a$ is a quadratic non-residue. Of course, for $a \equiv 0 \pmod p$ no such $r$ can be found, so this case needs special handling. Below we only discuss the case $a \not\equiv 0 \pmod p$. Then we can pick a random $r$ and test it; the expected number of steps to find one is $2$. Then $(r-x)^{\frac{p+1}{2}}\bmod (x^2-(r^2-a))$ is a solution, which can be evaluated by binary exponentiation.

??? note "Why only two steps are needed in expectation"
    Consider the case where $r^2-a$ is a quadratic residue. Then there exists an $x$ such that $r^2-a \equiv x^2 \pmod p$; rearranging gives $(r+x)(r-x) \equiv a \pmod p$. It is easy to see that every $(r+x) \in [1, p-1]$ corresponds one-to-one to a solution pair $(r,x)$, so the original equation has $p-1$ solutions in total. We distinguish the two cases $x \equiv 0$ and $x \not\equiv 0$. For $x \equiv 0$, since $a$ is a quadratic residue, this corresponds to $2$ values of $r$; for $x \not\equiv 0$, there are $p-1-2$ cases, and each $r$ corresponds to two of them, giving $\dfrac{p-3}{2}$ values of $r$ in total. Altogether there are $2+\dfrac{p-3}{2}=\dfrac{p+1}{2}$ cases in which $r^2-a$ is a quadratic residue, so the probability of getting a quadratic non-residue in one random trial is $\dfrac{p-1}{2p}$, and the expected number of steps is $\dfrac{2p}{p-1} \approx 2$.

???+ note "Proof"
    For convenience, first let $f(x)=x^2-(r^2-a)\in\mathbf{F}_p\lbrack x\rbrack$.
    
    What we need to prove is that $(r-x)^{\frac{p+1}{2}} \bmod f(x)$ is a solution of the original equation and that it belongs to $\mathbf{F}_p$. We first prove the former, i.e. that $(r-x)^{p+1}\equiv a\pmod {f(x)}$. For this we first need to prove two lemmas:
    
    **Lemma 1:** $x^p \equiv -x \pmod {f(x)}$
    
    Proof:
    
    $$
    \begin{aligned}
    x^p&= x(x^2)^{\frac{p-1}{2}}\\
    &\equiv x(r^2-a)^{\frac{p-1}{2}}&\pmod{f(x)}&\quad (\because{x^2\equiv r^2-a\pmod{f(x)}})\\
    &\equiv -x&\pmod{f(x)}&\quad (\because{r^2-a}\text{ is quadratic non-residue})
    \end{aligned}
    $$
    
    **Lemma 2:** $(a+b)^p \equiv a^p+b^p \pmod p$
    
    Using the binomial theorem it is easy to see that, except for the first and the last term, the $p$ in the numerator cannot be canceled, so only $a^p+b^p$ remains.
    
    $$
    \begin{aligned}
    (a+b)^p&=\sum_{i=0}^p\binom{p}{i}a^ib^{p-i}\\
    &=\sum_{i=0}^p\frac{p!}{i!(p-i)!}a^ib^{p-i}\\
    &\equiv a^p+b^p\pmod p
    \end{aligned}
    $$
    
    With these two lemmas, we return to proving the original claim:
    
    $$
    \begin{aligned}
    (r-x)^{p+1}
    &= (r-x)^p(r-x)\\
    &\equiv (r^p-x^p)(r-x)&\pmod{f(x)}\\
    &\equiv (r+x)(r-x)&\pmod{f(x)}\\
    &= r^2-x^2\\
    &\equiv r^2-(r^2-a)&\pmod{f(x)}\\
    &= a\\
    \end{aligned}
    $$
    
    Next we prove by contradiction that the solution we obtained belongs to $\mathbf{F}_p$, i.e. that its coefficient of $x$ is $0$.
    
    Suppose there exists $(a_0+a_1x)^2 \equiv a \pmod {f(x)}$ with $a_1 \not\equiv 0 \pmod p$, i.e. $a_0^2+2a_0a_1x+a_1^2x^2 \equiv a \pmod {f(x)}$; rearranging and simplifying gives:
    
    $$
    a_0^2+a_1^2(r^2-a)-a \equiv -2a_0a_1x \pmod {f(x)}
    $$
    
    The coefficient of $x$ on the left-hand side is $0$, so the coefficient of $x$ on the right-hand side is also $0$, i.e. $a_0a_1 \equiv 0 \pmod p$. Since we assumed $a_1 \not\equiv 0 \pmod p$, we must have $a_0 \equiv 0 \pmod p$, so $(a_1x)^2 \equiv a \pmod {f(x)}$, i.e. $r^2-a \equiv aa_1^{-2} \pmod p$.
    
    Since $a$ and $a_1^{-2}$ are both quadratic residues, by the multiplicativity of the Legendre symbol $aa_1^{-2}$ is also a quadratic residue, which contradicts the fact that $r^2-a$ is a quadratic non-residue. Hence the original equation has no solution whose coefficient of $x$ is not $0$, and the coefficient of $x$ in the solution we obtained must also be $0$.

??? example "Template problem [Luogu P5491【模板】二次剩余 (Template: quadratic residue)](https://www.luogu.com.cn/problem/P5491)"
    ```cpp
    --8<-- "docs/math/code/quad-residue/quad-residue_1.cpp"
    ```

### Bostan–Mori algorithm

This algorithm is based on Cipolla's algorithm: we transform the problem into a [homogeneous linear recurrence with constant coefficients](../poly/linear-recurrence.md) and then apply the Bostan–Mori algorithm. Consider another common description of Cipolla's algorithm: $b=x^{\left(p+1\right)/2}\bmod{\left(x^2-tx+a\right)}$ is a solution satisfying $b^2\equiv a\pmod{p}$[^ref3], where $x^2-tx+a\in \mathbf{F}_p\lbrack x\rbrack$ is an irreducible polynomial. The coefficient $t$ is likewise chosen at random. The proof is omitted. Following the algorithm in the paper by Bostan and Mori[^ref4], we find that the problem can be transformed into computing a certain coefficient of the multiplicative inverse of a formal power series:

$$
b=\left\lbrack x^{(p+1)/2}\right\rbrack\dfrac{1}{1-tx+ax^2}
$$

and

$$
\left\lbrack x^n\right\rbrack\dfrac{k_0+k_1x}{1+k_2x+k_3x^2}=
\begin{cases}
\left\lbrack x^{(n-1)/2}\right\rbrack\dfrac{k_1-k_0k_2+k_1k_3x}{1+(2k_3-k_2^2)x+k_3^2x^2},&\text{if }n\bmod 2=1\\
\left\lbrack x^{n/2}\right\rbrack\dfrac{k_0+(k_0k_3-k_1k_2)x}{1+(2k_3-k_2^2)x+k_3^2x^2},&\text{else if }n\neq 0
\end{cases}
$$

while for $n=0$ clearly $\left\lbrack x^0\right\rbrack\dfrac{k_0+k_1x}{1+k_2x+k_3x^2}=k_0$. This algorithm uses fewer multiplications than Cipolla's algorithm. Other related algorithms with few multiplications can be found in Müller's paper[^ref2].

### Legendre's algorithm

For the congruence $x^2\equiv a\pmod p$, where $p$ is an odd prime and $a$ is a quadratic residue, Legendre's algorithm can be described as follows: find $r$ such that $r^2-a$ is a quadratic non-residue, and let $a_0+a_1x=(r-x)^{\frac{p-1}{2}}\bmod (x^2-a)$; then $a_0\equiv 0\pmod p$ and $a_1^{-2}\equiv a\pmod p$.

???+ note "Proof"
    Choose $b$ with $b^2\equiv a\pmod p$. Then $(r-b)(r+b)=r^2-a$ is a quadratic non-residue, so
    
    $$
    (r-b)^{\frac{p-1}{2}}(r+b)^{\frac{p-1}{2}}\equiv -1\pmod p
    $$
    
    There is a ring homomorphism
    
    $$
    \begin{aligned}
    \phi:\mathbf{F}_p\lbrack x\rbrack/(x^2-a)&\to \mathbf{F}_p\times \mathbf{F}_p\\
    x&\mapsto (b,-b)
    \end{aligned}
    $$
    
    Then
    
    $$
    \begin{aligned}
    (a_0+a_1b,a_0-a_1b)&=\phi(a_0+a_1x)\\
    &=\phi(r-x)^{\frac{p-1}{2}}\\
    &=((r-b)^{\frac{p-1}{2}},(r+b)^{\frac{p-1}{2}})\\
    &=(\pm 1,\mp 1)
    \end{aligned}
    $$
    
    so $2a_0=(\pm 1)+(\mp 1)=0$ and $2a_1b=(\pm 1)-(\mp 1)=\pm 2$.

### Tonelli–Shanks algorithm

The Tonelli–Shanks algorithm is an algorithm based on discrete logarithms for solving the congruence $x^2\equiv a\pmod p$[^ref1], where $p$ is an odd prime and $a$ is a quadratic residue modulo $p$.

Let $p-1=m2^n$, where $m$ is odd. Again we use randomization to find $r\in\mathbf{F}_p$ such that $r$ is a quadratic non-residue. Let $g\equiv r^m\pmod p$ and $b\equiv a^{(m-1)/2}\pmod p$. Then there exists an integer $e\in\lbrace 0,1,2,\dots ,2^n-1\rbrace$ such that $ab^2\equiv g^e\pmod p$. If $a$ is a quadratic residue, then $e$ is even and $\left(abg^{-e/2}\right)^2\equiv a\pmod p$.

???+ note "Proof"
    By Fermat's little theorem,
    
    $$
    g^{2^n} \equiv r^{m2^n} = r^{p-1} \equiv 1 \pmod p.
    $$
    
    Moreover, since $r$ is a quadratic non-residue,
    
    $$
    g^{2^{n-1}} \equiv r^{m2^{n-1}} = r^{\frac{p-1}{2}} \equiv -1 \pmod p.  
    $$
    
    Therefore the order of $g$ modulo $p$ is $2^n$. Furthermore, since $ab^2\equiv a^m\pmod p$ is a solution of $x^{2^n}\equiv 1\pmod p$, $a^m$ is a power of $g$. Write $a^m\equiv g^e\pmod p$.
    
    Since $a$ is a quadratic residue,
    
    $$
    g^{e2^{n-1}} \equiv a^{m2^{n-1}} = a^{\frac{p-1}{2}} \equiv 1 \pmod p.
    $$
    
    By the properties of the order, $2^n\mid e2^{n-1}$, so $e$ is even. Hence $abg^{-e/2}\bmod p$ is well defined, and
    
    $$
    \left(abg^{-e/2}\right)^2 = a^2b^2g^{-e} \equiv a^{m+1}g^{-e} \equiv a \pmod p.
    $$

The remaining question is how to compute $e$. Tonelli and Shanks proposed determining one binary digit of $e$ at a time. Write $e$ in binary as $e=e_0+2e_1+4e_2+\cdots$, where $e_k\in\lbrace 0,1\rbrace$. Since $a$ is a quadratic residue, initially $e_0=0$, and then the values $e_k$ are determined digit by digit using the following property:

$$
\left(g^eg^{-(e\bmod 2^k)}\right)^{2^{n-1-k}}\equiv g^{2^{n-1}\cdot e_k}\equiv 
\begin{cases}
1\pmod p,&\text{if }e_k=0\\
-1\pmod p,&\text{if }e_k=1
\end{cases}
$$

Here $g^e\equiv ab^2\pmod p$ is known, and the value of $e\bmod 2^k$ can be computed from the previous digits $e_0,e_1,\cdots,e_{k-1}$. Of course, when implementing the algorithm it suffices to directly maintain the product $g^eg^{-(e\bmod 2^k)}\bmod p$.

## Exercises

-   [Luogu P5491【模板】二次剩余 (Template: quadratic residue)](https://www.luogu.com.cn/problem/P5491)
-   ["Timus 1132" Square Root](https://acm.timus.ru/problem.aspx?space=1&num=1132)

## References and notes

1.  [Quadratic residue - Wikipedia](https://en.wikipedia.org/wiki/Quadratic_residue)
2.  [Euler's criterion - Wikipedia](https://en.wikipedia.org/wiki/Euler%27s_criterion)

[^ref1]: Daniel. J. Bernstein. Faster Square Roots in Annoying Finite Fields.

[^ref2]: S. Müller, On the computation of square roots in finite fields, Design, Codes and Cryptography, Vol.31, pp. 301-312, 2004.

[^ref3]: A. Menezes, P. van Oorschot and S. Vanstone. Handbook of Applied Cryptography, 1996.

[^ref4]: Alin Bostan, Ryuhei Mori. A Simple and Fast Algorithm for Computing the N-th Term of a Linearly Recurrent Sequence. Available at <https://arxiv.org/abs/2008.08822>.

[^ref5]: [Proofs of quadratic reciprocity - Wikipedia](https://en.wikipedia.org/wiki/Proofs_of_quadratic_reciprocity)

[^ref6]: Carl Friedrich Gauss. Untersuchungen über höhere Arithmetik, 1965. Page 458-462.

[^ref7]: Kobi Kremnizer.[Lectures in number theory 2022](https://courses.maths.ox.ac.uk/pluginfile.php/29788/mod_resource/content/1/numbertheory-2022.pdf). Proposition 4.3.
