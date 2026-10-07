---
title: Tree block decomposition
---

## Ways to decompose a tree into blocks

See [The real Mo's algorithm on trees](../misc/mo-algo-on-tree.md).

You can also see [ouuan's blog / Mo's algorithm, Mo's algorithm with updates and Mo's algorithm on trees explained / Mo's algorithm on trees](https://ouuan.github.io/莫队、带修莫队、树上莫队详解/#树上莫队).

Mo's algorithm on trees can likewise be looked up in those two articles.

## Applications of tree block decomposition

Besides Mo's algorithm, tree block decomposition can also be applied flexibly to some other problems on trees. However, problems solvable by tree block decomposition usually have better solutions, so there are relatively few such problems.

As a side note, the tree block decomposition solution of "gty 的妹子树" can be broken by a star graph.

### [BZOJ4763 雪辉](https://hydro.ac/p/bzoj-P4763)

First decompose the tree into blocks, then for the key vertex of every block precompute the bitset of colors on the path to each key vertex among its ancestors, as well as the nearest key ancestor of every key vertex; the complexity is $O(n\sqrt n+\frac{nc}{32})$, where $n\sqrt n$ is the complexity of jumping upward by brute force from every key vertex and $\frac{nc}{32}$ is the complexity of storing $O(n)$ `bitset`s.

When answering a query, first jump by brute force from an endpoint of the path to the key vertex of its block, then jump block by block upward from that key vertex until reaching the block containing the $lca$, and then jump by brute force to the $lca$. The `bitset`s between key vertices have already been precomputed; the rest is computed during the brute-force jumps. The complexity of a single query is $O(\sqrt n+\frac c{32})$, where $\sqrt n$ is the complexity of the brute-force jumps inside a block and of jumping block by block upward, and $O(\frac c{32})$ is the complexity of merging the precomputed results with the results of the brute-force jumps. The number of colors can be obtained with `count()` of the `bitset`, and $\operatorname{mex}$ with `_Find_first()` of the `bitset`.

So the total complexity is $O((n+m)(\sqrt n+\frac c{32}))$.

??? note "Reference code"
    ```cpp
    --8<-- "docs/ds/code/tree-decompose/tree-decompose_1.cpp"
    ```

### [BZOJ4812 由乃打扑克](https://hydro.ac/p/bzoj-P4812)

This problem is basically the same as the previous one; the only difference is how to compute the answer once the `bitset` is obtained.

~~Since BZOJ measures the total time limit over all test cases, it is hard to break, so you can get away with `_Find_next()`.~~

The intended solution processes $16$ bits at a time: for all $2^{16}$ possible states precompute the number of consecutive ones in the high bits, the number of consecutive ones in the low bits, and the contribution of the middle. The only catch is that you then have to hand-write a `bitset`, because the standard library `bitset` cannot extract a given group of $16$ bits…

The code can be found in [this blog post](https://www.cnblogs.com/FallDream/p/bzoj4763.html).
