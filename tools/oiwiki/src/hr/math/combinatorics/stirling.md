---
title: Stirlingovi brojevi
---

## Stirlingovi brojevi druge vrste (Stirling Number)

??? note "Zašto prvo uvodimo Stirlingove brojeve druge vrste"
    Iako se zovu „druge vrste”, Stirlingovi brojevi druge vrste prvi su opisani u Stirlingovim radovima i u knjizi Concrete Mathematics, a ujedno se koriste znatno češće od Stirlingovih brojeva prve vrste.

**Stirlingovi brojevi druge vrste** (Stirlingovi brojevi podskupova) $\begin{Bmatrix}n\\ k\end{Bmatrix}$, koji se zapisuju i kao $S(n,k)$, označavaju broj načina da se $n$ međusobno različitih elemenata rastavi na $k$ nerazlučivih nepraznih podskupova.

### Rekurzivna relacija

$$
\begin{Bmatrix}n\\ k\end{Bmatrix}=\begin{Bmatrix}n-1\\ k-1\end{Bmatrix}+k\begin{Bmatrix}n-1\\ k\end{Bmatrix}
$$

Rubni je uvjet $\begin{Bmatrix}n\\ 0\end{Bmatrix}=[n=0]$.

Dokažimo to kombinatornom interpretacijom.

Pri umetanju novog elementa postoje dvije mogućnosti:

-   novi element stavimo sam u zaseban podskup, za što postoji $\begin{Bmatrix}n-1\\ k-1\end{Bmatrix}$ načina;
-   novi element stavimo u jedan od postojećih nepraznih podskupova, za što postoji $k\begin{Bmatrix}n-1\\ k\end{Bmatrix}$ načina.

Prema principu zbroja, zbrajanjem tih dvaju izraza dobivamo rekurzivnu relaciju.

### Eksplicitna formula

$$
\begin{Bmatrix}n\\m\end{Bmatrix}=\sum\limits_{i=0}^m\dfrac{(-1)^{m-i}i^n}{i!(m-i)!}
$$

Formulu dokazujemo formulom uključivanja-isključivanja. Neka je $G_i$ broj načina da se $n$ međusobno različitih elemenata rasporedi u $i$ međusobno različitih skupova (prazni skupovi dopušteni), a $F_i$ broj načina da se $n$ međusobno različitih elemenata rasporedi u $i$ međusobno različitih nepraznih skupova (prazni skupovi nisu dopušteni).

Očito je

$$
\begin{aligned}
G_i&=i^n\\
G_i&=\sum\limits_{j=0}^i\binom{i}{j}F_j
\end{aligned}
$$

Prema binomnoj inverziji

$$
\begin{aligned}
F_i&=\sum\limits_{j=0}^{i}(-1)^{i-j}\binom{i}{j}G_j\\
&=\sum\limits_{j=0}^{i}(-1)^{i-j}\binom{i}{j}j^n\\
&=\sum\limits_{j=0}^{i}\dfrac{i!(-1)^{i-j}j^n}{j!(i-j)!}
\end{aligned}
$$

Promotrimo vezu između $F_i$ i $\begin{Bmatrix}n\\i\end{Bmatrix}$. Kod Stirlingovih brojeva druge vrste skupovi se međusobno ne razlikuju, pa je $F_i$ točno $i!$ puta veći od $\begin{Bmatrix}n\\i\end{Bmatrix}$. Stoga je

$$
\begin{Bmatrix}n\\m\end{Bmatrix}=\dfrac{F_m}{m!}=\sum\limits_{i=0}^m\dfrac{(-1)^{m-i}i^n}{i!(m-i)!}
$$

### Računanje Stirlingovih brojeva druge vrste u istom retku

Stirlingovi brojevi druge vrste „u istom retku” niz su brojeva $\begin{Bmatrix}n\\i\end{Bmatrix}$ s različitim $i$ i jednakim $n$. Izračunati sve Stirlingove brojeve druge vrste u istom retku znači za $i=0..n$ odrediti broj načina da se $n$ različitih elemenata rastavi na $i$ nepraznih skupova.

Prema gore navedenoj eksplicitnoj formuli to se računa konvolucijom. Vremenska složenost tog postupka je $O(n \log n)$.

Kôd u nastavku koristi klasu polinoma pod imenom `poly` i služi samo kao referenca.

??? note "Implementacija"
    ```cpp
    #ifndef _FEISTDLIB_POLY_
    #define _FEISTDLIB_POLY_
    
    /*
     * This file is part of the fstdlib project.
     * Version: Build v0.0.2
     * You can check for details at https://github.com/FNatsuka/fstdlib
     */
    
    #include <algorithm>
    #include <cmath>
    #include <cstdio>
    #include <vector>
    
    namespace fstdlib {
    
    using ll = long long;
    int mod = 998244353, grt = 3;
    
    class poly {
     private:
      std::vector<int> data;
    
      void out(void) {
        for (int i = 0; i < (int)data.size(); ++i) printf("%d ", data[i]);
        puts("");
      }
    
     public:
      poly(std::size_t len = std::size_t(0)) { data = std::vector<int>(len); }
    
      poly(const std::vector<int> &b) { data = b; }
    
      poly(const poly &b) { data = b.data; }
    
      void resize(std::size_t len, int val = 0) { data.resize(len, val); }
    
      std::size_t size(void) const { return data.size(); }
    
      void clear(void) { data.clear(); }
    #if __cplusplus >= 201103L
      void shrink_to_fit(void) { data.shrink_to_fit(); }
    #endif
      int &operator[](std::size_t b) { return data[b]; }
    
      const int &operator[](std::size_t b) const { return data[b]; }
    
      poly operator*(const poly &h) const;
      poly operator*=(const poly &h);
      poly operator*(const int &h) const;
      poly operator*=(const int &h);
      poly operator+(const poly &h) const;
      poly operator+=(const poly &h);
      poly operator-(const poly &h) const;
      poly operator-=(const poly &h);
      poly operator<<(const std::size_t &b) const;
      poly operator<<=(const std::size_t &b);
      poly operator>>(const std::size_t &b) const;
      poly operator>>=(const std::size_t &b);
      poly operator/(const int &h) const;
      poly operator/=(const int &h);
      poly operator==(const poly &h) const;
      poly operator!=(const poly &h) const;
      poly operator+(const int &h) const;
      poly operator+=(const int &h);
      poly inv(void) const;
      poly inv(const int &h) const;
      friend poly sqrt(const poly &h);
      friend poly log(const poly &h);
      friend poly exp(const poly &h);
    };
    
    int qpow(int a, int b, int p = mod) {
      int res = 1;
      while (b) {
        if (b & 1) res = (ll)res * a % p;
        a = (ll)a * a % p, b >>= 1;
      }
      return res;
    }
    
    std::vector<int> rev;
    
    void dft_for_module(std::vector<int> &f, int n, int b) {
      static std::vector<int> w;
      w.resize(n);
      for (int i = 0; i < n; ++i)
        if (i < rev[i]) std::swap(f[i], f[rev[i]]);
      for (int i = 2; i <= n; i <<= 1) {
        w[0] = 1, w[1] = qpow(grt, (mod - 1) / i);
        if (b == -1) w[1] = qpow(w[1], mod - 2);
        for (int j = 2; j < i / 2; ++j) w[j] = (ll)w[j - 1] * w[1] % mod;
        for (int j = 0; j < n; j += i)
          for (int k = 0; k < i / 2; ++k) {
            int p = f[j + k], q = (ll)f[j + k + i / 2] * w[k] % mod;
            f[j + k] = (p + q) % mod, f[j + k + i / 2] = (p - q + mod) % mod;
          }
      }
    }
    
    poly poly::operator*(const poly &h) const {
      int N = 1;
      while (N < (int)(size() + h.size() - 1)) N <<= 1;
      std::vector<int> f(this->data), g(h.data);
      f.resize(N), g.resize(N);
      rev.resize(N);
      for (int i = 0; i < N; ++i)
        rev[i] = (rev[i >> 1] >> 1) | (i & 1 ? N >> 1 : 0);
      dft_for_module(f, N, 1), dft_for_module(g, N, 1);
      for (int i = 0; i < N; ++i) f[i] = (ll)f[i] * g[i] % mod;
      dft_for_module(f, N, -1), f.resize(size() + h.size() - 1);
      for (int i = 0, inv = qpow(N, mod - 2); i < (int)f.size(); ++i)
        f[i] = (ll)f[i] * inv % mod;
      return f;
    }
    
    poly poly::operator*=(const poly &h) { return *this = *this * h; }
    
    poly poly::operator*(const int &h) const {
      std::vector<int> f(this->data);
      for (int i = 0; i < (int)f.size(); ++i) f[i] = (ll)f[i] * h % mod;
      return f;
    }
    
    poly poly::operator*=(const int &h) {
      for (int i = 0; i < (int)size(); ++i) data[i] = (ll)data[i] * h % mod;
      return *this;
    }
    
    poly poly::operator+(const poly &h) const {
      std::vector<int> f(this->data);
      if (f.size() < h.size()) f.resize(h.size());
      for (int i = 0; i < (int)h.size(); ++i) f[i] = (f[i] + h[i]) % mod;
      return f;
    }
    
    poly poly::operator+=(const poly &h) {
      std::vector<int> &f = this->data;
      if (f.size() < h.size()) f.resize(h.size());
      for (int i = 0; i < (int)h.size(); ++i) f[i] = (f[i] + h[i]) % mod;
      return f;
    }
    
    poly poly::operator-(const poly &h) const {
      std::vector<int> f(this->data);
      if (f.size() < h.size()) f.resize(h.size());
      for (int i = 0; i < (int)h.size(); ++i) f[i] = (f[i] - h[i] + mod) % mod;
      return f;
    }
    
    poly poly::operator-=(const poly &h) {
      std::vector<int> &f = this->data;
      if (f.size() < h.size()) f.resize(h.size());
      for (int i = 0; i < (int)h.size(); ++i) f[i] = (f[i] - h[i] + mod) % mod;
      return f;
    }
    
    poly poly::operator<<(const std::size_t &b) const {
      std::vector<int> f(size() + b);
      for (int i = 0; i < (int)size(); ++i) f[i + b] = data[i];
      return f;
    }
    
    poly poly::operator<<=(const std::size_t &b) { return *this = (*this) << b; }
    
    poly poly::operator>>(const std::size_t &b) const {
      std::vector<int> f(size() - b);
      for (int i = 0; i < (int)f.size(); ++i) f[i] = data[i + b];
      return f;
    }
    
    poly poly::operator>>=(const std::size_t &b) { return *this = (*this) >> b; }
    
    poly poly::operator/(const int &h) const {
      std::vector<int> f(this->data);
      int inv = qpow(h, mod - 2);
      for (int i = 0; i < (int)f.size(); ++i) f[i] = (ll)f[i] * inv % mod;
      return f;
    }
    
    poly poly::operator/=(const int &h) {
      int inv = qpow(h, mod - 2);
      for (int i = 0; i < (int)data.size(); ++i) data[i] = (ll)data[i] * inv % mod;
      return *this;
    }
    
    poly poly::inv(void) const {
      int N = 1;
      while (N < (int)(size() + size() - 1)) N <<= 1;
      std::vector<int> f(N), g(N), d(this->data);
      d.resize(N), f[0] = qpow(d[0], mod - 2);
      for (int w = 2; w < N; w <<= 1) {
        for (int i = 0; i < w; ++i) g[i] = d[i];
        rev.resize(w << 1);
        for (int i = 0; i < w * 2; ++i)
          rev[i] = (rev[i >> 1] >> 1) | (i & 1 ? w : 0);
        dft_for_module(f, w << 1, 1), dft_for_module(g, w << 1, 1);
        for (int i = 0; i < w * 2; ++i)
          f[i] = (ll)f[i] * (2 + mod - (ll)f[i] * g[i] % mod) % mod;
        dft_for_module(f, w << 1, -1);
        for (int i = 0, inv = qpow(w << 1, mod - 2); i < w; ++i)
          f[i] = (ll)f[i] * inv % mod;
        for (int i = w; i < w * 2; ++i) f[i] = 0;
      }
      f.resize(size());
      return f;
    }
    
    poly poly::operator==(const poly &h) const {
      if (size() != h.size()) return 0;
      for (int i = 0; i < (int)size(); ++i)
        if (data[i] != h[i]) return 0;
      return 1;
    }
    
    poly poly::operator!=(const poly &h) const {
      if (size() != h.size()) return 1;
      for (int i = 0; i < (int)size(); ++i)
        if (data[i] != h[i]) return 1;
      return 0;
    }
    
    poly poly::operator+(const int &h) const {
      poly f(this->data);
      f[0] = (f[0] + h) % mod;
      return f;
    }
    
    poly poly::operator+=(const int &h) { return *this = (*this) + h; }
    
    poly poly::inv(const int &h) const {
      poly f(*this);
      f.resize(h);
      return f.inv();
    }
    
    int modsqrt(int h, int p = mod) { return 1; }
    
    poly sqrt(const poly &h) {
      int N = 1;
      while (N < (int)(h.size() + h.size() - 1)) N <<= 1;
      poly f(N), g(N), d(h);
      d.resize(N), f[0] = modsqrt(d[0]);
      for (int w = 2; w < N; w <<= 1) {
        g.resize(w);
        for (int i = 0; i < w; ++i) g[i] = d[i];
        f = (f + f.inv(w) * g) / 2;
        f.resize(w);
      }
      f.resize(h.size());
      return f;
    }
    
    poly log(const poly &h) {
      poly f(h);
      for (int i = 1; i < (int)f.size(); ++i) f[i - 1] = (ll)f[i] * i % mod;
      f[f.size() - 1] = 0, f = f * h.inv(), f.resize(h.size());
      for (int i = (int)f.size() - 1; i > 0; --i)
        f[i] = (ll)f[i - 1] * qpow(i, mod - 2) % mod;
      f[0] = 0;
      return f;
    }
    
    poly exp(const poly &h) {
      int N = 1;
      while (N < (int)(h.size() + h.size() - 1)) N <<= 1;
      poly f(N), g(N), d(h);
      f[0] = 1, d.resize(N);
      for (int w = 2; w < N; w <<= 1) {
        f.resize(w), g.resize(w);
        for (int i = 0; i < w; ++i) g[i] = d[i];
        f = f * (g + 1 - log(f));
        f.resize(w);
      }
      f.resize(h.size());
      return f;
    }
    
    struct comp {
      long double x, y;
    
      comp(long double _x = 0, long double _y = 0) : x(_x), y(_y) {}
    
      comp operator*(const comp &b) const {
        return comp(x * b.x - y * b.y, x * b.y + y * b.x);
      }
    
      comp operator+(const comp &b) const { return comp(x + b.x, y + b.y); }
    
      comp operator-(const comp &b) const { return comp(x - b.x, y - b.y); }
    
      comp conj(void) { return comp(x, -y); }
    };
    
    const int EPS = 1e-9;
    
    template <typename FLOAT_T>
    FLOAT_T fabs(const FLOAT_T &x) {
      return x > 0 ? x : -x;
    }
    
    template <typename FLOAT_T>
    FLOAT_T sin(const FLOAT_T &x, const long double &EPS = fstdlib::EPS) {
      FLOAT_T res = 0, delt = x;
      int d = 0;
      while (fabs(delt) > EPS) {
        res += delt, ++d;
        delt *= -x * x / ((2 * d) * (2 * d + 1));
      }
      return res;
    }
    
    template <typename FLOAT_T>
    FLOAT_T cos(const FLOAT_T &x, const long double &EPS = fstdlib::EPS) {
      FLOAT_T res = 0, delt = 1;
      int d = 0;
      while (fabs(delt) > EPS) {
        res += delt, ++d;
        delt *= -x * x / ((2 * d) * (2 * d - 1));
      }
      return res;
    }
    
    const long double PI = std::acos((long double)(-1));
    
    void dft_for_complex(std::vector<comp> &f, int n, int b) {
      static std::vector<comp> w;
      w.resize(n);
      for (int i = 0; i < n; ++i)
        if (i < rev[i]) std::swap(f[i], f[rev[i]]);
      for (int i = 2; i <= n; i <<= 1) {
        w[0] = comp(1, 0), w[1] = comp(cos(2 * PI / i), b * sin(2 * PI / i));
        for (int j = 2; j < i / 2; ++j) w[j] = w[j - 1] * w[1];
        for (int j = 0; j < n; j += i)
          for (int k = 0; k < i / 2; ++k) {
            comp p = f[j + k], q = f[j + k + i / 2] * w[k];
            f[j + k] = p + q, f[j + k + i / 2] = p - q;
          }
      }
    }
    
    class arbitrary_module_poly {
     private:
      std::vector<int> data;
    
      int construct_element(int D, ll x, ll y, ll z) const {
        x %= mod, y %= mod, z %= mod;
        return ((ll)D * D * x % mod + (ll)D * y % mod + z) % mod;
      }
    
     public:
      int mod;
    
      arbitrary_module_poly(std::size_t len = std::size_t(0),
                            int module_value = 1e9 + 7) {
        mod = module_value;
        data = std::vector<int>(len);
      }
    
      arbitrary_module_poly(const std::vector<int> &b, int module_value = 1e9 + 7) {
        mod = module_value;
        data = b;
      }
    
      arbitrary_module_poly(const arbitrary_module_poly &b) {
        mod = b.mod;
        data = b.data;
      }
    
      void resize(std::size_t len, const int &val = 0) { data.resize(len, val); }
    
      std::size_t size(void) const { return data.size(); }
    
      void clear(void) { data.clear(); }
    #if __cplusplus >= 201103L
      void shrink_to_fit(void) { data.shrink_to_fit(); }
    #endif
      int &operator[](std::size_t b) { return data[b]; }
    
      const int &operator[](std::size_t b) const { return data[b]; }
    
      arbitrary_module_poly operator*(const arbitrary_module_poly &h) const;
      arbitrary_module_poly operator*=(const arbitrary_module_poly &h);
      arbitrary_module_poly operator*(const int &h) const;
      arbitrary_module_poly operator*=(const int &h);
      arbitrary_module_poly operator+(const arbitrary_module_poly &h) const;
      arbitrary_module_poly operator+=(const arbitrary_module_poly &h);
      arbitrary_module_poly operator-(const arbitrary_module_poly &h) const;
      arbitrary_module_poly operator-=(const arbitrary_module_poly &h);
      arbitrary_module_poly operator<<(const std::size_t &b) const;
      arbitrary_module_poly operator<<=(const std::size_t &b);
      arbitrary_module_poly operator>>(const std::size_t &b) const;
      arbitrary_module_poly operator>>=(const std::size_t &b);
      arbitrary_module_poly operator/(const int &h) const;
      arbitrary_module_poly operator/=(const int &h);
      arbitrary_module_poly operator==(const arbitrary_module_poly &h) const;
      arbitrary_module_poly operator!=(const arbitrary_module_poly &h) const;
      arbitrary_module_poly inv(void) const;
      arbitrary_module_poly inv(const int &h) const;
      friend arbitrary_module_poly sqrt(const arbitrary_module_poly &h);
      friend arbitrary_module_poly log(const arbitrary_module_poly &h);
    };
    
    arbitrary_module_poly arbitrary_module_poly::operator*(
        const arbitrary_module_poly &h) const {
      int N = 1;
      while (N < (int)(size() + h.size() - 1)) N <<= 1;
      std::vector<comp> f(N), g(N), p(N), q(N);
      const int D = std::sqrt(mod);
      for (int i = 0; i < (int)size(); ++i)
        f[i].x = data[i] / D, f[i].y = data[i] % D;
      for (int i = 0; i < (int)h.size(); ++i) g[i].x = h[i] / D, g[i].y = h[i] % D;
      rev.resize(N);
      for (int i = 0; i < N; ++i)
        rev[i] = (rev[i >> 1] >> 1) | (i & 1 ? N >> 1 : 0);
      dft_for_complex(f, N, 1), dft_for_complex(g, N, 1);
      for (int i = 0; i < N; ++i) {
        p[i] = (f[i] + f[(N - i) % N].conj()) * comp(0.50, 0) * g[i];
        q[i] = (f[i] - f[(N - i) % N].conj()) * comp(0, -0.5) * g[i];
      }
      dft_for_complex(p, N, -1), dft_for_complex(q, N, -1);
      std::vector<int> r(size() + h.size() - 1);
      for (int i = 0; i < (int)r.size(); ++i)
        r[i] = construct_element(D, p[i].x / N + 0.5, (p[i].y + q[i].x) / N + 0.5,
                                 q[i].y / N + 0.5);
      return arbitrary_module_poly(r, mod);
    }
    
    arbitrary_module_poly arbitrary_module_poly::operator*=(
        const arbitrary_module_poly &h) {
      return *this = *this * h;
    }
    
    arbitrary_module_poly arbitrary_module_poly::operator*(const int &h) const {
      std::vector<int> f(this->data);
      for (int i = 0; i < (int)f.size(); ++i) f[i] = (ll)f[i] * h % mod;
      return arbitrary_module_poly(f, mod);
    }
    
    arbitrary_module_poly arbitrary_module_poly::operator*=(const int &h) {
      for (int i = 0; i < (int)size(); ++i) data[i] = (ll)data[i] * h % mod;
      return *this;
    }
    
    arbitrary_module_poly arbitrary_module_poly::operator+(
        const arbitrary_module_poly &h) const {
      std::vector<int> f(this->data);
      if (f.size() < h.size()) f.resize(h.size());
      for (int i = 0; i < (int)h.size(); ++i) f[i] = (f[i] + h[i]) % mod;
      return arbitrary_module_poly(f, mod);
    }
    
    arbitrary_module_poly arbitrary_module_poly::operator+=(
        const arbitrary_module_poly &h) {
      if (size() < h.size()) resize(h.size());
      for (int i = 0; i < (int)h.size(); ++i) data[i] = (data[i] + h[i]) % mod;
      return *this;
    }
    
    arbitrary_module_poly arbitrary_module_poly::operator-(
        const arbitrary_module_poly &h) const {
      std::vector<int> f(this->data);
      if (f.size() < h.size()) f.resize(h.size());
      for (int i = 0; i < (int)h.size(); ++i) f[i] = (f[i] + mod - h[i]) % mod;
      return arbitrary_module_poly(f, mod);
    }
    
    arbitrary_module_poly arbitrary_module_poly::operator-=(
        const arbitrary_module_poly &h) {
      if (size() < h.size()) resize(h.size());
      for (int i = 0; i < (int)h.size(); ++i)
        data[i] = (data[i] + mod - h[i]) % mod;
      return *this;
    }
    
    arbitrary_module_poly arbitrary_module_poly::operator<<(
        const std::size_t &b) const {
      std::vector<int> f(size() + b);
      for (int i = 0; i < (int)size(); ++i) f[i + b] = data[i];
      return arbitrary_module_poly(f, mod);
    }
    
    arbitrary_module_poly arbitrary_module_poly::operator<<=(const std::size_t &b) {
      return *this = (*this) << b;
    }
    
    arbitrary_module_poly arbitrary_module_poly::operator>>(
        const std::size_t &b) const {
      std::vector<int> f(size() - b);
      for (int i = 0; i < (int)f.size(); ++i) f[i] = data[i + b];
      return arbitrary_module_poly(f, mod);
    }
    
    arbitrary_module_poly arbitrary_module_poly::operator>>=(const std::size_t &b) {
      return *this = (*this) >> b;
    }
    
    arbitrary_module_poly arbitrary_module_poly::inv(void) const {
      int N = 1;
      while (N < (int)(size() + size() - 1)) N <<= 1;
      arbitrary_module_poly f(1, mod), g(N, mod), h(*this), f2(1, mod);
      f[0] = qpow(data[0], mod - 2, mod), h.resize(N), f2[0] = 2;
      for (int w = 2; w < N; w <<= 1) {
        g.resize(w);
        for (int i = 0; i < w; ++i) g[i] = h[i];
        f = f * (f * g - f2) * (mod - 1);
        f.resize(w);
      }
      f.resize(size());
      return f;
    }
    
    arbitrary_module_poly arbitrary_module_poly::inv(const int &h) const {
      arbitrary_module_poly f(*this);
      f.resize(h);
      return f.inv();
    }
    
    arbitrary_module_poly arbitrary_module_poly::operator/(const int &h) const {
      int inv = qpow(h, mod - 2, mod);
      std::vector<int> f(this->data);
      for (int i = 0; i < (int)f.size(); ++i) f[i] = (ll)f[i] * inv % mod;
      return arbitrary_module_poly(f, mod);
    }
    
    arbitrary_module_poly arbitrary_module_poly::operator/=(const int &h) {
      int inv = qpow(h, mod - 2, mod);
      for (int i = 0; i < (int)size(); ++i) data[i] = (ll)data[i] * inv % mod;
      return *this;
    }
    
    arbitrary_module_poly arbitrary_module_poly::operator==(
        const arbitrary_module_poly &h) const {
      if (size() != h.size() || mod != h.mod) return 0;
      for (int i = 0; i < (int)size(); ++i)
        if (data[i] != h[i]) return 0;
      return 1;
    }
    
    arbitrary_module_poly arbitrary_module_poly::operator!=(
        const arbitrary_module_poly &h) const {
      if (size() != h.size() || mod != h.mod) return 1;
      for (int i = 0; i < (int)size(); ++i)
        if (data[i] != h[i]) return 1;
      return 0;
    }
    
    arbitrary_module_poly sqrt(const arbitrary_module_poly &h) {
      int N = 1;
      while (N < (int)(h.size() + h.size() - 1)) N <<= 1;
      arbitrary_module_poly f(1, mod), g(N, mod), d(h);
      f[0] = modsqrt(h[0], mod), d.resize(N);
      for (int w = 2; w < N; w <<= 1) {
        g.resize(w);
        for (int i = 0; i < w; ++i) g[i] = d[i];
        f = (f + f.inv(w) * g) / 2;
        f.resize(w);
      }
      f.resize(h.size());
      return f;
    }
    
    arbitrary_module_poly log(const arbitrary_module_poly &h) {
      arbitrary_module_poly f(h);
      for (int i = 1; i < (int)f.size(); ++i) f[i - 1] = (ll)f[i] * i % f.mod;
      f[f.size() - 1] = 0, f = f * h.inv(), f.resize(h.size());
      for (int i = (int)f.size() - 1; i > 0; --i)
        f[i] = (ll)f[i - 1] * qpow(i, f.mod - 2, f.mod) % f.mod;
      f[0] = 0;
      return f;
    }
    
    using m_poly = arbitrary_module_poly;
    }  // namespace fstdlib
    
    #endif
    ```

???+ note "Implementacija"
    ```cpp
    int main() {
      scanf("%d", &n);
      fact[0] = 1;
      for (int i = 1; i <= n; ++i) fact[i] = (ll)fact[i - 1] * i % mod;
      exgcd(fact[n], mod, ifact[n], ifact[0]),
          ifact[n] = (ifact[n] % mod + mod) % mod;
      for (int i = n - 1; i >= 0; --i) ifact[i] = (ll)ifact[i + 1] * (i + 1) % mod;
      poly f(n + 1), g(n + 1);
      for (int i = 0; i <= n; ++i)
        g[i] = (i & 1 ? mod - 1ll : 1ll) * ifact[i] % mod,
        f[i] = (ll)qpow(i, n) * ifact[i] % mod;
      f *= g, f.resize(n + 1);
      for (int i = 0; i <= n; ++i) printf("%d ", f[i]);
      return 0;
    }
    ```

### Računanje Stirlingovih brojeva druge vrste u istom stupcu

Stirlingovi brojevi druge vrste „u istom stupcu” niz su brojeva $\begin{Bmatrix}i\\k\end{Bmatrix}$ s različitim $i$ i jednakim $k$. Izračunati sve Stirlingove brojeve druge vrste u istom stupcu znači za $i=0..n$ odrediti broj načina da se $i$ različitih elemenata rastavi na $k$ nepraznih skupova.

Računamo pomoću eksponencijalne funkcije izvodnice.

Broj načina da jedna kutija sadrži $i$ predmeta i pritom bude neprazna je $[i>0]$. Njegovu eksponencijalnu funkciju izvodnicu možemo zapisati kao $F(x)=\sum\limits_{i=1}^{+\infty}\dfrac{x^i}{i!} = \mathrm{e}^x-1$. Iz prethodno naučenog znamo da je $F^k(x)$ eksponencijalna funkcija izvodnica za raspoređivanje $i$ označenih predmeta u $k$ označenih kutija, pa je nakon dijeljenja s $k!$ to eksponencijalna funkcija izvodnica za raspoređivanje $i$ označenih predmeta u $k$ neoznačenih kutija.

$\begin{Bmatrix}i\\k\end{Bmatrix}=\dfrac{\left[\dfrac{x^i}{i!}\right]F^k(x)}{k!}$, pa je dovoljno u $O(n\log n)$ izračunati potenciju polinoma.

Osim toga, $\exp F(x)=\sum\limits_{i=0}^{+\infty}\dfrac{F^i(x)}{i!}$ eksponencijalna je funkcija izvodnica za raspoređivanje $i$ označenih predmeta u proizvoljno mnogo neoznačenih kutija (EXP dijeljenjem svakog člana s $i!$ uklanja oznake kutija). To je zapravo funkcija izvodnica Bellovih brojeva.

Ovdje se pojavljuje mnogo toga „označenog” i „neoznačenog”; pažljivo ih razlikujte.

???+ note "Implementacija"
    ```cpp
    int main() {
      scanf("%d%d", &n, &k);
      poly f(n + 1);
      fact[0] = 1;
      for (int i = 1; i <= n; ++i) fact[i] = (ll)fact[i - 1] * i % mod;
      for (int i = 1; i <= n; ++i) f[i] = qpow(fact[i], mod - 2);
      f = exp(log(f >> 1) * k) << k, f.resize(n + 1);
      int inv = qpow(fact[k], mod - 2);
      for (int i = 0; i <= n; ++i)
        printf("%lld ", (ll)f[i] * fact[i] % mod * inv % mod);
      return 0;
    }
    ```

## Stirlingovi brojevi prve vrste (Stirling Number)

**Stirlingovi brojevi prve vrste** (Stirlingovi brojevi ciklusa) $\begin{bmatrix}n\\ k\end{bmatrix}$, koji se zapisuju i kao $s(n,k)$, označavaju broj načina da se $n$ međusobno različitih elemenata rastavi na $k$ nerazlučivih nepraznih ciklusa.

Ciklus je kružni raspored u kojem je kraj spojen s početkom. Ciklus možemo zapisati kao $[A,B,C,D]$ i smatramo da je $[A,B,C,D]=[B,C,D,A]=[C,D,A,B]=[D,A,B,C]$, tj. dva ciklusa koja se mogu dobiti jedan iz drugoga rotacijom ekvivalentna su. Napomena: dva ciklusa koja se mogu dobiti jedan iz drugoga zrcaljenjem ne smatramo ekvivalentnima, tj. $[A,B,C,D]\neq[D,C,B,A]$.

### Rekurzivna relacija

$$
\begin{bmatrix}n\\ k\end{bmatrix}=\begin{bmatrix}n-1\\ k-1\end{bmatrix}+(n-1)\begin{bmatrix}n-1\\ k\end{bmatrix}
$$

Rubni je uvjet $\begin{bmatrix}n\\ 0\end{bmatrix}=[n=0]$.

Dokaz ove rekurzivne relacije možemo provesti preko njezine kombinatorne interpretacije.

Pri umetanju novog elementa postoje dvije mogućnosti:

-   novi element stavimo u zaseban ciklus, za što postoji ukupno $\begin{bmatrix}n-1\\ k-1\end{bmatrix}$ načina;
-   element umetnemo u bilo koji od postojećih ciklusa, za što postoji ukupno $(n-1)\begin{bmatrix}n-1\\ k\end{bmatrix}$ načina.

Prema principu zbroja, zbrajanjem tih dvaju izraza dobivamo rekurzivnu relaciju.

### Eksplicitna formula

Stirlingovi brojevi prve vrste nemaju praktičnu eksplicitnu formulu.

### Računanje Stirlingovih brojeva prve vrste u istom retku

Slično kao kod Stirlingovih brojeva druge vrste, konstruiramo funkciju izvodnicu Stirlingovih brojeva prve vrste u istom retku, tj.

$F_n(x)=\sum\limits_{i=0}^n\begin{bmatrix}n\\i\end{bmatrix}x^i$

Iz rekurzivne relacije lako se zapisuje

$F_n(x)=(n-1)F_{n-1}(x)+xF_{n-1}(x)$

pa je

$F_n(x)=\prod\limits_{i=0}^{n-1}(x+i)=\dfrac{(x+n-1)!}{(x-1)!}$

To je zapravo $n$-ta rastuća faktorijelna potencija od $x$, koja se zapisuje $x^{\overline n}$. Nju se, naravno, može izračunati grubom silom množenjem po načelu podijeli pa vladaj u $O(n\log^2n)$, ali metodama vezanima uz rastuće potencije može se izračunati u $O(n\log n)$; detalje vidi u [Pomak polinoma | Pomak uzastopnih vrijednosti u točkama](../poly/shift.md#stirlingovi-brojevi-prve-vrste-bez-predznaka-u-istom-retku).

### Računanje Stirlingovih brojeva prve vrste u istom stupcu

Po uzoru na računanje Stirlingovih brojeva druge vrste, problem možemo riješiti eksponencijalnom funkcijom izvodnicom. Napomena: budući da rekurzivna relacija ovisi o retku, njome ne možemo računati Stirlingove brojeve prve vrste u istom stupcu.

Očito je eksponencijalna funkcija izvodnica jednog ciklusa

$F(x)=\sum\limits_{i=1}^n\dfrac{(i-1)!x^i}{i!}=\sum\limits_{i=1}^n\dfrac{x^i}{i}$

Njezina $k$-ta potencija eksponencijalna je funkcija izvodnica za $\begin{bmatrix}i\\k\end{bmatrix}$, pa je dovoljno računati u $O(n\log n)$.

???+ note "Implementacija"
    ```cpp
    int main() {
      scanf("%d%d", &n, &k);
      fact[0] = 1;
      for (int i = 1; i <= n; ++i) fact[i] = (ll)fact[i - 1] * i % mod;
      ifact[n] = qpow(fact[n], mod - 2);
      for (int i = n - 1; i >= 0; --i) ifact[i] = (ll)ifact[i + 1] * (i + 1) % mod;
      poly f(n + 1);
      for (int i = 1; i <= n; ++i) f[i] = (ll)fact[i - 1] * ifact[i] % mod;
      f = exp(log(f >> 1) * k) << k, f.resize(n + 1);
      for (int i = 0; i <= n; ++i)
        printf("%lld ", (ll)f[i] * fact[i] % mod * ifact[k] % mod);
      return 0;
    }
    ```

## Primjene

### Pretvorba između rastućih potencija i običnih potencija

Rastuću faktorijelnu potenciju označavamo $x^{\overline{n}}=\prod_{k=0}^{n-1} (x+k)$.

Tada se rastuće potencije mogu pretvoriti u obične potencije sljedećim identitetom:

$$
x^{\overline{n}}=\sum_{k} \begin{bmatrix}n\\ k\end{bmatrix} x^k
$$

Za pretvorbu običnih potencija u rastuće potencije vrijedi sljedeći identitet:

$$
x^n=\sum_{k} \begin{Bmatrix}n\\ k\end{Bmatrix} (-1)^{n-k} x^{\overline{k}}
$$

### Pretvorba između padajućih potencija i običnih potencija

Padajuću faktorijelnu potenciju označavamo $x^{\underline{n}}=\dfrac{x!}{(x-n)!}=\prod_{k=0}^{n-1} (x-k)$.

Tada se obične potencije mogu pretvoriti u padajuće potencije sljedećim identitetom:

$$
x^n=\sum_{k} \begin{Bmatrix}n\\ k\end{Bmatrix} x^{\underline{k}}
$$

Za pretvorbu padajućih potencija u obične potencije vrijedi sljedeći identitet:

$$
x^{\underline{n}}=\sum_{k} \begin{bmatrix}n\\ k\end{bmatrix} (-1)^{n-k} x^k
$$

### Veza između prikaza polinoma padajućim faktorijelnim potencijama i prikaza polinoma vrijednostima u točkama

Ovdje prikaz polinoma padajućim faktorijelnim potencijama znači prikaz polinoma u obliku

$$
f(x)=\sum\limits_{i=0}^nb_i{x^{\underline{i}}}
$$

a prikaz vrijednostima u točkama znači prikaz polinoma pomoću $n+1$ točaka

$$
(i,a_i),i=0..n
$$

Očito između koeficijenata padajućih faktorijelnih potencija $b$ i vrijednosti u točkama $a$ vrijedi sljedeća veza:

$$
a_k=\sum\limits_{i=0}^{n}b_ik^{\underline{i}}
$$

tj.

$$
\begin{aligned}
a_k&=\sum\limits_{i=0}^{n}\dfrac{b_ik!}{(k-i)!}\\\dfrac{a_k}{k!}&=\sum\limits_{i=0}^kb_i\dfrac{1}{(k-i)!}
\end{aligned}
$$

To je izraz u obliku konvolucije, pa pretvorbu između vrijednosti u točkama i padajućih faktorijelnih potencija možemo obaviti u vremenskoj složenosti $O(n\log n)$.

## Zadaci za vježbu

-   [HDU3625 Examining the Rooms](https://acm.hdu.edu.cn/showproblem.php?pid=3625)
-   [UOJ540 联合省选 2020 组合数问题 (Zajednički pokrajinski izbor 2020 – Problem binomnih koeficijenata)](https://uoj.ac/problem/540)
-   [UOJ269 清华集训 2016 如何优雅地求和 (Tsinghua trening 2016 – Kako elegantno zbrajati)](https://uoj.ac/problem/269)

## Literatura i napomene

1.  [Stirling Number of the First Kind - Wolfram MathWorld](http://mathworld.wolfram.com/StirlingNumberoftheFirstKind.html)
2.  [Stirling Number of the Second Kind - Wolfram MathWorld](http://mathworld.wolfram.com/StirlingNumberoftheSecondKind.html)
