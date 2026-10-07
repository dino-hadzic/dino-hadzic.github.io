---
title: Cat tree
---

## Introduction

It is well known that a segment tree supports fast queries for the "sum" of information over an interval, such as the maximum subarray sum, the interval sum, the product of a sequence of matrices in an interval, and so on.

The problem, however, is that the range query of an ordinary segment tree may still be a bit slow in the eyes of some evil problem setters.

Simply put, building a segment tree requires $O(n)$ merge operations, and every range query requires $O(\log{n})$ merge operations. When querying something like an interval sum this is still tolerable, but when we need to query a range matrix product, where one merge (i.e. one matrix multiplication) has complexity as high as $O(k^3)$, even $O(\log{n})$ merges are sometimes unacceptable time-wise.

The so-called "cat tree" is a static segment tree that does not support updates and only supports fast range queries. The approach is only worthwhile when the number of queries is large ($m=\Omega(n)$).

Building such a static segment tree requires $O(n\log{n})$ merge operations, but the query complexity is accelerated to $O(1)$ merge operations.

When handling information with expensive merges such as matrix multiplication, the cat tree reduces the complexity of a single query from $O(k^3 \log n)$ to $O(k^3)$.

Note that for static range linear-basis queries, although the cat tree can improve the complexity of the range linear basis implemented with an ordinary segment tree, there is an approach with better time and space complexity: the [prefix linear basis](../math/linear-algebra/basis.md#拓展前缀线性基). Moreover, an ordinary segment tree can handle dynamic range linear-basis problems, while for static range linear-basis queries the cat tree is not only more complex to implement and not optimal, but also offers no functional advantage.

## Principle

When querying the "sum" of information over the interval $[l,r]$, find the LCA in the segment tree of the node representing $[l,l]$ and the node representing $[r,r]$. Let this node $p$ represent the interval $[L,R]$; we find some very interesting properties:

1.  The interval $[L,R]$ certainly contains $[l,r]$. Obviously, since it is an ancestor of both $l$ and $r$.

2.  The interval $[l,r]$ certainly crosses the midpoint of $[L,R]$. Since $p$ is the LCA of $l$ and $r$, the left child of $p$ is an ancestor of $l$ but not of $r$, and the right child of $p$ is an ancestor of $r$ but not of $l$. Therefore $l$ must lie in the interval $[L,\mathit{mid}]$ and $r$ must lie in the interval $(\mathit{mid},R]$.

With these two properties we can reduce the query complexity to $O(1)$.

## Implementation

Specifically, when building the tree, for a node of the segment tree let its interval be $(l,r]$.

Unlike a traditional segment tree, which keeps only the sum of $[l,r]$ in this node, we additionally store in this node the suffix-sum array of $(l,\mathit{mid}]$ and the prefix-sum array of $(\mathit{mid},r]$.

Then the build complexity is $T(n)=2T(n/2)+O(n)=O(n\log{n})$, and likewise the space complexity grows from the original $O(n)$ to $O(n\log{n})$.

Now the most important part: the query.

If the queried interval is $[l,r]$, find the LCA of the node representing $[l,l]$ and the node representing $[r,r]$, and call it $p$.

By the two properties just described, $l,r$ lie within the interval of $p$ and certainly cross the midpoint of $p$.

This means a very crucial fact: we can use the prefix-sum and suffix-sum arrays in $p$ to split $[l,r]$ into $[l,\mathit{mid}]+(\mathit{mid},r]$ and thus assemble the interval $[l,r]$.

And this procedure needs only $O(1)$ merge operations!

But it seems we have overlooked something?

The complexity of finding the LCA does not seem to be $O(1)$: brute force is $O(\log{n})$, binary lifting is $O(\log{\log{n}})$, and switching to a sparse table is too expensive...

## Heap-style construction

Specifically, we pad the sequence to a power of $2$ and then build the segment tree.

Now we find that the index of the LCA of two nodes in the segment tree is exactly the longest common prefix (LCP) of the binary representations of the two node indices.

A moment's thought shows that, in binary, for $x$ and $y$ we have `lcp(x,y)=x>>digits[x^y]`. (Here `digits[x]` denotes the number of binary digits of $x$, i.e. $\lfloor \log_2 x \rfloor+1$.)

So precomputing a `digits` array makes finding the LCA trivial.

Thus we have built a cat tree.

Since building involves computing prefix sums and suffix sums, for information with merge complexity $O(k^3)$ such as matrix multiplication the build complexity is $O(n\log n \cdot k^3)$. On this basis, the cat tree reduces the complexity of a single static range matrix product query from $O(k^3 \log n)$ to $O(k^3)$, so that when the number of queries is large ($m=\Omega(n)$), the total complexity of handling $m$ queries is improved from $O(n \cdot k^3 + m \cdot k^3 \log n)$ to $O(n\log n \cdot k^3 + m \cdot k^3)$.

### References

-   [immortalCO's blog (Chinese)](https://immortalco.blog.uoj.ac/blog/2102)
-   [\[Kle77\]](http://ieeexplore.ieee.org/document/1675628/) V. Klee, "Can the Measure of be Computed in Less than O (n log n) Steps?," Am. Math. Mon., vol. 84, no. 4, pp. 284–285, Apr. 1977.
-   [\[BeW80\]](https://www.tandfonline.com/doi/full/10.1080/00029890.1977.11994336) Bentley and Wood, "An Optimal Worst Case Algorithm for Reporting Intersections of Rectangles," IEEE Trans. Comput., vol. C–29, no. 7, pp. 571–577, Jul. 1980.
