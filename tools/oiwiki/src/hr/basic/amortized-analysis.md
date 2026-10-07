---
title: Amortizirana složenost
---

Preduvjeti: [Vremenska složenost](./complexity.md)

Ova stranica predstavlja osnove amortizirane složenosti.

## Uvod

Amortizirana analiza (amortized analysis) tehnika je za analizu performansi algoritama i dinamičkih struktura podataka. Ne promatra samo cijenu pojedine operacije, nego procjenjuje prosječnu cijenu niza operacija i tako daje točniju sliku ukupnih performansi. Amortizirana analiza ne uključuje vjerojatnost; jamči samo prosječno vrijeme po operaciji u najgorem slučaju, a ne govori ništa o prosječnim performansama sustava. U najgorem slučaju amortizirana analiza raspodjeljuje trošak skupih operacija na jeftine i tako osigurava da prosječna cijena svih operacija ostane u razumnim granicama.

Amortizirana analiza obično se provodi na tri glavna načina: agregatnom analizom, metodom računovodstva i metodom potencijala. Svaka od njih ima drugačiji naglasak i prikladna je za drugačije situacije, ali im je zajednički cilj uravnotežiti cijene operacija i tako optimirati ukupne performanse strukture podataka u najgorem slučaju.

## Sadržaj

Promotrimo proširivi niz, npr. `vector` u C++-u, početnog kapaciteta $m = 1$. Pri svakom umetanju novog elementa, ako je niz pun, treba udvostručiti njegovu veličinu, kopirati elemente iz starog niza u novi i tek onda umetnuti novi element.

U nastavku ćemo na primjeru umetanja u dinamički niz analizirati amortiziranu cijenu trima metodama: agregatnom analizom, metodom računovodstva i metodom potencijala.

### Agregatna analiza

Agregatna analiza (aggregate analysis) računa ukupnu cijenu niza operacija i dijeli je na pojedine operacije, čime dobiva amortiziranu vremensku složenost po operaciji.

Na primjeru dinamičkog niza najprije uočimo dvije ključne cijene umetanja:

-   ako niz nije pun, umetanje stoji $O(1)$;
-   ako je niz pun, umetanje zahtijeva proširenje, a kopiranje elemenata nakon proširenja stoji $O(m)$, gdje je $m$ trenutna veličina niza.

Zato ukupnu cijenu $n$ umetanja možemo izračunati u dva dijela:

1.  **Cijena umetanja**: izravna cijena svakog umetanja novog elementa je konstantno vrijeme $O(1)$, pa je za $n$ operacija ukupna cijena $O(n)$;
2.  **Cijena proširenja niza**: svako proširenje uključuje kopiranje elemenata starog niza u novi. Te se operacije događaju kad je veličina niza potencija broja $2$. Zbroj starih kapaciteta koji se kopiraju pri proširenjima jednak je zbroju svih potencija broja $2$ strogo manjih od $n$; za $n\ge1$ ukupna cijena kopiranja je $\sum_{i=0}^{\lceil\log_2 n\rceil - 1}2^i=2^{\lceil\log_2 n\rceil}-1<2n$, dakle $O(n)$.

Stoga je ukupna cijena umetanja u taj niz $O(n)$, a amortizirano po operaciji $O(1)$. Čak i u najgorem slučaju, prosječna cijena jednog umetanja ostaje konstantno vrijeme.

### Metoda računovodstva

Metoda računovodstva (accounting method) svakoj operaciji unaprijed dodjeljuje fiksnu amortiziranu cijenu i tako osigurava da ukupna cijena svih operacija ne premaši zbroj tih unaprijed dodijeljenih cijena. Metoda računovodstva nalikuje mehanizmu **plaćanja unaprijed**: jeftinije operacije pohranjuju dio naknade kako bi se njome platile buduće skupe operacije.

Na primjeru dinamičkog niza, svakom umetanju možemo dodijeliti fiksnu amortiziranu cijenu kako bi u trenutku kad je potrebno proširenje već bila pohranjena dovoljna naknada.

1.  **Raspodjela naknade**:
    -   Pretpostavimo da je stvarna cijena svakog umetanja $1$, a amortizirana cijena neka je $3$.
    -   Od toga se $1$ troši na trenutno umetanje, a $2$ se čuva za moguće buduće proširenje.

2.  **Korištenje naknade**:
    -   Kad je niz pun, treba ga proširiti; stvarna cijena je $O(m)$, gdje je $m$ trenutna veličina niza.
    -   Pretpostavimo da niz prije proširenja ima $n$ elemenata. Budući da je $n/2$ elemenata u stražnjoj polovici niza pri umetanju ukupno pohranilo $n$ jedinica amortizirane cijene, to je upravo dovoljno da se plati proširenje.

Slijedi konkretan primjer:

```text
Početno stanje:
arr    = [1, 2, 3, 4]  // početni niz
amount = [2, 2, 2, 2]  // naknada pohranjena uz svaki element

// Prvo proširenje: niz je pun, treba ga proširiti
arr    = [1, 2, 3, 4, null, null, null, null]  // niz nakon proširenja
amount = [2, 2, 0, 0, 0, 0, 0, 0]  // naknade elemenata 3 i 4 plaćaju proširenje

// Nastavljamo umetati nove elemente dok se niz ponovno ne napuni
arr    = [1, 2, 3, 4, 5, 6, 7, 8]  // punimo niz dalje
amount = [2, 2, 0, 0, 2, 2, 2, 2]  // novoumetnuti elementi također pohranjuju naknadu

// Drugo proširenje: niz je ponovno pun, treba više prostora
arr    = [1, 2, 3, 4, 5, 6, 7, 8, null, null, null, null, null, null, null, null]  // niz nakon proširenja
amount = [2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  // naknade elemenata 5, 6, 7 i 8 plaćaju proširenje
```

Gornji postupak pokazuje da je amortizirana cijena pohranjena pri svakom umetanju dovoljna za plaćanje budućih proširenja, čime je amortizirana cijena svake operacije održana na $O(1)$.

### Metoda potencijala

Metoda potencijala (potential method) definira funkciju potencijala (obično označenu $\Phi$) koja mjeri **potencijalnu energiju** strukture podataka, tj. rezervirane resurse u stanju sustava kojima se mogu platiti buduće skupe operacije. Promjene potencijala služe za uravnoteženje ukupne cijene niza operacija, čime se osigurava da amortizirana cijena cijelog algoritma ostane u razumnim granicama.

#### Načelo

Najprije definiramo **stanje** $S$ kao stanje strukture podataka u nekom trenutku; ono može sadržavati broj elemenata, kapacitet, pokazivače i slične podatke. Početno stanje, tj. stanje prije ikakve operacije, označavamo $S_0$.

Zatim definiramo funkciju potencijala $\Phi(S)$ koja mjeri potencijal stanja $S$ strukture podataka. Uz početno stanje $S_0$, potencijal svakog dostižnog stanja $S$ mora zadovoljavati $\Phi(S) \geq \Phi(S_0)$[^clemson][^uci][^stanford]; neki izvori dodatno zahtijevaju $\Phi(S_0)=0$[^cornell], što zapravo nije nužno.

Za svaku operaciju amortizirana cijena $\hat{c}$ definira se kao:

$$
\hat{c} = c + \Phi(S') - \Phi(S)
$$

gdje je $c$ stvarna cijena operacije, a $S$ i $S'$ stanja strukture podataka prije i poslije operacije. Formula kaže da je amortizirana cijena jednaka stvarnoj cijeni uvećanoj za promjenu potencijala. Ako operacija povećava potencijal (tj. $\Phi(S') > \Phi(S)$), amortizirana cijena raste; ako operacija troši potencijal (tj. $\Phi(S') < \Phi(S)$), amortizirana cijena pada.

Pomoću funkcije potencijala možemo analizirati ukupnu cijenu niza operacija. Neka su $S_1, S_2, \dots, S_m$ stanja koja nastaju iz početnog stanja $S_0$ nakon $m$ operacija, a $c_i$ stvarna cijena $i$-te operacije. Tada je amortizirana cijena $p_i$ $i$-te operacije:

$$
p_i = c_i + \Phi(S_i) - \Phi(S_{i-1})
$$

Stoga je ukupni vremenski trošak $m$ operacija:

$$
\sum_{i=1}^m c_i = \sum_{i=1}^m p_i + \Phi(S_0) - \Phi(S_m)
$$

Budući da je $\Phi(S) \geq \Phi(S_0)$, gornja granica ukupnog vremenskog troška je:

$$
\sum_{i=1}^m p_i \geq \sum_{i=1}^m c_i
$$

Dakle, ako je $p_i = O(T(n))$, onda je $O(T(n))$ gornja granica amortizirane složenosti.

#### Primjer: analiza proširenja dinamičkog niza

Na primjeru umetanja u dinamički niz `vector`, označimo početno stanje $h_0$ i definirajmo funkciju potencijala $\Phi(h)$:

$$
\Phi(h) = 2n - m
$$

gdje je $n$ broj elemenata u nizu, a $m$ trenutni kapacitet niza. Promjene te funkcije potencijala odražavaju povećanje i smanjenje unaprijed pohranjene naknade za buduća proširenja. U početnom stanju praznog niza kapaciteta $1$ vrijedi $\Phi(h_0)=-1$; u svim nepraznim dostižnim stanjima (samo umetanja, udvostručavanje kad je pun) vrijedi $m\leq 2n$, pa je $\Phi(h)\geq 0>\Phi(h_0)$.

1.  **Umetanje (bez proširenja)**:
    -   **Cijena operacije**: $O(1)$, jer se umeće samo jedan element.
    -   **Promjena potencijala**: nakon umetanja broj elemenata raste za 1, a potencijal za $2$.
        -   $\Phi(h') - \Phi(h) = 2(n + 1) - m - (2n - m) = 2$.
    -   **Amortizirana cijena**: $1 + 2 = 3$.

2.  **Umetanje (s proširenjem)**:
    -   Pretpostavimo da je trenutni kapacitet $m = n$; umetanje novog elementa pokreće proširenje i novi kapacitet postaje $2n$.
    -   **Cijena operacije**: $O(n)$, jer treba kopirati sve elemente u novi niz i umetnuti novi element.
    -   **Promjena potencijala**: nakon proširenja i umetanja potencijal se mijenja za $2-n$, što je pad tek za $n>2$.
        -   $\Phi(h') - \Phi(h) = 2(n + 1) - 2n - (2n - n) = 2 - n$.
    -   **Amortizirana cijena**: $n + 1 + (2 - n) = 3$.

Iz analize se vidi da, iako je stvarna cijena proširenja visoka, zbog oblika funkcije potencijala ukupna amortizirana cijena ostaje konstantna, $O(1)$.

## Prošireni primjer: operacije na stogu

Operacije na stogu klasičan su primjer primjene amortizirane analize. Pretpostavimo da krećemo od praznog stoga, da se `pop` poziva samo na nepraznom stogu i da stog `S` podržava sljedeće tri operacije:

| Operacija        | Opis                                       | Stvarna cijena $c_i$        |
| ---------------- | ------------------------------------------ | --------------------------- |
| `S.push(x)`      | stavlja element $x$ na stog                | $1$                         |
| `S.pop()`        | skida element s vrha stoga                 | $1$                         |
| `S.multi-pop(k)` | skida najviše $k$ elemenata s vrha stoga   | $O(\min(\lvert S\rvert,k))$ |

Amortiziranu cijenu tih operacija analizirat ćemo trima metodama: agregatnom analizom, metodom računovodstva i metodom potencijala.

### Agregatna analiza

Agregatna analiza računa ukupnu cijenu svih operacija i ravnomjerno je raspodjeljuje na svaku operaciju, čime dobiva amortiziranu cijenu.

1.  Za $n_{\text{push}}$ operacija `push(x)` svaka stoji $O(1)$, pa je ukupna cijena $O(n_{\text{push}})$;
2.  za $n_{\text{pop}}$ operacija `pop()` svaka stoji $O(1)$, pa je ukupna cijena $O(n_{\text{pop}})$;
3.  za $n_{\text{multi-pop}}$ operacija `multi-pop(k)`, iako je stvarna cijena svake $O(\min(\lvert S \rvert, k))$, broj elemenata koje te operacije skinu ne može premašiti broj prethodno stavljenih elemenata `push(x)`, pa je ukupna cijena i dalje ograničena s $n_{\text{push}}$.

Ukupan broj operacija je $n=n_{\text{push}}+n_{\text{pop}}+n_{\text{multi-pop}}$, pri čemu je $n_{\text{push}}\le n$. Svaki element najviše jednom ulazi na stog i najviše jednom izlazi s njega, pa je ukupna cijena obračunata po elementima $O(n_{\text{push}})=O(n)$; čak i ako posebno uračunamo konstantan trošak provjere pri svakom pozivu, ukupna cijena ostaje $O(n)$, a amortizirana $O(1)$.

### Metoda računovodstva

Metoda računovodstva pri svakom `push(x)` rezervira dio naknade za plaćanje mogućih budućih operacija `pop()` ili `multi-pop(k)`.

1.  **`S.push(x)`**: neka je amortizirana cijena svakog `push(x)` jednaka $2$; $1$ jedinica troši se na trenutnu operaciju, a druga se $1$ jedinica pohranjuje kao naknada za buduće operacije `pop()` ili `multi-pop(k)`;
2.  **`S.pop()`**: stvarna cijena je $1$, ali je prethodni `push(x)` za nju već pohranio $1$ jedinicu naknade, pa je amortizirana cijena $0$;
3.  **`S.multi-pop(k)`**: stvarna cijena svakog skinutog elementa je $1$ i može se platiti naknadom koju je ranije pohranio `push(x)` tog elementa, pa je amortizirana cijena $0$.

Iz analize slijedi da je naknada pohranjena pri stavljanju na stog dovoljna za buduće skidanje tog elementa, pa je amortizirana cijena svake operacije $O(1)$.

### Metoda potencijala

Metoda potencijala definira funkciju potencijala kojom mjeri stanje stoga i promjenama potencijala uravnotežuje cijene operacija.

1.  **Funkcija potencijala**: neka je $\Phi(h)$ broj elemenata na stogu, tj. $\Phi(h) = \lvert S \rvert$. Svaki element pridonosi $1$ jedinicu potencijala;
2.  **`S.push(x)`**: svaki `push(x)` povećava broj elemenata na stogu, potencijal raste za $1$, pa je amortizirana cijena $1 + 1 = 2$;
3.  **`S.pop()`**: svaki `pop()` smanjuje broj elemenata na stogu, potencijal pada za $1$, pa je amortizirana cijena $1 - 1 = 0$;
4.  **`S.multi-pop(k)`**: neka je $t=\min(\lvert S\rvert,k)$; `multi-pop(k)` zapravo skida $t$ elemenata, potencijal pada za $t$, pa je amortizirana cijena obračunata po elementima $t-t=0$; uračunamo li i trošak poziva, iznosi $O(1)$.

Uz ovako definiranu funkciju potencijala amortizirana cijena operacije `push(x)` je $2$, a operacija `pop()` i `multi-pop(k)` $0$. Stoga je amortizirana cijena svih operacija na stogu $O(1)$.

## Literatura i bilješke

-   [Amortized Analysis - Wikipedia](https://en.wikipedia.org/wiki/Amortized_analysis)

[^clemson]: [Clemson University - Amortized Analysis + Splay Trees](https://people.computing.clemson.edu/~srimani/8380_F22/Course_Materials_Web/5_F22_Amortized%20Analysis%2BSplay%20Trees.pdf#page=8)

[^uci]: [UC Irvine - Amortized Analysis](https://ics.uci.edu/~goodrich/teach/cs263/notes/02-Amortized.pdf#page=5)

[^stanford]: [Stanford CS166 - Amortized Analysis](https://web.stanford.edu/class/archive/cs/cs166/cs166.1206/lectures/07/Small07.pdf#page=69)

[^cornell]: [Cornell CS 3110 - Lecture 20: Amortized Analysis](https://www.cs.cornell.edu/courses/cs3110/2011sp/Lectures/lec20-amortized/amortized.htm)
