---
title: Memoized search
---

## Definition

Memoized search is a way of implementing search that records information about states that have already been visited, thereby avoiding visiting the same state repeatedly.

Because memoized search ensures that every state is visited only once, it is also a common way of implementing dynamic programming.

## Introduction

???+ note "[\[NOIP2005\] Herb Gathering](https://www.luogu.com.cn/problem/P1048)"
    There are $M$ different herbs in a cave; gathering each one takes some time $t_i$, and each one has its own value $v_i$. You are given a period of time $T$, during which you can gather some herbs. Maximize the total value of the gathered herbs.
    
    $1 \leq T \leq 10^3$, $1 \leq t_i,v_i,M \leq 100$

### Naive [DFS](../search/dfs.md) approach

It is easy to implement the following naive search: during the search, record three parameters — which item is currently being considered, how much time remains, and how much value has already been obtained — then enumerate whether the current item is chosen and transition to the corresponding state.

???+ note "Implementation"
    === "C++"
        ```cpp
        int n, t;
        int tcost[103], mget[103];
        int ans = 0;
        
        void dfs(int pos, int tleft, int tans) {
          if (tleft < 0) return;
          if (pos == n + 1) {
            ans = max(ans, tans);
            return;
          }
          dfs(pos + 1, tleft, tans);
          dfs(pos + 1, tleft - tcost[pos], tans + mget[pos]);
        }
        
        int main() {
          cin >> t >> n;
          for (int i = 1; i <= n; i++) cin >> tcost[i] >> mget[i];
          dfs(1, t, 0);
          cout << ans << endl;
          return 0;
        }
        ```
    
    === "Python"
        ```python
        tcost = [0] * 103
        mget = [0] * 103
        ans = 0
        
        
        def dfs(pos, tleft, tans):
            global ans
            if tleft < 0:
                return
            if pos == n + 1:
                ans = max(ans, tans)
                return
            dfs(pos + 1, tleft, tans)
            dfs(pos + 1, tleft - tcost[pos], tans + mget[pos])
        
        
        t, n = map(lambda x: int(x), input().split())
        for i in range(1, n + 1):
            tcost[i], mget[i] = map(lambda x: int(x), input().split())
        dfs(1, t, 0)
        print(ans)
        ```

The time complexity of this approach is exponential, and it cannot pass this problem.

### Optimization

Why is the approach above inefficient? Because the same state is visited many times.

If we store the information of each state after processing it, the next time we need to visit that state we can directly use the previously computed information and thus avoid repeated computation. This fully exploits the fact that many dynamic programming problems have a large number of overlapping subproblems, and belongs to the idea of "memoization": trading space for time.

Specifically for this problem, on top of the naive DFS we add an array `mem` to record the return value of every `dfs(pos,tleft)`. Initially every value in `mem` is set to `-1` (meaning "not solved yet"). Every time we need to visit a state, if its value in `mem` is `-1`, we visit the state recursively. Otherwise, we directly use the value already stored in `mem`.

With this processing we ensure that every state is visited only once, so the time complexity of the algorithm is $O(TM)$.

???+ note "Implementation"
    === "C++"
        ```cpp
        int n, t;
        int tcost[103], mget[103];
        int mem[103][1003];
        
        int dfs(int pos, int tleft) {
          if (mem[pos][tleft] != -1)
            return mem[pos][tleft];  // already visited state: directly return the previously recorded value
          if (pos == n + 1) return mem[pos][tleft] = 0;
          int dfs1, dfs2 = -INF;
          dfs1 = dfs(pos + 1, tleft);
          if (tleft >= tcost[pos])
            dfs2 = dfs(pos + 1, tleft - tcost[pos]) + mget[pos];  // state transition
          return mem[pos][tleft] = max(dfs1, dfs2);  // finally store the value of the current state
        }
        
        int main() {
          memset(mem, -1, sizeof(mem));
          cin >> t >> n;
          for (int i = 1; i <= n; i++) cin >> tcost[i] >> mget[i];
          cout << dfs(1, t) << endl;
          return 0;
        }
        ```
    
    === "Python"
        ```python
        tcost = [0] * 103
        mget = [0] * 103
        mem = [[-1 for i in range(1003)] for j in range(103)]
        
        
        def dfs(pos, tleft):
            if mem[pos][tleft] != -1:
                return mem[pos][tleft]
            if pos == n + 1:
                mem[pos][tleft] = 0
                return mem[pos][tleft]
            dfs1 = dfs2 = -INF
            dfs1 = dfs(pos + 1, tleft)
            if tleft >= tcost[pos]:
                dfs2 = dfs(pos + 1, tleft - tcost[pos]) + mget[pos]
            mem[pos][tleft] = max(dfs1, dfs2)
            return mem[pos][tleft]
        
        
        t, n = map(lambda x: int(x), input().split())
        for i in range(1, n + 1):
            tcost[i], mget[i] = map(lambda x: int(x), input().split())
        print(dfs(1, t))
        ```

## Relation to and difference from the iterative approach

When solving dynamic programming problems, the code of memoized search and the code of the iterative (bottom-up) approach are highly similar in form. This is because they use the same state representation and similar state transitions. For this very reason, the time complexities of the two implementations are generally the same.

Below is the code of the iterative implementation (for ease of comparison, without the rolling array optimization); by comparing them, the similarity in form is easy to see.

```cpp
int n, t, w[105], v[105], f[105][1005];

int main() {
  cin >> n >> t;
  for (int i = 1; i <= n; i++) cin >> w[i] >> v[i];
  for (int i = 1; i <= n; i++)
    for (int j = 0; j <= t; j++) {
      f[i][j] = f[i - 1][j];
      if (j >= w[i])
        f[i][j] = max(f[i][j], f[i - 1][j - w[i]] + v[i]);  // state transition equation
    }
  cout << f[n][t];
  return 0;
}
```

When solving dynamic programming problems, both memoized search and the iterative approach ensure that the same state is solved at most once. The way they achieve this differs slightly, however: the iterative approach avoids repeated visits by fixing an explicit visiting order, while memoized search, although it does not fix a visiting order, achieves the same goal by marking states that have already been visited.

Compared with the iterative approach, memoized search does not need to fix a visiting order, so it is sometimes easier to implement and handles boundary cases conveniently; this is a major advantage of memoized search. At the same time, however, memoized search makes it hard to apply optimizations such as rolling arrays, and because of the recursion its running efficiency is lower than that of the iterative approach. Therefore, the more suitable implementation should be chosen depending on the problem.

## How to write a memoized search

### Method 1

1.  Write down the DP states and equation for the problem
2.  write the dfs function based on them
3.  add the memoization array

Example:

$dp_{i} = \max\{dp_{j}+1\}\quad (1 \leq j < i \land a_{j}<a_{i})$ (longest increasing subsequence)

becomes

=== "C++"
    ```cpp
    int dfs(int i) {
      if (mem[i] != -1) return mem[i];
      int ret = 1;
      for (int j = 1; j < i; j++)
        if (a[j] < a[i]) ret = max(ret, dfs(j) + 1);
      return mem[i] = ret;
    }
    
    int main() {
      memset(mem, -1, sizeof(mem));
      // input omitted
      int ret = 0;
      for (int j = 1; j <= n; j++) {
        ret = max(ret, dfs(j));
      }
      cout << ret << endl;
    }
    ```

=== "Python"
    ```python
    def dfs(i):
        if mem[i] != -1:
            return mem[i]
        ret = 1
        for j in range(1, i):
            if a[j] < a[i]:
                ret = max(ret, dfs(j) + 1)
        mem[i] = ret
        return mem[i]
    ```

### Method 2

1.  Write a brute-force search program for the problem (preferably a [dfs](../search/dfs.md))
2.  turn this dfs into a dfs "without external variables"
3.  add the memoization array

Example: the "Herb Gathering" example in this article
