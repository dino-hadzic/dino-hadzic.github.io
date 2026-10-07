---
title: Rotating calipers
---

This page mainly introduces the rotating calipers method.

## Introduction

The rotating calipers algorithm (in Chinese literature "旋转卡壳"), building on a convex hull algorithm, enumerates the edges of the hull while maintaining the other required points, and can thus solve in linear time problems related to the properties of the convex hull, such as the diameter of the hull or the minimum bounding rectangle.

???+ note "The algorithm's Chinese name"
    The common Chinese name of this algorithm is "旋转卡壳" (xuánzhuǎn qiǎké, roughly "rotating jamming"). It can be understood as follows: for the edge we are currently enumerating, through every maintained point we can draw a line that is either parallel or perpendicular to it; to guarantee optimality for the current edge, our task is to make these lines "jam" (clamp) the convex hull exactly. The edges are usually enumerated in the order in which they rotate in some direction, so the whole process consists of "rotating" and "jamming".
    
    The literal translation of its English name "rotating calipers" would be "rotating measuring calipers", where "calipers" means "a caliper gauge". The original idea of the paper that first proposed the term[^ref1] is: clamp the convex hull with an adjustable "caliper", then "rotate" the "caliper" around the hull.

## Diameter of the convex hull

???+ note "Example 1: [Luogu P1452 Beauty Contest G](https://www.luogu.com.cn/problem/P1452)"
    Given $n$ points in the plane, find the maximum distance over all pairs of points. ($2\leq n \leq 50000,|x|,|y| \leq 10^4$)

### Procedure

First compute the convex hull of all given points with any convex hull algorithm; the pair of points with the maximum distance must lie on the hull. Because of the shape of the hull we observe that, if we traverse the edges of the hull counterclockwise and find for each edge the point farthest from it, then as the edge rotates, the corresponding farthest point also rotates counterclockwise and never goes backward. This means that while enumerating the edges of the hull counterclockwise, we can record and maintain the current farthest point and keep computing and updating the answer.

The array obtained after computing the hull is naturally ordered counterclockwise, but remember to append node 1 (the lower-left corner) to the end of the array in advance, so that when enumerating the edges $(i,i+1)$ one by one, all edges are visited.

![](images/rotating-calipers1.png)

During the enumeration, for every edge we check whether the distance of $j+1$ from the edge $(i,i+1)$ is greater than that of $j$; if so, we increase $j$ by one, otherwise $j$ is the optimal point for this edge. To compare the distances of points from the edge, we can compute the areas of the two triangles with cross products (as in the figure, the yellow and blue triangles share a base) and compare them directly.

### Implementation

???+ note "Core code"
    === "C++"
        ```cpp
        int sta[N], top;  // store the indices of the hull vertices on a stack; the first and last vertex have the same index
        
        ll pf(ll x) { return x * x; }
        
        ll dis(int p, int q) { return pf(a[p].x - a[q].x) + pf(a[p].y - a[q].y); }
        
        ll sqr(int p, int q, int y) { return abs((a[q] - a[p]) * (a[y] - a[q])); }
        
        ll mx;
        
        void get_longest() {  // diameter of the convex hull
          int j = 3;
          if (top < 4) {
            mx = dis(sta[1], sta[2]);
            return;
          }
          for (int i = 1; i < top; ++i) {
            while (sqr(sta[i], sta[i + 1], sta[j]) <=
                   sqr(sta[i], sta[i + 1], sta[j % top + 1]))
              j = j % top + 1;
            mx = max(mx, max(dis(sta[i + 1], sta[j]), dis(sta[i], sta[j])));
          }
        }
        ```
    
    === "Python"
        ```python
        sta = [0] * N
        top = 0  # store the indices of the hull vertices on a stack; the first and last vertex have the same index
        
        
        def pf(x):
            return x * x
        
        
        def dis(p, q):
            return pf(a[p].x - a[q].x) + pf(a[p].y - a[q].y)
        
        
        def sqr(p, q, y):
            return abs((a[q] - a[p]) * (a[y] - a[q]))
        
        
        def get_longest():  # diameter of the convex hull
            j = 3
            if top < 4:
                mx = dis(sta[1], sta[2])
                return
            for i in range(1, top):
                while sqr(sta[i], sta[i + 1], sta[j]) <= sqr(
                    sta[i], sta[i + 1], sta[j % top + 1]
                ):
                    j = j % top + 1
                mx = max(mx, max(dis(sta[i + 1], sta[j]), dis(sta[i], sta[j])))
        ```

## Minimum bounding rectangle

[Luogu P3187 Minimum Bounding Rectangle](https://www.luogu.com.cn/problem/P3187)

Given the coordinates of some points, find the rectangle of minimum area that covers all the points. ($3\leq n \leq 50000$)

### Procedure

With the previous problem as a warm-up, the natural idea here is again rotating calipers, but this time the quantity asked for is an area. Maintaining only one optimal point as in the previous problem would only find a pair of parallel lines at minimum distance; we also need to determine the left and right boundaries of the rectangle. So this time we maintain three points: one opposite the line being enumerated and two on different sides. The optimal opposite point is still determined by comparing areas computed with cross products; comparing areas here amounts to comparing one side length of the rectangle. The optimal side points are determined with dot products, because comparing dot products means comparing projection lengths, and the sum of the left and right projection lengths represents the other side length of the rectangle. The optimality of these two side lengths is independent, so once the positions of the three optimal points are found, we can determine the minimum area of a rectangle that covers all points and has the line of the current edge as one of its sides.

![](images/rotating-calipers2.png)

When finally computing the answer, if the problem does not require all four vertices, there is a rather clever way to compute the area of the rectangle directly using cross and dot products. Let twice the area of the purple part be $S$; the final area is

$$
S\times (|\overrightarrow{AD}\cdot \overrightarrow{AB}|+|\overrightarrow{BC}\cdot \overrightarrow{BA}|-|\overrightarrow{AB}\cdot \overrightarrow{BA}|)/|\overrightarrow{AB}\cdot \overrightarrow{BA}|
$$

### Implementation

The necessary convex hull computation is omitted; here is the core code for this problem:

???+ note "Core code"
    === "C++"
        ```cpp
        void get_biggest() {
          int j = 3, l = 2, r = 2;
          double t1, t2, t3, ans = 2e10;
          for (int i = 1; i < top; ++i) {
            while (sqr(sta[i], sta[i + 1], sta[j]) <=
                   sqr(sta[i], sta[i + 1], sta[j % top + 1]))
              j = j % top + 1;
            while (dot(sta[i + 1], sta[r % top + 1], sta[i]) >=
                   dot(sta[i + 1], sta[r], sta[i]))
              r = r % top + 1;
            if (i == 1) l = r;
            while (dot(sta[i + 1], sta[l % top + 1], sta[i]) <=
                   dot(sta[i + 1], sta[l], sta[i]))
              l = l % top + 1;
            t1 = sqr(sta[i], sta[i + 1], sta[j]);
            t2 = dot(sta[i + 1], sta[r], sta[i]) + dot(sta[i + 1], sta[l], sta[i]);
            t3 = dot(sta[i + 1], sta[i + 1], sta[i]);
            ans = min(ans, t1 * t2 / t3);
          }
        }
        ```
    
    === "Python"
        ```python
        def get_biggest():
            j = 3
            l = 2
            r = 2
            ans = 2e10
            for i in range(1, top):
                while sqr(sta[i], sta[i + 1], sta[j]) <= sqr(
                    sta[i], sta[i + 1], sta[j % top + 1]
                ):
                    j = j % top + 1
                while dot(sta[i + 1], sta[r % top + 1], sta[i]) >= dot(
                    sta[i + 1], sta[r], sta[i]
                ):
                    r = r % top + 1
                if i == 1:
                    l = r
                while dot(sta[i + 1], sta[l % top + 1], sta[i]) <= dot(
                    sta[i + 1], sta[l], sta[i]
                ):
                    l = l % top + 1
                t1 = sqr(sta[i], sta[i + 1], sta[j])
                t2 = dot(sta[i + 1], sta[r], sta[i]) + dot(sta[i + 1], sta[l], sta[i])
                t3 = dot(sta[i + 1], sta[i + 1], sta[i])
                ans = min(ans, t1 * t2 / t3)
        ```

## Exercises

-   [POJ 3608. Bridge Across Islands](http://poj.org/problem?id=3608)
-   [2011 ACM-ICPC World Finals, Problem K. Trash Removal](https://codeforces.com/gym/101175)
-   [ICPC WF Moscow Invitational Contest - Online Mirror, Problem F. Framing Pictures](https://codeforces.com/contest/1578/problem/F)

## References and notes

[^ref1]: Toussaint, Godfried T. (1983). "Solving geometric problems with the rotating calipers". Proc. MELECON '83, Athens. CiteSeerX 10.1.1.155.5671

-   <https://en.wikipedia.org/wiki/Rotating_calipers>

-   <http://www-cgrl.cs.mcgill.ca/~godfried/research/calipers.html>

-   Shamos, Michael (1978). "Computational Geometry" (PDF). Yale University. pp. 76–81.
