---
title: Kahan summation
---

## Introduction

The **Kahan summation** algorithm, also known as compensated summation or carry summation, is an algorithm for **reducing the error when accumulating the sum of a sequence of finite-precision floating-point numbers**. It achieves this mainly by keeping a separate variable (commonly named $c$) that accumulates the error.

The algorithm was discovered mainly by William Kahan in the 1960s. Since Ivo Babuška independently proposed a similar algorithm, Kahan summation is also known as Kahan–Babuška summation.

## Rounding error

In computer programs, we need to approximate real numbers with a finite number of digits; most of today's computers use the floating-point numbers specified by [IEEE-754](https://en.wikipedia.org/wiki/IEEE_754) as this approximation. Since we cannot represent $\frac{1}{3}$ exactly with a finite number of digits, part of the value must be rounded off (truncated) when using the IEEE-754 representation. This **rounding off error** is a characteristic of floating-point computation.

In floating-point addition, commutativity holds, but associativity does not. That is, $a+b = b+a$ but $(a+b)+c \neq a+(b+c)$. Therefore, when adding a sequence of floating-point numbers, we can either accumulate them one by one from left to right, or group them into pairs while keeping the original order. The second method is relatively slower and needs more memory, and it is often used by the dedicated summation functions of some languages, but its result is relatively more accurate.

To obtain a more accurate floating-point sum, we need the Kahan summation algorithm.

When computing $S_{new}=S_{old}+a$ ($a$ is one value of the floating-point sequence), define the value actually added to $S$ as $a_{eff}=S_{new}-S_{old}$; if $a_{eff}$ is larger than $a$, there was an upward rounding error, and if $a_{eff}$ is smaller than $a$, there was a downward rounding error. The rounding error is then defined as $E_{roundoff} = a_{eff} - a$. The value used to correct this rounding error is $a-a_{eff}$, i.e. the negative of $E_{roundoff}$. Defining $c$ as the variable that compensates for the lost low-order digits, we get $c_{new} = c_{old} + (a - a_{eff})$.

## Procedure

The Kahan summation algorithm accumulates the error in a separate variable. As shown in the reference code below, $sum$ is the final accumulated result that is returned. $c$ is the variable that compensates for the lost low-order digits (the part that was rounded off), and it is the essential variable of the Kahan summation algorithm.

Because $sum$ is large and $y$ is small, the low-order digits of $y$ are lost. $(t - sum)$ cancels the high-order part of $y$, and subtracting $y$ recovers the negative value (the low-order part of $y$). Therefore, algebraically $c$ is always zero. In the next iteration, the lost low-order part is added back into $y$.

## Implementation

??? note "Reference code"
    ```cpp
    float kahanSum(vector<float> nums) {
      float sum = 0.0f;
      float c = 0.0f;
      for (auto num : nums) {
        float y = num - c;
        float t = sum + y;
        c = (t - sum) - y;
        sum = t;
      }
      return sum;
    }
    ```

## Exercises

In OI, Kahan summation exists mainly as an auxiliary tool that provides a computed result with a smaller error.

???+ note "Example [CodeForces Contest 800 Problem A. Voltage Keepsake](https://codeforces.com/contest/800/problem/A)"
    There are $n$ devices used simultaneously. The $i$-th device uses $a_{i}$ units of power per second. This usage is continuous, that is, in $\lambda$ seconds the device will use $\lambda \times a_{i}$ units of power. The $i$-th device currently has $b_{i}$ units of power stored. All devices can store an arbitrary amount of power. There is a single charger that can be plugged into any single device. The charger adds $p$ units of power per second to the device. This charging is continuous, that is, if the device is plugged in for $\lambda$ seconds, it will gain $\lambda \times p$ units of power. We can switch which device is being charged at any moment of time (including real moments; the time needed to switch is negligible). Find the maximum amount of time the devices can be used before one of them reaches $0$ units of power.

???+ note "Example [CodeForces Contest 504 Problem B. Misha and Permutations Summation](https://codeforces.com/problemset/problem/504/B)"
    Define the sum of two permutations $p$ and $q$ of the numbers $0, 1, \cdots, (n - 1)$ as $Perm((Ord(p)+Ord(q))\bmod n!)$, where $Perm(x)$ is the $x$-th lexicographical permutation of the numbers $0, 1, \cdots, (n-1)$ (counting from zero), and $Ord(p)$ is the number of permutations lexicographically smaller than $p$. For example, $Perm(0) = (0, 1, \cdots , n - 2, n - 1)$, $Perm(n! - 1) = (n - 1, n-2,\cdots, 1,0))$. Misha has two permutations $p$ and $q$; find their sum.

## Summation in programming languages

Python's standard library specifies the correctly rounded summation function [fsum](https://docs.python.org/3/library/math.html#math.fsum), which can be used to return an accurate floating-point sum of the values in an iterable; it avoids loss of precision by tracking multiple intermediate partial sums using the Shewchuk algorithm.

In the Julia language, the default implementation of the [sum](https://docs.julialang.org/en/v1/base/collections/#Base.sum) function is pairwise summation, for high accuracy and good performance. Meanwhile, the external library function [sum\_kbn](http://www.jlhub.com/julia/manual/en/function/sum_kbn) provides an implementation of the Neumaier variant for cases where higher accuracy is needed; see [KahanSummation.jl](https://github.com/JuliaMath/KahanSummation.jl).

## References and notes

1.  [Kahan\_summation\_algorithm - Wikipedia](https://en.wikipedia.org/wiki/Kahan_summation_algorithm)
2.  [Kahan summation - Rosetta Code](https://rosettacode.org/wiki/Kahan_summation)
3.  [VK Cup Round 2 + Codeforces Round 409 Announcement](https://codeforces.com/blog/entry/51577)
4.  [Rounding off errors in Java - GeeksforGeeks](https://www.geeksforgeeks.org/rounding-off-errors-java/)
