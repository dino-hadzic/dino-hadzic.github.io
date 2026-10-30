---
title: Elementary functions of polynomials
---

This page covers the common elementary function operations on polynomials. Specifically, the page contains the following:

1.  polynomial inverse
2.  polynomial square root
3.  polynomial division
4.  polynomial modulo
5.  polynomial exponential function
6.  polynomial logarithm
7.  polynomial trigonometric functions
8.  polynomial inverse trigonometric functions

??? note "Elementary and non-elementary functions"
    Elementary functions are defined as follows[^ref1]:
    
    If a field $F$ has a map $u\to \partial u$ satisfying:
    
    1.  $\partial(u+v)=\partial u+\partial v$
    2.  $\partial(uv)=u\partial v+v\partial u$
    
    then the field is called a **differential field**.
    
    If a function $u$ over a differential field $F$ satisfies any one of the following conditions, the function $u$ is called an elementary function:
    
    1.  $u$ is an algebraic function over $F$.
    2.  $u$ is exponential over $F$, i.e. there exists $a\in F$ such that $\partial u=u\partial a$.
    3.  $u$ is logarithmic over $F$, i.e. there exists $a\in F$ such that $\partial u=\frac{\partial a}{a}$.
    
    Common elementary functions are:
    
    1.  algebraic functions: functions $f(x)$ for which there exists a polynomial $P$ of finite degree such that $P(f(x))=0$, e.g. $2x+1$,$\sqrt{x}$,$(1+x^2)^{-1}$,$|x|$.
    2.  exponential functions
    3.  logarithmic functions
    4.  trigonometric functions
    5.  inverse trigonometric functions
    6.  hyperbolic functions
    7.  inverse hyperbolic functions
    8.  compositions of the functions above, e.g.:
    
        $$
        \frac{\mathrm{e}^{\tan x}}{1+x^2}\sin\left(\sqrt{1+\ln^2 x}\right)
        $$
    
        $$
        -\mathrm{i} \ln\left(x+\mathrm{i}\sqrt{1-x^2}\right)
        $$
    
    Common non-elementary functions are:
    
    1.  the error function:
    
        $$
        \operatorname{erf}(x):=\frac{2}{\sqrt{\pi}}\int_{0}^{x}\exp\left(-t^2\right)\mathrm{d}t
        $$

## Polynomial inverse

Given a polynomial $f\left(x\right)$, find $f^{-1}\left(x\right)$.

### Solution

#### Doubling method

First, it is easy to see that

$$
\left[x^{0}\right]f^{-1}\left(x\right)=\left(\left[x^{0}\right]f\left(x\right)\right)^{-1}
$$

Suppose we have already found the inverse $f^{-1}_{0}\left(x\right)$ of $f\left(x\right)$ modulo $x^{\left\lceil\frac{n}{2}\right\rceil}$.
We have:

$$
\begin{aligned}
    f\left(x\right)f^{-1}_{0}\left(x\right)&\equiv 1 &\pmod{x^{\left\lceil\frac{n}{2}\right\rceil}}\\
    f\left(x\right)f^{-1}\left(x\right)&\equiv 1 &\pmod{x^{\left\lceil\frac{n}{2}\right\rceil}}\\
    f^{-1}\left(x\right)-f^{-1}_{0}\left(x\right)&\equiv 0 &\pmod{x^{\left\lceil\frac{n}{2}\right\rceil}}
\end{aligned}
$$

Squaring both sides gives:

$$
f^{-2}\left(x\right)-2f^{-1}\left(x\right)f^{-1}_{0}\left(x\right)+f^{-2}_{0}\left(x\right)\equiv 0 \pmod{x^{n}}
$$

Multiplying both sides by $f\left(x\right)$ and rearranging gives:

$$
f^{-1}\left(x\right)\equiv f^{-1}_{0}\left(x\right)\left(2-f\left(x\right)f^{-1}_{0}\left(x\right)\right) \pmod{x^{n}}
$$

It suffices to compute this recursively.

**Time complexity**

$$
T\left(n\right)=T\left(\frac{n}{2}\right)+O\left(n\log{n}\right)=O\left(n\log{n}\right)
$$

#### Newton's method

See [Newton's method](./newton.md#newtons-method).

#### Graeffe's method

To find $f^{-1}(x)\bmod x^{2n}$, consider

$$
\begin{aligned}
f^{-1}(x)\bmod x^{2n}&= f(-x)(f(x)f(-x))^{-1}\bmod x^{2n}\\
&=f(-x)g^{-1}(x^2)\bmod x^{2n}
\end{aligned}
$$

It suffices to find $g^{-1}(x)\bmod x^n$ and recover $g^{-1}(x^2)\bmod x^{2n}$ from it, because $f(x)f(-x)$ is an even function; the time complexity is the same as above.

### Code

??? note "Polynomial inverse"
    ```cpp
    constexpr int MAXN = 262144;
    constexpr int mod = 998244353;
    
    using i64 = long long;
    using poly_t = int[MAXN];
    using poly = int *const;
    
    void polyinv(const poly &h, const int n, poly &f) {
      /* f = 1 / h = f_0 (2 - f_0 h) */
      static poly_t inv_t;
      std::fill(f, f + n + n, 0);
      f[0] = fpow(h[0], mod - 2);
      for (int t = 2; t <= n; t <<= 1) {
        const int t2 = t << 1;
        std::copy(h, h + t, inv_t);
        std::fill(inv_t + t, inv_t + t2, 0);
    
        DFT(f, t2);
        DFT(inv_t, t2);
        for (int i = 0; i != t2; ++i)
          f[i] = (i64)f[i] * sub(2, (i64)f[i] * inv_t[i] % mod) % mod;
        IDFT(f, t2);
    
        std::fill(f + t, f + t2, 0);
      }
    }
    ```

### Example problems

1.  Counting labeled simple undirected connected graphs: [“POJ 1737” Connected Graph](http://poj.org/problem?id=1737)

## Polynomial square root

Given a polynomial $g\left(x\right)$, find $f\left(x\right)$ satisfying:

$$
f^{2}\left(x\right)\equiv g\left(x\right) \pmod{x^{n}}
$$

### Solution

#### Doubling method

First we discuss the case where $\left[x^0\right]g(x)$ is not $0$.

It is easy to see that:

$$
\left[x^0\right]f(x) = \sqrt{\left[x^0\right]g(x)}
$$

If $\left[x^0\right]g(x)$ has no square root, then the polynomial $g(x)$ has no square root.

> $\left[x^0\right]g(x)$ may have several square roots; choosing different roots yields different $f(x)$.

Suppose we have already found the square root $f_{0}\left(x\right)$ of $g\left(x\right)$ modulo $x^{\left\lceil\frac{n}{2}\right\rceil}$; then we have:

$$
\begin{aligned}
    f_{0}^{2}\left(x\right)&\equiv g\left(x\right) &\pmod{x^{\left\lceil\frac{n}{2}\right\rceil}}\\
    f_{0}^{2}\left(x\right)-g\left(x\right)&\equiv 0 &\pmod{x^{\left\lceil\frac{n}{2}\right\rceil}}\\
    \left(f_{0}^{2}\left(x\right)-g\left(x\right)\right)^{2}&\equiv 0 &\pmod{x^{n}}\\
    \left(f_{0}^{2}\left(x\right)+g\left(x\right)\right)^{2}&\equiv 4f_{0}^{2}\left(x\right)g\left(x\right) &\pmod{x^{n}}\\
    \left(\frac{f_{0}^{2}\left(x\right)+g\left(x\right)}{2f_{0}\left(x\right)}\right)^{2}&\equiv g\left(x\right) &\pmod{x^{n}}\\
    \frac{f_{0}^{2}\left(x\right)+g\left(x\right)}{2f_{0}\left(x\right)}&\equiv f\left(x\right) &\pmod{x^{n}}\\
    2^{-1}f_{0}\left(x\right)+2^{-1}f_{0}^{-1}\left(x\right)g\left(x\right)&\equiv f\left(x\right) &\pmod{x^{n}}
\end{aligned}
$$

It suffices to compute this by doubling.

**Time complexity**

$$
T\left(n\right)=T\left(\frac{n}{2}\right)+O\left(n\log{n}\right)=O\left(n\log{n}\right)
$$

There is also a variant with a smaller constant: while maintaining $f\left(x\right)$ during the doubling, also maintain $f^{-1}\left(x\right)$ instead of computing the inverse from scratch every time.

> When $\left[x^{0}\right]g\left(x\right)\neq 1$, quadratic residues may be needed to compute $\left[x^{0}\right]f\left(x\right)$.

The method above needs the inverse of $f_{0}(x)$, so the constant term must not be $0$.

If $\left[x^0\right]g(x) = 0$, factor $g(x)$ as $x^{k}h(x)$, where $\left[x^0\right]h(x) \not = 0$.

-   If $k$ is odd, $g(x)$ has no square root.

-   If $k$ is even, find the square root $\sqrt{h(x)}$ of $h(x)$, and then obtain $f(x) \equiv x^{k/2} \sqrt{h(x)} \pmod{x^{n}}$.

??? note "Reference code for the Luogu template problem [P5205【模板】多项式开根 (Template: polynomial square root)](https://www.luogu.com.cn/problem/P5205)"
    ```cpp
    --8<-- "docs/math/code/poly/sqrt/sqrt_1.cpp"
    ```

#### Newton's method

See [Newton's method](./newton.md#newtons-method).

### Example problems

1.  [“Codeforces Round #250” E. The Child and Binary Tree](https://codeforces.com/contest/438/problem/E)

## Polynomial division and modulo

Given polynomials $f\left(x\right),g\left(x\right)$, find the quotient $Q\left(x\right)$ and the remainder $R\left(x\right)$ of $f\left(x\right)$ divided by $g\left(x\right)$.

### Solution

Notice that if we could eliminate the influence of $R\left(x\right)$, the problem could be solved directly by [polynomial inverse](#polynomial-inverse).

Consider the transformation

$$
f^{R}\left(x\right)=x^{\operatorname{deg}{f}}f\left(\frac{1}{x}\right)
$$

Looking closely, it essentially reverses the coefficients of $f\left(x\right)$.

Let $n=\operatorname{deg}{f},m=\operatorname{deg}{g}$.

In $f\left(x\right)=Q\left(x\right)g\left(x\right)+R\left(x\right)$ replace $x$ with $\frac{1}{x}$ and multiply both sides by $x^{n}$; we get:

$$
\begin{aligned}
    x^{n}f\left(\frac{1}{x}\right)&=x^{n-m}Q\left(\frac{1}{x}\right)x^{m}g\left(\frac{1}{x}\right)+x^{n-m+1}x^{m-1}R\left(\frac{1}{x}\right)\\
    f^{R}\left(x\right)&=Q^{R}\left(x\right)g^{R}\left(x\right)+x^{n-m+1}R^{R}\left(x\right)
\end{aligned}
$$

Note that in the expression above the coefficient of $R^{R}\left(x\right)$ is $x^{n-m+1}$, so working modulo $x^{n-m+1}$ eliminates the influence of $R^{R}\left(x\right)$.

Since the degree of $Q^{R}\left(x\right)$ is $\left(n-m\right)<\left(n-m+1\right)$, $Q^{R}\left(x\right)$ is not affected.

Therefore:

$$
f^{R}\left(x\right)\equiv Q^{R}\left(x\right)g^{R}\left(x\right)\pmod{x^{n-m+1}}
$$

Using polynomial inverse we find $Q\left(x\right)$, and substituting back gives $R\left(x\right)$.

**Time complexity**  $O\left(n\log{n}\right)$.

## Polynomial logarithm and exponential

Given a polynomial $f(x)$, find $\ln{f(x)}$ and $\exp{f(x)}$ modulo $x^{n}$.

### Solution

#### Ordinary method

=== "Polynomial logarithm"
    First, for a polynomial $f(x)$, if $\ln{f(x)}$ exists, then by its [definition](./intro.md#复合) it must satisfy:
    
    $$
    [x^{0}]f(x)=1
    $$
    
    Differentiating and then integrating $\ln{f(x)}$ gives:
    
    $$
    \begin{aligned}
        \frac{\mathrm{d} \ln{f(x)}}{\mathrm{d} x} & \equiv \frac{f'(x)}{f(x)} & \pmod{x^{n}} \\
        \ln{f(x)} & \equiv \int \mathrm{d} \ln{f(x)} \equiv \int\frac{f'(x)}{f(x)} \mathrm{d} x & \pmod{x^{n}}
    \end{aligned}
    $$
    
    Differentiating and integrating a polynomial take $O(n)$ time and the inverse takes $O(n\log{n})$, so computing $\ln$ of a polynomial takes $O(n\log{n})$ time.

=== "Polynomial exponential"
    First, for a polynomial $f(x)$, if $\exp{f(x)}$ exists, then it must satisfy:
    
    $$
    [x^{0}]f(x)=0
    $$
    
    Otherwise the constant term of $\exp{f(x)}$ does not converge.
    
    Differentiating $\exp{f(x)}$ gives:
    
    $$
    \frac{\mathrm{d} \exp{f(x)}}{\mathrm{d} x} \equiv \exp{f(x)}f'(x)\pmod{x^{n}}
    $$
    
    Comparing coefficients on both sides gives:
    
    $$
    [x^{n-1}]\frac{\mathrm{d} \exp{f(x)}}{\mathrm{d} x} = \sum_{i = 0}^{n - 1} \left([x^{i}]\exp{f(x)}\right) \left([x^{n-i-1}]f'(x)\right)
    $$
    
    $$
    n[x^{n}]\exp{f(x)} = \sum_{i = 0}^{n - 1} \left([x^{i}]\exp{f(x)}\right) \left((n - i)[x^{n - i}]f(x)\right)
    $$
    
    This can be solved with divide and conquer FFT.
    
    **Time complexity**  $O(n\log^{2}{n})$.

#### Newton's method

Using [Newton's method](./newton.md#newtons-method), the polynomial $\exp$ can be computed in $O(n\log{n})$ time.

### Code

??? note "Polynomial ln/exp"
    ```cpp
    constexpr int MAXN = 262144;
    constexpr int mod = 998244353;
    
    using i64 = long long;
    using poly_t = int[MAXN];
    using poly = int *const;
    
    void derivative(const poly &h, const int n, poly &f) {
      for (int i = 1; i != n; ++i) f[i - 1] = (i64)h[i] * i % mod;
      f[n - 1] = 0;
    }
    
    void integrate(const poly &h, const int n, poly &f) {
      for (int i = n - 1; i; --i) f[i] = (i64)h[i - 1] * inv[i] % mod;
      f[0] = 0; /* C */
    }
    
    void polyln(const poly &h, const int n, poly &f) {
      /* f = ln h = ∫ h' / h dx */
      assert(h[0] == 1);
      static poly_t ln_t;
      const int t = n << 1;
    
      derivative(h, n, ln_t);
      std::fill(ln_t + n, ln_t + t, 0);
      polyinv(h, n, f);
    
      DFT(ln_t, t);
      DFT(f, t);
      for (int i = 0; i != t; ++i) ln_t[i] = (i64)ln_t[i] * f[i] % mod;
      IDFT(ln_t, t);
    
      integrate(ln_t, n, f);
    }
    
    void polyexp(const poly &h, const int n, poly &f) {
      /* f = exp(h) = f_0 (1 - ln f_0 + h) */
      assert(h[0] == 0);
      static poly_t exp_t;
      std::fill(f, f + n + n, 0);
      f[0] = 1;
      for (int t = 2; t <= n; t <<= 1) {
        const int t2 = t << 1;
    
        polyln(f, t, exp_t);
        exp_t[0] = sub(pls(h[0], 1), exp_t[0]);
        for (int i = 1; i != t; ++i) exp_t[i] = sub(h[i], exp_t[i]);
        std::fill(exp_t + t, exp_t + t2, 0);
    
        DFT(f, t2);
        DFT(exp_t, t2);
        for (int i = 0; i != t2; ++i) f[i] = (i64)f[i] * exp_t[i] % mod;
        IDFT(f, t2);
    
        std::fill(f + t, f + t2, 0);
      }
    }
    ```

### Example problems

1.  Compute $f^{k}(x)$

    The ordinary approach is polynomial binary exponentiation, with time complexity $O(n\log{n}\log{k})$.

    When $[x^{0}]f(x)=1$, we have:

    $$
    f^{k}(x)=\exp{\left(k\ln{f(x)}\right)}
    $$

    When $[x^{0}]f(x)\neq 1$, let $f_{i}x^{i}$ be the lowest-degree term of $f(x)$; then:

    $$
    f^{k}(x)=f_{i}^{k}x^{ik}\exp{\left(k\ln{\frac{f(x)}{f_{i}x^{i}}}\right)}
    $$

    **Time complexity**  $O(n\log{n})$.

## Polynomial trigonometric functions

Given a polynomial $f\left(x\right)$, find $\sin{f\left(x\right)}, \cos{f\left(x\right)}$ and $\tan{f\left(x\right)}$ modulo $x^{n}$.

### Solution

First, from [Euler's formula](../complex.md#欧拉公式) $\left(\mathrm{e}^{\mathrm{i}x} = \cos{x} + \mathrm{i}\sin{x}\right)$ we obtain [another expression of the trigonometric functions](https://en.wikipedia.org/wiki/Trigonometric_functions#Relationship_to_exponential_function_and_complex_numbers):

$$
\begin{aligned}
    \sin{x} &= \frac{\mathrm{e}^{\mathrm{i}x} - \mathrm{e}^{-\mathrm{i}x}}{2\mathrm{i}} \\
    \cos{x} &= \frac{\mathrm{e}^{\mathrm{i}x} + \mathrm{e}^{-\mathrm{i}x}}{2}
\end{aligned}
$$

Substituting $f\left(x\right)$ gives:

$$
\begin{aligned}
    \sin{f\left(x\right)} &= \frac{\exp{\left(\mathrm{i}f\left(x\right)\right)} - \exp{\left(-\mathrm{i}f\left(x\right)\right)}}{2\mathrm{i}} \\
    \cos{f\left(x\right)} &= \frac{\exp{\left(\mathrm{i}f\left(x\right)\right)} + \exp{\left(-\mathrm{i}f\left(x\right)\right)}}{2}
\end{aligned}
$$

Writing the program directly from the expressions above gives $\sin{f\left(x\right)}$ and $\cos{f\left(x\right)}$ modulo $x^{n}$. Then from $\tan{f\left(x\right)} = \frac{\sin{f\left(x\right)}}{\cos{f\left(x\right)}}$ we obtain $\tan{f\left(x\right)}$.

### Code

??? note "Polynomial trigonometric functions"
    Note that we perform the NTT over $\mathbb{Z}_{998244353}$, so accordingly the imaginary unit $\mathrm{i}$ should be replaced by $86583718$ or $911660635$:
    
    $$
    \begin{aligned}
               & \mathrm{i} = \sqrt{-1} \equiv \sqrt{998244352} \pmod{998244353}       \\
      \implies & \phantom{\text{or}} \quad \mathrm{i} \equiv 86583718 \pmod{998244353} \\
               & \text{or} \quad \mathrm{i} \equiv 911660635 \pmod{998244353}
    \end{aligned}
    $$
    
    ```cpp
    constexpr int MAXN = 262144;
    constexpr int mod = 998244353;
    constexpr int imgunit = 86583718; /* sqrt(-1) = sqrt(998233452) */
    
    using i64 = long long;
    using poly_t = int[MAXN];
    using poly = int *const;
    
    void polytri(const poly &h, const int n, poly &sin_t, poly &cos_t) {
      /* sin(f) = (exp(i * f) - exp(- i * f)) / 2i */
      /* cos(f) = (exp(i * f) + exp(- i * f)) / 2 */
      /* tan(f) = sin(f) / cos(f) */
      assert(h[0] == 0);
      static poly_t tri1_t, tri2_t;
    
      for (int i = 0; i != n; ++i) tri2_t[i] = (i64)h[i] * imgunit % mod;
      polyexp(tri2_t, n, tri1_t);
      polyinv(tri1_t, n, tri2_t);
    
      if (sin_t != nullptr) {
        const int invi = fpow(pls(imgunit, imgunit), mod - 2);
        for (int i = 0; i != n; ++i)
          sin_t[i] = (i64)(tri1_t[i] - tri2_t[i] + mod) * invi % mod;
      }
      if (cos_t != nullptr) {
        for (int i = 0; i != n; ++i) cos_t[i] = div2(pls(tri1_t[i], tri2_t[i]));
      }
    }
    ```

## Polynomial inverse trigonometric functions

Given a polynomial $f\left(x\right)$, find $\arcsin{f\left(x\right)}, \arccos{f\left(x\right)}$ and $\arctan{f\left(x\right)}$ modulo $x^{n}$.

### Solution

Following the method for the polynomial $\ln$, differentiating and then integrating the inverse trigonometric functions gives:

$$
\begin{aligned}
    \frac{\mathrm{d}}{\mathrm{d} x} \arcsin{x} &= \frac{1}{\sqrt{1 - x^{2}}} \\
    \arcsin{x} &= \int \frac{1}{\sqrt{1 - x^{2}}} \mathrm{d} x \\
    \frac{\mathrm{d}}{\mathrm{d} x} \arccos{x} &= - \frac{1}{\sqrt{1 - x^{2}}} \\
    \arccos{x} &= - \int \frac{1}{\sqrt{1 - x^{2}}} \mathrm{d} x \\
    \frac{\mathrm{d}}{\mathrm{d} x} \arctan{x} &= \frac{1}{1 + x^{2}} \\
    \arctan{x} &= \int \frac{1}{1 + x^{2}} \mathrm{d} x
\end{aligned}
$$

Substituting $f\left(x\right)$ gives:

$$
\begin{aligned}
    \frac{\mathrm{d}}{\mathrm{d} x} \arcsin{f\left(x\right)} &= \frac{f'\left(x\right)}{\sqrt{1 - f^{2}\left(x\right)}} \\
    \arcsin{f\left(x\right)} &= \int \frac{f'\left(x\right)}{\sqrt{1 - f^{2}\left(x\right)}} \mathrm{d} x \\
    \frac{\mathrm{d}}{\mathrm{d} x} \arccos{f\left(x\right)} &= - \frac{f'\left(x\right)}{\sqrt{1 - f^{2}\left(x\right)}} \\
    \arccos{f\left(x\right)} &= - \int \frac{f'\left(x\right)}{\sqrt{1 - f^{2}\left(x\right)}} \mathrm{d} x \\
    \frac{\mathrm{d}}{\mathrm{d} x} \arctan{f\left(x\right)} &= \frac{f'\left(x\right)}{1 + f^{2}\left(x\right)} \\
    \arctan{f\left(x\right)} &= \int \frac{f'\left(x\right)}{1 + f^{2}\left(x\right)} \mathrm{d} x
\end{aligned}
$$

It suffices to compute directly from the formulas.

### Code

??? note "Polynomial inverse trigonometric functions"
    ```cpp
    constexpr int MAXN = 262144;
    constexpr int mod = 998244353;
    
    using i64 = long long;
    using poly_t = int[MAXN];
    using poly = int *const;
    
    void derivative(const poly &h, const int n, poly &f) {
      for (int i = 1; i != n; ++i) f[i - 1] = (i64)h[i] * i % mod;
      f[n - 1] = 0;
    }
    
    void integrate(const poly &h, const int n, poly &f) {
      for (int i = n - 1; i; --i) f[i] = (i64)h[i - 1] * inv[i] % mod;
      f[0] = 0; /* C */
    }
    
    void polyarcsin(const poly &h, const int n, poly &f) {
      /* arcsin(f) = ∫ f' / sqrt(1 - f^2) dx  */
      static poly_t arcsin_t;
      const int t = n << 1;
      std::copy(h, h + n, arcsin_t);
      std::fill(arcsin_t + n, arcsin_t + t, 0);
    
      DFT(arcsin_t, t);
      for (int i = 0; i != t; ++i) arcsin_t[i] = sqr(arcsin_t[i]);
      IDFT(arcsin_t, t);
    
      arcsin_t[0] = sub(1, arcsin_t[0]);
      for (int i = 1; i != n; ++i)
        arcsin_t[i] = arcsin_t[i] ? mod - arcsin_t[i] : 0;
    
      polysqrt(arcsin_t, n, f);
      polyinv(f, n, arcsin_t);
      derivative(h, n, f);
    
      DFT(f, t);
      DFT(arcsin_t, t);
      for (int i = 0; i != t; ++i) arcsin_t[i] = (i64)f[i] * arcsin_t[i] % mod;
      IDFT(arcsin_t, t);
    
      integrate(arcsin_t, n, f);
    }
    
    void polyarccos(const poly &h, const int n, poly &f) {
      /* arccos(f) = - ∫ f' / sqrt(1 - f^2) dx  */
      polyarcsin(h, n, f);
      for (int i = 0; i != n; ++i) f[i] = f[i] ? mod - f[i] : 0;
    }
    
    void polyarctan(const poly &h, const int n, poly &f) {
      /* arctan(f) = ∫ f' / (1 + f^2) dx  */
      static poly_t arctan_t;
      const int t = n << 1;
      std::copy(h, h + n, arctan_t);
      std::fill(arctan_t + n, arctan_t + t, 0);
    
      DFT(arctan_t, t);
      for (int i = 0; i != t; ++i) arctan_t[i] = sqr(arctan_t[i]);
      IDFT(arctan_t, t);
    
      inc(arctan_t[0], 1);
      std::fill(arctan_t + n, arctan_t + t, 0);
    
      polyinv(arctan_t, n, f);
      derivative(h, n, arctan_t);
    
      DFT(f, t);
      DFT(arctan_t, t);
      for (int i = 0; i != t; ++i) arctan_t[i] = (i64)f[i] * arctan_t[i] % mod;
      IDFT(arctan_t, t);
    
      integrate(arctan_t, n, f);
    }
    ```

## References and links

[^ref1]: [Elementary function – Wikipedia](https://en.wikipedia.org/wiki/Elementary_function)
