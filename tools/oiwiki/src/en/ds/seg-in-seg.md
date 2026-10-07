---
title: Segment tree nested in a segment tree
---

## Common uses

In algorithm competitions we sometimes need to maintain multi-dimensional information. In such situations we often use nested trees (a "tree of trees") to store the information.

## Implementation principle

Let us consider how nested trees can implement point updates and region queries on a two-dimensional plane. Look at the outer segment tree: the subtrees of its $n$ leaves, numbered $1$ to $n$, represent the segment trees of rows $1$ to $n$. The parent of two such leaves then represents the region covered by the subtrees of its two children.

## Properties

### Space complexity

Normally we cannot afford to build a full inner segment tree for every node of the outer segment tree, since the memory requirement would be too large. Nested trees therefore usually create nodes dynamically. A single update touches $\log{n}$ nodes of the outer segment tree, and $\log{n}$ nodes in the subtree of each of them, so a single update creates at most $\log^2{n}$ nodes.

### Time complexity

For a query we perform $\log{n}$ operations on the outer segment tree, each of which performs $\log{n}$ operations on an inner segment tree, so the time complexity is $\log^2{n}$.
An update has the same complexity as a query, also $\log^2{n}$.

## Classic example

[Luogu P3810 陌上花开](https://www.luogu.com.cn/problem/P3810): handle the first dimension by sorting, then maintain the second and third dimensions with nested trees.

## Sample code

Query on the second dimension

```cpp
int tree_query(int k, int l, int r, int x) {
  if (k == 0) return 0;
  if (1 <= l && r <= sec[x].y) return vec_query(ou_root[k], 1, p, 1, sec[x].z);
  int mid = l + r >> 1, res = 0;
  if (1 <= mid) res += tree_query(ou_ch[k][0], l, mid, x);
  if (sec[x].y > mid) res += tree_query(ou_ch[k][1], mid + 1, r, x);
  return res;
}
```

Update on the second dimension

```cpp
void tree_insert(int &k, int l, int r, int x) {
  if (k == 0) k = ++ou_tot;
  vec_insert(ou_root[k], 1, p, sec[x].z);
  if (l == r) return;
  int mid = l + r >> 1;
  if (sec[x].y <= mid)
    tree_insert(ou_ch[k][0], l, mid, x);
  else
    tree_insert(ou_ch[k][1], mid + 1, r, x);
}
```

Query on the third dimension

```cpp
int vec_query(int k, int l, int r, int x, int y) {
  if (k == 0) return 0;
  if (x <= l && r <= y) return data[k];
  int mid = l + r >> 1, res = 0;
  if (x <= mid) res += vec_query(ch[k][0], l, mid, x, y);
  if (y > mid) res += vec_query(ch[k][1], mid + 1, r, x, y);
  return res;
}
```

Update on the third dimension

```cpp
void vec_insert(int &k, int l, int r, int loc) {
  if (k == 0) k = ++tot;
  data[k]++;
  if (l == r) return;
  int mid = l + r >> 1;
  if (loc <= mid) vec_insert(ch[k][0], l, mid, loc);
  if (loc > mid) vec_insert(ch[k][1], mid + 1, r, loc);
}
```

## Related algorithms

When a problem with multi-dimensional information does not require online processing, we can also consider divide-and-conquer algorithms such as **CDQ divide and conquer** or **parallel binary search** to avoid advanced data structures and reduce the implementation difficulty.
