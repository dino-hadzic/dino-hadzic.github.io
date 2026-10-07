---
title: Vršna i bridna povezanost
---

## Definicija

Definicije pojmova koji se koriste u nastavku potraži u [osnovnim pojmovima teorije grafova](./concept.md):

-   bridna povezanost, bridni rez (rezni skup bridova);
-   vršna povezanost, vršni rez (rezni skup vrhova);
-   klika.

## Svojstva

### Whitneyeva nejednakost

**Whitneyeva nejednakost** (1932) daje odnos između vršne povezanosti $\kappa$, bridne povezanosti $\lambda$ i najmanjeg stupnja $\delta$:

$$
\kappa \le \lambda \le \delta
$$

???+ note "Dokaz"
    Intuitivno: ako imamo bridni rez veličine $\lambda$ i iz svakog njegova brida odaberemo po jedan kraj, dobit ćemo vršni rez veličine $\lambda$, pa prva nejednakost vrijedi.
    
    Svi bridovi incidentni s vrhom najmanjeg stupnja (ako ih ima više, bilo kojim od njih) čine bridni rez veličine $\delta$, pa vrijedi i druga nejednakost.

Ova se nejednakost ne može poboljšati; drugim riječima, za svaku trojku koja je zadovoljava može se naći graf s upravo tim parametrima.

???+ note "Konstrukcija"
    Dvije klike veličine $\delta + 1$ spojimo s $\lambda$ bridova tako da u jednoj kliki ti bridovi završavaju u $\lambda$ različitih vrhova, a u drugoj u $\kappa$ različitih vrhova.

### Mengerov teorem

Iz [teorema o maksimalnom toku i minimalnom rezu](./flow/min-cut.md) (poznatog i kao Ford–Fulkersonov teorem) slijedi da je najveći broj disjunktnih (u parovima bez zajedničkog brida) putova između dvaju vrhova jednak najmanjoj veličini reza (ta se posljedica naziva i **Mengerov teorem** – op. prev.).

## Računanje

U nastavku sve težine bridova iznose $1$.

### Bridna povezanost maksimalnim tokom

Prolazimo po svim parovima vrhova $(s, t)$ i za svaki pokrenemo maksimalni tok s izvorom $s$, ponorom $t$ i težinama bridova $1$. Potrebno je $O(n^2)$ maksimalnih tokova; s Edmonds–Karpovim algoritmom složenost je $O(|V|^3 |E|^2)$. Dinicov algoritam daje bolje: $O(|V|^2 |E| \min(|V|^{2/3}, |E|^{1/2}))$.

### Globalni minimalni rez

[Stoer–Wagnerovim algoritmom](./stoer-wagner.md) dovoljno je jednom izračunati minimalni rez bez izvora i ponora. Složenost je $O(|V||E| + |V|^{2}\log|V|)$, što se obično približno uzima kao $O(|V|^3)$.

### Vršna povezanost

Opet prolazimo po parovima vrhova, ali ovaj put svaki vrh $x$ koji nije izvor ni ponor razdvojimo na dva vrha $x_1$ i $x_2$ i dodamo brid $(x_1, x_2)$. Svaki brid $(u, v)$ izvornog grafa zamijenimo dvama bridovima $(u_2, v_1)$ i $(v_2, u_1)$. Maksimalni tok tada je jednak veličini najmanjeg vršnog reza između $s$ i $t$ (zvanoj i lokalna vršna povezanost). Složenost je ista kao kod računanja bridne povezanosti maksimalnim tokom.

**Ova je stranica prevedena iz članaka [Рёберная связность. Свойства и нахождение](http://e-maxx.ru/algo/rib_connectivity) i [Вершинная связность. Свойства и нахождение](http://e-maxx.ru/algo/vertex_connectivity) te njihova engleskog prijevoda [Edge connectivity/Vertex connectivity](https://cp-algorithms.com/graph/edge_vertex_connectivity.html). Ruska je inačica pod licencijom Public Domain + Leave a Link, a engleska pod CC-BY-SA 4.0.**

## Daljnje čitanje

-   Rad [*Connectivity Algorithms*](https://www.cse.msu.edu/~cse835/Papers/Graph_connectivity_revised.pdf) prikazuje napredak algoritama za računanje povezanosti posljednjih godina. Zainteresirani ga čitatelji mogu sami pregledati.
