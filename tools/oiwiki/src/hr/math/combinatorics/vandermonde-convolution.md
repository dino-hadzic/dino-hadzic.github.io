---
title: Vandermondeova konvolucija
---

## Uvod

Vandermondeova konvolucija identitet je kojim se spajaju binomni koeficijenti, a uglavnom se primjenjuje pri izvođenju formula u kombinatorici.

## Formula Vandermondeove konvolucije

$$
\sum_{i=0}^k\binom{n}{i}\binom{m}{k-i}=\binom{n+m}{k}
$$

### Dokaz

Dokažimo je pomoću binomnog teorema:

$$
\begin{aligned}
\sum_{k=0}^{n+m}\binom{n+m}{k}x^k&=(x+1)^{n+m}\\
&=(x+1)^n(x+1)^m\\
&=\sum_{r=0}^n\binom{n}{r}x^r\sum_{s=0}^m\binom{m}{s}x^s\\
&=\sum_{k=0}^{n+m}\sum_{r=0}^k\binom{n}{r}\binom{m}{k-r}x^k\\
\end{aligned}
$$

Dakle vrijedi:

$$
\binom{n+m}{k}=\sum_{r=0}^k\binom{n}{r}\binom{m}{k-r}
$$

Razmotrimo i dokaz preko kombinatornog značenja:

Izbor $k$ brojeva iz skupa veličine $n+m$ može se shvatiti tako da skup veličine $n+m$ rastavimo na dva skupa, veličina $n$ i $m$, pa izbrojimo načine da iz skupa veličine $n$ uzmemo $i$ brojeva, a iz skupa veličine $m$ uzmemo $k-i$ brojeva. Budući da prolazimo po svim vrijednostima $i$, dovoljno je razmotriti samo jedan rastav, jer su različiti rastavi međusobno ekvivalentni.

## Posljedice

### Posljedica 1 i dokaz

$$
\sum_{i=-r}^{s}\binom{n}{r+i}\binom{m}{s-i}=\binom{n+m}{r+s}
$$

Dokaz je sličan dokazu izvorne formule.

### Posljedica 2 i dokaz

$$
\sum_{i=1}^n\binom{n}{i}\binom{n}{i-1}=\binom{2n}{n-1}
$$

Izvođenjem iz osnovnih znanja kombinatorike dobivamo:

$$
\sum_{i=1}^n\binom{n}{i}\binom{n}{i-1}=\sum_{i=0}^{n-1}\binom{n}{i+1}\binom{n}{i}=\sum_{i=0}^{n-1}\binom{n}{n-1-i}\binom{n}{i}=\binom{2n}{n-1}
$$

### Posljedica 3 i dokaz

$$
\sum_{i=0}^n\binom{n}{i}^2=\binom{2n}{n}
$$

Izvođenjem iz osnovnih znanja kombinatorike dobivamo:

$$
\sum_{i=0}^n\binom{n}{i}^2=\sum_{i=0}^n\binom{n}{i}\binom{n}{n-i}=\binom{2n}{n}
$$

### Posljedica 4 i dokaz

$$
\sum_{i=0}^m\binom{n}{i}\binom{m}{i}=\binom{n+m}{m}
$$

Izvođenjem iz osnovnih znanja kombinatorike dobivamo:

$$
\sum_{i=0}^m\binom{n}{i}\binom{m}{i}=\sum_{i=0}^m\binom{n}{i}\binom{m}{m-i}=\binom{n+m}{m}
$$

Pritom je $\binom{n+m}{m}$ dobro poznat broj načina prebrojavanja putova u mreži (rešetki). Stoga možemo razmotriti i dokaz preko kombinatornog značenja.

U mreži od $(0,0)$ do $(n,m)$ ukupno se napravi $n+m$ koraka. Dogovorimo se da je $(0,0)$ u gornjem lijevom kutu mreže; pritom se napravi $n$ koraka prema dolje i $m$ koraka udesno, pa je broj načina $\binom{n+m}{m}$.

Promijenimo kut gledanja: $n+m$ koraka rastavimo na dva dijela – prvo napravimo $n$ koraka, a zatim $m$ koraka. Ako je među prvih $n$ koraka $i$ koraka udesno, tada je među preostalih $m$ koraka $m-i$ koraka udesno, čime je tvrdnja dokazana.

## Zadaci za vježbu

-   [CF785D Anton and School - 2](https://codeforces.com/problemset/problem/785/D)

-   [Luogu P2791 幼儿园篮球题 (Zadatak o košarci u vrtiću)](https://www.luogu.com.cn/problem/P2791)

## Literatura i bilješke

1.  [Vandermonde's Convolution Formula](https://www.cut-the-knot.org/arithmetic/algebra/VandermondeConvolution.shtml)
