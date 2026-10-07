---
title: Introduction to DP optimizations
---

## Introduction

This page lists some common optimization techniques for dynamic programming (DP). "DP optimization" refers to the following: for many dynamic programming problems it is easy to write down a naive state transition equation, but computing it directly is often inefficient, so some techniques are needed to reduce the time complexity.

These techniques are closely related to each other, often share similar ideas, and frequently have to be combined. Therefore this article only gives a rough classification and focuses on the most basic ideas.

## Optimization with common techniques

The transitions of many dynamic programming problems can be optimized with common algorithms and data structures.

Such techniques appear in two typical situations. In the first one, the DP problem has a state transition equation of the form

$$
f(i) = F(a_i,\{f(j) : j < i\}).
$$

Here the computation of the current state $f(i)$ depends on the current input $a_i$ and on the states of the whole previous sequence $\{f(j):j < i\}$. Hence we can maintain a data structure and treat every computation of $f(i)$ as a query; after obtaining the current state $f(i)$, we perform one more update operation on the data structure, to be used in later transitions.

In the second situation, the DP problem has a state transition equation of the form

$$
f(i,\cdot) = F(a_i,f(i-1,\cdot)).
$$

Here every $f(i,\cdot)$ is an array or some other more complex object. So although $f(i,\cdot)$ depends on a single previous state only, the complexity of one transition is high and it has to be optimized with data structures and similar techniques.

### Prefix sum optimization of DP

Related page: [prefix sums](../../basic/prefix-sum.md#前缀和)

If the computation of the current state depends on the sum of a subsegment of previous states, the computation can be sped up by maintaining prefix sums. One class of problems involving high-dimensional prefix sums is also called [SOS DP](../../basic/prefix-sum.md#特例子集和-dp).

Exercises:

-   [Luogu P2513 \[HAOI2009\] Sequence with a given number of inversions](https://www.luogu.com.cn/problem/P2513)
-   [AtCoder Educational DP Contest M - Candies](https://atcoder.jp/contests/dp/tasks/dp_m)

### Monotonic queue/monotonic stack optimization of DP

Main page: [monotonic queue/monotonic stack optimization](./monotonic-queue-stack.md)

If the current state depends on a range minimum/maximum or similar information about previous states, the computation can be sped up by maintaining a monotonic queue or a monotonic stack.

### Segment tree/Fenwick tree optimization of DP

Related pages: [segment tree](../../ds/seg.md), [Fenwick tree](../../ds/fenwick.md)

If every state transition queries the sum, minimum/maximum or similar information on some range, or if a single update affects a whole range, the computation can be sped up by maintaining a segment tree or a Fenwick tree.

Exercises:

-   [AtCoder Educational DP Contest Q - Flowers](https://atcoder.jp/contests/dp/tasks/dp_q)
-   [AtCoder Educational DP Contest W - Intervals](https://atcoder.jp/contests/dp/tasks/dp_w)
-   [Codeforces 115 E. Linear Kingdom Races](https://codeforces.com/problemset/problem/115/E)

### CDQ divide and conquer optimization of DP

Main page: [CDQ divide and conquer optimization of DP](../../misc/cdq-divide.md#cdq-分治优化-1d1d-动态规划的转移)

As above, view the whole DP process as a sequence of queries and updates. In some problems computing them in order is too slow, so the whole sequence of queries and updates can be processed offline and sped up with CDQ divide and conquer.

CDQ divide and conquer optimization of DP is also common in the following kinds of problems:

-   [slope optimization of DP based on CDQ divide and conquer](./slope.md#optimizing-dp-with-binary-searchcdqbalanced-trees)
-   [divide and conquer optimization of DP with decision monotonicity](./quadrangle.md#divide-and-conquer)

### Binary lifting optimization of DP

Related page: [binary lifting](../../basic/binary-lifting.md)

In some problems the state $f(i)$ is defined as the result of performing $2^i$ transitions starting from the initial state. This reformulation of the original problem uses the idea of binary lifting (doubling), so it is often called binary lifting optimization of DP.

Sometimes DP problems with a state transition equation of the form

$$
f(i,j) = f(i-1,f(i-1,j))
$$

are also called binary lifting (optimized) DP.

Exercises:

-   [Luogu P1081 \[NOIP 2012 Senior\] Road trip](https://www.luogu.com.cn/problem/P1081)
-   [Luogu P1613 Running away](https://www.luogu.com.cn/problem/P1613)
-   [Luogu P4739 \[CERC2017\] Donut Drone](https://www.luogu.com.cn/problem/P4739)

## Optimization using the structure of the problem

Many dynamic programming problems have structural properties such as convexity or monotonicity, and exploiting them properly allows solving the problem quickly.

### Slope optimization of DP

Main page: [slope optimization](./slope.md)

Similarly to the techniques of the previous section, exploiting the convexity of the problem allows speeding up a single transition by maintaining a convex hull.

### Quadrangle inequality optimization of DP

Main page: [quadrangle inequality optimization](./quadrangle.md)

DP problems whose functions satisfy the quadrangle inequality usually have some kind of decision monotonicity. Exploiting this property, there are many specialized techniques that reduce the computational complexity. Common problem types include one-dimensional decision monotonicity problems, interval partition problems, interval merging problems, and so on.

### Slope Trick optimization of DP

Main page: [Slope Trick](./slope-trick.md)

In some problems the difference (i.e. the slope) of the state function is easier to maintain during the state transitions than the function itself. This optimization usually also requires convexity of the problem.

### WQS binary search/convex optimization of DP

Main page: [WQS binary search](./wqs-binary-search.md)

For optimization DP problems with a constraint on the number of chosen items, if the problem is easier to solve without the constraint and the optimal value is a convex function of that constraint, the computation can be simplified with WQS binary search.

## Optimization with mathematical methods

The transitions of many dynamic programming problems can be sped up with mathematical tools.

### Matrix exponentiation optimization of DP

Related page: [binary exponentiation](../../math/binary-exponentiation.md)

If the state transition equation of a DP problem can be written in the autonomous form

$$
f(i) = F(f(i-1)),
$$

that is, the current state $f(i)$ depends only on the previous state $f(i-1)$ and on no other input, then binary exponentiation directly speeds up the computation of

$$
f(n) = F^n(f(0))
$$

which gives the final answer. Since a single operation $F$ can often be written as a matrix, this technique is usually called matrix exponentiation optimization of DP. In fact, any transformation that satisfies associativity (i.e. any element of a [monoid](../../math/algebra/basic.md#群)) can be sped up with this technique.

Exercises:

-   [Luogu P1397 \[NOI2013\] Matrix game](https://www.luogu.com.cn/problem/P1397)
-   [Luogu P3176 \[HAOI2015\] Digit string splitting](https://www.luogu.com.cn/problem/P3176)
-   [Codeforces 576 D. Flights for Regular Customers](https://codeforces.com/problemset/problem/576/D)
-   [Luogu P6772 \[NOI2020\] Gourmet](https://www.luogu.com.cn/problem/P6772)

### FFT optimization of DP

Related page: [FFT](../../math/poly/fft.md)

If the state transition equation of a DP problem has the form of a convolution, the transition can be sped up with FFT. Of course, depending on the specific problem, other polynomial techniques may be used as well.

Exercises:

-   [Codeforces 553 E. Kyoya and Train](https://codeforces.com/contest/553/problem/E)
-   [Codeforces 1784 D. Wooden Spoon](https://codeforces.com/problemset/problem/1784/D)

### Lagrange interpolation optimization of DP

Related page: [Lagrange interpolation](../../math/numerical/interp.md#lagrange-插值法)

In some DP problems the state function $f(i,j)$ is a polynomial of degree $k$ in $j$. Then we can compute its values at $k+1$ points by brute force, obtain an expression for $f(i,\cdot)$ by Lagrange interpolation, and thus optimize the transition or even obtain the answer directly.

Exercises:

-   [Luogu P5223 Function](https://www.luogu.com.cn/problem/P5223)
-   [Luogu P4463 \[Chinese IOI training camp 2012\] calc](https://www.luogu.com.cn/problem/P4463)
-   [Luogu P5469 \[NOI2019\] Robot](https://www.luogu.com.cn/problem/P5469)

## Optimization by simplifying the states

Besides optimizing the transitions, the computational complexity can also be reduced by simplifying the states.

### DP of DP and DFA minimization

Main pages: [DP of DP](../dp-of-dp.md), [DFA minimization](../../misc/fsm.md#dfa-最小化)

In some DP problems the state function can be written in the form $f(i,x)$, but the transition of $x$ itself is complicated and may even depend on another DP problem. For such problems we can first build an automaton for the transitions of the state $x$, reduce the number of states by DFA minimization, and then run the outer DP.

### State design optimization of DP

Main page: [state design optimization](./state.md)

Some special problems can be solved with a drastically reduced number of states through clever state design.

## Further reading

-   [A potpourri of DP optimization methods (DP 优化方法大杂烩) by Alex Wei](https://www.cnblogs.com/alex-wei/p/DP_Involution.html)
