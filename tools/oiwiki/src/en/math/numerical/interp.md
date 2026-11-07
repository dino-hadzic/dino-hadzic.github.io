---
title: Interpolation
---

## Introduction

Interpolation is a method of estimating new data points within a certain range from known, discrete data points. Interpolation is often used in function fitting.

For example, for the data points:

| $x$    | $0$ | $1$      | $2$      | $3$      | $4$       | $5$       | $6$       |
| ------ | --- | -------- | -------- | -------- | --------- | --------- | --------- |
| $f(x)$ | $0$ | $0.8415$ | $0.9093$ | $0.1411$ | $-0.7568$ | $-0.9589$ | $-0.2794$ |

![](../images/interp-1.svg)

where $f(x)$ is unknown, interpolation can estimate the unknown data points by fitting $f(x)$ in some prescribed form.

For example, we can fit $f(x)$ with a piecewise linear function:

![](../images/interp-2.svg)

This kind of interpolation is called [linear interpolation](https://en.wikipedia.org/wiki/Linear_interpolation).

We can also fit $f(x)$ with a polynomial:

![](../images/interp-3.svg)

This kind of interpolation is called [polynomial interpolation](https://en.wikipedia.org/wiki/Polynomial_interpolation).

The general form of polynomial interpolation is as follows:

???+ note "Polynomial interpolation"
    Given $n+1$ known points $(x_0,y_0),(x_1,y_1),\dots,(x_n,y_n)$, find a polynomial of the form $f(x)=\sum_{i=0}^n a_ix^i$ satisfying
    
    $$
    f(x_i)=y_i,\qquad\forall i=0,1,\dots,n
    $$
    
    that is, the polynomial $f(x)$.

Below we introduce two ways of doing polynomial interpolation: Lagrange interpolation and Newton interpolation. It is not hard to prove that the two methods give equal results.

## Lagrange interpolation

We need to construct a function $f(x)$ passing through the points $P_1(x_1, y_1), P_2(x_2,y_2),\cdots,P_n(x_n,y_n)$. First, let the projection of the $i$-th point onto the $x$-axis be $P_i^{\prime}(x_i,0)$.

Consider constructing $n$ functions $f_1(x), f_2(x), \cdots, f_n(x)$ such that the graph of the $i$-th function $f_i(x)$ passes through $\begin{cases}P_j^{\prime}(x_j,0),(j\neq i)\\P_i(x_i,y_i)\end{cases}$; then the required function is $f(x)=\sum\limits_{i=1}^nf_i(x)$.

We can set $f_i(x)=a\cdot\prod_{j\neq i}(x-x_j)$; substituting the point $P_i(x_i,y_i)$ gives $a=\dfrac{y_i}{\prod_{j\neq i} (x_i-x_j)}$, so

$$
f_i(x)=y_i\cdot\dfrac{\prod_{j\neq i} (x-x_j)}{\prod_{j\neq i} (x_i-x_j)}=y_i\cdot\prod_{j\neq i}\dfrac{x-x_j}{x_i-x_j}
$$

Thus we obtain the form of Lagrange interpolation:

$$
f(x)=\sum_{i=1}^ny_i\cdot\prod_{j\neq i}\dfrac{x-x_j}{x_i-x_j}
$$

The time complexity of the naive implementation is $O(n^2)$; it can be optimized to $O(n\log^2 n)$, see [fast polynomial interpolation](../poly/multipoint-eval-interpolation.md#fast-polynomial-interpolation).

???+ note "[Luogu P4781【模板】拉格朗日插值 (Template: Lagrange interpolation)](https://www.luogu.com.cn/problem/P4781)"
    Given $n$ point pairs $(x_i,y_i)$ and $k$, where $\forall i,j$ we have $i\neq j \iff x_i\neq x_j$, and $f(x_i)\equiv y_i\pmod{998244353}$ and $\deg(f(x)) < n$ (define $\deg(0)=-\infty$), compute $f(k)\bmod{998244353}$.
    
    ??? note "Solution"
        In this problem only the value $f(k)$ is needed, so we can substitute $k$ directly while computing the expression above; sometimes, however, several evaluations or more complex operations are needed, in which case the coefficients of $f$ must be found. The code gives an implementation that computes the coefficients.
        
        $$
        f(k)=\sum_{i=1}^{n}y_i\prod_{j\neq i }\frac{k-x_j}{x_i-x_j}
        $$
        
        In this problem we also need to compute inverses. If we first compute the numerator and denominator separately, then multiply the numerator by the inverse of the denominator and add it to the final answer, the bottleneck of the time complexity will not be computing inverses, and the time complexity is $O(n^2)$.
        
        Since we work under the fixed modulus $998244353$, we tentatively regard the time complexity of computing a multiplicative inverse as constant here.
    
    ??? note "Implementation"
        ```cpp
        --8<-- "docs/math/code/numerical/interp/interp_1.cpp"
        ```

### Lagrange interpolation with consecutive integer abscissas

If the abscissas of the known points are consecutive integers, we can interpolate in $O(n)$.

Let the required polynomial be $f(x)$, and suppose we know $f(1),\cdots,f(n+1)$ ($1\le i\le n+1$); substitute into the interpolation formula above:

$$
\begin{aligned}
f(x)&=\sum\limits_{i=1}^{n+1}y_i\prod\limits_{j\ne i}\frac{x-x_j}{x_i-x_j}\\
&=\sum\limits_{i=1}^{n+1}y_i\prod\limits_{j\ne i}\frac{x-j}{i-j}
\end{aligned}
$$

In the product at the end, the numerator and denominator can be considered separately; it is easy to see that the numerator is:

$$
\dfrac{\prod\limits_{j=1}^{n+1}(x-j)}{x-i}
$$

The product of $i-j$ in the denominator can be split into two factorials:

$$
(-1)^{n+1-i}\cdot(i-1)!\cdot(n+1-i)!
$$

Thus the interpolation formula for abscissas $1,\cdots,n+1$ is:

$$
f(x)=\sum\limits_{i=1}^{n+1}(-1)^{n+1-i}y_i\cdot\frac{\prod\limits_{j=1}^{n+1}(x-j)}{(i-1)!(n+1-i)!(x-i)}
$$

Precompute the prefix and suffix products of $(x-i)$, the factorials and the inverse factorials, then substitute into this formula; the complexity is $O(n)$.

???+ note "Example problem [CF622F The Sum of the k-th Powers](https://codeforces.com/contest/622/problem/F)"
    Given $n,k$, compute $\sum\limits_{i=1}^ni^k$ modulo $10^9+7$.
    
    ??? note "Solution"
        In this problem the answer is a polynomial of degree $k+1$, so we can compute the values $1^i,\cdots,(k+2)^i$ with a linear sieve and then interpolate in $O(n)$.
        
        One can also derive the following expression from the formula of the method of differences using combinatorics:
        
        $$
        f(x)=\sum_{i=1}^{n+1}\binom{x-1}{i-1}\sum_{j=1}^{i}(-1)^{i+j}\binom{i-1}{j-1}y_{j}=\sum\limits_{i=1}^{n+1}y_i\cdot\frac{\prod\limits_{j=1}^{n+1}(x-j)}{(x-i)\cdot(-1)^{n+1-i}\cdot(i-1)!\cdot(n+1-i)!}
        $$
    
    ??? note "Implementation"
        ```cpp
        --8<-- "docs/math/code/numerical/interp/interp_2.cpp"
        ```

## Newton interpolation

Newton interpolation is an interpolation method based on higher-order differences; its advantage is that it supports inserting a new data point in $O(n)$.

To achieve $O(n)$ insertion of a new data point, we set:

$$
f(x)=\sum_{j=0}^n a_jn_j(x)
$$

where $n_j(x):=\prod_{i=0}^{j-1}(x-x_i)$ is called the **Newton basis**.

If we solve for $a_j$, we obtain the interpolation polynomial $f(x)$. We define the **forward divided differences** as follows:

$$
\begin{aligned}
    \lbrack y_k\rbrack  & := y_k,                                                                & k=0,\dots,n, \\
    [y_k,\dots,y_{k+j}] & := \dfrac{[y_{k+1},\dots,y_{k+j}]-[y_k,\dots,y_{k+j-1}]}{x_{k+j}-x_k}, & k=0,\dots,n-j,~j=1,\dots,n.
\end{aligned}
$$

Then:

$$
\begin{aligned}
    f(x)&=[y_0]+[y_0,y_1](x-x_0)+\dots+[y_0,\dots,y_n](x-x_0)\dots(x-x_{n-1})\\
    &=\sum_{j=0}^n [y_0,\dots,y_j]n_j(x)
\end{aligned}
$$

This is the form of Newton interpolation. The time complexity of the naive implementation is $O(n^2)$.

If the sample points are equally spaced (i.e. $x_i=x_0+ih$, $i=1,\dots,n$), we can derive

$$
[y_k,\dots,y_{k+j}]=\frac{1}{j!h^j}\Delta^{(j)}y_k,
$$

where $\Delta^{(j)}y_k$ are the **forward differences**, defined as follows:

$$
\begin{aligned}
    \Delta^{(0)}y_k & := y_k,                                       & k=0,\dots,n, \\
    \Delta^{(j)}y_k & := \Delta^{(j-1)} y_{k+1}-\Delta^{(j-1)} y_k, & k=0,\dots,n-j,~j=1,\dots,n.
\end{aligned}
$$

Setting $x=x_0+sh$, the Newton interpolation formula becomes

$$
f(x)=\sum_{j=0}^n \binom{s}{j}j!h^j[y_0,\dots,y_j]=\sum_{j=0}^n \binom{s}{j}\Delta^{(j)}y_0.
$$

??? note "Implementation ([Luogu P4781【模板】拉格朗日插值 (Template: Lagrange interpolation)](https://www.luogu.com.cn/problem/P4781))"
    ```cpp
    --8<-- "docs/math/code/numerical/interp/interp_3.cpp"
    ```

### Newton interpolation with consecutive integer abscissas

For example: find the coefficients of the polynomial $f(x)=\sum_{i=0}^{3} a_ix^i$, given that the values $f(1)$ through $f(6)$ are $1, 5, 14, 30, 55, 91$ respectively.

$$
\begin{array}{cccccccccccc}
1 &    &  5 &    & 14 &    & 30 &    & 55 &    & 91 & \\
&  4 &    &  9 &    & 16 &    & 25  &    & 36 & \\
&    &  5 &    &  7 &    &  9 &    &  11 & \\
&    &    &  2 &    &  2 &    &  2 & \\
\end{array}
$$

The first row consists of the first $n$ consecutive values of $f(x)$; each subsequent row consists of the differences of corresponding adjacent pairs of terms in the previous row. Observe that if this operation is performed enough times (provided $f(x)$ is a polynomial), eventually a constant value is always obtained.

We compute that the first term of the $i-1$-th order differences is $\sum_{j=1}^{i}(-1)^{i+j}\binom{i-1}{j-1}f(j)$, and the first term of the $i-1$-th order differences contributes to $f(k)$ $\binom{k-1}{i-1}$ times.

$$
f(k)=\sum_{i=1}^n\binom{k-1}{i-1}\sum_{j=1}^{i}(-1)^{i+j}\binom{i-1}{j-1}f(j)
$$

The time complexity is $O(n^2)$.

## Implementation in C++

Since C++20, the standard library has added the functions [`std::midpoint`](https://en.cppreference.com/w/cpp/numeric/midpoint) and [`std::lerp`](https://en.cppreference.com/w/cpp/numeric/lerp), used for computing the midpoint and for linear interpolation, respectively.

## Exercises

-   [“NOIP2020” 微信步数 (WeChat Steps)](https://loj.ac/p/3389)
-   [“联合省选 2022” 填树 (Joint Provincial Selection 2022: Filling the Tree)](https://loj.ac/p/3701)
-   [“NOI2019” 机器人 (Robot)](https://loj.ac/p/3157)

## References

1.  [Interpolation - Wikipedia](https://en.wikipedia.org/wiki/Interpolation)
2.  [Newton polynomial - Wikipedia](https://en.wikipedia.org/wiki/Newton_polynomial)
