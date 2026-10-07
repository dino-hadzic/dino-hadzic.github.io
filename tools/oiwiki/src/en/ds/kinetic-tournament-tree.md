---
title: Kinetic Tournament Tree
---

Prerequisites: [segment tree](./seg.md)

## Problem introduction

Given a sequence of univariate linear functions $F=\{f_1,\dots,f_n\}$, $f_i: \mathbf{R} \rightarrow \mathbf{R}$, where $f_i(x)=k_ix+b_i$ and $k_i,b_i \in \mathbf{R}$. We need to maintain the following operations:

-   $\operatorname{QueryMax}(l,r)$: given $l$ and $r$, return $\max_{i=l}^r{f_i(0)}$.
-   $\operatorname{TranslateLeft}(l,r,\delta)$: given $l$, $r$ and $\delta$, for all $i\in[l,r]$ perform $f_i(x) \leftarrow f_i(x+\delta)$; this operation is equivalent to $b_i\leftarrow b_i+k_i\delta$. Here $\delta > 0$.

For convenience, we assume that all functions are pairwise distinct.

Translating the linear functions of an interval to the left is essentially $b_i \leftarrow k_i\cdot \delta$, i.e. the constant term $b_i$ is increased by the slope $k_i$ times the horizontal translation $\delta$; this operation is equivalent to the "range addition weighted by position-dependent coefficients" encountered in many data structure problems: for every index $i$ in the interval $[l, r]$, add to its value a fixed number $\delta$ times a coefficient $k_i$ specific to that position. So, essentially, translating linear functions over an interval is the so-called range addition weighted by position-dependent coefficients.

To show the unique binary divide-and-conquer tree structure of the KTT, we will start directly from interval translation.

## Kinetic Data Structures

Kinetic Data Structures are abbreviated KDS. KDS are used to maintain properties of a system of geometric objects during continuous motion.

### Event queue

We assume that every point has a known motion plan, which provides complete or partial information about its motion; for example, the curve or line formed by the function $f_i(x)$ describes the trajectory of the moving point $i$ well. The motion plan may change at any time, due to collisions or interaction with the environment; we call the cause of a change of the motion plan an event. The event queue produces the events in chronological order.

A key aspect of KDS is that the events must be easy to maintain, i.e. the event types in the event queue correspond to possible combinatorial changes involving a constant and usually small number of objects. For example, in the maintenance for this problem, one event type we use is "the order of the functions $f_i(0)$ and $f_{j}(0)$ changes".

The event queue can be maintained implicitly.

### Certificates

These events should be equivalent to guarantees given by the intersection of a series of low-degree algebraic conditions, each involving a finite number of objects. We call these conditions the certificates of the KDS. For example $[f_i(0) > f_j(0)]$.

## Kinetic Tournament Tree

### Overview

The Kinetic Tournament Tree (KTT for short) belongs to the Kinetic Data Structures; it first appeared in 1999 in [Data Structures for Mobile Data](https://www.sciencedirect.com/science/article/pii/S0196677498909889) and is used to maintain continuously changing data. More generally, every structure adopting the following kinetization strategy can be called a Kinetic Tournament:

-   Generate correctness certificates for the key operations of a static algorithm (e.g. comparisons), associate each certificate with a global event queue, and record the time at which the certificate may fail.
-   When some certificate fails, we can efficiently update the algorithm's output and maintain the set of certificates.

In the competitive programming community it became popular through the 2020 Chinese national training team paper "[浅谈函数最值的动态维护](https://github.com/OI-wiki/libs/blob/master/%E9%9B%86%E8%AE%AD%E9%98%9F%E5%8E%86%E5%B9%B4%E8%AE%BA%E6%96%87/IOI2020%E4%B8%AD%E5%9B%BD%E5%9B%BD%E5%AE%B6%E5%80%99%E9%80%89%E9%98%9F%E8%AE%BA%E6%96%87%E9%9B%86%20%E9%9D%9E%E6%AD%A3%E5%BC%8F%E7%89%88.pdf)" (On the dynamic maintenance of function extrema). The academic KTT and the competitive programming KTT differ in application area and implementation, so we present the KTT optimized for competitive programming.

### Basic structure

First consider designing a data structure similar to a segment tree for maintaining a static maximum. Build the structure of a segment tree; each internal node has as its value the larger of the values of its two children. After $O(n)$ comparisons, the value of the root is the global maximum. Now the values start to change. As long as the KTT can detect every change of the source of the maximum at a tree node, we can maintain the global maximum.

To let the KTT detect every change of the source of the maximum in the tree, for a tree node $x$ and the functions $f_L$ and $f_R$ provided by its left and right children, we define the certificate as "the order of $f_L$ and $f_R$ remains unchanged". When a certificate fails, we need to walk along the tree path to the node whose certificate failed and update its information. To maintain the time at which each certificate fails, we observe that the failure time is exactly the moment when the two functions have equal value, so the problem becomes finding the $x$-coordinate of the intersection of two linear functions, which can be solved in $O(1)$.

For every tree node we maintain the function attaining the maximum at $0$, the failure time of the current certificate and the earliest certificate failure time within the whole subtree; then, for every node, at the moment its certificate fails we can locate it and update its information. This information records the data of the functions themselves. Next we consider maintaining the interval translation operation: since translations simply accumulate, we can handle them with lazy tags.

We define the lazy tag $\Delta_v$ to mean that the functions at all other nodes in the subtree of $v$ should be translated to the left by $\Delta_v$ units. Now, for a tree node $v$, a new operation translates all functions in its subtree to the left by $\delta$, i.e. $f(x)\leftarrow f(x+\delta)$. We need to update the lazy tag: $\Delta_v\leftarrow \Delta_v + \delta$, i.e. accumulate the offset for all other nodes in the subtree. At the same time, translating to the left also changes the function values at $0$. We observe that if the failure $x$-coordinate of a certificate is $t$, after the translation it becomes $t-\delta$; if $t-\delta$ crosses the point $0$, the certificate has failed, and we need to recurse downward to find the node holding this certificate, update it, and propagate the new information up to the root. This procedure can be done together with the update.

Thus we obtain a simple implementation.

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/ds/code/ktt/ktt_1.cpp:core"
    ```

### Complexity analysis

Proving the time complexity of the KTT requires potential analysis.

Let $d(x)$ be the depth of node $x$ in the segment tree, with the root at depth $1$. Define the potential of node $x$ in the segment tree as:

$$
\alpha(x) = \begin{cases}
d(x) & \text{if the lower slope function has larger value}  \\
0    & \text{otherwise}\\
\end{cases}
$$

That is, if among the two functions compared at $x$ the one with the smaller slope has the larger value at $0$, the potential of the current node is $d(x)$, otherwise $0$.

Define the potential of the whole KTT as the sum of the potentials of all nodes:

$$
\Phi = \sum_x \alpha(x)
$$

Consider an update of node $x$ and its parent $p$ with actual cost $c=1$, with potentials $\Phi$ and $\Phi'$ before and after the update. We compute the amortized cost of updating node $x$. Since node $x$ is updated, its potential at this moment must drop from $d(x)$ to $0$. For $p$, in the worst case its potential may rise from $0$ to $d(p)$:

$$
\begin{aligned}
\hat{c} &= 1 + \Phi' - \Phi\\
    &= 1 + (\alpha'(p) + \alpha'(x)) - (\alpha(p) + \alpha(x))\\
    &= 1 + (\alpha'(p) - \alpha(p)) + (\alpha'(x) - \alpha(x))\\
    &\leq 1 + d(p) - d(x)\\
    &= 0
\end{aligned}
$$

Summing the actual costs, with initial potential $\Phi_s$ and final potential $\Phi_t$:

$$
\begin{aligned}
\sum c  &= \sum \hat{c} + \Phi_{s} - \Phi_{t}\\
    &\leq \Phi_{s} - \Phi_{t}\\
    &=O(n\log n)
\end{aligned}
$$

This is the number of updates the KTT performs to process all certificate failures when only global updates exist.

Additionally, consider the effect of interval translation on the potential. For one interval translation, the nodes to consider are those whose subtree contains some but not all nodes on which the translation is performed. These are exactly the nodes we pass through in the tree while performing the update; there are at most $O(\log n)$ of them, and in the worst case the potential of each rises by $d(x)\le \log n$, so each operation raises the potential by $O(\log^2 n)$.

To maintain interval translations, the certificate update operation is performed $O(n\log n + m\log^2 n)$ times. Each certificate update requires walking along the tree path to the node with the failed certificate, which costs $O(\log n)$. Hence the total time complexity is $O(n\log^2 n+ m\log^3 n)$.

The merit of this method is that it already reaches the lower bound $O(\lambda_{s}(n)\log^2 n)$ of the problem's time complexity. $\lambda_{s}(n)$ denotes the maximum length of an (n, s) Davenport–Schinzel sequence; linear functions correspond to $s=1$ with $\lambda_1(n)=n$. This belongs to computational geometry and is not elaborated here.

### Higher-degree case

What if we maintain not linear functions but polynomials or even more complex functions? Two complex functions may have several intersection points. Given a sequence of continuous, totally defined univariate functions $F=\{f_1,\dots,f_n\}$, $f_i: \mathbf{R} \rightarrow \mathbf{R}$, where the graphs of every pair of functions intersect in at most $s$ points. Representatively, the set of degree-$s$ polynomials satisfies this requirement.

For the same problem we use potential analysis.

$d(x)$ is the depth of node $x$ in the segment tree, with the root at depth $1$. Define $I(x)$ as the number of intersection points after the point $0$ of the two functions compared at node $x$. Define the potential of node $x$ in the segment tree as:

$$
\alpha(x)=d(x)^{\log_2(s+1)}I(x)
$$

Define the potential of the whole KTT as the sum of the potentials of all nodes:

$$
\Phi = \sum_x \alpha(x)
$$

Consider an update of node $x$ and its parent $p$ with actual cost $c=1$, with potentials $\Phi$ and $\Phi'$ before and after the update. We compute the amortized cost of updating node $x$. Since node $x$ is updated, its potential at this moment must drop from $d(x)^{\log_2(s+1)}I(x)$ to $d(x)^{\log_2(s+1)}(I(x)-1)$. For $p$, in the worst case its potential may rise from $0$ to $d(p)^{\log_2(s+1)}$:

$$
\begin{aligned}
        \hat{c} &= 1 + \Phi' - \Phi\\
                &= 1 + (\alpha'(x) - \alpha(x)) + (\alpha'(p) - \alpha(p))\\
                &\leq 1 - d(x)^{\log_2{(s+1)}} + s(d(x)-1)^{\log_2{(s+1)}}\\
                &\leq 0
    \end{aligned}
$$

From the third line to the fourth we used the constraint that $d(x)$ is a positive integer.

Summing the actual costs, with initial potential $\Phi_s$ and final potential $\Phi_t$:

$$
\begin{aligned}
    \sum c  &= \sum \hat{c} - \Phi_t + \Phi_s\\
            &\leq \Phi_s - \Phi_t\\
            &= O(ns (\log n)^{\log_2{(s+1)}})
\end{aligned}
$$

We obtain the upper bound $O(ns (\log n)^{1+\log_2{(s+1)}} + ms (\log n)^{2+\log_2{(s+1)}})$ on the complexity.[^ref1]

### Approximate case

Given a sequence of continuous, totally defined univariate functions $F=\{f_1,\dots,f_n\}$, define $\mathfrak U_F(x)$, $\mathfrak L_F(x)$ and $\mathfrak E_F(x)$ as the upper envelope, the lower envelope and the extent respectively:

$$
\begin{aligned}
    \mathfrak U_F(x) & = \max\{f_i(x) \mid f_i \in F\} \\
    \mathfrak L_F(x) & = \min\{f_i(x) \mid f_i \in F\} \\
    \mathfrak E_F(x) & = \mathfrak U_F(x) - \mathfrak L_F(x)
\end{aligned}
$$

If we only require the program to return $\tilde{\mathfrak U}_F(x)$ satisfying

$$
\mathfrak U_F(x) \geq \tilde{\mathfrak U}_F(x) \geq \mathfrak U_F(x) - \epsilon \mathfrak E_F(x)
$$

then in the complex case we can achieve $O((1/\epsilon^2)n\log^3 n)$, independent of the polynomial degree, and we may allow the functions to be translated over intervals both to the left and to the right at the same time.

## References and notes

[^ref1]: Note that this only gives an upper bound; the lower bound of the complexity should be $O(\lambda_{s}(n)\log n)$. The author conjectures that the potential analysis here should be constructed with reference to the closed-form expression of $\lambda_{s}(n)$ for Davenport–Schinzel sequences in order to obtain a tighter upper bound.

-   P. K. Agarwal, S. Har-Peled, and K. R. Varadarajan. Approximating extent measures of points. J. ACM, 51(4):606–635, July 2004.
-   J. Basch, L. J. Guibas, and J. Hershberger. Data structures for mobile data. Journal of Algorithms, 31(1):1–28, 1999.
-   G. Alexandron, H. Kaplan, and M. Sharir. Kinetic and dynamic data structures for convex hulls and upper envelopes. Computational Geometry, 36(2):144–158, 2007.
