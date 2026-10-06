---
title: Simulacija
---

Ova stranica kratko predstavlja simulaciju.

## Uvod

Simulacija znači da računalom simuliramo operacije koje zadatak traži.

Zadatke sa simulacijom obično odlikuju velika količina koda, mnogo operacija i zamršen tijek. Zbog količine koda u njima je često teško pronaći grešku, a pogriješiti na natjecanju znači izgubiti puno vremena.

## Savjeti

Pri rješavanju zadataka sa simulacijom sljedeći savjeti mogu ubrzati rješavanje:

-   Prije pisanja koda na papiru što detaljnije razradi tijek koji treba implementirati.
-   U kodu svaki dio po mogućnosti izdvoji u modul: funkciju, strukturu ili klasu.
-   Pojmove koji se mogu ponavljati pretvori u jedinstven oblik radi lakše obrade: npr. ako zadatak daje „GG-MM-DD sat:minuta”, izdvoji to u funkciju i pretvori u sekunde – bit će manje zabune.
-   Pri otklanjanju grešaka ispituj dio po dio. Prednost modularnosti je upravo to što se pojedini dio lako ispituje zasebno.
-   Pri pisanju koda misli moraju biti jasne; ne piši što ti prvo dođe u glavu, nego slijedi korake zapisane na papiru.

Zapravo, navedeni koraci pomažu i pri rješavanju drugih vrsta zadataka.

## Riješeni primjer

???+ note "[Climbing Worm](https://open.kattis.com/problems/climbingworm)"
    Crv zanemarive duljine nalazi se na dnu bunara dubokog $n$ inča. Svaki put popne se $u$ inča, ali se nakon toga mora odmoriti prije nego što se opet može penjati. Dok se odmara, sklizne $d$ inča. Zatim ponavlja penjanje i odmaranje. Koliko se najmanje puta crv mora popeti da izađe iz bunara? Ako nakon penjanja točno dosegne vrh bunara, također smatramo da je izašao.

??? note "Ideja rješenja"
    Zadatak jamči da crv može izaći iz bunara, tj. $u\ge n$ ili $u>d$. Pod tim uvjetom možemo izravno simulirati. Petljom ponavljamo postupak penjanja, a kad dosegnuta visina postane veća ili jednaka dubini bunara, izlazimo iz petlje.

??? note "Primjer rješenja"
    === "C++"
        ```cpp
        --8<-- "docs/basic/code/simulate/simulate_1.cpp"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/basic/code/simulate/simulate_1.py"
        ```
    
    === "Java"
        ```java
        --8<-- "docs/basic/code/simulate/simulate_1.java"
        ```

## Zadaci za vježbu

-   [„NOIP2014” Rock-paper-scissors (The Big Bang Theory version) - Universal Online Judge](https://uoj.ac/problem/15)
-   [„OpenJudge 3750” World of Warcraft](http://bailian.openjudge.cn/practice/3750/)
-   [„SDOI2010” Pig Kingdom Kill - LibreOJ](https://loj.ac/problem/2885)
