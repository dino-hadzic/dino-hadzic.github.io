---
title: The idea of sqrt decomposition
---

## Introduction

In fact, sqrt decomposition (decomposition into blocks) is an idea, not a data structure.

From NOIP through NOI to IOI, the idea of decomposition into blocks appears at every level of difficulty.

The basic idea of decomposition into blocks is to partition the original data appropriately and precompute some information on each of the resulting blocks, thereby obtaining a better time complexity than the usual brute-force algorithm.

The time complexity of decomposition into blocks depends mainly on the block length; the optimal block length for a given problem, together with the corresponding time complexity, can usually be found via the AM-GM inequality.

Decomposition into blocks is a very flexible idea. Compared with the Fenwick tree and the segment tree, its advantage is better generality: it can maintain many kinds of information that Fenwick trees and segment trees cannot.

Of course, the drawback of decomposition into blocks is that its asymptotic complexity is worse than that of the segment tree and the Fenwick tree.

Still, for most problems decomposition into blocks remains a good choice for solving them.

Below are a few examples.

## Range sum

??? note "Example problem [LibreOJ 6280 Sequence Block Decomposition Intro 4](https://loj.ac/problem/6280)"
    Given a sequence $\{a_i\}$ of length $n$, perform $n$ operations. There are two kinds of operations:
    
    1.  add $x$ to all numbers from $a_l$ to $a_r$;
    2.  compute $\sum_{i=l}^r a_i$.
    
        $1 \leq n \leq 5 \times 10^4$

We split the sequence into blocks of $s$ elements each and record the range sum $b_i$ of each block.

$$
\underbrace{a_1, a_2, \ldots, a_s}_{b_1}, \underbrace{a_{s+1}, \ldots, a_{2s}}_{b_2}, \dots, \underbrace{a_{(s-1) \times s+1}, \dots, a_n}_{b_{\frac{n}{s}}}
$$

The last block may be incomplete (since $n$ is very likely not a multiple of $s$), but this does not affect our discussion much.

First look at the query operation:

-   If $l$ and $r$ are in the same block, simply sum by brute force; since the block length is $s$, the worst-case complexity is $O(s)$.
-   If $l$ and $r$ are not in the same block, the answer consists of three parts: the incomplete block starting at $l$, several complete blocks in the middle, and the incomplete block ending at $r$. For the incomplete blocks we still use the brute-force computation above; for the complete blocks we directly sum the already computed $b_i$. In this case the worst-case complexity is $O(\dfrac{n}{s}+s)$.

Next the update operation:

-   If $l$ and $r$ are in the same block, simply update by brute force; since the block length is $s$, the worst-case complexity is $O(s)$.
-   If $l$ and $r$ are not in the same block, three parts have to be updated: the incomplete block starting at $l$, several complete blocks in the middle, and the incomplete block ending at $r$. For the incomplete blocks we still update the value of each element by brute force (don't forget to update the range sum $b_i$); for the complete blocks we directly modify $b_i$. In this case the worst-case complexity is still $O(\dfrac{n}{s}+s)$.

By the AM-GM inequality, the time complexity of a single operation is optimal when $\dfrac{n}{s}=s$, i.e. $s=\sqrt n$, and equals $O(\sqrt n)$.

??? note "Reference code"
    ```cpp
    --8<-- "docs/ds/code/decompose/decompose_1.cpp"
    ```

## Range sum 2

The complexity of the previous approach is $\Omega(1) , O(\sqrt{n})$.

Here we introduce an $O(\sqrt{n}) - O(1)$ algorithm.

For $O(1)$ queries we can maintain various prefix sums.

However, with updates they are inconvenient to maintain; we can only maintain prefix sums within a single block.

And prefix sums over whole blocks taken as units.

Each update costs $O(T+\frac{n}{T})$.

Query: involves three parts, each of which can be obtained directly from prefix sums, time complexity $O(1)$.

## Decomposing the queries into blocks

The same problem, but now the sequence has length $n$ and there are $m$ operations.

If the number of operations is relatively small, we can record the operations and add their effect at query time.

Suppose at most $T$ operations are recorded; then an update is $O(1)$ and a query is $O(T)$.

After $T$ operations, recompute the prefix sums, $O(n)$.

Total complexity: $O(mT+n\frac{m}{T})$.

For $T=\sqrt{n}$ the total complexity is $O(m \sqrt{n})$.

### Other problems

The idea of decomposition into blocks can also be applied to other integer-related problems: finding the number of zero elements, finding the first nonzero element, counting the elements satisfying some property, and so on.

There are also other problems that can be solved by decomposition into blocks, e.g. maintaining a set of numbers that allows adding and removing numbers, checking whether a number belongs to the set, and finding the $k$-th largest number. To solve this problem, the numbers must be stored in increasing order and split into several blocks, each containing $\sqrt{n}$ numbers. Every time a number is added or removed, the blocks must be rebalanced by moving numbers across the boundaries of adjacent blocks.

A well-known offline algorithm, [Mo's algorithm](../misc/mo-algo.md), is also based on the idea of decomposition into blocks.

## Practice problems

-   [UVa - 12003 - Array Transformer](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3154)
-   [UVa - 11990 Dynamic Inversion](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3141)
-   [SPOJ - Give Away](http://www.spoj.com/problems/GIVEAWAY/)
-   [Codeforces - Till I Collapse](http://codeforces.com/contest/786/problem/C)
-   [Codeforces - Destiny](http://codeforces.com/contest/840/problem/D)
-   [Codeforces - Holes](http://codeforces.com/contest/13/problem/E)
-   [Codeforces - XOR and Favorite Number](https://codeforces.com/problemset/problem/617/E)
-   [Codeforces - Powerful array](http://codeforces.com/problemset/problem/86/D)
-   [SPOJ - DQUERY](https://www.spoj.com/problems/DQUERY)

    **This page is mainly translated from the blog post [Sqrt-декомпозиция](http://e-maxx.ru/algo/sqrt_decomposition) and its English translation [Sqrt Decomposition](https://cp-algorithms.com/data_structures/sqrt_decomposition.html). The Russian version is licensed under Public Domain + Leave a Link; the English version is licensed under CC-BY-SA 4.0.**
