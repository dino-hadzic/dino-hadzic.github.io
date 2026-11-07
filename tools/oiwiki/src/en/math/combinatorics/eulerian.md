---
title: Eulerian numbers
---

???+ warning "Note"
    The Eulerian numbers below refer specifically to the Eulerian numbers. Do not confuse them with the Euler numbers or with Euler's number (the mathematical constants related to Euler, such as $\gamma$ or $\mathrm{e}$).

In enumerative combinatorics, the **Eulerian number** is the **number** of permutations of the numbers from $1$ to $n$ in which exactly $m$ elements are greater than the previous element (permutations with $m$ "ascents"). It is defined as

$$
A(n, m) = 
\left\langle 
\begin{matrix}
  n\\
  m - 1
\end{matrix}
\right\rangle
$$

For example, among the numbers from $1$ to $3$ there are $4$ permutations in total in which exactly one element is greater than the previous one:

| Permutation | Adjacent elements satisfying the condition | Count |
| ----- | ----------- | -- |
| 1 2 3 | 1, 2 & 2, 3 | 2  |
| 1 3 2 | 1, 3        | 1  |
| 2 1 3 | 1, 3        | 1  |
| 2 3 1 | 2, 3        | 1  |
| 3 1 2 | 1, 2        | 1  |
| 3 2 1 |             | 0  |

So by the definition of $A(n, m)$: if $n$ equals $3$ and $m$ equals $1$, the Eulerian number is $4$, meaning that there are $4$ permutations in total with $1$ element greater than the previous one.

For small values of $n$ and $m$ we can obtain the Eulerian numbers directly:

| $A(n, m)$ | Permutations satisfying the condition | Count |
| --------- | -------------------------------------------- | -- |
| $A(1, 0)$ | $(1)$                                        | 1  |
| $A(2, 0)$ | $(2, 1)$                                     | 1  |
| $A(2, 1)$ | $(1, 2)$                                     | 1  |
| $A(3, 0)$ | $(3, 2, 1)$                                  | 1  |
| $A(3, 1)$ | $(1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2)$ | 4  |
| $A(3, 2)$ | $(1, 2, 3)$                                  | 1  |

## Formula

Eulerian numbers can be computed by a recurrence or by recursion.

First, when $m \ge n$ or $n = 0$, there is no permutation satisfying the condition, so the Eulerian number is $0$ in this case.

Second, when $m = 0$, only the descending permutation satisfies the condition, so the Eulerian number is $1$ in this case.

Finally, consider inserting $n$ into a permutation of length $n-1$ to obtain a permutation of length $n$; since inserting $n$ increases the Eulerian number by at most $1$, $A(n, m)$ can be obtained by transitions only from $A(n-1, m-1)$ and $A(n-1, m)$.

Consider the position where $n$ is inserted: when $p_{i-1} < p_{i}$, if $n$ is inserted before $p_{i}$, i.e. if $n$ is inserted into an "ascent", the Eulerian number of the permutation does not change; also, if $n$ is inserted at the beginning of the permutation, the Eulerian number of the permutation does not change; otherwise, if $n$ is inserted at any other position, the Eulerian number of the permutation increases by $1$.

Consider the transition from $A(n-1, m-1)$ to $A(n, m)$: the Eulerian number has to increase by $1$, so $n$ cannot be inserted into an "ascent" or at the beginning of the permutation; there are $n - (m-1) - 1 = n-m$ options in total.

Consider the transition from $A(n-1, m)$ to $A(n, m)$: the Eulerian number has to stay the same, so $n$ can only be inserted into an "ascent" or at the beginning of the permutation; there are $m+1$ options in total.

Putting it all together, we have

$$
A(n, m) = \begin{cases}
    0, & m > n \text{ or } n = 0, \\
    1, & m = 0, \\
    (n-m) \cdot A(n-1, m-1) + (m+1) \cdot A(n-1, m), & \text{otherwise}.
\end{cases}
$$

## Implementation

=== "C++"
    ```cpp
    int eulerianNumber(int n, int m) {
      if (m >= n || n == 0) return 0;
      if (m == 0) return 1;
      return (((n - m) * eulerianNumber(n - 1, m - 1)) +
              ((m + 1) * eulerianNumber(n - 1, m)));
    }
    ```

=== "Python"
    ```python
    def eulerianNumber(n, m):
        if m >= n or n == 0:
            return 0
        if m == 0:
            return 1
        return ((n - m) * eulerianNumber(n - 1, m - 1)) + (
            (m + 1) * eulerianNumber(n - 1, m)
        )
    ```

## Exercises

-   [CF1349F1 Slime and Sequences (Easy Version)](https://codeforces.com/problemset/problem/1349/F1)
-   [CF1349F2 Slime and Sequences (Hard Version)](https://codeforces.com/problemset/problem/1349/F2)
-   [UOJ 593. 新年的军队 (New Year's Army)](https://uoj.ac/problem/593)
-   [P7511 三到六 (Three to Six)](https://www.luogu.com.cn/problem/P7511)
