---
title: LGV lemma
---

## Introduction

The Lindström–Gessel–Viennot lemma, or LGV lemma for short, can be used to handle problems such as counting non-intersecting paths in a directed acyclic graph.

Prerequisites: the basic part of [Graph theory concepts](./concept.md), [matrices](../math/linear-algebra/matrix.md), [Gaussian elimination for determinants](../math/numerical/gauss.md).

The LGV lemma applies only to **directed acyclic graphs**.

## Definitions

$\omega(P)$ denotes the product of the weights of all edges on the path $P$. (When counting paths, all edge weights can be set to $1$.) (In fact, edge weights can be generating functions.)

$e(u, v)$ denotes the sum of $\omega(P)$ over **every** path $P$ from $u$ to $v$, i.e. $e(u, v)=\sum\limits_{P:u\rightarrow v}\omega(P)$.

The set of starting points $A$ is a subset of the vertex set of the DAG of size $n$.

The set of endpoints $B$ is also a subset of the vertex set, also of size $n$.

A system of non-intersecting paths $S$ from $A$ to $B$: $S_i$ is a path from $A_i$ to $B_{\sigma(S)_i}$ ($\sigma(S)$ is a permutation), and for any $i\ne j$, $S_i$ and $S_j$ have no common vertex.

$t(\sigma)$ denotes the number of inversions of the permutation $\sigma$.

## The lemma

$$
M = \begin{bmatrix}e(A_1,B_1)&e(A_1,B_2)&\cdots&e(A_1,B_n)\\
e(A_2,B_1)&e(A_2,B_2)&\cdots&e(A_2,B_n)\\
\vdots&\vdots&\ddots&\vdots\\
e(A_n,B_1)&e(A_n,B_2)&\cdots&e(A_n,B_n)\end{bmatrix}
$$

$$
\det(M)=\sum\limits_{S:A\rightarrow B}(-1)^{t(\sigma(S))}\prod\limits_{i=1}^n \omega(S_i)
$$

where $\sum\limits_{S:A\rightarrow B}$ denotes the sum over every system of non-intersecting paths $S$ from $A$ to $B$ satisfying the requirements above.

### Proof

By the definition of the determinant,

$$
\begin{align}
\det(M)&=\sum_{\sigma}(-1)^{t(\sigma)}\prod_{i=1}^n e(a_i,b_{\sigma(i)})\\
&=\sum_{\sigma}(-1)^{t(\sigma)}\prod_{i=1}^n \sum_{P:a_i\to b_{\sigma(i)}} \omega(P)
\end{align}
$$

Observe that $\prod\limits_{i=1}^n \sum\limits_{P:a_i\to b_{\sigma(i)}} \omega(P)$ is in fact the sum of $\omega(P)$ over all path systems $P$ from $A$ to $B$ with permutation $\sigma$.

$$
\begin{align}
&\sum_{\sigma}(-1)^{t(\sigma)}\prod_{i=1}^n \sum_{P:a_i\to b_{\sigma(i)}} \omega(P)\\
=&\sum_{\sigma}(-1)^{t(\sigma)}\sum_{P=\sigma}\omega(P)\\
=&\sum_{P:A\to B}(-1)^{t(\sigma)}\prod_{i=1}^n \omega(P_i)
\end{align}
$$

Here $P$ is an arbitrary path system.

Let $U$ be a system of non-intersecting paths and $V$ a system of intersecting paths,

$$
\begin{align}
&\sum_{P:A\to B}(-1)^{t(\sigma)}\prod_{i=1}^n \omega(P_i)\\
=&\sum_{U:A\to B}(-1)^{t(U)}\prod_{i=1}^n \omega(U_i)+\sum_{V:A\to B}(-1)^{t(V)}\prod_{i=1}^n \omega(V_i)
\end{align}
$$

Suppose $P$ contains a pair of intersecting paths $P_i:a_1 \to u \to b_1,P_j:a_2 \to u \to b_2$. Then there necessarily exists a corresponding intersecting system $P_i'=a_1\to u\to b_2,P_j'=a_2\to u\to b_1$, with the other paths of $P'$ identical to those of $P$. We get $\omega(P)=\omega(P'),t(P)=t(P')\pm 1$.

Therefore $\sum\limits_{V:A\to B}(-1)^{t(\sigma)}\prod\limits_{i=1}^n \omega(V_i)=0$.

Hence $\det(M)=\sum\limits_{U:A\to B}(-1)^{t(U)}\prod\limits_{i=1}^n \omega(U_i)$.

This completes the proof[^1].

## Example problems

???+ note "Example 1 [CF348D Turtles](https://codeforces.com/contest/348/problem/D)"
    Problem: there is an $n\times m$ grid board in which some cells are passable and some are not. A turtle at $(x, y)$ can only move to $(x+1, y)$ or $(x, y+1)$. Find the number of pairs of non-intersecting turtle paths from $(1, 1)$ to $(n, m)$ modulo $10^9+7$. $2\le n,m\le3000$.

A fairly direct application of the LGV lemma. Considering all valid paths, we see that any path from $(1,1)$ must pass through $A=\{(1,2), (2,1)\}$, and to reach the target it must pass through $B=\{(n-1, m), (n, m-1)\}$, so $A, B$ can be fixed immediately. Applying the LGV lemma, the answer is:

$$
\begin{vmatrix}
f(a_1, b_1) & f(a_1, b_2) \\
f(a_2, b_1) & f(a_2, b_2)
\end{vmatrix} = f(a_1, b_1)\times f(a_2, b_2) - f(a_1, b_2)\times f(a_2, b_1)
$$

where $f(a, b)$ is the number of paths $a\rightarrow b$ on the board; counting paths on a grid with obstacles is a straightforward $O(nm)$ DP, so $f$ is easy to compute. The total complexity is $O(nm)$.

??? note "Reference code"
    ```cpp
    --8<-- "docs/graph/code/lgv/lgv_2.cpp"
    ```

???+ note "Example 2 [HDU 5852 Intersection is not allowed!](https://acm.hdu.edu.cn/showproblem.php?pid=5852)"
    Problem: there is an $n\times n$ board; a piece at $(x, y)$ can only move to $(x, y+1)$ or $(x + 1, y)$. There are $k$ pieces; initially the $i$-th piece is at $(1, a_i)$ and must end at $(n, b_i)$, and the paths must be pairwise non-intersecting. Find the number of ways modulo $10^9+7$. $1\le n\le 10^5$, $1\le k\le 100$, and it is guaranteed that $1\le a_1<a_2<\dots<a_n\le n$, $1\le b_1<b_2<\dots<b_n\le n$.

Observe that if the paths do not intersect, each path must go from $a_i$ to $b_i$, so in the LGV lemma we always have $\sigma(S)_i=i$ and there is no need to worry about signs. Set all edge weights to $1$ and apply the lemma directly.

The number of paths from $(1, a_i)$ to $(n, b_j)$ equals the number of ways to choose $n-1$ downward steps out of $n-1+b_j-a_i$ steps, so $e(A_i, B_j)=\binom{n-1+b_j-a_i}{n-1}$.

The determinant can be computed by Gaussian elimination.

The complexity is $O(n+k(k^2 + \log p))$, where $\log p$ is the cost of computing a modular inverse.

??? note "Reference code"
    ```cpp
    --8<-- "docs/graph/code/lgv/lgv_1.cpp"
    ```

## References

[^1]: The proof is taken from [Zhihu – Proof of the LGV lemma](https://zhuanlan.zhihu.com/p/517819133)
