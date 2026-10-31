---
title: Bit operations
---

Bit operations are unary and binary operations on the binary representation of integers; they fall into two classes, **bitwise operations** and **shifts**. Bit operations are among the most basic operations of a CPU and are usually very fast.

## Integers and bit sequences

See also: [Integer types](../lang/var.md#整数类型), [Complement representations](./numeral-sys/base.md#method-of-complements)

We call a fixed-length sequence consisting only of `0` and `1` a bit sequence. The leftmost bit is called the most significant bit and the rightmost bit the least significant bit.

Computers use bit sequences to represent integers in a certain range. There are only $2^N$ bit sequences of length $N$, so they can be put in one-to-one correspondence with only $2^N$ integers. Such correspondences fall into two classes: **signed** and **unsigned**. Signed means that the corresponding integers include negative numbers; unsigned means that all corresponding integers are nonnegative.

-   For the unsigned correspondence we can directly take the binary representation of the integer as the bit sequence, padding with `0` in the high positions if it is too short.

    Under the unsigned correspondence, a bit sequence of length $N$ can represent the integers in $[0,2^N-1]$.

-   For the signed correspondence we have two representation rules: **ones' complement** and **two's complement**.

    For nonnegative integers the representation rule is the same as the unsigned one. For a negative integer, we take the bit sequence of its opposite number and **invert it bitwise** (i.e., turn every `0` into `1` and every `1` into `0`); the result is called the ones' complement. If we convert the ones' complement to an integer under the unsigned correspondence, add one, convert it back to a bit sequence under the unsigned correspondence and discard the part exceeding the original length of the sequence, the new sequence we obtain is called the two's complement.

    Under ones' complement, a bit sequence of length $N$ can represent the integers in $[-2^{N-1}+1,2^{N-1}-1]$.

    Under two's complement, a bit sequence of length $N$ can represent the integers in $[-2^{N-1},2^{N-1}-1]$.

Take bit sequences of length $3$ as an example:

| Bit sequence | Unsigned integer | Signed integer (ones' complement) | Signed integer (two's complement) |
| ----- | ----- | --------- | --------- |
| `000` | $0$   | $0$       | $0$       |
| `001` | $1$   | $1$       | $1$       |
| `010` | $2$   | $2$       | $2$       |
| `011` | $3$   | $3$       | $3$       |
| `100` | $4$   | $-3$      | $-4$      |
| `101` | $5$   | $-2$      | $-3$      |
| `110` | $6$   | $-1$      | $-2$      |
| `111` | $7$   | $-0$      | $-1$      |

We can see that the biggest problem of ones' complement is the appearance of $-0$, a "negative number" that does not actually exist, so normally we only use two's complement. Since, when representing signed integers, the sign is determined solely by the most significant bit of the sequence, we call this bit the **sign bit**.

Converting a bit sequence to an integer is also easy: for nonnegative numbers nothing special is needed; for ones' complement, inverting gives the opposite number; for two's complement, inverting and adding one gives the opposite number.

## Bitwise operations

Bitwise operations are operations that apply certain [Boolean functions](./boolean-algebra.md#boolean-functions) to a bit sequence bit by bit. Formally, for a Boolean function $f:\mathbf{B}^k\to \mathbf{B}$, the bitwise operation is the function of the form

$$
\begin{aligned}
    F:\left(\mathbf{B}^m\right)^k&\to \mathbf{B}^m\\
    ((p_{1,1},\dots,p_{m,1}),\dots,(p_{1,k},\dots,p_{m,k}))&\mapsto (f(p_{1,1},\dots,p_{1,k}),\dots,f(p_{m,1},\dots,p_{m,k}))
\end{aligned}
$$

where $m$ is the length of the bit sequence. As usual, we generally study only unary and binary bitwise operations. Unless otherwise stated, the bitwise operations below are restricted to the unary and binary cases.

In general, we regard **bitwise NOT**, **bitwise AND**, **bitwise OR** and **bitwise XOR** as the basic bitwise operations; all other bitwise operations can be obtained by combining them.

| Bitwise operation | Mathematical notation | Corresponding Boolean function | C++ operator | Explanation |
| ---- | ----------------------------- | -------- | --------------- | ----------------------- |
| bitwise NOT | $\operatorname{NOT}$          | $\lnot$  | `~`             | $0$ becomes $1$, $1$ becomes $0$   |
| bitwise AND  | $\operatorname{AND}$          | $\land$  | `&`             | $1$ only if both corresponding bits are $1$   |
| bitwise OR  | $\operatorname{OR}$           | $\lor$   | <code>\|</code> | $1$ as soon as at least one of the two corresponding bits is $1$ |
| bitwise XOR | $\oplus$, $\operatorname{XOR}$ | $\oplus$ | `^`             | $1$ only if the two corresponding bits differ        |

???+ warning "Warning"
    Be careful to distinguish bitwise operations from Boolean functions.

For example:

-   $\operatorname{NOT} 01010111=10101000$,
-   $01010011 \operatorname{AND} 00110010=00010010$,
-   $01010011 \operatorname{OR}  00110010=01110011$,
-   $01010011 \operatorname{XOR} 00110010=01100001$.

Since in the four bitwise operations above the computation on each bit is independent, these four operations directly inherit the properties of their corresponding Boolean functions.

For convenience, when the length of the bit sequence is known, we can also apply bitwise operations directly to integers, for example:

$$
\begin{aligned}
    \operatorname{NOT} 5&=-6,\\
    \operatorname{NOT} (-5)&=4,\\
    5 \operatorname{AND} 6 &=4,\\
    5 \operatorname{OR} 6 &=7,\\
    5 \operatorname{XOR} 6 &=3.
\end{aligned}
$$

Assuming $x,y\geq 0$, we can also express bitwise operations as sums:

$$
\begin{aligned}
    \operatorname{NOT} x&=\sum_{n=0}^{\lfloor\log_{2}x\rfloor}2^n\left(\left(\left\lfloor\frac{x}{2^n}\right\rfloor\bmod 2+1\right)\bmod 2\right)\\
    &=\sum_{n=0}^{\lfloor\log_{2}x\rfloor}\left(2^{\left\lfloor\log_{2}x\right\rfloor +1}-1-x\right)\\
    x\operatorname{AND} y&=\sum_{n=0}^{\lfloor\log_{2}\max\{x,y\}\rfloor}2^n\left(\left\lfloor\frac{x}{2^n}\right\rfloor\bmod 2\right)\left(\left\lfloor{\frac{y}{2^n}}\right\rfloor\bmod 2\right)\\
    x\operatorname{OR} y&=\sum_{n=0}^{\lfloor\log_{2}\max\{x,y\}\rfloor}2^n\left(\left(\left\lfloor\frac{x}{2^n}\right\rfloor\bmod 2\right)+\left(\left\lfloor{\frac{y}{2^n}}\right\rfloor\bmod 2\right)-\left(\left\lfloor\frac{x}{2^n}\right\rfloor\bmod 2\right)\left(\left\lfloor{\frac{y}{2^n}}\right\rfloor\bmod 2\right)\right)\\
    x\operatorname{XOR} y&=\sum_{n=0}^{\lfloor\log_{2}\max\{x,y\}\rfloor}2^n\left(\left(\left(\left\lfloor\frac{x}{2^n}\right\rfloor\bmod 2\right)+\left(\left\lfloor{\frac{y}{2^n}}\right\rfloor\bmod 2\right)\right)\bmod 2\right)\\
    &=\sum_{n=0}^{\lfloor\log_{2}\max\{x,y\}\rfloor}2^n\left(\left(\left\lfloor\frac{x}{2^n}\right\rfloor +\left\lfloor\frac{y}{2^n}\right\rfloor\right)\bmod 2\right)
\end{aligned}
$$

When no ambiguity arises, "bitwise" is omitted below.

## Bit shifts

See also: [C++ bit operators](../lang/op.md#位操作符).

A shift is a binary operation that "moves a bit sequence left or right bit by bit"; the first argument is the bit sequence and the second is usually a nonnegative integer. Moving left is called a **left shift**, moving right a **right shift**. According to how the vacated positions are filled, shifts are divided into **arithmetic shifts**, **logical shifts** and **circular shifts (rotations)**. Here

-   a logical shift fills the vacated positions with 0,
-   an arithmetic right shift fills the vacated positions with the sign bit, and an arithmetic left shift is the same as a logical left shift,
-   a circular shift fills the vacated positions with the bits that were shifted out.

For example, for the $8$-bit sequence `10 01 01 10`:

| Operation         | Result            |
| ---------- | ------------- |
| arithmetic left shift by $2$ bits | `01 01 10 00` |
| arithmetic right shift by $2$ bits | `11 10 01 01` |
| logical left shift by $2$ bits | `01 01 10 00` |
| logical right shift by $2$ bits | `00 10 01 01` |
| circular left shift by $2$ bits | `01 01 10 10` |
| circular right shift by $2$ bits | `10 10 01 01` |

In C++, `a << b` denotes a left shift and `a >> b` a right shift; for which shift rule is applied, see [C++ bit operators](../lang/op.md#位操作符).

We can implement circular shifts with the following code:

???+ note "Implementation"
    ```cpp
    --8<-- "docs/math/code/bit/bit_1.cpp:core"
    ```

## Applications of bit operations

Bit operations generally serve three purposes:

1.  Performing certain computations efficiently, replacing other, less efficient ways. See [Compiler optimizations – strength reduction](../lang/optimizations.md#强度削减-strength-reduction).
2.  [Representing sets](./binary-set.md) (commonly used in [bitmask DP](../dp/state.md)).
3.  The problem itself requires bit operations.

Note that replacing other operations with bit operations often does not bring much optimization and instead makes the code more complex, so use them judiciously.

### Applications involving powers of 2

Since bit operations act on the binary representation, many applications related to integer powers of 2 can be derived.

Multiplying (dividing) a number by a nonnegative integer power of 2:

=== "C++"
    ```cpp
    --8<-- "docs/math/code/bit/bit_2.cpp:mul"
    ```

=== "Python"
    ```python
    --8<-- "docs/math/code/bit/bit_2.py:mul"
    ```

??? warning "Warning"
    The division we usually write rounds toward $0$, while the right shift here rounds down (note the difference); that is, the two methods are equivalent when the number is greater than or equal to $0$ and differ when the number is less than $0$. For example, the value of `-1 / 2` is $0$, while the value of `-1 >> 1` is $-1$.

### Absolute value

On some machines this is more efficient than `n > 0 ? n : -n`.

=== "C++"
    ```cpp
    --8<-- "docs/math/code/bit/bit_2.cpp:abs"
    ```

=== "Python"
    ```python
    --8<-- "docs/math/code/bit/bit_2.py:abs"
    ```

### Maximum/minimum of two numbers

On some machines this is more efficient than `a > b ? a : b`.

=== "C++"
    ```cpp
    --8<-- "docs/math/code/bit/bit_2.cpp:minmax"
    ```

=== "Python"
    ```python
    --8<-- "docs/math/code/bit/bit_2.py:minmax"
    ```

### Checking whether two nonzero numbers have the same sign

=== "C++"
    ```cpp
    --8<-- "docs/math/code/bit/bit_2.cpp:sgn"
    ```

=== "Python"
    ```python
    --8<-- "docs/math/code/bit/bit_2.py:sgn"
    ```

### Swapping two numbers

???+ note "This method has limitations"
    This method can only be used to swap two integers, so its range of application is limited.
    
    For swapping in the general case, it is recommended to call the `std::swap` function from the `algorithm` library directly.

```cpp
--8<-- "docs/math/code/bit/bit_2.cpp:swap"
```

### Manipulating the bits of a number

Getting a certain bit of the binary representation of a number:

=== "C++"
    ```cpp
    --8<-- "docs/math/code/bit/bit_2.cpp:get_bit"
    ```

=== "Python"
    ```python
    --8<-- "docs/math/code/bit/bit_2.py:get_bit"
    ```

Setting a certain bit of the binary representation of a number to $0$:

=== "C++"
    ```cpp
    --8<-- "docs/math/code/bit/bit_2.cpp:unset_bit"
    ```

=== "Python"
    ```python
    --8<-- "docs/math/code/bit/bit_2.py:unset_bit"
    ```

Setting a certain bit of the binary representation of a number to $1$:

=== "C++"
    ```cpp
    --8<-- "docs/math/code/bit/bit_2.cpp:set_bit"
    ```

=== "Python"
    ```python
    --8<-- "docs/math/code/bit/bit_2.py:set_bit"
    ```

Flipping a certain bit of the binary representation of a number:

=== "C++"
    ```cpp
    --8<-- "docs/math/code/bit/bit_2.cpp:flap_bit"
    ```

=== "Python"
    ```python
    --8<-- "docs/math/code/bit/bit_2.py:flap_bit"
    ```

These operations effectively treat a $32$-bit integer variable as a Boolean array of length $32$.

## Hamming weight

The Hamming weight of a string of symbols is the number of symbols that differ from the zero-symbol (defined over the alphabet in use). For a binary number, its Hamming weight equals the number of $1$s in it (i.e., `popcount`).

The Hamming weight of a number can be computed with a loop: we repeatedly remove the last bit of the number's binary representation (i.e., shift it right by $1$ bit), maintain an answer variable, and during the division update the answer according to whether the lowest bit is $1$.

The code is as follows:

```cpp
--8<-- "docs/math/code/bit/bit_2.cpp:popcnt1"
```

The Hamming weight of a number can also be computed with the `lowbit` operation: we repeatedly subtract its `lowbit`[^note1] from the number until the number becomes $0$.

The code is as follows:

```cpp
--8<-- "docs/math/code/bit/bit_2.cpp:popcnt2"
```

### Constructing a permutation with increasing Hamming weight

In [bitmask DP](../dp/state.md), enumerating in order of increasing popcount can sometimes avoid enumerating states repeatedly. This is a major use of constructing a permutation with increasing Hamming weight.

Below we explore concretely how to construct a permutation with increasing Hamming weight in $O(n)$ time.

We know that the smallest integer with Hamming weight $n$ is $2^n-1$. As long as we can construct, in constant time, the successor of an integer with the same Hamming weight, we can enumerate the Hamming weights and, starting from $2^n-1$, keep finding the next number, thus constructing the required permutation of $0\sim n$ in $O(n)$ time.

To find the successor of a number $x$ with the same Hamming weight, the idea is as follows, taking $(10110)_2$ as an example:

-   Move the rightmost $1$ of $(10110)_2$ to the left; if it cannot be moved, move the $1$ to its left, and so on, obtaining $(11010)_2$.

-   In the resulting $(11010)_2$, move all the $1$s from the original position of the last moved $1$ down to the lowest bit all the way to the right. Here the last moved $1$ was originally in the third position, so the last three bits $010$ must become $001$, giving $(11001)_2$.

This process can be optimized with bit operations:

```cpp
--8<-- "docs/math/code/bit/bit_3.cpp:hamming1"
```

-   In the first step, we add to the number $x$ its `lowbit`; in binary this amounts to replacing the rightmost contiguous block of $1$s of $x$ with a single $1$ to its left. For the binary number $(10110)_2$ just mentioned, after adding its `lowbit` it becomes $(11000)_2$. This actually gives the first half of our answer.
-   Next we need to fill in the trailing $1$s of the answer. The `lowbit` of $t$ is the position to which the leftmost $1$ of the rightmost contiguous block of $1$s of $x$ has moved, while the `lowbit` of $x$ is the position of the rightmost $1$ of that block of $x$. Again with $(10110)_2$ as the example, $t = (11000)_2$, $\operatorname{lowbit}(t) = (01000)_2$, $\operatorname{lowbit}(x)=(00010)_2$.
-   The division that follows is the hardest part of this bit trick to understand, but also the most crucial. Suppose the highest $1$ of the rightmost contiguous block of $1$s of the **original number** is at bit $r$ (bits numbered from $0$) and the lowest $1$ is at bit $l$; the `lowbit` of $t$ equals `1 << (r+1)`, the `lowbit` of $x$ equals `1 << l`, and `(((t&-t)/(x&-x))>>1)` yields `(1<<(r+1))/(1<<l)/2 = (1<<r)/(1<<l) = 1<<(r-l)`, which in binary is a $1$ followed by $r-l$ zeros, where the number of zeros is exactly the number of consecutive $1$s minus $1$. Taking our number as an example, $\frac{\operatorname{lowbit(t)/2}}{\operatorname{lowbit(x)}} = \frac{(00100)_2}{(00010)_2} = (00010)_2$. Subtracting $1$ from this number gives exactly the low bits we need to fill in, and OR-ing it with the original number gives the answer.

So the complete code for enumerating the permutation of $0\sim n$ in order of increasing Hamming weight is:

```cpp
--8<-- "docs/math/code/bit/bit_3.cpp:hamming2_begin"
--8<-- "docs/math/code/bit/bit_3.cpp:hamming2_end"
```

Note the special handling of $0$, since $0$ has no successor with the same Hamming weight.

## Related classes and functions in C++

### GCC built-in functions

GCC also has some built-in functions for bit operations:

-   `int __builtin_ffs(int x)`: returns the position of the last $1$ at the end of the binary representation of $x$, with positions numbered from $1$ (the lowest bit is number $1$). Returns $0$ when $x$ is $0$.
-   `int __builtin_clz(unsigned int x)`: returns the number of leading $0$s in the binary representation of $x$. The result is undefined when $x$ is $0$.
-   `int __builtin_ctz(unsigned int x)`: returns the number of trailing consecutive $0$s in the binary representation of $x$. The result is undefined when $x$ is $0$.
-   `int __builtin_clrsb(int x)`: when the sign bit of $x$ is $0$, returns the number of leading $0$s in the binary representation of $x$ minus one; otherwise returns the number of leading $1$s in the binary representation of $x$ minus one.
-   `int __builtin_popcount(unsigned int x)`: returns the number of $1$s in the binary representation of $x$.
-   `int __builtin_parity(unsigned int x)`: determines the parity of the number of $1$s in the binary representation of $x$.

All of these functions can have `l` or `ll` appended to the function name (e.g., `__builtin_popcountll`) to change the argument type to (`unsigned`)`long` or (`unsigned`)`long long` (the return value is still of type `int`).
For example, we sometimes want the base-two logarithm of a number; ignoring the special case `0`, this equals the number of bits in the number's binary representation `-1`, and the number of bits in the binary representation of an `N`-bit integer `n` can be expressed as `N - __builtin_clz(n)`, so `N - 1 - __builtin_clz(n)` gives the base-two logarithm of `n`.

Since these are built-in functions, highly optimized by the compiler, they run very fast (some need only a single instruction).

### More bits

If the bit sequence to be manipulated is very long, [`std::bitset`](../lang/csl/bitset.md) can be used.

## Recommended problems

-   [Luogu P1225 黑白棋游戏 (Black and White Pieces Game)](https://www.luogu.com.cn/problem/P1225)

## References and notes

1.  [Bit operation tricks](https://graphics.stanford.edu/~seander/bithacks.html)
2.  [Bit Operation Builtins (Using the GNU Compiler Collection (GCC))](https://gcc.gnu.org/onlinedocs/gcc/Bit-Operation-Builtins.html)
3.  [Bitwise operation - Wikipedia](https://en.wikipedia.org/wiki/Bitwise_operation)

[^note1]: The first $1$ in the binary representation of a number, going from low bits to high bits, together with the zeros after it; e.g., the `lowbit` of $(1010)_2$ is $(0010)_2$. See [Fenwick tree](../ds/fenwick.md) for details.
