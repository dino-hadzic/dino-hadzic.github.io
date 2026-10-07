---
title: Li Chao tree
---

## Introduction

???+ note "[Luogu 4097 \[HEOI2013\]Segment](https://www.luogu.com.cn/problem/P4097)"
    In the Cartesian plane, support the following two operations (forced online):
    
    1.  Add a line segment to the plane. The $i$-th inserted segment has index $i$, and its two endpoints are $(x_0,y_0)$ and $(x_1,y_1)$.
    2.  Given a number $k$, among the segments intersecting the line $x = k$, report the index of the segment whose intersection point has the largest $y$-coordinate (if several segments share the largest $y$-coordinate, output the one with the smallest index). In particular, if no segment intersects the given line, output $0$.
    
    Constraints: total number of operations $1 \leq n \leq 10^5$, $1 \leq k, x_0, x_1 \leq 39989$, $1 \leq y_0, y_1 \leq 10^9$.

We find that the traditional segment tree cannot maintain such information well. In such situations the **Li Chao tree** (Li Chao segment tree) comes into play.

## Procedure

We can transform the task into maintaining the following operations:

-   add a linear function with domain $[l,r]$;
-   given $k$, among all linear functions whose domain contains $k$, find the one with the largest value at $x=k$; if several functions have the same value, choose the one with the smallest index.

???+ warning "Note"
    When the segment is perpendicular to the $x$-axis, a division by zero occurs. Suppose the endpoints of the segment are $(x,y_0)$ and $(x,y_1)$ with $y_0<y_1$; then insert the linear function $f(x)=0\cdot x+y_1$ with domain $[x,x]$.

Seeing a range update, we follow the usual way segment trees solve range problems and give each node a lazy tag. The lazy tag of each node $i$ is a segment, denoted $l_i$, meaning that the whole interval represented by the node should be updated with $l_i$.

Now we need to insert a segment $f$. Consider some segment tree interval completely covered by the new segment $f$. If this interval has no tag, simply tag it with this segment.

If the interval already has a tag, since tags are hard to merge, the only option is to push the tag down. But the children also have their own tags, which may conflict as well, so we push tags down recursively.

![](images/li-chao-tree-1.png)

As shown in the figure, according to whether the value of the new segment $f$ is greater than that of the original tag $g$, we can divide the current interval into two subintervals. **One of them is certainly completely contained in the left or the right interval**; that is, of the two segments, one can only be the answer for the left interval or only for the right interval. We use that segment to recursively update the corresponding subtree and the other one as the lazy tag updating the whole interval; this guarantees the complexity of the recursive push-down. A segment is pushed down only when it can only be the answer for the left or only for the right interval, so there is no need to worry about missing a segment.

Specifically, let $m$ be the midpoint of the current interval; compare the value of the new segment $f$ at the midpoint with the value of the current best segment $g$ at the midpoint.

If the new segment $f$ is better, swap $f$ and $g$. Now consider the case where $f$ is not better than $g$ at the midpoint:

1.  If $f$ is better at the left endpoint, then $f$ and $g$ must intersect in the left half; $f$ can only beat $g$ in the left interval, so recurse into the left child to push it down.
2.  If $f$ is better at the right endpoint, then $f$ and $g$ must intersect in the right half; $f$ can only beat $g$ in the right interval, so recurse into the right child to push it down.
3.  If $g$ is better at both endpoints, $f$ can never be the answer and need not be pushed down further.

Besides these cases there is also the case where $f$ and $g$ intersect exactly at the midpoint; in the implementation it can be grouped with the case where $f$ is not better than $g$ at the midpoint, and the recursion will push down toward the endpoint where $f$ is better.

Finally, $g$ becomes the lazy tag of the current interval.

Pushing down the tag:

???+ note "Implementation"
    ```cpp
    constexpr double eps = 1e-9;
    
    int cmp(double x, double y) {  // floating-point numbers are used, so there is precision error
      if (x - y > eps) return 1;
      if (y - x > eps) return -1;
      return 0;
    }
    
    //...
    
    void upd(int root, int cl, int cr, int u) {  // update an interval fully covered by the segment
      int &v = s[root], mid = (cl + cr) >> 1;
      int bmid = cmp(calc(u, mid), calc(v, mid));
      if (bmid == 1 || (!bmid && u < v))  // in this problem remember to compare segment indices
        swap(u, v);
      int bl = cmp(calc(u, cl), calc(v, cl)), br = cmp(calc(u, cr), calc(v, cr));
      if (bl == 1 || (!bl && u < v)) upd(root << 1, cl, mid, u);
      if (br == 1 || (!br && u < v)) upd(root << 1 | 1, mid + 1, cr, u);
      // at most one of the two conditions above holds, which guarantees the complexity of the Li Chao tree
    }
    ```

Splitting the segment:

???+ note "Implementation"
    ```cpp
    void update(int root, int cl, int cr, int l, int r,
                int u) {  // locate the intervals fully covered by the inserted segment
      if (l <= cl && cr <= r) {
        upd(root, cl, cr, u);  // fully covers the current interval, update its tag
        return;
      }
      int mid = (cl + cr) >> 1;
      if (l <= mid) update(root << 1, cl, mid, l, r, u);  // recursively split the interval
      if (mid < r) update(root << 1 | 1, mid + 1, cr, l, r, u);
    }
    ```

Note that the lazy tag is not equivalent to the segment with the largest value at the midpoint of the interval.

![](images/li-chao-tree-2.png)

As shown in the figure, after adding the yellow segment only the tag of the red node is updated, while the tags of the green nodes remain unchanged. But at the midpoints of the second, third and fourth green intervals the yellow segment obviously has the largest value.

For a query we can use the idea of permanent tags: among the tagged segments of all segment tree intervals containing $x$ (at most $O(\log n)$ of them), compare to obtain the final answer.

Query:

???+ note "Implementation"
    ```cpp
    pdi query(int root, int l, int r, int d) {  // query
      if (r < d || d < l) return {0, 0};
      int mid = (l + r) >> 1;
      double res = calc(s[root], d);
      if (l == r) return {res, s[root]};
      return pmax({res, s[root]}, pmax(query(root << 1, l, mid, d),
                                       query(root << 1 | 1, mid + 1, r, d)));
    }
    ```

According to the description above, the time complexity of a query is obviously $O(\log n)$, while during insertion the original segment must be split into $O(\log n)$ intervals, and for each of them $O(\log n)$ time is spent on the recursive push-down, so the time complexity of insertion is $O(\log^2 n)$.

??? note "Reference code for [\[HEOI2013\]Segment](https://www.luogu.com.cn/problem/P4097)"
    ```cpp
    --8<-- "docs/ds/code/li-chao-tree/li-chao-tree_1.cpp"
    ```

## Merging

Similarly to merging ordinary segment trees, we define the following procedure to merge two Li Chao tree nodes $u,v$, with $u$ becoming the new root.

1.  If $v$ is empty, the procedure ends.

2.  If $u$ is empty, copy $v$ to $u$.

3.  Insert the segment corresponding to $v$ into the subtree rooted at $u$.

4.  Recursively merge the left and right subtrees of $u$ and $v$ respectively.

If the total number of nodes involved in merging several Li Chao trees is $n$, the complexity of this procedure is $O(n\log n)$: for the node corresponding to any segment, every time it is moved we either increase its depth by $1$ or delete it from the tree directly, and both operations cost $O(1)$, while the depth of each node is at most $O(\log n)$, hence the complexity above.

???+ note "Implementation"
    ```cpp
    void upd(int &root, int cl, int cr,
             int u) {  // several Li Chao trees are merged, so dynamic node creation is used
      static int idx = 0;
      if (!root) {
        s[root = ++idx] = u;
        return;
      }
      int &v = s[root], mid = (cl + cr) >> 1;
      int bmid = cmp(calc(u, mid), calc(v, mid));
      if (bmid == 1 || (!bmid && u < v)) swap(u, v);
      int bl = cmp(calc(u, cl), calc(v, cl)), br = cmp(calc(u, cr), calc(v, cr));
      if (bl == 1 || (!bl && u < v)) upd(ls[root], cl, mid, u);
      if (br == 1 || (!br && u < v)) upd(rs[root], mid + 1, cr, u);
    }
    
    int merge(int &u, int &v, int l, int r) {
      if (!u || !v) {
        return u + v;
      }
      if (l == r) {
        int b = cmp(calc(s[v], l), calc(s[u], l));
        if (b == 1 || (!b && s[v] < s[u])) return v;
        return u;
      }
      upd(u, l, r, s[v]);
      int mid = (l + r) >> 1;
      ls[u] = merge(ls[u], ls[v], l, mid);
      rs[u] = merge(rs[u], rs[v], mid + 1, r);
      return u;
    }
    ```

## Exercises

[「JSOI2008」Blue Mary 开公司](https://www.luogu.com.cn/problem/P4254)

[「CodeChef」TSUM2 Sum on Tree](https://www.codechef.com/problems/TSUM2)

[「USACO13MAR」Hill Walk G](https://www.luogu.com.cn/problem/P3081)

[「CF932F」Escape Through Leaf](https://codeforces.com/problemset/problem/932/F)
