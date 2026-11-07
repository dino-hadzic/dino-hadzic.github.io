---
title: Young tableau
---

## Introduction

A **Young tableau** (in Chinese literature also called a "Young matrix", 杨氏矩阵), or Young table for short, is a combinatorial object commonly used in representation theory and Schubert calculus.

A Young tableau is a special kind of matrix. It is convenient for studying the group representations and properties of the symmetric group and the general linear group. Young tableaux were first introduced by the Cambridge mathematician Alfred Young in 1900, and in 1903 the German mathematician Ferdinand Georg Frobenius applied them to the study of symmetric groups.

???+ note "Note"
    **Representation theory** is a branch of mathematics. It studies abstract algebraic structures by representing their elements as linear transformations of vector spaces. **Schubert calculus** is a branch of algebraic geometry introduced in the 19th century by Hermann Schubert in order to solve counting problems in projective geometry.

## Definitions

### Young diagrams

A **Young diagram** (also called a [Ferrers diagram](https://en.wikipedia.org/wiki/Partition_%28number_theory%29#Ferrers_diagram) when drawn with dots; it is discussed in the section [Integer partitions](./combinatorics/partition.md#ferrers-diagram)) is a finite collection of boxes or cells arranged in left-justified rows, with the row lengths in non-increasing order. Listing the number of boxes in each row of a Young diagram gives an **integer partition** $\lambda$ of a non-negative integer $n$ (the total number of boxes). Thus we can regard the shape of the Young diagram as $\lambda$, since it carries the same information as that integer partition.

Containment of Young diagrams defines a [partial order](../math/order-theory.md#partially-ordered-sets) on integer partitions; this order has the structure of a [lattice](../math/order-theory.md#directed-sets-and-lattices) and is called **Young's lattice**. Listing the number of boxes in each column of a Young diagram gives the "conjugate partition" or "transpose partition" of the integer partition $\lambda$; its Young diagram is obtained by reflecting the original Young diagram along the main diagonal.

The position of each box in a Young diagram is determined by two coordinates representing the **row** and the **column**. Columns are ordered from left to right, and rows are ordered from the row with the most boxes to the one with the fewest. Note that, depending on convention, there are two different ways of drawing Young diagrams: the first places rows with fewer boxes below rows with more boxes, while the second stacks the rows from the largest to the smallest layer by layer upward. Since the former is mainly used by English-speaking countries and the latter is usually used by French-speaking countries, they are customarily called the English notation and the French notation respectively.

The table below shows the different ways of drawing the Young diagram corresponding to the integer partition $(5,4,1)$:

-   English notation: ![](./images/young-diagram-1.svg)
-   French notation: ![](./images/young-diagram-2.svg)

### Young tableaux

#### Definition

A **Young tableau** is obtained by filling the boxes of a Young diagram with symbols taken from some alphabet, which is usually required to be a totally ordered set. The filled-in elements are written as $x_{1}$, $x_{2}$, $x_{3}$, $\ldots$. For convenience, however, we simply fill in positive integers.

When Young tableaux were first applied to the representation theory of the symmetric group, the $n$ boxes of the Young diagram could be filled arbitrarily with distinct positive integers from $1$ to $n$. Nowadays, however, most research uses "standard" Young tableaux, i.e. those in which, in addition to the above conditions, the numbers in each row and each column are strictly increasing. The numbers of distinct Young tableaux with $n$ boxes form the [involution numbers](https://en.wikipedia.org/wiki/Telephone_number_%28mathematics%29):

???+ note "Note"
    The **involution numbers** (telephone numbers) are an integer sequence in mathematics that counts the number of ways $n$ telephone lines can be connected to each other when each line can be connected to at most one other line. They also describe the number of matchings in a complete graph on $n$ vertices, the number of permutations of $n$ elements that are involutions, the sum of the absolute values of the coefficients of the Hermite polynomials, the number of standard Young tableaux with $n$ cells, and the sum of the degrees of the irreducible representations of the symmetric group.

$1, 1, 2, 4, 10, 26, 76, 232, 764, 2620, 9496, \ldots$ (sequence [A000085](https://oeis.org/A000085) in the [OEIS](https://en.wikipedia.org/wiki/On-Line_Encyclopedia_of_Integer_Sequences))

In other applications, a Young diagram may also be filled with repeated numbers. If the filling has strictly increasing numbers in each column and weakly increasing numbers in each row, the Young tableau is called **semistandard** (Semistandard Young Tableaux, sometimes called column-strict). The sequence obtained by recording the number of times each number appears in the Young tableau is regarded as the **weight** of the Young tableau. Hence the weight of a standard Young tableau is necessarily $(1,1,\ldots,1)$, because in a standard Young tableau every positive integer from $1$ to $n$ appears exactly once.

#### Insertion algorithm for standard Young tableaux

Properties of permutations can be visualized through Young tableaux. The **RSK insertion algorithm** provides a way to relate Young tableaux to permutations. It was proposed by Robinson, Schensted and Knuth.

Let $S$ be a Young tableau; define $S \leftarrow x$ as inserting $x$ into the Young tableau starting from the first row, as follows:

1.  In the current row, find the smallest number $y$ greater than $x$.
2.  If one is found, replace $y$ with $x$, move to the next row, set $x \leftarrow y$ and repeat step 1.
3.  If none is found, place $x$ at the end of this row and stop. Say $x$ is in row $s$, column $t$; then $(s, t)$ must be a corner. A cell $(s, t)$ is a corner if and only if neither $(s + 1, t)$ nor $(s, t + 1)$ contains a cell.

For example, the steps of inserting $3$ into the Young tableau $(2, 5, 9)(6, 7)(8)$ are:

![](./images/young-tableau-insert.svg)

### Variations

There are many variations of Young tableaux that are not fully strictly standard. For example, row-strict Young tableaux require the numbers in each row to be strictly increasing and the numbers in each column to be weakly increasing, i.e. they are the conjugates of column-strict Young tableaux. Moreover, in the theory of plane partitions it is customary to replace "increasing" in the above definition by "decreasing". Other variations, such as ribbon tableaux, first group some boxes together and then require the boxes of each group to be filled with the same number.

### Skew tableaux

Given two Young diagrams $\lambda = (\lambda{1}, \lambda{2} \ldots)$ and $\mu = (\mu{1}, \mu{2},\ldots)$ such that $\lambda$ contains $\mu$, i.e. $\mu{i} \leq \mu{i}$ for all $i$, define the "skew Young diagram" $\lambda/\mu$ as all boxes of $\lambda$ minus all boxes of $\mu$, i.e. the set difference of $\lambda$ and $\mu$. Filling the boxes of a skew Young diagram with elements gives a **skew tableau** (skew tableaux).

For example, the figure below shows a standard skew tableau corresponding to the integer partition $(5,4,1)$:

![](./images/skew-tableau.svg)

Similarly, if the numbers in each column are strictly increasing and the numbers in each row are weakly increasing, the skew tableau is called a **semistandard skew tableau**; if a semistandard skew tableau has the numbers $1$ to $n$ (the total number of boxes) filled in without repetition, the skew tableau is called a **standard skew tableau**. Note that different $\lambda$ and $\mu$ can give the same $\lambda/\mu$. Although most properties of skew tableaux depend only on the boxes remaining after taking the difference, some operations still depend on the choice of $\lambda$ and $\mu$. Therefore $\lambda/\mu$ must be regarded as containing information about two elements: $\lambda$ and $\mu$. When $\mu$ is the empty partition (the unique partition of $0$), the skew tableau $\lambda/\mu$ becomes the Young tableau $\lambda$.

## Applications

Young tableaux are often used in combinatorics, representation theory and algebraic geometry, where various ways of counting Young tableaux yield the definition of Schur functions and related identities. In informatics competitions, problems testing the hook length formula for Young tableaux appear frequently.

### Hook length

Given a Young tableau $\pi_{\lambda}$ with $n$ boxes in total, fill the $n$ numbers from $1$ to $n$ into the tableau so that each row is increasing from left to right and each column is increasing from bottom to top. Let $dim_{\pi_{\lambda}}$ denote the number of such fillings.

For a box $v$ in a Young tableau, define its **hook length** $\mathrm{hook}(v)$ as the number of boxes to its right in the same row plus the number of boxes above it in the same column, plus 1 (the box itself).

### Hook length formula

If $dim_{\lambda}$ denotes the number of such fillings, the **hook length formula** states that the number of fillings equals $n!$ divided by the product of the hook lengths of all boxes.

$$
\dim \pi _{\lambda}={\frac {n!}{\prod_{{x\in Y(\lambda)}}{\mathrm {hook}}(x)}}.
$$

![](./images/young-tableau-2.svg)

So for the Young tableau of the integer partition $10 = 5 + 4 + 1$, shown in the figure above, there are

$$
\dim \pi _{\lambda }={\frac  {10!}{7\cdot 5\cdot 4\cdot 3\cdot 1\cdot 5\cdot 3\cdot 2\cdot 1\cdot 1}}=288.
$$

fillings.

## Example problems

### Subsequence problems

For the Young tableau $P$ defined for a permutation $X = x_{1}, \ldots , x_{n}$ of $1$ to $n$:

1.  The length of the first row of $P_{X}$ is the length of the **longest increasing subsequence (LIS)** of the permutation $X$. Note that the first row of $P$ is not necessarily the LIS itself, so the properties of Young tableaux cannot be used directly to solve problems like "LIS partitioning".

2.  For a permutation $X$ and the Young tableau $P_{X}$ it produces, if $X^R$ is the reversal of $X$, then the Young tableau $P_{X^R}$ produced by $X^R$ is $P_{X}$ with rows and columns swapped.

    For example, for the permutations $X = 1, 5, 7, 2, 8, 6, 3, 4$ and $X^R = 4, 3, 6, 8, 2, 7, 5, 1$, we obtain the following Young tableau $P_{X}$:

    ![](./images/young-tableau-LIS.svg)

3.  The length of the first column of the Young tableau $P_{X}$ is the length of the **longest decreasing subsequence (LDS)** of the permutation $X$.

Define an $LIS/LDS$ of length at most $k$ as a $k-LIS$ and $k-LDS$; such problems can also be solved with Young tableaux. For $1-LIS$, obviously the longest $1-LIS$ subsequence is the $LDS$ of the sequence, which is exactly the first column of the Young tableau; similarly, the total length of the first $k$ columns of the Young tableau is the length of the longest $k-LIS$ subsequence. The proof is as follows:

For a permutation $X$ and its Young tableau $P$ with $m$ rows, let the permutation $X^∗$ be $(P_{m,1}\ldots,P_{m,λ_{m}},P_{m−1,1}\ldots,P_{1,1}\ldots P_{1,λ_{1}})$ (i.e. write the rows of the Young tableau one after another from bottom to top). Then $X$ can certainly be transformed into $X^*$ by swap operations.

Hence the length of the longest $k-LIS$ subsequence can be expressed as $F(k)=\sum_{i=1}^{m} \min(k,\lambda_{i})$, i.e. the total length of the first $k$ columns.

???+ note "[CTSC2017 最长上升子序列 (Longest Increasing Subsequence)](https://uoj.ac/problem/301)"
    There is a sequence $b$ of length $n$. For the sequence $B_{m} = (b_{1}, b_{2},\ldots, b_{m})$, let $C$ be a subsequence of $B_{m}$ such that the length of the longest increasing subsequence of $C$ does not exceed $k$; find the maximum length of $C$.

??? note "Solution idea"
    With multiple queries, consider the sweep line method. Then we need to maintain the Young tableau of every prefix. Using the conclusions above, the problem becomes how to quickly maintain the total length of the first $k$ columns of the Young tableau. Maintaining it directly has complexity $O(n^2 \log n)$, which is unacceptable. Consider maintaining the first $\sqrt{n}$ columns and the first $\sqrt{n}$ rows.
    
    One can see that the Young tableau certainly does not completely cover this $W \times H$ rectangle. If $K \leq W$, the answer is obtained directly; if $K > W$, the part beyond $W$ must lie within the $H$ rows. So we can consider how to maintain the first $\sqrt{n}$ columns and the first $\sqrt{n}$ rows at the same time. Reversing the permutation gives the reversal of the Young tableau, so it suffices to also maintain $-A_{i}$ at the same time; the complexity is $O(n \sqrt{n} \log n)$.

???+ note "[BJWC2018 最长上升子序列 (Longest Increasing Subsequence)](https://www.luogu.com.cn/problem/P4484)"
    Given a random permutation of length $n$, find the expected length of its longest increasing subsequence.

???+ note "[CF1268B 杨氏多米诺骨牌 (Domino for Young)](https://codeforces.com/problemset/problem/1268/B)"
    You are given a histogram with $n$ columns of lengths $a_{1} ,a_{2},\ldots,a_{n}\,(a_{1} \geq a_{2} \geq \ldots \geq a_{n} \geq 1)$, i.e. the Young diagram of $a=[3,2,2,2,1]$. Find the maximum number of non-overlapping dominoes ($1 \times 2$ or $2 \times 1$ rectangles) that can be drawn inside this histogram.

## References and further reading

1.  [Young Tableau - from Wolfram MathWorld](https://mathworld.wolfram.com/YoungTableau.html)
2.  [Young tableau - Wikipedia](https://en.wikipedia.org/wiki/Young_tableau)
3.  [Hook length formula - Wikipedia](https://en.wikipedia.org/wiki/Hook_length_formula)
4.  Yuan Fangzhou, [《浅谈杨氏矩阵在信息学竞赛中的应用》(On the Application of Young Tableaux in Informatics Competitions) IOI2019](https://github.com/OI-wiki/libs/blob/master/%E9%9B%86%E8%AE%AD%E9%98%9F%E5%8E%86%E5%B9%B4%E8%AE%BA%E6%96%87/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2019%E8%AE%BA%E6%96%87%E9%9B%86.pdf), Chinese National Team Candidates' Papers Collection, 202–229
