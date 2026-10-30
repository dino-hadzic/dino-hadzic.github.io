---
title: Polynomial shift | shift of consecutive point values
---

## Polynomial shift

Polynomial shift (Taylor shift) is a simple special case of polynomial composition: given the coefficients of $f(x)=\sum _ {i=0}^nf_ix^i$ and a constant $c$, find the coefficients of $f(x+c)$, i.e. $f(x)\mapsto f(x+c)$.

### Divide and conquer method

Let

$$
f(x)=f_0(x)+x^{\left\lfloor n/2\right\rfloor}f_1(x)
$$

Then

$$
f(x+c)=f_0(x+c)+(x+c)^{\left\lfloor n/2\right\rfloor}f_1(x+c)
$$

The coefficients of $(x+c)^{\left\lfloor n/2\right\rfloor}$ are binomial coefficients, so

$$
T(n)=2T(n/2)+O(n\log n)=O(n\log^2 n)
$$

where $O(n\log n)$ is the time of polynomial multiplication.

### Taylor's formula method

Applying Taylor's formula to $f(x)$ at $c$, we have

$$
f(x)=f(c)+\frac{f'(c)}{1!}(x-c)+\frac{f''(c)}{2!}(x-c)^2+\cdots +\frac{f^{(n)}(c)}{n!}(x-c)^n
$$

Then

$$
f(x+c)=f(c)+\frac{f'(c)}{1!}x+\frac{f''(c)}{2!}x^2+\cdots +\frac{f^{(n)}(c)}{n!}x^n
$$

Observe that for $t\geq 0$ we have

$$
\begin{aligned}
t!\lbrack x^t\rbrack f(x+c)&=f^{(t)}(c)\\
&=\sum _ {i=t}^nf_ii!\frac{c^{i-t}}{(i-t)!}\\
&=\sum _ {i=0}^{n-t}f _ {i+t}(i+t)!\frac{c^i}{i!}
\end{aligned}
$$

Let

$$
\begin{aligned}
A_0(x)&=\sum _ {i=0}^nf _ {n-i}(n-i)!x^i\\
B_0(x)&=\sum _ {i=0}^n\frac{c^i}{i!}x^i
\end{aligned}
$$

Then

$$
\begin{aligned}
\lbrack x^{n-t}\rbrack (A_0(x)B_0(x))&=\sum _ {i=0}^{n-t} (\lbrack x^{n-t-i}\rbrack A_0(x))(\lbrack x^i\rbrack B_0(x))\\
&=\sum _ {i=0}^{n-t}f _ {i+t}(i+t)!\frac{c^i}{i!}\\
&=t!\lbrack x^t\rbrack f(x+c)
\end{aligned}
$$

### Binomial theorem method

Consider the binomial theorem $\displaystyle (a+b)^n=\sum _ {i=0}^n\binom{n}{i}a^ib^{n-i}$; then

$$
\begin{aligned}
f(x+c)&=\sum _ {i=0}^nf_i(x+c)^i\\
&=\sum _ {i=0}^nf_i\left(\sum _ {j=0}^i\binom{i}{j}x^jc^{i-j}\right)\\
&=\sum _ {i=0}^nf_ii!\left(\sum _ {j=0}^i\frac{x^j}{j!}\frac{c^{i-j}}{(i-j)!}\right)\\
&=\sum _ {i=0}^n\frac{x^i}{i!}\left(\sum _ {j=i}^{n}f_jj!\frac{c^{j-i}}{(j-i)!}\right)
\end{aligned}
$$

The result is the same as with the method above.

## Shift of consecutive point values

???+ note "Example problem [LOJ 166 拉格朗日插值 2 (Lagrange Interpolation 2)](https://loj.ac/p/166)"
    Given the consecutive values $f(0),f(1),\dots ,f(n)$ of a polynomial $f$ of degree at most $n$, compute $f(c),f(c+1),\dots ,f(c+n)$ modulo $998244353$, where $1\leq n\leq 10^5,n < m\leq 10^8$.

### Lagrange interpolation formula method

Consider the [Lagrange interpolation formula](../numerical/interp.md#lagrange-插值法)

$$
\begin{aligned}
f(x)&=\sum _ {0\leq i\leq n}f(i)\prod _ {0\leq j\leq n\,\land \,j\neq i}\frac{x-j}{i-j}\\
&=\sum _ {0\leq i\leq n}f(i)\frac{x!}{(x-n-1)!(x-i)}\frac{(-1)^{n-i}}{i!(n-i)!}\\
&=\frac{x!}{(x-n-1)!}\sum _ {0\leq i\leq n}\frac{f(i)}{(x-i)}\frac{(-1)^{n-i}}{i!(n-i)!}
\end{aligned}
$$

Although the expression above has the form of a convolution, it does not guarantee $x-i\neq 0$ in the denominator, so below we only consider the case $c > n$; the other cases (e.g. when the coefficients are taken modulo a prime, one must avoid zeros in the denominators of the coefficients of $B_0(x)$) can be handled by case analysis. Let

$$
\begin{aligned}
A_0(x)&=\sum _ {0\leq i\leq n}\frac{f(i)(-1)^{n-i}}{i!(n-i)!}x^i\\
B_0(x)&=\sum _ {i\geq 0}\frac{1}{c-n+i}x^i
\end{aligned}
$$

Then for $t\geq 0$ we have

$$
\begin{aligned}
\lbrack x^{n+t}\rbrack (A_0(x)B_0(x))&=\sum _ {i=0}^{n+t}(\lbrack x^i\rbrack A_0(x))(\lbrack x^{n+t-i}\rbrack B_0(x))\\
&=\sum _ {i=0}^{n}\frac{f(i)(-1)^{n-i}}{i!(n-i)!}\frac{1}{c+t-i}\\
&=\frac{(c+t-n-1)!}{(c+t)!}f(c+t)
\end{aligned}
$$

In the implementation we truncate $B_0(x)$ to the part we need, which can also yield more point values, and cyclic convolution can be used.

Slightly modifying the problem: suppose that for some $d$ the given values are $f(d),f(d+k),\dots ,f(d+nk)$; then we can compute $f(c+d),f(c+d+k),\dots ,f(c+d+nk)$, viewed as shifting the point values $g(0),g(1),\dots ,g(n)$ of $g(x)=f(d+kx)$ to $g(c/k),g(c/k+1),\dots ,g(c/k+n)$.

The Lagrange interpolation formula also gives a way to compute a single point value in linear time by maintaining some prefix and suffix products.

## Applications

### Unsigned Stirling numbers of the first kind in one row

???+ note "Example problem [P5408 第一类斯特林数·行 (Stirling Numbers of the First Kind – Row)](https://www.luogu.com.cn/problem/P5408)"
    Compute $\displaystyle {n\brack 0},{n\brack 1},\dots ,{n\brack n}$ modulo the prime $167772161$, where $1\leq n< 262144$.

Consider

$$
x^{\overline{n}}=\sum _ {i=0}^n{n\brack i}x^i,\quad n\geq 0
$$

where $x^{\overline{n}}=x\cdot (x+1)\cdots (x+n-1)$ is the rising factorial. Let $f_n(x)=x^{\overline{n}}$; then

$$
f_{2n}(x)=x^{\overline{n}}\cdot (x+n)^{\overline{n}}=f_n(x)f_n(x+n)
$$

Using polynomial shift we can find $f_n(x+n)$ in $O(n\log n)$, and the problem is reduced to half of the original, namely finding the coefficients of $f_n(x)$; thus

$$
T(n)=T(n/2)+O(n\log n)=O(n\log n)
$$

### Factorial modulo a prime

???+ note "Example problem [P5282【模板】快速阶乘算法 (Template: Fast Factorial Algorithm)](https://www.luogu.com.cn/problem/P5282)"
    Compute $n!\bmod p$, where $p$ is prime and $1\leq n< p\leq 2^{31}-1$.

Let $v=\lfloor\sqrt{n}\rfloor$ and $g(x)=\prod _ {i=1}^v(x+i)$; then

$$
n!\equiv \left(\prod _ {i=0}^{v-1}g(iv)\right)\cdot \prod _ {i=v^2+1}^n i\pmod{p}
$$

where $\prod _ {i=v^2+1}^n i$ can be computed in $O(\sqrt{n})$ time; we want to compute the first part of the expression above quickly.

#### Polynomial multipoint evaluation

The coefficients of $g(x)$ can be obtained with the polynomial shift algorithm above in $O(n\log n)$ time, but the multipoint evaluation of $g(0),g(v),g(2v),\dots ,g(v^2-v)$ takes $O(\sqrt{n}\log ^2n)$ time.

#### Shift of consecutive point values

Let $g_d(x)=\prod _ {i=1}^d(x+i)$; with the $d+1$ point values $g_d(0),g_d(v),\dots ,g_d(dv)$ we can uniquely determine this polynomial of degree $d$, and moreover

$$
g _ {2d}(x)=g_d(x)g_d(x+d)
$$

so $2d+1$ point values suffice to uniquely determine $g _ {2d}(x)$. Hence we use the shift of consecutive point values to compute $g_d((d+1)v),g_d((d+2)v),\dots ,g_d(2dv)$ (i.e. shift the point values $h(0),h(1),\dots ,h(d)$ of $h(x)=g_d(vx)$ to $h(d+1),h(d+2),\dots ,h(2d)$) and $g_d(d),g_d(v+d),\dots ,g_d(2dv+d)$ (i.e. shift the point values $h(0),h(1),\dots ,h(d)$ of $h(x)=g_d(vx)$ to $h(d/v),h(d/v+1),h(d/v+2),\dots ,h(d/v+2d)$), and then multiply the corresponding point values to obtain $g _ {2d}(0),g _ {2d}(v),\dots ,g _ {2d}(2dv)$.

To compute $g _ {d+1}(0),g _ {d+1}(v),\dots ,g _ {d+1}(dv),g _ {d+1}((d+1)v)$ from $g_d(0),g_d(v),\dots ,g_d(dv)$, consider

$$
g _ {d+1}(x)=(x+d+1)\cdot g_d(x)
$$

The one extra point value can be obtained with a linear-time algorithm. So we start by maintaining $g_1(0)=1,g_1(v)=v+1$ and then use the shift of consecutive point values to maintain these point values by doubling; we have

$$
T(n)=T(n/2)+O(n\log n)=O(n\log n)
$$

and we only need about $\sqrt{n}$ point values, so the time complexity is $O(\sqrt{n}\log n)$.

### Prefix sums of binomial coefficients modulo a prime

???+ note "Example problem [LOJ 6386 组合数前缀和 (Prefix Sum of Binomial Coefficients)](https://loj.ac/p/6386)"
    Compute $\displaystyle \sum _ {i=0}^m\binom{n}{i}\bmod 998244353$, where $0\leq m\leq n\leq 9\times 10^8$.

Describing the recurrence step $n!=n\cdot (n-1)!$ with a matrix, we have

$$
\begin{bmatrix}
n!
\end{bmatrix}
=\left(
\prod _ {i=0}^{n-1}
\begin{bmatrix}i+1\end{bmatrix}
\right)
\begin{bmatrix}
1
\end{bmatrix}
$$

Similarly, the recurrence for the prefix sum of binomial coefficients can be described as

$$
\begin{bmatrix}
\binom{n}{m+1}\\
\sum _ {i=0}^m\binom{n}{i}
\end{bmatrix}=
\begin{bmatrix}
(n-m)/(m+1)&0\\
1&1
\end{bmatrix}
\begin{bmatrix}
\binom{n}{m}\\
\sum _ {i=0}^{m-1}\binom{n}{i}
\end{bmatrix}
$$

Paying attention to the order of matrix multiplication, we have

$$
\begin{aligned}
\begin{bmatrix}
\binom{n}{m+1}\\
\sum _ {i=0}^m\binom{n}{i}
\end{bmatrix}
&=\left(
\prod _ {i=0}^{m}
\begin{bmatrix}
(n-i)/(i+1)&0\\1&1
\end{bmatrix}
\right)
\begin{bmatrix}
1\\0
\end{bmatrix}\\
&=
\frac{1}{(m+1)!}
\left(
\prod _ {i=0}^{m}
\begin{bmatrix}
n-i&0\\i+1&i+1
\end{bmatrix}
\right)
\begin{bmatrix}
1\\0
\end{bmatrix}
\end{aligned}
$$

Let $v=\lfloor\sqrt{m}\rfloor$; we maintain the point values of the matrix

$$
\begin{aligned}
M _ d(x)&=
\prod _ {i=1}^d
\begin{bmatrix}
-x+n+1-i&0\\
x+i&x+i
\end{bmatrix}\\
&=
\begin{bmatrix}
f_d(x)&0\\
g_d(x)&h_d(x)
\end{bmatrix}
\end{aligned}
$$

namely $M _ d(0),M _ d(v),\dots ,M_d(dv)$, i.e. $f_d(0),f_d(v),\dots ,f_d(dv)$, $h_d(0),\dots ,h_d(dv)$ and $g_d(0),\dots ,g_d(dv)$; moreover

$$
\begin{aligned}
M _ {2d}(x)&=
\prod _ {i=1}^{2d}
\begin{bmatrix}
-x+n+1-i&0\\
x+i&x+i
\end{bmatrix}\\
&=
\left(
\prod _ {i=1}^d
\begin{bmatrix}
-x-d+n+1-i&0\\
x+d+i&x+d+i
\end{bmatrix}
\right)
\left(
\prod _ {i=1}^d
\begin{bmatrix}
-x+n+1-i&0\\
x+i&x+i
\end{bmatrix}
\right) \\
&=
\begin{bmatrix}
f_d(x+d)&0\\
g_d(x+d)&h_d(x+d)
\end{bmatrix}
\begin{bmatrix}
f_d(x)&0\\
g_d(x)&h_d(x)
\end{bmatrix} \\
&=
\begin{bmatrix}
f_d(x+d)f_d(x)&0\\
g_d(x+d)f_d(x)+h_d(x+d)g_d(x)&h_d(x+d)h_d(x)
\end{bmatrix}
\end{aligned}
$$

and the bottom-right element of the matrix is exactly what we maintain in the factorial algorithm; then

$$
\begin{aligned}
\prod _ {i=0}^{m}
\begin{bmatrix}
n-i&0\\i+1&i+1
\end{bmatrix}=
\left(
\prod _ {i=(k+1)v}^m
\begin{bmatrix}
n-i&0\\
i+1&i+1
\end{bmatrix}
\right)
\begin{bmatrix}
f_v(kv)&0\\
g_v(kv)&h_v(kv)
\end{bmatrix}
\cdots
\begin{bmatrix}
f_v(0)&0\\
g_v(0)&h_v(0)
\end{bmatrix}
\end{aligned}
$$

which can be computed in $O(\sqrt m\log m)$ time.

### Harmonic numbers modulo a prime

???+ note "Example problem [P5702 调和级数求和 (Harmonic Series Sum)](https://www.luogu.com.cn/problem/P5702)"
    Compute $\sum _ {i=1}^ni^{-1}\bmod p$, where $p$ is prime and $1\leq n< p< 2^{30}$.

Let $H_n=\sum _ {k=1}^nk^{-1}$; one recurrence step is

$$
\begin{bmatrix}
(n+1)!\\(n+1)!H _ {n+1}
\end{bmatrix}=
\begin{bmatrix}
n+1&0\\1&n+1
\end{bmatrix}
\begin{bmatrix}
n!\\n!H_n
\end{bmatrix}
$$

Then

$$
\begin{bmatrix}
{n+1\brack 1}\\{n+1\brack 2}
\end{bmatrix}=
\begin{bmatrix}
n!\\n!H_n
\end{bmatrix}=
\left(
\prod _ {i=0}^{n-1}
\begin{bmatrix}
i+1&0\\1&i+1
\end{bmatrix}
\right)
\begin{bmatrix}
1\\0
\end{bmatrix}
$$

Here $\displaystyle {n+1\brack 1}$ and $\displaystyle {n+1\brack 2}$ are unsigned Stirling numbers of the first kind. The method of maintaining the point values of the matrix is the same as above.

## Recurrences with polynomial coefficients

In the more general case, similar to the fast factorial algorithm above, what kind of algorithm do we expect to obtain?

???+ note "Example problem [P6115【模板】整式递推 (Template: Recurrence with Polynomial Coefficients)](https://www.luogu.com.cn/problem/P6115)"
    A sequence $a$ satisfies $\forall n\ge m,\sum_{k=0}^ma_{n-k}P_k(n)=0$, where the $P_k$ are polynomials of degree at most $d$.  
    Given the coefficients of all $P_k$ and $a_0,a_1,\dots,a_{m-1}$, compute $a_n$.
    The answer is taken modulo $998244353$. $n\le6\times10^8$, $1\le m,d\le7$, time limit $7s$.

To describe the construction of the matrices in the examples above more systematically, we introduce the concept of a [$\lambda$-matrix](../linear-algebra/jordan.md#lambda-%E7%9F%A9%E9%98%B5).

To implement recurrences with polynomial coefficients, we should note that in the fast factorial algorithm the point values we maintain are actually not $n!$ but $\prod_{i=0}^{T-1}(aT+i)$, i.e. **the ratio between a pair of point values**.

Since the order $m$ of a recurrence with polynomial coefficients is no longer $1$, **we can no longer directly maintain the ratio between a pair of numbers**; instead we maintain **the linear transformation between a pair of $m$-dimensional vectors**, i.e. an $m\times m$ matrix, **where each entry of the matrix corresponds to a point value of some polynomial**.

It is easy to see that for the general problem of evaluating a far coefficient of a recurrence with polynomial coefficients we can construct

$$
-{\frac{1}{P_0(n)}}\begin{bmatrix}P_1(n)&P_2(n)&P_3(n)&\cdots&P_{m-1}(n)&P_m(n)\\-P_0(n)\\&-P_0(n)\\&&-P_0(n)\\&&&\ddots\\&&&&-P_0(n)\\\end{bmatrix}
\begin{bmatrix}a_{n-1}\\a_{n-2}\\a_{n-3}\\\vdots\\a_{n-m+1}\\a_{n-m}\end{bmatrix}
=\begin{bmatrix}a_n\\a_{n-1}\\a_{n-2}\\\vdots\\a_{n-m+2}\\a_{n-m+1}\end{bmatrix}
$$

Let

$$
B(\lambda)=\begin{bmatrix}
    P_1(\lambda)&P_2(\lambda)&P_3(\lambda)&\cdots&P_{m-1}(\lambda)&P_m(\lambda)\\
    -P_0(\lambda)\\
    &-P_0(\lambda)\\
    &&-P_0(\lambda)\\
    &&&\ddots\\
    &&&&-P_0(\lambda)\\
\end{bmatrix}
$$

Setting aside the leading factor $-\frac1{P_0(n)}$ for now, we want to maintain quantities of the form $\prod_{i=0}^{T-1}B(aT+m+i)$, where the multiplication goes from right to left.

It is easy to see that $B_T(\lambda)=\prod_{i=0}^{T-1}B(\lambda+i)$ is a $\lambda$-matrix whose entries have degree at most $dT$, so $dT+1$ values suffice to maintain it.

Hence we maintain the **point values** of the $\lambda$-matrices $B_T(m)$, $B_T(m+T)$, $B_T(m+2T)$, $\dots$, $B_T(m+(dT-1)T)$, $B_T(m+dT^2)$, and then, similarly to the fast factorial algorithm, directly perform shifts of polynomial point values and doubling.

Specifically, to raise $t=\log_2T$ by $1$, we do the following:

1.  In $O(m^2dT\log(dT))$ time obtain $B_T(p+dT^2)$, $B_T(p+(dT+1)T)$, $B_T(p+(dT+2)T)$, $\cdots$, $B_T(p+(2dT-1)T)$, $B_T(p+(2dT)dT)$.
2.  In $O(m^2dT\log(dT))$ time obtain $B_T(p+2dT^2)$, $B_T(p+(2dT+1)T)$, $B_T(p+(2dT+2)T)$, $\cdots$, $B_T(p+(3dT-1)T)$, $B_T(p+(3dT)dT)$.
3.  In $O(m^2dT\log(dT))$ time obtain $B_T(p+3dT^2)$, $B_T(p+(3dT+1)T)$, $B_T(p+(3dT+2)T)$, $\cdots$, $B_T(p+(4dT-1)T)$, $B_T(p+(4dT)dT)$.
4.  Compute $B_{2T}(v)=B_{T}(v+T)B_{T}(v)$.

In each round we spend $O(m^2dT\log(dT))$ on the shifts; at the same time, in each round we only perform $\Theta(dT)$ matrix multiplications, whose complexity can be taken as $O(m^3dT)$.

Finally, we only need to go up to $T\ge\sqrt{n/d}$.

The factor $-\frac1{P_0(n)}$ from before can be handled in a similar way.

Thus the preprocessing complexity is $\Theta(\sqrt{nd}(m^3+m^2\log(nd)))$.

For the query, we only need $\Theta(n/T)$ vector–matrix multiplications and $O(T)$ brute-force transitions.

It is easy to see that this part of the computation is not the complexity bottleneck.

Therefore the total complexity of the algorithm is $\Theta(\sqrt{nd}(m^3+m^2\log(nd)))$.

When coding, we can use the cyclic convolution trick to reduce the constant of the NTT.

In practice we usually extract a far coefficient of a known D-finite (differentiably finite) generating function, so $m,d$ are constants, and we achieve far-coefficient evaluation in $\Theta(\sqrt n\log n)$.

## References

-   Alin Bostan, Pierrick Gaudry, and Eric Schost. Linear recurrences with polynomial coefficients and application to integer factorization and Cartier–Manin operator.
-   Min\_25's blog
-   [ZZQ's blog – 阶乘模大质数 (Factorial modulo a large prime)](https://www.cnblogs.com/zzqsblog/p/8408691.html)
