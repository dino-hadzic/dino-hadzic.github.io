---
title: Fundamental theorem of algebra
---

## Definition

Every univariate polynomial equation of degree $n$ with complex coefficients ($n$ at least $1$) has at least one root in the field of complex numbers.

It follows that a polynomial equation of degree $n$ with complex coefficients has exactly $n$ roots in the field of complex numbers, counting multiple roots with multiplicity.

Sometimes the theorem is also stated as:

Every nonzero univariate polynomial of degree $n$ with complex coefficients has exactly $n$ complex roots.

The proof of the fundamental theorem of algebra usually relies on complex analysis or modern algebra, so the theorem is most often applied directly as a well-known result.

By the fundamental theorem of algebra, a polynomial with complex coefficients $f(x)=a_nx^n+a_{n-1}x^{n-1}+\ldots+a_0$ can always be uniquely factored as:

$$
f(x)=a_n{(x-x_1)}^{k_1}{(x-x_2)}^{k_2}\ldots{(x-x_t)}^{k_t}
$$

where all the roots are complex numbers and $k_1+k_2+\ldots+k_t=n$.

## Complex conjugate root theorem

The objects studied by the fundamental theorem of algebra are polynomials with complex coefficients. When studying polynomials with real coefficients, although they can also be factored into complex roots, the scope of the study has to be enlarged, which is not very convenient.

Imaginary root: a root that is not real.

Theorem: the complex conjugate of a root of a polynomial with real coefficients is also a root of that polynomial.

Proof: take the conjugate of both sides of the equation in the fundamental theorem of algebra directly, and the proof is complete.

If the root itself is real, taking the conjugate leaves it unchanged, so nothing is affected.

If the root is imaginary, then the complex conjugate of the imaginary root is also a root of the original polynomial. Thus the two imaginary roots can be paired up.

Theorem: the conjugate imaginary roots of an equation with real coefficients always appear in pairs, and the multiplicities of conjugate imaginary roots are equal.

Proof: suppose one root is $a+b\mathrm{i}$; then another root is $a-b\mathrm{i}$. This means that two factors appear in the factorization:

$$
(x-a-b\mathrm{i})(x-a+b\mathrm{i})=x^2-2ax+a^2+b^2
$$

We can see that when the two factors are multiplied together, all coefficients become real numbers. The quadratic polynomial with real coefficients on the right-hand side of this equation divides the original polynomial.

Hence, dividing both sides of the equation in the fundamental theorem of algebra by this quadratic trinomial, we again obtain an equation of polynomials with real coefficients. Repeat the operation on the new equation; as the degree decreases, after a number of steps no imaginary roots remain.

Therefore the multiplicities of each pair of conjugate imaginary roots are equal. This completes the proof.

The following are corollaries of the complex conjugate root theorem:

-   A polynomial of odd degree with real coefficients has at least one real root, and has an odd number of real roots in total.
-   A polynomial of even degree with real coefficients may have no real roots, and has an even number of real roots in total.

The quadratic trinomial above, $x^2-2ax+a^2+b^2=x^2+px+q$, is called an irreducible quadratic factor with real coefficients. Irreducible means that it cannot be factored over the real numbers.

Theorem: a polynomial with real coefficients is always a product of irreducible factors with real coefficients of degree one or two.

Proof:

Whenever a polynomial with real coefficients has a real root $c$, there is a corresponding factor $x-c$ with real coefficients; whenever it has a pair of imaginary roots $a\pm b\mathrm{i}$, there is a corresponding factor $x^2-2ax+a^2+b^2$ with real coefficients.

Therefore it suffices to pair up the roots in the original factorization from the fundamental theorem of algebra using the complex conjugate root theorem, and the proof is complete.

By the complex conjugate root theorem, a polynomial with real coefficients $f(x)=a_nx^n+a_{n-1}x^{n-1}+\ldots+a_0$ can always be uniquely factored as:

$$
f(x)=a_n{(x-x_1)}^{k_1}{(x-x_2)}^{k_2}\ldots{(x-x_t)}^{k_t}{(x^2+p_1x+q_1)}^{l_1}{(x^2+p_2x+q_2)}^{l_2}\ldots{(x^2+p_sx+q_s)}^{l_s}
$$

where all coefficients are real numbers and $k_1+k_2+\ldots+k_t+2(l_1+l_2+\ldots+l_s)=n$.

## Lin's algorithm (Lin–Bairstow method)

### Introduction

How do we carry out the factorization of the fundamental theorem of algebra for a polynomial with real coefficients? Extending the number field to the complex numbers would be very complicated.

If we factor only over the real numbers, we can only guarantee that, when the degree is greater than $2$, a factor that is a quadratic trinomial with real coefficients always exists.

This is because, if the polynomial has imaginary roots, we directly put together a pair of conjugate imaginary roots. If the polynomial has only real roots, taking any two real roots and multiplying the corresponding linear factors also yields a factor that is a quadratic trinomial with real coefficients.

Once a quadratic trinomial factor is found, solving the quadratic for its real or complex roots is extremely easy. This leads to a computational method that successively **finds one quadratic factor** at a time to obtain the complex roots of the equation; this method avoids complex arithmetic.

In August 1940, August 1943, and July 1947, Lin Shih-nge (林士谔) successively published 3 papers on a method for solving the complex roots of high-order equations[^note1] in the Journal of Mathematics and Physics published by MIT, with improvements each time.

This method is still used today for fast computation on modern computers; the polynomial root-finding routines in software packages (such as MATLAB) are also based on the principle of this algorithm.

### Process

To find a quadratic trinomial factor, the polynomial has to be factored as:

$$
f(x)=(x^2+p_1x+q_1)g(x)
$$

Since the quadratic trinomial factor cannot be found all at once, following the idea of iterative solving, for the initial value we have:

$$
f(x)=(x^2+px+q)g(x)+rx+s
$$

which produces a linear expression as the remainder. As long as the remainder is small enough, the desired factor has been found approximately.

We want the final solution to be the initial value plus an offset correction:

$$
p_1=p+dp
$$

$$
q_1=q+dq
$$

The two numbers $(r, s)$ in the remainder are determined by the given coefficients $(p, q)$ of the divisor. The partial-derivative relations hold:

$$
dr=\frac{\partial r}{\partial p}dp+\frac{\partial r}{\partial q}dq
$$

$$
ds=\frac{\partial s}{\partial p}dp+\frac{\partial s}{\partial q}dq
$$

In the initial equation the dividend $f(x)$ is given, while the quotient $g(x)$ and the remainder $rx+s$ change as the divisor $x^2+px+q$ changes. Hence we have the partial-derivative relations

$$
0=xg(x)+\frac{\partial g(x)}{\partial p}(x^2+px+q)+\frac{\partial r}{\partial p}x+\frac{\partial s}{\partial p}
$$

$$
0=g(x)+\frac{\partial g(x)}{\partial q}(x^2+px+q)+\frac{\partial r}{\partial q}x+\frac{\partial s}{\partial q}
$$

Note that a partial derivative is just a number, independent of the variable $x$. Hence we have the divisibility relations

$$
xg(x)=-\frac{\partial g(x)}{\partial p}(x^2+px+q)-\frac{\partial r}{\partial p}x-\frac{\partial s}{\partial p}
$$

$$
g(x)=-\frac{\partial g(x)}{\partial q}(x^2+px+q)-\frac{\partial r}{\partial q}x-\frac{\partial s}{\partial q}
$$

The conclusion here is that the desired partial derivatives are exactly the remainders of continuing the division on the quotient. Division of a polynomial by a given quadratic trinomial is computed directly. This gives the four partial derivatives.

We want $s$ and $r$ plus the offsets $ds$ and $dr$ to become $0$, i.e. $ds$ and $dr$ are the negatives of $s$ and $r$. Hence we need to solve the equations:

$$
-\frac{\partial r}{\partial p}dp-\frac{\partial r}{\partial q}dq=r
$$

$$
-\frac{\partial s}{\partial p}dp-\frac{\partial s}{\partial q}dq=s
$$

From the above system of equations we obtain the offsets $dp$ and $dq$ corresponding to $p$ and $q$; it suffices to solve it directly with a second-order determinant.

### Implementation

```C
// a is the original polynomial, n is the degree of the polynomial, p is the linear coefficient to be found, q is the constant term to be found
void Shie(double a[], int n, double *p, double *q) {
  // array b is the quotient of polynomial a divided by the quadratic trinomial of the current iteration
  memset(b, 0, sizeof(b));
  // array c is the quotient of polynomial b times x squared divided by the quadratic trinomial of the current iteration
  memset(c, 0, sizeof(c));
  *p = 0;
  *q = 0;
  double dp = 1;
  double dq = 1;
  while (dp > eps || dp < -eps || dq > eps || dq < -eps)  // set eps yourself
  {
    double p0 = p;
    double q0 = q;
    b[n - 2] = a[n];
    c[n - 2] = b[n - 2];
    b[n - 3] = a[n - 1] - p0 * b[n - 2];
    c[n - 3] = b[n - 3] - p0 * b[n - 2];
    int j;
    for (j = n - 4; j >= 0; j--) {
      b[j] = a[j + 2] - p0 * b[j + 1] - q0 * b[j + 2];
      c[j] = b[j] - p0 * c[j + 1] - q0 * c[j + 2];
    }
    double r = a[1] - p0 * b[0] - q0 * b[1];
    double s = a[0] - q0 * b[0];
    double rp = c[1];
    double sp = b[0] - q0 * c[2];
    double rq = c[0];
    double sq = -q0 * c[1];
    dp = (rp * s - r * sp) / (rp * sq - rq * sp);
    dq = (r * sq - rq * s) / (rp * sq - rq * sp);
    *p += dp;
    *q += dq;
  }
}
```

## References and notes

[^note1]: [林士谔．论劈因法解高阶特征方程根值的应用问题．数学进展，1963(03):207-217. (Lin Shih-nge. On the application of the factor-splitting method to solving the roots of high-order characteristic equations. Advances in Mathematics, 1963(03):207-217.)](https://cnki.net/kcms/detail/detail.aspx?filename=SXJZ196303000&dbcode=CJFD&dbname=CJFD1979)
