---
title: Bubble sort
---

Ova stranica kratko predstavlja bubble sort (sortiranje mjehuričastim postupkom).

## Definicija

**Bubble sort** (sortiranje mjehuričastim postupkom) jednostavan je algoritam sortiranja. Ime je dobio po tome što tijekom izvođenja algoritma manji elementi poput mjehurića polako „isplivavaju” prema vrhu niza.

## Postupak

Algoritam radi tako da u svakom koraku provjerava dva susjedna elementa; ako prvi i drugi element ne zadovoljavaju zadani uvjet poretka, zamijeni ih. Kad više nema susjednih elemenata koje treba zamijeniti, sortiranje je gotovo.

Nakon $i$ prolaza posljednjih $i$ elemenata niza nužno je $i$ najvećih, pa je $n-1$ prolaza dovoljno da niz bude sortiran.

## Svojstva

### Stabilnost

Bubble sort je stabilan algoritam sortiranja.

### Vremenska složenost

Ako je niz već potpuno sortiran, bubble sort treba samo jedan prolaz kroz niz bez ijedne zamjene, pa je vremenska složenost $O(n)$.

U najgorem slučaju bubble sort izvodi $\dfrac{(n-1)n}{2}$ zamjena, pa je vremenska složenost $O(n^2)$.

Prosječna vremenska složenost bubble sorta je $O(n^2)$.

## Implementacija

### Pseudokod

$$
\begin{array}{ll}
1 & \textbf{Input. } \text{An array } A \text{ consisting of }n\text{ elements.} \\
2 & \textbf{Output. } A\text{ will be sorted in nondecreasing order stably.} \\
3 & \textbf{Method. }  \\
4 & \textit{flag}\gets \mathrm{True}\\
5 & \textbf{while }\textit{flag}\\
6 & \qquad \textit{flag}\gets \mathrm{False}\\
7 & \qquad\textbf{for }i\gets1\textbf{ to }n-1\\
8 & \qquad\qquad\textbf{if }A[i]>A[i + 1]\\
9 & \qquad\qquad\qquad \textit{flag}\gets \mathrm{True}\\
10 & \qquad\qquad\qquad \text{Swap } A[i]\text{ and }A[i + 1]
\end{array}
$$

=== "C++"
    ```cpp
    --8<-- "docs/basic/code/bubble-sort/bubble-sort_1.cpp"
    ```

=== "Python"
    ```python
    --8<-- "docs/basic/code/bubble-sort/bubble-sort_1.py:core"
    ```

=== "Java"
    ```java
    // Pretpostavljamo da je veličina niza n + 1; bubble sort kreće od indeksa 1
    static void bubble_sort(int[] a, int n) {
        boolean flag = true;
        while (flag) {
            flag = false;
            for (int i = 1; i < n; i++) {
                if (a[i] > a[i + 1]) {
                    flag = true;
                    int t = a[i];
                    a[i] = a[i + 1];
                    a[i + 1] = t;
                }
            }
        }
    }
    ```
