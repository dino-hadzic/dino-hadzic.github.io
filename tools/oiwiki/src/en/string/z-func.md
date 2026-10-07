---
title: Z-function (extended KMP)
---

Convention: string indices start at $0$.

## Definition

For a string $s$ of length $n$, define the function $z[i]$ as the length of the longest common prefix (LCP) of $s$ and $s[i,n-1]$ (i.e. the suffix starting at $s[i]$); the array $z$ is called the **Z-function** of $s$. In particular, $z[0] = 0$.

Outside China the algorithm computing this array is usually called the **Z Algorithm**, while in China it is called **extended KMP** (exKMP).

This article presents an algorithm that computes the Z-function in $O(n)$ time, together with its various applications.

## Explanation

The following examples show the Z-function of several strings:

-   $z(\mathtt{aaaaa}) = [0, 4, 3, 2, 1]$
-   $z(\mathtt{aaabaab}) = [0, 2, 1, 0, 2, 1, 0]$
-   $z(\mathtt{abacaba}) = [0, 0, 1, 0, 3, 0, 1]$

## Naive algorithm

The naive algorithm for the Z-function has complexity $O(n^2)$:

???+ note "Implementation"
    === "C++"
        ```cpp
        vector<int> z_function_trivial(string s) {
          int n = (int)s.length();
          vector<int> z(n);
          for (int i = 1; i < n; ++i)
            while (i + z[i] < n && s[z[i]] == s[i + z[i]]) ++z[i];
          return z;
        }
        ```
    
    === "Python"
        ```python
        def z_function_trivial(s):
            n = len(s)
            z = [0] * n
            for i in range(1, n):
                while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                    z[i] += 1
            return z
        ```

## Linear algorithm

As with most algorithms in the string topics, the key is to use the idea of an automaton to find a state transition function under the given constraints, so that previously computed states can be used to speed up the computation of new ones.

In this algorithm we compute the values $z[i]$ in order from $1$ to $n-1$ ($z[0]=0$). While computing $z[i]$ we make use of the already computed $z[0],\ldots,z[i-1]$.

For $i$, we call the interval $[i,i+z[i]-1]$ the **match segment** of $i$, also known as the Z-box.

During the algorithm we maintain the match segment with the rightmost right endpoint. For convenience, denote it by $[l,r]$. By definition, $s[l,r]$ is a prefix of $s$. While computing $z[i]$ we guarantee that $l\le i$. Initially $l=r=0$.

While computing $z[i]$:

-   If $i\le r$, then by the definition of $[l,r]$ we have $s[i,r] = s[i-l,r-l]$, hence $z[i]\ge \min(z[i-l],r-i+1)$. Then:
    -   if $z[i-l] < r-i+1$, then $z[i] = z[i-l]$;
    -   otherwise $z[i-l]\ge r-i+1$; in this case we set $z[i] = r-i+1$ and then extend $z[i]$ by brute-force comparing the following characters until it can no longer be extended.
-   If $i>r$, we simply follow the naive algorithm: start comparing from $s[i]$ and compute $z[i]$ by brute force.
-   After computing $z[i]$, if $i+z[i]-1>r$, we need to update $[l,r]$, i.e. set $l=i, r=i+z[i]-1$.

You can visit [this website](https://personal.utdallas.edu/~besp/demo/John2010/z-algorithm.htm) to see a simulation of the Z-function.

### Implementation

=== "C++"
    ```cpp
    vector<int> z_function(string s) {
      int n = (int)s.length();
      vector<int> z(n);
      for (int i = 1, l = 0, r = 0; i < n; ++i) {
        if (i <= r && z[i - l] < r - i + 1) {
          z[i] = z[i - l];
        } else {
          z[i] = max(0, r - i + 1);
          while (i + z[i] < n && s[z[i]] == s[i + z[i]]) ++z[i];
        }
        if (i + z[i] - 1 > r) l = i, r = i + z[i] - 1;
      }
      return z;
    }
    ```

=== "Python"
    ```python
    def z_function(s):
        n = len(s)
        z = [0] * n
        l, r = 0, 0
        for i in range(1, n):
            if i <= r and z[i - l] < r - i + 1:
                z[i] = z[i - l]
            else:
                z[i] = max(0, r - i + 1)
                while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                    z[i] += 1
            if i + z[i] - 1 > r:
                l = i
                r = i + z[i] - 1
        return z
    ```

## Complexity analysis

Each execution of the inner `while` loop moves $r$ to the right by at least $1$, and $r< n-1$, so it is executed at most $n$ times in total.

The outer loop is just a single linear pass.

The total complexity is $O(n)$.

## Applications

We now consider applications of the Z-function in several concrete situations.

These applications are largely similar to those of the [prefix function](./kmp.md).

### Finding all occurrences of a substring

To avoid confusion, we call $t$ the **text** and $p$ the **pattern**. The problem is: find all occurrences of the pattern $p$ in the text $t$.

To solve it, we construct a new string $s = p + \diamond + t$, i.e. we concatenate $p$ and $t$ but put a separator character $\diamond$ between them (we choose $\diamond$ so that it certainly does not occur in $p$ or $t$).

First we compute the Z-function of $s$. Then, for every $i$ in the interval $[0,|t| - 1]$, we consider the Z-function value $k = z[i + |p| + 1]$ of the suffix of $s$ starting at $t[i]$. If $k = |p|$, we know that there is an occurrence of $p$ at position $i$ of $t$; otherwise there is no occurrence of $p$ at position $i$ of $t$.

Its time complexity (and also its space complexity) is $O(|t| + |p|)$.

### Number of distinct substrings

Given a string $s$ of length $n$, compute the number of distinct substrings of $s$.

Consider computing the increment: knowing the current number of distinct substrings of $s$, compute the number of distinct substrings after appending one character to the end of $s$.

Let $k$ be the current number of distinct substrings of $s$. We append a new character $c$ to the end of $s$. Obviously some new substrings ending with $c$ will appear (substrings ending with $c$ that have not appeared before).

Let the string $t$ be the reverse of $s + c$ (the reverse is the string formed by the characters of the original string in reverse order). Our task is to count how many prefixes of $t$ do not appear elsewhere in $t$. Compute the Z-function of $t$ and find its maximum value $z_{\max}$. Then the reverses of the prefixes of $t$ of length at most $z_{\max}$ are substrings ending with $c$ that have already appeared in $s$.

Therefore the number of new substrings after appending the character $c$ to $s$ is $|t| - z_{\max}$.

The time complexity of the algorithm is $O(n^2)$.

It is worth noting that with the same method we can, in $O(n)$ time, recompute the number of distinct substrings after adding or removing one character at an endpoint (at the end or at the front).

### Whole period of a string

Given a string $s$ of length $n$, find its shortest whole period, i.e. find a shortest string $t$ such that $s$ can be represented as a concatenation of several copies of $t$.

Compute the Z-function of $s$; the length of the whole period is then the smallest divisor $i$ of $n$ satisfying $i+z[i]=n$.

The proof of this fact is the same as the proof in the applications of the [prefix function](./kmp.md).

## Practice problems

-   [Luogu P5410 [template] Extended KMP/exKMP (Z-function)](https://www.luogu.com.cn/problem/P5410)
-   [Luogu P7114 [NOIP2020] String matching](https://www.luogu.com.cn/problem/P7114)
-   [CF126B Password](http://codeforces.com/problemset/problem/126/B)
-   [UVa # 455 Periodic Strings](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=396)
-   [UVa # 11022 String Factoring](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1963)
-   [UVa 11475 - Extend to Palindrome](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=2470)
-   [Codechef - Chef and Strings](https://www.codechef.com/problems/CHSTR)
-   [Codeforces - Prefixes and Suffixes](http://codeforces.com/problemset/problem/432/D)
-   [Leetcode 2223 - Sum of Scores of Built Strings](https://leetcode.com/problems/sum-of-scores-of-built-strings/)

**This page is mainly translated from the blog post [Z-функция строки и её вычисление](http://e-maxx.ru/algo/z_function) and its English translation [Z-function and its calculation](https://cp-algorithms.com/string/z-function.html). The Russian version is licensed under Public Domain + Leave a Link; the English version under CC-BY-SA 4.0.**
