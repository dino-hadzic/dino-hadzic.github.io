---
title: Finger tree
---

???+ warning "Napomena"
    Ovo je poglavlje izborno štivo; prije čitanja provjerite jeste li donekle upoznati s funkcijskim programiranjem (functional programming).

## Uvod

**Finger tree** (prstno stablo) **čisto funkcijska** je struktura podataka koju su predložili Ralf Hinze i Ross Paterson.

## Zašto nam je potreban finger tree

U funkcijskom programiranju lista je vrlo čest tip podataka. Gotovo svi funkcijski jezici podržavaju operacije nad nizovima kao što su dodavanje i brisanje elemenata na oba kraja (operacije reda s dva kraja, deque), umetanje, spajanje i brisanje na proizvoljnom mjestu, pronalaženje elementa koji zadovoljava uvjet te razdvajanje niza na podnizove. Međutim, učinkovito izvođenje većeg broja operacija tim je jezicima teško postići; čak i kad postoje odgovarajuće implementacije, obično su vrlo složene i u praksi teško upotrebljive.

Finger tree nudi čisto funkcijsku strukturu podataka za nizove koja pristup te dodavanje na početak i kraj niza obavlja u amortiziranom konstantnom vremenu (amortized constant time), a spajanje i slučajni pristup u logaritamskom vremenu (logarithmic time). Osim dobrih asimptotskih granica vremena izvođenja, finger tree je i vrlo fleksibilan: u kombinaciji s monoidnim oznakama ([monoidal tag](https://en.wikipedia.org/wiki/Monoidal_category)) na elementima, finger tree može se iskoristiti za učinkovitu implementaciju nizova sa slučajnim pristupom, uređenih nizova, intervalnih stabala i prioritetnih redova.

## Osnovna struktura

Finger tree podatke pohranjuje na „prstima” (listovima) stabla, s amortiziranim konstantnim vremenom pristupa. Prst (finger) je točka iz koje se može pristupiti dijelu strukture podataka. U imperativnim jezicima (imperative language) to bi se zvalo pokazivač. U finger treeu „prst” je struktura koja pokazuje na krajeve niza ili na listove. Finger tree u svakom unutarnjem čvoru pohranjuje i rezultat primjene neke asocijativne operacije na njegove potomke. Podaci pohranjeni u unutarnjim čvorovima mogu pružiti funkcionalnost koja nadilazi stablaste strukture podataka.

1.  Dubina finger treea računa se odozdo prema gore.
2.  Prva razina finger treea, tj. listovi stabla, sadrži samo vrijednosti i ima dubinu $0$. Druga razina ima dubinu $1$, treća dubinu $2$ i tako dalje.
3.  Što je čvor bliže korijenu, to je dublje podstablo izvornog stabla (stabla prije nego što je postalo finger tree) na koje pokazuje. Tako je spuštanje niz stablo zapravo kretanje od listova prema korijenu, što je suprotno uobičajenim stablastim strukturama podataka. Da bismo dobili takvu strukturu, moramo osigurati da izvorno stablo ima jednoliku dubinu. Pri deklaraciji objekta čvora on mora biti parametriziran tipom svoje djece. Čvorovi na kralježnici dubine $1$ i veće pokazuju na stabla, a zahvaljujući toj parametrizaciji mogu se prikazati ugniježđenim čvorovima.

### Pretvaranje stabla u finger tree

???+ note "Napomena"
    **2-3 stablo** stablasta je struktura podataka u kojoj svaki čvor s djecom (unutarnji čvor) ima ili dvoje djece ($2$-čvor) i jedan podatkovni element, ili troje djece ($3$-čvor) i dva podatkovna elementa. 2-3 stablo je B-stablo reda $3$. Vanjski čvorovi stabla (listovi) nemaju djece i sadrže jedan ili dva podatkovna elementa.

Postupak započinjemo s balansiranim 2-3 stablom. Da bi finger tree ispravno radio, svi listovi moraju biti na istoj razini, kao na donjoj slici (slike su preuzete iz rada o finger treeu):

![](./images/finger-tree-1.png)

Prst je „struktura koja omogućuje učinkovit pristup čvorovima stabla u blizini određenog položaja”. Da bismo napravili finger tree, prste stavljamo na lijevi i desni kraj stabla: uzmemo krajnji lijevi i krajnji desni unutarnji čvor i podignemo ih, tako da ostatak stabla visi između njih. To nam daje amortizirano konstantno vrijeme pristupa krajevima niza.

![](./images/finger-tree-2.png)

Ova nova struktura podataka zove se finger tree. Finger tree sastoji se od nekoliko slojeva (plavi okviri dolje) raspoređenih duž kralježnice stabla (smeđa crta):

![](./images/finger-tree-3.png)

```haskell
data FingerTree a = Empty
                  | Single a
                  | Deep (Digit a) (FingerTree (Node a)) (Digit a)

data Digit a = One a | Two a a | Three a a a | Four a a a a
data Node a = Node2 a a | Node3 a a a
```

Znamenke (digits) u primjeru čvorovi su označeni slovima. Svaka je lista podijeljena prefiksom ili sufiksom svakog čvora na kralježnici. U pretvorenom 2-3 stablu čini se da popis znamenki na najvišoj razini može imati duljinu dva ili tri, dok niže razine imaju duljinu samo jedan ili dva. Da bi neke primjene finger treea mogle raditi tako učinkovito, finger tree dopušta od $1$ do $4$ podstabla na svakoj razini. Znamenke finger treea mogu se pretvoriti u listu, npr.:

```haskell
type Digit a = One a | Two a a | Three a a a | Four a a a a
```

Najviša razina ima elemente tipa $a$, sljedeća razina elemente tipa Node $a$, jer su to čvorovi između kralježnice i listova; općenito to znači da $n$-ta razina stabla ima elemente tipa $Node^{n}$ $a$, odnosno 2-3 stabla dubine $n$. To znači da je niz od $n$ elemenata predstavljen stablom dubine `Θ(log n)`. Element na udaljenosti $d$ od bližeg kraja pohranjen je u stablu na dubini `Θ(log d)`.

### Operacije reda s dva kraja

Finger tree također omogućuje učinkovit red s dva kraja (deque). Bez obzira na to je li struktura perzistentna, sve operacije traju `Θ(1)`. Može se promatrati kao proširenje implicitnog dequea[^okasaki1999purely]:

1.  Zamjena parova 2-3 čvorovima daje dovoljno fleksibilnosti za učinkovito spajanje. (Da bi operacije dequea ostale u konstantnom vremenu, Digit treba proširiti do četiri.)
2.  Označavanje unutarnjih čvorova monoidom (monoid) omogućuje učinkovito razdvajanje.

```haskell
data ImplicitDeque a = Empty
                     | Single a
                     | Deep (Digit a) (ImplicitDeque (a, a)) (Digit a)

data Digit a = One a | Two a a | Three a a a
```

## Vremenska složenost

Finger tree pruža amortizirani konstantan pristup „prstima” (listovima) stabla, gdje su podaci pohranjeni, te spajanje i razdvajanje u vremenu logaritamskom u veličini manjeg dijela. U svakom unutarnjem čvoru pohranjuje i rezultat primjene neke asocijativne operacije na njegove potomke. Ti „sažeti” podaci pohranjeni u unutarnjim čvorovima mogu pružiti funkcionalnost drugih struktura podataka osim stabala.

| Operacija                       | Finger tree              | Označeno 2-3 stablo (annotated 2-3 tree) | Lista (list)         | Vektor (vector) |
| ----------------------------- | ---------------------- | ----------------------------- | -------------------- | ---------- |
| `cons`,`snoc`                 | $O(1)$                 | $O(\log n)$                   | $O(1)$/$O(n)$        | $O(n)$     |
| `viewl`,`viewr`               | $O(1)$                 | $O(\log n)$                   | $O(1)$/$O(n)$        | $O(1)$     |
| `measure`/`length`            | $O(1)$                 | $O(1)$                        | $O(n)$               | $O(1)$     |
| `append`                      | $O(\log \min(l1, l2))$ | $O(\log n)$                   | $O(n)$               | $O(m+n)$   |
| `split`                       | $O(\log \min(n, l-n))$ | $O(\log n)$                   | $O(n)$               | $O(1)$     |
| `replicate`                   | $O(\log n)$            | $O(\log n)$                   | $O(n)$               | $O(n)$     |
| `fromList`,`toList`,`reverse` | $O(l)$/$O(l)$/$O(l)$   | $O(l)$                        | $O(1)$/$O(1)$/$O(n)$ | $O(n)$     |
| `index`                       | $O(\log \min(n, l-n))$ | $O(\log n)$                   | $O(n)$               | $O(1)$     |

## Primjene

Finger tree može se iskoristiti za izgradnju drugih stabala. Primjerice, prioritetni red može se ostvariti tako da se unutarnji čvorovi označe najmanjim prioritetom među djecom, a indeksirana lista/niz tako da se čvorovi označe brojem listova među njihovom djecom. Druge primjene uključuju nizove sa slučajnim pristupom (opisane dolje), uređene nizove i intervalna stabla.

Finger tree omogućuje prosječno $O(1)$ za push, reverse i pop, $O(\log n)$ za dodavanje i razdvajanje, a može se prilagoditi indeksiranim ili sortiranim nizovima. Kao i sve funkcijske strukture podataka, u svojoj je biti perzistentan; to znači da se stare inačice stabla uvijek čuvaju.

Što se tiče implementacija, konačni nizovi `Seq` u osnovnoj biblioteci Haskella implementirani su 2-3 finger treeom ([Data.Sequence](https://hackage.haskell.org/package/containers-0.6.5.1/docs/Data-Sequence.html)), a [implementacija](https://ocaml-batteries-team.github.io/batteries-included/hdoc2/BatFingerTree.html) modula `BatFingerTree` u OCamlu također koristi općenitu strukturu finger tree. Finger tree može se implementirati s lijenom evaluacijom ili bez nje, no lijenost omogućuje jednostavniju implementaciju.

## Literatura i dodatno štivo

1.  Ralf Hinze and Ross Paterson, "[Finger trees: a simple general-purpose data structure](http://www.staff.city.ac.uk/~ross/papers/FingerTree.html)", Journal of Functional Programming 16:2 (2006) pp 197-217.
2.  [Finger Tree - Wikipedia](https://en.wikipedia.org/wiki/Finger_tree)

[^okasaki1999purely]: [Purely Functional Data Structures](https://www.cambridge.org/us/academic/subjects/computer-science/programming-languages-and-applied-logic/purely-functional-data-structures), Chris Okasaki (1999)
