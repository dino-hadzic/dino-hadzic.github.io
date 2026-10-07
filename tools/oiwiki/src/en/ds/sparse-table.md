---
title: Sparse table
---

## Definition

![Sparse table diagram](images/st.svg)

The ST table (Sparse Table) is a data structure for solving **repeatable contribution problems**.

???+ note "What is a repeatable contribution problem?"
    A **repeatable contribution problem** (idempotent operation) is a range query for an operation $\operatorname{opt}$ satisfying $x\operatorname{opt} x=x$. For example, the maximum satisfies $\max(x,x)=x$ and gcd satisfies $\operatorname{gcd}(x,x)=x$, so RMQ and range GCD are repeatable contribution problems. Range sum does not have this property: if the precomputed ranges used to compute a range sum overlap, the overlapping part is counted twice, which we do not want. In addition, $\operatorname{opt}$ must also be associative for the sparse table to be applicable.

???+ note "What is RMQ?"
    RMQ stands for Range Maximum/Minimum Query, i.e. the maximum (minimum) over a range. There are many ways to solve the RMQ problem; see the [RMQ topic](../topic/rmq.md).

## Introduction

???+ example "[Luogu P3865【模板】ST 表 & RMQ 问题](https://www.luogu.com.cn/problem/P3865)"
    Given $n$ ($1\le n\le 10^5$) integers and $m$ ($1\le m\le 2\times 10^6$) queries, for each query you need to answer the maximum over the range $[l,r]$.

Consider the brute-force approach. For every query, scan the range $[l,r]$ once and find the maximum.

Clearly this algorithm exceeds the time limit.

## Sparse table

The sparse table is based on the idea of [binary lifting](../basic/binary-lifting.md); it achieves $\Theta(n\log n)$ preprocessing and answers each query in $\Theta(1)$. It does not support updates.

Based on the idea of binary lifting, let us think about how to find the range maximum. We can see that if we follow the usual binary lifting procedure and jump $2^i$ steps each time, the query complexity is still $\Theta(\log n)$, which is no better than a segment tree, and the preprocessing step is even slower than a segment tree.

We notice that $\max(x,x)=x$, i.e. range maximum is a problem with the "repeatable contribution" property. Even if the precomputed ranges used to compute it overlap, the final answer is correct as long as the union of these ranges is the queried range.

If we simulate by hand, we find that we can cover the query range with at most two precomputed ranges, i.e. the query time complexity can be reduced to $\Theta(1)$, which is very effective for problems with a huge number of queries.

The concrete implementation is as follows:

Let $f(i,j)$ denote the maximum over the range $[i,i+2^j-1]$.

Clearly $f(i,0)=a_i$.

By the definition, the second dimension corresponds to "jumping $2^j-1$ steps" in binary lifting; following the binary lifting idea, we write the state transition: $f(i,j)=\max(f(i,j-1),f(i+2^{j-1},j-1))$.

![](./images/st-preprocess-lift.svg)

That is the preprocessing part. Queries can be implemented simply as follows:

For every query $[l,r]$, split it into two parts: $[l,l+2^s-1]$ and $[r-2^s+1,r]$, where $s=\left\lfloor\log_2(r-l+1)\right\rfloor$. The maximum of the results of the two parts is the answer.

![Query procedure of a sparse table](./images/st-query.svg)

By the argument about "repeatable contribution problems" above, since the maximum is a "repeatable contribution problem", the overlap does not affect the range maximum. And since these two ranges completely cover $[l,r]$, the correctness of the answer is guaranteed.

???+ example "[Luogu P3865【模板】ST 表 & RMQ 问题](https://www.luogu.com.cn/problem/P3865) reference implementation"
    === "C style"
        ```cpp
        --8<-- "docs/ds/code/sparse-table/sparse-table_1.cpp"
        ```
    
    === "C++ style"
        ```cpp
        --8<-- "docs/ds/code/sparse-table/sparse-table_2.cpp"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/ds/code/sparse-table/sparse-table_1.py"
        ```

## Notes

1.  There is usually a lot of input and output, so enabling I/O optimization is recommended.

2.  When preprocessing a sparse table, one usually needs an array with one dimension of size $\log n$ and the other of size $n$; the dimension of size $\log n$ should be the first one, to improve cache locality.

3.  Recomputing the logarithm with [std::log](https://en.cppreference.com/w/cpp/numeric/math/log) every time is not worth it; it is recommended to compute it with builtin functions such as `__builtin_clz` or `__lg`. If these builtins are unavailable, the logarithm values can also be precomputed. The precomputation is as follows:

$$
\begin{cases}
\texttt{Logn}[1] \gets 0, \\
\texttt{Logn}\left[i\right] \gets \texttt{Logn}\left[\frac{i}{2}\right] + 1.
\end{cases}
$$

## Maintaining other information with a sparse table

Besides RMQ there are other "repeatable contribution problems". For example "range bitwise AND", "range bitwise OR" and "range GCD" can all be solved efficiently by a sparse table.

Note that for "range GCD" the query complexity of a sparse table is not better than that of a segment tree (letting the value range be $w$, the query complexity of a sparse table is $\Theta(\log w)$, while that of a segment tree is $\Theta(\log n+\log w)$, and the value range is usually larger than $n$), but the preprocessing complexity of a sparse table is not worse than that of a segment tree either, and in terms of coding complexity a sparse table is much simpler than a segment tree.

If we analyze it, "repeatable contribution problems" generally carry some RMQ-like component. For example, "range bitwise AND" takes the minimum of every bit, and "range GCD" takes the minimum of the exponent of every prime factor.

## Summary

A sparse table maintains "repeatable contribution" range information (which must also be associative) well, with low time complexity and very little code compared with other algorithms. However, the information a sparse table can maintain is very limited, it does not extend well, and it does not support updates.

## Exercises

-   ["SCOI2007" 降雨量](https://loj.ac/p/2279)

-   [\[USACO07JAN\] Balanced Lineup](https://www.luogu.com.cn/problem/P2880)

## Appendix: time complexity analysis of range GCD with a sparse table

While the algorithm runs, there may be $\Theta(\log n)$ iterations. Each iteration may call the GCD function recursively; letting the value range be $w$, the time complexity of the GCD function is at most $\Omega(\log w)$, so the total time complexity appears to be $O(n\log n\log w)$.

However, during GCD, every recursive call (except the last one) at least halves some number in the sequence, and the numbers in the sequence can be halved at most $\log_2 (w^n)=\Theta(n\log w)$ times, so the recursive part of GCD runs at most $O(n\log w)$ times. Adding the $\Theta(n\log n)$ of the loops (and of the last level of recursion), the final time complexity is $O(n(\log w+\log n))$; since data can be constructed so that the time complexity is $\Omega(n(\log w+\log n))$, the final time complexity is $\Theta(n(\log w+\log n))$.

The time complexity of the query part is easy to analyze: consider the worst case, where every query asks about the worst pair of numbers; the time complexity is $\Theta(\log w)$. Therefore the time complexity of maintaining "range GCD" with a sparse table is $\Theta(n(\log n+\log w))$ preprocessing and $\Theta(\log w)$ per query.

The corresponding operations of a segment tree are $\Theta(n\log w)$ preprocessing and $\Theta(\log n+\log w)$ per query.

This is not a rigorous mathematical argument; a more rigorous one follows:

??? note "A more rigorous proof"
    Understanding this part may require knowledge of the "potential method" from [Time complexity](../basic/complexity.md).
    
    First we analyze the time complexity of the preprocessing part:
    
    Let the "sequence under consideration" be the sequence of the current level of the loop when preprocessing the sparse table. For example, the sequence of level zero is the original sequence, and the sequence of level one is the sequence of level zero after one iteration, i.e. `st[1..n][1]`; denote it by $A$.
    
    The potential function is defined as the base-two logarithm of the product of all numbers in the "sequence under consideration", i.e. $\Phi(A)=\log_2\left(\prod\limits_{i=1}^n A_i\right)$.
    
    In one iteration, the time spent equals the time spent by the loop plus the time spent by GCD. The time spent by GCD varies: at the shortest it may be only two or even one recursive call, and at the longest it may be $O(\log w)$ recursive calls. However, during GCD, except for the very first and the very last level, every recursive call at least halves some result in the "sequence under consideration". That is, $\Phi(A)$ decreases by at least $1$, so the time spent on that level of recursion can be amortized by the potential function.
    
    At the same time, we can see that the initial value of $\Phi(A)$ is at most $\log_2 (w^n)=\Theta(n\log w)$, and $\Phi(A)$ never increases. Therefore the time complexity of the preprocessing part of the sparse table is $O(n(\log w+\log n))$.
