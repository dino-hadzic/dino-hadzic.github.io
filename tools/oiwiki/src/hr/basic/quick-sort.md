---
title: Quick sort
---

Ova stranica kratko predstavlja quick sort (brzo sortiranje).

## Definicija

**Quick sort** (quicksort, brzo sortiranje), poznat i kao partition-exchange sort, široko je korišten algoritam sortiranja.

## Osnovna ideja i implementacija

### Postupak

Quick sort sortira niz metodom [podijeli pa vladaj](./divide-and-conquer.md).

Quick sort se sastoji od tri koraka:

1.  podijeli niz na dva dijela (uz očuvanje relativnog odnosa veličina);
2.  rekurzivno primijeni quick sort na oba podniza;
3.  spajanje nije potrebno, jer je niz tada već potpuno sortiran.

Za razliku od merge sorta, prvi korak ne dijeli niz jednostavno na prednju i stražnju polovicu, nego pri dijeljenju treba očuvati odnos veličina. Konkretno, niz se dijeli na dva dijela tako da nijedan broj u prvom podnizu nije veći od brojeva u drugom. Radi prosječne vremenske složenosti obično se nasumično bira broj $m$ kao granica između dvaju podnizova.

Zatim održavamo dva pokazivača, prednji $p$ i stražnji $q$, i redom provjeravamo je li trenutni broj na strani na kojoj treba biti (prednjoj ili stražnjoj). Ako nije – npr. ako stražnji pokazivač $q$ naiđe na broj manji od $m$ – zamijenimo brojeve na položajima $p$ i $q$ i pomaknemo $p$ za jedno mjesto naprijed. Kad su trenutni brojevi na ispravnim mjestima, pomičemo pokazivače i nastavljamo dok se ne sretnu.

Zapravo quick sort ne propisuje kako točno izvesti prvi korak; i za izbor $m$ i za particioniranje postoji više načina.

U trećem koraku podnizovi su već sortirani i brojevi u prvom nisu veći od brojeva u drugom, pa ih samo nadovežemo.

Slijede osnovne implementacije s fiksnim izborom pivota: nerekurzivna C++ implementacija uzima posljednji element trenutnog podniza, a rekurzivna C++ i Python implementacija prvi element. Pivot se ne bira nasumično, pa se na sortiranom ulazu i sličnim slučajevima mogu degradirati u $O(n^2)$.

=== "C++"
    === " Nerekurzivna implementacija[^ref2]"
        ```cpp
        --8<-- "docs/basic/code/quick-sort/quick-sort_1.cpp:sort"
        ```
    
    === "Rekurzivna implementacija"
        ```cpp
        --8<-- "docs/basic/code/quick-sort/quick-sort_2.cpp:sort"
        ```

=== "Python[^ref2]"
    ```python
    --8<-- "docs/basic/code/quick-sort/quick-sort_2.py:sort"
    ```

## Svojstva

### Stabilnost

Quick sort je nestabilan algoritam sortiranja.

### Vremenska složenost

Najbolja i prosječna vremenska složenost quick sorta je $O(n\log n)$, a najgora $O(n^2)$.

U najboljem slučaju svaki je odabrani pivot medijan niza; tada složenost zadovoljava rekurziju $T(n) = 2T(\dfrac{n}{2}) + \Theta(n)$ i po glavnom teoremu $T(n) = \Theta(n\log n)$.

U najgorem slučaju svaki je odabrani pivot minimum ili maksimum niza; tada složenost zadovoljava rekurziju $T(n) = T(n - 1) + \Theta(n)$, a zbrajanjem dobivamo $T(n) = \Theta(n^2)$.

Analiza očekivanja u nastavku pretpostavlja da su ključevi međusobno različiti i da se pivot svaki put bira jednoliko nasumično iz trenutnog podniza.

??? note "Dokaz"
    Dokažimo da je u tom slučaju vremenska složenost algoritma $O(n\log n)$.
    
    **Lema 1.** Pri quick sortu niza od $n$ elemenata, ako je $X$ broj različitih parova elemenata koji su uspoređeni tijekom particioniranja, vremenska složenost quick sorta je $O(n + X)$.
    
    U svakom particioniranju jedan se element bira za pivot, pa se particioniranje događa najviše $n$ puta. Budući da se pri particioniranju svaki par elemenata usporedi samo konstantan broj puta, a količina usporedbi i ostalih osnovnih operacija je istog reda veličine, ukupna je složenost $O(n + X)$.
    
    Neka je $a_i$ $i$-ti najmanji broj u izvornom nizu, $A_{i,j} = \{ a_i, a_{i+1}, \dots, a_j \}$, a $X_{i,j}$ diskretna slučajna varijabla s vrijednostima $0$ ili $1$ koja označava jesu li $a_i$ i $a_j$ uspoređeni tijekom sortiranja.
    
    Očito su svi odabrani pivoti različiti, a elementi se uspoređuju samo s pivotom, pa je broj različitih uspoređenih parova
    
    $$
    \begin{aligned} X = \sum \limits _ {i = 1} ^ {n - 1} \sum \limits _ {j = i + 1} ^ n X_{i,j} \end{aligned}
    $$
    
    Po linearnosti očekivanja,
    
    $$
    \begin{aligned} E[X] & = E \left[ \sum \limits _ {i = 1} ^ {n - 1} \sum \limits _ {j = i + 1} ^ n X_{i,j} \right] \\ & = \sum \limits _ {i = 1} ^ {n - 1} \sum \limits _ {j = i + 1} ^ n E[X_{i,j}] \\ & = \sum \limits _ {i = 1} ^ {n - 1} \sum \limits _ {j = i + 1} ^ n P(a_i\ \text{i}\ a_j\ \text{su uspoređeni}) \end{aligned}
    $$
    
    **Lema 2.** $a_i$ i $a_j$ uspoređeni su ako i samo ako je $a_i$ ili $a_j$ prvi element skupa $A_{i,j}$ odabran za pivot.
    
    Prvo nužnost: ako ni $a_i$ ni $a_j$ nije prvi pivot odabran iz $A_{i,j}$, onda $a_i$ i $a_j$ nisu uspoređeni.
    
    Ako ni $a_i$ ni $a_j$ nije prvi odabrani pivot iz $A_{i,j}$, postoji $x$ s $i < x < j$ takav da je $a_x$ prvi odabrani pivot iz $A_{i,j}$. U particioniranju s pivotom $a_x$ elementi $a_i$ i $a_j$ dospijevaju u različite podnizove, pa se kasnije sigurno ne uspoređuju. Budući da se elementi uspoređuju samo s pivotom, $a_i$ i $a_j$ nisu uspoređeni ni prije ni tijekom tog particioniranja. Dakle $a_i$ i $a_j$ nisu uspoređeni.
    
    Zatim dovoljnost: ako je $a_i$ ili $a_j$ prvi pivot odabran iz $A_{i,j}$, onda su $a_i$ i $a_j$ uspoređeni.
    
    Bez smanjenja općenitosti neka je $a_i$ prvi pivot odabran iz $A_{i,j}$. Budući da nijedan drugi element iz $A_{i,j}$ nije bio odabran za pivot, svi elementi $A_{i,j}$ nalaze se u istom podnizu. U particioniranju s pivotom $a_i$, $a_i$ se uspoređuje sa svim elementima trenutnog podniza, pa i s $a_j$.
    
    Izračunajmo $P(a_i\ \text{i}\ a_j\ \text{su uspoređeni})$. Dok nijedan element iz $A_{i,j}$ nije odabran za pivot, svi su elementi $A_{i,j}$ u istom podnizu. Zato svaki element $A_{i,j}$ ima jednaku vjerojatnost da bude prvi odabran za pivot. Budući da $A_{i,j}$ ima $j - i + 1$ elemenata, po lemi 2
    
    $$
    P(a_i \text{ i } a_j \text{ su uspoređeni}) = P(a_i \text{ ili } a_j \text{ je prvi pivot odabran iz skupa } A_{i,j}) = \dfrac{2}{j-i+1}
    $$
    
    Stoga
    
    $$
    \begin{aligned} E[X] & = \sum \limits _ {i = 1} ^ {n - 1} \sum \limits _ {j = i + 1} ^ n P(a_i\ \text{i}\ a_j\ \text{su uspoređeni}) \\ & = \sum \limits _ {i = 1} ^ {n - 1} \sum \limits _ {j = i + 1} ^ n \dfrac{2}{j - i + 1} \\ & = \sum \limits _ {i = 1} ^ {n - 1} \sum \limits _ {k = 2} ^ {n - i + 1} \dfrac{2}{k} \\ & = \sum \limits _ {i = 1} ^ {n - 1} O(\log n) \\ & = O(n \log n) \end{aligned}
    $$
    
    Dakle, očekivana vremenska složenost quick sorta je $O(n \log n)$.

Nasumičan izbor pivota smanjuje vjerojatnost najgore podjele. Osim toga, pristup memoriji u quick sortu slijedi načelo lokalnosti, što mu u praksi pomaže da postigne dobre performanse.[^ref1]

## Optimizacije

### Jednostavne ideje optimizacije

Ako quick sort implementiramo samo prema gore opisanoj osnovnoj ideji (ili prepišemo predložak), u pravilu nećemo proći zadatak-predložak [P1177 【模板】快速排序](https://www.luogu.com.cn/problem/P1177), jer se mogu konstruirati podaci na kojima naivni quick sort degradira u $O(n^2)$.

Zato naivni quick sort treba optimirati. Tri su uobičajene ideje[^ref3]:

-   Pivot (element za usporedbu) birati metodom **medijana od tri (median-of-three): medijan prvog, posljednjeg i srednjeg elementa**. Tako se izbjegava degradacija na ekstremnim podacima (npr. uzlazno ili silazno sortiran niz).
-   Kad je podniz kratak, učinkovitiji je **insertion sort**.
-   Nakon svakog prolaza **elemente jednake pivotu skupiti oko pivota**; tako se izbjegava degradacija na ekstremnim podacima (npr. kad je većina elemenata jednaka).

Slijedi nekoliko zrelih načina optimizacije quick sorta.

### Trosmjerni quick sort

#### Definicija

**Trosmjerni quick sort** (3-way quicksort) dijeli elemente na tri dijela prema odnosu s pivotom. Ideja se temelji na rješenju [problema nizozemske zastave](https://en.wikipedia.org/wiki/Dutch_national_flag_problem).

#### Postupak

Za razliku od izvornog quick sorta, trosmjerni quick sort nakon nasumičnog izbora pivota $m$ dijeli niz na tri dijela: manje od $m$, jednako $m$ i veće od $m$. Time se postiže upravo skupljanje elemenata jednakih pivotu oko pivota.

#### Svojstva

Na nizovima s mnogo ponovljenih vrijednosti trosmjerni quick sort znatno je učinkovitiji od izvornog. Njegova najbolja vremenska složenost je $O(n)$.

#### Implementacija

Trosmjerni quick sort vrlo je jednostavno implementirati; slijedi referentna implementacija.

=== "C++"
    ```cpp
    --8<-- "docs/basic/code/quick-sort/quick-sort_3.cpp:sort"
    ```

=== "Python[^ref2]"
    ```python
    --8<-- "docs/basic/code/quick-sort/quick-sort_3.py:sort"
    ```

### Introsort

#### Definicija

**Introsort** (introspective sort)[^ref4] kombinacija je quick sorta i [heap sorta](./heap-sort.md), koju je 1997. osmislio David Musser. Introsort je zapravo optimizacija quick sorta koja jamči najgoru vremensku složenost $O(n\log n)$.

#### Svojstva

Introsort ograničava dubinu particioniranja quick sorta, obično na $2\lfloor \log_2n \rfloor$[^ref5]; kad se granica prekorači, prelazi na heap sort. Tako zadržava lokalnost pristupa memoriji quick sorta, a sprječava degradaciju na $O(n^2)$ u nekim slučajevima.

#### Implementacija

Od lipnja 2000. funkcija `sort()` u `stl_algo.h` SGI-jevog C++ STL-a implementirana je introsortom.

## Linearno pronalaženje k-tog najmanjeg elementa

U primjerima koda u nastavku, element s uzlaznim indeksom $k$ definiran je kao element na $k$-tom mjestu (indeksi od 0) kad se niz poreda uzlazno.

Najjednostavniji način da se pronađe $k$-ti najmanji element (k-th order statistic) jest sortirati niz i uzeti element na mjestu $k$. Složenost je $O(n\log n)$, što je za ovaj problem rasipno.

Problem možemo riješiti idejom quick sorta. Nakon „particioniranja” u quick sortu niz $A_{p} \cdots A_{r}$ podijeljen je na $A_{p} \cdots A_{q}$ i $A_{q+1} \cdots A_{r}$; prema odnosu broja elemenata lijevog dijela ($q - p + 1$) i $k$ odlučujemo hoćemo li rekurzivno nastaviti samo u lijevom ili samo u desnom dijelu.

Kao i kod quick sorta, složenost ovisi o pivotu izabranom u svakom particioniranju. Ako se pivot bira nasumično, može se dokazati da je očekivana vremenska složenost $O(n)$.

???+ note "Referentna implementacija"
    ```cpp
    --8<-- "docs/basic/code/quick-sort/quick-sort_4.cpp:sort"
    ```

### Medijan medijana

**Medijan medijana** (median of medians) deterministički je način izbora pivota u particioniranju, koji algoritmu za „pronalaženje $k$-tog najmanjeg elementa” jamči linearnu vremensku složenost i u najgorem slučaju.

Algoritam teče ovako:

1.  niz podijeli na $\lceil n/5\rceil$ grupa od najviše pet elemenata; posljednja grupa može imati manje od pet;
2.  svaku grupu sortiraj i uzmi medijan; za parnu duljinu uvijek uzmi manji medijan;
3.  rekurzivno odaberi medijan tih medijana kao pivot, napravi trosmjernu podjelu na manje, jednake i veće od pivota i rekurzivno nastavi samo u dijelu (strogo manjem ili strogo većem) u kojem je traženi element.

#### Dokaz vremenske složenosti

Neka je broj grupa $g=\lceil n/5\rceil$. Sa svake strane pivota (uključujući jednakost) nalazi se barem $\lfloor g/2\rfloor$ medijana grupa; isključimo li posljednju grupu, svaka potpuna grupa daje barem tri elementa koja nisu veća odnosno nisu manja od pivota. Stoga je sa svake strane barem $3n/10-O(1)$ takvih elemenata, pa dijelovi strogo manjih i strogo većih elemenata imaju veličinu najviše $7n/10+O(1)$. U dio jednakih elemenata ne rekurziramo. Grupiranje, računanje medijana grupa i particioniranje zajedno stoje $O(n)$. Ukupno dobivamo nejednakost

$$
T(n)\le T(\lceil n/5\rceil)+T(7n/10+O(1))+O(n).
$$

Odaberimo konstante $a,b$ tako da je zbroj veličina dvaju rekurzivnih poziva s desne strane najviše $9n/10+a$, a nerekurzivni trošak najviše $bn$. Za $n\ge20a$ taj je zbroj najviše $19n/20$. Uz induktivnu pretpostavku $T(m)\le cm$ dovoljno je uzeti $c\ge20b$ i povećati $c$ da pokrije konačno mnogo baznih slučajeva, pa vrijedi $T(n)\le19cn/20+bn\le cn$. Dakle, najgora vremenska složenost je $O(n)$.

## Literatura i bilješke

[^ref1]: [C++ 性能榨汁机之局部性原理 - I'm Root lee !](http://irootlee.com/juicer_locality/)

[^ref2]: [Algorithm Implementation/Sorting/Quicksort – Wikibooks (kineski)](https://zh.wikibooks.org/wiki/%E7%AE%97%E6%B3%95%E5%AE%9E%E7%8E%B0/%E6%8E%92%E5%BA%8F/%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F)

[^ref3]: [Tri inačice quick sorta i njegove optimizacije (kineski)](https://blog.csdn.net/insistGoGo/article/details/7785038)

[^ref4]: [introsort](https://en.wikipedia.org/wiki/Introsort)

[^ref5]: Npr. [libstdc++ 14.2.0: `__introsort_loop` i `__sort`](https://github.com/gcc-mirror/gcc/blob/releases/gcc-14.2.0/libstdc%2B%2B-v3/include/bits/stl_algo.h#L1876-L1908). Zapravo je dovoljno ograničiti dubinu na $O(\log n)$ i pri dosezanju granice prijeći na heap sort da bi ukupna složenost bila $O(n\log n)$.
