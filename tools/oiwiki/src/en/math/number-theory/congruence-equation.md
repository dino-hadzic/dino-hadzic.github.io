---
title: Congruence equations
---

## Definition

???+ abstract "Congruence equation"
    For a positive integer $m$ and a univariate polynomial with integer coefficients $f(x)=\sum_{i=0}^n a_ix^i$, where the unknown is $x\in\mathbf{Z}_m$, an equation of the form
    
    $$
    f(x)\equiv 0\pmod m\tag{1}
    $$
    
    is called a univariate **congruence equation** in the unknown $x$ modulo $m$.
    
    If $a_n\not\equiv 0\pmod m$, the equation above is called a congruence equation of degree $n$.
    
    Systems of congruence equations are defined analogously.

For congruence equations of degree one and their systems, see [Linear congruences](./linear-equation.md) and [Chinese remainder theorem](./crt.md).

This article first studies the solvability of congruence equations and the structure of their solution sets, and then briefly introduces methods for solving higher-degree congruence equations.

By the [Chinese remainder theorem](./crt.md), solving a congruence equation modulo a composite $m$ can be reduced to solving it modulo prime powers. Therefore, below we only introduce the theory of congruence equations modulo a prime power and modulo a prime.

## Congruences modulo a prime power

Below we assume that the modulus is $m=p^e~(p\in\mathbf{P},~e\in\mathbf{Z}_{>1})$.

Note that if $x_0$ is a solution of the equation

$$
f(x)\equiv 0\pmod{p^e}
$$

then $x_0$ is a solution of the equation

$$
f(x)\equiv 0\pmod{p^{e-1}}
$$

This inspires us to try to construct solutions modulo a higher power from solutions modulo a lower power. We have the following theorem:

???+ note "Theorem 1 (Hensel's lemma)"
    For a prime $p$ and an integer $e>1$, take a polynomial with integer coefficients $f(x)=\sum_{i=0}^na_ix^i~(p^e\nmid a_n)$, and let $f'(x)=\sum_{i=1}^nia_ix^{i-1}$ be its derivative. Let $x_0$ be a solution of the equation
    
    $$
    f(x)\equiv 0\pmod{p^{e-1}}\tag{2}
    $$
    
    Then:
    
    1.  If $f'(x_0)\not\equiv 0\pmod p$, there exists an integer $t$ such that
    
        $$
        x=x_0+p^{e-1}t \tag{3}
        $$
    
        is a solution of the equation
    
        $$
        f(x)\equiv 0\pmod{p^e} \tag{4}
        $$
    
    2.  If $f'(x_0)\equiv 0\pmod p$ and $f(x_0)\equiv 0\pmod{p^e}$, then for $t=0,1,\dots,p-1$ all $x$ determined by formula $(3)$ are solutions of equation $(4)$.
    3.  If $f'(x_0)\equiv 0\pmod p$ and $f(x_0)\not\equiv 0\pmod{p^e}$, then no solution of equation $(4)$ can be constructed by formula $(3)$.

???+ note "Proof"
    Suppose that $(3)$ is a solution of equation $(4)$, i.e.
    
    $$
    f(x_0+p^{e-1}t)\equiv 0\pmod{p^e}
    $$
    
    Rearranging, we get
    
    $$
    f(x_0)+p^{e-1}tf'(x_0)\equiv 0\pmod{p^e}
    $$
    
    hence
    
    $$
    tf'(x_0)\equiv -\frac{f(x_0)}{p^{e-1}}\pmod p\tag{5}
    $$
    
    1.  If $f'(x_0)\not\equiv 0\pmod p$, equation $(5)$ in $t$ has a unique solution $t_0$; substituting into $(3)$, one verifies that it is a solution of equation $(4)$.
    2.  If $f'(x_0)\equiv 0\pmod p$ and $f(x_0)\equiv 0\pmod{p^e}$, every $t$ satisfies equation $(5)$; substituting into $(3)$, one verifies that they are all solutions of equation $(4)$.
    3.  If $f'(x_0)\equiv 0\pmod p$ and $f(x_0)\not\equiv 0\pmod{p^e}$, equation $(5)$ has no solution, so no solution of equation $(4)$ can be constructed by formula $(3)$.

Hence we have the corollary:

???+ note "Corollary 1"
    For $p$, $e$, $f(x)$, $x_0$ as in Theorem 1:
    
    1.  If $s$ is a solution of the equation $f(x)\equiv 0\pmod p$ and $f'(s)\not\equiv 0\pmod p$, then there exists $x_s\in\mathbf{Z}_{p^e}$, $x_s\equiv s\pmod p$, such that $x_s$ is a solution of equation $(4)$.
    2.  If the equations $f(x)\equiv 0\pmod p$ and $f'(x)\equiv 0\pmod p$ have no common solution, then equation $(4)$ and the equation $f(x)\equiv 0\pmod p$ have the same number of solutions.

Thus we can reduce congruence equations modulo a prime power to the case of congruence equations modulo a prime.

## Congruences modulo a prime

Below, let $p\in\mathbf{P}$, let $f(x)=\sum_{i=0}^na_ix^i$ be a polynomial with integer coefficients where $p\nmid a_n$, and let $x\in\mathbf{Z}_p$.

???+ note "Theorem 2"
    If the equation
    
    $$
    f(x)\equiv 0\pmod p\tag{6}
    $$
    
    has $k$ distinct solutions $x_1,x_2,\dots,x_k~(k\leq n)$, then
    
    $$
    f(x)\equiv g(x)\prod_{i=1}^k(x-x_i)\pmod p,
    $$
    
    where $\deg g=n-k$ and $[x^{n-k}]g(x)=a_n$.

???+ note "Proof"
    By mathematical induction on $k$.
    
    -   For $k=1$, polynomial division with remainder gives $f(x)=(x-x_1)g(x)+r$, where $r\in\mathbf{Z}$.
    
        From $f(x_1)\equiv 0\pmod p$ we get $r\equiv 0\pmod p$, hence $f(x)\equiv(x-x_1)g(x)\pmod p$.
    -   Suppose the statement holds for $k-1$ ($k>1$), and now let $f(x)$ have $k$ distinct solutions $x_1,x_2,\dots,x_k$; then $f(x)\equiv(x-x_1)h(x)\pmod p$, and hence
    
        $$
        (\forall i=2,3,\dots,k),~~0\equiv f(x_i)\equiv (x_i-x_1)h(x_i)\pmod p
        $$
    
        Therefore $h(x)$ has $k-1$ distinct solutions $x_2,x_3,\dots,x_k$, and by the induction hypothesis
    
        $$
        h(x)\equiv g(x)\prod_{i=2}^k(x-x_i)\pmod p
        $$
    
        where $\deg g=n-k$ and $[x^{n-k}]g(x)=a_n$.
    
        This proves the statement.

???+ note "Corollary 2"
    For a prime $p$:
    
    -   $(\forall x\in\mathbf{Z}),~~x^{p-1}-1 \equiv \prod_{i=1}^{p-1}(x-i)\pmod p$.
    -   ([Wilson's theorem](./factorial.md#wilsons-theorem)) $(p-1)! \equiv -1 \pmod p$.

???+ note "Theorem 3 (Lagrange's theorem)"
    Equation $(6)$ has at most $n$ distinct solutions.

???+ note "Proof"
    Suppose $f(x)$ has $n+1$ distinct solutions $x_1,x_2,\dots,x_{n+1}$; then by Theorem 2, for $x_1,x_2,\dots,x_n$ we have
    
    $$
    f(x)\equiv a_n\prod_{i=1}^n(x-x_i)\pmod p
    $$
    
    Let $x=x_{n+1}$; then
    
    $$
    0\equiv f(x_{n+1})\equiv a_n\prod_{i=1}^n(x_{n+1}-x_i)\pmod p
    $$
    
    but the right-hand side is obviously not a multiple of $p$, so the assumption leads to a contradiction.

???+ note "Corollary 3"
    If the congruence equation $\sum_{i=0}^nb_ix^i\equiv 0\pmod p$ has more than $n$ solutions, then
    
    $$
    (\forall i=0,1,\dots,n),~~p\mid b_i.
    $$

???+ note "Theorem 4"
    If the number of solutions of equation $(6)$ is not $p$, then there necessarily exists a polynomial with integer coefficients $r(x)$ with $\deg r<p$ such that $f(x)\equiv 0\pmod p$ and $r(x)\equiv 0\pmod p$ have the same solution set.

???+ note "Proof"
    Without loss of generality let $n\geq p$, and divide $f(x)$ with remainder:
    
    $$
    f(x)=g(x)\left(x^p-x\right)+r(x)
    $$
    
    where $\deg r<p$.
    
    By [Fermat's little theorem](./fermat.md), for every integer $x$ we have $x^p\equiv x\pmod p$, hence
    
    -   if $r(x)\equiv 0\pmod p$, then by Corollary 2, $f(x)$ has $p$ distinct solutions;
    -   if $r(x)\not\equiv 0\pmod p$, then from $f(x)\equiv r(x)\pmod p$ it follows that $f(x)$ and $r(x)$ have the same solution set.

We can use this theorem to reduce the degree of a congruence equation.

???+ note "Theorem 5"
    Let $n\leq p$. The equation
    
    $$
    x^n+\sum_{i=0}^{n-1}a_ix^i\equiv 0\pmod p\tag{7}
    $$
    
    has $n$ solutions if and only if there exist polynomials with integer coefficients $q(x)$, $r(x)~(\deg r < n)$ such that
    
    $$
    x^p-x=f(x)q(x)+pr(x). \tag{8}
    $$

???+ note "Proof"
    -   Necessity: by polynomial division, there exist polynomials with integer coefficients $q(x)$, $r_1(x)~(\deg r_1 < n)$ such that
    
        $$
        x^p-x=f(x)q(x)+r_1(x).
        $$
    
        If equation $(7)$ has $n$ solutions, then $r_1\equiv 0\pmod p$ also has the same $n$ solutions, and hence by Corollary 3 there exists a polynomial with integer coefficients $r(x)$ satisfying $r_1(x)=pr(x)$; this proves the statement.
    -   Sufficiency: if $(8)$ holds, then by [Fermat's little theorem](./fermat.md), for every integer $x$,
    
        $$
        0\equiv x^p-x\equiv f(x)q(x)\pmod p.
        $$
    
        That is, the equation $f(x)q(x)\equiv 0\pmod p$ has $p$ solutions.
    
        Let the number of solutions of equation $(7)$ be $s$; then by Lagrange's theorem $s\leq n$.
    
        Moreover, since $\deg q=p-n$, by Lagrange's theorem the number of solutions of $q(x)\equiv 0\pmod p$ does not exceed $p-n$, and the solution set of the equation $f(x)q(x)\equiv 0\pmod p$ is the union of the solution set of $f(x)\equiv 0\pmod p$ and the solution set of $q(x)\equiv 0\pmod p$, so $s+(p-n)\geq p$, i.e. $s\geq n$.
    
        Therefore $s=n$.

For non-monic polynomials, since $\mathbf{Z}_p$ is a field, they can be converted into monic polynomials, so the theorem applies.

???+ note "Theorem 6"
    Let $n\mid p-1$ and $p\nmid a$. The equation
    
    $$
    x^n\equiv a\pmod p\tag{9}
    $$
    
    has a solution if and only if
    
    $$
    a^{\frac{p-1}{n}}\equiv 1\pmod p.
    $$
    
    Moreover, if $(9)$ has a solution, the number of solutions is $n$.

???+ note "Note"
    For the concrete structure of the solution set of equation $(9)$, see [k-th power residues](./residue.md).

???+ note "Proof"
    -   Necessity: if equation $(9)$ has a solution $x_0$, then
    
        $$
        a^{\frac{p-1}{n}}\equiv {\left(x_0^n\right)}^{\frac{p-1}{n}}\equiv 1\pmod p
        $$
    -   Sufficiency: if $a^{\frac{p-1}{n}}\equiv 1\pmod p$, then
    
        $$
        \begin{aligned}
            x^p-x&=x\left(x^{p-1}-1\right)\\
            &=x\left(\left(x^n\right)^{\frac{p-1}{n}}-a^{\frac{p-1}{n}}+a^{\frac{p-1}{n}}-1\right)\\
            &=\left(x^n-a\right)P(x)+x\left(a^{\frac{p-1}{n}}-1\right)\\
        \end{aligned}
        $$
    
        where $P(x)$ is some polynomial with integer coefficients, so by Theorem 5 equation $(9)$ has $n$ solutions.

## Methods for solving higher-degree congruences (and systems)

First, using the [Chinese remainder theorem](./crt.md), we convert solving a **system of congruence equations** into solving **congruence equations**, and solving a congruence equation modulo a **composite** $m$ into solving congruence equations modulo **prime powers**. Then, using [Theorem 1](#congruences-modulo-a-prime-power), we convert solving a congruence equation modulo a **prime power** into solving a congruence equation modulo a **prime**.

Combining the theorems on congruence equations modulo a prime, we only need to consider how to solve the equation

$$
x^n+\sum_{i=0}^{n-1}a_ix^i\equiv 0\pmod p
$$

where $p$ is a prime and $n<p$.

By substituting $x$ with $x-\dfrac{a_{n-1}}{n}$ we can eliminate the $x^{n-1}$ term, so we only need to consider how to solve the equation

$$
x^n+\sum_{i=0}^{n-2}a_ix^i\equiv 0\pmod p\tag{10}
$$

where $p$ is a prime and $n<p$.

-   If $n=1$, see [Linear congruences](./linear-equation.md) for the method.
-   If $n=2$, see [Quadratic residues](./quad-residue.md) for the method.
-   If equation $(10)$ can be converted into

    $$
    x^n\equiv a\pmod p,
    $$

    see [k-th power residues](./residue.md) for the method.

## References

1.  [Congruence Equation -- from Wolfram MathWorld](https://mathworld.wolfram.com/CongruenceEquation.html)
2.  [Lagrange's theorem (number theory) - Wikipedia](https://en.wikipedia.org/wiki/Lagrange%27s_theorem_%28number_theory%29)
3.  潘承洞, 潘承彪 (Pan Chengdong, Pan Chengbiao). 初等数论 (Elementary Number Theory).
4.  冯克勤 (Feng Keqin). 初等数论及其应用 (Elementary Number Theory and Its Applications).
5.  闵嗣鹤, 严士健 (Min Sihe, Yan Shijian). 初等数论 (Elementary Number Theory).
