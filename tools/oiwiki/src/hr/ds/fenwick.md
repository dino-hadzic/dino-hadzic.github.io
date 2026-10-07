---
title: Fenwickovo stablo
---

## Uvod

Fenwickovo stablo (Fenwick tree, binary indexed tree, BIT) struktura je podataka s malo koda koja podržava **izmjenu u točki** i **upit na intervalu**.

??? note "Što su „izmjena u točki” i „upit na intervalu”?"
    Zamislimo ovakav zadatak:
    
    Zadan je niz $a$; treba izvoditi sljedeće dvije operacije:
    
    -   za zadane $x, y$ uvećaj $a[x]$ za $y$;
    -   za zadane $l, r$ izračunaj zbroj $a[l \ldots r]$.
    
    Prva je operacija „izmjena u točki”, a druga „upit na intervalu”.
    
    Slično postoje i „izmjena na intervalu” i „upit u točki”. Po jedan primjer svake:
    
    -   izmjena na intervalu: za zadane $l, r, x$ svaki broj u $a[l \ldots r]$ uvećaj za $x$;
    -   upit u točki: za zadani $x$ izračunaj vrijednost $a[x]$.
    
    Primijetimo da su intervalni problemi u pravilu strogo teži od problema u točki, jer je operacija u točki isto što i operacija na intervalu duljine $1$.

Informacija i operacija koju obično Fenwickovo stablo održava moraju biti **asocijativne** i **invertibilne** (moraju se moći „oduzimati”), npr. zbrajanje (zbroj), množenje (umnožak), XOR itd.

-   Asocijativnost: $(x \circ y) \circ z = x \circ (y \circ z)$, gdje je $\circ$ binarna operacija.
-   Invertibilnost: operacija ima inverznu operaciju, tj. iz poznatih $x \circ y$ i $x$ može se izračunati $y$.

Treba napomenuti:

-   da bi množenje po modulu bilo invertibilno, svaki broj mora imati inverz (što je sigurno ispunjeno kad je modul prost);
-   informacije poput $\gcd$ i $\max$ nisu invertibilne, pa se ne mogu obrađivati običnim Fenwickovim stablom, ali:
    -   s dva Fenwickova stabla mogu se obrađivati intervalni ekstremi, vidi [Efficient Range Minimum Queries using Binary Indexed Trees](http://history.ioinformatics.org/oi/files/volume9.pdf#page=41);
    -   na ovoj stranici predstavit ćemo i prošireno Fenwickovo stablo složenosti $\Theta(\log^2n)$ koje podržava upite nad neinvertibilnim informacijama.

Zapravo su problemi koje rješava Fenwickovo stablo podskup problema koje rješava segment tree: što može Fenwickovo stablo, sigurno može i segment tree; što može segment tree, Fenwickovo stablo ne mora moći. Ipak, kôd Fenwickova stabla mnogo je kraći od koda segment treea, a i konstanta u vremenu izvođenja manja je, pa ga se i dalje isplati naučiti.

Ponekad, uz pomoć niza razlika i pomoćnih nizova, Fenwickovo stablo rješava i jače probleme **zbrajanja na intervalu uz upit u točki** te **zbrajanja na intervalu uz zbroj intervala**.

## Fenwickovo stablo

### Prvi dojam

Najprije primjer: želimo znati prefiksni zbroj $a[1 \ldots 7]$. Kako?

Jedan je način: $a_1 + a_2 + a_3 + a_4 + a_5 + a_6 + a_7$, dakle zbrajamo $7$ brojeva.

No što ako već znamo tri broja $A$, $B$, $C$, gdje je $A$ zbroj $a[1 \ldots 4]$, $B$ zbroj $a[5 \ldots 6]$, a $C$ zbroj $a[7 \ldots 7]$ (zapravo sam $a[7]$)? Kako biste tada računali? Sigurno biste odgovorili: $A + B + C$, dakle zbrajamo samo $3$ broja.

Upravo zato Fenwickovo stablo brzo računa informacije: prefiks $[1, n]$ uvijek možemo rastaviti na **najviše $\boldsymbol{\log n}$ intervala** čije su informacije **već poznate**.

Tada samo spojimo informacije tih $\log n$ intervala i dobijemo odgovor. U usporedbi s izravnim spajanjem $n$ informacija učinkovitost je znatno veća.

Lako je vidjeti da informacija mora biti asocijativna, inače je ne bismo mogli ovako spajati.

Sljedeća slika prikazuje kako Fenwickovo stablo radi:

![](./images/fenwick.svg)

Najdonjih osam kvadratića predstavlja izvorni niz podataka $a$. Nepravilno raspoređeni kvadratići iznad (isti niz kao i najgornjih osam kvadratića) predstavljaju „nadređeni” niz niza $a$ – niz $c$.

Niz $c$ služi za pohranu zbroja nekog intervala izvornog niza $a$; drugim riječima, informacije tih intervala su poznate, a naš je cilj upitni prefiks rastaviti na te male intervale.

Primjerice, sa slike se vidi:

-   $c_2$ pokriva $a[1 \ldots 2]$;
-   $c_4$ pokriva $a[1 \ldots 4]$;
-   $c_6$ pokriva $a[5 \ldots 6]$;
-   $c_8$ pokriva $a[1 \ldots 8]$;
-   preostali $c[x]$ pokrivaju samo sam $a[x]$ (može se gledati kao mali interval $a[x \ldots x]$ duljine $1$).

Lako je uočiti da $c[x]$ uvijek pokriva ukupnu informaciju nekog intervala čiji je desni kraj $x$. Lijevi kraj zasad ne razmatramo; najprije osjetimo kako Fenwickovo stablo odgovara na upit.

Primjer: izračunajmo zbroj $a[1 \ldots 7]$.

Postupak: krećemo od $c_{7}$ i skačemo unatrag; vidimo da $c_{7}$ pokriva samo element $a_{7}$. Zatim pogledamo $c_{6}$; vidimo da $c_{6}$ pokriva $a[5 \ldots 6]$. Zatim skočimo na $c_{4}$; vidimo da $c_{4}$ pokriva elemente $a[1 \ldots 4]$. Zatim pokušamo skočiti na $c_0$, ali $c_0$ zapravo ne postoji, pa stajemo.

Upravo smo pronašli $c_7, c_6, c_4$; to su upravo tri mala intervala na koja se rastavlja $a[1 \ldots 7]$, a spajanjem dobivamo odgovor $c_7 + c_6 + c_4$.

Primjer: izračunajmo zbroj $a[4 \ldots 7]$.

Opet krećemo od $c_7$, skačemo na $c_6$ pa na $c_4$. Sada vidimo da on pokriva zbroj $a[1 \ldots 4]$, ali mi ne želimo dio $a[1 \ldots 3]$ – što sad? Vrlo jednostavno: samo oduzmemo zbroj $a[1 \ldots 3]$.

Pa zašto onda odmah na početku upit za zbroj $a[4 \ldots 7]$ ne pretvorimo u upit za zbroj $a[1 \ldots 7]$ i upit za zbroj $a[1 \ldots 3]$, a na kraju oduzmemo rezultate?

![](images/fenwick-query.svg)

### Pokriveni interval

Postavlja se pitanje: koliko se interval koji pokriva $c[x](x \ge 1)$ zapravo proteže ulijevo? Drugim riječima, kolika je duljina intervala?

U Fenwickovu stablu duljina intervala koji pokriva $c[x]$ definirana je kao $2^{k}$, gdje:

-   ako najniži binarni bit zovemo $0$-tim bitom, $k$ je upravo redni broj bita na kojem je najniža jedinica (`1`) u binarnom zapisu od $x$;
-   $2^k$ (duljina intervala koji pokriva $c[x]$) upravo je broj koji u binarnom zapisu od $x$ čine najniža `1` i sve nule (`0`) iza nje.

Primjer: koji interval pokriva $c_{88}$?

Budući da je $88_{(10)}=01011000_{(2)}$, binarni broj koji čine najniža `1` i nule iza nje jest `1000`, tj. $8$, pa $c_{88}$ pokriva $8$ elemenata niza $a$.

Dakle, $c_{88}$ predstavlja informaciju intervala $a[81 \ldots 88]$.

Broj koji čine najniža `1` u binarnom zapisu od $x$ i nule iza nje označimo s $\operatorname{lowbit}(x)$; tada je interval koji pokriva $c[x]$ jednak $[x-\operatorname{lowbit}(x)+1, x]$.

???+ warning "Napomena"
    $\operatorname{lowbit}$ nije redni broj $k$ bita na kojem je najniža `1`, nego broj $2^k$ koji čine ta `1` i sve nule iza nje.

Kako izračunati `lowbit`? Iz poznavanja bitovnih operacija dobivamo `lowbit(x) = x & -x`.

??? note "Zašto lowbit radi"
    Ako sve bitove binarnog zapisa od `x` invertiramo i dodamo 1, dobivamo binarni zapis od `-x`. Primjerice, binarni zapis broja $6$ je `110`; nakon invertiranja svih bitova dobivamo `001`, a dodavanjem `1` dobivamo `010`.
    
    Neka je binarni zapis od `x` oblika `(...)10...00`; nakon invertiranja svih bitova dobivamo `[...]01...11`, a nakon dodavanja `1` dobivamo `[...]10...00`, što je upravo binarni zapis od `-x`. Ovdje je prva `1` u binarnom zapisu od `x` ujedno najniža `1` od `x`.
    
    Svaki bit iza trotočke u `(...)` i `[...]` međusobno je suprotan, pa je `x & -x = (...)10...00 & [...]10...00 = 10...00`, a to je upravo `lowbit`.

???+ note "Implementacija"
    === "C++"
        ```cpp
        int lowbit(int x) {
          // Broj koji u binarnom zapisu od x čine najniža jedinica i sve nule iza nje.
          // lowbit(0b01011000) == 0b00001000
          //          ~~~~^~~~
          // lowbit(0b01110010) == 0b00000010
          //          ~~~~~~^~
          return x & -x;
        }
        ```
    
    === "Python"
        ```python
        def lowbit(x):
            """
            Broj koji u binarnom zapisu od x čine najniža jedinica i sve nule iza nje.
            lowbit(0b01011000) == 0b00001000
                    ~~~~~^~~
            lowbit(0b01110010) == 0b00000010
                    ~~~~~~~^~
            """
            return x & -x
        ```

### Upit na intervalu

Pogledajmo sada konkretnu implementaciju operacija Fenwickova stabla; krenimo od upita na intervalu.

Prisjetimo se postupka upita za $a[4 \ldots 7]$: pretvorili smo ga u dva potpostupka – upit za zbroj $a[1 \ldots 7]$ i upit za zbroj $a[1 \ldots 3]$ – i na kraju oduzeli.

Zapravo se svaki upit na intervalu može tako riješiti: zbroj $a[l \ldots r]$ jednak je zbroju $a[1 \ldots r]$ minus zbroj $a[1 \ldots l - 1]$, čime intervalni problem pretvaramo u prefiksni, koji je lakše obraditi.

Pretvaranje intervalnog upita za $l \ldots r$ u prefiksne upite za $1 \ldots r$ i $1 \ldots l - 1$ te oduzimanje vrlo je čest trik na natjecanjima.

Kako onda izvesti prefiksni upit? Prisjetimo se postupka upita za $a[1 \ldots 7]$:

> Od $c_{7}$ skačemo unatrag; vidimo da $c_{7}$ pokriva samo element $a_{7}$. Zatim pogledamo $c_{6}$; vidimo da $c_{6}$ pokriva $a[5 \ldots 6]$. Zatim skočimo na $c_{4}$; vidimo da $c_{4}$ pokriva elemente $a[1 \ldots 4]$. Zatim pokušamo skočiti na $c_0$, ali $c_0$ zapravo ne postoji, pa stajemo.
>
> Upravo smo pronašli $c_7, c_6, c_4$; to su upravo tri mala intervala na koja se rastavlja $a[1 \ldots 7]$; spojimo ih i odgovor je $c_7 + c_6 + c_4$.

Promotrimo gornji postupak: pri svakom skoku unatrag sigurno skačemo na mjesto neposredno lijevo od lijevog kraja trenutnog intervala, koje postaje desni kraj novog intervala; samo tako prefiks rastavljamo bez preklapanja i bez praznina. Primjerice, $c_6$ pokriva $a[5 \ldots 6]$, pa sljedeći put skačemo na $5 - 1 = 4$, tj. pristupamo $c_4$.

Postupak upita za $a[1 \ldots x]$ možemo zapisati ovako:

-   krećemo od $c[x]$ i skačemo unatrag; $c[x]$ pokriva $a[x-\operatorname{lowbit}(x)+1 \ldots x]$;
-   stavimo $x \gets x - \operatorname{lowbit}(x)$; ako je $x = 0$, došli smo do kraja i prekidamo petlju; inače se vraćamo na prvi korak;
-   spojimo sve posjećene $c$.

U implementaciji ne moramo najprije pronaći sve $c$ pa ih tek onda spajati; možemo spajati usput dok skačemo.

Primjerice, ako je informacija koju održavamo zbroj, jednostavno stavimo početno $\mathrm{ans} = 0$, a zatim za svaki posjećeni $c[x]$ napravimo $\mathrm{ans} \gets \mathrm{ans} + c[x]$; na kraju je $\mathrm{ans}$ rezultat spajanja svega.

???+ note "Implementacija"
    === "C++"
        ```cpp
        int getsum(int x) {  // zbroj a[1]..a[x]
          int ans = 0;
          while (x > 0) {
            ans = ans + c[x];
            x = x - lowbit(x);
          }
          return ans;
        }
        ```
    
    === "Python"
        ```python
        def getsum(x):  # zbroj a[1]..a[x]
            ans = 0
            while x > 0:
                ans = ans + c[x]
                x = x - lowbit(x)
            return ans
        ```

### Fenwickovo stablo i svojstva njegova oblika stabla

Prije objašnjenja izmjene u točki objasnimo neka osnovna svojstva Fenwickova stabla i podrijetlo njegova oblika stabla; to pomaže boljem razumijevanju izmjene u točki.

Dogovorimo se:

-   $l(x) = x - \operatorname{lowbit}(x) + 1$. Dakle, $l(x)$ je lijevi kraj intervala koji pokriva $c[x]$.
-   Svaki pozitivni cijeli broj $x$ može se zapisati u obliku $s \times 2^{k + 1} + 2^k$, gdje je $\operatorname{lowbit}(x) = 2^k$.
-   U nastavku „$c[x]$ i $c[y]$ su disjunktni” znači da se intervali koje pokrivaju $c[x]$ i $c[y]$ ne sijeku, tj. $[l(x), x]$ i $[l(y), y]$ su disjunktni. Izrazi poput „$c[x]$ je sadržan u $c[y]$” tumače se analogno.

**Svojstvo $\boldsymbol{1}$: za $\boldsymbol{x \le y}$ ili su $\boldsymbol{c[x]}$ i $\boldsymbol{c[y]}$ disjunktni ili je $\boldsymbol{c[x]}$ sadržan u $\boldsymbol{c[y]}$.**

??? note "Dokaz"
    Dokaz: pretpostavimo da se $c[x]$ i $c[y]$ sijeku, tj. da se $[l(x), x]$ i $[l(y), y]$ sijeku; tada sigurno vrijedi $l(y) \le x \le y$.
    
    Zapišimo $y$ kao $s \times 2^{k +1} + 2^k$; tada je $l(y) = s \times 2^{k + 1} + 1$. Stoga se $x$ može zapisati kao $s \times 2^{k +1} + b$, gdje je $1 \le b \le 2^k$.
    
    Lako je vidjeti da je $\operatorname{lowbit}(x) = \operatorname{lowbit}(b)$. Kako je još $b - \operatorname{lowbit}(b) \ge 0$,
    
    vrijedi $l(x) = x - \operatorname{lowbit}(x) + 1 = s \times 2^{k +1} + b - \operatorname{lowbit}(b) +1 \ge s \times 2^{k +1} + 1 = l(y)$, tj. $l(y) \le l(x) \le x \le y$.
    
    Dakle, ako se $c[x]$ i $c[y]$ sijeku, interval koji pokriva $c[x]$ sigurno je u cijelosti sadržan u $c[y]$.

**Svojstvo $\boldsymbol{2}$: $\boldsymbol{c[x]}$ je pravi podskup od $\boldsymbol{c[x + \operatorname{lowbit}(x)]}$.**

??? note "Dokaz"
    Dokaz: neka je $y = x + \operatorname{lowbit}(x)$ i $x = s \times 2^{k + 1} + 2^k$; tada je $y = (s + 1) \times 2^{k +1}$ i $l(x) = s \times 2^{k + 1} + 1$.
    
    Lako je vidjeti da je $\operatorname{lowbit}(y) \ge 2^{k + 1}$, pa je $l(y) = (s + 1) \times 2^{k + 1} - \operatorname{lowbit}(y) + 1 \le s \times 2^{k +1} + 1= l(x)$, tj. $l(y) \le l(x) \le x < y$.
    
    Dakle, $c[x]$ je pravi podskup od $c[x + \operatorname{lowbit}(x)]$.

**Svojstvo $3$: za svaki $\boldsymbol{x < y < x + \operatorname{lowbit}(x)}$, $\boldsymbol{c[x]}$ i $\boldsymbol{c[y]}$ su disjunktni.**

??? note "Dokaz"
    Dokaz: neka je $x = s \times 2^{k + 1} + 2^k$; tada je $y = x + b = s \times 2^{k + 1} + 2^k + b$, gdje je $1 \le b < 2^k$.
    
    Lako je vidjeti da je $\operatorname{lowbit}(y) = \operatorname{lowbit}(b)$. Kako je još $b - \operatorname{lowbit}(b) \ge 0$,
    
    vrijedi $l(y) = y - \operatorname{lowbit}(y) + 1 = x + b - \operatorname{lowbit}(b) + 1 > x$, tj. $l(x) \le x < l(y) \le y$.
    
    Dakle, $c[x]$ i $c[y]$ su disjunktni.

Uz ta tri svojstva pogledajmo sada oblik stabla Fenwickova stabla (zanemarite bridove od $a$ prema $c$).

![](./images/fenwick.svg)

Zapravo je oblik stabla Fenwickova stabla graf koji dobijemo povlačenjem brida od $x$ prema $x + \operatorname{lowbit}(x)$, pri čemu je $x + \operatorname{lowbit}(x)$ roditelj od $x$.

Napomena: kad razmatramo oblik stabla Fenwickova stabla, ne uzimamo u obzir veličinu Fenwickova stabla, tj. radi lakše analize smatramo da je stablo beskonačno veliko. U stvarnoj implementaciji trebamo samo $c[x]$ za $x \le n$, gdje je $n$ duljina izvornog niza.

Ovo stablo prirodno ima mnogo lijepih svojstava; navodimo neka (neka $fa[u]$ označava neposrednog roditelja od $u$):

-   $u < fa[u]$.
-   $u$ je veći od svakog svog potomka i manji od svakog svog pretka.
-   $\operatorname{lowbit}$ vrha $u$ strogo je manji od $\operatorname{lowbit}$ vrha $fa[u]$.

??? note "Dokaz"
    Neka je $y = x + \operatorname{lowbit}(x)$ i $x = s \times 2^{k + 1} + 2^k$; tada je $y = (s + 1) \times 2^{k +1}$ i lako je vidjeti da je $\operatorname{lowbit}(y) \ge 2^{k + 1} > \operatorname{lowbit}(x)$, što je i trebalo dokazati.

-   Visina vrha $x$ je $\log_2\operatorname{lowbit}(x)$, tj. redni broj bita najniže `1` u binarnom zapisu od $x$.

??? note "Definicija visine"
    Visina $h(x)$ vrha $x$ zadovoljava: ako je $x \bmod 2 = 1$, onda je $h(x) = 0$; inače je $h(x) = \max(h(y)) + 1$, gdje $y$ prolazi svom djecom od $x$ (tada $x$ ima barem jedno dijete, $x - 1$).
    
    Drugim riječima, visina vrha točno je za $1$ veća od visine njegova najvišeg djeteta. Ako vrh nema djece, visina mu je $0$.
    
    Pojam visine uvodimo ovdje kako bismo kasnije lakše objasnili složenost.

-   $c[u]$ je pravi podskup od $c[fa[u]]$ (svojstvo $2$).
-   $c[u]$ je pravi podskup od $c[v]$, gdje je $v$ bilo koji predak od $u$ (indukcijom iz prethodnog svojstva).
-   $c[u]$ pravo sadrži $c[v]$, gdje je $v$ bilo koji potomak od $u$ (prethodno svojstvo sa zamijenjenim $u$ i $v$).
-   Za svaki $v' > u$, ako $v'$ nije predak od $u$, onda su $c[u]$ i $c[v']$ disjunktni.

??? note "Dokaz"
    Među $u$ i precima od $u$ sigurno postoji vrh $v$ takav da je $v < v' < fa[v]$; prema svojstvu $3$, $c[v']$ je disjunktan s $c[v]$, a $c[v]$ sadrži $c[u]$, pa je $c[v']$ disjunktan s $c[u]$.

-   Za svaki $v < u$, ako $v$ nije u podstablu od $u$, onda su $c[u]$ i $c[v]$ disjunktni (prethodno svojstvo sa zamijenjenim $u$ i $v'$).
-   Za svaki $v > u$, $c[u]$ je pravi podskup od $c[v]$ ako i samo ako je $v$ predak od $u$ (sažetak nekoliko prethodnih svojstava). To je temeljno načelo izmjene u točki u Fenwickovu stablu.
-   Neka je $u = s \times 2^{k + 1} + 2^k$; tada $u$ ima $k = \log_2\operatorname{lowbit}(u)$ djece, s oznakama $u - 2^t(0 \le t < k)$.
    -   Primjer: neka je $k = 3$ i binarna oznaka od $u$ neka je `...1000`; tada $u$ ima troje djece, s binarnim oznakama `...0111`, `...0110` i `...0100`.

??? note "Dokaz"
    Oduzmemo li od broja $x$ broj $2^t$, $t$-ti bit od $x$ se invertira, a niži bitovi ostaju nepromijenjeni.
    
    Promotrimo dijete $v$ od $u$: vrijedi $v + \operatorname{lowbit}(v) = u$, tj. $v = u - 2^t$ i $\operatorname{lowbit}(v) = 2^t$. Neka je $u = s \times 2^{k + 1} + 2^k$.
    
    **Slučaj $\boldsymbol{0 \le t < k}$**: $t$-ti bit od $u$ i svi bitovi iza njega su $0$, pa $t$-ti bit od $v = u - 2^t$ postaje $1$, a bitovi iza njega ostaju $0$; **vrijedi** $\operatorname{lowbit}(v) = 2^t$.
    
    **Slučaj $\boldsymbol{t = k}$**: tada je $v = u - 2^k$, $k$-ti bit od $v$ postaje $0$; **ne vrijedi** $\operatorname{lowbit}(v) = 2^t$.
    
    **Slučaj $\boldsymbol{t > k}$**: tada je $v = u - 2^t$, $k$-ti bit od $v$ je $1$, pa je $\operatorname{lowbit}(v) = 2^k$; **ne vrijedi** $\operatorname{lowbit}(v) = 2^t$.

-   Intervali koje pokrivaju $c$ sve djece od $u$ točno se nadovezuju u $[l(u), u - 1]$.
    -   Primjer: neka je $k = 3$ i binarna oznaka od $u$ neka je `...1000`; tada $u$ ima troje djece, s binarnim oznakama `...0111`, `...0110` i `...0100`.
    -   `c[...0100]` predstavlja `a[...0001 ~ ...0100]`.
    -   `c[...0110]` predstavlja `a[...0101 ~ ...0110]`.
    -   `c[...0111]` predstavlja `a[...0111 ~ ...0111]`.
    -   Lako je vidjeti da je unija gornjih triju pokrivenih intervala upravo `a[...0001 ~ ...0111]`, tj. $[l(u), u - 1]$.

??? note "Dokaz"
    Djeca od $u$ uvijek se mogu zapisati kao $u - 2^t(0 \le t < k)$; lako je vidjeti da je za manji $t$ broj $u - 2^t$ veći, pa je interval koji predstavlja više udesno. Neka je $f(t) = u - 2^t$; tada su $f(k - 1), f(k - 2), \ldots, f(0)$ redom djeca od $u$ slijeva nadesno.
    
    Lako je vidjeti da je $\operatorname{lowbit}(f(t)) = 2^t$, pa je $l(f(t)) = u - 2^t - 2^t + 1 = u - 2^{t + 1} + 1$.
    
    Promotrimo dvoje susjedne djece $f(t + 1)$ i $f(t)$. Desni kraj intervala prvog je $f(t + 1) = u - 2^{t + 1}$, a lijevi kraj intervala drugog je $l(f(t)) = u - 2^{t + 1} + 1$; točno se nadovezuju.
    
    Promotrimo krajnje lijevo dijete $f(k - 1)$: lijevi kraj njegova intervala $l(f(k - 1)) = u - 2^k + 1$ upravo je $l(u)$.
    
    Promotrimo krajnje desno dijete $f(0)$: desni kraj njegova intervala upravo je $u - 1$.
    
    Dakle, intervali koje pokrivaju ta djeca točno se slažu u $[l(u), u - 1]$.

### Izmjena u točki

Razmotrimo sada kako izmijeniti $a[x]$ u točki.

Cilj nam je brzo i ispravno održavati niz $c$. Radi učinkovitosti trebamo proći i izmijeniti samo one $c[y]$ koji pokrivaju $a[x]$, jer se ostali $c$ očito ne mijenjaju.

Svaki $c[y]$ koji pokriva $a[x]$ sigurno sadrži $c[x]$ (prema svojstvu $1$), pa je $y$ u obliku stabla Fenwickova stabla predak od $x$. Stoga od $x$ neprestano skačemo na roditelja dok ne premašimo duljinu izvornog niza.

Neka $n$ označava veličinu niza $a$; postupak izmjene $a[x]$ u točki lako je zapisati:

-   početno stavimo $x' = x$;
-   izmijenimo $c[x']$;
-   stavimo $x' \gets x' + \operatorname{lowbit}(x')$; ako je $x' > n$, došli smo do kraja i prekidamo petlju; inače se vraćamo na drugi korak.

Vrsta informacije na intervalu i vrsta izmjene u točki zajedno određuju način izmjene $c[x']$. Nekoliko primjera:

-   Ako $c[x']$ održava zbroj intervala, a izmjena je uvećanje $a[x]$ za $p$, onda se svi $c[x']$ također uvećaju za $p$.
-   Ako $c[x']$ održava umnožak intervala, a izmjena je množenje $a[x]$ s $p$, onda se svi $c[x']$ također pomnože s $p$.

Međutim, zbog slobode izmjene u točki vrsta izmjene i održavana informacija ne moraju biti ista operacija; primjerice, ako $c[x']$ održava zbroj intervala, a izmjena je pridruživanje $a[x]$ vrijednosti $p$, možemo je pretvoriti u uvećanje $a[x]$ za $p - a[x]$. Ako je izmjena množenje $a[x]$ s $p$, pretvorimo je u uvećanje $a[x]$ za $a[x] \times p - a[x]$.

Implementaciju dajemo na primjeru održavanja zbroja intervala i zbrajanja u točki.

???+ note "Implementacija"
    === "C++"
        ```cpp
        void add(int x, int k) {
          while (x <= n) {  // ne smije izaći izvan granica
            c[x] = c[x] + k;
            x = x + lowbit(x);
          }
        }
        ```
    
    === "Python"
        ```python
        def add(x, k):
            while x <= n:  # ne smije izaći izvan granica
                c[x] = c[x] + k
                x = x + lowbit(x)
        ```

### Izgradnja stabla

To znači izgraditi Fenwickovo stablo iz početno zadanog niza (potpuno predobraditi $c$).

Obično se to može izravno pretvoriti u $n$ izmjena u točki, složenosti $\Theta(n \log n)$ (analiza složenosti slijedi kasnije).

Primjerice, ako treba izgraditi stablo za niz $a = (5, 1, 4)$, to jednostavno gledamo kao zbrajanje $5$ u točki $a[1]$, zbrajanje $1$ u točki $a[2]$ i zbrajanje $4$ u točki $a[3]$.

Postoji i izgradnja u $\Theta(n)$; vidi odjeljak [$\Theta(n)$ izgradnja stabla](#thetan-izgradnja-stabla) na ovoj stranici.

### Analiza složenosti

Prostorna složenost očito je $\Theta(n)$.

Vremenska složenost:

-   Za upit na intervalu: cijeli iterativni postupak $x \gets x - \operatorname{lowbit}(x)$ možemo gledati kao postupno pretvaranje svih jedinica u binarnom zapisu od $x$ u nule, od nižih bitova prema višima; broj intervala na koje rastavljamo jednak je broju jedinica u binarnom zapisu od $x$ (tj. $\operatorname{popcount}(x)$). Dakle, složenost jednog upita je $\Theta(\log n)$;
-   Za izmjenu u točki: pri skakanju na roditelja posjećena visina strogo raste, a stalno vrijedi $x \le n$. Budući da je visina vrha $x$ jednaka $\log_2\operatorname{lowbit}(x)$, dosegnuta visina ne premašuje $\log_2n$, pa je broj posjećenih $c$ reda $\log n$. Dakle, složenost jedne izmjene u točki je $\Theta(\log n)$.

## Zbrajanje na intervalu, zbroj intervala

Preduvjet: [Prefiksne sume i razlike](../basic/prefix-sum.md).

Ovaj se problem može riješiti s dva Fenwickova stabla koja održavaju niz razlika.

Promotrimo niz razlika $d$ niza $a$, gdje je $d[i] = a[i] - a[i - 1]$. Budući da je prefiksni zbroj niza razlika upravo izvorni niz, vrijedi $a_i=\sum_{j=1}^i d_j$.

Kao i prije, upit za zbroj intervala pretvaramo oduzimanjem u upit za prefiksni zbroj. Promotrimo upit za zbroj $a[1 \ldots r]$, tj. $\sum_{i=1}^{r} a_i$, i izvedimo:

$$
\begin{aligned}
&\sum_{i=1}^{r} a_i\\=&\sum_{i=1}^r\sum_{j=1}^i d_j
\end{aligned}
$$

Promotrimo li izraz, lako vidimo da se svaki $d_j$ zbraja ukupno $r - j + 1$ puta. Nastavimo izvod:

$$
\begin{aligned}
&\sum_{i=1}^r\sum_{j=1}^i d_j\\=&\sum_{i=1}^r d_i\times(r-i+1)
\\=&\sum_{i=1}^r d_i\times (r+1)-\sum_{i=1}^r d_i\times i
\end{aligned}
$$

Iz $\sum_{i=1}^r d_i$ ne možemo izvesti vrijednost $\sum_{i=1}^r d_i \times i$, pa trebamo dva Fenwickova stabla koja zasebno održavaju zbrojeve $d_i$ i $d_i \times i$.

Kako onda izvesti zbrajanje na intervalu? Promotrimo kako zbrajanje $x$ na intervalu $a[l \ldots r]$ izvornog niza utječe na $d$.

Budući da je razlika $d[i] = a[i] - a[i - 1]$,

-   $a[l]$ se uvećao za $v$, a $a[l - 1]$ je nepromijenjen, pa se $d[l]$ uvećao za $v$;
-   $a[r + 1]$ je nepromijenjen, a $a[r]$ se uvećao za $v$, pa se $d[r + 1]$ umanjio za $v$;
-   za svaki $i$ različit od $l$ i od $r+1$, $a[i]$ i $a[i - 1]$ ili su oba nepromijenjena ili su se oba uvećala za $v$, a $a[i] + v - (a[i - 1] + v)$ i dalje je $a[i] - a[i - 1]$, pa su ostali $d[i]$ nepromijenjeni.

Odatle se lako dosjetiti načina održavanja: u Fenwickovu stablu koje održava $d_i$ zbrojimo $v$ u točki $l$ i $-v$ u točki $r + 1$; u Fenwickovu stablu koje održava $d_i \times i$ zbrojimo $v \times l$ u točki $l$ i $-v \times (r + 1)$ u točki $r + 1$.

Za slabiji problem, „zbrajanje na intervalu uz upit u točki”, dovoljno je Fenwickovim stablom održavati samo niz razlika $d_i$. Za upit vrijednosti $a[x]$ u točki jednostavno izračunamo zbroj $d[1 \ldots x]$.

Ovdje izravno dajemo kôd za „zbrajanje na intervalu, zbroj intervala”:

???+ note "Implementacija"
    === "C++"
        ```cpp
        int t1[MAXN], t2[MAXN], n;
        
        int lowbit(int x) { return x & (-x); }
        
        void add(int k, int v) {
          int v1 = k * v;
          while (k <= n) {
            t1[k] += v, t2[k] += v1;
            // Pazi: ne smije se pisati t2[k] += k * v, jer k više nije indeks u izvornom nizu
            k += lowbit(k);
          }
        }
        
        int getsum(int *t, int k) {
          int ret = 0;
          while (k) {
            ret += t[k];
            k -= lowbit(k);
          }
          return ret;
        }
        
        void add1(int l, int r, int v) {
          add(l, v), add(r + 1, -v);  // zbrajanje na intervalu rastavljamo na dva prefiksna zbrajanja
        }
        
        long long getsum1(int l, int r) {
          return (r + 1ll) * getsum(t1, r) - 1ll * l * getsum(t1, l - 1) -
                 (getsum(t2, r) - getsum(t2, l - 1));
        }
        ```
    
    === "Python"
        ```python
        t1 = [0] * MAXN
        t2 = [0] * MAXN
        n = 0
        
        
        def lowbit(x):
            return x & (-x)
        
        
        def add(k, v):
            v1 = k * v
            while k <= n:
                t1[k] = t1[k] + v
                t2[k] = t2[k] + v1
                k = k + lowbit(k)
        
        
        def getsum(t, k):
            ret = 0
            while k:
                ret = ret + t[k]
                k = k - lowbit(k)
            return ret
        
        
        def add1(l, r, v):
            add(l, v)
            add(r + 1, -v)
        
        
        def getsum1(l, r):
            return (
                (r) * getsum(t1, r)
                - l * getsum(t1, l - 1)
                - (getsum(t2, r) - getsum(t2, l - 1))
            )
        ```

Po istom načelu trebalo bi se moći implementirati „množenje na intervalu, umnožak intervala”, „XOR intervala s brojem, upit za XOR intervala” itd., sve dok su održavana informacija i operacija na intervalu ista vrsta operacije; zainteresirani čitatelji mogu to sami isprobati.

## Dvodimenzionalno Fenwickovo stablo

### Izmjena u točki, upit za podmatricu

Dvodimenzionalno Fenwickovo stablo, poznato i kao Fenwickovo stablo nad Fenwickovim stablima, služi za održavanje izmjena u točki i prefiksnih informacija nad dvodimenzionalnim nizom.

Slično jednodimenzionalnom Fenwickovu stablu, s $c(x, y)$ označavamo ukupnu informaciju matrice $a(x - \operatorname{lowbit}(x) + 1, y - \operatorname{lowbit}(y) + 1) \ldots a(x, y)$, tj. matrice kojoj je $a(x, y)$ donji desni kut, visina $\operatorname{lowbit}(x)$, a širina $\operatorname{lowbit}(y)$.

Za izmjenu u točki neka je:

$$
f(x, i) = \begin{cases}x &i = 0\\f(x, i - 1) + \operatorname{lowbit}(f(x, i - 1)) & i > 0\\\end{cases}
$$

Dakle, $f(x, i)$ je $i$-ti predak od $x$ u obliku stabla Fenwickova stabla ($0$-ti predak je sam vrh).

Tada $a(x, y)$ pokrivaju samo elementi $c(f(x, i), f(y, j))$, pa pri izmjeni $a(x, y)$ treba izmijeniti samo sve $c(f(x, i), f(y, j))$ za koje je $f(x, i) \le n$ i $f(y, j) \le m$.

??? note "Dokaz ispravnosti"
    Neka $c(p, q)$ pokriva $a(x, y)$; tražimo moguće vrijednosti $p$ i $q$.
    
    Promotrimo jednodimenzionalno Fenwickovo stablo $c_1$ veličine $n$ (nad izvornim nizom $a_1$) i jednodimenzionalno Fenwickovo stablo $c_2$ veličine $m$ (nad izvornim nizom $a_2$).
    
    Tvrdnja je tada ekvivalentna uvjetu: $c_1(p)$ pokriva $a_1[x]$ i $c_2(q)$ pokriva $a_2[y]$.
    
    Drugim riječima, u obliku stabla Fenwickova stabla $p$ je jedan od vrhova među $x$ i njegovim precima, a $q$ jedan od vrhova među $y$ i njegovim precima.
    
    Dakle, $p = f(x, i)$ i $q = f(y, j)$.

Za upit neka je:

$$
g(x, i) = \begin{cases}x &i = 0\\g(x, i - 1) - \operatorname{lowbit}(g(x, i - 1)) & i, g(x, i - 1) > 0\\0&\text{otherwise.}\end{cases}
$$

Tada spajamo sve $c(g(x, i), g(y, j))$ za koje je $g(x, i), g(y, j) > 0$.

??? note "Dokaz ispravnosti"
    Neka $\circ$ označava operaciju spajanja dviju informacija (primjerice, ako je informacija zbroj intervala, onda je $\circ = +$).
    
    Promotrimo jednodimenzionalno Fenwickovo stablo $c_1$: $c_1[g(x, 0)] \circ c_1[g(x, 1)] \circ c_1[g(x, 2)] \circ \cdots$ upravo predstavlja informaciju intervala $[1 \ldots x]$ izvornog niza.
    
    Slično, neka je $t(x) = c(x, g(y, 0)) \circ c(x, g(y, 1)) \circ c(x, g(y, 2)) \circ \cdots$; tada $t(x)$ upravo predstavlja informaciju matrice $a(x - \operatorname{lowbit}(x) + 1, 1) \ldots a(x, y)$.
    
    Opet slično, $t(g(x, 0)) \circ t(g(x, 1)) \circ t(g(x, 2)) \circ \cdots$ predstavlja informaciju matrice $a(1, 1) \ldots a(x, y)$.
    
    Zapravo, gledamo li funkciju $t(x)$ kao Fenwickovo stablo, dobivamo Fenwickovo stablo ugniježđeno u Fenwickovo stablo; otud i naziv „Fenwickovo stablo nad Fenwickovim stablima”.

Slijedi kôd za zbrajanje u točki i upit za zbroj podmatrice.

???+ note "Implementacija"
    === "Zbrajanje u točki"
        ```cpp
        void add(int x, int y, int v) {
          for (int i = x; i <= n; i += lowbit(i)) {
            for (int j = y; j <= m; j += lowbit(j)) {
              // Pazi: ovdje moramo uvesti varijable petlje; ne možemo kao u jednodimenzionalnom slučaju pisati samo while (x <= n)
              c[i][j] += v;
            }
          }
        }
        ```
    
    === "Upit za zbroj podmatrice"
        ```cpp
        int sum(int x, int y) {
          int res = 0;
          for (int i = x; i > 0; i -= lowbit(i)) {
            for (int j = y; j > 0; j -= lowbit(j)) {
              res += c[i][j];
            }
          }
          return res;
        }
        
        int ask(int x1, int y1, int x2, int y2) {
          // upit za zbroj podmatrice
          return sum(x2, y2) - sum(x2, y1 - 1) - sum(x1 - 1, y2) + sum(x1 - 1, y1 - 1);
        }
        ```

### Zbrajanje na podmatrici, zbroj podmatrice

Preduvjet: [Prefiksne sume i razlike](../basic/prefix-sum.md) i odjeljak [Zbrajanje na intervalu, zbroj intervala](#zbrajanje-na-intervalu-zbroj-intervala) na ovoj stranici.

Slično problemu „zbrajanje na intervalu, zbroj intervala” jednodimenzionalnog Fenwickova stabla, razmotrimo održavanje niza razlika.

Niz razlika nad dvodimenzionalnim nizom izgleda ovako:

$$
d(i, j) = a(i, j) - a(i - 1, j) - a(i, j - 1) + a(i - 1, j - 1)．
$$

??? note "Zašto baš takva definicija?"
    Zato što bi u idealnom slučaju dvodimenzionalni prefiksni zbroj nad matricom razlika trebao dati izvornu matricu, jer su to međusobno inverzne operacije.
    
    Formula dvodimenzionalnog prefiksnog zbroja glasi:
    
    $s(i, j) = s(i - 1, j) + s(i, j - 1) - s(i - 1, j - 1) + a(i, j)$.
    
    Dakle, ako je $a$ izvorni niz, a $d$ niz razlika, vrijedi:
    
    $a(i, j) = a(i - 1, j) + a(i, j - 1) - a(i - 1, j - 1) + d(i, j)$
    
    Prebacivanjem članova dobivamo formulu dvodimenzionalnih razlika:
    
    $d(i, j) = a(i, j) - a(i - 1, j) - a(i, j - 1) + a(i - 1, j - 1)$.

Tako zbrajanje $v$ na podmatrici s gornjim lijevim kutom $(x_1, y_1)$ i donjim desnim kutom $(x_2, y_2)$ odgovara, u nizu razlika, zbrajanju $v$ u točkama $d(x_1, y_1)$ i $d(x_2 + 1, y_2 + 1)$ te zbrajanju $-v$ u točkama $d(x_2 + 1, y_1)$ i $d(x_1, y_2 + 1)$.

Što se tiče razloga, dovoljno je ta četiri $d$ raspisati po definiciji i analizirati promjenu svakog člana.

Primjer: neka je niz razlika početno $0$; nakon zbrajanja $v$ na podmatrici $a(2, 2) \ldots a(3, 4)$ niz razlika postaje:

$$
\begin{pmatrix}0&0&0&0&0\\0&v&0&0&-v\\0&0&0&0&0\\0&-v&0&0&v\end{pmatrix}
$$

(Pritom je podmatrica $a(2, 2) \ldots a(3, 4)$ upravo središnja matrica veličine $2 \times 3$.)

Dakle, zbrajanje na podmatrici izvodimo pretvaranjem u četiri zbrajanja u točki nad nizom razlika.

Razmotrimo sada upit za zbroj podmatrice:

Za točku $(x, y)$ dvodimenzionalni prefiksni zbroj može se zapisati kao:

$$
\sum_{i = 1}^x\sum_{j = 1}^y\sum_{h = 1}^i\sum_{k = 1}^j d(h, k)
$$

Razlog je taj što je prefiksni zbroj prefiksnog zbroja razlika upravo izvorni prefiksni zbroj.

Slično problemu „zbrajanje na intervalu, zbroj intervala” jednodimenzionalnog Fenwickova stabla, prebrojimo pojavljivanja $d(h, k)$: ima ih $(x - h + 1) \times (y - k + 1)$.

Nastavimo izvod:

$$
\begin{aligned}
&\sum_{i = 1}^x\sum_{j = 1}^y\sum_{h = 1}^i\sum_{k = 1}^j d(h, k)
\\=&\sum_{i = 1}^x\sum_{j = 1}^y d(i, j) \times (x - i + 1) \times (y - j + 1)
\\=&\sum_{i = 1}^x\sum_{j = 1}^y d(i, j) \times (xy + x + y + 1) - d(i, j) \times i \times (y + 1) - d(i, j) \times j \times (x + 1) + d(i, j) \times i \times j
\end{aligned}
$$

Dakle, trebamo održavati četiri Fenwickova stabla, koja redom održavaju zbrojeve $d(i, j)$, $d(i, j) \times i$, $d(i, j) \times j$ i $d(i, j) \times i \times j$.

Naravno, kao i u jednodimenzionalnom slučaju, ako treba samo zbrajanje na podmatrici uz upit u točki, dovoljno je održavati jedan niz razlika i pitati za prefiksni zbroj.

Slijedi kôd:

???+ note "Implementacija"
    ```cpp
    using ll = long long;
    ll t1[N][N], t2[N][N], t3[N][N], t4[N][N];
    
    void add(ll x, ll y, ll z) {
      for (int X = x; X <= n; X += lowbit(X))
        for (int Y = y; Y <= m; Y += lowbit(Y)) {
          t1[X][Y] += z;
          t2[X][Y] += z * x;  // Pazi: z * x, a ne z * X; isto vrijedi i dalje
          t3[X][Y] += z * y;
          t4[X][Y] += z * x * y;
        }
    }
    
    void range_add(ll xa, ll ya, ll xb, ll yb,
                   ll z) {  // podmatrica od (xa, ya) do (xb, yb)
      add(xa, ya, z);
      add(xa, yb + 1, -z);
      add(xb + 1, ya, -z);
      add(xb + 1, yb + 1, z);
    }
    
    ll ask(ll x, ll y) {
      ll res = 0;
      for (int i = x; i; i -= lowbit(i))
        for (int j = y; j; j -= lowbit(j))
          res += (x + 1) * (y + 1) * t1[i][j] - (y + 1) * t2[i][j] -
                 (x + 1) * t3[i][j] + t4[i][j];
      return res;
    }
    
    ll range_ask(ll xa, ll ya, ll xb, ll yb) {
      return ask(xb, yb) - ask(xb, ya - 1) - ask(xa - 1, yb) + ask(xa - 1, ya - 1);
    }
    ```

## Fenwickovo stablo nad frekvencijskim nizom i primjene

Znamo da se obično Fenwickovo stablo gradi izravno nad izvornim nizom; $c_6$ predstavlja informaciju intervala $a[5 \ldots 6]$.

No zapravo Fenwickovo stablo možemo izgraditi i nad frekvencijskim nizom izvornog niza; to je Fenwickovo stablo nad frekvencijskim nizom.

??? note "Što je frekvencijski niz?"
    Frekvencijski niz $b$ niza $a$ zadovoljava: vrijednost $b[x]$ jednaka je broju pojavljivanja $x$ u $a$.
    
    Primjerice, frekvencijski niz od $a = (1, 3, 4, 3, 4)$ jest $b = (1, 0, 2, 2)$.
    
    Očito veličina $b$ ovisi o rasponu vrijednosti od $a$.
    
    Ako je raspon vrijednosti izvornog niza prevelik, a bitne nisu konkretne vrijednosti nego samo njihov međusobni poredak, izvorni se niz često [komprimira (diskretizira)](../misc/discrete.md) prije izgradnje frekvencijskog niza.
    
    Osim toga, frekvencijski niz prikazuje niz bez obzira na poredak: opisuje sadržaj elemenata niza, a zanemaruje njihov redoslijed; ako se dva niza razlikuju samo u poretku, a sadrže isto, imaju isti frekvencijski niz.
    
    Zato je kod problema u kojima poredak zadanog niza ne utječe na odgovor obično zornije razmišljati u terminima frekvencijskog niza, primjerice [\[NOIP2021\] 数列](https://www.luogu.com.cn/problem/P7961).

Pomoću Fenwickova stabla nad frekvencijskim nizom možemo riješiti nekoliko klasičnih problema.

### Izmjena u točki, upit za globalno $k$-ti najmanji

Ovdje razmatramo samo $k$-ti najmanji; problem $k$-tog najvećeg jednostavnim se računom svodi na $k$-ti najmanji.

Problem dopušta kompresiju vrijednosti: ako je raspon vrijednosti izvornog niza $a$ prevelik, komprimiramo ga pa tek onda gradimo frekvencijski niz $b$. Pazite: treba komprimirati i vrijednosti koje se pojavljuju u izmjenama u točki, a ne samo elemente izvornog niza $a$.

Za izmjenu u točki dovoljno je izmjenu u točki izvornog niza pretvoriti u izmjenu u točki frekvencijskog niza. Konkretno, ako se $a[x]$ mijenja iz $y$ u $z$, to u frekvencijskom nizu $b$ odgovara umanjenju $b[y]$ za $1$ i uvećanju $b[z]$ za $1$.

Za upit $k$-tog najmanjeg razmotrimo binarno pretraživanje po $x$: pitamo za prefiksni zbroj $[1, x]$ frekvencijskog niza i tražimo $x_0$ takav da je prefiksni zbroj $[1, x_0]$ $< k$, a prefiksni zbroj $[1, x_0 + 1]$ $\ge k$; tada je $k$-ti broj $x_0 + 1$ (napomena: prefiksni zbroj $[1, 0]$ smatramo $0$).

Složenost je tada $\Theta(\log^2n)$.

Razmotrimo zamjenu binarnog pretraživanja binary liftingom.

Neka je $x = 0$, $\mathrm{sum} = 0$; prolazimo $i$ od $\log_2n$ prema $0$:

-   pitamo za zbroj $t$ intervala $[x + 1 \ldots x + 2^i]$ frekvencijskog niza;
-   ako je $\mathrm{sum} + t < k$, proširenje uspijeva: $x \gets x + 2^i$, $\mathrm{sum} \gets \mathrm{sum} + t$; inače proširenje ne uspijeva i ništa ne radimo.

Tako dobiveni $x$ najveći je broj za koji je prefiksni zbroj $[1 \ldots x]$ $< k$, pa je konačni odgovor $x + 1$.

Čini se da ova metoda nimalo ne poboljšava vremensku učinkovitost, ali zapravo je za upit zbroja $[x + 1 \ldots x + 2^i]$ dovoljno pristupiti vrijednosti $c[x + 2^i]$.

Razlog je jednostavan: promotrimo $\operatorname{lowbit}(x + 2^i)$; on je sigurno $2^i$, jer su se na $x$ dotad dodavale samo potencije $2^j$ s $j > i$. Zato $c[x + 2^i]$ predstavlja upravo interval $[x + 1 \ldots x + 2^i]$.

Tako se vremenska složenost smanjuje na $\Theta(\log n)$.

???+ note "Implementacija"
    === "C++"
        ```cpp
        // upit za k-ti najmanji u Fenwickovu stablu nad frekvencijskim nizom
        int kth(int k) {
          int sum = 0, x = 0;
          for (int i = log2(n); ~i; --i) {
            x += 1 << i;                   // pokušaj proširenja
            if (x > n || sum + t[x] >= k)  // ako proširenje ne uspije
              x -= 1 << i;
            else
              sum += t[x];
          }
          return x + 1;  // ako ne postoji, vraća n + 1
        }
        ```
    
    === "Python"
        ```python
        # upit za k-ti najmanji u Fenwickovu stablu nad frekvencijskim nizom
        def kth(k):
            sum = 0
            x = 0
            i = int(log2(n))
            while ~i:
                x = x + (1 << i)  # pokušaj proširenja
                if x > n or sum + t[x] >= k:  # ako proširenje ne uspije
                    x = x - (1 << i)
                else:
                    sum = sum + t[x]
                i = i - 1
            return x + 1  # ako ne postoji, vraća n + 1
        ```

### Globalne inverzije (globalni dvodimenzionalni parcijalni poredak)

Dodatno čitanje i referentna implementacija: [Inverzije](../math/permutation.md#逆序数)

Globalne inverzije također se mogu elegantno riješiti Fenwickovim stablom nad frekvencijskim nizom. Problem glasi: za zadani niz $a$ duljine $n$ izračunajte broj parova $(i, j)$ u $a$ za koje je $i < j$ i $a[i] > a[j]$.

Problem dopušta kompresiju vrijednosti: ako je raspon vrijednosti izvornog niza $a$ prevelik, komprimiramo ga pa tek onda gradimo frekvencijski niz $b$.

Prolazimo $i$ unatrag od $n$ do $1$ kao indeks prvog elementa inverzije, zatim izračunamo koliko $j > i$ zadovoljava $a[j] < a[i]$ i na kraju zbrojimo odgovore.

Zapravo trebamo učiniti samo ovo (neka je trenutno $a[i] = x$):

-   upitamo za prefiksni zbroj $b[1 \ldots x - 1]$; to je broj inverzija čiji je lijevi element $a[i]$;
-   uvećamo $b[x]$ za $1$.

Razlog je sasvim prirodan: elementi koji se pojavljuju u $b[1 \ldots x-1]$ sigurno su manji od trenutnog $x = a[i]$, a zbog prolaska $i$ unatrag indeksi $j$ u izvornom nizu tih elemenata koji su već u frekvencijskom nizu prirodno su veći od trenutnog indeksa $i$.

Na primjeru, $a = (4, 3, 1, 2, 1)$.

$i$ prolazi $5 \to 1$:

-   $a[5] = 1$, prefiksni zbroj $b[1 \ldots 0]$ je $0$, $b[1]$ uvećamo za $1$, $b = (1, 0, 0, 0)$.
-   $a[4] = 2$, prefiksni zbroj $b[1 \ldots 1]$ je $1$, $b[2]$ uvećamo za $1$, $b = (1, 1, 0, 0)$.
-   $a[3] = 1$, prefiksni zbroj $b[1 \ldots 0]$ je $0$, $b[1]$ uvećamo za $1$, $b = (2, 1, 0, 0)$.
-   $a[2] = 3$, prefiksni zbroj $b[1 \ldots 2]$ je $3$, $b[3]$ uvećamo za $1$, $b = (2, 1, 1, 0)$.
-   $a[1] = 4$, prefiksni zbroj $b[1 \ldots 3]$ je $4$, $b[4]$ uvećamo za $1$, $b = (2, 1, 1, 1)$.

Konačni je odgovor stoga $0 + 1 + 0 + 3 + 4 = 8$.

Primijetimo da se pri prolasku po $i$ dva koraka – upit $b[1 \ldots x - 1]$ i uvećanje $b[x]$ – mogu zamijeniti, tj. najprije uvećati $b[x]$ pa tek onda upitati $b[1 \ldots x - 1]$, bez utjecaja na odgovor. Dva objašnjenja:

-   Izmjena $b[x]$ ne utječe na upit $b[1 \ldots x - 1]$.
-   Nakon zamjene zapravo brojimo parove s $i \le j$ i $a[i] > a[j]$, a za $i = j$ nikad ne vrijedi $a[i] > a[j]$, pa je $i \le j$ isto što i $i < j$; to je ekvivalentno izvornom problemu inverzija.

Ako brojimo nestroge inverzije ($i < j$ i $a[i] \ge a[j]$), treba pitati za zbroj $b[1 \ldots x]$, a tada se ta dva koraka ne smiju zamijeniti; opet dva objašnjenja:

-   Izmjena $b[x]$ **utječe** na upit $b[1 \ldots x]$.
-   Nakon zamjene zapravo brojimo parove s $i \le j$ i $a[i] \ge a[j]$, a za $i = j$ uvijek vrijedi $a[i] \ge a[j]$, pa $i \le j$ **nije isto što i** $i < j$ i problem **nije ekvivalentan** izvornomu.

Ako brojimo parove s $i \le j$ i $a[i] \ge a[j]$, onda ta dva koraka upravo treba zamijeniti.

Osim toga, za izvorni problem inverzija postoji i pristup s prolaskom $j$ unaprijed, pri čemu pitamo koliko $i < j$ zadovoljava $a[i] > a[j]$. Postupak je sljedeći (neka je $x = a[j]$):

-   upitamo za zbroj intervala $b[x + 1 \ldots V]$ ($V$ je veličina od $b$, tj. raspon vrijednosti od $a$ (ili raspon nakon kompresije));
-   uvećamo $b[x]$ za $1$.

Razlog: elementi koji se pojavljuju u $b[x + 1 \ldots V]$ sigurno su veći od trenutnog $x = a[j]$, a zbog prolaska $j$ unaprijed indeksi $i$ u izvornom nizu tih elemenata koji su već u frekvencijskom nizu prirodno su manji od trenutnog indeksa $j$.

Nadalje, inverzije se mogu brojati i [merge sortom](../basic/merge-sort.md#inverzije). Taj pristup izbjegava kompresiju vrijednosti. Vremenska je složenost također $O(n\log n)$. Referentne implementacije obaju algoritama nalaze se u poglavlju [Inverzije](../math/permutation.md#逆序数).

## Fenwickovo stablo za neinvertibilne informacije

Primjerice za održavanje intervalnih ekstrema i slično.

Napomena: iako ova metoda ima malo koda, vremenska složenost i izmjene u točki i upita na intervalu je $\Theta(\log^2n)$, što je lošije od složenosti $\Theta(\log n)$ sa segment treeom.

### Upit na intervalu

I dalje slijedimo prijašnju ideju: od $r$ skačemo unatrag po $\operatorname{lowbit}$, ali ne smijemo skočiti lijevo od $l$.

Zato, kad dođemo do $c[x]$, najprije provjerimo je li sljedeće odredište $x - \operatorname{lowbit}(x)$ manje od $l$:

-   ako je manje od $l$, u ukupnu informaciju izravno spojimo **točku $\boldsymbol{a[x]}$** i skočimo na $c[x - 1]$;
-   ako je veće ili jednako $l$, nismo izašli iz granica, pa normalno spojimo $c[x]$ i skočimo na $c[x - \operatorname{lowbit}(x)]$.

Slijedi kôd na primjeru upita za maksimum na intervalu:

???+ note "Implementacija"
    ```cpp
    int getmax(int l, int r) {
      int ans = 0;
      while (r >= l) {
        ans = max(ans, a[r]);
        --r;
        for (; r - lowbit(r) >= l; r -= lowbit(r)) {
          // Pazi: uvjet petlje ne smije glasiti r - lowbit(r) + 1 >= l,
          // inače za l = 1 r skoči na 0 i petlja postaje beskonačna
          ans = max(ans, C[r]);
        }
      }
      return ans;
    }
    ```

Može se dokazati da je vremenska složenost gornjeg algoritma $\Theta(\log^2n)$.

??? note "Dokaz vremenske složenosti"
    Promotrimo najviši bit u kojem se $r$ i $l$ razlikuju; na tom bitu $r$ sigurno ima $1$, a $l$ ima $0$ (jer je $r \ge l$).
    
    Ako $r$ iza tog bita ima još jedinica, sigurno vrijedi $r - \operatorname{lowbit}(r) \ge l$, pa sljedeći korak sigurno pretvara najnižu jedinicu od $r$ u $0$;
    
    ako je ta jedinica od $r$ ujedno i najniža jedinica od $r$, bilo da radimo $r \gets r - \operatorname{lowbit}(r)$ ili $r \gets r - 1$, ta jedinica od $r$ sigurno postaje $0$.
    
    Dakle, nakon najviše $\log n$ transformacija od $r$ najviši bit u kojem se $r$ i $l$ razlikuju sigurno se spušta za jedan. Stoga je ukupna vremenska složenost $\Theta(\log^2n)$.

### Ažuriranje u točki

???+ note "Napomena"
    Prije učenja ovog odjeljka razumijte sljedeća dva svojstva oblika stabla Fenwickova stabla.
    
    -   Neka je $u = s \times 2^{k + 1} + 2^k$; tada $u$ ima $k = \log_2\operatorname{lowbit}(u)$ djece, s oznakama $u - 2^t(0 \le t < k)$.
    -   Intervali koje pokrivaju $c$ sve djece od $u$ točno se nadovezuju u $[l(u), u - 1]$.
    
    Značenje i dokaz tih dvaju svojstava nalaze se u odjeljku [Fenwickovo stablo i svojstva njegova oblika stabla](#fenwickovo-stablo-i-svojstva-njegova-oblika-stabla) na ovoj stranici.

Nakon ažuriranja $a[x]$ trebamo ažurirati samo one $c[y]$ za koje je $y$ predak od $x$ u obliku stabla Fenwickova stabla.

Za ekstreme (na primjeru maksimuma) česta je pogrešna ideja: ako $a[x]$ mijenjamo u $p$, sve $c[y]$ ažuriramo na $\max(c[y], p)$. Evo protuprimjera: u $(1, 2, 3, 4, 5)$ promijenimo $5$ u $4$; maksimum je $4$, ali gornjom izmjenom dobili bismo $5$. Pogrešno je i izravno postaviti $c[y]$ na $p$; protuprimjer je promjena $3$ u $4$ u gornjem primjeru.

Zapravo za neinvertibilne informacije ne postoji način da se $c[y]$ izravno izmijeni pomoću $p$. Razlog je taj što je izmjena zapravo „uklanjanje” starog broja iz intervala i dodavanje novog. Utjecaj „uklanjanja” na informaciju intervala odgovara „inverznoj operaciji”, a neinvertibilne informacije nemaju „inverznu operaciju”, pa se $c[y]$ ne može izravno izmijeniti.

Drugim riječima, za svaki pogođeni $c[y]$ informaciju tog intervala svakako moramo ponovno izgraditi.

Promotrimo djecu od $c[y]$: njihove su informacije sigurno ispravne (jer najprije ažuriramo djecu pa onda roditelja), a ta djeca upravo tvore pokriveni interval $[l(y), y - 1]$; dodamo li još točku $a[y]$, dobivamo $[l(y), y]$, tj. $c[y]$. Tako svaki $c$ koji treba izmijeniti možemo ponovno izgraditi spajanjem najviše $\log n$ intervala.

???+ note "Implementacija"
    ```cpp
    void update(int x, int v) {
      a[x] = v;
      for (int i = x; i <= n; i += lowbit(i)) {
        // prolazimo pogođene intervale
        C[i] = a[i];
        for (int j = 1; j < lowbit(i); j *= 2) {
          C[i] = max(C[i], C[i - j]);
        }
      }
    }
    ```

Lako je vidjeti da je vremenska složenost gornjeg algoritma $\Theta(\log^2n)$.

### Izgradnja stabla

Može se rastaviti na $n$ izmjena u točki, izgradnja u $\Theta(n\log^2n)$.

Postoji i izgradnja u $\Theta(n)$; vidi prvi način u odjeljku [$\Theta(n)$ izgradnja stabla](#thetan-izgradnja-stabla) na ovoj stranici.

## Trikovi

### $\Theta(n)$ izgradnja stabla

Na primjeru održavanja zbroja intervala.

Prvi način:

Vrijednost svakog vrha dobiva se zbrajanjem vrijednosti sve djece koja su s njim izravno povezana. Zato doprinose možemo razmatrati obrnuto: svaki put kad je vrijednost djece utvrđena, vlastitom vrijednošću ažuriramo svog neposrednog roditelja.

???+ note "Implementacija"
    === "C++"
        ```cpp
        // izgradnja stabla u Θ(n)
        void init() {
          for (int i = 1; i <= n; ++i) {
            t[i] += a[i];
            int j = i + lowbit(i);
            if (j <= n) t[j] += t[i];
          }
        }
        ```
    
    === "Python"
        ```python
        # izgradnja stabla u Θ(n)
        def init():
            for i in range(1, n + 1):
                t[i] = t[i] + a[i]
                j = i + lowbit(i)
                if j <= n:
                    t[j] = t[j] + t[i]
        ```

Drugi način:

Već smo rekli da $c[i]$ predstavlja interval $[i-\operatorname{lowbit}(i)+1, i]$; zato možemo najprije predobraditi niz prefiksnih zbrojeva $\mathrm{sum}$, a zatim izračunati niz $c$.

???+ note "Implementacija"
    === "C++"
        ```cpp
        // izgradnja stabla u Θ(n)
        void init() {
          for (int i = 1; i <= n; ++i) {
            t[i] = sum[i] - sum[i - lowbit(i)];
          }
        }
        ```
    
    === "Python"
        ```python
        # izgradnja stabla u Θ(n)
        def init():
            for i in range(1, n + 1):
                t[i] = sum[i] - sum[i - lowbit(i)]
        ```

### Optimizacija vremenskim žigom

Vrlo čest trik za zadatke s više testnih skupova. Ako bismo pri svakom novom skupu podataka grubo praznili Fenwickovo stablo, mogli bismo premašiti vremensko ograničenje. Zato koristimo oznaku $\mathrm{tag}$ koja pamti kad je vrh zadnji put korišten (tj. u kojem je skupu podataka zadnji put upotrijebljen). Pri svakoj operaciji usporedimo vrijeme u $\mathrm{tag}$ tog položaja s trenutnim vremenom i tako odredimo treba li taj položaj biti $0$ ili vrijednost iz niza.

???+ note "Implementacija"
    === "C++"
        ```cpp
        // optimizacija vremenskim žigom
        int tag[MAXN], t[MAXN], Tag;
        
        void reset() { ++Tag; }
        
        void add(int k, int v) {
          while (k <= n) {
            if (tag[k] != Tag) t[k] = 0;
            t[k] += v, tag[k] = Tag;
            k += lowbit(k);
          }
        }
        
        int getsum(int k) {
          int ret = 0;
          while (k) {
            if (tag[k] == Tag) ret += t[k];
            k -= lowbit(k);
          }
          return ret;
        }
        ```
    
    === "Python"
        ```python
        # optimizacija vremenskim žigom
        tag = [0] * MAXN
        t = [0] * MAXN
        Tag = 0
        
        
        def reset():
            Tag = Tag + 1
        
        
        def add(k, v):
            while k <= n:
                if tag[k] != Tag:
                    t[k] = 0
                t[k] = t[k] + v
                tag[k] = Tag
                k = k + lowbit(k)
        
        
        def getsum(k):
            ret = 0
            while k:
                if tag[k] == Tag:
                    ret = ret + t[k]
                k = k - lowbit(k)
            return ret
        ```

## Primjeri zadataka

-   [Fenwickovo stablo 1: izmjena u točki, upit na intervalu](https://loj.ac/problem/130)
-   [Fenwickovo stablo 2: izmjena na intervalu, upit u točki](https://loj.ac/problem/131)
-   [Fenwickovo stablo 3: izmjena na intervalu, upit na intervalu](https://loj.ac/problem/132)
-   [Dvodimenzionalno Fenwickovo stablo 1: izmjena u točki, upit na intervalu](https://loj.ac/problem/133)
-   [Dvodimenzionalno Fenwickovo stablo 2: izmjena na intervalu, upit u točki](https://loj.ac/problem/134)
-   [Dvodimenzionalno Fenwickovo stablo 3: izmjena na intervalu, upit na intervalu](https://loj.ac/problem/135)
