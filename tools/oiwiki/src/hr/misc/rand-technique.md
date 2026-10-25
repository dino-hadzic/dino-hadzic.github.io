---
title: Randomizirane tehnike
---

## Pregled

Preduvjeti: [Slučajni brojevi](../misc/random.md) i [Osnove vjerojatnosti](../math/probability/basic-conception.md)

Ovaj članak daje jednostavnu klasifikaciju tehnika povezanih s randomizacijom u OI/ICPC-u i predstavlja svaku od kategorija. Članak također predstavlja neke metode koje se u OI/ICPC-u rijetko koriste, ali su stilom i duhom bliske OI/ICPC-u; takav je sadržaj označen oznakom `(*)`.

Ova klasifikacija ne predstavlja široko prihvaćen konsenzus i zasigurno ne može obuhvatiti sve mogućnosti, pa služi samo kao orijentacija.

**Oznake i dogovori**:

-   $\mathrm{Pr}[A]$ označava vjerojatnost da se dogodi događaj $A$.
-   $\mathrm{E}[X]$ označava očekivanje slučajne varijable $X$.
-   Znak pridruživanja $:=$ označava uvođenje nove veličine, npr. $Y:=1926$ znači da uvodimo veličinu $Y$ s vrijednošću $1926$.

## Pokrivanje ciljnog elementa slučajnim skupom

U golemom prostoru rješenja postoji jedno (ili više) rješenje koje tražimo. Možemo pokušati više puta „baciti mrežu”; dovoljno je da jedanput ulovimo ciljno rješenje da bismo uspjeli.

### Primjer: provjera je li graf trodijelan

???+ note "Zadatak"
    Zadan je jednostavan neusmjereni graf s $n$ vrhova i $m$ bridova. Obojite svaki vrh jednom od tri boje R, G, B tako da svaki par susjeda bude različito obojen, ili javite da rješenje ne postoji.

Za svaki vrh $v$ iz $\{R,G,B\}$ nezavisno i s jednakom vjerojatnošću slučajno odaberemo jednu boju $C_v$ i propišemo da $v$ **ne** smije biti obojen bojom $C_v$. Vjerojatnost da optimalno rješenje zadovoljava upravo ta ograničenja očito je $\big(\frac 23\big)^n$.

Uz ta ograničenja, za par susjeda $(u,v)$ zahtjev „$u$ i $v$ su različitih boja” ekvivalentan je sljedećoj relaciji „implikacije”:

-   Za svaku boju $X$ različitu od $C_u$ i $C_v$: ako je $u$ obojen bojom $X$, onda je $v$ obojen bojom $\{R,G,B\}\setminus\{X,C_v\}$.

Stoga svakom $v$ možemo pridružiti Booleovu varijablu $B_v$ čija vrijednost govori kojom je od dviju preostalih boja $v$ obojen. Pomoću modela 2-SAT zadatak se zatim rješava u složenosti $O(n+m)$.

Ovako je vjerojatnost uspjeha jednog pokušaja $\big(\frac 23\big)^n$. Ponovimo algoritam $-\big(\frac 32\big)^n\log \epsilon$ puta i ispišemo rješenje čim ga jedanput dobijemo; time jamčimo točnost s vjerojatnošću $1-\epsilon$. (Više o tome u odjeljku „Analiza gornjih ograda vjerojatnosti” u nastavku.)

***

**Osvrt**: u ovom je zadatku „prostor rješenja” skup $\{R,G,B\}^n$, a mi svaki put slučajno nametnemo ograničenja i time tražimo „ciljno rješenje”, tj. valjano bojenje, unutar smanjenog prostora.

### Primjer: [CodeChef SELEDGE](https://www.codechef.com/problems/SELEDGE)

???+ note "Sažetak zadatka"
    Zadan je neusmjereni graf u kojem i vrhovi i bridovi imaju nenegativne težine. Pronađite skup bridova $S$ veličine $\leq K$ koji maksimizira zbroj težina vrhova incidentnih sa $S$ umanjen za zbroj težina bridova iz $S$. Težina svakog vrha broji se samo jedanput.

Opažanje: ako tri odabrana brida čine lanac, uklanjanje srednjeg nikad ne pogoršava rješenje; ako neki odabrani bridovi čine ciklus, uklanjanje bilo kojeg od njih nikad ne pogoršava rješenje.

Posljedica: skup bridova optimalnog rješenja nužno čini nekoliko disjunktnih zvijezda (tj. stabala promjera najviše 2).

Posljedica: skup bridova optimalnog rješenja nužno čini bipartitan graf.

Svaki vrh nezavisno i s jednakom vjerojatnošću obojimo jednom od dviju boja, crnom ili bijelom, i zahtijevamo da to bojenje bude upravo crno-bijelo bojenje bipartitnog grafa koji odgovara optimalnom rješenju.

Pokušajmo izračunati vjerojatnost da optimalno rješenje zadovoljava taj zahtjev:

-   Promotrimo zvijezdu s $n$ vrhova; ona očito ima 2 bojenja, pa je vjerojatnost da je ispravno obojena $\dfrac 2{2^n}=2^{1-n}$.
-   Neka zvijezde u optimalnom rješenju imaju redom $a_1,\cdots,a_l$ vrhova; tada nužno vrijedi $(a_1-1)+\cdots+(a_l-1)\leq K$, gdje je $K$ najveći dopušteni broj odabranih bridova.
-   Stoga je vjerojatnost da su sve zvijezde ispravno obojene $2^{1-a_1}\cdots 2^{1-a_l}\geq 2^{-K}$.

Uz gornji zahtjev pokušajmo izgraditi model toka minimalne cijene (min-cost flow) kojim računamo optimalan odgovor:

-   Izgradimo bipartitan graf: bijeli vrhovi su na lijevoj strani i spojeni su sa $S$, crni su na desnoj strani i spojeni su s $T$.
    -   Za bijeli vrh $v$ povučemo iz $S$ do njega brid kapaciteta 1 i cijene $-A_v$ te brid kapaciteta $\infty$ i cijene 0.
    -   Za crni vrh $v$ povučemo od njega do $T$ brid kapaciteta 1 i cijene $-A_v$ te brid kapaciteta $\infty$ i cijene 0.
-   Za svaki brid $(u,v,B)$ izvornog grafa u kojem je $u$ bijel, a $v$ crn, povučemo brid od $u$ do $v$ kapaciteta 1 i cijene $B$.
-   Ako u tom grafu ograničimo tok na najviše $K$, odgovor je minimalna cijena sa suprotnim predznakom.

Ako rješavamo SPFA-om za tok minimalne cijene, složenost je $O\big(K^2(n+m)\big)$. Dokaz:

-   Prvo, očito je broj pokretanja SPFA-a $\leq K$.
-   Zatim, u jednom pokretanju SPFA-a svaki vrh ulazi u red najviše $O(K)$ puta. Razlog:
    -   U svakom trenutku najviše $3K$ bridova nosi tok, jer bi inače u izvornom grafu bilo odabrano više od $K$ bridova.
    -   Na svakom proširujućem putu duljine $L$ barem je $\dfrac L2-2$ bridova obratni brid nekog brida koji nosi tok, jer svi bridovi unaprijed idu s lijeve strane grafa na desnu, pa samo ti obratni bridovi mogu ići s desne strane na lijevu.
    -   Iz tih dvaju zaključaka slijedi da duljina svakog proširujućeg puta ne prelazi $6K+4$.
-   Ukupno, složenost je $O\big(K^2(n+m)\big)$.

Slično kao u prethodnom zadatku, cijeli postupak moramo ponoviti $-2^K \log\epsilon$ puta da bismo dobili točnost s vjerojatnošću $1-\epsilon$. Ukupna složenost: $O\big(2^KK^2(n+m)\cdot -\log\epsilon\big)$.

## Pogađanje ciljnog skupa slučajnim elementom

Trebamo pronaći bilo koji element nekog skupa; zato slučajno biramo elemente u nadi da ćemo pogoditi upravo taj skup.

### Primjer: [Gym 101550I](https://codeforces.com/gym/101550/attachments)

???+ note "Sažetak zadatka"
    Zadan je graf sljedećeg oblika: dva paralelna lanca te dva paralelna brida koja ih povezuju. Zadano je nekoliko jednostavnih putova u tom grafu (svaki put predstavlja jedan telefonski razgovor). Odaberite što manje bridova na koje ćete postaviti prislušne uređaje tako da se na svakom zadanom putu nalazi barem jedan prislušni uređaj.

Cijeli graf možemo rastaviti na jedan ciklus i četiri lanca koji iz njega izlaze. Za svaki od tih četiriju lanaca (označimo ga $C$) razmotrimo kako na njemu postaviti prislušne uređaje:

-   Uz uvjet da presretnemo sve razgovore koji se odvijaju potpuno unutar $C$, upotrijebimo najmanji mogući broj prislušnih uređaja.
-   Uz uvjet iz prethodne točke, nastojimo da najmanja udaljenost uređaja na $C$ od ciklusa bude što manja.
    -   Svrha je tog zahtjeva presresti što više razgovora koji imaju točno jedan kraj unutar $C$.

Zatim promotrimo ukupno 4 brida na kojima se lanci spajaju s ciklusom; grubom silom nabrojimo sve mogućnosti ima li na tim bridovima prislušnih uređaja ili ne. Očito, ako želimo presresti razgovore koji prelaze s lanca na ciklus, postavljanje uređaja na ta 4 brida sigurno je optimalno. Sad razgovore možemo podijeliti u sljedeće vrste:

1.  Razgovori potpuno na lancu. Oni su već sigurno presretnuti, pa ih možemo zanemariti.
2.  Razgovori koji prelaze s lanca na ciklus i već su presretnuti. Možemo ih zanemariti.
3.  Razgovori koji prelaze s lanca na ciklus i nisu presretnuti. Možemo im jednostavno odrezati dio na lancu (jer je raspored uređaja na lancu već fiksiran) i zadržati samo dio na ciklusu.
4.  Razgovori potpuno na ciklusu.

Time je zadatak sveden na zadatak na ciklusu.

Neka su u optimalnom rješenju prislušni uređaji na ciklusu postavljeni na skup bridova $S$. Ako znamo bilo koji element $e$ skupa $S$, možemo:

-   prvo u $e$ prerezati ciklus u lanac;
-   zatim od $e$ greedy postupkom uzastopno pronalaziti sljedeći brid na koji postavljamo uređaj; uočimo da se, uz prikladnu pretpripremu, svaki korak greedy postupka može izvesti u složenosti $O(1)$;
-   i tako riješiti zadatak u složenosti $O(|S|)$.

Zato slučajno odaberemo brid $e'$ na ciklusu, propišemo $e'\in S$ i izvedemo gornji postupak; to ponovimo više puta i uzmemo najbolje rješenje.

Analiza složenosti jednog pokušaja:

-   Opažanje: označimo sa $S'$ optimalno rješenje među svim rješenjima koja sadrže $e'$; tada je $|S'|\leq |S|+1$.
-   Stoga je složenost jednog pokušaja $O(|S'|)=O(|S|)$.

Analiza vjerojatnosti uspjeha:

-   Očito je vjerojatnost uspjeha jednog pokušaja $\dfrac {|S|}n$, gdje je $n$ duljina ciklusa.
-   Stoga je potrebno $-\dfrac n{|S|}\log\epsilon$ ponavljanja da bismo dobili točnost s vjerojatnošću $1-\epsilon$.

Ukupno, složenost je algoritma $O\big(|S|\cdot -\dfrac n{|S|}\log\epsilon\big)=O(-n\log\epsilon)$.

### Primjer: [CSES 1685 New Flight Routes](https://cses.fi/problemset/task/1685)

???+ note "Sažetak zadatka"
    Zadan je usmjereni graf. Dodajte što manje bridova tako da graf postane jako povezan; potrebno je **ispisati rješenje**.

Prvo sažmemo jako povezane komponente izvornog grafa. Cilj nam je očito da svaki ponor (vrh bez izlaznih bridova) može doći do svakog izvora (vrha bez ulaznih bridova).

Nije teško dokazati da ćemo bridove dodavati samo od ponora prema izvorima, jer svakom drugom dodanom bridu odgovara neki brid od ponora prema izvoru koji nije slabiji od njega.

Naša ključna operacija jest: uzmemo ponor $t$ i izvor $s$ (ne moraju biti u istoj slabo povezanoj komponenti) i dodamo brid $t\to s$ tako da **ni $s$ ni $t$ više nisu ni ponor ni izvor** (nazovimo to ciljem I). U idealnom slučaju takva operacija svaki put smanjuje broj ponora i broj izvora za jedan, pa je ponavljamo dok ne ostane samo jedan ponor ili samo jedan izvor, a taj je slučaj trivijalan. Stoga pretpostavljamo da je odgovor maksimum broja izvora i broja ponora.

Nije teško uočiti da gornja operacija postiže cilj I ako i samo ako $t$ ima prethodnika različitog od $s$, a $s$ ima sljedbenika različitog od $t$. Može se dokazati (dokaz dajemo malo kasnije) da u svakom DAG-u s barem dva izvora i barem dva ponora postoji takav par $(s,t)$; međutim, sama egzistencija ne pomaže nam konstruirati rješenje, pa je potrebna daljnja analiza.

-   Čak i s tim nužnim i dovoljnim uvjetom teško je izravno dobiti algoritam, uglavnom zato što dodavanje brida $t\to s$ može utjecati na valjanost drugih parova $(s',t')$, a to je teško obraditi.

Uočimo da o odnosima između izvora i ponora znamo vrlo malo (čak i brzi upit je li neki $t$ dostižan iz nekog $s$ zahtijeva pretpripremu s DFS-om i bitsetom, što vremensko ograničenje ne dopušta); to nam sugerira da trebamo neko vrlo općenito i snažno svojstvo.

Opažanje: parova $(s,t)$ koji ne zadovoljavaju cilj I ima najviše $n+m-1$, gdje je $n$ broj izvora, a $m$ broj ponora.

-   Razlog: ako svaki takav par $(s,t)$ promatramo kao brid između $s$ i $t$, graf koji čine svi ti bridovi izgleda kao nekoliko disjunktnih lanaca, pa broj bridova ne prelazi broj vrhova umanjen za jedan.
-   Motivacija za to opažanje jest to što, da bismo egzistencijalni rezultat primijenili u algoritmu, prethodni korak često mora biti pojačati kvalitativni rezultat u kvantitativni.

Posljedica: ako par $(s,t)$ biramo slučajno s jednakom vjerojatnošću, vjerojatnost da zadovoljava gornji zahtjev iznosi $\geq \dfrac {(n-1)(m-1)}{nm}$.

-   Uočimo da je ovaj rezultat strogo jači od ranije navedenog egzistencijalnog rezultata.

Posljedica: ako nezavisno i s jednakom vjerojatnošću uzastopno slučajno odaberemo $\dfrac {\min(n,m)}2$ parova $(s,t)$ bez zajedničkih elemenata i nad njima **redom** izvedemo operaciju (tj. dodamo brid $t\to s$), vjerojatnost da sve te operacije zadovoljavaju cilj I iznosi $\geq \dfrac 14$.

-   Razlog:

$$
\begin{aligned}
&\phantom{=\ }\dfrac {(n-1)(m-1)}{nm}\cdot\dfrac{(n-2)(m-2)}{(n-1)(m-1)}\cdots\dfrac{(n-k)(m-k)}{(n-k+1)(m-k+1)}\\
&=\dfrac{(n-k)(m-k)}{nm}\\
&\geq \dfrac 14
\end{aligned}
$$

A provjeriti zadovoljavaju li svih $k$ uzastopno odabranih parova $(s,t)$ cilj I vrlo je jednostavno: dovoljno je još jedanput sažeti jako povezane komponente i provjeriti jesu li se i $n$ i $m$ smanjili za $k$. Uočimo da, ako se svaki put smanje za $k=\dfrac{\min(n,m)}2$, onda $\min(n,m)$ nužno postaje 1 unutar $O\big(\log(n+m)\big)$ rundi, čime dolazimo do trivijalnog slučaja.

???+ note "Pseudokod algoritma"
    ```text
    while(n>1 and m>1):
        randomly choose k=min(n,m)/2 pairs (s,t)
        add edge t->s for all these pairs
        if new_n>n-k or new_m>m-k:
            roll_back()
    solve_trivial()
    ```

Složenost: $O\big((|V|+|E|) \log |V|\big)$.

***

**Osvrt**: trebali smo pronaći bilo koji par $(s,t)$ koji ostvaruje cilj I, pa smo $(s,t)$ birali slučajno.

## Dobivanje svojstava slučajnih podataka randomizacijom

Ako su podaci zadatka generirani slučajno, možda ih možemo riješiti iskorištavanjem svojstava slučajnih podataka. U nekim slučajevima, čak i ako podaci nisu generirani slučajno, randomizacijom im možemo dati neka svojstva slučajnih podataka i time si pomoći u rješavanju zadatka.

### Primjer: randomizirani inkrementalni algoritam

Slučajno generirani niz elemenata može imati svojstva poput „očekivani broj promjena optimalnog rješenja na prefiksima vrlo je malen”; randomizirani inkrementalni algoritam (randomized incremental algorithm) ta svojstva dobiva slučajnim permutiranjem ulaznog niza.

Više u članku [Randomizirani inkrementalni algoritam](../geometry/random-incremental.md).

### Primjer: randomizirano rješenje zadatka [TopCoder MagicMolecule](https://archive.topcoder.com/ProblemStatement/pm/11705)

???+ note "Sažetak zadatka"
    Zadan je neusmjereni graf s $n$ vrhova i težinama na vrhovima. Među svim klikama veličine barem $\dfrac {2n}3$ pronađite onu s najvećim zbrojem težina vrhova.
    
    $n\leq 50$

Lako se dosjetiti pretrage „susret u sredini” (meet in the middle). Skup vrhova ravnomjerno podijelimo na lijevu i desnu polovicu $V_L,V_R$ (obje veličine $\dfrac n2$) i izračunamo niz $f_{L,k}$ koji označava najveći zbroj težina među svim klikama s $\geq k$ elemenata unutar skupa vrhova $L\subseteq V_L$. Zatim nabrojimo svaku kliku $C_R$ desne polovice, odredimo koji su vrhovi lijeve polovice spojeni sa svim vrhovima iz $C_R$ (taj skup označimo $N_L$) i odgovor ažuriramo vrijednošću $f_{N_L,\frac 23 n-|C_R|}+\textit{value}(C_R)$.

-   Uočimo da se svaki $f_{L,k}$ može izračunati prijelazom u $O(1)$. Konkretno, uzmemo proizvoljan element $d$ skupa $L$ i razmotrimo slučajeve:
    -   Ako u optimalnom rješenju $d$ nije u klici, prijelaz je iz $f_{L\setminus \{d\},k}$.
    -   Ako je u optimalnom rješenju $d$ u klici, prijelaz je iz $f_{L\cap N(d),k}+\textit{value}(d)$, gdje je $N(d)$ skup susjeda vrha $d$.
    -   Ne zaboravimo i $f_{L,k}$ ažurirati vrijednošću $f_{L,k+1}$.

Ovo rješenje prekoračuje vremensko ograničenje. Pokušajmo ga optimizirati:

-   Skup vrhova dijelimo na pola uniformno slučajno. Tada je, uz nezanemarivu vjerojatnost, i skup vrhova optimalnog rješenja $C_{res}$ podijeljen točno na pola (tj. $|C_{res}\cap V_L|=|C_{res}\cap V_R|$).
    -   Naravno, $|C_{res}|$ može biti neparan. Radi jednostavnosti ovdje pretpostavljamo da je paran; neparan slučaj ne mijenja bitno rješenje.
    -   Eksperimentalno se pokazuje da je s otprilike 20 slučajnih pokušaja vrlo velika vjerojatnost da barem jedan zadovoljava to svojstvo. Drugim riječima, ako se naš algoritam oslanja na svojstvo „$C_{res}$ je podijeljen na pola”, onda ponavljanje algoritma 20 puta i uzimanje najboljeg rezultata također s vrlo velikom vjerojatnošću daje točan odgovor.
-   S tim svojstvom možemo izravno propisati da lijeva klika $L$ i desna klika $C_R$ imaju veličinu $\geq \dfrac n3$. To donosi dva poboljšanja složenosti:
    -   U $f$ možemo izostaviti dimenziju koja pamti veličinu.
    -   Budući da treba razmatrati samo klike veličine $\geq \dfrac n3$, broj lijevih klika $L$ i desnih klika $C_R$ koje treba razmotriti također se znatno smanjuje, na otprilike $1.8\cdot 10^6$.
-   Sad je usko grlo računanje zbroja težina nekog podskupa jedne strane, jer to zahtijeva pretpripremu u $O\big(2^{|V_L|}+2^{|V_R|}\big)$.
    -   Rješenje: unutar $V_L$ i $V_R$ ponovno podijelimo na pola; kad tražimo zbroj težina nekog podskupa, podijelimo ga na lijevu i desnu polovicu, za svaku zasebno dohvatimo zbroj i rezultate zbrojimo.
-   Time se zadatak može riješiti u zadanom vremenu.

***

**Osvrt**: slučajan skup ima svojstvo „razlika veličina dviju polovica podjele nije prevelika”, a mi smo to svojstvo dobili slučajnom podjelom.

## Randomizacija za hashiranje

### Primjer: [UOJ #207 共价大爷游长沙](https://uoj.ac/problem/207) („Kovalentni djed obilazi Changsha”)

???+ note "Sažetak zadatka"
    Održavajte stablo koje se dinamički mijenja i skup parova vrhova koji se dinamički mijenja. Trebate podržati:
    
    -   brisanje i dodavanje brida, uz jamstvo da je rezultat i dalje stablo;
    -   dodavanje/brisanje para vrhova;
    -   za zadani brid $e$ odrediti leži li $e$ na jednostavnom putu između $s$ i $t$ za svaki par vrhova $(s,t)$ iz skupa.

Za svaki brid $e$ grafa definiramo skup $S_e$ kao skup ključnih putova (tj. parova $(a,b)$ iz zadatka) koji prolaze tim bridom. Za svaki brid dinamički održavamo hash skupa $S_e$; tako lako provjeravamo je li $S_e$ jednak cijelom skupu (tj. je li $e$ „neizbježan brid”).

Hashiramo tako da svakom paru $(a,b)$ pridružimo slučajan nenegativan cijeli broj $H_{(a,b)}$ manji od $2^{64}$, a hash skupa tada je XOR vrijednosti $H$ njegovih elemenata.

Tada hash svakog fiksnog skupa nužno ima uniformnu distribuciju na $R:=\left\{0,1,\cdots,2^{64}-1\right\}$ (drugim riječima, hash poprima vrijednosti iz $R$, i to svaku s jednakom vjerojatnošću). Razlog:

1.  Pojedinačni $H_{(a,b)}$ očito ima uniformnu distribuciju.
2.  XOR dviju nezavisnih slučajnih varijabli s uniformnom distribucijom na $R$ također nužno ima uniformnu distribuciju na $R$. Dokaz nije težak, prepuštamo ga čitatelju.

Stoga je točnost algoritma zajamčena.

Za održavanje tog hasha dovoljno je upotrijebiti LCT (link-cut tree).

### Primjer: [CodeChef PANIC](https://www.codechef.com/problems/PANIC) i analiza vjerojatnosti greške

Grubi pregled rješenja:

1.  Može se dokazati[^ref1] da $S(N)$ zadovoljava linearnu rekurziju reda $O(K)$ po $N$.
2.  Algoritmom BM (Berlekamp–Massey) pronađemo tu rekurziju.
3.  Pomoću rekurzije, Cayley–Hamiltonovim teoremom izračunamo $S(N)$.

Ovdje nas zanima samo drugi dio, tj. kako pronaći rekurziju za niz matrica. Zato je dovoljno razmotriti sljedeći zadatak:

???+ note "Zadatak"
    Zadan je niz matrica koji modulo $P:=998244353$ zadovoljava homogenu linearnu rekurziju (množenje skalarom i zbrajanje u rekurziji definirani su kao množenje matrice skalarom i zbrajanje matrica). Pronađite najkraću rekurziju.

Ako niz matrica zadovoljava rekurziju $F$, onda i svaki njegov element (pozicija u matrici) zadovoljava $F$. Međutim, ako za neku poziciju pronađemo najkraću rekurziju $F'$, ona može biti kraća od $F$, što stvara problem.

Rješenje: svakoj poziciji $(i,j)$ matrice pridružimo slučajnu težinu $x_{i,j}<P$, zatim za svaku matricu niza izračunamo težinski zbroj svih njezinih pozicija modulo $P$, brojeve dobivene za pojedine matrice poredamo u niz i na dobiveni niz primijenimo algoritam BM.

Analiza vjerojatnosti greške:

-   Pretpostavimo da je gornji postupak dao rekurziju $F'$ reda $l$ različitu od $F$ (i, očito, ne dulju od $F$).
-   Budući da niz matrica ne zadovoljava $F'$, nužno postoji pozicija $(i,j)$ u matrici takva da pripadni niz $S_{i,j}$ za neki $N$ ne zadovoljava $F'$. Drugim riječima:

$$
S(N)_{i,j}-F'_1S(N-1)_{i,j}-\cdots-F'_lS(N-l)_{i,j}\not\equiv 0\pmod {P}
$$

-   Ako je $(i,j)$ jedina pozicija koja ne zadovoljava rekurziju, nužno vrijedi:

$$
T_{i,j}:=\Big(x_{i,j}\cdot\big(S(N)_{i,j}-F'_1S(N-1)_{i,j}-\cdots-F'_lS(N-l)_{i,j}\big)\bmod P\Big)=0
$$

-   Očito to vrijedi samo kad je $x_{i,j}=0$, što ima vjerojatnost $P^{-1}$.
-   Što ako ima više pozicija koje ne zadovoljavaju rekurziju?
    -   Za svaku takvu poziciju $(i,j)$ lako se dokaže da $T_{i,j}$ ima uniformnu distribuciju na $R:=\{0,1,\cdots,P-1\}$.
    -   Zbroj (u modularnom smislu) nekoliko međusobno nezavisnih slučajnih varijabli s uniformnom distribucijom na $R$ također ima uniformnu distribuciju na $R$. Dokaz nije težak, prepuštamo ga čitatelju.
    -   Stoga je i u tom slučaju vjerojatnost greške $P^{-1}$.

### Primjer: [UOJ #552 同构判定鸭](https://uoj.ac/problem/552) („Patka za provjeru izomorfizma”) i analiza vjerojatnosti greške

???+ note "Sažetak zadatka"
    Zadana su dva usmjerena grafa $G_0,G_1$ čiji su bridovi označeni malim slovima. Za svaki od grafova odredite „multiskup stringova koji odgovaraju svim putovima” (može biti beskonačan) i provjerite jesu li ta dva multiskupa jednaka. Ako nisu, ispišite najkraći string koji se u tim multiskupovima pojavljuje različit broj puta.

Neka $f_{K,i,j}$ označava hash multiskupa svih stringova koji odgovaraju svim putovima duljine $j$ u grafu $G_K$ koji počinju u vrhu $i$. Stanja obrađujemo po rastućem $j$; pri prijelazu nabrajamo izlazne bridove vrha $i$ i propišemo da je taj brid prvi brid puta.

Da bismo provjerili postoji li loš string duljine $=L$, dovoljno je $\{f_{0,*,L}\}$ i $\{f_{1,*,L}\}$ svaki „objediniti” i usporediti (zamjenski znak `*` ovdje označava svaki vrh; npr. $\{f_{0,*,L}\}$ označava skup svih $f_{0,i,L}$ gdje $i$ prolazi svim vrhovima). U službenom rješenju[^ref2] dokazano je da duljina najkraćeg lošeg stringa (ako postoji) ne prelazi $n_1+n_2$, pa je složenost ovog rješenja pouzdana.

Razmotrimo sad konkretan način hashiranja. Uočimo da uobičajeni način hashiranja, tj. preslikavanje stringa $a_1a_2\cdots a_k$ u $\big(a_1+Pa_2+P^2a_3+\cdots+P^{k-1}a_k\big)\bmod Q$ i definiranje hasha multiskupa kao zbroja hasheva njegovih elemenata modulo $Q$, ovdje ne radi. Protuprimjer: skupovi `{"ab","cd"}` i `{"cb","ad"}` imaju jednak hash bez obzira na izbor $P$ i $Q$.

Problem je gornjeg pristupa u tome što je hash stringa zbroj, pa se svaki njegov pribrojnik može odvojiti i drukčije kombinirati. Da to izbjegnemo, hash ćemo pretvoriti u produkt. Osim toga, zbog komutativnosti množenja različite pozicije postale bi nerazlučive, pa različitim pozicijama pridružujemo različite težine.

Za svaki par $(c,j)$ (gdje je $c$ znak, a $j$ cijeli broj koji označava na kojoj se poziciji u stringu $c$ nalazi) unaprijed generiramo slučajan broj $x_{c,j}$. Zatim string $a_1a_2\cdots a_k$ preslikavamo u $x_{a_1,1}x_{a_2,2}\cdots x_{a_k,k}\bmod Q$ (gdje je $Q$ **slučajno odabran** prost broj), a hash multiskupa definiramo kao zbroj hasheva njegovih elemenata modulo $Q$. Analizirajmo vjerojatnost greške.

???+ note "(*) Schwartz–Zippelova lema"
    Neka je $f\in F[z_1,\cdots,z_k]$ polinom u $k$ varijabli stupnja $d$ nad poljem $F$ različit od nule i neka je $S$ konačan podskup od $F$. Tada najviše $d\cdot |S|^{k-1}$ uređenih $k$-torki $(z_1,\cdots,z_k)\in S^k$ zadovoljava $f(z_1,\cdots,z_k)=0$.
    
    ??? note "Ako ne znate što je polje"
        Dovoljno je zapamtiti da su sljedeće dvije stvari polja:
        
        1.  Sustav ostataka modulo prost broj s pripadnim operacijama.
        2.  Skup realnih brojeva s pripadnim operacijama.
    
    Posljedica: ako su $z_1,\cdots,z_k$ nezavisno i s jednakom vjerojatnošću slučajno odabrani iz $S$, onda je $\mathrm{Pr}\big[f(z_1,\cdots,z_k)=0\big]\leq \dfrac d{|S|}$.

Označimo s $F$ polje koje odgovara sustavu ostataka modulo $Q$. Tada za $L\leq n_1+n_2$ izrazi $\sum\limits_i f_{0,i,L}$ i $\sum\limits_i f_{1,i,L}$ odgovaraju polinomima stupnja $L$ nad $F$ u skupu varijabli $\{x_{*,*}\}$; označimo ta dva polinoma $P_0,P_1$.

Ako dva različita multiskupa stringova imaju jednak hash, postoje dvije mogućnosti:

1.  $P_0\equiv P_1\pmod {Q}$, tj. koeficijenti svih članova $P_0$ i $P_1$ podudaraju se modulo $Q$.
2.  $P_0\not\equiv P_1\pmod {Q}, P_0(x_{*,*})\equiv P_1(x_{*,*})\pmod {Q}$, tj. $P_0$ i $P_1$ nisu identički jednaki, ali odabrani skup vrijednosti $\{x_{*,*}\}$ slučajno daje jednake vrijednosti u toj točki.

Analiza vjerojatnosti prve mogućnosti:

-   Opažanje: za proizvoljne $A\neq B; A,B\leq N$ i slučajno odabran prost broj $Q\leq Q_{\max}$ nužno vrijedi:

$$
\mathrm{Pr}\big[A\equiv B\pmod {Q}\big]=O\Big(\dfrac{\log N \log Q_{max}}{Q_{max}}\Big)
$$

-   Razlog: svaki $Q$ za koji vrijedi $A\equiv B$ nužno zadovoljava $Q\big|(A-B)$, a takvih $Q$ ima $\omega(A-B)\leq \log_2 N$; prema teoremu o prostim brojevima, različitih prostih brojeva do $Q_{\max}$ ima $\Theta\Big(\dfrac {Q_{\max}}{\log Q_{\max}}\Big)$. Dijeljenjem tih dviju veličina dobivamo gornju formulu.
-   Ako u gornjem opažanju za $A,B$ (uz $A\neq B$) uzmemo koeficijente nekog određenog člana u $P_0,P_1$ (što je jednako broju pojavljivanja stringa koji odgovara tom članu u $G_0$ odnosno $G_1$), lako se vidi da je $A,B\leq (m_1+m_2)^{L}$, pa dobivamo:

$$
\mathrm{Pr}\big[A\equiv B\pmod {Q}\big]=O\Big(\dfrac{L\log (m_1+m_2) \log Q_{max}}{Q_{max}}\Big)
$$

-   Stoga je $Q_{\max}\approx 10^{12}$ više nego dovoljno. Ako računalo ne podržava računanje s tako velikim cijelim brojevima, može se upotrijebiti dvostruki hash.

Analiza vjerojatnosti druge mogućnosti:

-   U Schwartz–Zippelovoj lemi:
    -   za polje $F$ uzmemo polje koje odgovara sustavu ostataka modulo $Q$;
    -   za $f(x_{*,*})=P_0(x_{*,*})-P_1(x_{*,*})$ uzmemo polinom stupnja $L$ različit od nule;
    -   uzmemo $S=F$.
-   Dobivamo: tražena vjerojatnost $\leq \dfrac LQ$.

Uočimo da točnost moramo jamčiti za svaki $L$, pa je za potpunu strogost potrebno još primijeniti union bound (v. u nastavku).

U praksi modul ne moramo birati slučajno, jer je, primjerice, uzimanje vlastitog datuma rođenja kao modula zapravo već ekvivalentno slučajnom broju.

### Primjer: (\*) broj različitih elemenata u podmatrici

???+ note "Zadatak"
    Zadana je matrica $n\times m$ i $q$ upita o broju različitih elemenata u nekoj povezanoj podmatrici; traži se online algoritam.
    
    Dopuštena je relativna greška $\epsilon$ i vjerojatnost greške $\delta$; drugim riječima, za barem $(1-\delta)q$ upita morate dati odgovor čija relativna greška u odnosu na točan odgovor ne prelazi $\epsilon$.
    
    $n\cdot m\leq 2\cdot10^5;q\leq 10^6;\epsilon=0.5,\delta=0.2$

Lema: neka su $X_{1\cdots k}$ međusobno nezavisne slučajne varijable s uniformnom distribucijom na $[0,1]$. Tada je $\mathrm{E}\big[\min\limits_i X_i\big]=\dfrac 1{k+1}$.

-   Dokaz: promotrimo jediničnu kružnicu na kojoj se nalazi $k+1$ točaka čiji su **međusobni položaji** uniformno slučajni, redom na položajima $0,X_1,X_2,\cdots,X_k$. Tada je $\min\limits_i X_i$ jednak duljini jednog određenog od $k+1$ razmaka. Budući da su ti razmaci „simetrični”, očekivana duljina svakog određenog razmaka iznosi $\dfrac 1{k+1}$.

Uzmemo $k$ kao broj različitih elemenata i pomoću gornje leme iz $\min\limits_i X_i$ unatrag izvedemo $k$.

Upotrijebimo neku hash funkciju koja svaki element matrice uniformno i nezavisno slučajno preslikava u realan broj iz $[0,1]$, pri čemu se jednaki elementi preslikavaju u jednake realne brojeve. Tada realni brojevi koji odgovaraju svim elementima neke podmatrice, nakon uklanjanja duplikata, čine upravo jednu realizaciju skupa $\{X_1,\cdots,X_k\}$ iz leme, gdje je $k$ jednak broju različitih elemenata u podmatrici.

Tako dobivamo algoritam:

1.  Elementima matrice pridružimo hash vrijednosti iz $[0,1]$. Da bismo osigurali slučajnost, hash funkciju možemo izravno implementirati pomoću `map` i generatora slučajnih brojeva: svaki put kad naiđemo na novu, još neviđenu vrijednost, dodijelimo joj slučajan hash.
2.  Pri odgovaranju na upit odredimo minimum $M$ hash vrijednosti u podmatrici i ispišemo $\dfrac 1M-1$.

Međutim, taj algoritam nije zadovoljavajući. Očekivanje njegove izlazne vrijednosti jest $\mathrm{E}\Big[\dfrac 1{\min\limits_i X_i}-1\Big]$, a ta vrijednost zapravo nije jednaka $\dfrac 1{\mathrm{E}\big[\min\limits_i X_i\big]}-1=k$, nego je (može se dokazati) jednaka $\infty$.

Drugim riječima, ne smijemo pojedinačnu realizaciju $\min\limits_i X_i$ staviti izravno u nazivnik, nego prvo moramo izračunati njezino očekivanje i tek očekivanje staviti u nazivnik.

Kako izračunati očekivanje? Više puta slučajno uzorkujemo i uzmemo prosjek.

Gornji postupak izvedemo s $C$ različitih skupina hash funkcija; pri odgovaranju na upit izračunamo $C$ različitih vrijednosti $M$, izračunamo njihov prosjek $\overline M$ i ispišemo $\big(\overline M\big)^{-1}-1$.

Eksperimentalno se pokazuje da je $C\approx 80$ dovoljno za zadovoljavanje uvjeta. Strogi je dokaz vrlo zamoran, pa ga ovdje izostavljamo.

Naposljetku, kako pronaći minimum u podmatrici? Dovoljna je dvodimenzionalna sparse tablica (sparse table): pretpriprema $O(nm\log n\log m)$, odgovor na upit $O(1)$.

## Ostale primjene randomizacije u algoritmima

Ostale uloge randomizacije uključuju:

-   Zaštitu od ciljano konstruiranih testnih podataka kojima bi autor testova srušio rješenje. Primjerice, pri pretraživanju slučajno permutiramo redoslijed susjeda.
-   Jamčenje (u nekom smislu) uniformnosti „operacija” koje algoritam izvodi. Primjerice, algoritam [simuliranog kaljenja](../misc/simulated-annealing.md).

U tim je situacijama randomizacija često (ali ne uvijek) povezana s heurističkim „hakiranjem” i pokušajima da se izvuku parcijalni bodovi.

### Primjer: [„TJOI2015” 线性代数](https://loj.ac/problem/2100) („Linearna algebra”)

Standardno rješenje ovog zadatka jest mrežni tok, no ovdje koristimo sljedeći heuristički pristup:

-   Svaki put slučajno odaberemo položaj, invertiramo vrijednost na tom položaju, usporedimo i ažuriramo odgovor.

??? note "Kod"
    ```cpp
    #include <algorithm>
    #include <cstdlib>
    #include <iostream>
    
    int n;
    
    int a[510], b[510], c[510][510], d[510];
    int p[510], q[510];
    
    int maxans = 0;
    
    void check() {
      memset(d, 0, sizeof d);
      int nowans = 0;
      for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++) d[i] += a[j] * c[i][j];
      for (int i = 1; i <= n; i++) nowans += (d[i] - b[i]) * a[i];
      maxans = std::max(maxans, nowans);
    }
    
    int main() {
      srand(19260817);
      std::cin >> n;
      for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++) std::cin >> c[i][j];
      for (int i = 1; i <= n; i++) std::cin >> b[i];
      for (int i = 1; i <= n; i++) a[i] = 1;
      check();
      for (int T = 1000; T; T--) {
        int tmp = rand() % n + 1;
        a[tmp] ^= 1;
        check();
      }
      std::cout << maxans << '\n';
    }
    ```

### Primjer: (\*) randomizirani heap[^ref3]

Najčešća implementacija spojivog heapa (mergeable heap) vjerojatno je lijevo nagnuto stablo (leftist tree), koje održavanjem visina podstabala drži stablo nagnuto ulijevo i time jamči složenost spajanja. Međutim, održavanje visina pomalo je nezgodno i htjeli bismo ga izbjeći.

Zato možemo upotrijebiti randomizirani heap: djecu ne zamjenjujemo prema visini stabla, nego slučajno.

???+ note "Kod"
    ```cpp
    struct Node {
      int child[2];
      long long val;
    } nd[100010];
    
    int root[100010];
    
    int merge(int u, int v) {
      if (!(u && v)) return u | v;
      int x = rand() & 1, p = nd[u].val > nd[v].val ? u : v;
      nd[p].child[x] = merge(nd[p].child[x], u + v - p);
      return p;
    }
    
    void pop(int &now) { now = merge(nd[now].child[0], nd[now].child[1]); }
    ```

Randomizirani heap ne postavlja nikakve stroge ni meke zahtjeve na oblik heapa; očekivana složenost operacije spajanja vrijedi za bilo koja dva heapa (kao argumente funkcije `merge`). Dokazujemo u nastavku.

???+ note "Dokaz očekivane složenosti"
    Dokazat ćemo: za proizvoljan heap $A$, ako od korijena svaki put slučajno krenemo lijevo ili desno (dok više ne možemo dalje), očekivana duljina puta (tj. broj vrhova na putu) iznosi $h(A)\leq\log_2 (|A|+1)$.
    
    -   Uočimo da je u gornjem postupku očekivana složenost spajanja heapova $A,B$ jednaka $O\big(h(A)+h(B)\big)$, pa gornja tvrdnja jamči očekivanu složenost randomiziranog heapa.
    
    Dokaz provodimo matematičkom indukcijom. Bazni je slučaj prazan $A$, za koji je tvrdnja očita. Dalje pretpostavljamo da $A$ nije prazan.
    
    Neka su $L,R$ dva podstabla od $A$. Tada:
    
    $$
    \begin{align} h(A)
    &=1+\frac{h(L)+h(R)}2
    \\&\leq1+\frac{\log_2(|L|+1)+\log_2(|R|+1)}2
    \\&=\log_2{2\sqrt{(|L|+1)(|R|+1)}}
    \\&\leq\log_2{\frac{2\big((|L|+1)+(|R|+1)\big)}2}
    \\&=\log_2{(|A|+1)} \end{align}
    $$
    
    Time je dokaz završen.

## Dokazne tehnike povezane sa slučajnošću

U nastavku navodimo nekoliko korisnijih tehnika.

Naravno, ovih nekoliko tehnika nikako nije sve; ako znate neku tehniku koja nije navedena, slobodno je dopunite.

### Analiza gornjih ograda vjerojatnosti

Više na stranici [Vjerojatnosne nejednakosti](../math/probability/concentration-inequality.md).

Osim nejednakosti spomenutih na toj stranici, u izvodima se često koristi i sljedeći rezultat:

**Upotreba Eulerova broja**: $\Big(1-\dfrac{1}{n}\Big)^n\leq \dfrac{1}{\mathrm{e}},\forall n\geq1$

-   Lijeva je strana monotono rastuća po $n\geq 1$ i njezin je limes u $+\infty$ jednak $\dfrac{1}{\mathrm{e}}$, odakle slijedi tvrdnja.
-   To nam govori: ako imamo $n$ međusobno nezavisnih događaja od kojih se svaki događa s vjerojatnošću $1-\dfrac 1n$, vjerojatnost da se svi dogode iznosi najviše $\dfrac{1}{\mathrm{e}}$.

### Ideja „sprezanja”

Ideja „sprezanja” (coupling) često se koristi kad istodobno obrađujemo više od jednog slučajnog objekta ili kad istodobno obrađujemo slučajan i deterministički objekt.

#### Uvod: povezanost slučajnog grafa

???+ note "Zadatak"
    Za $n \in \mathbf{N}^*; p,q\in [0,1]$ uz $q\leq p$ dokažite: očekivani broj komponenata povezanosti slučajnog grafa $G_1(n,p)$ ne prelazi očekivani broj komponenata povezanosti slučajnog grafa $G_2(n,q)$. Ovdje $G(n,\alpha)$ označava jednostavan neusmjereni graf $G$ s $n$ vrhova u kojem se svaki od $\dfrac {n(n-1)}2$ mogućih bridova pojavljuje s vjerojatnošću $\alpha$, pri čemu su te vjerojatnosti međusobno nezavisne.

Ova tvrdnja izgleda posve prirodno, no strogi dokaz nije tako jednostavan.

???+ note "Ideja dokaza"
    Zamislimo da svaki od tih dvaju grafova koristi generator slučajnih bitova 0/1 kako bi odredio postoji li svaki brid: generator $T_1$ grafa $G_1$ svaki put ispisuje 1 s vjerojatnošću $p$, a generator $T_2$ grafa $G_2$ svaki put ispisuje 1 s vjerojatnošću $q$. Tako je za konstrukciju grafa dovoljno odgovarajući generator pokrenuti $\dfrac {n(n-1)}2$ puta.
    
    Sad ta dva generatora spojimo u jedan. Promotrimo generator slučajnih brojeva $T$ koji svaki put ispisuje 0 s vjerojatnošću $q$, 1 s vjerojatnošću $p-q$ i 2 s vjerojatnošću $1-p$. Ako $T$ pokrenemo $\dfrac {n(n-1)}2$ puta, možemo istodobno konstruirati i $G_1$ i $G_2$. Konkretno, ako je izlaz 0, smatramo da promatranog brida nema ni u $G_1$ ni u $G_2$; ako je izlaz 1, smatramo da je promatrani brid samo u $G_1$; ako je izlaz 2, smatramo da je promatrani brid i u $G_1$ i u $G_2$.
    
    Lako se provjeri da tako generirani $G_1$ i $G_2$ odgovaraju svojim definicijama i da je u svakoj realizaciji skup bridova $G_2$ podskup skupa bridova $G_1$. Stoga je u svakoj realizaciji broj komponenata povezanosti $G_2$ barem jednak broju komponenata povezanosti $G_1$; tada, naravno, i očekivanja zadovoljavaju isti odnos.

Ideja upotrijebljena u ovom dokazu zove se „sprezanje” i može se shvatiti doslovno. U ovom se primjeru očituje kao spajanje dvaju inače nezavisnih slučajnih procesa u jedan.

#### Primjena: [NERC 2019 Problem G: Game Relics](https://codeforces.com/contest/1267/problem/G)

???+ note "Sažetak zadatka"
    Zadano je nekoliko predmeta, svaki s cijenom $c_i$. Želite dobiti sve predmete, a za to možete proizvoljno izvoditi dvije operacije:
    
    1.  Odaberete predmet $i$ koji još nemate i kupite ga za $c_i$ novčića.
    2.  Platite $x$ novčića i s jednakom vjerojatnošću slučajno izvučete jedan od svih predmeta (uključujući one koje već imate). Ako taj predmet još nemate, dobivate ga; inače ne dobivate ništa, ali vam se vraća $\dfrac x2$ novčića. $x$ je konstanta zadana na ulazu.
    
    Odredite očekivani trošak uz optimalnu strategiju.

Opažanje: ako odlučimo izvlačiti, sigurno ćemo izvlačiti sve dok ne dobijemo novi predmet.

-   Razlog: ako izvlačenjem nismo dobili novi predmet, nova je situacija potpuno jednaka situaciji prije izvlačenja, pa ako je u staroj situaciji optimalan potez bio „izvuci jedanput”, onda je u novoj situaciji optimalan potez sigurno „izvuci još jedanput”.

Možemo izračunati $f_k$: ako trenutačno imamo $k$ različitih predmeta, koliko očekivano moramo platiti da izvlačenjem dobijemo novi predmet. Prema upravo iznesenom opažanju, $f_k$ možemo smatrati fiksnom cijenom, tj. zadatak pretvaramo u „svaki put platimo $f_k$ novčića i slučajno dobijemo jedan novi predmet”.

???+ note "Računanje očekivane cijene"
    Očito je $f_k=\dfrac x2 \cdot (R-1)+x$, gdje je $R$ očekivani broj izvlačenja potrebnih za dobivanje novog predmeta.
    
    Lema: ako novčić pada na glavu s vjerojatnošću $p$, očekivani broj bacanja do prve glave iznosi $\dfrac 1p$.
    
    -   Intuitivno: $\dfrac 1p \cdot p = 1$, pa u toliko bacanja očekujemo 1 glavu, što izgleda ispravno.
    -   Ta se intuicija može učiniti strogom pomoću [zakona velikih brojeva](https://en.wikipedia.org/wiki/Law_of_large_numbers), tj. promatranjem $n\to \infty$ pokusa „bacaj novčić dok ne padne glava”. Detalje izvoda izostavljamo.
    -   Drugi je mogući dokaz izravno uvrstiti definiciju očekivanja i izračunati. Detalje izvoda izostavljamo.
    
    Očito je vjerojatnost da jednim izvlačenjem dobijemo novi predmet $\dfrac {n-k}n$, pa je $R=\dfrac n{n-k}$.

Zaključak: optimalna je strategija nužno prvo nekoliko puta izvlačiti, a zatim kupiti sve predmete koji nisu izvučeni.

Taj je zaključak u skladu s intuicijom, jer $f_k$ raste s $k$, pa se čini da je ranije izvlačenje doista malo bolje od kasnijeg.

???+ note "Dokaz"
    Prvo dokazujemo poseban slučaj. Dokazat ćemo:
    
    -   slučajni proces $A$: prvo kupimo predmet $x$, zatim izvlačimo dok ne dobijemo sve predmete
    -   ... sigurno nije bolji od ...
    -   slučajnog procesa $B$: izvlačimo dok ne dobijemo sve predmete osim $x$, a zatim, ako još nemamo $x$, kupimo ga.
    
    Neka slučajni procesi $A$ i $B$ koriste isti generator slučajnih brojeva. Drugim riječima, prvo izvlačenje u $A$ i prvo izvlačenje u $B$ daju isti element, a isto vrijedi za drugo, treće ...
    
    Očito su tada brojevi izvlačenja u $A$ i $B$ nužno jednaki. Za predmet $y\neq x$ koji $A$ izvuče uočavamo:
    
    -   broj predmeta koje $A$ posjeduje u trenutku izvlačenja $y$ sigurno je veći ili jednak broju predmeta koje $B$ posjeduje u trenutku izvlačenja $y$.
    
    Stoga cijena jednog izvlačenja u $B$ nije veća od cijene jednog izvlačenja u $A$, pa ni ukupna cijena izvlačenja nije veća nego u $A$.
    
    Očito ni trošak kupnje u $B$ nije veći nego u $A$. Ukupno, $B$ sigurno nije lošiji od $A$.
    
    Zatim se matematičkom indukcijom ta tvrdnja proširuje na opći slučaj. Konkretno, svaki put pronađemo posljednju kupnju u trenutačnoj strategiji i prema gornjoj tvrdnji njezino premještanje na kraj sigurno nije lošije. Detalje izostavljamo.

Na temelju tog zaključka još jedanput ekvivalentno preoblikujemo zadatak: operaciju „odaberi predmet i kupi ga za pripadnu cijenu” zamijenimo operacijom „slučajno odaberi predmet koji još nemaš i kupi ga za pripadnu cijenu”. Ekvivalentnost vrijedi zato što, budući da se kupnja koristi samo za „čišćenje” na kraju, nije važno koji predmet odaberemo.

Sad vidimo da su „izvlačenje” i „kupnja” u biti postale ista operacija; razlikuju se samo u plaćenoj cijeni. Izbor između kupnje i izvlačenja uopće ne utječe na redoslijed dobivanja predmeta, a svaki je redoslijed dobivanja predmeta jednako vjerojatan.

Opažanje: u nekom trenutku trebamo odabrati kupnju ako i samo ako je cijena sljedećeg izvlačenja (određena brojem već izvučenih predmeta) veća od prosječne cijene preostalih predmeta (ako su jednake, svejedno je).

-   Može se dokazati da s vremenom brzina rasta cijene izvlačenja nije manja od brzine rasta prosječne cijene preostalih predmeta. To znači da postoji samo jedna „granična točka” prelaska s izvlačenja na kupnju, što dodatno potvrđuje raniji zaključak.

Naposljetku nabrojimo sve moguće situacije (tj. skupove već posjedovanih elemenata), izračunamo vjerojatnost pojavljivanja svake situacije (broj permutacija posjedovanih elemenata podijeljen ukupnim brojem permutacija), pomnožimo je s cijenom optimalne odluke u toj situaciji (određenom brojem posjedovanih elemenata i ukupnom cijenom preostalih predmeta) i sve zbrojimo. Taj se postupak može optimizirati DP-om nalik na problem naprtnjače (knapsack), čime se zadatak rješava.

***

**Osvrt**: vidimo da je tehnika sprezanja u ovom zadatku upotrijebljena dvaput. Prvi put u dokazu, gdje smo dvama slučajnim procesima dali isti izvor slučajnosti; drugi put pri pretvaranju kupnje u slučajnu kupnju (tj. uvođenju izvora slučajnosti), čime su kupnja i izvlačenje u biti „spregnute” u istu operaciju (tj. izvlačenje i kupnja dijele isti izvor slučajnosti).

## Literatura

[^ref1]: [PANIC - Editorial](https://discuss.codechef.com/t/panic-editorial/80145)

[^ref2]: [UOJ NOI Round #4 Day2 题解](https://peehs-moorhsum.blog.uoj.ac/blog/6375) (rješenja)

[^ref3]: [Anna Gambin and Adam Malinowski, Randomized Meldable Priority Queues](https://www.researchgate.net/publication/2801527_Randomized_Meldable_Priority_Queues)
