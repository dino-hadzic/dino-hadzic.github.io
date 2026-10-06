---
title: Lookup tables
---

Prerequisite: [Block decomposition](../ds/decompose.md).

Naive table lookup (打表) means computing and storing, at contest time, the answers for all possible inputs, then declaring an array in the code, putting the answers into it and simply printing them.

Note that this trick only applies to problems where the input range is small (e.g. the input is a single number with a small range); otherwise it may lead to overly long code, MLE, or the table taking too long to compute.

???+ note "Example"
    Let $f(x)$ be the number of $1$s in the binary representation of the integer $x$. Given a positive integer $n$ ($n\leq 10^9$), output $\sum_{i=1}^n f^2(i)$.

If we stored the answer for every $n$, besides possibly getting MLE, the code might exceed the maximum code length limit and fail to compile.

So we optimise the answer table. Using the idea of [block decomposition](../ds/decompose.md), we choose a reasonable step $m$ (usually determined by the code length limit) and for the $i$-th block compute

$$
\sum_{k=\frac{n}{m}(i-1)+1}^{\frac{ni}{m}} f^2(k)
$$

When outputting the answer we use the block idea: whole blocks are computed from the precomputed values, and partial blocks by brute force.

Generally, in such problems a single function value $f(x)$ is quick to compute, but a huge number of values must be summed (multiplied, or combined with some other quickly mergeable operation), and enumeration exceeds the time limit. When no standard approach can be found, a blocked lookup table is a good choice.

???+ note "Note"
    When the exponent in the problem above is not fixed but has a small range, a lookup table can also be considered.

### Problems

[「BZOJ 3798」特殊的质数](https://hydro.ac/p/bzoj-P3798): count the primes in $[l,r]$ that can be written as the sum of the squares of two positive integers.

[「Luogu P1822」魔法指纹](https://www.luogu.com.cn/problem/P1822)
