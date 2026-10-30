---
title: Fast number-theoretic transform
---

## Introduction

The **number-theoretic transform** (NTT) is an implementation of the discrete Fourier transform (DFT) on a number-theoretic basis; the **fast number-theoretic transform** (FNTT) is an implementation of the [fast Fourier transform](./fft.md) (FFT) on a number-theoretic basis.

The **number-theoretic transform** is a fast algorithm for computing convolutions. The most commonly used algorithms include the fast Fourier transform mentioned earlier. However, the fast Fourier transform has some implementation drawbacks: for example, the data vector has to be multiplied by a matrix with complex coefficients, and the real and imaginary parts of each complex coefficient are values of sine and cosine functions, so most of the coefficients are floating-point numbers. In other words, complex and floating-point arithmetic is required, which makes the amount of computation larger, and the error produced by floating-point arithmetic is larger as well.

The NTT handles polynomial multiplication with a modulus; it can be said to be somewhat restricted by the modulus, and the numbers are also larger. Currently the most common modulus is 998244353.

## Prerequisites

Learning the number-theoretic transform requires the following prerequisites: the discrete Fourier transform, generated subgroups, [primitive roots](../number-theory/primitive-root.md), and the discrete logarithm. This knowledge can be learned on the corresponding pages and is not repeated here.

## Definition

### Number-theoretic transform

In mathematics, the NTT is the discrete Fourier transform (DFT) over an arbitrary [ring](../algebra/basic.md#环). In the case of a finite field it is usually called the number-theoretic transform (NTT).

The **number-theoretic transform** (NTT) is obtained by carrying the discrete Fourier transform over to $F={\mathbb {Z}/p}$, the integers modulo a prime $p$. This is a **finite field**, and as long as $n$ divides $p-1$, a primitive $n$-th root of unity exists, so we have $p=\xi n+1$ for a positive integer $ξ$. Concretely, for a prime $p=qn+1, (n=2^m)$, the primitive root $g$ satisfies $g^{qn} \equiv 1 \pmod p$; if we regard $g_n=g^q\pmod p$ as the equivalent of $\omega_n$, it satisfies similar properties, e.g. $g_n^n \equiv 1 \pmod p, g_n^{n/2} \equiv -1 \pmod p$.

Since we are dealing with a number-theoretic transform here, $N$ (to distinguish it from the $n$ in the FFT, we call the $n$ here $N$) can be larger than the $n$ in the FFT, but it suffices to regard $\frac{qN}{n}$ as the $q$ here, which avoids the size problem.

Common choices are:

$$
p = 167772161 = 5 \times 2^{25}+1, g=3
$$

$$
p = 469762049 = 7 \times 2^{26}+1, g=3
$$

$$
p = 754974721 = 3^2 \times 5 \times 2^{24}+1, g=11
$$

$$
p = 998244353 = 7 \times 17 \times 2^{23}+1, g=3
$$

$$
p = 1004535809 = 479 \times 2^{21}+1, g=3
$$

This is exactly the equivalent $\mathrm{e}^{2\pi \mathrm{i} n}$ of $g^{qn}$.

When the iteration reaches length $l$, we have $g_l = g^{\frac{p-1}{l}}$, or $\omega_n = g_l = g_N^{\frac{N}{l}} = g_N^{\frac{p-1}{l}}$.

## Fast number-theoretic transform

The **fast number-theoretic transform** (FNTT) is the fast algorithm obtained by adding a divide-and-conquer step to the number-theoretic transform (NTT).

The divide-and-conquer approach used by the fast number-theoretic transform is exactly the same as the one used by the fast Fourier transform. This means that a simple modification of the fast Fourier transform code is enough to obtain the code of the fast number-theoretic transform.

The term NTT often mentioned in algorithm competitions usually actually refers to the fast number-theoretic transform; by default, "number-theoretic transform" is taken to mean "fast number-theoretic transform".

The logic of this abbreviation is similar to that of the fast Fourier transform. In fact, the term "fast Fourier transform" (FFT) refers to the "fast discrete Fourier transform" (FDFT), but since "fast" can only apply to the discrete case, and even only to the special case where the order of the primitive root of unity is a power of $2$, and cannot apply to the continuous case, the word "discrete" is omitted, FDFT becomes FFT, i.e. FFT always refers to the special discrete case.

The number-theoretic transform, or the fast number-theoretic transform, is an operation performed modulo a number; there is no continuous case, it is always discrete, so naturally there is no need to mention the word "discrete".

In the field of algorithms, an operation without a speed-up is meaningless. The term DFT is introduced in the fast Fourier transform article because the DFT also has other concrete applications in signal processing and image processing, and at the same time the DFT is the principle behind, or the prerequisite for, the FFT.

When no confusion arises, NTT is often used to denote the FNTT. To avoid confusion in the further explanation below, the two terms NTT and FNTT are kept separate in what follows.

The concrete relationship between DFT, FFT, NTT, and FNTT is:

-   Adding a divide-and-conquer step to the DFT and the NTT gives the FFT and the FNTT. The method and principle of the divide-and-conquer step can be found in the fast Fourier transform article.

-   Replacing complex addition and complex multiplication in the DFT and the FFT by addition and multiplication modulo $p$, with the magnitudes usually restricted to the range from $0$ to $p-1$, and replacing the primitive root of unity by a primitive root of unity of the same order modulo $p$, the order being a power of $2$, gives the NTT and the FNTT.

Since the replaced operations only involve addition and multiplication, DFT, FFT, NTT, and FNTT share the same principle; all of them are carried out over a ring with addition and multiplication, without the stricter field requirement that division be defined.

In fact, as long as a primitive root exists, i.e. a generator in the sense of group theory, the NTT or FNTT for that modulus can be carried out. Considering that the moduli $1$, $2$, and $4$ are too small to be of practical significance, for an odd prime $p$ and a positive integer $\alpha$ it suffices to give a primitive root $g$ for the moduli $p^\alpha$ and $2p^\alpha$, and using the same method the NTT or FNTT can still be carried out.

## Template

??? example "[Library Checker - Convolution](https://judge.yosupo.jp/problem/convolution_mod)"
    ```cpp
    --8<-- "docs/math/code/poly/ntt/ntt_1.cpp"
    ```

## References and further reading

1.  [FWT（快速沃尔什变换）零基础详解 qaq（ACM/OI）(A detailed explanation of the FWT (fast Walsh–Hadamard transform) from scratch (ACM/OI))](https://zhuanlan.zhihu.com/p/41867199)
2.  [FFT（快速傅里叶变换）0 基础详解！附 NTT（ACM/OI）(A detailed explanation of the FFT (fast Fourier transform) from scratch, with the NTT (ACM/OI))](https://zhuanlan.zhihu.com/p/40505277)
3.  [Number-theoretic transform(NTT) - Wikipedia](https://en.wikipedia.org/wiki/Discrete_Fourier_transform_%28general%29#Number-theoretic_transform)
4.  [Tutorial on FFT/NTT—The tough made simple. (Part 1)](https://codeforces.com/blog/entry/43499)
5.  [NTT 模板 - BlackJack\_ CSDN 博客 (NTT template – BlackJack\_'s CSDN blog)](https://blog.csdn.net/blackjack_/article/details/79346433)
