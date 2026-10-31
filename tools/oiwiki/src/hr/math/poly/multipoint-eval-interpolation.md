---
title: Evaluacija polinoma u više točaka | brza interpolacija
---

## Evaluacija polinoma u više točaka

### Opis

Zadan je polinom $f\left(x\right)$ i $n$ točaka $x_{1},x_{2},\dots,x_{n}$; treba izračunati

$$
f\left(x_{1}\right),f\left(x_{2}\right),\dots,f\left(x_{n}\right)
$$

### Rješenje

Razmotrimo kako metodom podijeli pa vladaj (divide and conquer) veličinu problema smanjiti na pola.

Zadane točke podijelimo na dva dijela:

$$
\begin{aligned}
    X_{0}&=\left\{x_{1},x_{2},\dots,x_{\left\lfloor\frac{n}{2}\right\rfloor}\right\}\\
    X_{1}&=\left\{x_{\left\lfloor\frac{n}{2}\right\rfloor+1},x_{\left\lfloor\frac{n}{2}\right\rfloor+2},\dots,x_{n}\right\}
\end{aligned}
$$

Konstruiramo polinom

$$
g_{0}\left(x\right)=\prod_{x_{i}\in X_{0}}\left(x-x_{i}\right)
$$

Tada je $\forall x\in X_{0}:g_{0}\left(x\right)=0$.

Razmotrimo zapis $f\left(x\right)$ u obliku $g_{0}\left(x\right)Q\left(x\right)+f_{0}\left(x\right)$, tj.:

$$
f_{0}\left(x\right)\equiv f\left(x\right)\pmod{g_{0}\left(x\right)}
$$

Tada je $\forall x\in X_{0}:f\left(x\right)=g_{0}\left(x\right)Q\left(x\right)+f_{0}\left(x\right)=f_{0}\left(x\right)$, a za $X_{1}$ vrijedi analogno.

Time je veličina problema smanjena na pola, pa se problem može riješiti podjelom + računanjem ostatka pri dijeljenju polinoma.

Vremenska složenost

$$
T\left(n\right)=2T\left(\frac{n}{2}\right)+O\left(n\log{n}\right)=O\left(n\log^{2}{n}\right)
$$

## Brza interpolacija polinoma

### Opis

Zadan je skup od $n+1$ točaka

$$
X=\left\{\left(x_{0},y_{0}\right),\left(x_{1},y_{1}\right),\dots,\left(x_{n},y_{n}\right)\right\}
$$

Treba naći polinom $f\left(x\right)$ stupnja $n$ takav da vrijedi $\forall\left(x,y\right)\in X:f\left(x\right)=y$.

### Rješenje

Razmotrimo Lagrangeovu interpolacijsku formulu

$$
f(x) = \sum_{i=1}^{n} \prod_{j\neq i }\frac{x-x_j}{x_i-x_j} y_i
$$

Označimo polinom $M(x) = \prod_{i=1}^n (x - x_i)$; prema L'Hôpitalovu pravilu vrijedi

$$
\prod_{j\neq i} (x_i - x_j) = \lim_{x\rightarrow x_i} \frac{\prod_{j=1}^n (x - x_j)}{x - x_i} = M'(x_i)
$$

Stoga se polinom može zapisati kao

$$
f(x) = \sum_{i = 1}^n \frac{y_i}{M'(x_i)}\prod_{j \neq i}(x - x_j)
$$

Najprije podjelom izračunamo koeficijente polinoma $M(x)$, a zatim evaluacijom u više točaka u vremenu $O(n\log^2 n)$ izračunamo sve vrijednosti $M'(x_i)$.

Stavimo $v_i = \frac{y_i}{M'(x_i)}$ i razmotrimo kako izračunati $f(x)$. Za $n = 1$ imamo $f(x) = v_1, M(x) = x - x_1$. Inače stavimo

$$
\begin{aligned}
f_0(x) & = \sum_{i = 1}^{\left\lfloor \frac n2 \right \rfloor} v_i\prod_{j \neq i \wedge j \le \left\lfloor \frac n2 \right \rfloor}(x - x_j)\\
M_0(x) & = \prod_{i = 1}^{\left\lfloor \frac n2 \right \rfloor} (x - x_i)\\
f_1(x) & = \sum_{i = \left\lfloor \frac n2 \right \rfloor+1}^n v_i\prod_{j \neq i \wedge \left\lfloor \frac n2 \right \rfloor < j \le n}(x - x_j) \\
M_1(x) & = \prod_{i = \left\lfloor \frac n2 \right \rfloor+1}^n (x - x_i)
\end{aligned}
$$

Dobivamo $f(x) = f_0(x)M_1(x) + f_1(x)M_0(x), M(x) = M_0(x)M_1(x)$, pa se može računati podjelom; složenost ovog dijela također je $O(n\log^2 n)$.
