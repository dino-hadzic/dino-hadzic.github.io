---
title: Newton's method
---

## Introduction

This article describes how to use Newton's method for finding roots to find an approximate solution of an equation. The method was proposed by Newton in the 17th century.

The concrete task is: for a function $f(x)$ that is continuous and monotonic on $[a,b]$, find an approximate solution of the equation $f(x)=0$.

## Explanation

Initially we start from the given $f(x)$ and an approximate solution $x_0$ (the question of the initial value is related to Newton fractals; see [Newton's fractal](https://www.bilibili.com/video/BV1HQ4y1q78v) by 3Blue1Brown).

Suppose our current approximate solution is $x_i$. We draw the line $l$ tangent to $f(x)$ at the point $(x_i,f(x_i))$ and denote the x-coordinate of the intersection of $l$ with the $x$-axis by $x_{i+1}$; this is a better approximate solution. We repeat this iterative process.
From the geometric meaning of the derivative, we obtain the following relation:

$$
 f'(x_i) = \frac{f(x_i)}{x_{i} - x_{i+1}}
$$

Rearranging gives the following recurrence:

$$
 x_{i+1} = x_i - \frac{f(x_i)}{f'(x_i)}
$$

Intuitively, if $f(x)$ is reasonably smooth, then as the number of iterations increases, $x_i$ gets closer and closer to the solution of the equation.

The convergence rate of Newton's method is quadratic, which means that the number of correct digits of the approximate solution doubles after each iteration.
For a proof of the convergence of Newton's method, see [citizendium - Newton method Convergence analysis](http://en.citizendium.org/wiki/Newton%27s_method#Convergence_analysis)

Of course, Newton's method also has its drawbacks; for details, see the analysis on pages 18–20 of [Xiaolin Wu - Roots of Equations](https://www.ece.mcmaster.ca/~xwu/part2.pdf)

## Computing square roots

Let us try to compute square roots with Newton's method. Let $f(x)=x^2-n$; an approximate solution of this equation is an approximation of $\sqrt{n}$. Thus we obtain

$$
x_{i+1}=x_i-\frac{x_i^2-n}{2x_i}=\frac{x_i+\frac{n}{x_i}}{2}
$$

When implementing it, take care to set a suitable precision. The code is as follows

### Implementation

=== "C++"
    ```cpp
    double sqrt_newton(double n) {
      constexpr static double eps = 1E-15;
      double x = 1;
      while (true) {
        double nx = (x + n / x) / 2;
        if (abs(x - nx) < eps) break;
        x = nx;
      }
      return x;
    }
    ```

=== "Python"
    ```python
    def sqrt_newton(n):
        eps = 1e-15
        x = 1
        while True:
            nx = (x + n / x) / 2
            if abs(x - nx) < eps:
                break
            x = nx
        return x
    ```

## Computing integer square roots

Although we can call the `sqrt()` function to obtain the value of the square root, here we still describe a variant of Newton's method for finding the largest integer solution of the inequality $x^2\le n$. We still consider a process similar to Newton's iteration, but with a slight modification of the boundary condition. If in the previous iteration the approximate solution $x$ became smaller, and in this iteration it would become larger, then we do not perform this iteration and exit the loop.

### Implementation

=== "C++"
    ```cpp
    int isqrt_newton(int n) {
      int x = 1;
      bool decreased = false;
      for (;;) {
        int nx = (x + n / x) >> 1;
        if (x == nx || (nx > x && decreased)) break;
        decreased = nx < x;
        x = nx;
      }
      return x;
    }
    ```

=== "Python"
    ```python
    def isqrt_newton(n):
        x = 1
        decreased = False
        while True:
            nx = (x + n // x) // 2
            if x == nx or (nx > x and decreased):
                break
            decreased = nx < x
            x = nx
        return x
    ```

## Arbitrary-precision square roots

Finally, consider Newton's method with arbitrary-precision arithmetic (bignum). The iteration is unchanged, but this time we need to pay attention to the choice of the initial approximate solution, i.e., the value of $x_0$. Since the numbers that require arbitrary-precision arithmetic are generally very large, different initial values have a great impact on the efficiency of the algorithm. A natural idea is to take $x_0=2^{\left\lfloor\frac{1}{2}\log_2n\right\rfloor}$, which allows $x_0$ to be computed quickly and is also reasonably close to the approximate value of the square root.

### Implementation

Here is an implementation in Java:

```java
public static BigInteger isqrtNewton(BigInteger n) {
  BigInteger a = BigInteger.ONE.shiftLeft(n.bitLength() / 2);
  boolean p_dec = false;
  for (;;) {
    BigInteger b = n.divide(a).add(a).shiftRight(1);
    if (a.compareTo(b) == 0 || a.compareTo(b) < 0 && p_dec)
      break;
    p_dec = a.compareTo(b) > 0;
    a = b;
  }
  return a;
}
```

In practice: for $n=10^{1000}$ the running time of this algorithm is 60 ms; if we do not optimize the value of $x_0$ and iterate directly from $x_0=1$, the running time increases to 120 ms.

## Exercises

-   [UVa 10428 - The Roots](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=16&page=show_problem&problem=1369)
-   [LeetCode 69. x 的平方根 (Sqrt(x))](https://leetcode-cn.com/problems/sqrtx/)

    **This page is mainly translated from the blog post [Метод Ньютона (касательных) для поиска корней](http://e-maxx.ru/algo/roots_newton) and its English translation [Newton's method for finding roots](https://cp-algorithms.com/num_methods/roots_newton.html). The Russian version is licensed under Public Domain + Leave a Link; the English version under CC-BY-SA 4.0.**
