---
title: Selection sort
---

Ova stranica kratko predstavlja selection sort (sortiranje odabirom).

## Definicija

**Selection sort** (sortiranje odabirom) jednostavan je i intuitivan algoritam sortiranja. Radi tako da u svakom koraku pronađe $i$-ti najmanji element (tj. najmanji element među $A_{i..n}$) i zamijeni ga s elementom na $i$-tom mjestu niza.

![primjer animacije selection sorta](images/selection-sort-animate.svg)

## Svojstva

### Stabilnost

Stabilnost selection sorta ovisi o konkretnoj implementaciji.

Ako se implementira vezanom listom, budući da su umetanje i brisanje na bilo kojem mjestu vezane liste $O(1)$, nije potrebna operacija swap (zamjena dvaju elemenata): u svakom koraku iz nesortiranog dijela odaberemo najmanji element (ako ih je više, prvi od njih) i umetnemo ga ispred prvog elementa nesortiranog dijela, čime je stabilnost osigurana.

Implementacija nad nizom obično koristi `swap` da bi najmanji element premjestila u sortirani dio i tako smanjila broj pomicanja, pa je nestabilna.

Sve implementacije u nastavku temelje se na zamjeni elemenata niza i stoga su **nestabilne**.

### Vremenska složenost

Najbolja, prosječna i najgora vremenska složenost selection sorta jednake su $O(n^2)$.

## Implementacija

### Pseudokod

$$
\begin{array}{ll}
1 & \textbf{Input. } \text{An array } A \text{ consisting of }n\text{ elements.} \\
2 & \textbf{Output. } A\text{ will be sorted in nondecreasing order.} \\
3 & \textbf{Method. }  \\
4 & \textbf{for } i\gets 1\textbf{ to }n-1\\
5 & \qquad \textit{ith}\gets i\\
6 & \qquad \textbf{for }j\gets i+1\textbf{ to }n\\
7 & \qquad\qquad\textbf{if }A[j]<A[\textit{ith}]\\
8 & \qquad\qquad\qquad \textit{ith}\gets j\\
9 & \qquad \text{swap }A[i]\text{ and }A[\textit{ith}]\\
\end{array}
$$

=== "C++"
    ```cpp
    --8<-- "docs/basic/code/selection-sort/selection-sort_1.cpp"
    ```

=== "Python"
    ```python
    --8<-- "docs/basic/code/selection-sort/selection-sort_1.py:core"
    ```

=== "Java"
    ```java
    // indeksi niza arr počinju od 1
    static void selection_sort(int[] arr, int n) {
        for (int i = 1; i < n; i++) {
            int ith = i;
            for (int j = i + 1; j <= n; j++) {
                if (arr[j] < arr[ith]) {
                    ith = j;
                }
            }
            // swap
            int temp = arr[i];
            arr[i] = arr[ith];
            arr[ith] = temp;
        }
    }
    ```
