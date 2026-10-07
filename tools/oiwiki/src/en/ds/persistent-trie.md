---
title: Persistent trie
---

## Introduction

A persistent trie is built in the same way as a persistent segment tree: on every modification only the nodes that are added or whose values change are modified, while the unchanged nodes are kept and linked to from the previous version, so that the trie reachable from the root of every version is complete and contains all the information.

In most persistent-trie problems, the trie appears in the form of a [01-trie](../string/trie.md#maintaining-xor-extremes).

??? note "Example problem [Maximum XOR Sum](https://www.luogu.com.cn/problem/P4735)"
    Maintain the following operations on an array $a$ of length $n$:
    
    1.  Append a number $x$ to the end of the array; the length $n$ increases by $1$.
    2.  Given a query interval $[l,r]$ and a value $k$, find the maximum of $k \oplus \bigoplus^{n}_{i=p} a_i$ over $l\le p\le r$.

## Procedure

The value to compute is a bit awkward. Using the usual trick for XORs of consecutive elements, let $s_x=\bigoplus_{i=1}^x a_i$; then the original expression equals $s_{p-1}\oplus s_n\oplus k$. Note that $s_n \oplus k$ is fixed during a query, so the query becomes: find the maximum XOR with a fixed value ($s_n\oplus k$) over the interval $[l-1,r-1]$.

Continuing along the lines of the persistent segment tree, consider the case where every query covers the whole interval. Then it suffices to build a trie over that interval, insert every number of the interval into it, and during a query jump, whenever possible, to the bit different from the current one.

To query an interval we use the idea of prefix sums and differences: the trie of the interval is obtained by "subtracting" two prefix tries (that is, two historical versions obtained by adding the numbers in order). In addition, in the spirit of dynamically created nodes, we do not add nodes that have never been computed, which reduces the memory usage.

```cpp
--8<-- "docs/ds/code/persistent-trie/persistent-trie_1.cpp"
```
