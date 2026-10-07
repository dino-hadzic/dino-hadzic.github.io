---
title: Quadrangle inequality optimization
---

The quadrangle inequality optimization exploits the monotonicity of the decisions in the state transition equation, so it is also often called **DP optimization by decision monotonicity**.

## Basics

Consider the simplest case: we need to solve the following sequence of optimization problems:

$$
f(i) = \min_{1 \leq j \leq i} w(j,i) \qquad \left(1 \leq i \leq n\right) \tag{1}
$$

We assume that the cost function $w(j,i)$ can be computed in $O(1)$ time.

???+ info "Conventions"
    The state transition equation of a dynamic program can often be written as a sequence of optimization problems. Take equation (1) as an example: these problems have a parameter $i$, and both the objective function and the feasible region may depend on $i$. Each problem is, for a given parameter $i$, to choose a feasible solution $j$ that minimizes the objective function. For convenience, in what follows the optimization problem with parameter $i$ is simply called "problem $i$", a feasible solution $j$ of the problem is called "decision $j$", and the value of the objective function at the optimal solution is called "state $f(i)$". Moreover, the smallest optimal decision of problem $i$ is denoted by $\operatorname{opt}(i)$.

In general the total time complexity of these problems is $O(n^2)$, since for problem $i$ we have to consider every possible decision $j$. But when decision monotonicity holds, the decision space can be shrunk effectively and the total complexity optimized.

-   **Decision monotonicity**: for every $i_1 < i_2$ we must have $\operatorname{opt}(i_1) \leq \operatorname{opt}(i_2)$.

??? note "Remark"
    For problem $i$, the set of optimal decisions need not be an interval. Decision monotonicity can in fact be defined on the sets of optimal decisions. For sets $A$ and $B$, define $A \leq B$ if and only if for every $a\in A$ and $b\in B$ we have $\min\{a,b\}\in A$ and $\max\{a,b\}\in B$. This implies the monotonicity of the smallest (largest) optimal decision, which is the definition adopted here. The results stated in this article for the smallest optimal decision hold equally for the largest optimal decision. However, there are situations where the smallest optimal decision of a larger problem is strictly smaller than the largest optimal decision of a smaller problem, i.e. for some $i_1 < i_2$ we may have $\mathop{\mathrm{optmax}}(i_1) > \mathop{\mathrm{optmin}}(i_2)$, so when writing code one must take care to always compute the smallest, or always the largest, optimal decision.
    
    On the other hand, the problems with the same smallest optimal decision form an interval. This interval, as a function of the smallest optimal decision, must be strictly increasing. In other words, if $j_1 = \operatorname{opt}(i_1)$, $j_2 = \operatorname{opt}(i_2)$ and $j_1 < j_2$, then necessarily $i_1 < i_2$. Equivalently, if the intervals of problems for which decisions $j_1 < j_2$ can be the smallest optimal decision are $[l_{j_1},r_{j_1}]$ and $[l_{j_2},r_{j_2}]$ respectively, then necessarily $r_{j_1} < l_{j_2}$.

The most common way to establish decision monotonicity is the quadrangle inequality. In different contexts this property is also called the Monge property (for describing matrices $A_{j,i}$) or submodularity (for describing functions $f([j,i])$ whose argument is an interval).

-   **Quadrangle inequality**: if for all $a\leq b\leq c\leq d$ we have

    $$
    w(a,c)+w(b,d) \leq w(a,d)+w(b,c),
    $$

    we say that the function $w$ satisfies the quadrangle inequality (in short: "crossing is no more than nesting"). If equality always holds, we say that the function $w$ satisfies the **quadrangle equality**.

Unless stated otherwise, below we always assume $a\leq b\leq c\leq d$. The quadrangle inequality gives a sufficient but not necessary condition for decision monotonicity.

???+ note "Theorem 1"
    If $w$ satisfies the quadrangle inequality, then problem (1) has decision monotonicity.

??? note "Proof"
    We prove by contradiction. Suppose that for some $c < d$ we have $a = \operatorname{opt}(d) < \operatorname{opt}(c) = b$. Then $a < b \leq c < d$. By optimality, $w(a,d) \leq w(b,d)$ and $w(b,c) < w(a,c)$, so $w(a,d) - w(b,d) \leq 0 < w(a,c) - w(b,c)$, which contradicts the quadrangle inequality.

The quadrangle inequality can be understood as saying that, on a reasonable domain, the second-order mixed difference $\Delta_i\Delta_jw(j,i)$ of $w$ is non-positive.

Using decision monotonicity, many common algorithms can be optimized to $O(n\log n)$ complexity. These algorithms differ in their range of applicability, implementation difficulty and efficiency, so a suitable algorithm should be chosen according to the situation. This mainly depends on the properties of $w(j,i)$. Unless stated otherwise, in this article we assume that $w(j,i)$ supports **random access**, i.e. $w(j,i)$ can be read or computed in $O(1)$ time. But not in every problem is $w(j,i)$ so easy to compute. Therefore, besides the basic case, this article also discusses methods of optimizing DP by decision monotonicity when $w(j,i)$ has only the following properties:

-   **Sliding access**: $w(j,i)$ can be obtained in $O(1)$ time from $w(j\pm 1,i)$ or $w(j,i\pm 1)$. (Similar to the situation in [Mo's algorithm](../../misc/mo-algo.md).)
-   **Dynamic computation**: computing $w(j,i)$ depends on $\{f(j'):j' < j\}$. This means that $f$ and $w$ can only be computed in order. The interval partition problem without a limit on the number of intervals, described below, belongs to this situation.

These two properties are not mutually exclusive; it is possible that $w(j,i)$ has to be computed dynamically and supports only sliding access.

### Divide and conquer

To solve all states it suffices to find all optimal decisions. To find $\operatorname{opt}(i)$ for all $1 \leq i \leq n$, we first compute $\operatorname{opt}(n/2)$, then compute $\operatorname{opt}(i)$ separately for $1 \leq i < n/2$ and $n/2 < i \leq n$; here we know that $\operatorname{opt}(i)$ in the first half must lie between $1$ and $\operatorname{opt}(n/2)$ (inclusive), and in the second half between $\operatorname{opt}(n/2)$ and $n$ (inclusive). The two subintervals are handled analogously until the optimal decision of every problem has been computed. If the lower and upper bounds of the search are recorded during the recursion, the complexity of the algorithm stays $O(n\log n)$. The recursion tree has $O(\log n)$ levels, and at each level every decision is computed at most twice, so the total number of computations is $O(n\log n)$.

???+ example "Implementation example"
    ```cpp
    --8<-- "docs/dp/code/opt/quadrangle/quadrangle-divide-conquer.cpp:core"
    ```

Besides the basic case with random access, the divide and conquer algorithm can also be applied when $w(j,i)$ supports only sliding access. It suffices to maintain a pointer $(j,i)$ and the corresponding value $w(j,i)$ during the computation and, whenever a new value is needed, to move the pointer to the current position by brute force while updating the function value. The time complexity is still $O(n\log n)$. A more detailed discussion is in the section [Simplified LARSCH algorithm](#simplified-larsch-algorithm) below. However, the divide and conquer algorithm cannot handle the case where $w(j,i)$ has to be computed dynamically, because it cannot compute the smallest optimal decision $\operatorname{opt}(n/2)$ in the middle of the interval before the problems of the left half have been solved.

### Queue with binary search

Note that for every decision $j$, the problems $i$ for which it is the smallest optimal decision must form an interval. We can use a monotonic queue to record the interval of problems solved by each decision seen so far; then the optimal solution of a problem is naturally obtained from the decisions recorded in the queue.

Concretely, the algorithm scans the decisions in order. When it reaches decision $k$, the queue must contain **triples** consisting of every currently possible decision $j$ and the left and right endpoints $l_j$ and $r_j$ of the interval of problems it solves. For the problems in the given interval $[l_j,r_j]$, $j$ must be the smallest optimal decision among the decisions considered so far (i.e. among the decisions in $[1,k]$). At any time the decisions stored in the queue need not be consecutive, but the unsolved problems $[k,n]$ must be the disjoint union of the problem intervals stored in the queue.

To show that, while the queue is being updated, the problems $i$ for which decision $j$ is the smallest optimal decision always form a contiguous interval, we need to slightly strengthen the previous result:

???+ note "Corollary 1"
    Let $\operatorname{opt}_k(i)$ be the smallest optimal decision of problem $i$ when only the decisions in $[1,k]$ are considered. If $w$ satisfies the quadrangle inequality, then for every $i_1 < i_2$ we must have $\operatorname{opt}_k(i_1) \leq \operatorname{opt}_k(i_2)$.

??? note "Proof"
    Let $M$ be a sufficiently large positive real number. The function $w'(j,i) = w(j,i) + M[j > k]$ still satisfies the quadrangle inequality; here $[\cdot]$ is the Iverson bracket. Consider the auxiliary DP with cost function $w'$. In the auxiliary DP, for no problem $i$ can a decision $j > k$ be the smallest optimal decision, i.e. $\operatorname{opt}'(i) = \operatorname{opt}'_k(i) = \operatorname{opt}_k(i)$. Applying Theorem 1 to the auxiliary DP gives the corollary.

The algorithm proceeds as follows:[^cmp-min-opt]

-   Initially the queue is empty. Similar to a monotonic queue, when considering each new decision $j$ we perform a pop and a push.
-   **Pop**: first remove the previous problem $j-1$ from the queue. If the right endpoint of the problem interval solved by the decision at the front of the queue is exactly $j-1$, pop the front; otherwise set the left endpoint of the problem interval of that decision to $j$.
-   **Push**: when pushing decision $j$, first compare it with the decision $j'$ at the back of the queue.
    -   If for problem $l_{j'}$ the decision $j$ being pushed is strictly better than the existing decision $j'$, i.e. $w(j,l_{j'}) < w(j',l_{j'})$, pop decision $j'$ from the back of the queue. Repeat this until the queue is empty or the decision $j'$ at the back is better than $j$ for problem $l_{j'}$.
    -   If the queue is empty, push $(j,j,n)$, i.e. regard decision $j$ as optimal for all unsolved problems.
    -   If the decision $j'$ at the back of the queue is not worse than the decision $j$ being pushed even for problem $r_{j'}$, then if $r_{j'} < n$ push $(j,r_{j'}+1,n)$, meaning that $j$ is the smallest optimal decision for the problems $[r_{j'}+1,n]$; otherwise $j$ need not be pushed, since it is not better than the existing decisions.
    -   The remaining case is that the decision $j'$ at the back of the queue is strictly better than decision $j$ for problem $l_{j'}$ and strictly worse for problem $r_{j'}$. This means there is a problem $i\in(l_{j'},r_{j'}]$ such that the smallest optimal decision of the problems $[l_{j'},i-1]$ is $j'$ and that of the problems $[i,r_{j'}]$ is $j$. So we **binary search** for the smallest $i\in[l_{j'},r_{j'}]$ with $w(j,i) < w(j',i)$, change the right endpoint $r_{j'}$ of the interval at the back of the queue to $i-1$, and push $(j,i,n)$.
-   After processing decision $j$, all decisions up to $j$ have been processed. Then the decision at the front of the queue is the smallest optimal decision of problem $j$, so we can record the corresponding optimal solution.

???+ example "Implementation example"
    ```cpp
    --8<-- "docs/dp/code/opt/quadrangle/quadrangle-monotone-queue.cpp:core"
    ```

As with a monotonic queue, every decision enters the queue at most once and leaves at most once. A pop is $O(1)$ and a push is $O(\log n)$ (a binary search may be needed), so the total time complexity is $O(n\log n)$.

Since the queue-with-binary-search algorithm considers the problems and decisions in order, it can be applied when $w(j,i)$ has to be computed dynamically. This is its advantage over the divide and conquer algorithm. However, since the binary search step relies on random access to $w(j,i)$, it cannot be applied when $w(j,i)$ supports only sliding access.

???+ example "Example 1: [\"POI2011\" Lightning Conductor](https://loj.ac/problem/2157)"
    Given a sequence $a_1,a_2,\cdots,a_n$ of length $n$. For every $1 \leq i \leq n$, find the smallest non-negative integer $f_i$ such that
    
    $$
    \forall j\in\left[1,n\right]:a_j \leq a_i + f_i - \sqrt{|i-j|}.
    $$

??? note "Solution idea"
    Clearly, rearranging the inequality gives the required integer $f_i = \max_{j}\{a_j+\sqrt{|i-j|}-a_i\}$. First consider the case $j \leq i$ (the other case is analogous); we get the state transition equation:
    
    $$
    f_i = -\min_{j\le i}\{-a_j-\sqrt{i-j}+a_i\}.
    $$
    
    From the convexity of $-\sqrt{x}$ it is easy to see (details follow later) that the function $w(j,i) = -a_j-\sqrt{i-j}+a_i$ satisfies the quadrangle inequality, so applying the algorithm above solves the problem in $O(n\log n)$ time.

??? note "Implementation"
    ```cpp
    --8<-- "docs/dp/code/opt/quadrangle/quadrangle_1.cpp"
    ```

### Simplified LARSCH algorithm

Neither of the previous two algorithms can handle the case where $w(j,i)$ has to be computed dynamically and supports only sliding access. In this section we present an algorithm that overcomes both difficulties at once. It is a simplified version of the LARSCH algorithm proposed by Larmore and Schieber in 1991[^larsch], hence the name **simplified LARSCH algorithm**. The original version of the algorithm solves DP with decision monotonicity in $O(n)$ time, but its implementation is complex and is not described here.

We still consider solving by divide and conquer. When solving the problems in the interval $(l,r]$, we assume the following are known:

-   the smallest optimal decisions $\operatorname{opt}(i)$ and the optimal values of the problems $i$ in $[1,l]$, and
-   the smallest optimal decision $\operatorname{opt}_l(r)$ and the optimal value of problem $r$ when only the decisions in $[1,l]$ are considered.

After solving the problems in $(l,r]$ we need to obtain the smallest optimal decisions and the optimal values of the problems in $(l,r]$.

Let $\textit{mid}$ be the midpoint of the interval $(l,r]$. The procedure is as follows:

1.  Scan the decisions $j\in[\operatorname{opt}(l),\operatorname{opt}_l(r)]$ and update the smallest optimal decision and the optimal value of problem $\textit{mid}$.
2.  Recursively solve the problems in the interval $(l,\textit{mid}]$.
3.  Scan the decisions $j\in(l,\textit{mid}]$ and update the smallest optimal decision and the optimal value of problem $r$.
4.  Recursively solve the problems in the interval $(\textit{mid},r]$.

Before starting the recursion on the whole interval $[1,n]$, the problems $i\in\{1,n\}$ must first be updated with decision $j=1$. The algorithm stops when the recursion reaches $l=r$.

???+ example "Implementation example"
    ```cpp
    --8<-- "docs/dp/code/opt/quadrangle/quadrangle-simplified-larsch.cpp:core"
    ```

First we show the correctness of the algorithm. It suffices to check that before each recursive step (i.e. steps 2 and 4) the preconditions stated above hold. By Corollary 1 of the previous section, $\operatorname{opt}(l)=\operatorname{opt}_l(l)\le\operatorname{opt}_l(\textit{mid})\le\operatorname{opt}_l(r)$, so after step 1 $\operatorname{opt}_l(\textit{mid})$ is known, and thus before step 2 the precondition for recursively solving the problems in $(l,\textit{mid}]$ holds. Since $\{\operatorname{opt}(i):i\in[1,l]\}$ was already known and step 2 yields $\{\operatorname{opt}(i):i\in(l,\textit{mid}]\}$, afterwards all $\{\operatorname{opt}(i):i\in[1,\textit{mid}]\}$ are known; also, since $\operatorname{opt}_l(r)$ was already known, after step 3 $\operatorname{opt}_\textit{mid}(r)$ is known as well. Hence before step 4 the precondition for recursively solving the problems in $(\textit{mid},r]$ also holds.

Next we show that the complexity of the algorithm is still $O(n\log n)$. The recursion tree has $O(\log n)$ levels. For each node at the same level of the recursion tree, the decisions scanned are those in $[\operatorname{opt}(l),\operatorname{opt}_l(r)]$ and $(l,\textit{mid}]$. Since $\operatorname{opt}(l)\le\operatorname{opt}_l(r)\le\operatorname{opt}(r)$, at the same level each decision is scanned only $O(1)$ times. Thus the total number of scans at each level of the recursion tree is $O(n)$. If one access or computation of $w(j,i)$ costs $O(1)$, the time complexity of the algorithm is $O(n\log n)$.

In some cases where $w(j,i)$ supports only sliding access, the complexity of this algorithm is still $O(n\log n)$. Then for steps 1 and 3 of the algorithm we separately maintain a pointer $(j,i)$ and the current value $w(j,i)$. Whenever a new value needs to be accessed, we move the pointer $(j,i)$ by brute force from the position of the previous access to the current position, carrying the function value $w(j,i)$ along. It is easy to verify that, when traversing the recursion tree, the total number of such moves is $O(n\log n)$. Hence the time complexity of the algorithm is still $O(n\log n)$.

??? note "Proof of the complexity without random access"
    It suffices to prove that the total number of pointer moves is $O(n\log n)$. Let $A$ and $B$ be the pointers belonging to steps 1 and 3. In fact the following can be guaranteed: before solving the problems in $(l,r]$, pointer $A$ is at position $(\operatorname{opt}(l),l)$ and pointer $B$ at position $(l,l)$; afterwards, pointer $A$ is at position $(\operatorname{opt}(r),r)$ and pointer $B$ at position $(r,r)$.
    
    Construct the following pointer movement rule. In step 1, let pointer $A$ move along the path
    
    $$
    (\operatorname{opt}(l),l)\to(\operatorname{opt}(l),\textit{mid})\to(\operatorname{opt}_l(r),\textit{mid})\to(\operatorname{opt}(l),\textit{mid})\to(\operatorname{opt}(l),l)
    $$
    
    Then pointers $A$ and $B$ are at the prescribed positions before solving the problems in $(l,\textit{mid}]$. In step 2, by the rule, pointer $A$ moves to $(\operatorname{opt}(\textit{mid}),\textit{mid})$ and pointer $B$ to $(\textit{mid},\textit{mid})$. In step 3, let pointer $B$ move along the path
    
    $$
    (\textit{mid},\textit{mid}) \to (l,\textit{mid}) \to (l, r) \to (\textit{mid},r) \to (\textit{mid},\textit{mid})
    $$
    
    Then pointers $A$ and $B$ are at the prescribed positions before solving the problems in $(\textit{mid},r]$. In step 4, by the rule, pointer $A$ moves to $(\operatorname{opt}(r),r)$ and pointer $B$ to $(r,r)$. Both pointers are at the prescribed positions after solving the problems in $(l,r]$. Hence this movement rule satisfies the requirement above. Moreover, it suffices for all computations in steps 1 and 3. Counting the pointer moves under this rule directly, step 1 requires
    
    $$
    2(\operatorname{opt}_l(r) - \operatorname{opt}(l)) + 2(\textit{mid} - l)
    $$
    
    moves, and step 3 requires
    
    $$
    2(\textit{mid}-l)+2(r-\textit{mid}) = 2(r-l)
    $$
    
    moves. Summing these counts over all nodes of the recursion tree and using the fact that at the same level all the $[l,r]$ and all the $[\operatorname{opt}(l),\operatorname{opt}_l(r)]$ overlap at most at their endpoints, we get that the total number of moves is $O(n\log n)$.
    
    Since the movement rule above introduces more intermediate points than the pointers actually pass through during the computation, the actual number of pointer moves does not exceed the estimate for this rule. Hence the actual number of pointer moves is also $O(n\log n)$.

Since this algorithm, before solving the problems in $(l,r]$, already has the optimal solutions $f(i)$ in $[1,l]$ computed, it can also be applied when $w(j,i)$ has to be computed dynamically.

## Interval partition problem

Consider the problem of partitioning an interval into several subintervals. Formally, the given interval $[1,n]$ is partitioned into $[a_1,b_1],\cdots,[a_k,b_k]$, where $a_1=1$, $b_k=n$ and $b_{i}+1=a_{i+1}$ for every $i < k$. The cost of a given partition is $\sum_{i=1}^kw(a_i,b_i)$. The problem asks to minimize this cost. We can write the following 1D1D state transition equation.

$$
f(i) = \min_{1\leq j\leq i} f(j-1)+w(j,i) \qquad (1\leq i\leq n)
$$

Here $f(0)=0$. Note that as soon as $w(j,i)$ satisfies the quadrangle inequality, $f(j-1)+w(j,i)$ necessarily satisfies the quadrangle inequality too, since the first term contains no cross term of $j$ and $i$ and cancels in the mixed difference. However, since the cost function depends on the previous subproblems, this transition can only be computed in order, so the first divide and conquer algorithm described above cannot be applied; usually only the queue-with-binary-search algorithm or the simplified LARSCH algorithm is suitable. The complexity of the algorithm is $O(n\log n)$.

### Case with a bounded number of intervals

The problem above can be strengthened by limiting the number of intervals, i.e. the problem requires the interval to be partitioned into exactly $m$ subintervals. Then the number of subintervals after partitioning has to be added as a dimension of the transition state. The corresponding 2D1D state transition equation is:

$$
f(k,i) = \min_{1\leq j\leq i} f(k-1,j-1)+w(j,i) \qquad (1\leq k\leq m,\ 1\leq i\leq n) \tag{2}
$$

Here $f(0,0)=0$ and $f(0,i)=f(k,0)=\infty$ for all $1\leq k\leq m$ and $1\leq i\leq n$. As before, $f(k-1,j-1)+w(j,i)$ necessarily satisfies the quadrangle inequality. Now the computation of the $k$-th layer no longer depends on the results of that layer, so each layer can be computed with any algorithm from the previous section, with complexity $O(mn\log n)$.

For this problem, there are other optimization algorithms exploiting decision monotonicity. The second optimization idea relies on the following result. This algorithm is very similar to Knuth's optimization, described in detail below.

???+ note "Theorem 2"
    If $w$ satisfies the quadrangle inequality, then for problem (2) we have $\operatorname{opt}(k-1,i) \leq \operatorname{opt}(k,i) \leq \operatorname{opt}(k,i+1)$.

??? note "Proof"
    The second inequality is just the decision monotonicity of the $k$-th layer. The key is the first inequality.
    
    We prove $\operatorname{opt}(k,i) \leq \operatorname{opt}(k+1,i)$. Suppose we have the following two partitions of the interval $[1,i]$ (indexed in reverse order): $[a_{k},d_{k}],\cdots,[a_1,d_1]$ and $[b_{k+1},c_{k+1}],\cdots,[b_1,c_1]$. Here the left endpoint of each interval is the smallest optimal decision of the problem belonging to its right endpoint; likewise, if we look at all possible partitions from right to left, the right endpoint is the smallest optimal decision of the problem belonging to the left endpoint. For example, $d_j$ and $c_j$ are respectively the smallest optimal decisions for the right endpoint of the first interval from the left when partitioning $[a_j,i]$ and $[b_j,i]$ into $j$ parts. By decision monotonicity, if $a_{j-1} > b_{j-1}$, i.e. $d_j > c_j$, then necessarily $a_j > b_j$. Hence, if the claim does not hold, then $a_1 > b_1$. From this, by induction, $a_{k} > b_{k}$, which clearly contradicts the assumption. This proves the claim.
    
    The first inequality can also be proved as follows. Again consider the two partitions from the proof above. If the claim does not hold, then $a_1 > b_1$; but since $a_{k} < b_{k}$, we can find the smallest $j>1$ with $a_j \leq b_j$. Then $a_{j-1} > b_{j-1}$, so $d_j>c_j$. We have found intervals with $a_j \leq b_j \leq c_j < d_j$. Consider the results of recombining these two partitions. The partition $[b_{k+1},c_{k+1}],\cdots,[b_{j+1},c_{j+1}],[b_j,d_j],[a_{j-1},d_{j-1}],\cdots,[a_1,d_1]$ has $(k+1)$ parts, so the assumed optimality gives
    
    $$
    \begin{aligned}
    &w(b_{k+1},c_{k+1})+\cdots+w(b_{j+1},c_{j+1})+w(b_j,c_j)+w(b_{j-1},c_{j-1})+\cdots+w(b_1,c_1) \\
    &\qquad \leq w(b_{k+1},c_{k+1})+\cdots+w(b_{j+1},c_{j+1})+w(b_j,d_j)+w(a_{j-1},d_{j-1})+\cdots+w(a_1,d_1).
    \end{aligned}
    $$
    
    Likewise, the partition $[a_{k},d_{k}],\cdots,[a_{j+1},d_{j+1}],[a_j,c_j],[b_{j-1},c_{j-1}],\cdots,[b_1,c_1]$ has $k$ parts, so
    
    $$
    \begin{aligned}
    &w(a_{k},d_{k})+\cdots+w(a_{j+1},d_{j+1})+w(a_j,d_j)+w(a_{j-1},d_{j-1})+\cdots+w(a_1,d_1) \\
    &\qquad < w(a_{k},d_{k})+\cdots+w(a_{j+1},d_{j+1})+w(a_j,c_j)+w(b_{j-1},c_{j-1})+\cdots+w(b_1,c_1).
    \end{aligned}
    $$
    
    Here the inequality is strict because $a_1 > b_1$, and by assumption $a_1$ is the smallest optimal one among the left endpoints of the last part of all partitions into $k$ parts. Adding the two inequalities gives $w(b_j,c_j) + w(a_j,d_j) < w(b_j,d_j) + w(a_j,c_j)$, contradicting the quadrangle inequality. This proves the claim.

Using this result we can restrict the search range of the decision $j$. In the implementation, we enumerate $k$ in increasing order and $i$ in decreasing order, and brute-force $j$ within the lower and upper bounds determined earlier; this guarantees $O(n(n+m))$ complexity.

??? warning "Note"
    The complexity of this algorithm is not $O(nm)$. A correct complexity analysis must consider the $n\times m$ state matrix. Since for problem $(k,i)$ only the decisions $\operatorname{opt}(k-1,i) \leq j \leq \operatorname{opt}(k,i+1)$ need to be considered, the total number of decisions scanned for the problems on one anti-diagonal (i.e. with fixed $i-k$) is $O(n)$. There are $(n+m)$ such diagonals in total, so the total time complexity is $O(n(n+m))$.

The last optimization method comes from the following observation.

???+ note "Theorem 3"
    If $w$ satisfies the quadrangle inequality, then the optimal value of problem (2), $g(k):=f(k,n)$, is a convex function of $k$.

??? note "Proof"
    We prove $g(k-1) + g(k+1) \ge 2g(k)$. Consider the optimal partitions into $(k-1)$ and $(k+1)$ parts respectively: $[a_1,d_1],\cdots,[a_{k-1},d_{k-1}]$ and $[b_1,c_1],\cdots,[b_{k+1},c_{k+1}]$. Take the smallest $1 \leq j \leq k-1$ with $c_{j+1} \leq d_j$; its existence follows from $c_{k} < n = d_{k-1}$. By minimality, $b_{j+1} > a_j$. Hence $a_j < b_{j+1} \leq c_{j+1} \leq d_j$. Similarly to above, swapping the tails of the two existing partitions gives the following two partitions of the interval:
    
    $$
    \begin{aligned}
    & [a_1,d_1],\cdots,[a_{j-1},d_{j-1}],[a_j,c_{j+1}],[b_{j+2},c_{j+2}],\cdots,[b_{k+1},c_{k+1}], \\
    & [b_1,c_1],\cdots,[b_j,c_j],[b_{j+1},d_j],[a_{j+1},d_{j+1}],\cdots,[a_{k-1},d_{k-1}].
    \end{aligned}
    $$
    
    Both resulting partitions have $k$ parts, so by optimality
    
    $$
    \begin{aligned}
    2g(k) &\le w(a_1,d_1) + \cdots + w(a_{j-1},d_{j-1}) + w(a_j,c_{j+1}) + w(b_{j+2},c_{j+2}) + \cdots + w(b_{k+1},c_{k+1}) \\
    &\quad + w(b_1,c_1) + \cdots + w(b_j,c_j) + w(b_{j+1},d_j) + w(a_{j+1},d_{j+1}) + \cdots + w(a_{k-1},d_{k-1}) \\
    &\le w(a_1,d_1) + \cdots + w(a_{j-1},d_{j-1}) + w(a_j,d_j) + w(a_{j+1},d_{j+1}) + \cdots + w(a_{k-1},d_{k-1}) \\
    &\quad + w(b_1,c_1) + \cdots + w(b_j,c_j) + w(b_{j+1},c_{j+1}) + w(b_{j+2},c_{j+2}) + \cdots + w(b_{k+1},c_{k+1}) \\
    &= g(k-1) + g(k+1).
    \end{aligned}
    $$
    
    The second inequality is exactly the quadrangle inequality. This proves the required convexity.

This result guarantees that the problem can be solved with WQS binary search (known abroad as the Aliens trick). Concretely, consider the parametrized cost function $w_c(j,i):=w(j,i)+c$, solve the problem without a limit on the number of intervals and obtain the optimal value $f_c(n)$. As the real number $c$ increases, the number of intervals in the corresponding optimal solution decreases monotonically, so we can binary search for the parameter $c$ at which the optimal number of intervals is exactly $m$; the optimal value of the original problem is then $f(m,n) = f_c(n)-cm$. The real number $c$ can be understood as the Lagrange multiplier of the constraint on the number of intervals. The implementation of this algorithm has many details; see the page [WQS binary search](./wqs-binary-search.md). The time complexity of this algorithm is $O(n\log n\log C)$, where $C$ is the size of the value range of the parameter $c$.

The three algorithms for the interval partition problem with a bounded number of intervals have different advantages and disadvantages for different input sizes, so a suitable algorithm should be chosen according to the problem.

???+ example "Example 3: [P4767 \[IOI2000\] Post offices, enhanced](https://www.luogu.com.cn/problem/P4767)  [P6246 \[IOI2000\] Post offices, doubly enhanced](https://www.luogu.com.cn/problem/P6246)"
    There are several villages along a highway. The highway is represented by an integer number line, and the position of each village is given by an integer coordinate. No two villages are at the same position. The distance between two positions is the absolute value of the difference of their integer coordinates.
    
    Post offices will be built in some, but not necessarily all, of the villages. The construction sites should be chosen so that the sum of the distances from each village to its nearest post office is as small as possible.
    
    Write a program that, given the positions of the villages and the number of post offices, computes the smallest possible sum of the distances from each village to its nearest post office.

??? note "Solution idea"
    Every village has a nearest post office, so every post office has the villages it covers; it is easy to see that they form an interval.
    
    Partition the $n$ villages into $m$ intervals and place one post office in each interval.

    It is known mathematically that for the interval $[i,j]$ the post office should be built at the $\left\lfloor\dfrac{i+j}2\right\rfloor$-th village. With prefix sums, $w(i,j)$ is easily computed.
    
    The problem reduces to the interval partition problem with a bounded number of intervals. It can be proved that the function $w$ satisfies the quadrangle inequality. It suffices to apply the optimization methods above directly.

??? note "Implementation 1, the second optimization in the text, complexity $O(n(n+m))$"
    ```cpp
    --8<-- "docs/dp/code/opt/quadrangle/quadrangle_2.cpp"
    ```

??? note "Implementation 2, WQS binary search, complexity $O(n\log n\log C)$"
    ```cpp
    --8<-- "docs/dp/code/opt/quadrangle/quadrangle_3.cpp"
    ```

## Interval merging problem

Another class of dynamic programming problems that can be optimized with the quadrangle inequality is the interval merging problem: $n$ intervals $[i,i]$ of length one are merged two at a time until the interval $[1,n]$ is obtained. Each merge of $[j,k]$ and $[k+1,i]$ costs $w(j,i)$. We want the merging scheme of minimum cost. For such problems we have the following 2D1D state transition equation:

$$
f(j,i) = \min_{j \leq k < i} f(j,k) + f(k+1,i) + w(j,i) \qquad (1\le j< i\le n) \tag{3}
$$

Here the initial cost is $f(i,i)=0$. The total complexity of the brute-force algorithm is $O(n^3)$, and when decision monotonicity holds it can be optimized to $O(n^2)$. This algorithm was first proposed by Knuth when solving the optimal binary search tree problem and was further studied and summarized by Yao; abroad it is known as Knuth's optimization or the Knuth–Yao speedup.

Besides the quadrangle inequality, decision monotonicity in the interval merging problem also requires the cost function to be monotone with respect to interval inclusion.

-   **Monotonicity with respect to interval inclusion**: if for all $a \leq b \leq c \leq d$ we have

    $$
    w(b,c) \leq w(a,d),
    $$

    we say that the function $w$ is monotone with respect to the interval inclusion relation.

This is in fact a first-order condition on the cost function: $w(j,i)$ is decreasing in $j$ and increasing in $i$.

???+ note "Lemma 1"
    If $w$ satisfies monotonicity with respect to interval inclusion and the quadrangle inequality, then the state $f(j,i)$ satisfies the quadrangle inequality.

??? note "Proof"
    Let $a \leq b \leq c \leq d$. We prove $f(a,d) + f(b,c) \geq f(a,c) + f(b,d)$ by induction on $d-a$. When $a=b$ or $c=d$, the required claim is an equality. In the general case we distinguish cases according to the position of $d'=\operatorname{opt}(a,d)$.
    
    Case 1: $c \leq d'$ or $d' < b$, i.e. $[b,c]$ is contained in $[a,d']$ or in $[d'+1,d]$.
    
    Without loss of generality let $c \leq d'$; the other case is analogous. Then
    
    $$
    \begin{aligned}
    f(a,d) + f(b,c)
    & = f(a,d') + f(d'+1,d) + w(a,d) + f(b,c) \\
    & \geq f(a,c) + f(b,d') + f(d'+1,d) + w(a,d) \\
    & \geq f(a,c) + f(b,d') + f(d'+1,d) + w(b,d) \\
    & \geq f(a,c) + f(b,d).
    \end{aligned}
    $$
    
    Here the first inequality follows from the induction hypothesis $f(a,c) + f(b,d') \leq f(a,d') + f(b,c)$, the second from monotonicity with respect to interval inclusion $w(b,d) \leq w(a,d)$, and the third from the optimality condition $f(b,d) \leq f(b,d') + f(d'+1,d) + w(b,d)$.
    
    Case 2: $b \leq d' < c$, i.e. $d'$ lies in $[b,c]$. Then we look at the position of $c'=\operatorname{opt}(b,c)$.
    
    Without loss of generality let $c' \leq d'$, i.e. $[b,c']$ is contained in $[a,d']$; the other case is analogous. Then
    
    $$
    \begin{aligned}
    f(a,d) + f(b,c)
    & = f(a,d') + f(d'+1,d) + w(a,d) + f(b,c') + f(c'+1,c) + w(b,c) \\
    & \geq f(a,c') + f(c'+1,c) + w(b,c) + f(b,d') + f(d'+1,d) + w(a,d) \\
    & \geq f(a,c') + f(c'+1,c) + w(a,c) + f(b,d') + f(d'+1,d) + w(b,d) \\
    & \geq f(a,c) + f(b,d).
    \end{aligned}
    $$
    
    Here the first inequality follows from the induction hypothesis $f(a,c') + f(b,d') \leq f(a,d') + f(b,c')$, the second from the quadrangle inequality $w(a,c) + w(b,d) \leq w(a,d) + w(b,c)$, and the third from the optimality conditions for $f(a,c)$ and $f(b,d)$.

???+ note "Theorem 4"
    If $w$ satisfies monotonicity with respect to interval inclusion and the quadrangle inequality, then the smallest optimal decision $\operatorname{opt}(j,i)$ in problem (3) satisfies
    
    $$
    \operatorname{opt}(j,i-1) \leq \operatorname{opt}(j,i) \leq \operatorname{opt}(j+1,i). \qquad (j + 1 < i)
    $$

??? note "Proof"
    Lemma 1 already gives that $f(j,i)$ satisfies the quadrangle inequality, so for fixed $j$ the objective function $f(j,k) + f(k+1,i) + w(j,i)$, as a function of $(k,i)$, satisfies the quadrangle inequality; by Theorem 1, $\operatorname{opt}(j,i-1) \leq \operatorname{opt}(j,i)$. Note that terms not containing both $(k,i)$ do not affect the validity of the quadrangle inequality. Similarly, for fixed $i$ it also satisfies the quadrangle inequality as a function of $(j,k)$, so $\operatorname{opt}(j,i) \leq \operatorname{opt}(j+1,i)$. This proves the claim.

With this result we can again restrict the search range of the decision $k$. Here we enumerate the interval length $i-j+1$ in increasing order, then all intervals $[j,i]$ of the same length, brute-force all $k$ between $\operatorname{opt}(j,i-1)$ and $\operatorname{opt}(j+1,i)$, obtain the optimal value $f(j,i)$ and record the smallest optimal decision $\operatorname{opt}(j,i)$. For all intervals of the same length, the total length of the decision space in this algorithm is $O(n)$, and the number of possible interval lengths is also $O(n)$, so the total complexity of the algorithm is $O(n^2)$.

???+ example "Implementation example"
    ```cpp
    --8<-- "docs/dp/code/opt/quadrangle/quadrangle-knuth-optimization.cpp:core"
    ```

## Classes of functions satisfying the quadrangle inequality

To make it easier to prove that a function satisfies the quadrangle inequality, we have the following properties:

**Property 1**: if the functions $w_1(j,i)$ and $w_2(j,i)$ both satisfy the quadrangle inequality (or monotonicity with respect to interval inclusion), then for all $c_1,c_2\geq 0$ the function $c_1w_1+c_2w_2$ also satisfies the quadrangle inequality (or monotonicity with respect to interval inclusion).

**Property 2**: if there are functions $f(x)$ and $g(x)$ such that $w(j,i) = f(j)-g(i)$, then the function $w$ satisfies the quadrangle equality. If the functions $f$ and $g$ are monotonically increasing, the function $w$ also satisfies monotonicity with respect to interval inclusion.

**Property 3**: let $h(x)$ be a monotonically increasing convex function. If the function $w(j,i)$ satisfies the quadrangle inequality and is monotone with respect to interval inclusion, then the composition $h(w(j,i))$ also satisfies the quadrangle inequality and monotonicity with respect to interval inclusion.

**Property 4**: let $h(x)$ be a convex function. If the function $w(j,i)$ satisfies the quadrangle equality and is monotone with respect to interval inclusion, then the composition $h(w(j,i))$ also satisfies the quadrangle inequality.

First a clarification: the definition of a convex function differs between Chinese textbooks; here a convex function means a function that is convex downwards, i.e. (if differentiable) a function whose first derivative is monotonically increasing.

??? note "Proof"
    The first two properties are easily proved from the definition; we prove the third, and the proof of Property 4 is similar. Since $h(x)$ is monotone, $h(w(j,i))$ clearly preserves monotonicity with respect to interval inclusion. The key is to prove the quadrangle inequality.
    
    For this, consider the second-order mixed difference on $a \leq j \leq b \leq c \leq i \leq d$.
    
    $$
    \begin{aligned}
    \Delta_i\Delta_j h\left(w(j,i)\right)
    &= h\left(w(b,d)\right) - h\left(w(a,c) + \Delta_jw(j,c) + \Delta_iw(a,i)\right) \\
    &\quad + h\left(w(a,c) + \Delta_jw(j,c) + \Delta_iw(a,i)\right) - h\left(w(a,c) + \Delta_jw(j,c)\right) \\
    &\quad - h\left(w(a,c) + \Delta_iw(a,i)\right) + h\left(w(a,c)\right).
    \end{aligned}
    $$
    
    Here, by interval monotonicity, $\Delta_iw(a,i) := w(a,d) - w(a,c) \geq 0$ and $\Delta_jw(j,c) := w(b,c) - w(a,c) \leq 0$. By the convexity of $h(x)$, for $t_1,t_2\geq 0$ we have $h(x + t_1 - t_2) - h(x + t_1) \leq h(x - t_2) - h(x)$, so the sum of the last two lines is necessarily non-positive. Also, by the quadrangle inequality, $w(b,d) \leq w(a,c) + \Delta_jw(j,c) + \Delta_iw(a,i) = w(b,c) + w(a,d) - w(a,c)$, so, since $h(x)$ is monotonically increasing, the difference in the first line is necessarily non-positive too. Hence the total second-order mixed difference is non-positive. This is exactly the quadrangle inequality.
    
    This proof is in fact a discrete version of the following proof with derivatives.
    
    $$
    \frac{\partial^2}{\partial x\partial y}h(w(x,y)) = h''(w(x,y))\frac{\partial }{\partial x}w(x,y)\frac{\partial}{\partial y}w(x,y) + h'(w(x,y))\frac{\partial^2}{\partial x\partial y}w(x,y) \leq 0.
    $$
    
    This clearly holds under the conditions $h' \geq 0$, $h'' \geq 0$, $w_x \leq 0$, $w_y \geq 0$ and $w_{xy} \leq 0$. Here monotonicity with respect to interval inclusion gives the first-order condition on $w$, and the quadrangle inequality the second-order condition.

## Exercises

-   [Codeforces - Ciel and Gondolas](https://codeforces.com/contest/321/problem/E)(Be careful with input/output!)
-   [SPOJ - LARMY](https://www.spoj.com/problems/LARMY/)
-   [Codechef - CHEFAOR](https://www.codechef.com/problems/CHEFAOR)
-   [Hackerrank - Guardians of the Lunatics](https://www.hackerrank.com/contests/ioi-2014-practice-contest-2/challenges/guardians-lunatics-ioi14)
-   [ACM ICPC World Finals 2017 - Money](https://open.kattis.com/problems/money)

## References and footnotes

-   [Quora Answer by Michael Levin](https://www.quora.com/What-is-divide-and-conquer-optimization-in-dynamic-programming)
-   [Video Tutorial by "Sothe" the Algorithm Wolf](https://www.youtube.com/watch?v=wLXEWuDWnzI)
-   [Divide and Conquer DP](https://cp-algorithms.com/dynamic_programming/divide-and-conquer-dp.html)
-   [Knuth's Optimization](https://cp-algorithms.com/dynamic_programming/knuth-optimization.html)
-   [Quadrangle Inequality Properties](https://codeforces.com/blog/entry/86306)
-   [Wang Qinshi, "An analysis of a class of binary search methods" (王钦石《浅析一类二分方法》)](https://github.com/hzwer/shareOI/blob/master/%E5%9F%BA%E7%A1%80%E7%AE%97%E6%B3%95/%E6%B5%85%E6%9E%90%E4%B8%80%E7%B1%BB%E4%BA%8C%E5%88%86%E6%96%B9%E6%B3%95_%E7%8E%8B%E9%92%A6%E7%9F%B3.pdf)
-   [簡易版 LARSCH Algorithm by noshi91](https://noshi91.hatenablog.com/entry/2023/02/18/005856)
-   [Quadrangle inequality and decision monotonicity by b6e0\_ - Luogu blog](https://www.luogu.com.cn/article/h81hh5lk)
-   [A simple version of the LARSCH algorithm for online decision monotonicity by Register\_int - Luogu blog](https://www.luogu.com.cn/article/vqf42hah)

[^cmp-min-opt]: "Worse" and "better" in the description of the algorithm should be understood as a lexicographic comparison in which the function value is compared first and then the decision. In this lexicographic order, "better" means that either the function value is smaller, or the value is equal and the decision is smaller.

[^larsch]: Larmore, Lawrence L., and Baruch Schieber. "On-line dynamic programming with applications to the prediction of RNA secondary structure." Journal of Algorithms 12, no. 3 (1991): 490-515.
