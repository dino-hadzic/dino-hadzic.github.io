---
title: Quadratic Fields
---

This article briefly introduces the concepts related to quadratic fields. Two important related examples are the Gaussian integers and the Eisenstein integers, which can be used to solve some number-theoretic problems.

## Basic Concepts

This section first introduces a series of basic concepts. Quadratic fields and quadratic integer rings are special cases of the more general concepts of algebraic field extensions and rings of algebraic integers, so almost all definitions and conclusions of this section can be appropriately generalized to the general case. The discussion in this section is restricted to the special case of quadratic fields, without introducing too much algebraic number theory.

### Quadratic Field

The elements of a quadratic field are quadratic algebraic numbers.

A **quadratic algebraic number** is a complex number that can be expressed as a solution of a quadratic equation with integer coefficients. By the quadratic formula, every quadratic algebraic number can be written in the form

$$
a+b\sqrt{d}
$$

where $a$ and $b$ are rational numbers and $d$ is a squarefree integer. Every number of this form is also a quadratic algebraic number. Quadratic algebraic numbers can be divided into rational numbers and **quadratic irrational numbers**. Clearly, the representation of a quadratic irrational number in the above form is unique.

For any squarefree integer $d\neq 0,1$, one can verify that the set $\mathbf Q(\sqrt{d})=\{a+b\sqrt{d}:a,b\in\mathbf Q\}$ is closed under addition, subtraction, multiplication and division. Since a set closed under the four arithmetic operations is called a [field](../algebra/basic.md#域), the set $\mathbf Q(\sqrt{d})$ is called a **quadratic field**. Every quadratic field contains all rational numbers, so they are all [quadratic extensions](../algebra/field-theory.md#域的扩张) of the field of rational numbers $\mathbf Q$. When $d>0$, all numbers in the quadratic field $\mathbf Q(\sqrt{d})$ are real, and $\mathbf Q(\sqrt{d})$ is called a real quadratic field. When $d<0$, no number in the quadratic field other than the rationals is real, and $\mathbf Q(\sqrt{d})$ is called an imaginary quadratic field.

### Conjugate and Norm

The **conjugate** of the quadratic irrational number $a+b\sqrt{d}$ is defined as $a-b\sqrt{d}$. Conjugate quadratic irrational numbers are the two distinct roots of the same quadratic equation with integer coefficients. In a real quadratic field, the conjugate of a quadratic irrational number does not coincide with its conjugate as a complex number; in an imaginary quadratic field, the conjugate of a quadratic irrational number is exactly its conjugate as a complex number. Finally, the conjugate of a rational number is defined to be itself. This defines the concept of conjugate for all quadratic algebraic numbers.

In any quadratic field, identities produced by the four arithmetic operations cannot distinguish conjugates. That is, replacing every number in an identity by its conjugate, i.e., changing the sign of every square root, the identity still holds.

Using conjugates, one can construct several maps from quadratic algebraic numbers to rational numbers, which turn discussions about quadratic algebraic numbers into discussions about rational numbers. The simpler one is the **trace** of a quadratic algebraic number $\alpha$, namely the sum of the number and its conjugate, denoted $\operatorname{tr}(\alpha)$. Since this is in fact just $2$ times its rational part, it does not provide much information.

More useful is the norm of a quadratic algebraic number. The product of a quadratic algebraic number and its conjugate is called its **norm**:

$$
N(a+b\sqrt{d})=a^2-db^2
$$

Clearly, in an imaginary quadratic field the concept of the norm coincides with the concept of the squared modulus of a complex number; in a real quadratic field, however, these two concepts do not coincide.

The norm has good properties. First, since $d$ is squarefree and thus cannot be a perfect square, only $0$ has norm $0$. Second, the norm preserves multiplication and division:

$$
N(a_1+b_1\sqrt{d})N(a_2+b_2\sqrt{d})=N((a_1+b_1\sqrt{d})(a_2+b_2\sqrt{d})),
$$

$$
\frac{N(a_1+b_1\sqrt{d})}{N(a_2+b_2\sqrt{d})}=N\left(\frac{a_1+b_1\sqrt{d}}{a_2+b_2\sqrt{d}}\right).
$$

Moreover, the reciprocal of a quadratic algebraic number is the ratio of its conjugate to its norm:

$$
\dfrac{1}{a+b\sqrt{d}}=\frac{a-b\sqrt{d}}{N(a+b\sqrt{d})}.
$$

By Vieta's formulas, the quadratic algebraic number $\alpha$ is in fact a root of the equation

$$
x^2-\operatorname{tr}(\alpha)x+N(\alpha)=0
$$

The discriminant of this equation is also called the **discriminant** of the quadratic algebraic number, denoted $\operatorname{disc}(\alpha)$, and its value is $4db^2$.

???+ note "Matrix representation"
    Similarly to complex numbers, quadratic algebraic numbers can also be represented by matrices. Let $d\neq 0,1$ be a squarefree integer and let $a,b$ be rational numbers; then $a+b\sqrt{d}$ can be represented by the matrix
    
    $$
    \begin{pmatrix}a & b \\ db & a\end{pmatrix}.
    $$
    
    One can verify that the results of addition, subtraction, multiplication and division of these matrices correspond to the results of the operations on quadratic algebraic numbers. The trace and determinant of the matrix correspond to the trace and norm of the quadratic algebraic number respectively, and the discriminant of the characteristic polynomial of the matrix is exactly the discriminant of the quadratic algebraic number. The adjugate matrix corresponds to the conjugate of the quadratic algebraic number.

### Quadratic Integer Ring

Among quadratic algebraic numbers, the quadratic integers are special. A **quadratic integer** is a complex number that can be expressed as a solution of a monic quadratic equation with integer coefficients. The only difference from quadratic algebraic numbers is the restriction on the leading coefficient. By the quadratic formula, the two roots of the quadratic equation $x^2+px+q=0$ are

$$
\frac{-p\pm\sqrt{p^2-4q}}{2}.
$$

If $p$ is even, i.e., $p=2k$, the two roots can be written as $-k\pm\sqrt{k^2-q}$; if $p$ is odd, i.e., $p=2k+1$, the two roots can be written as $-k-\dfrac{1\pm\sqrt{4(k^2+k-q)+1}}{2}$. From these two cases one concludes that the quadratic integers in $\mathbf Q(\sqrt{d})$ can necessarily be written in the form

$$
a+b\omega
$$

where $a$ and $b$ are integers, and

$$
\omega=\begin{cases}
\dfrac{1+\sqrt{d}}{2}, & d\equiv 1\pmod 4,\\
\sqrt{d}, & d\equiv 2,3\pmod 4.
\end{cases}
$$

Conversely, every complex number of this form is a quadratic integer. Every non-rational quadratic integer has a unique representation in this form.

The set of all quadratic integers in the quadratic field $\mathbf Q(\sqrt{d})$ is denoted $\mathbf Z[\omega]$. Since this set is closed under addition, subtraction and multiplication, it is also called a **quadratic integer ring**. The rational numbers in a quadratic integer ring are exactly all the integers. Considering the set of all ratios of quadratic integers in $\mathbf Z[\omega]$, one obtains the corresponding quadratic field $\mathbf Q(\sqrt{d})$.

The trace, norm and discriminant of a quadratic integer are all integers. The discriminant with the smallest absolute value among the discriminants of all quadratic irrational numbers in the quadratic integer ring $\mathbf Z[\omega]$ is also called the discriminant of the corresponding quadratic field $\mathbf Q(\sqrt{d})$. When $d\equiv 1\pmod 4$, the discriminant is $d$; when $d\equiv 2,3\pmod 4$, the discriminant is $4d$.

### Divisibility, Associates and Units

Similarly to the integers, a theory of divisibility can be built for quadratic integers as well. Of course, the discussion must take place within the same quadratic integer ring.

For quadratic integers $\alpha$ and $\beta$ in the quadratic integer ring $\mathbf Z[\omega]$, if there exists a quadratic integer $\gamma$ in the same ring such that $\beta=\alpha\gamma$, we say that $\alpha$ divides $\beta$, written $\alpha\mid\beta$. The divisibility relation is a [preorder](../order-theory.md#二元关系) on the quadratic integer ring. If both $\alpha\mid\beta$ and $\beta\mid\alpha$ hold, then $\alpha$ and $\beta$ can be regarded as the same number when studying divisibility; they are called **associates**. The associate relation is an equivalence relation on the quadratic integer ring.

In analogy with the divisibility theory of the integers, being associates corresponds to being negatives of each other. Divisibility theory usually only needs to consider the natural numbers, without examining the case of negative numbers. For quadratic integers, the associate relation may be somewhat more complicated. If the quadratic integers $\alpha$ and $\beta$ are associates, then there exist quadratic integers $\gamma$ and $\delta$ such that $\beta=\alpha\gamma$ and $\alpha=\beta\delta$. Therefore the ratio $\gamma$ of $\beta$ to $\alpha$ must be a special quadratic integer, namely one for which there exists a quadratic integer $\delta$ with $\gamma\delta=1$. Such a quadratic integer $\gamma$ is called a **unit**, also known as an invertible element. Two quadratic integers are associates if and only if their ratio is a unit. Therefore, to understand the associate relation on a quadratic integer ring, one has to understand the structure of its units.

Since the norm preserves multiplication and the norm of a quadratic integer is always an integer, the norm can be used to turn the divisibility relation of quadratic integers into the divisibility relation of integers. That is, if $\alpha\mid\beta$, then necessarily $N(\alpha)\mid N(\beta)$. Likewise, a quadratic integer $\alpha$ is a unit if and only if its norm $N(\alpha)=\pm 1$. Therefore, to obtain all units of the quadratic integer ring $\mathbf Z[\omega]$, it suffices to solve the Diophantine equation:

$$
N(a+b\omega)=\pm 1,
$$

where the expression for the norm is

$$
N(a+b\omega)=\begin{cases}
a^2+ab+\dfrac{1-d}{4}b^2, & d\equiv 1\pmod 4,\\
a^2-db^2, & d\equiv 2,3\pmod 4.
\end{cases}
$$

For imaginary quadratic integer rings, i.e., when $d<0$, since the norm is necessarily a nonnegative integer, it is easy to verify that for all squarefree negative $d\neq -1,-3$ the only solutions are $(a,b)=(\pm 1,0)$; that is, except for $\mathbf Z[\sqrt{-1}]$ and $\mathbf Z[\frac{1+\sqrt{-3}}{2}]$, the units of imaginary quadratic integer rings are only $\pm 1$. Writing $\mathrm{i}=\sqrt{-1}$, the quadratic integer ring $\mathbf Z[\mathrm{i}]$ is also called the ring of Gaussian integers, and its set of units is $\{\pm 1,\pm\mathrm{i}\}$. Writing $\omega=\frac{1+\sqrt{-3}}{2}$, the quadratic integer ring $\mathbf Z[\omega]$ is also called the ring of Eisenstein integers, and its set of units is $\{\pm 1,\pm\omega,\pm\omega^2\}$.

For real quadratic integer rings, i.e., when $d>0$, the situation is more complicated and can be reduced to the discussion of the corresponding [Pell's equation](./pell-equation.md). From the results on Pell's equation, the set of all units in this case can be written as $\{\pm u^k:k\in\mathbf Z\}$, where $u$ is called the **fundamental unit**. The fundamental unit can be found by solving the corresponding Pell's equation. The fundamental unit is not unique: if $u$ is a fundamental unit, then its conjugate $\bar u$ as well as $-u$ and $-\bar u$ are fundamental units too.

The structure of the units of quadratic integer rings generalizes to general [rings of algebraic integers](../algebra/field-theory.md#代数扩张). [Dirichlet's unit theorem](https://en.wikipedia.org/wiki/Dirichlet%27s_unit_theorem) in algebraic number theory states that the units of any ring of algebraic integers form a [finitely generated abelian group](../algebra/group-theory.md#有限生成-abel-群), and the theorem also gives the rank of this group.

The greatest common divisor, division with remainder, Bézout's theorem, the unique factorization theorem and other contents of the divisibility theory of the integers can be generalized to some or all quadratic integer rings. Whether such a generalization is possible in a given quadratic integer ring actually reflects whether the properties of that ring are close enough to those of the ring of integers. The unique factorization theorem does not hold in every quadratic integer ring; among the quadratic integer rings in which the unique factorization theorem holds, only some admit division with remainder. For a discussion of these topics, refer to the section [Quadratic integer rings](../algebra/ring-theory.md#例子二次整数环) in the ring theory part, or to related books.

### Unique Factorization

If the unique factorization theorem for the integers can be generalized to a quadratic integer ring, it should have the following form: every quadratic integer in the ring $\mathbf Z[\omega]$ can be written as a product of several irreducible elements, and this factorization is unique up to associates and order. Here an [irreducible element](../algebra/ring-theory.md#整除关系) is a quadratic integer that cannot be further factored into a product of non-units, analogous to the primes in the unique factorization theorem for the integers. As mentioned above, the unique factorization theorem does not hold in every quadratic integer ring.

For example, in $\mathbf Z[\sqrt{-5}]$ there is the factorization $9=3\times 3=(2+\sqrt{-5})\times(2-\sqrt{-5})$, but $3$ and $2\pm\sqrt{-5}$ are already irreducible elements, so the factorization is not unique. To show that these three numbers are all irreducible, one can examine their norms: their norms are all $9$, so if they could be factored into a product of non-units, the norms of the resulting factors could only be $3$, but there is no quadratic integer of norm $3$ in $\mathbf Z[\sqrt{-5}]$.

The main reason why the unique factorization theorem fails in a general quadratic integer ring is that factorization using only quadratic integers is not fine enough. For example, if one wants to factor the product $abcd$ but the available basic elements are only $\{ab,cd,ac,bd\}$, the resulting factorization is naturally not unique; to obtain a unique factorization theorem one must further consider $\{a,b,c,d\}$. In a quadratic integer ring, the structure finer than quadratic integers is the [ideals](../algebra/ring-theory.md#理想) of the quadratic integer ring; mapping a quadratic integer to its corresponding principal ideal embeds its associate class into the set of ideals, so the factorization of numbers is only a special case of the factorization of ideals. Considering the factorization of ideals in a quadratic integer ring, one can prove that the ideals of every quadratic integer ring factor uniquely into a product of several prime ideals. This says that all quadratic integer rings are [Dedekind domains](https://en.wikipedia.org/wiki/Dedekind_domain). More generally, all rings of algebraic integers are Dedekind domains.

If the unique factorization theorem holds in a quadratic integer ring, then its prime ideals and irreducible elements (equivalence classes up to associates) are in one-to-one correspondence, so for this class of quadratic integer rings, factoring ideals into prime ideals is equivalent to factoring quadratic integers into irreducible elements. Moreover, in this case the irreducible elements are also called [prime elements](../algebra/ring-theory.md#整除关系), corresponding to the concept of primes among the integers. The following discussion uses prime ideals and related concepts; readers unfamiliar with this concept can replace them word for word by prime elements, and the statements remain correct in the case where the unique factorization theorem holds.

To fully understand unique factorization in a general quadratic integer ring $\mathbf Z[\omega]$, one needs to know what the prime ideals of $\mathbf Z[\omega]$ are. First, every prime ideal of $\mathbf Z[\omega]$ divides (the principal ideal of) its norm. Factoring its norm within the integers into a product of several primes, by the unique factorization theorem the prime ideal necessarily divides (the principal ideal of) one of these prime factors. Therefore the prime ideals of $\mathbf Z[\omega]$ are necessarily obtained by further factoring the primes of the integers. To list all prime ideals of $\mathbf Z[\omega]$, it suffices to give the unique factorization in $\mathbf Z[\omega]$ of (the principal ideal of) each prime $p$ of $\mathbf Z$. Since the norm of (the principal ideal of) the prime $p$ in $\mathbf Z[\omega]$ is $p^2$, and its factorization into prime ideals means that the norms of those prime ideals must be divisors of $p^2$, they can only be $p$ or $p^2$. This shows that there are only the following three possibilities:

1.  $p$ is **inert** in $\mathbf Z[\omega]$, i.e., $(p)$ is still a prime ideal in $\mathbf Z[\omega]$;
2.  $p$ **splits** in $\mathbf Z[\omega]$, i.e., $(p)$ can be written in $\mathbf Z[\omega]$ as a product of two distinct conjugate prime ideals;
3.  $p$ **ramifies** in $\mathbf Z[\omega]$, i.e., $(p)$ can be written in $\mathbf Z[\omega]$ as the square of some prime ideal.

It can further be proved that to decide which of the three cases a prime $p$ falls into, it suffices to compute the [Kronecker symbol](https://en.wikipedia.org/wiki/Kronecker_symbol) $\left(\dfrac{D}{p}\right)$ for the discriminant $D$ of the quadratic field containing $\mathbf Z[\omega]$ and the prime $p$. The three cases correspond respectively to the three values of the Kronecker symbol: $-1$, $+1$ and $0$. When $p$ is an odd prime, the Kronecker symbol is the [Legendre symbol](./quad-residue.md#legendre-符号), and the three cases correspond respectively to $D$ being a [quadratic non-residue](./quad-residue.md) modulo $p$, $D$ being a [quadratic residue](./quad-residue.md) modulo $p$, and $p$ dividing $D$. When $p=2$, the three cases correspond respectively to $D\equiv \pm 3\pmod 8$, $D\equiv \pm 1\pmod 8$, and $2$ dividing $D$.

## Gaussian Integers

In this section, let $\mathrm{i}=\sqrt{-1}$ denote the imaginary unit. The quadratic field $\mathbf Q(\mathrm{i})$ is also called the Gaussian field; it is also the fourth [cyclotomic field](../algebra/field-theory.md#分圆域). The corresponding quadratic integer ring $\mathbf Z[\mathrm{i}]$ is also called the ring of Gaussian integers, and its elements are called **Gaussian integers**. The Gaussian integers have four units in total, namely $\pm 1$ and $\pm\mathrm{i}$, so every nonzero Gaussian integer has four associates (including itself). In the complex plane, the Gaussian integers represent all the lattice points, and the norm $N(a+b\mathrm{i})=a^2+b^2$ of a Gaussian integer is exactly the norm in the complex plane.

![](./images/gaussian-integer.svg)

Division with remainder can be performed on the Gaussian integers: for Gaussian integers $a$ and $b\neq 0$, there always exist Gaussian integers $q$ and $r$ such that $a=bq+r$ and $N(r)<N(b)$. To compute such a division with remainder, one can first compute $\dfrac{a}{b}$ in $\mathbf Q(\mathrm{i})$, then find the nearest lattice point in the complex plane as $q$, and then compute $r=a-bq$; the remainder obtained this way always satisfies $N(r)\le\dfrac{1}{2}N(b)$. Using division with remainder, the Euclidean algorithm, Bézout's theorem and so on can be carried over to the Gaussian integers, and the unique factorization theorem can then be established.

### Gaussian Primes

Using the conclusions of the previous section, one can find the prime elements among the Gaussian integers (also called Gaussian primes). Since the discriminant of the ring of Gaussian integers is $-4$, and the Kronecker symbol $\left(\dfrac{-4}{n}\right)$ takes the value $0$ for even $n$ and the value $\left(\dfrac{-1}{n}\right)=(-1)^{(n-1)/2}$ for odd $n$, we have

$$
\left(\dfrac{-4}{n}\right) = \begin{cases}
+1,& n\equiv 1\pmod 4,\\
-1,& n\equiv 3\pmod 4,\\
0,& 2\mid n.
\end{cases}
$$

Therefore there are three kinds of Gaussian primes in total:

1.  the primes of the form $4k+3$ among the integers;
2.  the two conjugate Gaussian prime factors of a prime of the form $4k+1$ among the integers;
3.  the factor $1+\mathrm{i}$ of the prime $2$, whose conjugate is an associate of it.

For example, in $\mathbf Z[\mathrm{i}]$ there is the factorization $60=2^2\times 3\times 5=-(1+\mathrm{i})^4\times 3\times(2+\mathrm{i})\times(2-\mathrm{i})$.

The discussion here of whether a prime $p$ can be further factored in $\mathbf Z[\mathrm{i}]$ is in fact equivalent to the discussion of whether the prime $p$ can be written as a sum of integer squares $a^2+b^2$. Therefore, from the conclusion here one deduces that a prime $p$ can be written as a sum of two squares if and only if $p=2$ or $p\equiv 1\pmod 4$. This is [Fermat's theorem on sums of two squares](https://en.wikipedia.org/wiki/Fermat%27s_theorem_on_sums_of_two_squares).

### Lattice Points on a Circle

In the complex plane, the Gaussian integers represent all the lattice points. The norm of a Gaussian integer is the square of the Euclidean distance from the lattice point to the origin. Therefore, quadratic integers with the same norm correspond to lattice points on a circle centered at the origin of the complex plane. In other words, the number of lattice points on the circle $x^2+y^2=n$ equals the number of Gaussian integers $x+y\mathrm{i}$ with norm $n$.

To solve the equation $N(x+y\mathrm{i})=n$, one can consider the factorization of the Gaussian integer $x+y\mathrm{i}$ into prime factors; the product of the norms of these prime factors equals $n$. Therefore, once the factorization of $n$ is known, the possible prime factors of $x+y\mathrm{i}$ can be determined from the prime factors of $n$. Let the prime factorization of the integer $n$ be

$$
n=2^kp_1^{r_1}\cdots p_\ell^{r_\ell}q_1^{s_1}\cdots q_{m}^{s_m},
$$

where $p_1,\cdots,p_\ell$ are the prime factors of the form $4k+1$ and $q_1,\cdots,q_m$ are the prime factors of the form $4k+3$.

First, the equation $N(x+y\mathrm{i})=n$ has a solution if and only if the exponents $s_1,\cdots,s_m$ of the prime factors of the form $4k+3$ of $n$ are all even; this is because $q_1,\cdots,q_m$ are also Gaussian primes whose norms equal their own squares, so in the prime factorization of the norm they necessarily appear in pairs.

Now suppose the equation has a solution. Then a solution of the equation necessarily has the form

$$
u(1+\mathrm{i})^k(a_1+b_1\mathrm{i})^{r_{1}^+}(a_1-b_1\mathrm{i})^{r_{1}^-}\cdots(a_\ell+ b_\ell\mathrm{i})^{r_\ell^+}(a_\ell-b_\ell\mathrm{i})^{r_\ell^-}q_1^{s_1/2}\cdots q_{m}^{s_m/2},
$$

where $u$ is a unit, $a_j\pm b_j\mathrm{i}$ are the conjugate prime factors of $p_j$ in the ring of Gaussian integers, and $r_j^++r_j^-=r_j$. Therefore the number of solutions of the equation equals

$$
4(1+r_1)\cdots(1+r_\ell).
$$

Let $f(n)$ denote the number of integer solutions of the equation $x^2+y^2=n$. When it has a solution, $f(n)$ is given by the above expression; otherwise, $f(n)=0$. It is easy to verify that $\dfrac14f(n)$ is a [multiplicative function](./basic.md#积性函数). The values of a multiplicative function are determined by its values at prime powers. From the expression for $f(n)$ one can determine that the values of $\dfrac14f(n)$ at prime powers $p^k$ are as follows:

1.  if $p$ is a prime of the form $4k+3$, then $\dfrac14f(1)=1,\dfrac14f(p)=0,\dfrac14f(p^2)=1,\dfrac14f(p^3)=0,\cdots$;
2.  if $p$ is a prime of the form $4k+1$, then $\dfrac14f(p^k)=k+1$;
3.  if $p=2$, then $\dfrac14f(2^k)=1$.

It is easy to verify that all three cases can be written as

$$
\dfrac14f(p^k) = \sum_{j=0}^k\left(\dfrac{-4}{p}\right)^j = \sum_{j=0}^k\left(\dfrac{-4}{p^j}\right) = \sum_{d\mid p^k}\left(\dfrac{-4}{d}\right).
$$

Since the Kronecker symbol $\left(\dfrac{-4}{n}\right)$ is a completely multiplicative function, we obtain

$$
f(n) = 4\sum_{d\mid n}\left(\dfrac{-4}{d}\right)=4\sum_{d\mid n}\chi_{4,3}(d).
$$

The notation in the rightmost sum uses the fact that the Kronecker symbol $\left(\dfrac{-4}{n}\right)$ is the real [Dirichlet character](https://en.wikipedia.org/wiki/Dirichlet_character) modulo $4$.

### Pythagorean Equation

Using Gaussian integers, one can find the general solution of the Pythagorean equation. The Pythagorean equation is the following quadratic Diophantine equation:

$$
x^2+y^2=z^2.
$$

Comparing with the content of the previous section, this amounts to solving the equation $N(x+y\mathrm{i})=z^2$. Let $z$ have the prime factorization in $\mathbf Z$

$$
z=2^kp_1^{r_1}\cdots p_\ell^{r_\ell}q_1^{s_1}\cdots q_{m}^{s_m},
$$

so that its solution $x+y\mathrm{i}$ has the prime factorization in $\mathbf Z[\mathrm{i}]$

$$
x+y\mathrm{i} = u(1+\mathrm{i})^{2k}(a_1+b_1\mathrm{i})^{r_{1}^+}(a_1-b_1\mathrm{i})^{r_{1}^-}\cdots(a_\ell+ b_\ell\mathrm{i})^{r_\ell^+}(a_\ell-b_\ell\mathrm{i})^{r_\ell^-}q_1^{s_1}\cdots q_{m}^{s_m}
$$

with $r_j^++r_j^-=2r_j$. One can compute the greatest common divisor of $x+y\mathrm{i}$ and $z$, obtaining the following integer:

$$
\kappa = 2^kp_1^{\min\{r_1^+,r_1^-\}}\cdots p_\ell^{\min\{r_\ell^+,r_\ell^-\}}q_1^{s_1}\cdots q_m^{s_m}.
$$

Removing this common factor, $\kappa^{-1}(x+y\mathrm{i})$ contains only prime factors of the form $a_j\pm b_j\mathrm{i}$, conjugate factors do not appear in pairs, and the exponents $|r_j^+-r_j^-|$ of these factors are necessarily even (since their sum $2r_j$ is even). Therefore $\kappa^{-1}(x+y\mathrm{i})$ is the square of some quadratic integer $u+v\mathrm{i}$. From this we obtain the following equations:

$$
x+y\mathrm{i} = \kappa(u+v\mathrm{i})^2,\ z=\kappa N(u+v\mathrm{i}).
$$

Within the integers $\mathbf Z$, this amounts to the following system of equations:

$$
x = \kappa(u^2-v^2),\ y = 2\kappa uv,\ z = \kappa(u^2+v^2).
$$

Conversely, for any integers $u$ and $v$, the $(x,y,z)$ given by the above expressions satisfies the Pythagorean equation. Therefore this is the general solution of the Pythagorean equation.

From the process above, one sees that in a primitive Pythagorean triple $(x,y,z)$ (i.e., one where the common divisor of $x,y,z$ is one), one of $x,y$ is necessarily odd and the other even, and $z$ is odd and contains only prime factors of the form $4k+1$.

A similar method can also be used to obtain the general solution of the equation $x^2+y^2=z^3$, or to prove that the equation $x^4+y^4=z^4$ has no solution. Of course, using the general solution of the Pythagorean equation and the method of infinite descent, one can prove the stronger statement that the equation $x^4+y^4=z^2$ has no solution.

## Eisenstein Integers

In this section, let $\omega=\dfrac{-1+\sqrt{3}\mathrm{i}}{2}=e^{2\pi\mathrm{i}/3}$.[^omega] The quadratic field $\mathbf Q(\sqrt{3}\mathrm{i})$ is the third and sixth [cyclotomic field](../algebra/field-theory.md#分圆域), and the algebraic integers in it are called Eisenstein integers. The ring $\mathbf Z[\omega]$ formed by all Eisenstein integers is called the ring of Eisenstein integers. The ring of Eisenstein integers has six units in total, namely $\pm 1$, $\pm\omega$ and $\pm\omega^2$. In the complex plane, all Eisenstein integers form a triangular lattice. Unlike the Gaussian integers, the lattice points here are generally not integer points.

![](./images/eisenstein-integer.svg)

The norm of an Eisenstein integer is

$$
N(a+b\omega) = a^2-ab+b^2,
$$

which is also the square of the distance from the above lattice point in the complex plane to the origin.

Eisenstein integers are also very similar to Gaussian integers. On the Eisenstein integers one can likewise use the norm $N(\cdot)$ to define division with remainder, and establish the Euclidean algorithm, Bézout's theorem, the unique factorization theorem and other results. Similarly to the above, one can derive the factors of primes in the ring of Eisenstein integers. For this, note that the discriminant of $\mathbf Z[\omega]$ is $-3$, and the Kronecker symbol is

$$
\left(\dfrac{-3}{n}\right) = \begin{cases}
+1, & n\equiv 1\pmod 3,\\
-1, & n\equiv 2\pmod 3,\\
0,  & 3\mid n,
\end{cases}
$$

so the prime elements in the ring of Eisenstein integers, i.e., the Eisenstein primes, come in the following three kinds:

1.  the primes of the form $3k+2$ among the integers, i.e., $2$ and the primes of the form $6k+5$;
2.  the two conjugate Eisenstein prime factors of a prime of the form $3k+1$ (that is, a prime of the form $6k+1$) among the integers;
3.  the factor $(3+\sqrt{3}\mathrm{i})/2$ of the prime $3$, whose conjugate is an associate of it.

Using the method of the previous section, one can find the number of Eisenstein integers with norm $n$. Let this number be $f(n)$; then it equals

$$
f(n)=6\sum_{d\mid n}\left(\dfrac{-3}{d}\right)=6\sum_{d\mid n}\chi_{3,2}(d). 
$$

Here $\chi_{3,2}(n)=\left(\dfrac{-3}{n}\right)$ is the real Dirichlet character modulo $3$. This expression shows that such an Eisenstein integer exists if and only if the exponents of all prime factors of the form $3k+2$ of $n$ are even.

By the norm formula above, $f(n)$ is also the number of integer solutions of the Diophantine equation $x^2-xy+y^2=n$ or of the Diophantine equation $x^2+xy+y^2=n$. Its geometric meaning is the number of lattice points on the tilted ellipse $x^2\pm xy+y^2=n$.

Closely related to these equations is another Diophantine equation, $x^2+3y^2=n$, whose integer solutions correspond to lattice points on an ellipse in standard position. The change of variables $x=(u+v)/2$ and $y=(u-v)/2$ transforms it into the already solved equation $u^2-uv+v^2=n$. However, although integer solutions of $x^2+3y^2=n$ always correspond to integer solutions of $u^2-uv+v^2=n$, the converse is not necessarily true. If $n$ is even, then $u$ and $v$ are necessarily both even, which means that $x$ and $y$ are necessarily integers, and the number of integer solutions of $x^2+3y^2=n$ is still $f(n)$. However, if $n$ is odd, then $u$ and $v$ may be one odd and one even, or both odd, so the corresponding $x$ and $y$ may be both half-integers or both integers. This case requires a more careful discussion.

When one integer solution $(u,v)$ of the equation $u^2-uv+v^2=n$ is known, the integer solutions corresponding to the Eisenstein integers that are associates of $u+v\omega$ (including itself) are respectively

$$
(u,v),(u-v,u),(-v,u-v),(-u,-v),(v-u,-u),(v,v-u).
$$

Since the three integers $u,v,u-v$, as long as they are not all even, necessarily consist of two odd numbers and one even number, among these six integer solutions exactly two consist entirely of odd numbers and four consist of one odd and one even number. This shows that when $n$ is odd, only $\dfrac13$ of the integer solutions of the equation $u^2-uv+v^2=n$ consist entirely of odd numbers, and only then can they correspond to integer solutions of $x^2+3y^2=n$. Hence, when $n$ is odd, the number of integer solutions of $x^2+3y^2=n$ is $\dfrac13f(n)$.

Finally, similarly to the method of solving the Pythagorean equation, Eisenstein integers can be used to solve the following Diophantine equations:

$$
x^2-xy+y^2=z^2
$$

$$
x^2+xy+y^2=z^2
$$

$$
x^2+3y^2=z^2
$$

$$
x^2+3y^2=z^3
$$

Their general solutions are not repeated here. A similar method can also be used to prove that $x^3+y^3=z^3$ has no solution.

## References and Notes

-   [Quadratic field - Wikipedia](https://en.wikipedia.org/wiki/Quadratic_field)
-   [Quadratic integer - Wikipedia](https://en.wikipedia.org/wiki/Quadratic_integer)
-   [Gaussian integer - Wikipedia](https://en.wikipedia.org/wiki/Gaussian_integer)
-   [Eisenstein integer - Wikipedia](https://en.wikipedia.org/wiki/Eisenstein_integer)
-   [Kronecker symbol - Wolfram MathWorld](https://mathworld.wolfram.com/KroneckerSymbol.html)
-   [Dirichlet character - Wikipedia](https://en.wikipedia.org/wiki/Dirichlet_character)
-   [Theodorus J. Dekker's Notes on Primes in Quadratic Fields](https://staff.science.uva.nl/t.j.dekker/PrimesPaper/Primes.pdf)
-   [Franz Lemmermeyer's Notes on Ideals in Quadratic Number Fields](http://www.fen.bilkent.edu.tr/~franz/ant/ant02.pdf)
-   [J.S. Milne - Algebraic Number Theory](https://www.jmilne.org/math/CourseNotes/ANT301.pdf)

[^omega]: Note that the choice of $\omega$ here differs from the choice above. By convention, when discussing general quadratic integer rings one usually sets $\omega=(1+\sqrt{d})/2$ (when $d\equiv 1\pmod4$), whereas for the ring of Eisenstein integers one often sets $\omega=(-1+\sqrt{-3})/2$. This difference has no substantial effect, but it may change the form of some expressions. Note that the ring of Eisenstein integers should not be written as $\mathbf Z[\sqrt{-3}]$.
