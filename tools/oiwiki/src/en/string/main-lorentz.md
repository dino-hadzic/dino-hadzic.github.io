---
title: Main–Lorentz algorithm
---

## Tandem repetitions

### Definition

Given a length-$n$ string $s$.

A string obtained by writing a string twice in a row is called a **tandem repetition**. For precision, we call the repeated string the base string below. Equivalently, a tandem repetition is a pair of indices $(i, j)$ such that $s[i \dots j]$ is the concatenation of two identical strings.

The goal is to find all tandem repetitions in the given string $s$. Alternatively, solve a simpler problem: find any tandem repetition in $s$, or the longest one.

The algorithm below was proposed by Michael Main and Richard J. Lorentz in 1982.

???+ note "Conventions"
    All string indices below start at $0$.
    
    Let $\overline{s}$ denote the reverse of $s$. For example, $\overline{\tt abc} = \tt cba$.

### Explanation

Consider the string $\tt acababaee$. It contains three tandem repetitions:

-   $s[2 \dots 5] = \tt abab$
-   $s[3 \dots 6] = \tt baba$
-   $s[7 \dots 8] = \tt ee$

As another example, the string $\tt abaaba$ contains only two tandem repetitions:

-   $s[0 \dots 5] = \tt abaaba$
-   $s[2 \dots 3] = \tt aa$

### Number of tandem repetitions

A string of length $n$ may contain as many as $O(n^2)$ tandem repetitions. An obvious example is a string of $n$ identical letters: every even-length substring is a tandem repetition. In general, a periodic string with a short period has many tandem repetitions.

Nevertheless, we can count tandem repetitions in $O(n \log n)$ time, because the algorithm uses a compressed representation that combines multiple repetitions into one.

Here are some interesting facts about the number of tandem repetitions:

-   A tandem repetition whose base string is not itself a tandem repetition is called a **primitive repetition**. One can prove that there are at most $O(n \log n)$ primitive repetitions.
-   A tandem repetition can be compressed as a Crochemore triple $(i, p, r)$, where $i$ is its starting position, $p$ is the length of a repeating unit (not necessarily the base string!), and $r$ is the number of repetitions of that unit. All tandem repetitions of a string can then be represented by $O(n \log n)$ Crochemore triples.
-   Fibonacci strings are defined as follows:

$$
\begin{align} t_0 &= a, \\ t_1 &= b, \\ t_i &= t_{i-1} + t_{i-2}, \end{align}
$$

Fibonacci strings are highly periodic. For a length-$f_i$ Fibonacci string $t_i$, even compression with Crochemore triples yields $O(f_i \log f_i)$ triples. Its number of primitive repetitions is also $O(f_i \log f_i)$.

## Main–Lorentz algorithm

### Explanation

The core idea of the Main–Lorentz algorithm is **divide and conquer**.

Split the string into left and right parts. First count the tandem repetitions lying entirely in the left or right part, then count those starting in the left part and ending in the right part. Below, we call these **crossing repetitions**.

Counting crossing repetitions is the key to the Main–Lorentz algorithm and is discussed in detail below.

### Procedure

#### Finding crossing repetitions

Denote the left part by $u$ and the right part by $v$. Then $s = u + v$, and the lengths of $u, v$ are each approximately half the length of $s$.

Consider the middle character of a tandem repetition, defined here as the first character of its right half. In other words, if $s[i...j]$ is a tandem repetition, its middle character is $s[(i + j + 1)/2]$. A repetition is called **left** if its middle character lies in $u$, and **right** otherwise.

We next discuss how to find all left repetitions.

Let the length of a left repetition be $2l$. Consider its first character in $v$, namely $s[|u|]$. In $u$, there must be an equal character $u[\textit{cntr}]$.

Fix $\textit{cntr}$ and find all matching repetitions. For example, in $\tt c \; \underset{\textit{cntr}}{a} \; c \; | \; a \; d \; a$ (where $\tt |$ separates the left and right parts), fixing $cntr = 1$ gives the repetition $\tt caca$.

Fixing $\textit{cntr}$ clearly also fixes $l$. Once we know how to find all repetitions for a fixed value, we can enumerate values from $0$ to $|u| - 1$ for $\textit{cntr}$ and find all matching repetitions.

#### Identifying left repetitions

Even with $\textit{cntr}$ fixed, multiple repetitions may satisfy the conditions. How do we find them all?

Consider another example: in $\tt abcabcac$, take the repetition $\overbrace{\tt a}^{l_1} \overbrace{\underset{\textit{cntr}}{\tt b} \tt c}^{l_2} \overbrace{\tt a}^{l_1}  \; | \; \overbrace{\tt b \; \tt c}^{l_2}$. Let $l_1$ be the length from the repetition's first character through $s[\textit{cntr} - 1]$, and $l_2$ the length from $s[\textit{cntr}]$ through the last character of the repetition's left base string.

We can now give a **necessary and sufficient condition** for a substring of length $2l = 2(l_1 + l_2) = 2(|u| - \textit{cntr})$ to be a tandem repetition:

Let $k_1$ be the largest integer satisfying $u[\textit{cntr} - k_1 \dots \textit{cntr} - 1] = u[|u| - k_1 \dots |u| - 1]$, and $k_2$ the largest integer satisfying $u[\textit{cntr} \dots \textit{cntr} + k_2 - 1] = v[0 \dots k_2 - 1]$. Under the conditions $l_1 \leq k_1$ and $l_2 \leq k_2$, each pair $(l_1, l_2)$ then corresponds to exactly one tandem repetition.

To summarize:

-   Fix $\textit{cntr}$.
-   All repetitions sought have length $2l = 2(|u| - \textit{cntr})$. There may still be several, depending on $l_1$ and $l_2$.
-   Compute $k_1$ and $k_2$ as defined above.
-   All matching repetitions satisfy:

$$
\begin{align} l_1 + l_2 &= l = |u| - \textit{cntr} \\ l_1 &\le k_1, \\ l_2 &\le k_2. \\ \end{align}
$$

It remains to compute $k_1$ and $k_2$ efficiently. Using the [Z-function](./z-func.md), we can obtain them in $O(1)$ time:

-   For $k_1$, compute the Z-function of $\overline{u}$.
-   For $k_2$, compute the Z-function of $v + \# + u$, where $\#$ is a character occurring in neither $u$ nor $v$.

#### Right repetitions

Finding right repetitions is almost identical to finding left repetitions. Consider the character at the boundary in $u$, namely $s[|u| - 1]$. It must equal a character in $v$; denote that character's position in $v$ by $\textit{cntr}$.

Let $k_1$ be the largest integer satisfying $v[\textit{cntr} - k_1 + 1 \dots \textit{cntr}] = u[|u| - k_1 \dots |u| - 1]$, and $k_2$ the largest integer satisfying $v[\textit{cntr} + 1 \dots \textit{cntr} + k_2] = v[0 \dots k_2 - 1]$. Computing the Z-functions of $\overline{u} + \# + \overline{v}$ and $v$ yields $k_1$ and $k_2$, respectively.

Enumerate $\textit{cntr}$ and use the analogous procedure to find right repetitions.

### Implementation

The Main–Lorentz algorithm describes all tandem repetitions with quadruples $(\textit{cntr}, l, k_1, k_2)$. If we only need to count repetitions or find the longest one, these quadruples contain enough information. By the [master theorem](../basic/complexity.md#master-theorem), the time complexity is $O(n \log n)$.

Note that extracting the starting and ending positions of every repetition from these quadruples takes $O(n^2)$ time in the worst case. The implementation below does this and stores all repetition endpoints in `repetitions`.

```cpp
vector<int> z_function(string const& s) {
  int n = s.size();
  vector<int> z(n);
  for (int i = 1, l = 0, r = 0; i < n; i++) {
    if (i <= r) z[i] = min(r - i + 1, z[i - l]);
    while (i + z[i] < n && s[z[i]] == s[i + z[i]]) z[i]++;
    if (i + z[i] - 1 > r) {
      l = i;
      r = i + z[i] - 1;
    }
  }
  return z;
}

int get_z(vector<int> const& z, int i) {
  if (0 <= i && i < (int)z.size())
    return z[i];
  else
    return 0;
}

vector<pair<int, int>> repetitions;

void convert_to_repetitions(int shift, bool left, int cntr, int l, int k1,
                            int k2) {
  for (int l1 = max(1, l - k2); l1 <= min(l, k1); l1++) {
    if (left && l1 == l) break;
    int l2 = l - l1;
    int pos = shift + (left ? cntr - l1 : cntr - l - l1 + 1);
    repetitions.emplace_back(pos, pos + 2 * l - 1);
  }
}

void find_repetitions(string s, int shift = 0) {
  int n = s.size();
  if (n == 1) return;

  int nu = n / 2;
  int nv = n - nu;
  string u = s.substr(0, nu);
  string v = s.substr(nu);
  string ru(u.rbegin(), u.rend());
  string rv(v.rbegin(), v.rend());

  find_repetitions(u, shift);
  find_repetitions(v, shift + nu);

  vector<int> z1 = z_function(ru);
  vector<int> z2 = z_function(v + '#' + u);
  vector<int> z3 = z_function(ru + '#' + rv);
  vector<int> z4 = z_function(v);

  for (int cntr = 0; cntr < n; cntr++) {
    int l, k1, k2;
    if (cntr < nu) {
      l = nu - cntr;
      k1 = get_z(z1, nu - cntr);
      k2 = get_z(z2, nv + 1 + cntr);
    } else {
      l = cntr - nu + 1;
      k1 = get_z(z3, nu + 1 + nv - 1 - (cntr - nu));
      k2 = get_z(z4, (cntr - nu) + 1);
    }
    if (k1 + k2 >= l) convert_to_repetitions(shift, cntr < nu, cntr, l, k1, k2);
  }
}
```

**This page is mainly translated from the blog post [Поиск всех тандемных повторов в строке. Алгоритм Мейна-Лоренца](http://e-maxx.ru/algo/string_tandems) and its English translation [Finding repetitions](https://cp-algorithms.com/string/main_lorentz.html). The Russian version is licensed under Public Domain + Leave a Link; the English version is licensed under CC-BY-SA 4.0.**
