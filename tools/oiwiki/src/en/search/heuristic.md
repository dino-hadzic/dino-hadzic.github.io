---
title: Heuristic search
---

This page briefly introduces heuristic search and its usage.

## Definition

Heuristic search is a search algorithm that adds a heuristic function on top of an ordinary search algorithm.

The role of the heuristic function is to evaluate every branch choice of the search based on the information already available, and then to choose a branch. Simply put, heuristic search analyzes both "take" and "do not take", and from that picks the better solution or discards useless ones.

## Worked example

Since the concept is rather abstract, we explain it with an example.

???+ note "["NOIP2005 Junior" Herb Gathering](https://www.luogu.com.cn/problem/P1048)"
    Problem summary: there are $N$ kinds of items and a knapsack of capacity $W$. Each kind of item has a weight $w_i$ and a value $v_i$. Choose several items (each kind at most once) to put into the knapsack so that the total value of the items in the knapsack is maximized and their total weight does not exceed the capacity of the knapsack.

??? note "Solution idea"
    We write an evaluation function $f$ that can prune all useless "$0$" branches (that is, prune a large number of useless "do not take" branches).
    
    The evaluation function $f$ works as follows:
    
    When taking an item, we check whether the given capacity is exceeded (feasibility pruning); when not taking it, we check whether the total value of all remaining herbs + the current value is greater than the best solution found so far (optimality pruning).

??? note "Sample code"
    ```cpp
    --8<-- "docs/search/code/heuristic/heuristic_1.cpp"
    ```
