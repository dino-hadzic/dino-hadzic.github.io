---
title: Numerical characteristics of random variables
---

This article introduces the expectation, variance and other numerical characteristics of random variables.

## Expectation

### Definition

#### Discrete random variables

Let the distribution of a discrete random variable $X$ be $p_i = P\{ X = x_i \}$. If the sum

$$
\sum x_i p_i
$$

converges absolutely, its value is called the **expectation** (expected value) of $X$, denoted $EX$.

#### Continuous random variables

Let the density function of a continuous random variable $X$ be $f(x)$. If the integral

$$
\int_{\mathbb{R}} xf(x) \text{d} x
$$

converges absolutely, its value is called the **expectation** of $X$, denoted $EX$.

#### Unified definition

Let the distribution function of a random variable $X$ be $F(x)$. If the [Stieltjes integral](https://en.wikipedia.org/wiki/Riemann%E2%80%93Stieltjes_integral)

$$
\int_{\mathbb{R}} x \text{d} F(x)
$$

converges absolutely, its value is called the **expectation** of $X$, denoted $EX$.

??? example "An example where the expectation does not exist"
    Consider a discrete random variable $X$ with the following distribution
    
    $$
    P\left\{ X = (-1)^k \frac{2^k}{k} \right\} = \frac{1}{2^k}, \quad k = 1, 2, \cdots
    $$
    
    Although the sum $\sum x_i p_i$ converges to $- \ln 2$, it does not converge absolutely, so the expectation of $X$ does not exist.
    
    Next, consider a continuous random variable $Y$ with the following density function
    
    $$
    f(y) = \frac{1}{\pi} \cdot \frac{1}{1 + y^2}, \quad y \in (-\infty, +\infty)
    $$
    
    It is easy to verify that the expectation of $Y$ does not exist either.

### Properties of expectation

#### Linearity

If the expectations of the random variables $X, Y$ exist, then

-   for any real numbers $a, b$, $E(aX + b) = a \cdot EX + b$;
-   $E(X + Y) = EX + EY$.

#### Expectation of a product of random variables

If the expectations of the random variables $X$, $Y$ exist and $X$, $Y$ are independent, then

$$
E(XY) = EX \cdot EY
$$

Note: the independence in the above property is **not** a necessary condition.

??? example "Counterexample"
    Consider random variables $X$ and $Y$, where $X$ is uniformly distributed on $[-1, 1]$ and $Y = X^2$.

### Converting between expectation and probability

For a random event $A$, consider its indicator function $I_A$:

$$
I_A(\omega) = \begin{cases}
    1, & \omega \in A \\
    0, & \omega \notin A
\end{cases}
$$

By definition, its expectation is $EI_A = P(A)$. This conversion is very common in practical applications.

??? example "Example"
    Suppose that in a sequence $\{ a_i \}$ of length $n$, the element $a_k$ takes the value $k$ with probability $p_k$ and the value $0$ with probability $1 - p_k$. Consider how to find the expectation of $S = \sum_{i=1}^{n} a_i$.
    
    If we compute directly from the definition, we need to find the probability of $S$ at each possible value; this computation is rather tedious and is not elaborated here.
    
    On the other hand, if $I_k$ denotes the indicator function of the random event $a_k = k$, then
    
    $$
    S = \sum_{k=1}^{n} k \cdot I_k
    $$
    
    and it is then easy to obtain
    
    $$
    ES = E \left( \sum_{k=1}^{n} k \cdot I_k \right) = \sum_{k=1}^{n} k \cdot E[I_k] = \sum_{k=1}^{n} k \cdot p_k
    $$

## Conditional distribution and conditional expectation

We have studied conditional probability before; analogously, the notion of conditional expectation can be introduced.

### Definition

For two random variables $X$, $Y$, the distribution (density function) of $X$ given $Y = y$ is called the **conditional distribution (conditional density)**, denoted respectively

$$
P( X = x_i | Y = y ) \qquad f_{X|Y}(x|y)
$$

The expectation of $X$ under this condition is called the **conditional expectation**, denoted $E[X|Y=y]$.

### Properties of conditional expectation

Many properties of conditional expectation follow from those of conditional probability and are not repeated here.

It is worth mentioning that $E[X | Y]$ is in general a function of the random variable $Y$, and this function is usually not linear. But in fact

$$
E[E[X|Y]] = EX
$$

The formula above is called the **law of total expectation**.

### Application

???+ example "[HDU 5984 Pocky](https://acm.hdu.edu.cn/showproblem.php?pid=5984)"
    There is a Pocky stick of length $L$, which is broken at random into two pieces each time. If the length of the right piece is at most $d$, we stop; otherwise we repeat the process on the right piece. Find the expected number of repetitions.

??? note "Solution"
    Let $f(x)$ denote the expected number of repetitions for length $x$. The case $x \leq d$ is trivial.
    
    When $x > d$, let the distance of the breaking point from the right end be $k$; clearly $k \sim U[0, x]$, and the expected number of repetitions is then
    
    $$
    g(k) = \begin{cases}
        1, & k \leq d \\
        1 + f(k), & k > d
    \end{cases}
    $$
    
    By the law of total expectation,
    
    $$
    f(x) = Eg(k) = 1 + \frac{1}{x} \cdot \int_{d}^{x} f(t) \text{d} t
    $$
    
    Solving this integral equation and plugging in the initial condition gives
    
    $$
    f(x) = 1 + \ln \frac{x}{d}
    $$

## Variance

### Definition

Let the expectation $EX$ of a random variable $X$ exist, and let the expectation

$$
E(X - EX)^2
$$

also exist. Then the value of the above expression is called the **variance** of the random variable $X$, denoted $DX$ or $Var(x)$. The arithmetic square root of the variance is called the **standard deviation**, denoted $\sigma(X) = \sqrt{DX}$.

### Properties of variance

If the variance of a random variable $X$ exists, then

-   for any constants $a, b$, $D(aX + b) = a^2 \cdot DX$
-   $DX = E(X^2) - (EX)^2$

## Covariance and correlation coefficient

In general, the equality $D(X + Y) = DX + DY$ does not hold, so two questions naturally arise:

-   What exactly is the difference between $D(X + Y)$ and $DX + DY$?
-   Under what conditions are $D(X + Y)$ and $DX + DY$ equal?

For the first question, we introduce the covariance as the answer.

### Definition of covariance

For random variables $X, Y$, the quantity

$$
E((X - EX)(Y - EY))
$$

is called the **covariance** of $X$ and $Y$, denoted $\operatorname{Cov}(X, Y)$.

### Properties of covariance

For random variables $X, Y, Z$,

-   $\operatorname{Cov}(X, Y) = \operatorname{Cov}(Y, X)$
-   for any constants $a, b$, $\operatorname{Cov}(aX + bY, Z) = a \cdot \operatorname{Cov}(X, Z) + b \cdot \operatorname{Cov}(Y, Z)$

At the same time, covariance and variance are related as follows:

-   $DX = \operatorname{Cov}(X, X)$
-   $D(X + Y) = DX + 2 \operatorname{Cov}(X, Y) + DY$

??? note "About covariance"
    You may have noticed that the properties of covariance formally coincide completely with the properties of the inner product of vectors.
    
    From the viewpoint of functional analysis, for a given probability space, all random variables on it form a linear space, the covariance is an inner product on this space, and the standard deviation is the norm induced by this inner product.

As for the second question raised above, it is easy to see that $D(X + Y) = DX + DY$ if and only if $\operatorname{Cov}(X, Y) = 0$. An intuitive sufficient condition is that $X$ and $Y$ are independent, since then

$$
\operatorname{Cov}(X, Y) = E((X - EX)(Y - EY)) = E(X - EX) E(Y - EY) = 0
$$

But this condition is not necessary. To describe the relationship between random variables $X$, $Y$ satisfying $\operatorname{Cov}(X, Y) = 0$, we introduce the correlation coefficient.

### Correlation coefficient

For random variables $X, Y$, the quantity

$$
\frac{ \operatorname{Cov}(X, Y)}{ \sigma(X)\sigma(Y) }
$$

is called the **Pearson correlation coefficient** of $X$ and $Y$, denoted $\rho_{X,Y}$.

The Pearson correlation coefficient describes how tight the linear relationship between two random variables is. The larger $|\rho_{X,Y}|$, the stronger the linear relationship between $X$ and $Y$. It is not hard to prove that $|\rho_{X,Y}| \leq 1$, and that $|\rho_{X,Y}| = 1$ can only occur in the following two cases:

-   when there exist a real number $a$ and a positive real number $b$ such that $P(X = a + bY) = 1$, we have $\rho_{X,Y} = 1$;
-   when there exist a real number $a$ and a negative real number $b$ such that $P(X = a + bY) = 1$, we have $\rho_{X,Y} = -1$.

When $\rho_{X,Y} = 0$, we say that the random variables $X$ and $Y$ are **uncorrelated**; in this case there is no linear relationship between $X$ and $Y$.

??? note "“Uncorrelated” and “independent”"
    Two random variables being uncorrelated only means that there is no linear relationship between them, not that there is no relationship of any other form.
    
    Therefore, two random variables $X, Y$ being uncorrelated is a **necessary but not sufficient** condition for their independence.

For the second question raised at the beginning of this section, we give the conclusion: $\operatorname{Cov}(X, Y) = 0$ holds if and only if one of $X$, $Y$ takes a constant value with probability $1$, or $X, Y$ are uncorrelated.
