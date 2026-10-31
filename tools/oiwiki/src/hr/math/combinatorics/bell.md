---
title: Bellovi brojevi
---

Bellovi brojevi $B_n$ (Bell numbers), nazvani po Ericu Templeu Bellu, niz su cijelih brojeva iz kombinatorike koji počinje ovako ([OEIS A000110](https://oeis.org/A000110)):

$$
B_0 = 1,B_1 = 1,B_2=2,B_3=5,B_4=15,B_5=52,B_6=203,\dots
$$

$B_n$ je broj particija skupa kardinalnosti $n$. Particija skupa $S$ definira se kao familija u parovima disjunktnih nepraznih podskupova od $S$ čija je unija $S$. Na primjer, $B_3 = 5$ jer skup ${a, b, c}$ s 3 elementa ima 5 različitih particija:

$$
\begin{aligned}
&\{ \{a\},\{b\},\{c\}\} \\
&\{ \{a\},\{b,c\}\} \\
&\{ \{b\},\{a,c\}\} \\
&\{ \{c\},\{a,b\}\} \\
&\{ \{a,b,c\}\} \\
\end{aligned}
$$

$B_0$ je 1 jer prazan skup ima točno 1 particiju.

## Rekurzivna formula

Bellovi brojevi zadovoljavaju rekurzivnu formulu:

$$
B_{n+1}=\sum_{k=0}^n\binom{n}{k}B_{k}
$$

Dokaz:

$B_{n+1}$ je broj particija skupa s $n+1$ elementom. Neka je skup koji pripada broju $B_n$ jednak $\{b_1,b_2,b_3,\dots,b_n\}$, a skup koji pripada broju $B_{n+1}$ jednak $\{b_1,b_2,b_3,\dots,b_n,b_{n+1}\}$; tada možemo smatrati da $B_{n+1}$ nastaje iz $B_{n}$ dodavanjem elementa $b_{n+1}$. Promotrimo element $b_{n+1}$.

-   Ako je sam u svojem bloku, preostaje $n$ elemenata, pa je u tom slučaju broj particija $\dbinom{n}{n}B_{n}$;

-   ako je u istom bloku s još 1 elementom, preostaje $n-1$ element, pa je u tom slučaju broj particija $\dbinom{n}{n-1}B_{n-1}$;

-   ako je u istom bloku s još 2 elementa, preostaje $n-2$ elemenata, pa je u tom slučaju broj particija $\dbinom{n}{n-2}B_{n-2}$;

-   …

Nastavljajući tako dobivamo gornju formulu.

Svaki je Bellov broj zbroj odgovarajućih [Stirlingovih brojeva druge vrste](./stirling.md#stirlingovi-brojevi-druge-vrste-stirling-number),
jer je Stirlingov broj druge vrste broj načina da se skup kardinalnosti $n$ podijeli na točno $k$ nepraznih skupova.

$$
B_{n} = \sum_{k=0}^n{n\brace k}
$$

## Bellov trokut

Sljedećim postupkom konstruiramo trokutastu matricu (oblikom sličnu Pascalovu trokutu):

-   $a_{0,0} = 1$;
-   za $n \ge 1$ prvi član $n$-tog retka jednak je posljednjem članu prethodnog retka, tj. $a_{n,0}=a_{n-1,n-1}$;
-   za $m,n \ge 1$ $m$-ti član $n$-tog retka jednak je zbroju broja lijevo od njega i broja gore lijevo od njega, tj. $a_{n,m}=a_{n,m-1}+a_{n-1,m-1}$.

Dio rezultata izgleda ovako:

$$
\begin{aligned}
& 1   \\
& 1\quad\qquad 2  \\
& 2\quad\qquad 3\quad\qquad 5  \\
& 5\quad\qquad 7\quad\qquad 10\,\,\,\qquad 15 \\
& 15\,\,\,\qquad 20\,\,\,\qquad  27\,\,\,\qquad 37\,\,\,\qquad 52  \\
& 52\,\,\,\qquad  67\,\,\,\qquad 87\,\,\,\qquad 114\qquad 151\qquad 203\\
& 203\qquad  255\qquad 322\qquad  409\qquad 523\qquad  674\qquad 877 \\  
\end{aligned}
$$

Prvi član svakog retka Bellov je broj. Pomoću ovog trokuta Bellovi se brojevi mogu rekurzivno izračunati.

??? note "Referentna implementacija"
    === "C++"
        ```cpp
        constexpr int MAXN = 2000 + 5;
        int bell[MAXN][MAXN];
        
        void f(int n) {
          bell[0][0] = 1;
          for (int i = 1; i <= n; i++) {
            bell[i][0] = bell[i - 1][i - 1];
            for (int j = 1; j <= i; j++)
              bell[i][j] = bell[i - 1][j - 1] + bell[i][j - 1];
          }
        }
        ```
    
    === "Python"
        ```python
        MAXN = 2000 + 5
        bell = [[0 for i in range(MAXN + 1)] for j in range(MAXN + 1)]
        
        
        def f(n):
            bell[0][0] = 1
            for i in range(1, n + 1):
                bell[i][0] = bell[i - 1][i - 1]
                for j in range(1, i + 1):
                    bell[i][j] = bell[i - 1][j - 1] + bell[i][j - 1]
        ```

## Eksponencijalna funkcija izvodnica

Promotrimo eksponencijalnu funkciju izvodnicu Bellovih brojeva i njezinu derivaciju:

$$
\begin{aligned}
\hat B(x) &= \sum_{n = 0}^{+\infty}\frac{B_n}{n!}x^n \\
&= 1 + \sum_{n = 0}^{+\infty}\frac{B_{n+1}}{(n + 1)!}x^{n + 1} \\
\hat B'(x) &= \sum_{n = 0}^{+\infty}\frac{B_{n+1}}{n!}x^{n}
\end{aligned}
$$

Iz rekurzivne formule za Bellove brojeve dobivamo:

$$
\frac{B_{n+1}}{n!} = \sum_{k = 0}^{n}\frac{1}{(n-k)!}\frac{B_{k}}{k!}
$$

To je izraz oblika konvolucije, pa vrijedi:

$$
\hat B'(x) = \mathrm{e}^x \hat B(x)
$$

To je diferencijalna jednadžba čije je rješenje:

$$
\hat B(x) = \exp\left(\mathrm{e}^x + C\right)
$$

Naposljetku, za $x = 0$ vrijedi $\hat B(x) = 1$; uvrštavanjem dobivamo $C = -1$, pa zatvoreni oblik eksponencijalne funkcije izvodnice Bellovih brojeva glasi:

$$
\hat B(x) = \exp\left(\mathrm{e}^x - 1\right)
$$

Nakon što unaprijed izračunamo prvih $n$ članova od $\mathrm{e}^x - 1$, jednim [eksponencijalom polinoma](../poly/elementary-func.md#logaritam-i-eksponencijalna-funkcija-polinoma) dobivamo prvih $n$ Bellovih brojeva; usko je grlo vremenske složenosti eksponencijal polinoma, pa se može postići vremenska složenost $O(n \log n)$.

## Literatura

<https://en.wikipedia.org/wiki/Bell_number>
