---
title: Sparivanje u grafovima
---

## Uvod

**Sparivanje** (matching) ili **nezavisni skup bridova** skup je bridova grafa koji nemaju zajedničkih krajeva. Algoritmi za sparivanje u grafovima često se koriste u informatičkim natjecanjima i grubo se dijele na dvije vrste: maksimalno sparivanje i sparivanje maksimalne težine. Budući da je sparivanje u [bipartitnim grafovima](../bi-graph.md) ekvivalentno problemu toka u mreži, ima dobra svojstva i razmjerno se lako obrađuje, ovdje ćemo obje vrste algoritama najprije predstaviti na bipartitnim grafovima, a zatim raspraviti algoritme za opće grafove.

## Sparivanje u grafu

Neka je $G=(V,E)$ neusmjeren graf, gdje je $V$ skup vrhova, a $E$ skup bridova. Ako skup bridova $M\subseteq E$ ne sadrži petlje i nikoja dva brida nemaju zajednički vrh, skup bridova $M$ zove se **sparivanje** (matching) ili **nezavisni skup bridova** (independent edge set) grafa $G$. Brid $e\in E$ koji se pojavljuje u sparivanju $M$ zove se **spareni brid**, a inače **nespareni brid**. Analogno, vrh $v\in V$ koji je kraj nekog sparenog brida zove se **spareni vrh**, a inače **nespareni vrh**.

Veličina sparivanja $M$ broj je bridova koje sadrži. Za sparivanja u (težinskim) neusmjerenim grafovima često se razmatraju sljedeći pojmovi:

-   **Maksimalno sparivanje po inkluziji** (maximal matching): sparivanje kojemu se ne može dodati nijedan spareni brid. Ono ne mora biti sparivanje najveće veličine.

    ![maximal matching](images/graph-match-1.svg)

-   **Najveće sparivanje** (maximum matching ili maximum cardinality matching): sparivanje s najviše sparenih bridova. Može ih biti više, ali je broj bridova najvećeg sparivanja određen i ne može premašiti polovicu broja vrhova grafa.

    ![maximum cardinality matching](images/graph-match-2.svg)

-   **Sparivanje maksimalne težine** (maximum weight matching): u težinskom grafu, sparivanje s najvećim zbrojem težina bridova.

    ![maximum weight matching](images/graph-match-3.svg)

-   **Najveće sparivanje maksimalne težine** (maximum weight maximum cardinality matching): uz uvjet da je broj sparenih bridova najveći, sparivanje s najvećim zbrojem težina. Dakle, među svim najvećim sparivanjima ono s najvećim zbrojem težina.

    ![maximum weight maximum cardinality matching](images/graph-match-4.svg)

-   **Savršeno sparivanje** (perfect matching): sparivanje u kojemu je svaki vrh sparen. Savršeno sparivanje uvijek je i najveće sparivanje. Potpun graf s parnim brojem vrhova nužno ima savršeno sparivanje.

-   **Gotovo savršeno sparivanje** (near-perfect matching): sparivanje s točno jednim nesparenim vrhom. To je moguće samo kad graf ima neparan broj vrhova. I gotovo savršeno sparivanje uvijek je najveće sparivanje. Potpun graf s neparnim brojem vrhova nužno ima gotovo savršeno sparivanje.

Problemi sparivanja u natjecateljskom programiranju uglavnom se odnose na najveće sparivanje ili sparivanje maksimalne težine.

## Povećavajući put

U algoritmima za sparivanje povećavajući put središnja je struktura kojom se sparivanje poboljšava.

### Definicija

Za graf $G=(V,E)$ i njegovo sparivanje $M$ možemo definirati sljedeće dvije vrste (jednostavnih) putova:

-   **alternirajući put** (alternating path) put je u kojem se spareni i nespareni bridovi izmjenjuju;
-   **povećavajući put** (augmenting path) alternirajući je put koji počinje i završava u nesparenom vrhu.

Budući da na povećavajućem putu ima $1$ nespareni brid više nego sparenih, broj bridova povećavajućeg puta uvijek je neparan. Ako na povećavajućem putu zamijenimo uloge sparenih i nesparenih bridova, on ostaje alternirajući put, a broj sparenih bridova poraste za $1$. Postupak traženja povećavajućeg puta i njegova obrtanja radi povećanja sparivanja zove se **povećanje** (augmentation). Matematičkim jezikom, povećanje je simetrična razlika sparivanja $M$ i povećavajućeg puta $P$, čime dobivamo novo sparivanje $M\oplus P$.

Sljedeća slika prikazuje kako nakon jednog povećanja broj sparenih bridova raste s $2$ na $3$.

![augment-1](./images/augment-1.png)

### Bergeova lema

Bergeova lema kaže da je metoda poboljšavanja sparivanja povećavajućim putovima dovoljna. Drugim riječima, kad se povećavajući put više ne može naći, dobiveno je najveće sparivanje.

???+ note "Bergeova lema"
    Za graf $G=(V,E)$ i njegovo sparivanje $M$, sparivanje $M$ je najveće ako i samo ako ne postoji povećavajući put u odnosu na $M$.

??? note "Dokaz"
    Već smo pokazali da je, kad postoji povećavajući put $P$, sparivanje $M\oplus P$ veće od $M$, pa $M$ sigurno nije najveće.
    
    Obrnuto, treba pokazati da ako postoji sparivanje $M'$ veće od $M$, onda nužno postoji povećavajući put $P$ u odnosu na $M$. Promotrimo simetričnu razliku $M\oplus M'$. Stupnjevi vrhova u grafu $(V,M\oplus M')$ mogu biti samo $0$, $1$ ili $2$; komponente povezanosti takvog grafa nužno su putovi, ciklusi ili izolirani vrhovi. Štoviše, dva brida susjedna vrhu stupnja $2$ nužno dolaze iz različitih sparivanja, pa je u tim ciklusima broj bridova iz $M$ jednak broju bridova iz $M'$. Budući da je $M'$ veće od $M$, postoji barem jedan put u kojem je bridova iz $M'$ više nego iz $M$; označimo ga $P$. Tada su početak i kraj puta $P$ nespareni vrhovi za $M$, a $P$ je alternirajući put u odnosu na $M$, pa je $P$ nužno povećavajući put u odnosu na $M$. Time je dokaz završen.

Iz ovog teorema slijedi osnovna ideja za traženje najvećeg sparivanja:

-   prolazimo kroz sve nesparene vrhove i tražimo povećavajuće putove dok ih više ne možemo naći.

Zapravo, nakon svakog povećanja nije potrebno iznova prolaziti sve nesparene vrhove. Tijekom cijelog postupka traženja najvećeg sparivanja svaki vrh dovoljno je obraditi samo jednom.

??? note "Dokaz"
    Dovoljno je pokazati: ako u trenutku kad obrada stigne do vrha $v$ ne postoji povećavajući put s početkom u $v$, onda ni nakon nekoliko rundi povećanja ne postoji povećavajući put s početkom u $v$. To znači da, iako povećanje mijenja sparivanje, nije potrebno ponovno provjeravati već obrađene nesparene vrhove.
    
    Pretpostavimo suprotno. Dakle, neka je $v$ već obrađeni nespareni vrh i neka je nakon povećanja duž povećavajućeg puta $P$ od $u$ do $w$ u nekoj rundi nastao povećavajući put $P'$ s početkom u $v$ koji prije nije postojao. Tada put $P'$ nužno ima zajednički brid s $P$; inače povećanje duž $P$ ne bi promijenilo stanje sparenosti bridova na $P'$, pa $P'$ ne bi bio novi povećavajući put nastao tim povećanjem.
    
    ![augment-2](./images/augment-2.svg)
    
    (Na slici crna boja označava nesparene bridove, a crvena i plava različita stanja sparenosti.)
    
    Neka je $x$ prvi vrh iz $P$ do kojeg dolazimo krećući od $v$ duž puta $P'$. Budući da je alternirajući put od $v$ do $x$ postojao i prije ovog povećanja, a tada nije postojao povećavajući put s početkom u $v$, $x$ je nužno spareni vrh, pa ne može biti ni $u$ ni $w$. Stoga su na povećavajućem putu $P$ dva brida susjedna vrhu $x$ i njihova su stanja sparenosti suprotna. To znači da, bez obzira na stanje sparenosti brida kojim alternirajući put s početkom u $v$ dolazi do $x$, taj se put može duž $P$ produljiti do $u$ ili do $w$. Dakle, povećavajući put s početkom u $v$ postojao je već prije povećanja, što je u suprotnosti s pretpostavkom.

### Alternirajuće stablo

Još jedan pojam usko vezan uz povećavajuće putove jest alternirajuće stablo. To je stablo koje nastaje tijekom DFS-a ili BFS-a iz nesparenog vrha $r$ pri traženju povećavajućeg puta.

Za graf $G=(V,E)$ i njegovo sparivanje $M$, ako je podgraf $H\subseteq G$ stablo s korijenom u nesparenom vrhu $r$ i put koji povezuje $r$ s bilo kojim $v\in V(H)$ alternirajući je put, onda $H$ zovemo **alternirajuće stablo** (alternating tree). Vrhove parne dubine u stablu zovemo parnim vrhovima, a vrhove neparne dubine neparnim vrhovima.

Sljedeća slika prikazuje jedno alternirajuće stablo koje može nastati BFS-om iz nesparenog vrha $1$. (Na slici su crveni bridovi spareni, a crni nespareni; tamni su vrhovi spareni, a svijetli nespareni.)

![](images/alternating-tree.svg)

## Postojanje savršenog sparivanja

U teoriji sparivanja postoje dva važna teorema o egzistenciji kojima se može utvrditi postoji li savršeno sparivanje u bipartitnom ili općem grafu.

### Hallov teorem

Neka je $G=(X,Y,E)$ bipartitan graf i $|X|\le |Y|$. Ako su za sparivanje $M$ grafa $G$ svi vrhovi iz $X$ spareni, $M$ zovemo **$X$-savršeno sparivanje**, a ponekad kraće savršeno sparivanje (bipartitnog grafa $G$). To je najveće sparivanje koje se u bipartitnom grafu može postići. Hallov teorem daje nužan i dovoljan uvjet za postojanje takvog sparivanja.

Hallov teorem kaže da $X$-savršeno sparivanje sigurno postoji čim je za svaki podskup od $X$ u $Y$ osigurano dovoljno vrhova koji se s njim mogu spariti.

???+ note "Hallov teorem"
    Neka je $G=(X,Y,E)$ bipartitan graf i $|X|\le |Y|$. Za svaki $W\subseteq X$ neka $N_G(W)$ označava skup svih vrhova grafa $G$ susjednih nekom vrhu iz $W$. Tada $X$-savršeno sparivanje postoji ako i samo ako $|W|\le |N_G(W)|$ vrijedi za sve $W\subseteq X$.

??? note "Dokaz"
    Uvjet je očito nužan. Ako $X$-savršeno sparivanje $M$ postoji, svaki vrh iz $X$ sparen je s različitim vrhom iz $Y$. Skup $N_G(W)$ sadrži barem vrhove sparene s vrhovima iz $W$, pa mu je veličina barem $|W|$.
    
    Uvjet je i dovoljan. Pretpostavimo da $X$-savršeno sparivanje ne postoji; tada postoji najveće sparivanje $M$ u kojem je neki vrh $v\in X$ i dalje nesparen. Neka je $Z$ skup svih vrhova dostupnih alternirajućim putovima iz $v$, te $S=Z\cap X$, $T=Z\cap Y$. Svi vrhovi iz $S\setminus\{v\}$ nužno su spareni, jer je $G$ bipartitan pa alternirajući put iz $v$ do vrha iz $X$ ima parnu duljinu i njegov je posljednji brid nužno spareni brid; i svi vrhovi iz $T$ nužno su spareni, jer bi inače postojao povećavajući put, što je po Bergeovoj lemi u suprotnosti s time da je $M$ najveće. Budući da su svi spareni, a sparivanje je moguće samo između $X$ i $Y$, vrhovi iz $S\setminus\{v\}$ i iz $T$ u bijekciji su, tj. $|T|=|S|-1$. Istodobno, budući da su vrhovi iz $T$ spareni s vrhovima iz $S$, vrijedi barem $T\subseteq N_G(S)$; no za bilo koji $u\in N_G(S)$, ako je susjedan vrhu $v'$ iz $S$, produljenjem alternirajućeg puta do $v'$ dobivamo alternirajući put do $u$, pa je $u\in T$: dakle $T=N_G(S)$. Ovi argumenti pokazuju $|N_G(S)|<|S|$, što je u suprotnosti s uvjetom Hallova teorema. Time je pokazano da $X$-savršeno sparivanje postoji.

???+ note "Korolar"
    Svaki $k$-regularan ($k\ge 1$) bipartitan graf ima savršeno sparivanje.

??? note "Dokaz"
    U regularnom bipartitnom grafu svi vrhovi imaju isti stupanj, neka je $k\ge 1$. Najprije provjerimo da vrijedi Hallov uvjet, tj. da za svaki $W\subseteq X$ vrijedi $|N_G(W)|\ge |W|$. Broj bridova susjednih vrhovima iz $W$ jednak je $k|W|$, a svaki vrh iz $N_G(W)$ susjedan je najviše $k$ od tih bridova, pa nužno $k|W|\le k|N_G(W)|$, tj. $|W|\le |N_G(W)|$. Posebno, $|X|\le |Y|$; a kako su $X$ i $Y$ simetrični, vrijedi $|X|=|Y|$. To znači da je u regularnom bipartitnom grafu $X$-savršeno sparivanje ujedno savršeno sparivanje. Budući da Hallov teorem jamči postojanje $X$-savršenog sparivanja, postoji i savršeno sparivanje.

### Tutteov teorem

Tutteov teorem daje nužan i dovoljan uvjet za postojanje savršenog sparivanja u općem grafu. Uvjet proizlazi iz izravnog zapažanja: graf s neparnim brojem vrhova sigurno nema savršeno sparivanje.

???+ note "Tutteov teorem"
    Graf $G=(V,E)$ ima savršeno sparivanje ako i samo ako za svaki $U\subseteq V$ vrijedi $\operatorname{odd}(G-U)\le |U|$, gdje $G-U$ označava podgraf dobiven brisanjem vrhova iz $U$ i njima susjednih bridova iz $G$, a $\operatorname{odd}(G-U)$ broj komponenata povezanosti podgrafa $G-U$ s neparnim brojem vrhova.

??? note "Dokaz"
    Dovoljno je razmatrati jednostavne grafove, jer višestruki bridovi i petlje ne utječu ni na Tutteov uvjet ni na postojanje savršenog sparivanja.
    
    Nužnost uvjeta razmjerno je lagana. Pretpostavimo da postoji savršeno sparivanje $M$. Za bilo koji $U\subseteq V$, nakon brisanja vrhova iz $U$ iz grafa $G$, svaka komponenta povezanosti s neparnim brojem vrhova ima barem jedan vrh koji se ne može spariti s vrhom iste komponente, pa se ti vrhovi mogu spariti samo s vrhovima iz $U$. Da bi takvo sparivanje postojalo, mora vrijediti barem $\operatorname{odd}(G-U)\le |U|$. To je Tutteov uvjet.
    
    Dovoljnost uvjeta nešto je složenija. Pretpostavimo da $G$ zadovoljava Tutteov uvjet, ali nema savršeno sparivanje. Budući da dodavanje bilo kojeg brida u $G$ čuva Tutteov uvjet, bez smanjenja općenitosti neka je $G$ maksimalan takav graf, tj. $G$ nema savršeno sparivanje, ali dodavanjem bilo kojeg još nepostojećeg brida $e$ graf $G+e$ ima savršeno sparivanje. Neka je $U\subseteq V$ skup svih vrhova stupnja $|V|-1$. Može se dokazati da je svaka komponenta povezanosti grafa $G-U$ potpun graf. Iz toga se može konstruirati savršeno sparivanje grafa $G$: najprije uzmemo najveće sparivanje svake komponente od $G-U$, pri čemu nespareni vrh ostaje samo u komponentama s neparnim brojem vrhova; te nesparene vrhove sparimo s vrhovima iz $U$; budući da je broj vrhova grafa $G$ paran (u Tutteovu uvjetu uzmemo $U=\varnothing$), i broj preostalih nesparenih vrhova u $U$ paran je, pa ih sparimo u parove. Ta kontradikcija pokazuje da ne postoji $G$ koji zadovoljava Tutteov uvjet, a nema savršeno sparivanje.
    
    Ključno je dokazati da je svaka komponenta povezanosti grafa $G-U$ potpun graf. Pretpostavimo suprotno. Neka vrhovi $x,y,z$ pripadaju takvoj komponenti, pri čemu $(x,y)\in E$, $(y,z)\in E$, $(x,z)\notin E$. Nadalje, budući da $y\notin U$, nužno postoji $w\in V\setminus U$ takav da $(y,w)\notin E$. Zbog maksimalnosti grafa $G$, u grafovima $G+(x,z)$ i $G+(y,w)$ postoje savršena sparivanja $M_1$ odnosno $M_2$. Promotrimo njihovu simetričnu razliku $M_1\oplus M_2$. Budući da su stupnjevi svih vrhova u grafu $(V,M_1\oplus M_2)$ ili $0$ ili $2$, $M_1\oplus M_2$ zapravo je disjunktna unija nekoliko parnih ciklusa, a svaki se sastoji od naizmjeničnih sparenih bridova iz $M_1$ i $M_2$. Bez smanjenja općenitosti neka je $(x,z)\in M_1$ i $(y,w)\in M_2$, jer je inače $M_1$ ili $M_2$ već savršeno sparivanje grafa $G$; stoga se oba ta brida pojavljuju u $M_1\oplus M_2$.
    
    ![](images/tutte-proof.svg)
    
    Kako slika prikazuje, moguća su dva slučaja:
    
    -   $(x,z)$ i $(y,w)$ leže na različitim ciklusima (lijevo na slici): neka je $C$ ciklus na kojem leži $(y,w)$; tada je skup bridova $M_2\oplus C$ savršeno sparivanje grafa $G$;
    -   $(x,z)$ i $(y,w)$ leže na istom ciklusu (desno na slici): zbog simetrije neka ciklus redom prolazi kroz $x,y,w,z$; tada možemo uzeti put $P$ na ciklusu od $y$ preko $w$ do $z$, označiti $\{(y,z)\}\cup P$ kao ciklus $C$, i tada je skup bridova $M_2\oplus C$ također savršeno sparivanje grafa $G$.
    
    U oba slučaja dobivamo kontradikciju s izborom grafa $G$. Ta kontradikcija pokazuje da je svaka komponenta povezanosti grafa $G-U$ potpun graf.

???+ note "Korolar"
    Svaki 3-regularan graf bez mostova ima savršeno sparivanje.

??? note "Dokaz"
    Da bismo provjerili Tutteov uvjet, uzmimo proizvoljan $U\subseteq V$; treba dokazati $\operatorname{odd}(G-U)\le |U|$. Neka su $G_1,\cdots,G_n$ sve komponente povezanosti grafa $G-U$ s neparnim brojem vrhova. Neka je $m_i$ broj bridova koji povezuju vrhove iz $G_i$ s vrhovima iz $U$. Jednostavnim prebrojavanjem dobivamo
    
    $$
    3|V(G_i)| = \sum_{v\in V(G_i)} d(v) = 2|E(G_i)| + m_i.
    $$
    
    Dakle, $m_i$ je nužno neparan. Budući da $G$ nema mostova (tj. reznih bridova), vrijedi $m_i\ge 3$. Iz toga slijedi
    
    $$
    \operatorname{odd}(G-U) = n \le \dfrac{1}{3}\sum_{i=1}^n m_i \le \dfrac{1}{3}\sum_{v\in U} d(v) = |U|.
    $$
    
    Dakle, Tutteov uvjet vrijedi i graf $G$ nužno ima savršeno sparivanje.

## Uobičajeni algoritmi

Jedan od osnovnih problema kombinatorne optimizacije jest nalaženje najvećeg sparivanja i sparivanja maksimalne težine u grafu.

### Najveće sparivanje u bipartitnom grafu

Vidi stranicu [Najveće sparivanje u bipartitnom grafu](./bigraph-match.md).

U netežinskom bipartitnom grafu problem se može riješiti Kuhnovim algoritmom u vremenu $O(|V||E|)$ ili Hopcroft–Karpovim algoritmom u vremenu $O(|V|^{1/2}|E|)$.

### Sparivanje maksimalne težine u bipartitnom grafu

Vidi stranicu [Sparivanje maksimalne težine u bipartitnom grafu](./bigraph-weight-match.md).

U težinskom bipartitnom grafu problem se može riješiti mađarskim algoritmom. Ako se pri traženju najkraćeg puta koristi Bellman–Fordov algoritam, složenost je $O(|V|^2|E|)$; uz Dijkstrin algoritam s Fibonaccijevom gomilom problem se rješava u vremenu $O(|V|^{2}\log {|V|}+|V||E|)$.

### Najveće sparivanje u općem grafu

Vidi stranicu [Najveće sparivanje u općem grafu](./general-match.md).

U netežinskom općem grafu problem se može riješiti Edmondsovim blossom algoritmom u vremenu $O(|V|^2|E|)$.

### Sparivanje maksimalne težine u općem grafu

Vidi stranicu [Sparivanje maksimalne težine u općem grafu](./general-weight-match.md).

U težinskom općem grafu problem se može riješiti Edmondsovim blossom algoritmom u vremenu $O(|V|^2|E|)$.

## Povezani problemi

Najveće sparivanje (maksimalne težine) usko je povezano s drugim problemima teorije grafova. U ovom odjeljku razmatramo samo opće grafove; za rezultate o bipartitnim grafovima vidi stranicu [Najveće sparivanje u bipartitnom grafu](./bigraph-match.md#povezani-problemi).

### Najveće sparivanje maksimalne težine

Problemi najvećeg sparivanja maksimalne težine i sparivanja maksimalne težine međusobno se svode jedan na drugi. Bitna je razlika među njima to što u najvećem sparivanju maksimalne težine mogu postojati bridovi negativne težine, dok ih u sparivanju maksimalne težine nema.

Najprije, problem sparivanja maksimalne težine svodi se na problem najvećeg sparivanja maksimalne težine. Za to najprije težine svih negativnih bridova grafa $G$ postavimo na $0$; zatim dodavanjem bridova težine $0$ graf proširimo do potpunog grafa $G'$. Uočimo da se u potpunom grafu s nenegativnim težinama najveće sparivanje maksimalne težine i sparivanje maksimalne težine podudaraju. Stoga je dovoljno izračunati najveće sparivanje maksimalne težine $M'$ grafa $G'$ i iz $M'$ izbrisati sve bridove težine nula; dobiveni skup bridova $M$ sparivanje je maksimalne težine grafa $G$.[^other-approach]

![graph-match](images/graph-match-5.svg)

Obrnuto, problem najvećeg sparivanja maksimalne težine svodi se na problem sparivanja maksimalne težine. Dovoljno je težinama svih bridova grafa $G$ dodati dovoljno velik pozitivan broj $K$ pa je sparivanje maksimalne težine dobivenog grafa $G'$ zajamčeno i najveće sparivanje, a time nužno najveće sparivanje maksimalne težine. Naime, računanje sparivanja maksimalne težine grafa $G'$ odgovara maksimiziranju, preko svih sparivanja grafa $G$, izraza

$$
K|M| + \sum_{e\in M}w(e).
$$

Kad je $K$ dovoljno velik, dobitak $K$ od jednog sparenog brida više premašuje promjenu zbroja težina u drugom članu. Stoga će algoritam najprije spariti što više bridova, a tek zatim maksimizirati zbroj težina sparenih bridova. Konstantu $K$ dovoljno je odabrati tako da bude strogo veća od razlike zbroja težina bilo kojih dvaju sparivanja. Očit je izbor

$$
K = \sum_{e\in E}|w(e)| + 1.
$$

![graph-match](images/graph-match-6.svg)

### Minimalni (težinski) pokrivač bridovima

Još jedan problem usko povezan s najvećim sparivanjem (maksimalne težine) jest minimalni (težinski) pokrivač bridovima. Odnos pokrivača bridovima i sparivanja (zvanog i nezavisni skup bridova) sličan je odnosu pokrivača vrhovima i nezavisnog skupa.

Skup bridova $C\subseteq E$ grafa $G=(V,E)$ zove se **pokrivač bridovima** (edge cover) grafa $G$ ako je svaki vrh $v\in V$ kraj nekog brida iz $C$. Pri razmatranju pokrivača bridovima uvijek pretpostavljamo da graf $G$ nema izoliranih vrhova.

Za netežinske grafove problem minimalnog pokrivača bridovima gotovo je isto što i problem najvećeg sparivanja. Za bilo koje najveće sparivanje $M$ grafa $G$ dovoljno je svakom nesparenom vrhu dodati jedan susjedni brid pa dobivamo minimalni pokrivač bridovima $C$. Njihove veličine zadovoljavaju jednostavan odnos $|M|+|C|=|V|$. Na sljedećoj su slici neki primjeri minimalnih pokrivača bridovima:

![graph-match](images/graph-match-7.svg)

Za težinske grafove problem minimalnog težinskog pokrivača bridovima svodi se na problem **savršenog sparivanja minimalne težine**. Najprije kopiramo graf $G=(V,E)$ i dobivamo $\tilde G=(\tilde V,\tilde E)$ s istim težinama bridova; zatim svaki vrh $v\in V$ povežemo s njegovom kopijom $\tilde v\in\tilde V$ bridom čija je težina najmanja težina brida incidentnog s $v$ u grafu $G$. Dobiveni graf označimo $G'=(V',E')$. Ako je $G$ bipartitan ili rijedak graf, i $G'$ je redom bipartitan odnosno rijedak. Pritom se problem minimalnog težinskog pokrivača bridovima grafa $G$ svodi na problem savršenog sparivanja minimalne težine grafa $G'$[^edge-cover]: za savršeno sparivanje minimalne težine $M'$ grafa $G'$ dovoljno je zadržati bridove iz $E$ i sve sparene bridove $(v,\tilde v)$ zamijeniti bridom najmanje težine incidentnim s $v$ u grafu $G$ pa dobivamo minimalni težinski pokrivač bridovima grafa $G$.

## Literatura

1.  [Wikiwand - Matching (graph theory)](https://www.wikiwand.com/en/Matching_%28graph_theory%29)
2.  [Wikiwand - Blossom algorithm](https://www.wikiwand.com/en/Blossom_algorithm)
3.  Chen Yinbo, „Kratak pregled algoritama za sparivanje u grafovima i njihovih primjena”, 2015.
4.  [Bilješke o algoritmima - Matching](http://web.ntnu.edu.tw/~algo/Matching.html)
5.  [the-tourist/algo](https://github.com/the-tourist/algo)
6.  [Bill Yang's Blog - Bilješke o blossom algoritmu](https://blog.bill.moe/blossom-algorithm-notes/)
7.  [Najveće sparivanje, savršeno sparivanje i mađarski algoritam u bipartitnim grafovima](https://www.renfei.org/blog/bipartite-matching.html)
8.  [Wikiwand - Hopcroft–Karp algorithm](https://www.wikiwand.com/en/Hopcroft%E2%80%93Karp_algorithm)
9.  Bondy, John Adrian, and Uppaluri Siva Ramachandra Murty. Graph theory with applications. Vol. 290. London: Macmillan, 1976.

[^other-approach]: Naravno, to nije jedini način svođenja. Za graf $G=(V,E)$ možemo i njegovu kopiju $\tilde G=(\tilde V,\tilde E)$ vrh po vrh povezati s izvornim grafom, a težine svih bridova novih u odnosu na izvorni graf $G$ (uključujući bridove u kopiji) postaviti na $0$, čime dobivamo graf $G'=(V',E')$. Drugim riječima, skup vrhova novog grafa $G'$ jest $V\cup\tilde V$, a njegov skup bridova, osim bridova grafa $G$, povezuje svaki vrh $v\in V$ s njegovom kopijom $\tilde v\in\tilde V$ bridom težine nula te za svaki brid $(u,v)\in E$ povezuje $\tilde u$ i $\tilde v$ bridom težine nula. Svakom sparivanju $M$ grafa $G$ odgovara savršeno sparivanje grafa $G'$ istog zbroja težina: dovoljno je svaki nespareni vrh $v$ grafa $G$ spariti s njegovom kopijom $\tilde v$, a za svaki spareni brid $(u,v)$ spariti $\tilde u$ i $\tilde v$. Stoga najveće sparivanje maksimalne težine grafa $G'$, tj. savršeno sparivanje maksimalne težine, ograničeno na $E$ daje sparivanje maksimalne težine grafa $G$. Prednost je ovog svođenja što je, ako je $G$ bipartitan ili rijedak graf, i prošireni graf $G'$ redom bipartitan odnosno rijedak.

[^edge-cover]: Za svako savršeno sparivanje $M'$ grafa $G'$ ovdje opisanim postupkom dobivamo pokrivač bridovima $C$ grafa $G$ čiji je zbroj težina polovica zbroja težina od $M'$; obrnuto, obrtanjem te konstrukcije, za svaki pokrivač bridovima $C$ grafa $G$ možemo konstruirati savršeno sparivanje $M'$ grafa $G'$ čiji zbroj težina ne premašuje dvostruki zbroj težina od $C$. To pokazuje da svođenje vrijedi.
