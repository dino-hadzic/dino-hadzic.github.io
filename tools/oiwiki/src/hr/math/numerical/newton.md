---
title: Newtonova metoda
---

## Uvod

U ovom članku opisujemo kako Newtonovom metodom (Newton's method for finding roots, metoda tangenti) naći približno rješenje jednadžbe. Metodu je u 17. stoljeću predložio Newton.

Konkretan je zadatak sljedeći: za funkciju $f(x)$ koja je neprekidna i monotona na $[a,b]$ naći približno rješenje jednadžbe $f(x)=0$.

## Objašnjenje

Na početku krećemo od zadane funkcije $f(x)$ i jednog približnog rješenja $x_0$ (pitanje početne vrijednosti povezano je s Newtonovim fraktalima; vidi [Newtonov fraktal](https://www.bilibili.com/video/BV1HQ4y1q78v) autora 3Blue1Brown).

Pretpostavimo da je trenutačno približno rješenje $x_i$. Povucimo pravac $l$ koji dira $f(x)$ u točki $(x_i,f(x_i))$ i označimo apscisu sjecišta pravca $l$ s osi $x$ sa $x_{i+1}$; to je bolje približno rješenje. Taj iterativni postupak ponavljamo.
Prema geometrijskom značenju derivacije dobivamo sljedeću relaciju:

$$
 f'(x_i) = \frac{f(x_i)}{x_{i} - x_{i+1}}
$$

Sređivanjem dobivamo sljedeću rekurzivnu formulu:

$$
 x_{i+1} = x_i - \frac{f(x_i)}{f'(x_i)}
$$

Intuitivno, ako je $f(x)$ razmjerno glatka, s povećanjem broja iteracija $x_i$ će se sve više približavati rješenju jednadžbe.

Brzina konvergencije Newtonove metode kvadratna je, što znači da se nakon svake iteracije broj točnih znamenaka približnog rješenja udvostručuje.
Dokaz konvergencije Newtonove metode može se naći u [citizendium - Newton method Convergence analysis](http://en.citizendium.org/wiki/Newton%27s_method#Convergence_analysis)

Naravno, Newtonova metoda ima i nedostatke; pojedinosti vidi u analizi na str. 18–20 u [Xiaolin Wu - Roots of Equations](https://www.ece.mcmaster.ca/~xwu/part2.pdf)

## Računanje drugog korijena

Pokušajmo Newtonovom metodom izračunati drugi korijen. Neka je $f(x)=x^2-n$; približno rješenje te jednadžbe približna je vrijednost od $\sqrt{n}$. Tako dobivamo

$$
x_{i+1}=x_i-\frac{x_i^2-n}{2x_i}=\frac{x_i+\frac{n}{x_i}}{2}
$$

Pri implementaciji treba paziti na odabir odgovarajuće preciznosti. Kôd slijedi

### Implementacija

=== "C++"
    ```cpp
    double sqrt_newton(double n) {
      constexpr static double eps = 1E-15;
      double x = 1;
      while (true) {
        double nx = (x + n / x) / 2;
        if (abs(x - nx) < eps) break;
        x = nx;
      }
      return x;
    }
    ```

=== "Python"
    ```python
    def sqrt_newton(n):
        eps = 1e-15
        x = 1
        while True:
            nx = (x + n / x) / 2
            if abs(x - nx) < eps:
                break
            x = nx
        return x
    ```

## Računanje cjelobrojnog drugog korijena

Iako vrijednost drugog korijena možemo dobiti pozivom funkcije `sqrt()`, ovdje ipak opisujemo varijantu Newtonove metode kojom se nalazi najveće cjelobrojno rješenje nejednadžbe $x^2\le n$. I dalje promatramo postupak sličan Newtonovoj iteraciji, ali s malo izmijenjenim rubnim uvjetom. Ako je u prethodnoj iteraciji približno rješenje $x$ postalo manje, a u ovoj iteraciji postaje veće, tu iteraciju ne izvodimo i izlazimo iz petlje.

### Implementacija

=== "C++"
    ```cpp
    int isqrt_newton(int n) {
      int x = 1;
      bool decreased = false;
      for (;;) {
        int nx = (x + n / x) >> 1;
        if (x == nx || (nx > x && decreased)) break;
        decreased = nx < x;
        x = nx;
      }
      return x;
    }
    ```

=== "Python"
    ```python
    def isqrt_newton(n):
        x = 1
        decreased = False
        while True:
            nx = (x + n // x) // 2
            if x == nx or (nx > x and decreased):
                break
            decreased = nx < x
            x = nx
        return x
    ```

## Drugi korijen velikih brojeva

Na kraju razmotrimo Newtonovu metodu za velike brojeve (bignum). Način iteriranja ostaje isti, ali ovaj put moramo obratiti pozornost na odabir početnog približnog rješenja, tj. na vrijednost $x_0$. Budući da su brojevi za koje je potrebna aritmetika velikih brojeva u pravilu vrlo veliki, različite početne vrijednosti jako utječu na učinkovitost algoritma. Prirodna je ideja uzeti $x_0=2^{\left\lfloor\frac{1}{2}\log_2n\right\rfloor}$, čime se $x_0$ može brzo izračunati, a ujedno je razmjerno blizu približnoj vrijednosti drugog korijena.

### Implementacija

Dajemo implementaciju u Javi:

```java
public static BigInteger isqrtNewton(BigInteger n) {
  BigInteger a = BigInteger.ONE.shiftLeft(n.bitLength() / 2);
  boolean p_dec = false;
  for (;;) {
    BigInteger b = n.divide(a).add(a).shiftRight(1);
    if (a.compareTo(b) == 0 || a.compareTo(b) < 0 && p_dec)
      break;
    p_dec = a.compareTo(b) > 0;
    a = b;
  }
  return a;
}
```

Rezultati u praksi: za $n=10^{1000}$ vrijeme izvođenja ovog algoritma iznosi 60 ms; ako ne optimiziramo vrijednost $x_0$, nego iteriramo izravno od $x_0=1$, vrijeme izvođenja raste na 120 ms.

## Zadaci za vježbu

-   [UVa 10428 - The Roots](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=16&page=show_problem&problem=1369)
-   [LeetCode 69. x 的平方根 (Sqrt(x))](https://leetcode-cn.com/problems/sqrtx/)

    **Ova je stranica uglavnom prevedena iz članka [Метод Ньютона (касательных) для поиска корней](http://e-maxx.ru/algo/roots_newton) i njegova engleskog prijevoda [Newton's method for finding roots](https://cp-algorithms.com/num_methods/roots_newton.html). Ruska je inačica pod licencijom Public Domain + Leave a Link, a engleska pod licencijom CC-BY-SA 4.0.**
