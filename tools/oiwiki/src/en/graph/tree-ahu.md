---
title: AHU algorithm
---

The AHU algorithm decides whether two rooted trees are isomorphic.

Another common way to test tree isomorphism is [tree hashing](tree-hash.md).

Prerequisites: [Tree basics](tree-basic.md), [Centroid of a tree](tree-centroid.md)

We recommend reading this together with the examples in the references at the end.

## Definition of tree isomorphism

### Isomorphism of rooted trees

Two rooted trees $T_1(V_1,E_1,r_1)$ and $T_2(V_2,E_2,r_2)$ are isomorphic if there is a bijection $\varphi: V_1 \rightarrow V_2$ such that

$$
\forall u,v \in V_1,(u,v) \in E_1 \iff (\varphi(u),\varphi(v))  \in E_2
$$

**and** $\varphi(r_1)=r_2$.

### Isomorphism of unrooted trees

Two unrooted trees $T_1(V_1,E_1)$ and $T_2(V_2,E_2)$ are isomorphic if there is a bijection $\varphi: V_1 \rightarrow V_2$ such that

$$
\forall u,v \in V_1,(u,v) \in E_1 \iff (\varphi(u),\varphi(v))  \in E_2
$$

holds.

Put simply: if the vertices of tree $T_1$ can be relabeled so that trees $T_1$ and $T_2$ become **exactly the same**, the two trees are isomorphic.

## Reducing the problem

The isomorphism problem for unrooted trees can be reduced to the one for rooted trees as follows:

For unrooted trees $T_1(V_1, E_1)$ and $T_2(V_2,E_2)$, first find **all** centroids of each.

-   If the two trees have different numbers of centroids, they are not isomorphic.
-   If both trees have exactly $1$ centroid, call them $c_1$ and $c_2$; then the unrooted trees $T_1(V_1, E_1)$ and $T_2(V_2,E_2)$ are isomorphic if and only if the rooted trees $T_1(V_1,E_1,c_1)$ and $T_2(V_2,E_2,c_2)$ are isomorphic.
-   If both trees have exactly $2$ centroids, call them $c_1,c'_1$ and $c_2,c'_2$; then the unrooted trees $T_1(V_1, E_1)$ and $T_2(V_2,E_2)$ are isomorphic if and only if the rooted trees $T_1(V_1,E_1,c_1)$ and $T_2(V_2,E_2,c_2)$ are isomorphic **or** the rooted trees $T_1(V_1,E_1,c'_1)$ and $T_2(V_2,E_2,c_2)$ are isomorphic.

So once we can solve rooted tree isomorphism, the procedure above reduces unrooted tree isomorphism to it and thereby solves it.

If there is an algorithm solving rooted tree isomorphism in $O(\left|V\right|)$, the procedure above solves unrooted tree isomorphism in $O(\left|V\right|)$ as well.

## Naive AHU algorithm

The naive AHU algorithm is based on bracket sequences.

### Principle 1

A valid bracket sequence corresponds uniquely to a rooted tree, and the bracket sequence of a tree is the concatenation of the bracket sequences of its subtrees. If we obtain a new bracket sequence by changing the order in which the subtrees' sequences are concatenated, the tree of the new sequence is isomorphic to the tree of the original one.

### Principle 2

Tree isomorphism is transitive: if $T_1$ and $T_2$ are isomorphic and $T_2$ and $T_3$ are isomorphic, then $T_1$ and $T_3$ are isomorphic.

### Corollary

Consider the recursive algorithm computing the bracket sequence of a tree, which concatenates the subtrees' sequences when returning from the recursion. Suppose that when concatenating we put the lexicographically smaller sequences first, and call the final result $NAME$.

Take the $NAME$ of the subtree rooted at $r$ as the $NAME$ of vertex $r$, written $NAME(r)$. Then for rooted trees $T_1(V_1,E_1,r_1)$ and $T_2(V_2,E_2,r_2)$, if $NAME(r_1)=NAME(r_2)$, the trees $T_1$ and $T_2$ are isomorphic.

### Naming algorithm

???+ note "Implementation"
    $$
    \begin{array}{ll}
    1 & \textbf{Input. } \text{A rooted tree }T\\
    2 & \textbf{Output. } \text{The name of rooted tree }T\\
    3 & \text{ASSIGN-NAME(u)}\\
    4 & \qquad \text{if  } u \text{  is a leaf}\\
    5 & \qquad \qquad \text{NAME(} u \text{) = (0)}\\
    6 & \qquad \text{else }\\
    7 & \qquad \qquad \text{for all child } v \text{ of } u\\
    8 & \qquad \qquad \qquad \text{ASSIGN-NAME(}v\text{)}\\
    9 & \qquad \text{sort the names of the children of }u\\
    10 & \qquad \text{concatenate the names of all children }u\text{ to temp}\\
    11 & \qquad \text{NAME(} u \text{) = (temp)}
    \end{array}
    $$

### AHU algorithm

???+ note "Implementation"
    $$
    \begin{array}{ll}
    1 & \textbf{Input. } \text{Two rooted trees }T_1(V_1,E_1,r_1)\text{ and }T_2(V_2,E_2,r_2) \\
    2 & \textbf{Output. } \text{Whether these two trees are isomorphic}\\
    3 & \text{AHU}(T_1(V_1,E_1,r_1), T_2(V_2,E_2,r_2))\\
    4 & \qquad \text{ASSIGN-NAME(}r_1\text{)}\\
    5 & \qquad \text{ASSIGN-NAME(}r_2\text{)}\\
    6 & \qquad \text{if  NAME}(r_1) = \text{NAME}(r_2)\\
    7 & \qquad \qquad \text{return true}\\
    8 & \qquad \text{else}\\
    10 & \qquad \qquad \text{return false}
    \end{array}
    $$

### Complexity proof

For a rooted tree with $n$ vertices that is a chain, the name of a vertex can have length up to $n$, so the complexity of ASSIGN-NAME is a constant multiple of $1+2+\cdots+n$, i.e. $\Theta(n^2)$. Hence the complexity of the naive AHU algorithm is $O(n^2)$.

## Optimized AHU algorithm

The drawback of the naive AHU algorithm is that the $NAME$ of a tree can be too long; this is what we optimize.

### Principle 1

Split the tree into levels: the vertices on level $i$ are at shortest distance $i$ from the root. The $NAME$ of a vertex on level $i$ can be obtained **only** by concatenating the $NAME$s of vertices on level $i+1$.

### Principle 2

Within one level, the $NAME$ of a vertex is uniquely identified by its rank within the level.

**Note** that the rank is taken over both trees: if vertex $u$ is on level $i$, its rank equals the number of vertices on level $i$ of $T_1$ and $T_2$ whose $NAME$ is smaller than $NAME(u)$.

### Corollary

We can replace the original $NAME$ of a vertex by its rank within the level, and replace the concatenation of $NAME$s by appending elements to an array.

Replacing strings by integers and arrays in this way does not affect the correctness of the algorithm and greatly reduces its complexity.

### Complexity proof

First note that the total length of the concatenated $NAME$s on level $i$ equals the sum of the degrees of the level-$i$ vertices, i.e. the number of vertices on level $i+1$; denote it $L_i$. The next step of the algorithm treats these $NAME$s as strings (arrays), sorts them, and replaces them by their rank within the level (i.e. remaps them to a number). The following lemmas give the complexity of sorting $m$ strings of total length $L$:

1.  Radix sort sorts them in $O(L+|\Sigma|)$ time, where $|\Sigma|$ is the alphabet size. (There are some implementation details; see the references.)
2.  Quicksort sorts them in $O(L \log m)$ time. Proof sketch: the recursion tree of quicksort has height $O(\log m)$, and comparing two strings of lengths $\ell_1$ and $\ell_2$ directly costs $O(\min\{\ell_1,\ell_2\})$.

In the AHU algorithm the alphabet size of the level-$i$ strings is at most the number of vertices on level $i+1$, i.e. $L_i$, so radix sort runs in linear time. Since $\sum_i L_i=O(n)$, summing the complexities over all levels shows that with radix sort of the strings the total complexity is $T(n)=O(n)$. Likewise, if quicksort is used to sort the strings, $T(n)=O(n \log n)$.

## Example

[SPOJ-TREEISO](https://www.spoj.com/problems/TREEISO/en/)

Problem summary: given two unrooted trees, decide whether they are isomorphic.

???+ note "Reference code"
    ```cpp
    --8<-- "docs/graph/code/tree-ahu/tree-ahu_1.cpp"
    ```

## References

Most of this article is translated from the [paper](http://wwwmayr.in.tum.de/konferenzen/Jass08/courses/1/smal/Smal_Paper.pdf) and the [slides](https://logic.pdmi.ras.ru/~smal/files/smal_jass08_slides.pdf). The proofs in the references are more complete and rigorous; this article simplifies them somewhat.

For the complexity analysis of the AHU algorithm and the linear-time radix sort of strings, see Section 3.2 Radix sorting of The Design and Analysis of Computer Algorithms, in particular Example 3.2.
