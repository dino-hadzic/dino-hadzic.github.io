---
title: Manacher
---

## Description

Given a length-$n$ string $s$, find all pairs $(i, j)$ such that the substring $s[i \dots j]$ is a palindrome. If $t = t_{\text{rev}}$, then $t$ is a palindrome ($t_{\text{rev}}$ is the reverse of $t$).

## Explanation

Clearly, there can be $O(n^2)$ palindromes in the worst case, so at first glance there seems to be no linear-time algorithm for this problem.

However, information about palindromes can be expressed **more compactly**: for every position $i = 0 \dots n - 1$, find the values $d_1[i]$ and $d_2[i]$. They represent the numbers of odd-length and even-length palindromes centered at position $i$, respectively. Equivalently, they are the radii of the longest palindromes centered at $i$ (both radii $d_1[i]$, $d_2[i]$ count the characters from position $i$ through the palindrome's rightmost position, inclusive).

For example, the string $s = \mathtt{abababc}$ has three odd-length palindromes centered at $s[3] = b$. The longest has radius $3$, so $d_1[3] = 3$:

$$
a\ \overbrace{b\ a\ \underset{s_3}{b}\ a\ b}^{d_1[3]=3}\ c
$$

The string $s = \mathtt{cbaabd}$ has two even-length palindromes centered at $s[3] = a$. The longest has radius $2$, so $d_2[3] = 2$:

$$
c\ \overbrace{b\ a\ \underset{s_3}{a}\ b}^{d_2[3]=2}\ d
$$

The key idea is that if position $i$ is the center of a palindrome of length $l$, then $i$ is also the center of palindromes of lengths $l - 2$, $l - 4$, and so on. Therefore, the two arrays $d_1[i]$ and $d_2[i]$ suffice to describe all palindromic substrings of the string.

Surprisingly, there is a fairly simple linear-time algorithm for computing these two "palindrome arrays", $d_1[]$ and $d_2[]$. This article describes it in detail.

## Solutions

There are several ways to solve this problem: string hashing gives an $O(n \log n)$ solution, while suffix arrays and fast LCA give an $O(n)$ solution.

However, the algorithm described here is **much** simpler and has smaller constants in both time and space complexity. It was proposed by **Glenn K. Manacher** in 1975.

## Naive algorithm

To avoid ambiguity later, let us specify what we mean by the "naive algorithm".

For each center $i$, the algorithm compares a pair of corresponding characters and tries to increase the answer by $1$ for as long as possible.

This algorithm is slow: it takes $O(n^2)$ time to compute the answer.

Here is an implementation of the naive algorithm:

???+ note "Implementation"
    === "C++"
        ```cpp
        vector<int> d1(n), d2(n);
        for (int i = 0; i < n; i++) {
          d1[i] = 1;
          while (0 <= i - d1[i] && i + d1[i] < n && s[i - d1[i]] == s[i + d1[i]]) {
            d1[i]++;
          }
        
          d2[i] = 0;
          while (0 <= i - d2[i] - 1 && i + d2[i] < n &&
                 s[i - d2[i] - 1] == s[i + d2[i]]) {
            d2[i]++;
          }
        }
        ```
    
    === "Python"
        ```python
        d1 = [0] * n
        d2 = [0] * n
        for i in range(0, n):
            d1[i] = 1
            while 0 <= i - d1[i] and i + d1[i] < n and s[i - d1[i]] == s[i + d1[i]]:
                d1[i] += 1
        
            d2[i] = 0
            while 0 <= i - d2[i] - 1 and i + d2[i] < n and s[i - d2[i] - 1] == s[i + d2[i]]:
                d2[i] += 1
        ```

## Manacher's algorithm

Here we only describe how to find all odd-length palindromic substrings, that is, how to compute $d_1[]$. Finding all even-length palindromic substrings (computing $d_2[]$) only requires minor modifications to the odd-length algorithm.

To compute the answer efficiently, maintain the **boundaries $[l, r]$** of the rightmost palindromic substring found so far (the palindrome with the greatest $r$, where $l$ and $r$ are its left and right boundary positions). Initially set $l = 0$ and $r = -1$ (*-1* is not a reverse index here; any negative number works, and it is used only to simplify loop initialization).

### Procedure

Suppose we now want to process the next $i$ and compute $d_1[i]$, and all previous values in $d_1[]$ have already been computed. Proceed as follows:

-   If $i$ lies outside the current palindromic substring, that is, $i > r$, use the naive algorithm.

    Keep increasing $d_1[i]$, checking at each step whether the current substring $[i - d_1[i] \dots i + d_1[i]]$ is a palindrome ($d_1[i]$ denotes the radius, here and below). Stop at the first pair of unequal characters or at a boundary of $s$. In either case, $d_1[i]$ has been computed. Remember to update $(l, r)$ afterward.

-   Now consider $i \le r$. We try to obtain information from the previously computed values of $d_1[]$. Within the palindrome $(l, r)$, first reflect position $i$, obtaining $j = l + (r - i)$. Consider $d_1[j]$. Since $j$ is symmetric to $i$, we can **almost always** set $d_1[i] = d_1[j]$. The idea is illustrated below (think of "copying" the palindrome centered at $j$ to the position centered at $i$):

    $$
    \ldots\
    \overbrace{
        s_l\ \ldots\
        \underbrace{
            s_{j-d_1[j]+1}\ \ldots\ s_j\ \ldots\ s_{j+d_1[j]-1}
        }_\text{palindrome}\
        \ldots\
        \underbrace{
            s_{i-d_1[j]+1}\ \ldots\ s_i\ \ldots\ s_{i+d_1[j]-1}
        }_\text{palindrome}\
        \ldots\ s_r
    }^\text{palindrome}\
    \ldots
    $$

    However, there is a **tricky case** that must be handled correctly: the "inner" palindrome reaches the boundary of the "outer" palindrome, that is, $j - d_1[j] + 1 \le l$ (equivalently, $i + d_1[j] - 1 \ge r$). Symmetry is not guaranteed outside the "outer" palindrome, so simply setting $d_1[i] = d_1[j]$ would be incorrect: we do not have enough information to assert that the palindrome at $i$ has the same length.

    To handle this case correctly, "truncate" the palindrome by setting $d_1[i] = r - i + 1$. Then run the naive algorithm to increase $d_1[i]$ as much as possible.

    This case is illustrated below (the palindrome centered at $j$ has been truncated to fit inside the "outer" palindrome):

    $$
    \ldots\
    \overbrace{
        \underbrace{
            s_l\ \ldots\ s_j\ \ldots\ s_{j+(j-l)}
        }_\text{palindrome}\
        \ldots\
        \underbrace{
            s_{i-(r-i)}\ \ldots\ s_i\ \ldots\ s_r
        }_\text{palindrome}
    }^\text{palindrome}\
    \underbrace{
        \ldots \ldots \ldots \ldots \ldots
    }_\text{try moving here}
    $$

    The illustration shows that although the palindrome centered at $j$ may be longer and extend beyond the "outer" palindrome, at position $i$ we can only use the part fully contained inside the "outer" palindrome. The answer at $i$ may nevertheless be larger, so we next run the naive algorithm to try extending it beyond the "outer" palindrome, into the region labeled "try moving here".

Finally, after computing each $d_1[i]$, remember to update $(l, r)$.

To reiterate, the algorithm for computing the even-length palindrome array $d_2[]$ is very similar to the one above for the odd-length palindrome array $d_1[]$.

## Complexity of Manacher's algorithm

Since the naive algorithm is used when computing the answer for a particular position, the linear time complexity may not be obvious at first glance.

A closer analysis, however, shows that the complexity is linear. Note that the [algorithm for computing the Z-function](./z-func.md) is similar and also runs in linear time.

Indeed, each iteration of the naive algorithm increases $r$ by $1$, and $r$ never decreases throughout the algorithm. These observations imply that the naive algorithm performs $O(n)$ iterations in total.

The rest of Manacher's algorithm is clearly linear as well, so the total complexity is $O(n)$.

## Implementation of Manacher's algorithm

### Handling the cases separately

To compute $d_1[]$, use the following code:

=== "C++"
    ```cpp
    vector<int> d1(n);
    for (int i = 0, l = 0, r = -1; i < n; i++) {
      int k = (i > r) ? 1 : min(d1[l + r - i], r - i + 1);
      while (0 <= i - k && i + k < n && s[i - k] == s[i + k]) {
        k++;
      }
      d1[i] = k--;
      if (i + k > r) {
        l = i - k;
        r = i + k;
      }
    }
    ```

=== "Python"
    ```python
    d1 = [0] * n
    l, r = 0, -1
    for i in range(0, n):
        k = 1 if i > r else min(d1[l + r - i], r - i + 1)
        while 0 <= i - k and i + k < n and s[i - k] == s[i + k]:
            k += 1
        d1[i] = k
        k -= 1
        if i + k > r:
            l = i - k
            r = i + k
    ```

The code for computing $d_2[]$ is very similar, with slight differences in the arithmetic expressions:

=== "C++"
    ```cpp
    vector<int> d2(n);
    for (int i = 0, l = 0, r = -1; i < n; i++) {
      int k = (i > r) ? 0 : min(d2[l + r - i + 1], r - i + 1);
      while (0 <= i - k - 1 && i + k < n && s[i - k - 1] == s[i + k]) {
        k++;
      }
      d2[i] = k--;
      if (i + k > r) {
        l = i - k - 1;
        r = i + k;
      }
    }
    ```

=== "Python"
    ```python
    d2 = [0] * n
    l, r = 0, -1
    for i in range(0, n):
        k = 0 if i > r else min(d2[l + r - i + 1], r - i + 1)
        while 0 <= i - k - 1 and i + k < n and s[i - k - 1] == s[i + k]:
            k += 1
        d2[i] = k
        k -= 1
        if i + k > r:
            l = i - k - 1
            r = i + k
    ```

### Unified handling

Although the explanation and implementations above handle $d_1[]$ and $d_2[]$ separately, a trick lets us reduce both computations to that of $d_1[]$.

Given a length-$n$ string $s$, into each of its $n + 1$ gaps insert a separator $\#$, producing a length-$2n + 1$ string $s'$. For example, $s = \mathtt{abababc}$ becomes $s' = \mathtt{\#a\#b\#a\#b\#a\#b\#c\#}$.

Each $\#$ between letters represents the corresponding "gap" in $s$. The two end separators $\#$ are added for implementation convenience.

After processing $s'$ to compute $d_1[]$, at any position $i$, the longest palindromic substring described by $d_1[i]$ must end with $\#$ (if it ended with a letter, the $\#$ on each side would allow one more outward extension). Thus, a maximal palindrome in $s$ centered on a letter, of length $m + 1$, corresponds in $s'$ to a maximal palindrome centered on the same letter, of length $2m + 3$. A maximal palindrome in $s$ centered on a gap, of length $m$, corresponds in $s'$ to a maximal palindrome centered on the corresponding $\#$, of length $2m + 1$ (in both cases $m$ is even, but this does not affect the conclusion). Combining these observations with a little calculation, we find that in $s'$, $d_1[i]$ equals **the total length plus one** of the maximal palindromic substring centered at the corresponding position in $s$.

This establishes the relationship between the arrays for $s'$, namely $d_1[]$, and those for $s$, namely $d_1[]$ and $d_2[]$.

Since this unified approach processes $s'$ to compute $d_1[]$, once $s'$ has been constructed, the code is the same as the code for $d_1[]$ in the previous section.

## Practice problems

-   [UVa #11475 "Extend to Palindrome"](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2470)
-   [National training team: Longest double palindrome](https://www.luogu.com.cn/problem/P4555)
-   [CF1326D2. Labyrinth](https://codeforces.com/contest/1326/problem/D2)

**This page is mainly translated from the blog post [Нахождение всех подпалиндромов](http://e-maxx.ru/algo/palindromes_count) and its English translation [Finding all sub-palindromes in $O(N)$](https://cp-algorithms.com/string/manacher.html). The Russian version is licensed under Public Domain + Leave a Link; the English version is licensed under CC-BY-SA 4.0.**
