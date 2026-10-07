---
title: Slope optimization
---

## Introductory example

???+ note "[\"HNOI2008\" Toy packing](https://loj.ac/problem/10188)"
    There are $n$ toys in a row, the $i$-th toy has value $c_i$. The $n$ toys have to be split into several segments. The cost of a segment $[l,r]$ is $(r-l+\sum_{i=l}^r c_i-L)^2$, where $L$ is a constant. Find the minimum total cost of a split.
    
    $1\le n\le 5\times 10^4, 1\le L, c_i\le 10^7$.

### Naive DP solution

Let $f_i$ be the minimum cost of splitting the first $i$ items into several segments.

State transition equation: $f_i=\min_{j<i}\{f_j+(i-(j+1)+pre_i-pre_j-L)^2\}=\min_{j<i}\{f_j+(pre_i-pre_j+i-j-1-L)^2\}$.

Here $pre_i$ is the sum of the first $i$ numbers, i.e. $\sum_{j=1}^i c_j$.

The time complexity of this approach is $O(n^2)$, which is not enough for this problem.

### Optimization

Let us simplify the state transition equation above: let $s_i=pre_i+i,L'=L+1$; then $f_i=\min_{j<i}\{f_j+(s_i-s_j-L')^2\}$.

Moving the terms independent of $j$ outside, we get

$$
f_i - (s_i-L')^2=\min_{j<i}\{f_j+s_j^2 + 2s_j(L'-s_i) \} 
$$

Consider the slope-intercept form of a line, $y=kx+b$, and rearrange it as $b=y-kx$. We express the information depending on $j$ as $y$, the information depending on both $i$ and $j$ as $kx$, and the quantity to be minimized (the information depending on $i$) as $b$, i.e. the intercept. Concretely, let

$$
\begin{aligned}
x_j&=s_j\\
y_j&=f_j+s_j^2\\
k_i&=-2(L'-s_i)\\
b_i&=f_i-(s_i-L')^2\\
\end{aligned}
$$

Then the transition equation is written as $b_i = \min_{j<i}\{ y_j-k_ix_j \}$. Viewing $(x_j,y_j)$ as points in the plane, $k_i$ is the slope of a line and $b_i$ is the intercept of the line with slope $k_i$ passing through $(x_j,y_j)$. The problem becomes: choose a suitable $j$ ($1\le j<i$) that minimizes the intercept of the line.

![slope\_optimization](../images/optimization.svg)

As in the figure, we translate the line with slope $k_i$ upwards from below until some point $(x_p,y_p)$ lies on it; then $b_i=y_p-k_ix_p$ and $b_i$ attains its minimum. After computing $f_i$, we add the point $(x_i,y_i)$ to the point set as a new DP decision. So how do we maintain the point set?

It is easy to see that a point at which $b_i$ can attain its minimum must lie on the lower convex hull. Therefore, when looking for $p$ we do not need to enumerate all $i-1$ points, only the points on the convex hull. Moreover, in this problem $k_i$ increases as $i$ increases, so we can maintain the convex hull with a monotonic queue.

Concretely, let $K(a,b)$ denote the slope of the line through $(x_a,y_a)$ and $(x_b,y_b)$. Consider the queue $q_l,q_{l+1},\ldots,q_r$ that maintains the points of the lower convex hull. That is, for $l<i<r$ we always have $K(q_{i-1},q_i) < K(q_i,q_{i+1})$.

We maintain a pointer $e$ to compute the minimum of $b_i$. We need to find an $e$ with $K(q_{e-1},q_e)\le k_i< K(q_e,q_{e+1})$ (the cases $e=l$ and $e=r$ need special handling); then $p=q_e$, i.e. $q_e$ is the optimal decision for $i$. Since $k_i$ is monotonically increasing, the number of moves of $e$ is amortized $O(1)$.

When inserting a point $(x_i,y_i)$, we check whether $K(q_{r-1},q_r)<K(q_r,i)$; if the inequality does not hold, we pop $q_r$, until it is satisfied. Then we push $i$ to the back of $q$.

In this way the complexity of the DP is optimized to $O(n)$.

To summarize the algorithm for the slope optimization template problem above:

1.  Push the initial state into the queue.
2.  Each time, use a line $f(i)$ associated with $i$ to "cut" the maintained convex hull, find the optimal decision, and update $dp_i$.
3.  Add the state $dp_i$. If a state (i.e. a point on the convex hull) is no longer on the convex hull after $dp_i$ is added, it has to be removed before adding $dp_i$.

Next we present more advanced applications of slope optimization, combining it with binary search/divide and conquer/data structures in order to maintain DP equations with worse properties (lacking some monotonicity properties).

## Optimizing DP with binary search/CDQ/balanced trees

When looking for the optimal decision at point $i$, we use a line $f(i)$ associated with $i$ to cut the convex hull we maintain. The point that is hit is the optimal decision.

In the example above, the slope of the line changes monotonically with $i$, but in some problems the slope is not monotonic. Then we have to maintain every node of the convex hull and cut the hull with the current line each time. This can be done with binary search, because the slopes between adjacent points of the convex hull are monotonic.

???+ note "Toy packing, modified"
    There are $n$ toys in a row, the $i$-th toy has value $c_i$. The $n$ toys have to be split into several segments. The cost of a segment $[l,r]$ is $(r-l+\sum_{i=l}^r c_i-L)^2$, where $L$ is a constant. Find the minimum total cost of a split.
    
    $1\le n\le 5\times 10^4,1\le L\le 10^7,-10^7\le c_i\le 10^7$.

The only difference from the "Toy packing" problem is that the values of the toys can be negative. Continuing the previous idea, let $f_i$ be the minimum cost of splitting the first $i$ items into several segments.

State transition equation: $f_i=\min_{j<i}\{f_j+(pre_i-pre_j+i-j-1-L)^2\}$.

Here $pre_i = \sum_{j=1}^i c_j$.

Applying the same transformation to the equation gives

$$
f_i - (s_i-L')^2=\min_{j<i}\{f_j+s_j^2 + 2s_j(L'-s_i) \} 
$$

However, now two conditions no longer hold:

1.  the slope of the line is no longer monotonic;
2.  the x-coordinates of the decision points being added are no longer monotonic.

We still consider maintaining the convex hull.

When looking for the optimal decision point, i.e. when cutting the hull with the line, we replace taking the front of the monotonic queue with: binary search on the hull. We binary search for the edge of the hull whose slope is closest to the slope of the line, which gives the optimal decision.

When adding a decision point, i.e. adding a point to the hull, we have two ways of maintaining it.

The first way is to maintain the hull directly with a balanced tree. Then the binary search for the decision point becomes a binary search on the balanced tree, and inserting a decision point becomes inserting a node into the balanced tree and deleting several points that are kicked out of the hull. This approach is conceptually simple but tedious to implement.

Below we present an approach based on [CDQ divide and conquer](../../misc/cdq-divide.md).

Let $\text{CDQ}(l,r)$ denote computing $f_i,i\in [l,r]$. Consider $\text{CDQ}(1,n)$:

-   We first call $\text{CDQ}(1,mid)$ to compute $f_i,i\in[1,mid]$. Then we build the convex hull of the decision points in $[1,mid]$ and use it to update $f_i,i\in [mid+1,n]$. Now the set of decision points is fixed; unlike before, we do not add decision points while computing DP values, so we can first sort the $f_i$ with $i \in [mid+1,n]$ by the slope $k_i$ of their lines and then compute the DP values with a monotonic queue. Of course, the DP values can also be computed by binary search on the static hull.

-   For every point in $[mid+1,n]$ whose optimal decision lies in $[1,mid]$, this step sets its optimal answer. After this step, all points in $[1,mid]$ have played their full role, and whether or not they are in the hull no longer affects later updates. Therefore we can simply discard the decision points of this interval and solve the remaining problem of the right interval with $\text{CDQ}(mid+1,n)$.

The time complexity is $O(n\log^2 n)$.

Comparing "Toy packing" and "Toy packing, modified", we can draw the following two conclusions:

-   Binary search/CDQ/balanced trees etc. can optimize the computation of a DP equation and reduce the complexity to some extent, but they cannot change the equation itself.
-   The properties of a DP equation depend on the characteristics of the data, but the DP equation itself depends on the mathematical model of the problem.

## Summary

Slope optimization of DP has to be applied flexibly; its essence is to transform an optimization problem into a problem about the minimum/maximum intercept in the plane related to a convex hull. For equations with worse properties, data structures are sometimes needed to help, and that has to be decided problem by problem.

## Exercises

-   ["SDOI2016" Expedition](https://loj.ac/problem/2035)
-   ["ZJOI2007" Warehouse construction](https://loj.ac/problem/10189)
-   ["APIO2010" Commando](https://loj.ac/problem/10190)
-   ["JSOI2011" Lemon](https://www.luogu.com.cn/problem/P5504)
-   ["Codeforces 311B" Cats Transport](http://codeforces.com/problemset/problem/311/B)
-   ["NOI2007" Currency exchange](https://loj.ac/problem/2353)
-   ["NOI2019" Way home](https://loj.ac/problem/3156)
-   ["NOI2016" The king drinks water](https://uoj.ac/problem/223)
-   ["NOI2014" Buying tickets](https://uoj.ac/problem/7)
