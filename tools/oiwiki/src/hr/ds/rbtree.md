---
title: Crveno-crno stablo
---

author: 0x03A6, abc1763613206, auuuu4, CCXXXI, Conless, Enter-tainer, fanenr, happyZYM, hsfzLZH1, iamtwz, LeverImmy, leverimmy, Lhcfl, Marcythm, RIvance, Tiphereth-A, trudbot, Xeniume, Xeonacid, YBYCS, yuhuoji

Crveno-crno stablo samobalansirajuće je binarno stablo pretraživanja. Svaki čvor dodatno pohranjuje polje color („RED” ili „BLACK”), koje služi održavanju ravnoteže stabla pri umetanju i brisanju.

Crveno-crno stablo inačica je B-stabla reda 4 ([2-3-4 stabla](https://en.wikipedia.org/wiki/2%E2%80%933%E2%80%934_tree)).[^gilbas1978]

## Svojstva

Ispravno crveno-crno stablo mora zadovoljavati sljedeća četiri svojstva:

1.  Čvor je crven ili crn.
2.  NIL čvorovi (prazni listovi) crni su.
3.  Djeca crvenog čvora crna su.
4.  Svaki put od korijena do NIL čvora sadrži jednak broj crnih čvorova.

Donja slika prikazuje ispravno crveno-crno stablo:

![rbtree-example](images/rbtree-example.svg)

???+ note "Napomena"
    Neki izvori dodaju i peto svojstvo: korijen mora biti crn. To svojstvo zahtijeva da nakon umetanja obojimo korijen u crno ako je crven. No to možemo odgoditi do brisanja, pa svojstvo nije nužno (implementacija u ovom članku ipak ga zadovoljava). Radi preciznosti navodimo i [izvorni tekst Wikipedije](https://en.wikipedia.org/wiki/Red%E2%80%93black_tree#Properties):
    
    > Neki autori, primjerice Cormen i sur.,[^cite_note-cormen2009-18] navode „korijen je crn” kao peti zahtjev, ali ne i Mehlhorn i Sanders[^cite_note-mehlhorn2008-17] ni Sedgewick i Wayne.[^cite_note-algs4-16] Budući da se korijen uvijek može promijeniti iz crvenog u crni, to pravilo malo utječe na analizu. Ovaj ga članak također izostavlja jer donekle ometa rekurzivne algoritme i dokaze.

## Definicija klase crveno-crnog stabla

```cpp
--8<-- "docs/ds/code/rbtree/rbtree.hpp:class-node1"
  // ...
--8<-- "docs/ds/code/rbtree/rbtree.hpp:class-node2"
```

???+ note "Napomena"
    Pohranjivanje pokazivača na djecu čvora crveno-crnog stabla u niz omogućuje veću ponovnu uporabu koda.

## Operacije

???+ note "Napomena"
    Postoji više načina implementacije umetanja/brisanja u crveno-crnom stablu. Ovaj članak prati implementaciju iz knjige *Introduction to Algorithms*: održavanje ravnoteže nakon umetanja dijeli se na 3 slučaja, a nakon brisanja na 4.

Obilazak, pronalaženje minimuma/maksimuma, pretraživanje elemenata, određivanje ranga elementa, pronalaženje elementa prema rangu i pronalaženje prethodnika/sljedbenika isti su kao u [binarnom stablu pretraživanja](./bst.md), pa ih ovdje nećemo ponavljati.

U komentarima koda za održavanje ravnoteže nakon umetanja/brisanja upotrebljavamo sljedeće oznake:

-   `p` označava da je čvor `p` crn;
-   `[p]` označava da je čvor `p` crven;
-   `{p}` označava da je čvor `p` crven ili crn;
-   `|p|` označava da je čvor `p` NIL čvor ili crn.

### Rotacije

Rotacije su ključ održavanja ravnoteže u većini balansiranih stabala. Mijenjaju dubinu lokalnih čvorova, a ne mijenjaju rezultat inorder obilaska ispravnog BST-a.

![rbtree-rotations](images/rbtree-rotate.svg)

???+ note "Implementacija"
    ```cpp
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:rotate"
    ```

### Umetanje

Umetanje u crveno-crno stablo slično je umetanju u obični BST. Novi čvor u crveno-crnom stablu u početku je crven. Nakon umetanja potrebne su korekcije ovisno o stanju umetnutog i povezanih čvorova kako bi vrijedila prethodno navedena četiri svojstva.

???+ note "Implementacija"
    ```cpp
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:insert"
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:insert-leaf"
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:insert-fixup1"
        // ...
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:insert-fixup2"
    ```

### Održavanje ravnoteže nakon umetanja

???+ note "Napomena"
    Za bolje razumijevanje sami provjerite vrijedi li svojstvo 4 nakon održavanja ravnoteže.

Budući da je umetnuti čvor, ako nije korijen, nužno crven, umetanje može narušiti svojstvo 3 pa treba održavati ravnotežu.

Neka je umetnuti čvor $n$, njegov roditelj $p$, djed $g$, a stric $u$. Iz svojstva 3 slijedi da $g$ mora biti crn.

Ravnotežu rekurzivno održavamo od mjesta umetanja prema gore. Ako je $p$ crn, možemo stati; inače razlikujemo 3 slučaja.

```cpp
--8<-- "docs/ds/code/rbtree/rbtree.hpp:insert-aux1"
      // ...
--8<-- "docs/ds/code/rbtree/rbtree.hpp:insert-aux2"
```

#### Umetanje, slučaj 1

I $p$ i $u$ crveni su. Dovoljno je samo promijeniti boje.

![](images/rbtree-insert-case1.svg)

???+ note "Implementacija"
    ```cpp
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:insert-case1"
    ```

#### Umetanje, slučaj 2

$p$ je crven, $u$ je crn, a smjerovi čvorova $p$ i $n$ razlikuju se.

Rotacijom oko čvora $p$ prelazimo na treći slučaj.

![](images/rbtree-insert-case2.svg)

???+ note "Implementacija"
    ```cpp
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:insert-case2"
    ```

#### Umetanje, slučaj 3

$p$ je crven, $u$ je crn, a smjerovi čvorova $p$ i $n$ jednaki su.

Rotiramo oko čvora $g$ tako da $p$ postane korijen podstabla, a zatim zamijenimo boje čvorova $p$ i $g$.

![](images/rbtree-insert-case3.svg)

???+ note "Implementacija"
    ```cpp
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:insert-case3"
    ```

### Brisanje

Brisanje u crveno-crnom stablu ima nešto više koraka nego u običnom BST-u. Konkretno:

-   Ako čvor $n$ koji brišemo ima dvoje djece, zamijenimo podatke čvora $n$ i najmanjeg čvora $s$ u desnom podstablu, pa postavimo $n$ na $s$. Tada $n$ više ne može imati dvoje djece.
-   Ako čvor $n$ koji brišemo ima jedno dijete $s$, iz svojstva 4 slijedi da $s$ mora biti crven, a iz svojstva 3 da $n$ mora biti crn. Dovoljno je pokazivač na $n$ u roditelju $p$ zamijeniti adresom čvora $s$, roditeljski pokazivač čvora $s$ postaviti na adresu čvora $p$, a zatim $s$ obojiti u crno.
-   Ako čvor $n$ koji brišemo nema djece, a $n$ je korijen ili je $n$ crven, možemo ga izravno izbrisati. Inače bi izravno brisanje narušilo svojstvo 4 pa treba održavati ravnotežu.

???+ note "Implementacija"
    ```cpp
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:delete"
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:delete-leaf"
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:delete-fixup1"
        // ...
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:delete-fixup2"
    ```

### Održavanje ravnoteže nakon brisanja

???+ note "Napomena"
    Za bolje razumijevanje sami provjerite vrijedi li svojstvo 4 nakon održavanja ravnoteže.

Iz prethodne rasprave znamo da je $n$ crni list koji nije korijen. Neka čvor $n$ ima roditelja $p$, brata $s$ i nećake $c$ i $d$.

I nakon brisanja ravnotežu rekurzivno održavamo od $n$ prema gore. Ako je $n$ korijen ili je $n$ crven, možemo stati; inače razlikujemo 4 slučaja.

```cpp
--8<-- "docs/ds/code/rbtree/rbtree.hpp:delete-aux1"
      // Brisanje, slučaj 1
      // ...
      // Ostali slučajevi
--8<-- "docs/ds/code/rbtree/rbtree.hpp:delete-aux2"
      // ...
--8<-- "docs/ds/code/rbtree/rbtree.hpp:delete-aux3"
```

#### Brisanje, slučaj 1

$s$ je crven.

Rotiramo oko $p$ tako da $s$ postane korijen podstabla, a zatim zamijenimo boje čvorova $s$ i $p$, čime prelazimo na jedan od preostala tri slučaja.

![](images/rbtree-remove-case1.svg)

???+ note "Implementacija"
    ```cpp
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:delete-case1"
    ```

#### Brisanje, slučaj 2

Boja čvora $p$ nije određena, a $s$, $c$ i $d$ crni su.

Dovoljno je obojiti $s$ u crveno.

![](images/rbtree-remove-case2.svg)

Ako je $p$ crven, time narušavamo svojstvo 3. No ako je $p$ crven, odmah se izlazi iz petlje, pa ga na kraju obojimo u crno.

???+ note "Implementacija"
    ```cpp
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:delete-case2"
    ```

#### Brisanje, slučaj 3

Boja čvora $p$ nije određena, $s$ i $d$ crni su, a $c$ je crven.

Rotiramo oko $s$ tako da $c$ postane korijen podstabla kojemu je korijen prije bio $s$, a zatim zamijenimo boje čvorova $s$ i $c$, čime prelazimo na četvrti slučaj.

![](images/rbtree-remove-case3.svg)

???+ note "Implementacija"
    ```cpp
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:delete-case3"
    ```

#### Brisanje, slučaj 4

Boje čvorova $p$ i $c$ nisu određene, $s$ je crn, a $d$ je crven.

Rotiramo oko $p$ tako da $s$ postane korijen podstabla, zamijenimo boje čvorova $s$ i $p$, a $d$ obojimo u crno. Time možemo završiti održavanje ravnoteže.

![](images/rbtree-remove-case4.svg)

???+ note "Implementacija"
    ```cpp
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:delete-case4"
    ```

## Referentni kod

Sljedeći kod implementira set pomoću crveno-crnog stabla:

??? note "Implementacija"
    ```cpp
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:full"
    ```

??? note "Primjeri zadataka: [Luogu P3369 [Predložak] Obično balansirano stablo](https://www.luogu.com.cn/problem/P3369) i [Luogu P6136 [Predložak] Obično balansirano stablo (jači testni podaci)](https://www.luogu.com.cn/problem/P6136)"
    ```cpp
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:class"
    --8<-- "docs/ds/code/rbtree/rbtree_1.cpp:main"
    ```

## Veza s 2-3-4 stablima

2-3-4 stablo B-stablo je reda 4. Kao i opće B-stablo, podržava pretraživanje, umetanje i brisanje u vremenu $O(\log n)$. Postoje tri vrste čvorova: 2-čvorovi, 3-čvorovi i 4-čvorovi, koji redom sadrže jedan, dva ili tri podatkovna elementa. Svi su listovi na istoj dubini (najnižoj razini), a svi su podaci pohranjeni uređeno.

2-3-4 stabla i crveno-crna stabla izomorfna su: svakom crveno-crnom stablu odgovara jedinstveno 2-3-4 stablo. Proširivanje, razdvajanje i spajanje čvorova pri umetanju i brisanju u 2-3-4 stablu odgovara promjeni boja i rotacijama u crveno-crnom stablu. Donja slika prikazuje crveno-crne čvorove koji odgovaraju 2-čvorovima, 3-čvorovima i 4-čvorovima. Primijetite da 3-čvor 2-3-4 stabla odgovara dvama slučajevima crveno-crnog stabla: crveni čvor može biti lijevo ili desno nagnut, pa jednom crveno-crnom stablu može odgovarati više 2-3-4 stabala.

![2-3-4-tree-rbt-1](images/2-3-4-tree-rbt-1.svg)

Donja slika prikazuje crveno-crno stablo i pripadajuće 2-3-4 stablo. Pomicanjem crvenih čvorova uz lijevu i desnu stranu njihova roditelja oblikujemo čvor B-stabla i dobivamo odgovarajuće 2-3-4 stablo. Možemo primijetiti da je broj čvorova crveno-crnog stabla jednak broju čvorova 2-3-4 stabla.

![2-3-4-tree-rbt](images/2-3-4-tree-rbt-2.svg)

Umetanje i brisanje u crveno-crnom stablu možemo razumjeti usporedbom s 2-3-4 stablom.[^234-vs-rbt]

## Primjena u stvarnim projektima

Crveno-crna stabla imaju najbolju ukupnu učinkovitost među danas uobičajenim memorijskim balansiranim stablima u industriji, pa se široko upotrebljavaju u stvarnim projektima. Navodimo nekoliko primjera s poveznicama na izvorni kod radi usporedbe i učenja.

### Linux

Izvorni kod:

-   [`linux/lib/rbtree.c`](https://elixir.bootlin.com/linux/latest/source/lib/rbtree.c)

Sve operacije crveno-crnog stabla u Linuxu implementirane su iterativno, petljama. Uz učinkovitost, brojni komentari osiguravaju čitljivost, pa taj kod svakako preporučujemo za proučavanje. Crveno-crna stabla vrlo su raširena u jezgri Linuxa; ovdje navodimo samo nekoliko klasičnih primjera.

-   [CFS raspoređivanje zadataka koji nisu u stvarnom vremenu](https://www.kernel.org/doc/html/latest/scheduler/sched-design-CFS.html)

    Od stabilnih inačica jezgre nakon 2.6.24 Linux upotrebljava novi raspoređivač CFS. Svi izvršivi procesi koji nisu u stvarnom vremenu održavaju se u crveno-crnom stablu s virtualnim vremenom izvođenja kao ključem, radi pravednijeg i učinkovitijeg raspoređivanja zadataka. CFS napušta nizove active/expired i dinamičko računanje prioriteta te više ne prati vrijeme spavanja zadataka niti razlikuje interaktivne zadatke. Umjesto toga sljedeći zadatak bira pomoću crveno-crnog stabla s vremenski izračunatim ključevima, a prioritet raspoređivanja određuje prema CPU vremenu koje su zauzeli svi zadaci.

-   [epoll](https://man7.org/linux/man-pages/man7/epoll.7.html)

    epoll, skraćeno od event poll, implementacija je IO multipleksiranja (IO multiplexing) u jezgri Linuxa i poboljšanje ranijih poll/select mehanizama. Linuxova implementacija epolla pohranjuje deskriptore datoteka u crveno-crno stablo.

### Nginx

Izvorni kod:

-   [`nginx/src/core/ngx_rbtree.h`](https://github.com/nginx/nginx/blob/master/src/core/ngx_rbtree.h)
-   [`nginx/src/core/ngx_rbtree.c`](https://github.com/nginx/nginx/blob/master/src/core/ngx_rbtree.c)

Vremenski okidači u korisničkom prostoru nginxa implementirani su pomoću crveno-crnog stabla. U nginxu se svi timer čvorovi održavaju u jednom crveno-crnom stablu. Svaka iteracija worker procesa poziva funkciju `ngx_process_events_and_timers`, koja zatim poziva `ngx_event_expire_timers` za obradu vremenskih okidača. Ta funkcija uzastopno uzima čvor s najmanjom vremenskom vrijednošću iz stabla, provjerava je li istekao i izvršava njegovu funkciju, sve dok ne dođe do čvora čije vrijeme još nije isteklo.

Postoji mnogo javno dostupnih analiza izvornog koda crveno-crnog stabla u nginxu; čitatelji ih mogu sami potražiti i proučiti.

### C++

Izvorni kod:

-   GNU libstdc++

    -   [`libstdc++-v3/include/bits/stl_tree.h`](https://github.com/gcc-mirror/gcc/blob/master/libstdc%2B%2B-v3/include/bits/stl_tree.h)
    -   [`libstdc++-v3/src/c++98/tree.cc`](https://github.com/gcc-mirror/gcc/blob/master/libstdc%2B%2B-v3/src/c%2B%2B98/tree.cc)

    Osim toga, `libstdc++` u zaglavlju `<ext/rb_tree>` nudi [`__gnu_cxx::rb_tree`](https://github.com/gcc-mirror/gcc/blob/master/libstdc%2B%2B-v3/include/ext/rb_tree), koji nasljeđuje `std::_Rb_tree` i može se smatrati aliasom tipa namijenjenim vanjskoj uporabi. To zaglavlje **nije** dio C++ standarda, pa ga ne preporučujemo osim ako je nužno.

    Crveno-crno stablo dostupno je i u [`pb_ds`](../lang/pb-ds/tree.md) biblioteke `libstdc++`.

-   LLVM libcxx
    -   [`libcxx/include/__tree`](https://github.com/llvm/llvm-project/blob/main/libcxx/include/__tree)

-   Microsoft STL
    -   [`stl/inc/xtree`](https://github.com/microsoft/STL/blob/main/stl/inc/xtree)

U većini implementacija STL-a unutarnja struktura podataka za `std::set` i `std::map` jest crveno-crno stablo (primjerice u prethodno navedenim implementacijama). Međutim, C++ standard ne zahtijeva da `std::set` i `std::map` budu implementirani pomoću crveno-crnog stabla, pa se u projektima ne treba izravno oslanjati na njihove unutarnje strukture podataka.

### OpenJDK

Izvorni kod:

-   [`java.util.TreeMap<K, V>`](https://github.com/openjdk/jdk/blob/master/src/java.base/share/classes/java/util/TreeMap.java)
-   [`java.util.TreeSet<K, V>`](https://github.com/openjdk/jdk/blob/master/src/java.base/share/classes/java/util/TreeSet.java)
-   [`java.util.HashMap<K, V>`](https://github.com/openjdk/jdk/blob/master/src/java.base/share/classes/java/util/HashMap.java)

JDK-ovi `TreeMap` i `TreeSet` upotrebljavaju crveno-crno stablo kao temeljnu strukturu podataka. Od JDK-a 1.8 nadalje i u unutarnjoj hash tablici `HashMap`-a povezani popis pojedinog unosa automatski se pretvara u crveno-crno stablo kada njegova duljina premaši 8, radi učinkovitijeg pretraživanja.

## Literatura

-   Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022).*Introduction to algorithms*. MIT press.
-   [Red-Black Tree - Wikipedia](https://en.wikipedia.org/wiki/Red%E2%80%93black_tree)
-   [Red-Black Tree Visualization](https://www.cs.usfca.edu/~galles/visualization/RedBlack.html)

[^gilbas1978]: L. J. Guibas and R. Sedgewick, "A dichromatic framework for balanced trees,"*19th Annual Symposium on Foundations of Computer Science (sfcs 1978)*, Ann Arbor, MI, USA, 1978, pp. 8-21, doi:[10.1109/SFCS.1978.3](https://doi.org/10.1109%2FSFCS.1978.3).

[^cite_note-cormen2009-18]: <https://en.wikipedia.org/wiki/Red–black_tree#cite_note-Cormen2009-18>

[^cite_note-mehlhorn2008-17]: <https://en.wikipedia.org/wiki/Red–black_tree#cite_note-Mehlhorn2008-17>

[^cite_note-algs4-16]: <https://en.wikipedia.org/wiki/Red–black_tree#cite_note-Algs4-16>: 432–447

[^234-vs-rbt]: [Ovaj članak na blogu](https://www.cnblogs.com/zhenbianshu/p/8185345.html) daje detaljan opis.
