---
title: Randomized incremental algorithm
---

## Introduction

The randomized incremental algorithm is an important algorithm in computational geometry: it does not require much theoretical background, has low time complexity, and has a wide range of applications.

The idea of the incremental algorithm is similar to the first principle of mathematical induction; in essence, it reduces a problem to a subproblem exactly one level smaller. After solving the subproblem, the current object is added. Written as a recurrence:

$$
T(n)=T(n-1)+g(n)
$$

The incremental algorithm has a concise form and can be applied to many geometry problems.

The incremental algorithm is often combined with randomization, giving the randomized incremental algorithm.

The idea of the randomized incremental algorithm is: each time a new object is added, if it changes the answer, recompute locally. Therefore, the randomized incremental algorithm usually requires that it be easy to quickly decide whether adding an element changes the answer, and that the expected number of answer changes under a random order be small.

The randomized incremental algorithm is commonly used to solve the [smallest enclosing circle](smallest-enclosing-circle.md) problem, and can also be used to solve half-space intersection, higher-dimensional convex hulls, randomized Delaunay triangulation, and other problems.

## Exercises

[最小圆覆盖 (Smallest Enclosing Circle)](https://www.luogu.com.cn/problem/P1742)

[「HNOI2012」射箭 (Archery)](https://www.luogu.com.cn/problem/P3222)

[CodeForces 442E](https://codeforces.com/problemset/problem/442/E)

## References and further reading

[随机增量算法 (Randomized Incremental Algorithm) – Xie Yilun](https://github.com/hzwer/shareOI/blob/master/%E8%AE%A1%E7%AE%97%E5%87%A0%E4%BD%95/%E9%9A%8F%E6%9C%BA%E5%A2%9E%E9%87%8F%E7%AE%97%E6%B3%95_%E8%A7%A3%E8%BD%B6%E4%BC%A6.pdf)

<https://www.cnblogs.com/aininot260/p/9635757.html>

<https://blog.csdn.net/u014609452/article/details/62039612>

[随机 Delaunay 三角剖分 (Randomized Delaunay Triangulation)](https://zhuanlan.zhihu.com/p/364390356)
