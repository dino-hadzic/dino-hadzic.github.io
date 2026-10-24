---
title: Rollback Mo's algorithm
---

## Introduction

In some problems, when moving from one interval to another, either insertion or deletion may be impossible to implement. When only insertion is infeasible or only deletion is infeasible, the problem can be solved with rollback Mo's algorithm in $O(n \sqrt m)$ time. The core idea of rollback Mo's algorithm is: since only one of the operations can be implemented, use only that operation and leave the rest to rollbacks.

Rollback Mo's algorithm comes in two variants, one using only insertions and one using only deletions. Below we only describe the variant that uses only insertions; the variant using only deletions differs from it only in small implementation details, so it is not described separately.

## Example problem [JOISC 2014 Day1 历史研究 (Historical Research)](https://loj.ac/problem/2874)

You are given an array $A$ of length $n$ and $m$ queries $(1 \leq n, m \leq 10^5)$; each query asks for the number with the largest importance in an interval $[L, R]$, and you must **output its importance**. The importance of a number $i$ is defined as $i$ multiplied by the number of occurrences of $i$ in the interval.

In this problem, updating the answer during insertions is easy to implement, but updating it during deletions is not. If an insertion affects the answer, the new answer must be the importance of the number just inserted; however, if the number with the largest importance in the interval changes after a deletion, it is hard to determine which number is the new one with the largest importance. Therefore ordinary Mo's algorithm can hardly solve this problem.

## Process

-   Split the original sequence into blocks, and sort the queries by the index of the block containing the left endpoint in ascending order as the first key and by the right endpoint in ascending order as the second key.
-   Process the queries in order:
    -   If the block $B$ containing the left endpoint of the query differs from the block containing the left endpoint of the previous query, initialize the left endpoint of the Mo interval to the right endpoint of $B$ plus $1$, and the right endpoint of the Mo interval to the right endpoint of $B$;
    -   If the left and right endpoints of the query belong to the same block, answer the query by scanning the interval directly;
    -   If the left and right endpoints of the query belong to different blocks:
        -   If the right endpoint of the query is greater than the right endpoint of the Mo interval, keep extending the right endpoint until the right endpoint of the Mo interval equals the right endpoint of the query;
        -   Keep extending the left endpoint of the Mo interval until it equals the left endpoint of the query;
        -   Answer the query;
        -   Undo the changes to the left endpoint of the Mo interval, rolling the left endpoint of the Mo interval back to the right endpoint of $B$ plus $1$.

## Complexity proof

Suppose the block size of rollback Mo's algorithm is $b$:

-   Queries whose left and right endpoints lie in the same block can be computed in $O(b)$ time;
-   For the other queries, consider the queries whose left endpoints lie in the same block: their right endpoints are monotonically increasing, so the time complexity of moving the right endpoint is $O(n)$, while the movement of the left endpoint for a single query does not exceed $b$. Since there are $\frac{n}{b}$ blocks, the total complexity is $O(mb+\frac{n^2}{b})$; taking $b=\frac{n}{\sqrt{m}}$ is optimal, giving a time complexity of $O(n\sqrt{m})$.

## Implementation

??? note "Reference code"
    ```cpp
    --8<-- "docs/misc/code/rollback-mo-algo/rollback-mo-algo_1.cpp"
    ```

## References

-   [回滚莫队及其简单运用 (Rollback Mo's algorithm and its simple applications) | Parsnip's Blog](https://www.cnblogs.com/Parsnip/p/10969989.html)
