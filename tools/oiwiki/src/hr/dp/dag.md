---
title: DP na DAG-u
---

## Definicija

DAG je [usmjereni aciklički graf](../graph/dag.md). Binarne relacije u mnogim praktičnim problemima mogu se modelirati DAG-om, čime se ti problemi svode na problem najduljeg (najkraćeg) puta u DAG-u.

## Objašnjenje

Na primjeru sljedećeg zadatka analizirajmo postupak modeliranja DAG-om.

???+ note "Primjer [UVa 437 Babilonska kula – The Tower of Babylon](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=378)"
    Zadano je $n (n\leqslant 30)$ vrsta blokova, za svaku su poznate tri duljine bridova, a svake vrste ima beskonačno mnogo. Treba odabrati neke kvadre i složiti ih u što viši toranj (svaki blok može odabrati bilo koji brid kao visinu), tako da su duljina i širina baze svakog bloka strogo manje od duljine i širine baze bloka pod njim. Odredi najveću visinu tornja.

## Postupak

### Izgradnja DAG-a

Budući da duljina i širina baze svakog bloka moraju biti strogo manje od duljine i širine baze bloka pod njim, nije teško taj odnos uzeti kao temelj za izgradnju grafa, čime se zadatak svodi na problem najduljeg puta.

Drugim riječima, ako se blok $j$ može postaviti na blok $i$, između $i$ i $j$ postoji brid $(i, j)$, a težina brida je visina koju je blok $j$ odabrao.

Druga je poteškoća u ovom zadatku to što visina svakog bloka može biti odabrana na tri načina; kako onda prikladno izgraditi graf?

Svaki blok rastavimo na tri načina slaganja, tj. jedan blok rastavimo na tri bloka, pri čemu svaki od dobivenih blokova uzima drugu visinu.

Početna je točka tlo, čija je baza beskonačno velika, pa je iz tla dostižan svaki blok; pri pisanju programa, naravno, ne moramo posebno zapisivati beskonačnost.

Pretpostavimo da imamo dva bloka s bridovima $31, 41, 59$ odnosno $33, 83, 27$; tada cijeli DAG izgleda kao na slici dolje.

![](./images/dag-babylon.png)

Plavi puni okvir na slici označava skupinu blokova dobivenih rastavljanjem jednog bloka; duljine bridova baze pišemo u $\{\}$ zato što, nakon što blok odabere visinu, bridovi baze više nemaju poredak.

Žuti iscrtkani okvir označava dio koji se računa više puta; ponavljanje računanja može se izbjeći [memoiziranim pretraživanjem](./memo.md).

### Prijelaz

Zadatak traži najveću visinu tornja, a to smo već sveli na problem najduljeg puta; početak je, kako je rečeno, tlo, a kraj? Očito je kraj prirodno određen: to je trenutak kad se na neki blok više ne može postaviti nijedan drugi.

Razmotrimo sada jednadžbu prijelaza.

Neka $d(i,r)$ označava najveću visinu kad je blok $i$ na dnu i složen je na $r$-ti način. Tada vrijedi sljedeća jednadžba prijelaza:

$$
d(i, r) = \max\left\{d(j, r') + h\right\}
$$

Ovdje $j$ prolazi po svim blokovima koji se mogu staviti na blok $i$ složen na način $r$, $r'$ je odgovarajući način slaganja bloka $j$, a $h$ je visina bloka $i$ pri slaganju na $r$-ti način.

??? note "Implementacija"
    ```cpp
    --8<-- "docs/dp/code/dag/dag_1.cpp"
    ```
