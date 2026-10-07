---
title: String hashing
---

## Definition

We define a function $f$ that maps strings to integers; this $f$ is called a hash function.

We want this function $f$ to help us conveniently decide whether two strings are equal.

## The idea of hashing

The core idea of hashing is to map the input into a range of values that is relatively small and easy to compare.

??? warning "Warning"
    "Relatively small range of values" means different things in different situations.
    
    In a [hash table](../ds/hash.md), the range must be small enough that linear space and time complexity are acceptable.
    
    In string hashing, the range must be small enough that values can be compared quickly ($10^9$ and $10^{18}$ can both be compared quickly).
    
    At the same time, to reduce the collision rate, the range must not be too small either.

## Properties

Concretely, the most important properties of a hash function can be summarized in the following two points:

1.  when the hash values differ, the two strings are definitely different;

2.  when the hash values are equal, the two strings are not necessarily equal (but they are equal with high probability, and of course we hope they always are).

    The phenomenon where the hash values are equal but the original strings differ is called a hash collision.

## Explanation

What do we need to pay attention to?

Time complexity and the accuracy of the hash.

We usually use a polynomial hash: for a string $s$ of length $l$, the polynomial hash function can be defined as $f(s) = \sum_{i=1}^{l} s[i] \times b^{l-i} \pmod M$. For example, for the string $xyz$, the hash value is $xb^2+yb+z$.

It should be pointed out that many people use another definition of the hash function, namely $f(s) = \sum_{i=1}^{l} s[i] \times b^{i-1} \pmod M$; under this definition, the hash value of the same string $xyz$ becomes $x+yb+zb^2$.

Obviously both definitions of the hash function work, but the formulas used to compute substring hashes, discussed later, differ between them, so be very careful **not to confuse these two hashing schemes**.

Since the former definition is simpler to compute, more widely used, and can be understood by analogy with a base-$b$ number, the rest of this article discusses only the hash function defined by $f(s) = \sum_{i=1}^{l} s[i] \times b^{l-i} \pmod M$.

Also, for convenience and to enlarge the modulus, in C++ we sometimes use `unsigned long long` for the result of the hash function. Due to the semantics of C++, this amounts to setting the modulus $M$ to $2^{64}$, which is also a good choice.

Accuracy is discussed below.

## Error analysis of hashing

### Hash collisions

A hash collision means that two different strings map to the same hash value.

Let $d$ be the size of the hash value space (the number of all possible values) and $n$ the number of computations (the number of strings to be hashed).

Then the probability of a hash collision is:

$$
p(n,d) = 1 - \frac{d!}{d^n\left(d-n\right)!} \approx 1 - \exp(-\frac{n(n-1)}{2d} )
$$

??? note "Proof"
    When every hash value is generated with equal probability, the probability of no collision is:
    
    $$
    \overline{p}(n,d) = 1 \cdot \left (1 - \frac{1}{d} \right) \cdot \left ( 1- \frac{2}{d}\right) \cdots \left ( 1- \frac{n-1}{d}\right)
    $$
    
    Simplifying, we get:
    
    $$
    \begin{aligned}
    \overline{p}(n,d) 
    & = \frac{d}{d}\cdot \frac{d-1}{d}\cdot \frac{d-2}{d} \cdots \frac{d-n+1}{d}\\
    & = \frac{d\cdot (d-1)\cdot (d-2)\cdots(d-n+1)}{d^n}\\
    & = \frac{d!}{d^n\left(d-n\right)!}
    \end{aligned}
    $$
    
    So the probability of a hash collision is:
    
    $$
    p(n,d) = 1 - \frac{d!}{d^n\left(d-n\right)!}
    $$
    
    This formula is still too complicated, so we simplify it further.
    
    By Taylor's formula:
    
    $$
    \exp(x) = \sum_{k=0}^{\infty}\frac{x^k}{k!}=1+x+\frac{x^2}{2}+\frac{x^3}{6}+\frac{x^4}{24}+\cdots
    $$
    
    When $x$ is very small, $\exp(x)$ approaches $1+x$.
    
    Substituting this into the original formula for no collision:
    
    $$
    \overline{p}(n,d) \approx 1 \cdot \exp(-\frac{1}{d}) \cdot \exp(-\frac{2}{d}) \cdots \exp(-\frac{n-1}{d})
    $$
    
    Simplifying:
    
    $$
    \begin{aligned}
    \overline{p}(n,d) & \approx \exp(-\frac{1}{d} - \frac{2}{d} - \cdots -\frac{n-1}{d})\\
    &=\exp(-\frac{n(n-1)}{2d} )
    \end{aligned}
    $$
    
    So the probability of a hash collision is:
    
    $$
    p(n,d) \approx 1 - \exp(-\frac{n(n-1)}{2d})
    $$

### Breaking a large-modulus hash

Look at this formula:

$$
p(n,d) \approx 1 - \exp(-\frac{n(n-1)}{2d} )
$$

To break the hash (force a collision), the following conditions must hold:

1.  $d$ must be larger than the modulus.
2.  $1-p(d,n)$ should be as small as possible.

An example:

If the alphabet consists of **uppercase and lowercase letters and digits**, and the modulus is $10^9+7$:

$\log_{62}10^9+7\approx 6$

$p(10^6,62^{6}) \approx 0.9$

So within this range, if we randomly generate $10^6$ strings of length $6$, the probability that two of them have the same hash value is as high as $90\%$.

### Breaking a natural-overflow hash

Because the modulus of this hash is too large, it cannot be broken by the method above, so we need another method.

First, this hash has the form $f(s) = \sum_{i=1}^{l} s[i] \times b^{l-i}$; we consider cases according to $b$.

#### Even b

Then $f(s) = s_1\cdot b^l + s_2\cdot b^{l-1} + \cdots + s_l\cdot b \pmod M$, where $M$ is $2^{64}$.

It is easy to see that if $l \ge 64$, then $s_i\cdot b^l \equiv 0 \pmod M$.

So we only need to construct strings of the form:

`aaa...a`

`baa...a`

with length greater than $64$ to get a collision.

#### Odd b

Define $!s_i$ as $s_i$ with all characters flipped.

Example:

$s_i = abaab$

$!s_i = babba$

i.e. `a` becomes `b` and `b` becomes `a`.

Further define $hash_i$ as the hash value of $s_i$ and $!hash_i$ as the hash value of $!s_i$.

Repeatedly construct $s_i = s_{i-1} + !s_{i-1}$.

$s_{12}$ and $!s_{12}$ are the two strings we want.

??? note "Derivation"
    First, we have:
    
    $$
    \begin{aligned}
    hash_i = hash_{i-1}\cdot base^{2^{i-2}} + !hash_{i-1}\\
    !hash_{i} = !hash_{i-1}\cdot base^{2^{i-2}}+hash_{i-1}
    \end{aligned}
    $$
    
    Try subtracting:
    
    $$
    \begin{aligned}
    &hash_i - !hash_i\\
    =\ &hash_{i-1}\cdot base^{2^{i-2}} + !hash_{i-1}-(!hash_{i-1}\cdot base^{2^{i-2}}+hash_{i-1})\\
    =\ &(hash_{i-1}-!hash_{i-1})\cdot (base^{2^{i-2}}-1)
    \end{aligned}
    $$
    
    A $2^i$ has appeared, but the original expression is too complicated, so let us substitute:
    
    Let:
    
    $$
    \begin{aligned}
    f_i = hash_i - !hash_i\\
    g_i = base^{2^{i-2}}-1
    \end{aligned}
    $$
    
    From the original expression we get:
    
    $$
    \begin{aligned}
    f_i &= f_{i-1} \cdot g_i\\
        &=f_1 \cdot g_1 \cdot g_2 \cdots g_{i-1}\\
    \end{aligned}
    $$
    
    Since $base^{2^{i-2}}$ is always odd, $g_i$ is always even.
    
    Therefore:
    
    $$
    2^{i-1} | f_i
    $$
    
    But this is too large: we would need $i-1\ge 64$ to break the hash; simplify further:
    
    $$
    g_i = base^{2^{i-2}}-1 = (base^{2^{i-3}}-1)\cdot(base^{2^{i-3}}+1)\\
    $$
    
    i.e. $g_i$ has the form $g_{i-1} \cdot c\ (c \equiv 0 \pmod 2)$.
    
    So $2 | s_1$, $4 | s_2$, ..., i.e.
    
    $$
    \begin{aligned}
    & 2^i &| g_i\\
    &2^1\cdot2^2\cdot2^3\cdots2^{i-1} &| f_i\\
    &2^{i(i-1)/2} &| f_i
    \end{aligned}
    $$
    
    i.e. already at $i=12$ we get $2^{64} | hash_i - !hash_i$, as required.

### Example problems

???+ note "[Example: BZOJ 3097 Hash Killer I](https://hydro.ac/p/bzoj-P3097)"
    Given a hash implemented with **natural overflow**, construct a string that breaks it.

???+ note "[Example: BZOJ 3097 Hash Killer II](https://hydro.ac/p/bzoj-P3098)"
    Given a hash implemented with a **large modulus**, construct a string that breaks it.

???+ note "[Example: Luogu U461211 String Hash (strengthened data)](https://www.luogu.com.cn/problem/U461211)"
    Given $n$ strings, determine how many distinct strings there are.

## Improvements to hashing

### Multi-value hashing

After so many ways to break hashes, of course there are also remedies.

Multi-value hashing means having several hash functions, each with a different modulus; this solves the problem of hash collisions.

When comparing, if any one of the hash values differs, the two strings are considered different; if all hash values are equal, the strings are considered equal.

Generally, double hashing is enough.

### Multiple substring hash queries

Computing the hash value of a string once has complexity $O(n)$, where $n$ is the length of the string, which is no different from brute-force matching; if we need to query the hash values of substrings of a string many times, recomputing each time is very inefficient.

The usual approach is to precompute the hash value of every prefix of the whole string, treating the hash value as a base-$b$ number taken modulo $M$; then the hash of any substring can be computed quickly:

Let $f_i(s)$ denote $f(s[1..i])$, i.e. the hash value of the prefix of length $i$ of the original string; then by definition $f_i(s)=s[1]\cdot b^{i-1}+s[2]\cdot b^{i-2}+\dots+s[i-1]\cdot b+s[i]$

Now we want to quickly compute $f(s[l..r])$ in a way similar to prefix sums; by definition the hash value of the string $s[l..r]$ is $f(s[l..r])=s[l]\cdot b^{r-l}+s[l+1]\cdot b^{r-l-1}+\dots+s[r-1]\cdot b+s[r]$

Comparing the two expressions above, we find that $f(s[l..r])=f_r(s)-f_{l-1}(s) \times b^{r-l+1}$ holds (you can verify it by substituting by hand), so with this formula we can quickly obtain the hash of a substring. Here $b^{r-l+1}$ can be precomputed in $O(n)$ and then each query answered in $O(1)$ (of course one can also answer each query in $O(\log n)$ with fast exponentiation).

## Implementation

### Modular hash:

Note: relatively slow, not recommended in practice.

=== "C++"
    ```cpp
    using std::string;
    
    constexpr int M = 1e9 + 7;
    constexpr int B = 233;
    
    using ll = long long;
    
    int get_hash(const string& s) {
      int res = 0;
      for (int i = 0; i < s.size(); ++i) {
        res = ((ll)res * B + s[i]) % M;
      }
      return res;
    }
    
    bool cmp(const string& s, const string& t) {
      return get_hash(s) == get_hash(t);
    }
    ```

=== "Python"
    ```python
    M = int(1e9 + 7)
    B = 233
    
    
    def get_hash(s):
        res = 0
        for char in s:
            res = (res * B + ord(char)) % M
        return res
    
    
    def cmp(s, t):
        return get_hash(s) == get_hash(t)
    ```

### Double hash:

=== "C++"
    ```cpp
    using ull = unsigned long long;
    ull base = 131;
    ull mod1 = 212370440130137957, mod2 = 1e9 + 7;
    
    ull get_hash1(std::string s) {
      int len = s.size();
      ull ans = 0;
      for (int i = 0; i < len; i++) ans = (ans * base + (ull)s[i]) % mod1;
      return ans;
    }
    
    ull get_hash2(std::string s) {
      int len = s.size();
      ull ans = 0;
      for (int i = 0; i < len; i++) ans = (ans * base + (ull)s[i]) % mod2;
      return ans;
    }
    
    bool cmp(const std::string s, const std::string t) {
      bool f1 = get_hash1(s) != get_hash1(t);
      bool f2 = get_hash2(s) != get_hash2(t);
      return f1 || f2;
    }
    ```

=== "Python"
    ```python
    def get_hash1(s: str) -> int:
        base = 131
        mod1 = 212370440130137957
        ans = 0
        for char in s:
            ans = (ans * base + ord(char)) % mod1
        return ans
    
    
    def get_hash2(s: str) -> int:
        base = 131
        mod2 = 1000000007
        ans = 0
        for char in s:
            ans = (ans * base + ord(char)) % mod2
        return ans
    
    
    def cmp(s: str, t: str) -> bool:
        f1 = get_hash1(s) != get_hash1(t)
        f2 = get_hash2(s) != get_hash2(t)
        return f1 or f2
    ```

## Applications of hashing

### String matching

Compute the hash value of the pattern, then compute the hash value of every substring of the text whose length equals the length of the pattern, and compare each with the hash value of the pattern.

### String matching with up to $k$ mismatches

Problem: given a source string $s$ of length $n$ and a pattern $p$ of length $m$, count how many substrings of the source string match the pattern. $s'$ matches $s$ if and only if $s'$ and $s$ have the same length and differ in at most $k$ positions. Here $1\leq n,m\leq 10^6$, $0\leq k\leq 5$.

This problem cannot be solved with KMP, but it can be solved with hashing + binary search.

Enumerate all substrings that could match; suppose the current substring is $s'$. Using hashing + binary search we can quickly find the first position where $s'$ and $p$ differ. Then remove from $s'$ and $p$ the part up to and including this mismatch position, and continue searching for the next mismatch. This process happens at most $k$ times.

The total time complexity is $O(m+kn\log_2m)$.

### Longest palindromic substring

Binary search on the answer; to check feasibility, enumerate the palindrome centers (axes of symmetry) and use hashing to check whether the two sides are equal. The hash values of both the string and its reverse need to be precomputed. The time complexity is $O(n\log n)$.

This problem can be solved in $O(n)$ time with [Manacher's algorithm](./manacher.md).

Hashing can also solve this problem in $O(n)$: let $R_i$ denote the length of the longest palindrome ending at $i$; then the answer is $\max_{i=1}^nR_i$. Since $R_i\leq R_{i-1}+2$, we only need to start from $R_{i-1}+2$ and decrease by brute force until we find the first palindrome. Let the variable $z$ denote the currently enumerated $R_i$, initially $0$; then $z$ increases by $2$ each time $i$ increases, and decreases by $1$ in each iteration of the brute-force loop, so the brute-force loop runs at most $2n$ times and the total time complexity is $O(n)$.

### Longest common substring

Problem: given $m$ non-empty strings of total length at most $n$, find the longest common substring of all the strings; if there are several, output any of them. Here $1\leq m, n\leq 10^6$.

Obviously, if a common substring of length $k$ exists, then a common substring of length $k-1$ also exists. Therefore we can binary search on the length of the longest common substring. Suppose the current length is $k$; the logic of `check(k)` is: hash all substrings of length $k$ of each string and store the hash values in $n$ hash tables. Then take their intersection.

The time complexity is $O(m+n\log n)$.

### Counting the number of distinct substrings of a string

Problem: given a string of length $n$ consisting only of lowercase English letters, find the number of distinct substrings of the string.

To solve this problem, we iterate over all substrings of length $l=1,\cdots ,n$. For each length $l$, we multiply their hash values by the same power of $b$ and store them in an array. The number of distinct elements in the array equals the number of distinct substrings of that length, and this number is added to the final answer.

For convenience, we use $h [i]$ as the prefix hash and define $h[0]=0$.

??? note "Reference code"
    ```cpp
    int count_unique_substrings(string const& s) {
      int n = s.size();
    
      constexpr static int b = 31;
      constexpr static int m = 1e9 + 9;
      vector<long long> b_pow(n);
      b_pow[0] = 1;
      for (int i = 1; i < n; i++) b_pow[i] = (b_pow[i - 1] * b) % m;
    
      vector<long long> h(n + 1, 0);
      for (int i = 0; i < n; i++)
        h[i + 1] = (h[i] + (s[i] - 'a' + 1) * b_pow[i]) % m;
    
      int cnt = 0;
      for (int l = 1; l <= n; l++) {
        set<long long> hs;
        for (int i = 0; i <= n - l; i++) {
          long long cur_h = (h[i + l] + m - h[i]) % m;
          cur_h = (cur_h * b_pow[n - i - 1]) % m;
          hs.insert(cur_h);
        }
        cnt += hs.size();
      }
      return cnt;
    }
    ```

### Example problems

???+ note "[CF1200E Compress Words](http://codeforces.com/contest/1200/problem/E)"
    You are given several strings; the answer string is initially empty. In step $i$, the $i$-th string is appended to the end of the answer string, removing as much overlap as possible (i.e. removing the longest string that is both a suffix of the current answer string and a prefix of the $i$-th string). Find the final string.
    
    There are at most $10^5$ strings, with total length at most $10^6$.
    
    ??? note "Solution"
        In each step we need the longest string that is both a suffix of the current answer and a prefix of the $i$-th string. Enumerate the length of this string and compare with hashing.
        
        Of course, this problem can also be solved with the [KMP algorithm](./kmp.md).
    
    ??? note "Reference code"
        ```cpp
        --8<-- "docs/string/code/hash/hash_1.cpp"
        ```

**Part of this page is translated from the blog post [строковый хеш](https://github.com/e-maxx-eng/e-maxx-eng/blob/61aff51f658644424c5e1b717f14fb7bf054ae80/src/string/string-hashing.md) and its English translation [String Hashing](https://cp-algorithms.com/string/string-hashing.html). The Russian version is licensed under Public Domain + Leave a Link; the English version is licensed under CC-BY-SA 4.0.**
