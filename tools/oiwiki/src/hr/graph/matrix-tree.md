---
title: Teorem o matrici i stablima
---

Teorem o matrici i stablima (matrix-tree theorem, Kirchhoffov teorem) rješava problem prebrojavanja razapinjućih stabala grafa.

## Oznake u ovom članku

Grafovi u ovom članku, neusmjereni i usmjereni, smiju imati višestruke bridove, ali se podrazumijeva da nemaju petlji.

??? note "Slučaj s petljama"
    Petlje ne utječu na broj razapinjućih stabala; pri računanju Laplaceove matrice petlje se jednostavno ne broje. Međutim, pri prebrojavanju Eulerovih ciklusa BEST teoremom petlje se moraju uračunati u stupanj.

### Neusmjereni grafovi

Neka je $G$ neusmjereni graf s $n$ vrhova. Matricu stupnjeva $D(G)$ definiramo kao

$$
D_{ii}(G) = \mathrm{deg}(i),\ D_{ij} = 0,\ i\neq j.
$$

Neka je $\#e(i,j)$ broj bridova između vrhova $i$ i $j$; matricu susjedstva $A$ definiramo kao

$$
A_{ij}(G)=A_{ji}(G)=\#e(i,j),\ i\neq j.
$$

Laplaceovu matricu (zvanu i Kirchhoffova matrica) $L$ definiramo kao

$$
L(G) = D(G) - A(G).
$$

Broj svih razapinjućih stabala grafa $G$ označavamo $t(G)$.

### Usmjereni grafovi

Neka je $G$ usmjereni graf s $n$ vrhova. Matricu izlaznih stupnjeva $D^\mathrm{out}(G)$ definiramo kao

$$
D^\mathrm{out}_{ii}(G) = \mathrm{deg}^\mathrm{out}(i),\ D^\mathrm{out}_{ij} = 0,\ i\neq j.
$$

Analogno definiramo matricu ulaznih stupnjeva $D^\mathrm{in}(G)$.

Neka je $\#e(i,j)$ broj usmjerenih bridova iz vrha $i$ u vrh $j$; matricu susjedstva $A$ definiramo kao

$$
A_{ij}(G)=\#e(i,j),\ i\neq j.
$$

Izlaznu Laplaceovu matricu $L^\mathrm{out}$ definiramo kao

$$
L^\mathrm{out}(G) = D^\mathrm{out}(G) - A(G).
$$

Ulaznu Laplaceovu matricu $L^\mathrm{in}$ definiramo kao

$$
L^\mathrm{in}(G) = D^\mathrm{in}(G) - A(G).
$$

Broj svih razapinjućih stabala grafa $G$ usmjerenih prema korijenu $k$ označavamo $t^\mathrm{root}(G,k)$. Stablo usmjereno prema korijenu (in-arborescence) usmjereni je graf čiji je pripadni neusmjereni graf stablo i u kojem svi bridovi pokazuju prema roditelju.

Broj svih razapinjućih stabala grafa $G$ usmjerenih od korijena $k$ prema listovima označavamo $t^\mathrm{leaf}(G,k)$. Stablo usmjereno prema listovima (out-arborescence) usmjereni je graf čiji je pripadni neusmjereni graf stablo i u kojem svi bridovi pokazuju prema djetetu.

## Iskaz teorema

Teorem o matrici i stablima ima više oblika.

Definiramo $[n]=\{1,2,\cdots,n\}$, a podmatrica $A_{S,T}$ matrice $A$ je podmatrica dobivena odabirom elemenata $A_{i,j}\pod{i\in S,j\in T}$.

???+ note "Teorem 1 (teorem o matrici i stablima, neusmjereni graf, oblik s determinantom)"
    Za neusmjereni graf $G$ i proizvoljan $k$ vrijedi
    
    $$
    t(G) = \det L(G)_{[n]\setminus\{k\},[n]\setminus\{k\}}.
    $$
    
    Drugim riječima, svi glavni minori reda $n-1$ Laplaceove matrice neusmjerenog grafa jednaki su i svi su jednaki broju razapinjućih stabala grafa.

???+ note "Korolar 1 (teorem o matrici i stablima, neusmjereni graf, oblik sa svojstvenim vrijednostima)"
    Neka su $\lambda_1\ge\lambda_2\ge\cdots\ge\lambda_{n-1}\ge\lambda_n=0$ svih $n$ svojstvenih vrijednosti matrice $L(G)$. Tada vrijedi
    
    $$
    t(G) = \frac{1}{n}\lambda_1\lambda_2\cdots\lambda_{n-1}.
    $$

???+ note "Teorem 2 (teorem o matrici i stablima, usmjereni graf, stabla prema korijenu, oblik s determinantom)"
    Za usmjereni graf $G$ i proizvoljan $k$ vrijedi
    
    $$
    t^\mathrm{root}(G,k) = \det L^\mathrm{out}(G)_{[n]\setminus\{k\},[n]\setminus\{k\}}.
    $$
    
    Drugim riječima, glavni minor dobiven brisanjem $k$-tog retka i $k$-tog stupca izlazne Laplaceove matrice usmjerenog grafa jednak je broju stabala usmjerenih prema korijenu $k$.

Stoga, ako želimo prebrojati sva stabla usmjerena prema korijenu u grafu, dovoljno je proći sve korijene $k$ i zbrojiti $t^\mathrm{root}(G,k)$.

???+ note "Teorem 3 (teorem o matrici i stablima, usmjereni graf, stabla prema listovima, oblik s determinantom)"
    Za usmjereni graf $G$ i proizvoljan $k$ vrijedi
    
    $$
    t^\mathrm{leaf}(G,k) = \det L^\mathrm{in}(G)_{[n]\setminus\{k\},[n]\setminus\{k\}}.
    $$
    
    Drugim riječima, glavni minor dobiven brisanjem $k$-tog retka i $k$-tog stupca ulazne Laplaceove matrice usmjerenog grafa jednak je broju stabala usmjerenih prema listovima s korijenom $k$.

Stoga, ako želimo prebrojati sva stabla usmjerena prema listovima u grafu, dovoljno je proći sve korijene $k$ i zbrojiti $t^\mathrm{leaf}(G,k)$.

???+ note "Napomena"
    Stabla usmjerena prema korijenu zovu se i „ulazna stabla” (in-arborescence), ali budući da se za njihovo prebrojavanje koriste izlazni stupnjevi, da ne bi došlo do zabune između $\mathrm{in}$ i $\mathrm{out}$, koristimo naziv „prema korijenu”.

## Dokaz teorema

Primijetimo da su oblici gornjih teorema vrlo slični; ovdje dajemo jedinstven način dokazivanja i ujedno proširujemo prethodne rezultate na težinske grafove.

Grubi tijek dokaza je sljedeći:

-   najprije, svi se slučajevi mogu svesti na prebrojavanje stabala usmjerenih prema korijenu u usmjerenom grafu;
-   jezikom matrica dajemo nužan i dovoljan uvjet da odabrani bridovi čine stablo usmjereno prema korijenu;
-   odabir bridova povezujemo s determinantom Laplaceove matrice pomoću Cauchy–Binetove formule;
-   na kraju, rezultat u obliku determinante pretvaramo u rezultat u obliku svojstvenih vrijednosti.

### Lema: Cauchy–Binetova formula

???+ note "Lema 1 (Cauchy–Binet)"
    Za matricu $A$ dimenzija $n\times m$ i matricu $B$ dimenzija $m\times n$ vrijedi
    
    $$
    \det(AB)=\sum_{S\subset[m];~|S|=n}\det A_{[n],S}\det B_{S,[n]},
    $$
    
    pri čemu znak sume znači da $S$ prolazi sve podskupove skupa $[m]$ veličine $n$. Ako je $n>m$, nužno je $\det(AB)=0$.

??? note "Dokaz (kombinatorni pogled)"
    Prema modelu zadatka [„NOI2021” Sjecišta puteva](https://loj.ac/p/3533), najprije razmotrimo sljedeće kombinatorno značenje determinante. Za matricu $C$ reda $n\times n$ konstruiramo usmjereni aciklički graf $G=(V,E)$. Skup vrhova je $V=[2]\times[n]\subset\mathbb R^2$, tj. dva stupca točaka u ravnini. Lijevi stupac označimo $L=\{l_i=(1,i):i\in[n]\}$, a desni $R=\{r_i=(2,i):i\in[n]\}$; skup usmjerenih bridova je $E=\{(l_i,r_j):i,j\in[n]\}$ s težinama $w(l_i,r_j)=C_{i,j}$. Podskup bridova $E^\sigma\subset E$ veličine $n$ zovemo skupinom puteva ako su mu svi početci međusobno različiti i svi završetci međusobno različiti. Očito su skupine puteva $E^\sigma$ u bijekciji s permutacijama $\sigma$ skupa $[n]$. Primijetimo da se, nacrtamo li skupinu puteva u ravnini, ti bridovi mogu međusobno sjeći, a broj sjecišta (s kratnostima) jednak je broju inverzija permutacije $\sigma$. Naime, bridovi $(l_i,r_{\sigma(i)})$ i $(l_j,r_{\sigma(j)})$ sijeku se ako i samo ako je $(i-j)(\sigma(i)-\sigma(j))< 0$, tj. ako je to inverzija. Radi jednostavnosti, parnost broja inverzija pripadne permutacije, tj. parnost broja sjecišta skupine puteva, zovemo parnošću skupine puteva. Dakle, ako skupine puteva brojimo s težinama i od broja skupina s parnim brojem sjecišta oduzmemo broj skupina s neparnim brojem sjecišta, dobivamo Leibnizov razvoj determinante:
    
    $$
    \det(C)=\sum_{\sigma\in S_n}\mathrm{sgn}(\sigma)\prod_{i\in[n]}C_{i,\sigma(i)},
    $$
    
    gdje je $S_n$ grupa permutacija skupa $[n]$, a $\mathrm{sgn}(\sigma)$ predznak permutacije $\sigma$ (jednak $1$ ako je broj inverzija paran, a $-1$ ako je neparan).
    
    Kad razumijemo kombinatorno značenje determinante, Cauchy–Binetovu formulu možemo dokazati sljedećim kombinatornim modelom. Za matricu $A$ reda $n\times m$ i matricu $B$ reda $m\times n$ konstruiramo usmjereni aciklički graf $G=(V,E)$. Skup vrhova je $V=L\cup D\cup R$, gdje je $L=\{l_i=(1,i):i\in[n]\}$, $D=\{d_i=(2,i):i\in[m]\}$ i $R=\{r_i=(3,i):i\in[n]\}$; skup usmjerenih bridova je $E=E_L\cup E_R$, gdje je $E_L=\{(l_i,d_j):i\in[n],j\in[m]\}$ i $E_R=\{(d_j,r_i):j\in[m],i\in[n]\}$, s težinama redom $w(l_i,d_j)=A_{i,j}$ i $w(d_j,r_i)=B_{j,i}$. Opet promatramo skupine puteva od $L$ preko $D$ do $R$ (putevi u parovima nemaju zajedničkih vrhova), brojimo ih s težinama i od broja skupina s parnim brojem sjecišta oduzimamo broj skupina s neparnim brojem sjecišta. Pokazat ćemo da lijeva i desna strana Cauchy–Binetove formule računaju tu veličinu na dva različita načina.
    
    Za lijevu stranu, na temelju opisanog grafa $G$ konstruiramo novi graf $G'$ sa skupom vrhova $V'=L\cup R$ i skupom bridova $E'=\{(l_i,r_j):i,j\in[n]\}$, pri čemu bridu $(l_i,r_j)$ pridružimo težinu $\sum_{k\in[m]}A_{i,k}B_{k,j}$, tj. težinski broj jednostavnih puteva od $l_i$ do $r_j$ u izvornom grafu $G$. Ta je težina upravo $(AB)_{i,j}$. To odgovara sažimanju troslojnog grafa u dvoslojni. Međutim, skupine puteva (brojane s težinama) u dvoslojnom grafu $G'$ nisu u bijekciji sa skupinama puteva u troslojnom grafu $G$. Budući da svaki put u dvoslojnom grafu odgovara više jednostavnih puteva u troslojnom, pri brojanju skupina puteva u dvoslojnom grafu množimo težine, što odgovara uzimanju svih kombinacija pripadnih skupova puteva u troslojnom grafu, a to nužno uključuje slučajeve u kojima putevi dijele zajednički međuvrh. No parovi puteva koji dijele međuvrh ne doprinose konačnom rezultatu, jer za $i_1< i_2$, $j_1< j_2$ i proizvoljan međuvrh $d$ postoje dva para jednostavnih puteva $(l_{i_1}\rightarrow d\rightarrow r_{j_1}, l_{i_2}\rightarrow d\rightarrow r_{j_2})$ i $(l_{i_1}\rightarrow d\rightarrow r_{j_2}, l_{i_2}\rightarrow d\rightarrow r_{j_1})$, a parnosti brojeva sjecišta tih dviju skupina puteva u troslojnom grafu nužno su suprotne, jer su, gledamo li samo početke i završetke, te dvije skupine zamijenile završetke. Dakle, doprinosi puteva sa zajedničkim međuvrhom pri brojanju u sažetom dvoslojnom grafu međusobno se poništavaju u parovima. U preostalim slučajevima, ako su zadani početci i završetci dvaju puteva, parnost broja njihovih sjecišta ne ovisi o izboru međuvrhova (dok god nisu isti). Stoga sve skupine puteva izvornog grafa $G$ koje odgovaraju jednoj skupini puteva u $G'$ imaju istu parnost. Prema tome, $\det(AB)$ je jedan način računanja spomenute razlike brojeva skupina puteva.
    
    Desna strana odgovara prolasku svih mogućih kombinacija međuvrhova. Za proizvoljan skup međuvrhova $S\subset D=[m]$ s $|S|=n$ promatramo zasebno skupine puteva od $L$ do $S$ i od $S$ do $R$; spajanjem dobivamo skupine puteva od $L$ do $R$, a kompozicija permutacija prvih dviju skupina jednaka je permutaciji dobivene skupine, pa je umnožak parnosti prvih dviju skupina jednak parnosti dobivene skupine. Zato je razlika brojeva skupina puteva sa skupom međuvrhova $S$ upravo umnožak razlike za skupine od $L$ do $S$ i razlike za skupine od $S$ do $R$. Zbrajanjem po svim mogućim $S$ dobivamo desnu stranu, pa je i ona jednaka spomenutoj razlici brojeva skupina puteva.

??? note "Dokaz (algebarski pogled)"
    Gornji kombinatorni dokaz može se doslovno prevesti u algebarski. Ovdje umjesto toga dajemo drugi, tehnički zahtjevniji algebarski dokaz koji koristi nekoliko poznatih rezultata. Za $m< n$ determinanta je nula jer
    
    $$
    \mathrm{rank}(AB)\le \min\{\mathrm{rank}(A),\mathrm{rank}(B)\}\le m< n.
    $$
    
    Za $m=n$ Cauchy–Binetova formula kaže da je determinanta umnoška kvadratnih matrica jednaka umnošku njihovih determinanti.
    
    Za $m>n$ primijetimo da je
    
    $$
    x^{m-n}\det(xI_n+AB) = \det(xI_m+BA).
    $$
    
    Poznato je da je koeficijent uz $x^{n-k}$ u $\det(xI_n+C)$ jednak zbroju svih glavnih minora reda $k$ matrice $C$. Usporedbom koeficijenata na obje strane gornje jednakosti dobivamo
    
    $$
    \det(AB) = \sum_{S\subset[m];~|S|=n}\det (BA)_{S,S} = \sum_{S\subset[m];~|S|=n}\det B_{S,[n]}\det A_{[n],S} = \sum_{S\subset[m];~|S|=n}\det A_{[n],S}\det B_{S,[n]}.
    $$
    
    Druga jednakost koristi rezultat za slučaj $m=n$.

### Opis strukture grafa matricom incidencije

Neka je $G=(V,E)$ usmjereni graf s $n$ vrhova i $m$ bridova, u kojem brid $e$ ima težinu $w(e)$. Definiramo izlaznu matricu incidencije reda $m\times n$

$$
M^\mathrm{out}_{ij}=\begin{cases}
\sqrt{w(e_i)},&\exists u(e_i=(v_j,u)),\\
0,&\textrm{otherwise},
\end{cases}
$$

i ulaznu matricu incidencije reda $m\times n$

$$
M^\mathrm{in}_{ij}=\begin{cases}
\sqrt{w(e_i)},&\exists u(e_i=(u,v_j)),\\
0,&\textrm{otherwise}.
\end{cases}
$$

Svaki njihov redak zapisuje jedan brid: izlazna matrica incidencije $M^\mathrm{out}$ bilježi početak brida, a ulazna matrica incidencije $M^\mathrm{in}$ bilježi kraj brida.

Jednostavnim računom dobivamo

$$
D^\mathrm{out}(G) = (M^\mathrm{out})^T M^\mathrm{out},\ A(G) = (M^\mathrm{out})^T M^\mathrm{in},\ D^\mathrm{in}(G) = (M^\mathrm{in})^T M^\mathrm{in}.
$$

Odatle je

$$
L^\mathrm{out}(G) = (M^\mathrm{out})^T (M^\mathrm{out}-M^\mathrm{in}),\ L^\mathrm{in}(G) = (M^\mathrm{in}-M^\mathrm{out})^T M^\mathrm{in}.
$$

Cauchy–Binetova formula iz prethodnog odjeljka pokazuje da je glavni minor Laplaceove matrice zapravo zbroj po nizu podstruktura. Svaka podstruktura odražava svojstva pripadnog podgrafa.

???+ note "Lema 2"
    Za podskup vrhova $W\subseteq V$ i podskup bridova $S\subseteq E$ takve da je $|W|=|S|\le n$, ako je podgraf $T=(V,S)$ šuma usmjerena prema korijenima iz $V\setminus W$, tada je izraz
    
    $$
    \det(M^\mathrm{out}_{S,W})\det(M^\mathrm{out}_{S,W}-M^\mathrm{in}_{S,W})
    $$
    
    jednak $\prod_{e\in S}w(e)$, što označavamo $w(T)$; inače je taj izraz jednak nuli.

??? note "Dokaz"
    Bez smanjenja općenitosti neka je $w(e)=1$. Naime, po multilinearnosti determinante iz svakog retka svake determinante možemo izlučiti faktor $\sqrt{w(e)}$, a umnožak tih faktora je $w(T)$.
    
    Najprije analiziramo uvjete pod kojima su dva faktora jednaka nuli. Prvi faktor $\det(M^\mathrm{out}_{S,W})$ u svakom retku ima najviše jedan element različit od nule, i to $+1$. Ako je neki redak cijeli nula, ili ako dva retka imaju $+1$ u istom stupcu, determinanta je nužno nula. Dakle, determinanta je različita od nule ako i samo ako svaki redak i svaki stupac imaju točno jedan $+1$, tj. početak svakog brida iz $S$ leži u $W$ i svaki vrh iz $W$ početak je točno jednog brida iz $S$. Ako je $T$ šuma usmjerena prema korijenima iz $V\setminus W$, nužan je uvjet da svaki vrh osim korijena ima točno jednog roditelja, što osigurava da taj faktor nije nula; obrat ne mora vrijediti, jer nije zajamčeno da nema ciklusa, pa treba promotriti i drugi faktor. Napomena: krajevi bridova iz $S$ ne moraju biti u $W$.
    
    Pretpostavimo da je prvi faktor različit od nule; tada je podgraf $T$ šuma usmjerena prema korijenima ako i samo ako $T$ nema ciklusa. Drugi faktor $\det(M^\mathrm{out}_{S,W}-M^\mathrm{in}_{S,W})$ u svakom retku ima jedan $+1$, a može imati jedan ili nijedan $-1$. Za bridove čiji je kraj također u $W$: ako je kraj brida $e_i$ početak brida $e_j$, dodavanjem retka brida $e_j$ retku brida $e_i$ poništavamo $-1$ u retku $e_i$. Možemo si predočiti da taj redak sada opisuje jednostavan put $e_i$ pa $e_j$. Ako se u retku pojavio novi $-1$, to znači da je kraj brida $e_j$ također u $W$, a položaj tog $-1$ je kraj brida $e_j$; tada možemo pronaći brid koji počinje u kraju brida $e_j$ i opet ga dodati tom retku. Takav brid uvijek postoji, jer prethodni odlomak pokazuje da je svaki vrh iz $W$ početak točno jednog brida iz $S$. Postupak nastavljamo dok se u retku više ne pojavljuje $-1$, što odgovara dodavanju novih bridova jednostavnom putu $e_i\rightarrow e_j\rightarrow \cdots\rightarrow e_k$. Ako na kraju u retku ostane samo jedan $+1$, kraj brida $e_k$ nije u odabranom skupu vrhova $W$ i postupak završava; ako je posljednji dodani brid poništio postojeći $+1$, tj. u retku su ostale samo nule, kraj novog brida $e_k$ je početak početnog brida $e_i$, tj. pojavio se ciklus; ako postupak nikad ne završi, put je ušao u ciklus i redci bridova na tom ciklusu također postaju nula. Dakle, nužan i dovoljan uvjet da nema ciklusa jest da se determinanta gornjim operacijama može preoblikovati tako da svaki redak ima točno jedan $+1$. Budući da su položaji tih $+1$ početci bridova pripadnih redaka, dobivena je matrica zapravo $M^\mathrm{out}_{S,W}$, pa su determinante jednake.
    
    Ukupno, ako $T$ nije šuma usmjerena prema korijenima, tada je ili $\det(M^\mathrm{out}_{S,W})=0$ ili $\det(M^\mathrm{out}_{S,W}-M^\mathrm{in}_{S,W})=0$; inače su oba različita od nule i umnožak im je $\left(\det(M^\mathrm{out}_{S,W})\right)^2=1$.

### Teorem o matrici i stablima za težinske usmjerene grafove

Sada možemo dokazati glavni rezultat ovog članka. Svi prije navedeni oblici teorema posebni su slučajevi ovog teorema.

???+ note "Teorem 4 (teorem o matrici i stablima, težinski usmjereni graf, stabla prema korijenu, oblik s determinantom)"
    Za proizvoljan $k$ vrijedi
    
    $$
    \sum_{T\in\mathcal T^\mathrm{root}(G,k)}w(T)=\det L^\mathrm{out}(G)_{[n]\setminus\{k\},[n]\setminus\{k\}}.
    $$
    
    Ovdje je $\mathcal T^\mathrm{root}(G,k)$ skup razapinjućih stabala grafa $G$ usmjerenih prema korijenu $k$.

??? note "Dokaz"
    Neka je $W=[n]\setminus\{k\}$ skup preostalih vrhova bez vrha $k$. Po Cauchy–Binetovoj formuli desnu stranu možemo zapisati kao
    
    $$
    \det L^\mathrm{out}(G)_{W,W} = \sum_{S\subset[m];~|S|=n-1}\det(M^\mathrm{out}_{S,W})\det(M^\mathrm{out}_{S,W}-M^\mathrm{in}_{S,W}).
    $$
    
    Prolazeći sve $S$, po lemi 2 desna strana pribraja $w(T)$ ako i samo ako $T=(V,S)$ čini šumu usmjerenu prema korijenima iz $V\setminus W=\{k\}$, tj. ako je $T$ razapinjuće stablo usmjereno prema korijenu $k$.

Kad je $w(e)=1$, težina svakog stabla je $1$, pa je lijeva strana broj svih stabala, tj. $t^\mathrm{root}(G,k)$; time dobivamo teorem 2. Analogno se rezultat izravno prenosi na stabla usmjerena prema listovima, što daje teorem 3. Na kraju, za prebrojavanje razapinjućih stabala neusmjerenog grafa možemo primijeniti sljedeći korolar.

???+ note "Korolar 2 (teorem o matrici i stablima, težinski neusmjereni graf, oblik s determinantom)"
    Za neusmjereni graf $G$ i proizvoljan $k$ vrijedi
    
    $$
    \sum_{T\in\mathcal T(G)}w(T) = \det L(G)_{[n]\setminus\{k\},[n]\setminus\{k\}}.
    $$
    
    Ovdje je $\mathcal T(G)$ skup razapinjućih stabala grafa $G$. To također pokazuje da su svi glavni minori reda $(n-1)$ matrice $L(G)$ jednaki.

??? note "Dokaz"
    Za neusmjereni graf $G=(V,E)$ konstruiramo usmjereni graf $G'=(V,E')$, gdje je $E'=\{(v_i,v_j):(v_i,v_j)\in E\}\cup\{(v_j,v_i):(v_i,v_j)\in E\}$, tj. svaki neusmjereni brid grafa $G$ razdvojimo na dva suprotno usmjerena brida. Za proizvoljan $k$, razapinjuća stabla grafa $G'$ usmjerena prema korijenu $k$ u bijekciji su s razapinjućim stablima grafa $G$. Od prvih prema drugima dovoljno je ukloniti orijentaciju bridova i izbor korijena; od drugih prema prvima dovoljno je, krenuvši od odabranog korijena $k$, brid po brid orijentirati prema korijenu. Dakle,
    
    $$
    \sum_{T\in\mathcal T(G)}w(T) = \sum_{T\in\mathcal T^\mathrm{root}(G',k)}w(T) = \det L^\mathrm{out}(G')_{[n]\setminus\{k\},[n]\setminus\{k\}} = \det L(G)_{[n]\setminus\{k\},[n]\setminus\{k\}}.
    $$
    
    Ovdje smo koristili $L^\mathrm{out}(G')=L(G)$, što se lako izravno provjeri.

### Oblik sa svojstvenim vrijednostima

I ovdje najprije promatramo rezultat za usmjerene grafove.

???+ note "Teorem 5"
    Za usmjereni graf $G$ definiramo polinom više varijabli
    
    $$
    \chi(x_1,\cdots,x_n)=\det(\mathrm{diag}(x_1,\cdots,x_n)-L^\mathrm{out}(G)).
    $$
    
    Ovdje je $\mathrm{diag}(x_1,\cdots,x_n)$ dijagonalna matrica s $x_1,\cdots,x_n$ na dijagonali. Tada je
    
    $$
    (-1)^{n-r}[x_{k_1}\cdots x_{k_r}]\chi(x_1,\cdots,x_n)
    $$
    
    jednako (težinskom) broju šuma grafa $G$ usmjerenih prema korijenima $\{k_1,\cdots,k_r\}$.

??? note "Dokaz"
    Po uzoru na dokaz teorema 4, primijetimo da je za $W=[n]\setminus\{k_1,\cdots,k_r\}$ izraz iz teorema jednak $\det L^\mathrm{out}(G)_{W,W}$ (dovoljno je pogledati Leibnizov razvoj determinante). Po Cauchy–Binetovoj formuli to je jednako
    
    $$
    \det L^\mathrm{out}(G)_{W,W} = \sum_{S\subset[m];~|S|=n-r}\det(M^\mathrm{out}_{S,W})\det(M^\mathrm{out}_{S,W}-M^\mathrm{in}_{S,W}).
    $$
    
    Prolazeći sve $S$, po lemi 2 desna strana pribraja $w(T)$ ako i samo ako $T=(V,S)$ čini šumu usmjerenu prema korijenima iz $V\setminus W=\{k_1,\cdots,k_r\}$.

Uvrstimo li $x$ za sve nepoznanice, dobivamo karakteristični polinom Laplaceove matrice

$$
P(x) = \det(xI-L^\mathrm{out}(G)) = \chi(x,\cdots,x).
$$

???+ note "Lema 3"
    Laplaceova matrica $L^\mathrm{out}(G)$ ima barem jednu svojstvenu vrijednost jednaku nuli.

??? note "Dokaz"
    Dovoljno je dokazati da joj je determinanta nula. Po uzoru na dokaze teorema 4 i 5, uzmimo $W=[n]$ (tj. skup korijena je prazan); vrijednost te determinante trebala bi biti broj šuma usmjerenih prema korijenima koje se sastoje od nula stabala. Takvih nema, pa je determinanta nula.

???+ note "Korolar 3"
    Za usmjereni graf $G$, zbroj težina svih šuma usmjerenih prema korijenima koje se sastoje od $k$ stabala jednak je koeficijentu
    
    $$
    (-1)^{n-k}[x^k]P(x).
    $$

??? note "Dokaz"
    Dovoljno je zbrojiti po svim mogućim izborima $k$ korijena.

Definiramo $k$-razapinjuću šumu kao razapinjući podgraf grafa koji ima $k$ komponenti povezanosti i nema ciklusa.

???+ note "Korolar 4"
    Neka je $\mathcal T_k(G)$ skup $k$-razapinjućih šuma neusmjerenog grafa $G$, a $P(x)=\det(xI-L(G))$ karakteristični polinom njegove Laplaceove matrice. Tada je
    
    $$
    \sum_{T\in\mathcal T_k(G)}w(T)Q(T) = (-1)^{n-k}[x^k]P(x).
    $$
    
    Ovdje je $Q(T)$ umnožak brojeva vrhova svih komponenti povezanosti šume $T$. Posebno, za $k=1$ je $Q(T)=n$, pa je
    
    $$
    n\sum_{T\in\mathcal T(G)}w(T) = \lambda_1\lambda_2\cdots\lambda_{n-1}.
    $$

??? note "Dokaz"
    Po uzoru na dokaz korolara 2, možemo izravno primijeniti korolar 3. Svaka šuma od $k$ stabala usmjerenih prema korijenima u usmjerenom grafu odgovara jednoj $k$-razapinjućoj šumi u neusmjerenom grafu. Međutim, budući da svaka $k$-razapinjuća šuma $T$ ima $Q(T)$ načina odabira korijena, ona se pojavljuje u $Q(T)$ usmjerenih šuma usmjerenih prema korijenima.

## Primjene

### Cayleyjeva formula

???+ note "Korolar 5 (Cayley)"
    Označenih nekorijenskih stabala veličine $n$ ima $n^{n-2}$.

??? note "Dokaz"
    Ekvivalentno, dovoljno je pokazati da potpuni graf s $n$ vrhova ima $n^{n-2}$ razapinjućih stabala. Zapišimo Laplaceovu matricu
    
    $$
    L(G) = \left(\begin{matrix} n-1 & -1 & \cdots & -1 \\ -1 & n-1 & \cdots & -1 \\ \vdots & \vdots & \ddots & \vdots \\ -1 & -1 & \cdots & n-1  \end{matrix}\right)_{n\times n}.
    $$
    
    Računajući bilo koji njezin glavni minor dobivamo
    
    $$
    \det(nI_{n-1}-{\bf 1}{\bf 1}^T) = n^{n-1}\det(I_{n-1}-n^{-1}{\bf 1}{\bf 1}^T) = n^{n-1}(1-n^{-1}{\bf 1}^T{\bf 1}) = n^{n-1}(1-(n-1)/n) = n^{n-2}.
    $$
    
    Primjenom teorema 1 slijedi tvrdnja.

### BEST teorem

Preduvjeti: [Eulerovi grafovi](./euler.md)

Ovaj teorem povezuje broj Eulerovih ciklusa usmjerenog Eulerovog grafa s brojem njegovih stabala usmjerenih prema korijenu i time rješava problem prebrojavanja Eulerovih ciklusa u usmjerenim grafovima. Napomena: prebrojavanje Eulerovih ciklusa u proizvoljnom neusmjerenom grafu je #P-potpun problem.

Pri implementaciji najprije treba provjeriti je li zadani graf Eulerov, ukloniti sve vrhove stupnja nula, zatim izgraditi graf i izračunati broj stabala usmjerenih prema korijenu te po BEST teoremu dobiti broj Eulerovih ciklusa. Napomena: ako se traži broj Eulerovih ciklusa koji počinju u zadanom vrhu, odgovor treba još pomnožiti izlaznim stupnjem tog vrha, što odgovara izboru prvog brida ciklusa.

Prije dokaza BEST teorema trebamo sljedeći rezultat.

???+ note "Svojstvo (kriterij postojanja Eulerovog ciklusa u usmjerenom grafu)"
    Usmjereni graf ima Eulerov ciklus ako i samo ako su vrhovi stupnja različitog od nule jako povezani i svaki vrh ima jednak izlazni i ulazni stupanj.

Za Eulerove grafove, budući da su izlazni i ulazni stupnjevi jednaki, možemo izostaviti gornje indekse i pisati $\mathrm{deg}(v)$. BEST teorem glasi:

???+ note "Teorem 6 (BEST teorem)"
    Neka je $G$ usmjereni Eulerov graf i $k$ proizvoljan vrh. Tada je broj različitih Eulerovih ciklusa $\mathrm{ec}(G)$ grafa $G$ jednak
    
    $$
    \mathrm{ec}(G) = t^\mathrm{root}(G,k)\prod_{v\in V}(\deg (v) - 1)!.
    $$
    
    To ujedno pokazuje da za bilo koja dva vrha $k, k'$ Eulerovog grafa $G$ vrijedi $t^\mathrm{root}(G,k)=t^\mathrm{root}(G,k')$.

??? note "Dokaz"
    Osnovna ideja dokaza je uspostaviti korespondenciju između Eulerovih ciklusa koji počinju u $k$ i parova (stablo usmjereno prema korijenu $k$, poredak izlaznih bridova u svakom vrhu). Kad odredimo da Eulerov ciklus počinje u $k$, broj koji treba dokazati jednak je
    
    $$
    \mathrm{deg}(k)\mathrm{ec}(G) = t^\mathrm{root}(G,k)\deg(k)!\prod_{v\neq k}(\deg (v) - 1)!.
    $$
    
    Konstrukcija koja odgovara kombinatornom značenju tog broja je sljedeća. Za Eulerov ciklus s početkom u $k$, prema redoslijedu pojavljivanja bridova u ciklusu, možemo konstruirati
    
    -   stablo usmjereno prema korijenu $k$, sastavljeno od posljednjih izlaznih bridova svih nekorijenskih vrhova, tj. $t^\mathrm{root}(G,k)$,
    -   poredak svih izlaznih bridova korijena $k$, tj. $\mathrm{deg}(k)!$, i
    -   poredak svih izlaznih bridova osim posljednjeg u svakom nekorijenskom vrhu $v\neq k$, tj. $(\mathrm{deg}(v)-1)!$.
    
    Pokažimo da je preslikavanje dobiveno ovom konstrukcijom bijekcija.
    
    S jedne strane, za zadani Eulerov ciklus treba dokazati da posljednji izlazni bridovi svih nekorijenskih vrhova čine stablo usmjereno prema korijenu. Po konstrukciji svaki nekorijenski vrh u stablu ima točno jedan izlazni brid, pa je dovoljno dokazati da ti bridovi ne tvore ciklus. Primijetimo: poredamo li sve vrhove prema trenutku njihova posljednjeg pojavljivanja u Eulerovom ciklusu, posljednji izlazni brid nekorijenskog vrha nužno vodi u vrh koji je strogo kasniji u tom poretku. Ako bi postojao ciklus, u njemu bi postojao najkasniji vrh, a budući da je na ciklusu, on vodi u vrh koji nije kasniji, što je u suprotnosti s rečenim. Dakle, posljednji izlazni bridovi nekorijenskih vrhova nužno čine stablo usmjereno prema korijenu.
    
    S druge strane, za proizvoljno stablo usmjereno prema korijenu i poretke preostalih izlaznih bridova možemo rekonstruirati Eulerov ciklus koji gornjom konstrukcijom daje upravo to stablo i te poretke. Dovoljno je krenuti iz korijena $k$ i pri svakom dolasku u vrh, prema zadanom poretku izlaznih bridova tog vrha, odabrati prvi još neiskorišteni izlazni brid kao sljedeći brid Eulerovog ciklusa; ako su svi izlazni bridovi iz poretka tog vrha već iskorišteni, kao sljedeći brid uzimamo izlazni brid tog vrha u stablu usmjerenom prema korijenu. Budući da je graf Eulerov, svaki vrh ima jednak ulazni i izlazni stupanj, pa se postupak ne može zaustaviti u nekorijenskom vrhu, tj. dobiveni put doista je ciklus. Da bismo dokazali da je dobiveni put valjan Eulerov ciklus, dovoljno je pokazati da postupak prolazi sve bridove.
    
    Ako ne prolazi, postoji vrh $v$ čiji neki izlazni brid nije prođen. Promotrimo vrh $v$. Vrh $v$ ne može biti korijen, jer postupak završava u korijenu, a ako bi korijenu preostao izlazni brid, to je u suprotnosti sa završetkom postupka. Dakle, $v$ nije korijen. Prema opisanom postupku, ako nekorijenskom vrhu $v$ preostaje bilo koji izlazni brid, onda mu nužno preostaje i izlazni brid $e$ u stablu. Neka je $e=(v,u)$. Budući da neki ulazni brid vrha $u$ nije prođen, a izlazni stupanj vrha $u$ jednak je ulaznom, nužno ni neki izlazni brid vrha $u$ nije prođen. Zatim slično promatramo vrh $u$. Ovim zaključivanjem promatrani vrh prešao je iz $v$ u $u$, tj. pomaknuli smo se jedan korak prema korijenu stabla. Indukcijom se dokazuje da tada nužno ni neki izlazni brid korijena $k$ nije prođen. Već smo pokazali da je to nemoguće, pa dobivamo kontradikciju. Dakle, put iz prethodnog odlomka doista je valjan Eulerov ciklus.
    
    Lako se provjeri da su oba preslikavanja injekcije, pa su nužno i bijekcije. Time je tvrdnja dokazana.

## Implementacija

Iz grafa zapišemo Laplaceovu matricu, obrišemo jedan redak i jedan stupac i izračunamo determinantu dobivene matrice. Determinantu možemo računati Gaussovom eliminacijom.

Na primjer, broj razapinjućih stabala kvadrata (ciklusa s četiri vrha):

$$
\begin{pmatrix}
2 & 0 & 0 & 0 \\
0 & 2 & 0 & 0 \\
0 & 0 & 2 & 0 \\
0 & 0 & 0 & 2 \end{pmatrix}-\begin{pmatrix}
0 & 1 & 0 & 1 \\
1 & 0 & 1 & 0 \\
0 & 1 & 0 & 1 \\
1 & 0 & 1 & 0 \end{pmatrix}=\begin{pmatrix}
2 & -1 & 0 & -1 \\
-1 & 2 & -1 & 0 \\
0 & -1 & 2 & -1 \\
-1 & 0 & -1 & 2 \end{pmatrix}
$$

$$
\begin{vmatrix}
2 & -1 & 0 \\
-1 & 2 & -1 \\
0 & -1 & 2 \end{vmatrix} = 4
$$

Rješava se Gaussovom eliminacijom u vremenskoj složenosti $O(n^3)$.

??? note "Implementacija"
    ```cpp
    #include <algorithm>
    #include <cmath>
    #include <cstdlib>
    #include <cstring>
    #include <iostream>
    using namespace std;
    constexpr double eps = 1e-7;
    
    struct matrix {
      static constexpr int MAXN = 20;
      int n, m;
      double mat[MAXN][MAXN];
    
      matrix() { memset(mat, 0, sizeof(mat)); }
    
      void print() {
        cout << "MATRIX " << n << " " << m << endl;
        for (int i = 0; i < n; i++) {
          for (int j = 0; j < m; j++) {
            cout << mat[i][j] << "\t";
          }
          cout << endl;
        }
      }
    
      void random(int n) {
        this->n = n;
        this->m = n;
        for (int i = 0; i < n; i++)
          for (int j = 0; j < n; j++) mat[i][j] = rand() % 100;
      }
    
      void initSquare() {
        this->n = 4;
        this->m = 4;
        memset(mat, 0, sizeof(mat));
        mat[0][1] = mat[0][3] = -1;
        mat[1][0] = mat[1][2] = -1;
        mat[2][1] = mat[2][3] = -1;
        mat[3][0] = mat[3][2] = -1;
        mat[0][0] = mat[1][1] = mat[2][2] = mat[3][3] = 2;
        this->n--;  // brišemo jedan redak
        this->m--;  // brišemo jedan stupac
      }
    
      double gauss() {
        double ans = 1;
        for (int i = 0; i < n; i++) {
          int sid = i;
          for (int j = i + 1; j < n; j++)
            if (abs(mat[j][i]) > abs(mat[sid][i])) sid = j;
          if (abs(mat[sid][i]) <= eps) return 0;
          if (sid != i) {
            for (int j = 0; j < n; j++) swap(mat[sid][j], mat[i][j]);
            ans = -ans;
          }
          for (int j = i + 1; j < n; j++) {
            double ratio = mat[j][i] / mat[i][i];
            for (int k = 0; k < n; k++) {
              mat[j][k] -= mat[i][k] * ratio;
            }
          }
        }
        for (int i = 0; i < n; i++) ans *= mat[i][i];
        return ans;
      }
    };
    
    int main() {
      srand(1);
      matrix T;
      // T.random(2);
      T.initSquare();
      T.print();
      double ans = T.gauss();
      T.print();
      cout << ans << endl;
    }
    ```

## Primjeri zadataka

???+ note "Primjer 1: [„HEOI2015” Soba malog Z-a](https://loj.ac/problem/2122)"
    **Rješenje.** Izravna primjena teorema o matrici i stablima. Svaku praznu sobu promatramo kao vrh, iz ulaza izgradimo graf i Laplaceovu matricu $L$, obrišemo proizvoljni $i$-ti redak i $i$-ti stupac i izračunamo determinantu tog minora. Determinantu računamo Gaussovom eliminacijom na gornjotrokutasti oblik i množenjem dijagonale. U ovom zadatku Gaussova eliminacija radi se nad $\mathbb{Z}/10^9\mathbb{Z}$, pa koristimo Euklidov algoritam (uzastopno dijeljenje) umjesto inverza.

???+ note "Primjer 2: [„FJOI2007” Kotačasti virus](https://www.luogu.com.cn/problem/P2144)"
    **Rješenje.** Zadatak ima mnogo rješenja; teorem o matrici i stablima najizravnije je. Za ulaz $n$ lako se zapiše Laplaceova matrica reda $n+1$:
    
    $$
    L_n = \begin{bmatrix}
    n&  -1&  -1&  -1&  \cdots&  -1&  -1\\
    -1&  3&  -1&  0&  \cdots&  0&  -1\\
    -1&  -1&  3&  -1&  \cdots&  0&  0\\
    -1&  0&  -1&  3&  \cdots&  0&  0\\
    \vdots&  \vdots&  \vdots&  \vdots&  \ddots&  \vdots&  \vdots\\
    -1&  0&  0&  0&  \cdots&  3&  -1\\
    -1&  -1&  0&  0&  \cdots&  -1&  3\\
    \end{bmatrix}_{n+1}
    $$
    
    Dovoljno je izračunati determinantu njezina minora reda $n$; ostaje samo računanje s velikim brojevima.

??? note "Primjer 2+"
    Pojačajmo podatke primjera 2: neka je $n\leq 100000$, a odgovor se traži modulo 1000007. (Rješenje zahtijeva malo linearne algebre.)
    
    **Rješenje.** Izvedemo rekurziju i primijenimo brzo potenciranje matrica.
    
    Izvod rekurzije:
    
    Primijetimo da matrica dobivena brisanjem 1. retka i 1. stupca iz $L_n$ ima pravilnu strukturu, pa zapravo tražimo determinantu matrice
    
    $$
    M_n = \begin{bmatrix}
    3&  -1&  0&  \cdots&  0&  -1\\
    -1&  3&  -1&  \cdots&  0&  0\\
    0&  -1&  3&  \cdots&  0&  0\\
    \vdots&  \vdots&  \vdots&  \ddots&  \vdots&  \vdots\\
    0&  0&  0&  \cdots&  3&  -1\\
    -1&  0&  0&  \cdots&  -1&  3\\
    \end{bmatrix}_{n}
    $$
    
    Razvojem determinante $M_n$ po prvom stupcu dobivamo
    
    $$
    \det M_n = 3\det \begin{bmatrix}
    3&  -1&  \cdots&  0&  0\\
    -1&  3&  \cdots&  0&  0\\
    \vdots&  \vdots&  \ddots&  \vdots&  \vdots\\
    0&  0&  \cdots&  3&  -1\\
    0&  0&  \cdots&  -1&  3\\
    \end{bmatrix}_{n-1} + \det\begin{bmatrix}
    -1&  0&  \cdots&  0&  -1\\
    -1&  3&  \cdots&  0&  0\\
    \vdots&  \vdots&  \ddots&  \vdots&  \vdots\\
    0&  0&  \cdots&  3&  -1\\
    0&  0&  \cdots&  -1&  3\\
    \end{bmatrix}_{n-1} + (-1)^n \det\begin{bmatrix}
    -1&  0&  \cdots&  0&  -1\\
    3&  -1&  \cdots&  0&  0\\
    -1&  3&  \cdots&  0&  0\\
    \vdots&  \vdots&  \ddots&  \vdots&  \vdots\\
    0&  0&  \cdots&  3&  -1\\
    \end{bmatrix}_{n-1}
    $$
    
    Determinante tih triju matrica označimo $d_{n-1}, a_{n-1}, b_{n-1}$.  
    Primijetimo da je $d_n$ tridijagonalna determinanta; sličnim razvojem dobivamo rekurziju $d_n=3d_{n-1}-d_{n-2}$. Slično, razvojem dobivamo $a_{n-1}=-d_{n-2}-1$ i $(-1)^n b_{n-1}=-d_{n-2}-1$.  
    Uvrštavanjem tih rekurzija u gornji izraz dobivamo:
    
    $$
    \det M_n = 3d_{n-1}-2d_{n-2}-2
    $$
    
    $$
    d_n = 3d_{n-1}-d_{n-2}
    $$
    
    Stoga pretpostavljamo da i $\det M_n$ zadovoljava nehomogenu linearnu rekurziju drugog reda. Metodom neodređenih koeficijenata dobivamo konačnu rekurziju
    
    $$
    \det M_n = 3\det M_{n-1} - \det M_{n-2} + 2
    $$
    
    Zapišemo li je kao $(\det M_n+2) = 3(\det M_{n-1}+2) - (\det M_{n-2} + 2)$, odgovor dobivamo brzim potenciranjem matrica.

???+ note "Primjer 3: [„BZOJ3659” WHICH DREAMED IT](https://hydro.ac/p/bzoj-P3659)"
    **Rješenje.** Zadatak je izravna primjena BEST teorema, ali treba paziti: budući da zadatak kaže da se „dva načina izvršavanja zadatka smatraju različitima ako i samo ako se ključevi koriste u različitom redoslijedu”, za svaki Eulerov ciklus iz sobe 1 možemo krenuti bilo kojim izlaznim bridom, pa odgovor još treba pomnožiti izlaznim stupnjem sobe 1.

???+ note "Primjer 4: [„Zajednički pokrajinski izbor 2020 A” Domaća zadaća](https://loj.ac/p/3304)"
    **Rješenje.** Najprije Möbiusovom inverzijom problem svedemo na računanje zbroja težina bridova po svim razapinjućim stablima; budući da to nije usko vezano s ovim člankom, izostavljamo.
    
    Elemente determinante zapišemo kao $w_ix+1$; konačni odgovor je koeficijent uz linearni član determinante. Naime, odgovor je zapravo zbroj po svim bridovima (broj razapinjućih stabala u kojima je taj brid odabran) $\times$ (težina tog brida), a brid uz koji dolazi linearni koeficijent upravo je odabrani brid. Članove stupnja višeg od jedan možemo zanemariti; složenost $O(n^3)$.
    
    [„Pekinški pokrajinski trening 2019” Prebrojavanje razapinjućih stabala](https://www.luogu.com.cn/problem/P5296) općenitiji je slučaj: računa se zbroj $k$-tih potencija zbroja težina razapinjućih stabala; elementi determinante konstruiraju se sličnom metodom, detalje vidi u rješenjima na Luoguu.

???+ note "Primjer 5: [AGC051D C4](https://atcoder.jp/contests/agc051/tasks/agc051_d)"
    **Rješenje.** Prebrojavanje Eulerovih ciklusa u neusmjerenom grafu je #P-potpun problem, ali graf u ovom zadatku je jednostavan: kad odredimo koliko je bridova između $S$ i $T$ usmjereno od $S$ prema $T$, time su određene orijentacije ostalih triju skupina bridova, pa izravnom primjenom BEST teorema dobivamo rješenje složenosti $O(a+b+c+d)$.
