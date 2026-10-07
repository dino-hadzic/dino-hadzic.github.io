---
title: Lyndon factorization
---

author: sshwy, StudyingFather, orzAtalod

## Definition

We first introduce the concept of Lyndon factorization.

Lyndon string: for a string $s$, if $s$ is lexicographically strictly smaller than all suffixes of $s$, we call $s$ a simple string, or a **Lyndon string**. For example, `a`, `b`, `ab`, `aab`, `abb`, `ababb`, and `abcd` are Lyndon strings. If and only if $s$ is lexicographically strictly smaller than all its nontrivial cyclic shifts (nontrivial means nonempty and different from the string itself), $s$ is a Lyndon string.

Lyndon factorization: the Lyndon factorization of a string $s$ is denoted by $s=w_1w_2\cdots w_k$, where all $w_i$ are simple strings in nonincreasing lexicographic order, that is, $w_1\ge w_2\ge\cdots\ge w_k$. Such a factorization exists and is unique.

## Duval's algorithm

### Explanation

Duval's algorithm finds the Lyndon factorization of a string in $O(n)$ time.

First, we introduce another concept: if a string $t$ can be written as $t=ww\cdots\overline{w}$, where $w$ is a Lyndon string and $\overline{w}$ is a prefix of $w$ ($\overline{w}$ may be empty), then $t$ is called a pre-simple string, or a pre-Lyndon string. A Lyndon string is also a pre-Lyndon string.

Duval's algorithm uses a greedy approach. During the algorithm, we split the string $s$ into three parts, $s=s_1s_2s_3$: $s_1$ is a Lyndon string whose Lyndon factorization has already been recorded; $s_2$ is a pre-Lyndon string; and $s_3$ is the unprocessed part.

### Procedure

At a high level, the algorithm repeatedly tries to append the first character of $s_3$ to $s_2$. If $s_2$ ceases to be a pre-Lyndon string, we can cut off a prefix of $s_2$ (its Lyndon factors) and append it to $s_1$.

Let us describe the procedure in more detail. Define a pointer $i$ to the first character of $s_2$; $i$ moves from $1$ to $n$ (the string length). Within the loop, define another pointer $j$ to the first character of $s_3$, and a pointer $k$ to the character currently being considered in $s_2$ (the character corresponding to $j$ in the previous repetition in $s_2$). We want to append $s[j]$ to $s_2$, so we compare $s[j]$ with $s[k]$:

1.  If $s[j]=s[k]$, appending $s[j]$ to $s_2$ preserves the pre-simple property. We only need to increment the pointers $j,k$ (move them to the next position).
2.  If $s[j]>s[k]$, then $s_2s[j]$ becomes a Lyndon string. We increment $j$ and move $k$ to the first character of $s_2$, so $s_2$ becomes a new Lyndon string with one repetition.
3.  If $s[j]<s[k]$, then $s_2s[j]$ is not pre-simple. We must split off a Lyndon substring of $s_2$, of length $j-k$, which is one repetition. Replace $s_2$ with the remaining part and continue (note that the pointers $j,k$ are unchanged in this case) until all complete repetitions have been removed. For the leftover part, simply "rewind" to its beginning.

### Implementation

The following code returns the Lyndon factorization of the string $s$.

=== "C++"
    ```cpp
    // duval_algorithm
    vector<string> duval(string const& s) {
      int n = s.size(), i = 0;
      vector<string> factorization;
      while (i < n) {
        int j = i + 1, k = i;
        while (j < n && s[k] <= s[j]) {
          if (s[k] < s[j])
            k = i;
          else
            k++;
          j++;
        }
        while (i <= k) {
          factorization.push_back(s.substr(i, j - k));
          i += j - k;
        }
      }
      return factorization;
    }
    ```

=== "Python"
    ```python
    # duval_algorithm
    def duval(s):
        n, i = len(s), 0
        factorization = []
        while i < n:
            j, k = i + 1, i
            while j < n and s[k] <= s[j]:
                if s[k] < s[j]:
                    k = i
                else:
                    k += 1
                j += 1
            while i <= k:
                factorization.append(s[i : i + j - k])
                i += j - k
        return factorization
    ```

### Complexity analysis

We now prove the complexity of this algorithm.

The outer loop runs at most $n$ times because $i$ increases each time. The second inner loop also takes $O(n)$ time, since it only records the Lyndon factorization. Now consider the first inner loop. Each Lyndon string found in an outer iteration is longer than the remaining string that we have compared, so the sum of the lengths of these remaining strings is less than $n$. Thus the inner loop performs at most $O(n)$ iterations. In fact, the total number of iterations does not exceed $4n-3$, and the time complexity is $O(n)$.

## Minimal representation (finding the smallest cyclic shift)

For a length-$n$ string $s$, we can use the algorithm above to find its minimal representation.

Construct the Lyndon factorization of $ss$, then find a Lyndon string $t$ in this factorization whose starting position is less than $n$ and whose ending position is at least $n$. Using the properties of Lyndon factorization, it is easy to prove that the first character of the substring $t$ is the first character of the minimal representation of $s$. In other words, starting at the beginning of $t$, the next $n$ characters form the minimal representation of $s$.

Thus, during factorization it suffices to record the beginning of each pre-Lyndon string.

=== "C++"
    ```cpp
    // smallest_cyclic_string
    string min_cyclic_string(string s) {
      s += s;
      int n = s.size();
      int i = 0, ans = 0;
      while (i < n / 2) {
        ans = i;
        int j = i + 1, k = i;
        while (j < n && s[k] <= s[j]) {
          if (s[k] < s[j])
            k = i;
          else
            k++;
          j++;
        }
        while (i <= k) i += j - k;
      }
      return s.substr(ans, n / 2);
    }
    ```

=== "Python"
    ```python
    # smallest_cyclic_string
    def min_cyclic_string(s):
        s += s
        n = len(s)
        i, ans = 0, 0
        while i < n / 2:
            ans = i
            j, k = i + 1, i
            while j < n and s[k] <= s[j]:
                if s[k] < s[j]:
                    k = i
                else:
                    k += 1
                j += 1
            while i <= k:
                i += j - k
        return s[ans : ans + n / 2]
    ```

## Exercises

-   [UVa #719 - Glass Beads](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=660)

    **This page is mainly translated from the blog post [Декомпозиция Линдона. Алгоритм Дюваля. Нахождение наименьшего циклического сдвига](http://e-maxx.ru/algo/duval_algorithm) and its English translation [Lyndon factorization](https://cp-algorithms.com/string/lyndon_factorization.html). The Russian version is licensed under Public Domain + Leave a Link; the English version is licensed under CC-BY-SA 4.0.**
