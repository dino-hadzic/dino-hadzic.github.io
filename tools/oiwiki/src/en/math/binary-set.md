---
title: Binary set operations
---

Prerequisites: [Bitwise operations](./bit.md#bitwise-operations), [Integers and bit sequences](./bit.md#integers-and-bit-sequences).

The binary representation of a number can be viewed as a set ($0$ means the element is not in the set, $1$ means it is). For example, the set $\{1,3,4,8\}$ can be represented as $(100011010)_2$. The corresponding bitwise operations can then be viewed as operations on sets.

| Operation   |    Set notation     |         Bitwise notation          |
| ------ | :-------------: | :-------------------------: |
| intersection   |   $a \cap b$    | $a \operatorname{AND} b$ |
| union   |   $a \cup b$    | $a \operatorname{OR} b$ |
| complement   |    $\bar{a}$    | $\operatorname{NOT} a$ (the universal set has all bits equal to 1) |
| difference   | $a \setminus b$ | $a \operatorname{AND} \operatorname{NOT} b$ |
| symmetric difference | $a\triangle b$  | $a \operatorname{XOR} b$  |

Before we move on to traversing the subsets of a set, let us look at some examples of applications of bitwise operations.

### Modulo a power of 2

Taking a number modulo a nonnegative integer power of $2$ is equivalent to taking the last several bits of the number's binary representation, which is equivalent to an AND with $mod-1$.

=== "C++"
    ```cpp
    int modPowerOfTwo(int x, int mod) { return x & (mod - 1); }
    ```

=== "Python"
    ```python
    def modPowerOfTwo(x, mod):
        return x & (mod - 1)
    ```

It follows that a nonnegative integer power of $2$ taken modulo itself gives $0$, i.e., if $n$ is a nonnegative integer power of $2$, the result of the AND of $n$ and $n-1$ is $0$.

In fact, for a positive integer $n$, $n-1$ clears the lowest $1$ bit of $n$ and sets all the following bits to $1$. Therefore, the AND of $n$ and $n-1$ is equivalent to deleting the lowest $1$ bit of $n$.

This lets us check whether a number is a nonnegative integer power of $2$: $n$ is a nonnegative integer power of $2$ if and only if the binary representation of $n$ contains exactly one $1$.

=== "C++"
    ```cpp
    bool isPowerOfTwo(int n) { return n > 0 && (n & (n - 1)) == 0; }
    ```

=== "Python"
    ```python
    def isPowerOfTwo(n):
        return n > 0 and (n & (n - 1)) == 0
    ```

### Traversing subsets

Traversing all subsets of a set represented by a binary number is equivalent to enumerating all submasks of the mask corresponding to that binary number.

A mask is a string of bits that is ANDed with a source string to obtain a new operand in which several input bits of the source string are masked out.

A mask acts as a screen on the source string: a $1$ bit in the mask means the corresponding bit of the source is kept, and a $0$ bit in the mask means the corresponding bit of the source is set to $0$. Changing several $1$ bits of a mask to $0$ bits gives a submask of the mask; the mask itself is also its own submask.

Given a mask $m$, we want to efficiently iterate over all submasks $s$ of $m$; we can consider an implementation based on bitwise tricks.

```cpp
// traverse the non-empty subsets of m in descending order
int s = m;
while (s > 0) {
  // s is a non-empty subset of m
  s = (s - 1) & m;
}
```

Or using a more compact for statement:

```cpp
// traverse the non-empty subsets of m in descending order
for (int s = m; s; s = (s - 1) & m)
// s is a non-empty subset of m
```

Neither of these two pieces of code handles the submask equal to $0$; to handle the submask equal to $0$ other methods can be used, for example:

```cpp
// traverse the subsets of m in descending order
for (int s = m;; s = (s - 1) & m) {
  // s is a subset of m
  if (s == 0) break;
}
```

Next we prove that the code above visits all submasks of $m$, without repetition, and in descending order.

Suppose we have a current bitmask $s$ and want to move on to the next bitmask. Subtracting $1$ from the mask $s$ is equivalent to removing the rightmost set bit of $s$ and turning all bits to its right into $1$.

To make $s-1$ a new submask, we need to remove all the extra $1$ bits not contained in the mask $m$; this removal can be done with the bitwise operation `(s - 1) & m`.

These two steps are equivalent to cutting the mask $s-1$ down to the largest value that can be reached arithmetically, i.e., the next submask after $s$ in descending order.

Therefore, the algorithm generates all submasks of the mask in descending order, performing only two operations per iteration.

A special case is $s=0$. After performing $s-1$ we get $-1$, in which all bits are $1$. After the operation `(s - 1) & m` the new $s$ will equal $m$. Therefore, if the loop does not end at $s=0$, the algorithm's loop will never terminate.

Letting $\text{popcount}(m)$ denote the number of $1$s in the binary representation of $m$, this method traverses the subsets of the set $m$ in $O(2^{\text{popcount}(m)})$ time.

### Traversing the submasks of all masks

In problems using bitmask DP, we sometimes want to traverse all submasks of each mask:

```cpp
for (int m = 0; m < (1 << n); ++m)
  // traverse the non-empty subsets of m in descending order
  for (int s = m; s; s = (s - 1) & m)
// s is a non-empty subset of m
```

This traverses the subsets of every subset of a set of size $n$.

Next we prove that the time complexity of this operation is $O(3^n)$, where $n$ is the total number of bits of the mask, i.e., the total number of elements in the set.

Consider the $i$-th bit, i.e., the $i$-th element of the set; there are three cases:

- it is $0$ in the mask $m$, hence $0$ in the submask $s$, i.e., the element is in neither the big nor the small subset;
- it is $1$ in $m$ but $0$ in $s$, i.e., the element is only in the big subset, not in the small one;
- it is $1$ in both $m$ and $s$, i.e., the element is in both the big and the small subset.

There are $n$ bits in total, hence $3^n$ different combinations.

There is another way to prove it:

If the mask $m$ has $k$ $1$s, then it has $2^k$ submasks. For a given $k$ there are $\dbinom{n}{k}$ corresponding masks $m$, so the total number over all masks is:

$$
\sum_{k=0}^n \dbinom{n}{k} 2^k
$$

The sum above equals the expansion of $(1+2)^n$ by the binomial theorem, hence there are $3^n$ different combinations.

### References

**This page is mainly translated from the blog post [Перебор всех подмасок данной маски](http://e-maxx.ru/algo/all_submasks) and its English translation [Submask Enumeration](https://cp-algorithms.com/algebra/all-submasks.html). The Russian version is licensed under Public Domain + Leave a Link; the English version under CC-BY-SA 4.0.**

### Exercises

- [Atcoder - Close Group](https://atcoder.jp/contests/abc187/tasks/abc187_f)
- [Codeforces - Nuclear Fusion](http://codeforces.com/problemset/problem/71/E)
- [Codeforces - Sandy and Nuts](http://codeforces.com/problemset/problem/599/E)
- [UVa 1439 - Exclusive Access 2](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4185)
- [UVa 11825 - Hackers' Crackdown](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2925)
