---
title: Mo's algorithm with modifications
---

Please make sure you already know ordinary Mo's algorithm. If you do not yet, first read the previous page [Ordinary Mo's algorithm](./mo-algo.md).

## Characteristics

Ordinary Mo's algorithm cannot handle modifications.

We can force it to support modifications: just like in DP, we can forcibly add one more dimension, the **time dimension**, representing the time of this operation.

The time dimension represents the number of modifications applied so far.

That is, the query $[l,r]$ becomes $[l,r,\text{time}]$.

Then our coordinates can also move along the time dimension, i.e. $[l,r,\text{time}]$ has one more direction in which it can move, and it can become:

-   $[l-1,r,\text{time}]$
-   $[l+1,r,\text{time}]$
-   $[l,r-1,\text{time}]$
-   $[l,r+1,\text{time}]$
-   $[l,r,\text{time}-1]$
-   $[l,r,\text{time}+1]$

Such a transition is also $O(1)$, but our sorting has one more key; a little more tinkering is all that is needed.

The sorting and transitions can be done in a way similar to ordinary Mo's algorithm, achieving $O(n^{5/3})$.

This time we sort with blocks of size $n^{2/3}$, giving $n^{1/3}$ blocks; the first key is the block containing the left endpoint, the second key is the block containing the right endpoint, and the third key is the time.

???+ note "Optimal block length and time complexity analysis"
    Let the sequence length be $n$, with $m$ queries and $t$ modifications.
    
    The second sorting key of Mo's algorithm with modifications is the index of the block containing the right endpoint, unlike ordinary Mo's algorithm.
    
    Think about what happens if the right endpoint is not divided into blocks:
    
    -   Unordered right endpoints would move $n$ times for every query.
    -   Ordered right endpoints would bring unordered times, so every query would move $t$ times in time.
    
    In either case, the time cost is unacceptable.
    
    Now let us analyze the time complexity.
    
    Let the block length be $s$; then there are $\dfrac{n}{s}$ blocks. For blocks $i$ and $j$, let $q_{i,j}$ denote the number of queries whose left endpoint lies in block $i$ and whose right endpoint lies in block $j$.
    
    For each "group" of queries $(i,j)$ in which neither endpoint changes block, the endpoints move $O(s)$ times per step, and the time increases monotonically: $O(t)$.
    
    The time spent when the left and right endpoints change blocks is negligible.
    
    Written out, this is:
    
    $$
    \begin{aligned}
    &\sum_{i=1}^{n/s}\sum_{j=i+1}^{n/s}(q_{i,j}\cdot s+t)\\
    =&ms+\left(\dfrac{n}{s}\right)^2t\\
    =&ms+\dfrac{n^2t}{s^2}
    \end{aligned}
    $$
    
    We find the minimum of this expression by differentiation. Let $f(s)=ms+\dfrac{n^2t}{s^2}$. Then $f'(s)=m-\dfrac{2n^2t}{s^3}=0$.
    
    We get $s=\sqrt[3]{\dfrac{2n^2t}{m}}=\dfrac{2^{1/3}n^{2/3}t^{1/3}}{m^{1/3}}=s_0$.
    
    That is, when the block length is $\dfrac{n^{2/3}t^{1/3}}{m^{1/3}}$, we obtain the optimal time complexity $O\left(n^{2/3}m^{2/3}t^{1/3}\right)$.
    
    The commonly quoted $O\left(n^{5/3}\right)$ is precisely the time complexity when $n,m,t$ are treated as being of the same order of magnitude.
    
    In practice it is still recommended to set the block length to $n^{2/3}$.

## Example problem

???+ note "Example [「国家集训队」数颜色/维护队列 (Counting Colors / Maintaining a Queue)](https://www.luogu.com.cn/problem/P1903)"
    Problem summary: you are given a sequence and M operations of two kinds:
    
    1.  change the number at some position of the sequence
    2.  query the number of distinct numbers in the range $[l,r]$ (several equal numbers count as one)

It is easy to see that without operation 1 (modification), we could easily solve this with ordinary Mo's algorithm.

But the problem also has point modifications, so we use **Mo's algorithm with modifications**.

### Procedure

First consider the approach of ordinary Mo's algorithm:

-   Each time the range is extended, for every number added, count how many times it has already occurred; if the number of occurrences of this value before the addition was $0$, it is a new value and the answer increases by $1$. Then the number of occurrences of this value increases by $1$.
-   Each time the range is shrunk, for every number deleted, count how many times it occurs after the deletion; if the number of occurrences of this value after the deletion is $0$, this value has been completely removed from the current range, i.e. the current range has one color fewer, and the answer decreases by $1$. Then the number of occurrences of this value decreases by $1$.

Now consider the modifications:

-   A point modification changes the number at some position. If we move from a query that has gone through $i$ modifications to a query that has gone through $j$ modifications, and $i<j$, we need to forcibly apply the $(i+1)$-th to the $j$-th modifications.
-   If $j<i$, we need to forcibly undo the $i$-th to the $(j+1)$-th modifications.

How do we forcibly apply a modification? Suppose a modification changes the color at position $pos$, the original color at $pos$ was $a$ and the color after the modification is $b$, and suppose the current range of Mo's algorithm has been extended to $[l,r]$.

-   Applying the modification: we first check whether $pos$ is inside the range $[l,r]$. If so, this amounts to deleting color $a$ from the range and adding color $b$, and changing the $pos$-th entry of the current color sequence to $b$. If it is not inside the range $[l,r]$, we simply change the $pos$-th entry of the current color sequence to $b$.
-   Undoing the modification: this is the same as applying a modification that changes the $pos$-th entry and turns color $b$ into color $a$.

Thus this problem is easily solved with Mo's algorithm with modifications!

### Implementation

??? note "Reference code"
    ```cpp
    --8<-- "docs/misc/code/modifiable-mo-algo/modifiable-mo-algo_1.cpp"
    ```
