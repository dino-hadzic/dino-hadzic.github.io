---
title: Ring theory
---

Prerequisites: [Basic concepts of abstract algebra](./basic.md), [Group theory](./group-theory.md)

## Introduction

**Ring theory** studies rings of all kinds.

The parts of ring theory covered in this article are inseparable from the theory of divisibility in number theory. First, analogously to normal subgroups in group theory, this article introduces the kernel of a ring homomorphism, which is called an ideal of the ring; this is in fact a generalization of the concept of a number in number theory to general rings. Then, generalizing concepts from the ring of integers such as primes, the Euclidean algorithm and prime factorization to general rings yields the concepts of various types of integral domains.

Many results from number theory still hold in other common rings. One could say that part of the work of ring theory consists in discussing whether these results from number theory hold in general rings, and if not, what restrictions must be imposed on the ring for them to hold.

???+ info "Notation"
    When there is no risk of ambiguity, this article may omit the multiplication symbol of a ring and write the ring $(R,+,\cdot)$ as the ring $R$. In a ring $R$, the additive identity is also called the zero element and denoted by $0$; the multiplicative identity is also called the unity (identity element) and denoted by $1$.

??? warning "The definition of a ring in this article does not require a unity"
    Note that the definition of a ring in this article does not require a unity. Some texts require a unity in the definition of a ring; in that case the statements of some results in this article need slight adjustments. For example, in this article ideals can be defined in terms of subrings, whereas in other texts they may need to be defined in terms of additive subgroups.

## Ideals

Analogously to the case of groups, the concepts of subrings and ring homomorphisms can be established.

???+ abstract "Subring"
    For a ring $(R,+,\cdot)$ and a subset $S$ of it, if $(S,+,\cdot)$ is also a ring, then $S$ is called a **subring** of $R$.

???+ example "Example: the ring of integers $\mathbf Z$"
    For any integer $n$, the set $n\mathbf Z=\{nk:k\in\mathbf Z\}$ is a subring of $\mathbf Z$.

???+ abstract "Ring homomorphism"
    For rings $(R,+,\cdot)$ and $(S,\oplus,\odot)$, if a map $\pi$ preserves the addition and multiplication of the rings, that is, $\pi(r_1+r_2)=\pi(r_1)\oplus\pi(r_2)$ and $\pi(r_1\cdot r_2)=\pi(r_1)\odot\pi(r_2)$ hold for all $r_1,r_2\in R$, then the map $\pi:R\rightarrow S$ is called a **homomorphism** from the ring $R$ to the ring $S$.

??? info "The case where the definition of a ring requires a unity"
    If the definition of a ring requires a unity, then the definition of a ring homomorphism often also requires that the unity be mapped to the unity. For homomorphisms between nonzero rings with unity, this extra requirement merely guarantees that the homomorphism does not map the whole ring with unity to the zero element.

???+ example "Example: the ring of integers $\mathbf Z$ (continued)"
    The map of reduction modulo any nonzero integer $n$, that is, $\pi:\mathbf Z\rightarrow\mathbf Z/n\mathbf Z$ with $\pi(a)=\bar a$, is a ring homomorphism.

The [discussion](./group-theory.md#群同态) of the kernel and image of a group homomorphism can be carried over here almost verbatim. The (relative) size of the image of a homomorphism determines whether the homomorphism is surjective, while the triviality or not of the kernel of a homomorphism determines whether the homomorphism is injective. The kernel of a ring homomorphism is defined as follows:

???+ abstract "Kernel of a homomorphism"
    The **kernel** of a homomorphism $\pi:R\rightarrow S$ from the ring $R$ to the ring $S$ is $\{r\in R:\pi(r)=0\}$, denoted by $\ker\pi$, where $0$ is the additive identity of $S$.

Clearly, the kernel and image of a ring homomorphism are both subrings. Conversely, not every subring can be the kernel of some ring homomorphism. The subrings that can be kernels of ring homomorphisms are called ideals of the ring.

???+ abstract "Ideal"
    For a ring $R$ and a subring $I$ of it, $I$ is called, in the ring $R$, a
    
    -   **left ideal** if $rI\subseteq I$ for all $r\in R$, where $rI=\{ra:a\in I\}$;
    -   **right ideal** if $Ir\subseteq I$ for all $r\in R$, where $Ir=\{ar:a\in I\}$;
    -   **ideal** if $I$ is both a left ideal of $R$ and a right ideal of $R$.

Here the ideal $I$ is required to be closed under both left and right multiplication by elements of the ring $R$. This condition is natural. Indeed, the elements of an ideal are mapped to the zero element under a ring homomorphism, and multiplying any element by zero, on the left or on the right, should give zero; this is precisely the closure that is required. Moreover, since the additive structure of a ring is an abelian group, every subgroup is normal; and the multiplicative structure of a ring is very primitive and imposes no additional restrictions on substructures. This shows that closure under left and right multiplication is also sufficient.

???+ example "Example: the ring of integers $\mathbf Z$ (continued)"
    As an example, the subring $n\mathbf Z$ mentioned earlier is in fact an ideal of $\mathbf Z$. It is the set of all multiples of $n$. The product of a multiple of $n$ with any integer is again a multiple of $n$. In fact, all ideals of $\mathbf Z$ are of this form; such a ring is called a [principal ideal domain](#principal-ideal-domains). In a general ring, some ideals are not the set of multiples of some element; the existence of such general rings was precisely the original motivation for studying ideals (rather than simply multiples)[^ideal-history].

### Quotient rings

As with groups, based on an ideal of a ring one can define the **quotient ring** on the set of all cosets (in the sense of the additive group). Consider the set

$$
R/I=\{a+I:a\in R\},
$$

where the coset $a+I=\{a+b:b\in I\}$. It can be shown that, if and only if $I$ is an ideal, the operations

$$
\begin{aligned}
(a+I)+(b+I)&=(a+b)+I,\\
(a+I)(b+I)&=(ab)+I
\end{aligned}
$$

are well defined, that is, the results of these operations do not depend on the choice of representatives of the cosets. Under these operations, $R/I$ forms a ring. Again in accordance with the case of groups, the **first isomorphism theorem** for rings can be established, and there is a natural homomorphism from a ring to its quotient ring. These show that ideals of rings and normal subgroups of groups play the same role in the homomorphisms of the respective structures.

???+ note "First isomorphism theorem"
    Let $\pi:R\rightarrow S$ be a homomorphism from the ring $R$ to the ring $S$. Then $\ker\pi$ is an ideal of $R$, and $R/\ker\pi\cong\pi(R)$ is a subring of $S$.

???+ abstract "Natural homomorphism"
    For a ring $R$ and an ideal $I$ of it, the map $\pi:R\rightarrow R/I$ given by $\pi(r)=r+I$ is a surjective homomorphism from $R$ to $R/I$, called the **natural homomorphism** from the ring $R$ to the quotient ring $R/I$.

???+ example "Example: the ring of integers $\mathbf Z$ (continued)"
    As an example, the ring $\mathbf Z/n\mathbf Z$ of congruence classes of integers modulo $n$ is the quotient ring of $\mathbf Z$ by its ideal $n\mathbf Z$. This also explains the meaning of the notation $\mathbf Z/n\mathbf Z$. The map modulo $n$ mentioned above, $\pi:\mathbf Z\rightarrow\mathbf Z/n\mathbf Z$, is exactly the natural map mentioned here, and the corresponding kernel is precisely the ideal $n\mathbf Z$.

In the case of rings, the other isomorphism theorems hold as well.

???+ note "Second isomorphism theorem"
    Let the ring $R$ have a subring $A$ and an ideal $B$. Then $A+B=\{a+b:a\in A,b\in B\}$ is also a subring of $R$, $A\cap B$ is an ideal of $A$, $B$ is an ideal of $A+B$, and $(A+B)/B\cong A/(A\cap B)$.

???+ note "Third isomorphism theorem"
    Let the ring $R$ have ideals $I,J$ with $I\subseteq J$. Then $J/I$ is also an ideal of $R/I$, and $(R/I)/(J/I)\cong R/J$.

???+ note "Correspondence theorem"
    Let the ring $R$ have an ideal $I$. Then there is a bijection $\varphi:\mathcal S\rightarrow\mathcal T$ between the set of all subrings of $R$ containing $I$, $\mathcal S=\{S:I\subseteq S\subseteq R\}$, and the set of all subrings of the quotient ring $R/I$, $\mathcal T=\{T:T\text{ is a subring of }R/I\}$, which maps $S\in\mathcal S$ to $S/I\in\mathcal T$. This bijection preserves the inclusion relation between subrings, and ideals of $R$ are always mapped to ideals of $R/I$.

These theorems will play a fundamental role in the discussion of the structure of rings and ideals below.

### Operations on ideals

Various operations can be defined on the ideals of a ring. This is similar to how concepts such as the greatest common divisor and the least common multiple can be defined on the divisibility structure of the integers.

???+ abstract "Operations on ideals"
    Let the ring $R$ have ideals $I,J$. The following operations can be defined:
    
    -   the **sum** of ideals: $I+J=\{a+b:a\in I,b\in J\}$;
    -   the **product** of ideals: $IJ=\{\sum_{i=1}^na_ib_i:a_i\in I,b_i\in J\}$, that is, the set of all finite sums of products of the form $ab$;
    -   the **intersection** of ideals: $I\cap J$.

It is easy to verify that the results of these operations are still ideals of the ring.

???+ example "Example: the ring of integers $\mathbf Z$ (continued)"
    Consider the case of the ring of integers $\mathbf Z$. For the ideals $n\mathbf Z$ and $m\mathbf Z$, we get
    
    $$
    \begin{aligned}
    n\mathbf Z+m\mathbf Z&=\gcd(m,n)\mathbf Z,\\
    (n\mathbf Z)(m\mathbf Z)&=(mn)\mathbf Z,\\
    (n\mathbf Z)\cap(m\mathbf Z)&=\mathrm{lcm}(m,n)\mathbf Z.
    \end{aligned}
    $$

In general, for a ring $R$ and its ideals $I$ and $J$, we always have

$$
IJ\subseteq I\cap J\subseteq I,J\subseteq I+J.
$$

Using these definitions, the Chinese remainder theorem for integers can be generalized to general rings. But before that, concepts such as primes and coprimality also need to be generalized to general rings.

### Maximal ideals

The properties of a ring can be understood through the structure of its ideals.

A nonzero ring $R$ always has two trivial ideals, namely $\{0\}$ and $R$. If the ring $R$ is moreover a commutative nonzero ring with unity, then a ring with only these two ideals is a field, and only a field has this property[^simple-ring].

???+ note "Theorem"
    Let $R$ be a commutative nonzero ring with unity. Then $R$ is a field if and only if $R$ has only the trivial ideals $\{0\}$ and $R$.

??? note "Proof"
    If $R$ is a field, then for any nonzero ideal $I$ we can take an arbitrary nonzero element $a\in I$; then any element $r\in R$ of the field satisfies $r=(ra^{-1})a\in (ra^{-1})I\subseteq I$, hence $I=R$. Conversely, for any $a\in R$ with $a\neq 0$, one can verify that $aR=\{ar:r\in R\}$ is an ideal, which must equal $R$, so there exists $b\in R$ such that $ab=1$; this shows that $a$ has an inverse, hence $R$ is a field.

The commutativity condition here is necessary; otherwise, one would need to require both the left and the right ideals to be trivial in order to guarantee that the ring is a division ring.

This result can be generalized to the case where the ring itself is not a field. But then one has to consider quotient rings instead and discuss the conditions under which a quotient ring of a commutative nonzero ring with unity is a field. The quotient ring $R/I$ being a field means that the quotient ring $R/I$ has only trivial ideals; by the correspondence theorem, this means that in the original ring $R$ there is no ideal strictly between the ideal $I$ being quotiented out and the original ring $R$. Such an ideal $I$ is called a maximal ideal.

???+ abstract "Maximal ideal"
    For a ring $R$ and an ideal $M$ of it, if $M\neq R$ and the only ideals of $R$ containing $M$ are $M$ and $R$, then the ideal $M$ is called a **maximal ideal**.

???+ note "Theorem"
    Let the commutative nonzero ring with unity $R$ have an ideal $M$. Then the quotient ring $R/M$ is a field if and only if $M$ is a maximal ideal.

???+ example "Example: the ring of integers $\mathbf Z$ (continued)"
    For example, the ideal $n\mathbf Z$ of the ring of integers $\mathbf Z$ is maximal if and only if $n$ is a prime. For a prime $p$, the quotient ring $\mathbf Z/p\mathbf Z$ is a field, also denoted by $\mathbf F_p$.

Not every ring has a maximal ideal, but a nonzero ring with unity always has a maximal ideal.

???+ note "Theorem (Krull)"
    For an ideal $I\neq R$ of a nonzero ring with unity $R$, there always exists a maximal ideal $M$ of $R$ such that $I\subseteq M$.

??? note "Proof"
    The idea is to use Zorn's lemma. Consider the set $\mathcal S$ of all proper ideals of $R$ (that is, ideals not equal to $R$) containing $I$. Since $I\in\mathcal S$, it is nonempty, and it forms a partially ordered set under inclusion. For any chain $J_0\subseteq J_1\subseteq\cdots\subseteq J_n\subseteq\cdots$ in it, let $J$ be their union; it is easy to verify that this is also an ideal. Moreover, $J\neq R$, for otherwise $1\in J$, that is, there would exist $n$ such that $1\in J_n$, contradicting the fact that $J_n$ is a proper ideal. Therefore, by Zorn's lemma, there exists a maximal ideal $M\supseteq I$.

A maximal ideal is the analogue of an irreducible element in the theory of divisibility. This is because the inclusion relation between ideals corresponds to the divisibility relation between integers; having no ideal as a superset corresponds to having no factor that divides it. However, the concept of a maximal ideal is broader than that of an irreducible element, because not all ideals are principal.

### Prime ideals

The condition of being a field is stricter than that of being an integral domain. Ideals that ensure the quotient ring is an integral domain are called prime ideals; they are analogous to the concept of primes in the theory of divisibility.

???+ abstract "Prime ideal"
    For a commutative ring $R$ and an ideal $P$ of it, if $P\neq R$ and for any elements $a,b\in R$ of the ring, whenever $ab\in P$ holds we always have $a\in P$ or $b\in P$, then the ideal $P$ is called a **prime ideal**.

This definition may look somewhat abrupt, but compared with the [definition of a prime](../number-theory/basic.md#fundamental-theorem-of-arithmetic), this definition of a prime ideal is natural as well.

???+ note "Theorem"
    Let the commutative nonzero ring with unity $R$ have an ideal $P$. Then the quotient ring $R/P$ is an integral domain if and only if $P$ is a prime ideal.

??? note "Proof"
    For a commutative nonzero ring with unity $R$, the quotient ring $R/P$ is an integral domain if and only if $R/P$ has no zero divisors. Denote the coset $a+P$ by $\bar a$. That the quotient ring $R/P$ has no zero divisors is equivalent to: $\bar a\bar b=\bar 0$ always implies $\bar a=\bar 0$ or $\bar b=\bar 0$. By the definition of the quotient ring, this is equivalent to: $ab\in P$ always implies $a\in P$ or $b\in P$.

In the ring of integers $\mathbf Z$, $n\mathbf Z$ is a maximal ideal if and only if $n$ is a prime, while $n\mathbf Z$ is a prime ideal if and only if $n$ is a prime or $n=0$. In a general commutative ring, a maximal ideal is always a prime ideal, but the converse need not hold, of course; this can be seen from the properties of the corresponding quotient rings.

???+ note "Theorem"
    For a commutative nonzero ring with unity $R$, every maximal ideal of it is necessarily a prime ideal.

We will see later that the converse holds only in rings with sufficiently good properties, sufficiently similar to the ring of integers.

### Principal ideals

Analogously to the concept of subgroups, in the discussion of rings one often needs to consider the ideal generated by some subset.

???+ abstract "Ideal generated by a subset"
    For a nonzero ring with unity $R$ and a nonempty subset $A\subseteq R$ of it, if $I$ is the smallest (with respect to inclusion) among the ideals of $R$ containing $A$, then the ideal $I$ is called the **ideal generated by the subset $A$** and denoted by $(A)$. In this case, $A$ is called a **generating set** of $(A)$.

???+ abstract "Principal ideal"
    An ideal generated by a single element $a\in R$ is called a **principal ideal** and denoted by $(a)$. In this case, $a$ is called a **generator** of $(a)$.

For a set $A$, one can give a construction of the ideal it generates. First, define

$$
\begin{aligned}
RA&=\{r_1a_1+\cdots+r_na_n:r_i\in R,a_i\in A,n\in\mathbf N_+\},\\
AR&=\{a_1r_1+\cdots+a_nr_n:r_i\in R,a_i\in A,n\in\mathbf N_+\}.
\end{aligned}
$$

These are in fact the left ideal and the right ideal generated by $A$, respectively. Then the ideal generated by the subset $A$ is exactly $RAR$. For commutative rings, all of these structures coincide.

All ideals $n\mathbf Z$ of the ring of integers are principal ideals; below they are often denoted by $(n)$.

## Integral domains

An integral domain is a commutative nonzero ring with unity and without zero divisors. This concept is precisely the generalization of the ring of integers. However, a ring obtained this way need not have properties good enough to allow every result of the theory of divisibility of integers to be carried over verbatim. In order to generalize results from number theory, further restrictions can be imposed on integral domains. Among them, the three most common kinds of integral domains are Euclidean domains, principal ideal domains and unique factorization domains; each of these concepts is strictly contained in the next.

### Divisibility relation

First, the relevant concepts of the theory of divisibility of integers are generalized here to general commutative rings.

???+ abstract "Divisibility"
    Let the commutative ring $R$ have elements $a,b\in R$. If there exists $x\in R$ such that $a=bx$, then $b$ is said to **divide** $a$, written $b\mid a$. In this case, $b$ is called a **divisor** of $a$.

???+ abstract "Associates"
    Let the commutative ring $R$ have elements $a,b\in R$. If they differ only by an invertible element, that is, there exists an invertible element $u\in R$ such that $a=bu$, then $a$ and $b$ are said to be **associates**.

The divisibility relation is a [partial order](../order-theory.md#二元关系) on the ring, and the associate relation is an equivalence relation on the ring. From the point of view of ideals, $a\mid b$ is equivalent to $(b)\subseteq (a)$, and $a$ and $b$ being associates is equivalent to $(a)=(b)$. Therefore, when discussing elements of a ring, one usually does not care about the difference between associates. Similarly to the case of integers, the greatest common divisor of $a$ and $b$ in a commutative ring is defined as the infimum of $\{a,b\}$.

???+ abstract "Greatest common divisor"
    For a commutative ring $R$ and its elements $a,b\in R$, if there exists a nonzero element $d\in R$ satisfying $d\mid a$ and $d\mid b$, and such that $d'\mid d$ holds for any $d'$ satisfying $d'\mid a$ and $d'\mid b$, then $d$ is called a **greatest common divisor** of $a$ and $b$, written $\gcd(a,b)$.

In an integral domain, the greatest common divisor is uniquely determined up to associates. The discussion below is restricted to integral domains.

In an integral domain, a concept similar to primes can also be established. In the theory of integers, there are two equivalent definitions of a prime, but in a general integral domain these two definitions correspond to different concepts:

???+ abstract "Prime element"
    Let the integral domain $R$ have a nonzero element $p\in R$. If $(p)$ is a prime ideal, that is, $p$ is not invertible and $p\mid ab$ always implies $p\mid a$ or $p\mid b$, then $p$ is called a **prime** (prime element).

???+ abstract "Irreducible element"
    Let the integral domain $R$ have a nonzero element $r\in R$. If $r$ is not invertible, and for any $a,b\in R$ with $r=ab$ either $a$ or $b$ is invertible, then $r$ is called an **irreducible** (irreducible element), or $r$ is said to be irreducible. Conversely, if $r=ab$ with $a,b\in R$ both not invertible, then $r$ is said to be reducible.

It can be shown that the principal ideal $(r)$ corresponding to an irreducible element $r$ is necessarily maximal among all proper principal ideals of the ring; however, in a general integral domain not all ideals are principal, so the concepts of irreducible element and maximal ideal are not equivalent.

Analogously to the proof that in a principal ideal domain every prime ideal is maximal, the following result can be proved in general:

???+ note "Theorem"
    Let $R$ be an integral domain. If $a\in R$ is a prime, then $a$ is necessarily also an irreducible.

??? note "Proof"
    Let $r\in R$ be a prime, and let $a,b\in R$ satisfy $r=ab$. Since $r$ is prime, we may assume $r\mid a$ holds; then $a=cr=cba$. Since the cancellation law holds in an integral domain, we have $1=bc$, so $b$ has the inverse $c$. This shows that $r$ is irreducible.

The converse does not hold.

??? example "Counterexample"
    In the quadratic integer ring $\mathbf Z[\sqrt{-5}]$, $3$ is irreducible, but $9=3\cdot 3=(2+\sqrt{-5})(2-\sqrt{-5})$, so it is not prime.
    
    Here we give the proof of this counterexample; readers unfamiliar with quadratic integer rings should first read the section [Quadratic integer rings](#example-quadratic-integer-rings). Let $N(\cdot)$ be the norm on the quadratic integer ring. For any factorization $3=ab$ we have $N(a)N(b)=N(3)=9$. If $a,b$ are both not invertible, then $N(a)$ and $N(b)$ are both greater than $1$, so necessarily $N(a)=N(b)=3$. But there are no such elements in $\mathbf Z[\sqrt{-5}]$, that is, $x^2+5y^2=3$ has no integer solutions. This shows that $3$ is irreducible. As for $3$ not being prime, one needs to show that $3$ does not divide $2\pm\sqrt{-5}$, which is obvious.

### Euclidean domains

Related reading: [(Extended) Euclidean algorithm](../number-theory/gcd.md), [Bézout's identity](../number-theory/bezouts.md)

A Euclidean domain is an integral domain in which successive division (that is, the Euclidean algorithm) can be performed.

???+ abstract "Euclidean domain"
    For an integral domain $R$, if there exists a map $N:R\setminus\{0\}\rightarrow\mathbf N$ such that for any $a,b\in R$ with $b\neq 0$ there exist $q,r\in R$ such that $a=qb+r$ holds with $r=0$ or $N(r)<N(b)$, then the integral domain $R$ is called a **Euclidean domain** (ED). The map $N$ is called the norm of the elements of the Euclidean domain.

??? info "Other equivalent definitions"
    The definition adopted in this article defines the norm only at nonzero elements. Different texts may treat the definition of a Euclidean domain differently. For example, some texts may additionally define $N(0)=0$; but the value $N(0)$ is not used in the subsequent division with remainder, so this is immaterial. As another example, the definition on [Wikipedia](https://en.wikipedia.org/wiki/Euclidean_domain) further requires the norm $N$ to satisfy the property that $N(a)\le N(ab)$ for any nonzero $a,b\in R$. However, it is easy to verify that if a Euclidean domain $R$ has a norm $N(\cdot)$ satisfying the property required by the definition in this article, then one can define the norm $N'(a)=\min_{b\in R\setminus\{0\}} N(ab)$, which satisfies the additional property $N'(a)\le N'(ab)$. Therefore, these different definitions are all equivalent.

This definition is in fact a generalization of division with remainder for integers. The existence of the norm makes it possible to measure the relative size of the remainder and the divisor. Thus, during successive division, the norm of the corresponding remainders keeps decreasing; since the norm takes values in the natural numbers, such a process must end at $r=0$. In this way, we obtain the Euclidean algorithm in a Euclidean domain.

Being able to perform the Euclidean algorithm means that greatest common divisors can be computed efficiently in a Euclidean domain. In complete analogy with the theory of divisibility of integers, one can prove that the result of the Euclidean algorithm is necessarily a greatest common divisor, and that Bézout's identity holds, where the coefficients can be determined by the extended Euclidean algorithm.

???+ note "Theorem"
    For a Euclidean domain $R$ and its elements $a,b\in R$, the result $d$ of applying the Euclidean algorithm to $a$ and $b$ is a greatest common divisor of $a$ and $b$, and there exist $x,y\in R$ such that $d=ax+by$ holds; conversely, any element of the form $ax+by$ is a multiple of $d$.

Note that, in the language of ring theory, all elements of the form $ax+by$ are exactly the elements of the ideal $(a,b)$, and this theorem says that $(a,b)$ is necessarily the principal ideal $(d)$.

In fact, every ideal in a Euclidean domain is principal.

???+ note "Theorem"
    Every ideal in a Euclidean domain is a principal ideal.

??? note "Proof"
    Let $R$ be a Euclidean domain and $I$ an ideal of it. If $I=\{0\}$, it is obviously principal. Let $I$ be a nonzero ideal. By definition, there is a norm $N(\cdot)$ on the ring $R$, so we can take a nonzero element $d$ of $I$ with the smallest norm. Then for any $a\in I$ we have $a=qd+r$ with $r=0$ or $N(r)< N(d)$. Since $r=a-qd\in I$, by the way $d$ was chosen we get $r=0$, that is, $a=qd\in (d)$. This shows that $I$ is necessarily a principal ideal.

### Principal ideal domains

An integral domain in which all ideals are principal is called a principal ideal domain. This is a class of integral domains with rather good properties, and also a very common one. In these integral domains, the concept of an ideal of the ring is equivalent to the concept of multiples in the integers.

???+ abstract "Principal ideal domain"
    For an integral domain $R$, if every ideal of it is principal, then it is called a **principal ideal domain** (PID).

Therefore, the last theorem of the previous section can be restated as follows:

???+ note "Theorem"
    Every Euclidean domain is a principal ideal domain.

In a principal ideal domain, maximal ideals are equivalent to ideals generated by irreducible elements. Just as primes and irreducibles are equivalent in the integers, in a principal ideal domain these two concepts are also equivalent, so maximal ideals and prime ideals are completely equivalent as well.

???+ note "Theorem"
    Let the principal ideal domain $R$ have a nonzero ideal $I$. Then $I$ is a prime ideal if and only if $I$ is a maximal ideal.

??? note "Proof"
    It suffices to show that every prime ideal is maximal. Let the principal ideal domain $R$ have a nonzero prime ideal $(p)$, and at the same time an ideal $(a)$ satisfying $(p)\subseteq(a)\subseteq R$. This means $a\mid p$, so there exists $b\in R$ such that $p=ab$. But since $(p)$ is a prime ideal, $ab\in(p)$ implies $a\in(p)$ or $b\in(p)$. If $a\in(p)$, then $(a)\subseteq (p)$, hence $(a)=(p)$; if $b\in(p)$, then $b=cp$, hence $p=acp$, and since $p\neq 0$, we have $1=ac$, that is, $a$ has the inverse $c$, so $(a)=R$. This shows that $(p)$ is a maximal ideal.

???+ note "Corollary"
    Let the principal ideal domain $R$ have a nonzero element $r$. Then $r$ is a prime if and only if $r$ is an irreducible.

The analysis of Bézout's identity in the previous section can be transferred to principal ideal domains.

???+ note "Theorem"
    Let $R$ be a principal ideal domain, and let $a,b\in R$ be nonzero elements. Let $d\in R$ be a generator of the ideal $(a,b)$. Then the greatest common divisor of $a$ and $b$ is $d$, unique up to associates; moreover, there exist $x,y\in R$ such that $ax+by=d$ holds.

That is, [Bézout's identity](../number-theory/bezouts.md) still holds in a principal ideal domain. Although greatest common divisors exist in both, the biggest difference between Euclidean domains and principal ideal domains is that in the former the greatest common divisor can be computed efficiently by the Euclidean algorithm, whereas in a principal ideal domain there is generally no such efficient algorithm.

### Unique factorization domains

A concept more general than principal ideal domains is that of unique factorization domains. The unique factorization theorem for integers is called the [fundamental theorem of arithmetic](../number-theory/basic.md#fundamental-theorem-of-arithmetic). A similar unique factorization theorem actually still holds in some integral domains that are not principal ideal domains. Such integral domains are called unique factorization domains.

???+ abstract "Unique factorization domain"
    For an integral domain $R$, if every nonzero non-invertible element $r$ can be written in the form $r=p_1\cdots p_n$, where $p_1,\cdots,p_n$ are irreducibles that may repeat, and such a factorization is unique up to associates and reordering, then the integral domain $R$ is called a **unique factorization domain** (UFD).

The fundamental theorem of arithmetic says that the ring of integers $\mathbf Z$ is a unique factorization domain.

Earlier we gave a counterexample of an irreducible that is not prime; in the integral domain $\mathbf Z[\sqrt{-5}]$ involved there, the unique factorization theorem no longer holds. However, in all unique factorization domains, irreducibles and primes are equivalent.

???+ note "Theorem"
    For a unique factorization domain $R$ and a nonzero element $a\in R$ of it, $a$ is a prime if and only if $a$ is an irreducible.

??? note "Proof"
    It suffices to show that every irreducible is prime. For an irreducible $r$, if $r\mid ab$, then there exists $c\in R$ such that $ab=rc$ holds. Since $R$ is a unique factorization domain, $a,b,c\in R$ can all be factored into products of irreducibles. Comparing the two sides, by the uniqueness of factorization, $r$ must be an associate of some irreducible factor of $a$ or $b$, so $r$ divides one of $a$ and $b$. This shows that $r$ is also prime.

All principal ideal domains are unique factorization domains.

???+ note "Theorem"
    Every principal ideal domain is a unique factorization domain.

??? note "Proof"
    Let $R$ be a principal ideal domain, and let $r\in R$ be neither zero nor invertible. To show that $r$ can be uniquely factored into a product of a sequence of irreducibles, we proceed in two steps: first prove the existence of the factorization, then prove its uniqueness.
    
    The existence of the factorization is rather natural. If $r$ is already irreducible, there is no need to factor further; otherwise, there necessarily exist $r_1,r_2$ such that $r=r_1r_2$ with $r_1,r_2$ both not invertible. Further, if $r_1$ and $r_2$ are both irreducible, there is again no need to factor further; otherwise, whichever of $r_1$ and $r_2$ is not irreducible can be factored further, and $r$ can be written as a product of more elements. Thus, as long as not all factors in the product are irreducible, the factorization process can be continued. The factorization necessarily terminates after finitely many steps. Otherwise, the axiom of choice guarantees that one can extract from $R$ an infinite chain of elements $\{r_{(i)}\}_{i=0}^\infty$ with $r_{(0)}=r$ and $r_{(i+1)}\mid r_{(i)}$ for all $i\in\mathbf N$, where all these divisibility relations are strict, that is, there are no associates in the chain. In the language of ideals, this corresponds to a strictly increasing infinite sequence of ideals $I_{0}\subset I_{1}\subset \cdots\subset I_{i}\subset\cdots\subset R$, where $I_i=(r_{(i)})$. It is easy to verify that the union of these ideals $I=\bigcup_{i=0}^\infty I_i$ is still an ideal, hence necessarily principal. Let $a$ be a generator of the principal ideal $I$; then there exists $n\in\mathbf N$ with $a\in I_n$. Therefore, $I=(a)\subseteq I_n$. This shows that such a strictly increasing infinite sequence of ideals does not exist, hence the above factorization process necessarily terminates within finitely many steps.
    
    Next we prove the uniqueness of the factorization. We can use induction on the number of factors in the factorization. The key step of the induction is to verify that if $r=p_1p_2\cdots p_n=q_1q_2\cdots q_m$ and $n\le m$, then $p_1$ is necessarily an associate of some $q_j$. Here we need the earlier result: in a principal ideal domain, every irreducible is prime. We know that $p_1$ is an irreducible in $R$, so it is also prime, and for the product on the right-hand side one can show inductively that there necessarily exists some element $q_j$ such that $p_1\mid q_j$. Therefore, there exists $c\in R$ such that $q_j=p_1c$, and since $q_j$ is irreducible and $p_1$ is irreducible, by definition $c$ can only be invertible, hence $p_1$ is an associate of $q_j$. Then, using the cancellation law, $p_1$ and $q_j$ can be cancelled on the left and right sides respectively, and the invertible element by which they differ can be multiplied into any of the remaining elements. By the induction hypothesis, $p_2\cdots p_n$ and $q_1\cdots q_{j-1}q_{j+1}\cdots q_m$ necessarily have the same number of irreducibles, and they are the same up to associates. This proves the theorem.

Finally, the existence of greatest common divisors still holds in unique factorization domains.

???+ note "Theorem"
    Let the unique factorization domain $R$ have nonzero elements $a,b\in R$ that can be factored in the form $a=up_1^{r_1}\cdots p_n^{r_n}$ and $b=vp_1^{s_1}\cdots p_n^{s_n}$, where $u,v$ are invertible, $p_1,\cdots,p_n$ are pairwise distinct irreducibles, and $r_i,s_i$ are natural numbers. Then one of their greatest common divisors is $d=p_1^{\min\{r_1,s_1\}}\cdots p_n^{\min\{r_n,s_n\}}$.

This actually shows that the property of greatest common divisors existing is weaker than the unique factorization theorem holding[^gcd-domain].

### Example: quadratic integer rings

Related reading: [Quadratic fields](../number-theory/quadratic.md)

An understanding of abstract algebra cannot do without examples. It was precisely because the research on Fermat's Last Theorem required studying the properties of a class of algebraic integers that today's ring theory gradually developed[^ring-theory-history]. Here we discuss the simplest algebraic integers, namely quadratic integers. The proofs of many results in this part require sophisticated knowledge of algebraic number theory and are therefore omitted.

A **quadratic integer** is a complex root of a quadratic equation $\alpha^2+b\alpha+c=0$ with integer coefficients and leading coefficient one. All quadratic integers, and only they, have the form

$$
\alpha=a+b\omega,~(a,b\in\mathbf Z)
$$

where

$$
\omega=\begin{cases}
\dfrac{1+\sqrt{D}}{2},& D\equiv 1\pmod 4,\\
\sqrt D,& D\equiv 2,3\pmod 4,
\end{cases}
$$

in which $D$ is squarefree.

??? note "Analysis"
    By the quadratic formula, we know that a root of this equation can necessarily be written as
    
    $$
    \alpha=\frac{-b\pm\sqrt{b^2-4c}}{2}.
    $$
    
    When $b=2k+1$ is odd, this root can be written as
    
    $$
    \alpha=-k-\frac{1\pm\sqrt{4(k^2+k-c)+1}}{2}.
    $$
    
    Otherwise, when $b=2k$ is even, this root can be written as
    
    $$
    \alpha=-k\pm\sqrt{k^2-c}.
    $$
    
    From this one concludes that quadratic integers necessarily have the above form.

It is easy to verify that for such $\omega$, the set $\mathbf Z[\omega]=\{a+b\omega:a,b\in\mathbf Z\}$ forms a ring. This is called a **quadratic integer ring**, and its field of fractions is exactly the quadratic field $\mathbf Q(\sqrt D)$. When $D>0$, all quadratic integers are real, so it is also called a **real quadratic integer ring**; when $D<0$, all quadratic integers other than the integers are complex, so it is also called an **imaginary quadratic integer ring**.

All quadratic integer rings $\mathbf Z[\omega]$ are integral domains. Among them, when $D=-1$, $\mathbf Z[\sqrt{-1}]$ (also written $\mathbf Z[\mathrm{i}]$) is also called the ring of Gaussian integers; when $D=-3$, $\mathbf Z\left[\dfrac{1+\sqrt{-3}}{2}\right]$ is called the ring of Eisenstein integers.

For a quadratic integer $a+b\omega$, its **conjugate** can be defined as $a+b\bar\omega$, where

$$
\bar\omega=\begin{cases}
\dfrac{1-\sqrt{D}}{2},& D\equiv 1\pmod 4,\\
-\sqrt D,& D\equiv 2,3\pmod 4,
\end{cases}
$$

Note that since quadratic integers are real when $D>0$, the concept of conjugate here does not fully coincide with the concept of the conjugate of a complex number, but both are special cases of the concept of conjugates of algebraic elements in field theory. Conjugate quadratic integers are roots of the same quadratic equation with integer coefficients.

On a quadratic integer ring one can define the **norm**

$$
\begin{aligned}
N(a+b\omega)&=(a+b\omega)(a+b\bar\omega)\\
&=\begin{cases}
a^2+ab+\dfrac{1-D}{4}b^2,& D\equiv 1\pmod 4,\\
a^2-Db^2,& D\equiv 2,3\pmod 4.
\end{cases}
\end{aligned}
$$

The norm of a quadratic integer is always an integer. In particular, when $D<0$, the norm is always a natural number. The norm preserves the multiplicative structure, that is, $N(ab)=N(a)N(b)$.

The invertible elements (units) in a quadratic integer ring are exactly those elements whose norm is $\pm1$. For the case $D>0$, this amounts to considering the solutions of the [Pell equation](../number-theory/pell-equation.md) $x^2-Dy^2=\pm1$ or $x^2-Dy^2=\pm4$. For the case $D<0$, it is easy to verify that, apart from the two special cases where the invertible elements in the ring of Gaussian integers $\mathbf Z[\rm{i}]$ are $\{\pm1,\pm\rm{i}\}$ and the invertible elements in the ring of Eisenstein integers $\mathbf Z[\omega]$ are $\{\pm1,\pm\omega,\pm\omega^2\}$, the invertible elements in all other cases are only $\{\pm1\}$.

The norm $N(\alpha)$ defined on a quadratic integer ring can be used to prove that it is a Euclidean domain. For the case $D>0$, its absolute value $|N(\alpha)|$ has to be used as the norm in the definition of a Euclidean domain. Using the norm obtained this way, it can be shown that, for $D<0$,

$$
D=-1,-2,-3,-7,-11
$$

or, for $D>0$,

$$
D=2, 3, 5, 6, 7, 11, 13, 17, 19, 21, 29, 33, 37, 41, 57, 73
$$

the quadratic integer rings corresponding to these integers are Euclidean domains with respect to the norm $|N(\cdot)|$. However, the norm in the definition of a Euclidean domain need not be the norm defined above. For example, for $D=14,69$, the corresponding quadratic integer rings are also Euclidean domains, but a different norm has to be used. For the case $D<0$, it can be shown that the cases listed above are all the Euclidean domains among quadratic integer rings.

Using more sophisticated methods, one can also determine whether a given quadratic integer ring is a principal ideal domain. It can be shown that for $D<0$, only for

$$
D=-1,-2,-3,-7,-11,-19,-43,-67,-163
$$

are the corresponding quadratic integer rings principal ideal domains. Comparing with the result above, we see that cases such as $D=-19$ provide examples of principal ideal domains that are not Euclidean domains. For $D>0$, there is currently no complete result.

However, it can be shown that in quadratic integer rings, unique factorization domains and principal ideal domains are equivalent. The result above shows that, for example, $\mathbf Z[\sqrt{-5}]$ is not a principal ideal domain, hence not a unique factorization domain either. We have already shown directly by an example that it does not have unique factorization, namely

$$
9=3\times3=(2+\sqrt{-5})\times(2-\sqrt{-5}).
$$

Using the same example, one can show that the ideal $(3,2+\sqrt{-5})$ is not principal either. We will see later that a simple example of a unique factorization domain that is not a principal ideal domain is the polynomial ring $\mathbf Z[x]$.

Although many quadratic integer rings are not unique factorization domains, they are all [Dedekind domains](https://en.wikipedia.org/wiki/Dedekind_domain). This means that every nontrivial ideal in any quadratic integer ring can be uniquely factored into a product of a sequence of prime ideals. But if the quadratic integer ring itself is not a principal ideal domain, these prime ideal factors do not necessarily correspond to prime elements, so the unique factorization theorem (that is, the factorization of numbers into products of primes) no longer holds: this was also the original motivation for studying ideals rather than numbers.

## Polynomial rings

Related reading: [Introduction to polynomial techniques](../poly/intro.md)

In algorithmic competitions, one frequently encounters various operations on polynomials. Operations on polynomials such as multiplication, inversion and remainder can be regarded as generalizations of operations on numbers to the polynomial ring. Using the language of abstract algebra, the properties of the corresponding operations in the polynomial ring can be understood more quickly.

???+ abstract "Polynomial"
    For a nonzero commutative ring with unity $R$, a **polynomial** over $R$ is a formal sum
    
    $$
    \sum_{k=0}^{n}a_kx^k = a_0+a_1x+\cdots+a_{n-1}x^{n-1}+a_nx^n,
    $$
    
    where $n\in\mathbf N$ and $a_k\in R$ for each $k$. These $a_k$ are called the **coefficients** of the polynomial, and the corresponding $a_kx^k$ are called the **terms** of the polynomial. The $k$ in the term $a_kx^k$ is called the **degree** of that term.
    
    The polynomial all of whose coefficients are zero (that is, the zero element) is called the **zero polynomial** and denoted by $0$. For other polynomials, we may assume $a_n\neq 0$, that is, $a_nx^n$ is the term of highest degree among the terms with nonzero coefficient. In this case, the natural number $n$ is called the **degree** of the polynomial, the term $a_nx^n$ it belongs to is called the **leading term**, and $a_n$ is also called the **leading coefficient**. A polynomial whose leading coefficient equals one (that is, the unity) is called a **monic** polynomial. The degree of the zero polynomial is left unspecified, or defined to be $-\infty$.

The $x$ appearing in the notation of a polynomial is called the **indeterminate** of the polynomial. It has no meaning of its own and no range of values. It exists only to mark the position of the coefficients through its exponent. Therefore, a polynomial can also be written as a sequence over $R$

$$
(a_0,a_1,...,a_{n-1},a_n,0,0,\cdots).
$$

However, such a sequence can have only finitely many nonzero terms. Two polynomials are said to be equal if their corresponding coefficient sequences are the same. This amounts to their formal sums being completely identical after padding with terms whose coefficients are zero. Below, we no longer distinguish between the formal-sum notations of equal polynomials: if necessary, the reader can fill in the missing zero coefficients.

Sometimes one needs to substitute elements of the ring for the indeterminate in a polynomial. For example, let $f(x)$ be a polynomial over $R$ and $a\in R$; then the result of substituting $a$ into the polynomial $f(x)$ is $f(a)$. Its meaning is: replacing $x$ by $a$ in the formal sum of the polynomial yields an arithmetic expression in $R$, and $f(a)$ is the result of evaluating this expression in $R$.

??? info "“Polynomials” and “polynomial functions”"
    The reader should not confuse these two concepts. A polynomial is merely a finite sequence of coefficients; it does not automatically become a function. Although the operation of substituting ring elements for the indeterminate described here does map polynomials to polynomial functions, this map need not be injective. For example, $f(x)=x^p-x$ as a polynomial over the field $\mathbf F_p$ is clearly not equal to the zero polynomial; but $f(x)$ as a polynomial function $\mathbf F_p\rightarrow \mathbf F_p$ is identically zero (this is Fermat's little theorem). Although the two concepts are different, many concepts for polynomial functions can be generalized to polynomials; for example, in imitation of differentiation, indefinite integration and composition of polynomial functions, one can define the (formal) [derivative](../poly/intro.md#derivative), [indefinite integral](../poly/intro.md#derivative), [composition](../poly/intro.md#composition), etc. of polynomials. These formal operations do not depend on any topological structure, but many rules of computation still hold.

For polynomials

$$
\begin{aligned}
f(x)&=a_0+a_1x+\cdots+a_{n-1}x^{n-1}+a_nx^n,\\
g(x)&=b_0+b_1x+\cdots+b_{n-1}x^{n-1}+b_nx^n,
\end{aligned}
$$

the addition of polynomials is defined as

$$
f(x)+g(x) = (a_0+b_0)+(a_1+b_1)x+\cdots+(a_{n-1}+b_{n-1})x^{n-1}+(a_n+b_n)x^n,
$$

and the multiplication of polynomials is defined as

$$
f(x)g(x) = a_0b_0+(a_1b_0+a_0b_1)x+(a_2b_0+a_1b_1+a_0b_2)x^2+\cdots,
$$

where the coefficient of the $x^k$ term is $\sum_{i=0}^ka_{k-i}b_i$. Under the addition and multiplication defined this way, it can be shown that all polynomials over $R$ form a ring, denoted by $R[x]$.

The degree of a polynomial $f(x)$ is denoted by $\deg f(x)$. The polynomials of degree zero are the constant polynomials; together with the zero polynomial, they constitute the embedding of $R$ into $R[x]$. Clearly, $R$ has zero divisors if and only if $R[x]$ has zero divisors.

???+ note "Theorem"
    The polynomial ring $R[x]$ is an integral domain if and only if $R$ is an integral domain.

In the polynomial ring $R[x]$ over an integral domain $R$, the results of addition and multiplication satisfy

$$
\begin{aligned}
\deg(f(x)+g(x)) &\le \max\{\deg f(x),\deg g(x)\},\\
\deg(f(x)g(x)) &= \deg f(x) + \deg g(x).
\end{aligned}
$$

Here we set $\deg 0 = -\infty$. Therefore, the invertible elements of the polynomial ring are necessarily just the invertible elements among its constant polynomials. No polynomial of degree one or higher is invertible.

The discussion below is restricted to polynomials over integral domains.

???+ info "Convention"
    Below, the phrases “polynomial over the ring $R$” and “polynomial in the polynomial ring $R[x]$” are used interchangeably. For example, a polynomial being irreducible over the ring $R$ means that the polynomial is irreducible in the ring $R[x]$. Moreover, if $R$ is a subring of $S$, then a polynomial over $R$ automatically becomes a polynomial over $S$; this is not further remarked upon either.

### Polynomial rings over a field

Among polynomial rings over integral domains, the ones with the simplest properties are, of course, polynomial rings over a field. In the polynomial ring $F[x]$ over a field $F$, the coefficients can be divided, so division with remainder can be defined. Let the norm of a nonzero polynomial $f(x)$ be $N(f(x))=\deg f(x)$. Then for a polynomial $f(x)$ and a nonzero polynomial $g(x)$ in $F[x]$, division with remainder can obviously be performed:

$$
f(x)=g(x)q(x)+r(x),
$$

where $q(x),r(x)\in F[x]$, and $r(x)=0$ or $\deg r(x)<\deg g(x)$. This shows that polynomial rings over a field are all Euclidean domains.

???+ note "Theorem"
    The polynomial ring $F[x]$ over a field $F$ is a Euclidean domain, hence also a principal ideal domain and a unique factorization domain.

In algorithmic competitions, due to computational precision, one often considers the polynomial ring $\mathbf F_p[x]=(\mathbf Z/p\mathbf Z)[x]$, where the modulus $p$ is required to be a prime. Such a ring admits the Euclidean algorithm and similar operations. However, the polynomial ring $(\mathbf Z/n\mathbf Z)[x]$ for an arbitrary modulus $n$ is not even an integral domain.

Division with remainder holding means that a root of a polynomial always corresponds to a linear factor of it.

???+ abstract "Root"
    A **root** of a polynomial $f(x)$ is an element $\xi\in F$ such that $f(\xi)=0$ holds.

???+ note "Theorem"
    For a polynomial $f(x)$ over a field $F$ and an element $\xi\in F$ of the field, $\xi$ is a root of $f(x)$ if and only if $f(x)$ has the linear factor $(x-\xi)$.

??? note "Proof"
    Division with remainder shows that there exist $q(x),r(x)$ such that $f(x)=q(x)(x-\xi)+r(x)$ holds with $\deg r(x)<\deg(x-\xi)=1$. Therefore, $r(x)$ is a constant polynomial or the zero polynomial; let $r(x)=c$, then necessarily $f(x)=q(x)(x-\xi)+c$. Substituting $x=\xi$, we get $0=f(\xi)=c$, that is, $f(x)=q(x)(x-\xi)$.

The concept of a root can be generalized to the case of multiple roots.

???+ abstract "Multiple root"
    If the polynomial $f(x)$ has the factor $(x-\xi)^k$, and $(x-\xi)^{k+1}$ does not divide $f(x)$, then $\xi$ is called a **root of multiplicity $k$** of $f(x)$. If $k>1$, the root $\xi$ is called a **multiple root** of $f(x)$; if $k=1$, the root $\xi$ is called a **simple root** of $f(x)$.

???+ note "Theorem"
    If a polynomial $f(x)$ over a field $F$ has the (possibly repeated) roots $\xi_1,\cdots,\xi_k$, then it necessarily has the factor $(x-\xi_1)\cdots(x-\xi_k)$. Furthermore, if a polynomial $f(x)$ over a field $F$ has degree $n$, then it has at most $n$ roots (counted with multiplicity).

??? note "Proof"
    It suffices to note that $F[x]$ is a unique factorization domain.

Although the unique factorization theorem holds for polynomials over a field, there is no general method to determine whether a given polynomial is reducible. The cases of small degree are relatively easy. For example, all polynomials of degree one are irreducible. Over special fields, all irreducible polynomials are of degree one. Such fields are called [algebraically closed fields](./field-theory.md#代数闭域). Over such a field, every polynomial of degree greater than zero has a root, so every polynomial of degree greater than one can be factored further. One such example is the field of complex numbers $\mathbf C$. Over the field of real numbers $\mathbf R$, on the other hand, there exist irreducible polynomials of degree two; over the field of rational numbers $\mathbf Q$, the structure of irreducible polynomials is even more complicated. The [Field theory](./field-theory.md) page has more discussion of polynomials over the field of rational numbers and over finite fields.

The results above all concern polynomials over a field. Polynomials over more general integral domains can often be reduced to this case.

Now consider the polynomial ring $R[x]$ over a unique factorization domain $R$. When computing directly in $R[x]$, many operations are restricted because the coefficients often cannot be divided. Let us consider extending $R$ to its field of fractions $F$, and then factoring a polynomial $f(x)$ of $R[x]$ in $F[x]$. We know that $F[x]$ is a unique factorization domain, so the factorization in $R[x]$ can be deduced from the factorization of $f(x)$ in $F[x]$. Fortunately, this idea is always feasible.

???+ note "Gauss's lemma"
    For a unique factorization domain $R$ and its field of fractions $F$, if $f(x)\in R[x]$, then if $f(x)=A(x)B(x)$ in $F[x]$, there necessarily exist $s,t\in F$ such that $a(x)=sA(x)\in R[x]$, $b(x)=tB(x)\in R[x]$, and $f(x)=a(x)b(x)$. Therefore, if $f(x)$ of degree greater than zero is irreducible in $R[x]$, then it is irreducible in $F[x]$.

??? note "Proof"
    Let $f(x)\in R[x]$ be reducible in $F[x]$, with $f(x)=A(x)B(x)$. Let $r_a$ and $r_b$ be the least common multiples of the denominators of all coefficients of $A(x)$ and $B(x)$, respectively; then $\tilde a(x)=r_aA(x)$ and $\tilde b(x)=r_bB(x)$ are both polynomials over $R$. Let $r=r_ar_b$; then $rf(x)=\tilde a(x)\tilde b(x)$. If $r$ is invertible in $R$, we can take the factorization $f(x)=(r^{-1}\tilde a(x))\tilde b(x)$, which obviously satisfies the requirements of the lemma.
    
    Otherwise, if $r$ has an irreducible factor $p$, we need to show that this factor can be cancelled on both sides of the equation while all coefficients remain in the integral domain $R$. Note that $p$ is necessarily also prime, so $(p)$ is a prime ideal. Reducing both sides of the equation modulo $p$, we get the polynomial equation $0=\bar a(x)\bar b(x)$ over $(R/(p))[x]$, where $\bar a$ and $\bar b$ are the reduced polynomials. Since $R/(p)$ is an integral domain, $(R/(p))[x]$ is also an integral domain, so we may assume $\bar a(x)=0$. This means that $p$ divides all coefficients of $\tilde a(x)$. Therefore, the factor $p$ can be cancelled directly on both sides of the equation.
    
    By the definition of a unique factorization domain, $r$ has at most finitely many such irreducible factors, so after cancelling them finitely many times we are reduced to the case where $r$ is invertible in $R$. This proves the lemma.

???+ note "Corollary"
    For a unique factorization domain $R$ and its field of fractions $F$, if $f(x)\in R[x]$ and all coefficients of $f(x)$ are coprime (that is, their greatest common divisor is the unity of $R$), then $f(x)$ is irreducible in $R[x]$ if and only if $f(x)$ is irreducible in $F[x]$.

That is, the irreducibles of the ring of integer-coefficient polynomials $\mathbf Z[x]$ are all irreducibles of $\mathbf Q[x]$. An effective method for determining whether an integer-coefficient polynomial is irreducible is Eisenstein's criterion. By Gauss's lemma, it also provides a method for determining whether a rational-coefficient polynomial is irreducible.

???+ note "Eisenstein's criterion"
    Let $f(x)=a_0+a_1x+\cdots+a_{n-1}x^{n-1}+a_nx^n$ be an integer-coefficient polynomial of degree $n$. If there exists a prime $p$ such that $p\mid a_i$ holds for all $i=0,1,\cdots,n-1$, $p$ does not divide $a_n$, and $p^2$ does not divide $a_0$, then the polynomial $f(x)$ is irreducible over the field of rational numbers $\mathbf Q$. If $\gcd(a_0,a_1,\cdots,a_n)=1$, then the polynomial $f(x)$ is also irreducible over the ring of integers $\mathbf Z$.

??? note "Proof"
    By Gauss's lemma, if the polynomial $f(x)$ is reducible over the field of rational numbers $\mathbf Q$, then it is also reducible over the ring of integers $\mathbf Z$. Let $f(x)=b(x)c(x)$ be its factorization in $\mathbf Z[x]$. Reducing both sides of the equation modulo the prime $p$, we get a factorization in $\mathbf F_p[x]$, $\overline{f}(x)=\overline{b}(x)\overline{c}(x)$. But the hypotheses of the theorem say that $\overline{f}(x)=x^n$, so there necessarily exists an integer $m$ such that $\overline b(x)=x^m$ and $\overline c(x)=x^{n-m}$, where $0<m<n$. Hence, the constant terms $b_0$ and $c_0$ of the factors $b(x)$ and $c(x)$ are both multiples of $p$. Hence, the constant term $a_0=b_0c_0$ of $f(x)$ is necessarily a multiple of $p^2$. This contradicts the given hypothesis.

??? example "Examples"
    1.  The polynomial $x^3-2$ is irreducible in $\mathbf Q[x]$. It suffices to apply Eisenstein's criterion with $p=2$.
    2.  The polynomial $x^4+1$ is irreducible in $\mathbf Q[x]$. Otherwise, $(x+1)^4+1=x^4+4x^3+6x^2+4x+2$ would be reducible as well. But applying Eisenstein's criterion with $p=2$ shows that the latter is not reducible.

For a unique factorization domain $R$, since the polynomial ring over the corresponding field of fractions $F$ is a unique factorization domain, and Gauss's lemma shows that the factorizations of polynomials over the field of fractions $F$ and over the original integral domain $R$ correspond to each other, $R[x]$ is also a unique factorization domain. Therefore, we have the following theorem:

???+ note "Theorem"
    The polynomial ring $R[x]$ is a unique factorization domain if and only if $R$ is a unique factorization domain.

Here $\mathbf Z[x]$ provides an example that a unique factorization domain need not be a principal ideal domain. For example, in $\mathbf Z[x]$, $(2,x)$ is not a principal ideal.

There are many ways to extend a polynomial ring to a larger set. For example, for the polynomial ring $R[x]$ over an integral domain, it can be extended to its field of fractions, denoted by $R(x)$. This field of fractions is often called the **field of rational fractions**, whose elements have the basic form $\dfrac{f(x)}{g(x)}$, where $f(x)$ and $g(x)$ are both polynomials.

### Multivariate polynomial rings

Polynomial rings can be generalized to the case of several indeterminates. For a commutative ring with unity $R$, one can define the polynomial ring over $R$, namely the univariate polynomial ring $R[x]$. Further, one can define the polynomial ring $R[x][y]$ over $R[x]$, which can be regarded as the bivariate polynomial ring $R[x,y]$ over $R$. In this way, the polynomial ring in $k$ variables $R[x_1,\cdots,x_k]$ over $R$ can be defined inductively. When $R$ is an integral domain, every multivariate polynomial ring over it is an integral domain; similarly, the property of being a unique factorization domain is also passed on to every multivariate polynomial ring.

### Ring of formal power series

One can also consider the case where arbitrarily many coefficients in the formal sum may be nonzero. A **formal power series** over a commutative ring with unity $R$ is defined as

$$
\sum_{k=0}^\infty a_kx^k=a_0+a_1x+a_2x^2+\cdots.
$$

Addition and multiplication of power series can be defined in the same way as in the polynomial ring $R[x]$. Moreover, formal power series then also form a ring, denoted by $R[[x]]$. The convergence of these formal power series need not be considered, because in fact each formal power series is just its sequence of coefficients, and no further topological structure is attached.

The structure of the ring of formal power series is very interesting. In a polynomial ring over an integral domain, the invertible elements can only be constants. In the ring of formal power series, however, one can have

$$
(1-x)^{-1}=\sum_{k=0}^\infty x^k=1+x+x^2+\cdots.
$$

This phenomenon is general. As long as the constant term $a_0$ of a formal power series is invertible in $R$, $\sum_{k=0}^\infty a_kx^k$ is necessarily invertible as well. This is because if we set

$$
\left(\sum_{k=0}^\infty a_kx^k\right)\left(\sum_{k=0}^\infty b_kx^k\right)=1,
$$

then, writing out the system of equations that the coefficients must satisfy, the expressions for $b_k$ can be found recursively, involving only the inverse of $a_0$.

Various operations can be defined on the ring of formal power series, such as inversion, division, compositional inverse, formal derivative, elementary functions, etc.; see [Introduction to polynomial techniques](../poly/intro.md) for details.

### Ring of formal Laurent series

The ring of formal power series can be extended further so as to allow terms of negative degree. A **formal Laurent series** over a commutative ring with unity $R$ is defined as

$$
\sum_{k=N}^\infty a_kx^k,
$$

where $N\in\mathbf Z$. Thus, a formal Laurent series can have finitely many terms of negative degree. Extending the previous addition and multiplication to formal Laurent series yields the ring of formal Laurent series, denoted by $R((x))$. If $F$ is a field, then $F((x))$ is also a field.

The ring of formal Laurent series has applications in [Lagrange inversion](../poly/lagrange-inversion.md).

## Chinese remainder theorem

Related reading: [Chinese remainder theorem](../number-theory/crt.md)

In number theory, the Chinese remainder theorem is often used to solve systems of congruences. For general commutative rings with unity, a Chinese remainder theorem can be established as well. Each congruence amounts to specifying the image of the unknown in some quotient ring, so the Chinese remainder theorem in a commutative ring with unity amounts to determining an element of the ring from its images in these quotient rings.

This discussion can be turned into formal language. For a nonzero commutative ring with unity $R$ and its ideals $I_1,\cdots,I_n$, consider the ring homomorphism $\varphi:R\rightarrow R/I_1\times \cdots\times R/I_n$ that maps $r$ to $(r+I_1,\cdots,r+I_n)$. Here, $r+I_i$ is a coset, and $\times$ denotes the direct product of rings:

???+ abstract "Direct product"
    For rings $R_1$ and $R_2$, multiplication on the direct product $R_1\times R_2$ of their additive groups can be defined componentwise; then $R_1\times R_2$ becomes a ring, called the **direct product** of the rings $R_1$ and $R_2$, still denoted by $R_1\times R_2$.

The kernel of the homomorphism $\varphi$ is $\ker\varphi=I_1\cap\cdots\cap I_n$. The question the Chinese remainder theorem answers is under what conditions such a map is surjective.

In the number-theoretic case, the theorem requires the moduli to be coprime. This condition can be generalized to the ring-theoretic setting.

???+ abstract "Comaximal ideals"
    Let the ring $R$ have ideals $I$ and $J$. If $I+J=R$, then $I$ and $J$ are said to be **comaximal**.

In the case of rings with unity, if we consider the principal ideals $(a)$ and $(b)$, this condition amounts to the existence of $x,y\in R$ such that $ax+by=1$, which is similar to Bézout's identity for coprime integers. Using this definition, one can establish the **Chinese remainder theorem** in commutative rings with unity, completely in imitation of the case of the ring of integers.

???+ note "Chinese remainder theorem"
    Let the nonzero commutative ring with unity $R$ have ideals $I_1,\cdots,I_n$. If they are pairwise comaximal, then the ring homomorphism $\varphi$ defined above is surjective, and its kernel equals the product of these ideals, $\ker\varphi=I_1\cap\cdots\cap I_n=I_1\cdots I_n$; therefore,
    
    $$
    R/(I_1\cdots I_n)=R/(I_1\cap\cdots\cap I_n)\cong R/I_1\times\cdots\times R/I_n.
    $$

??? note "Proof"
    The content of the theorem is rich, but only two claims remain to be proved, namely that $\varphi$ is surjective and that $I_1\cap\cdots\cap I_n=I_1\cdots I_n$. The key is to make good use of the comaximality condition.
    
    First we prove the case $n=2$. Since the ideals $I_1$ and $I_2$ are comaximal, that is, $I_1+I_2=R$, the unity $1$ of $R$ can be written in the form $a_1+a_2$, where $a_i\in I_i$. Since $a_1\in I_1$ and $a_1=1-a_2\in 1+I_2$, we have $\varphi(a_1)=(I_1,1+I_2)$; similarly, $\varphi(a_2)=(1+I_1,I_2)$. Therefore, $(\varphi(a_2),\varphi(a_1))$ plays a role similar to a “basis” in a vector space. Hence, for any image $(r_1+I_1,r_2+I_2)$, one can find the preimage $r_1a_2+r_2a_1$ under the homomorphism $\varphi$. This shows that $\varphi$ is surjective.
    
    It remains to prove $I_1\cap I_2=I_1I_2$. For a general ring we always have $I_1I_2\subseteq I_1\cap I_2$; the key is the reverse inclusion. For any $r\in I_1\cap I_2$, we have $r=r(a_1+a_2)=ra_1+ra_2\in I_1I_2$. Hence $I_1\cap I_2\subseteq I_1I_2$ holds as well. This proves the claim.
    
    For the case $n>2$, mathematical induction is needed. The key of the induction step is to show that for pairwise comaximal ideals $I_1,\cdots,I_n$, the ideals $I_1$ and $I_2\cdots I_n$ are always comaximal. Since $I_1$ is comaximal with each of $I_2,\cdots,I_n$, for each $i=2,\cdots,n$ there exist $a_i\in I_1$ and $b_i\in I_i$ such that $1=a_i+b_i$ holds. Therefore, $1=(a_2+b_2)\cdots(a_n+b_n)$ holds. Hence, $1\in (b_2\cdots b_n)+I_1\subseteq I_1+(I_2\cdots I_n)$. This shows that the ideals $I_1$ and $I_2\cdots I_n$ are comaximal.

### Application: Lagrange interpolation formula

Related reading: [Lagrange interpolation](../numerical/interp.md#lagrange-插值法), [Fast polynomial interpolation](../poly/multipoint-eval-interpolation.md#fast-polynomial-interpolation)

The interpolation problem is: given a sequence of point values $\{(x_i,y_i)\}_{i=1}^n$, find a polynomial $f(x)$ over a field $F$ such that $f(x_i)=y_i$ holds for all $i=1,\cdots,n$. Of course, all $x_i$ are assumed to be pairwise distinct. The Lagrange interpolation formula gives the general solution to this kind of problem.

For a polynomial $f(x)$ over a field $F$, the condition $f(x_i)=y_i$ is equivalent to $x_i$ being a root of the polynomial $f(x)-y_i$, hence equivalent to $(x-x_i)\mid(f(x)-y_i)$, that is, $f(x)\equiv y_i\pmod{x-x_i}$. Therefore, the interpolation problem is equivalent to solving the system of congruences

$$
\begin{cases}
f(x)\equiv y_1&\pmod{x-x_1},\\
f(x)\equiv y_2&\pmod{x-x_2},\\
\cdots\\
f(x)\equiv y_n&\pmod{x-x_n}.
\end{cases}
$$

These linear polynomials $\{x-x_i\}_{i=1}^n$ are pairwise coprime. By the Chinese remainder theorem, the solution of the problem should have the form

$$
f(x)=\sum_{i=1}^ny_iM_i(x),
$$

where $M_i(x)=m_i(x)\prod_{j\neq i}(x-x_j)$ and $M_i(x)\equiv 1\pmod{x-x_i}$. By the equivalence derived earlier, this is equivalent to $M_i(x_i)=1$, that is,

$$
m_i(x_i)\prod_{j\neq i}(x_i-x_j) = 1.
$$

We may take $m_i(x)$ to be a constant polynomial, namely

$$
m_i(x) = \frac{1}{\prod_{j\neq i}(x_i-x_j)}.
$$

From this we obtain the Lagrange interpolation formula

$$
f(x)=\sum_{i=1}^ny_i\frac{\prod_{j\neq i}(x-x_j)}{\prod_{j\neq i}(x_i-x_j)}.
$$

In general, by generalizing this method, one can also derive the [Hermite interpolation formula](https://en.wikipedia.org/wiki/Hermite_interpolation), which allows prescribing the values of several derivatives of the polynomial at each point.

### Application: multiplicative group of integers modulo n

Related reading: [Primitive roots](../number-theory/primitive-root.md), [Fundamental theorem of finitely generated abelian groups](./group-theory.md#分类定理)

As an application of the Chinese remainder theorem and of material from group theory, here we discuss the structure of the multiplicative group of integers modulo $n$. In this section, the bar notation for congruence classes is omitted.

The **multiplicative group of integers modulo $n$** is $(\mathbf Z/n\mathbf Z)^\times$, that is, the multiplicative group of the invertible elements of the quotient ring $\mathbf Z/n\mathbf Z$ (also called the group of units). The order of the group $(\mathbf Z/n\mathbf Z)^\times$ is $\varphi(n)$, because the necessary and sufficient condition for the existence of an inverse is being coprime to $n$. Here $\varphi(n)$ is [Euler's totient function](../number-theory/euler-totient.md). Moreover, the group $(\mathbf Z/n\mathbf Z)^\times$ is always abelian.

By the fundamental theorem of arithmetic, the modulus $n$ can be factored into a product of powers of distinct primes:

$$
n=p_1^{\alpha_1}\cdots p_s^{\alpha_s}.
$$

It is easy to verify that for ideals of the ring of integers, the condition that the ideals are comaximal is equivalent to their generators being coprime. Therefore, applying the Chinese remainder theorem yields

$$
\mathbf Z/n\mathbf Z\cong\mathbf Z/p_1^{\alpha_1}\mathbf Z\times\cdots\times\mathbf Z/p_s^{\alpha_s}\mathbf Z.
$$

An isomorphism of rings means that the corresponding multiplicative structures are isomorphic as well, so

$$
(\mathbf Z/n\mathbf Z)^\times\cong(\mathbf Z/p_1^{\alpha_1}\mathbf Z)^\times\times\cdots\times(\mathbf Z/p_s^{\alpha_s}\mathbf Z)^\times.
$$

This shows that $\varphi(n)=\varphi(p_1^{\alpha_1})\cdots\varphi(p_s^{\alpha_s})$, that is, Euler's totient function is multiplicative.

Therefore, to study the case of a general modulus, it suffices to consider the case where the modulus is a prime power $p^k$. For prime powers, the two cases $p=2$ and $p$ an odd prime need to be considered separately:

-   For the case $p=2$, direct verification gives $(\mathbf Z/2\mathbf Z)^\times\cong C_1$ and $(\mathbf Z/4\mathbf Z)^\times\cong C_2$. For the case $k\ge3$, we have $(\mathbf Z/2^k\mathbf Z)^\times\cong C_2\times C_{2^{k-2}}$.

    ??? note "Proof"
        Direct computation using the binomial theorem shows that
        
        $$
        \begin{aligned}
        5^{2^{k-2}}=(1+2^2)^{2^{k-2}}&\equiv 1\pmod {2^k},\\
        5^{2^{k-3}}=(1+2^2)^{2^{k-3}}&\equiv 1+2^{k-1}\pmod {2^k}.
        \end{aligned}
        $$
        
        Therefore, $5$ is an element of order $2^{k-2}$ in $(\mathbf Z/2^k\mathbf Z)^\times$. At the same time, $-1$ and $5^{2^{k-3}}$ are two distinct elements of order two, so $-1\notin\langle 5\rangle$. Hence, the intersection of $\langle-1\rangle$ and $\langle 5\rangle$ is trivial, and by the characterization of direct products of groups we have
        
        $$
        (\mathbf Z/2^k\mathbf Z)^\times\cong\langle-1\rangle\times\langle 5\rangle\cong C_2\times C_{2^{k-2}}.
        $$
-   For the case where $p$ is an odd prime, it can be shown that $(\mathbf Z/p^k\mathbf Z)^\times$ is isomorphic to the cyclic group $C_{\varphi(p^k)}$.

    ??? note "Proof"
        To show that $(\mathbf Z/p^k\mathbf Z)^\times$ is cyclic, by the fundamental theorem of finite abelian groups it suffices to show that each of its Sylow $q$‑subgroups is cyclic. First, for the Sylow $p$‑subgroup, direct computation shows that
        
        $$
        \begin{aligned}
        (1+p)^{p^{k-1}} &\equiv 1\pmod{p^k},\\
        (1+p)^{p^{k-2}} &\equiv 1+p^{k-1}\pmod{p^k}.
        \end{aligned}
        $$
        
        Hence, $(1+p)$ is an element of order $p^{k-1}$. That is, the unique Sylow $p$‑subgroup of $(\mathbf Z/p^k\mathbf Z)^\times$ is the cyclic group $\langle 1+p\rangle$.
        
        For the other Sylow $q$‑subgroups ($q\neq p$), they can be reduced to the case $k=1$ via a group homomorphism. Consider the group homomorphism $\varphi:(\mathbf Z/p^k\mathbf Z)^\times\rightarrow(\mathbf Z/p\mathbf Z)^\times$ that maps the coset $r+p^k\mathbf Z$ to the coset $r+p\mathbf Z$. The kernel of this map has size $p^{k-1}$, so when the map $\varphi$ is restricted to a Sylow $q$‑subgroup ($q\neq p$) of $(\mathbf Z/p^k\mathbf Z)^\times$, the kernel of the restricted map is trivial, so this Sylow $q$‑subgroup is isomorphic to the image of the map, namely the Sylow $q$‑subgroup of $(\mathbf Z/p\mathbf Z)^\times$. Therefore, it suffices to show that the Sylow $q$‑subgroups of $(\mathbf Z/p\mathbf Z)^\times$ are all cyclic.
        
        Finally, we show that the Sylow $q$‑subgroups of $(\mathbf Z/p\mathbf Z)^\times$ are all cyclic. Since $(\mathbf Z/p\mathbf Z)^\times$ is a finite abelian group, it can be decomposed according to invariant factors as
        
        $$
        C_{n_1}\times\cdots\times C_{n_r}.
        $$
        
        Here, $n_1\mid n_2\mid \cdots \mid n_r$. Therefore, each direct factor has $n_1$ elements whose order divides $n_1$. If $r>1$, then necessarily strictly more than $n_1$ elements satisfy the equation $x^{n_1}=1$. But $\mathbf Z/p\mathbf Z$ is a field, and a polynomial of degree $n_1$ over a field has at most $n_1$ roots, so $r=1$. That is, $(\mathbf Z/p\mathbf Z)^\times\cong C_{p-1}$.
        
        This proves $(\mathbf Z/p^k\mathbf Z)^\times\cong C_{p^{k-1}}\times C_{p-1}\cong C_{\varphi(p^{k})}$.

The structure of the multiplicative group for a general modulus is thereby determined as well. From the results obtained, we know that the multiplicative group of integers modulo $n$ is cyclic if and only if the modulus $n$ takes the values

$$
1,2,4,p^k,2p^k
$$

where $p$ is an odd prime; otherwise, the multiplicative group of integers modulo $n$ necessarily has a subgroup $C_2\times C_2$ and cannot be cyclic. When the multiplicative group is cyclic, a generator of the multiplicative group is called a **primitive root** of that modulus. Therefore, the theorem here gives precisely the necessary and sufficient condition for the existence of primitive roots.

Of course, the analysis of the structure of the multiplicative group contains more information than the condition for the existence of primitive roots. It clearly reflects the orders of the various elements of the multiplicative group. An element $x$ of the group $(\mathbf Z/n\mathbf Z)^\times$ satisfying $x^k=1$, that is, a solution of the congruence $x^k\equiv 1\pmod n$, is called a **$k$-th root of unity modulo $n$**; an element of order exactly $k$ is called a **primitive $k$-th root of unity modulo $n$**. Using the structure of the multiplicative group, the existence and number of these roots of unity can be computed precisely. Finally, the least common multiple of the orders of all elements of the group $(\mathbf Z/n\mathbf Z)^\times$, that is, the smallest positive integer $k$ such that $x^k=1$ for all $x\in (\mathbf Z/n\mathbf Z)^\times$, expressed as a function of $n$, is the [Carmichael function](../number-theory/primitive-root.md#carmichael-function). A series of its properties can all be obtained from the structure of the multiplicative group.

## References and notes

-   Dummit, D.S. and Foote, R.M. (2004) Abstract Algebra. 3rd Edition, John Wiley & Sons, Inc.
-   [Quadratic integer - Wikipedia](https://en.wikipedia.org/wiki/Quadratic_integer)
-   [Formal power series - Wikipedia](https://en.wikipedia.org/wiki/Formal_power_series)
-   [Multiplicative group of integers modulo $n$- Wikipedia](https://en.wikipedia.org/wiki/Multiplicative_group_of_integers_modulo_n)

[^ideal-history]: <https://en.wikipedia.org/wiki/Ideal_(ring_theory)#History>

[^simple-ring]: As in the case of groups, such a ring is called a **simple ring**. A commutative simple ring can only be a field, while the case of noncommutative simple rings is much more complicated.

[^gcd-domain]: An integral domain in which greatest common divisors exist is called a [GCD domain](https://en.wikipedia.org/wiki/GCD_domain).

[^ring-theory-history]: A brief history of ring theory can be found [here](https://mathshistory.st-andrews.ac.uk/HistTopics/Ring_theory/).
