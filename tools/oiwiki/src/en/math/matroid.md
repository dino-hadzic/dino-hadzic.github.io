---
title: Matroids
---

## Introduction

A **matroid** is an abstract algebraic structure introduced by Hassler Whitney in 1935 with the aim of unifying and generalizing notions related to independence, such as linear independence in linear algebra and acyclicity in graph theory.

Matroids provide a powerful theoretical tool for optimization problems related to independence; they are widely used in combinatorics, graph theory, algorithm design and other fields, and they play an especially important role as the mathematical foundation of optimization methods such as greedy algorithms.

## Definition

### Matroid

A **matroid** is written as $M = (E, \mathcal{I})$, where:

-   $E$ is a finite set, called the **ground set**.
-   $\mathcal{I}$ is a family of subsets of $E$, called the **family of independent sets**; its members are called **independent sets**. It has the following three properties:

    -   **Non-emptiness**: the empty set is independent, i.e. $\emptyset \in \mathcal{I}$.

    -   **Hereditary property**: every subset of an independent set is also an independent set. If $I \in \mathcal{I}$, then for every $I' \subseteq I$ we have $I' \in \mathcal{I}$.

    -   **Exchange (augmentation) property**: if $I, J \in \mathcal{I}$ and $|I| < |J|$, then there exists $j \in J \setminus I$ such that $I \cup \{j\} \in \mathcal{I}$.

If a structure of the form $(E, \mathcal{I})$ satisfies the three properties above, it is called a matroid.

### Basis

A **basis** is a maximal independent set of the matroid, i.e. an independent set to which no element can be added while keeping it independent. The set of all bases is called the **family of bases** and is denoted $\mathcal{B}$.

**Properties**:

1.  **Equal cardinality**: all bases have the same size, called the **rank** of the matroid.

2.  **Augmentation property**: every independent set can be extended to a basis by adding elements of some basis.

### Circuit

A **circuit** is a minimal dependent set of the matroid, i.e. a set all of whose proper subsets are independent while the set itself is not independent; no two circuits contain one another.

### Rank

The **rank function** $r: 2^E \rightarrow \mathbb{Z}_{\geq 0}$ maps subsets of the ground set $E$ to nonnegative integers. For every $S \subseteq E$, $r(S)$ is defined as the size of the largest independent set contained in $S$, i.e.

$$
r(S) = \max \{ |I| \mid I \subseteq S \wedge I \in \mathcal{I} \}.
$$

**Properties**:

1.  **Non-negativity**: for every $S \subseteq E$ we have $0 \leq r(S) \leq |S|$.

2.  **Monotonicity**: if $A \subseteq B \subseteq E$, then $r(A) \leq r(B)$.

3.  **Submodularity**: for all $A, B \subseteq E$ we have $r(A \cup B) + r(A \cap B) \leq r(A) + r(B)$.

## Typical examples

### 1. Uniform matroid

**Definition**: given a ground set $E$ and a nonnegative integer $k$, the family of independent sets of the uniform matroid $U_{k,E}$ consists of all subsets of size at most $k$, i.e.

$$
\mathcal{I} = \{ I \subseteq E \mid |I| \leq k \}.
$$

-   **Bases**: all subsets of size $k$.

-   **Circuits**: all subsets of size $k + 1$.

-   **Rank**: $r(E) = \min(k, |E|)$, i.e. an independent set can contain at most $k$ elements.

### 2. Graphic matroid

**Definition**: given an undirected graph $G = (V, E)$, the ground set of the graphic matroid $M(G)$ is the edge set $E$, and its family of independent sets consists of all edge sets that contain no cycle, i.e. all forests.

-   **Bases**: the spanning trees of the graph (when the graph is connected). A spanning tree is a maximal independent set: no edge can be added without creating a cycle.

-   **Circuits**: the simple cycles of the graph; removing any edge from a cycle leaves an independent set.

-   **Rank**: $r(E) = |V|  - c$, where $c$ is the number of connected components of the graph. For a connected undirected graph the rank equals the number of vertices minus one, i.e. $|V|  - 1$.

### 3. Linear matroid

**Definition**: a linear matroid is based on a vector space. Given a vector space $V$, the ground set $E$ is a finite set of vectors from $V$, and the family of independent sets consists of all linearly independent subsets of $E$.

-   **Bases**: maximal linearly independent sets of vectors; their size equals the dimension of the vector space.

-   **Circuits**: minimal linearly dependent sets of vectors, i.e. sets all of whose proper subsets are independent while the set itself is linearly dependent.

-   **Rank**: the rank of a linear matroid is $r(E) = \dim(V)$, i.e. the dimension of the vector space. The size of an independent set cannot exceed the dimension of the vector space.

### 4. Partition matroid

**Definition**: partition the ground set $E$ into disjoint subsets $E_1, E_2, \dots, E_m$ and assign a nonnegative integer $k_i$ to each subset $E_i$. The family of independent sets of the partition matroid consists of the subsets that take at most $k_i$ elements from each part, i.e.

$$
\mathcal{I} = \left\{ I \subseteq E \mid \forall i,\, |I \cap E_i|  \leq k_i \right\}.
$$

-   **Bases**: the independent sets satisfying $|I \cap E_i| = k_i$ are the bases of the partition matroid. Every basis takes exactly $k_i$ elements from each subset.

-   **Circuits**: the circuits of a partition matroid are the minimal dependent sets, i.e. sets that contain more than $k_i$ elements from at least one subset.

-   **Rank**: the rank of a partition matroid is $r(E) = \sum_{i=1}^m k_i$, i.e. the size of the largest independent set equals the sum over the subsets of the maximum number of elements allowed from each.

### 5. Colored matroid

**Definition**: a colored matroid is a special form of partition matroid in which every element is assigned a color. Given a ground set $E$ and a set of colors $C$, every element $e \in E$ is associated with some color $c \in C$. Besides the independence condition of an ordinary matroid, the independent sets of a colored matroid must also obey the restrictions imposed on the colors, e.g. that an independent set may contain at most a certain number of elements of the same color.

-   **Bases**: the bases of a colored matroid are the maximal independent sets that satisfy the color restrictions and the independence condition.

-   **Circuits**: the circuits are the minimal dependent sets, i.e. sets of elements that violate independence or some color restriction.

-   **Rank**: the rank of a colored matroid is the size of the largest independent set satisfying the color restrictions. It depends both on the structure of the matroid and on the specific color restrictions.

## Constructions and operations

### Duality

Given a matroid $M = (E, \mathcal{I})$, its **dual matroid** $M^* = (E, \mathcal{I}^*)$ is defined by:

$$
\mathcal{I}^* = \{ I^* \subseteq E \mid \exists B \in \mathcal{I}, |B| = r(E), B \subseteq E \setminus I^* \}.
$$

**Properties**:

-   **Bases**: the bases of the dual matroid $M^*$ are the complements in the ground set $E$ of the bases of $M$. In other words, if $B$ is a basis of $M$, then $E \setminus B$ is a basis of $M^*$.

-   **Rank function**: the rank function of the dual matroid is $r^*(S) = |S| - r(E) + r(E \setminus S)$, where $S$ is a subset of $E$. This means the rank of the dual matroid can be computed from the size of the ground set, the rank of the original matroid, and the rank of the ground set with $S$ removed.

-   **Involutivity**: the dual of the dual matroid is the original matroid again, i.e. $(M^*)^* = M$.

**Example**:

For an undirected graph $G = (V, E)$, the dual $M(G)^*$ of the graphic matroid $M(G)$ is the matroid formed by the cut sets of the graph. The bases of the graphic matroid $M(G)$ are the spanning trees of the graph, the bases of its dual $M(G)^*$ are the complements of these spanning trees, and the circuits of the dual $M(G)^*$ are the minimal cut sets of the graph, i.e. the minimal edge sets whose removal splits the graph into two disconnected parts.

For example, consider a simple triangle graph $G$ with edge set $E = \{e_1, e_2, e_3\}$. The bases of the graphic matroid $M(G)$ are the two-edge sets (e.g. $\{e_1, e_2\}$), the bases of the dual matroid $M(G)^*$ are the single-edge sets (e.g. $\{e_3\}$), and the circuits of $M(G)^*$ are the two-edge sets (i.e. the minimal cut sets, e.g. $\{e_2,e_3\}$), since removing these edges splits the graph into two connected components.

### Deletion and contraction

**Deletion**:

For $A \subseteq E$, deleting $A$ from the matroid $M$ yields a new matroid $M \setminus A$ whose family of independent sets $\mathcal{I}'$ is defined as:

$$
\mathcal{I}' = \{ I \subseteq E \setminus A \mid I \in \mathcal{I} \}.
$$

We see that deletion simply removes some elements from the matroid and keeps the independent sets formed by the remaining elements; the original independent sets stay unchanged, only elements are removed.

**Contraction**:

For $A \subseteq E$, contracting $A$ in the matroid $M$ yields the matroid $M / A$ whose family of independent sets $\mathcal{I}''$ is defined as:

$$
\mathcal{I}'' = \left\{ I \subseteq E \setminus A \,\bigg|\, \exists B \subseteq A,\, B \in \mathcal{I},\, r(B) = r(A),\, I \cup B \in \mathcal{I} \right\}
$$

Contraction can be understood as shrinking the elements of the set $A$ and then considering the independent sets that the remaining elements form together with a basis of $A$. The result of the contraction depends on the basis of $A$; the independent sets after contraction are in fact the independent sets obtained by reducing the higher-rank subsets of the original matroid.

**Example – graphic matroid**:

-   **Deletion**: in a graphic matroid, deletion corresponds to removing some edges from the graph. After an edge is removed from a graph $G$, we consider the independent sets formed by the remaining edges, i.e. the edge sets without cycles. For example, if one edge is removed from a triangle graph, the remaining two edges still form a forest.

-   **Contraction**: contraction corresponds to shrinking an edge into a single vertex. In a graphic matroid, contracting an edge means merging its two endpoints into one vertex and removing that edge; after the vertices are merged, the other edges of the graph can still form independent sets. For example, in a triangle graph, contracting any edge merges two vertices into one, and the remaining two edges form a new matroid.

## Matroids and greedy algorithms

**Problem statement**:

One application of matroids is solving optimization problems with greedy algorithms. Concretely, we are given a matroid $M = (S, \mathcal{I})$, where $S$ is the ground set and $\mathcal{I}$ is the family of independent sets. Every element $x \in S$ is assigned a positive integer weight $w(x)$, and the goal is to find an independent set of maximum weight, formally:

$$
\max_{A \in \mathcal{I}} w(A) = \max_{A \in \mathcal{I}} \sum_{x \in A} w(x)
$$

Clearly, a maximum-weight independent set must be a maximal independent set. If an independent set $A$ is not maximal, there is an element $x$ that can be added to $A$, and since $w(x) > 0$, adding it increases the weight, so $A$ is not a maximum-weight independent set.

### Procedure

The greedy algorithm for a maximum-weight independent set proceeds as follows:

1.  **Sort the elements**: sort the ground set $S$ by weight in decreasing order; denote the resulting sequence by $e_1, e_2, \dots, e_n$.
2.  **Initialize**: set the independent set $A = \emptyset$.
3.  **Build the independent set**: consider the sorted elements $e_i$ in order; if $A \cup \{ e_i \} \in \mathcal{I}$, set $A = A \cup \{ e_i \}$.
4.  **Output**: the final set $A$ is a maximum-weight independent set.

**Complexity analysis**:

Let $n = |S|$ be the size of the ground set and let $f(n)$ be the complexity of checking whether a set is independent. The time complexity of the greedy algorithm is:

$$
O(n \log n + n f(n))
$$

where $O(n \log n)$ is the complexity of sorting and $O(n f(n))$ is the complexity of the successive independence checks.

???+ note "Note"
    -   In a graphic matroid, a [DSU (union-find)](../ds/dsu.md) can be used to detect cycles efficiently, making $f(n)$ nearly constant.
    -   In a linear matroid, the independence check usually involves matrix operations, and its complexity depends on the specific implementation.

**Proof of correctness**:

Let $M = (S, \mathcal{I})$ be a matroid, let $A \in \mathcal{I}$ be an independent set, and suppose $A$ is a subset of some maximum-weight independent set $T$. Define the set $P = \{ x \in S \setminus A \mid A \cup \{x\} \in \mathcal{I} \}$, i.e. the set of all elements that, when added to $A$, keep $A$ independent.

Let $y$ be the element of $P$ with the largest weight. Then $A' = A \cup \{ y \}$ is also a subset of some maximum-weight independent set, which we prove as follows:

Suppose $A' = A \cup \{ y \}$ is not a subset of any maximum-weight independent set. Then there is a maximum-weight independent set $T$ with $|A'| < |T|$.

Since $|A'|< |T|$, by the **exchange property** of matroids there exists $x \in T \setminus A'$ such that $A' \cup \{ x \} \in \mathcal{I}$.

Using the **exchange property**, we keep adding such $x$ to $A'$ and finally construct a new independent set $A''$ with $|A''| = |T|$.

Let $K = A'' \cap T$; then $x = T \setminus K$ and $y = A'' \setminus K$. Since $y$ is the element of $P$ with the largest weight, we have $w(x) \leq w(y)$.

Therefore $w(A'') = w(K) + w(y) \geq w(K) + w(x) = w(T)$, and:

-   if $w(A'') > w(T)$, then $T$ is not a maximum-weight independent set, contradicting the assumption;
-   if $w(A'') = w(T)$, then $A''$ is a maximum-weight independent set and $A'$ is a subset of it, contradicting the assumption that $A'$ is not a subset of any maximum-weight independent set.

Hence the assumption fails: $A' = A \cup \{ y \}$ must be a subset of some maximum-weight independent set, so by repeatedly applying the greedy strategy we eventually find a maximum-weight independent set.

### Example

**Minimum spanning tree**:

Given a connected undirected graph $G = (V, E)$ in which every edge $e \in E$ has a weight $w(e)$, the goal is to find a spanning tree that contains all vertices and has minimum total weight.

**Constructing the matroid**:

To formulate the minimum spanning tree problem as a matroid problem, we build the graphic matroid $M(G)$:

-   **Ground set**: $S = E$, i.e. all edges of the graph.
-   **Family of independent sets**: $\mathcal{I}$ consists of all edge sets without cycles (i.e. all forests).

**Greedy algorithm**:

Within the framework of the graphic matroid, [Kruskal's algorithm](../graph/mst.md#kruskals-algorithm) is the typical greedy algorithm based on matroid theory for building a minimum spanning tree. Although [Prim's algorithm](../graph/mst.md#prims-algorithm) is also an effective greedy algorithm that likewise finds a minimum spanning tree, it does not strictly rely on matroid greediness. Therefore, in discussions of matroid theory, Kruskal's algorithm is the main example of a greedy algorithm.

-   **Kruskal's algorithm**:
    1.  **Sort the edges**: sort all edges by weight in increasing order.
    2.  **Select step by step**: pick the edge of smallest weight in turn; if adding it does not create a cycle, add it to the spanning tree.
    3.  **Termination**: repeat the above until the spanning tree contains $|V| - 1$ edges.

-   **Prim's algorithm**:
    -   **Principle**: Prim's algorithm starts from an initial vertex and gradually grows the spanning tree, each time choosing the smallest-weight edge connecting a vertex inside the tree with a vertex outside it.
    -   Although Prim's algorithm is also greedy, its selection strategy differs from other greedy algorithms based on the exchange property of matroids. Therefore, in the strict sense of matroid theory, Prim's algorithm is not regarded as a typical matroid greedy algorithm.

## Matroid intersection

For two matroids $M_1 = (S, \mathcal{I}_1)$ and $M_2 = (S, \mathcal{I}_2)$ defined on the same ground set $S$, if $\mathcal{I} = \mathcal{I}_1 \cap \mathcal{I}_2$ satisfies the three properties of a family of independent sets of a matroid, then $M = (S, \mathcal{I})$ is called the **intersection** of $M_1$ and $M_2$.

**Note**: the intersection of two arbitrary matroids is not necessarily a matroid; it is a matroid only when the intersection of the families of independent sets satisfies the three properties in the definition of a family of independent sets.

### Problem statement

1.  **Maximum independent set**: find a largest independent set in $\mathcal{I}_1 \cap \mathcal{I}_2$ (i.e. an independent set of maximum cardinality).
2.  **Maximum-weight independent set**: given a weight function $w: S \to \mathbb{R}$, find an independent set in $\mathcal{I}_1 \cap \mathcal{I}_2$ with the largest sum of weights.

### Algorithm

**Unweighted version**:

1.  **Initialize**: choose an initial independent set $I \in \mathcal{I}_1 \cap \mathcal{I}_2$, usually $I = \emptyset$.
2.  **Iterate**:
    -   **Build the exchange graph**: build the exchange graph $D_{M_1, M_2}(I)$ based on the current independent set $I$.
    -   **Choose a path**: in the exchange graph, find an augmenting path $P$ from the source $s$ to the sink $t$.
    -   **Augment**: walk along the path $P$ from $s$ to $t$, node by node:
        -   if the node belongs to the left side (i.e. it is an element of $I$), remove that element from $I$;
        -   if the node belongs to the right side (i.e. it is an element of $S \setminus I$), add that element to $I$.
    -   **Repeat**: after updating the independent set $I$, repeat the above steps until no new augmenting path can be found.
3.  **Result**: the final independent set $I$ is a maximum independent set of the matroid intersection $M = M_1 \cap M_2$.

**Weighted version**:

To find an independent set with the largest sum of weights, the algorithm must choose the augmenting paths more carefully.

1.  **Set the weights**: for every element $e \in S$, define its weight $w'(e)$ in the exchange graph:
    -   **left-side nodes** (elements of $I$): $w'(e) = -w(e)$;
    -   **right-side nodes** (elements of $S \setminus I$): $w'(e) = w(e)$.
2.  **Choose a path**: in the exchange graph $D_{M_1, M_2}(I)$, look for an **augmenting path** $P$ from the source $s$ to the sink $t$ such that augmenting along it increases the total weight of the independent set $I$ the most.
    -   **Augmentation condition**: the total weight of the elements added along the path $P$ is larger than the total weight of the removed elements, i.e. $\sum_{y \in \text{added elements}} w(y) > \sum_{x \in \text{removed elements}} w(x)$
3.  **Augmentation operation**: walk along the path $P$ from $s$ to $t$, node by node:
    -   if the node belongs to the left side (i.e. it is an element of $I$), remove that element from $I$;
    -   if the node belongs to the right side (i.e. it is an element of $S \setminus I$), add that element to $I$.
4.  **Iterate**: repeat steps 1 to 3, rebuilding the exchange graph and looking for augmenting paths, gradually increasing the total weight of the independent set $I$.
5.  **Termination**: the algorithm stops when no path satisfying the augmentation condition can be found in the exchange graph.
6.  **Result**: the final independent set $I$ is a **maximum-weight independent set** of the matroid intersection $M = M_1 \cap M_2$.

**Complexity**:

-   **Number of augmentations**: if the ranks of the two matroids are $r_1$ and $r_2$, the maximum number of augmentations is $\min(r_1, r_2)$.

-   **Complexity of one augmentation**:
    -   building the exchange graph costs $O(n^2)$, where $n = |S|$;
    -   the complexity of finding an augmenting path depends on the search strategy and is usually $O(n^2)$, e.g. with breadth-first search.

-   **Total time complexity**: the overall time complexity is $O(r \cdot n^2)$, where $r = \min(r_1, r_2)$.

## Example problems

**Minimum spanning tree**:

Given an undirected graph $G = (V, E)$ in which every edge $e \in E$ has a weight $w(e)$, find a spanning tree that contains all vertices and has minimum total weight.

-   Detailed description: [Minimum spanning tree](../graph/mst.md).
-   Template problem: [Luogu P3366【模板】最小生成树 (template: minimum spanning tree)](https://www.luogu.com.cn/problem/P3366).

??? note "Solution idea"
    Use Kruskal's algorithm: sort all edges by weight in increasing order, then pick them one by one and, if adding an edge does not create a cycle, add it to the spanning tree; the resulting spanning tree is a minimum spanning tree.

**Colorful Graph**:

Given an undirected graph $G = (V, E)$ with several colors, where every edge has a color, find a largest edge set such that:

1.  the chosen edges do not form any cycle;
2.  the number of edges of each color is at most $k$ (where $k$ is a given positive integer).

??? note "Solution idea"
    1.  **Matroid modeling**:
    
        -   **Graphic matroid ($M_1$)**: defined as the edge sets that form no cycle, i.e. the family of independent sets $\mathcal{I}_1$ contains all edge sets without cycles.
        -   **Color matroid ($M_2$)**: defined as the edge sets in which the number of edges of each color is at most $k$, i.e. the family of independent sets $\mathcal{I}_2$ contains all edge sets in which the number of edges of each color is $\leq k$.
    2.  **Solve the matroid intersection**: by solving $M = M_1 \cap M_2$, we find a largest edge set that forms no cycle and has at most $k$ edges of each color.

**Constrained resource allocation problem**:

In a resource allocation problem there is a set of resources $R = \{r_1, r_2, \dots, r_n\}$ and a set of projects $P = \{p_1, p_2, \dots, p_m\}$. Every project $p_i$ needs to be allocated a certain amount of resources, and the total amount allocated of each resource must not exceed its supply.

**Goal**: find a resource allocation that satisfies the demands of all projects without exceeding the resource supplies.

??? note "Solution idea"
    1.  **Matroid modeling**:
    
        -   **Demand matroid ($M_1$)**: defined as the allocations that satisfy the resource demands of the projects, i.e. the family of independent sets $\mathcal{I}_1$ contains all sets of resource assignments that satisfy the project demands.
        -   **Supply matroid ($M_2$)**: defined as the allocations that do not exceed the supply of any resource, i.e. the family of independent sets $\mathcal{I}_2$ contains all sets of resource assignments that respect the supply limits.
    2.  **Solve the matroid intersection**: by solving $M = M_1 \cap M_2$, we find a resource allocation that satisfies the demands of all projects without exceeding the resource supplies.

## References and notes

1.  [Wikipedia – Matroid](https://en.wikipedia.org/wiki/Matroid)
2.  [Baidu Baike – 拟阵 (Matroid)](https://baike.baidu.com/item/%E6%8B%9F%E9%98%B5)
3.  [Luogu – 拟阵与最优化问题 (Matroids and optimization problems)](https://www.luogu.com.cn/article/87d02q9f)
4.  [Luogu – 从拟阵基础到 Shannon 开关游戏 (From matroid basics to the Shannon switching game)](https://www.luogu.com.cn/article/fuj3x886)
