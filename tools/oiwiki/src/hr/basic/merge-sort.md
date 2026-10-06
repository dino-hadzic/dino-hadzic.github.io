---
title: Merge sort
---

Ova stranica predstavlja merge sort (sortiranje spajanjem) i njegovu primjenu na brojanje inverzija.

## Definicija

**Merge sort** ([sortiranje spajanjem](https://en.wikipedia.org/wiki/Merge_sort)) učinkovit je stabilan algoritam sortiranja temeljen na usporedbama.

## Svojstva

Merge sort se temelji na ideji „podijeli pa vladaj”: niz podijeli na dijelove, sortira ih i spoji. Vremenska složenost u najboljem, najgorem i prosječnom slučaju je $\Theta (n \log n)$, a prostorna složenost $\Theta (n)$.

Merge sort može raditi i sa samo $\Theta (1)$ pomoćnog prostora, ali se radi jednostavnosti obično koristi pomoćni niz jednake duljine kao izvorni.

## Postupak

### Spajanje

Središnji dio merge sorta je postupak spajanja (merge): dva sortirana niza `a` i `b` spajaju se u jedan sortirani niz `c`.

Slijeva nadesno prolazimo kroz `a[i]` i `b[j]` i svaki put manji element zapisujemo u `c[k]`; kad jedan niz iscrpimo, preostale elemente drugog niza dodamo na kraj `c`.

Radi stabilnosti sortiranja, kad je prvi element prednjeg dijela manji **ili jednak** prvom elementu stražnjeg dijela (`a[i] <= b[j]`), a ne samo kad je strogo manji (`a[i] < b[j]`), on se kao minimum stavlja u `c[k]`.

#### Implementacija

=== "C/C++"
    === "Nizovima"
        ```cpp
        --8<-- "docs/basic/code/merge-sort/merge-sort_1.cpp:array"
        ```
    
    === "Pokazivačima"
        ```cpp
        --8<-- "docs/basic/code/merge-sort/merge-sort_1.cpp:pointer"
        ```
    
    Može se koristiti i funkcija `std::merge` iz biblioteke `<algorithm>`; upotreba je ista kao u gornjoj inačici s pokazivačima.

=== "Python"
    ```python
    --8<-- "docs/basic/code/merge-sort/merge-sort_1.py:merge"
    ```

### Merge sort metodom „podijeli pa vladaj”

1.  Kad je duljina niza $1$, niz je već sortiran i ne treba ga dalje dijeliti.
2.  Kad je duljina niza veća od $1$, niz vjerojatno nije sortiran. Tada ga podijelimo na dva dijela i za svaki provjerimo je li sortiran (prema prvom pravilu). Ako jesu, spojimo ih u jedan sortirani niz; inače na nesortiranim dijelovima ponovimo drugo pravilo, a zatim spojimo.

Matematičkom indukcijom može se dokazati da ovaj postupak pretvara niz u sortirani niz.

Radi složenosti sortiranja niz se obično dijeli na dva što jednakija dijela ($\textit{mid} = \left\lfloor \dfrac{l + r}{2} \right\rfloor$).

#### Implementacija

Napomena: intervali u kodu u nastavku su redom $[l, r)$, $[l, \textit{mid})$ i $[\textit{mid}, r)$.

=== "C/C++"
    ```cpp
    --8<-- "docs/basic/code/merge-sort/merge-sort_1.cpp:recursive"
    ```

=== "Python"
    ```python
    --8<-- "docs/basic/code/merge-sort/merge-sort_1.py:recursive"
    ```

### Merge sort udvostručavanjem (bottom-up)

Znamo da je niz duljine $1$ već sortiran.

Cijeli niz razrežemo na segmente duljine $1$.

Slijeva nadesno spajamo po dva sortirana segmenta duljine $1$ i dobivamo niz sortiranih segmenata duljine $\le 2$;

slijeva nadesno spajamo po dva sortirana segmenta duljine $\le 2$ i dobivamo niz sortiranih segmenata duljine $\le 4$;

slijeva nadesno spajamo po dva sortirana segmenta duljine $\le 4$ i dobivamo niz sortiranih segmenata duljine $\le 8$;

…

Postupak ponavljamo dok ne ostane samo jedan sortirani segment – to je sortirani izvorni niz.

???+ note "Zašto $\le$, a ne $=$"
    Duljina niza vjerojatno nije oblika $2^x$, pa se na kraju može pojaviti nepotpun segment, a posljednji segment može ostati bez para.

#### Implementacija

=== "C/C++"
    ```cpp
    --8<-- "docs/basic/code/merge-sort/merge-sort_1.cpp:iterative"
    ```

=== "Python"
    ```python
    --8<-- "docs/basic/code/merge-sort/merge-sort_1.py:iterative"
    ```

## Inverzije

Dodatno čitanje i referentna implementacija: [Inverzije](../math/permutation.md#逆序数)

Inverzija je uređeni par $(i, j)$ takav da je $i < j$ i $a_i > a_j$.

Sortirani niz nema inverzija. U postupku spajanja merge sorta, svaki put kad se prvi element stražnjeg dijela uzme kao trenutni minimum, broj preostalih elemenata prednjeg dijela jednak je broju inverzija koje to spajanje uklanja; stoga merge sort broji inverzije u vremenu $\Theta (n \log n)$. Osim toga, inverzije se mogu brojati i Fenwickovim stablom ili segmentnim stablom, također u $O(n \log n)$; detaljno objašnjenje tog algoritma nalazi se u odgovarajućem dijelu poglavlja [Fenwickovo stablo](../ds/fenwick.md#全局逆序对全局二维偏序). Referentne implementacije obaju algoritama nalaze se u poglavlju [Inverzije](../math/permutation.md#逆序数).

## Vanjske poveznice

-   [Merge Sort - GeeksforGeeks](https://www.geeksforgeeks.org/merge-sort/)
-   [Merge sort – Wikipedia](https://en.wikipedia.org/wiki/Merge_sort)
-   [Inversion (discrete mathematics) – Wikipedia](https://en.wikipedia.org/wiki/Inversion_(discrete_mathematics))
