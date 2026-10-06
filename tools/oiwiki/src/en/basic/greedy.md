---
title: Greedy algorithms
---

This page briefly introduces greedy algorithms.

## Introduction

A **greedy algorithm** uses the computer to simulate the decision process of a "greedy" person. This person is extremely greedy: at every step they choose the operation that is best according to some criterion. They are also short-sighted: they only look at what is in front of them and never consider the consequences that may follow.

As one might expect, greedy methods do not always yield the optimal solution, so whenever you use one you should make sure you can prove its correctness.

## Explanation

### Scope of application

Greedy algorithms are especially effective on problems with optimal substructure. Optimal substructure means the problem can be decomposed into subproblems, and the optimal solutions of the subproblems lead to the optimal solution of the whole problem.[^ref1]

### Proof

Common proof techniques are the exchange argument and mathematical induction; the two can also be combined.

1.  Exchange argument: start from an arbitrary optimal solution and, through a finite number of exchanges or replacements that preserve feasibility and do not worsen the objective, transform it into the solution produced by the greedy algorithm, thus proving that the greedy solution is also optimal. The proof is often written by contradiction.
2.  Induction: first compute the optimal solution $F_1$ of the boundary case (e.g. $n = 1$), then prove that for every $n$, $F_{n+1}$ can be derived from $F_{n}$.

## Key points

### Common problem types

In problems up to the "提高组" (NOIP senior) level, two kinds of greedy are most common.

-   Sort XXX in some order, then pick in some order (e.g. from smallest to largest).
-   Each time take the largest/smallest item in XXX and update XXX. (Sometimes taking the maximum/minimum can be optimised, e.g. by maintaining a priority queue.)

The difference is that the former is always offline – process first, then choose; the latter may be online – choose while processing.

### Sorting-based solutions

The sorting / adjacent-swap method typically appears when the input is an array with a few (usually one or two) weights, and the optimum is found by sorting and then simulating a pass.

???+ note "Example [NOIP 2012 King's Game](https://www.luogu.com.cn/problem/P1080)"
    For the National Day of country H, the king invites $n$ ministers to play a game with prizes. First, each minister writes an integer on each of his left and right hands, and the king also writes an integer on each of his hands. Then the $n$ ministers line up, with the king at the front. After lining up, every minister receives a number of gold coins from the king: the product of the numbers on the left hands of everyone in front of him, divided by the number on his own right hand, rounded down.
    
    The king does not want any minister to receive an especially large reward, so he asks you to rearrange the queue so that the minister with the largest reward gets as little as possible. Note that the king is always at the front of the queue.

??? note "Solution idea"
    Let the $i$-th minister in the current order have the numbers $a_i, b_i$ on his left and right hands. We derive the greedy strategy using the adjacent-swap method.
    
    Ignore the rounding for now and let $s$ be the product of the $a_i$ of everyone in front of the $i$-th minister. Before swapping, the larger reward among the two is
    
    $$
    \dfrac{s}{b_i b_{i+1}}\max(b_{i+1},a_i b_i),\tag{1}
    $$
    
    and after swapping it is
    
    $$
    \dfrac{s}{b_i b_{i+1}}\max(b_i,a_{i+1}b_{i+1}).\tag{2}
    $$
    
    If $a_i b_i\le a_{i+1}b_{i+1}$, then since $b_{i+1}\le a_{i+1}b_{i+1}$, expression $(1)$ is not larger than expression $(2)$. Rounding down is monotone and $\max(\lfloor u\rfloor,\lfloor v\rfloor)=\lfloor\max(u,v)\rfloor$, so swapping the two does not decrease the maximum reward. Therefore sorting in ascending order of $a_i b_i$ is optimal.
    
    In the implementation we store the two input numbers in a struct and overload the operator:
    
    ```cpp
    struct uv {
      int a, b;
    
      bool operator<(const uv& x) const { return 1LL * a * b < 1LL * x.a * x.b; }
    };
    ```

### "Regret" solutions

The idea: tentatively accept the new option; if a constraint conflict occurs, undo the option in the chosen set that is worst by the greedy criterion. The strategy still needs a proof of correctness.

???+ note "Example [\"USACO09OPEN\" Work Scheduling](https://www.luogu.com.cn/problem/P2949)"
    John's working day starts at time $0$ and has $10^9$ units of time. In any unit of time he can choose to complete any one of the $N(1 \leq N \leq 10^5)$ jobs numbered $1$ to $N$. Job $i$ has deadline $D_i(1 \leq D_i \leq 10^9)$ and yields profit $P_i( 1\leq P_i\leq 10^9 )$ when completed. Given the profits and deadlines, find the maximum profit John can obtain.

??? note "Solution idea"
    1.  First assume every job is done; sort the jobs by deadline and push them into the queue;
    2.  when deciding whether to do job `i`, if its deadline allows, compare it with the element in the queue with the smallest profit; if job `i` pays more (regret), then `ans += a[i].p - q.top()`.  
        Use a priority queue (min-heap) to keep the minimum at the front.
    3.  The condition `a[i].d<=q.size()` can be understood as follows: in the period from 0 to `a[i].d` at most `a[i].d` jobs can be done; if `q.size()>=a[i].d`, then the time to finish `q.size()` jobs is at least `a[i].d`, so when job `i` is more profitable, the least profitable job should be swapped out of the priority queue.

??? note "Sample code"
    === "C++"
        ```cpp
        --8<-- "docs/basic/code/greedy/greedy_1.cpp"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/basic/code/greedy/greedy_1.py"
        ```

??? note "Complexity analysis"
    -   Space complexity: for $n$ jobs we use $n$ elements of the array $a$, and the priority queue holds at most $n$ elements, so the space complexity is $O(n)$.
    -   Time complexity: `std::sort` takes $O(n\log n)$, maintaining the priority queue takes $O(n\log n)$; in total $O(n\log n)$.

## Difference from dynamic programming

Ordinary greedy relies on local choices that can be proven safe; dynamic programming maintains the optimal value of every state and compares candidate transitions.

## Exercises

-   ["USACO1.3" Barn Repair](https://www.luogu.com.cn/problem/P1209)
-   [Luogu P2123 Queen's Game](https://www.luogu.com.cn/problem/P2123)
-   [Problems tagged greedy on LeetCode](https://leetcode-cn.com/tag/greedy/)

## References and notes

[^ref1]: [Greedy algorithm – Wikipedia](https://en.wikipedia.org/wiki/Greedy_algorithm)
