---
title: 15-puzzle
---

## Uvod

**Slagalica 15** (engl. 15-puzzle, poznata i kao Gem Puzzle, Boss Puzzle, Game of 15, Mystic Square, N-puzzle itd.) igra je s kliznim pločicama (engl. sliding puzzle). Ploča ima dimenzije $4\times 4$ polja; na 15 polja nalaze se pločice s izmiješanim rednim brojevima, a jedno je polje prazno. Pločice u istom retku ili stupcu kao prazno polje mogu se pomicati vodoravnim ili okomitim klizanjem. Cilj slagalice je rasporediti pločice po redu brojeva.

Slagalica 15 često se naziva i **slagalica n**, pri čemu se broj $n$ odnosi na ukupan broj pločica na ploči. Varijante slagalice 15 drugih dimenzija imaju slična imena, npr. slagalica $8$ odnosi se na $8$ pločica na ploči $3\times3$. No slagalica $15$ može se zvati i slagalica $16$, pri čemu se 16 odnosi na broj polja. Njezina poopćenja ponekad uključuju i klizne ploče dimenzija $n \times m$.

Slagalica 15 klasičan je problem za modeliranje [heurističkih algoritama](../search/heuristic.md). Uobičajeni oblici su [manhattanska udaljenost](../geometry/distance.md#manhattanska-udaljenost) i broj pločica na krivom mjestu; obje su dopustive heuristike (engl. admissible heuristic), tj. nikad ne precjenjuju preostali broj poteza, što jamči optimalnost nekih algoritama pretraživanja (npr. [algoritma A\*](../search/astar.md)).

???+ note "Napomena"
    **Igre s kliznim pločicama** vrsta su logičkih igara u kojima se pločice klizanjem po ravnini slažu u određeni raspored. Uobičajene igre s kliznim pločicama uključuju brojčane slagalice, Huarong Dao (华容道, kinesku kliznu slagalicu) i Rush Hour. Slagalica 15 najstarija je od njih; izumio ju je Noyes Chapman, a igra je postala vrlo popularna 1880-ih. Za razliku od drugih logičkih igara tipa „obilazak” (tour), u igrama s kliznim pločicama nijedna pločica ne smije napustiti ploču, što ih razlikuje od logičkih igara s preslagivanjem.

## Definicija

Zadana je ploča $4 \times 4$ na kojoj je $15$ pločica proizvoljno raspoređeno. Trebamo ih po rednim brojevima rasporediti kao na slici dolje. Pravilo pomicanja: u jednom potezu smije se zamijeniti samo prazno polje s jednom susjednom pločicom. Uobičajena pitanja su pronaći najmanji broj poteza kojima se slagalica rješava, izračunati broj pločica na krivom mjestu ili utvrditi može li se uopće doći do konačnog uređenog rasporeda.

![](./images/15puzzle-1.svg)

## Dokaz rješivosti

Johnson i Story (1879.) dokazali su da obrat vrijedi za ploče dimenzija $m\times n$ ako su $m$ i $n$ barem $2$: indukcijom po $m$ i $n$, počevši od $m=n=2$, dokazuje se da su sve parne permutacije rješive. Archer (1999.) dao je drugi dokaz, zasnovan na definiranju klasa ekvivalencije pomoću Hamiltonovih putova.

## Algoritmi

Pronaći neko rješenje slagalice s brojevima razmjerno je lako, ali pronalaženje **optimalnog rješenja** **NP-težak** je problem. Optimalno rješenje slagalice 15 ima najviše 80 poteza, a optimalno rješenje slagalice 8 najviše 31 potez.

Na slagalicu n mogu se primijeniti uobičajeni algoritmi pretraživanja grafova, kao što su pretraživanje u širinu i pretraživanje u dubinu, a za pronalaženje optimalnog rješenja možemo koristiti i algoritam [pretraživanja A\*](../search/astar.md). Heuristička funkcija $h(n)$ može biti

-   broj pločica na krivom mjestu;
-   zbroj euklidskih udaljenosti svih pločica na krivom mjestu do njihovih ciljnih položaja;
-   zbroj manhattanskih udaljenosti svih pločica na krivom mjestu do njihovih ciljnih položaja.

### Teorija grupa

Budući da se kombinacije slagalice s 15 pločica mogu generirati „3-ciklusima” (engl. 3-cycles), može se dokazati da se slagalica s 15 pločica može prikazati alternirajućom grupom $A_{15}$. Zapravo, svaka klizna slagalica s $2\times k-1$ jednakih kvadratnih pločica može se prikazati alternirajućom grupom $A_{2k-1}$.

## Zadaci za vježbu

-   [N Puzzle](https://www.hackerrank.com/challenges/n-puzzle)
-   [A. Amity Assessment](https://codeforces.com/problemset/problem/645/A)
-   [Sliding Puzzle](https://leetcode.com/problems/sliding-puzzle/)
-   [POJ 1077 - Eight](http://poj.org/problem?id=1077)

## Literatura i dodatno čitanje

1.  [15 puzzle - Wikipedia](https://en.wikipedia.org/wiki/15_puzzle)
2.  jrdnjacobson, [How to Solve the 15 Puzzle - instructables](https://www.instructables.com/How-To-Solve-The-15-Puzzle/)
3.  Korf, R. E. (2000), ["Recent Progress in the Design and Analysis of Admissible Heuristic Functions"](https://www.researchgate.net/publication/2604757_Recent_Progress_in_the_Design_and_Analysis_of_Admissible_Heuristic_Functions), u: Choueiry, B. Y.; Walsh, T. (ur.), Abstraction, Reformulation, and Approximation (PDF), SARA 2000. Lecture Notes in Computer Science, sv. 1864, Springer, Berlin, Heidelberg, str. 45–55, doi:10.1007/3-540-44914-0\_3, ISBN 978-3-540-67839-7, pristupljeno 26. travnja 2010.
4.  [Welcome to N-Puzzle - web demo](https://tristanpenman.com/demos/n-puzzle/)
