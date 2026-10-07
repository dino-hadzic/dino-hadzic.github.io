---
title: Backtracking
---

Ova stranica kratko predstavlja pojam backtrackinga i njegovu primjenu.

## Uvod

Backtracking (povratno pretraživanje) tehnika je koja se često koristi u [pretraživanju u dubinu (DFS)](./dfs.md) i [pretraživanju u širinu (BFS)](./bfs.md).

Njegova je bit: ako ne možeš dalje, vrati se.

## Postupak

1.  Izgradi stablo prostora stanja;

2.  obiđi ga;

3.  kad naiđeš na rubni uvjet, ne pretražuj dalje u dubinu, nego prijeđi na drugu granu;

4.  kad je ciljni uvjet dosegnut, ispiši rezultat.

## Primjeri

???+ example "[USACO 1.5.4 Checker Challenge](https://www.luogu.com.cn/problem/P1219)"
    Zadana je šahovska ploča $6 \times 6$ kao dolje, na koju je postavljeno šest figura tako da se u svakom retku, svakom stupcu i na svakoj dijagonali (uključujući sve dijagonale usporedne s dvjema glavnima) nalazi najviše jedna figura.
    
    ```plain
    0   1   2   3   4   5   6
      -------------------------
    1 |   | O |   |   |   |   |
      -------------------------
    2 |   |   |   | O |   |   |
      -------------------------
    3 |   |   |   |   |   | O |
      -------------------------
    4 | O |   |   |   |   |   |
      -------------------------
    5 |   |   | O |   |   |   |
      -------------------------
    6 |   |   |   |   | O |   |
      -------------------------
    ```
    
    Gornji raspored može se opisati nizom $\{2,4,6,1,3,5\}$: $i$-ti broj znači da se u $i$-tom retku figura nalazi u stupcu $a_i$, kako je prikazano dolje.
    
    Redak $i$: $\{1,2,3,4,5,6\}$
    
    Stupac $a_i$: $\{2,4,6,1,3,5\}$
    
    To je samo jedan od načina postavljanja figura. Napišite program koji pronalazi sve rasporede i ispisuje ih gore opisanim nizovima, u leksikografskom poretku. Treba ispisati samo prva $3$ rješenja, a u posljednjem retku ukupan broj rješenja. Posebno pripazite: program treba optimizirati da bude učinkovit i za veće ploče.

??? note "Primjer rješenja"
    ```cpp
    --8<-- "docs/search/code/backtracking/backtracking_1.cpp"
    ```

???+ example "[Labirint](https://www.luogu.com.cn/problem/P1605)"
    Zadan je labirint dimenzija $N \times M$ s $T$ prepreka; kroz prepreke se ne može proći. Zadane su koordinate početka i cilja, a svako polje smije se posjetiti najviše jednom. Koliko ima načina da se od početka dođe do cilja? U labirintu se kreće na četiri načina: gore, dolje, lijevo i desno, svaki put za jedno polje. Zajamčeno je da na početnom polju nema prepreke.

??? note "Primjer rješenja"
    ```cpp
    --8<-- "docs/search/code/backtracking/backtracking_2.cpp"
    ```
