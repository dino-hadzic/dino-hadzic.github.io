---
title: Sqrt Tree
---

## Introduction

You are given a sequence of length n, ${\left\langle a_i\right\rangle}_{i=1}^n$, and an associative operation $\circ$ (for example, $\gcd,\min,\max,+,\operatorname{and},\operatorname{or},\operatorname{xor}$ are all associative); then for every range query $[l,r]$ we need to compute $a_l\circ a_{l+1}\circ\dotsb\circ a_{r}$.

A Sqrt Tree can be preprocessed in $O(n\log\log n)$ time and answers queries in $O(1)$ time.

## Explanation

### Splitting the sequence into blocks

First we split the whole sequence into $O(\sqrt{n})$ blocks, each of size $O(\sqrt{n})$. For every block we compute:

1.  $P_i$ – the prefix range queries inside the block
2.  $S_i$ – the suffix range queries inside the block
3.  an additional array $\left\langle B_{i,j}\right\rangle$ holding the answer for the range from the $i$-th block to the $j$-th block.

For example, suppose $\circ$ is the addition $+$ and the sequence is $\{1,2,3,4,5,6,7,8,9\}$.

First we split the sequence into three blocks, obtaining $\{1,2,3\},\{4,5,6\},\{7,8,9\}$.

Then the prefix and suffix range answers of each block are

$$
\begin{aligned}
&P_1=\{1,3,6\},S_1=\{6,5,3\}\\
&P_2=\{4,9,15\},S_2=\{15,11,6\}\\
&P_3=\{7,15,24\},S_3=\{24,17,9\}\\
\end{aligned}
$$

The array $B$ is:

$$
B=\begin{bmatrix}
6 & 21 & 45\\
0 & 15 & 39\\
0 & 0 & 24\\
\end{bmatrix}
$$

(For the invalid cases $i>j$ we assume the answer is 0.)

Clearly we can precompute these values in $O(n)$ time, and the space complexity is $O(n)$ as well. Once they are ready, we can use them to answer queries that span several blocks in $O(1)$ time. But we still cannot handle queries whose whole range lies inside a single block, so we need to prepare something more.

### Building a tree

It is natural to build the structure above recursively inside every block to support queries inside a block. For blocks of size $1$ we can answer queries in $O(1)$. This way we build a tree in which every node represents a range of the sequence. The ranges of the leaves have length $1$ or $2$. A node of size $k$ has $O(\sqrt{k})$ children, so the height of the whole tree is $O(\log\log n)$, and the total length of the ranges on each level is $O(n)$; therefore the complexity of building this tree is $O(n\log\log n)$.

??? note "Proof of the tree height"
    By definition, let $T(n)$ be the height of the subtree of a node that "controls" $n$ elements; we can write the recurrence:
    
    $$
    T(n)=T(\sqrt n)+1
    $$
    
    Substituting $n=2^m$ gives
    
    $$
    T(2^m)=T(2^{\frac m2})+1
    $$
    
    Defining further $S(m)=T(2^m)$ and substituting, we have
    
    $$
    S(m)=S(\dfrac m2)+1
    $$
    
    By the master theorem, $S(m)=O(\log m)$, hence $T(n)=S(\log n)=O(\log\log n)$.

Now we can answer queries in $O(\log\log n)$ time. For a query $[l,r]$ we only need to quickly find the node $u$ with the smallest range that contains $[l,r]$; then $[l,r]$ necessarily spans several blocks in the block partition of $u$, so the answer can be computed in $O(1)$. The overall complexity of one query is $O(\log\log n)$, because the tree height is $O(\log\log n)$. We can still optimize this process, though.

### Optimizing the query complexity

It is natural to binary search over the height, with an $O(1)$ validity check. This makes the complexity $O(\log\log\log n)$. But we can speed this process up even further.

Let us assume that

1.  the size of every block is an integer power of $2$;
2.  the block sizes on the same level are equal.

To this end we need to append some $0$ elements at the end of the sequence so that its length becomes an integer power of $2$. Although some blocks may become twice as large as before, this is still $O(\sqrt{k})$, so the complexity of preprocessing the blocks remains $O(n)$.

Now we can easily determine whether a query range is entirely contained in one block. For a range $[l,r]$ (0-indexed), write the endpoints in binary. As an example, for $k=4, l=39, r=46$ the binary representation is

$$
l = 39_{10} = 100111_2,
r = 46_{10} = 101110_2
$$

We know that the range lengths on one level are equal, and so are the block sizes (in the example above $2^k=2^4=16$). These blocks completely cover the whole sequence, so the first block represents the elements $[0,15]$ (in binary $[000000_2,001111_2]$), the second block represents the element range $[16,31]$ (in binary $[010000_2,011111_2]$), and so on. We notice that the positions of elements in the same block differ only in the last $k$ bits of their binary representation (in the example above $k=4$). The $l,r$ of the example also differ only in the last $k$ bits, so they are in the same block.

Therefore we need to check whether the two endpoints of the range differ only in the last $k$ bits, i.e. $l\oplus r\le 2^k-1$. Thus we can quickly find the level on which the answer range lies:

1.  for every $i\in [1,n]$ we find the highest $1$ bit of $i$;
2.  now for a query $[l,r]$ we compute the highest bit of $l\oplus r$, which quickly determines the level on which the answer range lies.

This way we can answer queries in $O(1)$ time.

## Updating elements

We can update elements in a Sqrt Tree; both point updates and range updates are supported.

### Point update

Consider a point assignment $a_x=val$; we want to update the information for this operation efficiently.

#### Naive implementation

First let us see what a Sqrt Tree looks like after one point update.

Consider a node of length $l$ and the corresponding sequences: $\left\langle P_i\right\rangle,\left\langle S_i\right\rangle,\left\langle B_{i,j}\right\rangle$. It is easy to see that only $O(\sqrt{l})$ elements change in $\left\langle P_i\right\rangle$ and $\left\langle S_i \right\rangle$. In $\left\langle B_{i,j}\right\rangle$, however, $O(l)$ elements change. So $O(l)$ elements are updated in the tree node. Therefore the complexity of a point update in a Sqrt Tree is $O(n+\sqrt{n}+\sqrt{\sqrt{n}}+\dotsb)=O(n)$.

#### Replacing the B array with a Sqrt Tree

Note that the bottleneck of a point update is updating the root's $\left\langle B_{i,j}\right\rangle$. So we try to replace the root's $\left\langle B_{i,j}\right\rangle$ with another Sqrt Tree, which we call $index$. Its role is the same as that of the original two-dimensional array: it maintains the answers for queries over whole blocks. The other non-root nodes still use $\left\langle B_{i,j}\right\rangle$. Note: if the root of a Sqrt Tree has an $index$ structure, we say the Sqrt Tree **has an index**; if the root of a Sqrt Tree has a $\left\langle B_{i,j}\right\rangle$ structure, we say it **has no index**. The $index$ tree itself has no index.

So we can update the $index$ tree like this:

1.  Update $\left\langle P_i\right\rangle$ and $\left\langle S_i\right\rangle$ in $O(\sqrt{n})$ time.
2.  Update $index$; its length is $O(n)$, but we only need to update one of its elements (the one representing the changed block); the time complexity of this step is $O(\sqrt{n})$ (using the naive algorithm).
3.  Enter the child where the change occurred and update its information with the naive algorithm in $O(\sqrt{n})$ time.

Note that the query complexity is still $O(1)$, because we use the $index$ tree at most once. So the complexity of a point update is $O(\sqrt{n})$.

### Updating a range

A Sqrt Tree also supports the range assignment operation $\operatorname{Update}(l,r,x)$, which sets all numbers in the range $[l,r]$ to $x$. We have two implementations for this: one spends $O(\sqrt{n}\log\log n)$ to update the information and $O(1)$ to query; the other updates in $O(\sqrt{n})$, but the query time grows to $O(\log\log n)$.

We can put lazy tags on a Sqrt Tree just like on a segment tree. But there is one difference on a Sqrt Tree. Since pushing down the lazy tag of one node can cost $O(\sqrt{n})$, we do not push tags down during a query; instead we check whether the parent has a tag and, if so, push it down.

#### First implementation

In the first implementation we only put lazy tags on nodes of level $1$ (nodes whose range length is $O(\sqrt{n})$), and when pushing a tag down we directly update the whole subtree, with complexity $O(\sqrt{n}\log\log n)$. The procedure is as follows:

1.  Consider the nodes on level $1$; for those entirely contained in the updated range, put a lazy tag on them;

2.  Two blocks are only partially covered; we directly **rebuild** these two blocks in $O(\sqrt{n}\log\log n)$ time. If a block carries a lazy tag from a previous update, push the tag down while rebuilding;

3.  Update the root's $\left\langle P_i\right\rangle$ and $\left\langle S_i\right\rangle$, time complexity $O(\sqrt{n})$;

4.  Rebuild the $index$ tree, time complexity $O(\sqrt{n}\log\log n)$.

Now we can perform range updates efficiently. So how do we answer queries using the lazy tags? The procedure is as follows:

1.  If our query is contained in a block with a lazy tag, we can compute the answer using the lazy tag;

2.  If our query spans several blocks, we only need to care about the answers of the leftmost and rightmost incomplete blocks. The answer for the blocks in the middle can be queried in the $index$ tree (because the $index$ tree is rebuilt after every update), with complexity $O(1)$.

So the query complexity is still $O(1)$.

#### Second implementation

In this implementation every node can carry a lazy tag. Therefore, when processing a query, we have to take the lazy tags of the ancestors into account, so the query complexity becomes $O(\log\log n)$. However, updating the information becomes faster. The operations are as follows:

1.  For the blocks entirely contained in the updated range, add the lazy tag to these blocks, complexity $O(\sqrt{n})$;
2.  For the blocks partially covered by the updated range, update $\left\langle P_i\right\rangle$ and $\left\langle S_i\right\rangle$, complexity $O(\sqrt{n})$ (because only two blocks are modified);
3.  Update the $index$ tree, complexity $O(\sqrt{n})$ (using the same update algorithm);
4.  For the subtrees without an index, update their $\left\langle B_{i,j}\right\rangle$;
5.  Recursively update the two ranges that are not entirely covered.

The time complexity is $O(\sqrt{n}+\sqrt{\sqrt{n}}+\dotsb)=O(\sqrt{n})$.

## Implementation

The implementation below builds the tree in $O(n\log\log n)$ time, answers queries in $O(1)$ time and performs point updates in $O(\sqrt{n})$ time.

```cpp
SqrtTreeItem op(const SqrtTreeItem &a, const SqrtTreeItem &b);

int log2Up(int n) {
  int res = 0;
  while ((1 << res) < n) {
    res++;
  }
  return res;
}

class SqrtTree {
 private:
  int n, lg, indexSz;
  vector<SqrtTreeItem> v;
  vector<int> clz, layers, onLayer;
  vector<vector<SqrtTreeItem>> pref, suf, between;

  void buildBlock(int layer, int l, int r) {
    pref[layer][l] = v[l];
    for (int i = l + 1; i < r; i++) {
      pref[layer][i] = op(pref[layer][i - 1], v[i]);
    }
    suf[layer][r - 1] = v[r - 1];
    for (int i = r - 2; i >= l; i--) {
      suf[layer][i] = op(v[i], suf[layer][i + 1]);
    }
  }

  void buildBetween(int layer, int lBound, int rBound, int betweenOffs) {
    int bSzLog = (layers[layer] + 1) >> 1;
    int bCntLog = layers[layer] >> 1;
    int bSz = 1 << bSzLog;
    int bCnt = (rBound - lBound + bSz - 1) >> bSzLog;
    for (int i = 0; i < bCnt; i++) {
      SqrtTreeItem ans;
      for (int j = i; j < bCnt; j++) {
        SqrtTreeItem add = suf[layer][lBound + (j << bSzLog)];
        ans = (i == j) ? add : op(ans, add);
        between[layer - 1][betweenOffs + lBound + (i << bCntLog) + j] = ans;
      }
    }
  }

  void buildBetweenZero() {
    int bSzLog = (lg + 1) >> 1;
    for (int i = 0; i < indexSz; i++) {
      v[n + i] = suf[0][i << bSzLog];
    }
    build(1, n, n + indexSz, (1 << lg) - n);
  }

  void updateBetweenZero(int bid) {
    int bSzLog = (lg + 1) >> 1;
    v[n + bid] = suf[0][bid << bSzLog];
    update(1, n, n + indexSz, (1 << lg) - n, n + bid);
  }

  void build(int layer, int lBound, int rBound, int betweenOffs) {
    if (layer >= (int)layers.size()) {
      return;
    }
    int bSz = 1 << ((layers[layer] + 1) >> 1);
    for (int l = lBound; l < rBound; l += bSz) {
      int r = min(l + bSz, rBound);
      buildBlock(layer, l, r);
      build(layer + 1, l, r, betweenOffs);
    }
    if (layer == 0) {
      buildBetweenZero();
    } else {
      buildBetween(layer, lBound, rBound, betweenOffs);
    }
  }

  void update(int layer, int lBound, int rBound, int betweenOffs, int x) {
    if (layer >= (int)layers.size()) {
      return;
    }
    int bSzLog = (layers[layer] + 1) >> 1;
    int bSz = 1 << bSzLog;
    int blockIdx = (x - lBound) >> bSzLog;
    int l = lBound + (blockIdx << bSzLog);
    int r = min(l + bSz, rBound);
    buildBlock(layer, l, r);
    if (layer == 0) {
      updateBetweenZero(blockIdx);
    } else {
      buildBetween(layer, lBound, rBound, betweenOffs);
    }
    update(layer + 1, l, r, betweenOffs, x);
  }

  SqrtTreeItem query(int l, int r, int betweenOffs, int base) {
    if (l == r) {
      return v[l];
    }
    if (l + 1 == r) {
      return op(v[l], v[r]);
    }
    int layer = onLayer[clz[(l - base) ^ (r - base)]];
    int bSzLog = (layers[layer] + 1) >> 1;
    int bCntLog = layers[layer] >> 1;
    int lBound = (((l - base) >> layers[layer]) << layers[layer]) + base;
    int lBlock = ((l - lBound) >> bSzLog) + 1;
    int rBlock = ((r - lBound) >> bSzLog) - 1;
    SqrtTreeItem ans = suf[layer][l];
    if (lBlock <= rBlock) {
      SqrtTreeItem add =
          (layer == 0) ? (query(n + lBlock, n + rBlock, (1 << lg) - n, n))
                       : (between[layer - 1][betweenOffs + lBound +
                                             (lBlock << bCntLog) + rBlock]);
      ans = op(ans, add);
    }
    ans = op(ans, pref[layer][r]);
    return ans;
  }

 public:
  SqrtTreeItem query(int l, int r) { return query(l, r, 0, 0); }

  void update(int x, const SqrtTreeItem &item) {
    v[x] = item;
    update(0, 0, n, 0, x);
  }

  SqrtTree(const vector<SqrtTreeItem> &a)
      : n((int)a.size()), lg(log2Up(n)), v(a), clz(1 << lg), onLayer(lg + 1) {
    clz[0] = 0;
    for (int i = 1; i < (int)clz.size(); i++) {
      clz[i] = clz[i >> 1] + 1;
    }
    int tlg = lg;
    while (tlg > 1) {
      onLayer[tlg] = (int)layers.size();
      layers.push_back(tlg);
      tlg = (tlg + 1) >> 1;
    }
    for (int i = lg - 1; i >= 0; i--) {
      onLayer[i] = max(onLayer[i], onLayer[i + 1]);
    }
    int betweenLayers = max(0, (int)layers.size() - 1);
    int bSzLog = (lg + 1) >> 1;
    int bSz = 1 << bSzLog;
    indexSz = (n + bSz - 1) >> bSzLog;
    v.resize(n + indexSz);
    pref.assign(layers.size(), vector<SqrtTreeItem>(n + indexSz));
    suf.assign(layers.size(), vector<SqrtTreeItem>(n + indexSz));
    between.assign(betweenLayers, vector<SqrtTreeItem>((1 << lg) + bSz));
    build(0, 0, n, 0);
  }
};
```

## Exercises

[CodeChef - SEGPROD](https://www.codechef.com/NOV17/problems/SEGPROD)

**This page is mainly translated from [Sqrt Tree - Algorithms for Competitive Programming](https://cp-algorithms.com/data_structures/sqrt-tree.html), licensed under CC-BY-SA 4.0.**
