---
title: Fast Walsh–Hadamard transform
---

## Introduction

The Walsh transform[^note1] is a method used in spectral analysis as an alternative to the discrete Fourier transform, and it is widely applied in signal processing. The FFT works with the double type, whereas the Walsh transform decomposes a signal into square waves of different oscillation frequencies, so all coefficients are integers with the same absolute value; this avoids floating-point multiplications and speeds up the computation.

So the core idea of the FWT and the FFT should be the same: both are transforms of an array. We denote the result of applying the fast Walsh transform to an array $A$ by $FWT[A]$.

The core idea of the FWT is then:

We need a new sequence $C$ obtained from the sequences $A$ and $B$ by some computation rule, that is, $C = A \cdot B$;

we first compute the sequences $FWT[A], FWT[B]$ in the forward direction, then use $FWT[C]=FWT[A] \cdot FWT[B]$ to obtain $FWT[C]$ in $O(n)$ time, where $\cdot$ is the position-wise product of the sequences;

then we apply the inverse transform to obtain the original sequence $C$. The time complexity is $O(n \log{n})$.

In competitive programming, the FWT is a method for solving convolution problems where the indices are combined with bit operations.

Formula: $C_{i} = \sum_{i=j \oplus k}A_{j} B_{k}$

(where $\oplus$ is one of the binary bit operations)

Below we take $\cup$ (bitwise OR), $\cap$ (bitwise AND) and $\oplus$ (bitwise XOR) as examples.

## FWT operations

### OR operation

If $k=i\cup j$, then the positions where the binary digits of $i$ are $1$ and the positions where the binary digits of $j$ are $1$ are certainly a subset of the positions where the binary digits of $k$ are $1$.

Now we want to obtain $FWT[C] = FWT[A] \cdot FWT[B]$, so we have to construct the rule of this FWT.

By the definition, we can obviously construct $FWT[A]_i = A'_i = \sum_{i=i\cup j}A_{j}$, meaning that the $1$ bits of $j$ form a subset of those of $i$.

Then we have:

$$
\begin{aligned}
FWT[A]_i\cdot FWT[B]_i&=\left(\sum_{i\cup j=i} A_j\right)\left(\sum_{i\cup k=i} B_k\right) \\
&=\sum_{i\cup j=i}\sum_{i\cup k=i}A_jB_k \\
&=\sum_{i\cup(j\cup k)=i}A_jB_k \\
&= FWT[C]_i
\end{aligned}
$$

Next let us see how to compute $FWT[A]$.

First of all, we certainly cannot enumerate everything: the complexity would be $O(n^2)$. Since we cannot enumerate the whole thing, we consider divide and conquer.

We split the whole interval in two; after splitting, the indices written in binary follow a pattern.

Let $A_0$ denote the first half of $A$ and $A_1$ the second half of the interval. Then in $A_0$ the highest bit (the highest bit of the largest index of A) is $0$, so its subsets are just its own subsets (because the highest bit is $0$), while in $A_1$ the highest bit is $1$, so the subsets satisfying the condition are not only its own, but also include the subsets whose highest bit is $0$, that is,

$$
FWT[A] = merge(FWT[A_0], FWT[A_0] + FWT[A_1])
$$

where merge means concatenating the two arrays like string concatenation, and $+$ is ordinary addition, i.e. adding the corresponding entries.

In this way, through the halving, we complete the merging in $O(\log{n})$ levels, and each merge requires one pass of computation, which means we obtain $FWT[A]$ in $O(n\log{n})$ time.

Next comes the inversion, which is actually very simple: since we know that the subsets of $A_0$ are itself ($A_0 = FWT[A_0]$) and the subsets of $A_1$ give $FWT[A_0] + FWT[A_1]$, the recurrence for the inversion follows easily:

$$
UFWT[A'] = merge(UFWT[A_0'], UFWT[A_1'] - UFWT[A_0'])
$$

Below we give the implementation. It is easy to see that the forward and inverse transforms can be merged into one function: for the forward transform $\text{type}=1$, for the inverse transform $\text{type}=-1$.

???+ note "Implementation"
    ```cpp
    void Or(ll *a, ll type) {  // iterative implementation, smaller constant
      for (ll x = 2; x <= n; x <<= 1) {
        ll k = x >> 1;
        for (ll i = 0; i < n; i += x) {
          for (ll j = 0; j < k; j++) {
            (a[i + j + k] += a[i + j] * type) %= P;
          }
        }
      }
    }
    ```

### AND operation

For the AND operation, by analogy with the OR operation we get similar conclusions

$$
FWT[A] = merge(FWT[A_0] + FWT[A_1], FWT[A_1])
$$

$$
UFWT[A'] = merge(UFWT[A_0'] - UFWT[A_1'], UFWT[A_1'])
$$

Below we give the implementation. For the forward transform $\text{type}=1$, for the inverse transform $\text{type}=-1$.

???+ note "Implementation"
    ```cpp
    void And(ll *a, ll type) {
      for (ll x = 2; x <= n; x <<= 1) {
        ll k = x >> 1;
        for (ll i = 0; i < n; i += x) {
          for (ll j = 0; j < k; j++) {
            (a[i + j] += a[i + j + k] * type) %= P;
          }
        }
      }
    }
    ```

### XOR operation

The XOR convolution is based on the following principle:

If we let $x\circ y$ denote the parity of the number of $1$s in $x\cap y$, that is, $x\circ y=\text{popcnt}(x\cap y)\bmod 2$, then it is easy to see that $(x\circ y)\oplus (x\circ z)=x\circ(y\oplus z)$.

The computation of $FWT[A]$ is also easy to obtain.

Let $FWT[A]_i=\sum_{i\circ j=0}A_j-\sum_{i\circ j=1}A_j$. Let us prove the correctness of $FWT[C] = FWT[A] \cdot FWT[B]$:

$$
\begin{aligned}
FWT[A]_iFWT[B]_i&=\left(\sum_{i\circ j=0}A_j-\sum_{i\circ j=1}A_j\right)\left(\sum_{i\circ k=0}B_k-\sum_{i\circ k=1}B_k\right) \\
&=\left(\sum_{i\circ j=0}A_j\sum_{i\circ k=0}B_k+\sum_{i\circ j=1}A_j\sum_{i\circ k=1}B_k\right)-\left(\sum_{i\circ j=0}A_j\sum_{i\circ k=1}B_k+\sum_{i\circ j=1}A_j\sum_{i\circ k=0}B_k\right) \\
&=\sum_{(j\oplus k)\circ i=0}A_jB_k-\sum_{(j\oplus k)\circ i=1}A_jB_k \\
&=FWT[C]_i
\end{aligned}
$$

Let us see how to compute the values of $A,B$ quickly; again by divide and conquer:

For the subarray $FWT[A_0]$, where the current bit of $i$ is $0$, when performing the $\circ$ operation we find that the result does not change whether it is combined with $0$ or with $1$ (because $0\cap 0=0,0\cap1=0$), so in $FWT[A]=\sum_{i\circ j=0}A_j-\sum_{i\circ j=1}A_j$ we have $\sum_{i\circ j=1}A_j=0$.

For the subarray $A_1$, where the current bit of $i$ is $1$, when performing the $\circ$ operation we find that the result with $0$ is $0$ and the result with $1$ is $1$ (because $1\cap 0=0,1\cap1=1$).

In summary, we have:

$$
FWT[A]=merge((FWT[A_0]+FWT[A_1])-0, FWT[A_0]-FWT[A_1])
$$

that is:

$$
FWT[A] = merge(FWT[A_0] + FWT[A_1], FWT[A_0] - FWT[A_1])
$$

The inverse transform follows easily:

$$
UFWT[A'] = merge(\frac{UFWT[A_0'] + UFWT[A_1']}{2}, \frac{UFWT[A_0'] - UFWT[A_1']}{2})
$$

Here is the code; for the forward transform $\text{type}=1$, for the inverse transform $\text{type}=\frac{1}{2}$.

???+ note "Implementation"
    ```cpp
    void Xor(ll *a, ll type) {
      for (ll x = 2; x <= n; x <<= 1) {
        ll k = x >> 1;
        for (ll i = 0; i < n; i += x) {
          for (ll j = 0; j < k; j++) {
            (a[i + j] += a[i + j + k]) %= P;
            (a[i + j + k] = a[i + j] - a[i + j + k] * 2) %= P;
            (a[i + j] *= type) %= P;
            (a[i + j + k] *= type) %= P;
          }
        }
      }
    }
    ```

### XNOR operation

By analogy with the XOR operation we give the formulas:

$FWT[A]_{i} = \sum_{C_1}A_{j} - \sum_{C_2}A_{j}$ ($C_1$ means that $\text{popcnt}(x\cup y)\bmod 2$ is $0$, and $C_2$ means that $\text{popcnt}(x\cup y)\bmod 2$ is $1$)

$$
FWT[A] = merge(FWT[A_1] - FWT[A_0], FWT[A_1] + FWT[A_0])
$$

$$
UFWT[A'] = merge(\frac{UFWT[A_1'] - UFWT[A_0']}{2}, \frac{UFWT[A_1'] + UFWT[A_0']}{2})
$$

## FWT from another perspective

Let $c(i,j)$ be the contribution coefficient of $A_j$ to $FWT[A]_i$. We can re-describe the process of the FWT:

$$
FWT[A]_i = \sum_{j=0}^{n-1} c(i,j) A_j
$$

Because we have:

$$
FWT[A]_i\cdot FWT[B]_i=FWT[C]_i
$$

a simple proof gives: $c(i,j)c(i,k)=c(i,j\odot k)$, where $\odot$ is any bit operation.

At the same time, the function $c$ has another important property: it can be processed bit by bit.

For example, when we transform:

$$
FWT[A]_i = \sum_{j=0}^{n-1} c(i,j) A_j
$$

doing it this way is rather poor, so we split it:

$$
FWT[A]_i = \sum_{j=0}^{n/2-1} c(i,j) A_j+\sum_{j=n/2}^{n-1} c(i,j) A_j
$$

Considering the difference between $i,j$ in the first and the second expression, we find that only the highest bit differs.

So we denote the values of $i,j$ with the highest bit removed by $i',j'$, and let $i_0$ be the highest bit of $i$. We have:

$$
FWT[A]_i = c(i_0,0)\sum_{j=0}^{n/2-1} c(i',j') A_j+c(i_0,1)\sum_{j=n/2}^{n-1} c(i',j') A_j
$$

If $i_0=0$, then:

$$
FWT[A]_i = c(0,0)\sum_{j=0}^{n/2-1} c(i',j') A_j+c(0,1)\sum_{j=n/2}^{n-1} c(i',j') A_j
$$

For $i_0=1$:

$$
FWT[A]_i = c(1,0)\sum_{j=0}^{n/2-1} c(i',j') A_j+c(1,1)\sum_{j=n/2}^{n-1} c(i',j') A_j
$$

In other words, we only need:

$$
\begin{bmatrix}
c(0,0) & c(0,1) \\
c(1,0) & c(1,1)
\end{bmatrix}
$$

four numbers to complete the transform. We call this matrix the bit matrix.

If we want to perform the inverse transform, we need the inverse of the bit matrix above.

If the inverse matrix is $c^{-1}$, the original values can be obtained by a similar operation:

$$
A_i = \sum_{j=0}^n c^{-1}(i,j) FWT[A]_j
$$

The inverse matrix does not necessarily exist; for example, if there is a row of $0$s or a column of $0$s, the matrix has no inverse, so we must be especially careful when constructing it.

### Bitwise OR

We can construct:

$$
\begin{bmatrix}
1 & 0 \\
1 & 1
\end{bmatrix}
$$

This satisfies $c(i,j)c(i,k)=c(i,j\cup k)$. We find that this is exactly the same as the $FWT[A]=\text{merge}(FWT[A_0], FWT[A_0]+FWT[A_1])$ we derived earlier! Similarly, the following is also a matrix satisfying this condition, but we usually use the one above:

$$
\begin{bmatrix}
1 & 1 \\
1 & 0
\end{bmatrix}
$$

Although the following matrix also satisfies $c(i,j)c(i,k)=c(i,j\cup k)$, it has a row of $0$s and thus no inverse, so it is not valid:

$$
\begin{bmatrix}
0 & 0 \\
1 & 1
\end{bmatrix}
$$

If we want to perform the inverse transform, we need to invert the matrix; taking the **topmost** matrix as an example, we get:

$$
\begin{bmatrix}
1 & 0 \\
-1 & 1
\end{bmatrix}
$$

Then, following the method of the forward transform, just substitute the inverse transform matrix.

### Bitwise AND

We can construct:

$$
\begin{bmatrix}
1 & 1 \\
0 & 1
\end{bmatrix}
$$

This satisfies $c(i,j)c(i,k)=c(i,j\cap k)$.

Inverse matrix:

$$
\begin{bmatrix}
1 & -1 \\
0 & 1
\end{bmatrix}
$$

### Bitwise XOR

We can construct:

$$
\begin{bmatrix}
1 & 1 \\
1 & -1
\end{bmatrix}
$$

This satisfies $c(i,j)c(i,k)=c(i,j\oplus k)$.

Inverse matrix:

$$
\begin{bmatrix}
0.5 & 0.5 \\
0.5 & -0.5
\end{bmatrix}
$$

## FWT is a linear transformation

The FWT is a linear transformation. That is, it satisfies:

$$
FWT[A+B]=FWT[A]+FWT[B]
$$

and:

$$
FWT[c\cdot A]=c\cdot FWT[A]
$$

## K-dimensional FWT

In essence, bit operations are operations on an $n$-dimensional $\{0,1\}$ vector. The OR operation takes $\max$ in each dimension. The AND operation takes $\min$ in each dimension. The XOR operation adds the corresponding components in each dimension and then takes $\bmod 2$.

Bit operations have one characteristic: every component of the vector is independent.

Let us extend $\{0,1\}$ to $[0,K)\cap \mathbf{Z}$, that is, to base $K$, and see what we get.

### max operation

We extend the $\cup$ operation to base $K$, defining $i\cup j$ as the digit-wise $\max$; we have:

$$
c(i,j)c(i,k)=c(i,j\cup k)
$$

If $j=k$, the above becomes:

$$
c(i,j)c(i,j)=c(i,j)
$$

In other words, in every row the $1$s must come before the $0$s; if they come after, it is invalid. Playing around a bit, we find a valid construction:

$$
\begin{bmatrix}
1 & 0 & 0 & 0 \\
1 & 1 & 0 & 0 \\
1 & 1 & 1 & 0 \\
1 & 1 & 1 & 1
\end{bmatrix}
$$

Inverting gives:

$$
\begin{bmatrix}
1 & 0 & 0 & 0 \\
-1 & 1 & 0 & 0 \\
0 & -1 & 1 & 0 \\
0 & 0 & -1 & 1
\end{bmatrix}
$$

### min operation

We extend the $\cap$ operation to base $K$, defining $i\cap j$ as the digit-wise $\min$; we have:

$$
c(i,j)c(i,k)=c(i,j\cap k)
$$

If $j=k$, the above becomes:

$$
c(i,j)c(i,j)=c(i,j)
$$

In other words, in every row the $1$s must come after the $0$s; if they come before, it is invalid. Playing around a bit, we find a valid construction:

$$
\begin{bmatrix}
1 & 1 & 1 & 1 \\
0 & 1 & 1 & 1 \\
0 & 0 & 1 & 1 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

Inverting gives:

$$
\begin{bmatrix}
1 & -1 & 0 & 0 \\
0 & 1 & -1 & 0 \\
0 & 0 & 1 & -1 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

The first two are rarely used; the one used much more often is:

### Carryless addition

We extend the $\oplus$ operation to base $K$, defining $i\oplus j$ as digit-wise addition followed by $\bmod K$; we have:

$$
c(i,j)c(i,k)=c(i,j\oplus k)
$$

If we construct $c(i,j)=\omega_{K}^j$, the requirement is satisfied:

$$
\omega_{K}^j\omega_{K}^k=\omega_{K}^{j\oplus k}
$$

But a matrix in which every row is the same has no inverse either, so we can construct $c(i,j)=\omega_{K}^{(i-1)j}$ instead.

We get the following matrix:

$$
\begin{bmatrix}
1 & 1 & 1 & \cdots & 1 \\
1 & \omega_{K}^1 & \omega_{K}^2 & \cdots & \omega_{K}^{k-1} \\
1 & \omega_{K}^2 & \omega_{K}^4 & \cdots & \omega_{K}^{2(k-1)} \\
1 & \omega_{K}^3 & \omega_{K}^6 & \cdots & \omega_{K}^{3(k-1)} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & \omega_{K}^{k-1} & \omega_{K}^{2(k-1)} & \cdots & \omega_{K}^{(k-1)(k-1)}
\end{bmatrix}
$$

This is exactly the [Vandermonde matrix](https://en.wikipedia.org/wiki/Vandermonde_matrix); inverting gives:

$$
\frac{1}{K}\begin{bmatrix}
1 & 1 & 1 & \cdots & 1 \\
1 & \omega_{K}^{-1} & \omega_{K}^{-2} & \cdots & \omega_{K}^{-(k-1)} \\
1 & \omega_{K}^{-2} & \omega_{K}^{-4} & \cdots & \omega_{K}^{-2(k-1)} \\
1 & \omega_{K}^{-3} & \omega_{K}^{-6} & \cdots & \omega_{K}^{-3(k-1)} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & \omega_{K}^{-(k-1)} & \omega_{K}^{-2(k-1)} & \cdots & \omega_{K}^{-(k-1)(k-1)}
\end{bmatrix}
$$

If a root of unity exists for the modulus given in the problem, the implementation is simple.

However, **a root of unity may not exist in modular arithmetic**, so we consider a field extension: we artificially define an $x$ satisfying $x^K=1$ and then directly substitute $x$ into the computation, so that every number is a polynomial of degree $k-1$ in $x$. We only need to compute $\bmod {x^K-1}$. The matrix can then be written as:

$$
\begin{bmatrix}
1 & 1 & 1 & \cdots & 1 \\
1 & x^1 & x^2 & \cdots & x^{k-1} \\
1 & x^2 & x^4 & \cdots & x^{2(k-1)} \\
1 & x^3 & x^6 & \cdots & x^{3(k-1)} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & x^{k-1} & x^{2(k-1)} & \cdots & x^{(k-1)(k-1)}
\end{bmatrix}
$$

But doing so may introduce zero divisors, that is, **a number may have several representations**, and we cannot determine the true value of a number.

Instead of taking $\bmod {x^K-1}$, we take $\bmod$ the cyclotomic polynomial $\Phi_{K}(x)$, in which $x$ has order $k$ and which is irreducible over $\mathbb{Q}$. So we define the computation above to be carried out $\bmod {\Phi_{K}(x)}$.

One more problem is that $\bmod \Phi_{K}(x)$ has a large constant (because $\Phi$ is itself a polynomial). But since $\Phi_{K}(x)\mid x^k-1$, we only need to take $\bmod x^k -1$ during the computation and $\bmod \Phi_{K}(x)$ at the very end.

## Examples

???+ note "[CF 1103E Radix sum](https://www.luogu.com.cn/problem/CF1103E)"
    Given a sequence $a_1,a_2,...,a_n$ of length $n$, for every $p \in [0,n-1]$ find the number of integer sequences $i_1,i_2,...,i_n$ satisfying the following conditions, modulo $2^{58}$:
    
    -   $\forall j \in [1,n] , i_j \in [1,n]$;
    -   $\sum\limits_{j=1}^n a_{i_j} = p$, where addition is defined as decimal carryless addition.
    
    $n\le10^5,a_i\le10^5$
    
    ??? note "Solution"
        We can think of DP: define the state $f_{i,s}$ meaning that the first $i$ numbers have been considered and the current sum state is $s$. Since the FWT is linear, we can first transform into the FWT point-value representation, then raise it to its $n$-th power, and finally transform back.
        
        The above is trivial, but the problem gives the modulus $2^{58}$. We find that there is no root of unity, so we consider a field extension.
        
        The cyclotomic polynomial here is $\Phi_{10}(x)=x^4-x^3+x^2-x+1$.
        
        However, we find that in the UFWT we need to divide by the base $10$, and $10$ has no inverse modulo $2^{58}$. In fact, $5$ does have an inverse modulo $2^{58}$: $57646075230342349$, so we only need to divide by another $2$. Let the answer after dividing by $5$ be $x$ and the true answer be $y$, that is, $2^5y\equiv x\pmod{2^{64}}$; obviously we have $y\equiv \frac{x}{2^5}\pmod{2^{64-5}}$, that is, $y\equiv \frac{x}{2^5}\pmod{2^{59}}$, so it suffices to divide the final answer by $2^5$. Although it is unclear why the problem setter wanted the modulus $2^{58}$, we just take the remainder once more.

???+ note "[CF103329F (XXII Opencup, Grand Prix of XiAn) The Struggle](https://codeforces.com/gym/103329/problem/F)"
    Given an ellipse $E$ in which the coordinates of all integer points lie in $[1,4 \cdot 10^6]$, find the value of $\sum_{(x,y) \in E} (x \oplus y)^{33}x^{-2}y^{-1} \mod 10^9+7$.
    
    ??? note "Solution"
        This is a problem where the technique is not immediately apparent; the problem setter provided a detailed editorial in English, see [this link](https://codeforces.com/blog/entry/96518).

## References

-   [桃酱的算法笔记 (Taojiang's algorithm notes)](https://zhuanlan.zhihu.com/p/41867199)
-   [ZnPdCo's blog](https://znpdco.github.io/%E7%AE%97%E6%B3%95/2024/05/07/FWT.html)

[^note1]: [Wikipedia](https://en.wikipedia.org/wiki/Hadamard_transform)
