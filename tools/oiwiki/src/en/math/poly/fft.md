---
title: Fast Fourier transform
---

Prerequisites: [Complex numbers](../complex.md).

This article introduces an algorithm that computes the product of two polynomials of degree $n$ in $O(n\log n)$ time, more efficiently than the naive $O(n^2)$ algorithm. Since the multiplication of two integers can also be regarded as polynomial multiplication, this algorithm can also be used to speed up the multiplication of large integers.

## Introduction

Let us introduce two polynomials $A$ and $B$:

$$
\begin{aligned}
A ={}& 5x^2 + 3x + 7 \\
B ={}& 7x^2 + 2x + 1 \\
\end{aligned}
$$

The product of the two polynomials, $C = A \times B$, can be computed in $O(n^2)$ time complexity (here $n$ is the degree of the polynomial $A$ or $B$):

$$
\begin{aligned}
C ={}& A \times B \\
  ={}& 35x^4 + 31x^3 + 60x^2 + 17x + 7
\end{aligned}
$$

Clearly the coefficients $c_i$ of the polynomial $C$ satisfy $c_i = \sum_{j = 0}^i a_j b_{i - j}$. For this naive algorithm, computing each term takes $O(n)$ time, and there are $O(n)$ terms in total, so the time complexity is $O(n^2)$.

Can we speed it up and reduce its time complexity? If we use the fast Fourier transform, we can reduce the complexity to $O(n \log n)$.

## Fourier transform

The Fourier transform is a method for analyzing signals: it can analyze the components of a signal, and it can also synthesize a signal from those components. Many waveforms can serve as components of a signal; the Fourier transform uses sine waves as the components.

Let $f(t)$ be a function of time $t$; then the Fourier transform can detect to what extent a period of frequency $\omega$ appears in $f(t)$:

$$
F(\omega)=\mathbb{F}[f(t)]=\int_{-\infty}^{\infty}f(t)\mathrm{e}^{-\mathrm{i}{\omega}t}dt
$$

Its inverse transform is

$$
f(t)=\mathbb{F}^{-1}[F(\omega)]=\frac{1}{2\pi}\int_{-\infty}^{\infty}F(\omega)\mathrm{e}^{\mathrm{i}{\omega}t}d\omega
$$

The form of the inverse transform is very similar to that of the forward transform; the denominator $2\pi$ is exactly the period of the exponential function.

The Fourier transform amounts to a continuous inner product of the time-domain function with a complex exponential function of period $2\pi$. The inverse transform is again an inner product.

The Fourier transform has a corresponding convolution theorem: a convolution in the time domain can be turned into a product in the frequency domain, and a convolution in the frequency domain can be turned into a product in the time domain.

## Discrete Fourier transform

The **discrete Fourier transform** (DFT) is the form of the Fourier transform that is discrete in both the time domain and the frequency domain; it transforms the time-domain samples of a signal into frequency-domain samples of its DTFT (discrete-time Fourier transform).

The Fourier transform is a continuous inner product of functions in integral form; the discrete Fourier transform is an inner product in summation form.

Let $\{x_n\}_{n=0}^{N-1}$ be a sequence satisfying a finiteness condition; its discrete Fourier transform (DFT) is:

$$
X_k=\sum_{n=0}^{N-1}x_n\mathrm{e}^{-\mathrm{i}\frac{2\pi}{N}kn}
$$

where $\mathrm{e}$ is the base of the natural logarithm and $i$ is the imaginary unit. The transform is usually denoted by the symbol $\mathcal {F}$, i.e.

$$
\hat{x}=\mathcal{F}x
$$

Similarly to the integral form, its **inverse discrete Fourier transform** (IDFT) is:

$$
x_n=\frac{1}{N}\sum_{k=0}^{N-1}X_k\mathrm{e}^{\mathrm{i}\frac{2\pi}{N}kn}
$$

which can be written as:

$$
x=\mathcal{F}^{-1}\hat{x}
$$

In fact, the normalization coefficients in front of the sums in the DFT and IDFT formulas are not important. In the definition above, the coefficients in front of the DFT and the IDFT are $1$ and $\frac {1}{N}$ respectively. Sometimes we change both coefficients to $\frac{1}{{\sqrt{N}}}$.

The discrete Fourier transform is still a transform from the time domain to the frequency domain. Due to the special nature of the summation form, other interpretations are possible.

If we regard the sequence $x_n$ as the coefficients of the $x^n$ terms of a polynomial $f(x)$, then the computed $X_k$ is exactly the value $f(\mathrm{e}^{\frac{-2\pi \mathrm{i}k}{N}})$ of the polynomial $f(x)$ at the root of unity $\mathrm{e}^{\frac{-2\pi \mathrm{i}k}{N}}$.

This gives another interpretation of the convolution theorem, namely as a special evaluation operation on polynomials. The discrete Fourier transform is exactly the evaluation of a polynomial at the roots of unity.

For example, let us compute:

$$
\dbinom{n}{3}+\dbinom{n}{7}+\dbinom{n}{11}+\dbinom{n}{15}+\ldots
$$

Define the function $f(x)$ as:

$$
f(x)={(1+x)}^n=\dbinom{n}{0}x^0+\dbinom{n}{1}x^1+\dbinom{n}{2}x^2+\dbinom{n}{3}x^3+\ldots
$$

Then we notice that substituting the fourth root of unity, $f(\mathrm{i})$, gives the following sequence:

$$
f(\mathrm{i})={(1+\mathrm{i})}^n=\dbinom{n}{0}+\dbinom{n}{1}\mathrm{i}-\dbinom{n}{2}-\dbinom{n}{3}\mathrm{i}+\ldots
$$

So the following sum cancels exactly all the other terms:

$$
f(1)+\mathrm{i}f(\mathrm{i})-f(-1)-\mathrm{i}f(-\mathrm{i})=4\dbinom{n}{3}+4\dbinom{n}{7}+4\dbinom{n}{11}+4\dbinom{n}{15}+\ldots
$$

Hence the answer to this math problem is:

$$
\dbinom{n}{3}+\dbinom{n}{7}+\dbinom{n}{11}+\dbinom{n}{15}+\ldots=\frac{2^n+\mathrm{i}(1+\mathrm{i})^n-\mathrm{i}(1-\mathrm{i})^n}{4}
$$

This math problem evaluates at the roots of unity, which is exactly a discrete Fourier transform.

### Matrix formula

Since the discrete Fourier transform is a **linear** operator, it can be described by matrix multiplication. In matrix notation, the discrete Fourier transform is expressed as follows:

$$
\begin{bmatrix}
    X_{0}  \\
    X_{1}  \\
    X_{2}  \\
    \vdots \\
    X_{N-1}
\end{bmatrix}
=
\begin{bmatrix}
    1      & 1            & 1               & \cdots & 1                   \\
    1      & \alpha       & \alpha^{2}      & \cdots & \alpha^{N-1}        \\
    1      & \alpha^{2}   & \alpha^{4}      & \cdots & \alpha^{2(N-1)}     \\
    \vdots & \vdots       & \vdots          & \ddots & \vdots              \\
    1      & \alpha^{N-1} & \alpha^{2(N-1)} & \cdots & \alpha^{(N-1)(N-1)}
\end{bmatrix}
\begin{bmatrix}
    x_{0}  \\
    x_{1}  \\
    x_{2}  \\
    \vdots \\
    x_{N-1}
\end{bmatrix}
$$

where $\alpha = \mathrm{e}^{-\mathrm{i}\frac{2\pi}{N}}$.

## Fast Fourier transform

The FFT is an efficient algorithm for implementing the DFT, called the fast Fourier transform (FFT). It makes no new discoveries in the theory of the Fourier transform, but for applying the discrete Fourier transform in computer systems, or digital systems, it is a big step forward. The fast number-theoretic transform (NTT) is an implementation of the fast Fourier transform (FFT) on a number-theoretic basis.

In 1965, Cooley and Tukey published the fast Fourier transform algorithm. In fact the FFT had been discovered long before that, but at the time modern computers did not yet exist and people did not realize the importance of the FFT. Some investigators believe that the FFT was discovered by Runge and König in 1924. But in fact Gauss had already invented the algorithm in 1805, though he never published it.

### Divide-and-conquer implementation

The basic idea of the FFT algorithm is divide and conquer. For the DFT, it computes the value of $f(x)$ at $x=\omega_n^k$ in a divide-and-conquer fashion. The divide-and-conquer idea of the radix-2 FFT manifests itself in splitting the polynomial into odd-degree and even-degree terms.

For example, for a polynomial with $8$ terms in total:

$$
f(x) = a_0 + a_1x + a_2x^2+a_3x^3+a_4x^4+a_5x^5+a_6x^6+a_7x^7
$$

Split it into two groups by the parity of the degree, then factor an $x$ out of the right one:

$$
\begin{aligned}
f(x) &= (a_0+a_2x^2+a_4x^4+a_6x^6) + (a_1x+a_3x^3+a_5x^5+a_7x^7)\\
     &= (a_0+a_2x^2+a_4x^4+a_6x^6) + x(a_1+a_3x^2+a_5x^4+a_7x^6)
\end{aligned}
$$

Build new functions from the coefficients of the even-degree and odd-degree terms separately:

$$
\begin{aligned}
G(x) &= a_0+a_2x+a_4x^2+a_6x^3\\
H(x) &= a_1+a_3x+a_5x^2+a_7x^3
\end{aligned}
$$

Then the original $f(x)$ is expressed in terms of the new functions as:

$$
f(x)=G\left(x^2\right) + x  \times  H\left(x^2\right)
$$

Using the property of roots of unity of even order $\omega^i_n = -\omega^{i + n/2}_n$, and the fact that $G\left(x^2\right)$ and $H\left(x^2\right)$ are even functions, we know that in the complex plane $\omega^i_n$ and $\omega^{i+n/2}_n$ give the same values of $G(x^2)$ and $H(x^2)$. We get:

$$
\begin{aligned}
f(\omega_n^k) &= G((\omega_n^k)^2) + \omega_n^k  \times H((\omega_n^k)^2) \\
              &= G(\omega_n^{2k}) + \omega_n^k  \times H(\omega_n^{2k}) \\
              &= G(\omega_{n/2}^k) + \omega_n^k  \times H(\omega_{n/2}^k)
\end{aligned}
$$

and:

$$
\begin{aligned}
f(\omega_n^{k+n/2}) &= G(\omega_n^{2k+n}) + \omega_n^{k+n/2}  \times H(\omega_n^{2k+n}) \\
                    &= G(\omega_n^{2k}) - \omega_n^k  \times H(\omega_n^{2k}) \\
                    &= G(\omega_{n/2}^k) - \omega_n^k  \times H(\omega_{n/2}^k)
\end{aligned}
$$

Therefore, once we have computed $G(\omega_{n/2}^k)$ and $H(\omega_{n/2}^k)$, we can obtain both $f(\omega_n^k)$ and $f(\omega_n^{k+n/2})$ at the same time. So it suffices to recursively perform the DFT on $G$ and $H$.

Considering that the polynomial length the divide-and-conquer DFT can handle can only be $2^m(m \in \mathbf{N}^ \ast )$ — otherwise the left and right halves would have different lengths when splitting, and the right half would run out of coefficients — before the first DFT the sequence has to be padded up to length $2^m(m \in \mathbf{N}^\ast )$ (high-degree coefficients padded with $0$), i.e. a polynomial whose highest degree is $2^m-1$.

When substituting values, since $n$ distinct values have to be substituted, we substitute $\omega_n^0,\omega_n^1,\omega_n^2,\cdots, \omega_n^{n-1} (n=2^m(m \in \mathbf{N}^ \ast ))$, a total of $2^m$ distinct values.

As for the implementation, the STL provides a template for complex numbers, and of course one can also implement them by hand. The difference is that with the STL `complex` one can call the `exp` function to compute $\omega_n$. But in fact computing $\omega_n$ via the imaginary numbers obtained from Euler's formula is equivalent.

This concludes the introduction to the DFT in the FFT algorithm: it converts a polynomial from the coefficient representation to the point-value representation.

It is worth noting that, because we use complex roots of unity, we need to pad the high-degree terms of the $n$-term polynomial with zeros so that $n = 2 ^ k, k \in \mathbf{N}^ \ast$.

???+ note "Recursive FFT"
    ```cpp
    #include <cmath>
    #include <complex>
    
    using Comp = std::complex<double>;  // STL complex
    
    constexpr Comp I(0, 1);  // i
    constexpr int MAX_N = 1 << 20;
    
    Comp tmp[MAX_N];
    
    // rev=1, DFT; rev=-1, IDFT
    // after applying this function, take care of the normalization coefficient
    void DFT(Comp* f, int n, int rev) {
      if (n == 1) return;
      for (int i = 0; i < n; ++i) tmp[i] = f[i];
      // even indices go to the left, odd indices go to the right
      for (int i = 0; i < n; ++i) {
        if (i & 1)
          f[n / 2 + i / 2] = tmp[i];
        else
          f[i / 2] = tmp[i];
      }
      Comp *g = f, *h = f + n / 2;
      // recursive DFT
      DFT(g, n / 2, rev), DFT(h, n / 2, rev);
      // cur is the current complex root of unity; for k = 0 the corresponding root of unity is omega^0_n = 1.
      // step is the difference between two roots of unity, i.e. it satisfies omega^k_n = step*omega^{k-1}*n,
      // the definition is equivalent to exp(I*(-2*M_PI/n*rev))
      Comp cur(1, 0), step(cos(2 * M_PI / n), sin(-2 * M_PI * rev / n));
      for (int k = 0; k < n / 2;
           ++k) {  // F(omega^k_n) = G(omega^k*{n/2}) + omega^k*n\*H(omega^k*{n/2})
        tmp[k] = g[k] + cur * h[k];
        // F(omega^{k+n/2}*n) = G(omega^k*{n/2}) - omega^k_n*H(omega^k\_{n/2})
        tmp[k + n / 2] = g[k] - cur * h[k];
        cur *= step;
      }
      for (int i = 0; i < n; ++i) f[i] = tmp[i];
    }
    ```

The time complexity is $O(n\log n)$.

### Implementation by doubling

This algorithm can be optimized further from the "divide and conquer" point of view. In the radix-2 FFT, each time we separate the coefficients of the odd-degree and even-degree terms of the whole polynomial, until only one coefficient is left. However, this recursive process needs more memory. Therefore we can first "imitate the recursion" to "split" these coefficients in the original array, and then merge the computed values by "doubling".

For the "splitting", the bit-reversal permutation can be used.

For the "merging", the butterfly optimization makes it possible to use only $O(1)$ extra space.

#### Bit-reversal permutation

Taking a polynomial with $8$ terms as an example, let us simulate the splitting process:

-   The initial sequence is $\{x_0, x_1, x_2, x_3, x_4, x_5, x_6, x_7\}$
-   After one split $\{x_0, x_2, x_4, x_6\},\{x_1, x_3, x_5, x_7 \}$
-   After two splits $\{x_0,x_4\} \{x_2, x_6\},\{x_1, x_5\},\{x_3, x_7 \}$
-   After three splits $\{x_0\}\{x_4\}\{x_2\}\{x_6\}\{x_1\}\{x_5\}\{x_3\}\{x_7 \}$

The pattern: it is just the original sequence where each number is written in binary and then the binary representation is reversed — that is the index of the final position. For example, $x_1$ is 001, reversed it is 100, i.e. 4, and the final position is indeed 4. We call this transformation the bit-reversal permutation; the proof is left to the reader.

By its definition, we can compute the result of the transformation for every number in $O(n)$ time:

???+ note "Bit-reversal permutation implementation ($O(n)$)"
    ```cpp
    /*
     * The permutation performed before the FFT and IFFT
     * Position i is swapped with the position obtained by reversing the binary representation of i
     * len must be a power of 2
     */
    void change(Complex y[], int len) {
      // Initially i is 0...01 and j is 10...0, which are mirror images in binary.
      // Afterwards i is incremented by one, while j keeps being the mirror image of i, until i = 1...11.
      for (int i = 1, j = len / 2, k; i < len - 1; i++) {
        // Swap the elements whose indices are bit-reversals of each other; i < j guarantees each swap happens once
        if (i < j) swap(y[i], y[j]);
        // i does a normal + 1, j does a reversed + 1, so that i and j always stay reversals of each other.
        // Here k stands for the highest bit where a 0 appears. j first subtracts the high bits that are all 1,
        // until a 0 is met, and then it suffices to add.
        // Consider the number of times each bit of j flips: the highest bit flips n times,
        // the second highest n/2 times, and so on, so the time complexity is:
        // T(n) = n + n/2 + n/4 + ... = O(n)
        k = len / 2;
        while (j >= k) {
          j = j - k;
          k = k / 2;
        }
        j += k;
      }
    }
    ```

The bit-reversal permutation can also be computed in $O(n)$ by a recurrence from small to large: let $len=2^k$, where $k$ is the length of the binary representation, and let $R(x)$ denote the number obtained by reversing the $k$-bit binary representation of $x$ (padded with $0$ in the high bits). We want $R(0),R(1),\cdots,R(n-1)$.

First, $R(0)=0$.

We compute $R(x)$ from small to large. Hence when computing $R(x)$, the value of $R\left(\left\lfloor \dfrac{x}{2} \right\rfloor\right)$ is already known. So we shift $x$ right by one bit (divide by $2$), reverse it, and shift right by one bit again, which gives the reversal of all bits of $x$ **except the (binary) units digit**.

Consider the reversal of the units digit: if the units digit is $0$, the highest bit after reversal is $0$. If the units digit is $1$, the highest bit after reversal is $1$, so we also have to add $\dfrac{len}{2}=2^{k-1}$. In summary

$$
R(x)=\left\lfloor \frac{R\left(\left\lfloor \frac{x}{2} \right\rfloor\right)}{2} \right\rfloor + (x\bmod 2)\times \frac{len}{2}
$$

An example: let $k=5$, $len=(100000)_2$. To reverse $(11001)_2$:

1.  Consider $(1100)_2$; we know $R((1100)_2)=R((01100)_2)=(00110)_2$, and shifting right by one more bit gives $(00011)_2$.
2.  Consider the units digit: if it is $1$, it has to be reversed to the highest bit of the number, i.e. add $(10000)_2=2^{k-1}$ to the reversed number; if it is $0$, no change is needed.

???+ note "Bit-reversal permutation implementation ($O(n)$)"
    ```cpp
    // Likewise, len must be guaranteed to be a power of 2
    // Let rev[i] be the value of i after reversal
    void change(Complex y[], int len) {
      for (int i = 0; i < len; ++i) {
        rev[i] = rev[i >> 1] >> 1;
        if (i & 1) {  // if the last bit is 1, it is reversed to len/2
          rev[i] |= len >> 1;
        }
      }
      for (int i = 0; i < len; ++i) {
        if (i < rev[i]) {  // guarantees that each pair is swapped only once
          swap(y[i], y[rev[i]]);
        }
      }
      return;
    }
    ```

#### Butterfly optimization

Knowing $G(\omega_{n/2}^k)$ and $H(\omega_{n/2}^k)$, we need to use the following two formulas to compute $f(\omega_n^k)$ and $f(\omega_n^{k+n/2})$:

$$
\begin{aligned}
    f(\omega_n^k)       & = G(\omega_{n/2}^k) + \omega_n^k \times H(\omega_{n/2}^k) \\
    f(\omega_n^{k+n/2}) & = G(\omega_{n/2}^k) - \omega_n^k \times H(\omega_{n/2}^k)
\end{aligned}
$$

After the bit-reversal permutation, for given $n, k$:

-   The value of $G(\omega_{n/2}^k)$ is stored at array index $k$, and the value of $H(\omega_{n/2}^k)$ is stored at array index $k + \dfrac{n}{2}$.
-   The value of $f(\omega_n^k)$ will be stored at array index $k$, and the value of $f(\omega_n^{k+n/2})$ will be stored at array index $k + \dfrac{n}{2}$.

Therefore we can directly overwrite the values at array indices $k$ and $k + \frac{n}{2}$, without allocating an extra array to store the values. This method is called the **butterfly operation**, or more precisely the radix-2 butterfly operation.

Let us explain in more detail how to use the butterfly operation to perform all merges of segments of length $\frac{n}{2}$:

1.  Let the segment length be $s = \frac{n}{2}$;
2.  Simultaneously enumerate the left endpoints $l_g = 0, 2s, 4s, \cdots, N-2s$ of the sequence $\{G(\omega_{n/2}^k)\}$ and the left endpoints $l_h = s, 3s, 5s, \cdots, N-s$ of the sequence $\{H(\omega_{n/2}^k)\}$;
3.  When merging two segments, enumerate $k = 0, 1, 2, \cdots, s-1$; at this point $G(\omega_{n/2}^k)$ is stored at array index $l_g + k$, and $H(\omega_{n/2}^k)$ is stored at array index $l_h + k$;
4.  Use the butterfly operation to compute $f(\omega_n^k)$ and $f(\omega_n^{k+n/2})$, then overwrite them directly in place.

## Inverse fast Fourier transform

The inverse Fourier transform can be expressed in terms of the Fourier transform. There are two ways to understand this.

### Linear algebra point of view

The role of the IDFT (inverse Fourier transform) is to convert the point-value form of the target polynomial into its coefficient form. The DFT itself is a linear transformation; it can be understood as treating the target polynomial as a vector and left-multiplying it by a matrix to obtain the transformed vector, which simulates substituting the complex roots of unity into the polynomial:

$$
\begin{bmatrix}y_0 \\ y_1 \\ y_2 \\ y_3 \\ \vdots \\ y_{n-1} \end{bmatrix}
=
\begin{bmatrix}1 & 1 & 1 & 1 & \cdots & 1 \\
1 & \omega_n^1 & \omega_n^2 & \omega_n^3 & \cdots & \omega_n^{n-1} \\
1 & \omega_n^2 & \omega_n^4 & \omega_n^6 & \cdots & \omega_n^{2(n-1)} \\
1 & \omega_n^3 & \omega_n^6 & \omega_n^9 & \cdots & \omega_n^{3(n-1)} \\
\vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\
1 & \omega_n^{n-1} & \omega_n^{2(n-1)} & \omega_n^{3(n-1)} & \cdots & \omega_n^{(n-1)^2} \end{bmatrix}
\begin{bmatrix} a_0 \\ a_1 \\ a_2 \\ a_3 \\ \vdots \\ a_{n-1} \end{bmatrix}
$$

Now we already have the result on the far left, and the $x$ values in the middle also correspond one-to-one to the point-value representation of the target polynomial, so by basic knowledge of matrices we only need to left-multiply both sides of the equation by the inverse of the big matrix in the middle.

Since the elements of this matrix are very special, its inverse also has a special property: just **take the reciprocal** of every element and then **divide by the length of the transform $n$**, and we get its inverse matrix.

Note: the length of the Fourier transform is not the length of the polynomial; the length of the transform must be greater than the length of the product polynomial. The polynomials to be multiplied are not long enough, so they need to be padded with $0$ in the high-degree terms.

To make the computed result the reciprocal of the original, by Euler's formula we get

$$
\frac{1}{\omega_k}=\omega_k^{-1}=\mathrm{e}^{-\frac{2\pi \mathrm{i}}{k}}=\cos\left(\frac{2\pi}{k}\right)+\mathrm{i} \sin\left(-\frac{2\pi}{k}\right)
$$

Therefore we can try taking the root of unity $\omega_k$ to be $\mathrm{e}^{-\frac{2\pi \mathrm{i}}{k}}$; then our computed result becomes the reciprocal of the original, and the only extra operation afterwards is to **divide by its length $n$**, while the rest of the procedure is exactly the same as the DFT. We can define one function with an additional parameter $1$ or $-1$ that is multiplied onto $\pi$. Passing $1$ gives the DFT, passing $-1$ gives the IDFT.

### Periodicity of the complex roots of unity

The relationship between the IDFT and the DFT can also be understood using the periodicity of the complex roots of unity.

Consider the original polynomial $f(x)=a_0+a_1x+a_2x^2+\cdots+a_{n-1}x^{n-1}=\sum_{i=0}^{n-1}a_ix^i$. The IDFT restores your point-value representation to the coefficient representation.

Consider a **constructive method**. We know $y_i=f\left( \omega_n^i \right),i\in\{0,1,\cdots,n-1\}$ and want $\{a_0,a_1,\cdots,a_{n-1}\}$. Construct the polynomial

$$
A(x)=\sum_{i=0}^{n-1}y_ix^i
$$

which amounts to treating $\{y_0,y_1,y_2,\cdots,y_{n-1}\}$ as the coefficient representation of the polynomial $A$.

Now we have two ways of deriving, which correspond to two implementation methods.

#### Method one

Let $b_i=\omega_n^{-i}$; then the point-value representation of the polynomial $A$ at $x=b_0,b_1,\cdots,b_{n-1}$ is $\left\{ A(b_0),A(b_1),\cdots,A(b_{n-1}) \right\}$.

Transforming the defining expression of $A(x)$, we can express $A(b_k)$ as

$$
\begin{aligned}
A(b_k)&=\sum_{i=0}^{n-1}f(\omega_n^i)\omega_n^{-ik}=\sum_{i=0}^{n-1}\omega_n^{-ik}\sum_{j=0}^{n-1}a_j(\omega_n^i)^{j}\\
&=\sum_{i=0}^{n-1}\sum_{j=0}^{n-1}a_j\omega_n^{i(j-k)}=\sum_{j=0}^{n-1}a_j\sum_{i=0}^{n-1}\left(\omega_n^{j-k}\right)^i\\
\end{aligned}
$$

Write $S\left(\omega_n^a\right)=\sum_{i=0}^{n-1}\left(\omega_n^a\right)^i$.

When $a=0 \pmod{n}$, $S\left(\omega_n^a\right)=n$.

When $a\neq 0 \pmod{n}$, we subtract with a shift

$$
\begin{aligned}
S\left(\omega_n^a\right)&=\sum_{i=0}^{n-1}\left(\omega_n^a\right)^i\\
\omega_n^a S\left(\omega_n^a\right)&=\sum_{i=1}^{n}\left(\omega_n^a\right)^i\\
S\left(\omega_n^a\right)&=\frac{\left(\omega_n^a\right)^n-\left(\omega_n^a\right)^0}{\omega_n^a-1}=0\\
\end{aligned}
$$

That is to say

$$
S\left(\omega_n^a\right)=
\begin{cases}
n,&a=0\\
0,&a\neq 0
\end{cases}
$$

Substituting back into the original expression

$$
A(b_k)=\sum_{j=0}^{n-1}a_jS\left(\omega_n^{j-k}\right)=a_k\cdot n
$$

That is to say, given the points $b_i=\omega_n^{-i}$, the point-value representation of $A$ is

$$
\begin{aligned}
&\left\{ (b_0,A(b_0)),(b_1,A(b_1)),\cdots,(b_{n-1},A(b_{n-1})) \right\}\\
=&\left\{ (b_0,a_0\cdot n),(b_1,a_1\cdot n),\cdots,(b_{n-1},a_{n-1}\cdot n) \right\}
\end{aligned}
$$

In summary, we take the root of unity to be its reciprocal, run an FFT on $\{y_0,y_1,y_2,\cdots,y_{n-1}\}$, and then divide by $n$ to obtain the coefficient representation of $f(x)$.

#### Method two

We substitute $\omega_n^i$ directly into $A(x)$.

The derivation is much the same as in method one; in the end we get $A(\omega_n^k) = \sum_{j=0}^{n-1}a_jS\left(\omega_n^{j+k}\right)$.

$S\left(\omega_n^{j+k}\right) = n$ holds if and only if $j+k=0 \pmod{n}$, otherwise it is $0$. Hence $A(\omega_n^k) = a_{n-k}\cdot n$.

This means that if we apply the DFT to $\{y_0,y_1,y_2,\cdots,y_{n-1}\}$, divide by $n$, and then reverse the last $n - 1$ elements, we can likewise restore the coefficient representation of $f(x)$.

### Implementation

So our FFT function can combine the DFT and the IDFT in one. The implementation is as follows:

???+ note "Non-recursive FFT (corresponding to method one)"
    ```cpp
    /*
     * Perform the FFT
     * len must be of the form 2^k
     * on == 1 means DFT, on == -1 means IDFT
     */
    void fft(Complex y[], int len, int on) {
      // bit-reversal permutation
      change(y, len);
      // Simulate the merging process: at first merge from length one to length two, and keep merging up to length len.
      for (int h = 2; h <= len; h <<= 1) {
        // wn: the step between the current complex roots of unity: w^1_h
        Complex wn(cos(2 * PI / h), sin(on * 2 * PI / h));
        // merge, len / h times in total.
        for (int j = 0; j < len; j += h) {
          // Compute the current complex root of unity; at first it is 1 = w^0_n, then it increases with step wn: w^1_n
          // ...
          Complex w(1, 0);
          for (int k = j; k < j + h / 2; k++) {
            // the left part and the right part are the solutions of the subproblems
            Complex u = y[k];
            Complex t = w * y[k + h / 2];
            // this adds up the results of the two divide-and-conquer parts
            y[k] = u + t;
            y[k + h / 2] = u - t;
            // the ω in the second half of a "step" is always the negative of the one in the "first half"
            // a point on the "red circle" "comes back" after a full turn, and after half a turn it becomes exactly the negative
            // the square of the negative of a number equals the square of the number itself
            w = w * wn;
          }
        }
      }
      // If it is the IDFT, every element of the inverse matrix is not just the reciprocal of the original element, it also has to be divided by the length len.
      if (on == -1) {
        for (int i = 0; i < len; i++) {
          y[i].x /= len;
          y[i].y /= len;
        }
      }
    }
    ```

???+ note "Non-recursive FFT (corresponding to method two)"
    ```cpp
    /*
     * Perform the FFT
     * len must be of the form 2^k
     * on == 1 means DFT, on == -1 means IDFT
     */
    void fft(Complex y[], int len, int on) {
      change(y, len);
      for (int h = 2; h <= len; h <<= 1) {             // simulate the merging process
        Complex wn(cos(2 * PI / h), sin(2 * PI / h));  // compute the current complex root of unity
        for (int j = 0; j < len; j += h) {
          Complex w(1, 0);  // compute the current complex root of unity
          for (int k = j; k < j + h / 2; k++) {
            Complex u = y[k];
            Complex t = w * y[k + h / 2];
            y[k] = u + t;  // this adds up the results of the two divide-and-conquer parts
            y[k + h / 2] = u - t;
            // the ω in the second half of a "step" is always the negative of the one in the "first half"
            // a point on the "red circle" "comes back" after a full turn, and after half a turn it becomes exactly the negative
            // the square of the negative of a number equals the square of the number itself
            w = w * wn;
          }
        }
      }
      if (on == -1) {
        reverse(y + 1, y + len);
        for (int i = 0; i < len; i++) {
          y[i].x /= len;
          y[i].y /= len;
        }
      }
    }
    ```

??? note "FFT template ([HDU 1402 - A * B Problem Plus](http://acm.hdu.edu.cn/showproblem.php?pid=1402))"
    ```cpp
    --8<-- "docs/math/code/poly/fft/fft_3.cpp"
    ```

## References

1.  [桃酱的算法笔记 (Taojiang's algorithm notes)](https://zhuanlan.zhihu.com/p/41867199).
