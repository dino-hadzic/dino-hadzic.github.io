---
title: Introduction to modular arithmetic
---

In algorithm competitions, an important component of number theory is **modular arithmetic**, that is, performing all kinds of integer operations under some modulus. Besides the basic four arithmetic operations and exponentiation, one can also conveniently take logarithms, extract roots of various orders, compute factorials and binomial coefficients, and so on.

Modular arithmetic appears in all kinds of problems, not only in the number theory part. The actual answer to many problems may be very large and exceed the range of common integer types. In that case, to avoid introducing big-integer arithmetic and printing long numbers, problems often require the answer to be printed modulo some number. This requires a solid command of all kinds of modular arithmetic techniques.

## Integer division and modulo in C/C++

In C/C++, integer division and the modulo operation are inconsistent with the division and modulo customary in mathematics.

For all standard versions of C/C++, it is specified that in integer division:

1.  when the divisor is 0, the behavior is undefined;
2.  otherwise, the result of `(a / b) * b + a % b` equals `a`.

In other words, the sign of the modulo operation depends on how division rounds, and how division rounds is implementation-defined (decided by the compiler).

Starting from the [C99](https://en.cppreference.com/w/c/language/operator_arithmetic) and [C++11](https://en.cppreference.com/w/cpp/language/operator_arithmetic) versions of the standards, it is specified that **the quotient is rounded toward zero** (the fractional part is discarded); the sign of the modulo is then the same as that of the dividend. Since then, the following assertions are guaranteed to be true:

```c
assert(5 % 3 == 2);
assert(5 % -3 == 2);
assert(-5 % 3 == -2);
assert(-5 % -3 == -2);
```

## Modular integer class

Modular arithmetic can be viewed as performing all kinds of operations on the [congruence classes](./basic.md#congruence-classes-and-residue-systems) under some modulus. If a struct is used to represent a congruence class, and addition, subtraction, multiplication and other operations between congruence classes are encapsulated as methods of the struct or as operator overloads, then modular arithmetic can be naturally implemented as a modular integer class. Below is a simple example that supports addition, subtraction, multiplication and binary exponentiation of $32$-bit signed integers under a modulus $M < 2^{30}$:

???+ example "A simple modular integer class"
    ```cpp
    --8<-- "docs/math/code/mod-arithmetic/mod-arithmetic.cpp:core"
    ```

This implementation deliberately reduces the number of modulo operations, because a modulo operation is usually much more expensive than an ordinary addition, subtraction, multiplication or comparison. The code comments provide equivalent and more direct implementations. The main idea of these simple optimizations is that when two integers in $[0,M)$ are added or subtracted, the result certainly falls in the interval $(-M,2M)$, so it can be adjusted back into the interval $[0,M)$ by one addition or subtraction. The exponentiation in this implementation uses the technique of [binary exponentiation](../binary-exponentiation.md#modular-exponentiation).

Besides these basic operations, the following operations can also be performed under various moduli:

-   [inverse](./inverse.md)
-   [division](./linear-equation.md)
-   [factorial](./factorial.md)
-   [binomial coefficients](./lucas.md)
-   [square root](./quad-residue.md#square-roots-in-modular-arithmetic)
-   [logarithm](./discrete-logarithm.md)
-   [roots](./residue.md#root-extraction-in-modular-arithmetic)

These operations are usually easier under a prime modulus. For a composite modulus, extended versions of the corresponding algorithms and the [Chinese remainder theorem](./crt.md) are often needed. Most of these modular operations can be viewed as solving some kind of congruence equation. For general methods of solving congruence equations, see the [Congruence equations](./congruence-equation.md) page.

## Related algorithms

This section introduces several methods for optimizing modulo, multiplication and binary exponentiation in the modular setting. For the vast majority of problems, the simple implementation given above is efficient enough. However, when a problem has strict requirements on the constant factor of the algorithm, these optimizations can come into play and further reduce the running time of the algorithm by cutting unnecessary computations and modulo operations.

### Fast multiplication

In primality testing and integer factorization, one often encounters modular multiplication with a modulus in the `long long` range. To avoid integer overflow during the computation, this section introduces a "fast multiplication" that handles a modulus in the `long long` range, does not need `__int128`, and has complexity $O(1)$. This algorithm requires that, on the judge system, `long double` is represented as at least an $80$-bit extended-precision floating-point number[^long-double-80bit].

Suppose $0 \le a, b < m$ and we want to compute $ab\bmod m$. Notice that:

$$
ab\bmod m=ab-\left\lfloor \dfrac{ab}m \right\rfloor m.
$$

Using the natural overflow of `unsigned long long`:

$$
ab\bmod m=ab-\left\lfloor \dfrac{ab}m \right\rfloor m=\left(ab-\left\lfloor \dfrac{ab}m \right\rfloor m\right)\bmod 2^{64}.
$$

As long as we can compute the quotient $\left\lfloor\dfrac{ab}m\right\rfloor$, the multiplication and subtraction in the rightmost expression can be computed directly with `unsigned long long`.

Next, we only need to consider how to compute $\left\lfloor\dfrac {ab}m\right\rfloor$. The solution is to first compute $\dfrac am$ with `long double` and then multiply by $b$. Since `long double` is used, there will undoubtedly be precision errors. Suppose `long double` is represented as an $80$-bit extended-precision floating-point number (that is, $1$ sign bit, $15$ exponent bits and $64$ mantissa bits); then `long double` can represent at most $64$ significant bits exactly[^floating-format]. So in the worst case $\dfrac am$ goes wrong starting from bit $65$, and the error range[^ld-mul-err] is $\left(-2^{-64},2^{-64}\right)$. After multiplying by $b$, a $64$-bit signed integer, the error range is $(-0.5,0.5)$. To simplify the following discussion, we can first add $0.5$ and then round down; the final error range is $\{0,1\}$.

Finally, when substituting into the formula above, we need to multiply by $-m$, so the final error range is $\{0,-m\}$. Since $m$ is in the `long long` range, when the result $r\in[0,m)$ we return $r$ directly, and otherwise we return $r+m$.

The code implementation is as follows:

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/math/code/mod-arithmetic/i64-mul.cpp:ld-mul"
    ```

Nowadays, the C/C++ compilers on the vast majority of judge systems already support the `__int128` type[^int128], so one can also simply promote the type of the multiplicands to `__int128` and then take the modulo:

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/math/code/mod-arithmetic/i64-mul.cpp:i128-mul"
    ```

Of course, the modulo operation on `__int128` is not cheap either. If the constant factor needs to be squeezed further, consider the methods introduced in the next two sections.

### Barrett reduction

As mentioned above, division and modulo operations are usually more expensive than the other arithmetic operations. To reduce the cost of modulo operations, there are algorithms that obtain the same result without directly taking a modulo. The Barrett reduction algorithm introduced in this section is one of them.

Let $m$ be a fixed modulus, and suppose we want to compute $a\bmod m$ many times for different $a > 0$. By division with remainder,

$$
z = a\bmod m = a - \left\lfloor\dfrac{a}{m}\right\rfloor m.
$$

The key is the computation of the quotient $\left\lfloor\dfrac{a}{m}\right\rfloor$. Let $R$ be some constant; then[^floor-barrett]

$$
\left\lfloor\dfrac{a}{m}\right\rfloor = \left\lfloor a\dfrac{R}{m} / R\right\rfloor \approx \left\lfloor a\left\lfloor\dfrac{R}{m}\right\rfloor/R\right\rfloor.
$$

If we choose $R = 2^k$, then $\left\lfloor\dfrac{R}{m}\right\rfloor$ in the right-hand expression can be precomputed, and the division by $R$ can be done by a shift. So computing the quotient with the right-hand expression needs only one multiplication and one shift. Substituting into the expression for $a\bmod m$, we get an estimate $z'$ of the desired remainder.

Now we analyze the error of this approach. The [floor function](./basic.md#floor-and-ceiling-functions) has the property that for $x > y > 0$, $\lfloor x\rfloor - \lfloor y\rfloor \le \lceil x - y\rceil$. Therefore, the error

$$
\begin{aligned}
\Delta &= |z' - z| = m\left|\left\lfloor\dfrac{a}{m}\right\rfloor - \left\lfloor a\left\lfloor\dfrac{R}{m}\right\rfloor/R\right\rfloor\right|\\
&\le m\left\lceil a\left(\dfrac{R}{m} - \left\lfloor\dfrac{R}{m}\right\rfloor\right) /R\right\rceil \le m\left\lceil\dfrac{a}{R}\right\rceil.
\end{aligned}
$$

As long as $a \le R$, the error $\Delta$ does not exceed $m$. Since $z' \ge z$, the estimate $z'$ can only be $z$ or $z + m$. After obtaining the estimate, it suffices to subtract the extra $m$ when $z' \ge m$ to guarantee a correct answer.

In the computation of Barrett reduction, only two multiplications, one shift and at most two subtractions are used to complete the integer modulo. But the efficiency gain is not free: in fact, the intermediate variables involved in Barrett reduction are often longer than the input variables. It is easy to see that the longest intermediate variable in Barrett reduction is $a\left\lfloor\dfrac{R}{m}\right\rfloor$. Let $\ell(x)$ be the length of the binary representation of the integer $x$. Then

$$
\ell\left(a\left\lfloor\dfrac{R}{m}\right\rfloor\right) \approx \ell(a) + \ell(R) - \ell(m).
$$

Since the choice of $R$ must satisfy the condition $a \le R$, this length is at least $2\ell(a) - \ell(m)$. But when a modulo is needed, we generally have $\ell(m)\le\ell(a)$, so the length of this intermediate variable may be greater than the input length $\ell(a)$. For example, if a $64$-bit integer must be reduced modulo a $32$-bit integer, the intermediate variable actually needs a $64 \times 2 - 32 = 96$-bit integer.

One application of Barrett reduction is computing the remainder of a product, $ab\bmod m$. If one of the factors is fixed, say $b$, then

$$
ab\bmod m = ab - \left\lfloor a\left\lfloor\dfrac{bR}{m}\right\rfloor/R\right\rfloor m
$$

gives an estimate similar to the one above, and it suffices to precompute the value of $\left\lfloor\dfrac{bR}{m}\right\rfloor$. This case with fixed $b$ is sometimes also called Shoup's modular multiplication[^shoup].

The more common case is that $a, b$ are both not fixed. Then one must first compute the value of $ab$ and then use Barrett reduction to get $ab\bmod m$. For example, when implementing modular multiplication, we need to compute $ab\bmod m$ for $0 \le a,b < m$. Then the chosen $R$ must satisfy $ab \le R$. By the analysis above, the longest intermediate variable in the computation has length $2\ell(ab)-\ell(m)$. When $\ell(a)\approx\ell(b)\approx\ell(m)$, this length is $3\ell(m)$. In other words, if Barrett reduction is used to implement modular multiplication of $32$-bit integers, the intermediate variables need $96$-bit integers. This is one limitation of Barrett reduction in practical use in algorithm competitions.

As an example, a reference implementation of modular multiplication of $32$-bit signed integers using Barrett reduction is as follows:

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/math/code/mod-arithmetic/i32-mul.cpp:barrett"
    ```

The implementation needs $128$-bit integers[^int128].

### Montgomery multiplication

The function of the Montgomery multiplication algorithm is very similar to that of the Barrett algorithm: it can likewise reduce the cost of modulo operations in modular integer arithmetic. Unlike the previous two algorithms, which both approximate the quotient, Montgomery multiplication maps all integers into the Montgomery space, where operations are relatively easy, thereby lowering the overall computational cost.

Let the modulus $m$ be odd, and choose $R = 2^k > m$. Then the Montgomery form corresponding to the congruence class $a \bmod m$ is

$$
aR\bmod m.
$$

Since $R\perp m$, there is a bijection between the congruence class $a \bmod m$ and its Montgomery form $aR\bmod m$. Therefore, we can convert integers into Montgomery form, perform a number of operations modulo $m$, and then convert the resulting Montgomery form back into an integer; the result is always correct.

Many modular integer operations can be done conveniently using the Montgomery form. We have just explained that to compare whether two congruence classes are the same, it suffices to compare their Montgomery forms. Moreover, since

$$
(a\pm b)R\bmod m = ((aR\bmod m)\pm(bR\bmod m)) \bmod{m},
$$

addition and subtraction of congruence classes correspond to addition and subtraction of their Montgomery forms. However, to compute the product of congruence classes, one cannot directly multiply the two Montgomery forms. Since

$$
(ab)R\bmod m =  ((aR\bmod m)(bR\bmod m)R^{-1}) \bmod{m},
$$

when multiplying two Montgomery forms, the following **Montgomery reduction** operation must be applied to their product $x$:

$$
\operatorname{REDC}: x \mapsto xR^{-1}\bmod m.
$$

Using this operation, the Montgomery form of the product $ab$ is $\operatorname{REDC}((aR\bmod m)(bR\bmod m))$. The Montgomery reduction operation is the core operation of Montgomery multiplication:

-   Converting $a$ to its Montgomery form is $\operatorname{REDC}((a\bmod m)(R^2\bmod m))$.
-   Converting the Montgomery form of $a$ back to $a\bmod m$ is $\operatorname{REDC}(aR\bmod m)$.
-   The Montgomery form corresponding to the modular inverse $a^{-1}\bmod m$ is $\operatorname{REDC}((aR\bmod m)^{-1}(R^3\bmod m))$.

Now we discuss how to implement the Montgomery reduction operation $\operatorname{REDC}$. When computing $\operatorname{REDC}(x)$, we always assume $0 \le x < m^2$, which holds in all the cases above. Since $R\perp m$, by [Bézout's identity](./bezouts.md) there exist integers $R^{-1},m'$ such that

$$
RR^{-1} + mm' = 1.
$$

Therefore, letting $q=\lfloor xm' / R\rfloor$, we have

$$
\begin{aligned}
xR^{-1} &= x\dfrac{1 - mm'}{R} \equiv \dfrac{x-xmm' + qmR}{R} = \dfrac{x - m(xm'\bmod R)}{R} \pmod{m}.
\end{aligned}
$$

Since $0 \le x < m^2 < mR$ and $0 \le xm'\bmod R < R$, we have

$$
-m < \dfrac{x - m(xm'\bmod R)}{R} < m.
$$

That is, this quotient differs from $xR^{-1}\bmod m$ by at most one $m$. It suffices to add $m$ when the quotient is less than zero to obtain $\operatorname{REDC}(x)$. Computing this quotient needs only two integer multiplications, one integer subtraction and two bit operations (taking the modulo and dividing by $R=2^k$, respectively). Therefore, the Montgomery reduction operation can be performed efficiently.

To perform Montgomery multiplication, a series of constants must be precomputed. First, Montgomery reduction uses $m' = m^{-1}\bmod R$, which can be computed with the Newton–Hensel method introduced [below](#integer-class-modulo-a-power-of-2). Second, when reducing various operations to Montgomery reduction, constants such as $R^2\bmod m$ are also involved. To obtain it, compute $R\bmod m$ once, and adding it to itself gives $2R\bmod m$. Then, treating that as the Montgomery form of $2$ and directly applying binary exponentiation, we get $2^kR\bmod m = R^2\bmod m$.

As an example, an implementation of Montgomery multiplication for $32$-bit signed integers is as follows:

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/math/code/mod-arithmetic/i32-mul.cpp:montgomery"
    ```

Compared with implementing modular multiplication via Barrett reduction, the computation of Montgomery multiplication involves several steps: conversion, multiplication of Montgomery forms, inverse conversion, and so on. Therefore, only when the number of modular operations between the conversion and the inverse conversion is large enough can the cost of conversion and inverse conversion be amortized, yielding high overall efficiency. However, since the implementation of Montgomery multiplication only involves intermediate variables of length $2\ell(m)$, it is more flexible to implement. For example, modular multiplication of $32$-bit integers needs only $64$-bit intermediate variables. So if a modular integer class is needed for all kinds of number-theoretic computations, Montgomery multiplication is more suitable.

### Integer class modulo a power of 2

This section discusses the implementation of a modular integer class when the modulus is a power of $2$. In this special case, division and modulo operations can be implemented with bit operations and are very efficient. Both Barrett reduction and Montgomery multiplication exploit this property of $2^e$ as divisor and modulus to speed up computation. In particular, when the modulus is exactly a special number such as $2^{32}$ or $2^{64}$, a modular integer class can be implemented using unsigned integers of the corresponding width together with natural overflow, without any explicit modulo operation. Even when the modulus is not exactly of this kind, it can be reduced to the case of these special moduli. For example, when the modulus is $2^{58}$, the intermediate computations can be done modulo $2^{64}$, and the result is finally reduced modulo $2^{58}$. Besides the convenient modulo, the other operations of the integer class modulo $2^e$ also have many special implementations. This section focuses on the implementation of the inverse and exponentiation operations.

First, the inverse: given an odd $a$ and a modulus $m=2^e~(e > 2)$, we need to find $a^{-1}\bmod m$. Common methods for finding an inverse include the extended Euclidean algorithm and the binary exponentiation method. The extended Euclidean algorithm involves taking modulo with respect to a general modulus; the ordinary binary exponentiation method needs to compute $a^{\varphi(m)-1}\bmod{m}$, which requires $\Theta(e)$ integer multiplications. A more efficient method is the [Newton–Hensel method](../poly/newton.md). Concretely, consider applying the following result:[^newton-hensel]

$$
ax \equiv 1 \pmod{2^e} \implies ax(2 - ax) \equiv 1\pmod{2^{2e}}.
$$

According to this expression, starting from $x = 1$ and repeatedly applying $x \gets x(2-ax)$, we obtain $a^{-1}\bmod m$ after $\lceil\log_2 e\rceil$ iterations.

As an example, a reference implementation of the inverse of integers modulo $2^{32}$ is as follows:

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/math/code/mod-arithmetic/mod-32-inv-pow.cpp:inv"
    ```

Next, exponentiation: given $x,a,b$ and a modulus $m=2^e~(e > 2)$, we need to find $xa^b\bmod m$, where $a$ is odd. From the [analysis](./primitive-root.md#recursive-formula) of the multiplicative structure of integers modulo $2^e$, we know that $a$ can always be written in the form $\pm g^{\ell}$[^mod-2-g], and the minus sign appears if and only if $a\equiv 3\pmod 4$. In that case, we can replace $a$ by $-a$ and multiply the final result by $(-1)^b$. Therefore, in what follows we may assume that $a\equiv 1\pmod 4$ holds. Then the core idea of the algorithm is to write $a$ in the form $g^{L(a)}\bmod m$ and then compute the desired power as $xg^{bL(a)}\bmod m$.

Computing $L(a)$ means computing the discrete logarithm $\operatorname{ind}_ga$. Notice that as long as $a\equiv 1\pmod 4$, $a$ can always be written in the following form:

$$
a \equiv (2^{e_1}+1)(2^{e_2}+1)\cdots(2^{e_s}+1) \pmod{m},
$$

where $1 < e_1 < e_2 < \cdots < e_s < e$. This is because, by directly expanding this product, one finds that the second-lowest bit equal to $1$ in the binary representation of $a$ is exactly bit $e_1$ (indices start from $0$), and from this the representation can be found recursively. By the [properties](./discrete-logarithm.md#properties) of the discrete logarithm, we have

$$
4L(a) \equiv 4L(2^{e_1}+1) + 4L(2^{e_2}+1) + \cdots + 4L(2^{e_s}+1) \pmod{m}. 
$$

Since the modulus of the discrete logarithm equals the order $\delta_m(g)=2^{e-2}=m/4$, here we directly multiply the whole congruence by $4$ to ensure that the computation can be carried out in the residue classes modulo $m$. Thus, it suffices to precompute all $4L(2^d+1)$ for $1 < d < e$, and then the value of $4L(a)$ can be computed quickly.

Conversely, from $L(a)$ it is easy to obtain the value of $g^{L(a)}\bmod{m}$. By the [binomial theorem](../combinatorics/combination.md#binomial-theorem), for $1 < d < e$ we have

$$
\begin{aligned}
(2^d+1)^{2^{e-d}} \equiv 1 \pmod{m},\quad
(2^d+1)^{2^{e-d-1}} \equiv 1 + 2^{e-1} \pmod{m},
\end{aligned}
$$

so $\delta_m(2^d+1) = 2^{e-d}$. By the properties of the order,

$$
\delta_m(2^d+1) = \dfrac{\delta_m(g)}{\gcd(\delta_m(g), \operatorname{ind}_g(2^d+1))}.
$$

Therefore, $\gcd(\delta_m(g), \operatorname{ind}_g(2^d+1)) = 2^{d-2}$. This shows that $L(2^d+1) = \operatorname{ind}_g(2^d+1) = 2^{d-2}r$, where $2\nmid r$. So the lowest bit equal to $1$ in the binary representation of $4L(2^d+1)$ is exactly bit $d$ (indices start from $0$). Therefore, $4L(a)$ can likewise be decomposed recursively, via its binary representation, into a sum of terms of the form $4L(2^d+1)$. From this, the value of $a$ is obtained.

In a concrete implementation, there are some points that can be further optimized. First, decomposing $a$ into product form still requires division. It is more convenient to compute the decomposition of $a^{-1}$, i.e. to find $1 < e_1 < e_2 < \cdots < e_s < e$ such that

$$
a(2^{e_1}+1)(2^{e_2}+1)\cdots(2^{e_s}+1) \equiv 1 \pmod{m}
$$

holds. Again, $e_1$ is determined by finding the second-lowest bit equal to $1$, but to cancel the factor $2^{e_1}+1$ in $a^{-1}$, it suffices to multiply $a$ by $2^{e_1}+1$, which can be done with bit operations. Also, since $4L(a^{-1})=-4L(a)$, when accumulating $4L(a)$ we need to use subtraction instead of addition. Second, for a specially chosen base $g$, the iteration need not proceed to $d = e-1$; it suffices to proceed to $d = \lceil e/2\rceil - 1$. For this, we need to choose $g$ such that

$$
4L(2^{\lceil e/2\rceil} + 1) = 2^{\lceil e/2\rceil}.
$$

For $d \ge e / 2$, we have

$$
(2^d+1)^2 = 2^{2d} + 2^{d+1} + 1 \equiv 2^{d+1} + 1 \pmod{m}.
$$

So, by induction starting from $d = \lceil e/2\rceil$, we see that $4L(2^d+1)=2^d$ holds for all $d \ge e/2$. Furthermore, as long as $e/2 \le e_1 < e_2 < \cdots < e_s < e$, we have

$$
(2^{e_1}+1)(2^{e_2}+1)\cdots(2^{e_s}+1) \equiv 1 + 2^{e_1} + 2^{e_2} + \cdots + 2^{e_s} \pmod{m}
$$

and

$$
4L((2^{e_1}+1)(2^{e_2}+1)\cdots(2^{e_s}+1)) = 2^{e_1} + 2^{e_2} + \cdots + 2^{e_s}.
$$

Therefore, after processing all binary bits with $d < e/2$, the discrete logarithm of the remaining part can be obtained directly without bit-by-bit computation. With the first optimization, the whole exponentiation needs only $O(e)$ additions, subtractions and bit operations plus $1$ multiplication; with the second optimization, about half of the additions, subtractions and bit operations can be saved, but $1$ extra multiplication is needed.

As an example, a reference implementation of exponentiation of integers modulo $2^{32}$ is as follows:

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/math/code/mod-arithmetic/mod-32-inv-pow.cpp:pow"
    ```

The precomputation of the discrete logarithms can be done with the Pohlig–Hellman algorithm, and the base $g$ can be chosen as

$$
5^{\operatorname{ind}_5(2^{\lceil e/2\rceil}+1)/2^{\lceil e/2\rceil - 2}}\bmod{2^e}.
$$

## References and notes

-   [Fast modular multiplication by orz - Codeforces](https://codeforces.com/blog/entry/96759)
-   [Barrett Reduction - Wikipedia](https://en.wikipedia.org/wiki/Barrett_reduction)
-   [Barrett Reduction - A41](https://encrypt.a41.io/primitives/modular-arithmetic/modular-reduction/barrett-reduction#cost-analysis-of-modular-multiplication)
-   [Barrett 约减原理及正确性证明 by Chen - 知乎专栏](https://zhuanlan.zhihu.com/p/690876166) (Principle of Barrett reduction and proof of correctness, Zhihu)
-   [Montgomery Multiplication - CP Algorithms](https://cp-algorithms.com/algebra/montgomery_multiplication.html)
-   [Montgomery 模乘 by Chen - 知乎专栏](https://zhuanlan.zhihu.com/p/645428404) (Montgomery multiplication, Zhihu)
-   [Binary Exponentiation by Factoring - CP Algorithms](https://cp-algorithms.com/algebra/factoring-exp.html)
-   Barrett, Paul. "Implementing the Rivest Shamir and Adleman public key encryption algorithm on a standard digital signal processor." In Conference on the Theory and Application of Cryptographic Techniques, pp. 311-323. Berlin, Heidelberg: Springer Berlin Heidelberg, 1986.
-   Becker, Hanno, Vincent Hwang, Matthias J. Kannwischer, Bo-Yin Yang, and Shang-Yi Yang. "Neon NTT: Faster Dilithium, Kyber, and Saber on Cortex-A72 and Apple M1." IACR Transactions on Cryptographic Hardware and Embedded Systems (2022): 221-244.
-   Montgomery, Peter L. "Modular multiplication without trial division." Mathematics of computation 44, no. 170 (1985): 519-521.

[^long-double-80bit]: This applies to the GCC or Clang compilers on most 64-bit systems.

[^floating-format]: See [Extended precision - Wikipedia](https://en.wikipedia.org/wiki/Extended_precision).

[^ld-mul-err]: Here the condition $a < m$ is used, i.e. $a / m \in [0,1)$.

[^int128]: Among today's mainstream compiler environments, only MSVC on the Windows platform does not support the `__int128` type. If you need to write code compatible with multiple platforms, you can detect the MSVC environment via the macro `_MSC_VER`, and under that condition include the [`<intrin.h>`](https://learn.microsoft.com/en-us/cpp/intrinsics/x64-amd64-intrinsics-list?view=msvc-170) header and use the intrinsics it provides (such as `_umul128`) to implement 128-bit integer arithmetic indirectly (available only on 64-bit platforms).

[^floor-barrett]: Here $\left\lfloor\dfrac{R}{m}\right\rfloor$ can also be replaced by another integer estimate of $\dfrac{R}{m}$, such as the ceiling $\left\lceil\dfrac{R}{m}\right\rceil$ or rounding to the nearest integer $\left\lfloor\dfrac{R}{m}\right\rceil$, as long as the error-correction step for the estimate is adjusted accordingly.

[^shoup]: Shoup implemented this extension of Barrett reduction in his number theory library [NTL](https://libntl.org/), hence the name.

[^newton-hensel]: Direct verification: from $ax \equiv 1 \pmod{2^e}$ we can set $ax = 1 + \lambda 2^e$, and then $ax(2-ax) = (1+\lambda 2^e)(1-\lambda 2^e) = 1 - \lambda^2 2^{2e} \equiv 1\pmod{2^{2e}}$.

[^mod-2-g]: The page cited in the text only proves that $g$ can be taken to be $5$. In fact, by repeating that proof in full, one can show that $g$ can be any integer congruent to $5$ modulo $8$. The choice of $g$ is discussed later in the text.
