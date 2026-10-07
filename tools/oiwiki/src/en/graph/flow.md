---
title: Introduction to network flow
---

This page introduces the basic concepts related to network flow.

## Overview

A **network** is a special directed graph $G=(V,E)$ that differs from an ordinary directed graph in that it has capacities and a source and a sink.

-   Every edge $(u, v)$ in $E$ has a weight called its **capacity**, denoted $c(u, v)$. When $(u,v)\notin E$, we may assume $c(u,v)=0$.

-   $V$ contains two special vertices: the **source** $s$ and the **sink** $t$ ($s \neq t$).

For a network $G=(V, E)$, a **flow** is a function from the edge set $E$ to the integers or the reals that satisfies the following properties.

1.  Capacity constraint: for every edge, the flow through it must not exceed its capacity, i.e. $0 \leq f(u,v) \leq c(u,v)$;
2.  Flow conservation: for every vertex $u$ other than the source and the sink, the net flow is $0$. Here we define the net flow of $u$ as $f(u) = \sum_{x \in V} f(u, x) - \sum_{x \in V} f(x, u)$.

For a network $G = (V, E)$ and a flow $f$ on it, we define the **value** $|f|$ of $f$ as the net flow of the source, $f(s)$. As a corollary of flow conservation, this also equals the negative of the net flow of the sink, $-f(t)$.

For a network $G = (V, E)$, if $\{S, T\}$ is a partition of $V$ (i.e. $S \cup T = V$ and $S \cap T = \varnothing$) with $s \in S, t \in T$, we call $\{S, T\}$ an **$s$-$t$ cut** of $G$. We define the capacity of the $s$-$t$ cut $\{S, T\}$ as $||S, T|| = \sum_{u \in S} \sum_{v \in T} c(u, v)$.

## Common problems

Common network flow problems include, but are not limited to, the following types.

-   Maximum flow problem: for a network $G = (V, E)$, assign a flow to every edge so as to obtain a flow $f$ whose value is as large as possible. Such an $f$ is called a **maximum flow** of $G$.
-   Minimum cut problem: for a network $G = (V, E)$, find an $s$-$t$ cut $\{S, T\}$ whose total capacity is as small as possible. That total capacity is called the **minimum cut** of $G$.
-   Minimum-cost maximum-flow problem: in a network $G = (V, E)$, every edge is additionally given a weight $w(u, v)$ called its **cost**, meaning the price paid by one unit of flow passing through $(u, v)$. Among all maximum flows of $G$, the one with the smallest total cost is called the **minimum-cost maximum flow**.

We will cover each of them in detail in later chapters.

## Example: the "24 network flow problems"

The "24 network flow problems" (网络流 24 题) is a problem list widely circulated on the Chinese internet ([LibreOJ](https://loj.ac/problems/tag/30)/[Luogu](https://www.luogu.com.cn/problem/list?tag=332)) that has existed since at least around 2010. The list introduces some classic techniques for modeling other problems as network flow problems. Owing to the limitations of its time, these are not necessarily the most representative network flow problems, but they are still worth a look for readers serious about algorithm competitions.
