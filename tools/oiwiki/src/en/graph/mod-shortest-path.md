---
title: Modular shortest path
---

When a problem looks like "given $n$ integers, how many other integers can be formed from these $n$ integers (each of the $n$ integers may be used repeatedly)", or "given $n$ integers, find the smallest (largest) integer that cannot be formed from them", or "how many additions are needed at least to form a number congruent to $p$ modulo $K$", the modular shortest path technique can be used.

The modular shortest path uses congruences to construct states, which reduces the space complexity.

By analogy with [difference constraints](./diff-constraints.md), the states constructed from congruences can be viewed as vertices in a single-source shortest path problem. A state transition in the modular shortest path usually looks like $f(i+y) = f(i) + y$, similar to $f(v) = f(u) +edge(u,v)$ in the single-source shortest path.

## Examples

### Example 1

???+ note "[P3403 Elevator](https://www.luogu.com.cn/problem/P3403)"
    Problem summary: given $x，y，z，h$, for how many $k \in [1,h]$ do there exist $a, b, c$ with $ax+by+cz=k$? ($0\leq a,b,c$, $1\le x,y,z\le 10^5$, $h\le 2^{63}-1$)

Without loss of generality assume $x < y < z$.

Let $d_i$ be the lowest floor $p$ reachable using only **operation 2** and **operation 3** such that $p\bmod x = i$, i.e. the smallest number congruent to $i$ modulo $x$ obtainable with **operations 2** and **3**; it is used to count how many numbers in that residue class satisfy the condition.

We get two transitions:

-   $i \xrightarrow{y} (i+y) \bmod x$

-   $i \xrightarrow{z} (i+z) \bmod x$

Note that we usually take the modulus to be the smallest of the numbers $a_i$, here $x$, to keep the space complexity as small as possible (smallest residue system).

This is in fact equivalent to adding edges in a shortest path graph:

`add(i, (i+y) % x, y)`

`add(i, (i+z) % x, z)`

Next we only need to compute $d_0, d_1, d_2, \dots, d_{x-1}$, which takes a single run of a shortest path algorithm.

??? example "Implementation based on shortest paths"
    ```cpp
    --8<-- "docs/graph/code/mod-shortest-path/mod-shortest-path_1.cpp"
    ```

In fact, however, a regular shortest path computation is not even needed; notice two special properties:

First, there are only two edge weights, and for every path, by commutativity of addition, the order in which edges of the two weights are traversed does not matter. So we can run the shortest path twice, each time building only the edges of one weight.

Second, in a graph with a single edge weight every vertex $u$ has exactly one incoming edge (from $(u-y) \bmod x$) and one outgoing edge (to $(u+y) \bmod x$), so the whole graph necessarily consists of several cycles. Moreover, one can prove that there are exactly $\gcd(x,y)$ cycles of equal length.

???+ note "Proof"
    Let $d=\gcd(x,y)$ and $x=da,y=db$, so $\gcd(a,b)=1$.
    
    Starting from $u$ and taking $k$ steps we reach $(u+ky) \bmod x$. If this closes a cycle, then $ky \equiv 0 \pmod x$, i.e. $kb \equiv 0 \pmod a$.
    
    Since $\gcd(a,b)=1$, the smallest such $k$ is $k=a$, so the cycle length is $a = \dfrac{x}{d}$. Because we started from an arbitrary vertex, all cycles have the same length, and there are $d$ of them.

Furthermore, the edge weights are positive, so after going around a cycle twice no further relaxation is possible. It suffices to simply loop around the cycle and update. This way we are not limited by the complexity of the shortest path algorithm and achieve $O(x)$.

As with difference constraints, if $\{a_1,a_2,\cdots,a_n\}$ is a solution then $\{a_1+d,a_2+d,\cdots,a_n+d\}$ is also a solution; therefore in this problem we take $i=1$ as the source, since then $dis_{1}=1$ at the source is the smallest value in the known range, so the solution obtained is also a smallest one.

The answer is:

$$
\sum_{i=0}^{x-1}\left(\frac{h-d_i}{x} + 1\right)
$$

We add 1 because the floor $d_i$ itself also counts.

In the implementation note that the range is $h \leq 2^{63}-1$, so before computing the shortest paths the initial value of $d_i$ must be at least $2^{63}$, which exceeds the maximum of `long long` in C++. One can therefore use `unsigned long long`, or first set $h \gets h - 1$ and call the lowest floor floor $0$; the rest of the code stays the same.

??? example "Implementation based on the cycle optimization"
    ```cpp
    --8<-- "docs/graph/code/mod-shortest-path/mod-shortest-path_2.cpp"
    ```

### Example 2

???+ note "[ARC084B Small Multiple](https://atcoder.jp/contests/arc084/tasks/arc084_b)"
    Problem summary: given $n$, find the smallest digit sum among the multiples of $n$. ($1\le n\le 10^5$)

This problem can be solved with an unbounded knapsack optimized by cyclic convolution in $O(n\log^2 n)$ time, but we want a linear algorithm.

Observe that any positive integer can be obtained by starting from $1$ and performing, in some order, the operations "multiply by $10$" and "add $1$", where the number of "add $1$" operations is exactly the digit sum of the number. This suggests a shortest path.

For all $0\le k\le n-1$, add an edge of weight $0$ from $k$ to $10k$, and an edge of weight $1$ from $k$ to $k+1$ (vertex labels are taken modulo $n$).

Every multiple of $n$ corresponds to a path from vertex $1$ to vertex $0$ in this graph, so it suffices to find the shortest path from $1$ to $0$. Some paths are invalid (e.g. taking $10$ consecutive edges of weight $1$), but the answers produced by these paths are never better, so they do not affect the result.

The time complexity is $O(n)$.

## Exercises

[Luogu P3403 Elevator](https://www.luogu.com.cn/problem/P3403)

[Luogu P2662 Cattle Fence](https://www.luogu.com.cn/problem/P2662)

[\[National Training Team\] Momo's Equation](https://www.luogu.com.cn/problem/P2371)

[「NOIP2018」Currency System](https://loj.ac/problem/2951)

[AGC057D - Sum Avoidance](https://atcoder.jp/contests/agc057/tasks/agc057_d)

[「THUPC 2023 Preliminary」Knapsack](https://loj.ac/p/6872)
