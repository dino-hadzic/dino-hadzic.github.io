---
title: Dominator tree
---

## Introduction

In 1959, the concept of "dominance" was introduced by Reese T. Prosser in [a paper on network flows](http://portal.acm.org/ft_gateway.cfm?id=1460314&type=pdf&coll=GUIDE&dl=GUIDE&CFID=79528182&CFTOKEN=33765747), but no concrete algorithm for computing it was given; it was not until 1969 that Edward S. Lowry and C. W. Medlock first proposed [an efficient algorithm](http://portal.acm.org/ft_gateway.cfm?id=362838&type=pdf&coll=GUIDE&dl=GUIDE&CFID=79528182&CFTOKEN=33765747). The most widely used Lengauer–Tarjan algorithm was proposed by Lengauer and Tarjan in 1979 in [a paper](https://www.cs.princeton.edu/courses/archive/fall03/cs528/handouts/a%20fast%20algorithm%20for%20finding.pdf).

In the competitive programming world, the concept of the dominator tree was first introduced in [ZJOI2012 Disaster](https://www.luogu.com.cn/problem/P2597), where it was also called the "extinction tree"; Chen Sunli also presented this algorithm in a 2020 Chinese national training team paper.

Dominator trees are currently not popular in competitions and related problems are rare; however, in industry, especially in compiler-related fields, dominator trees are widely used.

This article introduces the concept of the dominator tree and several methods for computing it.

## Dominance relation

In an arbitrary directed graph, fix an entry vertex $s$. For a vertex $u$, if every path from $s$ to $u$ passes through some vertex $v$, we say that $v$ **dominates** $u$, or that $v$ is a **dominator** of $u$, written $v\ dom\ u$.

For vertices unreachable from $s$, discussing dominance is meaningless, so unless stated otherwise this article assumes that $s$ can reach every vertex of the graph.

![](images/dom-tree1.png)

For example, in this directed graph, $2$ is dominated by $1$, $3$ is dominated by $1, 2$, 4 is dominated by $1, 2, 3$, 5 is dominated by $1, 2$, etc.

### Lemmas

In the lemmas below, we assume $u, v, w\ne s$

**Lemma 1:** $s$ is a dominator of every vertex; every vertex is a dominator of itself.

**Proof:** Clearly every path from $s$ to $u$ must pass through the two vertices $s$ and $u$.

**Lemma 2:** The dominance relation obtained by considering only simple paths is the same as the one obtained by considering all paths.

**Proof:** For a non-simple path, let $S$ be the set of vertices visited between two visits of the same vertex; deleting the vertices of $S$ associates every non-simple path with a simple path.

A vertex of $S$ that lies on the non-simple path but not on the simple path can never be a dominator, since at least one simple path from $s$ to $u$ does not contain it; for vertices lying on both the simple and the non-simple path, it suffices to consider the simple path.

In summary, discarding non-simple paths has no effect on the dominance relation.

**Lemma 3:** If $u$ $dom$ $v$ and $v$ $dom$ $w$, then $u$ $dom$ $w$.

**Proof:** A path through $w$ must pass through $v$, and a path through $v$ must pass through $u$, so a path through $w$ must pass through $u$, i.e. $u \ dom \ w$.

**Lemma 4:** If $u \ dom \ v$ and $v \ dom\ u$, then $u=v$.

**Proof:** Suppose $u \ne v$; then every path reaching $v$ has already reached $u$, and at the same time every path reaching $u$ has already reached $v$, a contradiction.

**Lemma 5:** If $u \ne v \ne w$, $u \ dom \ w$ and $v \ dom \ w$, then $u \ dom \ v$ or $v \ dom \ u$.

**Proof:** Consider a path $s \rightarrow \dots \rightarrow u \rightarrow \dots \rightarrow v \rightarrow \dots \rightarrow w$. If there is no dominance relation between $u$ and $v$, there must exist a path from $s$ to $v$ not passing through $u$, i.e. a path $s \rightarrow \dots \rightarrow v \rightarrow \dots \rightarrow w$, contradicting $u\ dom\ w$.

### Computing the dominance relation

#### Vertex deletion method

A statement equivalent to the definition: if, after deleting some vertex of the graph, some vertices become unreachable, then the deleted vertex dominates those vertices that became unreachable.

So we only need to try deleting every vertex and run a dfs; the complexity is $O(n^3)$. The core code is given below.

```cpp
// assume the graph has n vertices, starting vertex s = 1
std::bitset<N> vis;
std::vector<int> edge[N];
std::vector<int> dom[N];

void dfs(int u, int del) {
  vis[u] = true;
  for (int v : edge[u]) {
    if (v == del or vis[v]) {
      continue;
    }
    dfs(v, del);
  }
}

void getdom() {
  for (int i = 2; i <= n; ++i) {
    vis.reset();
    dfs(1, i);
    for (int j = 1; j <= n; ++j) {
      if (!vis[j]) {
        dom[j].push_back(i);
      }
    }
  }
}
```

#### Iterative data-flow method

The iterative data-flow method is also a topic rarely seen in competitive programming, so we first give a brief introduction.

Data-flow analysis is a concept from compiler theory, used to analyze how data flows along the execution paths of a program; the iterative data-flow method sets up equations on the nodes of the program's flow graph and solves them by repeated iteration, thereby obtaining the data-flow values at certain points of the program. Here we regard the directed graph as a program flow graph.

In this problem, the equation is:

$$
dom(u)=\{u\} \cup \left(\bigcap_{v\in pre(u)}{dom(v)}\right)
$$

where $pre(u)$ is defined as the set of predecessors of $u$. This equation follows from Lemma 3.

In plain words, the dominator set of a vertex is the intersection of the dominator sets of all its predecessors, united with the vertex itself. Iterate the dominator set of every vertex according to this equation until the answer no longer changes.

To improve efficiency, in each round of iteration we want all predecessors of the vertex currently being processed to have already been processed in this round as far as possible; therefore we use depth-first search to obtain the reverse postorder of the graph and iterate in that order.

A reference implementation of the core code is given below. The predecessor set of every vertex and the reverse postorder of the graph need to be precomputed, but this is not the main topic of this article, so no reference implementation is provided for it.

```cpp
std::vector<int> pre[N];  // predecessors of every vertex
std::vector<int> ord;     // reverse postorder of the graph
std::bitset<N> dom[N];
std::vector<int> Dom[N];

void getdom() {
  dom[1][1] = true;
  flag = true;
  while (flag) {
    flag = false;
    for (int u : ord) {
      std::bitset<N> tmp;
      tmp[u] = true;
      for (int v : pre[u]) {
        tmp &= dom[v];
      }
      if (tmp != dom[u]) {
        dom[u] = tmp;
        flag = true;
      }
    }
  }
  for (int i = 2; i <= n; ++i) {
    for (int j = 1; j <= n; ++j) {
      if (dom[i][j]) {
        Dom[i].push_back(j);
      }
    }
  }
}
```

It is easy to see that the complexity of the above algorithm is $O(n^2)$.

## Dominator tree

In the previous section we saw that every vertex other than $s$ has at least two dominators: $s$ and itself.

For any vertex $u$, the dominator $v$ that is closest to $u$ among its dominators other than itself is called the immediate dominator of $u$, written $idom(u) = v$. Clearly, except for $s$, which has no immediate dominator, every vertex has exactly one immediate dominator.

If for every vertex $u$ other than $s$ we add an edge from $idom(u)$ to $u$, we obtain a directed graph with $n$ vertices and $n - 1$ edges. By Lemmas 3 and 4, we know that the dominance relation cannot be circular, i.e. these edges cannot form a cycle, so the resulting graph is in fact a tree. We call this tree the **dominator tree** of the original graph.

## Computing the dominator tree

### Computing from dom

Consider the dominator set $\{s_1, s_2, \dots, s_k\}$ of some vertex; then there must exist a path $s \rightarrow \dots \rightarrow s_1 \rightarrow \dots \rightarrow s_2 \rightarrow \dots \rightarrow \dots \rightarrow s_k \rightarrow\dots \rightarrow u$. Clearly the immediate dominator of $u$ is $s_k$. Hence the definition of the immediate dominator is equivalent to:

For the dominator set $S$ of a vertex $u$, if $v \in S$ satisfies $\forall w \in S\setminus\{u,v\}, w\ dom \ v$, then $idom(u)=v$.

Therefore, after obtaining the dominator set of every vertex with the algorithms described above, we can easily obtain the immediate dominator of every vertex from the definition above and thus construct the dominator tree. Reference code is given below.

```cpp
std::bitset<N> dom[N];
std::vector<int> Dom[N];
int idom[N];

void getidom() {
  for (int u = 2; u <= n; ++u) {
    for (int v : Dom[u]) {
      std::bitset<N> tmp = (dom[v] & dom[u]) ^ dom[u];
      if (tmp.count() == 1 and tmp[u]) {
        idom[u] = v;
        break;
      }
    }
  }
  for (int u = 2; u <= n; ++u) {
    e[idom[u]].push_back(u);
  }
}
```

### Special case: trees

Clearly the dominator tree of a tree-shaped graph is the tree itself.

### Special case: DAGs

We notice that a DAG has a nice property: when solving in topological order, solutions obtained earlier are not affected by later ones. We can use this property to compute the dominator tree of a DAG quickly.

???+ warning "Note"
    Note that the DAG here may have only one starting vertex; if there are several, vertices dominated by the starting vertices would have several parents in the dominator tree, so the dominance relation could not be expressed simply by a dominator tree.

**Lemma 6:** In a directed graph, $v\ dom\ u$ if and only if $\forall w \in pre(u), v\ dom \ w$.

**Proof:** First we prove sufficiency. Every path from $s$ to $u$ must pass through some vertex $w \in pre(u)$, and $v$ dominates that vertex, so every path from $s$ to $u$ must pass through $v$; hence $v \ dom \ u$.

Then necessity. If $\exists w\in pre(u)$ such that $v$ does not dominate $w$, there must be a path $s \rightarrow \cdots \rightarrow w \rightarrow \cdots \rightarrow u$ not passing through $v$, so $v$ does not dominate $u$.

We observe that a dominator of $u$ must be a common ancestor of all its predecessors in the dominator tree, so clearly the immediate dominator of $u$ is the LCA of all its predecessors in the dominator tree. Computing the LCA by binary lifting supports adding one vertex at a time, so the algorithm above is clearly feasible.

A reference implementation is given below:

```cpp
std::stack<int> sta;
std::vector<int> e[N], g[N], tree[N];  // g is the reverse graph of the original graph, tree is the dominator tree
int n, s, in[N], tpn[N], dep[N], idom[N];  // n is the number of vertices, s the starting vertex, in the in-degree
int fth[N][17];

void topo(int s) {
  sta.push(s);
  while (!sta.empty()) {
    int u = sta.top();
    sta.pop();
    tpn[++tot] = u;
    for (int v : e[u]) {
      --in[v];
      if (!in[v]) {
        sta.push(v);
      }
    }
  }
}

int lca(int u, int v) {
  if (dep[u] < dep[v]) {
    std::swap(u, v);
  }
  for (int i = 15; i >= 0; --i) {
    if (dep[fth[u][i]] >= dep[v]) {
      u = fth[u][i];
    }
  }
  if (u == v) {
    return u;
  }
  for (int i = 15; i >= 0; --i) {
    if (fth[u][i] != fth[v][i]) {
      u = fth[u][i];
      v = fth[v][i];
    }
  }
  return fth[u][0];
}

void build() {
  topo(s);
  for (int i = 1; i <= n; ++i)
    for (int j = 0; j <= 15; ++j) fth[i][j] = s;
  for (int i = 1; i <= n; ++i) {
    int u = tpn[i];
    if (g[u].size()) {
      int v = g[u][0];
      for (int j = 1, q = g[u].size(); j < q; ++j) {
        v = lca(v, g[u][j]);
      }
      tree[v].push_back(u);
      fth[u][0] = v;
      dep[u] = dep[v] + 1;
      for (int i = 1; i <= 15; ++i) {
        fth[u][i] = fth[fth[u][i - 1]][i - 1];
      }
    }
  }
}

```

### Lengauer–Tarjan algorithm

The Lengauer–Tarjan algorithm is one of the most famous algorithms for computing dominator trees; it computes the dominator tree of a directed graph in $O(n\alpha(n, m))$ time. This algorithm introduces the concept of the **semi-dominator** and uses semi-dominators to help compute immediate dominators.

#### Conventions

First, we perform a dfs of the directed graph starting from $s$; the visited vertices and edges form a tree $T$. We call the traversed edges tree edges and the others non-tree edges; let $dfn(u)$ be the position at which vertex $u$ is visited; define $u<v$ if and only if $dfn(u) < dfn(v)$.

#### Semi-dominator

The semi-dominator of a vertex $u$ is the smallest vertex $v$ such that there is a path from $v$ to $u$ on which every vertex other than $u, v$ is greater than $u$. Formally, the semi-dominator $sdom(u)$ of $u$ is defined as:

$sdom(u) = \min(v|\exists v=v_0 \rightarrow v_1 \rightarrow\dots \rightarrow v_k = u, \forall 1\le i\le k - 1, v_i > u)$

We find that semi-dominators have some useful properties:

**Lemma 7:** For every vertex $u$, $sdom(u) < u$.

**Proof:** From the definition it is easy to see that the parent $fa(u)$ of $u$ in $T$ also satisfies the condition of a semi-dominator, and $fa(u) < u$, so no vertex greater than $u$ can be its semi-dominator.

**Lemma 8:** For every vertex $u$, $idom(u)$ is an ancestor of $u$ in $T$.

**Proof:** The path from $s$ to $u$ in $T$ corresponds to a path in the original graph, so $idom(u)$ must lie on this path.

**Lemma 9:** For every vertex $u$, $sdom(u)$ is an ancestor of $u$ in $T$.

**Proof:** Suppose $sdom(u)$ is not an ancestor of $u$. Then $sdom(u)$ cannot have an edge to any vertex with $\mathrm{dfs}$ order greater than or equal to $u$ (otherwise that vertex would be inside the subtree of $sdom(u)$ rather than another subtree), a contradiction.

**Lemma 10:** For every vertex $u$, $idom(u)$ is an ancestor of $sdom(u)$.

**Proof:** We can go from $s$ to $sdom(u)$ and then follow the path from the definition to $u$. By definition, the vertices on the path from $sdom(u)$ to $u$ do not dominate $u$, so $idom(u)$ must be an ancestor of $sdom(u)$.

**Lemma 11:** For any vertices $u \ne v$ such that $v$ is an ancestor of $u$, either $v$ is an ancestor of $idom(u)$, or $idom(u)$ is an ancestor of $idom(v)$.

**Proof:** For any vertex $w$ between $v$ and $idom(v)$, by the definition of the immediate dominator there must be a path from $s$ to $idom(v)$ and then to $v$ not passing through $w$. Hence these vertices $w$ cannot be $idom(u)$, so $idom(u)$ is either a descendant of $v$ or an ancestor of $idom(v)$.

From the lemmas above we obtain the following theorem:

**Theorem 1:** The semi-dominator of a vertex $u$ is the smallest vertex among its predecessors and the semi-dominators of all ancestors (in $T$) of its predecessors that are greater than $u$. Formally, $sdom(u)=\min(\{v|\exists v \rightarrow u, v < u \} \cup \{sdom(w) | w > u\ and\ \exists w \rightarrow \dots \rightarrow v \rightarrow u \})$.

**Proof:** Let $x$ equal the right side of the expression above.

First we prove $sdom(u) \le x$. By Lemma 7, this is equivalent to proving that both choices above satisfy the condition of a semi-dominator. The case where $x$ is a predecessor of $u$ is obvious; for the second part, concatenate the path $x=v_0\rightarrow\dots\rightarrow v_j=w$ from the definition of the semi-dominator, a path $w=v_j \rightarrow\dots\rightarrow v_k=v$ in $T$ satisfying $\forall i\in[j, k-1], v_i\ge w > u$, and the path $v \rightarrow u$; this constructs a path satisfying the definition of the semi-dominator.

Then we prove $sdom(u)\ge x$. Consider the path $sdom(u)=v_0\rightarrow v_1 \rightarrow\dots\rightarrow v_k=u$ from the definition of the semi-dominator of $u$. It is easy to see that $k=1$ and $k > 1$ correspond to the two choices in the definition. If $k = 1$, there is a directed edge $sdom(u) \rightarrow u$, and the claim follows from Lemma 7; if $k>1$, let $j$ be the smallest number such that $j \ge 1$ and $v_j$ is an ancestor of $v_{k-1}$ in $T$. Since $k$ satisfies this condition, such a $j$ must exist.

We prove that $v_0 \rightarrow \dots \rightarrow v_j$ is a path satisfying the semi-dominator condition for $v_j$, i.e. that $\forall i \in [1, j), v_i>v_j$. If not, let $i$ be the index with $v_i < v_j$ for which $v_i$ is smallest. Then all vertices on the path $v_i\rightarrow\dots\rightarrow v_j$ are at least $v_i$, so by the property of the dfs tree, $v_i$ must be an ancestor of $v_j$, and hence also an ancestor of $v_{k-1}$, contradicting the minimality of $j$. Therefore $sdom(v_j)\le sdom(u)$. Since $x\le sdom(v_j)$, we get $sdom(u)\ge x$. Combined with the previously proved $sdom(u) \le x$, we have $x=sdom(u)$.

By Theorem 1 we can compute the semi-dominator of every vertex. It is easy to see that the complexity bottleneck of computing semi-dominators is the second case; we optimize it with a weighted disjoint set union, updating the minimum during each path compression.

```cpp
void dfs(int u) {
  dfn[u] = ++dfc;
  pos[dfc] = u;
  for (int i = h[0][u]; i; i = e[i].x) {
    int v = e[i].v;
    if (!dfn[v]) {
      dfs(v);
      fth[v] = u;
    }
  }
}

int find(int x) {
  if (fa[x] == x) {
    return x;
  }
  int tmp = fa[x];
  fa[x] = find(fa[x]);
  if (dfn[sdm[mn[tmp]]] < dfn[sdm[mn[x]]]) {
    mn[x] = mn[tmp];
  }
  return fa[x];
}

void getsdom() {
  dfs(1);
  for (int i = 1; i <= n; ++i) {
    mn[i] = fa[i] = sdm[i] = i;
  }
  for (int i = dfc; i >= 2; --i) {
    int u = pos[i], res = INF;
    for (int j = h[1][u]; j; j = e[j].x) {
      int v = e[j].v;
      if (!dfn[v]) {
        continue;
      }
      find(v);
      if (dfn[v] < dfn[u]) {
        res = std::min(res, dfn[v]);
      } else {
        res = std::min(res, dfn[sdm[mn[v]]]);
      }
    }
    sdm[u] = pos[res];
    fa[u] = fth[u];
  }
}

```

#### Computing immediate dominators

##### Converting to a DAG

But I still don't know what semi-dominators are for!

Consider adding to $T$, for every $u$, the directed edge $sdom(u) \rightarrow u$. By Lemma 9, the new graph $G$ obtained this way is necessarily a directed acyclic graph; by Lemma 10, we also find that adding edges this way does not change the dominance relation, so we have converted the original graph into a DAG and can solve it with the algorithm above.

##### Computing via semi-dominators

Building a pile of graphs is too inelegant!

**Theorem 2:** For any vertex $u$, if every vertex $v$ on the path in $T$ from $sdom(u)$ to $w$ satisfies $sdom(v)\ge sdom(w)$, then $idom(u) =sdom(u)$.

**Proof:** By Lemma 10 we know that $idom(u)$ is $sdom(u)$ or an ancestor of it, so it suffices to prove $sdom(u) \ dom \ u$.

Consider an arbitrary path $P$ from $s$ to $u$; we need to prove that $sdom(u)$ must be on $P$. Let $v$ be the last vertex on $P$ satisfying $v<sdom(u)$. If $v$ does not exist, we must have $sdom(u)=idom(u) =s$; otherwise let $w$ be the first vertex on $P$ after $v$ that lies on the path in the DFS tree from $sdom(u)$ to $u$.

We next prove $sdom(w)\le v <sdom(v)$. Consider the path in $T$ from $v$ to $w$, $v = v_0 \rightarrow \dots v_k = w$. If the claim fails, there exists $i\in[1, k- 1], v_i < w$. Then there must be some $j\in [i, k - 1]$ such that $v_j$ is an ancestor of $w$. From the choice of $v$ we know $sdom(u)\le v_j$, so $v_j$ also lies on the path in the DFS tree from $sdom(u)$ to $u$, contradicting the definition of $w$. Therefore $sdom(w)\le v < sdom(v)$, and combined with the hypothesis of the theorem we get $y=sdom(u)$, i.e. the path $P$ contains $sdom(u)$.

**Theorem 3:** For any vertex $u$, the vertex $v$ with the smallest semi-dominator among all vertices on the path in $T$ from $sdom(u)$ to $u$ necessarily satisfies $sdom(v)\le sdom(u)$ and $idom(v) = idom(u)$.

**Proof:** Since $u$ itself also satisfies the condition on $v$, $sdom(v)\le sdom(u)$.

Since $idom(u)$ is an ancestor of $v$ in $T$, by Lemma 11 $idom(u)$ is also an ancestor of $idom(v)$, so it suffices to prove that $idom(v)$ dominates $u$.

Consider an arbitrary path $P$ from $s$ to $u$; we need to prove that $sdom(u)$ must be on $P$. Let $x$ be the last vertex on $P$ satisfying $x<sdom(u)$. If $x$ does not exist, we must have $sdom(u)=idom(u) =s$; otherwise let $y$ be the first vertex on $P$ after $x$ that lies on the path in the DFS tree from $sdom(u)$ to $u$.

In the same way as in the proof of Theorem 2, we obtain $sdom(y) \le x$. By Lemma 10, $sdom(y)\le x<idom(v) \le sdom(v)$. Now, from the definition of $v$, $y$ cannot be a descendant of $sdom(u)$; on the other hand, $y$ cannot be both a descendant of $idom(v)$ and an ancestor of $v$, otherwise the path going along the DFS tree from $s$ to $sdom(y)$, then along P to $y$, and finally along the DFS tree to $v$ would avoid $idom(v)$, contradicting the definition of a dominator. Therefore $y=idom(v)$, i.e. $P$ contains $idom(v)$.

From the two theorems above we obtain the relationship between $sdom(u)$ and $idom(u)$.

Let $v$ be the vertex with the smallest $sdom(v)$ among all vertices between $sdom(u)$ and $u$. Then:

$$
idom(u) =
\left\{ 
\begin{aligned} 
& sdom(u), &\text{if}\ sdom(u) = sdom(v)
\\
&idom(v), &\text{otherwise}
\end{aligned}
\right.
$$

Only a slight modification of the code above for computing semi-dominators is needed.

```cpp
struct E {
  int v, x;
} e[MAX * 4];

int h[3][MAX * 2];

int dfc, tot, n, m, u, v;
int fa[MAX], fth[MAX], pos[MAX], mn[MAX], idm[MAX], sdm[MAX], dfn[MAX],
    ans[MAX];

void add(int x, int u, int v) {
  e[++tot] = {v, h[x][u]};
  h[x][u] = tot;
}

void dfs(int u) {
  dfn[u] = ++dfc;
  pos[dfc] = u;
  for (int i = h[0][u]; i; i = e[i].x) {
    int v = e[i].v;
    if (!dfn[v]) {
      dfs(v);
      fth[v] = u;
    }
  }
}

int find(int x) {
  if (fa[x] == x) {
    return x;
  }
  int tmp = fa[x];
  fa[x] = find(fa[x]);
  if (dfn[sdm[mn[tmp]]] < dfn[sdm[mn[x]]]) {
    mn[x] = mn[tmp];
  }
  return fa[x];
}

void tar(int st) {
  dfs(st);
  for (int i = 1; i <= n; ++i) {
    fa[i] = sdm[i] = mn[i] = i;
  }
  for (int i = dfc; i >= 2; --i) {
    int u = pos[i], res = INF;
    for (int j = h[1][u]; j; j = e[j].x) {
      int v = e[j].v;
      if (!dfn[v]) {
        continue;
      }
      find(v);
      if (dfn[v] < dfn[u]) {
        res = std::min(res, dfn[v]);
      } else {
        res = std::min(res, dfn[sdm[mn[v]]]);
      }
    }
    sdm[u] = pos[res];
    fa[u] = fth[u];
    add(2, sdm[u], u);
    u = fth[u];
    for (int j = h[2][u]; j; j = e[j].x) {
      int v = e[j].v;
      find(v);
      if (sdm[mn[v]] == u) {
        idm[v] = u;
      } else {
        idm[v] = mn[v];
      }
    }
    h[2][u] = 0;
  }
  for (int i = 2; i <= dfc; ++i) {
    int u = pos[i];
    if (idm[u] != sdm[u]) {
      idm[u] = idm[idm[u]];
    }
  }
}

```

## Example problems

### [Luogu P5180 [Template] Dominator Tree](https://www.luogu.com.cn/problem/P5180)

One can compute only the dominance relation and record how many vertices each vertex dominates during the computation, or build the dominator tree and compute the subtree size of every vertex.

Here we give the code for the latter approach.

??? note "Reference code"
    ```cpp
    --8<-- "docs/graph/code/dom-tree/dom-tree_1.cpp"
    ```

### [ZJOI2012 Disaster](https://www.luogu.com.cn/problem/P2597)

Compute the dominator tree on the DAG and then the subtree sizes.

??? note "Reference code"
    ```cpp
    --8<-- "docs/graph/code/dom-tree/dom-tree_2.cpp"
    ```
