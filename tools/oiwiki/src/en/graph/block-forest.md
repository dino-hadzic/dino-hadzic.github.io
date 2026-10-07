---
title: Block forest (round-square tree)
---

Before reading the following, make sure you are familiar with [Graph theory concepts](./concept.md).

Related reading: [Cut vertices and bridges](./cut.md).

## Introduction

As is well known, trees (or forests) have very nice properties and are easy to maintain with many common data structures.

General graphs do not have such nice properties, but fortunately we can sometimes transfer certain problems on general graphs to trees.

The block forest (also called the round-square tree)[^ref1] is exactly such a method of turning a graph into a tree. This article introduces the construction, properties and some applications of the block forest.

Due to space constraints, some conclusions in this article are stated without proof; readers may understand or prove them on their own.

## Definition

The block forest was originally a tool for handling "cactus graphs" (undirected graphs in which every edge lies in at most one simple cycle), but by exploring more of its properties we can sometimes use it on general undirected graphs as well.

To introduce the block forest, we must first introduce **vertex-biconnected components**.

One definition of a **vertex-biconnected graph** is: between any two distinct vertices of the graph there are at least two vertex-disjoint paths.  
Vertex-disjoint means both that no vertex repeats along a path (a simple path) and that the intersection of the two paths is empty (of course both paths necessarily pass through the start and end vertices, which are not taken into account here).

Notice that for a graph with only one vertex it is hard to define whether it is vertex-biconnected, so for now we do not consider graphs with $1$ vertex.

An almost equivalent definition is: a graph with no cut vertices.  
This definition fails only when the graph has just two vertices and one edge connecting them. It has no cut vertex, but two disjoint paths cannot be found, because there is only one path.  
(It can also be understood as that single path counting twice; the intersection is indeed empty, since it passes through no other vertices.)

Although the original definition is indeed the former, for convenience we adopt the latter as the definition of a vertex-biconnected graph.

A **vertex-biconnected component** of a graph is a **maximal vertex-biconnected subgraph**.  
Unlike strongly connected components etc., a vertex may belong to several vertex-biconnected components, but an edge belongs to exactly one (if the former definition were adopted, it might belong to none).

In the block forest, every original vertex corresponds to a **round vertex**, and every vertex-biconnected component corresponds to a **square vertex**.  
So there are $n+c$ vertices in total, where $n$ is the number of vertices of the original graph and $c$ is the number of vertex-biconnected components of the original graph.

For every vertex-biconnected component, its square vertex is connected by an edge to every vertex in that component.  
Each vertex-biconnected component forms a "star", and several "stars" are connected through the cut vertices of the original graph (because the vertices separating vertex-biconnected components are cut vertices).

Clearly, every edge of the block forest connects a round vertex and a square vertex.

The pictures below show the vertex-biconnected components of a graph and the shape of its block forest.[^ref2]

![](./images/block-forest1.svg)![](./images/block-forest2.svg)![](./images/block-forest3.svg)

The number of vertices of the block forest is less than $2n$, because the number of cut vertices is less than $n$; so remember to allocate all arrays with double size.

In fact, the "block forest" is a tree only if the original graph is connected; if the original graph has $k$ connected components, its block forest is a forest of $k$ trees.

If some connected component of the original graph has only one vertex, it needs to be treated case by case; in the following discussion we do not consider isolated vertices.

## Procedure

Given a graph, how do we construct its block forest? First note that if the graph is disconnected, it can be split into connected subgraphs considered separately, so we only consider connected graphs.

Since the block forest is based on vertex-biconnected components, which in turn are based on cut vertices, we only need a method similar to finding cut vertices.

The usual algorithm for finding cut vertices is Tarjan's algorithm; if you know it, understanding the following is easy, and if you don't, that is fine too.

We skip Tarjan's cut vertex algorithm and directly introduce the algorithm used for the block forest (actually a variant of Tarjan's):

Run a DFS on the graph, using two key arrays `dfn` and `low` (similar to Tarjan).

`dfn[u]` stores the DFS order of vertex $u$, i.e. which vertex in order it was when first visited.  
`low[u]` stores the **smallest** DFS order of a vertex that some vertex $v$ in the subtree of $u$ in the DFS tree can reach using **at most one back edge or tree edge to the parent**.  
If you have never heard of Tarjan's algorithm this may be a bit hard to understand, so let us give an example:

![](./images/block-forest4.svg)

(Notice that this graph is in fact equivalent to the graph in the pictures above.)  
Here tree edges are drawn as straight lines from top to bottom, and back edges as curves from bottom to top. The label of a vertex is its DFS order.

Then the `low` array is as follows:

|        $i$        | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ |
| :---------------: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| $\mathrm{low}[i]$ | $1$ | $1$ | $1$ | $3$ | $3$ | $4$ | $3$ | $3$ | $7$ |

Not very hard to understand, is it? Note that the `low` of $9$ here is $7$, which differs from some cut vertex approaches, because for convenience we allowed going up through the parent edge; the main idea is the same, though.

We can easily write the DFS function computing `dfn` and `low` (the `dfn` array is initially zero):

???+ note "Implementation"
    === "C++"
        ```cpp
        void Tarjan(int u) {
          low[u] = dfn[u] = ++dfc;                // low is initialized to the dfn of the current vertex
          for (int v : G[u]) {                    // iterate over the neighbors of u
            if (!dfn[v]) {                        // if not visited yet
              Tarjan(v);                          // recurse
              low[u] = std::min(low[u], low[v]);  // for unvisited ones take min with low
            } else
              low[u] = std::min(low[u], dfn[v]);  // for visited ones take min with dfn
          }
        }
        ```
    
    === "Python"
        ```python
        def Tarjan(u):
            low[u] = dfn[u] = dfc  # low is initialized to the dfn of the current vertex
            dfc = dfc + 1
            for v in G[u]:  # iterate over the neighbors of u
                if dfn[v] == False:  # if not visited yet
                    Tarjan(v)  # recurse
                    low[u] = min(low[u], low[v])  # for unvisited ones take min with low
                else:
                    low[u] = min(low[u], dfn[v])  # for visited ones take min with dfn
        ```

Next, let us consider the relationship between vertex-biconnected components, the DFS tree and these two arrays.

We can see that every vertex-biconnected component is a connected subtree in the DFS tree containing at least two vertices; in particular, the topmost vertex has only one child inside the component.

We can also see that every tree edge lies in exactly one vertex-biconnected component.

Consider the topmost vertex $u$ of a vertex-biconnected component in the DFS tree; we identify this component at $u$, because the subtree of $u$ contains all the information about the whole component.

Since there are at least two vertices, consider the next vertex $v$ of this component; there is a tree edge between $u$ and $v$.

It is easy to see that then necessarily $\mathrm{low}[v]=\mathrm{dfn}[u]$.  
More precisely, for a tree edge $u\to v$, $u,v$ are in the same vertex-biconnected component and $u$ is the shallowest vertex of that component **if and only if** $\mathrm{low}[v]=\mathrm{dfn}[u]$.

So we can determine during the DFS where vertex-biconnected components exist, but we cannot yet precisely determine the vertex set of each component.

This is not hard to handle: during the DFS we maintain a stack storing the vertices whose component (there may be several) has not been determined yet.

When a component is found, all its vertices other than $u$ are gathered at the top of the stack; we just keep popping until $v$ is popped.

Of course, we can process the popped vertices at the same time: simply connect them to the newly created square vertex. Finally, connect $u$ to the square vertex as well.

This completes the construction of the block forest quite naturally; we can number the square vertices with integers starting from $n+1$, which effectively distinguishes round and square vertices.

This part may not be explained clearly enough, so below is a piece of code with detailed comments, output statements that help understanding, and a sample test; readers are encouraged to copy the code and experiment on their own, since code is what helps understanding the most (don't forget to enable `c++11`).

???+ note "Implementation"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <vector>
    
    constexpr int MN = 100005;
    
    int N, M, cnt;
    std::vector<int> G[MN], T[MN * 2];
    
    int dfn[MN], low[MN], dfc;
    int stk[MN], tp;
    
    void Tarjan(int u) {
      printf("  Enter : #%d\n", u);
      low[u] = dfn[u] = ++dfc;                // low is initialized to the dfn of the current vertex
      stk[++tp] = u;                          // push onto the stack
      for (int v : G[u]) {                    // iterate over the neighbors of u
        if (!dfn[v]) {                        // if not visited yet
          Tarjan(v);                          // recurse
          low[u] = std::min(low[u], low[v]);  // for unvisited ones take min with low
          if (low[v] == dfn[u]) {  // marks that a vertex-biconnected component rooted at u was found
            ++cnt;                 // increase the number of square vertices
            printf("  Found a New BCC #%d.\n", cnt - N);
            // pop the vertices of the component other than u and add edges in the block forest
            for (int x = 0; x != v; --tp) {
              x = stk[tp];
              T[cnt].push_back(x);
              T[x].push_back(cnt);
              printf("    BCC #%d has vertex #%d\n", cnt - N, x);
            }
            // note that u itself must be connected too (but not popped)
            T[cnt].push_back(u);
            T[u].push_back(cnt);
            printf("    BCC #%d has vertex #%d\n", cnt - N, u);
          }
        } else
          low[u] = std::min(low[u], dfn[v]);  // for visited ones take min with dfn
      }
      printf("  Exit : #%d : low = %d\n", u, low[u]);
      printf("  Stack:\n    ");
      for (int i = 1; i <= tp; ++i) printf("%d, ", stk[i]);
      puts("");
    }
    
    int main() {
      scanf("%d%d", &N, &M);
      cnt = N;  // component / square vertex indices start from N
      for (int i = 1; i <= M; ++i) {
        int u, v;
        scanf("%d%d", &u, &v);
        G[u].push_back(v);  // add the edge in both directions
        G[v].push_back(u);
      }
      // handle disconnected graphs
      for (int u = 1; u <= N; ++u)
        if (!dfn[u]) Tarjan(u), --tp;
      // note that when Tarjan exits there is still one element on the stack, the root; pop it
      return 0;
    }
    ```

Here is a test case:

```text
13 15
1 2
2 3
1 3
3 4
3 5
4 5
5 6
4 6
3 7
3 8
7 8
7 9
10 11
11 10
11 12
```

The graph corresponding to this example (it includes multi-edges and an isolated vertex):

![](./images/block-forest5.svg)

## Examples

We present some example problems that can be solved with the block forest.

???+ note "[「APIO2018」Duathlon](https://loj.ac/p/2587)"
    ??? note "Problem summary"
        Given a simple undirected graph, how many triples $\langle s, c, f \rangle$ ($s, c, f$ pairwise distinct) are there such that there is a simple path starting at $s$, passing through $c$ and arriving at $f$?
    
    ??? note "Solution"
        Speaking of simple paths, we must mention a very nice property of vertex-biconnected components: for two vertices in the same component, the union of the simple paths between them is exactly equal to that component.  
        That is, between two distinct vertices $u,v$ of the same component there must exist a simple path passing through a given third vertex $w$ of the same component.
        
        Proof of this property:
        
        -   Clearly, if a simple path leaves the component, it can never come back to it, otherwise this would conflict with the definition of a vertex-biconnected component.
        -   So we only need to prove that for any three distinct vertices $u,v,c$ of a vertex-biconnected graph, there is a simple path from $u$ to $v$ passing through $c$.
        -   First exclude the case with $2$ vertices: it satisfies the property, but $3$ distinct vertices cannot be chosen.
        -   For the remaining cases, build a network flow model: connect the source to $c$ with an edge of capacity $2$, and $u$ and $v$ to the sink with edges of capacity $1$.
        -   A bidirectional edge $\langle x,y\rangle$ of the original graph becomes an edge from $x$ to $y$ with capacity $1$ and an edge from $y$ to $x$ with capacity $1$.
        -   Finally, give every vertex other than the source, the sink and $c$ a capacity of $1$, which can be done by vertex splitting.
        -   Since the edge from the source to $c$ has capacity $2$, if the maximum flow of this network is $2$, then a path through $c$ is proven to exist.
        -   By the max-flow min-cut theorem, the minimum cut is clearly at most $2$; it remains to prove that the minimum cut is greater than $1$.
        -   This is equivalent to proving that cutting any single edge of capacity $1$ cannot disconnect the source from the sink.
        -   If we cut the edge connecting $u$ or $v$ to the sink, by the first definition of a vertex-biconnected component there must be a simple path from $c$ to the other, uncut vertex.
        -   If we cut an edge created by splitting a vertex, this is equivalent to deleting a vertex; by the second definition of a vertex-biconnected component the remaining graph is still connected.
        -   If we cut an edge created from an original edge, this is equivalent to deleting an edge, which is weaker than deleting a vertex, so a path clearly exists.
        -   Hence we have proven that the minimum cut is greater than $1$, i.e. the maximum flow equals $2$. Q.E.D.
        
        What does this conclusion tell us? It tells us: considering the path between two round vertices in the block forest, the set of round vertices adjacent to the square vertices on that path equals the set of vertices on the simple paths between the two vertices in the original graph.
        
        Back to the problem: fix $s$ and $f$ and count the valid $c$; clearly the number of valid $c$ equals the number of vertices in the union of the simple paths between $s,f$ minus $2$ (removing $s,f$ themselves).
        
        So after building the block forest of the original graph, the number of vertices on the simple paths between two vertices is related to the number of square vertices (components) and round vertices on their path in the block forest.
        
        Next comes a common trick with the block forest: when counting paths, assign suitable weights to the vertices.  
        In this problem, the weight of every square vertex is the size of the corresponding component, and the weight of every round vertex is $-1$.
        
        With these weights, the sum of vertex weights on the block forest path between two round vertices is exactly the size of the union of simple paths in the original graph minus $2$.
        
        The problem becomes computing $\sum$ of path weight sums between pairs of round vertices in the block forest.
        
        From another angle, we count the contribution of every vertex to the answer, i.e. its weight times the number of paths passing through it; this can be computed with a simple tree DP.
        
        Finally, do not forget to handle the case where the graph is disconnected. Here is the corresponding code:
    
    ??? note "Reference code"
        ```cpp
        --8<-- "docs/graph/code/block-forest/block-forest_1.cpp"
        ```
    
    By the way, the answer of the test case above for this problem is $212$.

???+ note "[Codeforces #487 E. Tourists](https://codeforces.com/contest/487/problem/E)"
    ??? note "Problem summary"
        Given a simple undirected connected graph, support two kinds of operations:
        
        1.  Modify the weight of a vertex.
        
        2.  Query the minimum vertex weight over all simple paths between two vertices.
    
    ??? note "Solution"
        Likewise, we build the block forest of the original graph, set the weight of a square vertex to the minimum weight of its adjacent round vertices, and the problem becomes a path minimum query.
        
        Path minimum can be maintained with heavy-light decomposition and a segment tree, but what about modifications?
        
        Modifying the weight of one round vertex requires modifying all adjacent square vertices, which can easily be forced to $O(n)$ modifications.
        
        Here we use the fact that the block forest is a tree: set the weight of a square vertex to the minimum weight of its round children; then a modification only needs to update the parent square vertex.
        
        To maintain the square vertices, keep a `multiset` of weights for each square vertex.
        
        Note that when querying, if the LCA is a square vertex, the weight of the LCA's parent round vertex must also be considered.
        
        Note: the number of vertices of the block forest must be allocated as twice that of the original graph, otherwise arrays will overflow.
    
    ??? note "Reference code"
        ```cpp
        --8<-- "docs/graph/code/block-forest/block-forest_2.cpp"
        ```

???+ note "[「SDOI2018」Strategy Game](https://loj.ac/p/2562)"
    ??? note "Problem summary"
        Given a simple undirected connected graph. There are $q$ queries:
        
        each gives a vertex set $S$ ($2 \le |S| \le n$); how many vertices $u$ satisfy $u \notin S$ and, after deleting $u$, the vertices of $S$ are not all in one connected component?
        
        Each test point has multiple test cases.
    
    ??? note "Solution"
        First build the block forest; the query becomes the number of round vertices in the connected subgraph of the block forest corresponding to $S$, minus $|S|$.
        
        How to compute the number of round vertices in the connected subgraph? One method:
        
        put the weight of a round vertex on the edge between it and its parent square vertex; the problem becomes a sum of edge weights, for which one may refer to a solution of [「SDOI2015」Treasure Hunt](https://loj.ac/p/2182).  
        That is, sort the vertices of $S$ by DFS order and compute the sum of distances between adjacent vertices in that order (including the distance between the first and the last); the answer is half of that sum, because every edge is traversed exactly twice.
        
        Finally, if the shallowest vertex of the subgraph is a round vertex, add $1$ to the answer, since we did not count it.
        
        Because there are multiple test cases, remember to initialize the arrays.
    
    ??? note "Reference code"
        ```cpp
        --8<-- "docs/graph/code/block-forest/block-forest_3.cpp"
        ```

## Exercises

-   [UVa 1464 Traffic Real Time Query](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=447&page=show_problem&problem=4210)
-   [Luogu P4320 Meeting on the Road](https://www.luogu.com.cn/problem/P4320)
-   [Luogu P10517 Land Planning](https://www.luogu.com.cn/problem/P10517)

## External links

immortalCO, [The block forest — a powerful tool for cacti](https://immortalco.blog.uoj.ac/blog/1955), Universal OJ.

## References and notes

[^ref1]: In 2017, Chen Junkun defined and named the block forest structure in his paper for the Chinese IOI2017 national training team, "Problem report on 'The Magical Subgraph' and its extensions".

[^ref2]: Chen Junkun, "The ordinary block forest and the magical (~~dynamic~~) dynamic programming", NOI2018 winter camp, page 4.
