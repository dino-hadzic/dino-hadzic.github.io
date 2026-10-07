---
title: Z-funkcija (prošireni KMP)
---

Dogovor: indeksi stringa počinju od $0$.

## Definicija

Za string $s$ duljine $n$ definiramo funkciju $z[i]$ kao duljinu najduljeg zajedničkog prefiksa (LCP) stringova $s$ i $s[i,n-1]$ (tj. sufiksa koji počinje znakom $s[i]$); niz $z$ zovemo **Z-funkcija** stringa $s$. Posebno, $z[0] = 0$.

U inozemstvu se algoritam za računanje tog niza obično zove **Z Algorithm**, a u Kini se naziva **prošireni KMP** (exKMP).

Ovaj članak opisuje algoritam za računanje Z-funkcije u vremenskoj složenosti $O(n)$ i njezine razne primjene.

## Objašnjenje

Sljedećih nekoliko primjera prikazuje Z-funkciju različitih stringova:

-   $z(\mathtt{aaaaa}) = [0, 4, 3, 2, 1]$
-   $z(\mathtt{aaabaab}) = [0, 2, 1, 0, 2, 1, 0]$
-   $z(\mathtt{abacaba}) = [0, 0, 1, 0, 3, 0, 1]$

## Naivni algoritam

Naivni algoritam za Z-funkciju ima složenost $O(n^2)$:

???+ note "Implementacija"
    === "C++"
        ```cpp
        vector<int> z_function_trivial(string s) {
          int n = (int)s.length();
          vector<int> z(n);
          for (int i = 1; i < n; ++i)
            while (i + z[i] < n && s[z[i]] == s[i + z[i]]) ++z[i];
          return z;
        }
        ```
    
    === "Python"
        ```python
        def z_function_trivial(s):
            n = len(s)
            z = [0] * n
            for i in range(1, n):
                while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                    z[i] += 1
            return z
        ```

## Linearni algoritam

Kao i kod većine algoritama iz područja stringova, ključ je u tome da idejom automata pronađemo funkciju prijelaza stanja pod zadanim ograničenjima, tako da pomoću prethodnih stanja ubrzamo računanje novih.

U ovom algoritmu vrijednosti $z[i]$ računamo redom od $1$ do $n-1$ ($z[0]=0$). Pri računanju $z[i]$ koristimo već izračunate $z[0],\ldots,z[i-1]$.

Za $i$ interval $[i,i+z[i]-1]$ zovemo **segment podudaranja** za $i$, ili Z-box.

Tijekom algoritma održavamo segment podudaranja s najdesnijim desnim krajem. Radi jednostavnosti označimo ga $[l,r]$. Po definiciji je $s[l,r]$ prefiks od $s$. Pri računanju $z[i]$ jamčimo da je $l\le i$. Na početku je $l=r=0$.

Pri računanju $z[i]$:

-   Ako je $i\le r$, onda po definiciji $[l,r]$ vrijedi $s[i,r] = s[i-l,r-l]$, pa je $z[i]\ge \min(z[i-l],r-i+1)$. Tada:
    -   ako je $z[i-l] < r-i+1$, onda je $z[i] = z[i-l]$;
    -   inače je $z[i-l]\ge r-i+1$; tada postavimo $z[i] = r-i+1$ i zatim grubom silom uspoređujemo sljedeće znakove i proširujemo $z[i]$ dok god je to moguće.
-   Ako je $i>r$, onda izravno po naivnom algoritmu uspoređujemo od $s[i]$ i grubom silom odredimo $z[i]$.
-   Nakon što izračunamo $z[i]$, ako je $i+z[i]-1>r$, moramo ažurirati $[l,r]$, tj. postaviti $l=i, r=i+z[i]-1$.

Simulaciju rada Z-funkcije možete pogledati na [ovoj stranici](https://personal.utdallas.edu/~besp/demo/John2010/z-algorithm.htm).

### Implementacija

=== "C++"
    ```cpp
    vector<int> z_function(string s) {
      int n = (int)s.length();
      vector<int> z(n);
      for (int i = 1, l = 0, r = 0; i < n; ++i) {
        if (i <= r && z[i - l] < r - i + 1) {
          z[i] = z[i - l];
        } else {
          z[i] = max(0, r - i + 1);
          while (i + z[i] < n && s[z[i]] == s[i + z[i]]) ++z[i];
        }
        if (i + z[i] - 1 > r) l = i, r = i + z[i] - 1;
      }
      return z;
    }
    ```

=== "Python"
    ```python
    def z_function(s):
        n = len(s)
        z = [0] * n
        l, r = 0, 0
        for i in range(1, n):
            if i <= r and z[i - l] < r - i + 1:
                z[i] = z[i - l]
            else:
                z[i] = max(0, r - i + 1)
                while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                    z[i] += 1
            if i + z[i] - 1 > r:
                l = i
                r = i + z[i] - 1
        return z
    ```

## Analiza složenosti

Svako izvršavanje unutarnje petlje `while` pomiče $r$ udesno za barem $1$, a $r< n-1$, pa se ukupno izvrši najviše $n$ puta.

Vanjska petlja samo je jedan linearni prolaz.

Ukupna složenost je $O(n)$.

## Primjene

Razmotrimo sada primjene Z-funkcije u nekoliko konkretnih situacija.

Te su primjene uvelike slične primjenama [prefiksne funkcije](./kmp.md).

### Traženje svih pojavljivanja podstringa

Da izbjegnemo zabunu, $t$ ćemo zvati **tekst**, a $p$ **uzorak**. Zadatak glasi: pronaći sva pojavljivanja (occurrence) uzorka $p$ u tekstu $t$.

Da bismo ga riješili, konstruiramo novi string $s = p + \diamond + t$, tj. spojimo $p$ i $t$, ali između njih stavimo razdjelni znak $\diamond$ (znak $\diamond$ biramo tako da se sigurno ne pojavljuje ni u $p$ ni u $t$).

Najprije izračunamo Z-funkciju od $s$. Zatim za svaki $i$ u intervalu $[0,|t| - 1]$ promotrimo vrijednost Z-funkcije $k = z[i + |p| + 1]$ sufiksa od $s$ koji počinje znakom $t[i]$. Ako je $k = |p|$, znamo da postoji pojavljivanje uzorka $p$ na $i$-toj poziciji teksta $t$; inače na $i$-toj poziciji teksta $t$ nema pojavljivanja uzorka $p$.

Vremenska složenost (a ujedno i prostorna) iznosi $O(|t| + |p|)$.

### Broj različitih podstringova

Zadan je string $s$ duljine $n$; treba izračunati broj različitih podstringova od $s$.

Razmotrimo računanje prirasta: znajući trenutni broj različitih podstringova od $s$, izračunajmo broj različitih podstringova nakon dodavanja jednog znaka na kraj od $s$.

Neka je $k$ trenutni broj različitih podstringova od $s$. Dodajmo novi znak $c$ na kraj od $s$. Očito će se pojaviti neki novi podstringovi koji završavaju s $c$ (podstringovi koji završavaju s $c$ i prije se nisu pojavili).

Neka je string $t$ obrat stringa $s + c$ (obrat je string dobiven obrnutim redoslijedom znakova izvornog stringa). Zadatak nam je izbrojiti koliko se prefiksa od $t$ ne pojavljuje nigdje drugdje u $t$. Izračunajmo Z-funkciju od $t$ i pronađimo njezinu najveću vrijednost $z_{\max}$. Tada su obrati prefiksa od $t$ duljine najviše $z_{\max}$ podstringovi koji završavaju s $c$ i već su se pojavili u $s$.

Dakle, broj novih podstringova nakon dodavanja znaka $c$ na kraj od $s$ iznosi $|t| - z_{\max}$.

Vremenska složenost algoritma je $O(n^2)$.

Vrijedi napomenuti da istom metodom u vremenu $O(n)$ možemo ponovno izračunati broj različitih podstringova nakon dodavanja ili uklanjanja jednog znaka na kraju (s kraja ili s početka).

### Cijeli period stringa

Zadan je string $s$ duljine $n$; treba pronaći njegov najkraći cijeli period, tj. najkraći string $t$ takav da se $s$ može zapisati kao spoj nekoliko kopija stringa $t$.

Izračunajmo Z-funkciju od $s$; duljina cijelog perioda tada je najmanji djelitelj $i$ broja $n$ za koji vrijedi $i+z[i]=n$.

Dokaz te činjenice jednak je dokazu u primjenama [prefiksne funkcije](./kmp.md).

## Zadaci za vježbu

-   [Luogu P5410 [predložak] prošireni KMP/exKMP (Z-funkcija)](https://www.luogu.com.cn/problem/P5410)
-   [Luogu P7114 [NOIP2020] Podudaranje stringova](https://www.luogu.com.cn/problem/P7114)
-   [CF126B Password](http://codeforces.com/problemset/problem/126/B)
-   [UVa # 455 Periodic Strings](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=396)
-   [UVa # 11022 String Factoring](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1963)
-   [UVa 11475 - Extend to Palindrome](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=2470)
-   [Codechef - Chef and Strings](https://www.codechef.com/problems/CHSTR)
-   [Codeforces - Prefixes and Suffixes](http://codeforces.com/problemset/problem/432/D)
-   [Leetcode 2223 - Sum of Scores of Built Strings](https://leetcode.com/problems/sum-of-scores-of-built-strings/)

**Ova je stranica uglavnom prevedena iz članka [Z-функция строки и её вычисление](http://e-maxx.ru/algo/z_function) i njegova engleskog prijevoda [Z-function and its calculation](https://cp-algorithms.com/string/z-function.html). Ruska je inačica objavljena pod licencijom Public Domain + Leave a Link, a engleska pod CC-BY-SA 4.0.**
