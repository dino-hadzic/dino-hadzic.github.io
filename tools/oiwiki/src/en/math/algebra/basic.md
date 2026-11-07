---
title: Basic concepts
---

This chapter gives a brief introduction to abstract algebra. At present, the main content of algorithm competitions does not directly test knowledge of abstract algebra, but descriptions of algorithms and solutions of problems often involve basic concepts of abstract algebra, so readers who know the basic concepts of abstract algebra can understand some algorithms more quickly. Therefore, this material is not required knowledge for any contestant; it is only provided for readers who are interested or who may benefit from it. At the same time, this chapter avoids an overly complete and deep treatment of abstract algebra[^oi-wiki-not-wikipedia] and focuses on the basic concepts and on the parts most closely related to the rest of the OI material. Readers who want to study abstract algebra systematically should learn from professional textbooks on abstract algebra.

To help readers better understand what they may gain from reading this part, here are some examples from algorithm competitions in which knowledge of abstract algebra may be involved:

-   many theorems in number theory and on polynomials are special cases of results in abstract algebra;
-   in data structures, structures such as the [segment tree](../../ds/seg.md) can maintain information forming a monoid, and the recurrence relations of many DP problems can be abstracted into such a monoid structure;
-   in combinatorics, the rigorous statement and proof of the [Pólya enumeration theorem](../combinatorics/polya.md) require concepts from group theory.

Based on this, this chapter focuses on the basic knowledge that cannot be skipped and on the parts directly related to these applications. To begin with, this article introduces the basic concepts of groups, rings and fields.

## Groups

The definition of a group is as follows.

???+ abstract "Group"
    Let $G$ be a nonempty set with a binary operation $\cdot:G\times G\rightarrow G$ on it. If they satisfy the following properties, then $(G,\cdot)$ is called a **group**:
    
    1.  associative property: for all $a,b,c\in G$, $a\cdot(b\cdot c)=(a\cdot b)\cdot c$ holds;
    2.  existence of an identity element: there exists $e\in G$ such that for every $a\in G$, $a\cdot e = e\cdot a = a$ holds. Here, $e$ is called the **identity element** of $G$, also called the unit element;
    3.  existence of inverse elements: for every $a\in G$ there exists a corresponding $b\in G$ such that $a\cdot b=b\cdot a=e$. Here, $b$ is called the **inverse element** of $a$.

??? info "On the closure condition in the definition"
    The binary operation here already implies the so-called closure condition, namely that for all $a,b\in G$, $a\cdot b\in G$. Some texts list it separately.

???+ note "Basic properties of groups"
    For a group $(G,\cdot)$, the following properties always hold:
    
    1.  for any finite sequence $\{g_i\}_{i=1}^k\subseteq G$, the result of the product $g_1\cdot g_2\cdot\cdots\cdot g_k$ does not depend on how the parentheses are placed;
    2.  the identity element $e$ is always unique;
    3.  for every element $a\in G$, its inverse $a^{-1}$ is also unique;
    4.  cancellation law: for $a,b,c\in G$, if $a\cdot c=b\cdot c$ or $c\cdot a=c\cdot b$, then $a=b$.

Groups are quite common. Informally, all transformations that do not lose structure automatically form a group. Let us take several common types of groups as examples.

???+ example "Examples of groups"
    -   **Symmetric group**: all [permutations](../permutation.md) of a set $M$, i.e. bijections from $M$ to $M$ itself, form a group $S_M$ under composition of maps. The identity element is the identity transformation, and the inverse element is the inverse map (a bijection necessarily has an inverse map). If the set $M$ is finite of size $n$, the group is also often denoted $S_n$ and called the symmetric group of degree $n$.
    -   Symmetry group in space: for a geometric figure, all transformations that map it onto itself also form a group under composition of maps. This describes the spatial symmetry of the geometric figure. For concrete examples, see [Common symmetry groups](../combinatorics/polya.md#common-symmetry-groups).
    -   Additive group of the integers: the set of integers $\mathbf Z$ forms a group $(\mathbf Z,+)$ under the addition operation $+$. The identity element is $0$, and the inverse element is the opposite number.
    -   Multiplicative group of integers modulo $n$: for a modulus $n$, the [congruence classes](../number-theory/basic.md#congruence-classes-and-residue-systems) corresponding to all integers coprime to $n$ form a group $((\mathbf Z/n\mathbf Z)^\times,\times)$ under multiplication. The identity element is $\bar 1$, and the inverse element is exactly the [modular inverse](../number-theory/inverse.md) modulo $n$ (the corresponding congruence class), whose existence is guaranteed by [Bézout's identity](../number-theory/bezouts.md). For a concrete structural analysis, see [Multiplicative group of integers modulo $n$](./ring-theory.md#应用整数同余类的乘法群).
    -   General linear group: all invertible square matrices of dimension $n$ over a number field $F$ form a group $GL_n(F)$ under multiplication. The identity element is the identity matrix, and the inverse element is the inverse matrix.

To better understand the definition of a group, it helps to look at a few examples that are not groups for comparison.

???+ example "Examples that are not groups"
    -   All maps from $M$ to itself (not necessarily bijections) do not form a group, because the maps that are not bijections have no inverse element.
    -   The integers under multiplication do not form a group, because $2$ has no multiplicative inverse within the integers.
    -   The positive integers under addition do not form a group either, because the positive integers have no additive identity element.
    -   All nonzero congruence classes modulo $n$ often do not form a group under multiplication. For example, in $(\mathbf Z/6\mathbf Z)\setminus\{\overline 0\}$, the product $\overline 2\times\overline 3=\overline 0$ does not belong to this set, which means that multiplication is not a well-defined binary operation on this set (in other words, it does not satisfy closure).

Sometimes it is also necessary to discuss the properties of these less complete structures. Therefore, the following concepts, which are broader than groups, can be defined.

???+ abstract "Semigroup"
    For a nonempty set $G$ and a binary operation $\cdot$ on it, if the operation is associative, then $(G,\cdot)$ is called a **semigroup**.

???+ abstract "Monoid"
    For a semigroup $(G,\cdot)$, if it also has an identity element, then $(G,\cdot)$ is called a **monoid**.

???+ example "Examples of monoids and semigroups"
    Among the examples above, $(\mathbf N_+,+)$ is a semigroup, and $(\mathbf Z,\times)$ is a monoid.

Finally, many familiar operations on groups satisfy not only the associative property but also the commutative property. The structure of such groups is relatively simple; they are called Abelian groups, also called commutative groups.

???+ abstract "Abelian group"
    For a group $(G,\cdot)$, if the operation $\cdot$ also satisfies the commutative property, i.e. for all $a,b\in G$, $a\cdot b=b\cdot a$ holds, then $(G,\cdot)$ is called an **Abelian group** or a **commutative group**.

???+ example "Examples of Abelian and non-Abelian groups"
    -   The additive group of the integers $(\mathbf Z,+)$ is an Abelian group.
    -   For $n\ge3$, the symmetric group $S_n$ is not an Abelian group.

These are the basic definitions related to group theory. For more on group theory, see [Group theory](./group-theory.md) or related books.

## Rings

The definition of a ring is as follows.

???+ abstract "Ring"
    For a nonempty set $R$ and two binary operations on it, $+:R\times R\rightarrow R$ and $\cdot:R\times R\rightarrow R$, if they satisfy the following properties, then $(R,+,\cdot)$ is called a **ring**:
    
    1.  $(R,+)$ forms an Abelian group, whose identity element is denoted $0$, and the inverse of an element $a\in R$ under $+$ is denoted $-a$.
    2.  $(R,\cdot)$ forms a semigroup, i.e. $\cdot$ is associative.
    3.  Distributive property: for all $a,b,c\in R$, $a\cdot(b+c)=a\cdot b+a\cdot c$ and $(a+b)\cdot c=a\cdot c+b\cdot c$ hold.

For convenience of exposition, these two binary operations $+$ and $\cdot$ are usually called the addition and multiplication of the ring; correspondingly, the additive identity element is called the **zero**, and the multiplicative identity element (if it exists) is called the **identity**. One should avoid confusing them with the addition and multiplication of concrete sets of numbers, and with the natural numbers zero and one.

??? info "On whether the definition requires a multiplicative identity"
    In some definitions, a ring must have a multiplicative identity element; correspondingly, those without a multiplicative identity are called **rngs** (or pseudo-rings). When encountered, this must be judged from the context. Wikipedia uses this definition[^ring-wiki].

The additive structure of a ring is quite simple, but the multiplicative structure is very primitive. Therefore, by analogy with groups, imposing more requirements on multiplication yields the following related definitions.

???+ abstract "Ring with identity"
    For a ring $(R,+,\cdot)$, if it has an identity, i.e. a multiplicative identity element exists, denoted $1$, then $(R,+,\cdot)$ is called a **ring with identity**.

???+ abstract "Division ring"
    For a nonzero ring with identity $(R,+,\cdot)$, if every element $a\in R$ other than $0$ has a multiplicative inverse (denoted $a^{-1}$), then $(R,+,\cdot)$ is called a **division ring**.

???+ abstract "Commutative ring"
    For a ring $(R,+,\cdot)$, if its multiplication satisfies the commutative property, then $(R,+,\cdot)$ is called a **commutative ring**.

An interesting point in the definition of a division ring is that it treats $0$ as a special element of the multiplicative structure. This is because $0 = 0\cdot a = a\cdot 0$[^zero-multiplication]. In other words, the additive identity of a ring multiplied by any element gives itself again. Thus it naturally cannot have a multiplicative inverse, unless it is itself the multiplicative identity. The only such ring is the zero ring (see the examples below).

The lesson here is that, when understanding the multiplicative structure of a general ring, one should remove the influence of the additive identity and examine $R\setminus\{0\}$. Based on this idea, we have the following definitions.

???+ abstract "Zero divisor"
    For a ring $(R,+,\cdot)$, if there exists $b\in R$ with $b\ne 0$ such that $a\cdot b=0$ or $b\cdot a=0$ holds, then the nonzero element $a$ is called a **zero divisor**.

???+ abstract "Invertible element (unit)"
    For a ring $(R,+,\cdot)$, if an element $a$ has a multiplicative inverse, i.e. there exists $b\in R$ such that $a\cdot b=b\cdot a=1$ holds, then the element $a\in R$ is called an **invertible element**, or a **unit**.

???+ warning "“Unit” and “identity element”"
    Please do not confuse these two concepts. To avoid confusion, the abstract algebra section will use the name “invertible element” instead of “unit”.

A zero divisor cannot be an invertible element, and an invertible element cannot be a zero divisor. However, a nonzero element can be neither a zero divisor nor an invertible element.

If a ring has no zero divisors, this means that the set of all nonzero elements is closed under multiplication, i.e. $(R\setminus\{0\},\cdot)$ forms a semigroup. Further, if we also require it to be a commutative monoid, we obtain the definition of an integral domain.

???+ abstract "Integral domain"
    For a nonzero ring $(R,+,\cdot)$, if it is a commutative ring, has a multiplicative identity element, and has no zero divisors, then it is called an integral domain.

Although elements of an integral domain do not necessarily have inverses, the property of having no zero divisors is already enough to establish the cancellation law in an integral domain.

???+ note "Cancellation law in an integral domain"
    Let an integral domain $R$ have elements $a,b,c\in R$ with $a\neq 0$. If $ab=ac$, then necessarily $b=c$.

For a general ring with identity, if we consider only all of its invertible elements, we likewise obtain a group structure. This is called the multiplicative group or the unit group of the ring.

???+ abstract "Multiplicative group (unit group)"
    For a ring with identity $(R,+,\cdot)$, let $R^\times$ be the set of all invertible elements in $R$. Then $(R^\times,\cdot)$ forms a group, called the **multiplicative group** of the ring with identity $R$, or its **unit group**.

Some of the simplest examples of rings are as follows.

???+ example "Examples of rings"
    -   Zero ring: the set $\{0\}$ forms a ring under the usual addition $+$ and multiplication $\times$, called the zero ring. It is the only ring with just one element, and also the only ring in which the additive identity and the multiplicative identity are equal.
    -   Ring of integers: the set of integers $\mathbf Z$ with the usual addition $+$ and multiplication $\times$ defined on it forms the ring $(\mathbf Z,+,\times)$. In fact, this is an integral domain, but it is not a division ring.
    -   Polynomial ring: for a ring $R$, one can define the [polynomial ring](./ring-theory.md#多项式环)  $R[x]$ over it. If $R$ is an integral domain, then this polynomial ring is necessarily an integral domain.
    -   Quaternions: by analogy with the complex numbers, one can consider the set $\mathbf H=\{a+b\mathrm{i}+c\mathrm{j}+d\mathrm{k}:a,b,c,d\in\mathbf R\}$ and define addition and multiplication on it, where the multiplication of $\mathrm{i},\mathrm{j},\mathrm{k}$ satisfies
    
        $$
        \mathrm{i}^2=\mathrm{j}^2=\mathrm{k}^2=-1,\ \mathrm{i}\mathrm{j}=-\mathrm{j}\mathrm{i}=\mathrm{k},\ \mathrm{j}\mathrm{k}=-\mathrm{k}\mathrm{j}=\mathrm{i},\ \mathrm{k}\mathrm{i}=-\mathrm{i}\mathrm{k}=\mathrm{j}.
        $$
    
        Then one can verify that $\mathbf H$ forms a ring, and moreover it is a noncommutative division ring.
    -   The subset $2\mathbf Z$ of the integers forms a ring under the usual addition and multiplication; it is a commutative ring with no zero divisors, but it has no identity.
    -   The congruence classes of integers modulo $n$, $\mathbf Z/n\mathbf Z$, form a ring under the addition and multiplication of congruence classes; it is a commutative ring with identity (namely $\bar 1$). Such a ring has zero divisors if and only if $n$ is composite. Hence, when $n$ is prime, the ring $(\mathbf Z/n\mathbf Z, +,\times)$ is an integral domain; moreover, it is then also a division ring, so it actually forms a field. Its multiplicative group $((\mathbf Z/n\mathbf Z)^\times,\times)$ is exactly the multiplicative group of integers modulo $n$.
    -   Matrix ring: all square matrices of dimension $n$ over a ring $R$ form a ring $M_n(R)$ under matrix addition and multiplication. In general, this ring has zero divisors and is not commutative.
    -   For the set of all subsets $\mathcal P(A)$ of a set $A$, if we define the symmetric difference of sets $\triangle$ and the intersection $\cap$ as its addition and multiplication respectively, then $(\mathcal P(A),\triangle,\cap)$ forms a ring. In general, this ring has an identity, has zero divisors, and is commutative.

Of course, the discussion of the structure of rings goes far beyond this; to learn more, see [Ring theory](./ring-theory.md) or related books.

## Fields

A field is an algebraic structure with stronger properties than a ring. Specifically, a field is a commutative division ring. Of course, its complete definition can also be written out.

???+ abstract "Field"
    For a nonempty set $F$ and two binary operations on it, $+:F\times F\rightarrow F$ and $\cdot:F\times F\rightarrow F$, if they satisfy the following properties, then $(F,+,\cdot)$ is called a **field**:
    
    1.  $(F,+)$ forms an Abelian group, whose identity element is denoted $0$, and the inverse of an element $a\in F$ under $+$ is denoted $-a$.
    2.  $(F\setminus\{0\},\cdot)$ forms an Abelian group, whose identity element is denoted $1$, and the inverse of an element $a\in F\setminus\{0\}$ under $\cdot$ is denoted $a^{-1}$.
    3.  Distributive property: for all $a,b,c\in F$, $a\cdot(b+c)=a\cdot b+a\cdot c$ holds.

In other words, a field is an algebraic structure closed under all four arithmetic operations: addition, subtraction, multiplication and division.

Common examples of fields are as follows.

???+ example "Examples of fields"
    -   Number fields: the set of rational numbers $\mathbf Q$, the set of real numbers $\mathbf R$ and the set of complex numbers $\mathbf C$ all form fields under the usual addition and multiplication.
    -   Finite field: the set of congruence classes of integers modulo a prime $p$, $\mathbf Z/p\mathbf Z$, forms a field under the addition and multiplication of congruence classes. Of course, there are other finite fields besides these; their structure is uniquely determined by their size, and the size is necessarily a power of a prime.
    -   **Fraction field**: let $(R,+,\cdot)$ be an integral domain. One can consider the set $Q$ of elements of the form $ab^{-1}$. Strictly speaking, define an equivalence relation on the set $R\times(R\setminus\{0\})$: $(a_1,b_1)\sim(a_2,b_2)$ if and only if $a_1b_2=a_2b_1$. Then the set $Q$ is the set of equivalence classes under this relation, $R\times(R\setminus\{0\})/\sim$, where the equivalence class containing $(a,b)$ is denoted $ab^{-1}$. If we define the operations on it as
    
        $$
        \begin{aligned}
        a_1b_1^{-1}+a_2b_2^{-1} &= (a_1\cdot b_2+a_2\cdot b_1)(b_1\cdot b_2)^{-1},\\
        (a_1b_1^{-1})\cdot(a_2b_2^{-1}) &= (a_1\cdot a_2)(b_1\cdot b_2)^{-1}
        \end{aligned}
        $$
    
        then $(Q,+,\cdot)$ forms a field, called the fraction field of $R$. For example, the field of rational numbers $(\mathbf Q,+,\times)$ is the fraction field of the ring of integers $(\mathbf Z,+,\times)$.
    -   Quadratic field: it is obtained by extending the field of rational numbers $\mathbf Q$ by adjoining $\sqrt d$, where $d\neq 0,1$ is squarefree. For related content, see [Quadratic field](../number-theory/quadratic.md).

Compared with rings, fields have a very simple additive and multiplicative structure. Hence the structure of a field itself is often very simple. This makes the study of fields very different from the study of rings: one usually turns instead to studying field extensions and the corresponding Galois theory. In algorithm competitions, it is sometimes necessary to compute in extensions of the field of rational numbers or of finite fields. For content on field theory, see [Field theory](./field-theory.md) or related books.

## Applications

Finally, we use the following problem as an example to show how abstract algebraic objects help analyze concrete problems.

???+ note "[【模板】“动态 DP”& 动态树分治（加强版）(Template: “dynamic DP” and dynamic tree decomposition, enhanced version)](https://www.luogu.com.cn/problem/P4751)"
    Given a tree of size $n$ with vertex weights, perform $m$ modifications of vertex weights. After each modification, output the total weight of a maximum weighted independent set of the tree. The problem is forced online.

???+ note "Analysis"
    This problem is the template for dynamic DP; an implementation with the correct complexity requires the [global balanced binary tree](../../ds/global-bst.md), and the concrete sample code is on the corresponding page. Here we only analyze the modeling process in the setting of this problem.
    
    To highlight the key points, for now we do not consider how the global balanced binary tree handles the tree structure, and instead consider the DP problem of the maximum weighted independent set on a chain. Consider each vertex on the chain $[1,n]$ in order; vertex $i$ can be chosen ($1$) or not chosen ($0$). Let the optimal solutions of the subproblem on $[1,i]$ in these two cases be $f_{i,1}$ and $f_{i,0}$ respectively. Thus the DP equation can be written as
    
    $$
    \begin{aligned}
    f_{i,1}&=w_{i}+f_{i-1,0},\\
    f_{i,0}&=\max\{f_{i-1,1},f_{i-1,0}\}.
    \end{aligned}
    $$
    
    Its initial values are $(f_{0,1},f_{0,0})=(0,0)$, and the final answer is $\max\{f_{n,1},f_{n,0}\}$. To express the influence of vertex $i$ on the final result, it suffices to note that this recurrence relation can be written as
    
    $$
    (f_{i,1},f_{i,0})=g(f_{i-1,1},f_{i-1,0};w_i).
    $$
    
    This is a sequence of maps from $\mathbf R^2$ to $\mathbf R^2$ that map $(f_{i-1,1},f_{i-1,0})$ to $(f_{i,1},f_{i,0})$; in the language of groups, these transformations form a monoid under composition of maps. This is exactly what a segment tree can maintain.
    
    However, if such parametrized transformations $g(\cdot;w_i)$ have no special structure, a general map from $\mathbf R^2$ to $\mathbf R^2$ cannot be described by finite-dimensional data. Here another observation is needed: if on $\mathbf R\cup\{-\infty\}$ we define $\max$ as addition and $+$ as multiplication, then $\mathbf R\cup\{-\infty\}$ forms a ring-like structure, where $-\infty$ is the additive identity and $0$ is the multiplicative identity. But it is not a ring, because not all of its elements have additive inverses. Such a structure is called a semiring[^semiring], and the semiring formed here by $(\mathbf R\cup\{-\infty\},\max,+)$ is called the **tropical semiring**.
    
    Based on the tropical semiring $(R,\oplus,\otimes)$, one can define matrix multiplication over it. Namely, for an $m\times n$ matrix $A=(a_{ij})$ and an $n\times p$ matrix $B=(b_{jk})$, their product $AB$ can be defined as $(c_{ik})$, each of whose entries equals
    
    $$
    c_{ik} = \bigoplus_{j=1}^n(a_{ij}\otimes b_{jk}) = \max_{1\le j\le n}\;(a_{ij}+b_{jk}).
    $$
    
    With this notation, the recurrence relation above can be viewed as a linear transformation over the tropical semiring and written in matrix language as
    
    $$
    \left(\begin{matrix}f_{i,1}\\f_{i,0}\end{matrix}\right)
    =\left(\begin{matrix}-\infty&w_i\\0&0\end{matrix}\right)\left(\begin{matrix}f_{i-1,1}\\f_{i-1,0}\end{matrix}\right).
    $$
    
    Hence, it suffices to maintain the product of these matrices over the tropical semiring with a segment tree to answer the dynamic DP problem on a chain with multiple modifications.
    
    Now let us return to the tree version of the problem. For a vertex $i$ of the tree, denote the set of its children by $S(i)$; then the DP equation there is
    
    $$
    \begin{aligned}
    f_{i,1}&=w_i+\sum_{j\in S(i)}f_{j,0},\\
    f_{i,0}&=\sum_{j\in S(i)}\max\{f_{j,1},f_{j,0}\}.
    \end{aligned}
    $$
    
    First, heavy-light decomposition reduces the problem to the chain version. Let $h$ be the heavy child of $i$; then the recurrence above can be written as
    
    $$
    \begin{aligned}
    f_{i,1}&=w_i+f_{h,0}+g_{i,1},\\
    f_{i,0}&=\max\{f_{h,0},f_{h,1}\}+g_{i,0},
    \end{aligned}
    $$
    
    where
    
    $$
    \begin{aligned}
    g_{i,1}&=\sum_{j\in S(i),\ j\neq h}f_{j,0},\\
    g_{i,0}&=\sum_{j\in S(i),\ j\neq h}\max\{f_{j,1},f_{j,0}\}
    \end{aligned}
    $$
    
    summarize the contributions of the light children. As described above, all these transformations can be written in matrix form over the tropical semiring, so the whole problem can be maintained on a segment tree over the heavy-light decomposition. However, a single modification using heavy-light decomposition plus a segment tree directly costs $O(\log^2n)$, so the global balanced binary tree mentioned above is needed to optimize it to $O(\log n)$; of course, it can also be maintained with an LCT.
    
    The tropical semiring mentioned here and the matrix operations above are actually not rare. If $\max$ above is replaced by $\min$, the corresponding tropical semiring is commonly used in shortest path problems. If a square matrix $A$ of dimension $n$ gives the (minimum) edge weights between pairs of vertices of some graph with $n$ vertices, then the entry at $(i,j)$ of $A^k$ is the shortest distance from vertex $i$ to vertex $j$ using at most $k$ edges; in particular, $A^n$ is the distance matrix of the graph. Of course, in an actual implementation one does not really compute this matrix power by brute force, but uses the Floyd algorithm with complexity $O(n^3)$.

## References and notes

-   Dummit, D.S. and Foote, R.M. (2004) Abstract Algebra. 3rd Edition, John Wiley & Sons, Inc.
-   [Tropical semiring - Wikipedia](https://en.wikipedia.org/wiki/Tropical_semiring)

[^oi-wiki-not-wikipedia]: Because [OI Wiki is not an encyclopaedia](../../intro/what-oi-wiki-is-not.md#oi-wiki-is-not-an-encyclopaedia).

[^ring-wiki]: [Ring (mathematics) - Wikipedia](https://en.wikipedia.org/wiki/Ring_%28mathematics%29)

[^zero-multiplication]: The derivation of this identity is $0\cdot a+0 = 0\cdot a = (0+0)\cdot a = 0\cdot a + 0\cdot a$, where the first and second equalities are the definition of the additive identity, the third equality is the distributive property, and the final implication is the cancellation law for addition. Multiplication on the other side is similar.

[^semiring]: A semiring is the algebraic structure obtained by relaxing, in the definition of a ring with identity, the requirement that inverses must exist for addition, i.e. the additive structure is a commutative monoid and the multiplicative structure is a monoid. For more information, see [Wikipedia](https://en.wikipedia.org/wiki/Semiring).
