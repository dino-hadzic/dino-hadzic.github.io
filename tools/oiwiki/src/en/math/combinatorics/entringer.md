---
title: Entringer numbers
---

## Entringer numbers

The Entringer numbers (Entringer numbers, [OEIS A008281](http://oeis.org/A008281)) $E(n,k)$ count the permutations of the $n+1$ numbers from $0$ to $n$ that satisfy the following conditions:

-   the first element is $k$;
-   the element after the first one is smaller than the first, the next element is larger than the previous one, the next one is again smaller than the previous one, and so on; the relative order of all subsequent adjacent elements follows this rule.

The initial values of the Entringer numbers are:

$$
E(0,0)=1
$$

$$
E(n,0)=0
$$

They satisfy the recurrence relation:

$$
E(n,k)=E(n,k-1)+E(n-1,n-k)
$$

## Seidel–Entringer–Arnold triangle

A suitably arranged number triangle of Entringer numbers is called the Seidel–Entringer–Arnold triangle (Seidel–Entringer–Arnold triangle, [OEIS A008280](http://oeis.org/A008280)). In this triangle the Entringer numbers $E_(n,k)$ are arranged in boustrophedon ("ox-plowing") order:

$$
\begin{aligned}
& E(0,0) \\
& E(1,0) \rightarrow E(1,1) \\
& E(2,2) \leftarrow E(2,1) \leftarrow E(2,0) \\
& E(3,0) \rightarrow E(3,1) \rightarrow E(3,2) \rightarrow E(3,3) \\
& E(4,4) \leftarrow E(4,3) \leftarrow E(4,2) \leftarrow E(4,1) \leftarrow E(4,0)
\end{aligned}
$$

That is:

$$
\begin{aligned}
& 1 \\
& 0 \rightarrow 1 \\
& 1 \leftarrow 1 \leftarrow 0 \\
& 0 \rightarrow 1 \rightarrow 2 \rightarrow 2 \\
& 5 \leftarrow 5 \leftarrow 4 \leftarrow 2 \leftarrow 0
\end{aligned}
$$

The advantage of arranging the Entringer numbers this way is that it is consistent with their recurrence relation $E(n,k)=E(n,k-1)+E(n-1,n-k)$, which makes it easy to memorize and understand.

The Entringer numbers have an exponential generating function:

$$
\sum_{m=0}^\infty\sum_{n=0}^\infty E\left(m+n,\frac{1}{2}\left(m+n+{(-1)}^{m+n}(n-m)\right)\right)\frac{x^m}{m!}\frac{x^n}{n!}=\frac{\cos x+\sin x}{\cos (x+y)}
$$

The layout of the coefficients of this generating function is in fact just a simple stretching of the Seidel–Entringer–Arnold triangle above:

$$
\begin{array}{ccccc}
E(0,0) & E(1,1) & E(2,0) & E(3,3) & E(4,0) \\
E(1,0) & E(2,1) & E(3,2) & E(4,1) & \\
E(2,2) & E(3,1) & E(4,2) & & \\
E(3,0) & E(4,3) & & & \\
E(4,4) & & & &
\end{array}
$$

That is:

$$
\begin{aligned}
& 1\quad 1\quad 0\quad 2\quad 0\\
& 0\quad 1\quad 2\quad 2\\
& 1\quad 1\quad 4\\
& 0\quad 5\\
& 5
\end{aligned}
$$

## Zigzag permutations

A zigzag permutation (zigzag permutation) is a permutation $c_1$ to $c_i$ of the numbers from $1$ to $n$ such that the value of no element $c_i$ lies between $c_{i-1}$ and $c_{i+1}$.

The number of zigzag permutations $Z_n$ ([OEIS A001250](http://oeis.org/A001250)), starting from $n=0$, is:

$$
1, 1, 2, 4, 10, 32, 122, 544, \cdots
$$

For example, the alternating permutations for the first few $n$ are:

$$
\begin{aligned}
n=1: & \{1\}\\
n=2: & \{1,2\}, \{2,1\}\\
n=3: & \{1,3,2\}, \{2,1,3\}, \{2,3,1\}, \{3,1,2\}\\
n=4: & \{1,3,2,4\}, \{1,4,2,3\}, \{2,1,4,3\}, \{2,3,1,4\}, \{2,4,1,3\}, \\
& \{3,1,4,2\}, \{3,2,4,1\}, \{3,4,1,2\}, \{4,1,3,2\}, \{4,2,3,1\}
\end{aligned}
$$

## Alternating permutations and zigzag numbers

(Note that this concept should be distinguished from "derangements".)

For $n$ greater than $1$, the reversal of every zigzag permutation is again a zigzag permutation, so they can be paired up; hence their number is necessarily even.

Here we give another way of pairing: zigzag permutations are divided into alternating permutations (alternating permutation) and reverse alternating permutations (reverse alternating permutation).

The first element of an alternating permutation is greater than the second; the order relations are:

$$
c_1>c_2<c_3>\cdots
$$

The first element of a reverse alternating permutation is smaller than the second; the order relations are:

$$
c_1<c_2>c_3<\cdots
$$

If we swap $1$ and $n$, swap $2$ and $n-1$, and so on, the set of alternating permutations and the set of reverse alternating permutations are exchanged. Therefore the number of alternating permutations equals the number of reverse alternating permutations, and each is exactly half the number of zigzag permutations.

For $n$ greater than $1$, write:

$$
A_n=\frac{Z_n}{2}
$$

Define the initial values:

$$
A_0=A_1=1
$$

These $A_n$ are called the zigzag numbers (Euler zigzag number, [OEIS A000111](http://oeis.org/A000111)); starting from $n=0$ they are:

$$
1, 1, 1, 2, 5, 16, 61, 272, \cdots
$$

Let us now try to compute $A_n$.

From the numbers $1$ to $n$, choose $k$ numbers to form a subset; there are $\dbinom{n}{k}$ ways to do this.

In this $k$-element subset, choose a reverse alternating permutation $u$; there are $A_k$ ways. In the remaining subset of $n-k$ elements, obtained by removing this $k$-element subset from the whole set, choose a reverse alternating permutation $v$; there are $A_{n-k}$ ways.

Consider the permutation $w$ of $n+1$ elements formed by taking the reversal of $u$ as the beginning, appending $n+1$, and then appending $v$. Then $w$ is certainly a zigzag permutation, and every zigzag permutation of $n+1$ elements can be cut at the element $n+1$ to obtain the corresponding reverse alternating permutations $u$ and $v$; moreover, different zigzag permutations of $n+1$ elements give different $u$ and $v$.

Hence we have the recurrence:

$$
2A_{n+1}=\sum_{k=0}^n \dbinom{n}{k} A_k A_{n-k}
$$

$$
2(n+1)\frac{A_{n+1}}{(n+1)!}=\sum_{k=0}^n \frac{A_k}{k!}\frac{A_{n-k}}{(n-k)!}
$$

When $n$ is $0$ this recurrence does not hold; the initial values $A_0$ and $A_1$ are both $1$.

Evidently this is a convolution of exponential generating functions. Suppose the exponential generating function of $A_n$ is $y$; then we have the differential equation:

$$
2\frac{\mathrm{d}y}{\mathrm{d}x}=y^2+1
$$

The $1$ added on the right-hand side handles the special case when $n$ is $0$. The general solution of this equation is:

$$
y=\tan\left(\frac{1}{2}x+C\right)
$$

Substituting that the $0$-th term is $1$, we get the particular solution:

$$
y=\tan x+\sec x
$$

The tangent function is odd and the secant function is even; their sum forms the generating function of the zigzag numbers.

## Relation between Entringer numbers and zigzag numbers

By the definition of the Entringer numbers, the Entringer number $E(n,k)$ is the number of alternating permutations of $0$ to $n$ whose first element is $k$. Therefore the Entringer numbers and the zigzag numbers are in fact related by:

$$
A_n=E(n,n)
$$

There is also a reason why $A_n$ are called "zigzag numbers": let $E_n$ be the Euler numbers (Euler number) and $B_n$ the Bernoulli numbers.

When $n$ is even, the zigzag numbers with even index are also called the "secant numbers" $S_n$ or "zig numbers". They satisfy:

$$
A_n=(-1)^{n/2}E_n
$$

The first few terms are ([OEIS A000364](http://oeis.org/A000364)):

$$
1, 1, 5, 61, 1385, \cdots
$$

When $n$ is odd, the zigzag numbers with odd index are also called the "tangent numbers" $T_n$ or "zag numbers". They satisfy:

$$
A_n=\frac{(-1)^{(n-1)/2}2^{n+1}(2^{n+1}-1)B_{n+1}}{n+1}
$$

The first few terms are ([OEIS A000182](http://oeis.org/A000182)):

$$
1, 2, 16, 272, 7936, \cdots
$$

Thus the Taylor expansions at $x=0$ give the secant numbers and the tangent numbers:

$$
\sec x=A_0+A_2\frac{x^2}{2!}+A_4\frac{x^4}{4!}+\cdots
$$

$$
\tan x=A_1x+A_3\frac{x^3}{3!}+A_5\frac{x^5}{5!}+\cdots
$$

Or, written together:

$$
\sec x+\tan x=A_0+A_1x+A_2\frac{x^2}{2!}+A_3\frac{x^3}{3!}+A_4\frac{x^4}{4!}+A_5\frac{x^5}{5!}+\cdots
$$

which forms the generating function of the zigzag numbers.

## References and links

1.  [Alternating permutation - Wikipedia](https://en.wikipedia.org/wiki/Alternating_permutation)
