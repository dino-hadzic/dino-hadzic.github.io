---
title: Hill climbing
---

## Uvod

Hill climbing (penjanje uzbrdo) metoda je lokalnog odabira najboljeg rješenja koja koristi heuristiku; riječ je o poboljšanju pretraživanja u dubinu (DFS) koje pomoću povratnih informacija pomaže pri donošenju odluka o generiranju rješenja.

Jednostavno rečeno: kad trenutačno ne možemo izravno doći do optimalnog rješenja, ali za dva rješenja znamo odrediti koje je bolje, na temelju nekih povratnih informacija generiramo novo moguće rješenje.

Stoga hill climbing svaki put u blizini trenutačno najboljeg pronađenog rješenja $x$ traži novo rješenje. Ako je to novo rješenje $x'$ bolje, prelazimo na $x'$, inače ostajemo gdje jesmo.

Za unimodalne funkcije ovaj algoritam očito radi.

P: Ako već znamo da je funkcija unimodalna, zašto ne upotrijebiti ternarno pretraživanje?

O: Prednost hill climbinga jest to što, kad ne znamo kako se piše pravo rješenje (često kod zlobnih zadataka iz računalne geometrije i zlobnih matematičkih zadataka) ili kad stanje ima mnogo dimenzija pa nije lako napisati podjelu (primjer 2 može se ispravno riješiti i binarnim pretraživanjem), optimalno rješenje možemo dobiti vrlo grubim računanjem.

Međutim, za većinu funkcija koje treba optimizirati hill climbing lako upada u lokalni optimum, kao na slici dolje (optimalno rješenje je $\color{green}{\Uparrow}$, a hill climbing može pronaći $\color{red}{\Downarrow}$).

![](./images/hill-climbing.png)

## Konkretna implementacija

Hill climbing obično uvodi parametar temperature (slično simuliranom kaljenju). Slikovito rečeno, hill climbing je poput pijanog zeca koji skače po planini: svaki put skoči prema mjestu koje smatra višim (a to je često samo netočna procjena trenda); očito može jednim skokom stići na vrh, ali može i preskočiti vrh i prevaliti se na drugu stranu. No ne smeta, zec će se nakon toga skokom vratiti. Jasno je da je taj proces vrlo neučinkovit i zec nikad ne bi našao izlaz, pa se tijekom procesa zec trijezni i pri svakom skoku postaje oprezniji te skače malo manje, kako bi stigao do odgovarajuće optimalne točke.

Postupno triježnjenje zeca jest proces hlađenja, tj. parametar temperature tijekom penjanja neprestano se smanjuje.

O hlađenju: parametar hlađenja konstanta je malo manja od $1$, obično iz $[0.985, 0.999]$.

## Primjeri zadataka

???+ example "[「JSOI2008」球形空间产生器 (Generator sfernog prostora)](https://www.luogu.com.cn/problem/P4035)"
    Zadana je $n + 1$ točka u $n$-dimenzionalnom prostoru za koje se zna da leže na istoj $n$-dimenzionalnoj sferi; odredite središte sfere. $n \leq 10$, apsolutne vrijednosti koordinata ne prelaze $20000$.

??? note "Rješenje"
    Očito unimodalna funkcija, pa se može riješiti hill climbingom. Tijek algoritma za ovaj zadatak:
    
    1.  Središte sfere inicijaliziramo kao težište zadanih točaka (tj. svaka njegova koordinata prosjek je odgovarajućih koordinata svih zadanih točaka), kako bismo smanjili količinu pretraživanja.
    2.  Za trenutačno središte izračunamo prosjek euklidskih udaljenosti svih zadanih točaka do njega.
    3.  Prođemo kroz sve zadane točke. Bilježimo vrijednost promjene $\textit{cans}$ (zasebno za svaku dimenziju): za euklidsku udaljenost svake točke, ako je veća od prosjeka, vrijednosti promjene dodamo razliku, inače je oduzmemo. Zapravo tu usporedbu i ne treba raditi: dovoljno je ne gledati apsolutnu vrijednost i računati izravno s koordinatama. Taj proces možemo zorno zamisliti kao novo središte koje guramo po prostoru: kad naiđemo na predaleku točku, povučemo ga malo prema njoj, a kad naiđemo na preblisku točku, odgurnemo ga malo od nje.
    4.  Zabilježeni $\textit{cans}$ pomnožimo temperaturom, ažuriramo središte i vratimo se na korak 2.
    5.  Završavamo kad temperatura padne ispod zadanog praga.
    
    Dakle, pri ažuriranju središta ne smijemo izravno dodati vrijednost promjene, nego umnožak vrijednosti promjene i temperature.
    
    Ne može se svaki zadatak s hill climbingom riješiti baš pomoću temperature; ovo je samo jedan primjer.

??? note "Primjer koda"
    ```cpp
    --8<-- "docs/misc/code/hill-climbing/hill-climbing_1.cpp"
    ```

???+ example "[「BZOJ 3680」吊打 XXX (Premlatiti XXX-a)](https://hydro.ac/p/bzoj-P3680)"
    Odredite težinsku (generaliziranu) Fermatovu točku za $n$ točaka.

??? note "Rješenje"
    Okvir je sličan, uz malo fizikalnog znanja.

??? note "Primjer koda"
    ```cpp
    --8<-- "docs/misc/code/hill-climbing/hill-climbing_2.cpp"
    ```

## Optimizacija

Lako se dolazi do ideje da, kako bismo dobili što bolji odgovor, hill climbing možemo pokrenuti više puta. Načini su promjena početnog stanja, promjena parametra hlađenja, promjena početne temperature itd.; zatim otvorimo globalnu varijablu za najbolje rješenje u koju pamtimo odgovor. Nakon svakog završenog pokretanja ažuriramo globalni optimum.

Problem koji se pri tome može pojaviti jest prekoračenje vremenskog ograničenja; na pravom natjecanju ručno napravite velike testne podatke i na njima podesite parametre.

## Nedostaci

Nedostatak hill climbinga već je spomenut: lako upada u lokalni optimum. Kad ciljna funkcija nije unimodalna, taj je nedostatak fatalan. Zato uvodimo [**simulirano kaljenje**](./simulated-annealing.md).
