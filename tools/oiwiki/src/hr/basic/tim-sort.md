---
title: Timsort
---

Ova stranica predstavlja Timsort, hibridni i stabilni algoritam sortiranja.

## Uvod

Timsort je 2002. osmislio Tim Peters, jedan od glavnih razvijatelja Pythona, i primijenio ga u jeziku Python. Vješto spaja prednosti insertion sorta i merge sorta te je precizno optimiran za postojeću uređenost u podacima, pa je osobito prikladan za skupove podataka s mnogo djelomično sortiranih podnizova. CPython koristi Timsort od inačice 2.3, a od inačice 3.11 njegovu strategiju redoslijeda spajanja zamjenjuje Powersortom[^powersort]. Timsort se široko primjenjuje i u drugim programskim okruženjima; npr. u Javi SE 7 koristi se za sortiranje nizova objekata koji nisu primitivnog tipa.

Ova stranica opisuje tradicionalni Timsort, pri čemu kao mjerodavna uzima pravila spajanja iz CPythona 3.6.5 u kojima je ispravljen problem održavanja invarijante stoga[^merge-policy].

## Koraci

Osnovna je ideja Timsorta povećati učinkovitost sortiranja prepoznavanjem i iskorištavanjem uređenosti koja već postoji u podacima. Glavni koraci su:

1.  **Prepoznavanje runova**: niz koji sortiramo pretražuje se i u njemu se prepoznaju sortirani uzastopni podnizovi (runovi, engl. run);
2.  **Proširivanje runova**: ako je duljina prepoznatog runa manja od `MIN_RUN`, run se proširuje insertion sortom;
3.  **Spajanje runova**: Timsort održava poseban stog i posebnom strategijom spajanja spaja runove na stogu u veće sortirane nizove.

### Prepoznavanje runova

Najprije Timsort pretražuje niz slijeva nadesno i prepoznaje uzastopne sortirane nizove, koje nazivamo runovima:

-   **Uzlazni run**: ako je sljedeći element veći ili jednak prethodnom, run se nastavlja širiti.
-   **Silazni run**: ako je sljedeći element manji od prethodnog, run se nastavlja širiti, a zatim se obrće u uzlazni.

### Proširivanje runova

Da bi sortiranje malih količina podataka bilo učinkovitije, Timsort uvodi najmanju duljinu runa `MIN_RUN`. Njezina se vrijednost obično računa dinamički prema duljini niza koji sortiramo i najčešće je između $32$ i $64$.

-   Ako je duljina prepoznatog runa veća ili jednaka `MIN_RUN`, nije potrebna dodatna radnja i run se izravno stavlja na stog.
-   Ako je duljina prepoznatog runa manja od `MIN_RUN`, binarnim insertion sortom umeću se sljedeći elementi u run dok duljina runa ne dosegne `MIN_RUN`, a zatim se run stavlja na stog.

### Spajanje runova

U Timsortu se spajanje (merge sort) upravlja i kontrolira pomoću **stoga**. Na stogu se čuvaju već prepoznati sortirani runovi, a posebna pravila spajanja određuju kako se runovi na stogu spajaju; cilj je pri spajanju održati uravnoteženost i stabilnost nizova.

#### Pravila spajanja

Timsort je stabilan algoritam sortiranja, tj. jednaki elementi nakon sortiranja zadržavaju izvorni međusobni poredak. Da bi to osigurao, Timsort pri spajanju spaja samo susjedne, uzastopne runove, a nikad izravno nesusjedne. Nesusjedni runovi mogu sadržavati jednake elemente, pa bi njihovo izravno spajanje vrlo vjerojatno poremetilo njihov međusobni poredak.

Istodobno, da bi kontrolirao uravnoteženost spajanja i broj runova koji čekaju na spajanje, Timsort zahtijeva da svaka tri susjedna runa na stogu zadovoljavaju sljedeće invarijante. Označimo tri runa od vrha stoga prema dnu redom X, Y i Z:

-   **Uvjet 1**: `len(Z) > len(Y) + len(X)`
-   **Uvjet 2**: `len(Y) > len(X)`

Kad su na stogu samo dva runa, također se zahtijeva `len(Y) > len(X)`. Nakon svakog stavljanja novog runa na stog, `mergeCollapse` provjerava najviše četiri runa s vrha stoga; označimo ih od vrha prema dolje X, Y, Z, W. Spajanje se odlučuje sljedećim redom[^merge-policy]:

1.  ako je `len(Z) <= len(Y) + len(X)` ili `len(W) <= len(Z) + len(Y)`, Y se spaja s kraćim od X i Z; ako su X i Z jednake duljine, bira se X;
2.  inače, ako je `len(Y) <= len(X)`, spajaju se Y i X;
3.  inače se ova runda spajanja prekida i nastavlja se prepoznavanje sljedećeg runa.

Provjeravaju se samo uvjeti za koje svi potrebni runovi postoje; nakon svakog spajanja ponovno se određuju X, Y, Z, W i postupak se ponavlja. Slika u nastavku prikazuje promjenu stoga pri spajanju X i Y.

![Pravila spajanja](./images/tim-sort-1.svg)

???+ note "Zašto treba provjeravati četvrti run?"
    Ako se provjeravaju samo tri runa s vrha stoga, nakon spajanja može se propustiti narušavanje invarijante dublje na stogu. Npr. stavimo li redom runove duljina $240,160,50,40,60$ (od dna prema vrhu stoga), staro bi pravilo spojilo $50$ i $40$ i dobilo $240,160,90,60$. Vrh stoga tada zadovoljava $160>90+60$ i $90>60$, ali dublje vrijedi $240\le160+90$.
    
    Taj nedostatak poništava jamstvo fiksnog kapaciteta stoga izvedeno iz invarijante na cijelom stogu. CPython je 2015. ispravio uvjete provjere[^merge-fix].

#### Optimizacija spajanja

Da bi spajanje runova različitih duljina bilo učinkovitije i trošilo manje memorije, Timsort prije spajanja binarnim pretraživanjem precizno određuje raspon elemenata koje treba obraditi i spaja samo dio koji se zaista mora premjestiti. Konkretno:

1.  **Određivanje točaka umetanja**: binarnim pretraživanjem nađe se položaj na koji bi se prvi element drugog runa umetnuo u prvi run, te položaj na koji bi se posljednji element prvog runa umetnuo u drugi run. Time se sužava raspon koji treba spojiti i obrađuju se samo elementi koje treba premjestiti;

2.  **Privremeni međuspremnik**: tradicionalni algoritmi spajanja na mjestu preslabo su učinkoviti i zahtijevaju mnogo premještanja elemenata. Da bi smanjio taj trošak, Timsort koristi privremeni međuspremnik: kraći run kopira u međuspremnik, a zatim elemente postupno kopira iz međuspremnika natrag u izvorni niz.

Npr. pretpostavimo da postoje dva runa, A i B:

-   Run A: $[1, 2, 3, 6, 10]$
-   Run B: $[4, 5, 7, 9, 12, 14, 17]$

Binarnim pretraživanjem utvrđujemo:

-   element $4$ treba umetnuti na četvrto mjesto runa A;
-   element $10$ treba umetnuti na peto mjesto runa B.

Stoga su prva $3$ elementa runa A i posljednja $3$ elementa runa B već na ispravnim mjestima i ne treba ih obrađivati. Treba spojiti samo $[6, 10]$ iz runa A i $[4, 5, 7, 9]$ iz runa B; postupak spajanja prikazan je na slici:

![Spajanje u Timsortu](./images/tim-sort-2.apng)

#### Galopirajući način

Da bi spajanje bilo još učinkovitije, Timsort uvodi **galopirajući način (galloping mode)**. U standardnom spajanju algoritam uspoređuje elemente dvaju runova jedan po jedan i manji stavlja u rezultat. No ako jedan run sadrži dugačak niz uzastopnih elemenata manjih od trenutnog elementa drugog runa, usporedba jedan po jedan uzrokuje nepotreban trošak.

Da bi to riješio, Timsort postavlja prag `Min_Gallop` (zadano $7$). Kad broj uzastopnih „pobjeda” elemenata iz jednog runa dosegne `Min_Gallop`, algoritam prelazi u galopirajući način i brzo pronalazi položaj elementa. Koraci su:

1.  **Eksponencijalno pretraživanje**: od trenutnog položaja algoritam pretražuje run koracima eksponencijalno rastuće duljine $(1, 2, 4, 8, \dots)$ dok ne nađe interval u kojem se nalazi traženi element;
2.  **Binarno pretraživanje**: kad je interval koji sadrži traženi element određen, algoritam u njemu binarnim pretraživanjem precizno pronalazi položaj elementa.

Na taj način Timsort preskače mnogo nepotrebnih usporedbi, brzo obrađuje uzastopne manje (ili veće) elemente jednog runa i skupno ih premješta u rezultat spajanja.

Galopirajući način ipak nije uvijek učinkovitiji. Pri nekim razdiobama podataka može dovesti do više usporedbi. Zato Timsort primjenjuje dinamičku prilagodbu:

-   **Prilagodba praga**: održava se promjenjivi parametar `Min_Gallop`. Kad se galopirajući način pokaže dobrim (tj. uzastopno se više puta biraju elementi iz istog runa), `Min_Gallop` se smanjuje za $1$ i tako potiče daljnje galopiranje; kad se pokaže lošim (često prebacivanje između dvaju runova), `Min_Gallop` se povećava za $1$ i galopiranje se koristi rjeđe.

Dinamičkim podešavanjem vrijednosti `Min_Gallop` algoritam prema stvarnim podacima pronalazi ravnotežu između običnog spajanja i galopirajućeg načina. Za djelomično ili visoko sortirane podatke galopirajući način znatno povećava učinkovitost i performanse Timsorta približava $O(n)$; za nasumične podatke algoritam postupno naginje običnom spajanju, čime jamči vremensku složenost $O(n \log n)$.

## Složenost

Vremenska složenost Timsorta ovisi o uređenosti podataka:

-   **Najbolji slučaj**: $O(n)$
    -   Kad su podaci već sortirani ili gotovo sortirani, duljine prepoznatih runova bliske su $n$, broj spajanja se smanjuje i složenost teži k $O(n)$.
-   **Najgori slučaj**: $O(n \log n)$
    -   Ako ima $r$ runova, na kraju je potrebno $r-1$ dvosmjernih spajanja; broj spajanja ne može se zapisati kao $O(\log n)$.

Prepoznavanje runova stoji $O(n)$, a proširivanje kratkih runova uz ograničen `MIN_RUN` također ukupno $O(n)$. Cijena spajanja jednaka je zbroju duljina dvaju runova koji se spajaju, što je isto što i zbroj, po svim elementima, broja spajanja u kojima element sudjeluje. Gornja granica tog zbroja ovisi o konkretnim pravilima spajanja; za pravila spajanja Pythona 3.6.5 analizirana u literaturi[^complexity] amortizirana analiza daje $O(n+n\log r)$, pa je najgori slučaj $O(n\log n)$.

Što se tiče prostorne složenosti, Timsort treba otprilike $O(n)$ dodatnog prostora za stog i privremeni međuspremnik, pa je ukupna prostorna složenost $O(n)$.

## Implementacija

???+ note "Pseudokod"
    $$
    \begin{array}{ll}
    1 & \textit{nRemaining} \gets \text{duljina niza} \\
    2 & \textit{minRun} \gets \text{odaberi prikladnu vrijednost MinRun}(\textit{nRemaining}) \\
    3 & \textit{startIndex} \gets 0 \\
    4 & \textbf{while } \textit{nRemaining} > 0 \ \textbf{do} \\
    5 & \qquad \textit{runLength} \gets \text{prepoznaj run }(\textit{array}, \textit{startIndex}, \textit{nRemaining}) \\
    6 & \qquad \textbf{if } \textit{runLength} < \textit{minRun} \ \textbf{then} \\
    7 & \qquad \qquad \textit{extendLength} \gets \min(\textit{minRun}, \textit{nRemaining}) \\
    8 & \qquad \qquad \text{insertion sortom proširi interval } [\textit{startIndex}, \textit{startIndex} + \textit{extendLength} - 1]\\
    9 & \qquad \qquad \textit{runLength} \gets \textit{extendLength} \\
    10 & \qquad \textbf{end if} \\
    11 & \qquad \text{stavi run } (\textit{startIndex}, \textit{runLength}) \text{ na stog} \\
    12 & \qquad \textbf{pozovi } \text{mergeCollapse(stog)} \ \text{provjeri i spoji runove na stogu} \\
    13 & \qquad \textit{startIndex} \gets \textit{startIndex} + \textit{runLength} \ \text{ažuriraj početni položaj} \\
    14 & \qquad \textit{nRemaining} \gets \textit{nRemaining} - \textit{runLength} \ \text{ažuriraj preostalu duljinu} \\
    15 & \textbf{end while} \\
    16 & \textbf{pozovi } \text{mergeForceCollapse(stog)} \ \text{konačno spoji sve runove na stogu} \\
    \end{array}
    $$

## Literatura i bilješke

1.  [Timsort](https://en.wikipedia.org/wiki/Timsort)
2.  [Bilješke Tima Petersa o dizajnu (CPython 3.6.5; uvjeti spajanja prema kodu te inačice)](https://github.com/python/cpython/blob/v3.6.5/Objects/listsort.txt)
3.  [Implementacija u Javi](https://cs.android.com/android/platform/superproject/main/+/main:libcore/ojluni/src/main/java/java/util/TimSort.java)
4.  [Implementacija u C-u (CPython 3.6.5)](https://github.com/python/cpython/blob/v3.6.5/Objects/listobject.c)

[^complexity]: [On the Worst-Case Complexity of TimSort](https://drops.dagstuhl.de/opus/volltexte/2018/9467/pdf/LIPIcs-ESA-2018-4.pdf).

[^powersort]: [CPython: commit koji uvodi Powersortovu strategiju redoslijeda spajanja](https://github.com/python/cpython/commit/5cb4c672d855033592f0e05162f887def236c00a); [opis strategije spajanja u CPythonu 3.11](https://github.com/python/cpython/blob/v3.11.0/Objects/listsort.txt#L329-L347).

[^merge-policy]: [CPython 3.6.5: `merge_collapse`](https://github.com/python/cpython/blob/v3.6.5/Objects/listobject.c#L1816-L1849).

[^merge-fix]: [CPython Issue 23515: Bad logic in timsort's merge\_collapse](https://bugs.python.org/issue23515).
