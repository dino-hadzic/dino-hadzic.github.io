---
title: Tree center
---

## Definition

In a tree, if taking node $x$ as the root makes the longest chain starting from $x$ the shortest possible, then $x$ is called the center of the tree.

## Properties

-   The center of a tree is not necessarily unique, but there are at most $2$ centers, and the two centers are adjacent.
-   The center of a tree always lies on the diameter of the tree.
-   The paths from every node of the tree to its farthest node all pass through the center of the tree.
-   When the center of the tree is the root, the two chains from it to the endpoints of the diameter are the longest and the second longest chain.
-   When two trees are merged into one by connecting them with an edge, connecting their centers minimizes the diameter of the new tree.
-   The distance from the center of the tree to any other node does not exceed half of the diameter of the tree.

## Method

Find a node $x$ such that, when it is taken as the root, the length of the longest chain is minimal.

### Steps

1.  Maintain $len1_x$, the longest chain inside the subtree of node $x$.
2.  Maintain $len2_x$, the longest chain that does not overlap with $len1_x$.
3.  Maintain $up_x$, the longest chain outside the subtree of node $x$; this chain necessarily passes through the parent of $x$.
4.  Find the node $x$ minimizing $\max(len1_x, up_x)$; this $x$ is the center of the tree.

???+ note "Reference code"
    ```cpp
    // this code assumes nodes are numbered from 1, i.e. i ∈ [1,n], and stores the graph with vectors
    int d1[N], d2[N], up[N], x, y, mini = 1e9;  // d1,d2 correspond to len1,len2 in the text above
    
    struct node {
      int to, val;  // to is the node the edge points to, val is the edge weight
    };
    
    vector<node> nbr[N];
    
    void dfsd(int cur, int fa) {  // compute len1 and len2
      for (node nxtn : nbr[cur]) {
        int nxt = nxtn.to, w = nxtn.val;  // nxt is the node this edge leads to, val is the edge weight
        if (nxt == fa) {
          continue;
        }
        dfsd(nxt, cur);
        if (d1[nxt] + w > d1[cur]) {  // the longest chain can be updated
          d2[cur] = d1[cur];
          d1[cur] = d1[nxt] + w;
        } else if (d1[nxt] + w > d2[cur]) {  // the longest chain cannot be updated, but the second longest can
          d2[cur] = d1[nxt] + w;
        }
      }
    }
    
    void dfsu(int cur, int fa) {
      for (node nxtn : nbr[cur]) {
        int nxt = nxtn.to, w = nxtn.val;
        if (nxt == fa) {
          continue;
        }
        up[nxt] = up[cur] + w;
        if (d1[nxt] + w != d1[cur]) {  // if the longest chain in our own subtree is not inside the subtree of nxt
          up[nxt] = max(up[nxt], d1[cur] + w);
        } else {  // the longest chain in our own subtree is inside the subtree of nxt, only the second longest can be used
          up[nxt] = max(up[nxt], d2[cur] + w);
        }
        dfsu(nxt, cur);
      }
    }
    
    void GetTreeCenter() {  // find the centers of the tree, denoted x and y (if it exists)
      dfsd(1, 0);
      dfsu(1, 0);
      for (int i = 1; i <= n; i++) {
        if (max(d1[i], up[i]) < mini) {  // found the node with the currently smallest max(len1[x],up[x])
          mini = max(d1[i], up[i]);
          x = i;
          y = 0;
        } else if (max(d1[i], up[i]) == mini) {  // the other center
          y = i;
        }
      }
    }
    ```

### Example

Suppose we have the following tree:

```text
           A
          / \
         B   C
        / \   \
       D   E   F
```

-   The diameter of the tree is $D \rightarrow B \rightarrow A \rightarrow C \rightarrow F$. The length of the diameter is $4$.
-   The center of the tree is node $A$, because the longest chains starting from $A$ (to $D$ or to $F$) both have length $2$.
-   If $B$ or $C$ were taken as the root, the longest chain starting from those nodes would be longer, so they are not the center of the tree.

### Time complexity

The time complexity of the above algorithm is $O(n)$, where $n$ is the number of nodes in the tree.

## References

-   [TutorialsPoint: Centers of a Tree](https://www.tutorialspoint.com/centers-of-a-tree)
-   [ProofWiki: Definition of Center of Tree](https://proofwiki.org/wiki/Definition:Center_of_Tree)
-   [Wikipedia: Tree (graph theory)](https://en.wikipedia.org/wiki/Tree_%28graph_theory%29#Properties)
