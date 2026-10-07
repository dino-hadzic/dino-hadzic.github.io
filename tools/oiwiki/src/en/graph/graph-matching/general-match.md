---
title: Maximum matching in general graphs
---

## Blossom algorithm

The blossom algorithm (also known as the blossom tree algorithm) solves the maximum cardinality matching problem in general graphs. It was proposed by Jack Edmonds in 1961.
With some modifications it can also solve the maximum weight matching problem in general graphs.
This algorithm was the first to prove that maximum matching has polynomial complexity.

The difference between general graph matching and bipartite matching is that the graph may contain odd cycles.

![general-matching-1](./images/general-matching-1.png)

Take this graph as an example: if we directly flip (swap matching and non-matching edges), the resulting $M$ is invalid, since some vertices appear in two matching edges, and the culprit is the odd cycle.

Now consider the augmenting algorithm for general graphs.
From the bipartite point of view, each time we enumerate an unmatched vertex, take it as the root and label it **"o"**, then alternately label **"o"** and **"i"**; it is easy to see that the edges from **"i"** to **"o"** are matching edges.

Suppose the current vertex is $v$ and the adjacent vertex is $u$; there are two cases:

1.  $u$ has not been visited: if $u$ is unmatched, an augmenting path is found; otherwise, look for an augmenting path from the partner of $u$.
2.  $u$ has been visited: if it is labeled "o", we need to **contract a blossom**; otherwise we have met an even cycle and skip it.

The even cycle case can be treated as a bipartite graph, so it can be ignored. After **contracting the blossom**, continue looking for an augmenting path in the new graph.

![general-matching-2](./images/general-matching-2.png)

Let the original graph be $G$ and the graph after **contracting the blossom** be $G'$; we only need to prove:

1.  if $G$ has an augmenting path, so does $G'$;
2.  if $G'$ has an augmenting path, so does $G$.

![general-matching-3](./images/general-matching-3.png)

Let the non-tree edge (the one closing the cycle) be $(u,v)$, and define the blossom root $h=LCA(u,v)$.
The odd cycle is alternating, and only the two edges adjacent to $h$ have the same type – both are non-matching edges.
Then the tree edge entering $h$ must be a matching edge, and the edges leaving the cycle from every vertex other than $h$ are non-matching edges.

By observation, there are two ways to leave the cycle through an outgoing edge: clockwise or counterclockwise.

![general-matching-4](./images/general-matching-4.png)

Hence neither **contracting the blossom** nor **not contracting it** affects correctness.

In the implementation, after finding a **blossom** we do not need to actually **contract** it; we can use an array to record which blossom (rooted at which vertex) each vertex belongs to.

### Complexity analysis

Each search for an augmenting path traverses all edges, and when a **blossom** is met, the vertices of the **blossom** are maintained: $O(|E|^2)$.

Enumerating all unmatched vertices and searching for augmenting paths gives $O(|V||E|^2)$ in total.

### Reference code

??? note "Reference code"
    ```cpp
    // graph
    template <typename T>
    class graph {
     public:
      struct edge {
        int from;
        int to;
        T cost;
      };
    
      vector<edge> edges;
      vector<vector<int>> g;
      int n;
    
      graph(int _n) : n(_n) { g.resize(n); }
    
      virtual int add(int from, int to, T cost) = 0;
    };
    
    // undirectedgraph
    template <typename T>
    class undirectedgraph : public graph<T> {
     public:
      using graph<T>::edges;
      using graph<T>::g;
      using graph<T>::n;
    
      undirectedgraph(int _n) : graph<T>(_n) {}
    
      int add(int from, int to, T cost = 1) {
        assert(0 <= from && from < n && 0 <= to && to < n);
        int id = (int)edges.size();
        g[from].push_back(id);
        g[to].push_back(id);
        edges.push_back({from, to, cost});
        return id;
      }
    };
    
    // blossom / find_max_unweighted_matching
    template <typename T>
    vector<int> find_max_unweighted_matching(const undirectedgraph<T> &g) {
      std::mt19937 rng(std::random_device{}());
      vector<int> match(g.n, -1);   // matching
      vector<int> aux(g.n, -1);     // timestamp
      vector<int> label(g.n);       // "o" or "i"
      vector<int> orig(g.n);        // blossom root
      vector<int> parent(g.n, -1);  // parent
      queue<int> q;
      int aux_time = -1;
    
      auto lca = [&](int v, int u) {
        aux_time++;
        while (true) {
          if (v != -1) {
            if (aux[v] == aux_time) {  // found an already visited vertex, i.e. the LCA
              return v;
            }
            aux[v] = aux_time;
            if (match[v] == -1) {
              v = -1;
            } else {
              v = orig[parent[match[v]]];  // continue from the parent of the matched vertex
            }
          }
          swap(v, u);
        }
      };  // lca
    
      auto blossom = [&](int v, int u, int a) {
        while (orig[v] != a) {
          parent[v] = u;
          u = match[v];
          if (label[u] == 1) {  // label the starting vertex "o" and look for an augmenting path
            label[u] = 0;
            q.push(u);
          }
          orig[v] = orig[u] = a;  // contract the blossom
          v = parent[u];
        }
      };  // blossom
    
      auto augment = [&](int v) {
        while (v != -1) {
          int pv = parent[v];
          int next_v = match[pv];
          match[v] = pv;
          match[pv] = v;
          v = next_v;
        }
      };  // augment
    
      auto bfs = [&](int root) {
        fill(label.begin(), label.end(), -1);
        iota(orig.begin(), orig.end(), 0);
        while (!q.empty()) {
          q.pop();
        }
        q.push(root);
        // label the starting vertex "o"; here "0" stands for "o" and "1" stands for "i"
        label[root] = 0;
        while (!q.empty()) {
          int v = q.front();
          q.pop();
          for (int id : g.g[v]) {
            auto &e = g.edges[id];
            int u = e.from ^ e.to ^ v;
            if (label[u] == -1) {  // found an unvisited vertex
              label[u] = 1;        // label it "i"
              parent[u] = v;
              if (match[u] == -1) {  // found an unmatched vertex
                augment(u);          // augment along the augmenting path
                return true;
              }
              // found a matched vertex; push its partner into the queue to extend the alternating tree
              label[match[u]] = 0;
              q.push(match[u]);
              continue;
            } else if (label[u] == 0 && orig[v] != orig[u]) {
              // found a visited vertex also labeled "o", so we found a "blossom"
              int a = lca(orig[v], orig[u]);
              // find the LCA, then contract the blossom
              blossom(u, v, a);
              blossom(v, u, a);
            }
          }
        }
        return false;
      };  // bfs
    
      auto greedy = [&]() {
        vector<int> order(g.n);
        // randomly shuffle order
        iota(order.begin(), order.end(), 0);
        shuffle(order.begin(), order.end(), rng);
    
        // match the vertices that can be matched
        for (int i : order) {
          if (match[i] == -1) {
            for (auto id : g.g[i]) {
              auto &e = g.edges[id];
              int to = e.from ^ e.to ^ i;
              if (match[to] == -1) {
                match[i] = to;
                match[to] = i;
                break;
              }
            }
          }
        }
      };  // greedy
    
      // start with a random matching
      greedy();
      // look for augmenting paths from unmatched vertices
      for (int i = 0; i < g.n; i++) {
        if (match[i] == -1) {
          bfs(i);
        }
      }
      return match;
    }
    ```

??? note "[UOJ #79. 一般图最大匹配](https://uoj.ac/problem/79)"
    ```cpp
    --8<-- "docs/graph/code/graph-matching/general-match/general-match_1.cpp"
    ```

## General graph matching based on Gaussian elimination

???+ tip "Tip"
    Before reading the following, you may need to read the material on matrices in the "Linear algebra" section:
    
    -   [Matrices](../../math/linear-algebra/matrix.md)
    -   [Determinant](../../math/linear-algebra/determinant.md)
    -   [Gaussian elimination](../../math/numerical/gauss.md)

This part introduces a general graph matching algorithm based on Gaussian elimination. Compared with the classical blossom algorithm, its advantage is that it is easier to understand and to write, and it also makes problems such as "essential vertices of maximum matchings" easier to solve; its disadvantage is a large constant factor, since the $O(n^3)$ of Gaussian elimination is essentially always fully used, whereas the blossom algorithm usually does not reach its worst case.

### Prerequisite: Tutte matrix

**Definition**: For an undirected graph $G = (V, E)$ with $n$ vertices, its Tutte matrix $\tilde{A}(G)$ is an $n \times n$ matrix where:

$$
\tilde{A}(G)_{i,j} = \begin{cases}
x_{i,j}, & i<j,\; (v_i, v_j)\in E \\
-x_{i,j}, & i > j,\; (v_i, v_j) \in E \\
0, & \text{otherwise}
\end{cases}
$$

Here $x_{i, j}$ is a variable, so $\tilde{A}(G)$ contains $|E|$ variables in total.

When there is no ambiguity, $\tilde{A}(G)$ is abbreviated as $\tilde{A}$ below.

**Theorem** (Tutte's theorem): $G$ has a perfect matching if and only if $\det \tilde{A} \ne 0$.

??? note "Proof"
    We introduce the notion of an "even cycle cover": an even cycle cover of an undirected graph $G$ covers all vertices with several even cycles (including 2-cycles), without overlap or omission.
    
    It is easy to prove that $G$ has a perfect matching if and only if $G$ has an even cycle cover.
    
    -   If $G$ has an even cycle cover, we just take every other edge in each cycle to get a perfect matching.
    -   If $G$ has a perfect matching, we just take the 2-cycles corresponding to the matching edges to get an even cycle cover.
    
    Then we prove that $G$ has an even cycle cover if and only if $\tilde{A} \ne 0$.
    
    Consider the definition of the determinant
    
    $$
    \det A = \sum_{\pi} (-1)^{\pi} \prod_{i} A_{i, \pi_i}
    $$
    
    where $\pi$ is an arbitrary permutation and $(-1)^{\pi}$ is $-1$ if the number of inversions in $\pi$ is odd and $1$ otherwise.
    
    It is easy to see that every permutation can be viewed as a cycle cover of $G$. If this cycle cover contains an odd cycle, then its sum with the cover obtained by reversing that cycle must be $0$, so only even cycle covers can make the determinant nonzero. This completes the proof.

**Theorem**: $\operatorname{rank}\tilde{A}$ is always even, and the size of a maximum matching of $G$ equals half of $\operatorname{rank}\tilde{A}$.

??? note "Proof"
    The rank of a skew-symmetric matrix can only be even; the latter is left to the reader.

In practice it is impossible to compute with $|E|$ variables, but we can choose a field, e.g. the residue system $\mathcal{Z}_p$ modulo some prime $p$, randomly replace each variable by a number in $\mathcal{Z}_p$, and then compute. For convenience, when there is no ambiguity, $\tilde{A}$ below directly refers to the matrix after substitution.

**Theorem**: $\operatorname{rank}\tilde{A}$ is at most twice the size of a maximum matching of $G$, and the probability that the two are equal is at least $1 - \frac n p$.

Since $n$ in general graph maximum matching essentially never exceeds $10^3$, in practice taking $p$ to be a prime on the order of $10^9$ is enough.

By the theorem, if we only need the size of the maximum matching and not the matching itself, a single Gaussian elimination computing $\operatorname{rank}\tilde{A}$ suffices, which is far simpler than the blossom algorithm. If the matching itself has to be output, however, things are slightly more complicated and require the algorithm introduced below.

### Constructing a perfect matching

By Tutte's theorem and the theorem above, if $G$ has a perfect matching, then $\tilde{A}$ has full rank with high probability. For convenience, "with high probability" is omitted in the following.

Denote the vertex of $G$ with label $i$ by $v_i$; then we have the following theorem:

**Theorem**: $\tilde{A}^{-1}_{j,i} \ne 0 \iff G - \{v_i, v_j\}$ has a perfect matching.

???+ tip "Inverse matrix and adjugate matrix"
    For any square matrix $A$ of order $n$, its adjugate matrix is defined by $A^*_{i, j} = (-1)^{i + j} M_{j, i}$, where $M_{j, i}$ is the minor obtained by deleting row $j$ and column $i$. In other words, if $M$ is the cofactor matrix of $A$, then $A^* = M^T$.
    
    **Theorem**: If $A$ is invertible, then $A^{-1} = \frac 1 {\det A} A^*$.
    
    So here $A^{-1}_{j, i} \ne 0 \iff M_{i, j} \ne 0$, i.e. the part of $A$ left after deleting row $i$ and column $j$ has full rank.

In other words, if $(v_i, v_j) \in E$ and $\tilde{A}^{-1}_{j, i} \ne 0$, then there is a perfect matching containing the edge $(v_i, v_j)$. Such edges are called **feasible edges** below.

By the theorem above, for an undirected graph $G$ with a perfect matching, we get a fairly obvious brute-force algorithm for finding a perfect matching: each time enumerate $i, j$, and if $(v_i, v_j)$ is a feasible edge (the edge exists and $\tilde{A}^{-1}_{j, i} \ne 0$), add $(v_i, v_j)$ to the matching, delete both vertices from $G$, and recompute the new $\tilde{A}^{-1}$.

This takes $\frac n 2$ rounds in total, each $O(n^3)$, for a total complexity of $O(n ^ 4)$, which is a bit slow. In fact, when recomputing $\tilde{A}^{-1}$ we do not have to compute the inverse from scratch by Gaussian elimination each time; instead we can use the following theorem:

**Theorem** (elimination theorem): Let

$$
A = \begin{bmatrix}
  a_{1, 1} & v^T \\
  u & B
\end{bmatrix} \quad A^{-1} = \begin{bmatrix}
  \hat a^{1, 1} & \hat v^T \\
  \hat u & \hat B
\end{bmatrix}
$$

with $\hat a_{1, 1} \ne 0$; then

$$
B^{-1} = \hat B - \frac {\hat u \hat v^T} {\hat a_{1, 1}}
$$

The theorem describes eliminating the first row and the first column. In fact, it generalizes quite obviously to eliminating any row and column, so we only need to compute $\tilde{A}^{-1}$ once at the very start of the algorithm, and afterwards each deletion of two vertices only requires two $O(n^2)$ elimination steps.

??? note "The description is a bit abstract; see the C++ code"
    ```cpp
    void eliminate(int A[][MAXN], int r, int c) {  // eliminate row r and column c
      row_marked[r] = col_marked[c] = true;        // already eliminated
    
      int inv = quick_power(A[r][c], p - 2);  // inverse
    
      for (int i = 1; i <= n; i++)
        if (!row_marked[i] && A[i][c]) {
          int tmp = (long long)A[i][c] * inv % p;
    
          for (int j = 1; j <= n; j++)
            if (!col_marked[j] && A[r][j])
              A[i][j] = (A[i][j] - (long long)tmp * A[r][j]) % p;
        }
    }
    ```

This takes $\frac n 2$ rounds in total, each of complexity $O(n^2)$, so the above algorithm finds a perfect matching in $O(n^3)$ time.

### Constructing a maximum matching

We have just solved the problem of constructing a perfect matching, but problems usually require a maximum matching.

As mentioned above, the size of a maximum matching of $G$ equals half of $\operatorname{rank}\tilde{A}$. If we can find a largest full-rank square submatrix of $\tilde{A}$, then finding a perfect matching of the induced subgraph corresponding to this submatrix gives a maximum matching of $G$.

From another point of view, if $G$ has a perfect matching, then $\tilde{A}$ has full rank; in other words, $\tilde{A}$ is linearly independent. So if $\tilde{A}$ does not have full rank, we can compute a linear basis of $\tilde{A}$ and keep only the rows and columns corresponding to the basis, obtaining a largest full-rank square submatrix of $\tilde{A}$.

After finding the largest full-rank square submatrix, use the algorithm above to find a perfect matching of the induced subgraph, which gives a maximum matching of the original graph. Note that since Gaussian elimination may swap rows, the implementation must carefully maintain the vertex labels.

??? note "[UOJ #79. 一般图最大匹配](https://uoj.ac/problem/79)"
    ```cpp
    --8<-- "docs/graph/code/graph-matching/general-match/general-match_2.cpp"
    ```

## Exercises

-   [UOJ #79. 一般图最大匹配](https://uoj.ac/problem/79)
-   [UOJ#171.【WC2016】挑战 NPC](https://uoj.ac/problem/171)

## References

1.  Mucha M, Sankowski P.[Maximum matchings via Gaussian elimination](http://web.eecs.umich.edu/~pettie/matching/Mucha-Sankowski-maximum-matching-matrix-multiplication.pdf)
2.  周子鑫，杨家齐 (Zhou Zixin, Yang Jiaqi), "基于线性代数的一般图匹配" (General graph matching based on linear algebra)
3.  ZYQN ["基于线性代数的一般图匹配算法" (A general graph matching algorithm based on linear algebra)](https://oi.cyo.ng/wp-content/uploads/2017/02/maximum_matchings_via_gaussian_elimination.pdf)
