---
title: Half-plane intersection
---

## Definition

### Half-plane

A line together with one of its sides. A half-plane is a point set, namely the point set formed by a line and one of its sides. When it contains the line itself, it is called a closed half-plane; when it does not, it is called an open half-plane.

Analytically it is usually written as $Ax+By+C\ge 0$.

In computational geometry it is represented by a vector; throughout a problem, the half-plane is consistently taken to be the left or the right side of the vector.

![Half-plane](./images/hpi1.svg)

### Half-plane intersection

The half-plane intersection is the intersection of several half-planes. Since half-planes are point sets, their intersection is again a point set. In the Cartesian coordinate system it encloses a region.

This closely resembles an ordinary linear programming problem: the resulting half-plane intersection is exactly the feasible region of linear programming. In general the half-plane intersection is bounded, and problems such as computing its area are often asked.

It can be understood as the intersection of the right sides of all vectors in a set of vectors, or as the solution of the following system of inequalities.

$$
\begin{cases}
A_1x+B_1y+C\ge 0\\
A_2x+B_2y+C\ge 0\\
\cdots
\end{cases}
$$

### Kernel of a polygon

If the segment connecting any point of a point set to any point of the polygon has no other intersection with the polygon, that point set is called the kernel of the polygon.

Treat each edge of the polygon as a vector, joined head to tail; then the intersection of the half-planes of these vectors that face the interior of the polygon is exactly the kernel of the polygon.

## Solution – the S&I algorithm

### Sorting by polar angle

The C language has a library function `atan2(double y,double x)` that returns $\theta\in (-\pi,\pi]$, $\theta =\arctan \frac{y}{x}$.

Call this function directly with the vector as its argument and sort using the return value as the key; this gives a new set of edges (vectors).

If, while sorting, we encounter collinear vectors (with the same direction), we take the one closer to the feasible region. For example, if two vectors have the same polar angle and we want the left half-plane of the vectors, we only need to keep the left vector. To decide, compare the start or end point of one vector with the other vector and check whether it lies on the left or on the right.

### Maintaining a monotonic queue

Since the half-plane intersection is a convex polygon, we need to maintain a convex hull. Because a vector added later can only affect the edges added first or the edges added last (the hull is connected at that point), we only need to delete elements from the front and the back of the queue, so a monotonic queue is used.

We iterate over the sorted vectors and maintain a separate array of intersection points. As soon as the queue contains more than 2 elements, intersection points appear between them.

For the current vector, if the previous intersection point lies on the **opposite side** of the half-plane represented by this vector, the previous edge becomes meaningless.

![Monotonic queue](./images/hpi2.svg)

As in the figure above, suppose we take the left half-plane of the vectors. After sorting by polar angle, the traversal order should be $\vec a\to\vec b\to\vec c$. When $\vec a$ and $\vec b$ enter the queue, a point $D$ appears in the intersection array (the intersection array stores, at the same index, the intersection of the vector in the queue with the previous vector).

Next, when we reach $\vec c$, we find that $D$ is on the right side of $\vec c$. And because **the polar angle of the vector that produced** $D$ **must be smaller than** that of $\vec c$, the vector that produced $D$ (namely $\vec b$) no longer affects the half-plane intersection.

There is another possible situation: near the end, a newly added vector may start affecting the queue from the front.

![Effect on the front of the queue](./images/hpi7.svg)

Again suppose we take the left half-plane of the vectors. After adding the vector $\vec f$, the first intersection point $G$ lies on the right side of $\vec f$; reading the criterion above in reverse, we see that the vector $\vec a$, i.e. the vector at the **front of the queue**, should be removed.

Finally, use the vector at the front of the queue to eliminate redundant vectors at the back. This is because the vectors at the front are constrained by later ones, while the vectors at the back are not. At this point they form a closed loop, so the vector at the front can constrain the vectors at the back.

### Obtaining the half-plane intersection

If the half-plane intersection is a convex $n$-gon, we end up with $n$ points in the intersection array. Connecting them head to tail gives an $n$-gon with a consistent orientation (clockwise or counterclockwise).

Its area can then be computed by triangulation. (Computing the area is the most basic way this is tested.)

Occasionally the half-plane intersection does not exist or has area 0; pay attention to the boundary cases.

### Remarks

When a vector appears that can pop all points out of the queue (i.e. all points in the queue are on its right side), we **must** process the back of the queue first and only then the front. Therefore, in the loop we first run the `--r;` part and then the `++l;` part; only then is it correct. The reason is as follows.

![](./images/hpi4.svg)

Normally, when we add an edge (vector $\vec w$) after the queue (whose order is $\left\{\vec{u},\vec{v}\right\}$), an intersection point $N$ appears that shrinks the region behind $\vec{v}$.

![](./images/hpi5.svg)

However, every operation is generic, so it may happen that the point $M$ gets "squeezed out".

![](./images/hpi6.svg)

If a vector $\vec a$ now appears such that $M$ lies on the right side of $\vec a$, $M$ has to leave the queue. If at this moment we start from the front of the queue with `++l`, we obviously enlarge the region. In fact, $M$ is determined jointly by $\vec u$ and $\vec v$, so we have to consider whether it is $\vec u$ or $\vec v$ that affects the current process. And because after sorting by polar angle the vectors are in counterclockwise order, the influence of $\vec v$ is greater.

As in the figure above, if $M$ is confirmed to be on the right side of $\vec a$, then the influence of $\vec v$ certainly contributes nothing to the answer of the half-plane intersection.

The reason we eliminate the front of the queue is that **the constraint of the current vector is stronger than that of the vector at the front**, and the precondition of this criterion is that the queue contains more than two segments (vectors); otherwise the situation above arises.

Therefore we must always eliminate from the back of the queue first and only then from the front.

???+ note "Code – comparison part"
    ```cpp
    friend bool operator<(seg x, seg y) {
      db t1 = atan2((x.b - x.a).y, (x.b - x.a).x);
      db t2 = atan2((y.b - y.a).y, (y.b - y.a).x);  // compute the polar angle
      if (fabs(t1 - t2) > eps)                      // if the polar angles differ
        return t1 < t2;
      return (y.a - x.a) * (y.b - x.a) >
             eps;  // determine which side of y vector x is on; the leftmost one comes first
    }
    ```

???+ note "Code – incremental part"
    ```cpp
    // pnt its(seg a,seg b) computes the intersection of segments a and b
    // s[] are the vectors sorted by polar angle
    // q[] is the queue of vectors
    // t[i] is the intersection of s[i-1] and s[i]
    // [Code style] the range of the queue is (l,r]
    // We compute the half-plane on the left side of the vectors
    int l = 0, r = 0;
    for (int i = 1; i <= n; ++i)
      if (s[i] != s[i - 1]) {
        // Note: the back of the queue must be checked first
        while (r - l > 1 && (s[i].b - t[r]) * (s[i].a - t[r]) >
                                eps)  // if the previous intersection is on the right of the vector, pop the back
          --r;
        while (r - l > 1 && (s[i].b - t[l + 2]) * (s[i].a - t[l + 2]) >
                                eps)  // if the first intersection is on the right of the vector, pop the front
          ++l;
        q[++r] = s[i];
        if (r - l > 1) t[r] = its(q[r], q[r - 1]);  // compute the new intersection
      }
    while (r - l > 1 &&
           (q[l + 1].b - t[r]) * (q[l + 1].a - t[r]) > eps)  // note: remove redundant elements
      --r;
    t[r + 1] = its(q[l + 1], q[r]);  // then compute the new intersection
    ++r;
    // Note that ++r must not be done inside the index of t here…
    ```

## Exercises

[POJ 2451 Uyuw's Concert](http://poj.org/problem?id=2451) pay attention to the boundary cases

[POJ 1279 Art Gallery](http://poj.org/problem?id=1279) find the kernel of a polygon

[「CQOI2006」凸多边形 (Convex Polygon)](https://www.luogu.com.cn/problem/P4196)
