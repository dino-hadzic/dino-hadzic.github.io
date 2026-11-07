---
title: Vandermonde's identity
---

## Introduction

Vandermonde's convolution (Vandermonde's identity) is a formula for merging binomial coefficients; it is mainly used when deriving formulas in combinatorics.

## Vandermonde's convolution formula

$$
\sum_{i=0}^k\binom{n}{i}\binom{m}{k-i}=\binom{n+m}{k}
$$

### Proof

Let us prove it using the binomial theorem:

$$
\begin{aligned}
\sum_{k=0}^{n+m}\binom{n+m}{k}x^k&=(x+1)^{n+m}\\
&=(x+1)^n(x+1)^m\\
&=\sum_{r=0}^n\binom{n}{r}x^r\sum_{s=0}^m\binom{m}{s}x^s\\
&=\sum_{k=0}^{n+m}\sum_{r=0}^k\binom{n}{r}\binom{m}{k-r}x^k\\
\end{aligned}
$$

Hence:

$$
\binom{n+m}{k}=\sum_{r=0}^k\binom{n}{r}\binom{m}{k-r}
$$

Let us also consider a proof via the combinatorial meaning:

Choosing $k$ numbers from a set of size $n+m$ can be viewed as splitting the set of size $n+m$ into two sets, of sizes $n$ and $m$, and then counting the ways to take $i$ numbers from the set of size $n$ and $k-i$ numbers from the set of size $m$. Since we enumerate over all values of $i$, it suffices to consider only one split, because different splits are equivalent to each other.

## Corollaries

### Corollary 1 and proof

$$
\sum_{i=-r}^{s}\binom{n}{r+i}\binom{m}{s-i}=\binom{n+m}{r+s}
$$

The proof is similar to the proof of the original formula.

### Corollary 2 and proof

$$
\sum_{i=1}^n\binom{n}{i}\binom{n}{i-1}=\binom{2n}{n-1}
$$

Deriving from basic combinatorics, we have:

$$
\sum_{i=1}^n\binom{n}{i}\binom{n}{i-1}=\sum_{i=0}^{n-1}\binom{n}{i+1}\binom{n}{i}=\sum_{i=0}^{n-1}\binom{n}{n-1-i}\binom{n}{i}=\binom{2n}{n-1}
$$

### Corollary 3 and proof

$$
\sum_{i=0}^n\binom{n}{i}^2=\binom{2n}{n}
$$

Deriving from basic combinatorics, we have:

$$
\sum_{i=0}^n\binom{n}{i}^2=\sum_{i=0}^n\binom{n}{i}\binom{n}{n-i}=\binom{2n}{n}
$$

### Corollary 4 and proof

$$
\sum_{i=0}^m\binom{n}{i}\binom{m}{i}=\binom{n+m}{m}
$$

Deriving from basic combinatorics, we have:

$$
\sum_{i=0}^m\binom{n}{i}\binom{m}{i}=\sum_{i=0}^m\binom{n}{i}\binom{m}{m-i}=\binom{n+m}{m}
$$

Here $\binom{n+m}{m}$ is the familiar number of ways in grid path counting. So we can also consider a proof via its combinatorial meaning.

In a grid, going from $(0,0)$ to $(n,m)$ takes $n+m$ steps in total. Let $(0,0)$ be the top-left corner of the grid; then $n$ of the steps go down and $m$ of the steps go right, so the number of ways is $\binom{n+m}{m}$.

From a different point of view, we split the $n+m$ steps into two parts: first take $n$ steps, then take $m$ steps. If $i$ of the first $n$ steps go right, then $m-i$ of the remaining $m$ steps go right, which proves the claim.

## Exercises

-   [CF785D Anton and School - 2](https://codeforces.com/problemset/problem/785/D)

-   [Luogu P2791 幼儿园篮球题 (Kindergarten Basketball Problem)](https://www.luogu.com.cn/problem/P2791)

## References and notes

1.  [Vandermonde's Convolution Formula](https://www.cut-the-knot.org/arithmetic/algebra/VandermondeConvolution.shtml)
