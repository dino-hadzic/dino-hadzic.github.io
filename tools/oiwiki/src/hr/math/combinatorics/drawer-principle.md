---
title: Dirichletov princip
---

## Definicija

Dirichletov princip naziva se i princip pretinaca ili princip golubinjaka (the pigeonhole principle).

Često se koristi u dokazima egzistencije i pri određivanju rješenja u najgorem slučaju.

## Jednostavan slučaj

Ako $n+1$ predmeta podijelimo u $n$ skupina, tada barem jedna skupina sadrži dva (ili više) predmeta.

Taj se teorem čini prilično očitim; dokazuje se kontradikcijom: kad bi svaka skupina sadržavala najviše $1$ predmet, ukupno bi bilo najviše $1\times n$ predmeta, a zapravo ih ima $n+1$ – kontradikcija.

## Poopćenje

Ako $n$ predmeta podijelimo u $k$ skupina, tada postoji barem jedna skupina koja sadrži barem $\left \lceil \dfrac{n}{k} \right \rceil$ predmeta.

I poopćeni oblik može se dokazati kontradikcijom: kad bi svaka skupina sadržavala manje od $\left \lceil \dfrac{n}{k} \right \rceil$ predmeta, njihov bi ukupan broj bio $S\leq (\left \lceil \dfrac{n}{k} \right \rceil -1 ) \times k=k\left\lceil \dfrac{n}{k} \right\rceil-k < k(\dfrac{n}{k}+1)-k=n$ – kontradikcija.

Osim toga, particiju je moguće oslabiti u pokrivač, a zaključak ostaje isti.  
Zadan je skup $S$ i familija $\{A_1,A_2\ldots A_k\}$ nepraznih podskupova skupa $S$.

-   Ako vrijedi $\bigcup_{i=1}^k A_i$, familija se naziva pokrivačem (cover) skupa $S$.
-   Ako pokrivač dodatno zadovoljava $i\neq j\to A_i\cap A_j=\varnothing$, naziva se particijom skupa $S$.

Dirichletov princip tada se može iskazati ovako: za pokrivač $\{A_1,A_2\ldots A_k\}$ skupa $S$ postoji barem jedan skup $A_i$ za koji vrijedi $\left\vert A_i \right\vert \geq \left\lceil \dfrac{\left\vert S \right\vert}{k} \right\rceil$.

## Literatura

-   [Wikipedia: Pigeonhole principle](https://en.wikipedia.org/wiki/Pigeonhole_principle)
-   *Discrete Mathematics and Its Applications*: Chapter 6, Section 1
