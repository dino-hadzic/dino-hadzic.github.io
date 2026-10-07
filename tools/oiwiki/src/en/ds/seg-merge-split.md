---
title: Segment tree merging & splitting
---

Merging and splitting segment trees are commonly used techniques, typical for situations in which a segment tree on values maintains a multiset.

For example, if several operations are located at some nodes of a tree and the information of the children must be passed bottom-up to the parent, while the information at a single node is conveniently maintained by a segment tree, segment tree merging can be applied to control the overall complexity.

## Segment tree merging

### Procedure

As the name suggests, segment tree merging means building a new segment tree in which every node is the result of merging the corresponding nodes of the two original segment trees. It is often used to maintain information on trees or graphs.

Obviously we cannot actually build a complete new segment tree every time, so we use the segment tree with dynamic node creation described earlier.

The merging procedure is essentially quite brute-force:

Let the two segment trees be A and B; we merge recursively starting from node 1.

When the recursion reaches some node, if the corresponding node of tree A or tree B is empty, directly return the corresponding node of the other tree – this uses the property of dynamic node creation.

If the recursion reaches a leaf, merge the corresponding nodes of the two trees.

Finally, update the current node from its children and return it.

???+ note "Complexity of segment tree merging"
    Obviously, for two full segment trees the complexity of a single merge is $O(n)$. In practice, however, segment trees on values are usually used, and the total number of nodes of all segment trees to be merged is not much larger than $n$. Moreover, the same segment tree is usually not merged repeatedly, so the total number of nodes added is roughly of order $n\log n$. Thus the total complexity of merging all segment trees is $O(n\log n)$. Of course, in some situations a mergeable heap may be the better choice.

### Implementation

```cpp
int merge(int a, int b, int l, int r) {
  if (!a) return b;
  if (!b) return a;
  if (l == r) {
    // do something...
    return a;
  }
  int mid = (l + r) >> 1;
  tr[a].l = merge(tr[a].l, tr[b].l, l, mid);
  tr[a].r = merge(tr[a].r, tr[b].r, mid + 1, r);
  pushup(a);
  return a;
}
```

### Example problem

???+ note "[Luogu P4556 \[Vani 有约会\] 雨天的尾巴/【模板】线段树合并](https://www.luogu.com.cn/problem/P4556)"
    ??? note "Solution idea"
        Template problem for segment tree merging: use differencing to turn the updates on the tree into point updates, then DFS upward merging the segment trees and compute the answers.
    
    ??? note "Reference code"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-merge.cpp"
        ```

## Segment tree splitting

### Procedure

Segment tree splitting is essentially the inverse of segment tree merging. Splitting only makes sense for ordered sequences; for unordered sequences it is meaningless. It is commonly used on segment trees on values with dynamic node creation.

Note that when both splitting and merging are present, nodes must be recycled during merging, to avoid a node being used more than once during splitting.

To split $[l,r]$ out of a segment tree over the interval $[1,N]$ and build a new tree:

Recursively split starting from node 1; when the node does not exist or its interval $[s,t]$ is disjoint from $[l,r]$, return directly.

When $[s,t]$ and $[l,r]$ intersect, a new node must be created.

When $[s,t]$ is contained in $[l,r]$, the current node must be attached directly under the new tree and the old edge cut.

???+ note "Complexity of segment tree splitting"
    One can see that at most $\log n$ edges are cut, so the time complexity of each split is $O(\log⁡ n)$, the same as a range query.

### Implementation

```cpp
void split(int &p, int &q, int s, int t, int l, int r) {
  if (t < l || r < s) return;
  if (!p) return;
  if (l <= s && t <= r) {
    q = p;
    p = 0;
    return;
  }
  if (!q) q = New();
  int m = s + t >> 1;
  if (l <= m) split(ls[p], ls[q], s, m, l, r);
  if (m < r) split(rs[p], rs[q], m + 1, t, l, r);
  push_up(p);
  push_up(q);
}
```

### Example problem

???+ note "[P5494【模板】线段树分裂](https://www.luogu.com.cn/problem/P5494)"
    ??? note "Solution idea"
        Template problem for segment tree splitting: split out $[x,y]$.
        
        -   Merge tree $t$ into tree $p$: a single merge.
        
        -   Insert $x$ copies of $q$ into tree $p$: a point update.
        
        -   Query the number of elements in $[x,y]$: a range sum.
        
        -   Query the $k$-th smallest element.
    
    ??? note "Reference code"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-split.cpp"
        ```

## Exercises

-   [Luogu P4556 \[Vani 有约会\] 雨天的尾巴/【模板】线段树合并](https://www.luogu.com.cn/problem/P4556)
-   [Luogu P5494【模板】线段树分裂](https://www.luogu.com.cn/problem/P5494)
-   [Luogu P1600 天天爱跑步](https://www.luogu.com.cn/problem/P1600)
-   [Luogu P4577 \[FJOI2018\] 领导集团问题](https://www.luogu.com.cn/problem/P4577)
-   [Luogu P2824 \[HEOI2016/TJOI2016\] 排序](https://www.luogu.com.cn/problem/P2824)
