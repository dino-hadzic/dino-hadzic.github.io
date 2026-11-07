---
title: Nepristrane kombinatorne igre
---

Preduvjeti: [Uvod u teoriju igara](./intro.md)

U ovom članku raspravljamo o [nepristranim kombinatornim igrama](./intro.md#公平组合博弈) (impartial games).

Među nepristranim kombinatornim igrama najosnovnija i najvažnija jest normalna Nim igra. Sprague–Grundyjev teorem kaže da je svaka nepristrana kombinatorna igra s normalnim pravilom ekvivalentna Nim igri s jednom hrpom. Iz toga se mogu razviti pojmovi Sprague–Grundyjeve funkcije i Nim-brojeva, koji potpuno opisuju nepristranu kombinatornu igru s normalnim pravilom. Zato u ovom članku najprije izvodimo rezultate o normalnoj Nim igri i Sprague–Grundyjevu teoriju. Nakon toga raspravljamo o nekim nepristranim kombinatornim igrama koje se često pojavljuju na algoritamskim natjecanjima.

Na kraju se kratko bavimo misère (obrnutom) Nim igrom. Misère igre znatno su složenije od normalnih igara i rijetko se pojavljuju na algoritamskim natjecanjima. Ako nije posebno rečeno, sve igre spomenute u ovom članku podrazumijevaju se kao normalne nepristrane kombinatorne igre.

???+ info "„Stanje”, „pozicija” i „igra”"
    U ovom članku ta se tri izraza koriste naizmjenično. U teoriji igara stanje (state) igre obično obuhvaća sve informacije koje bi do određenog trenutka igre mogle biti povezane s igrom. U općem slučaju stanje igre obično obuhvaća prošle poteze obaju igrača, već realizirane vrijednosti slučajnih varijabli, sadržaj informacija poznatih obama igračima i slično. Pozicija (position) igre razmjerno nije standardni izraz teorije igara; obično označava situaciju s kojom se oba igrača suočavaju u određenom trenutku igre, npr. položaj figura u igrama na ploči. Samo za nepristrane kombinatorne igre (ili općenitije: igre nulte sume, determinističke, s potpunom informacijom) vrijedi da, budući da igra ne uključuje slučajnost, a skup budućih poteza igrača i funkcija dobitka ne ovise o povijesti puta kojim se došlo do trenutne pozicije (tj. o prethodnim potezima obaju igrača), nema razlike između stanja (state) i pozicije (position) igre, te se oboje može promatrati kao čvor (node) grafa igre. Budući da se igra (game) uvijek može opisati svojom početnom pozicijom, ponekad se riječ „pozicija” koristi izravno i za samu igru.

## Nim igra

Pravila Nim igre vrlo su jednostavna:

???+ abstract "Nim igra"
    Imamo $n$ hrpa kamenčića, a $i$-ta hrpa sadrži $a_i$ kamenčića. Dva igrača naizmjence uzimaju proizvoljan broj kamenčića s proizvoljne jedne hrpe, ali ne smiju propustiti potez. Pobjeđuje igrač koji uzme posljednji kamenčić.

Lako je provjeriti da je Nim igra nepristrana kombinatorna igra s normalnim pravilom.

???+ example "Primjer"
    Evo primjera. Trenutačno imamo $3$ hrpe kamenčića, s redom $2,5,4$ kamenčića. Tada možemo uzeti $2$ kamenčića s $1$. hrpe i pozicija postaje $0, 5, 4$; možemo i uzeti $4$ kamenčića s $2$. hrpe i pozicija postaje $2, 1, 4$. Ako u nekom trenutku pozicija postane $0, 0, 5$ i na potezu je igrač A, tada A može uzeti $5$ kamenčića s $3$. hrpe, tj. uzeti posljednji kamenčić, i tada A pobjeđuje.

### Graf igre i stanja

Moguće promjene pozicije u Nim igri mogu se opisati grafom igre (game graph).

Promatramo li svako moguće stanje kao čvor grafa i povučemo li brid od svakog stanja do njegovih sljedbenika (tj. stanja do kojih se može doći jednim potezom), dobivamo usmjereni aciklički graf; to je graf igre. Graf je aciklički jer se u Nim igri svakim potezom ukupan broj kamenčića strogo smanjuje.

???+ example "Primjer"
    Na primjer, za Nim igru s početnom pozicijom od $3$ hrpe kamenčića, u kojima je redom $1,1,2$ kamenčića, možemo nacrtati sljedeći graf igre:
    
    ![Primjer grafa igre](./images/nim.svg)
    
    Kao što ćemo odmah spomenuti, crveni čvorovi na slici označavaju pobjednička stanja, a crni gubitnička stanja.

Budući da je Nim igra nepristrana kombinatorna igra, to ima li igrač pobjedničku strategiju ovisi samo o trenutačnom stanju igre, a ne o tome koji je igrač na potezu. Zato se sva stanja mogu podijeliti na **pobjednička stanja** (za igrača na potezu) i **gubitnička stanja** (za igrača na potezu), koja označavamo redom kao $\mathcal N$-stanja i $\mathcal P$-stanja[^n-vs-p]. Ta definicija vrijedi za sve nepristrane kombinatorne igre.

Pomoću sljedeće leme sva se stanja mogu induktivno označiti kao pobjednička ili gubitnička:

???+ note "Lema"
    U nepristranoj kombinatornoj igri s normalnim pravilom
    
    1.  stanje bez sljedbenika gubitničko je stanje $\mathcal P$,
    2.  stanje je pobjedničko stanje $\mathcal N$ ako i samo ako postoji barem jedan njegov sljedbenik koji je gubitničko stanje $\mathcal P$,
    3.  stanje je gubitničko stanje $\mathcal P$ ako i samo ako su svi njegovi sljedbenici pobjednička stanja $\mathcal N$.

??? note "Dokaz"
    Za prvu tvrdnju: ako igrač trenutačno nema nijedan dopušten potez, već je izgubio igru.
    
    Za drugu tvrdnju: ako stanje ima barem jednog sljedbenika koji je gubitničko stanje, igrač može odigrati potez u to gubitničko stanje; tada se protivnik nalazi u stanju koje je gubitničko za igrača na potezu, pa igrač pobjeđuje.
    
    Za treću tvrdnju: ako ne postoji nijedan sljedbenik koji je gubitničko stanje, igrač može, kako god odigrao, prijeći samo u pobjedničko stanje; tada se protivnik nalazi u stanju koje je pobjedničko za igrača na potezu, pa igrač gubi igru.

U svim nepristranim kombinatornim igrama graf igre usmjereni je aciklički graf. Zato pomoću ta tri svojstva, nakon što nacrtamo graf igre, u vremenu $O(|V|+|E|)$ možemo za svako stanje izračunati je li pobjedničko ili gubitničko. Pritom je $|V|$ broj stanja u grafu igre, a $|E|$ broj bridova, tj. ukupan broj poteza koji se mogu odigrati iz svih stanja.

Ta se lema može poopćiti na misère igre i na slučaj kad usmjereni graf može imati cikluse. Više o tome u odjeljku [Igra na usmjerenom grafu](#igra-na-usmjerenom-grafu).

### Nim-zbroj

Nastavimo s proučavanjem Nim igre.

Crtanjem grafa igre možemo odrediti pobjeđuje li igrač na potezu u nekoj poziciji. No za to je potrebno $\Omega(\prod_{i=1}^n(a_i+1))$ vremena, što je previsoka složenost i nije praktično primjenjivo. Zapravo se može uočiti da to je li stanje Nim igre pobjedničko za igrača na potezu ovisi samo o Nim-zbroju brojeva kamenčića u trenutačnoj poziciji.

???+ abstract "Nim-zbroj"
    **Nim-zbroj** (Nim sum) prirodnih brojeva $a_1,a_2,\cdots,a_n$ definira se kao $a_1\oplus a_2\oplus\cdots\oplus a_n$.

Nim-zbroj zapravo je [operacija isključivog ili (xor)](../bit.md#logičke-operacije-po-bitovima).

???+ note "Teorem"
    U Nim igri stanje $(a_1,a_2,\cdots,a_n)$ gubitničko je stanje $\mathcal P$ ako i samo ako je Nim-zbroj
    
    $$
    a_1\oplus a_2\oplus\cdots\oplus a_n = 0.
    $$

??? note "Dokaz"
    Primijenimo indukciju po svim mogućim stanjima:
    
    1.  Ako vrijedi $a_i=0$ za sve $i=1,\cdots,n$, stanje nema sljedbenika, a Nim-zbroj jednak je $0$, pa tvrdnja vrijedi.
    2.  Ako je $k = a_1\oplus a_2\oplus\cdots\oplus a_n\neq 0$, treba dokazati da je stanje pobjedničko. Drugim riječima, treba konstruirati dopušten potez takav da je sljedbenik gubitničko stanje; po pretpostavci indukcije dovoljno je dokazati da sljedbenik zadovoljava $a'_1\oplus a'_2\oplus\cdots\oplus a'_n=0$. Prema svojstvima Nim-zbroja (tj. operacije xor) to je ekvivalentno tvrdnji da postoji $i$-ta hrpa kamenčića s koje se može uzeti nekoliko kamenčića tako da njihov broj postane $a_i\oplus k$, tj. da vrijedi $a_i>a_i\oplus k$.
    
        Doista, neka je u binarnom zapisu broja $k$ najviša znamenka $1$ na $d$-tom mjestu. Tada sigurno postoji neki $a_i$ čiji je $d$-ti bit jednak $1$. Za odgovarajuću hrpu sigurno vrijedi $a_i>a_i\oplus k$, jer je $d$-ti bit broja $a_i\oplus k$ jednak $0$, a viši bitovi isti su kao u $a_i$.
    3.  Ako je $a_1\oplus a_2\oplus\cdots\oplus a_n= 0$, treba dokazati da je stanje gubitničko. Po pretpostavci indukcije dovoljno je dokazati da Nim-zbroj nijednog njegova sljedbenika nije $0$. To je nužno tako: svaki dopušten potez mijenja $a_i$ u $a'_i\neq a_i$, pa Nim-zbroj nužno postaje $a'_i\oplus a_i\neq 0$.

Prema tome, u vremenu $O(n)$ možemo odrediti je li stanje Nim igre pobjedničko za igrača na potezu.

## Sprague–Grundyjeva teorija

Sprague–Grundyjeva teorija kaže da je svaka nepristrana kombinatorna igra s normalnim pravilom ekvivalentna Nim igri s jednom hrpom. Glavna situacija u kojoj se taj rezultat primjenjuje jest kad se igra sastoji od više međusobno nezavisnih podigara. Tada se stanje igre može odrediti računanjem Nim-zbroja vrijednosti SG funkcije podigara. Ako igra sama nema takvu strukturu, za određivanje pobjedničkih i gubitničkih stanja dovoljno je primijeniti lemu iz prethodnog odjeljka [Graf igre](#graf-igre-i-stanja).

### Zapis igara

Već smo rekli da se svaka nepristrana kombinatorna igra može opisati crtanjem grafa igre. Budući da u grafu igre svojstva svakog stanja ovise samo o njegovim sljedbenicima, stanje $S$ u grafu igre možemo prikazati skupom njegovih sljedbenika.

???+ example "Primjer (nastavak)"
    Za gornji graf igre dobivamo sljedeći prikaz stanja:
    
    $$
    \begin{aligned}
    S_{0,0,0} &= \{\},\\
    S_{0,1,0} &= \{S_{0,0,0}\} = \{\{\}\},\\
    S_{0,0,1} &= \{S_{0,0,0}\} = \{\{\}\},\\
    S_{0,0,2} &= \{S_{0,0,0},S_{0,0,1}\} = \{\{\},\{\{\}\}\},\\
    S_{0,1,1} &= \{S_{0,1,0},S_{0,0,1}\} = \{\{\{\}\}\},\\
    S_{0,1,2} &= \{S_{0,0,2},S_{0,1,0},S_{0,1,1}\} = \{\{\{\},\{\{\}\}\},\{\{\}\},\{\{\{\}\}\}\}.
    \end{aligned}
    $$
    
    Pritom je $S_{0,1,0}=S_{0,0,1}$.

Igra se može prikazati svojim početnim stanjem.

Iako prikaz nepristrane igre može biti prilično složen, Nim igra s jednom hrpom razmjerno je mnogo jednostavnija. Kad postoji samo jedna hrpa s $n$ kamenčića, može se prikazati kao

$$
*0 = \{\},~*n = \{*m : m<n,~m\in\mathbf N\} = \{*0,*1,\cdots,*(n-1)\}.
$$

Pritom oznaka $*n$ označava (početno stanje) Nim igre s jednom hrpom od $n$ kamenčića.

???+ example "Primjer (nastavak)"
    Tom se oznakom stanja iz gornjeg primjera mogu jednostavno zapisati kao
    
    $$
    S_{0,0,0} = *0,~
    S_{0,1,0} = S_{0,0,1} = *1,~
    S_{0,0,2} = *2,~
    S_{0,1,1} = \{*1\},~
    S_{0,1,2} = \{*1, *2, \{*1\}\}.
    $$

U daljnjoj raspravi oznaku $T\in S$ treba shvatiti tako da je stanje $T$ sljedbenik stanja $S$.

### Zbroj i ekvivalencija igara

Relacija ekvivalencije igara oslanja se na pojam zbroja igara[^more-sums].

???+ note "Zbroj igara"
    **Zbroj** (sum) igara $G$ i $H$, ili **kombinirana igra** (combined game), u oznaci $G+H$, jest igra
    
    $$
    G + H = \{g + H : g \in G\} \cup \{G + h : h \in H\}.
    $$

Zbroj igara možemo shvatiti kao igru sastavljenu od dviju podigara koje se odvijaju istodobno i ne utječu jedna na drugu; igrač u svakom potezu može i mora odabrati točno jednu od podigara i u njoj odigrati jedan potez, a igra završava kad se ni u jednoj od dviju podigara više ne može odigrati potez. Pojam zbroja igara može se poopćiti na proizvoljno mnogo igara i zadovoljava asocijativnost i komutativnost – drugim riječima, rezultat kombiniranja više igara ne ovisi ni o redoslijedu kombiniranja ni o poretku igara. Nim igra zbroj je više Nim igara s jednom hrpom.

Jedno je opažanje sljedeće: iako su u Nim igri s jednom hrpom sva stanja osim onoga bez kamenčića pobjednička za igrača na potezu, te različite Nim igre s jednom hrpom ne daju iste igre kad se kombiniraju s drugim Nim igrama s jednom hrpom. Na primjer, igra $*n$ daje gubitničku igru samo kad se kombinira s još jednom igrom $*n$; kombiniranjem sa svim ostalim Nim igrama s jednom hrpom $*n'\neq *n$ dobivaju se pobjedničke igre.

Pouka tog opažanja jest da se svojstva neke igre mogu proučavati promatranjem njezinih zbrojeva s drugim igrama. To nas dovodi do pojma ekvivalencije igara.

???+ abstract "Relacija ekvivalencije igara"
    Ako su za sve igre $H$ igre $G_1+H$ i $G_2+H$ obje gubitnička stanja ili obje pobjednička stanja, kažemo da su igre $G_1$ i $G_2$ **ekvivalentne** (equivalent) i pišemo $G_1\approx G_2$.

Lako je provjeriti da je tako definirana relacija $\approx$ doista [relacija ekvivalencije](../order-theory.md#二元关系) na skupu svih nepristranih igara.

### Sprague–Grundyjeva funkcija

Analiza Nim igre pokazuje da različite Nim igre s jednom hrpom nisu međusobno ekvivalentne. Međutim, svaka nepristrana igra ekvivalentna je nekoj Nim igri s jednom hrpom. Zato se svakoj nepristranoj igri može pridružiti broj; to je Sprague–Grundyjeva funkcija.

Za dokaz tih rezultata najprije treba uspostaviti dvije leme o relaciji ekvivalencije igara. Prvo, kombiniranje gubitničke igre s bilo kojom igrom daje igru ekvivalentnu izvornoj.

???+ note "Lema 1"
    Za igru $G$ i bilo koju gubitničku igru $A\in\mathcal P$ vrijedi $G\approx G + A$.

??? note "Dokaz"
    Po definiciji dovoljno je dokazati da su za svaku igru $H$ igre $G+H$ i $G+A+H$ obje gubitnička stanja ili obje pobjednička stanja.
    
    Ako igra $G+H$ ima pobjedničku strategiju, tada i igra $G+A+H$ ima pobjedničku strategiju. Ako protivnik odigra potez u podigri $A$, odigramo potez u podigri $A$ i vratimo je u gubitničko stanje; inače igramo prema pobjedničkoj strategiji za igru $G+H$. Tako sigurno osiguravamo konačnu pobjedu.
    
    Ako je igra $G+H$ gubitnička igra, tada je i igra $G+A+H$ gubitnička igra. Naime, bez obzira na to odigramo li u ovom potezu u podigri $G+H$ ili u podigri $A$, protivnik može u sljedećem potezu odgovarajuću podigru vratiti u gubitničko stanje. Na kraju igrač koji je prvi na potezu sigurno ne može pobijediti.

Drugo, dvije su igre ekvivalentne ako i samo ako je njihov zbroj gubitnička igra. Ta lema daje način dokazivanja ekvivalencije dviju igara.

???+ note "Lema 2"
    Igre $G$ i $G'$ ekvivalentne su ako i samo ako je $G+G'\in\mathcal P$ gubitnička igra.

??? note "Dokaz"
    Ako su igre $G$ i $G'$ ekvivalentne, tada su $G+G'$ i $G+G$ istodobno pobjedničke ili istodobno gubitničke, a igra $G+G$ gubitnička je igra. Naime, na svaki potez prvog igrača drugi igrač može odigrati isti potez u drugoj podigri, pa na kraju sigurno prvi igrač nema poteza.
    
    Obratno, ako je $G+G'$ gubitnička igra, tada po lemi 1 vrijedi $G\approx G+(G+G') = (G+G)+G' \approx G'$.

Pomoću tih lema dobivamo sljedeći teorem:

???+ note "Teorem (Sprague–Grundy)"
    Za svaku (konačnu) nepristranu igru $G$ postoji $n\in\mathbf N$ takav da vrijedi $G\approx *n$.

??? note "Dokaz"
    Tvrdnju teorema dokazujemo matematičkom indukcijom. Neka je igra $G = \{G_1,G_2,\cdots,G_k\}$. Po pretpostavci indukcije postoje $n_1,n_2,\cdots,n_k$ takvi da je $G_i\approx *n_i$; tada možemo promatrati igru
    
    $$
    G' = \{*n_1,*n_2,\cdots,*n_k\}.
    $$
    
    Dokazat ćemo da je $G'\approx *m$, gdje je $m=\operatorname{mex}\{n_1,n_2,\cdots,n_k\}$ najmanji prirodni broj koji se ne pojavljuje u skupu.
    
    U prvom koraku treba pokazati $G\approx G'$. Po lemi 2 dovoljno je dokazati da je igra $G+G'$ gubitnička igra. Bez smanjenja općenitosti neka je $G\neq *0$. Ako prvi igrač odabere $G_i$, drugi igrač može odabrati $*n_i$; obratno, ako prvi igrač odabere $*n_i$, drugi igrač može odabrati $G_i$. U svakom slučaju, nakon ta dva poteza igra postaje $G_i+*n_i$, što je po lemi 2 i $G_i\approx *n_i$ gubitnička igra. Time je dokazano $G\approx G'$.
    
    U drugom koraku treba pokazati $G'\approx*m$. Po lemi 2 dovoljno je dokazati da je $G'+*m$ gubitnička igra. Bez smanjenja općenitosti neka je $G'\neq *0$. Ako prvi igrač odabere $*n_i\in *m$, tada po definiciji broja $m$ drugi igrač može odabrati $*n_i\in G'$ i pozicija igre postaje $*n_i + *n_i\in\mathcal P$, pa prvi igrač gubi. Ako prvi igrač odabere $*n_i\in G'$ uz $n_i<m$, drugi igrač može odabrati $*n_i\in *m$ i pozicija igre jednako tako postaje $*n_i+*n_i\in\mathcal P$, pa prvi igrač gubi. Konačno, ako prvi igrač odabere $*n_i\in G'$ uz $n_i>m$, drugi igrač može odabrati $*m\in *n_i$ i pozicija igre postaje $*m+*m\in\mathcal P$, pa prvi igrač gubi. Time je dokazano $G'\approx *m$.
    
    Po tranzitivnosti relacije ekvivalencije slijedi $G\approx *m$. Time je indukcija dovršena i dokazano je da je svaka igra $G$ ekvivalentna nekoj Nim igri s jednom hrpom.

Taj rezultat pokazuje da se svakoj nepristranoj igri $G$ može pridružiti prirodni broj $n$ takav da je $G\approx *n$.

???+ abstract "Nim-broj"
    **Nim-broj** (nimber) koji odgovara nepristranoj igri $G$ jedinstveni je prirodni broj $n$ za koji vrijedi $G\approx *n$.

Funkcija koja nepristranu igru preslikava u njezin Nim-broj naziva se **Sprague–Grundyjeva funkcija** (Sprague–Grundy function), skraćeno **SG funkcija**, i označava se $\operatorname{SG}(\cdot)$. Budući da je svako stanje nepristrane igre i samo nepristrana igra, za svako stanje nepristrane igre može se izračunati odgovarajući Nim-broj, koji se naziva i pripadnom vrijednošću SG funkcije.

Iz dokaza teorema u ovom odjeljku slijedi da se Sprague–Grundyjeva funkcija može rekurzivno računati ovako:

???+ note "Korolar"
    Vrijednost Sprague–Grundyjeve funkcije $\operatorname{SG}(x)$ koja odgovara stanju $x$ nepristrane igre $G$ zadovoljava
    
    $$
    \operatorname{SG}(x) = \operatorname{mex}\{\operatorname{SG}(x'): x'\in x\}.
    $$
    
    Pritom je $\operatorname{mex}(A):=\min\{n\in\mathbf N:n\notin A\}$ najmanji prirodni broj koji se ne pojavljuje u skupu $A$.

Drugim riječima, vrijednost SG funkcije nekog stanja jednaka je vrijednosti $\operatorname{mex}$ vrijednosti SG funkcije svih njegovih sljedbenika.

Pomoću vrijednosti SG funkcije (tj. Nim-broja) može se odrediti je li stanje pobjedničko za igrača na potezu.

???+ note "Korolar"
    Stanje $x$ nepristrane igre $G$ pobjedničko je za igrača na potezu ako i samo ako je $\operatorname{SG}(x)\neq 0$.

Konačno, vrijednost SG funkcije zbroja igara jednaka je Nim-zbroju (tj. xor-u) vrijednosti SG funkcije podigara.

???+ note "Teorem (Sprague–Grundy)"
    Za nepristrane igre $G_1,G_2,\cdots,G_n$ vrijedi
    
    $$
    \operatorname{SG}(G_1+ G_2+\cdots + G_n) = \operatorname{SG}(G_1)\oplus \operatorname{SG}(G_2)\oplus\cdots\oplus\operatorname{SG}(G_n).
    $$

??? note "Dokaz"
    Budući da je $*a_1+ *a_2 + \cdots + *a_n$ upravo Nim igra s brojevima kamenčića $(a_1,a_2,\cdots,a_n)$, prema rezultatu o Nim igri igra
    
    $$
    *a_1+ *a_2 + \cdots + *a_n + *(a_1\oplus a_2\oplus\cdots\oplus a_n)
    $$
    
    gubitnička je za igrača na potezu. Po lemi 2 vrijedi
    
    $$
    *a_1+ *a_2 + \cdots + *a_n \approx *(a_1\oplus a_2\oplus\cdots\oplus a_n).
    $$
    
    Dakle vrijedi
    
    $$
    \operatorname{SG}(*a_1 + *a_2 + \cdots + *a_n) = a_1\oplus a_2\oplus\cdots\oplus a_n.
    $$
    
    Stavimo $a_i=\operatorname{SG}(G_i)$; tada je $G_i\approx *a_i$, pa prema algebarskim svojstvima relacije $\approx$ vrijedi
    
    $$
    (G_1+ G_2+\cdots + G_n) + (*a_1 + *a_2 + \cdots + *a_n) = \sum_{i=1}^n(G_i+*a_i) \in\mathcal P.
    $$
    
    Stoga vrijedi
    
    $$
    \begin{aligned}
    \operatorname{SG}(G_1+ G_2+\cdots + G_n) &= \operatorname{SG}(*a_1 + *a_2 + \cdots + *a_n) \\
    &= a_1\oplus a_2\oplus \cdots \oplus a_n \\
    &= \operatorname{SG}(G_1)\oplus \operatorname{SG}(G_2)\oplus\cdots\oplus\operatorname{SG}(G_n).
    \end{aligned}
    $$

Pomoću tog teorema računanje vrijednosti SG funkcije zbroja igara može se znatno pojednostavniti.

Iz toga možemo sažeti postupak računanja vrijednosti SG funkcije:

-   za više nezavisnih igara možemo zasebno izračunati njihove vrijednosti SG funkcije i zatim uzeti Nim-zbroj;
-   za pojedinu igru vrijednost SG funkcije svakog stanja jednaka je vrijednosti $\operatorname{mex}$ vrijednosti SG funkcije svih njegovih sljedbenika;
-   posebno, vrijednost SG funkcije završnog stanja (tj. stanja bez sljedbenika) jednaka je $\operatorname{mex}\varnothing = 0$.

### Nim-brojevi

Svakoj nepristranoj igri jedinstveno odgovara jedan Nim-broj. Skup (konačnih) Nim-brojeva upravo je skup prirodnih brojeva $\mathbf N$. Međutim, njegova algebarska svojstva razlikuju se od svojstava skupa prirodnih brojeva. Konkretno, na Nim-brojevima mogu se definirati dvije operacije: Nim-zbroj $\oplus$ i Nim-produkt $\otimes$:

???+ abstract "Operacije s Nim-brojevima"
    Za Nim-brojeve $a,b$ možemo definirati:
    
    -   Nim-zbroj $a\oplus b=\operatorname{mex}(\{a'\oplus b:a'<a,~a'\in\mathbf N\}\cup\{a\oplus b':b'<b,~b'\in\mathbf N\})$,
    -   Nim-produkt $a\otimes b=\operatorname{mex}(\{(a'\otimes b)\oplus(a\otimes b')\oplus(a'\otimes b'):a'<a,~b'<b,~a',b'\in\mathbf N\})$.

Skup svih Nim-brojeva uz operacije $\oplus$ i $\otimes$ čini [polje](../algebra/basic.md#域) karakteristike $2$. Štoviše, te operacije i njihove inverzne operacije zatvorene su na prvih $2^{2^n}$ Nim-brojeva; tako se dobiva niz [konačnih polja](../algebra/field-theory.md#有限域) $\mathbf F_{2^{2^n}}$ veličine $2^{2^n}$.

## Uobičajene nepristrane igre

Iako Sprague–Grundyjeva teorija potpuno rješava problem nepristranih igara, pri obradi konkretnih nepristranih igara izravna primjena Sprague–Grundyjeva teorema i dalje nije učinkovita. Na primjer, u Nim igri složenost računanja Sprague–Grundyjevih vrijednosti grubom silom eksponencijalna je. Zato je rezultate za konkretne nepristrane igre često potrebno pogoditi tabliranjem (ispisom tablice vrijednosti programom).

U ovom odjeljku navodimo neke uobičajene nepristrane igre i rezultate o njima. Pri iskazivanju rezultata navodimo samo pravilo za određivanje pobjedničkih i gubitničkih stanja. Pobjednička strategija pak sastoji se u odigravanju prikladnog poteza tako da pozicija koju ostavljamo protivniku bude upravo gubitničko stanje. Budući da se na algoritamskim natjecanjima često pojavljuju varijante tih igara, važno je svladati i tijek dokaza rezultata za svaku igru.

???+ info "Metoda dokazivanja rezultata u ovom odjeljku"
    Dokazi rezultata u ovom odjeljku provjerni su. Za neku igru rezultat opisuje njezina gubitnička i pobjednička stanja za igrača na potezu. U dokazu je dovoljno provjeriti da se iz gubitničkog stanja mogu dobiti samo pobjednička stanja, a da se iz pobjedničkog stanja uvijek može dobiti barem jedno gubitničko stanje. Da bi se ti dokazi prepisali u stroge dokaze, treba izgraditi graf igre i zatim na stanjima grafa igre primijeniti matematičku indukciju; ti su provjerni koraci upravo njezin induktivni dio.

### Bachetova igra

U odnosu na Nim igru s jednom hrpom, Bachetova igra (Bash game) ograničava broj kamenčića koji se mogu uzeti u jednom potezu.

???+ abstract "Bachetova igra"
    Imamo jednu hrpu s ukupno $n$ kamenčića. Dva igrača naizmjence uzimaju najmanje $1$, a najviše $k$ kamenčića. Pobjeđuje igrač koji uzme posljednji kamenčić.

O tome vrijedi sljedeći rezultat:

???+ note "Teorem"
    Igrač na potezu gubi ako i samo ako je $n\equiv 0\pmod {k+1}$.

??? note "Dokaz 1"
    Kad je $n\not\equiv 0\pmod {k+1}$, dovoljno je uzeti $n\bmod{(k+1)}\in[1,k]$ kamenčića da bi protivnik sigurno bio u gubitničkom stanju. Dakle to je pobjedničko stanje za igrača na potezu.
    
    Obratno, kad je $n\equiv 0\pmod {k+1}$, ili više nema izbora, ili nakon što uzmemo $k'$ kamenčića protivnik odmah može uzeti $k+1-k'$ kamenčića i vratiti nas u gubitničko stanje.

??? note "Dokaz 2"
    Kao primjenu Sprague–Grundyjeva teorema možemo izračunati $f(n)$, vrijednost SG funkcije pozicije u kojoj je preostalo $n$ kamenčića.
    
    Za $n\le k$ induktivno se dokazuje $f(n)=n$. To je isto kao u Nim igri s jednom hrpom, jer ograničenje broja uzetih kamenčića ne igra nikakvu ulogu. Za $n>k$ treba dokazati $f(n)=n\bmod{(k+1)}$. Budući da se svaki put može uzeti od $1$ do $k$ kamenčića, vrijedi
    
    $$
    f(n) = \operatorname{mex}\{f(n-k),f(n-k+1),\cdots,f(n-1)\}.
    $$
    
    Po pretpostavci indukcije to prolazi kroz sve ostatke modulo $k+1$ osim $n\bmod{(k+1)}$. Stoga vrijedi $f(n) = n\bmod{(k+1)}$.

### Mooreov Nim-k

U odnosu na Nim igru, Mooreov Nim-$k$ dopušta da se u jednom potezu uzimaju kamenčići s najviše $k$ hrpa.

???+ abstract "Mooreov Nim-$k$"
    Imamo $n$ hrpa kamenčića, a $i$-ta hrpa sadrži $a_i$ kamenčića. Dva igrača naizmjence uzimaju proizvoljan broj kamenčića s najmanje $1$, a najviše $k$ hrpa, ali ne smiju propustiti potez. Pobjeđuje igrač koji uzme posljednji kamenčić.

O tome vrijedi sljedeći rezultat:

???+ note "Teorem"
    Zapišimo broj kamenčića na svakoj hrpi binarno i za svako mjesto $d$ prebrojimo koliko hrpa ima $1$ na $d$-tom bitu broja kamenčića te izračunajmo ostatak tog broja pri dijeljenju s $(k+1)$. Ako je za svako mjesto taj ostatak jednak $0$, igrač na potezu gubi; inače igrač na potezu pobjeđuje.

??? note "Dokaz"
    Po uzoru na dokaz rezultata o Nim igri ovaj se rezultat lako dokazuje. Neka je $d$ najviše binarno mjesto na kojem ostatak nije $0$ i neka je odgovarajući ostatak $k'\le k$. Tada se pobjednička strategija sastoji u tome da među hrpama čiji broj kamenčića ima $1$ na $d$-tom bitu odaberemo $k'$ hrpa i odaberemo brojeve uzetih kamenčića upravo tako da u protivnikovoj poziciji ostatak na svakom mjestu bude $0$. Jedino što treba objasniti jest da je takav odabir brojeva uzetih kamenčića uvijek moguć.
    
    Doista, dovoljno je $d$-ti bit svih $k'$ odabranih hrpa postaviti na $0$ da bi ostatak na $d$-tom mjestu u rezultatu postao $0$; budući da se viši bitovi ne mijenjaju, niži bitovi tih hrpa mogu se postaviti proizvoljno. Niža mjesta obrađujemo redom od višeg prema nižem: neka je već odabrano $c$ hrpa, a ostatak preostalih hrpa na tom mjestu neka je $r$. Ako je $c\ge k+1-r$, točno $k+1-r$ odabranih hrpa dobiva na tom mjestu bit $1$; inače je $c+r\le k$, pa dodatno odaberemo $r$ hrpa koje na tom mjestu imaju bit $1$, postavimo im taj bit na $0$, a prethodno odabranim hrpama postavimo taj bit na $0$. Tako broj odabranih hrpa nikad ne prelazi $k$.

### Stepenasti Nim

Stepenasti Nim (staircase Nim) nešto je složeniji: dopušta premještanje kamenčića između susjednih hrpa.

???+ abstract "Stepenasti Nim"
    Imamo $n$ hrpa kamenčića, a $i$-ta hrpa sadrži $a_i$ kamenčića. Dva igrača naizmjence igraju; u svakom potezu igrač ili uzima proizvoljan broj kamenčića s $1$. hrpe, ili premješta proizvoljan broj kamenčića s hrpe $i>1$ na $i-1$-vu hrpu, ali ne smije propustiti potez. Pobjeđuje igrač koji uzme posljednji kamenčić.

O tome vrijedi sljedeći rezultat:

???+ note "Teorem"
    Igrač na potezu gubi ako i samo ako je Nim-zbroj brojeva kamenčića na hrpama s neparnim indeksom $a_1\oplus a_3\oplus\cdots\oplus a_{n-1+(n\bmod 2)}=0$.

??? note "Dokaz"
    Kad god igrač premjesti kamenčiće s hrpe parnog indeksa na hrpu neparnog indeksa, protivnik te iste kamenčiće može premjestiti dalje na sljedeću hrpu parnog indeksa (ili ih ukloniti), pa takav potez ne utječe na poziciju hrpa neparnog indeksa. Tada se premještanje sa svake hrpe neparnog indeksa na susjednu hrpu parnog indeksa (ili uklanjanje) može promatrati kao nezavisna Nim igra s jednom hrpom. Prema rezultatu Sprague–Grundyjeva teorema o zbroju igara, vrijednost SG funkcije stepenastog Nima jest Nim-zbroj vrijednosti SG funkcije tih podigara. Odatle slijedi gornji rezultat.

### Fibonaccijev Nim

Fibonaccijev Nim sličan je Bachetovoj igri: postoji samo jedna hrpa kamenčića i broj kamenčića uzetih u jednom potezu ograničen je. Za razliku od Bachetove igre, u Fibonaccijevu Nimu ograničenje broja uzetih kamenčića dinamično je.

???+ abstract "Fibonaccijev Nim"
    Imamo jednu hrpu s ukupno $n$ kamenčića. Dva igrača naizmjence uzimaju kamenčiće. Igrač koji igra prvi nije ograničen u broju kamenčića koje uzima, ali ne smije uzeti sve kamenčiće; nakon toga broj kamenčića uzetih u jednom potezu ne smije biti veći od dvostrukog broja kamenčića uzetih u prethodnom potezu (tj. u protivnikovu potezu). Broj uzetih kamenčića nikad ne smije biti $0$. Pobjeđuje igrač koji uzme posljednji kamenčić.

O tome vrijedi sljedeći rezultat:

???+ note "Teorem"
    Na početku igre igrač na potezu gubi ako i samo ako je broj kamenčića $n$ [Fibonaccijev broj](../combinatorics/fibonacci.md).

??? note "Dokaz"
    Neka je $q$ kvota (quota), tj. najveći broj kamenčića koji se u trenutačnoj poziciji smije uzeti. Tada je u prvom potezu $q=n-1$, a u kasnijim potezima $q$ je dvostruki broj kamenčića koje je (protivnik) uzeo u prethodnom potezu. Promotrimo [Fibonaccijevo kodiranje](../combinatorics/fibonacci.md#fibonaccijevo-kodiranje) preostalog broja kamenčića $n$, tj. jedinstveni rastav broja $n$ na zbroj nesusjednih pozitivnih Fibonaccijevih brojeva. Treba dokazati da je trenutačno stanje pobjedničko ako i samo ako je $q$ veći ili jednak najmanjem Fibonaccijevu broju u rastavu broja $n$.
    
    Pobjednička strategija glasi: ako je moguće, uzmi sve preostale kamenčiće; inače uzmi najmanji Fibonaccijev broj iz rastava. Budući da je drugi najmanji Fibonaccijev broj u rastavu sigurno strogo veći od dvostrukog najmanjeg, čim u pobjedničkom stanju u trenutačnom potezu ne možemo uzeti sve kamenčiće, protivnik u sljedećem potezu ne može uzeti ni drugi najmanji Fibonaccijev broj (tj. najmanji Fibonaccijev broj u sljedećem potezu), pa je protivnik sigurno u gubitničkom stanju.
    
    Obratno, ako smo trenutačno u gubitničkom stanju, neka je $k$ broj kamenčića koje sada uzimamo; on je sigurno strogo manji od najmanjeg Fibonaccijeva broja $F$ u trenutačnom rastavu. Pretpostavimo da je najmanji Fibonaccijev broj u sljedećem potezu $F'$; on je sigurno i najmanji Fibonaccijev broj u rastavu broja $F - k$. Ako je $F'\le 2$, tada iz $k\ge 1$ slijedi da je kvota u sljedećem potezu $2k\ge 2\ge F'$, pa je to već pobjedničko stanje. Inače neka je $F'=F''+F'''$ uz $F''>F'''$, tj. $F''',F'',F'$ tri su susjedna člana Fibonaccijeva niza. Ako je $k<F''$, tada pri računanju $k + (F-k)$ u Fibonaccijevu kodiranju nema prijenosa, pa se prirodno ne može dobiti $F$. Zato sigurno vrijedi $k\ge F''$. To pokazuje da je kvota u sljedećem potezu $2k>F''+F'''=F'$, pa je to pobjedničko stanje.

### Wythoffova igra

Wythoffova igra dopušta istodobno uklanjanje kamenčića s više hrpa, ali zahtijeva da se sa svake hrpe ukloni jednak broj kamenčića.

???+ abstract "Wythoffova igra"
    Imamo dvije hrpe kamenčića, s $a_1$ odnosno $a_2$ kamenčića. Dva igrača naizmjence uzimaju kamenčiće s jedne ili s obje hrpe, ne smiju propustiti potez, a kad uzimaju s obje hrpe, broj uzetih kamenčića mora biti jednak. Pobjeđuje igrač koji uzme posljednji kamenčić.

O tome vrijedi sljedeći rezultat:

???+ note "Teorem"
    Bez smanjenja općenitosti neka je $a_1\le a_2$; tada igrač na potezu gubi ako i samo ako je $a_1 = \lfloor(a_2-a_1)\phi\rfloor$, gdje je $\phi=(\sqrt{5}+1)/2$ zlatni rez.

Za dokaz tog rezultata potrebna je sljedeća lema:

???+ abstract "Beattyjev niz"
    Neka je $r > 1$ iracionalan broj. Beattyjev niz koji on generira jest $\mathcal B_r = \{\lfloor kr\rfloor : k \in\mathbf N_+\}$.

???+ note "Rayleighov teorem"
    Neka su $r,s > 1$ dva iracionalna broja takva da je $\dfrac{1}{r}+\dfrac{1}{s}=1$. Tada nizovi $\mathcal B_r$ i $\mathcal B_s$ čine particiju skupa pozitivnih cijelih brojeva $\mathbf N_+$. U tom se slučaju nazivaju i komplementarnim Beattyjevim nizovima.

??? note "Dokaz"
    Neka je $\mathcal A_r=\{kr:k\in\mathbf N_+\}$. Sortirajmo elemente skupa $\mathcal A=\mathcal A_r\cup\mathcal A_s$ i dobivamo niz $\{a_i\}_{i\in\mathbf N_+}$. Dovoljno je dokazati da $i=\lfloor a_i\rfloor$ vrijedi za sve $i\in\mathbf N_+$ da bismo dobili da je $\mathcal B_r\cup\mathcal B_s$ particija skupa pozitivnih cijelih brojeva $\mathbf N_+$.
    
    Najprije dokazujemo da u nizu nema ponovljenih elemenata. Pretpostavimo suprotno: postoje $k,\ell\in\mathbf N_+$ takvi da vrijedi $kr=\ell s$. Tada je
    
    $$
    \dfrac{\ell}{k} = \dfrac{r}{s} = r - 1.
    $$
    
    No lijeva je strana jednakosti racionalan broj, a desna iracionalan – kontradikcija. Dakle brojevi u nizu međusobno su različiti.
    
    Zatim dokazujemo da skup $\mathcal A$ sadrži točno $\lfloor a_i\rfloor$ brojeva manjih ili jednakih $a_i$. Bez smanjenja općenitosti neka je $a_i\in\mathcal A_r$, tj. $a_i=kr$; prebrojimo li zasebno elemente skupova $\mathcal A_r$ i $\mathcal A_s$, dobivamo da skup $\mathcal A$ sadrži točno
    
    $$
    k + \left\lfloor\dfrac{kr}{s}\right\rfloor = k + \lfloor k(r-1)\rfloor = \lfloor kr\rfloor = \lfloor a_i\rfloor
    $$
    
    elemenata manjih ili jednakih $a_i$. Nadalje, budući da je niz $\{a_i\}$ strogo rastući, brojeva manjih ili jednakih $a_i$ ima točno $i$. Odatle slijedi $i=\lfloor a_i\rfloor$.

Iz toga se dobiva dokaz prethodnog rezultata.

??? note "Dokaz rezultata o Wythoffovoj igri"
    Za sva stanja $(a_1,a_2)$ iz teorema s $a_1 < a_2$ koja su gubitnička za igrača na potezu stavimo $k = a_2 - a_1 \in\mathbf N_+$; tada vrijedi $a_1=\lfloor k\phi\rfloor$ i $a_2=\lfloor k(\phi+1)\rfloor$. Budući da je $\phi$ zlatni rez, vrijedi $\dfrac{1}{\phi}+\dfrac{1}{\phi+1}=1$. Po Rayleighovu teoremu nizovi $\{\lfloor k\phi\rfloor\}$ i $\{\lfloor k(\phi+1)\rfloor\}$ čine particiju skupa pozitivnih cijelih brojeva $\mathbf N_+$. To zapravo znači da među svim gubitničkim stanjima $(a_1,a_2)$ s $a_1 < a_2$ komponente $a_1$ i $a_2$ poprimaju svaki pozitivni cijeli broj točno jedanput, a i njihova razlika $a_2-a_1$ poprima svaki pozitivni cijeli broj točno jedanput.
    
    Budući da u Wythoffovoj igri dopušten potez ili ostavlja jednu od komponenata nepromijenjenom, ili ostavlja razliku komponenata nepromijenjenom, iz gubitničkog stanja doista se jednim dopuštenim potezom ne može dobiti drugo gubitničko stanje. Obratno, za svako pobjedničko stanje $(a_1,a_2)$ bez smanjenja općenitosti neka je $a_1\le a_2$ i stavimo $k=a_2-a_1$. Ako je $a_1>\lfloor k\phi\rfloor$, igrač na potezu može s obje hrpe uzeti po $(a_1 - \lfloor k\phi\rfloor)$ kamenčića i prevesti poziciju u gubitničko stanje. Inače, budući da je $(a_1,a_2)$ pobjedničko stanje, vrijedi $a_1 < \lfloor k\phi\rfloor$, pa je $k\ge 1$. Prema rezultatu iz prethodnog odlomka (i gubitničkom stanju $(0,0)$) za taj $a_1$ nužno postoji jedinstveno gubitničko stanje $(a_1,a_2')$ (ovdje ne zahtijevamo $a_1\le a_2'$). Nadalje, ako je $a_1 \ge a_2'$, očito vrijedi $a_2' \le a_1 < a_2$; inače, ako je $a_1 < a_2'$, možemo uzeti $k'=a_2'-a_1$ tako da je $a_1=\lfloor k'\phi\rfloor$, a kako je i $a_1 < \lfloor k\phi\rfloor$, slijedi $k' < k$, pa je $a_2'=a_1 + k' < a_1+k = a_2$. Dakle čim je $a_1 < \lfloor k\phi\rfloor$, sigurno vrijedi $a_2' < a_2$, pa igrač na potezu treba samo s druge hrpe uzeti $(a_2-a'_2)$ kamenčića da bi poziciju preveo u gubitničko stanje.

### Igra okretanja novčića

Igre okretanja novčića (coin-turning games) također su uobičajena vrsta nepristranih kombinatornih igara.

???+ abstract "Igra okretanja novčića"
    Neka je $(S,\preceq)$ [dobro utemeljen parcijalno uređen skup](../order-theory.md), a preslikavanje $f:S\rightarrow\mathcal P\mathcal PS$ takvo da je za sve $s\in S$ skup $f(s)$ neprazan, za $T\in f(s)$ vrijedi $s\in T$ i za sve $t\in T$ vrijedi $t\preceq s$. Na svakom elementu skupa $S$ leži po jedan novčić, licem gore ili naličjem gore. Igrači naizmjence igraju: odabiru novčić $s$ okrenut licem gore i skup $T\in f(s)$ te okreću sve novčiće iz skupa $T$. Pobjeđuje igrač koji sve novčiće okrene naličjem gore.

Igra okretanja novčića zapravo je velika klasa igara. Ovisno o konkretnom izboru parcijalno uređenog skupa $S$ i preslikavanja $f$, konkretni oblik igre okretanja novčića razlikuje se. Uvjet koji preslikavanje $f$ mora zadovoljavati u opisu igre kaže da u skupu novčića $T$ koje igrač odabere okrenuti uvijek postoji novčić $s$ okrenut licem gore takav da su svi ostali elementi skupa $T$ poredani ispred $s$. To osigurava da igra završava nakon konačno mnogo poteza.

???+ example "Primjer"
    1.  Neka je $S=\{1,2,\cdots,n\}$ i $f(s)=\{\{t,s\}:t \le s\}$. To znači: imamo red od $n$ novčića, u svakom potezu okrećemo jedan novčić okrenut licem gore i možemo odabrati još jedan novčić lijevo od njega te ga okrenuti.
    2.  Neka je $S=\{1,2,\cdots,n\}$ i $f(s)=\{[t,s]:t \le s\}$. To znači: imamo red od $n$ novčića, u svakom potezu okrećemo niz uzastopnih novčića, ali najdesniji od tih novčića prije okretanja mora biti okrenut licem gore.
    3.  Neka je $S=\{1,2,\cdots,n\}^2$ i $f(s)=\{\{s\}\}$. To znači: imamo $n$ redaka i $n$ stupaca novčića, a u svakom potezu smijemo okrenuti samo jedan novčić okrenut licem gore.
    4.  Neka je $S$ skup čvorova korijenskog stabla, a $f(s)$ skup svih onih podskupova skupa čvorova na putu od vrha $s$ do korijena stabla koji sadrže sam $s$. To znači: imamo korijensko stablo, na svakom čvoru leži po jedan novčić, u svakom potezu okrećemo jedan novčić okrenut licem gore i možemo odabrati novčiće na nekoliko njegovih predaka te ih okrenuti.

Iako postoji mnogo vrsta igara okretanja novčića, pristup njihovu rješavanju jedinstven je. Za igru okretanja novčića $(S,f)$ neka je $G_s$ pozicija u kojoj je samo novčić na elementu $s$ okrenut licem gore. Te pozicije zovemo osnovnim pozicijama. Tada se svaka pozicija $G$ može promatrati kao zbroj igara koje odgovaraju tim osnovnim pozicijama. Drugim riječima, vrijedi sljedeći rezultat:

???+ note "Teorem"
    Za igru okretanja novčića $(S,f)$ i poziciju $G$ neka je $H(G)\subseteq S$ skup položaja novčića okrenutih licem gore. Tada je vrijednost SG funkcije pozicije $G$ jednaka
    
    $$
    \operatorname{SG}(G) = \bigoplus_{s\in H(G)}\operatorname{SG}(G_s).
    $$

??? note "Dokaz"
    Promotrimo srodnu igru: u poziciji $G'$ na svakom elementu skupa $S$ leži nekoliko kamenčića; u svakom potezu igrač može uzeti jedan kamenčić s mjesta $s$, odabrati skup $T\in f(s)$ i zatim na svaki element skupa $T\setminus\{s\}$ staviti po jedan kamenčić. I za takvu igru možemo definirati osnovne pozicije $G'_s$, tj. pozicije u kojima samo na mjestu $s$ leži jedan kamenčić. U takvoj je igri svaka pozicija zbroj osnovnih pozicija koje odgovaraju svim njezinim kamenčićima. Naime, ako pri stavljanju novih kamenčića svaki pridružimo uzetom kamenčiću, svaki kamenčić koji se pojavi tijekom igre možemo pridružiti nekom kamenčiću iz početne pozicije, pa se tijekovi podigara koje odgovaraju različitim kamenčićima početne pozicije međusobno ne ometaju i cijela se igra može promatrati kao zbroj tih podigara. Budući da su SG vrijednosti osnovnih pozicija koje odgovaraju kamenčićima na istom mjestu jednake, prema svojstvima xor vrijednosti slijedi da SG vrijednost pozicije $G'$ ovisi samo o parnosti brojeva kamenčića na pojedinim mjestima, a ne o konkretnim brojevima. Stoga, ako za poziciju $G'$ skup mjesta s neparnim brojem kamenčića označimo $H(G')$, analiza iz ovog odlomka može se sažeti u formulu:
    
    $$
    \operatorname{SG}(G') = \bigoplus_{s\in H(G')} \operatorname{SG}(G'_s).
    $$
    
    Stoga je u nastavku dovoljno uspostaviti ekvivalenciju igre $G'$ i igre $G$ da bi se dokazala formula iz teorema.
    
    Treba pokazati da su za poziciju $G'$ nove igre i poziciju $G$ igre okretanja novčića igre $G'$ i $G$ ekvivalentne čim su mjesta s neparnim brojem kamenčića u $G'$ jednaka mjestima novčića okrenutih licem gore u $G$. Prema lemi 2 iz odjeljka [Sprague–Grundyjeva funkcija](#spraguegrundyjeva-funkcija) to je ekvivalentno dokazu da je pozicija $G+G'$ gubitničko stanje. Pobjednička strategija drugog igrača vrlo je jednostavna: ako prvi igrač uzme kamenčić s mjesta $s$ na kojem leži više od jednog kamenčića, drugi igrač jednostavno oponaša potez prvog igrača; inače drugi igrač odabere iste $s$ i $T\in f(s)$ kao prvi igrač, ali u drugoj podigri – ako prvi igrač uzima kamenčić, drugi okreće novčiće, a ako prvi okreće novčiće, drugi uzima kamenčić. Kako god prvi igrač odigra, drugi igrač može nastaviti igrati i osigurati da se u preostaloj poziciji mjesta s neparnim brojem kamenčića podudaraju s mjestima novčića okrenutih licem gore. Tako igra nužno završava kad prvi igrač više nema dopuštenog poteza, pa prvi igrač gubi. Time je teorem dokazan.

Pomoću tog rezultata, da bismo odredili je li neka pozicija pobjednička, dovoljno je izračunati vrijednosti SG funkcije osnovnih pozicija koje odgovaraju svim novčićima okrenutim licem gore i zatim uzeti Nim-zbroj. Ni vrijednosti SG funkcije tih osnovnih pozicija nije teško izračunati, jer su njihovi sljedbenici već zadani preslikavanjem $f$, a SG vrijednosti sljedbenika mogu se računati induktivno:

$$
\operatorname{SG}(G_s) = \operatorname{mex}\limits_{T\in f(s)}\bigoplus_{t\in T\setminus\{s\}}\operatorname{SG}(G_t).
$$

To zapravo daje rekurzivnu formulu za vrijednosti SG funkcije osnovnih pozicija.

### Igra na bipartitnom grafu

Preduvjeti: [Najveće sparivanje u bipartitnom grafu](../../graph/graph-matching/bigraph-match.md)

Na kraju ovog odjeljka raspravljamo o igri na bipartitnom grafu. Iako se ta igra obično naziva igrom na bipartitnom grafu, njezin opis i dokaz rezultata ne ovise o strukturi bipartitnog grafa, pa njezin rezultat zapravo vrijedi za sve neusmjerene grafove. Međutim, najveće sparivanje u općem grafu razmjerno je složeno, pa se taj rezultat obično pojavljuje u zadacima s bipartitnim grafovima.

???+ abstract "Igra na bipartitnom grafu"
    Dva igrača naizmjence igraju. Pozicija s kojom se svaki igrač suočava sastoji se od neusmjerenog grafa $G=(V,E)$ i jednog njegova vrha $v\in V$. U potezu nekog igrača, ako je trenutačna pozicija $(G,v)$, taj igrač mora odabrati vrh $u$ susjedan vrhu $v$. Zatim se vrh $v$ i svi njemu incidentni bridovi uklanjaju iz grafa $G$ i dobiva se preostali graf $G'$. Nova je pozicija $(G',u)$ i predaje se sljedećem igraču. Ako na početku poteza nekog igrača trenutačni vrh $v$ nema susjednih vrhova u grafu (tj. ne postoji dopušten izbor), taj igrač ne može odigrati potez i zato gubi igru.

O tome vrijedi sljedeći rezultat:

???+ note "Teorem"
    Igrač na potezu pobjeđuje ako i samo ako je vrh $v$ ključni vrh najvećeg sparivanja grafa $G$, tj. ako je u svim najvećim sparivanjima grafa $G$ vrh $v$ spareni vrh.

??? note "Dokaz"
    Najprije neka je vrh $v$ ključni vrh najvećeg sparivanja grafa $G$. Neka je $M$ jedno najveće sparivanje grafa $G$. Tada prvi igrač može poziciju pomaknuti na vrh $u$ koji je u $M$ sparen s vrhom $v$. Budući da se vrh $v$ pojavljuje u svim najvećim sparivanjima grafa $G$, veličina najvećeg sparivanja preostalog grafa $G'$ najviše je $|M|-1$; štoviše, uklanjanjem brida $(u,v)$ iz $M$ dobiva se sparivanje $M'$ grafa $G'$ veličine $|M|-1$. Iz tih dviju činjenica slijedi da je $M'$ najveće sparivanje grafa $G'$. No u poziciji u kojoj se nalazi drugi igrač vrh $u$ nije spareni vrh sparivanja $M'$. Dakle drugi je igrač nužno u gubitničkom stanju.
    
    Obratno, pretpostavimo da postoji najveće sparivanje $M$ u kojem je $v$ nespareni vrh. Budući da $M$ ne sadrži vrh $v$, ono je i najveće sparivanje preostalog grafa $G'$; stoga je svako najveće sparivanje $N$ grafa $G'$ ujedno najveće sparivanje grafa $G$ koje ne sadrži vrh $v$. Vrh $u$ susjedan vrhu $v$ sigurno je spareni vrh u $N$; inače bismo brid $(u,v)$ mogli dodati u $N$ i dobiti veće sparivanje grafa $G$. To pokazuje da je $u$ ključni vrh najvećeg sparivanja grafa $G'$. Dakle, kako god prvi igrač odabrao, drugi je igrač u pobjedničkom stanju.

Algoritam za pronalaženje ključnih vrhova najvećeg sparivanja bipartitnog grafa opisan je na [stranici o najvećem sparivanju u bipartitnom grafu](../../graph/graph-matching/bigraph-match.md#ključni-vrhovi-najvećeg-sparivanja).

Osim toga, igra na bipartitnom grafu ima i varijantu:

???+ abstract "Varijanta igre na bipartitnom grafu"
    Neka je $G=(V,E)$ neusmjeren graf i neka na svakom vrhu grafa leži po jedan kamenčić. Dva igrača naizmjence uzimaju kamenčiće. Na početku igre prvi igrač može uzeti bilo koji kamenčić; u kasnijim potezima vrh s kojeg igrač uzima kamenčić mora biti susjedan vrhu s kojeg je protivnik uzeo kamenčić u prethodnom potezu. Gubi igrač koji prvi ne može uzeti kamenčić.

Očito je ta varijanta ekvivalentna tome da u prethodno opisanoj igri na bipartitnom grafu prvi igrač odabere početnu poziciju, a zatim igra na bipartitnom grafu počinje od drugog igrača. Stoga u toj varijanti prvi igrač gubi ako i samo ako je svaki vrh ključni vrh najvećeg sparivanja, tj. ako graf $G$ ima [savršeno sparivanje](../../graph/graph-matching/graph-match.md#definicija).

## Misère Nim igra

U ovom odjeljku raspravljamo o rješavanju misère Nim igre.

???+ abstract "Misère Nim igra"
    Imamo $n$ hrpa kamenčića, a $i$-ta hrpa sadrži $a_i$ kamenčića. Dva igrača naizmjence uzimaju proizvoljan broj kamenčića s proizvoljne jedne hrpe, ali ne smiju propustiti potez. Igrač koji uzme posljednji kamenčić gubi.

O tome vrijedi sljedeći rezultat:

???+ note "Teorem"
    U misère Nim igri stanje $(a_1,a_2,\cdots,a_n)$ gubitničko je stanje $\mathcal P$ ako i samo ako
    
    1.  postoji $i$ takav da je $a_i>1$ i Nim-zbroj je $a_1\oplus a_2\oplus\cdots\oplus a_n=0$, ili
    2.  za sve $i$ vrijedi $a_i\le 1$ i broj preostalih nepraznih hrpa neparan je.

??? note "Dokaz"
    Budući da je stanje bez poteza pobjedničko stanje $\mathcal N$ za igrača na potezu, induktivno se može dokazati: ako svaka hrpa ima najviše jedan kamenčić, neparan broj nepraznih hrpa odgovara gubitničkom stanju $\mathcal P$, a paran broj nepraznih hrpa odgovara pobjedničkom stanju $\mathcal N$.
    
    Zatim promotrimo slučaj u kojem neke hrpe imaju strogo više od $1$ kamenčića.
    
    Slučaj A: ako samo jedna hrpa ima strogo više od $1$ kamenčića, Nim-zbroj sigurno nije $0$. Štoviše, igrač na potezu može prijeći u poziciju u kojoj sve hrpe imaju najviše $1$ kamenčić, i to tako da upravlja parnošću broja preostalih nepraznih hrpa. Dakle to je pobjedničko stanje $\mathcal N$.
    
    Slučaj B: sada više od jedne hrpe ima strogo više od $1$ kamenčića; tada, kako god odigramo, u sljedećoj poziciji barem jedna hrpa ima strogo više od $1$ kamenčića. Po pretpostavci indukcije u sljedećoj poziciji gubitak igrača na potezu odgovara Nim-zbroju nula, a pobjeda igrača na potezu Nim-zbroju različitom od nule. To je potpuno isto kao pretpostavka indukcije za normalnu Nim igru. Stoga ponavljanjem argumenta za Nim igru dobivamo da i trenutačna pozicija zadovoljava rezultat da Nim-zbroj nula odgovara gubitničkom stanju.

## Igra na usmjerenom grafu

Nepristrane kombinatorne igre o kojima raspravljamo u ovom članku zahtijevaju da se ista pozicija ne može pojaviti dvaput i da ne postoji mogućnost neriješenog ishoda. Zato je odgovarajući graf igre uvijek usmjereni aciklički graf. U ovom odjeljku popuštamo to ograničenje i raspravljamo o tome kako na općem usmjerenom grafu za svako stanje odrediti pobjeđuje li igrač na potezu, gubi li ili je ishod neriješen.

Pravila igre na usmjerenom grafu uglavnom su ista kao u drugim nepristranim kombinatornim igrama: iz početnog stanja igrači naizmjence prelaze jedan korak duž brida usmjerenog grafa dok više nema kamo. Ovisno o tome igra li se po normalnom ili po misère pravilu, igrač koji ne može odigrati potez gubi odnosno pobjeđuje. U takvoj igri ishod svakog stanja ima tri mogućnosti: pobjeda igrača na potezu, gubitak igrača na potezu, neriješeno. Pri neriješenom ishodu igra nikad ne završava. Iako je situacija nešto složenija, [lema](#graf-igre-i-stanja) o gubitničkim i pobjedničkim stanjima i dalje vrijedi, a preostala su stanja neriješena:

-   ako stanje ima sljedbenike, pobjedničko je za igrača na potezu ako i samo ako je jedan od sljedbenika gubitničko stanje;
-   ako stanje ima sljedbenike, gubitničko je za igrača na potezu ako i samo ako su svi sljedbenici pobjednička stanja;
-   ako se stanje ne može klasificirati ni kao pobjedničko ni kao gubitničko, ono je neriješeno stanje.

Da bismo sva stanja klasificirali u te tri vrste, dovoljno je primijeniti pristup sličan [topološkom sortiranju](../../graph/topo.md):

1.  Pri inicijalizaciji zabilježimo izlazne stupnjeve svih stanja, sva stanja s izlaznim stupnjem nula stavimo u red i, ovisno o tome igra li se po normalnom ili po misère pravilu, označimo ih kao gubitnička odnosno pobjednička stanja.
2.  Izbacimo stanje s početka reda. Ako je gubitničko, sve njegove još neodređene prethodnike označimo kao pobjednička stanja; inače je trenutačno stanje pobjedničko, pa svim njegovim prethodnicima smanjimo izlazni stupanj za jedan i prethodnike s izlaznim stupnjem nula označimo kao gubitnička stanja. Prethodnike za koje se može odrediti jesu li pobjednički ili gubitnički stavimo u red.
3.  Algoritam završava kad se red isprazni. Stanja koja još nisu određena kao pobjednička ili gubitnička sva su neriješena stanja.

Taj algoritam klasificira sva stanja u vremenu $O(|V|+|E|)$.

## Primjeri zadataka

U ovom odjeljku raspravljamo o nekoliko tipičnih primjera zadataka.

???+ example "[Luogu P2148 \[SDOI2009\] E&D](https://www.luogu.com.cn/problem/P2148)"
    Imamo $2n$ hrpa kamenčića. Za $k=1,2,\cdots,n$ hrpe $2k-1$ i $2k$ čine jednu skupinu. Dva igrača naizmjence igraju; u svakom potezu igrač odabire jednu skupinu hrpa, uklanja jednu hrpu iz nje, a drugu hrpu dijeli na dvije neprazne hrpe i stavlja ih na dva mjesta te skupine. Ako sve hrpe imaju samo po jedan kamenčić, igrač na potezu nema dopuštenog poteza i gubi igru. Za zadane brojeve kamenčića na hrpama $\{a_i\}_{i=1}^{2n}$ treba odrediti je li to pobjedničko stanje za igrača na potezu.

??? note "Rješenje"
    Očito su igre u različitim skupinama hrpa međusobno nezavisne, pa je dovoljno izračunati vrijednost SG funkcije igre za svaku skupinu da bismo izračunali SG vrijednost cijele igre i tako odredili je li stanje pobjedničko. Ključno je pitanje kako izračunati vrijednost SG funkcije pojedine skupine hrpa. To nije jednostavno. Uobičajen pristup takvim zadacima iz teorije igara jest tabliranje. Neka je $f(i,j)$ SG vrijednost skupine hrpa s redom $(i,j)$ kamenčića. Napišemo li program koji grubom silom ispisuje tablicu, dobivamo sljedeći rezultat:
    
    ```text
    0 1 0 2 0 1 0 3 0 1 0 2 0 1 0 4 
    1 1 2 2 1 1 3 3 1 1 2 2 1 1 4 4
    0 2 0 2 0 3 0 3 0 2 0 2 0 4 0 4
    2 2 2 2 3 3 3 3 2 2 2 2 4 4 4 4
    0 1 0 3 0 1 0 3 0 1 0 4 0 1 0 4
    1 1 3 3 1 1 3 3 1 1 4 4 1 1 4 4
    0 3 0 3 0 3 0 3 0 4 0 4 0 4 0 4
    3 3 3 3 3 3 3 3 4 4 4 4 4 4 4 4
    0 1 0 2 0 1 0 4 0 1 0 2 0 1 0 4
    1 1 2 2 1 1 4 4 1 1 2 2 1 1 4 4
    0 2 0 2 0 4 0 4 0 2 0 2 0 4 0 4
    2 2 2 2 4 4 4 4 2 2 2 2 4 4 4 4
    0 1 0 4 0 1 0 4 0 1 0 4 0 1 0 4
    1 1 4 4 1 1 4 4 1 1 4 4 1 1 4 4
    0 4 0 4 0 4 0 4 0 4 0 4 0 4 0 4
    4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
    ```
    
    Ta je tablica vrlo pravilna. Jednostavno opažanje: tablica se dijeli na nekoliko matrica $2\times 2$, u gornjem lijevom kutu uvijek je $0$, a ostale su tri vrijednosti uvijek jednake. Stoga tablicu možemo sažeti tako da svaku matricu $2\times 2$ zamijenimo onom zajedničkom vrijednošću izvan gornjeg lijevog kuta:
    
    ```text
    1 2 1 3 1 2 1 4 
    2 2 3 3 2 2 4 4 
    1 3 1 3 1 4 1 4 
    3 3 3 3 4 4 4 4 
    1 2 1 4 1 2 1 4 
    2 2 4 4 2 2 4 4 
    1 4 1 4 1 4 1 4 
    4 4 4 4 4 4 4 4 
    ```
    
    Može se uočiti da je ta sažeta tablica jednaka vrijednostima na istim mjestima prethodne potpune tablice uvećanima za jedan. Time je problem zapravo riješen. Neka indeksi počinju od $0$; tada je vrijednost $g(i,j)$ na mjestu $(i,j)$ tablice zadana sljedećom rekurzivnom formulom:
    
    $$
    g(i,j) =
    \begin{cases}
    0, & \text{if }2\mid i\text{ and }2\mid j,\\
    g(\lfloor i/2\rfloor,\lfloor j/2\rfloor)+1,& \text{otherwise}.
    \end{cases}
    $$
    
    Tražena SG funkcija jest $f(i,j)=g(i-1,j-1)$. Pomoću te rekurzivne formule algoritam može izračunati vrijednost $f(i,j)$ u vremenu $O(\log\max\{i,j\})$.
    
    Naravno, jednostavnom indukcijom može se dobiti da je $g(i,j)$ zapravo najmanji broj puta koji $i$ i $j$ treba istodobno uzastopno dijeliti s $2$ da bi se dobila dva parna broja. Drugim riječima, to je broj uzastopnih $1$ na kraju bitovnog ili brojeva $i$ i $j$. Zato se ta vrijednost može izračunati i izravno pomoću `__builtin_ctz(~(i | j))`.
    
    U takvim zadacima, čim se tabliranjem i promatranjem dobije izraz za SG funkciju, on se lako dokazuje indukcijom, pa je ključ rješavanja u tome da se ti rezultati na neki način dobiju, a ne izvedu. Na primjer, kad je rezultat poznat, rekurzivna relacija iz ovog zadatka može se induktivno dokazati ovako. Neka je $S_k$ skup SG vrijednosti pozicija koje se mogu dobiti dijeljenjem $k$ kamenčića na dvije neprazne hrpe; tada je $f(i,j) = \operatorname{mex}(S_i \cup S_j)$. Stoga za $S_k$ vrijedi rekurzivna relacija:
    
    $$
    S_k = \{\operatorname{mex}(S_i \cup S_j) : i + j = k,~i,j\in\mathbf N_+\}.
    $$
    
    Treba dokazati da je $d\in S_k$ ako i samo ako je $d$-ti bit (najniži bit je $0$-ti) binarnog zapisa broja $(k-1)$ jednak $1$.
    
    Koristimo matematičku indukciju. Baza indukcije $S_1=\varnothing$ očito vrijedi. Pretpostavimo da tvrdnja vrijedi za sve pozitivne cijele brojeve manje od $k$. Tada je $d\in S_k$ ako i samo ako postoje $i,j\in\mathbf N_+$ takvi da je $i+j=k$, $d$-ti bitovi brojeva $(i-1)$ i $(j-1)$ oba su $0$ i za svaki $d' < d$ barem jedan od njih ima $d'$-ti bit jednak $1$. Očito takav rastav postoji ako i samo ako, promatramo li samo bitove $0\sim d$, tj. modulo $2^{d+1}$, vrijednost $(k-1)=(i-1)+(j-1)+1$ leži u rasponu $[2^d,2^{d+1})$. Taj je uvjet ekvivalentan tome da je $d$-ti bit broja $(k-1)$ jednak $1$. Time korak indukcije vrijedi. Izvorna je tvrdnja dokazana.

??? note "Referentni kod"
    ```cpp
    --8<-- "docs/math/code/impartial-game/impartial-game-1.cpp"
    ```

???+ example "[Luogu P5675 \[GZOI2017\] 取石子游戏 (Igra uzimanja kamenčića)](https://www.luogu.com.cn/problem/P5675)"
    Imamo $n$ hrpa kamenčića, a $i$-ta hrpa sadrži $a_i$ kamenčića. Dvoje igra Nim igru. Sada možemo proizvoljno odrediti nekoliko hrpa kamenčića kao početnu poziciju i među njima odrediti jednu hrpu s koje prvi igrač u prvom potezu mora uzeti kamenčiće, ali ne možemo odrediti broj uzetih kamenčića. Koliko ima načina određivanja takvih da prvi igrač ne može pobijediti? Podaci zadovoljavaju $n,a_i\le 200$.

??? note "Rješenje"
    Za takve zadatke treba iskoristiti rezultate o uobičajenim igrama i kombinirati ih s drugim znanjima. Pretpostavimo da je određeno da prvi igrač mora uzimati s $i$-te hrpe i da je Nim-zbroj brojeva kamenčića svih određenih hrpa $v$; tada prvi igrač ne može pobijediti ako i samo ako je $a_i \le a_i\oplus v$, tj. broj kamenčića $a_i$ na $i$-toj hrpi ne prelazi Nim-zbroj $a_i\oplus v$ brojeva kamenčića preostalih hrpa osim $i$-te. Budući da je raspon podataka vrlo malen, izravno nabrajamo hrpu određenu za prvi potez; kad nabrajamo $i$-tu hrpu, svaka se preostala hrpa odabire ili ne, a broj načina koji daju pojedini Nim-zbroj može se izračunati DP-om; na kraju zbrojimo one brojeve načina koji odgovaraju vrijednostima većima ili jednakima $a_i$.

??? note "Referentni kod"
    ```cpp
    --8<-- "docs/math/code/impartial-game/impartial-game-2.cpp"
    ```

???+ example "[Luogu P2599 \[ZJOI2009\] 取石子游戏 (Igra uzimanja kamenčića)](https://www.luogu.com.cn/problem/P2599)"
    Imamo $n$ hrpa kamenčića, a $i$-ta hrpa sadrži $a_i$ kamenčića. Dvoje naizmjence uzima kamenčiće; svaki put smije se odabrati samo jedna od dviju krajnjih hrpa, krajnje lijeve ili krajnje desne, i s nje uzeti proizvoljan broj kamenčića, ali ne smije se propustiti potez. Pobjeđuje igrač koji uzme posljednji kamenčić. Treba odrediti pobjeđuje li prvi igrač.

??? note "Rješenje"
    Budući da u ovom zadatku ne postoje međusobno nezavisne podigre, u načelu se koristi samo [lema za određivanje gubitničkih i pobjedničkih stanja](#graf-igre-i-stanja). Počnimo analizu od najjednostavnijeg slučaja. Kad je $n\le 2$, to je Nim igra. Kad je $n \ge 3$, problem postaje složen. Međutim, budući da se potez može odigrati samo na dvjema krajnjim hrpama, neka su brojevi kamenčića na njima redom $x$ i $y$. Nadalje, neka je $f(x,y)$ indikatorska funkcija pobjedničkog stanja za igrača na potezu, tj. $f(x,y)=1$ kad igrač na potezu pobjeđuje, a inače $f(x,y)=0$. Lako je uočiti da vrijednosti $f(x,y)$ zadovoljavaju rekurzivnu relaciju: $f(x,y)=0$ ako i samo ako za sve $s < x$ i $t < y$ vrijedi $f(x,t)=f(s,y)=1$. Baza rekurzije jest $x=0$ ili $y=0$; tada igra više nema $n$ hrpa i treba dodatno promotriti brojeve kamenčića na srednjim hrpama. Zato privremeno pretpostavimo da su $f(x,0)$ i $f(0,y)$ poznati i promotrimo kako iz njihovih vrijednosti izvesti sve vrijednosti $f(x,y)$. To nije teško. Promotrimo beskonačnu matricu sa skupom indeksa $\mathbf N\times\mathbf N$; računanje $f(x,y)$ odgovara upisivanju $0$ i $1$ u nju, a uvjet koji treba zadovoljiti jest da svaki redak i svaki stupac sadrže najviše jednu $0$ te da, ako se na prethodnim mjestima u istom retku i istom stupcu nije pojavila $0$, na tom mjestu mora biti $0$. Položaj $0$ u svakom retku zapravo definira funkciju iz indeksa retka $x$ u indeks stupca $y$. Nakon nekoliko jednostavnih primjera (tj. tabliranja) može se uočiti: ako je jedinstveni $x$ za koji je $f(x,0)=0$ označen $x_0$, a jedinstveni $y$ za koji je $f(0,y)=0$ označen $y_0$, tada za svaki pozitivni cijeli broj $x$ vrijednost za koju vrijedi $f(x,y)=0$ glasi
    
    $$
    y = \begin{cases}
    0, & x = x_0,\\
    x - 1, & x_0 < x \le y_0,\\
    x + 1, & y_0 \le x < x_0,\\
    x, & \text{otherwise}.
    \end{cases}
    $$
    
    Drugim riječima, dovoljno je znati $x_0$ i $y_0$ da bismo u vremenu $O(1)$ izračunali bilo koju vrijednost $f(x,y)$ i odredili je li trenutačno stanje pobjedničko za igrača na potezu. A $x_0$ i $y_0$ mogu se računati rekurzivno. Na primjer, $x_0$ je jedinstveno rješenje jednadžbe $f(x,0)=0$, no istodobno se vrijednost $f(x,0)$ može izračunati tako da uklonimo krajnje desnu hrpu i promatramo samo preostalih $n-1$ hrpa; drugim riječima, promatramo li samo prvih $n-1$ hrpa, možemo jednako tako izračunati $f_{1,n-1}(x,y)$, a tada očito vrijedi $f(x,0)=f_{1,n-1}(x,a_{n-1})$; slično, uklonimo li krajnje lijevu hrpu i izračunamo $f_{2,n}(x,y)$, dobivamo $f(0,y)=f_{2,n}(a_2,y)$. Naravno, računanje unutarnjih funkcija $f_{1,n-1}(x,y)$ i $f_{2,n}(x,y)$ ovisi o još dubljim funkcijama. To je tipičan [intervalni DP](../../dp/interval.md). Na svakoj je razini dovoljno održavati $x_0$ i $y_0$ odgovarajuće funkcije.

??? note "Referentni kod"
    ```cpp
    --8<-- "docs/math/code/impartial-game/impartial-game-3.cpp"
    ```

## Zadaci za vježbu

Najprije nekoliko osnovnih (template) zadataka. Oni su jednostavne primjene rezultata s ove stranice:

-   [Luogu P2197【模板】Nim 游戏 (Predložak: Nim igra)](https://www.luogu.com.cn/problem/P2197)
-   [Luogu P2252 \[SHOI2002\] 取石子游戏 (Igra uzimanja kamenčića)](https://www.luogu.com.cn/problem/P2252)
-   [Luogu P2594 \[ZJOI2009\] 染色游戏 (Igra bojenja)](https://www.luogu.com.cn/problem/P2594)
-   [Luogu P3185 \[HNOI2007\] 分裂游戏 (Igra dijeljenja)](https://www.luogu.com.cn/problem/P3185)
-   [Luogu P3480 \[POI 2009\] KAM-Pebbles](https://www.luogu.com.cn/problem/P3480)
-   [Luogu P4101 \[HEOI2014\] 人人尽说江南好 (Svi hvale Jiangnan)](https://www.luogu.com.cn/problem/P4101)
-   [Luogu P4279 \[SHOI2008\] 小约翰的游戏 (Igra malog Johna)](https://www.luogu.com.cn/problem/P4279)
-   [Luogu P6487 \[COCI 2010/2011 #4\] HRPA](https://www.luogu.com.cn/problem/P6487)
-   [Luogu P6560 \[SBCOI2020\] 时光的流逝 (Protjecanje vremena)](https://www.luogu.com.cn/problem/P6560)
-   [Luogu P7589 黑白棋（2021 CoE-II B）(Crno-bijele figure)](https://www.luogu.com.cn/problem/P7589)
-   [AtCoder Regular Contest 168 B - Arbitrary Nim](https://atcoder.jp/contests/arc168/tasks/arc168_b)

Zatim nekoliko zadataka koji zahtijevaju više razmišljanja ili su složeniji:

-   [Luogu P2490 \[SDOI2011\] 黑白棋 (Crno-bijele figure)](https://www.luogu.com.cn/problem/P2490)
-   [Luogu P3179 \[HAOI2015\] 数组游戏 (Igra s nizom)](https://www.luogu.com.cn/problem/P3179)
-   [Luogu P5363 \[SDOI2019\] 移动金币 (Premještanje zlatnika)](https://www.luogu.com.cn/problem/P5363)
-   [Luogu P5970 \[POI 2016\] Nim z utrudnieniem](https://www.luogu.com.cn/problem/P5970)
-   [Luogu P6791 \[SNOI2020\] 取石子 (Uzimanje kamenčića)](https://www.luogu.com.cn/problem/P6791)
-   [Luogu P7864「EVOI-RD1」摘叶子 (Branje listova)](https://www.luogu.com.cn/problem/P7864)
-   [Luogu P8347「Wdoi-6」另一侧的月 (Mjesec s druge strane)](https://www.luogu.com.cn/problem/P8347)
-   [AtCoder Grand Contest 002 E - Candy Piles](https://atcoder.jp/contests/agc002/tasks/agc002_e)
-   [AtCoder Grand Contest 010 F - Tree Game](https://atcoder.jp/contests/agc010/tasks/agc010_f)
-   [AtCoder Grand Contest 017 D - Game on Tree](https://atcoder.jp/contests/agc017/tasks/agc017_d)
-   [AtCoder Beginner Contest 278 G - Generalized Subtraction Game](https://atcoder.jp/contests/abc278/tasks/abc278_g)
-   [SPOJ COT3 - Combat on a tree](https://www.spoj.com/problems/COT3/)
-   [Codeforces 494 E. Sharti](https://codeforces.com/problemset/problem/494/E)
-   [Codeforces 1149 E. Election Promises](https://www.luogu.com.cn/problem/CF1149E)
-   [Codeforces 1451 F. Nullify The Matrix](https://codeforces.com/problemset/problem/1451/F)
-   [Codeforces 1704 F. Colouring Game](https://codeforces.com/problemset/problem/1704/F)

Na kraju nekoliko zadataka o igri na bipartitnom grafu. Budući da zahtijevaju algoritme za sparivanje u bipartitnom grafu, navodimo ih zasebno:

-   [Luogu P4136 谁能赢呢？(Tko može pobijediti?)](https://www.luogu.com.cn/problem/P4136)
-   [Luogu P4617 \[COCI 2017/2018 #5\] Planinarenje](https://www.luogu.com.cn/problem/P4617)
-   [Luogu P4055 \[JSOI2009\] 游戏 (Igra)](https://www.luogu.com.cn/problem/P4055)
-   [Luogu P1971 \[NOI2011\] 兔兔与蛋蛋游戏 (Igra Zekića i Jajića)](https://www.luogu.com.cn/problem/P1971)
-   [Codeforces 1147 F. Zigzag Game](https://codeforces.com/problemset/problem/1147/F)

## Literatura i bilješke

-   [（转载）Nim 游戏博弈（收集完全版）by exponent - 博客园 (Nim igre – teorija igara (potpuna zbirka, preneseno), exponent, cnblogs)](http://www.cnblogs.com/exponent/articles/2141477.html)
-   [\[组合游戏与博弈论\]【学习笔记】by Candy? - 博客园 (Kombinatorne igre i teorija igara – bilješke s učenja, Candy?, cnblogs)](https://www.cnblogs.com/candy99/p/6548836.html)
-   [Nim - Wikipedia](https://en.wikipedia.org/wiki/Nim)
-   [Sprague–Grundy theorem - Wikipedia](https://en.wikipedia.org/wiki/Sprague%E2%80%93Grundy_theorem)
-   [Nimber - Wikipedia](https://en.wikipedia.org/wiki/Nimber)
-   [Beatty Sequence - Wikipedia](https://en.wikipedia.org/wiki/Beatty_sequence)
-   [Games on arbitrary graphs - CP Algorithms](https://cp-algorithms.com/game_theory/games_on_graphs.html)
-   [算法学习笔记（74): 二分图博弈 by Pecco - 知乎 (Bilješke o algoritmima (74): igra na bipartitnom grafu, Pecco, Zhihu)](https://zhuanlan.zhihu.com/p/359334008)
-   Conway, John H. On numbers and games. AK Peters/CRC Press, 2000.
-   Berlekamp, Elwyn R., John H. Conway, and Richard K. Guy. Winning ways for your mathematical plays, volume 1-4. AK Peters/CRC Press, 2001-2004.

[^n-vs-p]: Nazivi „$\mathcal N$-stanje” i „$\mathcal P$-stanje” označavaju redom „sljedeći igrač pobjeđuje” (Next player wins) i „prethodni igrač pobjeđuje” (Previous player wins).

[^more-sums]: „Zbrojevi” o kojima raspravljamo u ovom članku svi su **disjunktivni zbrojevi** (disjunctive sum) uz **dugo pravilo** (long rule). To je i najčešći način kombiniranja igara. Osim njega postoje i drugi mogući načini kombiniranja igara. Za detaljnu raspravu o njima može se pogledati 14. poglavlje knjige Conway, John H. On numbers and games. AK Peters/CRC Press, 2000.
