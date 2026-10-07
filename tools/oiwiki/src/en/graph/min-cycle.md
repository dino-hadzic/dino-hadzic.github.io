---
title: Minimum cycle
---

## Introduction

???+ question "Problem"
    Given a graph, what is the minimum total edge weight of a cycle consisting of $n$ vertices $(n\ge 3)$?

The minimum cycle of a graph is also called its girth.

## Procedure

### Brute force

Suppose there is an edge of length $w$ between $u$ and $v$, and let $dis(u,v)$ denote the shortest path between $u$ and $v$ after the edge between $u$ and $v$ is deleted.

Then the minimum cycle in an undirected graph is $dis(u,v)+w$.

Note that when looking for the minimum cycle in a directed graph the formula has to be adjusted: the minimum cycle is $dis(v,u)+w$.

The total time complexity is $O(n^2m)$.

### Dijkstra

Related: [Shortest paths/Dijkstra](./shortest-path.md#dijkstras-algorithm)

#### Procedure

Enumerate all edges; for each one, delete it and run Dijkstra from its starting vertex, by the same reasoning as above.

#### Properties

Time complexity $O(m(n+m)\log n)$.

### Floyd

Related: [Shortest paths/Floyd](./shortest-path.md#floyds-algorithm)

#### Procedure

Denote the weight of the edge between $u,v$ in the original graph by $val\left(u,v\right)$.

Note the following property of the Floyd algorithm: when the outermost loop reaches vertex $k$ (before the $k$-th iteration starts), the entry $dis_{u,v}$ of the shortest path array $dis$ is the shortest path from $u$ to $v$ passing only through vertices with indices in the interval $\left[1, k\right)$.

By definition the minimum cycle has at least three vertices; let $w$ be the vertex with the largest index on it and $u,v$ the two vertices adjacent to $w$ on the cycle. Then, when the outermost loop reaches $k=w$, the length of this cycle is $dis_{u,v}+val\left(v,w\right)+val\left(w,u\right)$.

Hence, in the loop, for every $k$ enumerate the pairs $(i,j)$ with $i<k,j<k$ and update the answer.

#### Recording the path

We now know that the cycle has the form $u\to k\to v$, then returns from $v$ to $u$ (passing only through vertices with indices $<k$).

The problem reduces to finding the path $v\leadsto u$. From the triangle inequality $dis_{u,v}\le dis_{u,i}+dis_{i,v}$, record $pos_{u,v}=j$, the vertex such that $dis_{u,v}=dis_{u,j}+dis_{j,v}$. Clearly $j$ lies on the path $v\leadsto u$.

Thus the path splits into two parts, $v\leadsto j$ and $j\leadsto u$, which are handled recursively.

???+ note "Proof that the recursion does not loop forever"
    We argue by contradiction.
    
    Suppose the cycle passes through some vertex $u$ twice. Then the cycle contains a portion that leaves $u$ and returns to $u$ after several edges, which forms a new cycle.
    
    Since the graph has no negative cycles (if it had, there would be no minimum cycle), the total weight of the new cycle is at most that of the original cycle.
    
    So it suffices to take only this cycle, and then the vertex $u$ is not repeated; the assumption fails, so the cycle does not pass through the same vertex twice.
    
    Therefore, when the recursion reaches the vertices $u,v$, their $pos_{u,v}$ is certainly different from both of them, i.e. a new vertex is added.
    
    In particular, when $u$ and $v$ are adjacent we simply return.
    
    Since the total number of vertices is $n$, the number of additions (i.e. recursive calls) does not exceed $n$, so the recursion does not loop forever.

#### Properties

Time complexity: $O(n^3)$.

#### Implementation

Reference implementations in C++ and Python (recording the path):

=== "C++"
    ```cpp
    // the graph has n vertices
    int val[MAXN + 1][MAXN + 1];  // adjacency matrix of the original graph
    int cnt, path[MAXN + 5];      // path and length of the minimum cycle
    
    void get_path(int u, int v) {  // get the path from u to v
      if (pos[u][v] == 0) return;
    
      int k = pos[u][v];
      get_path(u, k);
      path[++cnt] = k;
      get_path(k, v);
    }
    
    void Floyd(const int &n) {
      static int dis[MAXN + 1][MAXN + 1];  // shortest path matrix
      static int pos[MAXN + 1][MAXN + 1];
      memcpy(dis, val, sizeof(val));
      memset(pos, 0, sizeof(pos));
      for (int k = 1; k <= n; ++k) {
        for (int i = 1; i < k; ++i)
          for (int j = 1; j < i; ++j)
            if (ans >
                (long long)val[i][k] + val[k][j] + dis[i][j]) {  // found a shorter cycle
              // Since j<i<k is guaranteed here, the three vertices are distinct and no zero-length cycle appears.
              ans = val[i][k] + val[k][j] + dis[i][j], cnt = 0;
              path[++cnt] = i, path[++cnt] = k,
              path[++cnt] = j;  // add the vertices i,k,j in order
              get_path(j, i);   // add the path from j to i
            }
    
        for (int i = 1; i <= n; ++i)  // usual Floyd shortest-path update
          for (int j = 1; j <= n; ++j) {
            if (dis[i][j] > dis[i][k] + dis[k][j]) {
              dis[i][j] = dis[i][k] + dis[k][j];
              pos[i][j] = k;  // the current path is obtained via k
            }
          }
      }
    }
    ```

=== "Python"
    ```python
    # A sufficiently large value representing infinity
    INF = sys.maxsize
    
    
    def get_path(i, j, pos, path, cnt):
        """
        Recursively collect the intermediate vertices on the shortest path from vertex i to vertex j.
    
        Args:
            i (int): start vertex (0-based index).
            j (int): end vertex (0-based index).
            pos (list[list[int]]): matrix of intermediate vertices of shortest paths. pos[i][j] = k means the shortest path from i to j passes through k.
            path (list[int]): list storing the path vertices (0-based index).
            cnt (int): current number of vertices on the path.
    
        Returns:
            int: updated number of vertices on the path.
        """
        # If pos[i][j] is -1, there is no intermediate vertex between i and j
        if pos[i][j] == -1:
            return cnt
    
        # Get the intermediate vertex k
        k = pos[i][j]
        # Recursively get the path from i to k
        cnt = get_path(i, k, pos, path, cnt)
        # Add the intermediate vertex k to the path
        path[cnt] = k
        cnt += 1
        # Recursively get the path from k to j
        cnt = get_path(k, j, pos, path, cnt)
        return cnt
    
    
    def find_minimum_cycle_undirected(n, edges):
        """
        Find the minimum cycle in an undirected graph using the Floyd-Warshall algorithm.
    
        Args:
            n (int): number of vertices of the graph (1 to n).
            edges (list[tuple]): list of edges; each element is (u, v, w), meaning there is an edge of weight w between vertices u and v.
                                 Vertex indices are 1 to n.
    
        Returns:
            tuple: the length and the path of the minimum cycle.
                   If there is no cycle, returns (INF, []).
                   The path is a list of vertex indices (1-based index).
        """
        # Internally use 0-based indexing
        N = n
        # Initialize the adjacency matrix g with the original edge weights
        g = [[INF for _ in range(N)] for _ in range(N)]
        # Initialize the shortest path matrix dis, initially equal to g
        dis = [[INF for _ in range(N)] for _ in range(N)]
        # Initialize the pos matrix recording intermediate vertices of shortest paths
        pos = [[-1 for _ in range(N)] for _ in range(N)]
    
        # Set the diagonal to 0 (distance from a vertex to itself)
        for i in range(N):
            g[i][i] = 0
            dis[i][i] = 0
    
        # Build the adjacency matrix from the input edges (undirected graph)
        for u, v, w in edges:
            # Convert 1-based indices to 0-based
            u -= 1
            v -= 1
            # In an undirected graph edges go both ways
            g[u][v] = min(g[u][v], w)
            g[v][u] = min(g[v][u], w)
            dis[u][v] = min(dis[u][v], w)
            dis[v][u] = min(dis[v][u], w)
    
        # Initialize the minimum cycle length to infinity
        min_cycle_len = INF
        # Initialize the minimum cycle path
        min_cycle_path = []
    
        # Core part of the Floyd-Warshall algorithm
        # k is the intermediate vertex (0-based index)
        for k in range(N):
            # Before updating dis[i][j], check whether vertex k yields a smaller cycle
            # The cycle is i -> k -> j -> ... -> i
            # Here dis[i][j] is the shortest path using only vertices 0 to k-1 as intermediate vertices
            # The C++ code loops with i < k and j < i; we follow the same logic here (0-based)
            for i in range(k):  # 0 <= i < k
                for j in range(i):  # 0 <= j < i
                    # Check whether i, k, j form a cycle closed via dis[i][j]
                    # Make sure the original edges g[i][k] and g[k][j] exist (not INF)
                    # and the shortest path dis[i][j] from i to j exists (not INF)
                    if g[i][k] != INF and g[k][j] != INF and dis[i][j] != INF:
                        current_cycle_len = g[i][k] + g[k][j] + dis[i][j]
                        if current_cycle_len < min_cycle_len:
                            min_cycle_len = current_cycle_len
                            # Reconstruct the path
                            path = [0] * (N + 5)  # temporary array for the path, large enough
                            cnt = 0
                            # Add i, k, j to the path in order
                            path[cnt] = i
                            cnt += 1
                            path[cnt] = k
                            cnt += 1
                            path[cnt] = j
                            cnt += 1
                            # Get the intermediate vertices of the shortest path from j to i (using the dis and pos computed so far)
                            cnt = get_path(j, i, pos, path, cnt)
                            # Extract the actual path vertices (drop the unused part)
                            # Convert 0-based indices to 1-based
                            min_cycle_path = [node + 1 for node in path[:cnt]]
    
            # Standard Floyd-Warshall shortest path update
            for i in range(N):
                for j in range(N):
                    if (
                        dis[i][k] != INF
                        and dis[k][j] != INF
                        and dis[i][j] > dis[i][k] + dis[k][j]
                    ):
                        dis[i][j] = dis[i][k] + dis[k][j]
                        # Record that the shortest path from i to j passes through k
                        pos[i][j] = k
    
        return min_cycle_len, min_cycle_path
    ```

## Template problem

??? note "[AcWing 344 Sightseeing Tour](https://www.acwing.com/problem/content/346)"
    Given an undirected graph with $n$ vertices, find a cycle in the graph containing at least $3$ vertices, with no repeated vertices, such that the sum of the edge lengths on the cycle is minimal.
    
    This problem is called the minimum cycle problem in undirected graphs.
    
    You must output the minimum cycle itself; if it is not unique, output any one.
    
    $n \le 100$

The time limit allows an $O(n^3)$ approach, so we apply the Floyd-based minimum cycle method directly.

=== "C++"
    ```cpp
    #include <bits/stdc++.h>
    using lint = long long;
    // A sufficiently large constant for the maximum number of vertices
    const int MAXN = 110;
    
    // A sufficiently large value for infinity; initial minimum cycle length
    lint ans = 1e9;  // lint is an alias for long long
    
    // number of vertices n and edges m of the graph
    // cnt is the number of vertices on the minimum cycle path
    // path stores the vertices of the minimum cycle path
    int n, m, cnt, path[MAXN];
    
    // g stores the adjacency matrix of the original graph
    // dis stores the shortest path matrix (updated during the Floyd-Warshall algorithm)
    // pos records intermediate vertices of shortest paths; pos[i][j] = k means the shortest path from i to j passes through k
    int g[MAXN][MAXN], dis[MAXN][MAXN], pos[MAXN][MAXN];
    
    // Recursive function: get the intermediate vertices on the shortest path from vertex u to vertex v
    // Reconstruct the path from the pos matrix
    void get_path(int u, int v) {
      // If pos[u][v] is 0, there is no intermediate vertex between u and v; return immediately
      if (pos[u][v] == 0) return;
    
      // Get the intermediate vertex k
      int k = pos[u][v];
      // Recursively get the path from u to k
      get_path(u, k);
      // Add the intermediate vertex k to the path
      path[++cnt] = k;
      // Recursively get the path from k to v
      get_path(k, v);
    }
    
    // Floyd-Warshall algorithm function: find the minimum cycle in the graph
    void Floyd() {
      // Outer loop: k is the intermediate vertex (1 to n)
      for (int k = 1; k <= n; ++k) {
        // Inner loops: i and j, checking whether vertex k yields a smaller cycle
        // The loops run i from 1 to k-1 and j from 1 to i-1
        // This checks cycles of the form i -> k -> j -> ... -> i
        for (int i = 1; i < k; ++i)
          for (int j = 1; j < i; ++j)
            // Check whether connecting i and j through vertex k forms a smaller cycle
            // The cycle length is the original edge weight from i to k, g[i][k], + the original edge weight from k to j, g[k][j]
            // + the current shortest path from i to j, dis[i][j]
            if (ans > (long long)g[i][k] + g[k][j] + dis[i][j]) {
              // Found a smaller cycle
              ans = g[i][k] + g[k][j] + dis[i][j];  // update the minimum cycle length
              cnt = 0;                              // reset the path counter
              // Add i, k, j to the path in order
              path[++cnt] = i, path[++cnt] = k, path[++cnt] = j;
              // Get the intermediate vertices of the shortest path from j to i and add them to the path
              get_path(j, i);
            }
    
        // Standard Floyd-Warshall shortest path update
        // i from 1 to n, j from 1 to n
        for (int i = 1; i <= n; ++i)
          for (int j = 1; j <= n; ++j) {
            // If a shorter path from i to j is obtained through the intermediate vertex k
            if (dis[i][j] > dis[i][k] + dis[k][j]) {
              // Update the shortest path
              dis[i][j] = dis[i][k] + dis[k][j];
              // Record that the shortest path from i to j passes through k
              pos[i][j] = k;
            }
          }
      }
    }
    
    // Main function
    int main() {
      // Read the number of vertices n and edges m
      std::cin >> n >> m;
      // Initialize the original adjacency matrix g with all weights set to infinity (0x3f usually stands for a very large value)
      memset(g, 0x3f, sizeof(g));
      // Set the distance from a vertex to itself to 0
      for (int i = 1; i <= n; ++i) g[i][i] = 0;
      // Read m edges and build the original adjacency matrix g
      // In an undirected graph edges go both ways; take the smaller weight
      for (int i = 0, u, v, w; i < m; ++i) {
        std::cin >> u >> v >> w;
        g[u][v] = g[v][u] = std::min(g[u][v], w);
      }
      // Copy the original adjacency matrix g into the shortest path matrix dis
      memcpy(dis, g, sizeof(g));
      // Call the Floyd algorithm to find the minimum cycle
      Floyd();
      // Decide from the minimum cycle length whether a cycle exists
      if (ans == 1e9) {  // If the minimum cycle length is still infinite, there is no cycle
        puts("No solution.");
      } else {
        // If a cycle exists, print the path vertices
        // std::cout << "ans = " << ans << std::endl; // print the minimum cycle length (commented out)
        // Print the path vertices separated by spaces
        for (int i = 1; i <= cnt; ++i)
          std::cout << path[i]
                    << (i == cnt ? "" : " ");  // no space after the last vertex
        std::cout << std::endl;                // newline after printing the path
      }
      return 0;
    }
    ```

=== "Python"
    ```python
    import copy
    import sys
    
    # A sufficiently large value representing infinity
    INF = sys.maxsize
    
    
    def get_path(i, j, pos, path, cnt):
        """
        Recursively collect the intermediate vertices on the shortest path from vertex i to vertex j.
    
        Args:
            i (int): start vertex (0-based index).
            j (int): end vertex (0-based index).
            pos (list[list[int]]): matrix of intermediate vertices of shortest paths. pos[i][j] = k means the shortest path from i to j passes through k.
            path (list[int]): list storing the path vertices (0-based index).
            cnt (int): current number of vertices on the path.
    
        Returns:
            int: updated number of vertices on the path.
        """
        # If pos[i][j] is -1, there is no intermediate vertex between i and j
        if pos[i][j] == -1:
            return cnt
    
        # Get the intermediate vertex k
        k = pos[i][j]
        # Recursively get the path from i to k
        cnt = get_path(i, k, pos, path, cnt)
        # Add the intermediate vertex k to the path
        path[cnt] = k
        cnt += 1
        # Recursively get the path from k to j
        cnt = get_path(k, j, pos, path, cnt)
        return cnt
    
    
    def find_minimum_cycle_undirected(n, edges):
        """
        Find the minimum cycle in an undirected graph using the Floyd-Warshall algorithm.
    
        Args:
            n (int): number of vertices of the graph (1 to n).
            edges (list[tuple]): list of edges; each element is (u, v, w), meaning there is an edge of weight w between vertices u and v.
                                 Vertex indices are 1 to n.
    
        Returns:
            tuple: the length and the path of the minimum cycle.
                   If there is no cycle, returns (INF, []).
                   The path is a list of vertex indices (1-based index).
        """
        # Internally use 0-based indexing
        N = n
        # Initialize the adjacency matrix g with the original edge weights
        g = [[INF for _ in range(N)] for _ in range(N)]
        # Initialize the shortest path matrix dis, initially equal to g
        dis = [[INF for _ in range(N)] for _ in range(N)]
        # Initialize the pos matrix recording intermediate vertices of shortest paths
        pos = [[-1 for _ in range(N)] for _ in range(N)]
    
        # Set the diagonal to 0 (distance from a vertex to itself)
        for i in range(N):
            g[i][i] = 0
            dis[i][i] = 0
    
        # Build the adjacency matrix from the input edges (undirected graph)
        for u, v, w in edges:
            # Convert 1-based indices to 0-based
            u -= 1
            v -= 1
            # In an undirected graph edges go both ways
            g[u][v] = min(g[u][v], w)
            g[v][u] = min(g[v][u], w)
            dis[u][v] = min(dis[u][v], w)
            dis[v][u] = min(dis[v][u], w)
    
        # Initialize the minimum cycle length to infinity
        min_cycle_len = INF
        # Initialize the minimum cycle path
        min_cycle_path = []
    
        # Core part of the Floyd-Warshall algorithm
        # k is the intermediate vertex (0-based index)
        for k in range(N):
            # Before updating dis[i][j], check whether vertex k yields a smaller cycle
            # The cycle is i -> k -> j -> ... -> i
            # Here dis[i][j] is the shortest path using only vertices 0 to k-1 as intermediate vertices
            # The C++ code loops with i < k and j < i; we follow the same logic here (0-based)
            for i in range(k):  # 0 <= i < k
                for j in range(i):  # 0 <= j < i
                    # Check whether i, k, j form a cycle closed via dis[i][j]
                    # Make sure the original edges g[i][k] and g[k][j] exist (not INF)
                    # and the shortest path dis[i][j] from i to j exists (not INF)
                    if g[i][k] != INF and g[k][j] != INF and dis[i][j] != INF:
                        current_cycle_len = g[i][k] + g[k][j] + dis[i][j]
                        if current_cycle_len < min_cycle_len:
                            min_cycle_len = current_cycle_len
                            # Reconstruct the path
                            path = [0] * (N + 5)  # temporary array for the path, large enough
                            cnt = 0
                            # Add i, k, j to the path in order
                            path[cnt] = i
                            cnt += 1
                            path[cnt] = k
                            cnt += 1
                            path[cnt] = j
                            cnt += 1
                            # Get the intermediate vertices of the shortest path from j to i (using the dis and pos computed so far)
                            cnt = get_path(j, i, pos, path, cnt)
                            # Extract the actual path vertices (drop the unused part)
                            # Convert 0-based indices to 1-based
                            min_cycle_path = [node + 1 for node in path[:cnt]]
    
            # Standard Floyd-Warshall shortest path update
            for i in range(N):
                for j in range(N):
                    if (
                        dis[i][k] != INF
                        and dis[k][j] != INF
                        and dis[i][j] > dis[i][k] + dis[k][j]
                    ):
                        dis[i][j] = dis[i][k] + dis[k][j]
                        # Record that the shortest path from i to j passes through k
                        pos[i][j] = k
    
        return min_cycle_len, min_cycle_path
    
    
    # --- Main program entry ---
    if __name__ == "__main__":
        # Read the number of vertices n and edges m
        n, m = map(int, sys.stdin.readline().split())
    
        # Read the edges
        edges = []
        for _ in range(m):
            u, v, w = map(int, sys.stdin.readline().split())
            edges.append((u, v, w))
    
        # Find the minimum cycle
        min_len, path = find_minimum_cycle_undirected(n, edges)
    
        # Output the result
        if min_len == INF:
            print("No solution.")
        else:
            # Print the path vertices (1-based index) separated by spaces
            print(" ".join(map(str, path)))
    ```

## Example 2

GDOI2018 Day2 Patrol

Given an undirected graph with $n$ vertices and no negative edge weights, perform $q$ operations of three kinds:

1.  delete a vertex of the graph and all edges incident to it;
2.  restore a deleted vertex and all edges incident to it;
3.  query the size of the minimum cycle containing vertex $x$.

For $50\%$ of the tests, $n,q \le 100$.

For every simple cycle containing vertex $x$ there are two edges adjacent to $x$; deleting either one turns the simple cycle into a simple path.

So enumerate all edges adjacent to $x$, delete one of them each time and run Dijkstra.

Or simply run the Floyd minimum cycle algorithm for every query, $O(qn^3)$.

For $100\%$ of the tests, $n,q \le 400$.

We still use the Floyd minimum cycle algorithm.

If there were no deletions, deleting the queried vertex would break the simple cycle into a simple path.

But the second step is now computed with Floyd.

So the answer requires the distance between any two vertices without passing through the queried vertex $x$.

How to do this online?

Force it offline, and use the offline approach to avoid deletion operations.

Order the queries by time and build a segment tree over them.

The lifetime of every vertex covers all queries except those asking about that vertex; if a vertex is queried $x$ times, its lifetime can be viewed as $x + 1$ intervals, which are inserted into the segment tree.

Then traverse the whole segment tree: when entering a node, store a backup of the Floyd array, add all vertices inserted on that interval, and when leaving, roll back using the backup.

The time complexity of this approach is $O(qn^2\log q)$.

There is also an online approach with better time complexity.

For a query about vertex $x$, run a shortest path computation from $x$, build the shortest path tree, and along the way determine for every vertex which subtree of $x$ it lies in.

Then there must be a non-tree edge whose two endpoints lie in different subtrees of the root, such that this non-tree edge $+$ the paths from its two endpoints to the root form the minimum cycle.

Proof:

Clearly the minimum cycle contains at least one non-tree edge whose endpoints lie in different subtrees of the root.

Suppose this edge is $(u,v)$; the path from $x$ to $u$ in the shortest path tree is the shortest of all paths from $x$ to $u$, and likewise for the path from $x$ to $v$, so the cycle $x\to u\to v\to x$ is certainly no longer than the minimum cycle.

So we can enumerate all non-tree edges and update the answer.

The complexity of each query is that of one single-source shortest path computation, $O(n^2)$.

The total time complexity is $O(qn^2)$.
