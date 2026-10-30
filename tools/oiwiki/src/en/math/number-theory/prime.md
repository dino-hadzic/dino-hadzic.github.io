---
title: Prime numbers
---

For the definitions of prime and composite numbers, see [Number theory basics](./basic.md).

Prime-counting function: the number of primes less than or equal to $x$ is denoted by $\pi(x)$. As $x$ grows, the following approximation holds: $\pi(x) \sim \dfrac{x}{\ln(x)}$.

## Primality testing

A **primality test** can be used to determine whether a given natural number is prime.

There are two kinds of primality tests:

1.  Deterministic tests: they determine with certainty whether a number is prime. Common examples include trial division, the Lucas–Lehmer test, and elliptic curve primality proving.
2.  Probabilistic tests: they are usually much faster than deterministic tests, but they may (although with a very small probability) misidentify a [composite number](./basic.md#primes-and-composite-numbers) as prime (the converse never happens). Therefore, numbers that pass a probabilistic primality test are called **probable primes** until their primality can be proven deterministically. Numbers that pass the test but are actually composite are called **pseudoprimes**. There are many specific types of pseudoprimes; the most common are Fermat pseudoprimes, which are composite numbers satisfying Fermat's little theorem. A common example of a probabilistic test is the Miller–Rabin test.

### Trial division

The brute-force approach is, of course, to enumerate every number from small to large and check whether it divides the given number.

???+ example "Reference implementation"
    === "C++"
        ```cpp
        bool isPrime(int a) {
          if (a < 2) return false;
          for (int i = 2; i < a; ++i)
            if (a % i == 0) return false;
          return true;
        }
        ```
    
    === "Python"
        ```python
        def isPrime(a):
            if a < 2:
                return False
            for i in range(2, a):
                if a % i == 0:
                    return False
            return True
        ```

This is perfectly safe, but is it really necessary to check every number?

It is easy to notice the following fact: if $x$ is a divisor of $a$, then $\frac{a}{x}$ is also a divisor of $a$.

This tells us that for each pair $(x, \frac{a}{x} )$, it suffices to check only one of them. For convenience, we only look at the smaller number of each pair. It is not hard to see that all these smaller numbers lie in the interval $[1, \sqrt{a}]$.

Since $1$ is certainly a divisor, we do not check it.

???+ example "Reference implementation"
    === "C++"
        ```cpp
        bool isPrime(int a) {
          if (a < 2) return 0;
          for (int i = 2; (long long)i * i <= a; ++i)  // prevents overflow
            if (a % i == 0) return 0;
          return 1;
        }
        ```
    
    === "Python"
        ```python
        def isPrime(a):
            if a < 2:
                return False
            for i in range(2, int(sqrt(a)) + 1):
                if a % i == 0:
                    return False
            return True
        ```

### Fermat primality test

The **Fermat primality test** is the simplest probabilistic primality test.

From [Fermat's little theorem](./fermat.md#fermats-little-theorem) we can derive an idea for testing primality:

The basic idea is to repeatedly pick bases $a$ in $[2, n-1]$ and check whether $a^{n-1} \equiv 1 \pmod n$ holds every time.

???+ example "Reference implementation"
    === "C++"
        ```cpp
        bool fermat(int n) {
          if (n < 3) return n == 2;
          // test_time is the number of tests; an integer not less than 8 is recommended
          // to ensure accuracy, but it should not be too large either, or efficiency suffers
          for (int i = 1; i <= test_time; ++i) {
            int a = rand() % (n - 2) + 2;
            if (quickPow(a, n - 1, n) != 1) return false;
          }
          return true;
        }
        ```
    
    === "Python"
        ```python
        def fermat(n):
            if n < 3:
                return n == 2
            # test_time is the number of tests; an integer not less than 8 is recommended
            # to ensure accuracy, but it should not be too large either, or efficiency suffers
            for i in range(1, test_time + 1):
                a = random.randint(0, 32767) % (n - 2) + 2
                if quickPow(a, n - 1, n) != 1:
                    return False
            return True
        ```

If $a^{n-1} \equiv 1 \pmod n$ but $n$ is not prime, then $n$ is called a **Fermat pseudoprime** to base $a$. In practice we observe that if $a^{n-1} \equiv 1 \pmod n$, then $n$ is usually prime. However, counterexamples do exist: for $n = 341$ and $a = 2$, although $2^{340}\equiv 1 {\pmod {341}}$, $341 = 11 \cdot 31$ is composite. In fact, for any fixed base $a$, there are infinitely many such counterexamples[^inf-fermat-pp].

Since the Fermat primality test cannot guarantee correctness for a single base, a natural idea is to check several bases. However, even if we check all possible bases $a$ coprime to $n$, we still cannot guarantee that $n$ is prime. In other words, the converse of Fermat's little theorem does not hold: even if $a^{n-1}\equiv 1\pmod n$ for all $a\perp n$, $n$ is not necessarily prime. Such numbers are called [Carmichael numbers](./primitive-root.md#carmichael-numbers). There are infinitely many of them, too. This forces us to look for a stricter primality test.

### Miller–Rabin primality test

The **Miller–Rabin primality test** is a better method for determining primality. It was obtained by Miller and Rabin by improving the Fermat primality test. Like other probabilistic primality tests, it can only detect probable primes. To be sure that a number is prime, a much slower deterministic algorithm is needed. However, no composite number has been found so far that passes the Miller–Rabin test or other advanced probabilistic tests, so we can use it with confidence.

Ignoring the complexity of multiplication, the time complexity of $k$ rounds of the test on the number $n$ is $O(k \log n)$. The Miller–Rabin primality test is often used to test arbitrary-precision numbers; in that case the time complexity is $O(k \log^3n)$, and with techniques such as FFT it can be optimized to [$O(k \log^2n \log \log n \log \log \log n)$](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Complexity).

To deal with the challenge posed by Carmichael numbers, the Miller–Rabin primality test additionally uses the following property of primes:

???+ note "Quadratic probing theorem"
    If $p$ is an odd prime, then the solutions of $x^2 \equiv 1 \pmod p$ are $x \equiv 1 \pmod p$ or $x \equiv p - 1 \pmod p$.

??? note "Proof"
    It is easy to verify that when $p$ is an odd prime, both $x\equiv 1\pmod p$ and $x\equiv p-1\pmod p$ satisfy the equation above. By [Lagrange's theorem](./congruence-equation.md#congruences-modulo-a-prime), these are all the solutions of the equation.

Combining Fermat's little theorem and the quadratic probing theorem, we obtain the Miller–Rabin primality test:

1.  Decompose the exponent $n-1$ in $a^{n-1} \equiv 1 \pmod n$ as $n-1=u \times 2^t$, where $u$ is odd;
2.  In each round of the test, for the randomly chosen $a$, first compute $v = a^{u} \bmod n$, then square this value at most $t$ times;
3.  If during the whole process a nontrivial square root of $1$ (i.e., a root other than $\pm 1$) is found, the number can be declared composite;
4.  Otherwise, apply the Fermat primality test as well.

There are also a few small implementation details:

-   In a round of the test, if at some moment $a^{u \times 2^s} \equiv n-1 \pmod n$, then all subsequent squarings yield $1$, so this round of the test can be passed directly.
-   If a nontrivial square root is found, i.e., $a^{u \times 2^s} \not\equiv n-1 \text{ or } 1 \pmod n$ but $a^{u \times 2^{s+1}} \equiv 1 \pmod n$, then all subsequent squarings yield $1$. One can either return `false` immediately or wait until after the $t$ squarings to return `false`.

This gives a more correct Miller–Rabin (from fjzzq2002):

???+ example "Reference implementation"
    === "C++"
        ```cpp
        bool millerRabin(int n) {
          if (n < 3 || n % 2 == 0) return n == 2;
          if (n % 3 == 0) return n == 3;
          int u = n - 1, t = 0;
          while (u % 2 == 0) u /= 2, ++t;
          // test_time is the number of tests; an integer not less than 8 is recommended
          // to ensure accuracy, but it should not be too large either, or efficiency suffers
          for (int i = 0; i < test_time; ++i) {
            // 0, 1, n-1 pass the test directly; a is taken from the range [2, n-2]
            int a = rand() % (n - 3) + 2, v = quickPow(a, u, n);
            if (v == 1) continue;
            int s;
            for (s = 0; s < t; ++s) {
              if (v == n - 1) break;  // got the trivial square root n-1, this round of the test passes
              v = (long long)v * v % n;
            }
            // if a nontrivial square root was found, the loop cannot break early and runs until s == t
            // if the Fermat primality test fails, v never equals -1 before reaching s == t
            if (s == t) return 0;
          }
          return 1;
        }
        ```
    
    === "Python"
        ```python
        def millerRabin(n):
            if n < 3 or n % 2 == 0:
                return n == 2
            if n % 3 == 0:
                return n == 3
            u, t = n - 1, 0
            while u % 2 == 0:
                u = u // 2
                t = t + 1
            # test_time is the number of tests; an integer not less than 8 is recommended
            # to ensure accuracy, but it should not be too large either, or efficiency suffers
            for i in range(test_time):
                # 0, 1, n-1 pass the test directly; a is taken from the range [2, n-2]
                a = random.randint(2, n - 2)
                v = pow(a, u, n)
                if v == 1:
                    continue
                s = 0
                while s < t:
                    if v == n - 1:
                        break
                    v = v * v % n
                    s = s + 1
                # if a nontrivial square root was found, the loop cannot break early and runs until s == t
                # if the Fermat primality test fails, v never equals -1 before reaching s == t
                if s == t:
                    return False
            return True
        ```

It can be proven[^millerrabinproof] that the probability that an odd composite number $n > 9$ passes the Miller–Rabin primality test for a single randomly chosen base $a$ is at most one quarter. Therefore, after randomly choosing $k$ bases, the probability of still misidentifying a composite number as prime does not exceed $1/4^k$.

??? note "Proof"
    Let $n-1=u2^t$, where $u$ is odd and $t$ is a positive integer. Then the integer $n$ passes the Miller–Rabin primality test with base $a$ exactly when
    
    $$
    a^u\equiv 1{\textstyle\pmod n},\text{ or }a^{u2^i}\equiv -1{\textstyle\pmod n}\text{ for some }0\le i < t.
    $$
    
    Denote the set of such $a$ (or rather of their congruence classes) by $S$; we need to show that
    
    $$
    |S| \le \dfrac14\varphi(n).
    $$
    
    Here $\varphi(n)$ is [Euler's totient function](./euler-totient.md). The proof has three steps.
    
    **Step one**: let $\ell$ be the largest positive integer such that $2^\ell \mid p-1$ holds for all prime factors $p$ of $n$. Then it can be shown that
    
    $$
    S\subseteq S' = \{a\bmod n:a^{u2^{\ell-1}}\equiv\pm 1{\textstyle\pmod n}\}.
    $$
    
    There are only two possibilities for an element $a$ of $S$. If $a^u\equiv 1\pmod n$, then obviously $a^{u2^{\ell-1}}\equiv 1\pmod n$ also holds, i.e., $a\in S'$. If $a^{u2^i}\equiv -1\pmod n$ holds for some $0\le i < t$, then for every prime factor $p\mid n$ we have $a^{u2^i}\equiv-1\pmod p$. Let $\delta_p(a)$ be the [order](./primitive-root.md#order) of $a$ modulo $p$; then clearly $\delta_p(a)\mid u2^{i+1}$ but $\delta_p(a)\nmid u2^{i}$, which means that in the prime factorization of $\delta_p(a)$ the exponent of $2$ is exactly $i+1$, hence $2^{i+1}\mid\delta_p(a)$. By Fermat's little theorem, $\delta_p(a)\mid p-1$, so $2^{i+1}\mid p-1$. This holds for all prime factors $p$ of $n$. Therefore $i+1\le\ell$. This shows that $a^{u2^{\ell-1}} = (a^{u2^i})^{2^{\ell-1-i}} \equiv \pm 1 \pmod n$, so again $a\in S'$. Combining the two possibilities, we get $S\subseteq S'$.
    
    **Step two**: compute the size $|S'|$.
    
    Suppose $n$ has the prime factorization $n = p_1^{e_1}p_2^{e_2}\cdots p_k^{e_k}$. Then by the [Chinese remainder theorem](./crt.md), the condition $a^{u2^{\ell - 1}}\equiv 1\pmod n$ is equivalent to $a^{u2^{\ell - 1}}\equiv 1\pmod{p_i^{e_i}}$ holding for all $p_i^{e_i}$. Since a [primitive root](./primitive-root.md#primitive-root) modulo an odd prime power $p_i^{e_i}$ always exists, the [number of solutions](./residue.md#properties) of the congruence $a^{u2^{\ell - 1}}\equiv 1\pmod{p_i^{e_i}}$ is
    
    $$
    \gcd(u2^{\ell-1},p_i^{e_i-1}(p_i-1)) = \gcd(u2^{\ell-1},p_i-1) = 2^{\ell-1}\gcd(u,p_i-1).
    $$
    
    The first equality holds because $u$ is a divisor of $n-1$ and thus cannot be a multiple of $p_i$; the second equality holds because of the way $\ell$ was chosen. Therefore, by the Chinese remainder theorem, the number of solutions of the congruence $a^{u2^{\ell-1}}\equiv 1\pmod n$ is
    
    $$
    \prod_{p\mid n}2^{\ell-1}\gcd(u,p-1).
    $$
    
    Similarly, the condition $a^{u2^{\ell - 1}}\equiv -1\pmod n$ is equivalent to $a^{u2^{\ell - 1}}\equiv -1\pmod{p_i^{e_i}}$ holding for all $p_i^{e_i}$. For any factor $p_i^{e_i}$, the condition $a^{u2^{\ell - 1}}\equiv -1\pmod{p_i^{e_i}}$ is equivalent to $a^{u2^{\ell - 1}}\not\equiv 1\pmod{p_i^{e_i}}$ and $a^{u2^{\ell}}\equiv 1\pmod{p_i^{e_i}}$ both holding. As above, the number of solutions of the congruence $a^{u2^{\ell}}\equiv 1\pmod{p_i^{e_i}}$ is $2^{\ell}\gcd(u,p_i-1)$, so the number of solutions of the congruence $a^{u2^{\ell - 1}}\equiv -1\pmod{p_i^{e_i}}$ is also equal to
    
    $$
    2^{\ell}\gcd(u,p_i-1) - 2^{\ell-1}\gcd(u,p_i-1) = 2^{\ell-1}\gcd(u,p_i-1).
    $$
    
    Applying the Chinese remainder theorem again, the number of solutions of the congruence $a^{u2^{\ell - 1}}\equiv -1\pmod n$ is equal to
    
    $$
    \prod_{p\mid n}2^{\ell-1}\gcd(u,p-1).
    $$
    
    Therefore, combining the two cases, we have
    
    $$
    |S'| = 2\prod_{p\mid n}2^{\ell-1}\gcd(u,p-1).
    $$
    
    **Step three**: prove that $|S'|\le\varphi(n)/4$.
    
    Combining with the expression for Euler's totient function $\varphi(n)=\prod_ip_i^{e_i-1}(p_i-1)$, we get
    
    $$
    \dfrac{\varphi(n)}{|S'|} = \dfrac{1}{2}\prod_ip_i^{e_i-1}\dfrac{p_i-1}{2^{\ell-1}\gcd(u,p_i-1)}.
    $$
    
    For each $i$, the corresponding factor $p_i^{e_i-1}\dfrac{p_i-1}{2^{\ell-1}\gcd(u,p_i-1)}$ is an even number, so $\varphi(n)/|S'|$ is an integer. Suppose $|S'|\le\varphi(n)/4$ does not hold. Then necessarily $\varphi(n)/|S'|=1,2,3$, i.e.,
    
    $$
    \prod_ip_i^{e_i-1}\dfrac{p_i-1}{2^{\ell-1}\gcd(u,p_i-1)} = 2,4,6.
    $$
    
    Since every factor in the product is even, the product either has only one factor and that factor equals $2,4,6$, or it has exactly two factors, both equal to $2$.
    
    Consider first the case with two factors. Then neither factor has an odd prime factor, so $p_i^{e_i-1}=1$, i.e., $n$ is squarefree. Without loss of generality, let $n=p_1p_2$ with $p_1<p_2$ both prime. Both factors equal $2$, so we always have $p_i-1=2^{\ell}\gcd(u,p_i-1)$. Therefore $p_i=1+2^\ell m_i$, where $m_i$ is odd and $m_i\mid u$. Taking $p_1p_2=n=1+u2^t$ modulo $m_1$ gives $p_1p_2\equiv 1\pmod{m_1}$, hence $p_2\equiv 1\pmod{m_1}$, which shows that $m_1\mid m_2$. The converse also holds. This shows $m_1=m_2$, that is, $p_1=p_2$. This contradicts $p_1<p_2$. So this case is impossible.
    
    Finally, consider the case with only one factor, i.e., the composite number $n=p^e$ with $e>1$. Then necessarily $p^{e-1}\mid 2,4,6$. Therefore the only possibility is $p=3,e=2$, i.e., $n=9$, which contradicts the assumption of the statement. This case is impossible as well.
    
    Combining all cases, $|S'|\le\varphi(n)/4$ holds.
    
    Combining the three steps above, $|S|\le |S'|\le \varphi(n)/4$ holds for all odd composite numbers $n>9$.

Moreover, assuming the [generalized Riemann hypothesis](https://en.wikipedia.org/wiki/Generalized_Riemann_hypothesis) (GRH) holds, for the number $n$ it suffices to test all integers in $[2, \min\{n-2, \lfloor 2\ln^2 n \rfloor\}]$ to **determine** the primality of $n$.[^deterministic-proof]

Within the scope of OI, primality is usually tested for numbers in the range $[1, 2^{64})$. For numbers in $[1, 2^{32})$, choosing the three numbers $\{2, 7, 61\}$ as bases for the Miller–Rabin primality test determines primality; for numbers in $[1, 2^{64})$, choosing the seven numbers $\{2, 325, 9375, 28178, 450775, 9780504, 1795265022\}$ as bases for the Miller–Rabin primality test determines primality.[^witnesses]

One can also choose $\{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37\}$ (i.e., the first $12$ primes) to test primes in the range $[1, 2^{64})$.

Note that if you use the numbers $a$ from the sequences above as bases to determine the primality of $n$:

-   all the numbers must be used, not just those smaller than $n$;
-   replace $a$ with $a \bmod n$;
-   if $a \equiv 0 \pmod n$ or $a \equiv \pm 1 \pmod n$, that round of the test is passed directly.

## Anti-primes

As the name suggests, a prime is a number with only two divisors, so an anti-prime is a number with the most divisors (and the smallest value among those with the same number of divisors); thus anti-primes are defined relative to a set.

An intuitive definition of an anti-prime is: in a set of positive integers, the number with the most divisors and the smallest value is the anti-prime.

???+ abstract "Anti-prime"
    For a positive integer $n$, if every positive integer smaller than $n$ has fewer divisors than $n$, then $n$ is called an **anti-prime** (a.k.a. highly composite number).

???+ warning "Note"
    Do not confuse this with an [emirp](https://en.wikipedia.org/wiki/Emirp), which is a prime that becomes a different prime when its digits are reversed (e.g., 149 and 941 are both emirps, while 101 is not).

### Procedure

So how do we find anti-primes?

First, since we need the number of divisors, the first thing to do is prime factorization. Decompose $n$ into the form $n=p_{1}^{k_{1}}p_{2}^{k_{2}} \cdots p_{m}^{k_{m}}$, where the $p$ are primes and the $k$ are their exponents. Then the total number of divisors is $(k_1+1) \times (k_2+1) \times \cdots \times (k_m+1)$.

But the complexity of prime factorization is obviously high, and the result for one number cannot be reused for the next. So we need a different approach.

Let us look at the characteristics of anti-primes.

1.  An anti-prime must be a product of powers of consecutive primes starting from $2$.

2.  The exponent of a smaller prime is greater than or equal to the exponent of a larger prime, i.e., in $n=p_{1}^{k_{1}}p_{2}^{k_{2}} \cdots p_{m}^{k_{m}}$ we have $k_1 \geq k_2 \geq k_3 \geq \cdots \geq k_m$.

Explanation:

1.  If the primes are not consecutive starting from $2$, then keeping the exponents unchanged and replacing a prime with a smaller prime keeps the number of divisors the same but makes the value of $n$ smaller. The value of $n$ is smallest when the primes are consecutive starting from $2$.

2.  If the exponent of a smaller prime is less than the exponent of a larger prime, then swapping the two primes (keeping the exponents unchanged) leaves the number of divisors of $n$ unchanged but makes the value of $n$ smaller.

There are two more questions:

1.  For a given $n$, up to which prime should we enumerate?

    In the most extreme case $n=p_{1}p_{2} \cdots p_{m}$, so it suffices to multiply consecutive primes while the product is at most $n$. Enumerating a larger prime would mean that the exponent of some earlier prime must be $0$, so the number cannot be an anti-prime.

2.  Up to which exponent should we enumerate?

    Consider an extreme case: when some power of the smallest prime is already larger than the given $n$ (its maximum value), any other form of the decomposition must have a maximum exponent smaller than this exponent. In the extreme case $n$ is a power of $2$, so it suffices to enumerate up to $\lfloor\log_2 n\rfloor$.

Now that we have the details, how exactly do we implement it?

We can regard the moment we arrive at each prime as the root of a tree, and then search level by level. When do we stop?

1.  The current number is already larger than the one we want;

2.  The current factor is no longer needed;

3.  The current number of divisors is larger than the one we want;

4.  The current number of divisors is exactly the one we want (then check whether the minimum $\mathit{ans}$ needs updating).

Then in the DFS we just keep enumerating the exponents level by level and iterating downward.

### Example problems

???+ example "[Codeforces 27E. A number with a given number of divisors](https://codeforces.com/problemset/problem/27/E)"
    Find the smallest natural number with a given number of divisors. The answer is guaranteed not to exceed $10^{18}$.

??? note "Solution idea"
    For this kind of problem, we just use the number of divisors as the return condition of the DFS and keep updating the minimum found.

??? note "Reference code"
    ```cpp
    --8<-- "docs/math/code/prime/prime_1.cpp"
    ```

???+ example "[ZOJ 2562 More Divisors](https://pintia.cn/problem-sets/91827364500/exam/problems/type/7?problemSetProblemId=91827366061)"
    Among the numbers not exceeding $n$, find the one with the most divisors.

??? note "Solution idea"
    Same idea as above, except that the return condition of the DFS has to be changed. Pay attention to the data range in such problems: 32-bit integers may overflow.

??? note "Reference code"
    ```cpp
    --8<-- "docs/math/code/prime/prime_2.cpp"
    ```

## References and notes

1.  Rui-Juan Jing, Marc Moreno-Maza, Delaram Talaashrafi, "[Complexity Estimates for Fourier-Motzkin Elimination](https://arxiv.org/abs/1811.01510)", Journal of Functional Programming 16:2 (2006) pp 197-217.
2.  [数论部分第一节：素数与素性测试 (Number theory, section 1: primes and primality tests)](http://www.matrix67.com/blog/archives/234)
3.  [Miller–Rabin 与 Pollard–Rho 学习笔记 (Notes on Miller–Rabin and Pollard–Rho) - Bill Yang's Blog](https://blog.bill.moe/miller-rabin-notes/)
4.  [Primality test - Wikipedia](https://en.wikipedia.org/wiki/Primality_test)
5.  [Fermat pseudoprime - Wikipedia](https://en.wikipedia.org/wiki/Fermat_pseudoprime)
6.  [桃子的算法笔记——反素数详解（acm/OI）(Taozi's algorithm notes – anti-primes in detail (acm/OI))](https://zhuanlan.zhihu.com/p/41759808)
7.  [The Rabin-Miller Primality Test](http://home.sandiego.edu/~dhoffoss/teaching/cryptography/10-Rabin-Miller.pdf)
8.  [Highly composite number - Wikipedia](https://en.wikipedia.org/wiki/Highly_composite_number)

[^inf-fermat-pp]: Theorem 1 of Pomerance, Carl, John L. Selfridge, and Samuel S. Wagstaff. "The pseudoprimes to 25⋅ 10⁹." Mathematics of Computation 35, no. 151 (1980): 1003-1026. shows that for a fixed base $a$, there are also infinitely many composite numbers that pass the stronger Miller–Rabin primality test.

[^millerrabinproof]: This result and its proof follow Section 3.5 of Crandall, Richard, and Carl Pomerance. Prime numbers: a computational perspective. New York, NY: Springer New York, 2005.

[^deterministic-proof]: Bach, Eric , "[Explicit bounds for primality testing and related problems](https://doi.org/10.2307%2F2008811)", Mathematics of Computation, 55:191 (1990) pp 355–380.

[^witnesses]: For more results of this kind, see [Deterministic variant of the Miller–Rabin primality test](https://miller-rabin.appspot.com/#).
