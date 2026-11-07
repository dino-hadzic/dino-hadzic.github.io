---
title: Osnovni pojmovi
---

Ovo poglavlje kratko uvodi znanja iz apstraktne algebre. Glavni sadržaj algoritamskih natjecanja trenutačno ne ispituje izravno znanje apstraktne algebre, ali se u opisima algoritama ili u rješenjima zadataka često pojavljuju osnovni pojmovi apstraktne algebre, pa čitatelji koji vladaju osnovnim pojmovima apstraktne algebre mogu brže razumjeti neke algoritme. Stoga ovaj sadržaj nije obvezno znanje za ikojeg natjecatelja, nego je namijenjen samo onim čitateljima koje to zanima ili koji od toga mogu imati koristi. Istodobno, ovo poglavlje izbjegava preopširno i preduboko izlaganje apstraktne algebre[^oi-wiki-not-wikipedia] te se usredotočuje na osnovne pojmove i na dijelove najtješnje povezane s ostalim gradivom OI-ja. Čitatelji koji žele sustavno naučiti apstraktnu algebru trebali bi učiti iz stručnih udžbenika apstraktne algebre.

Kako bismo čitatelju bolje pomogli razumjeti što može dobiti čitanjem ovog dijela, navodimo nekoliko primjera iz algoritamskih natjecanja u kojima se može pojaviti znanje apstraktne algebre:

-   mnogi teoremi teorije brojeva i teorije polinoma posebni su slučajevi rezultata apstraktne algebre;
-   u strukturama podataka, strukture poput [segment treea](../../ds/seg.md) mogu održavati informacije koje čine monoid, a rekurzivne relacije mnogih DP problema mogu se apstrahirati u takvu strukturu monoida;
-   u kombinatorici, stroga formulacija i dokaz [Pólyina teorema prebrojavanja](../combinatorics/polya.md) zahtijevaju pojmove iz teorije grupa.

Na temelju toga, ovo se poglavlje usredotočuje na osnovno znanje koje se ne može preskočiti i na dijelove izravno povezane s tim primjenama. Za početak, ovaj članak uvodi osnovne pojmove grupe, prstena i polja.

## Grupa

Definicija grupe glasi ovako.

???+ abstract "Grupa"
    Neka je $G$ neprazan skup na kojem je zadana binarna operacija $\cdot:G\times G\rightarrow G$. Ako oni zadovoljavaju sljedeća svojstva, kažemo da je $(G,\cdot)$ **grupa** (group):
    
    1.  asocijativnost (associative property): za sve $a,b,c\in G$ vrijedi $a\cdot(b\cdot c)=(a\cdot b)\cdot c$;
    2.  postojanje neutralnog elementa: postoji $e\in G$ takav da za svaki $a\in G$ vrijedi $a\cdot e = e\cdot a = a$. Ovdje se $e$ naziva **neutralnim elementom** (identity element) grupe $G$, a također i jediničnim elementom;
    3.  postojanje inverznih elemenata: za svaki $a\in G$ postoji odgovarajući $b\in G$ takav da je $a\cdot b=b\cdot a=e$. Ovdje se $b$ naziva **inverznim elementom** (inverse element) elementa $a$.

??? info "O uvjetu zatvorenosti u definiciji"
    Ovdje binarna operacija već implicitno sadrži takozvani uvjet zatvorenosti, tj. da za sve $a,b\in G$ vrijedi $a\cdot b\in G$. Neki ga tekstovi navode zasebno.

???+ note "Osnovna svojstva grupe"
    Za grupu $(G,\cdot)$ uvijek vrijede sljedeća svojstva:
    
    1.  za svaki konačan niz $\{g_i\}_{i=1}^k\subseteq G$, rezultat umnoška $g_1\cdot g_2\cdot\cdots\cdot g_k$ ne ovisi o načinu postavljanja zagrada;
    2.  neutralni element $e$ uvijek je jedinstven;
    3.  za svaki element $a\in G$ njegov inverz $a^{-1}$ također je jedinstven;
    4.  zakon kraćenja (cancellation law): za $a,b,c\in G$, ako je $a\cdot c=b\cdot c$ ili $c\cdot a=c\cdot b$, onda je $a=b$.

Grupe su vrlo česte. Jednostavno rečeno, sve transformacije koje ne gube strukturu automatski čine grupu. Kao primjer uzmimo nekoliko uobičajenih vrsta grupa.

???+ example "Primjeri grupa"
    -   **Simetrična grupa** (symmetric group): sve [permutacije](../permutation.md) skupa $M$, tj. bijekcije s $M$ na sam $M$, čine uz kompoziciju preslikavanja grupu $S_M$. Neutralni element je identiteta, a inverzni element je inverzno preslikavanje (bijekcija nužno ima inverzno preslikavanje). Ako je skup $M$ konačan, veličine $n$, grupa se često označava i $S_n$ i naziva simetričnom grupom stupnja $n$.
    -   Grupa simetrija (symmetry group) u prostoru: za geometrijski lik, sve transformacije koje ga preslikavaju na njega samog također čine uz kompoziciju preslikavanja grupu. Ona opisuje prostornu simetriju tog geometrijskog lika. Konkretne primjere vidi u [Uobičajene grupe simetrija](../combinatorics/polya.md#uobičajene-grupe-simetrija).
    -   Aditivna grupa cijelih brojeva: skup cijelih brojeva $\mathbf Z$ uz operaciju zbrajanja $+$ čini grupu $(\mathbf Z,+)$. Neutralni element je $0$, a inverzni element je suprotni broj.
    -   Multiplikativna grupa cijelih brojeva modulo $n$ (multiplicative group of integers modulo $n$): za modul $n$, [klase kongruencije](../number-theory/basic.md#klase-kongruencije-i-sustavi-ostataka) koje odgovaraju svim cijelim brojevima relativno prostim s $n$ čine uz operaciju množenja grupu $((\mathbf Z/n\mathbf Z)^\times,\times)$. Neutralni element je $\bar 1$, a inverzni element upravo je [modularni inverz](../number-theory/inverse.md) modulo $n$ (odgovarajuća klasa kongruencije), čije postojanje jamči [Bézoutov teorem](../number-theory/bezouts.md). Konkretnu analizu strukture vidi u [Multiplikativna grupa cijelih brojeva modulo $n$](./ring-theory.md#应用整数同余类的乘法群).
    -   Opća linearna grupa (general linear group): sve invertibilne kvadratne matrice reda $n$ nad brojevnim poljem $F$ čine uz operaciju množenja grupu $GL_n(F)$. Neutralni element je jedinična matrica, a inverzni element je inverzna matrica.

Da bismo bolje razumjeli definiciju grupe, pogledajmo usporedno nekoliko primjera koji nisu grupe.

???+ example "Primjeri koji nisu grupe"
    -   Sva preslikavanja s $M$ na sebe (ne nužno bijekcije) ne čine grupu, jer preslikavanja koja nisu bijekcije nemaju inverzni element.
    -   Cijeli brojevi uz množenje ne čine grupu, jer $2$ nema multiplikativni inverz u skupu cijelih brojeva.
    -   Pozitivni cijeli brojevi uz zbrajanje također ne čine grupu, jer pozitivni cijeli brojevi nemaju neutralni element za zbrajanje.
    -   Sve klase kongruencije modulo $n$ različite od nule uz množenje često ne čine grupu. Primjerice, u $(\mathbf Z/6\mathbf Z)\setminus\{\overline 0\}$ umnožak $\overline 2\times\overline 3=\overline 0$ ne pripada tom skupu, što znači da množenje nije dobro definirana binarna operacija na tom skupu (odnosno, ne zadovoljava zatvorenost).

Katkad je potrebno razmatrati i svojstva ovakvih manje potpunih struktura. Zato se mogu definirati sljedeći pojmovi, koji su općenitiji od grupe.

???+ abstract "Polugrupa"
    Za neprazan skup $G$ i binarnu operaciju $\cdot$ na njemu, ako je ta operacija asocijativna, kažemo da je $(G,\cdot)$ **polugrupa** (semigroup).

???+ abstract "Monoid"
    Za polugrupu $(G,\cdot)$, ako u njoj još postoji i neutralni element, kažemo da je $(G,\cdot)$ **monoid** (monoid).

???+ example "Primjeri monoida i polugrupa"
    Među gornjim primjerima, $(\mathbf N_+,+)$ je polugrupa, a $(\mathbf Z,\times)$ je monoid.

Naposljetku, mnoge poznate operacije na grupama osim asocijativnosti zadovoljavaju i komutativnost. Struktura takvih grupa relativno je jednostavna; one se nazivaju Abelovim grupama, a također i komutativnim grupama.

???+ abstract "Abelova grupa"
    Za grupu $(G,\cdot)$, ako operacija $\cdot$ zadovoljava i komutativnost (commutative property), tj. ako za sve $a,b\in G$ vrijedi $a\cdot b=b\cdot a$, kažemo da je $(G,\cdot)$ **Abelova grupa** (Abelian group) ili **komutativna grupa** (commutative group).

???+ example "Primjeri Abelovih i ne-Abelovih grupa"
    -   Aditivna grupa cijelih brojeva $(\mathbf Z,+)$ jest Abelova grupa.
    -   Za $n\ge3$ simetrična grupa $S_n$ nije Abelova grupa.

To su osnovne definicije vezane uz teoriju grupa. Više o teoriji grupa vidi u [Teorija grupa](./group-theory.md) ili u odgovarajućim knjigama.

## Prsten

Definicija prstena glasi ovako.

???+ abstract "Prsten"
    Za neprazan skup $R$ i dvije binarne operacije na njemu, $+:R\times R\rightarrow R$ i $\cdot:R\times R\rightarrow R$, ako oni zadovoljavaju sljedeća svojstva, kažemo da je $(R,+,\cdot)$ **prsten** (ring):
    
    1.  $(R,+)$ čini Abelovu grupu, čiji se neutralni element označava $0$, a inverz elementa $a\in R$ u odnosu na $+$ označava se $-a$.
    2.  $(R,\cdot)$ čini polugrupu, tj. $\cdot$ je asocijativna.
    3.  Distributivnost (distributive property): za sve $a,b,c\in R$ vrijedi $a\cdot(b+c)=a\cdot b+a\cdot c$ i $(a+b)\cdot c=a\cdot c+b\cdot c$.

Radi jednostavnosti izražavanja, te se dvije binarne operacije $+$ i $\cdot$ obično nazivaju zbrajanjem i množenjem tog prstena; u skladu s tim, neutralni element zbrajanja naziva se **nula** (zero), a neutralni element množenja (ako postoji) **jedinični element** (identity). Treba paziti da ih ne pomiješamo sa zbrajanjem i množenjem u konkretnim skupovima brojeva te s prirodnim brojevima nula i jedan.

??? info "O tome zahtijeva li definicija neutralni element množenja"
    U nekim definicijama prsten nužno mora imati neutralni element množenja; nasuprot tome, oni bez neutralnog elementa množenja nazivaju se **pseudoprstenima** (rng ili pseudo-ring). Kad se s tim susretnete, treba prosuditi prema kontekstu. Wikipedija koristi upravo takvu definiciju[^ring-wiki].

Aditivna struktura prstena prilično je jednostavna, ali je multiplikativna struktura vrlo primitivna. Stoga, ako po analogiji s grupama postavimo više zahtjeva na množenje, dobivamo sljedeće srodne definicije.

???+ abstract "Prsten s jedinicom"
    Za prsten $(R,+,\cdot)$, ako ima jedinični element, tj. ako postoji neutralni element množenja, koji se označava $1$, kažemo da je $(R,+,\cdot)$ **prsten s jedinicom** (ring with identity).

???+ abstract "Tijelo"
    Za prsten s jedinicom $(R,+,\cdot)$ različit od nule, ako za svaki element $a\in R$ različit od $0$ postoji multiplikativni inverz (označava se $a^{-1}$), kažemo da je $(R,+,\cdot)$ **tijelo** (division ring).

???+ abstract "Komutativni prsten"
    Za prsten $(R,+,\cdot)$, ako je njegovo množenje komutativno, kažemo da je $(R,+,\cdot)$ **komutativni prsten** (commutative ring).

Zanimljivo je da se u definiciji tijela $0$ smatra posebnim elementom multiplikativne strukture. Razlog je to što je $0 = 0\cdot a = a\cdot 0$[^zero-multiplication]. Drugim riječima, neutralni element zbrajanja u prstenu pomnožen bilo kojim elementom daje opet sebe. Tako on prirodno ne može imati multiplikativni inverz, osim ako je on sâm neutralni element množenja. Takav je prsten jedino nul-prsten (vidi primjere dolje).

Pouka je da pri razumijevanju multiplikativne strukture općeg prstena treba ukloniti utjecaj neutralnog elementa zbrajanja i promatrati $R\setminus\{0\}$. Na temelju te zamisli imamo sljedeće definicije.

???+ abstract "Djelitelj nule"
    Za prsten $(R,+,\cdot)$, ako postoji $b\in R$, $b\ne 0$, takav da vrijedi $a\cdot b=0$ ili $b\cdot a=0$, kažemo da je element $a$ različit od nule **djelitelj nule** (zero divisor).

???+ abstract "Invertibilni element (jedinica)"
    Za prsten $(R,+,\cdot)$, ako element $a$ ima multiplikativni inverz, tj. ako postoji $b\in R$ takav da vrijedi $a\cdot b=b\cdot a=1$, kažemo da je element $a\in R$ **invertibilni element** ili **jedinica** (unit).

???+ warning "„Jedinica” i „neutralni element”"
    Nemojte miješati ta dva pojma. Kako bi se izbjegla zabuna, u dijelu o apstraktnoj algebri upotrebljavat će se naziv „invertibilni element” umjesto „jedinica”.

Djelitelj nule ne može biti invertibilni element, a invertibilni element ne može biti djelitelj nule. Međutim, element različit od nule može biti ni djelitelj nule ni invertibilni element.

Ako prsten nema djelitelja nule, to znači da je skup svih elemenata različitih od nule zatvoren na množenje, tj. $(R\setminus\{0\},\cdot)$ čini polugrupu. Nadalje, ako još zahtijevamo da to bude komutativni monoid, dobivamo definiciju integralne domene.

???+ abstract "Integralna domena"
    Za prsten $(R,+,\cdot)$ različit od nule, ako je komutativan, ima neutralni element množenja i nema djelitelja nule, nazivamo ga integralnom domenom (integral domain).

Iako elementi integralne domene ne moraju imati inverz, svojstvo da nema djelitelja nule već je dovoljno da se u integralnoj domeni uspostavi zakon kraćenja.

???+ note "Zakon kraćenja u integralnoj domeni"
    Neka integralna domena $R$ ima elemente $a,b,c\in R$ s $a\neq 0$. Ako je $ab=ac$, onda nužno vrijedi $b=c$.

Za opći prsten s jedinicom, ako promatramo samo sve njegove invertibilne elemente, također dobivamo strukturu grupe. Ona se naziva multiplikativnom grupom prstena ili grupom jedinica.

???+ abstract "Multiplikativna grupa (grupa jedinica)"
    Za prsten s jedinicom $(R,+,\cdot)$, neka je $R^\times$ skup svih invertibilnih elemenata u $R$. Tada $(R^\times,\cdot)$ čini grupu, koja se naziva **multiplikativnom grupom** (multiplicative group) prstena s jedinicom $R$, ili **grupom jedinica** (unit group).

Neki od najjednostavnijih primjera prstena su sljedeći.

???+ example "Primjeri prstena"
    -   Nul-prsten (zero ring): skup $\{0\}$ uz uobičajeno zbrajanje $+$ i množenje $\times$ čini prsten, koji se naziva nul-prstenom. To je jedini prsten sa samo jednim elementom, a također i jedini prsten u kojem su neutralni element zbrajanja i neutralni element množenja jednaki.
    -   Prsten cijelih brojeva: skup cijelih brojeva $\mathbf Z$ s uobičajeno definiranim zbrajanjem $+$ i množenjem $\times$ čini prsten $(\mathbf Z,+,\times)$. Zapravo, to je integralna domena, ali nije tijelo.
    -   Prsten polinoma: za prsten $R$ može se nad njim definirati [prsten polinoma](./ring-theory.md#多项式环)  $R[x]$. Ako je $R$ integralna domena, onda je i taj prsten polinoma nužno integralna domena.
    -   Kvaternioni (quaternion): po analogiji s kompleksnim brojevima može se promatrati skup $\mathbf H=\{a+b\mathrm{i}+c\mathrm{j}+d\mathrm{k}:a,b,c,d\in\mathbf R\}$ i na njemu definirati zbrajanje i množenje, pri čemu množenje elemenata $\mathrm{i},\mathrm{j},\mathrm{k}$ zadovoljava
    
        $$
        \mathrm{i}^2=\mathrm{j}^2=\mathrm{k}^2=-1,\ \mathrm{i}\mathrm{j}=-\mathrm{j}\mathrm{i}=\mathrm{k},\ \mathrm{j}\mathrm{k}=-\mathrm{k}\mathrm{j}=\mathrm{i},\ \mathrm{k}\mathrm{i}=-\mathrm{i}\mathrm{k}=\mathrm{j}.
        $$
    
        Tada se može provjeriti da $\mathbf H$ čini prsten, i to nekomutativno tijelo.
    -   Podskup $2\mathbf Z$ skupa cijelih brojeva uz uobičajeno zbrajanje i množenje čini prsten; on je komutativan prsten bez djelitelja nule, ali nema jedinični element.
    -   Klase kongruencije cijelih brojeva modulo $n$, $\mathbf Z/n\mathbf Z$, uz zbrajanje i množenje klasa kongruencije čine prsten; on je komutativan prsten s jedinicom (tj. $\bar 1$). Takav prsten ima djelitelje nule ako i samo ako je $n$ složen broj. Stoga je za prost $n$ prsten $(\mathbf Z/n\mathbf Z, +,\times)$ integralna domena; štoviše, tada je on i tijelo, pa zapravo čini polje. Njegova multiplikativna grupa $((\mathbf Z/n\mathbf Z)^\times,\times)$ upravo je multiplikativna grupa cijelih brojeva modulo $n$.
    -   Prsten matrica: sve kvadratne matrice reda $n$ nad prstenom $R$ uz zbrajanje i množenje matrica čine prsten $M_n(R)$. Općenito, taj prsten ima djelitelje nule i nije komutativan.
    -   Za skup svih podskupova $\mathcal P(A)$ nekog skupa $A$, ako simetričnu razliku skupova $\triangle$ definiramo kao zbrajanje, a presjek $\cap$ kao množenje, onda $(\mathcal P(A),\triangle,\cap)$ čini prsten. Općenito, taj prsten ima jedinični element, ima djelitelje nule i komutativan je.

Naravno, rasprava o strukturi prstena daleko nadilazi ovo; za više sadržaja vidi [Teorija prstena](./ring-theory.md) ili odgovarajuće knjige.

## Polje

Polje je algebarska struktura s jačim svojstvima od prstena. Konkretno, polje je komutativno tijelo. Naravno, može se napisati i njegova potpuna definicija.

???+ abstract "Polje"
    Za neprazan skup $F$ i dvije binarne operacije na njemu, $+:F\times F\rightarrow F$ i $\cdot:F\times F\rightarrow F$, ako oni zadovoljavaju sljedeća svojstva, kažemo da je $(F,+,\cdot)$ **polje** (field):
    
    1.  $(F,+)$ čini Abelovu grupu, čiji se neutralni element označava $0$, a inverz elementa $a\in F$ u odnosu na $+$ označava se $-a$.
    2.  $(F\setminus\{0\},\cdot)$ čini Abelovu grupu, čiji se neutralni element označava $1$, a inverz elementa $a\in F\setminus\{0\}$ u odnosu na $\cdot$ označava se $a^{-1}$.
    3.  Distributivnost: za sve $a,b,c\in F$ vrijedi $a\cdot(b+c)=a\cdot b+a\cdot c$.

Drugim riječima, polje je algebarska struktura zatvorena na sve četiri osnovne računske operacije: zbrajanje, oduzimanje, množenje i dijeljenje.

Uobičajeni primjeri polja su sljedeći.

???+ example "Primjeri polja"
    -   Brojevna polja: skup racionalnih brojeva $\mathbf Q$, skup realnih brojeva $\mathbf R$ i skup kompleksnih brojeva $\mathbf C$ uz uobičajeno zbrajanje i množenje čine polja.
    -   Konačno polje (finite field): skup klasa kongruencije cijelih brojeva modulo prost broj $p$, $\mathbf Z/p\mathbf Z$, uz zbrajanje i množenje klasa kongruencije čini polje. Naravno, osim njih postoje i druga konačna polja; njihova je struktura jednoznačno određena njihovom veličinom, a veličina je nužno oblika potencije prostog broja.
    -   **Polje razlomaka** (fraction field): neka je $(R,+,\cdot)$ integralna domena. Može se promatrati skup $Q$ elemenata oblika $ab^{-1}$. Strogo govoreći, na skupu $R\times(R\setminus\{0\})$ definiramo relaciju ekvivalencije: $(a_1,b_1)\sim(a_2,b_2)$ ako i samo ako je $a_1b_2=a_2b_1$. Tada je skup $Q$ skup klasa ekvivalencije te relacije, $R\times(R\setminus\{0\})/\sim$, pri čemu se klasa ekvivalencije koja sadrži $(a,b)$ označava $ab^{-1}$. Ako na njemu definiramo operacije
    
        $$
        \begin{aligned}
        a_1b_1^{-1}+a_2b_2^{-1} &= (a_1\cdot b_2+a_2\cdot b_1)(b_1\cdot b_2)^{-1},\\
        (a_1b_1^{-1})\cdot(a_2b_2^{-1}) &= (a_1\cdot a_2)(b_1\cdot b_2)^{-1}
        \end{aligned}
        $$
    
        onda $(Q,+,\cdot)$ čini polje, koje se naziva poljem razlomaka integralne domene $R$. Primjerice, polje racionalnih brojeva $(\mathbf Q,+,\times)$ polje je razlomaka prstena cijelih brojeva $(\mathbf Z,+,\times)$.
    -   Kvadratno polje (quadratic field): nastaje proširenjem polja racionalnih brojeva $\mathbf Q$ dodavanjem $\sqrt d$, gdje je $d\neq 0,1$ bez kvadratnih faktora. Više o tome vidi u [Kvadratno polje](../number-theory/quadratic.md).

U usporedbi s prstenima, polja imaju vrlo jednostavnu aditivnu i multiplikativnu strukturu. Stoga je struktura samog polja često vrlo jednostavna. Zbog toga se proučavanje polja uvelike razlikuje od proučavanja prstena: obično se umjesto toga proučavaju proširenja polja i pripadna Galoisova teorija. Na algoritamskim natjecanjima katkad je potrebno računati u proširenjima polja racionalnih brojeva ili konačnih polja. Sadržaj iz teorije polja vidi u [Teorija polja](./field-theory.md) ili u odgovarajućim knjigama.

## Primjene

Na kraju, na primjeru sljedećeg zadatka pokazujemo kako apstraktni algebarski objekti pomažu u analizi konkretnih problema.

???+ note "[【模板】„动态 DP”& 动态树分治（加强版）(Predložak: „dinamički DP” i dinamička dekompozicija stabla, pojačana verzija)](https://www.luogu.com.cn/problem/P4751)"
    Zadano je stablo veličine $n$ s težinama vrhova; izvodi se $m$ izmjena težina vrhova. Nakon svake izmjene treba ispisati zbroj težina najvećeg težinskog nezavisnog skupa na stablu. Zadatak je prisilno online.

???+ note "Analiza ideje"
    Ovaj je zadatak predložak za dinamički DP; implementacija ispravne složenosti zahtijeva [globalno balansirano binarno stablo](../../ds/global-bst.md), a konkretan primjer koda nalazi se na odgovarajućoj stranici. Ovdje samo u kontekstu tog zadatka analiziramo postupak modeliranja.
    
    Da bismo istaknuli bitno, ovdje zasad ne razmatramo obradu strukture stabla globalnim balansiranim binarnim stablom, nego promatramo DP problem najvećeg težinskog nezavisnog skupa na lancu. Redom promatramo svaki vrh na lancu $[1,n]$; vrh $i$ može se odabrati ($1$) ili ne odabrati ($0$). Neka je optimalno rješenje potproblema na $[1,i]$ u tim dvama slučajevima redom $f_{i,1}$ i $f_{i,0}$. Tako se može napisati DP jednadžba
    
    $$
    \begin{aligned}
    f_{i,1}&=w_{i}+f_{i-1,0},\\
    f_{i,0}&=\max\{f_{i-1,1},f_{i-1,0}\}.
    \end{aligned}
    $$
    
    Početne su vrijednosti $(f_{0,1},f_{0,0})=(0,0)$, a konačni je odgovor $\max\{f_{n,1},f_{n,0}\}$. Da bismo prikazali utjecaj vrha $i$ na konačni rezultat, dovoljno je primijetiti da se ta rekurzivna relacija može zapisati kao
    
    $$
    (f_{i,1},f_{i,0})=g(f_{i-1,1},f_{i-1,0};w_i).
    $$
    
    To je niz preslikavanja s $\mathbf R^2$ u $\mathbf R^2$ koja $(f_{i-1,1},f_{i-1,0})$ preslikavaju u $(f_{i,1},f_{i,0})$; jezikom grupa, te transformacije uz kompoziciju preslikavanja čine monoid. Upravo to segment tree može održavati.
    
    Međutim, ako takve parametrizirane transformacije $g(\cdot;w_i)$ nemaju posebnu strukturu, opće preslikavanje s $\mathbf R^2$ u $\mathbf R^2$ nemoguće je opisati konačnodimenzionalnim podacima. Ovdje je potrebno još jedno opažanje: ako na $\mathbf R\cup\{-\infty\}$ definiramo $\max$ kao zbrajanje, a $+$ kao množenje, onda $\mathbf R\cup\{-\infty\}$ čini strukturu nalik prstenu, pri čemu je $-\infty$ neutralni element zbrajanja, a $0$ neutralni element množenja. No to nije prsten, jer njegovi elementi nemaju svi aditivni inverz. Takva se struktura naziva poluprstenom[^semiring], a poluprsten $(\mathbf R\cup\{-\infty\},\max,+)$ koji se ovdje pojavljuje naziva se **tropskim poluprstenom** (tropical semiring).
    
    Na temelju tropskog poluprstena $(R,\oplus,\otimes)$ može se definirati množenje matrica nad njim. Naime, za matricu $A=(a_{ij})$ dimenzija $m\times n$ i matricu $B=(b_{jk})$ dimenzija $n\times p$ može se definirati njihov umnožak $AB$ kao $(c_{ik})$, čiji je svaki element jednak
    
    $$
    c_{ik} = \bigoplus_{j=1}^n(a_{ij}\otimes b_{jk}) = \max_{1\le j\le n}\;(a_{ij}+b_{jk}).
    $$
    
    S tim oznakama gornja se rekurzivna relacija može shvatiti kao linearna transformacija nad tropskim poluprstenom i matričnim jezikom zapisati kao
    
    $$
    \left(\begin{matrix}f_{i,1}\\f_{i,0}\end{matrix}\right)
    =\left(\begin{matrix}-\infty&w_i\\0&0\end{matrix}\right)\left(\begin{matrix}f_{i-1,1}\\f_{i-1,0}\end{matrix}\right).
    $$
    
    Stoga, dovoljno je segment treeom održavati umnožak tih matrica nad tropskim poluprstenom da bi se odgovorilo na problem dinamičkog DP-a na lancu s više izmjena.
    
    Vratimo se sada na verziju problema na stablu. Za vrh $i$ stabla, skup njegove djece označimo $S(i)$; tada DP jednadžba na tom mjestu glasi
    
    $$
    \begin{aligned}
    f_{i,1}&=w_i+\sum_{j\in S(i)}f_{j,0},\\
    f_{i,0}&=\sum_{j\in S(i)}\max\{f_{j,1},f_{j,0}\}.
    \end{aligned}
    $$
    
    Najprije heavy-light dekompozicijom problem svodimo na verziju na lancu. Neka je $h$ teško dijete vrha $i$; tada se gornja rekurzivna jednadžba može zapisati kao
    
    $$
    \begin{aligned}
    f_{i,1}&=w_i+f_{h,0}+g_{i,1},\\
    f_{i,0}&=\max\{f_{h,0},f_{h,1}\}+g_{i,0},
    \end{aligned}
    $$
    
    gdje
    
    $$
    \begin{aligned}
    g_{i,1}&=\sum_{j\in S(i),\ j\neq h}f_{j,0},\\
    g_{i,0}&=\sum_{j\in S(i),\ j\neq h}\max\{f_{j,1},f_{j,0}\}
    \end{aligned}
    $$
    
    sažimaju doprinos lake djece. Prema gore opisanom, sve se te transformacije mogu zapisati u matričnom obliku nad tropskim poluprstenom, pa se i cijeli problem može održavati segment treeom nad heavy-light dekompozicijom. Međutim, jedna izmjena izravno s heavy-light dekompozicijom i segment treeom košta $O(\log^2n)$, pa je potrebno gore spomenuto globalno balansirano binarno stablo kojim se to optimizira na $O(\log n)$; naravno, može se održavati i LCT-om.
    
    Ovdje spomenuti tropski poluprsten i gornje matrične operacije zapravo nisu rijetki. Ako u gornjem tekstu $\max$ zamijenimo s $\min$, odgovarajući se tropski poluprsten često koristi u problemima najkraćih putova. Ako kvadratna matrica $A$ reda $n$ daje (najmanje) težine bridova između parova vrhova nekog grafa s $n$ vrhova, onda je element na mjestu $(i,j)$ matrice $A^k$ najkraća udaljenost od vrha $i$ do vrha $j$ koristeći najviše $k$ bridova; posebno, $A^n$ upravo je matrica udaljenosti tog grafa. Naravno, u stvarnoj implementaciji ta se potencija matrice ne računa doslovno grubom silom, nego se koristi Floydov algoritam složenosti $O(n^3)$.

## Literatura i napomene

-   Dummit, D.S. and Foote, R.M. (2004) Abstract Algebra. 3rd Edition, John Wiley & Sons, Inc.
-   [Tropical semiring - Wikipedia](https://en.wikipedia.org/wiki/Tropical_semiring)

[^oi-wiki-not-wikipedia]: Jer [OI Wiki nije enciklopedija](../../intro/what-oi-wiki-is-not.md#oi-wiki-nije-enciklopedija).

[^ring-wiki]: [Ring (mathematics) - Wikipedia](https://en.wikipedia.org/wiki/Ring_%28mathematics%29)

[^zero-multiplication]: Izvod te jednakosti glasi $0\cdot a+0 = 0\cdot a = (0+0)\cdot a = 0\cdot a + 0\cdot a$, pri čemu prva i druga jednakost slijede iz definicije neutralnog elementa zbrajanja, treća iz distributivnosti, a završna implikacija iz zakona kraćenja za zbrajanje. Množenje s druge strane analogno je.

[^semiring]: Poluprsten (semiring) algebarska je struktura koja se dobiva kad se u definiciji prstena s jedinicom izostavi zahtjev da za zbrajanje nužno postoje inverzi, tj. aditivna je struktura komutativni monoid, a multiplikativna struktura monoid. Više informacija vidi na [Wikipediji](https://en.wikipedia.org/wiki/Semiring).
