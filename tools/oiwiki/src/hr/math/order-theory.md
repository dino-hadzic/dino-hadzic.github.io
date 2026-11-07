---
title: Teorija uređaja
---

## Uvod

Teorija uređaja (order theory) grana je matematike koja pomoću binarnih relacija strogo formalizira pojam „poretka”. U nastavku uvodimo osnovne definicije te grane.

## Definicije

### Binarna relacija

???+ note "Definicija"
    **Binarna relacija** (binary relation) $R$ na skupovima $X$ i $Y$ definira se kao uređena trojka $(X,Y,G(R))$, gdje se $X$ naziva domena (domain), $Y$ kodomena (codomain), a $G(R)\subseteq X\times Y=\{(x,y):x\in X,y\in Y\}$ graf (graph) binarne relacije $R$. $xRy$ vrijedi ako i samo ako $(x,y)\in G(R)$.
    
    Ako je $X=Y$, binarnu relaciju nazivamo homogenom binarnom relacijom (homogeneous relation) ili endorelacijom (endorelation).
    
    Ako nije drukčije rečeno, sve binarne relacije u nastavku su homogene.

Na primjer, djeljivost $\mid$ i relacija „manje ili jednako” $\leq$ na $\mathbf{N}_+$ binarne su relacije.

Kad proučavamo binarne relacije, često nas zanima imaju li neka posebna svojstva. Za binarnu relaciju $R$ na skupu $S$ definiramo sljedeća posebna svojstva:

1.  refleksivnost (reflexive): $(\forall~a \in S)~~aRa$,
2.  irefleksivnost (irreflexive, anti-reflexive): $(\forall~a \in S)~~\lnot(aRa)$,
3.  simetričnost (symmetric): $(\forall~a,b \in S)~~aRb \iff bRa$,
4.  antisimetričnost (antisymmetric): $(\forall~a,b \in S)~~(aRb \land bRa) \implies a=b$,
5.  asimetričnost (asymmetric): $(\forall~a,b \in S)~~aRb \implies \lnot(bRa)$,
6.  tranzitivnost (transitive): $(\forall~a,b,c \in S)~~(aRb \land bRc) \implies aRc$,
7.  povezanost (connected): $(\forall~a,b \in S)~~a \neq b \implies (aRb \lor bRa)$,
8.  dobra utemeljenost (well-founded): $(\exists~m \in S \neq \varnothing)~~(\forall~a \in S\setminus\{m\})~~\lnot(aRm)$ (tj. neprazan skup $S$ ima minimalni element $m$),
9.  tranzitivnost neusporedivosti (transitive of incomparability): $(\forall~a,b,c \in S)~~(\lnot(aRb \lor bRa) \land \lnot(bRc \lor cRb)) \implies \lnot(aRc \lor cRa)$ (ako vrijedi $\lnot(aRb \lor bRa)$, kažemo da su $a$ i $b$ neusporedivi).

Ujedno definiramo neke posebne binarne relacije:

| Binarna relacija                       | Refleksivnost | Irefleksivnost | Simetričnost | Antisimetričnost | Asimetričnost | Tranzitivnost | Povezanost | Dobra utemeljenost | Tranzitivnost neusporedivosti |
| -------------------------------------- | ------------- | -------------- | ------------ | ---------------- | ------------- | ------------- | ---------- | ------------------ | ----------------------------- |
| relacija ekvivalencije (equivalence relation) | da     |                | da           |                  |               | da            |            |                    |                               |
| preduređaj (preorder, quasiorder)      | da            |                |              |                  |               | da            |            |                    |                               |
| parcijalni uređaj (partial order)      | da            |                |              | da               |               | da            |            |                    |                               |
| totalni uređaj (total order)           | da            |                |              | da               |               | da            | da         |                    |                               |
| dobri uređaj (well-order)              | da            |                |              | da               |               | da            | da         | da                 |                               |
| strogi preduređaj (strict preorder)    |               | da             |              |                  |               | da            |            |                    |                               |
| strogi parcijalni uređaj (strict partial order) |      | da             |              |                  | da            | da            |            |                    |                               |
| strogi slabi uređaj (strict weak order) |              | da             |              |                  | da            | da            |            |                    | da                            |
| strogi totalni uređaj (strict total order) |           | da             |              |                  | da            | da            | da         |                    |                               |

### Operacije s relacijama

Za binarne relacije $R$ i $S$ na skupovima $X$ i $Y$ možemo definirati sljedeće operacije:

1.  unija $R\cup S$ relacija $R$ i $S$ zadovoljava $G(R\cup S):=\{(x,y):xRy \lor xSy\}$ (npr. $\leq$ je unija relacija $<$ i $=$),
2.  presjek $R\cap S$ relacija $R$ i $S$ zadovoljava $G(R\cap S):=\{(x,y):xRy \land xSy\}$,
3.  komplement $\bar{R}$ relacije $R$ zadovoljava $G(\bar{R}):=\{(x,y):\lnot(xRy)\}$,
4.  dualna (inverzna) relacija $R^T$ relacije $R$ zadovoljava $G(R^T):=\{(y,x):xRy\}$.

Za binarnu relaciju $R$ na skupovima $X$ i $Y$ te binarnu relaciju $S$ na skupovima $Y$ i $Z$ možemo definirati njihovu kompoziciju $S\circ R$ koja zadovoljava $G(S\circ R):=\{(x,z):(\exists~y\in Y)~~xRy\land ySz\}$.

### Parcijalno uređen skup

???+ note "Definicija"
    Ako binarna relacija $\preceq$ na skupu $S$ ima svojstva **refleksivnosti**, **antisimetričnosti** i **tranzitivnosti**, kažemo da je $S$ **parcijalno uređen skup** (partially ordered set, poset), a $\preceq$ **parcijalni uređaj** (partial order) na njemu.
    
    Ako parcijalni uređaj $\preceq$ ima još i svojstvo **povezanosti**, nazivamo ga **totalnim uređajem** (total order), a pripadni skup **totalno uređenim skupom** (totally ordered set), **linearno uređenim skupom** (linearly ordered set, loset) ili **jednostavno uređenim skupom** (simply ordered set).

Lako se vidi da su $\mathbf{N}$, $\mathbf{Z}$, $\mathbf{Q}$ i $\mathbf{R}$ totalno uređeni skupovi s obzirom na $\leq$.

### Vizualizacija parcijalno uređenog skupa: Hasseov dijagram

Za konačne parcijalno uređene skupove parcijalni uređaj možemo zorno prikazati Hasseovim dijagramom.

???+ note "Definicija"
    Za konačan parcijalno uređen skup $S$ i parcijalni uređaj $\preceq$ na njemu definiramo $x\prec y\iff (x\preceq y\land x\neq y)$; pripadni **Hasseov dijagram** jest graf $G=\langle V,E\rangle$ koji zadovoljava sljedeće uvjete:
    
    -   $V=S$,
    -   $E=\{(x,y)\in S\times S: x\prec y \land ((\nexists~z\in S)~~x\prec z\prec y)\}$

Na primjer, za partitivni skup $S$ skupa $\{0,1,2\}$ i relaciju inkluzije skupova $\subseteq$ pripadni Hasseov dijagram jest:

![](images/order-theory1.svg)

Budući da je parcijalni uređaj antisimetričan, Hasseov dijagram nužno je [usmjereni aciklički graf](../graph/dag.md), pa pomoću [topološkog sortiranja](../graph/topo.md) za svaki konačan parcijalno uređen skup možemo konstruirati totalni uređaj.

### Lanci i antilanci

???+ note "Definicija"
    Za parcijalno uređen skup $S$ i parcijalni uređaj $\preceq$ na njemu, totalno uređen podskup skupa $S$ nazivamo **lancem** (chain). Ako su u podskupu $T$ skupa $S$ svaka dva različita elementa neusporediva (tj. $(\forall~a,b \in T)~~a \neq b \implies (a \npreceq b \land b \npreceq a)$), $T$ nazivamo **antilancem** (antichain).
    
    Za parcijalno uređen skup $S$ i parcijalni uređaj $\preceq$ na njemu, duljinu najduljeg antilanca parcijalno uređenog skupa $S$ nazivamo **širinom** (partial order width).

Na primjer, za partitivni skup $S$ skupa $\{0,1,2\}$ i relaciju inkluzije skupova $\subseteq$, $\{\varnothing,\{1\},\{1,2\}\}$ je lanac, $\{\{1\},\{0,2\}\}$ je antilanac, a širina skupa $S$ iznosi $3$.

### Posebni elementi preduređenih skupova

U preduređenim skupovima možemo definirati pojmove maksimalnog (minimalnog) elementa, gornje (donje) međe, supremuma (infimuma) itd.; ti se pojmovi mogu poopćiti i na druge relacije uređaja.

???+ note "Definicija"
    Za preduređen skup $S$ i preduređaj $\preceq$ na njemu uzmimo element $m$ skupa $S$:
    
    1.  ako vrijedi $(\forall~a \in S\setminus\{m\})~~\lnot(m\preceq a)$, $m$ nazivamo **maksimalnim elementom** (maximal element),
    2.  ako za $T \subseteq S$ vrijedi $(\forall~t\in T)~~t\preceq m$, $m$ nazivamo **gornjom međom** (upper bound) skupa $T$,
    3.  ako za $T \subseteq S$ vrijedi da je $m$ gornja međa skupa $T$ i da za svaku gornju među $n$ skupa $T$ vrijedi $m \preceq n$, $m$ nazivamo **supremumom** (supremum) skupa $T$.
    
    Analogno se definiraju **minimalni element** (minimal element), **donja međa** (lower bound) i **infimum** (infimum).

Na primjer, $1$ je minimalni element i donja međa skupa $\mathbf{N}_+$.

Može se dokazati:

-   U preduređenom skupu maksimalni (minimalni) element, gornja (donja) međa i supremum (infimum) ne moraju postojati, a i kad postoje, ne moraju biti jedinstveni.

-   Ako podskup $T$ parcijalno uređenog skupa $S$ ima supremum (infimum), on je nužno jedinstven.

    Supremum i infimum skupa $T$ označavamo redom $\sup T$ i $\inf T$. Ako parcijalno uređen skup $S$ ima i gornju i donju među, kažemo da je $S$ omeđen.

U beskonačnom parcijalno uređenom skupu maksimalni element ne mora postojati. Postoji li maksimalni element u beskonačnom parcijalno uređenom skupu, može se utvrditi pomoću **Zornove leme** (Zorn's Lemma).

???+ note "[Zornova lema](https://en.wikipedia.org/wiki/Zorn%27s_lemma)"
    **Zornova lema**, poznata i kao **Kuratowski–Zornova lema**, glasi: ako svaki lanac nepraznog parcijalno uređenog skupa ima gornju među, taj parcijalno uređen skup ima maksimalni element.

Zornova lema ekvivalentna je **[aksiomu izbora](https://en.wikipedia.org/wiki/Axiom_of_choice)**, **[teoremu o dobrom uređaju](https://en.wikipedia.org/wiki/Well-ordering_theorem)** itd.

### Usmjereni skupovi i rešetke

Znamo da je supremum (infimum) podskupa parcijalno uređenog skupa, ako postoji, nužno jedinstven. No to ne vrijedi za maksimalne (minimalne) elemente. Na primjer, promotrimo parcijalno uređen skup $S=\{\{0\},\{1\},\{2\},\{0,1\},\{0,2\},\{1,2\}\}$ s parcijalnim uređajem $\subseteq$; lako se vidi da on ima $3$ maksimalna i $3$ minimalna elementa.

Želimo parcijalno uređenom skupu dodati određene uvjete tako da maksimalni (minimalni) element, ako postoji, bude jedinstven; tada možemo definirati pojam najvećeg (najmanjeg) elementa.

???+ note "Usmjereni skup"
    Za preduređen skup $S$ i preduređaj $\preceq$ na njemu, ako vrijedi $(\forall~a,b\in S)~~(\exists~c\in S)~~a\preceq c\land b\preceq c$, $\preceq$ nazivamo **smjerom** (direction) skupa $S$, a $S$ **usmjerenim skupom** (directed set) ili **filtriranim skupom** (filtered set).
    
    Skup $S$ koji zadovoljava gornju definiciju ponekad se naziva i **usmjerenim prema gore** (upward directed set); analogno se definira skup **usmjeren prema dolje** (downward directed set).

Usmjereni skup može se definirati i na sljedeći način:

???+ note "Ekvivalentna definicija usmjerenog skupa"
    Za preduređen skup $S$ i preduređaj $\preceq$ na njemu, ako svaki konačan podskup $T$ skupa $S$ ima gornju među, $\preceq$ nazivamo smjerom skupa $S$, a $S$ usmjerenim skupom.

Lako se vidi:

-   Ako skup usmjeren prema gore ima maksimalni element, on je nužno jedinstven. Maksimalni element skupa usmjerenog prema gore nazivamo **najvećim elementom** (greatest element).
-   Ako skup usmjeren prema dolje ima minimalni element, on je nužno jedinstven. Minimalni element skupa usmjerenog prema dolje nazivamo **najmanjim elementom** (least element).

U parcijalno uređenom skupu sa smjerom za svaka dva elementa $a,b$ skup $\{a,b\}$ ima gornju među; zamijenimo li gornju među supremumom, dobivamo definiciju gornje polurešetke.

Za parcijalno uređen skup $S$ i parcijalni uređaj $\preceq$ na njemu:

???+ note "Gornja polurešetka"
    Ako za svaka dva elementa $a,b$ skupa $S$ skup $\{a,b\}$ ima supremum $c$, $S$ nazivamo **gornjom polurešetkom** (join-semilattice, upper semilattice), a $c$ nazivamo **spojem** (join) elemenata $a$ i $b$ i označavamo $a\lor b$.

???+ note "Donja polurešetka"
    Ako za svaka dva elementa $a,b$ skupa $S$ skup $\{a,b\}$ ima infimum $c$, $S$ nazivamo **donjom polurešetkom** (meet-semilattice, lower semilattice), a $c$ nazivamo **susretom** (meet) elemenata $a$ i $b$ i označavamo $a\land b$.

???+ note "Rešetka"
    Ako je $S$ i gornja i donja polurešetka, $S$ nazivamo **rešetkom** (lattice).

Na primjer, skup pozitivnih djelitelja broja $60$, $S=\{1,2,3,4,5,6,10,12,15,20,30,60\}$, parcijalno je uređen skup s obzirom na djeljivost; za svaka dva pozitivna cijela broja $a,b$ iz njega $\operatorname{lcm}(a,b)$ je spoj elemenata $a$ i $b$, a $\gcd(a,b)$ susret elemenata $a$ i $b$, pa je $S$ rešetka.

### Dualnost

U teoriji uređaja dualnost je vrlo čest pojam; primjerice, gore spomenuti maksimalni i minimalni element su dualni, gornja i donja međa su dualne, supremum i infimum su dualni.

Za parcijalno uređen skup $P$ i parcijalni uređaj $\preceq$ na njemu definiramo njegov **dualni** (dual, opposite) parcijalno uređen skup $P^d$ koji zadovoljava: $x \preceq y$ vrijedi u $P$ ako i samo ako $y \preceq x$ vrijedi u $P^d$. Obrnemo li bridove Hasseova dijagrama skupa $P$, dobivamo Hasseov dijagram skupa $P^d$.

## Dilworthov i Mirskyjev teorem

Za konačan parcijalno uređen skup $S$ i parcijalni uređaj $\preceq$ na njemu vrijedi sljedeći par dualnih teorema:

???+ note "Dilworthov teorem"
    Širina skupa $S$ (duljina najduljeg antilanca) jednaka je najmanjem broju lanaca koji ga pokrivaju.
    
    ??? note "Dokaz"
        Provodimo matematičku indukciju. Za $|S|\leq 3$ tvrdnja očito vrijedi.
        
        Pretpostavimo da tvrdnja vrijedi za sve parcijalno uređene skupove s manje od $|S|$ elemenata i neka je širina skupa $S$ jednaka $d$. Ako su svi elementi skupa $|S|$ međusobno neusporedivi, tvrdnja očito vrijedi; inače u $S$ uzmimo lanac duljine veće od $1$ te neka je $m$ njegov najmanji, a $M$ njegov najveći element.
        
        Neka je $T=S\setminus\{m,M\}$. Ako širina skupa $T$ ne prelazi $d-1$, po pretpostavci indukcije $T$ se može pokriti s najviše $d-1$ lanaca, pa se $S$ može pokriti tim lancima i lancem $\{m,M\}$, i tvrdnja vrijedi. Inače je širina skupa $T$ također $d$; neka je $A$ najdulji antilanac u $T$.
        
        Promotrimo sljedeća dva skupa:
        
        $$
        S^+:=\{x\in S:(\exists~a\in A)~~a\preceq x\}
        $$
        
        $$
        S^-:=\{x\in S:(\exists~a\in A)~~x\preceq a\}
        $$
        
        Lako uočavamo sljedeća svojstva:
        
        -   $S^+\cup S^-=S$,
        -   $S^+\cap S^-=A$,
        -   $|S^+|<|S|$, $|S^-|<|S|$ (jer $m\notin S^+$ i $M\notin S^-$).
        
        Primijenimo li pretpostavku indukcije na $S^+$ i $S^-$, najmanji broj lanaca koji pokrivaju svaki od tih dvaju skupova jest $d$, a svaki od tih lanaca sadrži točno jedan element $a$ iz $A$. Označimo te lance redom $C_a^+$ i $C_a^-$; tada je $\{C_a^-\cup\{a\}\cup C_a^+\}_{a\in A}$ najmanji pokrivač skupa $S$ lancima, čime je tvrdnja dokazana.

???+ note "Mirskyjev teorem"
    Duljina najduljeg lanca skupa $S$ jednaka je najmanjem broju antilanaca koji ga pokrivaju.
    
    ??? note "Dokaz"
        Neka je duljina najduljeg lanca skupa $S$ jednaka $d$; tada je po definiciji najmanji broj antilanaca u pokrivaču barem $d$.
        
        Neka je $f(s)$ duljina najduljeg lanca čiji je najmanji element $s$. Uočimo da iz $f(s)=f(t)$ slijedi da su $s$ i $t$ neusporedivi, pa je $(\forall~n\in\mathbf{N})~~f^{-1}(\{n\})$ antilanac, pri čemu se $f^{-1}(\{n\}):=\{a\in S:f(a)=n\}$ naziva [razinski skup (level set)](https://en.wikipedia.org/wiki/Level_set).
        
        Stoga se lako zaključuje da je $\{f^{-1}(\{i\}):1\leq i\leq d\}$ pokrivač antilancima, pa je najmanji broj antilanaca u pokrivaču najviše $d$.

Dilworthov teorem ekvivalentan je [Hallovu teoremu o braku](../graph/graph-matching/graph-match.md#hallov-teorem).

Dilworthovim teoremom možemo dokazati sljedeći teorem:

???+ note "Erdős–Szekeresov teorem"
    Niz realnih brojeva $\{a_i\}$ s barem $rs+1$ elemenata ima ili nepadajući podniz duljine $r+1$ ili nerastući podniz duljine $s+1$.
    
    ??? note "Dokaz"
        Neka je duljina niza $n\geq rs+1$. Definirajmo parcijalno uređen skup $\{(i,a_i)\}_{i=1}^{n}$ s parcijalnim uređajem $\preceq$ zadanim ovako:
        
        $$
        (i,a_i)\preceq (j,a_j)\iff (i\leq j\land a_i\leq a_j)
        $$
        
        Pretpostavimo da širina tog parcijalno uređenog skupa ne prelazi $s$; tada se po Dilworthovu teoremu on može pokriti s najviše $s$ lanaca. Ako duljina nijednog od tih lanaca ne prelazi $r$, niz ima najviše $rs$ elemenata, što je u suprotnosti s uvjetom.

### Primjeri zadataka

???+ note "[Luogu P1020 \[NOIP1999 提高组\] 导弹拦截 (Presretanje projektila)](https://www.luogu.com.cn/problem/P1020)"
    Neka je država za obranu od neprijateljskih projektila razvila sustav za presretanje projektila. No taj sustav ima nedostatak: iako prvi hitac može dosegnuti bilo koju visinu, svaki sljedeći hitac ne može biti viši od prethodnoga. Jednog dana radar je zabilježio dolazak neprijateljskih projektila. Budući da je sustav još u pokusnoj fazi, postoji samo jedan, pa je moguće da neće moći presresti sve projektile.
    
    Zadane su visine projektila redom kojim dolaze. Izračunajte koliko najviše projektila taj sustav može presresti i koliko je najmanje takvih sustava potrebno da bi se presreli svi projektili.
    
    Za sve podatke visine projektila pozitivni su cijeli brojevi koji ne prelaze $5\times 10^4$.
    
    ??? note "Rješenje"
        Neka ima ukupno $n$ projektila i neka je visina $i$-tog projektila $h_i$. Skup $\{(i,h_i)\}_{i=1}^{n}$ parcijalno je uređen skup s parcijalnim uređajem $\preceq$ zadanim ovako:
        
        $$
        (i,h_i)\preceq(j,h_j) \iff (i\leq j \land h_i\geq h_j)
        $$
        
        Po Dilworthovu teoremu tada vrijedi: **najmanji broj nerastućih podnizova koji pokrivaju niz jednak je duljini najduljeg rastućeg podniza**. Zadatak se stoga može riješiti [postupkom složenosti $O(n\log n)$ za najdulji nepadajući podniz](../dp/basic.md#algoritam-2).
    
    ??? note "Referentni kod"
        ```cpp
        --8<-- "docs/math/code/order-theory/order-theory_1.cpp"
        ```

???+ note "[\[TJOI2015\] 组合数学 (Kombinatorika)](https://www.luogu.com.cn/problem/P3974)"
    Zadana je mreža s $n$ redaka i $m$ stupaca u čijem se svakom polju nalazi određen broj komada blaga. Svaki put krećemo iz gornjeg lijevog kuta i smijemo se kretati samo desno ili dolje; pri svakom prolasku kroz polje smijemo pokupiti najviše jedan komad blaga. Koliko je najmanje prolazaka potrebno da bi se moglo pokupiti sve blago?
    
    $1\le n \le 1000$, $1\le m \le 1000$, u svakom polju ima najviše $10^6$ komada blaga.
    
    ??? note "Rješenje"
        Zanemarimo li težine polja mreže, lako se vidi da je kretanje po mreži prema zadanim pravilima ekvivalentno kretanju po DAG-u, pa ga možemo promatrati kao Hasseov dijagram i tako konstruirati parcijalno uređen skup. Po Dilworthovu teoremu tada vrijedi: **najmanji broj lanaca koji pokrivaju DAG jednak je veličini najvećeg nezavisnog skupa vrhova**.
        
        Stoga je u ovom zadatku traženi odgovor zbroj težina najvećeg težinskog nezavisnog skupa vrhova zadane mreže.
        
        Neka je $a_{ij}$ težina polja $(i,j)$ mreže, a $f(i,j)$ odgovor za podmrežu od $(i,j)$ do $(1,m)$. Uočimo da nijedno polje nije susjedno polju gore desno od sebe, pa je jednadžba prijelaza stanja:
        
        $$
        f(i,j)=\max\{f(i-1,j),f(i,j+1),f(i-1,j+1)+a_{ij}\}
        $$
        
        Odgovor je $f(n,1)$.
    
    ??? note "Referentni kod"
        ```cpp
        --8<-- "docs/math/code/order-theory/order-theory_2.cpp"
        ```

### Zadaci za vježbu

-   [\[CTSC2008\] 祭祀 (Obred)](https://www.luogu.com.cn/problem/P4298)
-   [CodeForces 590E Birthday](https://codeforces.com/problemset/problem/590/E)

## Primjena u C++-u

Pogledajte i: [Sortiranje u standardnoj biblioteci – Osnove algoritama](../basic/stl-sort.md).

U C++ STL-u teorija uređaja primjenjuje se u [algoritmima i strukturama podataka koji zahtijevaju usporedbe](https://en.cppreference.com/w/cpp/named_req/Compare#Standard_library). U C++-u često moramo definirati vlastiti komparator, a STL [zahtijeva](https://en.cppreference.com/w/cpp/named_req/Compare) da on bude **strogi slabi uređaj**. Neka je $<$ vlastiti komparator; tada možemo definirati:

-   $x>y$ kao $y<x$;
-   $x \leq y$ kao $y \nless x$;
-   $x \geq y$ kao $x \nless y$;
-   $x=y$ kao $x \nless y\land y \nless x$.

## Literatura i dodatno štivo

1.  [Order theory - From Academic Kids](https://academickids.com/encyclopedia/index.php/Order_theory)
2.  [Binary Relation - Wikipedia](https://en.wikipedia.org/wiki/Binary_relation)
3.  [Order Theory - Wikipedia](https://en.wikipedia.org/wiki/Order_theory)
4.  [Hasse diagram - Wikipedia](https://en.wikipedia.org/wiki/Hasse_diagram)
5.  [Directed set - Wikipedia](https://en.wikipedia.org/wiki/Directed_set)
6.  [Order Theory, Lecture Notes by Mark Dean for Decision Theory](http://www.columbia.edu/~md3405/DT_Order_15.pdf)
7.  Lu Kaicheng, Lu Huaming, [《组合数学》（第 3 版）(Kombinatorika, 3. izdanje)](http://www.tup.tsinghua.edu.cn/bookscenter/book_00458101.html), 2006
8.  [List of Order Theory Topics - Wikipedia](https://en.wikipedia.org/wiki/List_of_order_theory_topics)
9.  [浅谈邻项交换排序的应用以及需要注意的问题 (O primjeni sortiranja zamjenom susjednih elemenata i na što treba paziti) by ouuan](https://ouuan.github.io/post/%E6%B5%85%E8%B0%88%E9%82%BB%E9%A1%B9%E4%BA%A4%E6%8D%A2%E6%8E%92%E5%BA%8F%E7%9A%84%E5%BA%94%E7%94%A8%E4%BB%A5%E5%8F%8A%E9%9C%80%E8%A6%81%E6%B3%A8%E6%84%8F%E7%9A%84%E9%97%AE%E9%A2%98/)
10. [One thing you should know about comparators—Strict Weak Ordering](https://codeforces.com/blog/entry/72525)
11. [Dilworth's theorem - Wikipedia](https://en.wikipedia.org/wiki/Dilworth%27s_theorem)
12. [Dilworth's Theorem | Brilliant Math & Science Wiki](https://brilliant.org/wiki/dilworths-theorem/)
13. [Hall's marriage theorem - Wikipedia](https://en.wikipedia.org/wiki/Hall's_marriage_theorem)
14. [Hall's Marriage Theorem | Brilliant Math & Science Wiki](https://brilliant.org/wiki/hall-marriage-theorem/)
15. [Dilworth 学习笔记 (Bilješke o Dilworthovu teoremu) - Selfish](https://www.luogu.com.cn/blog/Rolling-Code/dilworth)
