---
title: Simulated annealing
---

## Introduction

Simulated annealing is a randomized algorithm. When the number of possible solutions of a problem is enormous (or even infinite) and the function is not unimodal, we often use simulated annealing to solve it.

## Explanation

Looking at the process of [hill climbing](./hill-climbing.md), we notice: a non-optimal solution near the current optimum is simply discarded by hill climbing. But in many cases we need to accept this non-optimal solution in order to escape the local optimum – that is the simulated annealing algorithm.

??? note "What is annealing? (from [Baidu Baike](https://baike.baidu.com/item/%E9%80%80%E7%81%AB/1039313))"
    Annealing is a metal heat-treatment process in which a metal is slowly heated to a certain temperature, held there for a sufficient time, and then cooled at a suitable rate. Its purposes are to reduce hardness and improve machinability; to eliminate residual stress, stabilize dimensions, and reduce the tendency to deform and crack; and to refine grains, adjust the structure, and eliminate structural defects. More precisely, annealing is a heat-treatment process for materials, including both metallic and non-metallic materials. Moreover, the purposes of annealing new materials are partly the same as and partly different from those of traditional metal annealing.

Since the laws of annealing introduce more random factors, the probability of obtaining the optimal solution increases greatly. So we can simulate this process, taking the objective function as the energy function.

### Process

In one sentence: if the solution of the new state is better, update the answer; otherwise accept the new state with a certain probability.

Define the current temperature as $T$, and the energy (value) difference between the new state $S'$ and the known state $S$ (the new state is obtained from the known state in a random way) as $\Delta E$ ($\Delta E\geqslant 0$); then the probability of a state transition (updating the optimal solution) is

$$
P(\Delta E)=
\begin{cases}
1,                              & S' \text{ is better than } S,\\
\mathrm{e}^\frac{-\Delta E}{T}, & \text{otherwise}.
\end{cases}
$$

**Note**: sometimes, to make the obtained solution of higher quality, after simulated annealing finishes we randomly sample states near the obtained solution several times at the current temperature, trying to get a better solution (the process is similar to simulated annealing).

### How to anneal (cool down)

In simulated annealing we have three parameters: the initial temperature $T_0$, the cooling coefficient $d$, and the final temperature $T_k$. Here $T_0$ is a fairly large number, $d$ is a number very close to $1$ but less than $1$, and $T_k$ is a positive number close to $0$.

First let the temperature be $T=T_0$, then make one transition attempt according to the steps above, and then let $T=d\cdot T$. When $T<T_k$, the simulated annealing process ends, and the current optimal solution is the final optimal solution.

Note that to make the solution more precise, we usually do not take the current solution directly as the answer, but maintain the best value among all solutions encountered during the annealing process.

Here is a picture from [Simulated annealing - Wikipedia](https://en.wikipedia.org/wiki/Simulated_annealing) (as the temperature decreases, the jumps become less and less random, and the optimal solution becomes more and more stable).

![](./images/simulated-annealing.gif)

## Implementation

The code here uses [「BZOJ 3680」吊打 XXX (Beat Up XXX)](https://hydro.ac/p/bzoj-P3680) (find the weighted Fermat point of $n$ points) as an example.

```cpp
--8<-- "docs/misc/code/simulated-annealing/simulated-annealing_1.cpp"
```

## Some tricks

### Block-wise simulated annealing

Sometimes the function has many peaks and simulated annealing has difficulty finding the optimal solution.

In that case we can split the whole domain into several segments, run simulated annealing on each segment, and then take the best solution.

### Using up the time limit

There is a function `clock()` that returns the running time of the program.

We can replace `simulateAnneal();` in the main program with `while ((double)clock()/CLOCKS_PER_SEC < MAX_TIME) simulateAnneal();`. This keeps running simulated annealing until the elapsed time is about to exceed the time limit.

Here `MAX_TIME` is a custom number slightly less than the time limit (in seconds).

## Exercises

-   [「BZOJ 3680」吊打 XXX (Beat Up XXX)](https://hydro.ac/p/bzoj-P3680)
-   [「JSOI 2016」炸弹攻击 (Bomb Attack)](https://loj.ac/problem/2076)
-   [「HAOI 2006」均分数据 (Evenly Splitting Data)](https://www.luogu.com.cn/problem/P2503)
