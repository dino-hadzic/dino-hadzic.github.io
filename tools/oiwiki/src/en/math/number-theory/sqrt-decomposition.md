---
title: Floor-division blocks
---

Floor-division blocks (number-theoretic blocking) allow fast computation of sums of the form

$$
\sum_{i=1}^nf(i)g\left(\left\lfloor\dfrac ni\right\rfloor\right)
$$

If $\sum_{i=l}^{r}f(i)$ can be computed in $O(1)$ time, or the prefix sums of $f$ have already been precomputed, floor-division blocks can compute the value of the above sum in $O(\sqrt{n})$ time.

Floor-division blocks are often combined with techniques such as [Möbius inversion](./mobius.md).

## Idea

First, we explain the idea of floor-division blocks with a simple example. Suppose we need to count the lattice points under the hyperbola shown in the figure:

![Lattice points under a hyperbola](./images/sqrt-decomposition.svg)

This amounts to computing the sum:

$$
\sum_{i=1}^{11}\left\lfloor\dfrac{11}{i}\right\rfloor.
$$

This is the special case of the sum shown above with $f(k)=1,~g(k)=k$.

The simplest method is, of course, to compute column by column and add up, but this requires computing the number of lattice points in each of the columns $i=1,2,\cdots,11$. Looking at the figure, one can notice that these columns of points can be divided into $5$ blocks, and within each block the columns of points have the same height, forming a rectangular grid of points. Therefore, as long as we know the widths of these blocks, we can quickly finish counting by computing the sizes of these rectangular blocks.

This is the basic idea of floor-division blocks.

## Properties

This section discusses several results about dividing the lattice points under the hyperbola $y = \dfrac{n}{x}$ into blocks. Specifically, the integers between $1\sim n$ need to be divided into blocks according to the value of $\left\lfloor\dfrac{n}{i}\right\rfloor$. Let

$$
D(n) = \left\{\left\lfloor\dfrac{n}{i}\right\rfloor : 1 \le i \le n,~i\in\mathbf N_+\right\}.
$$

This is the set of all possible values of $\left\lfloor\dfrac{n}{i}\right\rfloor$.

First, there are only $O(\sqrt{n})$ such distinct values. Therefore, floor-division blocking yields only $O(\sqrt{n})$ blocks.

???+ note "Property 1"
    $|D(n)|\le 2\sqrt{n}$.

??? note "Proof"
    We distinguish two cases:
    
    -   When $i\le\sqrt{n}$, $i$ takes at most $\sqrt{n}$ values, so $\left\lfloor\dfrac{n}{i}\right\rfloor$ also takes at most $\sqrt{n}$ values.
    -   When $i>\sqrt{n}$, $\left\lfloor\dfrac{n}{i}\right\rfloor \le\dfrac{n}{i} < \sqrt{n}$ also takes at most $\sqrt{n}$ values.
    
    Therefore, the total number of all possible values is $|D(n)|\le 2\sqrt{n}$.

With a more careful analysis, the set $D(n)$ and its size can actually be described precisely.

???+ note "Property 2"
    Let $s = \lfloor\sqrt{n}\rfloor$. The elements of the set $D(n)$, in increasing order, are
    
    $$
    1 < 2 < \cdots < s-1 < s \le \left\lfloor\dfrac{n}{s}\right\rfloor < \left\lfloor\dfrac{n}{s-1}\right\rfloor < \cdots < \left\lfloor\dfrac{n}{2}\right\rfloor < \left\lfloor\dfrac{n}{1}\right\rfloor = n.
    $$
    
    Furthermore, $|D(n)| = \lfloor \sqrt{4n+1}\rfloor - 1$.

??? note "Proof"
    First, for $1 \le i \le s$, one can prove $\left\lfloor\dfrac{n}{\lfloor n/i\rfloor}\right\rfloor = i$. Let $d = \left\lfloor\dfrac{n}{i}\right\rfloor$; we need to prove $\left\lfloor\dfrac{n}{d}\right\rfloor = i$. Written as inequalities, this means that, knowing $d \le \dfrac{n}{i} < d + 1$, we need to prove $i \le \dfrac{n}{d} < i + 1$. The known condition can be written as $i\le\dfrac{n}{d} < i + \dfrac{i}{d}$, so it suffices to prove $\dfrac{i}{d} \le 1$, i.e. $i \le d = \left\lfloor\dfrac{n}{i}\right\rfloor$. This is equivalent to $i \le \dfrac{n}{i}$, which holds for all $1 \le i \le s \le \sqrt{n}$.
    
    This result actually shows that the map $i \mapsto \left\lfloor\dfrac{n}{i}\right\rfloor$ is a bijection between the set $\{i:1\le i \le s\}$ and the set $\left\{\left\lfloor\dfrac{n}{i}\right\rfloor: 1\le i\le s\right\}$. Since the $i$ are pairwise distinct, the values $\left\lfloor\dfrac{n}{i}\right\rfloor$ are pairwise distinct as well. The only elements of the two sets that can possibly coincide are $s$ and $\left\lfloor\dfrac{n}{s}\right\rfloor$. Therefore, $|D(n)|=2s - \left[s = \lfloor n/s\rfloor\right]$.
    
    To obtain the final expression for $|D(n)|$, we need to examine when $s = \left\lfloor\dfrac{n}{s}\right\rfloor$ holds.
    
    -   When $s = \left\lfloor\dfrac{n}{s}\right\rfloor$, we always have $s \le \dfrac{n}{s} < s + 1$, i.e. $s^2 \le n < s^2+s$. Then $4s^2 + 1 \le 4n + 1 < 4s^2+4s+1 = (2s+1)^2$. Since $4n+1$ is necessarily odd, the left side can be equivalently relaxed to $4s^2$, so this condition is equivalent to $2s \le \sqrt{4n+1} < 2s+1$, i.e. $\lfloor \sqrt{4n+1}\rfloor = 2s$.
    -   When $s < \left\lfloor\dfrac{n}{s}\right\rfloor$, we always have $s + 1 \le \dfrac{n}{s}$, i.e. $s^2 + s\le n$. Since also $n < (s+1)^2$, we have $s^2 + s\le n < (s+1)^2$. This is equivalent to $(2s+1)^2\le 4n+1 < 4(s+1)^2+1$. Using again that $4n+1$ is odd, the right side can be equivalently tightened to $4(s+1)^2$, so this condition is equivalent to $2s+1\le\sqrt{4n+1} < 2s+2$, i.e. $\lfloor \sqrt{4n+1}\rfloor = 2s+1$.
    
    Combining these two cases, we get that $|D(n)| = \lfloor \sqrt{4n+1}\rfloor - 1$ holds.

Next, the left and right endpoints of a single block are easy to determine.

???+ note "Property 3"
    For $d\in D(n)$, all integers $i$ satisfying $\left\lfloor\dfrac{n}{i}\right\rfloor=d$ lie in the range
    
    $$
    \left\lfloor\dfrac{n}{d+1}\right\rfloor + 1\le i \le \left\lfloor\dfrac{n}{d}\right\rfloor.
    $$

??? note "Proof"
    Because $\left\lfloor\dfrac{n}{i}\right\rfloor=d$ amounts to the inequality
    
    $$
    d\le \dfrac{n}{i} < d+1.
    $$
    
    This is further equivalent to
    
    $$
    \dfrac{n}{d+1} < i\le \dfrac{n}{d}.
    $$
    
    Using the fact that $i\in\mathbf N_+$, we can round this inequality to integers, and it is equivalent to
    
    $$
    \left\lfloor\dfrac{n}{d+1}\right\rfloor + 1 \le i\le \left\lfloor\dfrac{n}{d}\right\rfloor.
    $$

This property also reflects the symmetry of the figure: the set of right endpoints of all blocks (the green points in the figure above) is exactly $D(n)$. This is easy to understand, because the whole figure is symmetric with respect to the line $y=x$.

Besides these properties, the set $D(n)$ also has a nice recursive property:

???+ note "Property 4"
    For $m\in D(n)$, we have $D(m)\subseteq D(n)$.

??? note "Proof"
    Let $m = \left\lfloor\dfrac{n}{k}\right\rfloor$. Then, since for all $i\in\mathbf N_+$ we have
    
    $$
    \left\lfloor\dfrac{m}{i}\right\rfloor = \left\lfloor\dfrac{\lfloor n/k\rfloor}{i}\right\rfloor = \left\lfloor\dfrac{n}{ki}\right\rfloor \in D(n),
    $$
    
    it follows that $D(m)\subseteq D(n)$. Here, the second equality uses the property of the [floor function](./basic.md#取整函数) for nested fractions.

As mentioned above, $D(n)$ is both the set of values of $\left\lfloor\dfrac{n}{i}\right\rfloor$ over the blocks and the set of right endpoints of the blocks. This means that if floor-division blocks are applied recursively (i.e. the value of the function at $n$ depends on its values at $m\in D(n)\setminus\{n\}$), then the set of values and the set of right endpoints involved in the whole computation are in fact both $D(n)$. A typical example is [Du's sieve](./hyperbola.md#杜教筛).

## Procedure

Using the results of the previous section, we obtain the concrete procedure of floor-division blocks.

To compute the value of the sum

$$
\sum_{i=1}^nf(i)g\left(\left\lfloor\dfrac ni\right\rfloor\right)
$$

we can divide the indices $i=1,2,\cdots,n$ into blocks according to the value of $\left\lfloor\dfrac ni\right\rfloor$. Since the indices with the same value of $\left\lfloor\dfrac ni\right\rfloor$ form a segment of consecutive integers $[l,r]$, the value of the sum over this block is

$$
\left(\sum_{i=l}^rf(i)\right)\cdot g\left(\left\lfloor\dfrac nl\right\rfloor\right).
$$

To compute this sum quickly, we usually need to be able to compute the left sum over $f$ quickly. Sometimes the expression for this sum is known and a single computation can be done in $O(1)$ time; sometimes its prefix sums can be precomputed, and a single query can still be done in $O(1)$ time.

When computing the left and right endpoints of each block in order, the left endpoint $l$ of the current block equals the right endpoint of the previous block plus $1$, and the right endpoint of the current block equals $\left\lfloor\dfrac n{\lfloor n/l\rfloor}\right\rfloor$. From this, we obtain the following pseudocode:

$$
\begin{array}{l}
\textbf{Algorithm }\text{Sum}(f,g,n):\\
\textbf{Input. }n,~s(k)=\sum_{i=1}^kf(i),~g(k).\\
\textbf{Output. }S(n) = \sum_{i=1}^nf(i)g(\lfloor n/i\rfloor).\\
\textbf{Method.}\\
\begin{array}{ll}
1 & l \gets 1\\
2 & \textit{result} \gets 0 \\
3 & \textbf{while } l \leq n \textbf{ do}\\
4 & \qquad r \gets \left\lfloor \dfrac{n}{\lfloor n/l \rfloor} \right\rfloor\\
5 & \qquad \textit{result} \gets \textit{result} + (s(r)-s(l-1))\cdot g\left(\left\lfloor \dfrac{n}{l} \right\rfloor\right)\\
6 & \qquad l \gets r+1\\
7 & \textbf{end while}\\
8 & \textbf{return }\textit{result}
\end{array}
\end{array}
$$

Assuming that the time complexity of a single computation of $s(\cdot)$ is $O(1)$, the time complexity of the whole procedure is $O(\sqrt{n})$.

## Extensions

So far we have discussed the most common and most basic form of floor-division blocks. This section further discusses extended forms of floor-division blocks.

### Floor-division blocks with ceilings

Floor-division blocks can be used to compute sums containing ceilings:

$$
\sum_{i=1}^nf(i)g\left(\left\lceil\dfrac ni\right\rceil\right).
$$

Since $\left\lceil\dfrac ni\right\rceil = \left\lfloor\dfrac {n-1}i\right\rfloor + 1$, this sum can be converted to the floor case:

$$
f(n)g(1) + \sum_{i=1}^{n-1}f(i)g\left(\left\lfloor\dfrac {n-1}i\right\rfloor + 1\right).
$$

Note that the upper limit of summation has changed, and the term for $i=n$ appears separately.

### Multidimensional floor-division blocks

Floor-division blocks can also be used to handle sums containing more than one floor expression:

$$
\sum_{i=1}^{n}f(i)g\left(\left\lfloor\dfrac {n_1}i\right\rfloor,\left\lfloor\dfrac {n_2}i\right\rfloor,\cdots,\left\lfloor\dfrac {n_m}i\right\rfloor\right).
$$

Here, usually $n\le\min\{n_1,n_2,\cdots,n_m\}$; otherwise the case where some $\lfloor n_j/i\rfloor=0$ needs to be handled separately. To apply the idea of floor-division blocks, we need to ensure that within each block the values of all floor expressions $\left\lfloor\dfrac {n_1}i\right\rfloor,\left\lfloor\dfrac {n_2}i\right\rfloor,\cdots,\left\lfloor\dfrac {n_m}i\right\rfloor$ do not change, that is, a multidimensional block should be the intersection of all one-dimensional blocks. To this end, for a known left endpoint $l$, the corresponding right endpoint is

$$
\min\left\{\left\lfloor\dfrac {n_1}{\lfloor n_1/l\rfloor}\right\rfloor,\left\lfloor\dfrac {n_2}{\lfloor n_2/l\rfloor}\right\rfloor,\cdots,\left\lfloor\dfrac {n_m}{\lfloor n_m/l\rfloor}\right\rfloor\right\}.
$$

In other words, the minimum of the right endpoints of all one-dimensional blocks is taken as the right endpoint of the multidimensional block. This can be understood with the following figure:

![Illustration of multidimensional floor-division blocks](./images/n-dimension-sqrt-decomposition.svg)

The two-dimensional form is the most common; in that case, $r \gets \left\lfloor \dfrac{n}{\lfloor n/l \rfloor}\right\rfloor$ in the pseudocode above is replaced by

$$
r \gets \min\left\{\left\lfloor \dfrac{n_1}{\lfloor n_1/l \rfloor}\right\rfloor,\left\lfloor \dfrac{n_2}{\lfloor n_2/l \rfloor}\right\rfloor\right\}.
$$

### Floor-division blocks with arbitrary exponents

Floor-division blocks can be used to compute sums with floor expressions containing arbitrary exponents:

$$
\sum_{i=1}^{\lfloor n^{\alpha/\beta}\rfloor}f(i)g\left(\left\lfloor\dfrac {n^\alpha}{i^\beta}\right\rfloor\right).
$$

Here, $\alpha,\beta$ are positive real numbers. In the basic form discussed in this article, $\alpha=\beta=1$.

???+ note "Property"
    For a positive integer $n$ and positive real numbers $\alpha, \beta$, let
    
    $$
    D(n,\alpha,\beta) = \left\{\left\lfloor\dfrac{n^\alpha}{i^\beta}\right\rfloor: i=1,2,\cdots,\lfloor n^{\alpha/\beta}\rfloor\right\}.
    $$
    
    Then we have
    
    1.  $|D(n,\alpha,\beta)|\le 2n^{\alpha/(1+\beta)}$.
    2.  For $d\in D(n,\alpha,\beta)$, the values of $i$ for which $\left\lfloor\dfrac{n^\alpha}{i^\beta}\right\rfloor=d$ holds lie in the range
    
        $$
        \left\lfloor\dfrac{n^{\alpha/\beta}}{(d+1)^{1/\beta}}\right\rfloor + 1\le i \le \left\lfloor\dfrac{n^{\alpha/\beta}}{d^{1/\beta}}\right\rfloor.
        $$

??? note "Proof"
    For the first point, we distinguish two cases:
    
    -   When $i\le \dfrac{n^\alpha}{i^\beta}$, we have $i\le n^{\alpha/(1+\beta)}$, so $\left\lfloor\dfrac{n^\alpha}{i^\beta}\right\rfloor$ takes at most $n^{\alpha/(1+\beta)}$ values.
    -   When $i > \dfrac{n^\alpha}{i^\beta}$, we have $i> n^{\alpha/(1+\beta)}$, and hence $\dfrac{n^\alpha}{i^\beta} < n^{\alpha/(1+\beta)}$, so $\left\lfloor\dfrac{n^\alpha}{i^\beta}\right\rfloor$ also takes at most $n^{\alpha/(1+\beta)}$ values.
    
    Combining both cases, we have $|D(n,\alpha,\beta)|\le 2n^{\alpha/(1+\beta)}$.
    
    For the second point, $\left\lfloor\dfrac{n^\alpha}{i^\beta}\right\rfloor=d$ is equivalent to
    
    $$
    d \le \dfrac{n^\alpha}{i^\beta} < d+1 \iff \dfrac{n^{\alpha/\beta}}{(d+1)^{1/\beta}} < i \le \dfrac{n^{\alpha/\beta}}{d^{1/\beta}}.
    $$
    
    Rounding this inequality to integers gives the second statement.

Using these properties, floor-division blocks with arbitrary exponents can be implemented with time complexity $O(n^{\alpha/(1+\beta)})$.

???+ example "Example"
    For example, the following sum with $\alpha=\beta=1/2$
    
    $$
    \sum_{i=1}^nf(i)g\left(\left\lfloor\sqrt{\dfrac {n}{i}}\right\rfloor\right),
    $$
    
    can be solved with floor-division blocks in $O(n^{1/3})$ time. When the left endpoint of a block is $l$, the right endpoint can be computed as $r=\left\lfloor\dfrac{n}{\lfloor\sqrt{n/l}\rfloor^2}\right\rfloor$.

## Example problems

???+ example "[UVa11526 H(n)](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=27&page=show_problem&problem=2521)"
    There are $T$ test cases, each with one integer $n$. For each test case, output $\sum_{i=1}^n\left\lfloor\dfrac ni\right\rfloor$.

??? note "Solution"
    According to the analysis above, each block with the same value of $\left\lfloor\dfrac ni\right\rfloor$ can be computed at once. The time complexity is $O(T\sqrt n)$.

??? note "Implementation"
    ```cpp
    --8<-- "docs/math/code/sqrt-decomposition/sqrt-decomposition_1.cpp"
    ```

???+ example "[Codeforces 1954E Chain Reaction](https://codeforces.com/contest/1954/problem/E)"
    There is a row of $n$ monsters, and the initial health of each monster is $a_i$. One attack decreases the health of a contiguous segment of living monsters by $k$; a monster with health not greater than $0$ is considered dead. For every $k$, find the number of attacks needed to kill all monsters. Here, $n,a_i\leq 10^5$.

??? note "Solution"
    Let $a_0=0$. Suppose that killing all of the first $(i-1)$ monsters requires $T(k,i-1)$ attacks, and the health of the $i$-th monster is $a_i$. Since killing the $(i-1)$-th monster requires attacking it $\lceil a_{i-1}/k\rceil$ times, and all these attacks can be extended to the $i$-th monster, killing the $i$-th monster requires only $\max\{0,\lceil a_i/k\rceil-\lceil a_{i-1}/k\rceil\}$ more attacks. Hence, the total number of attacks is
    
    $$
    T(k,n)=\sum_{i=1}^n\max\left\{0,\left\lceil\dfrac{a_i}{k}\right\rceil-\left\lceil\dfrac{a_{i-1}}{k}\right\rceil\right\}.
    $$
    
    Since $n,k$ in the problem are both fairly large, computing this sum separately for every $k$ is not feasible. We can maintain, for each $i=1,2,\cdots,n$, the sequence $\{T(k,i)\}_k$. Initially, let $T(k,0)\equiv 0$. Suppose the sequence $\{T(k,i-1)\}_k$ is known, and consider how to modify it to obtain the sequence $\{T(k,i)\}_k$. According to the analysis above, it suffices to increase the $k$-th term of the sequence by $\max\left\{0,\left\lceil\dfrac{a_i}{k}\right\rceil-\left\lceil\dfrac{a_{i-1}}{k}\right\rceil\right\}$. Using two-dimensional floor-division blocks, this modification can be split into $O(\sqrt{a_{i-1}}+\sqrt{a_i})$ range modifications, and the value added on each range is constant. The sequence $\{T(k,n)\}_k$ obtained at the end is the answer.
    
    Since the problem involves a series of range-add operations, and queries happen only after all modifications are done, the range additions can be performed by maintaining a difference array, and the required sequence is obtained at the end by computing prefix sums. The total time complexity is $O(\max_i a_i+\sum_i\sqrt{a_i})$. Other solutions to this problem exist as well.

??? note "Implementation"
    ```cpp
    --8<-- "docs/math/code/sqrt-decomposition/sqrt-decomposition_2.cpp"
    ```

## Exercises

-   [UVa11526 H(n)](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=27&page=show_problem&problem=2521)
-   [Luogu P2261 CQOI2007 余数求和 (Sum of remainders)](https://www.luogu.com.cn/problem/P2261)
-   [Luogu P3455 POI2007 ZAP-Queries](https://www.luogu.com.cn/problem/P3455)

## References and notes

-   [杜教筛的时空复杂度分析 by riteme (Time and space complexity analysis of Du's sieve)](https://riteme.site/blog/2018-9-11/time-space-complexity-dyh-algo.html)
