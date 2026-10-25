---
title: Osnove teorije izračunavanja
---

Ovaj dio predstavlja osnovna znanja iz teorije izračunavanja. Taj sadržaj u OI-ju nema veliku ulogu (ali ipak ponešto koristi: ako naiđete na NP-težak problem, možete smatrati da za njega ne postoji rješenje polinomne složenosti), pa ga možete upoznati iz interesa ili kao pripremu za daljnje učenje.

Mnogi zaključci u ovom tekstu navedeni su bez dokaza; ako vas zanima, odgovarajuće dokaze možete potražiti sami.

Predznanje: [Vremenska složenost](../basic/complexity.md).

## Problemi

### Jezici

**Abeceda** (alphabet) neprazan je konačan skup; elementi tog skupa nazivaju se **simboli/znakovi** (symbols).

Neka $\Sigma^\ast$ označava skup nizova nastalih nadovezivanjem nenegativnog broja znakova iz $\Sigma$; **jezik** (language) nad abecedom $\Sigma$ podskup je od $\Sigma^\ast$.

Treba napomenuti da je „jezik” ovdje apstraktan pojam: nizovi znakova u uobičajenom smislu jesu jezik, ali i skup svih usmjerenih acikličkih grafova može biti jezik (između 01-nizova i usmjerenih grafova može se uspostaviti bijekcija; konkretan način nije potrebno znati).

Budući da se svaki jezik može pretvoriti u oblik 01-nizova, u nastavku je, ako nije drukčije rečeno, $\Sigma=\{0, 1\}$.

### Problemi odlučivanja

Problem odlučivanja (decision problem) problem je na koji se može odgovoriti samo s DA/NE; u biti je to odlučivanje pripada li niz nekom jeziku, tj. $f:\Sigma^\ast\rightarrow\{0, 1\}, f(x)=1\iff x\in L$ problem je odlučivanja za abecedu $\Sigma$ i jezik $L$. Na primjer, „odlučiti je li graf usmjeren aciklički graf” jest problem odlučivanja.

Problemi odlučivanja zbog svoje su jednostavnosti čest predmet proučavanja teorije izračunavanja. Ako nije drukčije rečeno, „problem” u ovom tekstu znači „problem odlučivanja”; dakako, neke se tvrdnje ponekad mogu jednostavno poopćiti i na druge probleme.

Jezik može označavati i problem odlučivanja „odlučiti pripada li niz tom jeziku”, pa se „jezik” i „problem” mogu smatrati sinonimima.

### Funkcijski problemi

Odgovor na funkcijski problem (function problem) nije samo DA/NE; može biti broj ili nešto drugo. Na primjer, „izračunati zbroj dvaju brojeva” funkcijski je problem.

Svaki se funkcijski problem može pretvoriti u problem odlučivanja; na primjer, „izračunati zbroj dvaju brojeva” može se pretvoriti u „odlučiti je li zbroj dvaju brojeva jednak trećem broju”.

I problem odlučivanja može se pretvoriti u funkcijski problem: izračunati indikatorsku funkciju tog problema odlučivanja, tj. funkciju $f$ iz gornje definicije problema odlučivanja.

## Turingov stroj

### Deterministički Turingov stroj

Ako nije drukčije rečeno, „Turingov stroj” obično znači „deterministički Turingov stroj”; tako je i u ovom tekstu.

Postoji mnogo različitih definicija Turingova stroja; ovdje biramo jednu od njih, a Turingovi strojevi prema drugim definicijama obično su po računskoj moći ekvivalentni Turingovu stroju definiranom u nastavku.

Turingov stroj jest stroj koji radi na traci koja se beskonačno proteže u oba smjera i podijeljena je na ćelije; stroj ima unutarnja stanja i glavu koja se po traci može pomicati i mijenjati njezin sadržaj.

Formalno, Turingov stroj jest sedmorka $M=\langle Q,\Gamma,b,\Sigma,\delta,q_0,F\rangle$, gdje je:

-   $Q$ konačan neprazan **skup stanja**;
-   $\Gamma$ konačna neprazna **abeceda trake**;
-   $b\in\Gamma$ **prazni znak**, jedini znak koji se tijekom izračunavanja smije na traci pojavljivati beskonačno često;
-   $\Sigma\subseteq(\Gamma\setminus\{b\})$ **skup ulaznih simbola**, znakovi koji se smiju pojaviti na početnoj traci (tj. u ulazu);
-   $q_0\in Q$ **početno stanje**;
-   $F\subseteq Q$ skup **prihvaćajućih stanja**; ako se Turingov stroj zaustavi u nekom prihvaćajućem stanju, kažemo da je sadržaj početne trake **prihvaćen** tim Turingovim strojem.
-   $\delta :(Q\setminus F)\times \Gamma \not \to Q\times \Gamma \times \{L,R\}$ parcijalna funkcija (tj. funkcija definirana samo na podskupu domene) koja se naziva **funkcija prijelaza**. Ako $\delta$ u trenutnom stanju nije definirana, Turingov stroj se zaustavlja.

Turingov stroj počinje od početnog stanja i početka trake te u svakom koraku djeluje prema trenutnom unutarnjem stanju $x$ i znaku $y$ u ćeliji trake na koju trenutačno pokazuje glava: ako $\delta(x, y)$ nije definirano, zaustavlja se; inače, ako je $\delta(x, y)=(a, b, c)$, unutarnje stanje mijenja u $a$, znak u ćeliji na koju pokazuje glava mijenja u $b$, a ako je $c$ jednako $L$, pomiče se za jednu ćeliju ulijevo, a ako je $R$, za jednu ćeliju udesno.

Zapravo, nije nužno znati pojedinosti rada Turingova stroja; dovoljno je steći intuitivno razumijevanje.

Izlaz Turingova stroja $M$ na ulazu $x$ označavamo $M(x)$ ($M(x)=1$ ako i samo ako $M$ prihvaća $x$, a $M(x)=0$ ako i samo ako se $M$ na ulazu $x$ zaustavlja u konačno mnogo koraka i $M$ ne prihvaća $x$); u zagradi može biti i više argumenata odvojenih zarezima, a u konkretnoj implementaciji abecedi se može dodati element koji predstavlja zarez i razdvaja argumente.

Vremenska složenost rješavanja problema na Turingovu stroju i na von Neumannovu računalu razlikuje se najviše za polinomni faktor, pa se pri proučavanju klasa složenosti Turingov stroj može koristiti kao računski model.

### Nedeterministički Turingov stroj

Nedeterministički Turingov stroj vrsta je Turingova stroja; od determinističkoga se razlikuje po tome što deterministički Turingov stroj u svakom koraku može prijeći samo u jedno stanje, dok nedeterministički može „istodobno” prijeći u više stanja i tako paralelno računati u više „grana”; čim se jedna od tih „grana” zaustavi u prihvaćajućem stanju, nedeterministički Turingov stroj prihvaća ulaz.

Zapravo, svaki deterministički Turingov stroj može, na način sličan iterativnom produbljivanju (iterative deepening), u eksponencijalnom vremenu simulirati polinomno dugo izvođenje nedeterminističkog Turingova stroja.

U stvarnom životu deterministički Turingov stroj odgovara jednojezgrenom procesoru koji podržava samo serijsku obradu, a nedeterministički Turingov stroj idealnom višejezgrenom procesoru koji podržava paralelnu obradu neograničene veličine.

### Višetračni Turingov stroj

Standardni Turingov stroj radi samo na jednoj traci, ali radi jednostavnosti u ovom tekstu proučavamo višetračne Turingove strojeve. Kod Turingova stroja s $k$ traka jedna je traka ulazna traka samo za čitanje, a preostalih $k-1$ traka može se čitati i pisati; među tih $k-1$ traka jedna služi kao izlazna.

Broj traka višetračnog Turingova stroja mora biti konačan.

Prostor koji višetračni Turingov stroj koristi jest broj ćelija koje su glave posjetile na svim trakama osim ulazne.

### Kodiranje Turingovih strojeva

Turingovi strojevi mogu se kodirati prirodnim brojevima, tj. postoji surjekcija $f:\mathbb{N}\to\mathbb{M}$ takva da svakom prirodnom broju odgovara jedan Turingov stroj, a svaki Turingov stroj ima beskonačno mnogo kodova. Stoga skup sastavljen od nekoliko Turingovih strojeva može biti jezik.

Turingov stroj kodiran prirodnim brojem $\alpha$ označavamo $M_{\alpha}$.

### Univerzalni Turingov stroj

Postoji Turingov stroj $\mathcal U$ koji zadovoljava:

1.  ako se $M_{\alpha}$ na ulazu $x$ zaustavlja u konačnom vremenu, tada je $\mathcal{U}(x, \alpha)=M_{\alpha}(x)$, a inače se $\mathcal{U}(x, \alpha)$ ne zaustavlja u konačnom vremenu;
2.  ako se za svaki $x\in\{0, 1\}^\ast$ stroj $M_\alpha$ na ulazu $x$ zaustavlja u vremenu $T(|x|)$, tada se za svaki $x\in\{0, 1\}^\ast$ stroj $\mathcal{U}(x, \alpha)$ zaustavlja u vremenu $O(T(|x|)\log T(|x|))$.

Drugim riječima: postoji univerzalni Turingov stroj koji može simulirati bilo koji Turingov stroj, a pritom je sporiji od simuliranog stroja samo za faktor logaritma njegova vremena izvođenja.

## Izračunljivost

### Neizračunljivi problemi

Ako za problem odlučivanja postoji Turingov stroj koji se uvijek zaustavlja u konačno mnogo koraka i ispravno odlučuje, taj je problem **Turing-izračunljiv**; inače je problem **Turing-neizračunljiv**.

Budući da se Turingovi strojevi mogu kodirati prirodnim brojevima, Turingovih strojeva ima prebrojivo beskonačno mnogo, dok jezika (tj. skupova binarnih nizova) ima neprebrojivo beskonačno mnogo, a svaki Turingov stroj odlučuje najviše jedan jezik; stoga sigurno postoje Turing-neizračunljivi problemi.

### Problem zaustavljanja

Problem zaustavljanja (halting problem) klasičan je Turing-neizračunljiv problem: za zadane $\alpha$ i $x$ odlučiti hoće li se $M_{\alpha}$ na ulazu $x$ zaustaviti u konačno mnogo koraka.

??? note "Dokaz da je problem zaustavljanja Turing-neizračunljiv"
    Definirajmo funkciju $\mathsf{UC}:\{0,1\}^\ast\to\{0,1\}$ kao:
    
    $$
    \mathsf{UC}(\alpha)=\begin{cases}0&M_\alpha(\alpha)=1\\1&\text{otherwise}\end{cases}
    $$
    
    Najprije dokazujemo da je funkcija $\mathsf{UC}$ Turing-neizračunljiva:
    
    Pretpostavimo da postoji Turingov stroj $M_{\beta}$ koji računa $\mathsf{UC}$. Prema definiciji od $\mathsf{UC}$ dobivamo $\mathsf{UC}(\beta)=1\iff M_\beta(\beta)\neq 1$, a iz toga što $M_{\beta}$ računa $\mathsf{UC}$ dobivamo $M_{\beta}(\beta)=\mathsf{UC}(\beta)$, što je proturječje; dakle, pretpostavka ne vrijedi i ne postoji Turingov stroj koji računa $\mathsf{UC}$.
    
    Neka je $M_{\mathsf{HALT}}$ Turingov stroj koji rješava problem zaustavljanja; vrijednost $M_{\mathsf{HALT}}(x,\alpha)$ rješenje je problema odlučivanja hoće li se $M_\alpha$ na ulazu $x$ zaustaviti u konačno mnogo koraka. Tada možemo konstruirati Turingov stroj $M_{\mathsf{UC}}$ koji računa funkciju $\mathsf{UC}$:
    
    $M_\mathsf{UC}$ najprije poziva $M_\mathsf{HALT}(α,α)$; ako on vrati $0$, tada je $M_\mathsf{UC}(α)=1$; inače $M_\mathsf{UC}$ univerzalnim Turingovim strojem simulira izračun i dobiva odgovor.
    
    Budući da je funkcija $\mathsf{UC}$ Turing-neizračunljiva, $M_\mathsf{HALT}$ ne postoji, što znači da je problem zaustavljanja Turing-neizračunljiv.

## Church–Turingova teza

Church–Turingova teza kaže: ako se neka klasa problema može riješiti efektivnom metodom, onda tu klasu problema može riješiti neki Turingov stroj.

Pritom „efektivna metoda” mora zadovoljavati:

1.  sastoji se od konačno mnogo jasnih uputa;
2.  kad se njome rješava jedan od problema iz te klase, metoda mora završiti u konačno mnogo koraka i dati točan odgovor.

Ta teza nije dokazana, ali je temeljni aksiom teorije izračunavanja.

## Klase složenosti

Klasa složenosti ima mnogo; ovaj tekst predstavlja samo manji dio onih češćih.

### R i RE

Za jezik $L$ i Turingov stroj $M$: ako se $M$ na svakom ulazu zaustavlja u konačno mnogo koraka i vrijedi $M(x)=1\iff x\in L$, kažemo da $M$ **odlučuje** $L$.

Za jezik $L$ i Turingov stroj $M$: ako se $M$ na svakom ulazu koji pripada $L$ zaustavlja u konačno mnogo koraka i vrijedi $M(x)=1\iff x\in L$, kažemo da $M$ **prepoznaje** $L$.

Klasa složenosti $\mathsf R$ skup je jezika koje odlučuje neki Turingov stroj, tj. svih Turing-izračunljivih jezika.

Klasa složenosti $\mathsf{RE}$ skup je jezika koje prepoznaje neki Turingov stroj. $\mathsf{RE}$ se naziva i klasom rekurzivno prebrojivih jezika.

Iz definicije slijedi $\mathsf{R}\subseteq\mathsf{RE}$.

### DTIME

Ako postoji deterministički Turingov stroj koji odlučuje jezik i za svaki ulaz $x$ zaustavlja se u vremenu $O(f(|x|))$, tada taj jezik pripada klasi $\mathsf{DTIME}(f(n))$.

### P

Klasa složenosti $\mathsf P$ označava probleme odlučivanja koje deterministički Turingov stroj može riješiti u polinomnom vremenu, tj.:

$$
\mathsf{P}=\bigcup\limits_{k\in\mathbb{N}}\mathsf{DTIME}(n^k)
$$

Linearno programiranje, računanje najvećeg zajedničkog djelitelja i inačica odlučivanja problema najvećeg sparivanja u grafu problemi su klase $\mathsf P$.

### EXPTIME

Klasa složenosti $\mathsf{EXPTIME}$ označava probleme odlučivanja koje deterministički Turingov stroj može riješiti u eksponencijalnom vremenu, tj.:

$$
\mathsf{EXPTIME}=\bigcup\limits_{k\in\mathbb{N}}\mathsf{DTIME}(2^{n^k})
$$

Oslabljena inačica problema zaustavljanja — za zadani kod Turingova stroja i pozitivan cijeli broj $k$ odlučiti zaustavlja li se taj Turingov stroj unutar $k$ koraka — problem je klase $\mathsf{EXPTIME}$. Naime, rješenje tog problema treba $O(k)$ vremena, a broj $k$ može se kodirati binarnim nizom duljine $O(\log k)$.

### NTIME

Ako postoji nedeterministički Turingov stroj koji odlučuje jezik i za svaki ulaz $x$ zaustavlja se u vremenu $O(f(|x|))$, tada taj jezik pripada klasi $\mathsf{NTIME}(f(n))$.

### NP

Klasa složenosti $\mathsf{NP}$ označava probleme odlučivanja koje nedeterministički Turingov stroj može riješiti u polinomnom vremenu, tj.:

$$
\mathsf{NP}=\bigcup\limits_{k\in\mathbb{N}}\mathsf{NTIME}(n^k)
$$

Svi problemi klase $\mathsf P$ ujedno su problemi klase $\mathsf{NP}$. Za više problema klase $\mathsf{NP}$ pogledajte NPC probleme i NP-intermediate probleme u nastavku.

#### NP-hard

Ako se svi problemi klase $\mathsf{NP}$ mogu u polinomnom vremenu reducirati na problem $H$, tada je problem $H$ NP-težak (NP-hard).

Drugim riječima, kad bi se NP-težak problem $H$ mogao riješiti u jednoj jedinici vremena, svi bi se problemi klase $\mathsf{NP}$ mogli riješiti u polinomnom broju jedinica vremena.

#### NP-complete

Ako je problem i problem klase $\mathsf{NP}$ i NP-težak, tada je taj problem NP-potpun (NP-complete), odnosno riječ je o NPC problemu.

Neki klasični NPC problemi: inačica odlučivanja problema trgovačkog putnika, inačica odlučivanja problema najvećeg nezavisnog skupa, inačica odlučivanja problema najmanjeg vršnog pokrivača, inačica odlučivanja problema najduljeg puta, inačica odlučivanja 0-1 cjelobrojnog programiranja, problem pokrivanja skupa, problem bojenja grafa, problem ruksaka, problem trodimenzionalnog sparivanja, inačica odlučivanja problema najvećeg reza.

Funkcijske inačice NPC problema obično su NP-teške; na primjer, „odlučiti postoji li u grafu klika veličine $k$” i problem je klase $\mathsf{NP}$ i NP-težak, pa je NPC problem, dok njegova funkcijska inačica „pronaći najveću kliku grafa” nije NPC problem, ali je ta funkcijska inačica i dalje NP-teška.

Slično tome, i druge klase složenosti imaju „XX-complete” probleme; na primjer, svi problemi klase $\mathsf{EXPTIME}$ mogu se u polinomnom vremenu reducirati na EXPTIME-potpun (EXPTIME-complete) problem.

#### co-NP

Problem je problem klase $\mathsf{co-NP}$ ako i samo ako je njegov komplement problem klase $\mathsf{NP}$. Shvatimo li „problem” kao „jezik”, a „jezik” kao podskup od $\Sigma^\ast$, jasno je što znači „komplement”.

Na primjer: „za zadanih $n$ podskupova odlučiti može li se među njima odabrati $k$ koji pokrivaju cijeli skup” NPC je problem, a njegov komplement „za zadanih $n$ podskupova odlučiti vrijedi li da nikojih $k$ od njih ne pokriva cijeli skup” problem je klase $\mathsf{co-NP}$. Ako je odgovor na prvi problem „da”, to je kao da smo pronašli protuprimjer za drugi problem, pa je odgovor na drugi problem „ne”.

#### NP-intermediate

Ako je problem problem klase $\mathsf{NP}$, ali nije ni problem klase $\mathsf{P}$ ni NPC problem, nazivamo ga NP-intermediate problemom.

Prema današnjim spoznajama, problem izomorfizma grafova, problem diskretnog logaritma i problem faktorizacije možda su NP-intermediate.

Ladnerov teorem kaže da, ako je $\mathsf{P}\ne\mathsf{NP}$, sigurno postoje problemi koji su NP-intermediate.

### NEXPTIME

Klasa složenosti $\mathsf{NEXPTIME}$ označava probleme odlučivanja koje nedeterministički Turingov stroj može riješiti u eksponencijalnom vremenu, tj.:

$$
\mathsf{NEXPTIME}=\bigcup\limits_{k\in\mathbb{N}}\mathsf{NTIME}(2^{n^k})
$$

### #P

Problemi klase $\mathsf{\#P}$ nisu problemi odlučivanja, nego problemi prebrojavanja vezani uz probleme klase $\mathsf{NP}$: prebrojati rješenja problema klase $\mathsf{NP}$ problem je klase $\mathsf{\#P}$. Drugim riječima, prebrojati u koliko se grana nedeterminističkog Turingova stroja koji se uvijek zaustavlja u polinomnom vremenu niz prihvaća problem je klase $\mathsf{\#P}$.

Brojanje sparivanja ili savršenih sparivanja u općem ili bipartitnom grafu #P-potpuno je, a pripadni je problem odlučivanja „odlučiti postoji li u grafu (savršeno) sparivanje”.

### DSPACE

Ako postoji deterministički Turingov stroj koji na ulazu $x$ odlučuje jezik u prostoru $O(f(|x|))$, tada taj jezik pripada klasi $\mathsf{DSPACE}(f(n))$.

-   $\mathsf{REG}=\mathsf{DSPACE}(O(1))$, tj. regularni jezici, odnosno jezici koje mogu odlučiti automati.

-   $\mathsf{L}=\mathsf{DSPACE}(O(\log n))$; treba imati na umu da prostor koji Turingov stroj koristi ne uključuje prostor koji zauzima ulaz.

-   $\mathsf{PSPACE}=\bigcup\limits_{k\in\mathbb N}\mathsf{DSPACE}(n^k)$

-   $\mathsf{EXPSPACE}=\bigcup\limits_{k\in\mathbb N}\mathsf{DSPACE}(2^{n^k})$

### NSPACE

Ako postoji nedeterministički Turingov stroj koji na ulazu $x$ odlučuje jezik u prostoru $O(f(|x|))$, tada taj jezik pripada klasi $\mathsf{NSPACE}(f(n))$.

-   $\mathsf{REG}=\mathsf{DSPACE}(O(1))=\mathsf{NSPACE}(O(1))$

-   $\mathsf{NL}=\mathsf{NSPACE}(O(\log n))$

-   $\mathsf{CSL}=\mathsf{NSPACE}(O(n))$, tj. kontekstno ovisni jezici.

-   $\mathsf{PSPACE}=\mathsf{NPSPACE}=\bigcup\limits_{k\in\mathbb N}\mathsf{NSPACE}(n^k)$

-   $\mathsf{EXPSPACE}=\mathsf{NEXPSPACE}=\bigcup\limits_{k\in\mathbb N}\mathsf{NSPACE}(2^{n^k})$

## Polinomno vrijeme

Jednostavno rečeno, ako postoji pozitivan broj $k$ takav da je vremenska složenost algoritma $O(n^k)$ (pazite, ne $\Theta(n^k)$), gdje je $n$ veličina problema (duljina ulaza), kažemo da je algoritam **polinomnog vremena**. Ako se problem može riješiti algoritmom polinomnog vremena (na determinističkom Turingovu stroju), tada problem pripada klasi složenosti $\mathsf{P}$.

Polinomno vrijeme dijeli se na jako polinomno i slabo polinomno vrijeme; osim toga postoji i pseudopolinomno vrijeme.

### Strongly polynomial time – jako polinomno vrijeme

Najprije definirajmo računski model koji nazivamo aritmetičkim modelom. U aritmetičkom modelu aritmetičke operacije nad brojevima (zbrajanje, oduzimanje, množenje, dijeljenje, usporedba) izvode se u jediničnom vremenu (tj. u vremenu $O(1)$, neovisno o veličini brojeva).

Ako je broj operacija algoritma u aritmetičkom modelu polinoman u broju brojeva u ulazu, a prostorna složenost polinomna u veličini ulaza (a ne u broju brojeva), tada je taj algoritam **jako polinomnog vremena**. Budući da se aritmetičke operacije u uobičajenom računskom modelu mogu izvesti u vremenu polinomnom u veličini ulaza (tj. u logaritmu veličine brojeva), algoritam jako polinomnog vremena sigurno je polinomnog vremena.

Općenito, vremenska složenost algoritma jako polinomnog vremena ne ovisi o rasponu vrijednosti.

### Weakly polynomial time – slabo polinomno vrijeme

Ako je algoritam polinomnog vremena, ali nije jako polinomnog vremena, tada je **slabo polinomnog vremena**.

Na primjer, Euklidov algoritam za računanje najvećeg zajedničkog djelitelja, vremenske složenosti $O(\log a + \log b)$ ($a$ i $b$ veličine su ulaznih brojeva), slabo je polinomnog vremena.

### Pseudo-polynomial time – pseudopolinomno vrijeme

Ako je vrijeme izvođenja algoritma polinomno u rasponu vrijednosti, kažemo da je algoritam **pseudopolinomnog vremena**. Algoritam pseudopolinomnog vremena može, ali i ne mora biti polinomnog vremena; razlog zašto možda nije polinomnog vremena jest to što je za prikaz pozitivnog cijelog broja veličine $n$ općenito potrebno samo $O(\log n)$ binarnih znamenaka, pa je algoritam polinoman u rasponu vrijednosti obično eksponencijalan u duljini ulaza. Iako po definiciji pseudopolinomno vrijeme može biti i polinomno vrijeme, kad kažemo da je algoritam pseudopolinomnog vremena, obično mislimo da nije polinomnog vremena.

Na primjer, problem ruksaka NP-težak je problem, ali ima rješenje pseudopolinomnog vremena temeljeno na dinamičkom programiranju.

Ako NPC/NP-težak problem ima rješenje pseudopolinomnog vremena, kažemo da je problem **slabo NPC**/**slabo NP-težak**. Ako NPC/NP-težak problem, uz pretpostavku $\mathsf{P} \ne \mathsf{NP}$, nema rješenje pseudopolinomnog vremena, kažemo da je problem **jako NPC**/**jako NP-težak**.

## Konstruktibilne funkcije

### Vremenski konstruktibilne funkcije

Ponekad želimo da Turingov stroj zna koliko je vremena potrošio, na primjer da bismo ga prisilili da se zaustavi nakon $T(n)$ koraka izračunavanja. No ako samo računanje $T(n)$ traje dulje od $T(n)$, to nije moguće. Zato su definirane vremenski konstruktibilne funkcije, kako bi se takve poteškoće izbjegle.

Ako postoji Turingov stroj $M$ takav da se za ulaz $1^n$ ($n$ jedinica) $M$ zaustavlja u vremenu $O(f(n))$ i ispisuje binarni zapis od $f(n)$ (pazite, izlaz Turingova stroja ovdje nije prihvaćanje/neprihvaćanje, nego niz; izlaz se može ispisati na traku), tada je $f(n)$ **vremenski konstruktibilna funkcija**.

Budući da čitanje ulaza traje $O(n)$ vremena, nekonstantne funkcije reda $o(n)$ nisu vremenski konstruktibilne.

### Prostorno konstruktibilne funkcije

Slično se mogu definirati prostorno konstruktibilne funkcije.

Ako postoji Turingov stroj $M$ takav da se za ulaz $1^n$ ($n$ jedinica) $M$ zaustavlja u prostoru $O(f(n))$ i ispisuje binarni zapis od $f(n)$, tada je $f(n)$ **prostorno konstruktibilna funkcija**.

## Odnosi među klasama složenosti

### Teoremi o vremenskoj hijerarhiji

#### Teorem o determinističkoj vremenskoj hijerarhiji

Ako je $f(n)$ vremenski konstruktibilna funkcija, tada:

$$
\mathsf {DTIME}\left(o\left({\frac {f(n)}{\log f(n)}}\right)\right)\subsetneq \mathsf {DTIME}(f(n))
$$

Iz teorema o determinističkoj vremenskoj hijerarhiji slijedi $\mathsf{P}\subsetneq\mathsf{EXPTIME}$.

??? note "Dokaz teorema o determinističkoj vremenskoj hijerarhiji"
    Definirajmo jezik $L=\{(x, y)|\mathcal{U}((x, y), x)\text{ se u vremenu }f(|x|+|y|)\text{ zaustavlja i odbija}\}$. Budući da je $f(n)$ vremenski konstruktibilna funkcija, $L$ se može odlučiti računanjem prema definiciji, u vremenu $O(f(|x|+|y|))$, pa je $L\in\mathsf{DTIME}(f(n))$.
    
    Pretpostavimo sada da je $L\in\mathsf{DTIME}(o\left({\dfrac {f(n)}{\log f(n)}}\right))$ i neka je $M_z$ Turingov stroj koji odlučuje $L$ u vremenu $o\left({\dfrac {f(n)}{\log f(n)}}\right)$.
    
    Neka je vrijeme izvođenja univerzalnog Turingova stroja $\mathcal{U}(x, z)$ s obzirom na $x$ jednako $g(|x|)$. Iz gornjeg opisa univerzalnog Turingova stroja dobivamo $g(n)=o(f(n))$, pa je za dovoljno velik $y$ $g(|z|+|y|)<f(|z|+|y|)$.
    
    Neka je $y'$ dovoljno velik $y$. Tada se $\mathcal{U}((z, y'), z)$ sigurno zaustavlja u vremenu $f(|z|+|y'|)$, pa je $M_z(z, y')\ne M_z(z, y')$, što je proturječje; dakle, pretpostavka ne vrijedi i teorem o determinističkoj vremenskoj hijerarhiji je dokazan.

#### Teorem o nedeterminističkoj vremenskoj hijerarhiji

Ako je $g(n)$ vremenski konstruktibilna funkcija i $f(n+1)=o(g(n))$, tada je $\mathsf{NTIME}(f(n))\subsetneq\mathsf{NTIME}(g(n))$.

Iz teorema o nedeterminističkoj vremenskoj hijerarhiji slijedi $\mathsf{NP}\subsetneq\mathsf{NEXPTIME}$.

### Teorem o prostornoj hijerarhiji

Ako je $f(n)$ prostorno konstruktibilna funkcija i $f(n)=\Omega(\log n)$, tada je $\mathsf{SPACE}(o(f(n)))\subsetneq\mathsf{SPACE}(f(n))$.

Pritom $\mathsf{SPACE}$ može označavati $\mathsf{DSPACE}$ ili $\mathsf{NSPACE}$.

Iz teorema o prostornoj hijerarhiji slijedi $\mathsf{PSPACE}\subsetneq\mathsf{EXPSPACE}$.

### Savitchev teorem

Deterministički Turingov stroj može simulirati nedeterministički Turingov stroj u prostoru koji je kvadrat prostora što ga troši nedeterministički stroj (iako utrošeno vrijeme može biti mnogo veće), tj.:

Ako je $f(n)=\Omega(\log n)$, tada:

$$
\mathsf{NSPACE}\left(f\left(n\right)\right)\subseteq \mathsf {DSPACE}\left(\left(f\left(n\right)\right)^2\right)
$$

Posljedica: $\mathsf{PSPACE}=\mathsf{NPSPACE}$, $\mathsf{EXPSPACE}=\mathsf{NEXPSPACE}$.

### P?=NP

Jesu li klase složenosti $\mathsf{P}$ i $\mathsf{NP}$ jednake poznat je neriješen problem teorije računske složenosti.

Ako je $\mathsf{P}=\mathsf{NP}$, slijedi $\mathsf{NP}=\mathsf{co-NP}$, ali ne i obratno (zasad ne postoji način da se iz $\mathsf{NP}=\mathsf{co-NP}$ dokaže $\mathsf{P}=\mathsf{NP}$).

???+ note "Zašto NP?=co-NP nije očito?"
    Budući da problem klase $\mathsf{NP}$ i njemu pripadni problem klase $\mathsf{co-NP}$ imaju suprotne odgovore, lako se dolazi na ovu ideju: za problem klase $\mathsf{co-NP}$ dovoljno je obrnuti izlaz nedeterminističkog Turingova stroja koji rješava njegov komplement i time je taj problem klase $\mathsf{co-NP}$ riješen, pa je $\mathsf{NP}=\mathsf{co-NP}$.
    
    Zapravo, opisana metoda doista rješava taj problem klase $\mathsf{co-NP}$, ali nismo pronašli nedeterministički Turingov stroj koji ga rješava: ako Turingov stroj obrće izlaz nedeterminističkog Turingova stroja, taj Turingov stroj nije nedeterministički Turingov stroj. Naime, nedeterministički Turingov stroj prihvaća ako prihvaća u nekoj grani, a odbija ako odbija u svim granama; obrnemo li njegov izlaz, prihvaća u svim granama, a odbija u jednoj grani, što više ne odgovara definiciji nedeterminističkog Turingova stroja. Stoga to što se tim Turingovim strojem može riješiti problem klase $\mathsf{co-NP}$ ne čini taj problem klase $\mathsf{co-NP}$ problemom klase $\mathsf{NP}$.

Ako je $\mathsf{P}=\mathsf{NP}$, slijedi i $\mathsf{EXPTIME}=\mathsf{NEXPTIME}$.

Ako je $\mathsf{P}\ne\mathsf{NP}$, slijedi da klasa NP-intermediate nije prazna.

## Literatura

1.  [计算复杂性（1）自动机与正则语言 (Računska složenost (1): automati i regularni jezici)](https://lingerois.com/p/%E8%AE%A1%E7%AE%97%E5%A4%8D%E6%9D%82%E6%80%A71-%E8%87%AA%E5%8A%A8%E6%9C%BA%E4%B8%8E%E6%AD%A3%E5%88%99%E8%AF%AD%E8%A8%80/);

2.  [计算复杂性（2）图灵机与可计算性 (Računska složenost (2): Turingovi strojevi i izračunljivost)](https://lingerois.com/p/%E8%AE%A1%E7%AE%97%E5%A4%8D%E6%9D%82%E6%80%A72-%E5%9B%BE%E7%81%B5%E6%9C%BA%E4%B8%8E%E5%8F%AF%E8%AE%A1%E7%AE%97%E6%80%A7/);

3.  odgovarajući članci na [Wikipediji](https://en.wikipedia.org/) i literatura navedena u njima.
