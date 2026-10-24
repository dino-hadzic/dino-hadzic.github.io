---
title: 2D Mo's algorithm
---

2D Mo's algorithm, as the name suggests, is Mo's algorithm in which every state can be extended in four directions.

In 2D Mo's algorithm every pointer move processes the numbers of a whole row or column; the concrete implementation is similar to ordinary one-dimensional Mo's algorithm and is not repeated here. Here we focus on the choice of the block size.

## Choosing the block size

Let the number of queries be $q$, let the top-left corner of the current matrix be $(x_1,\ y_1)$ and the bottom-right corner $(x_2,\ y_2)$, and let the block size be $B$.

Then the pointer $x_1$ moves $\Theta(q\cdot B)$ times, while the pointer $y_2$ moves $\Theta(n^4\cdot B^{-3})$ times.

So it suffices to set $q\cdot B=n^4\cdot B^{-3}$, i.e. $B=n\cdot q^{-\frac 14}$.

Note that $B$ computed this way **may be $0$**, so **handle this case specially**.

Finally, the time complexity of the computation part is $\Theta(n^2\cdot q^{\frac 34})$; adding the sorting of the queries, the total time complexity is $\Theta(n^2\cdot q^{\frac 34}+q\log q)$.

## Example problem 1

???+ note "[BZOJ 2639 矩形计算 (Rectangle Computation)](https://hydro.ac/p/bzoj-P2639)"
    You are given an $n\times m$ matrix whose every element is an integer, followed by $q$ queries; each query asks for the weight of a submatrix. The weight of a matrix is defined as follows: for an integer $x$, if it appears $p$ times in the matrix, it contributes $p^2$ to the weight of the matrix.
    
    Constraints: $1\leq n,\ m\leq 200$, $0\leq q\leq 10^5$, $|$ matrix element $| \leq 2\times 10^9$.

??? note "Solution idea"
    First discretize the values; then, in the 2D Mo's algorithm, use an array to record the current number of occurrences of each number.

??? note "Sample code"
    ```cpp
    --8<-- "docs/misc/code/mo-algo-2dimen/mo-algo-2dimen_1.cpp"
    ```

## Example problem 2

???+ note "[Luogu P1527 \[国家集训队\] 矩阵乘法 (Matrix Multiplication)](https://www.luogu.com.cn/problem/P1527)"
    You are given an $n\times n$ matrix and $q$ queries; each query asks for the $k$-th smallest number in a subrectangle.
    
    Constraints: $1\leq n\leq 500$, $1\leq q\leq 6\times 10^4$, $0\leq a_{i,j}\leq 10^9$.

First, as in the previous problem, the whole matrix needs to be discretized. Note, however, that in this problem, besides splitting the positions into blocks, we also need to split the value range into blocks (value-range blocking) in order to compute the answer.

Here we also need odd-even sorting as an optimization; for details see [Ordinary Mo's algorithm](../misc/mo-algo.md#普通莫队的优化).

For this problem the time limit is not very generous, so pay attention to the constant factor of the code. The computed block size is generally small: when $n$ and $q$ both take their maximum values the block size is about $11$, so it can be set directly as a constant to save running time.

??? note "Sample code"
    ```cpp
    --8<-- "docs/misc/code/mo-algo-2dimen/mo-algo-2dimen_2.cpp"
    ```
