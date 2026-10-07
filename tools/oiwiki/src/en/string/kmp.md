---
title: Prefix function and the KMP algorithm
---

## Definition of string prefix and suffix

For the definitions of prefix, proper prefix, suffix and proper suffix of a string, see [String basics](./basic.md).

## Prefix function

### Definition

Given a string $s$ of length $n$, its **prefix function** is defined as an array $\pi$ of length $n$.
Here $\pi[i]$ is defined as follows:

1.  if the substring $s[0\dots i]$ has a pair of equal proper prefix and proper suffix, $s[0\dots k-1]$ and $s[i - (k - 1) \dots i]$, then $\pi[i]$ is the length of that proper prefix (or proper suffix, since they are equal), i.e. $\pi[i]=k$;
2.  if there is more than one such pair, $\pi[i]$ is the length of the longest one;
3.  if there is no such pair, $\pi[i]=0$.

Simply put, $\pi[i]$ is the length of the longest equal proper prefix and proper suffix of the substring $s[0\dots i]$.

In mathematical terms:

$$
\pi[i] = \max_{k = 0 \dots i}\{k: s[0 \dots k - 1] = s[i - (k - 1) \dots i]\}
$$

In particular, by convention $\pi[0]=0$.

### Procedure

For example, for the string `abcabcd`:

$\pi[0]=0$, because `a` has no proper prefix or proper suffix, so by convention it is 0

$\pi[1]=0$, because `ab` has no equal proper prefix and proper suffix

$\pi[2]=0$, because `abc` has no equal proper prefix and proper suffix

$\pi[3]=1$, because `abca` has exactly one pair of equal proper prefix and proper suffix: `a`, of length 1

$\pi[4]=2$, because the only equal proper prefix and proper suffix of `abcab` is `ab`, of length 2

$\pi[5]=3$, because the only equal proper prefix and proper suffix of `abcabc` is `abc`, of length 3

$\pi[6]=0$, because `abcabcd` has no equal proper prefix and proper suffix

In the same way we compute that the prefix function of the string `aabaaab` is $[0, 1, 0, 1, 2, 2, 3]$.

## Naive algorithm for computing the prefix function

### Procedure

An algorithm that computes the prefix function directly from the definition works as follows:

-   in a loop, compute the values $\pi[i]$ of the prefix function in the order $i = 1\to n - 1$ ($\pi[0]$ is set to $0$);
-   to compute the current value $\pi[i]$, let the variable $j$ start from the largest possible proper prefix length, $i$;
-   if at the current length the proper prefix and proper suffix are equal, this length is $\pi[i]$; otherwise decrease $j$ by 1 and keep matching until $j=0$;
-   if $j = 0$ and there has still been no match, set $\pi[i] = 0$ and move to the next index $i + 1$.

???+ note "Implementation"
    A concrete implementation:
    
    === "C++"
        ```cpp
        // Note:
        // string substr (size_t pos = 0, size_t len = npos) const;
        vector<int> prefix_function(string s) {
          int n = (int)s.length();
          vector<int> pi(n);
          for (int i = 1; i < n; i++)
            for (int j = i; j >= 0; j--)
              if (s.substr(0, j) == s.substr(i - j + 1, j)) {
                pi[i] = j;
                break;
              }
          return pi;
        }
        ```
    
    === "Python"
        ```python
        def prefix_function(s):
            n = len(s)
            pi = [0] * n
            for i in range(1, n):
                for j in range(i, -1, -1):
                    if s[0:j] == s[i - j + 1 : i + 1]:
                        pi[i] = j
                        break
            return pi
        ```
    
    === "Java"
        ```java
        static int[] prefix_function(String s) {
            int n = s.length();
            int[] pi = new int[n];
            for (int i = 1; i < n; i++) {
                for (int j = i; j >= 0; j--) {
                    if (s.substring(0, j).equals(s.substring(i - j + 1, i + 1))) {
                        pi[i] = j;
                        break;
                    }
                }
            }
            return pi;
        }
        ```

Clearly the time complexity of this algorithm is $O(n^3)$, which leaves a lot of room for improvement.

## Efficient algorithm for computing the prefix function

### First optimization

The first important observation is that **adjacent values of the prefix function increase by at most $1$**.

Look at the figure below and reason as follows: if we want $\pi[i+1]$ to be as large as possible, the newly added character $s[i+1]$ must also match its corresponding character, i.e. $s[i+1]=s[\pi[i]]$, and then $\pi[i+1] = \pi[i]+1$.

$$
\underbrace{\overbrace{s_0 ~ s_1 ~ s_2}^{\pi[i] = 3} ~ s_3}_{\pi[i+1] = 4} ~ \dots ~ \underbrace{\overbrace{s_{i-2} ~ s_{i-1} ~ s_{i}}^{\pi[i] = 3} ~ s_{i+1}}_{\pi[i+1] = 4}
$$

So when we move to the next position, the value of the prefix function either increases by one, stays the same, or decreases.

???+ note "Implementation"
    The improved algorithm is now:
    
    === "C++"
        ```cpp
        vector<int> prefix_function(string s) {
          int n = (int)s.length();
          vector<int> pi(n);
          for (int i = 1; i < n; i++)
            for (int j = pi[i - 1] + 1; j >= 0; j--)  // improved: j=i => j=pi[i-1]+1
              if (s.substr(0, j) == s.substr(i - j + 1, j)) {
                pi[i] = j;
                break;
              }
          return pi;
        }
        ```
    
    === "Python"
        ```python
        def prefix_function(s):
            n = len(s)
            pi = [0] * n
            for i in range(1, n):
                for j in range(pi[i - 1] + 1, -1, -1):
                    if s[0:j] == s[i - j + 1 : i + 1]:
                        pi[i] = j
                        break
            return pi
        ```
    
    === "Java"
        ```java
        static int[] prefix_function(String s) {
            int n = s.length();
            int[] pi = new int[n];
            for (int i = 1; i < n; i++) {
                for (int j = pi[i - 1] + 1; j >= 0; j--) {
                    if (s.substring(0, j).equals(s.substring(i - j + 1, i + 1))) {
                        pi[i] = j;
                        break;
                    }
                }
            }
            return pi;
        }
        ```

In this first improved algorithm, the best case when computing each $\pi[i]$ is that the very first string comparison already matches, i.e. the base number of string comparisons is $n-1$.

Since `j = pi[i-1]+1` (with `pi[0]=0`) bounds the maximum number of string comparisons, we can see that the upper bound on the number of comparisons grows by $1$ only in the best case, while every comparison beyond the first consumes room for later growth.

From this we get the case with the most string comparisons: at least $1$ comparison spent and at most $n-2$ comparisons accumulated, giving $n-1 + n-2 = 2n-3$ string comparisons in total.

So after this optimization, computing the prefix function requires only $O(n)$ string comparisons, and the total complexity drops to $O(n^2)$.

### Second optimization

In the first optimization we discussed the best case when computing $\pi[i+1]$: $s[i+1]=s[\pi[i]]$, in which case $\pi[i+1] = \pi[i]+1$. Now let us go a bit further along this line and discuss where to jump when $s[i+1] \neq s[\pi[i]]$.

![](images/prefix_str_1.svg)

As shown in the figure above, on a mismatch we want to find, for the substring $s[0\dots i]$, the second-largest length $j$ after $\pi[i]$ such that the prefix property at position $i$ still holds, i.e. $s[0 \dots j - 1] = s[i - j + 1 \dots i]$:

$$
\overbrace{\underbrace{s_0 ~ s_1}_j ~ s_2 ~ s_3}^{\pi[i]} ~ \dots ~ \overbrace{s_{i-3} ~ s_{i-2} ~ \underbrace{s_{i-1} ~ s_{i}}_j}^{\pi[i]} ~ s_{i+1}
$$

If we find such a length $j$, we only need to compare $s[i + 1]$ and $s[j]$ again. If they are equal, then $\pi[i + 1] = j + 1$. Otherwise we need to find the next length $j^{(2)}$ after $j$ for the substring $s[0\dots i]$ such that the prefix property holds, and so on, until $j = 0$. If $s[i + 1] \neq s[0]$, then $\pi[i + 1] = 0$. The diagram of the second comparison is shown below

![](images/prefix_str_2.svg)

Looking at the figure, we see that because $s[0\dots \pi[i]-1] = s[i-\pi[i]+1\dots i]$, the second-largest length $j$ of $s[0\dots i]$ has the following property:

$$
s[0 \dots j - 1] = s[i - j + 1 \dots i]= s[\pi[i]-j\dots \pi[i]-1]
$$

The diagram for this formula is shown below:

![](images/prefix_str_3.svg)

That is, $j$ equals the value of the prefix function of the substring $s[\pi[i]-1]$, which corresponds to the lower half of the figure, i.e. $j=\pi[\pi[i]-1]$. Similarly, the next length after $j$ equals the value of the prefix function of $s[j-1]$, $j^{(2)}=\pi[j-1]$.

Clearly we obtain a transition equation for $j$: $j^{(n)}=\pi[j^{(n-1)}-1], \ \ (j^{(n-1)}>0)$

### Final algorithm

So in the end we can build an algorithm that performs no string comparisons at all and only $O(n)$ operations.

Moreover, the implementation of this algorithm is surprisingly short and intuitive:

???+ note "Implementation"
    === "C++"
        ```cpp
        vector<int> prefix_function(string s) {
          int n = (int)s.length();
          vector<int> pi(n);
          for (int i = 1; i < n; i++) {
            int j = pi[i - 1];
            while (j > 0 && s[i] != s[j]) j = pi[j - 1];
            if (s[i] == s[j]) j++;
            pi[i] = j;
          }
          return pi;
        }
        ```
    
    === "Python"
        ```python
        def prefix_function(s):
            n = len(s)
            pi = [0] * n
            for i in range(1, n):
                j = pi[i - 1]
                while j > 0 and s[i] != s[j]:
                    j = pi[j - 1]
                if s[i] == s[j]:
                    j += 1
                pi[i] = j
            return pi
        ```
    
    === "Java"
        ```java
        static int[] prefix_function(String s) {
            int n = s.length();
            int[] pi = new int[n];
            for (int i = 1; i < n; i++) {
                int j = pi[i - 1];
                while (j > 0 && s.charAt(i) != s.charAt(j)) {
                    j = pi[j - 1];
                }
                if (s.charAt(i) == s.charAt(j)) {
                    j++;
                }
                pi[i] = j;
            }
            return pi;
        }
        ```

This is an **online** algorithm, i.e. it processes the data as it arrives – for example, you can read the string character by character and process each one immediately to compute the prefix function value for that character. The algorithm still needs to store the string itself and the previously computed prefix function values, but if we know in advance the maximum possible value $M$ of the prefix function of the string, we only need to store the first $M + 1$ characters of the string and the corresponding prefix function values.

## Applications

### Searching for a substring in a string: the Knuth–Morris–Pratt algorithm

The algorithm was published jointly by Knuth, Pratt and Morris in 1977[^kmp]. This task is a typical application of the prefix function.

#### Procedure

Given a text $t$ and a string $s$, we want to find and display all occurrences of $s$ in $t$.

For convenience we denote the length of the string $s$ by $n$ and the length of the text $t$ by $m$.

We construct the string $s + \# + t$, where $\#$ is a separator that appears neither in $s$ nor in $t$. Next we compute the prefix function of this string. Now consider the meaning of the prefix function values after the first $n + 1$ values (those belonging to the string $s$ and the separator). By definition, $\pi[i]$ is the length of the longest proper substring ending at $i$ that is also a prefix; in our case it is the length of the longest substring ending at $i$ that equals a prefix of $s$. Because of the separator, this length cannot exceed $n$. If the equality $\pi[i] = n$ holds, it means that $s$ appears in full at that position (i.e. its right end is at position $i$). Note that this index is relative to the string $s + \# + t$.

Therefore, if $\pi[i] = n$ holds at some position $i$, the string $s$ occurs in the string $t$ at position $i - (n - 1) - (n + 1) = i - 2n$. The figure below shows the index diagram.

![](./images/strstr_kmp_indices.svg)

As already mentioned when computing the prefix function, if we know that the prefix function values never exceed a certain bound, we do not need to store the whole string and the whole prefix function, only the beginning of both. In our case this means that it suffices to store the string $s + \#$ and the corresponding prefix function values. We can read the string $t$ one character at a time and compute the prefix function value at the current position.

Thus the Knuth–Morris–Pratt algorithm (KMP algorithm for short) solves the problem in $O(n + m)$ time and $O(n)$ memory.

???+ note "Implementation"
    === "C++"
        ```cpp
        vector<int> find_occurrences(string text, string pattern) {
          string cur = pattern + '#' + text;
          int sz1 = text.size(), sz2 = pattern.size();
          vector<int> v;
          vector<int> lps = prefix_function(cur);
          for (int i = sz2 + 1; i <= sz1 + sz2; i++) {
            if (lps[i] == sz2) v.push_back(i - 2 * sz2);
          }
          return v;
        }
        ```
    
    === "Python"
        ```python
        def find_occurrences(t, s):
            cur = s + "#" + t
            sz1, sz2 = len(t), len(s)
            ret = []
            lps = prefix_function(cur)
            for i in range(sz2 + 1, sz1 + sz2 + 1):
                if lps[i] == sz2:
                    ret.append(i - 2 * sz2)
            return ret
        ```
    
    === "Java"
        ```java
        static List<Integer> find_occurrences(String text, String pattern) {
            String cur = pattern + '#' + text;
            int sz1 = text.length(), sz2 = pattern.length();
            List<Integer> v = new ArrayList<>();
            int[] lps = prefix_function(cur);
            for (int i = sz2 + 1; i <= sz1 + sz2; i++) {
                if (lps[i] == sz2) {
                    v.add(i - 2 * sz2);
                }
            }
            return v;
        }
        ```

### Period of a string

For a string $s$ and $0 < p \le |s|$, if $s[i] = s[i+p]$ holds for all $i \in [0, |s| - p - 1]$, then $p$ is called a period of $s$.

For a string $s$ and $0 \le r < |s|$, if the prefix of length $r$ and the suffix of length $r$ of $s$ are equal, the prefix of length $r$ is called a border of $s$.

From the fact that $s$ has a border of length $r$ it follows that $|s|-r$ is a period of $s$.

By the definition of the prefix function, we obtain the lengths of all borders of $s$, namely $\pi[n-1],\pi[\pi[n-1]-1], \ldots$.[^ref1]

Therefore, using the prefix function we can compute all periods of $s$ in $O(n)$ time. In particular, since $\pi[n-1]$ is the length of the longest border of $s$, $n - \pi[n-1]$ is the smallest period of $s$.

### Counting the occurrences of each prefix

In this section we discuss two problems at once. Given a string $s$ of length $n$, in the first variant of the problem we want to count the occurrences of each prefix $s[0 \dots i]$ in the same string, and in the second variant we want to count the occurrences of each prefix $s[0 \dots i]$ in another given string $t$.

Let us first solve the first problem. Consider the prefix function value $\pi[i]$ at position $i$. By definition it means that a prefix of $s$ of length $\pi[i]$ occurs at position $i$ with its right end at $i$, and that no longer prefix satisfies this. At the same time, shorter prefixes may also end at this position. It is easy to see that we have run into the question already answered when computing the prefix function: given a prefix of length $j$ that is also a suffix ending at $i$, what is the next smaller length $k < j$ of a prefix that is also a suffix ending at $i$? Therefore, ending at position $i$ there is a prefix of length $\pi[i]$, a prefix of length $\pi[\pi[i] - 1]$, a prefix of length $\pi[\pi[\pi[i] - 1] - 1]$, and so on, until the length becomes $0$. Hence we can compute the answer as follows.

???+ note "Implementation"
    === "C++"
        ```cpp
        vector<int> ans(n + 1);
        for (int i = 0; i < n; i++) ans[pi[i]]++;
        for (int i = n - 1; i > 0; i--) ans[pi[i - 1]] += ans[i];
        for (int i = 0; i <= n; i++) ans[i]++;
        ```
    
    === "Python"
        ```python
        ans = [0] * (n + 1)
        for i in range(0, n):
            ans[pi[i]] += 1
        for i in range(n - 1, 0, -1):
            ans[pi[i - 1]] += ans[i]
        for i in range(0, n + 1):
            ans[i] += 1
        ```

#### Explanation

In the code above we first count how many times each prefix function value occurs in the array $\pi$, and then compute the final answer: if we know that the prefix of length $i$ occurs exactly $\text{ans}[i]$ times, this value must be added to the number of occurrences of its longest substring that is both a suffix and a prefix. Finally, to count the original prefixes themselves, we add $1$ to each result.

Now consider the second problem. We apply the trick from Knuth–Morris–Pratt: construct the string $s + \# + t$ and compute its prefix function. The only difference from the first problem is that we only care about the prefix function values related to the string $t$, i.e. $\pi[i]$ for $i \ge n + 1$. With these values we apply the same algorithm as in the first problem.

### Number of distinct substrings of a string

Given a string $s$ of length $n$, we want to compute the number of its distinct substrings.

We will solve this problem iteratively. In other words, knowing the current number of distinct substrings, we want to find a way to recompute this number after appending one character to the end of $s$.

Let $k$ be the current number of distinct substrings of $s$. We append a new character $c$ to $s$. Obviously some new substrings ending with the character $c$ will appear. We want to count those substrings ending with this character that we have not encountered before.

Construct the string $t = s + c$ and reverse it to get the string $t^{\sim}$. Now our task becomes counting how many prefixes of $t^{\sim}$ do not appear anywhere else in $t^{\sim}$. If we compute the maximum value $\pi_{\max}$ of the prefix function of $t^{\sim}$, then the longest prefix that occurs in $s$ has length $\pi_{\max}$. Naturally, all shorter prefixes occur as well.

Therefore the number of new substrings that appear after adding a new character is $|s| + 1 - \pi_{\max}$.

So for each added character we can compute the number of new substrings in $O(n)$ time, and the final complexity is $O(n^2)$.

It is worth noting that we can also recompute the number of distinct substrings when adding a character at the front, or when removing a character from the end or the front.

### String compression

Given a string $s$ of length $n$, we want to find its shortest "compressed" representation, i.e. we want to find a shortest string $t$ such that $s$ can be represented as a concatenation of one or more copies of $t$.

Obviously we only need to find the length of $t$. Knowing this length, the answer to the problem is the prefix of $s$ of that length.

Let us compute the prefix function of $s$. Using its last value $\pi[n - 1]$, we define the value $k = n - \pi[n - 1]$. We will show that if $k$ divides $n$, then $k$ is the answer; otherwise there is no valid compression, and the answer is $n$.

Assume $n$ is divisible by $k$. Then the string can be divided into blocks of length $k$. By the definition of the prefix function, the prefix of length $n - k$ of the string equals its suffix. But this means that the last block equals the second-to-last block, the second-to-last block equals the third-to-last, and so on. As a result all blocks are equal, so we can compress the string $s$ to length $k$.

???+ note "Proof"
    Admittedly, we still need to prove that this value is optimal. Indeed, if there were a compressed representation shorter than $k$, the last value of the prefix function $\pi[n - 1]$ would have to be greater than $n - k$. Therefore $k$ is the answer.
    
    Now assume $n$ is not divisible by $k$; we will prove by contradiction that this implies the answer is $n$[^1]. Suppose the shortest compressed representation $r$ has length $p$ ($p$ divides $n$) and the string $s$ is divided into $n / p \ge 2$ blocks. Then the last value of the prefix function $\pi[n - 1]$ must be greater than $n - p$ (if it were equal, $n$ would be divisible by $k$), i.e. the suffix it represents partially covers the first block. Now consider the second block of the string. This block has two interpretations: the first is $r_0 r_1 \dots r_{p - 1}$, and the other is $r_{p - k} r_{p - k + 1} \dots r_{p - 1} r_0 r_1 \dots r_{p - k - 1}$. Since both interpretations correspond to the same string, we obtain a system of $p$ equations, which can be written briefly as $r_{(i + k) \bmod p} = r_{i \bmod p}$, where $\cdot \bmod p$ denotes the least non-negative residue modulo $p$.
    
    $$
    \begin{gathered}
    \overbrace{r_0 ~ r_1 ~ r_2 ~ r_3 ~ r_4 ~ r_5}^p ~ \overbrace{r_0 ~ r_1 ~ r_2 ~ r_3 ~ r_4 r_5}^p \\
    r_0 ~ r_1 ~ r_2 ~ r_3 ~ \underbrace{\overbrace{r_0 ~ r_1 ~ r_2 ~ r_3 ~ r_4 ~ r_5}^p ~ r_0 ~ r_1}_{\pi[11] = 8}
    \end{gathered}
    $$
    
    By the extended Euclidean algorithm we can obtain $x$ and $y$ such that $xk + yp = \gcd(k, p)$. By suitably adding the equation $pk - kp = 0$ we can obtain $x' > 0$ and $y' < 0$ such that $x'k + y'p = \gcd(k, p)$. This means that by repeatedly applying the equations of the system above we obtain a new system $r_{(i + \gcd(k, p)) \bmod p} = r_{i \bmod p}$.
    
    Since $\gcd(k, p)$ divides $p$, this means that $\gcd(k, p)$ is a period of $r$. Moreover, since $\pi[n - 1] > n - p$, we have $n - \pi[n - 1] = k < p$, so $\gcd(k, p)$ is a period of $r$ smaller than $p$. Therefore the string $s$ has a compressed representation of length $\gcd(k, p) < p$, contradicting the minimality of $p$.
    
    In summary, there is no compressed representation of length less than $k$, so the answer is $k$.

[^1]: In both the Russian and the English version this part of the proof appears to be flawed. This part of the proof was added by the authors of this article.

### Building an automaton from the prefix function

Let us return to the string obtained by joining two strings with a separator. For strings $s$ and $t$ we compute the prefix function of $s + \# + t$. Obviously, since $\#$ is a separator, the prefix function value never exceeds $|s|$. Therefore we only need to store the string $s + \#$ and its corresponding prefix function values, and afterwards we can compute the prefix function values for all subsequent characters on the fly:

$$
\underbrace{s_0 ~ s_1 ~ \dots ~ s_{n-1} ~ \#}_{\text{need to store}} ~ \underbrace{t_0 ~ t_1 ~ \dots ~ t_{m-1}}_{\text{do not need to store}}
$$

In fact, in this situation knowing the next character $c$ of $t$ and the prefix function value at the previous position is enough to compute the prefix function value at the next position, without using any other characters of $t$ or their prefix function values.

In other words, we can build an **automaton** (a finite state machine): its states are the current prefix function values, and the transition from one state to another is determined by the next character.

Thus, even without the string $t$, we can use the algorithm for building a transition table to build a table $( \text { old } \pi , c ) \rightarrow \text { new } _ { - } \pi$:

???+ note "Implementation"
    ```cpp
    void compute_automaton(string s, vector<vector<int>>& aut) {
      s += '#';
      int n = s.size();
      vector<int> pi = prefix_function(s);
      aut.assign(n, vector<int>(26));
      for (int i = 0; i < n; i++) {
        for (int c = 0; c < 26; c++) {
          int j = i;
          while (j > 0 && 'a' + c != s[j]) j = pi[j - 1];
          if ('a' + c == s[j]) j++;
          aut[i][c] = j;
        }
      }
    }
    ```

However, in this form, for the lowercase alphabet, the time complexity of the algorithm is $O(|\Sigma|n^2)$. Note that we can apply dynamic programming to reuse the already computed parts of the table. As soon as we move from the value $j$ to $\pi[j - 1]$, we are in fact saying that the transition $(j, c)$ leads to the same state as the transition $(\pi[j - 1], c)$, and that answer has already been computed exactly.

???+ note "Implementation"
    ```cpp
    void compute_automaton(string s, vector<vector<int>>& aut) {
      s += '#';
      int n = s.size();
      vector<int> pi = prefix_function(s);
      aut.assign(n, vector<int>(26));
      for (int i = 0; i < n; i++) {
        for (int c = 0; c < 26; c++) {
          if (i > 0 && 'a' + c != s[i])
            aut[i][c] = aut[pi[i - 1]][c];
          else
            aut[i][c] = i + ('a' + c == s[i]);
        }
      }
    }
    ```

In the end we can build this automaton in $O(|\Sigma|n)$ time.

When is this automaton useful? First, recall that most of the time we use the prefix function of the string $s + \# + t$ for one purpose: finding all occurrences of the string $s$ in the string $t$.

Therefore the most direct benefit of this automaton is **speeding up the computation of the prefix function of the string $s + \# + t$**.

By building the automaton for $s + \#$, we no longer need to store the string $s$ and its prefix function values. All transitions have already been computed in the table.

But besides that, there is a second, less direct application. We can use the automaton to speed up the computation when the string $t$ is **some gigantic string built according to certain rules**. Gray strings, or a string built by recursively combining several short input strings, are examples of this.

For completeness, let us solve the following problem: given a number $k \le 10^5$ and a string $s$ of length $\le 10^5$, we need to compute the number of occurrences of $s$ in the $k$-th Gray string. Recall that Gray strings are defined as follows:

$$
\begin{aligned}
g_1 &= \mathtt{a}\\
g_2 &= \mathtt{aba}\\
g_3 &= \mathtt{abacaba}\\
g_4 &= \mathtt{abacabadabacaba}
\end{aligned}
$$

Because of their astronomical length, in this case it is impossible even to construct the string $t$: the $k$-th Gray string has $2^k - 1$ characters. However, knowing only the first few prefix function values, we can efficiently compute the prefix function value at the end of this string.

Besides the automaton, we also need to compute the values $G[i][j]$: the state of the automaton after processing $g_i$ starting from state $j$, and the values $K[i][j]$: the number of occurrences of $s$ in $g_i$ when $g_i$ is processed starting from state $j$. In fact, $K[i][j]$ is the number of times the prefix function took the value $|s|$ during this process. It is easy to see that the answer to the problem is $K[k][0]$.

How do we compute these values? First, by definition, the initial conditions are $G[0][j] = j$ and $K[0][j] = 0$. All subsequent values can be computed from the previous values using the automaton. To compute the values for some $i$, recall that the string $g_i$ is the concatenation of $g_{i - 1}$, the $i$-th character of the alphabet, and $g_{i - 1}$. Therefore the automaton passes through the following states:

$$
\begin{gathered}
\text{mid} = \text{aut}[G[i - 1][j]][i] \\
G[i][j] = G[i - 1][\text{mid}]
\end{gathered}
$$

The value of $K[i][j]$ can also be computed simply.

$$
K[i][j] = K[i - 1][j] + [\text{mid} == |s|] + K[i - 1][\text{mid}]
$$

Here $[\cdot]$ equals $1$ when the expression inside is true and $0$ otherwise. In summary, we can now solve the problem about Gray strings, as well as a large class of similar problems. For example, the same method solves the following problem: given a string $s$ and some patterns $t_i$, where each pattern is given as follows: the pattern consists of ordinary characters, among which previous strings may be recursively inserted in the form $t_{k}^{\text{cnt}}$, i.e. at that position we must insert the string $t_k$ $\text{cnt}$ times. Here is an example of such patterns:

$$
\begin{aligned}
t_1 &= \mathtt{abdeca} \\
t_2 &= \mathtt{abc} + t_1^{30} + \mathtt{abd} \\
t_3 &= t_2^{50} + t_1^{100} \\
t_4 &= t_2^{10} + t_3^{100}
\end{aligned}
$$

The recursive substitutions make the string lengths explode; their lengths can even reach the order of $100^{100}$. And we must find the number of occurrences of the string $s$ in each of these strings.

This problem can likewise be solved by building the automaton of the prefix function. As before, we compute the transitions for each pattern using the previously computed results and count the answer accordingly.

## Practice problems

-   [UVa 455 "Periodic Strings"](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=396)
-   [UVa 11022 "String Factoring"](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1963)
-   [UVa 11452 "Dancing the Cheeky-Cheeky"](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=2447)
-   [UVa 12604 - Caesar Cipher](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4282)
-   [UVa 12467 - Secret Word](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3911)
-   [UVa 11019 - Matrix Matcher](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1960)
-   [SPOJ - Pattern Find](http://www.spoj.com/problems/NAJPF/)
-   [Codeforces - Anthem of Berland](http://codeforces.com/contest/808/problem/G)
-   [Codeforces - MUH and Cube Walls](http://codeforces.com/problemset/problem/471/D)

## References and notes

**This page is mainly translated from the blog post [Префикс-функция. Алгоритм Кнута-Морриса-Пратта](http://e-maxx.ru/algo/prefix_function) and its English translation [Prefix function. Knuth–Morris–Pratt algorithm](https://cp-algorithms.com/string/prefix-function.html). The Russian version is licensed under Public Domain + Leave a Link; the English version under CC-BY-SA 4.0.**

[^ref1]: [Jin Ce – Selected lectures on string algorithms (Chinese)](https://github.com/hzwer/shareOI/blob/master/%E5%AD%97%E7%AC%A6%E4%B8%B2/%E5%AD%97%E7%AC%A6%E4%B8%B2%E7%AE%97%E6%B3%95%E9%80%89%E8%AE%B2_%E9%87%91%E7%AD%96.pdf)

[^kmp]: Knuth, Donald E., James H. Morris, Jr, and Vaughan R. Pratt. "Fast pattern matching in strings." SIAM journal on computing 6.2 (1977): 323-350.[doi: 10.1137/0206024](https://epubs.siam.org/doi/abs/10.1137/0206024)
