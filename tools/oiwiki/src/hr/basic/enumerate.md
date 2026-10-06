---
title: Nabrajanje
---

Ova stranica kratko predstavlja nabrajanje (enumeraciju).

## Uvod

**Nabrajanje** (enumerate) strategija je rješavanja problema u kojoj odgovor pogađamo na temelju postojećeg znanja.

Ideja nabrajanja je neprestano pogađati: iz skupa mogućnosti redom isprobavati jednu po jednu i zatim provjeriti je li uvjet zadatka ispunjen.

## Ključne točke

### Odredi prostor rješenja

Izgradi sažet matematički model.

Pri nabrajanju treba jasno znati: koji su mogući slučajevi? Koje elemente treba nabrajati?

### Smanji prostor nabrajanja

Koji je raspon nabrajanja? Treba li zaista nabrojati sve?

Pri rješavanju nabrajanjem o ta dva pitanja treba dobro promisliti, inače dolazi do nepotrebnog utroška vremena.

### Odaberi prikladan redoslijed nabrajanja

Ovisi o zadatku. Primjerice, ako zadatak traži najveći prost broj koji zadovoljava uvjet, prirodno je nabrajati od većih prema manjima.

## Primjer

Slijedi primjer rješavanja nabrajanjem i optimiranja raspona nabrajanja.

??? note "Primjer"
    Zadan je niz čiji su elementi međusobno različiti i različiti od $0$. Odredi broj uređenih parova elemenata niza čiji je zbroj $0$.

??? note "Ideja rješenja"
    Kôd koji nabraja dva broja lako je napisati.
    
    === "C++"
        ```cpp
        for (int i = 0; i < n; ++i)
          for (int j = 0; j < n; ++j)
            if (a[i] + a[j] == 0) ++ans;
        ```
    
    === "Python"
        ```python
        for i in range(n):
            for j in range(n):
                if a[i] + a[j] == 0:
                    ans += 1
        ```
    
    === "Java"
        ```java
        for (int i = 0; i < n; ++i)
          for (int j = 0; j < n; ++j)
            if (a[i] + a[j] == 0) ++ans;
        ```
    
    Pogledajmo kako smanjiti raspon nabrajanja. Ako $(a_i,a_j)$ zadovoljava uvjet, zadovoljava ga i $(a_j,a_i)$; a budući da nijedan element nije $0$, uvjet povlači $i\ne j$. Zato možemo nabrajati samo $j<i$, tako da se svaki neuređeni par broji jednom, i rezultat pomnožiti s $2$ da dobijemo broj uređenih parova. Kôd:
    
    === "C++"
        ```cpp
        for (int i = 0; i < n; ++i)
          for (int j = 0; j < i; ++j)
            if (a[i] + a[j] == 0) ++ans;
        ans *= 2;
        ```
    
    === "Python"
        ```python
        for i in range(n):
            for j in range(i):
                if a[i] + a[j] == 0:
                    ans += 1
        ans *= 2
        ```
    
    === "Java"
        ```java
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < i; ++j)
                if (a[i] + a[j] == 0) ++ans;
        ans *= 2;
        ```
    
    Lako se vidi da je raspon nabrajanja za $j$ smanjen, pa je i vrijeme izvođenja manje.
    
    Možemo ići i korak dalje.
    
    Moramo li zaista nabrajati oba broja? Kad odaberemo jedan broj, uvjet zadatka već određuje što drugi element (drugi broj) mora zadovoljavati; ako nađemo način da izravno provjerimo postoji li traženi broj, uštedjet ćemo vrijeme nabrajanja drugog broja. Naprednije, ako ograničenja to dopuštaju, možemo košarom (bucket)[^1] bilježiti brojeve koje smo već vidjeli.
    
    === "C++"
        ```cpp
        --8<-- "docs/basic/code/enumerate/enumerate_1.cpp"
        ```
    
    === "Python"
        ```python
        met = [False] * (MAXN * 2 + 1)
        for i in range(n):
            if met[MAXN - a[i]]:
                ans += 1
            met[a[i] + MAXN] = True
        ans *= 2
        ```
    
    === "Java"
        ```java
        boolean[] met = new boolean[MAXN * 2 + 1];
        for (int i = 0; i < n; ++i) {
            if (met[MAXN - a[i]]) ++ans;
            met[MAXN + a[i]] = true;
        }
        ans *= 2;
        ```

### Analiza složenosti

-   Vremenska složenost: zadatak se rješava jednim prolazom kroz niz $a$, pa je za dovoljno velik $n$ složenost $O(n)$.
-   Prostorna složenost: $O(n+\max\{|x|:x\in a\})$.

## Zadaci za vježbu

-   [2811: Lights Out - OpenJudge](http://bailian.openjudge.cn/practice/2811/)

## Literatura i bilješke

[^1]: [Bucket sort](../basic/bucket-sort.md), [Problem većinskog elementa](../misc/main-element.md#离线算法) i [objašnjenje strukture „bucket” na Stack Overflowu](https://stackoverflow.com/questions/42399355/what-is-a-bucket-or-double-bucket-data-structure) (engleski)
