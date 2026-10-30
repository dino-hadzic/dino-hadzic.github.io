---
title: Base (positional notation)
---

A **positional numeral system**, also called a **carry system**, **base system**, **positional notation**, **place-value notation**, or **positional number system**, is a numeral system that can represent all natural numbers using a finite number of symbols. The number of symbols a positional system can use is called its **radix** or **base**; a positional system with base $n$ is called base $n$ ($n>1$); for example, the decimal system we use most often normally uses only the ten symbols `0, 1, 2, 3, 4, 5, 6, 7, 8, 9` to write numbers. A carry is the operation "when a digit of a number reaches the base, set it to 0 and add one to the digit in the next higher position".

In general, we write a number in base $n$ as $(a_k\cdots a_1a_0)_n$, $(a_k\cdots a_1a_0)_{(n)}$, ${a_k\cdots a_1a_0}_{(n)}$, ${a_k\cdots a_1a_0}_{n}$, etc. If the base is implied by the context, we may omit the subscript. Note that $a_k\cdots a_1a_0$ here is not the product of $k+1$ numbers but a sequence.

For a base-$k$ number $a_n\cdots a_1a_0$, the value it represents is $a_nk^n+\cdots+a_1k^1+a_0k^0=\sum_{i=0}^n a_ik^i$; for a number $m$ whose representation in base $k$ is $a_n\cdots a_1a_0$, we have:

$$
\begin{array}{cc}
    a_0=m-q_0k,&q_0=f(m/k),\\
    a_1=q_0-q_1k,&q_1=f(q_0/k),\\
    \vdots&\vdots\\
    a_n=q_{n-1}-q_nk,&q_n=f(q_{n-1}/k)=0,\\
\end{array}
$$

where $f(x)=\lfloor x\rfloor$.

The length of the representation of the number $n$ in base $k$ is $\lceil\log_k (n+1)\rceil$.

We usually represent fractions by adding a decimal point "$.$"[^note4], negative numbers by adding a minus sign "$-$", infinite repeating decimals by adding an overline over the final segment of the fractional part, etc. For readability, we may insert a separator (such as a space, $,$, `'`, etc.) every few digits; for example, $12~345$ denotes $12345$.

In computing, the more commonly used positional systems are binary, octal, and hexadecimal.

## Conversion between different bases

### Decimal to other bases

We demonstrate with binary as an example; the principle for other bases is similar.

For the integer part, repeatedly divide the decimal number by $2$ until the quotient is $0$, then take all the remainders from bottom to top; these are the digits of the integer part of the binary number. For the fractional part, multiply it by $2$ and take the integer part of the result, then repeat the computation with the resulting fractional part until the fractional part is all $0$; then take the integer parts of all the results from top to bottom; these are the digits of the fractional part of the binary number.

???+ example "Example"
    Convert $35.25$ to binary.
    
    Integer part:
    
    $$
    \begin{aligned}
        35/2&=17  &\dots 1,\\
        17/2&=8   &\dots 1,\\
        8/2&=4    &\dots 0,\\
        4/2&=2    &\dots 0,\\
        2/2&=1    &\dots 0,\\
        1/2&=0    &\dots 1.
    \end{aligned}
    $$
    
    Fractional part:
    
    $$
    \begin{aligned}
        0.25\times 2&=0.5  &\dots 0,\\
        0.5\times 2&=1     &\dots 1.
    \end{aligned}
    $$
    
    So $35.25 = (100011.01)_2$.

???+ note "Implementation"
    ```cpp
    --8<-- "docs/math/code/base/base_1.cpp:from_dec"
    ```

### Other bases to decimal

Again with binary as an example. To convert a binary number to decimal, simply multiply the value of each digit by $2^i$, where $i$ is the position of the current digit and the units digit has position $0$.

???+ example "Example"
    Convert $(11010.01)_{2}$ to decimal.
    
    $$
    \begin{aligned}
        (11010.01)_{2}&=\phantom{+~}1\times 2^4+1\times 2^3+0\times 2^2+1\times 2^1+0\times 2^0\\
        &\phantom{=}+~0\times 2^{-1}+1\times 2^{-2} \\
                    &=26.25.
    \end{aligned}
    $$
    
    So $(11010.01)_2 = (26.25)_{10}$.

???+ note "Implementation"
    ```cpp
    --8<-- "docs/math/code/base/base_1.cpp:to_dec"
    ```

### Conversion between binary, octal, and hexadecimal

One octal digit can be represented by 3 binary digits (since $2^3 = 8$), and one hexadecimal digit can be represented by 4 binary digits ($2^4 = 16$), and vice versa.

## Method of complements

See also: [Ones' complement and two's complement](../bit.md#整数与位序列)

The **method of complements** is a technique for representing negative numbers with positive ones so that subtraction can be computed with the same algorithm/circuit/mechanical structure as the addition of positive numbers. The method of complements is widely used in the design of calculators and computers to simplify their structure.

For an $n$-digit number $a$ in base $b$, its **radix complement** (called the $b$'s complement) is $b^n-a$, and its **diminished radix complement** (called the $b-1$'s complement, or simply the **diminished complement**) is $b^n-1-a$. In binary, the radix complement is called the $2$'s complement (two's complement), also known as the **two's complement code**; the diminished radix complement is called the $1$'s complement (ones' complement), also known as the **ones' complement code**; in decimal, the radix complement is also called the $10$'s complement (ten's complement) and the diminished radix complement the $9$'s complement (nine's complement); and so on for other bases.

For $n$-digit numbers $x,y$ in base $b$, when computing $x-y$ we have the following methods (if the result exceeds $n$ digits, the higher digits are discarded):

1.  Take the diminished complement $x'=b^n-1-x$ of $x$ and compute $x'+y=b^n-1-x+y$; the diminished complement of this result is the answer.
2.  Take the diminished complement $y'=b^n-1-y$ of $y$ and compute $x+y'=b^n-1+x-y$; adding one directly gives the answer.
3.  Take the radix complement $x'=b^n-x$ of $x$ and compute $x'+y=b^n-x+y$; the radix complement of this result is the answer.
4.  Take the radix complement $y'=b^n-y$ of $y$ and compute $x+y'=b^n+x-y$; this is the answer.

Moreover, for numbers in base $k$, let $d=k-1$; then $\cdots dd=:\overline{d}=\sum_{i=0}^{\infty} dk^i=-1$, so for an $n$-digit number $x$ whose radix complement in base $k$ is written $a_{n-1}\cdots a_1a_0$, the number $\overline{d}a_{n-1}\cdots a_1a_0$ equals $\sum_{i=0}^{n-1}a_ik^i+\sum_{i=n}^{\infty} dk^i=k^n-x+(-k^n)=-x$. This idea of "numbers with infinitely many digits" can be generalized to [**$p$-adic numbers**](https://en.wikipedia.org/wiki/P-adic_number) ($p$-adic number).

In addition, we have an interesting theorem about complements and infinite repeating decimals:

???+ note "Midy's theorem"
    Let $a$ be a positive integer, $p$ a positive prime, and let the representation of $a/p$ in base $b$ be $0.\overline{a_1a_2\cdots a_l}$, where $l$ is the (shortest) period length. If $l$ is even[^note5], let $l=2k$; then $a_1a_2\cdots a_k$ is the diminished complement of $a_{k+1}a_{k+2}\cdots a_{2k}$, i.e.:
    
    -   $a_i+a_{i+k}=b$,
    -   $a_1a_2\cdots a_k+a_{k+1}a_{k+2}\cdots a_{2k}=b^k-1$.
    
    Furthermore, if $l$ has a non-trivial divisor $k$ and $l=nk$, then $\sum_{i=0}^{n-1}a_{ik+1}a_{ik+2}\cdots a_{(i+1)k}$ is a multiple of $b^k-1$.

??? example "Example"
    For $1/19=0.\overline{052~631~578~947~368~421}=0.\overline{032~745}_{(8)}$, we have:
    
    -   $052~631~578+947~368~421=999~999~999$,
    -   $052+631+578+947+368+421=3\times 999$,
    -   $032_{(8)}+745_{(8)}=777_{(8)}$,
    -   $03_{(8)}+27_{(8)}+45_{(8)}=77_{(8)}$.

??? note "Proof"
    For the $a,b,p,l,n,k$ in the theorem, it is easy to see that $1\leq a<p$, $b>1$, and $(a,p)=(b,p)=1$.
    
    For an integer $0\leq i<l$, let $f(i)=b^i\cdot a/p-\lfloor b^i\cdot a/p\rfloor$; we have
    
    $$
    0<f(i)=0.\overline{a_{i+1}a_{i+2}\cdots a_{nk}a_1a_2\cdots a_i}<1 \implies 0<pf(i)<p.
    $$
    
    Note that $pf(i)\in\mathbf{N}_+$ and $pf(i)\equiv ab^i\pmod p$, hence $pf(i)=ab^i\bmod p$.
    
    Let $S_n=\sum_{i=0}^{n-1}f(ik)=\sum_{i=0}^{n-1}0.\overline{a_{ik+1}a_{ik+2}\cdots a_{nk}a_1a_2\cdots a_{ik}}$; we can "exchange" some digits between the decimals (for example $0.\overline{{\color{Orchid}{14}}{\color{RoyalBlue}{28}}{\color{YellowGreen}{57}}}+0.\overline{{\color{RoyalBlue}{28}}{\color{YellowGreen}{57}}{\color{Orchid}{14}}}+0.\overline{{\color{YellowGreen}{57}}{\color{Orchid}{14}}{\color{RoyalBlue}{28}}}=0.\overline{\color{Orchid}{141414}}+0.\overline{\color{RoyalBlue}{282828}}+0.\overline{\color{YellowGreen}{575757}}=0.\overline{\color{Orchid}{14}}+0.\overline{\color{RoyalBlue}{28}}+0.\overline{\color{YellowGreen}{57}}=14/99+28/99+57/99=1$), so
    
    $$
    \begin{aligned}
        S_n&=\sum_{i=0}^{n-1}0.\overline{a_{ik+1}a_{ik+2}\cdots a_{(i+1)k}}\\
        &=\sum_{i=0}^{n-1}a_{ik+1}a_{ik+2}\cdots a_{(i+1)k}/\left(b^k-1\right),
    \end{aligned}
    $$
    
    and therefore
    
    $$
    pS_n=p\sum_{i=0}^{n-1}a_{ik+1}a_{ik+2}\cdots a_{(i+1)k}/\left(b^k-1\right)= \sum_{i=0}^{n-1} \left(ab^{ik}\bmod p\right),
    $$
    
    hence
    
    $$
    \sum_{i=0}^{n-1}a_{ik+1}a_{ik+2}\cdots a_{(i+1)k}=\left(b^k-1\right)\frac{\sum_{i=0}^{n-1} \left(ab^{ik}\bmod p\right)}{p}.
    $$
    
    If $p\mid \left(b^k-1\right)$, note that
    
    $$
    \left(b^k-1\right)a/p=a_1a_2\cdots a_k.\overline{a_{k+1}a_{k+2}\cdots a_{nk}a_1a_2\cdots a_k}-0.\overline{a_{1}a_{2}\cdots a_{nk}},
    $$
    
    so $a_{k+1}a_{k+2}\cdots a_{nk}a_1a_2\cdots a_k=a_{1}a_{2}\cdots a_{nk}$, and hence $a_1a_2\cdots a_k=a_{k+1}a_{k+2}\cdots a_{2k}=\dots=a_{(n-1)k+1}a_{(n-1)k+2}\cdots a_{nk}$, i.e. $0.\overline{a_1a_2\cdots a_l}=0.\overline{a_1a_2\cdots a_k}$, which contradicts the definition of $l$; therefore $p\nmid \left(b^k-1\right)$.
    
    Hence there exists a positive integer $c=\dfrac{\sum_{i=0}^{n-1} \left(ab^{ik}\bmod p\right)}{p}$ such that
    
    $$
    \sum_{i=0}^{n-1}a_{ik+1}a_{ik+2}\cdots a_{(i+1)k}=c\left(b^k-1\right).
    $$

???+ note "Corollary"
    For the above $b,n,k,p$, we have
    
    $$
    \sum_{i=0}^{n-1} b^{ik}\equiv 0\pmod p.
    $$

## Generalized positional systems

In a standard positional system, the base $b$ is always a fixed positive number, each digit is chosen from $b$ different symbols, and a non-negative number is represented (ignoring the decimal point and the minus sign). In fact, there are still many numeration systems with similar characteristics that do not fully conform to the rules of positional systems; we call such numeration systems **generalized positional systems** or **non-standard positional numeral systems**. Below we introduce several common generalized positional systems.

### Bijective numeration

A standard positional system does not establish a bijection with the numbers it represents; for example, $1$, $01$, and $001$ represent the same number[^note1], whereas a **bijective numeral system** does establish a bijection with the numbers it represents.

Bijective base $k$ ($k\geq 1$) uniquely represents a number using the digit set $\{1,2,\dots,k\}$ with the following rules:

1.  the empty string represents $0$;
2.  a non-empty string $a_n\cdots a_1a_0$ represents the number $a_nk^n+\cdots+a_1k^1+a_0k^0=\sum_{i=0}^n a_ik^i$.

For a positive number $m$ whose representation in bijective base $k$ is $a_n\cdots a_1a_0$, we have:

$$
\begin{array}{cc}
    a_0=m-q_0k,&q_0=f(m/k),\\
    a_1=q_0-q_1k,&q_1=f(q_0/k),\\
    \vdots&\vdots\\
    a_n=q_{n-1}-q_nk,&q_n=f(q_{n-1}/k)=0,\\
\end{array}
$$

where $f(x)=\lceil x\rceil-1$.

For example, the column labels of Microsoft Excel use bijective base $26$.

Among bijective numeral systems we have the [unary numeral system](https://en.wikipedia.org/wiki/Unary_numeral_system); a non-empty string in unary consists only of $1$s, and the length of the string is the number it represents.

Similar to the discussion under the [method of complements](#method-of-complements), in bijective base $k$ with $k>1$, let $d=k-1$; then $\cdots dd=:\overline{d}=\sum_{i=0}^{\infty} dk^i=-1$, and hence $\overline{d}k=0$, so if the representation of $x$ in bijective base $k$ is $a_{n-1}\cdots a_1a_0$, then $\overline{d}ka_{n-1}\cdots a_1a_0$ is $-x$.

Below are some properties of bijective base-$k$ numbers:

-   There are $k^l$ numbers of length $l\geq 0$.
-   When $k\geq 2$, the length of the representation of the number $n$ in bijective base $k$ is $\lfloor\log_k (n+1)(k-1)\rfloor$.
-   When $k\geq 2$, if the representation of a number $n$ in base $k$ contains no $0$, then its representation in base $k$ is the same as its representation in bijective base $k$.

The code for converting bijective base $k$ to decimal is the same as for converting base $k$ to decimal; below is a reference implementation of converting decimal to bijective base $k$

???+ note "Implementation"
    ```cpp
    --8<-- "docs/math/code/base/base_1.cpp:from_dec_bi"
    ```

### Signed-digit representation

Some positional systems allow negative digits, for example [balanced ternary](./balanced-ternary.md).

### Gray code

Main article: [Gray code](./gray-code.md)

Gray code, also called **cyclic binary code** or **reflected binary code** (RBC), is a special binary numeral system often used in data verification.

### Non-positive bases

We know that for a base-$k$ number $a_n\cdots a_1a_0$, the value it represents is $\sum_{i=0}^n a_ik^i$; with a slight modification we can define the base $-k$ number ${a_n\cdots a_1a_0}_{(-k)}$ representing $\sum_{i=0}^n a_i(-k)^i$, where $a_n,\dots,a_1,a_0\in \{0,1,\dots,k-1\}$. For example, $12345_{(-10)}=8265_{(10)}$. Such a system is called a [**negative-base system**](https://en.wikipedia.org/wiki/Negative_base).

Similarly, we can define [**complex-base systems**](https://en.wikipedia.org/wiki/Complex-base_system), such as the [**base-$2\mathrm{i}$ system**](https://en.wikipedia.org/wiki/Quater-imaginary_base) (quater-imaginary base, quater-imaginary numeral system), and we can also define [**non-integer bases of numeration**](https://en.wikipedia.org/wiki/Non-integer_base_of_numeration) used for the **$\beta$-expansion** ($\beta$-expansion) of real numbers, etc.

### Mixed radix

In a standard positional system, the base corresponding to each digit is fixed, whereas a mixed-radix system allows each digit to have a different base. The most common application of mixed-radix systems is timekeeping: hours use base $24$, while minutes and seconds use base $60$.

The number represented by $a_n\cdots a_1a_0$ in base $b$ is $\sum_{i=0}^n a_ib^i$, whereas in a mixed-radix system it represents $\sum_{i=0}^n a_i\prod_{j=0}^{i-1}b_j$, where $b_j$ is the base corresponding to $a_j$.

In algorithmic competitions, the most common mixed-radix system is the [**factorial number system**](https://en.wikipedia.org/wiki/Factorial_number_system), in which numbers can be written as ${a_n\cdots a_1a_0}_{~!}$ and represent $\sum_{i=0}^na_i i!$[^note2]. For applications of the factorial number system in algorithmic competitions, see [Lehmer code/Cantor expansion](../permutation.md#排名).

???+ note "Implementation (decimal to factorial number system)"
    ```cpp
    --8<-- "docs/math/code/base/base_1.cpp:from_dec_factorial"
    ```

???+ note "Implementation (factorial number system to decimal)"
    ```cpp
    --8<-- "docs/math/code/base/base_1.cpp:to_dec_factorial"
    ```

## Implementation in C++

For non-negative numbers, C++ writes an integer literal as `<prefix><digits><suffix>`, where `<digits>` and `<suffix>` may both be empty. The `<suffix>` indicates the type of the literal, e.g. `u` or `U` means the literal is `unsigned`, `l` or `L` means it is `long`, etc. For the `<prefix>`:

-   when the `<prefix>` is `0x` or `0X`, it is a hexadecimal literal, and the characters in `<digits>` can only be chosen from `0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, A, b, B, c, C, d, D, e, E, f, F`. For example, `0x1234ABCD` is $\text{1234ABCD}_{(16)}=305~441~741$;
-   when the `<prefix>` is `0`, it is an octal literal, and the characters in `<digits>` can only be chosen from `0, 1, 2, 3, 4, 5, 6, 7`. For example, `01234567` is $1234567_{(8)}=342391$;[^note3]
-   when the `<prefix>` is `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, or `9`, it is a decimal literal, and the characters in `<digits>` can only be chosen from `0, 1, 2, 3, 4, 5, 6, 7, 8, 9`;
-   since C++14, when the `<prefix>` is `0b` or `0B`, it is a binary literal, and the characters in `<digits>` can only be chosen from `0, 1`. For example, `0b11001010` is $11001010_{(2)}=202$.

## References and notes

-   [Positional notation - Wikipedia](https://en.wikipedia.org/wiki/Positional_notation)
-   [Method of complements - Wikipedia](https://en.wikipedia.org/wiki/Method_of_complements)
-   [Non-standard positional numeral systems - Wikipedia](https://en.wikipedia.org/wiki/Non-standard_positional_numeral_systems)
-   [Bijective numeration - Wikipedia](https://en.wikipedia.org/wiki/Bijective_numeration)
-   [Midy's theorem - Wikipedia](https://en.wikipedia.org/wiki/Midy%27s_theorem)
-   [N3472 - Binary Literals in the C++ Core Language](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2012/n3472.pdf)

[^note1]: We call the $0$s before the highest non-$0$ digit [**leading zeros**](https://en.wikipedia.org/wiki/Leading_zero). Similarly, we can define [**trailing zeros**](https://en.wikipedia.org/wiki/Trailing_zero).

[^note2]: The base corresponding to $a_i$ is $i+1$, $0\leq a_i\leq i$. Note that $(n+1)!-n!=n\cdot n!$, so the representation of a number in the factorial number system is unique once leading zeros are removed.

[^note3]: `0` is an octal literal.

[^note4]: Some regions use "$,$" as the decimal point.

[^note5]: When $a=1$, the sequence of primes satisfying this condition in decimal is [A028416](https://oeis.org/A028416).
