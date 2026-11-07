---
title: Introduction to linear algebra
---

??? tip "Tip"
    This page is not closely related to the other pages in the "Linear algebra" category. Nevertheless, the author believes it is indeed necessary to talk about the essence of linear algebra and to trace the origins of its concepts and the connections between them, so that the reader gains an initial but systematic understanding of linear algebra.

As early as several thousand years ago, people used systems of linear equations to solve problems, and today linear algebra is still widely applied.

Linear algebra originates from observation. People noticed that many objects share similar properties, for example:

-   Forces can be decomposed and composed.

-   For arbitrary $k,x_0$, $k \sin (x-x_0)$ can be decomposed into $k_1\sin x + k_2\cos x$.

These properties are related to **scaling**, **decomposition**, **superposition** and the like of the objects being described. Linear algebra abstracts these properties away from the concrete objects and studies them as an independent discipline. In OI, knowledge of linear algebra can be used directly to solve problems, and also to optimize algorithms, data structures, etc. For example:

-   maintaining a linear basis (xor basis) with heavy-light decomposition to find the maximum xor on a path in a tree

-   turning the problem of counting the spanning trees of a graph into computing the determinant of a matrix via the matrix-tree theorem (Kirchhoff's theorem)

-   optimizing recurrences with fast matrix exponentiation
