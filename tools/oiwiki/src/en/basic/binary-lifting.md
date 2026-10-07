---
title: Binary lifting
---

This page briefly introduces binary lifting.

## Definition

**Binary lifting**, as the name suggests, means "growing by doubling". When we carry out a recurrence and the state space is so large that ordinary linear recurrence cannot meet the time and space requirements, we can, by doubling, compute only the values at positions that are integer powers of $k$ in the state space, as representatives. When a value at another position is needed, we use the property that "any integer can be written as a sum of powers of $k$" and assemble the required value from the representatives computed earlier. Hence binary lifting requires that the state space of the recurrence be divisible with respect to powers of $k$. Usually $k = 2$.[^ref1]

This method is used in many algorithms, most commonly for the RMQ problem and for finding the [LCA (lowest common ancestor)](../graph/lca.md).

## Applications

### The RMQ problem

See: [RMQ](../topic/rmq.md).

RMQ stands for Range Maximum/Minimum Query. The method that solves RMQ with the doubling idea is the [sparse table](../ds/sparse-table.md).

### LCA on a tree by binary lifting

See: [Lowest common ancestor](../graph/lca.md).

## Examples

### Example 1

???+ note "Example"
    How can we weigh every weight in $[0,31]$ using as few weights as possible? (Weights may be put on only one side of the balance.)

??? note "Solution idea"
    The answer is to use the five weights 1 2 4 8 16, which can weigh everything in $[0,31]$. Likewise, to weigh everything in $[0,127]$ we can use the seven weights 1 2 4 8 16 32 64. By always choosing non-negative integer powers of 2 as the weights, we can weigh any required weight with very few weights.
    
    For example, to weigh everything in $[0,1023]$ only 10 weights are needed, and for everything in $[0,1048575]$ only 20. If the target weight doubles, the number of weights only increases by 1. This is called "logarithmic" growth, because the number of weights needed is proportional to the logarithm of the range of the target weight.

### Example 2

???+ note "Example"
    Given a cycle of length $n$ and a constant $k$, each jump goes from vertex $i$ to vertex $(i+k)\bmod n+1$, and there are $m$ jumps in total. Every vertex has a weight $a_i$. Find the sum of the weights of the starting vertices of the $m$ jumps modulo $10^9+7$.
    
    Constraints: $1\leq n\leq 10^6$, $1\leq m\leq 10^{18}$, $1\leq k\leq n$, $0\le a_i\le 10^9$.

??? note "Solution idea"
    Clearly we cannot brute-force the $m$ jumps, since $m$ can be as large as $10^{18}$ and the time would be unacceptable.
    
    So we need some preprocessing, aggregating information in advance so that queries can be answered faster. If we recorded the result for every possible number of jumps, neither time nor space would be acceptable.
    
    So how should we preprocess? Look at the first example. Any ideas?
    
    Back to this problem. We want to precompute some information and then assemble the answer from it as quickly as possible, while not precomputing too much. So we can precompute information in units of non-negative powers of 2: then only a small amount of information is processed in the preprocessing step, and assembling the answer takes little effort too.
    
    For this problem, that means precomputing for every vertex the result of jumping 1, 2, 4, 8, … steps (the vertex reached and the sum of weights). Then, to jump 13 steps, we just jump 1+4+8 steps: jump 1 step from the start, then 4 steps from the vertex reached, then 8 steps, adding up the precomputed weight sums along the way, and we obtain the weight sum for 13 steps.
    
    For each vertex and $2^i$ steps, store `go[i][x]`, the vertex where a jump of $2^i$ steps from vertex $x$ ends, and `sum[i][x]`, the sum of weights collected by jumping $2^i$ steps from vertex $x$. In the preprocessing, use a double loop: a jump of $2^i$ steps can be seen as a jump of $2^{i-1}$ steps followed by another $2^{i-1}$ steps, since clearly $2^{i-1}+2^{i-1}=2^i$. That is, `sum[i][x] = sum[i-1][x]+sum[i-1][go[i-1][x]]` and `go[i][x] = go[i-1][go[i-1][x]]`.
    
    There are some implementation details to watch. To make sure nothing is counted twice or missed, we usually precompute "left-closed, right-open" weight sums. That is, for a jump of 1 step we record only the weight of that vertex; for a jump of 2 steps we record the weights of that vertex and the next one. In other words, the weight of the end vertex is never included in `sum`. Then in the preprocessing we can simply add the two partial sums without worrying that the end of the first part and the start of the second part are counted twice.
    
    Although $m\leq 10^{18}$ looks scary, it suffices to precompute levels $0$ to $59$, and the problem is easily solved, much faster than brute force. In technical terms, the [time complexity](./complexity.md) of this approach is $\Theta(n\log m)$ for preprocessing and $\Theta(\log m)$ per query.

??? note "Sample code"
    ```cpp
    --8<-- "docs/basic/code/binary-lifting/binary-lifting_1.cpp"
    ```

## References and notes

[^ref1]: From Li Yudong, *Algorithm Competition Advanced Guide* (《算法竞赛进阶指南》), section 0x06 "Doubling".
