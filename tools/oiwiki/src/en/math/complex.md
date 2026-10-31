---
title: Complex numbers
---

If you have already learned about complex numbers, skip this page.

Learning about complex numbers requires some background on vectors; if you have not learned about vectors yet, see the [page on vectors](../math/linear-algebra/vector.md).

## Complex numbers

### Introduction

???+ note "Note"
    The introduction below is taken from a Chinese high-school mathematics textbook (人教版 A 版必修二, People's Education Press edition, version A, compulsory volume 2).

From the point of view of equations, whether a negative real number has a square root is the question of whether the equation $x^2+a=0 (a>0)$ has a solution, which reduces to whether the equation $x^2+1=0$ has a solution.

Looking back at the previous extensions of number sets, we see that each extension was closely tied to a practical need. For example, to solve the problem of measuring the diagonal of a square, and the problem that an equation like $x^2-2=0$ has no solution in the set of rational numbers, people extended the set of rational numbers to the set of real numbers. After the extension, the addition and multiplication defined on the set of real numbers agree with the addition and multiplication previously defined on the set of rational numbers, and addition and multiplication are both commutative and associative, and multiplication is distributive over addition.

Following this idea, to solve the problem that an equation like $x^2+1=0$ has no solution in the real number system, we imagine introducing a new number $\mathrm{i}$ such that $x=\mathrm{i}$ is a solution of the equation $x^2+1=0$, i.e. such that $\mathrm{i}^2=-1$.

Think about it: after adding the newly introduced number $\mathrm{i}$ to the set of real numbers, we want the number $\mathrm{i}$ and the real numbers to still support addition and multiplication just like real numbers do, and we want addition and multiplication to be commutative and associative, and multiplication to be distributive over addition. So, after extending the real number system, which numbers make up the new number system?

Following the idea above, we write the product of a real number $b$ and $\mathrm{i}$ as $b\mathrm{i}$, and the sum of a real number $a$ and $b\mathrm{i}$ as $a+b\mathrm{i}$. Note that all real numbers as well as $\mathrm{i}$ can be written in the form $a+b\mathrm{i}(a,b\in \mathbf{R})$, so all these numbers belong to the extended new number set.

### Definition

We define numbers of the form $a+b\mathrm{i}$, where $a,b\in \mathbf{R}$, to be **complex numbers**; here $\mathrm{i}$ is called the **imaginary unit**, and the set of all complex numbers is called the **set of complex numbers**, denoted by $\mathbf{C}$.

Complex numbers are usually denoted by $z$, i.e. $z=a+b\mathrm{i}$. This form is called the **algebraic form of a complex number**. Here $a$ is called the **real part** of the complex number $z$, denoted by $\operatorname{Re}(z)$, and $b$ is called the **imaginary part** of $z$, denoted by $\operatorname{Im}(z)$. Unless stated otherwise, we always have $a,b\in \mathbf{R}$.

A complex number $z$ is real if and only if $b=0$; when $b\not = 0$ it is imaginary, and when $a=0$ and $b\not = 0$ it is purely imaginary.

The relationship between purely imaginary, imaginary, real and complex numbers is shown in the figure below.

![](./images/complex-relation.svg)

## Properties and operations

### Geometric meaning

We know that numbers of the form $a+b\mathrm{i}$ are called complex numbers, and we have given their definition and classification; now we can dig into some deeper properties.

We placed all real numbers on the number line and found that the points of the number line correspond one-to-one to the real numbers. Let us consider doing the same for complex numbers.

First we define **equality of complex numbers**: two complex numbers $z_1=a+b\mathrm{i},z_2=c+d\mathrm{i}$ are equal if and only if $a=c$ and $b=d$.

This definition is very natural, and we do not explain it further here.

In other words, we can represent a complex number $z=a+b\mathrm{i}$ by the unique ordered pair of real numbers $(a,b)$. Thus, thinking of the rectangular coordinate system, we find that **the set of complex numbers corresponds one-to-one to the set of points of the rectangular coordinate system**. Good, we have found one geometric meaning of complex numbers.

This rectangular coordinate system is then no longer an ordinary one, since its points have a special meaning: they represent complex numbers. So we call such a rectangular coordinate system the **complex plane**, the $x$-axis the **real axis**, and the $y$-axis the **imaginary axis**. We further say: **the set of complex numbers corresponds one-to-one to the set of all points of the complex plane**.

Recalling what we learned about plane vectors, we find that the coordinate representation of a vector is also an ordered pair of real numbers $(a,b)$. Clearly, the complex number $z=a+b\mathrm{i}$ corresponds to the point $Z(a,b)$ of the complex plane, so it also corresponds to the plane vector $\overrightarrow{OZ}=(a,b)$. Thus we have found another geometric meaning of complex numbers: **the set of complex numbers corresponds one-to-one to the set of vectors in the complex plane (the real number $0$ corresponds to the zero vector)**.

Transferring our knowledge of vectors to complex numbers, we define the **modulus of a complex number** to be the modulus (length) of the vector corresponding to it. The modulus of the complex number $z=a+b\mathrm{i}$ is $|z|=\sqrt{a^2+b^2}$.

For convenience, we often refer to the complex number $z=a+b\mathrm{i}$ as the point $Z$ or the vector $\overrightarrow {OZ}$, and we agree that equal vectors represent the same complex number.

Also, from our knowledge of vectors we see that imaginary numbers cannot be compared by size (whereas real numbers can).

### Addition and subtraction

For complex numbers $z_1=a+b\mathrm{i},z_2=c+d\mathrm{i}$, addition is defined as follows:

$$
z_1+z_2=(a+c)+(b+d)\mathrm{i}
$$

Clearly, the sum of two complex numbers is again a complex number.

Comparing with vector addition, we find that addition of complex numbers follows the rule of vector addition, which again confirms the correctness of the geometric meaning of complex numbers.

Likewise one can verify that addition of complex numbers is **commutative** and **associative**, i.e.:

$$
\begin{aligned}
z_1+z_2&=z_2+z_1\\
(z_1+z_2)+z_3&=z_1+(z_2+z_3)
\end{aligned}
$$

Subtraction is the inverse operation of addition, so we can derive the rule for subtraction from the rule for addition and the definition of equality of complex numbers:

$$
z_1-z_2=(a-c)+(b-d)\mathrm{i}
$$

This also agrees with vector subtraction.

### Multiplication, division and conjugation

For complex numbers $z_1=a+b\mathrm{i},z_2=c+d\mathrm{i}$, multiplication is defined as follows:

$$
\begin{aligned}
z_1z_2&=(a+b\mathrm{i})(c+d\mathrm{i})\\
&=ac+bc\mathrm{i}+ad\mathrm{i}+bd\mathrm{i}^2\\
&=(ac-bd)+(bc+ad)\mathrm{i}
\end{aligned}
$$

We see that multiplying two complex numbers is similar to multiplying two polynomials: just replace $\mathrm{i}^2$ by $-1$ and collect the real and imaginary parts separately.

Multiplication of complex numbers is similar in form to the cross product of vectors.

It is easy to see that multiplication of complex numbers is **commutative**, **associative** and **distributive over addition**, i.e.:

-   $z_1z_2=z_2z_1$
-   $(z_1z_2)z_3=z_1(z_2z_3)$
-   $z_1(z_2+z_3)=z_1z_2+z_1z_3$

Since these laws hold, we find that the **multiplication formulas of the real field also hold in the complex field**.

Division is the inverse operation of multiplication; let us derive it:

$$
\begin{aligned}
\frac{a+b\mathrm{i}}{c+d\mathrm{i}}&=\frac{(a+b\mathrm{i})(c-d\mathrm{i})}{(c+d\mathrm{i})(c-d\mathrm{i})}\\
&=\frac{ac+bd}{c^2+d^2}+\frac{bc-ad}{c^2+d^2}\mathrm{i} &(c+d\mathrm{i}\not =0)
\end{aligned}
$$

Since vectors have no division, we do not discuss the relation to vectors here.

To make the denominator real, we multiplied by $c-d\mathrm{i}$; this expression is very meaningful.

For a complex number $z=a+b\mathrm{i}$, the number $a-b\mathrm{i}$ is called the **complex conjugate** of $z$, usually denoted by $\bar z$. We find that if two complex numbers are conjugates of each other, they are **symmetric with respect to the real axis**.

For complex numbers $z,w$, complex conjugation has the following properties:

-   $z\cdot\bar{z}=|z|^2$
-   $\overline{\overline{z}}=z$
-   $\operatorname{Re}(z)=\dfrac{z+\bar{z}}{2}$, $\operatorname{Im}(z)=\dfrac{z-\bar{z}}{2}$
-   $\overline{z\pm w}=\bar{z}\pm\bar{w}$
-   $\overline{zw}=\bar{z}\bar{w}$
-   $\overline{z/w}=\bar{z}/\bar{w}$

### Argument and principal value of the argument

If we take the real unit $1$ as the positive horizontal direction and the imaginary unit $\mathrm{i}$ as the positive vertical direction, we obtain the complex plane viewed in rectangular coordinates.

The position of a complex number $z$ can also be determined using polar coordinates $(r, \theta)$. We have already mentioned that $r$ is the modulus of the complex number $z$.

The angle $\theta$ from the positive real axis to the vector corresponding to a **nonzero** complex number $z=x+\mathrm{i}y$ satisfies the relation:

$$
\tan \theta=\frac{y}{x}
$$

and is called the **argument** of the complex number $z$, denoted by:

$$
\theta= \arg z
$$

Any **nonzero** complex number $z$ has infinitely many arguments, so $\arg z$ is in fact a set. The capitalized notation $\operatorname{Arg} z$ denotes **one particular value** satisfying the condition:

$$
-\pi<\operatorname{Arg} z \le \pi
$$

$\operatorname{Arg} z$ is called the **principal value of the argument** or the **principal argument**. An argument is the principal value of the argument plus an integer multiple (possibly zero or negative) of $2k\pi$, i.e. $\arg z = \{\operatorname{Arg} z + 2k\pi \mid k\in \mathbf Z\}$.

Note that the sum of two principal values of the argument is not necessarily a principal value of the argument, while the sum of two arguments is always a valid argument.

The figure formed in the complex plane by the complex numbers of modulus less than $1$ is called the **unit disk**. Complex numbers of modulus equal to $1$ are called **unit complex numbers**, and the figure formed in the complex plane by all unit complex numbers is called the **unit circle**. When no confusion can arise, the unit circle is sometimes also referred to simply as the unit disk.

Viewed in polar coordinates, multiplication and division of complex numbers become very simple. For complex multiplication, the moduli are multiplied and the arguments are added. For complex division, the moduli are divided and the arguments are subtracted.

### Euler's formula

???+ note "Euler's formula[^ref1]"
    For every real number $x$,
    
    $$
    \mathrm{e}^{\mathrm{i}x}=\cos x+\mathrm{i}\sin x
    $$
    
    After supplementing the definitions of the [complex exponential function and complex trigonometric functions](#exponential-function-and-trigonometric-functions), this formula can be extended to all complex numbers.

### Exponential function and trigonometric functions

For a complex number $z=x+\mathrm{i}y$, the function $f(z)=\mathrm{e}^x(\cos y+\mathrm{i}\sin y)$ satisfies $f(z_1+z_2)=f(z_1)f(z_2)$. This gives the definition of the **complex exponential function**:

$$
\exp z=\mathrm{e}^x(\cos y+\mathrm{i}\sin y)
$$

On the set of real numbers the complex exponential function agrees completely with the real exponential function. In the complex plane it has the following properties:

-   The modulus is always positive: $|\exp z|=\exp x>0$.
-   Argument: $\arg(\exp z)=\{y + 2k\pi \mid k\in\mathbf Z\}$.
-   Addition theorem: $\exp (z_1+z_2)=\exp (z_1)\exp (z_2)$.
-   Periodicity: $\exp z$ is a periodic function with fundamental period $2\pi \mathrm{i}$. If every period of a function $f(z)$ is an integer multiple of some period, that period is called the **fundamental period**.

The **complex trigonometric functions** (also simply called **trigonometric functions**) are defined as follows:

$$
\cos z=\frac{\exp (\mathrm{i}z)+\exp (-\mathrm{i}z)}{2}
$$

$$
\sin z=\frac{\exp (\mathrm{i}z)-\exp (-\mathrm{i}z)}{2\mathrm{i}}
$$

If we take $z\in\mathbf{R}$, then by [Euler's formula](#eulers-formula):

$$
\cos z=\operatorname{Re}\left(\mathrm{e}^{\mathrm{i}z}\right)
$$

$$
\sin z=\operatorname{Im}\left(\mathrm{e}^{\mathrm{i}z}\right)
$$

On the set of real numbers the complex trigonometric functions agree completely with the real trigonometric functions. In the complex plane they have the following properties:

-   Parity: the sine function is odd and the cosine function is even.
-   Trigonometric identities: the usual trigonometric identities still hold, e.g. the sum of squares equals $1$, the angle sum and difference formulas, etc.
-   Periodicity: the sine and cosine functions have fundamental period $2\pi$.
-   Zeros: all the zeros of the real sine and cosine functions constitute all the zeros of the complex sine and cosine functions. This extension introduces no new zeros.
-   Unboundedness of the modulus: the modulus of the complex sine and cosine functions can exceed any given positive number; it is no longer bounded by $1$ as for the real sine and cosine functions.

## Three forms of a complex number

Using the rectangular and the polar coordinate viewpoints, a complex number can be written in three forms.

The **algebraic form** of a complex number is used to represent an arbitrary complex number.

$$
z=x+y\mathrm{i}
$$

The algebraic form is convenient for computing the four operations of addition, subtraction, multiplication and division of complex numbers.

The **trigonometric form** and the **exponential form** of a complex number are used to represent nonzero complex numbers.

$$
z=r(\cos \theta +\mathrm{i}\sin \theta)=r \exp (\mathrm{i}\theta)
$$

These two forms are more convenient for computing multiplication and division of complex numbers and the operations that follow. If only functions seen in high school are used, the trigonometric form can be used. If the complex exponential function has been introduced, writing the equivalent exponential form is more convenient.

## Roots of unity

Consider the solutions of the equation $x^n=1$ over the complex numbers. Clearly there are $n$ such solutions, and all these $n$ solutions are called **$n$-th (complex) roots of unity**. From our knowledge of the complex plane, the $n$-th roots of unity divide the unit circle into $n$ equal parts.

Let $\omega_n=\exp\dfrac{2\pi \mathrm{i}}{n}$ (i.e. the unit complex number with argument $2\pi/n$); then the solution set of $x^n=1$ is $\{\omega_n^k\mid k=0,1\cdots,n-1\}$, where

$$
w_n^k = \exp\dfrac{2\pi k \mathrm{i}}{n} = \cos\dfrac{2\pi k}{n} + \mathrm{i}\sin\dfrac{2\pi k}{n}.
$$

Unless stated otherwise, "the $n$-th root of unity" in general discussion refers to the first solution counterclockwise from $1$, i.e. the $\omega_n$ above; all other solutions can be expressed as powers of $\omega_n$.

???+ tip "Why does “the $n$-th root of unity” usually refer specifically to the first one?"
    Mainly for convenience in applications. All $n$-th roots of unity can be expressed as powers of the first $n$-th root of unity $\omega_n$; moreover, for any $k < n$, the complex number $\omega_n$ is not a $k$-th root of unity.

### Primitive roots of unity

In fact, $\omega_n$ is not the only $n$-th root of unity with this kind of property. The elements of the set

$$
\{\omega_n^k\mid 0\le k<n,~\gcd(n,k)=1\}
$$

are called **primitive $n$-th roots of unity**. From the expression above, there are $\varphi(n)$ primitive $n$-th roots of unity in total, where $\varphi(n)$ is [Euler's totient function](./number-theory/euler-totient.md).

Any primitive root of unity $\omega$ has the same property as the $\omega_n$ above: for any $0<k<n$, the $k$-th power of $\omega$ is not $1$, that is, $\omega$ is not a $k$-th root of unity. Therefore, all roots of unity can be generated from any primitive root of unity.

To understand the structure of the primitive $n$-th roots of unity, we need the following property of roots of unity:

???+ note "Property"
    For integers $n$ and $k$, let $d=\gcd(n,k)$; then $\omega_n^k = \omega_{n/d}^{k/d}$.

??? note "Proof"
    By direct computation,
    
    $$
    w_n^k = \exp\dfrac{2\pi k\mathrm{i}}{n} = \exp\dfrac{2\pi (k/d)\mathrm{i}}{n/d} = \omega_{n/d}^{k/d}.
    $$

This shows that whenever $\gcd(n,k)\neq 1$, $\omega_n^k$ is necessarily a (primitive) root of unity of order $\dfrac{n}{\gcd(n,k)}$. Hence a root of unity $\omega_n^k$ with the property above must satisfy $\gcd(n,k)=1$. This is exactly why primitive roots of unity are defined as above.

In addition, as a simple corollary of this analysis, we have:

???+ note "Theorem"
    As $k$ ranges over the divisors of $n$, the primitive $k$-th roots of unity form exactly a partition of the $n$-th roots of unity. Moreover, for $\ell\perp n$, the map $x\mapsto x^\ell$ is a bijection of the $n$-th roots of unity that preserves this partition: it still maps primitive roots of unity of order $k\mid n$ to primitive $k$-th roots of unity.

Although there are many choices of primitive root of unity, the first root $\omega_n$ has the simplest form, so $\omega_n$ remains the most commonly used in competitive programming. In some scenarios, to improve computational efficiency, a [primitive root of unity](./number-theory/residue.md#roots-of-unity) modulo some modulus may be used instead of $\omega_n$ in the complex field.

## Complex numbers in programming languages

### Complex numbers in C

The C99 standard provides the `<complex.h>` header.

The `<complex.h>` header provides three types: `double complex`, `float complex` and `long double complex`.

The arithmetic operators '+', '-', '\*' and '/' can be applied to any mix of floating-point and complex numbers. When one side of an expression is complex, the result is complex.

The `<complex.h>` header provides the imaginary unit `I`; when this header is included, the capital letter `I` cannot be used as a variable name.

For a single complex number, `<complex.h>` provides several operations: the `creal` function extracts the real part, `cimag` extracts the imaginary part, `cabs` computes the modulus, and `carg` computes the principal value of the argument.

Every function comes in three versions depending on the type. For example, the `creal` function has the versions `creal`, `crealf` and `creall`, handling the types `double`, `float` and `long double`, respectively. The version with no suffix handles `double`. All the functions below follow this rule, and we will not point it out again.

The return values of these functions are ordinary floating-point numbers. An ordinary floating-point number can be assigned directly to a complex number, but a complex number cannot be assigned directly to a floating-point number; the extraction operations above must be used instead.

The `conj` function computes the complex conjugate; its return value is a complex number.

The `cexp` function computes the complex exponential, `clog` the principal value of the logarithm, `csin` the sine, `ccos` the cosine, and `ctan` the tangent.

The `cpow` function computes the power function, `csqrt` the square root, `casin` the arcsine, `cacos` the arccosine, and `catan` the arctangent. All of these functions compute the principal values of multivalued functions.

### Complex numbers in C++

The `<ctype.h>` header of C becomes `<cctype>` in C++, and almost all headers follow this naming rule.

However, `<complex.h>` does not: C++ has no `<ccomplex>` header. Complex numbers in C++ are simply in `<complex>`, and its contents are completely different from those in C.

Interesting. The reason is that `<complex>` already existed in the first version of C++, C++98, whereas the C language only added it in C99.

In C++, complex types are defined as `complex<float>`, `complex<double>` and `complex<long double>`. Thanks to object-oriented polymorphism, the names of the functions below are unique, with no f or l suffix.

A complex number object has the member functions `real` and `imag`, which access the real and imaginary parts.

A complex number object has the non-member functions `real`, `imag`, `abs` and `arg`, which return the real part, the imaginary part, the modulus and the argument.

A complex number object also has the non-member functions `norm`, the square of the modulus, and `conj`, the complex conjugate.

A complex number object also has the non-member functions `exp`, `log` (principal value of the logarithm with base $\mathrm{e}$), `log10` (principal value of the logarithm with base 10, not available in C), `pow`, `sqrt`, `sin`, `cos` and `tan`, with the same meaning as in C.

Since C++14, the [literal operators `std::literals::complex_literals::""if, ""i, ""il`](https://en.cppreference.com/w/cpp/numeric/complex/operator%2522%2522i.html) are defined. For example, `100if`, `100i` and `100il` return `std::complex<float>{0.0f, 100.0f}`, `std::complex<double>{0.0, 100.0}` and `std::complex<long double>{0.0l, 100.0l}`, respectively. This lets us conveniently write complex number declarations like `auto z = 4.0 + 3i`.

## References and links

-   [Complex number - Wikipedia](https://en.wikipedia.org/wiki/Complex_number)
-   [Euler's formula - Wikipedia](https://en.wikipedia.org/wiki/Euler's_formula)
-   [Complex number arithmetic - cppreference.com](https://en.cppreference.com/w/c/numeric/complex)
-   [std::complex - cppreference.com](https://en.cppreference.com/w/cpp/numeric/complex)

[^ref1]: For more about Euler's formula, see two videos: [欧拉公式与初等群论 (Euler's formula and elementary group theory)](https://www.bilibili.com/video/BV1fx41187tZ) and [微分方程概论 - 第五章：在 3.14 分钟内理解 $\mathrm{e}^{\mathrm{i}\pi}$ (Introduction to differential equations – chapter 5: understanding $\mathrm{e}^{\mathrm{i}\pi}$ in 3.14 minutes)](https://www.bilibili.com/video/BV1G4411D7kZ).
