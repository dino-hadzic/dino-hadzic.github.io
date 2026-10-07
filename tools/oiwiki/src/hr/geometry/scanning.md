---
title: Sweep line
---

## Uvod

Sweep line (pomični pravac, „pravac koji mete”) obično se primjenjuje na geometrijske likove; sasvim u skladu s imenom, riječ je o pravcu koji prelazi („mete”) preko cijele slike. Obično se koristi za rješavanje problema površine i opsega likova te za dvodimenzionalno brojanje točaka i slično.

## Unija površina pravokutnika u ravnini

U dvodimenzionalnom koordinatnom sustavu zadani su donji lijevi i gornji desni vrhovi više pravokutnika; treba izračunati površinu lika koji čine svi pravokutnici zajedno.

### Postupak

Prema slici je jasno da se ukupna površina može izračunati izravno, grubom silom. Što ako su podaci veliki? Tu na red dolazi algoritam **sweep line**.

Zamislimo da imamo pravac koji kreće odozdo i pomiče se prema gore:

![](./images/scanning.svg)

Kao na slici, cijeli lik podijelimo na male pravokutnike različitih boja; visina malog pravokutnika je prijeđena udaljenost, ali se vodoravna širina stalno mijenja.

Svakom pravokutniku označimo donji i gornji rub: donji rub oznakom 1, a gornji oznakom -1. Kad god naiđemo na vodoravni rub, težini tog ruba (na njegovoj projekciji na vodoravnu os) dodamo njegovu oznaku.

???+ note "Napomena"
    Ova operacija nalikuje prolasku kroz niz zagrada: otvorena zagrada dodaje 1, zatvorena oduzima 1; „težina” odgovara trenutnoj dubini, a to je li „težina” veća od 0 odgovara tome jesmo li trenutno unutar zagrada, odnosno ulazi li taj interval u širinu malog pravokutnika.

Širina malih pravokutnika (ne mora biti samo jedan) jest ukupna duljina intervala na brojevnom pravcu na kojima je težina veća od 0.

### Implementacija

Segment treeom održavamo duljinu pravokutnika, tj. točke brojevnog pravca čiji je broj pokrivanja veći od 0. Zahtjevi su sljedeći:

-   dodati 1 ili oduzeti 1 težini na nekom intervalu;
-   izračunati, na cijelom brojevnom pravcu, „zbroj duljina intervala” čija je težina veća od 0.

Ako to pokušate izravno implementirati običnim predloškom segment treea, možda ćete naići na poteškoće. Konkretno, pri dodavanju na intervalu, čak i kad se interval izmjene podudara s intervalom čvora, ne možemo u konstantnom vremenu znati kako se mijenja broj pokrivanja. Razlog je što ne znamo izravno koliko se duljine unutar raspona čvora mijenja iz 1 u 0 (ili iz 0 u 1).

Ovaj se zadatak može riješiti jednostavnim postupkom podijeli pa vladaj: za svaki čvor čuvamo dva podatka – „broj potpunih pokrivanja njegova intervala `v[]`” (nalik lijenoj oznaci koju ne treba propagirati) i „pokrivenu duljinu `w[]`”.

Potrebna je [kompresija koordinata](../misc/discrete.md).

??? note "[Luogu P5490 [Predložak] Sweep line i unija površina pravokutnika](https://www.luogu.com.cn/problem/P5490) – referentni kod"
    ```cpp
    --8<-- "docs/geometry/code/scanning/scanning_1.cpp"
    ```

??? note "[„POJ 1151” Atlantis](http://poj.org/problem?id=1151) – referentni kod"
    ```cpp
    --8<-- "docs/geometry/code/scanning/scanning_2.cpp"
    ```

### Zadaci za vježbu

-   [„POJ1177” Picture](http://poj.org/problem?id=1177)
-   [„POJ3832” Posters](http://poj.org/problem?id=3832)
-   [Luogu P1856 \[IOI1998\] \[USACO5.5\] Opseg pravokutnika Picture](https://www.luogu.com.cn/problem/P1856)
    -   Doprinos vodoravnih rubova jest promjena pokrivene duljine.
    -   Ako posebno računamo u oba smjera, izbjegavamo razmatranje okomitih rubova.
    -   Pri sortiranju operacija pazite na slučaj kad se rubovi dvaju pravokutnika podudaraju.
    -   Ograničenja dopuštaju da se umjesto segment treea izravno simulira u kvadratnom vremenu.

## B-dimenzionalni ortogonalni raspon

B-dimenzionalni ortogonalni raspon je skup točaka u B-dimenzionalnom pravokutnom koordinatnom sustavu čija je $i$-ta koordinata u cjelobrojnom rasponu $[l_i,r_i]$.

Općenito, jednodimenzionalni ortogonalni raspon kraće zovemo interval, dvodimenzionalni pravokutnik, a trodimenzionalni kvadar (ono što često zovemo dvodimenzionalno brojanje točaka upravo je dvodimenzionalni ortogonalni raspon).

Za statički dvodimenzionalni problem možemo jednu dimenziju obraditi sweep lineom, a drugu održavati strukturom podataka.
Dok se sweep line pomiče slijeva nadesno, u dimenziji koju održava struktura podataka nastaju izmjene i upiti.
Ako je tražena informacija diferencijabilna (može se rastaviti na razlike), koristimo razlike; inače treba podijeli pa vladaj. Razlike se obično održavaju Fenwick treeom ili segment treeom, ali budući da se Fenwick tree lakše piše i ima manju konstantu, većina bira Fenwick tree. Podijeli pa vladaj obično je CDQ podijeli pa vladaj (ali ovdje se njime ne bavimo).

Drugi, lakše razumljiv pogled na problem jest gledati ga kao problem na nizu, a ne u ravnini. Ako tako gledamo, sweep line zapravo nabraja desni kraj $r=1\cdots n$ i održava strukturu podataka koja za trenutni $r$ i zadani $l$ odgovara koji je odgovor za interval od $l$ do $r$. Dakle sweep line prolazi kroz desne krajeve upita, a struktura podataka održava odgovore za sve lijeve krajeve; drugim riječima, prolazimo kroz jednu dimenziju, a struktura podataka održava drugu.

Složenost je obično $O((n+m)\log n)$.

## Dvodimenzionalno brojanje točaka

Zadan je niz duljine $n$ i $m$ upita; svaki upit traži broj elemenata na intervalu $[l,r]$ čija je vrijednost u $[x,y]$.

Taj se problem zove dvodimenzionalno brojanje točaka. Lako je vidjeti da je ekvivalentan upitu o broju točaka unutar pravokutnika u ravnini. Ovdje opisujemo najjednostavniji način rješavanja: sweep line + Fenwick tree.

Očito je riječ o statičkom dvodimenzionalnom problemu; sweep lineom ga pretvaramo u dinamički jednodimenzionalni problem. Dinamički jednodimenzionalni problem rješavamo strukturom podataka nad nizom; ovdje možemo koristiti Fenwick tree.

Najprije komprimiramo koordinate svih upita i Fenwick treeom održavamo vrijednosti. Za $l$ i $r$ svakog upita, kad u nabrajanju dođemo do $l-1$, prebrojimo koliko je trenutno brojeva u intervalu $[x,y]$ – neka ih je $a$; nastavljamo nabrajati i kad dođemo do $r$, prebrojimo koliko je trenutno brojeva u intervalu $[x,y]$ – neka ih je $b$. Tada je $b-a$ odgovor na taj upit.

### Primjeri

???+ note "[Luogu P2163 \[SHOI2007\] Vrtlarove nevolje](https://www.luogu.com.cn/problem/P2163)"
    Najprije komprimiramo koordinate. Neka pravokutnik s donjim lijevim vrhom $(0, 0)$ i gornjim desnim vrhom $(x, y)$ sadrži $ans_{x, y}$ točaka. Odgovor na upit tada se rastavlja na razlike kao $ans_{c, d} - ans_{a - 1, d} - ans_{c, b - 1} + ans_{a - 1, b - 1}$.
    
    ??? note "Kod"
        ```cpp
        --8<-- "docs/geometry/code/scanning/scanning_3.cpp"
        ```

???+ note "[Luogu P1908 Inverzije](https://www.luogu.com.cn/problem/P1908)"
    Da, i inverzije se mogu brojati idejom sweep linea. Brojanje inverzija pretvorimo u sljedeće: nabrajamo položaje $i$ od kraja prema početku i tražimo broj točaka na intervalu $[i+1,n]$ čija je vrijednost u intervalu $[0,a_i]$. Vrijednosti u zadatku su do $10^9$, pa očito najprije treba komprimirati koordinate. Niz prolazimo od kraja prema početku; za svaki broj ažuriramo Fenwick tree (ili segment tree), a zatim prebrojimo koliko je dosad brojeva manjih od trenutnog. Budući da idemo od kraja prema početku, broj manjih brojeva upravo je broj inverzija koje trenutni broj tvori; dovoljne su izmjena u točki i upit na intervalu Fenwick treeom ili segment treeom.
    
    ??? note "Kod"
        ```cpp
        --8<-- "docs/geometry/code/scanning/scanning_4.cpp"
        ```

???+ note "[Luogu P1972 \[SDOI2009\] HH-ova ogrlica](https://www.luogu.com.cn/problem/P1972)"
    Kratki opis zadatka: zadan je niz; više puta se pita koliko različitih brojeva ima na intervalu $[l,r]$.
    
    Za ovakve probleme možemo izvesti neka svojstva, a zatim sweep lineom nabrajati sve desne krajeve dok struktura podataka održava odgovor za svaki lijevi kraj; problem možemo prebaciti i u ravninu, gdje postaje upit o informaciji unutar pravokutnika.
    
    U ovom zadatku neka je $pre_i$ položaj prethodnog pojavljivanja vrijednosti $a_i$ u nizu; ako se $a_i$ prije nije pojavio, $pre_i = 0$. Prema uvjetima zadatka, ako se neka vrijednost pojavi više puta na intervalu, pridonosi samo jednom. Dogovorimo se da svaka vrijednost pridonosi na mjestu svog prvog pojavljivanja na intervalu; tada se vidi da je ukupni doprinos broj indeksa $x$ s $pre_x \le l - 1$, što se lako dokazuje kontradikcijom.
    
    Problem je sada: zadan je niz $pre$; više puta se pita koliko je $i$ na intervalu $[l,r]$ takvih da je $pre_i \le l - 1$.
    
    Svaki $pre_i$ možemo gledati kao točku u ravnini: $i$ je x-koordinata, a $pre_i$ y-koordinata. Problem tako postaje dvodimenzionalno brojanje točaka: koliko točaka ima u pravokutniku s donjim lijevim vrhom $(l,0)$ i gornjim desnim vrhom $(r,l - 1)$.
    
    Uočimo da je upit diferencijabilan: možemo ga rastaviti na broj točaka u pravokutniku s donjim lijevim vrhom $(0,0)$ i gornjim desnim $(r,l - 1)$ minus broj točaka u pravokutniku s donjim lijevim vrhom $(0,0)$ i gornjim desnim $(l - 1,l - 1)$, što nam olakšava primjenu ideje sweep linea.
    
    Jedna operacija košta $O(\log n)$; ukupno je $n$ operacija dodavanja točke i $2m$ upita, pa je ukupna vremenska složenost $O((n + m) \log n)$.
    
    ??? note "Kod"
        ```cpp
        --8<-- "docs/geometry/code/scanning/scanning_5.cpp"
        ```

### Zadaci za vježbu

-   [Luogu P8593 „KDOI-02” Jedan hitac](https://www.luogu.com.cn/problem/P8593) primjena inverzija.
-   [AcWing 4709. Trojke](https://www.acwing.com/problem/content/4712/) lakša inačica prethodnog zadatka, također primjena inverzija.
-   [Luogu P8773 \[Lanqiao Cup 2022 pokrajinsko A\] XOR odabranih brojeva](https://www.luogu.com.cn/problem/P8773) izmijenjena inačica HH-ove ogrlice.
-   [Luogu P8844 \[Chuanzhi Cup #4 kvalifikacije\] Xiao Ka i opalo lišće](https://www.luogu.com.cn/problem/P8844) problem na stablu pretvoren u problem na nizu, a zatim dvodimenzionalno brojanje točaka.

Ukratko, glavna ideja dvodimenzionalnog brojanja točaka jest da struktura podataka održava jednu dimenziju, a mi nabrajamo drugu.

## Literatura

-   [cnblogs/Yang1208: objašnjenje sweep linea, segment tree s dinamičkim stvaranjem čvorova](https://www.cnblogs.com/yangsongyi/p/8378629.html)
-   [csdn/riba2534: rješenje zadatka POJ1151 Atlantis](https://blog.csdn.net/riba2534/article/details/76851233)
-   [csdn/刀刀狗 0102: rješenje zadatka POJ1151 Atlantis](https://blog.csdn.net/winddreams/article/details/38495093)
-   [Kratko o sweep lineu](https://www.luogu.com.cn/article/f8q5bmnz)
