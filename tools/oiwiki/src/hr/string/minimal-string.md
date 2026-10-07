---
title: Minimalna reprezentacija
---

## Definicija

Algoritam minimalne reprezentacije rješava problem pronalaženja minimalne reprezentacije stringa.

## Minimalna reprezentacija stringa

### Ciklička ekvivalentnost

Ako u stringu $S$ možemo odabrati poziciju $i$ tako da vrijedi

$$
S[i\cdots n]+S[1\cdots i-1]=T
$$

kažemo da su $S$ i $T$ ciklički ekvivalentni.

### Minimalna reprezentacija

Minimalna reprezentacija stringa $S$ leksikografski je najmanji među svim stringovima koji su ciklički ekvivalentni stringu $S$.

## Jednostavno grubo pretraživanje

U svakom koraku uspoređujemo cikličke pomake koji počinju na $i$ i $j$, a trenutačni pomak pri uspoređivanju označavamo s $k$. Kad naiđemo na različite znakove, preskočimo većeg kandidata. Na kraju ostaje optimalno rješenje.

### Implementacija

=== "C++"
    ```cpp
    int k = 0, i = 0, j = 1;
    while (k < n && i < n && j < n) {
      if (sec[(i + k) % n] == sec[(j + k) % n]) {
        ++k;
      } else {
        if (sec[(i + k) % n] > sec[(j + k) % n])
          ++i;
        else
          ++j;
        k = 0;
        if (i == j) i++;
      }
    }
    i = min(i, j);
    ```

=== "Python"
    ```python
    k, i, j = 0, 0, 1
    while k < n and i < n and j < n:
        if sec[(i + k) % n] == sec[(j + k) % n]:
            k += 1
        else:
            if sec[(i + k) % n] > sec[(j + k) % n]:
                i += 1
            else:
                j += 1
            k = 0
            if i == j:
                i += 1
    i = min(i, j)
    ```

### Objašnjenje

Ova implementacija dobro radi na nasumičnim podacima, ali mogu se konstruirati posebni ulazi na kojima je prespora.

Primjerice, za $\texttt{aaa}\cdots\texttt{aab}$ lako je vidjeti da složenost raste na $O(n^2)$.

Algoritam postaje manje učinkovit kad string sadrži više uzastopnih ponavljanja podstringova. Razmotrimo kako optimizirati taj postupak.

## Algoritam minimalne reprezentacije

### Osnovna ideja

Promotrimo dva stringa $A,B$ koji u izvornom stringu $S$ počinju na pozicijama $i,j$ i imaju jednakih prvih $k$ znakova, odnosno

$$
S[i \cdots i+k-1]=S[j \cdots j+k-1]
$$

Najprije razmotrimo slučaj $S[i+k]>S[j+k]$. Nijedan string s početnim indeksom $l$ za koji vrijedi $i\le l\le i+k$ ne može biti odgovor. Naime, za svaki string $S_{i+p}$ (string koji počinje na $i+p$, gdje je $p \in [0, k]$) postoji bolji string $S_{j+p}$.

Zato pri uspoređivanju možemo preskočiti indekse $l\in [i,i+k]$ i izravno uspoređivati $S_{i+k+1}$.

Time smo optimizirali prethodno grubo pretraživanje.

### Vremenska složenost

$O(n)$

### Postupak

1.  Postavimo pokazivač $i$ na $0$, a $j$ na $1$; duljinu podudaranja $k$ postavimo na $0$.
2.  Usporedimo znakove na pomaku $k$ i prema rezultatu pomaknemo odgovarajući pokazivač. Ako pokazivači nakon pomicanja postanu jednaki, jedan proizvoljno povećamo za jedan kako bismo uspoređivali različite stringove.
3.  Ponavljamo postupak dok uspoređivanje ne završi.
4.  Odgovor je manji od $i,j$.

### Implementacija

=== "C++"
    ```cpp
    int k = 0, i = 0, j = 1;
    while (k < n && i < n && j < n) {
      if (sec[(i + k) % n] == sec[(j + k) % n]) {
        k++;
      } else {
        sec[(i + k) % n] > sec[(j + k) % n] ? i = i + k + 1 : j = j + k + 1;
        if (i == j) i++;
        k = 0;
      }
    }
    i = min(i, j);
    ```

=== "Python"
    ```python
    k, i, j = 0, 0, 1
    while k < n and i < n and j < n:
        if sec[(i + k) % n] == sec[(j + k) % n]:
            k += 1
        else:
            if sec[(i + k) % n] > sec[(j + k) % n]:
                i = i + k + 1
            else:
                j = j + k + 1
            if i == j:
                i += 1
            k = 0
    i = min(i, j)
    ```
