---
title: Numerical integration
---

## Definition of the definite integral

Simply put, the definite integral $\int_{l}^{r}f(x)\mathrm{d}x$ of a function $f(x)$ over the interval $[l,r]$ is the area of the region enclosed by $f(x)$ and the $x$-axis over the interval $[l,r]$ (where the part above the $x$-axis counts as positive and the part below the $x$-axis counts as negative).

In many cases we need to compute an approximate value of an integral efficiently and accurately. **Simpson's method**, introduced below, is exactly such a method of numerical integration.

## Simpson's method

The idea of this method is to divide the interval of integration into several small segments and apply the integral formula for a quadratic function on each segment.

??? note "Integral formula for a quadratic function (Simpson's formula)"
    For a quadratic function $f(x)=ax^2+bx+c$ we have:
    
    $$
    \int_l^r f(x) {\mathrm d}x = \frac{(r-l)(f(l)+f(r)+4 f(\frac{l+r}{2}))}{6}
    $$
    
    Derivation:
    For a quadratic function $f(x)=ax^2+bx+c$;
    integrating gives $F(x)=\int_0^x f(x) {\mathrm d}x = \frac{a}{3}x^3+\frac{b}{2}x^2+cx+D$, where D is a constant, so
    
    $$
    \begin{aligned}
    \int_l^r f(x) {\mathrm d}x &= F(r)-F(l) \\
    &= \frac{a}{3}(r^3-l^3)+\frac{b}{2}(r^2-l^2)+c(r-l) \\
    &=(r-l)(\frac{a}{3}(l^2+r^2+lr)+\frac{b}{2}(l+r)+c) \\
    &=\frac{r-l}{6}(2al^2+2ar^2+2alr+3bl+3br+6c)\\
    &=\frac{r-l}{6}((al^2+bl+c)+(ar^2+br+c)+4(a(\frac{l+r}{2})^2+b(\frac{l+r}{2})+c)) \\
    &=\frac{r-l}{6}(f(l)+f(r)+4f(\frac{l+r}{2}))
    \end{aligned}
    $$

Based on this Simpson's formula, we first introduce the plain Simpson's method of integration.

### Plain Simpson's method

In 1743, this method was published in a paper by Thomas Simpson.

#### Description

Given a natural number $n$, divide the interval $[l, r]$ into $2n$ intervals $x$ of equal length.

$x_i = l + i h, ~~ i = 0 \ldots 2n,$ $h = \frac {r-l} {2n}.$

Then we can compute the value of the integral on every small interval $[x_ {2i-2}, x_ {2i}]$, $i = 1\ldots n$; the sum of the integral values over all intervals is the total integral.

For one interval $[x_ {2i-2}, x_ {2i}]$, $i = 1\ldots n$, choose the three points $(x_ {2i-2}, x_ {2i-1}, x_ {2i})$ in it; they determine a parabola and hence a function $P(x)$, which exists and is unique. Computing the integral of the original function on this interval thus becomes computing the integral of the new quadratic function $P(x)$ on this interval. This we can approximate using Simpson's formula.

$\int_{x_ {2i-2}} ^ {x_ {2i}} f (x) ~dx \approx \int_{x_ {2i-2}} ^ {x_ {2i}} P (x) ~dx = \left(f(x_{2i-2}) + 4f(x_{2i-1})+(f(x_{2i})\right)\frac {h} {3}$

Summing over the segments gives the following conclusion:

$\int_l ^ r f (x) dx \approx \left(f (x_0) + 4 f (x_1) + 2 f (x_2) + 4f(x_3) + 2 f(x_4) + \ldots + 4 f(x_{2N-1}) + f(x_{2N}) \right)\frac {h} {3}$

#### Error

We state the result directly: the error of the plain Simpson's method is:

$$
-\tfrac{1}{90} \left(\tfrac{r-l}{2}\right)^5 f^{(4)}(\xi)
$$

where $\xi$ is some value in the interval $[l,r]$.

#### Implementation

=== "C++"
    ```cpp
    constexpr int N = 1000 * 1000;
    
    double simpson_integration(double a, double b) {
      double h = (b - a) / N;
      double s = f(a) + f(b);
      for (int i = 1; i <= N - 1; ++i) {
        double x = a + h * i;
        s += f(x) * ((i & 1) ? 4 : 2);
      }
      s *= h / 3;
      return s;
    }
    ```

=== "Python"
    ```python
    N = 1000 * 1000
    
    
    def simpson_integration(a, b):
        h = (b - a) / N
        s = f(a) + f(b)
        for i in range(1, N):
            x = a + h * i
            if i & 1:
                s = s + f(x) * 4
            else:
                s = s + f(x) * 2
        s = s * (h / 3)
        return s
    ```

### Adaptive Simpson's method

To guarantee precision, the plain method is inevitably limited in time by $n$; we should look for a more suitable method.

The only remaining problem is how to split the interval. If there are too few segments the computational error is large; if there are too many, the time efficiency is low. We need to find a balance between accuracy and efficiency.

We reason as follows: if a segment of the graph is already very close to a quadratic function, then substituting it directly into the formula gives an integral of very high precision, and there is no need to split this segment further.

So we have the following splitting method: each time, judge how similar the current segment is to a quadratic function; if it is similar enough, substitute it directly into the formula, otherwise split the current segment into a left and a right part and solve recursively.

Only one problem remains: how to judge whether a segment is similar to a quadratic function?

We substitute the current segment directly into the formula to get its integral, then split the current segment at its midpoint into two parts and substitute both parts directly into the formula as well. If the integral of the current segment and the sum of the integrals of the two parts after splitting differ very little, we may consider the current segment very similar to a quadratic function, and there is no need to split it recursively any further.

The above is the idea of the adaptive Simpson's method. When deciding in the divide-and-conquer step, besides checking whether the precision is satisfied, a minimum number of iterations is usually enforced as well.

Reference code:

=== "C++"
    ```cpp
    double simpson(double l, double r) {
      double mid = (l + r) / 2;
      return (r - l) * (f(l) + 4 * f(mid) + f(r)) / 6;  // Simpson's formula
    }
    
    double asr(double l, double r, double eps, double ans, int step) {
      double mid = (l + r) / 2;
      double fl = simpson(l, mid), fr = simpson(mid, r);
      if (abs(fl + fr - ans) <= 15 * eps && step < 0)
        return fl + fr + (fl + fr - ans) / 15;  // if similar enough, return directly
      return asr(l, mid, eps / 2, fl, step - 1) +
             asr(mid, r, eps / 2, fr, step - 1);  // otherwise split into two parts and solve recursively
    }
    
    double calc(double l, double r, double eps) {
      return asr(l, r, eps, simpson(l, r), 12);
    }
    ```

=== "Python"
    ```python
    def simpson(l, r):
        mid = (l + r) / 2
        return (r - l) * (f(l) + 4 * f(mid) + f(r)) / 6  # Simpson's formula
    
    
    def asr(l, r, eps, ans, step):
        mid = (l + r) / 2
        fl = simpson(l, mid)
        fr = simpson(mid, r)
        if abs(fl + fr - ans) <= 15 * eps and step < 0:
            return fl + fr + (fl + fr - ans) / 15  # if similar enough, return directly
        return asr(l, mid, eps / 2, fl, step - 1) + asr(
            mid, r, eps / 2, fr, step - 1
        )  # otherwise split into two parts and solve recursively
    
    
    def calc(l, r, eps):
        return asr(l, r, eps, simpson(l, r), 12)
    ```

## Exercises

-   [Luogu4525【模板】自适应辛普森法 1 (Template: Adaptive Simpson's Method 1)](https://www.luogu.com.cn/problem/P4525)
-   [HDU1724 Ellipse](https://acm.hdu.edu.cn/showproblem.php?pid=1724)
-   [NOI2005 月下柠檬树 (Lemon Tree Under the Moon)](https://www.luogu.com.cn/problem/P4207)

## References

<https://doi.org/10.1145/321526.321537>: This article discusses improvements to the adaptive Simpson's method, and in it the origin and advantage of the constant `15` in the code above are discussed in detail.
