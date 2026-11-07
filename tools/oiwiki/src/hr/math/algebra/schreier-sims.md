---
title: Schreier–Simsov algoritam
---

Predznanje: [Osnovni pojmovi apstraktne algebre](./basic.md), [Teorija grupa](./group-theory.md), [Permutacije](../permutation.md)

## Uvod

**Schreier–Simsov algoritam** (Schreier–Sims algorithm) algoritam je računalne teorije grupa (computational group theory), nazvan po matematičarima Ottu Schreieru i Charlesu Simsu. Algoritam u polinomnom vremenu rješava mnoge probleme, kao što su određivanje reda konačne grupe permutacija ili provjera pripada li zadana permutacija zadanoj grupi. Schreier–Simsov algoritam prvi je uveo Sims 1970. godine, na temelju Schreierove leme. Godine 1981.[^knuth-year] Donald Knuth dodatno je poboljšao vrijeme izvođenja algoritma. Kasnije je razvijena i brža randomizirana inačica algoritma. Sustavi računalne algebre (primjerice GAP i Magma) obično koriste visoko optimiranu Monte Carlo inačicu tog algoritma[^monte-carlo].

???+ info "Oznake"
    U skladu s običajem u literaturi o računalnoj teoriji grupa, u ovom se članku djelovanje grupe zapisuje kao desno djelovanje, što znači da se permutacije komponiraju slijeva nadesno. Sva djelovanja grupa u ovom članku mogu se smatrati djelovanjima permutacijama, iako neki algoritmi vrijede i za općenitija djelovanja grupa. U skladu s tim, skup na kojem grupa djeluje je prema zadanom $X=\{1,2,\cdots,n\}$, a njegovi se elementi nazivaju točkama. Rezultat djelovanja permutacije $g$ na točku $x$ označava se $x^g$; kaže se i da permutacija $g$ pomiče točku $x$ u točku $x^g$. Konačno, pod djelovanjem grupe permutacija $G$ orbita točke $x$ označava se $x^G=\{x^g:g\in G\}$, a njezin stabilizator $G_x=\{g\in G:x^g=x\}$. Pojam stabilizatora može se poopćiti i na skup $B\subseteq X$; njegov je stabilizator definiran kao $G_B=\bigcap_{x\in B}G_x$.

## Pregled

Schreier–Simsov algoritam pokušava riješiti u osnovi sljedeći problem:

-   Zadan je skup $S$ nekih permutacija skupa $X$ veličine $n$. Kako u računalu učinkovito pohraniti grupu permutacija $G=\langle S\rangle$ koju generira $S$ i odgovoriti na niz upita o toj grupi?

Očito, takva grupa $G$ može biti vrlo velika, i to daleko veća od skupa $X$ i generirajućeg skupa $S$. Primjerice, simetrična grupa $S_n=\langle(123\cdots n),(12)\rangle$ stupnja $n$ ima $n!$ elemenata, ali je generiraju samo dvije permutacije. Pohranjivanje svakog elementa grupe nije realistično.

Slično kao što se [Gaussovom eliminacijom](../numerical/gauss.md) konstruira [linearna baza](../linear-algebra/basis.md) vektorskog prostora, ideja je Schreier–Simsova algoritma pronaći „bazu” konačne grupe permutacija $G$:

1.  Ulaz algoritma je generirajući skup $S$ grupe $G$ koji sadrži nekoliko permutacija;
2.  ako grupa $G$ nije trivijalna, uvijek se može pronaći točka $\beta$ čiji se položaj pod djelovanjem grupe $G$ mijenja, tj. $|\beta^G|>1$;
3.  nađe se orbita $\Delta=\beta^{G}$ točke $\beta$ i za svaku točku $\delta\in\Delta$ orbite nađe se permutacija $t_{\delta}$ u grupi $G$ koja pomiče točku $\beta$ u $\delta$;
4.  nađe se generirajući skup $S'$ stabilizatora $G_{\beta}$ točke $\beta$;
5.  algoritam se rekurzivno poziva na $G'=\langle S'\rangle$, sve dok se ne dobije trivijalna grupa $\{e\}$.

Opravdanost ove ideje leži u tome što je stabilizator $G_{\beta}$ točke $\beta$ podgrupa grupe $G$, sve njegove (desne) susjedne klase čine particiju grupe $G$, a te su klase u bijekciji s orbitom $\beta^G$ točke $\beta$; permutacije $t_{\delta}$ pronađene u 3. koraku upravo su predstavnici tih klasa. Taj skup $T$ predstavnika klasa naziva se **transverzala** (transversal) stabilizatora $G_{\beta}$. Drugim riječima, svaki element $g$ grupe $G$ odgovara jedinstvenom paru elemenata $(h,t)\in G_\beta\times T$ takvom da je $g=ht$. Stoga, ako se na neki način uspiju pohraniti podgrupa $G_{\beta}$ i odgovarajuća transverzala $T$, može se pohraniti i cijela grupa $G$. A problem pohranjivanja podgrupe $G_{\beta}$ već je riješen – dovoljno je rekurzivno pozvati algoritam.

Naravno, u implementaciji algoritma ima još mnogo detalja koje treba razjasniti, i to je glavni sadržaj ovog članka. No prije toga treba proučiti rezultat koji se dobiva pozivom algoritma, tj. u kakvu strukturu algoritam pohranjuje grupu i na koje upite pomoću nje može odgovoriti. Za to je potrebno razjasniti nekoliko pojmova.

### Lanac stabilizatora

Pretpostavimo da je algoritam pozvan na grupi $G=\langle S\rangle$ ukupno $k$ puta te da je u $i$-tom pozivu ulaz bio skup permutacija $S^{(i-1)}$, pronađena točka $\beta_i$, dobivena transverzala $T_i$, a dobiveni generirajući skup stabilizatora $S^{(i)}$. Ako označimo $G^{(i)}=\langle S^{(i)}\rangle$, algoritam je zapravo dobio lanac podgrupa

$$
G=G^{(0)}> G^{(1)}>\cdots> G^{(k-1)}> G^{(k)}=\{e\}.
$$

Štoviše, svaka podgrupa u lancu je stabilizator

$$
G^{(i)}=G_{\beta_1,\cdots,\beta_i}.
$$

Stoga se Schreier–Simsov algoritam može promatrati upravo kao računanje takvog **lanca stabilizatora** (stabilizer chain).

### Baza i jaki generirajući skup

Ako podskup $B$ skupa $X$ zadovoljava $G_B=\{e\}$, kaže se da je $B$ **baza** (base) grupe permutacija $G$. Očito je gornji algoritam dobio bazu $B=\{\beta_1,\cdots,\beta_k\}$. To znači da rezultat djelovanja permutacije $g\in G$ na te točke jedinstveno određuje tu permutaciju unutar grupe $G$. Štoviše, baza koju algoritam vraća zadovoljava i uvjet

$$
G^{(i-1)}=G_{\beta_1,\cdots,\beta_{i-1}}>G_{\beta_1,\cdots,\beta_{i-1},\beta_i}=G^{(i)}.
$$

To znači da svaka točka baze nosi stvarnu informaciju o elementima grupe. Takva se baza naziva **neredundantnom** (nonredundant). Algoritam uvijek vraća neredundantnu bazu. Lanac stabilizatora koji odgovara takvoj bazi strogo je padajući.

Istodobno, unija generirajućih skupova dobivenih algoritmom

$$
\bar S=\bigcup_{i=0}^kS^{(i)}
$$

također je generirajući skup grupe $G$ i vrijedi $\langle\bar S\cap G^{(i)}\rangle = G^{(i)}$. Generirajući skup koji zadovoljava taj uvjet naziva se **jakim generirajućim skupom** (strong generating set) grupe $G$ u odnosu na bazu $B$. Stoga se Schreier–Simsov algoritam može promatrati i kao računanje **baze i jakog generirajućeg skupa** (base and strong generating set, BSGS) grupe $G$. Ta je formulacija ekvivalentna formulaciji pomoću lanca stabilizatora i u ovom se članku ne razlikuju.

Naravno, algoritam daje i niz orbita $\Delta_i=\beta_{i}^{G^{(i-1)}}$ i odgovarajućih transverzala $T_i$. Te se orbite nazivaju **osnovnim orbitama** (basic orbits) grupe $G$. Kad se u ovom članku spominju lanac stabilizatora ili baza i jaki generirajući skup grupe $G$, uvijek se podrazumijeva da su odgovarajuće osnovne orbite i transverzale također izračunate.

### Struktura podataka

U ovom će se članku dati niz pseudokodova. U pseudokodu se lanac stabilizatora grupe (ili baza i jaki generirajući skup) pohranjuje u strukturu podataka $C$:

$$
C=(S,\Delta,T,C').
$$

Podatkovni članovi te strukture redom su generirajući skup $S$ trenutačne grupe, osnovna orbita $\Delta$, odgovarajuća transverzala $T$ i stabilizator $C'$ pohranjen kao ugniježđena podstruktura. Naravno, stabilizator $C'$ također je struktura istog oblika. Cijela je grupa zapravo pohranjena u slojevitoj strukturi, gdje svaki sloj opisuje jednu grupu u lancu stabilizatora. Najunutarnjiji sloj prazna je struktura koja predstavlja $G^{(k)}=\{e\}$.

U pseudokodu se članovima te strukture pristupa redom preko $C.generators$, $C.orbit$, $C.transversal$ i $C.next$. Prvi element orbite $C.orbit[0]$ prema zadanom je točka $\beta$ iz baze, a odgovarajući predstavnik klase $C.transversal[\beta]$ prema zadanom je identiteta $e$. Napomena: iako se ovdje elementima orbite i transverzale pristupa indeksima polja, oni ne moraju nužno biti pohranjeni kao polja; treba to shvatiti tako da pružaju način pristupa prvom elementu orbite te dohvaćanja predstavnika klase prema točki orbite. Konkretni detalji implementacije raspravljaju se u nastavku.

### Primjene

Nakon što se dobiju baza i jaki generirajući skup grupe, može se riješiti niz upita o grupi. Među njima su najosnovniji, i oni s kojima se najčešće susreće na algoritamskim natjecanjima, upit o redu grupe i upit pripada li neka permutacija zadanoj grupi.

#### Red grupe

Ako su poznati baza i jaki generirajući skup grupe $G$, primjenom Lagrangeova teorema i teorema o orbiti i stabilizatoru dobiva se da se red grupe $G$ može izračunati kao

$$
|G|=\prod_{i=1}^k[G^{(i-1)}:G^{(i)}]=\prod_{i=1}^k[G^{(i-1)}:G^{(i-1)}_{\beta_i}]=\prod_{i=1}^k|T_i|.
$$

Dakle, dovoljno je pomnožiti veličine svih transverzala $T_i$ (ili, ekvivalentno, duljine osnovnih orbita $\Delta_i$) da bi se dobio red grupe $G$.

#### Provjera pripadnosti

Ako su poznati baza i jaki generirajući skup grupe $G$, može se odrediti i pripada li neka permutacija $h$ grupi $G$. To se naziva problemom **provjere pripadnosti** (membership testing).

Taj se problem može riješiti rekurzivno. Da bi se utvrdilo $h\in G^{(i-1)}$, prvo treba pronaći predstavnika $t\in T_i$ one klase podgrupe $G^{(i)}$ koja sadrži $h$. Ako se takav može pronaći, stavimo $h'=ht^{-1}$; tada je $h=h't$, a $h\in G^{(i-1)}$ ekvivalentno je $h'\in G^{(i)}$, pa se problem svodi na utvrđivanje $h'\in G^{(i)}$. Ako se takav $t$ ne može pronaći, ili je rekurzija već stigla do $G^{(k)}=\{e\}$, ali je $h\neq e$, može se zaključiti $h\notin G$. Zapravo, taj postupak ne samo da utvrđuje $h\in G$, nego u slučaju $h\in G$ prikazuje $h$ kao produkt niza predstavnika klasa $t_k\cdots t_2t_1$, gdje je $t_i\in T_i$. Za elemente grupe $G$ takav prikaz postoji i jedinstven je. To ponovno dokazuje da je gornja formula za red grupe točna.

Taj postupak sada zapisujemo kao sljedeći pseudokod:

$$
\begin{array}{l}
\textbf{Algorithm }\textrm{MembershipTest}(C,h):\\
\textbf{Input. }\textrm{A stabilizer chain }C\textrm{ for a group }G\textrm{ and a permutation }h.\\
\textbf{Output. }\textrm{Whether }h\in G.\\
\textbf{Method.}\\
\begin{array}{ll}
1  & \textbf{while }C\textrm{ is not empty }\\
2  & \qquad \beta \leftarrow C.orbit[0]\\
3  & \qquad \delta \leftarrow \beta^h\\
4  & \qquad \textbf{if }\delta\in C.orbit\textbf{ then}\\
5  & \qquad \qquad t \leftarrow C.transversal[\delta]\\
6  & \qquad \qquad h \leftarrow ht^{-1}\\
7  & \qquad \textbf{else }\\
8  & \qquad \qquad \textbf{return }\textrm{false}\\
9  & \qquad \textbf{end if}\\
10 & \qquad C \leftarrow C.next\\
11 & \textbf{end while}\\
12 & \textbf{return }h=e
\end{array}
\end{array}
$$

U nastavku će se vidjeti da je problem provjere pripadnosti ujedno važan sastavni dio implementacije Schreier–Simsova algoritma o kojoj govori ovaj članak.

## Računanje orbite, transverzale i stabilizatora

Da bi se implementirao Schreier–Simsov algoritam, prvo treba riješiti sljedeći potproblem:[^orbit-algo]

-   Zadani su generirajući skup $S$ grupe $G$ i točka $\beta$. Kako izračunati orbitu $\beta^G$, odgovarajuću transverzalu $T$ i generirajući skup stabilizatora $G_\beta$?

To je problem koji se rješava u ovom odjeljku.

### Pohranjivanje orbite i transverzale

Da bi se dobile orbita i transverzala, dovoljno je izravno pretraživati. Pseudokod je sljedeći:

$$
\begin{array}{l}
\textbf{Algorithm }\textrm{OrbitTransversal}(S,\beta):\\
\textbf{Input. }\textrm{A generating set }S\textrm{ for a group }G\textrm{ and a point }\beta.\\
\textbf{Output. }\textrm{The orbit }\Delta=\beta^G\textrm{ and the transversal }T.\\
\textbf{Method.}\\
\begin{array}{ll}
1  & \Delta \leftarrow [\beta]\\
2  & T[\beta] \leftarrow e\\
3  & \textbf{for }\delta\in\Delta\\
4  & \qquad \textbf{for }s\in S\\
5  & \qquad \qquad \gamma \leftarrow \delta^s\\
6  & \qquad \qquad \textbf{if }\gamma\notin\Delta\textbf{ then}\\
7  & \qquad \qquad \qquad\textrm{append }\gamma\textrm{ to }\Delta\\
8  & \qquad \qquad \qquad T[\gamma] \leftarrow T[\delta]\cdot s\\
9  & \qquad \qquad \textbf{end if}\\
10 & \qquad \textbf{end for}\\
11 & \textbf{end for}\\
12 & \textbf{return }\Delta, T
\end{array}
\end{array}
$$

U konkretnoj implementaciji mogu se koristiti i pretraživanje u širinu (BFS) i pretraživanje u dubinu (DFS). Broj stanja koja pretraživanje obiđe je $|S||T|$; ako se orbita i transverzala razumno pohrane, vremenska je složenost sasvim prihvatljiva.

Budući da je u kontekstu grupa permutacija orbita tek skup od najviše $n$ točaka, za učinkovito pretraživanje i dodavanje može se pohraniti kao polje Booleovih vrijednosti ili neuređeni skup. Tako su obje operacije složenosti $O(1)$, a ukupno zauzeće prostora je $O(n)$. Naravno, ovisno o implementaciji transverzale, možda će dodatno trebati označiti položaj prvog elementa.

Pitanje je kojom strukturom podataka pohraniti odgovarajuću transverzalu $T$.

#### Izravno pohranjivanje

Najjednostavnija je metoda, naravno, izravno pohraniti svaki element $t$ transverzale $T$. Jedna permutacija pohranjena u [jednorednom zapisu](../permutation.md#jednoredni-zapis) zauzima točno $n$ prostora, pa je prostorna složenost pohranjivanja takve transverzale $O(|T|n)$. Prednost je toga da je vremenska složenost pristupa jednom predstavniku klase $O(1)$, a cijena je da je vremenska složenost prvog računanja tih predstavnika klasa $O(|T|n)$.

#### Schreierovo stablo

Drugi je uobičajen pristup implementirati stablastu strukturu za pohranjivanje transverzale. Ona se naziva **Schreierovim stablom** (Schreier tree) ili **Schreierovim vektorom** (Schreier vector)[^schreier-vector]. Korijen joj je $\beta$, a vrhovi su elementi $\delta$ orbite $\Delta$. Svaki put kad se tijekom pretraživanja dobije novi vrh $\gamma=\delta^s$, povuče se brid od starog vrha $\delta$ do novog vrha $\gamma$ i na bridu se zabilježi indeks (ili pokazivač) permutacije $s$ iz generirajućeg skupa $S$. Budući da je generirajući skup već pohranjen, dodatna prostorna složenost pohranjivanja transverzale je $O(|T|)$. Za slučajeve kad je $n$ vrlo velik, to učinkovito štedi prostor, a složenost prvog računanja je $O(|T|)$. Nuspojava je, međutim, da svaki put kad treba dobiti predstavnika klase treba proći bridovima na putu od vrha do korijena i ponovno izračunati predstavnika, pa vremenska složenost jako ovisi o dubini Schreierova stabla. U općem slučaju dubina stabla može doseći red veličine $O(n)$.

U konkretnoj implementaciji treba, ovisno o situaciji, odvagnuti vremensku i prostornu složenost algoritma. U slučajevima s kojima se može susresti na algoritamskim natjecanjima $n$ obično nije velik, prostora je dovoljno, a vremenska složenost često postaje usko grlo. Ubrzo će se vidjeti da upravo najzahtjevniji korak Schreier–Simsova algoritma mnogo puta pristupa predstavnicima klasa, pa je izravno pohranjivanje često bolje. No u nekim primjenama $n$ može biti vrlo velik, a prostor oskudniji, pa transverzalu može biti potrebno pohraniti Schreierovim stablom. Za taj su slučaj, kako bi se izbjegla prevelika dubina Schreierova stabla, istraživači predložili mnoge metode kojima se, kad stablo postane preduboko, rekonstruira plitko Schreierovo stablo. Zainteresirani čitatelji mogu pogledati literaturu na kraju članka.

U pseudokodu ovaj članak neće razlikovati konkretne implementacije transverzale, nego će samo pretpostavljati da struktura podataka koja pohranjuje transverzalu $T$ implementira operacije pristupa i izmjene predstavnika klase $T[\delta]$ prema elementu orbite $\delta\in\Delta$.

### Schreierova lema

Nakon što se dobiju orbita $\beta^G$ i transverzala $T$, Schreierova lema daje način da se dobije generirajući skup stabilizatora $G_\beta$.

???+ note "Schreierova lema"
    Neka grupa $G=\langle S\rangle$ ima podgrupu $H\le G$. Neka je $T$ (desna) transverzala podgrupe $H$ takva da je $e\in T$[^schreier-lemma-unity], i označimo s $\overline g$ predstavnika $t\in T$ one klase u kojoj leži $g\in G$. Tada je skup
    
    $$
    U=\{ts(\overline{ts})^{-1}:t\in T,s\in S\}
    $$
    
    generirajući skup podgrupe $H$. Njegovi se elementi nazivaju **Schreierovim generatorima** (Schreier generators) podgrupe $H$.

??? note "Dokaz"
    Prvo, prema definiciji predstavnika klase, $ts(\overline{ts})^{-1}\in H$ vrijedi za sve $t\in T,s\in S$, pa je $\langle U\rangle\subseteq H$.
    
    Obratno, za bilo koji $h\in H$, budući da je $S$ generirajući skup grupe $G\ge H$, nužno postoji niz $s_i\in S\cup S^{-1}$ takav da vrijedi
    
    $$
    h=s_1s_2\cdots s_r
    $$
    
    Stavimo $t_1=e$ i rekurzivno definirajmo $t_{i+1}=\overline{t_is_i}\in T$; tada je
    
    $$
    \begin{aligned}
    h&=\left(t_1s_1t_2^{-1}\right)\left(t_2s_2t_3^{-1}\right)\cdots\left(t_rs_rt_{r+1}^{-1}\right)t_{r+1}.
    \end{aligned}
    $$
    
    A za svaki $i=1,2,\cdots,r$ vrijedi $t_is_it_{i+1}^{-1}=t_is_i(\overline{t_is_i})^{-1}\in U\cup U^{-1}\subseteq H$, pa je $t_{r+1}\in H$. No $H\cap T=\{e\}$, pa je $t_{r+1}=e$. To pokazuje da se svaki $h\in H$ može zapisati kao produkt niza elemenata $u_i=t_is_it_{i+1}^{-1}\in U\cup U^{-1}$, tj. $U$ generira $H$.

Budući da je podgrupa koja odgovara transverzali $T$ upravo stabilizator $G_\beta$, nakon što se izračuna transverzala $T$, kombinirajući je s generirajućim skupom $S$ grupe $G$ dobiva se generirajući skup stabilizatora $G_\beta$.

### Algoritam

Uz malu izmjenu gornjeg pseudokoda može se, istodobno s računanjem orbite i transverzale, dobiti i generirajući skup odgovarajućeg stabilizatora:

$$
\begin{array}{l}
\textbf{Algorithm }\textrm{OrbitTransversalStabilizer}(S,\beta):\\
\textbf{Input. }\textrm{A generating set }S\textrm{ for a group }G\textrm{ and a point }\beta.\\
\textbf{Output. }\textrm{The orbit }\Delta=\beta^G\textrm{, the transversal }T\textrm{, and a}\\
\qquad\textrm{ generating set }S'\textrm{ for the stabilizer }G_\beta.\\
\textbf{Method.}\\
\begin{array}{ll}
1  & \Delta \leftarrow [\beta]\\
2  & T[\beta] \leftarrow e\\
3  & S' \leftarrow [e]\\
4  & \textbf{for }\delta\in\Delta\\
5  & \qquad \textbf{for }s\in S\\
6  & \qquad \qquad \gamma \leftarrow \delta^s\\
7  & \qquad \qquad \textbf{if }\gamma\notin\Delta\textbf{ then}\\
8  & \qquad \qquad \qquad\textrm{append }\gamma\textrm{ to }\Delta\\
9  & \qquad \qquad \qquad T[\gamma] \leftarrow T[\delta]\cdot s\\
10 & \qquad \qquad \textbf{else} \\
11 & \qquad \qquad \qquad \textrm{append }T[\delta]\cdot s\cdot T[\gamma]^{-1}\textrm{ to }S'\\
12 & \qquad \qquad \textbf{end if}\\
13 & \qquad \textbf{end for}\\
14 & \textbf{end for}\\
15 & \textbf{return }\Delta, T, S'
\end{array}
\end{array}
$$

U pseudokodu je, za svaki par $(\delta,s)$, $t_\delta st_{\delta^s}^{-1}$ novi Schreierov generator samo kad u orbiti ne nastaje novi element; inače je to identiteta $e$. Stoga Schreierovih generatora koji stvarno nastaju u algoritmu (ne računajući početnu identitetu) ima najviše

$$
|S||T|-(|T|-1) = (|S|-1)|T|+1
$$

U općem slučaju ta je gornja ograda oštra[^upper-bound]. No za konačne grupe koje se u praksi obrađuju ta je ograda prilično labava: većina novodobivenih Schreierovih generatora ponavljanja su ranije dobivenih generatora ili se mogu dobiti kompozicijom ranijih generatora.

Budući da se osnovni tijek Schreier–Simsova algoritma može implementirati kao rekurzivno pozivanje gornjeg algoritma za računanje orbite i stabilizatora, zapravo smo već dobili jednu naivnu implementaciju Schreier–Simsova algoritma. No ako se ne provodi prosijavanje, broj Schreierovih generatora raste eksponencijalno: uzastopnom primjenom $|S^{(i)}|=O(|S^{(i-1)}||T_i|)$ dobiva se da će veličina generirajućeg skupa najunutarnjijeg stabilizatora doseći $O(|S||G|)$. To je očito apsurdno neučinkovito, jer je najunutarnjiji stabilizator $\{e\}$.

Simsov rad daje način da se ograniči brzina rasta broja Schreierovih generatora, čime se jamči da je veličina konačno dobivenog jakog generirajućeg skupa $\bar S$ jednaka $O(n^2)$. Tako se baza i jaki generirajući skup mogu izračunati u polinomnom vremenu.

## Schreier–Simsov algoritam

Da bi se riješio gornji problem, u ovom se odjeljku raspravlja o inkrementalnoj implementaciji Schreier–Simsova algoritma kojom se dobiva jaki generirajući skup veličine $O(n^2)$.

### Prosijavanje

Ključna optimizacija kojom Schreier–Simsov algoritam poboljšava gornji naivni algoritam vrlo je jednostavna: prije dodavanja bilo kojeg Schreierova generatora u generirajući skup stabilizatora zahtijeva se da on prvo prođe **prosijavanje** (sifting). Prosijavanje znači da se prvo provjeri nalazi li se novi Schreierov generator već u podgrupi koju generiraju postojeći generatori, a zatim se dodaju samo oni generatori kojih još nema. Za to je dovoljno upotrijebiti algoritam za provjeru pripadnosti $\textrm{MembershipTest}(C,h)$ iz prethodnog teksta.

No preduvjet za to jest da je za Schreierove generatore koji su već proizvedeni na temelju trenutačne grupe već izgrađen lanac stabilizatora (ili baza i jaki generirajući skup) grupe koju oni generiraju. To znači da se pri svakom dodavanju novog Schreierova generatora u generirajući skup stabilizatora mora dinamički održavati unutarnji lanac stabilizatora, kako bi se mogao koristiti za kasnija prosijavanja. No svako umetanje generatora u trenutačni sloj može proizvesti više Schreierovih generatora, pa i više puta ažurirati unutarnju strukturu; a svako ažuriranje unutarnje strukture može izazvati više ažuriranja još dubljih struktura.

Čini se da ranije spomenuti problem eksponencijalne eksplozije i dalje postoji. Zapravo nije tako. Budući da se prosijavanje provodi unaprijed, struktura nekog sloja ažurira se samo kad generator koji se dodaje doista proširi tu strukturu. To pokazuje da je broj ažuriranja jednog sloja zapravo jednak broju strogih povećanja grupe pohranjene u tom sloju. No duljina lanca podgrupa grupe veličine $|G|$ je najviše $\log_2|G|$, jer Lagrangeov teorem jamči da se sa svakim produljenjem lanca podgrupa za jedan veličina grupe barem udvostruči. To pokazuje da se jedan sloj ažurira najviše $\log_2|G|$ puta, pa je veličina konačno dobivenog jakog generirajućeg skupa $\bar S$ jednaka $O(|B|\log|G|)$.

Ta se ocjena može dodatno poboljšati. Budući da je grupa $G$ koja se ovdje pojavljuje podgrupa simetrične grupe $S_n$ stupnja $n$, duljina lanca podgrupa grupe $G$ ne može premašiti duljinu lanca podgrupa grupe $S_n$. Može se dokazati[^subgroup-chain] da duljina strogo rastućeg lanca podgrupa grupe $S_n$ ne premašuje $3n/2$. To pokazuje da je broj ažuriranja jednog sloja zapravo $O(n)$. Očito ni veličina baze ne premašuje $n$. Stoga je veličina konačno dobivenog jakog generirajućeg skupa $\bar S$ jednaka $O(n^2)$.

Ovdje spomenutu metodu prosijavanja predložio je Sims i naziva se i Simsovim filtrom (Sims filter). Postoji i složenija metoda prosijavanja koju je predložio Jerrum, nazvana [Jerrumov filtar](https://groupprops.subwiki.org/w/index.php?title=Jerrum%27s_filter) (Jerrum filter), kojom se jamči da je veličina dobivenog jakog generirajućeg skupa $O(n)$. Zainteresirani čitatelji mogu je proučiti sami.

Mala je optimizacija postupka prosijavanja da implementacija $\textrm{MembershipTest}(C,h)$ ne vraća Booleovu vrijednost, nego konačno dobiveni „ostatak prosijavanja”[^siftee] $h$ (tj. da se $8$. i $12$. redak pseudokoda zamijene s $\textbf{return }h$). Ako je „ostatak” $h\neq e$, provjera pripadnosti nije uspjela, i tada se u trenutačni sloj može izravno dodati „ostatak” $h$ umjesto izvornog $h$. Taj je „ostatak” $h$ već lišen faktora nekoliko predstavnika klasa, pa pomiče manje elemenata i time smanjuje lokalni obujam računanja. Ta optimizacija ne mijenja gornju analizu.

### Postupak

Sad se može opisati konkretan postupak Schreier–Simsova algoritma: prvo se inicijalizira prazna struktura $C$ za pohranjivanje lanca stabilizatora grupe. Zatim se u strukturu $C$ jedan po jedan dodaju generatori iz generirajućeg skupa $S$; konačno dobivena struktura $C$ upravo je lanac stabilizatora grupe $\langle S\rangle$. Pseudokod je sljedeći:

$$
\begin{array}{l}
\textbf{Algorithm }\textrm{SchreierSims}(S):\\
\textbf{Input. }\textrm{A generating set }S\textrm{ for a group }G.\\
\textbf{Output. }\textrm{The stabilizer chain }C\textrm{ for the group }G.\\
\textbf{Method.}\\
\begin{array}{ll}
1  & C \leftarrow []\\
2  & \textbf{for }s\in S\\
3  & \qquad C \leftarrow \textrm{Extend}(C,s)\\
4  & \textbf{end for}\\
5  & \textbf{return }C
\end{array}
\end{array}
$$

Srž algoritma je korak dodavanja novog generatora $s$ u trenutačnu strukturu $C$, tj. potprogram $\textrm{Extend}(C,s)$. Kao što je rečeno, i prije i poslije dodavanja permutacije $s$ treba osigurati da je $C$ lanac stabilizatora. Tako se prije dodavanja permutacije $s$ može prvo provesti prosijavanje. Ako se utvrdi da $s$ nije u postojećoj grupi, **inkrementalno** se računaju orbita, predstavnici klasa i Schreierovi generatori. „Inkrementalno” ovdje znači da se ono što je već izračunato ne računa ponovno. Samo se tako može zajamčiti ispravna složenost.

Razmotrimo kako $\textrm{OrbitTransversalStabilizer}(S,\beta)$ preraditi u inkrementalnu inačicu. Prostor stanja koji algoritam pretražuje je $\Delta\times S$. Nakon dodavanja novog generatora $s$ prostor stanja postaje $\Delta'\times\left(S\cup\{s\}\right)$. Razlika tih dvaju skupova je

$$
\left(\Delta\times\{s\}\right)\cup\left((\Delta'\setminus\Delta)\times \left(S\cup\{s\}\right)\right).
$$

To znači da pri dodavanju novog generatora $s$ prvo treba izračunati kombinacije novog generatora $s$ sa starom orbitom i odgovarajućim predstavnicima klasa; ako se pritom dobiju novi elementi orbite, razmatraju se i kombinacije tih elemenata sa svim generatorima (bez obzira na to jesu li novi ili stari); postupak se ponavlja dok se orbita više ne produljuje.

Pseudokod dodavanja permutacije $g$ u strukturu $C$ je sljedeći:

$$
\begin{array}{l}
\textbf{Algorithm }\textrm{Extend}(C,g):\\
\textbf{Input. }\textrm{A stabilizer chain }C\textrm{ for the group generated by }S\textrm{ and a}\\
\qquad \textrm{permutation }g.\\
\textbf{Output. }\textrm{A stabilizer chain }C\textrm{ for the group generated by }S\cup\{g\}.\\
\textbf{Method.}\\
\begin{array}{ll}
1  & \textbf{if }\textrm{MembershipTest}(C,g)\textrm{ is passed}\textbf{ then}\\
2  & \qquad \textbf{return }C\\
3  & \textbf{end if}\\
4  & \textbf{if }C\textrm{ is empty}\textbf{ then}\\
5  & \qquad \beta \leftarrow \textrm{an element moved by }g\\
6  & \qquad C.orbit[0] \leftarrow \beta \\
7  & \qquad C.transversal[\beta] \leftarrow e\\
8  & \textbf{end if}\\
9  & \textrm{append }g\textrm{ to }C.generators\\
10 & \Delta \leftarrow \textrm{a copy of }C.orbit \\
11 & \textbf{for }\delta\in\Delta \\
12 & \qquad \gamma \leftarrow \delta^g \\
13 & \qquad \textbf{if }\gamma\notin C.orbit\textbf{ then}\\
14 & \qquad \qquad \textrm{append }\gamma\textrm{ to }C.orbit\\
15 & \qquad \qquad C.transversal[\gamma] \leftarrow C.transversal[\delta]\cdot g\\
16 & \qquad \textbf{else}\\
17 & \qquad \qquad s'\leftarrow C.transversal[\delta]\cdot g\cdot C.transversal[\gamma]^{-1}\\
18 & \qquad \qquad C.next \leftarrow \textrm{Extend}(C.next, s')\\
19 & \qquad \textbf{end if}\\
20 & \textbf{end for} \\
21 & \textbf{for }\delta\in C.orbit\setminus\Delta \\ 
22 & \qquad \textbf{for }s\in C.generators \\
23 & \qquad \qquad \gamma \leftarrow \delta^s \\
24 & \qquad \qquad \textbf{if }\gamma\notin C.orbit\textbf{ then}\\
25 & \qquad \qquad \qquad \textrm{append }\gamma\textrm{ to }C.orbit\\
26 & \qquad \qquad \qquad C.transversal[\gamma] \leftarrow C.transversal[\delta]\cdot s\\
27 & \qquad \qquad \textbf{else}\\
28 & \qquad \qquad \qquad s'\leftarrow C.transversal[\delta]\cdot s\cdot C.transversal[\gamma]^{-1}\\
29 & \qquad \qquad \qquad C.next \leftarrow \textrm{Extend}(C.next, s')\\
30 & \qquad \qquad \textbf{end if}\\
31 & \qquad \textbf{end for}\\
32 & \textbf{end for} \\
33 & \textbf{return }C
\end{array}
\end{array}
$$

Time je dobiven potpun Schreier–Simsov algoritam.

### Druga implementacija

Gornja je implementacija već ispravna, ali se redci $12\sim 19$ i $23\sim 30$ pomalo ponavljaju. Na temelju toga Knuth je u svom radu predložio rekurzivnu implementaciju koja je sažetija. Njegov je pristup da se taj ponavljajući dio promatra kao ažuriranje transverzale (i orbite). Svako ažuriranje transverzale treba kombinirati sa svim generatorima, a ovisno o tome je li nastao novi predstavnik klase, odlučuje se hoće li se rekurzivno pozvati sam potprogram ili postupak dodavanja generatora. Pseudokod je sljedeći:

$$
\begin{array}{l}
\textbf{Algorithm }\textrm{Extend}(C,g):\\
\textbf{Input. }\textrm{A stabilizer chain }C\textrm{ for the group generated by }S\textrm{ and a}\\
\qquad \textrm{permutation }g.\\
\textbf{Output. }\textrm{A stabilizer chain }C\textrm{ for the group generated by }S\cup\{g\}.\\
\textbf{Method.}\\
\begin{array}{ll}
1  & \textbf{if }\textrm{MembershipTest}(C,g)\textrm{ is passed}\textbf{ then}\\
2  & \qquad \textbf{return }C\\
3  & \textbf{end if}\\
4  & \textbf{if }C\textrm{ is empty}\textbf{ then}\\
5  & \qquad \beta \leftarrow \textrm{an element moved by }g\\
6  & \qquad C.orbit[0] \leftarrow \beta \\
7  & \qquad C.transversal[\beta] \leftarrow e\\
8  & \textbf{end if}\\
9  & \textrm{append }g\textrm{ to }C.generators\\
10 & \textbf{for }t\in\textrm{a copy of }C.transversal\\
11 & \qquad \textrm{ExtendTransversal}(C,t\cdot g)\\
12 & \textbf{end for}\\
13 & \textbf{return }C
\end{array}\\
\\
\textbf{Sub-Algorithm }\textrm{ExtendTransversal}(C,t):\\
\textbf{Method.}\\
\begin{array}{ll}
1  & \beta \leftarrow C.orbit[0]\\
2  & \gamma \leftarrow \beta^t\\
3  & \textbf{if }\gamma\notin C.orbit\textbf{ then}\\
4  & \qquad \textrm{append }\gamma\textrm{ to }C.orbit\\
5  & \qquad C.transversal[\gamma] \leftarrow t\\
6  & \qquad \textbf{for }s\in C.generators\\
7  & \qquad \qquad \textrm{ExtendTransversal}(C,t\cdot s)\\
8  & \qquad \textbf{end for}\\
9  & \textbf{else}\\
10 & \qquad s' \leftarrow t\cdot C.transversal[\gamma]^{-1}\\
11 & \qquad C.next \leftarrow \textrm{Extend}(C.next,s')\\
12 & \textbf{end if}
\end{array}
\end{array}
$$

Usporedbom ovog pseudokoda s onim iz prethodnog odjeljka vidi se da je ispravan. Štoviše, složenosti im se ne razlikuju. Napomena: $10$. redak potprograma $\textrm{Extend}$ prolazi transverzalom kakva je bila pri ulasku u petlju; predstavnici klasa koji nastaju tijekom petlje već su u rekurziji $\textrm{ExtendTransversal}$ kombinirani sa svim generatorima i ne treba ih ponovno prolaziti.

### Složenost

Za analizu složenosti Schreier–Simsova algoritma potrebno je nekoliko oznaka. Neka je duljina permutacija $n$, a veličina generirajućeg skupa $|S|$ jednaka $m$. Duljinu dobivene (neredundantne) baze označimo $|B|$. Nadalje, u konačno dobivenom stabilizatoru $G^{(i-1)}$ na $i$-tom sloju izvana prema unutra broj generatora označimo $|S^{(i-1)}|$, a veličinu transverzale (ili duljinu orbite) $|T_i|$. U nastavku se analizira vremenska složenost gornje inkrementalne implementacije Schreier–Simsova algoritma. Algoritam se sastoji od dva glavna dijela: prosijavanja te računanja orbita, transverzala i Schreierovih generatora.

I početno zadani generatori i Schreierovi generatori dobiveni u algoritmu moraju proći prosijavanje, pa je ukupan broj izvođenja postupka prosijavanja $O(\sum_{i=1}^{|B|}|S^{(i-1)}||T_i|+|S|)$. Jedno prosijavanje zahtijeva računanje produkta permutacija s $O(|B|)$ predstavnika klasa. Neka je vrijeme računanja produkta s jednim predstavnikom klase $\tau$. Pri izravnom pohranjivanju predstavnika klasa je $\tau\in O(n)$, a pri pohranjivanju predstavnika klasa Schreierovim stablom je $\tau\in O(n^2)$. Ukupna vremenska složenost izvođenja postupka prosijavanja je $O(\tau|B|\sum_{i=1}^{|B|}|S^{(i-1)}||T_i|+\tau|B||S|)$.

Što se tiče računanja orbita i ostalih podataka, budući da je implementacija inkrementalna, svaki par $(\delta,s)\in\Delta_i\times S^{(i-1)}$ u prostoru stanja računa se najviše jednom. Za računanje orbita i transverzala, ovisno o načinu pohranjivanja, vremenska složenost računanja jednog predstavnika klase može biti $O(n)$ ili $O(1)$. No u svakom slučaju ona ne premašuje složenost računanja Schreierovih generatora. Pri izravnom pohranjivanju ona je $O(n)$, a uz Schreierovo stablo $O(n^2)$. Usporedbom s ukupnom vremenskom složenošću postupka prosijavanja vidi se da vremenska složenost računanja tih podataka ne premašuje vremensku složenost potrebnu za prosijavanje. Stoga je vremenska složenost Schreier–Simsova algoritma upravo $O(\tau|B|\sum_{i=1}^{|B|}|S^{(i-1)}||T_i|+\tau|B||S|)$, dobivena u prethodnom odlomku.

Što se tiče prostorne složenosti, struktura podataka koju algoritam na kraju daje pohranjuje $O(\sum_{i=1}^{|B|}|S^{(i-1)}|)$ generatora i $O(\sum_{i=1}^{|B|}|T_i|)$ predstavnika klasa. Pri izravnom pohranjivanju i generatori i predstavnici klasa zahtijevaju $O(n)$ prostora; uz Schreierovo stablo generatori zahtijevaju $O(n)$ prostora, a predstavnici klasa samo $O(1)$.

Ranije je pokazano da je duljina strogo rastućeg lanca podgrupa simetrične grupe stupnja $n$ jednaka $O(n)$, što vrijedi i za $|B|$ i za $|S^{(i)}|$. Stoga Schreier–Simsov algoritam implementiran s izravnim pohranjivanjem transverzala ima vremensku složenost $O(n^5+mn^2)$ i prostornu složenost $O(n^3)$. Naravno, za slučaj $\log|G|\in O(n)$ bolja je ocjena vremenske složenosti[^knuth-complexity] $O(n^2\log^3|G|+mn\log|G|)$ i prostorne složenosti $O(n^2\log|G|)$. Za slučajne generirajuće skupove praktična su mjerenja pokazala da je složenost algoritma znatno niža od $\Theta(n^5)$ i da iznosi otprilike $\Theta(n^4)$.

Iako u odnosu na izravno pohranjivanje Schreierovo stablo u vremensku složenost unosi dodatni faktor $n$, u slučaju kad je $n$ vrlo velik, a sama grupa daleko manja od simetrične grupe stupnja $n$, njegova je prostorna složenost $O(n\log^2|G|)$, što je daleko manje od $O(n^2\log|G|)$ kod izravnog pohranjivanja. No na algoritamskim natjecanjima teško je naići na takvu situaciju u kojoj je pohranjivanje Schreierovim stablom bolje.

### Referentna implementacija

Ovdje dajemo referentnu implementaciju Schreier–Simsova algoritma. Budući da je $n$ malen, u implementaciji se baza $B=\{n,n-1,\cdots,1\}$ izravno zadaje umjesto da je algoritam bira. Prednost je toga da permutacije u grupi na $k$-tom sloju iznutra prema van (ne računajući praznu strukturu) mijenjaju samo prvih $k$ elemenata, što olakšava daljnje računanje. Druga je optimizacija u kodu da se pri pohranjivanju predstavnika klasa zapravo pohranjuju njihove inverzne permutacije, što pojednostavnjuje operacije s permutacijama.

??? example "Referentna implementacija"
    ```cpp
    --8<-- "docs/math/code/schreier-sims/schreier-sims.cpp"
    ```

## Zadaci za vježbu

-   [LOJ 177. 生成子群阶数 (Red generirane podgrupe)](https://loj.ac/p/177)
-   [\[WC2017\] 棋盘 (Šahovska ploča)](https://uoj.ac/problem/287)
-   [Permutations](https://codeforces.com/gym/421334/problem/A)
-   [\[Grand Prix of Yekaterinburg 2015\] Problem H. Heimdall](https://disk.yandex.com/i/OfEXXcu-anMHuw)

## Literatura i napomene

-   [Schreier–Sims algorithm - Wikipedia](https://en.wikipedia.org/wiki/Schreier%E2%80%93Sims_algorithm)
-   [Sims, Charles C, Computational methods in the study of permutation groups, Computational Problems in Abstract Algebra, pp. 169–183, Pergamon, Oxford, 1970.](https://www.sciencedirect.com/science/article/pii/B9780080129754500205)
-   [Knuth, Donald E. Efficient representation of perm groups, Combinatorica 11 (1991), no. 1, 33–43.](https://arxiv.org/abs/math/9201304)
-   [Ákos Seress, Permutation Group Algorithms, Cambridge University Press](https://www.cambridge.org/core/books/permutation-group-algorithms/199629665EC545A10BCB99FFE6AAFD25)
-   [Alexander Hulpke's Notes on Computational Group Theory](https://www.math.colostate.edu/%7Ehulpke/CGT/cgtnotes.pdf)
-   [Derek Holt's Slides on The Schreier–Sims algorithm for finite permutation groups](https://blogs.cs.st-andrews.ac.uk/codima/files/2015/11/CoDiMa2015_Holt.pdf)
-   [Martin Jaggi, Implementations of 3 Types of the Schreier–Sims Algorithm, MAS334 - Mathematics Computing Project, 2005](https://www.m8j.net/data/List/Files-118/Documentation.pdf)
-   [Henrik Bäärnhielm. The Schreier–Sims algorithm for matrix groups](https://henrik.baarnhielm.net/schreiersims.pdf)

[^knuth-year]: Knuthov je rad objavljen 1991. godine, ali je njegovo poboljšanje već 1981. bilo široko predstavljeno na konferenciji. Rad je napisan na temelju njegova konferencijskog izlaganja.

[^monte-carlo]: Ne miješati s Monte Carlo metodom. Monte Carlo algoritam ovdje označava randomizirani algoritam s konstantnom i po volji malom vjerojatnošću pogreške.

[^orbit-algo]: Ni ovaj problem ni algoritmi u ovom odjeljku ne zahtijevaju pretpostavku da je promatrano djelovanje grupe djelovanje permutacijama, pa se mogu primijeniti u širem kontekstu. Primjerice, ako se ti algoritmi primijene na djelovanje konjugiranjem, također se mogu izračunati orbite (klase konjugiranosti), transverzale i stabilizatori (centralizatori).

[^schreier-vector]: Budući da se ta stablasta struktura može implementirati nizom pokazivača na roditeljski čvor, naziva se i Schreierovim vektorom.

[^schreier-lemma-unity]: Uvjet $e\in T$ nije nužan da bi Schreierova lema vrijedila.

[^upper-bound]: [Nielsen–Schreierov teorem](https://en.wikipedia.org/wiki/Nielsen%E2%80%93Schreier_theorem) kaže da je za [slobodnu grupu](https://en.wikipedia.org/wiki/Free_group) generiranu s $n$ generatora njezina podgrupa indeksa $k$ slobodna grupa generirana s $k(n-1)+1$ generatora.

[^subgroup-chain]: Vidi [Cameron, P. J., Solomon, R., & Turull, A. (1989). Chains of subgroups in symmetric groups. Journal of algebra, 127(2), 340-352.](https://www.sciencedirect.com/science/article/pii/0021869389902561)

[^siftee]: To nije strog stručni naziv; u različitoj engleskoj literaturi naziva se siftee ili sifted element.

[^knuth-complexity]: Gornja ograda iz Knuthova rada ima još jedan logaritamski faktor manje, što zahtijeva pažljiviju ocjenu duljina osnovnih orbita lanca stabilizatora grupe.
