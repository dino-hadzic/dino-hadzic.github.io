---
title: Knapsack DP basics
---

Prerequisites: [Introduction to dynamic programming](../index.md).

## Introduction

Before explaining concretely what "knapsack DP" is, let us look at the following example:

???+ note "[\"USACO07 DEC\" Charm Bracelet](https://www.luogu.com.cn/problem/P2871)"
    Problem summary: there are $n$ items and a knapsack of capacity $W$; every item has two attributes, weight $w_{i}$ and value $v_{i}$. Choose some items to put into the knapsack so that the total value of the items in the knapsack is maximized and the total weight of the items in the knapsack does not exceed its capacity.

In the example above, every item has only two possible states (taken or not), corresponding to the binary $0$ and $1$, so such problems are called "0-1 knapsack problems".

## 0-1 knapsack

### Explanation

In the example, the known conditions are the weight $w_{i}$ and value $v_{i}$ of the $i$-th item, and the total capacity $W$ of the knapsack.

Let the DP state $f_{i,j}$ be the maximum total value a knapsack of capacity $j$ can achieve when only the first $i$ items may be put in.

Consider the transition. Suppose all states for the first $i-1$ items have already been processed. For the $i$-th item: if it is not put into the knapsack, the remaining capacity of the knapsack does not change, nor does the total value of the items in the knapsack, so the maximum value in this case is $f_{i-1,j}$; if it is put into the knapsack, the remaining capacity decreases by $w_{i}$ and the total value of the items in the knapsack increases by $v_{i}$, so the maximum value in this case is $f_{i-1,j-w_{i}}+v_{i}$.

From this we obtain the state transition equation:

$$
f_{i,j}=\max(f_{i-1,j},f_{i-1,j-w_{i}}+v_{i})
$$

If we directly record the states in a two-dimensional array here, we get MLE. We can consider optimizing with a rolling array.

Since only $f_{i-1}$ affects $f_i$, we can drop the first dimension and directly use $f_{i}$ to denote the maximum value of a knapsack of capacity $i$ when processing the current item, obtaining the following equation:

$$
f_j=\max \left(f_j,f_{j-w_i}+v_i\right)
$$

**Be sure to memorize and understand this transition equation, because the transition equations of most knapsack problems are derived from it.**

### Implementation

One more thing to note: it is easy to write the following **incorrect core code**:

=== "C++"
    ```cpp
    for (int i = 1; i <= n; i++)
      for (int l = 0; l <= W - w[i]; l++)
        f[l + w[i]] = max(f[l] + v[i], f[l + w[i]]);
    // simplified from f[i][l + w[i]] = max(max(f[i - 1][l + w[i]], f[i - 1][l] + v[i]),
    // f[i][l + w[i]]);
    ```

=== "Python"
    ```python
    for i in range(1, n + 1):
        for l in range(0, W - w[i] + 1):
            f[l + w[i]] = max(f[l] + v[i], f[l + w[i]])
    # simplified from f[i][l + w[i]] = max(max(f[i - 1][l + w[i]], f[i - 1][l] + v[i]),
    # f[i][l + w[i]])
    ```

What is wrong with this code? The enumeration order is wrong.

Looking closely at the code, we see: for the currently processed item $i$ and the current state $f_{i,j}$, when $j\geqslant w_{i}$, $f_{i,j}$ is affected by $f_{i,j-w_{i}}$. This amounts to item $i$ being put into the knapsack multiple times, which does not match the problem statement. (In fact, this is exactly the solution to the unbounded knapsack problem.)

To avoid this, we can change the enumeration order, enumerating from $W$ down to $w_{i}$. Then the error above does not occur, because $f_{i,j}$ is always updated before $f_{i,j-w_{i}}$.

Therefore the actual core code is

=== "C++"
    ```cpp
    for (int i = 1; i <= n; i++)
      for (int l = W; l >= w[i]; l--) f[l] = max(f[l], f[l - w[i]] + v[i]);
    ```

=== "Python"
    ```python
    for i in range(1, n + 1):
        for l in range(W, w[i] - 1, -1):
            f[l] = max(f[l], f[l - w[i]] + v[i])
    ```

??? note "Example code"
    ```cpp
    --8<-- "docs/dp/code/knapsack/knapsack_1.cpp"
    ```

## Unbounded knapsack

### Explanation

The unbounded knapsack model is similar to the 0-1 knapsack; the only difference from the 0-1 knapsack is that an item can be chosen an unlimited number of times rather than only once.

We can borrow the idea of the 0-1 knapsack to define the state: let $f_{i,j}$ be the maximum value a knapsack of capacity $j$ can achieve when only the first $i$ items may be chosen.

Note that although the definition is similar to the 0-1 knapsack, its state transition equation differs from that of the 0-1 knapsack.

### Procedure

Consider a naive approach: for the $i$-th item, enumerate how many copies are chosen and transition accordingly. The time complexity of this is $O(nW^2)$, where $n$ is the total number of items and $W$ is the knapsack capacity.

The state transition equation is as follows:

$$
f_{i,j}=\max_{k=0}^{\lfloor j/w_i\rfloor}(f_{i-1,j-k\times w_i}+v_i\times k)
$$

Consider a simple optimization. We can see that for $f_{i,j}$, it suffices to transition from $f_{i,j-w_i}$. Therefore the state transition equation is:

$$
f_{i,j}=\max(f_{i-1,j},f_{i,j-w_i}+v_i)
$$

The reason is that when we transition this way, $f_{i,j-w_i}$ has already been updated from $f_{i,j-2\times w_i}$, so $f_{i,j-w_i}$ is the optimal result that already fully accounts for the number of copies of the $i$-th item chosen. In other words, through the property of locally optimal substructure, we reuse the previous enumeration process and optimize the complexity of the enumeration.

As with the 0-1 knapsack, we can drop the first dimension to optimize the space complexity. If you understood the optimization of the 0-1 knapsack, it is not hard to see that the compressed loop runs forward (that is, the incorrect optimization mentioned above).

??? note "[\"Luogu P1616\" Crazy Herb Gathering](https://www.luogu.com.cn/problem/P1616)"
    Problem summary: there are $n$ kinds of items and a knapsack of capacity $W$; every kind of item has two attributes, weight $w_{i}$ and value $v_{i}$. Choose some items to put into the knapsack so that the total value of the items in the knapsack is maximized and the total weight of the items in the knapsack does not exceed its capacity.

??? note "Example code"
    ```cpp
    --8<-- "docs/dp/code/knapsack/knapsack_2.cpp"
    ```

## Bounded knapsack

The bounded knapsack is also a variant of the 0-1 knapsack. The difference from the 0-1 knapsack is that there are $k_i$ copies of each kind of item rather than one.

A very naive idea: equivalently convert "choose each kind of item $k_i$ times" into "there are $k_i$ identical items, each chosen once". This turns it into a 0-1 knapsack model, which can be solved by applying the method described above. The state transition equation is as follows:

$$
f_{i,j}=\max_{k=0}^{k_i}(f_{i-1,j-k\times w_i}+v_i\times k)
$$

The time complexity is $O(W\sum_{i=1}^nk_i)$.

??? note "Core code"
    ```cpp
    for (int i = 1; i <= n; i++) {
      for (int weight = W; weight >= w[i]; weight--) {
        // one more loop level over the number of copies
        for (int k = 1; k * w[i] <= weight && k <= cnt[i]; k++) {
          dp[weight] = max(dp[weight], dp[weight - k * w[i]] + k * v[i]);
        }
      }
    }
    ```

### Binary grouping optimization

Consider optimizing. We still convert the bounded knapsack into a 0-1 knapsack model to solve it.

### Explanation

Obviously, the $O(nW)$ part of the complexity cannot be optimized further; we can only start from $O(\sum k_i)$. For convenience, we use $A_{i,j}$ to denote the $j$-th item split off from the $i$-th kind of item.

In the naive approach, $\forall j\le k_i$, all $A_{i,j}$ denote the same item. The main reason for our low efficiency is that we do a large amount of repetitive work. For example, we considered the two completely equivalent cases "choose $A_{i,1},A_{i,2}$ together" and "choose $A_{i,2},A_{i,3}$ together". We did such repetitive work many times. Optimizing the way of splitting thus becomes the key to solving the problem.

### Procedure

We can make the splitting more efficient by "binary grouping".

Specifically, let $A_{i,j}\left(j\in\left[0,\lfloor \log_2(k_i+1)\rfloor-1\right]\right)$ denote the large item "bundled" from $2^{j}$ single items. In particular, if $k_i+1$ is not an integer power of $2$, a large item "bundled" from $k_i-2^{\lfloor \log_2(k_i+1)\rfloor}+1$ single items must be added at the end to make up the difference.

A few examples:

-   $6=1+2+3$
-   $8=1+2+4+1$
-   $18=1+2+4+8+3$
-   $31=1+2+4+8+16$

Obviously, the splitting above can represent an equivalent choice of any number $\le k_i$ of items. After splitting every kind of item in this way, it suffices to solve the problem with the 0-1 knapsack method.

The time complexity is $O(W\sum_{i=1}^n\log_2k_i)$

### Implementation

??? note "Binary grouping code"
    === "C++"
        ```cpp
        index = 0;
        for (int i = 1; i <= m; i++) {
          int c = 1, p, h, k;
          cin >> p >> h >> k;
          while (k > c) {
            k -= c;
            list[++index].w = c * p;
            list[index].v = c * h;
            c *= 2;
          }
          list[++index].w = p * k;
          list[index].v = h * k;
        }
        ```
    
    === "Python"
        ```python
        index = 0
        for i in range(1, m + 1):
            c = 1
            p, h, k = map(int, input().split())
            while k > c:
                k -= c
                index += 1
                list[index].w = c * p
                list[index].v = c * h
                c *= 2
            index += 1
            list[index].w = p * k
            list[index].v = h * k
        ```

### Monotonic queue optimization

See [Monotonic queue/monotonic stack optimization](../opt/monotonic-queue-stack.md).

Exercise: [\"Luogu P1776\" Treasure Selection\_NOI Daokan 2010 Tigao (02)](https://www.luogu.com.cn/problem/P1776)

## Counting the number of ways

For a problem with a given knapsack capacity, item costs, other relations, etc., find the total number of ways to fill a certain capacity.

For such problems, simply replace taking the maximum with summation.

For example, the transition equation of the 0-1 knapsack problem becomes:

$$
\mathit{dp}_j \leftarrow \mathit{dp}_j + \mathit{dp}_{j-c_i} \qquad (j \ge c_i)
$$

Initial condition: $\mathit{dp}_0=1$

This is because there is also one way for capacity $0$: putting nothing in.

## References and notes

-   [Nine Lectures on the Knapsack Problem – Cui Tianyi (Chinese)](https://github.com/tianyicui/pack).
