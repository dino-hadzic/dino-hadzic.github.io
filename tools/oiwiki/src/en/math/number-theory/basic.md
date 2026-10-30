---
title: Number theory basics
---

This article gives a brief introduction to the opening part of number theory.

## Divisibility

???+ note "Definition"
    Let $a,b\in\mathbf{Z}$, $a\ne 0$. If $\exists q\in\mathbf{Z}$ such that $b=aq$, we say that $b$ is **divisible** by $a$ and write $a\mid b$; if $b$ is not divisible by $a$, we write $a\nmid b$.

Properties of divisibility:

-   $a\mid b\iff-a\mid b\iff a\mid-b\iff|a|\mid|b|$
-   $a\mid b\land b\mid c\implies a\mid c$
-   $a\mid b\land a\mid c\iff\forall x,y\in\mathbf{Z}, a\mid(xb+yc)$
-   $a\mid b\land b\mid a\implies b=\pm a$
-   Let $m\ne0$; then $a\mid b\iff ma\mid mb$.
-   Let $b\ne0$; then $a\mid b\implies|a|\le|b|$.
-   Let $a\ne0,b=qa+c$; then $a\mid b\iff a\mid c$.

### Divisors

???+ note "Definition"
    If $a\mid b$, we say that $b$ is a **multiple** of $a$ and $a$ is a **divisor** of $b$.

$0$ is a multiple of every non-$0$ integer. For an integer $b\ne0$, $b$ has only finitely many divisors.

Trivial divisors (trivial factors): for an integer $b\ne0$, $\pm1$ and $\pm b$ are the trivial divisors of $b$. When $b=\pm1$, $b$ has only two trivial divisors.

For an integer $b\ne 0$, the other divisors of $b$ are called proper divisors (proper factors, nontrivial divisors, nontrivial factors).

Properties of divisors:

-   Let $b\ne0$ be an integer. As $d$ runs over all divisors of $b$, $\dfrac{b}{d}$ also runs over all divisors of $b$.
-   Let $b\gt 0$ be an integer; then as $d$ runs over all positive divisors of $b$, $\dfrac{b}{d}$ also runs over all positive divisors of $b$.

In concrete problems, **unless stated otherwise, a divisor always means a positive divisor.**

## Division with remainder

???+ note "Remainder"
    Let $a,b$ be two given integers, $a\ne0$. Let $d$ be a given integer. Then there certainly exists a unique pair of integers $q$ and $r$ satisfying $b=qa+r,d\le r<|a|+d$.

Whatever value the integer $d$ takes, $r$ is collectively called the remainder. $a\mid b$ is equivalent to $a\mid r$.

Usually $d$ is taken to be $0$; then the equation $b=qa+r,0\le r<|a|$ is called division with remainder (Euclidean division). The remainder $r$ here is called the least nonnegative remainder.

There are two other common ways of choosing the remainder:

-   the absolutely least remainder: $d$ is the negative of half of the absolute value of $a$, i.e. $b=qa+r,-\dfrac{|a|}{2}\le r<|a|-\dfrac{|a|}{2}$;
-   the least positive remainder: $d$ is $1$, i.e. $b=qa+r,1\le r<|a|+1$.

The remainder of division with remainder is only the least nonnegative remainder. **Unless stated otherwise, the remainder always means the least nonnegative remainder.**

Properties of the remainder:

-   When any integer is divided by a positive integer $a$, the remainder is certainly one and only one of these $a$ numbers: $0$ to $(a-1)$.
-   When $a$ consecutive integers are divided by a positive integer $a$, exactly the $a$ remainders above are obtained. In particular, there is certainly one and only one of them that is divisible by $a$.

## Greatest common divisor and least common multiple

For the definitions of the four terms common divisor, common multiple, greatest common divisor and least common multiple, see [Greatest common divisor](./gcd.md).

???+ warning "Warning"
    Some authors consider the greatest common divisor of $0$ and $0$ to be undefined, while the remaining authors generally regard it as $0$. The C++ STL implementation adopts the latter, i.e. it considers the greatest common divisor of $0$ and $0$ to be $0$[^gcdcpp].

The greatest common divisor has the following properties:

-   $(a_1,\dots,a_n)=(|a_1|,\dots,|a_n|)$;
-   $(a,b)=(b,a)$;
-   if $a\ne 0$, then $(a,0)=(a,a)=|a|$;
-   $(bq+r,b)=(r,b)$;
-   $(a_1,\dots,a_n)=((a_1,a_2),a_3,\dots,a_n)$. Furthermore, $\forall 1<k<n-1,~(a_1,\dots,a_n)=((a_1,\dots,a_k),(a_{k+1},\dots,a_n))$;
-   for integers $a_1,\dots,a_n$ not all equal to $0$ and a nonzero integer $m$, $(ma_1,\dots,ma_n)=|m|(a_1,\dots,a_n)$;
-   for integers $a_1,\dots,a_n$ not all equal to $0$, if $(a_1,\dots,a_n)=d$, then $(a_1/d,\dots,a_n/d)=1$;
-   $(a^n,b^n)=(a,b)^n$.

The greatest common divisor also has the following properties related to coprimality:

-   if $b|ac$ and $(a,b)=1$, then $b\mid c$;
-   if $b|c$, $a|c$ and $(a,b)=1$, then $ab\mid c$;
-   if $(a,b)=1$, then $(a,bc)=(a,c)$;
-   if $(a_i,b_j)=1,~\forall 1\leq i\leq n,1\leq j\leq m$, then $\left(\prod_i a_i,\prod_j b_j\right)=1$. In particular, if $(a,b)=1$, then $(a^n,b^m)=1$;
-   for integers $a_1,\dots,a_n$, if $\exists v\in \mathbf{Z},~\prod_i a_i=v^m$ and $(a_i,a_j)=1,~\forall i\ne j$, then $\forall 1\leq i\leq n,~\sqrt[m]{a_i}\in\mathbf{Z}$.

The least common multiple has the following properties:

-   $[a_1,\dots,a_n]=[|a_1|,\dots,|a_n|]$;
-   $[a,b]=[b,a]$;
-   if $a\ne 0$, then $[a,1]=[a,a]=|a|$;
-   if $a\mid b$, then $[a,b]=|b|$;
-   $[a_1,\dots,a_n]=[[a_1,a_2],a_3,\dots,a_n]$. Furthermore, $\forall 1<k<n-1,~[a_1,\dots,a_n]=[[a_1,\dots,a_k],[a_{k+1},\dots,a_n]]$;
-   if $a_i\mid m,~\forall 1\leq i\leq n$, then $[a_1,\dots,a_n]\mid m$;
-   $[ma_1,\dots,ma_n]=|m|[a_1,\dots,a_n]$;
-   $[a,b,c][ab,bc,ca]=[a,b][b,c][c,a]$;
-   $[a^n,b^n]=[a,b]^n$.

The greatest common divisor and the least common multiple can be combined into many remarkable identities, such as:

-   $(a,b)[a,b]=|ab|$;
-   $(ab,bc,ca)[a,b,c]=|abc|$;
-   $\dfrac{(a,b,c)^2}{(a,b)(b,c)(a,c)}=\dfrac{[a,b,c]^2}{[a,b][b,c][a,c]}$.

All of these properties can be proved from the definitions or by the [unique factorization theorem](#fundamental-theorem-of-arithmetic), and the proofs using the unique factorization theorem are easier to understand.

### Coprime integers

???+ note "Definition"
    If $(a_1,a_2)=1$, we say that $a_1$ and $a_2$ are **coprime** (**relatively prime**).
    
    If $(a_1,\ldots,a_k)=1$, we say that $a_1,\ldots,a_k$ are **coprime** (**relatively prime**).

If several integers are coprime, they are not necessarily pairwise coprime. For example, $6$, $10$ and $15$ are coprime, but no two of them are coprime.

Properties of coprime integers and the theory of the greatest common divisor: Bézout's identity. See [Bézout's identity](./bezouts.md).

### Euclidean algorithm

The algorithm of successive division is an algorithm also called Euclid's algorithm. See [Greatest common divisor](./gcd.md).

## Primes and composite numbers

For algorithms concerning primes, see [Primes](./prime.md).

???+ note "Definition"
    Let $p\ne0,\pm1$ be an integer. If $p$ has no divisors other than the trivial ones, we call $p$ a **prime** (**irreducible number**).
    
    If an integer $a\ne0,\pm 1$ and $a$ is not a prime, we call $a$ a **composite number**.

$p$ and $-p$ are always both prime or both composite. **Unless stated otherwise, a prime always means a positive prime.**

If a factor of an integer is a prime, that prime is called a prime factor (prime divisor) of the integer.

Simple properties of primes and composite numbers:

-   An integer $a$ greater than $1$ is composite if and only if $a$ can be written as a product of integers $d$ and $e$ ($1<d,e<a$).
-   If a prime $p$ has a divisor $d$ greater than $1$, then $d=p$.
-   An integer $a$ greater than $1$ can certainly be written as a product of primes.
-   For a composite number $a$, there certainly exists a prime $p\le\sqrt{a}$ such that $p\mid a$.
-   There are infinitely many primes.
-   All primes greater than $3$ can be written in the form $6n\pm 1$[^ref1].

## Fundamental theorem of arithmetic

???+ note "Fundamental lemma of arithmetic"
    Let $p$ be a prime and $p\mid a_1a_2$. Then at least one of $p\mid a_1$ and $p\mid a_2$ holds.

A slightly modified converse of the fundamental lemma of arithmetic also gives another definition of a prime.

???+ note "Another definition of a prime"
    For an integer $p\ne 0,\pm 1$, if for all integers $a_1,a_2$ satisfying $p\mid a_1a_2$ we have $p\mid a_1$ or $p\mid a_2$, then $p$ is called a prime.

??? tip "Tip"
    The motivation for this definition can be found in [prime ideals](../algebra/ring-theory.md#素理想).

???+ note "Fundamental theorem of arithmetic (unique factorization theorem)"
    Let $a$ be a positive integer. Then there necessarily exists a representation
    
    $$
    a=p_1p_2\cdots p_s
    $$
    
    where $p_j(1\le j\le s)$ are primes. Moreover, this representation is unique up to order.

???+ note "Canonical prime factorization"
    Merging equal primes in the representation above, we obtain
    
    $$
    a={p_1}^{\alpha_1}{p_2}^{\alpha_2}\cdots{p_s}^{\alpha_s},p_1<p_2<\cdots<p_s
    $$
    
    which is called the canonical prime factorization of the positive integer $a$.

The fundamental theorem of arithmetic and the fundamental lemma of arithmetic are two equivalent theorems.

## Congruence

???+ note "Definition"
    Let $m\ne0$ be an integer. If $m\mid(a-b)$, we call $m$ the **modulus**, say that $a$ is congruent to $b$ modulo $m$, and call $b$ a **residue** of $a$ modulo $m$. We write $a\equiv b\pmod m$.
    
    Otherwise, $a$ is not congruent to $b$ modulo $m$ and $b$ is not a residue of $a$ modulo $m$. We write $a\not\equiv b\pmod m$.
    
    Such an equation is called a congruence modulo $m$, or simply a **congruence**.

By the properties of divisibility, the congruence above is also equivalent to $a\equiv b\pmod{(-m)}$.

In what follows, unless stated otherwise, the modulus is always a **positive integer**.

The $b$ in the congruence is a residue of $a$ modulo $m$; this concept coincides completely with the remainder. By restricting the range of $b$, one correspondingly obtains the least nonnegative residue, the absolutely least residue and the least positive residue of $a$ modulo $m$.

Properties of congruence:

-   Congruence is an [equivalence relation](../order-theory.md#二元关系), i.e. congruence is
    -   reflexive: $a\equiv a\pmod m$;
    -   symmetric: if $a\equiv b\pmod m$, then $b\equiv a\pmod m$;
    -   transitive: if $a\equiv b\pmod m,b\equiv c\pmod m$, then $a\equiv c\pmod m$.
-   Linear operations: if $a,b,c,d\in\mathbf{Z},m\in\mathbf{N}^*,a\equiv b\pmod m,c\equiv d\pmod m$, then:
    -   $a\pm c\equiv b\pm d\pmod m$;
    -   $a\times c\equiv b\times d\pmod m$.
-   Let $f(x)=\sum_{i=0}^n a_ix^i$ and $g(x)=\sum_{i=0}^n b_ix^i$ be two polynomials with integer coefficients, $m\in\mathbf{N}^*$, and $a_i\equiv b_i\pmod m,~0\leq i\leq n$; then for every integer $x$ we have $f(x)\equiv g(x)\pmod m$. Furthermore, if $s\equiv t\pmod m$, then $f(s)\equiv g(t)\pmod m$.
-   If $a,b\in\mathbf{Z},k,m\in\mathbf{N}^*,a\equiv b\pmod m$, then $ak\equiv bk\pmod{mk}$.
-   If $a,b\in\mathbf{Z},d,m\in\mathbf{N}^*,d\mid a,d\mid b,d\mid m$, then whenever $a\equiv b\pmod m$ holds, we have $\dfrac{a}{d}\equiv\dfrac{b}{d}\left(\bmod\;{\dfrac{m}{d}}\right)$.
-   If $a,b\in\mathbf{Z},d,m\in\mathbf{N}^*,d\mid m$, then whenever $a\equiv b\pmod m$ holds, we have $a\equiv b\pmod d$.
-   If $a,b\in\mathbf{Z},d,m\in\mathbf{N}^*$, then whenever $a\equiv b\pmod m$ holds, we have $(a,m)=(b,m)$. If $d$ divides $m$ and one of $a,b$, then $d$ necessarily divides the other of $a,b$.

There is one more property, the multiplicative inverse. See [Modular inverse](./inverse.md).

## Congruence classes and residue systems

For convenience of discussion, for sets $A,B$ and an element $r$ we introduce the following notation:

-   $r+A:=\{r+a:a\in A\}$;
-   $rA:=\{ra:a\in A\}$;
-   $A+B:=\{a+b:a\in A,b\in B\}$;
-   $AB:=\{ab:a\in A,b\in B\}$.

???+ note "Congruence class"
    For a nonzero integer $m$, partition all integers into $|m|$ pairwise disjoint sets such that any two numbers in the same set are congruent modulo $m$; each of these $|m|$ sets is called a **congruence class** or **residue class** modulo $m$. We denote by $r\bmod m$ the congruence class modulo $m$ containing the integer $r$.
    
    It is not hard to prove that for every nonzero integer $m$ such a partition certainly exists and is unique.

From the definition of congruence classes:

-   $r\bmod m=\{r+km:k\in\mathbf{Z}\}$;
-   $r\bmod m=s\bmod m\iff r\equiv s\pmod m$;
-   for all $r,s\in\mathbf{Z}$, either $r\bmod m=s\bmod m$ or $(r\bmod m)\cap (s\bmod m)=\varnothing$;
-   if $m_1\mid m$, then for every integer $r$ we have $r+m\mathbf{Z}\subseteq r+m_1\mathbf{Z}$.

Note that congruence is an equivalence relation, so congruence classes are exactly the equivalence classes of the congruence relation.

We denote the set of all congruence classes modulo $m$ by $\mathbf{Z}_m$, i.e.

$$
\mathbf{Z}_m:=\{r\bmod m:0\leq r<m\}
$$

It is easy to see that:

-   for every integer $a$, $a+\mathbf{Z}_m=\mathbf{Z}_m$;
-   for every integer $b$ coprime to $m$, $b\mathbf{Z}_m=\mathbf{Z}_m$.

By the definition of a [quotient group](../algebra/group-theory.md#商群), $\mathbf{Z}_m=\mathbf{Z}/m\mathbf{Z}$, so sometimes we also write $\mathbf{Z}/m\mathbf{Z}$ for $\mathbf{Z}_m$.

By the [pigeonhole principle](../combinatorics/drawer-principle.md):

-   Among any $m+1$ integers there are certainly two that are congruent modulo $m$.
-   There exist $m$ integers that are pairwise incongruent modulo $m$.

From this we give the definition of a complete residue system:

???+ note "(Complete) residue system"
    For $m$ integers $a_1,a_2,\dots,a_m$, if for every number $x$ there is one and only one $a_i$ such that $x$ and $a_i$ are congruent modulo $m$, these $m$ integers $a_1,a_2,\dots,a_m$ are called a **complete residue system** modulo $m$, or simply a **residue system**.

We can also define the following systems modulo $m$:

-   the least nonnegative (complete) residue system: $0,\dots,m-1$;
-   the least positive (complete) residue system: $1,\dots,m$;
-   the absolutely least (complete) residue system: $-\lfloor m/2\rfloor,\dots,-\lfloor -m/2\rfloor-1$;
-   the greatest nonpositive (complete) residue system: $-m+1,\dots,0$;
-   the greatest negative (complete) residue system: $-m,\dots,-1$.

Unless stated otherwise, we generally use only the least nonnegative residue system.

We notice that the following proposition holds:

-   In any congruence class modulo $m$, any two integers $a_1,a_2$ from it satisfy $(a_1,m)=(a_2,m)$.

Consider the congruence class $r\bmod m$; if $(r,m)=1$, then all elements of this class are coprime to $m$, which suggests that we may learn the structure of the set of all integers coprime to $m$ in a similar way.

???+ note "Reduced congruence class"
    For a congruence class $r\bmod m$, if $(r,m)=1$, the class is called a **reduced congruence class** or **reduced residue class**.
    
    We denote the number of reduced residue classes modulo $m$ by $\varphi(m)$ and call it [Euler's totient function](./euler-totient.md).

We denote the set of all reduced congruence classes modulo $m$ by $\mathbf{Z}_m^*$, i.e.

$$
\mathbf{Z}_m^*:=\{r\bmod m:0\leq r<m,(r,m)=1\}
$$

???+ warning "Warning"
    For every integer $a$ and every integer $b$ coprime to $m$, $b\mathbf{Z}_m^*=\mathbf{Z}_m^*$, but $a+\mathbf{Z}_m^*$ is not necessarily $\mathbf{Z}_m^*$. In this respect it differs from $\mathbf{Z}_m$.

By the [pigeonhole principle](../combinatorics/drawer-principle.md):

-   Among any $\varphi(m)+1$ integers coprime to $m$ there are certainly two that are congruent modulo $m$.
-   There exist $\varphi(m)$ integers coprime to $m$ that are pairwise incongruent modulo $m$.

From this we give the definition of a reduced residue system:

???+ note "Reduced residue system"
    For $t=\varphi(m)$ integers $a_1,a_2,\dots,a_t$, if $(a_i,m)=1,~\forall 1\leq i\leq t$, and for every number $x$ satisfying $(x,m)=1$ there is one and only one $a_i$ such that $x$ and $a_i$ are congruent modulo $m$, these $t$ integers $a_1,a_2,\dots,a_t$ are called a **reduced residue system**, **restricted residue system** or **simplified residue system** modulo $m$.

Similarly, we can also define concepts such as the least nonnegative reduced residue system.

Unless stated otherwise, we generally use only the least nonnegative reduced residue system.

### Composition of residue systems

For a positive integer $m$ we have the following theorem:

-   If $m=m_1m_2,~1\leq m_1,m_2$, and $Z_{m_1},Z_{m_2}$ are **complete** residue systems modulo $m_1,m_2$ respectively, then for every $a$ coprime to $m_1$,

    $$
    Z_m=aZ_{m_1}+m_1Z_{m_2}.
    $$

    is a **complete** residue system modulo $m$. Furthermore, if $m=\prod_{i=1}^k m_i,~1\leq m_1,m_2,\dots,m_k$, and $Z_{m_1},\dots,Z_{m_k}$ are **complete** residue systems modulo $m_1,\dots,m_k$ respectively, then

    $$
    Z_m=\sum_{i=1}^k\left(\prod_{j=1}^{i-1}m_j\right)Z_{m_i}.
    $$

    is a **complete** residue system modulo $m$.

???+ note "Proof"
    It suffices to prove that for all $x,x'\in Z_{m_1}$, $y,y'\in Z_{m_2}$ satisfying $ax+m_1y\equiv ax'+m_1y'\pmod{m_1m_2}$ we have
    
    $$
    ax+m_1y=ax'+m_1y'.
    $$
    
    Indeed, from $m_1\mid m_1m_2$ we have $ax+m_1y\equiv ax'+m_1y'\pmod{m_1}$, hence $ax\equiv ax'\pmod{m_1}$, and from $(a,m_1)=1$ we get $x\equiv x'\pmod{m_1}$, so $x=x'$.
    
    Further, $m_1y\equiv m_1y'\pmod{m_1m_2}$, so $y\equiv y'\pmod{m_2}$, i.e. $y=y'$.
    
    Therefore,
    
    $$
    ax+m_1y=ax'+m_1y'.
    $$

-   If $m=m_1m_2,~1\leq m_1,m_2,(m_1,m_2)=1$, and $Z_{m_1}^*,Z_{m_2}^*$ are **reduced** residue systems modulo $m_1,m_2$ respectively, then

    $$
    Z_m^*=m_2Z_{m_1}^*+m_1Z_{m_2}^*.
    $$

    is a **reduced** residue system modulo $m$.

???+ tip "Tip"
    This theorem is equivalent to proving that Euler's totient function is a [multiplicative function](#multiplicative-functions).

???+ note "Proof"
    Let $Z_{m_1},Z_{m_2}$ be complete residue systems modulo $m_1,m_2$ respectively; we have already proved that
    
    $$
    Z_m=m_2Z_{m_1}+m_1Z_{m_2}
    $$
    
    is a complete residue system modulo $m$. Let $M=\{a\in Z_m:(a,m)=1\}\subseteq Z_m$; clearly $M$ is a reduced residue system modulo $m$, so it suffices to prove $M=Z_m^*$.
    
    Clearly $Z_m^*\subseteq Z_m$.
    
    Take any $m_2x+m_1y\in M$, where $x\in Z_{m_1}$ and $y\in Z_{m_2}$; we have $(m_2x+m_1y,m_1m_2)=1$, and from $(m_1,m_2)=1$ we get
    
    $$
    1=(m_2x+m_1y,m_1)=(m_2x,m_1)=(x,m_1),
    $$
    
    $$
    1=(m_2x+m_1y,m_2)=(m_1y,m_2)=(y,m_2).
    $$
    
    Therefore $x\in Z_{m_1}^*$ and $y\in Z_{m_2}^*$, i.e. $M\subseteq Z_m^*$.
    
    Take any $m_2x+m_1y\in Z_m^*$, where $x\in Z_{m_1}^*$ and $y\in Z_{m_2}^*$; we have $(x,m_1)=1$ and $(y,m_2)=1$, and from $(m_1,m_2)=1$ we get
    
    $$
    (m_2x+m_1y,m_1)=(m_2x,m_1)=(x,m_1)=1,
    $$
    
    $$
    (m_2x+m_1y,m_2)=(m_1y,m_2)=(x,m_2)=1,
    $$
    
    hence $(m_2x+m_1y,m_1m_2)=1$, i.e. $Z_m^*\subseteq M$.
    
    In summary,
    
    $$
    Z_m^*=m_2Z_{m_1}^*+m_1Z_{m_2}^*.
    $$
    
    is a **reduced** residue system modulo $m$.

## Number-theoretic functions

A number-theoretic function (also called an arithmetic function) is a function whose domain is the positive integers. A number-theoretic function can also be viewed as a sequence.

### Multiplicative functions

???+ note "Definition"
    In number theory, if a function $f(n)$ satisfies $f(1)=1$ and $f(xy)=f(x)f(y)$ for all coprime $x, y \in\mathbf{N}^*$, then $f(n)$ is a **multiplicative function**.
    
    In number theory, if a function $f(n)$ satisfies $f(1)=1$ and $f(xy)=f(x)f(y)$ for all $x, y \in\mathbf{N}^*$, then $f(n)$ is a **completely multiplicative function**.

#### Properties

If $f(x)$ and $g(x)$ are both multiplicative functions, then the following functions are also multiplicative:

$$
\begin{aligned}
h(x)&=f(x^p)\\
h(x)&=f^p(x)\\
h(x)&=f(x)g(x)\\
h(x)&=\sum_{d\mid x}f(d)g\left(\dfrac{x}{d}\right)
\end{aligned}
$$

For a positive integer $x$, let its unique prime factorization be $x=\prod p_i^{k_i}$, where the $p_i$ are primes.

If $F(x)$ is a multiplicative function, then $F(x)=\prod F(p_i^{k_i})$.

If $F(x)$ is a completely multiplicative function, then $F(x)=\prod F(p_i^{k_i})=\prod F(p_i)^{k_i}$.

#### Examples

-   Unit function: $\varepsilon(n)=[n=1]$. (completely multiplicative)
-   Identity function: $\operatorname{id}_k(n)=n^k$; $\operatorname{id}_{1}(n)$ is usually abbreviated as $\operatorname{id}(n)$. (completely multiplicative)
-   Constant function: $1(n)=1$. (completely multiplicative)
-   Divisor function: $\sigma_{k}(n)=\sum_{d\mid n}d^{k}$. $\sigma_{0}(n)$ is usually abbreviated as $d(n)$ or $\tau(n)$, and $\sigma_{1}(n)$ is usually abbreviated as $\sigma(n)$.
-   Euler's totient function: $\varphi(n)=\sum_{i=1}^n[(i,n)=1]$.
-   Möbius function: $\mu(n)=\begin{cases}1&n=1\\0&\exists d>1,d^{2}\mid n\\(-1)^{\omega(n)}&\text{otherwise}\end{cases}$, where $\omega(n)$ denotes the number of distinct prime factors of $n$.

### Additive functions

???+ note "Definition"
    In number theory, if a function $f(n)$ satisfies $f(1)=0$ and $f(xy)=f(x)+f(y)$ for all coprime $x, y \in\mathbf{N}^*$, then $f(n)$ is an **additive function**.
    
    In number theory, if a function $f(n)$ satisfies $f(1)=0$ and $f(xy)=f(x)+f(y)$ for all $x, y \in\mathbf{N}^*$, then $f(n)$ is a **completely additive function**.

???+ warning "Additive function"
    The additive functions in this section are the additive functions of number theory and should be distinguished from additive maps in algebra.

#### Properties

For a positive integer $x$, let its unique prime factorization be $x=\prod p_i^{k_i}$, where the $p_i$ are primes.

If $F(x)$ is an additive function, then $F(x)=\sum F(p_i^{k_i})$.

If $F(x)$ is a completely additive function, then $F(x)=\sum F(p_i^{k_i})=\sum F(p_i)\cdot k_i$.

#### Examples

For convenience, let $\mathbf P$ be the set of all primes.

-   Multiplicity of $p$ in the prime factorization: $\nu_p(n) = \max\{k\in\mathbf N: p^k\mid n\}$, where $p\in\mathbf P$. (completely additive)
-   Number of all prime factors: $\Omega(n)=\sum_{p \in\mathbf P} \nu_p(n)$. (completely additive)
-   Number of distinct prime factors: $\omega(n)=\sum_{p \in\mathbf P} [p \mid n]$.
-   Sum of all prime factors: $a_0(n)=\sum_{p \in\mathbf P} \nu_p(n)\cdot p$. (completely additive)
-   Sum of distinct prime factors: $a_1(n)=\sum_{p \in\mathbf P} [p \mid n] \cdot p$.

## Floor and ceiling functions

For a real number $x$, the **floor function** and the **ceiling function** are defined respectively as

$$
\lfloor x\rfloor = \max\{k\in\mathbf Z:k\le x\},~\lceil x\rceil = \min\{k\in\mathbf Z:k\ge x\}.
$$

Using the floor function, a real number can be decomposed into an integer part and a fractional part: $x = \lfloor x\rfloor + \{x\}$. Here $\{x\}$ denotes the fractional part of $x$.

The floor and ceiling functions have the following basic properties ($x\in\mathbf R,~n\in\mathbf Z$):

-   $x\in\mathbf Z \iff x = \lfloor x\rfloor = \lceil x\rceil$.
-   $\lceil x\rceil - \lfloor x\rfloor = [x\notin\mathbf Z]$.
-   $x - 1 < \lfloor x\rfloor \le x \le \lceil x\rceil < x + 1$.
-   $\lfloor -x\rfloor = -\lceil x\rceil,~\lceil -x\rceil = -\lfloor x\rfloor$.
-   $\lfloor x + n\rfloor = \lfloor x\rfloor + n,~\lceil x + n\rceil = \lceil x \rceil + n$.
-   $\lfloor x\rfloor$ and $\lceil x\rceil$ are both monotonically non-decreasing functions of $x$.

When proving equalities involving the floor (ceiling) function, the following equivalent forms are often used ($x\in\mathbf R,~n\in\mathbf Z$):

-   $\lfloor x\rfloor = n \iff n \le x < n + 1 \iff x - 1 < n \le x$.
-   $\lceil x\rceil = n \iff n - 1 < x \le n \iff x \le n < x + 1$.

When proving inequalities involving the floor (ceiling) function, the following equivalent forms are often used ($x\in\mathbf R,~n\in\mathbf Z$):

-   $x < n \iff \lfloor x\rfloor < n$.
-   $n < x \iff n < \lceil x\rceil$.
-   $x \le n \iff \lceil x\rceil \le n$.
-   $n \le x \iff n \le \lfloor x\rfloor$.

Properties involving sums and differences ($x,y\in\mathbf R$):

-   $\lfloor x\rfloor + \lfloor y\rfloor \le \lfloor x + y\rfloor \le \lfloor x\rfloor + \lfloor y\rfloor + 1$, and exactly one equality holds.
-   $\lceil x\rceil +\lceil y\rceil -1\leq \lceil x+y\rceil \leq \lceil x\rceil +\lceil y\rceil$, and exactly one equality holds.
-   $\lfloor|x - y|\rfloor \le |\lfloor x\rfloor - \lfloor y\rfloor| \le \lceil|x - y|\rceil$.
-   $\lfloor|x - y|\rfloor \le |\lceil x\rceil - \lceil y\rceil| \le \lceil|x-y|\rceil$.

Properties involving quotients ($x\in\mathbf R,~n\in\mathbf Z,~m\in\mathbf Z_+$):

-   $\left\lceil\dfrac{n}{m}\right\rceil = \left\lfloor\dfrac{n+m-1}{m}\right\rfloor,~\left\lfloor\dfrac{n}{m}\right\rfloor = \left\lceil\dfrac{n-m+1}{m}\right\rceil$.
-   $\left\lfloor\dfrac{x + n}{m} \right\rfloor = \left\lfloor\dfrac{\lfloor x\rfloor + n}{m} \right\rfloor,~\left\lceil\dfrac{x + n}{m} \right\rceil = \left\lceil\dfrac{\lceil x\rceil + n}{m} \right\rceil$.
-   $\left\lfloor\dfrac{\lfloor x/n\rfloor}{m}\right\rfloor = \left\lfloor\dfrac{x}{nm}\right\rfloor,~\left\lceil\dfrac{\lceil x/n\rceil}{m}\right\rceil = \left\lceil\dfrac{x}{nm}\right\rceil$.
-   For $x > 0$, $\displaystyle\left\lfloor\dfrac{x}{m}\right\rfloor = \sum_{k=1}^{\lfloor x\rfloor}[m\mid k]$.

Here the second and third properties can both be seen as direct corollaries of the following result:

-   Let $f$ be a continuous strictly increasing function such that whenever $f(x)\in\mathbf Z$ we have $x\in\mathbf Z$. Then

    $$
    \lfloor f(x)\rfloor = \lfloor f(\lfloor x\rfloor)\rfloor,~ \lceil f(x)\rceil = \lceil f(\lceil x\rceil)\rceil.
    $$

    ??? note "Proof"
        By symmetry, it suffices to prove the first equality. If $x$ is an integer, the claim is obvious. Otherwise, $\lfloor x\rfloor < x$. By the monotonicity of $f$ and of the floor function, $\lfloor f(x)\rfloor \ge \lfloor f(\lfloor x\rfloor)\rfloor$. If equality does not hold, let $y = \lfloor f(x)\rfloor$; it satisfies $\lfloor f(\lfloor x\rfloor)\rfloor < y \le \lfloor f(x)\rfloor$, which is equivalent to $f(\lfloor x\rfloor) < y \le f(x)$. By the continuity of $f$, there exists $\lfloor x\rfloor < x_0 \le x$ such that $f(x_0)=y$. Since $y\in\mathbf Z$, we have $x_0\in\mathbf Z$, which contradicts the definition of $\lfloor x\rfloor$. Hence equality holds, i.e. $\lfloor f(x)\rfloor = \lfloor f(\lfloor x\rfloor)\rfloor$.

Finally, a group of results about sums involving the floor and ceiling functions ($x\in\mathbf R,~n\in\mathbf Z,~m\in\mathbf Z_+$):

-   $n = \left\lfloor\dfrac{n}{2}\right\rfloor + \left\lceil\dfrac{n}{2}\right\rceil$.
-   $n = \left\lfloor\dfrac{n}{m} \right\rfloor + \left\lfloor\dfrac{n+1}{m} \right\rfloor + \cdots + \left\lfloor\dfrac{n+m-1}{m} \right\rfloor$.
-   $n = \left\lceil\dfrac{n}{m} \right\rceil + \left\lceil\dfrac{n-1}{m} \right\rceil + \cdots + \left\lceil\dfrac{n-m+1}{m} \right\rceil$.
-   $\lfloor mx\rfloor = \lfloor x\rfloor + \left\lfloor x+\dfrac{1}{m}\right\rfloor + \cdots + \left\lfloor x+\dfrac{m-1}{m}\right\rfloor$.
-   $\lceil mx\rceil = \lceil x\rceil + \left\lceil x - \dfrac{1}{m}\right\rceil + \cdots + \left\lceil x - \dfrac{m-1}{m}\right\rceil$.
-   When $m\perp n$, $\displaystyle\sum_{k=1}^{m-1}\left\lfloor\dfrac{kn}{m}\right\rfloor=\dfrac{1}{2}(n-1)(m-1)$.
-   When $m\perp n$, $\displaystyle\sum_{k=1}^{m-1}\left\lceil\dfrac{kn}{m}\right\rceil=\dfrac{1}{2}(n+1)(m-1)$.

The derivation of these and even more general sums of similar form can be found on the [Euclidean-like algorithm](./euclidean.md) page.

More properties and applications of the floor and ceiling functions can be found on the following pages:

-   The modulo operation: $n\bmod m = n - \left\lfloor\dfrac{n}{m}\right\rfloor m$. It can be used to [optimize integer modulo operations](./mod-arithmetic.md#related-algorithms).
-   Proving the [law of quadratic reciprocity](./quad-residue.md#二次互反律) using Gauss's lemma.
-   [Floor-division blocks](./sqrt-decomposition.md), especially the part proving its properties.
-   [Legendre's formula](./factorial.md#legendre-公式) for computing the exponent of a prime factor in a factorial.
-   [Beatty sequences](../game-theory/impartial-game.md#wythoff-游戏), Rayleigh's theorem and Wythoff's game.

## References and notes

-   潘承洞，潘承彪．初等数论．北京大学出版社．(Pan Chengdong, Pan Chengbiao. Elementary Number Theory. Peking University Press.)
-   [Floor and ceiling functions - Wikipedia](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions)
-   Graham, Ronald L., Donald E. Knuth, and Oren Patashnik. "Concrete mathematics: a foundation for computer science." (1989).

[^ref1]: [Are all primes (past 2 and 3) of the forms 6n+1 and 6n-1?](https://primes.utm.edu/notes/faq/six.html)

[^gcdcpp]: [std::gcd - cppreference.com](https://en.cppreference.com/w/cpp/numeric/gcd)
