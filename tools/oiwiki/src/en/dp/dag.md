---
title: DP on a DAG
---

## Definition

A DAG is a [directed acyclic graph](../graph/dag.md). Binary relations in many practical problems can be modeled with a DAG, which turns these problems into longest (shortest) path problems on a DAG.

## Explanation

Let us analyze the process of DAG modeling using the following problem as an example.

???+ note "Example [UVa 437 The Tower of Babylon](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=378)"
    There are $n (n\leqslant 30)$ types of blocks; the three edge lengths of each type are known and there are infinitely many blocks of each type. Choose some blocks and stack them into a tower that is as tall as possible (each block may choose any of its edges as its height), such that the length and width of the base of every block are strictly smaller than the length and width of the base of the block below it. Find the maximum height of the tower.

## Procedure

### Building the DAG

Since the length and width of the base of every block must be strictly smaller than those of the block below it, it is natural to use this relation as the basis for building the graph, and the problem turns into a longest path problem.

That is, if block $j$ can be placed on block $i$, there is an edge $(i, j)$ between $i$ and $j$, and the edge weight is the height chosen for block $j$.

Another issue in this problem is that each block has three choices of height; how should the graph be built?

We may split every block into three stacking orientations, i.e. decompose one block into three blocks, each of the resulting blocks choosing a different height.

The initial starting point is the ground, whose base is infinitely large, so every block is reachable from the ground; of course, when writing the program we do not need to write out infinity explicitly.

Suppose there are two blocks with edges $31, 41, 59$ and $33, 83, 27$ respectively; then the whole DAG looks like the figure below.

![](./images/dag-babylon.png)

The solid blue box in the figure marks the group of blocks obtained by splitting one block; the base edge lengths are written with $\{\}$ because once a block has chosen its height, the base edges are unordered.

The dashed yellow box marks the part that is computed repeatedly; this repeated computation can be avoided with [memoized search](./memo.md).

### Transition

The problem asks for the maximum height of the tower, which has already been turned into a longest path problem. The starting point, as said above, is the ground; what about the end point? Clearly the end point is determined naturally: it is when no other block can be placed on top of some block.

Now let us consider the transition equation.

Let $d(i,r)$ denote the maximum height when block $i$ is at the bottom and is stacked in orientation $r$. Then we have the following transition equation:

$$
d(i, r) = \max\left\{d(j, r') + h\right\}
$$

Here $j$ ranges over all blocks that can be placed on block $i$ stacked in orientation $r$, $r'$ is the corresponding orientation of $j$, and $h$ is the height of block $i$ in orientation $r$.

??? note "Implementation"
    ```cpp
    --8<-- "docs/dp/code/dag/dag_1.cpp"
    ```
