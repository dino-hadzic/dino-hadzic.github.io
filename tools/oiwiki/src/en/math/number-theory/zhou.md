---
title: Zhou's sieve
---

## Prerequisites

-   [Multiplicative functions](./basic.md#multiplicative-functions)

## Definition

Zhou's sieve (洲阁筛) is a sieve method that can compute the prefix sums of most multiplicative functions in sublinear time complexity.

Below we explain the principle of Zhou's sieve in detail, using the computation of $\displaystyle\sum_{i=1}^nf(i)$ as an example.

## Notation

-   $\mathbb P$ denotes the set of primes, and $p_i$ denotes the $i$-th prime.
-   $m$ denotes the number of primes not exceeding $\sqrt n$.

## Requirements

For $p\in\mathbb P,c\in\mathbb N$, the value $f(p^c)$ is a low-degree polynomial in $p$.

## Idea

-   Every integer in $[1,n]$ has at most one prime factor $>\sqrt n$.
-   We use the property that $\left\lfloor\dfrac ni\right\rfloor(i\in[1,n]\cap\mathbb N)$ takes only about $\sqrt n$ distinct values to reduce the time complexity.

## Procedure

Split all integers in $[1,n]$ into two classes according to whether they have a prime factor $>\sqrt n$:

$$
\sum_{i=1}^nf(i)=\sum_{i=1}^n\left[\exists d\in(\sqrt n,n]\cap\mathbb P,d\mid i\right]f(i)+\sum_{i=1}^n\left[\forall d\in(\sqrt n,n]\cap\mathbb P,d\nmid i\right]f(i)
$$

For the first part, we enumerate the largest factor and, by the properties of multiplicative functions, transform it:

$$
\sum_{i=1}^nf(i)=\sum_{i=1}^{\sqrt n}f(i)\cdot\left(\sum_{d=\lfloor\sqrt n\rfloor+1}^{\lfloor\frac ni\rfloor}[d\in\mathbb P]f(d)\right)+\sum_{i=1}^n\left[\forall d\in(\sqrt n,n]\cap\mathbb P,d\nmid i\right]f(i)
$$

The first and second parts can be computed separately.

### Part 1

> Compute $\displaystyle\sum_{i=1}^{\sqrt n}f(i)\cdot\left(\sum_{d=\lfloor\sqrt n\rfloor+1}^{\lfloor\frac ni\rfloor}[d\in\mathbb P]f(d)\right)$.

We enumerate $i$ and then compute the part in parentheses in $O(1)$.

Let $\displaystyle g(t,l)=\sum_{i=1}^l[\forall j\in[1,t],\gcd(i,p_j)=1]f(i)$, i.e., the sum of the $f$ values of all numbers in $[1,l]$ that are coprime to each of $p_1,p_2,\dots,p_t$.

The computation of Part 1 thus becomes $\displaystyle\sum_{i=1}^{\sqrt n}f(i)\cdot g\left(m,\left\lfloor\frac ni\right\rfloor\right)$.

The boundary is $g(0,l)=\sum_{i=1}^lf(i)$, and the transition is $g(t,l)=g(t-1,l)-f(p_t)\cdot g\left(t-1,\left\lfloor\frac l{p_t}\right\rfloor\right)$.

$l$ takes about $\sqrt n$ distinct values, and for each of them we need to enumerate the primes, so the complexity is $\displaystyle O\left(\frac{\sqrt n}{\ln\sqrt n}\cdot\sqrt n\right)= O\left(\frac n{\log n}\right)$, which needs optimization.

Note that when $p_{t+1}^2>l$, the only number satisfying the condition is $1$, so in this case $g(t,l)=f(1)=1$.

Substituting into the recurrence we get: when $p_t^2>l$, $g(t,l)=g(t-1,l)-f(p_t)$.

Therefore, as soon as we find $p_t^2>l$ we stop the transitions; denote this $t$ by $t_l$, then $\forall t>t_l,g(t,l)=g(t_l,l)-\sum_{i=t_l}^{t-1}f(p_i)$.

By precomputing the prefix sums of the $f$ values at primes we can compute $g$ quickly, and the time complexity is optimized to $O\left(\dfrac{n^{\frac34}}{\log n}\right)$.

### Part 2

> Compute $\displaystyle\sum_{i=1}^n\left[\forall d\in(\sqrt n,n]\cap\mathbb P,d\nmid i\right]f(i)$.

Let $\displaystyle h(t,l)=\sum_{i=1}^l\left[i=\prod_{j=t}^mp_j^{c_j},c_j\in\mathbb N\right]f(i)$, i.e., the sum of the $f$ values of all numbers in $[1,l]$ that contain only the prime factors $p_t,p_{t+1},\dots,p_m$.

Part 2 is exactly $h(0,n)$.

The boundary is $h(m+1,l)=1$, and the transition is $\displaystyle h(t,l)=h(t+1,l)+\sum_{c\in\mathbb N^*}f(p_t^c)\cdot h\left(t+1,\left\lfloor\frac l{p_t^c}\right\rfloor\right)$.

$l$ takes about $\sqrt n$ distinct values, so the complexity of direct transitions is $\displaystyle O\left(\sqrt n\cdot\frac{\sqrt n}{\ln\sqrt n}\right)= O\left(\frac n{\log n}\right)$, which needs optimization.

Similarly to the optimization of $g$, note that when $p_t>l$, the only number that can be formed from $p_t,p_{t+1},\dots,p_m$ is $1$, so in this case $h(t,l)=f(1)=1$.

Analogously, we derive $\forall p_t^2>l,h(t,l)=h(t+1,l)+f(p_t)$.

Therefore, as soon as we find $p_t^2>l$ we stop the transitions; denote this $t$ by $t_l$, and whenever $h$ is needed later, add $\displaystyle\sum_{i=p_{t_l}}^{\min(l,\sqrt n)}[i\in\mathbb P]f(i)$ to the current value of $h$.

The time complexity is optimized to $O\left(\dfrac{n^{\frac34}}{\log n}\right)$.

### Summation

Having computed the answers of Part 1 and Part 2, their sum is exactly $\displaystyle\sum_{i=1}^nf(i)$.

## References

[积性函数线性筛/杜教筛/洲阁筛学习笔记 (Notes on the linear sieve, Du's sieve and Zhou's sieve for multiplicative functions) | Bill Yang's Blog](https://blog.bill.moe/multiplicative-function-sieves-notes)
