---
title: Permutations
---

Permutations and arrangements are concepts that appear very frequently in all kinds of problems.

???+ warning "This article is not about the number of arrangements"
    The topic of this article is full permutations, not the number of arrangements (k-permutations) from combinatorics. For material on the number of arrangements, see [Combinatorics](./combinatorics/combination.md).

???+ info "Convention"
    Unless stated otherwise, this article always deals with finite sets.

## Definition

A bijection (i.e. one-to-one correspondence) $\sigma$ from a set $X$ to itself is called a **permutation** of $X$. If the set $X$ also carries a [total order](./order-theory.md#二元关系), then a permutation of it is often also called a **(full) arrangement**. This total order is called the natural order on the set.

??? info "“Permutation” and “arrangement”"
    In the Chinese context, "permutation" (置换) usually refers to changing the order of elements, while "arrangement" (排列) usually refers to lining elements up in a row. When there is a natural order among the elements, these two concepts are one and the same: an "arrangement" can be viewed as the result of a "permutation", and relative to the natural order of the elements, the order of the elements in the "arrangement" specifies the "permutation". Since whenever this article uses the word "arrangement" it always assumes that a natural order exists on the set, this article does not specifically distinguish between the two concepts.
    
    Of course, elements without a natural order can also be "arranged". Such "arrangements" often appear in combinatorial counting problems. That is beyond the scope of this article.

Let the size of the set $X$ be $n$; then the number of all permutations of $X$ is $n!$. In particular, $0!=1$, i.e. there is exactly one permutation on the empty set, namely the empty permutation.

???+ info "Notation"
    Permutations are about the correspondence between elements and do not care what the elements actually are. Hence, when discussing a set of size $n$, it is usually assumed that the set in question is $\{1,2,\cdots,n\}$; when a natural order on the set is needed, the natural order on the natural numbers is usually assumed.

## Notations

There are several ways to write a permutation. Here we discuss the different notations for permutations using the following permutation as an example.

$$
\sigma(1) = 2,\
\sigma(2) = 6,\
\sigma(3) = 5,\
\sigma(4) = 4,\
\sigma(5) = 3,\
\sigma(6) = 1.
$$

### Two-line notation

A permutation of the set $X=\{x_1,x_2,\cdots,x_n\}$ can be written as

$$
\sigma=\begin{pmatrix}x_1&x_2&\cdots&x_n\\
x_{p_1}&x_{p_2}&\cdots&x_{p_n}
\end{pmatrix}.
$$

It means that the permutation $\sigma$ maps the element $x_i$ to $x_{p_i}$. Here, of course, we need $X=\{x_{p_1},x_{p_2},\cdots,x_{p_n}\}$. In the two-line notation of a permutation, the order in which the elements appear in the first row does not matter; what matters is the correspondence between the two rows.

For example, the earlier example can be written in two-line notation as

$$
\sigma=
\begin{pmatrix}
1 & 2 & 3 & 4 & 5 & 6 \\
2 & 6 & 5 & 4 & 3 & 1
\end{pmatrix},
$$

and of course it can also be written as

$$
\sigma=
\begin{pmatrix}
6 & 5 & 4 & 3 & 2 & 1 \\
1 & 3 & 4 & 5 & 6 & 2
\end{pmatrix}.
$$

### One-line notation

Very often the set $X$ has a natural order. If in the two-line notation the first row is written in the natural order by default and omitted, then the permutation can be written as

$$
\sigma=\sigma(1)\sigma(2)\cdots\sigma(n).
$$

This is more like the concept of an arrangement in natural language. So this ordered tuple is sometimes also called an "arrangement".

The earlier example can be written in one-line notation as

$$
\sigma=265431.
$$

This one-line notation is often used to compare different arrangements.

### Cycle notation

There is an even more compact way to express a permutation, called the cycle notation of the permutation. It expresses the permutation as a product of a series of disjoint cycles. Below we describe the steps for writing a given permutation in cycle notation.

Given a permutation $\sigma$, it can be written in cycle notation by the following steps:

1.  If there is still an element of $X$ that has not been written down, write a left parenthesis and write down any such element;
2.  When the last element written down is $x$,
    -   if $\sigma(x)$ has already been written down earlier, write a right parenthesis and return to step 1;
    -   if $\sigma(x)$ has not been written down yet, write down $\sigma(x)$ and continue with step 2;
3.  Repeat the above steps until all elements of $X$ have been written down.

Inside each pair of parentheses is one cycle. The number of elements inside the parentheses is called the length of the corresponding cycle. In practice, cycles of length one are often omitted.

The earlier example can be written in cycle notation as

$$
\sigma=(126)(35)(4)=(126)(35).
$$

In the identity transformation all cycles have length one; it is often written as $(1)$ rather than omitted entirely.

## Composition

The composition of permutations is the composition of maps. The composition of permutations is also often called the multiplication of permutations.

Given two permutations

$$
\sigma=\begin{pmatrix}x_1&x_2&\cdots&x_n\\ x_{p_1}&x_{p_2}&\cdots&x_{p_n}\end{pmatrix},\ \pi=\begin{pmatrix}x_{p_1}&x_{p_2}&\cdots&x_{p_n}\\ x_{q_1}&x_{q_2}&\cdots&x_{q_n}\end{pmatrix},
$$

their product $\pi\circ\sigma$ is

$$
\pi\circ\sigma=\begin{pmatrix}x_1&x_2&\cdots&x_n\\
x_{q_1}&x_{q_2}&\cdots&x_{q_n}\end{pmatrix}.
$$

Simply put, first apply the map $\sigma$, then apply the map $\pi$. Note that in the two-line notation above, the order of the second row of the inner map $\sigma$ agrees with the order of the first row of the outer map $\pi$.

Since the permutations $\sigma$ and $\pi$ are essentially two maps, $(\pi\circ\sigma)(x)=\pi(\sigma(x))$. The order of evaluation of the composition of permutations is from right to left. Multiplication of permutations is not commutative, so computing in the wrong order may lead to a wrong result.

Repeated composition of the same permutation is called a power of the permutation, and it can be computed quickly using [binary exponentiation](./binary-exponentiation.md#applying-a-permutation-multiple-times).

### Inverse permutation

Since a permutation is a bijection, a permutation always has a corresponding inverse permutation.

Given the permutation

$$
\sigma=\begin{pmatrix}x_1&x_2&\cdots&x_n\\ x_{p_1}&x_{p_2}&\cdots&x_{p_n}\end{pmatrix},
$$

its inverse permutation is

$$
\sigma^{-1}=\begin{pmatrix}x_{p_1}&x_{p_2}&\cdots&x_{p_n}\\x_1&x_2&\cdots&x_n\end{pmatrix}.
$$

In cycle notation, it suffices to invert each cycle to obtain the inverse of the original permutation; and to invert a cycle, it suffices to reverse the order in which the elements are written. For example, the cycle notation of the inverse of the permutation $\sigma$ from the example above is

$$
\sigma^{-1} = (621)(53) = (162)(35).
$$

Given an arrangement of $1\sim n$, it and the sequence formed by the position of each element in that arrangement are inverse arrangements of each other.

## Cycles

A **cycle** is itself a special permutation. The characteristic of a cycle is that, starting from any point $x$ of the cycle, any point $y$ of the cycle can be reached by repeatedly applying the permutation $\sigma$. A cycle of length $k$ is also called a **$k$‑cycle** ($k$-cycle). Applying a $k$‑cycle $k$ times yields the identity transformation, i.e. every element returns to its original position.

The cycle notation of a permutation can be viewed as writing the permutation as a product of these special permutations (i.e. cycles), so the cycle notation of a permutation can also be viewed as the **cycle decomposition** of the permutation. For every permutation, the way it decomposes into a product of cycles is unique up to order. Cycles can be regarded as the basic building blocks of permutations.

The cycle decomposition of a permutation has a clear geometric meaning. If every ordered pair $(x,\sigma(x))$ of a permutation of the set $X$ is regarded as an edge of a directed graph with vertex set $X$, then these cycles are exactly the cycles (closed walks) of this graph. If the permutation $\sigma$ can be decomposed into $m$ cycles, this means that the corresponding directed graph has a total of $m$ cycles (including self-loops). These cycles are naturally pairwise disjoint.

### Fixed points

The elements of $1$‑cycles are the **fixed points** of the permutation. For a permutation $\sigma$ of the set $X$, the set of fixed points of $\sigma$ is usually denoted $X^\sigma$, i.e. $X^\sigma=\{x\in X:\sigma(x)=x\}$.

### Transpositions

A $2$‑cycle is also called a **transposition**. In other words, a transposition is a permutation that swaps the positions of only one pair of elements. Its cycle notation is $(x_ix_j)$, meaning that it swaps the positions of $x_i$ and $x_j$.

Every permutation can be written as a product of a series of transpositions. This amounts to saying that an arrangement in any order can be restored to a specified ascending order by a series of operations that swap two elements. This is exactly what swap-based sorting algorithms do.

Furthermore, the correctness of the [bubble sort algorithm](../basic/bubble-sort.md) in fact shows that every permutation can be written as a product of a series of adjacent transpositions. Here an **adjacent transposition** is a transposition that swaps only adjacent elements.

## Properties

In applications, one often needs to pay attention to the properties of a single permutation.

### Parity

The way a cycle is decomposed into transpositions is not unique. For example,

$$
(123)=(13)(12)=(12)(23)=(12)(13)(12)(13).
$$

However, when a permutation is decomposed into a series of transpositions, the parity of the number of transpositions needed is fixed. The parity of the number of transpositions in the decomposition of a permutation is also called the **parity** of the permutation.

A permutation that can be decomposed into a product of an even number of transpositions is called an even permutation, and one that can be decomposed into a product of an odd number of transpositions is called an odd permutation. For $n\ge2$, the numbers of odd and even permutations of $n$ elements are equal.

### Sign

Based on the parity of a permutation, one can also define the **sign** of the permutation, denoted $\operatorname{sgn}\sigma$. The sign of an even permutation is defined as $+1$, and the sign of an odd permutation as $-1$.

The sign of a product of permutations equals the product of their signs, i.e.

$$
\operatorname{sgn}(\pi\circ\sigma)=\operatorname{sgn}
\pi\cdot\operatorname{sgn}\sigma.
$$

In other words, the composition of two permutations of the same parity is an even permutation, and the composition of two permutations of different parity is an odd permutation. This conclusion is obvious from the point of view of the decomposition into transpositions.

In particular, a single transposition necessarily changes the parity of a permutation. This is exactly why, although the decomposition into transpositions is not unique, the parity of the number of transpositions needed is determined.

The sign of a permutation appears in the [Leibniz formula for the determinant](./linear-algebra/determinant.md#全排列方法定义).

### Order of a permutation

The **order** of a permutation is the smallest positive integer $a$ satisfying the following condition: after repeating the permutation $a$ times, all elements return to their original positions. That is,

$$
\operatorname{ord}\sigma=\min\{a\in\mathbf N_+:\sigma^a=(1)\}.
$$

On a finite set, the order of every permutation is finite. This means that, starting from the initial order, as long as a given sequence is repeatedly shuffled according to a fixed pattern, the arrangement can always be restored to its original state in finite time.

### Cycle type of a permutation

Decompose a permutation of $n$ elements into cycles; the **cycle type** of the permutation is the multiset of the cycle lengths in the decomposition. These cycle lengths form an integer partition of $n$. If the resulting decomposition contains $\alpha_k$ cycles of length $k$ in total, the cycle type of the permutation is often written as

$$
1^{\alpha_1}2^{\alpha_2}\cdots n^{\alpha_n},
$$

and these exponents satisfy $\sum_{k=1}^nk\alpha_k=n$.

Given the cycle type of a permutation, the number of distinct permutations is

$$
\frac{n!}{1^{\alpha_1}2^{\alpha_2}\cdots n^{\alpha_n}\alpha_1!\alpha_2!\cdots\alpha_n!}.
$$

??? note "Analysis"
    This is because any arrangement of $1\sim n$ can be split according to the cycle type into the corresponding cycle decomposition. However, the order among cycles of the same length does not affect the permutation, so the total must be divided by $\prod_k\alpha_k!$. Moreover, within a single cycle we actually have a circular arrangement, and the choice of the starting point does not affect the permutation either, so we must divide by $\prod_kk^{\alpha_k}$. This yields the formula above.

If only the number $k$ of cycles into which the permutation decomposes is given, the number of distinct permutations is the [Stirling number of the first kind](./combinatorics/stirling.md#stirling-numbers-of-the-first-kind-stirling-number) $\begin{bmatrix}n\\ k\end{bmatrix}$. The number of distinct cycle types is the [partition number](./combinatorics/partition.md) $p_n$ of $n$.

From the cycle type of a permutation, properties such as the order and parity of the permutation can be conveniently determined.

Since the order of a $k$‑cycle is $k$ and distinct cycles are pairwise disjoint, the order of the permutation $\sigma$ is

$$
\operatorname{lcm}\{k:\alpha_k>0\}.
$$

Similarly, since the parity of a $k$‑cycle is opposite to the parity of $k$, the parity of the permutation $\sigma$ is the parity of

$$
\sum_k(k-1)\alpha_k=\sum_{k}k\alpha_k-\sum_{k}\alpha_k=n-c(\sigma)
$$

Here, $c(\sigma)$ is the number of cycles (including $1$‑cycles, i.e. fixed points).

The cycle type of a permutation plays an important role in [Pólya counting](./combinatorics/polya.md).

## Arrangements

If the set $X$ itself has a natural order, the permutation $\sigma$ is often called an arrangement and written in one-line notation

$$
\sigma(1)\sigma(2)\cdots\sigma(n)
$$

Be careful not to confuse this with cycles.

### Inversion number

In an arrangement, if some larger number comes before some smaller number, we say that these two numbers form an **inversion**. The comparison here is made under the natural order.

The total number of inversions appearing in an arrangement is called the **inversion number** of the arrangement. The inversion number of an arrangement is the minimum number of adjacent swaps needed to restore it to the sorted ascending sequence. Hence the parity of the inversion number of an arrangement coincides with the parity of the corresponding permutation. This can serve as an equivalent definition of the parity of a permutation.

To compute the inversion number, one can use [merge sort](../basic/merge-sort.md#inversions) or a [Fenwick tree](../ds/fenwick.md#global-inversions-global-two-dimensional-partial-order); the time complexity of both is $O(n\log n)$. Explanations of both algorithms can be found in the corresponding chapters; here we give their reference implementations.

??? example "Reference implementation"
    === "Merge sort"
        ```cpp
        --8<-- "docs/math/code/permutation/inversion_2.cpp"
        ```
    
    === "Fenwick tree"
        ```cpp
        --8<-- "docs/math/code/permutation/inversion_1.cpp"
        ```

### Order

Arrangements can be compared. Since each one-line notation is a string, the order of arrangements is the [lexicographic order](../string/basic.md#lexicographic-order) on these strings.

In the C++ standard library header `<algorithm>`, `prev_permutation` and `next_permutation` can be used to find the previous and next arrangement of the current one in lexicographic order, respectively.

### Rank

If the arrangements of $n$ elements are listed in lexicographic order from smallest to largest, the position of a given arrangement in this sequence is the rank of that arrangement. It establishes a one-to-one correspondence between arrangements and positive integers, and is often used for state compression in arrangement-related problems.

In the Chinese competitive programming community, this rank is often called the "Cantor expansion" of the arrangement, but this name is not quite standard. More rigorously, the **Cantor expansion** of the rank of an arrangement corresponds to the **Lehmer code** of that arrangement.

??? info "About the “Cantor expansion”"
    As the name suggests, the Cantor expansion is a method of expanding a natural number into a sequence. It can be viewed as a special numeral system, also called the [factorial number system](./numeral-sys/base.md#mixed-radix). In this numeral system, different positions have different radices. For example, the decimal number $463_{10}$ can be written in the factorial number system as
    
    $$
    463_{10}=341010_{!}.
    $$
    
    It means the following
    
    $$
    463=3\times 5!+4\times 4!+1\times 3!+0\times 2!+1\times 1!+0\times 0!.
    $$
    
    Cantor studied such mixed-radix numeral systems, so the digit representation of a natural number in this system is often also called the Cantor expansion of the natural number.

??? example "Example"
    Readers unfamiliar with how to compute the rank can use this simple example to understand the basic idea of the algorithm below.
    
    To compute the rank of the arrangement $\sigma=452631$ is to compute how many arrangements are lexicographically smaller than $\sigma$, and add one. The idea here is similar to [digit DP](../dp/number.md): we discuss position by position.
    
    -   The choice for position $1$ must be smaller than in $\sigma$, so it can only come from $\{1,2,3\}$, and the remaining $5$ positions can be chosen arbitrarily; $3\times 5!$ possible arrangements in total;
    -   If position $1$ is also chosen as $4$, then the choice for position $2$ must be smaller than in $\sigma$, so it can only come from $\{1,2,3\}$ (here $4$ has already been chosen), and the remaining $4$ positions can be chosen arbitrarily; $3\times 4!$ possible arrangements in total;
    -   Similarly, when the choices for the first $2$ positions agree with $\sigma$, the choice for position $3$ must be smaller than in $\sigma$, so it can only come from $\{1\}$, and the remaining $3$ positions can be chosen arbitrarily; $1\times 3!$ possible arrangements in total;
    -   When the choices for the first $3$ positions agree with $\sigma$, the choice for position $4$ must be smaller than in $\sigma$, so it can only come from $\{1,3\}$, and the remaining $2$ positions can be chosen arbitrarily; $2\times 2!$ possible arrangements in total;
    -   When the choices for the first $4$ positions agree with $\sigma$, the choice for position $5$ must be smaller than in $\sigma$, so it can only come from $\{1\}$, and the remaining $1$ position can be chosen arbitrarily; $1\times 1!$ possible arrangements in total;
    -   When the choices for the first $5$ positions agree with $\sigma$, the choice for position $6$ cannot yield an arrangement smaller than $\sigma$, so there are $0\times 0!$ possible arrangements in total.
    
    Therefore, the rank of the arrangement $\sigma$ is
    
    $$
    1+3\times 5!+3\times 4!+1\times 3!+2\times 2!+1\times 1!+0\times 0!=444.
    $$
    
    For different arrangements, the key point is to determine the coefficients in front of the factorials. In fact, these coefficients are exactly the number of elements that come after that position but are smaller than the element at that position.

From the example we see that the algorithm for computing the rank of a given arrangement can be divided into two steps:

1.  Convert the given arrangement of length $n$ into its Lehmer code, i.e. the sequence $L_\sigma$ of length $n$ whose $i$-th entry is

    $$
    L_\sigma(i)=\#\{j>i:\sigma(j)<\sigma(i)\},
    $$

    that is, the number of elements in the arrangement that come after position $i$ but are smaller than $\sigma(i)$. It equals the rank of the given element among the not-yet-used elements (minus one).

2.  Regard the Lehmer code as the Cantor expansion of a natural number, compute the original natural number, and add one. In other words, the final rank equals

    $$
    \operatorname{rank}\sigma=1+L_\sigma(1)(n-1)!+L_\sigma(2)(n-2)!+\cdots+L_\sigma(n)0!.
    $$

To solve the inverse problem, i.e. to find the corresponding arrangement given its rank, simply run the above process in reverse. The sum of the numbers in the Lehmer code obtained in this process is exactly the inversion number of the arrangement.

In the programming implementation, the key is to be able to quickly compute "the rank of a given element among the not-yet-used elements" (when computing the rank) and "the element of a given rank among the not-yet-used elements" (when computing the arrangement); all of these can be maintained with data structures such as a [Fenwick tree](../ds/fenwick.md) or a [segment tree](../ds/seg.md). The time complexity of both the forward and the inverse operation is $O(n\log n)$.

??? example "Reference implementation"
    === "Rank of a given arrangement"
        ```cpp
        --8<-- "docs/math/code/permutation/perm_rank.cpp"
        ```
    
    === "Arrangement of a given rank"
        ```cpp
        --8<-- "docs/math/code/permutation/rank_perm.cpp"
        ```

## References and notes

-   [Permutation - Wikipedia](https://en.wikipedia.org/wiki/Permutation)
-   [Lehmer code - Wikipedia](https://en.wikipedia.org/wiki/Lehmer_code)
-   [Factorial number system - Wikipedia](https://en.wikipedia.org/wiki/Factorial_number_system)
