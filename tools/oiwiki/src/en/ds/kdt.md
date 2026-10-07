---
title: K-D Tree
---

A k-D Tree (KDT, k-Dimension Tree) is a data structure that can **efficiently handle information in $k$-dimensional space**.

When the number of nodes $n$ is much larger than $2^k$, a k-D Tree is very time-efficient.

In competitive programming problems we usually have $k=2$. When analyzing time complexity on this page, $k$ is treated as a constant.

## Building the tree

A k-D Tree has the shape of a binary search tree, and every node of this binary search tree corresponds to a point in $k$-dimensional space. The points of every subtree lie inside a $k$-dimensional hyperrectangle, and all points inside this hyperrectangle belong to that subtree.

Suppose we know the coordinates of $n$ distinct points in $k$-dimensional space and want to build a k-D Tree from them. The steps are as follows:

1.  If the current hyperrectangle contains only one point, return that point.

2.  Choose a dimension and split the current hyperrectangle into two hyperrectangles along this dimension.

3.  Choose the split point: pick a point in the chosen dimension; the points whose value in this dimension is smaller than that of the chosen point go into one hyperrectangle (the left subtree), the rest go into the other (the right subtree).

4.  Make the chosen point the root of this subtree, recursively build the left and right subtrees on the two resulting hyperrectangles, and maintain the subtree information.

For easier understanding, here is an example with $k=2$.

![](./images/kdt1.jpg)

The resulting k-D Tree might look like this:

![](./images/kdt2.jpg)

The coordinates at each node of the tree are the coordinates of the chosen split point, and the $x$ or $y$ next to a non-leaf node is the chosen split dimension.

This way the complexity cannot be guaranteed. For steps $2$ and $3$ we propose two optimizations:

1.  Cycle through the $k$ dimensions in turn, so that in any $k$ consecutive levels every dimension is split exactly once.
2.  When choosing the split point in a dimension, choose the **median** in that dimension, which keeps the sizes of the left and right subtrees as equal as possible.

One can see that with optimization $2$ the height of the resulting k-D Tree is at most $\log n+O(1)$.

Now the bottleneck of the construction is quickly selecting the median in one dimension and placing the points with a smaller value in that dimension to its left and the rest to its right. If we used the `sort` function to sort along that dimension every time, the time complexity would be $O(n\log^2 n)$. In fact, finding the median of $n$ elements once and placing it at its correct sorted position can be done in $O(n)$.

Let us recall the idea of quicksort. Each time we pick a number, put the numbers smaller than it on its left and the larger ones on its right, so that this number is in its correct sorted position, and then recursively sort the values on the left and on the right. The expected complexity is $O(n\log n)$. But since a k-D Tree only requires the median to be at its correct sorted position, we only need to recurse into **the side** that contains the median. It can be proven that the expected complexity is then $O(n)$. The `algorithm` library has a function `nth_element()` that does exactly this: to find, among the values between `s[l]` and `s[r]`, the one that would be at position `s[mid]` after sorting with the comparison rule `cmp`, while guaranteeing that the values to the left of `s[mid]` are smaller than `s[mid]` and those to the right are larger, simply write `nth_element(s+l,s+mid,s+r+1,cmp)`.

With this idea, the time complexity of building a k-D Tree is $O(n\log n)$.

## Operations in high-dimensional space

To query some information about all points inside a high-dimensional rectangle, store for every node the maximum and minimum coordinate in every dimension within its subtree. If the rectangle of the current subtree does not intersect the queried rectangle, do not search its subtree; if the rectangle of the current subtree is completely contained in the queried rectangle, return the sum of weights of all points in the subtree; otherwise check whether the current point lies inside the queried rectangle, update the answer, and search recursively in the left and right subtrees.

??? note "Implementation"
    ```cpp
    int query(int p) {
      if (!p) return 0;
      bool flag{false};
      for (int k : {0, 1}) flag |= (!(l.x[k] <= t[p].L[k] && t[p].R[k] <= h.x[k]));
      if (!flag) return t[p].sum;
      for (int k : {0, 1})
        if (t[p].R[k] < l.x[k] || h.x[k] < t[p].L[k]) return 0;
      int ans{0};
      flag = false;
      for (int k : {0, 1}) flag |= (!(l.x[k] <= t[p].x[k] && t[p].x[k] <= h.x[k]));
      if (!flag) ans = t[p].v;
      return ans += query(t[p].l) + query(t[p].r);
    }
    ```

### Complexity analysis

Consider the two-dimensional case first. When querying a rectangle $R$, we divide the nodes of the k-D Tree into three classes:

1.  disjoint from $R$;
2.  completely contained in $R$;
3.  partially contained in $R$.

Clearly the complexity of a single query is the number of class 3 nodes. Note that the rectangle of a class 3 node either completely contains $R$, or such rectangles do not contain one another; there are obviously only $O(h)=O(\log n)$ of the former, so let us analyze the number of the latter.

First, without loss of generality, shift all sides of the rectangle by $\epsilon$ so that the query rectangle does not pass through any existing point. This obviously does not affect the set of points covered by the query.

Note that the rectangle of a class 3 node that is not in a containment relation must be crossed by a side of $R$. So we only need to count the rectangles crossed by each side of $R$, i.e., how many node rectangles a single segment can pass through at most.

Consider some node $u$: it has four grandchildren, and on the way to each grandchild it is split once in each of the two dimensions. By observation, when a rectangle is split into four sub-rectangles this way, a segment parallel to a coordinate axis passes through at most two of them; that is, a query starting from $u$ descends into at most two grandchildren that still have class 3 nodes (this may fail if the segment coincides exactly with a split boundary, but shifting the boundary of the query rectangle rules this case out).

Since during construction every point is the median of its whole subtree in the current split dimension, the subtree size must halve. So, if the subtree size of $u$ is $n$, we can write the following recurrence:

$$
T(n)=2T(n/4)+O(1)
$$

By the master theorem, $T(n)=O(\sqrt{n})$.

Generalizing the recurrence to $k$ dimensions gives $T(n)=2^{k-1}T(n/2^k)+O(1)$, hence $T(n)=O(n^{1-\frac1k})$ (treating $k$ as a constant).

### Insertion/deletion

If the maintained set of $k$-dimensional points is mutable, i.e., points may be inserted or deleted, the balance of the k-D Tree can no longer be guaranteed. Because of how a k-D Tree is constructed, it cannot support rotations, and random priorities like those of an FHQ treap cannot guarantee its complexity either. There are two common maintenance methods.

???+ note "Note"
    Many contestants use the scapegoat tree structure for maintenance. But note that the complexity analysis above requires the subtree size of the children to be strictly halved, i.e., the tree height must be strictly $\log n+O(1)$, while a scapegoat tree only guarantees a height of $O(\log n)$, so the query complexity cannot be guaranteed.

#### Square-root rebuilding

When inserting, first store the points to be inserted, and rebuild once every $B$ insertions.

For deletion, just mark the node. If stricter requirements apply, keep track of how many nodes in the tree have been deleted and rebuild when the count reaches $B$.

Updates cost amortized $O(n\log n/B)$ and queries $O(B+n^{1-\frac1k})$; if the numbers of updates and queries are of the same order, $B=O(\sqrt{n\log n})$ is optimal (update $O(\sqrt{n\log n})$, query $O(\sqrt{n\log n}+n^{1-\frac1k})$).

#### Binary grouping

Maintain several k-D Trees whose sizes are powers of $2$, such that the sizes sum to $n$.

When inserting, add a new k-D Tree of size $1$, then repeatedly merge trees of equal size (simply flatten and rebuild). In the implementation it suffices to rebuild only once.

It is easy to see that the sizes of the trees to be merged must start from $2^0$ with consecutive exponents. The complexity is similar to binary addition, amortized $O(n\log^2 n)$, since the rebuild itself carries a $\log$ factor.

For a query, simply query each tree separately; the complexity is $O\left(\sum_{i\geq0} (\frac n{2^i})^{1-\frac1k}\right)=O(n^{1-\frac1k})$.

### Example problem

???+ note "[Luogu P4148 简单题](https://www.luogu.com.cn/problem/P4148)"
    On an $n\times n$ two-dimensional matrix with all initial values $0$, perform $q$ operations, each of one of two types:
    
    1.  `1 x y A`: add $A$ to the number at coordinates $(x,y)$.
    2.  `2 x1 y1 x2 y2`: output the sum of the numbers in the rectangle with lower-left corner $(x1,y1)$ and upper-right corner $(x2,y2)$ (including the boundary).
    
    Forced online. Memory limit `20M`. It is guaranteed that the answer and all intermediate values fit in an `int`.
    
    $1\le n\le 500000 , 1\le q\le 200000$

The 20M memory limit rules out all nested trees, forced online rules out CDQ divide and conquer; only a k-D Tree remains.

Below is sample code using binary grouping.

??? note "Sample code"
    ```cpp
    --8<-- "docs/ds/code/kdt/kdt_3.cpp"
    ```

## Neighborhood queries

???+ warning "Warning"
    The worst-case time complexity of a single nearest-point query with a k-D Tree is still $O(n)$, but it is nevertheless an excellent heuristic for scoring partial points; use it with care. The explanation of neighborhood queries here only serves to deepen the understanding of the k-D Tree structure.

???+ note "Example problem [Luogu P1429 平面最近点对（加强版）](https://www.luogu.com.cn/problem/P1429)"
    Given $n$ points $(x_i,y_i)$ in the plane, find the [Euclidean distance](../geometry/distance.md#euclidean-distance) between the closest pair of points in the plane.
    
    $2\le n\le 200000 , 0\le x_i,y_i\le 10^9$

First build a 2-D Tree over these $n$ points.

Enumerate every node and, for each node, find the closest point different from it; this gives the answer. Traversing every node of the 2-D Tree by brute force for each node costs $O(n)$, so pruning is needed. We can maintain, for each subtree, the minimum and maximum coordinate of all its nodes in every dimension. Suppose the closest pair distance found so far is $ans$; if the **minimum** distance from the query point to the rectangle enclosing all points of a subtree is at least $ans$, that subtree certainly contains no answer, so we do not enter it.

In addition, a heuristic search can be used: if both subtrees of a node may contain the answer, search first in the subtree closer to the query point. One may say that **the minimum distance from the query point to the rectangle of a subtree is the heuristic function of this problem**.

??? note "Sample code"
    ```cpp
    --8<-- "docs/ds/code/kdt/kdt_1.cpp"
    ```

???+ note "Example problem [CQOI2016 K 远点对](https://loj.ac/problem/2043)"
    Given $n$ points $(x_i,y_i)$ in the plane, find the distance between the $k$-th farthest unordered pair of points under the Euclidean distance.
    
    $n\le 100000 , 1\le k\le 100 , 0\le x_i,y_i<2^{31}$

Similar to the previous example, except that the closest pair becomes the $k$-th farthest pair, and the heuristic function becomes the maximum distance from the query point to the rectangle of a subtree. Use a min-heap to maintain the distances of the $k$ farthest pairs found so far; if the distance of the current pair is larger than the top of the heap, pop the top and insert this distance. Likewise, use the distance at the top of the heap for pruning.

Since the problem stresses unordered pairs, i.e., swapping the two points gives the same pair, every ordered pair is counted twice, so the input $k$ must be multiplied by $2$.

??? note "Sample code"
    ```cpp
    --8<-- "docs/ds/code/kdt/kdt_2.cpp"
    ```

## Exercises

[SDOI2010 捉迷藏](https://www.luogu.com.cn/problem/P2479)

[Violet 天使玩偶/SJY 摆棋子](https://www.luogu.com.cn/problem/P4169)

[国家集训队 JZPFAR](https://www.luogu.com.cn/problem/P2093)

[BOI2007 Mokia 摩基亚](https://www.luogu.com.cn/problem/P4390)

[Luogu P4475 巧克力王国](https://www.luogu.com.cn/problem/P4475)

[CH 弱省胡策 R2 TATT](https://www.luogu.com.cn/problem/P3769)
