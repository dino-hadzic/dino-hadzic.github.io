---
title: Uvod u sortiranje
---

Ova stranica kratko predstavlja algoritme sortiranja.

## Definicija

**Algoritam sortiranja** (sorting algorithm) je algoritam koji skup zadanih podataka poredava prema nekom poretku. Algoritama sortiranja ima mnogo i njihova se svojstva uvelike razlikuju.

## Svojstva

### Stabilnost

Stabilnost označava mijenja li se nakon sortiranja relativni poredak jednakih elemenata.

Stabilan algoritam zadržava relativni redoslijed zapisa s jednakim ključevima: ako je algoritam sortiranja stabilan i postoje dva zapisa $R$ i $S$ s jednakim ključem, pri čemu se u izvornom nizu $R$ pojavljuje prije $S$, tada će i u sortiranom nizu $R$ biti prije $S$.

Radix sort, counting sort, insertion sort, bubble sort i merge sort stabilni su algoritmi sortiranja.

Selection sort, heap sort, quick sort i shell sort nisu stabilni.

### Vremenska složenost

Glavna stranica: [Složenost](./complexity.md)

Vremenska složenost opisuje odnos između vremena izvođenja algoritma i veličine ulaza, a obično se zapisuje notacijom $O$.

Složenost se najčešće jednostavno računa brojanjem izvršenih „elementarnih operacija”, a ponekad se može približno procijeniti i brojanjem razina ugniježđenih petlji.

Vremenska složenost dijeli se na najbolju, prosječnu i najgoru. Na natjecanjima iz informatike (OI) obično se razmatra najgora složenost, jer ona predstavlja donju granicu brzine algoritma – pri ocjenjivanju se ne može dogoditi ništa lošije od toga.

Svaki algoritam sortiranja temeljen na usporedbama u najgorem slučaju treba $\Omega(n\log n)$ usporedbi da bi sortirao $n$ međusobno različitih elemenata.

Naravno, postoje i algoritmi koji nisu $O(n\log n)$. Primjerice, vremenska složenost [counting sorta](./counting-sort.md) je $O(n+w)$, gdje $w$ označava veličinu raspona vrijednosti ulaznih podataka.

Slijedi usporedba nekoliko algoritama sortiranja.

![Usporedba nekoliko algoritama sortiranja](images/sort-intro-1.apng)

### Prostorna složenost

Slično vremenskoj složenosti, prostorna složenost opisuje količinu memorije koju algoritam troši. Općenito, što je prostorna složenost manja, to je algoritam bolji.

## Vanjske poveznice

-   [Sorting algorithm – Wikipedia](https://en.wikipedia.org/wiki/Sorting_algorithm)
