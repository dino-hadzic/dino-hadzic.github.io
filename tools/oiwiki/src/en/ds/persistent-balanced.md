---
title: Persistent balanced tree
---

## Persistent non-rotating treap

### Prerequisites

The **persistent balanced tree commonly used in OI** is usually a **persistent non-rotating treap**, so first study the [**non-rotating treap**](./treap.md).

### Idea and approach

A non-rotating treap can be made persistent by copying the nodes visited during **Merge** and **Split** (usually during **Split**, to avoid affecting earlier versions).

For a rotating treap, in addition to the nodes on the path, copy the nodes affected by rotations (unless they have already been copied during the current operation). A rotation generally affects only two nodes, so this does not increase the time complexity.

This method is generally called path copying.

"All supported operations can be implemented using **Merge Split Newnode Build**." **Build** is only used for construction and need not be considered here, while **Newnode** (creating a new node) is the tool for achieving persistence.

Observe **Merge** and **Split**: both operate from the top down!

We can therefore make them persistent **in the same way as a persistent segment tree**.

### Making operations persistent

**Making a data structure persistent** means preserving historical information in the **data structure** so that earlier versions can be accessed later.

In a **persistent segment tree**, creating each new version copies **the path along which updates are made**.

For a persistent treap (the version currently common in Chinese OI), the process is as follows:

After copying node $X_{a}$ (version $a$ of node $X$) to create a new version $X_{a+1}$ (version $a+1$ of node $X$):

-   If a child node $Y$ does not need modification, let the pointer in $X_{a+1}$ point directly to $Y_{a}$ (version $a$ of node $Y$).
-   Otherwise, if $Y$ must change, **create** a new node $Y_{a+1}$ (version $a+1$ of node $Y$) when **recursing downward** to **store the new information**, and point $X_{a+1}$ to $Y_{a+1}$ (version $a+1$ of node $Y$).

### Persistent implementation

We need:

-   An array of `struct` objects storing the information for **each node** (usually called `tree`); of course, those writing a **pointer-based implementation** can omit this array.

-   A **root array** storing the *tree root* of each version. Each version query starts from **the node stored in the root array**.

-   `split()` for splitting: **split one tree into two trees**.

-   `merge()` for merging: **merge two trees according to their random priorities**.

-   `newNode()` to create a new node.

-   `build()` to build the tree.

#### Split

During **splitting**, **create new nodes** along each split path to point to the resulting paths. Store the roots of the two resulting trees in a `std::pair`.

`split(x,k)` returns a `std::pair`.

It places the first $k$ elements of the tree rooted at $_x$ into **one tree**, with the remaining nodes forming another tree, and returns their roots (first is the first tree's root and second is the second tree's root).

-   If the **left subtree** of $x$ has $key \geq k$, **recurse directly into the left subtree**, then merge the second tree produced by splitting it with the **right subtree** of the current $x$.
-   Otherwise, recurse into the **right subtree**.

```cpp
static std::pair<int, int> _split(int _x, int k) {
  if (_x == 0)
    return std::make_pair(0, 0);
  else {
    int _vs = ++_cnt;  // Create a new node (the key idea of persistence)
    _trp[_vs] = _trp[_x];
    std::pair<int, int> _y;
    if (_trp[_vs].key <= k) {
      _y = _split(_trp[_vs].leaf[1], k);
      _trp[_vs].leaf[1] = _y.first;
      _y.first = _vs;
    } else {
      _y = _split(_trp[_vs].leaf[0], k);
      _trp[_vs].leaf[0] = _y.second;
      _y.second = _vs;
    }
    _trp[_vs]._update();
    return _y;
  }
}
```

#### Merge

`merge(x,y)` returns the root of the merged tree.

This is also implemented recursively. If **x's random priority** > **y's random priority**, call `merge(x_{rc},y)`; otherwise, call `merge(x,y_{lc})`.

```cpp
static int _merge(int _x, int _y) {
  if (_x == 0 || _y == 0)
    return _x ^ _y;
  else {
    if (_trp[_x].fix < _trp[_y].fix) {
      _trp[_x].leaf[1] = _merge(_trp[_x].leaf[1], _y);
      _trp[_x]._update();
      return _x;
    } else {
      _trp[_y].leaf[0] = _merge(_x, _trp[_y].leaf[0]);
      _trp[_y]._update();
      return _y;
    }
  }
}
```

## Persistent WBLT

### Prerequisites

A persistent WBLT is a modification of WBLT, so first study [WBLT](./wblt.md).

### Idea and approach

Use **path copying**: copy the nodes **modified** during an operation without affecting the previous nodes.

### Handling lazy tags

To handle lazy tags, note that in a persistent WBLT a node can have multiple parents, but only $0$ or $2$ children. The pushdown operation propagates lazy tags and affects only the children. Performing pushdown on a node is not itself a problem; its children are the concern, because they may have other parents. Propagating a tag to a child can add a tag to another parent's version that does not belong there, which is incorrect unless the child has only one parent. Therefore, copy the children during pushdown and apply the tags to the new copies.

### Implementing path copying

For path copying, define a refresh function taking a reference to node $p$. It copies node $p$ into a new node and reassigns $p$. The rule is: refresh a node if it is about to be modified or if its children are about to change (rather than just the information in its children); otherwise, refreshing is unnecessary.

For read-only queries, refresh is unnecessary except during pushdown. If all operations perform path copying, the order of pushdown and refresh does not matter.

### A small optimization for persistent WBLT

Here is an optimization. Pushdown copies two nodes; permanent lazy tags are one possible approach. However, as noted above, children with only one parent do not need copying. We can exploit this property to reduce unnecessary node copies.

Record each node's number of parents as $use$ (treat the root of each version as having one parent). On each refresh, if $use\leq 1$, copying is unnecessary. Otherwise, create a new node and decrease $use$ by $1$, representing the parent moving to a copy of this child. The parent can then freely modify the new node without affecting other versions. Also, when copying a node with children, increase both children's $use$ by $1$; when merging two subtrees, the returned node also contributes a parent to its children's $use$; when deleting a node, both children lose one parent. This saves some time and space.

### Code implementation

??? note "Complete code (persistent sequence balanced tree)"
    ```cpp
    --8<-- "docs/ds/code/persistent-balanced/persistent-wblt.cpp"
    ```

## Example problem

???+ note "[Luogu P3835 [Template] Persistent Balanced Tree](https://www.luogu.com.cn/problem/P3835)"
    Implement a data structure supporting the following operations (initially, it contains no data):
    
    1.  Insert the number $x$.
    2.  Delete the number $x$ (if multiple copies exist, delete only one; if none exists, ignore the operation).
    3.  Query the rank of $x$ (the number of elements smaller than it + 1).
    4.  Query the number with rank $x$.
    5.  Find the predecessor of $x$ (the largest number less than $x$; if none exists, output $-2\,147\,483\,647$).
    6.  Find the successor of $x$ (the smallest number greater than $x$; if none exists, output $2\,147\,483\,647$).
    
    Every operation is based on a historical version and creates a new version (operations 3, 4, 5, and 6 leave the original state unchanged). Each version is numbered by the operation's index. In particular, the initial version is numbered 0.

This is the persistent version of the **Ordinary Balanced Tree** problem, with similar operations.

The only difference is the use of persistent merge and split operations.

## Recommended practice problems

1.  [Luogu P3919: Persistent Array (template problem)](https://www.luogu.com.cn/problem/P3919)

2.  [Codeforces 702F: T-shirt](http://codeforces.com/problemset/problem/702/F)

3.  [Luogu P5055: Persistent Sequence Balanced Tree](https://www.luogu.com.cn/problem/P5055)

4.  [Luogu P5350: Sequence](https://www.luogu.com.cn/problem/P5350)
