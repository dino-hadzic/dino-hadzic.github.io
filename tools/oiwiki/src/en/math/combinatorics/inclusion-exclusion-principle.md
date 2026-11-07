---
title: Inclusion–exclusion principle
---

## Introduction

???+ note "Introductory example"
    Suppose that in a class $10$ students like math, $15$ students like Chinese, and $21$ students like programming. How many students in the class like at least one subject?

Is it $10+15+21=46$ students? No, because some students may like both math and Chinese, or Chinese and programming, or possibly even all three.

For convenience, denote the sets of students who like Chinese, math, and programming by $A,B,C$ respectively; then the total number of students is $|A\cup B\cup C|$. As we just said, if we simply add the numbers of elements $|A|,|B|,|C|$ of these three sets, some elements are counted more than once, so we need to subtract $|A\cap B|,|B\cap C|,|C\cap A|$; but then a small part has been subtracted too many times and needs to be added back, namely $|A\cap B\cap C|$. That is,

$$
|A\cup B\cup C|=|A|+|B|+|C|-|A\cap B|-|B\cap C|-|C\cap A|+|A\cap B\cap C|
$$

![Inclusion–exclusion principle – Venn diagram example](./images/incexcp.png)

Generalizing the problem above to the general case gives the well-known inclusion–exclusion principle.

## Definition

Suppose the elements of U have n different properties, call the i-th property $P_i$, and let the elements having property $P_i$ form the set $S_i$. Then

$$
\begin{aligned}
\left|\bigcup_{i=1}^{n}S_i\right|=&\sum_{i}|S_i|-\sum_{i<j}|S_i\cap S_j|+\sum_{i<j<k}|S_i\cap S_j\cap S_k|-\cdots\\
&+(-1)^{m-1}\sum_{a_i<a_{i+1} }\left|\bigcap_{i=1}^{m}S_{a_i}\right|+\cdots+(-1)^{n-1}|S_1\cap\cdots\cap S_n|
\end{aligned}
$$

that is,

$$
\left|\bigcup_{i=1}^{n}S_i\right|=\sum_{m=1}^n(-1)^{m-1}\sum_{a_i<a_{i+1} }\left|\bigcap_{i=1}^mS_{a_i}\right|
$$

### Proof

For every element, use the binomial theorem to compute how many times it is counted. For an element x, suppose it appears in the sets $T_1,T_2,\cdots,T_m$; then the number of times it is counted is

$$
\begin{aligned}
Cnt=&|\{T_i\}|-|\{T_i\cap T_j|i<j\}|+\cdots+(-1)^{k-1}\left|\left\{\bigcap_{i=1}^{k}T_{a_i}|a_i<a_{i+1}\right\}\right|\\
&+\cdots+(-1)^{m-1}|\{T_1\cap\cdots\cap T_m\}|\\
=&\dbinom{m}{1}-\dbinom{m}{2}+\cdots+(-1)^{m-1}\dbinom{m}{m}\\
=&\dbinom{m}{0}-\sum_{i=0}^m(-1)^i\dbinom{m}{i}\\
=&1-(1-1)^m=1
\end{aligned}
$$

So every element is counted exactly once, and putting everything together gives the union. This completes the proof.

### Complement

The **union of sets** within the universal set U can be computed with the inclusion–exclusion principle, while the intersection of sets is obtained by subtracting the **union of the complements** from the universal set:

$$
\left|\bigcap_{i=1}^{n}S_i\right|=|U|-\left|\bigcup_{i=1}^n\overline{S_i}\right|
$$

It suffices to apply inclusion–exclusion to the right-hand side.

Readers who have already met inclusion–exclusion know the material above well; what they care about more are the applications.

So next we give 3 example problems of different levels to show applications of the inclusion–exclusion principle.

## Counting nonnegative integer solutions of an indeterminate equation

???+ note "Counting nonnegative integer solutions of an indeterminate equation"
    Given the indeterminate equation $\sum_{i=1}^nx_i=m$ and $n$ constraints $x_i\leq b_i$, where $m,b_i \in \mathbb{N}$, find the number of nonnegative integer solutions of the equation.

### Without the constraints

If there are no constraints $x_i\leq b_i$, the number of nonnegative integer solutions of the indeterminate equation $\sum_{i=1}^nx_i=m$ is $\dbinom{m+n-1}{n-1}$.

Sketch of proof: stars and bars.

This is the same as distributing $m$ balls into $n$ boxes, where a box may be empty. This problem cannot be solved directly with a binomial coefficient.

So we add another $n-1$ balls; the problem then becomes choosing $n-1$ balls from a sequence of $m+n-1$ balls, and these $n-1$ balls split the sequence into $n$ parts, which correspond one-to-one to the $n$ boxes. The number of ways to choose $n-1$ balls out of $m+n-1$ balls is $\dbinom{m+n-1}{n-1}$.

### Inclusion–exclusion model

Next we try to abstract the model of the inclusion–exclusion principle:

1.  Universal set U: the nonnegative integer solutions of the indeterminate equation $\sum_{i=1}^nx_i=m$
2.  Elements: the variables $x_i$.
3.  Properties: the property of $x_i$ is the condition that $x_i$ satisfies, namely the condition $x_i\leq b_i$

Goal: the size of the set in which all variables satisfy their corresponding properties, i.e. $|\bigcap_{i=1}^nS_i|$.

This can be computed with $\left|\bigcap_{i=1}^{n}S_i\right|=|U|-\left|\bigcup_{i=1}^n\overline{S_i}\right|$. $|U|$ can be computed with a binomial coefficient, and the second part is naturally expanded with the inclusion–exclusion principle.

So the problem becomes computing the size of the intersection of some sets $\overline{S_{a_i}}$. Consider the meaning of $\overline{S_{a_i} }$: it denotes the number of solutions with $x_{a_i}\geq b_{a_i}+1$, and the intersection means that all these conditions hold simultaneously. Therefore, in the indeterminate equation corresponding to this intersection, some variables have a **lower bound**, while others have no constraint.

Can we eliminate these lower bounds? Since we want nonnegative integer solutions and the lower bounds of some variables are greater than $0$, we simply **subtract the lower bound**, which makes the lower bound of these variables $0$, i.e. no lower bound at all. Therefore, for

$$
\left|\bigcap_{a_i<a_{i+1} }^{1\leq i\leq k}S_{a_i}\right|
$$

the corresponding indeterminate equation is

$$
\sum_{i=1}^nx_i=m-\sum_{i=1}^k(b_{a_i}+1)
$$

so this can also be computed with a binomial coefficient. The array $a$ of length $k$ amounts to enumerating subsets.

## HAOI2008 硬币购物 (Coin shopping)

???+ note "HAOI2008 硬币购物 (Coin shopping)"
    There are 4 kinds of coins; the i-th kind has value $C_i$. There are $n$ queries; each query gives the number $D_i$ of coins of each kind and a price $S$, and asks for the number of ways to pay.
    
    $n\leq 10^3,S\leq 10^5$.

Solving it with a knapsack would have complexity $O(4nS)$, which is unacceptable. The most noticeable feature of this problem is that there are only four kinds of coins. Abstracting the model, we are actually asked for the number of nonnegative integer solutions of the equation $\sum_{i=1}^4C_ix_i=S,x_i\leq D_i$.

Using the same inclusion–exclusion approach, the property of $x_i$ is $x_i\leq D_i$. Plugging into the formula of the inclusion–exclusion principle, in the end we need to solve

$$
\sum_{i=1}^4C_ix_i=S-\sum_{i=1}^kC_{a_i}(D_{a_i}+1)
$$

which is an unbounded knapsack problem. This problem can be precomputed, so the total complexity including the queries is $O(4S+2^4n)$.

??? note "Implementation"
    ```cpp
    --8<-- "docs/math/code/inclusion-exclusion-principle/inclusion-exclusion-principle_1.cpp"
    ```

## Coloring subgraphs of a complete graph

The previous three problems were forward applications of the inclusion–exclusion principle; this problem requires using the inclusion–exclusion principle in reverse.

???+ note "Coloring subgraphs of a complete graph"
    A and B like coloring graphs (not necessarily connected), and their rule is that adjacent vertices must be colored with the same color. Today A and B play a game on the **complete graph** $G=(V,E)$ of order $n$. They define an evaluation function $F(S)$, where S is an edge set, $S\subseteq E$. The value of $F(S)$ is the total number of ways to color the graph $G'=(V,S)$ with $m$ colors. Their other rule is: if $|S|$ is odd, A's score increases by $F(S)$, otherwise B's score increases by $F(S)$. Find the difference between the scores of A and B.

### Mathematical form

At first glance the algorithmic direction of this problem is not obvious, so for tricky problems we first abstract the mathematical form. The score difference is a difference by parity, so a power of -1 can be used as the coefficient. We want

$$
Ans=\sum_{S\subseteq E}(-1)^{|S|-1}F(S)
$$

### Inclusion–exclusion model

We treat "adjacent vertices are colored with the same color" as a property. Here we first ignore the coloring rule and assume we color the graph directly with m colors. We treat the graph $G'=(V,S)$ as an **element**. The **property** $x_i=x_j$ means that vertices i,j have the same color (note that it is not required that there is an edge between i and j).

The **set** corresponding to the property $x_i=x_j$ is defined as $Q_{i,j}$; it consists of all colorings of graphs $G'$ satisfying this property, its size is the number of colorings satisfying the property, and its elements are the colored graphs $G'$ satisfying the property.

Back to the problem: "adjacent vertices must be colored with the same color" can be understood as the intersection of several sets $Q$. So we can write

$$
F(S)=\left|\bigcap_{(i,j)\in S}Q_{i,j}\right|
$$

The right-hand side of the formula above means the number of colorings in which $x_i=x_j$ holds for every edge $(i,j)$ in S, which is exactly $F(S)$.

Doesn't it smell like inclusion–exclusion? Since the inclusion–exclusion principle itself has no form with pairs, we map **all** edges $(i,j)$ to $T=\frac{n(n+1)}{2}$ integers: suppose $(i,j)$ is mapped to $k,1\leq k\leq T$, and at the same time $Q_{i,j}$ is mapped to $Q_k$. The property $x_i=x_j$ is then defined as $P_k$.

At the same time, S can be represented as a set of several k's, i.e. $S\iff K=\{k_1,k_2,\cdots,k_m\}$. (In other words, we have established an equivalence between edge sets and sets of numbers.)

And E corresponds to the set $M=\left\{1,2,\cdots,\frac{n(n+1)}{2}\right\}$. Hence

$$
F(S)\iff F(\{ {k_i}\})=\left|\bigcap_{k_i}Q_{k_i}\right|
$$

### Reverse analysis

Expanding the expression we want,

$$
\begin{aligned}
Ans &= \sum_{K\subseteq M}(-1)^{|K|-1}\left|\bigcap_{k_i\in K}Q_{k_i}\right|\\
    &= \sum_{i}|Q_i|-\sum_{i<j}|Q_i\cap Q_j|+\sum_{i<j<k}|Q_i\cap Q_j\cap Q_k|-\cdots+(-1)^{T-1}\left|\bigcap_{i=1}^TQ_i\right|
\end{aligned}
$$

the expanded form of the inclusion–exclusion principle appears, so we derive this expression in reverse:

$$
Ans=\left|\bigcup_{i=1}^TQ_i\right|
$$

Now consider the meaning of the right-hand side: it suffices that any one of the conditions $1\sim T$ holds, i.e. it is the number of colorings in which there exist two vertices of the same color (not necessarily adjacent)! We know that the universal set of colorings is $U$, and clearly $|U|=m^n$. Turning to the complement, we want the number of colorings in which every two vertices have different colors, namely $A_m^n=\frac{m!}{(m-n)!}$. Therefore

$$
Ans=m^n-A_m^n
$$

To solve this problem, we first abstracted the mathematical form of the problem, then started from the condition carrying the most information, the definition of the function $F(S)$, and turned it into intersections, unions and complements of sets. Then we transformed the expression into the form of the inclusion–exclusion principle and **derived in reverse** the final result. What this problem shows is precisely the reverse use of the inclusion–exclusion principle.

## Inclusion–exclusion in number theory

The inclusion–exclusion principle can elegantly solve some number-theoretic problems.

### Counting pairs with greatest common divisor k by inclusion–exclusion

Consider the following problem:

???+ note "Counting pairs with greatest common divisor $k$"
    Let $1 \le x, y \le N$, and let $f(k)$ denote the number of ordered pairs $(x, y)$ whose greatest common divisor is $k$. Find the values $f(1)$ to $f(N)$.

This problem can certainly be solved with Euler's totient function or Möbius inversion, but neither is as simple as using the inclusion–exclusion principle.

By the inclusion–exclusion principle, first find all pairs having $k$ as a **common divisor**, then remove all pairs having a multiple of $k$ as a **common divisor**; the remaining pairs are exactly those having $k$ as their **greatest common divisor**. That is, $f(k)=$ the number of pairs having $k$ as a **common divisor** $-$ the number of pairs having a multiple of $k$ as a **common divisor**.

Furthermore, the number of pairs having a multiple of $k$ as a **common divisor** equals the sum of the numbers of pairs having a multiple of $k$ as their **greatest common divisor**. So we can write the following expression:

$$
f(k)= \lfloor (N/k) \rfloor ^2 - \sum_{i=2}^{i*k \le N} f(i*k)
$$

Since for $k>N/2$ we can directly compute $f(k)= \lfloor (N/k) \rfloor ^2$, we can go backwards and compute from $f(N)$ down to $f(1)$. Thus we have solved this problem with the inclusion–exclusion principle.

```cpp
for (long long k = N; k >= 1; k--) {
  f[k] = (N / k) * (N / k);
  for (long long i = k + k; i <= N; i += k) f[k] -= f[i];
}
```

The time complexity of the method above is $O( \sum_{i=1}^{N} N/i)=O(N \sum_{i=1}^{N} 1/i)=O(N \log N)$.

As a bonus, here are three problems with the same solution to practice on.

-   [Luogu P2398 GCD SUM](https://www.luogu.com.cn/problem/P2398)
-   [Luogu P2158 \[SDOI2008\] 仪仗队 (Honor guard)](https://www.luogu.com.cn/problem/P2158)
-   [Luogu P1447 \[NOI2010\] 能量采集 (Energy collection)](https://www.luogu.com.cn/problem/P1447)

### Deriving Euler's totient function by inclusion–exclusion

Consider the following problem:

???+ note "Formula for Euler's totient function"
    Compute Euler's totient function $\varphi(n)$, where $\varphi(n)=|\{1\leq x\leq n|\gcd(x,n)=1\}|$.

Direct computation is $O(n\log n)$, the linear sieve is $O(n)$, and Du's sieve is $O(n^{\frac{2}{3}})$ (though why drag Du's sieve into an introductory number theory problem solved by inclusion–exclusion); next we derive the formula for Euler's totient function by inclusion–exclusion.

To decide whether two numbers are coprime, first factor into primes:

$$
n=\prod_{i=1}^k{p_i}^{c_i}
$$

Then we require that for every $p_i$, $x$ is not a multiple of $p_i$, i.e. $p_i\nmid x$. Treat this as a property with corresponding set $S_i$; then

$$
\varphi(n)=\left|\bigcap_{i=1}^kS_i\right|=|U|-\left|\bigcup_{i=1}^k\overline{S_i}\right|
$$

The size of the universal set is $|U|=n$, and $\overline{S_i}$ is the set determined by $p_i\mid x$, so clearly $|\overline{S_i}|=\frac{n}{p_i}$, from which it follows that

$$
\left|\bigcap_{a_i<a_{i+1}}S_{a_i}\right|=\frac{n}{\prod p_{a_i}}
$$

Hence we get

$$
\begin{aligned}
\varphi(n)&=n-\sum_{i}\frac{n}{p_i}+\sum_{i<j}\frac{n}{p_ip_j}-\cdots+(-1)^k\frac{n}{p_1p_2 \cdots p_k}\\
&=n\left(1-\frac{1}{p_1}\right)\left(1-\frac{1}{p_2}\right)\cdots\left(1-\frac{1}{p_k}\right)\\
&=n\prod_{i=1}^k\left(1-\frac{1}{p_i}\right)
\end{aligned}
$$

which is exactly the mathematical expression of Euler's totient function.

## Generalization of the inclusion–exclusion principle

The inclusion–exclusion principle is often used in counting problems on sets; for two set functions $f(S),g(S)$, if

$$
f(S)=\sum_{T\subseteq S}g(T)
$$

then

$$
g(S)=\sum_{T\subseteq S}(-1)^{|S|-|T|}f(T)
$$

### Proof

Let us prove it briefly. We start from the right-hand side of the equation:

$$
\begin{aligned}
&\sum_{T\subseteq S}(-1)^{|S|-|T|}f(T)\\
=&\sum_{T\subseteq S}(-1)^{|S|-|T|}\sum_{Q\subseteq T}g(Q)\\
=&\sum_{Q}g(Q)\sum_{Q\subseteq T\subseteq S}(-1)^{|S|-|T|}\\
\end{aligned}
$$

We notice that the second sum does not depend on $Q$, so we remove $Q$ from it:

$$
=\sum_{Q}g(Q)\sum_{T\subseteq (S\setminus Q)}(-1)^{|S\setminus Q|-|T|}
$$

Define the function of a set $P$ as $F(P)=\sum_{T\subseteq P}(-1)^{|P|-|T|}$ and simplify it:

$$
\begin{aligned}
F(P)&=\sum_{T\subseteq P}(-1)^{|P|-|T|}\\
&=\sum_{i=0}^{|P|}\dbinom{|P|}{i}(-1)^{|P|-i}=\sum_{i=0}^{|P|}\dbinom{|P|}{i}1^i(-1)^{|P|-i}\\
&=(1-1)^{|P|}=0^{|P|}
\end{aligned}
$$

So the value of the original expression is

$$
\sum_{Q}g(Q)\sum_{T\subseteq (S\setminus Q)}(-1)^{|S\setminus Q|-|T|}=\sum_{Q}g(Q)F(S\setminus Q)=\sum_{Q}g(Q)\cdot 0^{|S\setminus Q|}
$$

Analyzing this, only when $|S\setminus Q|=0$ do we have $0^0=1$; then $Q=S$ and the contribution to the answer is $g(S)$. Otherwise $0^{|S\setminus Q|}=0$, which contributes nothing. Thus we get

$$
\sum_{Q}g(Q)\cdot 0^{|S\setminus Q|}=g(S)
$$

This completes the proof.

### Corollary

This form also has the following corollary. In the universal set $U$, for functions $f(S),g(S)$, if

$$
f(S)=\sum_{S\subseteq T}g(T)
$$

then

$$
g(S)=\sum_{S\subseteq T}(-1)^{|T|-|S|}f(T)
$$

This corollary is really the complement form, and the proof is similar.

## Counting DAGs

???+ note "Counting DAGs"
    Count the labeled directed acyclic graphs on $n$ vertices, modulo $10^9+7$. $n\leq 5\times 10^3$.

### Direct DP

Consider a DP: define $f[i,j]$ as the number of DAGs with $i$ vertices in which $j$ vertices have in-degree $0$. Suppose that after removing these $j$ vertices, $k$ vertices have in-degree $0$; then before the removal each of these $k$ vertices had edges from at least some of the $j$ vertices, which gives $2^j-1$ cases; and besides the edges to these $k$ vertices, the $j$ vertices can be connected arbitrarily to the remaining vertices, which gives $2^{i-j-k}$ cases. So the recurrence is:

$$
f[i,j]=\binom{i}{j}\sum_{k=1}^{i-j}(2^j-1)^k2^{(i-j-k)j}f[i-j,k]
$$

The complexity of computing the formula above is $O(n^3)$.

### Relaxing the constraint

The definition of the DP above, exactly $j$ vertices of in-degree $0$, is too strict; it can be relaxed to at least $j$ vertices of in-degree $0$. Directly define $f[i]$ as the number of DAGs with $i$ vertices. We can apply inclusion–exclusion directly. Consider the chosen $j$ vertices: these $j$ vertices can be connected arbitrarily to the remaining $i-j$ vertices, i.e. $\left(2^{i-j}\right)^j=2^{(i-j)j}$ cases:

$$
f[i]=\sum_{j=1}^i(-1)^{j-1}\binom{i}{j}2^{(i-j)j}f[i-j]
$$

The complexity of computing the formula above is $O(n^2)$.

## Min-max inclusion–exclusion

For a sequence $\{x_i\}$ satisfying a [total order](../order-theory.md#偏序集) relation whose elements can be added and subtracted, let its length be $n$ and let $S=\{1,2,3,\cdots,n\}$; then:

$$
\max_{i\in S}{x_i}=\sum_{T\subseteq S}{(-1)^{|T|-1}\min_{j\in T}{x_j}}
$$

$$
\min_{i\in S}{x_i}=\sum_{T\subseteq S}{(-1)^{|T|-1}\max_{j\in T}{x_j}}
$$

**Proof:** Consider building a mapping to the ordinary inclusion–exclusion principle. For $x\in S$, suppose $x$ is the $k$-th smallest element. Define a mapping $f:x\mapsto \{1,2,\cdots,k\}$. Clearly this is a bijection.

Then it is easy to see that for $x,y\in S$, $f(\min(x,y))=f(x)\cap f(y)$ and $f(\max(x,y))=f(x)\cup f(y)$. Therefore we get:

$$
\begin{aligned}
\left|f\left(\max_{i\in S}{x_i}\right)\right|
&= \left| \bigcup_{i\in S} f(x_i) \right|\\
&= \sum_{T\subseteq S}(-1)^{|T|-1} \left|\bigcap_{j\in T}f(x_j)\right|\\
&= \sum_{T\subseteq S}(-1)^{|T|-1} \left|f\left(\min_{j\in T}{x_j}\right)\right|\\
\end{aligned}
$$

Then map $\left|f\left(\max_{i\in S}{x_i}\right)\right|$ back to $\max_{i\in S}{x_i}$; $\min$ is similar.

This completes the proof.

But you may find this formula very silly – the maximum can obviously be computed directly. The reason min-max inclusion–exclusion is so important is that it also holds for expectations, i.e.:

$$
E\left(\max_{i\in S}{x_i}\right)=\sum_{T\subseteq S}{(-1)^{|T|-1}E\left(\min_{j\in T}{x_j} \right)}
$$

$$
E\left(\min_{i\in S}{x_i}\right)=\sum_{T\subseteq S}{(-1)^{|T|-1}E\left(\max_{j\in T}{x_j} \right)}
$$

**Proof:** Consider one way of computing the expectation:

$$
E\left(\max_{i\in S}{x_i}\right)=\sum_{y}{P(y=x)\max_{j\in S}{y_j}}
$$

where $y$ is a sequence of length $n$.

Apply the previous formula to the $\max$ on the right:

$$
\begin{aligned}E\left(\max_{i\in S}{x_i}\right)&=\sum_{y}{P(y=x)\max_{j\in S}{y_j}}\\
&=\sum_{y}{P(y=x)\sum_{T\subseteq S}{(-1)^{|T|-1}\min_{j\in T}{y_j}}} \end{aligned}
$$

Swap the order of summation:

$$
\begin{aligned}E\left(\max_{i\in S}{x_i}\right)
&=\sum_{y}{P(y=x)\sum_{T\subseteq S}{(-1)^{|T|-1}\min_{j\in T}{y_j}}}\\
&=\sum_{T\subseteq S}{(-1)^{|T|-1}\sum_y{P(y=x)\min_{j\in T}{y_j}}}\\
&=\sum_{T\subseteq S}{(-1)^{|T|-1}E\left(\min_{j\in T}{y_j}\right)} \end{aligned}
$$

$\min$ is similar.

This completes the proof.

There is an even stronger statement:

$$
\underset{i\in S}{\operatorname{kthmax}{x_i}}=\sum_{T\subseteq S}{(-1)^{|T|-k}\dbinom {|T|-1}{k-1}\min_{j\in T}{x_j}}
$$

$$
\underset{i\in S}{\operatorname{kthmin}{x_i}}=\sum_{T\subseteq S}{(-1)^{|T|-k}\dbinom {|T|-1}{k-1}\max_{j\in T}{x_j}}
$$

$$
E\left(\underset{i\in S}{\operatorname{kthmax}{x_i}}\right)=\sum_{T\subseteq S}{(-1)^{|T|-k}\dbinom {|T|-1}{k-1}E\left(\min_{j\in T}{x_j}\right)}
$$

$$
E\left(\underset{i\in S}{\operatorname{kthmin}{x_i}}\right)=\sum_{T\subseteq S}{(-1)^{|T|-k}\dbinom {|T|-1}{k-1}E\left(\max_{j\in T}{x_j}\right)}
$$

By convention, if $n< m$ then $\dbinom nm=0$.

**Proof:** Without loss of generality assume $\forall 1\le i<n,x_i\le x_{i+1}$. Then:

$$
\begin{aligned}
\sum_{T\subseteq S}{(-1)^{|T|-k}\dbinom {|T|-1}{k-1}\min_{j\in T}{x_j}}
&=\sum_{i\in S}{x_i\sum_{T\subseteq S}{(-1)^{|T|-k}\dbinom {|T|-1}{k-1}\left[x_i=\min_{j\in T}{x_j} \right]}}\\
&=\sum_{i\in S}{x_i\sum_{j=k}^n{\dbinom {n-i}{j-1}\dbinom {j-1}{k-1}(-1)^{j-k}}}
\end{aligned}
$$

Also, by the combinatorial identity $\dbinom ab\dbinom bc=\dbinom ac\dbinom {a-c}{b-c}$, we have:

$$
\begin{aligned}
\sum_{T\subseteq S}{(-1)^{|T|-k}\dbinom {|T|-1}{k-1}\min_{j\in T}{x_j}}
&=\sum_{i\in S}{x_i\sum_{j=k}^n{\dbinom {n-i}{j-1}\dbinom {j-1}{k-1}(-1)^{j-k}}}\\
&=\sum_{i\in S}{x_i\sum_{j=k}^n{\dbinom {n-i}{k-1}\dbinom {n-i-k+1}{j-k}(-1)^{j-k}}}\\
&=\sum_{i\in S}{\dbinom {n-i}{k-1}x_i\sum_{j=k}^n{\dbinom {n-i-k+1}{j-k}(-1)^{j-k}}}\\
&=\sum_{i\in S}{\dbinom {n-i}{k-1}x_i\sum_{j=0}^{n-i-k+1}{\dbinom {n-i-k+1}j(-1)^{j}}}
\end{aligned}
$$

When $i=n-k+1$:

$$
\dbinom {n-i}{k-1}\sum_{j=0}^{n-i-k+1}{\dbinom {n-i-k+1}j(-1)^{j}}=1
$$

Otherwise:

$$
\dbinom {n-i}{k-1}\sum_{j=0}^{n-i-k+1}{\dbinom {n-i-k+1}j(-1)^{j}}=0
$$

Therefore:

$$
\sum_{i\in S}{\dbinom {n-i}{k-1}x_i\sum_{j=0}^{n-i-k+1}{\dbinom {n-i-k+1}j(-1)^{j}}}=\underset{i\in S}{\operatorname{kthmax}}{x_i}
$$

The remaining three are similar.

This completes the proof.

From min-max inclusion–exclusion we can also obtain the following formula:

$$
\underset{i\in S}{\operatorname{lcm}}{x_i}=\prod_{T\subseteq S}{\left(\gcd_{j\in T}{x_j} \right)^{(-1)^{|T|-1}}}
$$

because $\operatorname{lcm},\gcd,a^{1},a^{-1}$ correspond respectively to $\max,\min,+,-$; in other words, this is min-max inclusion–exclusion applied to the exponents, so it naturally holds.

## PKUWC2018 随机游走 (Random walk)

???+ note "[PKUWC2018 随机游走 (Random walk)](https://loj.ac/problem/2542)"
    Given a tree with $n$ vertices, you start from $x$ and at each step choose uniformly at random one of the edges incident to the current vertex and walk along it.
    
    There are $Q$ queries. Each query gives a set $S$; find the expected number of steps if, starting from $x$, you keep walking randomly until every vertex in the set $S$ has been visited at least once.
    
    In particular, the vertex $x$ (i.e. the starting point) is considered to have been visited once at the very beginning.
    
    The answer is taken modulo $998244353$.
    
    $1\le n\le 18,1\le Q\le 5000,1\le |S|\le n$.

The expected number of steps of the walk is also the time of the walk. Let the random variable $x_i$ denote the time of the first visit to vertex $i$. Then what we want is

$$
E\left(\max_{i\in S}x_i\right)
$$

By min-max inclusion–exclusion we get

$$
E\left(\max_{i\in S}x_i\right)
=E\left(\sum_{T\subseteq S}(-1)^{|T|-1}\min_{i\in T}x_i\right)
=\sum_{T\subseteq S}(-1)^{|T|-1}E\left(\min_{i\in T}x_i\right)
$$

For a set $T\in[n]$, consider computing $F(T)=E(\min_{i\in T}x_i)$.

Consider the meaning of $E(\min_{i\in T}x_i)$: it is the expected time of the first visit to some vertex in $T$. Let $f(i)$ denote the expected time to first reach some vertex in $T$ starting from vertex $i$.

-   For $i\in T$, $f(i)=0$.
-   For $i\notin T$, $f(i)=1+\frac{1}{\text{deg}(i)}\sum_{(i,j)\in E}f(j)$.

Direct Gaussian elimination has complexity $O(n^3)$, so computing $F(T)$ for every $T$ would have total complexity $O(2^nn^3)$, which is unacceptable. We use the technique of elimination on a tree.

Let the root be vertex $1$, and let the parent of vertex $u$ be $p_u$. For a leaf $i$, $f(i)$ only depends on the parent of $i$ (or possibly $f(i)=0$, which is even better). So we can write $f(i)$ in the form $f(i)=A_i+B_if(p_i)$, where $A_i,B_i$ can be computed quickly.

For a non-leaf vertex $i$, consider its sequence of children $j_1,\cdots,j_k$. Since $f(j_e)=A_{j_e}+B_{j_e}f(i)$, we get

$$
f(i)=1+\frac{1}{\deg(i)}\sum_{e=1}^k\left(A_{j_e}+B_{j_e}f(i)\right)+\frac{f(p_i)}{\deg(i)}
$$

Rearranging gives

$$
f(i)=\frac{\deg(i)+\sum_{e=1}^kA_{j_e}}{\deg(i)-\sum_{e=1}^kB_{j_e}}+
\frac{f(p_i)}{\deg(i)-\sum_{e=1}^kB_{j_e}}
$$

So we have written $f(i)$ in the form $A_i+B_if(p_i)$ as well. In this way we can work backwards all the way to the root, and the root has no parent, which means

$$
f(1)=\frac{\deg(1)+\sum_{e=1}^kA_{j_e}}{\deg(1)-\sum_{e=1}^kB_{j_e}}
$$

Solving this equation gives $f(1)$, and another top-down pass gives $f(i)$ for every vertex. Then $F(T)=f(x)$. The time complexity is $O(n)$.

In this way we can compute $F(T)$ for every $T$ in total time $O(2^nn)$.

Back to the inclusion–exclusion part: we know that $E(\max_{i\in S}x_i)=\sum_{T\subseteq S}(-1)^{|T|-1}F(T)$.

Let $F'(T)=(-1)^{|T|-1}F(T)$; then we further get $E(\max_{i\in S}x_i)=\sum_{T\subseteq S}F'(T)$. So we can use FMT (also called subset prefix sums, or the FWT OR transform) to compute $E(\max_{i\in S}x_i)$ for every $S$ in $O(2^nn)$ time, and then answer queries in $O(1)$.

### Exercises

-   [ABC331 - G - Collect Them All](https://atcoder.jp/contests/abc331/tasks/abc331_g)
-   [Luogu P4707 重返现世 (Return to the real world)](https://www.luogu.com.cn/problem/P4707)

## References

[浅探容斥原理 (A brief look at the inclusion–exclusion principle) – Wang Di](https://github.com/OI-wiki/libs/blob/master/%E9%9B%86%E8%AE%AD%E9%98%9F%E5%8E%86%E5%B9%B4%E8%AE%BA%E6%96%87/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2013%E8%AE%BA%E6%96%87%E9%9B%86.pdf), collected papers of the candidates for the Chinese national team for the informatics olympiad, 2013

[有标号的 DAG 计数系列问题 (A series of problems on counting labeled DAGs) – Cyhlnj](https://www.cnblogs.com/cjoieryl/p/10078167.html)

[Total order – Wikipedia](https://en.wikipedia.org/wiki/Total_order)
