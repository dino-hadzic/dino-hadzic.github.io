---
title: Heap sort
---

Ova stranica kratko predstavlja heap sort (sortiranje hrpom).

## Definicija

**Heap sort** (sortiranje hrpom) algoritam je sortiranja oblikovan pomoću strukture podataka [binarna hrpa](../ds/binary-heap.md) (binary heap). Struktura podataka na koju se heap sort primjenjuje je niz.

## Postupak

Heap sort je u biti selection sort izgrađen nad hrpom.

### Sortiranje

Najprije izgradimo max-hrpu, zatim uzmemo element s vrha hrpe kao najveći, zamijenimo ga s elementom na kraju niza i uspostavimo svojstvo hrpe na ostatku;

potom uzmemo element s vrha hrpe kao drugi najveći, zamijenimo ga s predzadnjim elementom niza i opet uspostavimo svojstvo hrpe na ostatku;

i tako dalje – nakon $n-1$ operacija cijeli je niz sortiran.

### Izgradnja binarne hrpe nad nizom

Počevši od korijena, čvorove razine po razini slažemo u niz.

Tako čvor s indeksom `i` u nizu ima roditelja, lijevo dijete i desno dijete kako slijedi:

```cpp
iParent(i) = (i - 1) / 2;
iLeftChild(i) = 2 * i + 1;
iRightChild(i) = 2 * i + 2;
```

## Svojstva

### Stabilnost

Kao i kod selection sorta, zamjene u heap sortu mogu promijeniti relativni poredak jednakih elemenata, pa je to nestabilan algoritam sortiranja.

### Vremenska složenost

Najgora vremenska složenost heap sorta je $O(n\log n)$.

### Prostorna složenost

Budući da se hrpa može izgraditi izravno nad ulaznim nizom, ovo je algoritam u mjestu (in-place).

## Implementacija

=== "C++"
    ```cpp
    --8<-- "docs/basic/code/heap-sort/heap-sort_1.cpp:sort"
    ```

=== "Python"
    ```python
    --8<-- "docs/basic/code/heap-sort/heap-sort_1.py:sort"
    ```

## Vanjske poveznice

-   [Heapsort – Wikipedia](https://en.wikipedia.org/wiki/Heapsort)
