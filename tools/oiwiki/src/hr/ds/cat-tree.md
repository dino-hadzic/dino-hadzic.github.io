---
title: Cat tree
---

## Uvod

Dobro je poznato da segment tree podržava brze upite o „zbroju” informacija nekog intervala, npr. najveći zbroj podintervala, zbroj intervala, umnožak niza matrica u intervalu itd.

Problem je, međutim, da je upit nad intervalom običnog segment treea u očima nekih zlobnih autora zadataka ipak pomalo spor.

Jednostavno rečeno, izgradnja segment treea zahtijeva $O(n)$ spajanja, a svaki upit nad intervalom $O(\log{n})$ spajanja. Kad se pita zbroj intervala, to je još podnošljivo, ali kad treba pitati umnožak matrica u intervalu, gdje jedno spajanje (tj. jedno množenje matrica) ima složenost $O(k^3)$, i $O(\log{n})$ spajanja katkad je vremenski neprihvatljivo.

Takozvani „cat tree” (mačje stablo) statični je segment tree koji ne podržava izmjene, već samo brze upite nad intervalom. Vrijedan je tek kad je broj upita velik ($m=\Omega(n)$).

Izgradnja takvog statičnog segment treea zahtijeva $O(n\log{n})$ spajanja, ali se složenost upita ubrzava na $O(1)$ spajanja.

Pri obradi informacija sa skupim spajanjem, poput množenja matrica, cat tree smanjuje složenost jednog upita s $O(k^3 \log n)$ na $O(k^3)$.

Napomena: za statične upite o linearnoj bazi (linear basis) intervala, iako cat tree može poboljšati složenost implementacije običnim segment treeom, postoji pristup bolji i vremenski i prostorno: [prefiksna linearna baza](../math/linear-algebra/basis.md#拓展前缀线性基). Osim toga, obični segment tree može rješavati dinamičke upite o linearnoj bazi intervala, dok je za statične upite cat tree ne samo složeniji za implementaciju i neoptimalan, nego nema ni funkcionalnih prednosti.

## Načelo

Pri upitu za „zbroj” informacija intervala $[l,r]$ pronađemo u segment treeu LCA čvora koji predstavlja $[l,l]$ i čvora koji predstavlja $[r,r]$. Neka taj čvor $p$ predstavlja interval $[L,R]$; uočavamo nekoliko vrlo zanimljivih svojstava:

1.  Interval $[L,R]$ sigurno sadrži $[l,r]$. Očito, jer je predak i od $l$ i od $r$.

2.  Interval $[l,r]$ sigurno prelazi preko sredine intervala $[L,R]$. Budući da je $p$ LCA od $l$ i $r$, lijevo dijete od $p$ predak je od $l$, ali ne i od $r$, a desno dijete od $p$ predak je od $r$, ali ne i od $l$. Stoga je $l$ sigurno u intervalu $[L,\mathit{mid}]$, a $r$ sigurno u intervalu $(\mathit{mid},R]$.

S ta dva svojstva složenost upita možemo smanjiti na $O(1)$.

## Implementacija

Konkretno, pri izgradnji stabla za čvor segment treea neka je njegov interval $(l,r]$.

Za razliku od klasičnog segment treea, koji u čvoru čuva samo zbroj od $[l,r]$, u čvoru dodatno pohranjujemo niz sufiksnih zbrojeva od $(l,\mathit{mid}]$ i niz prefiksnih zbrojeva od $(\mathit{mid},r]$.

Tada je složenost izgradnje $T(n)=2T(n/2)+O(n)=O(n\log{n})$, a jednako tako prostorna složenost raste s izvornih $O(n)$ na $O(n\log{n})$.

Slijedi najvažnije: upit.

Ako je interval upita $[l,r]$, pronađemo LCA čvora koji predstavlja $[l,l]$ i čvora koji predstavlja $[r,r]$ i označimo ga $p$.

Prema dvama upravo opisanim svojstvima, $l,r$ leže unutar intervala od $p$ i sigurno prelaze preko sredine od $p$.

To znači vrlo važnu činjenicu: pomoću niza prefiksnih i sufiksnih zbrojeva u $p$ možemo $[l,r]$ rastaviti na $[l,\mathit{mid}]+(\mathit{mid},r]$ i tako sastaviti interval $[l,r]$.

A taj postupak zahtijeva samo $O(1)$ spajanja!

Ali čini se da smo nešto zanemarili?

Složenost traženja LCA, čini se, nije $O(1)$: brute force daje $O(\log{n})$, binary lifting $O(\log{\log{n}})$, a prelazak na sparse table preskup je…

## Izgradnja u obliku hrpe

Konkretno, niz nadopunimo do potencije broja $2$ i zatim izgradimo segment tree.

Tada uočavamo da je oznaka LCA dvaju čvorova segment treea upravo najdulji zajednički prefiks (LCP) binarnih zapisa oznaka tih čvorova.

Kratkim razmišljanjem vidimo da u binarnom zapisu za $x$ i $y$ vrijedi `lcp(x,y)=x>>digits[x^y]`. (Pri tome `digits[x]` označava broj binarnih znamenki od $x$, tj. $\lfloor \log_2 x \rfloor+1$.)

Dakle, dovoljno je unaprijed izračunati niz `digits` i traženje LCA postaje trivijalno.

Tako smo izgradili cat tree.

Budući da izgradnja uključuje računanje prefiksnih i sufiksnih zbrojeva, za informacije sa složenošću spajanja $O(k^3)$ poput množenja matrica složenost je izgradnje $O(n\log n \cdot k^3)$. Na toj osnovi cat tree smanjuje složenost jednog statičnog upita za umnožak matrica u intervalu s $O(k^3 \log n)$ na $O(k^3)$, pa kad je broj upita velik ($m=\Omega(n)$), ukupnu složenost obrade $m$ upita poboljšava s $O(n \cdot k^3 + m \cdot k^3 \log n)$ na $O(n\log n \cdot k^3 + m \cdot k^3)$.

### Literatura

-   [Blog immortalCO (kineski)](https://immortalco.blog.uoj.ac/blog/2102)
-   [\[Kle77\]](http://ieeexplore.ieee.org/document/1675628/) V. Klee, "Can the Measure of be Computed in Less than O (n log n) Steps?," Am. Math. Mon., vol. 84, no. 4, pp. 284–285, Apr. 1977.
-   [\[BeW80\]](https://www.tandfonline.com/doi/full/10.1080/00029890.1977.11994336) Bentley and Wood, "An Optimal Worst Case Algorithm for Reporting Intersections of Rectangles," IEEE Trans. Comput., vol. C–29, no. 7, pp. 571–577, Jul. 1980.
