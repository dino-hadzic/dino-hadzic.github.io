---
title: Konačni automat
---

Preduvjeti: [Jezici i problemi odlučivanja](./cc-basic.md#problemi)

**Konačni automat** (Finite State Machine, FSM; u nastavku kraće i samo automat) najjednostavnija je vrsta računskog modela, što se očituje u tome da su mu i izražajna moć i resursi iznimno ograničeni. Automati se široko primjenjuju u natjecateljskom programiranju i računarstvu, a njihova se ideja pojavljuje u mnogim algoritmima nad nizovima znakova, pa se preporučuje da prije učenja nekih algoritama nad nizovima znakova ([KMP](../string/kmp.md), [AC automat](../string/ac-automaton.md), [SAM](../string/sam.md)) najprije savladate automate.

## Uvod u automate

Najprije shvatimo čemu automati služe: automat je matematički model kojim se provjerava zadovoljava li neki niz signala određeni uzorak ili pravilo.

Neke pojmove iz te rečenice vrijedi pobliže objasniti. „Niz signala” označava niz signala poredanih po redu, npr. znakove niza znakova od prvoga do posljednjega, elemente polja od $1$ do $n$, znamenke broja od najviše do najniže itd. „Provjeriti zadovoljava li neko pravilo” može se shvatiti ovako: zanima nas pripada li taj niz nekom određenom skupu. Taj je skup definiran pravilima koja smo unaprijed zadali, npr. „svi binarni nizovi parne duljine” ili „svi palindromi”.

Ponekad trebamo odgovoriti na ovakva pitanja: ima li zadani niz neko svojstvo? Na primjer, je li binarni broj neparan, je li niz znakova palindrom, je li podniz nekog drugog niza znakova i slično. Automat je upravo matematički alat za rješavanje takvih problema.

Automat radi vrlo slično dijagramu toka. Zamislite da u aplikaciji za dostavu hrane želite naručiti mliječni čaj (milk tea); svi vaši izbori tvore jedan niz. Sljedeći dijagram toka jedan je primjer:

![order fsm](./images/fsm1.svg)

Ako je, na primjer, vaš niz izbora „otvori sučelje za narudžbu -> odaberi mliječni čaj -> imaš novca za mliječni čaj”, onda su stanja kroz koja redom prolazite možda „aplikacija za dostavu -> sučelje za narudžbu -> plaćanje mliječnog čaja -> mliječni čaj kupljen”. Tako je naš „automat za mliječni čaj” na temelju naših izbora odlučio jesmo li kupili mliječni čaj. Uočavamo još i da do nekog stanja može voditi više od jednog puta. Isto tako, ako niste kupili mliječni čaj, možda ste izravno izašli iz sučelja za narudžbu ili niste imali novca pa ga niste kupili.

Tim smo automatom nizove signala podijelili u dvije skupine: nizove signala u kojima je mliječni čaj kupljen i nizove u kojima nije. Ovisno o tome u kojem se stanju nalazimo na kraju, riješili smo jedan problem odlučivanja.

Iako smo rad automata upravo usporedili s dijagramom toka, dijagram toka sam je po sebi tek zoran alat za vizualizaciju i ne čini matematičku definiciju automata. Da bismo strukturu automata opisali preciznije, elemente dijagrama toka moramo apstrahirati. Nakon apstrakcije vidimo da se struktura dijagrama toka zapravo može pojednostaviti u usmjereni graf u kojem svaki vrh predstavlja jedno stanje, a svaki usmjereni brid prijelaz između stanja.

Stoga se temeljna struktura automata formalno može promatrati kao usmjereni graf koji nazivamo **dijagramom stanja**.

Automat radi slično dijagramu toka, s tim razlikama: svaki vrh automata vrh je odlučivanja; vrh automata samo je stanje, a ne zadatak; brid automata može prihvatiti više različitih znakova (nije ograničen na `T` ili `F`).

Na primjer, automat koji obavlja zadatak „provjeri je li binarni broj paran” izgleda ovako:

![example fsm](./images/fsm2.svg)

Krenuvši od početnog vrha, prihvaćamo binarni zapis broja od najviše znamenke prema najnižoj i gledamo gdje smo na kraju stali. Ako smo stali u vrhu s crvenim krugom, broj je paran; inače nije.

Ovdje valja naglasiti: u nastavku ćemo često spominjati pojmove poput „znak” i „abeceda (skup znakova)”, ali to ne znači da se automati primjenjuju samo na nizove znakova; znak ne mora biti slovo poput $\tt abc\cdots z$, može biti i jedan izbor.

Ako treba odlučiti o odnosu konačnog niza signala i nekog drugog niza signala (npr. je li taj konačni niz signala podniz drugog niza signala), uobičajeno je za taj konačni niz signala izgraditi automat. O tome će biti riječi pri učenju KMP-a.

Treba imati na umu da je automat samo **matematički model**, a **ne algoritam** i **ne struktura podataka**. Isti se automat može implementirati na mnogo načina, s različitim vremenskim i prostornim složenostima.

Dalje možete nastaviti proučavati automate na ovoj stranici ili prijeći na konkretne primjere poput [KMP-a](../string/kmp.md), [AC automata](../string/ac-automaton.md) ili [SAM-a](../string/sam.md).

FSM-ovi se dijele u dvije vrste: determinističke konačne automate i nedeterminističke konačne automate.

## Deterministički konačni automat

**Deterministički konačni automat** (Deterministic Finite Automaton, DFA) odlikuje se time što mu je postupak odlučivanja determinističan. Na primjeru „automata za mliječni čaj”: čim otvorite sučelje za narudžbu, ulazite u sučelje za narudžbu; ne mogu se dogoditi nepredviđene situacije poput pada mreže zbog kojeg se sučelje ne otvara ili praznog mobitela s crnim zaslonom.

???+ abstract "DFA"
    DFA je uređena petorka $(Q,\Sigma,\delta,q_0,F)$ koja sadrži:
    
    1.  **Konačan skup stanja** $Q$. Gledamo li DFA kao usmjereni graf, stanja DFA odgovaraju vrhovima grafa.
    2.  **Abecedu** $\Sigma$. Automat na ulazu može primati samo te znakove.
    3.  **Funkciju prijelaza** $\delta:Q\times \Sigma \to Q$, funkciju koja prima dva argumenta i vraća jednu vrijednost; prvi argument i povratna vrijednost su stanja, a drugi je argument znak iz abecede. Gledamo li DFA kao usmjereni graf, funkcija prijelaza DFA odgovara bridovima između vrhova, pri čemu je na svakom bridu jedan znak.
    4.  **Početno stanje** $q_0\in Q$, jedno posebno stanje. U raznim se tekstovima početno stanje obično označava sa $s$, $\textit{start}$ ili $q_0$; u ovom tekstu koristimo $q_0$.
    5.  **Skup prihvaćajućih stanja** $F\subseteq Q$, skup posebnih stanja.

DFA se jednostavno može prikazati sljedećom strukturom:

???+ example "Referentna implementacija"
    ```cpp
    --8<-- "docs/misc/code/fsm/dfa.hpp:dfa"
    ```

Postupak određivanja niza stanja kroz koja ulazni niz $w$ prolazi u DFA i provjere je li prihvaćen naziva se **izračun** (computation).

???+ abstract "Tijek izračuna DFA"
    Neka je $M=(Q,\Sigma,\delta,q_0,F)$ DFA, a $w=w_1w_2\cdots w_n\in\Sigma^*$ niz. Ako postoji niz stanja $r_0,r_1,\cdots,r_n$ iz $Q$ takav da
    
    -   $r_0=q_0$,
    -   $\delta(r_i,w_{i+1})=r_{i+1}$ vrijedi za svaki $i=0,1,\cdots,n-1$,
    -   $r_n\in F$,
    
    kažemo da $M$ **prihvaća** (accepts) $w$. U suprotnom kažemo da $M$ **ne prihvaća** $w$.

Kad DFA čita niz znakova, od početnog stanja prelazi znak po znak prema funkciji prijelaza. Ako se nakon čitanja svih znakova niza nalazi u prihvaćajućem stanju, kažemo da DFA **prihvaća** taj niz; u suprotnom kažemo da ga DFA **ne prihvaća**.

???+ abstract "Formalni jezik"
    **Formalni jezik** (language) nad abecedom $\Sigma$, ili kraće **jezik**, skup je $L$ nizova nad $\Sigma$.

???+ abstract "Jezik koji automat prepoznaje"
    Za automat $M$ jezik $L(M)$ koji on prepoznaje definira se kao skup svih nizova koje prihvaća, $\{w\mid M\text{ accepts }w\}$.

Ne može se svaki jezik prepoznati DFA-om.

???+ abstract "Regularni jezik"
    Ako neki jezik može prepoznati neki DFA, nazivamo ga **regularnim jezikom** (regular language), a kaže se i pravilni jezik.

Već smo spomenuli da se automat može prikazati dijagramom stanja. Evo DFA koji prihvaća nizove $\tt a$, $\tt ab$ i $\tt aac$ i nijedan drugi:

![](./images/fsm3.svg)

(Na slici je izostavljeno stanje neuspjeha; svi neprikazani prijelazi vode u to stanje neuspjeha.)

## Nedeterministički konačni automat

**Nedeterministički konačni automat**[^nfa-and-nfaepsilon] (Nondeterministic Finite Automaton, NFA) prirodno je poopćenje DFA. U NFA za svako stanje i svaki znak može postojati nula, jedno ili više sljedećih stanja. Usto NFA o kojem govorimo u ovom odjeljku dopušta prihvaćanje praznog znaka, tj. iz nekog stanja može prijeći u neko od svojih sljedećih stanja ne potrošivši nijedan znak.

Uzmimo opet primjer „automata za mliječni čaj”. Nakon narudžbe, iako imate novca za mliječni čaj, zbog loše mreže možda ga ipak ne kupite – to je postojanje više sljedećih stanja; moguće je i da zbog prespore ruke, iako je ulazni niz (tj. niz radnji) jednak, mliječni čaj ne kupite jer je rasprodan – to je postojanje praznog znaka: praznim se znakom može, ali i ne mora prijeći. Gornje se ponašanje postiže malom izmjenom prethodnog automata:

![order nfa](./images/fsm4.svg)

Očito je svaki DFA ujedno i NFA, pa NFA može prepoznati barem sve regularne jezike. No može li NFA kao proširenje DFA prepoznati više jezika? Zapravo ne; ekvivalentnost DFA i NFA razmotrit ćemo poslije.

???+ abstract "NFA"
    Neka $\mathcal{P}(Q)$ označava partitivni skup skupa $Q$. Neka $\varepsilon\notin\Sigma$ označava prazni niz i neka je $\Sigma_\varepsilon = \Sigma\cup\{\varepsilon\}$. NFA je uređena petorka $(Q,\Sigma,\delta,q_0,F)$ koja sadrži:
    
    1.  **Konačan skup stanja** $Q$,
    2.  **Abecedu** $\Sigma$,
    3.  **Funkciju prijelaza** $\delta:Q\times \Sigma_{\varepsilon} \to \mathcal{P}(Q)$, funkciju koja prima dva argumenta i vraća **skup stanja**; prvi je argument stanje, drugi je argument znak iz abecede ili prazni niz $\varepsilon$, a povratna je vrijednost skup svih mogućih sljedećih stanja (može biti prazan),
    4.  **Početno stanje** $q_0\in Q$,
    5.  **Skup prihvaćajućih stanja** $F\subseteq Q$.

Izračun NFA odgovara istodobnom pokretanju više DFA. U svakom se koraku iscrpno isprobavaju sve mogućnosti, i na kraju, čim barem jedna grana stigne u prihvaćajuće stanje, NFA prihvaća cijeli niz.

???+ abstract "Tijek izračuna NFA"
    Neka je $N=(Q,\Sigma,\delta,q_0,F)$ NFA. Ako se niz $w$ može zapisati kao neki $y_1y_2\cdots y_m$ (gdje je $y_i\in\Sigma_\varepsilon$) i postoji niz stanja $r_0,r_1,\cdots,r_m$ iz $Q$ takav da
    
    -   $r_0=q_0$,
    -   $r_{i+1}\in\delta(r_i,y_{i+1})$ vrijedi za svaki $i=0,1,\cdots,m-1$,
    -   $r_m\in F$,
    
    kažemo da $N$ **prihvaća** $w$. U suprotnom kažemo da $N$ **ne prihvaća** $w$.

Budući da su prazni znakovi dopušteni, pri zapisu niza $w$ kao $y_1y_2\cdots y_m\in\Sigma^*_\varepsilon$ može se umetnuti proizvoljno mnogo praznih znakova. Na primjer, niz $\texttt{abc}$ može se zapisati kao $\texttt{a}\varepsilon\texttt{bc}\varepsilon\varepsilon\in\Sigma^*_\varepsilon$. Za razliku od DFA, kod kojeg svaki ulaz daje samo jedan ishod, kod NFA svaki ulaz može dati više ishoda koji čine skup ishoda.

## Ekvivalentnost DFA i NFA

Za dva automata kažemo da su ekvivalentni ako i samo ako prepoznaju isti jezik. DFA i NFA su ekvivalentni, tj. svaki je NFA ekvivalentan nekom DFA; stoga je i klasa jezika koje prepoznaju NFA upravo klasa svih regularnih jezika. Svaki se DFA izravno može promatrati kao NFA; obrnuto, NFA se u DFA može pretvoriti **konstrukcijom partitivnog skupa** (powerset construction).

???+ abstract "Konstrukcija partitivnog skupa"
    Neka je NFA $N = (Q, \Sigma, \delta, q_0, F)$. Definirajmo $E(q)$ kao skup stanja dostižnih iz stanja $q$ samo $\varepsilon$-prijelazima (uključujući i samo $q$), tj. $\varepsilon$-zatvorenje stanja $q$.
    
    Konstruiramo DFA $M = (Q', \Sigma, \delta', E(q_0), F')$, gdje je:
    
    -   **konačan skup stanja** $Q' = \mathcal{P}(Q)$,
    -   **funkcija prijelaza** $\delta' : Q' \times \Sigma \to Q'$ takva da je $\delta'(S, c) = \bigcup_{q \in S,~q' \in \delta(q, c)} E(q')$,
    -   **skup prihvaćajućih stanja** $F' = \{ S \subseteq Q \mid S \cap F \neq \varnothing \}$.
    
    Očito u svakom koraku izračuna stanje u kojem se nalazi $M$ odgovara skupu stanja u kojima se može nalaziti $N$.

Iako NFA i DFA imaju jednaku moć prepoznavanja jezika, NFA su i dalje korisni. Razlog je to što za neke regularne jezike NFA treba daleko manje stanja nego DFA. Na primjer, može se konstruirati NFA s $n$ stanja čiji odgovarajući minimalni DFA ima $\Theta(2^n)$ stanja. Tada je vremenski povoljnije izravno izvoditi izračun na NFA.

## Vremenska složenost izračuna DFA i NFA

Neka je duljina zadanog niza $n$, broj stanja automata $s$, a veličina abecede konstanta. Tada je očito vremenska složenost izračuna DFA $O(n)$: dovoljno je simulirati gore opisani postupak.

Naivni izračun NFA ima vremensku složenost $O(ns^2)$, jer treba razmotriti svako moguće sljedeće stanje te složenost spajanja stanja. Dakako, pomoću bitseta ili metode četiriju Rusa (Method of Four Russians) složenost izračuna može se poboljšati na $O\left(\dfrac{ns^2}{w}\right)$ odnosno $O\left(\dfrac{ns^2}{w\cdot \log n}\right)$.

## Regularni izrazi i regularni jezici

U ovom odjeljku razmatramo definiciju i svojstva regularnih izraza i regularnih jezika te proučavamo odnos regularnih izraza i FSM-ova.

### Regularni izrazi

**Regularni izraz** (regular expression) još je jedan uobičajen način opisivanja regularnih jezika. Iako taj naziv susrećemo u mnogim suvremenim programskim jezicima (npr. Pythonu), ti jezici zapravo implementiraju nadskup regularnih izraza.

???+ abstract "Regularni izraz"
    Za zadanu abecedu $\Sigma$ regularni izraz je niz simbola induktivno definiran sljedećim pravilima:
    
    1.  svaki znak $c \in \Sigma$ regularni je izraz;
    2.  simbol praznog niza $\varepsilon$ regularni je izraz;
    3.  simbol praznog jezika $\varnothing$ regularni je izraz;
    4.  ako su $R_1$ i $R_2$ regularni izrazi, onda su i $(R_1 + R_2)$, $(R_1 R_2)$ (zapisuje se i $(R_1 \cdot R_2)$) te $(R_1^\ast)$ regularni izrazi.

Svrha je regularnog izraza tim simbolima opisati neki jezik. Svakom regularnom izrazu odgovara jedan formalni jezik.

???+ abstract "Jezik koji regularni izraz predstavlja"
    Neka je $L(R)$ formalni jezik koji odgovara regularnom izrazu $R$. Tada vrijedi:
    
    1.  ako je $R = c$, gdje je $c \in \Sigma$, onda je $L(R) = \{c\}$;
    2.  ako je $R = \varepsilon$, onda je $L(R) = \{\varepsilon\}$;
    3.  ako je $R = \varnothing$, onda je $L(R) = \varnothing$;
    4.  ako je $R = (R_1 + R_2)$, onda je $L(R) = L(R_1) \cup L(R_2)$;
    5.  ako je $R = (R_1 R_2) = (R_1\cdot R_2)$, onda je $L(R) = \{ uv \mid u \in L(R_1),~ v \in L(R_2) \}$, gdje $uv$ označava nadovezivanje dvaju nizova jednog na drugi;
    6.  ako je $R = (R_1^\ast)$, onda je $L(R) = \{u_1 u_2 \cdots u_n \mid u_i \in L(R_1),\ n \in \mathbf{N}_+\}\cup\{\varepsilon\}$, što se naziva i **Kleeneova zvjezdica** (Kleene star) ili **Kleeneovo zatvorenje** (Kleene closure), kraće zatvorenje.

Naravno, kad se dogovori prioritet operacija, zagrade se mogu izostaviti kad god to ne izaziva zabunu.

???+ example "Primjer"
    Neka je $L(R_1) = \{0,\ 01\}$ i $L(R_2) = \{\varepsilon,\ 1,\ 11,\ 111,\ \dots\}$. Tada je:
    
    -   $L(R_1R_2) = \{0,\ 01,\ 011,\ 0111,\ \dots\}$,
    -   $L(R_2^\ast) = L(R_2)$,
    -   $L(R_1 + R_2) = \{0,\ 01,\ \varepsilon,\ 1,\ 11,\ 111,\ \dots\}$.

Svaki se regularni izraz [Thompsonovom konstrukcijom](https://en.wikipedia.org/wiki/Thompson%27s_construction) (Thompson's construction) može pretvoriti u NFA, a svaki se DFA metodom eliminacije stanja[^state-elimination-method] (State Elimination Method) može pretvoriti u regularni izraz. Stoga su regularni izrazi i FSM-ovi ekvivalentni.

### Regularni jezici

U ovom pododjeljku ne razmatramo konkretne regularne izraze, nego regularne izraze s varijablama kao parametrima (varijabla može biti bilo koji regularni jezik). Primjena algebarskih zakona regularnih izraza pomaže pri njihovu pojednostavljivanju.

???+ note "Algebarska svojstva regularnih jezika"
    1.  Komutativnost unije: $L + M = M + L$
    2.  Asocijativnost unije: $(L + M) + N = L + (M + N)$
    3.  Asocijativnost nadovezivanja: $(LM)N = L(MN)$
    4.  $\varnothing$ je neutralni element unije: $\varnothing + L = L + \varnothing = L$
    5.  $\varepsilon$ je neutralni element nadovezivanja: $\varepsilon L = L \varepsilon = L$
    6.  $\varnothing$ je nul-element nadovezivanja: $\varnothing L = L \varnothing = \varnothing$
    7.  Distributivnost: $L(M + N) = LM + LN$, $(M + N)L = ML + NL$
    8.  Idempotentnost unije: $L + L = L$
    9.  Zakoni o zatvorenju: $(L^\ast)^\ast = L^\ast$, $\varnothing^\ast = \varepsilon$, $\varepsilon^\ast = \varepsilon$

Važno je svojstvo regularnih jezika i njihova **zatvorenost**. Ta nam svojstva omogućuju da, polazeći od nekoliko jednostavnih automata, određenim operacijama konstruiramo konačne automate (FSM) koji prepoznaju druge jezike. Ukratko, zatvorenost je alat za konstrukciju složenih FSM-ova.

O zatvorenosti regularnih jezika vrijedi:

???+ note "Zatvorenost regularnih jezika"
    Neka su $L,M$ dva regularna jezika nad abecedom $\Sigma$ i neka je $h:\Sigma\to\Sigma^*$ preslikavanje. Homomorfizam niza $s=s_1s_2\cdots s_n$ definiramo kao $h(s)=h(s_1)h(s_2)\cdots h(s_n)$. Tada:
    
    1.  unija $L + M$ dvaju regularnih jezika je regularna,
    2.  nadovezivanje $LM$ dvaju regularnih jezika je regularno,
    3.  zatvorenje $L^*$ regularnog jezika je regularno,
    4.  komplement $\Sigma^*\setminus L$ regularnog jezika je regularan,
    5.  presjek $L\cap M$ dvaju regularnih jezika je regularan,
    6.  razlika $L\setminus M$ dvaju regularnih jezika je regularna,
    7.  obrat $L^R=\{s_n\cdots s_2s_1 \mid s=s_1s_2\cdots s_n\in L\}$ regularnog jezika je regularan,
    8.  homomorfna slika $h(L)=\{h(s)\mid s\in L\}$ regularnog jezika je regularna,
    9.  inverzna homomorfna slika $h^{-1}(L) = \{ s \in \Sigma^\ast \mid h(s) \in L \}$ regularnog jezika je regularna.

Jednostavna je posljedica da su svi konačni jezici regularni. Zapravo, [trie](../string/trie.md) upravo je automat koji ih prepoznaje.

## Myhill–Nerodeov teorem

Myhill–Nerodeov teorem daje kriterij za odlučivanje je li jezik regularan. Teorem pojmom klasa ekvivalencije opisuje strukturna obilježja regularnih jezika.

???+ abstract "Nerodeova relacija ekvivalencije"
    Za jezik $L$ i proizvoljne nizove $x,y\in \Sigma^\ast$, ako za svaki $z\in\Sigma^*$ vrijedi $xz\in L\iff yz\in L$, kažemo da su nizovi $x$ i $y$ ekvivalentni s obzirom na $L$ i pišemo $x\equiv_L y$.

Drugim riječima, ako za dva niza $x$ i $y$ vrijedi da nadovezivanjem istog proizvoljnog niza $z$ (uključujući prazni niz) na $x$ i na $y$ dobiveni nizovi uvijek ili oba pripadaju $L$ ili oba ne pripadaju $L$, kažemo da su $x$ i $y$ ekvivalentni s obzirom na $L$.

Prema toj definiciji skup svih konačnih nizova dijelimo u jednu ili više klasa ekvivalencije. Ako i samo ako je tih klasa ekvivalencije konačno mnogo, od njih se može konstruirati DFA koji prepoznaje taj jezik. Broj stanja tog DFA jednak je broju klasa ekvivalencije. Štoviše, taj je broj stanja najmanji među svim DFA koji prepoznaju taj jezik. To je Myhill–Nerodeov teorem.

???+ note "Myhill–Nerodeov teorem"
    Jezik $L$ je regularan ako i samo ako je broj klasa ekvivalencije na koje relacija ekvivalencije $\equiv_L$ dijeli $\Sigma^\ast$ konačan.
    
    Za svaki DFA koji prepoznaje jezik $L$, bilo koja dva niza $x$ i $y$ koja ga dovode u isto stanje nužno pripadaju istoj klasi ekvivalencije.
    
    Nadalje, broj klasa ekvivalencije jednak je broju stanja minimalnog DFA koji prepoznaje $L$. Svaka klasa ekvivalencije odgovara točno jednom stanju minimalnog DFA. Taj je minimalni DFA jedinstven do na izomorfizam.

Teorem daje način da se DFA konstruira pomoću relacije ekvivalencije:

-   Skup stanja čine sve klase ekvivalencije dobivene podjelom prema relaciji ekvivalencije. U svakoj klasi ekvivalencije proizvoljno odaberemo predstavnika (npr. neki niz najmanje duljine).
-   Za konstrukciju funkcije prijelaza dovoljno je na odabranog predstavnika nadovezati znak prijelaza i pronaći stanje koje odgovara klasi ekvivalencije dobivenog niza; to je sljedeće stanje tog prijelaza. Budući da su svi nizovi unutar iste klase ekvivalencije ekvivalentni, izbor predstavnika ne utječe na ishod prijelaza.
-   Početno stanje je klasa ekvivalencije koja odgovara praznom nizu $\varepsilon$.
-   Skup prihvaćajućih stanja skup je onih klasa ekvivalencije čiji predstavnik pripada zadanom jeziku.

Klasičan je primjer [sufiksni automat](../string/sam.md), koji je upravo minimalni DFA konstruiran pomoću Myhill–Nerodeova teorema.

Myhill–Nerodeov teorem obično se primjenjuje za konstrukciju DFA koji odgovaraju nekim beskonačnim regularnim jezicima. Vrlo su često uvjeti zadatka razmjerno jednostavni, pa je za konstrukciju automata koji prepoznaje cijeli jezik dovoljno razmotriti skup nizova ne prevelike duljine.

### Primjer zadatka

U ovom odjeljku na jednom primjeru pokazujemo kako se Myhill–Nerodeov teorem primjenjuje u praksi.

???+ example "[P12294 \[THUPC 2025 决赛\] 一个 01 串，n 次三目运算符，最后值为 1（加强版）](https://www.luogu.com.cn/problem/P12294) (P12294, THUPC 2025 finale: Jedan 01-niz, n ternarnih operatora, konačna vrijednost 1, pojačana verzija)"
    Tablica ternarne operacije nad $a,b,c$ je $s_0s_1\cdots s_7$ ($s$ se sastoji samo od $0$ i $1$) i znači: ako je bit $s$ na mjestu $a+2b+4c$ jednak $1$, rezultat je $1$, inače je $0$.
    
    Zadana je tablica operacije $s$ i $q$ nizova od $0$ i $1$ duljine $2n+1$; za svaki niz treba zasebno odgovoriti:
    
    može li se $n$ puta izvesti operacija koja tri uzastopne znamenke zamjenjuje pripadnom vrijednošću iz tablice tako da je rezultat $1$; ako može, ispisati postupak, inače utvrditi da rješenja nema.
    
    $1\le 2n+1\le 10^5,~\sum(2n+1)\le 3\times 10^5$.

??? note "Rješenje"
    Skup $01$-nizova iz kojih se može dobiti $1$ regularan je jezik (tj. postoji DFA koji odlučuje može li se iz $01$-niza dobiti $1$)[^prove-regular-language]. Stoga primjenjujemo Myhill–Nerodeov teorem. Budući da su uvjeti razmjerno jednostavni, eksperimentom se pokazuje da je dovoljno na klase ekvivalencije podijeliti $01$-nizove duljine $\le 9$; pri provjeri jesu li dva niza ekvivalentna dovoljno je isprobati nastavke duljine $\le 6$. Ako za dva niza vrijedi da se nadovezivanjem proizvoljnog nastavka duljine $\le 6$ iz oba istodobno može dobiti željeni niz ili ni iz jednog ne može, ta su dva niza ekvivalentna.
    
    Svaki prijelaz odgovara dodavanju novog znaka $0$ ili $1$ na kraj trenutačnog niza, nakon čega se novi niz zamjenjuje najkraćim nizom iz njegove klase ekvivalencije. Prema tim prijelazima gradimo automat. Taj automat u složenosti $O(n)$ odlučuje postoji li za niz duljine $n$ redoslijed operacija koji daje rezultat $1$. Pritom je broj stanja automata vrlo malen.
    
    Radi praktičnosti gradimo $6$ automata, koji redom odlučuju može li se nekim redoslijedom operacija dobiti rezultat $0,1,00,01,10,11$. Za sve moguće tablice operacije najveći broj stanja automata iznosi $47$.
    
    Pomoću automata i odgovarajuće pretprocesiranja statički upit nad intervalom (postoji li u intervalu redoslijed operacija koji daje rezultat $1$) može se ostvariti sparse tableom ili cat treeom: prvi odgovara na upit u $O(\log n)$, a drugi u $O(1)$.
    
    Konstrukciju rješavamo metodom podijeli pa vladaj. Neka $f(l,r,t)$ označava postupak kojim se interval $[l,r]$ spaja u $t\in\{0,1,00,01,10,11\}$. Koristimo heurističko cijepanje: održavamo dva pokazivača $i,j$, jedan ide slijeva nadesno, a drugi zdesna nalijevo, i tako isprobavamo točku prekida $\textit{mid}$ jednaku $i$ ili $j$. Za $t\in\{0,1\}$ isprobavamo kako se $t$ dijeli na lijevi i desni dio, pri čemu je u jednom dijelu $t$ duljine $2$, a u drugom duljine $1$. (Na primjer, za tablicu medijana $s=00010111$, $1$ se može podijeliti na $01$ i $1$.) Za $t\in\{00,01,10,11\}$ $t$ se izravno dijeli na lijevi i desni dio.
    
    Ako su tako dobiveni lijevi i desni dio redom $t_1$ i $t_2$, dalje provjeravamo može li $[l,\textit{mid}]$ dati $t_1$ i može li $[\textit{mid}+1,r]$ dati $t_2$; ako može, izravno nastavljamo rekurzivno. Ako se za provjeru koristi cat tree u $O(1)$, složenost konstrukcije heurističkim cijepanjem iznosi $O(n\log n)$; koristi li se za provjeru sparse table, složenost konstrukcije je $O(n\log^2n)$.
    
    S cat treeom ukupna je složenost $O(n|Q|\log n+n\log n)$, gdje je $|Q|\le 47$. Referentni kôd radi jednostavnosti koristi sparse table, a konstantu smanjuje blokovskom podjelom na najnižoj razini; pripadna ukupna složenost je $O(n|Q|\log n+n\log^2 n)$.

??? note "Referentni kod"
    ```cpp
    --8<-- "docs/misc/code/fsm/fsm_1.cpp:main"
    ```

### Zadaci za vježbu

-   [Median Replace Hard](https://qoj.ac/problem/12010)
-   [JOISC 2024 卡牌收集 (Card Collection)](https://www.luogu.com.cn/problem/P10436) (izgradnjom automata pomoću Myhill–Nerodeova teorema u ovom se zadatku može odgovarati na više upita nad intervalima)

## Minimizacija DFA

Ranije smo spomenuli da su dva DFA ekvivalentna ako i samo ako prepoznaju isti regularni jezik. Prema prepoznatom jeziku svi se DFA dijele u beskonačno mnogo klasa ekvivalencije. Pri algoritmima poput DP-a unutar DP-a izgrađeni DFA može imati prevelik $|Q|$, zbog čega je složenost prijelaza vanjskog DP-a prevelika. Zato često treba pronaći minimalni DFA u klasi ekvivalencije kojoj dani DFA pripada, kako bi se smanjila složenost prijelaza vanjskog DP-a.

Myhill–Nerodeov teorem iz prethodnog odjeljka daje jedan način konstrukcije. No za neke složenije probleme izravna konstrukcija Myhill–Nerodeovim teoremom zahtijeva obilazak skupa prilično dugih nizova i troši mnogo vremena. Stoga trebamo metodu kojom se, polazeći od već konstruiranog DFA (što je obično lako), izravno konstruira minimalni DFA. To se naziva problemom **minimizacije DFA** (DFA minimization).

Uobičajeni algoritam za minimizaciju DFA jest **Hopcroftov algoritam**. Myhill–Nerodeov teorem kaže da su za svaki DFA koji prepoznaje neki jezik nizovi koji ga dovode u isto stanje nužno Nerode-ekvivalentni. Svi Nerode-ekvivalentni nizovi odgovaraju istom stanju minimalnog DFA, pa je stanje minimalnog DFA nužno skup nekoliko stanja postojećeg DFA (ovdje pretpostavljamo da su sva stanja postojećeg DFA dostižna iz $q_0$; inače najprije treba ukloniti nedostižna stanja). Možemo krenuti od skupa stanja postojećeg DFA i podijeliti ga u nekoliko klasa ekvivalencije ne razmatrajući konkretne nizove. Hopcroftov algoritam kreće od najgrublje podjele $\{F,Q\setminus F\}$ i nizom svjedoka $A$ profinjuje tu podjelu dok se više ne može profiniti. To je temeljna ideja Hopcroftova algoritma.

**Svjedok** $A$ je skup stanja takav da on i njegov komplement $Q\setminus A$ sigurno odgovaraju različitim Nerodeovim klasama ekvivalencije. Drugim riječima, za svaki $u\in A$ i $v\in Q\setminus A$ postoji niz $s\in\Sigma^*$ takav da se nakon čitanja niza $s$ iz $u$ odnosno iz $v$ točno jedan od njih nalazi u prihvaćajućem stanju. Stoga, ako dva stanja $u,v\in Q$ pod nekim znakom $c$ prelaze točno jedno u svjedoka $A$, a drugo izvan svjedoka $A$, tj. od $\delta(u,c)\in A$ i $\delta(v,c)\in A$ vrijedi točno jedno, onda $u,v$ također nisu ekvivalentna – nakon čitanja niza $cs$ iz $u$ odnosno iz $v$ točno je jedan od njih u prihvaćajućem stanju. Stoga se podjela može profiniti prema tome vrijedi li $\delta(u,c)\in A$. Konkretno, neka je

$$
S_x = \{u\mid u\in P_x,~\delta(u,c)\in A\}.
$$

Ako ni $S_x$ ni $P_x\setminus S_x$ nisu prazni, skup stanja $P_x$ u trenutačnoj podjeli može se profiniti u $S_x$ i $P_x\setminus S_x$.

Na početku skup prihvaćajućih stanja $F$ kao svjedoka stavljamo u skup svjedoka $W$, tj. $W\gets\{F\}$, a trenutačnu podjelu održavamo kao $P\gets\{F,~Q\setminus F\}$. Početni je svjedok očito valjan: stanja iz $F$ i $Q\setminus F$ nikako ne mogu biti ekvivalentna. Svaki put iz skupa svjedoka $W$ proizvoljno uzimamo jedan skup $A$ kojim profinjujemo trenutačnu podjelu. Prolazimo kroz sve znakove $c\in\Sigma$. Za svaki skup stanja $P_x$ u trenutačnoj podjeli $P$ izračunamo gore opisani $S_x$. Ako je $S_x\neq\varnothing$ i $|S_x|\neq|P_x|$, znači da se $P_x$ može dalje podijeliti u dva skupa $S_x$ i $P_x\setminus S_x$, kojima izravno zamjenjujemo $P_x$ u $P$.

Svaki put kad dobijemo finiju podjelu, dobili smo i nove svjedoke. U načelu bi se i novodobiveni $S_x$ i $P_x\setminus S_x$ mogli staviti u skup svjedoka $W$ i pričekati daljnju provjeru. No to nije nužno. Lako je uvidjeti da je za tri svjedoka $P_x,S_x,P_x\setminus S_x$ dovoljno provjeriti bilo koja dva da bi se zajamčila točnost rezultata: ishodi su samo $\delta(u,c)\in S_x$, $\delta(u,c)\in P_x\setminus S_x$ i $\delta(u,c)\notin P_x$, a za podjelu skupa na tri dijela dovoljne su dvije provjere. Stoga, kad $P_x$ dijelimo na $S_x$ i $P_x\setminus S_x$: ako se $P_x$ još nalazi u skupu svjedoka $W$, to znači da svjedok $P_x$ još nije provjeren, pa $P_x$ u skupu svjedoka $W$ zamjenjujemo dvama skupovima $S_x$ i $P_x\setminus S_x$; inače je trenutačna podjela sigurno jednakovrijedna[^smaller-evidence] rezultatu provjere svjedoka $P_x$, pa je dovoljno u skup svjedoka $W$ staviti manji od $S_x$ i $P_x\setminus S_x$. Slično heurističkom cijepanju, time se postiže dobra složenost.

Zapisan kao pseudokod, gornji postupak glasi:

$$
\begin{array}{l}
\textbf{Algorithm } \text{Hopcroft's Algorithm}(Q, \Sigma, \delta, q_0, F): \\
\textbf{Input. } \text{DFA } M=(Q, \Sigma, \delta, q_0, F). \\
\textbf{Output. } \text{A partition of } Q \text{ into equivalence classes of the minimal DFA.} \\
\textbf{Method. } \\
\begin{array}{ll}
1 & P \gets \{F,\; Q \setminus F\} \\
2 & W \gets \{F\} \\
3 & \textbf{while } W \ne \varnothing \\
4 & \quad \text{choose and remove any } A \in W \\
5 & \quad \textbf{for each } c \in \Sigma \\
6 & \quad \quad S \gets \{ q \in Q \mid \delta(q,c) \in A \} \\
7 & \quad \quad \textbf{for each } Y \in P \text{ such that } S \cap Y \ne \varnothing \text{ and } Y \setminus S \ne \varnothing \\
8 & \quad \quad \quad Y_1 \gets S \cap Y,~Y_2 \gets Y \setminus S \\
9 & \quad \quad \quad P \gets (P \setminus \{Y\}) \cup \{Y_1, Y_2\} \\
10 & \quad \quad \quad \textbf{if } Y \in W \\
11 & \quad \quad \quad \quad W \gets (W \setminus \{Y\}) \cup \{Y_1, Y_2\} \\
12 & \quad \quad \quad \textbf{else} \\
13 & \quad \quad \quad \quad \text{add the smaller of } Y_1 \text{ and } Y_2 \text{ to } W \\
14 & \textbf{return } P
\end{array}
\end{array}
$$

Pri implementaciji algoritma usko je grlo složenosti računanje skupa $S$. Izravan prolazak kroz sva stanja $q\in Q$ s provjerom vrijedi li $\delta(q,c)\in A$ nije prihvatljiv. Stoga prije pokretanja algoritma treba pretprocesirati obrnute prijelaze $\{q\in Q\mid \delta(q,c)=a\}$, pa se pomoću njih prolaskom kroz $a\in A$ dobiva skup $S$. Time se osigurava da se svaki prijelaz $\delta(q,c)=a$ obilazi samo kad $a$ pripada nekom svjedoku; a gore opisani način odabira svjedoka jamči da je u nizu svjedoka $A_1\supset A_2\supset\cdots\supset A_k$ koji sadrže $a$ i stvarno se koriste u algoritmu svaki prethodni barem dvostruko veći od sljedećeg, pa je $k\in O(\log |Q|)$. Drugim riječima, svaki se prijelaz obilazi najviše $O(\log |Q|)$ puta, a ukupan je broj prijelaza $|Q||\Sigma|$, pa je ukupna složenost $O(|Q||\Sigma|\log |Q|)$.

Referentna implementacija:[^detail]

??? example "Referentna implementacija"
    ```cpp
    --8<-- "docs/misc/code/fsm/dfa.hpp:hopcroft"
    ```

Ova referentna implementacija dopušta da stanja automata nose oznake s proizvoljnim cjelobrojnim vrijednostima, a ne samo binarnu oznaku „prihvaća” / „ne prihvaća”. Iz referentne implementacije vidi se da je jedina razlika u odnosu na osnovni Hopcroftov algoritam u konstrukciji početne podjele i skupa svjedoka. Takav prošireni automat naziva se i [Mooreov automat](https://en.wikipedia.org/wiki/Moore_machine) (Moore machine). Jednu njegovu primjenu pokazuje drugi primjer zadatka u ovom odjeljku.

### Primjeri zadataka

U ovom odjeljku na dva primjera pokazujemo kako se tehnika minimizacije DFA primjenjuje u praksi.

???+ example "Primjer zadatka"
    Zadan je niz $a$ duljine $n$ sastavljen od znakova $01?$; početno je varijabla $x = 0$, a znakove $a_i$ obilazimo redom i izvodimo sljedeće operacije:
    
    1.  ako je $a_i = 0$, stavljamo $x \gets x - \text{lowbit}(x)$;
    2.  ako je $a_i = 1$, stavljamo $x \gets x + \text{lowbit}(2^k - 1 - x)$;
    3.  ako je $a_i = ?$, slobodno biramo $0$ ili $1$ i izvodimo pripadnu od gornjih dviju operacija.
    
    Ako je na kraju $x \in [0, r]$, taj niz operacija zovemo dobrim.
    
    Za svaki $i = 1 \ldots n$ treba odrediti koliko „dobrih” potpunih nizova postoji uz prisilno $a_i = 0$. Posebno, za $a_i = 1$ odgovor je $0$.
    
    $1\le n\le 10^5,~1\le k\le 20,~0\le r<2^k$. Odgovor se ispisuje modulo $998244353$.

??? note "Rješenje"
    Razmotrimo naivni DP. Neka $f_{i,j}$ označava broj načina da se, krenuvši od $x=0$ i izvevši operacije na $[1,i]$, dobije trenutačna vrijednost $j$. Neka $g_{i,j}$ označava broj načina da se, krenuvši od $x=j$ i izvevši operacije na $[i,n]$, na kraju dobije $x \in [0, r]$. Odgovor uz prisilno $a_i=0$ tada je $\sum_j f_{i-1,j}g_{i+1,j - \text{lowbit}(j)}$. Složenost je $O(n2^k)$.
    
    Prijelaze po $j$ izravno pretvorimo u DFA, zatim provedemo minimizaciju DFA i onda napravimo DP.

??? note "Referentni kod"
    ```cpp
    --8<-- "docs/misc/code/fsm/fsm_2.cpp:main"
    ```

???+ example "[Minimal Subset Difference](https://codeforces.com/contest/956/problem/F)"
    Neka $f(n)$ označava najmanju apsolutnu vrijednost koja se može dobiti kad se između svih znamenaka dekadskog broja $n$ umetnu znakovi plus ili minus.
    
    Zadano je $T$ upita. U svakom su upitu zadani $l, r, k$; treba odrediti broj $m$ takvih da je $l \le m \le r$ i $f(m) \le k$.
    
    $1 \le T \le 5\times 10^4$, $1 \le l \le r \le 10^{18}$, $0 \le k \le 9$.

??? note "Rješenje"
    Najprije dajemo pohlepni način računanja $f(n)$. Broj promatramo od najviše znamenke prema najnižoj; na početku je dobiveni zbroj $0$. Kad dođemo do neke znamenke, ako je trenutačno dobiveni broj manji ili jednak $0$, dodajemo tu znamenku, a inače je oduzimamo. Apsolutna vrijednost rezultata ovako pohlepno izračunatog sigurno je manja ili jednaka $9$. Stoga je i apsolutna vrijednost pravog $f(n)$ sigurno manja ili jednaka $9$.
    
    Razmislimo dalje: koliko najviše može iznositi broj dobiven u međukoracima da bi se na kraju dobio konačni odgovor? Budući da je odgovor sigurno manji ili jednak $9$, a znamenaka ima najviše $19$ i svaki se put može dodati ili oduzeti najviše $9$, broj dobiven tijekom postupka sigurno je manji ili jednak $90$, inače se na kraju ne može „vratiti”. Ta se gornja granica zapravo može još sniziti[^upper-bound].
    
    Razmotrimo naivni DP unutar DP-a. Najprije, kako unutarnji DP odlučuje o odgovoru za neki broj: neka $g_{i,c}$ označava može li se samo iz prvih $i$ znamenaka tog broja dobiti $c$. Prema prethodnome, za $c$ je dovoljno zadržati brojeve manje ili jednake $90$. Ako je na trenutačnom mjestu znamenka $v$, imamo prijelaz:
    
    $$
    g_{i+1,c+v}\gets g_{i+1,c+v}\lor g_{i,c},~
    g_{i+1,|c-v|}\gets g_{i+1,|c-v|}\lor g_{i,c}.
    $$
    
    Vanjski DP je znamenkasti DP (digit DP). Upit rastavimo na razliku. Neka je stanje $f_{\textit{len},\textit{lim},\textit{sta}}$, čiji indeksi redom označavaju da smo obradili $\textit{len}$ znamenaka, postoji li ograničenje gornjom granicom te da se automat trenutačno nalazi u stanju $\textit{sta}$.
    
    Za razliku od običnog DFA, ovdje za svako stanje automata trebamo pamtiti pripadni odgovor. Jednim pretraživanjem grubom silom vidi se da unutarnji DP ima samo $19564$ stanja. Nakon toga izravno provodimo minimizaciju DFA, čime se broj stanja smanjuje na $715$.
    
    Tada unaprijed izračunamo sve odgovore znamenkastog DP-a za $\textit{lim}=0$, pa pri više testnih primjera treba obraditi samo slučaj $\textit{lim}=1$ i odgovor se dobiva vrlo brzo.
    
    Vremenska složenost je $O(|S||\Sigma|\log |S|+(|Q||\Sigma|+T)|\Sigma|\log_{10} V)$ ($|S|=19564$, $|Q|=715$).

??? note "Referentni kod"
    ```cpp
    --8<-- "docs/misc/code/fsm/fsm_3.cpp:main"
    ```

### Zadaci za vježbu

-   [Language Recognition](http://poj.org/problem?id=3576)
-   [Equanimous](https://qoj.ac/problem/7083)

## Česte primjene automata

U ovom odjeljku navodimo neke česte primjene automata u natjecateljskom programiranju[^is-dfa].

### Trie

[Trie](../string/trie.md) je prvi automat s kojim se većina natjecatelja susreće; prihvaća elemente zadanog skupa nizova i nijedan drugi. Funkcija prijelaza su bridovi trieja, a prihvaćajuća su stanja ona stanja u koja dolazimo pri umetanju pojedinog niza u trie.

### KMP automat

[KMP algoritam](../string/kmp.md) može se promatrati kao automat: KMP automat zasnovan na nizu $s$ prihvaća nizove kojima je $s$ sufiks i nijedan drugi, a prihvaćajuće mu je stanje $|s|$.

Funkcija prijelaza je sljedeća, pri čemu indeksi niza $s$ počinju od $1$, a $\pi(i)$ označava duljinu najduljeg zajedničkog pravog prefiksa i sufiksa prefiksa $s[1..i]$ (tj. $\pi[i-1]$ iz [prefiksne funkcije](../string/kmp.md)):

$$
\delta(i, c)=
\begin{cases}
i+1&i<|s|\land s[i+1]=c\\
0&s[1]\ne c\land i=0\\
\delta(\pi(i),c)&(i=|s|\lor s[i+1]\ne c)\land i>0
\end{cases}
$$

### AC automat

[AC automat](../string/ac-automaton.md) prihvaća nizove kojima je neki element zadanog skupa nizova sufiks i nijedan drugi. Drugim riječima, trie + KMP.

### Sufiksni automat

[Sufiksni automat](../string/sam.md) prihvaća sufikse zadanog niza i nijedan drugi niz.

### Generalizirani sufiksni automat

[Generalizirani sufiksni automat](../string/general-sam.md) prihvaća sufikse nekog elementa zadanog skupa nizova i nijedan drugi niz. Drugim riječima, trie + SAM.

Odnos generaliziranog SAM-a i SAM-a jednak je odnosu AC automata i KMP automata.

### Palindromski automat

[Palindromski automat](../string/pam.md) poseban je po tome što se ne može baš zgodno definirati kao automat.

Ako ga ipak želimo definirati, on prihvaća **središte i desnu polovicu** svakog palindromskog podniza nekog niza i ništa drugo.

„Središte i desna polovica” kod palindroma neparne duljine znači doslovno to, a kod palindroma parne duljine definira se kao poseban znak nakon kojeg slijedi desna polovica. Ta definicija izgleda vrlo čudno, ali upravo ona PAM čini pravim automatom, a ne tek dvama stablima.

### Automat podnizova

[Automat podnizova](../string/seq-automaton.md) prihvaća podnizove zadanog niza i nijedan drugi niz.

### DP unutar DP-a

[DP unutar DP-a](../dp/dp-of-dp.md) jedna je primjena automata; može se promatrati kao tehnika u kojoj se najprije unutarnjim DP-om izgradi automat, a zatim se vanjskim DP-om po tom automatu rješavaju zadaci prebrojavanja i optimizacije.

## Sufiksne poveznice

Budući da su automati neraskidivo povezani s podudaranjem, a jedna je temeljna ideja podudaranja „ako ovaj niz ne odgovara, pokušaj s njegovim sufiksom”, u mnogim automatima (KMP, AC automat, SAM, PAM) postoji pojam sufiksne poveznice.

Jedno stanje odgovara nekoliko nizova. Njegova sufiksna poveznica pokazuje na stanje automata koje odgovara najduljem zajedničkom pravom sufiksu nizova pridruženih tom stanju. Općenito sufiksne poveznice tvore stablo, a stabla sufiksnih poveznica različitih automata imaju neka zajednička svojstva na koja pri učenju vrijedi obratiti pozornost.

## Dodatna literatura

-   [计算复杂性（1）Warming Up: 自动机模型 (Računska složenost (1), Warming Up: model automata)](https://lingeros-tot.github.io/2019/03/05/Warming-Up-自动机模型/)
-   [国家集训队 2021 论文 徐哲安 浅谈有限状态自动机及其应用 (Zbornik radova kineske nacionalne reprezentacije 2021., Xu Zhe'an: Kratki pregled konačnih automata i njihovih primjena)](https://github.com/OIerTFX/IOI/blob/master/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2021%E8%AE%BA%E6%96%87%E9%9B%86/pdf-files/%E5%BE%90%E5%93%B2%E5%AE%89%20%E6%B5%85%E8%B0%88%E6%9C%89%E9%99%90%E7%8A%B6%E6%80%81%E8%87%AA%E5%8A%A8%E6%9C%BA%E5%8F%8A%E5%85%B6%E5%BA%94%E7%94%A8.pdf)
-   [Myhill–Nerode theorem - Wikipedia](https://en.wikipedia.org/wiki/Myhill%E2%80%93Nerode_theorem)
-   Knuutila, Timo. "Re-describing an algorithm by Hopcroft." Theoretical Computer Science 250, no. 1-2 (2001): 333-363.
-   Hopcroft, John E., Rajeev Motwani, and Jeffrey D. Ullman. "Introduction to automata theory, languages, and computation." 2nd ed. Addison-Wesley, 2001.

[^nfa-and-nfaepsilon]: U ovoj definiciji dopuštamo prijelaze između stanja praznim znakom ($\varepsilon$), pa je, točnije rečeno, riječ o nedeterminističkom konačnom automatu s $\varepsilon$-prijelazima (NFA-$\varepsilon$). Neki ga udžbenici nazivaju jednostavno NFA; radi sažetosti i ovaj tekst slijedi taj običaj. Teorijski se NFA i NFA-$\varepsilon$ razlikuju, ali im je računska moć zapravo jednaka.

[^state-elimination-method]: Vidi odjeljak 3.2 u [国家集训队 2021 论文 徐哲安 浅谈有限状态自动机及其应用 (Zbornik radova kineske nacionalne reprezentacije 2021., Xu Zhe'an: Kratki pregled konačnih automata i njihovih primjena)](https://github.com/OIerTFX/IOI/blob/master/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2021%E8%AE%BA%E6%96%87%E9%9B%86/pdf-files/%E5%BE%90%E5%93%B2%E5%AE%89%20%E6%B5%85%E8%B0%88%E6%9C%89%E9%99%90%E7%8A%B6%E6%80%81%E8%87%AA%E5%8A%A8%E6%9C%BA%E5%8F%8A%E5%85%B6%E5%BA%94%E7%94%A8.pdf).

[^prove-regular-language]: Vidi [službeno rješenje](https://qoj.ac/download.php?type=attachments&id=2079&r=1).

[^smaller-evidence]: „Jednakovrijedna” ovdje znači: iako svjedok $P_x$ možda nije stvarno provjeren, provjera trenutačne podjele svjedokom $P_x$ ne bi donijela nikakvo poboljšanje. Jednostavno rečeno, u stablu svjedoka nastalom cijepanjem skupova neki je njegov predak i sve bočne grane na putu do njega već provjereno, pa se induktivno može pokazati da je to jednakovrijedno tome da je i on već provjeren.

[^detail]: U implementaciji algoritma postoji jedna pojedinost: za svjedoka $A$ moguće je da se nakon provjere dijela znakova taj skup svjedoka već rascijepio na $B$ i $C$. Neka je, bez smanjenja općenitosti, $|B|\ge |C|$. U referentnoj implementaciji manji skup $C$ umeće se na kraj reda svjedoka, a veći skup svjedoka $B$ zamjenjuje $A$ na njegovu dotadašnjem mjestu. Kad algoritam nastavi, preostali se znakovi zapravo provjeravaju samo svjedokom $B$. To je ispravno: za već provjerene znakove provjerena su barem dva skupa, $A$ i $C$, a za još neprovjerene znakove provjerena su barem dva skupa, $B$ i $C$.

[^upper-bound]: Vidi primjer 5.2 u [国家集训队 2021 论文 徐哲安 浅谈有限状态自动机及其应用 (Zbornik radova kineske nacionalne reprezentacije 2021., Xu Zhe'an: Kratki pregled konačnih automata i njihovih primjena)](https://github.com/OIerTFX/IOI/blob/master/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2021%E8%AE%BA%E6%96%87%E9%9B%86/pdf-files/%E5%BE%90%E5%93%B2%E5%AE%89%20%E6%B5%85%E8%B0%88%E6%9C%89%E9%99%90%E7%8A%B6%E6%80%81%E8%87%AA%E5%8A%A8%E6%9C%BA%E5%8F%8A%E5%85%B6%E5%BA%94%E7%94%A8.pdf).

[^is-dfa]: Definicija automata u ovom tekstu zahtijeva da automat bude potpun, tj. da svako stanje za svaki znak ima prijelaz. U opisima ovih automata vezanih uz nizove znakova stanje neuspjeha obično se izostavlja. Trie, SAM i drugi takvi su primjeri. Da bi odgovarali definiciji iz ovog teksta, u opise tih automata treba izričito dodati stanje neuspjeha.
