---
title: Graph enumeration
---

In combinatorics, graph enumeration is the branch that studies problems of counting graphs with given properties. [Generating functions](../poly/intro.md), the [Pólya enumeration theorem](./polya.md), the [symbolic method](../poly/symbolic-method.md#%E9%9B%86%E5%90%88%E7%9A%84-cycle-%E6%9E%84%E9%80%A0) and the [OEIS](https://oeis.org/) are the most important mathematical tools for solving such problems. Graph enumeration problems fall into two large classes: labeled and unlabeled. In most cases[^1] the labeled version of a problem is simpler than the corresponding unlabeled one, so we first look at counting labeled structures.

[^1]: Unlabeled binary trees may be a counterexample: when the structure is simple, the corresponding permutation group is the identity group, and the labeled version is then obtained directly by multiplying by $n!$.

## Labeled trees

This is Cayley's formula; see the article on the [Prüfer sequence](../../graph/prufer.md). We can also obtain this result using [Kirchhoff's matrix-tree theorem](../../graph/matrix-tree.md) or [generating functions](../poly/intro.md#generating-functions) together with the [Lagrange theorem](https://codeforces.com/blog/entry/104184).

### Exercises

-   [Hihocoder 1047. Random Tree](https://vjudge.net/problem/HihoCoder-1047)

## Labeled connected graphs

### Example problem "POJ 1737" Connected Graph

???+ note "Example problem [“POJ 1737” Connected Graph](http://poj.org/problem?id=1737)"
    Problem summary: find the number of labeled connected graphs with $n$ vertices ($n \leq 50$).

Problems of this kind first appeared in Lou Tiancheng's (楼教主) problem series “男人八题” (“Eight Problems for Men”). Let $g_n$ be the number of labeled graphs with $n$ vertices and $c_n$ the sequence we are looking for. A graph with $n$ vertices has at most $\binom{n}{2}$ edges, each edge has two states (present or absent) and these states are independent, so $g_n = 2^{\binom{n}{2}}$. Fix one vertex and enumerate the size of the connected component it belongs to: from the remaining $n-1$ vertices we have to choose $i-1$ vertices that form one connected component together with it. The vertices outside this component may be connected arbitrarily, so we get the following recurrence:

$$
\begin{align}
\sum_{i=1}^{n} \binom{n-1}{i-1} c_i g_{n-i} &= g_n \\
c_n &= g_n - \sum_{i=1}^{n-1} \binom{n-1}{i-1} c_i g_{n-i} 
\end{align}
$$

Rearranging the terms gives an $O(n^2)$ recurrence for the sequence $c_n$, which is enough to solve this problem.

### Example problem "集训队作业 2013" 城市规划

???+ note "Example problem [“集训队作业 2013” 城市规划 (Team Selection Homework 2013 – Urban Planning)](https://www.luogu.com.cn/problem/P4841)"
    Problem summary: find the number of labeled connected graphs with $n$ vertices ($n \leq 130000$).

For sequence problems with larger constraints we usually need to construct the generating functions of these sequences so that efficient polynomial algorithms can be used.

#### Method 1: divide-and-conquer FFT

The recurrence above can be viewed as a kind of self-convolution, so it can be computed with divide-and-conquer FFT in $O(n\log^2n)$.

#### Method 2: polynomial inverse

Expand the binomial coefficient in the recurrence above and rearrange:

$$
\begin{align}
\sum_{i=1}^{n} \binom{n-1}{i-1} c_i g_{n-i} &= g_n \\
\sum_{i=1}^{n} \frac{c_i}{(i-1)!} \frac{g_{n-i}}{(n-i)!} &= \frac{g_n}{(n-1)!}
\end{align}
$$

Construct the polynomials:

$$
\begin{align}
C(x) &= \sum_{n=1} \frac{c_n}{(n-1)!} x^n \\
G(x) &= \sum_{n=0} \frac{g_n}{n!} x^n \\
H(x) &= \sum_{n=1} \frac{g_n}{(n-1)!} x^n
\end{align}
$$

Substituting into the equation above gives $CG = H$; it suffices to compute the [polynomial inverse](../poly/elementary-func.md#polynomial-inverse) and then obtain $C(x)$ by convolution.

#### Method 3: polynomial exp

Another approach is to use the [combinatorial meaning of the polynomial exp of an EGF](../poly/egf.md#egf-%E4%B8%AD%E5%A4%9A%E9%A1%B9%E5%BC%8F-exp-%E7%9A%84%E7%BB%84%E5%90%88%E6%84%8F%E4%B9%89). Let $C(x)$ and $G(x)$ be the EGFs of the sequences of labeled connected graphs and of simple graphs, respectively; then they satisfy the following relation:

$$
\begin{align}
\exp(C(x)) &= G(x) \\
C(x) &= \ln(G(x))
\end{align}
$$

It suffices to compute $C(x)$ with the [polynomial logarithm](../poly/elementary-func.md#polynomial-logarithm-and-exponential).

## Labeled Eulerian and bipartite graphs

### Example problem "SPOJ KPGRAPHS" Counting Graphs

???+ note "Example problem [“SPOJ KPGRAPHS” Counting Graphs](http://www.spoj.com/problems/KPGRAPHS/)"
    Problem summary: find the number of labeled graphs with $n$ vertices satisfying each of the following properties ($n \leq 1000$).
    
    -   connected graphs [A001187](https://oeis.org/A001187),
    -   Eulerian graphs [A033678](https://oeis.org/A033678),
    -   bipartite graphs [A047864](https://oeis.org/A047864).

This problem limits the code length, so polynomial templates cannot be used directly, but generating functions still help us with the analysis.

The connected-graph problem was solved in the previous examples; consider Eulerian graphs. Note that all of the methods for counting connected graphs above generalize to labeled connected graphs with an arbitrary property. For example, if in the recurrence for connected graphs we replace $g_n$, the number of all graphs, by the number of graphs in which every vertex has even degree, the resulting $c_n$ is exactly the number of Eulerian graphs.

Let us wrap the recurrence from POJ 1737 into a "connectification" function (transition to connected structures):

```cpp
void ln(Int C[], Int G[]) {
  for (int i = 1; i <= n; ++i) {
    C[i] = G[i];
    for (int j = 1; j <= i - 1; ++j)
      C[i] -= binom[i - 1][j - 1] * C[j] * G[i - j];
  }
}
```

The first two questions are then solved easily:

```cpp
for (int i = 1; i <= n; ++i) G[i] = pow(2, binom[i][2]);
ln(C, G);
for (int i = 1; i <= n; ++i) G[i] = pow(2, binom[i - 1][2]);
ln(E, G);
```

Note that this connectification recurrence is in fact equivalent to taking the polynomial logarithm of the corresponding EGF. Similarly we can write the inverse connectification function, which is equivalent to taking the polynomial exp of the EGF.

```cpp
void exp(Int G[], Int C[]) {
  for (int i = 1; i <= n; ++i) {
    G[i] = C[i];
    for (int j = 1; j <= i - 1; ++j)
      G[i] += binom[i - 1][j - 1] * C[j] * G[i - j];
  }
}
```

Now let us discuss counting labeled bipartite graphs.

Let $b_n$ denote the number of bipartite graphs with n vertices and $g_n$ the number of graphs with $n$ vertices whose vertices are colored with 2 colors so that there is no edge between vertices of the same color. Enumerating the number of vertices of one of the colors, we get[^2]:

$$
g_n = \sum_{i=0}^{n} \binom{n}{i}2^{i(n-i)}
$$

[^2]: [PinkRabbit's (粉兔) blog](https://www.luogu.com.cn/blog/PinkRabbit/solution-sp4420) tells us that this sequence can also be sped up with the [Chirp Z-transform](../poly/czt.md).

Next we establish the relation between $g_n$ and $b_n$ in two different ways.

#### Method 1: double counting

Let $c_{n, k}$ denote the number of bipartite graphs with k connected components. It is not hard to obtain the following relation:

$$
\begin{align}
b_n &= \sum_{i=1}^{n} c_{n, i} \\
g_n &= \sum_{i=1}^{n} c_{n, i} 2^i 
\end{align}
$$

Comparing the two expressions for $g_n$ and expanding gives:

$$
\begin{align}
\sum_{i=0}^{n} \binom{n}{i}2^{i(n-i)} &= \sum_{i=1}^{n} c_{n, i} 2^i \\
c_{n, i} &= \sum_{i=0}{n-1} \binom{n-1}{i-1} c_{n, 1}c_{n-i,k-1}
\end{align}
$$

It is not hard to obtain a recurrence for $b_n$ in $O(n^3)$; using the inclusion–exclusion principle it can be further optimized to $O(n^2)$, which solves this problem.

#### Method 2: connectification recurrence

Methods 2 and 3 both use connected bipartite graphs $b1_n$  [A001832](https://oeis.org/A001832) as the bridge between $g_n$ and $b_n$.

Note that every connected bipartite graph has exactly two different colorings, corresponding to two different connected 2-colored graphs,
so applying connectification to $g_n$ gives exactly twice the sequence $b1_n$, while $b_n$ is obtained from $b1_n$ by inverse connectification.

Therefore:

```cpp
for (int i = 1; i <= n; ++i) {
  G[i] = 0;
  for (int j = 0; j < i + 1; ++j) G[i] += binom[i][j] * pow(2, j * (i - j));
}
ln(B1, G);
for (int i = 1; i <= n; ++i) B1[i] /= 2;
exp(B, B1);
```

Both recurrences run in $O(n^2)$, which solves this problem.

#### Method 3: polynomial exp

Note that the recurrence above can also be understood through EGFs.

Let $G(x)$ be the EGF of $g_n$, $B1(x)$ the EGF of $b1_n$ and $B(x)$ the EGF of $b_n$. Applying the approach of method 2, we have:

$$
\begin{align}
G(x) &= \exp(2B1(x)) \\
B(x) &= \exp(B1(x))  \\
     &= \exp(\frac{\ln{G(x)}}{2}) \\
     &= \sqrt{G}
\end{align}
$$

Differentiating both sides and comparing coefficients yields a recurrence that is easy to code, which solves this problem.
Note that methods 2 and 3 are essentially the same, and in general method 3 gives a better time complexity.

$$
\begin{align}
B_n^2 &= G  \\
2B_nB_n' &= G' 
\end{align}
$$

??? note "Reference code"
    ```cpp
    --8<-- "docs/math/code/combinatorics/graph-enumeration/graph-enumeration_1.cpp"
    ```

### Exercises

-   [UOJ Goodbye Jihai D. 新年的追逐战 (New Year's Chase)](https://uoj.ac/contest/50/problem/498)
-   [BZOJ 3864. 大朋友和多叉树 (Big Friend and the Multiway Tree)](https://hydro.ac/p/bzoj-P3864)
-   [BZOJ 2863. 愤怒的元首 (The Angry Leader)](https://hydro.ac/p/bzoj-P2863)
-   [Luogu P6295. 有标号 DAG 计数 (Counting Labeled DAGs)](https://www.luogu.com.cn/problem/P6295)
-   [LOJ 6569. 仙人掌计数 (Counting Cacti)](https://loj.ac/p/6569)
-   [LOJ 6570. 毛毛虫计数 (Counting Caterpillars)](https://loj.ac/p/6570)
-   [Luogu P5434. 有标号荒漠计数 (Counting Labeled Deserts)](https://www.luogu.com.cn/problem/P5434)
-   [Luogu P3343. \[ZJOI2015\] 地震后的幻想乡 (Gensokyo After the Earthquake)](https://www.luogu.com.cn/problem/P3343)
-   [HDU 5279. YJC plays Minecraft](https://acm.hdu.edu.cn/showproblem.php?pid=5279)
-   [Luogu P7364. 有标号二分图计数 (Counting Labeled Bipartite Graphs)](https://www.luogu.com.cn/problem/P7364)
-   [Luogu P5827. 点双连通图计数 (Counting Vertex-Biconnected Graphs)](https://www.luogu.com.cn/problem/P5827)
-   [Luogu P5827. 边双连通图计数 (Counting Edge-Biconnected Graphs)](https://www.luogu.com.cn/problem/P5828)
-   [Luogu P6596. How Many of Them](https://www.luogu.com.cn/problem/P6596)
-   [Luogu U152448. 有标号强连通图计数 (Counting Labeled Strongly Connected Graphs)](https://www.luogu.com.cn/problem/U152448)
-   [Project Euler 434. Rigid graphs](https://projecteuler.net/problem=434)

## Riddell's formula

The use of the exp of an EGF described above is sometimes called Riddell's formula for labeled graphs, and the [Euler transform](../poly/symbolic-method.md#%E9%9B%86%E5%90%88%E7%9A%84-multiset-%E6%9E%84%E9%80%A0) of a generating function is sometimes called Riddell's formula for unlabeled graphs. The latter first appeared in Euler's study of integer partitions; besides graph enumeration problems, it also appears in the unbounded knapsack problem.

For a given sequence $a_i$ with corresponding OGF $A(x)$, the Euler transform of $A(x)$ is defined as:

$$
\begin{align}
\mathcal{E}(A(x)) &= \prod_{i} (1-x^i)^{-a_i}  \\
                  &= \exp (\sum_{i} \frac{A(x^i)}{i})  
\end{align}
$$

Let $b_i$ be the coefficients of $\mathcal{E}(A(x))$ and define the auxiliary array $c_i = \sum_{d|n} d a_d$; then we have the recurrence

$$
n b_n = c_n + \sum_{i=1}^{n-1} c_i b_{n-i}
$$

## Unlabeled trees

### Example problem "SPOJ PT07D" Let us count 1 2 3

???+ note "Example problem [“SPOJ PT07D” Let us count 1 2 3](https://www.spoj.com/problems/PT07D/)"
    Problem summary: find the number of trees with n vertices satisfying each of the following properties.
    
    -   labeled rooted trees [A000169](https://oeis.org/A000169),
    -   labeled unrooted trees [A000272](https://oeis.org/A000272),
    -   unlabeled rooted trees [A000081](https://oeis.org/A000081),
    -   unlabeled unrooted trees [A000055](https://oeis.org/A000055).

#### Rooted trees

The labeled case was solved earlier in the text; now consider unlabeled rooted trees. Let their OGF be $F(x)$. Applying the Euler transform, we get:

$$
F(x) = x\mathcal{E}(F(x))
$$

It suffices to extract the coefficients.

#### Unrooted trees

Use inclusion–exclusion: from the number of rooted trees subtract those in which the root is not the centroid, and treat the cases by the parity of $n$.

When $n$ is odd:

There necessarily exists a subtree of size $\geq \left\lceil \frac{n}{2}\right\rceil$; enumerating the size of this subtree gives:

$$
g_n = f_n - \sum_{i=\left\lceil\frac{n}{2}\right\rceil}^{n-1} f_i f_{n-i}
$$

When $n$ is even:

Note that in the case of two centroids the procedure above subtracts only once, so we additionally have to subtract

$$
g_n = f_n - \sum_{i=\frac{n}{2}+1}^{n-1} f_i f_{n-i} - \binom{f_{\frac{n}{2}}}{2}
$$

### Example problem "Luogu P5900" 无标号无根树计数

???+ note "Example problem [“Luogu P5900” 无标号无根树计数 (Counting Unlabeled Unrooted Trees)](https://www.luogu.com.cn/problem/P5900)"
    Problem summary: find the number of unlabeled unrooted trees with n vertices ($n \leq 200000$).

For larger constraints the approach is the same: after the Euler transform it suffices to use polynomial templates.

## Unlabeled simple graphs

### Example problem "SGU 282. Isomorphism" Isomorphism

???+ note "Example problem [“SGU 282. Isomorphism” Isomorphism](https://codeforces.com/problemsets/acmsguru/problem/99999/282)"
    Problem summary: find the number of ways to color the edges of an unlabeled complete graph with n vertices using m colors.

Note that for m = 2 the objects in question are exactly the unlabeled simple graphs [A000088](https://oeis.org/A000088). Consider the Pólya enumeration theorem:

$$
\frac{1}{|G|}\sum_{g\in G} m^{c(g)}
$$

In this problem the permutation group $G$ is the group of edge permutations generated by the symmetric group of order $n$ on the vertices, but the brute-force approach enumerates $O(n!)$ permutations, which is not enough to solve this problem.

Let us classify the permutations by their cycle structure: each cycle structure corresponds to an integer partition, and we generate the partitions with dfs(). The problem then reduces to finding, for each partition $p$, the number of corresponding permutations $w(p)$ and the number of cycles $c(p)$ in each class of permutations; the answer is

$$
\frac{1}{|G|} \sum_{p \in P} w(p) m^{c(p)}
$$

Consider $w(p)$: each part of the partition corresponds to a cyclic permutation, and the order among parts of the same size does not matter, so we have:

$$
w(p) = \frac{n!}{\prod_{i}(p_i)\prod_{i}(q_i!)} 
$$

Here $q_i$ denotes the number of times a part of size $i$ appears in $p$.

Consider $c(p)$: the number of cycles on the vertex set acted on by $p$ is $|p|$, but the problem is about edge coloring, so we also have to consider the edge permutation generated by the vertex permutation.

If both endpoints of an edge lie in the same cycle of size $p_i$, the number of cycles generated by the edges is exactly $\left\lfloor \frac{p_i}{2} \right\rfloor$.

If the endpoints of an edge lie in two different cycles of sizes $p_i$ and $p_j$, the length of each cycle is $\operatorname{lcm}(p_i,p_j)$, so the number of cycles generated by the edges is exactly $\frac{p_i p_j}{\operatorname{lcm}(p_i,p_j)} = \gcd(p_i, p_j)$.

??? note "Reference code"
    ```cpp
    --8<-- "docs/math/code/combinatorics/graph-enumeration/graph-enumeration_2.cpp"
    ```

## Exercises

-   [CodeForces 438 E. The Child and Binary Tree](https://codeforces.com/problemset/problem/438/E)
-   [Luogu P5448. \[THUPC2018\] 好图计数 (Counting Good Graphs)](https://www.luogu.com.cn/problem/P5448)
-   [Luogu P5818. \[JSOI2011\] 同分异构体计数 (Counting Isomers)](https://www.luogu.com.cn/problem/P5818)
-   [Luogu P6597. 烯烃计数 (Counting Alkenes)](https://www.luogu.com.cn/problem/P6597)
-   [Luogu P6598. 烷烃计数 (Counting Alkanes)](https://www.luogu.com.cn/problem/P6598)
-   [Luogu P4128. \[SHOI2006\] 有色图 (Colored Graphs)](https://www.luogu.com.cn/problem/P4128)
-   [Luogu P4727. \[HNOI2009\] 图的同构计数 (Counting Graph Isomorphisms)](https://www.luogu.com.cn/problem/P4727)
-   [AtCoder Beginner Contest 222 H. Binary Tree](https://atcoder.jp/contests/abc222/tasks/abc222_h)
-   [AtCoder Beginner Contest 284 Ex. Count Unlabeled Graphs](https://atcoder.jp/contests/abc284/tasks/abc284_h)
-   [Luogu P4708. 画画 (Drawing)](https://www.luogu.com.cn/problem/P4708)
-   [Luogu P7592. 数树 (Counting Trees) (2021 CoE-II E)](https://www.luogu.com.cn/problem/P7592)
-   [Luogu P5206. \[WC2019\] 数树 (Counting Trees)](https://www.luogu.com.cn/problem/P5206)

## References and notes

1.  [WC2015, 顾昱洲营员交流资料 Graphical Enumeration (Gu Yuzhou, camp participant exchange material: Graphical Enumeration)](https://github.com/lychees/ACM-Training/blob/master/Note/%E5%86%AC%E4%BB%A4%E8%90%A5/2015/%E9%A1%BE%E6%98%B1%E6%B4%B2%E8%90%A5%E5%91%98%E4%BA%A4%E6%B5%81%E8%B5%84%E6%96%99%20Graphical%20Enumeration.pdf)
2.  [WC2019, 生成函数，多项式算法与图的计数 (Generating Functions, Polynomial Algorithms and Graph Enumeration)](https://github.com/lychees/ACM-Training/tree/master/Note/%E5%86%AC%E4%BB%A4%E8%90%A5/2019/d4)
3.  [Counting labeled graphs - Algorithms for Competitive Programming](https://cp-algorithms.com/combinatorics/counting_labeled_graphs.html)
4.  [Graphical Enumeration Paperback, Frank Harary, Edgar M. Palmer](https://github.com/lychees/ACM-Training/blob/master/Note/Book/)
5.  [The encyclopedia of integer sequences, N. J. A. Sloane, Simon Plouffe](https://github.com/lychees/ACM-Training/blob/master/Note/Book/The%20encyclopedia%20of%20integer%20sequences%20\(N.%20J.A.%20Sloane%2C%20Simon%20Plouffe\).pdf)
6.  [Combinatorial Problems and Exercises, László Lovász](https://github.com/lychees/ACM-Training/blob/master/Note/Book/Combinatorial%20Problems%20and%20Exercises_L%C3%A1szl%C3%B3%20Lov%C3%A1sz.pdf)
7.  [Graph Theory and Additive Combinatorics](https://yufeizhao.com/gtacbook/)
