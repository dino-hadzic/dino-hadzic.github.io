---
title: Balanced tree nested in a segment tree
---

## Common uses

In algorithm competitions we sometimes need to maintain multi-dimensional information. In such situations we often use nested trees to store the information. When we need to maintain predecessors, successors, the $k$-th largest element, the rank of a number, or support insertions and deletions, we usually need a balanced tree, i.e., a segment tree whose nodes hold balanced trees.

## Procedure

We explain the implementation principle on the problem **二逼平衡树** (LOJ 106).

To build the nested tree, we build the outer segment tree as usual, and for each of its nodes we build a balanced tree containing the part of the sequence covered by that node. Concretely, we can insert the elements of the sequence one by one: whenever we pass a segment tree node, we add the element to the balanced tree of that node.

Operation 1, the rank of a value in an interval: we process the outer segment tree as usual, and for the balanced tree of each node inside the interval we return the number of elements smaller than the value; when merging intervals we add these counts. Finally the result $+1$ is the rank of the value in the interval.

Operation 2, the value with rank $k$ in an interval: we can use binary search. An element may occur several times, so its rank is an interval, and some elements do not occur in the original sequence at all. Hence we use an idea similar to operation 1: we binary search using the number of elements smaller than the value as the reference, which gives the answer.

Operation 3, replacing one number with another: we simply delete the number from all balanced trees that contain it and then insert the new number. The outer segment tree is processed as usual.

Operation 4, the predecessor of a value in an interval: we process the outer segment tree as usual, and for the balanced tree of each node inside the interval we return the predecessor of the value in that balanced tree; when merging interval results we take the maximum.

## Properties

### Space complexity

Every element is added to $O(\log n)$ balanced trees, so the space complexity is $O((n + q)\log{n})$.

### Time complexity

-   For operations 1, 3 and 4 we perform $O(\log{n})$ operations on the outer segment tree, each of which performs $O(\log{n})$ operations on an inner balanced tree, so the time complexity is $O(\log^2{n})$.
-   Operation 2 has an extra binary search, so it is $O(\log^3{n})$.

## Classic example

[LOJ 106 二逼平衡树](https://loj.ac/problem/106): outer segment tree, inner balanced trees.

## Implementation

For the balanced tree code, see [Splay](./splay.md) and other articles.

Operation 1:

```cpp
int vec_rank(int k, int l, int r, int x, int y, int t) {
  if (x <= l && r <= y) {
    return spy[k].chk_rank(t);
  }
  int mid = l + r >> 1;
  int res = 0;
  if (x <= mid) res += vec_rank(k << 1, l, mid, x, y, t);
  if (y > mid) res += vec_rank(k << 1 | 1, mid + 1, r, x, y, t);
  if (x <= mid && y > mid) res--;
  return res;
}
```

Operation 2:

```cpp
int el = 0, er = 100000001, emid;
while (el != er) {
  emid = el + er >> 1;
  if (vec_rank(1, 1, n, tl, tr, emid) - 1 < tk)
    el = emid + 1;
  else
    er = emid;
}
printf("%d\n", el - 1);
```

Operation 3:

```cpp
void vec_chg(int k, int l, int r, int loc, int x) {
  int t = spy[k].find(dat[loc]);
  spy[k].dele(t);
  spy[k].insert(x);
  if (l == r) return;
  int mid = l + r >> 1;
  if (loc <= mid) vec_chg(k << 1, l, mid, loc, x);
  if (loc > mid) vec_chg(k << 1 | 1, mid + 1, r, loc, x);
}
```

Operation 4:

```cpp
int vec_front(int k, int l, int r, int x, int y, int t) {
  if (x <= l && r <= y) return spy[k].chk_front(t);
  int mid = l + r >> 1;
  int res = 0;
  if (x <= mid) res = max(res, vec_front(k << 1, l, mid, x, y, t));
  if (y > mid) res = max(res, vec_front(k << 1 | 1, mid + 1, r, x, y, t));
  return res;
}
```

## Related algorithms

When a problem with multi-dimensional information does not require online processing, we can also consider divide-and-conquer algorithms such as [CDQ divide and conquer](../misc/cdq-divide.md) or [parallel binary search](../misc/parallel-binsearch.md) to avoid advanced data structures and reduce the implementation difficulty.
