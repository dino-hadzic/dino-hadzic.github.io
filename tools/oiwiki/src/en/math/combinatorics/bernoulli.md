---
title: Bernoulli numbers
---

The Bernoulli numbers $B_n$ are a sequence of rational numbers closely related to number theory. The first few Bernoulli numbers discovered are:

$B_0=1,B_1=-\frac{1}{2},B_2=\frac{1}{6},B_3=0,B_4=-\frac{1}{30},\dots$

## Sums of equal powers

The Bernoulli numbers are named after Jacob Bernoulli, who discovered a remarkable relation while studying formulas for sums of $m$-th powers. Let us write

$$
S_{m}(n)=\sum_{k=0}^{n-1}k^m=0^m+1^m+\dots+(n-1)^m
$$

Bernoulli looked at the following list of formulas and sketched out a pattern:

$$
\begin{aligned}
S_0(n)&=n\\
S_1(n)&=\frac{1}{2}n^2-\frac{1}{2}n\\
S_2(n)&=\frac{1}{3}n^3-\frac{1}{2}n^2+\frac{1}{6}n\\
S_3(n)&=\frac{1}{4}n^4-\frac{1}{2}n^3+\frac{1}{4}n^2\\
S_4(n)&=\frac{1}{5}n^5-\frac{1}{2}n^4+\frac{1}{3}n^3-\frac{1}{30}n
\end{aligned}
$$

One can observe that in $S_m(n)$ the coefficient of $n^{m+1}$ is always $\frac{1}{m+1}$, the coefficient of $n^m$ is always $-\frac{1}{2}$, the coefficient of $n^{m-1}$ is always $\frac{m}{12}$, the coefficient of $n^{m-3}$ is $-\frac{m(m-1)(m-2)}{720}$, the coefficient of $n^{m-4}$ is always zero, and so on.

The coefficient of $n^{m-k}$ is always some constant multiplied by $m^{\underline{k}}$, where $m^{\underline{k}}$ denotes the falling factorial power, i.e. $\frac{m!}{(m-k)!}$.

## Recurrence formula

$$
\begin{aligned}
S_m{(n)}&=\frac{1}{m+1}(B_0n^{m+1}+\binom{m+1}{1}B_1 n^m+\dots+\binom{m+1}{m}B_m n) \\
&=\frac{1}{m+1}\sum_{k=0}^{m}\binom{m+1}{k}B_kn^{m+1-k}
\end{aligned}
$$

The Bernoulli numbers are defined by the implicit recurrence relation:

$$
\begin{aligned}
\sum_{j=0}^{m}\binom{m+1}{j}B_j&=0,(m>0)\\
B_0&=1
\end{aligned}
$$

For example, $\binom{2}{0}B_0+\binom{2}{1}B_1=0$; the first few values are clearly

|  $n$  | $0$ |       $1$      |      $2$      | $3$ |       $4$       | $5$ |       $6$      | $7$ |       $8$       | $\dots$ |
| :---: | :-: | :------------: | :-----------: | :-: | :-------------: | :-: | :------------: | :-: | :-------------: | :-----: |
| $B_n$ | $1$ | $-\frac{1}{2}$ | $\frac{1}{6}$ | $0$ | $-\frac{1}{30}$ | $0$ | $\frac{1}{42}$ | $0$ | $-\frac{1}{30}$ | $\dots$ |

### Proof

#### Proof by induction

This proof comes from Concrete Mathematics, section 6.5 BERNOULLI NUMBER.

We prove it using identities for binomial coefficients and induction:

$$
\begin{aligned}
S_{m+1}(n)+n^{m+1}&= \sum_{k=0}^{n-1}(k+1)^{m+1}\\
&=\sum_{k=0}^{n-1}\sum_{j=0}^{m+1}\binom{m+1}{j}k^j\\
&=\sum_{j=0}^{m+1}\binom{m+1}{j}S_j(n)
\end{aligned}
$$

Let $\hat{S}_{m}(n)=\frac{1}{m+1} \sum_{k=0}^{m} \binom{m+1}{k}B_kn^{m+1-k}$. We want to prove that $S_m(n)=\hat{S}_m(n)$; assume that for $j\in[0,m)$ we have $S_j(n)=\hat{S}_j(n)$.

Subtracting $S_{m+1}(n)$ from both sides of the original equation, we get:

$$
\begin{aligned}
S_{m+1}(n)+n^{m+1}&=\sum_{j=0}^{m+1}\binom{m+1}{j}S_j(n)\\
n^{m+1}&=\sum_{j=0}^{m}\binom{m+1}{j}S_j(n)\\
&=\sum_{j=0}^{m-1}\binom{m+1}{j}\hat{S}_j(n)+\binom{m+1}{m}S_m(n)
\end{aligned}
$$

Let us try adding $\binom{m+1}{m}\hat{S}_m(n)-\binom{m+1}{m}\hat{S}_m(n)$ to the right-hand side and then simplifying; we get:

$$
n^{m+1}=\sum_{j=0}^{m}\binom{m+1}{j}\hat{S}_j(n)+(m+1)(S_m(n)-\hat{S}_m(n))
$$

Let $\Delta = S_m(n)-\hat{S}_m(n)$, and expand $\hat{S}_j(n)$; then we have

$$
\begin{aligned}
n^{m+1}&=\sum_{j=0}^{m}\binom{m+1}{j}\hat{S}_j(n)+(m+1)\Delta\\
&=\sum_{j=0}^{m}\binom{m+1}{j}\frac{1}{j+1}\sum_{k=0}^{j}\binom{j+1}{k}B_kn^{j+1-k}+(m+1)\Delta\\
\end{aligned}
$$

Reversing the order of summation in the second $\sum$ and then rewriting the binomial coefficients with identities, we get:

$$
\begin{aligned}
n^{m+1}&=\sum_{j=0}^{m}\binom{m+1}{j}\frac{1}{j+1}\sum_{k=0}^{j}\binom{j+1}{j-k}B_{j-k}n^{k+1}+(m+1)\Delta\\
&=\sum_{j=0}^{m}\binom{m+1}{j}\frac{1}{j+1}\sum_{k=0}^{j}\binom{j+1}{k+1}B_{j-k}n^{k+1}+(m+1)\Delta\\
&=\sum_{j=0}^{m}\binom{m+1}{j}\frac{1}{j+1}\sum_{k=0}^{j}\frac{j+1}{k+1}\binom{j}{k}B_{j-k}n^{k+1}+(m+1)\Delta\\
&=\sum_{j=0}^{m}\binom{m+1}{j}\sum_{k=0}^{j}\binom{j}{k}\frac{B_{j-k}}{k+1}n^{k+1}+(m+1)\Delta
\end{aligned}
$$

Swapping the two summation signs, we get:

$$
n^{m+1}=\sum_{k=0}^{m}\frac{n^{k+1}}{k+1}\sum_{j=k}^{m}\binom{m+1}{j}\binom{j}{k}B_{j-k}+(m+1)\Delta
$$

We transform $\binom{m+1}{j}\binom{j}{k}$ with an identity:

$$
\binom{m+1}{j}\binom{j}{k}＝\binom{m+1}{k}\binom{m-k+1}{j-k}
$$

Then the expression becomes:

$$
\begin{aligned}
n^{m+1}&=\sum_{k=0}^{m}\frac{n^{k+1}}{k+1}\sum_{j=k}^{m}\binom{m+1}{k}\binom{m-k+1}{j-k}B_{j-k}+(m+1)\Delta\\
&=\sum_{k=0}^{m}\frac{n^{k+1}}{k+1}\binom{m+1}{k}\sum_{j=k}^{m}\binom{m-k+1}{j-k}B_{j-k}+(m+1)\Delta\\
\end{aligned}
$$

Replacing every $j-k$ by $j$, we get:

$$
n^{m+1}=\sum_{k=0}^{m}\frac{n^{k+1}}{k+1}\binom{m+1}{k}\sum_{j=0}^{m-k}\binom{m-k+1}{j}B_{j}+(m+1)\Delta
$$

Consider the recurrence relation we mentioned earlier

$$
\begin{aligned}
\sum_{j=0}^{m}\binom{m+1}{j}B_j&=0,(m>0)\\
B_0&=1\\
\sum_{j=0}^{m}\binom{m+1}{j}B_j&=[m = 0]
\end{aligned}
$$

Substituting it in, we get:

$$
\begin{aligned}
n^{m+1}&=\sum_{k=0}^{m}\frac{n^{k+1}}{k+1}\binom{m+1}{k}[m - k = 0]+(m+1)\Delta\\
&=\frac{n^{m+1}}{m+1}\binom{m+1}{m}+(m+1)\Delta\\
&=n^{m+1}+(m+1)\Delta
\end{aligned}
$$

Hence $\Delta=0$, and $S_m(n)=\hat{S}_m(n)$.

#### Proof using exponential generating functions

Take the recurrence $\sum_{j=0}^{m}\binom{m+1}{j}B_j=[m=0]$

and add $B_{m + 1}$ to both sides, obtaining:

$$
\begin{aligned}
\sum_{j=0}^{m+1}\binom{m+1}{j}B_j&=[m=0]+B_{m+1}\\
\sum_{j=0}^{m}\binom{m}{j}B_j&=[m=1]+B_{m}\\
\sum_{j=0}^{m}\dfrac{B_j}{j!}\cdot\dfrac{1}{(m-j)!}&=[m=1]+\dfrac{B_{m}}{m!}
\end{aligned}
$$

Let $B(z) = \sum\limits_{i\ge 0}\dfrac{B_i}{i!}z^i$. Note that the left-hand side has the form of a convolution, so:

$$
\begin{aligned}
B(z)\mathrm{e}^z &= z+B(z)\\
B(z)&=\dfrac{z}{\mathrm{e}^z - 1}
\end{aligned}
$$

Let $F_n(z) = \sum_{m\ge 0}\dfrac{S_m(n)}{m!}z^m$; then:

$$
\begin{aligned}
F_n(z) &= \sum_{m\ge 0}\dfrac{S_m(n)}{m!}z^m\\
&= \sum_{m\ge 0}\sum_{i=0}^{n-1}\dfrac{i^mz^m}{m!}\\
\end{aligned}
$$

Swap the order of summation:

$$
\begin{aligned}
F_n(z) &=\sum_{i=0}^{n-1}\sum_{m\ge 0}\dfrac{i^mz^m}{m!}\\
       &=\sum_{i=0}^{n-1}\mathrm{e}^{iz}\\
       &=\dfrac{\mathrm{e}^{nz} - 1}{\mathrm{e}^z - 1}\\
       &=\dfrac{z}{\mathrm{e}^z - 1}\cdot\dfrac{\mathrm{e}^{nz} - 1}{z}
\end{aligned}
$$

Substitute $B(z)=\dfrac{z}{\mathrm{e}^z - 1}$:

$$
\begin{aligned}
F_n(z) &= B(z)\cdot\dfrac{\mathrm{e}^{nz} - 1}{z}\\
&= \left(\sum_{i\ge 0}\dfrac{B_i}{i!} \right)\left(\sum_{i\ge 1}\dfrac{n^i z^{i - 1}}{i!}\right)\\
&= \left(\sum_{i\ge 0}\dfrac{B_i}{i!} \right)\left(\sum_{i\ge 0}\dfrac{n^{i+1} z^{i}}{(i+1)!}\right)
\end{aligned}
$$

Since $F_n(z) = \sum_{m\ge 0}\dfrac{S_m(n)}{m!}z^m$, i.e. $S_m(n)=m![z^m]F_n(z)$:

$$
\begin{aligned}
S \times m(n)&=m![z^m]F_n(z)\\
             &= m!\sum_{i=0}^{m}\dfrac{B \times i}{i!}\cdot\dfrac{n^{m-i+1}}{(m-i+1)!}\\
             &=\dfrac{1}{m+1}\sum_{i=0}^{m}\binom{m+1}{i}B_in^{m-i+1}
\end{aligned}
$$

This completes the proof.

??? note "Reference implementation"
    ```cpp
    using ll = long long;
    constexpr int MAXN = 10000;
    constexpr int mod = 1e9 + 7;
    ll B[MAXN];        // Bernoulli numbers
    ll C[MAXN][MAXN];  // binomial coefficients
    ll inv[MAXN];      // inverses (for computing the Bernoulli numbers)
    
    void init() {
      // precompute binomial coefficients
      for (int i = 0; i < MAXN; i++) {
        C[i][0] = C[i][i] = 1;
        for (int k = 1; k < i; k++) {
          C[i][k] = (C[i - 1][k] % mod + C[i - 1][k - 1] % mod) % mod;
        }
      }
      // precompute inverses
      inv[1] = 1;
      for (int i = 2; i < MAXN; i++) {
        inv[i] = (mod - mod / i) * inv[mod % i] % mod;
      }
      // precompute Bernoulli numbers
      B[0] = 1;
      for (int i = 1; i < MAXN; i++) {
        ll ans = 0;
        if (i == MAXN - 1) break;
        for (int k = 0; k < i; k++) {
          ans += C[i + 1][k] * B[k];
          ans %= mod;
        }
        ans = (ans * (-inv[i + 1]) % mod + mod) % mod;
        B[i] = ans;
      }
    }
    ```
