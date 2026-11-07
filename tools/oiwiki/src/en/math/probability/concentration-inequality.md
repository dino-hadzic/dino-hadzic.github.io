---
title: Probability inequalities
---

[Randomized algorithms](../../misc/rand-technique.md) are sometimes used in competitive programming, and the correctness and time/space complexity of these algorithms usually rely on the premise that "the probability of certain random events is very small". For example, the complexity of quicksort relies on the event "the chosen `pivot` element is almost the smallest or the largest element" happening rarely.

This article briefly introduces some tools for analyzing randomized algorithms and gives several examples of simple applications.

## Union Bound

Let $A_1, \cdots, A_m$ be random events. Then

$$
P\left\{ \bigcup_{i=1}^m A_i \right\} \leq \sum_{i=1}^m P\{A_i\}
$$

that is, the probability that at least one of a group of events occurs does not exceed the sum of the probabilities of the individual events.

In fact, this result can be strengthened slightly:

-   The probability that at least one of a group of events occurs is **at least** the sum of the probabilities of the individual events, minus the sum of the probabilities that each pair occurs simultaneously.
-   The probability that at least one of a group of events occurs is **at most** the sum of the probabilities of the individual events, minus the sum of the probabilities that each pair occurs simultaneously, plus the sum of the probabilities that each triple occurs simultaneously.
-   …

As the number of levels grows, the alternating upper and lower bounds become tighter and tighter. This series of results resembles the inclusion–exclusion principle in form, and the proof is also similar to that of inclusion–exclusion, so it is omitted here.

## Markov's inequality

Let $X$ be a random variable taking nonnegative values. Then for any positive real number $a$,

$$
P\{ X \geq a \} \leq \frac{EX}{a}
$$

In fact, since Markov's inequality itself does not use any information about the distribution of the random variable other than its expectation, the bound obtained by applying this inequality directly is usually very loose.

### Proof

Let $I$ be the indicator function of the event $X \geq a$. Then

$$
I \leq \frac{X}{a}
$$

and hence

$$
P\{ X \geq a \} = EI \leq E \left[ \frac{X}{a} \right] = \frac{EX}{a}
$$

## Chebyshev's inequality

Let $X$ be a random variable. Then for any $a > 0$,

$$
P \{ |X - EX| \geq a \} \leq \frac{DX}{a^2}
$$

In particular, when $a$ is taken to be $k\sigma$,

$$
P \{ |X - EX| \geq k\sigma \} \leq \frac{1}{k^2}
$$

where $\sigma$ is the standard deviation of $X$.

### Proof

By assumption,

$$
P \{ |X - EX| \geq a \} = P \{ (X - EX)^2 \geq a^2 \}
$$

Note that $(X - EX)^2$ is nonnegative, so by Markov's inequality

$$
P \{ (X - EX)^2 \geq a^2 \} \leq \frac{E(X - EX)^2}{a^2} = \frac{DX}{a^2}
$$

## Chernoff bound

The general Chernoff bound can be derived by applying Markov's inequality directly to the random variable $\mathrm{e}^{tX}$:

Let $X$ be a random variable. Then for any $t > 0$,

$$
P\{ X \geq a \} = P\{ \mathrm{e}^{tX} > \mathrm{e}^{ta} \} \leq \frac{E \mathrm{e}^{tX}}{\mathrm{e}^{ta}}
$$

Similarly, when $t < 0$,

$$
P\{ X \leq a \} = P\{ \mathrm{e}^{tX} > \mathrm{e}^{ta} \} \leq \frac{E \mathrm{e}^{tX}}{\mathrm{e}^{ta}}
$$

### Chernoff bound for sums of Poisson trials

The random variables encountered in competitive programming are usually not that "general"; we can describe them using Poisson trials from probability theory.

A Poisson trial is a random experiment with only two possible outcomes.

The outcome of a single Poisson trial can be described by a random variable $X$ taking the value $0$ or $1$, with distribution

$$
P\{ X = i \} = \begin{cases}
    p_i, & i = 1 \\
    1 - p_1, & i = 0
\end{cases}
$$

For Poisson trials, we have the following result:

For $n$ independent Poisson trials $X_1, X_2, \cdots, X_n$, let $X = \sum_{i=1}^{n} X_i$ and $\mu = EX$. Then for any $0 < \epsilon < 1$,

$$
P\left\{ |X - \mu| \geq \epsilon \mu \right\} \leq 2 \exp\left( - \frac{1}{3} \mu \epsilon^2 \right)
$$

## Hoeffding's inequality

If $X_1, \cdots, X_n$ are mutually independent real random variables with $X_i\in [a_i,b_i]$, and we define the random variable $X=\sum\limits_{i=1}^n X_i$, then

$$
P\{ |X - EX| \geq \epsilon \} \leq 2\exp \left( \frac {-2\epsilon^2}{\sum\limits_{i=1}^n (b_i-a_i)^2} \right)
$$

Both the Chernoff bound and Hoeffding's inequality bound the extent to which a random variable deviates from its expected value. The proofs of these two inequalities are rather lengthy; interested readers can consult the relevant chapters of the book Probability and Computing.

Empirically, if $EX$ is not too close to $a_1+\cdots+a_n$, the bound given by this inequality is often relatively tight; if it is very close (for example in [UOJ #72 全新做法 (A completely new approach)](https://matthew99.blog.uoj.ac/blog/5511)), the bound given is often very loose, and in that case the Chernoff bound is the better choice.

## Examples of applications

### Example: estimating π by random sampling of points

Consider the following algorithm for estimating the exact value of $\pi$:

Generate $n$ points at random in the square region $[-1, 1]^2$, and let $m$ be the number of points that fall into the unit disk $x^2 + y^2 \leq 1$; then $\dfrac{4m}{n}$ can be taken as an approximation of $\pi$.

Question: how should $n$ be chosen so that the above algorithm returns a result with relative error at most $\epsilon$ with probability at least $(1 - \delta)$?

??? note "Solution"
    Let $X_i$ denote the event "the $i$-th randomly generated point lies in the unit disk"; then the total number of points in the disk is $X = \sum_{i=1}^{n} X_i$. We need to find a suitable $n$ such that
    
    $$
    P\left\{ \left| \frac{4X}{n} - \pi \right| \geq \epsilon \pi \right\} \leq \delta
    $$
    
    This is equivalent to
    
    $$
    P\left\{ \left| X - \frac{\pi}{4}n \right| \geq \epsilon \cdot \frac{\pi}{4}n  \right\} \leq \delta
    $$
    
    By the Chernoff bound, it suffices to require
    
    $$
    2 \exp\left( - \frac{1}{3} \epsilon^2 \cdot \frac{\pi}{4}n \right) \leq \delta
    $$
    
    from which we obtain
    
    $$
    n \geq \frac{12}{\pi} \epsilon^{-2} \ln \frac{2}{\delta}
    $$
    
    that is, the required accuracy is achieved when $n = \Omega(\epsilon^{-2} \ln \frac{1}{\delta})$.

### Example: the lottery problem

A box contains $n$ balls, exactly $k$ of which correspond to grand prizes. You perform a number of independent, equiprobable random draws, putting the ball back into the box after each draw. How many draws are needed to guarantee, with probability at least $(1 - \epsilon)$, that **every** prize ball has been drawn at least once?

??? note "Solution"
    If there were only one prize ball, then $M=n\log\epsilon^{-1}$ draws would suffice, because the probability of missing it in all $M$ draws is
    
    $$
    \Big(1-\dfrac 1n\Big)^{n\log\epsilon^{-1}}\leq e^{\log\epsilon}=\epsilon
    $$
    
    Now there are $k>1$ prize balls, so by the Union Bound it suffices to ensure that the probability of missing each prize ball is at most $\dfrac \epsilon k$. The answer is therefore $n \log \dfrac{k}{\epsilon}$.

### Example: randomly selecting half of the elements

Give an algorithm that selects, uniformly at random, a subset of size $\dfrac{n}{2}$ from $n$ elements; it is guaranteed that $n$ is even. The only source of randomness you may use is a fair coin, and you should try to minimize the number of coin flips (the minimum is not required).

??? note "Solution"
    First, one can think of the following algorithm:
    
    -   By flipping the coin $n$ times, we can choose one of all subsets uniformly at random.
    -   Repeat this process until the size of the chosen subset is exactly $\dfrac n2$.
        -   Note that subsets of size $\dfrac n2$ make up at least $\dfrac 1n$ of all subsets, so the expected number of repetitions is $\leq n$.
    
    This algorithm requires $n^2$ coin flips in expectation.
    
    Another algorithm:
    
    -   We can select 1 out of $n$ at random using $2\lceil\log_2 n\rceil$ coin flips in expectation.
        -   Concretely: generate a random binary number with $\lceil\log_2 n\rceil$ digits; if it is greater than or equal to $n$, try again, otherwise select the element with the corresponding index (indices start from 0) and stop.
    -   Then we select one element from all the elements, then another one from the remaining elements, and so on, until $\dfrac n2$ elements have been selected.
    
    This algorithm requires $n\lceil\log_2 n\rceil$ coin flips in expectation.
    
    Stitching the two algorithms together:
    
    -   First, use the first algorithm to obtain a random subset.
    -   If the size of this subset is less than $\dfrac n2$, use the second algorithm to keep adding elements until the size is filled up to $\dfrac n2$.
    -   If the size of this subset exceeds $\dfrac n2$, use the second algorithm to keep removing elements until the size is cut down to $\dfrac n2$.
    
    Let us try to analyze the number of operations required in the second and third steps (i.e. the number of additions/removals of elements):
    
    -   Let the 0-1 random variable $X_i$ indicate whether $i$ is selected into the initial subset, and let $X:=X_1+\cdots+X_n$ denote the size of the subset; then the number of operations required in the second and third steps equals $\big|X-\mathrm{E}[X]\big|$. Taking $t=c\cdot\sqrt n$ in Hoeffding's inequality (where $c$ is an arbitrary constant), we get $\mathrm{Pr}\Big[\big|X-\mathrm{E}[X]\big|\geq t\Big]\leq 2\mathrm{e}^{-c^2}$. In other words, by allowing a deviation of order $\Theta(\sqrt n)$, we can obtain an arbitrarily small constant failure probability.
    
    So far we have shown that this algorithm guarantees, with high probability, that the number of coin flips is within $n+\Theta(\sqrt n\log n)$.
    
    -   Here $n$ comes from the coin flips used to obtain the initial subset, and $\Theta(\sqrt n\log n)$ is the total cost of $\Theta(\sqrt n)$ additions/removals of elements.
    
    ??? note "Computing the expected complexity"
        Let us analyze from another angle and try to compute the expected number of coin flips of this algorithm.
        
        Use Hoeffding's inequality to bound the expected number of operations in the second and third steps from above:
        
        $$
        E|X - EX| = \int_0^\infty P\{ |X - E[X]| \geq t \} \mathrm{d}t \leq 
        2 \int_0^\infty \exp \left(-\frac {t^2}{n}\right) \mathrm{d}t=\sqrt{\pi n}
        $$
        
        Hence the expected number of coin flips required in the second and third steps is $\sqrt{\pi n}\cdot2\lceil\log_2 n\rceil$.
        
        In total, this algorithm requires $n+2\sqrt{\pi n}\lceil\log_2 n\rceil$ coin flips in expectation.

### Exercise: Balls and Bins

$n$ balls are thrown independently and uniformly at random into $n$ bins. Prove that the number of balls in the fullest bin is at least $\Omega \left( \dfrac{\log n}{\log \log n} \right)$ with probability $1 - \dfrac{1}{n}$.
