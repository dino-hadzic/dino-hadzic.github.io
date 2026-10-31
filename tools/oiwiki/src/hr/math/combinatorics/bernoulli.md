---
title: Bernoullijevi brojevi
---

Bernoullijevi brojevi $B_n$ niz su racionalnih brojeva usko povezan s teorijom brojeva. Prvih nekoliko otkrivenih Bernoullijevih brojeva jesu:

$B_0=1,B_1=-\frac{1}{2},B_2=\frac{1}{6},B_3=0,B_4=-\frac{1}{30},\dots$

## Zbrojevi jednakih potencija

Bernoullijevi brojevi nazvani su po Jacobu Bernoulliju, koji je proučavajući formule za zbroj $m$-tih potencija otkrio zanimljivu vezu. Označimo

$$
S_{m}(n)=\sum_{k=0}^{n-1}k^m=0^m+1^m+\dots+(n-1)^m
$$

Bernoulli je promatrao sljedeći niz formula i u njemu uočio obrazac:

$$
\begin{aligned}
S_0(n)&=n\\
S_1(n)&=\frac{1}{2}n^2-\frac{1}{2}n\\
S_2(n)&=\frac{1}{3}n^3-\frac{1}{2}n^2+\frac{1}{6}n\\
S_3(n)&=\frac{1}{4}n^4-\frac{1}{2}n^3+\frac{1}{4}n^2\\
S_4(n)&=\frac{1}{5}n^5-\frac{1}{2}n^4+\frac{1}{3}n^3-\frac{1}{30}n
\end{aligned}
$$

Može se uočiti da je u $S_m(n)$ koeficijent uz $n^{m+1}$ uvijek $\frac{1}{m+1}$, koeficijent uz $n^m$ uvijek je $-\frac{1}{2}$, koeficijent uz $n^{m-1}$ uvijek je $\frac{m}{12}$, koeficijent uz $n^{m-3}$ jest $-\frac{m(m-1)(m-2)}{720}$, koeficijent uz $n^{m-4}$ uvijek je nula itd.

Koeficijent uz $n^{m-k}$ uvijek je neka konstanta pomnožena s $m^{\underline{k}}$, pri čemu $m^{\underline{k}}$ označava padajuću faktorijelnu potenciju, tj. $\frac{m!}{(m-k)!}$.

## Rekurzivna formula

$$
\begin{aligned}
S_m{(n)}&=\frac{1}{m+1}(B_0n^{m+1}+\binom{m+1}{1}B_1 n^m+\dots+\binom{m+1}{m}B_m n) \\
&=\frac{1}{m+1}\sum_{k=0}^{m}\binom{m+1}{k}B_kn^{m+1-k}
\end{aligned}
$$

Bernoullijevi brojevi definirani su implicitnom rekurzivnom relacijom:

$$
\begin{aligned}
\sum_{j=0}^{m}\binom{m+1}{j}B_j&=0,(m>0)\\
B_0&=1
\end{aligned}
$$

Na primjer, $\binom{2}{0}B_0+\binom{2}{1}B_1=0$; prvih nekoliko vrijednosti očito je

|  $n$  | $0$ |       $1$      |      $2$      | $3$ |       $4$       | $5$ |       $6$      | $7$ |       $8$       | $\dots$ |
| :---: | :-: | :------------: | :-----------: | :-: | :-------------: | :-: | :------------: | :-: | :-------------: | :-----: |
| $B_n$ | $1$ | $-\frac{1}{2}$ | $\frac{1}{6}$ | $0$ | $-\frac{1}{30}$ | $0$ | $\frac{1}{42}$ | $0$ | $-\frac{1}{30}$ | $\dots$ |

### Dokaz

#### Dokaz indukcijom

Ovaj dokaz potječe iz knjige Concrete Mathematics, odjeljak 6.5 BERNOULLI NUMBER.

Dokazujemo pomoću identiteta za binomne koeficijente i matematičke indukcije:

$$
\begin{aligned}
S_{m+1}(n)+n^{m+1}&= \sum_{k=0}^{n-1}(k+1)^{m+1}\\
&=\sum_{k=0}^{n-1}\sum_{j=0}^{m+1}\binom{m+1}{j}k^j\\
&=\sum_{j=0}^{m+1}\binom{m+1}{j}S_j(n)
\end{aligned}
$$

Neka je $\hat{S}_{m}(n)=\frac{1}{m+1} \sum_{k=0}^{m} \binom{m+1}{k}B_kn^{m+1-k}$. Želimo dokazati da je $S_m(n)=\hat{S}_m(n)$; pretpostavimo da za $j\in[0,m)$ vrijedi $S_j(n)=\hat{S}_j(n)$.

Oduzmemo li $S_{m+1}(n)$ s obje strane izvorne jednakosti, dobivamo:

$$
\begin{aligned}
S_{m+1}(n)+n^{m+1}&=\sum_{j=0}^{m+1}\binom{m+1}{j}S_j(n)\\
n^{m+1}&=\sum_{j=0}^{m}\binom{m+1}{j}S_j(n)\\
&=\sum_{j=0}^{m-1}\binom{m+1}{j}\hat{S}_j(n)+\binom{m+1}{m}S_m(n)
\end{aligned}
$$

Pokušajmo na desnu stranu izraza dodati $\binom{m+1}{m}\hat{S}_m(n)-\binom{m+1}{m}\hat{S}_m(n)$ i zatim pojednostavniti; dobivamo:

$$
n^{m+1}=\sum_{j=0}^{m}\binom{m+1}{j}\hat{S}_j(n)+(m+1)(S_m(n)-\hat{S}_m(n))
$$

Neka je $\Delta = S_m(n)-\hat{S}_m(n)$; raspišemo li $\hat{S}_j(n)$, imamo

$$
\begin{aligned}
n^{m+1}&=\sum_{j=0}^{m}\binom{m+1}{j}\hat{S}_j(n)+(m+1)\Delta\\
&=\sum_{j=0}^{m}\binom{m+1}{j}\frac{1}{j+1}\sum_{k=0}^{j}\binom{j+1}{k}B_kn^{j+1-k}+(m+1)\Delta\\
\end{aligned}
$$

Obrnemo li redoslijed zbrajanja u drugoj sumi $\sum$ i zatim identično preoblikujemo zapis binomnih koeficijenata, dobivamo:

$$
\begin{aligned}
n^{m+1}&=\sum_{j=0}^{m}\binom{m+1}{j}\frac{1}{j+1}\sum_{k=0}^{j}\binom{j+1}{j-k}B_{j-k}n^{k+1}+(m+1)\Delta\\
&=\sum_{j=0}^{m}\binom{m+1}{j}\frac{1}{j+1}\sum_{k=0}^{j}\binom{j+1}{k+1}B_{j-k}n^{k+1}+(m+1)\Delta\\
&=\sum_{j=0}^{m}\binom{m+1}{j}\frac{1}{j+1}\sum_{k=0}^{j}\frac{j+1}{k+1}\binom{j}{k}B_{j-k}n^{k+1}+(m+1)\Delta\\
&=\sum_{j=0}^{m}\binom{m+1}{j}\sum_{k=0}^{j}\binom{j}{k}\frac{B_{j-k}}{k+1}n^{k+1}+(m+1)\Delta
\end{aligned}
$$

Zamjenom redoslijeda dvaju znakova zbrajanja dobivamo:

$$
n^{m+1}=\sum_{k=0}^{m}\frac{n^{k+1}}{k+1}\sum_{j=k}^{m}\binom{m+1}{j}\binom{j}{k}B_{j-k}+(m+1)\Delta
$$

Identično preoblikujemo $\binom{m+1}{j}\binom{j}{k}$:

$$
\binom{m+1}{j}\binom{j}{k}＝\binom{m+1}{k}\binom{m-k+1}{j-k}
$$

Tada izraz postaje:

$$
\begin{aligned}
n^{m+1}&=\sum_{k=0}^{m}\frac{n^{k+1}}{k+1}\sum_{j=k}^{m}\binom{m+1}{k}\binom{m-k+1}{j-k}B_{j-k}+(m+1)\Delta\\
&=\sum_{k=0}^{m}\frac{n^{k+1}}{k+1}\binom{m+1}{k}\sum_{j=k}^{m}\binom{m-k+1}{j-k}B_{j-k}+(m+1)\Delta\\
\end{aligned}
$$

Zamijenimo li svako $j-k$ s $j$, dobivamo:

$$
n^{m+1}=\sum_{k=0}^{m}\frac{n^{k+1}}{k+1}\binom{m+1}{k}\sum_{j=0}^{m-k}\binom{m-k+1}{j}B_{j}+(m+1)\Delta
$$

Razmotrimo rekurzivnu relaciju koju smo ranije spomenuli

$$
\begin{aligned}
\sum_{j=0}^{m}\binom{m+1}{j}B_j&=0,(m>0)\\
B_0&=1\\
\sum_{j=0}^{m}\binom{m+1}{j}B_j&=[m = 0]
\end{aligned}
$$

Uvrštavanjem dobivamo:

$$
\begin{aligned}
n^{m+1}&=\sum_{k=0}^{m}\frac{n^{k+1}}{k+1}\binom{m+1}{k}[m - k = 0]+(m+1)\Delta\\
&=\frac{n^{m+1}}{m+1}\binom{m+1}{m}+(m+1)\Delta\\
&=n^{m+1}+(m+1)\Delta
\end{aligned}
$$

Dakle $\Delta=0$ i vrijedi $S_m(n)=\hat{S}_m(n)$.

#### Dokaz eksponencijalnom funkcijom izvodnicom

Rekurzivnoj relaciji $\sum_{j=0}^{m}\binom{m+1}{j}B_j=[m=0]$

dodamo $B_{m + 1}$ s obje strane i dobivamo:

$$
\begin{aligned}
\sum_{j=0}^{m+1}\binom{m+1}{j}B_j&=[m=0]+B_{m+1}\\
\sum_{j=0}^{m}\binom{m}{j}B_j&=[m=1]+B_{m}\\
\sum_{j=0}^{m}\dfrac{B_j}{j!}\cdot\dfrac{1}{(m-j)!}&=[m=1]+\dfrac{B_{m}}{m!}
\end{aligned}
$$

Neka je $B(z) = \sum\limits_{i\ge 0}\dfrac{B_i}{i!}z^i$. Uočimo da je lijeva strana oblika konvolucije, pa:

$$
\begin{aligned}
B(z)\mathrm{e}^z &= z+B(z)\\
B(z)&=\dfrac{z}{\mathrm{e}^z - 1}
\end{aligned}
$$

Neka je $F_n(z) = \sum_{m\ge 0}\dfrac{S_m(n)}{m!}z^m$; tada:

$$
\begin{aligned}
F_n(z) &= \sum_{m\ge 0}\dfrac{S_m(n)}{m!}z^m\\
&= \sum_{m\ge 0}\sum_{i=0}^{n-1}\dfrac{i^mz^m}{m!}\\
\end{aligned}
$$

Zamijenimo redoslijed zbrajanja:

$$
\begin{aligned}
F_n(z) &=\sum_{i=0}^{n-1}\sum_{m\ge 0}\dfrac{i^mz^m}{m!}\\
       &=\sum_{i=0}^{n-1}\mathrm{e}^{iz}\\
       &=\dfrac{\mathrm{e}^{nz} - 1}{\mathrm{e}^z - 1}\\
       &=\dfrac{z}{\mathrm{e}^z - 1}\cdot\dfrac{\mathrm{e}^{nz} - 1}{z}
\end{aligned}
$$

Uvrstimo $B(z)=\dfrac{z}{\mathrm{e}^z - 1}$:

$$
\begin{aligned}
F_n(z) &= B(z)\cdot\dfrac{\mathrm{e}^{nz} - 1}{z}\\
&= \left(\sum_{i\ge 0}\dfrac{B_i}{i!} \right)\left(\sum_{i\ge 1}\dfrac{n^i z^{i - 1}}{i!}\right)\\
&= \left(\sum_{i\ge 0}\dfrac{B_i}{i!} \right)\left(\sum_{i\ge 0}\dfrac{n^{i+1} z^{i}}{(i+1)!}\right)
\end{aligned}
$$

Budući da je $F_n(z) = \sum_{m\ge 0}\dfrac{S_m(n)}{m!}z^m$, tj. $S_m(n)=m![z^m]F_n(z)$:

$$
\begin{aligned}
S \times m(n)&=m![z^m]F_n(z)\\
             &= m!\sum_{i=0}^{m}\dfrac{B \times i}{i!}\cdot\dfrac{n^{m-i+1}}{(m-i+1)!}\\
             &=\dfrac{1}{m+1}\sum_{i=0}^{m}\binom{m+1}{i}B_in^{m-i+1}
\end{aligned}
$$

Time je tvrdnja dokazana.

??? note "Referentna implementacija"
    ```cpp
    using ll = long long;
    constexpr int MAXN = 10000;
    constexpr int mod = 1e9 + 7;
    ll B[MAXN];        // Bernoullijevi brojevi
    ll C[MAXN][MAXN];  // binomni koeficijenti
    ll inv[MAXN];      // inverzi (za računanje Bernoullijevih brojeva)
    
    void init() {
      // predračun binomnih koeficijenata
      for (int i = 0; i < MAXN; i++) {
        C[i][0] = C[i][i] = 1;
        for (int k = 1; k < i; k++) {
          C[i][k] = (C[i - 1][k] % mod + C[i - 1][k - 1] % mod) % mod;
        }
      }
      // predračun inverza
      inv[1] = 1;
      for (int i = 2; i < MAXN; i++) {
        inv[i] = (mod - mod / i) * inv[mod % i] % mod;
      }
      // predračun Bernoullijevih brojeva
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
