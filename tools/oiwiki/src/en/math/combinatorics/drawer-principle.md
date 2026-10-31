---
title: Pigeonhole principle
---

## Definition

The drawer principle is also known as the pigeonhole principle (or Dirichlet's box principle).

It is often used in existence proofs and for finding the solution in the worst case.

## Simple case

If $n+1$ objects are divided into $n$ groups, then at least one group contains two (or more) objects.

This theorem looks fairly obvious; it is proved by contradiction: if every group contained at most $1$ object, there would be at most $1\times n$ objects in total, but there are actually $n+1$ objects, a contradiction.

## Generalization

If $n$ objects are divided into $k$ groups, then there exists at least one group containing at least $\left \lceil \dfrac{n}{k} \right \rceil$ objects.

The generalized form can also be proved by contradiction: if every group contained fewer than $\left \lceil \dfrac{n}{k} \right \rceil$ objects, their total would be $S\leq (\left \lceil \dfrac{n}{k} \right \rceil -1 ) \times k=k\left\lceil \dfrac{n}{k} \right\rceil-k < k(\dfrac{n}{k}+1)-k=n$, a contradiction.

Moreover, the partition can be weakened to a cover and the conclusion still holds.  
Given a set $S$ and a family $\{A_1,A_2\ldots A_k\}$ of nonempty subsets of $S$:

-   If $\bigcup_{i=1}^k A_i$ holds, the family is called a cover of $S$.
-   If a cover additionally satisfies $i\neq j\to A_i\cap A_j=\varnothing$, it is called a partition of $S$.

The pigeonhole principle can then be stated as follows: for a cover $\{A_1,A_2\ldots A_k\}$ of $S$, there is at least one set $A_i$ satisfying $\left\vert A_i \right\vert \geq \left\lceil \dfrac{\left\vert S \right\vert}{k} \right\rceil$.

## References

-   [Wikipedia: Pigeonhole principle](https://en.wikipedia.org/wiki/Pigeonhole_principle)
-   *Discrete Mathematics and Its Applications*: Chapter 6, Section 1
