---
title: Uvod u linearnu algebru
---

??? tip "Savjet"
    Ova stranica nije usko povezana s ostalim stranicama u kategoriji „Linearna algebra”. Autor ipak smatra da je doista potrebno progovoriti o biti linearne algebre te pratiti podrijetlo pojmova i veze među njima, kako bi čitatelj stekao početno, ali sustavno razumijevanje linearne algebre.

Još prije nekoliko tisuća godina ljudi su rješavali probleme pomoću sustava linearnih jednadžbi, a linearna algebra i danas ima široku primjenu.

Linearna algebra potječe iz ljudskog promatranja. Uočeno je da mnogi objekti imaju slična svojstva, primjerice:

-   sile se mogu rastavljati i zbrajati (slagati);

-   za proizvoljne $k,x_0$, $k \sin (x-x_0)$ može se rastaviti na $k_1\sin x + k_2\cos x$.

Ta su svojstva povezana sa **skaliranjem**, **rastavljanjem**, **superpozicijom** i sličnim operacijama nad opisanim objektima. Linearna algebra apstrahira ta svojstva iz konkretnih objekata i proučava ih kao zasebnu disciplinu. U OI-ju se znanje iz linearne algebre može izravno upotrijebiti za rješavanje zadataka, ali i za optimizaciju algoritama, struktura podataka i sl. Na primjer:

-   održavanje linearne baze (xor baze) pomoću heavy-light dekompozicije radi određivanja najvećeg xor-a na putu u stablu

-   pretvaranje problema prebrojavanja razapinjućih stabala grafa u računanje determinante matrice pomoću matričnog teorema o stablima (Kirchhoffova teorema)

-   optimizacija rekurzija brzim potenciranjem matrica
