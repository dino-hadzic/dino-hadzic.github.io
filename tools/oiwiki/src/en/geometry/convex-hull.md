---
title: Convex hull
---

## Two-dimensional convex hull

### Definition

#### Convex polygon

A convex polygon is a **simple polygon** all of whose interior angles lie in the range $[0,\pi]$.

#### Convex hull

The smallest convex polygon in the plane that contains all given points is called the convex hull.

Its definition: for a given set $X$, the intersection $S$ of all convex sets containing $X$ is called the **convex hull** of $X$.

Intuitively, it is the shape taken by a rubber band stretched around all the given points.

The convex hull encloses all the given points with the smallest perimeter. If a concave polygon encloses all the points, its perimeter is certainly not minimal, as in the figure below. By the triangle inequality, a convex polygon is always optimal in terms of perimeter.

![](./images/ch.png)

### Andrew's algorithm for the convex hull

Commonly used methods are the Graham scan and Andrew's algorithm; here we mainly introduce Andrew's algorithm.

#### Properties

The time complexity of the algorithm is $O(n\log n)$, where $n$ is the size of the point set whose hull we compute; the bottleneck is sorting all points by two keys.

#### Procedure

First sort all points with the x coordinate as the first key and the y coordinate as the second key.

Obviously, after sorting, the smallest and the largest element must be on the convex hull. Moreover, since the polygon is convex, if we start from a point and walk counterclockwise, the path always "turns left"; as soon as a right turn appears, that part is not on the hull. Therefore we can use a monotonic stack to maintain the upper and lower hulls.

Seen from left to right, the upper and lower hulls turn in different directions, so to make the monotonic stack work we first obtain the lower hull by **enumerating in increasing order**, and then the upper hull in **decreasing** order.

While computing a hull, as soon as we find that the direction of travel from the two points on top of the stack ($S_1,S_2$, where $S_1$ is the top) to the point about to be pushed ($P$) turns right, i.e. the cross product is less than $0$: $\overrightarrow{S_2S_1}\times \overrightarrow{S_1P}<0$, we pop the top of the stack, go back one step and keep checking until $\overrightarrow{S_2S_1}\times \overrightarrow{S_1P}\ge 0$ or only one element remains on the stack.

Usually the points lying on the edges of the hull do not need to be kept, so the "$<$" in the condition $\overrightarrow{S_2S_1}\times \overrightarrow{S_1P}<0$ above can be changed to $\le$ as appropriate, and the latter condition should then be changed to $>$.

![Andrew](./images/andrew.svg)

#### Implementation

???+ note "Implementation"
    === "C++"
        ```cpp
        // stk[] is integer, it stores indices
        // p[] stores vectors or points
        tp = 0;                       // initialize the stack
        std::sort(p + 1, p + 1 + n);  // sort the points
        stk[++tp] = 1;
        // Push the first element without setting used, so that 1 also updates the monotonic stack when closing the hull at the end
        for (int i = 2; i <= n; ++i) {
          while (tp >= 2  // in the next line the * operator is overloaded as the cross product
                 && (p[stk[tp]] - p[stk[tp - 1]]) * (p[i] - p[stk[tp]]) <= 0)
            used[stk[tp--]] = 0;
          used[i] = 1;  // used means the point is on the hull
          stk[++tp] = i;
        }
        int tmp = tp;  // tmp is the size of the lower hull
        for (int i = n - 1; i > 0; --i)
          if (!used[i]) {
            // ↓do not touch the lower hull while computing the upper hull
            while (tp > tmp && (p[stk[tp]] - p[stk[tp - 1]]) * (p[i] - p[stk[tp]]) <= 0)
              used[stk[tp--]] = 0;
            used[i] = 1;
            stk[++tp] = i;
          }
        for (int i = 1; i <= tp; ++i)  // copy into a new array
          h[i] = p[stk[i]];
        int ans = tp - 1;
        ```
    
    === "Python"
        ```python
        stk = []  # integer, stores indices
        p = []  # stores vectors or points
        tp = 0  # initialize the stack
        p.sort()  # sort the points
        tp = tp + 1
        stk[tp] = 1
        # Push the first element without setting used, so that 1 also updates the monotonic stack when closing the hull at the end
        for i in range(2, n + 1):
            while tp >= 2 and (p[stk[tp]] - p[stk[tp - 1]]) * (p[i] - p[stk[tp]]) <= 0:
                # in the next line the * operator is overloaded as the cross product
                used[stk[tp]] = 0
                tp = tp - 1
            used[i] = 1  # used means the point is on the hull
            tp = tp + 1
            stk[tp] = i
        tmp = tp  # tmp is the size of the lower hull
        for i in range(n - 1, 0, -1):
            if used[i] == False:
                #      ↓do not touch the lower hull while computing the upper hull
                while tp > tmp and (p[stk[tp]] - p[stk[tp - 1]]) * (p[i] - p[stk[tp]]) <= 0:
                    used[stk[tp]] = 0
                    tp = tp - 1
                used[i] = 1
                tp = tp + 1
                stk[tp] = i
        for i in range(1, tp + 1):
            h[i] = p[stk[i]]
        ans = tp - 1
        ```

According to the code above, the hull finally has $\textit{ans}$ elements (point $1$ is stored additionally, so the array $h$ has $\textit{ans}+1$ elements), ordered counterclockwise. The perimeter is

$$
\sum_{i=1}^{\textit{ans}}\left|\overrightarrow{h_ih_{i+1}}\right|
$$

### Graham scan

#### Properties

Like Andrew's algorithm, the Graham scan has time complexity $O(n\log n)$, and the bottleneck is also sorting all the points.

#### Procedure

First find the point $P$ with the smallest y coordinate among all points. By the definition of the convex hull, this point must be on the hull. Then sort all points by their polar angle relative to point $P$.

![](./images/ch1.svg)

Similarly to Andrew's algorithm, if we start from point $P$ and walk along the hull counterclockwise, all the points we pass must "turn left". Formally, for any three consecutive points $P_1, P_2, P_3$ visited counterclockwise on the hull, $\overrightarrow{P_1 P_2} \times \overrightarrow{P_2 P_3} \ge 0$ must hold.

Create a stack to store the hull, push $P$ first, and then try to add every point in order of polar angle. If the direction of travel from the two points on top of the stack $P_1, P_2$ (where $P_1$ is the top) to the point $P_0$ being pushed "turns right", pop the top $P_1$; repeat this until the point being pushed and the two points on top of the stack satisfy the condition, or only one element remains on the stack, and then push $P_0$.

![](./images/ch2.svg)

![](./images/ch3.svg)

???+ note "Implementation"
    ```cpp
    struct Point {
      double x, y, ang;
    
      Point operator-(const Point& p) const { return {x - p.x, y - p.y, 0}; }
    } p[MAXN];
    
    double dis(Point p1, Point p2) {
      return sqrt((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y));
    }
    
    bool cmp(Point p1, Point p2) {
      if (p1.ang == p2.ang) {
        return dis(p1, p[1]) < dis(p2, p[1]);
      }
      return p1.ang < p2.ang;
    }
    
    double cross(Point p1, Point p2) { return p1.x * p2.y - p1.y * p2.x; }
    
    int main() {
      for (int i = 2; i <= n; ++i) {
        if (p[i].y < p[1].y || (p[i].y == p[1].y && p[i].x < p[1].x)) {
          std::swap(p[1], p[i]);
        }
      }
      for (int i = 2; i <= n; ++i) {
        p[i].ang = atan2(p[i].y - p[1].y, p[i].x - p[1].x);
      }
      std::sort(p + 2, p + n + 1, cmp);
      sta[++top] = 1;
      for (int i = 2; i <= n; ++i) {
        while (top >= 2 &&
               cross(p[sta[top]] - p[sta[top - 1]], p[i] - p[sta[top]]) < 0) {
          top--;
        }
        sta[++top] = i;
      }
      return 0;
    }
    ```

## Minkowski sum

### Definition

The Minkowski sum $P+Q$ of point sets $P$ and $Q$ is defined as $P+Q=\{a+b|a\in P,b\in Q\}$: treat every point of $Q$ as a vector, translate every point of $P$ by these vectors, and the set of all results is $P+Q$. Here we only discuss the Minkowski sum of **convex hulls**.

For example, for the point set $P=\{(0,0),(-3,3),(2,1)\}$ and the point set $Q=\{(0,0),(-1,3),(1,4),(2,2)\}$:

![](./images/convex-hull1.svg)

Translate $P$ by every vector of $Q$:

![](./images/convex-hull2.svg)

It is easy to see that the new figure is also a **convex hull**:

![](./images/convex-hull3.svg)

### Properties

1.  If the point sets $P$ and $Q$ are convex, their Minkowski sum $P+Q$ is also convex.

    ??? note "Proof"
        Let $e,f\in P+Q$; there exist $a,b \in P$ and $c,d\in Q$ with $e=a+c,f=b+d$. Then for every $t\in[0,1]$:
        
        $$
        \begin{aligned}
        te + (1-t)f &= t(a+c)+(1-t)(b+d)\\
        &=(ta+(1-t)b)+(tc+(1-t)d)\\
        &\in P+Q.
        \end{aligned}
        $$
        
        This completes the proof.
2.  If the point sets $P$ and $Q$ are convex, the edge set of their Minkowski sum $P+Q$ is obtained by sorting the edges of the convex sets $P$ and $Q$ by polar angle and concatenating them.

    ??? note "Proof"
        Without loss of generality, assume that no edge of the convex set $P$ has the same slope as any edge of $Q$. Rotate the coordinate system so that some edge $XY$ of $P$ is parallel to the $x$ axis and is the lowest.
        
        Let $U$ be the lowest point of $Q$ at that moment, and $A$ the **lowest** and **leftmost** point of $P+Q$.
        
        We see that $\vec{A} = \vec{X} + \vec{U}$, so $A$ must lie on the boundary of $P+Q$.
        
        Similarly, the **lowest** and **rightmost** point $B$ of $P+Q$ satisfies $\vec{B} = \vec{Y} + \vec{U}$ and must also lie on the boundary of $P+Q$.
        
        Therefore $\vec{AB} = \vec{XY} + \vec{U}$.
        
        If we perform the rotations in order, the results successively form every edge of $P+Q$.
        
        This completes the proof.

### Implementation

By property 2, we can sort the convex sets $P,Q$ by polar angle to obtain the order in which their edges appear on $P+Q$, take $P_1+Q_1$ as the starting point of $P+Q$, and then place the edges one by one with a **merge**-like procedure.

Time complexity: $O(n+m)$

???+ note "Implementation"
    ```cpp
    template <class T>
    struct Point {
      T x, y;
    
      Point(T x = 0, T y = 0) : x(x), y(y) {}
    
      friend Point operator+(const Point &a, const Point &b) {
        return {a.x + b.x, a.y + b.y};
      }
    
      friend Point operator-(const Point &a, const Point &b) {
        return {a.x - b.x, a.y - b.y};
      }
    
      // Dot product
      friend T operator*(const Point &a, const Point &b) {
        return a.x * b.x + a.y * b.y;
      }
    
      // Cross product
      friend T operator^(const Point &a, const Point &b) {
        return a.x * b.y - a.y * b.x;
      }
    };
    
    template <class T>
    vector<Point<T>> minkowski_sum(vector<Point<T>> a, vector<Point<T>> b) {
      vector<Point<T>> c{a[0] + b[0]};
      for (usz i = 0; i + 1 < a.size(); ++i) a[i] = a[i + 1] - a[i];
      for (usz i = 0; i + 1 < b.size(); ++i) b[i] = b[i + 1] - b[i];
      a.pop_back(), b.pop_back();
      c.resize(a.size() + b.size() + 1);
      merge(a.begin(), a.end(), b.begin(), b.end(), c.begin() + 1,
            [](const Point<T> &a, const Point<T> &b) { return (a ^ b) < 0; });
      for (usz i = 1; i < c.size(); ++i) c[i] = c[i] + c[i - 1];
      return c;
    }
    ```

### Example

???+ note "[Example: \[JSOI2018\] War](https://loj.ac/p/2549)"
    There are two convex hulls $P,Q$; $Q$ is translated $q$ times, and after each move we must answer whether they intersect. $1\le n,m\le 10^5,1\le q\le 10^5$.

??? note "Implementation"
    ```cpp
    --8<-- "docs/geometry/code/convex-hull/convex-hull_1.cpp"
    ```

## Three-dimensional convex hull

### Basics

> Circle inversion: let $O$ be the center of inversion and $R$ the radius of inversion. If a line through $O$ passes through $P$ and $P'$ and $OP\times OP'=R^{2}$, then $P$ and $P'$ are said to be inverses of each other with respect to $O$.

### Procedure

The procedure for computing the hull is as follows:

-   First perturb the points slightly to avoid four coplanar points.
-   For an already known hull, add a new point $P$; treat $P$ as a point light source casting rays onto the hull. The visible and invisible faces are certainly separated by a sequence of edges.
-   Delete the visible faces and add the faces formed by those separating edges and $P$.
    Repeat this process; by [Pick's theorem](./pick.md), Euler's formula (in a convex polyhedron the numbers of vertices $V$, edges $E$ and faces $F$ satisfy $V−E+F=2$) and circle inversion, the complexity is $O(n^2)$.[^3d-v]

### Template problem

[P4724 [Template] 3D Convex Hull](https://www.luogu.com.cn/problem/P4724)

Repeating the process above gives the answer.

???+ note "Implementation"
    ```cpp
    --8<-- "docs/geometry/code/3d/3d_1.cpp"
    ```

## Exercises

-   [UVa11626 Convex Hull](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=78&page=show_problem&problem=2673)

-   ["USACO5.1" Fencing the Cows](https://www.luogu.com.cn/problem/P2742)

-   [POJ1873 The Fortified Forest](http://poj.org/problem?id=1873)

-   [POJ1113 Wall](http://poj.org/problem?id=1113)

-   [USACO22JAN Multiple Choice Test P](https://www.luogu.com.cn/problem/P8101)

-   ["SHOI2012" Credit Card Convex Hull](https://www.luogu.com.cn/problem/P3829)

## References and notes

[^3d-v]: [Notes on learning the 3D convex hull](https://www.cnblogs.com/xzyxzy/p/10225804.html)
