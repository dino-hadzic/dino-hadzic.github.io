---
title: A*
---

Ova stranica predstavlja algoritam pretraživanja A\*.

Algoritam pretraživanja A\* (A\* search algorithm, čita se „A-star”), kraće algoritam A\*, algoritam je za nalaženje najkraćeg puta između zadanog početnog i ciljnog vrha u težinskom usmjerenom grafu. Pripada obilascima grafa (graph traversal) i algoritmima pretraživanja „najbolji prvi” (best-first search), a ujedno je poboljšanje [BFS-a](./bfs.md).

## Postupak

Cilj je algoritma A\* pronaći najkraći put od početnog vrha $s$ do ciljnog vrha $t$ u usmjerenom grafu. Neka je $d(x,y)$ udaljenost između vrhova $x$ i $y$, tj. duljina najkraćeg puta među njima. Označimo s $g(x)=d(s,x)$ funkciju udaljenosti od početnog vrha $s$ do vrha $x$, s $h^*(x)$ funkciju udaljenosti od vrha $x$ do ciljnog vrha $t$, a s $h(x)$ procjenu za $h^*(x)$[^note1]. Naposljetku, procjenu duljine najkraćeg puta od $s$ preko $x$ do $t$ označimo s

$$
f(x) = g(x) + h(x).
$$

Tijekom pretrage algoritam A\* svaki put iz prioritetnog reda uzima vrh s najmanjim $f$. Zatim sve njegove sljedbenike $x$ stavlja u prioritetni red i pomoću stvarno zabilježenog $g(x)$ i procijenjenog $h(x)$ ažurira $f(x)$.

## Svojstva

Budući da stvarna vrijednost $h^*(x)$ tijekom pretrage nije poznata, kao njezina procjena koristi se lako izračunljiv $h(x)$. Stvarna složenost pretrage A\* ovisi o svojstvima te funkcije procjene $h(x)$. Lako je zamisliti da će, ako je $h\equiv h^*$, tj. ako je procjena točna, pretraga napredovati strogo duž najkraćeg puta. Ako je pak $h\equiv 0$, algoritam A\* degenerira u [Dijkstrin algoritam](./../graph/shortest-path.md#dijkstra-算法); kad je $h\equiv 0$ i sve težine bridova su $1$, to je upravo [BFS](./bfs.md).

Pretpostavimo da graf nema bridova negativne težine. Ako procjena $h(x)$ nikad ne premašuje stvarnu udaljenost $h^*(x)$, tj. $0\le h\le h^*$, algoritam A\* sigurno pronalazi optimalno rješenje. Funkcija procjene $h(x)$ koja zadovoljava taj uvjet zove se **dopustiva** (admissible). Prema prethodnoj raspravi, što je $h$ bliži $h^*$, to je odgovarajući algoritam A\* učinkovitiji. Općenito, u najgorem slučaju algoritam prolazi sve vrhove koji zadovoljavaju

$$
f(x) = g(x) + h(x) \le C^*
$$

gdje je $C^*$ najkraća udaljenost između početnog vrha $s$ i ciljnog vrha $t$. Intuitivno, što je $h$ bliži $h^*$, to pri svakom širenju manje sljedbenika zadovoljava taj uvjet, pa algoritam pretražuje manje grana. Zato se algoritam A\* može promatrati kao optimizacija pretraživanja „rezanjem”.

Ako $h$ nije samo dopustiva nego i **konzistentna** (consistent), tj.

$$
h(x) \le h(y) + d(x, y),
$$

algoritam A\* nikada ne vraća u red vrh koji je već izbačen iz reda. Uvjet konzistentnosti može se shvatiti kao nejednakost trokuta za vrhove $x,y,t$.

## Riješeni primjer

Klasična je primjena algoritma A\* problem k najkraćih puteva. Opis tog problema, rješenje algoritmom A\* i rješenje bolje složenosti pomoću perzistentnih spojivih gomila nalaze se na stranici [Problem k-tog najkraćeg puta](./../graph/kth-path.md).

U ovom odjeljku predstavljamo klasičan zadatak rješiv algoritmom A\*.

???+ example "[Slagalica s osam pločica](https://www.luogu.com.cn/problem/P1379)"
    Na ploči $3\times 3$ nalazi se osam pločica, a na svakoj je jedan od brojeva od $1$ do $8$. Na ploči je jedno prazno polje, označeno s $0$. Pločica susjedna praznom polju može se pomaknuti na njega, pri čemu njezino prijašnje mjesto postaje prazno. Za zadani početni i ciljni raspored (radi jednostavnosti neka je ciljno stanje kao u nastavku) pronađite niz poteza s najmanjim brojem koraka od početnog do ciljnog rasporeda.
    
    $$
    \begin{aligned}
    123\\
    804\\
    765
    \end{aligned}
    $$

??? note "Ideja rješenja"
    Funkciju $h$ možemo definirati kao broj pločica koje nisu na svome mjestu. Lako se vidi da je $h$ i dopustiva i konzistentna, pa se zadatak može riješiti algoritmom A\*.

??? note "Primjer rješenja"
    ```cpp
    --8<-- "docs/search/code/astar/astar_1.cpp"
    ```

## Literatura i bilješke

-   [A\* search algorithm - Wikipedia](https://en.wikipedia.org/wiki/A*_search_algorithm)

[^note1]: Ovdje $h$ dolazi od „heuristic”. Vidi [Heuristic (computer science) - Wikipedia](https://en.wikipedia.org/wiki/Heuristic_(computer_science)) i odjeljak „Bounded relaxation” u [A\* search algorithm - Wikipedia](https://en.wikipedia.org/wiki/A*_search_algorithm#Bounded_relaxation).
