---
title: Monotonic stack
---

## Introduction

What is a monotonic stack? As the name suggests, a monotonic stack is a stack that satisfies a monotonicity property. Compared with a monotonic queue, elements enter and leave only at one end.

For convenience of description, the examples and pseudocode below maintain a monotonically increasing stack of integers.

## Procedure

### Insertion

When inserting an element into a monotonic stack, in order to maintain the monotonicity of the stack, we must pop the fewest elements possible subject to the whole stack being monotonic after the element is pushed on top.

For example, suppose the elements of the stack from top to bottom are $\{0,11,45,81\}$.

![](images/monotonic-stack-before.svg)

When inserting the element $14$, to preserve monotonicity we have to pop the elements $0,11$ in turn; after the operation the stack becomes $\{14,45,81\}$.

![](images/monotonic-stack-after.svg)

In pseudocode:

???+ note "Implementation"
    ```text
    insert x
    while !sta.empty() && sta.top()<x
        sta.pop()
    sta.push(x)
    ```

### Usage

Naturally, we read an element from the top of the stack; this element is one of the extremes with respect to the monotonicity.

In the example above, what we obtain is the minimum of the stack.

## Applications

??? note "[POJ3250 Bad Hair Day](http://poj.org/problem?id=3250)"
    There are $N$ cows standing in a row from left to right, and each cow has a height $h_i$. Suppose there are $c_i$ cows between the $i$-th cow from the left and "the first cow to its right with height $≥h_i$". Compute $\sum_{i=1}^{N} c_i$.

A rather basic application is this problem, a simple use of a monotonic stack: record the position at which each cow is popped (if it is never popped, take the far right end), and with a little processing we can compute the result the problem asks for.

In addition, a monotonic stack can also be used to solve the RMQ problem offline.

We sort all queries by their right endpoint, then each time scan the sequence from left to right up to the right endpoint of the current query, inserting the scanned elements into the monotonic stack. This way, whenever we answer a query, the values stored in the monotonic stack are exactly the candidates at positions $\le r$ that can be the answer, and these elements satisfy the monotonicity property. Then the first element in the monotonic stack whose position is $\ge l$ is the answer to the current query, and this step can be implemented with binary search. Solving RMQ with a monotonic stack has time complexity $O(q\log q + q\log n)$ and space complexity $O(n)$.

## Exercises

-   [Luogu P5788 【模板】单调栈](https://www.luogu.com.cn/problem/P5788)
-   [Luogu P1901 发射站](https://www.luogu.com.cn/problem/P1901)
