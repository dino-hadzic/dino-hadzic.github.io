---
title: Stoer–Wagner algorithm
---

## Definitions

Since we drop the notion of a **source and sink**, we need to redefine the concept of a **cut**.

(In fact, the definition of a cut in the network flow chapters does not match Wikipedia's; it is only because the cuts one usually meets are the "minimum cut problem with source and sink" that this usage has become conventional.)

### Cut

A set of edges whose removal makes a flow network disconnected (i.e. splits it into two subgraphs) is called a cut of the graph.

That is: in an undirected graph $G = (V, E)$, let $C$ be a set of arcs of $G$; if deleting all arcs in $C$ from $G$ makes $G$ disconnected, $C$ is called a cut of $G$.

### Minimum cut problem with source and sink

Same as the definition in [Minimum cut](./flow/min-cut.md).

### Minimum cut problem without source and sink

The cut whose arcs have the smallest total weight. Also called the **global minimum cut**.

Obviously, the complexity of running a network flow directly is not acceptable here.

***

## Stoer–Wagner algorithm

### Introduction

The Stoer–Wagner algorithm was proposed in 1995 by *Mechthild Stoer* and *Frank Wagner*; it is an algorithm that solves the global minimum cut problem on **undirected graphs with positive weights** by **recursion**.

### Properties

The algorithm's complexity is $O(|V||E| + |V|^{2}\log|V|)$, usually approximated as $O(|V|^3)$.

Its implementation rests on the following basic fact: let $S, T$ be any two vertices of the graph $G$. Then for any cut $C$ of $G$, either $S, T$ lie in the same connected component, or $C$ is an ${S-T}$ cut.

### Procedure

1.  Pick any two vertices $s, t$ in $G$, take them as source and sink and compute the $S-T$ minimum cut of $G$ (call it the *cut of phase*); update the current answer.
2.  "Merge" the vertices $s, t$; if $|V|$ in $G$ is greater than $1$, go back to step 1.
3.  Output the minimum over all *cuts of phase*.

Merging two vertices $s, t$: delete the edge $(s, t)$ between $s$ and $t$; for every vertex $k$ in $G \setminus \{s, t\}$, delete $(t, k)$ and add its weight $d(t, k)$ to $d(s, k)$.

Explanation: if $s, t$ are in the same connected component, then for a vertex $k$ in $G \setminus \{s, t\}$, if $(k, s) \in C_{\min}$, then necessarily $(k, t) \in C_{\min}$ as well; otherwise, since $s, t$ are connected and $k, t$ are connected, $s, k$ would be in the same component, and then $C = C_{\min} \setminus \{(t, k)\}$ would be better than $C_{\min}$. And vice versa. Hence $s, t$ can be regarded as a single vertex.

Step 1 handles the case where $s,t$ are not in the same component, and step 2 handles the remaining cases. Since every execution of step 2 decreases $|V|$ by $1$, the algorithm terminates after $|V| - 1$ rounds.

### Computing the S-T minimum cut

(Obviously not with network flow.)

Suppose that after several merges the current graph is $G'=(V', E')$ and we perform step 1.

We build a set $A$, initially $A = \varnothing$.

Each time we add to $A$ the vertex of $V'$ with $i \notin A$ that maximizes the weight function $w(A, i)$, until $|A| = |V'|$.

Here the weight function is defined as:

$w(A, i) = \sum_{j \in A} d(i, j)$

(if $(i, j) \notin E'$, then $d(i, j) = 0$).

It is easy to see that the order in which vertices join $A$ is fixed; let $\operatorname{ord}(i)$ denote the $i$-th vertex added to $A$, $t = \operatorname{ord}(|V'|)$; and let $\operatorname{pos}(v)$ denote the size of $|A|$ after $v$ is added to $A$, i.e. the order in which $v$ was added.

Then for any vertex $s$, one cut between $s$ and $t$ is $w(t)$.

### Proof

A vertex $v$ is said to be activated if and only if, at the time $v$ joins $A$, the last vertex $u$ currently in $A$ joined earlier than $v$, and in the graph $G'' = (V', E'/C)$, $u$ and $v$ are not in the same connected component.

![Stoer-Wagner1](./images/Stoer-Wagner1.png)

In the figure, the blue and yellow regions are two different connected components, and the numbers in square brackets are the order of joining $A$. Gray vertices are active vertices, white ones are not.

Define $A_v = \{u \mid \operatorname{pos}(u) < \operatorname{pos}(v)\}$, i.e. the vertices added to $A$ strictly before $v$, and let $E_v$ be the edge set of the subgraph of $E'$ induced by the vertex set $A_v \cup\{v\}$. (Note that it includes the vertex $v$.)

Define the induced cut $C_v$ as $C \cap E_v$. $w(C_v) = \sum_{(i,j) \in C_v} d(i, j)$.

???+ note "Lemma 1"
    For every activated vertex $v$, $w(A_v, v) \le w(C_v)$.
    
    Proof: by mathematical induction.
    
    For the first activated vertex $v_0$, by definition $w(A_{v_0}, v_0) = w(C_{v_0})$.
    
    For two later activated vertices $u, v$, assuming $\operatorname{pos}(v) < \operatorname{pos}(u)$, we have:
    
    $w(A_u, u) = w(A_v, u) + w(A_u - A_v, u)$
    
    Moreover, we know:
    
    $w(A_v, u) \le w(A_v, v)$ and $w(A_v, v) \le w(C_v)$; combining them gives:
    
    $w(A_u, u) \le w(C_v) + w(A_u - A_v, u)$
    
    Since $w(A_u - A_v, u)$ contributes to $w(C_u)$ but not to $w(C_v)$, with all edge weights positive we can derive:
    
    $w(A_u,u) \le w(C_u)$
    
    This completes the induction.

Since $\operatorname{pos}(s) < \operatorname{pos}(t)$ and $s, t$ are not in the same connected component, $t$ will be activated, from which we get $w(A_t, t) \le w(C_t) = w(C)$.

??? note "[P5632 [Template] Stoer–Wagner algorithm](https://www.luogu.com.cn/problem/P5632)"
    ```cpp
    --8<-- "docs/graph/code/stoer-wagner/stoer-wagner_1.cpp"
    ```

***

### Complexity analysis and optimizations

The complexity of the *contract* operation is $O(|E| + |V|\log|V|)$.

A total of $O(|V|)$ *contract* operations are performed, for a total complexity of $O(|E||V| + |V|^2\log|V|)$.

Going by experience with [shortest paths](./shortest-path.md), the bottleneck of the algorithm is finding the vertex with the largest weight.

In one *contract* we need to fetch the top of the heap $|V|$ times and increase weights $|E|$ times.

A Fibonacci heap can do the top fetch in $O(\log|V|)$ and the increase in $O(1)$, so the theoretical complexity can reach $O(|E| + |V|\log|V|)$; however, because of the Fibonacci heap's large constant factor and code size, its practical value is low.

(In actual tests you need O2 and some luck with judge fluctuations to pass.)
