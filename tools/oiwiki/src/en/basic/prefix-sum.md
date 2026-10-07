---
title: Prefix sums & difference arrays
---

## Introduction

Prefix sums and difference arrays are techniques commonly used in algorithm competitions: the former for quickly computing range sums, the latter for efficiently performing range updates.

???+ tip "Convention"
    For ease of discussion, in this article the indices of the array $\{a_i\}$ start from $1$, and we additionally define $a_0 = 0$.

## Prefix sums

A prefix sum can be simply understood as "the sum of the first $n$ terms of a sequence"; it is an important form of preprocessing.

### One-dimensional prefix sums

For a sequence $\{a_i\}$ of length $n$, if we need to answer many queries for the sum of the numbers in a range $[l,r]$, we can consider using prefix sums. The prefix sum of the sequence is

$$
S_{i} = \sum_{j=1}^i a_j.
$$

It can be computed term by term from the recurrence

$$
S_0 = 0,~ S_i = S_{i-1} + a_i.
$$

To query the sum of the sequence over the range $[l,r]$, we only need to compute the difference

$$
S([l,r]) = S_r - S_{l-1}.
$$

Thus, with $O(n)$ preprocessing, the complexity of a single range-sum query is reduced to $O(1)$.

???+ example "Reference implementation"
    === "C++"
        ```cpp
        --8<-- "docs/basic/code/prefix-sum/prefix-sum_1.cpp:core"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/basic/code/prefix-sum/prefix-sum_1.py:core"
        ```

The C++ standard library implements the prefix-sum function [`std::partial_sum`](https://en.cppreference.com/w/cpp/algorithm/partial_sum), defined in the header `<numeric>`. Since C++17 the standard library also provides a functionally identical prefix-sum function, [`std::inclusive_scan`](https://en.cppreference.com/w/cpp/algorithm/inclusive_scan), likewise defined in the header `<numeric>`.

### Two-dimensional/multidimensional prefix sums

Extending one-dimensional prefix sums to several dimensions gives multidimensional prefix sums. There are two common methods for computing them.

#### Based on the inclusion-exclusion principle

This method is mostly used for two-dimensional prefix sums. Given a two-dimensional array $A$ of size $m\times n$, we want its prefix sum $S$. Then $S$ is also a two-dimensional array of size $m\times n$, and

$$
S_{i,j} = \sum_{i'\le i}\sum_{j'\le j}A_{i',j'}.
$$

By analogy with the one-dimensional case, $S_{i,j}$ should be computable from $S_{i-1,j}$ or $S_{i,j-1}$, which avoids re-summing the earlier terms. However, if we simply add $S_{i-1,j}$ and $S_{i,j-1}$ and then add $A_{i,j}$, the prefix sum of the overlapping part $S_{i-1,j-1}$ is counted twice, so this part has to be subtracted again. This is the [inclusion-exclusion principle](../math/combinatorics/inclusion-exclusion-principle.md). We obtain the following recurrence:

$$
S_{i,j} = A_{i,j} + S_{i-1,j} + S_{i,j-1} - S_{i-1,j-1}. 
$$

In the implementation, it suffices to iterate over all $(i,j)$ directly and sum.

???+ note "Example"
    Consider a concrete example.
    
    ![Two-dimensional prefix sum example](./images/prefix-sum-2d.svg)
    
    Here $S$ is the prefix sum of the matrix $A$. By definition, $S_{3,3}$ is the sum of the submatrix inside the dashed box in the left figure. Moreover, $S_{3,2}$ is the sum of the blue submatrix, $S_{2,3}$ is the sum of the red submatrix, and the sum of their overlap is $S_{2,2}$. We see that adding $S_{3,2}$ and $S_{2,3}$ directly would count $S_{2,2}$ twice, so we should have
    
    $$
    S_{3,3} = A_{3,3} + S_{2,3} + S_{3,2} - S_{2,2} = 5 + 18 + 15 - 9 = 29.
    $$

By the same reasoning, once the two-dimensional prefix sums have been preprocessed, the sum of the submatrix with upper-left corner $(i_1,j_1)$ and lower-right corner $(i_2,j_2)$ can be computed as

$$
S_{i_2,j_2} - S_{i_1-1,j_2} - S_{i_2,j_1-1} + S_{i_1-1,j_1-1}.
$$

This can be done in $O(1)$ time.

In the two-dimensional case, the time complexity of the above algorithm can simply be regarded as $O(mn)$, i.e. linear in the size of the given array. However, as the dimension $k$ grows, the number of terms involved in inclusion-exclusion grows exponentially, so the time complexity becomes $O(2^kN)$, where $k$ is the dimension of the array and $N$ is the size of the given array. Hence this algorithm is no longer suitable.

???+ example "[Luogu P1387 Largest Square](https://www.luogu.com.cn/problem/P1387)"
    In an $n\times m$ matrix containing only $0$s and $1$s, find the largest square that contains no $0$ and output its side length.

??? note "Reference code"
    === "C++"
        ```cpp
        --8<-- "docs/basic/code/prefix-sum/prefix-sum_2.cpp:full-text"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/basic/code/prefix-sum/prefix-sum_2.py:full-text"
        ```

#### Dimension-by-dimension prefix sums

In the general case, given a $k$-dimensional array $A$ of size $N$, we again want its prefix sum $S$. Here,

$$
S_{i_1,\cdots,i_k} = \sum_{i'_1\le i_1}\cdots\sum_{i'_k\le i_k} A_{i'_1,\cdots,i'_k}.
$$

From the formula we can see that a $k$-dimensional prefix sum equals $k$ successive summations. So an obvious algorithm is: at each step consider only one dimension, fix all the other dimensions, and compute a number of one-dimensional prefix sums; after doing this for all $k$ dimensions, the result is the $k$-dimensional prefix sum.

??? example "Reference implementation of a three-dimensional prefix sum"
    ```cpp
    --8<-- "docs/basic/code/prefix-sum/prefix-sum_4.cpp:core"
    ```

Since for each dimension the whole array is traversed only once, the complexity of this algorithm is $O(kN)$, which is usually acceptable.

#### Special case: sum over subsets DP

The high-dimensional case often appears in a class of problems called **sum over subsets** (SOS). This is a special case of high-dimensional prefix sums.

The problem is as follows. Consider a function $f$ defined on all subsets of a set of size $n$; we want its sum-over-subsets function $g$, which satisfies

$$
g(S) = \sum_{T\subseteq S}f(T).
$$

That is, $g(S)$ equals the sum of the values $f(T)$ over all its subsets $T\subseteq S$.

First, the sum-over-subsets problem can be written in the form of a high-dimensional prefix sum. Note that any subset $S$ can be represented, using the idea of bitmasks, as a 0-1 string $s$ of length $n$, and a subset $T$ corresponds to a string $t$. Treat each bit of the string as one dimension of the array index; then $f$ is really an $n$-dimensional array in which every index is in $\{0,1\}$. At the same time, the subset relation is equivalent to the ordering of indices, i.e.

$$
T\subseteq S \iff \forall i(t_i \le s_i). 
$$

Therefore, summing over subsets is computing the prefix sum of this $n$-dimensional array.

Now we can directly use the dimension-by-dimension prefix-sum method described above to obtain the sum over subsets. The time complexity is $O(n2^n)$.

??? example "Reference implementation"
    ```cpp
    --8<-- "docs/basic/code/prefix-sum/prefix-sum_5.cpp:core"
    ```

The inverse of the sum over subsets is carried out via the [inclusion-exclusion principle](../math/combinatorics/inclusion-exclusion-principle.md). The sum-over-subsets problem is also one of the necessary steps of the fast Möbius transform.

### Prefix sums on trees

One-dimensional prefix sums can also be generalized to rooted trees (with root $1$). By preprocessing prefix sums we can quickly compute the sum of weights along a path in the tree.

#### Weights on vertices

First we discuss the case where the weights are stored at the vertices. Let vertex $x$ have weight $a_x$. Through the recurrence

$$
S_1 = a_1,~ S_{x} = S_{\operatorname{fa}(x)} + a_x
$$

we obtain the sum of the weights of the vertices on the path from the root to vertex $x$, where $\operatorname{fa}(x)$ denotes the parent of $x$. After preprocessing the prefix sums, the sum of vertex weights on the path connecting vertices $x$ and $y$ can be computed as

$$
S_x + S_y - S_{\operatorname{lca}(x, y)} - S_{\operatorname{fa}(\operatorname{lca}(x, y))}.
$$

Here $\operatorname{lca}(x, y)$ denotes the [lowest common ancestor](../graph/lca.md) (LCA) of vertices $x$ and $y$.

#### Weights on edges

The case where the weights are stored on the edges can almost be reduced to the vertex-weight case. For every non-root vertex $x\neq 1$, let $\operatorname{edge}(x)$ denote the edge connecting vertex $x$ to its parent $\operatorname{fa}(x)$. Then we may assume that the edge weight is stored at the vertex farther from the root. In other words, vertex $x$ stores the weight of the edge $\operatorname{edge}(x)$. The root stores the weight $0$. Then, using the recurrence discussed in the previous subsection, we can likewise preprocess the sum $S_x$ of the weights of all edges on the path from the root to vertex $x$.

Now the sum of the edge weights on the path connecting vertices $x$ and $y$ can be queried as

$$
S_x + S_y - 2S_{\operatorname{lca}(x, y)}.
$$

Note that, unlike the vertex-weight case, the queried sum does not include the weight stored at $\operatorname{lca}(x, y)$, because the edge weight it stores is not on the desired path.

#### Subtree sums

Unlike arrays, a tree is not symmetric between its two ends, so computing a "prefix sum" bottom-up (from leaves to root) and top-down (from root to leaves) gives different results. In general, "prefix sums on trees" refers to the prefix sum computed top-down. For ease of discussion, this article calls the "prefix sum" computed bottom-up the **subtree sum**.

The sum of the vertex weights of the subtree rooted at vertex $x$, i.e. the corresponding subtree sum, is

$$
T_x = \sum_{y\in\operatorname{desc}(x)} a_y.
$$

Here $\operatorname{desc}(x)$ denotes the set of all descendants of $x$ (including $x$ itself).

Unlike prefix sums on trees, subtree sums cannot be used to compute path weight sums in $O(1)$, but they help in understanding the tree difference arrays below.

## Difference arrays

Difference arrays are the strategy opposite to prefix sums: the inverse operation of the prefix sum. Rather than computing the difference array of a given sequence, the more common scenario in competitions is to maintain the difference array in order to perform many range updates. After the range updates are finished, the original sequence can be recovered via prefix sums to answer queries about it. Note that all updates must come before the queries.

If mixed updates and queries have to be supported many times, a [Fenwick tree](../ds/fenwick.md) is needed, but the underlying idea is the same.

### One-dimensional difference arrays

For a sequence $\{a_i\}$, its difference array $\{D_i\}$ is

$$
D_i = a_i - a_{i-1},~ a_0 = 0.
$$

The C++ standard library implements the difference function [`std::adjacent_difference`](https://en.cppreference.com/w/cpp/algorithm/adjacent_difference), defined in the header `<numeric>`.

The relationship between prefix sums and difference arrays is as follows:

???+ note "Property"
    Let $\{D_i\}$ be the difference array of $\{a_i\}$. Then:
    
    -   the sequence $\{a_i\}$ is the prefix sum of the sequence $\{D_i\}$, i.e.
    
        $$
        a_i = \sum_{j=1}^i D_j.
        $$
    -   the prefix sum of the sequence $\{a_i\}$ is
    
        $$
        S_i = \sum_{j=1}^i\sum_{k=1}^jD_k = \sum_{j=1}^i(i-j+1)D_j. 
        $$

Difference arrays are often used when a number has to be added to a range of the sequence many times, and afterwards the value at some position of the sequence is queried one or more times.

Suppose we want to add $v$ to every number of the sequence $\{a_i\}$ in the range $[l,r]$. We can do the following on its difference array $\{D_i\}$:

$$
D_{l} \gets D_{l} + v,~ D_{r+1}\gets D_{r+1} - v.
$$

After all updates are finished, the updated values of $\{a_i\}$ can be recovered with a prefix-sum pass. A single update is $O(1)$. For queries, one $O(n)$ prefix-sum pass is needed, after which every query is $O(1)$.

???+ example "Reference code"
    ```cpp
    --8<-- "docs/basic/code/prefix-sum/prefix-sum_6.cpp:core"
    ```

### Two-dimensional/multidimensional difference arrays

Difference arrays can likewise be generalized to several dimensions. If we regard the multidimensional difference array as the inverse of the multidimensional prefix sum, then computing the multidimensional difference array amounts to recovering the original array from its multidimensional prefix sum. By the earlier discussion, we can use inclusion-exclusion. For example, the two-dimensional difference array is defined as

$$
D_{i,j} = a_{i,j} - a_{i-1,j} - a_{i,j-1} + a_{i-1,j-1}.
$$

However, if the whole difference array has to be computed, the simpler and more efficient approach is dimension-by-dimension differencing: enumerate all dimensions and compute the differences of the array along each of them.

Two-dimensional difference arrays are often used for many rectangle additions on a two-dimensional array. For example, to add $v$ to every number in the matrix with upper-left corner $(x_1,y_1)$ and lower-right corner $(x_2,y_2)$, we can do the following on its difference array $\{D_{i,j}\}$:

$$
\begin{aligned}
D_{x_1,y_1} &\gets D_{x_1,y_1} + v, \\
D_{x_1,y_2+1} &\gets D_{x_1,y_2+1} - v,\\
D_{x_2+1,y_1} &\gets D_{x_2+1,y_1} - v,\\
D_{x_2+1,y_2+1} &\gets D_{x_2+1,y_2+1} + v.
\end{aligned}
$$

After all updates are finished, a single two-dimensional prefix-sum pass is enough to quickly query the values of the updated array.

??? example "Reference code"
    ```cpp
    --8<-- "docs/basic/code/prefix-sum/prefix-sum_7.cpp:core"
    ```

Of course, the same idea also works for dimensions $k>2$, but a single update then needs $O(2^k)$ time, which becomes impractical as $k$ grows.

### Difference arrays on trees

Difference arrays can be generalized to rooted trees to implement range additions along a path in the tree. Depending on whether the maintained information is stored on vertices or on edges, tree difference arrays are divided into **vertex differences** and **edge differences**, which differ slightly in implementation. Also, rather than tree prefix sums, it is more common to compute subtree sums after all updates and then answer queries. This is the case discussed in this section.

#### Vertex differences

To add $v$ to all vertex weights on the path between vertices $x$ and $y$, we can do the following on the difference array $\{D_x\}$:

$$
\begin{aligned}
D_x &\gets D_x + v, \\
D_{\operatorname{lca}(x, y)} &\gets D_{\operatorname{lca}(x, y)} - v,\\
D_y &\gets D_y + v, \\
D_{\operatorname{fa}(\operatorname{lca}(x, y))} &\gets D_{\operatorname{fa}(\operatorname{lca}(x, y))} - v.
\end{aligned}
$$

After all updates are finished, a single subtree-sum pass yields the updated vertex weights.

???+ example "Example"
    When performing a range addition on the vertex weights of the path between vertices $S$ and $T$, the first two formulas above perform a one-dimensional difference operation on the path in the blue box, and the last two perform a one-dimensional difference operation on the path in the red box:
    
    ![](./images/prefix-sum1.svg)
    
    Summing bottom-up amounts to computing the prefix sums of these two ranges from bottom to top. Comparing with the one-dimensional difference operation above shows the correctness of vertex differences.

#### Edge differences

To add $v$ to all edge weights on the path between vertices $x$ and $y$, we can do the following on the difference array $\{D_x\}$:

$$
\begin{aligned}
D_x &\gets D_x + v, \\
D_y &\gets D_y + v, \\
D_{\operatorname{lca}(x, y)} &\gets D_{\operatorname{lca}(x, y)} - 2v.
\end{aligned}
$$

After all updates are finished, a single subtree-sum pass yields the updated edge weights (stored at the child vertex of the corresponding edge).

???+ example "Example"
    As shown in the figure, edge differences can be used to solve the range addition on the edge weights of the red path.
    
    ![](./images/prefix-sum2.svg)
    
    Since differencing directly on edges is difficult, the values that should be accumulated on the red edges are moved down into the adjacent vertices, which makes the operation convenient. Comparing with the vertex-difference formulas explains the edge-difference formulas.

### Example problem

???+ example "[USACO15DEC Max Flow](https://usaco.org/index.php?page=viewproblem2&cpid=576)"
    FJ has installed $N-1$ pipes between the $N(2 \le N \le 50,000)$ stalls of his barn. All stalls are connected by the pipes.
    
    FJ has $K(1 \le K \le 100,000)$ milk transport routes; the $i$-th route transports from stall $s_i$ to stall $t_i$. A transport route adds one unit of pressure to the stalls at its two endpoints and to every stall it passes through along the way. Compute the pressure of the stall with the greatest pressure.

??? note "Solution idea"
    We need to count how many times each vertex is passed through, so we use tree difference arrays to add one to every vertex on each route's path, which quickly gives the number of times each vertex is visited. Here LCA is computed with binary lifting, and finally a DFS traverses the whole tree, summing the difference array while backtracking to obtain the answer.

??? note "Reference code"
    ```cpp
    --8<-- "docs/basic/code/prefix-sum/prefix-sum_3.cpp"
    ```

## Exercises

Prefix sums:

-   [Luogu B3612 Range Sum](https://www.luogu.com.cn/problem/B3612)
-   [Luogu U69096 Inverse of Prefix Sum](https://www.luogu.com.cn/problem/U69096)
-   [AtCoder joi2007ho\_a Maximum Sum](https://atcoder.jp/contests/joi2007ho/tasks/joi2007ho_a)
-   [USACO16JAN Subsequences Summing to Sevens](https://usaco.org/index.php?page=viewproblem2&cpid=595)
-   [USACO05JAN Moo Volume S](https://www.luogu.com.cn/problem/P6067)

Two-dimensional/multidimensional prefix sums:

-   [HDU 6514 Monitor](https://acm.hdu.edu.cn/showproblem.php?pid=6514)
-   [Luogu P1387 Largest Square](https://www.luogu.com.cn/problem/P1387)
-   [HNOI2003 Laser Bomb](https://www.luogu.com.cn/problem/P2280)
-   [CF 165E Compatible Numbers](https://codeforces.com/contest/165/problem/E)
-   [CF 383E Vowels](https://codeforces.com/problemset/problem/383/E)
-   [ARC 100C Or Plus Max](https://atcoder.jp/contests/arc100/tasks/arc100_c)

Prefix sums on trees:

-   [LOJ 10134. Dis](https://loj.ac/problem/10134)
-   [LOJ 2491. Sum](https://loj.ac/problem/2491)

Difference arrays:

-   [Fenwick Tree 3: Range Update, Range Query](https://loj.ac/problem/132)
-   [Poetize6 IncDec Sequence](https://www.luogu.com.cn/problem/P4552)
-   [Luogu P4231 Three-Step Kill](https://www.luogu.com.cn/problem/P4231)

Two-dimensional/multidimensional difference arrays:

-   [Luogu P3397 Carpets](https://www.luogu.com.cn/problem/P3397)
-   [Luogu P8228 Wdoi-5 Modular Nuclear Reactor](https://www.luogu.com.cn/problem/P8228)

Difference arrays on trees:

-   [USACO15DEC Max Flow](https://usaco.org/index.php?page=viewproblem2&cpid=576)
-   [JLOI2014 Squirrel's New Home](https://loj.ac/problem/2236)
-   [NOIP2015 Transportation Plan](http://uoj.ac/problem/150)
-   [NOIP2016 Running Every Day](http://uoj.ac/problem/261)
