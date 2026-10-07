---
title: Tournament sort
---

Ova stranica kratko predstavlja tournament sort (turnirsko sortiranje).

## Definicija

**Tournament sort** (turnirsko sortiranje), poznat i kao selection sort stablom, poboljšana je inačica [selection sorta](./selection-sort.md) i varijanta [heap sorta](./heap-sort.md) (oba koriste potpuno binarno stablo). Nadograđuje selection sort tako da sljedeći element koji treba odabrati pronalazi pomoću prioritetnog reda.

## Uvod

Tournament sort ime je dobio po natjecanjima s jednostrukom eliminacijom. U takvom sustavu natjecanja sudjeluje mnogo igrača; uspoređuju se u parovima, a pobjednik prolazi u sljedeći krug. Taj način eliminacije određuje najboljeg igrača, ali igrač izbačen u posljednjem krugu nije nužno drugi najbolji – može biti slabiji od nekog ranije izbačenog igrača.

## Postupak

Za primjer uzmimo **turnirsko stablo za minimum**:

![tournament-sort1](./images/tournament-sort1.svg)

Elementi koje treba sortirati prikazani su u listovima. Crveni bridovi označavaju put pobjednika – manjeg elementa u svakom krugu usporedbi. Očito se jednim „turnirom” među skupom elemenata može izabrati najmanji.

Nakon svakog kruga usporedbi među $n$ elemenata dobivamo $\left\lceil\dfrac{n}{2}\right\rceil$ „pobjednika”; manji element svakog para ulazi u sljedeći krug. Ako neki element ne može dobiti par, izravno prelazi u sljedeći krug.

![tournament-sort2](./images/tournament-sort2.svg)

Nakon završenog „turnira” izabrani element treba ukloniti. Jednostavno ga postavimo na $\infty$ (operacija slična onoj u [heap sortu](./heap-sort.md)), pa ponovno odigramo „turnir” kako bismo odabrali drugi najmanji element.

Postupak se ponavlja dok svi elementi nisu sortirani.

## Svojstva

### Stabilnost

Tournament sort je nestabilan algoritam sortiranja.

### Vremenska složenost

Najbolja, prosječna i najgora vremenska složenost tournament sorta jednake su $O(n\log n)$. „Turnir” se inicijalizira u vremenu $O(n)$, a potom se od $n$ elemenata jedan odabire u vremenu $O(\log n)$.

### Prostorna složenost

Prostorna složenost tournament sorta je $O(n)$.

## Implementacija

=== "C++"
    ```cpp
    --8<-- "docs/basic/code/tournament-sort/tournament-sort_1.cpp:sort"
    ```

=== "Python"
    ```python
    --8<-- "docs/basic/code/tournament-sort/tournament-sort_1.py:sort"
    ```

## Vanjske poveznice

-   [Tournament sort - Wikipedia](https://en.wikipedia.org/wiki/Tournament_sort)
