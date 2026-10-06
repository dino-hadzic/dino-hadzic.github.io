---
title: Counting sort
---

Potrebno predznanje: [Prefiksne sume](./prefix-sum.md)

???+ warning "Napomena"
    Ova stranica ne opisuje [**radix sort**](./radix-sort.md).

Ova stranica kratko predstavlja counting sort (sortiranje brojanjem).

## Definicija

**Counting sort** (sortiranje brojanjem) algoritam je sortiranja koji radi u linearnom vremenu.

## Postupak

Counting sort radi tako da koristi dodatni niz $C$, u kojem je $i$-ti element broj elemenata niza $A$ čija je vrijednost jednaka $i$; zatim pomoću niza $C$ elemente niza $A$ raspoređuje na ispravna mjesta.[^ref1]

Postupak se sastoji od tri koraka:

1.  izbroji koliko se puta pojavljuje svaki broj;
2.  izračunaj [prefiksne sume](./prefix-sum.md) broja pojavljivanja;
3.  pomoću prefiksnih suma pojavljivanja, zdesna nalijevo, odredi rang svakog broja.

### Zašto se računaju prefiksne sume

Rekonstrukcija prema frekvencijama može sortirati čiste ključeve i obraditi duplikate; ali ako treba stabilno preurediti izvorne zapise, položaj u izlazu određuje se prefiksnim sumama frekvencija.

Računajući prefiksnu sumu svakog člana dodatnog niza $C$ i kombinirajući je s vrijednošću člana, svakom od jednakih elemenata možemo dodijeliti jedinstven rang:

vrijednost člana niza $C$ jednaka je broju ponavljanja tog ključa, a njegova prefiksna suma jednaka je rangu posljednjeg od tih jednakih elemenata.

Ako elemente raspoređujemo u obrnutom redoslijedu niza $A$, sortirani niz očito zadržava izvorni poredak niza $A$ (za jednake ključeve), tj. dobivamo stabilan algoritam sortiranja.

![primjer animacije counting sorta](images/counting-sort-animate.svg)

## Svojstva

### Stabilnost

Counting sort je stabilan algoritam sortiranja.

### Vremenska složenost

Vremenska složenost counting sorta je $O(n+w)$, gdje $w$ označava veličinu raspona vrijednosti podataka koji se sortiraju.

## Implementacija

### Pseudokod

$$
\begin{array}{ll}
1 & \textbf{Input. } \text{An array } A \text{ consisting of }n\text{ positive integers no greater than } w. \\
2 & \textbf{Output. } \text{Array }A\text{ after sorting in nondecreasing order stably.} \\
3 & \textbf{Method. }  \\
4 & \textbf{for }i\gets0\textbf{ to }w\\
5 & \qquad \textit{cnt}[i]\gets0\\
6 & \textbf{for }i\gets1\textbf{ to }n\\
7 & \qquad \textit{cnt}[A[i]]\gets\textit{cnt}[A[i]]+1\\
8 & \textbf{for }i\gets1\textbf{ to }w\\
9 & \qquad \textit{cnt}[i]\gets \textit{cnt}[i]+\textit{cnt}[i-1]\\
10 & \textbf{for }i\gets n\textbf{ downto }1\\
11 & \qquad B[\textit{cnt}[A[i]]]\gets A[i]\\
12 & \qquad \textit{cnt}[A[i]]\gets \textit{cnt}[A[i]]-1\\
13 & \textbf{return } B
\end{array}
$$

=== "C++"
    ```cpp
    --8<-- "docs/basic/code/counting-sort/counting-sort_1.cpp"
    ```

=== "Python"
    ```python
    --8<-- "docs/basic/code/counting-sort/counting-sort_1.py:core"
    ```

## Literatura i bilješke

[^ref1]: [Counting sort – Wikipedia](https://en.wikipedia.org/wiki/Counting_sort)
