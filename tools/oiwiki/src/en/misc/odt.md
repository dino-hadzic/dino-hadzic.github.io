---
title: Chtholly tree / amortized color segments
---

## Introduction

The Chtholly tree, also known as the Old Driver Tree (ODT), originates from [CF896C](https://codeforces.com/problemset/problem/896/C).

The name refers to the technique of "maintaining color segments in an amortized way using a balanced tree (`std::set`, `std::map`, etc.) or a linked list (`std::list`, a hand-written linked list, etc.)", not to a specific data structure. Its core idea is to merge a segment of equal values into a single node and process it as a whole. Compared with traditional data structures such as the segment tree, for problems with range-assignment operations the Chtholly tree can maintain the value of every assigned segment much more conveniently.

## Implementation (std::set)

### Node type

```cpp
struct Node_t {
  int l, r;
  mutable int v;

  Node_t(const int &il, const int &ir, const int &iv) : l(il), r(ir), v(iv) {}

  bool operator<(const Node_t &o) const { return l < o.l; }
};
```

Here `int v` is the additional data that you specify yourself.

???+ note "What does the `mutable` keyword mean?"
    `mutable` means "changeable"; it lets us modify the value of `v` in later operations. In C++, `mutable` exists to break through the restrictions of `const`. A variable marked `mutable` (`mutable` can only be applied to non-static data members of a class) is always in a modifiable state, even inside a `const` function.
    
    This means that we can directly modify the `v` value of an element already inserted into the `set`, without taking the element out and re-inserting it into the `set`.

### Node storage

We want to maintain all nodes so that the left endpoints of the intervals they represent increase monotonically and the intervals are pairwise disjoint; ideally we can guarantee that the union of all intervals is one maximal contiguous range. Here we take `std::set` as an example and maintain all nodes in a `set<Node_t> odt;`.

During initialization, insert one very long interval into the Chtholly tree (e.g. if the problem asks to maintain information for positions $1$ to $n$, insert the interval $[1,n+1]$).

### The split operation

The `split` operation is the core of the Chtholly tree. It takes a position $x$, splits the interval that originally contains the point $x$ (call it $[l, r]$) into two intervals $[l, x)$ and $[x, r]$, and returns an iterator to the latter.

Reference code:

```cpp
auto split(int x) {
  auto it = odt.lower_bound(Node_t(x, 0, 0));
  if (it != odt.end() && it->l == x) return it;
  --it;
  int l = it->l, r = it->r, v = it->v;
  odt.erase(it);
  odt.insert(Node_t(l, x - 1, v));
  return odt.insert(Node_t(x, r, v)).first;
}
```

On compilers that do not support return type deduction with `auto`, the return type of the function can be changed to `set<Node_t>::iterator`.

### The assign operation

Another important operation is `assign`. It assigns a value to a whole interval. Suppose the interval $[l,r]$ is to be assigned the value $v$.

First, cut out the interval $[l, r]$. Call `split(r + 1), split(l)` in this order and denote the iterators they return by $itr, itl$; then the iterator range $[itl, itr)$ points to all intervals of the Chtholly tree contained in $[l,r]$.

Next, delete the old information. `std::set` has a member function `erase` with the signature `iterator erase( const_iterator first, const_iterator last );`, which removes the elements in the range `[first; last)`. So we call `odt.erase(itl, itr);` to delete the old information.

Finally, insert the new value of the interval $[l,r]$. It suffices to call `odt.insert(Node_t(l, r, v))`.

Reference code:

```cpp
void assign(int l, int r, int v) {
  auto itr = split(r + 1), itl = split(l);
  odt.erase(itl, itr);
  odt.insert(Node_t(l, r, v));
}
```

???+ note "Why `split(r + 1)` first and then `split(l)`?"
    1.  `std::set::erase` invalidates references and iterators to the erased elements. Other references and iterators are not affected.
    2.  `std::set::insert` does not invalidate any iterators or references.
    3.  The `split` operation splits an interval. After calling `split(r + 1)`, $r + 1$ becomes the left endpoint of the right one of the two new intervals; when we then split the left interval, we will certainly not touch the interval whose left endpoint is $r + 1$, so we will not split it, nor delete the interval with left endpoint $r + 1$ and invalidate the iterator. Conversely, calling `split(l)` first and then `split(r + 1)` may delete the interval whose left endpoint is $l$ and invalidate the iterator.

### The perform operation

Extract a range of the Chtholly tree and operate on it. Similar to the `assign` operation, except that deleting the intervals is replaced by iterating over them.

Reference code:

```cpp
void perform(int l, int r) {
  auto itr = split(r + 1), itl = split(l);
  for (; itl != itr; ++itl) {
    // Perform Operations here
  }
}
```

Note that such extraction must not be abused, as it may make the time complexity wrong. See the section "Complexity analysis" below.

## Implementation (std::map)

Compared with the `std::set` implementation, the `split` operation of the `std::map` implementation is simpler to write. Apart from that, the other operations are no different from the `std::set` ones.

### Node storage

Since the intervals stored in a Chtholly tree are contiguous, we do not necessarily need to record the right endpoints. We can store all intervals in a `map<int, int> mp;`, whose keys maintain the left endpoints and whose values maintain the value from that left endpoint up to just before the next left endpoint.

During initialization, if the problem asks to maintain information for positions $1$ to $n$, call `mp[1] = -1, mp[n + 1] = -1`, which sets all of $[1,n+1)$, i.e. $[1, n]$, to the special value $-1$; the interval $[n+1, +\infty)$ serves as a sentinel, and it may also be initialized.

### The split operation

Reference code (first version):

```cpp
void split(int x) {
  auto it = prev(mp.upper_bound(x));  // find the interval whose left endpoint is at most x.
  mp[x] = it->second;  // create the new interval and copy the value stored in the previous interval into it.
}
```

Reference code (second version):

```cpp
auto split(int pos) {
  auto it = prev(mp.upper_bound(pos));  // find the interval whose left endpoint is at most x.
  return mp.insert(it, make_pair(pos, it->second));
  // create the new interval and copy the value stored in the previous interval into it.
}
```

Here the overload `iterator insert( const_iterator pos, const value_type& value );` of `std::map::insert` is used; it inserts `value` as close as possible to the position just before `pos`. If the insertion happens exactly at the position just before `pos`, the complexity is amortized constant; otherwise it is logarithmic in the size of the container.

### The assign operation

For the `assign` operation, we need to delete the left endpoints of all intervals inside $[l,r−1]$ and then create a new interval.

```cpp
void assign(int l, int r, int v) {  // note: here r is the right endpoint of the interval + 1
  split(l);
  split(r);
  auto it = mp.find(l);
  while (it->first != r) {
    it = mp.erase(it);
  }
  mp[l] = v;
}
```

### The perform operation

```cpp
void perform(int l, int r) {  // note: here r is the right endpoint of the interval + 1
  split(l);
  split(r);
  auto it = mp.find(l);
  while (it->first != r) {
    // Perform Operations here
    it = next(it);
  }
}
```

## Implementation (linked list)

The mainstream implementation currently maintains the nodes with a `set`, but since the average number of maintained intervals is very small, the advantage of `set` is not significant. In contrast, a linked list (or an array) can maintain the split and merge operations more concisely.

### Node storage

```cpp
using i64 = int64_t;

struct Block {
  Block *next;  // next node of the linked list
  int l, r;     // range of the interval
  i64 val;      // value on the interval

  Block(Block *next, int l, int r, i64 val)
      : next(next), l(l), r(r), val(val) {}

  bool operator<(const Block &b) const { return val < b.val; }
} *root;
```

### The split operation

```cpp
// returns the interval whose left endpoint is mid+1
Block *split(int mid) {
  for (Block *b = root; b; b = b->next) {  // traverse the linked list
    if (b->l == mid + 1) {                 // left endpoint is mid+1
      return b;
    }
    // find the interval [l, r] containing both mid and mid+1 and split it into [l, mid] and [mid+1,
    // r]
    if (b->l <= mid && mid + 1 <= b->r) {
      b->next = new Block(b->next, mid + 1, b->r, b->val);
      b->r = mid;
      return b->next;
    }
  }
  return nullptr;  // not found, return null
}
```

When operating on intervals, since we cannot maintain only a part of an interval, the intervals must be split in advance before each of the operations below, and only then is the corresponding operation carried out.

```cpp
Block *lb, *rb;

// pre-split, guarantees that subsequent operations stay inside [l, r]
void prepare(int l, int r) {
  lb = split(l - 1);
  rb = split(r);
}
```

### The assign operation

```cpp
void assign(int l, int r, i64 val) {
  prepare(l, r);
  lb->r = r;  // change the interval [lb.l, lb.r] into [lb.l, r]
  lb->val = val;
  lb->next = rb;  // link [lb.l, r] to the adjacent interval on its right
}

// note: the memory of the deleted nodes is not freed here; add it yourself if needed
```

### The perform operation

```cpp
void perform(int l, int r) {
  prepare(l, r);
  for (Block *b = lb; b != rb; b = b->next) {
    // Perform Operations here
  }
}
```

## Complexity analysis

### Calling assign on the same interval immediately after perform

In this case we observe that two `split` operations add at most two intervals; one `assign` deletes all intervals in the range and adds one interval, while traversing the deleted intervals. Therefore, the number of intervals we traverse is linear in the number of deleted intervals, and each operation adds only $O(1)$ intervals, so the number of intervals we operate on is linear in the number of operations (including initialization); the time complexity is amortized $O(m\log n)$, where $m$ is the number of operations and $n$ is the maximum number of intervals in the Chtholly tree (we may assume $n\leq m$).

### No assign after perform

If specially constructed data is allowed, this can certainly be broken: it suffices to have enough distinct intervals in the Chtholly tree and traverse them repeatedly to push the complexity of the Chtholly tree to quadratic or even higher.

To guarantee the correct complexity, the data must be random. See the [proof of the complexity of the Chtholly tree on Codeforces](http://codeforces.com/blog/entry/56135?#comment-398940) for details. A more detailed rigorous proof can be found in [珂朵莉树的复杂度分析 (Complexity analysis of the Chtholly tree)](https://zhuanlan.zhihu.com/p/102786071). The conclusion of the proof is that the complexity of a Chtholly tree implemented with `std::set` is $O(n \log \log n)$, while that of a linked-list implementation is $O(n \log n)$.

## Exercises

-   [「Luogu 1840」Color the Axis](https://www.luogu.com.cn/problem/P1840)
-   ~~[「SCOI2010」序列操作 (Sequence operations)](https://www.luogu.com.cn/problem/P2572)~~ (hack data has been added to the source of this problem)
-   [「SHOI2015」脑洞治疗仪 (Brain hole treatment device)](https://loj.ac/problem/2037)
-   [「Luogu 4979」矿洞：坍塌 (Mine: collapse)](https://www.luogu.com.cn/problem/P4979)
-   [「Luogu 8146」risrqnis](https://www.luogu.com.cn/problem/P8146)

## Further reading

[ODT 的映射思想的推广 (Generalizing the mapping idea of ODT) - Luogu articles (luogu.com.cn)](https://www.luogu.com.cn/article/0mys9qkh)

## References and notes

-   [Problem - 896C - Codeforces](https://codeforces.com/problemset/problem/896/C) (origin of the Chtholly tree)
-   [CF896C Willem, Chtholly and Seniorious 题解 (editorial) - Luogu articles (luogu.com.cn)](https://www.luogu.com.cn/article/gyxbe23s) (reference for the `std::set` implementation)
-   [珂朵莉树的 map 实现 (map implementation of the Chtholly tree) - Zhihu (zhihu.com)](https://zhuanlan.zhihu.com/p/469794466) (reference for the `std::map` implementation)
-   [题解 CF896C【Willem, Chtholly and Seniorious】(editorial of CF896C) - Luogu articles (luogu.com.cn)](https://www.luogu.com.cn/article/umiw1fwp) (reference for the linked-list implementation)
-   [Codeforces Round #449 Editorial - Codeforces](https://codeforces.com/blog/entry/56135?#comment-398940) (on the proof of the complexity of the Chtholly tree)
-   [珂朵莉树的复杂度分析 (Complexity analysis of the Chtholly tree) - Zhihu (zhihu.com)](https://zhuanlan.zhihu.com/p/102786071) (complexity analysis of the Chtholly tree)
