---
title: Euclidean-like algorithm
---

## Introduction

The Euclidean-like algorithm (类欧几里得算法) was presented by Hong Huadun in 2016 during the participants' exchange at the winter camp (冬令营). It is often used to solve summation problems for sequences (indexed by $i$) of the form

$$
\left\lfloor\dfrac{ai+b}{c}\right\rfloor
$$

Its main idea is to use the recursive structure of fractions themselves to reduce the problem to one of smaller size and solve it recursively. Since the recursive structure of fractions is directly [related](./continued-fraction.md#computing-the-continued-fraction-representation) to the [Euclidean algorithm](./gcd.md#euclidean-algorithm), this summation method is also called the Euclidean-like algorithm.

Since [continued fractions](./continued-fraction.md) and the [Stern–Brocot tree](./stern-brocot.md) also describe the recursive structure of fractions, problems that can be solved with the Euclidean-like algorithm can usually be solved with these methods as well. Compared with them, the Euclidean-like algorithm is usually easier to understand, and its implementation is also more concise.

## Euclidean-like algorithm

The simplest example is the summation problem:

$$
f(a,b,c,n)=\sum_{i=0}^n\left\lfloor \frac{ai+b}{c} \right\rfloor,
$$

where $a,b,c,n$ are all positive integers.

### Algebraic approach

First, taking $a,b$ modulo $c$ simplifies the problem and reduces it to the case $0\le a,b<c$:

$$
\begin{aligned}
f(a,b,c,n)&=\sum_{i=0}^n\left\lfloor \frac{ai+b}{c} \right\rfloor\\
&=\sum_{i=0}^n\left\lfloor
\frac{\left(\left\lfloor\frac{a}{c}\right\rfloor c+(a\bmod c)\right)i+\left(\left\lfloor\frac{b}{c}\right\rfloor c+(b\bmod c)\right)}{c}\right\rfloor\\
&=\sum_{i=0}^n\left(\left\lfloor\frac{a}{c}\right\rfloor i+\left\lfloor\frac{b}{c}\right\rfloor+\left\lfloor\frac{\left(a\bmod c\right)i+\left(b\bmod c\right)}{c}
\right\rfloor\right)\\
&=\frac{n(n+1)}{2}\left\lfloor\frac{a}{c}\right\rfloor
+(n+1)\left\lfloor\frac{b}{c}\right\rfloor+f(a\bmod c,b\bmod c,c,n).
\end{aligned}
$$

Now consider the transformed problem. Let

$$
m = \left\lfloor \frac{an+b}{c} \right\rfloor.
$$

Then the original problem can be written as a double sum:

$$
\sum_{i=0}^n\left\lfloor \frac{ai+b}{c} \right\rfloor
=\sum_{i=0}^n\sum_{j=0}^{m-1}\left[j<\left\lfloor \frac{ai+b}{c} \right\rfloor\right].
$$

We swap the order of summation; for this, we need to compute, for each $j$, the range of $i$ satisfying the condition. To that end, we rewrite the condition:

$$
\begin{aligned}
&j<\left\lfloor \frac{ai+b}{c} \right\rfloor = \left\lceil \frac{ai+b+1}{c} \right\rceil-1\\
&\iff j + 1 < \left\lceil \frac{ai+b+1}{c} \right\rceil
\iff j+1< \frac{ai+b+1}{c} \\
&\iff \dfrac{cj+c-b-1}{a} < i
\iff \left\lfloor\dfrac{cj+c-b-1}{a}\right\rfloor < i.
\end{aligned}
$$

The rewriting repeatedly uses the properties of the [rounding functions](./basic.md#floor-and-ceiling-functions) (floor and ceiling). Substituting the rewritten condition, the original expression can be written as:

$$
\begin{aligned}
f(a,b,c,n)&=\sum_{j=0}^{m-1}
\sum_{i=0}^n\left[i>\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor \right]\\
&=\sum_{j=0}^{m-1}\left(n-\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor\right)\\
&=nm-f\left(c,c-b-1,a,m-1\right).
\end{aligned}
$$

Let $(a',b',c',n')=(c,c-b-1,a,m-1)$; this brings us back to the case $a'>c'$ discussed earlier.

Combining these two steps, we see that during the process, $(a,c)$ are repeatedly reduced modulo each other and swapped until $a=0$. This resembles the Euclidean algorithm of repeated division applied to $(a,c)$, which is where the Euclidean-like algorithm gets its name. Its time complexity is $O(\log\min\{a,c\})$.

During the computation, the case $m=0$ may occur; then the inner recursion has $n=-1$. This does not affect the final result. However, if the algorithm is terminated immediately when $m=0$ occurs, its time complexity can be improved to $O(\log\min\{a,c,n\})$.

??? note "Explanation of the complexity"
    Using the similarity between this algorithm and the Euclidean algorithm, it is easy to show that its time complexity is $O(\log\min\{a,c\})$. Therefore, it suffices to show that if the algorithm terminates at $m=0$, its time complexity is also $O(\log n)$.
    
    Let $m=\lfloor(an+b)/c\rfloor$, and write $S=mn$, $k=m/n$; they correspond, respectively, to the area of the lattice of points and the slope of the line in the geometric intuition (see the next section). For sufficiently large $n$, approximately $k\doteq a/c$.
    
    Consider how $S$ and $k$ change during the algorithm. In the first step, the modulo reduction, $n$ stays unchanged, $k$ approximately changes from $a/c$ to $(a\bmod c)/c$, which corresponds to the slope changing from $k$ to $k-\lfloor k\rfloor$, and $S$ is approximately multiplied by $(k-\lfloor k\rfloor)/k$. In the second step, swapping the coordinate axes, $S$ stays approximately unchanged, while $k$ becomes its reciprocal. Therefore, if after these two steps the pair $(k,S)$ becomes $(k',S')$, then $k'=(k-\lfloor k\rfloor)^{-1}$ and $S'=\dfrac{k-\lfloor k\rfloor}{k}S\le (k-\lfloor k\rfloor)S$, because from the second round on, we always have $k\ge 1$ at the beginning of each round.
    
    Since $1\le\lfloor k'\rfloor\le k'<\lfloor k'\rfloor+1$, after two rounds of recursion $S$ is multiplied by at most
    
    $$
    (k'-\lfloor k'\rfloor)(k-\lfloor k\rfloor) = 1-\dfrac{\lfloor k'\rfloor}{k'} < 1-\dfrac{\lfloor k'\rfloor}{\lfloor k'\rfloor+1} = \dfrac{1}{\lfloor k'\rfloor+1}\le \dfrac{1}{2}.
    $$
    
    Therefore, the algorithm necessarily terminates after at most $O(\log S)$ rounds. Since from the second round on, the $S$ at the beginning of each round never exceeds the $S$ at the end of the modulo reduction of the previous round, and the latter is roughly $kn^2$ with $k<1$, we have $O(\log S)\subseteq O(\log n)$. This proves the claim above.

A reference implementation of the template problem follows:

??? example "Template problem implementation ([Library Checker - Sum of Floor of Linear](https://judge.yosupo.jp/problem/sum_of_floor_of_linear))"
    ```cpp
    --8<-- "docs/math/code/euclidean/euclidean-0.cpp:full-text"
    ```

### Geometric intuition

This algorithm can also be understood from a geometric point of view. The problems that the Euclidean-like algorithm can solve are mainly problems of counting lattice points below a line.

As shown in the leftmost part of the figure below, the sum corresponds to the number of lattice points below the line

$$
y = \dfrac{ax+b}{c}
$$

and above the $x$-axis (not including the $x$-axis) whose abscissa lies in $[0,n]$.

![](./images/euclidean-1.svg)

First, we remove the integer parts of the slope and the intercept. This step corresponds to counting the blue points in the middle part of the figure above separately. When the slope and the intercept are both integers, the blue points necessarily form a trapezoidal array, that is, the lattice points in different columns form an arithmetic progression, so the number of these points is easy to compute. After removing these points, the number of remaining lattice points equals the number of red points in the rightmost part of the figure above. The problem is thus reduced to the case where both the slope and the intercept are less than one. Since the height of the trapezoid is $n+1$ and the lengths of its two bases are $\lfloor b/c\rfloor$ and $(\lfloor a/c\rfloor n+\lfloor b/c\rfloor)$, respectively, by the formula for the area of a trapezoid this step can be summarized by the formula

$$
f(a,b,c,n) = f(a\bmod c,b\bmod c,c,n) + \dfrac{1}{2}(n+1)\left(\left\lfloor\dfrac{b}{c}\right\rfloor+\left(\left\lfloor\dfrac{a}{c}\right\rfloor n+\left\lfloor\dfrac{b}{c}\right\rfloor\right)\right).
$$

Next, we swap the coordinate axes. As shown in the leftmost part of the figure below, the red and blue points together form a rectangular lattice of points with width $n$ and height $m=\lfloor(an+b)/c\rfloor$. To count the red points, it suffices to count the blue points and subtract that from the number of points in the rectangular lattice. After the swap, the blue lattice in the left part of the figure becomes a red lattice below some line. Moreover, after the swap the slope is greater than one, so we are back to the case already handled above.

![](./images/euclidean-2.svg)

The key is how to compute the equation of the line above the new red lattice. Swapping the coordinate axes in the leftmost part of the figure above yields its middle part. The line above the red lattice after the swap (the solid line in the middle part) does not correspond to the line before the swap (the solid line in the leftmost part), but is the result of shifting the line before the swap slightly to the upper left (the dashed line in the leftmost part). This is because if we swapped the line (the solid line in the leftmost part) directly, we would get the dashed line in the middle part, but by definition the lattice points below it include the lattice points lying exactly on the line, which would cause the points on the line to be counted twice. To avoid this, the line $y=(cx-b)/a$ obtained by swapping the axes of the line $y=(ax+b)/c$ needs to be shifted slightly downward to the line $y=(cx-b-1)/a$, so that the lattice below it is exactly the blue lattice before the swap.

There is another detail to handle. The intercept of the line in the middle part of the figure above is negative, which means we have not yet returned to the initial situation. To make the intercept non-negative again, it suffices to shift the line (the solid line in the middle part) one unit to the left. Doing so does not miss any lattice point, because the blue lattice before the swap has no points with ordinate zero, so after the swap there are no points with abscissa zero. Finally, the equation of the line becomes $y=(cx+c-b-1)/a$; at the same time, the upper bound of the abscissas of the lattice changes from $m$ to $m-1$. This step can be summarized by the formula

$$
f(a,b,c,n) = mn - f(c,c-b-1,a,m-1).
$$

This recursive algorithm works mainly for two reasons:

-   First, the slope of the line repeatedly has its fractional part taken and then its reciprocal, which is equivalent to computing the [continued fraction expansion](./continued-fraction.md#computing-the-continued-fraction-representation) of the slope $k=a/c$ of the line. Since the length of the continued fraction expansion of a rational fraction is $O(\log\min\{a,c\})$, this process necessarily terminates after $O(\log\min\{a,c\})$ steps;
-   Second, since the slope of the line is less than one every time the coordinate axes are swapped, intuitively we should have $m<n$, that is, after each such round of iteration the range of abscissas keeps shrinking. The rigorous analysis in the complexity computation above shows that after every two rounds of iteration, $S=mn$ is at most half of what it was, so this process necessarily terminates after $O(\log n)$ steps.

This is also why the complexity of the Euclidean-like algorithm is $O(\log\min\{a,c,n\})$ when the slope is rational.

Using similar geometric intuition, the Euclidean-like algorithm can be generalized to the case of an irrational slope; for a detailed analysis, see the example problem below.

### Example problems

???+ example "[【模板】类欧几里得算法 (Template: Euclidean-like algorithm)](https://www.luogu.com.cn/problem/P5170)"
    Multiple queries. Given positive integers $a,b,c,n$, compute
    
    $$
    \begin{aligned}
    f(a,b,c,n) &= \sum_{i=0}^n\left\lfloor \frac{ai+b}{c} \right\rfloor,\\
    g(a,b,c,n) &= \sum_{i=0}^ni\left\lfloor \frac{ai+b}{c} \right\rfloor,\\
    h(a,b,c,n) &= \sum_{i=0}^n\left\lfloor \frac{ai+b}{c} \right\rfloor^2.
    \end{aligned}
    $$

??? note "Solution 1"
    Similarly to the derivation for $f$, we can obtain recursive expressions for $g,h$.
    
    First, using modulo reduction, we reduce the problem to the case $0\le a,b<c$:
    
    $$
    \begin{aligned}
    g(a,b,c,n)
    &=g(a\bmod c,b\bmod c,c,n)+\left\lfloor\frac{a}{c}\right\rfloor\frac{n(n+1)(2n+1)}{6}+\left\lfloor\frac{b}{c}\right\rfloor\frac{n(n+1)}{2}, \\
    h(a,b,c,n)&=h(a\bmod c,b\bmod c,c,n)\\
    &\quad+2\left\lfloor\frac{b}{c}\right\rfloor f(a\bmod c,b\bmod c,c,n)
    +2\left\lfloor\frac{a}{c}\right\rfloor g(a\bmod c,b\bmod c,c,n)\\
    &\quad+\left\lfloor\frac{a}{c}\right\rfloor^2\frac{n(n+1)(2n+1)}{6}+\left\lfloor\frac{b}{c}\right\rfloor^2(n+1)
    +\left\lfloor\frac{a}{c}\right\rfloor\left\lfloor\frac{b}{c}\right\rfloor n(n+1).
    \end{aligned}
    $$
    
    Then, by swapping the order of summation, we can transform further. As before, let
    
    $$
    m = \left\lfloor \frac{an+b}{c} \right\rfloor.
    $$
    
    Then, for the sum $g$, we have
    
    $$
    \begin{aligned}
    g(a,b,c,n)&=\sum_{i=0}^ni\left\lfloor \frac{ai+b}{c} \right\rfloor\\
    &=\sum_{i=0}^n \sum_{j=0}^{m-1}i
    \left[j<\left\lfloor\frac{ai+b}{c}\right\rfloor\right] \\
    &=\sum_{j=0}^{m-1}\sum_{i=0}^n i\left[i>\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor \right]\\
    &=\sum_{j=0}^{m-1}\dfrac{1}{2}\left(\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor+n+1\right)\left(n-\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor\right)\\
    &=\dfrac{1}{2}mn(n+1) - \dfrac{1}{2}\sum_{j=0}^{m-1}\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor - \dfrac{1}{2}\sum_{j=0}^{m-1}\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor^2\\
    &=\dfrac{1}{2}mn(n+1) - \dfrac{1}{2}f(c,c-b-1,a,m-1) - \dfrac{1}{2}h(c,c-b-1,a,m-1).
    \end{aligned}
    $$
    
    For the sum $h$, we have
    
    $$
    \begin{aligned}
    h(a,b,c,n)&=\sum_{i=0}^n\left\lfloor \frac{ai+b}{c} \right\rfloor^2\\
    &=\sum_{i=0}^n\sum_{j=0}^{m-1}(2j+1)\left[j<\left\lfloor\frac{ai+b}{c}\right\rfloor\right]\\
    &=\sum_{j=0}^{m-1}\sum_{i=0}^n(2j+1)\left[i>\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor \right]\\
    &=\sum_{j=0}^{m-1}(2j+1)\left(n-\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor\right)\\
    &=nm^2 - \sum_{j=0}^{m-1}\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor - 2\sum_{j=0}^{m-1}j\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor\\
    &=nm^2 - f(c,c-b-1,a,m-1) - 2g(c,c-b-1,a,m-1).
    \end{aligned}
    $$
    
    From the geometric point of view, these nonlinear sums correspond to assigning a weight $w(i,j)$ to each point $(i,j)$ in the region. Apart from these weights, the rest of the computation is exactly the same. For the choice of weights, in general we have
    
    $$
    \sum_{i=0}^ni^r\left\lfloor \frac{ai+b}{c} \right\rfloor^s = \sum_{i=0}^n\sum_{j=0}^{m-1} i^r\left((j+1)^s-j^s\right)\left[j<\left\lfloor\frac{ai+b}{c}\right\rfloor\right].
    $$
    
    Another feature of this problem is that $g$ and $h$ are intertwined in the recursive computation. Therefore, $(f,g,h)$ must be computed recursively together as a triple.
    
    ```cpp
    --8<-- "docs/math/code/euclidean/euclidean-1.cpp"
    ```

???+ example "[\[清华集训 2014\] Sum (Tsinghua Training Camp 2014)](https://www.luogu.com.cn/problem/P5172)"
    Multiple queries. Given positive integers $n$ and $r$, compute
    
    $$
    \sum_{d=1}^n(-1)^{\lfloor d\sqrt{r}\rfloor}.
    $$

??? note "Solution 1"
    If $r$ is a perfect square, then the sum equals $n$ when $\sqrt{r}$ is even; otherwise, depending on the parity of $n$, the sum alternates between $0$ and $-1$. Below we consider the case where $r$ is not a perfect square.
    
    To apply the Euclidean-like algorithm, we first transform the sum into the familiar form:
    
    $$
    \begin{aligned}
    \sum_{d=1}^n(-1)^{\lfloor d\sqrt{r}\rfloor} &= \sum_{d=1}^n\left(1 - 2(\lfloor d\sqrt{r}\rfloor\bmod 2)\right)\\
    &= n - 2\sum_{d=1}^n\left(\lfloor d\sqrt{r}\rfloor - 2\left\lfloor\dfrac{\lfloor d\sqrt{r}\rfloor}{2}\right\rfloor\right) \\
    &= n - 2\sum_{d=1}^n\lfloor d\sqrt{r}\rfloor + 4 \sum_{d=1}^n\left\lfloor\dfrac{d\sqrt{r}}{2}\right\rfloor\\
    &= n - 2f(1,0,1,n) + 4f(1,0,2,n).
    \end{aligned}
    $$
    
    Here the function $f$ has the form
    
    $$
    f(a,b,c,n) = \sum_{i=1}^n\left\lfloor\dfrac{a\sqrt{r}+b}{c}i\right\rfloor.
    $$
    
    Unlike the algorithm in the main text, the slope here is no longer rational. Let the slope be
    
    $$
    k = \dfrac{a\sqrt{r}+b}{c}.
    $$
    
    Again we distinguish two cases. If $k\ge 1$, then
    
    $$
    \begin{aligned}
    f(a,b,c,n) &= \sum_{i=1}^n \lfloor ki\rfloor = \sum_{i=1}^n \lfloor(k-\lfloor k\rfloor)i\rfloor + \lfloor k\rfloor \sum_{i=1}^ni\\
    &= \lfloor k\rfloor\dfrac{n(n+1)}{2} + f(a,b-c\lfloor k\rfloor,c,n).
    \end{aligned}
    $$
    
    The problem reduces to the case where the slope is less than one. If $k<1$, let $m=\lfloor nk\rfloor$; then
    
    $$
    \begin{aligned}
    f(a,b,c,n) &= \sum_{i=1}^n \lfloor ki\rfloor = \sum_{i=1}^n\sum_{j=1}^m[j\le\lfloor ki\rfloor]\\
    &= \sum_{j=1}^m\sum_{i=1}^n[i>\lfloor k^{-1}j\rfloor] = nm - \sum_{j=1}^m\sum_{i=1}^n[i\le\lfloor k^{-1}j\rfloor].
    \end{aligned}
    $$
    
    The condition for swapping $i$ and $j$ in this derivation is simpler than in the main text because the line $y=kx$ has no lattice points other than the origin. The key is to write the sum after the swap in the form $f(a,b,c,n)$, which requires $a',b',c'$ to satisfy
    
    $$
    k^{-1} = \dfrac{a'\sqrt{r}+b'}{c'}.
    $$
    
    This is not hard: it suffices to rationalize the denominator, which gives
    
    $$
    k^{-1} = \dfrac{c}{a\sqrt{r}+b} = \dfrac{ca\sqrt{r}-cb}{a^2r-b^2}.
    $$
    
    Therefore,
    
    $$
    a'=ca,~b'=-cb,~c'=a^2r-b^2.
    $$
    
    This shows that
    
    $$
    f(a,b,c,n) = nm - f(ca,-cb,a^2r-b^2,m).
    $$
    
    To avoid integer overflow, $a,b,c$ must be divided by their greatest common divisor every time. Since this computation coincides exactly with computing the continued fraction of $k$, by the [theory of continued fractions](./continued-fraction.md#quadratic-irrationals), as long as $\gcd(a,b,c)=1$ is guaranteed, they necessarily stay within the integer range during the computation. Moreover, although $(a,b,c,n)$ does not overflow, under the constraints of this problem $f(a,b,c,n)$ may exceed the range of $64$-bit integers; natural overflow is fine and needs no extra handling, since the final result is guaranteed to lie in $[-n,n]$.
    
    Although the slope never becomes zero, the complexity of the algorithm is still $O(\log n)$, which is easy to see from the earlier argument about the algorithm's complexity.
    
    ```cpp
    --8<-- "docs/math/code/euclidean/euclidean-2.cpp"
    ```

???+ example "[Fraction](https://www.luogu.com.cn/problem/P5179)"
    Given positive integers $a,b,c,d$, among all irreducible fractions $p/q$ satisfying $a/b<p/q<c/d$, find the one with the lexicographically smallest $(q,p)$.

??? note "Solution"
    This problem is also a classic application of the [Stern–Brocot tree](./stern-brocot.md); the corresponding solution can be found [here](./continued-fraction.md#the-tree-of-continued-fractions). Since it depends only on the recursive structure of fractions, it can likewise be solved with a method similar to the Euclidean algorithm, and thus can also be regarded as an application of the Euclidean-like algorithm.
    
    If there is at least one natural number between $a/b$ and $c/d$ (endpoints excluded), we can directly take $(q,p)=(1,\lfloor a/b\rfloor+1)$. Otherwise, we necessarily have
    
    $$
    \left\lfloor\dfrac{a}{b}\right\rfloor \le \dfrac{a}{b} <\dfrac{p}{q} <\dfrac{c}{d}\le\left\lfloor\dfrac{a}{b}\right\rfloor+1.
    $$
    
    From this inequality we see that the integer part of $p/q$ is determined to be $\lfloor a/b\rfloor$; we remove this integer part directly and then take the reciprocal of the whole expression to determine its fractional part. This is exactly the [basic method](./continued-fraction.md#computing-the-continued-fraction-representation) for determining the continued fraction of $p/q$. If the final answer is $p/q$, the time complexity of the algorithm is $O(\log\min\{p,q\})$.
    
    There is one detail here: whether the lexicographically smallest fraction obtained after taking reciprocals is also the lexicographically smallest fraction before taking reciprocals. In other words, among the fractions $p/q$ satisfying $a/b<p/q<c/d$, whether the one with the lexicographically smallest $(q,p)$ is also the one with the lexicographically smallest $(p,q)$. Suppose not: let $p/q$ have the lexicographically smallest $(q,p)$, but $r/s\neq p/q$ have the lexicographically smallest $(r,s)$. Then necessarily $r<p$ and $q<s$. But this means
    
    $$
    \dfrac{a}{b} < \dfrac{r}{s} < \dfrac{r}{q} < \dfrac{p}{q} < \dfrac{c}{d}.
    $$
    
    Therefore, $r/q$ is strictly smaller than the current solution in either lexicographic order. This contradicts the assumption. Hence the above algorithm is correct.
    
    ```cpp
    --8<-- "docs/math/code/euclidean/euclidean-3.cpp"
    ```

## Universal Euclidean algorithm

The derivations of the Euclidean-like algorithm discussed in the previous section are usually rather tedious, and the sums it can handle are mainly those that can be transformed into (weighted) lattice point counting below a line. This section discusses a more general method that further abstracts the above process and can therefore solve more problems. For this reason, the method is also called the universal Euclidean algorithm (万能欧几里得算法). It also uses the recursive structure of fractions to solve problems, but its way of reducing the problem differs somewhat from that of the Euclidean-like algorithm.

We still consider the most classic summation problem:

$$
f(a,b,c,n)=\sum_{i=1}^n\left\lfloor \frac{ai+b}{c} \right\rfloor,
$$

where $a,b,c,n$ are all positive integers.

### Problem transformation

Let the line segment with parameters $(a,b,c,n)$ be

$$
y = \frac{ax+b}{c},~0< x\le n.
$$

For this segment, we can define a string $S$ consisting of $U$ and $R$, also called the **operation sequence**, as follows:

-   the string consists of exactly $n$ copies of $R$ and $m=\lfloor(an+b)/c\rfloor$ copies of $U$;
-   the number of $U$'s before the $i$-th $R$ is exactly $\lfloor(ai+b)/c\rfloor$, where $i=1,\cdots,n$.

Geometrically, this roughly corresponds to the following: starting from the origin, every time we cross a vertical grid line to the right, we write an $R$, and every time we cross a horizontal grid line upward, we write a $U$. As shown in the figure below:

![](./images/euclidean-universal.svg)

Of course, such a definition still needs to consider a series of special cases:

-   when passing through a lattice point (i.e., crossing upward and to the right at the same time), we write $U$ first and then $R$;
-   at the beginning of the string, in addition to the number of upward grid line crossings in the interval $(0,1]$, an extra $\lfloor b/c\rfloor$ copies of $U$ must be added;
-   at the end of the string, there must be no extra $U$'s.

If anything in the geometric description is unclear, the algebraic definition above can be consulted to aid understanding. The geometric description helps in understanding the algorithm procedure below.

The basic idea of the universal Euclidean algorithm is to regard $U$ and $R$ in the operation sequence as elements of some [monoid](../algebra/basic.md#群), to regard the whole operation sequence as a product of elements of the monoid, and the final answer to the problem is related to this product.

For example, in this problem we can define the state vector $v = (1,y,\sum y)$, representing the current state after crossing a number of grid lines upward and to the right starting from the origin. Here the first component is a constant, the second component is the ordinate $y$, and the third component is the required sum. Initially, $v=(1,0,0)$. Every time we cross a grid line upward, the ordinate increases by one, which corresponds to multiplying the state vector on the right by the matrix

$$
U = \begin{pmatrix}1 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{pmatrix}.
$$

Every time we cross a grid line to the right, the sum accumulates the current ordinate, which corresponds to multiplying the state vector on the right by the matrix

$$
R = \begin{pmatrix}1 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1\end{pmatrix}.
$$

Therefore, the final state is the product $(1,0,0)S$, where $S$ is understood as the product of the matrices above. The required answer is the third component of the final state.

Besides defining the elements of the monoid as matrices, we can also define them as the contribution of a segment of the operation sequence to the final result, and define the product of operations as the merging of the contributions of two segments of the operation sequence.

In this problem, we can define the contribution of each segment of the operation sequence as $(x,y,\sum y)$. To explain this notation rigorously, these components can all be viewed as functions of the operation sequence; that is, for an operation sequence $S$, its contribution can be written as $(x(S),y(S),(\sum y)(S))$. Here $x(S)$ and $y(S)$ correspond to the numbers of $R$'s and $U$'s in the operation sequence $S$, respectively, that is, the numbers of times the segment crosses grid lines to the right and upward. The summation sign in the last component is generally defined as follows: for a function $f(S)$ on operation sequences, we can define $(\sum f)(S)$, also written $\sum_S f$, as the following expression:

$$
\sum_S f := \sum\{f(S_{[1,r]}):S_r=R\}.
$$

Here $S_r$ is the $r$-th character of $S$, and $S_{[1,r]}$ is the prefix of $S$ consisting of its first $r$ characters. In other words, this summation sign can be viewed as a sum over all prefixes of the operation sequence $S$ that end with $R$. For example, we have

$$
\sum_S 1 = x,~ \sum_S x = \dfrac{1}{2}x(x+1).
$$

As another example, $\sum y$ is the accumulation, at each rightward grid line crossing in the operation sequence, of the number of upward grid line crossings so far. For the whole operation sequence, the values of $y$ at all prefixes ending with $R$ are exactly the values $\lfloor(ai+b)/c\rfloor$ at $i=1,\cdots,n$. Therefore, the $\sum y$ computed for the whole operation sequence is exactly the quantity required in this problem.

The two operations are $U=(0,1,0)$ and $R=(1,0,0)$, respectively. Further, the product of two elements $(x_1,y_1,s_1)$ and $(x_2,y_2,s_2)$ can be defined as

$$
(x_1,y_1,s_1)\cdot (x_2,y_2,s_2) = (x_1+x_2,y_1+y_2,s_1+s_2+x_2y_1).
$$

Here the result of merging the contributions in the last component can be obtained by the following computation:

$$
\sum_{S_1+S_2}y = \sum_{S_1}y + \sum_{S_2}(y+y_1) = \sum_{S_1}y + \sum_{S_2}y + y_1\sum_{S_2}1 = s_1+s_2+x_2y_1.
$$

It is easy to verify that this multiplication is associative and that the identity element is $(0,0,0)$, so these elements form a monoid under this multiplication. The required answer is the third component of the product.

Both methods yield the correct result. However, since it keeps a lot of redundant information, the matrix computation has a large constant factor, so the second method is more practical when dealing with actual problems.

### Algorithm procedure

Unlike the Euclidean-like algorithm, which reduces the problem as a whole, the universal Euclidean algorithm reduces the problem by merging these operations in batches. Denote the product of the operations corresponding to the string by

$$
F(a,b,c,n,U,R).
$$

The reduction process is as follows:

-   When $b\ge c$, the operation sequence begins with $\lfloor b/c\rfloor$ copies of $U$; we compute their product directly and remove these $U$'s from the operation sequence. Then the number of $U$'s before the $i$-th $R$ equals

    $$
    \left\lfloor\dfrac{ai+b}{c}\right\rfloor - \left\lfloor\dfrac{b}{c}\right\rfloor = \left\lfloor\dfrac{ai+(b\bmod c)}{c}\right\rfloor.
    $$

    Therefore, this corresponds to changing the segment parameters from $(a,b,c,n)$ to $(a,b\bmod c,c,n)$. So, in this case, we have

    $$
    F(a,b,c,n,U,R) = U^{\lfloor b/c\rfloor}F(a,b\bmod c,c,n,U,R).
    $$

-   When $a\ge c$, every $R$ in the operation sequence is preceded by at least $\lfloor a/c\rfloor$ copies of $U$, which can be merged into the $R$. That is, we can replace $R$ with $U^{\lfloor a/c\rfloor}R$. In the merged string, the number of $U$'s before the $i$-th $R$ equals

    $$
    \left\lfloor\dfrac{ai+b}{c}\right\rfloor - \left\lfloor\dfrac{a}{c}\right\rfloor i = \left\lfloor\dfrac{(a\bmod c)i+b}{c}\right\rfloor.
    $$

    Therefore, this corresponds to changing the segment parameters from $(a,b,c,n)$ to $(a\bmod c,b,c,n)$. So, in this case, we have

    $$
    F(a,b,c,n,U,R) = F(a\bmod c,b,c,n,U,U^{\lfloor a/c\rfloor}R).
    $$

-   In the remaining case, we need to swap the coordinate axes, which is essentially swapping $U$ and $R$, except that the parameters of the segment after the swap must be computed carefully. From the definition of the operation sequence, we need to determine coefficients $(a',b',c',n')$ such that in the operation sequence before the transformation, the number of $R$'s before the $j$-th $U$ is exactly $\lfloor(a'j+b')/c'\rfloor$ and there are $n'$ copies of $U$ in total. By definition,

    $$
    n'=\left\lfloor\dfrac{an+b}{c}\right\rfloor = m,
    $$

    and the number of $R$'s before the $j$-th $U$ equals the largest $i$ such that

    $$
    \begin{aligned}
    \left\lfloor\dfrac{ai+b}{c}\right\rfloor < j 
    &\iff \dfrac{ai+b}{c} < j \iff i < \dfrac{cj-b}{a} \\
    &\iff i < \left\lceil\dfrac{cj-b}{a}\right\rceil = \left\lfloor\dfrac{cj-b - 1}{a}\right\rfloor + 1.
    \end{aligned}
    $$

    Therefore, $i = \lfloor(cj-b-1)/a\rfloor$. This derivation is similar to the derivation of the Euclidean-like algorithm above, and likewise uses the properties of the floor and ceiling functions.

    There are two details to handle:

    -   The intercept term $-(b+1)/a$ is negative. Note that shifting the segment one unit to the left restores a non-negative intercept, since we always have $(c-b-1)/a\ge 0$. Therefore, we can extract the first part $R^{\lfloor(c-b-1)/a\rfloor}U$ of the sequence before the swap, and swap $U$ and $R$ only in the remaining operation sequence;
    -   After swapping $U$ and $R$, there are extra $U$'s at the end. Therefore, before swapping $U$ and $R$, we first need to extract the last run of $R$'s, and swap $U$ and $R$ only in the remaining operation sequence. The number of $R$'s in this run is $n-\lfloor(cm-b-1)/a\rfloor$.

    After removing some characters from the beginning and the end, the number of $R$'s before the $j$-th $U$ becomes:

    $$
    \left\lfloor\dfrac{c(j+1)-b-1}{a}\right\rfloor - \left\lfloor\dfrac{c-b-1}{a}\right\rfloor = \left\lfloor\dfrac{cj+(c-b-1)\bmod a}{a}\right\rfloor.
    $$

    Recall that the number of $U$'s in the sequence before the swap is $m = \lfloor(an+b)/c\rfloor$. The above shift by one unit to the left requires that there be at least one $U$ before the swap, that is, $m>0$. Using this condition, we distinguish two cases:

    -   For $m>0$, after handling the two points above, the operation sequence with $U$ and $R$ swapped is exactly the valid sequence corresponding to the segment with parameters $(c,(c-b-1)\bmod a,a,m-1)$. So we have

        $$
        F(a,b,c,n,U,R) = R^{\lfloor(c-b-1)/a\rfloor}UF(c,(c-b-1)\bmod a,a,m-1,R,U)R^{n-\lfloor(cm-b-1)/a\rfloor}.
        $$

    -   In particular, for $m=0$, the operation sequence before the swap contains only $n$ copies of $R$; no swap is needed, and we can return directly

        $$
        F(a,b,c,n,U,R) = R^n.
        $$

        Unlike the Euclidean-like algorithm, this special case of the universal Euclidean algorithm must be handled separately; otherwise the computation would be incorrect because negative exponents would be involved.

Using these observations, the problem can be solved recursively.

Suppose that the time complexity of a single multiplication of elements in the monoid is $O(1)$. Then, if all the powers of these elements during the computation are calculated with [binary exponentiation](../binary-exponentiation.md), the final complexity of the algorithm is $O(\log\max\{a,c\}+\log(b/c))$[^complexity].

??? note "Explanation of the complexity"
    Compared with the Euclidean(-like) algorithm, the universal Euclidean algorithm only adds the steps of binary exponentiation. The complexity of the rest of the computation is similar to that of the Euclidean-like algorithm and has already been shown to be $O(\log\min\{a,c,n\})$. Now we need to compute the total complexity of these binary exponentiations.
    
    Except in the first round of iteration, we always have $b<c$, so each of these rounds involves three binary exponentiations, with total complexity:
    
    $$
    O\left(\log\left\lfloor\dfrac{a}{c}\right\rfloor+\log\left\lfloor\dfrac{c-b_1-1}{a_1}\right\rfloor+\log\left(n-\left\lfloor\dfrac{cm-b_1-1}{a_1}\right\rfloor\right)\right),
    $$
    
    where $a_1=a\bmod c$, $b_1=b\bmod c$ and $m=\lfloor(a_1n+b_1)/c\rfloor$. For the last two terms, we have the respective estimates:
    
    $$
    \begin{aligned}
    \dfrac{c-b_1-1}{a_1} &\le \dfrac{c}{a_1},\\
    n-\left\lfloor\dfrac{cm-b_1-1}{a_1}\right\rfloor &\le n - \dfrac{cm-b_1-1}{a_1} + 1 \\
    &\le n - \dfrac{c((a_1n+b_1)/c-1)-b_1-1}{a_1} +1 \\
    &= \dfrac{c+1}{a_1}+1.
    \end{aligned}
    $$
    
    Therefore, the complexity of both of these terms is $O(\log(c/a_1))$.
    
    In each round of iteration, the segment parameters change from $(a,\cdot,c,\cdot)$ to $(c,\cdot,a\bmod c,\cdot)$, and the total time complexity of that round is
    
    $$
    O\left(\log\dfrac{a}{c}+\log\dfrac{c}{a\bmod c}\right).
    $$
    
    Over all rounds of the recursion, these terms telescope, so the final total complexity is $O(\log a+\log c)=O(\log\max\{a,c\})$.
    
    Finally, adding the complexity $O(\log(b/c))$ of the binary exponentiation $U^{\lfloor b/c\rfloor}$ in the first round of iteration, we obtain the total complexity $O(\log\max\{a,c\}+\log(b/c))$.

The procedure of the universal Euclidean algorithm can be written as a unified template; when dealing with a specific problem, only the implementation of the template type `T` needs to be changed.

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/math/code/euclidean/euclidean-4.cpp:euclidean"
    ```

Using the universal Euclidean algorithm, the template problem can be implemented as follows:

??? example "Template problem implementation ([Library Checker - Sum of Floor of Linear](https://judge.yosupo.jp/problem/sum_of_floor_of_linear))"
    ```cpp
    --8<-- "docs/math/code/euclidean/euclidean-4.cpp:full-text"
    ```

### Example problems

???+ example "[【模板】类欧几里得算法 (Template: Euclidean-like algorithm)](https://www.luogu.com.cn/problem/P5170)"
    Multiple queries. Given positive integers $a,b,c,n$, compute
    
    $$
    \begin{aligned}
    f(a,b,c,n) &= \sum_{i=0}^n\left\lfloor \frac{ai+b}{c} \right\rfloor,\\
    g(a,b,c,n) &= \sum_{i=0}^ni\left\lfloor \frac{ai+b}{c} \right\rfloor,\\
    h(a,b,c,n) &= \sum_{i=0}^n\left\lfloor \frac{ai+b}{c} \right\rfloor^2.
    \end{aligned}
    $$

??? note "Solution 2"
    To apply the template of the universal Euclidean algorithm, we first extract the term $i=0$ and consider it separately. The remaining part can be viewed as computing $\sum y,\sum xy,\sum y^2$ for the segment with parameters $(a,b,c,n)$. As stated in the main text, there are two ways to convert the operation sequence into elements of a monoid.
    
    **Matrix computation**: the state vector is defined as $(1,x,y,xy,y^2,\sum y,\sum xy,\sum y^2)$. The initial state is $(1,0,0,0,0,0,0,0)$, and the two operations are, respectively,
    
    $$
    U =
    \begin{pmatrix}
    1 & 0 & 1 & 0 & 1 & 0 & 0 & 0 \\
    0 & 1 & 0 & 1 & 0 & 0 & 0 & 0 \\
    0 & 0 & 1 & 0 & 2 & 0 & 0 & 0 \\
    0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 
    \end{pmatrix},~
    R = 
    \begin{pmatrix}
    1 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 1 & 1 & 0 & 1 & 1 & 0 \\
    0 & 0 & 0 & 1 & 0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 0 & 1 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 
    \end{pmatrix}.
    $$
    
    The final answer consists of the last three components of the vector obtained by multiplying the initial state on the right by the product of these operation matrices.
    
    This approach has a huge constant factor and cannot pass this problem; the details are given here only to aid understanding.
    
    **Contribution merging**: the contribution of a segment of the operation sequence is defined as $(x,y,\sum y,\sum xy,\sum y^2)$. The two operations are, respectively,
    
    $$
    U = (0,1,0,0,0),~ R = (1,0,0,0,0).
    $$
    
    When merging contributions, we have
    
    $$
    \begin{aligned}
    \sum_{S_1+S_2} y 
    &= \sum_{S_1}y + \sum_{S_2}(y+y_1) = \sum_{S_1}y + \sum_{S_2}y + x_2y_1,\\
    \sum_{S_1+S_2} xy
    &= \sum_{S_1}xy + \sum_{S_2}(x+x_1)(y+y_1) \\
    &= \sum_{S_1}xy + \sum_{S_2}xy + x_1\sum_{S_2}y + y_1\sum_{S_2}x + x_1y_1\sum_{S_2}1\\
    &= \sum_{S_1}xy + \sum_{S_2}xy + x_1\sum_{S_2}y + \dfrac{1}{2}x_2(x_2+1)y_1 + x_1x_2y_1,\\
    \sum_{S_1+S_2}y^2
    &= \sum_{S_1}y^2 + \sum_{S_2}(y+y_1)^2 \\
    &= \sum_{S_1}y^2 + \sum_{S_2}y^2 + 2y_1\sum_{S_2}y + y_1^2\sum_{S_2}1  \\
    &= \sum_{S_1}y^2 + \sum_{S_2}y^2 + 2y_1\sum_{S_2}y + x_2y_1^2.
    \end{aligned}
    $$
    
    This shows that the multiplication of operations should be defined as
    
    $$
    \begin{aligned}
    &(x_1,y_1,s_1,t_1,u_1)\cdot(x_2,y_2,s_2,t_2,u_2)\\
    &= (x_1+x_2,y_1+y_2,s_1+s_2+x_2y_1,\\
    &\qquad t_1+t_2+x_1s_2+(1/2)x_2(x_2+1)y_1+x_1x_2y_1,\\
    &\qquad u_1+u_2+2y_1s_2+x_2y_1^2).
    \end{aligned}
    $$
    
    Although direct verification is rather tedious, the contribution vectors defined above do form a monoid under this multiplication, with identity element $(0,0,0,0,0)$.
    
    For the general case, we have
    
    $$
    \begin{aligned}
    \sum_{S_1+S_2}x^ry^s &= \sum_{S_1}x^ry^s + \sum_{S_2}(x+x_1)^r(y+y_1)^s \\
    &= \sum_{S_1}x^ry^s + \sum_{i=0}^r\sum_{j=0}^s\binom{r}{i}\binom{s}{j}x_1^{r-i}y_1^{s-j}\sum_{S_2}x^iy^j.
    \end{aligned}
    $$
    
    As long as the contributions of all lower powers are maintained, sums of the general form can be computed.
    
    ```cpp
    --8<-- "docs/math/code/euclidean/euclidean-5.cpp"
    ```

???+ example "[\[清华集训 2014\] Sum (Tsinghua Training Camp 2014)](https://www.luogu.com.cn/problem/P5172)"
    Multiple queries. Given positive integers $n$ and $r$, compute
    
    $$
    \sum_{d=1}^n(-1)^{\lfloor d\sqrt{r}\rfloor}.
    $$

??? note "Solution 2"
    First, the case where $r$ is a perfect square is handled separately, exactly as before, and is omitted here. We only consider the case where $r$ is not a perfect square.
    
    There are many ways to apply the universal Euclidean algorithm to this problem. For example, we can define a linear transformation for each operation:
    
    $$
    U(x) = -x,~ R(x) = x + 1.
    $$
    
    The multiplication of operations is defined as the composition of linear transformations. Then the final answer is the value at $x=0$ of the function obtained by composing the transformations corresponding to the operation sequence.
    
    We can also define the contribution of each segment of the operation sequence. The contribution can be defined as $((-1)^y,\sum(-1)^y)$. Then the two operations are taken to be, respectively,
    
    $$
    U = (-1,0),~ R = (1,1).
    $$
    
    The merging of contributions is defined as
    
    $$
    (u_1,v_1)\cdot(u_2,v_2) = (u_1u_2,v_1+u_1v_2).
    $$
    
    It is easy to verify that under this multiplication all operations form a monoid, with identity element $(1,0)$. The final answer is the second component of the product of all elements.
    
    These two methods are equivalent, because if the linear transformation is written as $f(x)=ux+v$, the change of coefficients under composition of linear transformations is exactly the multiplication of operations defined above. In other words, these two monoids are isomorphic.
    
    In this problem, the parameters of the segment are $(k,n)$, where $k\in\mathbf R$ is the slope of the line. Let the product corresponding to the operation sequence be $F(k,n,U,R)$. Then we have the following recursive algorithm:
    
    -   If $k\ge 1$, every $R$ in the operation sequence is preceded by at least $\lfloor k\rfloor$ copies of $U$, so we have
    
        $$
        F(k,n,U,R) = F(k-\lfloor k\rfloor,n,U,U^{\lfloor k\rfloor} R).
        $$
    -   If $k<1$, swap $U$ and $R$ in the operation sequence and discard the trailing $U$'s (i.e., the $R$'s before the swap); then, writing $m=\lfloor kn\rfloor$, we have
    
        $$
        F(k,n,U,R) = F(k^{-1},m,R,U)R^{n-\lfloor k^{-1}m\rfloor}.
        $$
    
    The iteration of $k$ in the algorithm is in fact the computation of the continued fraction expansion of $\sqrt{r}$. For this, the [PQa algorithm](./pell-equation.md#pqa-algorithm) can be applied. The computation of the continued fraction and the iteration of the universal Euclidean algorithm can be carried out simultaneously.
    
    As in the case of the Euclidean-like algorithm, the complexity of the algorithm is still $O(\log n)$.
    
    ```cpp
    --8<-- "docs/math/code/euclidean/euclidean-6.cpp"
    ```

## Exercises

Template problems:

-   [Library Checker - Sum of Floor of Linear](https://judge.yosupo.jp/problem/sum_of_floor_of_linear)
-   [Luogu P5170【模板】类欧几里得算法 (Template: Euclidean-like algorithm)](https://www.luogu.com.cn/problem/P5170)
-   [Luogu P5171 Earthquake](https://www.luogu.com.cn/problem/P5171)
-   [Luogu P5172 \[清华集训 2014\] Sum (Tsinghua Training Camp 2014)](https://www.luogu.com.cn/problem/P5172)
-   [Luogu P4132 \[BJOI2012\] 算不出的等式 (The Uncomputable Equation)](https://www.luogu.com.cn/problem/P4132)
-   [LOJ 138. 类欧几里得算法 (Euclidean-like algorithm)](https://loj.ac/p/138)
-   [LOJ 6440. 万能欧几里得 (Universal Euclidean algorithm)](https://loj.ac/p/6440)
-   [Luogu P5179 Fraction](https://www.luogu.com.cn/problem/P5179)
-   [Codeforces 1182 F. Maximum Sine](https://codeforces.com/problemset/problem/1182/F)

Application problems:

-   [Luogu P4433 \[COCI 2009/2010 #1\] ALADIN](https://www.luogu.com.cn/problem/P4433)
-   [AtCoder Beginner Contest 372 G - Ax + By < C](https://atcoder.jp/contests/abc372/tasks/abc372_g)
-   [AtCoder Beginner Contest 313 G - Redistribution of Piles](https://atcoder.jp/contests/abc313/tasks/abc313_g)
-   [AtCoder Beginner Contest 283 Ex - Popcount Sum](https://atcoder.jp/contests/abc283/tasks/abc283_h)
-   [Codeforces 1098 E. Fedya the Potter](https://codeforces.com/problemset/problem/1098/E)
-   [Codeforces 868 G. El Toll Caves](https://codeforces.com/problemset/problem/868/G)

## References and notes

[^complexity]: In the problems usually considered, $b$ is of the same order as $a$, so the term $O(\log(b/c))$ can be ignored. Moreover, if one round of modulo reduction from the Euclidean-like algorithm is performed before calling the universal Euclidean algorithm, eliminating the influence of $b$, the complexity of this binary exponentiation can be avoided. This is actually because in common problems the initial form of $U$ is rather special, and its powers have a simpler form that does not need to be computed by binary exponentiation. For example, in the example in the main text, the result of $U^{\lfloor b/c\rfloor}$ is obtained by replacing the off-diagonal $1$ in $U$ with $\lfloor b/c\rfloor$, with no need for binary exponentiation.
