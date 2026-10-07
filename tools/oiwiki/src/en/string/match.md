---
title: String matching
---

This page briefly describes the string matching problem and its solutions.

## The string matching problem

### Definition

Also called pattern matching. The problem can be summarized as: "given strings $S$ and $T$, find the substring $T$ in the text $S$". The string $T$ is called the pattern.

### Types

-   Single-pattern matching: given one pattern and one text, find all positions where the former occurs in the latter.
-   Multi-pattern matching: given several patterns and one text, find all positions where these patterns occur in the text.
    -   If there are several texts, simply concatenate them and treat them as one text.
    -   It can be solved directly as several single-pattern matchings, but that is not efficient enough.
-   Other types: e.g. matching any suffix of a string, matching any suffix of several strings, ...

## Brute force

Abbreviated as the BF (Brute Force) algorithm. The basic idea: start from the first character of the text $S$ and compare it with the first character of the pattern $T$; if they are equal, continue comparing the following characters of both; otherwise, the pattern $T$ goes back to its first character and the comparison restarts from the second character of the text $S$. This repeats until all characters of $S$ or $T$ have been compared.

### Implementation

=== "C++"
    ```cpp
    /*
     * s: the text to search in
     * t: the pattern
     * n: length of the text
     * m: length of the pattern
     */
    std::vector<int> match(char *s, char *t, int n, int m) {
      std::vector<int> ans;
      int i, j;
      for (i = 0; i < n - m + 1; i++) {
        for (j = 0; j < m; j++) {
          if (s[i + j] != t[j]) break;
        }
        if (j == m) ans.push_back(i);
      }
      return ans;
    }
    ```

=== "Python"
    ```python
    def match(s, t, n, m):
        if m < 1:
            return []
    
        ans = []
        for i in range(0, n - m + 1):
            for j in range(0, m):
                if s[i + j] != t[j]:
                    break
            else:
                ans.append(i)
        return ans
    ```

### Time complexity

Let $n$ be the length of the text and $m$ the length of the pattern. Assume $m\ll n$.

When the BF algorithm finds a match: in the best case only one pass succeeds, taking $m$ comparisons, while every other, unsuccessful pass fails at the first character of the pattern, taking another $n-m$ comparisons; the total is $n$ comparisons, so the time complexity is $O(n)$. In the worst case there are $n-m+1$ passes, each taking $m$ comparisons, for a total of $m(n-m+1)$ comparisons, so the time complexity is $O(mn)$.

When the BF algorithm finds no match: in the best case every unsuccessful pass fails at the first character of the pattern, so the BF algorithm performs $n-m+1$ comparisons and the time complexity is $O(n)$; in the worst case every unsuccessful pass fails at the last character of the pattern, so the BF algorithm performs $m(n-m+1)$ comparisons and the time complexity is $O(mn)$.

If the pattern contains at least two distinct characters, the average time complexity of the BF algorithm is $O(n)$. However, the strings given in competitive programming problems are usually not purely random.

## Hashing

See: [String hashing](./hash.md)

## KMP algorithm

See: [Prefix function and KMP algorithm](./kmp.md)
