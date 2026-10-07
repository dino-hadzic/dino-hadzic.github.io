---
title: Iterativno produbljivanje
---

## Definicija

Iterativno produbljivanje (iterative deepening) je pretraživanje u dubinu koje **svaki put ograničava dubinu pretrage**.

## Objašnjenje

Pretraživanje iterativnim produbljivanjem u biti je i dalje pretraživanje u dubinu, samo što uz pretragu nosi i dubinu $d$: kad $d$ dosegne zadanu dubinu, vraća se. Obično se koristi za nalaženje optimalnog rješenja. Ako jedna pretraga ne nađe dopustivo rješenje, zadana se dubina poveća za jedan i pretraga kreće iznova od korijena.

Ako već tražimo optimalno rješenje, zašto ne upotrijebiti BFS? Znamo da se BFS temelji na redu, čija je prostorna složenost velika; kad je stanja mnogo ili je pojedino stanje veliko, BFS s redom pokazuje svoje nedostatke. Zapravo je iterativno produbljivanje nalik BFS-u ostvarenom na način DFS-a, a prostorna mu je složenost razmjerno mala.

Kad stablo pretrage ima mnogo grana, složenost pretrage sa svakom dodatnom razinom raste eksponencijalno, pa je složenost ponovljenih prethodnih dijelova gotovo zanemariva; zato se iterativno produbljivanje može približno smatrati BFS-om.

## Postupak

Najprije postavimo manju dubinu kao globalnu varijablu i pokrenemo DFS. Pri svakom ulasku u DFS trenutnu dubinu povećamo za jedan, a kad $d$ premaši zadanu dubinu $\textit{limit}$, vraćamo se. Ako tijekom pretrage nađemo odgovor, možemo se vratiti unatrag i usput zabilježiti put. Ako odgovor nije nađen, vraćamo se na ulaz u funkciju, povećavamo zadanu dubinu i nastavljamo pretragu.

???+ note "Implementacija (pseudokod)"
    ```text
    IDDFS(u,d)
        if d>limit
            return
        else
            for each edge (u,v)
                IDDFS(v,d+1)
    return
    ```

## Napomene

U većini zadataka pretraživanje u širinu je ipak praktičnije i u njemu je lakše otkrivati ponavljanja. Kad primijetimo da pretraživanje u širinu nije dovoljno dobro po prostoru, a zadatak traži optimalno rješenje, treba razmisliti o iterativnom produbljivanju.
