---
title: Advanced knapsack DP
---

## Knapsack-related tricks

### Knapsack with generalized items

In this kind of knapsack, a single item $i$ has no fixed cost and value; its value depends on the cost allocated to it. In a knapsack problem with capacity $V$, when the cost allocated to item $i$ is $v_i$, the value obtained is $h_i\left(v_i\right)$.

So we enumerate the weight $w'$ allocated to the $i$-th item; the value of the item is then $h_i(w')$, and the current value is $f_{i - 1, w - w'} + h_i(w')$. Therefore the state transition equation is $f_{i, j} = \max \limits_{0 \le k \le j}(f_{i - 1, j - k} + h_i(k))$. In fact, everything described above is just the $(\max, +)$ convolution.

### Grouped knapsack

???+ note "[\"Luogu P1757\" Grouped Knapsack to the Sky](https://www.luogu.com.cn/problem/P1757)"
    There are $n$ items and a knapsack of size $m$; the $i$-th item has value $w_i$ and volume $v_i$. In addition, every item belongs to a group, and at most one item may be chosen from the same group. Find the maximum total value of items the knapsack can carry.

Such problems merely change "choose one among all items" into "choose one from the current group", so it suffices to run a 0-1 knapsack for each group.

Let us also say a word about storage. We can let $t_{k,i}$ denote the index of the $i$-th item of the $k$-th group, and $\mathit{cnt}_k$ denote the number of items in the $k$-th group.

#### Implementation

=== "C++"
    ```cpp
    --8<-- "docs/dp/code/knapsack/knapsack_4.cpp:core"
    ```

=== "Python"
    ```python
    for k in range(1, ts + 1):  # loop over each group
        for i in range(m, -1, -1):  # loop over the knapsack capacity
            for j in range(1, cnt[k] + 1):  # loop over each item in the group
                if i >= w[t[k][j]]:  # the knapsack capacity is sufficient
                    dp[i] = max(
                        dp[i], dp[i - w[t[k][j]]] + c[t[k][j]]
                    )  # state transition as in the 0-1 knapsack
    ```

Note here: **the loop order must not be mixed up**; only then is correctness guaranteed.

### Rollback knapsack

Counting the number of ways in an ordinary 0-1 knapsack only requires a direct DP, but sometimes situations of the form "all other items may be chosen, only a few items may not" arise, usually with different items in the same group repeatedly being forbidden, as in some complex tree knapsacks. A direct DP may then TLE, so the rollback knapsack is introduced to handle this situation.

Note that the items in the knapsack are unordered: for two items, which one is put in first has no effect on the current situation, so we can regard **every item as the last one put in**. Therefore we can first precompute the DP for everything, and then cancel the contribution of a particular item. That is:

$$
dp_j \gets dp_j - dp_{j - w_i}
$$

Note that the loop must run from small to large; otherwise the contribution would correspond to the unbounded knapsack.

## Knapsack miscellany

### Outputting the solution

Outputting the solution simply means recording how a certain state of the knapsack was derived. We can let $g_{i,v}$ denote whether the $i$-th item was chosen when it occupies space $v$. Then, during the transition, record which strategy was used (chosen or not). Pseudocode for the output:

```cpp
int v = V;  // records the current space

// since the last item stores the final state, loop starting from the last item
for (from the last item down to the first) {
  if (g[i][v]) {
    item i was chosen;
    v -= weight of item i;
  } else {
    item i was not chosen;
  }
}
```

### Counting the number of optimal solutions

To count the number of optimal solutions, we slightly modify the definition of the $\mathit{dp}$ array in the 0-1 knapsack: the DP state $f_{i,j}$ is the maximum total value a knapsack of capacity $j$ can achieve when only the first $i$ items may be put in and the knapsack is "exactly full".

After this modification, each DP state can be paired with a $g_{i,j}$ denoting the number of ways.

$f_{i,j}$ denotes the maximum value when only the first $i$ items are considered and the knapsack volume is "exactly" $j$.

$g_{i,j}$ denotes the number of ways when only the first $i$ items are considered and the knapsack volume is "exactly" $j$.

Transition equation:

If $f_{i,j} = f_{i-1,j}$ and $f_{i,j} \neq f_{i-1,j-v}+w$, it is better not to put the item into the knapsack, and the number of ways comes from $g_{i-1,j}$;

if $f_{i,j} \neq f_{i-1,j}$ and $f_{i,j} = f_{i-1,j-v}+w$, it is better to put the item into the knapsack, and the number of ways comes from $g_{i-1,j-v}$;

if $f_{i,j} = f_{i-1,j}$ and $f_{i,j} = f_{i-1,j-v}+w$, both putting it in and not putting it in achieve the optimum, and the number of ways comes from $g_{i-1,j}$ and $g_{i-1,j-v}$.

Initial conditions:

```cpp
memset(f, 0xcf, sizeof(f));
// since we want the maximum, initialize to negative infinity to avoid transitions from states that are not full
// if we want the minimum, initialize to positive infinity 0x3f
f[0] = 0;
g[0] = 1;  // putting nothing in is one way
```

Since the maximum knapsack volume may not be fillable, the optimal solution is not necessarily $f_{m}$.

Finally, we find the value of the optimal solution and add up the numbers of ways in the $g_{j}$ array for all entries achieving the optimum.

???+ note "Implementation"
    ```cpp
    for (int i = 0; i < N; i++) {
      for (int j = V; j >= v[i]; j--) {
        int tmp = std::max(dp[j], dp[j - v[i]] + w[i]);
        int c = 0;
        if (tmp == dp[j]) c += cnt[j];                       // if transitioning from dp[j]
        if (tmp == dp[j - v[i]] + w[i]) c += cnt[j - v[i]];  // if transitioning from dp[j-v[i]]
        dp[j] = tmp;
        cnt[j] = c;
      }
    }
    int max = 0;  // find the optimal solution
    for (int i = 0; i <= V; i++) {
      max = std::max(max, dp[i]);
    }
    int res = 0;
    for (int i = 0; i <= V; i++) {
      if (dp[i] == max) {
        res += cnt[i];  // sum the numbers of ways for the optimal solution
      }
    }
    ```

### The k-th best solution of the knapsack

The ordinary 0-1 knapsack asks for the optimal solution; with a slight modification of the ordinary knapsack DP method, adding one dimension to record the top k best solutions in the current state, we obtain an algorithm for the $k$-th best solution of the 0-1 knapsack.
Specifically: $f_{i,j,k}$ records the $k$-th largest value sum obtainable among the first $i$ items when the total volume of the chosen items is $j$. This state can be understood as extending $f_{i,j}$ of the ordinary 0-1 knapsack, which records only one datum, to record an ordered sequence of best solutions. During the transition, the optimum of the ordinary knapsack is computed as $f_{i,j}=\max(f_{i-1,j},f_{i-1,j-v_i}+w_i)$; now we instead need to merge the two decreasing sequences of size $k$, $f_{i-1,j}$ and $f_{i-1,j-v_i}+w_i$, and keep the top $k$ largest values after merging in $f_{i,j}$. This step uses the two-pointer method with complexity $O(k)$, so the overall time complexity is $O(nmk)$. As for space, this method can compress away the first dimension just like the ordinary knapsack, giving complexity $O(mk)$.

??? note "Example [HDU 2639 Bone Collector II](https://acm.hdu.edu.cn/showproblem.php?pid=2639)"
    Find the strictly $k$-th best solution of the 0-1 knapsack. $n \leq 100,v \leq 1000,k \leq 30$

??? note "Implementation"
    ```cpp
    --8<-- "docs/dp/code/knapsack/knapsack_3.cpp:core"
    ```

## Knapsack-related problems

### Mixed knapsack

The mixed knapsack mixes the 0-1 knapsack, the unbounded knapsack, and the bounded knapsack: some items can be taken only once, some an unlimited number of times, and some at most $k$ times.

Such problems look hard, but the choice of each kind of item is still independent, so it suffices to determine which kind of knapsack the current item belongs to and apply the solution for that kind.

#### Example

???+ note "[\"Luogu P1833\" Cherry Blossoms](https://www.luogu.com.cn/problem/P1833)"
    There are $n$ kinds of cherry trees and a time of length $T$; some cherry trees can be viewed only once, some at most $A_{i}$ times, and some an unlimited number of times. Every cherry tree has an aesthetic value $C_{i}$. Determine which cherry trees to view within time $T$ to maximize the aesthetic value.

??? note "Core code"
    ```cpp
    --8<-- "docs/dp/code/knapsack/knapsack_5.cpp:core"
    ```

Exercise: [HDU 5410 CRB and His Birthday](https://acm.hdu.edu.cn/showproblem.php?pid=5410)

### Two-dimensional cost knapsack

???+ note "[\"Luogu P1855\" Squeezing kkksc03](https://www.luogu.com.cn/problem/P1855)"
    There are $n$ tasks to complete; completing the $i$-th task takes $t_i$ minutes and incurs an expense of $c_i$ yuan.
    
    There are now $T$ minutes and $W$ yuan available to handle these tasks. Find the maximum number of tasks that can be completed.

This problem is clearly a 0-1 knapsack problem, but with the difference that choosing an item consumes two kinds of cost (money and time); it suffices to add one dimension to the state for the second cost. The state transition equation then becomes $f_{i, j, k} = \max(f_{i - 1, j, k}, f_{i - 1, j - t_i, k - c_i} + w_i)$. In this problem all $w_i$ equal $1$.

Note here that opening yet another dimension for the item index is no longer appropriate, because it easily leads to MLE.

#### Implementation

=== "C++"
    ```cpp
    --8<-- "docs/dp/code/knapsack/knapsack_6.cpp:core"
    ```

=== "Python"
    ```python
    for k in range(1, n + 1):
        for i in range(m, mi - 1, -1):  # one enumeration level over the money
            for j in range(t, ti - 1, -1):  # one enumeration level over the time
                dp[i][j] = max(dp[i][j], dp[i - mi][j - ti] + 1)
    ```

### Knapsack with dependencies

???+ note "[\"Luogu P1064\" Jin Ming's Budget Plan](https://www.luogu.com.cn/problem/P1064)"
    Jin Ming has $n$ yuan and wants to buy $m$ items; the $i$-th item has price $v_i$ and importance $p_i$. Some items are accessories belonging to a main item; to buy such an item, its main item must be bought as well.
    
    The goal is to maximize the sum of $v_i \times p_i$ over all purchased items.

Simply treat it as a [tree knapsack](../tree.md#树上背包). Note that all knapsacks must be merged together at the end.

## References and notes

-   [Nine Lectures on the Knapsack Problem – Cui Tianyi (Chinese)](https://github.com/tianyicui/pack).
