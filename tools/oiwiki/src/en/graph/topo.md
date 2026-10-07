---
title: Topological sorting
---

## Definition

Topological sorting solves the problem of how to order all the vertices of a directed acyclic graph.

We can describe the process with the example of scheduling university courses for each semester. Say the university curriculum contains: "Programming", "Algorithmic Languages", "Advanced Mathematics", "Discrete Mathematics", "Compiler Techniques", "General Physics", "Data Structures", "Database Systems", and so on. According to the schedule in the example, when we want to study "Data Structures" we first have to pass "Discrete Mathematics"; after finishing that course we have the prerequisite for "Compiler Techniques". Of course, "Compiler Techniques" has an even earlier prerequisite, "Algorithmic Languages". These courses are like vertices $u$, and the directed edges $(u,v)$ between them are like the order in which the courses are taken. When the registrar arranges these courses so that the timetable respects the logical dependencies, that is exactly the process of topological sorting.

![topo](images/topo-example-1.svg)

But what if one day the teacher making the schedule dozes off and says that to study "Data Structures" you first need "Operating Systems", while the prerequisite of "Operating Systems" is in turn "Data Structures"; which one should be studied first (not considering studying both at the same time)? Here a cycle appears between "Data Structures" and "Operating Systems"; the students clearly cannot figure out what to study first, so a topological sort is impossible. If a directed graph contains a cycle, we cannot topologically sort it.

So we can say: in a [DAG (directed acyclic graph)](./dag.md) we order the vertices linearly so that for every directed edge $(u,v)$ from vertex $u$ to $v$, $u$ comes before $v$.

Also, given a DAG, if there is an edge from $i$ to $j$ we say that $j$ depends on $i$. If there is a path from $i$ to $j$ ($j$ is reachable from $i$), we say that $j$ depends indirectly on $i$.

The goal of topological sorting is to order all the vertices so that a vertex that comes earlier does not depend on a vertex that comes later.

## AOV network

In everyday life a large project can be seen as a set of several subprojects, and there is necessarily some order among them: some subprojects can only start after certain other subprojects have been completed.

We represent the ordering among the subprojects with a directed graph in which the precedence relations are directed edges. Such a directed graph is called an activity-on-vertex network, i.e. an **AOV network (Activity On Vertex Network)**. An AOV network is necessarily a directed acyclic graph, i.e. it has no cycles. Unlike a DAG, the activities of an AOV network are represented on the vertices. (The picture above is an AOV network.)

In an AOV network the vertices represent activities and the arcs represent precedence relations among the activities. An AOV network must not contain a cycle; then we can find a sequence of vertices such that the predecessor activities of every activity come before its vertex. Such a sequence is called a topological sequence (the topological sequence of an AOV network is not unique), and the process of constructing a topological sequence from an AOV network is called topological sorting. Hence topological sorting can also be explained as arranging all activities of an AOV network in a sequence such that the predecessor activities of every activity come before it (the topological sort of an AOV network is not unique either).

-   Predecessor activity: the activity at the tail of a directed edge is called a predecessor activity of the activity at its head (an activity can only be carried out after all of its predecessors have been completed).

-   Successor activity: the activity at the head of a directed edge is called a successor activity of the activity at its tail.

To check whether an AOV network has a cycle, construct a topological sequence and see whether it contains all the vertices.

### Steps for constructing a topological sequence

1.  Pick a vertex with in-degree zero from the graph.
2.  Output this vertex and delete it and all of its outgoing edges from the graph.

Repeat the two steps above until all vertices have been output (the topological sort is complete), or until there is no vertex with in-degree zero left in the graph; in that case the graph has a cycle, the topological sort cannot be completed, and we are in a deadlock.

## Critical path and AOE network

Corresponding to the AOV network is the **AOE network (Activity On Edge Network)**, i.e. a network in which the edges represent activities. An AOE network is a weighted directed acyclic graph in which the vertices represent events and the arcs represent the duration of activities. AOE networks are usually used to estimate the completion time of a project. An AOE network must be acyclic, and it has a unique starting vertex with in-degree zero (the source) and a unique finishing vertex with out-degree zero (the sink).

![topo](images/topo-example-2.svg)

Some activities in an AOE network can be carried out in parallel, so the shortest time to complete the whole project is the length of the longest activity path from the starting vertex to the finishing vertex (the length of a path here means the sum of the durations of the activities on the path, i.e. the sum of the arc weights, not the number of arcs on the path). Since a project requires all of its activities to be completed, the longest activity path is also the critical path, and it determines the total completion time of the project.

### Basic concepts of AOE networks

-   Activity: in an AOE network an arc represents an activity. The weight of the arc represents the duration of the activity; the activity starts after its predecessor event (the tail of the arc) is triggered.

-   Event: in an AOE network a vertex represents an event; an event is triggered when all of its predecessor activities (the arcs pointing into it) have been completed.

-   Earliest occurrence time of an event (vertex) $v_i$: the earliest possible time at which the event can occur, denoted $ve(i)$; it determines the earliest start time of the activities starting at this vertex; obviously the earliest time of the source is 0. Since an event requires all of its predecessor activities to be completed, it equals the maximum length of a path from the starting vertex to this vertex, recursively: $ve(i) = \max\{ve(j) + val^j_i ~\vert~ j \in pre_i\}$, where $val^j_i$ is the weight of the edge from j to i (i.e. the duration of the activity from j to i) and $pre_i$ is the set of all predecessor events of i.

-   Latest occurrence time of an event (vertex) $v_i$: the latest time at which the event can occur without delaying the whole project, denoted $vl(i)$; it determines the latest start time of all activities ending in this state; it equals the minimum of the latest start times of all successor activities of the event, i.e. $vl(i) = \min\{vl(j) - val^i_j ~\vert~ j \in nxt_i\}$, where $val^i_j$ is the weight of the edge from i to j (i.e. the duration of the activity from i to j) and $nxt_i$ is the set of all successor events of i.

-   Earliest start time of an activity (arc) $(u, v)$: the earliest possible time at which the activity can start, denoted $e(u,v)$; obviously it equals the earliest occurrence time of its predecessor event, i.e. $e(u,v)=ve(u)$.

-   Latest start time of an activity (arc) $(u, v)$: the latest time the activity can start without delaying the whole project, denoted $l(u,v)$; it equals the latest occurrence time of its successor event minus the duration (weight) of the activity, i.e. $l(u,v)=vl(v)-val^u_v$, where $val^u_v$ is the weight of the edge from u to v (i.e. the duration of the activity from u to v).

-   Critical path: the length of the longest path from the source to the sink in the AOE network.

-   Critical activity: an activity on the critical path; its earliest start time equals its latest start time.

### Computing the earliest and latest times recursively

Compute in topological order: the earliest times recursively from front to back, the latest times from back to front, using the formulas given in **Basic concepts of AOE networks** above.

## Kahn's algorithm

### Procedure

Initially, the set $S$ contains all vertices with in-degree $0$ and $L$ is an empty list.

Each time, take a vertex $u$ out of $S$ (any one will do) and put it into $L$, then delete all edges $(u, v_1), (u, v_2), (u, v_3) \cdots$ of $u$. For an edge $(u, v)$, if the in-degree of $v$ becomes $0$ after deleting the edge, put $v$ into $S$.

Repeat the above until the set $S$ is empty. Check whether any edge remains in the graph; if so, the graph must contain a cycle; otherwise return $L$, and the order of the vertices in $L$ is the resulting topological sequence.

Let us first look at the pseudocode from [Wikipedia](https://en.wikipedia.org/wiki/Topological_sorting#Kahn's_algorithm)

???+ note "Implementation"
    ```text
    L ← Empty list that will contain the sorted elements
    S ← Set of all nodes with no incoming edges
    while S is not empty do
        remove a node n from S
        insert n into L
        for each node m with an edge e from n to m do
            remove edge e from the graph
            if m has no other incoming edges then
                insert m into S
    if graph has edges then
        return error (graph has at least one cycle)
    else
        return L (a topologically sorted order)
    ```

The core of the code is maintaining a set of vertices with in-degree 0.

See the following picture

![topo](images/topo-example.svg)

The result of sorting it is: 2 -> 8 -> 0 -> 3 -> 7 -> 1 -> 5 -> 6 -> 9 -> 4 -> 11 -> 10 -> 12

### Time complexity

For the graph $G = (V, E)$, initializing the set $S$ of vertices with in-degree $0$ already requires traversing the whole graph and checking every edge, which costs $O(E+V)$. Then the set is processed, which obviously also takes $O(E+V)$ time.

Hence the total time complexity is $O(E+V)$

### Implementation

=== "C++"
    ```cpp
    int n, m;
    vector<int> G[MAXN];
    int in[MAXN];  // stores the in-degree of every vertex
    
    bool toposort() {
      vector<int> L;
      queue<int> S;
      for (int i = 1; i <= n; i++)
        if (in[i] == 0) S.push(i);
      while (!S.empty()) {
        int u = S.front();
        S.pop();
        L.push_back(u);
        for (auto v : G[u]) {
          if (--in[v] == 0) {
            S.push(v);
          }
        }
      }
      if (L.size() == n) {
        for (auto i : L) cout << i << ' ';
        return true;
      }
      return false;
    }
    ```

=== "Python"
    ```python
    from collections import defaultdict, deque
    
    
    def topo_sort(graph):
        lst = []
        in_degree = defaultdict(int)
        for u in graph:
            for v in graph[u]:
                in_degree[v] += 1
    
        s = deque([u for u in graph if in_degree[u] == 0])
        while s:
            u = s.popleft()
            lst.append(u)
            for v in graph.get(u, []):
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    s.append(v)
    
        return None if any(in_degree.values()) else lst
    ```

## DFS algorithm

### Implementation

=== "C++"
    ```cpp
    using Graph = vector<vector<int>>;  // adjacency list
    
    struct TopoSort {
      enum class Status : uint8_t { to_visit, visiting, visited };
    
      const Graph& graph;
      const int n;
      vector<Status> status;
      vector<int> order;
      vector<int>::reverse_iterator it;
    
      TopoSort(const Graph& graph)
          : graph(graph),
            n(graph.size()),
            status(n, Status::to_visit),
            order(n),
            it(order.rbegin()) {}
    
      bool sort() {
        for (int i = 0; i < n; ++i) {
          if (status[i] == Status::to_visit && !dfs(i)) return false;
        }
        return true;
      }
    
      bool dfs(const int u) {
        status[u] = Status::visiting;
        for (const int v : graph[u]) {
          if (status[v] == Status::visiting) return false;
          if (status[v] == Status::to_visit && !dfs(v)) return false;
        }
        status[u] = Status::visited;
        *it++ = u;
        return true;
      }
    };
    ```

=== "Python"
    ```python
    from enum import Enum, auto
    
    
    class Status(Enum):
        to_visit = auto()
        visiting = auto()
        visited = auto()
    
    
    def topo_sort(graph: list[list[int]]) -> list[int] | None:
        n = len(graph)
        status = [Status.to_visit] * n
        order = []
    
        def dfs(u: int) -> bool:
            status[u] = Status.visiting
            for v in graph[u]:
                if status[v] == Status.visiting:
                    return False
                if status[v] == Status.to_visit and not dfs(v):
                    return False
            status[u] = Status.visited
            order.append(u)
            return True
    
        for i in range(n):
            if status[i] == Status.to_visit and not dfs(i):
                return None
    
        return order[::-1]
    ```

Time complexity: $O(E+V)$, space complexity: $O(V)$

### Proof of correctness

Consider a graph: if after deleting some vertex with in-degree $0$ the new graph can be topologically sorted, then so can the original graph. Conversely, if the original graph can be topologically sorted, so can the graph after the deletion.

### Applications

Topological sorting can decide whether a graph has a cycle, and also whether a graph is a chain. Topological sorting can be used to find the critical path of an AOE network and estimate the shortest completion time of a project.

### Lexicographically largest/smallest topological order

Just replace the queue in Kahn's algorithm with a priority queue implemented by a max-heap/min-heap; the total time complexity then becomes $O(E+V \log{V})$.

## Exercises

[CF 1385E](https://codeforces.com/problemset/problem/1385/E): a construction via topological sorting.

[Luogu P1347](https://www.luogu.com.cn/problem/P1347): topological sorting template.

## References

1.  Discrete Mathematics and Its Applications (Chinese edition). ISBN:9787111555391
2.  [Topological sorting - Wikipedia](https://en.wikipedia.org/wiki/Topological_sorting)
3.  [数据结构第九讲（图：拓扑排序，关键路径，最短路径）- Zhihu](https://zhuanlan.zhihu.com/p/164751109) (Data Structures, Lecture 9: graphs – topological sorting, critical path, shortest path)
