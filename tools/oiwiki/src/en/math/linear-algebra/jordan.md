---
title: Jordan normal form
---

## Jordan decomposition

Let $T$ be a linear transformation on an $n$-dimensional space $V$. If the minimal polynomial of $T$ is

$$
m_A(\lambda)={(\lambda-\lambda_1)}^{r_1}{(\lambda-\lambda_2)}^{r_2}\cdots{(\lambda-\lambda_k)}^{r_k}
$$

then by the primary decomposition the space $V$ can be decomposed into a direct sum of subspaces:

$$
V=V_1\oplus V_2\oplus\cdots\oplus V_k
$$

where $V_i=N\left({(A-\lambda_i I)}^{r_i}\right)$, with $A$ the matrix corresponding to $T$; all these subspaces are invariant under $T$.

Let the transformation $T_i$ be the projection of $V$ onto the subspace $V_i$, i.e. construct polynomials $u_i(T)$ such that:

-   $$
    T_i=u_i(T)\frac{m_A(T)}{{(T-\lambda_i T_e)}^{r_i}}
    $$
-   $$
    T_1+T_2+\cdots+T_k=T_e
    $$

where $T_e$ denotes the identity transformation of the space $V$. Then we have the properties:

-   The restriction ${T_i|}_{V_i}$ of the transformation $T_i$ to the space $V_i$ is the identity transformation of $V_i$.
-   If $i$ and $j$ are different, the restriction ${T_i|}_{V_j}$ of the transformation $T_i$ to the space $V_j$ is the zero transformation of $V_j$.

Hence the transformation $T_i$ maps every vector $\xi$ of the space $V$ to its component $\xi_i$ in the space $V_i$.

Construct the transformation:

$$
T_D=\lambda_1 T_1+\lambda_2 T_2+\cdots+\lambda_k T_k
$$

Since every transformation $T_i$ is a polynomial in the transformation $T$, the transformation $T_D$ is also a polynomial in $T$, so every subspace $V_i$ is invariant under $T_D$.

From the equalities above, the restriction ${T_D|}_{V_i}$ of $T_D$ to the subspace $V_i$ is a homothety of $V_i$ with ratio $\lambda_i$. Therefore the transformation $T_D$ is diagonalizable.

Construct:

$$
T_N=T-T_D
$$

Then the transformation $T_N$ is also a polynomial in $T$, so every subspace $V_i$ is invariant under $T_N$. For any vector $\xi_i$ in the subspace $V_i$ we have:

$$
{T_N}^{r_i}(\xi_i)={T-T_D}^{r_i}(\xi_i)={T-\lambda_i T_i}^{r_i}(\xi_i)=0
$$

Let $r$ be the maximum of all $r_i$; then for any vector $\xi$ of the space $V$, the $r$-th power of the transformation $T_N$ maps $\xi$ to the zero vector. Therefore $T_N$ is a nilpotent transformation.

Thus every transformation $T$ of the space $V$ can be written as:

$$
T=T_D+T_N
$$

where $T_D$ is diagonalizable and $T_N$ is a nilpotent transformation. Since $T_D$ and $T_N$ are both polynomials in $T$, their product commutes:

$$
T_DT_N=T_NT_D
$$

Theorem: Let $T_1$ and $T_2$ be two diagonalizable transformations of the space $V$ with $T_1T_2=T_2T_1$. Then there exists a basis such that the matrices of $T_1$ and $T_2$ with respect to this same basis are both diagonal.

Theorem: Let $T$ be a linear transformation on an $n$-dimensional space $V$. Then there exist a diagonalizable transformation $T_D$ and a nilpotent transformation $T_N$ such that:

-   $$
    T=T_D+T_N
    $$
-   $$
    T_DT_N=T_NT_D
    $$

Both are polynomials in $T$, and they are uniquely determined by $T$.

This theorem gives a decomposition of the transformation $T$, called the Jordan decomposition of $T$; $T_D$ is called the diagonalizable part of $T$ and $T_N$ the nilpotent part of $T$.

Similarly, there is the Jordan decomposition of a matrix:

Theorem: Let $A$ be a matrix of order $n$. Then there exist a diagonalizable matrix $D$ and a nilpotent matrix $N$ such that:

-   $$
    A=D+N
    $$
-   $$
    DN=ND
    $$

Both are polynomials in the matrix $A$, and they are uniquely determined by $A$.

This theorem gives a decomposition of the matrix $A$, called the Jordan decomposition of $A$; $D$ is called the diagonalizable part of $A$ and $N$ the nilpotent part of $A$.

## Lambda matrices

The part introduced next concerns more general matrices containing a variable parameter $\lambda$, not just tables of numbers. This discussion is somewhat broader than that of matrices consisting purely of numbers.

For $\lambda$-matrices, the field corresponding to the underlying space becomes the field of rational functions in one variable $\lambda$.

A matrix whose entries are polynomials in $\lambda$ is called a $\lambda$-matrix and is denoted $A(\lambda)$.

Since the field of polynomials contains the number field, numerical matrices are special $\lambda$-matrices; the characteristic matrix $\lambda I-A$ of a numerical matrix $A$ is a kind of $\lambda$-matrix.

### Elementary operations on lambda matrices

For $\lambda$-matrices one can likewise define addition and subtraction, multiplication, elementary operations, and rank. For square $\lambda$-matrices one can likewise define the determinant, minors, and cofactors.

For $\lambda$-matrices the elementary operations are mostly the same as for numerical matrices; only the operation of adding a multiple is changed to (taking row operations as an example):

-   Multiply a row by a polynomial $\varphi(\lambda)$ in $\lambda$ and add it to another row.

Note that the scaling operation is not modified. This is because adding a multiple does not change the determinant, while scaling does. To preserve the properties of rank over the field of polynomials, the determinant may only be changed within the number field.

The corresponding elementary matrices are modified accordingly.

It is easy to see that the determinants of all three kinds of elementary matrices are nonzero constants, so they all have full rank. Hence multiplying by them on the left or on the right does not change the rank of a $\lambda$-matrix.

If $A(\lambda)$ can be transformed into $B(\lambda)$ by finitely many elementary operations, then $A(\lambda)$ and $B(\lambda)$ are called equivalent.

If $\lambda$-matrices are equivalent, they have the same rank. The converse does not hold, which is a difference from numerical matrices.

## Smith normal form

Theorem: Let the rank of a $\lambda$-matrix be $r$. Then $A(\lambda)$ is necessarily equivalent to:

$$
\begin{pmatrix}
D(\lambda) & 0\\
0 & 0\\
\end{pmatrix}
$$

where:

$$
D(\lambda)=\begin{pmatrix}
d_1(\lambda) &  & \\
 & \ddots & \\
 &  & d_r(\lambda)\\
\end{pmatrix}
$$

Every $d_i(\lambda)$ is a monic polynomial (leading coefficient $1$), and any two adjacent polynomials satisfy the divisibility relation $d_i(\lambda)|d_{i+1}(\lambda)$.

This normal form is called the Smith normal form, and the $d_i(\lambda)$ are called the invariant factors.

The concrete method for computing the Smith normal form is to eliminate from the upper left corner to the lower right corner: at each step the element in the upper left corner is the greatest common divisor of all the remaining polynomials to the lower right, and this upper-left element is used to eliminate the whole row and column to $0$.

Theorem: The condition that $A(\lambda)$ and $B(\lambda)$ are equivalent is equivalent to the condition that $A(\lambda)$ and $B(\lambda)$ have exactly the same invariant factors.

### Elementary divisors

By the fundamental theorem of algebra, let the factorization of the invariant factors $d_1(\lambda),d_2(\lambda),\cdots,d_m(\lambda)$ of $A(\lambda)$ be:

$$
d_i(\lambda)={(\lambda-\lambda_1)}^{e_{i1}}{(\lambda-\lambda_2)}^{e_{i2}}\cdots{(\lambda-\lambda_S)}^{e_{iS}}
$$

where $\lambda_1,\cdots,\lambda_S$ are pairwise distinct. Since:

$$
d_i(\lambda)|d_{i+1}(\lambda)
$$

the exponents $e_{1j},e_{2j},\cdots,e_{mj}$ are increasing, and all exponents of the last term $d_m(\lambda)$ are nonzero.

All factors in the expression above with exponent greater than zero are collectively called the elementary divisors of $A(\lambda)$.

Note that elementary divisors are counted with multiplicity. If for some $j$ the exponent $e_{ij}$ appears several times, then the corresponding elementary divisor ${(\lambda-\lambda_j)}^{e_{ij}}$ must also appear the corresponding number of times.

The previous theorem states that $A(\lambda)$ and $B(\lambda)$ are equivalent if and only if they have exactly the same invariant factors. If the invariant factors are exactly the same, the elementary divisors are of course exactly the same as well, but the converse does not hold. In fact we have the result:

Theorem: $A(\lambda)$ and $B(\lambda)$ have exactly the same invariant factors if and only if they have exactly the same elementary divisors and the same rank.

Hence "exactly the same elementary divisors and the same rank" also becomes a criterion for the equivalence of $\lambda$-matrices.

When performing elementary operations, one may also first transform $A(\lambda)$ into a diagonal matrix, then find the elementary divisors and the rank, and then find the invariant factors to obtain the normal form. We have the result:

Theorem: Let $A(\lambda)$ be equivalent to the diagonal matrix:

$$
\operatorname{diag}\{f_1(\lambda),f_2(\lambda),\cdots,f_r(\lambda),0,\cdots,0\}
$$

Then the powers ${(\lambda-\lambda_j)}^{e_{ij}}$ of all the linear factors of $f_1(\lambda),f_2(\lambda),\cdots,f_r(\lambda)$ constitute the elementary divisors of $A(\lambda)$.

The concrete method for constructing the invariant factors from the elementary divisors and the rank is as follows: first classify the elementary divisors by their factor and arrange them in a table; put the same kind of factor in the same row in order of decreasing powers, and put the highest powers of all kinds of factors in the same column; pad the number of columns with $1$ up to the rank $r$; then the product of each column constitutes one invariant factor.

### Application to characteristic matrices

If $A$ and $B$ are numerical matrices, their characteristic matrices are $\lambda$-matrices. We have the result:

Theorem: The condition that the numerical matrices $A$ and $B$ are similar is equivalent to the condition that the characteristic matrices $\lambda I-A$ and $\lambda I-B$ are equivalent.

Since the characteristic matrix $\lambda I-A$ contains $n$ copies of $\lambda$ only on the main diagonal, its rank is $n$. By the reasoning above, the ranks of the characteristic matrices of numerical matrices of the same size are always equal, so we have the equivalence:

The numerical matrices $A$ and $B$ are similar if and only if the characteristic matrices $\lambda I-A$ and $\lambda I-B$ have exactly the same elementary divisors.

For the characteristic matrix $\lambda I-A$, elementary operations preserve equivalence, so they do not change the rank.

Looking at the three kinds of elementary operations, since the only rewritten one, adding a multiple, does not change the determinant, in fact all three kinds of elementary operations only change the polynomial resulting from the determinant by a constant factor, so they do not change the factorization or the degree of the polynomial resulting from the determinant.

Therefore the determinant of the characteristic matrix $\lambda I-A$ is a polynomial of degree $n$; after elementary operations bring it to Smith normal form, since the rank is $n$, the determinant is exactly the product of all the invariant factors on the main diagonal, which also equals the product of all the elementary divisors. Hence the sum of the degrees of all elementary divisors of the characteristic matrix $\lambda I-A$ equals $n$.

## Jordan normal form

The matrix

$$
\begin{pmatrix}
\lambda & 1 & 0 & \cdots & 0 & 0\\
0 & \lambda & 1 & \cdots & 0 & 0\\
0 & 0 & \lambda & \cdots & 0 & 0\\
\vdots & \vdots & \vdots &  & \vdots & \vdots\\
0 & 0 & 0 & \cdots & \lambda & 1\\
0 & 0 & 0 & \cdots & 0 & \lambda\\
\end{pmatrix}
$$

whose entries on the main diagonal are all $\lambda$, whose entries immediately above the main diagonal are all $1$, and whose remaining entries are all $0$, is called a Jordan matrix belonging to $\lambda$, or a Jordan block.

Clearly, a nilpotent Jordan matrix is a special case of a Jordan matrix, namely the case where $\lambda$ is $0$.

Theorem: Let $T$ be a transformation of an $n$-dimensional space $V$, and let $\lambda_1,\cdots,\lambda_k$ be all the pairwise distinct eigenvalues of $T$. Then there exists a basis such that the matrix of $T$ with respect to this basis has the form:

$$
\begin{pmatrix}
B_1 &  &  & 0\\
 & B_2 &  & \\
 &  & \ddots & \\
0 &  &  & B_k\\
\end{pmatrix}
$$

where

$$
B_i=\begin{pmatrix}
J_{i1} &  &  & 0\\
 & J_{i2} &  & \\
 &  & \ddots & \\
0 &  &  & J_{is_i}\\
\end{pmatrix}
$$

and $J_{i1},\cdots,J_{is_i}$ are all Jordan blocks belonging to $\lambda_i$.

This is because, first, from the minimal polynomial:

$$
m_A(\lambda)={(\lambda-\lambda_1)}^{r_1}{(\lambda-\lambda_2)}^{r_2}\cdots{(\lambda-\lambda_k)}^{r_k}
$$

we have the primary decomposition:

$$
V=V_1\oplus V_2\oplus\cdots\oplus V_k
$$

where:

$$
V_i=N\left({(A-\lambda_i I)}^{r_i}\right)
$$

with $A$ the matrix corresponding to $T$.

Let the transformation $S_i$ be the restriction ${T|}_{V_i}$ of $T$ to $V_i$; next we try to carry out the Jordan decomposition of each $S_i$.

Denote by $T_e$ the identity transformation on $V$. Unlike the Jordan decomposition above, denote by $T_i$ the nilpotent part of the Jordan decomposition of $S_i$:

$$
S_i=\lambda_i T_e+T_i
$$

Then $T_i$ is a nilpotent transformation of the subspace $V_i$; in fact it is also the restriction ${(T-\lambda_i T_e)|}_{V_i}$ of $T-\lambda_i T_e$ to $V_i$.

The subspace $V_i$ can be decomposed into a direct sum of cyclic subspaces of the nilpotent transformation $T_i$:

$$
V_i=W_{i1}\oplus W_{i2}\oplus\cdots\oplus W_{is_i}
$$

In each cyclic subspace $W_{ij}$, take a cyclic basis and arrange it in reverse order; putting these together gives a basis of $V_i$, and the matrix of $T_i$ with respect to this basis has the form:

$$
N_i=\begin{pmatrix}
N_{i1} &  &  & 0\\
 & N_{i2} &  & \\
 &  & \ddots & \\
0 &  &  & N_{is_i}\\
\end{pmatrix}
$$

All $N_{ij}$ are nilpotent Jordan blocks. Then, for the basis of $V_i$ chosen above, the matrix corresponding to $S_i$ is:

$$
B_i=\begin{pmatrix}
\lambda_i &  &  & 0\\
 & \lambda_i &  & \\
 &  & \ddots & \\
0 &  &  & \lambda_i\\
\end{pmatrix}+\begin{pmatrix}
N_{i1} &  &  & 0\\
 & N_{i2} &  & \\
 &  & \ddots & \\
0 &  &  & N_{is_i}\\
\end{pmatrix}=\begin{pmatrix}
J_{i1} &  &  & 0\\
 & J_{i2} &  & \\
 &  & \ddots & \\
0 &  &  & J_{is_i}\\
\end{pmatrix}
$$

Here $J_{i1},J_{i2},\cdots,J_{is_i}$ are all Jordan blocks belonging to $\lambda_i$.

For every subspace $V_i$, choose a basis in the way described above and put them together into a basis of $V$; then the matrix of $T$ with respect to this basis has exactly the form prescribed by the theorem.

A matrix of order $n$ of the form:

$$
\begin{pmatrix}
J_1 &  &  & 0\\
 & J_2 &  & \\
 &  & \ddots & \\
0 &  &  & J_m\\
\end{pmatrix}
$$

in which every $J_i$ is a Jordan block, is called a Jordan normal form.

Theorem: Every matrix $A$ of order $n$ is similar to a Jordan normal form. Apart from the order in which the Jordan blocks are arranged, the Jordan normal form similar to $A$ is uniquely determined by $A$.

Note that in the matrix $B_i$ constructed above, the first term is a scalar multiple of the identity matrix, so it naturally commutes with the second term. Therefore the first term is exactly the diagonalizable part of the Jordan decomposition of $B_i$, and the second term is exactly the nilpotent part of the Jordan decomposition of $B_i$.

In the Jordan normal form corresponding to a matrix, the diagonal matrix formed by the entries on the main diagonal is the diagonalizable part of this Jordan normal form, and replacing the entries on the main diagonal by $0$ gives the nilpotent part of this Jordan normal form.

Theorem: In the Jordan normal form of a matrix $A$, every Jordan block:

$$
J_i=\begin{pmatrix}
\lambda_i & 1 &  &  & \\
 & \lambda_i & 1 &  & \\
 &  & \ddots & \ddots & \\
 &  &  & \ddots & 1\\
 &  &  &  & \lambda_i\\
\end{pmatrix}
$$

corresponds to one elementary divisor ${(\lambda-\lambda_i)}^{n_i}$ of the characteristic matrix $\lambda I-A$; all the elementary divisors of the characteristic matrix $\lambda I-A$ correspond to all the Jordan blocks in the Jordan normal form of $A$.

This is because the matrix $A$ is similar to its Jordan normal form, so their characteristic matrices are equivalent as well; this can be seen by bringing the characteristic matrix of the Jordan normal form to Smith normal form.

By this theorem, the Jordan normal form of a matrix $A$ can be written down using the elementary divisors of the characteristic matrix $\lambda I-A$.

One corollary is that the matrix $A$ is diagonalizable if and only if all the elementary divisors of the characteristic matrix $\lambda I-A$ are linear (of degree one).

## Frobenius' theorem

It was pointed out above that the rank of the Smith normal form of a characteristic matrix of order $n$ is $n$.

Theorem: Let the Smith normal form of the characteristic matrix $\lambda I-A$ of a matrix $A$ be:

$$
\operatorname{diag}\{d_1(\lambda),d_2(\lambda),\cdots,d_n(\lambda)\}
$$

Then the last invariant factor $d_n(\lambda)$ is exactly the minimal polynomial $m_A(\lambda)$ of the matrix $A$.

Corollary: The following conditions are each equivalent to the matrix $A$ being diagonalizable:

-   The minimal polynomial $m_A(\lambda)$ has no repeated roots.
-   The invariant factors of the characteristic matrix $\lambda I-A$ have no repeated roots.
-   All the elementary divisors of the characteristic matrix $\lambda I-A$ are linear (of degree one).
