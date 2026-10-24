---
title: Mo's algorithm with secondary offline processing
---

## Overview

Sometimes we encounter problems that look very suitable for Mo's algorithm, but whose single transition is not $O(1)$; in that case applying Mo's algorithm directly, even with an adjusted block size, leads to an incorrect complexity.

If, in such a case, the contribution of each transition to the answer can be written as a difference, we can split these transitions apart, store them offline and process them in bulk with another algorithm.

Let $f(x, l, r)$ denote the contribution of $x$ with respect to $[l, r]$.

For example, when we extend the current interval $[l, r]$ to $[l, r + 1]$, what we need is $f(a_{r + 1}, l, r)$. If it can be differenced, we can write it as $f(a_{r + 1}, 1, r) - f(a_{r + 1}, 1, l - 1)$, where the first term can be precomputed for every $r$, and every term of the second kind can be stored offline at the corresponding $l - 1$ and then processed by enumerating from small to large with a sweep line. The other transition directions can be handled similarly.

This algorithm, which processes the transitions offline once more on top of Mo's algorithm, itself an offline algorithm, is called Mo's algorithm with secondary offline processing.

Let us understand it through concrete problems.

## Example problems

???+ note "[Luogu P5047 \[Ynoi2019 模拟赛 (mock contest)\] Yuno loves sqrt technology II](https://www.luogu.com.cn/problem/P5047)"
    You are given a sequence $a$ of length $n$ and $m$ queries; each query asks for the number of inversions in an interval.
    
    Constraints: $1 \leq n,m \leq 10^5$, $0 \leq a_i \leq 10^9$.

With plain Mo's algorithm each transition costs at least $O(\log n)$; observing the problem, the information we need in each transition is "the rank of a number within some interval", and this information can be differenced with respect to the interval, so we consider secondary offline processing.

When we extend $[l, r]$ to $[l, r + 1]$, we need the number of elements in the interval $[l, r]$ that are greater than $a_{r + 1}$.
Let $f(x, r)$ denote the number of elements in the interval $[1, r]$ greater than $a_x$, and $g(x, r)$ the number of elements in the interval $[1, r]$ smaller than $a_x$. Then the change of the answer can be written as $f(r + 1, r) - f(r + 1, l - 1)$.

Similarly, the change when shrinking $[l, r]$ to $[l, r - 1]$ can be written as $-f(r, r - 1) + f(r, l - 1)$; extending $[l, r]$ to $[l - 1, r]$ can be written as $g(l - 1, r) - g(l - 1, l - 2)$, and shrinking $[l, r]$ to $[l + 1, r]$ can be written as $- g(l, r) + g(l, l - 1)$.

The terms $f(x, x - 1)$ and $g(x, x - 1)$ in these formulas can be precomputed in advance with a Fenwick tree in $O(n \log n)$; for the remaining terms $f(x, p)$ and $g(x, p)$, we store $x$ offline at $l$ for batch processing.

There is a trick here to save memory: we notice that, when processing each query, the values $x$ stored offline at $p$ always form a contiguous segment, so we do not need to store every move, only the segment being adjusted. This way the memory drops from the total number of moves $O(n\sqrt{m})$ to the number of queries $O(m)$.

Now we handle the problem we stored offline: insert numbers into a set, and query the rank of a number in the set. The total number of endpoint moves of Mo's algorithm is $O(n\sqrt{m})$, while the array only has length $O(n)$, so we consider solving this problem with value-range blocking, which has $O(\sqrt{n})$ insertion and $O(1)$ query.

Thus we have solved this problem in $O(n \sqrt{m} + n \sqrt{n})$ time complexity and $O(n + m)$ space complexity.

Finally, it is worth noting that what we computed is the change of the answer at each step rather than the answer itself, so prefix sums must be taken to obtain the final answers.

??? note "Sample code"
    ```cpp
    --8<-- "docs/misc/code/mo-algo-secondary-offline/mo-algo-secondary-offline_1.cpp"
    ```

???+ note "[Luogu P5501 \[LnOI2019\] 来者不拒，去者不追 (Welcome those who come, do not chase those who leave)](https://www.luogu.com.cn/problem/P5501)"
    Multiple queries ask for the sum of the "Abbi values" of all numbers in an interval $[l, r]$.
    
    The Abbi value is defined as follows: if $a_i$ is the $k$-th smallest in the query interval $[l,r]$, then its "Abbi value" equals $ka_i$.

Let $f(x,r)$ be the sum of the numbers in $[1,r]$ greater than $a_x$, and $g(x,r)$ the number of numbers in $[1,r]$ greater than $a_x$. Then, when we move the right endpoint to the right, the contribution produced is $f(r,r-1)-f(r,l-1) + a_r(r-l+ 1-(g(r,r-1)-g(r,l-1)))$; the other directions can be written out analogously and are not repeated here.

The terms $f(r, r - 1)$ and $g(r, r - 1)$ in the formula above can still be precomputed, and the rest are stored offline at the other endpoint and processed with a sweep line. It is easy to see that what we have to handle is still a problem with $O(n)$ insertions and $O(n\sqrt{m})$ rank queries, so we likewise solve it with value-range blocking.

??? note "Sample code"
    ```cpp
    --8<-- "docs/misc/code/mo-algo-secondary-offline/mo-algo-secondary-offline_2.cpp"
    ```
