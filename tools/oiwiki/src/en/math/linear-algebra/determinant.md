---
title: Determinant
---

The determinant is an operation on square matrices. For a square matrix $A$, $\det A$ denotes the determinant of $A$.

This article introduces three definitions of the determinant. It can be proved that the definitions in this article are equivalent.

## Definition via permutations

Prerequisites: [permutations](../permutation.md), [inversion number](../permutation.md#inversion-number).

This method can be used to compute determinants of low order by hand; its time complexity is of factorial order.

We use the notation $\pi(j_1j_2\cdots j_n)$ for the inversion number of the permutation $j_1j_2\cdots j_n$, and $S_n$ for the set of all permutations of length $n$. The notation:

$$
\begin{aligned}
\det A &= \begin{vmatrix}
a_{11} & a_{12} & \cdots & a_{1n}\\
a_{21} & a_{22} & \cdots & a_{2n}\\
\vdots & \vdots &  & \vdots\\
a_{n1} & a_{n2} & \cdots & a_{nn}\\
\end{vmatrix} \\
&= \sum_{(j_1j_2\cdots j_n) \in S_n} (-1)^{\pi(j_1j_2\cdots j_n)} a_{1 j_1} a_{2 j_2}\dots a_{n j_n}
\end{aligned}
$$

denotes a determinant of order $n$, which is an algebraic sum of $n!$ terms; these terms are all possible products $a_{1j_1}a_{2j_2}\cdots a_{nj_n}$ of $n$ entries of the square matrix $A$ taken from different rows and different columns.

The sign in front of the term $a_{1j_1}a_{2j_2}\cdots a_{nj_n}$ is ${(-1)}^{\pi(j_1j_2\cdots j_n)}$; in other words, when $j_1j_2\cdots j_n$ is an even permutation the sign is positive, and when $j_1j_2\cdots j_n$ is an odd permutation the sign is negative.

The rule of diagonals for determinants of order two and three is in fact an application of the definition via permutations. For the same reason, the rule of diagonals no longer applies to determinants of order four and higher. In particular, a determinant of order one is the entry itself.

Theorem: from a determinant of order $n$, take the entries from rows $i_1,i_2,\cdots,i_n$ and columns $j_1,j_2,\cdots,j_n$ and form the product

$$
a_{i_1j_1}a_{i_2j_2}\cdots a_{i_nj_n}
$$

where $i_1,i_2,\cdots,i_n$ and $j_1,j_2,\cdots,j_n$ are both permutations of the $n$ numbers $1,2,\cdots,n$. Then the sign of this term in the determinant is ${(-1)}^{s+t}$, where

$$
s=\pi(i_1i_2\cdots i_n)
$$

$$
t=\pi(j_1j_2\cdots j_n)
$$

Theorem: a determinant equals the determinant of its transpose.

Theorem: suppose all entries of row $i$ of the determinant $\det A$ can be written as a sum of two terms:

$$
\begin{vmatrix}
a_{11} & a_{12} & \cdots & a_{1n}\\
\vdots & \vdots &  & \vdots\\
b_{i1}+c_{i1} & b_{i2}+c_{i2} & \cdots & b_{in}+c_{in}\\
\vdots & \vdots &  & \vdots\\
a_{n1} & a_{n2} & \cdots & a_{nn}\\
\end{vmatrix}
$$

Then this determinant equals the sum of the two determinants $\det A_1$ and $\det A_2$, where row $i$ of $A_1$ is $b_{i1},b_{i2},\cdots,b_{in}$, row $i$ of $A_2$ is $c_{i1},c_{i2},\cdots,c_{in}$, and all other rows of $A_1$ and $A_2$ are the same as in $A$. The same property also holds for columns.

## Inductive definition

This method only describes an algebraic property of the determinant; its time complexity is also of factorial order, and it is not suitable for computation.

### Cofactor

In a determinant $\det A$ of order $n$, choose any $k$ rows and $k$ columns of the matrix $A$. The matrix of order $k$ formed by the entries at the intersections of these rows and columns is called a submatrix of order $k$, and its determinant is called a minor of order $k$.

For a determinant $\det A$ of order $n$, the minor matrix $M_{ij}$ of an entry $a_{ij}$ is the submatrix of order $n-1$ that remains after deleting the row and column containing $a_{ij}$ from the original matrix $A$; its determinant $\det M_{ij}$ is called the minor.

For a determinant $\det A$ of order $n$, the minor $\det M_{ij}$ of the entry $a_{ij}$ multiplied by the sign ${(-1)}^{i+j}$ is called the cofactor of the entry $a_{ij}$ and is denoted by the symbol $A_{ij}$.

From the definition via permutations in the previous section one can derive the following conclusion:

Theorem: if in a determinant $\det A$ of order $n$ all entries of row $i$ or of column $j$ except $a_{ij}$ are $0$, then this determinant equals the product of $a_{ij}$ and its cofactor $A_{ij}$.

### Expansion of the determinant

Since the determinant is unchanged by transposing the square matrix, it suffices to introduce only one of the expansions along a row or along a column.

The determinant $\det A$ is defined as the sum of the products of all entries of any one of its rows (or columns) with their corresponding cofactors.

In other words, the determinant can be defined recursively by the expansion along a row (or a column):

$$
\begin{aligned}
\det A &= a_{i1}A_{i1}+a_{i2}A_{i2}+\cdots+a_{in}A_{in} \\
&= \sum_{j = 1}^{n} a_{ij}A_{ij} \\
&= \sum_{j = 1}^{n} (-1)^{i + j} a_{ij} \det M_{ij}
\end{aligned}
$$

$$
\begin{aligned}
\det A &= a_{1j}A_{1j}+a_{2j}A_{2j}+\cdots+a_{nj}A_{nj} \\
&= \sum_{i = 1}^{n} a_{ij}A_{ij} \\
&= \sum_{i = 1}^{n} (-1)^{i + j} a_{ij} \det M_{ij}
\end{aligned}
$$

The recursion ends at the determinant of a matrix of order one, which is the unique entry contained in that matrix.

Hence we have the conclusion:

Theorem: the sum of the products of the entries of some row (or column) of the determinant $\det A$ with the cofactors of the corresponding entries of another row (or another column) equals $0$.

In other words, when $i\neq j$:

$$
a_{i1}A_{j1}+a_{i2}A_{j2}+\cdots+a_{in}A_{jn}=0
$$

$$
a_{1i}A_{1j}+a_{2i}A_{2j}+\cdots+a_{ni}A_{nj}=0
$$

## Axiomatic definition

The axiomatic definition says that an operation satisfying certain properties can only be the determinant.

Prerequisites: [elementary operations](./elementary-operations.md).

Let $D_i(k)$ denote the [multiplication matrix](./elementary-operations.md#multiplication-matrix), $P_{ij}$ the [switching matrix](./elementary-operations.md#switching-matrix), and $T_{ij}(k)$ the [addition matrix](./elementary-operations.md#addition-matrix).

An operation $\det$ on a matrix $A$ of order $n$ is called a determinant if it satisfies the following four properties:

-   Multiplying all entries of some row or column of a determinant by the same number $k$ is the same as multiplying the determinant by $k$.

    $$
    \det(D_i(k)A) = \det(AD_i(k)) = k \det A
    $$

-   Swapping two rows or two columns of a determinant changes its sign.

    $$
    \det(P_{ij}A) = \det(AP_{ij}) = -\det A
    $$

-   Multiplying the entries of some row or column of a determinant by the same number and adding them to the corresponding entries of another row or column leaves the determinant unchanged.

    $$
    \det(T_{ij}(k)A) = \det(AT_{ij}(k))= \det A
    $$

-   The determinant of the identity matrix is $1$.

    $$
    \det I = 1
    $$

Using the properties of the determinant related to elementary operations, determinants of higher order can be conveniently computed by hand. [Computing determinants by Gaussian elimination](../numerical/gauss.md#行列式计算) also uses these properties, with time complexity $O(n^3)$.

The properties above also have several corollaries:

-   A common factor of some row or column of a determinant can be taken outside the determinant sign.
-   If all entries of some row or column of a determinant are $0$, then the determinant equals $0$.
-   If the corresponding entries of two rows or two columns of a determinant are proportional, then the determinant equals $0$.
-   If two rows or two columns of a determinant are completely identical, then the determinant equals $0$.

These corollaries are very commonly used when computing determinants by hand.
