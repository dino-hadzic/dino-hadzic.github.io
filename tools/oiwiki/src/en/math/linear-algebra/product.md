---
title: Dot product and cross product
---

This article introduces simple operations between vectors.

Before the main text, a special note on translation. For historical reasons, mathematics and physics have all sorts of Chinese translations for the two terms "inner product" and "outer product".

In physics they are usually translated as "标积" and "矢积" ("scalar product" and "vector product"), expressing that the result of the operation is a scalar or a vector, respectively. The terms "数量积" and "向量积" ("quantity product" and "vector product") in high-school mathematics textbooks also follow this way of translating by meaning.

In mathematics they can also usually be translated as "内积" and "外积" ("inner product" and "outer product"), which is a literal translation of the two terms. "点乘" and "叉乘" ("dot multiplication" and "cross multiplication") are colloquial names derived from the operation symbols, and these colloquial names are also very common.

In the "dot multiplication" operation the dot symbol is often omitted, and in linear algebra it is even regarded directly as matrix multiplication, without writing the dot.

## Dot product

The concept of the dot product **applies to vectors of any dimension**.

### Definition

The dot product has several different but equivalent definitions; some of them are introduced below.

#### Geometric definition

In the $n$-dimensional Euclidean space $\mathbf{R}^n$, given two vectors $\boldsymbol{a}, \boldsymbol{b}$ with angle $\theta$ between them,

$$
\boldsymbol{a} \cdot \boldsymbol{b} = |\boldsymbol{a}| |\boldsymbol{b}| \cos \theta
$$

is the **inner product** of these two vectors, also called the **dot product** or **scalar product**. Here $|\boldsymbol{b}|\cos \theta$ is called the projection of $\boldsymbol{b}$ onto the direction of $\boldsymbol{a}$. The geometric meaning of the dot product is: the dot product $\boldsymbol{a} \cdot \boldsymbol{b}$ equals the product of the magnitude of $\boldsymbol{a}$ and the projection of $\boldsymbol{b}$ onto the direction of $\boldsymbol{a}$.

#### Algebraic definition

In the $n$-dimensional Euclidean space $\mathbf{R}^n$, given two vectors $\boldsymbol{a} = (a_1, a_2, \dots, a_n), \boldsymbol{b} = (b_1, b_2, \dots, b_n)$,

$$
\boldsymbol{a} \cdot \boldsymbol{b} = \sum_{i = 1}^{n} a_i b_i
$$

is the **inner product** of these two vectors, also called the **dot product** or **scalar product**. The geometric and algebraic definitions of the dot product are equivalent in Euclidean space, and the latter is more convenient to use.

When no confusion can arise, the dot of the dot product may be omitted. A superscript $2$ on a vector is shorthand for the dot product of the vector with itself, i.e. **the square of the magnitude of the vector**, with the magnitude bars omitted. This superscript $2$ must not be understood as the square of a vector, because the result of a dot product of vectors is a scalar, so there is no dot product of any number of vectors other than $2$. Likewise, the square of the squared magnitude of a vector cannot be abbreviated as a superscript $4$; instead, the result with superscript $2$ must be treated as a whole, and so on.

### Properties

Note that the result of the dot product is a scalar; what is special about it is that it is a bilinear operation, linear in each of the two vectors separately. Specifically, the dot product satisfies:

$$
\begin{aligned}
(\boldsymbol{a} + \boldsymbol{b}) \cdot \boldsymbol{c} &= \boldsymbol{a} \cdot \boldsymbol{c} + \boldsymbol{b} \cdot \boldsymbol{c} \\
\boldsymbol{a} \cdot (\boldsymbol{b} + \boldsymbol{c}) &= \boldsymbol{a} \cdot \boldsymbol{b} + \boldsymbol{a} \cdot \boldsymbol{c} \\
(\lambda \boldsymbol{a}) \cdot \boldsymbol{b} &= \lambda (\boldsymbol{a} \cdot \boldsymbol{b}) \\
\boldsymbol{a} \cdot (\lambda \boldsymbol{b}) &= \lambda (\boldsymbol{a} \cdot \boldsymbol{b})
\end{aligned}
$$

The dot product is also commutative, i.e.:

$$
\boldsymbol{a} \cdot \boldsymbol{b} = \boldsymbol{b} \cdot \boldsymbol{a}
$$

### Applications

Some common applications of the dot product are introduced below.

1.  Testing whether two vectors are perpendicular:

    $$
    \boldsymbol{a} \perp \boldsymbol{b} \iff \boldsymbol{a} \cdot \boldsymbol{b} = 0
    $$

    That is, the dot product of two mutually perpendicular vectors is $0$; the dot product of a vector and the zero vector is $0$. If a zero dot product is used as the definition of perpendicularity, it follows that the zero vector is perpendicular to every vector.

2.  Testing whether two vectors are collinear:

    $$
    \exists\lambda \in \mathbf{R} (\boldsymbol{a} = \lambda \boldsymbol{b}) \iff |\boldsymbol{a} \cdot \boldsymbol{b}| = |\boldsymbol{a}| |\boldsymbol{b}|
    $$

3.  Computing the magnitude of a vector:

    $$
    |\boldsymbol a| = \sqrt{\boldsymbol{a} \cdot \boldsymbol{a}}
    $$

4.  Computing the angle between two vectors:

    $$
    \theta = \arccos \frac{\boldsymbol{a} \cdot \boldsymbol{b}}{|\boldsymbol a| |\boldsymbol b|}
    $$

## Determinants of order 2 and 3

Determinants of order 2 and 3 can be defined specially as simpler special cases of the determinant. In the last part of calculus, field theory, Green's theorem uses a determinant of order 2, Gauss's theorem (the divergence theorem) uses the dot product, and Stokes' theorem uses a determinant of order 3.

A determinant of order 2 can be regarded as a function of four variables, defined as:

$$
\begin{vmatrix}
    a & b \\
    c & d
\end{vmatrix}=ad-bc
$$

A determinant of order 3 can be regarded as a function of nine variables, defined as:

$$
\begin{vmatrix}
    a & b & c \\
    d & e & f \\
    g & h & i
\end{vmatrix}=aei+dhc+gbf-ahf-dbi-gec
$$

A special mnemonic is the "rule of diagonals" (rule of Sarrus); the rule of diagonals applies only to determinants of order 2 and 3.

Special note: the expansion of a determinant of order 4 has 24 terms in total, and the term on the anti-diagonal has a positive sign. If the "rule of diagonals" for determinants of order 3 is forcibly applied, not only are there too few terms, but the sign of the anti-diagonal term is also wrong; therefore the "rule of diagonals" for determinants of order 3 does not apply to determinants of higher order, and determinants of higher order are also not suitable for computation by direct expansion.

## Cross product

The cross product is an operation **specific to three-dimensional vectors**.

In physics, three-dimensional vectors are by default vectors related to spatial position and are always written in bold. However, the four-dimensional vectors related to relativity in physics are not written in bold, but use special notation and indices.

In linear algebra, all vectors are written in bold, and since this is tedious, and since most operations in linear algebra are between vectors and matrices, so that ambiguity is unlikely, the vector notation may be omitted when writing by hand.

### Definition

The cross product has several different but equivalent definitions; some of them are introduced below.

#### Geometric definition

In the three-dimensional Euclidean space $\mathbf{R}^3$, the cross product of vectors $\boldsymbol{a}, \boldsymbol{b}$ is defined as a vector, denoted by $\boldsymbol{a} \times \boldsymbol{b}$, whose magnitude and direction are defined as follows:

1.  $|\boldsymbol{a} \times \boldsymbol{b}| = |\boldsymbol{a}| |\boldsymbol{b}| \sin \langle \boldsymbol{a}, \boldsymbol{b} \rangle$;
2.  $\boldsymbol{a} \times \boldsymbol{b}$ is perpendicular to both $\boldsymbol{a}, \boldsymbol{b}$, and the directions of $\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{a} \times \boldsymbol{b}$ obey the right-hand rule.

Looking at the magnitude of the cross product and recalling the formula for the area of a triangle $S=\frac{1}{2}ab\sin C$, we see that the geometric meaning of the cross product is: **$|\boldsymbol{a} \times \boldsymbol{b}|$ is the area of the parallelogram with $\boldsymbol{a}, \boldsymbol{b}$ as adjacent sides**.

#### Algebraic definition

In the three-dimensional Euclidean space $\mathbf{R}^3$, the cross product of vectors $\boldsymbol{a} = (x_1, y_1, z_1), \boldsymbol{b} = (x_2, y_2, z_2)$ is defined as a vector $\boldsymbol{c}$, denoted by $\boldsymbol{c} = \boldsymbol{a} \times \boldsymbol{b}$, and the result can be expressed by a determinant of order 3:

$$
\begin{vmatrix}
    \boldsymbol{i} & \boldsymbol{j} & \boldsymbol{k} \\
    x_1 & y_1 & z_1  \\
    x_2 & y_2 & z_2
\end{vmatrix}
$$

where $\boldsymbol{i}, \boldsymbol{j}, \boldsymbol{k}$ denote the unit vectors pointing along the coordinate axes $x, y, z$ and are written in the places of the corresponding coordinates. Expanding gives

$$
\begin{aligned}
\boldsymbol{c} &= \boldsymbol{a} \times \boldsymbol{b} \\
&= (y_1z_2 - y_2z_1)\boldsymbol{i} + (z_1x_2 - z_2x_1)\boldsymbol{j} + (x_1y_2 - x_2y_1)\boldsymbol{k} \\
&= (y_1z_2 - y_2z_1, z_1x_2 - z_2x_1, x_1y_2 - x_2y_1)
\end{aligned}
$$

### Properties

1.  The cross product is a bilinear operation, linear in each of the two vectors separately. Specifically, the cross product satisfies:

    $$
    \begin{aligned}
    (\boldsymbol{a} + \boldsymbol{b}) \times \boldsymbol{c} &= \boldsymbol{a} \times \boldsymbol{c} + \boldsymbol{b} \times \boldsymbol{c} \\
    \boldsymbol{a} \times (\boldsymbol{b} + \boldsymbol{c}) &= \boldsymbol{a} \times \boldsymbol{b} + \boldsymbol{a} \times \boldsymbol{c} \\
    (\lambda \boldsymbol{a}) \times \boldsymbol{b} &= \lambda (\boldsymbol{a} \times \boldsymbol{b}) \\
    \boldsymbol{a} \times (\lambda \boldsymbol{b}) &= \lambda (\boldsymbol{a} \times \boldsymbol{b})
    \end{aligned}
    $$

    The first two properties may also be called distributivity, i.e. the cross product is distributive over vector addition.

2.  The cross product is anticommutative, i.e.:

    $$
    \boldsymbol a \times \boldsymbol b=-\boldsymbol b \times \boldsymbol a
    $$

3.  By the geometric definitions of the dot product and the cross product above:

    $$
    \begin{aligned}
    |\boldsymbol a \times \boldsymbol b| &= |\boldsymbol a| |\boldsymbol b| \sin \langle \boldsymbol a, \boldsymbol b \rangle \\
    \boldsymbol a \cdot \boldsymbol b &= |\boldsymbol a| |\boldsymbol b| \cos \theta \\
    &= |\boldsymbol a| |\boldsymbol b| \cos \langle \boldsymbol a, \boldsymbol b\rangle
    \end{aligned}
    $$

    we can write the identity:

    $$
    (\boldsymbol a\times \boldsymbol b) \cdot (\boldsymbol a\times \boldsymbol b) = |\boldsymbol a|^2 |\boldsymbol b|^2-{(\boldsymbol a \cdot \boldsymbol b)}^2
    $$

4.  The cross product satisfies the Jacobi identity:

    $$
    \boldsymbol a \times (\boldsymbol b \times \boldsymbol c) + \boldsymbol b \times (\boldsymbol c \times \boldsymbol a) + \boldsymbol c \times (\boldsymbol a \times \boldsymbol b) = \boldsymbol 0
    $$

### Applications

Some common applications of the cross product are introduced below.

1.  Testing whether two vectors are collinear:

    $$
    \exists\lambda \in \mathbf{R} (\boldsymbol{a} = \lambda \boldsymbol{b}) \iff \boldsymbol{a} \times \boldsymbol{b} = \boldsymbol{0}
    $$

    That is, the cross product of two collinear three-dimensional vectors is $\boldsymbol 0$; the cross product of a three-dimensional vector with itself is $\boldsymbol 0$; the cross product of a three-dimensional vector and the zero vector is $\boldsymbol 0$. If a zero cross product is used as the definition of collinearity of two vectors, it follows that the zero vector is collinear with every vector.

2.  Computing the area of the parallelogram spanned by two vectors:

    $$
    S \langle \boldsymbol a, \boldsymbol b \rangle = |\boldsymbol a \times \boldsymbol b|
    $$

#### The case of two-dimensional vectors

For two-dimensional vectors the cross product cannot be computed, but the area of the parallelogram spanned by two vectors can still be computed:

Let $\boldsymbol{a} = (m, n), \boldsymbol{b} = (p, q)$, and extend the rectangular coordinate system in the plane to a rectangular coordinate system in space, with the original plane lying in the $xOy$ plane of the new coordinate system; the original coordinates $(m, n)$ and $(p, q)$ become $(m, n, 0)$ and $(p, q, 0)$.

Then the cross product of the two vectors is $(0, 0, mq - np)$, so the area of the parallelogram is $|mq - np|$, which can be regarded as the absolute value of a determinant of order 2.

Here, by the right-hand rule and the sign of the $z$ coordinate, one can infer the direction of $\boldsymbol b$ relative to $\boldsymbol a$: if it is in the counterclockwise direction the $z$ coordinate is positive, otherwise it is negative; in short, **clockwise negative, counterclockwise positive**.

## Scalar triple product

Like the cross product, the scalar triple product of vectors is an operation **specific to three-dimensional vectors**.

### Definition

Let $\boldsymbol a, \boldsymbol b, \boldsymbol c$ be three vectors in three-dimensional space. Then $(\boldsymbol a \times \boldsymbol b) \cdot \boldsymbol c$ is called the scalar triple product of the three vectors $\boldsymbol a, \boldsymbol b, \boldsymbol c$, denoted by $[\boldsymbol a \boldsymbol b \boldsymbol c]$ or $(\boldsymbol a, \boldsymbol b, \boldsymbol c)$ or $(\boldsymbol a \boldsymbol b \boldsymbol c)$ or $\det(\boldsymbol a, \boldsymbol b, \boldsymbol c)$. The geometric meaning of the absolute value of the scalar triple product, $|(\boldsymbol a \times \boldsymbol b) \cdot \boldsymbol c|$, is the volume of the parallelepiped with edges $\boldsymbol a, \boldsymbol b, \boldsymbol c$.

The scalar triple product of vectors can be expressed by a determinant of order 3:

$$
\begin{aligned}
(\boldsymbol a \times \boldsymbol b) \cdot \boldsymbol c &= \det(\boldsymbol a, \boldsymbol b, \boldsymbol c) \\
&= \begin{vmatrix}
    a_x & b_x & c_x \\
    a_y & b_y & c_y \\
    a_z & b_z & c_z
\end{vmatrix} \\
&= a_x b_y c_z + a_y b_z c_x + a_z b_x c_y - a_z b_y c_x -a _y b_x c_z - a_x b_z c_y
\end{aligned}
$$

### Properties

1.  The scalar triple product is linear in each of the three vectors separately; specifically:

    $$
    \begin{aligned}
    \det(\lambda\boldsymbol{u} + \mu\boldsymbol{v}, \boldsymbol{b}, \boldsymbol{c}) &= \lambda\det(\boldsymbol{u}, \boldsymbol{b}, \boldsymbol{c}) + \mu\det(\boldsymbol{v}, \boldsymbol{b}, \boldsymbol{c}) \\
    \det(\boldsymbol{a}, \lambda\boldsymbol{u} + \mu\boldsymbol{v}, \boldsymbol{c}) &= \lambda\det(\boldsymbol{a}, \boldsymbol{u}, \boldsymbol{c}) + \mu\det(\boldsymbol{a}, \boldsymbol{v}, \boldsymbol{c}) \\
    \det(\boldsymbol{a}, \boldsymbol{b}, \lambda\boldsymbol{u} + \mu\boldsymbol{v}) &= \lambda\det(\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{u}) + \mu\det(\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{v})
    \end{aligned}
    $$

2.  The scalar triple product is antisymmetric: swapping the positions of two vectors turns the scalar triple product into its negative, hence:

    $$
    \det(\boldsymbol a, \boldsymbol b, \boldsymbol c) = \det(\boldsymbol b, \boldsymbol c, \boldsymbol a) = \det(\boldsymbol c, \boldsymbol a, \boldsymbol b) = -\det(\boldsymbol b, \boldsymbol a, \boldsymbol c) = -\det(\boldsymbol a, \boldsymbol c, \boldsymbol b)= -\det(\boldsymbol c, \boldsymbol b, \boldsymbol a)
    $$

    From this we also obtain the following relation between the dot product and the cross product:

    $$
    (\boldsymbol a \times \boldsymbol b) \cdot \boldsymbol c = \boldsymbol a \cdot (\boldsymbol b \times \boldsymbol c)
    $$

### Applications

The scalar triple product of vectors has the following common applications.

1.  Computing the volume of the tetrahedron $ABCD$:

    $$
    V=\frac{1}{6}\left|\det(\overrightarrow{AB}, \overrightarrow{AC}, \overrightarrow{AD})\right|
    $$

2.  Testing whether $\boldsymbol a, \boldsymbol b, \boldsymbol c$ are coplanar;

    Three three-dimensional vectors $\boldsymbol a, \boldsymbol b, \boldsymbol c$ are coplanar if and only if $\det(\boldsymbol a, \boldsymbol b, \boldsymbol c)=0$.

3.  Determining the handedness of the coordinate system formed by $\boldsymbol a, \boldsymbol b, \boldsymbol c$;

    Whether the sign of the scalar triple product $\det(\boldsymbol a, \boldsymbol b, \boldsymbol c)$ is positive or negative depends on whether the angle between $\boldsymbol a \times \boldsymbol b$ and $\boldsymbol c$ is acute or obtuse, i.e. whether they point to the same side or to opposite sides of the plane spanned by $\boldsymbol a$ and $\boldsymbol b$, which is equivalent to whether the three vectors $\boldsymbol a, \boldsymbol b, \boldsymbol c$, in this order, form a right-handed or a left-handed system. Specifically:

    -   $\det(\boldsymbol a, \boldsymbol b, \boldsymbol c) < 0$ is equivalent to $\boldsymbol a, \boldsymbol b, \boldsymbol c$, in this order, forming a left-handed system;
    -   $\det(\boldsymbol a, \boldsymbol b, \boldsymbol c) > 0$ is equivalent to $\boldsymbol a, \boldsymbol b, \boldsymbol c$, in this order, forming a right-handed system.

## Vector triple product

The scalar triple product of three-dimensional vectors is a mix of the dot product and the cross product and has cyclic symmetry. The cross product of two three-dimensional vectors is again a three-dimensional vector; so are there related results for the cross product of a cross product?

First we prove a lemma.

$$
(\boldsymbol a \times \boldsymbol b)\times \boldsymbol a = (\boldsymbol a \cdot \boldsymbol a) \boldsymbol b - (\boldsymbol a \cdot \boldsymbol b) \boldsymbol a
$$

Proof: by the right-hand rule, $\boldsymbol a \times \boldsymbol b$ is perpendicular to both $\boldsymbol a$ and $\boldsymbol b$, and the left-hand side of the identity to be proved is perpendicular to $\boldsymbol a \times \boldsymbol b$, so the left-hand side is coplanar with $\boldsymbol a$ and $\boldsymbol b$.

Therefore we may assume:

$$
(\boldsymbol a \times \boldsymbol b)\times \boldsymbol a = \lambda \boldsymbol a + \mu \boldsymbol b
$$

By the results on the scalar triple product, taking the dot product of both sides of the above equation with $\boldsymbol a$ and with $\boldsymbol b$ respectively gives:

$$
\begin{aligned}
\lambda (\boldsymbol a \cdot \boldsymbol a)+\mu (\boldsymbol a \cdot \boldsymbol b) &= 0 \\
\lambda (\boldsymbol a \cdot \boldsymbol b) + \mu (\boldsymbol b \cdot \boldsymbol b) &= \det(\boldsymbol b, \boldsymbol a \times \boldsymbol b, \boldsymbol a) \\
&= (\boldsymbol a \times \boldsymbol b) \cdot (\boldsymbol a \times \boldsymbol b)
\end{aligned}
$$

By the identity derived earlier:

$$
(\boldsymbol a \times \boldsymbol b) \cdot (\boldsymbol a \times \boldsymbol b) = |\boldsymbol a|^2|\boldsymbol b|^2-(\boldsymbol a \cdot \boldsymbol b)^2
$$

we can solve:

$$
\begin{aligned}
\lambda &= -\boldsymbol a \cdot \boldsymbol b \\
\mu &= \boldsymbol a \cdot \boldsymbol a
\end{aligned}
$$

This completes the proof.

In the proof above it was mentioned that the cross product of $\boldsymbol a \times \boldsymbol b$ with any vector is coplanar with $\boldsymbol a$ and $\boldsymbol b$. Next we prove the result on the **vector triple product**:

$$
(\boldsymbol a\times \boldsymbol b)\times \boldsymbol c=(\boldsymbol a \cdot \boldsymbol c)\boldsymbol b - (\boldsymbol b \cdot \boldsymbol c)\boldsymbol a
$$

The coplanarity above helps in memorizing the vector triple product formula. Clearly, the lemma above is a special case of the vector triple product.

Proof: it suffices to consider the case where all three vectors are nonzero and non-collinear; the other special cases are obvious.

The three-dimensional vectors $\boldsymbol a$, $\boldsymbol b$ and $\boldsymbol a \times \boldsymbol b$ are not coplanar, so we may assume:

$$
\boldsymbol c = \alpha \boldsymbol a + \beta \boldsymbol b + \gamma(\boldsymbol a \times \boldsymbol b)
$$

Hence:

$$
\begin{aligned}
(\boldsymbol a \times \boldsymbol b) \times \boldsymbol c &= (\boldsymbol a \times \boldsymbol b) \times (\alpha \boldsymbol a + \beta \boldsymbol b + \gamma(\boldsymbol a \times \boldsymbol b)) \\
&= \alpha(\boldsymbol a \times \boldsymbol b) \times \boldsymbol a + \beta(\boldsymbol a \times \boldsymbol b) \times \boldsymbol b
\end{aligned}
$$

By the lemma above:

$$
\begin{aligned}
(\boldsymbol a \times \boldsymbol b) \times \boldsymbol a &=(\boldsymbol a \cdot \boldsymbol a) \boldsymbol b - (\boldsymbol a \cdot \boldsymbol b) \boldsymbol a \\
(\boldsymbol a \times \boldsymbol b) \times \boldsymbol b
&= -(\boldsymbol b \times \boldsymbol a) \times \boldsymbol b \\
&= -(\boldsymbol b \cdot \boldsymbol b)\boldsymbol a+(\boldsymbol a \cdot \boldsymbol b) \boldsymbol b
\end{aligned}
$$

Therefore:

$$
\begin{aligned}
(\boldsymbol a \times \boldsymbol b) \times \boldsymbol c &= \alpha((\boldsymbol a \cdot \boldsymbol a)\boldsymbol b - (\boldsymbol a \cdot \boldsymbol b)\boldsymbol a) + \beta((\boldsymbol a \cdot \boldsymbol b)\boldsymbol b - (\boldsymbol b \cdot \boldsymbol b)\boldsymbol a) \\
&=(\alpha(-\boldsymbol a \cdot \boldsymbol b) + \beta(-\boldsymbol b \cdot \boldsymbol b))\boldsymbol a + (\alpha \boldsymbol a \cdot \boldsymbol a + \beta \boldsymbol a \cdot \boldsymbol b)\boldsymbol b \\
&= (\boldsymbol a \cdot \boldsymbol c) \boldsymbol b - (\boldsymbol b \cdot \boldsymbol c) \boldsymbol a
\end{aligned}
$$

This completes the proof.

By the anticommutativity of the cross product, we obtain the two formulas for the vector triple product:

$$
\begin{aligned}
(\boldsymbol a\times \boldsymbol b)\times \boldsymbol c &=(\boldsymbol a \cdot \boldsymbol c)\boldsymbol b - (\boldsymbol b \cdot \boldsymbol c)\boldsymbol a \\
\boldsymbol a \times(\boldsymbol b \times \boldsymbol c) &= (\boldsymbol a \cdot \boldsymbol c)\boldsymbol b - (\boldsymbol a \cdot \boldsymbol b)\boldsymbol c
\end{aligned}
$$

Clearly, the vector triple product has strict requirements on the order of operations.

With the help of the scalar triple product and the vector triple product, Lagrange's identity can also be proved.

$$
(\boldsymbol a \times \boldsymbol b) \cdot (\boldsymbol c \times \boldsymbol d)=(\boldsymbol a \cdot \boldsymbol c)(\boldsymbol b \cdot \boldsymbol d)-(\boldsymbol a \cdot \boldsymbol d)(\boldsymbol b \cdot \boldsymbol c)
$$

Proof:

$$
\begin{aligned}
(\boldsymbol a \times \boldsymbol b) \cdot (\boldsymbol c \times \boldsymbol d) &= \det(\boldsymbol c, \boldsymbol d, \boldsymbol a \times \boldsymbol b) \\
&= \det(\boldsymbol a \times \boldsymbol b, \boldsymbol c, \boldsymbol d) \\
&= ((\boldsymbol a \times \boldsymbol b)\times \boldsymbol c)\cdot \boldsymbol d \\
&= (\boldsymbol b(\boldsymbol a \cdot \boldsymbol c)- \boldsymbol a(\boldsymbol b \cdot \boldsymbol c))\cdot \boldsymbol d \\
&= (\boldsymbol a \cdot \boldsymbol c)(\boldsymbol b \cdot \boldsymbol d) - (\boldsymbol a \cdot \boldsymbol d)(\boldsymbol b \cdot \boldsymbol c)
\end{aligned}
$$

Clearly, the earlier identity

$$
(\boldsymbol a \times \boldsymbol b) \cdot (\boldsymbol a \times \boldsymbol b) = |\boldsymbol a|^2|\boldsymbol b|^2 - (\boldsymbol a \cdot \boldsymbol b)^2
$$

is a special case of Lagrange's identity.
