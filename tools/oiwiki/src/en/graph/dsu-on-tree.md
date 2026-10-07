---
title: DSU on tree
---

## Introduction

What is a heuristic algorithm?

A heuristic algorithm is an optimization of some algorithm based on human experience and intuition.

For example, the most common one is the heuristic merge in a union-find structure; the code looks like this:

```cpp
void merge(int x, int y) {
  int xx = find(x), yy = find(y);
  if (size[xx] < size[yy]) swap(xx, yy);
  fa[yy] = xx;
  size[xx] += size[yy];
}
```

Here, for two sets of different sizes, we merge the smaller set into the larger one rather than the larger into the smaller.

Why? The size of the set can be regarded (under normal circumstances) as the height of the set, and merging a set of smaller height into one of larger height obviously helps us find the parent.

Making the tree of smaller height a subtree of the tree of larger height—this optimization can be called the heuristic merge algorithm.

## The algorithm

DSU on tree (heuristic merge on a tree) is an algorithm that, for certain offline problems on trees, can be as fast as or faster than most algorithms while being easier to understand and implement.

Consider the following problem: [Counting colors on a tree](https://www.luogu.com.cn/problem/U41492).

???+ note "Introductory problem"
    Given a tree with $n$ nodes rooted at $1$, where the color of node $u$ is $c_u$, for every node $u$ answer how many distinct colors appear in the subtree rooted at $u$.
    
    $n\le 2\times 10^5$.

![dsu-on-tree-1.png](./images/dsu-on-tree-1.svg)

Such problems are mostly solved with lots of data structures (nested data structures and the like); if offline processing is allowed, is there a simpler way?

## Process

Since offline processing is supported, consider preprocessing and then outputting the answers in $O(1)$.

Direct brute-force preprocessing has time complexity $O(n^2)$: we perform one traversal for every node, each traversal obviously has complexity of the same order as $n$, and there are $n$ nodes, so the complexity is $O(n^2)$.

We can notice that the answer for every node is obtained from its subtree and itself; let us use this property.

We can first preprocess the subtree size of every node and its heavy child; as in heavy-light decomposition, the heavy child is the child whose subtree has the most nodes, and this can obviously be done in $O(n)$.

Let $cnt_i$ denote the number of occurrences of color $i$, and $ans_u$ the answer for node $u$.

To process a node $u$, we proceed in the following steps:

1.  First traverse the light (non-heavy) children of $u$ and compute their answers, but **do not keep their effect on the array $cnt$**;
2.  Traverse its heavy child and **keep its effect on the array $cnt$**;
3.  Traverse the nodes in the subtrees of the light children of $u$ again and add their contributions to obtain the answer for $u$.

![dsu-on-tree-2.png](./images/dsu-on-tree-2.svg)

The figure above shows an example.

This way, for one node we traverse the heavy subtree once and the non-heavy subtrees twice, which is obviously the best deal.

By carrying out this process we obtain the answers for all subtrees of that node.

Why not merge the first and the third step? Because the array $cnt$ cannot be duplicated; otherwise the memory would be too large, and we need to stay within $O(n)$ space.

Obviously, if a node $u$ is traversed $x$ times, its heavy child is traversed $x$ times and its light children (if any) $2x$ times.

Note that, except for the heavy child, $cnt$ must be cleared after every traversal.

## Proof

As in heavy-light decomposition, we define heavy and light edges (the edge to the heavy child is heavy, the others are light). For the definitions of heavy child and heavy edge see the figure below; for a tree with $n$ nodes:

The number of light edges from the root to any node of the tree does not exceed $\log n$. Suppose there are $x$ light edges from the root to the node and the subtree size of the node is $y$. Obviously the subtree size of a child connected by a light edge is less than half of its parent's (otherwise it would not be a light edge), so $y<n/2^x$, hence obviously $n>2^x$, and so $x<\log n$.

Moreover, if a node is the heavy child of its parent, its subtree must be the largest among its siblings, so none of the parents on the heavy edges along the path from any node to the root will traverse this node when computing their answers. Therefore the number of times a node is traversed equals the number of light edges on the path from it to the root $+1$ (the $+1$ is because the node itself has to be traversed). So a node is traversed $=\log n+1$ times, the total time complexity is $O(n(\log n+1))=O(n\log n)$, and outputting the answers costs $O(m)$.

![dsu-on-tree-3.png](./images/dsu-on-tree-3.svg)

*The bold edges in the figure are the heavy edges, and the children the heavy edges point to are the heavy children*

## Optimization

As mentioned in the proof, dsu on tree uses the notion of light and heavy children from heavy-light decomposition to speed up merging. That being the case, we can also directly use the dfs order obtained from heavy-light decomposition, turn the recursion into iteration, and further reduce the constant factor of dsu on tree.

The dfs order itself has the following property: the subtree of a node is always contiguous in the dfs order. Therefore, the dfs order array can be traversed in reverse. This guarantees that when we reach a node, all other nodes in its subtree have already been processed.

The dfs order obtained from heavy-light decomposition has the following nice property: a heavy chain is always contiguous in the dfs order. Therefore, when traversing the nodes in reverse dfs order, for the node at the top of a heavy chain the next node to be traversed is certainly not its parent, so its effect must be cleared; otherwise, for a node that is not at the top of a heavy chain, the previously traversed node is either its own heavy child or a node of another branch whose effect has already been cleared, so its effect can be inherited directly. On this basis, we then use the dfs order to quickly accumulate the effect of all light children and record the answer.

The above process is called the non-recursive/iterative implementation of dsu on tree (also called the dfs-order implementation of dsu on tree). Compared with the original recursive implementation, it reduces the time and space overhead of recursive function calls and obtains a considerable constant-factor optimization, **and in particular it has a significant stack-space advantage when processing trees containing many chain-like structures.**

## Implementation

??? example "Reference implementation"
    === "Recursive implementation"
        ```cpp
        --8<-- "docs/graph/code/dsu-on-tree/dsu-on-tree_1.cpp"
        ```
    
    === "Non-recursive implementation"
        ```cpp
        --8<-- "docs/graph/code/dsu-on-tree/dsu-on-tree_2.cpp"
        ```

## Applications

1.  Problems whose intended solution set by the problem setter is dsu on tree

    E.g. [CF741D](http://codeforces.com/problemset/problem/741/D). Given a tree where the value of each node is a letter from 'a' to 'v', each query asks to find, within a subtree, a path such that the characters it contains can be rearranged into a palindrome.

    Since it becomes a palindrome after rearrangement, a character that appears twice is as if it did not appear at all; in other words, the path satisfies **at most one character appears an odd number of times**.

    The usual approach is to dfs from every node, and at each node brute-force all letters to find paths whose xor with it has more than 1 bit set, then take the longest; this is $O(n^2\log n)$ and can be optimized to $O(n\log^2n)$ with dsu on tree. For the concrete approach see the further reading below.

2.  Problems that can be hacked with dsu

    Partial scores of some nested-data-structure problems (without modification operations) can be grabbed, and the complexity of dsu is better than the $O(n\sqrt{m})$ of Mo's algorithm on trees.

## Exercises

[CF600E Lomsat gelral](http://codeforces.com/problemset/problem/600/E)

Problem summary: the nodes of a tree have colors; a color dominates a subtree if and only if no other color appears in that subtree more often than it does. Find, for every subtree, the sum of all colors dominating it.

[UOJ284 Happy Game Chicken](https://uoj.ac/problem/284)

[CF1709E XOR Tree](https://codeforces.com/contest/1709/problem/E)

## References / further reading

[dsu on tree as introduced by the author of CF741D](http://codeforces.com/blog/entry/44351)

[The same author's editorial](http://codeforces.com/blog/entry/48871)
