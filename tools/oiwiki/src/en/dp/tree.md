---
title: Tree DP
---

Tree DP is DP performed on a tree. Because of the inherent recursive nature of trees, tree DP is usually carried out recursively.

## Basics

We introduce the general procedure of tree DP with the following problem.

???+ note "Example [Luogu P1352 Party Without the Boss](https://www.luogu.com.cn/problem/P1352)"
    A university has $n$ employees numbered $1 \sim N$. There is a subordination relation among them, i.e. their relations form a tree rooted at the president, where the parent node is the direct superior of the child node. There is an anniversary party; each invited employee adds a certain happiness index $a_i$, but if the direct superior of an employee attends the party, that employee refuses to come under any circumstances. Write a program to determine which employees to invite so that the happiness index is maximized, and output this maximum happiness index.

Let $f(i,0/1)$ denote the optimal solution for the subtree rooted at $i$ (the second dimension being 0 means $i$ does not attend the party, 1 means $i$ attends).

For every state there are two decisions (below, $x$ is always a child of $i$):

-   When the superior does not attend, the subordinates may or may not attend; then $f(i,0) = \sum\max \{f(x,1),f(x,0)\}$;
-   When the superior attends, none of the subordinates attend; then $f(i,1) = \sum{f(x,0)} + a_i$.

We can update the optimal solution of the current node with a DFS, when returning to the previous level.

```cpp
--8<-- "docs/dp/code/tree/tree_1.cpp"
```

Usually the state of a tree DP is the optimal solution for the current node. First the DFS traverses all optimal solutions of the subtrees, then passes them up to the parent of the subtree to transition; the value at the root is the required optimal solution.

### Exercises

-   [HDU 2196 Computer](https://acm.hdu.edu.cn/showproblem.php?pid=2196)

-   [POJ 1463 Strategic game](http://poj.org/problem?id=1463)

-   [\[POI2014\]FAR-FarmCraft](https://www.luogu.com.cn/problem/P3574)

## Tree knapsack

The knapsack problem on a tree is, simply put, the combination of the knapsack problem and tree DP.

???+ note "Example [Luogu P2014 CTSC1997 Course Selection](https://www.luogu.com.cn/problem/P2014)"
    There are $n$ courses; course $i$ is worth $a_i$ credits. Each course has zero or one prerequisite course; a course with a prerequisite can only be taken after its prerequisite has been completed.
    
    A student wants to take $m$ courses. Find the maximum number of credits obtainable.
    
    $n,m \leq 300$

The property that each course has at most one prerequisite is similar to the property that in a rooted tree each node has at most one parent.

Hence we can build a tree based on this property, so that all courses form a forest. For convenience we add a new course worth $0$ credits (numbered $0$) as the prerequisite of all courses without one; this turns the forest into a tree rooted at course $0$.

Let $f(u,i,j)$ denote the maximum credits in the subtree rooted at $u$ when the first $i$ subtrees of $u$ have been traversed and $j$ courses have been chosen.

The transition combines the features of tree DP and [knapsack DP](./knapsack/basic.md): we enumerate each child $v$ of $u$ and at the same time the number of courses chosen in the subtree rooted at $v$, merging the result of the subtree into $u$.

Let $s_x$ be the number of children of node $x$ and $\textit{siz}_x$ the size of the subtree rooted at $x$; the state transition equation is:

$$
f(u,i,j)=\max_{v,k \leq j,k \leq \textit{siz}_v} f(u,i-1,j-k)+f(v,s_v,k)
$$

Pay attention to the constraints in the transition equation above; they ensure that meaningless states are never visited.

The second dimension of $f$ can easily be dropped using a rolling array; note that $j$ must then be enumerated in decreasing order.

It can be proved that the time complexity of this approach is $O(nm)$[^note1].

??? note "Sample code"
    ```cpp
    --8<-- "docs/dp/code/tree/tree_2.cpp"
    ```

### Exercises

-   ["CTSC1997" Course Selection](https://www.luogu.com.cn/problem/P2014)

-   ["JSOI2018" Infiltration](https://loj.ac/problem/2546)

-   ["SDOI2017" Apple Tree](https://loj.ac/problem/2268)

-   ["Codeforces Round 875 Div. 1" Problem D. Mex Tree](https://codeforces.com/contest/1830/problem/D)

## Rerooting DP

Rerooting DP in tree DP is also called the two-pass technique; usually no root is specified, and changing the root affects some values, e.g. the sum of depths of the children or the sum of vertex weights.

Two DFS passes are usually needed: the first DFS preprocesses information such as depths and weight sums, and the second DFS runs the rerooting dynamic programming.

We use some examples to familiarize you with this topic.

???+ note "Example [\[POI2008\]STA-Station](https://www.luogu.com.cn/problem/P3478)"
    Given a tree with $n$ nodes, find a node such that, when the tree is rooted at it, the sum of the depths of all nodes is maximized.

Let $u$ be the current node and $v$ a child of the current node. First let $s_i$ denote the number of nodes in the subtree rooted at $i$; we have $s_u=1+\sum s_v$. Clearly one DFS is needed to compute all $s_i$; this DFS is the preprocessing, giving us the total number of nodes in the subtree of each node.

Consider the state transition; this is where "rerooting" shows up. Let $f_u$ be the sum of depths of all nodes when $u$ is the root.

$f_v\leftarrow f_u$ expresses rerooting, i.e. moving from root $u$ to root $v$. Clearly, during the rerooting transition, taking $v$ or $u$ as the root changes the depths of the nodes in its subtree. Concretely:

-   the depth of every node in the subtree of $v$ decreases by one, so the total depth sum decreases by $s_v$;

-   the depth of every node not in the subtree of $v$ increases by one, so the total depth sum increases by $n-s_v$;

From these two facts we derive the state transition equation $f_v = f_u - s_v + n - s_v=f_u + n - 2 \times s_v$.

So in the second DFS we traverse the whole tree and apply the transition $f_v=f_u + n - 2 \times s_v$, obtaining the depth sum for every node as root. Finally one pass over the depth sums of all roots gives the answer.

??? note "Sample code"
    ```cpp
    --8<-- "docs/dp/code/tree/tree_3.cpp"
    ```

### Exercises

-   [Atcoder Educational DP Contest, Problem V, Subtree](https://atcoder.jp/contests/dp/tasks/dp_v)

-   [Educational Codeforces Round 67, Problem E, Tree Painting](https://codeforces.com/contest/1187/problem/E)

-   [POJ 3585 Accumulation Degree](http://poj.org/problem?id=3585)

-   [\[USACO10MAR\]Great Cow Gathering G](https://www.luogu.com.cn/problem/P2986)

-   [CodeForce 708C Centroids](http://codeforces.com/problemset/problem/708/C)

## References and notes

[^note1]: [Complexity proof of subtree-merging knapsack DP – LYD729's CSDN blog](https://blog.csdn.net/lyd_7_29/article/details/79854245)
