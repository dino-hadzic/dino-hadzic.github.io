---
title: Elementarne funkcije polinoma
---

Ova stranica obuhvaća uobičajene operacije elementarnih funkcija nad polinomima. Konkretno, stranica sadrži sljedeće:

1.  inverz polinoma
2.  korijen polinoma
3.  dijeljenje polinoma
4.  ostatak pri dijeljenju polinoma
5.  eksponencijalnu funkciju polinoma
6.  logaritamsku funkciju polinoma
7.  trigonometrijske funkcije polinoma
8.  inverzne trigonometrijske funkcije polinoma

??? note "Elementarne i neelementarne funkcije"
    Elementarne funkcije definiraju se ovako[^ref1]:
    
    Ako u polju $F$ postoji preslikavanje $u\to \partial u$ koje zadovoljava:
    
    1.  $\partial(u+v)=\partial u+\partial v$
    2.  $\partial(uv)=u\partial v+v\partial u$
    
    tada to polje nazivamo **diferencijalnim poljem**.
    
    Ako funkcija $u$ nad diferencijalnim poljem $F$ zadovoljava bilo koji od sljedećih uvjeta, funkciju $u$ nazivamo elementarnom funkcijom:
    
    1.  $u$ je algebarska funkcija nad $F$.
    2.  $u$ je eksponencijalnog tipa nad $F$, tj. postoji $a\in F$ takav da je $\partial u=u\partial a$.
    3.  $u$ je logaritamskog tipa nad $F$, tj. postoji $a\in F$ takav da je $\partial u=\frac{\partial a}{a}$.
    
    Uobičajene elementarne funkcije su:
    
    1.  algebarske funkcije: funkcije $f(x)$ za koje postoji polinom konačnog stupnja $P$ takav da je $P(f(x))=0$, npr. $2x+1$,$\sqrt{x}$,$(1+x^2)^{-1}$,$|x|$.
    2.  eksponencijalne funkcije
    3.  logaritamske funkcije
    4.  trigonometrijske funkcije
    5.  inverzne trigonometrijske funkcije
    6.  hiperbolne funkcije
    7.  inverzne hiperbolne funkcije
    8.  kompozicije gornjih funkcija, npr.:
    
        $$
        \frac{\mathrm{e}^{\tan x}}{1+x^2}\sin\left(\sqrt{1+\ln^2 x}\right)
        $$
    
        $$
        -\mathrm{i} \ln\left(x+\mathrm{i}\sqrt{1-x^2}\right)
        $$
    
    Uobičajene neelementarne funkcije su:
    
    1.  funkcija pogreške:
    
        $$
        \operatorname{erf}(x):=\frac{2}{\sqrt{\pi}}\int_{0}^{x}\exp\left(-t^2\right)\mathrm{d}t
        $$

## Inverz polinoma

Zadan je polinom $f\left(x\right)$; treba odrediti $f^{-1}\left(x\right)$.

### Rješenje

#### Metoda udvostručavanja

Najprije, očito je

$$
\left[x^{0}\right]f^{-1}\left(x\right)=\left(\left[x^{0}\right]f\left(x\right)\right)^{-1}
$$

Pretpostavimo da smo već odredili inverz $f^{-1}_{0}\left(x\right)$ polinoma $f\left(x\right)$ modulo $x^{\left\lceil\frac{n}{2}\right\rceil}$.
Vrijedi:

$$
\begin{aligned}
    f\left(x\right)f^{-1}_{0}\left(x\right)&\equiv 1 &\pmod{x^{\left\lceil\frac{n}{2}\right\rceil}}\\
    f\left(x\right)f^{-1}\left(x\right)&\equiv 1 &\pmod{x^{\left\lceil\frac{n}{2}\right\rceil}}\\
    f^{-1}\left(x\right)-f^{-1}_{0}\left(x\right)&\equiv 0 &\pmod{x^{\left\lceil\frac{n}{2}\right\rceil}}
\end{aligned}
$$

Kvadriranjem obiju strana dobivamo:

$$
f^{-2}\left(x\right)-2f^{-1}\left(x\right)f^{-1}_{0}\left(x\right)+f^{-2}_{0}\left(x\right)\equiv 0 \pmod{x^{n}}
$$

Množenjem obiju strana s $f\left(x\right)$ i prebacivanjem članova dobivamo:

$$
f^{-1}\left(x\right)\equiv f^{-1}_{0}\left(x\right)\left(2-f\left(x\right)f^{-1}_{0}\left(x\right)\right) \pmod{x^{n}}
$$

Dovoljno je računati rekurzivno.

**Vremenska složenost**

$$
T\left(n\right)=T\left(\frac{n}{2}\right)+O\left(n\log{n}\right)=O\left(n\log{n}\right)
$$

#### Newtonova metoda

Vidi [Newtonovu metodu](./newton.md#newtons-method).

#### Graeffeova metoda

Želimo li odrediti $f^{-1}(x)\bmod x^{2n}$, promotrimo

$$
\begin{aligned}
f^{-1}(x)\bmod x^{2n}&= f(-x)(f(x)f(-x))^{-1}\bmod x^{2n}\\
&=f(-x)g^{-1}(x^2)\bmod x^{2n}
\end{aligned}
$$

Dovoljno je odrediti $g^{-1}(x)\bmod x^n$ pa iz toga rekonstruirati $g^{-1}(x^2)\bmod x^{2n}$, jer je $f(x)f(-x)$ parna funkcija; vremenska složenost ista je kao gore.

### Kôd

??? note "Inverz polinoma"
    ```cpp
    constexpr int MAXN = 262144;
    constexpr int mod = 998244353;
    
    using i64 = long long;
    using poly_t = int[MAXN];
    using poly = int *const;
    
    void polyinv(const poly &h, const int n, poly &f) {
      /* f = 1 / h = f_0 (2 - f_0 h) */
      static poly_t inv_t;
      std::fill(f, f + n + n, 0);
      f[0] = fpow(h[0], mod - 2);
      for (int t = 2; t <= n; t <<= 1) {
        const int t2 = t << 1;
        std::copy(h, h + t, inv_t);
        std::fill(inv_t + t, inv_t + t2, 0);
    
        DFT(f, t2);
        DFT(inv_t, t2);
        for (int i = 0; i != t2; ++i)
          f[i] = (i64)f[i] * sub(2, (i64)f[i] * inv_t[i] % mod) % mod;
        IDFT(f, t2);
    
        std::fill(f + t, f + t2, 0);
      }
    }
    ```

### Primjeri zadataka

1.  Prebrojavanje označenih jednostavnih neusmjerenih povezanih grafova: [„POJ 1737” Connected Graph](http://poj.org/problem?id=1737)

## Korijen polinoma

Zadan je polinom $g\left(x\right)$; treba odrediti $f\left(x\right)$ takav da vrijedi:

$$
f^{2}\left(x\right)\equiv g\left(x\right) \pmod{x^{n}}
$$

### Rješenje

#### Metoda udvostručavanja

Najprije razmotrimo slučaj kada $\left[x^0\right]g(x)$ nije $0$.

Očito je:

$$
\left[x^0\right]f(x) = \sqrt{\left[x^0\right]g(x)}
$$

Ako $\left[x^0\right]g(x)$ nema kvadratni korijen, ni polinom $g(x)$ nema kvadratni korijen.

> $\left[x^0\right]g(x)$ može imati više kvadratnih korijena; odabirom različitih korijena dobivaju se različiti $f(x)$.

Pretpostavimo da smo već odredili kvadratni korijen $f_{0}\left(x\right)$ polinoma $g\left(x\right)$ modulo $x^{\left\lceil\frac{n}{2}\right\rceil}$; tada vrijedi:

$$
\begin{aligned}
    f_{0}^{2}\left(x\right)&\equiv g\left(x\right) &\pmod{x^{\left\lceil\frac{n}{2}\right\rceil}}\\
    f_{0}^{2}\left(x\right)-g\left(x\right)&\equiv 0 &\pmod{x^{\left\lceil\frac{n}{2}\right\rceil}}\\
    \left(f_{0}^{2}\left(x\right)-g\left(x\right)\right)^{2}&\equiv 0 &\pmod{x^{n}}\\
    \left(f_{0}^{2}\left(x\right)+g\left(x\right)\right)^{2}&\equiv 4f_{0}^{2}\left(x\right)g\left(x\right) &\pmod{x^{n}}\\
    \left(\frac{f_{0}^{2}\left(x\right)+g\left(x\right)}{2f_{0}\left(x\right)}\right)^{2}&\equiv g\left(x\right) &\pmod{x^{n}}\\
    \frac{f_{0}^{2}\left(x\right)+g\left(x\right)}{2f_{0}\left(x\right)}&\equiv f\left(x\right) &\pmod{x^{n}}\\
    2^{-1}f_{0}\left(x\right)+2^{-1}f_{0}^{-1}\left(x\right)g\left(x\right)&\equiv f\left(x\right) &\pmod{x^{n}}
\end{aligned}
$$

Dovoljno je računati udvostručavanjem.

**Vremenska složenost**

$$
T\left(n\right)=T\left(\frac{n}{2}\right)+O\left(n\log{n}\right)=O\left(n\log{n}\right)
$$

Postoji i varijanta s manjom konstantom: tijekom udvostručavanja uz $f\left(x\right)$ istodobno održavamo i $f^{-1}\left(x\right)$ umjesto da svaki put iznova računamo inverz.

> Kada je $\left[x^{0}\right]g\left(x\right)\neq 1$, za izračun $\left[x^{0}\right]f\left(x\right)$ možda će trebati kvadratni ostaci.

Gornja metoda zahtijeva poznavanje inverza od $f_{0}(x)$, pa slobodni član ne smije biti $0$.

Ako je $\left[x^0\right]g(x) = 0$, rastavimo $g(x)$ na $x^{k}h(x)$, pri čemu je $\left[x^0\right]h(x) \not = 0$.

-   Ako je $k$ neparan, $g(x)$ nema kvadratni korijen.

-   Ako je $k$ paran, odredimo kvadratni korijen $\sqrt{h(x)}$ polinoma $h(x)$ i dobivamo $f(x) \equiv x^{k/2} \sqrt{h(x)} \pmod{x^{n}}$.

??? note "Referentni kôd za Luogu predložak [P5205【模板】多项式开根 (Predložak: korijen polinoma)](https://www.luogu.com.cn/problem/P5205)"
    ```cpp
    --8<-- "docs/math/code/poly/sqrt/sqrt_1.cpp"
    ```

#### Newtonova metoda

Vidi [Newtonovu metodu](./newton.md#newtons-method).

### Primjeri zadataka

1.  [„Codeforces Round #250” E. The Child and Binary Tree](https://codeforces.com/contest/438/problem/E)

## Dijeljenje i ostatak polinoma

Zadani su polinomi $f\left(x\right),g\left(x\right)$; treba odrediti kvocijent $Q\left(x\right)$ i ostatak $R\left(x\right)$ pri dijeljenju $f\left(x\right)$ s $g\left(x\right)$.

### Rješenje

Primjećujemo da bismo, kad bismo mogli ukloniti utjecaj $R\left(x\right)$, zadatak mogli izravno riješiti [inverzom polinoma](#inverz-polinoma).

Razmotrimo transformaciju

$$
f^{R}\left(x\right)=x^{\operatorname{deg}{f}}f\left(\frac{1}{x}\right)
$$

Promatranjem vidimo da ona zapravo obrće redoslijed koeficijenata polinoma $f\left(x\right)$.

Neka je $n=\operatorname{deg}{f},m=\operatorname{deg}{g}$.

U $f\left(x\right)=Q\left(x\right)g\left(x\right)+R\left(x\right)$ zamijenimo $x$ s $\frac{1}{x}$ i obje strane pomnožimo s $x^{n}$; dobivamo:

$$
\begin{aligned}
    x^{n}f\left(\frac{1}{x}\right)&=x^{n-m}Q\left(\frac{1}{x}\right)x^{m}g\left(\frac{1}{x}\right)+x^{n-m+1}x^{m-1}R\left(\frac{1}{x}\right)\\
    f^{R}\left(x\right)&=Q^{R}\left(x\right)g^{R}\left(x\right)+x^{n-m+1}R^{R}\left(x\right)
\end{aligned}
$$

Uočimo da je u gornjem izrazu koeficijent uz $R^{R}\left(x\right)$ jednak $x^{n-m+1}$, pa ako sve promatramo modulo $x^{n-m+1}$, uklanjamo utjecaj $R^{R}\left(x\right)$.

Budući da je stupanj $Q^{R}\left(x\right)$ jednak $\left(n-m\right)<\left(n-m+1\right)$, $Q^{R}\left(x\right)$ time nije pogođen.

Dakle:

$$
f^{R}\left(x\right)\equiv Q^{R}\left(x\right)g^{R}\left(x\right)\pmod{x^{n-m+1}}
$$

Inverzom polinoma odredimo $Q\left(x\right)$, a uvrštavanjem natrag dobivamo $R\left(x\right)$.

**Vremenska složenost**  $O\left(n\log{n}\right)$.

## Logaritam i eksponencijalna funkcija polinoma

Zadan je polinom $f(x)$; treba odrediti $\ln{f(x)}$ i $\exp{f(x)}$ modulo $x^{n}$.

### Rješenje

#### Obična metoda

=== "Logaritam polinoma"
    Najprije, ako za polinom $f(x)$ postoji $\ln{f(x)}$, tada po [definiciji](./intro.md#复合) mora vrijediti:
    
    $$
    [x^{0}]f(x)=1
    $$
    
    Deriviranjem pa integriranjem $\ln{f(x)}$ dobivamo:
    
    $$
    \begin{aligned}
        \frac{\mathrm{d} \ln{f(x)}}{\mathrm{d} x} & \equiv \frac{f'(x)}{f(x)} & \pmod{x^{n}} \\
        \ln{f(x)} & \equiv \int \mathrm{d} \ln{f(x)} \equiv \int\frac{f'(x)}{f(x)} \mathrm{d} x & \pmod{x^{n}}
    \end{aligned}
    $$
    
    Deriviranje i integriranje polinoma imaju vremensku složenost $O(n)$, a inverz $O(n\log{n})$, pa je vremenska složenost računanja $\ln$ polinoma $O(n\log{n})$.

=== "Eksponencijalna funkcija polinoma"
    Najprije, ako za polinom $f(x)$ postoji $\exp{f(x)}$, tada mora vrijediti:
    
    $$
    [x^{0}]f(x)=0
    $$
    
    U suprotnom slobodni član od $\exp{f(x)}$ ne konvergira.
    
    Deriviranjem $\exp{f(x)}$ dobivamo:
    
    $$
    \frac{\mathrm{d} \exp{f(x)}}{\mathrm{d} x} \equiv \exp{f(x)}f'(x)\pmod{x^{n}}
    $$
    
    Usporedbom koeficijenata na obje strane dobivamo:
    
    $$
    [x^{n-1}]\frac{\mathrm{d} \exp{f(x)}}{\mathrm{d} x} = \sum_{i = 0}^{n - 1} \left([x^{i}]\exp{f(x)}\right) \left([x^{n-i-1}]f'(x)\right)
    $$
    
    $$
    n[x^{n}]\exp{f(x)} = \sum_{i = 0}^{n - 1} \left([x^{i}]\exp{f(x)}\right) \left((n - i)[x^{n - i}]f(x)\right)
    $$
    
    To se rješava FFT-om s podjelom (divide and conquer FFT).
    
    **Vremenska složenost**  $O(n\log^{2}{n})$.

#### Newtonova metoda

[Newtonovom metodom](./newton.md#newtons-method) $\exp$ polinoma može se izračunati u vremenskoj složenosti $O(n\log{n})$.

### Kôd

??? note "ln/exp polinoma"
    ```cpp
    constexpr int MAXN = 262144;
    constexpr int mod = 998244353;
    
    using i64 = long long;
    using poly_t = int[MAXN];
    using poly = int *const;
    
    void derivative(const poly &h, const int n, poly &f) {
      for (int i = 1; i != n; ++i) f[i - 1] = (i64)h[i] * i % mod;
      f[n - 1] = 0;
    }
    
    void integrate(const poly &h, const int n, poly &f) {
      for (int i = n - 1; i; --i) f[i] = (i64)h[i - 1] * inv[i] % mod;
      f[0] = 0; /* C */
    }
    
    void polyln(const poly &h, const int n, poly &f) {
      /* f = ln h = ∫ h' / h dx */
      assert(h[0] == 1);
      static poly_t ln_t;
      const int t = n << 1;
    
      derivative(h, n, ln_t);
      std::fill(ln_t + n, ln_t + t, 0);
      polyinv(h, n, f);
    
      DFT(ln_t, t);
      DFT(f, t);
      for (int i = 0; i != t; ++i) ln_t[i] = (i64)ln_t[i] * f[i] % mod;
      IDFT(ln_t, t);
    
      integrate(ln_t, n, f);
    }
    
    void polyexp(const poly &h, const int n, poly &f) {
      /* f = exp(h) = f_0 (1 - ln f_0 + h) */
      assert(h[0] == 0);
      static poly_t exp_t;
      std::fill(f, f + n + n, 0);
      f[0] = 1;
      for (int t = 2; t <= n; t <<= 1) {
        const int t2 = t << 1;
    
        polyln(f, t, exp_t);
        exp_t[0] = sub(pls(h[0], 1), exp_t[0]);
        for (int i = 1; i != t; ++i) exp_t[i] = sub(h[i], exp_t[i]);
        std::fill(exp_t + t, exp_t + t2, 0);
    
        DFT(f, t2);
        DFT(exp_t, t2);
        for (int i = 0; i != t2; ++i) f[i] = (i64)f[i] * exp_t[i] % mod;
        IDFT(f, t2);
    
        std::fill(f + t, f + t2, 0);
      }
    }
    ```

### Primjeri zadataka

1.  Izračunati $f^{k}(x)$

    Uobičajeni pristup je brzo potenciranje polinoma, vremenske složenosti $O(n\log{n}\log{k})$.

    Kada je $[x^{0}]f(x)=1$, vrijedi:

    $$
    f^{k}(x)=\exp{\left(k\ln{f(x)}\right)}
    $$

    Kada je $[x^{0}]f(x)\neq 1$, neka je $f_{i}x^{i}$ član najnižeg stupnja polinoma $f(x)$; tada je:

    $$
    f^{k}(x)=f_{i}^{k}x^{ik}\exp{\left(k\ln{\frac{f(x)}{f_{i}x^{i}}}\right)}
    $$

    **Vremenska složenost**  $O(n\log{n})$.

## Trigonometrijske funkcije polinoma

Zadan je polinom $f\left(x\right)$; treba odrediti $\sin{f\left(x\right)}, \cos{f\left(x\right)}$ i $\tan{f\left(x\right)}$ modulo $x^{n}$.

### Rješenje

Najprije iz [Eulerove formule](../complex.md#欧拉公式) $\left(\mathrm{e}^{\mathrm{i}x} = \cos{x} + \mathrm{i}\sin{x}\right)$ dobivamo [drugi zapis trigonometrijskih funkcija](https://en.wikipedia.org/wiki/Trigonometric_functions#Relationship_to_exponential_function_and_complex_numbers):

$$
\begin{aligned}
    \sin{x} &= \frac{\mathrm{e}^{\mathrm{i}x} - \mathrm{e}^{-\mathrm{i}x}}{2\mathrm{i}} \\
    \cos{x} &= \frac{\mathrm{e}^{\mathrm{i}x} + \mathrm{e}^{-\mathrm{i}x}}{2}
\end{aligned}
$$

Uvrštavanjem $f\left(x\right)$ dobivamo:

$$
\begin{aligned}
    \sin{f\left(x\right)} &= \frac{\exp{\left(\mathrm{i}f\left(x\right)\right)} - \exp{\left(-\mathrm{i}f\left(x\right)\right)}}{2\mathrm{i}} \\
    \cos{f\left(x\right)} &= \frac{\exp{\left(\mathrm{i}f\left(x\right)\right)} + \exp{\left(-\mathrm{i}f\left(x\right)\right)}}{2}
\end{aligned}
$$

Program napisan izravno po gornjim izrazima daje $\sin{f\left(x\right)}$ i $\cos{f\left(x\right)}$ modulo $x^{n}$. Zatim iz $\tan{f\left(x\right)} = \frac{\sin{f\left(x\right)}}{\cos{f\left(x\right)}}$ dobivamo $\tan{f\left(x\right)}$.

### Kôd

??? note "Trigonometrijske funkcije polinoma"
    Uočimo da NTT radimo nad $\mathbb{Z}_{998244353}$, pa u skladu s tim imaginarnu jedinicu $\mathrm{i}$ treba zamijeniti s $86583718$ ili $911660635$:
    
    $$
    \begin{aligned}
               & \mathrm{i} = \sqrt{-1} \equiv \sqrt{998244352} \pmod{998244353}       \\
      \implies & \phantom{\text{or}} \quad \mathrm{i} \equiv 86583718 \pmod{998244353} \\
               & \text{or} \quad \mathrm{i} \equiv 911660635 \pmod{998244353}
    \end{aligned}
    $$
    
    ```cpp
    constexpr int MAXN = 262144;
    constexpr int mod = 998244353;
    constexpr int imgunit = 86583718; /* sqrt(-1) = sqrt(998233452) */
    
    using i64 = long long;
    using poly_t = int[MAXN];
    using poly = int *const;
    
    void polytri(const poly &h, const int n, poly &sin_t, poly &cos_t) {
      /* sin(f) = (exp(i * f) - exp(- i * f)) / 2i */
      /* cos(f) = (exp(i * f) + exp(- i * f)) / 2 */
      /* tan(f) = sin(f) / cos(f) */
      assert(h[0] == 0);
      static poly_t tri1_t, tri2_t;
    
      for (int i = 0; i != n; ++i) tri2_t[i] = (i64)h[i] * imgunit % mod;
      polyexp(tri2_t, n, tri1_t);
      polyinv(tri1_t, n, tri2_t);
    
      if (sin_t != nullptr) {
        const int invi = fpow(pls(imgunit, imgunit), mod - 2);
        for (int i = 0; i != n; ++i)
          sin_t[i] = (i64)(tri1_t[i] - tri2_t[i] + mod) * invi % mod;
      }
      if (cos_t != nullptr) {
        for (int i = 0; i != n; ++i) cos_t[i] = div2(pls(tri1_t[i], tri2_t[i]));
      }
    }
    ```

## Inverzne trigonometrijske funkcije polinoma

Zadan je polinom $f\left(x\right)$; treba odrediti $\arcsin{f\left(x\right)}, \arccos{f\left(x\right)}$ i $\arctan{f\left(x\right)}$ modulo $x^{n}$.

### Rješenje

Po uzoru na računanje $\ln$ polinoma, deriviranjem pa integriranjem inverznih trigonometrijskih funkcija dobivamo:

$$
\begin{aligned}
    \frac{\mathrm{d}}{\mathrm{d} x} \arcsin{x} &= \frac{1}{\sqrt{1 - x^{2}}} \\
    \arcsin{x} &= \int \frac{1}{\sqrt{1 - x^{2}}} \mathrm{d} x \\
    \frac{\mathrm{d}}{\mathrm{d} x} \arccos{x} &= - \frac{1}{\sqrt{1 - x^{2}}} \\
    \arccos{x} &= - \int \frac{1}{\sqrt{1 - x^{2}}} \mathrm{d} x \\
    \frac{\mathrm{d}}{\mathrm{d} x} \arctan{x} &= \frac{1}{1 + x^{2}} \\
    \arctan{x} &= \int \frac{1}{1 + x^{2}} \mathrm{d} x
\end{aligned}
$$

Uvrštavanjem $f\left(x\right)$ dobivamo:

$$
\begin{aligned}
    \frac{\mathrm{d}}{\mathrm{d} x} \arcsin{f\left(x\right)} &= \frac{f'\left(x\right)}{\sqrt{1 - f^{2}\left(x\right)}} \\
    \arcsin{f\left(x\right)} &= \int \frac{f'\left(x\right)}{\sqrt{1 - f^{2}\left(x\right)}} \mathrm{d} x \\
    \frac{\mathrm{d}}{\mathrm{d} x} \arccos{f\left(x\right)} &= - \frac{f'\left(x\right)}{\sqrt{1 - f^{2}\left(x\right)}} \\
    \arccos{f\left(x\right)} &= - \int \frac{f'\left(x\right)}{\sqrt{1 - f^{2}\left(x\right)}} \mathrm{d} x \\
    \frac{\mathrm{d}}{\mathrm{d} x} \arctan{f\left(x\right)} &= \frac{f'\left(x\right)}{1 + f^{2}\left(x\right)} \\
    \arctan{f\left(x\right)} &= \int \frac{f'\left(x\right)}{1 + f^{2}\left(x\right)} \mathrm{d} x
\end{aligned}
$$

Dovoljno je računati izravno po formulama.

### Kôd

??? note "Inverzne trigonometrijske funkcije polinoma"
    ```cpp
    constexpr int MAXN = 262144;
    constexpr int mod = 998244353;
    
    using i64 = long long;
    using poly_t = int[MAXN];
    using poly = int *const;
    
    void derivative(const poly &h, const int n, poly &f) {
      for (int i = 1; i != n; ++i) f[i - 1] = (i64)h[i] * i % mod;
      f[n - 1] = 0;
    }
    
    void integrate(const poly &h, const int n, poly &f) {
      for (int i = n - 1; i; --i) f[i] = (i64)h[i - 1] * inv[i] % mod;
      f[0] = 0; /* C */
    }
    
    void polyarcsin(const poly &h, const int n, poly &f) {
      /* arcsin(f) = ∫ f' / sqrt(1 - f^2) dx  */
      static poly_t arcsin_t;
      const int t = n << 1;
      std::copy(h, h + n, arcsin_t);
      std::fill(arcsin_t + n, arcsin_t + t, 0);
    
      DFT(arcsin_t, t);
      for (int i = 0; i != t; ++i) arcsin_t[i] = sqr(arcsin_t[i]);
      IDFT(arcsin_t, t);
    
      arcsin_t[0] = sub(1, arcsin_t[0]);
      for (int i = 1; i != n; ++i)
        arcsin_t[i] = arcsin_t[i] ? mod - arcsin_t[i] : 0;
    
      polysqrt(arcsin_t, n, f);
      polyinv(f, n, arcsin_t);
      derivative(h, n, f);
    
      DFT(f, t);
      DFT(arcsin_t, t);
      for (int i = 0; i != t; ++i) arcsin_t[i] = (i64)f[i] * arcsin_t[i] % mod;
      IDFT(arcsin_t, t);
    
      integrate(arcsin_t, n, f);
    }
    
    void polyarccos(const poly &h, const int n, poly &f) {
      /* arccos(f) = - ∫ f' / sqrt(1 - f^2) dx  */
      polyarcsin(h, n, f);
      for (int i = 0; i != n; ++i) f[i] = f[i] ? mod - f[i] : 0;
    }
    
    void polyarctan(const poly &h, const int n, poly &f) {
      /* arctan(f) = ∫ f' / (1 + f^2) dx  */
      static poly_t arctan_t;
      const int t = n << 1;
      std::copy(h, h + n, arctan_t);
      std::fill(arctan_t + n, arctan_t + t, 0);
    
      DFT(arctan_t, t);
      for (int i = 0; i != t; ++i) arctan_t[i] = sqr(arctan_t[i]);
      IDFT(arctan_t, t);
    
      inc(arctan_t[0], 1);
      std::fill(arctan_t + n, arctan_t + t, 0);
    
      polyinv(arctan_t, n, f);
      derivative(h, n, arctan_t);
    
      DFT(f, t);
      DFT(arctan_t, t);
      for (int i = 0; i != t; ++i) arctan_t[i] = (i64)f[i] * arctan_t[i] % mod;
      IDFT(arctan_t, t);
    
      integrate(arctan_t, n, f);
    }
    ```

## Literatura i poveznice

[^ref1]: [Elementary function – Wikipedia](https://en.wikipedia.org/wiki/Elementary_function)
