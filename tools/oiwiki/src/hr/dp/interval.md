---
title: Intervalni DP
---

## Definicija

Intervalni DP (interval DP) proširenje je linearnog dinamičkog programiranja: pri podjeli problema na faze bitno je u kojem se redoslijedu elementi pojavljuju unutar faze i iz kojih je elemenata prethodne faze trenutno stanje nastalo spajanjem.

Neka stanje $f(i,j)$ označava najveću vrijednost koja se može dobiti spajanjem svih elemenata s indeksima od $i$ do $j$. Tada je $f(i,j)=\max\{f(i,k)+f(k+1,j)+cost\}$, gdje je $cost$ vrijednost spajanja tih dviju skupina elemenata.

## Svojstva

Intervalni DP ima sljedeća obilježja:

**Spajanje**: dva ili više dijelova spajaju se u cjelinu (ili se, naravno, cjelina dijeli na dijelove);

**Značajka**: problem se može rastaviti na oblik u kojem se dijelovi spajaju po dva;

**Rješavanje**: za cijeli problem definiramo optimalnu vrijednost, prolazimo po točki spajanja, rastavljamo problem na lijevi i desni dio te na kraju spajanjem optimalnih vrijednosti dvaju dijelova dobivamo optimalnu vrijednost izvornog problema.

## Objašnjenje

### Primjer

???+ note "[„NOI1995” Spajanje kamenja](https://loj.ac/problem/10147)"
    Sažetak zadatka: na kružnici je $n$ brojeva $a_1,a_2,\dots,a_n$. Izvodi se $n-1$ operacija spajanja; u svakoj se dvije susjedne hrpe spajaju u jednu, a dobiva se broj bodova jednak zbroju kamenja u novonastaloj hrpi. Treba maksimizirati ukupan broj bodova.

Najprije razmotrimo slučaj u kojem hrpe nisu na kružnici, nego u nizu.

Neka $f(i,j)$ označava najveći broj bodova koji se može dobiti spajanjem svega kamenja u intervalu $[i,j]$ u jednu hrpu.

Zapišimo **jednadžbu prijelaza stanja**: $f(i,j)=\max\{f(i,k)+f(k+1,j)+\sum_{t=i}^{j} a_t \}~(i\le k<j)$

Neka $sum_i$ označava prefiksnu sumu niza $a$; jednadžba prijelaza tada postaje $f(i,j)=\max\{f(i,k)+f(k+1,j)+sum_j-sum_{i-1} \}$.

### Kako izvoditi prijelaze stanja

Budući da za izračun $f(i,j)$ trebamo znati sve vrijednosti $f(i,k)$ i $f(k+1,j)$, a oba ta stanja sadrže manje elemenata nego $f(i,j)$, kao fazu DP-a uzimamo $len=j-i+1$. Najprije prolazimo $len$ od manjeg prema većem, zatim prolazimo vrijednosti $i$, iz $len$ i $i$ formulom računamo $j$ i na kraju prolazimo $k$. Vremenska složenost je $O(n^3)$.

### Kako obraditi kružnicu

U zadatku je kamenje raspoređeno u kružnicu, a ne u niz. Što učiniti?

**Prvi način**: budući da kamenje čini kružnicu, možemo prolaziti mjesto na kojem je prerežemo i tako je pretvoriti u niz. Kako to treba učiniti $n$ puta, ukupna je vremenska složenost $O(n^4)$.

**Drugi način**: niz produljimo na dvostruku duljinu, na $2\times n$ hrpa, pri čemu je $i$-ta hrpa jednaka $n+i$-toj. Nakon rješavanja dinamičkim programiranjem uzmemo najbolju od vrijednosti $f(1,n),f(2,n+1),\dots,f(n,2n-1)$ i to je konačan odgovor. Vremenska složenost je $O(n^3)$.

## Implementacija

=== "C++"
    ```cpp
    for (len = 2; len <= n; len++)
      for (i = 1; i <= 2 * n - len; i++) {
        int j = len + i - 1;
        for (k = i; k < j; k++)
          f[i][j] = max(f[i][j], f[i][k] + f[k + 1][j] + sum[j] - sum[i - 1]);
      }
    ```

=== "Python"
    ```python
    for len in range(2, n + 1):
        for i in range(1, 2 * n - len + 1):
            j = len + i - 1
            for k in range(i, j):
                f[i][j] = max(f[i][j], f[i][k] + f[k + 1][j] + sum[j] - sum[i - 1])
    ```

## Nekoliko zadataka za vježbu

[NOIP 2006 Energetska ogrlica](https://www.luogu.com.cn/problem/P1063)

[NOIP 2007 Igra uzimanja brojeva iz matrice](https://www.luogu.com.cn/problem/P1005)

[„IOI2000” Poštanski uredi](https://www.luogu.com.cn/problem/P4767)
