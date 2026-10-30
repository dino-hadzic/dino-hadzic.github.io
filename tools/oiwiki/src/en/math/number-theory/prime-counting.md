---
title: Prime counting
---

This article introduces sublinear algorithms for the prime counting problem. The prime counting problem asks for the number of primes not exceeding $n$, i.e., $\pi(n)$. For $n\sim 10^8$ it can be computed with a [sieve](./sieve.md) in $\tilde O(n)$ time. However, when $n \sim 10^{10}$ or even larger, sieves and other algorithms based on enumeration become hard to apply. For this situation, this article introduces a series of algorithms that are relatively easy to implement, with time complexities mostly between $\tilde O(n^{2/3})$ and $\tilde O(n^{3/4})$.

The prime counting problem is a special case of the problem of prefix sums of prime powers. Lucy's algorithm introduced in this article generalizes directly to prefix sums of prime powers, and this generalization forms part of algorithms for summing multiplicative functions such as the [Min\_25 sieve](./min-25.md).

???+ tip "Tip"
    This article provides many prime counting algorithms. For readability, none of them has received much constant-factor optimization. These algorithms differ in time and space performance and in implementation difficulty, so readers can choose a suitable algorithm according to their own needs. For data in the range $10^{11}\sim 10^{13}$, the algorithm of the section [Lehmer's truncation rule](#lehmers-truncation-rule) is often already efficient enough and relatively simple to implement, while the [optimized Lucy's algorithm](#further-optimizations) is slightly more complex to implement but has excellent time and space performance. For smaller data ranges, the [original Lucy's algorithm](#lucys-algorithm) is the simplest to implement and has wider uses in summing multiplicative functions.

## Basic concepts and notation

This article uses the following notation:

-   $\mathbf P$ is the set of (positive) primes, and $p_a$ is the $a$-th smallest prime (indices start from $1$). For convenience of exposition, we also set $p_0=1$. In this article, the letters $p$ and $q$ always denote primes.
-   $\operatorname{lpf}(n)$ denotes the least prime factor of $n$. We also set $\operatorname{lpf}(1)=+\infty$.
-   $D(x) = \{\lfloor x/i\rfloor : i = 1,2,\dots,\lfloor x\rfloor\}$. Its properties are described in detail in the section [Properties of floor-division blocks](./sqrt-decomposition.md#properties).
-   $\pi(x)$ is the number of primes not exceeding $x$.
-   $\varphi(x,a)=\#\{n \in\mathbf N_+ : n \le x,~ (p\mid n \implies p > p_a)\}$ is the number of positive integers not exceeding $x$ all of whose prime factors are greater than $p_a$.
-   $P_k(x,a)=\#\{n\in\mathbf N_+ : n \le x,~ n = q_1q_2\cdots q_k,~ \forall i(q_i > p_a)\}$ is the number of positive integers not exceeding $x$ that have exactly $k$ prime factors (counted with multiplicity), all of which are greater than $p_a$.
-   $S(x,a)$ is the number of integers greater than $1$ and not exceeding $x$ that remain in the sieve of Eratosthenes after sieving with the first $a$ primes.

These functions have the following simple properties:

-   $\varphi(x,0) = \lfloor x\rfloor$.
-   $S(x,a) = \varphi(x,a) + \min\{\pi(x),a\} - 1$.
-   $\varphi(x,a) = \sum_{k=0}^{\infty} P_k(x,a)$.
-   $P_0(x,a) = 1$.
-   $P_1(x,a) = \pi(x) - \min\{\pi(x),a\}$.
-   For $x < p_{a+1}^k$, we have $P_k(x,a) = 0$.

All these properties follow easily from the definitions.

## Meissel–Lehmer algorithm

Substituting the expressions for $P_0$ and $P_1$ into the expansion of $\varphi$ and simplifying, we obtain

$$
\pi(x) = \varphi(x,a) + a - 1 - P_2(x,a) - P_3(x,a) - \cdots.
$$

This means that $\pi(x)$ can be obtained by computing the value of $\varphi(x,a)$, with the error given by a series of $P_k$ terms. As the value of $a$ increases, the number of error terms gradually decreases. In particular, for $a = \pi(\sqrt{x})$ we have $P_2(x,a)=P_3(x,a)=\cdots=0$, that is,

$$
\pi(x) = \varphi(x,\pi(\sqrt{x})) + \pi(\sqrt{x}) - 1.
$$

For $\pi(x^{1/3}) \le a < \pi(\sqrt{x})$, the term $P_2(x,a)$ is nonzero, but the subsequent terms are still zero, i.e.,

$$
\pi(x) = \varphi(x,a) + a - 1 - P_2(x,a).
$$

Similarly, for $\pi(x^{1/4}) \le a < \pi(x^{1/3})$, both terms $P_2(x,a)$ and $P_3(x,a)$ are nonzero, and so on. In short, using these relations, the computation of $\pi(x)$ can be reduced to the computation of $\varphi(x,a)$ and of the terms $P_k(x,a)$. All algorithms that rely on these reduction relations may be called Meissel–Lehmer algorithms.

For $\varphi(x,a)$, we have the following recurrence relation:

$$
\varphi(x,a) = \varphi(x,a - 1) - \varphi\left(\dfrac{x}{p_a},a-1\right).
$$

Naturally, the boundary condition is given by $\varphi(x,0) = \lfloor x\rfloor$.

???+ example "Example"
    Take $x=30,a=2$ as an example ($p_a=3$); one step of the recurrence is shown in the figure below:
    
    ![](images/phi-recurrence.svg)
    
    In the figure, green cells denote integers all of whose prime factors are greater than $p_a=3$ ($1$ has no prime factors and is also counted), while green and orange cells together denote integers all of whose prime factors are greater than $2$. The number of the former is $\varphi(x,a)=\varphi(30,2)=10$, and the number of the latter is $\varphi(x,a-1)=\varphi(30,1)=15$.
    
    The difference between the two is exactly the orange part: numbers divisible by $3$ that have no prime factor smaller than $3$. Hence all orange numbers have the form $n=3k$. Since every prime factor of $k$ is also a prime factor of $n$, $k$ likewise has no prime factor smaller than $3$, i.e., $k$ itself also falls in a green or orange cell; moreover, from $3k\le 30$ we get $k\le\lfloor x/p_a\rfloor=10$. The converse holds as well: the prime factors of $n=3k$ are nothing but $3$ and the prime factors of $k$, so as long as $k\le 10$ and it has no prime factor smaller than $3$, $n$ falls in the orange part. The two are therefore in one-to-one correspondence.
    
    The table is deliberately arranged in $30/3=10$ columns, so the first row is exactly $1,\dots,10$. Such $k$ are precisely the green and orange cells inside the dashed box, $\varphi(x/p_a,a-1)=\varphi(30/3,1)=5$ in total; the label $3\times k$ in the upper right corner of each orange cell indicates its corresponding $k$. Therefore
    
    $$
    \varphi(x,a) = \varphi(x,a-1) - \varphi\left(\left\lfloor\dfrac{x}{p_a}\right\rfloor,a-1\right).
    $$
    
    That is, $\varphi(30,2)=\varphi(30,1)-\varphi(30/3,1)=15-5=10$.

The recursion tree obtained by computing recursively with this relation is a binary tree. Expanding it completely, we get

$$
\varphi(x,a) = \sum_{n\mid p_1p_2\cdots p_a} \mu(n)\left\lfloor\dfrac{x}{n}\right\rfloor.
$$

It follows that the number of leaves of this binary tree equals the number of all squarefree $p_a$-smooth numbers (i.e., integers with no prime factor exceeding $p_a$) not exceeding $x$, and this number is $\Theta(x)$[^smooth]. This means that the complexity of direct recursive computation is still $\Omega(x)$. For fast computation, this binary tree needs to be pruned appropriately. The main difference between the various Meissel–Lehmer algorithms lies precisely in the pruning method. In the literature these are called **truncation rules**. Next, this section focuses on several simple truncation rules.

Finally, we deal with $P_k(x,a)$. Taking $P_2(x,a)$ as an example, we have

$$
\begin{aligned}
P_2(x,a) &= \sum_{i,j:~p_a < p_i\le p_j\le x/p_i} 1 = \sum_{i = a+1}^{\pi(\sqrt{x})}\sum_{j=i}^{\pi(x/p_i)} 1 \\
&= \sum_{i = a+1}^{\pi(\sqrt{x})}\left(\pi\left(\dfrac{x}{p_i}\right) - i + 1\right)\\
&= \sum_{i = a+1}^{\pi(\sqrt{x})}\pi\left(\dfrac{x}{p_i}\right)-\dfrac{1}{2}\left(\pi(\sqrt{x})+a-1\right)\left(\pi(\sqrt{x}) - a\right).
\end{aligned}
$$

This means that the computation of $P_2(x,a)$ can be reduced to the computation of several values $\pi(x/p)$. For $k>2$ similar summation formulas still exist, but the number of summation levels grows, so they gradually become impractical. Common algorithms mostly take $a\ge\pi(x^{1/3})$ to avoid computing more $P_k$ terms. In actual computation, the values $\pi(x/p)$ for this part are usually precomputed with a sieve.

Mathematicians thought very early about computing $\pi(x)$ directly without enumeration. Legendre gave the above expression for $a=\pi(\sqrt{x})$, but expanding $\varphi(x,a)$ completely yields too many terms to be practically usable for computation. In 1870, Meissel proposed computing at $a=\pi(x^{1/3})$, reducing the number of terms in the expansion of $\varphi(x,a)$ while the error remains easy to compute. In 1959, Lehmer further improved and simplified the procedure. In 1985, the truncation rule proposed by Lagarias, Miller, and Odlyzko for the first time brought this idea to sublinear complexity, achieving $\tilde O(x^{2/3})$ time complexity and $\tilde O(x^{1/3})$ space complexity. Afterwards, Deléglise and Rivat (1996), Gourdon (2001), Staple (2015), and others made further optimizations in this direction, further reducing the power of $\log x$ in the complexity. It should be noted that, in order to keep good space complexity and handle problems of size around $x\sim 10^{26}$, these algorithms are usually rather intricate. This section greatly simplifies the details and only introduces some simple optimization ideas. This sacrifices some time and space complexity, but the code is easier to implement. Readers interested in the original treatment can study the references at the end of the article on their own.

In addition, besides enumeration methods and the combinatorial methods introduced in this article, $\pi(x)$ can also be computed with analytic methods, achieving $\tilde O(\sqrt{x})$ time complexity. But they cannot be applied in algorithm competitions, so this article does not cover them.

### Lehmer's truncation rule

Lehmer (1959) proposed a truncation rule. In the following two cases, $\varphi(u,b)$ is no longer expanded:

1.  when $u < p_b$;
2.  when $b = c$, where $c$ is a small positive integer chosen in advance.

In the first case, by the earlier discussion, necessarily $\varphi(u,b)=1$, so nothing needs to be computed. In the second case, the value $\varphi(u,c)$ needs to be computed additionally. By definition,

$$
\varphi(u,c) = \sum_{n=1}^{u} \prod_{b=1}^{c} [p_b \nmid n].
$$

Since the divisibility relation by $p_b$ is periodic with period $p_b$, the summand $\prod_{b=1}^{c} [p_b \nmid n]$ is periodic with period $p_c\# = \prod_{b=1}^{c}p_b$. Using the periodicity, we have

$$
\varphi(u,c) = \left\lfloor\dfrac{u}{p_c\#}\right\rfloor \varphi(p_c\#, c) + \varphi(u \bmod p_c\#, c).
$$

Therefore, as long as all values $\varphi(n,c)$ for $n=0,1,2,\dots,p_c\#$ are precomputed with the recurrence relation, the value $\varphi(u,c)$ in the second case can be looked up quickly.

It should be noted that although these two truncation rules do improve computational efficiency, the asymptotic complexity of the algorithm does not improve significantly. Lagarias, Miller, and Odlyzko (1985) proved that in Lehmer's algorithm the number of leaves of the recursion tree is $\Omega\left(\dfrac{x}{\log^4 x}\right)$, so the time complexity is still $\tilde\Theta(x)$.

Of course, the first truncation rule proposed by Lehmer can be improved appropriately:

$$
\varphi(u,b) = \begin{cases}
1,  & u \le p_b,\\
\pi(u) - b + 1, & p_b < u \le p_b^2,\\
\pi(u) -\dfrac{1}{2}\left(\pi(\sqrt{u})+b-2\right)\left(\pi(\sqrt{u}) - b+1\right) + \sum\limits_{i = b+1}^{\pi(\sqrt{u})}\pi\left(\dfrac{u}{p_i}\right), & p_b^2 < u \le p_b^3.
\end{cases}
$$

The last two cases use the relations derived earlier. This improvement further reduces the size of the recursion tree, but introduces more $\pi(u/p)$ terms that need to be computed. Since $u/p$ can reach up to $x/p_{c+1}$, in order to reduce ineffective pruning, one can set an upper bound $V$ on the $u$ for which this rule may be triggered, and precompute the values $\pi(u)$ for $[1,V]$; when $u > V$, the normal recursion is still used.

Below is an implementation of the improved Lehmer truncation rule:

??? example "Reference implementation"
    ```cpp
    --8<-- "docs/math/code/prime-counting/lehmer.cpp:core"
    ```

Although the theoretical complexity of this implementation is hard to prove[^sgtlaugh], its advantage is a very small constant factor and a simple implementation, so the code runs very efficiently in practice. The values of the constants $c,V,N$ etc. in the code can be adjusted according to actual needs.

### LMO truncation rule

Lagarias, Miller, and Odlyzko (1985) proposed another truncation rule. Choose $y$ satisfying $x^{1/3} \le y \le x^{2/5}$ and take $a=\pi(y)$. Then, in the following two cases, $\varphi(x/n,b)$ is no longer expanded:

1.  when $b=c$ and $n\le y$, where $c$ is a small natural number chosen in advance;
2.  when $n > y$.

LMO call the first case ordinary leaves and the second case special leaves.

The advantage of this truncation rule is that the leaves are easy to count. Note that different leaves necessarily have different $n$. Ordinary leaves always satisfy $n \le y$, so their number is $O(y)$. Special leaves always satisfy $n > y$ and $\dfrac{n}{\operatorname{lpf}(n)} \le y$. Accordingly, special leaves can be divided into two kinds: $\operatorname{lpf}(n) < \sqrt{y}$ and $\operatorname{lpf}(n) \ge \sqrt{y}$. For the first kind, necessarily $\operatorname{lpf}(n) < \sqrt{y}$, so the number of possible $\operatorname{lpf}(n)$ does not exceed $\pi(\sqrt{y})$, and $\dfrac{n}{\operatorname{lpf}(n)} \le y$ has at most $y$ choices, so the number of possible $n$ – that is, the total number of leaves of this kind – does not exceed $y\pi(\sqrt{y})$. For the second kind, necessarily $n=pq$ with $\sqrt{y} \le p < q \le y$, so the number of such leaves is at most $\dfrac{1}{2}\pi(y)^2$. Combining both cases, the total number of special leaves is $O\left(\dfrac{y^2}{\log^2x}\right)$.

For ordinary leaves, the same precomputation method as described earlier can be used. For special leaves, to compute the value $\varphi(x/n,b)$, it can be understood by definition as "the number of positive integers not exceeding $x/n$ whose least prime factor is strictly greater than $p_b$." (Recall that we set $\operatorname{lpf}(1) = +\infty$ earlier.) After this transformation, all queries at special leaves can be processed offline: precompute the values of $\operatorname{lpf}$ for the integers in $[1,x/y]$ and sort them, then update and query with a Fenwick tree. Taking into account the sorting of the offline queries and the Fenwick tree operations, the time complexity of this approach is

$$
O\left(\dfrac{y^2}{\log^2x}\log \dfrac{y^2}{\log^2x} + \left(\dfrac{x}{y} + \dfrac{y^2}{\log^2x}\right)\log\pi\left(\dfrac{x}{y}\right)\right) = O\left(\dfrac{x}{y}\log x + \dfrac{y^2}{\log x}\right).
$$

Apart from the computation of $\varphi(x,a)$, which is special, the rest of the computation is similar to the previous section. It suffices to precompute the values $\pi(u)$ for $[1,x/y]$ and then compute $P_2(x,a)$ using the earlier relation; for the case $c > 0$, the values $\varphi(u,c)$ also need to be precomputed. Note that, to meet the needs of the offline queries, during the recursive search for leaves one also needs to record the sign in front of each leaf, i.e., the value of $\mu(n)$, in order to accumulate the contributions. This yields the complete algorithm.

The time and space complexity of this algorithm are both $\tilde O(x^{2/3})$. If $c = 0$ is taken, the complexity of the other parts is negligible, and the total complexity of this algorithm attains its minimum $O(x^{2/3}\log^{1/3}x)$ at $y = x^{1/3}\log^{2/3}x$. In this case, the space complexity of the algorithm is $O(x^{2/3}\log^{-2/3}x)$. If $c$ is taken to be a small positive integer, the time and space cost of precomputation must be balanced against the constant-factor improvement of the subsequent queries, but the overall complexity does not change.

Below is a reference implementation of this algorithm for $c=0$:

??? example "Reference implementation"
    ```cpp
    --8<-- "docs/math/code/prime-counting/lmo-offline.cpp:core"
    ```

This offline approach has a high space complexity and has difficulty handling problems of size $10^{13}$. The bottleneck is that the $\operatorname{lpf}$ information for $[1,x/y]$ needs to be stored during precomputation. In fact, this information is only used for the subsequent offline queries, and only a single sequential pass is needed, so it can perfectly well be computed at query time with a [segmented sieve](./sieve.md#segmented-sieve).

In fact, the original paper provides an implementation entirely based on the segmented sieve. Both the computation of $P_2(x,a)$ and of $\varphi(x,a)$ are done inside the segmented sieve, yielding an algorithm with $\tilde O(x^{2/3})$ time complexity and $\tilde O(x^{1/3})$ space complexity. This requires enumerating all leaves directly in some way and converting the offline algorithm into an online one. Next, we introduce a simple way to implement it.

The core of the implementation is the segmented sieve: after precomputing the primes in $[1,y]$, split $[1,x/y]$ into blocks of length $y$ and apply the sieve to each block separately. When processing each block, the values $\pi(u)$ and $\varphi(u,b)$ at the elements of that block need to be recorded. Since these values are all counts, they are easy to maintain during the block processing. Then, one needs to find which queries fall into the processing range of that block. In the algorithm described earlier in this section, let $y=\tilde O(x^{1/3})$ and $c=0$. Then the number of primes $\pi(x)$ has the following expression:

$$
\begin{aligned}
\pi(x) &= \dfrac{1}{2}\left(\pi(\sqrt{x})+a-2\right)\left(\pi(\sqrt{x}) - a + 1\right) - \sum_{y < p\le\sqrt{x}}\pi\left(\dfrac{x}{p}\right) \\
&\quad +\sum_{n\le y}\mu(n)\varphi\left(\dfrac{x}{n},0\right) + \sum_{n > y,~{n}/{\operatorname{lpf}(n)}\le y,~\operatorname{lpf}(n)\le y}\mu(n)\varphi\left(\dfrac{x}{n},\pi(\operatorname{lpf}(n))-1\right).
\end{aligned}
$$

The first term only needs the value $\pi(\sqrt{x})$, which can be computed when the block processing reaches that element. The second term requires enumerating primes $p$ such that $x/p$ lies in the block currently being processed; after solving for the interval in which $p$ lies, the corresponding sequence of primes can be obtained with a segmented sieve. Since the interval in which $p$ lies contains no elements greater than $\sqrt{x}$, this inner segmented sieve only needs the primes within $[1,x^{1/4}]$. For the third term, it suffices to enumerate the elements in $[1,y]$. The fourth term requires enumerating the primes in $[1,y]$ as $\operatorname{lpf}(n)$, then determining the range of values of $\dfrac{n}{\operatorname{lpf}(n)}$, and then enumerating those elements in it whose prime factors are not less than $\operatorname{lpf}(n)$[^lmo-segsieve]; this computes the values of this part of the leaves. When computing the contribution of the part in the current block, a Fenwick tree can be used. In this way, while guaranteeing $\tilde O(x^{1/3})$ space complexity, $\tilde O(x^{2/3})$ time complexity is still achieved. Of course, its implementation is somewhat more involved than the offline algorithm.

??? example "Reference implementation"
    ```cpp
    --8<-- "docs/math/code/prime-counting/lmo-online.cpp:core"
    ```

The original paper and subsequent papers classified and discussed special leaves in more detail, further optimizing the time and space complexity. However, the implementation given in this section is sufficient for competition needs, so we no longer discuss those more complex optimization ideas of the Meissel–Lehmer algorithm.

## Lucy's algorithm

When applying the Meissel–Lehmer algorithm, one of the core problems to solve is that the recursion tree of $\varphi(x,a)$ is too large. This is because the termination condition of the recurrence relation of $\varphi(x,a)$ only occurs at $a=0$. Consider replacing $\varphi(x,a)$ with $S(x,a)$. Its advantage is that if $p_a^2 > x$, then sieving with the prime $p_a$ in the sieve of Eratosthenes does not remove any composite number (since they necessarily have a smaller prime factor), i.e., $S(x,a)=S(x,a-1)$. This makes early termination of the recursion tree possible. For the case $p_a^2\le x$, we have $a\le\pi(x)$, so $S(x,a) = \varphi(x,a)+a-1$. Moreover, from $a-1\le\pi(x/p_a)$, all terms in the recurrence relation of $\varphi(x,a)$ can be correspondingly replaced with $S(\cdot,\cdot)$, which yields the recurrence relation of $S(x,a)$. Combining both cases, the recurrence relation of $S(x,a)$ can be written as

$$
S(x,a) = S(x,a-1) - [p_a^2 \le x]\left(S\left(\dfrac{x}{p_a},a-1\right)-(a-1)\right).
$$

The boundary condition is $S(x,0)=\lfloor x\rfloor -1$. Finally, from the relation

$$
\pi(x) = S(x,\pi(\sqrt{x})),
$$

the value of the prime counting function $\pi(x)$ is obtained directly.

???+ example "Example"
    Again for the case $x=30,a=2$, the recurrence relation of $S(x,a)$ is shown in the figure below:
    
    ![](images/s-recurrence.svg)
    
    The initial interval of the sieve of Eratosthenes is $[2,x] = [2,30]$, so cell $1$ is drawn white and does not participate in the count. Gray cells are composite numbers sieved out earlier, orange cells are composite numbers sieved out in this round by the prime $p_a=3$; among the remaining cells, light purple denotes the previous primes, dark purple denotes the current prime $3$, and green denotes integers not yet sieved out (which may be prime or composite, such as $25$). Thus $S(x,a-1)=S(30,1)=15$ is the total of the orange, purple, and green cells, $S(x,a)=S(30,2)=11$ is the total of the purple and green cells, and the difference between the two is exactly those $4$ orange cells.
    
    Similarly to the case of $\varphi(x,a)$, these numbers still have the form $3k$, and from $3k\le 30$ we know that $k$ falls in $[2,\lfloor x/p_a\rfloor] = [2,10]$ inside the dashed box ($k=1$ is not among them, which is exactly why $3$ itself remains and does not turn orange). The difference is that $k$ now only ranges over $3,5,7,9$ (marked in the upper right corner of each orange cell): $k$ must be a survivor of the previous round of sieving (otherwise $3k$ would long ago have been sieved out together with $k$), i.e., $2,3,5,7,9$ inside the box, $S(x/p_a,a-1)=S(10,1)=5$ in total; among these, the primes smaller than $p_a$ must also be removed – they are exactly the first $a-1$ primes, here just $k=2$ – because $3\times 2=6$ was long ago sieved out by $2$. Therefore
    
    $$
    S(x,a) = S(x,a-1) - \left(S\left(\left\lfloor\dfrac{x}{p_a}\right\rfloor, a-1\right) - (a-1)\right).
    $$
    
    That is, $S(30,2)=S(30,1)-\bigl(S(10,1)-(2-1)\bigr)=15-(5-1)=11$.

This recurrence relation is easy to compute with dynamic programming. Since $S(x,a)=S(\lfloor x\rfloor,a)$, all divisions in the recurrence relation can be regarded as integer divisions. By the [properties of floor-division blocks](./sqrt-decomposition.md#properties), the values of the first dimension in the dynamic programming must lie in the set $D(x)$, which has only $\Theta(\sqrt{x})$ elements. Moreover, due to the special form of the recurrence relation, the values $S(\cdot,a)$ can be stored in a single array of length $|D(x)|$; for each $a$, traverse the elements of $D(x)$ from largest to smallest and update the array using the recurrence relation, until the element is strictly smaller than $p_a^2$. Only $\pi(\sqrt{x})$ rounds of updates are needed to obtain the final result.

The space complexity of the algorithm is clearly $O(x^{1/2})$. As for the time complexity, the complexity of the precomputation part is $O(x^{1/2})$, and the complexity of the dynamic programming part is given by

$$
I = \sum_{a=1}^{\pi(\sqrt{x})}|\{u\in D(x) : u \ge p_a^2\}|
$$

It can be estimated in two parts. For $a\in[1,\pi(x^{1/4})]$, since the summand does not exceed $|D(x)|$, this part of the sum does not exceed $\pi(x^{1/4})|D(x)|$, which is $O(x^{3/4}\log^{-1}x)$. For $a\in(\pi(x^{1/4}),\pi(\sqrt{x})]$, we have $p_a^2 > \sqrt{x}$; from the structure of the set $D(x)$, the number of these elements is exactly $\lfloor x/p_a^2\rfloor$. From this, combined with the prime number theorem $p_a\sim a\log a$, we get

$$
\sum_{a=\pi(x^{1/4})+1}^{\pi(\sqrt{x})}\dfrac{x}{p_a^2} \in O\left(\int_{\pi(x^{1/4})}^{+\infty}\dfrac{x}{a^2\log^2a}da\right) = O\left(\dfrac{x^{3/4}}{\log x}\right).
$$

Adding the two parts, the overall time complexity of the algorithm is $O(x^{3/4}\log^{-1}x)$.

In a concrete implementation, the step of precomputing the primes not exceeding $\sqrt{x}$ can be merged into the dynamic programming process. It suffices to enumerate all integers $u$ in the interval $[2,\sqrt{x}]$ from small to large and check the condition $S(u,\pi(u-1)) \neq S(u-1,\pi(u-1))$ to find all primes in the interval; when the condition holds, a state transition must be performed. The reason is that when the enumeration reaches $u$, the transition to $S(\cdot,\pi(u-1))$ has already been made, so $\pi(u) = S(u,\pi(u-1))$ and $\pi(u-1) = S(u-1,\pi(u-1))$, and the above condition holding necessarily means that $u$ is prime. In addition, the value $a-1$ in the state transition equation is also given by $S(u-1,\pi(u-1))$, so it does not need to be maintained separately. This yields the following implementation:

??? example "Reference implementation"
    ```cpp
    --8<-- "docs/math/code/prime-counting/lucy.cpp:core"
    ```

This algorithm is simple to implement; although its time complexity is slightly worse, thanks to its very small constant factor it performs excellently for smaller data sizes. More importantly, since $\pi(x)=S(x,a)$ holds for all $a\ge \pi(\sqrt{x})$, as a byproduct the algorithm actually obtains the values of $\pi(\cdot)$ at all elements of the set $D(x)$. This property is especially important in problems of summing multiplicative functions; its generalization and applications will be discussed later.

### Fenwick tree optimization

Using a Fenwick tree, it is easy to reduce the time complexity of Lucy's algorithm from $\tilde O(x^{3/4})$ to $\tilde O(x^{2/3})$.

To this end, take a real number $y\in (\sqrt{x},x]$. The current state $S(\cdot,a)$ is maintained in two parts: the part greater than $y$ is still computed recursively according to the recurrence relation above; the part not greater than $y$ is maintained with the sieve of Eratosthenes, using a Fenwick tree to update and query the current values of $S(\cdot,a)$.

The space complexity of the algorithm is clearly $O(y)$. To compute the time complexity of the algorithm, the following three parts need to be considered: in the sieve of Eratosthenes part, every composite number sieved out requires one update of the Fenwick tree, $O(y)$ composite numbers in total, so the total time cost is $O(y\log y)$; for $p_a^2 \le y$, the state transition of the corresponding round needs to be performed $O(x/y)$ times, each transition involving an $O(\log y)$ query, with $O(\pi(\sqrt{y}))$ such rounds in total, so the total time cost is

$$
O\left(\pi(\sqrt{y})\dfrac{x}{y}\log y\right) = O\left(\dfrac{x}{\sqrt{y}}\right)
$$

Finally, for $p_a^2 > y$, the state transition of the corresponding round needs to be performed $O(x/p_a^2)$ times, and by the method of the previous subsection the total time cost is

$$
O\left(\sum_{a=\pi(\sqrt{y})+1}^{\pi(\sqrt{x})}\dfrac{x}{p_a^2}\log y\right) = O\left(\dfrac{x}{\sqrt{y}}\right)
$$

Adding the three parts and setting $y = x^{2/3}\log^{-2/3}x$, we get the overall time complexity $O(x^{2/3}\log^{1/3}x)$. In this case, the space complexity is also $\tilde O(x^{2/3})$.

??? example "Reference implementation"
    ```cpp
    --8<-- "docs/math/code/prime-counting/lucy-fenwick.cpp:core"
    ```

It should be noted that although the theoretical time complexity is indeed reduced, the constant-factor loss introduced by the Fenwick tree actually makes the algorithm slower for smaller data sizes, while for larger data sizes the significantly worse memory usage limits the algorithm's use. Therefore, this optimization is not very practical.

### Further optimizations

Although the Fenwick tree successfully optimizes Lucy's algorithm to $\tilde O(x^{2/3})$, the actual running efficiency is still not high. To obtain an efficient algorithm, Lucy's algorithm can be further optimized as follows (let $z < w < y < x$, all of which are powers of $x$):

1.  In the Fenwick-tree-optimized Lucy's algorithm, the time cost of the sieve of Eratosthenes part is $O(y\log y)$. In fact, in the first several rounds of state transitions, the number of composite numbers sieved out is huge, and there is no need to maintain them with a Fenwick tree. Therefore, one can choose $z < y$. When $p_a \le z$, only the state transition equation is used; when $p_a > z$, the Fenwick tree is introduced to maintain the part of $S(\cdot,a)$ not exceeding $y$. Since by the time the Fenwick tree is introduced all integers containing a prime factor not greater than $z$ have already been sieved out, among the remaining numbers – usually called $z$-rough numbers – only $O\left(\dfrac{y}{\log z}\right)$ do not exceed $y$[^rough]. Thus the time cost of the sieve part can be reduced to $O(y)$. The time cost introduced by these initial rounds of state transitions is $O(x^{1/2}z/\log x)$.

2.  Lucy's algorithm described above ultimately obtains the values of $\pi(\cdot)$ at all elements of $D(x)$. If only the value $\pi(x)$ is wanted, many state transitions are unnecessary. For example, to compute the value $S(x,a)$, one only needs to know the values $S(x,a-1)$ and $S\left(\dfrac{x}{p_a},a-1\right)$; and to compute these two values, one only needs to know the values

    $$
    S(x,a-2),~ S\left(\dfrac{x}{p_a},a-2\right),~ S\left(\dfrac{x}{p_{a-1}},a-2\right),~ S\left(\dfrac{x}{p_ap_{a-1}},a-2\right)
    $$

    By induction, at the $i$-th round of state transitions, the $n$ in the states $S\left(\dfrac{x}{n},i\right)$ whose values need to be known must be $p_i$-rough numbers. Since $p_i$-rough numbers are closed under multiplication, it suffices to process all $p_i$-rough numbers (as divisor nodes) at every state transition to guarantee that, when the state transitions terminate, the node values at all $p_i$-rough numbers are correct.

    Of course, the set of $p_i$-rough numbers can be maintained dynamically during the sieving process[^lucy-rough]; alternatively, the earlier set of $z$-rough numbers can be reused in place of all the sets of $p_i$-rough numbers. The second approach seemingly does some useless work, but both reduce the complexity of the state transition part by a factor of $\log x$; they only differ in the constant factor.

3.  Similarly to the sieve part, the state transition part also has the problem of the extra $\log x$ factor introduced by the Fenwick tree. To reduce Fenwick tree queries, the part of the Fenwick tree that is no longer updated can be stored in a static array. Specifically, when the state transitions reach the $i$-th round, the values $S(u,i)$ at $u < p_i^2$ no longer change, so they can be queried and stored.

    Let us compute the complexity improvement this brings. To incorporate the influence of the other optimizations, here we assume that state transitions with the Fenwick tree sieve are only used for the part $z < p_i \le w$, and assume $y \ge w^2$ so that the counts below are tight. Since the $u$ for which a state transition needs to be performed necessarily have the form $\lfloor x/j\rfloor$, it suffices to count the corresponding $j$. For ease of computation, we ignore the discussion of the boundaries of the inequalities. Since $u > y$, necessarily $j < x / y$. If $jp_i < x / y$, the Fenwick tree is not involved; if $x / y < jp_i < \min\{x/p_i^2,p_ix/y\}$, the query can only be done on the Fenwick tree; if $\min\{x/p_i^3,x/y\} < j < x/y$, the query can be done in the static array or on the Fenwick tree. The total count of the first part is

    $$
    \sum_{z < p_i < w}\dfrac{x}{yp_i} = \dfrac{x}{y}\log\dfrac{\log w}{\log z} \in O\left(\dfrac{x}{y}\right).
    $$

    The total count of the second part is

    $$
    \sum_{z < p_i < y^{1/3}}\dfrac{x}{y}\left(1-\dfrac{1}{p_i}\right) + \sum_{y^{1/3} < p_i < w}\left(\dfrac{x}{p_i^3} - \dfrac{x}{yp_i}\right) \le \dfrac{x}{y}\pi(y^{1/3}) + \dfrac{x}{y^{2/3}\log y} \in O\left(\dfrac{x}{y^{2/3}\log y}\right).
    $$

    The total count of the third part is

    $$
    \sum_{y^{1/3} < p_i < w}\left(\dfrac{x}{y}-\dfrac{x}{p_i^3}\right) \le \pi(w)\dfrac{x}{y} \in O\left(\dfrac{xw}{y\log w}\right).
    $$

    The count of the first part is far smaller than the other two and can be neglected. When $w^2 \le y \ll w^3$, the total count of the third part is far larger than that of the second part. Only then does storing this part of the values in a static array reduce the total time complexity of the state transition part by a factor of $\log x$; otherwise, the queries of the second part become the bottleneck. In summary, after introducing this optimization, the total time complexity of the state transition part is

    $$
    O\left(\max\left\{\dfrac{x}{y^{2/3}},\dfrac{xw}{y\log x}\right\}\right).
    $$

    Note that, since the distribution of rough numbers is roughly uniform, the effect of the second optimization (i.e., the rough number optimization of the state transition part) is independent of this one. If the rough number optimization is applied at the same time, the complexity obtained here can be reduced by another $\log x$.

4.  The state transitions can be terminated early, updating only up to the part $p_a\le w$, and the remaining part is handled with the idea of the Meissel–Lehmer algorithm. Unlike the Meissel–Lehmer algorithm, which relies on $\varphi(x,a)$, $S(x,a)$ stores the values of $\pi(x)$ needed up to $x \le p_a^2$, so no extra precomputation is needed. However, when combined with the previous optimization methods, one must pay attention to the influence of the rough number optimization of the dynamic programming part (i.e., optimization 2) and not use values that have not been correctly updated. Doing so improves both the time and the space complexity of the algorithm, but the specific extent of the improvement depends heavily on the implementation of the remaining parts, so no general analysis is given here. This part of the reference implementation will be analyzed concretely below.

Combine these four small optimizations. For any $w \le x^{1/3}$, with $z < w$ and $w^2 \le y < w^3$, the total time complexity of the sieve part and the state transition part is

$$
O\left(y + \dfrac{z\sqrt{x}}{\log x} + \dfrac{xw}{y\log x}\right).
$$

Hence, at $y=x^{5/8}\log^{-1}x$ and $z=w^{1/2}$, the total time complexity reaches $O\left(\dfrac{\sqrt{xw}}{\log x}\right)$. Here, $z$ is taken as large as possible without increasing the overall complexity, in order to reduce the density of $z$-rough numbers and lower the constant factor of the algorithm.

If the algorithm is terminated early at $w=x^{1/3}$, the time and space complexity of the algorithm are both at least[^complex-third] $O(x^{2/3}\log^{-1}x)$. Below we show that if the algorithm is terminated at $w=x^{1/4}$, lower time and space complexity is obtained.

Let $w=x^{1/4}$. Since the algorithm terminates early at $a=\pi(x^{1/4})$, to obtain $\pi(x)$ we need to use the relation:

$$
\pi(x) = S(x,a) - P_2(x,a) - P_3(x,a).
$$

From the earlier analysis we know

$$
P_2(x,a) = \sum_{i=a+1}^{\pi(\sqrt{x})}\pi\left(\dfrac{x}{p_i}\right) - \dfrac{1}{2}(\pi(\sqrt{x})+a-1)(\pi(\sqrt{x})-a).
$$

Since we have already sieved up to $p_a$, $\pi(\sqrt{x})$ can be obtained from $S(\cdot,a)$. However, since $x/p_i\in[\sqrt{x},x^{3/4})$, the $\pi(\cdot)$ in the sum still does not agree with $S(\cdot,a)$. Hence, expanding further, we have

$$
\sum_{i=a+1}^{\pi(\sqrt{x})}\pi\left(\dfrac{x}{p_i}\right) = \sum_{i=a+1}^{\pi(\sqrt{x})}S\left(\dfrac{x}{p_i},a\right) - \sum_{i=a+1}^{\pi(\sqrt{x})}P_2\left(\dfrac{x}{p_i},a\right).
$$

Substituting back into the previous formula, we get

$$
\begin{aligned}
\pi(x) &= S(x,a) + \dfrac{1}{2}(\pi(\sqrt{x})+a-1)(\pi(\sqrt{x})-a) \\
&\quad - \sum_{i=a+1}^{\pi(\sqrt{x})}S\left(\dfrac{x}{p_i},a\right) + \underbrace{ \sum_{i=a+1}^{\pi(\sqrt{x})}P_2\left(\dfrac{x}{p_i},a\right) - P_3(x,a) }_{\Delta(x)}.
\end{aligned}
$$

To compute $\Delta(x)$, consider its combinatorial meaning. From the definitions of $P_2(x,a)$ and $P_3(x,a)$ we know

$$
\begin{aligned}
\sum_{i=a+1}^{\pi(\sqrt{x})}P_2\left(\dfrac{x}{p_i},a\right) &= \#\{p_ip_jp_k \le x : a < i,~ a < j \le k\},\\
P_3(x,a) &= \#\{p_ip_jp_k \le x : a < i \le j \le k\}.
\end{aligned}
$$

Taking the difference of the two sets, we get

$$
\Delta(x) = \#\{p_ip_jp_k \le x : a < j,~ j < i,~ j \le k\}.
$$

To count, we still consider enumerating the least prime factor $p_j$ (because its enumeration upper bound is the smallest); for fixed $j$, the remaining indices must satisfy $i > j$ and $k \ge j$; hence, splitting off the special case $k=j$, the remaining cases have $i,k > j$, which can be further simplified using symmetry, giving the following expression:

$$
\Delta(x) = \underbrace{\sum_{j=a+1}^{\pi(x^{1/3})}\left(\pi\left(\dfrac{x}{p_j^2}\right) - j\right)}_{i > j = k} + \underbrace{2\sum_{j=a+1}^{\pi(x^{1/3})}\left(\sum_{i=j+1}^{\pi(\sqrt{x/p_j})}\left(\pi\left(\dfrac{x}{p_ip_j}\right) - i\right) \right)}_{i > k > j \text{ or }k > i > j } + \underbrace{\sum_{j=a+1}^{\pi(x^{1/3})}\left(\pi\left(\sqrt{\dfrac{x}{p_j}}\right) - j\right)}_{i=k > j}.
$$

Rearranging the sums, we get

$$
\Delta(x) = \sum_{j=a+1}^{\pi(x^{1/3})}\left(\pi\left(\dfrac{x}{p_j^2}\right) - j + 2 \sum_{i=j+1}^{\pi(\sqrt{x/p_j})}\pi\left(\dfrac{x}{p_ip_j}\right) - \left( \pi\left(\sqrt{\dfrac{x}{p_j}}\right) ^ 2 - j^2 \right) \right).
$$

Using this expression, the complexity of computing $\Delta(x)$ is (for the estimation method, see the earlier part on the complexity of Lucy's algorithm)

$$
O\left(\sum_{x^{1/4} < p \le x^{1/3}}\pi\left(\sqrt{\dfrac{x}{p}}\right)\right) = O\left(\dfrac{x^{2/3}}{\log^2 x}\right).
$$

This is also the complexity of the computation of the last part. A simple check shows that all terms $\pi(x/n)$ involved in computing $\Delta(x)$ satisfy $x/n\le\sqrt{x} < y$, so they can all be obtained directly from the $S(\cdot,a)$ stored in the Fenwick tree (they need to be stored in a static array in advance, to avoid introducing extra $O(\log x)$ queries).

Combining with the earlier analysis, when $z=x^{1/8},~w=x^{1/4},~y=x^{5/8}\log^{-1}x$, the total time complexity of the sieve and dynamic programming parts is $O(x^{5/8}\log^{-1}x)$, so the overall time complexity of the algorithm is $O(x^{2/3}\log^{-2}x)$. The space complexity is the length of the Fenwick tree, $O(y)=O(x^{5/8}\log^{-1}x)$.

??? example "Reference implementation"
    ```cpp
    --8<-- "docs/math/code/prime-counting/lucy-opt.cpp:core"
    ```

Within the data ranges common in algorithm competitions ($10^{10}\sim 10^{14}$), the time and space cost of this implementation is quite good. It should be noted that although in the theoretical complexity analysis the last part is the complexity bottleneck, since its complexity has a smaller logarithmic factor and a better constant, within the above data ranges the actual bottleneck of the algorithm is still the sieve and dynamic programming parts. This is precisely why optimizing their complexity is indispensable.

## Generalization: prefix sums of prime powers

More generally, consider the following problem:

$$
F_{\text{prime}}(x) = \sum_{p\in\mathbf P,~p\le x}f(p).
$$

That is, compute the sum of the values of the number-theoretic function $f(\cdot)$ at the primes not exceeding $x$. The prime counting function $\pi(x)$ is the special case $f\equiv 1$.

Assume that the number-theoretic function $f$ satisfies the following conditions:

1.  $f$ is completely multiplicative, i.e., $f(mn)=f(m)f(n)$ holds for all positive integers $m,n$;
2.  the prefix sum $F(x)=\sum_{n \le x}f(n)$ is easy to compute.

Common number-theoretic functions satisfying these conditions include power functions and [Dirichlet characters](https://en.wikipedia.org/wiki/Dirichlet_character) (for example, the [Legendre symbol](./quad-residue.md#legendre-symbol)). Of course, if some function can be expressed as a linear combination of several functions satisfying these conditions, its prefix sum over primes can also be obtained. Therefore, the method of this section can handle the cases where $f$ is a polynomial or $f$ is a periodic function[^periodic]. Another, more concise way of handling periodic functions is described in the example problems below.

Under these conditions, the earlier recurrence relation can be generalized. Define $S(x,a)$ as the sum of the values of $f(\cdot)$ at the integers remaining in the interval $[2,x]$ after sieving out the first $a$ primes, i.e.,

$$
S(x,a) = \sum_{1 < n \le x,~ (n\in\mathbf P) \lor (\operatorname{lpf}(n) > p_a)} f(n).
$$

Then the earlier recurrence relation for $S(x,a)$ can be rewritten as follows:

$$
S(x,a) = S(x,a-1) - [p_a^2 \le x]f(p_a)\left(S\left(\dfrac{x}{p_a},a-1\right)-S(p_{a}-1,a-1)\right).
$$

The boundary condition is $S(x,0) = F(x) - 1$. What this formula expresses is similar to before: in the sieve of Eratosthenes, a composite number sieved out by $p_a$ must be the product of $p_a$ and some integer not yet sieved out by the first $a-1$ primes. However, among all integers not yet sieved out by the first $a-1$ primes are the first $a-1$ primes themselves, which need to be removed additionally. Therefore, to obtain the sum of the function values at these composite numbers, using **complete multiplicativity**, the coefficient $f(p_a)$ can be factored out, and the remaining sum is $S(x/p_a,a-1)$ minus the contribution $S(p_a-1,a-1)$ of the first $(a-1)$ primes. Note that the subtracted term can also be written as $S(p_{a-1},a-1)$; they are equal.

Using this recurrence relation, the value of $F_{\text{prime}}(x)$ can be computed with Lucy's algorithm in $O(x^{3/4}\log^{-1}x)$ time, with a space complexity of only $O(x^{1/2})$. Using a Fenwick tree, the time complexity can be reduced to $\tilde O(x^{2/3})$, but this is not very practical.

??? example "Reference implementation for the template problem [Luogu P5493 质数前缀统计 (prime prefix statistics)](https://www.luogu.com.cn/problem/P5493)"
    ```cpp
    --8<-- "docs/math/code/prime-counting/prime-power-sum.cpp"
    ```

In principle, for the generalized Lucy's algorithm it is recommended to precompute the primes rather than merging this into the dynamic programming. This is because the criterion $S(u,\pi(u-1))\neq S(u-1,\pi(u-1))$ does not necessarily hold for general $f$. In addition, although this section only discusses the generalization of Lucy's algorithm, the other algorithms can be generalized similarly; however, Lucy's algorithm can compute the values of $F_\text{prime}$ at all values in $D(x)$, which is more useful for the subsequent summation of multiplicative functions, so this section only introduces its generalization.

## Example problems

???+ example "[Codeforces 665 F. Four Divisors](https://codeforces.com/problemset/problem/665/F)"
    Given $n$, find the number of integers in $[1,n]$ that have exactly $4$ divisors. Here $1\le n\le 10^{11}$.

??? note "Solution"
    An integer with exactly $4$ divisors must have the form $p^3$ or $pq$, where $p,q$ are primes and $p < q$. In the interval $[1,n]$, there are $\pi(n^{1/3})$ integers of the form $p^3$, and the number of integers of the form $pq$ is
    
    $$
    \sum_{p < \sqrt{n}}\left(\pi\left(\dfrac{n}{p}\right)-\pi(p)\right)
    $$
    
    Since all prime counting functions involved in the above expression can be computed from the values in the set $D(n)$, a single run of Lucy's algorithm suffices to solve the problem. The time complexity is $O(n^{3/4}\log^{-1}n)$, and the space complexity is $O(n^{1/2})$.

??? note "Reference implementation"
    ```cpp
    --8<-- "docs/math/code/prime-counting/prime-count-1.cpp"
    ```

???+ example "[LOJ 6028. “from CommonAnts” 质数计数 II (prime counting II)](https://loj.ac/p/6028)"
    Given $n,m$, find, for each of the residues $0,1,2,\dots,m-1$, how many primes in $[1,n]$ are congruent to it modulo $m$. Here $1\le n\le 3\times 10^{10}$, $1 < m\le 12$, and $n > m$.

??? note "Solution"
    For any residue $r=0,1,2,\dots,m-1$, the function $[n\bmod m = r]$ is clearly periodic. As explained earlier, such problems can be handled by summing Dirichlet characters, but that is too cumbersome and involves complex-number computation. Therefore, this problem is solved with another method.
    
    Consider adding one dimension to the state transition equation of Lucy's algorithm. Let $S(n,r,a)$ denote the number of integers in $[2,n]$ that remain after sieving with the first $a$ primes and are congruent to $r$ modulo $m$. Similarly to the main text, the following recurrence relation is obtained:
    
    $$
    S(n,rp_a\bmod m,a) = S(n,rp_a\bmod m,a-1) - [p_a^2 \le n]\left(S\left(\dfrac{n}{p_a},r,a-1\right)-S(p_{a}-1,r,a-1)\right).
    $$
    
    In the recurrence formula, the second argument of the function uses multiplication rather than division, taking into account the possibility that $p_a\mid m$. The boundary condition is $S(n,r,0) = \left\lfloor\dfrac{n-r}{m}\right\rfloor + [r> 1]$. Based on this, the problem can be solved by dynamic programming. The time complexity is $O(mn^{3/4}\log^{-1}n)$, and the space complexity is $O(mn^{1/2})$.

??? note "Reference implementation"
    ```cpp
    --8<-- "docs/math/code/prime-counting/prime-count-2.cpp"
    ```

## Exercises

-   [Counting Primes - Library Checker](https://judge.yosupo.jp/problem/counting_primes)
-   [Luogu P7884 【模板】Meissel-Lehmer (template)](https://www.luogu.com.cn/problem/P7884)
-   [SPOJ NTHPRIME - Nth Prime](https://www.spoj.com/problems/NTHPRIME/)
-   [SPOJ SUMPRIM1 - Sum of primes](https://www.spoj.com/problems/SUMPRIM1/)
-   [SPOJ BBAD - Breaking Math](https://www.spoj.com/problems/BBAD/)
-   [SPOJ APS2 - Amazing Prime Sequence (hard)](https://www.spoj.com/problems/APS2/)
-   [SPOJ DIVFACT4 - Divisors of factorial (extreme)](https://www.spoj.com/problems/DIVFACT4/)

## References and notes

-   [Meissel–Lehmer algorithm - Wikipedia](https://en.wikipedia.org/wiki/Meissel%E2%80%93Lehmer_algorithm)
-   [Lucy's Algorithm + Fenwick Trees - griff's math blog!](https://gbroxey.github.io/blog/2023/04/09/lucy-fenwick.html)
-   [Counting primes in $\tilde O(n^{2/3})$ by Maksim1744 - Codeforces](https://codeforces.com/blog/entry/91632)
-   [题解 P7884【模板】Meissel–Lehmer 算法 (editorial of P7884 “Meissel–Lehmer algorithm”) by 渐变色 - Luogu](https://www.luogu.com.cn/article/q4d4jl20)
-   Lehmer, Derrick H. "On the exact number of primes less than a given limit." Illinois Journal of Mathematics 3, no. 3 (1959): 381-388.
-   Lagarias, Jeffrey C., Victor S. Miller, and Andrew M. Odlyzko. "Computing $\pi(x)$: the Meissel-Lehmer method." Mathematics of Computation 44.170 (1985): 537-560.
-   [Deléglise, Marc, and Joël Rivat. "Computing 𝜋 (𝑥): the Meissel, Lehmer, Lagarias, Miller, Odlyzko method." Mathematics of Computation 65.213 (1996): 235-245.](https://dl.acm.org/doi/abs/10.1090/s0025-5718-96-00674-6)
-   [Staple, Douglas B. "The combinatorial algorithm for computing $\pi(x)$." arXiv preprint arXiv:1503.01839 (2015).](https://arxiv.org/pdf/1503.01839)

[^lucy-rough]: For an implementation with dynamic maintenance, see [the section on optimization tricks in griff's blog post](https://gbroxey.github.io/blog/2023/04/09/lucy-fenwick.html#trick-for-further-optimization).

[^periodic]: Every number-theoretic function with period $m$ that takes nonzero values only at integers coprime to $m$ can be expressed as a linear combination of several Dirichlet characters modulo $m$. Since computing the prefix sum over primes only involves finitely many integers not coprime to $m$, the original periodic function can always be adjusted appropriately so that it takes the value zero at these integers, and thus can be expressed as a linear combination of Dirichlet characters modulo $m$.

[^rough]: See [Buchstab function - Wikipedia](https://en.wikipedia.org/wiki/Buchstab_function#Applications).

[^complex-third]: A simple analysis shows that the time and space complexity of the algorithm is in fact exactly $O(x^{2/3}\log^{-1}x)$.

[^sgtlaugh]: Although the original author annotated in the code that the complexity is roughly $O(x^{2/3})$, actual measurements show that for constant $V$ the complexity is roughly $\Theta(x)$. Even if the size of $V$ is adjusted appropriately according to the problem size, the complexity is still at least $\Omega(x^{0.8})$.

[^smooth]: See [Smooth number - Wikipedia](https://en.wikipedia.org/wiki/Smooth_number#Distribution).

[^lmo-segsieve]: The total number of $n$ enumerated in this step is actually larger than the number of special leaves, but this does not affect the overall complexity. See the original paper for a concrete proof.
