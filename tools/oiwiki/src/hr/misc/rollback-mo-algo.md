---
title: Mo algoritam s vraćanjem (rollback Mo)
---

## Uvod

U nekim zadacima pri prelasku s jednog intervala na drugi dodavanje ili brisanje može biti neizvedivo. Kad je neizvedivo samo dodavanje ili samo brisanje, problem se može riješiti Mo algoritmom s vraćanjem (rollback Mo's algorithm) u vremenu $O(n \sqrt m)$. Osnovna ideja Mo algoritma s vraćanjem jest: ako možemo izvesti samo jednu operaciju, koristimo samo nju, a ostalo rješavamo vraćanjem (rollback).

Mo algoritam s vraćanjem dijeli se na inačicu koja koristi samo dodavanje i inačicu koja koristi samo brisanje. U nastavku opisujemo samo inačicu koja koristi samo dodavanje; inačica samo s brisanjem razlikuje se od nje tek u sitnicama implementacije, pa je ne opisujemo zasebno.

## Primjer zadatka [JOISC 2014 Day1 历史研究 (Povijesno istraživanje)](https://loj.ac/problem/2874)

Zadan je niz $A$ duljine $n$ i $m$ upita $(1 \leq n, m \leq 10^5)$; svaki upit traži broj s najvećom važnošću u intervalu $[L, R]$, a treba **ispisati njegovu važnost**. Važnost broja $i$ definira se kao $i$ pomnoženo s brojem pojavljivanja $i$ u intervalu.

U ovom je zadatku ažuriranje odgovora pri dodavanju lako izvesti, ali ažuriranje pri brisanju nije. Naime, ako dodavanje utječe na odgovor, novi odgovor sigurno je važnost upravo dodanog broja; ako se pak nakon brisanja promijeni broj s najvećom važnošću u intervalu, teško je odrediti koji je broj novi broj s najvećom važnošću. Zato se ovaj zadatak teško rješava običnim Mo algoritmom.

## Postupak

-   Izvorni niz podijelimo na blokove, a upite sortiramo po indeksu bloka kojem pripada lijevi kraj uzlazno kao prvom ključu i po desnom kraju uzlazno kao drugom ključu.
-   Upite obrađujemo redom:
    -   Ako je blok $B$ kojem pripada lijevi kraj upita različit od bloka kojem pripada lijevi kraj prethodnog upita, lijevi kraj Mo intervala inicijaliziramo na desni kraj bloka $B$ plus $1$, a desni kraj Mo intervala na desni kraj bloka $B$;
    -   Ako lijevi i desni kraj upita pripadaju istom bloku, na upit odgovaramo izravnim skeniranjem intervala;
    -   Ako lijevi i desni kraj upita pripadaju različitim blokovima:
        -   Ako je desni kraj upita veći od desnog kraja Mo intervala, proširujemo desni kraj dok desni kraj Mo intervala ne postane jednak desnom kraju upita;
        -   Proširujemo lijevi kraj Mo intervala dok ne postane jednak lijevom kraju upita;
        -   Odgovaramo na upit;
        -   Poništavamo izmjene lijevog kraja Mo intervala, tj. vraćamo lijevi kraj Mo intervala na desni kraj bloka $B$ plus $1$.

## Dokaz složenosti

Pretpostavimo da je veličina bloka u Mo algoritmu s vraćanjem $b$:

-   Upiti kojima su lijevi i desni kraj u istom bloku mogu se izračunati u vremenu $O(b)$;
-   Za ostale upite promotrimo upite s lijevim krajem u istom bloku: njihovi desni krajevi monotono rastu, pa je vremenska složenost pomicanja desnog kraja $O(n)$, a pomak lijevog kraja za jedan upit ne prelazi $b$. Budući da ima $\frac{n}{b}$ blokova, ukupna je složenost $O(mb+\frac{n^2}{b})$; optimalno je uzeti $b=\frac{n}{\sqrt{m}}$, pa je vremenska složenost $O(n\sqrt{m})$.

## Implementacija

??? note "Referentni kôd"
    ```cpp
    --8<-- "docs/misc/code/rollback-mo-algo/rollback-mo-algo_1.cpp"
    ```

## Literatura

-   [回滚莫队及其简单运用 (Mo algoritam s vraćanjem i njegove jednostavne primjene) | Parsnip's Blog](https://www.cnblogs.com/Parsnip/p/10969989.html)
