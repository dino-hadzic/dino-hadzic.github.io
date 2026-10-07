---
title: Random walk on a tree
---

Given a rooted tree, a coin sits on some vertex of the tree and at every step moves to an adjacent vertex with equal probability. We ask for the expected distance traveled by the coin until it reaches an adjacent vertex.

## Definitions

-   $T=(V,E)$: the tree under discussion
-   $d(u)$: the degree of vertex $u$
-   $w(u,v)$: the weight of the edge between vertices $u$ and $v$
-   $p_u$: the parent of vertex $u$
-   $\textit{root}$: the root of the tree
-   $\textit{son}_u$: the set of children of vertex $u$
-   $\textit{sibling}_u$: the set of siblings of vertex $u$

## Expected distance of walking to the parent

Let $f(u)$ denote the expected distance of walking from vertex $u$ to its parent $p_u$. Then:

$$
f(u) = \cfrac{w(u,p_u) + \sum\limits_{v \in \textit{son}_u}(w(u,v) + f(v) + f(u))}{d(u)}
$$

The first part of the numerator corresponds to walking directly to the parent; the second part to walking to a child first, coming back from the child, and then walking to the parent. The denominator $d(u)$ expresses that from vertex $u$ every adjacent vertex is chosen with equal probability.

Simplifying:

$$
\begin{aligned}
    f(u) &= \cfrac{w(u,p_u) + \sum\limits_{v \in \textit{son}_u}(w(u,v) + f(v) + f(u))}{d(u)} \\
         &= \cfrac{w(u,p_u) + \sum\limits_{v \in \textit{son}_u}(w(u,v) + f(v)) + (d(u)-1)f(u)}{d(u)} \\
         &= w(u,p_u) + \sum\limits_{v \in \textit{son}_u}(w(u,v) + f(v)) \\
         &= \sum\limits_{(u,t) \in E}w(u,t) + \sum\limits_{v \in \textit{son}_u}f(v)
\end{aligned}
$$

For a leaf $l$, the initial state is $f(l) = w(p_l, l)$.

When all edge weights in the tree are $1$, the formula above becomes:

$$
f(u) = d(u) + \sum\limits_{v \in \textit{son}_u}f(v)
$$

i.e. the sum of the degrees of all vertices in the subtree of $u$, which is twice the size of the subtree of $u$ $-1$ (every vertex has exactly one edge to its parent; except for the edge between $u$ and $p_u$, which contributes only $1$ to the degree, every edge contributes $2$ to the degree).

## Expected distance of walking to a child

Let $g(u)$ denote the expected distance of walking from vertex $p_u$ to its child $u$. Then:

$$
g(u) = \cfrac{w(p_u,u) + \left(w(p_u,p_{p_u})+g(p_u)+g(u)\right) + \sum\limits_{s \in \textit{sibling}_u}(w(p_u,s)+f(s)+g(u))}{d(p_u)}
$$

The first part of the numerator corresponds to walking directly to the child $u$; the second part to walking to the parent first, coming back from the parent, and then walking to $u$; the third part to walking to a sibling of $u$ first, coming back from it, and then walking to $u$. The denominator $d(p_u)$ expresses that from vertex $p_u$ every adjacent vertex is chosen with equal probability.

Simplifying:

$$
\begin{aligned}
    g(u) &= \cfrac{w(p_u,u) + \left(w(p_u,p_{p_u})+g(p_u)+g(u)\right) + \sum\limits_{s \in \textit{sibling}_u}(w(p_u,s)+f(s)+g(u))}{d(p_u)} \\
         &= \cfrac{w(p_u,u) + w(p_u,p_{p_u}) + g(p_u) + \sum\limits_{s \in \textit{sibling}_u}\left(w(p_u,s)+f(s)\right)+(d(p_u)-1)g(u)}{d(p_u)} \\
         &= w(p_u,u) + w(p_u,p_{p_u}) + g(p_u) + \sum\limits_{s \in \textit{sibling}_u}(w(p_u,s)+f(s)) \\
         &= \sum\limits_{(p_u,t) \in E}w(p_u,t) + g(p_u) + \sum\limits_{s \in \textit{sibling}_u}f(s) \\
         &= \sum\limits_{(p_u,t) \in E}w(p_u,t) + g(p_u) + \left(f(p_u)-\sum\limits_{(p_u,t) \in E}w(p_u,t)-f(u)\right) \\
         &= g(p_u) + f(p_u) - f(u)
\end{aligned}
$$

The initial state is $g(\text{root}) = 0$.

## Implementation (for an unweighted tree)

```cpp
vector<int> G[MAXN];

void dfs1(int u, int p) {
  f[u] = G[u].size();
  for (auto v : G[u]) {
    if (v == p) continue;
    dfs1(v, u);
    f[u] += f[v];
  }
}

void dfs2(int u, int p) {
  if (u != root) g[u] = g[p] + f[p] - f[u];
  for (auto v : G[u]) {
    if (v == p) continue;
    dfs2(v, u);
  }
}
```
