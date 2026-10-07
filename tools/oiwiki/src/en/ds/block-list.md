---
title: Unrolled linked list
---

![./images/kuaizhuanglianbiao.png](./images/kuaizhuanglianbiao.png "./images/kuaizhuanglianbiao.png")

An unrolled linked list (block linked list) looks roughly like this…

It is easy to see that an unrolled linked list is just a linked list in which every node points to an array.
We split the original array of length n into $\sqrt{n}$ nodes, and the array belonging to each node has size $\sqrt{n}$.
So we define the structure as follows; the code is below.
Here `sqn` stands for `sqrt(n)`, i.e. $\sqrt{n}$, and `pb` stands for `push_back`, i.e. appending one element to this `node`.

???+ note "Implementation"
    ```cpp
    struct node {
      node* nxt;
      int size;
      char d[(sqn << 1) + 5];
    
      node() { size = 0, nxt = NULL, memset(d, 0, sizeof(d)); }
    
      void pb(char c) { d[size++] = c; }
    };
    ```

An unrolled linked list should support at least: splitting, insertion and lookup.
What is splitting? Splitting means splitting one `node` into two smaller `node`s so that the size of every `node` stays close to $\sqrt{n}$ (otherwise the structure may degenerate into a plain array). A split is performed when the size of a `node` exceeds $2\times \sqrt{n}$.

How is a split done? First create a new node, then `copy` the last $\sqrt{n}$ values of the node being split into the new node, then delete those last $\sqrt{n}$ values from the node being split (`size--`), and finally insert the new node right after the node that was split.

Every operation of an unrolled linked list has complexity $\sqrt{n}$.

One more thing needs to be said.
As elements are inserted (or deleted), $n$ changes, and so does $\sqrt{n}$. Then the block size changes too – do we really have to maintain the block size every time?

Actually no: just set $\sqrt{n}$ to a fixed value. For example, if the limit given in the problem is $10^6$, set $\sqrt{n}$ to the constant $10^3$ and never change it.

```cpp
list<vector<char>> orz_list;
```

## `rope` in libstdc++

### Introduction

`rope` in libstdc++ also plays the role of an unrolled linked list; it is implemented with a persistent balanced tree and supports random access as well as inserting and deleting elements.

Since `rope` is not really implemented as an unrolled linked list, its time complexity is not the same as that of an unrolled linked list but corresponds to the complexity of a persistent balanced tree (i.e. $O(\log n)$).

It can be included as follows:

```cpp
#include <ext/rope>
using namespace __gnu_cxx;
```

???+ warning "About library functions starting with a double underscore"
    In OI it was long unclear whether library functions starting with a double underscore may be used; the [Supplementary notes on programming language restrictions in NOI series events](https://www.noi.cn/xw/2021-09-01/735729.shtml) published by CCF in 2021 state that "library functions and macros starting with an underscore are allowed, except for those library functions and macros that perform explicitly forbidden operations." So `rope` can currently be used in OI without problems.

### Basic operations

|          Operation          |                            Effect                            |
| :-------------------------: | :----------------------------------------------------------: |
|        `rope<int> a`        | initializes a `rope` (very similar to containers like `vector`) |
|       `a.push_back(x)`      |              appends the element `x` to the end of `a`           |
|      `a.insert(pos, x)`     |            inserts the element `x` at position `pos` of `a`      |
|      `a.erase(pos, x)`      |         deletes `x` elements starting at position `pos` of `a`   |
|     `a.at(x)` or `a[x]`     |                 accesses the `x`-th element of `a`               |
| `a.length()` or `a.size()`  |                      returns the size of `a`                     |

## Example problem

[POJ2887 Big String](http://poj.org/problem?id=2887)

Solution:
A very simple template problem. The code is as follows:

```cpp
--8<-- "docs/ds/code/block-list/block-list_1.cpp"
```
