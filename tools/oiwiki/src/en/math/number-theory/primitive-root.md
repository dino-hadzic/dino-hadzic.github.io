---
title: Multiplicative order & primitive root
---

Prerequisites: [Fermat's little theorem](./fermat.md#fermats-little-theorem), [Euler's theorem](./fermat.md#eulers-theorem), [Lagrange's theorem](./congruence-equation.md#congruences-modulo-a-prime)

The multiplicative order and the primitive root are important tools for understanding the multiplicative structure of the [reduced residue system](./basic.md#congruence-classes-and-residue-systems) $\mathbf Z_m^*$ modulo $m$. Concepts such as the [discrete logarithm](./discrete-logarithm.md) are defined on top of them. A more general discussion can be found in the relevant sections of the [group theory](../algebra/group-theory.md#阶) and [ring theory](../algebra/ring-theory.md#应用整数同余类的乘法群) pages of the abstract algebra part.

## Order

In this section we always assume that the modulus $m\in\mathbf N_+$ and the base $a\in\mathbf Z$ are coprime, i.e. $(a,m)=1$, which is also written as $a\perp m$.

For $n\in\mathbf Z$, the powers $a^n\bmod m$ exhibit a cyclic structure. The minimum length of this cycle is the order of $a$ modulo $m$. The order is defined as the exponent at which the power $a^n \bmod m$ returns to the starting point $a^0\bmod m = 1$ for the first time:

???+ abstract "Order"
    For $a\in\mathbf Z,m\in\mathbf N_+$ with $a\perp m$, the smallest positive integer $n$ satisfying the congruence $a^n \equiv 1 \pmod m$ is called **the order of $a$ modulo $m$**, denoted by $\delta_m(a)$ or $\operatorname{ord}_m(a)$.

???+ tip "Note"
    In [abstract algebra](../algebra/group-theory.md#阶), the "order" here is exactly the order of the element $a$ in the group formed by the reduced residue system modulo $m$ under multiplication. The notation $\delta$ for the order is used only for this particular group. Many of the properties below generalize directly to properties of the order of a group element in abstract algebra.
    
    There is also the concept of the "half-order", denoted by $\delta^-$ in number theory. It is the smallest positive integer satisfying the congruence $a^n \equiv -1 \pmod m$. The half-order is not a concept of group theory. The order always exists, while the half-order does not necessarily exist.

### Cyclic structure of powers

Using the order, the cyclic structure of powers can be described. For the power $a^n\bmod m$, divide the exponent $n$ by the order $\delta_m(a)$ with remainder:

$$
n = \delta_m(a)q + r, ~ 0\le r < \delta_m(a). 
$$

Then, by the laws of exponents, we obtain

$$
a^n = a^{\delta_m(a)q + r} = (a^{\delta_m(a)})^q \cdot a^r \equiv a^r \pmod m.
$$

This shows that a power with an arbitrary exponent can be shifted into the first non-negative cycle. From this, a series of properties of the order can be derived.

???+ note "Property 1"
    For $a\in\mathbf Z,m\in\mathbf N_+$ with $a\perp m$, the powers $a^0(=1),a,a^2,\cdots,a^{\delta_m(a)-1}$ are pairwise incongruent modulo $m$.

??? note "Proof"
    We argue by contradiction. Suppose there exist two numbers $0\le i< j<\delta_m(a)$ with $a^i\equiv a^j\pmod m$; then $a^{j - i}\equiv 1\pmod m$. But $0 < j - i < \delta_m(a)$. This contradicts the minimality of the order, so the statement holds.

???+ note "Property 2"
    For $a,n\in\mathbf Z,m\in\mathbf N_+$ with $a\perp m$, the congruence $a^n \equiv 1 \pmod m$ holds if and only if $\delta_m(a)\mid n$.

??? note "Proof"
    As stated above, $a^{n}\equiv a^{n\bmod\delta_m(a)}\pmod m$. By Property 1, the only $r$ in the range $0\le r < \delta_m(a)$ for which $a^r\equiv 1\pmod m$ holds is $r=0$. Therefore $a^n \equiv 1 \pmod m$ holds if and only if $n\bmod \delta_m(a) = 0$, that is, $\delta_m(a)\mid n$.

By [Euler's theorem](./fermat.md#eulers-theorem), the congruence $a^{\varphi(m)}\equiv 1\pmod m$ holds for all $a\perp m$. Combined with Property 2, this means that $\delta_m(a)\mid\varphi(m)$ for all $a\perp m$. In other words, $\varphi(m)$ is a common multiple of the orders of all $a\perp m$. For a positive integer $m$, the least common multiple of the orders $\delta_m(a)$ of all $a\perp m$, denoted by $\lambda(m)$, is the [Carmichael function](#carmichael-function) of $m$. Its properties are discussed in detail later.

Similarly to other cyclic structures, the order of $a^k$ can be computed from the order of $a$.

???+ note "Property 3"
    For $k,a\in\mathbf Z,m\in\mathbf N_+$ with $a\perp m$, we have
    
    $$
    \delta_m(a^k) = \dfrac{\delta_m(a)}{(\delta_m(a),k)}.
    $$

??? note "Proof"
    By Property 2, the congruence $(a^k)^n = a^{kn} \equiv 1\pmod m$ holds if and only if $\delta_m(a) \mid kn$. This condition is equivalent to
    
    $$
    \dfrac{\delta_m(a)}{\left(\delta_m(a),k\right)} \mid n.
    $$
    
    The smallest positive integer satisfying this condition is
    
    $$
    \delta_m(a^k)=\dfrac{\delta_m(a)}{\left(\delta_m(a),k\right)}.
    $$

### Order of a product

Let $a,b$ be distinct integers coprime to $m$. If the orders $\delta_m(a)$ and $\delta_m(b)$ are known, then some information about the order $\delta_{m}(ab)$ of their product $ab$ can also be obtained.

???+ note "Property 4"
    For $a,b\in\mathbf Z,m\in\mathbf N_+$ with $a,b\perp m$, we have
    
    $$
    \dfrac{[\delta_m(a),\delta_m(b)]}{(\delta_m(a),\delta_m(b))} \mid \delta_m(ab) \mid [\delta_m(a),\delta_m(b)].
    $$

??? note "Proof"
    Since $[\delta_m(a),\delta_m(b)]$ is a multiple of both $\delta_m(a)$ and $\delta_m(b)$, by Property 2 we have
    
    $$
    (ab)^{[\delta_m(a),\delta_m(b)]} = a^{[\delta_m(a),\delta_m(b)]} b^{[\delta_m(a),\delta_m(b)]} \equiv 1 \pmod m.
    $$
    
    Applying Property 2 again, we obtain
    
    $$
    \delta_m(ab) \mid [\delta_m(a),\delta_m(b)].
    $$
    
    This gives the divisibility relation on the right.
    
    Conversely, since
    
    $$
    1 \equiv (ab)^{\delta_m(ab)\delta_m(b)} \equiv a^{\delta_m(ab)\delta_m(b)} \pmod m,
    $$
    
    applying Property 2 we obtain $\delta_m(a)\mid\delta_m(ab)\delta_m(b)$. Canceling $(\delta_m(a),\delta_m(b))$ on both sides, we obtain
    
    $$
    \dfrac{\delta_m(a)}{(\delta_m(a),\delta_m(b))}\mid\delta_m(ab)\dfrac{\delta_m(b)}{(\delta_m(a),\delta_m(b))}.
    $$
    
    After canceling the common factor, the two fractions are coprime, which gives
    
    $$
    \dfrac{\delta_m(a)}{(\delta_m(a),\delta_m(b))}\mid\delta_m(ab).
    $$
    
    Similarly, we also have
    
    $$
    \dfrac{\delta_m(b)}{(\delta_m(a),\delta_m(b))}\mid\delta_m(ab).
    $$
    
    Since the left-hand sides of the two divisibility relations are coprime, we have
    
    $$
    \dfrac{[\delta_m(a),\delta_m(b)]}{(\delta_m(a),\delta_m(b))} =\dfrac{\delta_m(a)\delta_m(b)}{(\delta_m(a),\delta_m(b))^2}\mid\delta_m(ab).
    $$
    
    This gives the divisibility relation on the left.

In the case where the orders of $a$ and $b$ are coprime, this conclusion has a simpler form.

???+ note "Property 4'"
    For $a,b\in\mathbf Z,m\in\mathbf N_+$ with $a,b\perp m$, we have
    
    $$
    \delta_m(ab) = \delta_m(a)\delta_m(b) \iff \delta_m(a)\perp\delta_m(b).
    $$

??? note "Proof"
    If $\delta_m(a)\perp\delta_m(b)$, then all divisibility relations in Property 4 are equalities, so
    
    $$
    \delta_m(ab) = [\delta_m(a),\delta_m(b)] = \delta_m(a)\delta_m(b).
    $$
    
    Conversely, if $\delta_m(ab)=\delta_m(a)\delta_m(b)$, then by Property 4 we have
    
    $$
    \delta_m(a)\delta_m(b) = \delta_m(ab) \mid [\delta_m(a),\delta_m(b)].
    $$
    
    This immediately shows $(\delta_m(a),\delta_m(b))=1$, i.e. $\delta_m(a)\perp\delta_m(b)$.

In the general case, the bound obtained in Property 4 is already tight. A case in which the order of the product attains the lower bound is easy to construct: for example, for $(a,b,m)=(3,5,7)$ we have $\delta_m(a)=\delta_m(b)=6$, but the order of their product is $\delta_m(ab)=1$.

Although in the general case the order of the product $ab$ is not necessarily the least common multiple of their orders, one can always find an element whose order equals this least common multiple.

???+ note "Property 5"
    For $a,b\in\mathbf Z,m\in\mathbf N_+$ with $a,b\perp m$, there always exists $c\in\mathbf Z$ with $c\perp m$ such that
    
    $$
    \delta_m(c) = [\delta_m(a),\delta_m(b)].
    $$

??? note "Proof"
    Consider the prime factorizations:
    
    $$
    \delta_m(a) = \prod_p p^{\alpha_p},~ \delta_m(b) = \prod_p p^{\beta_p}.
    $$
    
    According to the relative sizes of $\alpha_p$ and $\beta_p$, all prime factors can be divided into two classes:
    
    $$
    A = \{p : \alpha_p \ge \beta_p\}, ~ B = \{p : \alpha_p < \beta_p\}.
    $$
    
    Accordingly, set
    
    $$
    \gamma_A = \prod_{p\in A}p^{\alpha_p},~\gamma_B = \prod_{p\in B}p^{\alpha_p},~\eta_A = \prod_{p\in A}p^{\beta_p},~\eta_B = \prod_{p\in B}p^{\beta_p},
    $$
    
    so that $\delta_m(a) = \gamma_A\gamma_B$ and $\delta_m(b)=\eta_A\eta_B$. By Property 3, we have
    
    $$
    \begin{aligned}
    \delta_m(a^{\gamma_B}) &= \dfrac{\delta_m(a)}{(\delta_m(a),\gamma_B)} = \dfrac{\delta_m(a)}{\gamma_B} = \gamma_A,\\
    \delta_m(b^{\eta_A}) &= \dfrac{\delta_m(b)}{(\delta_m(b),\eta_A)} = \dfrac{\delta_m(b)}{\eta_A} = \eta_B.
    \end{aligned}
    $$
    
    Since $\gamma_A\perp\eta_B$, by Property 4' we have
    
    $$
    \delta_m(a^{\gamma_B}b^{\eta_A}) = \gamma_A\eta_B = \prod_p p^{\max\{\alpha_p,\beta_p\}} = [\delta_m(a),\delta_m(b)].
    $$
    
    Therefore, $c=a^{\gamma_B}b^{\eta_A}$ is an element of order $[\delta_m(a),\delta_m(b)]$.

This conclusion is often used to construct elements of a prescribed order.

## Primitive root

Primitive roots are special elements – their order equals the number of elements of the reduced residue system modulo $m$.

???+ abstract "Primitive root"
    For $m\in\mathbf N_+$, if there exists $g\in\mathbf Z$ with $g\perp m$ such that $\delta_m(g)=|\mathbf Z_m^*|=\varphi(m)$, then $g$ is called a **primitive root modulo $m$**. Here $\varphi(m)$ is [Euler's totient function](./euler-totient.md).

Not every positive integer $m$ has a primitive root modulo $m$. By [Property 1](#cyclic-structure-of-powers) above, if a primitive root $g$ modulo $m$ exists, then the congruence classes of $g,g^2,\cdots,g^{\varphi(m)}$ are pairwise distinct and form the reduced residue system modulo $m$. In particular, for a prime $p$, the residues $g^i\bmod p$ for $i=1,2,\cdots,p-1$ are pairwise distinct.

???+ tip "Note"
    In [abstract algebra](../algebra/ring-theory.md#应用整数同余类的乘法群), a primitive root is a generator of a cyclic group. This concept bears the name "primitive root" only in the group formed by the reduced residue system modulo $m$ under multiplication; in general cyclic groups it is called a "generator". Not every group formed by the reduced residue system modulo $m$ under multiplication is cyclic: the existence of a primitive root indicates that it is isomorphic to a cyclic group, and the non-existence indicates that it is not.

When the modulus is $1$, the multiplicative group of integers modulo $1$ is $\{0\}$. It is obviously cyclic, so the primitive root is $0$.

### Primitive root criterion

If all prime factors of $\varphi(m)$ are known, it is easy to decide whether a given $g$ is a primitive root modulo $m$.

???+ note "Theorem"
    For an integer $m\ge 3$ and $g\perp m$, $g$ is a primitive root modulo $m$ if and only if for every prime factor $p$ of $\varphi(m)$,
    
    $$
    g^{\frac{\varphi(m)}{p}}\not\equiv 1 \pmod m.
    $$

??? note "Proof"
    Necessity is obvious. To prove sufficiency, we argue by contradiction. If $g$ is not a primitive root modulo $m$, then necessarily $\delta_m(g)< \varphi(m)$. By [Property 2](#cyclic-structure-of-powers) and Euler's theorem, $\delta_m(g)\mid\varphi(m)$. Hence, let $p$ be a prime factor of $\dfrac{\varphi(m)}{\delta_m(g)}$; then $\delta_m(g)\mid\dfrac{\varphi(m)}{p}$. Applying Property 2 again, we obtain
    
    $$
    g^{\frac{\varphi(m)}{p}} \equiv 1 \pmod m.
    $$
    
    But $p$ is also a prime factor of $\varphi(m)$, which contradicts the hypothesis of the theorem. Hence sufficiency holds.

### Number of primitive roots

A primitive root, if it exists, is not necessarily unique. In general, regarding the possible orders of all elements of the reduced residue system modulo $m$ and the number of elements of a given order, we have the following conclusion:

???+ note "Theorem"
    If a positive integer $m$ has a primitive root $g$, then an element of order $d$ modulo $m$ exists if and only if $d\mid\varphi(m)$, and in that case there are exactly $\varphi(d)$ of them. In particular, the number of primitive roots modulo $m$ is $\varphi(\varphi(m))$.

??? note "Proof"
    By the definition of a primitive root, all reduced congruence classes modulo $m$ can be written in the form $g^k\bmod m$, where $k$ is one of $1,2,\cdots,\varphi(m)$. By [Property 3](#cyclic-structure-of-powers), the orders of these elements equal
    
    $$
    \delta_m(g^k) = \dfrac{\varphi(m)}{(\varphi(m),k)}.
    $$
    
    Therefore, an element of order $d$ exists if and only if $d\mid\varphi(m)$. Moreover, for $d\mid\varphi(m)$, letting $d'=\varphi(m)/d$, the set of these elements is
    
    $$
    \begin{aligned}
    A &= \{g^k : (\varphi(m),k)=d',~1\le k \le\varphi(m)\} \\
    &= \{g^k : d'\mid k,~ (d, k/d') = 1,~ 1 \le k/d' \le d\}.
    \end{aligned}
    $$
    
    The numbers $k'=k/d'$ corresponding to these elements are exactly the positive integers not exceeding $d$ and coprime to $d$. By the definition of Euler's totient function, there are $\varphi(d)$ of them.

### Primitive root existence theorem

In this section we establish the following primitive root existence theorem:

???+ note "Theorem"
    A primitive root modulo $m$ exists if and only if $m=1,2,4,p^e,2p^e$, where $p$ is an odd prime and $e\in\mathbf N_+$.

To prove this statement, the following four cases need to be discussed separately:

1.  $m=1,2,4$: the primitive roots are $g=0,1,3$ respectively, and they obviously exist.

2.  $m=p^{e}$ is a power of an odd prime, where $p$ is an odd prime and $e\in\mathbf N_+$.

    ???+ note "Lemma 1"
        For an odd prime $p$, a primitive root modulo $p$ exists.

    ??? note "Proof"
        The proof consists of two steps.
        
        **Step 1**: for $d\mid(p-1)$, the congruence $x^d\equiv 1\pmod p$ has exactly $d$ pairwise distinct solutions.
        
        Let $p-1=kd$ and consider the polynomial
        
        $$
        f(x) = x^{d(k-1)} + x^{d(k-2)} + \cdots + x^d + 1. 
        $$
        
        By [Euler's theorem](./fermat.md#eulers-theorem), the congruence $(x^d-1)f(x)=x^{p-1}-1\equiv 0\pmod{p}$ has exactly $p-1$ pairwise distinct solutions. These solutions are the zeros of $x^d-1$ and of $f(x)$ respectively. By [Lagrange's theorem](./congruence-equation.md#congruences-modulo-a-prime), they can have at most $d$ and $d(k-1)$ pairwise distinct zeros respectively. Since $d+d(k-1)=p-1$, the former must have exactly $d$ pairwise distinct zeros. This shows that the congruence $x^d\equiv 1\pmod p$ has exactly $d$ pairwise distinct solutions.
        
        **Step 2**: for $d\mid(p-1)$, there are exactly $\varphi(d)$ elements of order $d$.
        
        Sort all divisors of $p-1$ and apply induction. Since an element of order $1$ can only be $1$, there is exactly one such element, so the base case holds. For $d\mid(p-1)$, by [Property 2](#cyclic-structure-of-powers) above, the solutions of the congruence $x^d\equiv 1\pmod p$ must satisfy $\delta_p(x)\mid d$. Therefore, the number of elements of order $d$ among them is
        
        $$
        N(d) = d - \sum_{e\mid d,~e\neq d} N(e) = d - \sum_{e\mid d,~e\neq d} \varphi(e) = \varphi(d).
        $$
        
        The second equality is the induction hypothesis, and the third is a property of Euler's totient function. By mathematical induction, for all $d\mid(p-1)$ there are exactly $\varphi(d)$ elements of order $d$.
        
        In particular, for $d=p-1$ there are exactly $\varphi(p-1)$ elements of order $(p-1)$. Therefore, a primitive root modulo $p$ exists.

    ???+ note "Lemma 2"
        For an odd prime $p$ and $e \in \mathbf{N}_+$, a primitive root modulo $p^e$ exists.

    ??? note "Proof"
        The proof consists of three steps.
        
        **Step 1**: there exists a primitive root $g$ modulo $p$ such that $g^{p-1}\not\equiv 1\pmod{p^2}$.
        
        Take any primitive root $g$ modulo $p$. If it does not satisfy the condition, i.e. $g^{p-1}\equiv 1\pmod{p^2}$, then it can be shown that $g+p$ satisfies the condition: $g+p$ is also a primitive root modulo $p$, and
        
        $$
        \begin{aligned}
        (g+p)^{p-1} &\equiv \binom{p-1}{0}g^{p-1} + \binom{p-1}{1}g^{p-2}p \\
        &= g^{p-1} + g^{p-2}p(p-1) \\ 
        &\equiv 1 - pg^{p-2} \not\equiv 1 \pmod{p^2}.
        \end{aligned}
        $$
        
        **Step 2**: for the $g$ chosen above and every $e\ge 1$, we have $g^{\varphi(p^e)}\not\equiv 1\pmod{p^{e+1}}$.
        
        The choice of $g$ guarantees that the statement holds for $e=1$. Suppose the statement holds for $e$; we now prove that it also holds for $e+1$. For any $e \ge 1$, by Euler's theorem there exists an integer $t$ such that
        
        $$
        g^{\varphi(p^e)} = 1 + t p^e
        $$
        
        holds. By the induction hypothesis, $t\perp p$. Since $\varphi(p^{e+1})=p\varphi(p^e)$, we have
        
        $$
        g^{\varphi(p^{e+1})} = \left(g^{\varphi(p^{e})}\right)^p = (1 + t p^e)^p \equiv 1 + t p^{e+1} \pmod{p^{e+2}}.
        $$
        
        Combined with $t\perp p$, this shows $g^{\varphi(p^{e+1})}\not\equiv 1\pmod{p^{e+2}}$. By mathematical induction, the statement holds.
        
        **Step 3**: the $g$ chosen above is a primitive root modulo $p^e$ for every $e\ge 1$.
        
        The choice of $g$ guarantees that the statement holds for $e=1$. Suppose the statement holds for $e$; we now prove that it also holds for $e+1$. Write $\delta_{p^{e+1}}(g)$ briefly as $\delta$. Since $g^\delta\equiv 1\pmod{p^{e+1}}$, necessarily also $g^\delta\equiv 1\pmod{p^e}$. By the induction hypothesis, $\delta_{p^e}(g) = \varphi(p^e)$. Therefore, by [Property 2](#cyclic-structure-of-powers) of the order above, $\varphi(p^e)\mid\delta$. Also, by Euler's theorem, $\delta\mid\varphi(p^{e+1})$. But $\varphi(p^{e+1})=p\varphi(p^e)$. Therefore, there are only two possibilities: $\delta=\varphi(p^e)$ or $\delta=\varphi(p^{e+1})$. However, the conclusion of Step 2 shows that $g^{\varphi(p^e)}\not\equiv 1\pmod{p^{e+1}}$. Therefore, the possibility $\delta=\varphi(p^e)$ is ruled out. The only possibility is $\delta=\varphi(p^{e+1})$. This shows that $g$ is a primitive root modulo $p^{e+1}$. By mathematical induction, the statement holds for all $e\ge 1$.

3.  $m=2p^{e}$, where $p$ is an odd prime and $e\in\mathbf N_+$.

    ???+ note "Lemma 3"
        For an odd prime $p$ and $e \in \mathbf{N}_+$, a primitive root modulo $2p^e$ exists.

    ??? note "Proof"
        Let $g$ be a primitive root modulo $p^{e}$; then $g+p^e$ is also a primitive root modulo $p^{e}$. One of the two is necessarily odd; without loss of generality, let it be $g$. Clearly $(g,2p^e)=1$. Let $\delta=\delta_{2p^e}(g)$; we need to prove $\delta=\varphi(2p^e)$. By Euler's theorem, $\delta\mid\varphi(2p^e)$. At the same time, by definition $g^\delta\equiv 1\pmod{2p^e}$, so $g^\delta\equiv 1\pmod{p^e}$; therefore, by [Property 2](#cyclic-structure-of-powers) of the order and the choice of $g$, $\delta_{p^e}(g)=\varphi(p^e)\mid \delta$. By the formula for Euler's totient function, $\varphi(2p^e) = \varphi(p^e)$. Therefore, $\delta=\delta_{2p^e}(g)=\varphi(p^e)=\varphi(2p^e)$. This shows that $g$ is a primitive root modulo $2p^e$.

4.  $m\ne 1,2,4,p^{e},2p^{e}$, where $p$ is an odd prime and $e\in\mathbf N_+$.

    ???+ note "Lemma 4"
        Suppose $m\neq 1,2,4$ and there is no odd prime $p$ and positive integer $e$ such that $m=p^e$ or $m=2p^e$. Then no primitive root modulo $m$ exists.

    ??? note "Proof"
        For $m=2^e$ with $e\ge 3$, suppose a primitive root $g$ modulo $m$ exists. Since $g\perp m$, it must be odd. Suppose $g=2k+1$ with $k\in\mathbf N$; then
        
        $$
        \begin{aligned}
        g^{2^{e-2}}
        &=(2k+1)^{2^{e-2}} \\
        &\equiv 1 + \binom{2^{e-2}}{1}(2k) + \binom{{2^{e-2}}}{2}(2k)^2 \\
        &= 1 + 2^{e-1}k + 2^{e-1}(2^{e-2}-1)k^2 \\
        &= 1 + 2^{e-1}(k + (2^{e-2}-1)k^2) \\
        &\equiv 1 \pmod{2^{e}}.
        \end{aligned}
        $$
        
        In the second-to-last line, since $k$ and $(2^{e-2}-1)k^2$ have the same parity, their sum is even. By the definition of the order, $\delta_{2^{e}}(g)\le 2^{e-2}< \varphi(2^{e}) = 2^{e-1}$. This contradicts the assumption that $g$ is a primitive root. By contradiction, such a primitive root does not exist.
        
        Suppose $m$ satisfies the stated conditions and is not a power of $2$; then there necessarily exist $2 < m_1 < m_2$ with $m_1\perp m_2$ such that $m=m_1m_2$. Suppose a primitive root $g$ modulo $m$ exists. Since $g\perp m$, we have $g\perp m_i$ for $i=1,2$. By Euler's theorem,
        
        $$
        g^{\varphi(m_i)} \equiv 1 \pmod{m_i}.
        $$
        
        Since $m_i > 2$, $\varphi(m_i)$ is even, so for $i=1,2$ we have
        
        $$
        g^{\frac{1}{2}\varphi(m_1)\varphi(m_2)} \equiv 1 \pmod{m_i}.
        $$
        
        By the [Chinese remainder theorem](./crt.md),
        
        $$
        g^{\frac{1}{2}\varphi(m_1)\varphi(m_2)} \equiv 1 \pmod{m}.
        $$
        
        Since moreover $\varphi(m)=\varphi(m_1)\varphi(m_2)$, by the definition of the order we have
        
        $$
        \delta_m(g) \le \frac{1}{2}\varphi(m_1)\varphi(m_2) = \dfrac{1}{2}\varphi(m) < \varphi(m).
        $$
        
        This contradicts the assumption that $g$ is a primitive root modulo $m$. Hence, by contradiction, no primitive root modulo $m$ exists.

Combining the four cases above, we have obtained a necessary and sufficient condition for a number to have a primitive root.

### Algorithm for finding a primitive root

For any modulus $m$ for which a primitive root exists, to find its primitive root $g$ it suffices to enumerate candidate positive integers and check one by one whether each is a primitive root. When enumerating, there are usually two approaches: enumerating one by one from small to large, or randomly generating some positive integers. The practical efficiency of these two approaches is comparable.

When enumerating one by one from small to large, one obtains the smallest primitive root $g_m$ modulo $m$, so the complexity of the enumeration part depends on the size of $g_m$. The following estimates are known:

-   Upper bound estimates: Wang Yuan[^yuan1959note] and Burgess[^burgess1962character] proved that the least primitive root of a prime $p$ satisfies $g_p=O\left(p^{0.25+\epsilon}\right)$, where $\epsilon>0$. Cohen, Odoni, and Stothers[^cohen1974least] and Elliott and Murata[^elliott1998least] proved that this estimate also holds for the moduli $p^2$ and $2p^2$ respectively, where $p$ is an odd prime. Since for $e>2$ a primitive root modulo $p^2$ (or $2p^2$) is also a primitive root modulo $p^e$ (or $2p^e$), the upper bound $O\left(p^{0.25+\epsilon}\right)$ for the least primitive root holds in all cases.
-   Lower bound estimates: Fridlender[^fridlender1949least] and Salié[^salie1949kleinsten] proved that there exists $C>0$ such that for infinitely many primes $p$, the least primitive root satisfies $g_p > C\log p$.
-   Average-case estimates: Burgess and Elliott[^burgess1968average] proved that on average the least primitive root of a prime $p$ is $g_p=O((\log p)^2(\log\log p)^4)$. Elliott and Murata[^elliott1997average] further conjectured that the average value of the least primitive root of a prime $p$ is a constant, and by numerical verification[^more-evidence] obtained that it is approximately $4.926$. Subsequently, Elliott and Murata[^elliott1998least] extended this conjecture to the case of the modulus $2p^2$.

Based on these analyses, when searching for the smallest primitive root by brute force, the complexity $O(g_m(\log m)^2)$ of the enumeration part is acceptable.

Besides enumerating from small to large, a primitive root can also be found by randomly generating positive integers and verifying them. The density of primitive roots is not low:[^density-prim-root]

$$
\dfrac{\varphi(\varphi(m))}{m} = \Omega\left(\dfrac{1}{\log\log m}\right).
$$

Therefore, when searching for a primitive root by the random method, the expected complexity of the enumeration part is $O((\log m)^2\log\log m)$.

Note that testing a primitive root requires knowing the prime factorization of $\varphi(m)$. Among the [commonly used factorization algorithms](./pollard-rho.md) in competitive programming, even Pollard's rho algorithm, which has the best complexity, needs $O(m^{1/4+\epsilon})$ time. Therefore, as long as the prime factorization of $\varphi(m)$ is unknown, whichever enumeration method is used, the complexity bottleneck of finding a primitive root lies in the factorization step rather than in the enumeration and verification part.

## Carmichael function

In contrast to the order of an element modulo $m$, which is a local concept, the Carmichael function is a global concept. It is the smallest common period of the powers of all integers coprime to $m$.

???+ abstract "Carmichael function"
    For $m\in\mathbf N_+$, define $\lambda(m)$ as the smallest positive integer $n$ such that the congruence $a^n\equiv 1\pmod m$ holds for all $a\perp m$. The function $\lambda:\mathbf N_+\to\mathbf N_+$ is called the **Carmichael function**.

By [Property 2](#cyclic-structure-of-powers), $a^n\equiv 1\pmod m$ holding for all $a\perp m$ means that $\delta_m(a)\mid n$ holds for all $a\perp m$. That is, a positive integer $n$ satisfying this condition must be a common multiple of all $\delta_m(a)$. Therefore, the smallest such $n$ is their least common multiple:

$$
\lambda(m) = \operatorname{lcm}\{\delta_m(a) : a\perp m\}.
$$

This is also often used as an equivalent definition of the Carmichael function.

Applying [Property 5](#order-of-a-product) repeatedly, there must exist some element $a\perp m$ such that $\delta_m(a)=\lambda(m)$. Therefore, the above formula can also be written as

$$
\lambda(m) = \max\{\delta_m(a) : a\perp m\}.
$$

An element $a\perp m$ attaining this maximum is also called a **$\lambda$‑primitive root** modulo $m$. It exists for every modulus $m$.

### Recursive formula

The Carmichael function is an [arithmetic function](./basic.md#number-theoretic-functions). This section discusses a recursive formula for it and thereby gives another proof of the primitive root existence theorem.

Although it is not a multiplicative function, when computing the Carmichael function, coprime factors can likewise be handled separately.

???+ note "Lemma"
    For coprime positive integers $m_1,m_2$, we have $\lambda(m_1m_2)=[\lambda(m_1),\lambda(m_2)]$.

??? note "Proof"
    Let $a_1$ and $a_2$ be $\lambda$‑primitive roots modulo $m_1$ and modulo $m_2$ respectively. Let $m=m_1m_2$; by the [Chinese remainder theorem](./crt.md), there exists $a\perp m$ such that $a\equiv a_i\pmod{m_i}$ holds for $i=1,2$. Since $a^{\lambda(m)}\equiv 1\pmod m$, for $i=1,2$ we have $a_i^{\lambda(m)} \equiv 1\pmod{m_i}$, and then by [Property 2](#cyclic-structure-of-powers) and the choice of $a_i$, $\lambda(m_i)=\delta_{m_i}(a_i)\mid \lambda(m)$. This shows $[\lambda(m_1),\lambda(m_2)]\mid\lambda(m)$.
    
    Conversely, for any $a\perp m$ and $i=1,2$, we have $a^{[\lambda(m_1),\lambda(m_2)]} \equiv 1 \pmod{m_i}$. Applying the Chinese remainder theorem, we obtain that $a^{[\lambda(m_1),\lambda(m_2)]} \equiv 1 \pmod{m}$ holds for all $a\perp m$. By the definition of the Carmichael function, $\lambda(m)\mid [\lambda(m_1),\lambda(m_2)]$.
    
    Hence the equality in the statement holds.

Therefore, it remains only to compute the values of the Carmichael function at prime powers. First, we handle the case of powers of $2$.

???+ note "Lemma"
    For $m=2^e$ with $e\in\mathbf N_+$, we have $\lambda(2)=1$, $\lambda(4)=2$, and $\lambda(m)=2^{e-2}$ for all $e\ge 3$.

??? note "Proof"
    The cases $m=2,4$ can be checked separately. For $m=2^e$ with $e\ge 3$, first repeat the first part of the proof of [Lemma 4](#primitive-root-existence-theorem) above to obtain $\lambda(m)\le 2^{e-2}$. Then it suffices to prove that an element of order $2^{e-2}$ exists. For this, we have
    
    $$
    5^{2^{e-3}} = (1 + 2^2)^{2^{e-3}} \equiv 1 + 2^2\times 2^{e-3} = 1 + 2^{e-1} \not\equiv 1 \pmod{2^e}.
    $$
    
    This shows $\delta_m(5)\nmid 2^{e-3}$, and since $\delta_m(5) \mid 2^{e-2}$, $5$ can only be an element of order $2^{e-2}$. This shows that $\lambda(m)=2^{e-2}$.

In the course of proving this lemma, we have actually obtained a description of the structure of the reduced residue system modulo $2^e$:

???+ note "Corollary"
    Let the modulus be $2^e$ with $e \ge 2$. Then every odd number is congruent to a unique integer of the form $\pm 5^k$, where $k\in\mathbf N$ and $k < 2^{e-2}$. That is, $\pm 1,\pm 5,\cdots,\pm 5^{2^{e-2}-1}$ are pairwise incongruent and form a reduced residue system.

??? note "Proof"
    It is easy to verify that the case $e=2$ holds. For $e \ge 3$, since the preceding proof already showed that the order of $5$ modulo $2^e$ is $2^{e-2}$, the numbers $1,5,\cdots,5^{2^{e-2}-1}$ are pairwise incongruent. Since all these integers are congruent to $1$ modulo $4$ and their negatives are congruent to $3$ modulo $4$, the numbers $\pm 1,\pm 5,\cdots,\pm 5^{2^{e-2}-1}$ are pairwise incongruent modulo $2^e$. Since there are $2^{e-1}$ of them in total, which is exactly the size of the reduced residue system modulo $2^{e}$, they form the reduced residue system itself.

Next, we handle the case of odd prime powers.

???+ note "Lemma"
    For $m=p^e$, where $p$ is an odd prime and $e\in\mathbf N_+$, we have $\lambda(m)=p^{e-1}(p-1)$.

??? note "Proof"
    First we prove that the statement holds for $e=1$, i.e. when $m=p$ is an odd prime. For this, by the definition of the Carmichael function, all integers $a$ coprime to $p$ are solutions of the congruence $x^{\lambda(p)}\equiv 1\pmod{p}$. Modulo $p$, this congruence has $p-1$ pairwise distinct solutions in total. By [Lagrange's theorem](./congruence-equation.md#congruences-modulo-a-prime), $p-1\le\lambda(p)$. At the same time, Euler's theorem requires $\lambda(p)\mid\varphi(p)=p-1$. Therefore, $\lambda(p)=p-1$.
    
    For $m=p^e$ with $e> 1$, we can start by proving that $1+p$ is an element of order $p^{e-1}$. For this, we have
    
    $$
    (1+p)^{p^{e-1}} \equiv 1,\quad (1+p)^{p^{e-2}} \equiv 1 + p^{e-1} \not\equiv 1 \pmod{p^e}.
    $$
    
    Therefore, $\delta_m(1+p)=p^{e-1}$. Moreover, let $g$ be a primitive root modulo $p$; then, since $g^{\delta_m(g)}\equiv 1 \pmod{p}$, by [Property 2](#cyclic-structure-of-powers) of the order we have $p-1\mid\delta_m(g)$. By the definition of the Carmichael function and Euler's theorem,
    
    $$
    p^{e-1}(p-1) \mid [\delta_m(1+p),\delta_m(g)] \mid \lambda(m) \mid \varphi(m) = p^{e-1}(p-1).
    $$
    
    Therefore, $\lambda(m)=p^{e-1}(p-1)$.

Summarizing the results of this section, we obtain the recursive formula for the Carmichael function:

???+ note "Theorem"
    For any positive integer $m$, we have
    
    $$
    \lambda(m) = \begin{cases}
    \varphi(m), & \text{if }m=1,2,4,p^e\text{ for odd prime }p\text{ and }e \ge 1,\\
    \frac{1}{2}\varphi(m), &\text{if }m=2^e,~e\ge 3,\\
    \operatorname{lcm}\{\lambda(p_1^{e_1}),\lambda(p_2^{e_2}),\cdots,\lambda(p_s^{e_s})\}, &\text{if }m = p_1^{e_1}p_2^{e_2}\cdots p_s^{e_s}\text{ for distinct }p_1,p_2,\cdots,p_s.
    \end{cases}
    $$

Using this recursive formula, the earlier result can be strengthened:

???+ note "Corollary"
    For positive integers $m_1,m_2$, we have $\lambda([m_1,m_2])=[\lambda(m_1),\lambda(m_2)]$.

Comparing the definitions of the primitive root and the Carmichael function, a primitive root modulo $m$ exists if and only if $\lambda(m)=\varphi(m)$. From the recursive formula for the Carmichael function, the following result is easily obtained by induction:

???+ note "Corollary"
    A primitive root modulo $m$ exists if and only if $m=1,2,4,p^e,2p^e$, where $p$ is an odd prime and $e\in\mathbf N_+$.

Since the proof of the recursive formula in this section did not use the primitive root existence theorem, this constitutes another proof of that theorem.

### Carmichael numbers

Using the Carmichael function, one can discuss the properties and distribution of Carmichael numbers (OEIS: [A002997](https://oeis.org/A002997)). These are the composite numbers that the [Fermat primality test](./prime.md#fermat-primality-test) can never correctly rule out.

???+ abstract "Carmichael number"
    For a composite number $n$, if the congruence $a^{n-1} \equiv 1 \pmod n$ holds for all integers $a\perp n$, then $n$ is called a **Carmichael number**.

The smallest Carmichael number is $561 = 3 \times 11 \times 17$.

By the definition of the Carmichael function, a composite number $n$ is a Carmichael number if and only if $\lambda(n)\mid n-1$, where $\lambda(n)$ is the Carmichael function. Furthermore, the following method for deciding whether a composite number $n$ is a Carmichael number can be obtained:

???+ note "Korselt's criterion[^korselt1899probleme]"
    A composite number $n$ is a Carmichael number if and only if $n$ is squarefree and $(p-1) \mid (n-1)$ for every prime factor $p$ of $n$.

??? note "Proof"
    First we prove the necessity of the condition. Suppose $\lambda(n)\mid (n-1)$. Inspecting the recursive formula for the Carmichael function, if $n$ has a square factor $p^2$, then necessarily $p\mid \lambda(n)$. But $p\nmid (n-1)$, a contradiction. Similarly, for any prime factor $p$ of $n$, the recursive formula for the Carmichael function shows that $(p-1)\mid \lambda(n)$, so $(p-1) \mid (n-1)$ as well.
    
    Then we prove the sufficiency of the condition. Since $n$ is a squarefree composite number, it has at least two distinct prime factors, among which there must be an odd prime factor $p$; from $(p-1)\mid(n-1)$ it follows that $n-1$ is even, so $n$ must be odd. For a squarefree odd composite number $n$, by the recursive formula for the Carmichael function, $\lambda(n)=\operatorname{lcm}\{p-1:p\mid n\}$. Therefore, as long as $(p-1) \mid (n-1)$ holds for all prime factors $p$, we must have $\lambda(n)\mid (n-1)$.

Starting from this criterion, some simple properties of Carmichael numbers can be established:

???+ note "Corollary"
    Carmichael numbers are odd, squarefree, and have at least $3$ distinct prime factors.

??? note "Proof"
    The first two properties follow directly from Korselt's criterion and its proof. To obtain the third property, it suffices to further prove that the product $n=p_1p_2$ of distinct primes $p_1,p_2$ is never a Carmichael number. Suppose $n=p_1p_2$ is a Carmichael number. By Korselt's criterion, $(p_i-1)\mid (n-1)$. But we have
    
    $$
    n-1=p_1p_2-1\equiv p_2-1 \pmod{p_1-1}.
    $$
    
    Therefore, $(p_1-1)\mid(p_2-1)$. Similarly, $(p_2-1)\mid(p_1-1)$. That is, $p_1=p_2$. This contradicts the assumption. Therefore, a Carmichael number $n$ has at least $3$ distinct prime factors.

Using analytic number theory, some properties of the distribution of Carmichael numbers can also be obtained. Let $C(n)$ be the number of Carmichael numbers less than or equal to $n$. Alford, Granville, and Pomerance[^alford1994infinitely] proved that for sufficiently large $n$, $C(n)>n^{2/7}$. Hence there are infinitely many Carmichael numbers. Before that, Erdős[^erdos1956pseudoprimes] had already proved that $C(n) < n\exp\left(-c\dfrac{\ln n\ln\ln\ln n}{\ln\ln n}\right)$, where $c$ is a constant. Therefore, the distribution of Carmichael numbers is very sparse (compared to primes). In fact,[^pinchcarmichael] $C(10^9)=646$ and $C(10^{18})=1~401~644$.

## References and notes

-   [Primitive root modulo n - Wikipedia](https://en.wikipedia.org/wiki/Primitive_root_modulo_n)
-   [The order of a unit - Course Notes](https://crypto.stanford.edu/pbc/notes/numbertheory/order.html)
-   [The primitive root theorem - Amin Witno's notes](http://witno.com/philadelphia/notes/won5.pdf)
-   [Carmichael function - Wikipedia](https://en.wikipedia.org/wiki/Carmichael_function)
-   [Carmichael's Lambda Function - Brilliant Math & Science Wiki](https://brilliant.org/wiki/carmichaels-lambda-function/)
-   [Carmichael number - Wikipedia](https://en.wikipedia.org/wiki/Carmichael_number)
-   [Carmichael Number - Wolfram MathWorld](https://mathworld.wolfram.com/CarmichaelNumber.html)

[^yuan1959note]: Wang Y. "On the least primitive root of a prime." (in Chinese). Acta Math Sinica, 1959, 4: 432–441; English transl. in*Sci. Sinica*, 1961, 10: 1–14.

[^burgess1962character]: BURGESS, David A. "On character sums and primitive roots." Proceedings of the London Mathematical Society, 1962, 3.1: 179-192.

[^cohen1974least]: Cohen, S. D., R. W. K. Odoni, and W. W. Stothers. "On the least primitive root modulo $p^2$." Bulletin of the London Mathematical Society 6, no. 1 (1974): 42-46.

[^elliott1998least]: Elliott, P. D. T. A., and L. Murata. "The least primitive root mod $2p^2$." Mathematika 45, no. 2 (1998): 371-379.

[^fridlender1949least]: FRIDLENDER, V. R. "On the least n-th power non-residue." Dokl. Akad. Nauk SSSR. 1949. p. 351-352.

[^salie1949kleinsten]: SALIÉ, Hans. "Über den kleinsten positiven quadratischen Nichtrest nach einer Primzahl." Mathematische Nachrichten, 1949, 3.1: 7-8.

[^burgess1968average]: Burgess, D. A., and P. D. T. A. Elliott. "The average of the least primitive root." Mathematika 15, no. 1 (1968): 39-50.

[^elliott1997average]: Elliott, Peter DTA, and Leo Murata. "On the average of the least primitive root modulo p." Journal of The London Mathematical Society 56, no. 3 (1997): 435-454.

[^more-evidence]: More results can be found at [Least prime primitive root of prime numbers](https://sweet.ua.pt/tos/p_roots.html).

[^density-prim-root]: If a primitive root modulo $m$ exists, then $\varphi(m)\ge\dfrac{1}{3}m$, with equality only at $m=2\times 3^e~(e\in\mathbf N_+)$. Furthermore, for $m > 2$, Euler's totient function $\varphi(m)$ satisfies the estimate $\varphi(m)>\dfrac{m}{e^{\gamma}\log\log m+\frac{3}{\log\log m}}$. Combining these two facts gives the expression in the text. For this estimate of Euler's totient function, see the paper Rosser, J. Barkley, and Lowell Schoenfeld. "Approximate formulas for some functions of prime numbers." Illinois Journal of Mathematics 6, no. 1 (1962): 64-94.

[^korselt1899probleme]: Korselt, A. R. (1899). "Problème chinois." L'Intermédiaire des Mathématiciens. 6: 142–143.

[^alford1994infinitely]: W. R. Alford; Andrew Granville; Carl Pomerance (1994). "There are Infinitely Many Carmichael Numbers." Annals of Mathematics. 140 (3): 703–722.

[^erdos1956pseudoprimes]: Erdős, P. (1956). "On pseudoprimes and Carmichael numbers." Publ. Math. Debrecen. 4 (3–4): 201–206.

[^pinchcarmichael]: PINCH, Richard GE. The Carmichael numbers up to ${10}^{20}$.
