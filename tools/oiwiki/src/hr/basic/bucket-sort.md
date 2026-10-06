---
title: Bucket sort
---

Ova stranica kratko predstavlja bucket sort (sortiranje u košare).

## Definicija

**Bucket sort** (sortiranje u košare) algoritam je sortiranja pogodan za slučaj kad je raspon vrijednosti podataka velik, ali su vrijednosti raspodijeljene prilično ravnomjerno.

## Postupak

Bucket sort radi u sljedećim koracima:

1.  pripremi niz unaprijed zadanog broja praznih košara;
2.  prođi nizom i svaki element stavi u odgovarajuću košaru;
3.  sortiraj svaku nepraznu košaru;
4.  iz nepraznih košara redom vrati elemente u izvorni niz.

## Svojstva

### Stabilnost

Ako se za sortiranje unutar košara koristi stabilan algoritam i ako se pri stavljanju elemenata u košare ne mijenja njihov relativni poredak, bucket sort je stabilan algoritam sortiranja.

Budući da u svakoj košari nema mnogo elemenata, unutar košara se obično koristi insertion sort. Tada je bucket sort stabilan.

### Vremenska složenost

Neka je $n$ broj elemenata i $k$ broj košara. Ako elementi padaju u košare nezavisno i ravnomjerno, prosječna vremenska složenost bucket sorta je $O(n + n^2/k + k)$ (podjela raspona vrijednosti na $k$ jednakih dijelova + sortiranje + ponovno spajanje elemenata), što je za $k\approx n$ jednako $O(n)$.[^ref1]

Najgora vremenska složenost bucket sorta je $O(n^2+k)$.

## Implementacija

U nastavku indeksi niza `a[]` počinju od $1$ i zahtijeva se $0\le a_i\le w$ i $0\le n<N$, gdje je $w$ gornja granica najvećeg ključa.

=== "C++"
    ```cpp
    --8<-- "docs/basic/code/bucket-sort/bucket-sort_1.cpp:sort"
    ```

=== "Python"
    ```python
    --8<-- "docs/basic/code/bucket-sort/bucket-sort_1.py:sort"
    ```

## Literatura i bilješke

[^ref1]: [Bucket sort - Wikipedia](https://en.wikipedia.org/wiki/Bucket_sort#Average-case_analysis)
