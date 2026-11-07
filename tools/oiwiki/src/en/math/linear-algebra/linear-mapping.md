---
title: Linear mapping
---

Studying linear mappings means studying mappings between linear (vector) spaces.

A linear mapping can be represented in matrix form, so many concepts from matrix theory have a counterpart for linear mappings.

## Linear mappings and linear operators

Let $V$ and $W$ be two linear spaces over a field $F$, and let $T$ be a mapping from $V$ to $W$.

If for all vectors $x$ and $y$ in $W$ and all scalars $k$ and $l$ in the field $F$ we have:

$$
T(kx+ly)=kTx+lTy
$$

we say that $T$ is a linear mapping from $V$ to $W$. If $W=V$, we say that $T$ is a linear operator (linear transformation) on $V$.

For example, the identity $T_e$ leaves the space unchanged, and the zero operator $T_0$ maps the space to the zero space.

We denote by $L(V,W)$ the set of all linear mappings from $V$ to $W$. The set of all linear operators $L(V,V)$ is also written $L(V)$.

### Properties

-   A linear mapping maps the zero vector to the zero vector.
-   A linear mapping preserves the form of linear operations, i.e., the linear mapping of a linear combination equals the linear combination of the linear mappings.
-   A linear mapping preserves linear dependence, i.e., if vectors are linearly dependent before the mapping, they are linearly dependent after it as well.

A linear mapping does not, however, preserve linear independence: vectors that are linearly independent before the mapping need not be linearly independent after it.

## Matrix representation of a linear mapping

Let the dimension of $V$ be $n$, let $\alpha_1,\cdots,\alpha_n$ be a basis of $V$, let the dimension of $W$ be $m$, let $\beta_1,\cdots,\beta_m$ be a basis of $W$, and let $T$ be a linear mapping from $V$ to $W$.

Express the image of each $\alpha$ under $T$ in terms of the vectors $\beta$:

$$
T\alpha_j=a_{1j}\beta_1+\cdots+a_{mj}\beta_m
$$

In matrix notation:

$$
T(\alpha_1,\cdots,\alpha_n)=(T\alpha_1,\cdots,T\alpha_n)=(\beta_1,\cdots,\beta_m)A
$$

The matrix $A$ is called the matrix representation (matrix) of the linear mapping $T$ with respect to this pair of bases.

## Kernel and image of a linear mapping

The kernel and the image are described here from the viewpoint of the linear mapping. Using the matrix representation one sees that the kernel and image of a linear mapping coincide with the kernel and image of the matrix.

Let $T$ be a linear mapping from the space $V$ to the space $W$, and let:

$$
N(T)=\{x\in V|Tx=0\}
$$

$$
R(T)=Im(T)=\{y\in W|y=Tx,Vx\in V\}
$$

It is easy to verify that $N(T)$ is a subspace of $V$ and $R(T)$ is a subspace of $W$. We call $N(T)$ and $R(T)$ the kernel and the image of $V$; the dimension of $N(T)$ is called the **nullity** or **defect** of $T$, and the dimension of $R(T)$ the **rank** of $T$.

Theorem: Let $T$ be a linear mapping from the space $V$ to the space $W$, and let $V$ be finite-dimensional. Then $N(T)$ and $R(T)$ are both finite-dimensional, and:

$$
\operatorname{dim} N(T)+\operatorname{dim} R(T)=\operatorname{dim} V
$$

That is, the nullity plus the rank of $T$ equals the dimension of its domain $V$.

## Matrix representation of a linear operator

Let the dimension of $V$ be $n$, let $\alpha_1,\cdots,\alpha_n$ be a basis of $V$, and let $T$ be a linear operator on $V$. Then:

$$
T\alpha_j=a_{1j}\alpha_1+\cdots+a_{nj}\alpha_n
$$

In matrix notation:

$$
T(\alpha_1,\cdots,\alpha_n)=(T\alpha_1,\cdots,T\alpha_n)=(\alpha_1,\cdots,\alpha_n)A
$$

The matrix $A$ is called the matrix representation (matrix) of the linear operator $T$ with respect to this basis.

By the structure of the space and the linearity of $T$, the operator $T$ is completely determined by $T\alpha_1,\cdots,T\alpha_n$, so $T$ uniquely determines a matrix $A$.

Theorem: Let the dimension of $V$ be $n$ and let $\alpha_1,\cdots,\alpha_n$ be a basis of $V$. For an arbitrary square matrix $A$ of order $n$ there is one and only one linear operator $T$ from $V$ to $V$ such that the matrix of $T$ is exactly $A$.

Corollary: There is a one-to-one correspondence between $L(V,V)$ and the set of all square matrices of order $n$.

For example: the zero operator corresponds to the zero matrix, and the identity to the identity matrix.

## The space of linear operators

Theorem: $L(V)$ also forms a linear space. Introduce operations on $L(V)$: for all $T_1$ and $T_2$ in $L(V)$, every $x$ in $V$, and every $k$ in the field $F$, let:

$$
(T_1+T_2)x=T_1x+T_2x
$$

$$
(kT_1)x=k(T_1x)
$$

It is easy to verify that $L(V)$ is a linear space over $F$, the so-called space of linear operators.

For linear operators $T_1$ and $T_2$ in $L(V)$, define the product $T_1T_2$ of $T_1$ and $T_2$ as:

$$
(T_1T_2)x=T_2(T_1x)
$$

One can verify that $(T_1T_2)$ is also a linear operator in $L(V)$, and that the product of linear operators is associative but not commutative, similar to the product of matrices.

If for a linear operator $T_1$ in $L(V)$ there is a linear operator $T_2$ in $L(V)$ such that for every vector $x$ in $V$:

$$
(T_1T_2)x=T_1(T_2x)=x
$$

we say that $T_2$ is the inverse operator of $T_1$ and write:

$$
T_2=T_1^{-1}
$$

Moreover:

$$
T_1T_2=T_2T_1=T_e
$$

Theorem: Let the dimension of $V$ be $n$, let $\alpha_1,\cdots,\alpha_n$ be a basis of $V$, and in this basis let the linear operator $T_1$ have matrix $A$ and $T_2$ have matrix $B$. Then:

-   the linear operator $T_1+T_2$ has matrix $A+B$
-   the scalar multiple $kT_1$ of a linear operator has matrix $kA$
-   the product of linear operators $T_1T_2$ has matrix $AB$
-   the inverse operator of $T_1$, if it exists, has matrix $A^{-1}$

## Coordinates

Let $n$ vectors $x$ form a basis of the $n$-dimensional space $V$. For an arbitrary vector $y$ in $V$, write $y$ as:

$$
y=a_1x_1+a_2x_2+\cdots+a_nx_n=(x_1,x_2,\cdots,x_n)\begin{pmatrix}a_1\\a_2\\\vdots\\a_n\end{pmatrix}
$$

The column vector:

$$
\begin{pmatrix}a_1\\a_2\\\vdots\\a_n\end{pmatrix}
$$

is called the **coordinates** of the vector $y$ in the basis $x_1,x_2,\cdots,x_n$.

We see that coordinates are a column vector made of scalars from the field; they should be distinguished from the vectors in the abelian group.

## Change-of-coordinates formula

Let the dimension of $V$ be $n$, let $T$ be an operator in $L(V)$, and let $T$ have matrix $A$ in the basis $\alpha_1,\cdots,\alpha_n$. Let:

$$
\xi=(\alpha_1,\cdots,\alpha_n)\begin{pmatrix}x_1\\x_2\\\vdots\\x_n\end{pmatrix}
$$

and let:

$$
T\xi=T(\alpha_1,\cdots,\alpha_n)\begin{pmatrix}y_1\\y_2\\\vdots\\y_n\end{pmatrix}
$$

Then:

$$
T\xi=T(\alpha_1,\cdots,\alpha_n)\begin{pmatrix}y_1\\y_2\\\vdots\\y_n\end{pmatrix}=(\alpha_1,\cdots,\alpha_n)A\begin{pmatrix}x_1\\x_2\\\vdots\\x_n\end{pmatrix}
$$

Points (column vectors) of the space $V$ are essentially always of the form "basis times coordinates". A point $x$ of the space $V$, given as a column vector, itself uses the identity matrix $I$ as its basis, i.e., $x=Ix$.

Only when there is a single, fixed basis does a pure linear operator $T$ reduce to multiplying the coordinates by an ordinary matrix on the left.

Think of the linear operator $T$ as a "filter" through which we observe the space $V$. The linear operator $T$ acts on the space $V$ and distorts the space $V$. After the filter is applied, the position of the point itself does not change.

This theorem also shows that a linear operator $T$ on a basis of column vectors is equivalent to multiplying the basis on the right by a transition matrix.

Hence, between different bases, the relation between coordinates is multiplication on the left by the inverse of the transition matrix.

## Transition matrix

Let $n$ vectors $x$ and $n$ vectors $y$ be two bases of the space $V$. For $1\leq i\leq n$, let the coordinates of each vector $y_i$ in the basis $x_1,x_2,\cdots,x_n$ be:

$$
y_i=(x_1,x_2,\cdots,x_n)\begin{pmatrix}a_{1i}\\a_{2i}\\\vdots\\a_{ni}\end{pmatrix}
$$

Then the $n$ vectors $y$ are arranged into the matrix on the left-hand side of the equation, and the $n$ coordinate columns into the matrix $A$ on the right-hand side:

$$
(y_1,y_2,\cdots,y_n)=(x_1,x_2,\cdots,x_n)A
$$

The matrix $A$ is called the **transition matrix** from the basis $x_1,x_2\cdots,x_n$ to the basis $y_1,y_2\cdots,y_n$, also known as the change-of-basis matrix.

Clearly the transition matrix is invertible. By the equation above, the transition matrix from the basis $y_1,y_2\cdots,y_n$ to the basis $x_1,x_2\cdots,x_n$ is $A^{-1}$.

We see that the transition matrix is a matrix made of scalars from the field, not a matrix made of vectors from the abelian group; the two should be distinguished.

Let $n$ vectors $x$ and $n$ vectors $y$ be two bases of the space $V$. For the same vector $z$ of the space $V$ we have:

$$
z=(x_1,x_2,\cdots,x_n)\begin{pmatrix}\xi_1\\\xi_2\\\vdots\\\xi_n\end{pmatrix}=(y_1,y_2\cdots,y_n)\begin{pmatrix}\eta_1\\\eta_2\\\vdots\\\eta_n\end{pmatrix}
$$

Substituting the equation from above

$$
(y_1,y_2\cdots,y_n)=(x_1,x_2\cdots,x_n)A
$$

by uniqueness we obtain:

$$
\begin{pmatrix}\xi_1\\\xi_2\\\vdots\\\xi_n\end{pmatrix}=A\begin{pmatrix}\eta_1\\\eta_2\\\vdots\\\eta_n\end{pmatrix}
$$

or

$$
\begin{pmatrix}\eta_1\\\eta_2\\\vdots\\\eta_n\end{pmatrix}=A^{-1}\begin{pmatrix}\xi_1\\\xi_2\\\vdots\\\xi_n\end{pmatrix}
$$

This is a transformation purely between coordinates; the change-of-coordinates formulas live entirely in the field of scalars. Because of the distinction made above, the vectors of the linear space and of the abelian group are "abstract vectors", while the coordinates and the entries of the transition matrix lie in the field of scalars and are regarded as "concrete vectors"; the two kinds of vectors should be regarded as "different things".

A matrix can transform the whole space, i.e., all coordinates; the column vectors $x$, as coordinates, fill the whole space.

The identity matrix $I$ consists of the unit vectors. The matrix $A$ transforms the identity matrix $I$ into the columns of the matrix $A$, i.e., it transforms the unit vectors into the columns of the matrix $A$. Therefore, multiplying by the matrix $A$ on the left can also be regarded as transforming the space in this way.

Multiplying a vector by a matrix on the left can also be regarded as multiplying coordinates by a set of vectors on the left. From the coordinate point of view this is:

$$
Iy=Xa
$$

The same column vector $y$ has coordinates $y$ in the "ordinary" space, the space represented by the identity matrix $I$, and in the new, transformed space its coordinates will be denoted $a$. In this way, the matrix $X$ is not only a basis in the ordinary space but also the transition matrix from the set of vectors $I$ to the set of vectors $X$.

A linear operator $T$ maps one basis to another basis, so the coordinates are mapped to other coordinates as well.

If the transition matrix of the linear operator $T$ that maps the basis $\alpha$ to $\beta$ is $A$, then for the corresponding basis matrices we have $\beta=\alpha A$.

Hence the relation between the coordinates is exactly reversed. Suppose the coordinates after applying the linear operator $T$ are $b$, i.e., through the filter we observe the coordinates $b$; then the representation of the point in $V$ is $\beta b$. To recover it, we use the transition matrix and write the representation of the point in $V$ as $\alpha Ab$. Now the viewpoint that a change of coordinates is multiplication on the left by the inverse of the transition matrix becomes clear.

## Linear operators and matrix similarity

The relation of a linear operator $T$ on the space $V$ to a basis $\alpha$ of the space $V$:

The linear operator $T$ acts on the basis $\alpha$ and maps the basis $\alpha$ to $T(\alpha)$, which amounts to multiplying the basis $\alpha$ on the right by $A$, i.e., $T(\alpha)=\alpha A$.

Matrix similarity deals with the following question: the same linear operator $T$ is described by the matrix $B$ in the space $V$ with basis $\beta$, and by the matrix $A$ in the space $V$ with basis $\alpha$.

If the transition matrix is $C$, i.e., $\beta=\alpha C$, what is the relation between the two descriptions $B$ and $A$?

Since it is the same operator $T$, we observe the fact that the transition-matrix relation holds both before and after applying the operator, i.e.:

$$
T(\beta)=T(\alpha)C=\alpha AC
$$

From the viewpoint of the basis $\beta$, the linear operator $T$ is still a multiplication on the right; the basis $\beta$ is converted to the basis $\alpha$ and then multiplied on the right by $C$, and the transition-matrix relation $C$ is preserved before and after applying the operator:

$$
T(\beta)=\beta B=\alpha CB
$$

Thus the problem is solved:

$$
B=C^{-1}AC
$$

Theorem: Let $T$ be an operator in $L(V)$. Then the matrices of $T$ in different bases are **similar**.

For square matrices $A$ and $B$, if there is an invertible matrix $C$ such that $B=C^{-1}AC$, then $A$ and $B$ are similar.

Matrix similarity preserves rank, so matrix similarity implies matrix equivalence. However, two equivalent matrices need not be similar.

Since matrix similarity is closely tied to the shape of the matrices, matrix similarity has nothing to do with the equivalence of sets of vectors or with systems of equations having the same solutions.

Looking back, the explanation of matrix similarity comes down to 4 equations: $\beta=\alpha C$, $T(\alpha)=\alpha A$, $T(\beta)=\beta B$, $T(\beta)=T(\alpha)C$.

## References

-   [【官方双语/合集】线性代数的本质 - 系列合集 P13 09 - 基变换](https://www.bilibili.com/video/BV1Ls411b7r2) (Essence of Linear Algebra, official bilingual collection, part 13: "Change of basis")
