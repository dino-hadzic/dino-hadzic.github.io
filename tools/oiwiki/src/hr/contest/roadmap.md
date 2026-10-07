---
title: Put učenja
---

???+ note "Napomena"
    Ovaj se članak još uređuje i o njemu se raspravlja; slobodno dopunite put učenja ili iznesite svoje ideje u komentarima!

Ovaj članak predstavlja put učenja za algoritamska natjecanja.

Taj put učenja ujedno je vodič početnicima za učenje gradiva algoritamskih natjecanja i popis za ponavljanje.

## 1 Osnove jezika C++

Krenite od sintakse jezika C++, korak po korak.

### 1.1 Hello, World!

Započnite svoje putovanje algoritamskim natjecanjima rečenicom `Hello, World!`

Usput upoznajte kako otprilike izgleda okvir izvornog programa u C++-u.

-   [Hello, World!](../lang/helloworld.md)
-   [Osnove sintakse jezika C++](../lang/basic.md)

### 1.2 Varijable i operacije

Računala su izvorno nastala radi računanja. Zato prvo naučimo kako obaviti neke jednostavne računske zadatke.

-   [Varijable](../lang/var.md)
-   [Operacije](../lang/op.md)

### 1.3 Upravljanje tokom programa

#### 1.3.1 Grananje

Ponekad pod različitim uvjetima trebamo izvršiti različite naredbe; tada nam trebaju naredbe grananja.

-   [Grananje](../lang/branch.md)

Naredbe grananja uključuju sljedeće:

-   naredbu if
-   naredbu if-else
-   naredbu if-elif-else
-   naredbu switch

#### 1.3.2 Petlje

Da bismo nekoliko naredbi izvršili više puta, trebamo naredbe petlje.

-   [Petlje](../lang/loop.md)

Naredbe petlje uključuju sljedeće:

-   naredbu for
-   naredbu while
-   naredbu do-while

### 1.4 Polja i strukture

Polja služe za pohranu velike količine podataka istog tipa. Strukture pak mogu povezati više varijabli u cjelinu.

-   [Polja](../lang/array.md)
-   [Strukture](../lang/struct.md)

### 1.5 Funkcije i rekurzija

Funkcijama program činimo modularnim i smanjujemo trošak implementacije.

Rekurzija je prva prepreka za početnike: „funkcija poziva samu sebe” ne zvuči baš lako razumljivo, ali ako se pažljivo udubite u bit, otkrit ćete da između „pozvati samog sebe” i „pozvati nekog drugog” nema bitne razlike.

-   [Funkcije](../lang/func.md)
-   [Rekurzija i podijeli pa vladaj](../basic/divide-and-conquer.md)

## 2 CSP-J, početna razina

### 2.1 Enumeracija i simulacija

Od sada već znate jezikom C++ obaviti neke jednostavne zadatke, ali to je daleko od dovoljnog.

Da biste točno riješili neke jednostavne zadatke, morate naučiti implementirati kôd enumeracijom (iscrpnim ispitivanjem) ili simulacijom logike koju imate u glavi. To ne izgleda osobito učinkovito, ali je ponekad vrlo korisno.

-   [Enumeracija](../basic/enumerate.md)
-   [Simulacija](../basic/simulate.md)

### 2.2 Rekurzija i podijeli pa vladaj

Rekurzija je metoda u kojoj funkcija u svojoj definiciji neprestano poziva samu sebe, a podijeli pa vladaj je postupak u kojem se problem neprestano razlaže na više potproblema koji se riješe i zatim spoje.

-   [Rekurzija i podijeli pa vladaj](../basic/divide-and-conquer.md)

### 2.3 Stringovi

Pri rješavanju informatičkih zadataka često se susreće tip podataka string; trebate naučiti neke STL funkcije za rad sa stringovima. Naravno, i simulacija je dobar način rješavanja zadataka sa stringovima.

-   [Osnove stringova](../string/basic.md)
-   [STL funkcije](../string/lib-func.md)

### 2.4 Sortiranje

Kad dobijete skup podataka, važno je pitanje i kako ih od nesređenih učiniti sređenima. Kad nemate ideju, razmislite o tome da sortirate polje. To je i temelj mnogih algoritama koji slijede.

Metoda sortiranja ima podosta, ali kad ih razumijete, nije ih teško zapamtiti.

-   [Uvod u sortiranje](../basic/sort-intro.md)
-   [Selection sort](../basic/selection-sort.md)
-   [Bubble sort](../basic/bubble-sort.md)
-   [Insertion sort](../basic/insertion-sort.md)
-   [Counting sort](../basic/counting-sort.md)
-   [Radix sort](../basic/radix-sort.md)
-   [Quick sort](../basic/quick-sort.md)
-   [Merge sort](../basic/merge-sort.md)
-   [Heap sort](../basic/heap-sort.md)
-   [Bucket sort](../basic/bucket-sort.md)
-   [STL za sortiranje](../basic/stl-sort.md)

NOI-jev program za početnu razinu zahtijeva samo selection, bubble i insertion sort, ukupno tri algoritma sortiranja, ali ni ostali nisu osobito teški i mogu se pojaviti u prvom krugu, pa su navedeni zajedno.

### 2.5 Binarno pretraživanje i binary lifting

Binarno pretraživanje (binary search) u biti primjenjuje ideju podijeli pa vladaj: neprestano smanjuje raspon pretraživanja dok se ne nađe odgovor. No treba paziti da se taj način pretraživanja mora primjenjivati na sređenim strukturama podataka.

-   [Binarno pretraživanje](../basic/binary.md)

Binary lifting (metoda udvostručavanja) je drukčiji: neprestanim udvostručavanjem obradu u linearnom opsegu pretvara u logaritamsku i time znatno popravlja vremensku složenost. (Za ovo gradivo treba malo matematičke podloge; nije problem zasad ga preskočiti.)

-   [Binary lifting](../basic/binary-lifting.md)

### 2.6 Pretraživanje

U početnoj skupini zadaci s pretraživanjem često se pojavljuju kao zadaci s labirintima, obično s podacima u obliku karte; osim toga, pretraživanje se vrlo često koristi za učinkovitu enumeraciju pri konstrukciji valjanih rješenja, a može poslužiti i za skupljanje djelomičnih bodova.

#### 2.6.1 Pretraživanje u dubinu (DFS)

Pretraživanje u dubinu označava algoritam koji rekurzivnom funkcijom jednostavno ostvaruje enumeraciju grubom silom; donekle je sličan algoritmu DFS iz teorije grafova, ali nije posve isti.

-   [DFS (pretraživanje)](../search/dfs.md)

#### 2.6.2 Pretraživanje u širinu (BFS)

Ako svako stanje zamislimo kao vrh grafa, možemo provesti sustavno pretraživanje.

-   [BFS (pretraživanje)](../search/bfs.md)

#### 2.6.3 Optimizacija pretraživanja

Mnogi se zadaci mogu riješiti DFS-om, ali složenost tog algoritma očito nije prolazna. Zato su potrebne optimizacije da bi radio brže. Takve optimizacije smanjuju broj pokušaja koji ne mogu uspjeti i zovu se „rezanje” (pruning). Optimizacije vezane uz BFS fleksibilnije su, ali osnovna je ideja ista kao ovdje.

-   [Optimizacija DFS-a rezanjem](../search/opt.md)

### 2.7 Uvod u strukture podataka

#### 2.7.1 Linearne strukture podataka

Polja, vezane liste, redovi i stogovi linearne su strukture. Vještom upotrebom tih struktura može se učiniti mnogo praktičnih stvari.

-   [Stog](../ds/stack.md)
-   [Red](../ds/queue.md)
-   [Vezana lista](../ds/linked-list.md)

#### 2.7.2 Složenije strukture podataka

-   [Stabla i binarna stabla](../graph/tree-basic.md)
-   [Pojam grafa](../graph/concept.md)
-   [Pohrana grafa](../graph/save.md)

### 2.8 Uvod u dinamičko programiranje

Dinamičko programiranje (Dynamic Programming, DP) metoda je rješavanja složenih problema razlaganjem izvornog problema na razmjerno jednostavne potprobleme.

Budući da dinamičko programiranje nije neki konkretan algoritam, nego način rješavanja određene vrste problema, pojavljuje se u najrazličitijim strukturama podataka, a i vrste zadataka vezanih uz njega vrlo su raznolike.

-   [Uvod u dinamičko programiranje](../dp/index.md)

#### 2.8.1 Problem ruksaka

Zadan je ruksak ograničenog kapaciteta; treba odabrati i u njega staviti neke predmete koji imaju obujam i vrijednost tako da ukupna vrijednost bude najveća. To je prva prepreka koja zaustavi mnoge natjecatelje; od ovog mjesta algoritme postaje malo teže razumjeti.

-   [DP za ruksak](../dp/knapsack/basic.md)

#### 2.8.2 Linearno dinamičko programiranje

U dinamičkom programiranju jedan od najtežih dijelova je oblikovanje stanja, za što trebaju konstruktivne tehnike. Kad ste zapisali stanja i jednadžbu prijelaza među stanjima, dovršiti zadatak iz dinamičkog programiranja više nije teško.

-   [Konstrukcija](../basic/construction.md)
-   [Osnove dinamičkog programiranja](../dp/basic.md)

Memoizirano pretraživanje način je implementacije pretraživanja koji pamti podatke o već obiđenim stanjima i tako izbjegava ponovni obilazak istog stanja. U nekim zadacima memoizirano pretraživanje može smanjiti težinu razmišljanja.

Budući da memoizirano pretraživanje osigurava da se svako stanje posjeti samo jednom, ono je i čest način implementacije dinamičkog programiranja.

-   [Memoizirano pretraživanje](../dp/memo.md)

#### 2.8.3 Složenije dinamičko programiranje

Intervalno dinamičko programiranje proširenje je linearnog dinamičkog programiranja; pri podjeli problema na faze uvelike ovisi o redoslijedu pojavljivanja elemenata u fazi i o tome iz kojih je elemenata prethodne faze nastalo spajanjem.

-   [Intervalni DP](../dp/interval.md)

### 2.9 Matematika

#### 2.9.1 Aritmetika velikih brojeva

Što ako ni `long long` (ili int64) nije dovoljan? Upotrijebite aritmetiku velikih brojeva. U biti je to simulacija četiriju osnovnih računskih operacija.

-   [Računanje s velikim brojevima](../math/bignum.md)

#### 2.9.2 Pretvorba brojevnih sustava

U računalima se osim binarnog često koriste i oktalni i heksadekadski sustav. Ponekad i pravilan odabir brojevnog sustava uvelike pomaže u rješavanju zadatka.

-   [Brojevni sustavi](../math/numeral-sys/base.md)

#### 2.9.3 Operacije nad bitovima

Operacije nad bitovima su operacije koje se izvode na binarnom zapisu cijelih brojeva. Budući da računalo podatke iznutra pohranjuje binarno, operacije nad bitovima vrlo su brze.

Osnovnih operacija nad bitovima ima 6: AND, OR, XOR, NOT po bitovima te pomak ulijevo i udesno.

-   [Operacije nad bitovima](../math/bit.md)

#### 2.9.4 Teorija brojeva

-   [Osnove teorije brojeva](../math/number-theory/basic.md)
-   [Prosti brojevi](../math/number-theory/prime.md)
-   [Sita](../math/number-theory/sieve.md)
-   [Najveći zajednički djelitelj](../math/number-theory/gcd.md)
-   [Eulerova funkcija](../math/number-theory/euler-totient.md)
-   [Rastav na proste faktore](../math/number-theory/pollard-rho.md)

#### 2.9.5 Kombinatorno prebrojavanje

-   [Permutacije i kombinacije](../math/combinatorics/combination.md)
-   [Dirichletov princip](../math/combinatorics/drawer-principle.md)
-   [Formula uključivanja i isključivanja](../math/combinatorics/inclusion-exclusion-principle.md)

***

Ovime ste naučili sve algoritme iz opsega početne skupine, ali da biste ih svladali, morate i dalje rješavati dovoljan broj zadataka kako biste učvrstili naučeno gradivo.
