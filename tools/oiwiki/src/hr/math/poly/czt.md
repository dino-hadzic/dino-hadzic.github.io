---
title: Chirp Z-transformacija
---

Slično diskretnoj Fourierovoj transformaciji, Chirp Z-transformacija je algoritam koji za zadani polinom $f(x) = \sum_{i = 0}^{m - 1} f_i x^i \in \mathbb{C}\lbrack x\rbrack$ i $q \in \mathbb{C} \setminus \{0\}$ izračunava $f(1), f(q), \dots, f(q^{n - 1})$, pri čemu se ne zahtijeva da $q$ bude korijen jedinice. Može se primijeniti i na teorijsko-brojevnu transformaciju. U nastavku predstavljamo Chirp Z-transformaciju i njezinu inverznu transformaciju.

## Chirp Z-transformacija

Prema definiciji, Chirp Z-transformacija može se zapisati kao

$$
\operatorname{\mathsf{CZT}}_n : \left(f(x), q\right) \mapsto
\begin{bmatrix}
f(1) & f(q) & \cdots & f\left(q^{n - 1}\right)
\end{bmatrix}
$$

gdje je $f(x) := \sum_{i = 0}^{m - 1} f_i x^i \in \mathbb{C}\lbrack x\rbrack$ i $q \in \mathbb{C} \setminus \{0\}$.

### Bluesteinov algoritam

Razmotrimo

$$
ij = \binom{i}{2} + \binom{-j}{2} - \binom{i - j}{2}
$$

gdje su $i, j \in \mathbb{Z}$; možemo konstruirati

$$
\begin{aligned}
G(x) & := \sum_{i = -(m - 1)}^{n - 1} q^{-\binom{i}{2}}x^i, \\
F(x) & := \sum_{i = 0}^{m - 1} f_i q^{\binom{-i}{2}}x^i.
\end{aligned}
$$

Pri tome je $G(x) \in \mathbb{C}\left\lbrack x, x^{-1}\right\rbrack$, a za $i = 0, \dots, n - 1$ imamo

$$
\begin{aligned}
\left\lbrack x^i\right\rbrack\left(G(x)F(x)\right) &=
\sum_{j = 0}^{m - 1}\left(\left(\left\lbrack x^{i - j}\right\rbrack G(x)\right)\left(\left\lbrack x^j\right\rbrack F(x)\right)\right) \\
&= \sum_{j = 0}^{m - 1} f_j q^{\binom{-j}{2} - \binom{i - j}{2}} \\
&= q^{-\binom{i}{2}} f\left(q^i\right)
\end{aligned}
$$

Osim toga, $q^{\binom{i + 1}{2}} = q^{\binom{i}{2}}\cdot q^i$ i $\binom{-i}{2} = \binom{i + 1}{2}$. Izračun se dakle može obaviti jednim množenjem polinoma; taj se algoritam naziva Bluesteinov algoritam.

??? note "Predložak ([P6800【模板】Chirp Z-Transform (predložak)](https://www.luogu.com.cn/problem/P6800))"
    ```cpp
    --8<-- "docs/math/code/poly/czt/czt_1.cpp:core"
    ```

## Inverzna Chirp Z-transformacija

Inverzna Chirp Z-transformacija može se zapisati kao

$$
\operatorname{\mathsf{ICZT}}_n :
\left(
    \begin{bmatrix} f(1) & f(q) & \cdots & f\left(q^{n - 1}\right)
    \end{bmatrix},q
\right)
\mapsto f(x)
$$

gdje je $f(x) \in \mathbb{C}\left\lbrack x\right\rbrack_{< n}$ i $q \in \mathbb{C} \setminus \{0\}$, te $q^i \neq q^j$ za sve $i \neq j$, što je uvjet za interpolaciju polinoma.

### Bostan–Schostov algoritam

Podsjetimo se da [Lagrangeova interpolacijska formula](../numerical/interp.md#lagrange-插值法) glasi

$$
f(x) = \sum_{i = 0}^{n - 1}\left(f\left(x_i\right)\prod_{0 \leq j < n \atop j \neq i} \frac{x - x_j}{x_i - x_j}\right)
$$

uz $x_i \neq x_j$ za sve $i \neq j$. Kao i u [brzoj interpolaciji polinoma](./multipoint-eval-interpolation.md#brza-interpolacija-polinoma), stavimo $M(x) := \prod_{i = 0}^{n - 1}\left(x - x_i\right)$; prema L'Hôpitalovu pravilu vrijedi

$$
M'(x_i) = \lim_{x \to x_i} \frac{M(x)}{x - x_i} = \prod_{0 \leq j < n \atop j \neq i}\left(x_i - x_j\right)
$$

**Modificirana Lagrangeova interpolacijska formula** glasi

$$
f(x) = M(x)\left(\sum_{i = 0}^{n - 1}\frac{f\left(x_i\right)/M'(x_i)}{x - x_i}\right)
$$

Sada dakle imamo

$$
f(x) = M(x)\left(\sum_{i = 0}^{n - 1}\frac{f\left(q^i\right)/M'\left(q^i\right)}{x - q^i}\right)
$$

gdje je $M(x)=\prod_{j = 0}^{n - 1}\left(x - q^j\right)$. Ako pretpostavimo da je $n$ paran te stavimo $n = 2k$ i $H(x) := \prod_{j = 0}^{k - 1}\left(x - q^j\right)$, tada je

$$
M(x) = H(x) \cdot q^{k^2} \cdot H\left(\frac{x}{q^k}\right)
$$

što nam omogućuje brzo računanje $M(x)$. Zatim Bluesteinovim algoritmom izračunamo $M'(1), \dots, M'(q^{n - 1})$. Stavimo $c_i := f\left(q^i\right)/M'\left(q^i\right)$; imamo

$$
f(x) = M(x)\left(\sum_{i = 0}^{n - 1}\frac{c_i}{x - q^i}\right)
$$

Budući da je $\deg f(x) < n$, dovoljno je izračunati $\sum_{i = 0}^{n - 1}\frac{c_i}{x - q^i}\bmod{x^n}$, gdje je $\frac{c_i}{x - q^i} \in \mathbb{C}\left\lbrack\left\lbrack x\right\rbrack\right\rbrack$, odnosno

$$
\begin{aligned}
\sum_{i = 0}^{n - 1}\frac{c_i}{x - q^i} \bmod x^n &=
-\sum_{i = 0}^{n - 1}\left(\sum_{j = 0}^{n - 1} c_i q^{-i(j+1)}x^j\right) \\
&= -\sum_{j = 0}^{n - 1} C\left(q^{-j - 1}\right) x^j
\end{aligned}
$$

gdje je $C(x) = \sum_{i = 0}^{n - 1} c_i x^i$. Vrijednosti $C\left(q^{-1}\right), \dots, C\left(q^{-n}\right)$ možemo izračunati Bluesteinovim algoritmom.

Ukratko, redom provodimo sljedeće izračune:

1.  metodom smanji pa vladaj (decrease and conquer) izračunamo $M(x)$;
2.  Bluesteinovim algoritmom izračunamo $M'(1), \dots, M'(q^{n - 1})$;
3.  Bluesteinovim algoritmom izračunamo $C\left(q^{-1}\right), \dots, C\left(q^{-n}\right)$;
4.  jednim množenjem polinoma izračunamo $f(x)$.

Vremenska složenost svakog od tih koraka jednaka je složenosti množenja dvaju polinoma stupnja najviše $n$.

??? note "Implementacija predloška"
    ```cpp
    --8<-- "docs/math/code/poly/czt/inv_czt_1.cpp:core"
    ```

## Literatura

1.  [Bostan, A. (2010). Fast algorithms for polynomials and matrices. JNCF 2010. Algorithms Project, INRIA.](https://specfun.inria.fr/bostan/publications/exposeJNCF.pdf)
