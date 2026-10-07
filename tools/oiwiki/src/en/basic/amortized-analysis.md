---
title: Amortized complexity
---

Prerequisites: [Time complexity](./complexity.md)

This page introduces the basics of amortized complexity.

## Introduction

Amortized analysis is a technique for analyzing the performance of algorithms and dynamic data structures. Instead of looking only at the cost of a single operation, it evaluates the average cost of a sequence of operations and thus gives a more accurate picture of the overall performance. Amortized analysis does not involve probability; it only guarantees the average time per operation in the worst case and says nothing about the average performance of the system. In the worst case, amortized analysis spreads the cost of expensive operations over cheap ones and thereby ensures that the average cost of all operations stays within reasonable bounds.

Amortized analysis is usually carried out with one of three main methods: aggregate analysis, the accounting method and the potential method. Each has a different emphasis and suits different situations, but their common goal is to balance the costs of operations and thus optimize the overall worst-case performance of a data structure.

## Content

Consider a growable array, e.g. `vector` in C++, with initial capacity $m = 1$. Whenever a new element is inserted and the array is full, the size of the array has to be doubled, the elements of the old array copied into the new one, and only then is the new element inserted.

Below we take insertion into a dynamic array as an example and analyze its amortized cost with the three methods: aggregate analysis, the accounting method and the potential method.

### Aggregate analysis

Aggregate analysis computes the total cost of a sequence of operations and averages it over the operations, which yields the amortized time complexity per operation.

For the dynamic array, first note the two key costs of an insertion:

-   if the array is not full, an insertion costs $O(1)$;
-   if the array is full, the insertion requires growing the array, and copying the elements after growing costs $O(m)$, where $m$ is the current size of the array.

Therefore the total cost of $n$ insertions can be computed in two parts:

1.  **Cost of the insertions**: the direct cost of inserting each new element is constant time $O(1)$, so for $n$ operations the total cost is $O(n)$;
2.  **Cost of growing the array**: every growth involves copying the elements of the old array into the new one. These operations happen when the size of the array is a power of $2$. The old capacities copied during growth sum to the sum of all powers of $2$ strictly less than $n$; for $n\ge1$ the total copying cost is $\sum_{i=0}^{\lceil\log_2 n\rceil - 1}2^i=2^{\lceil\log_2 n\rceil}-1<2n$, i.e. $O(n)$.

Hence the total insertion cost of this array is $O(n)$, and the amortized cost per operation is $O(1)$. Even in the worst case, the average cost of an insertion is still constant time.

### Accounting method

The accounting method assigns each operation a fixed amortized cost in advance and ensures that the total cost of all operations never exceeds the sum of these pre-assigned costs. The accounting method resembles a **prepayment** mechanism: cheaper operations store part of their charge to pay for expensive operations in the future.

For the dynamic array, we can assign each insertion a fixed amortized cost so that, by the time growth is needed, enough charge has already been saved.

1.  **Allocating the charge**:
    -   Suppose the actual cost of each insertion is $1$ and set the amortized cost to $3$.
    -   Of this, $1$ pays for the current insertion and $2$ is saved for a possible future growth.

2.  **Using the charge**:
    -   When the array is full it has to grow; the actual cost is $O(m)$, where $m$ is the current size of the array.
    -   Suppose the array has $n$ elements before growing. Since the $n/2$ elements in the back half of the array saved a total of $n$ units of amortized cost when they were inserted, this is exactly enough to pay for the growth.

Here is a concrete example:

```text
Initial state:
arr    = [1, 2, 3, 4]  // initial array
amount = [2, 2, 2, 2]  // charge saved with each element

// First growth: the array is full and has to grow
arr    = [1, 2, 3, 4, null, null, null, null]  // array after growing
amount = [2, 2, 0, 0, 0, 0, 0, 0]  // the charges of 3 and 4 pay for the growth

// Keep inserting new elements until the array is full again
arr    = [1, 2, 3, 4, 5, 6, 7, 8]  // keep filling the array
amount = [2, 2, 0, 0, 2, 2, 2, 2]  // newly inserted elements also save a charge

// Second growth: the array is full again and needs more space
arr    = [1, 2, 3, 4, 5, 6, 7, 8, null, null, null, null, null, null, null, null]  // array after growing
amount = [2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  // the charges of 5, 6, 7 and 8 pay for the growth
```

The process above shows that the amortized cost saved by each insertion is enough to pay for future growth, which keeps the amortized cost of every operation at $O(1)$.

### Potential method

The potential method defines a potential function (usually denoted $\Phi$) that measures the **potential energy** of the data structure, i.e. the reserved resources in the state of the system that can be used to pay for expensive operations in the future. Changes in potential balance the total cost of the sequence of operations, which ensures that the amortized cost of the whole algorithm stays within reasonable bounds.

#### Principle

First, define the **state** $S$ as the state of the data structure at some moment; it may include the number of elements, the capacity, pointers and so on. The initial state, i.e. the state before any operation, is denoted $S_0$.

Second, define the potential function $\Phi(S)$, which measures the potential of state $S$ of the data structure. With initial state $S_0$, the potential of every reachable state $S$ must satisfy $\Phi(S) \geq \Phi(S_0)$[^clemson][^uci][^stanford]; some sources additionally require $\Phi(S_0)=0$[^cornell], which is actually unnecessary.

For each operation, its amortized cost $\hat{c}$ is defined as:

$$
\hat{c} = c + \Phi(S') - \Phi(S)
$$

where $c$ is the actual cost of the operation and $S$ and $S'$ are the states of the data structure before and after the operation. The formula says that the amortized cost equals the actual cost plus the change in potential. If the operation increases the potential (i.e. $\Phi(S') > \Phi(S)$), the amortized cost goes up; if the operation consumes potential (i.e. $\Phi(S') < \Phi(S)$), the amortized cost goes down.

We can use the potential function to analyze the total cost of a sequence of operations. Let $S_1, S_2, \dots, S_m$ be the sequence of states produced from the initial state $S_0$ by $m$ operations, and let $c_i$ be the actual cost of the $i$-th operation. Then the amortized cost $p_i$ of the $i$-th operation is:

$$
p_i = c_i + \Phi(S_i) - \Phi(S_{i-1})
$$

Therefore the total time spent on the $m$ operations is:

$$
\sum_{i=1}^m c_i = \sum_{i=1}^m p_i + \Phi(S_0) - \Phi(S_m)
$$

Since $\Phi(S) \geq \Phi(S_0)$, an upper bound on the total time is:

$$
\sum_{i=1}^m p_i \geq \sum_{i=1}^m c_i
$$

Hence, if $p_i = O(T(n))$, then $O(T(n))$ is an upper bound on the amortized complexity.

#### Example: analysis of growing a dynamic array

Take insertion into the dynamic array `vector` as an example, denote the initial state by $h_0$ and define the following potential function $\Phi(h)$:

$$
\Phi(h) = 2n - m
$$

where $n$ is the number of elements in the array and $m$ is its current capacity. Changes in this potential function reflect the increase and decrease of the prepaid charge for future growth. In the initial state of an empty array with capacity $1$, $\Phi(h_0)=-1$; in every nonempty reachable state (insertions only, doubling when full) we have $m\leq 2n$, hence $\Phi(h)\geq 0>\Phi(h_0)$.

1.  **Insertion (no growth needed)**:
    -   **Cost of the operation**: $O(1)$, since only one element is inserted.
    -   **Change in potential**: after the insertion the number of elements increases by 1 and the potential increases by $2$.
        -   $\Phi(h') - \Phi(h) = 2(n + 1) - m - (2n - m) = 2$.
    -   **Amortized cost**: $1 + 2 = 3$.

2.  **Insertion (triggers growth)**:
    -   Suppose the current capacity is $m = n$; inserting a new element triggers growth and the new capacity becomes $2n$.
    -   **Cost of the operation**: $O(n)$, since all elements have to be copied into the new array and the new element inserted.
    -   **Change in potential**: after growing and inserting, the potential changes by $2-n$, which is a decrease only when $n>2$.
        -   $\Phi(h') - \Phi(h) = 2(n + 1) - 2n - (2n - n) = 2 - n$.
    -   **Amortized cost**: $n + 1 + (2 - n) = 3$.

The analysis shows that, although the actual cost of growing is high, thanks to the design of the potential function the overall amortized cost still stays constant, $O(1)$.

## Extended example: stack operations

Stack operations are one of the classic applications of amortized analysis. Suppose we start from an empty stack, `pop` is only called on a nonempty stack, and the stack `S` supports the following three operations:

| Operation        | Description                                | Actual cost $c_i$           |
| ---------------- | ------------------------------------------ | --------------------------- |
| `S.push(x)`      | push element $x$ onto the stack            | $1$                         |
| `S.pop()`        | pop the top element of the stack           | $1$                         |
| `S.multi-pop(k)` | pop at most $k$ elements from the top      | $O(\min(\lvert S\rvert,k))$ |

We will analyze the amortized cost of these stack operations with the three methods: aggregate analysis, the accounting method and the potential method.

### Aggregate analysis

Aggregate analysis computes the total cost of all operations and spreads it evenly over every operation, which yields the amortized cost.

1.  For $n_{\text{push}}$ `push(x)` operations, each costs $O(1)$, so the total cost is $O(n_{\text{push}})$;
2.  for $n_{\text{pop}}$ `pop()` operations, each costs $O(1)$, so the total cost is $O(n_{\text{pop}})$;
3.  for $n_{\text{multi-pop}}$ `multi-pop(k)` operations, although the actual cost of each is $O(\min(\lvert S \rvert, k))$, the number of elements popped by these operations cannot exceed the number of elements previously pushed by `push(x)`, so the total cost is still bounded by $n_{\text{push}}$.

The total number of operations is $n=n_{\text{push}}+n_{\text{pop}}+n_{\text{multi-pop}}$, and $n_{\text{push}}\le n$. Every element is pushed at most once and popped at most once, so the total cost charged per element is $O(n_{\text{push}})=O(n)$; even if we separately count the constant checking overhead of each call, the total cost is still $O(n)$, and the amortized cost is $O(1)$.

### Accounting method

The accounting method reserves part of the charge of each `push(x)` to pay for possible future `pop()` or `multi-pop(k)` operations.

1.  **`S.push(x)`**: suppose the amortized cost of each `push(x)` is $2$; $1$ unit pays for the current operation and the other $1$ unit is stored as a charge to pay for a future `pop()` or `multi-pop(k)`;
2.  **`S.pop()`**: the actual cost is $1$, but the earlier `push(x)` already saved $1$ unit of charge for it, so the amortized cost is $0$;
3.  **`S.multi-pop(k)`**: the actual cost of each popped element is $1$ and can be paid from the charge saved by the `push(x)` of that element, so the amortized cost is $0$.

By this analysis, the charge saved when an element is pushed is enough to pay for popping that element later, so the amortized cost of every operation is $O(1)$.

### Potential method

The potential method defines a potential function to measure the state of the stack and uses changes in potential to balance the costs of the operations.

1.  **Potential function**: let $\Phi(h)$ be the number of elements on the stack, i.e. $\Phi(h) = \lvert S \rvert$. Each element contributes $1$ unit of potential;
2.  **`S.push(x)`**: each `push(x)` increases the number of elements on the stack, the potential increases by $1$, so the amortized cost is $1 + 1 = 2$;
3.  **`S.pop()`**: each `pop()` decreases the number of elements on the stack, the potential decreases by $1$, so the amortized cost is $1 - 1 = 0$;
4.  **`S.multi-pop(k)`**: let $t=\min(\lvert S\rvert,k)$; `multi-pop(k)` actually pops $t$ elements, the potential decreases by $t$, so the amortized cost charged per element is $t-t=0$; counting the call overhead it is $O(1)$.

With this potential function, the amortized cost of `push(x)` is $2$, while the amortized cost of `pop()` and `multi-pop(k)` is $0$. Hence the amortized cost of all stack operations is $O(1)$.

## References and notes

-   [Amortized Analysis - Wikipedia](https://en.wikipedia.org/wiki/Amortized_analysis)

[^clemson]: [Clemson University - Amortized Analysis + Splay Trees](https://people.computing.clemson.edu/~srimani/8380_F22/Course_Materials_Web/5_F22_Amortized%20Analysis%2BSplay%20Trees.pdf#page=8)

[^uci]: [UC Irvine - Amortized Analysis](https://ics.uci.edu/~goodrich/teach/cs263/notes/02-Amortized.pdf#page=5)

[^stanford]: [Stanford CS166 - Amortized Analysis](https://web.stanford.edu/class/archive/cs/cs166/cs166.1206/lectures/07/Small07.pdf#page=69)

[^cornell]: [Cornell CS 3110 - Lecture 20: Amortized Analysis](https://www.cs.cornell.edu/courses/cs3110/2011sp/Lectures/lec20-amortized/amortized.htm)
