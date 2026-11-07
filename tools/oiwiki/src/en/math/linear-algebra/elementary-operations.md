---
title: Elementary operations
---

## Elementary matrices

The following three kinds of square matrices are called elementary matrices.

### Multiplication matrix

A multiplication matrix (scaling matrix) is a special diagonal matrix.

$$
D_i(k)=\operatorname{diag}\{1,\cdots,1,k,1,\cdots,1\}
$$

It denotes a diagonal matrix whose $i$-th entry on the main diagonal is $k$, where $k$ is required not to be $0$, and all other entries are $1$.

In particular, when $k$ is $1$, $D_i(1)$ is just the identity matrix $I$.

### Switching matrix

A switching matrix (swap matrix) is a special symmetric matrix.

$$
P_{ij}=\begin{pmatrix}
I_{i-1} &  &  &  & \\
 & 0 &  & 1 & \\
 &  & I_{j-i-1} &  & \\
 & 1 &  & 0 & \\
 &  &  &  & I_{n-j}\\
\end{pmatrix}
$$

All entries of a switching matrix are $1$ or $0$; on the main diagonal all other entries are $1$, only the $i$-th and $j$-th entries are $0$, and the two entries in row $i$, column $j$ and in row $j$, column $i$ are $1$.

A switching matrix requires $i$ and $j$ to be different.

### Addition matrix

An addition matrix is obtained from the identity matrix $I$ by setting the entry in row $i$, column $j$ to $k$.

$$
T_{ij}(k)=\begin{pmatrix}
1 &  &  &  &  &  & \\
 & \ddots &  &  &  &  & \\
 &  & 1 & \cdots & k &  & \\
 &  &  & \ddots & \vdots &  & \\
 &  &  &  & 1 &  & \\
 &  &  &  &  & \ddots & \\
 &  &  &  &  &  & 1\\
\end{pmatrix}
$$

An addition matrix requires $i$ and $j$ to be different. If $k$ is $0$, then $T_{ij}(0)$ degenerates to the identity matrix $I$.

An addition matrix is an upper triangular or a lower triangular matrix.

### Determinants of elementary matrices

The three kinds of elementary matrices have the determinants:

$$
|D_i(k)|=k
$$

$$
|P_{ij}|=-1
$$

$$
|T_{ij}(k)|=1
$$

Since the determinant of a product of square matrices equals the product of the determinants, together with the equivalence of elementary operations and matrix multiplication described below, this property of elementary matrices can be used to compute determinants.

## Elementary operations

Not only on square matrices but on a general matrix $A$ one can perform elementary row operations and elementary column operations, collectively called elementary operations.

Elementary row operations, like elementary column operations, come in 3 kinds: multiplication (scaling), switching (swapping), and addition (adding a multiple). We first introduce the elementary row operations:

-   multiply row $i$ by a nonzero number $k$: $B\mapsto D_i(k)B$.
-   swap rows $i$ and $j$: $B\mapsto P_{ij}B$.
-   add $k$ times row $j$ to row $i$: $B\mapsto T_{ij}(k)B$.

Replacing rows by columns in the operations above gives the elementary column operations.

Among the elementary operations, switching can be realized by multiplication and addition. Obviously, addition cannot be realized by multiplication and switching. Using knowledge of determinants and the equivalence of elementary operations and matrix multiplication described below, one can also show that multiplication cannot be realized by addition and switching.

Therefore, compared with switching, multiplication and addition are the more essential operations. Switching is an auxiliary operation introduced in order to keep the elimination orderly in the elimination method.

## Elementary operations and matrix multiplication

One can observe that all three kinds of elementary matrices are obtained by performing one corresponding operation on the identity matrix $I$. In the later section on linear mappings it is pointed out that there is a correspondence between linear mappings and matrices, similar to the relationship here.

Regardless of whether the matrix $A$ is square, performing an elementary row operation on $A$ is equivalent to multiplying $A$ on the left by an elementary matrix. Performing an elementary column operation on $A$ is equivalent to multiplying $A$ on the right by an elementary matrix.

### Multiplication operation

Multiplying on the left by a multiplication matrix $D_i(k)$ is equivalent to multiplying row $i$ by $k$. Multiplying on the right by a multiplication matrix $D_i(k)$ is equivalent to multiplying column $i$ by $k$.

The product of diagonal matrices is again a diagonal matrix; to multiply diagonal matrices, multiply the corresponding entries on the main diagonal. Since the identity matrix is a special multiplication matrix, and a multiplication matrix requires $k$ not to be $0$, we see that a diagonal matrix can be decomposed into a product of multiplication matrices as long as none of its entries on the main diagonal is $0$.

For a general diagonal matrix, regardless of whether some entries are $0$, there is a corresponding conclusion. Multiplying on the left by a diagonal matrix is equivalent to multiplying the corresponding rows by some factors, the factors being exactly the corresponding entries on the main diagonal of the diagonal matrix. Multiplying on the right by a diagonal matrix performs the same operation on the corresponding columns.

Since the determinant of the multiplication matrix $D_i(k)$ is $k$, after a multiplication operation on a row or column of a square matrix, its determinant becomes $k$ times the original. The determinant of a diagonal matrix is the product of the entries on the main diagonal.

Multiplication of multiplication matrices is commutative, and multiplication of diagonal matrices is also commutative; when a product contains only diagonal matrices, the order can be arbitrary.

The multiplication operation corresponding to the identity matrix leaves the matrix $A$ unchanged; in practice such an operation is not performed.

### Switching operation

Multiplying on the left by a switching matrix $P_{ij}$ is equivalent to swapping rows $i$ and $j$. Multiplying on the right by a switching matrix $P_{ij}$ is equivalent to swapping columns $i$ and $j$.

Similar to the relationship between multiplication matrices and diagonal matrices, here we introduce the concept of a permutation matrix. A permutation matrix is a square matrix with exactly one $1$ in every row and every column and $0$ elsewhere. The identity matrix $I$ is also a special permutation matrix.

A permutation matrix corresponds to permuting the rows of the identity matrix $I$, and equally to permuting the columns of the identity matrix $I$. The identity matrix $I$ itself corresponds to the identity transformation.

Multiplying on the left by a permutation matrix is equivalent to permuting the rows of the original matrix, and multiplying on the right by a permutation matrix is equivalent to permuting the columns of the original matrix; the corresponding permutation is the same as the one applied to the rows or columns of the identity matrix $I$.

Permutation matrices correspond exactly to permutations; the multiplicative group of permutation matrices is isomorphic to the permutation group. By a well-known theorem, if the identity transformation is regarded as the product of zero transpositions, every permutation can be decomposed into a product of transpositions, and therefore every permutation matrix can be decomposed into a product of switching matrices.

Since the determinant of a switching matrix is $-1$, after a switching operation on the rows or columns of a square matrix, its determinant becomes $-1$ times the original.

Multiplication of switching matrices is not commutative, and multiplication of permutation matrices is not commutative either.

The determinant of a permutation matrix is ${(-1)}^p$, where $p$ is the inversion number of the permutation corresponding to the permutation matrix, that is, the number of transpositions in the decomposition of the permutation into a product of transpositions.

### Addition operation

Multiplying on the left by an addition matrix $T_{ij}(k)$ is equivalent to adding $k$ times row $j$ to row $i$. Multiplying on the right by an addition matrix $T_{ij}(k)$ is equivalent to adding $k$ times column $i$ to column $j$.

If this is hard to remember, one can look at which operation on the identity matrix $I$ produced the addition matrix $T_{ij}(k)$; the two correspond to each other: left multiplication is an operation on rows, right multiplication is an operation on columns, in accordance with the mnemonic "row on the left, column on the right".

Since the determinant of an addition matrix is $1$, after an addition operation on a square matrix, its determinant does not change.

Multiplication of addition matrices is not commutative.

The addition operation corresponding to the identity matrix leaves the matrix $A$ unchanged; in practice such an operation is not performed.

#### Upper triangular matrix

An addition matrix is an upper triangular or a lower triangular matrix. Since the two kinds of matrices are symmetric with respect to the main diagonal, we discuss upper triangular matrices here. In fact, in this example only elementary row operations are needed, and no column operations.

If all entries on the main diagonal of an upper triangular matrix are $1$, it can be decomposed into a product of a sequence of addition matrices. The order of the decomposition is as follows: first perform an addition operation on the first row of the identity matrix $I$, then perform an addition operation on the second row of the identity matrix $I$, and so on, until every row has been processed.

Since multiplication of addition matrices is not commutative, the order of the operations above cannot be changed.

If no entry on the main diagonal of an upper triangular matrix is $0$, it can be decomposed into a product of a sequence of addition matrices and multiplication matrices. When processing each row of the identity matrix $I$, one can first perform a multiplication operation on that row, so that the entry on the main diagonal becomes the specified nonzero value.

If there is a $0$ on the main diagonal of an upper triangular matrix, it cannot be decomposed into a product of a sequence of elementary matrices.

Regardless of whether there is a $0$ on the main diagonal of an upper triangular matrix, the determinant of an upper triangular matrix equals the product of the entries on the main diagonal, just as for diagonal matrices.

#### Transforming a square matrix into a diagonal matrix by addition operations

Using only addition operations, any square matrix can be transformed into a diagonal matrix; this example requires both elementary row operations and elementary column operations.

If there is a nonzero entry in the first row or the first column of the square matrix, we can make the upper left entry nonzero by means of addition operations, and then, using elementary row and column operations, make all entries of the first row and the first column except the upper left one equal to $0$.

If the first row and the first column of the square matrix are already all $0$, we simply look at the second row and the second column.

With this method, one can even require that all nonzero entries of the diagonal matrix be in the upper left corner.

If the first row and the first column of the square matrix are already all $0$, we check whether the remaining rows and columns contain a nonzero entry; as long as there is one, we can make some entry of the first row or the first column different from $0$ by an addition operation, thereby reducing to the initial situation in which the upper left entry is not $0$.

Only when the remaining rows and columns contain no nonzero entries either can the upper left entry not be made nonzero; in that case the remaining square matrix is already the zero matrix.

#### Normal form matrix

Using elementary operations, any matrix, regardless of shape, can be reduced to a normal form matrix.

A normal form matrix has an identity matrix $I$ as a submatrix in the upper left corner, and all other entries are $0$. The reduction method is similar to the operation of transforming a square matrix into a diagonal matrix, and additionally multiplication operations are used to turn the nonzero entries in the upper left corner into $1$.

After a matrix is reduced to a normal form matrix, the number of entries equal to $1$ is exactly the rank of the matrix.

## Invertible matrices

Let $A$ be a matrix of order $n$. If there exists a matrix $B$ of order $n$ such that $AB=BA=I$, then $A$ is called an invertible matrix or a nonsingular matrix, and $B$ is called the inverse matrix of $A$, denoted by $A^{-1}$.

If the matrix $A$ is invertible, then the inverse of $A$ is uniquely determined by $A$.

The inverse $A^{-1}$ of an invertible matrix $A$ is also invertible, and the inverse of $A^{-1}$ is $A$.

The product $AB$ of two invertible matrices $A$ and $B$ is also invertible, and its inverse is $B^{-1}A^{-1}$.

The transpose $A^T$ of an invertible matrix $A$ is also invertible, and the inverse of the transpose equals the transpose of the inverse.

### Inverses of elementary matrices

All elementary matrices are invertible, and the inverse is an elementary matrix of the same kind:

$$
{D_i(k)}^{-1}=D_i\left(\frac{1}{k}\right)
$$

$$
P_{ij}^{-1}=P_{ij}
$$

$$
T_{ij}(k)^{-1}=T_{ij}(-k)
$$

Obviously the identity matrix $I$ is invertible, and its inverse is again $I$.

Elementary operations preserve the invertibility of a matrix: the matrices before and after the operation are either both invertible or both non-invertible.

A matrix $A$ is invertible if and only if $A$ can be written as a product of elementary matrices, that is, if and only if it can be transformed into the identity matrix $I$ by elementary operations.

After determinants are introduced, we will know:

A matrix $A$ is invertible if and only if the rank of $A$ is $n$, if and only if the determinant of $A$ is not $0$.

A simple notation: let $E_{ij}$ denote the $n\times n$ matrix whose entry in row $i$, column $j$ is $1$ and all other entries are zero; then

-   $D_i(k)=I_n+(k-1)E_{ii}$
-   $P_{ij}=I_n-E_{ii}-E_{jj}+E_{ij}+E_{ji}$
-   $T_{ij}(k)=I_n+kE_{ij}$

This notation can also be applied to their inverse matrices.

## Applications

### Solving systems of linear equations

For a system of linear equations, the coefficients of the unknowns form the coefficient matrix; appending the constant terms of the system to the right of the coefficient matrix gives the augmented matrix.

Applying elementary row operations, the augmented matrix of a system of linear equations can first be transformed into row echelon form, then into reduced row echelon form, thereby solving the system. This method is called solving systems of linear equations by elimination, and the Gauss–Jordan elimination described later is an elimination algorithm performed in a specific order.

### Computing determinants

Since the determinant of a product of square matrices equals the product of their determinants, the determinants of elementary matrices are easy to compute, and elementary operations are equivalent to multiplication by elementary matrices, elementary operations are also used in computing determinants.

Since elementary operations performed in a specific order are easier to program, the Gauss–Jordan elimination algorithm described later can also be used to compute determinants.
