---
title: Closest pair of points in the plane
---

## Introduction

Given $n$ points in the two-dimensional plane, find a pair of points with the smallest Euclidean distance.

Below we present a divide-and-conquer algorithm with time complexity $O(n\log n)$ that solves this problem. The algorithm was proposed in 1975 by [Franco P. Preparata](https://en.wikipedia.org/wiki/Franco_P._Preparata), and Preparata and [Michael Ian Shamos](https://en.wikipedia.org/wiki/Michael_Ian_Shamos) proved that it is optimal in the decision tree model.

## Procedure

As with ordinary divide-and-conquer algorithms, we split this set of $n$ points into two sets $S_1, S_2$ of equal size and keep recursing. But we run into a difficulty: how do we merge? That is, how do we find the closest pair of points with one point in $S_1$ and the other in $S_2$? For now, assume the merge operation takes $O(n)$ time; then the total complexity of the algorithm is $T(n) = 2T(\frac{n}{2}) + O(n) = O(n\log n)$.

We first sort all points with $x_i$ as the first key and $y_i$ as the second key, and use the point $p_m (m = \lfloor \frac{n}{2} \rfloor)$ as the dividing point to split the point set into $A_1,A_2$:

$$
\begin{aligned}
A_1 &= \{p_i \ \big | \ i = 0 \ldots m \}\\
A_2 &= \{p_i \ \big | \ i = m + 1 \ldots n-1 \}
\end{aligned}
$$

and recurse, finding the closest pair inside each of the two point sets; let the distances be $h_1,h_2$ and let $h$ be the smaller of the two.

Now it is time to merge! We try to find a pair of points, one belonging to $A_1$ and the other to $A_2$, whose distance is less than $h$. Therefore we put all points whose x coordinate differs from $x_m$ by less than $h$ into the set $B$:

$$
B = \{ p_i \ \big | \ \lvert x_i - x_m \rvert < h \}
$$

Looking at the figure, the line $m$ divides the points into two parts. To the left of $m$ is the point set $A_1$, and to the right is the point set $A_2$.

Then, by the rule $B = \{ p_i \ \big | \ \lvert x_i - x_m \rvert < h \}$, we obtain the point set $B$ consisting of the green points.![nearest-points1](./images/nearest-points1.png)

For each point $p_i$ in $B$, our current goal is to find a point that is also in $B$ and whose distance to it is less than $h$. To avoid considering two points with respect to each other twice, we only consider points whose y coordinate is less than $y_i$. Obviously, for a valid point $p_j$, $y_i - y_j$ must be less than $h$. Thus we obtain a set $C(p_i)$:

$$
C(p_i) = \{ p_j\ \big |\ p_j \in B,\ y_i - h < y_j \le y_i \}
$$

Pick a point $p_i$ in the point set $B$; by the rule $C(p_i) = \{ p_j\ \big |\ p_j \in B,\ y_i - h < y_j \le y_i \}$ we obtain the point set $C$ consisting of the yellow points inside the red rectangle.

![nearest-points2](./images/nearest-points2.png)

If we sort the points of $B$ by $y_i$, $C(p_i)$ is very easy to obtain: it is a few consecutive points immediately adjacent to $p_i$.

This gives us the steps of the merge:

1.  Build the set $B$.
2.  Sort the points of $B$ by $y_i$. The usual approach takes $O(n\log n)$, but we can change the strategy to optimize it to $O(n)$ (explained below).
3.  For each $p_i \in B$ consider $p_j \in C(p_i)$; for each pair $(p_i,p_j)$ compute the distance and update the answer (the closest pair of points in the set currently being processed).

Note that we mentioned sorting twice above. Since the point coordinates never change, the first sort can be done only once, before the divide and conquer starts. We let each recursive call return the current point set sorted by $y_i$; for the second sort, the upper level simply merges the two separately sorted point sets of the lower level.

It seems that this algorithm is still not good enough: $|C(p_i)|$ will be of order $O(n)$, making the total complexity wrong. In fact this is not the case — its maximum size is $7$, and we give the proof:

## Complexity proof

We already know that the y coordinates of all points in $C(p_i)$ lie in the range $(y_i-h,y_i]$, and that the x coordinates of all points in $C(p_i)$, as well as of $p_i$ itself, lie in the range $(x_m-h,x_m+h)$. This forms a $2h \times h$ rectangle.

We split this rectangle into two $h \times h$ squares. Ignoring $p_i$, the points in one square are $C(p_i) \cap A_1$ and the points in the other are $C(p_i) \cap A_2$, and the distance between any two points inside the same square is greater than $h$. (Because they come from the same lower level of the recursion.)

We split an $h \times h$ square into four small $\frac{h}{2} \times \frac{h}{2}$ squares. We can see that each small square contains at most $1$ point: the maximum distance between any two points in such a small square is the length of its diagonal, i.e. $\frac{h}{\sqrt 2}$, which is less than $h$.

![nearest-points3](./images/nearest-points3.png)

Hence each square contains at most $4$ points, the rectangle contains at most $8$ points, and after removing $p_i$ itself, $\max(C(p_i))=7$.

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/geometry/code/nearest-points/nearest-points_1.cpp"
    ```

## Generalization: minimum-perimeter triangle in the plane

The algorithm above generalizes in an interesting way to the following problem: among a given set of points, choose three points such that the sum of their pairwise distances is minimal.

The algorithm stays essentially the same: each time we try to find a triangle with perimeter smaller than the current answer $d$, put all points whose x coordinate differs from $x_m$ by less than $\frac{d}{2}$ into the set $B$, and try to update the answer. (The longest side of a triangle with perimeter $d$ is less than $\frac{d}{2}$.)

## Non-divide-and-conquer algorithm

In fact, besides the divide-and-conquer algorithm above, there is another, non-divide-and-conquer algorithm with the same time complexity $O(n \log n)$.

We can use a common idea for processing sequences: for each element, add to the answer the contribution of it together with all elements to its left. The same idea can be applied to the closest pair of points problem in the plane.

Specifically, we sort all points with $x_i$ as the first key and $y_i$ as the second key, and build a multiset keyed by $y_i$. For each position $i$ we perform the following operations:

1.  Delete from the set all points satisfying $x_i - x_j \ge d$. They can no longer contribute to the answer.
2.  For all points in the set satisfying $\lvert y_i - y_j \rvert < d$, compute their distance to $p_i$.
3.  Insert $p_i$ into the set.

Since each point is inserted and deleted at most once, the time complexity of inserting and deleting points is $O(n \log n)$, and the proof of the time complexity of the answer-counting part is similar to the complexity proof of the divide-and-conquer algorithm; the reader may try it.

??? example "Reference implementation"
    ```cpp
    --8<-- "docs/geometry/code/nearest-points/nearest-points_2.cpp"
    ```

## Expected linear-time approach

In fact, besides the approaches above with time complexity $O(n \log n)$, there is also an algorithm with **expected** complexity $O(n)$.

First [randomly shuffle](../misc/random.md#shuffle) the points; we will maintain the answer for a prefix of the point set. Consider how to obtain the answer for the $i$-th point from the first $i - 1$ points.

Let $s$ be the closest-pair distance among the first $i - 1$ points. We divide the plane into a grid of cells with side length $s$ and store the points inside each cell (using a [hash table](../ds/hash.md)), then check all points in the nine cells around the cell containing the $i$-th point and update the answer. Note that the number of points to check is $O(1)$, because the closest-pair distance among the first $i - 1$ points is $s$, so each cell contains at most $4$ points.

If the answer is updated during this process, we rebuild the grid; otherwise we do not. Among the first $i$ points, the probability that the closest pair contains $i$ is $O\left(\frac{1}{i}\right)$, while the cost of rebuilding the grid is $O(i)$, so the expected cost for the $i$-th point is $O(1)$. Therefore, for $n$ points, the expected complexity of this algorithm is $O(n)$.

## Exercises

-   [UVa 10245 "The Closest Pair Problem"\[difficulty: low\]](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1186)
-   [SPOJ #8725 CLOPPAIR "Closest Point Pair"\[difficulty: low\]](https://www.spoj.com/problems/CLOPPAIR/)
-   [CODEFORCES Team Olympiad Saratov - 2011 "Minimum amount"\[difficulty: medium\]](http://codeforces.com/contest/120/problem/J)
-   [SPOJ #7029 CLOSEST "Closest Triple"\[difficulty: medium\]](https://www.spoj.com/problems/CLOSEST/)
-   [Google Code Jam 2009 Final "Min Perimeter"\[difficulty: medium\]](https://github.com/google/coding-competitions-archive/blob/main/codejam/2009/world_finals/min_perimeter/statement.pdf)

## References and further reading

**The divide-and-conquer part of this page is mainly translated from the blog post [Нахождение пары ближайших точек](http://e-maxx.ru/algo/nearest_points) and its English translation [Finding the nearest pair of points](https://github.com/e-maxx-eng/e-maxx-eng/blob/master/src/geometry/nearest_points.md). The Russian version is licensed under Public Domain + Leave a Link; the English version is licensed under CC-BY-SA 4.0.**

[Zhihu column: Computational Geometry – The Closest Pair Problem](https://zhuanlan.zhihu.com/p/74905629)
