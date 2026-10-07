---
title: IDA*
---

Prerequisites: [A\* algorithm](./astar.md), [iterative deepening search](./iterative.md)

This page briefly introduces the IDA\* algorithm. IDA\* is the A\* algorithm combined with iterative deepening.

## Procedure

The IDA\* algorithm is a variant of iterative deepening search. Iterative deepening limits the search depth in each DFS, while IDA\* limits the path cost of a single DFS.

In one iteration, the algorithm runs a DFS from the start node $s$, records the actual cost $g(x)$ of reaching the current node $x$, and uses the estimated minimum cost $h(x)$ from $x$ to the target for pruning. If the estimated total cost of reaching the target along the current path

$$
f(x) = g(x) + h(x)
$$

exceeds the threshold $C$, the search of that branch is stopped.

The threshold $C$ is updated dynamically between iterations. The initial threshold is the estimated total cost of the start node, $h(s)$. Within one iteration, whenever the search stops because the threshold is exceeded, the minimum estimated total cost among all not-yet-visited successors is recorded. After the iteration ends, the threshold is set to this minimum and the next round of search begins.

## Properties

Since it uses the same pruning strategy as the A\* algorithm, the discussion of the properties of A\* also applies to IDA\*.

Compared with the A\* algorithm, IDA\* has the following advantages:

-   No duplicate checking and no sorting are needed, which favors deep pruning.
-   Lower memory requirements. Each iteration is a depth-first search, but with a limit on the path cost; using DFS reduces memory consumption.

It also has a disadvantage:

-   Repeated search. Even if two consecutive iterations differ only slightly, every relaxation of the limit restarts the search from scratch.

## Implementation

Let $h$ be a suitable estimate (heuristic) function and $s$ the start node of the search. The complete algorithm looks roughly as follows:

$$
\begin{array}{l}
\textbf{Algorithm. }\textrm{IdaStar}():\\
\textbf{Output. }\text{The shortest path, }\textit{path}\text{, and its cost, }C\text{, if a path exists,}\\
\quad \text{and }\textrm{NOT}\_\textrm{FOUND}\text{, otherwise.}\\
\textbf{Method.}\\
\begin{array}{ll}
1  & C \gets h(s) \\
2  & path \gets [s] \\
3  & \textbf{while }\text{true}\\
4  & \quad t \gets \textrm{Search}(\textit{path},0,C)\\
5  & \quad \textbf{if } t=\text{FOUND}\textbf{ then return }(\textit{path},C) \\
6  & \quad \textbf{if } t=\infty\textbf{ then return }\textrm{NOT}\_\textrm{FOUND} \\
7  & \quad C \gets t
\end{array}\\
\\
\textbf{Sub-Algorithm. }\textrm{Search}(\textit{path},g,C):\\
\textbf{Input. }\text{The current path, }\textit{path}\text{, its cost, }g\text{, and search limit }C.\\
\textbf{Output. }\text{FOUND, if the target node has been reached; }\infty\text{, if all}\\
\quad \text{reachable nodes have been explored; otherwise, the minimum}\\
\quad \text{total cost, }t\text{, among nodes not yet explored.}\\
\textbf{Method.}\\
\begin{array}{ll}
1  & \textit{node} \gets \text{the last element in }\textit{path}\\
2  & f \gets g + h(\textit{node}) \\
3  & \textbf{if } f > C \textbf{ then return } f \\
4  & \textbf{if }\textit{node}\text{ is the target }\textbf{then return }\text{FOUND}\\
5  & \textit{min} \gets \infty \\
6  & \textbf{for }\text{each }\textit{child}\text{ of }\textit{node }\textbf{do}\\
7  & \quad \textbf{if }\textit{child}\text{ not in }\textit{path}\textbf{ then}\\
8  & \quad \quad \text{append }\textit{child}\text{ to }\textit{path}\\
9  & \quad \quad t \gets \text{Search}(\textit{path}, g + \text{Cost}(\textit{node},\textit{child}), C)\\
10 & \quad \quad \textbf{if }t = \text{FOUND}\textbf{ then return }\text{FOUND}\\
11 & \quad \quad \textbf{if }t < \textit{min}\textbf{ then }\textit{min}\gets t\\
12 & \quad \quad \text{remove the last element of }\textit{path}\\
13 & \textbf{return }\textit{min}
\end{array}
\end{array}
$$

## Example

???+ example "[Egyptian Fractions](https://www.luogu.com.cn/problem/P1763)"
    In ancient Egypt, every rational number was written as a sum of pairwise distinct unit fractions (that is, fractions $1/a$, $a\in\mathbf{N}_+$). For example, $\dfrac{2}{3}=\dfrac{1}{2}+\dfrac{1}{6}$, but $\dfrac{2}{3}=\dfrac{1}{3}+\dfrac{1}{3}$ is not allowed, because equal unit fractions may not appear among the summands.
    
    A fraction $\dfrac{a}{b}$ has many representations. We agree that among different representations of the same fraction, one with fewer summands is better than one with more; if the number of summands is the same, the one whose smallest fraction is larger is better. For example, $\dfrac{19}{45}=\dfrac{1}{5}+\dfrac{1}{6}+\dfrac{1}{18}$ is the best representation.
    
    Given integers $a,b$ ($0<a<b<1000$), write a program that computes the best representation.

??? note "Solution idea"
    In theory this problem can be solved by backtracking, but the solution tree would be truly "horrifying": not only does its depth have no obvious upper bound, but the choice of summands is in theory infinite as well. In other words, with breadth-first traversal we could not even finish expanding a single level, because every level is infinite.

    The remedy is iterative deepening search: enumerate the depth limit $C$ from small to large, and in each search consider only nodes of depth at most $C$. This way, as long as the depth of the solution is finite, it will be found in finite time.

    The depth limit $C$ can also be used for pruning. Expand in order of increasing denominators; if at level $i$ the sum of the first $i$ fractions is $\dfrac{c}{d}$ and the $i$-th fraction is $\dfrac{1}{e}$, then at least

    $$
    h = \left(\dfrac{a}{b}-\dfrac{c}{d}\right)/\left(\dfrac{1}{e+1}\right)
    $$

    more fractions are needed for the sum to reach $\dfrac{a}{b}$. For example, if the search has currently reached $\dfrac{19}{45}=\dfrac{1}{5}+\dfrac{1}{100}+\cdots$, every following fraction is at most $\dfrac{1}{101}$, so at least $\left({\dfrac{19}{45}-\dfrac{1}{5}}\right)/\left({\dfrac{1}{101}}\right)=23$ more terms are needed for the sum to reach $\dfrac{19}{45}$; therefore the first $22$ iterations will not consider this subtree at all. The key point is this: we can estimate how many more steps are needed at least before a solution appears.

    Note that the word "at least" means the estimate is "optimistic". As in the A\* algorithm, a good estimate function must be "optimistic", that is, it must not overestimate the actual cost. Replacing the depth limit $g\le C$ of iterative deepening with the stricter limit $g + h \le C$ gives the IDA\* algorithm discussed on this page. Since the path cost in this article is simply its length, IDA\* also limits the path length, only adding an estimate of how many more steps are needed. In more general problems, depending on the cost to be minimized, other estimate functions can be designed.

    In the implementation, IDA\* is further optimized with pruning:

    1.  When expanding a node, the next denominator to consider is at least $\left(\dfrac{a}{b}-\dfrac{c}{d}\right)^{-1}$, which improves the starting point of the enumeration of $e$.
    2.  The path cost limit of IDA\* can be rewritten as

        $$
        e \le \left(\dfrac{a}{b}-\dfrac{c}{d}\right)^{-1}(C-g) - 1.
        $$

        So there is no need to enumerate all following denominators and check them one by one; it suffices to enumerate up to this upper bound.
    3.  When the search reaches the last two fractions, feasibility is checked directly with a quadratic equation instead of continuing the search. Specifically, to find $e<x<y\le E_\text{max}$ such that

        $$
        \dfrac{1}{x} + \dfrac{1}{y} = \dfrac{p}{q} := \dfrac{a}{b}-\dfrac{c}{d},
        $$

        it suffices to solve the system of quadratic equations in two unknowns

        $$
        \begin{cases}
        x + y = kp,\\
        xy = kq
        \end{cases}
        $$

        where $k\in\mathbf N_+$. From the theory of quadratic equations, the system has two distinct real roots only when

        $$
        \Delta = k^2p^2-4kq > 0 \iff k > \dfrac{4q}{p^2}
        $$

        holds, and the roots are

        $$
        x = \dfrac{kp - \sqrt{\Delta}}{2},~ y = \dfrac{kp + \sqrt{\Delta}}{2}.
        $$

        Therefore we can directly enumerate all feasible $k$ and check whether such a pair of integer solutions exists. When enumerating $k$, the upper bound is determined by $y < E_\text{max}$.
    4.  Every time a solution is found, the upper bound of the denominators $M_e$ is set to the largest denominator in the current solution minus one.

    In addition, the implementation directly stores the values $\dfrac{a}{b}-\dfrac{c}{d}$ and $C-g$: the numerator and denominator of the former are kept in the variables `a` and `b`, and the latter is stored in the variable `d`.

??? note "Sample code"
    ```cpp
    --8<-- "docs/search/code/idastar/idastar_1.cpp"
    ```

## Exercises

-   [UVa 1343 The Rotation Game](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=4089)
