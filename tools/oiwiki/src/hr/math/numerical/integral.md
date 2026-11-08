---
title: Numerička integracija
---

## Definicija određenog integrala

Jednostavno rečeno, određeni integral $\int_{l}^{r}f(x)\mathrm{d}x$ funkcije $f(x)$ na intervalu $[l,r]$ označava površinu područja koje $f(x)$ na intervalu $[l,r]$ zatvara s osi $x$ (pri čemu se dio iznad osi $x$ računa pozitivno, a dio ispod osi $x$ negativno).

U mnogim slučajevima trebamo učinkovito i točno izračunati približnu vrijednost nekog integrala. **Simpsonova metoda**, koju predstavljamo u nastavku, upravo je jedna takva metoda numeričke integracije.

## Simpsonova metoda

Ideja je ove metode podijeliti interval integracije na više malih dijelova i na svakom dijelu primijeniti formulu za integral kvadratne funkcije.

??? note "Formula za integral kvadratne funkcije (Simpsonova formula)"
    Za kvadratnu funkciju $f(x)=ax^2+bx+c$ vrijedi:
    
    $$
    \int_l^r f(x) {\mathrm d}x = \frac{(r-l)(f(l)+f(r)+4 f(\frac{l+r}{2}))}{6}
    $$
    
    Izvod:
    Za kvadratnu funkciju $f(x)=ax^2+bx+c$;
    integriranjem dobivamo $F(x)=\int_0^x f(x) {\mathrm d}x = \frac{a}{3}x^3+\frac{b}{2}x^2+cx+D$, gdje je D konstanta, pa je
    
    $$
    \begin{aligned}
    \int_l^r f(x) {\mathrm d}x &= F(r)-F(l) \\
    &= \frac{a}{3}(r^3-l^3)+\frac{b}{2}(r^2-l^2)+c(r-l) \\
    &=(r-l)(\frac{a}{3}(l^2+r^2+lr)+\frac{b}{2}(l+r)+c) \\
    &=\frac{r-l}{6}(2al^2+2ar^2+2alr+3bl+3br+6c)\\
    &=\frac{r-l}{6}((al^2+bl+c)+(ar^2+br+c)+4(a(\frac{l+r}{2})^2+b(\frac{l+r}{2})+c)) \\
    &=\frac{r-l}{6}(f(l)+f(r)+4f(\frac{l+r}{2}))
    \end{aligned}
    $$

Na temelju te Simpsonove formule najprije predstavljamo običnu Simpsonovu metodu integracije.

### Obična Simpsonova metoda

Godine 1743. ta je metoda objavljena u jednom radu Thomasa Simpsona.

#### Opis

Za zadani prirodni broj $n$ podijelimo interval $[l, r]$ na $2n$ jednako dugih intervala $x$.

$x_i = l + i h, ~~ i = 0 \ldots 2n,$ $h = \frac {r-l} {2n}.$

Tada možemo izračunati vrijednost integrala na svakom malom intervalu $[x_ {2i-2}, x_ {2i}]$, $i = 1\ldots n$; zbroj vrijednosti integrala na svim intervalima ukupni je integral.

Za jedan interval $[x_ {2i-2}, x_ {2i}]$, $i = 1\ldots n$, odaberemo tri točke $(x_ {2i-2}, x_ {2i-1}, x_ {2i})$ u njemu; one određuju parabolu, a time i funkciju $P(x)$, koja postoji i jedinstvena je. Računanje integrala izvorne funkcije na tom intervalu tako postaje računanje integrala nove kvadratne funkcije $P(x)$ na tom intervalu. Njega možemo približno izračunati Simpsonovom formulom.

$\int_{x_ {2i-2}} ^ {x_ {2i}} f (x) ~dx \approx \int_{x_ {2i-2}} ^ {x_ {2i}} P (x) ~dx = \left(f(x_{2i-2}) + 4f(x_{2i-1})+(f(x_{2i})\right)\frac {h} {3}$

Zbrajanjem po dijelovima dobivamo sljedeći zaključak:

$\int_l ^ r f (x) dx \approx \left(f (x_0) + 4 f (x_1) + 2 f (x_2) + 4f(x_3) + 2 f(x_4) + \ldots + 4 f(x_{2N-1}) + f(x_{2N}) \right)\frac {h} {3}$

#### Pogreška

Navodimo izravno rezultat: pogreška obične Simpsonove metode iznosi:

$$
-\tfrac{1}{90} \left(\tfrac{r-l}{2}\right)^5 f^{(4)}(\xi)
$$

gdje je $\xi$ neka vrijednost iz intervala $[l,r]$.

#### Implementacija

=== "C++"
    ```cpp
    constexpr int N = 1000 * 1000;
    
    double simpson_integration(double a, double b) {
      double h = (b - a) / N;
      double s = f(a) + f(b);
      for (int i = 1; i <= N - 1; ++i) {
        double x = a + h * i;
        s += f(x) * ((i & 1) ? 4 : 2);
      }
      s *= h / 3;
      return s;
    }
    ```

=== "Python"
    ```python
    N = 1000 * 1000
    
    
    def simpson_integration(a, b):
        h = (b - a) / N
        s = f(a) + f(b)
        for i in range(1, N):
            x = a + h * i
            if i & 1:
                s = s + f(x) * 4
            else:
                s = s + f(x) * 2
        s = s * (h / 3)
        return s
    ```

### Adaptivna Simpsonova metoda

Obična metoda, da bi osigurala točnost, vremenski je neizbježno ograničena brojem $n$; trebali bismo pronaći prikladniju metodu.

Jedini je problem sada kako podijeliti interval. Ako je dijelova premalo, pogreška računanja je velika; ako ih je previše, vremenska je učinkovitost niska. Trebamo pronaći ravnotežu između točnosti i učinkovitosti.

Razmišljamo ovako: ako je neki dio grafa već vrlo blizu kvadratnoj funkciji, izravnim uvrštavanjem u formulu dobivamo integral vrlo visoke točnosti i taj dio ne treba dalje dijeliti.

Tako dolazimo do sljedećeg načina dijeljenja: svaki put procijenimo koliko je trenutačni dio sličan kvadratnoj funkciji; ako je dovoljno sličan, izravno ga uvrstimo u formulu, a inače trenutačni dio podijelimo na lijevi i desni dio i riješimo rekurzivno.

Preostaje još jedan problem: kako procijeniti je li neki dio sličan kvadratnoj funkciji?

Trenutačni dio izravno uvrstimo u formulu i izračunamo integral, zatim ga u polovištu podijelimo na dva dijela i oba dijela također izravno uvrstimo u formulu. Ako se integral trenutačnog dijela i zbroj integrala dvaju dijelova nakon podjele vrlo malo razlikuju, možemo smatrati da je trenutačni dio vrlo sličan kvadratnoj funkciji i ne treba ga dalje rekurzivno dijeliti.

To je ideja adaptivne Simpsonove metode. Pri odlučivanju u fazi podijeli-pa-vladaj, osim provjere točnosti, obično se prisilno izvodi i najmanji broj iteracija.

Referentni kôd:

=== "C++"
    ```cpp
    double simpson(double l, double r) {
      double mid = (l + r) / 2;
      return (r - l) * (f(l) + 4 * f(mid) + f(r)) / 6;  // Simpsonova formula
    }
    
    double asr(double l, double r, double eps, double ans, int step) {
      double mid = (l + r) / 2;
      double fl = simpson(l, mid), fr = simpson(mid, r);
      if (abs(fl + fr - ans) <= 15 * eps && step < 0)
        return fl + fr + (fl + fr - ans) / 15;  // ako je dovoljno slično, odmah vrati rezultat
      return asr(l, mid, eps / 2, fl, step - 1) +
             asr(mid, r, eps / 2, fr, step - 1);  // inače podijeli na dva dijela i riješi rekurzivno
    }
    
    double calc(double l, double r, double eps) {
      return asr(l, r, eps, simpson(l, r), 12);
    }
    ```

=== "Python"
    ```python
    def simpson(l, r):
        mid = (l + r) / 2
        return (r - l) * (f(l) + 4 * f(mid) + f(r)) / 6  # Simpsonova formula
    
    
    def asr(l, r, eps, ans, step):
        mid = (l + r) / 2
        fl = simpson(l, mid)
        fr = simpson(mid, r)
        if abs(fl + fr - ans) <= 15 * eps and step < 0:
            return fl + fr + (fl + fr - ans) / 15  # ako je dovoljno slično, odmah vrati rezultat
        return asr(l, mid, eps / 2, fl, step - 1) + asr(
            mid, r, eps / 2, fr, step - 1
        )  # inače podijeli na dva dijela i riješi rekurzivno
    
    
    def calc(l, r, eps):
        return asr(l, r, eps, simpson(l, r), 12)
    ```

## Zadaci za vježbu

-   [Luogu4525【模板】自适应辛普森法 1 (Predložak: adaptivna Simpsonova metoda 1)](https://www.luogu.com.cn/problem/P4525)
-   [HDU1724 Ellipse](https://acm.hdu.edu.cn/showproblem.php?pid=1724)
-   [NOI2005 月下柠檬树 (Limunovo stablo na mjesečini)](https://www.luogu.com.cn/problem/P4207)

## Literatura

<https://doi.org/10.1145/321526.321537>: Taj članak razmatra poboljšanja adaptivne Simpsonove metode, a u njemu se podrobno objašnjava podrijetlo i prednost konstante `15` iz gornjeg koda.
