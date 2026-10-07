---
title: Algoritmi za traženje najveće klike
---

Preduvjeti: [klika](./concept.md)

## Uvod

U računarstvu, problem klike odnosi se na računski problem pronalaženja klike (podskupa vrhova koji su svi međusobno susjedni, tj. potpunog podgrafa) u zadanom grafu.

Problem klike pojavljuje se i u stvarnom životu. Promotrimo, na primjer, društvenu mrežu u kojoj vrhovi grafa predstavljaju korisnike, a bridovi znače da se dva povezana korisnika poznaju. Kad pronađemo kliku, pronašli smo skupinu ljudi koji se svi međusobno poznaju.

Ako želimo pronaći najveću skupinu ljudi u toj mreži koji se svi međusobno poznaju, trebamo algoritam za traženje najveće klike.

Već smo uveli pojam [maksimalne klike](./concept.md); najveća klika (maximum clique) je maksimalna klika s najvećim brojem vrhova.

## Objašnjenje

Ideja je koristiti rekurziju i backtracking: vrhove čuvamo u listi i pri svakom dodavanju vrha provjeravamo tvore li odabrani vrhovi i dalje kliku. Ako nakon dodavanja vrha skup više nije klika, vraćamo se na položaj koji zadovoljava uvjet i pokušavamo dodati drugi vrh.

Backtracking koristimo zato što ne znamo je li neki vrh $v$ **na kraju** član najveće klike. Ako rekurzivni algoritam odabere $v$ kao član najveće klike, a najveću kliku ne nađe, treba se vratiti i potražiti rješenje bez $v$.

## Postupak

**Bron–Kerboschov** algoritam optimizirana je izvedba te ideje. Njegov osnovni oblik rekurzivno pretražuje pomoću triju skupova: $R$, $P$ i $X$. Koraci su sljedeći:

1.  Skupove $R,X$ inicijaliziramo kao prazne, a skup $P$ kao skup svih vrhova grafa.
2.  Svaki put iz skupa $P$ uzimamo vrh $v$; kad u skupu više nema vrhova, postoje dva slučaja:
    1.  skup $R$ je maksimalna klika, a skup $X$ je prazan,
    2.  nema maksimalne klike, pa se vraćamo (backtracking).
3.  Za svaki vrh $v$ uzet iz skupa $P$ radimo sljedeće:
    1.  dodamo vrh $v$ u skup $R$, zatim rekurzivno obradimo skupove $R,P,X$,
    2.  izbrišemo vrh $v$ iz skupa $P$ i dodamo ga u skup $X$,
    3.  ako su skupovi $P,X$ oba prazni, skup $R$ je maksimalna klika.

Metoda se može dodatno optimizirati. Da bismo uštedjeli vrijeme i omogućili brže vraćanje, pretragu možemo voditi pomoću stožernog vrha (pivot vertex). Druga je ideja na početku sortirati sve vrhove i pri nabrajanju ići redom po indeksima kako bi se izbjegla ponavljanja.

## Implementacija

### Pseudokod

```text
R := {}
P := node set of G 
X := {}

BronKerbosch1(R, P, X):
    if P and X are both empty:
        report R as a maximal clique
    for each vertex v in P:
        BronKerbosch1(R ⋃ {v}, P ⋂ N(v), X ⋂ N(v))
        P := P \ {v}
        X := X ⋃ {v}
```

### Implementacija u C++-u

??? note "Kôd implementacije"
    ```cpp
    --8<-- "docs/graph/code/max-clique/max-clique_1.cpp"
    ```

## Primjer zadatka

???+ note "[POJ 2989: All Friends](http://poj.org/problem?id=2989)"
    Sažetak zadatka: zadano je $n$ ljudi među kojima je $m$ parova prijatelja; odredite broj maksimalnih klika.

Ideja: tipičan zadatak za Bron–Kerboschov algoritam.

Pseudokod:

```text
 BronKerbosch(All, Some, None):  
     if Some and None are both empty:  
         report All as a maximal clique // svi su vrhovi odabrani i nema vrhova koji se ne smiju odabrati, uvećaj odgovor  
     for each vertex v in Some: // prolazimo svaki element skupa Some  
         BronKerbosch1(All ⋃ {v}, Some ⋂ N(v), None ⋂ N(v))   
         // dodajemo v u All; očito samo prijatelji od v mogu biti kandidati, a iz None utjecaj imaju samo prijatelji od v  
         Some := Some - {v} // već obrađen, brišemo iz Some i dodajemo u None  
         None := None ⋃ {v} 
```

Da bismo uštedjeli vrijeme i omogućili brže vraćanje, algoritam možemo optimizirati izborom stožernog vrha (pivot vertex) $v$.

Znamo da gornji algoritam nužno mnogo puta ponovno računa već pronađene maksimalne klike i zatim se vraća.

Uzmimo za primjer prije spomenute skupove $R$, $P$ i $X$:

Promotrimo sljedeće: uzmemo li vrh $u$ iz skupa $P\cup X$, da bi se s $R$ dobila maksimalna klika, odabrani vrh nužno je neki vrh iz $P\cap N(u)$ ($N(u)$ označava skup susjeda od $u$).

Ako nakon što uzmemo $u$ možemo u maksimalnu kliku dodati i njegov susjed $v$, dovoljno je uzeti samo $u$. Tako smanjujemo kasnije ponovljeno računanje za $v$. Nakon toga uzimamo samo vrhove koji nisu susjedni s $u$.

Implementacija u C++-u s ovom optimizacijom:

??? note "Kôd implementacije"
    ```cpp
    --8<-- "docs/graph/code/max-clique/max-clique_2.cpp"
    ```

## Zadaci za vježbu

-   [ZOJ 1492 Maximum Clique](https://pintia.cn/problem-sets/91827364500/exam/problems/type/7?page=4&problemSetProblemId=91827364991)
-   [POJ 1419 Najveća klika neusmjerenog grafa](http://poj.org/problem?id=1419)
-   [POJ 1129 Radiopostaje](http://poj.org/problem?id=1129)

## Literatura

-   [Clique problem – Wikipedia](https://en.wikipedia.org/wiki/Clique_problem)
-   [Maksimalne i najveće klike neusmjerenog grafa (Bron–Kerboschov algoritam)](https://blog.csdn.net/yo_bc/article/details/77453478)
-   [Problem najveće klike – Bron–Kerboschov algoritam](https://hallelujahjeff.github.io/2018/04/12/34/)
-   [Problem najveće klike](https://www.cnblogs.com/zhj5chengfeng/archive/2013/07/29/3224092.html)
