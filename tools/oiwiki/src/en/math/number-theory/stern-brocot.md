---
title: Stern–Brocot Tree and Farey Sequence
---

## Introduction

This article introduces a data structure that stores irreducible fractions, together with other related concepts. They are closely related to [continued fractions](./continued-fraction.md), can be used in algorithm competitions to solve a range of number-theoretic problems, and may appear as the hidden background of some problems.

## Stern–Brocot Tree

The Stern–Brocot tree is an elegant structure for maintaining fractions that contains all distinct positive rational numbers. The structure was discovered independently by Moritz Stern in 1858 and by Achille Brocot in 1861.

### Construction

#### Level-by-Level Construction

The Stern–Brocot tree can be obtained while iteratively constructing the Stern–Brocot sequence of order $k$ for increasing $k$. The Stern–Brocot sequence of order $0$ consists of two simple fractions:

$$
\frac{0}{1},\ \frac{1}{0}.
$$

Here $\dfrac{1}{0}$ is, strictly speaking, not a rational fraction; it can be understood as the irreducible fraction representing $\infty$.

Inserting between every two adjacent fractions $\dfrac{a}{b}$ and $\dfrac{c}{d}$ of the Stern–Brocot sequence of order $k$ their mediant[^mediant] $\dfrac{a+c}{b+d}$ yields the Stern–Brocot sequence of order $k+1$. Although the definition of the mediant itself allows the fraction to be reduced, in the construction of the Stern–Brocot tree it suffices to simply add the numerators and the denominators, without worrying about reduction. In this way the Stern–Brocot sequences of all orders can be constructed iteratively. The results of the first few iterations are as follows:

$$
\begin{array}{ccccccccc}
&&&\dfrac{0}{1}, & \dfrac{1}{1}, & \dfrac{1}{0} &&&\\\\
&&\dfrac{0}{1}, & \dfrac{1}{2}, & \dfrac{1}{1}, & \dfrac{2}{1}, & \dfrac{1}{0} &&\\\\
\dfrac{0}{1}, & \dfrac{1}{3}, & \dfrac{1}{2}, & \dfrac{2}{3}, & \dfrac{1}{1}, & \dfrac{3}{2}, & \dfrac{2}{1}, & \dfrac{3}{1}, & \dfrac{1}{0}
\end{array}
$$

Connecting the fractions newly added in each iteration into a tree structure gives the Stern–Brocot tree, as shown in the figure below:

![](./images/stern-brocot-tree.svg)

The Stern–Brocot sequence of order $k$, excluding the left and right endpoints, is exactly the in-order traversal of the Stern–Brocot tree of depth $k-1$.

#### Construction by Triples

Another equivalent construction takes the triple

$$
\left(\dfrac{0}{1},\dfrac{1}{1},\dfrac{1}{0}\right)
$$

as the root node and, after every node

$$
\left(\dfrac{a}{b},\dfrac{p}{q},\dfrac{c}{d}\right)
$$

appends

$$
\left(\dfrac{a}{b},\dfrac{a+p}{b+q},\dfrac{p}{q}\right),\ \left(\dfrac{p}{q},\dfrac{p+c}{q+d},\dfrac{c}{d}\right)
$$

as its left and right children respectively; this constructs the whole Stern–Brocot tree. In the triple recorded at each node of the Stern–Brocot tree, the fraction actually stored is the middle fraction $\dfrac{p}{q}$ of the triple, while the left and right fractions $\dfrac{a}{b}$ and $\dfrac{c}{d}$ are fractions that appeared earlier. Moreover, considering the previous construction, one sees that the fraction $\dfrac{p}{q}$ is exactly the one obtained by inserting the mediant of $\dfrac{a}{b}$ and $\dfrac{c}{d}$.

#### Matrix Representation and the Stern–Brocot Number System

The construction by triples means that every node of the Stern–Brocot tree corresponds to a matrix

$$
S = \begin{pmatrix}
b & d\\
a & c
\end{pmatrix}.
$$

The root of the Stern–Brocot tree is the identity matrix $I$, and moving to the left child or to the right child corresponds to multiplying the matrix of the current node on the right by the matrix

$$
L=\begin{pmatrix}
1 & 1 \\
0 & 1
\end{pmatrix},~
R=\begin{pmatrix}
1 & 0 \\
1 & 1
\end{pmatrix}.
$$

The fraction actually corresponding to each node is $f(S)=\dfrac{a+c}{b+d}$. The matrix $S$ of every node can be written as a product of a sequence of matrices $L$ and $R$, which can also be understood as a string over $L$ and $R$ representing the path from the root to that node. All positive rational numbers are thus uniquely represented by such strings, which can be regarded as a representation of the positive rationals; hence it is also called the **Stern–Brocot number system**.

#### Implementation of Tree Construction

The tree construction algorithm simply simulates the process above. Below is the code that performs an in-order traversal of the first $n$ levels of the Stern–Brocot tree.

???+ example "Tree construction"
    === "C++"
        ```cpp
        --8<-- "docs/math/code/stern-brocot/tree-build.cpp:core"
        ```
    
    === "Python"
        ```py
        --8<-- "docs/math/code/stern-brocot/tree-build.py:core"
        ```

The complexity of the tree construction algorithm is $O(2^n)$.

### Properties

We now discuss the properties of the Stern–Brocot tree. In short, the Stern–Brocot tree is a [binary search tree](../../ds/bst.md) containing all positive irreducible rational fractions; it is also a [heap](../../ds/binary-heap.md) with respect to numerators and with respect to denominators, and a [Cartesian tree](../../ds/cartesian-tree.md) of the pairs (denominator, numerator). If one considers the intervals formed by the left and right endpoints in the construction by triples above, the Stern–Brocot tree can also be viewed as a [segment tree](../../ds/seg.md) over $[0,\infty]$. These statements can be derived from the following three basic properties:

#### Monotonicity

In the construction above, the fractions on every level are strictly increasing. This only needs an inductive proof. Indeed, if $\dfrac{a}{b} < \dfrac{c}{d}$, then necessarily

$$
\dfrac{a}{b} < \dfrac{a+c}{b+d} < \dfrac{c}{d}.
$$

This follows by clearing the denominators of the inequality. The base case is $\dfrac{0}{1} < \dfrac{1}{0}$, where monotonicity obviously holds.

#### Irreducibility

In the construction above, every fraction is irreducible. For this one likewise proves by induction that in the construction above, any two adjacent fractions $\dfrac{a}{b}$ and $\dfrac{c}{d}$ on the same level satisfy the equation

$$
bc-ad = \det\begin{pmatrix}
b & d\\
a & c
\end{pmatrix} = 1.
$$

At the root this is the identity matrix, so it obviously holds. When moving down, the matrices $L$ and $R$ we multiply by both have determinant $1$, so by the properties of the [determinant](../linear-algebra/determinant.md) it holds on the next level as well:

$$
\det\begin{pmatrix}b & b+d \\ a & a+c \end{pmatrix} = \det\begin{pmatrix}b+d & d \\ a+c & c\end{pmatrix} = 1.
$$

For the base case $\dfrac{0}{1}$ and $\dfrac{1}{0}$ this is also obvious. Consequently, by [Bézout's identity](./bezouts.md), the numerator and denominator of every fraction are necessarily coprime, i.e., all fractions are irreducible.

#### Completeness

Finally, we need to show that the Stern–Brocot tree contains all positive irreducible fractions. Since the first two properties already show that the Stern–Brocot tree is a binary search tree, and any positive irreducible fraction $\dfrac{p}{q}$ necessarily lies between $\dfrac{0}{1}$ and $\dfrac{1}{0}$, by the way searching in a binary search tree works, the only possibility for $\dfrac{p}{q}$ to be absent from the binary search tree is that the search process is infinitely long. We will prove below that for any positive rational number $\dfrac{p}{q}$, an infinitely long search process is impossible.

Let the lower bound for $\dfrac{p}{q}$ obtained during the search be $\dfrac{a}{b}$ and the upper bound be $\dfrac{c}{d}$. The initial lower bound is $\dfrac{0}{1}$, the initial upper bound is $\dfrac{1}{0}$, and afterwards the bounds are gradually adjusted according to the result of comparing $\dfrac{a+c}{b+d}$ with $\dfrac{p}{q}$. If the search process were infinitely long, then at every step

$$
\dfrac{a}{b} < \dfrac{p}{q} < \dfrac{c}{d},
$$

so for infinitely many steps we would necessarily have

$$
bp-aq \ge 1,\ cq-dp \ge 1.
$$

Multiplying the two inequalities by $(c+d)$ and $(a+b)$ respectively, we obtain

$$
(c+d)(bp-aq) + (a+b)(cq-dp) \ge a+b+c+d.
$$

Using the identity $bc-ad=1$ established earlier, this simplifies to

$$
p+q \ge a+b+c+d.
$$

However, each time the search goes one level deeper, the right-hand side of the inequality strictly increases while the left-hand side stays the same, so the above condition cannot hold for infinitely many steps. Therefore the search process stops after finitely many steps.

### Finding a Fraction

In practical applications of the Stern–Brocot tree, one frequently needs to query the position of a given fraction in the Stern–Brocot tree.

#### Naive Algorithm

Since the Stern–Brocot tree is a binary search tree, it suffices to compare the current fraction with the fraction being sought to determine the path from the root to the given fraction. Denoting a move to the left child and a move to the right child on the path by $L$ and $R$ respectively, every path corresponds to a string over $L$ and $R$, which is exactly the representation of the rational number in the Stern–Brocot number system mentioned above. Finding the path leading to some rational number amounts to finding the representation of that rational number in the Stern–Brocot number system.

The implementation of the naive fraction-finding algorithm is as follows:

???+ example "Naive fraction finding"
    === "C++"
        ```cpp
        --8<-- "docs/math/code/stern-brocot/fraction-finding-1.cpp:core"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/math/code/stern-brocot/fraction-finding-1.py:core"
        ```

The complexity of the algorithm is $O(p+q)$, so it is not practical in algorithm competitions.

In the Stern–Brocot number system, every positive irrational number corresponds to a unique infinitely long string. The same algorithm can be used to construct this string. Every prefix of this infinitely long string corresponds to a rational irreducible fraction. Arranging these irreducible fractions in a sequence, the denominators of the fractions in the sequence are strictly increasing, and the limit of the sequence is the irrational number. Therefore the Stern–Brocot tree can be used to find a rational approximation of an irrational number to any precision. Note, however, that the gap between this sequence of rationals and the irrational number is not strictly decreasing. For the rigorous theory of rational approximation, refer to the section [Diophantine approximation](./continued-fraction.md#丢番图逼近) on the continued fractions page. When using the Stern–Brocot tree in practice to find the best approximation of a real number with denominator not exceeding a given bound, one should finally compare the distances from the left and right endpoints of the interval to that real number.

#### Fast Algorithm

The naive fraction-finding algorithm is not efficient, but a simple optimization gives a fast finding algorithm with complexity $O(\log(p+q))$. The key to the optimization is to process consecutive $L$'s and $R$'s together.

If the fraction $\dfrac{p}{q}$ being sought falls between $\dfrac{a}{b}$ and $\dfrac{c}{d}$, then during $t$ consecutive moves to the right the right boundary stays fixed while the left boundary moves to $\dfrac{a+tc}{b+td}$; conversely, during $t$ consecutive moves to the left the left boundary stays fixed while the right boundary moves to $\dfrac{ta+c}{tb+d}$. Therefore the number of moves to the right and to the left can be determined directly via $\dfrac{a+tc}{b+td}<\dfrac{p}{q}$ or $\dfrac{p}{q}<\dfrac{ta+c}{tb+d}$. Strict inequalities are used here because the algorithm moves the left and right endpoints, while the fraction being sought appears as the mediant of the finally obtained endpoints.

???+ example "Fast fraction finding"
    === "C++"
        ```cpp
        --8<-- "docs/math/code/stern-brocot/fraction-finding-2.cpp:core"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/math/code/stern-brocot/fraction-finding-2.py:core"
        ```

The current finding algorithm requires the fraction $\dfrac{p}{q}$ to be known. If the target fraction is unknown, one usually needs to find the number of moves by doubling (binary lifting) or by binary search at each move to the right or to the left. In that case the complexity of the fraction-finding algorithm is $O(\log^2(p+q))$.

#### Algorithm Based on Continued Fractions

For the case where the fraction is known, continued fractions give an even simpler algorithm. Without loss of generality, assume the first group of moves is to the right; otherwise, let the number of moves in the first group of right moves be zero. Move the endpoints alternately to the right and to the left, and arrange the positions of the endpoints after each group of moves as follows:

$$
\dfrac{p_0}{q_0},~\dfrac{p_1}{q_1},~\dfrac{p_2}{q_2},~\cdots,~\dfrac{p_{n-2}}{q_{n-2}},~\dfrac{p_{n-1}}{q_{n-1}},~\dfrac{p_n}{q_n}.
$$

Here the even-numbered groups of moves go to the right, so they record the position of the left endpoint; the odd-numbered groups go to the left, so they record the position of the right endpoint. Prepend two more endpoints to this list of endpoints:

$$
\dfrac{p_{-2}}{q_{-2}}=\dfrac{0}{1},~\dfrac{p_{-1}}{q_{-1}}=\dfrac{1}{0}.
$$

Let the number of moves in the $k$-th group be $t_k$; then by the relation between the number of moves and the positions of the endpoints obtained above,

$$
\dfrac{p_k}{q_k} = \dfrac{t_kp_{k-1}+p_{k-2}}{t_kq_{k-1}+q_{k-2}}.
$$

By the [recurrence relation](./continued-fraction.md#递推关系) of continued fractions, the endpoint is

$$
\dfrac{p_k}{q_k} = [t_0,t_1,\cdots,t_k].
$$

The continued fraction finally obtained is

$$
\dfrac{p}{q} = \dfrac{p_n+p_{n-1}}{q_n+q_{n-1}} = [t_0,t_1,\cdots,t_{n-1},t_n,1].
$$

Therefore, in the [continued fraction representation](./continued-fraction.md#简单连分数) of the target fraction ending in one, the terms before the final one encode the path from the root to the current node in the Stern–Brocot tree. Among them, the even-indexed terms (indices starting from $0$) are edges to the right child, and the odd-indexed terms are edges to the left child.

The continued fraction representation of a rational number can be obtained by the Euclidean algorithm, so the complexity of the fraction-finding algorithm based on the continued fraction representation is $O(\log\min\{p,q\})$.

???+ example "Fraction finding based on continued fractions"
    === "C++"
        ```cpp
        --8<-- "docs/math/code/stern-brocot/fraction-finding-3.cpp:core"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/math/code/stern-brocot/fraction-finding-3.py:core"
        ```

Using the continued fraction representation, the parent and children of a node can be expressed simply. For the node $[t_0,t_1,\cdots,t_n,1]$, its parent is the node with one fewer move in the direction of the last move: when $t_n>1$, the parent is $[t_0,t_1,\cdots,t_n - 1,1]$; otherwise, the parent is $[t_0,t_1,\cdots,t_{n-1},1]$. Its two children are $[t_0,t_1,\cdots,t_n+1,1]$ and $[t_0,t_1,\cdots,t_n,1,1]$ respectively; which of the two nodes is the left child and which is the right child is determined by the parity of $n$.

## Calkin–Wilf Tree

Another, simpler structure for storing positive rational fractions is the Calkin–Wilf tree. It is usually shown as follows:

![pic](./images/calkin-wilf-tree.svg)

The root of the tree is $\dfrac{1}{1}$. Then, for the node holding the fraction $\dfrac{p}{q}$, its left and right children are $\dfrac{p}{p+q}$ and $\dfrac{p+q}{q}$ respectively. Similarly to the Stern–Brocot tree, each of its fractions is irreducible, and it contains every positive irreducible fraction exactly once.

### Relation to Continued Fractions

Unlike the Stern–Brocot tree, the Calkin–Wilf tree is not a binary search tree, so it cannot be used for binary searching rational numbers.

In the Calkin–Wilf tree, when $p>q$, the parent of the fraction $\dfrac{p}{q}$ is $\dfrac{p-q}{q}$; when $p<q$, it is $\dfrac{p}{q-p}$. In the first case, starting from $\dfrac{p}{q}$, it is the right child of its parent, and one can keep moving up through the right side of the parent until the numerator is no longer greater than the denominator; the fraction stored at that node is $\dfrac{p\bmod q}{q}$, and the number of moves in this group is $\left\lfloor\dfrac{p}{q}\right\rfloor$. In the second case, it is the left child of its parent, and one can keep moving up through the left side of the parent until the denominator is no longer greater than the numerator; the fraction stored at that node is $\dfrac{p}{q\bmod p}$, and the number of moves in this group is $\left\lfloor\dfrac{q}{p}\right\rfloor$.

In the language of continued fractions, suppose the current node stores the remainder $s_k$ of some continued fraction; then moving up through the right side of the parent $\lfloor s_k\rfloor$ times reaches the fraction $\dfrac{1}{s_{k+1}}$, and then moving through the left side of the parent $\lfloor s_{k+1}\rfloor$ times reaches the fraction $s_{k+2}$. Therefore, the path from the node $s_0=\dfrac{p}{q}$ up to the root $\dfrac{1}{1}$ is encoded by the continued fraction $[t_0,t_1,\cdots,t_n,1]$: excluding the final $1$, the even-indexed terms (indices starting from $0$) denote the number of moves through the right side of the parent, and the odd-indexed terms denote the number of moves through the left side of the parent.

For the node holding the fraction $\dfrac{p}{q}=[t_0,t_1,\cdots,t_n,1]$, its parent has the following representation:

1.  when $t_0>0$, its parent is $\dfrac{p-q}{q}=[t_0 - 1, t_1, \cdots, t_n,1]$;
2.  when $t_0=0$ and $t_1>1$, its parent is $\dfrac{p}{q-p} = [0, t_1 - 1, t_2, \cdots, t_n,1]$;
3.  when $t_0=0$ and $t_1=1$, its parent is $\dfrac{p}{q-p} = [t_2, t_3, \cdots, t_n,1]$.

Conversely, its children are $\dfrac{p+q}{q}=[t_0+1,t_1,\cdots,t_n,1]$ and $\dfrac{p}{p+q}=[0,1,t_0,t_1,\cdots,t_n,1]$ respectively. For the continued fraction representation of the second child, when $t_0=0$, it should be understood as $[0,1+t_1,t_2,\cdots,t_n,1]$.

### Relation to the Stern–Brocot Tree

Again in connection with continued fractions: the nodes on a path in the Stern–Brocot tree exhibit the recurrence relation of the convergents, while the nodes on a path in the Calkin–Wilf tree exhibit the recurrence relation of the remainders. The continued fraction representation of a given fraction is fixed, so the encoding of its path to the root in the Calkin–Wilf tree is exactly the same as the encoding of the path from the root to it in the Stern–Brocot tree. However, since the directions of the paths are opposite, although the fractions stored on the same level of the Stern–Brocot tree and the Calkin–Wilf tree are the same, their positions are not.

If one performs a [breadth-first search](../../graph/bfs.md) on each of the two trees and numbers the nodes in order, with the root numbered $1$, then the left and right children of the node numbered $v$ are $2v$ and $2v+1$ respectively. Looking at the binary representation of the number, excluding the leading $1$, from the most significant bit to the least significant bit every $1$ denotes a move to the right child and every $0$ denotes a move to the left child. In the Calkin–Wilf tree, the number of the node holding the rational number represented by the continued fraction $[t_0,t_1,\cdots,t_n,1]$ is

$$
1\cdots \underbrace{0\cdots 0}_{t_3}\underbrace{1\cdots 1}_{t_2}\underbrace{0\cdots 0}_{t_1}\underbrace{1\cdots 1}_{t_0}.
$$

Correspondingly, in the Stern–Brocot tree, the number of the node holding the rational number represented by the continued fraction $[t_0,t_1,\cdots,t_n,1]$ is

$$
1\underbrace{1\cdots 1}_{t_0}\underbrace{0\cdots 0}_{t_1}\underbrace{1\cdots 1}_{t_2}\underbrace{0\cdots 0}_{t_3}\cdots.
$$

Deleting the leading $1$, the number formed by the remaining binary digits is exactly the index of the node within its level, counted from left to right (starting from $0$). This derivation shows that the arrangements of the fractions on the same level of the Stern–Brocot tree and the Calkin–Wilf tree are related by the bit-reversal permutation, i.e., the permutation of $0\sim (2^k-1)$ obtained by reversing the binary digits of the index (padded with leading $0$'s).

For this reason, the nodes of the Stern–Brocot tree are sometimes numbered according to the numbers of the corresponding nodes of the Calkin–Wilf tree; the resulting numbering is shown in the figure below:

![pic](./images/stern-brocot-index.svg)

This numbering can be constructed recursively: the root is numbered $1$; every time one moves to the left child, the leading $1$ of the number is replaced by $10$, and when one moves to the right child, the leading $1$ of the number is replaced by $11$. Reading this number from right to left yields the path from the root to that node.

### Stern's Diatomic Sequence

Arranging all fractions of the Calkin–Wilf tree according to their breadth-first search numbers, or all fractions of the Stern–Brocot tree according to the numbering shown in the figure above, yields the following sequence:

$$
\dfrac{1}{1},~\dfrac{1}{2},~\dfrac{2}{1},~\dfrac{1}{3},~\dfrac{3}{2},~\dfrac{2}{3},~\dfrac{3}{1},~\dfrac{1}{4},~\dfrac{4}{3},~\dfrac{3}{5},~\dfrac{5}{2},\cdots.
$$

Using the construction process of the Calkin–Wilf tree, one can prove that for any two adjacent fractions in this sequence, the denominator of the former necessarily equals the numerator of the latter. Listing the numerators alone gives Stern's diatomic sequence ([OEIS A002487](https://oeis.org/A002487)), also called the Stern–Brocot sequence. The numbering of the above sequence starts from $1$, and additionally the $0$-th number is defined to be $0$.

Let $a_n$ be the $n$-th number of Stern's diatomic sequence; then it satisfies the following recurrence relation:

$$
\begin{aligned}
a_{2n} &= a_n,\\
a_{2n+1} &= a_n + a_{n+1}. 
\end{aligned}
$$

The base cases are $a_0=0$ and $a_1=1$. To compute the value $a_n$ of Stern's diatomic sequence, directly using the recurrence relation has complexity $O(\log^2n)$, which is not good. A better approach is to regard it as the numerator of the fraction numbered $n$ in the Calkin–Wilf tree and compute it using the continued-fraction-based recurrence described above, with complexity $O(\log n)$.

## Farey Sequence

The Farey sequence has features extremely similar to the Stern–Brocot tree. Denote the **Farey sequence of order $n$** by $F_n$. For a given $n$, it is the sequence formed by arranging in increasing order all irreducible fractions in $[0,1]$ whose denominators are at most $n$:

$$
\begin{array}{lllllllllllll}
F_1=\bigg\{&\dfrac{0}{1},&&&&&&&&&&\dfrac{1}{1}&\bigg\}\\\\
F_2=\bigg\{&\dfrac{0}{1},&&&&&\dfrac{1}{2},&&&&&\dfrac{1}{1}&\bigg\}\\\\
F_3=\bigg\{&\dfrac{0}{1},&&&\dfrac{1}{3},&&\dfrac{1}{2},&&\dfrac{2}{3},&&&\dfrac{1}{1}&\bigg\}\\\\
F_4=\bigg\{&\dfrac{0}{1},&&\dfrac{1}{4},&\dfrac{1}{3},&&\dfrac{1}{2},&&\dfrac{2}{3},&\dfrac{3}{4},&&\dfrac{1}{1}&\bigg\}\\\\
F_5=\bigg\{&\dfrac{0}{1},&\dfrac{1}{5},&\dfrac{1}{4},&\dfrac{1}{3},&\dfrac{2}{5},&\dfrac{1}{2},&\dfrac{3}{5},&\dfrac{2}{3},&\dfrac{3}{4},&\dfrac{4}{5},&\dfrac{1}{1}&\bigg\}
\end{array}
$$

By the definition of the Farey sequence, it naturally satisfies monotonicity, irreducibility and completeness. As shown above, the fractions that $F_k$ adds compared to $F_{k-1}$ are always mediants of adjacent fractions in $F_{k-1}$.

The algorithm for building the Stern–Brocot tree described above applies equally to building the Farey sequence. Since the Stern–Brocot tree contains all irreducible fractions, it suffices to change the boundary condition to a restriction on the denominator to obtain code constructing the Farey sequence. The Farey sequence of order $n$, $F_n$, can be viewed as a subsequence of the Stern–Brocot sequence of order $n$.

???+ example "Constructing the Farey sequence"
    === "C++"
        ```cpp
        --8<-- "docs/math/code/stern-brocot/farey-build.cpp:core"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/math/code/stern-brocot/farey-build.py:core"
        ```

The complexity of constructing the Farey sequence directly is $O(|F_n|)=O(n^2)$.

### Sequence Length and Finding a Fraction

The length of the Farey sequence can be computed recursively. Compared to $F_{n-1}$, the extra fractions in the sequence $F_n$ all have denominator $n$, with numerator not exceeding $n$ and coprime to $n$, hence:

$$
\begin{aligned}
|F_n| &= |F_{n-1}| + \varphi(n) = 1 + \sum_{k=1}^n\varphi(k).
\end{aligned}
$$

Here $\varphi(n)$ is [Euler's totient function](./euler-totient.md). This expression can be computed in $O(n)$ using the [linear sieve](./sieve.md#筛法求欧拉函数), and the complexity can be reduced to $O(n^{2/3})$ using [Du's sieve](./hyperbola.md#杜教筛).

More common than computing the length of the sequence directly is the situation where one needs to find the index of some fraction $r=\dfrac{p}{q}$ in the sequence $F_n$. This amounts to evaluating

$$
1 + \sum_{k = 1}^n\sum_{i=1}^{\lfloor rk\rfloor}[i\perp k] = 1 + \sum_{d=1}^n\mu(d)\sum_{j=1}^{\lfloor n/d\rfloor}\lfloor rj\rfloor.
$$

To obtain the right-hand side, [Möbius inversion](./mobius.md) is applied. Combining the linear sieve with enumeration of divisors gives $O(n)$ preprocessing and $O(n\log n)$ per query; combining Du's sieve with the [Euclidean-like algorithm](./euclidean.md) gives $O(n^{2/3})$ preprocessing and $O(\sqrt n\log n)$ per query.

Conversely, finding the fraction from a known index requires binary searching over the real numbers in $[0,1]$, or [binary searching](#fast-algorithm) in the Stern–Brocot tree. The former may be limited by floating-point precision, with $O(\log V)$ queries for the index of a fraction, where $V$ is the precision range; the latter is not limited by floating-point precision, but requires $O(\log^2n)$ queries for the index of a fraction.

### Farey Neighbors

If the fractions $\dfrac{a}{b}$ and $\dfrac{c}{d}$ are adjacent in some Farey sequence, they are called **Farey neighbors**, also known as a Farey pair.

Let $\dfrac{a}{b}<\dfrac{c}{d}$. From the construction process of the Farey sequence, of two adjacent fractions the one added later is necessarily the mediant of the other fraction and its previous neighbor, so Farey neighbors are also adjacent in the Stern–Brocot sequence of some order; by the conclusion proved in [Irreducibility](#irreducibility), necessarily

$$
bc-ad=1.
$$

Conversely, this is also a sufficient condition for two irreducible proper fractions to be Farey neighbors. Let us show this. Without loss of generality, let $\dfrac{a}{b}$ be the one of the two fractions with the larger denominator; then both fractions appear in $F_b$. Let $\dfrac{e}{f}$ be the term immediately to the right of $\dfrac{a}{b}$ in the sequence $F_b$; by the necessity already shown, $be-af=1$. However, the [linear congruence](./linear-equation.md) $bx-ay=1$ has only one positive integer solution with $y\le b$, so necessarily $(e,f)=(c,d)$.

In fact, since the next irreducible fraction to appear between them is necessarily $\dfrac{a+c}{b+d}$, the fractions $\dfrac{a}{b}$ and $\dfrac{c}{d}$ are adjacent in the Farey sequences of order $\max\{b,d\}$ through $(b+d-1)$.

The Farey neighbor relation for denominators not exceeding $9$ is shown in the figure below:

![](./images/farey-diagram-ford-circle.svg)

The circles in the figure are called [Ford circles](https://en.wikipedia.org/wiki/Ford_circle): for every irreducible fraction $\dfrac{p}{q}$ in $[0,1]$, a circle is drawn with center $\left(\dfrac{p}{q},\dfrac{1}{2q^2}\right)$ and radius $\dfrac{1}{2q^2}$. The figure shows that the Ford circles corresponding to two fractions can only be tangent or disjoint, and the two circles are tangent if and only if the two fractions are Farey neighbors. Moreover, for any two tangent circles in the figure, there always exists a unique third circle tangent to both. The fraction corresponding to this third circle is exactly the mediant of the fractions corresponding to the two circles.

To verify that tangent circles always correspond to Farey neighbors, one can directly compute the distance between the two centers:

$$
\left(\dfrac{a}{b}-\dfrac{c}{d}\right)^2 + \left(\dfrac{1}{2b^2}-\dfrac{1}{2d^2}\right)^2 = \left(\dfrac{1}{2b^2}+\dfrac{1}{2d^2}\right)^2+\frac{(bc-ad)^2-1}{b^2d^2}.
$$

Since the two irreducible fractions are distinct, $|bc-ad|\ge 1$, so the two circles can only be tangent or disjoint. Moreover, the two circles are tangent if and only if $|bc-ad|=1$, which is equivalent to the two fractions being Farey neighbors.

Finally, let us count the number of Farey neighbor pairs. Except for $\left(\dfrac{0}{1},\dfrac{1}{1}\right)$, all other Farey neighbors have different denominators. Without loss of generality, let $\dfrac{p}{q}$ be the one with the larger denominator; then the other fraction can necessarily be obtained from the linear Diophantine equation in two variables

$$
qx-py=\pm 1
$$

Each of the two equations has exactly one positive integer solution satisfying $y<q$, corresponding to the neighbors to the left and to the right of $\dfrac{p}{q}$ respectively. Hence every proper fraction in $(0,1)$ has two Farey neighbors with denominators smaller than its own; adding $\dfrac{0}{1}$ and $\dfrac{1}{1}$, this shows that the sequence $F_n$ has a total of $(2|F_n|-3)$ pairs of Farey neighbors.

Of course, the fractions $\dfrac{a}{b}<\dfrac{c}{d}$ found in this process are exactly the left and right neighbors of $\dfrac{p}{q}$ when it is inserted into the sequence. Hence they are themselves Farey neighbors and $\dfrac{p}{q}$ is their mediant. Let $\dfrac{p}{q}=[t_0,t_1,\cdots,t_n,1]$; then these two Farey neighbors with smaller denominators are $[t_0,t_1,\cdots,t_n]$ and $[t_0,t_1,\cdots,t_{n-1}]$ respectively.

To compute the other Farey neighbors of the current fraction $\dfrac{p}{q}$, it suffices to find all solutions satisfying the conditions using the [extended Euclidean algorithm](./bezouts.md#两个变量的情形).

### Recurrence Relation

The Farey sequence has a concise recurrence relation that allows all fractions of the Farey sequence of order $n$ to be computed sequentially from left to right.

First, the analysis above shows that in $F_n$, the newly added term $\dfrac{p}{n}$ is always the mediant of its left and right adjacent fractions. In fact, this relation holds for all fractions in $F_n$ (except the two endpoints). Let $\dfrac{a}{b}<\dfrac{p}{q}<\dfrac{c}{d}$; by the necessary and sufficient condition for Farey neighbors, we always have

$$
bp-aq = 1 = cq-dp \iff \frac{p}{q} = \dfrac{a+c}{b+d}.
$$

However, in the general case, the fraction $\dfrac{a+c}{b+d}$ may need to be reduced.

Using this observation one can build the following recurrence. Suppose $\dfrac{a}{b}$ and $\dfrac{p}{q}$ are known and we want the value of the third fraction $\dfrac{c}{d}$. Then there exists $k$ such that

$$
a+c = kp,\ b+d=kq
$$

holds. Since the difference

$$
\frac{kp-a}{kq-b} - \dfrac{p}{q} = \dfrac{bp-aq}{q(kq-b)} = \dfrac{1}{q(kq-b)}
$$

decreases as $k$ increases, and the fraction immediately next to $\dfrac{p}{q}$ should be the one with the smallest such difference among all fractions satisfying $kq-b\le n$, necessarily

$$
k = \left\lfloor\dfrac{n+b}{q}\right\rfloor.
$$

One can verify that the fraction obtained this way is necessarily in $F_n$. Therefore the numerators and denominators of the fractions in $F_n$ satisfy the recurrence:

$$
\begin{aligned}
p_k &= \left\lfloor\frac{n + q_{k-2}}{q_{k-1}}\right\rfloor p_{k-1} - p_{k-2},\\
q_k &= \left\lfloor\frac{n + q_{k-2}}{q_{k-1}}\right\rfloor q_{k-1} - q_{k-2}.
\end{aligned}
$$

The recurrence starts from $(p_0,q_0)=(0,1)$ and $(p_1,q_1)=(1,n)$.

## Exercises

Problems with the material of this article as background:

-   [LOJ 6685. 迷宫 (Maze)](https://loj.ac/p/6685)
-   [UVa 10077. The Stern-Brocot Number System](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=33&page=show_problem&problem=1018)
-   [Luogu P8058. \[BalkanOI2003\] Farey 序列 (Farey Sequence)](https://www.luogu.com.cn/problem/P8058)
-   [UVa 12995. Farey Sequence](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=862&page=show_problem&problem=4878)
-   [UVa 10408. Farey Sequences](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=16&page=show_problem&problem=1349)
-   [UVa 12438. Farey Polygon](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=279&page=show_problem&problem=3869)
-   [AtCoder ARC123F. Insert Addition](https://atcoder.jp/contests/arc123/tasks/arc123_f)

Problems requiring binary search in the Stern–Brocot tree:

-   [AtCoder ABC333G. Nearest Fraction](https://atcoder.jp/contests/abc333/tasks/abc333_g)
-   [SPOJ DIVCNT1 - Counting Divisors](https://www.spoj.com/problems/DIVCNT1/)
-   [SPOJ AFS3 - Amazing Factor Sequence (hard)](https://www.spoj.com/problems/AFS3/)

## References and Notes

-   [Stern–Brocot tree - Wikipedia](https://en.wikipedia.org/wiki/Stern%E2%80%93Brocot_tree)
-   [Calkin–Wilf tree - Wikipedia](https://en.wikipedia.org/wiki/Calkin%E2%80%93Wilf_tree)
-   [Farey sequence - Wikipedia](https://en.wikipedia.org/wiki/Farey_sequence)

**Part of the content of this page is translated from the blog post [Дерево Штерна-Броко. Ряд Фарея](http://e-maxx.ru/algo/stern_brocot_farey) and its English translation [The Stern-Brocot Tree and Farey Sequences](https://cp-algorithms.com/others/stern_brocot_tree_farey_sequences.html). The Russian version is licensed under Public Domain + Leave a Link; the English version is licensed under CC-BY-SA 4.0. Another part of the content of this page is translated from the blog post [Continued fractions](https://cp-algorithms.com/algebra/continued-fractions.html), licensed under CC-BY-SA 4.0. The content has been modified.**

[^mediant]: The Chinese term is taken from Section 4.5 of 《具体数学》 (Concrete Mathematics), translated by Zhang Mingyao and Zhang Fan.
