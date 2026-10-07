---
title: Random walks on graphs
---

This page introduces the problem of random walks on graphs. It is studied from three angles: grid graphs, sparse graphs and general graphs; various methods for solving this kind of problem are introduced, and their advantages and disadvantages when solving different problems are compared.

## Definition

Given a directed simple graph $G=(V, E)(V=\{v_1, v_2, \cdots, v_{|V|}\})$, a starting vertex $s \in V$ and a target vertex $t \in V$, every edge $e=\left(x, y\right)$ has a positive weight $w_e$ such that for every $x \in V \backslash\left\{t\right\}$, $\sum_{\left(x, y\right) \in E} w_{\left(x, y\right)}=1$, and from every vertex $x$ there is a path to $t$. A token starts at the starting vertex; every second, from its current vertex $x$, it chooses the outgoing edge $\left(x, y\right)$ with probability $w_{(x, y)}$ and moves to $y$; it stops once it reaches the target. Find the expected time spent.

In fact, this problem can also be written in matrix form. Define the matrix $P$:

$$
P_{x, y}=
\begin{cases}
w_{(x, y)} & \text{if } (x, y) \in E \text{ and } x \neq t \\
0 & \text{if } (x, y) \notin E \text{ or } x=t \\
\end{cases}
$$

The required answer is then:

$$
\sum_{k \geq 0} k \times\left(P^k\right)_{s, t}
$$

where $\left(P^k\right)_{s, t}$ is the probability of reaching the target for the first time after exactly $k$ steps. When the graph is finite and every vertex can reach the target, it can be shown from the definition of $P$ that all its eigenvalues are less than 1, so the answer necessarily converges.

For convenience, on this page, unless stated otherwise, $n$ denotes $|V|$ and $m$ denotes $|E|$.

Also, on this page a sparse graph means a graph whose number of edges is of the same order as its number of vertices.

## Grid graphs

???+ note "Example 1 [Circles of Waiting](https://codeforces.com/problemset/problem/963/E)"
    A token is initially placed at the point $(0,0)$ of the Cartesian plane. Every second the token moves randomly. If it is currently at $(x, y)$, in the next second it moves to $(x-1, y)$ with probability $p_1$, to $(x, y-1)$ with probability $p_2$, to $(x+1, y)$ with probability $p_3$, and to $(x, y+1)$ with probability $p_4$. It is guaranteed that $p_1+p_2+p_3+p_4=1$.
    Find the expected time until it moves to a position whose Euclidean distance from the origin exceeds $R$. $0 \leq R \leq 50$, $p_1, p_2, p_3, p_4>0$, the answer is taken modulo $10^9+7$.

### Naive approach

Let $f(i, j)$ be the expected time for the token at $(i, j)$ to move to a position whose Euclidean distance from the origin exceeds $R$. The transition equation is:

$$
f(i, j)=
\begin{cases}
p_1 f(i-1, j) + p_2 f(i, j-1) + p_3 f(i+1, j) + p_4 f(i, j+1) + 1 & i^2 + j^2 \leq R^2 \\
0 & i^2 + j^2 > R^2
\end{cases}
$$

Since the transitions have no topological order, Gaussian elimination is required. The time complexity is $O\left(R^6\right)$, which cannot pass this problem.

### Direct elimination

Notice that most coefficients of the equations to be eliminated are 0; performing the elimination only at positions with nonzero values reduces the complexity.

Consider the elimination process: eliminate the equations in order from top to bottom in the coordinate system, and from left to right within the same row. Color the already eliminated equations yellow, the points adjacent to yellow points green, and the remaining points black, as in the figure below:

![graph-random-walk-1](images/graph-random-walk-1.svg)

Next, the equation corresponding to the next green cell is eliminated. In this equation, only the variables of the green cells and of the first black cell below it can have nonzero coefficients; and only in the equations of the green cells and of the first black cell below it can the coefficient of the current cell's variable be nonzero.

Notice that there are only $O(R)$ green cells, so eliminating a single equation costs $O\left(R^2\right)$. There are only $O\left(R^2\right)$ equations in total, so the complexity drops to $O\left(R^4\right)$, which passes this problem.

### Pivot-variable method

There are $O\left(R^2\right)$ equations and variables; if the size could be reduced to $O(R)$, naive Gaussian elimination would pass.

Take the variable of the leftmost cell in each row as a pivot variable, $2 R+1$ in total, and try to express the variables of the other cells as linear functions of these pivot variables. Process the columns from left to right; for every cell $(i, j)$ of the current column, notice that $f(i, j), f(i-1, j), f(i, j-1), f(i, j+1)$ are already known linear functions of the pivot variables, so rearranging the transition equation gives:

$$
f(i+1, j)=\frac{f(i, j)-p_1 f(i-1, j)-p_2 f(i, j-1)-p_4 f(i, j+1)-1}{p_3}
$$

This yields the representation of $f(i+1, j)$ as a linear function of the pivot variables. If $(i+1, j)$ already lies at Euclidean distance greater than $R$ from the origin, we obtain an equation $f(i+1, j)=0$. In the end, we obtain $2 R+1$ equations, and Gaussian elimination on these equations suffices.

In the stage of recursively deriving the linear functions of the pivot variables, there are $O\left(R^2\right)$ variables and deriving one variable takes $O(R)$ time; afterwards, the problem size has been reduced to $O(R)$. Both parts have time complexity $O\left(R^3\right)$, so the total time complexity is also $O\left(R^3\right)$, which passes this problem.

### Comparison of the two approaches

Below we compare the two approaches from several angles:

In terms of time complexity, the worst-case complexity of the pivot-variable method on a grid graph is $O(n \sqrt{n})$ (it is highest when both the length and the width of the grid are of order $O(\sqrt{n})$), while the worst-case complexity of direct elimination on a grid graph is $O\left(n^2\right)$; the pivot-variable method is better.

In terms of precision, for problems requiring real-number computation instead of modular arithmetic, direct elimination is more precise than the pivot-variable method.

In terms of applicability, the two approaches suit different situations.

When the grid graph contains obstacles or edges with probability $0$ of being taken, the pivot-variable method needs one extra pivot variable per obstacle or zero-probability edge; when the number of obstacles or zero-probability edges exceeds $O(R)$, the complexity of the pivot-variable method increases, while the complexity of direct elimination remains unchanged.

However, the pivot-variable method can also eliminate transition equations similar to those of grid graphs, for example $f(i, j)=p_1 f(i+1, j)+p_2 f(i, j+1)+p_3 f(\operatorname{pre}(i, j))+1$, where $\operatorname{pre}(i, j)=(x, y)(x \leq i, y \leq j)$ is a value given by the problem, whereas the complexity analysis of direct elimination does not apply to this model.

Furthermore, computing the determinant of the adjacency matrix of a grid graph cannot use the pivot-variable method; only direct elimination can be used to improve the time complexity.

In summary, both approaches have their strengths, and the choice should be made according to the specific problem.

## Sparse graphs

???+ note "Example 2 Expected Value"
    Given a simple undirected connected sparse graph $G=(V, E)$, a token is initially placed at $v_1$; every second the token chooses, uniformly at random, one of the edges incident to the current vertex and moves to the vertex it points to. Find the expected time to reach $v_n$. $n \leq 2000$, the answer is taken modulo $p$, where $p$ is a prime randomly chosen from the interval $\left[10^9, 1.01 \times 10^9\right]$.

### Basics

**Definition 4.1.** Every polynomial $p(λ)$ satisfying $p(A) = 0$ is called an annihilating polynomial of the matrix $A$.

**Definition 4.2.** Let $I_n$ denote the identity matrix of order $n$. The characteristic polynomial of an $n × n$ matrix $A$ is defined as $p(λ) = \det(λI_n - A)$, where $\det$ denotes the determinant of a matrix.
It is easy to see that the degree of the characteristic polynomial of a matrix $A$ of order $n$ does not exceed $n$.

**Theorem 4.2.** (Cayley–Hamilton theorem) The characteristic polynomial of any matrix is an annihilating polynomial of it.

Therefore, the degree of the minimal annihilating polynomial of a matrix of order $n$ also does not exceed $n$.

### Solving the original problem

Notice that the expected walking time is $E(t)=\sum_{i\geq0}\Pr[t>i]$; if we can compute the probability that the walk has not finished after $i$ steps, summing over all $i ≥ 0$ gives the answer.

Let $f(i, j)$ be the probability of being at $j$ after $i$ steps without having visited $n$. Then:

$$
f(i,j)=\sum_{(k,j)\in E}\frac{f(i-1,k)}{\deg_k}(j\neq n)
$$

where $\deg_k$ denotes the degree of $k$.

Notice that the transition of $f$ does not depend on $i$, so one transition can be seen as multiplication by a matrix, i.e. $f{i+1}=f_iM$. Since the degree of the minimal annihilating polynomial of $M$ does not exceed $n$, the length of the shortest linear recurrence of $f$ does not exceed $n$ either, so the length of the shortest recurrence of $\Pr[t>i]=\sum_{j=1}^{n-1}f(i,j)$ also does not exceed $n$. We can compute $\Pr[t>0],\Pr[t>1],\cdots,\Pr[t>3n]$ in $O(nm)$ time, and then use the *Berlekamp–Massey* algorithm to find the shortest recurrence of $\Pr[t > i]$ in $O(n^2)$ time.

Consider finding the generating function of a linear recurrent sequence $a$ of order $k$. Suppose that for $i ≥ i_0$, $a_i=\sum_{j=1}^kc_ja_{i-j}$, and let the generating functions of $a$ and $c$ be $A(x)$ and $C(x)$. Then $A(x)=A(x)C(x)+A_0(x)$, where $A_0(x)$ is determined by the terms with $i < i_0$.

Back to the original problem: since we can find the shortest recurrence of $\Pr[t > i]$, we can compute $C(x)$ and $A_0(x)$ (with the same definitions as in the previous paragraph), and rearranging gives $A(x)=\frac{A_0(x)}{1-C(x)}$. We want $\sum_{i\geq0}[x^i]A(x)$; it is easy to see that this value equals $A(1)$, so substituting $x = 1$ solves the problem. Since the modulus is a random prime, we may assume the denominator is not $0$.

Thus we solved this problem in $O(nm+n^2)$ time. If the numbers of vertices and edges of $G$ are of the same order, the time complexity in this problem can be regarded as $O(n^2)$.

## General graphs

???+ note "Example 3 Frank"
    Given a simple strongly connected directed graph $G = (V, E)$, for all $1 ≤ s ≤ n$, $1 ≤ t ≤ n$, $s ≠ t$, answer the following question:
    a token is initially placed at $v_s$; every second the token chooses, uniformly at random, one of the outgoing edges of the current vertex and moves to the vertex it points to. Find the expected time to reach $v_t$. $3 ≤ n ≤ 400$.

### Analysis and transformation

Let $p_{i, j}$ be the probability that the token at $i$ chooses the outgoing edge $(i, j)$ and moves to $j$; in particular, the probability is $0$ when the edge does not exist. Let $f_{i,j}$ be the expected time of a random walk from $i$ to $j$; in particular, $f_{i,i} = 0$. For $i ≠ j$, the transition equation is:

$$
f_{i,j}=1+\sum_{1\leq k\leq n}p_{i,k}f_{k,j}
$$

For $i = j$, let $g_i$ be the expected time of first returning to $i$ for a random walk starting at $i$; then:

$$
f_{i,i}=1-g_i+\sum_{1\le k\le n}p_{i,k}f_{k,i}
$$

For easier observation, we write the transition equations in matrix form. Let $P$ be the transition matrix of this graph, $F$ the answer matrix, $I$ the identity matrix of order $n$, $J$ the all-ones matrix of order $n$, and $G$ a matrix of order $n$ with $G_{i,i} = g_i$ and $0$ elsewhere. Then:

$$
F=J-G+PF
$$

If we can compute $G$, we only need to solve the equation:

$$
(I − P)F = J − G
$$

### Computing G

**Definition 5.1.** A stationary distribution of a transition matrix $P$ of order $n$ is an $n$-dimensional vector $π$ satisfying $\sum_{i=1}^{n}\pi_{i}=1$ and $πP = π$. Here every component of $π$ lies in the interval $[0,1]$.

The practical meaning of a stationary distribution is easy to see. If at some moment the token is at $v_i$ with probability $π_i$, then at every later moment the token still follows this probability distribution. We can compute $π$ in $O(n^3)$ time by solving the equations with Gaussian elimination. So what is the relationship between $π$ and $G$?

**Theorem 5.1.** For every $1 ≤ i ≤ n$, $π_ig_i = 1$.

???+ note "Proof"
    From $F = J - G + PF$, rearranging gives:
    
    $$
    G = PF + J − F
    $$
    
    Multiplying both sides on the left by $π$:
    
    $$
    πG = πPF + πJ − πF
    $$
    
    By the definition of $π$, $πP = π$, hence:
    
    $$
    πG = πJ
    $$
    
    Therefore:
    
    $$
    \pi_ig_i=\sum_{j=1}^n\pi_j=1  
    $$

This proves the claim.

So, by introducing the stationary distribution, we can compute $G$ in $O(n^3)$ time.

### Solving the original problem

While solving the equation we encounter a problem: $(I - P)$ does not have full rank, so the system cannot be solved by multiplying by an inverse matrix.

**Definition 5.2.** A directed spanning tree of a directed graph $G = (V,E)$ rooted at $r\in V$ is a subgraph $T = (V,A)$ of $G$ such that:

1.  for every $i ≠ r$, the out-degree of $i$ is $1$;
2.  the out-degree of $r$ is $0$;
3.  $T$ contains no cycle.

**Lemma 5.1.** (Matrix-tree theorem for directed graphs) For a directed graph $G$, let $D$ be its out-degree matrix, i.e. $D_{i,i} = d_i$, $D_{i,j} = 0(i ≠ j)$, where $d_i$ is the out-degree of $i$, and let $A$ be its adjacency matrix. Then the number of directed spanning trees rooted at $r$ equals the determinant of $D - A$ with the $r$-th row and $r$-th column removed.

**Theorem 5.2.** For the transition matrix $P$ of a strongly connected graph $G = (V,E)$, the rank of $(I - P)$ is $n - 1$.

???+ note "Proof"
    Since multiplying a row of a matrix by a nonzero constant does not change its rank, we multiply the $i$-th row of $(I - P)$ by the out-degree of $v_i$ to obtain a new matrix $L$; it suffices to show that the rank of $L$ is $n - 1$.  
    Since every row of $L$ sums to $0$, summing all column vectors of $L$ gives the zero vector, i.e. these vectors are linearly
    dependent, so the rank of $L$ is not $n$.  
    It is easy to see that $L$ equals the out-degree matrix of $G$ minus its adjacency matrix, so by Lemma 5.1 the determinant of $L$ with the $i$-th row and $i$-th column
    removed is the number of directed spanning trees rooted at $v_i$.  
    Since G is strongly connected, the number of directed spanning trees rooted at any vertex is nonzero, i.e. $L$ with the $i$-th row and
    $i$-th column removed still has full rank.  
    Since adding a column does not decrease the rank, all row vectors of $L$ with the $i$-th row removed are linearly independent. Hence the rank of $L$ is $n - 1$.  
    Back to the original problem, consider solving its equation. For convenience, write the equation in the form $AX = B$,
    where $A$, $B$ are known and $X$ must be found. Since $A$ does not have full rank, there are infinitely many solutions; we first find a particular solution.
    Perform Gaussian elimination on $A$ and $B$ together. Reduce the first $n - 1$ rows of $A$ to a form with values only on the main diagonal and in the $n$-th column,
    and the last row to all zeros, i.e. the following form:
    
    $$
    \begin{bmatrix}
    1 & 0 & 0 & \cdots & 0 & a_1 \\0&1&0&\cdots&0&a_2\\0&0&1&\cdots&0&a_3\\
    \vdots&\vdots&\vdots&\ddots&\vdots&\vdots
    \\0&0&0&\cdots&1&a_{n-1}\\0&0&0&\cdots&0&0
    \end{bmatrix}
    X=
    \begin{bmatrix}
    b_{1,1}&b_{1,2}&b_{1,3}&\cdots&b_{1,n-1}&b_{1,n}
    \\b_{2,1}&b_{2,2}&b_{2,3}&\cdots&b_{2,n-1}&b_{2,n}
    \\b_{3,1}&b_{3,2}&b_{3,3}&\cdots&b_{3,n-1}&b_{3,n}
    \\\vdots&\vdots&\vdots&\ddots&\vdots&\vdots
    \\b_{n-1,1}&b_{n-1,2}&b_{n-1,3}&\cdots&b_{n-1,n-1}&b_{n-1,n}
    \\0&0&0&\cdots&0&0
    \end{bmatrix}
    $$
    
    Set $X_{n,i} = 0$; this yields a particular solution, denoted $Y$. Next, adjust the particular solution into the true solution.  
    Note that $X_{n,i} = 0$; from the combinatorial meaning we have $Y_{i,j} = 1 + Y_{j,j} + P_{i,k}X_{k,j}$, from which $X_{i,j} = Y_{i,j} - Y_{j,j}$ follows easily.
    Finally, the problem is solved in $O(n^3)$ time.

## References

1.  浅谈图模型上的随机游走问题 (On random walk problems on graph models). Papers of the Chinese national team candidates for IOI 2019 (pp. 17–26)
