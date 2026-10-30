---
title: Integer factorization
---

## Introduction

Given a positive integer $N \in \mathbf{N}_{+}$, try to quickly find one of its [non-trivial divisors](./basic.md).

Consider the naive algorithm. Divisors come in pairs, so all divisors of $N$ can be split into two parts, $[2, \sqrt N]$ and $[\sqrt N+1,N)$. It suffices to iterate over the numbers in $[2, \sqrt N]$ and then use division to find at least two divisors. The time complexity of this method is $O(\sqrt N)$.

When $N\ge10^{18}$, the running time of this algorithm is unacceptable for us, so we hope for a better algorithm. One idea is a randomized approach: guess whether a number is a divisor of $N$; with luck the answer is found in $O(1)$ time, but for data with $N\ge10^{18}$ the probability of a successful guess is $\frac{1}{10^{18}}$ and the expected number of guesses is $10^{18}$. If we guess within $[2,\sqrt N]$, the success rate is somewhat higher. We hope for a method to optimize the guessing.

## Naive algorithm

The simplest algorithm is to iterate over $[2, \sqrt N]$.

=== "C++"
    ```cpp
    vector<int> breakdown(int N) {
      vector<int> result;
      for (int i = 2; i * i <= N; i++) {
        if (N % i == 0) {  // if i divides N, then i is a prime factor of N.
          while (N % i == 0) N /= i;
          result.push_back(i);
        }
      }
      if (N != 1) {  // means that after the operations N is left as a prime
        result.push_back(N);
      }
      return result;
    }
    ```

=== "Python"
    ```python
    def breakdown(N):
        result = []
        for i in range(2, int(sqrt(N)) + 1):
            if N % i == 0:  # if i divides N, then i is a prime factor of N.
                while N % i == 0:
                    N //= i
                result.append(i)
        if N != 1:  # means that after the operations N is left as a prime
            result.append(N)
        return result
    ```

We can prove that the elements in `result` are exactly all prime factors of `N`.

??? note "Proof that the elements in `result` are exactly all prime factors of $N$"
    First, examine how `N` changes. When the loop iteration for `i` ends, since the part `while(N % i == 0) N /= i` has just been executed, `i` no longer divides `N`. Moreover, every time a factor is removed, `N` still divides $N$. These two facts guarantee that, when the loop iteration for `i` begins, `N` is a divisor of $N$ that is not divisible by any integer smaller than `i`.
    
    Next, we prove that the elements in `result` are all divisors of $N$. When the loop reaches `i`, the condition for storing `i` in `result` is `N % i == 0`, which means `i` divides `N`, and it has already been shown that `N` is a divisor of $N$, hence `i` is a divisor of $N$. When the loop over `i` ends, if `N` is not one, it is also stored in `result`. By the above, it is then necessarily a divisor of $N$ as well.
    
    Next, we prove that all elements in `result` are prime. Suppose there is a composite number $K$ in `result`; then there necessarily exists an `i` greater than one and not exceeding $\sqrt K$ such that `i` is a divisor of $K$. Such a $K$ cannot be stored in `result` as some `i` in the loop, because the first paragraph showed that when the loop reaches $K$, `N` is not divisible by any `i` smaller than $K$. Such a $K$ also cannot be added after the loop ends, because the loop exit condition is `i * i > N`, so all `i` not exceeding $\sqrt K$ have already been visited, and by the above these `i` can never divide the current `N`, i.e. $K$.
    
    Finally, we prove that all prime factors of $N$ necessarily appear in `result`. Suppose $p$ is a prime factor of $N$ that does not appear in `result`. By the discussion above, $p$ cannot be an `i` that appeared in the loop. Let `i` be the last `i` before exiting the loop; then `i` is strictly smaller than $p$, and `N` after exiting the loop is not divisible by any previous `i`, hence $p$ divides `N`. So the final `N` is greater than one, and by the above it is necessarily prime, so `N` equals $p$ and will certainly be added to `result` at the end, contradicting the assumption.

It is worth pointing out that if a table of primes has already been prepared at the start, the time complexity drops from $O(\sqrt N)$ to $O(\frac {\sqrt{N}} {\ln N})$. See [Sieves](./sieve.md) for more information on building such tables.

Example problem: [CF 1445C](https://codeforces.com/problemset/problem/1445/C)

## Pollard's rho algorithm

### Introduction

The complexity of obtaining a non-trivial divisor by brute force is $O(p)=O(\sqrt N)$, where $p$ is the smallest prime factor of $N$. Pollard's rho algorithm, introduced below, is a randomized algorithm that obtains a non-trivial divisor in expected complexity $O(\sqrt p)=O(N^{1/4})$ (**note**: a non-trivial divisor is not necessarily a prime factor).

Its core idea is that for a random self-map $f: \mathbf Z_p \rightarrow \mathbf Z_p$, starting from any point $x_1$ and iteratively computing $x_n = f(x_{n-1})$, we enter a cycle in expected time $O(\sqrt p)$. If we can find $x_i \equiv x_j \pmod p$, then $p$ divides $\gcd(|x_i-x_j|, N)$, and this greatest common divisor is a non-trivial divisor of $N$.

To understand why the expected time to enter a cycle is $O(\sqrt p)$, we can take inspiration from the birthday paradox.

### Birthday paradox

Ignoring the year of birth (assume every year has 365 days), we ask: at least how many people must be in a room so that the probability that two of them share a birthday reaches $50\%$?

Solution: suppose a year has $n$ days and there are $k$ people in the room, numbered with the integers $1, 2,\dots, k$. Assume that each person's birthday is uniformly distributed over the $n$ days and that the birthdays of any two people are independent.

Let $A$ be the event that the $k$ people all have distinct birthdays; then the probability of event $A$ is

$$
P(A)=\prod_{i=0}^{k-1}\frac{n-i}{n}
$$

The probability that at least two people share a birthday is $P(\overline A)=1-P(A)$. By the problem statement $P(\overline A)\ge\frac{1}{2}$, so we have

$$
P(A)=\prod_{i=0}^{k-1}\frac{n-i}{n} \le \frac{1}{2}
$$

From the inequality $1+x\le \mathrm{e}^x$ we get

$$
P(A) \le \prod_{i=1}^{k-1}\exp\left({-\frac{i}{n}}\right)=\exp \left({-\frac{k(k-1)}{2n}}\right)
$$

Therefore

$$
\exp\left({-\dfrac{k(k-1)}{2n}}\right) \le \frac{1}{2}\implies P(A) \le \frac{1}{2}
$$

Substituting $n=365$, we solve $k\geq 23$. So at least $23$ people in a room make the probability that two of them share a birthday reach $50\%$; since this mathematical fact is very counterintuitive, it is called a paradox.

When $k>56$ and $n=365$, the probability that two people have the same birthday exceeds $99\%$[^ref1]. Thus, when a year has $n$ days and there are $\frac{1}{2}(\sqrt{8n\ln 2+1}+1)\approx \sqrt{2n\ln 2}$ people in the room, the probability that at least two of them share a birthday is about $50\%$.

Similarly one can compute that, if a sequence of birthdays is chosen uniformly at random, the expected number of people needed until the first repeated birthday is also $O(\sqrt n)$. Let this number of people be $X$; then

$$
E(X) = \sum_{x=0}^{n}P(X\ge x+1) = \sum_{x=0}^n\frac{n!}{(n-x)!n^x} = \sqrt{\frac{\pi n}{2}}+\frac23+o(1).
$$

This suggests that if we can choose a sequence of numbers at random, the expected sample size needed for a repeated number to appear is also $O(\sqrt n)$.

### Finding a divisor using the greatest common divisor

Actually constructing a sequence of random numbers modulo $p$ is not realistic, because $p$ is exactly what we need to find. So we generate a pseudorandom sequence $\{x_i\}$ via $f(x)=(x^2+c)\bmod N$: pick a random $x_1$ and let $x_2=f(x_1),\ x_3=f(x_2),\ \dots,\ x_i=f(x_{i-1})$, where $c\in[1,N)$ is a randomly chosen constant.

The function chosen here is easy to compute and often generates fairly random sequences. But it is not completely random. For example, let $N=50,\ c=6,\ x_1=1$; the data generated by $f(x)$ are

$$
1, 7, 5, 31, 17, 45, 31, 17, 45, 31,\dots
$$

We can see that after $x_4$ the data cycle among $31,17,45$. If these numbers are arranged as in the figure below, the picture looks very much like a $\rho$, which is why the algorithm is named rho.

![pollard-rho](./images/pollard-rho.svg)

More importantly, such a function indeed provides a self-map on $\mathbf Z_p$. That is, it satisfies the property: if $x\equiv y\pmod p$, then $f(x)\equiv f(y)\pmod p$.

???+ note "Proof"
    If $x\equiv y\pmod p$, then $x^2+c\equiv y^2+c\pmod p$. Note that $f(x)=x^2+c-k_xN$, where $k_x$ is an integer depending on $x$, and $p\mid N$, so $f(x)\equiv x^2+c\pmod p$, and hence $f(x)\equiv f(y)\pmod p$.

As a sequence obtained by repeatedly iterating a pseudorandom self-map on $\mathbf Z_p$, $\{x_n\bmod p\}$ repeats within expected time $O(\sqrt p)$. As soon as we observe such a repetition $x_i\equiv x_j\pmod p$, we can obtain a non-trivial divisor of $N$ from $\gcd(|x_i-x_j|,N)$. Note that since $p$ is unknown, we have no way to detect the repetition directly; a simple criterion is precisely that $\gcd(|x_i-x_j|,N)$ is strictly greater than one.

This algorithm does not always succeed, because $\gcd(|x_i-x_j|,N)$ may equal $N$. That is, $x_i\equiv x_j\pmod N$. In this case, when $\{x_n\bmod p\}$ repeats for the first time, $\{x_n\}$ happens to repeat as well. We have not obtained a non-trivial divisor. Moreover, once $\{x_n\}$ starts cycling, further iteration is pointless, because afterwards only this cycle repeats. The algorithm should report that the factorization failed, and the factorization must be redone with a different choice of $c$ in $f(x)$.

By the analysis above, in theory any function $f(x)$ that satisfies $\forall x \equiv y \pmod p, f(x) \equiv f(y) \pmod p$ and guarantees a certain pseudorandomness (for example, certain polynomial functions) can be used here. In practice, mainly $f(x)=x^2+c\ (c\neq 0,-2)$ is used.[^pseudo]

### Implementation

The algorithm we need to implement must quickly determine during the iteration whether $\{x_n\bmod p\}$ has already repeated. Viewing $f$ as the edges of a directed graph with vertex set $\mathbf Z_p$, what we actually need to implement is a cycle detection algorithm, except that the equality check is replaced by checking whether $\gcd(|x_i-x_j|,N)$ is greater than one.

#### Floyd's cycle detection

Suppose two people are racing: A is fast and B is slow. After some time, A will certainly meet B, and at the meeting the total distance run by A minus the total distance run by B is certainly a multiple of the lap length.

Let $a=f(0),b=f(f(0))$; in each step update $a=f(a),b=f(f(b))$, and just check whether $a$ and $b$ become equal during the updates; if they do, a cycle has appeared.

In each step we let $d=\gcd(|x_i-x_j|,N)$ and check whether $d$ satisfies $1< d< N$; if so, we can directly return $d$. If $d=N$, then $\{x_i\}$ has already formed a cycle, and once a cycle is formed we cannot continue, so we directly return $N$ itself, and in subsequent operations adjust the random constant $c$ and factor again.

??? note "Pollard's rho algorithm based on Floyd's cycle detection"
    === "C++"
        ```cpp
        ll Pollard_Rho(ll N) {
          if (N == 4) return 2;  // since we jump two steps at the start, 4 needs a special case
          ll c = rand() % (N - 1) + 1;
          ll t = f(0, c, N);
          ll r = f(f(0, c, N), c, N);
          while (t != r) {
            ll d = gcd(abs(t - r), N);
            if (d > 1) return d;
            t = f(t, c, N);
            r = f(f(r, c, N), c, N);
          }
          return N;
        }
        ```
    
    === "Python"
        ```python
        import random
        
        
        def Pollard_Rho(N):
            if N == 4:
                return 2  # since we jump two steps at the start, 4 needs a special case
            c = random.randint(1, N - 1)
            t = f(0, c, N)
            r = f(f(0, c, N), c, N)
            while t != r:
                d = gcd(abs(t - r), N)
                if d > 1:
                    return d
                t = f(t, c, N)
                r = f(f(r, c, N), c, N)
            return N
        ```

#### Brent's cycle detection

In fact, Floyd's cycle detection algorithm can be improved by a constant factor. Brent's cycle detection starts from $k=1$ and increments $k$; in round $k$, A waits in place while B moves forward $2^k$ steps. If B meets A during this process, a cycle has been found; otherwise A teleports to B's position and the next round begins.

It can be proved[^brent] that the number of calls to $f$ needed before a cycle is found this way is never greater than in Floyd's cycle detection algorithm. The tests in the original paper show that the average time needed by Brent's cycle detection is $24\%$ less than that of Floyd's cycle detection.

#### Doubling optimization

Whether Floyd's or Brent's cycle detection is used, the number of iterations is $O(\sqrt p)$. But using $\gcd$ in every iteration to check for a cycle slows down the algorithm. The number of $\gcd$ computations can be reduced by accumulating a product.

Simply put, if $\gcd(a,N)>1$, then $\gcd(ab\bmod N,N)=\gcd(ab,N)>1$ holds for any $b\in\mathbf N_+$. That is, if we compute $\gcd(\prod |x_i-x_j| \bmod N,N)>1$, then necessarily some pair $(x_i,x_j)$ satisfies $\gcd(|x_i-x_j|,N)>1$. If the product becomes zero at some point, the factorization fails; exit and return $N$ itself.

If a $\gcd$ is computed every $k$ pairs, the complexity of the algorithm drops to $O(\sqrt p+k^{-1}\sqrt p\log N)$, where $\log N$ is the cost of a single $\gcd$ computation. Note that when $k$ and $\log N$ are roughly of the same order, we get an expected complexity of $O(\sqrt p)$. In concrete implementations, $k=127$ is mostly chosen.

Here we provide an implementation of Pollard's rho algorithm with Brent's cycle detection plus the doubling optimization.

??? note "Implementation"
    === "C++"
        ```cpp
        ll Pollard_Rho(ll x) {
          ll t = 0;
          ll c = rand() % (x - 1) + 1;
          ll s = t;
          int step = 0, goal = 1;
          ll val = 1;
          for (goal = 1;; goal <<= 1, s = t, val = 1) {
            for (step = 1; step <= goal; ++step) {
              t = f(t, c, x);
              val = val * abs(t - s) % x;
              // if val is 0, exit and factor again
              if (!val) return x;
              if (step % 127 == 0) {
                ll d = gcd(val, x);
                if (d > 1) return d;
              }
            }
            ll d = gcd(val, x);
            if (d > 1) return d;
          }
        }
        ```
    
    === "Python"
        ```python
        from random import randint
        from math import gcd
        
        
        def Pollard_Rho(x):
            c = randint(1, x - 1)
            s = t = f(0, c, x)
            goal = val = 1
            while True:
                for step in range(1, goal + 1):
                    t = f(t, c, x)
                    val = val * abs(t - s) % x
                    if val == 0:
                        return x  # if val is 0, exit and factor again
                    if step % 127 == 0:
                        d = gcd(val, x)
                        if d > 1:
                            return d
                d = gcd(val, x)
                if d > 1:
                    return d
                s = t
                goal <<= 1
                val = 1
        ```

#### Complexity

The expected number of iterations in Pollard's rho algorithm is $O(\sqrt p)$, where $p$ is the smallest prime factor of $N$. Whether the concrete implementation uses Floyd's or Brent's cycle detection, without the doubling optimization the expected complexity is $O(\sqrt p\log N)$; with the doubling optimization, an expected complexity of approximately $O(\sqrt p)$ is obtained.

It is worth mentioning that the analysis above is based on a completely random self-map, whereas Pollard's rho algorithm actually uses a pseudorandom function, so the algorithm has no rigorous complexity analysis, but in practice it usually runs quite fast.

#### Example problem: the largest prime factor of a number

Example problem: [P4718【模板】Pollard-Rho 算法 (Template: Pollard's rho algorithm)](https://www.luogu.com.cn/problem/P4718)

For a number $n$, use the [Miller–Rabin algorithm](./prime.md#millerrabin-素性测试) to test whether it is prime; if so, it can be returned directly, otherwise use Pollard's rho algorithm to find a divisor $p$ and remove the factor $p$ from $n$. Then recursively factor $n$ and $p$, use Miller–Rabin to check whether a prime factor has appeared, and update max\_factor to obtain the largest prime factor. Since the data of this problem are very large, Floyd's cycle detection is not enough, so the doubling optimization is used here.

??? note "Implementation"
    ```cpp
    --8<-- "docs/math/code/pollard-rho/pollard-rho_1.cpp"
    ```

## References and links

[^ref1]: <https://en.wikipedia.org/wiki/Birthday_problem#Reverse_problem>

[^pseudo]: Menezes, Alfred J.; van Oorschot, Paul C.; Vanstone, Scott A. (2001). Handbook of Applied Cryptography. Section 3.11 and 3.12.

[^brent]: Brent, R. P. (1980), An improved Monte Carlo factorization algorithm, BIT Numerical Mathematics, 20(2): 176–184, doi:10.1007/BF01933190
