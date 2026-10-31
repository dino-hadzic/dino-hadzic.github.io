---
title: Derangements
---

## Derangements

### Definition

A derangement is a permutation in which no element appears in its natural position. That is, if a permutation $P$ of $1\sim n$ satisfies $P_i\neq i$, then $P$ is called a derangement of $n$.

For example, the derangements of three elements are $\{2,3,1\}$ and $\{3,1,2\}$. The derangements of four elements are $\{2,1,4,3\}$, $\{2,3,4,1\}$, $\{2,4,1,3\}$, $\{3,1,4,2\}$, $\{3,4,1,2\}$, $\{3,4,2,1\}$, $\{4,1,2,3\}$, $\{4,3,1,2\}$ and $\{4,3,2,1\}$. A derangement is a permutation without fixed points, i.e. without cycles of length 1.

### Computation by inclusion–exclusion

The universal set $U$ is the set of permutations of $1\sim n$, $|U|=n!$; let $S_i$ be the set of those permutations satisfying $P_i\neq i$. Using complements and the [inclusion–exclusion principle](./inclusion-exclusion-principle.md), the problem becomes computing:

$$
\begin{aligned}
\left|\bigcap_{i=1}^n S_i\right|
&=|U|-\left|\bigcup_{i=1}^n\overline{S_i}\right|\\
&=n!-\sum_{k=1}^n(-1)^{k-1}\sum_{a_i<a_{i+1}}\left|\bigcap_{i=1}^{k}\overline{S_{a_i}}\right|
\end{aligned}
$$

Here the sum means choosing $a_1, a_2, \cdots, a_k$ from $1, 2, \cdots, n$ such that $a_i<a_{i+1}$. Then

$$
\left|\bigcap_{i=1}^{k}\overline{S_{a_i}}\right|
$$

denotes the number of permutations in which the $k$ numbers $a_1,a_2,\cdots,a_k$ satisfy $P_{a_i}=a_i$ while the positions of the remaining $n-k$ numbers are arbitrary, hence:

$$
\left|\bigcap_{i=1}^{k}\overline{S_{a_i}}\right|=(n-k)!
$$

There are $\dbinom{n}{k}$ ways to choose these $k$ numbers, and summing over them gives:

$$
\begin{aligned}
&\sum_{k=1}^n(-1)^{k-1}\sum_{a_i<a_{i+1}}\left|\bigcap_{i=1}^{k}\overline{S_{a_i}}\right|\\
=&\sum_{k=1}^n(-1)^{k-1}\dbinom{n}{k}(n-k)!\\
=&\sum_{k=1}^n(-1)^{k-1}\frac{n!}{k!}\\
=&n!\sum_{k=1}^n\frac{(-1)^{k-1} }{k!}
\end{aligned}
$$

Therefore the number of derangements of $n$ elements is:

$$
D_n=n!-n!\sum_{k=1}^n\frac{(-1)^{k-1} }{k!}=n!\sum_{k=0}^n\frac{(-1)^k}{k!}
$$

The first few terms of the sequence of derangement numbers are $0,1,2,9,44,265$ ([OEIS A000166](http://oeis.org/A000166)).

### Computation by recurrence

Let us make the derangement problem concrete and consider the following problem:

There are $n$ different letters, numbered $1,2,3,4,5$, and these five letters are to be put into envelopes numbered $1,2,3,4,5$ such that the number of the envelope differs from the number of the letter. How many different placements are there?

Suppose we have reached the $n$-th envelope; initially we temporarily put the $n$-th letter into the $n$-th envelope, and then consider the recurrence in two cases:

-   the first $n-1$ envelopes are all filled wrongly;
-   among the first $n-1$ envelopes exactly one is filled correctly and all the others wrongly.

In the first case, where the first $n-1$ envelopes are all filled wrongly: since the first $n-1$ are already all wrong, the $n$-th letter only needs to be swapped with any one of the previous positions, which gives $D_{n-1}\times (n-1)$ possibilities in total.

In the second case, where exactly one of the first $n-1$ envelopes is filled correctly and the rest wrongly: the point of considering this case is that if one of the $n-1$ envelopes is filled correctly, then swapping that correct one with the $n$-th yields a derangement.

From the other cases it is impossible to obtain a derangement of length $n$ with a single operation.

It follows that the derangement numbers satisfy the recurrence relation:

$$
D_n=(n-1)(D_{n-1}+D_{n-2})
$$

Here is another recurrence relation as well:

$$
D_n=nD_{n-1}+{(-1)}^n
$$

### Other relations

The derangement numbers have a simple rounding expression, and their growth rate differs from the factorial only by a constant:

$$
D_n=\left\lfloor\frac{n!}{\mathrm{e}} + \frac{1}{2}\right\rfloor
$$

As the number of elements increases, the probability P of forming a derangement approaches:

$$
P=\lim_{n\to\infty}\frac{D_n}{n!}=\frac{1}{\mathrm{e}}
$$
