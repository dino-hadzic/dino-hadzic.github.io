---
title: Eulerova funkcija
---

## Definicija

Eulerova funkcija (Euler's totient function), tj. $\varphi(n)$, označava broj brojeva manjih ili jednakih $n$ koji su relativno prosti s $n$.

Na primjer, $\varphi(1) = 1$.

Kad je $n$ prost, očito je $\varphi(n) = n - 1$.

## Svojstva

-   Eulerova funkcija je [multiplikativna funkcija](./basic.md#multiplikativne-funkcije).

    Odnosno, za sve cijele brojeve $a,b$ za koje je $\gcd(a, b) = 1$ vrijedi $\varphi(ab) = \varphi(a)\varphi(b)$.

    Posebno, kad je $n$ neparan, vrijedi $\varphi(2n) = \varphi(n)$.

    Dokaz vidi u [Kompoziciji sustava ostataka](./basic.md#sastavljanje-sustava-ostataka).

-   $n = \sum_{d \mid n}{\varphi(d)}$.

    ???+ note "Dokaz"
        Može se izvesti pomoću znanja o [Möbiusovoj inverziji](./mobius.md).
        
        Može se razmišljati i ovako: ako je $\gcd(k, n) = d$, onda je $\gcd(\dfrac{k}{d},\dfrac{n}{d}) = 1, ( k < n )$.
        
        Ako s $f(x)$ označimo broj brojeva za koje je $\gcd(k, n) = x$, onda je $n = \sum_{i = 1}^n{f(i)}$.
        
        Prema gornjem dokazu uočavamo da je $f(x) = \varphi(\dfrac{n}{x})$, pa je $n = \sum_{d \mid n}\varphi(\dfrac{n}{d})$. Primijetimo da su djelitelji $d$ i $\dfrac{n}{d}$ simetrični, pa se gornja formula svodi na $n = \sum_{d \mid n}\varphi(d)$.

-   Ako je $n = p^k$, gdje je $p$ prost, onda je $\varphi(n) = p^k - p^{k - 1}$.
    (slijedi iz definicije)

-   Po osnovnom teoremu aritmetike, neka je $n = \prod_{i=1}^{s}p_i^{k_i}$, gdje su $p_i$ prosti; tada je $\varphi(n) = n \times \prod_{i = 1}^s{\dfrac{p_i - 1}{p_i}}$.

    ???+ note "Dokaz"
        -   Lema: neka je $p$ bilo koji prost broj; tada je $\varphi(p^k)=p^{k-1}\times(p-1)$.
        
            Dokaz: očito su među svim brojevima od $1$ do $p^k$ svi osim $p^{k-1}$ višekratnika broja $p$ relativno prosti s $p^k$, pa je $\varphi(p^k)=p^k-p^{k-1}=p^{k-1}\times(p-1)$, što je i trebalo dokazati.
        
        Sada dokazujemo $\varphi(n) = n \times \prod_{i = 1}^s{\dfrac{p_i - 1}{p_i}}$. Iz osnovnog teorema aritmetike i multiplikativnosti funkcije $\varphi(x)$ slijedi
        
        $$
        \begin{aligned}
            \varphi(n) &= \prod_{i=1}^{s} \varphi(p_i^{k_i}) \\
            &= \prod_{i=1}^{s} (p_i-1)\times {p_i}^{k_i-1}\\
            &=\prod_{i=1}^{s} {p_i}^{k_i} \times(1 - \frac{1}{p_i})\\
            &=n~ \prod_{i=1}^{s} (1- \frac{1}{p_i})
            &\square
        \end{aligned}
        $$

-   Za sve pozitivne cijele brojeve $m,n$ vrijedi $\varphi(mn)\varphi(\gcd(m,n))=\varphi(m)\varphi(n)\gcd(m,n)$.

    Slijedi izravnim računom iz prethodnog svojstva.

## Implementacija

Ako trebamo vrijednost Eulerove funkcije samo za jedan broj, računamo je izravno po definiciji, usporedno s rastavom na proste faktore. Taj se postupak može ubrzati algoritmom [Pollard rho](./pollard-rho.md).

???+ note "Referentna implementacija"
    === "C++"
        ```cpp
        #include <cmath>
        
        int euler_phi(int n) {
          int ans = n;
          for (int i = 2; i * i <= n; i++)
            if (n % i == 0) {
              ans = ans / i * (i - 1);
              while (n % i == 0) n /= i;
            }
          if (n > 1) ans = ans / n * (n - 1);
          return ans;
        }
        ```
    
    === "Python"
        ```python
        import math
        
        
        def euler_phi(n):
            ans = n
            for i in range(2, math.isqrt(n) + 1):
                if n % i == 0:
                    ans = ans // i * (i - 1)
                    while n % i == 0:
                        n = n // i
            if n > 1:
                ans = ans // n * (n - 1)
            return ans
        ```

Ako trebamo vrijednosti Eulerove funkcije za više brojeva, možemo ih izračunati linearnim sitom, koje će biti opisano kasnije.

Detalje vidi u: [Računanje Eulerove funkcije sitom](./sieve.md#sito-za-eulerovu-funkciju)

## Primjene

Eulerova funkcija često se koristi za pojednostavljivanje zbroja niza najvećih zajedničkih djelitelja. U nekim kineskim člancima to se naziva **Eulerovom inverzijom**[^1].

Uvrstimo li u tvrdnju

$$
n=\sum_{d \mid n}\varphi(d)
$$

$n=\gcd(a,b)$, dobivamo

$$
\gcd(a,b) = \sum_{d \mid \gcd(a,b)}\varphi(d) = \sum_d [d \mid a][d \mid b]\varphi(d),
$$

gdje je $[\cdot]$ Iversonova zagrada. Sumiranjem gornje formule dobivamo

$$
\sum_{i=1}^n\gcd(i,n)=\sum_{d}\sum_{i=1}^n[d \mid i][d \mid n]\varphi(d)=\sum_d\left\lfloor\frac{n}{d}\right\rfloor[d \mid n]\varphi(d)=\sum_{d \mid n}\left\lfloor\frac{n}{d}\right\rfloor\varphi(d).
$$

Ključno je opažanje $\sum_{i=1}^n[d \mid i]=\lfloor\frac{n}{d}\rfloor$, tj. broj brojeva $i$ između $1$ i $n$ djeljivih s $d$ jednak je $\lfloor\frac{n}{d}\rfloor$.

Pomoću te formule zbroj možemo izračunati prolaskom kroz djelitelje. Kad ima više upita, možemo unaprijed izračunati prefiksne sume Eulerove funkcije i odgovarati blokovskim dijeljenjem po cjelobrojnom kvocijentu (数论分块).

???+ note "[GCD SUM](https://www.luogu.com.cn/problem/P2398)"
    Zadan je $n\le 100000$; izračunajte
    
    $$
    \sum_{i=1}^n\sum_{j=1}^n\gcd(i,j).
    $$
    
    ??? note "Ideja"
        Po uzoru na gornje izvođenje dobivamo
        
        $$
        \sum_{i=1}^n\sum_{j=1}^n\gcd(i,j) = \sum_{d=1}^n\left\lfloor\frac{n}{d}\right\rfloor^2\varphi(d).
        $$
        
        Ovdje treba izračunati Eulerovu funkciju za sve brojeve od $1$ do $n$; linearnim sitom odgovor dobivamo u $O(n)$.

## Eulerov teorem

Teorem usko povezan s Eulerovom funkcijom jest Eulerov teorem. Glasi ovako:

Ako je $\gcd(a, m) = 1$, onda je $a^{\varphi(m)} \equiv 1 \pmod{m}$.

### Prošireni Eulerov teorem

Naravno, postoji i prošireni Eulerov teorem, koji se bavi slučajem općih $a$ i $m$.

$$
a^b\equiv
\begin{cases}
a^{b\bmod\varphi(m)},\,&\gcd(a,\,m)=1\\
a^b,&\gcd(a,\,m)\ne1,\,b<\varphi(m)\\
a^{b\bmod\varphi(m)+\varphi(m)},&\gcd(a,\,m)\ne1,\,b\ge\varphi(m)
\end{cases}
\pmod m
$$

Dokaz i zadatke vidi u [Eulerovu teoremu](./fermat.md).

## Zadaci

-   [SPOJ ETF. Euler Totient Function](http://www.spoj.com/problems/ETF/)
-   [UVa 10179. Irreducible Basic Fractions](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1120)
-   [UVa 10299. Relatives](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1240)
-   [UVa 11327. Enumerating Rational Numbers](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2302)
-   [TIMUS 1673. Admission to Exam](http://acm.timus.ru/problem.aspx?space=1&num=1673)
-   [Luogu P1390 公约数的和 (Zbroj zajedničkih djelitelja)](https://www.luogu.com.cn/problem/P1390)
-   [Luogu P2155 \[SDOI2008\] 沙拉公主的困惑 (Nedoumica princeze Salate)](https://www.luogu.com.cn/problem/P2155)
-   [Luogu P2568 GCD](https://www.luogu.com.cn/problem/P2568)

## Literatura i bilješke

[^1]: Taj se naziv ne pojavljuje u znanstvenim časopisima ni na forumima izvan Kine, pa pri njegovoj upotrebi treba biti oprezan.
