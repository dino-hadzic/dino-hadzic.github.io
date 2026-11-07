---
title: Exponential generating function
---

The exponential generating function (EGF) of a sequence $a$ is defined as the formal power series:

$$
\hat{F}(x)=\sum_{n}a_n \frac{x^n}{n!}
$$

## Basic operations

Addition and subtraction of exponential generating functions are the same as for ordinary generating functions: the corresponding coefficients are added.

Consider the multiplication of exponential generating functions. For two sequences $a,b$, let their exponential generating functions be $\hat{F}(x),\hat{G}(x)$; then

$$
\begin{aligned}
\hat{F}(x)\hat{G}(x)
&=\sum_{i\ge 0}a_i\frac{x^i}{i!}\sum_{j\ge 0}b_j\frac{x^j}{j!}\\
&=\sum_{n\ge 0}x^{n}\sum_{i=0}^na_ib_{n-i}\frac{1}{i!(n-i)!}\\
&=\sum_{n\ge 0}\frac{x^{n}}{n!}\sum_{i=0}^n\binom{n}{i}a_ib_{n-i}
\end{aligned}
$$

Therefore the sequence

$$
\left\langle \sum_{i=0}^n \binom{n}{i}a_ib_{n-i} \right\rangle
$$

has exponential generating function $\hat{F}(x)\hat{G}(x)$.

## Closed form

We likewise consider the closed form of exponential generating functions.

The exponential generating function of the sequence $\langle 1,1,1,\cdots\rangle$ is:

$$
\hat{F}(x) = \sum_{n \ge 0}\frac{x^n}{n!} = \mathrm{e}^x
$$

because the Taylor expansion of $\mathrm{e}^x$ at $x = 0$ gives exactly this infinite series.

Similarly, the exponential generating function of the geometric sequence $\langle 1,p,p^2,\cdots\rangle$ is:

$$
\hat{F}(x) = \sum_{n\ge 0}\frac{p^nx^n}{n!}=\mathrm{e}^{px}
$$

## Exponential and ordinary generating functions

How should we understand exponential generating functions? We defined the exponential generating function of a sequence $a$ as:

$$
F(x)=\sum_{n\ge 0}a_n\frac{x^n}{n!}
$$

But $F(x)$ is in fact also the ordinary generating function of the sequence $\left\langle \dfrac{a_n}{n!} \right\rangle$.

Both interpretations are perfectly fine. In other words, different generating functions are merely different ways of looking at a problem.

## Combinatorial meaning of polynomial exp in EGFs

If you have not yet learned polynomial exp, skip this part for now; this is a meaning derived from understanding exp, and in some sense it deepens the understanding of EGFs.

In an EGF, the $f$ in $f^n(x)$ is by default an EGF, so let us first consider the product of any two EGFs

$$
\hat{H}(x) = \hat{F}(x)\hat{G}(x) = \sum_{n\geq 0} \left[ \sum_{i = 0}^n\binom {n}{i}f_ig_{n-i} \right] \frac{x^n}{n!}
$$

The coefficient $[x^k]\hat{H}(x)$ obtained by multiplying two EGFs is in fact a convolution. If we consider $[x^k]\hat{H}(x)$ obtained by multiplying several EGFs, it is in fact the sum of the coefficients over all ways of choosing one term $x^{a_i}$ from each EGF such that $\sum_ia_i=k$.
From the viewpoint of sets, this is the number of ways to partition $n$ labeled elements into $k>0$ labeled sets.

> If $k=0$, the coefficient is obviously the product of the constant terms of the original EGFs, but certain requirements of polynomial $\exp$ force the constant term of the $f(x)$ in $\exp$ to be $0$; the concrete reasons are explained below.

In the definition of multinomial coefficients (see the combinatorial meaning of multinomial coefficients in the section on permutations and combinations) the sets are ordered by default, but in $\exp(f(x))$, for $f^k(x)$ the $k$ factors $f(x)$ multiplied together give the same EGF, while a set partition is obviously unordered, so the coefficient should be multiplied by $\dfrac{1}{k!}$.

Let $F_k(n)$ be the number of ways to partition $n$ labeled elements into $k$ nonempty unordered sets (nonemptiness is required because of $\exp$), and let $f_i$ be the number of certain combinatorial structures on a finite set of $i$ elements when those $i$ elements form one set (this is the original EGF; the way of counting the elements of this one set depends only on the size of the set). Then $F_k(n)$ is

$$
F_k(n)=\frac{n!}{k!}\sum_{\sum_{i}^ka_i=n}\prod_{j=1}^{k}\frac{f_{a_j}}{a_j!}
$$

Let the EGF of $f_n$ be $\hat{F}(x)$, that is:

$$
\hat{F}(x) = \sum_{n \geq 0} f_n\frac{x^n}{n!}
$$

Let the EGF of $F_k(n)$ be $G_k(x)$; then:

$$
\begin{aligned}
G_k(x)&=\sum_{n \geq 0} F_k(n)\frac{x^n}{n!}\\
&=\sum_{n \geq 0} x^n\frac{1}{k!}\sum_{\sum_i^k a_i=n}\prod_{j=1}^{k}\frac{f_{a_j}}{a_j!}\\
&=\frac{1}{k!}\sum_{n \geq 0}\sum_{\sum_i^k a_i=n}\prod_{j=1}^{k}\frac{f_{a_j}x^{a_j}}{a_j!}\\
&=\frac{1}{k!}\hat{F}^k(x)
\end{aligned}
$$

For all $k \geq 0$:

$$
\sum_{k \geq 0}G_k(x) = \sum_{k \geq 0}\frac{\hat{F}^k(x)}{k!} = \exp{\hat{F}(x)}
$$

Above we wrote down the relation directly from the combinatorial viewpoint; we can also prove the relation between $\exp(f(x))$ and $f(x)$ via a recurrence.

Again let $F_k(n)$ be the number of ways to partition $n$ labeled elements into $k$ nonempty (unlabeled) sets, let $g_i$ be the number of internal arrangements of a set of $i$ elements (same meaning as $f_i$ above), let $G(x)$ be the EGF of $\{g_i\}$, and let $H_k(x)$ be the EGF of $\{F_k(n)\}$.

Taking $i$ of the $n$ elements as one separately split-off set can be done in $g_i$ ways, and the remaining $n-i$ elements form $k-1$ sets in $F_{k-1}(n-i)$ ways. However, in the final partition every set of a given partition gets enumerated as the separately split-off set, so each partition is counted $k$ times and we still have to divide by $k$.

$$
\begin{aligned}
H_k(x) &= \sum_{n\ge 0}\cfrac{x^n}{n!}F_k(n)\\
&=\sum_{n\ge 0}\cfrac{x^n}{n!}\sum_{i=1}^{n-k+1}\binom n {i} F_{k-1}(n-i)\times g_i\times \cfrac{1}{k}\\
&=\cfrac{1}{k}\sum_{n\ge 0}\cfrac{x^n}{n!}\sum_{i=0}^{n}\binom n {i}F_{k-1}(n-i)\times g_i\\
&=\cfrac{1}{k}\cdot  H_{k-1}(x)G(x)
\end{aligned}
$$

The upper bound follows from the partition into nonempty sets: $n-(k-1)\geq i$ (each of the first $k-1$ sets has at least one element), but if the values $F_{k-1}(n-i)$ beyond the enumeration bound are set to $0$, nothing changes.

Having obtained the recurrence, we can expand it recursively; the base case is $k=1$, where $H_1(x)=G(x)$.

$$
\begin{aligned}
H_k(x) &= \cfrac{1}{k}\cdot   H_{k-1}(x)G(x)\\
&= \cfrac{1}{k}\cdot\cfrac{1}{k-1}\cdot   H_{k-2}(x)G^2(x)\\
&=\cdots \\
&= \cfrac{1}{k}\cdot\cfrac{1}{k-1} \cdots\cfrac{1}{2}\cdot H_{1}(x)G^{k-1}(x)\\
&= \cfrac{1}{k!}G^{k}(x)\\
\end{aligned}
$$

Likewise we have:

$$
\begin{aligned}
\sum_{k\ge 0}H_k(x)=\sum_{k\ge 0}\cfrac{G^k(x)}{k!}=\exp G(x)
\end{aligned}
$$

Obviously, **defining it as a partition into nonempty sets** ($g_0=0$) agrees with the intended meaning; if we **allowed the empty set** ($g_0=1$), then $[x^n]G^k$ would receive contributions from $[x^n]G^y,y>k$ (choosing the constant term in at least one $G$), there would be overcounting, and we would not obtain the desired quantity.

From the viewpoint of the recurrence, the product of several EGFs can also be seen as a knapsack-like combination (the process of merging two groups of counted objects).

In summary, the meaning of polynomial $\exp$ is: **the number of set families generated from a set of labeled elements**, or the total number of ways to partition the set into an arbitrary number of nonempty subsets.

## Permutations and circular permutations

The exponential generating function of the number of permutations of length $n$ is

$$
\hat{P}(x)=\sum_{n\ge 0}\frac{n!x^n}{n!}=\sum_{n\ge 0}x^n=\frac{1}{1-x}
$$

A circular permutation is defined as an arrangement of $1,2,\cdots,n$ in a circle; arrangements obtained by rotation are considered equivalent (but reflections are not considered equivalent).

The number of circular permutations of $n$ numbers is obviously $(n-1)!$. Therefore the exponential generating function of the number of circular permutations of $n$ numbers is

$$
\hat{Q}(x)=\sum_{n\ge 1}\frac{(n-1)!x^n}{n!}=\sum_{n\ge 1}\frac{x^n}{n}=-\ln(1-x)=\ln\left( \frac{1}{1-x} \right)
$$

That is, $\exp \hat{Q}(x)=\hat{P}(x)$. But this is only a mathematical derivation. How can we understand intuitively that the $\exp$ of the EGF of circular permutations is the EGF of permutations?

A permutation consists of several cycles. For example, $p=[4,3,2,5,1]$ has two cycles:

![](./images/p1.png)

(that is, we draw a directed edge from $p_i$ to $i$)

Different cycles lead to different permutations. For example, if we change the second cycle to

![](./images/p2.png)

then the corresponding permutation is $[5,3,2,1,4]$.

In other words, the number of permutations of length $n$ is the number of ways to

1.  partition $1,2,\cdots,n$ into several sets
2.  form a cycle from each set.

And the number of ways for the numbers of one set to form a cycle is obviously the number of circular permutations of the size of that set. Therefore the number of permutations of length $n$ is: partition $1,2,\cdots,n$ into several sets and take the product of the numbers of circular permutations of the sets.

This is the intuitive understanding of polynomial $\exp$.

Generalizing:

-   If the EGF of the number of **labeled** spanning trees on $n$ vertices is $\hat{F}(x)$, then the EGF of the number of **labeled** spanning forests on $n$ vertices is $\exp \hat{F}(x)$; intuitively, partition the $n$ vertices into several sets and take the product of the numbers of ways for each set to form a spanning tree.
-   If the EGF of the number of labeled connected undirected graphs on $n$ vertices is $\hat{F}(x)$, then the EGF of the number of labeled undirected graphs on $n$ vertices is $\exp \hat{F}(x)$, and the latter is easy to compute:

    $$
    \exp \hat{F}(x)=\sum_{n\ge 0}2^{\binom{n}{2}}\frac{x^n}{n!}
    $$

    Therefore, to compute the former, a single polynomial $\ln$ suffices.

Next let us look at some applications of exponential generating functions.

## Applications

### Derangement numbers

???+ note "Derangement numbers"
    A derangement of length $n$ is defined as a permutation satisfying $p_i\ne i$.
    
    Find the exponential generating function of the derangement numbers.

From the viewpoint of cycles, a derangement is a permutation whose cycles contain no self-loops, i.e., no cycle of length $1$. The exponential generating function of the latter is

$$
\sum_{n\ge 2}\frac{x^n}{n}=-\ln\left(1-x\right)-x
$$

so the exponential generating function of the derangement numbers is $\exp(-\ln(1-x)-x)$.

### 不动点 (Fixed point)

???+ note "[不动点 (Fixed point)](https://www.51nod.com/Html/Challenge/Problem.html#problemId=1728)"
    Problem: find the number of maps $f:\{1,2,\cdots,n\}\to \{1,2,\cdots,n\}$ such that
    
    $$
    \underbrace{f\circ f\circ\cdots\circ f}_{k}=\underbrace{f\circ f\circ\cdots\circ f}_{k-1}
    $$
    
    $nk\le 2\times 10^6,1\le k\le 3$.

Draw an edge from $i$ to $f(i)$. The condition means that from any $i$, walking $k$ steps and walking $k-1$ steps reach the same vertex. In other words, the cycle of every unicyclic tree (pseudotree) is a self-loop and the depth does not exceed $k$ (the root has depth $1$). Such a pseudotree can be treated as a rooted tree. So our problem becomes: count the forests of rooted trees on $n$ labeled vertices with depth at most $k$.

Consider rooted trees on $n$ labeled vertices with depth at most $k$, and suppose their generating function is:

$$
\hat{F_k}(x)=\sum_{n\ge 0}f_{n,k}\frac{x^n}{n!}
$$

We compute $\hat{F_k}(x)$ recursively. A rooted tree of depth at most $k$ is in fact several rooted trees of depth at most $k-1$ whose roots are all attached to one vertex. Therefore

$$
\hat{F_k}(x)=x\exp \hat{F}_{k-1}(x)
$$

Then the exponential generating function of the answer is $\exp \hat{F}_k(x)$; we just need its $n$-th term.

### Lust

???+ note "[Lust](https://codeforces.com/contest/891/problem/E)"
    You are given a sequence of $n$ numbers $a_1,a_2,\cdots,a_n$ and a variable $s$ with initial value $0$. You must repeat the following operation $k$ times:
    
    -   Choose $x$ uniformly at random from $1,2,\cdots,n$.
    -   Add $\prod_{i\ne x}a_i$ to $s$.
    -   Decrease $a_x$ by one.
    
    Find the expected value of $s$ after $k$ operations.
    
    $1\le n\le 5000,1\le k\le 10^9,0\le a_i\le 10^9$.

Suppose that after $k$ operations $a_i$ has decreased by $b_i$; then in fact

$$
s=\prod_{i=1}^n a_i-\prod_{i=1}^n(a_i- b_i)
$$

so our problem actually becomes finding the expected value of $\prod_{i=1}^n (a_i- b_i)$ after $k$ operations.

Let us compute the sum of $\prod_{i=1}^n (a_i- b_i)$ over all outcomes and divide by $n^k$ at the end.

The number of sequences of $k$ operations in which $i$ appears $b_i$ times is

$$
\frac{k!}{b_1!b_2!\cdots b_n!}
$$

which resembles the coefficients in the multiplication of exponential generating functions.

Let the exponential generating function for $a_j$ be

$$
F_j(x)=\sum_{i\ge 0}(a_j-i)\frac{x^i}{i!}
$$

Then the answer is

$$
[x^k]\prod_{j=1}^nF_j(x)
$$

To compute the answer quickly, we convert $F_j(x)$ into closed form:

$$
\begin{aligned}
F_j(x)&=\sum_{i\ge 0}a_j\frac{x^i}{i!}-\sum_{i\ge 1}\frac{x^i}{(i-1)!}\\
&=a_j\mathrm{e}^x-x\mathrm{e}^x\\
&=(a_j-x)\mathrm{e}^x
\end{aligned}
$$

Therefore we get

$$
\prod_{j=1}^nF_j(x)=\mathrm{e}^{nx}\prod_{j=1}^n(a_j-x)
$$

where $\prod_{j=1}^n(a_j-x)$ is a polynomial of degree $n$ that can be computed by brute force. Suppose its expansion is $\sum_{i=0}^nc_ix^i$; then

$$
\begin{aligned}
\prod_{j=1}^nF_j(x)
&=\left(\sum_{i\ge 0} \frac{n^ix^i}{i!}\right)\left(\sum_{i=0}^nc_ix^i\right)\\
&=\sum_{i\ge 0}\sum_{j=0}^i c_jx^j\frac{n^{i-j}x^{i-j}}{(i-j)!}\\
&=\sum_{i\ge 0}\frac{x^{i}}{i!}\sum_{j=0}^i n^{i-j}i^{\underline{j}}c_j
\end{aligned}
$$

It suffices to compute the coefficient of $x^k$ in this polynomial.
