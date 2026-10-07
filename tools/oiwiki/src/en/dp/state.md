---
title: Bitmask DP
---

## Introduction

Bitmask DP (state compression DP) is a kind of dynamic programming in which a set of states is encoded as an integer stored in the DP state, which makes the state transitions possible.

To achieve a lower time complexity, one usually looks for states with fewer possible values. Most problems use binary states: an $n$-bit binary number represents $n$ independent binary states.

State compression usually involves bit operations; see the [Bit operations](../math/bit.md) page for the basics.

## Example 1

???+ note "[\"SCOI2005\" Non-attacking Kings](https://loj.ac/problem/2153)"
    Place $K$ kings on an $N\times N$ board ($1 \leq N \leq 9, 1 \leq K \leq N \times N$) so that no two attack each other. How many placements are there?
    
    A king attacks one neighboring cell in each of the eight directions: up, down, left, right, upper left, lower left, upper right and lower right, $8$ cells in total.

### Explanation

Let $f(i,j,l)$ denote the number of valid placements in the first $i$ rows where the state of row $i$ is $j$ and $l$ kings have already been placed on the board.

For the state numbered $j$ we represent the placement of kings by the binary integer $sit(j)$: a bit of $sit(j)$ equal to $0$ means no king at the corresponding position, and $1$ means a king is placed there; $sta(j)$ denotes the number of kings in that state, i.e. the number of $1$s in the binary number $sit(j)$. For example, the state shown in the figure below is represented by the binary number $100101$ (the left side of the board corresponds to the low bits), so $sit(j)=100101_{(2)}=37, sta(j)=3$.

![](./images/SCOI2005-互不侵犯.png)

Let the state of the current row be $j$ and the state of the previous row be $x$; we get the following state transition equation: $f(i,j,l) = \sum f(i-1,x,l-sta(j))$.

Let the state number of the previous row be $x$. Under the condition that the current row and the previous row do not conflict, enumerate all possible $x$ and perform the transition; the transition equation is:

$$
f(i,j,l) = \sum f(i-1,x,l-sta(j))
$$

### Implementation

??? note "Sample code"
    ```cpp
    --8<-- "docs/dp/code/state/state_1.cpp"
    ```

## Example 2

???+ note "[\[POI2004\] PRZ](https://www.luogu.com.cn/problem/P5911)"
    $n$ people need to cross a bridge; person $i$ has weight $w_i$ and takes time $t_i$ to cross. The people cross in several groups; only after everyone in one group has crossed can the other groups cross. The maximum load of the bridge is $W$. What is the minimum time for everyone to cross?
    
    $100\le W \le 400$, $1\le n\le 16$, $1\le t_i\le 50$, $10\le w_i\le 100$.

### Explanation

Let $S$ denote a subset of the set of all people, $t(S)$ the longest crossing time among the people in $S$, $w(S)$ the total weight of the people in $S$, and $f(S)$ the minimum time for all people in $S$ to cross. Then:

$$
\begin{cases}
    f(\varnothing)=0,\\
    f(S)=\min\limits_{T\subseteq S;~w(T)\leq W}\left\{t(T)+f(S\setminus T)\right\}.
\end{cases}
$$

Note that here we cannot simply enumerate all sets and then check whether they are subsets; instead we must use [subset enumeration](../math/binary-set.md#遍历所有掩码的子掩码), which gives a time complexity of $O(3^n)$.

### Implementation

??? note "Sample code"
    ```cpp
    --8<-- "docs/dp/code/state/state_2.cpp"
    ```

## Exercises

-   [\"NOI2001\" Artillery Positions](https://loj.ac/problem/10173)
-   [\"USACO06NOV\" Corn Fields](https://www.luogu.com.cn/problem/P1879)
-   [\"Nine Provinces Joint Exam 2018\" A Pair of Wooden Chess Pieces](https://loj.ac/problem/2471)
