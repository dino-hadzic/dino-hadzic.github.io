---
title: Linear congruences
---

This article discusses solving linear congruences.

## Basic concepts

Let $a,b,n$ be integers and $x$ an unknown. Then an equation of the form

$$
ax\equiv b\pmod n
$$

is called a **linear congruence equation**.

Solving a linear congruence means finding all solutions $x$ in the interval $[0,n-1]$. Of course, adding or subtracting any multiple of $n$ still gives solutions of the equation. Modulo $n$, these are all the solutions of the equation.

The rest of this article introduces two approaches to solving linear congruences, using inverses and Diophantine equations, respectively. In the general case, both computing inverses and solving Diophantine equations require the [extended Euclidean algorithm](./gcd.md#extended-euclidean-algorithm), so the two approaches are in fact the same.

## Solving with inverses

First, consider the case where $a$ and $n$ are coprime, i.e. $\gcd(a,n)=1$. In this case we can compute the [inverse](./inverse.md)  $a^{-1}$ of $a$ and multiply both sides of the equation by $a^{-1}$, which gives the unique solution of the equation:

$$
x \equiv ba^{-1} \pmod n.
$$

Next, consider the case where $a$ and $n$ are not coprime, i.e. $\gcd(a,n)=d>1$. In this case the original equation does not necessarily have a solution. For example, $2x\equiv 1\pmod 4$ has no solution. Therefore, two cases need to be considered:

-   When $d$ does not divide $b$, the equation has no solution. For any $x$, the left-hand side $ax$ is a multiple of $d$, but the right-hand side $b$ is not a multiple of $d$. Therefore, they cannot differ by a multiple of $n$, because any multiple of $n$ is also a multiple of $d$. So the equation has no solution.

-   When $d$ divides $b$, the parameters $a,b,n$ of the equation can all be divided by $d$, giving a new equation:

    $$
    a'x \equiv b'\pmod{n'}.
    $$

    Here $\gcd(a',n')=1$, that is, $a'$ and $n'$ are coprime. This case has already been solved above, so the smallest non-negative integer solution $x'$ of the equation can be obtained by computing an inverse.

    Obviously, $x'$ is also a solution of the original equation. But it is not the only solution of the original equation. Since the set of all solutions of the transformed equation is

    $$
    \{x' + kn' : k\in\mathbf Z\}.
    $$

    those of these solutions that fall in the interval $[0,n-1]$ are exactly all the solutions of the original equation in the interval $[0,n-1]$:

    $$
    x \equiv (x' + kn')\pmod{n},\quad k = 0, 1, \cdots, d-1.
    $$

Summarizing the two cases, the **number of solutions** of a linear congruence equals $d=\gcd(a,n)$ or $0$.

## Solving with Diophantine equations

A linear congruence is equivalent to the [linear Diophantine equation in two variables](./bezouts.md#the-case-of-two-variables) $x,y$:

$$
ax + ny = b.
$$

By the discussion on the linked page, the equation has a solution if and only if $\gcd(a,n)\mid b$, and the general solution of the equation is

$$
\begin{aligned}
x &= x_0 + t\dfrac{n}{d},\\
y &= y_0 - t\dfrac{a}{d},
\end{aligned}
$$

where $d=\gcd(a,n)$ is their greatest common divisor and $t$ is an arbitrary integer.

Hence, the general solution of the linear congruence is

$$
x \equiv \left(x_0+t\dfrac{n}{d}\right)\pmod{n},\quad t\in\mathbf Z.
$$

Taking $x_0$ modulo $n/d$ gives the smallest (non-negative) integer solution of the congruence, i.e. the $x'$ above.

## Reference implementation

The reference implementation given in this section finds the smallest non-negative integer solution of the congruence. If no solution exists, it outputs $-1$.

???+ example "Reference implementation"
    === "C++"
        ```cpp
        --8<-- "docs/math/code/linear-equation/linear-equation.cpp:core"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/math/code/linear-equation/linear-equation.py:core"
        ```

## Exercises

-   [「NOIP2012」同余方程 (Congruence Equation)](https://loj.ac/problem/2605)

**This page is mainly translated from the blog post [Модульное линейное уравнение первого порядка](http://e-maxx.ru/algo/diofant_1_equation) and its English translation [Linear Congruence Equation](https://cp-algorithms.com/algebra/linear_congruence_equation.html). The Russian version is licensed under Public Domain + Leave a Link; the English version under CC-BY-SA 4.0. The content has been modified.**
