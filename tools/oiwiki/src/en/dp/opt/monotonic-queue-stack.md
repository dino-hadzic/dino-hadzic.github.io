---
title: Monotonic queue/monotonic stack optimization
---

## Introduction

Prerequisites: [monotonic queue](../../ds/monotonic-queue.md), [monotonic stack](../../ds/monotonic-stack.md).

A monotonic queue is mainly used to maintain the minimum/maximum of a range whose two endpoints move monotonically (non-decreasingly), while a monotonic stack is mainly used to find the first previous/next element greater/smaller than the current value.

???+ note "Note"
    -   To get the minimum, maintain a **strictly increasing/non-decreasing** monotonic queue/stack, and vice versa.
    -   When maintaining a strictly increasing/decreasing sequence, compare with **less than or equal/greater than or equal**; when maintaining a non-decreasing/non-increasing sequence, compare with **less than/greater than**.

## Steps of the monotonic queue optimization

-   Add the required elements: keep pushing elements into the monotonic queue until the current element reaches the right endpoint of the required range; this guarantees that all required elements are in the monotonic queue.
-   Pop the out-of-range front: a monotonic queue essentially maintains the minimum/maximum of all inserted elements, but we usually want the minimum/maximum of a range. So we pop the elements outside the left endpoint to guarantee that all elements in the monotonic queue are inside the required range.
-   Get the minimum/maximum: simply take the front of the queue as the answer.

## Steps of the monotonic stack optimization

-   Pop the invalid top: compare the current element with the top of the stack and pop the tops that violate the monotonic stack property. For example, for a strictly increasing stack (the top is the largest, the minimum is maintained), pop all elements of the stack that are greater than or equal to the current element.
-   Add the current element: simply push the current element onto the stack.

## Bounded knapsack with a monotonic queue

???+ note "Problem statement"
    You have $n$ items; the $i$-th item has weight $w_i$, value $v_i$ and there are $k_i$ copies of it. You have a knapsack with weight limit $W$, and you have to put items of the largest possible total value into it without exceeding the weight limit. Find the maximum value.

If you are not familiar with knapsack DP, read [knapsack DP](../knapsack/basic.md) first. Let $f_{i,j}$ be the maximum value obtainable from the first $i$ items in a knapsack of capacity $j$. The naive transition equation is

$$
f_{i,j}=\max_{k=0}^{k_i}(f_{i-1,j-k\times w_i}+v_i\times k)
$$

with time complexity $O(W\sum k_i)$.

Consider optimizing the transition for $f_i$. For convenience of notation, let $g_{x,y}=f_{i,x\times w_i+y},g'_{x,y}=f_{i-1,x\times w_i+y}$, where $0\le y \lt w_i$; then the transition equation can be written as:

$$
g_{x,y}=\max_{k=0}^{k_i}(g'_{x-k,y}+v_i\times k)
$$

Let $G_{x,y}=g'_{x,y}-v_i\times x$. Then the equation can be written as:

$$
g_{x,y}=\max_{k=0}^{k_i}(G_{x-k,y})+v_i\times x
$$

This is now the classical form suited for the monotonic queue optimization. $G_{x,y}$ can be computed in $O(1)$, so for a fixed $y$ we can compute all $g_{x,y}$ in $O\left( \left\lfloor \dfrac{W}{w_i} \right\rfloor \right)$ time. Therefore the complexity of computing all $g_{x,y}$ is $O\left( \left\lfloor \dfrac{W}{w_i} \right\rfloor \right)\times O(w_i)=O(W)$. Thus the total complexity of the transitions drops to $O(nW)$.

In the implementation we have to enumerate $y$ first, since only then can the monotonic queue be used while enumerating $x$; the monotonic queue stores $x-k$ rather than $k$, so the corresponding $G_{x-k,y}$ is obtained with `f[last][q.front() * w[i] + y] - q.front() * v[i]`. It is easy to see that $x-k\in [x - k_i,x]$, so while enumerating $x$ we have to remove the elements of the queue that are not in this range.

??? note "Reference code"
    ```cpp
    --8<-- "docs/dp/code/opt/monotonic-queue-stack/monotonic-queue-stack_2.cpp"
    ```

## Exercises

???+ note "Example [CF372C Watching Fireworks is Fun](http://codeforces.com/problemset/problem/372/C)"
    Problem summary: there are $n$ positions in a town and $m$ fireworks to be launched. The launch time of the $i$-th firework is $t_i$ and its position is $a_i$. If you are at position $x$ when a firework is launched, you gain $b_i-|a_i-x|$ happiness points.
    
    Initially you can be at any position, and in each unit of time you can move at most $d$ units of distance. Maximize the total happiness you can gain.

Let $f_{i,j}$ be the maximum happiness obtainable if you are at position $j$ when the $i$-th firework is launched.

Write down the state transition equation: $f_{i,j}=\max\{f_{i-1,k}+b_i-|a_i-j|\}$, where $j-(t_{i}-t_{i-1})\times d\le k\le j+(t_{i}-t_{i-1})\times d$.

Let us try to transform it:

Since a fixed constant $b_i$ appears inside the $\max$, we can move it outside.

$f_{i,j}=\max\{f_{i-1,k}+b_i-|a_i-j|\}=\max\{f_{i-1,k}-|a_i-j|\}+b_i$

If $i$ and $j$ are fixed, the value of $|a_i-j|$ is fixed too, so this part can also be moved outside.

Finally, the expression becomes:

$$
f_{i,j}=\max\{f_{i-1,k}-|a_i-j|\}+b_i=\max\{f_{i-1,k}\}-|a_i-j|+b_i
$$

Now consider the monotonic queue optimization. Since the $\max$ in the final expression depends only on the maximum of a contiguous segment of the previous state, when computing the states for a new $i$ we only need to build a monotonic queue from the previous $f_{i-1}$ and maintain it so that the value of $\max\{f_{i-1,k}\}$ is obtained in amortized $O(1)$ time, and then compute $f_{i,j}$ by the formula.

The total time complexity is $O(nm)$.

??? note "Reference code"
    ```cpp
    --8<-- "docs/dp/code/opt/monotonic-queue-stack/monotonic-queue-stack_1.cpp"
    ```

-   ["Luogu P1886" Sliding window](https://loj.ac/problem/10175)
-   ["NOI2005" Magnificent waltz](https://www.luogu.com.cn/problem/P2254)
-   ["SCOI2010" Stock trading](https://loj.ac/problem/10183)
