---
title: Fenwick tree
---

## Introduction

The Fenwick tree (binary indexed tree, BIT) is a data structure with very little code that supports **point updates** and **range queries**.

??? note "What are 'point update' and 'range query'?"
    Imagine the following problem:
    
    Given an array $a$, perform the following two operations:
    
    -   given $x, y$, add $y$ to $a[x]$;
    -   given $l, r$, compute the sum of $a[l \ldots r]$.
    
    The first operation is a "point update", the second a "range query".
    
    Similarly, there are also "range update" and "point query". One example of each:
    
    -   range update: given $l, r, x$, add $x$ to every number in $a[l \ldots r]$;
    -   point query: given $x$, compute the value of $a[x]$.
    
    Note that range problems are in general strictly harder than point problems, because a point operation is the same as a range operation on a range of length $1$.

The information and operation maintained by an ordinary Fenwick tree must be **associative** and **invertible** (it must be possible to "subtract"), e.g. addition (sum), multiplication (product), XOR, etc.

-   Associativity: $(x \circ y) \circ z = x \circ (y \circ z)$, where $\circ$ is a binary operation.
-   Invertibility: the operation has an inverse operation, i.e. given $x \circ y$ and $x$, one can compute $y$.

Note:

-   for modular multiplication to be invertible, every number must have an inverse (which certainly holds when the modulus is prime);
-   information such as $\gcd$ and $\max$ is not invertible, so it cannot be handled by an ordinary Fenwick tree, but:
    -   range extrema can be handled with two Fenwick trees, see [Efficient Range Minimum Queries using Binary Indexed Trees](http://history.ioinformatics.org/oi/files/volume9.pdf#page=41);
    -   this page also introduces an extended Fenwick tree with $\Theta(\log^2n)$ complexity that supports queries over non-invertible information.

In fact, the problems a Fenwick tree can solve are a subset of the problems a segment tree can solve: whatever a Fenwick tree can do, a segment tree can certainly do; whatever a segment tree can do, a Fenwick tree may not be able to do. However, the code of a Fenwick tree is much shorter than that of a segment tree, and its running-time constant is smaller, so it is still worth learning.

Sometimes, with the help of difference arrays and auxiliary arrays, the Fenwick tree can also solve the stronger problems of **range add with point query** and **range add with range sum**.

## Fenwick tree

### First impressions

First an example: we want to know the prefix sum $a[1 \ldots 7]$. How?

One way: $a_1 + a_2 + a_3 + a_4 + a_5 + a_6 + a_7$, i.e. we add $7$ numbers.

But what if we already know three numbers $A$, $B$, $C$, where $A$ is the sum of $a[1 \ldots 4]$, $B$ is the sum of $a[5 \ldots 6]$, and $C$ is the sum of $a[7 \ldots 7]$ (i.e. $a[7]$ itself)? How would you compute it then? Surely you would answer: $A + B + C$, i.e. we add only $3$ numbers.

This is exactly why a Fenwick tree computes information quickly: a prefix $[1, n]$ can always be split into **at most $\boldsymbol{\log n}$ ranges** whose information is **already known**.

Then we only merge the information of these $\log n$ ranges and obtain the answer. Compared to merging $n$ pieces of information directly, the efficiency is much higher.

It is easy to see that the information must be associative, otherwise we could not merge it like this.

The following figure shows how a Fenwick tree works:

![](./images/fenwick.svg)

The bottom eight squares represent the original data array $a$. The irregularly arranged squares above them (the same array as the top eight squares) represent the "superior" array of $a$ – the array $c$.

The array $c$ stores the sum of some range of the original array $a$; in other words, the information of these ranges is known, and our goal is to split the queried prefix into these small ranges.

For example, from the figure:

-   $c_2$ covers $a[1 \ldots 2]$;
-   $c_4$ covers $a[1 \ldots 4]$;
-   $c_6$ covers $a[5 \ldots 6]$;
-   $c_8$ covers $a[1 \ldots 8]$;
-   the remaining $c[x]$ cover only $a[x]$ itself (which can be viewed as a small range $a[x \ldots x]$ of length $1$).

It is easy to notice that $c[x]$ always covers the total information of some range whose right endpoint is $x$. We do not consider the left endpoint for now; let us first get a feeling for how a Fenwick tree answers a query.

Example: compute the sum of $a[1 \ldots 7]$.

Procedure: we start at $c_{7}$ and jump backwards; we see that $c_{7}$ covers only the element $a_{7}$. Then we look at $c_{6}$; we see that $c_{6}$ covers $a[5 \ldots 6]$. Then we jump to $c_{4}$; we see that $c_{4}$ covers the elements $a[1 \ldots 4]$. Then we try to jump to $c_0$, but $c_0$ does not actually exist, so we stop.

We have just found $c_7, c_6, c_4$; these are exactly the three small ranges into which $a[1 \ldots 7]$ is split, and merging them gives the answer $c_7 + c_6 + c_4$.

Example: compute the sum of $a[4 \ldots 7]$.

Again we start at $c_7$, jump to $c_6$ and then to $c_4$. Now we see that it covers the sum of $a[1 \ldots 4]$, but we do not want the part $a[1 \ldots 3]$ – what now? Very simple: we just subtract the sum of $a[1 \ldots 3]$.

So why not, right at the beginning, turn the query for the sum of $a[4 \ldots 7]$ into a query for the sum of $a[1 \ldots 7]$ and a query for the sum of $a[1 \ldots 3]$, and subtract the results at the end?

![](images/fenwick-query.svg)

### Covered range

The question arises: how far to the left does the range covered by $c[x](x \ge 1)$ actually extend? In other words, what is the length of the range?

In a Fenwick tree, the length of the range covered by $c[x]$ is defined as $2^{k}$, where:

-   if we call the lowest binary bit the $0$-th bit, $k$ is exactly the index of the bit holding the lowest one (`1`) in the binary representation of $x$;
-   $2^k$ (the length of the range covered by $c[x]$) is exactly the number formed by the lowest `1` in the binary representation of $x$ and all zeros (`0`) after it.

Example: which range does $c_{88}$ cover?

Since $88_{(10)}=01011000_{(2)}$, the binary number formed by the lowest `1` and the zeros after it is `1000`, i.e. $8$, so $c_{88}$ covers $8$ elements of the array $a$.

Thus $c_{88}$ represents the information of the range $a[81 \ldots 88]$.

Denote by $\operatorname{lowbit}(x)$ the number formed by the lowest `1` in the binary representation of $x$ and the zeros after it; then the range covered by $c[x]$ is $[x-\operatorname{lowbit}(x)+1, x]$.

???+ warning "Note"
    $\operatorname{lowbit}$ is not the index $k$ of the bit holding the lowest `1`, but the number $2^k$ formed by that `1` and all zeros after it.

How to compute `lowbit`? From our knowledge of bitwise operations we get `lowbit(x) = x & -x`.

??? note "Why lowbit works"
    If we invert all bits of the binary representation of `x` and add 1, we get the binary representation of `-x`. For example, the binary representation of $6$ is `110`; after inverting all bits we get `001`, and after adding `1` we get `010`.
    
    Let the binary representation of `x` be of the form `(...)10...00`; after inverting all bits we get `[...]01...11`, and after adding `1` we get `[...]10...00`, which is exactly the binary representation of `-x`. Here the first `1` in the binary representation of `x` is also the lowest `1` of `x`.
    
    Every bit behind the ellipsis in `(...)` and `[...]` is the opposite of the other, so `x & -x = (...)10...00 & [...]10...00 = 10...00`, which is exactly `lowbit`.

???+ note "Implementation"
    === "C++"
        ```cpp
        int lowbit(int x) {
          // The number formed by the lowest one in the binary representation of x and all zeros after it.
          // lowbit(0b01011000) == 0b00001000
          //          ~~~~^~~~
          // lowbit(0b01110010) == 0b00000010
          //          ~~~~~~^~
          return x & -x;
        }
        ```
    
    === "Python"
        ```python
        def lowbit(x):
            """
            The number formed by the lowest one in the binary representation of x and all zeros after it.
            lowbit(0b01011000) == 0b00001000
                    ~~~~~^~~
            lowbit(0b01110010) == 0b00000010
                    ~~~~~~~^~
            """
            return x & -x
        ```

### Range query

Let us now look at the concrete implementation of the Fenwick tree operations, starting with the range query.

Recall the procedure for querying $a[4 \ldots 7]$: we turned it into two sub-procedures – a query for the sum of $a[1 \ldots 7]$ and a query for the sum of $a[1 \ldots 3]$ – and subtracted at the end.

In fact, every range query can be solved this way: the sum of $a[l \ldots r]$ equals the sum of $a[1 \ldots r]$ minus the sum of $a[1 \ldots l - 1]$, which turns a range problem into a prefix problem, which is easier to handle.

Turning a range query for $l \ldots r$ into prefix queries for $1 \ldots r$ and $1 \ldots l - 1$ and subtracting is a very common trick in contests.

So how do we perform a prefix query? Recall the procedure for querying $a[1 \ldots 7]$:

> From $c_{7}$ we jump backwards; we see that $c_{7}$ covers only the element $a_{7}$. Then we look at $c_{6}$; we see that $c_{6}$ covers $a[5 \ldots 6]$. Then we jump to $c_{4}$; we see that $c_{4}$ covers the elements $a[1 \ldots 4]$. Then we try to jump to $c_0$, but $c_0$ does not actually exist, so we stop.
>
> We have just found $c_7, c_6, c_4$; these are exactly the three small ranges into which $a[1 \ldots 7]$ is split; merging them gives the answer $c_7 + c_6 + c_4$.

Observe the procedure above: at each backward jump we always jump to the position immediately to the left of the left endpoint of the current range, which becomes the right endpoint of the new range; only in this way is the prefix split without overlaps and without gaps. For example, $c_6$ covers $a[5 \ldots 6]$, so next we jump to $5 - 1 = 4$, i.e. we access $c_4$.

The procedure for querying $a[1 \ldots x]$ can be written as follows:

-   start at $c[x]$ and jump backwards; $c[x]$ covers $a[x-\operatorname{lowbit}(x)+1 \ldots x]$;
-   set $x \gets x - \operatorname{lowbit}(x)$; if $x = 0$, we have reached the end and break the loop; otherwise go back to the first step;
-   merge all visited $c$.

In the implementation we do not need to first find all $c$ and only then merge them; we can merge as we jump.

For example, if the maintained information is the sum, we simply set $\mathrm{ans} = 0$ initially, and then for every visited $c[x]$ do $\mathrm{ans} \gets \mathrm{ans} + c[x]$; at the end $\mathrm{ans}$ is the result of merging everything.

???+ note "Implementation"
    === "C++"
        ```cpp
        int getsum(int x) {  // sum of a[1]..a[x]
          int ans = 0;
          while (x > 0) {
            ans = ans + c[x];
            x = x - lowbit(x);
          }
          return ans;
        }
        ```
    
    === "Python"
        ```python
        def getsum(x):  # sum of a[1]..a[x]
            ans = 0
            while x > 0:
                ans = ans + c[x]
                x = x - lowbit(x)
            return ans
        ```

### The Fenwick tree and the properties of its tree shape

Before explaining point updates, let us explain some basic properties of the Fenwick tree and the origin of its tree shape; this helps to understand point updates better.

Conventions:

-   $l(x) = x - \operatorname{lowbit}(x) + 1$. That is, $l(x)$ is the left endpoint of the range covered by $c[x]$.
-   Every positive integer $x$ can be written in the form $s \times 2^{k + 1} + 2^k$, where $\operatorname{lowbit}(x) = 2^k$.
-   Below, "$c[x]$ and $c[y]$ are disjoint" means that the ranges covered by $c[x]$ and $c[y]$ do not intersect, i.e. $[l(x), x]$ and $[l(y), y]$ are disjoint. Expressions like "$c[x]$ is contained in $c[y]$" are interpreted analogously.

**Property $\boldsymbol{1}$: for $\boldsymbol{x \le y}$, either $\boldsymbol{c[x]}$ and $\boldsymbol{c[y]}$ are disjoint, or $\boldsymbol{c[x]}$ is contained in $\boldsymbol{c[y]}$.**

??? note "Proof"
    Proof: suppose $c[x]$ and $c[y]$ intersect, i.e. $[l(x), x]$ and $[l(y), y]$ intersect; then certainly $l(y) \le x \le y$.
    
    Write $y$ as $s \times 2^{k +1} + 2^k$; then $l(y) = s \times 2^{k + 1} + 1$. Hence $x$ can be written as $s \times 2^{k +1} + b$, where $1 \le b \le 2^k$.
    
    It is easy to see that $\operatorname{lowbit}(x) = \operatorname{lowbit}(b)$. Since also $b - \operatorname{lowbit}(b) \ge 0$,
    
    we have $l(x) = x - \operatorname{lowbit}(x) + 1 = s \times 2^{k +1} + b - \operatorname{lowbit}(b) +1 \ge s \times 2^{k +1} + 1 = l(y)$, i.e. $l(y) \le l(x) \le x \le y$.
    
    Thus, if $c[x]$ and $c[y]$ intersect, the range covered by $c[x]$ is certainly entirely contained in $c[y]$.

**Property $\boldsymbol{2}$: $\boldsymbol{c[x]}$ is a proper subset of $\boldsymbol{c[x + \operatorname{lowbit}(x)]}$.**

??? note "Proof"
    Proof: let $y = x + \operatorname{lowbit}(x)$ and $x = s \times 2^{k + 1} + 2^k$; then $y = (s + 1) \times 2^{k +1}$ and $l(x) = s \times 2^{k + 1} + 1$.
    
    It is easy to see that $\operatorname{lowbit}(y) \ge 2^{k + 1}$, so $l(y) = (s + 1) \times 2^{k + 1} - \operatorname{lowbit}(y) + 1 \le s \times 2^{k +1} + 1= l(x)$, i.e. $l(y) \le l(x) \le x < y$.
    
    Thus $c[x]$ is a proper subset of $c[x + \operatorname{lowbit}(x)]$.

**Property $3$: for every $\boldsymbol{x < y < x + \operatorname{lowbit}(x)}$, $\boldsymbol{c[x]}$ and $\boldsymbol{c[y]}$ are disjoint.**

??? note "Proof"
    Proof: let $x = s \times 2^{k + 1} + 2^k$; then $y = x + b = s \times 2^{k + 1} + 2^k + b$, where $1 \le b < 2^k$.
    
    It is easy to see that $\operatorname{lowbit}(y) = \operatorname{lowbit}(b)$. Since also $b - \operatorname{lowbit}(b) \ge 0$,
    
    we have $l(y) = y - \operatorname{lowbit}(y) + 1 = x + b - \operatorname{lowbit}(b) + 1 > x$, i.e. $l(x) \le x < l(y) \le y$.
    
    Thus $c[x]$ and $c[y]$ are disjoint.

With these three properties, let us now look at the tree shape of the Fenwick tree (ignore the edges from $a$ to $c$).

![](./images/fenwick.svg)

In fact, the tree shape of the Fenwick tree is the graph obtained by drawing an edge from $x$ to $x + \operatorname{lowbit}(x)$, where $x + \operatorname{lowbit}(x)$ is the parent of $x$.

Note: when considering the tree shape of the Fenwick tree, we do not take the size of the Fenwick tree into account, i.e. for ease of analysis we regard the tree as infinitely large. In an actual implementation we only need $c[x]$ for $x \le n$, where $n$ is the length of the original array.

This tree naturally has many nice properties; we list some (let $fa[u]$ denote the direct parent of $u$):

-   $u < fa[u]$.
-   $u$ is greater than every one of its descendants and smaller than every one of its ancestors.
-   The $\operatorname{lowbit}$ of vertex $u$ is strictly smaller than the $\operatorname{lowbit}$ of vertex $fa[u]$.

??? note "Proof"
    Let $y = x + \operatorname{lowbit}(x)$ and $x = s \times 2^{k + 1} + 2^k$; then $y = (s + 1) \times 2^{k +1}$ and it is easy to see that $\operatorname{lowbit}(y) \ge 2^{k + 1} > \operatorname{lowbit}(x)$, which is what we had to prove.

-   The height of vertex $x$ is $\log_2\operatorname{lowbit}(x)$, i.e. the index of the bit holding the lowest `1` in the binary representation of $x$.

??? note "Definition of height"
    The height $h(x)$ of vertex $x$ satisfies: if $x \bmod 2 = 1$, then $h(x) = 0$; otherwise $h(x) = \max(h(y)) + 1$, where $y$ ranges over all children of $x$ (in this case $x$ has at least one child, $x - 1$).
    
    In other words, the height of a vertex is exactly $1$ more than the height of its tallest child. If a vertex has no children, its height is $0$.
    
    We introduce the notion of height here so that the complexity can be explained more easily later.

-   $c[u]$ is a proper subset of $c[fa[u]]$ (property $2$).
-   $c[u]$ is a proper subset of $c[v]$, where $v$ is any ancestor of $u$ (by induction from the previous property).
-   $c[u]$ properly contains $c[v]$, where $v$ is any descendant of $u$ (the previous property with $u$ and $v$ swapped).
-   For every $v' > u$, if $v'$ is not an ancestor of $u$, then $c[u]$ and $c[v']$ are disjoint.

??? note "Proof"
    Among $u$ and the ancestors of $u$ there is certainly a vertex $v$ such that $v < v' < fa[v]$; by property $3$, $c[v']$ is disjoint from $c[v]$, and $c[v]$ contains $c[u]$, so $c[v']$ is disjoint from $c[u]$.

-   For every $v < u$, if $v$ is not in the subtree of $u$, then $c[u]$ and $c[v]$ are disjoint (the previous property with $u$ and $v'$ swapped).
-   For every $v > u$, $c[u]$ is a proper subset of $c[v]$ if and only if $v$ is an ancestor of $u$ (a summary of several previous properties). This is the fundamental principle of point updates in a Fenwick tree.
-   Let $u = s \times 2^{k + 1} + 2^k$; then $u$ has $k = \log_2\operatorname{lowbit}(u)$ children, labeled $u - 2^t(0 \le t < k)$.
    -   Example: let $k = 3$ and let the binary label of $u$ be `...1000`; then $u$ has three children, with binary labels `...0111`, `...0110` and `...0100`.

??? note "Proof"
    If we subtract $2^t$ from a number $x$, the $t$-th bit of $x$ is flipped, and the lower bits remain unchanged.
    
    Consider a child $v$ of $u$: we have $v + \operatorname{lowbit}(v) = u$, i.e. $v = u - 2^t$ and $\operatorname{lowbit}(v) = 2^t$. Let $u = s \times 2^{k + 1} + 2^k$.
    
    **Case $\boldsymbol{0 \le t < k}$**: the $t$-th bit of $u$ and all bits after it are $0$, so the $t$-th bit of $v = u - 2^t$ becomes $1$, and the bits after it remain $0$; $\operatorname{lowbit}(v) = 2^t$ **holds**.
    
    **Case $\boldsymbol{t = k}$**: then $v = u - 2^k$, the $k$-th bit of $v$ becomes $0$; $\operatorname{lowbit}(v) = 2^t$ **does not hold**.
    
    **Case $\boldsymbol{t > k}$**: then $v = u - 2^t$, the $k$-th bit of $v$ is $1$, so $\operatorname{lowbit}(v) = 2^k$; $\operatorname{lowbit}(v) = 2^t$ **does not hold**.

-   The ranges covered by the $c$ of all children of $u$ fit together exactly into $[l(u), u - 1]$.
    -   Example: let $k = 3$ and let the binary label of $u$ be `...1000`; then $u$ has three children, with binary labels `...0111`, `...0110` and `...0100`.
    -   `c[...0100]` represents `a[...0001 ~ ...0100]`.
    -   `c[...0110]` represents `a[...0101 ~ ...0110]`.
    -   `c[...0111]` represents `a[...0111 ~ ...0111]`.
    -   It is easy to see that the union of the three covered ranges above is exactly `a[...0001 ~ ...0111]`, i.e. $[l(u), u - 1]$.

??? note "Proof"
    The children of $u$ can always be written as $u - 2^t(0 \le t < k)$; it is easy to see that for smaller $t$ the number $u - 2^t$ is larger, so the range it represents is further to the right. Let $f(t) = u - 2^t$; then $f(k - 1), f(k - 2), \ldots, f(0)$ are the children of $u$ from left to right.
    
    It is easy to see that $\operatorname{lowbit}(f(t)) = 2^t$, so $l(f(t)) = u - 2^t - 2^t + 1 = u - 2^{t + 1} + 1$.
    
    Consider two adjacent children $f(t + 1)$ and $f(t)$. The right endpoint of the range of the former is $f(t + 1) = u - 2^{t + 1}$, and the left endpoint of the range of the latter is $l(f(t)) = u - 2^{t + 1} + 1$; they fit together exactly.
    
    Consider the leftmost child $f(k - 1)$: the left endpoint of its range $l(f(k - 1)) = u - 2^k + 1$ is exactly $l(u)$.
    
    Consider the rightmost child $f(0)$: the right endpoint of its range is exactly $u - 1$.
    
    Thus the ranges covered by these children fit together exactly into $[l(u), u - 1]$.

### Point update

Let us now consider how to update $a[x]$ at a point.

Our goal is to maintain the array $c$ quickly and correctly. For efficiency we need to visit and modify only those $c[y]$ that cover $a[x]$, because the other $c$ obviously do not change.

Every $c[y]$ that covers $a[x]$ certainly contains $c[x]$ (by property $1$), so in the tree shape of the Fenwick tree $y$ is an ancestor of $x$. Therefore, starting from $x$, we keep jumping to the parent until we exceed the length of the original array.

Let $n$ denote the size of the array $a$; the procedure for a point update of $a[x]$ is easy to write down:

-   initially set $x' = x$;
-   modify $c[x']$;
-   set $x' \gets x' + \operatorname{lowbit}(x')$; if $x' > n$, we have reached the end and break the loop; otherwise go back to the second step.

The type of range information and the type of point update together determine how $c[x']$ is modified. A few examples:

-   If $c[x']$ maintains the range sum and the update adds $p$ to $a[x]$, then every $c[x']$ is also increased by $p$.
-   If $c[x']$ maintains the range product and the update multiplies $a[x]$ by $p$, then every $c[x']$ is also multiplied by $p$.

However, because of the freedom of point updates, the type of update and the maintained information do not have to be the same operation; for example, if $c[x']$ maintains the range sum and the update assigns the value $p$ to $a[x]$, we can turn it into adding $p - a[x]$ to $a[x]$. If the update multiplies $a[x]$ by $p$, we turn it into adding $a[x] \times p - a[x]$ to $a[x]$.

We give the implementation using the example of maintaining range sums with point addition.

???+ note "Implementation"
    === "C++"
        ```cpp
        void add(int x, int k) {
          while (x <= n) {  // must not go out of bounds
            c[x] = c[x] + k;
            x = x + lowbit(x);
          }
        }
        ```
    
    === "Python"
        ```python
        def add(x, k):
            while x <= n:  # must not go out of bounds
                c[x] = c[x] + k
                x = x + lowbit(x)
        ```

### Building the tree

This means building the Fenwick tree from an initially given array (fully preprocessing $c$).

Usually this can be turned directly into $n$ point updates, with complexity $\Theta(n \log n)$ (the complexity analysis follows later).

For example, if we need to build the tree for the array $a = (5, 1, 4)$, we simply view this as adding $5$ at point $a[1]$, adding $1$ at point $a[2]$ and adding $4$ at point $a[3]$.

There is also a $\Theta(n)$ construction; see the section [$\Theta(n)$ tree construction](#thetan-tree-construction) on this page.

### Complexity analysis

The space complexity is obviously $\Theta(n)$.

Time complexity:

-   For a range query: the whole iterative procedure $x \gets x - \operatorname{lowbit}(x)$ can be viewed as gradually turning all ones in the binary representation of $x$ into zeros, from the lower bits to the higher ones; the number of ranges into which we split equals the number of ones in the binary representation of $x$ (i.e. $\operatorname{popcount}(x)$). Thus the complexity of one query is $\Theta(\log n)$;
-   For a point update: when jumping to the parent, the visited height strictly increases, and $x \le n$ always holds. Since the height of vertex $x$ equals $\log_2\operatorname{lowbit}(x)$, the reached height does not exceed $\log_2n$, so the number of visited $c$ is of the order $\log n$. Thus the complexity of one point update is $\Theta(\log n)$.

## Range add, range sum

Prerequisite: [Prefix sums and differences](../basic/prefix-sum.md).

This problem can be solved with two Fenwick trees maintaining the difference array.

Consider the difference array $d$ of the array $a$, where $d[i] = a[i] - a[i - 1]$. Since the prefix sum of the difference array is exactly the original array, we have $a_i=\sum_{j=1}^i d_j$.

As before, we turn the range-sum query into a prefix-sum query by subtraction. Consider the query for the sum of $a[1 \ldots r]$, i.e. $\sum_{i=1}^{r} a_i$, and derive:

$$
\begin{aligned}
&\sum_{i=1}^{r} a_i\\=&\sum_{i=1}^r\sum_{j=1}^i d_j
\end{aligned}
$$

Looking at the expression, it is easy to see that each $d_j$ is added $r - j + 1$ times in total. Continue the derivation:

$$
\begin{aligned}
&\sum_{i=1}^r\sum_{j=1}^i d_j\\=&\sum_{i=1}^r d_i\times(r-i+1)
\\=&\sum_{i=1}^r d_i\times (r+1)-\sum_{i=1}^r d_i\times i
\end{aligned}
$$

From $\sum_{i=1}^r d_i$ we cannot derive the value of $\sum_{i=1}^r d_i \times i$, so we need two Fenwick trees that separately maintain the sums of $d_i$ and of $d_i \times i$.

So how do we perform a range add? Consider how adding $x$ on the range $a[l \ldots r]$ of the original array affects $d$.

Since the difference is $d[i] = a[i] - a[i - 1]$,

-   $a[l]$ increased by $v$ and $a[l - 1]$ is unchanged, so $d[l]$ increased by $v$;
-   $a[r + 1]$ is unchanged and $a[r]$ increased by $v$, so $d[r + 1]$ decreased by $v$;
-   for every $i$ different from $l$ and from $r+1$, $a[i]$ and $a[i - 1]$ are either both unchanged or both increased by $v$, and $a[i] + v - (a[i - 1] + v)$ is still $a[i] - a[i - 1]$, so the remaining $d[i]$ are unchanged.

From this the maintenance method is easy to come up with: in the Fenwick tree maintaining $d_i$ we add $v$ at point $l$ and $-v$ at point $r + 1$; in the Fenwick tree maintaining $d_i \times i$ we add $v \times l$ at point $l$ and $-v \times (r + 1)$ at point $r + 1$.

For the weaker problem, "range add with point query", it suffices to maintain only the difference array $d_i$ with a Fenwick tree. To query the value of $a[x]$ at a point, we simply compute the sum of $d[1 \ldots x]$.

Here we directly give the code for "range add, range sum":

???+ note "Implementation"
    === "C++"
        ```cpp
        int t1[MAXN], t2[MAXN], n;
        
        int lowbit(int x) { return x & (-x); }
        
        void add(int k, int v) {
          int v1 = k * v;
          while (k <= n) {
            t1[k] += v, t2[k] += v1;
            // Note: we must not write t2[k] += k * v, because k is no longer an index into the original array
            k += lowbit(k);
          }
        }
        
        int getsum(int *t, int k) {
          int ret = 0;
          while (k) {
            ret += t[k];
            k -= lowbit(k);
          }
          return ret;
        }
        
        void add1(int l, int r, int v) {
          add(l, v), add(r + 1, -v);  // split the range add into two prefix adds
        }
        
        long long getsum1(int l, int r) {
          return (r + 1ll) * getsum(t1, r) - 1ll * l * getsum(t1, l - 1) -
                 (getsum(t2, r) - getsum(t2, l - 1));
        }
        ```
    
    === "Python"
        ```python
        t1 = [0] * MAXN
        t2 = [0] * MAXN
        n = 0
        
        
        def lowbit(x):
            return x & (-x)
        
        
        def add(k, v):
            v1 = k * v
            while k <= n:
                t1[k] = t1[k] + v
                t2[k] = t2[k] + v1
                k = k + lowbit(k)
        
        
        def getsum(t, k):
            ret = 0
            while k:
                ret = ret + t[k]
                k = k - lowbit(k)
            return ret
        
        
        def add1(l, r, v):
            add(l, v)
            add(r + 1, -v)
        
        
        def getsum1(l, r):
            return (
                (r) * getsum(t1, r)
                - l * getsum(t1, l - 1)
                - (getsum(t2, r) - getsum(t2, l - 1))
            )
        ```

By the same principle it should be possible to implement "range multiply, range product", "range XOR with a number, range XOR query", etc., as long as the maintained information and the range operation are the same kind of operation; interested readers can try this themselves.

## Two-dimensional Fenwick tree

### Point update, submatrix query

The two-dimensional Fenwick tree, also known as the Fenwick tree of Fenwick trees, is used to maintain point updates and prefix information over a two-dimensional array.

Similarly to the one-dimensional Fenwick tree, we denote by $c(x, y)$ the total information of the matrix $a(x - \operatorname{lowbit}(x) + 1, y - \operatorname{lowbit}(y) + 1) \ldots a(x, y)$, i.e. the matrix whose bottom-right corner is $a(x, y)$, with height $\operatorname{lowbit}(x)$ and width $\operatorname{lowbit}(y)$.

For a point update, let:

$$
f(x, i) = \begin{cases}x &i = 0\\f(x, i - 1) + \operatorname{lowbit}(f(x, i - 1)) & i > 0\\\end{cases}
$$

That is, $f(x, i)$ is the $i$-th ancestor of $x$ in the tree shape of the Fenwick tree (the $0$-th ancestor is the vertex itself).

Then $a(x, y)$ is covered only by the elements $c(f(x, i), f(y, j))$, so when updating $a(x, y)$ we only need to modify all $c(f(x, i), f(y, j))$ with $f(x, i) \le n$ and $f(y, j) \le m$.

??? note "Proof of correctness"
    Let $c(p, q)$ cover $a(x, y)$; we look for the possible values of $p$ and $q$.
    
    Consider a one-dimensional Fenwick tree $c_1$ of size $n$ (over the original array $a_1$) and a one-dimensional Fenwick tree $c_2$ of size $m$ (over the original array $a_2$).
    
    The statement is then equivalent to the condition: $c_1(p)$ covers $a_1[x]$ and $c_2(q)$ covers $a_2[y]$.
    
    In other words, in the tree shape of the Fenwick tree, $p$ is one of the vertices among $x$ and its ancestors, and $q$ is one of the vertices among $y$ and its ancestors.
    
    Thus $p = f(x, i)$ and $q = f(y, j)$.

For a query, let:

$$
g(x, i) = \begin{cases}x &i = 0\\g(x, i - 1) - \operatorname{lowbit}(g(x, i - 1)) & i, g(x, i - 1) > 0\\0&\text{otherwise.}\end{cases}
$$

Then we merge all $c(g(x, i), g(y, j))$ with $g(x, i), g(y, j) > 0$.

??? note "Proof of correctness"
    Let $\circ$ denote the operation merging two pieces of information (for example, if the information is the range sum, then $\circ = +$).
    
    Consider a one-dimensional Fenwick tree $c_1$: $c_1[g(x, 0)] \circ c_1[g(x, 1)] \circ c_1[g(x, 2)] \circ \cdots$ represents exactly the information of the range $[1 \ldots x]$ of the original array.
    
    Similarly, let $t(x) = c(x, g(y, 0)) \circ c(x, g(y, 1)) \circ c(x, g(y, 2)) \circ \cdots$; then $t(x)$ represents exactly the information of the matrix $a(x - \operatorname{lowbit}(x) + 1, 1) \ldots a(x, y)$.
    
    Again similarly, $t(g(x, 0)) \circ t(g(x, 1)) \circ t(g(x, 2)) \circ \cdots$ represents the information of the matrix $a(1, 1) \ldots a(x, y)$.
    
    In fact, if we view the function $t(x)$ as a Fenwick tree, we get a Fenwick tree nested inside a Fenwick tree; hence the name "Fenwick tree of Fenwick trees".

Below is the code for point addition and submatrix-sum query.

???+ note "Implementation"
    === "Point addition"
        ```cpp
        void add(int x, int y, int v) {
          for (int i = x; i <= n; i += lowbit(i)) {
            for (int j = y; j <= m; j += lowbit(j)) {
              // Note: here we must introduce loop variables; we cannot just write while (x <= n) as in the one-dimensional case
              c[i][j] += v;
            }
          }
        }
        ```
    
    === "Submatrix-sum query"
        ```cpp
        int sum(int x, int y) {
          int res = 0;
          for (int i = x; i > 0; i -= lowbit(i)) {
            for (int j = y; j > 0; j -= lowbit(j)) {
              res += c[i][j];
            }
          }
          return res;
        }
        
        int ask(int x1, int y1, int x2, int y2) {
          // submatrix-sum query
          return sum(x2, y2) - sum(x2, y1 - 1) - sum(x1 - 1, y2) + sum(x1 - 1, y1 - 1);
        }
        ```

### Submatrix add, submatrix sum

Prerequisites: [Prefix sums and differences](../basic/prefix-sum.md) and the section [Range add, range sum](#range-add-range-sum) on this page.

Similarly to the "range add, range sum" problem of the one-dimensional Fenwick tree, consider maintaining the difference array.

The difference array over a two-dimensional array looks like this:

$$
d(i, j) = a(i, j) - a(i - 1, j) - a(i, j - 1) + a(i - 1, j - 1)．
$$

??? note "Why exactly this definition?"
    Because ideally the two-dimensional prefix sum over the difference matrix should give the original matrix, since these are mutually inverse operations.
    
    The formula for the two-dimensional prefix sum is:
    
    $s(i, j) = s(i - 1, j) + s(i, j - 1) - s(i - 1, j - 1) + a(i, j)$.
    
    Thus, if $a$ is the original array and $d$ the difference array, we have:
    
    $a(i, j) = a(i - 1, j) + a(i, j - 1) - a(i - 1, j - 1) + d(i, j)$
    
    Rearranging the terms gives the formula for two-dimensional differences:
    
    $d(i, j) = a(i, j) - a(i - 1, j) - a(i, j - 1) + a(i - 1, j - 1)$.

Thus adding $v$ on the submatrix with top-left corner $(x_1, y_1)$ and bottom-right corner $(x_2, y_2)$ corresponds, in the difference array, to adding $v$ at the points $d(x_1, y_1)$ and $d(x_2 + 1, y_2 + 1)$ and adding $-v$ at the points $d(x_2 + 1, y_1)$ and $d(x_1, y_2 + 1)$.

As for the reason, it suffices to expand these four $d$ by definition and analyze the change of each term.

Example: let the difference array be initially $0$; after adding $v$ on the submatrix $a(2, 2) \ldots a(3, 4)$, the difference array becomes:

$$
\begin{pmatrix}0&0&0&0&0\\0&v&0&0&-v\\0&0&0&0&0\\0&-v&0&0&v\end{pmatrix}
$$

(Here the submatrix $a(2, 2) \ldots a(3, 4)$ is exactly the central matrix of size $2 \times 3$.)

Thus we perform a submatrix add by turning it into four point additions on the difference array.

Now consider the submatrix-sum query:

For a point $(x, y)$, the two-dimensional prefix sum can be written as:

$$
\sum_{i = 1}^x\sum_{j = 1}^y\sum_{h = 1}^i\sum_{k = 1}^j d(h, k)
$$

The reason is that the prefix sum of the prefix sum of the differences is exactly the original prefix sum.

Similarly to the "range add, range sum" problem of the one-dimensional Fenwick tree, we count the occurrences of $d(h, k)$: there are $(x - h + 1) \times (y - k + 1)$ of them.

Continue the derivation:

$$
\begin{aligned}
&\sum_{i = 1}^x\sum_{j = 1}^y\sum_{h = 1}^i\sum_{k = 1}^j d(h, k)
\\=&\sum_{i = 1}^x\sum_{j = 1}^y d(i, j) \times (x - i + 1) \times (y - j + 1)
\\=&\sum_{i = 1}^x\sum_{j = 1}^y d(i, j) \times (xy + x + y + 1) - d(i, j) \times i \times (y + 1) - d(i, j) \times j \times (x + 1) + d(i, j) \times i \times j
\end{aligned}
$$

Thus we need to maintain four Fenwick trees, maintaining respectively the sums of $d(i, j)$, $d(i, j) \times i$, $d(i, j) \times j$ and $d(i, j) \times i \times j$.

Of course, as in the one-dimensional case, if we only need submatrix add with point query, it suffices to maintain a single difference array and query its prefix sum.

The code follows:

???+ note "Implementation"
    ```cpp
    using ll = long long;
    ll t1[N][N], t2[N][N], t3[N][N], t4[N][N];
    
    void add(ll x, ll y, ll z) {
      for (int X = x; X <= n; X += lowbit(X))
        for (int Y = y; Y <= m; Y += lowbit(Y)) {
          t1[X][Y] += z;
          t2[X][Y] += z * x;  // Note: z * x, not z * X; the same applies below
          t3[X][Y] += z * y;
          t4[X][Y] += z * x * y;
        }
    }
    
    void range_add(ll xa, ll ya, ll xb, ll yb,
                   ll z) {  // submatrix from (xa, ya) to (xb, yb)
      add(xa, ya, z);
      add(xa, yb + 1, -z);
      add(xb + 1, ya, -z);
      add(xb + 1, yb + 1, z);
    }
    
    ll ask(ll x, ll y) {
      ll res = 0;
      for (int i = x; i; i -= lowbit(i))
        for (int j = y; j; j -= lowbit(j))
          res += (x + 1) * (y + 1) * t1[i][j] - (y + 1) * t2[i][j] -
                 (x + 1) * t3[i][j] + t4[i][j];
      return res;
    }
    
    ll range_ask(ll xa, ll ya, ll xb, ll yb) {
      return ask(xb, yb) - ask(xb, ya - 1) - ask(xa - 1, yb) + ask(xa - 1, ya - 1);
    }
    ```

## Fenwick tree over the frequency array and its applications

We know that an ordinary Fenwick tree is built directly over the original array; $c_6$ represents the information of the range $a[5 \ldots 6]$.

But in fact we can also build a Fenwick tree over the frequency array of the original array; this is the Fenwick tree over the frequency array.

??? note "What is a frequency array?"
    The frequency array $b$ of an array $a$ satisfies: the value $b[x]$ equals the number of occurrences of $x$ in $a$.
    
    For example, the frequency array of $a = (1, 3, 4, 3, 4)$ is $b = (1, 0, 2, 2)$.
    
    Obviously the size of $b$ depends on the value range of $a$.
    
    If the value range of the original array is too large, and what matters is not the concrete values but only their relative order, the original array is often [compressed (discretized)](../misc/discrete.md) before building the frequency array.
    
    Moreover, the frequency array represents an array without regard to order: it describes the content of the array's elements and ignores their order; if two arrays differ only in order but have the same content, they have the same frequency array.
    
    That is why, for problems in which the order of the given array does not affect the answer, it is usually more intuitive to think in terms of the frequency array, for example [\[NOIP2021\] 数列](https://www.luogu.com.cn/problem/P7961).

With the Fenwick tree over the frequency array we can solve several classic problems.

### Point update, global $k$-th smallest query

Here we only consider the $k$-th smallest; the $k$-th largest problem reduces to the $k$-th smallest by a simple computation.

This problem allows value compression: if the value range of the original array $a$ is too large, we compress it and only then build the frequency array $b$. Note that the values appearing in point updates must also be compressed, not only the elements of the original array $a$.

For a point update, it suffices to turn the point update of the original array into a point update of the frequency array. Concretely, if $a[x]$ changes from $y$ to $z$, this corresponds in the frequency array $b$ to decreasing $b[y]$ by $1$ and increasing $b[z]$ by $1$.

For the $k$-th smallest query, consider a binary search over $x$: we query the prefix sum $[1, x]$ of the frequency array and look for $x_0$ such that the prefix sum $[1, x_0]$ is $< k$ and the prefix sum $[1, x_0 + 1]$ is $\ge k$; then the $k$-th number is $x_0 + 1$ (note: we regard the prefix sum $[1, 0]$ as $0$).

The complexity is then $\Theta(\log^2n)$.

Consider replacing the binary search with binary lifting.

Let $x = 0$, $\mathrm{sum} = 0$; iterate $i$ from $\log_2n$ down to $0$:

-   query the sum $t$ of the range $[x + 1 \ldots x + 2^i]$ of the frequency array;
-   if $\mathrm{sum} + t < k$, the extension succeeds: $x \gets x + 2^i$, $\mathrm{sum} \gets \mathrm{sum} + t$; otherwise the extension fails and we do nothing.

The $x$ obtained this way is the largest number for which the prefix sum $[1 \ldots x]$ is $< k$, so the final answer is $x + 1$.

It seems that this method does not improve the time efficiency at all, but in fact, to query the sum of $[x + 1 \ldots x + 2^i]$ it suffices to access the value $c[x + 2^i]$.

The reason is simple: consider $\operatorname{lowbit}(x + 2^i)$; it is certainly $2^i$, because so far only powers $2^j$ with $j > i$ have been added to $x$. Therefore $c[x + 2^i]$ represents exactly the range $[x + 1 \ldots x + 2^i]$.

Thus the time complexity drops to $\Theta(\log n)$.

???+ note "Implementation"
    === "C++"
        ```cpp
        // k-th smallest query in a Fenwick tree over the frequency array
        int kth(int k) {
          int sum = 0, x = 0;
          for (int i = log2(n); ~i; --i) {
            x += 1 << i;                   // try to extend
            if (x > n || sum + t[x] >= k)  // if the extension fails
              x -= 1 << i;
            else
              sum += t[x];
          }
          return x + 1;  // if it does not exist, returns n + 1
        }
        ```
    
    === "Python"
        ```python
        # k-th smallest query in a Fenwick tree over the frequency array
        def kth(k):
            sum = 0
            x = 0
            i = int(log2(n))
            while ~i:
                x = x + (1 << i)  # try to extend
                if x > n or sum + t[x] >= k:  # if the extension fails
                    x = x - (1 << i)
                else:
                    sum = sum + t[x]
                i = i - 1
            return x + 1  # if it does not exist, returns n + 1
        ```

### Global inversions (global two-dimensional partial order)

Further reading and reference implementation: [Inversions](../math/permutation.md#逆序数)

Global inversions can also be solved elegantly with a Fenwick tree over the frequency array. The problem is: given an array $a$ of length $n$, compute the number of pairs $(i, j)$ in $a$ with $i < j$ and $a[i] > a[j]$.

This problem allows value compression: if the value range of the original array $a$ is too large, we compress it and only then build the frequency array $b$.

We iterate $i$ backwards from $n$ to $1$ as the index of the first element of an inversion, then compute how many $j > i$ satisfy $a[j] < a[i]$, and finally add up the answers.

In fact we only need to do the following (let the current $a[i] = x$):

-   query the prefix sum $b[1 \ldots x - 1]$; this is the number of inversions whose left element is $a[i]$;
-   increase $b[x]$ by $1$.

The reason is quite natural: the elements appearing in $b[1 \ldots x-1]$ are certainly smaller than the current $x = a[i]$, and because $i$ is iterated backwards, the indices $j$ in the original array of those elements already in the frequency array are naturally greater than the current index $i$.

As an example, $a = (4, 3, 1, 2, 1)$.

$i$ goes $5 \to 1$:

-   $a[5] = 1$, the prefix sum $b[1 \ldots 0]$ is $0$, increase $b[1]$ by $1$, $b = (1, 0, 0, 0)$.
-   $a[4] = 2$, the prefix sum $b[1 \ldots 1]$ is $1$, increase $b[2]$ by $1$, $b = (1, 1, 0, 0)$.
-   $a[3] = 1$, the prefix sum $b[1 \ldots 0]$ is $0$, increase $b[1]$ by $1$, $b = (2, 1, 0, 0)$.
-   $a[2] = 3$, the prefix sum $b[1 \ldots 2]$ is $3$, increase $b[3]$ by $1$, $b = (2, 1, 1, 0)$.
-   $a[1] = 4$, the prefix sum $b[1 \ldots 3]$ is $4$, increase $b[4]$ by $1$, $b = (2, 1, 1, 1)$.

The final answer is therefore $0 + 1 + 0 + 3 + 4 = 8$.

Note that while iterating over $i$, the two steps – querying $b[1 \ldots x - 1]$ and increasing $b[x]$ – can be swapped, i.e. first increase $b[x]$ and only then query $b[1 \ldots x - 1]$, without affecting the answer. Two explanations:

-   Modifying $b[x]$ does not affect the query $b[1 \ldots x - 1]$.
-   After swapping, we actually count pairs with $i \le j$ and $a[i] > a[j]$, and for $i = j$ we never have $a[i] > a[j]$, so $i \le j$ is the same as $i < j$; this is equivalent to the original inversion problem.

If we count non-strict inversions ($i < j$ and $a[i] \ge a[j]$), we need to query the sum $b[1 \ldots x]$, and then these two steps must not be swapped; again two explanations:

-   Modifying $b[x]$ **does** affect the query $b[1 \ldots x]$.
-   After swapping, we actually count pairs with $i \le j$ and $a[i] \ge a[j]$, and for $i = j$ we always have $a[i] \ge a[j]$, so $i \le j$ **is not the same as** $i < j$ and the problem **is not equivalent** to the original.

If we count pairs with $i \le j$ and $a[i] \ge a[j]$, then these two steps must indeed be swapped.

In addition, for the original inversion problem there is also an approach that iterates $j$ forwards, asking how many $i < j$ satisfy $a[i] > a[j]$. The procedure is as follows (let $x = a[j]$):

-   query the range sum $b[x + 1 \ldots V]$ ($V$ is the size of $b$, i.e. the value range of $a$ (or the range after compression));
-   increase $b[x]$ by $1$.

Reason: the elements appearing in $b[x + 1 \ldots V]$ are certainly greater than the current $x = a[j]$, and because $j$ is iterated forwards, the indices $i$ in the original array of those elements already in the frequency array are naturally smaller than the current index $j$.

Furthermore, inversions can also be counted with [merge sort](../basic/merge-sort.md#inversions). That approach avoids value compression. Its time complexity is also $O(n\log n)$. Reference implementations of both algorithms can be found in the chapter [Inversions](../math/permutation.md#逆序数).

## Fenwick tree for non-invertible information

For example, for maintaining range extrema and the like.

Note: although this method has little code, the time complexity of both point updates and range queries is $\Theta(\log^2n)$, which is worse than the $\Theta(\log n)$ complexity with a segment tree.

### Range query

We still follow the previous idea: from $r$ we jump backwards by $\operatorname{lowbit}$, but we must not jump to the left of $l$.

Therefore, when we reach $c[x]$, we first check whether the next destination $x - \operatorname{lowbit}(x)$ is smaller than $l$:

-   if it is smaller than $l$, we directly merge **the point $\boldsymbol{a[x]}$** into the total information and jump to $c[x - 1]$;
-   if it is greater than or equal to $l$, we have not gone out of bounds, so we merge $c[x]$ normally and jump to $c[x - \operatorname{lowbit}(x)]$.

Below is the code using the example of a range-maximum query:

???+ note "Implementation"
    ```cpp
    int getmax(int l, int r) {
      int ans = 0;
      while (r >= l) {
        ans = max(ans, a[r]);
        --r;
        for (; r - lowbit(r) >= l; r -= lowbit(r)) {
          // Note: the loop condition must not be r - lowbit(r) + 1 >= l,
          // otherwise for l = 1, r jumps to 0 and the loop becomes infinite
          ans = max(ans, C[r]);
        }
      }
      return ans;
    }
    ```

It can be proved that the time complexity of the above algorithm is $\Theta(\log^2n)$.

??? note "Proof of time complexity"
    Consider the highest bit in which $r$ and $l$ differ; in that bit $r$ certainly has a $1$ and $l$ has a $0$ (because $r \ge l$).
    
    If $r$ has further ones after that bit, then certainly $r - \operatorname{lowbit}(r) \ge l$, so the next step certainly turns the lowest one of $r$ into $0$;
    
    if that one of $r$ is also the lowest one of $r$, then whether we do $r \gets r - \operatorname{lowbit}(r)$ or $r \gets r - 1$, that one of $r$ certainly becomes $0$.
    
    Thus, after at most $\log n$ transformations of $r$, the highest bit in which $r$ and $l$ differ certainly drops by one. Therefore the total time complexity is $\Theta(\log^2n)$.

### Point update

???+ note "Note"
    Before studying this section, understand the following two properties of the tree shape of the Fenwick tree.
    
    -   Let $u = s \times 2^{k + 1} + 2^k$; then $u$ has $k = \log_2\operatorname{lowbit}(u)$ children, labeled $u - 2^t(0 \le t < k)$.
    -   The ranges covered by the $c$ of all children of $u$ fit together exactly into $[l(u), u - 1]$.
    
    The meaning and proof of these two properties can be found in the section [The Fenwick tree and the properties of its tree shape](#the-fenwick-tree-and-the-properties-of-its-tree-shape) on this page.

After updating $a[x]$, we only need to update those $c[y]$ for which $y$ is an ancestor of $x$ in the tree shape of the Fenwick tree.

For extrema (using the maximum as an example), a common wrong idea is: if we change $a[x]$ to $p$, update every $c[y]$ to $\max(c[y], p)$. Here is a counterexample: in $(1, 2, 3, 4, 5)$ change $5$ to $4$; the maximum is $4$, but with the above update we would get $5$. Directly setting $c[y]$ to $p$ is also wrong; a counterexample is changing $3$ to $4$ in the above example.

In fact, for non-invertible information there is no way to modify $c[y]$ directly using $p$. The reason is that an update is really "removing" the old number from the range and adding the new one. The effect of "removing" on the range information corresponds to an "inverse operation", and non-invertible information has no "inverse operation", so $c[y]$ cannot be modified directly.

In other words, for every affected $c[y]$ we must rebuild the information of that range.

Consider the children of $c[y]$: their information is certainly correct (because we first update the children and then the parent), and these children form exactly the covered range $[l(y), y - 1]$; if we also add the point $a[y]$, we get $[l(y), y]$, i.e. $c[y]$. Thus every $c$ that needs to be modified can be rebuilt by merging at most $\log n$ ranges.

???+ note "Implementation"
    ```cpp
    void update(int x, int v) {
      a[x] = v;
      for (int i = x; i <= n; i += lowbit(i)) {
        // iterate over the affected ranges
        C[i] = a[i];
        for (int j = 1; j < lowbit(i); j *= 2) {
          C[i] = max(C[i], C[i - j]);
        }
      }
    }
    ```

It is easy to see that the time complexity of the above algorithm is $\Theta(\log^2n)$.

### Building the tree

It can be split into $n$ point updates, a $\Theta(n\log^2n)$ construction.

There is also a $\Theta(n)$ construction; see the first method in the section [$\Theta(n)$ tree construction](#thetan-tree-construction) on this page.

## Tricks

### $\Theta(n)$ tree construction

Using the example of maintaining range sums.

First method:

The value of each vertex is obtained by summing the values of all children directly connected to it. Therefore we can consider the contributions in reverse: each time the value of a child is determined, we update its direct parent with its own value.

???+ note "Implementation"
    === "C++"
        ```cpp
        // Θ(n) tree construction
        void init() {
          for (int i = 1; i <= n; ++i) {
            t[i] += a[i];
            int j = i + lowbit(i);
            if (j <= n) t[j] += t[i];
          }
        }
        ```
    
    === "Python"
        ```python
        # Θ(n) tree construction
        def init():
            for i in range(1, n + 1):
                t[i] = t[i] + a[i]
                j = i + lowbit(i)
                if j <= n:
                    t[j] = t[j] + t[i]
        ```

Second method:

We have already said that $c[i]$ represents the range $[i-\operatorname{lowbit}(i)+1, i]$; therefore we can first preprocess the prefix-sum array $\mathrm{sum}$ and then compute the array $c$.

???+ note "Implementation"
    === "C++"
        ```cpp
        // Θ(n) tree construction
        void init() {
          for (int i = 1; i <= n; ++i) {
            t[i] = sum[i] - sum[i - lowbit(i)];
          }
        }
        ```
    
    === "Python"
        ```python
        # Θ(n) tree construction
        def init():
            for i in range(1, n + 1):
                t[i] = sum[i] - sum[i - lowbit(i)]
        ```

### Timestamp optimization

A very common trick for problems with multiple test cases. If we brute-force cleared the Fenwick tree for every new test case, we might exceed the time limit. Therefore we use a mark $\mathrm{tag}$ that records when a vertex was last used (i.e. in which test case it was last used). At every operation we compare the time in $\mathrm{tag}$ at that position with the current time, and thus determine whether that position should be $0$ or the value from the array.

???+ note "Implementation"
    === "C++"
        ```cpp
        // timestamp optimization
        int tag[MAXN], t[MAXN], Tag;
        
        void reset() { ++Tag; }
        
        void add(int k, int v) {
          while (k <= n) {
            if (tag[k] != Tag) t[k] = 0;
            t[k] += v, tag[k] = Tag;
            k += lowbit(k);
          }
        }
        
        int getsum(int k) {
          int ret = 0;
          while (k) {
            if (tag[k] == Tag) ret += t[k];
            k -= lowbit(k);
          }
          return ret;
        }
        ```
    
    === "Python"
        ```python
        # timestamp optimization
        tag = [0] * MAXN
        t = [0] * MAXN
        Tag = 0
        
        
        def reset():
            Tag = Tag + 1
        
        
        def add(k, v):
            while k <= n:
                if tag[k] != Tag:
                    t[k] = 0
                t[k] = t[k] + v
                tag[k] = Tag
                k = k + lowbit(k)
        
        
        def getsum(k):
            ret = 0
            while k:
                if tag[k] == Tag:
                    ret = ret + t[k]
                k = k - lowbit(k)
            return ret
        ```

## Example problems

-   [Fenwick tree 1: point update, range query](https://loj.ac/problem/130)
-   [Fenwick tree 2: range update, point query](https://loj.ac/problem/131)
-   [Fenwick tree 3: range update, range query](https://loj.ac/problem/132)
-   [Two-dimensional Fenwick tree 1: point update, range query](https://loj.ac/problem/133)
-   [Two-dimensional Fenwick tree 2: range update, point query](https://loj.ac/problem/134)
-   [Two-dimensional Fenwick tree 3: range update, range query](https://loj.ac/problem/135)
