---
title: Prüfer sequence
---

???+ note "Note"
    This article is translated from [e-maxx Prüfer Code](https://github.com/e-maxx-eng/e-maxx-eng/blob/master/src/graph/pruefer_code.md). Note also that in the original the vertices are numbered from $0$; following common practice, this article numbers them from $1$.

This article introduces the Prüfer sequence (Prüfer code), a way to represent a labeled tree by a unique sequence of integers.

The Prüfer sequence can be used to prove [Cayley's formula](#cayleys-formula). We will also explain how to count the ways to add edges to a graph so that it becomes connected.

**Note**: we do not consider trees with $1$ vertex.

## Prüfer sequence

### Introduction

The Prüfer sequence represents a labeled tree with $n$ vertices by $n-2$ integers in $[1,n]$. You can also think of it as a bijection between spanning trees of the complete graph and sequences. It is often used in combinatorial counting problems.

Heinz Prüfer invented this sequence in 1918 to prove [Cayley's formula](#cayleys-formula).

### Building the Prüfer sequence of a tree

The Prüfer sequence is built as follows: each time, pick the leaf with the smallest label and delete it, recording in the sequence the vertex it was connected to. After $n-2$ repetitions only two vertices remain and the algorithm ends.

Clearly a heap achieves $O(n\log n)$ complexity.

???+ note "Implementation"
    === "C++"
        ```cpp
        // code taken from the original, vertices are numbered from 0
        vector<vector<int>> adj;
        
        vector<int> pruefer_code() {
          int n = adj.size();
          set<int> leafs;
          vector<int> degree(n);
          vector<bool> killed(n);
          for (int i = 0; i < n; i++) {
            degree[i] = adj[i].size();
            if (degree[i] == 1) leafs.insert(i);
          }
        
          vector<int> code(n - 2);
          for (int i = 0; i < n - 2; i++) {
            int leaf = *leafs.begin();
            leafs.erase(leafs.begin());
            killed[leaf] = true;
            int v;
            for (int u : adj[leaf])
              if (!killed[u]) v = u;
            code[i] = v;
            if (--degree[v] == 1) leafs.insert(v);
          }
          return code;
        }
        ```
    
    === "Python"
        ```python
        # vertices are numbered from 0
        adj = [[]]
        
        
        def pruefer_code():
            n = len(adj)
            leafs = set()
            degree = [0] * n
            killed = [False] * n
            for i in range(1, n):
                degree[i] = len(adj[i])
                if degree[i] == 1:
                    leafs.intersection(i)
            code = [0] * (n - 2)
            for i in range(1, n - 2):
                leaf = leafs[0]
                leafs.pop()
                killed[leaf] = True
                for u in adj[leaf]:
                    if killed[u] == False:
                        v = u
                code[i] = v
                if degree[v] == 1:
                    degree[v] = degree[v] - 1
                    leafs.intersection(v)
            return code
        ```

For example, here is the construction of the Prüfer sequence of a tree with 7 vertices:

![Prüfer](./images/prufer1.png)

The final sequence is $2,2,3,3,2$.

Of course, there is also a linear construction algorithm.

### Linear construction of the Prüfer sequence

The essence of the linear construction is to maintain a pointer to the vertex we are about to delete. First observe that the number of leaves is non-strictly monotonically decreasing: deleting a leaf either keeps the total number of leaves the same or decreases it by 1.

So consider the following process: maintain a pointer $p$. Initially $p$ points to the leaf with the smallest label. At the same time we maintain the degree of every vertex, so that we know whether deleting a vertex creates a new leaf. The operations are:

1.  Delete the vertex pointed to by $p$ and check whether a new leaf is created.
2.  If a new leaf is created, say with label $x$, compare $p$ and $x$. If $x>p$, do nothing else; otherwise delete $x$ immediately, then check whether deleting $x$ creates a new leaf, and repeat step $2$ until no new leaf is created or the new leaf has label $>p$.
3.  Increment the pointer $p$ until it reaches a leaf that has not been deleted.

#### Correctness

Repeating the above operations $n-2$ times completes the construction of the sequence. Now consider the correctness of the algorithm.

$p$ is the current leaf with the smallest label. If deleting $p$ creates no leaf, we can only go look for the next leaf; if it creates a leaf $x$:

-   if $x>p$, then $p$ will reach it anyway while scanning forward, so we do nothing;
-   if $x<p$, then since $p$ was the smallest label and $x$ is even smaller than $p$, $x$ is now the leaf with the smallest label and is deleted first. After deleting $x$ we continue the same reasoning until there is no smaller leaf.

For the complexity analysis, note that every edge is visited at most once (when decreasing degrees), and the pointer traverses every vertex at most once, so the complexity is $O(n)$.

#### Implementation

=== "C++"
    ```cpp
    // code taken from the original, also starting from 0
    vector<vector<int>> adj;
    vector<int> parent;
    
    void dfs(int v) {
      for (int u : adj[v]) {
        if (u != parent[v]) parent[u] = v, dfs(u);
      }
    }
    
    vector<int> pruefer_code() {
      int n = adj.size();
      parent.resize(n), parent[n - 1] = -1;
      dfs(n - 1);
    
      int ptr = -1;
      vector<int> degree(n);
      for (int i = 0; i < n; i++) {
        degree[i] = adj[i].size();
        if (degree[i] == 1 && ptr == -1) ptr = i;
      }
    
      vector<int> code(n - 2);
      int leaf = ptr;
      for (int i = 0; i < n - 2; i++) {
        int next = parent[leaf];
        code[i] = next;
        if (--degree[next] == 1 && next < ptr) {
          leaf = next;
        } else {
          ptr++;
          while (degree[ptr] != 1) ptr++;
          leaf = ptr;
        }
      }
      return code;
    }
    ```

=== "Python"
    ```python
    # also starting from 0
    adj = [[]]
    parent = [0] * n
    
    
    def dfs(v):
        for u in adj[v]:
            if u != parent[v]:
                parent[u] = v
                dfs(u)
    
    
    def pruefer_code():
        n = len(adj)
        parent[n - 1] = -1
        dfs(n - 1)
    
        ptr = -1
        degree = [0] * n
        for i in range(0, n):
            degree[i] = len(adj[i])
            if degree[i] == 1 and ptr == -1:
                ptr = i
    
        code = [0] * (n - 2)
        leaf = ptr
        for i in range(0, n - 2):
            next = parent[leaf]
            code[i] = next
            if degree[next] == 1 and next < ptr:
                degree[next] = degree[next] - 1
                leaf = next
            else:
                ptr = ptr + 1
                while degree[ptr] != 1:
                    ptr = ptr + 1
                leaf = ptr
        return code
    ```

### Properties of the Prüfer sequence

1.  After building the Prüfer sequence, two vertices remain in the original tree, one of which is always the vertex with the largest label $n$.
2.  Every vertex appears in the sequence a number of times equal to its degree minus $1$. (Those that do not appear are leaves.)

### Rebuilding the tree from the Prüfer sequence

Rebuilding the tree works similarly. From the properties of the Prüfer sequence we can obtain the degree of every vertex in the original tree. Then we can also obtain the leaf with the smallest label, and this vertex must be connected to the vertex corresponding to the first number of the Prüfer sequence. Then we decrease the degrees of both vertices by one.

By now you probably know what to do. Each time we pick the vertex of degree $1$ with the smallest label, connect it to the vertex of the Prüfer sequence we are currently at, and decrease the degrees of both vertices. At the end two vertices of degree $1$ remain, one of which is vertex $n$. Connect them. Maintaining this process with a heap, where a vertex is added to the heap whenever its degree drops to $1$, has complexity $O(n\log n)$.

???+ note "Implementation"
    ```cpp
    // code taken from the original
    vector<pair<int, int>> pruefer_decode(vector<int> const& code) {
      int n = code.size() + 2;
      vector<int> degree(n, 1);
      for (int i : code) degree[i]++;
    
      set<int> leaves;
      for (int i = 0; i < n; i++)
        if (degree[i] == 1) leaves.insert(i);
    
      vector<pair<int, int>> edges;
      for (int v : code) {
        int leaf = *leaves.begin();
        leaves.erase(leaves.begin());
    
        edges.emplace_back(leaf, v);
        if (--degree[v] == 1) leaves.insert(v);
      }
      edges.emplace_back(*leaves.begin(), n - 1);
      return edges;
    }
    ```

### Rebuilding the tree in linear time

Same as the linear construction of the Prüfer sequence. New leaves are created when decreasing degrees, so compare such a leaf with the pointer $p$ and, if it is smaller, handle it first.

#### Implementation

```cpp
// code taken from the original
vector<pair<int, int>> pruefer_decode(vector<int> const& code) {
  int n = code.size() + 2;
  vector<int> degree(n, 1);
  for (int i : code) degree[i]++;

  int ptr = 0;
  while (degree[ptr] != 1) ptr++;
  int leaf = ptr;

  vector<pair<int, int>> edges;
  for (int v : code) {
    edges.emplace_back(leaf, v);
    if (--degree[v] == 1 && v < ptr) {
      leaf = v;
    } else {
      ptr++;
      while (degree[ptr] != 1) ptr++;
      leaf = ptr;
    }
  }
  edges.emplace_back(leaf, n - 1);
  return edges;
}
```

From these procedures one can see that the Prüfer sequence establishes a bijection with labeled unrooted trees.

## Cayley's formula

The complete graph $K_n$ has $n^{n-2}$ spanning trees.

How to prove it? There are many ways, but the proof via Prüfer sequences is very simple. Any integer sequence of length $n-2$ with values in $[1,n]$ corresponds bijectively, through the Prüfer sequence, to a spanning tree, so the number of them is $n^{n-2}$.

## Number of ways to make a graph connected

The Prüfer sequence may be more powerful than you think. It yields formulas more general than [Cayley's formula](#cayleys-formula). For example, the following problem:

> A labeled undirected graph with $n$ vertices and $m$ edges has $k$ connected components. We want to add $k-1$ edges so that the whole graph becomes connected. Count the number of ways.

### Proof

Let $s_i$ denote the number of vertices in the $i$-th connected component. Consider building a Prüfer sequence for the $k$ connected components. Since there are many ways to connect two components, this is not an ordinary Prüfer sequence. So let $d_i$ be the degree of the $i$-th component. Since the sum of degrees is twice the number of edges, $\sum_{i=1}^kd_i=2k-2$. Then for a given sequence $d$ the number of ways to build the Prüfer sequence is

$$
\binom{k-2}{d_1-1,d_2-1,\cdots,d_k-1}=\frac{(k-2)!}{(d_1-1)!(d_2-1)!\cdots(d_k-1)!}
$$

For the $i$-th component there are ${s_i}^{d_i}$ ways to connect it, so for a given sequence $d$ the number of ways to make the graph connected is

$$
\binom{k-2}{d_1-1,d_2-1,\cdots,d_k-1}\cdot \prod_{i=1}^k{s_i}^{d_i}
$$

Now we have to enumerate the sequence $d$, and the expression becomes

$$
\sum_{d_i\ge 1，\sum_{i=1}^kd_i=2k-2}\binom{k-2}{d_1-1,d_2-1,\cdots,d_k-1}\cdot \prod_{i=1}^k{s_i}^{d_i}
$$

Well, this is a very unpleasant expression. But don't panic! We have the multinomial theorem:

$$
(x_1 + \dots + x_m)^p = \sum_{\substack{c_i \ge 0 ,\  \sum_{i=1}^m c_i = p}} \binom{p}{c_1, c_2, \cdots ,c_m}\cdot \prod_{i=1}^m{x_i}^{c_i}
$$

So substitute in the original expression: let $e_i=d_i-1$; clearly $\sum_{i=1}^ke_i=k-2$, so the original expression becomes

$$
\sum_{e_i\ge 0，\sum_{i=1}^ke_i=k-2}\binom{k-2}{e_1,e_2,\cdots,e_k}\cdot \prod_{i=1}^k{s_i}^{e_i+1}
$$

Simplifying gives

$$
(s_1+s_2+\cdots+s_k)^{k-2}\cdot \prod_{i=1}^ks_i
$$

i.e.

$$
n^{k-2}\cdot\prod_{i=1}^ks_i
$$

which is the answer.

## Exercises

-   [Luogu P6086【模板】Prüfer 序列](https://www.luogu.com.cn/problem/P6086) (template problem)
-   [Luogu P11039【MX-X3-T6】「RiOI-4」TECHNOPOLIS 2085](https://www.luogu.com.cn/problem/P11039)
-   [UVa #10843 - Anne's game](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=20&page=show_problem&problem=1784)
-   [Timus #1069 - Prufer Code](http://acm.timus.ru/problem.aspx?space=1&num=1069)
-   [Codeforces - Clues](http://codeforces.com/contest/156/problem/D)
-   [Topcoder - TheCitiesAndRoadsDivTwo](https://archive.topcoder.com/ProblemStatement/pm/10774)
