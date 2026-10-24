---
title: Introduction to space optimization
---

Space optimization techniques are not very common in algorithm competitions, but they are still worth discussing.

## Information entropy

Information entropy describes the lower bound on the space occupied by stored data; if the actually available space is below this bound, information is necessarily lost.

???+ note "Definition"
    For a random variable $X$, the information entropy is defined as
    
    $$
    H(X)=-\sum_{x}P(X=x)\log_2 P(X=x).
    $$

The base of the logarithm in the definition is $2$ because each bit of information stored in a computer has only $2$ possible values: $0$ and $1$.

For example, let $X$ be uniformly distributed on $\{1,2,\dots,n\}$; then its information entropy is

$$
H(X)=-\sum_{i=1}^n\frac{1}{n}\log_2\frac{1}{n}=\log_2 n,
$$

so we need at least $\log_2 n$ bits to store an integer from $1$ to $n$.

### Example problem

???+ note "[\[WC2022\] 猜词 (Guess the Word)](https://www.luogu.com.cn/problem/P8079)"
    An interactive problem: you need to guess a 5-letter word within a limited number of attempts. Each guess must be a word that exists in the given dictionary. If you guess correctly, the game ends; after each wrong guess, the interactor returns which letters are in the correct position, and which letters appear in the target word but in the wrong position.
    
    ??? note "Solution"
        See [Solving Wordle using information theory - 3Blue1Brown](https://www.bilibili.com/video/BV1zZ4y1k7Jw).
        
        Consider computing the information entropy: obviously, choosing a word with high information entropy at each guess makes the expected number of guesses as small as possible.
        
        Since in this problem the first letter of the answer is given before guessing, we can precompute the optimal guess for each first letter.
        
        In addition, if few words remain, we can prefer to output words that may be the answer, thereby reducing the number of guesses.

## Common techniques

### Avoid storing unnecessary data

For example:

-   In a [persistent segment tree](../ds/persistent-seg.md), a single modification creates only $O(\log n)$ new nodes, so we do not need to store the complete segment tree of every version; it suffices to record the new nodes.
-   Consider [graph storage](../graph/save.md): for sparse graphs, an adjacency matrix stores a large number of useless $0$ values, so sparse graphs are usually stored with adjacency lists.
-   Each element of a `bool` array occupies one byte; when necessary, it can be replaced by `std::vector<bool>` or a [bitset](../lang/csl/bitset.md), where each element occupies only one bit.
-   In [knapsack DP](../dp/knapsack/basic.md), for the 0-1 knapsack, each computation of DP values uses only the data from the previous computation, so we can optimize space with a rolling array and only record the current DP values.

### Exploit properties of the data

Consider a [disjoint set union (DSU)](../ds/dsu.md) with path compression and union by size; the traditional approach needs two arrays, recording the parent index and the subtree size respectively.

Note that:

1.  After applying path compression, for a tree in the DSU we only need to record the subtree size of the root.
2.  The parent of a root is always itself.

We can use the properties of signed integers, representing roots by negative numbers and non-root nodes by positive numbers, so a single array suffices to implement a DSU with path compression and union by size.

???+ note "Implementation"
    ```cpp
    --8<-- "docs/misc/code/space-optimization/space-optimization_1.cpp"
    ```

## Exercises

-   [QOJ 6669 Mapa](https://qoj.ac/problem/6669)
-   [\[SDOI/SXOI2022\] 无处存储 (Nowhere to Store)](https://www.luogu.com.cn/problem/P8353)

## References and further reading

1.  Chen Zhixuan (陈知轩). 《浅谈信息学竞赛中的空间优化问题》 (On Space Optimization Problems in Informatics Competitions). Chinese National Training Team (国家集训队) paper, 2022.
2.  [Information theory - Wikipedia](https://en.wikipedia.org/wiki/Information_theory)
3.  [浅谈信息论 (A Brief Discussion of Information Theory) - Luogu column](https://www.luogu.com.cn/article/i65ca8i5)
