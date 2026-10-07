---
title: Pick's theorem
---

## Pick's theorem

Pick's theorem: given a simple polygon whose vertices are all lattice points, Pick's theorem gives the relationship between its area ${\displaystyle A}$, the number of interior lattice points ${\displaystyle i}$ and the number of boundary lattice points ${\displaystyle b}$: ${\displaystyle A=i+{\frac {b}{2}}-1}$.

Proof: [Pick's theorem](https://en.wikipedia.org/wiki/Pick%27s_theorem)

It has the following generalizations:

-   Take the area of the basic figure of the lattice as one unit. On a parallelogram lattice, Pick's theorem still holds. Applied to an arbitrary triangular lattice, Pick's theorem becomes ${\displaystyle A=2 \times i+b-2}$.
-   For a non-simple polygon ${\displaystyle P}$, Pick's theorem reads ${\displaystyle A=i+{\frac {b}{2}}-\chi (P)}$, where ${\displaystyle \chi (P)}$ denotes the **Euler characteristic** of ${\displaystyle P}$.
-   Higher-dimensional generalization: Ehrhart polynomials.
-   Pick's theorem is equivalent to **Euler's formula** (${\displaystyle V-E+F=2}$).

## An example problem ([POJ 1265](http://poj.org/problem?id=1265))

### Problem summary

In the Cartesian coordinate system, a robot starts from an arbitrary point and makes $\textit{n}$ moves, each time moving $\textit{dx}$ to the right and $\textit{dy}$ upward, finally forming a closed simple polygon in the plane. Find the number of lattice points on the boundary, the number of lattice points inside the polygon, and the area of the polygon.

### Solution

This problem actually uses the following three facts:

-   A segment with lattice-point endpoints, if both $\textit{dx}$ and $\textit{dy}$ are nonzero, passes through $\gcd(\textit{dx}, \textit{dy}) + 1$ lattice points; of course, when computing for a whole figure, the extra point is counted by the previous edge, so it need not be added. Hence the number of points covered by one edge is $\gcd(\textit{dx},\textit{dy})$, where $\textit{dx},\textit{dy}$ are the numbers of points the segment occupies horizontally and vertically. If $\textit{dx}$ or $\textit{dy}$ is $0$, the number of covered points is $\textit{dy}$ **or** $\textit{dx}$ respectively.
-   Pick's theorem: the area of a simple polygon with lattice-point vertices in the plane = number of boundary points/2 + number of interior points - 1.
-   The area of any polygon equals half the sum of the cross products of the vectors formed by consecutive pairs of vertices with the origin, taken in order (this can also be obtained by a clockwise definite integral).

??? note "Reference code"
    ```cpp
    --8<-- "docs/geometry/code/pick/pick_1.cpp"
    ```
