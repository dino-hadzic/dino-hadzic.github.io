---
title: Flows with lower and upper bounds
---

Before reading this article, please read [Maximum flow](./max-flow.md) and make sure you are fluent with maximum flow algorithms.

## Overview

A flow with lower and upper bounds (bounded flow) essentially means that every edge of the flow network has an upper bound $c(u,v)$ and a lower bound $b(u,v)$ on its flow. That is, a feasible flow must satisfy $b(u,v) \leq f(u,v) \leq c(u,v)$. At the same time, flow conservation must hold at every vertex other than the source and the sink.

Depending on what a problem asks for, we can use bounded flows to solve different problems.

## Feasible flow without source and sink

Given a flow network $G$ without source and sink, we ask whether there is a way to assign a flow to every edge such that the flow of every edge satisfies its bounds and flow conservation holds at every vertex.

Suppose every edge already carries $b(u,v)$ units of flow; call this the initial flow. At the same time, in a new graph we add an edge from $u$ to $v$ with capacity $c(u,v) - b(u,v)$. We then make adjustments on the new graph.

Since a maximum flow requires the initial flow to satisfy conservation (a maximum flow can be viewed as a bounded maximum flow with lower bounds $0$), but the constructed initial flow very likely does not satisfy conservation, suppose that for some vertex the initial inflow minus the initial outflow equals $M$.

If $M=0$, the flow is conserved and no extra edge is needed.

If $M>0$, the inflow is too large, so we create an extra source $S'$ and add an extra edge of capacity $M$ from $S'$ to this vertex.

If $M<0$, the outflow is too large, so we create an extra sink $T'$ and add an extra edge of capacity $-M$ from this vertex to $T'$.

If the extra edge is saturated, the conservation condition at this vertex can be satisfied; otherwise it cannot. (Because only the original graph together with the extra flow satisfies conservation in the original graph.)

After building the graph, run a maximum flow from $S'$ to $T'$. If all edges leaving $S'$ are saturated, a feasible flow exists; otherwise it does not.

### Example

???+ note "[Luogu P14578 [Template] Feasible bounded flow without source and sink](https://www.luogu.com.cn/problem/P14578)"
    A directed graph $G$ with $n$ vertices and $m$ directed edges; every edge has a lower bound $l_i$ and an upper bound $r_i$ on its flow.
    
    Construct an assignment such that the flow $w_i$ of every edge satisfies the constraint $l_i\leq w_i\leq r_i$ and flow is conserved at every vertex, i.e. the inflow of every vertex equals its outflow. Or report that there is no solution.

??? note "Sample code"
    ```cpp
    --8<-- "docs/graph/code/flow/bound/bound_1.cpp"
    ```

## Feasible flow with source and sink

Given a flow network $G$ with source and sink, we ask whether there is a way to assign a flow to every edge such that the flow of every edge satisfies its bounds and flow conservation holds at every vertex other than the source and the sink.

Let the source be $S$ and the sink be $T$.

Then we can add an edge from $T$ to $S$ with upper bound $\infty$ and lower bound $0$, reducing the problem to a feasible flow without source and sink.

If a solution exists, the value of the feasible flow from $S$ to $T$ equals the flow on the extra edge from $T$ to $S$.

## Maximum flow with source and sink

Given a flow network $G$ with source and sink, we ask whether there is a way to assign a flow to every edge such that the flow of every edge satisfies its bounds and flow conservation holds at every vertex other than the source and the sink. If so, we ask for the maximum flow value satisfying these constraints.

Find any feasible flow in the network. If none exists, we can stop right away.

Otherwise, consider the residual network after deleting all extra edges and make adjustments on it.

Run another maximum flow from $S$ to $T$ on the residual network; the answer is the value of the feasible flow plus this maximum flow.

??? warning "A very easy mistake to make"
    The maximum flow from $S$ to $T$ is run directly on the residual network left after computing the feasible flow with source and sink.
    
    It must never be run on the original flow network.

## Minimum flow with source and sink

Given a flow network $G$ with source and sink, we ask whether there is a way to assign a flow to every edge such that the flow of every edge satisfies its bounds and flow conservation holds at every vertex other than the source and the sink. If so, we ask for the minimum flow value satisfying these constraints.

Similarly, we consider pushing the unneeded flow back in the residual network.

Find any feasible flow in the network. If none exists, we can stop right away.

Otherwise, consider the residual network after deleting all extra edges.

Run another maximum flow from $T$ to $S$ on the residual network; the answer is the value of the feasible flow minus this maximum flow.

??? note "[AHOI 2014 Side Stories](https://loj.ac/problem/2226)"
    For every story edge from $x$ to $y$ with cost $v$, set the upper bound to $\infty$ and the lower bound to $1$.
    
    For every vertex, add an edge to $T$ with cost $c$, upper bound $\infty$ and lower bound $1$.
    
    The vertex $S$ is vertex number $1$.
    
    It suffices to run a minimum-cost feasible bounded flow with source and sink once.
    
    Since the minimum-cost feasible flow is solved similarly to the minimum feasible flow, we do not expand on it here.
