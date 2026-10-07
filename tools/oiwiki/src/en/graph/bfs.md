---
title: BFS (graph theory)
---

BFS stands for [Breadth First Search](https://en.wikipedia.org/wiki/Breadth-first_search).

It is one of the most basic and most important search algorithms on graphs.

"Breadth first" means that at every step we try to visit the vertices of the same level.
Only when the whole level has been visited do we move on to the next one.

As a consequence, the path found by BFS is the **shortest** valid path from the start vertex. In other words, the path contains the minimum number of edges.

When BFS finishes, every vertex has been visited via the shortest path from the start vertex to it.

The algorithm can be viewed as fire spreading over the graph: at the beginning only the start vertex is on fire, and at every moment every burning vertex spreads the fire to all of its neighbors.

## Implementation

The C++ and Python implementations below are based on storing the graph as a linked forward star; for that implementation see the page [Storing graphs](./save.md).

=== "Pseudocode"
    ```text
    bfs(s) {
      q = new queue()
      q.push(s), visited[s] = true
      while (!q.empty()) {
        u = q.pop()
        for each edge(u, v) {
          if (!visited[v]) {
            q.push(v)
            visited[v] = true
          }
        }
      }
    }
    ```

=== "C++"
    ```cpp
    void bfs(int u) {
      while (!Q.empty()) Q.pop();
      Q.push(u);
      vis[u] = 1;
      d[u] = 0;
      p[u] = -1;
      while (!Q.empty()) {
        u = Q.front();
        Q.pop();
        for (int i = head[u]; i; i = e[i].nxt) {
          if (!vis[e[i].to]) {
            Q.push(e[i].to);
            vis[e[i].to] = 1;
            d[e[i].to] = d[u] + 1;
            p[e[i].to] = u;
          }
        }
      }
    }
    
    void restore(int x) {
      vector<int> res;
      for (int v = x; v != -1; v = p[v]) {
        res.push_back(v);
      }
      std::reverse(res.begin(), res.end());
      for (int i = 0; i < res.size(); ++i) printf("%d", res[i]);
      puts("");
    }
    ```

=== "Python"
    ```python
    from queue import Queue
    
    
    def bfs(u):
        Q = Queue()
        Q.put(u)
        vis[u] = True
        d[u] = 0
        p[u] = -1
        while Q.qsize() != 0:
            u = Q.get()
            i = head[u]
            while i:
                if vis[e[i].to] == False:
                    Q.put(e[i].to)
                    vis[e[i].to] = True
                    d[e[i].to] = d[u] + 1
                    p[e[i].to] = u
                i = e[i].nxt
    
    
    def restore(x):
        res = []
        v = x
        while v != -1:
            res.append(v)
            v = p[v]
        res.reverse()
        for i in range(0, len(res)):
            print(res[i])
    ```

Concretely, we use a queue Q to record the vertices to be processed, and a boolean array `vis[]` to mark whether a vertex has already been visited.

At the beginning we set `vis` of all vertices to 0, meaning not visited; then we put the start vertex s into the queue Q and set `vis[s]` to 1.

After that, in every step we take the vertex u from the front of the queue Q, then mark all vertices v adjacent to u as visited and put them into the queue Q.

The loop repeats until the queue Q is empty, which means the BFS is finished.

During the BFS we can also record some extra information. For example, in the code above the array d records the shortest distance from the start vertex to a vertex (the minimum number of edges to pass), and the array p records from which vertex we reached the current one.

With the array d we can easily get the distance from the start vertex to a vertex.

With the array p we can easily reconstruct the shortest path from the start vertex to a vertex. The function `restore` in the code above uses this array to print, in order, the vertices on the shortest path from the start vertex to vertex x.

Time complexity: $O(n + m)$

Space complexity: $O(n)$ (the `vis` array and the queue)

## Open-closed table

When implementing BFS, we essentially keep the unvisited vertices in a container called open, and the already visited vertices in a container called closed.

## BFS on a tree/graph

### BFS order

Similarly to the DFS order, the BFS order is the sequence of vertex indices in the order in which they are visited during the BFS.

### BFS on a general graph

If the original graph is not connected, only the vertices reachable from the start vertex can be visited.

The BFS order is usually not unique either.

Analogously we can define the BFS tree: if during the BFS we record, for every vertex, from which vertex it was reached, we obtain a tree structure, which is the BFS tree.

## Applications

-   Finding the shortest paths from the start vertex to all other vertices in an unweighted graph.
-   Finding all connected components in $O(n+m)$ time. (We just run a BFS from every vertex that has not been visited yet; obviously each BFS covers exactly one connected component.)
-   If a move in a game is viewed as an edge (a transition) in the state graph, BFS can be used to find the minimum number of moves needed to get from one state of the game to another.
-   Finding the shortest cycle in a directed unweighted graph. (Run a BFS from every vertex; when we are about to reach again the already visited vertex we started from, we know we have found a cycle. The shortest cycle of the graph is the smallest of the cycles obtained from the individual BFS runs.)
-   Finding the edges that are guaranteed to lie on a shortest path $(a, b)$. (Run a BFS from a and from b, obtaining two arrays d. Then for every edge $(u, v)$, if $d_a[u]+1+d_b[v]=d_a[b]$, the edge lies on a shortest path.)
-   Finding the vertices that are guaranteed to lie on a shortest path $(a, b)$. (Run a BFS from a and from b, obtaining two arrays d. Then for every vertex v, if $d_a[v]+d_b[v]=d_a[b]$, the vertex lies on some shortest path.)
-   Finding a shortest path of even length. (We need to build a new graph in which every vertex is split into two new vertices, and an edge $(u, v)$ of the original graph becomes $((u, 0), (v, 1))$ and $((u, 1), (v, 0))$. Run a BFS on the new graph; the shortest path between $(s, 0)$ and $(t, 0)$ is the one we are looking for.)
-   Finding shortest paths in a graph with edge weights 0/1, see the double-ended queue BFS below.

## Double-ended queue BFS

If you are not familiar with the double-ended queue `deque`, see the [section on deque](../lang/csl/sequence-container.md#deque).

Double-ended queue BFS is also called 0-1 BFS.

### Scope of application

Shortest path problems in which an edge may or may not have a weight (since BFS applies to graphs with weight 1, the weights are usually 0 or 1), or which can be transformed into such edge weights.

For example, in a maze problem you can spend 1 coin to walk 5 steps, or spend no coin to walk 1 step; this can be solved with 0-1 BFS.

### Implementation

In general, we put the vertices reached through an unweighted edge at the front of the queue, and the vertices reached through a weighted edge at the back of the queue. This guarantees that, just like in an ordinary BFS, the weights from the front to the back of the queue are monotonically non-decreasing.

Here is the pseudocode:

```cpp
while (queue is not empty) {
  int u = front of the queue;
  pop the front;
  for (each neighbor of u) {
    update the data
    if (...)
      push to the front;
    else
      push to the back;
  }
}
```

### Example problem

### [Codeforces 173B](http://codeforces.com/problemset/problem/173/B)

Given an $n \times m$ grid, a laser beam enters from the top-left corner heading right; at every '#' you may choose to let the beam shoot out in all four directions, or do nothing. Find the minimum number of '#' that must shoot the beam in all four directions so that the beam exits to the right in row $n$.

The intended solution of this problem is not 0-1 BFS, but 0-1 BFS applies and reduces the amount of thinking; many strong contestants solved it this way during the contest.

The approach is simple: shooting out in one direction costs nothing (0), while shooting out in four directions costs (1); then just run the algorithm.

#### Code

```cpp
--8<-- "docs/graph/code/bfs/bfs_1.cpp"
```

## Priority queue BFS

A priority queue corresponds to a binary heap; the STL provides [`std::priority_queue`](../lang/csl/container-adapter.md), which makes using a priority queue convenient.

In a BFS based on a priority queue, at every step we take the vertex with the smallest cost from the front of the queue and continue the search from it. It is easy to prove that this greedy idea is correct, because the search expanding from this vertex will certainly not update the vertices with a higher cost. In other words, we do not go back to consider updating the remaining vertices with a higher cost.

Of course, a vertex may be pushed into the queue several times, each time with a different cost. When the vertex is taken out of the priority queue for the first time, there is no need to search from it again later; it can simply be ignored. Therefore, in a priority queue BFS every vertex is processed only once.

Compared with the ordinary queue BFS, the time complexity gains a factor of $\log n$, since the priority queue has to be maintained after all. However, the ordinary BFS may push and pop every vertex several times, and the time complexity can reach $O(n^2)$ rather than $O(n)$. So the priority queue BFS is usually still faster.

Huh? Doesn't this sound a lot like the heap-optimized [Dijkstra](./shortest-path.md#dijkstra-算法) algorithm? In fact, heap-optimized Dijkstra is exactly priority queue BFS.

## Exercises

-   ["NOIP2017" Cheese](https://uoj.ac/problem/332)

Double-ended queue BFS:

-   [CF1063B. Labyrinth](https://codeforces.com/problemset/problem/1063/B)
-   [CF173B. Chamber of Secrets](https://codeforces.com/problemset/problem/173/B)
-   ["BalticOI 2011 Day1" Switch the Lamp On](https://loj.ac/p/2632)

## References

<https://cp-algorithms.com/graph/breadth-first-search.html>
