---
title: Eulerovi brojevi (Eulerian numbers)
---

???+ warning "Napomena"
    Eulerovi brojevi u nastavku odnose se isključivo na Eulerian numbers. Ne treba ih miješati s Eulerovim brojevima (Euler numbers) ni s Eulerovim brojem (Euler's number, matematička konstanta povezana s Eulerom, npr. $\gamma$ ili $\mathrm{e}$).

U enumerativnoj kombinatorici **Eulerov broj** (Eulerian number) jest **broj** permutacija brojeva od $1$ do $n$ u kojima je točno $m$ elemenata veće od svog prethodnika (permutacija s $m$ „uspona”). Definira se kao

$$
A(n, m) = 
\left\langle 
\begin{matrix}
  n\\
  m - 1
\end{matrix}
\right\rangle
$$

Na primjer, od brojeva od $1$ do $3$ postoje ukupno $4$ permutacije u kojima je točno jedan element veći od svog prethodnika:

| Permutacija | Susjedni elementi koji zadovoljavaju uvjet | Broj |
| ----- | ----------- | -- |
| 1 2 3 | 1, 2 & 2, 3 | 2  |
| 1 3 2 | 1, 3        | 1  |
| 2 1 3 | 1, 3        | 1  |
| 2 3 1 | 2, 3        | 1  |
| 3 1 2 | 1, 2        | 1  |
| 3 2 1 |             | 0  |

Dakle, prema definiciji $A(n, m)$: ako je $n$ jednako $3$, a $m$ jednako $1$, Eulerov broj iznosi $4$, što znači da postoje ukupno $4$ permutacije u kojima je $1$ element veći od svog prethodnika.

Za male vrijednosti $n$ i $m$ Eulerove brojeve možemo odrediti izravno:

| $A(n, m)$ | Permutacije koje zadovoljavaju uvjet | Broj |
| --------- | -------------------------------------------- | -- |
| $A(1, 0)$ | $(1)$                                        | 1  |
| $A(2, 0)$ | $(2, 1)$                                     | 1  |
| $A(2, 1)$ | $(1, 2)$                                     | 1  |
| $A(3, 0)$ | $(3, 2, 1)$                                  | 1  |
| $A(3, 1)$ | $(1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2)$ | 4  |
| $A(3, 2)$ | $(1, 2, 3)$                                  | 1  |

## Formula

Eulerove brojeve možemo računati rekurzivnom relacijom ili rekurzijom.

Prvo, kada je $m \ge n$ ili $n = 0$, nema permutacija koje zadovoljavaju uvjet, pa je Eulerov broj tada $0$.

Drugo, kada je $m = 0$, uvjet zadovoljava samo silazna permutacija, pa je Eulerov broj tada $1$.

Naposljetku, promotrimo umetanje broja $n$ u permutaciju duljine $n-1$ čime dobivamo permutaciju duljine $n$; budući da umetanje $n$ povećava Eulerov broj najviše za $1$, $A(n, m)$ može se dobiti prijelazom samo iz $A(n-1, m-1)$ i $A(n-1, m)$.

Promotrimo položaj na koji umećemo $n$: kada je $p_{i-1} < p_{i}$, ako $n$ umetnemo ispred $p_{i}$, tj. ako $n$ umetnemo u „uspon”, Eulerov broj permutacije se ne mijenja; također, ako $n$ umetnemo na početak permutacije, Eulerov broj permutacije se ne mijenja; inače, ako $n$ umetnemo na bilo koji drugi položaj, Eulerov broj permutacije raste za $1$.

Promotrimo prijelaz iz $A(n-1, m-1)$ u $A(n, m)$: tada Eulerov broj treba porasti za $1$, pa $n$ ne smijemo umetnuti u „uspon” ni na početak permutacije; ukupno postoji $n - (m-1) - 1 = n-m$ mogućnosti.

Promotrimo prijelaz iz $A(n-1, m)$ u $A(n, m)$: tada Eulerov broj treba ostati nepromijenjen, pa $n$ možemo umetnuti samo u „uspon” ili na početak permutacije; ukupno postoji $m+1$ mogućnosti.

Sve zajedno, vrijedi

$$
A(n, m) = \begin{cases}
    0, & m > n \text{ or } n = 0, \\
    1, & m = 0, \\
    (n-m) \cdot A(n-1, m-1) + (m+1) \cdot A(n-1, m), & \text{otherwise}.
\end{cases}
$$

## Implementacija

=== "C++"
    ```cpp
    int eulerianNumber(int n, int m) {
      if (m >= n || n == 0) return 0;
      if (m == 0) return 1;
      return (((n - m) * eulerianNumber(n - 1, m - 1)) +
              ((m + 1) * eulerianNumber(n - 1, m)));
    }
    ```

=== "Python"
    ```python
    def eulerianNumber(n, m):
        if m >= n or n == 0:
            return 0
        if m == 0:
            return 1
        return ((n - m) * eulerianNumber(n - 1, m - 1)) + (
            (m + 1) * eulerianNumber(n - 1, m)
        )
    ```

## Zadaci za vježbu

-   [CF1349F1 Slime and Sequences (Easy Version)](https://codeforces.com/problemset/problem/1349/F1)
-   [CF1349F2 Slime and Sequences (Hard Version)](https://codeforces.com/problemset/problem/1349/F2)
-   [UOJ 593. 新年的军队 (Novogodišnja vojska)](https://uoj.ac/problem/593)
-   [P7511 三到六 (Od tri do šest)](https://www.luogu.com.cn/problem/P7511)
