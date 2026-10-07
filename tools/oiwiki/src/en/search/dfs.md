---
title: DFS (search)
---

## Introduction

DFS is a concept from graph theory; see the page [DFS (graph theory)](../graph/dfs.md). In **search algorithms** the term usually refers to an algorithm that uses a recursive function to conveniently implement brute-force enumeration; it is somewhat similar to the graph-theoretic DFS, but not exactly the same.

## Explanation

Consider this example:

???+ note "Example"
    Split a positive integer $n$ into $3$ positive integers, e.g. $6=1+2+3$, where each later number must be greater than or equal to the previous one. Print all the ways.

How would we solve this problem without knowing about search? With a triple loop, of course; reference code:

???+ note "Implementation"
    === "C++"
        ```cpp
        for (int i = 1; i <= n; ++i)
          for (int j = i; j <= n; ++j)
            for (int k = j; k <= n; ++k)
              if (i + j + k == n) printf("%d = %d + %d + %d\n", n, i, j, k);
        ```
    
    === "Python"
        ```python
        for i in range(1, n + 1):
            for j in range(i, n + 1):
                for k in range(j, n + 1):
                    if i + j + k == n:
                        print("%d = %d + %d + %d" % (n, i, j, k))
        ```
    
    === "Java"
        ```Java
        for (int i = 1; i < n + 1; i++) {
            for (int j = i; j < n + 1; j++) {
                for (int k = j; k < n + 1; k++) {
                    if (i + j + k == n) System.out.printf("%d = %d + %d + %d%n", n, i, j, k);
                }
            }
        }
        ```

What if we have to split into four integers? Add another loop? And what if we have to split into at most $m$ integers?

That is where recursive search comes in. The characteristic of this kind of search algorithm is that the search target is divided into several "levels"; at each level a decision is made based on the states of the previous levels, until the target state is reached.

Consider the problem above: split a positive integer $n$ into a sum of at most $m$ positive integers such that each later number is greater than or equal to the previous one, and print all the ways.

Suppose one way splits the positive integer $n$ into the sum of $k$ positive integers $a_1, a_2, \ldots, a_k$. Divide the problem into levels, where the $i$-th level decides $a_i$. To make the decision at level $i$ we need to record three state variables: $n-\sum_{j=1}^i{a_j}$, the sum of all remaining integers; $a_{i-1}$, the integer from the previous level, to make sure the integers are non-decreasing; and $i$, to make sure we print at most $m$ integers. To record the way we use an array `arr` whose $i$-th entry is $a_i$. Note that `arr` is in fact a stack of length $i$.

The code is as follows:

???+ note "Implementation"
    === "C++"
        ```cpp
        int m, arr[103];  // arr records the current way
        
        void dfs(int n, int i, int a) {
          if (n == 0) {
            for (int j = 1; j <= i - 1; ++j) printf("%d ", arr[j]);
            printf("\n");
          }
          if (i <= m) {
            for (int j = a; j <= n; ++j) {
              arr[i] = j;
              dfs(n - j, i + 1, j);  // Think carefully about what this line means.
            }
          }
        }
        
        // main program
        scanf("%d%d", &n, &m);
        dfs(n, 1, 1);
        ```
    
    === "Python"
        ```python
        arr = [0] * 103  # arr records the current way
        
        
        def dfs(n, i, a):
            if n == 0:
                print(arr[1:i])
            if i <= m:
                for j in range(a, n + 1):
                    arr[i] = j
                    dfs(n - j, i + 1, j)  # Think carefully about what this line means.
        
        
        # main program
        n, m = map(int, input().split())
        dfs(n, 1, 1)
        ```
    
    === "Java"
        ```Java
        static int m;
        
        // arr records the current way
        static int[] arr = new int[103];
        
        public static void dfs(int n, int i, int a) {
            if (n == 0) {
                for (int j = 1; j <= i - 1; j++) System.out.printf("%d ", arr[j]);
                System.out.println();
            }
            if (i <= m) {
                for (int j = a; j <= n; ++j) {
                    arr[i] = j;
                    dfs(n - j, i + 1, j); // Think carefully about what this line means.
                }
            }
        }
        
        // main program
        final int N = new Scanner(System.in).nextInt();
        m = new Scanner(System.in).nextInt();
        dfs(N, 1, 1);
        ```

## Worked example

???+ note "[Luogu P1706 Permutations](https://www.luogu.com.cn/problem/P1706)"
    ```cpp
    --8<-- "docs/search/code/dfs/dfs_1.cpp"
    ```
