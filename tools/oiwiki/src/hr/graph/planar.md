---
title: Planarni grafovi
---

Ovaj članak uvodi planarne (ravninske) grafove i srodne pojmove.

## Planarni grafovi

Ako se graf $G$ može nacrtati u ravnini $S$ tako da se bridovi sijeku samo u vrhovima, kažemo da se $G$ može uložiti u ravninu $S$ i da je $G$ **planaran graf** (planar graph). Nacrtani graf bez sjecišta bridova zove se ravninski prikaz ili **ravninsko ulaganje** (planar embedding) grafa $G$. Takvo ravninsko ulaganje planarnog grafa zove se i **ravninski graf** (plane graph).

???+ info "„Planaran graf” i „ravninski graf”"
    U različitim tekstovima značenje izraza „planaran graf” može se razlikovati. U definiciji iz ovog članka planaran graf je grafovsko-teorijski objekt koji se u ravninu može uložiti na različite načine; ravninski graf pak je geometrijski objekt koji, osim grafovske strukture, zadaje i način crtanja grafa. Istom planarnom grafu obično odgovara više ravninskih grafova. Zato ćemo za tvrdnje koje ovise samo o grafovskoj strukturi rabiti izraz „planaran graf”, a za one koje ovise i o načinu ulaganja u ravninu izraz „ravninski graf”.

Evo jednostavnih primjera planarnih grafova:

![](images/planar-1.svg)

(lijevo: leptir-graf; desno: potpuni graf $K_4$ reda $4$)

Evo jednostavnih primjera neplanarnih grafova:

![](images/planar-2.svg)

(lijevo: potpuni graf $K_5$ reda $5$; desno: potpuni bipartitni graf $K_{3,3}$ s po $3$ vrha u svakoj strani)

## Svojstva

U ovom odjeljku iznosimo svojstva ravninskih grafova.

### Strane i njihovi stupnjevi

Neka je $G$ ravninski graf; bridovi grafa $G$ dijele ravninu u kojoj $G$ leži na nekoliko područja, a svako se područje zove **strana** (face) grafa $G$. Neomeđena strana zove se **beskonačna strana** (unbounded face) ili **vanjska strana** (external face), a omeđene se zovu konačne ili unutarnje strane. Svaki ravninski graf ima točno jednu vanjsku stranu.

Zatvorena šetnja sastavljena od svih bridova koji okružuju neku stranu zove se **rub** (boundary) te strane, a za bridove ruba kažemo da su **incidentni** (incident) s tom stranom. Duljina ruba zove se **stupanj** (degree) strane. Pri računanju stupnja strane svaki se most broji dvaput. Zbroj stupnjeva svih strana ravninskog grafa jednak je $2$ puta broju bridova $|E|$.

U ravninskom grafu rub strane stupnja $1$ odgovara petlji, a rub strane stupnja $2$ obično paru višestrukih bridova[^face-2]. U jednostavnom povezanom ravninskom grafu s $|V|\ge 3$ vrhova sve strane imaju stupanj barem $3$.

### Eulerova formula

Važno svojstvo ravninskih grafova je **Eulerova formula** (Euler's formula). Ona daje vezu između broja vrhova $|V|$, broja bridova $|E|$ i broja strana $|F|$ grafa.

???+ note "Eulerova formula"
    Za povezan ravninski graf $G$ vrijedi
    
    $$
    |V| - |E| + |F| = 2.
    $$

??? note "Dokaz"
    Primjenjujemo matematičku indukciju po broju strana $|F|$. Baza je $|F|=1$. Tada ravninski graf ima samo vanjsku stranu i svi su bridovi mostovi. Dakle, graf $G$ je stablo, pa nužno vrijedi $|E|=|V|-1$; uvrštavanjem u Eulerovu formulu vidimo da ona vrijedi. Pretpostavimo da Eulerova formula vrijedi za ravninske grafove s $|F| = k$ strana. U ravninskom grafu $G$ s $|F|=k + 1$ strana nužno postoji brid $e$ koji nije most; on je zajednički brid dviju različitih strana. Uklanjanjem brida $e$ iz grafa dobivamo graf $G-e$ s $|V|$ vrhova, $|E|-1$ bridova i $|F|-1$ strana. Po pretpostavci indukcije za graf $G-e$ vrijedi Eulerova formula, tj. $|V|-(|E|-1)+(|F|-1)=2$, a sređivanjem dobivamo Eulerovu formulu za graf $G$. Dakle, po matematičkoj indukciji Eulerova formula vrijedi za sve ravninske grafove.

???+ note "Korolar"
    Za ravninski graf $G$ s $k$ komponenata povezanosti vrijedi
    
    $$
    |V| - |E| + |F| = k + 1.
    $$

??? note "Dokaz"
    Svaka komponenta povezanosti grafa $G$ je ravninski graf, ali te komponente dijele istu vanjsku stranu. Primijenimo li Eulerovu formulu izravno na svaku komponentu i zbrojimo, ukupan broj vrhova i ukupan broj bridova bit će točni, ali će ukupan broj strana biti veći za $(k-1)$, jer je jedinstvena vanjska strana ukupno izbrojena $k$ puta. Uzmemo li u obzir tu korekciju, dobivamo $|V|-|E|+|F| = 2k - (k-1) = k+1$.

Iz toga se može izvesti veza između broja bridova i broja vrhova ravninskog grafa.

???+ note "Teorem"
    Za ravninski graf $G$ s $k$ komponenata povezanosti, ako svaka strana grafa $G$ ima stupanj barem $l \ge 3$, vrijedi
    
    $$
    |E| \le \dfrac{l}{l-2}(|V|-k-1).
    $$

??? note "Dokaz"
    Budući da je stupanj svake strane grafa $G$ barem $l$, zbroj stupnjeva svih strana je barem $l|F|$, tj. $2|E| \ge l|F|$. Uvrštavanjem korolara Eulerove formule $|V| - |E| + |F| = k + 1$ dobivamo
    
    $$
    2|E| \ge l(k + 1 - |V| + |E|).
    $$
    
    Koristeći $l \ge 2$ i rješavajući po $|E|$ dobivamo
    
    $$
    |E| \le \dfrac{l}{l-2}(|V|-k-1).
    $$

???+ note "Korolar"
    Neka je $G$ jednostavan planaran graf s $|V|\ge 3$. Tada vrijedi
    
    $$
    |E| \le 3|V|-6.
    $$

??? note "Dokaz"
    Kad je $G$ povezan, sve strane imaju stupanj barem $3$. Uzmemo li u gornjem teoremu $k=1$ i $l=3$, dobivamo $|E|\le 3|V|-6$.
    
    Kad $G$ nije povezan, razlikujemo dva slučaja:
    
    -   Ako postoji komponenta povezanosti s barem $3$ vrha, za svaku komponentu s barem $3$ vrha možemo zasebno postaviti nejednakost $|E_i|\le 3|V_i|-6$. Za komponente s manje od $3$ vrha sigurno vrijedi $|E_i|\le |V_i| \le 3|V_i|$. Zbrajanjem nejednakosti za sve komponente dobivamo $|E|\le 3|V|-6$.
    -   Ako sve komponente povezanosti imaju manje od $3$ vrha, u cjelini sigurno vrijedi $|E|\le |V|$. Kako za $|V|\ge 3$ vrijedi $|V|\le 3|V|-6$, i dalje vrijedi $|E|\le 3|V|-6$.
    
    Time je tvrdnja dokazana.

Ovaj korolar pokazuje da su jednostavni planarni grafovi rijetki grafovi.

### Dualni graf

Svaki ravninski graf ima odgovarajući (geometrijski) dualni graf.

![](images/planar-dual-1.svg)

Neka je $G$ ravninski graf; graf $G^*$ crtamo ovako:

1.  Unutar svake strane $f_i$ grafa $G$ nacrtamo vrh $v_i^*$.
2.  Za svaki brid $e$ grafa $G$, ako $e$ leži na zajedničkom rubu strana $f_i$ i $f_j$, nacrtamo brid $e^*$ koji spaja $v_i^*$ i $v_j^*$ tako da siječe $e$ točno jednom i ne siječe druge bridove grafa $G$ ni grafa $G^*$. Posebno, ako se $e$ pojavljuje samo na rubu jedne strane $f_i$, nacrtamo petlju u vrhu $v_i^*$ koja siječe $e$.

Tako dobiven graf $G^*$ zove se **dualni graf** (dual graph) grafa $G$.

???+ note "Teorem"
    Neka je graf $G^*$ dualni graf ravninskog grafa $G$. Tada je graf $G^*$ povezan ravninski graf. Štoviše, graf $G^{**}$ izomorfan je grafu $G$ ako i samo ako je $G$ povezan.

??? note "Dokaz"
    Da je graf $G^*$ ravninski, jamči njegova konstrukcija. Treba još dokazati da je graf $G^*$ povezan. Za bilo koja dva vrha $v^*_i,v^*_j$ grafa $G^*$ neka dužina u ravnini koja spaja $v^*_i$ i $v^*_j$ redom prolazi kroz strane i bridove grafa $G$ $f_i,e_{s_1},f_{s_1},\cdots,f_{s_{r-1}},e_{s_r},f_j$; njima redom odgovaraju vrhovi i bridovi dualnog grafa $v_i^*,e_{s_1}^*,v^*_{s_1},\cdots,v^*_{s_{r-1}},e^*_{s_r},v^*_j$. Po konstrukciji grafa $G^*$ susjedni vrhovi i bridovi u tom nizu su incidentni, pa niz opisuje šetnju u grafu $G^*$. Dakle, graf $G^*$ je povezan.
    
    Graf $G^{**}$ je dualni graf grafa $G^*$, pa je nužno povezan. Stoga je nužan uvjet za izomorfnost $G$ i $G^{**}$ da je graf $G$ povezan. Preostaje dokazati da je taj uvjet i dovoljan. Za to je dovoljno pokazati da, kad je graf $G$ povezan, graf $G$ zadovoljava zahtjeve konstrukcije dualnog grafa grafa $G^*$. Budući da bridovi grafa $G^*$ i bridovi grafa $G$ prirodno odgovaraju jedni drugima, dovoljno je dokazati da svaka strana grafa $G^*$ sadrži točno jedan vrh grafa $G$. Za bilo koju stranu $f^*$ grafa $G^*$ neka je $e^*$ brid na njezinu rubu; tada se jedan od krajeva odgovarajućeg brida $e$ grafa $G$ nužno nalazi unutar strane $f^*$, pa strana $f^*$ sadrži barem jedan vrh grafa $G$. Budući da su i $G^*$ i $G$ povezani, vrijedi Eulerova formula; a kako $G$ i $G^*$ imaju jednak broj bridova, a broj strana grafa $G$ jednak je broju vrhova grafa $G^*$, broj vrhova grafa $G$ jednak je broju strana grafa $G^*$. Dakle, svaka strana grafa $G^*$ sadrži točno jedan vrh grafa $G$. Tvrdnja je dokazana.

Između strukture ravninskog grafa i njegova dualnog grafa postoji mnogo podudarnosti:

-   Strane u $G$ odgovaraju vrhovima u $G^*$, bridovi u $G$ odgovaraju bridovima u $G^*$, a vrhovi u $G$ odgovaraju stranama u $G^*$.
-   Petlje u $G$ odgovaraju mostovima u $G^*$, a petlje u $G^*$ odgovaraju mostovima u $G$.
-   Rezni skupovi bridova u $G$ odgovaraju zatvorenim šetnjama u $G^*$, a zatvorene šetnje u $G^*$ odgovaraju reznim skupovima bridova u $G$.

Treba paziti na to da je pojam dualnog grafa definiran samo za konkretan ravninski graf, a ne može se definirati za proizvoljan planaran graf. Zapravo, dualni grafovi dvaju izomorfnih ravninskih grafova ne moraju biti izomorfni. Drugim riječima, dualni grafovi različitih ravninskih ulaganja istog grafa mogu se razlikovati.

???+ example "Primjer"
    Na slici su dva izomorfna ravninska grafa čiji dualni grafovi nisu izomorfni.
    
    ![](images/planar-dual-2.svg)
    
    Dualni grafovi nisu izomorfni zato što desni graf ima stranu stupnja 1, pa njegov dualni graf ima vrh stupnja 1, dok ga lijevi nema.

Prebacivanje problema na planarnom grafu na dualni graf ponekad olakšava rješavanje. Tipičan je primjer da se problem [najmanjeg reza](./flow/min-cut.md) u planarnom grafu može pretvoriti u problem [najkraćeg puta](./shortest-path.md) u dualnom grafu. Neka je $G$ planaran graf s težinama na bridovima, a $s,t$ dva njegova vrha; tražimo najmanji $s$-$t$ rez.

![](images/planar-dual-3.svg)

Kao na slici, odabirom prikladnog ravninskog ulaganja postižemo da $s,t$ leže na rubu vanjske strane grafa $G$. Osim toga, dodamo zrake koje izlaze iz $s$ i $t$ i dijele vanjsku stranu na dva dijela, $f_{+}$ i $f_{-}$. Na temelju tog grafa izgradimo dualni graf i težine bridova pridružimo odgovarajućim bridovima dualnog grafa. Tada su putovi između vrhova koji u dualnom grafu $G^*$ odgovaraju stranama $f_{+}$ i $f_{-}$ (debela crvena linija) u bijekciji s $s$-$t$ reznim skupovima bridova grafa $G$ (debela crna linija), i to s jednakim težinama. Tako, nalaženjem najkraćeg puta u dualnom grafu dobivamo najmanji $s$-$t$ rez u grafu $G$.

Česta je zabluda na temelju opisane pretvorbe tvrditi da je najmanji rez u ravninskom grafu jednak najkraćem putu u dualnom grafu. Zapravo to vrijedi samo kad postoji ravninsko ulaganje grafa $G$ u kojem $s,t$ leže na istoj strani; u natjecateljskim zadacima koji ispituju ovo gradivo zadani graf obično ima takvo ravninsko ulaganje i ono je zadano. Navodimo teorem kojim se može provjeriti njegovo postojanje.

???+ note "Teorem"
    Za dva vrha $s,t$ planarnog grafa $G=(V,E)$ postoji ravninsko ulaganje grafa $G$ u kojem $s,t$ leže na istoj strani ako i samo ako je $(V,E \cup \{(s,t)\}$ planaran graf.

??? note "Dokaz"
    Ako postoji ravninsko ulaganje grafa $G$ u kojem $s,t$ leže na istoj strani, unutar te strane možemo dodati brid $(s,t)$ i graf ostaje planaran.
    
    Ako je $(V, E \cup \{(s,t)\})$ planaran graf, u bilo kojem njegovu ravninskom ulaganju $s,t$ leže na strani na kojoj je brid $(s,t)$. Nakon uklanjanja $(s,t)$ vrhovi $s,t$ i dalje leže na istoj strani. Tvrdnja je dokazana.

Na primjer, dodavanjem brida $(s,t)$ u graf na slici dolje dobiva se neplanaran graf $K_5$, pa takvo ravninsko ulaganje ne postoji i opisana pretvorba nije primjenjiva.

![](images/planar-st.svg)

### Daljnji rezultati

Naravno, o ravninskim grafovima postoji još mnogo poznatih rezultata. Ovdje ih kratko navodimo bez rasprave.

???+ note "Teorem o četiri boje"
    Svaki ravninski graf (bez petlji) može se obojiti s $4$ boje.

???+ note "Fáryjev teorem"
    Jednostavan planaran graf uvijek ima ravninsko ulaganje u kojem su svi bridovi dužine.

???+ note "Teorem (Wood)"
    Planaran graf ima najviše $8|V|-16$ maksimalnih klika.

???+ note "Teorem (Tutte)"
    Svaki $4$‑vršno povezan planaran graf je Hamiltonov.

## Prepoznavanje

U ovom odjeljku raspravljamo kako za zadani graf odlučiti je li planaran.

### Zabranjeni grafovi

Najklasičnija karakterizacija planarnih grafova daje se pomoću **zabranjenih grafova** (forbidden graph).

Najprije, $K_5$ i $K_{3,3}$ nisu planarni grafovi.

???+ note "Teorem"
    $K_5$ i $K_{3,3}$ nisu planarni grafovi.

??? note "Dokaz"
    Ranije smo pokazali da jednostavan povezan ravninski graf s $|V|\ge 3$ mora zadovoljavati
    
    $$
    |E| \le \dfrac{l}{l-2}(|V|-2).
    $$
    
    pri čemu je $l$ najmanji stupanj strane. Za $K_5$ vrijedi $l=3,~|V|=5,~|E|=10$, pa se $K_5$ ne može nacrtati kao ravninski graf. Za $K_{3,3}$ vrijedi $l=4,~|V|=6,~|E|=9$, pa se ni $K_{3,3}$ ne može nacrtati kao ravninski graf.

Zapravo, upravo su to najmanje strukture koje graf čine neplanarnim. Drugim riječima, čim graf (na određeni način) ne sadrži ta dva grafa kao podstrukture, sigurno je planaran.

Prvi teorem o prepoznavanju planarnosti je teorem Kuratowskog. On rabi pojam homeomorfnosti grafova: ako su grafovi $G_1$ i $G_2$ izomorfni, ili postanu izomorfni nakon višestrukog umetanja ili uklanjanja vrhova stupnja $2$, kažemo da su **homeomorfni** (homeomorphic). Time se može iskazati sljedeći rezultat:

???+ note "Teorem Kuratowskog"
    Graf $G$ je planaran ako i samo ako $G$ ne sadrži podgraf homeomorfan s $K_5$ ili $K_{3,3}$.

Još jedan srodan teorem je Wagnerov teorem. On planarne grafove karakterizira pomoću operacije kontrakcije. Kontrakcija znači višestruko sažimanje jednog brida grafa u jedan vrh. Time se može iskazati sljedeći rezultat:

???+ note "Wagnerov teorem"
    Graf $G$ je planaran ako i samo ako $G$ nema podgraf koji se može kontrahirati u $K_5$ ili $K_{3,3}$.

Da planarni grafovi ne sadrže takve podgrafove relativno je očito, pa je ključni dio obaju teorema dovoljnost odgovarajućeg uvjeta o zabranjenim grafovima. Budući da se podgraf homeomorfan s $K_5$ ili $K_{3,3}$ uvijek može kontrahirati u njih, dok obrat ne mora vrijediti, teorem Kuratowskog daje slabiji uvjet za planarnost koji je ujedno lakše provjeriti.

### Algoritmi za ispitivanje planarnosti

Iako se ne čini lakim, za problem ispitivanja planarnosti zapravo postoji mnogo linearnih algoritama. No budući da su njihove implementacije obično prilično složene, gotovo se nikad ne pojavljuju na natjecanjima iz algoritama.

Najraniji linearni algoritam je Hopcroft–Tarjanov algoritam[^ht74], ali je njegova implementacija prilično složena. Algoritam de Fraysseix–Ossona de Mendez–Rosenstiehl (poznat i kao LR algoritam za planarnost)[^dor06][^df08][^bra09] dodatno poboljšava tijek Hopcroft–Tarjanova algoritma i jedan je od trenutačno najboljih algoritama za ispitivanje planarnosti. Pythonova biblioteka NetworkX [implementira](https://github.com/networkx/networkx/blob/main/networkx/algorithms/planarity.py) upravo taj algoritam.

Još jedan jednako dobar algoritam je Boyer–Myrvoldov algoritam[^bm99][^bm04]. On u linearnom vremenu odlučuje je li zadani graf planaran. Štoviše, ako graf jest planaran, algoritam ispisuje ravninsko ulaganje; inače ispisuje podgraf Kuratowskog (tj. podgraf homeomorfan s $K_5$ ili $K_{3,3}$). C++ biblioteka Boost [implementira](https://www.boost.org/doc/libs/1_67_0/boost/graph/planar_detail/boyer_myrvold_impl.hpp) taj algoritam.

Više srodnih algoritama može se naći u literaturi navedenoj na kraju članka.

## Posebni ravninski grafovi

U ovom odjeljku uvodimo nekoliko posebnih klasa planarnih grafova.

### Maksimalni ravninski grafovi

Za jednostavan planaran graf $G$, ako dodavanjem brida između bilo koja dva nesusjedna vrha dobiveni graf više nije planaran, kažemo da je $G$ **maksimalan planaran graf** (maximal planar graph). Ravninsko ulaganje maksimalnog planarnog grafa zove se **maksimalan ravninski graf**.

???+ note "Teorem"
    Maksimalan planaran graf $G$ nužno je povezan. Štoviše, kad je broj vrhova $|V|\ge 3$, graf $G$ nema mostova.

??? note "Dokaz"
    Ako planaran graf $G$ nije povezan, tada u bilo kojem njegovu ravninskom ulaganju možemo odabrati dva vrha iz različitih komponenata povezanosti i spojiti ih unutar vanjske strane; dobiveni graf očito je i dalje ravninski, što pokazuje da graf $G$ nije maksimalan planaran graf. Dakle, ako je graf $G$ maksimalan planaran graf, nužno je povezan.
    
    Ako planaran graf $G$ ima $|V|\ge 3$ vrhova i $G$ ima most $e=(u,v)$, tada graf $G - e$ dobiven uklanjanjem brida $e$ ima točno dvije komponente povezanosti, a $u,v$ pripadaju različitim komponentama. Pretpostavimo da komponenta koja sadrži $v$ ima barem dva vrha. Tada možemo najprije nacrtati u ravnini komponentu $G_1$ koja sadrži $u$, odabrati bilo koju stranu $f$ grafa $G_1$ čiji rub sadrži $u$ i nacrtati drugu komponentu $G_2$ unutar strane $f$. Budući da je $G_2$ jednostavan graf, rub njegove vanjske strane sigurno nije petlja, pa postoji još barem jedan vrh $w\neq u,v$. Spojimo li $v,w$ s $u$, dobivamo ravninski graf koji sadrži $G$ kao podgraf. Dakle, graf $G$ nije maksimalan planaran graf. Stoga maksimalan planaran graf s $|V|\ge 3$ vrhova sigurno nema mostova.

Struktura maksimalnih ravninskih grafova može se opisati preciznije.

???+ note "Teorem"
    Ravninski graf $G$ s $|V|\ge 3$ vrhova maksimalan je ravninski graf ako i samo ako je jednostavan i svaka mu strana ima stupanj $3$.

??? note "Dokaz"
    Dovoljnost uvjeta je očita. Treba pokazati samo nužnost, tj. dokazati: u maksimalnom ravninskom grafu $G$ s $|V|\ge 3$ vrhova svaka strana ima stupanj $3$. Budući da je graf $G$ povezan jednostavan ravninski graf s $|V|\ge 3$, sve strane imaju stupanj barem $3$. Pretpostavimo li da tvrdnja ne vrijedi, postoji strana $f$ čiji rub ima duljinu barem $4$. Kako graf $G$ nema mostova, taj rub može biti samo ciklus. Neka je taj ciklus $v_1v_2v_3v_4\cdots v_1$. Ako $v_1$ i $v_3$ nisu susjedni, spajanje $v_1$ i $v_3$ unutar strane $f$ ne narušava planarnost, što je u suprotnosti s maksimalnošću grafa $G$; dakle $v_1$ i $v_3$ su susjedni; analogno, $v_2$ i $v_4$ su susjedni. No bridovi $(v_1,v_3)$ i $(v_2,v_4)$ ne pojavljuju se unutar strane $f$. To znači da oba brida moraju biti izvan strane $f$. Ali to je nemoguće: kako god ih nacrtali, ta se dva brida nužno sijeku. Dakle, u grafu $G$ ne postoji strana stupnja većeg od $3$. Tvrdnja je dokazana.

???+ note "Korolar"
    Za graf $G$ s $|V|\ge 3$ vrhova uvijek vrijedi $|E|=3|V|-6$ i broj strana $|F|=2|V|-4$.

Budući da je u maksimalnom ravninskom grafu svaka strana omeđena trima bridovima, maksimalan ravninski graf zove se i **ravninska triangulacija** (plane triangulation).

### Vanjskoplanarni grafovi

Neka je $G$ planaran graf; ako postoji ravninsko ulaganje $\tilde{G}$ grafa $G$ takvo da svi vrhovi grafa $G$ leže na rubu jedne strane grafa $\tilde{G}$, kažemo da je $G$ **vanjskoplanaran graf** (outerplanar graph). To se ulaganje zove i vanjskoravninsko ulaganje ili **vanjskoravninski graf**. Obično se strana čiji rub prolazi svim vrhovima crta kao vanjska strana.

![](images/planar-outer.svg)

Svaki vanjskoplanaran graf je planaran, ali obrat ne mora vrijediti. I vanjskoplanarni grafovi mogu se karakterizirati zabranjenim grafovima.

???+ note "Teorem"
    Graf $G$ je vanjskoplanaran ako i samo ako $G$ ne sadrži podgraf homeomorfan s $K_4$ ili $K_{2,3}$.

Za vanjskoplanarne grafove također se može govoriti o maksimalnim vanjskoplanarnim grafovima. Za jednostavan vanjskoplanaran graf $G$, ako dodavanjem brida između bilo koja dva nesusjedna vrha dobiveni graf više nije vanjskoplanaran, kažemo da je $G$ **maksimalan vanjskoplanaran graf** (maximal outerplanar graph). Vanjskoravninsko ulaganje maksimalnog vanjskoplanarnog grafa zove se **maksimalan vanjskoravninski graf**. Maksimalan vanjskoravninski graf zapravo je triangulacija mnogokuta u ravnini.

???+ note "Teorem"
    Maksimalan vanjskoravninski graf $G$ s $|V|\ge 3$ vrhova, u kojem svi vrhovi leže na rubu vanjske strane, tada graf $G$ ima točno $|V|-2$ unutarnjih strana.

??? note "Dokaz"
    Primjenjujemo matematičku indukciju po $|V|$. Baza je $|V|=3$. Tada je graf $G$ trokut i ima samo $1$ unutarnju stranu, pa tvrdnja vrijedi. Pretpostavimo da tvrdnja vrijedi za $|V| = k$. Treba dokazati da vrijedi i za $|V| = k+1$.
    
    Najprije, u grafu $G$ sigurno postoji vrh stupnja $2$. U suprotnom bi svaki vrh, osim sa susjednim vrhovima na rubu vanjske strane, morao biti spojen i s nekim trećim vrhom. Numerirajmo vrhove na rubu vanjske strane redom i za svaki $i = 1,2,\cdots,k+1$ definirajmo $f(i)$ kao najmanji broj vrha spojenog s vrhom $i$ čiji broj nije susjedan s njim. Razmotrimo moguće vrijednosti $f(i)$. Najprije, $1 < f(1)$. Budući da je vrh $1$ već spojen s $f(1)$, spojnica vrha $2$ i $f(2)$ ne može prijeći brid $(1,f(1))$, pa nužno vrijedi $1 < 2 < f(2) < f(1)$. Analogno, $2 < 3 < f(3) < f(2)$. Budući da je vrhova konačno mnogo, taj postupak sužavanja mora stati nakon konačno mnogo koraka. Neka je $i^*$ najveći broj $i$ za koji vrijedi $1 < \cdots < i-1 < i < f(i) < f(i-1) < \cdots < f(1)$. Budući da vrhovi $i^*$ i $f(i^*)$ nisu susjedni, nužno vrijedi $i^* < i^* + 1 < f(i^*)$. Ponavljanjem prethodnog rasuđivanja i dalje bi trebalo vrijediti $i^* < i^*+1 < f(i^*+1) < f(i^*)$, što je u suprotnosti s maksimalnošću $i^*$. Ta kontradikcija pokazuje da u grafu $G$ nužno postoji vrh stupnja $2$.
    
    Neka je $v$ takav vrh stupnja $2$. Uklanjanjem tog vrha iz grafa $G$ dobivamo vanjskoravninski graf $G-v$ s $k$ vrhova. On je nužno maksimalan vanjskoravninski graf, jer bi se inače svaki dopušteni način dodavanja brida u njemu mogao primijeniti i na graf $G$. Po pretpostavci indukcije graf $G-v$ ima točno $k-2$ unutarnje strane, a uklanjanjem vrha $v$ nestala je točno jedna unutarnja strana grafa $G$. Dakle, graf $G$ ima $k-1$ unutarnjih strana. Tvrdnja je dokazana.

???+ note "Teorem"
    Vanjskoravninski graf $G$ s $|V|\ge 3$ vrhova, u kojem svi vrhovi leže na rubu vanjske strane, tada je graf $G$ maksimalan vanjskoravninski graf ako i samo ako je rub vanjske strane grafa $G$ ciklus duljine $|V|$, a rubovi svih unutarnjih strana ciklusi duljine $3$.

??? note "Dokaz"
    Dovoljnost je očita. Naime, promotrimo spajanje dvaju nesusjednih vrhova na rubu vanjske strane. Ako se spoje unutar vanjske strane, svi vrhovi više ne mogu ležati na rubu jedne strane; inače spojnica nužno siječe rub neke unutarnje strane.
    
    Dokažimo sada nužnost. Pretpostavimo da rub vanjske strane $v_1v_2v_3\cdots v_nv_1~(n = |V|)$ grafa $G$ nije ciklus. Tada on neki vrh prolazi više puta, tj. postoje $i\neq j$ s $i-j\neq\pm 1\pmod{n}$ takvi da je $v_i=v_j$. Bez smanjenja općenitosti neka je $1 < i < j < n$. Tada se bridovi incidentni s $v_{i-1}$ mogu nalaziti samo unutar omeđenog područja koje zatvara zatvorena šetnja $v_jv_{j+1}\cdots v_nv_1\cdots v_{i-1}v_i$, a bridovi incidentni s $v_{i+1}$ samo unutar omeđenog područja koje zatvara zatvorena šetnja $v_iv_{i+1}\cdots v_{j-1}v_{j}$, pa $v_{i-1}$ i $v_{i+1}$ ne mogu biti susjedni. Unutar vanjske strane možemo dodati brid $e$ koji spaja $v_{i-1}$ i $v_{i+1}$ i dobiti graf $G+e$. On je očito također ravninski graf i rub njegove vanjske strane sadrži sve vrhove. To je u suprotnosti s maksimalnom vanjskoravninskošću grafa $G$. Dakle, vanjska strana grafa $G$ nužno je ciklus duljine $|V|$. Razlog zašto su rubovi unutarnjih strana grafa $G$ ciklusi duljine $3$ isti je kao kod maksimalnih ravninskih grafova pa ga ne ponavljamo.

???+ note "Korolar"
    Za maksimalan vanjskoravninski graf $G$ s $|V|\ge 3$ vrhova vrijedi:
    
    1.  $|E|=2|V|-3$.
    2.  $G$ ima barem $3$ vrha stupnja najviše $3$ i barem $2$ vrha stupnja $2$.
    3.  Vršna povezanost grafa $G$ je $2$.

## Zadaci

-   [Luogu P3209 \[HNOI2010\] Ispitivanje planarnosti](https://www.luogu.com.cn/problem/P3209)
-   [Luogu P3249 \[HNOI2016\] Rudnik](https://www.luogu.com.cn/problem/P3249)
-   [Luogu P4001 \[ICPC-Beijing 2006\] Vuk lovi zečeve](https://www.luogu.com.cn/problem/P4001)
-   [Luogu P4073 \[WC2013\] Planaran graf](https://www.luogu.com.cn/problem/P4073)
-   [Luogu P7295 \[USACO21JAN\] Paint by Letters P](https://www.luogu.com.cn/problem/P7295)

## Literatura i bilješke

-   [Planar graph - Wikipedia](https://en.wikipedia.org/wiki/Planar_graph)
-   [Planarity testing - Wikipedia](https://en.wikipedia.org/wiki/Planarity_testing)
-   Bondy, John Adrian, and Uppaluri Siva Ramachandra Murty. Graph theory with applications. Vol. 290. London: Macmillan, 1976.
-   Diestel, Reinhard. Graph theory. Vol. 173. Springer Nature, 2025.
-   Patrignani, Maurizio. "Planarity Testing and Embedding." (2013): 1-42.

[^face-2]: No to nije jedina mogućnost. Dvije ugniježđene petlje također tvore stranu stupnja 2. Osim toga, postojanje strane stupnja 2 ne znači nužno da graf nije jednostavan; na primjer, u grafu s jednim jedinim bridom jedina strana (vanjska) također ima stupanj 2.

[^ht74]: Hopcroft, John, and Robert Tarjan. "Efficient planarity testing." Journal of the ACM (JACM) 21, no. 4 (1974): 549-568.

[^dor06]: De Fraysseix, Hubert, Patrice Ossona De Mendez, and Pierre Rosenstiehl. "Trémaux trees and planarity." International Journal of Foundations of Computer Science 17, no. 05 (2006): 1017-1029.

[^df08]: De Fraysseix, Hubert. "Trémaux trees and planarity." Electronic Notes in Discrete Mathematics 31 (2008): 169-180.

[^bra09]: Brandes, Ulrik. "The left-right planarity test." Manuscript submitted for publication 3 (2009).

[^bm99]: Boyer, John M., and Wendy J. Myrvold. "Stop Minding Your p's and q's: A Simplified O (n) Planar Embedding Algorithm." In SODA, vol. 99, pp. 140-146. 1999.

[^bm04]: Boyer, John M., and Wendy J. Myrvold. "Simplified o (n) planarity by edge addition." Graph Algorithms and Applications 5 (2006): 241.
