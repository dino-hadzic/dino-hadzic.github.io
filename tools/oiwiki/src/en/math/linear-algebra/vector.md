---
title: Vectors
---

Before the main text, a special note on translation. For historical reasons, mathematics and physics translate the word "vector" into Chinese differently.

In physics it is usually translated as "矢量" (shǐliàng, "arrow quantity"), as opposed to the term "标量" (scalar). In mathematics it is usually translated as "向量" (xiàngliàng, "directed quantity"). Similar differences in translation exist between "本征" and "特征" (for "eigen-"), "幺正" and "酉" (for "unitary"), and so on.

Since **OI Wiki** is aimed mainly at computer science and related engineering disciplines, which are closer to mathematics, it uses the word "向量".

## Definition and related concepts

**Vector**: a quantity that has both magnitude and direction is called a vector. The vectors studied in mathematics are **free vectors**, i.e. vectors whose initial and terminal points can be translated arbitrarily as long as their magnitude and direction do not change. A vector is denoted by $\vec a$ or $\boldsymbol{a}$.

**Directed line segment**: a line segment with a direction is called a directed line segment. A directed line segment has three elements: **initial point, direction, and length**; once these three elements are known, the terminal point is uniquely determined. Vectors are usually represented by directed line segments.

**Magnitude of a vector**: the length of the directed line segment $\overrightarrow{AB}$ is called the magnitude of the vector, i.e. the size of this vector. It is denoted by $|\overrightarrow{AB}|$ or $|\boldsymbol{a}|$.

**Zero vector**: a vector of magnitude $0$. The direction of the zero vector is arbitrary. It is denoted by $\vec 0$ or $\boldsymbol{0}$.

**Unit vector**: a vector of magnitude $1$ is called the unit vector in that direction. It is usually denoted by $\vec e$ or $\boldsymbol{e}$.

**Parallel vectors**: two **nonzero** vectors with the same or opposite direction. Denoted by $\boldsymbol a\parallel \boldsymbol b$. For several mutually parallel vectors, one can draw any line parallel to these vectors, and then any group of parallel vectors can be translated onto the same line, so parallel vectors are also called **collinear vectors**.

**Equal vectors**: vectors with equal magnitude and the same direction.

**Opposite vectors**: vectors with equal magnitude and opposite directions.

**Angle between vectors**: given two nonzero vectors $\boldsymbol a,\boldsymbol b$, draw $\overrightarrow{OA}=\boldsymbol a,\overrightarrow{OB}=\boldsymbol b$; then $\theta=\angle AOB$ is the angle between the vector $\boldsymbol a$ and the vector $\boldsymbol b$. It is denoted by $\langle \boldsymbol a,\boldsymbol b\rangle$. Clearly, when $\theta=0$ the two vectors have the same direction, when $\theta=\pi$ they have opposite directions, and when $\theta=\frac{\pi}{2}$ they are perpendicular, denoted by $\boldsymbol a\perp \boldsymbol b$; by convention $\theta \in [0,\pi]$.

Note that plane vectors have a direction, so two vectors cannot be compared by size (although the magnitudes of two vectors can be compared). Two vectors can, however, be equal.

## Linear operations on vectors

### Addition and subtraction of vectors

Once a kind of quantity has been defined, we want it to have operations. Operations on vectors can be introduced by analogy with operations on numbers, and they can also be studied from the point of view of physics.

By analogy with the concept of displacement in physics: if a person walks from $A$ via $B$ to $C$, the displacement is $\overrightarrow{AB}+\overrightarrow{BC}$, which is in fact equivalent to walking directly from $A$ to $C$, i.e. $\overrightarrow{AB}+\overrightarrow{BC}=\overrightarrow{AC}$.

Note that the rule for composing forces, the parallelogram rule, can likewise be regarded as adding some vectors.

Let us summarize the rules of vector addition:

1.  **Triangle rule of vector addition**: if the vectors to be added are joined head to tail in order, their sum is the vector from the initial point of the first vector to the terminal point of the last one;
2.  **Parallelogram rule of vector addition**: if the two vectors to be added **share an initial point**, their sum is the diagonal of the parallelogram with these two vectors as adjacent sides, starting at the common initial point and pointing along the diagonal of the parallelogram.

In this way vector addition acquires a geometric meaning. Moreover, one can verify that vector addition satisfies the **commutative and associative laws**.

Since subtraction of real numbers can be written as adding the opposite number, we write vector subtraction the same way, i.e.: $\boldsymbol a-\boldsymbol b=\boldsymbol a+(-\boldsymbol b)$.

Thus, taking vectors with a common initial point and constructing their difference by the parallelogram rule, after a translation we find that **the "difference of vectors with a common initial point" is the directed line segment pointing from the "subtrahend" to the "minuend"**. This is the geometric meaning of vector subtraction.

Sometimes we have two points $A,B$ and want to know $\overrightarrow{AB}$; it can be obtained by subtraction: $\overrightarrow{AB}=\overrightarrow{OB}-\overrightarrow{OA}$.

### Scalar multiplication of vectors

The "product of a real number $\lambda$ and a vector $\boldsymbol a$" is defined to be a vector; this operation is **scalar multiplication**, denoted by $\lambda \boldsymbol a$, and its length and direction are defined as follows:

1.  $|\lambda \boldsymbol a|=|\lambda||\boldsymbol a|$;
2.  when $\lambda >0$, $\lambda\boldsymbol a$ has the same direction as $\boldsymbol a$; when $\lambda =0$, $\lambda \boldsymbol a=\boldsymbol 0$; when $\lambda<0$, $\lambda \boldsymbol a$ has the direction opposite to $\boldsymbol a$.

From the definition of scalar multiplication one can verify the following laws:

$$
\begin{aligned}
\lambda(\mu \boldsymbol a)&=(\lambda \mu)\boldsymbol a\\
(\lambda+\mu)\boldsymbol a&=\lambda \boldsymbol a+\mu \boldsymbol a\\
\lambda(\boldsymbol a+\boldsymbol b)&=\lambda \boldsymbol a+\lambda \boldsymbol b
\end{aligned}
$$

In particular:

$$
\begin{gathered}
(-\lambda)\boldsymbol a=-(\lambda \boldsymbol a)=-\lambda(\boldsymbol a)\\
\lambda(\boldsymbol a-\boldsymbol b)=\lambda \boldsymbol a-\lambda \boldsymbol b
\end{gathered}
$$

### Testing whether two vectors are collinear

Two **nonzero** vectors $\boldsymbol a$ and $\boldsymbol b$ are collinear $\iff$ there is a unique real number $\lambda$ such that $\boldsymbol b=\lambda \boldsymbol a$.

Proof: by the definition of scalar multiplication, for a **nonzero** vector $\boldsymbol a$, if there is a real number $\lambda$ such that $\boldsymbol b=\lambda \boldsymbol a$, then $\boldsymbol a \parallel \boldsymbol b$.

Conversely, if $\boldsymbol a\parallel \boldsymbol b$, $\boldsymbol a \not = \boldsymbol 0$, and $|\boldsymbol b|=\mu |\boldsymbol a|$, then $\boldsymbol b=\mu \boldsymbol a$ when $\boldsymbol a$ and $\boldsymbol b$ have the same direction, and $\boldsymbol b=-\mu \boldsymbol a$ when they have opposite directions.

Finally, addition, subtraction and scalar multiplication of vectors are collectively called the linear operations on vectors.

## Fundamental theorem of plane vectors and coordinate representation

### Fundamental theorem of plane vectors

Statement: if two vectors $\boldsymbol{e_1},\boldsymbol{e_2}$ are not collinear, then for any vector $\boldsymbol p$ coplanar with $\boldsymbol{e_1},\boldsymbol{e_2}$ there is a unique pair of real numbers $(x,y)$ such that $\mathbf p=x\boldsymbol{e_1}+y\boldsymbol{e_2}$.

There are so many plane vectors; how can all of them be represented with as few quantities as possible?

Representing all vectors with a single vector is clearly impossible; at most the vectors on one line can be represented.

Adding one more vector and representing vectors with two **non-collinear** vectors (two collinear vectors can be regarded as the same vector here), any plane vector can be decomposed along the directions of these two vectors.

Two non-collinear vectors in the same plane are called a **basis**. If the basis vectors are mutually perpendicular, the decomposition of a vector is an **orthogonal decomposition**.

### Coordinate representation of plane vectors

If we take the unit vectors $i,j$ in the directions of the horizontal and vertical axes as a basis, then by the fundamental theorem of plane vectors all vectors in the plane are in one-to-one correspondence with ordered pairs of real numbers $(x,y)$.

Ordered pairs of real numbers $(x,y)$ are in turn in one-to-one correspondence with the points of the rectangular coordinate system in the plane, so if we draw $\overrightarrow{OP}=\boldsymbol p$, the terminal point $P(x,y)$ is also uniquely determined. Since the objects of study are free vectors, the initial point can be translated freely, and so in the rectangular coordinate system in the plane every vector can be uniquely represented by an ordered pair of real numbers.

## Coordinate operations on plane vectors

### Linear operations on plane vectors

The coordinate operations can be derived from the linear operations on plane vectors; the main method is to express all coordinates in terms of the basis, combine them using the laws of operations, and then write the result in coordinate form.

If $\boldsymbol a=(m,n)$, $\boldsymbol b=(p,q)$ are two vectors, then:

$$
\begin{aligned}
\boldsymbol a+\boldsymbol b&=(m+p,n+q)\\
\boldsymbol a-\boldsymbol b&=(m-p,n-q)\\
k\boldsymbol a&=(km,kn)
\end{aligned}
$$

### Finding the coordinate representation of a vector

Given two points $A(a,b),B(c,d)$, it is easy to show that $\overrightarrow{AB}=(c-a,d-b)$.

### Translating a point

Sometimes a point $P$ has to be translated by some number of units of length in a certain direction. Combine the direction and distance of the translation into one vector and, by the triangle rule of vector addition, add this vector to $\overrightarrow{OP}$; the terminal point of the resulting vector is the translated point.

### Testing whether three points are collinear

If three points $A,B,C$ are collinear, then $\overrightarrow{OB}=\lambda \overrightarrow{OA}+(1-\lambda)\overrightarrow{OC}$.

### Extension of the three-point collinearity test

In triangle $ABC$, if $D$ is one of the points dividing $BC$ into $n$ equal parts ($n\ BD=k\ DC$), then: $\overrightarrow{AD}=\frac{n}{k+n}\overrightarrow{AB}+\frac{k}{k+n}\overrightarrow{AC}$

## Extension to three-dimensional space (solid geometry / space vectors)

In space, everything stated in the sections above still holds. Furthermore:

### Fundamental theorem of space vectors

Statement: if three vectors $\boldsymbol{e_1},\boldsymbol{e_2},\boldsymbol{e_3}$ are not coplanar, then for any vector $\boldsymbol p$ in space there is a unique triple of real numbers $(x,y,z)$ such that $\mathbf p=x\boldsymbol{e_1}+y\boldsymbol{e_2}+z\boldsymbol{e_3}$.
By the fundamental theorem of space vectors, we can likewise take three mutually perpendicular basis vectors $\boldsymbol{e_1},\boldsymbol{e_2},\boldsymbol{e_3}$ as an orthogonal basis, set up a **rectangular coordinate system in space**, and represent space vectors by a triple $(x,y,z)$ as coordinates.

### Fundamental theorem of coplanar vectors

If there are two non-collinear vectors $\boldsymbol{x},\boldsymbol{y}$, then a vector $\boldsymbol{p}$ is coplanar with $\boldsymbol{x},\boldsymbol{y}$ if and only if there is a unique pair of real numbers $(a,b)$ such that $\boldsymbol{p}=a\boldsymbol{x}+b\boldsymbol{y}$.

### Direction vector

The direction of a line in space is represented by a nonzero vector parallel to the line; this vector is called a direction vector of the line. The position of a line in space is **completely determined** by a point of space it passes through and one of its direction vectors.

Note that lines in the plane also have direction vectors.

For a line in **space**, a direction vector can be found as follows:

-   If $A(x_1,y_1,z_1),B(x_2,y_2,z_2)$ are given, then a direction vector of the line $AB$ is $\boldsymbol{s}=(x_2-x_1,y_2-y_1,z_2-z_1)$.

-   If a plane **perpendicular** to the required line is known, with general equation $ax+by+cz+d=0$, then a direction vector of the line perpendicular to this plane is $\boldsymbol{s}=(a,b,c)$; this direction vector is also **a normal vector** of the plane.

### Normal vector

For a plane (face) $ABCD$, its normal vector $\boldsymbol{n}$ is perpendicular to this plane.

Computation: take any two vectors in the plane, $\overrightarrow{AB},\overrightarrow{AD}$, such that $\overrightarrow{AB} \cdot \boldsymbol{n}=\boldsymbol{0}$ and $\overrightarrow{AD} \cdot \boldsymbol{n}=\boldsymbol{0}$, and compute it by the coordinate method.

## Vectors and matrices

In linear algebra, linear transformations can be represented by matrices. Let $T$ denote a linear transformation mapping $\mathbf R^n$ to $\mathbf R^m$, and let $\mathbf x$ be an $n$-dimensional column vector; then there is an $m\times n$ matrix $A$ such that

$$
T(\mathbf x)=A\mathbf x.
$$

The matrix $A$ is called the transformation matrix of the linear transformation $T$. In algorithmic problems, linear transformations are usually performed within the same dimension, so $A$ is a square matrix. Thus the problem of linearly transforming a vector can be turned into a matrix multiplication problem.

Next we discuss three transformations that are fairly common in contests and their transformation matrices: scaling (transformation matrix denoted by $S$), rotation (transformation matrix denoted by $R$) and translation (transformation matrix denoted by $T$).

### Scaling

For an $n$-dimensional column vector $\boldsymbol a$, scale each of its components by the factors $v_1,v_2,\ldots,v_n$. It is easy to see that the transformation matrix $R$ of scaling is an $n\times n$ diagonal matrix, i.e. $S=\operatorname{diag}\{v_1,v_2,\ldots,v_n\}$.

### Rotation

Rotating a vector is a relatively complicated operation; we restrict ourselves to the two- and three-dimensional cases.

#### Rotating a vector about a point

Rotating a vector about a point usually means rotating the vector about the origin. To rotate a point about another point $P$, we can use a translation so that $P$ is at the origin, rotate the vector, and then translate the coordinate system back to its original position. If the transformation matrix of the translation is $T$ and that of the rotation about the origin is $R$, the transformation matrix of the whole process is $TRT^{-1}$. By its geometric meaning, $T^{-1}$ always exists.

In two-dimensional space, let $\boldsymbol a=(x,y)$ with inclination angle $\theta$ and length $l=\sqrt{x^2+y^2}$. Then $x=l\cos \theta,y=l\sin\theta$. Rotating it counterclockwise about the origin by an angle $\alpha$ gives the vector $\boldsymbol b=(l\cos(\theta+\alpha),l\sin(\theta+\alpha))$.

![](./images/vector-rotation.svg)

By the trigonometric identities,

$$
\boldsymbol{b}=(l(\cos\theta\cos\alpha-\sin\theta\sin\alpha),l(\sin\theta\cos\alpha+\cos\theta\sin\alpha))
$$

Simplifying,

$$
\boldsymbol b=(l\cos\theta\cos\alpha-l\sin\theta\sin\alpha,l\sin\theta\cos\alpha+l\cos\theta\sin\alpha)
$$

Substituting $x,y$ back gives

$$
\boldsymbol b=(x\cos\alpha-y\sin\alpha,y\cos\alpha+x\sin\alpha)
$$

Therefore, in two-dimensional space the transformation matrix $R$ is

$$
R=
\begin{bmatrix}
\cos\alpha & -\sin\alpha\\
\sin\alpha & \cos\alpha
\end{bmatrix}.
$$

In three-dimensional space, rotating a vector requires two angle parameters, namely the rotation of the zenith angle and the rotation of the azimuth angle; the rotation can be carried out using the [spherical coordinate system in space](../coordinate.md#spherical-coordinate-system).

#### Rotating a vector about a line

For three-dimensional vectors, rotation about a line is more common. Again for convenience, we assume the line passes through the origin. If the line does not pass through the origin, we can still reduce to this case by translating the coordinate system.

Take a direction vector $\boldsymbol u=(u_x,u_y,u_z)$ of the line and rotate the three-dimensional vector about it counterclockwise by an angle $\theta$. Then the corresponding transformation matrix $R$ is[^note1]

$$
R=
\begin{bmatrix}
u_x^2 \left(1-\cos \theta\right) + \cos \theta & u_x u_y \left(1-\cos \theta\right) - u_z \sin \theta & u_x u_z \left(1-\cos \theta\right) + u_y \sin \theta \\ 
u_x u_y \left(1-\cos \theta\right) + u_z \sin \theta & u_y^2\left(1-\cos \theta\right) + \cos \theta & u_y u_z \left(1-\cos \theta\right) - u_x \sin \theta \\ 
u_x u_z \left(1-\cos \theta\right) - u_y \sin \theta & u_y u_z \left(1-\cos \theta\right) + u_x \sin \theta & u_z^2\left(1-\cos \theta\right) + \cos \theta
\end{bmatrix}.
$$

### Translation

Translation is not a linear transformation but an affine transformation. However, an affine transformation in $\mathbf R^n$ can still be represented by a linear transformation in $\mathbf R^{n+1}$.

Consider an $n$-dimensional vector $\boldsymbol a=(a_1,a_2, \ldots , a_n)$ which we want to translate along the vector $\boldsymbol t=(t_1, t_2, \ldots , t_n)$. We append one more component to the column vector $\boldsymbol a$ and set it to $1$, obtaining the new column vector $\boldsymbol a'=(a_1, a_2, \ldots , a_n, 1)$. Then the transformation matrix $T$ can be written as

$$
T=
\begin{bmatrix}
1 &   &        &   & t_1    \\
  & 1 &        &   & t_2    \\
  &   & \ddots &   & \vdots \\
  &   &        & 1 & t_n    \\
  &   &        &   & 1      \\
\end{bmatrix}.
$$

For other linear transformation matrices, add one column and one row to the matrix, with the bottom-right element equal to $1$ and all the other new entries filled with $0$; in this way every linear transformation matrix can be converted into an affine transformation matrix. For example, for the rotation of a two-dimensional vector the transformation matrix becomes

$$
R'=
\begin{bmatrix}
\cos\alpha & -\sin\alpha & 0\\
\sin\alpha & \cos\alpha & 0\\
0 & 0 & 1
\end{bmatrix}.
$$

## A more rigorous definition of vectors

Above, vectors were defined as directed line segments in space. Strictly speaking, however, vectors are not only directed line segments. To define vectors more rigorously, one first has to define a [vector space](./vector-space.md); see the [Vector space](./vector-space.md) page for details.

[^note1]: See [Rotation matrix from axis and angle - Wikipedia](https://en.wikipedia.org/wiki/Rotation_matrix#Rotation_matrix_from_axis_and_angle)
