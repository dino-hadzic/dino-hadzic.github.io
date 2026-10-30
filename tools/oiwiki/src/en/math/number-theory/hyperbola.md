---
title: Dirichlet hyperbola method and Du's sieve
---

Prerequisites: [Dirichlet convolution](./dirichlet.md), [floor-division blocks](./sqrt-decomposition.md)

This article introduces the Dirichlet hyperbola method, which can be used to compute the prefix sum of the Dirichlet convolution of two arithmetic functions in sublinear time complexity. Analyzing this algorithm leads to the concept of a block sieve; based on it, the article further introduces a fast method for computing the convolution of block sieves. Finally, the article introduces Du's sieve, which can be used to compute the prefix sum of the quotient of two arithmetic functions in the sense of Dirichlet convolution.

## Dirichlet hyperbola method

The Dirichlet hyperbola method can be used to compute the prefix sum of the Dirichlet convolution of two arithmetic functions.

Let $f,g,h$ be arithmetic functions with $h = f\ast g$. Then, by the definition of Dirichlet convolution, the prefix sum of $h$ is

$$
H(n) = \sum_{k=1}^nh(k) = \sum_{k=1}^n\sum_{xy=k}f(x)g(y).
$$

The set of points traversed by the sum is exactly the set of lattice points in the first quadrant (excluding the coordinate axes) below the hyperbola $xy=n$. Assign the lattice point $(x,y)$ the weight $f(x)g(y)$; then $H(n)$ is the sum of these weights.

![](./images/dirichlet-hyperbola.svg)

As the figure shows, this weight sum can be computed by the inclusion–exclusion principle:

$$
H(n) = \sum_{x=1}^{\lfloor x_0\rfloor}f(x)G\left(\left\lfloor\dfrac{n}{x}\right\rfloor\right) + \sum_{y=1}^{\lfloor y_0\rfloor}F\left(\left\lfloor\dfrac{n}{y}\right\rfloor\right)g(y) - F(\lfloor x_0\rfloor)G(\lfloor y_0\rfloor).
$$

Here $F,G$ are the prefix-sum functions of $f,g$ respectively, and $(x_0,y_0)$ is an arbitrary point on the hyperbola $xy=n$. In the expression, the first term is the weight sum of the green region in the figure, the second term is the weight sum of the orange region, and the third term is the weight sum of the overlap of the two regions. This expression has only $\lfloor x_0\rfloor + \lfloor y_0\rfloor + 1$ terms. For a reasonably chosen $(x_0,y_0)$, its computational complexity is significantly better than brute-force computation of the prefix sum of $h(n)$. This is the **Dirichlet hyperbola method**.

### Computing a value of the convolution prefix sum

The most basic application of the Dirichlet hyperbola method is computing a single value $H(n)$ of the prefix-sum function.

If the values of $F,G$ are known (or can be computed in $O(1)$ time), and hence the values of $f,g$ are also known, then every term in the expression of the Dirichlet hyperbola method can be computed in $O(1)$ time, and the total time complexity is $O(x_0+y_0)$. Since $x_0y_0=n$, the AM–GM inequality shows that the lowest time complexity $O(\sqrt{n})$ is obtained when $x_0=y_0=\sqrt{n}$.

This is not a new result. Setting $x_0 > n$ in the expression of the Dirichlet hyperbola method gives

$$
H(n) = \sum_{x=1}^nf(x)G\left(\left\lfloor\dfrac{n}{x}\right\rfloor\right).
$$

Using the technique of [floor-division blocks](./sqrt-decomposition.md), when the values of $F,G$ are known, this expression can be computed in $O(\sqrt{n})$ time. This is in fact almost equivalent to the algorithm obtained in this section: the two methods require essentially the same known information, and the expressions they compute are roughly the same.

??? note "Explanation of the equivalence"
    Examining the computation of floor-division blocks closely, one finds that the expression actually computed is
    
    $$
    H(n) = \sum_{y\in D(n)}\left(F\left(\left\lfloor\dfrac{n}{y}\right\rfloor\right)-F\left(\left\lfloor\dfrac{n}{y+1}\right\rfloor\right)\right)G(y).
    $$
    
    Here $D(n) = \left\{\left\lfloor\dfrac{n}{x}\right\rfloor : 1 \le x \le n,~x\in\mathbf N_+\right\}$ is the set of key points of floor-division blocks.
    
    By the properties of floor-division blocks, for $x\le\sqrt{n}$ the heights $y = \lfloor n/x\rfloor$ of the corresponding blocks are pairwise distinct, so the lengths of these blocks are all $1$, i.e.,
    
    $$
    \left\lfloor\dfrac{n}{y+1}\right\rfloor + 1 = x = \left\lfloor\dfrac{n}{y}\right\rfloor.
    $$
    
    Therefore, the sum corresponding to these blocks is
    
    $$
    I_1 = \sum_{x=1}^{\lfloor\sqrt{n}\rfloor}\left(F(x)-F(x-1)\right)G\left(\left\lfloor\dfrac{n}{x}\right\rfloor\right) = \sum_{x=1}^{\lfloor\sqrt{n}\rfloor}f(x)G\left(\left\lfloor\dfrac{n}{x}\right\rfloor\right).
    $$
    
    For the remaining blocks, the height $y$ runs over $1,2,\cdots,y^*= \left\lfloor\dfrac{n}{\lfloor\sqrt{n}\rfloor + 1}\right\rfloor$. Applying the [Abel transformation](https://en.wikipedia.org/wiki/Summation_by_parts) (i.e., the summation form of integration by parts) to the remaining sum gives
    
    $$
    \begin{aligned}
    I_2 &= \sum_{y=1}^{y^*}\left(F\left(\left\lfloor\dfrac{n}{y}\right\rfloor\right)-F\left(\left\lfloor\dfrac{n}{y+1}\right\rfloor\right)\right)G(y) \\
    &= \sum_{y=1}^{y^*}F\left(\left\lfloor\dfrac{n}{y}\right\rfloor\right)g(y) - F\left(\left\lfloor\dfrac{n}{y^*+1}\right\rfloor\right)G(y^*).
    \end{aligned}
    $$
    
    The properties of floor-division blocks show that $\lfloor n/\lfloor \sqrt{n}\rfloor\rfloor \ge \lfloor \sqrt{n}\rfloor$. We distinguish two cases:
    
    -   When $\lfloor n/\lfloor \sqrt{n}\rfloor\rfloor = \lfloor \sqrt{n}\rfloor$, necessarily $y^* < \lfloor \sqrt{n}\rfloor$. Since this block is adjacent to the block containing $x = \lfloor \sqrt{n}\rfloor$, the block heights can differ only by exactly one, i.e., $y^* = \lfloor \sqrt{n}\rfloor - 1$. In this case,
    
        $$
        \begin{aligned}
        I_2 &= \sum_{y=1}^{\lfloor\sqrt{n}\rfloor-1}F\left(\left\lfloor\dfrac{n}{y}\right\rfloor\right)g(y) - F(\lfloor\sqrt{n}\rfloor)G(\lfloor\sqrt{n}\rfloor-1)\\
        &= \sum_{y=1}^{\lfloor\sqrt{n}\rfloor-1}F\left(\left\lfloor\dfrac{n}{y}\right\rfloor\right)g(y) -  F(\lfloor\sqrt{n}\rfloor)\left(G(\lfloor\sqrt{n}\rfloor) - g(\lfloor\sqrt{n}\rfloor)\right) \\
        &= \sum_{y=1}^{\lfloor\sqrt{n}\rfloor}F\left(\left\lfloor\dfrac{n}{y}\right\rfloor\right)g(y) - F(\lfloor\sqrt{n}\rfloor)G(\lfloor\sqrt{n}\rfloor).
        \end{aligned}
        $$
    
    -   When $\lfloor n/\lfloor \sqrt{n}\rfloor\rfloor > \lfloor \sqrt{n}\rfloor$, necessarily $y^* = \lfloor \sqrt{n}\rfloor$. Substituting directly into the sum gives
    
        $$
        I_2 = \sum_{y=1}^{\lfloor\sqrt{n}\rfloor}F\left(\left\lfloor\dfrac{n}{y}\right\rfloor\right)g(y) - F(\lfloor\sqrt{n}\rfloor)G(\lfloor\sqrt{n}\rfloor).
        $$
    
    In summary, apart from one Abel transformation, the computation of floor-division blocks is actually computing the following expression:
    
    $$
    H(n) = \sum_{x=1}^{\lfloor\sqrt{n}\rfloor}f(x)G\left(\left\lfloor\dfrac{n}{x}\right\rfloor\right) + \sum_{y=1}^{\lfloor\sqrt{n}\rfloor}F\left(\left\lfloor\dfrac{n}{y}\right\rfloor\right)g(y) - F(\lfloor\sqrt{n}\rfloor)G(\lfloor\sqrt{n}\rfloor).
    $$
    
    This is exactly the expression of the Dirichlet hyperbola method for $(x_0,y_0)=(\sqrt{n},\sqrt{n})$. Hence one can say that the computations of the two algorithms are almost equivalent. Moreover, since the Dirichlet hyperbola method exploits more properties of floor-division blocks and avoids the unnecessary computations of naive floor-division blocks, its constant factor is somewhat smaller.

When dealing with real problems, the condition that the values of $F,G$ are known may be too strong. However, the Dirichlet hyperbola method (or the corresponding floor-division blocks) does not actually need all the values of $F,G$. Looking at the summation expression, we see that only the values of $F$ and $G$ on the set of key points of floor-division blocks

$$
D(n) = \left\{\left\lfloor\dfrac{n}{x}\right\rfloor : 1 \le x \le n,~x\in\mathbf N_+\right\}
$$

are needed. It is both the set of all block heights and the set of all right endpoints of the blocks. Note that by the [properties](./sqrt-decomposition.md#性质) of floor-division blocks, this set contains all integers $1\le x\le\sqrt{n}$, so knowing the values of $F,G$ on $D(n)$ is equivalent to knowing the values of $f,g$ at all $1\le x\le\sqrt{n}$. The size of this set is $\Theta(\sqrt{n})$, so when computing $H(n)$ we only need to know the values of $F,G$ on a sparse set. This observation is the key to optimizing the computation of prefix sums of arithmetic functions.

## Block sieves and their convolution

Sometimes $h=f\ast g$ is not the function whose prefix sum is ultimately needed, but only one of the intermediate steps. According to the analysis above, for the subsequent computation we need the values of the prefix-sum function $H$ on the set $D(n)$. This is called the **block sieve** of the arithmetic function $h$:

$$
\mathcal S_h(n) = \left\{H(x) : x \in D(n)\right\}.
$$

This section discusses methods for the **block sieve convolution** problem: given the block sieves of $f,g$, find the block sieve of their Dirichlet convolution $h = f\ast g$.

### Naive algorithm

The naive algorithm treats the computation of the block sieve as $|D(n)|$ computations of single prefix-sum values. The total time complexity of this is

$$
\begin{aligned}
O\left(\sum_{d\in D(n)}\sqrt{d}\right) &= O\left(\sum_{x=1}^{\lfloor\sqrt{n}\rfloor}\sqrt{x} + \sum_{x=1}^{\lfloor\sqrt{n}\rfloor}\sqrt{\dfrac{n}{x}}\right) \\
&= O\left(\int_1^{\sqrt{n}}\sqrt{x}\mathrm{d}x + \int_1^{\sqrt{n}}\sqrt{\dfrac{n}{x}}\mathrm{d}x\right)\\
&= O(n^{3/4}).
\end{aligned}
$$

It is precisely because the block sieve is sparse that the whole block sieve can be computed in sublinear time.

However, this algorithm is obviously too brute-force. The smaller elements of the set $D(n)$ are relatively dense, so adjacent prefix sums in the block sieve do not differ much; one can simply compute the values of the convolution $h$ directly and then take their prefix sums. This is faster than computing the prefix-sum value separately for each point. For example, computing the prefix-sum values separately for $x = 1,2,\cdots,\lfloor\sqrt{n}\rfloor$ takes

$$
O\left(\sum_{x=1}^{\lfloor\sqrt{n}\rfloor}\sqrt{x}\right) = O(n^{3/4})
$$

time; but computing the values of $h$ at these points directly and then accumulating them takes only $O(n^{1/2}\log n)$ time. Nevertheless, if only the block sieves of $f,g$ are known and nothing more, this idea cannot further optimize the complexity of the algorithm. This is because the block sieve only contains value information for $x \le \sqrt{n}$, so at most the values of $h$ at $1\le x\le\sqrt{n}$ can be computed, while computing the remaining prefix-sum values still takes $O(n^{3/4})$ time.

### Optimization using value information

If the known information includes, besides the block sieves of $f,g$, more of their values, then the complexity of this algorithm can indeed be improved. In practice, this algorithm is usually applied when the values of $f,g$ can be precomputed quickly.

Choose $z \ge \sqrt{n}$. The block sieve of the convolution $h$ is split into two parts:

-   Compute the values of the convolution $h$ of $f\ast g$ at $1\le x \le z$, then accumulate them directly to obtain the values of $H$ at $1\le x\le z$.
-   For $x\in D(n)$ with $x > z$, compute the value of $H$ at $x$ by the Dirichlet hyperbola method.

In the general case, the time complexity of this is

$$
\begin{aligned}
O\left(z\log z + \sum_{d\in D(n),~d\ge z}\sqrt{d}\right) &= O\left(z\log z + \sum_{x=1}^{n/z}\sqrt{\dfrac{n}{x}}\right)\\
&= O\left(z\log z + \int_1^{n/z}\sqrt{\dfrac{n}{x}}\mathrm{d}x\right)\\
&= O\left(z\log z + \dfrac{n}{\sqrt{z}}\right).
\end{aligned}
$$

When $z=\left(\dfrac{n}{\log n}\right)^{2/3}$, the total time complexity is minimized at $O\left(n^{2/3}(\log n)^{1/3}\right)$.

Of course, the complexity of [computing the values](./dirichlet.md#dirichlet-卷积的计算) of a Dirichlet convolution depends on the properties of $f,g,h$. When $f,g,h$ have special properties, the optimal split point and the complexity are slightly different:

-   If $f$ or $g$ is multiplicative, then when $z=\left(\dfrac{n}{\log\log n}\right)^{2/3}$ the total time complexity is minimized at $O\left(n^{2/3}(\log\log n)^{1/3}\right)$.
-   If $h$ is multiplicative, then when $z=n^{2/3}$ the total time complexity is minimized at $O(n^{2/3})$.

Applying this optimization does not require all the values of $f,g$, only their values at $1\le x\le z$. Since this algorithm also yields the values of $h$ at $1\le x\le z$, when $h$ is an intermediate variable, the values of $h$ can likewise be used to optimize the subsequent computation. The block sieve of an arithmetic function together with these values forms an enhanced block sieve: they are all the information necessary to compute convolution prefix sums in $O(n^{2/3+\varepsilon})$ time.

### Fast block sieve convolution

Prerequisites: [fast Fourier transform](../poly/fft.md)

???+ warning "Note"
    Beginners may skip this section.

This section discusses the fast block sieve convolution algorithm proposed by Zhou Kangyang in his 2024 Chinese national training team paper. It computes the values of $\mathcal S_h$, the convolution of the block sieves $\mathcal S_f$ and $\mathcal S_g$, in $O(\sqrt{n}\log^2n)$ time. This algorithm does not depend on additional value information or on the multiplicativity of the arithmetic functions, but its implementation is rather complex.

The block sieve convolution problem asks for the prefix sums of

$$
h(z) = \sum_{xy=z} f(x)g(y)
$$

on the block sieve $D(n) = \{\left\lfloor n / t\right\rfloor : 1\le t \le n\}$. For this problem, a single contribution can be labeled by $(x,y,t)$, i.e., the process of adding the term $f(x)g(y)$ to the prefix sum at $\left\lfloor n / t\right\rfloor$. The algorithm handles these contributions in several groups.

First, consider the contributions of all points with $x > \sqrt{n}$ to this series of prefix sums; the contributions with $y > \sqrt{n}$ are handled similarly. Since every contribution must satisfy $xy \le \lfloor n / t\rfloor$, i.e., $xyt \le n$, it suffices to enumerate all possible $t,y$, and using the prefix-sum technique together with the information in the block sieve $\mathcal S_f$, this part of the contributions can be computed in $O(\sum_{t,y: ty\le\sqrt{n}} 1) = O(\sqrt{n}\log n)$ time.

Next, consider the part of the contributions with $\left\lfloor n / t\right\rfloor\le\sqrt{n}$. This part can likewise be done by brute-force enumeration of all possible $x,y$, and the time complexity is still $O(\sum_{x,y:xy\le\sqrt{n}}1) = O(\sqrt{n}\log n)$. This part actually yields the first $\lfloor\sqrt{n}\rfloor$ values of the function $h$ on $D(n)$.

Consider the remaining contributions, i.e., those satisfying $x,y\le\sqrt{n}$ and $\left\lfloor n / t\right\rfloor > \sqrt{n}$. All contributions must satisfy $xyt\le n$, i.e., $\ln x + \ln y \le \ln(n/t)$. Take a positive number $S$; this condition can be approximated by $\lceil S\ln x\rceil + \lceil S\ln y\rceil \le S\ln(n/t)$. Define polynomials $\sigma_f(u)$ and $\sigma_g(u)$ such that their coefficients $[u^k]\sigma_f$ and $[u^k]\sigma_g$ equal, respectively, the sum of $f(x)$ over those with $\lceil S\ln x\rceil = k$ and the sum of $g(y)$ over those with $\lceil S\ln y\rceil = k$ (considering only the part with $x,y\le\sqrt{n}$). Using the fast Fourier transform (FFT) we can obtain their product $\sigma_f\sigma_g$, whose coefficient $[u^k](\sigma_f\sigma_g)$ represents the sum of $f(x)g(y)$ over pairs with $\lceil S\ln x\rceil + \lceil S\ln y\rceil = k$. Thus, for each remaining $\lfloor n/t\rfloor$ in $D(n)$ it suffices to find the largest $k$ satisfying $k \le S\ln(n/t)$ to obtain an estimate of this part of the contributions.

Finally, we correct the error of this part of the contributions. Above, we tried to approximate $\ln x + \ln y \le \ln(n/t)$ by the stronger condition $\lceil S\ln x\rceil + \lceil S\ln y\rceil \le S\ln(n/t)$, which may miss some contributions. This can only happen when $\lceil S\ln x\rceil + \lceil S\ln y\rceil > S\ln(n/t)$, so we have

$$
S\ln x + 1 +  S\ln y + 1 \ge \lceil S\ln x\rceil + \lceil S\ln y\rceil >  S\ln(n/t) \ge S\ln x + S\ln y.
$$

This is equivalent to

$$
xyt \in (n\mathrm{e}^{-2/S},n].
$$

This is an interval of length $O(n/S)$. Enumerating all possible contributions $(x,y,t)$ in the interval and checking one by one whether they were missed completes the error correction. To enumerate all contributions in the interval quickly, we can first sieve all primes not exceeding $\sqrt{n}$, then divide the integers in the interval by these primes; the remaining factor must be a prime greater than $\sqrt{n}$, which yields the prime factorization of all integers in the interval, and then all possible $(x,y,t)$ can be enumerated quickly.

Let us examine the time complexity of computing this last part of the contributions. When estimating the contributions, we need to multiply polynomials of length $S\log n$, with time complexity $O(S\log n\log(S\log n))$. In the error correction, the time complexity of precomputing the prime factorizations is $O(\sqrt{n}+(n/S)\log\log n)$, and the time complexity of enumerating all contributions in the interval is $O(\sum_{k\in(n\mathrm{e}^{-2/S},n]}d_3(k))$, where $d_3(n)$ denotes the number of ways to write $n$ as a product of three ordered integers. A result from analytic number theory[^piltz] states:

$$
\sum_{k\le n}d_3(k) = nP(\log n) + O(n^{43/96+\varepsilon}),
$$

where $P(\cdot)$ is a quadratic polynomial. Since the time complexity of the first two steps is already $O(\sqrt{n}\log n)$, ignoring all $o(\sqrt{n}\log n)$ terms, the time complexity of computing this last part of the contributions is

$$
O\left(S\log n\log(S\log n) + \dfrac{n}{S} \log^2n\right).
$$

Taking $S = \sqrt{n}$ gives a time complexity of $O(\sqrt{n}\log^2n)$. This is also the total time complexity of the algorithm.

??? example "Reference implementation"
    ```cpp
    --8<-- "docs/math/code/hyperbola/fast_bs_conv.cpp:core"
    ```

## Du's sieve

Above we discussed how to compute the prefix sum of the Dirichlet convolution of arithmetic functions. This section considers the reverse process: let $f \ast g = h$ with $f,h$ known; compute the prefix sum of $g$

$$
G(n) = \sum_{x=1}^ng(x).
$$

In other words, this section considers computing the prefix sum of the quotient of two arithmetic functions in the sense of Dirichlet convolution. Throughout this section we assume $f(1)\neq 0$, so that $f$ is invertible.

To this end, setting $x_0 > n$ in the expression of the Dirichlet hyperbola method gives

$$
H(n) = \sum_{x=1}^{n}f(x)G\left(\left\lfloor\dfrac{n}{x}\right\rfloor\right).
$$

Solving directly for $G(n)$ gives

$$
G(n) = \dfrac{1}{f(1)}\left(H(n)-\sum_{x=2}^nf(x)G\left(\left\lfloor\dfrac{n}{x}\right\rfloor\right)\right).
$$

This is the expression of Du's sieve. In fact, for $x_0 \ge 1$ we always have

$$
G(n) = \dfrac{1}{f(1)}\left(H(n)-\sum_{x=2}^{\lfloor x_0\rfloor}f(x)G\left(\left\lfloor\dfrac{n}{x}\right\rfloor\right) - \sum_{y=1}^{\lfloor y_0\rfloor}F\left(\left\lfloor\dfrac{n}{y}\right\rfloor\right)g(y) + F(\lfloor x_0\rfloor)G(\lfloor y_0\rfloor)\right).
$$

In either form, it is a recurrence relation for $G(n)$. To compute the value of $G(n)$, we need to compute the values of $G$ on $D(n)\setminus\{n\}$. Since $D(n)$ has a [recursive structure](./sqrt-decomposition.md#性质), i.e., for $m\in D(n)$ we always have $D(m)\subseteq D(n)$, during the whole recursive computation the value of $G$ at each element of $D(n)$ needs to be computed only once. In other words, when computing $G(n)$, we actually obtain the block sieve $\mathcal S_g(n)$ of $g$.

In a concrete implementation, one can use recursion with memoization to avoid repeated computations. Of course, one can also use an iterative method, computing the values of $G$ at the points of $D(n)$ in increasing order. In this case, the sum in the expression can be computed either with floor-division blocks or with the Dirichlet hyperbola method.

The complexity of these implementations is the same. Since Du's sieve always yields a block sieve, the complexity of Du's sieve is in fact equivalent to the complexity of computing a block sieve. If the only known information is the block sieves of $F,H$, the complexity of Du's sieve is $O(n^{3/4})$; if for some $z\ge\sqrt{n}$ the values of $g$ at $1\le x \le z$ can be precomputed in $T_0(z)$ time, the complexity of Du's sieve is

$$
O\left(T_0(z) + \dfrac{n}{\sqrt{z}}\right).
$$

When $g$ is a multiplicative function, a linear sieve can be applied, i.e., $T_0(z)=\Theta(z)$, so it is optimal to precompute up to $z = n^{2/3}$, and the total time complexity is $O(n^{2/3})$; in the more general case, the total time complexity is $O(n^{2/3}(\log n)^{1/3})$. All of this is fully consistent with the analysis in the block sieve section.

??? warning "A recursive implementation without memoization leads to wrong complexity"
    In the expression of Du's sieve, computing the value of $G(n)$ depends on the values of $G$ on $D(n)\setminus\{n\}$. The key to guaranteeing the complexity here is to notice the recursive structure of the set $D(n)$: when $m\in D(n)$, $D(m)\subseteq D(n)$. Using this property, the computation can be accelerated by memoization. With memoization, as shown above, the complexity of the algorithm is $O(n^{3/4})$. What we want to show here is that without memoization the complexity of the algorithm is wrong.
    
    Let $T(n)$ be the complexity of computing $G(n)$ recursively without memoization. Then we have
    
    $$
    \begin{aligned}
    T(n) &= \Theta(\sqrt{n}) + \sum_{d\in D(n),~d\neq n}T(d)\\
    &= \Theta(\sqrt{n}) + \sum_{x=1}^{\lfloor n/\lfloor\sqrt{n}\rfloor\rfloor - 1} T(x) + \sum_{x = 2}^{\lfloor\sqrt{n}\rfloor}T\left(\left\lfloor\dfrac{n}{x}\right\rfloor\right).
    \end{aligned}
    $$
    
    Using a proof idea similar to that of the [master theorem](../../basic/complexity.md#master-theorem), one can show that the last term dominates the growth of this expression and that $T(n)\in\Theta(n^\alpha)$, where $\alpha\approx 1.73$ is the root of $\zeta(\alpha)=2$.

When applying Du's sieve to compute the prefix sum of an arithmetic function $g$, the key is to find suitable $f,h$ such that $h=f\ast g$ and the block sieves of $f,h$ are both easy to compute. Sometimes such $f,h$ are obvious; at other times they need to be derived using the properties of Dirichlet convolution, and the corresponding decomposition can also be found by computing the corresponding Dirichlet generating functions or Bell series (when multiplicativity holds). The examples below illustrate these situations.

## Example problems

This section presents several problems on computing prefix sums of arithmetic functions.

???+ example "[AtCoder Regular Contest 116 C - Multiple Sequences](https://atcoder.jp/contests/arc116/tasks/arc116_c)"
    Given positive integers $N$ and $M$. Compute how many sequences $A$ of length $N$ satisfy $1 \le A_i \le M$ and $A_i$ divides $A_{i+1}$. The answer is taken modulo $998244353$. Constraints: $1 \le N, M \le 2\times 10^5$.

??? note "Solution"
    Let $f_n(m)$ be the number of sequences of length $n$ with $A_n=m$. Then the final answer is $\sum_{m=1}^M f_N(m)$. To compute $f_n(m)$, consider dynamic programming. The transition equation is:
    
    $$
    f_n(m) = \sum_{k\mid m}f_{n-1}(k).
    $$
    
    In the notation of Dirichlet convolution, it can be written as $f_n = f_{n-1}\ast 1$, where $1$ is the constant arithmetic function. Note that $f_1 = 1$, so by induction $f_n = 1 ^{\ast n}$. That is, $f_n$ is the convolution of $n$ constant functions. The final answer is the prefix sum of $f_N$. Since only multiplicative functions are involved in the process, using the method for computing prefix sums of Dirichlet convolutions introduced above, a single convolution prefix-sum computation takes only $O(M^{2/3})$ time; using [binary exponentiation](../binary-exponentiation.md), only $O(\log N)$ convolution prefix-sum computations are needed to obtain the value of the convolution prefix sum of $f_N$. The overall time complexity is $O(M^{2/3}\log N)$.

??? note "Reference implementation"
    ```cpp
    --8<-- "docs/math/code/hyperbola/hyperbola.cpp"
    ```

???+ example "[P4213【模板】杜教筛（Sum） (Template: Du's sieve (Sum))](https://www.luogu.com.cn/problem/P4213)"
    Let $\mu$ and $\varphi$ be the Möbius function and Euler's totient function, respectively. Compute the values of $S_1(n)= \sum_{i=1}^{n} \mu(i)$ and $S_2(n)= \sum_{i=1}^{n} \varphi(i)$. Constraints: $1\leq n<2^{31}$.

??? note "Solution"
    Note the Dirichlet convolution relations:
    
    $$
    \varepsilon = \mu \ast 1,~ \operatorname{id} = \varphi \ast 1.
    $$
    
    Here $\varepsilon(n) = [n=1]$ is the identity element of Dirichlet convolution, $\operatorname{id}(n) = n$ is the identity function, and $1(n) = 1$ is the constant function. Since the prefix sums of these three functions can all be computed in $O(1)$ time and they are all multiplicative, the Du's sieve method introduced above computes them in $O(n^{2/3})$ time.
    
    For computing the prefix sum of Euler's totient function, another method is to use [Möbius inversion](./mobius.md). Note that
    
    $$
    \begin{aligned}
    S_2(n) &= \sum_{i=1}^n\varphi(i) = \sum_{i=1}^n\sum_{j=1}^i[i\perp j] \\
    &= \sum_{i=1}^n\sum_{j=1}^i\sum_d\mu(d)[d\mid i][d\mid j] \\
    &= \sum_d\mu(d)\dfrac{1}{2}\left\lfloor\dfrac{n}{d}\right\rfloor\left(\left\lfloor\dfrac{n}{d}\right\rfloor+1\right).
    \end{aligned}
    $$
    
    In the floor-division blocks process, the prefix sum of $\mu(d)$ is needed, and it can be precomputed with Du's sieve. The time complexity is still $O(n^{2/3})$.

??? note "Reference implementation"
    ```cpp
    --8<-- "docs/math/code/du/du_1.cpp"
    ```

???+ example "[“Luogu P3768” 简单的数学题 (A simple math problem)](https://www.luogu.com.cn/problem/P3768)"
    Given $p,n$, compute
    
    $$
    \sum_{i=1}^n\sum_{j=1}^nij\cdot\gcd(i,j)\pmod p.
    $$
    
    Constraints: $n\leq 10^{10}$, $5\times 10^8\leq p\leq 1.1\times 10^9$, and $p$ is prime.

??? note "Solution"
    Using the properties of [Euler's totient function](./euler-totient.md), perform the following inversion:
    
    $$
    \begin{aligned}
    T(n) &= \sum_{i=1}^n\sum_{j=1}^nij\cdot\gcd(i,j)\\
    &= \sum_{i=1}^n\sum_{j=1}^nij\sum_d\varphi(d)[d\mid i][d\mid j]\\
    &= \sum_d\varphi(d)\left(\sum_{i=1}^{\lfloor n/d\rfloor}id\right)\left(\sum_{j=1}^{\lfloor n/d\rfloor}jd\right)\\
    &= \sum_d d^2\varphi(d) F\left(\left\lfloor\dfrac{n}{d}\right\rfloor\right)^2.
    \end{aligned}
    $$
    
    Here $F(n) = \dfrac{1}{2}n(n+1)$. This expression can be computed with floor-division blocks, but the prefix sum of $d^2\varphi(d)$ must be precomputed.
    
    For this, Du's sieve can be used. Let $f(n)=(\operatorname{id}^2\varphi)(n)$ and $S(n)=\sum_{i=1}^n f(i)$. The key to applying Du's sieve is to construct a function $g$ such that both $f\ast g$ and $g$ can be summed quickly. Above we already discussed precomputing the prefix sum of $\varphi$ with Du's sieve, which only requires the relation $\operatorname{id} = \varphi\ast 1$. Compared with $\varphi$, the $f$ here has an extra factor $\operatorname{id}^2$. Since $\operatorname{id}$ is a completely multiplicative function, by the [properties](./dirichlet.md#性质) of Dirichlet convolution it suffices to similarly multiply each term by $\operatorname{id}^2$, which gives
    
    $$
    \operatorname{id}^3 = f \ast \operatorname{id}^2.
    $$
    
    Since the prefix sums of $\operatorname{id}^2(n)=n^2$ and $\operatorname{id}^3(n)=n^3$ can both be computed in $O(1)$ time, the prefix sum of $f$ can be precomputed in $O(n^{2/3})$ time. Together with floor-division blocks, the overall time complexity is still $O(n^{2/3})$.
    
    Another way to represent a similar multiplicative function as the quotient (in the sense of Dirichlet convolution) of two functions is to use [Dirichlet generating functions](./dirichlet.md#dirichlet-生成函数).

??? note "Reference implementation"
    ```cpp
    --8<-- "docs/math/code/du/du_2.cpp"
    ```

## Exercises

-   [AtCoder Xmas Contest 2019 D - Sum of (-1)^f(n)](https://atcoder.jp/contests/xmascon19/tasks/xmascon19_d)

## References and notes

-   Ren Zhizhou. 2016. 《积性函数求和的几种方法》 (Several methods for summing multiplicative functions). 2016 paper of a candidate for the Chinese national team in informatics.
-   Zhou Kangyang. 2024. 《关于积性函数求和问题的一些进展》 (Some progress on the summation problem of multiplicative functions). 2024 paper of a candidate for the Chinese national team in informatics.
-   [Dirichlet hyperbola method - Wikipedia](https://en.wikipedia.org/wiki/Dirichlet_hyperbola_method)
-   [杜教筛的时空复杂度分析 (Time and space complexity analysis of Du's sieve) - riteme.site](https://riteme.site/blog/2018-9-11/time-space-complexity-dyh-algo.html)
-   [OI 中常用数论函数求和法的简化陈述 (A simplified account of common summation methods for arithmetic functions in OI) by negiizhao - UOJ](https://negiizhao.blog.uoj.ac/blog/7165)
-   [Dirichlet 積と、数論関数の累積和 (Dirichlet product and prefix sums of arithmetic functions) by maspy](https://maspypy.com/dirichlet-%e7%a9%8d%e3%81%a8%e3%80%81%e6%95%b0%e8%ab%96%e9%96%a2%e6%95%b0%e3%81%ae%e7%b4%af%e7%a9%8d%e5%92%8c)
-   [Dirichlet convolution. Part 1: Fast prefix sum computations by adamant - Codeforces](https://codeforces.com/blog/entry/117635)

[^piltz]: [Piltz divisor problem - Divisor summatory function - Wikipedia](https://en.wikipedia.org/wiki/Divisor_summatory_function#Piltz_divisor_problem)
