---
title: Tree decomposition
---

## Centroid decomposition

Centroid decomposition (also called point divide and conquer) is suited to problems about path information on large trees.

??? note "Example 1 [Luogu P3806【模板】点分治 1](https://www.luogu.com.cn/problem/P3806)"
    Given a tree with $n$ vertices and edge weights, answer $m$ queries; each query gives $k$ and asks whether there is a pair of vertices at distance $k$ in the tree.
    
    $n\le 10000,m\le 100,k\le 10000000$

First we pick an arbitrary vertex $\mathit{rt}$ as the root. All paths lying entirely inside its subtree fall into two kinds: those passing through the current root and those not passing through it. The paths through the current root again fall into two kinds: those with the root as one endpoint and those with neither endpoint at the root. The latter can be obtained by joining two chains of the former kind. So, for the chosen root $rt$, we first compute the contribution to the answer of the paths in its subtree that pass through this vertex, and then recurse into its subtrees to handle the paths that do not pass through it.

In this problem, for the paths through the root $\mathit{rt}$ we iterate over all its children $\mathit{ch}$ and, with $\mathit{ch}$ as the root, compute the distances from all vertices in the subtree of $\mathit{ch}$ to $\mathit{rt}$. Let $\mathit{dist}_i$ be the distance from vertex $i$ to the current root $rt$, and let $\mathit{tf}_{d}$ indicate whether a vertex $v$ with $\mathit{dist}_v=d$ exists in the subtrees processed so far. If a query $k$ satisfies $tf_{k-\mathit{dist}_i}=true$, a path of length $k$ exists. After checking whether the edges from the subtree of $\mathit{ch}$ can produce an answer, we add these new distances to the array $\mathit{tf}$.

Note that the array $\mathit{tf}$ must not be cleared directly with `memset`; instead, the positions of $\mathit{tf}$ that were used should be put into a queue and cleared from there, which is the only way to guarantee the time complexity.

In centroid decomposition, all recursive calls on one level together process every vertex once; if there are $h$ levels of recursion in total, the overall time complexity is $O(hn)$.

If we always choose the [centroid](./tree-centroid.md) of the subtree as the root, the number of recursion levels is minimal and the time complexity is $O(n\log n)$. This is why this technique is commonly called **centroid decomposition** of a tree in the international competitive programming community.

Note that after choosing a new root you must recompute the subtree sizes; otherwise a seemingly tiny change can break the time complexity or make correctness hard to guarantee.

??? note "Reference code"
    ```cpp
    --8<-- "docs/graph/code/tree-divide/tree-divide_1.cpp"
    ```

??? note "Example 2 [Luogu P4178 Tree](https://www.luogu.com.cn/problem/P4178)"
    Given a weighted tree with $n$ vertices and a number $k$, find the number of pairs of vertices whose distance in the tree is at most $k$.
    
    $n\le 40000,k\le 20000,w_i\le 1000$

Since we are now asked for the number of vertex pairs at distance in $[0,k]$, we use a segment tree for the maintenance and the queries.

??? note "Reference code"
    ```cpp
    --8<-- "docs/graph/code/tree-divide/tree-divide_2.cpp"
    ```

??? note "Example 3 [Luogu P2664 树上游戏](https://www.luogu.com.cn/problem/P2664)"
    Given a tree in which every vertex has a color, define $s(i,j)$ as the number of distinct colors on the path from $\mathit{i}$ to $\mathit{j}$, and $\mathit{sum_{i}}=\sum_{j=1}^n s(i,j)$. Compute $sum_i$ for all $1\leq i\leq n$. ($1 \le n, c_i \le 10^5$)

This problem tests the understanding and application of centroid decomposition quite well and is a good harder example and exercise.

First we need to understand a transformation. The problem defines $\mathit{sum_i}$ as the sum of the numbers of colors on the paths from $i$ to every vertex, but with this definition the answer is hard to accumulate in centroid decomposition, because it is hard to merge the information of two subtrees hanging from the current root. So we change the meaning of $\mathit{sum_i}$. For every color $j$, let $\mathit{cnt_j}$ be the number of paths with one endpoint at $i$ that contain color $j$; then $\mathit{sum_i}$ is simply $\sum \mathit{cnt_j}$. This transformation only changes the object we look at: we consider the contribution of each color to $\mathit{sum_i}$. And $\mathit{cnt_j}$ is easy to compute: whenever we meet a new color, we do $\mathit{cnt_{col_u}}+=\mathit{size_u}$, where $\mathit{size_u}$ is the subtree size of $u$, meaning that all vertices of this subtree contribute one to the answer of $u$ through this color.

In the centroid decomposition we only need to count separately:

1.  the contribution to the root of the paths in the subtree having the current root as an endpoint;
2.  the contribution to every vertex in the subtree of the paths whose LCA is the current root.

Part 1 is easy: since the recursion depth of centroid decomposition does not exceed $\log{n}$, on every level we can traverse the whole subtree and accumulate the answer directly from the definition of $\mathit{sum_i}$ during the traversal.

For part 2, let $d$ be a child of the current root $u$ and let $v$ be any vertex in the subtree of $d$. The answer for $v$ splits into two parts:

1.  The colors that appear on the path $(u, v)$; let their number be $\mathit{num}$, and let $\mathit{siz1}$ be the total size of all subtrees of $u$ other than $d$. Then these colors contribute $\mathit{num}\times \mathit{siz1}$ to the answer of $v$.
2.  The colors $j$ that do not appear on the path $(u, v)$; their contribution comes from the $\mathit{cnt_j}$ of all subtrees of $u$ other than $d$, and this part of the answer is $\sum_{j \notin (u, v)} \mathit{cnt_j}$.

That is the whole counting idea; see the reference code for the implementation details.

??? note "Reference code"
    ```cpp
    --8<-- "docs/graph/code/tree-divide/tree-divide_3.cpp"
    ```

## Edge decomposition

Similarly to centroid decomposition, we pick an edge that splits the tree into two parts as evenly as possible (so that the $\mathit{size}$ values of the two subtrees joined by the edge are as close as possible). Then we recursively process the left and right subtrees and collect the information.

But this does not work; consider a star graph (a "daisy graph"):

![star graph](./images/tree-divide1.svg)

We see that when a vertex has many children of similar $\mathit{size}$, the time complexity of edge decomposition is unacceptable.

If the graph were a binary tree, the drawback of edge decomposition on the star graph above would be avoided. So we consider turning a tree with arbitrary degrees into a binary tree.

Clearly it suffices to build the tree the way a segment tree is built, like this:

![building the tree](./images/tree-divide2.svg)

The newly created vertices are given suitable information according to the problem. For example, when counting path lengths, give the original edges weight $1$ and the new edges weight $0$.

Analyzing the complexity, at most $O(n)$ vertices are added, so the total complexity is $O(n\log n)$.

Almost every centroid decomposition problem can also be solved by edge decomposition (with a difference in the constant factor, which is not critical), so we do not give examples.

## Centroid tree

The centroid tree (point divide tree) is a reconstructed tree that changes the shape of the original tree so that the number of levels becomes a stable $\log n$.

It is commonly used to solve problems with modifications that do not depend on the original shape of the tree.

### Analysis

We reconstruct the original tree by finding a centroid at each step of the centroid decomposition.

Each centroid found is attached as a child of the centroid of the previous level; this forms a tree with $\log n$ levels.

Because the tree has $\log n$ levels, many brute-force approaches that would otherwise be too slow have the correct complexity on the centroid tree.

### Implementation

A small trick: subtracting the size of the heavy child of the previous level's vertex from the total size $\mathit{tot}$ of the previous recursion level gives the total size of the current level. This way finding the centroid needs only one DFS.

???+ note "Reference code"
    ```cpp
    #include <algorithm>
    #include <iostream>
    #include <vector>
    using namespace std;
    
    using IT = vector<int>::iterator;
    
    struct Edge {
      int to, nxt, val;
    
      Edge() {}
    
      Edge(int to, int nxt, int val) : to(to), nxt(nxt), val(val) {}
    } e[300010];
    
    int head[150010], cnt;
    
    void addedge(int u, int v, int val) {
      e[++cnt] = Edge(v, head[u], val);
      head[u] = cnt;
    }
    
    int siz[150010], son[150010];
    bool vis[150010];
    
    int tot, lasttot;
    int maxp, root;
    
    void getG(int now, int fa) {
      siz[now] = 1;
      son[now] = 0;
      for (int i = head[now]; i; i = e[i].nxt) {
        int vs = e[i].to;
        if (vs == fa || vis[vs]) continue;
        getG(vs, now);
        siz[now] += siz[vs];
        son[now] = max(son[now], siz[vs]);
      }
      son[now] = max(son[now], tot - siz[now]);
      if (son[now] < maxp) {
        maxp = son[now];
        root = now;
      }
    }
    
    struct Node {
      int fa;
      vector<int> anc;
      vector<int> child;
    } nd[150010];
    
    int build(int now, int ntot) {
      tot = ntot;
      maxp = 0x7f7f7f7f;
      getG(now, 0);
      int g = root;
      vis[g] = true;
      for (int i = head[g]; i; i = e[i].nxt) {
        int vs = e[i].to;
        if (vis[vs]) continue;
        int tmp = build(vs, ntot - son[vs]);
        nd[tmp].fa = now;
        nd[now].child.push_back(tmp);
      }
      return g;
    }
    
    int virtroot;
    
    int main() {
      int n;
      cin >> n;
      for (int i = 1; i < n; i++) {
        int u, v, val;
        cin >> u >> v >> val;
        addedge(u, v, val);
        addedge(v, u, val);
      }
      virtroot = build(1, n);
    }
    ```
