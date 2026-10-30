---
title: Sieves
---

## Prime sieves

### Introduction

What if we want to know how many primes there are that are less than or equal to $n$?

A natural idea is to run a primality test on every number less than or equal to $n$. This brute-force approach obviously does not achieve the optimal complexity.

### Sieve of Eratosthenes

#### Process

Consider the following: for any positive integer $n$ greater than $1$, its $x$-fold multiple is a composite number ($x > 1$). Using this conclusion, we can avoid many unnecessary checks.

If we consider the numbers from small to large and at the same time mark all (larger) multiples of the current number as composite, then the numbers that are not marked when the procedure finishes are exactly the primes.

#### Implementation

=== "C++"
    ```cpp
    vector<int> prime;
    bool is_prime[N];
    
    void Eratosthenes(int n) {
      is_prime[0] = is_prime[1] = false;
      for (int i = 2; i <= n; ++i) is_prime[i] = true;
      for (int i = 2; i <= n; ++i) {
        if (is_prime[i]) {
          prime.push_back(i);
          if ((long long)i * i > n) continue;
          for (int j = i * i; j <= n; j += i)
            // the multiples of 2 to i - 1 have already been sieved, so we start
            // directly from the multiples of i, which speeds things up
            is_prime[j] = false;  // no multiple of i is prime
        }
      }
    }
    ```

=== "Python"
    ```python
    prime = []
    is_prime = [False] * N
    
    
    def Eratosthenes(n):
        is_prime[0] = is_prime[1] = False
        for i in range(2, n + 1):
            is_prime[i] = True
        for i in range(2, n + 1):
            if is_prime[i]:
                prime.append(i)
                if i * i > n:
                    continue
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
    ```

The above is the **sieve of Eratosthenes**, with time complexity $O(n\log\log n)$.

???+ note "Proof"
    Let us now look at the derivation:
    
    If every operation on the array costs 1 unit of time, the time complexity is:
    
    $$
    O\left(\sum_{k=1}^{\pi(n)}{\frac{n}{p_k}}\right)=O\left(n\sum_{k=1}^{\pi(n)}{\frac{1}{p_k}}\right)
    $$
    
    where $p_k$ denotes the $k$-th smallest prime and $\pi(n)$ denotes the number of primes $\le n$. $\sum_{k=1}^{\pi(n)}$ represents the outer for loop, where the upper bound of the sum $\pi(n)$ is the number of times `if (prime[i])` enters the true branch; $\frac{n}{p_k}$ represents the number of executions of the inner for loop.
    
    By Mertens' second theorem, there is a constant $B_1$ such that:
    
    $$
    \sum_{k=1}^{\pi(n)}{\frac{1}{p_k}}=\log\log n+B_1+O\left(\frac{1}{\log n}\right)
    $$
    
    Therefore the time complexity of the **sieve of Eratosthenes** is $O(n\log\log n)$. Next we prove a weakened version of Mertens' second theorem, $\sum_{k\le\pi(n)}1/p_k=O(\log\log n)$:
    
    From $\pi(n)=\Theta(n/\log n)$ we know that the $n$-th prime has size $\Theta(n\log n)$. Hence
    
    $$
    \begin{aligned}
    \sum_{k=1}^{\pi(n)}{\frac{1}{p_k}}
    &=O\left(\sum_{k=2}^{\pi(n)}{\frac{1}{k\log k}}\right) \\
    &=O\left(\int_2^{\pi(n)}{\frac{\mathrm dx}{x\log x}}\right) \\
    &=O(\log\log\pi(n))=O(\log\log n)
    \end{aligned}
    $$
    
    Of course, the approach above is still not efficient enough; applying the following methods can slightly improve the efficiency of the algorithm.

#### Sieving up to the square root

Obviously, to find all primes up to $n$, it is enough to sieve only with the primes not exceeding $\sqrt n$.

=== "C++"
    ```cpp
    vector<int> prime;
    bool is_prime[N];
    
    void Eratosthenes(int n) {
      is_prime[0] = is_prime[1] = false;
      for (int i = 2; i <= n; ++i) is_prime[i] = true;
      // i * i <= n means i <= sqrt(n)
      for (int i = 2; i * i <= n; ++i) {
        if (is_prime[i])
          for (int j = i * i; j <= n; j += i) is_prime[j] = false;
      }
      for (int i = 2; i <= n; ++i)
        if (is_prime[i]) prime.push_back(i);
    }
    ```

=== "Python"
    ```python
    prime = []
    is_prime = [False] * N
    
    
    def Eratosthenes(n):
        is_prime[0] = is_prime[1] = False
        for i in range(2, n + 1):
            is_prime[i] = True
        # let i loop up to <= sqrt(n)
        for i in range(2, isqrt(n) + 1):  # `isqrt` is a function added in Python 3.8
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        for i in range(2, n + 1):
            if is_prime[i]:
                prime.append(i)
    ```

This optimization does not affect the asymptotic time complexity; in fact, repeating the proof above we get $n \ln \ln \sqrt n + o(n)$, which by the properties of logarithms is asymptotically the same, but the number of operations decreases noticeably.

#### Sieving only odd numbers

Since all even numbers except 2 are composite, we can simply skip them and only care about odd numbers.

First, this halves our memory requirements; second, the number of required operations is also roughly halved.

#### Reducing memory usage

We notice that sieving only needs an array of type `bool`. One element of a `bool` array usually takes $1$ byte (i.e. $8$ bits), but storing a Boolean value only needs $1$ bit.

Using knowledge of [bit operations](../bit.md), we can pack each Boolean value into a single bit, so that we only use $n$ bits (i.e. $\dfrac n 8$ bytes) instead of $n$ bytes, which significantly reduces memory usage. This technique is called "bit packing".

It is worth mentioning that there are data structures that perform bit packing automatically, such as `vector<bool>` and `bitset<>` in C++.

Moreover, `vector<bool>` and `bitset<>` give the program a constant-factor optimization: the sieve of Eratosthenes with time complexity $O(n \log \log n)$, after being optimized with `bitset<>` or `vector<bool>`, even outperforms the Euler sieve with time complexity $O(n)$.

See [bitset: combination with the sieve of Eratosthenes](../../lang/csl/bitset.md#与埃氏筛结合).

#### Segmented sieve

From the "sieving up to the square root" optimization we know that it is not necessary to keep the whole array `is_prime[1...n]` all the time. For sieving, it is enough to keep only the primes up to $\sqrt n$, i.e. `prime[1...sqrt(n)]`, and to split the whole range into blocks, sieving each block separately. This way we do not have to keep several blocks in memory at the same time, and the CPU handles the cache better.

Let $s$ be a constant that determines the block size; then we have $\lceil {\frac n s} \rceil$ blocks, and block $k$ ($k = 0 \dots \lfloor {\frac n s} \rfloor$) contains the numbers in the interval $[ks, ks + s - 1]$. We can process the blocks one by one, that is, for each block $k$ we iterate over all primes (from $1$ to $\sqrt n$) and sieve with them.

It is worth noting that we need to slightly modify the strategy when processing the first block: first, all primes in $[1, \sqrt n]$ should be kept; second, the numbers $0$ and $1$ should be marked as non-prime. When processing the last block, one should not forget that the last number $n$ is not necessarily at the end of the block.

The following implementation uses the segmented sieve to count the number of primes less than or equal to $n$.

???+ note "Implementation"
    ```cpp
    int count_primes(int n) {
      constexpr static int S = 10000;
      vector<int> primes;
      int nsqrt = sqrt(n);
      vector<char> is_prime(nsqrt + 1, true);
      for (int i = 2; i <= nsqrt; i++) {
        if (is_prime[i]) {
          primes.push_back(i);
          for (int j = i * i; j <= nsqrt; j += i) is_prime[j] = false;
        }
      }
      int result = 0;
      vector<char> block(S);
      for (int k = 0; k * S <= n; k++) {
        fill(block.begin(), block.end(), true);
        int start = k * S;
        for (int p : primes) {
          int start_idx = (start + p - 1) / p;
          int j = max(start_idx, p) * p - start;
          for (; j < S; j += p) block[j] = false;
        }
        if (k == 0) block[0] = block[1] = false;
        for (int i = 0; i < S && start + i <= n; i++) {
          if (block[i]) result++;
        }
      }
      return result;
    }
    ```

The asymptotic time complexity of the segmented sieve is the same as that of the sieve of Eratosthenes (unless the blocks are very small), but the required memory shrinks to $O(\sqrt{n} + S)$ and the cache behavior is better.
On the other hand, a division has to be performed for every pair of a block and a prime in the interval $[1, \sqrt{n}]$, and for smaller blocks this is considerably worse.
Therefore one has to keep a balance when choosing the constant $S$.

The best speed is obtained with a block size $S$ between $10^4$ and $10^5$.

### Linear sieve

The sieve of Eratosthenes still has room for optimization: it marks a composite number several times. Is there a way to save these meaningless steps? The answer is yes.

If we can make every composite number be marked exactly once, the time complexity can be lowered to $O(n)$.

???+ note "Implementation"
    === "C++"
        ```cpp
        vector<int> pri;
        bool not_prime[N];
        
        void pre(int n) {
          for (int i = 2; i <= n; ++i) {
            if (!not_prime[i]) {
              pri.push_back(i);
            }
            for (int pri_j : pri) {
              if (i * pri_j > n) break;
              not_prime[i * pri_j] = true;
              if (i % pri_j == 0) {
                // i % pri_j == 0
                // in other words, i has already been sieved by pri_j
                // since the primes in pri are in increasing order, the product of i
                // with any other prime will surely be sieved as a multiple of pri_j,
                // so there is no need to sieve it here first; we can simply break
                // here
                break;
              }
            }
          }
        }
        ```
    
    === "Python"
        ```python
        pri = []
        not_prime = [False] * N
        
        
        def pre(n):
            for i in range(2, n + 1):
                if not not_prime[i]:
                    pri.append(i)
                for pri_j in pri:
                    if i * pri_j > n:
                        break
                    not_prime[i * pri_j] = True
                    if i % pri_j == 0:
                        """
                        i % pri_j == 0
                        in other words, i has already been sieved by pri_j
                        since the primes in pri are in increasing order, the product of i
                        with any other prime will surely be sieved as a multiple of pri_j,
                        so there is no need to sieve it here first; we can simply break
                        here
                        """
                        break
        ```

The **linear sieve** above is also called the **Euler sieve**.

???+ note "Note"
    Note that while finding primes with the sieve we also obtain the smallest prime factor of every number.

## Sieve for Euler's totient function

Note that in the linear sieve every composite number is sieved by its smallest prime factor. For example, let $p_1$ be the smallest prime factor of $n$ and $n' = \frac{n}{p_1}$; then during the linear sieve $n$ is sieved as $n' \times p_1$.

Looking at the process of the linear sieve, we still need to handle two parts; below we distinguish cases according to $n' \bmod p_1$.

If $n' \bmod p_1 = 0$, then $n'$ contains all prime factors of $n$.

$$
\begin{aligned}
\varphi(n) & = n \times \prod_{i = 1}^s{\frac{p_i - 1}{p_i}} \\\\
& = p_1 \times n' \times \prod_{i = 1}^s{\frac{p_i - 1}{p_i}} \\\\
& = p_1 \times \varphi(n')
\end{aligned}
$$

What if $n' \bmod p_1 \neq 0$? Then $n'$ and $p_1$ are coprime, and by the properties of Euler's totient function we have:

$$
\begin{aligned}
\varphi(n) & = \varphi(p_1) \times \varphi(n') \\\\
& = (p_1 - 1) \times \varphi(n')
\end{aligned}
$$

### Implementation

=== "C++"
    ```cpp
    vector<int> pri;
    bool not_prime[N];
    int phi[N];
    
    void pre(int n) {
      phi[1] = 1;
      for (int i = 2; i <= n; i++) {
        if (!not_prime[i]) {
          pri.push_back(i);
          phi[i] = i - 1;
        }
        for (int pri_j : pri) {
          if (i * pri_j > n) break;
          not_prime[i * pri_j] = true;
          if (i % pri_j == 0) {
            phi[i * pri_j] = phi[i] * pri_j;
            break;
          }
          phi[i * pri_j] = phi[i] * phi[pri_j];
        }
      }
    }
    ```

=== "Python"
    ```python
    pri = []
    not_prime = [False] * N
    phi = [0] * N
    
    
    def pre(n):
        phi[1] = 1
        for i in range(2, n + 1):
            if not not_prime[i]:
                pri.append(i)
                phi[i] = i - 1
            for pri_j in pri:
                if i * pri_j > n:
                    break
                not_prime[i * pri_j] = True
                if i % pri_j == 0:
                    phi[i * pri_j] = phi[i] * pri_j
                    break
                phi[i * pri_j] = phi[i] * phi[pri_j]
    ```

## Sieve for the Möbius function

### Definition

By the definition of the Möbius function, let $n$ be a composite number, $p_1$ the smallest prime factor of $n$, and $n'=\frac{n}{p_1}$; then:

$$
\mu(n)=
\begin{cases}
    0 & n' \bmod p_1 = 0\\\\
    -\mu(n') & \text{otherwise}
\end{cases}
$$

If $n$ is prime, then $\mu(n)=-1$.

### Implementation

=== "C++"
    ```cpp
    vector<int> pri;
    bool not_prime[N];
    int mu[N];
    
    void pre(int n) {
      mu[1] = 1;
      for (int i = 2; i <= n; ++i) {
        if (!not_prime[i]) {
          mu[i] = -1;
          pri.push_back(i);
        }
        for (int pri_j : pri) {
          if (i * pri_j > n) break;
          not_prime[i * pri_j] = true;
          if (i % pri_j == 0) {
            mu[i * pri_j] = 0;
            break;
          }
          mu[i * pri_j] = -mu[i];
        }
      }
    }
    ```

=== "Python"
    ```python
    pri = []
    not_prime = [False] * N
    mu = [0] * N
    
    
    def pre(n):
        mu[1] = 1
        for i in range(2, n + 1):
            if not not_prime[i]:
                pri.append(i)
                mu[i] = -1
            for pri_j in pri:
                if i * pri_j > n:
                    break
                not_prime[i * pri_j] = True
                if i % pri_j == 0:
                    mu[i * pri_j] = 0
                    break
                mu[i * pri_j] = -mu[i]
    ```

## Sieve for the number of divisors

Let $d_i$ denote the number of divisors of $i$, and $num_i$ the number of occurrences of the smallest prime factor of $i$.

### Divisor count theorem

Theorem: if $n=\prod_{i=1}^m p_i^{c_i}$, then $d_i=\prod_{i=1}^m (c_i+1)$.

Proof: we know that the divisors of $p_i^{c_i}$ are $p_i^0,p_i^1,\dots ,p_i^{c_i}$, that is, $c_i+1$ of them; by the multiplication principle, the number of divisors of $n$ is $\prod_{i=1}^m (c_i+1)$.

### Implementation

Since $d_i$ is a multiplicative function, the linear sieve can be used.

Here we briefly describe the principle of the linear-sieve implementation.

1.  When $i$ is prime, $\textit{num}_i \gets 1,\textit{d}_i \gets 2$; at the same time let $q = \left\lfloor \dfrac {i}{p} \right\rfloor$, where $p$ is the smallest prime factor of $i$.
2.  When $p$ is a prime factor of $q$, $\textit{num}_i \gets \textit{num}_q + 1,\textit{d}_i \gets \dfrac{\textit{d}_q}{\textit{num}_i} \times (\textit{num}_i + 1)$.
3.  When $p,q$ are coprime, $\textit{num}_i \gets 1,\textit{d}_i \gets \textit{d}_q \times (\textit{num}_i+1)$.

=== "C++"
    ```cpp
    vector<int> pri;
    bool not_prime[N];
    int d[N], num[N];
    
    void pre(int n) {
      d[1] = 1;
      for (int i = 2; i <= n; ++i) {
        if (!not_prime[i]) {
          pri.push_back(i);
          d[i] = 2;
          num[i] = 1;
        }
        for (int pri_j : pri) {
          if (i * pri_j > n) break;
          not_prime[i * pri_j] = true;
          if (i % pri_j == 0) {
            num[i * pri_j] = num[i] + 1;
            d[i * pri_j] = d[i] / num[i * pri_j] * (num[i * pri_j] + 1);
            break;
          }
          num[i * pri_j] = 1;
          d[i * pri_j] = d[i] * 2;
        }
      }
    }
    ```

=== "Python"
    ```python
    pri = []
    not_prime = [False] * N
    d = [0] * N
    num = [0] * N
    
    
    def pre(n):
        d[1] = 1
        for i in range(2, n + 1):
            if not not_prime[i]:
                pri.append(i)
                d[i] = 2
                num[i] = 1
            for pri_j in pri:
                if i * pri_j > n:
                    break
                not_prime[i * pri_j] = True
                if i % pri_j == 0:
                    num[i * pri_j] = num[i] + 1
                    d[i * pri_j] = d[i] // num[i * pri_j] * (num[i * pri_j] + 1)
                    break
                num[i * pri_j] = 1
                d[i * pri_j] = d[i] * 2
    ```

## Sieve for the sum of divisors

$f_i$ denotes the sum of divisors of $i$, and $g_i$ denotes $p^0+p^1+p^2+\dots p^k$ for the smallest prime factor $p$ of $i$.

### Implementation

=== "C++"
    ```cpp
    vector<int> pri;
    bool not_prime[N];
    int g[N], f[N];
    
    void pre(int n) {
      g[1] = f[1] = 1;
      for (int i = 2; i <= n; ++i) {
        if (!not_prime[i]) {
          pri.push_back(i);
          g[i] = i + 1;
          f[i] = i + 1;
        }
        for (int pri_j : pri) {
          if (i * pri_j > n) break;
          not_prime[i * pri_j] = true;
          if (i % pri_j == 0) {
            g[i * pri_j] = g[i] * pri_j + 1;
            f[i * pri_j] = f[i] / g[i] * g[i * pri_j];
            break;
          }
          f[i * pri_j] = f[i] * f[pri_j];
          g[i * pri_j] = 1 + pri_j;
        }
      }
    }
    ```

=== "Python"
    ```python
    pri = []
    not_prime = [False] * N
    f = [0] * N
    g = [0] * N
    
    
    def pre(n):
        g[1] = f[1] = 1
        for i in range(2, n + 1):
            if not not_prime[i]:
                pri.append(i)
                g[i] = i + 1
                f[i] = i + 1
            for pri_j in pri:
                if i * pri_j > n:
                    break
                not_prime[i * pri_j] = True
                if i % pri_j == 0:
                    g[i * pri_j] = g[i] * pri_j + 1
                    f[i * pri_j] = f[i] // g[i] * g[i * pri_j]
                    break
                f[i * pri_j] = f[i] * f[pri_j]
                g[i * pri_j] = 1 + pri_j
    ```

## General multiplicative functions

If a [multiplicative function](./basic.md#积性函数)  $f$ satisfies: for any prime $p$ and positive integer $k$, $f(p^k)$ can be computed in time polynomial of low degree in $k$, then the values $f(1),f(2),\dots,f(n)$ can be sieved in $O(n)$ time.

Let the prime factorization of the composite number $n$ be $\prod_{i=1}^k p_i^{\alpha_i}$, where $p_1<p_2<\dots<p_k$ are primes; in the linear sieve we record $g_n=p_1^{\alpha_1}$. If $n$ is sieved as $x\cdot p$ ($p$ is prime), then $g$ satisfies the following recurrence:

$$
g_n=
\begin{cases}
    g_x\cdot p & x\bmod p=0\\\\
    p & \text{otherwise}
\end{cases}
$$

If $n=g_n$, then $n$ is a power of some prime and $f(n)$ can be computed in $O(1)$; otherwise $f(n)=f(\frac{n}{g_n})\cdot f(g_n)$.

**Part of this section is translated from the blog post [Решето Эратосфена](http://e-maxx.ru/algo/eratosthenes_sieve) and its English translation [Sieve of Eratosthenes](https://cp-algorithms.com/algebra/sieve-of-eratosthenes.html). The Russian version is licensed under Public Domain + Leave a Link; the English version is licensed under CC-BY-SA 4.0.**
