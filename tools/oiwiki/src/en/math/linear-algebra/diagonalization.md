---
title: Diagonalization
---

## Eigenspace

All eigenvectors of the matrix $A$ belonging to the eigenvalue $\lambda_0$, together with the zero vector, form a linear space called an eigenspace of the matrix $A$, denoted $E(\lambda_0)$. It is the solution space of the homogeneous linear system:

$$
(\lambda_0 I-A)X=0
$$

that is, the set of all solutions of that system.

For the eigenspace $E(\lambda_i)=N(\lambda_i I-A)$, the rank–nullity theorem gives:

$$
r(\lambda_i I-A)+\operatorname{dim} N(\lambda_i I-A)=n
$$

Therefore, the dimension of the eigenspace $E(\lambda_i)$ is:

$$
\operatorname{dim} E(\lambda_i)=n-r(\lambda_i I-A)
$$

It is also called the **geometric multiplicity** of $\lambda_i$.

## Invariant subspaces

When studying a linear operator $T$, we often want to choose a basis of the space $V$ in which the matrix of the linear operator $T$ has as simple a shape as possible.

Let $V$ be a linear space over a field $F$, $W$ a subspace of $V$, and $T$ a linear operator on $V$. If for every vector $x$ in $W$, $T(x)$ also lies in $W$ (we also say that the subspace is invariant or stable under the operator), we say that $W$ is an invariant subspace of $T$.

That the space is invariant under the operator does not mean that the coordinates really stay "unchanged"; there may be a stretch or some other deformation, but the result still lands in the space.

-   Every subspace of the linear space $V$ is an invariant subspace of scalar multiplication.
-   For every linear operator $T$ on $V$, the space $V$ and the zero subspace are invariant subspaces of $T$; they are called the trivial invariant subspaces.
-   The intersection and the sum of invariant subspaces are also invariant subspaces.

Let $W$ be an invariant subspace of the linear operator $T$. Considering only the action of $T$ on the invariant subspace $W$, we obtain a linear operator on the subspace $W$ itself, called the restriction of $T$ to the subspace $W$ and denoted ${T|}_W$.

For every linear operator $T$ on $V$, the image $R(T)$ and the kernel $N(T)$ are invariant subspaces of $T$. The meaning of these two cases is that, under the operator, the space $V$ is compressed into itself (the image) or compressed to $0$ (the kernel).

For every linear operator $T$ on $V$, the eigenspaces of $T$ are invariant subspaces of $T$.

## Primary decomposition

By the fundamental theorem of algebra, the minimal polynomial can be factored as:

$$
m_A(\lambda)={(\lambda-\lambda_1)}^{r_1}\cdots{(\lambda-\lambda_S)}^{r_S}
$$

Substituting the matrix $A$ for the variable $\lambda$ in the minimal polynomial, the kernels of the individual factors form a series of invariant subspaces of the matrix $A$:

$$
W_i=N({(\lambda_i I-A)}^{r_i})
$$

Theorem: The dimension of this invariant subspace $W_i$ is exactly the algebraic multiplicity of the eigenvalue $\lambda_i$.

Recall that the algebraic multiplicity is the degree of the corresponding factor of the characteristic polynomial, and the geometric multiplicity is the dimension of the eigenspace $E(\lambda_i)=N(\lambda_i I-A)$. This invariant subspace $W_i$ and the eigenspace $E(\lambda_i)$ are both kernels of matrices, and the two matrices are related as a matrix and its $r_i$-th power from the minimal polynomial. In other words, the dimension of the eigenspace is the geometric multiplicity, and after raising to the $r_i$-th power from the minimal polynomial the "eigenspace" becomes an "invariant subspace" whose dimension reaches the algebraic multiplicity from the characteristic polynomial.

This theorem is in fact a corollary of the primary decomposition theorem below.

Denote by $T$ the linear operator corresponding to the matrix $A$, and by $T_i={T|}_{W_i}$ its restriction to each subspace $W_i$. Then the minimal polynomial of $T_i$ is $(x-\lambda_i)^{r_i}$.

Theorem: Let $V$ be a linear space over a field $F$, and $T$ a linear operator on $V$. Then the space $V$ admits a primary decomposition with respect to the linear operator $T$, i.e., it splits into a direct sum of several invariant subspaces $W_i$.

$$
V=W_1\oplus W_2\oplus\cdots\oplus W_S
$$

This means that the matrix of $T$ in some basis is block diagonal (quasi-diagonal):

$$
\operatorname{diag}\{A_1,A_2,\cdots,A_S\}
$$

where $A_i$ is the matrix of $T_i$ in the corresponding basis.

The theorem shows that invariant subspaces can be used to simplify the matrix of a linear operator.

## Diagonalizable matrices

If a square matrix $A$ of order $n$ is similar to a diagonal matrix, we say that $A$ is a diagonalizable matrix, or a simple (semisimple) matrix.

-   The sum, product, and inverse of diagonal matrices, if they exist, are again diagonal matrices, and the entries on their diagonal are exactly their eigenvalues.
-   The matrix of a linear operator $T$ is diagonalizable if and only if the matrix of $T$ in some basis is diagonal.

Theorem: Let $\lambda_1,\cdots,\lambda_m$ be all the distinct eigenvalues of the matrix $A$. Then the following statements are equivalent:

-   The matrix $A$ is diagonalizable.
-   The matrix $A$ has $n$ linearly independent eigenvectors.
-   The following formula holds:

$$
\operatorname{dim} E(\lambda_1)+\cdots+\operatorname{dim} E(\lambda_m)=n
$$

We pointed out earlier that the exponent of an eigenvalue in the factorization of the characteristic polynomial is called the algebraic multiplicity, and the dimension of the eigenspace is called the geometric multiplicity. This theorem also shows that the matrix $A$ is diagonalizable if and only if, for every eigenvalue $\lambda$ of $A$, the algebraic multiplicity equals the geometric multiplicity.

Corollary: If a square matrix $A$ of order $n$ has exactly $n$ distinct eigenvalues, then it is necessarily diagonalizable. The converse need not hold.

Theorem: The matrix $A$ is diagonalizable if and only if the minimal polynomial of $A$ has no repeated roots.

Matrix similarity also preserves the linear dependence relations among eigenvectors.

Eigenvectors may very well fail to be real, and it may very well be impossible to find $n$ linearly independent eigenvectors.

For a repeated eigenvalue, the eigenvectors span a space. To describe this space, representatives must be chosen from it. Usually linearly independent representatives are chosen, and the number of representatives equals the dimension of the space.

When choosing representatives, they are often orthogonalized and normalized. What we finally obtain is a set of orthonormal representatives.

Eigenvectors are not necessarily orthogonal; eigenvectors of different eigenvalues may not be orthogonalizable. Therefore, orthogonalization can only be performed on eigenvectors of a repeated eigenvalue. Normalization, however, can be performed on any eigenvector.

## Nilpotent matrices

Let $T$ be a linear operator on the space $V$. If there is a positive integer $r$ such that $T^r$ is the zero operator, we say that $T$ is a nilpotent operator on the space $V$.

A matrix satisfying the condition $N^r=0$ for some positive integer $r$ is called a nilpotent matrix.

Usually one may further assume that $r$ is the smallest positive integer for which $T^r$ is the zero operator; then the minimal polynomial of $T$ is $x^r$. Hence there is a vector $\xi_0$ such that:

-   $$
    T^r(\xi_0)=0
    $$
-   $$
    T^{r-1}(\xi_0)\neq 0
    $$

### Cyclic subspaces

Theorem: Let $T$ be a linear operator on the space $V$, and $\xi$ a vector of the space $V$. If there is a positive integer $s$ such that:

-   $$
    T^s(\xi)=0
    $$
-   $$
    T^{s-1}(\xi)\neq 0
    $$

then the vectors $\xi,T(\xi),\cdots,T^{s-1}(\xi)$ are linearly independent.

This theorem allows us to give a definition:

Let $T$ be a linear operator on the space $V$, and $W$ a subspace of $V$. If there are a vector $\xi_0$ and a positive integer $r$ such that:

-   the vectors $\xi_0,T(\xi_0),\cdots,T^{r-1}(\xi_0)$ form a basis of $W$,
-   the following equation holds:

    $$
    T^r(\xi_0)=0
    $$

then the subspace $W$ is called a cyclic subspace with respect to $T$, or a $T$-cyclic subspace for short. In this case $\xi_0$ is called a generating vector of the cyclic subspace $W$, and the vectors $\xi_0,T(\xi_0),\cdots,T^{r-1}(\xi_0)$ are called a cyclic basis of $W$.

Clearly, a $T$-cyclic subspace $W$ is invariant under $T$, and for every vector $\xi$ in the cyclic subspace $W$ we have $T^r(\xi)=0$, where $r$ is the dimension of the cyclic subspace.

### Nilpotent Jordan blocks

If the space $W$ is a cyclic subspace of the operator $T$, then the restriction ${T|}_W$ of $T$ to $W$ is a nilpotent operator on $W$, and the matrix of ${T|}_W$ with respect to the reversed cyclic basis $T^{r-1}(\xi_0),T^{r-2}(\xi_0),\cdots,\xi_0$ of $W$ is an upper triangular matrix of order $r$ of the following shape:

$$
N_r=\begin{pmatrix}
0 & 1 & 0 & \cdots & 0 & 0\\
0 & 0 & 1 & \cdots & 0 & 0\\
0 & 0 & 0 & \cdots & 0 & 0\\
\vdots & \vdots & \vdots &   & \vdots& \vdots\\
0 & 0 & 0 & \cdots & 0 & 1\\
0 & 0 & 0 & \cdots & 0 & 0\\
\end{pmatrix}
$$

The matrix $N_r$ is called a nilpotent Jordan matrix of order $r$, or a nilpotent Jordan block of order $r$.

Let $T$ be a nilpotent operator on the $n$-dimensional space $V$. The uniquely determined sequence of positive integers $r_1\geq\cdots\geq r_S$ appearing in the decomposition of $V$ into $T$-cyclic subspaces is called the invariant exponents (indices) of $T$.

For a nilpotent matrix $A$ of order $n$, $A$ is similar to a matrix $N$ of the above shape and also uniquely determines a sequence of positive integers $r_1\geq\cdots\geq r_S$, called the invariant exponents of the matrix $A$.

Although a nilpotent matrix cannot be similar to a diagonal matrix, it is similar to such a standard form. The Jordan normal form combines diagonalization by similarity with the standard form of nilpotent matrices, and gives the standard form that a general matrix can reach by a similarity transformation.

### Some theorems

1.  Let $T$ be a nilpotent operator on the space $V$, and let

    $$
    h(x)=a_0+a_1x+\cdots+a_mx^m
    $$

    be a polynomial. Then the linear operator $h(T)$ has an inverse if and only if $a_0\neq 0$. When $h(T)$ is invertible, the inverse of $h(T)$ is also a polynomial in $T$.

2.  Let $T$ be a nilpotent operator on the space $V$, $W$ an $r$-dimensional $T$-cyclic subspace, and $\xi$ a vector in $W$. If there is an integer $k$ such that

    $$
    T^{r-k}(\xi)=0
    $$

    then there is a vector $\eta$ in $W$ such that

    $$
    \xi=T^k(\eta)
    $$

3.  Let $T$ be a nilpotent operator on the $n$-dimensional space $V$, $x^r$ the minimal polynomial of $T$, and $W_1$ an $r$-dimensional $T$-cyclic subspace. Then there is a complement $W_2$ of $W_1$ such that:

    $$
    V=W_1\oplus W_2
    $$

    and $W_2$ is also invariant under $T$.

4.  Let $T$ be a nilpotent operator on the $n$-dimensional space $V$. Then $V$ can be decomposed into a direct sum of $T$-cyclic subspaces:

    $$
    V=W_1\oplus W_2\oplus\cdots\oplus W_S
    $$

5.  Every nilpotent matrix of order $n$ is similar to a matrix of the form:

    $$
    N=\begin{pmatrix}
    N_{r_1} &   &   & 0\\
      & N_{r_2} &   &  \\
      &   & \cdots &  \\
    0 &   &   & N_{r_S}\\
    \end{pmatrix}
    $$

    where each $N_{r_i}$ is a nilpotent Jordan block of order $r_i$.

6.  If we stipulate that the $T$-cyclic subspaces $W_i$ are arranged in decreasing order of their dimensions $r_i$, $r_1\geq\cdots\geq r_S$, then the decomposition of $V$ into $T$-cyclic subspaces is uniquely determined by $T$.
