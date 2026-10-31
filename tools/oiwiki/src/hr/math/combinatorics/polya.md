---
title: Pólyino prebrojavanje
---

Preduvjeti: [Permutacije](../permutation.md)

## Uvod

Pólyin teorem prebrojavanja (Pólya enumeration theorem) obično se koristi za rješavanje zadataka prebrojavanja u kojima se pojavljuje pojam „bitno različit”.

???+ info "Ovaj članak može dotaknuti sadržaj iz teorije grupa"
    Ovaj članak može dotaknuti sadržaj iz teorije grupa. U njemu ćemo pojmove iz teorije grupa koji se pojavljuju kratko objasniti kako bi čitatelji koji nisu upoznati s tim gradivom mogli razumjeti i primijeniti Pólyin teorem prebrojavanja. Za sadržaj iz teorije grupa, strogu formulaciju i raspravu pogledajte poglavlja [Osnovni pojmovi apstraktne algebre](../algebra/basic.md), [Teorija grupa](../algebra/group-theory.md) i dr.

??? info "„Grupa simetrija”, „simetrična grupa” i „grupa permutacija”"
    U ovom će se članku neizbježno istodobno koristiti imena ovih triju vrsta grupa. Iako ih je lako pobrkati, ona doista označavaju različite pojmove. Za zadanu geometrijsku strukturu operacije simetrije na njoj jesu geometrijske transformacije koje je preslikavaju na samu sebe, a grupa simetrija (symmetry group) skup je tih operacija simetrije. Simetrična grupa (symmetric group) skup je svih permutacija zadanog skupa. Grupa permutacija (permutation group) pak je podgrupa simetrične grupe, tj. grupa koju čine neke (ne nužno sve) permutacije. U nastavku ćemo objasniti kako grupu simetrija zadane geometrijske strukture prikazati u obliku grupe permutacija i upotrijebiti je u zadacima prebrojavanja.

## Burnsideova lema

Povezano štivo: [Burnsideova lema](../algebra/group-theory.md#burnside-引理)

Pólyin teorem prebrojavanja primjena je i poopćenje Burnsideove leme. Prije uvođenja Pólyina teorema prebrojavanja potrebno je kratko ponoviti sadržaj Burnsideove leme.

Da bismo došli do općeg pravila, najprije razmotrimo jednostavan primjer.

???+ example "Bojenje ogrlice"
    Imamo ogrlicu s ukupno četiri perle, a svaka perla može biti crvena ili plava. Izračunajte koliko ima bitno različitih ogrlica. (Ako se dva bojenja mogu dovesti do podudaranja rotacijom ogrlice, smatramo ih jednakima.)

??? example "Rješenje i analiza"
    Ovaj je zadatak dovoljno jednostavan da ga možemo riješiti nabrajanjem. Perli ima ukupno $4$, a svaka se može obojiti u $2$ boje, pa svih mogućih bojenja ogrlice ima ukupno $2^4=16$. Grupiramo li u istu skupinu bojenja koja se rotacijom mogu dobiti jedno iz drugoga, dobivamo ukupno $6$ skupina, kao na slici dolje. (Pritom kôd pojedinog bojenja označava boje redom u smjeru kazaljke na satu počevši od perle u donjem lijevom kutu, $B$ označava plavu, a $R$ crvenu; kodovi bojenja koja pripadaju istoj skupini imaju istu boju pozadine.)
    
    ![Bojenje ogrlice](../images/necklaces.svg)
    
    Iz ovog se primjera vidi da je za izračun broja bitno različitih bojenja ključno zapravo znati koliko različitih bojenja odgovara svakom bitno jednakom bojenju. Drugim riječima, treba utvrditi veličinu svake skupine na gornjoj slici.
    
    Bojenja koja se mogu svrstati u istu skupinu upravo su ona bojenja koja se rotacijama mogu pretvoriti jedno u drugo. Ukupno postoje $4$ načina rotacije, tj.
    
    $$
    G=\{r_0,r_1,r_2,r_3\},
    $$
    
    koji redom označavaju rotaciju za $0,1,2,3$ koraka. Rotacija za $0$ koraka znači da se ništa ne mijenja.
    
    Pogledajmo najprije skupinu kojoj pripada bojenje $RRBB$. Primijenimo li na njega ove četiri operacije, redom dobivamo
    
    $$
    RRBB, RBBR, BBRR, BRRB.
    $$
    
    Ova su četiri bojenja međusobno različita, pa ta skupina ima $4$ elementa.
    
    Pogledajmo zatim skupinu kojoj pripada bojenje $BRBR$. Primijenimo li na njega iste četiri operacije, redom dobivamo
    
    $$
    BRBR, RBRB, BRBR, RBRB.
    $$
    
    Ovdje je rezultat rotacije za dva koraka jednak rezultatu bez rotacije, a rezultat rotacije za tri koraka jednak rezultatu rotacije za jedan korak. Stoga ta skupina ima $2$ elementa.
    
    Na kraju pogledajmo skupine kojima pripadaju bojenja $BBBB$ i $RRRR$. Primjenom četiriju operacija na njih dobivamo uvijek njih same. Zato svaka od tih skupina ima samo $1$ element.
    
    Označimo li s $x$ bojenje, a s $Gx$ skup kodova boja koji se mogu dobiti primjenom operacija na bojenje $x$, iz gornjeg se primjera može izvući pravilo: utjecaj operacija iz $G$ na $x$ ima neku vrstu „periodičnosti”.
    
    Neka $|G|$ označava ukupan broj operacija. Ta „periodičnost” utjecaja znači: ako $m$ različitih operacija iz $G$ preslikava bojenje $x$ u njega samo, tada se rezultati primjene tih operacija na $x$ ponavljaju po $m$ puta. Zato bojenje $x$ pod tim operacijama daje ukupno $|G|/m$ različitih rezultata, a to je upravo veličina skupine kojoj $x$ pripada.
    
    U ovom primjeru samo rotacija za nula koraka $r_0$ preslikava $RRBB$ u njega samo, pa je veličina njegove skupine jednaka $4/1=4$; rotacija za nula koraka $r_0$ i rotacija za dva koraka $r_2$ obje preslikavaju $BRBR$ u njega samo, pa je veličina njegove skupine jednaka $4/2=2$; bez obzira na broj koraka rotacije $BBBB$ se preslikava u njega samo, pa je veličina njegove skupine $4/4=1$.
    
    U daljnjem izlaganju s $G_x$ označavamo skup operacija koje preslikavaju $x$ u njega samo, pa je $|G_x|$ upravo gornji $m$. Tada je veličina skupine kojoj pripada $x$ jednaka $|G|/|G_x|$. Da bismo izračunali broj skupina bojenja, dovoljno je proći kroz sva moguća bojenja $x\in X$ i bojenju $x$ čija skupina ima veličinu $|Gx|$ pridružiti težinu $1/|Gx|$; tako broj skupina možemo izraziti kao
    
    $$
    |X/G|=\sum_{x\in X}\frac{1}{|Gx|}=\sum_{x\in X}\frac{|G_x|}{|G|}.
    $$
    
    Ovaj oblik izraza nije pogodan za primjenu. Označimo s $gx$ rezultat primjene operacije $g\in G$ na bojenje $x\in X$; tada je gore opisani skup $G_x$ upravo $\{g\in G:gx=x\}$, pa zamjenom redoslijeda zbrajanja dobivamo
    
    $$
    \begin{aligned}
    \sum_{x\in X}|G_x| 
    &=\sum_{x\in X}|\{g\in G:gx=x\}|\\
    &=\sum_{x\in X}\sum_{g\in G}[gx=x]\\
    &=\sum_{g\in G}\sum_{x\in X}[gx=x]\\
    &=\sum_{g\in G}|\{x\in X:gx=x\}|\\
    &=\sum_{g\in G}|X^g|.
    \end{aligned}
    $$
    
    Ovdje je $[\cdot]$ Iversonova zagrada. U rezultatu zamjene redoslijeda zbrajanja $X^g=\{x\in X:gx=x\}$ označava skup bojenja $x$ koja ostaju nepromijenjena pod operacijom $g$. Ukratko, to su fiksne točke operacije $g$.
    
    Nakon ovih razmatranja broj skupina sada možemo zapisati kao
    
    $$
    |X/G|=\frac{1}{|G|}\sum_{g\in G}|X^g|.
    $$
    
    Drugim riječima, broj skupina jednak je prosječnom broju fiksnih točaka svih rotacija.
    
    Kao primjenu ovog rezultata ponovno izračunajmo broj bojenja ogrlice. Fiksne točke rotacija možemo popisati ovako.
    
    | Operacija |        Fiksne točke       |
    | :---: | :-----------------------: |
    | $r_0$ |            $X$            |
    | $r_1$ |      $\{BBBB,RRRR\}$      |
    | $r_2$ | $\{BBBB,BRBR,RBRB,RRRR\}$ |
    | $r_3$ |      $\{BBBB,RRRR\}$      |
    
    Stoga je broj skupina jednak
    
    $$
    \frac{16+2+4+2}{4} = 6.
    $$
    
    Tako smo dobili prijašnji rezultat.

Iz ovog primjera može se izvesti opći rezultat za rješavanje ovakvih zadataka prebrojavanja. Radi lakše rasprave u ovom članku promatramo situaciju zadatka bojenja; naravno, sve se može primijeniti i na druge situacije, a odgovarajući primjeri dani su u nastavku.

Zadatak bojenja glasi: zadana je neka struktura i bojenjem svakog njezina objekta koji se može obojiti (npr. elementa, vrha, brida itd.) dobivaju se različita bojenja. Ta struktura ima neku simetriju, zbog koje se naizgled različita bojenja nakon niza operacija simetrije mogu pretvoriti jedno u drugo. Bojenja koja se mogu pretvoriti jedno u drugo nazivamo bitno jednakima. Zadatak je odrediti broj bitno različitih bojenja.

Prema analizi iz primjera, za rješavanje ovakvog zadatka najprije treba razmotriti koje sve operacije simetrije zadana struktura ima. Skup $G$ tih operacija simetrije naziva se grupom simetrija zadane strukture. U praktičnim primjenama većinom nije potrebno poznavati definiciju grupe; dovoljno je moći bez ponavljanja i bez propuštanja razmotriti sve operacije simetrije. U nastavku članka analizirana je struktura nekoliko uobičajenih grupa simetrija, a ondje je objašnjena i definicija grupe.

Skup svih bojenja označavamo s $X$, a pojedino bojenje u njemu s $x$. Rezultat djelovanja operacije $g\in G$ na bojenje $x\in X$ jest $gx$. Tada je skup svih rezultata koji se mogu dobiti djelovanjem neke operacije na bojenje $x$ jednak $Gx=\{gx:g\in G\}$ i naziva se orbitom od $x$ pod djelovanjem grupe $G$. Različita bojenja u istoj orbiti upravo su ona koja se u ovakvim zadacima nazivaju „bitno jednakima”. Stoga je broj svih bitno različitih bojenja jednak broju različitih orbita.

Analiza iz primjera može se poopćiti na opći slučaj.

???+ note "Burnsideova lema"
    Za zadano djelovanje grupe $G$ na skupu $X$ broj svih različitih orbita jednak je
    
    $$
    |X/G|=\frac{1}{|G|}\sum_{g\in G}|X^g|.
    $$
    
    Ovdje je $X^g=\{x\in X:gx=x\}$ skup fiksnih točaka pod djelovanjem $g\in G$.

Njezin dokaz gotovo doslovno ponavlja analizu iz gornjeg primjera. No u primjeru smo upotrijebili opažanje da rezultat djelovanja grupe $G$ na pojedini element $x$ ima neku „periodičnost”, pa je broj ponavljanja tog perioda jednak broju operacija koje preslikavaju $x$ u njega samog. To je opažanje točno i u općem slučaju, ali budući da struktura grupe $G$ može biti vrlo složena, njezina „periodičnost” nije nužno tako izravna kao u primjeru. Za strogu formulaciju tog opažanja potreban je [teorem o orbiti i stabilizatoru (orbit-stabilizer theorem)](../algebra/group-theory.md#稳定化子) iz teorije grupa.

U primjenama je dovoljno nabrojiti sve operacije simetrije i za svaku navesti broj fiksnih točaka da bi se riješio odgovarajući zadatak prebrojavanja. Slijedi nešto složenija primjena.

???+ example "Bojenje kocke"
    Kocku bojimo trima bojama. Odredite broj bitno različitih bojenja (dva bojenja koja se nakon rotacije u prostoru podudaraju smatraju se jednakima).

??? example "Rješenje"
    Budući da kocka ima $6$ strana, a svaka se strana može obojiti na $3$ načina, ukupno ima $3^6$ bojenja, tj. $|X|=3^6$. Grupu simetrija kocke označimo s $G$.
    
    ![](../images/cube.svg)
    
    Zatim trebamo analizirati sve operacije iz $G$; mogu se podijeliti u sljedeće vrste (radi jednostavnosti šest strana kocke nazivamo prednja, stražnja, gornja, donja, lijeva i desna):
    
    -   Mirovanje, tj. identiteta: budući da sva bojenja pod identitetom ostaju nepromijenjena, njoj odgovara $|X^g|=3^6$;
    -   Rotacija za $90^\circ$ oko osi kroz središta dviju nasuprotnih strana: par nasuprotnih strana može se odabrati na $3$ načina, a smjer rotacije na $2$ načina, pa ova vrsta sadrži ukupno $6$ permutacija. Odaberemo li za os spojnicu središta prednje i stražnje strane, gornja, donja, lijeva i desna strana moraju biti iste boje da bi bojenje ostalo nepromijenjeno nakon rotacije. Tada postoje $3$ područja koja se mogu neovisno obojiti, pa joj odgovara $|X^g|=3^3$;
    -   Rotacija za $180^\circ$ oko osi kroz središta dviju nasuprotnih strana: par nasuprotnih strana može se odabrati na $3$ načina, a izbor smjera rotacije nema utjecaja, pa ova vrsta sadrži ukupno $3$ permutacije. Odaberemo li za os spojnicu središta prednje i stražnje strane, gornja i donja strana moraju biti iste boje te lijeva i desna strana moraju biti iste boje da bi bojenje ostalo nepromijenjeno nakon rotacije. Tada postoje $4$ područja koja se mogu neovisno obojiti, pa joj odgovara $|X^g|=3^4$;
    -   Rotacija za $180^\circ$ oko osi kroz polovišta dvaju nasuprotnih bridova: par nasuprotnih bridova može se odabrati na $6$ načina, a smjer rotacije i dalje nema utjecaja na permutaciju, pa ova vrsta sadrži ukupno $6$ permutacija. Odaberemo li za nasuprotne bridove zajednički brid prednje i gornje strane te zajednički brid donje i stražnje strane, prednja i gornja strana moraju biti iste boje, donja i stražnja strana iste boje te lijeva i desna strana iste boje da bi bojenje ostalo nepromijenjeno nakon rotacije. Tada postoje $3$ područja koja se mogu neovisno obojiti, pa joj odgovara $|X^g|=3^3$;
    -   Rotacija za $120^\circ$ oko osi kroz dva nasuprotna vrha: par nasuprotnih vrhova može se odabrati na $4$ načina, a smjer rotacije na $2$ načina, pa ova vrsta sadrži ukupno $8$ permutacija. Odaberemo li za nasuprotne vrhove gornji desni vrh prednje strane i donji lijevi vrh stražnje strane, prednja, gornja i desna strana moraju biti iste boje te stražnja, donja i lijeva strana iste boje da bi bojenje ostalo nepromijenjeno nakon rotacije. Tada postoje $2$ područja koja se mogu neovisno obojiti, pa joj odgovara $|X^g|=3^2$.
    
    Stoga je broj svih bitno različitih bojenja
    
    $$
    \frac{1\times3^6+6\times3^3+3\times3^4+6\times3^3+8\times3^2}{1+6+3+6+8}=57.
    $$

## Pólyin teorem prebrojavanja

U iskazu Burnsideove leme nigdje se ne koristi svojstvo da je skup $X$ skup svih bojenja neke strukture. Zapravo, područje primjene Burnsideove leme nije ograničeno na zadatke prebrojavanja bojenja. Za zadatke prebrojavanja bojenja Pólyin teorem prebrojavanja daje konkretniju metodu računanja. Može se smatrati primjenom opće Burnsideove leme na zadatke prebrojavanja bojenja.

U odnosu na Burnsideovu lemu, poboljšanje koje donosi Pólyin teorem prebrojavanja jest konkretna metoda računanja veličine skupa fiksnih točaka $|X^g|$ u zadacima prebrojavanja bojenja.

To se zorno vidi iz gornjeg primjera bojenja kocke. Za sve operacije simetrije kocke veličina skupa fiksnih točaka oblika je $m^{c(g)}$, gdje je $m$ broj boja, a $c(g)$ broj područja koja se pod operacijom $g$ mogu neovisno obojiti. To opažanje vrijedi i u općem slučaju, ali treba dodatno razjasniti kako za zadani $g$ izračunati vrijednost $c(g)$.

Odabir bojenja neke strukture, izražen matematičkim jezikom, odabir je preslikavanja $f:X\rightarrow C$ iz skupa $X$ objekata te strukture koji se mogu obojiti (npr. perli ogrlice, strana kocke itd.) u skup boja $C$. Stoga je skup bojenja upravo $C^X$. Grupa simetrija $G$ te strukture djeluje na strukturi, a time prirodno djeluje i na skupu $X$. Takva operacija simetrije uvijek odgovara bijekciji skupa $X$, tj. **permutaciji** (permutation).[^perm-group]

Analizirajmo sada strukturu skupa fiksnih točaka $(C^X)^g$. Za zadani $g$, shvaćen kao permutacija skupa $X$, po uzoru na analizu iz primjera znamo: ako se pozicija $x$ iz $X$ nakon konačno mnogo ponavljanja operacije $g$ može premjestiti na poziciju $y$, tada fiksna točka $f\in (C^X)^g$ nužno mora zadovoljavati $f(x)=f(y)$. Jezikom orbita iz prethodnog odjeljka: budući da se pozicije $x$ i $y$ nalaze u istoj orbiti djelovanja[^g-act] operacije $g$, moraju biti obojene istom bojom. Jezikom permutacija: u [rastavu na cikluse](../permutation.md#zapis-ciklusima) permutacije $g$ pozicije $x$ i $y$ nalaze se u istom ciklusu, pa moraju biti obojene istom bojom. Različiti ciklusi u rastavu na cikluse ne moraju biti obojeni jednako, mogu se bojiti neovisno, pa je broj područja koja se mogu neovisno obojiti upravo $c(g)$, tj. broj ciklusa u rastavu permutacije $g$ na cikluse.

Prema tome, broj fiksnih točaka operacije $g$ jednak je $|C|^{c(g)}$. Uvrstimo li taj zaključak u Burnsideovu lemu, dobivamo netežinsku inačicu **Pólyina teorema prebrojavanja** (Pólya enumeration theorem).

???+ note "Pólyin teorem prebrojavanja (netežinska inačica)"
    Za zadano djelovanje grupe $G$ na skupu $X$ i skup boja $C$ broj različitih bojenja jednak je
    
    $$
    |C^X/G|=\frac{1}{|G|}\sum_{g\in G}m^{c(g)},
    $$
    
    gdje je $m$ broj boja, a $c(g)$ broj ciklusa u rastavu na cikluse permutacijskog prikaza elementa $g\in G$.

??? info "O značenju grupe $G$"
    Ovdje se oznake ponešto zloupotrebljavaju. Ako grupa $G$ djeluje na $X$, djelovanje grupe na skupu bojenja $C^X$ zapravo treba iznova definirati; ovdje to ne razlikujemo.

Kao jednostavnu primjenu Pólyina teorema prebrojavanja, u nastavku ponovno računamo prijašnje primjere pomoću Pólyina teorema prebrojavanja.

??? example "Drugo rješenje zadatka bojenja ogrlice"
    Označimo četiri perle brojevima $1\sim 4$; tada elementi grupe $G$ iz primjera imaju sljedeće permutacijske prikaze (svi su zapisani u obliku rastava na cikluse):
    
    -   rotacija za nula koraka $r_0=(1)$, ukupno $4$ ciklusa (uočite izostavljene $1$‑cikluse);
    -   rotacija za jedan korak $r_1=(1234)$, ukupno $1$ ciklus;
    -   rotacija za dva koraka $r_2=(13)(24)$, ukupno $2$ ciklusa;
    -   rotacija za tri koraka $r_3=(1432)$, ukupno $1$ ciklus.
    
    Stoga je broj bitno različitih bojenja
    
    $$
    \frac{2^4+2^1+2^2+2^1}{4}=6.
    $$

??? example "Drugo rješenje zadatka bojenja kocke"
    Budući da je prijašnja analiza zapravo već dala zapis ciklusima svih vrsta permutacija, samo ga nije eksplicitno ispisala brojevima, ovdje ne ponavljamo prijašnju analizu. Kao ilustraciju razmotrimo samo slučaj rotacije za $180^\circ$ oko osi kroz polovišta nasuprotnih bridova. Označimo prednju, stražnju, gornju, donju, lijevu i desnu stranu redom brojevima $1\sim6$; tada je odgovarajuća permutacija $(13)(24)(56)$, pa je $c(g)=3$. Ostale vrste permutacija analiziraju se slično, a konačni izraz za broj bojenja potpuno se podudara s gornjim.

## Poopćenje na težinski oblik

Netežinska inačica Pólyina teorema prebrojavanja može dati samo broj svih bitno različitih bojenja, ali je nemoćna pri rješavanju finijih zadataka. Primjerice, ako je u gornjem zadatku bojenja zadan broj dostupnih perli svake boje, gornja se Pólyina formula ne može izravno primijeniti. Pri rješavanju takvih zadataka u praksi treba ponovno provesti izvod pomoću Burnsideove leme; sažmemo li te rezultate u oblik funkcije izvodnice, dobivamo težinsku inačicu Pólyina teorema prebrojavanja.

???+ example "Bojenje ogrlice (s ograničenjem)"
    Imamo ogrlicu s ukupno četiri perle, a svaka perla može biti crvena ili plava; na raspolaganju su točno dvije crvene i dvije plave perle. Izračunajte koliko ima bitno različitih ogrlica. (Ako se dva bojenja mogu dovesti do podudaranja rotacijom ogrlice, smatramo ih jednakima.)

??? example "Rješenje i analiza"
    Primijenimo Burnsideovu lemu. Imamo po dvije crvene i plave perle, pa ukupno ima $\dbinom{4}{2}=6$ bojenja. Grupa simetrija $G=\{r_0,r_1,r_2,r_3\}$ odgovara redom rotacijama za $0\sim3$ koraka, a njihovi skupovi fiksnih točaka analiziraju se ovako:
    
    -   rotacija za nula koraka $r_0=(1)$: svih $6$ bojenja fiksne su točke;
    -   rotacija za jedan korak $r_1=(1234)$: fiksna točka zahtijeva da su sve perle iste boje, pa nema fiksnih točaka;
    -   rotacija za dva koraka $r_2=(13)(24)$: postoje dva područja koja se mogu neovisno obojiti, oba veličine $2$, a treba ih obojiti jedno crveno, a drugo plavo, pa je veličina skupa fiksnih točaka $2$;
    -   rotacija za tri koraka $r_3=(1432)$: isto kao kod rotacije za jedan korak, nema fiksnih točaka.
    
    Stoga je prema Burnsideovoj lemi broj bitno različitih bojenja
    
    $$
    \frac{6+0+2+0}{4}=2.
    $$

Iz ovog primjera može se izvući sljedeća metoda računanja. Kod zadataka s ograničenim brojem pojedinih boja također se cikluse svake permutacije iz grupe simetrija boje zasebno, ali broj uporaba svake boje mora biti točno jednak zadanom. Takvi kombinatorni zadaci obično nemaju eksplicitno rješenje; osim posebnih slučajeva koji se mogu izračunati [metodama kombinatorike](../combinatorics/combination.md), često ih treba rješavati kao [problem naprtnjače](../../dp/knapsack/basic.md).

Odgovor na ovakve zadatke prebrojavanja može se dati pomoću funkcija izvodnica. Za zadanu permutaciju $g$, ako je njezin [tip](../permutation.md#tip-permutacije) jednak $1^{\alpha_1}2^{\alpha_2}\cdots n^{\alpha_n}$, tj. ako ima $\alpha_k$ ciklusa duljine $k$, i ako se svaki ciklus može obojiti jednom od $m$ boja, tada je u funkciji izvodnici

$$
\prod_{k=1}^n\left(\sum_{i=1}^mx_i^k\right)^{\alpha_k}
$$

koeficijent uz monom $x_1^{\beta_1}x_2^{\beta_2}\cdots x_m^{\beta_m}$ upravo broj bojenja u kojima je boja $i$ upotrijebljena $\beta_i$ puta ($1\le i\le m$). Kombinatorno značenje izraza $\sum_{i=1}^mx_i^k$ u zagradi jest: za ciklus duljine $k$ broj bojenja koja boju $i$ upotrebljavaju $k$ puta jednak je $1$, a u ostalim slučajevima jednak je $0$; to upravo opisuje zahtjev da sve pozicije u istom ciklusu budu obojene jednako.

Za zadanu funkciju izvodnicu broja bojenja pod permutacijom $g$ primjenom Burnsideove leme na svaki monom dobivamo broj bitno različitih bojenja za svaku kombinaciju boja. Budući da je za svaki monom skup bojenja koje prebrojava njegov koeficijent zatvoren na djelovanje grupe $G$, a uzimanje prosjeka linearno je po koeficijentima, funkcija izvodnica broja bitno različitih bojenja jest

$$
\frac1{|G|}\sum_{g\in G}\prod_{k=1}^n\left(\sum_{i=1}^mx_i^k\right)^{\alpha_k}.
$$

Raspišemo li taj izraz, koeficijent uz svaki monom daje broj bitno različitih bojenja za zadanu kombinaciju boja.

U gornjem postupku funkcija izvodnica $\sum_{i=1}^mx_i^k$ za bojenje svakog ciklusa ni po čemu nije posebna i može se zamijeniti drugom funkcijom izvodnicom. Stoga vrijedi sljedeća opća inačica Pólyina teorema prebrojavanja.

???+ note "Ciklički indeks grupe permutacija"
    Za zadanu grupu permutacija $G$ **ciklički indeks** (cycle index) grupe $G$, koji se obično označava sa $Z_G$ ili $Z(G)$, definira se kao
    
    $$
    Z_G(t_1,t_2,\cdots,t_n)=\frac{1}{|G|}\sum_{g\in G}t_1^{c_1(g)}t_2^{c_2(g)}\cdots t_n^{c_n(g)},
    $$
    
    gdje je $c_k(g)$ broj ciklusa duljine $k$ u rastavu permutacije $g$ na cikluse, tj. $1^{c_1(g)}2^{c_2(g)}\cdots n^{c_n(g)}$ tip je permutacije $g$.

???+ note "Pólyin teorem prebrojavanja (težinska inačica)"
    Za zadano djelovanje grupe $G$ na skupu $X$, ako je broj bojenja svake točke zadan funkcijom izvodnicom $f(x_1,x_2,\cdots,x_m)$, tada je funkcija izvodnica broja bitno različitih bojenja skupa $X$ jednaka
    
    $$
    Z_G(f(x_1^1,x_2^1,\cdots,x_m^1),f(x_1^2,x_2^2,\cdots,x_m^2),\cdots,f(x_1^n,x_2^n,\cdots,x_m^n)),
    $$
    
    gdje je $Z_G(t_1,t_2,\cdots,t_n)$ ciklički indeks grupe $G$.

Ovdje, ako je funkcija izvodnica bojenja jedne pozicije $f(x_1,x_2,\cdots,x_m)$, tada je funkcija izvodnica bojenja ciklusa duljine $k$ jednaka $f(x_1^k,x_2^k,\cdots,x_m^k)$. To odražava činjenicu da, ako je neko bojenje fiksna točka zadane permutacije, sve pozicije u istom ciklusu moraju biti obojene istom bojom. Uvrstimo li u funkciju izvodnicu $x_i=1$, dobivamo gornju netežinsku inačicu Pólyina teorema prebrojavanja.

U iskazu teorema koristi se pojam cikličkog indeksa grupe permutacija. On ne ovisi o konkretnom zadatku bojenja. On opisuje strukturu grupe permutacija.

??? example "Drugo rješenje zadatka bojenja ogrlice s ograničenjem"
    Ciklički indeks grupe rotacija jest $\dfrac14\left(t_1^4+t_2^2+2t_4\right)$, funkcija izvodnica bojenja jedne točke jest $r+b$, pa je funkcija izvodnica svih bojenja
    
    $$
    \begin{aligned}
    F(r,b)&=\frac14\left((r+b)^4+(r^2+b^2)^2+2(r^4+b^4)\right)\\
    &=r^4+r^3b+2r^2b^2+rb^3+b^4.
    \end{aligned}
    $$
    
    Traženi broj jest koeficijent uz $r^2b^2$, tj. ukupno $2$ bitno različita bojenja. Usput, ovaj izraz daje i brojeve za druga ograničenja.

### Primjene

Težinska inačica Pólyina teorema prebrojavanja ima važnu ulogu u zadacima kombinatornog prebrojavanja. Ovdje kratko raspravljamo o njezinim primjenama, a općenitija rasprava nalazi se u [Simbolička metoda za kombinatorne probleme](../poly/symbolic-method.md#ograničene-konstrukcije).

???+ example "Dijamantna ogrlica"
    Imamo ogrlicu s ukupno četiri jednake perle, a na svaku perlu može se umetnuti nekoliko dijamanata. Ako imamo četiri dijamanta, koliko ukupno ima bitno različitih načina umetanja dijamanata? (Ako se dva rasporeda dijamanata mogu dovesti do podudaranja rotacijom ogrlice, smatramo ih jednakima.)

??? example "Rješenje i analiza"
    Grupa simetrija ogrlice ista je kao prije. Ne uzmemo li u obzir ograničenje ukupnog broja dijamanata, funkcija izvodnica rasporeda dijamanata na jednoj poziciji jest
    
    $$
    f(x)=1+x+x^2+\cdots=\sum_{i=0}^\infty x^i=\frac{1}{1-x}.
    $$
    
    Primjenom težinske inačice Pólyina teorema prebrojavanja dobivamo da je funkcija izvodnica svih rasporeda dijamanata
    
    $$
    \begin{aligned}
    F(x)&=\frac14\left(f(x)^4+f(x^2)^2+2f(x^4)\right)\\
    &=1+x+3x^2+5x^3+10x^4+\cdots.
    \end{aligned}
    $$
    
    Stoga je traženi broj rasporeda dijamanata koeficijent uz $x^4$, tj. ukupno $10$ rasporeda. Kao provjera, nabrajanjem se vidi da su to redom
    
    $$
    4000,3100,3010,3001,2200,2020,2110,2101,2011,1111.
    $$
    
    Ovdje svaka skupina od četiri znamenke označava broj dijamanata na pojedinoj perli.

Ovaj primjer pokazuje da je raspon zadataka koje težinska inačica Pólyina teorema prebrojavanja može riješiti znatno širi od zadataka prebrojavanja bojenja. Ona daje način da se prebrojavanje na jednoj točki proširi na prebrojavanje bitno različitih konfiguracija cijele strukture. Zadaci bojenja samo su poseban slučaj takvih zadataka.

## Uobičajene grupe simetrija

Jedna od teškoća u zadacima vezanima uz Pólyino prebrojavanje jest analiza strukture grupe permutacija. Ovdje kratko raspravljamo o strukturi uobičajenih grupa simetrija i opisujemo ih njihovim cikličkim indeksima. Treba imati na umu da za grupu simetrija iste strukture, ako se razlikuje skup objekata na koje djeluje, razlikuje se i odgovarajuće [djelovanje grupe](../algebra/group-theory.md#群作用), pa se razlikuju i njihovi permutacijski prikazi. Primjerice, djelovanja grupe simetrija kocke na njezine vrhove, bridove i strane odgovaraju redom grupi permutacija vrhova, grupi permutacija bridova i grupi permutacija strana kocke; brojevi vrhova, bridova i strana međusobno se razlikuju, pa se, naravno, razlikuju i te grupe permutacija i odgovarajući ciklički indeksi. Zato se pri rješavanju konkretnih zadataka ne smije zanemariti na koje objekte grupa djeluje.

??? info "Odnos grupe simetrija i grupe permutacija"
    Iako su ta dva pojma vrlo slična, oni nipošto nisu isti objekt. Jezikom teorije grupa: za zadanu grupu simetrija $G$ i njezino djelovanje na skupu $X$ permutacijski prikaz djelovanja grupe zapravo daje homomorfizam $\varphi$ iz grupe $G$ u simetričnu grupu $S_X$, a taj je permutacijski prikaz u kontekstu kombinatornog prebrojavanja obično vjeran, tj. $\ker\varphi=\{e\}$, pa je homomorfizam $\varphi$ zapravo ulaganje grupe $G$ u grupu $S_X$. Grupa permutacija u ovom članku slika je tog ulaganja, tj. $\varphi(G)$, i izomorfna je samoj grupi simetrija $G$. Stoga je za grupu simetrija $G$ iste strukture, ako se djelovanja grupe odaberu različito, ona izomorfna različitim grupama permutacija $\varphi(G)$, pa ima i različite cikličke indekse (ciklički indeksi izomorfnih grupa permutacija ne moraju biti jednaki).

Za zadanu strukturu njezina grupa simetrija skup je svih operacija koje je preslikavaju na samu sebe. Ona nužno zadovoljava sljedeće uvjete:

-   uzastopna primjena dviju operacija simetrije na zadanu strukturu može se smatrati primjenom neke druge operacije simetrije, tj. skup operacija simetrije zatvoren je na kompoziciju;
-   kompozicija operacija simetrije je asocijativna;
-   postoji identična operacija simetrije, tj. i to da zadana struktura ostane nepromijenjena smatra se operacijom;
-   svaka operacija ima inverznu operaciju koja poništava učinak zadane operacije.

[Grupa](../algebra/basic.md#群) je apstrakcija svih pojmova koji zadovoljavaju te uvjete. Rasprava o strukturi grupa glavni je predmet proučavanja [teorije grupa](../algebra/group-theory.md). Ovdje se analiza uglavnom usredotočuje na grupe simetrija, a rasprava o njihovoj strukturi uglavnom koristi geometrijsko gledište. Navedeni su uobičajeni primjeri iz kojih bi čitatelj trebao usvojiti uobičajene načine razmišljanja pri analizi ovakvih zadataka.

### Ciklička grupa

Za zadani pravilni $n$-terokut grupa simetrija koju čine sve njegove rotacije naziva se cikličkom grupom (cyclic group) i označava se s $C_n$. Označimo li rotaciju za $(360/n)^\circ$ u smjeru suprotnom od kazaljke na satu s $r$, elementi grupe $C_n$ mogu se zapisati kao

$$
C_n=\{e,r,r^2,\cdots,r^{n-1}\}.
$$

Ovdje $r^k$ označava rezultat $k$-strukog ponavljanja operacije $r$, tj. rotaciju za $(360k/n)^\circ$ u smjeru suprotnom od kazaljke na satu, a $e=r^0$ označava identičnu transformaciju.

Bez obzira na to promatramo li djelovanje cikličke grupe na skupu svih vrhova ili na skupu svih bridova pravilnog $n$-terokuta, njezin je permutacijski prikaz isti. Analizirajmo permutacijski prikaz djelovanja grupe na primjeru skupa svih vrhova. Njezin je ciklički indeks

$$
Z(C_n)=\frac1n\sum_{d\mid n}\varphi(d)t_{d}^{n/d}.
$$

Ovdje je $\varphi(\cdot)$ [Eulerova funkcija](../number-theory/euler-totient.md) iz teorije brojeva.

Uzimaju li se u obzir samo rotacije, grupa simetrija ogrlice duljine $n$ upravo je $C_n$.

??? note "Analiza"
    Neka je skup vrhova u smjeru suprotnom od kazaljke na satu označen s $\{0,1,\cdots,n-1\}$; tada je $r^k(i)=(i+k)\bmod n$. Skup vrhova u ciklusu kojem pripada vrh $i$ jest
    
    $$
    \{(i+\ell k)\bmod n:\ell\in\mathbf Z\}.
    $$
    
    Očito je $i\equiv i+\ell k\pmod n$ ako i samo ako
    
    $$
    \frac{n}{\gcd(k,n)}\mid\ell.
    $$
    
    To znači da je duljina ciklusa kojem pripada bilo koji vrh $i$ jednaka $\dfrac{n}{\gcd(k,n)}$. Stoga permutacija $r^k$ ima $\gcd(k,n)$ ciklusa jednake duljine. Grupiramo li slične članove u izrazu za ciklički indeks: za zadani $d\mid n$ postoji ukupno $\varphi(d)$ vrijednosti $k$ za koje je $\gcd(k,n)=n/d$, a svima njima odgovaraju monomi oblika $t_d^{n/d}$, pa se dobiva gornji izraz za ciklički indeks.

### Diedarska grupa

Za zadani pravilni $n$-terokut sve njegove rotacije i zrcaljenja s obzirom na osi simetrije također čine grupu simetrija; ona se naziva diedarskom grupom (dihedral group) i označava se s $D_{2n}$. Označimo li rotaciju za $(360/n)^\circ$ u smjeru suprotnom od kazaljke na satu s $r$, a zrcaljenje s obzirom na neku zadanu os simetrije (npr. pravac kroz središte i neki vrh) sa $s$, operacije grupe $D_{2n}$ mogu se zapisati kao

$$
D_{2n}=\{e,r,\cdots,r^{n-1},s,sr,\cdots,sr^{n-1}\}.
$$

Ovdje je $r^k$ i dalje rotacija, a $sr^k$, iako označava najprije $k$ rotacija pa zatim zrcaljenje s obzirom na zadanu os simetrije, može se ekvivalentno shvatiti kao zrcaljenje s obzirom na neku drugu os simetrije. Stoga grupa $D_{2n}$ sadrži ukupno $1$ identičnu transformaciju, $(n-1)$ rotacija i $n$ zrcaljenja. Njezina djelovanja na skupu vrhova i na skupu bridova također imaju jednak ciklički indeks[^dihedral-edge], tj.

$$
Z(D_{2n})=\frac12Z(C_n)+
\begin{cases}
\dfrac12t_1t_2^k,&n=2k+1,\\
\dfrac14\left(t_1^2t_2^{k-1}+t_2^k\right),&n=2k.
\end{cases}
$$

??? note "Analiza"
    Analiza skupa rotacija $r^k$ (uključujući identičnu transformaciju) u grupi $D_{2n}$ potpuno je ista kao kod cikličke grupe $C_n$; ključna je analiza preostalih zrcaljenja. Pritom treba razlikovati slučajeve prema parnosti broja vrhova $n$.
    
    Kad je $n=2k+1$, osi simetrije svih zrcaljenja spajaju vrh s polovištem nasuprotnog brida; takvih osi simetrije ima ukupno $n$. Nakon svakog zrcaljenja vrh na osi simetrije ostaje na mjestu, a ostali se vrhovi zamjenjuju u parovima, pa postoji $1$ fiksna točka ($1$‑ciklus) i $k$ $2$‑ciklusa.
    
    Kad je $n=2k$, postoje dvije vrste osi simetrije. Polovica osi simetrije spaja nasuprotne vrhove; zrcaljenje s obzirom na takvu os ostavlja dva vrha na osi simetrije na mjestu, a ostale vrhove zamjenjuje u parovima, pa postoje $2$ fiksne točke ($1$‑ciklusi) i $(k-1)$ $2$‑ciklusa. Druga polovica osi simetrije spaja polovišta nasuprotnih bridova; zrcaljenje s obzirom na takvu os sve vrhove zamjenjuje u parovima, pa postoji $k$ $2$‑ciklusa.
    
    Na temelju ove analize može se zapisati gornji izraz za ciklički indeks.

### Simetrična grupa

Za zadanih $n$ elemenata sve permutacije na njima čine grupu koja se naziva simetričnom grupom (symmetric group) stupnja $n$ i označava se sa $S_n$. Ona opisuje sve simetrije koje tih $n$ elemenata može imati. Ona je ujedno permutacijski prikaz djelovanja tih operacija simetrije na skupu elemenata.

Prema analizi u članku [Permutacije](../permutation.md#tip-permutacije) njezin je ciklički indeks

$$
Z(S_n)=\sum_{\alpha_1+2\alpha_2+\cdots+n\alpha_n=n}\frac{t_1^{\alpha_1}t_2^{\alpha_2}\cdots t_n^{\alpha_n}}{1^{\alpha_1}2^{\alpha_2}\cdots n^{\alpha_n}\alpha_1!\alpha_2!\cdots\alpha_n!}.
$$

Ovdje je iskorišteno to da je broj permutacija tipa $1^{\alpha_1}2^{\alpha_2}\cdots n^{\alpha_n}$ jednak

$$
\frac{n!}{1^{\alpha_1}2^{\alpha_2}\cdots n^{\alpha_n}\alpha_1!\alpha_2!\cdots\alpha_n!}.
$$

On zadovoljava rekurzivnu relaciju

$$
Z(S_n)=\frac1n\sum_{k=1}^nt_kZ(S_{n-k}),
$$

a početni je uvjet rekurzije $Z(S_0)=1$. Kombinatorno značenje te rekurzivne relacije jest: da bismo konstruirali permutaciju $n$ elemenata, možemo najprije odabrati duljinu $k$ ciklusa kojem pripada točka $n$, a zatim konstruirati permutaciju na skupu preostalih $(n-k)$ elemenata.

Za zadani potpuni graf s $n$ vrhova njegova grupa simetrija upravo je $S_n$. Ciklički indeks njezina djelovanja na skupu svih vrhova dan je gornjim $Z(S_n)$. No permutacijski prikaz njezina djelovanja na skupu svih bridova nije isti. Primjerice, već se veličine skupova razlikuju: broj svih bridova jest $n(n-1)/2$. Za slučaj bridova potrebna je dodatna analiza. Ovdje dajemo jednostavan primjer, a opći slučaj može se naći u zadacima za vježbu.

???+ example "Prebrojavanje neusmjerenih jednostavnih grafova"
    Izračunajte broj neusmjerenih jednostavnih grafova s $4$ vrha do na izomorfizam.

??? example "Rješenje"
    To je ekvivalentno bojenju bridova potpunog grafa s $4$ vrha dvjema bojama, pri čemu se traži broj bitno različitih bojenja. Grupa simetrija jest $S_4$; analizirajmo sada ciklički indeks njezine grupe permutacija bridova $S_4^{(2)}$. Označimo četiri vrha s $a,b,c,d$, a šest bridova numerirajmo redom $1=ab$, $2=bc$, $3=cd$, $4=da$, $5=ac$, $6=bd$.
    
    -   Identična transformacija ($1$ komad): bridovi također ostaju na mjestu, pa je odgovarajući monom $1\cdot t_1^6$;
    -   Zamjena dvaju vrhova ($6$ komada): pretpostavimo da zamjenjujemo $a$ i $b$; tada bridovi $1$ i $3$ ostaju na mjestu, dok se bridovi $2$ i $5$ zamjenjuju te bridovi $4$ i $6$ zamjenjuju, pa je odgovarajući monom $6t_1^2t_2^2$;
    -   Ciklička zamjena triju vrhova ($8$ komada): pretpostavimo da je ciklus $(abc)$; tada se bridovi $1,2,5$ među njima također ciklički zamjenjuju, a bridovi $4,6,3$ koji ih spajaju s četvrtim vrhom $d$ također se ciklički zamjenjuju, pa je odgovarajući monom $8t_3^2$;
    -   Zamjena dvaju parova vrhova ($3$ komada): pretpostavimo da se zamjenjuju vrhovi $a$ i $b$ te vrhovi $c$ i $d$; tada bridovi $1$ i $3$ ostaju na mjestu, dok se bridovi $2$ i $4$ zamjenjuju te bridovi $5$ i $6$ zamjenjuju, pa je odgovarajući monom $3t_1^2t_2^2$;
    -   Ciklička zamjena četiriju vrhova ($6$ komada): pretpostavimo da je ciklus $(abcd)$; tada se bridovi $1,2,3,4$ između susjednih vrhova također ciklički zamjenjuju, a bridovi $5,6$ između nasuprotnih vrhova istodobno se zamjenjuju, pa je odgovarajući monom $6t_2t_4$.
    
    Stoga je ciklički indeks grupe permutacija bridova
    
    $$
    Z(S_4^{(2)})=\frac{1}{24}(t_1^6+9t_1^2t_2^2+8t_3^2+6t_2t_4).
    $$
    
    Prema Pólyinu teoremu prebrojavanja broj neusmjerenih jednostavnih grafova s $4$ vrha do na izomorfizam jest
    
    $$
    \frac{2^6+9\times 2^4+8\times 2^2+6\times 2^2}{24} = 11.
    $$

### Poliedarske grupe

Poliedarska grupa (polyhedral group) grupa je simetrija pravilnog poliedra. Postoji samo pet pravilnih poliedara: pravilni tetraedar, kocka, pravilni oktaedar, pravilni dodekaedar i pravilni ikosaedar. Zamijenimo li vrhove i strane uz očuvanje odnosa susjedstva među vrhovima, bridovima i stranama, dobivamo dualni pravilni poliedar. Pritom je pravilni tetraedar dualan samom sebi, kocka je dualna pravilnom oktaedru, a pravilni dodekaedar dualan je pravilnom ikosaedru. Pomoću dualnosti može se pojednostaviti rasprava o njihovim grupama simetrija.

Uzmemo li u obzir samo rotacije koje se mogu izvesti u trodimenzionalnom prostoru, postoje samo tri takve grupe simetrija.

-   Tetraedarska grupa (tetrahedral group), tj. grupa simetrija pravilnog tetraedra:

    -   identična transformacija;
    -   rotacije za $120^\circ$ i $240^\circ$ oko osi kroz vrh i središte nasuprotne strane;
    -   rotacija za $180^\circ$ oko osi kroz polovišta nasuprotnih bridova.

    Ukupno $1+2\times4+1\times3=12$ operacija simetrije.

    Ciklički indeksi odgovarajućih grupa permutacija jesu sljedeći.

    -   Grupa permutacija vrhova i grupa permutacija strana: $\dfrac1{12}\left(t_1^4+8t_1t_3+3t_2^2\right)$;
    -   grupa permutacija bridova: $\dfrac1{12}\left(t_1^6+8t_3^2+3t_1^2t_2^2\right)$.

-   Oktaedarska grupa (octahedral group), tj. grupa simetrija kocke (i pravilnog oktaedra):

    -   identična transformacija;
    -   rotacije za $120^\circ$ i $240^\circ$ oko osi kroz nasuprotne vrhove;
    -   rotacija za $180^\circ$ oko osi kroz polovišta nasuprotnih bridova;
    -   rotacije za $90^\circ$, $180^\circ$ i $270^\circ$ oko osi kroz središta nasuprotnih strana.

    Ukupno $1+2\times 4+1\times 6+3\times 3=24$ operacije simetrije.

    Ciklički indeksi odgovarajućih grupa permutacija kocke jesu sljedeći.

    -   Grupa permutacija vrhova: $\dfrac{1}{24}\left(t_1^8+8t_1^2t_3^2+9t_2^4+6t_4^2\right)$;
    -   grupa permutacija bridova: $\dfrac{1}{24}\left(t_1^{12}+8t_3^4+6t_1^2t_2^5+6t_4^3+3t_2^6\right)$;
    -   grupa permutacija strana: $\dfrac{1}{24}\left(t_1^6+8t_3^2+6t_2^3+6t_1^2t_4+3t_1^2t_2^2\right)$.

    Grupe permutacija pravilnog oktaedra slične su, samo treba zamijeniti uloge vrhova i strana.

-   Ikosaedarska grupa (icosahedral group), tj. grupa simetrija pravilnog dodekaedra (i pravilnog ikosaedra):

    -   identična transformacija;
    -   rotacije za $120^\circ$ i $240^\circ$ oko osi kroz nasuprotne vrhove;
    -   rotacija za $180^\circ$ oko osi kroz polovišta nasuprotnih bridova;
    -   rotacije za $72^\circ$, $144^\circ$, $216^\circ$ i $288^\circ$ oko osi kroz središta nasuprotnih strana.

    Ukupno $1+2\times 10+1\times 15+4\times 6=60$ operacija simetrije.

    Ciklički indeksi odgovarajućih grupa permutacija pravilnog dodekaedra jesu sljedeći.

    -   Grupa permutacija vrhova: $\dfrac{1}{60}\left(t_1^{20}+20t_1^2t_3^6+15t_2^{10}+24t_5^4\right)$;
    -   grupa permutacija bridova: $\dfrac{1}{60}\left(t_1^{30}+20t_3^{10}+15t_1^2t_2^{14}+24t_5^6\right)$;
    -   grupa permutacija strana: $\dfrac{1}{60}\left(t_1^{12}+20t_3^4+15t_2^6+24t_1^2t_5^2\right)$.

    Grupe permutacija pravilnog ikosaedra slične su, samo treba zamijeniti uloge vrhova i strana.

Ovdje su navedeni ciklički indeksi grupa permutacija koje djeluju zasebno na vrhove, bridove odnosno strane. Želimo li istodobno bojiti različite vrste objekata, treba zapisati zajednički ciklički indeks.

## Zadaci za vježbu

### Zadaci bojenja

U ovim zadacima dovoljno je analizirati strukturu grupe permutacija i primijeniti Pólyin teorem prebrojavanja.

-   [Luogu P4980【模板】Polya 定理 (Predložak: Pólyin teorem)](https://www.luogu.com.cn/problem/P4980)
-   [Luogu P2561 \[AHOI2002\] 黑白瓷砖 (Crno-bijele pločice)](https://www.luogu.com.cn/problem/P2561)
-   [TRANSP - Transposing is Fun](https://www.spoj.com/problems/TRANSP/)
-   [TRANSP2 - Transposing is Even More Fun](https://www.spoj.com/problems/TRANSP2/)
-   [Luogu P3307 \[SDOI2013\] 项链 (Ogrlica)](https://www.luogu.com.cn/problem/P3307)

Kad su kombinacije dostupnih boja ograničene, broj načina bojenja ciklusa treba odrediti DP-om po uzoru na problem naprtnjače ili kombinatornim metodama.

-   [Luogu P1446 \[HNOI2008\] Cards](https://www.luogu.com.cn/problem/P1446)
-   [UVA10601 Cubes](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1542)
-   [Luogu P4916 \[MtOI2018\] 魔力环 (Čarobni prsten)](https://www.luogu.com.cn/problem/P4916)

### Prebrojavanje grafova

Pólyin teorem prebrojavanja može se primijeniti na zadatke [prebrojavanja grafova](../combinatorics/graph-enumeration.md); teškoća je u tim zadacima nabrajanje grupe permutacija bridova grafa.

-   [SGU 282. Isomorphism](https://codeforces.com/problemsets/acmsguru/problem/99999/282)
-   [Luogu P4727 \[HNOI2009\] 图的同构计数 (Prebrojavanje izomorfizama grafova)](https://www.luogu.com.cn/problem/P4727)
-   [Luogu P4128 \[SHOI2006\] 有色图 (Obojeni grafovi)](https://www.luogu.com.cn/problem/P4128)

Druga vrsta zadataka prebrojavanja grafova na koje se može primijeniti Pólyin teorem prebrojavanja zahtijeva izravno baratanje funkcijama izvodnicama.

-   [LOJ 6538 烷基计数 加强版 加强版 (Prebrojavanje alkilnih skupina, pojačana pojačana inačica)](https://loj.ac/p/6538)
-   [LOJ 6512「雅礼集训 2018」烷烃计数 (Prebrojavanje alkana)](https://loj.ac/p/6512)
-   [Luogu P6597 烯烃计数 (Prebrojavanje alkena)](https://www.luogu.com.cn/problem/P6597)
-   [Luogu P5818 \[JSOI2011\] 同分异构体计数 (Prebrojavanje izomera)](https://www.luogu.com.cn/problem/P5818)

## Literatura i bilješke

-   [Pólya enumeration theorem - Wikipedia](https://en.wikipedia.org/wiki/P%C3%B3lya_enumeration_theorem)
-   [Notes on Pólya's Enumeration Theorem](https://www.diva-portal.org/smash/get/diva2:324594/FULLTEXT01.pdf)
-   [Cycle index - Wikipedia](https://en.wikipedia.org/wiki/Cycle_index)

[^perm-group]: Stoga se grupa simetrija $G$ može prikazati kao grupa permutacija na skupu $X$, tj. kao podgrupa simetrične grupe $S_X$.

[^g-act]: Strogo govoreći, riječ je o djelovanju podgrupe $\langle g\rangle\le G$.

[^dihedral-edge]: Za razliku od slučaja cikličke grupe, kad je $n$ paran, permutacijski prikazi ovih dvaju djelovanja grupe nisu isti: zrcaljenje s obzirom na os simetrije kroz nasuprotne vrhove na skupu vrhova ima tip $1^22^{k-1}$, a na skupu bridova $2^k$, dok je kod zrcaljenja s obzirom na os simetrije kroz polovišta nasuprotnih bridova upravo obrnuto. No broj osi simetrije tih dviju vrsta jednak je, pa se ciklički indeks nakon zbrajanja ne mijenja.
