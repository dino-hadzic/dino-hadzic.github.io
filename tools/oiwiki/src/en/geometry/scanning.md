---
title: Sweep line
---

## Introduction

The sweep line is usually applied to geometric figures; quite literally, it is a line that sweeps back and forth across the whole figure. It is generally used to solve problems about the area and perimeter of figures, 2D point counting, and so on.

## Area of the union of rectangles in the plane

In a two-dimensional coordinate system, the lower-left and upper-right corners of several rectangles are given; find the area of the figure formed by all the rectangles.

### Procedure

From the picture it is clear that the total area can be computed directly by brute force. What if the data are large? This is where the **sweep line** algorithm comes in.

Now suppose we have a line that starts at the bottom and sweeps upward:

![](./images/scanning.svg)

As shown in the figure, the whole figure is divided into small rectangles of different colors; the height of a small rectangle is the distance swept, but the horizontal width keeps changing.

Mark the bottom and top edges of every rectangle: the bottom edge is marked 1 and the top edge -1. Whenever a horizontal edge is encountered, add the mark of that edge to the weight of the edge (over its projection onto the horizontal axis).

???+ note "Note"
    This operation resembles traversing a bracket sequence: an opening bracket adds 1, a closing bracket subtracts 1; the "weight" corresponds to the current depth, and whether the "weight" is greater than 0 corresponds to whether we are currently inside brackets, i.e. whether this interval counts toward the width of the small rectangle.

The width of the small rectangles (there may be more than one) is the total length of the intervals on the number line whose weight is greater than 0.

### Implementation

Use a segment tree to maintain the length of the rectangles, i.e. the points on the number line whose cover count is greater than 0. The requirements are:

-   add 1 or subtract 1 on an interval;
-   over the whole number line, compute the "total length of intervals" whose weight is greater than 0.

If you try to implement this directly with an ordinary segment tree template, you may run into some trouble. Specifically, during a range add, even when the modified range coincides with the node's range, we still cannot know in constant time how the cover count changes. This is because we cannot directly know how much length inside the node's range changes from 1 to 0 (or from 0 to 1).

This problem can be solved with plain divide and conquer: for every node maintain two pieces of information, "the number of times its whole range is covered `v[]`" (similar to a lazy tag that never needs to be pushed down) and "the covered length `w[]`".

[Coordinate compression](../misc/discrete.md) is required.

??? note "[Luogu P5490 [Template] Sweep Line & Union Area of Rectangles](https://www.luogu.com.cn/problem/P5490) reference code"
    ```cpp
    --8<-- "docs/geometry/code/scanning/scanning_1.cpp"
    ```

??? note "["POJ 1151" Atlantis](http://poj.org/problem?id=1151) reference code"
    ```cpp
    --8<-- "docs/geometry/code/scanning/scanning_2.cpp"
    ```

### Exercises

-   ["POJ1177" Picture](http://poj.org/problem?id=1177)
-   ["POJ3832" Posters](http://poj.org/problem?id=3832)
-   [Luogu P1856 \[IOI1998\] \[USACO5.5\] Rectangle Perimeter Picture](https://www.luogu.com.cn/problem/P1856)
    -   The contribution of horizontal edges is the change in covered length.
    -   Computing the two directions separately avoids a case analysis for vertical edges.
    -   When sorting the operations, take care of the case where edges of two rectangles coincide.
    -   The constraints allow skipping the segment tree and simulating directly in quadratic time.

## B-dimensional orthogonal range

A B-dimensional orthogonal range is the set of points in a B-dimensional rectangular coordinate system whose $i$-th coordinate lies in an integer range $[l_i,r_i]$.

Generally, a one-dimensional orthogonal range is simply called an interval, a two-dimensional one a rectangle, and a three-dimensional one a cuboid (what we usually call 2D point counting is a two-dimensional orthogonal range).

For a static two-dimensional problem, we can sweep one dimension with a sweep line and maintain the other with a data structure.
As the sweep line moves from left to right, modifications and queries occur in the dimension maintained by the data structure.
If the queried information is differentiable (can be split into differences), use differences directly; otherwise divide and conquer is needed. Differences are usually maintained with a Fenwick tree or a segment tree, but since the Fenwick tree is easier to write and has a small constant factor, most people choose the Fenwick tree. The divide and conquer is usually CDQ divide and conquer (but divide and conquer is not covered here).

Another, easier-to-understand way to look at the problem is from the perspective of a sequence rather than a two-dimensional plane. Viewed this way, the sweep line actually enumerates the right endpoint $r=1\cdots n$ and maintains a data structure that, for the current $r$ and a given value $l$, answers what the answer from $l$ to $r$ is. That is, the sweep line sweeps over the right endpoints of the queries while the data structure maintains the answers for all left endpoints; in other words, we traverse one dimension and the data structure maintains the other.

The complexity is usually $O((n+m)\log n)$.

## 2D point counting

Given a sequence of length $n$ and $m$ queries, each query asks for the number of elements in the interval $[l,r]$ whose value lies in $[x,y]$.

This problem is called 2D point counting. It is easy to see that it is equivalent to querying the number of points inside a rectangle in the plane. Here we describe the simplest way to handle this problem: sweep line + Fenwick tree.

Obviously, this is a static two-dimensional problem; with a sweep line we can turn the static two-dimensional problem into a dynamic one-dimensional problem. The dynamic one-dimensional problem is maintained with a data structure over the sequence; here a Fenwick tree can be used.

First compress the coordinates of all queries and maintain the values with a Fenwick tree. For the $l$ and $r$ of each query, when the enumeration reaches $l-1$, count the number $a$ of values currently in the interval $[x,y]$; continue enumerating, and when it reaches $r$, count the number $b$ of values currently in the interval $[x,y]$. Then $b-a$ is the answer to that query.

### Examples

???+ note "[Luogu P2163 \[SHOI2007\] The Gardener's Trouble](https://www.luogu.com.cn/problem/P2163)"
    First compress the coordinates. Suppose the rectangle with lower-left corner $(0, 0)$ and upper-right corner $(x, y)$ contains $ans_{x, y}$ points. Then the answer to a query can be split into differences as $ans_{c, d} - ans_{a - 1, d} - ans_{c, b - 1} + ans_{a - 1, b - 1}$.
    
    ??? note "Code"
        ```cpp
        --8<-- "docs/geometry/code/scanning/scanning_3.cpp"
        ```

???+ note "[Luogu P1908 Inversions](https://www.luogu.com.cn/problem/P1908)"
    Yes, inversions can also be counted with the sweep line idea. Transform counting inversions into: enumerate each position $i$ from back to front and count the points in the interval $[i+1,n]$ whose value lies in the interval $[0,a_i]$. The values in the problem go up to $10^9$, so obviously coordinate compression is needed first. We traverse the array from back to front; each time we reach a number we update the Fenwick tree (segment tree), and then count how many numbers so far are smaller than the current one. Since we traverse from back to front, the number of values smaller than the current one is exactly the number of inversions it forms; point update and range query with a Fenwick tree or segment tree suffice.
    
    ??? note "Code"
        ```cpp
        --8<-- "docs/geometry/code/scanning/scanning_4.cpp"
        ```

???+ note "[Luogu P1972 \[SDOI2009\] HH's Necklace](https://www.luogu.com.cn/problem/P1972)"
    Brief statement: given a sequence, answer many queries asking how many distinct values appear in the interval $[l,r]$.
    
    For this kind of problem we can derive some properties and then use a sweep line to enumerate all right endpoints while a data structure maintains the answer for every left endpoint; we can also transform the problem onto the two-dimensional plane, where it becomes a rectangle query.
    
    In this problem, let $pre_i$ be the position of the previous occurrence of $a_i$ in the sequence; if $a_i$ has not appeared before, $pre_i = 0$. By the statement, if a value appears several times in the interval, it contributes only once. Let us agree that each value contributes at its first occurrence in the interval; then the total contribution is the number of $x$ with $pre_x \le l - 1$, which is easily proved by contradiction.
    
    The problem is now: given a sequence $pre$, answer many queries asking how many $i$ in the interval $[l,r]$ satisfy $pre_i \le l - 1$.
    
    We can regard $pre_i$ as a point in the plane: $i$ is the x coordinate and $pre_i$ the y coordinate. The problem becomes 2D point counting: for each query, how many points lie in the rectangle with lower-left corner $(l,0)$ and upper-right corner $(r,l - 1)$.
    
    Note that this query is differentiable: we can split it into the number of points in the rectangle with lower-left corner $(0,0)$ and upper-right corner $(r,l - 1)$ minus the number of points in the rectangle with lower-left corner $(0,0)$ and upper-right corner $(l - 1,l - 1)$, which makes it convenient to apply the sweep line idea.
    
    Each operation costs $O(\log n)$; there are $n$ add-point operations and $2m$ query operations in total, so the total time complexity is $O((n + m) \log n)$.
    
    ??? note "Code"
        ```cpp
        --8<-- "docs/geometry/code/scanning/scanning_5.cpp"
        ```

### Exercises

-   [Luogu P8593 "KDOI-02" One Shot](https://www.luogu.com.cn/problem/P8593) an application of inversions.
-   [AcWing 4709. Triples](https://www.acwing.com/problem/content/4712/) an easier version of the previous problem, also an application of inversions.
-   [Luogu P8773 \[Lanqiao Cup 2022 Provincial A\] Choose Numbers XOR](https://www.luogu.com.cn/problem/P8773) a modified version of HH's Necklace.
-   [Luogu P8844 \[Chuanzhi Cup #4 Preliminary\] Xiao Ka and the Fallen Leaves](https://www.luogu.com.cn/problem/P8844) a tree problem turned into a sequence problem, followed by 2D point counting.

In short, the main idea of 2D point counting is to maintain one dimension with a data structure and enumerate the other.

## References

-   [cnblogs/Yang1208: sweep line explanation, segment tree with dynamic node creation](https://www.cnblogs.com/yangsongyi/p/8378629.html)
-   [csdn/riba2534: POJ1151 Atlantis solution](https://blog.csdn.net/riba2534/article/details/76851233)
-   [csdn/刀刀狗 0102: POJ1151 Atlantis solution](https://blog.csdn.net/winddreams/article/details/38495093)
-   [A brief discussion of sweep lines](https://www.luogu.com.cn/article/f8q5bmnz)
