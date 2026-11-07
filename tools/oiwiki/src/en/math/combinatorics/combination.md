---
title: Permutations and combinations
---

## Introduction

Permutations and combinations are the foundation of combinatorics. An arrangement (permutation) means taking a specified number of elements out of a given number of elements and ordering them; a combination means merely taking a specified number of elements out of a given number of elements, without regard to order. The central problem of permutations and combinations is to study the total number of possible arrangements and combinations that satisfy given requirements. Permutations and combinations are closely related to classical probability theory.

In high-school elementary mathematics, problems on permutations and combinations are mostly solved by methods such as tabulation and enumeration.

## Addition and multiplication principles

### Addition principle

If a job can be done in $n$ kinds of ways and $a_i(1 \le i \le n)$ denotes the number of ways of the $i$-th kind, then there are $S=a_1+a_2+\cdots +a_n$ different ways to do the job in total.

### Multiplication principle

If a job is done in $n$ steps and $a_i(1 \le i \le n)$ denotes the number of different ways to do the $i$-th step, then there are $S = a_1 \times a_2 \times \cdots \times a_n$ different ways to do the job in total.

## Basics of arrangements and combinations

### Number of arrangements

Taking any $m$ ($m\leq n$; $m$ and $n$ are natural numbers, and the same holds below) elements out of $n$ distinct elements and lining them up in a certain order is called an arrangement (k-permutation) of $m$ elements taken from $n$ distinct elements; the number of all arrangements of $m$ ($m\leq n$) elements taken from $n$ distinct elements is called the number of arrangements of $m$ elements taken from $n$ distinct elements, and is denoted by $\mathrm A_n^m$ (or $\mathrm P_n^m$).

The formula for the number of arrangements is as follows:

$$
\mathrm A_n^m = n(n-1)(n-2) \cdots (n-m+1) = \frac{n!}{(n - m)!}
$$

$n!$ denotes the factorial of $n$, e.g. $6! = 1 \times 2 \times 3 \times 4 \times 5 \times 6$.

The formula can be understood like this: out of $n$ people we choose $m$ to stand in a line ($m \le n$). For the first position we can choose $n$ people, for the second $n-1$, and so on; for the $m$-th (last) position we can choose $n-m+1$ people, which gives:

$$
\mathrm A_n^m = n(n-1)(n-2) \cdots (n-m+1) = \frac{n!}{(n - m)!}
$$

Full permutation: all $n$ people stand in a line, and the line has length $n$. For the first position we can choose $n$ people, for the second $n-1$, and so on, which gives:

$$
\mathrm A_n^n = n(n-1)(n-2) \cdots 3 \times 2 \times 1 = n!
$$

A full permutation is a special case of an arrangement.

### Number of combinations

Taking any $m \leq n$ elements out of $n$ distinct elements to form a set is called a combination of $m$ elements taken from $n$ distinct elements; the number of all combinations of $m \leq n$ elements taken from $n$ distinct elements is called the number of combinations of $m$ elements taken from $n$ distinct elements, is denoted by $\dbinom{n}{m}$, and is read "$n$ choose $m$".

Formula for the number of combinations:

$$
\dbinom{n}{m} = \frac{\mathrm A_n^m}{m!} = \frac{n!}{m!(n - m)!}
$$

How to understand the formula above? Consider choosing $m$ out of $n$ people ($m \le n$), without lining them up and without caring about order. If we cared about order the answer would be $\mathrm A_n^m$; since we do not, we have to remove the duplicates. How many duplicates are there? The same $m$ chosen people can still be "fully permuted" in $m!$ ways, hence:

$$
\begin{aligned}
\dbinom{n}{m} \times m! &= \mathrm A_n^m\\
\dbinom{n}{m} &= \frac{\mathrm A_n^m}{m!} = \frac{n!}{m!(n-m)!}
\end{aligned}
$$

The number of combinations is also often denoted by $\mathrm C_n^m$, i.e. $\displaystyle \mathrm C_n^m=\binom{n}{m}$. Nowadays the mathematical community generally uses the notation $\dbinom{n}{m}$ rather than $\mathrm C_n^m$.

The numbers of combinations are also called "binomial coefficients"; the binomial theorem below will explain the connection.

In particular, it is stipulated that $\mathrm A_n^m=\dbinom{n}{m}=0$ when $m>n$.

## Stars and bars

Stars and bars is a technique for counting the number of ways to divide identical elements into groups; it can also be used to count the number of solutions of a class of linear Diophantine equations.

### Number of sums of positive integers

Problem 1: There are $n$ **completely identical** elements, which are to be divided into $k$ groups such that every group has at least one element. How many ways are there to divide them?

Consider inserting $k - 1$ bars into the $n - 1$ gaps formed between adjacent pairs of the $n$ elements.

Since the elements are completely identical, the answer is simply $\dbinom{n - 1}{k - 1}$.

Essentially this counts the number of positive integer solutions of $x_1+x_2+\cdots+x_k=n$.

### Number of sums of nonnegative integers

Problem 2: What if the problem is changed slightly so that every group is allowed to be empty?

Obviously we cannot insert bars directly now, because many bars may be inserted into the same gap, which is very hard to count.

We try to create the conditions to reduce it to the constrained Problem 1: first borrow $k$ elements, and insert bars into the $n + k - 1$ gaps formed by these $n + k$ elements; the answer is

$$
\binom{n + k - 1}{k - 1} = \binom{n + k - 1}{n}
$$

Although this does not solve the original problem directly, this expression is exactly the answer to the original problem, which can be understood as follows:

At the beginning we borrowed $k$ elements to guarantee that every group has at least one element; after inserting the bars we take these $k$ borrowed elements back out of the $k$ groups. Since the elements are identical, the situations after the transformation and before it are in one-to-one correspondence, so the answers are equal.

From this we derive the stars and bars formula: $\dbinom{n + k - 1}{n}$.

Essentially this counts the number of nonnegative integer solutions of $x_1+x_2+\cdots+x_k=n$ (i.e. we require $x_i \ge 0$).

### Number of sums of integers with different lower bounds

Problem 3: What if we extend one step further and require that the $i$-th group receives at least $a_i,\sum a_i \le n$ elements?

Essentially this counts the number of solutions of $x_1+x_2+\cdots+x_k=n$ with $x_i \ge a_i$.

By analogy with the unconstrained case, we borrow $\sum a_i$ elements to guarantee that the $i$-th group receives at least $a_i$ elements. That is, let

$$
x_i^{\prime}=x_i-a_i
$$

and we obtain the new equation:

$$
\begin{aligned}
(x_1^{\prime}+a_1)+(x_2^{\prime}+a_2)+\cdots+(x_k^{\prime}+a_k)&=n\\
x_1^{\prime}+x_2^{\prime}+\cdots+x_k^{\prime}&=n-a_1-a_2-\cdots-a_k\\
x_1^{\prime}+x_2^{\prime}+\cdots+x_k^{\prime}&=n-\sum a_i
\end{aligned}
$$

where

$$
x_i^{\prime}\ge 0
$$

Then Problem 3 has been transformed into Problem 2, and applying the stars and bars formula directly gives the answer

$$
\binom{n - \sum a_i + k - 1}{n - \sum a_i}
$$

### Non-adjacent arrangements

Choosing $k$ of the $n$ natural numbers $1 \sim n$ such that no two of these $k$ numbers are adjacent can be done in $\dbinom {n-k+1}{k}$ ways.

## Binomial theorem

Before entering the advanced part on permutations and combinations, we first introduce a theorem closely related to binomial coefficients: the binomial theorem.

The binomial theorem describes the coefficients of an expansion:

$$
(a+b)^n=\sum_{i=0}^n\binom{n}{i}a^{n-i}b^i
$$

The proof can be done by mathematical induction, using $\dbinom{n}{k}+\dbinom{n}{k-1}=\dbinom{n+1}{k}$ in the induction step.

The binomial theorem can also easily be extended to the multinomial form:

Let $n$ be a positive integer and $x_i$ real numbers; then

$$
(x_1 + x_2 + \cdots + x_t)^n = \sum_{\text{nonnegative integer solutions of } n_1 + \cdots + n_t=n} \binom{n}{n_1,n_2,\cdots,n_t} x_1^{n_1}x_2^{n_2}\cdots x_t^{n_t}
$$

where $\dbinom{n}{n_1,n_2,\cdots,n_t}$ is the multinomial coefficient, whose properties are also very similar:

$$
\sum{\binom{n}{n_1,n_2,\cdots,n_t}} = t^n
$$

## Advanced permutations and combinations

Next we introduce some variants of permutations and combinations.

### Number of permutations of a multiset | multinomial coefficient

Please be sure to distinguish the **multinomial coefficient** from the **number of combinations of a multiset**! They are completely different concepts!

A multiset is a generalized set that may contain repeated elements. Let $S=\{n_1\cdot a_1,n_2\cdot a_2,\cdots,n_k\cdot a_k\}$ denote the multiset consisting of $n_1$ copies of $a_1$, $n_2$ copies of $a_2$, …, $n_k$ copies of $a_k$; the number of full permutations of $S$ is

$$
\frac{n!}{\prod_{i=1}^kn_i!}=\frac{n!}{n_1!n_2!\cdots n_k!}
$$

This amounts to dividing out the number of arrangements of identical elements. Concretely, you can think of having $k$ kinds of different balls, with $n_1,n_2,\cdots,n_k$ balls of each kind respectively, and $n=n_1+n_2+\ldots+n_k$. The number of full permutations of these $n$ balls is the **number of permutations of the multiset**. The number of permutations of a multiset is often called the **multinomial coefficient**. We can write the expression above with the multinomial coefficient notation:

$$
\binom{n}{n_1,n_2,\cdots,n_k}=\frac{n!}{\prod_{i=1}^kn_i!}
$$

One can see that $\dbinom{n}{m}$ is equivalent to $\dbinom{n}{m,n-m}$; the latter is merely more cumbersome and therefore not used.

### Number of combinations of a multiset 1

Let $S=\{n_1\cdot a_1,n_2\cdot a_2,\cdots,n_k\cdot a_k\}$ denote the multiset consisting of $n_1$ copies of $a_1$, $n_2$ copies of $a_2$, …, $n_k$ copies of $a_k$. Then for an integer $r(r<n_i,\forall i\in[1,k])$, the number of ways to choose $r$ elements from $S$ to form a multiset is the **number of combinations of the multiset**. This problem is equivalent to the number of nonnegative integer solutions of $x_1+x_2+\cdots+x_k=r$, which can be solved by stars and bars; the answer is

$$
\binom{r+k-1}{k-1}
$$

### Number of combinations of a multiset 2

Consider this problem: let $S=\{n_1\cdot a_1,n_2\cdot a_2,\cdots,n_k\cdot a_k,\}$ denote the multiset consisting of $n_1$ copies of $a_1$, $n_2$ copies of $a_2$, …, $n_k$ copies of $a_k$. For a positive integer $r$, find the number of ways to choose $r$ elements from $S$ to form a multiset.

Now the number of elements taken of each kind is bounded. Likewise, we can transform this problem into solving a linear equation with constraints:

$$
\forall i\in [1,k],\ x_i\le n_i,\ \sum_{i=1}^kx_i=r
$$

So the inclusion–exclusion principle naturally comes to mind. The inclusion–exclusion model is as follows:

1.  Universal set: the nonnegative integer solutions of $\displaystyle \sum_{i=1}^kx_i=r$.
2.  Properties: $x_i\le n_i$.

Let $S_i$ be the set satisfying property $i$, and $\overline{S_i}$ the set not satisfying property $i$, i.e. the set satisfying $x_i\ge n_i+1$ (which reduces to Problem 3 of stars and bars above). Then the answer is

$$
\left|\bigcap_{i=1}^kS_i\right|=|U|-\left|\bigcup_{i=1}^k\overline{S_i}\right|
$$

By the inclusion–exclusion principle, we have:

$$
\begin{aligned}
\left|\bigcup_{i=1}^k\overline{S_i}\right|
=&\sum_i\left|\overline{S_i}\right|
-\sum_{i,j}\left|\overline{S_i}\cap\overline{S_j}\right|
+\sum_{i,j,k}\left|\overline{S_i}\cap\overline{S_j}\cap\overline{S_k}\right|
-\cdots\\
&+(-1)^{k-1}\left|\bigcap_{i=1}^k\overline{S_i}\right|\\
=&\sum_i\binom{k+r-n_i-2}{k-1}
-\sum_{i,j}\binom{k+r-n_i-n_j-3}{k-1}+\sum_{i,j,k}\binom{k+r-n_i-n_j-n_k-4}{k-1}
-\cdots\\
&+(-1)^{k-1}\binom{k+r-\sum_{i=1}^kn_i-k-1}{k-1}
\end{aligned}
$$

Subtracting the expression above from the universal set $\displaystyle |U|=\binom{k+r-1}{k-1}$, we obtain the number of combinations of the multiset

$$
Ans=\sum_{p=0}^k(-1)^p\sum_{A}\binom{k+r-1-\sum_{A} n_{A_i}-p}{k-1}
$$

where A serves to enumerate subsets and satisfies $|A|=p,\ A_i<A_{i+1}$.

### Circular arrangements

All $n$ people stand in a circle; denote the number of all such arrangements by $\mathrm Q_n^n$. Consider one already formed circle: breaking it at different positions yields different lines.
Therefore we have

$$
\mathrm Q_n^n \times n = \mathrm A_n^n \Longrightarrow \mathrm Q_n = \frac{\mathrm A_n^n}{n} = (n-1)!
$$

From this we get the formula for partial circular arrangements:

$$
\mathrm Q_n^r = \frac{\mathrm A_n^r}{r} = \frac{n!}{r \times (n-r)!}
$$

## Properties of binomial coefficients | binomial corollaries

Since binomial coefficients are very important in competitive programming (OI), we introduce some of their properties here.

$$
\binom{n}{m}=\binom{n}{n-m}\tag{1}
$$

This amounts to taking the complement of the chosen set with respect to the universal set, so the value does not change. (Symmetry.)

$$
\binom{n}{k} = \frac{n}{k} \binom{n-1}{k-1}\tag{2}
$$

A recurrence derived from the definition.

$$
\binom{n}{m}=\binom{n-1}{m}+\binom{n-1}{m-1}\tag{3}
$$

The recurrence for binomial coefficients (the formula of Pascal's triangle, known in China as Yang Hui's triangle). We can use this formula to compute binomial coefficients in $O(n^2)$ time.

$$
\binom{n}{0}+\binom{n}{1}+\cdots+\binom{n}{n}=\sum_{i=0}^n\binom{n}{i}=2^n\tag{4}
$$

This is a special case of the binomial theorem. Taking $a=b=1$ gives the formula above.

$$
\sum_{i=0}^n(-1)^i\binom{n}{i}=[n=0]\tag{5}
$$

Another special case of the binomial theorem; take $a=1, b=-1$. The special case of this formula is $n=0$, when the result is $1$.

$$
\sum_{i=0}^k \binom{n}{i}\binom{m}{k-i} = \binom{m+n}{k}\tag{6}
$$

A formula for splitting binomial coefficients, used when dealing with some data structure problems. It is called [Vandermonde's identity](https://en.wikipedia.org/wiki/Vandermonde%27s_identity).

$$
\sum_{i=0}^n\binom{n}{i}^2=\binom{2n}{n}\tag{7}
$$

This is a special case of $(6)$; just take $n=k=m$.

$$
\sum_{i=0}^ni\binom{n}{i}=n2^{n-1}\tag{8}
$$

A weighted sum formula; it can be proved by differentiating the polynomial function corresponding to $(4)$.

$$
\sum_{i=0}^ni^2\binom{n}{i}=n(n+1)2^{n-2}\tag{9}
$$

Similar to the previous formula, it can be proved by differentiating the polynomial function.

$$
\sum_{l=0}^n\binom{l}{k} = \binom{n+1}{k+1}\tag{10}
$$

It can be proved by combinatorial analysis, considering the $k+1$-subsets of $S=\{a_1, a_2, \cdots, a_{n+1}\}$ one by one; it is quite commonly used in identity proofs. It is called the [hockey-stick identity (Zhu Shijie's identity)](https://en.wikipedia.org/wiki/Hockey-stick_identity).

$$
\binom{n}{r}\binom{r}{k} = \binom{n}{k}\binom{n-k}{r-k}\tag{11}
$$

It can be proved from the definition.

$$
\sum_{i=0}^n\binom{n-i}{i}=F_{n+1}\tag{12}
$$

where $F$ is the Fibonacci sequence.

$$
\binom{n+k}{k}^2=\sum_{j=0}^k\binom{k}{j}^2\binom{n+2k-j}{2k}\tag{13}
$$

It can be proved via $(6)$. It is called the [Li Shanlan identity](https://en.wikipedia.org/wiki/Li_Shanlan_identity).

## Binomial inversion

Let $f_n$ denote the number of ways to form a certain structure using exactly $n$ distinct elements, and $g_n$ the total number of ways to choose $i \geq 0$ elements out of $n$ distinct elements and form the certain structure from them.

If $f_n$ is known and we want $g_n$, then obviously:

$$
g_n = \sum_{i = 0}^{n} \binom{n}{i} f_i
$$

If $g_n$ is known and we want $f_n$, then:

$$
f_n = \sum_{i = 0}^{n} \binom{n}{i} (-1)^{n-i} g_i
$$

The above process of finding $f_n$ from a known $g_n$ is called **binomial inversion**.

### Proof

Expanding $g_i$ in the inversion formula gives:

$$
\begin{aligned}
f_n &= \sum_{i = 0}^{n} \binom{n}{i} (-1)^{n-i} \left[\sum_{j = 0}^{i} \binom{i}{j} f_j\right] \\
&= \sum_{i = 0}^{n}\sum_{j = 0}^{i}\binom{n}{i}\binom{i}{j} (-1)^{n-i}f_j
\end{aligned}
$$

Enumerating $j$ first and then $i$, we get:

$$
\begin{aligned}
f_n &= \sum_{j = 0}^{n}\sum_{i = j}^{n}\binom{n}{i}\binom{i}{j} (-1)^{n-i}f_j \\
&= \sum_{j = 0}^{n}f_j\sum_{i = j}^{n}\binom{n}{i}\binom{i}{j} (-1)^{n-i}
\end{aligned}
$$

Using formula (11) from ["Properties of binomial coefficients | binomial corollaries"](#properties-of-binomial-coefficients--binomial-corollaries), we get:

$$
\begin{aligned}
f_n &= \sum_{j = 0}^{n}f_j\sum_{i = j}^{n}\binom{n}{j}\binom{n - j}{i - j} (-1)^{n-i} \\
&= \sum_{j = 0}^{n}\binom{n}{j}f_j\sum_{i = j}^{n}\binom{n - j}{i - j} (-1)^{n-i}
\end{aligned}
$$

Let $k = i - j$. Then $i = k + j$, and the expression above becomes:

$$
f_n = \sum_{j = 0}^{n}\binom{n}{j}f_j\sum_{k = 0}^{n - j}\binom{n - j}{k} (-1)^{n-j-k}1^{k}
$$

Using formula (5) from ["Properties of binomial coefficients | binomial corollaries"](#properties-of-binomial-coefficients--binomial-corollaries), we get:

$$
f_n = \sum_{j = 0}^{n}\binom{n}{j}f_j[n = j] = f_n
$$

This completes the proof.
