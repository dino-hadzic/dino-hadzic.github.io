---
title: Field Theory
---

Prerequisites: [Basic concepts of abstract algebra](./basic.md), [Group theory](./group-theory.md), [Ring theory](./ring-theory.md)

## Introduction

**Field theory** is the theory of fields.

The field theory covered in this article is mainly the theory of field extensions. A field is an algebraic structure closed under addition, subtraction, multiplication, and division; in algorithm competitions one often computes modulo a prime $p$, which amounts to computing in the finite field $\mathbf F_p$. Similarly to the case of the field of real numbers $\mathbf R$, some problems are more conveniently solved by computing in a larger field (namely the field of complex numbers $\mathbf C$); a common example is speeding up the multiplication of polynomials with real coefficients using the [fast Fourier transform](../poly/fft.md). The same can be done for finite fields. Most readers are relatively unfamiliar with extensions of finite fields, so it is worthwhile to learn the general theory of extensions of fields. At the end of the article we give some algorithmic applications that require extending a finite field, and we also briefly discuss extensions of the ring of integers that may be needed in some of these applications.

Closely related to field theory is Galois theory. It connects extensions of a field with their automorphism groups, so that the properties of field extensions can be understood with the tools of group theory. Although this theory is often the core content of the corresponding algebra courses, it is far removed from the content of algorithm competitions, so this article does not cover it in depth. Interested readers should consult specialized textbooks.

???+ info "Notation"
    When no ambiguity arises, this article may omit the multiplication sign in rings and fields, and writes the ring $(R,+,\cdot)$ as the ring $R$ and the field $(F,+,\cdot)$ as the field $F$. The additive identity of a ring or field is called the zero, and the multiplicative identity is called the unity. Moreover, in this article $p$ always denotes a prime, and $q$ always denotes a prime power, which can be written as $p^n$, where $n$ is a positive integer.

## Field extensions

As in the case of groups and rings, the notions of subfield and field homomorphism can be introduced.

???+ abstract "Subfield"
    If a subring $E$ of a field $F$ is also a field, then $E$ is called a **subfield** of the field $F$.

Here, regardless of how the definitions of ring and subring treat the unity, a subfield $E$ necessarily contains the unity of the field $F$[^subfield-one].

???+ abstract "Field homomorphism"
    A ring homomorphism $\varphi:F\rightarrow E$ from a field $F$ to a field $E$ is also called a **field homomorphism** from the field $F$ to the field $E$.

??? info "How field homomorphisms treat the unity"
    If, unlike the definition in this article, ring homomorphisms are required to map the unity to the unity, then field homomorphisms naturally also map the unity to the unity. Otherwise, the unity may also be mapped to the zero.

Since a field has only trivial ideals, a field homomorphism either maps the whole field to zero or is necessarily an embedding. This shows that the discussion of field homomorphisms can be reduced to the discussion of subfields.

In the case of fields, the smaller field is usually the more familiar one, so one usually takes the subfield as the starting point for studying the larger field. This is the notion of a field extension.

???+ abstract "Field extension"
    For a field $F$, if $F$ is a subfield of $E$, then the field $E$ is called an **extension** of the field $F$, or an **extension field**, written $E/F$.

???+ info "Notation for field extensions"
    Although the notation looks the same, the notion of a field extension has nothing to do with quotient rings, and the two should not be confused.

???+ example "Example"
    The field of complex numbers $\mathbf C$ is an extension of the field of real numbers $\mathbf R$, and the field of real numbers $\mathbf R$ is in turn an extension of the field of rational numbers $\mathbf Q$.

### Degree of a field extension

For a field extension $E/F$, the field $E$ is always a [vector space](../linear-algebra/vector-space.md) over the field $F$. The dimension of this vector space is the degree of the field extension.

???+ abstract "Degree of a field extension"
    The **degree** of a field extension $E/F$ is the dimension of $E$ regarded as a vector space over the field $F$, i.e. $\dim_F(E)$, and is denoted $[E:F]$. If the degree of the field extension is finite, the extension is called a **finite extension**; otherwise it is called an **infinite extension**.

???+ example "Example"
    The degree $[\mathbf C:\mathbf R]$ of the field extension $\mathbf C/\mathbf R$ equals $2$, so it is a finite extension. The field extension $\mathbf R/\mathbf Q$ is an infinite extension.

Degrees of field extensions are multiplicative.

???+ note "Theorem"
    Let $F\subseteq K\subseteq E$ be fields. Then the degrees of the extensions between them satisfy $[E:F]=[E:K][K:F]$.

??? note "Proof"
    When the degree of the extension is infinite, this is obvious; otherwise, if $\{\alpha_i\}$ is a basis of $E$ as a vector space over $K$ and $\{\beta_j\}$ is a basis of $K$ as a vector space over $F$, one can verify that $\{\alpha_i\beta_j\}$ is a basis of $E$ as a vector space over $F$.

This article mainly deals with finite extensions of fields.

### Characteristic of a field

The study of field extensions has a natural starting point: the smallest subfield containing the unity of the field $F$. This field is also called the **prime subfield** of the field $F$.

The structure of the prime subfield is uniquely determined by the properties of the unity of the field. The characteristic of the field summarizes exactly these properties.

???+ abstract "Characteristic of a field"
    The **characteristic** of a field $F$ is the smallest positive integer $n$ such that $n\cdot 1=0$; if no such $n$ exists, the characteristic of the field $F$ is said to be $0$. Here $n\cdot 1$ denotes the sum of $n$ copies of the unity $1$. If the characteristic of the field $F$ is not $0$, the field $F$ is said to have **finite characteristic**.

The characteristic of a field can be understood through ring homomorphisms. The ring of integers $\mathbf Z$ is the closed structure obtained from $0$ and $1$ by repeatedly applying addition, subtraction, and multiplication. It can be regarded as a kind of "prototype": every ring with unity should "inherit" part of the structure of the ring of integers[^initial-object-ring]. Therefore, for a field $F$, one can consider a ring homomorphism $\varphi:\mathbf Z\rightarrow F$ and require $\varphi(1)=1$. Such a ring homomorphism is uniquely determined: it maps $n\in\mathbf N_+$ to $n\cdot 1$, i.e. the sum of $n$ copies of the unity $1$. The image $\varphi(\mathbf Z)$ of this homomorphism is embedded in the field $F$, so it necessarily has a unity, is commutative, and has no zero divisors; hence it is an integral domain. Therefore the kernel $\ker\varphi$ of the homomorphism is necessarily a prime ideal. The prime ideals of the ring of integers $\mathbf Z$ can only be of the form $(n)$, where $n=0$ or $n$ is a prime. The $n$ obtained in this way is exactly the characteristic of the field.

The characteristic of a field determines the structure of its prime subfield:

1.  When the characteristic is $0$, the homomorphism $\varphi$ is injective, and the ring of integers $\mathbf Z$ is embedded in the field $F$. The field of rational numbers $\mathbf Q$, being the smallest field containing the ring of integers, can necessarily also be embedded in the field $F$, and it is the prime subfield of the field $F$;
2.  When the characteristic is a prime $p$, the image $\mathbf Z/p\mathbf Z$ of the homomorphism $\varphi$ is embedded in the field $F$. In this case $\mathbf Z/p\mathbf Z$ is already a field, denoted $\mathbf F_p$, and it is the prime subfield of the field $F$.

This discussion actually proves the following result:

???+ note "Theorem"
    The characteristic of a field $F$ can only be $0$ or a prime $p$. The prime subfield of a field of characteristic $0$ is $\mathbf Q$, and the prime subfield of a field of characteristic $p$ is $\mathbf F_p$.

The fields $\mathbf Q$ and $\mathbf F_p$ in the theorem are also called **prime fields**, i.e. fields whose only subfield is the field itself. A finite field necessarily has finite characteristic, since a field of characteristic $0$ contains at least the subfield $\mathbf Q$.

Fields of finite characteristic and fields of characteristic zero often have different properties. For example, fields of finite characteristic have the following properties:

???+ note "Theorem"
    Let the characteristic of $F$ be $p$. Then:
    
    1.  In the additive group of the field $F$, all nonzero elements have order $p$, i.e. $px=0$ for all $x\in F$;
    2.  The "freshman's dream" holds, i.e. $(x+y)^p=x^p+y^p$ for all $x,y\in F$. Moreover, the map $x\mapsto x^p$ is an injective endomorphism of $F$, called the **Frobenius endomorphism**.

??? note "Proof"
    For the first property, it suffices to note that $px=(p1)x=0x=0$. For the second property, it suffices to note that in the binomial expansion of $(x+y)^p$, the coefficients of all terms other than $x^p$ and $y^p$ are multiples of $p$, so by the first property $(x+y)^p=x^p+y^p$. To verify that $x\mapsto x^p$ is an endomorphism, it remains to verify $(xy)^p=x^py^p$, which holds because multiplication in a field is commutative. Finally, a ring homomorphism between fields that maps the unity to the unity is necessarily injective.

Of course, for finite fields the Frobenius endomorphism is necessarily also surjective, so it is an automorphism of the field.

### Simple extensions

Similarly to extending the field of real numbers to the field of complex numbers, many extensions can be carried out by adding extra elements to a field and prescribing their arithmetic properties. In the general case, to avoid the trouble caused by prescribing arithmetic properties, one may consider a field extension $E/F$ and adjoin elements of $E\setminus F$ to $F$; the rules for computing with these extra elements and the elements of the field $F$ are then already determined in the larger field $E$.

???+ abstract "Field extension generated by a subset"
    Let $E/F$ be a field extension and $S\subseteq E$. Then the **extension of $F$ generated by $S$** (extension generated by $S$ over $F$) is the smallest subfield of $E$ containing both $F$ and $S$, denoted $F(S)$.

The simplest case is of course when the set $S$ has very few elements.

???+ abstract "Finitely generated extension"
    Let $E/F$ be a field extension. If there exists a finite set $S=\{\alpha_1,\cdots,\alpha_n\}\subseteq E$ such that $E=F(S)$, then $E$ is called a **finitely generated extension** of the field $F$, also written $F(\alpha_1,\cdots,\alpha_n)$.

???+ abstract "Simple extension"
    Let $E/F$ be a field extension. If there exists $\alpha\in E$ such that $E=F(\alpha)$, then the field $E$ is called a **simple extension** of the field $F$. The element $\alpha$ is called a **primitive element** of this simple extension.

???+ example "Examples"
    All of these examples are obtained by adjoining elements of $\mathbf C$ to $\mathbf Q$.
    
    1.  For a squarefree integer $D\neq 0,1$, the quadratic field $\mathbf Q(\sqrt D)$ is the simple extension obtained by adjoining $\sqrt D\in\mathbf C\setminus\mathbf Q$ to the field $\mathbf Q$. Its degree is $2$, since $\{1,\sqrt D\}$ forms a basis.
    2.  The field $\mathbf Q(\sqrt 2,\sqrt 3)$ is the extension obtained by adjoining $\sqrt 2$ and $\sqrt 3$ to the field $\mathbf Q$. Of course, $\mathbf Q(\sqrt 2,\sqrt 3)=\mathbf Q(\sqrt 2)(\sqrt 3)=\mathbf Q(\sqrt 3)(\sqrt 2)$, i.e. the final extension does not depend on the order and manner in which the elements are adjoined. This is also a simple extension, since $\mathbf Q(\sqrt 2,\sqrt 3)=\mathbf Q(\sqrt 2+\sqrt 3)$. Its degree is $4$, since $\{1,\sqrt 2,\sqrt 3,\sqrt 6\}$ forms a basis.
    3.  The field $\mathbf Q(\pi)$ is also a simple extension, where $\pi$ is the ratio of a circle's circumference to its diameter. It is an infinite extension, since already $\mathbf Q[\pi]\subseteq \mathbf Q(\pi)$ has a basis $\{1,\pi,\pi^2,\cdots\}$.
    4.  A finitely generated extension need not be a simple extension. For example, let $x,y$ be two indeterminates; then the field of rational functions $\mathbf Q(x,y)$ is a finitely generated extension of $\mathbf Q$, but its transcendence degree is $2$, so it is not a simple extension.

These examples show that the properties of simple extensions can differ enormously. This depends on the properties of the adjoined element.

### Algebraic extensions

To analyze all the cases that may arise when adjoining an element to a field, we may, following the earlier discussion of the characteristic of a field, consider ring homomorphisms from the polynomial ring $F[x]$ to the extension $E/F$. Here $F[x]$ plays the role that the ring of integers $\mathbf Z$ played before: it is exactly the "prototype" of the structure obtained by adjoining an indeterminate $x$ to the field $F$ and closing under addition, subtraction, and multiplication[^polynomial-universal].

Let the ring homomorphism $\varphi:F[x]\rightarrow E$ satisfy that the restriction of $\varphi$ to $F$ is the identity map and $\varphi(x)=\alpha$, i.e. the indeterminate is mapped to some element of the extension $E$. Since the image $\varphi(F[x])=F[\alpha]$ is necessarily an integral domain, the kernel $\ker\varphi$ of the homomorphism is necessarily a prime ideal of the polynomial ring $F[x]$. The polynomial ring over a field is a principal ideal domain, so the kernel necessarily has the form $(f(x))$, where $f(x)=0$ or $f(x)$ is an irreducible element of $F[x]$. We discuss these cases as follows:

1.  When the kernel of the homomorphism is $\ker\varphi=\{0\}$, the polynomial ring $F[x]$ is embedded in $E$, and its image $F[\alpha]$ is an integral domain. Therefore the smallest field in $E$ containing both $F$ and $\alpha$ is the field of fractions of $F[\alpha]$, namely $F(\alpha)$. This notation can be interpreted both as the result of substituting $\alpha$ for the indeterminate in the field of rational functions $F(x)$, and as the simple extension of the field $F$ generated by $\alpha$: in this context the two interpretations give the same result;

2.  When the kernel of the homomorphism is $\ker\varphi=(f(x))$ with $f(x)$ an irreducible element, we have $\varphi(f(x))=f(\alpha)=0$, i.e. $\alpha\in E$ is a root of the polynomial $f(x)$ over $F$. Since $F$ is a field, we may assume that $f(x)$ is a monic polynomial. In this case the image of the homomorphism $\varphi$ is the field $F(\alpha)$, so

    $$
    F[x]/(f(x))\cong F(\alpha).
    $$

    This splits further into two cases:

    1.  If $f(x)$ is a polynomial of degree one, i.e. $f(x)=x-\alpha$, then $\alpha\in F$, so the extension $F(\alpha)=F$ is trivial;
    2.  In the remaining cases, $f(x)$ is an irreducible polynomial of degree greater than one and $\alpha\in E\setminus F$; the image $F[\alpha]$ is then already a field containing $F$ and $\alpha$, so it is exactly $F(\alpha)$, the extension of $F$ generated by $\alpha$, and $F(\alpha)\supset F$ is not trivial.

This discussion motivates the following definitions:

???+ abstract "Algebraic and transcendental elements"
    For an extension $E/F$, if an element $\alpha\in E$ is a root of some nonzero polynomial $f(x)$ over $F$, then $\alpha$ is called an **algebraic element** over $F$; otherwise, the element $\alpha$ is called a **transcendental element** over $F$.

???+ abstract "Minimal polynomial"
    For an algebraic element $\alpha$ over a field $F$, the monic polynomial $f(x)$ of least degree having $\alpha$ as a root is called its **minimal polynomial**.

The minimal polynomial here is exactly the irreducible polynomial $f(x)$ in the analysis above. Of course, one can also prove directly that minimal polynomials are irreducible. The minimality of the minimal polynomial $f(x)$ means that any polynomial over the field $F$ having $\alpha$ as a root necessarily has $f(x)$ as a factor.

???+ example "Examples"
    1.  $\sqrt 2$ is an algebraic element over $\mathbf Q$, with minimal polynomial $x^2-2$.
    2.  $\sqrt 2$ is an algebraic element over $\mathbf R$, with minimal polynomial $x-\sqrt 2$.
    3.  $\pi$ is a transcendental element over $\mathbf Q$.
    4.  In general, algebraic elements over $\mathbf Q$ are called **algebraic numbers**, and transcendental elements are called **transcendental numbers**. In particular, if the minimal polynomial of an algebraic number has integer coefficients, it is called an **algebraic integer**. All algebraic integers in an algebraic extension form a ring. For example, the algebraic integers in the quadratic field $\mathbf Q(\sqrt{D})$ form the quadratic integer ring $\mathbf Z[\omega]$. For the meaning of this notation, see the page on [quadratic integer rings](./ring-theory.md#例子二次整数环).

???+ abstract "Algebraic and transcendental extensions"
    For an extension $E/F$, if all elements of the field $E$ are algebraic over $F$, then the field $E$ is called an **algebraic extension** of $F$; otherwise, the field $E$ is called a **transcendental extension** of $F$.

Depending on the properties of the adjoined element, the result of a simple extension falls into two classes. When the adjoined element is transcendental, the simple extension is always isomorphic to a field of rational functions. In this case there is no possibility of further simplification. But when the adjoined element is algebraic, the simple extension is actually $F[\alpha]$, i.e. the result of directly replacing the indeterminate $x$ in the polynomial ring $F[x]$ by $\alpha$. From an elementary point of view, compared with the transcendental case, the elements of the extension field can then be written without denominators; this means that a process similar to "rationalizing the denominator" in elementary arithmetic is always possible in a simple algebraic extension. Since the extension fields encountered in algorithm competitions are mainly simple algebraic extensions, the next section discusses computation in them in more detail.

The importance of simple algebraic extensions is also reflected in the following theorem:

???+ note "Theorem"
    A field extension is a finite extension if and only if it is a finitely generated algebraic extension.

??? note "Proof"
    Let $F$ be a field and $E=F(\alpha_1,\cdots,\alpha_n)$ a finitely generated algebraic extension of the field, i.e. all $\alpha_i$ are algebraic elements over $F$. Let $E_i=F(\alpha_1,\cdots,\alpha_i)$; then $E_0=F$ and $E_n=E$. Note that $\alpha_i$ is necessarily an algebraic element over $E_{i-1}$, since the minimal polynomial of $\alpha_i$ over the field $F$ is also a polynomial over $E_{i-1}$; moreover, the degree of the minimal polynomial of $\alpha_i$ over $E_{i-1}$ necessarily does not exceed the degree of the minimal polynomial of $\alpha_i$ over the field $F$. Therefore $[E_i:E_{i-1}]$ is necessarily finite, and by the multiplicativity of degrees of field extensions, $[E:F]=\prod_{i=1}^n[E_i:E_{i-1}]$ is also finite. Conversely, starting from $E_0=F$, for the already constructed $E_i$ one can each time choose an element $\alpha_{i+1}$ from $E\setminus E_i$ and adjoin it to $E_i$, obtaining the extension field $E_{i+1}=E_i(\alpha_{i+1})$, until $E_n=E$. Since the degree of the extension keeps decreasing, this process necessarily terminates in finitely many steps. Hence a finite extension is necessarily a finitely generated algebraic extension.

This means that to understand the properties of finite extensions, it suffices to understand simple algebraic extensions, since a finite extension can always be obtained by finitely many simple algebraic extensions.

### Structure and computation in simple algebraic extensions

In this section, let $F$ be a field, $E$ an extension field of it, and $\alpha\in E\setminus F$ an algebraic element over the field $F$. Let the minimal polynomial of $\alpha$ be $f(x)$, where $f(x)$ is a monic polynomial of degree $n$, i.e.

$$
f(x)=x^n+a_{n-1}x^{n-1}+\cdots+a_1x+a_0,
$$

where $a_0,a_1,\cdots,a_{n-1}\in F$ and $f(x)$ is irreducible over $F$.

The isomorphism $F(\alpha)\cong F[x]/(f(x))$ shows that arithmetic in the extension field $F(\alpha)$ is exactly polynomial arithmetic modulo $f(x)$. By polynomial division with remainder, it suffices to consider the congruence classes of all polynomials of degree less than $n=\deg f(x)$. For these polynomials, a natural basis is $\{1,\alpha,\cdots,\alpha^{n-1}\}$. Therefore we have the following result:

???+ note "Theorem"
    Under the assumptions of this section, the extension field $F(\alpha)$ can be written as
    
    $$
    F(\alpha)=\{\lambda(\alpha)=\lambda_0+\lambda_1\alpha+\cdots+\lambda_{n-1}\alpha^{n-1}:\lambda_0,\lambda_1,\cdots,\lambda_{n-1}\in F\}.
    $$
    
    Here $\lambda(x)$ ranges over all polynomials of degree less than $n$. Therefore the degree of the extension is $[F(\alpha):F]=n$, the degree of the minimal polynomial of $\alpha$. In the extension field, the addition of elements $\lambda(\alpha)$ and $\mu(\alpha)$ is just polynomial addition, i.e. adding the coefficients in corresponding positions; the product of elements $\lambda(\alpha)$ and $\mu(\alpha)$ can be written as $\rho(\alpha)$, where $\rho(x)$ is the remainder of the product $\lambda(x)\mu(x)$ divided by $f(x)$.

Of course, as a field, $F(\alpha)$ also allows division of its elements. By the description of multiplication in the theorem, this amounts to solving a [linear congruence](../number-theory/linear-equation.md) in the polynomial ring. By analogy with the integer case, to compute the quotient $\lambda(\alpha)/\mu(\alpha)$, one can first determine the multiplicative inverse of $\mu(\alpha)$ and then multiply it by $\lambda(\alpha)$. To compute the multiplicative inverse of $\mu(\alpha)$, it suffices to solve the congruence $\mu(x)\xi(x)\equiv 1\pmod{f(x)}$. This can be done with the extended Euclidean algorithm.

Below, we go through a few concrete examples to understand the details of the computation.

???+ example "Example"
    Consider the extension field $\mathbf Q(\alpha)$, where $\alpha$ is a root of the equation $x^3-2x-2=0$. We want to compute the value of
    
    $$
    \frac{1+\alpha}{1+\alpha+\alpha^2}
    $$
    
    in this field.
    
    The first step is to compute the inverse of $1+\alpha+\alpha^2$, i.e. to compute a solution of the congruence
    
    $$
    (x^2+x+1)\xi(x)+(x^3-2x-2)\nu(x)=1
    $$
    
    To this we apply the extended Euclidean algorithm. First we carry out the Euclidean algorithm of successive division, which gives the following steps:
    
    $$
    \begin{aligned}
    x^3-2x-2 &= (x-1)(x^2+x+1)+(-2x-1),\\
    x^2+x+1 &= \left(-\frac12x-\frac14\right)(-2x-1)+\frac34,\\
    -2x-1 &= \left(-\frac{8}{3}x-\frac{4}{3}\right)\frac{3}{4}.
    \end{aligned}
    $$
    
    Then we compute the coefficients in the congruence:
    
    $$
    \begin{aligned}
    \frac{3}{4}
    &=(x^2+x+1)+\left(\frac12x+\frac14\right)(-2x-1)\\
    &=(x^2+x+1)+\left(\frac12x+\frac14\right)\left((x^3-2x-2)-(x-1)(x^2+x+1)\right)\\
    &=\left(-\frac12x^2+\frac14x+\frac54\right)(x^2+x+1)+\left(\frac12x+\frac14\right)(x^3-2x-2).
    \end{aligned}
    $$
    
    Therefore the solution of the equation is
    
    $$
    \xi(x)=-\frac23x^2+\frac13x+\frac53,\ \nu(x)=\frac23x+\frac13.
    $$
    
    This shows that the inverse of $1+\alpha+\alpha^2$ is
    
    $$
    -\frac23\alpha^2+\frac13\alpha+\frac53.
    $$
    
    The second step is to compute the product of the inverse and $1+\alpha$. We have
    
    $$
    \begin{aligned}
    (1+\alpha)\left(-\frac23\alpha^2+\frac13\alpha+\frac53\right)
    &=-\frac23\alpha^3-\frac13\alpha^2+2\alpha+\frac53\\
    &=-\frac23(2\alpha+2)-\frac13\alpha^2+2\alpha+\frac53\\
    &=-\frac13\alpha^2+\frac23\alpha+\frac13.
    \end{aligned}
    $$
    
    This is the final answer.

In the example we only used the condition that $\alpha$ is a root of the equation, without specifying which particular root it is. The polynomial $x^3-2x-2=0$ has one real root and a pair of complex conjugate roots in the field of complex numbers $\mathbf C$, and the extension fields obtained by adjoining any one of them to the field of rational numbers $\mathbf Q$ are all isomorphic. In other words, these three distinct roots are indistinguishable from an algebraic point of view.

In general, for an irreducible polynomial $f(x)$ over a field $F$ with distinct roots $\alpha\neq\beta$ in an extension field, these roots exhibit the same algebraic properties when used to form simple extensions of the field $F$, and they are called **conjugates** of each other. The usual conjugation in the field of complex numbers is the special case of this notion for the field extension $\mathbf C/\mathbf R$.

???+ example "Example"
    Consider the extension field $\mathbf F_2(\alpha)$, where $\alpha$ is a root of the equation $x^2+x+1=0$. In general, for $a+b\alpha$ and $c+d\alpha$ we have the arithmetic rules
    
    $$
    \begin{aligned}
    (a+b\alpha)+(c+d\alpha)&=(a+c)+(b+d)\alpha,\\
    (a+b\alpha)(c+d\alpha)&=ac+(ad+bc)\alpha+bd\alpha^2\\
    &=(ac+bd)+(ad+bc+bd)\alpha.
    \end{aligned}
    $$
    
    This gives arithmetic rules similar to those of the field of complex numbers. Most readers are probably unfamiliar with such a root $\alpha$, but this does not prevent us from computing with the elements of such a field. In fact, $[\mathbf F_2(\alpha):\mathbf F_2]=2$, so as a vector space $|\mathbf F_2(\alpha)|=4$, i.e. we obtain a finite field of size $4$. We will see later that all finite fields are constructed in this way.

For small-scale computations, arithmetic modulo a monic polynomial $f(x)$ can usually be carried out by substituting

$$
x^n=-a_{n-1}x^{n-1}-\cdots-a_1x-a_0
$$

to reduce the degree of the target polynomial. Moreover, for extensions of low degree, one can often directly work out the arithmetic rules for the coefficients and use an implementation similar to a complex number class, without computing remainders every time.

As an example of a simple algebraic extension, see the [reference implementation](#reference-implementation) of finite fields below.

In practice, the algorithms described here can only handle cases where the degree of the extension is fairly low, which is sufficient for the vast majority of applications in algorithm competitions. For cases where the degree of the extension is so high that it becomes the bottleneck of the complexity, appropriate polynomial techniques ([fast Fourier transform](../poly/fft.md), [number-theoretic transform](../poly/ntt.md), [fast polynomial modulo](../poly/elementary-func.md#polynomial-division-and-modulo), [polynomial Euclidean algorithm](../poly/intro.md#factorization-and-the-euclidean-algorithm), etc.) should be used to speed up the computation.

### Splitting fields

The structure of simple algebraic extensions has been discussed in detail above. However, such extensions are often not sufficient:

???+ example "Example"
    Consider the extension $\mathbf Q(\sqrt[3]{2})/\mathbf Q$. The minimal polynomial of the algebraic element $\sqrt[3]{2}$ over the field $\mathbf Q$ is $x^3-2$. In the field of complex numbers $\mathbf C$, the polynomial $x^3-2$ has three roots, namely $\sqrt[3]{2},\sqrt[3]{2}\omega,\sqrt[3]{2}\omega^2$, where $\omega=\mathrm{e}^{2\pi\mathrm{i}/3}$ is a primitive cube root of $1$. Although $\mathbf Q(\sqrt[3]{2})\cong\mathbf Q(\sqrt[3]{2}\omega)\cong\mathbf Q(\sqrt[3]{2}\omega^2)$, the field $\mathbf Q(\sqrt[3]{2})$ does not contain the other two roots, so a computation such as $\sqrt[3]{2}+\sqrt[3]{2}\omega$ is already impossible in it. To fully study all three roots, the field $\mathbf Q(\sqrt[3]{2})$ must be extended further, namely to $\mathbf Q(\sqrt[3]{2},\sqrt[3]{2}\omega,\sqrt[3]{2}\omega^2)$.
    
    As explained above, to carry out such an extension it suffices to perform simple extensions element by element. Note that the minimal polynomial of $\sqrt[3]{2}\omega$ over the field $\mathbf Q$ is not the same as over the field $\mathbf Q(\sqrt[3]{2})$: the former is $x^3-2\in\mathbf Q[x]$, while the latter is $x^2+\sqrt[3]{2}x+\sqrt[3]{4}\in \mathbf Q(\sqrt[3]{2})[x]$, because
    
    $$
    x^3-2 = (x-\sqrt[3]{2})(x^2+\sqrt[3]{2}x+\sqrt[3]{4}).
    $$
    
    After the field is extended, a linear factor splits off from the original minimal polynomial, so the degree of the minimal polynomial of the remaining roots is lower than that of the minimal polynomial over the original field. The process of repeatedly extending the field is exactly the process of repeatedly "splitting" the polynomial. Therefore, at each simple extension the minimal polynomial has to be determined anew.

Adjoining all roots of a polynomial to the field gives the splitting field of the polynomial.

???+ abstract "Splitting"
    Let $F$ be a field. If a polynomial $f(x)$ can be factored in $F[x]$ into a product of linear factors, the polynomial $f(x)$ is said to **split** in the field $F$.

???+ abstract "Splitting field"
    For a polynomial $f(x)$ over a field $F$, if an extension $E/F$ is such that $f(x)$ splits in the field $E$ but does not split in any proper subfield of $E$, then the field $E$ is called a **splitting field** of the polynomial $f(x)$.

It can be shown that, just like simple extensions, the splitting field of a given polynomial is uniquely determined up to isomorphism, independently of the particular construction. A splitting field is always a finite extension.

???+ abstract "Normal extension"
    For an algebraic extension $E/F$, if for every $\alpha\in E$ the minimal polynomial of $\alpha$ splits in $E$, then the field $E$ is called a **normal extension** of the field $F$.

Normal extensions play a fundamental role in Galois theory.

### Algebraically closed fields

Most of the notions concerning extensions mentioned above must, in principle, be considered inside a field larger than the extension itself. Although in the case of simple extensions a field extension can be constructed via the polynomial ring without relying on a larger field, there is no such tool in the general case. For the field of rational numbers $\mathbf Q$ and the field of real numbers $\mathbf R$, one can always assume that algebraic extensions are contained in the field of complex numbers $\mathbf C$. For finite fields, there is no similar known field. In fact, every field has an algebraic closure, so that all algebraic extensions of the field can be assumed to take place inside the algebraic closure. This completely resolves the problem.

???+ abstract "Algebraic closure"
    For a field $F$, if a field $\overline F$ is an algebraic extension of the field $F$ and every $f(x)\in F[x]$ splits in $\overline F$, then the field $\overline F$ is called an **algebraic closure** of the field $F$.

An algebraic closure is a normal extension of the field. Its construction essentially consists of adjoining the roots of all possible polynomials to the field. Moreover, like the splitting field, the algebraic closure of a field is unique up to isomorphism.

???+ note "Theorem"
    Every field $F$ has an algebraic closure.

??? note "Proof"
    The difficulty of the proof comes from set theory. Here we cite a proof due to Artin.
    
    The first part of the proof starts from $F$ and constructs an extension $K_1/F$ such that every polynomial over $F$ has at least one root in $K_1$. For the field $F$, consider the polynomial ring in many indeterminates[^multi-poly-ring] $R=F[\cdots,x_f,\cdots]$, where the subscript of the indeterminate $x_f$ ranges over all monic polynomials over $F$. Let $I$ denote the ideal generated by all $f(x_f)$. First, $I\neq R$, so a maximal ideal $M\supseteq I$ exists. Otherwise, if $1\in I$, there would necessarily exist finitely many monic polynomials $f_i$ over the field $F$ and corresponding elements $g_i$ of the ring $R$ such that $g_1f_1(x_{f_1})+\cdots+g_kf_k(x_{f_k})=1$. Let $F(\alpha_1,\cdots,\alpha_k)$ be the algebraic extension obtained by adjoining roots $\alpha_i$ of the $f_i(x)$ to $F$. Substituting $\alpha_i$ for each $x_{f_i}$ in the above identity in $F(\alpha_1,\cdots,\alpha_k)$, and $0$ for all other indeterminates $x_f$ appearing in the various $g_i$, we obtain the equation $0=1$ in $F(\alpha_1,\cdots,\alpha_k)$, a contradiction. Hence $I\neq R$, and the construction of the maximal ideal $M$ is legitimate. The quotient ring $R/M$ is then a field, denoted $K_1$, and every monic polynomial $f(x)$ over $F$ has a root $\overline{x_f}$ in $K_1$.
    
    The second part of the proof inductively obtains an algebraically closed field $K$ (defined below) containing $F$. Repeating the above construction, from the field $K_i$ one can construct a field $K_{i+1}$ such that every polynomial over $K_i$ has at least one root in $K_{i+1}$. Moreover, $K_i$ embeds naturally into $K_{i+1}$, so their union $K=\bigcup_{i=1}^\infty K_i$ can be defined. It is easy to verify that this is also a field, and the coefficients of any polynomial over $K$ are necessarily all contained in some $K_i$, so one of its roots necessarily appears in $K_{i+1}\subseteq K$. This shows that every polynomial over $K$ has at least one root in $K$, so $K$ is an algebraically closed field.
    
    Finally, let $\overline F$ denote the set of all elements of $K$ that are algebraic over $F$. It is clearly a field, because for any $\alpha,\beta\in\overline F$ we have $\alpha\pm\beta,\alpha\beta,\alpha/\beta\in F(\alpha,\beta)\subseteq\overline F$. It is also an algebraic extension of $F$, because all its elements are algebraic over $F$. For a polynomial $f(x)$ over $F$, all its roots are algebraic over $F$, hence also lie in $\overline F$, and therefore it necessarily splits into a product of linear factors. This shows that $\overline F$ is an algebraic closure of $F$.

???+ example "Examples"
    1.  The algebraic closure of the field of real numbers $\mathbf R$ is the field of complex numbers $\mathbf C$.
    2.  The algebraic closure of the field of rational numbers $\mathbf Q$ is the set of all algebraic numbers (i.e. the algebraic elements in the field extension $\mathbf C/\mathbf Q$), denoted $\overline{\mathbf Q}$.

All algebraic extensions of an algebraic closure are trivial. Such fields are called algebraically closed.

???+ abstract "Algebraically closed field"
    If every nonconstant polynomial $f(x)$ over a field $F$ has at least one root $\alpha\in F$, then the field $F$ is called an **algebraically closed field**.

In fact, it has the following equivalent definitions:

???+ note "Theorem"
    For a field $F$, the following properties are equivalent:
    
    1.  The field $F$ is algebraically closed;
    2.  Every polynomial $f(x)$ over the field $F$ splits;
    3.  The only irreducible polynomials over the field $F$ are the polynomials of degree one;
    4.  The field $F$ has no nontrivial algebraic extensions;
    5.  The field $F$ has no nontrivial finite extensions;
    6.  The field $F$ is the algebraic closure of some field.

??? note "Proof"
    The equivalence of the first five properties is obvious from the definitions. For the sixth, an algebraically closed field is clearly its own algebraic closure, since it has no nontrivial algebraic extensions; conversely, we must show that the algebraic closure of a field $F$ is necessarily algebraically closed. Let $\overline F$ be an algebraic closure of the field $F$ and let $f(x)$ be a polynomial over $\overline F$. Let $\alpha$ be a root of $f(x)$ in the splitting field of $f(x)$, and let $S\subseteq\overline F$ be the set of nonzero coefficients of $f(x)$. Then, since $F(S)(\alpha)=F(S\cup\{\alpha\})$ is a finite extension, $\alpha$ is necessarily an algebraic element over $F$, so by the definition of the algebraic closure, the minimal polynomial of $\alpha$ over $F$ splits in the field $\overline F$, and hence $\alpha\in\overline F$. This shows that every polynomial over $\overline F$ has at least one root.

Finally, the [fundamental theorem of algebra](../poly/fundamental.md) [^fundamental-algebra] states that $\mathbf C$ is an algebraically closed field. The irreducible polynomials over the field of real numbers $\mathbf R$ have degree at most two, or equivalently, the algebraic extensions of it are at most quadratic extensions, precisely because the largest field that can be obtained by algebraic extension is $\mathbf C$.

### Separable extensions

The notion of a splitting field guarantees that for any polynomial over a field there is an extension field containing all of its roots, and the splitting field is precisely the smallest such extension field. The properties of a polynomial and the properties of its splitting field are closely related. However, if one wishes to study the properties of a polynomial via its splitting field, the first problem one faces is that the splitting field of a polynomial does not depend on the multiplicities of its roots. Therefore, if possible, one should consider some kind of "simplest representation" of the polynomial. Motivated by this, polynomials that have no repeated roots even in the algebraic closure of the field are called separable polynomials.

???+ abstract "Separable polynomial"
    For a polynomial $f(x)$ over a field $F$, if $f(x)$ has no repeated roots in the algebraic closure $\overline F$ of $F$, i.e. its factorization into a product of linear factors has no repeated factors, then $f(x)$ is called **separable**.

Since the discussion always takes place in the algebraic closure of the field $F$, whether a polynomial is separable does not actually depend on the choice of the field $F$. However, since the coefficients of the polynomial lie in $F$, one should give a criterion that decides separability of a polynomial within the field $F$, without explicitly constructing an extension field.

Readers familiar with analysis know that whether a polynomial function has repeated roots can be decided via its derivative: a repeated root of a polynomial function is also a root of its derivative. Although a polynomial and a polynomial function are not the same concept, the method for deciding whether a polynomial function has repeated roots can be transferred by analogy to polynomials. The derivative of a polynomial can be defined formally as follows:

???+ abstract "Formal derivative"
    For a polynomial
    
    $$
    f(x)=a_0+a_1x+a_2x^2+\cdots+a_{n-1}x^{n-1}+a_nx^n=\sum_{i=0}^na_ix^i
    $$
    
    over a field $F$, its **(formal) derivative**, denoted $Df(x)$, is defined to be the polynomial
    
    $$
    Df(x)=a_1+2a_2x+\cdots+(n-1)a_{n-1}x^{n-2}+na_nx^{n-1}=\sum_{i=1}^nia_ix^{i-1}.
    $$

This definition applies to polynomials over every field and does not depend on any topological structure; the derivative operator $D$ here merely maps one polynomial to another. Moreover, by comparing coefficients one can verify that the usual rules of differentiation, such as $D(f(x)g(x))=(Df(x))g(x)+f(x)(Dg(x))$, still hold for the formal derivative.

Furthermore, to check whether a polynomial $f(x)$ and its derivative $Df(x)$ have a common root in the splitting field, one need not construct this splitting field explicitly, but can decide it via their greatest common divisor; this is because a root of a polynomial always appears in its minimal polynomial, and a repeated root means that the corresponding minimal polynomial factor is also repeated. Thus the criterion for repeated roots is as follows:

???+ note "Theorem"
    For a polynomial $f(x)$ over a field $F$, if $f(x)$ has a repeated root $\alpha$, then the derivative $Df(x)$ also has the root $\alpha$. Furthermore, the polynomial $f(x)$ is separable if and only if $f(x)$ and its derivative $Df(x)$ are coprime, i.e. $\gcd(f(x),Df(x))=1$.

??? note "Proof"
    First, since division with remainder is preserved in extension fields, the result of the Euclidean algorithm does not depend on the choice of the extension field, so it suffices to discuss their common factors in the splitting field. Thus, let $\alpha$ be a root of $f(x)$ of multiplicity $k>1$; then in the splitting field there is a factorization $f(x)=(x-\alpha)^kg(x)$, so its derivative $Df(x)=k(x-\alpha)^{k-1}g(x)+(x-\alpha)^kDg(x)$ necessarily also has the root $\alpha$. Conversely, if both $f(x)$ and $Df(x)$ have the root $\alpha$, then for the factorization $f(x)=(x-\alpha)g(x)$ in the splitting field we have $Df(x)=(x-\alpha)Dg(x)+g(x)$, so $\alpha$ is also a root of $g(x)$, and hence $\alpha$ is a repeated root of $f(x)$. This proves the first part of the theorem. Furthermore, the polynomial $f(x)$ having a repeated root $\alpha$ is equivalent to $x-\alpha$ being a factor of $\gcd(f(x),Df(x))$. Therefore, the polynomial $f(x)$ being inseparable is equivalent to $\gcd(f(x),Df(x))$ having degree at least one.

A polynomial over a field can always be factored into a product of several irreducible polynomials. Since distinct (up to associates) irreducible polynomials always have distinct roots, repetition of roots is naturally connected with repetition of the corresponding polynomial factors. So, if the factorization of a polynomial has no repeated irreducible factors, can one conclude that the polynomial is separable? In other words, are all irreducible polynomials separable? Unfortunately, in general the answer is negative. The problem arises in fields of finite characteristic.

For an irreducible polynomial $f(x)$ over a field $F$, the polynomial $\gcd(f(x),Df(x))$, being a factor of $f(x)$, can only be one of two things: $1$ or $f(x)$. In the former case, the polynomial $f(x)$ is of course separable; the problem arises in the latter case. However, since the definition of the derivative already guarantees $Df(x)=0$ or $\deg Df(x)<\deg f(x)$, $f(x)$ being a factor of $Df(x)$ can only mean $Df(x)=0$. This is possible in fields of finite characteristic.

For a field $F$ of characteristic $p$, if $Df(x)=0$, then all nonzero coefficients of the polynomial can only appear at terms whose degree is a multiple of $p$, i.e. the polynomial $f(x)$ can be written as

$$
f(x)=a_0+a_px^p+a_{2p}x^{2p}+\cdots+a_{(k-1)p}x^{(k-1)p}+a_{kp}x^{kp}.
$$

If there really exists a polynomial $f(x)$ over the field $F$ that is both irreducible and inseparable, it can only have this form. However, if every element of the field $F$ always has a $p$-th root, i.e. for every coefficient $a_{jp}$ there exists $b_j\in F$ such that $a_{jp}$ can be written in the form $b_j^p$, then by the Frobenius endomorphism we always have

$$
\begin{aligned}
f(x)&=a_0+a_px^p+a_{2p}x^{2p}+\cdots+a_{(k-1)p}x^{(k-1)p}+a_{kp}x^{kp}\\
&=b_0^p+b_1^px^p+b_2^px^{2p}+\cdots+b_{k-1}^px^{(k-1)p}+b_k^px^{kp}\\
&=\left(b_0+b_1x+b_2x^2+\cdots+b_{k-1}x^{k-1}+b_kx^k\right)^p.
\end{aligned}
$$

Therefore, over such a field $F$ there are no irreducible polynomials of this form. Hence, over such a field all irreducible polynomials are separable. Such fields are called perfect fields.

???+ abstract "Perfect field"
    If all irreducible polynomials over a field $F$ are separable polynomials, it is called a **perfect field**.

For perfect fields, the notion of a separable polynomial coincides with the notion of a polynomial with no square factors in its unique factorization.

???+ note "Theorem"
    Let the field $F$ be perfect. Then a polynomial over $F$ is separable if and only if it can be written as a product of several distinct (up to associates) irreducible polynomials.

The discussion in this section is actually already sufficient to give a method for removing repeated factors from a polynomial, which is a key step in algorithms for factoring polynomials. But this is beyond the scope of this article; interested readers can consult the references at the end.

This discussion also gives a characterization of perfect fields:

???+ note "Theorem"
    A field $F$ is perfect if and only if the characteristic of $F$ is zero, or the characteristic of $F$ is $p$ and every element $x\in F$ has a $p$-th root (i.e. the Frobenius endomorphism is also an automorphism).

The field of rational numbers $\mathbf Q$ and the finite fields $\mathbf F_q$ discussed below are perfect fields.

When the field is not perfect, there do exist inseparable irreducible polynomials.

??? example "Example"
    Consider the polynomial $x^2-t$ over the field of rational functions $\mathbf F_2(t)$ of $\mathbf F_2$. Since $\mathbf F_2(t)$ is the field of fractions of the unique factorization domain $\mathbf F_2[t]$ and $t$ is a prime element of $\mathbf F_2[t]$, applying Eisenstein's criterion to the prime element $t$ shows that $x^2-t$ is irreducible in $\mathbf F_2[t]$, hence also irreducible in $\mathbf F_2(t)$. However, its derivative is $0$, so $x^2-t$ is not separable. In fact, in the extension field $\mathbf F_2(t)(\sqrt t)$ it has the double root $\sqrt t$.

Finally, let us return to the discussion of field extensions.

???+ abstract "Separable extension"
    For an algebraic extension $E/F$, if for every $\alpha\in E$ the minimal polynomial of $\alpha$ is a separable polynomial, then the field $E$ is called a **separable extension** of the field $F$.

All algebraic extensions of a perfect field are separable extensions. This can also serve as an equivalent definition of a perfect field.

If an algebraic extension is both normal and separable, it is also called a Galois extension. In a Galois extension, no irreducible polynomial has repeated roots, and the number of roots is exactly equal to the degree of the polynomial, so permutations of the roots fully reflect the properties of the field extension and of the polynomial. Such extensions provide the cornerstone on which Galois theory is built. Interested readers can consult the references at the end.

## Cyclotomic fields

As a simple example of field extensions, this section discusses cyclotomic fields. Another simple example of field extensions is given by [quadratic fields](../number-theory/quadratic.md).

### Group of roots of unity

In the field of complex numbers $\mathbf C$, the roots of the polynomial $x^n-1$ are called the **$n$-th roots of unity**. Write $\zeta_n=\mathrm{e}^{2\pi\mathrm{i}/n}$. Then the set of all $n$-th roots of unity is $C_n=\{\zeta_n^k:k\in\mathbf Z\}$. Under multiplication, $C_n$ forms a cyclic group of order $n$, which can be written $\langle\zeta_n\rangle$ and is called the group of $n$-th roots of unity. The generators of the group $C_n$, i.e. the elements whose order is exactly $n$, are called the **primitive $n$-th roots of unity**. The set of primitive $n$-th roots of unity $P_n=\{\zeta_n^k:k\in\mathbf Z,k\perp n\}$ has exactly $\varphi(n)$ elements, where $\varphi(n)$ is [Euler's totient function](../number-theory/euler-totient.md). Classifying the elements of the group of roots of unity $C_n$ by their order gives the following decomposition:

$$
C_n=\bigcup_{d|n}P_d.
$$

Counting the elements on both sides gives the identity $n=\sum_{d\mid n}\varphi(d)$.

### Cyclotomic field

A cyclotomic field is the extension field obtained by adjoining roots of unity to the field of rational numbers.

???+ abstract "Cyclotomic field"
    The extension field $\mathbf Q(\zeta_n)$ obtained by adjoining the complex $n$-th root of unity $\zeta_n=\mathrm{e}^{2\pi\mathrm{i}/n}$ to the field of rational numbers $\mathbf Q$ is called the **$n$-th cyclotomic field**.

Since all $n$-th roots of unity form the cyclic group $\langle\zeta_n\rangle$ under multiplication, the cyclotomic field $\mathbf Q(\zeta_n)$ also contains all these $n$-th roots of unity. In fact, $\mathbf Q(\zeta_n)$ is exactly the splitting field of the polynomial $x^n-1$ over the field $\mathbf Q$.

???+ note "Theorem"
    The cyclotomic field $\mathbf Q(\zeta_n)$ is the splitting field of the polynomial $x^n-1$ over the field of rational numbers $\mathbf Q$.

??? note "Proof"
    Let $F$ be the splitting field of the polynomial $x^n-1$ over the field of rational numbers $\mathbf Q$. Since $\mathbf Q(\zeta_n)$ contains all complex roots of the polynomial $x^n-1$, we have $F\subseteq\mathbf Q(\zeta_n)$. Conversely, since $\zeta_n\in F$, necessarily $\mathbf Q(\zeta_n)=F$. This shows $F=\mathbf Q(\zeta_n)$.

This can serve as an equivalent definition of the cyclotomic field. In fact, adjoining any primitive $n$-th root of unity to the field of rational numbers yields $\mathbf Q(\zeta_n)$.

### Cyclotomic polynomials

The cyclotomic field $\mathbf Q(\zeta_n)$ is a simple algebraic extension of the field of rational numbers $\mathbf Q$. By the analysis above, such a field is always isomorphic to a quotient ring of some polynomial ring. To obtain this isomorphism, one needs to analyze the minimal polynomial $f(x)$ of $\zeta_n$. Since $\zeta_n$ is a root of $x^n-1$, $f(x)$ is necessarily some factor of $x^n-1$. This means that we need to study the factorization of the polynomial $x^n-1$ in $\mathbf Q[x]$. By Gauss's lemma, it can necessarily be factored in $\mathbf Z[x]$ into a product of several irreducible monic polynomials.

Since $\mathbf Q(\zeta_n)$ is the splitting field, the polynomial $x^n-1$ has the factorization:

$$
x^n-1=\prod_{\zeta\in C_n}(x-\zeta)=\prod_{d\mid n}\prod_{\zeta\in P_d}(x-\zeta).
$$

Since roots of unity of different orders have different algebraic properties, they are certainly not roots of the same irreducible polynomial. Therefore, to study the minimal polynomial of $\zeta_n$, it suffices to consider the factor

$$
\Phi_n(x)=\prod_{\zeta\in P_n}(x-\zeta)
$$

in the above factorization. The minimal polynomial of the root of unity $\zeta_n$ is necessarily a factor of $\Phi_n(x)$. Moreover, the $\Phi_n(x)$ so defined has the following property:

???+ note "Theorem"
    $\Phi_n(x)$ is a monic polynomial with integer coefficients, and it is irreducible in $\mathbf Z[x]$.

??? note "Proof"
    By definition, $\Phi_n(x)$ is clearly a monic polynomial. First, we show that $\Phi_n(x)\in\mathbf Z[x]$. By Gauss's lemma, the polynomial $x^n-1$ has the same factorization in $\mathbf Z[x]$ and in $\mathbf Q[x]$, and every factor is a monic polynomial with integer coefficients. In this factorization, every factor $f(x)$ is irreducible over $\mathbf Q[x]$ and splits in $\mathbf Q(\zeta_n)$; all its roots are $n$-th roots of unity and necessarily have the same order, so these roots must all belong to one and the same $P_d$ and cannot be distributed among different $P_d$. This means that every factor $f(x)$ is a factor of some $\Phi_d(x)$. Hence $\Phi_n(x)$ can be written as a product of several monic polynomials with integer coefficients, and is therefore necessarily itself a monic polynomial with integer coefficients.
    
    Next, we show that $\Phi_n(x)$ is irreducible in $\mathbf Z[x]$. Suppose it has a factorization $f(x)g(x)$ with $f(x)$ irreducible in $\mathbf Z[x]$; then it suffices to show that $f(x)$ contains all primitive $n$-th roots of unity. That is, let $\zeta$ be a root of $f(x)$; we need to show that for all $k\perp n$, $\zeta^k$ is also a root of $f(x)$. Since $k$ can always be factored into a product of primes, it suffices to show that for every prime $p\perp n$, $\zeta^p$ is a root of $f(x)$. Suppose not, so that $\zeta^p$ is a root of $g(x)$. Then $\zeta$ is a common root of the polynomials $f(x)$ and $g(x^p)$ in $\mathbf Z[x]$. Since $f(x)$ is the minimal polynomial of $\zeta$ over $\mathbf Q$, necessarily $f(x)$ divides $g(x^p)$; that is, there exists $h(x)\in\mathbf Z[x]$ such that $g(x^p)=f(x)h(x)$. Reducing both sides modulo $p$, we obtain the equation $\overline{g}(x^p)=\overline{f}(x)\overline{h}(x)$ in $\mathbf F_p[x]$. Using the Frobenius endomorphism, we get $\overline{g}(x)^p=\overline{f}(x)\overline{h}(x)$. Since $\mathbf F_p[x]$ is also a unique factorization domain, $\overline{g}(x)$ and $\overline{f}(x)$ necessarily have a nontrivial common factor, so $x^n-\overline 1=\overline{f}(x)\overline{g}(x)$ is inseparable over $\mathbf F_p$. But since $p\perp n$, its formal derivative $nx^{n-1}$ is coprime to it, contradicting its inseparability. Hence $\zeta^p$ is necessarily also a root of $f(x)$, so $f(x)$ contains all primitive $n$-th roots of unity, and it is exactly $\Phi_n(x)$.

This shows that it is exactly the minimal polynomial of $\zeta_n$; it is also called the **$n$-th cyclotomic polynomial**. The defining formula above shows that it has $\varphi(n)$ complex roots, and these complex roots are exactly all the primitive $n$-th roots of unity, where $\varphi(n)$ is [Euler's totient function](../number-theory/euler-totient.md). This also shows that $\mathbf Q(\zeta_n)/\mathbf Q$ is an extension of degree $\varphi(n)$.

The ring of algebraic integers in the cyclotomic field $\mathbf Q(\zeta_n)$ is $\mathbf Z[\zeta_n]$. In addition, when $\varphi(n)=2$, the cyclotomic field is a [quadratic extension](../number-theory/quadratic.md). Specifically, $\mathbf Q(\zeta_4)$ is the quadratic field $\mathbf Q(\sqrt{-1})$; $\mathbf Q(\zeta_3)$ and $\mathbf Q(\zeta_6)$ coincide, and both are the quadratic field $\mathbf Q(\sqrt{-3})$.

Using cyclotomic polynomials, the polynomial $x^n-1$ has the unique factorization in $\mathbf Z[x]$

$$
x^n-1=\prod_{d\mid n}\Phi_d(x).
$$

Therefore $(x^d-1)\mid(x^n-1)$ if and only if $d\mid n$. Moreover, applying [Möbius inversion](../number-theory/mobius.md) to this formula gives

$$
\Phi_n(x)=\prod_{d\mid n}(x^d-1)^{\mu(n/d)}.
$$

Using this expression, all cyclotomic polynomials can be computed recursively. Here we give the first few cyclotomic polynomials as examples, to help the reader get familiar with them.

???+ example "Cyclotomic polynomials"
    The first $10$ cyclotomic polynomials are as follows:
    
    $$
    \begin{aligned}
    \Phi_1(x) &= x-1,\\
    \Phi_2(x) &= x+1,\\
    \Phi_3(x) &= x^2+x+1,\\
    \Phi_4(x) &= x^2+1,\\
    \Phi_5(x) &= x^4+x^3+x^2+x+1,\\
    \Phi_6(x) &= x^2-x+1,\\
    \Phi_7(x) &= x^6+x^5+x^4+x^3+x^2+x+1,\\
    \Phi_8(x) &= x^4+1,\\
    \Phi_9(x) &= x^6+x^3+1,\\
    \Phi_{10}(x) &= x^4-x^3+x^2-x+1.
    \end{aligned}
    $$
    
    An interesting fact is that, although it looks as if the coefficients of cyclotomic polynomials can only be $0$ and $\pm1$, this is not true for general $n$. The first counterexample occurs at $\Phi_{105}(x)$, and it can be shown that as $n$ grows, the coefficients can take arbitrarily large values.

Using the Möbius inversion formula above, the following properties can be summarized to simplify the computation of $\Phi_n(x)$:

???+ note "Properties"
    For the cyclotomic polynomial $\Phi_n(x)$, we have:
    
    1.  For a prime $p\mid n$, $\Phi_{pn}(x)=\Phi_n(x^p)$;
    2.  For a prime $p\perp n$, $\Phi_{pn}(x)=\dfrac{\Phi_n(x^p)}{\Phi_n(x)}$;
    3.  In particular, if $n>1$ is odd, then $\Phi_{2n}(x)=\Phi_n(-x)$;
    4.  For a prime $p$, $\Phi_{p}(x)=1+x+\cdots+x^{p-1}$;
    5.  In particular, $\Phi_{2^k}(x)=x^{2^{k-1}}+1$.

These properties show that in computing cyclotomic polynomials, the focus is on the case where the index is an odd squarefree number. In that case, one can add the prime factors one by one using the second property; adding each prime factor requires only one polynomial division.

Cyclotomic polynomials have many other properties.

???+ note "Theorem"
    Let $\Phi_n(x)$ be the cyclotomic polynomial of order $n>1$, and let its degree be $\varphi(n)$. Then:
    
    1.  The polynomial $\Phi_n(x)$ is a palindromic polynomial: the coefficient of the term of degree $j$ equals the coefficient of the term of degree $\varphi(n)-j$, i.e. $\Phi_n(x)=x^{\varphi(n)}\Phi_n(1/x)$;
    2.  The coefficient of the term of degree $\varphi(n)-1$ equals the Möbius function $-\mu(n)$;
    3.  If $n$ is a prime power $p^k$, then $\Phi_n(1)=p$; otherwise $\Phi_n(1)=1$;
    4.  Let $b>1$ and let $p$ be a prime factor of $\Phi_n(b)$. Then either $p\mid n$, or $n$ is the order of $b$ in the multiplicative group $(\mathbf Z/p\mathbf Z)^\times$, and these two cases cannot occur simultaneously.

??? note "Proof"
    For the first three properties, it suffices to use Möbius inversion. For 1, look directly at the Möbius inversion form of $\Phi_n(x)$, namely $\Phi_n(x)=\prod_{d\mid n}(x^d-1)^{\mu(n/d)}$; for 2, let the coefficient of the term of degree $\varphi(n)-1$ of $\Phi_n(x)$ be $f(n)$; comparing the coefficients of the terms of degree $n-1$ on both sides of $x^n-1=\prod_{d\mid n}\Phi_d(x)$ gives $\sum_{d\mid n}f(d)=-[n=1]$, and then apply Möbius inversion; for 3, divide both sides of $x^n-1=\prod_{d\mid n}\Phi_d(x)$ by $\Phi_1(x)=x-1$ and substitute $x=1$, giving $n=\prod_{d\mid n,d\neq 1}\Phi_d(1)$, and then apply Möbius inversion.
    
    We now prove the fourth property. First, if $n$ is the order of $b$ in the multiplicative group $(\mathbf Z/p\mathbf Z)^\times$, then $n$ is the smallest positive integer with $p\mid b^n-1$, so $p\mid\Phi_n(b)$. Conversely, if $p\mid\Phi_n(b)$, then $b^n\equiv 1\pmod p$; but if $n$ is not the order of $b$ in the multiplicative group $(\mathbf Z/p\mathbf Z)^\times$, let its order be $k$; then necessarily $k\mid n$ and $p\mid\Phi_k(b)$. In this case $\Phi_k(x)$ and $\Phi_n(x)$ have the common root $b$ in the field $\mathbf F_p$, which means that $x^n-1$ has the repeated root $b$. This shows $p\mid n$; otherwise $x^n-1$ would be coprime to its derivative, hence separable over $\mathbf F_p$, and could not have a repeated root. Therefore, there are only two possibilities for a prime factor $p$ of $\Phi_n(b)$: $p\mid n$, or $n$ is the order of $b$ in the multiplicative group $(\mathbf Z/p\mathbf Z)^\times$. These two cases are mutually exclusive, since the latter implies $n\mid p-1$.

Cyclotomic polynomials can also be used to solve some problems in number theory and algebra. For example, the period length of a fraction written as a decimal in some base is closely related to cyclotomic polynomials. For these concrete applications, interested readers can consult the references at the end of the article.

## Finite fields

A **finite field**, also called a **Galois field**, is a field with only finitely many elements. The structure of a finite field is uniquely determined by its number of elements, and its number of elements is necessarily a power of a prime.

???+ note "Theorem"
    A field of size $q$ exists if and only if $q$ is of the form $p^n$, a prime power. Moreover, such a field is unique up to isomorphism and is denoted $\mathbf F_q$. The prime $p$ is the characteristic of the field $\mathbf F_q$, and the positive integer $n$ is the degree of the field extension $\mathbf F_q/\mathbf F_p$. Finally, $\mathbf F_q$ is the splitting field of the polynomial $x^q-x$ over $\mathbf F_p$, and it contains exactly the $q$ distinct roots of $x^q-x$.

??? note "Proof"
    Let the field $F$ be finite. The characteristic of the field $F$ is necessarily finite; denote it by $p$. Hence the field $F$ has the prime subfield $\mathbf F_p$. Moreover, the field $F$ is necessarily a finite extension of $\mathbf F_p$; denote the degree of the extension by $n$. As an $n$-dimensional vector space over $\mathbf F_p$, the field $F$ has $q=p^n$ elements. All nonzero elements of the field $F$ form the group $F^\times$ of order $q-1$, so $x^{q-1}=1$. Therefore all elements of $F=F^\times\cup\{0\}$ satisfy $x^q=x$, i.e. they are the $q$ distinct roots of the polynomial $x^q-x$. Therefore, in the field $F$ the polynomial $x^q-x$ has the factor $\prod_{\alpha\in F}(x-\alpha)$, but the degree of this factor is already $q$ and its leading coefficient equals $1$, so $x^q-x=\prod_{\alpha\in F}(x-\alpha)$. This shows that $x^q-x$ splits in $F$. Any field in which $x^q-x$ splits, since $x^q-x$ has $q$ distinct roots, must have at least $q$ elements. This shows that $F$ is the smallest field in which $x^q-x$ splits, i.e. the splitting field of $x^q-x$. In summary, a finite field of size $q$ is necessarily the splitting field of the polynomial $x^q-x$ over its prime subfield. Since splitting fields are unique up to isomorphism, the field of size $q$ is necessarily also unique.
    
    Conversely, given a prime $p$ and a power $q=p^n$ of it, we must show that the splitting field of the polynomial $x^q-x$ over $\mathbf F_p$ has exactly $q$ elements, in order to show that fields of order $q$ exist for all prime powers. Since the splitting field of the polynomial $x^q-x$ over $\mathbf F_p$ always exists, let $F$ be the set of all roots of the polynomial $x^q-x$ in this splitting field. We now show that $F$ is a field, so that it is the splitting field of the polynomial $x^q-x$ itself. But iterating the Frobenius endomorphism $n$ times shows that $x\mapsto x^q$ is also an endomorphism, so for any $\alpha,\beta\in F$ we have $(\alpha\pm\beta)^q=\alpha^q\pm\beta^q$, $(\alpha\beta)^q=\alpha^q\beta^q$, and $(\alpha^{-1})^q=(\alpha^q)^{-1}$. Therefore the set $F$ is closed under addition, subtraction, multiplication, and division, and it is a field. This shows that $F$ is exactly the splitting field of the polynomial $x^q-x$ over $\mathbf F_p$.

???+ note "Corollary"
    In a finite field $\mathbf F_q$ ($q>2$), the sum of all nonzero elements is $0$ and their product is $-1$.

??? note "Proof"
    The nonzero elements of a finite field are exactly the $q-1$ roots of the polynomial $x^{q-1}-1$; it suffices to apply Vieta's formulas.

In the prime field $\mathbf F_p$, the statement of this corollary about the product is exactly (part of) [Wilson's theorem](../number-theory/factorial.md#wilsons-theorem) from number theory.

### Multiplicative structure

The multiplicative group $\mathbf F_q^\times=\mathbf F_q\setminus\{0\}$ of a finite field is always a cyclic group.

???+ note "Theorem"
    Every finite subgroup of the multiplicative group of a field $F$ is a cyclic group.

??? note "Proof"
    Let $G$ be a subgroup of the multiplicative group of the field $F$ with $|G|=n$. Then $G$ is a finite abelian group. By the fundamental theorem of finite abelian groups, the group $G$ has an invariant factor decomposition $C_{n_1}\times\cdots\times C_{n_s}$ with $n_1\mid\cdots\mid n_s$. Therefore, for every element $x$ of $G$, $x^{n_s}=1$. That is, the elements of the group $G$ are all roots of the polynomial $x^{n_s}-1$ over the field $F$. But the polynomial $x^{n_s}-1$ has at most $n_s$ distinct roots, i.e. $n\le n_s$. But $n_s\le n$, so in fact $n_s=n$. This shows $G\cong C_{n_s}$, i.e. the group $G$ is cyclic.

???+ note "Corollary"
    The multiplicative group of a finite field $\mathbf F_q$ satisfies $\mathbf F_q^\times\cong C_{q-1}$.

The cyclic group $\mathbf F_q^\times$ has $\varphi(q-1)$ generators, which are called the primitive elements of the finite field; here $\varphi(n)$ is [Euler's totient function](../number-theory/euler-totient.md).

???+ abstract "Primitive element"
    A generator of the multiplicative group of a finite field $\mathbf F_q$ is called a **primitive element** of $\mathbf F_q$.

??? warning "A primitive element of a simple extension and a primitive element of a finite field are not the same"
    Although a primitive element of a simple extension and a primitive element of a finite field share the same name, they are not the same. A primitive element of a simple extension is a generator of the corresponding simple extension, while a primitive element of a finite field is a generator of the corresponding multiplicative group (as a cyclic group). A primitive element of a finite field regarded as a simple extension of its prime subfield need not be a primitive element of the finite field itself. For example, in $\mathbf F_{25}\cong\mathbf F_5[x]/(x^2+x+1)$, $\overline x$ is a primitive element of the field extension, but it is not a primitive element of the field $\mathbf F_{25}$, since its order is $3$.

??? warning "A primitive element of $\mathbf F_{q}$ and a primitive root modulo $q$ are also not the same"
    For a finite field $\mathbf F_{q}$ of odd characteristic, a [primitive root](./ring-theory.md#应用整数同余类的乘法群) modulo $q$ always exists. However, it should not be confused with a primitive element of the finite field $\mathbf F_{q}$. Although both are generators of the corresponding multiplicative structure regarded as a cyclic group, $(\mathbf Z/q\mathbf Z)^\times$ and $\mathbf F_q$ are not the same when $q$ itself is not a prime. For example, the order of the former is $\varphi(q)$ while that of the latter is $q-1$, so the sizes of the two multiplicative groups already differ.

Let $\alpha$ be a primitive element of the finite field $\mathbf F_q$. Then for every nonzero element $x\in\mathbf F_q^\times$ there exists a unique natural number $k<q-1$ such that $x=\alpha^k$; this $k$ is called the **discrete logarithm** of the element $x$ of $\mathbf F_q$ with respect to the base $\alpha$. As in the case of $\mathbf F_p$, the [algorithms for the discrete logarithm](../number-theory/discrete-logarithm.md) all have fairly high complexity.

Through multiplication alone, a primitive element already generates all nonzero elements of the field. This shows that a finite field, as an extension of its subfields, is always a simple extension.

???+ note "Theorem"
    For a finite field $\mathbf F_q$, let $F$ be a subfield of $\mathbf F_q$. Then $\mathbf F_q$ is a simple algebraic extension of $F$; moreover, if $\alpha$ is a primitive element of $\mathbf F_q$, then $\mathbf F_q=F(\alpha)$.

The minimal polynomial of a primitive element is an irreducible polynomial over the subfield of the finite field.

### Containment relations

The subfields of a finite field are also finite fields. The containment relations between finite fields are also completely determined by their orders.

???+ note "Theorem"
    Let $\mathbf F_q$ and $\mathbf F_r$ be finite fields. Then $\mathbf F_r$ is a subfield of $\mathbf F_q$ if and only if there exists $k$ such that $q=r^k$. In other words, $\mathbf F_{p^d}$ is a subfield of $\mathbf F_{p^n}$ if and only if $d\mid n$.

??? note "Proof"
    If $\mathbf F_r$ is a subfield of $\mathbf F_q$, then the two necessarily have the same characteristic $p$. The field extensions $\mathbf F_q/\mathbf F_r$, $\mathbf F_r/\mathbf F_p$, and $\mathbf F_q/\mathbf F_p$ are all simple algebraic extensions; denote their degrees by $k,d,n$ respectively. Then the degrees necessarily satisfy $n=kd$. Moreover, $r=p^d$ and $q=p^n$, so $q=p^n=p^{kd}=(p^d)^k=r^k$.
    
    Conversely, we must show that for every $d\mid n$, $\mathbf F_{p^d}$ is a subfield of $\mathbf F_{p^n}$. Write $r=p^d$ and $q=p^n$. Let $F$ be the set of all roots of the equation $x^r-x=0$ in the finite field $\mathbf F_q$. Using the Frobenius endomorphism one can show that the set $F$ necessarily forms a field; the key is to show that there are exactly $r$ such roots, so that $F\cong\mathbf F_r$. Since $d\mid n$, we have $(p^d-1)\mid(p^n-1)$, so $(x^{p^d-1}-1)\mid(x^{p^n-1}-1)$, i.e. $(x^r-x)\mid (x^q-x)$. Therefore $x^r-x$ splits over $\mathbf F_q$, and hence has $r$ distinct roots in $\mathbf F_q$. This shows that $F\cong\mathbf F_r$ is a subfield of $\mathbf F_q$.

This theorem shows that the containment relations between the finite fields $\mathbf F_{p^n}$ correspond to the divisibility relations between the exponents $n$ in the orders $p^n$ of the fields. The lattice formed by all finite fields $\mathbf F_{p^n}$ of characteristic $p$ is thus isomorphic to the lattice formed by the integers $n$ under the divisibility relation. Of course, for operations such as the intersection of finite fields $\mathbf F_{p^n}$ to make sense, all fields of characteristic $p$ must be embedded in the algebraic closure of $\mathbf F_p$.

???+ note "Theorem"
    Let $F$ be the algebraic closure of $\mathbf F_p$. Then the set of roots of the polynomial $x^{p^n}-x$ in the field $F$ forms the finite field $\mathbf F_{p^n}$. We have:
    
    1.  $F=\bigcup_{n=1}^\infty\mathbf F_{p^n}$, i.e. the algebraic closure of $\mathbf F_p$ is the union of all finite fields of characteristic $p$;
    2.  The lattice formed by all finite fields $\mathbf F_{p^n}$ of characteristic $p$ under containment is isomorphic to the lattice formed by the integers $n$ under divisibility. In particular, the intersection of $\mathbf F_{p^n}$ and $\mathbf F_{p^m}$ is $\mathbf F_{p^n}\cap\mathbf F_{p^m}=\mathbf F_{p^{\gcd(n,m)}}$, and the smallest field containing both $\mathbf F_{p^n}$ and $\mathbf F_{p^m}$ is $\mathbf F_{p^n}\mathbf F_{p^m}=\mathbf F_{p^{\operatorname{lcm}(n,m)}}$.

??? note "Proof"
    The key is to prove the first part, i.e. that $\bigcup_{n=1}^\infty\mathbf F_{p^n}$ is the algebraic closure of $\mathbf F_p$. The second part is a simple consequence of the previous theorem on subfields of finite fields.
    
    Note that for any $\alpha\in\bigcup_{n=1}^\infty\mathbf F_{p^n}$ there necessarily exists $n\in\mathbf N_+$ such that $\alpha\in\mathbf F_{p^n}$, so $\alpha$ is an algebraic element over $\mathbf F_p$; hence $\bigcup_{n=1}^\infty\mathbf F_{p^n}$ is an algebraic extension of $\mathbf F_p$. Any polynomial $f(x)$ of degree $m$ over $\mathbf F_p$ has at most $m$ distinct roots $\{\alpha_i\}_{i=1}^m$ in the algebraic closure $F$. Let the degree of the minimal polynomial of the root $\alpha_i$ be $n_i$; then $\alpha_i$ is necessarily contained in the field $\mathbf F_{p^{n_i}}$. Hence all roots of $f(x)$ lie in $\bigcup_{n=1}^\infty\mathbf F_{p^n}$, i.e. $f(x)$ splits over $\bigcup_{n=1}^\infty\mathbf F_{p^n}$. By the definition of the algebraic closure, $\bigcup_{n=1}^\infty\mathbf F_{p^n}$ is exactly the algebraic closure of $\mathbf F_p$.

### Automorphism group

The subfields of a finite field $\mathbf F_q$ are all sets of roots of polynomials of the form $x^r-x$. In other words, they are all sets of fixed points of some map $x\mapsto x^r$. This actually reveals a deep correspondence between the subfields of a finite field and the subgroups of its automorphism group.

Every field of characteristic $p$ has the Frobenius endomorphism $\sigma_p:x\mapsto x^p$. In the case of a finite field $\mathbf F_q$, this is also an automorphism; this shows that all finite fields $\mathbf F_q$ are perfect fields. The automorphism group of the field $\mathbf F_q$ is the cyclic group $\langle \sigma_p\rangle$ of order $n$, and one of its generators is the Frobenius endomorphism $\sigma_p$.

???+ note "Theorem"
    The automorphism group $\operatorname{Aut}(\mathbf F_q)=\langle\sigma_p\rangle$ of a finite field $\mathbf F_q$ is a cyclic group of order $n$, and the generator $\sigma_p$ is the Frobenius endomorphism $x\mapsto x^p$.

??? note "Proof"
    First, the Frobenius endomorphism $\sigma_p$ is an automorphism of the finite field $\mathbf F_q$, since an injection on a finite set is necessarily also a surjection. Therefore $\sigma_p\in\operatorname{Aut}(\mathbf F_q)$.
    
    Next, the order of $\sigma_p$ is $n$. This is because for all $x\in\mathbf F_q$ we have $\sigma_p^n(x)=x^{p^n}=x$, so $\sigma_p^n$ is the identity map; and for any $k<n$, $\sigma_p^k$ is not the identity map, since otherwise all elements of $\mathbf F_q$ would have to be roots of $x^{p^k}-x$, which is impossible.
    
    Finally, $\operatorname{Aut}(\mathbf F_q)$ has at most $n$ elements. Let $\alpha$ be a primitive element of $\mathbf F_q$; then an automorphism $\sigma\in \operatorname{Aut}(\mathbf F_q)$ is uniquely determined by its value $\sigma(\alpha)$ at $\alpha$. But $\sigma$ must map $\alpha$ to one of its conjugates; otherwise $\alpha$ and $\sigma(\alpha)$ would no longer be roots of the same minimal polynomial. There are only $n$ such conjugates, which shows that $\operatorname{Aut}(\mathbf F_q)$ also has at most $n$ elements.
    
    Therefore, the $n$ elements of $\operatorname{Aut}(\mathbf F_q)$ are exactly those of $\langle\sigma_p\rangle$. This proves the theorem.

The subgroups of the automorphism group $\operatorname{Aut}(\mathbf F_q)$ are in one-to-one correspondence with the subfields of the finite field $\mathbf F_q$.

???+ note "Theorem"
    Let $\mathbf F_q$ be a finite field, $\mathcal F$ the set of all its subfields, and $\mathcal G$ the set of all subgroups of its automorphism group $\operatorname{Aut}(\mathbf F_q)$. Then:
    
    1.  For $F\in\mathcal F$, let $\operatorname{Aut}(\mathbf F_q/F)$ be the set of automorphisms in $\operatorname{Aut}(\mathbf F_q)$ that fix $F$, i.e. $\operatorname{Aut}(\mathbf F_q/F)=\{\sigma\in\operatorname{Aut}(\mathbf F_q):\forall x\in F(\sigma(x)=x)\}$; then $\operatorname{Aut}(\mathbf F_q/F)\le\operatorname{Aut}(\mathbf F_q)$;
    2.  For $G\in\mathcal G$, let $F^G$ be the intersection of the fixed-point sets of all automorphisms in $G$, i.e. $F^G=\{x\in\mathbf F_q:\forall\sigma\in G(\sigma(x)=x)\}$; then $F^G$ is a subfield of $\mathbf F_q$;
    3.  The maps $F\rightarrow\operatorname{Aut}(\mathbf F_q/F)$ and $G\rightarrow F^G$ are inverse to each other and form a one-to-one correspondence between $\mathcal F$ and $\mathcal G$;
    4.  This one-to-one correspondence maps the extension relation between subfields to the containment relation between subgroups, i.e. for any $F_1\subseteq F_2$ we have $\operatorname{Aut}(\mathbf F_q/F_2)\le\operatorname{Aut}(\mathbf F_q/F_1)$.

This result is a special case of the fundamental theorem of general Galois theory; it connects field extensions with the content of group theory, so that problems about field extensions can be solved by the methods of group theory.

### Irreducible polynomials

The irreducible polynomials over a finite field $\mathbf F_q$ are very easy to determine. Since every irreducible polynomial of degree $n$ over the finite field $\mathbf F_q$ corresponds to an algebraic extension of degree $n$, and such an extension is unique, the roots of all irreducible polynomials of degree $n$ can be found in $\mathbf F_{q^n}$. This shows that an irreducible polynomial of degree $n$ over $\mathbf F_q$ is necessarily a factor of $x^{q^n}-x$. To determine all irreducible polynomials of degree $n$ over the finite field $\mathbf F_q$, one needs to study the factorization of $x^{q^n}-x$ over $\mathbf F_q$. This is very similar to the case of cyclotomic polynomials.

The algebraic elements over a finite field $\mathbf F_q$ can be classified by the degree of their minimal polynomial. Let $P_n$ be the set of algebraic elements whose minimal polynomial has degree exactly $n$; then

$$
\mathbf F_{q^n} = \bigcup_{d\mid n}P_d.
$$

This corresponds to the factorization

$$
x^{q^n}-x = \prod_{d|n}\prod_{\zeta\in P_d}(x-\zeta).
$$

Since an irreducible polynomial of degree $n$ has $n$ roots, and the minimal polynomials of these roots all have degree $n$, an irreducible polynomial of degree $n$ is necessarily a factor of the polynomial

$$
\prod_{\zeta\in P_n}(x-\zeta) = \prod_{d\mid n}\left(x^{q^d}-x\right)^{\mu(n/d)}
$$

This expression is obtained by applying [Möbius inversion](../number-theory/mobius.md) to the preceding factorization. Since the degree of this polynomial is

$$
\sum_{d\mid n}\mu(d)q^{n/d},
$$

the number of irreducible monic polynomials of degree $n$ over $\mathbf F_q$ is

$$
\frac1n\sum_{d\mid n}\mu(d)q^{n/d}
$$

This is exactly the number of aperiodic necklaces of length $n$ that can be made from beads of $q$ colors, counted up to rotation ([proof](../combinatorics/polya.md#cyclic-group)), so this polynomial is also called the necklace polynomial.

???+ note "Theorem"
    Over a finite field $\mathbf F_q$ there exist irreducible polynomials of every degree.

Since irreducible polynomials over a finite field have a simple structure, factoring polynomials over a finite field is very easy. For example, to determine all irreducible factors of degree $n$ of a given polynomial, it suffices to compute the greatest common divisor of the given polynomial and $x^{q^n}-x$[^ddf]. Similarly, if a polynomial of degree $n$ is coprime to the polynomial $x^{q^k}-x$ for all $k<n$, one can conclude that this polynomial of degree $n$ is irreducible over $\mathbf F_q$.

As pointed out above, a root of an irreducible polynomial over a finite field need not be a primitive element of the corresponding extension field regarded as a finite field. The minimal polynomial of a primitive element of the finite field $\mathbf F_q$ over its prime subfield $\mathbf F_p$ is also called a **primitive polynomial**[^prim-poly] over the field $\mathbf F_p$. Implementing the extension field with such a polynomial guarantees that $\overline x$ is necessarily a primitive element of the extension field. Primitive polynomials of degree $n$ over the field $\mathbf F_p$ can be obtained by factoring the cyclotomic polynomial $\Phi_{p^n-1}(x)$ over $\mathbf F_p$.

???+ note "Theorem"
    Let $p$ be a prime, $n$ a positive integer, and $p\perp n$. Furthermore, let $d$ be the order of the element $p$ in the multiplicative group $(\mathbf Z/n\mathbf Z)^\times$. Then the cyclotomic polynomial $\Phi_n(x)$ factors over the field $\mathbf F_p$ into a product of $\dfrac{\varphi(n)}{d}$ irreducible polynomials of degree $d$ over $\mathbf F_p$; moreover, these factors are primitive polynomials if and only if $n=p^d-1$. In particular, the cyclotomic polynomial $\Phi_n(x)$ is irreducible over the field $\mathbf F_p$ if and only if $p$ is a primitive root modulo $n$.

??? note "Proof"
    If we note that the roots of the $n$-th cyclotomic polynomial are all the primitive $n$-th roots of unity over $\mathbf F_p$, and that the degree $d$ of the minimal polynomial of a primitive $n$-th root of unity is the number of its conjugates (including itself), which equals the length of its orbit under the automorphism group $\langle\sigma_p\rangle$, then we see that $d$ is the orbit length of the cyclic subgroup generated by the map $\zeta^i\mapsto\zeta^{ip}$ on $\{\zeta^i:i\perp n\}$, i.e. the order of the element $p$ in the multiplicative group $(\mathbf Z/n\mathbf Z)^\times$. If one does not want to rely on Galois theory, this can also be proved by showing that $d$ is the smallest positive integer such that $(x^n-1)\mid(x^{p^d-1}-1)$. The remaining claims are obvious.

Although irreducible polynomials are important for implementing finite fields, there is no good deterministic method for finding an irreducible polynomial of degree $n$ over a finite field $\mathbf F_q$. In general, such an irreducible polynomial can be generated by a randomized method. Since among all monic polynomials of degree $n$ the irreducible ones make up a proportion of $\Theta(1/n)$, one can randomly generate a monic polynomial of degree $n$ and then test whether it is reducible. In this way, an irreducible polynomial is found after generating an expected $\Theta(n)$ monic polynomials. Of course, an irreducible polynomial generated in this way need not be primitive, and its coefficients need not be simple. In practice, if the size of the finite field is given in advance, one can often look up a table[^list-prim-poly] to find a primitive polynomial with simple coefficients, which makes subsequent computations more convenient.

### Reference implementation

This section provides a naive implementation of finite fields, for reference only. The code implements the randomized method of generating an irreducible polynomial.

??? example "Reference implementation"
    ```cpp
    --8<-- "docs/math/code/finite-field/finite-field_1.cpp"
    ```

The finite fields most used in cryptography are those of characteristic $2$. For such finite fields, the elements of the field can be stored as bit strings, and the field operations can be implemented with bit operations.

## Applications

This section lists some applications of field extensions in algorithm competitions. The main situation is that when evaluating an arithmetic expression over a field, one needs to introduce in the intermediate steps some elements that do not exist in the original field, so that direct computation becomes possible. Readers should be familiar with using complex numbers to solve problems about real numbers, which is an example of an extension of the field of real numbers; what readers are probably less familiar with are extensions of finite fields. Therefore, we mainly discuss extensions of finite fields here, especially extensions of the prime field $\mathbf F_p$.

In some cases a field extension reduces the complexity of the computation and is therefore necessary, for example the [fast Fourier transform](../poly/fft.md) over the field of real numbers; in other cases a field extension is only one of many methods for solving the problem, and there are usually methods of similar complexity that avoid field extensions, for example the computation of the Fibonacci sequence discussed next. While understanding these applications, readers should compare the advantages and disadvantages of the different methods, so as to be able to choose an appropriate method when solving problems.

### Fibonacci sequence

For computing the [Fibonacci sequence](../combinatorics/fibonacci.md), the common methods are the $O(n)$ linear recurrence and the $O(\log n)$ matrix exponentiation. In fact, it can also be solved by the method of field extensions, with time complexity likewise $O(\log n)$. The Fibonacci sequence has the closed-form formula:

$$
f(n) = \frac{1}{\sqrt{5}}\left(\left(\frac{1+\sqrt{5}}{2}\right)^n-\left(\frac{1-\sqrt{5}}{2}\right)^n\right).
$$

Now we want to compute the value of $f(n)$ modulo a prime $p\neq 5$[^fib-p5]. To convert this problem into a computation in the finite field $\mathbf F_p$, the first thing to settle is the meaning of $\sqrt 5$ in $\mathbf F_p$. From an algebraic point of view, it is the square root of the element $5$. Therefore, if a square root of $5$ exists in $\mathbf F_p$, i.e. when $5$ is a quadratic residue modulo $p$, one can directly compute this square root and substitute it into the computation; otherwise, one needs to compute in the extension field $\mathbf F_p(\sqrt 5)\cong\mathbf F_p[x]/(x^2-5)$.

Of course, when computing in an extension field, it is not necessary to adjoin exactly $\sqrt 5$. For example, for the Fibonacci sequence one can also let $\phi$ be a root of the polynomial $x^2-x-1$, so that $f(n)$ can be written as

$$
f(n)=\frac{\phi^n-(-\phi)^{-n}}{2\phi-1}=\frac{\phi^n-(1-\phi)^n}{2\phi-1}.
$$

If $5$ is not a quadratic residue modulo $p$, the polynomial $x^2-x-1$ is irreducible. In this case one can compute in the extension field $\mathbf F_p(\phi)\cong\mathbf F_p[x]/(x^2-x-1)$ and obtain the same result as above.

The method for computing the Fibonacci sequence can of course be generalized to other situations. However, one thing should be noted: the irreducibility of polynomials over a finite field does not agree with that over the field of rational numbers. For example, $x^4-10x^2+1$ is irreducible over $\mathbf Q$, and the corresponding splitting field is $\mathbf Q(\sqrt 2+\sqrt 3)=\mathbf Q(\sqrt 2,\sqrt 3)$; but in $\mathbf F_p$, if neither $2$ nor $3$ is a quadratic residue modulo $p$, it is the product of two irreducible polynomials, i.e. the square root $\sqrt{3}$ already exists in the extension field $\mathbf F_p(\sqrt 2)$ and no further extension is needed.

### Generalization to “extensions” of rings

As shown in the previous section, field extensions have all kinds of restrictions. For the computation of the Fibonacci sequence, the method of extension fields alone can only handle the case where the modulus $p$ is a prime and $5$ is not a quadratic residue modulo $p$. However, note that the discussion in the section on [algebraic extensions](#algebraic-extensions) shows that if division is not required in the extended structure, then rings can be extended as well[^ring-extension]. This section briefly discusses this method, using the computation of the Fibonacci sequence modulo an arbitrary $m$ as an example. In other common situations that do not involve much division, such as computing determinants, the fast Fourier transform, and so on, one can also try to apply this method when necessary.

Let $m$ be an arbitrary positive integer and $f(n)$ the $n$-th term of the Fibonacci sequence. The problem is to compute the value of $f(n)\bmod m$. In principle, one needs to compute in $\mathbf Z/m\mathbf Z$. However, as shown in the previous section, for different moduli the reducibility of the polynomial $x^2-x-1$ and whether it has repeated roots differ, so the closed-form formula for the Fibonacci sequence may differ considerably. Moreover, if $\mathbf Z/m\mathbf Z$ itself is not a field, the elements after extension often have no valid inverse (for example, modulo $5$ the denominator $\sqrt 5$ is simply zero). Despite these many problems, it actually suffices, with coefficients reduced modulo $m$, to compute the constant term of the remainder

$$
(1-x)^n-x^n\mod{x^2-x-1}
$$

Comparing with the closed-form formula above, the validity of this approach is obvious: this seems to be exactly computing the value of

$$
f(n)=\frac{(1-\phi)^n-\phi^n}{1-2\phi}
$$

in the "extension" $(\mathbf Z/m\mathbf Z)[x]/(x^2-x-1)$, where $\phi$ is a root of $x^2-x-1$.

Although not quite as obvious, this approach is also valid. Note that in the extension $\mathbf Q(\phi)\cong\mathbf Q[x]/(x^2-x-1)$ of the field of rational numbers, the closed-form formula holds. This shows that in $\mathbf Q[x]$,

$$
(1-x)^n-x^n \equiv f(n)(1-2x) \pmod{x^2-x-1}
$$

holds. This involves only polynomials with integer coefficients, so it also holds in $\mathbf Z[x]$. Writing it as a division with remainder and reducing the coefficients on both sides modulo $m$, we obtain an identity in $(\mathbf Z/m\mathbf Z)[x]$. This conclusion holds for arbitrary $m$.

In general, if some expression can be computed in an extension field of the field of rational numbers $\mathbf Q$, then by clearing denominators one can certainly obtain a statement in $\mathbf Z[x]$, and then reducing modulo $m$ gives a statement in $(\mathbf Z/m\mathbf Z)[x]$. The key to making this approach work is that the step of clearing denominators must not have "irreparable" consequences. For example, in the computation of the Fibonacci sequence, if instead of the constant term one used the coefficient of the linear term, then since this coefficient has a factor of $2$, the number $2$ has no inverse when the modulus $m$ is even, and the value of $f(n)$ cannot be recovered; as another example, again in the computation of the Fibonacci sequence, if one used the closed-form formula with the term $(-\phi)^{-n}$, then the step of clearing denominators would introduce factors that are hard to handle, so that no conclusion could be drawn from the result after reduction. Therefore, the choice of the computation procedure is the key to being able to apply this technique.

### Cipolla's algorithm

This is a typical example of computing in an extension of a finite field. For a quadratic residue $a$ modulo $p\neq 2$, we want to find its square root, i.e. an $x$ such that $x^2\equiv a\pmod p$. Although this is a problem over $\mathbf F_p$, [Cipolla's algorithm](../number-theory/quad-residue.md#cipollas-algorithm) computes in the finite field $\mathbf F_{p^2}$. This section explains the algorithm in the language of field theory. For a proof using elementary number theory, see the linked page.

Specifically, Cipolla's algorithm first chooses $r$ such that $r^2-a$ is a quadratic non-residue modulo $p$, which means that $x^2-(r^2-a)$ is an irreducible polynomial. Therefore, letting $u=r^2-a$, one can consider the extension field $\mathbf F_p(\sqrt u)$. Since the Frobenius endomorphism can only map an element to one of its conjugates, and such a conjugate is unique in a quadratic extension, we have $(r-\sqrt u)^p=r+\sqrt u$. Hence $(r-\sqrt u)^{p+1}=(r+\sqrt u)(r-\sqrt u)=r^2-u=a$. Therefore, to determine the square root, it suffices to compute $(r-\sqrt u)^{(p+1)/2}$. This value necessarily lies in $\mathbf F_p$, since the splitting field of $x^2-a$ is $\mathbf F_p$ itself.

## Exercises

Finally, we list some problems that directly apply the content of this article, to deepen understanding. Note, however, that much of this content is not a regular topic in algorithm competitions.

-   Cyclotomic polynomials:
    -   [Luogu P1520 因式分解 (Factorization)](https://www.luogu.com.cn/problem/P1520)
    -   [Gym102114C Call It What You Want](https://codeforces.com/gym/102114/problem/C)
-   Finite fields:
    -   [Luogu P3923 大学数学题 (University Math Problem)](https://www.luogu.com.cn/problem/P3923)
    -   [\[COTS 2021\] 菜 Jelo](https://www.luogu.com.cn/problem/P11192)
    -   [CF1310F. Bad Cryptography](https://codeforces.com/problemset/problem/1310/F)
    -   [LOJ 178. 多项式求根 (Roots of a Polynomial)](https://loj.ac/p/178)
-   Field extensions:
    -   [\[Oleksandr Kulkov Contest 2\] Problem A. Square Root Partitioning](https://codeforces.com/gym/102354/problem/A)
    -   [CF1103E. Radix Sum](https://codeforces.com/problemset/problem/1103/E)

## References and notes

-   Dummit, D.S. and Foote, R.M. (2004) Abstract Algebra. 3rd Edition, John Wiley & Sons, Inc.
-   [Milne, J.S. Fields and Galois Theory.](https://www.jmilne.org/math/CourseNotes/FT.pdf)
-   [Factorization of polynomials - Wikipedia](https://en.wikipedia.org/wiki/Factorization_of_polynomials)
-   [Factorization of polynomials over finite fields - Wikipedia](https://en.wikipedia.org/wiki/Factorization_of_polynomials_over_finite_fields)
-   [Cyclotomic Polynomial - Wikipedia](https://en.wikipedia.org/wiki/Cyclotomic_polynomial)
-   [Brett Porter's Notes on Cyclotomic Polynomials](https://www.whitman.edu/documents/academics/majors/mathematics/2015/Final%20Project%20-%20Porter%2C%20Brett.pdf)
-   [Jordan Bell's Notes on Cyclotomic Polynomials](https://jordanbell.info/LaTeX/mathematics/cyclotomic/cyclotomic.pdf)
-   [Michel Waldschmidt. An introduction to the theory of finite fields](https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/FiniteFields.pdf)
-   [Finite Field Arithmetic - Wikipedia](https://en.wikipedia.org/wiki/Finite_field_arithmetic)

[^subfield-one]: This is because the unity $1_E$ of the field $E$ necessarily satisfies the relation $x^2-x=0$ over $F$, and the latter has only two roots $0_F$ and $1_F$ in the field $F$; since the definition of a field requires $1_E\neq 0_E$, necessarily $1_E=1_F$ and $0_E=0_F$.

[^initial-object-ring]: In the language of category theory, $\mathbf Z$ is the [initial object](https://en.wikipedia.org/wiki/Initial_and_terminal_objects) of the category of rings with unity.

[^polynomial-universal]: Strictly speaking, this refers to the [universal property](https://en.wikipedia.org/wiki/Polynomial_ring#Polynomial_evaluation) of the polynomial ring $R[x]$.

[^multi-poly-ring]: The polynomial ring here has infinitely many indeterminates. To define such a polynomial ring, one first has to define monomials. Let $X$ be the set of indeterminates; the monomials over it are all functions $\alpha:X\rightarrow\mathbf N$ that are nonzero at only finitely many indeterminates, which can be written as $x_{i_1}^{\alpha(i_1)}\cdots x_{i_k}^{\alpha(i_k)}$, where $i_1,\cdots,i_k$ are the indices of all indeterminates at which $\alpha$ is nonzero. Polynomials are all linear combinations of finitely many monomials. Under suitably defined addition and multiplication, they form a ring. For the case of finitely many indeterminates, one can show that this definition agrees with the result of the recursive definition in the section on [multivariate polynomial rings](./ring-theory.md#多元多项式环).

[^fundamental-algebra]: Although it is called the fundamental theorem of algebra, this result is not purely algebraic, since the construction of the field of real numbers requires a topological structure.

[^ddf]: This statement is not entirely rigorous, since irreducible factors of degree $d\mid n$ are also obtained. However, since in implementations of the algorithm one usually separates factors starting from smaller degrees, by the time the irreducible factors of degree $n$ are separated, the smaller factors should already have been separated, so this statement is acceptable.

[^prim-poly]: Do not confuse this name with the primitive polynomials of polynomial theory (i.e. polynomials whose coefficients have greatest common divisor one).

[^list-prim-poly]: For example, the appendix of [Hansen, T., & Mullen, G. L. (1992). Primitive polynomials over finite fields. Mathematics of computation, 59(200), 639-643](https://www.ams.org/journals/mcom/1992-59-200/S0025-5718-1992-1134730-7/S0025-5718-1992-1134730-7.pdf) provides such a list.

[^fib-p5]: When $p=5$, the characteristic equation $x^2-x-1=0$ of the Fibonacci sequence has the double root $x=3$, so in $\mathbf F_5$ the closed-form formula for the Fibonacci sequence is $f(n)=n3^{n-1}$.

[^ring-extension]: The so-called extension of a ring usually has two meanings: one is the [generalization of group extensions](https://en.wikipedia.org/wiki/Algebra_extension), the other is the [generalization of field extensions](https://en.wikipedia.org/wiki/Subring#Ring_extensions). This article refers to the second meaning. More specifically, the extensions involved in this section are all [integral extensions](https://en.wikipedia.org/wiki/Integral_element#Integral_extensions) of commutative rings with unity, which is the generalization of the notion of algebraic extensions of fields to commutative rings with unity.
