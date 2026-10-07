---
title: Bipartitni grafovi
---

## Uvod

Bipartitni graf (bipartite graph), zvan i dvodijelni graf, vrsta je grafa posebne strukture. Njegov se skup vrhova može podijeliti na dva disjunktna podskupa tako da svaki brid grafa spaja par vrhova iz različitih skupova, a nikad dva vrha iz istog skupa.

Zahvaljujući toj jednostavnoj strukturi, bipartitni grafovi ne samo da imaju mnoga elegantna svojstva, nego se i široko koriste za modeliranje stvarnih situacija, npr. raspodjele zadataka, sustava preporuka, tržišta uparivanja i sl. Mnogi optimizacijski problemi koji su teški na općim grafovima na bipartitnim se grafovima mogu riješiti učinkovito i točno.

## Definicija

Ako se skup vrhova $V$ grafa $G=(V,E)$ može podijeliti na dva disjunktna podskupa $X$ i $Y$ tako da krajevi svakog brida $e\in E$ pripadaju jedan skupu $X$, a drugi skupu $Y$, graf $G$ zovemo **bipartitnim grafom** (bipartite graph). Skupovi $X$ i $Y$ često se zovu njegova dva **dijela** (part), odnosno lijeva i desna strana bipartitnog grafa. Kad su dijelovi $X$ i $Y$ poznati, bipartitni graf $G$ možemo zapisati i kao trojku $(X, Y, E)$.

Tipičan bipartitni graf prikazan je na slici.

![](./images/bi-graph-1.svg)

Stabla, parni ciklusi, mrežasti grafovi i sl. uobičajeni su primjeri bipartitnih grafova.

## Karakterizacija

Bipartitni grafovi mogu se ekvivalentno definirati i sljedećim svojstvima:

-   Graf $G$ može se obojiti dvjema bojama. Drugim riječima, svi se vrhovi grafa mogu obojiti s najviše dvije boje tako da susjedni vrhovi imaju različite boje.
-   Graf $G$ ne sadrži ciklus neparne duljine.

Očito je da je prvo svojstvo ekvivalentno definiciji bipartitnog grafa: dovoljno je svaki od dvaju dijelova obojiti jednom bojom.

Drugo je svojstvo nešto složenije. Pokušajmo graf $G$ obojiti dvjema bojama. Budući da se bojanja različitih komponenata povezanosti međusobno ne ometaju, dovoljno je promatrati komponente jednu po jednu. Odaberimo bilo koji vrh $s$ u komponenti, pokrenimo DFS i za svaki vrh $v$ komponente zabilježimo udaljenost (tj. dubinu) od $s$ u DFS stablu. Indukcijom po DFS stablu, počevši od $s$, vidimo da, ako postoji valjano bojanje, ono nužno boji svaki vrh $v$ jednom od dviju boja ovisno o parnosti njegove udaljenosti do polaznog vrha $s$.

![](./images/bi-graph-2.svg)

Zatim promotrimo bridove koji nisu u stablu. Ako svaki od tih nestablastih bridova ima krajeve različitih boja, trenutno je bojanje valjano; u suprotnom valjano bojanje ne postoji. Nadalje, dva vrha imaju različite boje ako i samo ako su njihove udaljenosti do korijena $s$ različite parnosti, a to je ekvivalentno tome da dodavanje tog nestablastog brida tvori paran, a ne neparan ciklus. Dakle, dok god nema neparnih ciklusa, nestablasti bridovi nužno spajaju vrhove različitih boja, pa se cijeli graf može obojiti dvjema bojama i graf je sigurno bipartitan.

## Provjera

Da bismo provjerili je li graf bipartitan, dovoljno je iskoristiti gornju ekvivalentnu karakterizaciju i pokušati graf obojiti. Za to se graf može obići [DFS-om](./dfs.md) ili [BFS-om](./bfs.md). Ako nađemo neparan ciklus, tj. situaciju u kojoj bojanje nije moguće, graf nije bipartitan; inače jest.

Konkretan postupak:

-   Prolazimo po vrhovima; ako naiđemo na još neobojen vrh, našli smo novu komponentu povezanosti.
-   Taj vrh obojimo bilo kojom bojom i iz njega pokrenemo [DFS](./dfs.md) ili [BFS](./bfs.md), pokušavajući obojiti tu komponentu.
-   Pri obilasku susjednih vrhova, ako naiđemo na već obojen vrh, provjerimo je li njegova boja jednaka boji trenutnog vrha. Ako jest, graf nije bipartitan i odmah završavamo; inače nastavljamo obilazak.
-   Ako naiđemo na još neobojen vrh, obojimo ga bojom suprotnom od boje trenutnog vrha.

Referentni kôd:

???+ example "Referentni kôd"
    ```cpp
    --8<-- "docs/graph/code/bi-graph/check-bipartite.cpp:core"
    ```

Vremenska složenost je $O(|V|+|E|)$.

## Primjene

Zbog jednostavne strukture mnogi se optimizacijski problemi teorije grafova na bipartitnim grafovima mogu učinkovito riješiti. Pojedinosti potraži u odgovarajućim glavnim člancima.

-   maksimalna klika (trivijalno)
-   minimalno bojanje vrhova (trivijalno)
-   [minimalno bojanje bridova](./color.md#konstruktivni-dokaz-vizingova-teorema-za-bipartitne-grafove)
-   [maksimalno sparivanje](./graph-matching/bigraph-match.md)
-   [minimalni bridni pokrivač](./graph-matching/graph-match.md#最小权边覆盖)
-   [minimalni vršni pokrivač](./graph-matching/bigraph-match.md#二分图最小点覆盖)
-   [maksimalni nezavisni skup](./graph-matching/bigraph-match.md#二分图最大独立集)
-   [maksimalno težinsko sparivanje](./graph-matching/bigraph-weight-match.md)
-   [igre na bipartitnim grafovima](../math/game-theory/impartial-game.md#二分图博弈)
