---
title: Counting DP
---

**Counting DP** is a memoized-search method similar to DP (it differs somewhat from DP in the narrow sense, i.e. optimization problems) used to solve counting (and summation) problems.

## Basics

### Basic idea

A counting problem usually asks for the size of some set $S$. In competitive programming the size of $S$ can reach the order of $\Theta(n^n)$ or even $\Theta(2^{n!})$ (of course, the answer is usually taken modulo some fixed number), where $n$ is the problem size, so we cannot enumerate the elements of $S$ one by one.

If we can split $S$ into several disjoint subsets, the number of elements of $S$ equals the sum of the numbers of elements of these parts. If counting these subsets happens to be a problem similar to the original one, we can solve it with a method resembling dynamic programming.

### Example

???+ note "Example"
    Given a positive integer $n$, count the ways to write $n$ as a sum of $k$ positive integers, where arrangements with swapped positions count as different partitions.

Let $S_{n,k}$ be the set of tuples of positive integers $(a_1, \dots, a_k)$ with $a_1 + \dots + a_k = n$. If $a_k$ is fixed, we reason as follows: since $a_1 + a_2 + \dots + a_{k-1} + a_k = n$, we have $a_1 + a_2 + \dots + a_{k-1} = n - a_k$. By the definition of $S_{n,k}$, $(a_1, a_2, \dots, a_{k-1}) \in S_{n - a_k, k - 1}$.

Since $a_1, a_2, \dots, a_k$ are positive integers, $a_k$ ranges over $[1, n - k + 1] \cap \mathbb Z$. Therefore $S_{n,k}$ can be partitioned according to $a_k$ into $n - k + 1$ subsets, where for $a_k = i$ the subset is:

$$
\{(L, i) \mid L \in S_{n-i,k-1}\}.
$$

The number of elements of this subset is obviously $S_{n-i,k-1}$, and because the values of $i$ differ, these subsets are pairwise disjoint. Hence:

$$
|S_{n,k}| = \sum_{i=1}^{n-k+1} |S_{n-i,k-1}|.
$$

So we can handle it with a DP-like method: let $f_{n,k}$ be $|S_{n,k}|$; then the state transition equation is:

$$
f_{n,k} = \sum_{i=1}^{n-k+1} f_{n-i,k-1}.
$$

Now the problem can be solved with DP.

### Similarities and differences with optimization DP

Observe that both counting DP and optimization DP compute a value (a size, an optimum) over some domain $\Omega$; this value is obtained by processing every element of $\Omega$ once and then aggregating the processed values.

For example, in the 0-1 knapsack problem the elements of $\Omega$ are the sets of items put into the knapsack; for one choice $S$ in $\Omega$ we process $S$ once, obtaining $w(S)$, the total value of the items in $S$, and among all processed values we take the maximum to get the answer.

For a counting problem, the elements of $\Omega$ are the elements of the set $S$ whose size we want; the processing turns every element of $S$ into a $1$, and these $1$s are aggregated by addition. Since every element of $S$ corresponds to one $1$, the resulting value is exactly the number of elements of $S$.

When the aggregation is a maximum/minimum, we may split $\Omega$ into arbitrary parts; it suffices that their union is $\Omega$, no disjointness is required. Counting problems do not satisfy this, so we must split $\Omega$ into pairwise disjoint parts. This is the difference from optimization DP.

## Example

???+ note "Example"
    Given a positive integer $n$, count the ways to write $n$ as a sum of arbitrarily many positive integers, where arrangements with swapped positions count as the **same** partition.

### Solution 1

The elements of the set to count are multisets of positive integers whose sum is $n$. But this is clearly hard to work with directly.

If a multiset $T$ contains only positive integers $\le M$ and the sum of all elements of $T$ is $n$, we write $T \in S_{n, M}$. Consider how many times $M$ occurs. It can be $k \in \left[0, \left\lfloor \dfrac nM \right\rfloor\right] \cap \mathbb Z$ times. Then it transitions to $S_{n - kM, M - 1}$. Just sum up. The complexity is $\Theta(n^2 \log n)$ (the $\log$ comes from the harmonic series produced by the range of $k$).

But this is still not good enough. Consider the following example:

$$
\begin{aligned}
f_{8, 3} &= {\color{red}f_{8, 2} + f_{5, 2} + f_{2, 2}} \\
f_{9, 3} &= {\color{blue}f_{9, 2} + f_{6, 2} + f_{3, 2} + f_{0, 2}} \\
f_{10, 3} &= {\color{green}f_{10, 2} + f_{7, 2} + f_{4, 2} + f_{1, 2}}\\
f_{11, 3} &= f_{11, 2} + {\color{red}f_{8, 2} + f_{5, 2} + f_{2, 2}}\\
f_{12, 3} &= f_{12, 2} + {\color{blue}f_{9, 2} + f_{6, 2} + f_{3, 2} + f_{0, 2}}\\
f_{13, 3} &= f_{13, 2} + {\color{green}f_{10, 2} + f_{7, 2} + f_{4, 2} + f_{1, 2}}\\
\end{aligned}
$$

Substituting equal quantities gives $f_{11, 3} = f_{11, 2} + f_{8, 3}$, $f_{12, 3} = f_{12, 2} + f_{9, 3}$, $f_{13, 3} = f_{13, 2} + f_{10, 3}$. In the same way we obtain a general state transition equation:

$$
f_{n, M} = f_{n, M - 1} + \begin{cases} f_{n - M, M} & n \ge M, \\ 0 & \text{otherwise}. \end{cases}
$$

Now the time complexity is $\Theta(n^2)$.

### Solution 2

Observe that any multiset $T$ of positive integers can be obtained by two operations, "increment every element of $T$" and "add an element of value $1$ to $T$", and different operation sequences yield different results.

Thus a transition on $T$ becomes a transition on the operation sequence. Consider the last operation in an operation sequence that partitions $n$ into $m$ numbers (denote all such sequences by $B_{n,m}$). If it is operation $1$, no number is added, but $\sum T$ increases by $m$. For the final $\sum T = n$, the previous $T$ (denoted $T'$) must have sum $n-m$. So $B_{n,m} \to B_{n-m,m}$. If it is operation $2$, one number is added and $\sum T$ increases by $1$. So $B_{n,m} \to B_{n-1,m-1}$.

The time complexity is still $\Theta(n^2)$.

### Solution 3

Split $T$ into the part $T_1$ of elements greater than $\sqrt n$ and the part $T_2$ of elements less than or equal to $\sqrt n$. $T_2$ can be counted with Solution 1, and the number of possible $T_1$ by a slightly modified Solution 2: change the two operations to "increment every element of $T_1$" and "add an element of value $\lfloor \sqrt n \rfloor + 1$ to $T_1$". The state transition equation is easy to write down.

Split $n$ into two parts, $A$ and $B$. Enumerating one of them determines the other. Compute the number of $T_1$ with $\sum T_1 = A$ and the number of $T_2$ with $\sum T_2 = B$, multiply them, and sum over all $A$ to get the final result.

Since $M \le \sqrt n$ while counting $T_1$, using Solution 1 for $T_1$ takes $\Theta(n^{3/2})$ time. Likewise, while counting $T_2$ we have $|T_2| \le \dfrac{\sum T_2}{\sqrt n} \le \dfrac{n}{\sqrt n} = \sqrt n$, so using Solution 2 for $T_2$ also takes $\Theta(n^{3/2})$ time. The total time complexity is therefore $\Theta(n^{3/2})$.
