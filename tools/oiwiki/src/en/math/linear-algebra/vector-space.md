---
title: Vector space
---

A vector (linear) space is a generalization of $d$-dimensional Euclidean space ($0\leq d\leq 3$) and similar structures; the relationship between the corresponding concepts is shown in [Relationship between Euclidean space and vector space](#relationship-between-euclidean-space-and-vector-space).

Prerequisites: Abelian group, field.

Informally, a set that is closed under some operation and satisfies associativity, has an identity element and inverse elements forms a group. If commutativity also holds, it forms an Abelian group.

If a set is closed under the four arithmetic operations, it forms a field. See [Basic concepts of abstract algebra](../algebra/basic.md#域) for the relevant definitions.

## Definition

A vector space (linear space) is a fundamental concept and an important object of study in linear algebra. A vector space is a module-like algebraic structure consisting of a set of vectors $V$, a field $\Bbb{P}$, an addition operation $+$ and scalar multiplication.

Concretely, let $(V,+)$ be an Abelian group and $\Bbb{P}$ a field.

We define an algebraic operation between numbers in $\Bbb{P}$ and elements of $V$, called **scalar multiplication**: $\cdot:\Bbb{P}\times V\mapsto V$, written $p\cdot v$ or $pv$, where $p$ is in the field $\Bbb{P}$ and $v$ is in the Abelian group $V$. This operation is required to be closed, i.e. the result is always meaningful and also lies in the group $V$.

Furthermore, the following conditions must hold:

1.  **Distributivity of scalar multiplication over vector addition**: for $\mathbf u,\mathbf v\in V,a\in \Bbb{P}$, $a(\mathbf u+\mathbf v)=a\mathbf u+a\mathbf v$
2.  **Distributivity of scalar multiplication over scalar addition**: for $a,b\in \Bbb{P},\mathbf u\in V$, $(a+b)\mathbf u=a\mathbf u+b\mathbf u$
3.  **Associativity of scalar multiplication (compatibility with field multiplication)**: for $a,b\in \Bbb{P},\mathbf u\in V$, $a(b\mathbf u)=(ab)\mathbf u$
4.  **Identity element of scalar multiplication**: let $1\in \Bbb{P}$ be the multiplicative identity of $\Bbb{P}$; then for $u\in V$, $1\mathbf u=\mathbf u$

Then the algebraic structure $(V,+,\cdot,\mathbb{P})$ is said to be a **vector space** over $\Bbb{P}$ formed by $V$ with respect to $+,\cdot$; $\Bbb{P}$ is the **base field** (field of scalars) of the vector space, the elements of $V$ are called **vectors**, and the elements of $\Bbb{P}$ are called **scalars**. When the field $\Bbb{P}$ is the field of real numbers, it is called a real vector space. When the field $\Bbb{P}$ is the field of complex numbers, it is called a complex vector space.

Whether it is a list of numbers, arrows, or something else entirely, anything satisfying the axioms above can be regarded as a vector, and can therefore be studied using the theory of linear algebra.

The identity element of the additive group is called the zero vector and is written $\mathbf 0$ or $\mathbf\theta$.

The addition and subtraction of vectors from the original Abelian group, together with the newly defined scalar multiplication of the vector space, are collectively called **linear operations**.

???+ note "Note"
    For convenience, in the text below:
    
    1.  Elements of $V$ are not written in bold.
    2.  An algebraic structure $(V,+,\cdot,\mathbb{P})$ satisfying the definition of a vector space is also called a vector space.
    
    Please keep the distinction in mind.

### Intuitive understanding

Loosely speaking, scalar multiplication corresponds to a kind of "**scaling**", the elements of the base field $\Bbb{P}$ represent the "**ratio**" of the scaling, and vector addition corresponds to "**superposition**". At the same time, the elements of $\Bbb{P}$ also represent the range of values that the "**coordinates**" of a vector can take.

Conditions 1–4 describe the relationship between "scaling" and "superposition". They can be understood with the help of arrows in the two-dimensional plane.

### Simple properties

???+ note "Note"
    The following properties can be found in group theory and related areas.

For a vector space $(V,+,\cdot,\Bbb{P})$,

1.  $\theta$ is unique
2.  $\forall\alpha\in V$, $-\alpha$ is unique
3.  $\exists 0\in\mathbb{P}$, $\forall\alpha\in V$, we have $0\alpha=\theta$
4.  $\forall k\in\mathbb{P}$, we have $k\theta=\theta$
5.  $(-1)\alpha=-\alpha,~\forall\alpha\in V$
6.  No zero divisors: $\forall\alpha\in V,k\in\mathbb{P}$, we have $k\alpha=\theta\implies k=0\lor\alpha=\theta$
7.  Cancellation law of addition: $\forall\alpha,\beta,\gamma\in V$, we have $\alpha+\beta=\alpha+\gamma\implies\beta=\gamma$

    > In fact, the cancellation law of addition is a property of Abelian groups.

### Examples

1.  $\Bbb{P}^n$ forms a vector space over $\Bbb{P}$ with respect to the addition and multiplication of the field $\Bbb{P}$. For example, $\Bbb{P}$ may be $\Bbb{R}$, $\Bbb{C}$, $\Bbb{N}_p$ ($p$ prime), etc.
2.  The $n\times m$ matrices $\Bbb{P}^{n\times m}$ over the field $\Bbb{P}$ form a vector space over $\Bbb{P}$ with respect to matrix addition and scalar multiplication.
3.  The univariate polynomial ring $\Bbb{P}[x]$ over the field $\Bbb{P}$ forms a vector space over $\Bbb{P}$ with respect to polynomial addition and scalar multiplication.
4.  The set of all continuous functions on the interval $[a,b]$ (denoted $C[a,b]$) forms a vector space over the field of values with respect to "addition of functions" and "multiplication of a continuous function by a value".

## Related concepts

### Linear dependence and linear independence

For a vector space $(V,+,\cdot,\Bbb{P})$:

1.  $a_1,a_2,\dots,a_n\in V$ is called a **set of vectors** (family of vectors) in $V$.
2.  For $k_1,k_2,\dots,k_n\in\Bbb{P}$, $\sum_{i=1}^nk_ia_i$ is called a **linear combination** of the set of vectors $a_1,a_2,\dots,a_n$.
3.  If a vector $\beta\in V$ can be written as a linear combination of the set of vectors $a_1,a_2,\dots,a_n$, we say that $\beta$ can be **linearly expressed** by the set of vectors $a_1,a_2,\dots,a_n$.
4.  For $k_1,k_2,\dots,k_n\in\Bbb{P}$, if the set of vectors $a_1,a_2,\dots,a_n$ satisfies $\sum_{i=1}^nk_ia_i=\theta\iff k_i=0, i=1,2,\dots,n$, the set of vectors $a_1,a_2,\dots,a_n$ is called **linearly independent**; otherwise the set of vectors $a_1,a_2,\dots,a_n$ is called **linearly dependent**.

By convention, the zero vector is linearly dependent with any vector.

An expression for a linear representation or a linear dependence can be written in the form of a matrix multiplication:

$$
\beta=k_1a_1+k_2a_2+\cdots+k_ra_r=(a_1,a_2,\cdots,a_r)\begin{pmatrix} k_1 \\ k_2 \\ \vdots \\ k_r \end{pmatrix}
$$

By convention, the vectors $a$ are written side by side in order on the left, and the scalars $k$ are written vertically in order on the right, forming a "column vector".

Note: the "column vector" formed by the scalars here is merely a convenient formal notation; it is not in the space $V$ and is fundamentally different from the vectors on the left. If the vectors on the left happen to be column vectors, placing them side by side formally yields a "matrix", and the product above is exactly the familiar form "matrix times column vector on the right" from matrix algebra.

It is shown below that the linear representation here is also equivalent to the vector $\beta$ lying in the image of the matrix $(a_1,a_2\cdots,a_r)$.

According to the definition below, the zero vector always lies in the image. From the viewpoint of linear transformations, linear dependence is equivalent to several vectors being mapped to the zero vector after the transformation, while linear independence is equivalent to only the zero vector itself being mapped to the zero vector.

#### Properties

For a vector space $(V,+,\cdot,\Bbb{P})$,

1.  If a part of a set of vectors is linearly dependent, then the set of vectors is linearly dependent. If a set of vectors is linearly independent, then every nonempty subset of it is linearly independent. In short: **"large independent, small independent"; "small dependent, large dependent"**.
2.  A set of vectors containing $\theta$ is linearly dependent.
3.  A set of vectors is linearly dependent if and only if some vector in it can be linearly expressed by the remaining vectors.
4.  If a vector $\beta$ can be linearly expressed by the set of vectors $a_1,a_2,\dots,a_n$, then the representation is unique if and only if the set of vectors $a_1,a_2,\dots,a_n$ is linearly independent.
5.  If the set of vectors $a_1,a_2,\dots,a_n$ is linearly independent, then a vector $\beta$ can be linearly expressed by the set of vectors $a_1,a_2,\dots,a_n$ if and only if the set of vectors $a_1,a_2,\dots,a_n,\beta$ is linearly dependent.

### Maximal linearly independent subset, rank

Linear dependence can be understood as "redundancy": it means that some vectors in the set can be expressed by the others and can be removed. After removing them, a maximal linearly independent subset remains.

For a vector space $(V,+,\cdot,\Bbb{P})$:

1.  For a set of vectors $b_1,b_2,\dots,b_m$, let $\{a_1,a_2,\dots,a_n\}\subseteq\{b_1,b_2,\dots,b_m\}$ be such that:

    -   the set of vectors $a_1,a_2,\dots,a_n$ is linearly independent;
    -   $\forall\beta\in\{b_1,b_2,\dots,b_m\}\setminus\{a_1,a_2,\dots,a_n\}$, the set of vectors $a_1,a_2,\dots,a_n,\beta$ is linearly dependent.

    Then the set of vectors $a_1,a_2,\dots,a_n$ is called a **maximal linearly independent subset** of the set of vectors $b_1,b_2,\dots,b_m$. Similarly, one can define a maximal linearly independent subset of the vector space $V$.

    By convention, the maximal linearly independent subset of the set of vectors $\theta,\theta,\dots,\theta$ is the empty set, so the set of vectors corresponding to an all-$0$ matrix has no maximal linearly independent subset.

    The way of removing vectors from a set is not unique, so the maximal linearly independent subset is not unique either. It is customary to remove them in order from left to right.

    Conveniently, when removing in order, the vectors that remain are exactly the columns in which the entries $1$ are located in the reduced row echelon form matrix left by Gaussian elimination in the "row" viewpoint.

    The size of a maximal linearly independent subset of the set of vectors $b_1,b_2,\dots,b_m$ is called the **rank** of the set of vectors and is denoted $\operatorname{rank}\{b_1,b_2,\dots,b_m\}$; by convention, $\operatorname{rank}\{\theta,\theta,\dots,\theta\}=0$.

    Thus the definition of the rank of a set of vectors coincides exactly with the definition of the rank of a matrix.

2.  If the set of vectors $a_1,a_2,\dots,a_n$ can linearly express all vectors of the set of vectors $b_1,b_2,\dots,b_m$, we say that the set of vectors $b_1,b_2,\dots,b_m$ can be linearly expressed by the set of vectors $a_1,a_2,\dots,a_n$.

3.  If the set of vectors $a_1,a_2,\dots,a_n$ can be linearly expressed by the set of vectors $b_1,b_2,\dots,b_m$, and the set of vectors $b_1,b_2,\dots,b_m$ can be linearly expressed by the set of vectors $a_1,a_2,\dots,a_n$, the two sets of vectors are called **equivalent**, written $\{a_1,a_2,\dots,a_n\}\cong\{b_1,b_2,\dots,b_m\}$.

    **Equivalence** of sets of vectors means that they span the same space. Sets of vectors spanning the same space are equivalent to each other, and sets of vectors spanning different spaces are not equivalent.

    Equivalence of sets of vectors is a stronger condition than equivalence of matrices: not only must the ranks be equal, but the spaces must be exactly the same. Therefore, if two matrices are concatenated **horizontally**, the rank must not change.

    Equivalence of matrices only requires equal rank, so equivalence of matrices means that the first matrix or space can be transformed into the second matrix or space by an invertible transformation.

#### Properties

For a vector space $(V,+,\cdot,\Bbb{P})$,

1.  Suppose the set of vectors $a_1,a_2,\dots,a_n$ can be linearly expressed by the set of vectors $b_1,b_2,\dots,b_m$.
    -   If $n>m$, then the set of vectors $a_1,a_2,\dots,a_n$ is linearly dependent.
    -   If the set of vectors $a_1,a_2,\dots,a_n$ is linearly independent, then $n\leq m$.

2.  Equivalent linearly independent sets of vectors have the same size.

    All maximal linearly independent subsets of a set of vectors have the same size.

3.  A set of vectors is linearly independent if and only if its rank equals its size.

4.  If the set of vectors $a_1,a_2,\dots,a_n$ can be linearly expressed by the set of vectors $b_1,b_2,\dots,b_m$, then $\operatorname{rank}\{a_1,a_2,\dots,a_n\}\leq\operatorname{rank}\{b_1,b_2,\dots,b_m\}$.

5.  Equivalent sets of vectors have equal rank.

### Linear span

For a vector space $(V,+,\cdot,\Bbb{P})$, the set $\left\{v=\sum_{i=1}^nk_ia_i:a_i\in V,k_i\in\Bbb{P},i=1,2,\dots,n\right\}$ also forms a vector space, called the vector space **spanned** by the set of vectors $a_1,a_2,\dots,a_n$ (or the **linear span**), denoted $\operatorname{span}\{a_1,a_2,\dots,a_n\}$.

The $n$ vectors $a$ here need not be linearly independent.

### Subspace

For a vector space $(V,+,\cdot,\Bbb{P})$, if the algebraic structure $(V_1,+,\cdot,\Bbb{P})$ satisfies:

1.  $\varnothing\ne V_1$
2.  $V_1\subseteq V$
3.  $V_1$ forms a vector space over $\mathbb{P}$ with respect to $+,\cdot$

then $V_1$ is called a linear subspace (or simply a subspace) of $V$, written $V_1\leq V$.

Every space $V$ has two **trivial subspaces**: $V$ itself and the zero subspace. The zero subspace contains only the zero vector and contains no linearly independent vectors.

If $\subseteq$ in condition 2 is replaced by $\subset$, then $V_1$ is called a proper subspace of $V$, written $V_1<V$.

It is not hard to prove: a nonempty subset $V_1$ of a vector space $V$ is a subspace if and only if the linear operations are closed on $V_1$, i.e.:

1.  $\forall u,v\in V_1$, $u+v\in V_1$
2.  $\forall v\in V_1$, $\forall k\in \Bbb{P}$, $kv\in V_1$

### Intersection, sum and direct sum, direct product

For vector spaces $(V_1,+,\cdot,\Bbb{P})$ and $(V_2,+,\cdot,\Bbb{P})$:

1.  It is easy to verify that addition and scalar multiplication are closed on $V_1\cap V_2$, so $V_1\cap V_2$ is called the **intersection** of the vector spaces $V_1$ and $V_2$.

    Similarly, one can define the intersection of several vector spaces $\bigcap_{i=1}^m V_i$.

2.  If a vector space $V$ satisfies $V=\{u+v|u\in V_1,v\in V_2\}$, then $V$ is called the **sum** of the vector spaces $V_1$ and $V_2$, written $V=V_1+V_2$.

    One can verify that $V_1+V_2$ is the smallest subspace containing $V_1\cup V_2$.

    Similarly, one can define the sum of several vector spaces $\sum_{i=1}^m V_i$.

3.  Let $V=V_1+V_2$. If for every element $v$ of the vector space $V$ there is only one pair of vectors $v_1,v_2$ satisfying $v=v_1+v_2$, then $V$ is called the **direct sum** of the vector spaces $V_1$ and $V_2$, written $V_1\oplus V_2$.

    Similarly, one can define the direct sum of several vector spaces $\bigoplus_{i=1}^m V_i$.

4.  The **direct product** $V_1\times V_2$ of $V_1$ and $V_2$ is defined as their Cartesian product, which forms a vector space over $\Bbb{P}$ with respect to the following addition and scalar multiplication:

    1.  $+:(V_1\times V_2)\times(V_1\times V_2)\mapsto V_1\times V_2; ((u_1,v_1),(u_2,v_2))\to (u_1+u_2,v_1+v_2)$
    2.  $\cdot:\Bbb{P}\times(V_1\times V_2)\mapsto V_1\times V_2; (k,(u,v))\to (ku,kv)$

    Similarly, one can define the direct product of several vector spaces $\prod_{i=1}^m V_i$.

#### Examples

For the vector space $V=\Bbb{R}^3$, consider the vector spaces:

-   $V_1:=\{(x,0,0)|x\in\Bbb{R}\}$
-   $V_2:=\{(x,y,0)|x,y\in\Bbb{R}\}$
-   $V_3:=\{(0,y,z)|y,z\in\Bbb{R}\}$
-   $V_4:=\{(x,0,z)|x,z\in\Bbb{R}\}$

Then

1.  $V_1<V_2<V$, $V_3<V$
2.  $V_2=V_1+V_2$
3.  $V=V_1\oplus V_3=V_2+V_3$
4.  $V_2+V_3\leq V$

#### Properties

1.  Let $V_1,V_2,V_3$ be vector spaces over $\Bbb{P}$. Just like the intersection of sets, the intersection of vector spaces obeys the following rules:
    1.  Commutativity: $V_1\cap V_2=V_2\cap V_1$
    2.  Associativity: $V_1\cap(V_2\cap V_3)=(V_1\cap V_2)\cap V_3$
2.  Let $V_1,V_2,V_3$ be vector spaces over $\Bbb{P}$. Similarly to the union of sets, the sum of vector spaces obeys the following rules:
    1.  Commutativity: $V_1+V_2=V_2+V_1$
    2.  Associativity: $V_1+(V_2+V_3)=(V_1+V_2)+V_3$
3.  Let $V_1,V_2,V_3$ be vector spaces over $\Bbb{P}$. The intersection and sum of vector spaces are related as follows:
    1.  $V_1\cap (V_2+V_3)\supseteq (V_1\cap V_2)+(V_1\cap V_3)$
    2.  $V_1+(V_2\cap V_3)\subseteq (V_1+V_2)\cap (V_1+V_3)$
4.  $\operatorname{span}\{a_1,a_2,\dots,a_n\}+\operatorname{span}\{b_1,b_2,\dots,b_m\}=\operatorname{span}\{a_1,a_2,\dots,a_n,b_1,b_2,\dots,b_m\}$
5.  Let $V_1,V_2$ be vector spaces over $\Bbb{P}$. Then the following statements are equivalent:

    1.  $V_1+V_2=V_1\oplus V_2$

    2.  $\exists \beta\in V_1+V_2$ whose decomposition into a sum of vectors from $V_1$ and $V_2$ is unique ("for all" $\to$ "there exists")

    3.  The decomposition of $\theta$ into a sum of vectors from $V_1$ and $V_2$ is unique

    4.  $V_1\cap V_2=\{\theta\}$

    ???+ note "Proof"
        $1\implies 2$: follows immediately from the definition.
        
        $2 \implies 3$:
        
        Let $\beta=\beta_1+\beta_2$, where $\beta_1\in V_1, \beta_2\in V_2$. If $\theta=\alpha_1+\alpha_2$, $\theta\ne\alpha_1\in V_1,\alpha_2\in V_2$, then $\beta=\beta+\theta=(\beta_1+\alpha_1)+(\beta_2+\alpha_2)$.
        
        But $\beta_1\ne\beta_1+\alpha_1$, which contradicts the assumption.
        
        $3 \implies 4$:
        
        Take a nonzero vector $\alpha$ lying in both $V_1$ and $V_2$. Then $\theta=\alpha+(-\alpha)=(-\alpha)+\alpha$, which contradicts the assumption.
        
        $4 \implies 1$:
        
        If $V_1+V_2$ is not a direct sum, then there exists $\beta\in V_1+V_2$ such that $\beta=\beta_1+\beta_2=\gamma_1+\gamma_2$, where $\beta_1,\gamma_1\in V_1,\beta_2,\gamma_2\in V_2$ and $\beta_1,\beta_2,\gamma_1,\gamma_2$ are pairwise distinct.
        
        Then $\theta\ne\beta_1-\gamma_1=\gamma_2-\beta_2\in V_1\cap V_2$, which contradicts the assumption.

### Isomorphism

Let $V,V'$ both be vector spaces over the field $\Bbb{P}$. If there exists a bijection $\sigma:V\mapsto V'$ that preserves addition and scalar multiplication, i.e. $\forall u,v\in V$, $\forall k\in\Bbb{P}$:

1.  $\sigma(u+v)=\sigma(u)+\sigma(v)$
2.  $\sigma(ku)=k\sigma(u)$

then $\sigma$ is called an **isomorphism** from $V$ to $V'$, and $V$ and $V'$ are said to be **isomorphic**, written $V\cong V'$.

???+ note "Note"
    If $\sigma$ is injective, one can define a **monomorphism**; if $\sigma$ is surjective, one can define an **epimorphism**.

#### Properties

1.  Two vector spaces over the field $\Bbb{P}$ are isomorphic if and only if their dimensions are equal. (For the definition of dimension, see [Linear basis](./basis.md).)
2.  (Corollary of 1) An $n$-dimensional vector space over the field $\Bbb{P}$ is isomorphic to the vector space $\Bbb{P}^n$.

    ???+ note "Note"
        This property shows that we can essentially identify coordinates with vectors.

## Relationship between Euclidean space and vector space

Taking the three-dimensional Euclidean space we are most familiar with as an example, some of its related concepts correspond to concepts in vector spaces as shown in the following table:

| Three-dimensional Euclidean space | Vector space |
| -------- | ----------------- |
| vector | vector |
| perpendicularity | orthogonality (i.e. inner product equal to $0$) |
| three vectors collinear/coplanar | $k$ vectors linearly dependent |
| three vectors not coplanar | $k$ vectors linearly independent |
| basis vectors | [linear basis](./basis.md) |
| dimension of the space | dimension of the space |

## Applications

From this section on, we mainly discuss the "column" viewpoint of systems of linear equations.

The matrix $A$ itself is also made up of column vectors. We regard $A$ itself as a set of column vectors, with $x$ as the unknown coefficients, and ask whether this set of column vectors in $A$, paired with the unknowns, can be combined to produce the column vector $b$. Here the column vector $x$ is completely unknown.

The equation $Ax=b$ under study can then be rearranged as:

$$
\alpha_1 x_1 +\alpha_2 x_2 +\cdots+\alpha_n x_n=b 
$$

In this case, in the matrix multiplication, the matrix $A$ on the left can be viewed as a set of vectors, namely a set of column vectors. This set of column vectors, as a basis, spans a space, and the question is whether the column vector $b$ falls within this space.

### Solutions of systems of linear equations from the column viewpoint

The rank is the number of vectors in a maximal linearly independent subset and represents the "constraints". The remaining vectors then give the solution its degrees of freedom, i.e. they allow redundant vectors to be added in other directions.

If $n$ denotes the number of columns of the matrix $A$, i.e. the number of column vectors it contains, and $r(A)$ denotes the rank of the matrix A, then the number of degrees of freedom $S$ is:

$$
S=n-r(A)
$$

The set of all solutions of the system also forms a set of vectors, and the number of degrees of freedom $S$ is exactly the rank of the set of solution vectors of $Ax=0$, i.e. the dimension of the kernel discussed below.

### Equivalence of systems of equations

The common solutions of two systems of equations are defined as the intersection of their two solution sets.

Two systems of equations are **equivalent** (have the same solutions) if their solution sets are equal. Systems with equal solution sets are equivalent, and systems with different solution sets are not equivalent.

Equivalence of systems of equations is also a stronger condition than equivalence of matrices: not only must the ranks be equal, but the rank must remain unchanged after the two matrices are concatenated **vertically**.

Compare this with equivalence of sets of vectors, which requires that the rank remain unchanged when the matrices are concatenated horizontally. Therefore, the following relationship holds:

Equivalence of matrices does not necessarily imply equivalence of the corresponding sets of vectors or equivalence of the systems of equations, but equivalence of sets of vectors or equivalence of systems of equations necessarily implies equivalence of the corresponding matrices (equal rank).

If the sets of vectors corresponding to the matrices are equivalent, then after transposing the matrices the corresponding systems of equations are equivalent, and vice versa.

### Kernel and image of a matrix

The kernel and image in this part are described from the viewpoint of vector spaces.

For a matrix $A$, let $W$ be the set of all solutions $x$ of the equation $Ax=0$. Then $W$ is a vector space, and the field of scalars of $W$ is the same as the field containing the entries of $A$.

Such a $W$ is called the **kernel** (null space) of the matrix $A$, denoted $N(A)$.

The kernel $N(A)$ of the matrix $A$ is exactly the **solution space** of the equation $Ax=0$. According to the definition of a basis given later, the **fundamental system of solutions** of this equation is exactly a basis of the kernel.

If the matrix $A$ is invertible, then the kernel $N(A)$ of $A$ contains only the zero vector.

For a matrix $A$ whose $n$ columns are the vectors $\alpha$, the space spanned by the $n$ column vectors $\alpha$ is called the **image** of $A$, or the **column space**, denoted:

$$
R(A)=\operatorname{span}\{\alpha_1,\alpha_2,\cdots,\alpha_n\}
$$

According to the definition of dimension given later, the dimension of the image equals the rank of the matrix $A$.

By definition, every element $y$ of the image $R(A)$ has a corresponding representation:

$$
y=k_1\alpha_1+k_2\alpha_2+\cdots+k_n\alpha_n=(\alpha_1,\alpha_2,\cdots,\alpha_n)\begin{pmatrix}k_1\\k_2\\\vdots\\k_n\end{pmatrix}=A\begin{pmatrix}k_1\\k_2\\\vdots\\k_n\end{pmatrix}
$$

Therefore the image $R(A)$ is exactly the **range** of $Ax$ over all vectors $x$.

Similarly, one can define the **row space** of $A$, i.e. the range $R(A^T)$ of the transpose of $A$.

Since the row rank of a matrix equals its column rank, the dimension of the row space also equals the rank of the matrix, so transposition changes the image but does not change the dimension of the image.

Here we can establish a correspondence with the preceding text:

Equivalence of sets of vectors is equivalent to the corresponding matrices having the same image $R(A)$.

Equivalence of systems of equations is equivalent to the corresponding matrices having the same row space $R(A^T)$.

## References and notes

1.  丘维声，高等代数（下）．清华大学出版社． (Qiu Weisheng, Advanced Algebra (Vol. 2). Tsinghua University Press.)
2.  [Vector space](https://en.wikipedia.org/w/index.php?title=Vector_space&oldid=1108546097). *Wikipedia, The Free Encyclopedia*.
