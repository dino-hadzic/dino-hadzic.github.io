---
title: CDQ divide and conquer
---

This page introduces CDQ divide and conquer.

## Introduction

CDQ divide and conquer is an idea rather than a concrete algorithm, similar to [dynamic programming](../dp/index.md). Nowadays this idea has been extended very widely, and by principle and style of implementation it is roughly divided into three categories:

-   solving problems about pairs of points;
-   optimization and transitions of 1D dynamic programming;
-   turning some dynamic problems into static ones by CDQ divide and conquer.

The idea of CDQ divide and conquer was first organized and summarized, while still in high school, by Chen Danqi (陈丹琦), an IOI 2008 gold medalist, and it is named after her.[^ref1]

## Solving problems about pairs of points

Most problems of this kind look like "given a sequence of length $n$, count the pairs of points $(i,j)$ with certain properties" or "given a sequence of length $n$, find a pair of points $(i,j)$ that maximizes the value of some function".

The algorithm by which CDQ divide and conquer solves such problems is as follows:

1.  find the midpoint $mid$ of the sequence;

2.  divide all pairs of points $(i,j)$ into 3 categories:

    1.  pairs with $1 \leq i \leq mid,1 \leq j \leq mid$;
    2.  pairs with $1  \leq i \leq mid ,mid+1 \leq j \leq n$;
    3.  pairs with $mid+1 \leq  i \leq n,mid+1 \leq j \leq n$.

3.  split the sequence $(1,n)$ into two sequences $(1,mid)$ and $(mid+1,n)$. Now the pairs of the first and the third category both lie inside these two sequences;

4.  handle these two categories of pairs recursively;

5.  find a way to handle the pairs of the second category.

As we can see, the idea of CDQ divide and conquer is to keep distributing the pairs of points recursively to the left and the right interval.

In practice we usually use a function `solve(l,r)` that handles the pairs with $l \leq i \leq r,l \leq j \leq r$. The recursive part of the algorithm above is implemented by `solve(l,mid)` and `solve(mid+1,r)`. For the remaining pairs of the second category an additional algorithm has to be designed.

### Example problems

???+ example "[三维偏序 (3D Partial Order)](https://www.luogu.com.cn/problem/P3810)"
    Given a sequence in which every point has three attributes $a_i,b_i,c_i$, find how many pairs of points $(i,j)$ in this sequence satisfy $a_j \leq a_i$ and $b_j \leq b_i$ and $c_j \leq c_i$ and $j \ne i$.

??? note "Solution idea"
    The 3D partial order is the classic problem for CDQ divide and conquer.
    
    The problem asks us to count pairs of points in a sequence, so let us try CDQ divide and conquer.
    
    First sort the sequence by $a$.
    
    Suppose we have already written `solve(l,r)` and have handled `solve(l,mid)` and `solve(mid+1,r)` by recursion. What we have to do now is to count how many pairs of points $(i,j)$ with $l \leq i \leq mid$, $mid+1 \leq j \leq r$ also satisfy the constraints $a_{i} \leq a_{j}$, $b_{i} \leq b_{j}$, $c_{i} \leq c_{j}$.
    
    After a moment of thought we notice that the constraint $a_{i} \leq a_{j}$ is no longer useful: since $i$ is smaller than $mid$ and $j$ is larger than $mid$, $i$ is certainly smaller than $j$; and as the sequence has already been sorted by $a$, we necessarily have $a_{i} \leq a_{j}$. Two constraints remain: $b_{i} \leq b_{j}$ and $c_{i} \leq c_{j}$. Based on them we can enumerate $j$ and find how many $i$ satisfy the conditions.
    
    To make the enumeration convenient, we sort all points in $(l,mid)$ and $(mid+1,r)$ by the value of $b$ in increasing order. Then we enumerate every $j$ in turn and insert all points $i$ with $b_{i} \leq b_{j}$ into some data structure (here we choose a [Fenwick tree](../ds/fenwick.md)). Now we only have to query how many points in the Fenwick tree have a $c$ value less than or equal to $c_{j}$, and we have found how many $i$ can be validly matched with this point $j$.
    
    When we insert a point whose $c$ value equals $x$, we add one at position $x$ of the Fenwick tree, and querying how many points in the Fenwick tree are smaller than $x$ is actually computing a [prefix sum](../basic/prefix-sum.md); as long as we have [discretized](../misc/discrete.md) all $c$ values beforehand, the complexity is right.
    
    For every $j$ we have to insert all points $i$ with $b_{i} \leq b_{j}$ into the Fenwick tree. Since all $i$ and $j$ have already been sorted by $b$ beforehand, it suffices to insert the points into the Fenwick tree with the two pointers technique, and the number of insertions into the Fenwick tree drops from $O(n^2)$ to $O(n)$.
    
    With this algorithm we have processed the information about the pairs of the second category in $O(n\log n)$ time. The time complexity of the algorithm is then $T(n)=T(\lfloor \frac{n}{2} \rfloor)+T(\lceil \frac{n}{2} \rceil)+O(n\log n)=O(n\log^2n)$.

??? note "Example code"
    ```cpp
    --8<-- "docs/misc/code/cdq-divide/cdq-divide_1.cpp"
    ```

???+ example "[CQOI2011 动态逆序对 (Dynamic Inversions)](https://www.luogu.com.cn/problem/P3157)"
    For a sequence $a$, its number of inversions is defined as the number of elements of the set $\{(i,j)| i < j \wedge a_i > a_j \}$.
    
    Given a permutation of $1\sim n$, $m$ elements are deleted one by one in some order. Your task is to count the number of inversions of the whole sequence before every deletion.

??? note "Example code"
    ```cpp
    --8<-- "docs/misc/code/cdq-divide/cdq-divide_2.cpp"
    ```

## CDQ divide and conquer optimization of 1D/1D dynamic programming transitions

Related content: [CDQ divide and conquer optimization of DP](../dp/opt/dp-opt.md#cdq-divide-and-conquer-optimization-of-dp)

1D/1D dynamic programming refers to a specific class of DP problems whose characteristic is that the DP array is one-dimensional and the transition is $O(n)$. If the conditions are good, their time complexity can sometimes be reduced from $O(n^2)$ to $O(n\log^2n)$ by CDQ divide and conquer.

For example, given a sequence in which every element has two attributes $a$, $b$, we want to compute the value of a DP expression whose transition equation is as follows:

$dp_{i}=1+ \max_{j=1}^{i-1}dp_{j}[a_{j} < a_{i}][b_{j} < b_{i}]$

This is the DP equation of a two-dimensional longest increasing subsequence, i.e. only points $j$ with $j < i,a_{j} < a_{i},b_{j} < b_{i}$ can update the DP value of point $i$.

A direct transition is obviously $O(n^2)$. What follows is an explanation of how to optimize the transition process with CDQ divide and conquer.

We notice that the transition relation from $dp_{j}$ to $dp_{i}$ is also a relation between pairs of points, so we handle it in a way similar to how CDQ divide and conquer handles relations between pairs of points.

This transition process is relatively formulaic. Suppose the interval currently being processed is $(l,r)$; the algorithm goes roughly as follows:

1.  if $l=r$, the $\max$ part of the value $dp_{r}$ has already been computed, so we simply set $dp_{r} \gets dp_{r} + 1$ and return;
2.  call `solve(l,mid)` recursively;
3.  handle all transition relations with $l \leq j \leq mid$, $mid+1 \leq i \leq r$;
4.  call `solve(mid+1,r)` recursively.

The third step is done almost the same way as CDQ divide and conquer for the 3D partial order. When handling the transition relations with $l \leq j \leq mid$, $mid+1 \leq i \leq r$, we find that we no longer need to care about the constraint $j < i$. Therefore we again first sort all points $i$ and $j$ by the value of $a$, then insert the points $j$ into a Fenwick tree with the two pointers technique, and finally query the prefix maximum to update $dp_{i}$.

### Proof of correctness of the transition process

The biggest difference between this way of writing CDQ and the one for handling relations between pairs of points is the part that handles the pairs with $l \leq j \leq mid$, $mid+1 \leq i \leq r$. In the CDQ for relations between pairs of points this part can be placed anywhere. However, when optimizing DP with CDQ divide and conquer, this step must be sandwiched between $solve(l,mid)$ and $solve(mid+1,r)$. The reason is that DP transitions are **ordered**; they must satisfy two conditions, otherwise they are wrong:

1.  all values $dp_{j}$ used to compute $dp_{i}$ must already be fully computed; there must be no "half-finished product";

2.  all values $dp_{j}$ used to compute $dp_{i}$ must update $dp_{i}$; there must be no value $dp_{j}$ that has not updated it.

These two conditions are quite easy to satisfy in the $O(n^2)$ brute force, but after applying CDQ divide and conquer the order of transitions is obviously scrambled, so it is necessary to examine the correctness of the transitions.

The recursion tree of CDQ divide and conquer is shown below.

![Recursion tree of CDQ divide and conquer](./images/cdq-divide.svg)

If we run the algorithm just described, take point $8$ as an example: its DP value is completed in the 3 functions `solve(1,8)`, `solve(5,8)`, `solve(7,8)`, and the points used to update it those three times are the three disjoint intervals $(1,4)$, $(5,6)$, $(7,7)$; take point $5$ as another example: its DP value is settled in the function `solve(1,4)`, and the interval that updates it is $(1,4)$. Looking carefully, we find that the DP value of a point $i$ is updated $\log$ times, and the intervals that update it are exactly the $\log$ intervals into which $(1,i)$ is split in a segment tree. Therefore we have indeed guaranteed that every valid $j$ has updated point $i$, so condition 2 is satisfied.

Next we analyze the execution flow of our algorithm:

1.  the first function to finish is `solve(1,1)`. At this point we find that the value of $dp_{1}$ has been computed;
2.  the first function to execute the transition process is `solve(1,2)`. At this point we find that the value of $dp_{2}$ has been transitioned;
3.  the second function to finish is `solve(2,2)`. At this point we find that the value of $dp_{2}$ has been computed;
4.  next `solve(1,2)` finishes, and all $dp$ values on the interval $(1,2)$ have been computed;
5.  the next function to execute the transition process is `solve(1,4)`. After this transition we find that the value of $dp_{3}$ has been transitioned;
6.  the next function to finish is `solve(3,3)`. We find that the dp value of $dp_{3}$ has been computed;
7.  the next transition executed is `solve(3,4)`. At this point $dp_{4}$ was transitioned once from $(1,2)$ in `solve(1,4)` and is now transitioned from $(3,3)$ as well, so the value of $dp_{4}$ has also been transitioned;
8.  `solve(4,4)` finishes, the value of $dp_{4}$ is computed;
9.  `solve(3,4)` finishes, the values on $(3,4)$ are computed;
10. `solve(1,4)` finishes, the values on $(1,4)$ are computed.
11. …

By simulating the flow of the functions we notice one thing: every time `solve(l,r)` finishes, all DP values on the interval $(l,r)$ have been computed. Since every time we execute the transition function `solve(l,mid)` has already finished, every transition process we execute is valid, so condition 1 is satisfied.

In the process above we found that if we view the recursion tree of CDQ divide and conquer as a segment tree, then CDQ divide and conquer is the **inorder traversal function** of this segment tree; so we have effectively processed all DP values in order, only the order of transitions has been split up, and therefore the algorithm is correct.

### Example problems

???+ example "[SDOI2011 拦截导弹 (Intercepting Missiles)](https://www.luogu.com.cn/problem/P2487)"
    To defend against missile attacks of an enemy country, a certain country has developed a missile interception system. However, this system has a flaw: although its first shell can reach any height and intercept a missile of any speed, every subsequent shell cannot be higher than the previous one, and the flight speed of the missile it intercepts cannot be greater than that of the previous one either. One day the radar detected incoming enemy missiles. Since the system is still in its trial phase, there is only one set of it, so it may not be possible to intercept all missiles.
    
    If not all missiles can be intercepted, we of course choose the plan that minimizes the country's losses, i.e. the one that intercepts the largest number of missiles. However, there may be several plans that intercept the largest number of missiles; if there are several optimal plans, we pick one of them at random as the final blueprint of the interception operation.
    
    Our spies have already obtained the heights and speeds of all enemy missiles. Your task is to compute, when the decision described above is carried out, the probability that each missile is intercepted.

??? note "Example code"
    ```cpp
    --8<-- "docs/misc/code/cdq-divide/cdq-divide_3.cpp"
    ```

## Turning dynamic problems into static ones

In the first two cases the purpose of CDQ divide and conquer was to halve the sequence and then recursively handle the relations between pairs of points, in order to obtain a good complexity. In this section, however, what is halved is not an ordinary sequence but a sequence in time.

It applies to some data structure problems of the kind "support doing updates xxx and then doing queries xxx". Such problems have two characteristics:

-   if the queries are processed [offline](offline.md), all operations are naturally arranged in a sequence by time;
-   every update is closely related to the queries that come after it, and there are $O(n^2)$ such "update – query" relations in total.

We can use CDQ divide and conquer on this sequence of operations to handle the relations between updates and queries.

Similar to CDQ divide and conquer for relations between pairs of points, suppose the sequence currently being divided is $(l,r)$: we first recursively handle the update – query relations within $(l,mid)$ and $(mid,r)$, and then handle all update – query relations with $l \leq i \leq mid$, $mid+1 \leq j \leq r$, where $i$ is an update and $j$ is a query.

Note that if the individual updates are **independent** of each other, we do not need to care about the time ordering between $l \leq i \leq mid$ and $mid+1 \leq j \leq r$, or between `solve(l,mid)` and `solve(mid+1,r)` (for example in ordinary addition/subtraction problems). But if the updates are not independent (for example assignment operations), what the sequence looks like after an update may depend on the previous sequence. In that case the step that handles all update – query relations crossing mid must be placed between `solve(l,mid)` and `solve(mid+1,r)`. The reason is the same as for the CDQ divide and conquer optimization of 1D/1D dynamic programming: only dividing in inorder guarantees that every update is executed strictly in time order.

### Example problems

???+ example "Rectangle add, rectangle sum"
    Maintain a two-dimensional array, supporting adding a number to a rectangular region and querying the sum of a rectangular region.

??? note "Solution idea"
    For the version of this problem without updates, i.e. "given a two-dimensional array, query the sum of a rectangular region many times", there is a classic solution with a sweep line combined with a segment tree. Concretely, first split every rectangle into two operations, an insertion and a deletion, then split every query into the form of a difference of two-dimensional prefix sums, and finally process everything offline. However, the original problem has updates, so this solution cannot be applied directly.
    
    Let us try to apply CDQ divide and conquer to it. We process all queries and updates offline. These operations form a sequence, and there are $O(N^2)$ pairs of update – query relations. We still follow the general procedure of CDQ divide and conquer: divide all relations into three categories, handle only the update – query relations crossing $mid$ at this level of the recursion, and solve the remaining update – query relations recursively.
    
    We notice that all updates are completed before the queries. Then the original problem is equivalent to "there are some static rectangles in the plane; keep querying the sum of a rectangular region".
    
    Use a sweep line to handle all update – query relations crossing $mid$ in $O(n\log n)$ time; what remains is to recursively divide and conquer the update – query relations on the left and on the right side.
    
    In a CDQ divide and conquer implemented like this, the same query is processed $O(\log n)$ times. But that does not matter, because the updates that contribute to this query each time are pairwise disjoint. The time complexity of the whole procedure is $T(n)=T(\lfloor \frac{n}{2} \rfloor)+T(\lceil \frac{n}{2} \rceil)+ O(n\log n)=O(n\log^2n)$.
    
    Looking at the algorithm above, we find that at the beginning we could only solve the static rectangle add, rectangle sum problem, but after simply applying CDQ divide and conquer we can solve a dynamic rectangle add, rectangle sum problem offline. The essence of turning a dynamic problem into a static one is that CDQ divide and conquer only handles the update and query relations crossing a certain point each time, so we only need to consider the simple problem in which "all queries come after the updates". It is precisely because of this that CDQ divide and conquer is called "a tool for turning dynamic problems into static ones".

???+ example "[\[Ynoi2016\] 镜中的昆虫 (Insects in the Mirror)](https://www.luogu.com.cn/problem/P4690)"
    Maintain a sequence $a_i$ of length $n$ with $m$ operations.
    
    1.  Set the values on the interval $[l,r]$ to $x$;
    2.  Query how many distinct numbers appear on the interval $[l,r]$, i.e. the same number appearing several times counts only once.
    
    Problem in one sentence: range assignment, range color counting.

??? note "Solution idea"
    For every position maintain the position of the first point of the same color to its left, denoted $pre_{i}$; then range color counting is turned into a classic 2D dominance counting problem.
    
    By viewing a contiguous segment of the same color as a single point, it can be proved that the total amount of change of $pre$ is $O(n+m)$, i.e. a single operation causes only $O(1)$ changes of $pre$ values; so we can use CDQ divide and conquer to solve the dynamic point add, rectangle sum problem.
    
    The concrete changes of the array $pre$ can be handled with `std::set`. This technique of maintaining contiguous intervals with a set is also called [old driver tree](./odt.md).

??? note "Example code"
    ```cpp
    --8<-- "docs/misc/code/cdq-divide/cdq-divide_4.cpp"
    ```

???+ example "[\[HNOI2010\] 城市建设 (City Construction)](https://www.luogu.com.cn/problem/P3206)"
    The country PS is a large country with many cities. King Louis racks his brains over the construction of transportation between the cities. Louis can build roads between certain cities, and building a road between different cities requires a different cost.
    
    Louis wants to build the fewest roads so that all cities in the country are connected. However, due to certain factors, the cost of building a road between cities changes over time. Louis keeps receiving news that the construction cost of some road has changed. He wants to know, immediately after receiving each piece of news, the minimum total cost of connecting the cities. Louis has decided to ask you for help with this task.
    
    Problem in one sentence: given a graph, support dynamic changes of edge weights, and after every change of an edge weight output the minimum total cost of the minimum spanning tree of this graph.

??? note "Solution idea"
    In fact there is a solution with segment tree divide and conquer combined with LCT that solves this problem, but this implementation has too large a constant factor and probably needs clever constant optimization to pass this problem, so let us consider solving it with CDQ divide and conquer.
    
    Unlike the problems CDQ divide and conquer usually solves, here, when using CDQ divide and conquer, there is no update – query relation along which to divide, because we cannot separately consider "what contribution changing one edge makes to the minimum spanning tree of the whole graph". The traditional idea of CDQ divide and conquer does not seem to work very well.
    
    From the previous examples we can see that ordinary CDQ divide and conquer has a special connection with segment trees: during CDQ divide and conquer we actually implicitly build a segment tree (because the recursion tree of CDQ divide and conquer is exactly a segment tree). Ordinary CDQ considers the relation between the left and the right child of the segment tree. For this problem, what we need to consider is the relation between a parent and its child; in other words, when we are at the interval `$solve(l,r)$`, if we can find a way to make the size of the graph a quantity related to the length of the interval, we can solve this problem.
    
    So how do we design the algorithm concretely?
    
    Suppose we are constructing the edge set of the minimum spanning tree for the interval $(l,r)$, and we already know the edge set of the minimum spanning tree of its parent. We assign the edges that change within the interval $(l,r)$ the weights $+ \infty$ and $-\infty$ respectively, run Kruskal once for each, and find which edges are in the minimum spanning tree.
    
    For an edge:
    
    -   if all modified edge weights are set to $+\infty$ and it does not appear in the minimum spanning tree, it is proved that it cannot appear in the minimum spanning tree of any query in $(l,r)$. So we only add the tree edges of the minimum spanning tree to the edge set of $(l,r)$;
    -   if all modified edge weights are set to $-\infty$ and it appears in the minimum spanning tree, it is proved that it will certainly appear in the minimum spanning tree over the interval $(l,r)$. In that case we can use a disjoint set union to contract the vertices of these edges and add their weights to the answer.
    
    In this way we have constructed the edge set of the interval $(l,r)$. The minimum spanning tree obtained from these edges is equivalent to the minimum spanning tree of the original graph.
    
    So why is our complexity correct?
    
    First, the modified edges are certainly added to our edge set, and their number is of order $O(len)$.
    
    Next we need to prove that the edge set will not contain too many unmodified edges. We only add the tree edges of the minimum spanning tree with all weights set to $+\infty$, so the number of edges we add does not exceed the number of vertices of the current graph.
    
    Now we only have to prove that the number of vertices of the graph at every level of the recursion is of order $O(len)$, and then the number of edges of the graph is of order $O(len)$ as well.
    
    Proving that the number of vertices is $O(len)$ becomes very simple. The edges we contract every time we recurse downward are the unmodified edges appearing in the $-\infty$ spanning tree; thinking of it the other way around, we have cut all the modified edges appearing in the $-\infty$ spanning tree. Obviously we cut at most $len$ edges, so the whole graph splits into at most $O(len)$ connected components, and thus the number of vertices of the new graph is of order $O(len)$. So we have proved that the graph on which we run Kruskal is of order $O(len)$ every time, and hence the time complexity of every level is $O(n\log n)$.

    The time complexity is $T(n)=T(\lfloor \frac{n}{2} \rfloor)+T(\lceil \frac{n}{2} \rceil)+ O(n\log n)=O(n\log^2n)$.
    
    The implementation may be somewhat difficult. Note that the disjoint set union cannot use path compression, otherwise it would not support rollback. It is also not necessary to actually perform the contraction; it suffices to run Kruskal at every level directly in the disjoint set union of the previous level.

??? note "Example code"
    ```cpp
    --8<-- "docs/misc/code/cdq-divide/cdq-divide_5.cpp"
    ```

## References and notes

[^ref1]: [从《Cash》谈一类分治算法的应用 (On the application of a class of divide and conquer algorithms, starting from the problem "Cash")](https://www.cs.princeton.edu/~danqic/papers/divide-and-conquer.pdf)
