---
title: Monotonic queue
---

## Introduction

Before learning about the monotonic queue, let us look at an example problem.

???+ note "Example problem"
    [Sliding Window](http://poj.org/problem?id=2823)
    
    The problem essentially says: given an array of length $n$, output the maximum and the minimum of every $k$ consecutive numbers.

The most brute-force idea is simple: for every segment $i \sim i+k-1$ of the sequence, compare the elements one by one to find the maximum (and the minimum); the time complexity is about $O(n \times k)$.

Obviously a lot of work is repeated here: except for the first $k-1$ and the last $k-1$ numbers, every number is compared $k$ times, and $100\%$ of the test data in the problem has $n \le 1000000$, so for a slightly larger $k$ this clearly gets TLE.

This is where the monotonic queue comes in.

## Definition

As the name suggests, the essence of a monotonic queue splits into "monotonic" and "queue".

"Monotonic" refers to the "pattern" of the elements – increasing (or decreasing).

"Queue" means that elements can only be manipulated at the front and the back of the queue.

P.S. The "queue" in a monotonic queue differs somewhat from an ordinary queue; this will be mentioned later.

## Analysis of the example

### Explanation

With the notion of a "monotonic queue" above, it is natural to think of optimizing with a monotonic queue.

What we need is the maximum (minimum) of every $k$ consecutive numbers. Clearly, when a number enters the range in which we are "looking for" the maximum, if this number is larger than the numbers before it (which entered the queue earlier), then obviously those earlier numbers will leave the queue before it and can never be the maximum again.

In other words – when the condition above holds, we can "pop" the earlier numbers and then really push this number to the back of the queue.

This amounts to maintaining a decreasing queue, which matches the definition of a monotonic queue and reduces the number of repeated comparisons. Moreover, since the maintained queue lies within the query range and is decreasing, the front of the queue is necessarily the maximum of that query range, so when outputting we only need to output the front.

It is evident that in such an algorithm every number enters and leaves the queue at most once, so the time complexity is reduced to $O(n)$.

And since the length of the query interval is fixed, a value outside the query window must not be output no matter how large it is, so we also need a site array recording the position in the original array of the $i$-th element in the queue, in order to pop a front element that has gone out of bounds.

### Procedure

For example, constructing a monotonically increasing queue looks like this:

The original sequence is:

```text
1 3 -1 -3 5 3 6 7
```

Since we always have to keep the queue **increasing**, the following happens (assume $k = 3$):

| Operation                                                                                   | Queue state |
| ------------------------------------------------------------------------------------------- | ----------- |
| 1 enters the queue                                                                          | `{1}`       |
| 3 is larger than 1, 3 enters the queue                                                      | `{1 3}`     |
| -1 is smaller than every element in the queue, so clear the queue and -1 enters the queue   | `{-1}`      |
| -3 is smaller than every element in the queue, so clear the queue and -3 enters the queue   | `{-3}`      |
| 5 is larger than -3, it enters the queue directly                                           | `{-3 5}`    |
| 3 is smaller than 5, 5 leaves the queue, 3 enters the queue                                 | `{-3 3}`    |
| -3 is already outside the window, so -3 leaves the queue; 6 is larger than 3, 6 enters the queue | `{3 6}`  |
| 7 is larger than 6, 7 enters the queue                                                      | `{3 6 7}`   |

???+ note "Reference code for the example"
    ```cpp
    --8<-- "docs/ds/code/monotonic-queue/monotonic-queue_1.cpp"
    ```

P.S. One big difference between this "queue" and an ordinary queue is that operations can also be performed at the back; the STL has a similar data structure, deque.

???+ note "Example 2 [Luogu P2698 Flowerpot S](https://www.luogu.com.cn/problem/P2698)"
    You are given the coordinates of $N$ water drops; $y$ is the height of the drop and $x$ is the position where it lands on the $x$-axis. Each drop falls at a speed of 1 unit of length per second. You need to place a flowerpot somewhere on the $x$-axis so that the time between the first drop caught by the flowerpot and the last drop caught by it is at least $D$.
    A drop is considered caught as soon as it lands on the $x$-axis aligned with the edge of the flowerpot. Given the coordinates of the $N$ drops and the value $D$, compute the minimum width $W$ of the flowerpot. $1\leq N \leq 100000 , 1 \leq D \leq 1000000, 0 \leq x,y\leq 10^6$

After sorting all drops by their $x$ coordinate, the problem turns into finding an interval with the smallest difference of $x$ coordinates such that the difference between the maximum and the minimum $y$ coordinate within it is at least $D$. We notice that this problem has something in common with the previous example – both are about the maximum and minimum inside an interval – but here the size of the interval is not fixed; in fact the size of the interval is itself the answer we are looking for.

We can still use two monotonic queues, one increasing and one decreasing, to maintain the maximum and minimum of $[L,R]$ as $R$ keeps moving right. But now we observe that if $L$ is fixed, the maximum of $[L,R]$ can only grow and the minimum can only shrink, so letting $f(R) = \max[L,R]-\min[L,R]$, $f(R)$ is an increasing function of $R$, hence $f(R)\geq D \implies f(r)\geq D,R\lt r \leq N$. This shows that for every fixed $L$, the first $R$ to the right that satisfies the condition is the optimal answer.
So the overall procedure is: fix $L$, move $R$ from front to back, and maintain the extremes of $[L,R]$ with two monotonic queues. When the first $R$ satisfying the condition is found, update the answer and move $L$ backward as well. As $L$ moves, both monotonic queues must pop their fronts in time. This way, until $R$ reaches the end, every element still enters and leaves the queues once each, guaranteeing $O(n)$ time complexity.

???+ note "Reference code"
    ```cpp
    --8<-- "docs/ds/code/monotonic-queue/monotonic-queue_2.cpp"
    ```
