---
title: Persistent segment tree
---

## Chairman tree

A chairman tree is a persistent segment tree over values; see the [Zhihu discussion](https://www.zhihu.com/question/59195374).

???+ warning "About functional segment trees"
    A **functional segment tree** is a segment tree based on functional programming. Functional programming treats computation as mathematical functions and avoids mutable state or variables. It is easy to see that a functional segment tree is [fully persistent](persistent.md#full-persistence-fully-persistent).

## Motivation

Consider this problem: given a sequence $a$ of $n$ integers, answer queries for the $k$-th smallest value in a specified closed interval $[l, r]$.

How would you solve it?

One possible solution is a chairman tree.
Its main idea is to preserve a historical version at every insertion so that we can query the $k$-th smallest value in an interval.

How do we preserve them? The straightforward brute-force approach is to create a new segment tree each time.  
But wouldn't that use too much memory?

## Explanation

On inspection, we find that each update changes the same number of nodes.  
(For example, the figure below updates the node for value 1 in $[1,8]$; the red nodes are the modified nodes.)  
![](./images/persistent-seg.png)

Only $O(\log{n})$ nodes change, forming a chain: the number of nodes changed by each update equals the tree's height.  
A chairman tree cannot use heap-style storage: we cannot represent the left and right children by $x\times 2$ and $x\times 2+1$. Instead, allocate nodes dynamically and store each node's left and right child indices.  
Thus, besides recording the children, we only need to save the root after inserting each number to achieve persistence.

Simplify the problem: each query asks for the $k$-th smallest value in $[1,r]$.  
How? Find the root version from inserting r, then use an ordinary segment tree over values (also called a key-based or value-domain segment tree).

With that understood, return to the original problem: finding the $k$-th smallest value in $[l,r]$.  
Connect this to another concept: **prefix sums**.  
They cleverly use interval subtraction to answer each query in $O(1)$ after preprocessing.

The information maintained by a chairman tree also has this property.  
Therefore, to obtain the information for $[l,r]$, simply subtract the information for $[1,l - 1]$ from that for $[1,r]$.

The problem is solved!

Now analyze the space usage: with dynamically allocated nodes, one segment tree contains only $2n-1$ nodes.  
There are then $n$ updates, each adding at most $\lceil\log_2{n}\rceil+1$ nodes. Thus, in the worst case, the total number of nodes after $n$ updates reaches $2n-1+n(\lceil\log_2{n}\rceil+1)$.
Here $n \leq 10^5$, so one update adds at most $\lceil\log_2{10^5}\rceil+1 = 18$ nodes. After $n$ updates, the total is $2\times 10^5-1+18\times 10^5$; ignoring $-1$, this is approximately $20\times 10^5$.

One final tip: do not be too stingy with memory (most problems have generous memory limits, so exceeding them is usually not a concern)! Allocate $2^5\times 10^5$, nearly twice the original estimate (that is, `n << 5`).

## Implementation

```cpp
#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;
constexpr int MAXN = 1e5;  // Input bounds
int tot, n, m;
int sum[(MAXN << 5) + 10], rt[MAXN + 10], ls[(MAXN << 5) + 10],
    rs[(MAXN << 5) + 10];
int a[MAXN + 10], ind[MAXN + 10], len;

int getid(const int &val) {  // Coordinate compression
  return lower_bound(ind + 1, ind + len + 1, val) - ind;
}

int build(int l, int r) {  // Build the tree
  int root = ++tot;
  if (l == r) return root;
  int mid = l + r >> 1;
  ls[root] = build(l, mid);
  rs[root] = build(mid + 1, r);
  return root;  // Return the root of this subtree
}

int update(int k, int l, int r, int root) {  // Insertion operation
  int dir = ++tot;
  ls[dir] = ls[root], rs[dir] = rs[root], sum[dir] = sum[root] + 1;
  if (l == r) return dir;
  int mid = l + r >> 1;
  if (k <= mid)
    ls[dir] = update(k, l, mid, ls[dir]);
  else
    rs[dir] = update(k, mid + 1, r, rs[dir]);
  return dir;
}

int query(int u, int v, int l, int r, int k) {  // Query operation
  int mid = l + r >> 1,
      x = sum[ls[v]] - sum[ls[u]];  // Use interval subtraction to obtain the number of values in the left child
  if (l == r) return l;
  if (k <= x)  // If k is at most x, the k-th smallest number is in the left child
    return query(ls[u], ls[v], l, mid, k);
  else  // Otherwise, it is in the right child
    return query(rs[u], rs[v], mid + 1, r, k - x);
}

void init() {
  scanf("%d%d", &n, &m);
  for (int i = 1; i <= n; ++i) scanf("%d", a + i);
  memcpy(ind, a, sizeof ind);
  sort(ind + 1, ind + n + 1);
  len = unique(ind + 1, ind + n + 1) - ind - 1;
  rt[0] = build(1, len);
  for (int i = 1; i <= n; ++i) rt[i] = update(getid(a[i]), 1, len, rt[i - 1]);
}

int l, r, k;

void work() {
  while (m--) {
    scanf("%d%d%d", &l, &r, &k);
    printf("%d\n", ind[query(rt[l - 1], rt[r], 1, len, k)]);  // Answer the query
  }
}

int main() {
  init();
  work();
  return 0;
}
```

## Extension: persistent DSU using a chairman tree

A chairman tree is a convenient way to implement a persistent DSU. An example implementation is provided here.

```cpp
--8<-- "docs/ds/code/persistent-seg/persistent-seg_1.cpp"
```

## References

<https://en.wikipedia.org/wiki/Persistent_data_structure>

<https://www.cnblogs.com/zinthos/p/3899565.html>
