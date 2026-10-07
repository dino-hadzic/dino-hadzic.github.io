---
title: Triangulation
---

In geometry, a triangulation is a subdivision of a planar object into triangles, and by extension a subdivision of a higher-dimensional geometric object into simplices.
For a given point set there are many triangulations, for example:

![Three triangulations](./images/triangulation-0.svg)

This page introduces the two-dimensional Delaunay triangulation (DT for short) and a divide-and-conquer algorithm for constructing it.

## Delaunay triangulation

### Definition

In mathematics and computational geometry, for a given discrete set of points $P$ in the plane, its Delaunay triangulation DT($P$) satisfies:

1.  Empty circle property: DT($P$) is **unique** (if no four points are concyclic), and in DT($P$) no other point lies inside the circumcircle of **any** triangle.
2.  Maximizing the minimum angle: among all triangulations the point set $P$ can form, the triangles of DT($P$) have the largest minimum angle. In this sense DT($P$) is the triangulation **closest to regular**. Concretely, if two adjacent triangles form a convex quadrilateral, then after swapping its diagonal the minimum of the interior angles of the two triangles does not increase.

![A Delaunay triangulation with its circumcircles shown](./images/triangulation-1.svg)

### Properties

1.  Closest points: triangles are formed by the three closest points, and the segments (triangle edges) do not intersect each other.
2.  Uniqueness: no matter from which part of the region the construction starts, the final result is the same (if no four points of the set are concyclic).
3.  Optimality: if the diagonal of the convex quadrilateral formed by any two adjacent triangles can be swapped, the smallest of the six interior angles of the two triangles will not change.
4.  Most regular: if the minimum angles of all triangles of a triangulation are sorted in increasing order, the sequence obtained for the Delaunay triangulation has the largest values.
5.  Locality: adding, deleting or moving a single vertex only affects the neighboring triangles.
6.  Convex hull: the outer boundary of the triangulation forms a convex polygon (the convex hull).

## Divide-and-conquer algorithm for constructing the DT

There are many algorithms for constructing the DT; below we present a divide-and-conquer algorithm with time complexity $O(n \log n)$.

The first step of the divide-and-conquer construction is to sort the given point set in **increasing** order of the $x$ coordinate, breaking ties by increasing $y$ coordinate, and to remove coincident points. The figure below shows a sorted point set of size $10$.

![A sorted point set of size 10](./images/triangulation-2.svg)

If there are fewer than $2$ points, no edges are needed. Otherwise, the sorted point set is repeatedly split in the middle into two parts until the subsets have size $2$ or $3$. Two points are connected by an edge, three non-collinear points form a triangle, and for three collinear points only the two pairs of adjacent points (in sorted order) are connected.

![Dividing into subsets of 2 or 3 points](./images/triangulation-3.svg)

Then, while returning from the recursion, the triangulations of the left and right subsets are merged in turn. After merging, the edges are classified as LL-edges (edges inside the left subset), RR-edges (edges inside the right subset) and LR-edges (edges connecting the left and right subsets); in the figure below they are shown in gray, red and blue respectively. To maintain the DT properties, merging **may** require deleting some LL-edges and RR-edges, but these two kinds of edges are **never** added.

![The three kinds of edges after merging](./images/triangulation-4.svg)

The first step of merging the left and right triangulations is to find the lower common tangent of the two convex hulls and insert the corresponding base LR-edge. The recursion returns the boundary edges of the left and right hulls; starting from the rightmost point of the left hull and the leftmost point of the right hull, we move along the hull boundaries until no point lies to the right of the directed line from the left endpoint to the right endpoint.

![Merging the left and right triangulations](./images/triangulation-5.svg)

Next, we need to determine the next LR-edge, the one **immediately above** the base LR-edge. For example, for the right point set, the possible (right) endpoints of the next LR-edge are the other endpoints of the RR-edges connected to the right endpoint of the base LR-edge (points $6, 7, 9$), while the left endpoint is point $2$.

![The next LR-edge](./images/triangulation-6.svg)

Take the right endpoint as an example. Starting from the ray toward the left endpoint of the base LR-edge, we check the RR-edges connected to the right endpoint in clockwise order:

1.  Only endpoints strictly above the base LR-edge are valid candidates, i.e. the point lies to the left of the directed line from the left endpoint of the base to its right endpoint. The corresponding clockwise rotation angle must be in $(0^\circ,180^\circ)$.
2.  Let the current candidate be $c$ and the next adjacent neighbor in the same direction be $d$. If $d$ lies strictly inside the circumcircle of the two endpoints of the base LR-edge and $c$, delete the RR-edge to $c$ and continue checking the edge to $d$.
3.  Otherwise keep the current candidate and stop checking on this side. Since this side is already a Delaunay triangulation, it suffices to compare adjacent candidate edges in circular order.

![Checking valid candidates](./images/triangulation-7.svg)

As in the figure above, we check points $6,7,9$ in turn. The green circle corresponding to point $6$ contains the next neighbor $7$, so the RR-edge to $6$ is deleted; the purple circle corresponding to point $7$ does not contain the next neighbor $9$, so $7$ is kept as the right candidate. Afterwards it still has to be compared with the left candidate to determine the next LR-edge.

For the left point set, the procedure is mirrored: start from the ray toward the right endpoint of the base LR-edge and check in counterclockwise order.

![Checking valid candidates on the left side](./images/triangulation-8.svg)

When neither the left nor the right side has a valid candidate, the current base LR-edge is the upper common tangent and the merge is complete. If only one side has a valid candidate, connect it to the other endpoint of the base LR-edge to obtain the new LR-edge.

When both sides have valid candidates: if the right candidate lies strictly inside the circumcircle determined by the left candidate and the two endpoints of the base, choose the right candidate; otherwise choose the left candidate. Connect the chosen candidate to the endpoint of the base on the opposite side to obtain the new LR-edge. If the four points are concyclic, either choice works.

![The next LR-edge](./images/triangulation-9.svg)

Once this LR-edge has been added, take it as the base LR-edge and repeat the steps above, adding the next one, until the merge is complete.

![Merging](./images/triangulation-10.svg)

### Implementation

If edges are stored only in unordered adjacency lists and all adjacent edges of both endpoints are scanned every time an LR-edge is added, the time complexity is $O(n^2)$, because one endpoint may form several LR-edges in a row, causing its adjacency list to be scanned over and over.

The reference implementation uses the quad-edge[^quad-edge] structure to maintain the circular order of edges. Each undirected edge is recorded by four directed edges: two represent the two directions in the original graph and the other two represent the two directions in the dual graph. The four records are stored consecutively, so it suffices to maintain, for each directed edge, its origin and the next counterclockwise edge with the same origin; the following operations then take $O(1)$ time:

| Operation       | Meaning                                                      |
| --------------- | ------------------------------------------------------------ |
| `rev(e)`        | the reversed edge                                            |
| `onext(e)`      | the next counterclockwise edge with the same origin          |
| `oprev(e)`      | the previous counterclockwise edge with the same origin      |
| `lnext(e)`      | move one edge forward along the boundary of the left face    |
| `onext(rev(e))` | move one edge backward along the boundary of the right face  |

`splice(a, b)` modifies the circular relations in the original graph and the dual graph at the same time; it is used to join or split the rings containing two edges. `connect(a, b)` connects the end of `a` to the origin of `b` within the same face. When deleting an edge, its two directions are removed from their respective rings. These topological operations only modify a constant number of records; the reference implementation allocates and recycles edges with a dynamic array, with amortized $O(1)$ cost.

In the code, `base` is directed from the right point set to the left point set, so the points "above" the base LR-edge in the figures lie to the right of the directed edge `base`. The left candidate edge is `onext(rev(base))` and the right candidate edge is `oprev(base)`; after deleting a candidate edge, we simply continue along the circular order on that side.

??? note "Implementation"
    ```cpp
    --8<-- "docs/geometry/code/triangulation/triangulation_1.cpp:delaunay"
    ```

### Complexity

Suppose one merge involves $k$ points. When finding the lower common tangent, every move advances along the hull boundary of one side, for $O(k)$ moves in total. When selecting candidates, every further check is accompanied by the deletion of an LL-edge or RR-edge, and the two sub-triangulations together have only $O(k)$ edges. Apart from these deletions, each iteration of the main merge loop performs a constant number of tests and adds one LR-edge; newly added LR-edges are not deleted again during this merge, so their number is also $O(k)$. Therefore the total time of one merge is $O(k)$.

The initial sorting takes $O(n \log n)$, and the recursion satisfies $T(n)=T(\lfloor n/2 \rfloor)+T(\lceil n/2 \rceil)+O(n)$, so the total time complexity is $O(n \log n)$. At any moment the number of retained edges is $O(n)$, and the code recycles the storage of deleted edges instead of keeping all historical edges, so the space complexity is $O(n)$.

## Voronoi diagram

Given $n\ge 1$ pairwise distinct seed points in the plane, the Voronoi region of each seed consists of all points whose distance to that seed is not greater than the distance to any other seed. These regions are convex, possibly unbounded; their interiors are pairwise disjoint and together they cover the whole plane; the common boundary of two adjacent regions lies on the perpendicular bisector of the segment connecting the corresponding two seeds.

For a point set that is not entirely collinear and has no four concyclic points, the Voronoi diagram and the Delaunay triangulation are dual to each other: each triangular face corresponds to its circumcenter, each interior edge corresponds to the segment connecting the circumcenters of the two triangles on its sides, and each convex hull edge corresponds to a ray starting from the circumcenter of its triangle, perpendicular to that edge and pointing outward from the hull. If four concyclic points exist, after the construction the coincident circumcenters must be merged and zero-length dual edges removed. If all points are collinear, the Voronoi edges are the perpendicular bisectors of adjacent points in sorted order; if there is only one point, its region is the whole plane.

![Duality between the Voronoi diagram and the Delaunay triangulation](./images/triangulation-11.svg)

In the figure above, the solid points $P_i$ are the seeds and the hollow points $O_i$ are the circumcenters of the triangles; the solid blue lines form the Voronoi diagram and the dashed orange lines form the Delaunay triangulation. The background colors distinguish the Voronoi regions, the arrows indicate unbounded edges; only the part inside a finite window is shown.

After constructing the DT, using the existing circular order of edges to enumerate faces and edges, the conversion above can be done in $O(n)$ time, so the total time complexity of constructing the Voronoi diagram is $O(n \log n)$.

## Problems

[Luogu P6362 Planar Euclidean Minimum Spanning Tree](https://www.luogu.com.cn/problem/P6362) classic application of triangulation

[SGU 383 Caravans](https://codeforces.com/problemsets/acmsguru/problem/99999/383) triangulation + binary lifting

[ContestHunter. Endless Destruction](http://noi-test.zzstep.com/contest/Beta%20Round%20%EF%BC%832%20%28%E6%96%B0%E7%96%86%E7%9C%81%E9%98%9F%E4%BA%92%E6%B5%8BWeek1-Day2%29/%E6%97%A0%E5%B0%BD%E7%9A%84%E6%AF%81%E7%81%AD) triangulation, then the dual graph to build the Voronoi diagram

[Codeforces Gym 103485M. Constellation collection](https://codeforces.com/gym/103485/problem/M) build a graph after triangulation and run a flood fill

## References and further reading

1.  [Wikipedia - Triangulation (geometry)](https://en.wikipedia.org/wiki/Triangulation_%28geometry%29)
2.  [Wikipedia - Delaunay triangulation](https://en.wikipedia.org/wiki/Delaunay_triangulation)
3.  [Samuel Peterson - Computing Constrained Delaunay Triangulations in 2-D (1997-98)](http://www.geom.uiuc.edu/~samuelp/del_project.html)

[^quad-edge]: Leonidas Guibas, Jorge Stolfi. [Primitives for the Manipulation of General Subdivisions and the Computation of Voronoi Diagrams](https://people.eecs.berkeley.edu/~jrs/meshpapers/GuibasStolfi.pdf). ACM Transactions on Graphics, 4(2), 1985, 74–123.
