---
title: Garsia–Wachs algoritam
---

## Uvod

**Garsia–Wachs algoritam** (Garsia–Wachs Algorithm) učinkovit je algoritam kojim računalo u **linearnom vremenu** gradi **optimalno binarno stablo pretraživanja** i **alfabetski Huffmanov kod**. Nazvan je po Adrianu Garsiji i Michelle L. Wachs, koji su 1977. objavili odgovarajući rad.

## Opis problema

Zadan je cijeli broj $n$. Za $n+1$ nenegativnih težina $w_{0},w_{1},\dots ,w_{n}$ treba konstruirati korijensko binarno stablo u kojem svaki od $n$ unutarnjih čvorova ima dva djeteta, što znači da to binarno stablo ima $n+1$ listova. Ulazni niz duljine $n+1$ bijektivno preslikavamo na čvorove binarnog stabla u njihovu redoslijedu, a cilj je među svim mogućim strukturama stabla s $n$ unutarnjih čvorova naći stablo za koje je težinska suma vanjskih duljina puta od korijena do svakog lista najmanja.

### Optimalno binarno stablo pretraživanja

Ovaj se problem može shvatiti kao problem konstruiranja binarnog stabla pretraživanja nad $n$ uređenih ključeva, uz pretpostavku da će se stablo koristiti samo za traženje vrijednosti koje u njemu ne postoje. U tom slučaju $n$ ključeva dijeli prostor traženih vrijednosti na $n+1$ intervala, a težina jednog od tih intervala može se uzeti kao vjerojatnost da tražena vrijednost padne u taj interval. Težinska suma vanjskih duljina puta određuje očekivano vrijeme pretraživanja.

### Alfabetski Huffmanov kod

Ovaj se problem može upotrijebiti i za konstruiranje Huffmanova koda. To je metoda jednoznačnog kodiranja $n+1$ zadanih vrijednosti pomoću binarnih nizova promjenjive duljine. U toj interpretaciji kod vrijednosti zadan je nizom lijevih i desnih koraka od roditelja do djeteta na putu od korijena do lista u stablu (npr. lijevo je $0$, desno $1$). Za razliku od standardnog Huffmanova koda, Huffmanov kod konstruiran na ovaj način alfabetski je uređen, tj. poredak tih binarnih kodova jednak je ulaznom poretku vrijednosti. Ako je težina vrijednosti njezina frekvencija u kodiranoj poruci, izlaz Garsia–Wachs algoritma alfabetski je uređen Huffmanov kod koji sažima poruku na najmanju duljinu.

## Postupak

Garsia–Wachs algoritam općenito se sastoji od tri faze:

1.  Konstruiramo binarno stablo čije su vrijednosti u listovima, pri čemu redoslijed može biti pogrešan.
2.  Izračunamo udaljenost od korijena do svakog lista u stablu.
3.  Konstruiramo drugo binarno stablo s jednakim udaljenostima listova, ali ispravnim redoslijedom.

![](./images/garsia-wachs.png)

Kao što prikazuje gornja slika, u prvoj fazi algoritma gradi se binarno stablo (lijevo) traženjem i spajanjem neuređenih trojki ulaznog niza, a izlaz algoritma jest ispravno uređeno binarno stablo u kojem su visine listova jednake kao u drugom stablu.

Prva faza algoritma lakše se opisuje ako se na početak i kraj ulaznog niza dodaju dvije granične vrijednosti $\infty$ (ili bilo koja dovoljno velika konačna vrijednost). Zato se pri korištenju Garsia–Wachs algoritma u natjecateljskim rješenjima za niz $\mathit{num}$ duljine $n$ obično definira $\mathit{num}[0] = \mathit{num}[n+1] = \infty$.

Prva faza održava šumu koja se na početku sastoji od jednočvornih stabala stvorenih za svaku ulaznu težinu koja nije stražar (non-sentinel). Svakom je stablu pridružena vrijednost, zbroj težina njegovih listova; za svaku ulaznu težinu koja nije stražar nastaje jedan čvor stabla. Da bi se održavao niz tih vrijednosti, na svakom su kraju dvije granične vrijednosti. Početni niz čine samo težine listova u ulaznom redoslijedu. Zatim se sljedeći koraci ponavljaju, pri čemu svaki korak smanjuje duljinu ulaznog niza, dok ne ostane samo jedno stablo koje sadrži sve listove:

-   U nizu nađemo prve tri uzastopne vrijednosti $x$, $y$, $z$ takve da je $x \leq z$. Budući da je granična vrijednost na kraju niza veća od bilo kojih dviju konačnih vrijednosti ispred nje, takva trojka uvijek postoji.
-   Uklonimo $x$ i $y$ iz niza i stvorimo novi čvor stabla kao roditelja čvorova $x$ i $y$, s vrijednošću $x+y$.
-   Novi čvor ponovno umetnemo desno od vrijednosti koja je ispred izvornog položaja $x$-a najbliža $x$-u, a veća je ili jednaka $x+y$. Zbog lijeve granične vrijednosti takav položaj uvijek postoji.

Da bi se ta faza učinkovito implementirala, algoritam može trenutni niz vrijednosti održavati u bilo kojoj strukturi balansiranog binarnog stabla pretraživanja. Takva nam struktura omogućuje da u logaritamskom vremenu uklonimo $x$ i $y$ te ponovno umetnemo njihova novog roditelja. U svakom koraku težine na parnim indeksima niza do vrijednosti $y$ tvore jedan padajući niz, a težine na neparnim indeksima tvore drugi padajući niz. Stoga se položaj za ponovno umetanje $x+y$ može naći u logaritamskom vremenu dvama binarnim pretraživanjima po tim dvama padajućim nizovima pomoću balansiranog stabla. Linearnim sekvencijalnim pretraživanjem koje počinje od vrijednosti $z$ prethodne trojke možemo traženje prvog položaja koji zadovoljava $x \leq z$ obaviti u ukupno linearnoj vremenskoj složenosti.

Dokaz treće faze Garsia–Wachs algoritma, tj. da postoji drugo stablo s jednakim udaljenostima i da to stablo daje optimalno rješenje problema, vrlo je važan. No budući da postoji više načina dokazivanja i da su previše složeni, ovdje ga izostavljamo. Uz pretpostavku da je treća faza ispravna, druga i treća faza lako se implementiraju u linearnom vremenu. Stoga je na ulaznom nizu duljine $n$ ukupna vremenska složenost Garsia–Wachs algoritma $O(n\log n)$.

## Primjene

Paket [garsia-wachs](https://hackage.haskell.org/package/garsia-wachs) funkcijskog programskog jezika Haskell daje funkcijsku implementaciju Garsia–Wachs algoritma. Služi uglavnom za izgradnju optimalnih tablica pretraživanja ili za balansiranje strukture podataka [rope](https://hackage.haskell.org/package/rope) s optimalnom složenošću.

???+ note "Napomena"
    **rope** je alat u jeziku Haskell za rad s [finger treeovima](../ds/finger-tree.md) nad nizovima bajtova (bytestring) s neobaveznim anotacijama.

## Primjeri zadataka

???+ note "[POJ 1738 An old Stone Game](http://poj.org/problem?id=1738)"
    Postoji stara igra s kamenjem. Na početku igre igrač poreda $n$ ($1 \leq n \leq 50000$) hrpa kamenja u red. Cilj je spojiti kamenje u jednu hrpu po sljedećim pravilima: u svakom koraku igre igrač može spojiti dvije susjedne hrpe u jednu novu hrpu. Bodovi su ukupan broj kamenova u novoj hrpi. Izračunajte najmanji mogući ukupan broj bodova.

??? note "Ideja rješenja"
    Zadatak o spajanju hrpa kamenja klasičan je; obično ga rješavamo intervalnim DP-om, ali kad je količina podataka velika, npr. $n$ ($1 \leq n \leq 50000$) kao u ovom zadatku, učinkovitije je rješavati ga Garsia–Wachs algoritmom. Prvi korak: inicijaliziramo niz $\mathit{num}[n]$ veličine $n$, pri čemu je $\mathit{num}[0] = \mathit{num}[n+1] = \infty$. Drugi korak: svaki put nađemo najmanji $i$ takav da je $\mathit{num}[i-1] \leq \mathit{num}[i+1]$ i spojimo $\mathit{num}[i-1], \mathit{num}[i]$ u $\mathit{temp}$; zatim ispred nađemo najveći $j$ takav da je $\mathit{num}[j] > \mathit{temp}$ i premjestimo $\mathit{temp}$ iza $j$. Taj korak ponavljamo dok ne ostane $1$ hrpa.
    Što se tiče zahtjeva da se smiju spajati samo susjedne hrpe kamenja: budući da je $\mathit{num}[j]\geq \mathit{num}[i-1] + \mathit{num}[i]$, elemente od $\mathit{num}[j+1]$ do $\mathit{num}[i-2]$ možemo promatrati kao jednu cjelinu $\mathit{num}[mid]$, pa se sigurno najprije spaja $\mathit{sum}$. Zahtjev zadatka stoga nije narušen.

???+ note "[ATCODER N-Slimes](https://atcoder.jp/contests/dp/tasks/dp_n)"
    $N$ slimeova stoji u redu. Na početku je veličina $i$-tog slimea slijeva $a_{i}$. Taro pokušava spojiti sve slimeove u jedan veći slime. Uzastopno ponavlja sljedeću operaciju dok ne ostane samo jedan slime:
    odabere dva susjedna slimea i spoji ih u novi slime. Veličina novog slimea je $x+y$, gdje su $x$ i $y$ veličine slimeova prije spajanja. Taj korak ima cijenu $x+y$. Pri spajanju slimeova njihov se međusobni položaj ne mijenja. Odredite najmanju moguću ukupnu cijenu.

## Literatura i dodatno čitanje

1.  [Garsia–Wachs algorithm - Wikipedia](https://en.wikipedia.org/wiki/Garsia%E2%80%93Wachs_algorithm)
2.  [Data.Algorithm.GarsiaWachs - Hackage Haskell](https://hackage.haskell.org/package/garsia-wachs-1.2/docs/Data-Algorithm-GarsiaWachs.html)
3.  [garsia-wachs: A Functional Implementation of the Garsia-Wachs Algorithm](https://hackage.haskell.org/package/garsia-wachs)
4.  [Sentinel value - Wikipedia](https://en.wikipedia.org/wiki/Sentinel_value)
5.  [A new proof of the Garsia-Wachs algorithm](https://www.sciencedirect.com/science/article/abs/pii/0196677488900090)
