---
title: Union-find (DSU)
---

![](images/disjoint-set.svg)

## Uvod

Union-find (disjoint set union, DSU) struktura je podataka za upravljanje pripadnošću elemenata skupovima; implementira se kao šuma u kojoj svako stablo predstavlja jedan skup, a čvorovi stabla elemente tog skupa.

Kako i ime kaže, union-find podržava dvije operacije:

-   spajanje (Unite): spaja skupove kojima pripadaju dva elementa (spaja odgovarajuća stabla);
-   upit (Find): određuje kojem skupu pripada element (nalazi korijen odgovarajućeg stabla), čime se može provjeriti pripadaju li dva elementa istom skupu.

Uz odgovarajuće izmjene union-find može podržati brisanje ili premještanje pojedinog elementa te održavanje težina bridova u stablu. Pomoću segment treea s dinamičkim stvaranjem čvorova može se implementirati i [perzistentni union-find](./persistent-seg.md#拓展基于主席树的可持久化并查集).

???+ warning "Upozorenje"
    Union-find ne može uz nisku složenost podržati razdvajanje skupova.

## Inicijalizacija

Na početku je svaki element u zasebnom skupu, predstavljenom stablom koje ima samo korijen. Radi jednostavnosti roditelja korijena postavljamo na njega samog.

???+ example "Implementacija"
    === "C++"
        ```cpp
        struct dsu {
          vector<size_t> pa;
        
          explicit dsu(size_t size) : pa(size) { iota(pa.begin(), pa.end(), 0); }
        };
        ```
    
    === "Python"
        ```python
        class Dsu:
            def __init__(self, size):
                self.pa = list(range(size))
        ```

## Upit

Krećemo se stablom prema gore dok ne nađemo korijen.

![](images/disjoint-set-find.svg)

???+ example "Implementacija"
    === "C++"
        ```cpp
        size_t dsu::find(size_t x) { return pa[x] == x ? x : find(pa[x]); }
        ```
    
    === "Python"
        ```python
        def find(self, x):
            return x if self.pa[x] == x else self.find(self.pa[x])
        ```

### Kompresija puta

Svaki element kroz koji prođemo tijekom upita pripada tom skupu, pa ga možemo izravno spojiti na korijen i tako ubrzati kasnije upite.

![](images/disjoint-set-compress.svg)

???+ example "Implementacija"
    === "C++"
        ```cpp
        size_t dsu::find(size_t x) { return pa[x] == x ? x : pa[x] = find(pa[x]); }
        ```
    
    === "Python"
        ```python
        def find(self, x):
            if self.pa[x] != x:
                self.pa[x] = self.find(self.pa[x])
            return self.pa[x]
        ```

## Spajanje

Da bismo spojili dva stabla, dovoljno je korijen jednog stabla spojiti na korijen drugoga.

![](images/disjoint-set-merge.svg)

???+ example "Implementacija"
    === "C++"
        ```cpp
        void dsu::unite(size_t x, size_t y) { pa[find(x)] = find(y); }
        ```
    
    === "Python"
        ```python
        def unite(self, x, y):
            self.pa[self.find(x)] = self.find(y)
        ```

### Heurističko spajanje

Pri spajanju izbor korijena koji postaje korijen novog stabla utječe na složenost budućih operacija. Stablo s manje čvorova ili manjom dubinom možemo spojiti na drugo kako bismo izbjegli degeneraciju.

??? note "Detaljnija rasprava o složenosti"
    Budući da trebamo podržati samo spajanje skupova i upite, kad dva skupa spajamo u jedan, dobit ćemo ispravan rezultat bez obzira na to koji skup spojimo ispod kojega. Različiti načini spajanja ipak se razlikuju po vremenskoj složenosti. Konkretno, ako stablo skupa s manje čvorova i manjom dubinom spojimo ispod većeg stabla, očito će kasnije operacije pretraživanja trajati kraće nego pri obrnutom načinu spajanja (a dobivamo i bolju složenost najgoreg slučaja).
    
    Naravno, ne nailazimo uvijek na skupove koji su točno kao gore opisani – s manje čvorova i manjom dubinom. Budući da se i broj čvorova i dubina lako održavaju, obično biramo jedno od toga kao funkciju procjene. Bez obzira na izbor, vremenska je složenost $O (m\alpha(m,n))$; konkretan dokaz može se naći u radovima navedenim u literaturi.
    
    U stvarnom kodu na natjecanjima kôd često prolazi u zadanom vremenu i bez heurističkog spajanja. U Tarjanovu radu[^tarjan1984worst] dokazano je da je, bez heurističkog spajanja i samo s kompresijom puta, složenost najgoreg slučaja $O (m \log n)$. U radu Andrewa Yaoa[^yao1985expected] dokazano je da je, bez heurističkog spajanja i samo s kompresijom puta, prosječna složenost i dalje $O (m\alpha(m,n))$.
    
    Ako se koristi samo heurističko spajanje bez kompresije puta, vremenska je složenost $O(m\log n)$. Budući da jedna kompresija puta može izazvati velik broj izmjena, kompresija puta katkad nije prikladna. Primjerice, u perzistentnom union-findu i u kombinaciji „podjela segment treea po vremenu + union-find” obično se koristi union-find samo s heurističkim spajanjem.

Referentna implementacija spajanja po broju čvorova (uočite da treba prilagoditi inicijalizaciju):

???+ example "Implementacija"
    === "C++"
        ```cpp
        struct dsu {
          vector<size_t> pa, size;
        
          explicit dsu(size_t size_) : pa(size_), size(size_, 1) {
            iota(pa.begin(), pa.end(), 0);
          }
        
          void unite(size_t x, size_t y) {
            x = find(x), y = find(y);
            if (x == y) return;
            if (size[x] < size[y]) swap(x, y);
            pa[y] = x;
            size[x] += size[y];
          }
        };
        ```
    
    === "Python"
        ```python
        class Dsu:
            def __init__(self, size):
                self.pa = list(range(size))
                self.size = [1] * size
        
            def unite(self, x, y):
                x, y = self.find(x), self.find(y)
                if x == y:
                    return
                if self.size[x] < self.size[y]:
                    x, y = y, x
                self.pa[y] = x
                self.size[x] += self.size[y]
        ```

## Referentna implementacija

Potpuna implementacija union-finda s kompresijom puta i spajanjem po broju čvorova izgleda ovako:

??? example "Referentna implementacija za zadatak-predložak [Luogu P3367 „Predložak” Union-find](https://www.luogu.com.cn/problem/P3367)"
    === "C++"
        ```cpp
        --8<-- "docs/ds/code/dsu/dsu_0.cpp"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/ds/code/dsu/dsu_0.py"
        ```

## Složenost

Uz istodobnu kompresiju puta i heurističko spajanje prosječno vrijeme svake operacije union-finda iznosi samo $O(\alpha(n))$. Pritom je $\alpha$ inverz Ackermannove funkcije, koji raste iznimno sporo. Drugim riječima, prosječno vrijeme izvođenja jedne operacije union-finda može se smatrati vrlo malom konstantom. Dokaz vremenske složenosti nalazi se na [ovoj stranici](./dsu-complexity.md).

???+ info "Inverzna Ackermannova funkcija"
    [Ackermannova funkcija](https://en.wikipedia.org/wiki/Ackermann_function) $A(m, n)$ definirana je ovako:
    
    $A(m, n) = \begin{cases}n+1&\text{if }m=0\\A(m-1,1)&\text{if }m>0\text{ and }n=0\\A(m-1,A(m,n-1))&\text{otherwise}\end{cases}$
    
    Inverzna Ackermannova funkcija $\alpha(n)$ definirana je kao inverz Ackermannove funkcije, tj. kao najveći cijeli broj $m$ takav da je $A(m, m) \leqslant n$.

Prostorna složenost union-finda očito je $O(n)$.

## Proširene operacije

Na temelju običnog union-finda može se napraviti niz izmjena kako bi podržavao više operacija ili održavao složenije informacije.

### Union-find s brisanjem

Obični union-find ne podržava brisanje zato što bi brisanje čvora neizbježno izbrisalo sve čvorove podstabla kojem je on korijen. Da bi se taj problem riješio, u union-findu s brisanjem uvođenjem virtualnih čvorova osiguravamo da su svi čvorovi koji stvarno pohranjuju podatke uvijek listovi. Zato pri inicijalizaciji za svaki podatkovni čvor stvorimo virtualni čvor i roditelja podatkovnog čvora postavimo na taj virtualni čvor. Budući da se pri svakom spajanju dvaju skupova spajaju samo korijeni dvaju stabala, od početka do kraja samo virtualni čvorovi imaju djecu. Time je zajamčeno da pri brisanju čvora nećemo greškom izbrisati druge čvorove.

Napomena: nakon brisanja pojedinog čvora za njega treba ponovno stvoriti virtualni čvor kao roditelja; inače se kasnija spajanja i brisanja ne mogu ispravno izvesti.

??? example "Referentna implementacija za zadatak-predložak [SPOJ JMFILTER - Junk-Mail Filter](https://www.spoj.com/problems/JMFILTER/)"
    === "C++"
        ```cpp
        --8<-- "docs/ds/code/dsu/dsu_4.cpp"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/ds/code/dsu/dsu_4.py"
        ```

Sličnom se metodom može implementirati i premještanje pojedinog elementa između skupova. Detalji implementacije nalaze se u primjerima zadataka.

### Težinski union-find

Na bridovima union-finda možemo definirati i neku težinu te operaciju koja se nad tom težinom izvodi pri kompresiji puta, čime rješavamo više problema. Primjerice, za klasični zadatak „NOI2001” Hranidbeni lanac na težinama bridova možemo održavati aditivnu grupu modulo $3$. Za takve zadatke, u kojima se održavaju težine bridova modulo mali modul, moguće je i svaki čvor union-finda rastaviti na više stanja. Ta se tehnika za ovaj posebni slučaj naziva i „union-find po vrstama” ili „union-find s proširenom domenom”. Ti su pristupi objašnjeni u nastavku na primjerima zadataka.

Da bi se održavale težine bridova u union-findu, težinu brida spuštamo i pohranjujemo u dijete. Dakle, svaki čvor pohranjuje težinu brida između sebe i svojeg roditelja. Težinu treba prilagoditi samo kad se promijeni roditelj čvora. U općem slučaju to se događa pri kompresiji puta i pri spajanju dvaju čvorova. Primjerice, ako je težina brida udaljenost između trenutačnog čvora i njegova roditelja, tada pri kompresiji puta, svaki put kad roditelja trenutačnog čvora zamijenimo korijenom, težini pohranjenoj u trenutačnom čvoru treba dodati udaljenost od roditelja do korijena; slično, pri spajanju skupova dvaju čvorova treba izračunati težinu novog brida između dvaju korijena.

??? example "Referentna implementacija za zadatak-predložak [Library Checker - Unionfind with Potential](https://judge.yosupo.jp/problem/unionfind_with_potential)"
    === "C++"
        ```cpp
        --8<-- "docs/ds/code/dsu/dsu_5.cpp"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/ds/code/dsu/dsu_5.py"
        ```

## Primjeri zadataka

Na algoritamskim natjecanjima zadaci koji izravno ispituju union-find većinom zahtijevaju posebnu strukturu prilagođenu zadatku.

???+ example "[UVa11987 Almost Union-Find](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=229&page=show_problem&problem=3138)"
    Implementirajte strukturu podataka nalik union-findu koja podržava sljedeće operacije:
    
    1.  spajanje skupova kojima pripadaju dva elementa;
    2.  premještanje pojedinog elementa u skup u kojem se nalazi drugi element;
    3.  upit za veličinu i zbroj elemenata skupa kojem pripada element.

??? note "Rješenje"
    U ovom su zadatku operacije 1 i 3 jednostavne; teškoća je u operaciji 2. Pretpostavimo da element $x$ treba premjestiti u skup u kojem je element $y$. U običnom union-findu ne možemo jednostavno roditelja elementa $x$ postaviti na korijen skupa elementa $y$, jer bismo tako premjestili i sve elemente podstabla elementa $x$. Rješenje je osigurati da element $x$ nema djece. Zato pri izgradnji union-finda za svaki element $x$ stvorimo virtualni čvor $\tilde x$ i roditelja elementa $x$ usmjerimo na odgovarajući virtualni čvor $\tilde x$. Tako se pri spajanju dvaju skupova uvijek jedan korijen spaja na drugi, a korijeni su svi virtualni čvorovi, pa samo virtualni čvorovi imaju djecu, dok nijedan čvor koji stvarno pohranjuje element nema djece. Tada je premještanje elementa znatno jednostavnije implementirati.

??? note "Referentna implementacija"
    === "C++"
        ```cpp
        --8<-- "docs/ds/code/dsu/dsu_1.cpp"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/ds/code/dsu/dsu_1.py"
        ```

???+ example "[Luogu P2024 „NOI2011” Hranidbeni lanac](https://www.luogu.com.cn/problem/P2024)"
    U životinjskom kraljevstvu postoje tri vrste životinja $A,B,C$ čiji hranidbeni lanac tvori zanimljiv krug: $A$ jede $B$, $B$ jede $C$, $C$ jede $A$.
    
    Ima $N$ životinja označenih brojevima $1 \sim N$. Svaka je životinja jedne od vrsta $A,B,C$, ali ne znamo koje.
    
    Netko odnose u hranidbenom lancu tih $N$ životinja opisuje tvrdnjama dviju vrsta:
    
    -   tvrdnja `1 X Y` znači da su $X$ i $Y$ iste vrste;
    -   tvrdnja `2 X Y` znači da $X$ jede $Y$.
    
    Ta osoba o $N$ životinja, koristeći navedene dvije vrste tvrdnji, redom izgovara $K$ tvrdnji, od kojih su neke istinite, a neke lažne. Tvrdnja je lažna ako zadovoljava bilo koji od sljedećih triju uvjeta, a inače je istinita:
    
    -   tvrdnja je u sukobu s nekom prethodnom istinitom tvrdnjom;
    -   $X$ ili $Y$ u tvrdnji veći je od $N$;
    -   tvrdnja kaže da $X$ jede $X$.
    
    Vaš je zadatak da za zadani $N$ i $K$ tvrdnji ispišete ukupan broj lažnih tvrdnji.

??? note "Rješenje 1"
    Informacije o hranidbenom lancu održavamo težinskim union-findom. Ako su $x$ i $y$ iste vrste, vrijedi $x\equiv y\pmod 3$; ako $x$ jede $y$, vrijedi $x - y \equiv 1 \pmod 3$. Time se zadatak svodi na gore navedeni zadatak-predložak.
    
    Konkretno, za svaku tvrdnju, osim očito lažnih s $x>n$ ili $y>n$, treba provjeriti jesu li $x$ i $y$ već povezani: ako jesu, izračunamo njihovu udaljenost modulo 3 i usporedimo je s onim što tvrdnja kaže; inače ih povežemo prema informaciji iz tvrdnje. Osim očitih slučajeva, tvrdnja je lažna ako i samo ako su spomenuta dva čvora već povezana i odgovarajuća udaljenost proturječi tvrdnji.

??? note "Referentna implementacija 1"
    === "C++"
        ```cpp
        --8<-- "docs/ds/code/dsu/dsu_6.cpp"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/ds/code/dsu/dsu_6.py"
        ```

??? note "Rješenje 2"
    Svaku životinju $x$ rastavimo na tri stanja. U implementaciji različita stanja možemo izravno tretirati kao različite elemente:
    
    -   stanja u istom skupu kao $x$ pripadaju istoj vrsti kao $x$;
    -   stanja u istom skupu kao $x+n$ može jesti $x$;
    -   stanja u istom skupu kao $x+2n$ mogu jesti $x$.
    
    Tada za tvrdnju vrijedi:
    
    -   `1 x y` lažna je ako i samo ako:
    
        1.  $x>N$ ili $y>N$;
        2.  $y$ je u istom skupu kao $x+n$ ili $x+2n$.
    -   `2 x y` lažna je ako i samo ako:
    
        1.  $x>N$ ili $y>N$;
        2.  $y$ je u istom skupu kao $x$ ili $x+2n$.
    -   Ako je tvrdnja istinita, spojimo odgovarajuća stanja.

??? note "Referentna implementacija 2"
    === "C++"
        ```cpp
        --8<-- "docs/ds/code/dsu/dsu_2.cpp"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/ds/code/dsu/dsu_2.py"
        ```

???+ example "[ABC396E Min of Restricted Sum](https://atcoder.jp/contests/abc396/tasks/abc396_e)"
    Zadani su cijeli brojevi $N, M$ i cjelobrojni nizovi duljine $M$: $X=(X_1,X_2,\ldots,X_M)$, $Y=(Y_1,Y_2,\ldots,Y_M)$, $Z=(Z_1,Z_2,\ldots,Z_M)$. Zajamčeno je da su svi elementi nizova $X$ i $Y$ u rasponu od $1$ do $N$.
    
    Niz nenegativnih cijelih brojeva $A=(A_1,A_2,\ldots,A_N)$ duljine $N$ zovemo **dobrim nizom** ako i samo ako zadovoljava sljedeći uvjet:
    
    -   za svaki cijeli broj $i$ takav da je $1 \leq i \leq M$ vrijedi $A_{X_i} \oplus A_{Y_i} = Z_i$, gdje $\oplus$ označava operaciju XOR.
    
    Odredite postoji li takav dobar niz. Ako postoji, pronađite dobar niz s najmanjim zbrojem elemenata $\displaystyle \sum_{i=1}^N A_i$ i ispišite ga.

??? note "Rješenje"
    XOR je zapravo odnos „jednako” ili „različito” na pojedinom binarnom bitu. Ako sve bitove brojeva $A_i$ razdvojimo, XOR-odnose možemo održavati težinskim union-findom (ili union-findom po vrstama). Elementi iste komponente povezanosti nužno odgovaraju istom bitu različitih brojeva iz $A$. Pri računanju odgovora elementi iste komponente obično se dijele u dvije skupine koje moraju imati različite vrijednosti; većoj skupini dodijelimo $0$, a drugoj $1$, čime je ukupna težina zajamčeno najmanja.

??? note "Referentna implementacija"
    === "C++"
        ```cpp
        --8<-- "docs/ds/code/dsu/dsu_3.cpp"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/ds/code/dsu/dsu_3.py"
        ```

## Zadaci za vježbu

-   [„NOI2015” Automatska analiza programa](https://uoj.ac/problem/127)
-   [„JSOI2008” Ratovi zvijezda](https://www.luogu.com.cn/problem/P1197)
-   [„NOIP2023” Trovaljana logika](https://www.luogu.com.cn/problem/P9869)
-   [„NOI2002” Legenda o galaktičkim herojima](https://www.luogu.com.cn/problem/P1196)

## Ostale primjene

Kruskalov algoritam u [algoritmima za minimalno razapinjuće stablo](../graph/mst.md) i Tarjanov algoritam za [najnižeg zajedničkog pretka](../graph/lca.md) algoritmi su koji se temelje na union-findu.

Povezana tema: [primjene union-finda](../topic/dsu-app.md).

## Literatura i dodatno čitanje

1.  [Odgovor na Zhihuu: Postoji li u union-findu doista optimizacija kompresije puta prepolavljanjem?](https://www.zhihu.com/question/28410263/answer/40966441)
2.  Gabow, H. N., & Tarjan, R. E. (1985). A Linear-Time Algorithm for a Special Case of Disjoint Set Union. JOURNAL OF COMPUTER AND SYSTEM SCIENCES, 30, 209-221.[PDF](https://dl.acm.org/doi/pdf/10.1145/800061.808753)
3.  [CSDN: Union-find s proširenom domenom i težinski union-find](https://blog.csdn.net/qqqqqwerttwtwe/article/details/145440100)

[^tarjan1984worst]: Tarjan, R. E., & Van Leeuwen, J. (1984). Worst-case analysis of set union algorithms. Journal of the ACM (JACM), 31(2), 245-281.[ResearchGate PDF](https://www.researchgate.net/profile/Jan_Van_Leeuwen2/publication/220430653_Worst-case_Analysis_of_Set_Union_Algorithms/links/0a85e53cd28bfdf5eb000000/Worst-case-Analysis-of-Set-Union-Algorithms.pdf)

[^yao1985expected]: Yao, A. C. (1985). On the expected performance of path compression algorithms.[SIAM Journal on Computing, 14(1), 129-133.](https://epubs.siam.org/doi/abs/10.1137/0214010?journalCode=smjcat)
