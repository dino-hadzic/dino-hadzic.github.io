---
title: Scheduling jobs on one machine
---

You have $n$ jobs and need to find the order of executing them with the minimum cost. The $i$-th job takes $t_i$ time to execute, and making the $i$-th job wait for time $t$ costs $f_i(t)$.

Formally: given $n$ functions $f_i$ and $n$ numbers $t_i$, find a permutation $p$ that minimizes

$$
F(p)=\sum_{i=1}^nf_{p_i}\left(\sum_{j=1}^{i-1}t_{p_j}\right)
$$

## Special cost functions

### Linear cost function

First we consider the case where all functions are linear, i.e. $f_i(x)=c_ix+d_i$, where the $c_i$ are non-negative integers. Obviously we can add up the constant terms in advance, so the functions take the form $f_i(x)=c_ix$.

Consider two permutations $p$ and $p'$, where $p'$ is obtained from $p$ by swapping the elements at positions $i$ and $i+1$. Then

$$
\begin{aligned}
F(p')-F(p)&=c_{p'_i}\sum_{j=1}^{i-1}t_{p'_j}+c_{p'_{i+1}}\sum_{j=1}^{i}t_{p'_j}
-\left(c_{p_i}\sum_{j=1}^{i-1}t_{p_j}+c_{p_{i+1}}\sum_{j=1}^{i}t_{p_j}\right)\\
&=c_{p_i}t_{p_{i+1}}-c_{p_{i+1}}t_{p_i}
\end{aligned}
$$

So it suffices to sort with the strategy "swap if $c_{p_i}t_{p_{i+1}}-c_{p_{i+1}}t_{p_i}<0$". Written in the form $\dfrac{c_{p_i}}{t_{p_i}}<\dfrac{c_{p_{i+1}}}{t_{p_{i+1}}}$, this can be understood as sorting the permutation in decreasing order of $\dfrac{c_i}{t_i}$.

To handle this problem, our idea is to consider what changes after a small perturbation and greedily choose the optimal solution.

### Exponential cost function

Consider a cost function of the form $f_i(x)=c_i\mathrm{e}^{ax}$, where $c_i\ge 0,a>0$.

We follow the previous idea and consider the change in cost caused by swapping the elements at positions $i$ and $i+1$. The resulting algorithm is to sort the permutation in increasing order of $\dfrac{1-\mathrm{e}^{at_i}}{c_i}$.

### Identical monotonically increasing function

Consider the case where all $f_i(x)$ are the same monotonically increasing function. Then obviously we just sort the permutation in increasing order of $t_i$.

## Livshits–Kladov theorem

The Livshits–Kladov theorem holds if and only if the cost function is one of the following three cases:

-   linear function: $f_i(t) = c_it + d_i$, where $c_i\ge 0$;
-   exponential function: $f_i(t) = c_i \mathrm{e}^{a t} + d_i$, where $c_i,a>0$;
-   identical monotonically increasing function: $f_i(t) = \phi(t)$, where $\phi(t)$ is a monotonically increasing function.

The theorem is proven under the assumption that the cost function is sufficiently smooth (the third derivative exists). In these three cases, the optimal solution of the problem can be found by simple sorting in $O(n\log n)$ time.

**This page is mainly translated from the blog post [Задача Джонсона с одним станком](http://e-maxx.ru/algo/johnson_problem_1) and its English translation [Scheduling jobs on one machine](https://cp-algorithms.com/schedules/schedule_one_machine.html). The Russian version is licensed under Public Domain + Leave a Link; the English version under CC-BY-SA 4.0.**
