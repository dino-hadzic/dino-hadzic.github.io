---
title: State design optimization
---

## Overview

When optimizing a DP, speeding up the transitions is not the only option. Sometimes one can start from the definition of the states and achieve a better complexity by changing the way the states are designed.

The annoying part is that most of these optimizations are not general, i.e. they cannot be applied to many problems in a routine way. Therefore, the text below starts from concrete example problems and tries to provide some inspiration, hoping it will be of some help to the reader.

## Example 1

???+ note "Problem"
    Given two strings $A,B$ of lengths $n,m$ consisting only of lowercase letters, find the longest common subsequence of $A,B$. $(n\le 10^6,m\le 10^3)$

### Naive solution

You see it at a glance – isn't this a template problem?

Define the state $f_{i,j}$ as the longest common subsequence of the first $i$ characters of $A$ and the first $j$ characters of $B$; then

$$
f_{i,j}=
\begin{cases}
\max(f_{i-1,j},f_{i,j-1}) & ,A_i \neq B_j \\
f_{i-1,j-1}+1 & ,A_i = B_j 
\end{cases}
$$

The time complexity of this approach is $O(nm)$, which does not pass this problem.

### Better solution

Thinking more carefully, we notice a property: the final answer does not exceed $m$.

Thinking a bit more, we notice that the LCS has a greedy property.

Change the state definition: let $f_{i,j}$ be the length of the shortest prefix of $A$ whose longest common subsequence with the first $i$ characters of $B$ has length $j$ (i.e. swap the answer of the naive solution with the first dimension of the state).

By precomputing, for every position of $A$, the next occurrence of each of $a,b,\cdots,z$, the forward transition can be done in $O(1)$.

The complexity is $O(m^2+26n)$, which passes this problem.

## Example 2

???+ note "Problem"
    Given an unweighted directed graph with $n$ vertices, determine whether it has a Hamiltonian cycle. $(2\le n\le 20)$

### Naive solution

Seeing the constraints, we think of bitmask DP.

Let $f_{s,i}$ denote whether, starting from vertex $1$ and passing only through vertices in the set $s$, vertex $i$ can be reached. Let $g$ be the adjacency matrix of the graph. Then

$$
f_{s, i} = \bigvee_{j\in s, j\neq i}f_{s \setminus \{i\}, j}\wedge g_{j, i} \left(i\in s\right)
$$

The time complexity is $O(n^2 \times 2^n)$; with a tidy implementation it might pass, but it is not elegant.

### Better solution

In the state design above, each $dp$ value represents only a single `bool`, which feels wasteful.

For each state $s$ we can pack $f_{s,1},f_{s,2},\dots,f_{s,n}$ into one `int`; we notice that, after packing the adjacency matrix in the same way, the transition can be done in $O(1)$.

The time complexity is $O(n^2/w\times 2^n)$, which passes this problem, where $w$ is the number of bits of an `int`.

## Example 3

???+ note "Problem"
    An ordinary knapsack problem. $n$ is the number of items, $m$ is the knapsack capacity, and $v_i, w_i$ are the volume and value of the $i$-th item; $1 \le n \le 10^3$, $1 \le m, v_i \le \color{red}{10^{18}}$, $1 \le \sum w_i \le 10^3$.

### Naive solution

This is a template knapsack problem.

Define the state $f_{i, j}$ as the maximum total value when choosing among the first $i$ items with $j$ units of capacity currently used in the knapsack.

It is easy to get $f_{i, j} = \max(f_{i - 1, j}, f_{i - 1, j - v_i} + w_i)$.

Since $v_i \le 10^{18}$, this does not pass.

### Better solution

Swap the answer with the second dimension of the state: let $f_{i, j}$ be the minimum total volume when choosing among the first $i$ items such that the items in the knapsack **have total value $j$**.

Again, it is easy to get $f_{i, j} = \min(f_{i - 1, j}, f_{i - 1, j - w_i} + v_i)$.

Note that after changing the second dimension of the state, the transition has to change accordingly.

The time complexity is $O(n \sum w_i)$, which passes this problem.
