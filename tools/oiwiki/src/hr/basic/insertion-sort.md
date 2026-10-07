---
title: Insertion sort
---

Ova stranica kratko predstavlja insertion sort (sortiranje umetanjem).

## Definicija

**Insertion sort** (sortiranje umetanjem) jednostavan je i intuitivan algoritam sortiranja. Radi tako da elemente koje treba sortirati podijeli na „sortirani” i „nesortirani” dio, pa u svakom koraku iz „nesortiranih” elemenata odabere jedan i umetne ga na ispravno mjesto među „sortirane”.

Ista se operacija događa pri igranju karata: sa stola uzmemo kartu, umetnemo je po vrijednosti među karte u ruci, pa uzmemo sljedeću.

![primjer animacije insertion sorta](images/insertion-sort-animate.svg)

## Svojstva

### Stabilnost

Insertion sort je stabilan algoritam sortiranja.

### Vremenska složenost

Najbolja vremenska složenost insertion sorta je $O(n)$; vrlo je učinkovit kad je niz gotovo sortiran.

Najgora i prosječna vremenska složenost insertion sorta jednake su $O(n^2)$.

## Implementacija

### Pseudokod

$$
\begin{array}{ll}
1 & \textbf{Input. } \text{An array } A \text{ consisting of }n\text{ elements.} \\
2 & \textbf{Output. } A\text{ will be sorted in nondecreasing order stably.} \\
3 & \textbf{Method. }  \\
4 & \textbf{for } i\gets 2\textbf{ to }n\\
5 & \qquad \textit{key}\gets A[i]\\
6 & \qquad j\gets i-1\\
7 & \qquad\textbf{while }j>0\textbf{ and }A[j]>\textit{key}\\
8 & \qquad\qquad A[j + 1]\gets A[j]\\
9 & \qquad\qquad j\gets j - 1\\
10 & \qquad A[j + 1]\gets \textit{key}
\end{array}
$$

=== "C++"
    ```cpp
    --8<-- "docs/basic/code/insertion-sort/insertion-sort_1.cpp"
    ```

=== "Python"
    ```python
    --8<-- "docs/basic/code/insertion-sort/insertion-sort_1.py:core"
    ```

=== "Java"
    ```java
    --8<-- "docs/basic/code/insertion-sort/insertion-sort_1.java"
    ```

## Binarni insertion sort

Insertion sort može se dodatno ubrzati binarnim pretraživanjem; učinak je zamjetan kad je elemenata mnogo.

### Vremenska složenost

Binarni insertion sort mjesto umetanja određuje binarnim pretraživanjem, čime ukupan broj usporedbi pada na $O(n\log n)$, no u najgorem slučaju i dalje treba pomaknuti $\Theta(n^2)$ elemenata, pa je najgora vremenska složenost i dalje $\Theta(n^2)$.

### Implementacija

=== "C++"
    ```cpp
    void insertion_sort(int arr[], int len) {
      if (len < 2) return;
      for (int i = 1; i != len; ++i) {
        int key = arr[i];
        auto index = upper_bound(arr, arr + i, key) - arr;
        // Pomicanje elemenata memmove-om brže je od for petlje; složenost je i dalje O(n)
        memmove(arr + index + 1, arr + index, (i - index) * sizeof(int));
        arr[index] = key;
      }
    }
    ```
