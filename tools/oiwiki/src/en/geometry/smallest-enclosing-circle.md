---
title: Smallest enclosing circle
---

## Introduction

Given $n~(n\ge 1)$ points $P_1,P_2,\cdots,P_n$ in the plane, find a circle of minimum radius such that no point lies outside the circle. This circle is called the **smallest enclosing circle** (Minimum Enclosing Circle, MEC) of these points.

In this article we allow circles of radius $0$: when all points coincide at a single point $P$, we consider the smallest enclosing circle of these $n$ points to be the circle with center $P$ and radius $0$.

It is easy to see that the smallest enclosing circle is unique.

??? note "Proof"
    Suppose there are two different smallest enclosing circles with centers $O_1,O_2$ and the same radius $r$. Let $M$ be the midpoint of $O_1O_2$; then for every point $P$ we have
    
    $$
    \begin{aligned}
        |P-M|^2&=\frac{|P-O_1|^2+|P-O_2|^2}{2}-\frac{|O_1-O_2|^2}{4}\\
        &\le r^2-\frac{|O_1-O_2|^2}{4}<r^2.
    \end{aligned}
    $$
    
    Hence, with $M$ as the center we can construct an enclosing circle of smaller radius, a contradiction.
    
    ![](./images/smallest-enclosing-circle3.svg)

## Procedure

The common approach to the smallest enclosing circle problem is Welzl's algorithm[^welzl], which is based on the [randomized incremental algorithm](random-incremental.md). The core operation of the algorithm is: first shuffle the points randomly, then maintain the smallest enclosing circle of a point set while adding new points to the set one by one. Although the algorithm contains three nested loops, its expected time complexity is $O(n)$.

### Adding a point

We first consider what happens when a new point is added to the point set currently maintained. Let the current circle $C$ be the smallest enclosing circle of the processed point set, and now add the point $P$.

-   If $P$ is inside $C$ or on its circumference, $C$ is still the smallest enclosing circle.
-   If $P$ is outside $C$, then $P$ must lie on the circumference of the new smallest enclosing circle, so the problem can be reduced to the subproblem: given that $P$ is on the circumference, find the smallest enclosing circle.

??? tip "Why a new point outside the circle must lie on the circumference of the new circle"
    Let the centers of the old and new circles be $O_0,O_1$ and their radii $r_0,r_1$; then $r_0\le r_1$. Suppose $P$ lies strictly inside the new circle. For $0<t<1$, consider the circle $(O_t,r_t)$ satisfying
    
    $$
    O_t=(1-t)O_1+tO_0,\qquad r_t^2=(1-t)r_1^2+tr_0^2-t(1-t)|O_1-O_0|^2<r_1^2,
    $$
    
    and take $t$ sufficiently small so that $P$ is still inside the circle $(O_t,r_t)$. For any point $Q$ we have
    
    $$
    |Q-O_t|^2-r_t^2=(1-t)(|Q-O_1|^2-r_1^2)+t(|Q-O_0|^2-r_0^2).
    $$
    
    So the points of the old set are still covered by the circle $(O_t,r_t)$, and the points that were previously fixed simultaneously on the circumference of the circle $(O_0,r_0)$ and on the circumference of the circle $(O_1,r_1)$ are still on the circumference of the circle $(O_t,r_t)$. Since $P$ is inside the circle $(O_t,r_t)$, the circle $(O_t,r_t)$ is a valid enclosing circle, but we have $r_t<r_1$, contradicting the optimality of the new circle.
    
    ![](./images/smallest-enclosing-circle4.svg)

The conclusion above also applies when a new point is added while one or two points are already fixed on the circumference.

### Three nested loops

Next we consider the main body of Welzl's algorithm. We shuffle the input points uniformly at random, still denote them $P_1,P_2,\cdots,P_n$, and let $S_i=\{P_1,\cdots,P_i\}$, $S_0=\varnothing$. We maintain the current circle $C$; initially its center is $P_1$, its radius is $0$, and there are no fixed points on the circumference.

1.  (First loop) No points fixed on the circumference: enumerate $i=2,\cdots,n$ in order. If $P_i$ is already inside $C$, continue; otherwise fix $P_i$ on the circumference and recompute the smallest circle covering $S_{i-1}$.
2.  (Second loop) One fixed circumference point $P_i$: first set $C$ to the circle with diameter $P_iP_1$, then enumerate $j=2,\cdots,i-1$ in order. If $P_j$ is already inside $C$, continue; otherwise also fix $P_j$ on the circumference and recompute the smallest circle covering $S_{j-1}$.
3.  (Third loop) Two fixed circumference points $P_i,P_j$: first set $C$ to the circle with diameter $P_iP_j$, then enumerate $k=1,\cdots,j-1$ in order. If $P_k$ is already inside $C$, continue; otherwise update $C$ to the circumscribed circle of $\triangle P_iP_jP_k$.

Here "inside the circle" always includes the circumference, and the current circle in each line is the **smallest circle** satisfying the corresponding constraints. When the third loop ends, $S_{j-1}$ is covered, and together with $P_j$ on the circumference this is exactly the answer needed by the second loop; when the second loop ends, we likewise obtain the answer needed by the first loop. The feasibility of the inner loops is guaranteed by the outer loops, and it is easy to see that when the third loop updates, the three points $P_iP_jP_k$ are not collinear, so the algorithm is correct.

??? tip "Why the three points are not collinear when the third loop updates the smallest circle"
    Since $P_j$ was outside a circle passing through $P_i$, we have $P_i\ne P_j$. If $P_i,P_j,P_k$ are collinear and $P_k$ is outside the current circle $C$, then $P_k$ must lie outside the segment $P_iP_j$. We distinguish two cases:
    
    -   If $P_j$ lies between $P_i,P_k$, then when the second loop reached $P_j$, the current smallest circle passed through $P_i$ and covered $P_k$ in $S_{j-1}$, hence it also covered $P_j$ on the segment $P_iP_k$. This contradicts $P_j$ triggering the third loop.
    -   If $P_i$ lies between $P_j,P_k$, then when the first loop reached $P_i$, the current smallest circle covered $P_j,P_k$ in $S_{i-1}$, hence it also covered $P_i$ on the segment $P_jP_k$. This contradicts $P_i$ triggering the second loop.
    
    ![](./images/smallest-enclosing-circle5.svg)

### Computing the circumscribed circle

The computational geometry operations involved in Welzl's algorithm are fairly standard: mainly determining the position of a point relative to a circle, the circle with a given diameter defined by two points, and the circumscribed circle through three points. We skip the first two and focus on the third.

Given three non-collinear points $A=(x_A,y_A), B=(x_B,y_B), C=(x_C,y_C)$, the center of their circumscribed circle is the intersection of the perpendicular bisectors of the segments $AB$ and $AC$, which can be computed with the method in [Finding the intersection of two lines](./2d.md#finding-the-intersection-of-two-lines).

We can also set up and solve the equations directly. Let the circumcenter be $O=(x,y)$; then

$$
\begin{cases}
(x-x_A)^2+(y-y_A)^2=(x-x_B)^2+(y-y_B)^2,\\
(x-x_A)^2+(y-y_A)^2=(x-x_C)^2+(y-y_C)^2,
\end{cases}
$$

Let

$$
\begin{aligned}
A_1&=2(x_B-x_A),&B_1&=2(y_B-y_A),&C_1&=x_B^2+y_B^2-x_A^2-y_A^2,\\
A_2&=2(x_C-x_A),&B_2&=2(y_C-y_A),&C_2&=x_C^2+y_C^2-x_A^2-y_A^2,
\end{aligned}
$$

then

$$
x=\frac{C_1B_2-C_2B_1}{A_1B_2-A_2B_1},\quad y=\frac{A_1C_2-A_2C_1}{A_1B_2-A_2B_1}.
$$

After computing the center, take $r=|O-A|$. A nonzero denominator $A_1B_2-A_2B_1$ corresponds to the three points being non-collinear. When the three points are nearly collinear, the floating-point error of this method may be greatly amplified, which requires special attention in practice.

### Example

Let the points be $P_1=(-2,0)$, $P_2=(2,0)$, $P_3=(0,1)$, $P_4=(0,3)$. Denote by $C_i$ the smallest enclosing circle after processing the first $i$ points; the figure below shows the results of the outer loop. The solid blue line denotes the current circle, the gray dashed line the circle before the update, the solid orange point the point added in this round, and the hollow gray point a point not yet added.

![](./images/smallest-enclosing-circle1.svg)

Initially the radius is $0$. After adding $P_2$, the current enclosing circle has diameter $P_1P_2$. $P_3$ is inside the circle, so the circle does not change when it is added. $P_4$ lies outside the circle and a recomputation is required. After the recomputation, the center is $(0,5/6)$ and the radius is $13/6$; $P_1,P_2,P_4$ are on the circumference and $P_3$ is inside the circle.

Below we expand the recomputation process for $i=4$. The orange point denotes the point currently being checked, the purple outer ring marks the circumference points fixed in this loop level, whose set is denoted by $R$. The solid blue line and the gray dashed line denote the current circle and the circle from the previous step, respectively.

![](./images/smallest-enclosing-circle2.svg)

1.  $P_4$ is outside the old circle $C_3$; enter the second loop.
2.  Fix $P_4$ and first take the circle with diameter $P_4P_1$. When checking $j=2$, we find that $P_2$ is outside this circle; enter the third loop.
3.  Fix $P_4,P_2$ and set the current circle to the circle with diameter $P_4P_2$. When checking $k=1$, we find that $P_1$ is still outside the circle.
4.  Update to the circumscribed circle of $\triangle P_4P_2P_1$, completing the third loop. Back in the second loop, the point $P_3$ corresponding to $j=3$ is already inside the circle, so it is skipped, and we obtain $C_4$.

The temporary circles during the recomputation only need to satisfy the constraints of the current subproblem, so they do not necessarily cover all the points already processed at the upper level. For example, the circle in the second subfigure does not yet cover $P_2$, and the circle in the third subfigure does not yet cover $P_1$; this is exactly the reason for entering the next level or updating the circumscribed circle.

### Complexity analysis

From the procedure, the worst-case upper bound on the time complexity of this algorithm is $O(n^3)$, but the random shuffle reduces the probability of entering the inner loops, bringing the expected time complexity down to $O(n)$.

The smallest enclosing circle is determined by at most three points: when there is only one distinct point the radius is $0$; otherwise the smallest enclosing circle is determined by a pair of diameter endpoints or by three non-collinear points. After fixing one circumference point, at most two more points are needed to determine the optimal solution.

??? tip "Why at most two more points are needed after fixing one circumference point"
    Translate the fixed point to the origin. Let the center vector be $\vec{u}$; then the radius of the circle is $|\vec{u}|$. The condition that a point $x$ is covered is equivalent to
    
    $$
    |\vec{x}-\vec{u}|^2\le |\vec{u}|^2\iff 2\vec{u}\cdot \vec{x}\ge |\vec{x}|^2.
    $$
    
    Every point other than the origin imposes a half-plane constraint on the center; the feasible centers lie in the [intersection of these half-planes](./half-plane.md), and the optimal center is the point of this intersection closest to the origin. In two-dimensional space, keeping at most two active constraints is enough to keep this closest point unchanged.[^note1] Therefore, besides the fixed point, keeping at most two more input points suffices to keep the optimal solution unchanged.
    
    In the figure below, the blue region $H$ denotes all feasible centers, and the orange point $\vec{u}_*$ is the point of the region closest to the origin. Removing the constraints corresponding to the gray boundaries does not change the optimal center.
    
    ![](./images/smallest-enclosing-circle6.svg)

Therefore, a point whose removal changes the optimal circle must belong to every such set of determining points. With no fixed circumference point there are at most three such points; with one fixed circumference point there are at most two.

Now we perform a backward analysis. First fix $P_i$ and the unordered point set $S_j$ at some step of the second loop. Since the initial order is random, $P_j$ is effectively a point chosen uniformly at random from $S_j$. Adding $P_j$ triggers the third loop only if removing $P_j$ would change the constrained optimal circle, so the probability of triggering is at most $\min(1,2/j)$. The third-loop scan takes $O(j)$ time, so the expected time of the whole second loop is

$$
O(1)+\sum_{j=2}^{i-1}\left(O(1)+\frac{2}{j}\cdot O(j)\right)=O(i).
$$

Similarly, fix the unordered point set $S_i$ of the first loop; there are at most three points that trigger a second-loop recomputation, so the probability is at most $\min(1,3/i)$. After fixing this point, the relative order of the previous points is still random, so the conditional expected time of this recomputation is $O(i)$. Adding the cost of each check and the cost of the initial shuffle, the total expected time complexity is

$$
O(n)+\sum_{i=2}^{n}\left(O(1)+\min\left(1,\frac{3}{i}\right)\cdot O(i)\right)=O(n).
$$

## Example problem

???+ note "[Luogu P1742 最小圆覆盖 (Smallest Enclosing Circle)](https://www.luogu.com.cn/problem/P1742)"
    Given $N$ points, find the smallest circle containing all the points, and output the radius and the coordinates of the center.

The implementation below maintains the center and radius directly and shuffles the order of the points using `std::shuffle`. The three nested loops correspond to the subproblems with zero, one and two fixed circumference points described above, and `geto` computes the circumcenter of three points.

??? note "Reference implementation"
    ```cpp
    --8<-- "docs/geometry/code/smallest-enclosing-circle/smallest-enclosing-circle_1.cpp"
    ```

## Exercises

-   [「POI 2011」WYK-Plot](https://www.luogu.com.cn/problem/P3517)
-   [Library Checker - Minimum Enclosing Circle](https://judge.yosupo.jp/problem/minimum_enclosing_circle)

## References and notes

-   [Smallest-circle problem - Wikipedia](https://en.wikipedia.org/wiki/Smallest-circle_problem)
-   [Minimum Enclosing Circle - Algorithms for Competitive Programming](https://cp-algorithms.com/geometry/enclosing-circle.html)
-   [Computational Geometry Lecture 4: Smallest enclosing circles and more - University of Florida](https://www.cise.ufl.edu/~sitharam/COURSES/CG/kreveldnbhd.pdf)

[^welzl]: Welzl, E. (1991). Smallest enclosing disks (balls and ellipsoids). In: Maurer, H. (eds) New Results and New Trends in Computer Science. Lecture Notes in Computer Science, vol 555. Springer, Berlin, Heidelberg.

[^note1]: See the related content in [Linear programming](../math/linear-programming.md).
