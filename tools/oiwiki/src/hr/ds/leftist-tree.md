---
title: Leftist tree
---

## Što je leftist tree?

**Leftist tree** (lijevo nagnuto stablo) je, kao i [**pairing heap**](./pairing-heap.md), **spojivi heap** (mergeable heap): ima svojstvo heapa i može se brzo spajati.

## Definicija i svojstva leftist treea

Za binarno stablo definiramo **vanjski čvor** kao čvor s manje od dvoje djece, a $\mathrm{dist}$ čvora kao broj bridova na putu do najbližeg vanjskog čvora u njegovu podstablu. Prazan čvor ima $\mathrm{dist}$ jednak $0$.

???+ note "Napomena"
    U nekim je izvorima $\mathrm{dist}$ definiran kao ovdašnji $\mathrm{dist}$ umanjen za $1$; tako se definira zato što se pri pisanju koda mogu izostaviti neke provjere praznine, ali tada $\mathrm{dist}$ praznog čvora treba unaprijed postaviti na $-1$. Sav kôd u ovom članku koristi **definiciju u kojoj je $\mathrm{dist}$ praznog čvora $-1$**; obratite pozornost na razliku u odnosu na definiciju $\mathrm{dist}$ u tekstu.

Leftist tree je binarno stablo koje ne samo da ima svojstvo heapa nego je i „lijevo nagnuto”: za svaki čvor $\mathrm{dist}$ lijevog djeteta veći je ili jednak $\mathrm{dist}$ desnog djeteta.

Stoga je $\mathrm{dist}$ svakog čvora leftist treea jednak $\mathrm{dist}$ njegova desnog djeteta uvećanom za jedan.

Treba imati na umu da $\mathrm{dist}$ nije dubina: **dubina leftist treea nije ograničena**, a i lanac koji ide ulijevo zadovoljava definiciju leftist treea.

## Ključna operacija: spajanje (merge)

Pri spajanju dvaju heapova, zbog svojstva heapa, najprije korijen s manjom vrijednošću (radi jednostavnosti u ovom članku promatramo min-heap) uzmemo za korijen spojenog heapa, zatim lijevo dijete tog korijena postaje lijevo dijete spojenog heapa, a njegovo desno dijete rekurzivno spojimo s drugim heapom i rezultat postaje desno dijete spojenog heapa. Da bi vrijedilo svojstvo lijeve nagnutosti, ako je nakon spajanja $\mathrm{dist}$ lijevog djeteta manji od $\mathrm{dist}$ desnog, zamijenimo djecu.

Referentni kôd:

???+ note "Implementacija"
    ```cpp
    int merge(int x, int y) {
      if (!x || !y) return x | y;  // ako je jedan heap prazan, vrati drugi
      if (t[x].val > t[y].val) swap(x, y);  // manja vrijednost postaje korijen
      t[x].rs = merge(t[x].rs, y);          // rekurzivno spoji desno dijete s drugim heapom
      if (t[t[x].rs].d > t[t[x].ls].d)
        swap(t[x].ls, t[x].rs);   // ako lijeva nagnutost ne vrijedi, zamijeni djecu
      t[x].d = t[t[x].rs].d + 1;  // ažuriraj dist
      return x;
    }
    ```

Zbog lijeve nagnutosti, sa svakom razinom rekurzije $\mathrm{dist}$ korijena jednog od heapova smanji se za $1$, a u binarnom stablu s $n$ čvorova $\mathrm{dist}$ korijena nije veći od $\left\lceil\log (n+1)\right\rceil$, pa je složenost spajanja heapova veličina $n$ i $m$ jednaka $O(\log n+\log m)$.

???+ note "Dokaz svojstva $\mathrm{dist}$"
    Binarno stablo čiji korijen ima $\mathrm{dist}$ jednak $x$ ima barem $x-1$ razina koje čine puno binarno stablo, pa ima barem $2^x-1$ čvorova. Uočite da to svojstvo vrijedi za sva binarna stabla, a ne samo za leftist tree.

Leftist tree može se napisati i bez zamjene lijevog i desnog djeteta: dijete s većim $\mathrm{dist}$ smatramo lijevim, a dijete s manjim $\mathrm{dist}$ desnim:

???+ note "Implementacija"
    ```cpp
    int& rs(int x) { return t[x].ch[t[t[x].ch[1]].d < t[t[x].ch[0]].d]; }
    
    int merge(int x, int y) {
      if (!x || !y) return x | y;
      if (t[x].val < t[y].val) swap(x, y);
      int& rs_ref = rs(x);
      rs_ref = merge(rs_ref, y);
      t[x].d = t[rs(x)].d + 1;
      return x;
    }
    ```

## Ostale operacije na leftist treeu

### Umetanje čvora

Jedan čvor također se može smatrati heapom, pa ga samo spojimo.

### Brisanje korijena

Dovoljno je spojiti lijevo i desno dijete korijena.

### Brisanje proizvoljnog čvora

#### Postupak

Najprije spojimo lijevo i desno dijete, a zatim odozdo prema gore ažuriramo $\mathrm{dist}$ i, kad lijeva nagnutost ne vrijedi, zamjenjujemo djecu; rekurzija završava kad $\mathrm{dist}$ više ne treba ažurirati:

???+ note "Implementacija"
    ```cpp
    int& rs(int x) { return t[x].ch[t[t[x].ch[1]].d < t[t[x].ch[0]].d]; }
    
    // uz pushup, brisanje čvora uz očuvanje lijeve nagnutosti svodi se na merge lijevog i desnog djeteta
    int merge(int x, int y) {
      if (!x || !y) return x | y;
      if (t[x].val < t[y].val) swap(x, y);
      int& rs_ref = rs(x);
      rs_ref = merge(rs_ref, y);
      t[rs_ref].fa = x;
      t[x].d = t[rs(x)].d + 1;
      return x;
    }
    
    void pushup(int x) {
      if (!x) return;
      if (t[x].d != t[rs(x)].d + 1) {
        t[x].d = t[rs(x)].d + 1;
        pushup(t[x].fa);
      }
    }
    
    void erase(int x) {
      int y = merge(t[x].ch[0], t[x].ch[1]);
      t[y].fa = t[x].fa;
      if (t[t[x].fa].ch[0] == x)
        t[t[x].fa].ch[0] = y;
      else if (t[t[x].fa].ch[1] == x)
        t[t[x].fa].ch[1] = y;
      pushup(t[y].fa);
    }
    ```

#### Dokaz složenosti

Razmotrimo najprije postupak `merge`: svaki korak spušta $x$ ili $y$ za jednu razinu, pa je najgori slučaj da stalno biramo desni čvor leftist treea (čvor s najmanjim $\mathrm{dist}$) i spuštamo se za jednu razinu, pri čemu se $\mathrm{dist}$ smanji za $1$.

Razmotrimo zatim postupak `pushup`. Neka je $x$ čvor nad kojim trenutačno radimo `pushup`, $y$ njegov roditelj, a „početni $\mathrm{dist}$” čvora neka je njegov $\mathrm{dist}$ prije `pushupa`. Rekurzija kreće od roditelja obrisanog čvora i postoje dva slučaja:

1.  $x$ je desno dijete od $y$; tada je početni $\mathrm{dist}$ od $y$ jednak početnom $\mathrm{dist}$ od $x$ uvećanom za jedan.
2.  $x$ je lijevo dijete od $y$; budući da se $\mathrm{dist}$ čvora smanjuje najviše za jedan, rekurzija se nastavlja samo ako su početni $\mathrm{dist}$ lijevog i desnog djeteta od $y$ jednaki (tada smanjenje $\mathrm{dist}$ lijevog djeteta za jedan uzrokuje zamjenu djece), pa je početni $\mathrm{dist}$ od $y$ i dalje početni $\mathrm{dist}$ od $x$ uvećan za jedan.

Dakle, sa svakom razinom rekurzije početni $\mathrm{dist}$ od $x$ raste za jedan, pa ima najviše $O(\log n)$ razina rekurzije.

### Dodavanje/oduzimanje vrijednosti cijelom heapu, množenje pozitivnim brojem

Zapravo je moguća svaka operacija koja se može označiti (lazy tag) i ne mijenja relativni poredak.

Oznaku stavimo na korijen, a pri brisanju korijena ili spajanju heapova (pristupu djeci) oznaku spustimo:

???+ note "Implementacija"
    ```cpp
    int merge(int x, int y) {
      if (!x || !y) return x | y;
      if (t[x].val > t[y].val) swap(x, y);
      pushdown(x);
      t[x].rs = merge(t[x].rs, y);
      if (t[t[x].rs].d > t[t[x].ls].d) swap(t[x].ls, t[x].rs);
      t[x].d = t[t[x].rs].d + 1;
      return x;
    }
    
    int pop(int x) {
      pushdown(x);
      return merge(t[x].ls, t[x].rs);
    }
    ```

## Ostali spojivi heapovi

### Nasumični heap

???+ note "Implementacija"
    ```cpp
    int merge(int x, int y) {
      if (!x || !y) return x | y;
      if (t[y].val < t[x].val) swap(x, y);
      if (rand() & 1)  // nasumično odluči hoće li se lijevo i desno dijete zamijeniti
        swap(t[x].ls, t[x].rs);
      t[x].ls = merge(t[x].ls, y);
      return x;
    }
    ```

Vidimo da je jedina razlika ove implementacije to što spajanje koristi nasumične brojeve, čime se izbjegava računanje $\mathrm{dist}$. Prosječna vremenska složenost također je $O(\log n)$; detaljan dokaz nalazi se u [Randomized Heap](https://cp-algorithms.com/data_structures/randomized_heap.html).

### Skew heap

Skew heap (kosi heap) samoprilagođavajuća je inačica leftist treea. Pri spajanju dvaju heapova bezuvjetno zamjenjuje djecu svih čvorova na putu spajanja, pokušavajući tako održati ravnotežu. Prema amortiziranoj analizi, kod skew heapa odozgo prema dolje (top-down skew heap) umetanje, spajanje i brisanje minimuma imaju složenost $O(\log n)$[^ref1].

## Primjeri zadataka

### Zadaci-predlošci

[Luogu P3377 „Predložak” Leftist tree (spojivi heap)](https://www.luogu.com.cn/problem/P3377)

[Monkey King](https://www.luogu.com.cn/problem/P1456)

[Rimska igra](https://www.luogu.com.cn/problem/P2713)

Treba paziti na sljedeće:

1.  Prije spajanja provjerite jesu li elementi već u istom heapu.

2.  Dubina leftist treea može doseći $O(n)$, pa vrh heapa u kojem se čvor nalazi treba održavati union-find strukturom, a ne skakati izravno po roditeljima. (Iako su u mnogim zadacima testni podaci slabi, pa izravno skakanje po roditeljima prolazi...) (Pri održavanju korijena union-findom stari korijen mora pokazivati na novi, a novi na sebe.)

??? note "Referentni kôd za Rimsku igru"
    ```cpp
    --8<-- "docs/ds/code/leftist-tree/leftist-tree_1.cpp"
    ```

### Problemi na stablima

[„APIO2012” Raspoređivanje (Dispatching)](https://www.luogu.com.cn/problem/P1552)

[„JLOI2015” Osvajanje utvrda](https://loj.ac/problem/2107)

U takvim zadacima obično svaki čvor održava heap, spaja ga s djecom te prema uvjetima zadatka izbacuje elemente, mijenja ih i računa odgovor; nalik je zadacima sa spajanjem segment treeova.

??? note "Referentni kôd za Osvajanje utvrda"
    ```cpp
    --8<-- "docs/ds/code/leftist-tree/leftist-tree_2.cpp"
    ```

### [„SCOI2011” Nezgodne operacije](https://loj.ac/problem/2441)

Prvo, vrh heapa u kojem se čvor nalazi treba tražiti union-findom, a ne skakanjem prema gore.

Zatim razmotrimo upit za pojedini čvor: ako oznake stavljamo na uobičajen način, treba izračunati zbroj oznaka na putu od čvora do korijena, što u najgorem slučaju košta $O(n)$. Kad bi oznaka bila samo na vrhu heapa, upit bi bio brz, ali kako to postići?

Možemo postupiti slično kao kod heuristic merging (spajanje manjeg u veći): pri svakom spajanju oznaku manjeg heapa izravno spustimo na svaki njegov čvor, a oznaka većeg heapa postaje oznaka spojenog heapa. Budući da spojeni heap nosi oznaku drugog heapa, manji heap pri spuštanju mora spustiti svoju oznaku umanjenu za oznaku drugog heapa. Svakim spajanjem veličina heapa u kojem je čvor barem se udvostruči, pa se oznaka na svaki čvor spušta najviše $O(\log n)$ puta, a ukupna složenost izravnog spuštanja oznaka je $O(n\log n)$.

Zatim dodavanje vrijednosti pojedinom čvoru: dovoljno je čvor izbrisati, ažurirati i ponovno umetnuti.

Napokon, globalni maksimum: vrhove svih heapova možemo održavati balansiranim stablom / heapom koji podržava brisanje proizvoljnog čvora (npr. leftist treeom) / multisetom.

Dakle, operacije su redom:

1.  Izravno spusti oznake heapa s manje čvorova, spoji heapove, ažuriraj size i tag, iz multiseta izbriši onaj stari vrh koji nakon spajanja više nije vrh.
2.  Izbriši čvor, ažuriraj vrijednost, ponovno ga umetni, ažuriraj multiset. Treba razlikovati je li obrisani čvor korijen.
3.  Označi vrh heapa, ažuriraj multiset.
4.  Postavi globalnu oznaku.
5.  Upit: vrijednost + oznaka vrha heapa + globalna oznaka.
6.  Upit: vrijednost korijena + oznaka vrha heapa + globalna oznaka.
7.  Upit: maksimum multiseta + globalna oznaka.

??? note "Referentni kôd za Nezgodne operacije"
    ```cpp
    --8<-- "docs/ds/code/leftist-tree/leftist-tree_3.cpp"
    ```

### [„BOI2004” Sequence – Niz brojeva](https://www.luogu.com.cn/problem/P4331)

Ovo je zadatak iz stručnog rada; vidi [„Huang Yuanhe – Svojstva leftist treea i njegove primjene”](https://github.com/OI-wiki/libs/blob/master/%E9%9B%86%E8%AE%AD%E9%98%9F%E5%8E%86%E5%B9%B4%E8%AE%BA%E6%96%87/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2005%E8%AE%BA%E6%96%87%E9%9B%86/%E9%BB%84%E6%BA%90%E6%B2%B3--%E5%B7%A6%E5%81%8F%E6%A0%91%E7%9A%84%E7%89%B9%E7%82%B9%E5%8F%8A%E5%85%B6%E5%BA%94%E7%94%A8/%E9%BB%84%E6%BA%90%E6%B2%B3.pdf).

## Literatura

[^ref1]: [Self-Adjusting Heaps](https://epubs.siam.org/doi/10.1137/0215004)
