---
title: Storing a graph
---

To work with graphs in competitive programming, one first has to learn how a graph is stored.

## Conventions

We assume the reader has already read and understood the basic parts of [Basic concepts of graph theory](./concept.md); if you run into difficulties while reading, you can also look things up on that page.

In this article $n$ denotes the number of vertices of the graph, $m$ the number of edges, and $d^+(u)$ the out-degree of vertex $u$, i.e. the number of edges leaving $u$.

## Storing edges directly

### Method

Store the edges in an array whose every element contains the start and end vertex of one edge (and the weight in a weighted graph). (Or use several arrays storing the start vertices, end vertices and weights separately.)

??? note "Sample code"
    === "C++"
        ```cpp
        #include <iostream>
        #include <vector>
        
        using namespace std;
        
        struct Edge {
          int u, v;
        };
        
        int n, m;
        vector<Edge> e;
        vector<bool> vis;
        
        bool find_edge(int u, int v) {
          for (int i = 1; i <= m; ++i) {
            if (e[i].u == u && e[i].v == v) {
              return true;
            }
          }
          return false;
        }
        
        void dfs(int u) {
          if (vis[u]) return;
          vis[u] = true;
          for (int i = 1; i <= m; ++i) {
            if (e[i].u == u) {
              dfs(e[i].v);
            }
          }
        }
        
        int main() {
          cin >> n >> m;
        
          vis.resize(n + 1, false);
          e.resize(m + 1);
        
          for (int i = 1; i <= m; ++i) cin >> e[i].u >> e[i].v;
        
          return 0;
        }
        ```
    
    === "Python"
        ```python
        class Edge:
            def __init__(self, u=0, v=0):
                self.u = u
                self.v = v
        
        
        n, m = map(int, input().split())
        
        e = [Edge() for _ in range(m)]
        vis = [False] * n
        
        for i in range(m):
            e[i].u, e[i].v = map(int, input().split())
        
        
        def find_edge(u, v):
            for i in range(m):
                if e[i].u == u and e[i].v == v:
                    return True
            return False
        
        
        def dfs(u):
            if vis[u]:
                return
            vis[u] = True
            for i in range(m):
                if e[i].u == u:
                    dfs(e[i].v)
        ```

### Complexity

Checking whether a given edge exists: $O(m)$.

Iterating over all outgoing edges of a vertex: $O(m)$.

Traversing the whole graph: $O(nm)$.

Space complexity: $O(m)$.

### Applications

Since traversal with directly stored edges is inefficient, this representation is generally not used for traversing a graph.

In [Kruskal's algorithm](./mst.md#kruskals-algorithm) the edges have to be sorted by weight, so they must be stored directly.

In some problems the graph has to be built several times (e.g. once the original graph and once the reversed graph); then we can either use several other data structures to store several graphs at once, or store the edges directly and rebuild the graph from them whenever needed.

## Adjacency matrix

### Method

Store the edges in a two-dimensional array `adj`, where `adj[u][v]` equal to 1 means there is an edge from $u$ to $v$ and 0 means there is none. In a weighted graph, `adj[u][v]` can store the weight of the edge from $u$ to $v$.

??? note "Sample code"
    === "C++"
        ```cpp
        #include <iostream>
        #include <vector>
        
        using namespace std;
        
        int n, m;
        vector<bool> vis;
        vector<vector<bool>> adj;
        
        bool find_edge(int u, int v) { return adj[u][v]; }
        
        void dfs(int u) {
          if (vis[u]) return;
          vis[u] = true;
          for (int v = 1; v <= n; ++v) {
            if (adj[u][v]) {
              dfs(v);
            }
          }
        }
        
        int main() {
          cin >> n >> m;
        
          vis.resize(n + 1);
          adj.resize(n + 1, vector<bool>(n + 1));
        
          for (int i = 1; i <= m; ++i) {
            int u, v;
            cin >> u >> v;
            adj[u][v] = true;
          }
        
          return 0;
        }
        ```
    
    === "Python"
        ```python
        vis = [False] * (n + 1)
        adj = [[False] * (n + 1) for _ in range(n + 1)]
        
        for i in range(1, m + 1):
            u, v = map(lambda x: int(x), input().split())
            adj[u][v] = True
        
        
        def find_edge(u, v):
            return adj[u][v]
        
        
        def dfs(u):
            if vis[u]:
                return
            vis[u] = True
            for v in range(1, n + 1):
                if adj[u][v]:
                    dfs(v)
        ```

### Complexity

Checking whether a given edge exists: $O(1)$.

Iterating over all outgoing edges of a vertex: $O(n)$.

Traversing the whole graph: $O(n^2)$.

Space complexity: $O(n^2)$.

### Applications

An adjacency matrix is only suitable when there are no multiple edges (or they can be ignored).

Its most notable advantage is checking whether an edge exists in $O(1)$.

Since an adjacency matrix is very inefficient on sparse graphs (especially on graphs with many vertices, where the memory is unaffordable), it is usually used only on dense graphs.

## Adjacency list

### Method

Store the edges in an array of data structures that support dynamic insertion, e.g. `vector<int> adj[n + 1]`, where `adj[u]` holds the information about all outgoing edges of vertex $u$ (end vertex, weight, etc.).

??? note "Sample code"
    === "C++"
        ```cpp
        #include <iostream>
        #include <vector>
        
        using namespace std;
        
        int n, m;
        vector<bool> vis;
        vector<vector<int>> adj;
        
        bool find_edge(int u, int v) {
          for (int i = 0; i < adj[u].size(); ++i) {
            if (adj[u][i] == v) {
              return true;
            }
          }
          return false;
        }
        
        void dfs(int u) {
          if (vis[u]) return;
          vis[u] = true;
          for (int i = 0; i < adj[u].size(); ++i) dfs(adj[u][i]);
        }
        
        int main() {
          cin >> n >> m;
        
          vis.resize(n + 1);
          adj.resize(n + 1);
        
          for (int i = 1; i <= m; ++i) {
            int u, v;
            cin >> u >> v;
            adj[u].push_back(v);
          }
        
          return 0;
        }
        ```
    
    === "Python"
        ```python
        vis = [False] * (n + 1)
        adj = [[] for _ in range(n + 1)]
        
        for i in range(1, m + 1):
            u, v = map(lambda x: int(x), input().split())
            adj[u].append(v)
        
        
        def find_edge(u, v):
            for i in range(0, len(adj[u])):
                if adj[u][i] == v:
                    return True
            return False
        
        
        def dfs(u):
            if vis[u]:
                return
            vis[u] = True
            for i in range(0, len(adj[u])):
                dfs(adj[u][i])
        ```

### Complexity

Checking whether there is an edge from $u$ to $v$: $O(d^+(u))$ (if the edges are sorted in advance, [binary search](../basic/binary.md) brings this down to $O(\log(d^+(u)))$).

Iterating over all outgoing edges of vertex $u$: $O(d^+(u))$.

Traversing the whole graph: $O(n+m)$.

Space complexity: $O(m)$.

### Applications

Suitable for storing all kinds of graphs, unless there are special requirements (e.g. when edge existence must be checked quickly and there are few vertices, an adjacency matrix can be used).

Especially suitable when all outgoing edges of a vertex have to be sorted.

## Linked forward star

### Method

Essentially it is an adjacency list implemented with linked lists; the core code is as follows:

=== "C++"
    ```cpp
    // head[u] and cnt are initialized to -1
    void add(int u, int v) {
      nxt[++cnt] = head[u];  // successor of the current edge
      head[u] = cnt;         // first edge leaving vertex u
      to[cnt] = v;           // end vertex of the current edge
    }
    
    // iterate over the outgoing edges of u
    for (int i = head[u]; ~i; i = nxt[i]) {  // ~i means i != -1
      int v = to[i];
    }
    ```

=== "Python"
    ```python
    # head[u] and cnt are initialized to -1
    def add(u, v):
        cnt = cnt + 1
        nex[cnt] = head[u]  # successor of the current edge
        head[u] = cnt  # first edge leaving vertex u
        to[cnt] = v  # end vertex of the current edge
    
    
    # iterate over the outgoing edges of u
    i = head[u]
    while ~i:  # ~i means i != -1
        v = to[i]
        i = nxt[i]
    ```

??? note "Sample code"
    ```cpp
    #include <iostream>
    #include <vector>
    
    using namespace std;
    
    int n, m;
    vector<bool> vis;
    vector<int> head, nxt, to;
    
    void add(int u, int v) {
      nxt.push_back(head[u]);
      head[u] = to.size();
      to.push_back(v);
    }
    
    bool find_edge(int u, int v) {
      for (int i = head[u]; ~i; i = nxt[i]) {  // ~i means i != -1
        if (to[i] == v) {
          return true;
        }
      }
      return false;
    }
    
    void dfs(int u) {
      if (vis[u]) return;
      vis[u] = true;
      for (int i = head[u]; ~i; i = nxt[i]) dfs(to[i]);
    }
    
    int main() {
      cin >> n >> m;
    
      vis.resize(n + 1, false);
      head.resize(n + 1, -1);
    
      for (int i = 1; i <= m; ++i) {
        int u, v;
        cin >> u >> v;
        add(u, v);
      }
    
      return 0;
    }
    ```

### Complexity

Checking whether there is an edge from $u$ to $v$: $O(d^+(u))$.

Iterating over all outgoing edges of vertex $u$: $O(d^+(u))$.

Traversing the whole graph: $O(n+m)$.

Space complexity: $O(m)$.

### Applications

Suitable for storing all kinds of graphs, but it can neither check quickly whether an edge exists nor conveniently sort the outgoing edges of a vertex.

Its advantage is that edges are numbered, which is sometimes very useful; moreover, if `cnt` is initialized to an odd value, then when storing bidirectional edges `i ^ 1` is exactly the reverse edge of `i` (commonly used in [network flow](./flow.md)).
