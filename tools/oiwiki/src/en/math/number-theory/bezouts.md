---
title: Bézout's identity and linear Diophantine equations
---

Bézout's identity reveals a deep connection between the greatest common divisor and integer linear combinations, and it is one of the most basic and most important results in number theory. Based on it, this article further discusses how to solve linear Diophantine equations.

## Bézout's identity

**Bézout's identity**, also known as Bézout's lemma, gives a necessary and sufficient condition for an integer to be expressible as a linear combination of two integers with integer coefficients.

???+ note "Bézout's identity"
    Let $a,b$ be integers that are not both zero. Then for any integers $x,y$ we have $\gcd(a,b)\mid ax+by$; moreover, there exist integers $x,y$ such that $ax+by=\gcd(a,b)$.

??? note "Proof"
    Write $d=\gcd(a,b)$. Since $d\mid a,b$, there exist integers $u,v$ such that $a=du,~b=dv$. Therefore we always have
    
    $$
    ax + by = d(ux+vy).
    $$
    
    This shows that $d\mid ax+by$.
    
    Conversely, we need to show that there exist $x,y$ for which the equality holds. Since $\gcd(a,b)=\gcd(-a,b)=\gcd(a,-b)$, we may assume that $a,b$ are both non-negative. If one of $a,b$ is $0$, say $b=0$, then their greatest common divisor is $d=a$, and obviously $(x,y)=(1,0)$ satisfies the equality. Next, consider the case where $a,b$ are both nonzero; then $a,b$ are both positive.
    
    Consider the process of the Euclidean algorithm:
    
    $$
    \begin{aligned}
    a   &= q_1b   + r_1, && 0\le r_1 < b,\\
    b   &= q_2r_1 + r_2, && 0\le r_2 < r_1,\\
    r_1 &= q_3r_2 + r_3, && 0\le r_3 < r_2,\\
        & \cdots \\
    r_{n-3} &= q_{n-1}r_{n-2} + r_{n-1}, && 0\le r_{n-1} < r_{n-2},\\
    r_{n-2} &= q_nr_{n-1} + r_n,         && 0\le r_n     < r_{n-1},\\
    r_{n-1} &= q_{n+1}r_n.
    \end{aligned}
    $$
    
    Since the greatest common divisor is $d$, in the last step of the Euclidean algorithm we must have $r_n=d$. So the second-to-last equation can be written as
    
    $$
    d = r_n = r_{n-2} - q_nr_{n-1}.
    $$
    
    From the third-to-last equation we solve
    
    $$
    r_{n-1} = r_{n-3} - q_{n-1}r_{n-2}
    $$
    
    and substitute it into the previous expression, which eliminates $r_{n-1}$:
    
    $$
    \begin{aligned}
    d &= r_{n-2} - q_n(r_{n-3} - q_{n-1}r_{n-2}) \\
    &= (1 + q_nq_{n-1})r_{n-2} - q_nr_{n-3}.
    \end{aligned}
    $$
    
    Similarly, we can eliminate all of $r_{n-2},r_{n-3},\cdots,r_2,r_1$ step by step and finally obtain
    
    $$
    d = xa + yb.
    $$
    
    This proves that there exist $x,y$ such that $ax+by=d$. By the analysis above, this also proves the original statement.

Here, the proof of existence is constructive: it also gives a method for computing these coefficients. This method is exactly the [extended Euclidean algorithm](./gcd.md#extended-euclidean-algorithm).

Considering the special case of Bézout's identity when $\gcd(a,b)=1$, we obtain the following corollary:

???+ note "Corollary"
    Integers $a,b$ are coprime if and only if there exist integers $x,y$ such that $ax+by=1$.

### The case of several integers

Bézout's identity can be generalized to the case of several integers.

???+ note "Theorem"
    Let $a_1,a_2,\cdots,a_n$ be integers that are not all zero. Then for any integers $x_1,x_2,\cdots,x_n$ we have $\gcd(a_1,a_2,\cdots,a_n)\mid a_1x_1+a_2x_2+\cdots+a_nx_n$; moreover, there exist integers $x_1,x_2,\cdots,x_n$ such that $\gcd(a_1,a_2,\cdots,a_n)=a_1x_1+a_2x_2+\cdots+a_nx_n$.

??? note "Proof"
    Use the fact that $\gcd(a_1,a_2,\cdots,a_n)=\gcd(\gcd(a_1,a_2,\cdots,a_{n-1}),a_n)$ and induct on $n$.

### Example problem

???+ example "[Codeforces 510 D. Fox And Jumping](https://codeforces.com/problemset/problem/510/D)"
    There are $n\le 300$ cards, each with values $l_i$ and $c_i$. On an infinitely long tape, you may pay $c_i$ money to buy card $i$, after which you can jump $l_i$ units to the left or to the right any number of times. Find the minimum amount of money needed to be able to jump to every position on the tape. If it is impossible, output $-1$.

??? note "Solution"
    Analyzing the problem, we find that in order to jump onto every cell, the chosen numbers $l_{i_1}, \cdots, l_{i_k}$ must be able to produce an absolute value of $1$ through several additions or subtractions. That is, there exist integers $x_1, \cdots, x_k$ such that $l_{i_1} x_1 + \cdots + l_{i_k} x_k = 1$. By Bézout's identity for several integers, this is equivalent to choosing some numbers from the array $l_1, \cdots, l_n$ whose greatest common divisor is $1$, while requiring the total cost to be minimal.
    
    **Solution 1**: treat the minimum total cost as a shortest path problem, which can be solved with Dijkstra's algorithm. The vertices of the graph store the current value of the greatest common divisor. The starting vertex of the graph is $0$ and the target vertex is $1$. In each step, from the current vertex $x$ we walk along an edge of length $c_i$ to the vertex $\gcd(x,l_i)$. The time complexity of this algorithm is $O(n^2\log n)$.
    
    **Solution 2**: choosing some numbers from the array $l_1, \cdots, l_n$ whose greatest common divisor is $1$ with minimal total cost brings to mind the 0-1 knapsack problem.
    
    Let $f_{i, j}$ denote the minimum cost considering the first $i$ numbers with greatest common divisor $j$; then we have the transition:
    
    $$
    f_{i, j} = \min\left\{f_{i - 1, j},~\min_{\gcd(k, l_i) = j}\{f_{i - 1, k} + c_i\}\right\}.
    $$
    
    After the DP, the final total cost is $f_{n, 1}$.
    
    As in the ordinary 0-1 knapsack problem, it can be optimized with a rolling array, removing the first dimension. Moreover, the greatest common divisors $j$ that 300 numbers can form are very sparse, so they can be stored in a hash table.
    
    In fact, the graph built in Solution 1 is exactly the state transition graph of the dynamic programming in Solution 2; Solution 2 amounts to finding the shortest path in a directed acyclic graph by dynamic programming, so Solutions 1 and 2 are equivalent. However, Solution 2 does not need to store the whole graph, and the time complexity of the DP is $O(n + m)$ (where $m$ is the number of edges of the state transition graph), which is lower than Dijkstra's algorithm, so Solution 2 is better in both time and space.

## Linear Diophantine equations

A **linear Diophantine equation** is a Diophantine equation of the form

$$
a_1x_1 + a_2x_2 + \cdots + a_nx_n = b
$$

where $a_1,a_2,\cdots,a_n$ are all integers. The goal of this section is to find all of its integer solutions.

### The case of two variables

First consider the linear Diophantine equation in two variables:

$$
a_1x_1 + a_2x_2 = b.
$$

Bézout's identity states that this equation has a solution if and only if

$$
d = \gcd(a_1,a_2) \mid b.
$$

Next, assume this condition holds. Using the extended Euclidean algorithm we can find an integer solution $(x_1^*,x_2^*)$ of the equation $a_1x_1 + a_2x_2 = d$. From it, we obtain a particular solution of the original equation

$$
(x_1^\circ,x_2^\circ) = \left(\frac{b}{d}x_1^*,\frac{b}{d}x_2^*\right).
$$

To obtain all solutions, subtract the identity $a_1x_1^\circ+a_2x_2^\circ = b$ from the original equation; we get

$$
a_1(x_1 - x_1^\circ) + a_2(x_2 - x_2^\circ) = 0.
$$

This is a homogeneous linear Diophantine equation in $(x_1-x_1^\circ,x_2-x_2^\circ)$, whose general solution is

$$
(x_1-x_1^\circ,x_2-x_2^\circ) = \left(t\dfrac{a_2}{d},-t\dfrac{a_1}{d}\right).\quad(t\in\mathbf Z)
$$

Therefore, the general solution of the original equation is

$$
(x_1,x_2) = \left(x_1^\circ + t\dfrac{a_2}{d},x_2^\circ - t\dfrac{a_1}{d}\right).\quad(t\in\mathbf Z)
$$

These are a series of equally spaced lattice points on the line $a_1x_1+a_2x_2 = b$.

### The case of several variables

Once the case of two variables is solved, the case of several variables is also easy to solve. For the linear Diophantine equation in $n$ variables

$$
a_1x_1 + a_2x_2 + \cdots + a_nx_n = b,\quad (n>2)
$$

by Bézout's identity the equation has a solution if and only if

$$
\gcd(a_1,a_2,\cdots,a_n) \mid b.
$$

Similarly to the two-variable case, the general solution of a linear Diophantine equation in several variables can also be written in the form

$$
(x_1^\circ,x_2^\circ,\cdots,x_n^\circ) + \sum_{k=1}^{n-1} t_k(x_1^{(k)},x_2^{(k)},\cdots,x_n^{(k)})
$$

where $x^\circ$ is a particular solution and $x^{(k)}$ are $(n-1)$ linearly independent solutions of the corresponding homogeneous equation.

To find the concrete form of the general solution, we can reduce the equation in $n$ variables to an equation in $(n-1)$ variables. Write $d_1 = \gcd(a_1,a_2)$; then, by Bézout's identity, the set of all values of $a_1x_1+a_2x_2$ is exactly the set of all multiples of $d_1$. Therefore, we can first solve the linear Diophantine equation in $(n-1)$ variables:

$$
d_1y_1 + a_3x_3 + a_4x_4 + \cdots + a_nx_n = b.
$$

Suppose the general solution obtained for it is

$$
\begin{aligned}
y_1 &= y_1^\circ + \sum_{k=2}^{n-1}t_ky_1^{(k)}, \\
x_i &= x_i^\circ + \sum_{k=2}^{n-1}t_kx_i^{(k)},\quad i=3,\cdots,n.
\end{aligned}
$$

Let $(x_1^*,x_2^*)$ be a particular solution of $a_1x_1+a_2x_2=d_1$; then, by the discussion in the previous section, the general solution of the two-variable linear Diophantine equation $a_1x_1+a_2x_2=d_1y_1$ in $x_1,x_2$ is

$$
x_1 = x_1^*y_1 + t_1\dfrac{a_2}{d_1},~x_2 = x_2^*y_1 - t_1\dfrac{a_1}{d_1}.
$$

Substituting the expression for $y_1$, we obtain the general solution of the original equation

$$
\begin{aligned}
x_1 &= x_1^*y_1^\circ + t_1\dfrac{a_2}{d_1} + \sum_{k=2}^{n-1}t_kx_1^*y_1^{(k)}, \\
x_2 &= x_2^*y_1^\circ - t_1\dfrac{a_1}{d_1} + \sum_{k=2}^{n-1}t_kx_2^*y_1^{(k)}, \\
x_i &= x_i^\circ + \sum_{k=2}^{n-1}t_kx_i^{(k)},\quad i=3,\cdots,n.
\end{aligned}
$$

## Frobenius coin problem

Bézout's identity gives a necessary and sufficient condition for an integer to be linearly expressible by several integers. Closely related to this is the **Frobenius coin problem**:

-   If coins come in several integer denominations $a_1,a_2,\cdots,a_n$ and $\gcd(a_1,a_2,\cdots,a_n)=1$, what is the largest integer that cannot be formed from these coins?

This again asks when an integer $k$ can be expressed in the form $a_1x_1+a_2x_2+\cdots+a_nx_n$; in Bézout's identity the $x_i$ may be arbitrary integers, whereas in the Frobenius coin problem the $x_i$ can only be natural numbers (including zero).

The case of a single coin is trivial, because then we must have $a_1=1$ and every natural number can be expressed by it. The case $n>2$, on the other hand, is too complicated, so this section only discusses the case $n=2$.

### Sylvester's theorem

In 1882, Sylvester completely solved the Frobenius coin problem for $n = 2$:

???+ note "Theorem (Sylvester)"
    For coprime positive integers $a_1,a_2$, the largest integer that cannot be written as $a_1x_1+a_2x_2~(x_1,x_2\in\mathbf N)$ is $C = a_1a_2 - a_1 - a_2$. Moreover, for every $k\in\mathbf Z$, exactly one of the integers $k$ and $C-k$ can be written in this form.

For convenience, we call integers that can be written in the form $a_1x_1+a_2x_2~(x_1,x_2\in\mathbf N)$ **representable**.

??? note "Proof 1"
    Since $a_1,a_2$ are coprime, for any integer $k$ the equation $a_1x_1+a_2x_2=k$ certainly has a solution, and the general solution is
    
    $$
    (x_1,x_2) = (x_1^\circ + ta_2, x_2^\circ - ta_1).\quad(t\in\mathbf Z)
    $$
    
    Take $t$ to be the quotient of the division with remainder of $x_2^\circ$ by $a_1$; then the remainder $x_2 = x_2^\circ-ta_1$ lies between $0$ and $a_1-1$. Consider the solution $(x_1,x_2)$ obtained this way. Since $x_2$ is the smallest non-negative integer value it can take, $k$ is representable if and only if $x_1\ge 0$.
    
    **Step 1**: prove that all integers greater than $C$ are representable.
    
    When $k > C$, we have
    
    $$
    a_1x_1 = k - a_2x_2 > C - a_2(a_1-1) = -a_1.
    $$
    
    So $x_1 > -1$, that is, $x_1\ge 0$. This shows that $(x_1,x_2)$ is a solution in natural numbers. Hence $k$ can be written in the required form.
    
    **Step 2**: prove that $C$ is not representable. Consequently, $C$ is the largest non-representable integer, and $k$ and $C-k$ are not both representable.
    
    By contradiction. Suppose $C$ is representable, i.e. there exist $x_1,x_2\in\mathbf N$ such that $a_1x_1+a_2x_2=C$. Substituting the expression for $C$, we get
    
    $$
    a_1a_2 = a_1(x_1+1) + a_2(x_2+1).
    $$
    
    Therefore $a_2\mid (x_1+1)$ and $a_1\mid (x_2+1)$. Since $x_1+1,x_2+1$ are both positive, we have
    
    $$
    a_1a_2 \ge a_1a_2 + a_2a_1 = 2a_1a_2.
    $$
    
    A contradiction. This shows that $C$ is not representable. Combined with Step 1, it is the largest non-representable integer.
    
    If $k$ and $C-k$ were both representable, then adding the coefficients in the representations of $k$ and $C-k$ would give the coefficients of a representation of $C$, contradicting the non-representability of $C$; hence at most one of $k$ and $C-k$ is representable.
    
    **Step 3**: prove that if $k$ is not representable, then $C-k$ must be representable.
    
    Let $(x_1,x_2)$ be the integer solution of the equation $a_1x_1+a_2x_2=k$ described above. It was shown above that $k$ being non-representable is equivalent to $x_1<0$. Therefore, we have
    
    $$
    C - k = a_1a_2 - a_1 - a_2 - a_1x_1 - a_2x_2 = a_1(-1-x_1) + a_2(a_1-1-x_2).
    $$
    
    Here $-1-x_1$ and $a_1-1-x_2$ are both non-negative integers, so $C-k$ is representable.

??? note "Proof 2"
    Here we only prove that $C=a_1a_2-a_1-a_2$ is the largest non-representable integer; the rest of the proof is similar to Proof 1.
    
    Consider, modulo $a_2$, the smallest representable natural number in each residue class. Since different natural numbers in the same residue class can be converted into one another by adding or subtracting several copies of $a_2$, when discussing the smallest representable number it suffices to consider the possibility of adding or subtracting $a_1$. Since $a_1$ and $a_2$ are coprime, the smallest representable natural numbers in the residue classes are exactly the multiples of $a_1$
    
    $$
    0,~a_1,~2a_1,~\cdots,~(a_2-1)a_1.
    $$
    
    Therefore, the largest non-representable number is
    
    $$
    \max_{0\le i < a_2} ia_1 - a_2 = (a_2-1)a_1 - a_2 = C.
    $$

### Geometric meaning

View the equation $a_1x_1 + a_2x_2 = k$ as a line. Then $k$ is representable if and only if this line passes through at least one lattice point in the first quadrant (including the coordinate axes). When $k < a_1a_2$, this line passes through at most one lattice point in the first quadrant. Therefore, for $0\le k < a_1a_2$, the integer $k$ is representable if and only if this line passes through exactly one lattice point in the first quadrant.

Consequently, for $k < a_1a_2$, the number of representable natural numbers less than or equal to $k$ is exactly equal to the number of lattice points in the first quadrant below the line $a_1x_1 + a_2x_2 = k$ (including the points on the boundary). This number equals

$$
\sum_{i=0}^{\lfloor k / a_1 \rfloor} \left(\left\lfloor\dfrac{k-ia_1}{a_2}\right\rfloor+1\right).
$$

This is the classic problem of lattice points under a line, which can be solved with the [Euclidean-like algorithm](./euclidean.md#euclidean-like-algorithm) in $O(\log\min\{a_1,a_2,k\})$ time.

### Exercises

-   [Luogu P3951 NOIP2017 提高组 小凯的疑惑/蓝桥杯 2013 省 买不到的数目 (NOIP 2017, senior group, Xiao Kai's Puzzle / Lanqiao Cup 2013, provincial round, The Amount You Cannot Pay)](https://www.luogu.com.cn/problem/P3951)
