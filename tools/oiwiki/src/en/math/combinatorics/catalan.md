---
title: Catalan numbers
---

## Introduction

Catalan numbers frequently appear in various counting problems. The Belgian mathematician Eugène Charles Catalan discovered this sequence in 1958 while studying the problem of counting bracket sequences, and the sequence is named after him. The Qing dynasty mathematician Minggatu had already discovered this sequence as early as the 1730s.

Catalan numbers satisfy the following recurrence:

$$
C_n = \begin{cases}
1, & n = 0, \\
\sum_{i=0}^{n-1} C_{i}C_{n-1-i}, & n > 0.
\end{cases}\tag{1}
$$

The first few terms of the sequence are ([OEIS: A000108](https://oeis.org/A000108), indices start from $0$):

$$
1,1,2,5,14,42,132,429,1430,\ldots
$$

## Applications

The recurrence of the Catalan numbers $C_n$ has a natural recursive structure: a counting problem $C_n$ of size $n$ can be split, by enumerating the split point, into two subproblems of sizes $i$ and $(n-1-i)$. This recurrence makes Catalan numbers appear widely in problems with a similar recursive structure.

-   **Path counting**: there is an $n\times n$ grid with bottom-left corner $(0, 0)$ and top-right corner $(n, n)$. Starting from the bottom-left corner, each step can only go one unit to the right or up, and the path must not go above the diagonal $y=x$ (it may touch it). The total number of such paths reaching the top-right corner is $C_n$.

    ??? note "Proof"
        Let the number of ways be $T_n$. Consider the case $n \ge 2$. Let the point where the path reaches the diagonal $y=x$ **for the first time** be $(k,k)~(k \in [1,n])$. Consider the paths from $(0,0)$ to $(k,k)$ whose intermediate points, other than the start and end, **do not pass through the diagonal (must not touch it)**.
        
        ![catalan2](./images/catalan-2.svg)
        
        As shown in the figure, the first step of such a path must go right, from $(0,0)$ to $(1,0)$, and the last step must go up, from $(k,k-1)$ to $(k,k)$. Therefore, these paths are exactly the paths from $(1,0)$ to $(k,k-1)$ that do not cross the line $y=x-1$, so their number is $T_{k-1}$. Meanwhile, the number of valid paths from $(k,k)$ to $(n,n)$ is $T_{n-k}$. By the multiplication principle, the number of paths that first touch the diagonal at $(k,k)$ is $T_{k-1} T_{n-k}$. Enumerating all possibilities for $k$, the total number of valid paths is
        
        $$
        T_n = \sum_{k=1}^n T_{k-1}T_{n-k}.
        $$
        
        Substituting $k=i+1$, one sees that this is exactly the Catalan recurrence. From $T_0=1$ it follows that $T_n = C_n$.

    <!-- To make bot happy. Do NOT delete this line. -->

-   **Counting non-crossing chords in a circle**: there are $2n$ points on a circle. The number of ways to connect these points in pairs so that the resulting $n$ segments are pairwise non-crossing is $C_n$.

    ??? note "Proof"
        Denote the number of ways for $2n$ points by $T_n$. Label the $2n$ points clockwise as $1,2,\ldots,2n$. Since the chords are pairwise non-crossing, point $1$ can only be connected to an even-numbered point; otherwise the odd number of points between them could not be paired up without crossing the segment joining the two points. If $1$ is connected to $2k~(k\in[1,n])$, then there are $2k-2$ points on the left and $2n-2k$ points on the right, so by the multiplication principle the number of such ways is $T_{k-1}T_{n-k}$. Therefore, enumerating $k$, we have $T_n = \sum_{k=1}^n T_{k-1} T_{n-k}$. Letting $k=i+1$, we obtain the Catalan recurrence. From $T_0=1$ it follows that $T_n=C_n$.

    <!-- To make bot happy. Do NOT delete this line. -->

-   **Counting triangulations**: the number of ways to divide a convex $(n+2)$-gon into triangles by non-crossing diagonals is $C_n$.

    ??? note "Proof"
        Let the number of triangulations of an $(n+2)$-gon be $T_n$. First fix the side $(1,n+2)$ as the base; it must belong to some triangle, and denote the third vertex of that triangle by $k~(k\in[2,n+1])$. Thus, the original convex polygon is split into three parts:
        
        -   the triangle $(1,k,n+2)$;
        -   a $k$-gon with vertices $1\sim k$;
        -   an $(n+3-k)$-gon with vertices $k\sim (n+2)$.
        
        The latter two parts are both subproblems, so we have the recurrence
        
        $$
        T_n = \sum_{k=2}^{n+1} T_{k-2}T_{n+1-k}.
        $$
        
        Letting $k=i+2$, we obtain the Catalan recurrence. From $T_0=T_1=1$ it follows that $T_n=C_n$.

    <!-- To make bot happy. Do NOT delete this line. -->

-   **Counting binary trees**: the number of structurally distinct binary trees with $n$ nodes is $C_n$. Equivalently, the number of structurally distinct full binary trees with $n$ non-leaf nodes is $C_{n}$.

    ??? note "Proof"
        Denote the number of binary trees with $n$ nodes by $T_n$. Take an arbitrary root and enumerate the sizes of the left and right subtrees. If the left subtree has size $i\in[0,n-1]$, then the right subtree has size $(n-1-i)$. Both subtrees are subproblems, so we have the recurrence
        
        $$
        T_n = \sum_{i=0}^{n-1}T_iT_{n-1-i}.
        $$
        
        This is exactly the Catalan recurrence. From $T_0=T_1=1$ it follows that $T_n=C_n$.

    <!-- To make bot happy. Do NOT delete this line. -->

-   **Counting bracket sequences**: the number of valid bracket sequences formed by $n$ pairs of brackets is $C_n$.

    ??? note "Proof"
        Relate this to the path counting problem. View a left bracket as a step up and a right bracket as a step right. A bracket sequence is valid if, at every position, the number of left brackets is not less than the number of right brackets. This corresponds to the condition in the path counting problem that, at any moment, the number of steps up is not less than the number of steps right. Therefore, there is a bijection between valid bracket sequences and valid paths. The number of valid bracket sequences is likewise $C_n$.

    <!-- To make bot happy. Do NOT delete this line. -->

-   **Counting stack pop sequences**: the push sequence of an (infinite) stack is $1,2,3, \ldots ,n$. The number of valid pop sequences is $C_n$.

    ??? note "Proof"
        Relate this to the bracket sequence counting problem. View a push as a left bracket and a pop as a right bracket. At any moment, the number of pushes is not less than the number of pops. Therefore, there is a bijection between valid pop sequences and valid bracket sequences. The number of valid pop sequences is likewise $C_n$.

    <!-- To make bot happy. Do NOT delete this line. -->

-   **Counting sequences**: among the sequences $a_1,a_2, \ldots ,a_{2n}$ consisting of $n$ copies of $+1$ and $n$ copies of $-1$, the number of those whose partial sums satisfy $a_1+a_2+ \ldots +a_k \geq 0~(k=1,2,3, \ldots ,2n)$ is $C_n$.

    ??? note "Proof"
        Relate this to the bracket sequence counting problem. View $+1$ as a left bracket and $-1$ as a right bracket. At any moment, the number of $+1$'s is not less than the number of $-1$'s. Therefore, there is a bijection between valid sequences and valid bracket sequences. The number of valid sequences is likewise $C_n$.

Although this recurrence is widely applicable, computing it directly has a high complexity, so we need to look for simpler formulas.

## Common forms

Catalan numbers have the following common expressions:

$$
C_n = \frac{1}{n+1}\binom{2n}{n} = \dfrac{(2n)!}{n!(n+1)!},~ n\ge 0. \tag{2}
$$

$$
C_n = \binom{2n}{n} - \binom{2n}{n+1},~n \ge 0. \tag{3}
$$

$$
C_n = \frac{(4n-2)}{n+1}C_{n-1},~ n > 0,~ C_0 = 1. \tag{4}
$$

All of these forms of the Catalan numbers can be computed efficiently: the first two reduce the problem to computing factorials and binomial coefficients, while the third provides a recurrence for computing them one after another.

For these three common forms, this article provides two methods of proof.

### Algebraic derivation

Deriving the above expressions for Catalan numbers algebraically takes two steps. First, verify that the three forms are mutually equivalent.

??? note "Proof that expressions $(2)\sim(4)$ are equivalent"
    It suffices to show that expression $(3)$ can be transformed into the factorial form of expression $(2)$:
    
    $$
    \begin{aligned}
    C_n &= \binom{2n}{n} - \binom{2n}{n+1} \\
    &= \frac{(2n)!}{n!n!} - \frac{(2n)!}{(n-1)!(n+1)!} \\
    &= \frac{(2n)!}{n!n!}\left(1 - \frac{n!}{(n-1)!(n+1)}\right) \\
    &= \frac{(2n)!}{n!n!}\left(1- \frac{n}{n+1}\right) \\
    &= \dfrac{(2n)!}{n!(n+1)!}.
    \end{aligned}
    $$
    
    Also, expression $(4)$ can be transformed into the factorial form of expression $(2)$:
    
    $$
    C_n = \prod_{i=1}^n\frac{(4i-2)}{i+1} = \prod_{i=1}^n\frac{2i(2i-1)}{i(i+1)} = \dfrac{(2n)!}{n!(n+1)!}.
    $$
    
    Therefore, the three expressions are mutually equivalent.

Next, verify that these forms are indeed solutions of the Catalan recurrence. To this end, we use the generating function method to solve the recurrence $(1)$ directly.

??? note "Solving the recurrence $(1)$ with the generating function method"
    Consider the ordinary generating function of the Catalan numbers, $C(x)=\sum_{n=0}^{\infty}C_nx^n$. Since the Catalan recurrence closely resembles the form of a convolution, we try to use a convolution to construct an equation for $C(x)$:
    
    $$
    \begin{aligned}
    C(x)&=\sum_{n=0}^{\infty}C_nx^n\\
    &=1+\sum_{n=1}^{\infty}\left(\sum_{i=0}^{n-1}C_iC_{n-i-1}\right)x^{n}\\
    &=1+x\sum_{n=1}^{\infty}\sum_{i=0}^{n-1}C_ix^iC_{n-i-1}x^{n-i-1}\\
    &=1+x\sum_{i=0}^{\infty}C_ix^i\sum_{j=0}^{\infty}C_jx^j\\
    &=1+xC^2(x).
    \end{aligned}
    $$
    
    Here, the second-to-last equality swaps the order of summation and sets $j=n-1-i$. Solving, we obtain:
    
    $$
    C(x)=\dfrac{1\pm \sqrt{1-4x}}{2x} = \frac{2}{1\mp \sqrt{1-4x}}.
    $$
    
    From the initial condition $C_0=1$ we know $C(0)=1$. Substituting to check, the only feasible solution is
    
    $$
    C(x) = \dfrac{1- \sqrt{1-4x}}{2x}.
    $$
    
    Next, we need to expand it as a power series. By the [power series expansion](../poly/intro.md#common-power-series-expansions) of $(1+x)^a$, we have:
    
    $$
    \sqrt{1-4x} = \sum_{n=0}^{\infty} \dfrac{\left(\frac{1}{2}\right)_{-n}}{n!}(-4x)^n,
    $$
    
    where $\left(\dfrac{1}{2}\right)_{-n}$ is the falling factorial power:
    
    $$
    \begin{aligned}
    \left(\frac{1}{2}\right)_{-n} &= \prod_{k=0}^{n-1}\left(\dfrac{1}{2}-k\right) = \dfrac{1}{2^n}\prod_{k=1}^{n-1}(1-2k) = \dfrac{(-1)^{n-1}}{2^n}\prod_{k=1}^{n-1}(2k-1)\\
    &= \dfrac{(-1)^{n-1}}{2^{2n-1}}\prod_{k=1}^{n-1}\dfrac{(2k-1)2k}{k} = \dfrac{(-1)^{n-1}}{2^{2n-1}}\dfrac{(2n-2)!}{(n-1)!}.
    \end{aligned}
    $$
    
    Substituting into the expression for $C(x)$, we get
    
    $$
    \begin{aligned}
    C(x) &= \dfrac{1}{2x}\left(1-\sum_{n=0}^{\infty} \dfrac{\left(\frac{1}{2}\right)_{-n}}{n!}(-4x)^n\right)\\
    &= -\dfrac{1}{2x}\sum_{n=1}^\infty \dfrac{(-4x)^n}{n!}\left(\frac{1}{2}\right)_{-n} \\
    &= -\dfrac{1}{2x}\sum_{n=1}^\infty \dfrac{(-4x)^n}{n!}\dfrac{(-1)^{n-1}}{2^{2n-1}}\dfrac{(2n-2)!}{(n-1)!} \\
    &= \sum_{n=1}^{\infty}\dfrac{(2n-2)!}{(n-1)!n!}x^{n-1}\\
    &= \sum_{n=0}^{\infty}\dfrac{(2n)!}{n!(n+1)!}x^n.
    \end{aligned}
    $$
    
    This yields expression $(2)$ for $C_n$.

### Combinatorial meaning

Since Catalan numbers have a clear combinatorial meaning, these forms can also be proved using only combinatorial counting methods. This section provides one combinatorial proof for each of the three expressions.

??? note "Proof of expression $(2)$"
    Consider the sequence counting problem. For an arbitrary sequence $\{a_i\}_{i=1}^{2n}$ consisting of $\pm 1$, define its partial sums $S_i = \sum_{j=1}^{i}a_i$, and define its **exceedance** as the number of indices with $S_i < 0$ and $a_i = -1$. An exceedance of $0$ is equivalent to the sequence being valid; the exceedance ranges over $[0,n]$, so there are $(n+1)$ possible values in total. What we need to prove is that the numbers of sequences with different exceedances are actually the same.
    
    To this end, we construct a map $f$ from sequences with exceedance $e > 0$ to sequences with exceedance $(e-1)$. For a sequence $\{a_i\}$ with exceedance $e > 0$, take the index $k$ to be the smallest index such that $S_i = 0$ and $a_i = +1$. Swapping the parts of the sequence to the left and right of $a_k$, we obtain the following sequence $\{a'_i\}$:
    
    $$
    a_{k+1},a_{k+2},\cdots,a_{2n},a_k,a_{1},a_{2},\cdots,a_{k-1}.
    $$
    
    Since the partial sums corresponding to the part of the original sequence to the right of $a_k$ are unchanged by the swap, their contribution to the exceedance is also unchanged. For the part of the original sequence to the left of $a_k$, the corresponding partial sums all increase by $1$ after the swap, so their contribution to the exceedance decreases, and the decrease is exactly the number of indices in the part of the original sequence to the left of $a_k$ with $S_i=-1$ and $a_i=-1$. Since the choice of $a_k$ guarantees that there is exactly one such index, the exceedance of the sequence $\{a'_i\}$ equals $(e-1)$. That is, the map $f$ decreases the exceedance of a sequence by exactly $1$.
    
    The map $f$ is invertible. Note that in the sequence $\{a'_i\}$, the position corresponding to $a_k$ is exactly the largest index such that $S'_k=+1$ and $a'_i = +1$. This is because after the swap, these partial sums are exactly $1$ larger than the corresponding partial sums before the swap, so a current partial sum of $+1$ corresponds to a partial sum equal to $0$ before the swap. But by the choice of $k$, before the swap this part (i.e., the part of the original sequence to the left of $a_k$) contains no index such that $S_i = 0$ and $a_i = +1$.
    
    Hence, the map $f$ forms a bijection between sequences with exceedance $e>0$ and sequences with exceedance $(e-1)$. This shows that the numbers of sequences with different exceedances are actually the same. Since the total number of sequences is $\dbinom{2n}{n}$, the number of valid sequences (i.e., sequences with exceedance $0$) equals
    
    $$
    C_n = \dfrac{1}{n+1}\dbinom{2n}{n}.
    $$
    
    This proves expression $(2)$ for the Catalan numbers.

??? note "Proof of expression $(3)$"
    Consider the path counting problem. This is a typical lattice path counting problem that can be solved by the reflection principle. Specifically for this problem, we subtract the number of invalid paths from the total number of paths. In total, $2n$ steps are taken, $n$ of which go right, so the total number of paths is $\dbinom{2n}{n}$. A path is invalid if and only if it touches the line $y = x+1$. For any invalid path, we can find the first position where it touches the line $y = x+1$ and reflect the part of the path after that position across the line $y=x+1$. One then sees that an invalid path from $(0,0)$ to $(n,n)$ becomes a path from $(0,0)$ to $(n-1,n+1)$.
    
    ![catalan1](./images/catalan-1.svg)
    
    Since a path from $(0,0)$ to $(n-1,n+1)$ must cross the line $y = x+1$, every such path corresponds to an invalid path from $(0,0)$ to $(n,n)$. Similarly to the computation of the total number of paths, the total number of invalid paths is $\dbinom{2n}{n+1}$. Therefore, the total number of valid paths is
    
    $$
    C_n = \binom{2n}{n} - \binom{2n}{n+1}.
    $$
    
    This is expression $(3)$ for the Catalan numbers.

??? note "Proof of expression $(4)$"
    Consider the triangulation counting problem. Let $P$ be a convex $(n+2)$-gon and fix one of its sides as the base. For every triangulation of the polygon $P$, we can choose one of its non-base edges (including the edges added by the triangulation), mark it, and orient it. There are $(4n+2)C_n$ such triangulation-plus-marking configurations in total. Further, let $Q$ be a convex $(n+3)$-gon, again with one of its sides fixed as the base. For the polygon $Q$, we can choose one of its non-base sides to mark, and then triangulate. There are $(n+2)C_{n+1}$ such marking-plus-triangulation configurations in total.
    
    ![](./images/catalan-triangulation.svg)
    
    As shown in the figure, there is an obvious bijection between the results of these two groups of operations. For a result of triangulating and marking $P$, we can expand its marked edge into a triangle by expanding the endpoint the orientation points to into a new side, and mark this new side, which gives a result of marking and triangulating $Q$; for a result of marking and triangulating $Q$, we can contract its marked side into a single point, mark the diagonal obtained by the contraction, and orient it toward the vertex obtained by the contraction, which gives a result of triangulating and marking $P$. Therefore,
    
    $$
    (4n+2)C_n = (n+2)C_{n+1}.
    $$
    
    Rearranging slightly and combining with $C_0=1$, we obtain expression $(4)$ for the Catalan numbers.

## Example problem

???+ example "[Luogu P1044 栈 (Stack)](https://www.luogu.com.cn/problem/P1044)"
    The push order is $1,2,\ldots ,n$. Find the total number of all possible pop orders.

??? note "Reference code"
    === "C++"
        ```cpp
        --8<-- "docs/math/code/combinatorics/catalan/catalan_1.cpp"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/math/code/combinatorics/catalan/catalan_1.py"
        ```

## Exercises

-   [Luogu P2532 \[AHOI2012\] 树屋阶梯 (Treehouse Stairs)](https://www.luogu.com.cn/problem/P2532)
-   [Luogu P1641 \[SCOI2010\] 生成字符串 (Generating Strings)](https://www.luogu.com.cn/problem/P1641)
-   [Luogu P3200 \[HNOI2009\] 有趣的数列 (Interesting Sequence)](https://www.luogu.com.cn/problem/P3200)
-   [AtCoder Beginner Contest 205 E - White and Black Balls](https://atcoder.jp/contests/abc205/tasks/abc205_e)
-   [AtCoder Regular Contest 145 C - Split and Maximize](https://www.luogu.com.cn/problem/AT_arc145_c)
-   [Luogu P5014 水の三角（修改版）(Water Triangle, modified version)](https://www.luogu.com.cn/problem/P5014)
-   [Luogu P3978 \[TJOI2015\] 概率论 (Probability Theory)](https://www.luogu.com.cn/problem/P3978)

## References and notes

-   [Catalan number - Wikipedia](https://en.wikipedia.org/wiki/Catalan_number)
