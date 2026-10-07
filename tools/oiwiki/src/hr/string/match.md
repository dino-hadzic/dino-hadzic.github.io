---
title: Podudaranje stringova
---

Ova stranica ukratko opisuje problem podudaranja stringova (string matching) i načine njegova rješavanja.

## Problem podudaranja stringova

### Definicija

Zove se i podudaranje uzorka (pattern matching). Problem se može sažeti ovako: „zadani su stringovi $S$ i $T$; u tekstu $S$ treba pronaći podstring $T$”. String $T$ zove se uzorak (pattern).

### Vrste

-   Podudaranje jednog uzorka: zadani su jedan uzorak i jedan tekst; treba pronaći sve položaje na kojima se uzorak pojavljuje u tekstu.
-   Podudaranje više uzoraka: zadano je više uzoraka i jedan tekst; treba pronaći sve položaje na kojima se ti uzorci pojavljuju u tekstu.
    -   Ako ima više tekstova, dovoljno ih je nadovezati i obraditi kao jedan tekst.
    -   Može se riješiti i kao niz problema s jednim uzorkom, ali to nije dovoljno učinkovito.
-   Ostale vrste: npr. podudaranje bilo kojeg sufiksa jednog stringa, podudaranje bilo kojeg sufiksa više stringova…

## Pristup grubom silom

Skraćeno BF (Brute Force) algoritam. Osnovna ideja algoritma: krenemo od prvog znaka teksta $S$ i uspoređujemo ga s prvim znakom uzorka $T$; ako su jednaki, nastavljamo uspoređivati sljedeće znakove obaju stringova; inače se uzorak $T$ vraća na prvi znak i usporedba kreće iznova od drugog znaka teksta $S$. Tako se nastavlja dok se ne usporede svi znakovi stringa $S$ ili $T$.

### Implementacija

=== "C++"
    ```cpp
    /*
     * s: tekst u kojem tražimo
     * t: uzorak
     * n: duljina teksta
     * m: duljina uzorka
     */
    std::vector<int> match(char *s, char *t, int n, int m) {
      std::vector<int> ans;
      int i, j;
      for (i = 0; i < n - m + 1; i++) {
        for (j = 0; j < m; j++) {
          if (s[i + j] != t[j]) break;
        }
        if (j == m) ans.push_back(i);
      }
      return ans;
    }
    ```

=== "Python"
    ```python
    def match(s, t, n, m):
        if m < 1:
            return []
    
        ans = []
        for i in range(0, n - m + 1):
            for j in range(0, m):
                if s[i + j] != t[j]:
                    break
            else:
                ans.append(i)
        return ans
    ```

### Vremenska složenost

Neka je $n$ duljina teksta, a $m$ duljina uzorka. Pretpostavljamo $m\ll n$.

Kad BF algoritam uspješno pronađe uzorak: u najboljem slučaju samo je jedan prolaz uspješan i u njemu se obavi $m$ usporedbi, dok svaki od ostalih, neuspješnih prolaza propadne već na prvom znaku uzorka, što daje još $n-m$ usporedbi; ukupno je $n$ usporedbi, pa je vremenska složenost $O(n)$. U najgorem slučaju broj prolaza je $n-m+1$, u svakom se obavi $m$ usporedbi, ukupno $m(n-m+1)$ usporedbi, pa je vremenska složenost $O(mn)$.

Kad BF algoritam ne pronađe uzorak: u najboljem slučaju svaki neuspješni prolaz propadne na prvom znaku uzorka, pa BF algoritam obavi $n-m+1$ usporedbi i složenost je $O(n)$; u najgorem slučaju svaki neuspješni prolaz propadne na posljednjem znaku uzorka, pa BF algoritam obavi $m(n-m+1)$ usporedbi i složenost je $O(mn)$.

Ako uzorak sadrži barem dva različita znaka, prosječna vremenska složenost BF algoritma je $O(n)$. Međutim, stringovi u natjecateljskim zadacima obično nisu posve nasumični.

## Metoda hashiranja

Vidi: [Hashiranje stringova](./hash.md)

## KMP algoritam

Vidi: [Prefiksna funkcija i KMP algoritam](./kmp.md)
