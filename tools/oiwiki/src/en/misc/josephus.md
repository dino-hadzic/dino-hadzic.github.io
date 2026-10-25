---
title: Josephus problem
---

The Josephus problem has a long history, and the methods for solving it keep improving; however, there is still no extremely efficient algorithm (within logarithmic complexity) that solves it.

## Problem statement

> There are n people labeled $0,1,\cdots, n-1$. They stand in a circle counterclockwise; starting from person $0$, each time we count $k$ people counterclockwise from the current person, and that person is eliminated. The question is who remains last.

This classic problem was posed by Josephus in the 1st century AD, although he only considered the case $k=2$ at that time. Nowadays we can solve it with many efficient algorithms.

## Procedure

### Naive algorithm

The most naive algorithm is, of course, direct simulation. Simulate the elimination process with a circular linked list, repeat it $n-1$ times, and we get the answer. The complexity is $\Theta (n^2)$.

### Simple optimization

Finding the next person can be optimized with a segment tree. Concretely, build a segment tree over $0,1,\cdots, n-1$ and store the number of remaining people in each interval. Finding the position of the current person and the $k$-th person after them can then be done by binary search on the segment tree.

### Linear algorithm

Let $J_{n,k}$ denote the answer to the Josephus problem with parameters $n,k$. We have the following recurrence

$$
J_{n,k}=(J_{n-1,k}+k)\bmod n
$$

It is also easy to derive. We start from $0$ and count $k$ people; after person $k-1$ is eliminated, $n-1$ people remain. Once we compute the answer for these $n-1$ people, we add a relative offset of $k$ to obtain the real answer. The complexity of this algorithm is obviously $\Theta (n)$.

???+ note "Implementation"
    ```cpp
    int josephus(int n, int k) {
      int res = 0;
      for (int i = 1; i <= n; ++i) res = (res + k) % i;
      return res;
    }
    ```

### Logarithmic algorithm

For the case where $k$ is small and $n$ is large, there is also an algorithm with complexity $\Theta (k\log n)$.

Since each time we count $k$ people and eliminate one, within one round we can eliminate $\left\lfloor\frac{n}{k}\right\rfloor$ people, after which $n-\left\lfloor\frac{n}{k}\right\rfloor$ people remain. At that moment we are at the position of the $\left\lfloor\frac{n}{k}\right\rfloor\cdot k$-th person, and you can notice that this equals $n-n\bmod k$. So we continue recursively, and after the computation we restore the relative position. Restoring the relative position is based on the following: each elimination removes the $k$-th person counted, and their labels are inherited one by one by the people after them; in other words, when computing with a circle of $n-\left\lfloor\frac{n}{k}\right\rfloor$ people, for every $k$ people the position of $1$ person is not accounted for. Therefore, when the result is less than $0$, we take it modulo $n$ in the circle of $n$ people from which the labels that are multiples of $k$ have not yet been removed; when the result is greater than or equal to $0$, we can directly multiply it by $\frac{k}{k-1}$. This gives the following algorithm:

???+ note "Implementation"
    ```cpp
    int josephus(int n, int k) {
      if (n == 1) return 0;
      if (k == 1) return n - 1;
      if (k > n) return (josephus(n - 1, k) + k) % n;  // linear algorithm
      int res = josephus(n - n / k, k);
      res -= n % k;
      if (res < 0)
        res += n;  // mod n
      else
        res += res / (k - 1);  // restore position
      return res;
    }
    ```

It can be proven that the complexity of this algorithm is $\Theta (k\log n)$. Let the number of recursive calls be $x$; then at each step the problem size roughly becomes $\displaystyle n\left(1-\frac{1}{k}\right)$, so we get

$$
n\left(1-\frac{1}{k}\right)^x=1
$$

Solving this equation gives

$$
x=-\frac{\ln n}{\ln\left(1-\frac{1}{k}\right)}
$$

Below we prove that the complexity of the algorithm is $\Theta (k\log n)$.

???+ note "Proof"
    Consider $\displaystyle \lim _{k \rightarrow \infty} k \log \left(1-\frac{1}{k}\right)$; we have
    
    $$
    \begin{aligned}
    \lim _{k \rightarrow \infty} k \log \left(1-\frac{1}{k}\right)&=\lim _{k \rightarrow \infty} \frac{\log \left(1-\frac{1}{k}\right)}{1 / k}\\
    &=\lim _{k \rightarrow \infty} \frac{\frac{\mathrm d}{\mathrm d k} \log \left(1-\frac{1}{k}\right)}{\frac{\mathrm d}{\mathrm d k}\left(\frac{1}{k}\right)}\\
    &=\lim _{k \rightarrow \infty} \frac{\frac{1}{k^{2}\left(1-\frac{1}{k}\right)}}{-\frac{1}{k^{2}}}\\
    &=\lim _{k \rightarrow \infty}-\frac{k}{k-1}\\
    &=-\lim _{k \rightarrow \infty} \frac{1}{1-\frac{1}{k}}\\
    &=-1
    \end{aligned}
    $$
    
    So $x \sim k \ln n, k\to \infty$, i.e. $-\dfrac{\ln n}{\ln\left(1-\frac{1}{k}\right)}= \Theta (k\log n)$

**This page is mainly translated from the blog post [Задача Иосифа](https://e-maxx.ru/algo/joseph_problem) and its English translation [Josephus Problem](https://cp-algorithms.com/others/josephus_problem.html). The Russian version is licensed under Public Domain + Leave a Link; the English version under CC-BY-SA 4.0.**
