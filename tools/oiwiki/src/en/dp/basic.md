---
title: Dynamic programming basics
---

This page mainly introduces the basic idea of dynamic programming and the way states and state transition equations are designed in dynamic programming, to give beginners a first understanding of dynamic programming.

The other pages of this chapter introduce how to build dynamic programming models for various kinds of problems, as well as some optimization techniques for dynamic programming.

## Introduction

???+ note "[\[IOI1994\] Number Triangle](https://www.luogu.com.cn/problem/P1216)"
    Given a number triangle with $r$ rows ($r \leq 1000$), find a path from the top to any position in the bottom row such that the sum of the numbers along the path is maximized. Each step may move to the number below-left or below-right of the current one.
    
    ```plain
            7 
          3   8 
        8   1   0 
      2   7   4   4 
    4   5   2   6   5 
    ```
    
    In the example above, the optimal path is $7 \to 3 \to 8 \to 7 \to 5$.

The simplest brute-force idea is to try all paths. Since the number of paths is on the order of $O(2^r)$, this approach is unacceptable.

Note the following fact: every decision along an optimal path is itself optimal.

Take the optimal path mentioned in the problem as an example and consider only the first four steps $7 \to 3 \to 8 \to 7$: there is no path from the top to the $2$nd number in row $4$ with a larger sum.

And for each point, the next decision has only two options: below-left or below-right (if it exists). Therefore we only need to record the maximum sum at the current point and use this maximum to make the next decision, updating the maximum sums of the subsequent points.

This approach has another advantage: we have successfully reduced the size of the problem, splitting one problem into several smaller problems. To get the optimal solution from the top to row $r$, we only need the information about the optimal solution from the top to row $r-1$.

There is still one problem: the subproblems overlap heavily, so the same subproblem may be visited many times, and the efficiency is still low. The solution is to store the solution of each subproblem and restrict the order of visits through memoization, ensuring that each subproblem is visited only once.

These are some of the basic ideas of dynamic programming. Below we introduce the idea of dynamic programming more systematically.

## Principles of dynamic programming

A problem that can be solved by dynamic programming must satisfy three conditions: optimal substructure, no aftereffect, and overlapping subproblems.

### Optimal substructure

A problem with optimal substructure may also be suitable for a greedy approach.

Make sure that we examine all subproblems used in the optimal solution.

1.  Prove that the first component of an optimal solution to the problem is making a choice;
2.  for a given problem, among its possible first choices, assume that you already know which choice leads to an optimal solution. You do not care how this choice is obtained; just assume it is known;
3.  given the choice that leads to an optimal solution, determine which subproblems this choice produces and how best to characterize the subproblem space;
4.  prove that, as a component of an optimal solution to the original problem, the solution of each subproblem is itself an optimal solution of that subproblem. The method is proof by contradiction: suppose the solution of some subproblem is not its own optimal solution; then we could replace the current non-optimal solution in the solution of the original problem with the optimal solution of that subproblem, obtaining a better solution of the original problem, which contradicts the assumption that the solution of the original problem is optimal.

Keep the subproblem space as simple as possible and expand it only when necessary.

Differences in optimal substructure show up in two aspects:

1.  how many subproblems are involved in an optimal solution of the original problem;
2.  how many choices must be examined when determining which subproblems the optimal solution uses.

In the subproblem graph, every vertex corresponds to a subproblem, and the choices to be examined correspond to the edges leading to subproblem vertices.

### No aftereffect

Subproblems that have already been solved are not affected by later decisions.

### Overlapping subproblems

If there are many overlapping subproblems, we can use space to store the solutions of these subproblems and avoid solving the same subproblem repeatedly, thereby improving efficiency.

### Basic approach

For a problem that can be solved by dynamic programming, the following approach is generally used:

1.  Divide the original problem into several **stages**; each stage corresponds to several subproblems, whose features we extract (called **states**);
2.  find the possible **decisions** for each state, that is, the ways of transitioning between states (in mathematical language, the **state transition equation**);
3.  solve the problems of each stage in order.

Understood in terms of graph theory, we build a [directed acyclic graph](../graph/dag.md) in which every state corresponds to a node of the graph and decisions correspond to edges between nodes. The problem thus becomes finding the longest (shortest) path in a DAG (see [DP on DAGs](./dag.md)).

## Longest common subsequence

???+ note "Longest common subsequence problem"
    Given a sequence $A$ of length $n$ and a sequence $B$ of length $m$ ($n,m \leq 5000$), find a longest sequence that is a subsequence of both $A$ and $B$.

For the definition of a subsequence, see [subsequence](../string/basic.md). A brief example: the common subsequences of the strings `abcde` and `acde` are `a`, `c`, `d`, `e`, `ac`, `ad`, `ae`, `cd`, `ce`, `de`, `acd`, `ade`, `ace`, `cde`, `acde`, and the length of the longest common subsequence is 4.

Let $f(i,j)$ denote the length of the longest common subsequence when considering only the first $i$ elements of $A$ and the first $j$ elements of $B$; finding this length is a **subproblem**. $f(i,j)$ is what we call a **state**, and $f(n,m)$ is the final state to be reached, i.e., the desired result.

For each $f(i,j)$ there are three decisions: if $A_i=B_j$, it can be appended to the end of the common subsequence; the other two decisions are to skip $A_i$ or $B_j$. The state transition equation is as follows:

$$
f(i,j)=\begin{cases}f(i-1,j-1)+1&A_i=B_j\\\max(f(i-1,j),f(i,j-1))&A_i\ne B_j\end{cases}
$$

You can refer to the [interactive LCS page on SourceForge](http://lcs-demo.sourceforge.net/) to better understand the LCS procedure.

???+ example "Sample implementation"
    === "C++"
        ```cpp
        --8<-- "docs/dp/code/basic/lcs.cpp:core"
        ```
    
    === "Python"
        ```cpp
        --8<-- "docs/dp/code/basic/lcs.py:core"
        ```

The time complexity of this approach is $O(nm)$.

In addition, there is an $O\left(\dfrac{nm}{w}\right)$ algorithm for this problem[^ref1]. Interested readers can explore it on their own.

## Longest non-decreasing subsequence

???+ note "Longest non-decreasing subsequence problem"
    Given a sequence $a$ of length $n$ ($n \leq 5000$), find a longest subsequence of $a$ such that each element of the subsequence is not smaller than the previous one.

### Algorithm 1

Let $f(i)$ denote the length of the longest non-decreasing subsequence ending with $a_i$; the answer is $\max_{1 \leq i \leq n} f(i)$.

When computing $f(i)$, we try to append $a_i$ to other longest non-decreasing subsequences to update the answer. This gives the state transition equation $f(i)=\max_{1 \leq j < i,~a_j \leq a_i} (f(j)+1)$.

???+ example "Sample implementation"
    === "C++"
        ```cpp
        --8<-- "docs/dp/code/basic/lis-1.cpp:core"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/dp/code/basic/lis-1.py:core"
        ```

It is easy to see that the time complexity of this algorithm is $O(n^2)$.

### Algorithm 2

When the range of $n$ grows to $n \leq 10^5$, the first approach is no longer fast enough; below we give an $O(n \log n)$ approach.

Consider the previously defined state $(i, l)$, meaning that the longest non-decreasing subsequence ending with the $i$-th element has length $l$. Unlike the previous method of processing states for a fixed $i$, here we directly determine whether $(i, l)$ is valid:

-   The initial state $(1,1)$ is certainly valid.
-   For any $(i, l)$, if there exists $j < i$ such that $(j, l-1)$ is valid and $a_j \le a_i$, then $(i, l)$ is valid.

In the end, we only need to find the valid state $(i,l)$ with the largest $l$ to obtain the length of the longest non-decreasing subsequence.

Let the original sequence be $a_1, \cdots, a_n$. Define an array $d$ whose $x$-th element denotes the minimum value of the last element of a non-decreasing subsequence of length $x$. Initially the array is empty. Let $i$ run from $1$ to $n$, computing in turn the length of the longest non-decreasing subsequence of the first $i$ elements. For the current element $a_i$:

-   If $a_i$ is greater than or equal to the last element of $d$, append $a_i$ directly to the end of $d$.
    -   Explanation: if $a_i$ is greater than or equal to the last element of the current longest subsequence, there is a non-decreasing subsequence to which $a_i$ can be appended. Not inserting it would break optimality.
-   If $a_i$ is strictly smaller than the last element of $d$, find the **first** element greater than it and replace that element with $a_i$.
    -   Explanation: inserting it directly at the end would break the monotonicity of $d$; the replacement ensures that the last element for each length is as small as possible, leaving more possibilities for later elements.
    -   Optimization: since $d$ is monotonically non-decreasing, binary search can directly find the insertion position, reducing the overall complexity to $O(n\log n)$ instead of the $O(n^2)$ of brute-force search.

If the actual longest non-decreasing subsequence must also be output, we can additionally maintain an array $d'_x$ denoting the position of the minimum last element among non-decreasing subsequences of length $x$ (if there are several, any one will do). Specifically, when inserting element $a_i$ into $d_x$, we also update $d'_x$ to $i$. At the same time, we record the optimal predecessor $p_i$ of $i$ as $d'_{x-1}$. Finally, starting from any state of maximum length and following the predecessors $p_i$ backward, we obtain the complete subsequence.

???+ example "Sample implementation"
    === "C++"
        ```cpp
        --8<-- "docs/dp/code/basic/lis-2.cpp:core"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/dp/code/basic/lis-2.py:core"
        ```

The time complexity of this algorithm is $O(n\log n)$. The time complexity of outputting the answer is $O(\textit{ans})$.

???+ tip "Note"
    For the longest **increasing** subsequence problem, similarly, let $d_i$ denote the minimum value of the last element among all longest increasing subsequences of length $i$.
    
    Note that in step 2, if $a_i \leq d_{len}$, since adjacent elements of a longest increasing subsequence may not be equal, we need to find the **first** element in $d$ that is **not less than** $a_i$ and replace it with $a_i$.
    
    In the implementation (taking C++ as an example), the `upper_bound` function must be changed to `lower_bound`.

## References and notes

-   [Detailed explanation of the nlogn algorithm for the longest non-decreasing subsequence – lvmememe – cnblogs (Chinese)](https://www.cnblogs.com/itlqs/p/5743114.html)

[^ref1]: [Longest common subsequence with bit operations – -Wallace- – cnblogs (Chinese)](https://www.cnblogs.com/-Wallace-/p/bit-lcs.html)
