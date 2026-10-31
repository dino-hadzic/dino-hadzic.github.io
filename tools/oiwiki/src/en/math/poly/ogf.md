---
title: Ordinary generating function
---

The ordinary generating function (OGF) of a sequence $a$ is defined as the formal power series:

$$
F(x)=\sum_{n}a_n x^n
$$

The sequence $a$ may be finite or infinite. Common examples (assuming $a$ starts at index $0$):

1.  The ordinary generating function of the sequence $a=\langle 1,2,3\rangle$ is $1+2x+3x^2$.
2.  The ordinary generating function of the sequence $a=\langle 1,1,1,\cdots\rangle$ is $\sum_{n\ge 0}x^n$.
3.  The generating function of the sequence $a=\langle 1,2,4,8,16,\cdots\rangle$ is $\sum_{n\ge 0}2^nx^n$.
4.  The generating function of the sequence $a=\langle 1,3,5,7,9,\cdots\rangle$ is $\sum_{n\ge 0}(2n+1)x^n$.

In other words, if the sequence $a$ has a closed formula for its general term, the coefficients of its ordinary generating function are exactly that formula.

## Basic operations

Consider two sequences $a,b$ with ordinary generating functions $F(x),G(x)$. Then

$$
F(x)\pm G(x)=\sum_n (a_n\pm b_n)x^n
$$

so $F(x)\pm G(x)$ is the ordinary generating function of the sequence $\langle a_n\pm b_n\rangle$.

Consider multiplication, that is, convolution:

$$
F(x)G(x)=\sum_n x^n \sum_{i=0}^na_ib_{n-i}
$$

so $F(x)G(x)$ is the ordinary generating function of the sequence $\langle \sum_{i=0}^n a_ib_{n-i} \rangle$.

## Closed form

When working with generating functions we do not always keep the formal power series form; at suitable moments we convert to a closed form to simplify more easily.

For example, for the ordinary generating function $F(x)=\sum_{n\ge 0}x^n$ of $\langle 1,1,1,\cdots\rangle$ we can observe that

$$
F(x)x+1=F(x)
$$

Solving this equation gives

$$
F(x)=\frac{1}{1-x}
$$

This is the closed form of $\sum_{n\ge 0}x^n$.

Consider the generating function $F(x)=\sum_{n\ge 0}p^nx^n$ of the geometric sequence $\langle 1,p,p^2,p^3,p^4,\cdots\rangle$; we have

$$
\begin{aligned}F(x)px+1 &=F(x)\\F(x) &=\frac{1}{1-px}\end{aligned}
$$

Switching between the closed form and the expanded form of a geometric sequence is a frequently used tool.

???+ note "Small exercise"
    Find the ordinary generating functions (both as formal power series and in closed form) of the following sequences. The difficulty increases gradually.
    
    1.  $a=\langle 0,1,1,1,1,\cdots\rangle$.
    2.  $a=\langle 1,0,1,0,1,\cdots \rangle$.
    3.  $a=\langle 1,2,3,4,\cdots \rangle$.
    4.  $a_n=\binom{m}{n}$ ($m$ is a constant, $n\ge 0$).
    5.  $a_n=\binom{m+n}{n}$ ($m$ is a constant, $n\ge 0$).

??? note "Answers"
    The first one:
    
    $$
    F(x)=\sum_{n\ge 1}x^n=\dfrac{x}{1-x}
    $$
    
    The second one:
    
    $$
    \begin{aligned}
    F(x)&=\sum_{n\ge 0}x^{2n}\\
    &=\sum_{n\ge 0}(x^2)^{n}\\
    &=\frac{1}{1-x^2}
    \end{aligned}
    $$
    
    The third one (differentiation):
    
    $$
    \begin{aligned}F(x)&=\sum_{n\ge 0}(n+1)x^n\\&=\sum_{n\ge 1}nx^{n-1}\\&=\sum_{n\ge 0}(x^n)'\\&=\left(\frac{1}{1-x}\right)'\\&=\frac{1}{(1-x)^2}\end{aligned}
    $$
    
    The fourth one (binomial theorem):
    
    $$
    F(x)=\sum_{n\ge 0}\binom{m}{n}x^n=(1+x)^m
    $$
    
    The fifth one:
    
    $$
    F(x)=\sum_{n\ge 0}\binom{m+n}{n}x^n=\frac{1}{(1-x)^{m+1}}
    $$
    
    This can be proved by induction.
    
    First, for $m=0$ we have $F(x)=\dfrac{1}{1-x}$.
    
    And for $m>0$ we have
    
    $$
    \begin{aligned}
    \frac{1}{(1-x)^{m+1}}
    &=\frac{1}{(1-x)^m}\frac{1}{1-x}\\
    &=\left(\sum_{n\ge 0}\binom{m+n-1}{n}x^n \right)\left(\sum_{n\ge 0}x^n \right)\\
    &=\sum_{n\ge 0} x^n\sum_{i=0}^n \binom{m+i-1}{i}\\
    &=\sum_{n\ge 0}\binom{m+n}{n}x^n
    \end{aligned}
    $$

## Generating function of the Fibonacci sequence

Next we derive the generating function of the Fibonacci sequence.

The Fibonacci sequence is defined by $a_0=0,a_1=1,a_n=a_{n-1}+a_{n-2}\;(n>1)$. Let its ordinary generating function be $F(x)$; then, from the recurrence, we can similarly set up an equation for $F(x)$:

$$
F(x)=xF(x)+x^2F(x)-a_0x+a_1x+a_0
$$

Solving gives

$$
F(x)=\frac{x}{1-x-x^2}
$$

The next question is: how do we find its expanded form?

### First way of expanding

Treat $x+x^2$ as a whole; then we get

$$
\begin{aligned}
F(x) &= \dfrac{x}{1-(x+x^2)} \\
&= x\sum_{k=0}^{\infty}(x+x^2)^k \\
&= x\sum_{k=0}^{\infty}\sum_{i=0}^k\binom{k}{i}x^{k-i}(x^2)^i \\
&= \sum_{k=0}^{\infty}\sum_{i=0}^k\binom{k}{i}x^{k+i+1} \\
&= \sum_{n=1}^{\infty}\sum_{i=0}^{\lfloor(n-1)/2\rfloor}\binom{n-i-1}{i}x^n.
\end{aligned}
$$

In the last step we set $n=k+i+1$ and swapped the order of summation. From this we obtain the formula for the general term:

$$
a_n = \sum_{i=0}^{\lfloor(n-1)/2\rfloor}\binom{n-i-1}{i}.
$$

This is not the well-known form involving the golden ratio.

### Second way of expanding

Consider solving an equation with undetermined coefficients:

$$
\frac{A}{1-ax}+\frac{B}{1-bx}= \frac{x}{1-x-x^2}
$$

Bringing to a common denominator gives

$$
\frac{A-Abx+B-aBx}{(1-ax)(1-bx)} = \frac{x}{1-x-x^2}
$$

Equating the coefficients, we get

$$
\begin{cases}
A+B=0\\
-Ab-aB=1\\
a+b=1\\
ab=-1
\end{cases}
$$

Solving gives

$$
\begin{cases}
A=\frac{1}{\sqrt{5}}\\
B=-\frac{1}{\sqrt{5}}\\
a=\frac{1+\sqrt{5}}{2}\\
b=\frac{1-\sqrt{5}}{2}
\end{cases}
$$

Then, by the expansion of a geometric sequence, we obtain the formula for the general term of the Fibonacci sequence:

$$
\frac{x}{1-x-x^2}=\sum_{n\ge 0}x^n
\frac{1}{\sqrt{5}}\left( \left(\frac{1+\sqrt{5}}{2}\right)^n-\left(\frac{1-\sqrt{5}}{2}\right)^n \right)
$$

This is also called another closed form of the Fibonacci sequence ($\frac{x}{1-x-x^2}$ is one closed form).

For arbitrary polynomials $P(x),Q(x)$, the expansion of the generating function $\dfrac{P(x)}{Q(x)}$ can be found by the method above. In practice we usually first find the roots of $Q(x)$, write the denominator in the form $\prod (1-p_ix)^{d_i}$, and then determine the numerators.

When the factorization of the denominator has repeated roots, each extra multiplicity requires one more fraction. For example, consider the formula for the general term of the coefficients of the generating function

$$
G(x)=\frac{1}{(1-x)(1-2x)^2}
$$

Then we have

$$
G(x)=\frac{c_0}{1-x}+\frac{c_1}{1-2x}+\frac{c_2}{(1-2x)^2}
$$

Solving gives

$$
\begin{cases}
c_0&=1\\
c_1&=-2\\
c_2&=2
\end{cases}
$$

so

$$
[x^n]G(x)=1-2^{n+1}+(n+1)\cdot 2^{n+1}
$$

## Newton's binomial theorem

We redefine the binomial coefficient:

$$
\binom{r}{k}=\frac{r^{\underline{k}}}{k!}\quad(r\in\mathbf{C},k\in\mathbf{N})
$$

Note that $r$ ranges over the complex numbers. In this setting, for $\alpha\in\mathbf{C}$ we have

$$
(1+x)^{\alpha}=\sum_{n\ge 0}\binom{\alpha}{n}x^n
$$

The binomial theorem is actually a special case of Newton's binomial theorem.

## Generating function of the Catalan numbers

See [the algebraic derivation of the Catalan numbers](../combinatorics/catalan.md#algebraic-derivation).

## Applications

Next we give some example problems to show concrete applications of generating functions in OI.

### 食物 (Food)

???+ note "[食物 (Food)](https://hydro.ac/p/bzoj-P3028)"
    Choose $n$ items from many different kinds of food, where each kind is restricted as follows:
    
    1.  Chengde hamburger: an even number
    2.  cola: 0 or 1
    3.  chicken drumstick: 0, 1 or 2
    4.  peach juice: an odd number
    5.  chicken nuggets: a multiple of 4
    6.  baozi (steamed buns): 0, 1, 2 or 3
    7.  stir-fried potato with meat: at most one.
    8.  bread: a multiple of 3
    
    Every kind of food is counted "per item"; any selection whose total number of items is $n$ counts as one way. For the given $n$, compute the number of ways modulo $10007$.

This is a classic generating function problem. For one kind of food, let $a_n$ denote the number of ways to choose $n$ items of that food, and find its generating function. The generating function of the number of ways to choose $n$ items in total from two kinds of food is exactly the convolution of their generating functions. The generating function of the number of ways to choose $n$ items from several kinds of food is likewise the convolution of their generating functions.

Having understood that the number of ways can be expressed as a convolution, we can construct the generating functions (the numbers correspond to the numbers of the foods in the problem):

1.  $\displaystyle\sum_{n\ge 0}x^{2n}=\dfrac{1}{1-x^2}$.
2.  $1+x$.
3.  $1+x+x^2=\dfrac{1-x^3}{1-x}$.
4.  $\dfrac{x}{1-x^2}$.
5.  $\displaystyle \sum_{n\ge 0}x^{4n}=\dfrac{1}{1-x^4}$.
6.  $1+x+x^2+x^3=\dfrac{1-x^4}{1-x}$.
7.  $1+x$.
8.  $\dfrac{1}{1-x^3}$.

Multiplying everything together, we get the generating function of the answer:

$$
F(x)=\frac{(1+x)(1-x^3)x(1-x^4)(1+x)}{(1-x^2)(1-x)(1-x^2)(1-x^4)(1-x)(1-x^3)}
=\frac{x}{(1-x)^4}
$$

Then we convert it into expanded form (using the fifth exercise from the closed-form exercises):

$$
F(x)=\sum_{n\ge 1}\binom{n+2}{n-1}x^n
$$

So the answer is $\dbinom{n+2}{n-1}=\dbinom{n+2}{3}$.

### Sweet

???+ note "[[CEOI2004] Sweet](https://hydro.ac/p/bzoj-P3027)"
    There are $n$ piles of candies. Candies in different piles are of different kinds (i.e., candies in the same pile are of the same kind, and candies in different piles are of different kinds). The $i$-th pile contains $m_i$ candies. You want to eat at least $a$ but at most $b$ candies. Find the number of ways.
    
    Two ways are different if and only if the number of candies eaten differs, or, for some kind of candy, the number of candies of that kind eaten differs between the two ways.
    
    $n\le 10,0\le a\le b\le 10^7,m_i\le 10^6$.

The generating function of the number of ways to eat $j$ candies from the $i$-th pile (obviously 1) is

$$
F_i(x)=\sum_{j=0}^{m_i}x^j=\frac{1-x^{m_i+1}}{1-x}
$$

so the generating function of the number of ways to eat $i$ candies in total is

$$
G(x)=\prod_{i=1}^n F_i(x)=(1-x)^{-n}\prod_{i=1}^n(1-x^{m_i+1})
$$

What we want is $\sum_{i=a}^b[x^i]G(x)$.

Since $n\le 10$, we can expand $\prod_{i=1}^n(1-x^{m_i+1})$ by brute force (at most $2^n$ terms).

Then apply Newton's binomial theorem to $(1-x)^{-n}$:

$$
\begin{aligned}
(1-x)^{-n}
&=\sum_{i\ge 0}\binom{-n}{i}(-x)^i\\
&=\sum_{i\ge 0}\binom{n-1+i}{i}x^i
\end{aligned}
$$

We enumerate the coefficient of $x^k$ in $\prod_{i=1}^n(1-x^{m_i+1})$, say $c_k$. After multiplying by $(1-x)^{-n}$, its contribution to the answer is

$$
c_k\sum_{i=a-k}^{b-k}\binom{n-1+i}{i}=c_k\left(
\binom{n+b-k}{b-k}-
\binom{n+a-k-1}{a-k-1}
\right)
$$

This way the answer can be computed in $O(b)$.

The time complexity is $O(2^n+b)$.
