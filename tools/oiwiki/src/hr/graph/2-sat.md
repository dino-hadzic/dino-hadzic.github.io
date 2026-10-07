---
title: 2-SAT
---

SAT je kratica za problem ispunjivosti (Satisfiability). Opći oblik je problem k-ispunjivosti, kraće k-SAT. Za $k>2$ problem je NP-potpun, pa proučavamo samo slučaj $k=2$.

## Definicija

2-SAT, jednostavno rečeno, zadaje $n$ logičkih (Booleovih) formula, od kojih se svaka odnosi na dvije varijable, npr. $a \vee b$, što znači da barem jedna od varijabli $a, b$ mora biti istinita. Zatim treba odrediti postoji li zadovoljavajuća dodjela vrijednosti; očito ih može biti više, a u zadacima obično treba naći jednu. Nadalje, $\neg a$ označava negaciju od $a$.

## Pristup rješavanju

???+ example "[Luogu P4782 „Predložak” 2-SAT](https://www.luogu.com.cn/problem/P4782)"
    Zadano je $n$ logičkih varijabli $x_1\sim x_n$ i $m$ uvjeta koje treba zadovoljiti; svaki je uvjet oblika „$x_i$ je `true`/`false` ili $x_j$ je `true`/`false`”. Na primjer „$x_1$ je istinit ili $x_3$ je lažan”, „$x_7$ je lažan ili $x_2$ je lažan”.
    
    Cilj 2-SAT problema je svakoj varijabli dodijeliti vrijednost tako da svi uvjeti budu zadovoljeni.

Gornji problem zapisujemo logičkim formulama. Neka $a$ znači da je $x_a$ istinit ($\neg a$ tada znači da je $x_a$ lažan). Ako netko postavi zahtjeve $a$ i $b$, to je $(a \vee b)$ (barem jedna od varijabli $a, b$ je istinita). Za te odnose među varijablama gradimo usmjereni graf: istinitost i neistinitost od $a$ prikazujemo vrhovima grafa, a bridovi $\neg a\to b$ i $\neg b\to a$ znače: ako $a$ **ne vrijedi**, tada $b$ **sigurno vrijedi**; isto tako, ako $b$ **ne vrijedi**, tada $a$ **sigurno vrijedi**. Nakon što izgradimo graf, 2-SAT problem možemo riješiti algoritmom za sažimanje jako povezanih komponenata.

|      Izvorna formula      |              Bridovi u grafu              |
| :----------------: | :-----------------------------: |
|   $\neg a \vee b$  | $a \to b$ i $\neg b \to \neg a$ |
|     $a \vee b$     | $\neg a \to b$ i $\neg b \to a$ |
| $\neg a\vee\neg b$ | $a \to \neg b$ i $b \to \neg a$ |

U mnogim 2-SAT zadacima treba pronaći odnose oblika „ako $a$ **ne vrijedi**, tada $b$ **vrijedi**”.

## Rješavanje

Razmislimo što znači da su dva vrha u istoj jako povezanoj komponenti. Prema logičkom značenju bridova iz prethodnog odjeljka: ako su dva vrha u istoj jako povezanoj komponenti, uvjeti koje ta dva vrha predstavljaju **ili su oba zadovoljeni ili nijedan nije**.

Nakon izgradnje grafa [Tarjanovim algoritmom pronađemo SCC-ove](./scc.md) i za svaku logičku varijablu $a$ provjerimo jesu li vrh koji predstavlja „$a$ vrijedi” i vrh koji predstavlja „$a$ ne vrijedi” u istoj SCC (isti uvjet ne može biti istodobno zadovoljen i nezadovoljen, niti istodobno nezadovoljen i ne-nezadovoljen); ako jesu, ispisujemo da rješenja nema, inače rješenje postoji.

Pri ispisu rješenja vrijednost varijable određuje se prema topološkom poretku u grafu. Ako je varijabla $x$ u topološkom poretku iza $\neg x$, uzmemo $x$ kao istinito. Primijenjeno na sažimanje Tarjanovim algoritmom: kad je indeks SCC-a koji sadrži $x$ manji od indeksa SCC-a koji sadrži $\neg x$, uzimamo $x$ kao istinito. Naime, Tarjanov algoritam pri traženju jako povezanih komponenata koristi stog: komponenta koja je nakon sažimanja kasnije u topološkom poretku u Tarjanu se kasnije posjeti, pa se ranije izbaci sa stoga i sažme, te dobiva manji indeks. Zato su indeksi SCC-ova koje daje Tarjan zapravo **obrnuti topološki poredak**.

Algoritam jednom obiđe cijeli graf; budući da su u tom grafu $n$ i $m$ istog reda veličine, računanje odgovora ima složenost $O(n)$, pa je ukupna složenost $O(n)$.

??? note "Implementacija"
    ```cpp
    --8<-- "docs/graph/code/2-sat/2-sat_3.cpp"
    ```

## Primjeri

### Primjer 1

???+ example "[HDU3062 Party](https://acm.hdu.edu.cn/showproblem.php?pid=3062)"
    Na zabavu je pozvano $n$ bračnih parova, ali zbog prostora iz svakog para može doći samo jedna osoba. Među tih $2n$ ljudi neki su u velikom sukobu (naravno, supružnici međusobno nisu), a dvoje ljudi u sukobu neće se istodobno pojaviti na zabavi. Može li na zabavi istodobno biti $n$ ljudi?

Prema gornjoj analizi, ako se muž iz para $a_1$ ne slaže sa ženom iz para $a_2$, spojimo bridom muža iz $a_1$ s mužem iz $a_2$ i ženu iz $a_2$ sa ženom iz $a_1$, a zatim sažmemo komponente, obojimo ih i provjerimo.

??? note "Referentni kôd"
    ```cpp
    --8<-- "docs/graph/code/2-sat/2-sat_1.cpp"
    ```

### Primjer 2

???+ example "[2018-2019 ACM-ICPC Asia Seoul Regional K TV Show Game](https://codeforces.com/gym/101987/problem/K)"
    Zadano je $k$ lampica, svaka je crvena ili plava, ali boje u početku nisu poznate. Ima $n$ ljudi; svaki odabere tri lampice i pogađa njihove boje. Osoba koja pogodi boje barem dviju lampica dobiva nagradu. Odredi postoji li bojanje lampica pri kojem svi dobivaju nagradu; ako postoji, ispiši jedno takvo bojanje.

Prema [Wu Yu – „Rješavanje 2-SAT problema pomoću simetrije”](https://github.com/OI-wiki/libs/blob/master/%E9%9B%86%E8%AE%AD%E9%98%9F%E5%8E%86%E5%B9%B4%E8%AE%BA%E6%96%87/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2003%E8%AE%BA%E6%96%87%E9%9B%86/%E4%BC%8D%E6%98%B1--%E7%94%B1%E5%AF%B9%E7%A7%B0%E6%80%A7%E8%A7%A32-SAT%E9%97%AE%E9%A2%98/%E4%BC%8D%E6%98%B1.ppt) zaključujemo: želimo li ispisati jedno dopustivo rješenje 2-SAT problema, dovoljno je na DAG-u dobivenom sažimanjem Tarjanovim algoritmom birati i brisati odozdo prema gore.

U implementaciji se to može izvesti izgradnjom obrnutog grafa DAG-a i topološkim sortiranjem na njemu; ili se može iskoristiti svojstvo da nakon Tarjanova sažimanja manji indeks komponente znači da je vrh bliže listovima, pa prednost pri odabiru dajemo vrhovima s manjim indeksom komponente.

Slijedi kôd drugog načina implementacije.

??? note "Referentni kôd"
    ```cpp
    --8<-- "docs/graph/code/2-sat/2-sat_2.cpp"
    ```

## Zadaci

-   [Luogu P5782 Mirovni odbor](https://www.luogu.com.cn/problem/P5782)
-   [POJ3683 Priest John's Busiest Day](http://poj.org/problem?id=3683)
