---
title: DFS (graph theory)
---

## Introduction

DFS stands for [Depth First Search](https://en.wikipedia.org/wiki/Depth-first_search); it is an algorithm for traversing or searching a tree or a graph. "Depth first" means that at every step we try to move to a deeper node.

When explained, this algorithm is often put side by side with BFS, but apart from the fact that both can traverse the connected components of a graph, their uses are completely different, and there are very few situations where the two can be used interchangeably.

The term DFS is often used to refer to a search implemented with a recursive function, but the two are actually not the same. For that kind of search see [DFS (searching)](../search/dfs.md).

## Process

The most distinctive feature of DFS is that it **calls itself recursively**. At the same time, similarly to BFS, DFS marks the vertices it has visited and skips already marked vertices while traversing the graph, ensuring that **every vertex is visited exactly once**. A function that follows these two rules is a DFS in the broad sense.

Concretely, DFS has roughly the following structure:

    DFS(v) // v may be a vertex of the graph, or an abstract notion such as a DP state, etc.
      mark v as visited
      for u in neighbors of v
        if u is not marked as visited then
          DFS(u)
        end
      end
    end

The code above contains only the essential structure of DFS. A real DFS adds some code on top of it to perform other operations that exploit the properties of DFS.

## Properties

The time complexity of the algorithm is usually $O(n+m)$ and the space complexity is $O(n)$, where $n$ is the number of vertices and $m$ the number of edges. Note that the space complexity includes the stack space, whose space complexity is $O(n)$. This time complexity is achieved only if an edge is traversed in $O(1)$ on average, e.g. when the graph is stored as a forward star or an adjacency list; with an adjacency matrix this complexity is not necessarily achievable.

> Note: most current algorithm contests (including NOIP, most provincial selection contests and the contests organized by CCF) support an **unlimited stack**, i.e. the stack space is not limited separately, but the total memory is still subject to the limit stated in the problem. However, most operating systems impose an additional limit on the stack size, so when debugging locally you need some way to remove that limit.
>
> -   On Windows the usual way is to add `-Wl,--stack=1000000000` to the **compiler options**, which sets the stack limit to 1000000000 bytes.
> -   On Linux the usual way is to run `ulimit -s unlimited` **in the terminal** before running the program, which makes the stack unlimited. This has to be done only once per terminal and applies to every subsequent program run.

## Implementation

### Implementation with a stack

DFS can be implemented using a [stack](../ds/stack.md) as the temporary container for the vertices during the traversal; this closely mirrors BFS implemented with a [queue](../ds/queue.md).

=== "C++"
    ```cpp
    vector<vector<int>> adj;  // adjacency list
    vector<bool> vis;         // records whether a vertex has already been visited
    
    void dfs(int s) {
      stack<int> st;
      st.push(s);
      vis[s] = true;
    
      while (!st.empty()) {
        int u = st.top();
        st.pop();
    
        for (int v : adj[u]) {
          if (!vis[v]) {
            vis[v] = true;  // make sure there are no duplicates on the stack
            st.push(v);
          }
        }
      }
    }
    ```

=== "Python"
    ```python
    # adj : List[List[int]] adjacency list
    # vis : List[bool] records whether a vertex has already been visited
    
    
    def dfs(s: int) -> None:
        stack = [s]  # simulate the stack with a list and push the start vertex
        vis[s] = True  # the start vertex is visited
    
        while stack:  # continue while the stack is not empty
            u = (
                stack.pop()
            )  # take and discard the last element (the top of the stack); think of it as moving to u
    
            for v in adj[u]:  # for every element v adjacent to u
                if not vis[v]:  # if v has not been visited before
                    vis[v] = True  # make sure there are no duplicates on the stack
                    stack.append(v)  # push v onto the stack
    ```

### Recursive implementation

The evaluation of functions during recursive calls follows the order of pushing onto and popping from a stack, which is why the virtual address space occupied by function calls is called the call stack; hence DFS can be implemented recursively.

Using an [adjacency list](./save.md#adjacency-list) to store the graph:

=== "C++"
    ```cpp
    vector<vector<int>> adj;  // adjacency list
    vector<bool> vis;         // records whether a vertex has already been visited
    
    void dfs(const int u) {
      vis[u] = true;
      for (int v : adj[u])
        if (!vis[v]) dfs(v)
    }
    ```

=== "Python"
    ```python
    # adj : List[List[int]] adjacency list
    # vis : List[bool] records whether a vertex has already been visited
    
    
    def dfs(u: int) -> None:
        vis[u] = True
        for v in adj[u]:
            if not vis[v]:
                dfs(v)
    ```

Using a [linked forward star](./save.md#linked-forward-star) as an example:

=== "C++"
    ```cpp
    void dfs(int u) {
      vis[u] = 1;
      for (int i = head[u]; i; i = e[i].x) {
        if (!vis[e[i].t]) {
          dfs(v);
        }
      }
    }
    ```

=== "Java"
    ```Java
    public void dfs(int u) {
        vis[u] = true;
        for (int i = head[u]; i != 0; i = e[i].x) {
            if (!vis[e[i].t]) {
                dfs(v);
            }
        }
    }
    ```

=== "Python"
    ```python
    def dfs(u):
        vis[u] = True
        i = head[u]
        while i:
            if vis[e[i].t] == False:
                dfs(v)
            i = e[i].x
    ```

### DFS order

The DFS order is the sequence of vertex indices in the order in which they are visited during the DFS.

We observe that every subtree corresponds to a contiguous segment (an interval) of the DFS order.

### Bracket sequence

When DFS enters a vertex, record a left bracket `(`; when it leaves a vertex, record a right bracket `)`.

Every vertex appears twice. The depths of two adjacent vertices differ by 1.

### DFS on a general graph

On a disconnected graph only the connected component containing the start vertex can be visited.

On a connected graph the DFS order is usually not unique.

Note: the DFS order of a tree is not unique either.

If during the DFS we record, for every vertex, from which vertex it was reached, we obtain a tree structure called the DFS tree. The DFS tree is a spanning tree of the original graph.

The [DFS tree](./scc.md#dfs-spanning-tree) has many properties; for example, it can be used to find [strongly connected components](./scc.md).
