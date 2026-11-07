---
title: Random variables
---

## Related concepts

### Random variable

Given a probability space $(\Omega, \mathcal{F}, P)$, if a function $X : \Omega \to \mathbb{R}$ defined on the sample space $\Omega$ satisfies: for every $t \in \mathbb{R}$,

$$
\{ \omega \in \Omega : X(\omega) \le t \} \in \mathcal{F}
$$

then $X$ is called a **random variable**.

### Indicator function

For an event $A$ on the sample space $\Omega$, define the random variable

$$
I_A(\omega) = \begin{cases}
    1, & \omega \in A \\
    0, & \omega \notin A
\end{cases}
$$

and call $I_A$ the **indicator function** of the event $A$.

### Cumulative distribution function

For a random variable $X$, the function

$$
F(x) = P( X \leq x )
$$

is called the **cumulative distribution function** of the random variable $X$. We write $X \sim F(x)$.

The cumulative distribution function has the following properties:

-   **right-continuity**: $F(x) = F(x + 0)$
-   **monotonicity**: it is monotonically increasing (not strictly) on $\mathbb{R}$
-   $F(-\infty) = 0$,$F(+\infty) = 1$

At the same time, we can prove that every function satisfying the above requirements is the cumulative distribution function of some random variable. Therefore, cumulative distribution functions and random variables are in one-to-one correspondence.

## Classification of random variables

Random variables are divided into **discrete** and **continuous** ones according to whether their range (by definition, a random variable is a function) is countable.

### Discrete random variables

Let $X$ be a discrete random variable whose possible values are $x_1, x_2, \cdots$. Then we can describe $X$ by a series of equations of the form $P\{ X = x_i \} = p_i$. This is the **distribution table** (probability mass function) we learned in high school textbooks.

### Continuous random variables

Let $X$ be a continuous random variable. Examining $P\{ X = x \}$ is often meaningless (because this probability is very likely $0$).

??? note "Why we say the probability is “very likely” $0$"
    Consider the random variable $X$ that takes the value $0$ with probability $\frac{1}{2}$ and follows the uniform distribution on the open interval $(0, 1)$ with probability $\frac{1}{2}$. Clearly $X$ satisfies the definition of a continuous random variable.
    
    For every real number $r \in (0, 1)$, it is easy to obtain $P\{ X = r \} = 0$, but at the same time $P\{ X = 0 \} = \frac{1}{2}$.

On the other hand, let $X \sim F(x)$; then

$$
P( l < x \leq l + \Delta x ) = F(l + \Delta x) - F(l)
$$

A natural idea is to use the limit $\lim\limits_{\Delta x \to 0^+} \frac{F(l + \Delta x) - F(l)}{\Delta x}$ to describe the likelihood that $X$ takes the value $l$.

This expression is the familiar derivative, so the problem becomes finding a nonnegative function $f(x)$ such that

$$
F(x) = \int_{-\infty}^{x} f(x) \text{d} x
$$

If such an $f(x)$ exists, it is called the **density function** of $X$.

## Independence of random variables

Earlier we discussed the independence of random events. Since random variables and random events are closely related, we can similarly give the definition of independence of random variables.

### Definition

If random variables $X, Y$ satisfy that for all $x, y \in \mathbb{R}$,

$$
P( X \leq x, Y \leq y ) = P( X \leq x ) P( Y \leq y )
$$

then the random variables $X, Y$ are called **independent**.

??? note "Note"
    Some students may have noticed that high school textbooks define the independence of random variables using probabilities of the form $P(X = \alpha)$, but since the probability that a continuous random variable takes a specific value is usually $0$, in the more general setting the definition via the cumulative distribution function is the wiser choice.

### Properties

If random variables $X$,$Y$ are mutually independent, then for any functions $f, g$, the random variables $f(X)$ and $g(Y)$ are mutually independent.

??? warning "Warning"
    Sometimes we study the distribution of some function $f(X, Y)$ (such as $XY^2$) of mutually independent random variables $X$,$Y$.
    
    Although $X$ and $Y$ are independent, one must not take for granted that for some value $y$ of $Y$, $f(X, y)$ and $f(X, Y)$ follow the same distribution.
