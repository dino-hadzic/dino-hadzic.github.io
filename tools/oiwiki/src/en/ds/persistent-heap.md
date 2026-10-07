---
title: Persistent mergeable heap
---

Persistent mergeable heaps are usually used to solve the $k$ shortest paths problem.

If the time complexity of a mergeable heap is not amortized, then after making it persistent the complexity of a single operation is guaranteed to be $O(\log n)$, i.e., it cannot degrade on specially crafted data.

## Persistent leftist tree

Before studying this section, please get familiar with the [leftist tree](./leftist-tree.md).

### Procedure

Recall how leftist trees are merged. Suppose we want to merge two leftist trees rooted at $x$ and $y$ that satisfy the min-heap property:

1.  If one of the nodes $x,y$ is empty, return $x+y$.

2.  Among the nodes $x,y$ choose the one with the smaller value; it becomes the root of the merged leftist tree.

3.  Recursively merge the right subtree of $x$ with $y$ and make the resulting root the right child of $x$.

4.  Maintain the leftist property of the merged tree, update the `dist` value, and return the chosen root.

Since every recursive call decreases `dist[x]+dist[y]` by one and `dist[x]` is $O(\log n)$, at most $O(\log n)$ nodes are modified per operation, so the time complexity is $O(\log n)$.

Persistence requires keeping the history so that earlier versions can be accessed later. To make a leftist tree persistent, we have to copy the path that is modified along the way.

So the merge of persistent leftist trees goes like this:

1.  If one of the nodes $x,y$ is empty, return $x+y$.

2.  Among the nodes $x,y$ choose the one with the smaller value and create a copy $p$ of it; the copy becomes the root of the merged leftist tree.

3.  Recursively merge the right subtree of $p$ with $y$ and make the resulting root the right child of $p$.

4.  Maintain the leftist property of the tree rooted at $p$, update its `dist` value, and return $p$.

Since a leftist tree modifies and creates at most $O(\log n)$ nodes per operation, with $m$ operations both the time and the space complexity of the persistent leftist tree are $O(m\log n)$.

### Reference implementation

```cpp
int merge(int x, int y) {
  if (!x || !y) return x + y;
  if (v[x] > v[y]) swap(x, y);
  int p = ++cnt;
  lc[p] = lc[x];
  v[p] = v[x];
  rc[p] = merge(rc[x], y);
  if (dist[lc[p]] < dist[rc[p]]) swap(lc[p], rc[p]);
  dist[p] = dist[rc[p]] + 1;
  return p;
}
```
