---
title: Teorija prstena
---

Predznanje: [Osnovni pojmovi apstraktne algebre](./basic.md), [Teorija grupa](./group-theory.md)

## Uvod

**Teorija prstena** (ring theory) proučava najrazličitije prstene.

Sadržaj teorije prstena obrađen u ovom članku neraskidivo je povezan s teorijom djeljivosti iz teorije brojeva. Najprije, analogno normalnim podgrupama iz teorije grupa, uvodimo jezgru homomorfizma prstena, koja se naziva idealom prstena; to je zapravo poopćenje pojma broja iz teorije brojeva na opće prstene. Zatim, poopćavanjem pojmova iz prstena cijelih brojeva – prostih brojeva, Euklidova algoritma, rastava na proste faktore itd. – na opće prstene dobivamo pojmove različitih vrsta integralnih domena.

Mnogi rezultati iz teorije brojeva i dalje vrijede u drugim uobičajenim prstenima. Može se reći da se dio teorije prstena bavi upravo pitanjem vrijede li ti rezultati iz teorije brojeva i u općim prstenima; ako ne vrijede, kakva ograničenja treba nametnuti prstenu da bi vrijedili.

???+ info "Oznake"
    Kad to ne dovodi do zabune, u ovom ćemo članku izostavljati znak množenja u prstenu, a prsten $(R,+,\cdot)$ pisat ćemo kao prsten $R$. U prstenu $R$ neutralni element zbrajanja naziva se i nulom i označava s $0$; neutralni element množenja naziva se i jedinicom (jediničnim elementom) i označava s $1$.

??? warning "Definicija prstena u ovom članku ne zahtijeva jedinicu"
    Napominjemo da definicija prstena u ovom članku ne zahtijeva postojanje jedinice. Neki tekstovi u definiciji prstena zahtijevaju jedinicu; tada formulacije nekih rezultata iz ovog članka treba malo prilagoditi. Primjerice, u ovom se članku ideal može definirati preko potprstena, dok ga u drugim tekstovima može biti potrebno definirati preko aditivne podgrupe.

## Ideali

Analogno slučaju grupa, mogu se uvesti pojmovi potprstena i homomorfizma prstena.

???+ abstract "Potprsten"
    Za prsten $(R,+,\cdot)$ i njegov podskup $S$, ako je i $(S,+,\cdot)$ prsten, kažemo da je $S$ **potprsten** (subring) prstena $R$.

???+ example "Primjer: prsten cijelih brojeva $\mathbf Z$"
    Za svaki cijeli broj $n$ skup $n\mathbf Z=\{nk:k\in\mathbf Z\}$ potprsten je prstena $\mathbf Z$.

???+ abstract "Homomorfizam prstena"
    Za prstene $(R,+,\cdot)$ i $(S,\oplus,\odot)$, ako preslikavanje $\pi$ čuva zbrajanje i množenje prstena, tj. ako za sve $r_1,r_2\in R$ vrijedi $\pi(r_1+r_2)=\pi(r_1)\oplus\pi(r_2)$ i $\pi(r_1\cdot r_2)=\pi(r_1)\odot\pi(r_2)$, kažemo da je preslikavanje $\pi:R\rightarrow S$ **homomorfizam** (homomorphism) iz prstena $R$ u prsten $S$.

??? info "Slučaj kad definicija prstena zahtijeva jedinicu"
    Ako definicija prstena zahtijeva postojanje jedinice, onda se u definiciji homomorfizma prstena često zahtijeva i da se jedinica preslikava u jedinicu. Za homomorfizme između nenul prstena s jedinicom taj dodatni zahtjev samo osigurava da homomorfizam ne preslikava cijeli prsten s jedinicom u nulu.

???+ example "Primjer: prsten cijelih brojeva $\mathbf Z$ (nastavak)"
    Preslikavanje redukcije modulo proizvoljan nenul cijeli broj $n$, tj. $\pi:\mathbf Z\rightarrow\mathbf Z/n\mathbf Z$, gdje je $\pi(a)=\bar a$, homomorfizam je prstena.

[Rasprava](./group-theory.md#homomorfizmi-grupa) o jezgri i slici homomorfizma grupa može se gotovo doslovno prenijeti ovamo. (Relativna) veličina slike homomorfizma određuje je li homomorfizam surjekcija, a trivijalnost jezgre homomorfizma određuje je li homomorfizam injekcija. Jezgra homomorfizma prstena definira se ovako:

???+ abstract "Jezgra homomorfizma"
    **Jezgra** (kernel) homomorfizma $\pi:R\rightarrow S$ iz prstena $R$ u prsten $S$ skup je $\{r\in R:\pi(r)=0\}$, u oznaci $\ker\pi$, gdje je $0$ neutralni element zbrajanja u $S$.

Očito su jezgra i slika homomorfizma prstena potprsteni. Obratno, nije svaki potprsten jezgra nekog homomorfizma prstena. Potprsteni koji mogu biti jezgra homomorfizma prstena nazivaju se idealima prstena.

???+ abstract "Ideal"
    Za prsten $R$ i njegov potprsten $I$ kažemo da je $I$ u prstenu $R$
    
    -   **lijevi ideal** (left ideal) ako za sve $r\in R$ vrijedi $rI\subseteq I$, gdje je $rI=\{ra:a\in I\}$;
    -   **desni ideal** (right ideal) ako za sve $r\in R$ vrijedi $Ir\subseteq I$, gdje je $Ir=\{ar:a\in I\}$;
    -   **ideal** (ideal) ako je $I$ i lijevi ideal prstena $R$ i desni ideal prstena $R$.

Ovdje se zahtijeva da ideal $I$ bude zatvoren i na množenje slijeva i na množenje zdesna elementima prstena $R$. Taj je uvjet prirodan. Naime, elementi ideala u homomorfizmu prstena preslikavaju se u nulu, a umnožak bilo kojeg elementa s nulom, bilo slijeva bilo zdesna, trebao bi biti jednak nuli; to je upravo tražena zatvorenost. Osim toga, budući da je aditivna struktura prstena Abelova grupa, svaka je podgrupa normalna; multiplikativna je struktura prstena pak vrlo rudimentarna i ne nameće podstrukturama dodatna ograničenja. To pokazuje da je uvjet zatvorenosti na množenje slijeva i zdesna ujedno i dovoljan.

???+ example "Primjer: prsten cijelih brojeva $\mathbf Z$ (nastavak)"
    Kao primjer, prije spomenuti potprsten $n\mathbf Z$ zapravo je ideal prstena $\mathbf Z$. To je skup svih višekratnika broja $n$. Umnožak višekratnika broja $n$ s bilo kojim cijelim brojem opet je višekratnik broja $n$. Zapravo su svi ideali prstena $\mathbf Z$ tog oblika; takav se prsten naziva [prstenom glavnih ideala](#prsteni-glavnih-ideala). U općem prstenu neki ideali nisu skup višekratnika nekog elementa; postojanje takvih općih prstena upravo je bilo prvotni poticaj za proučavanje ideala (a ne jednostavno višekratnika)[^ideal-history].

### Kvocijentni prsten

Kao i kod grupa, na temelju ideala prstena može se na skupu svih susjednih klasa (u smislu aditivne grupe) definirati **kvocijentni prsten** (quotient ring). Promotrimo skup

$$
R/I=\{a+I:a\in R\},
$$

gdje je susjedna klasa $a+I=\{a+b:b\in I\}$. Može se dokazati da su, ako i samo ako je $I$ ideal, operacije

$$
\begin{aligned}
(a+I)+(b+I)&=(a+b)+I,\\
(a+I)(b+I)&=(ab)+I
\end{aligned}
$$

dobro definirane, tj. da rezultat tih operacija ne ovisi o izboru predstavnika susjednih klasa. Uz te operacije $R/I$ čini prsten. Opet u skladu sa slučajem grupa, može se dokazati **prvi teorem o izomorfizmu** (first isomorphism theorem) za prstene te postoji prirodni homomorfizam prstena u njegov kvocijentni prsten. To pokazuje da ideali prstena i normalne podgrupe grupa igraju istu ulogu u homomorfizmima odgovarajućih struktura.

???+ note "Prvi teorem o izomorfizmu"
    Neka je $\pi:R\rightarrow S$ homomorfizam iz prstena $R$ u prsten $S$. Tada je $\ker\pi$ ideal prstena $R$, a $R/\ker\pi\cong\pi(R)$ potprsten je prstena $S$.

???+ abstract "Prirodni homomorfizam"
    Za prsten $R$ i njegov ideal $I$ preslikavanje $\pi:R\rightarrow R/I$ zadano s $\pi(r)=r+I$ surjektivni je homomorfizam iz $R$ u $R/I$ i naziva se **prirodnim homomorfizmom** (natural homomorphism) iz prstena $R$ u kvocijentni prsten $R/I$.

???+ example "Primjer: prsten cijelih brojeva $\mathbf Z$ (nastavak)"
    Kao primjer, prsten $\mathbf Z/n\mathbf Z$ klasa kongruencije cijelih brojeva modulo $n$ kvocijentni je prsten prstena $\mathbf Z$ po njegovu idealu $n\mathbf Z$. To ujedno objašnjava značenje oznake $\mathbf Z/n\mathbf Z$. Gore spomenuto preslikavanje modulo $n$, $\pi:\mathbf Z\rightarrow\mathbf Z/n\mathbf Z$, upravo je ovdje spomenuto prirodno preslikavanje, a odgovarajuća jezgra upravo je ideal $n\mathbf Z$.

U slučaju prstena vrijede i ostali teoremi o izomorfizmu.

???+ note "Drugi teorem o izomorfizmu"
    Neka prsten $R$ ima potprsten $A$ i ideal $B$. Tada je $A+B=\{a+b:a\in A,b\in B\}$ također potprsten prstena $R$, $A\cap B$ je ideal prstena $A$, $B$ je ideal prstena $A+B$ i vrijedi $(A+B)/B\cong A/(A\cap B)$.

???+ note "Treći teorem o izomorfizmu"
    Neka prsten $R$ ima ideale $I,J$ takve da je $I\subseteq J$. Tada je $J/I$ također ideal prstena $R/I$ i vrijedi $(R/I)/(J/I)\cong R/J$.

???+ note "Teorem o korespondenciji"
    Neka prsten $R$ ima ideal $I$. Tada između skupa svih potprstena prstena $R$ koji sadrže $I$, $\mathcal S=\{S:I\subseteq S\subseteq R\}$, i skupa svih potprstena kvocijentnog prstena $R/I$, $\mathcal T=\{T:T\text{ is a subring of }R/I\}$, postoji bijekcija $\varphi:\mathcal S\rightarrow\mathcal T$ koja $S\in\mathcal S$ preslikava u $S/I\in\mathcal T$. Ta bijekcija čuva relaciju sadržavanja među potprstenima, a ideali prstena $R$ uvijek se preslikavaju u ideale prstena $R/I$.

Ti će teoremi igrati temeljnu ulogu u daljnjoj raspravi o strukturi prstena i ideala.

### Operacije s idealima

Na idealima prstena mogu se definirati razne operacije. To je slično tome što se na strukturi djeljivosti cijelih brojeva mogu definirati pojmovi poput najvećeg zajedničkog djelitelja i najmanjeg zajedničkog višekratnika.

???+ abstract "Operacije s idealima"
    Neka prsten $R$ ima ideale $I,J$. Mogu se definirati sljedeće operacije:
    
    -   **zbroj** (sum) ideala: $I+J=\{a+b:a\in I,b\in J\}$;
    -   **umnožak** (product) ideala: $IJ=\{\sum_{i=1}^na_ib_i:a_i\in I,b_i\in J\}$, tj. skup svih konačnih zbrojeva umnožaka oblika $ab$;
    -   **presjek** (intersection) ideala: $I\cap J$.

Lako se provjeri da su rezultati tih operacija opet ideali prstena.

???+ example "Primjer: prsten cijelih brojeva $\mathbf Z$ (nastavak)"
    Promotrimo slučaj prstena cijelih brojeva $\mathbf Z$. Za ideale $n\mathbf Z$ i $m\mathbf Z$ dobivamo
    
    $$
    \begin{aligned}
    n\mathbf Z+m\mathbf Z&=\gcd(m,n)\mathbf Z,\\
    (n\mathbf Z)(m\mathbf Z)&=(mn)\mathbf Z,\\
    (n\mathbf Z)\cap(m\mathbf Z)&=\mathrm{lcm}(m,n)\mathbf Z.
    \end{aligned}
    $$

Općenito, za prsten $R$ i njegove ideale $I$ i $J$ uvijek vrijedi

$$
IJ\subseteq I\cap J\subseteq I,J\subseteq I+J.
$$

Pomoću tih definicija kineski teorem o ostatcima za cijele brojeve može se poopćiti na opće prstene. No prije toga treba na opće prstene poopćiti još i pojmove poput prostog broja i relativne prostosti.

### Maksimalni ideali

Preko strukture ideala prstena mogu se razumjeti svojstva prstena.

Nenul prsten $R$ uvijek ima dva trivijalna ideala, $\{0\}$ i $R$. Ako je prsten $R$ k tome komutativan nenul prsten s jedinicom, onda je prsten koji ima samo ta dva ideala nužno polje, i obratno[^simple-ring].

???+ note "Teorem"
    Neka je $R$ komutativan nenul prsten s jedinicom. Tada je $R$ polje ako i samo ako $R$ ima samo trivijalne ideale $\{0\}$ i $R$.

??? note "Dokaz"
    Ako je $R$ polje, onda za svaki nenul ideal $I$ možemo uzeti proizvoljan nenul element $a\in I$; tada za svaki element polja $r\in R$ vrijedi $r=(ra^{-1})a\in (ra^{-1})I\subseteq I$, pa je $I=R$. Obratno, za svaki $a\in R$ takav da je $a\neq 0$ može se provjeriti da je $aR=\{ar:r\in R\}$ ideal, koji je nužno jednak $R$, pa postoji $b\in R$ takav da je $ab=1$; to pokazuje da $a$ ima inverz, pa je $R$ polje.

Uvjet komutativnosti prstena ovdje je nužan; inače bi, da bi prsten bio tijelo, trebalo zahtijevati da su i lijevi i desni ideali trivijalni.

Ovaj se rezultat može poopćiti na slučaj kad sam prsten nije polje. No tada umjesto toga treba promatrati kvocijentne prstene i raspraviti uvjete uz koje je kvocijentni prsten komutativnog nenul prstena s jedinicom polje. Da je kvocijentni prsten $R/I$ polje znači da kvocijentni prsten $R/I$ ima samo trivijalne ideale, a prema teoremu o korespondenciji to znači da u izvornom prstenu $R$ ne postoji ideal strogo između ideala $I$ po kojem se kvocijentira i izvornog prstena $R$. Takav ideal $I$ naziva se maksimalnim idealom.

???+ abstract "Maksimalni ideal"
    Za prsten $R$ i njegov ideal $M$, ako je $M\neq R$ i ako su jedini ideali prstena $R$ koji sadrže $M$ upravo $M$ i $R$, kažemo da je ideal $M$ **maksimalni ideal** (maximal ideal).

???+ note "Teorem"
    Neka komutativan nenul prsten s jedinicom $R$ ima ideal $M$. Tada je kvocijentni prsten $R/M$ polje ako i samo ako je $M$ maksimalni ideal.

???+ example "Primjer: prsten cijelih brojeva $\mathbf Z$ (nastavak)"
    Na primjer, ideal $n\mathbf Z$ prstena cijelih brojeva $\mathbf Z$ maksimalan je ako i samo ako je $n$ prost broj. Za prost broj $p$ kvocijentni prsten $\mathbf Z/p\mathbf Z$ polje je, koje se označava i s $\mathbf F_p$.

Nema svaki prsten maksimalni ideal, ali nenul prsten s jedinicom uvijek ima maksimalni ideal.

???+ note "Teorem (Krull)"
    Za ideal $I\neq R$ nenul prstena s jedinicom $R$ uvijek postoji maksimalni ideal $M$ prstena $R$ takav da vrijedi $I\subseteq M$.

??? note "Dokaz"
    Ideja je iskoristiti Zornovu lemu. Promotrimo skup $\mathcal S$ svih pravih ideala prstena $R$ (tj. ideala različitih od $R$) koji sadrže $I$. Budući da je $I\in\mathcal S$, taj je skup neprazan i s obzirom na relaciju sadržavanja čini parcijalno uređen skup. Za svaki lanac $J_0\subseteq J_1\subseteq\cdots\subseteq J_n\subseteq\cdots$ u njemu neka je $J$ njihova unija; lako se provjeri da je i to ideal. Štoviše, $J\neq R$, jer bi inače bilo $1\in J$, tj. postojao bi $n$ takav da je $1\in J_n$, što je u suprotnosti s time da je $J_n$ pravi ideal. Stoga prema Zornovoj lemi postoji maksimalni ideal $M\supseteq I$.

Maksimalni ideal analogon je ireducibilnog elementa iz teorije djeljivosti. Naime, relacija sadržavanja među idealima odgovara relaciji djeljivosti među cijelim brojevima; nepostojanje ideala koji bi bio nadskup odgovara nepostojanju faktora koji bi ga dijelio. No pojam maksimalnog ideala širi je od pojma ireducibilnog elementa, jer nisu svi ideali glavni.

### Prosti ideali

Uvjet da je nešto polje stroži je od uvjeta da je integralna domena. Ideali koji osiguravaju da je kvocijentni prsten integralna domena nazivaju se prostim idealima; oni su analogon pojma prostog broja iz teorije djeljivosti.

???+ abstract "Prosti ideal"
    Za komutativan prsten $R$ i njegov ideal $P$, ako je $P\neq R$ i ako za proizvoljne elemente prstena $a,b\in R$ iz $ab\in P$ uvijek slijedi $a\in P$ ili $b\in P$, kažemo da je ideal $P$ **prosti ideal** (prime ideal).

Ta definicija na prvi pogled djeluje pomalo neočekivano, ali u usporedbi s [definicijom prostog broja](../number-theory/basic.md#osnovni-teorem-aritmetike) i ova je definicija prostog ideala prirodna.

???+ note "Teorem"
    Neka komutativan nenul prsten s jedinicom $R$ ima ideal $P$. Tada je kvocijentni prsten $R/P$ integralna domena ako i samo ako je $P$ prosti ideal.

??? note "Dokaz"
    Za komutativan nenul prsten s jedinicom $R$ kvocijentni prsten $R/P$ integralna je domena ako i samo ako $R/P$ nema djelitelja nule. Označimo susjednu klasu $a+P$ s $\bar a$. Da kvocijentni prsten $R/P$ nema djelitelja nule ekvivalentno je tome da iz $\bar a\bar b=\bar 0$ uvijek slijedi $\bar a=\bar 0$ ili $\bar b=\bar 0$. Prema definiciji kvocijentnog prstena to je ekvivalentno tome da iz $ab\in P$ uvijek slijedi $a\in P$ ili $b\in P$.

U prstenu cijelih brojeva $\mathbf Z$ ideal $n\mathbf Z$ maksimalan je ako i samo ako je $n$ prost broj, a $n\mathbf Z$ prost je ideal ako i samo ako je $n$ prost broj ili $n=0$. U općem komutativnom prstenu maksimalni ideal uvijek je i prost, dok obrat, naravno, ne mora vrijediti; to se vidi iz svojstava odgovarajućih kvocijentnih prstena.

???+ note "Teorem"
    Neka je $R$ komutativan nenul prsten s jedinicom. Tada je svaki njegov maksimalni ideal nužno prosti ideal.

Uskoro ćemo vidjeti da obrat vrijedi samo u prstenima s dovoljno dobrim svojstvima, dovoljno sličnima prstenu cijelih brojeva.

### Glavni ideali

Analogno pojmu podgrupe, i u raspravi o prstenima često treba promatrati ideal generiran nekim podskupom.

???+ abstract "Ideal generiran podskupom"
    Za nenul prsten s jedinicom $R$ i njegov neprazan podskup $A\subseteq R$, ako je $I$ (s obzirom na relaciju sadržavanja) najmanji među idealima prstena $R$ koji sadrže $A$, ideal $I$ naziva se **idealom generiranim podskupom $A$** (ideal generated by a subset) i označava s $(A)$. Tada se $A$ naziva **generirajućim skupom** (generating set) ideala $(A)$.

???+ abstract "Glavni ideal"
    Ideal generiran jednim elementom $a\in R$ naziva se **glavnim idealom** (principal ideal) i označava s $(a)$. Tada se $a$ naziva **generatorom** (generator) ideala $(a)$.

Za skup $A$ može se dati konstrukcija ideala koji on generira. Najprije definiramo

$$
\begin{aligned}
RA&=\{r_1a_1+\cdots+r_na_n:r_i\in R,a_i\in A,n\in\mathbf N_+\},\\
AR&=\{a_1r_1+\cdots+a_nr_n:r_i\in R,a_i\in A,n\in\mathbf N_+\}.
\end{aligned}
$$

To su zapravo lijevi odnosno desni ideal generiran skupom $A$. Tada je ideal generiran podskupom $A$ upravo $RAR$. Za komutativne prstene sve su tako definirane strukture jednake.

Svi ideali $n\mathbf Z$ prstena cijelih brojeva glavni su ideali; u nastavku ih često označavamo s $(n)$.

## Integralne domene

Integralna domena komutativan je nenul prsten s jedinicom i bez djelitelja nule. Taj je pojam upravo poopćenje prstena cijelih brojeva. No tako dobiveni prsten ne mora imati dovoljno dobra svojstva da bi se svaki rezultat teorije djeljivosti cijelih brojeva mogao doslovno prenijeti. Da bi se rezultati iz teorije brojeva mogli poopćiti, na integralnu domenu mogu se nametnuti dodatna ograničenja. Tri su najčešće vrste integralnih domena Euklidovi prsteni, prsteni glavnih ideala i faktorijalni prsteni; svaki je od tih pojmova strogo sadržan u sljedećem.

### Relacija djeljivosti

Najprije ovdje poopćavamo odgovarajuće pojmove iz teorije djeljivosti cijelih brojeva na opće komutativne prstene.

???+ abstract "Djeljivost"
    Neka komutativan prsten $R$ ima elemente $a,b\in R$. Ako postoji $x\in R$ takav da je $a=bx$, kažemo da $b$ **dijeli** (divide) $a$ i pišemo $b\mid a$. Tada kažemo da je $b$ **djelitelj** (divisor) elementa $a$.

???+ abstract "Asociranost"
    Neka komutativan prsten $R$ ima elemente $a,b\in R$. Ako se oni razlikuju samo za invertibilni element, tj. ako postoji invertibilni element $u\in R$ takav da je $a=bu$, kažemo da su $a$ i $b$ **asocirani** (associate).

Relacija djeljivosti relacija je [parcijalnog uređaja](../order-theory.md#binarna-relacija) na prstenu, a relacija asociranosti relacija je ekvivalencije na prstenu. Gledano preko ideala, $a\mid b$ ekvivalentno je s $(b)\subseteq (a)$, a asociranost elemenata $a$ i $b$ ekvivalentna je s $(a)=(b)$. Stoga se pri raspravi o elementima prstena obično ne obazire na razliku među asociranim elementima. Slično kao kod cijelih brojeva, najveći zajednički djelitelj elemenata $a$ i $b$ komutativnog prstena definira se kao infimum skupa $\{a,b\}$.

???+ abstract "Najveći zajednički djelitelj"
    Za komutativan prsten $R$ i njegove elemente $a,b\in R$, ako postoji nenul element $d\in R$ koji zadovoljava $d\mid a$ i $d\mid b$ te za svaki $d'$ koji zadovoljava $d'\mid a$ i $d'\mid b$ vrijedi $d'\mid d$, kažemo da je $d$ **najveći zajednički djelitelj** (greatest common divisor) elemenata $a$ i $b$ i pišemo $\gcd(a,b)$.

U integralnoj domeni najveći zajednički djelitelj jednoznačno je određen do na asociranost. Daljnja je rasprava ograničena na integralne domene.

U integralnoj domeni može se uvesti i pojam sličan prostom broju. U teoriji cijelih brojeva postoje dvije ekvivalentne definicije prostog broja, ali u općoj integralnoj domeni te dvije definicije odgovaraju različitim pojmovima:

???+ abstract "Prosti element"
    Neka integralna domena $R$ ima nenul element $p\in R$. Ako je $(p)$ prosti ideal, tj. ako $p$ nije invertibilan i iz $p\mid ab$ uvijek slijedi $p\mid a$ ili $p\mid b$, kažemo da je $p$ **prosti element** (prime).

???+ abstract "Ireducibilni element"
    Neka integralna domena $R$ ima nenul element $r\in R$. Ako $r$ nije invertibilan i ako za sve $a,b\in R$ takve da je $r=ab$ vrijedi da je $a$ ili $b$ invertibilan, kažemo da je $r$ **ireducibilni element** (irreducible) ili da je $r$ ireducibilan. Obratno, ako je $r=ab$ i $a,b\in R$ nisu invertibilni, kažemo da je $r$ reducibilan.

Može se pokazati da je glavni ideal $(r)$ koji odgovara ireducibilnom elementu $r$ nužno maksimalan među svim pravim glavnim idealima prstena; no u općoj integralnoj domeni nisu svi ideali glavni, pa pojmovi ireducibilnog elementa i maksimalnog ideala nisu ekvivalentni.

Analogno dokazu da je u prstenu glavnih ideala svaki prosti ideal maksimalan, općenito se može dokazati sljedeći rezultat:

???+ note "Teorem"
    Neka je $R$ integralna domena. Ako je $a\in R$ prosti element, onda je $a$ nužno i ireducibilni element.

??? note "Dokaz"
    Neka je $r\in R$ prosti element i neka $a,b\in R$ zadovoljavaju $r=ab$. Budući da je $r$ prost, bez smanjenja općenitosti neka vrijedi $r\mid a$; tada je $a=cr=cba$. Budući da u integralnoj domeni vrijedi zakon kraćenja, imamo $1=bc$, pa $b$ ima inverz $c$. To pokazuje da je $r$ ireducibilan.

Obrat ne vrijedi.

??? example "Protuprimjer"
    U prstenu kvadratnih cijelih brojeva $\mathbf Z[\sqrt{-5}]$ element $3$ ireducibilan je, ali $9=3\cdot 3=(2+\sqrt{-5})(2-\sqrt{-5})$, pa on nije prost.
    
    Ovdje dajemo dokaz tog protuprimjera; čitatelji koji nisu upoznati s prstenima kvadratnih cijelih brojeva neka najprije pročitaju odjeljak [Prsteni kvadratnih cijelih brojeva](#primjer-prsteni-kvadratnih-cijelih-brojeva). Neka je $N(\cdot)$ norma na prstenu kvadratnih cijelih brojeva. Za svaki rastav $3=ab$ vrijedi $N(a)N(b)=N(3)=9$. Ako $a,b$ nisu invertibilni, onda su $N(a)$ i $N(b)$ veći od $1$, pa nužno vrijedi $N(a)=N(b)=3$. No u $\mathbf Z[\sqrt{-5}]$ nema takvih elemenata, tj. $x^2+5y^2=3$ nema cjelobrojnih rješenja. To pokazuje da je $3$ ireducibilan. Što se tiče toga da $3$ nije prost, treba dokazati da $3$ ne dijeli $2\pm\sqrt{-5}$, što je očito.

### Euklidovi prsteni

Povezano štivo: [(Prošireni) Euklidov algoritam](../number-theory/gcd.md), [Bézoutov teorem](../number-theory/bezouts.md)

Euklidov prsten integralna je domena u kojoj se može provoditi uzastopno dijeljenje s ostatkom (tj. Euklidov algoritam).

???+ abstract "Euklidov prsten"
    Za integralnu domenu $R$, ako postoji preslikavanje $N:R\setminus\{0\}\rightarrow\mathbf N$ takvo da za sve $a,b\in R$ uz $b\neq 0$ postoje $q,r\in R$ za koje vrijedi $a=qb+r$ te $r=0$ ili $N(r)<N(b)$, kažemo da je integralna domena $R$ **Euklidov prsten** (Euclidean domain, ED). Preslikavanje $N$ naziva se normom (norm) elemenata Euklidova prstena.

??? info "Druge ekvivalentne definicije"
    Definicija usvojena u ovom članku definira normu samo na nenul elementima. Različiti tekstovi mogu različito pristupati definiciji Euklidova prstena. Primjerice, neki tekstovi mogu dodatno definirati $N(0)=0$; no u dijeljenju s ostatkom koje slijedi vrijednost $N(0)$ ne koristi se, pa to nije bitno. Nadalje, definicija na [Wikipediji](https://en.wikipedia.org/wiki/Euclidean_domain) zahtijeva i da norma $N$ zadovoljava svojstvo: za sve nenul $a,b\in R$ vrijedi $N(a)\le N(ab)$. No lako se provjeri da, ako Euklidov prsten $R$ ima normu $N(\cdot)$ koja zadovoljava svojstvo iz definicije u ovom članku, onda se može definirati norma $N'(a)=\min_{b\in R\setminus\{0\}} N(ab)$ koja zadovoljava i dodatno svojstvo $N'(a)\le N'(ab)$. Stoga su sve te različite definicije ekvivalentne.

Ta je definicija zapravo poopćenje dijeljenja s ostatkom cijelih brojeva. Postojanje norme omogućuje usporedbu relativne veličine ostatka i djelitelja. Tako se pri uzastopnom dijeljenju norma odgovarajućih ostataka stalno smanjuje; budući da norma poprima vrijednosti u prirodnim brojevima, takav postupak nužno završava s $r=0$. Tako dobivamo Euklidov algoritam u Euklidovu prstenu.

Mogućnost provođenja Euklidova algoritma znači da se u Euklidovu prstenu najveći zajednički djelitelj može učinkovito izračunati. Potpuno analogno teoriji djeljivosti cijelih brojeva može se dokazati da je rezultat Euklidova algoritma nužno najveći zajednički djelitelj te da vrijedi Bézoutov teorem, pri čemu se koeficijenti u njemu mogu odrediti proširenim Euklidovim algoritmom.

???+ note "Teorem"
    Za Euklidov prsten $R$ i njegove elemente $a,b\in R$ rezultat $d$ Euklidova algoritma primijenjenog na $a$ i $b$ najveći je zajednički djelitelj elemenata $a$ i $b$ te postoje $x,y\in R$ takvi da vrijedi $d=ax+by$; obratno, svaki element oblika $ax+by$ višekratnik je elementa $d$.

Uočimo da su, u jeziku teorije prstena, svi elementi oblika $ax+by$ upravo elementi ideala $(a,b)$, a taj teorem kaže da je $(a,b)$ nužno glavni ideal $(d)$.

Zapravo je svaki ideal Euklidova prstena glavni.

???+ note "Teorem"
    Svaki ideal Euklidova prstena glavni je ideal.

??? note "Dokaz"
    Neka je $R$ Euklidov prsten i $I$ njegov ideal. Ako je $I=\{0\}$, on je očito glavni. Neka je $I$ nenul ideal. Prema definiciji na prstenu $R$ postoji norma $N(\cdot)$, pa možemo uzeti nenul element $d$ iz $I$ s najmanjom normom. Tada za svaki $a\in I$ vrijedi $a=qd+r$ uz $r=0$ ili $N(r)< N(d)$. Budući da je $r=a-qd\in I$, iz načina na koji je izabran $d$ slijedi $r=0$, tj. $a=qd\in (d)$. To pokazuje da je $I$ nužno glavni ideal.

### Prsteni glavnih ideala

Integralna domena u kojoj su svi ideali glavni naziva se prstenom glavnih ideala. To je vrsta integralnih domena s vrlo dobrim svojstvima, a ujedno i vrlo česta. U tim je integralnim domenama pojam ideala prstena istovjetan pojmu višekratnika kod cijelih brojeva.

???+ abstract "Prsten glavnih ideala"
    Za integralnu domenu $R$, ako je svaki njezin ideal glavni, kažemo da je ona **prsten glavnih ideala** (principal ideal domain, PID).

Stoga se posljednji teorem prethodnog odjeljka može iskazati ovako:

???+ note "Teorem"
    Svaki Euklidov prsten ujedno je prsten glavnih ideala.

U prstenu glavnih ideala maksimalni ideali upravo su ideali generirani ireducibilnim elementima. Slično kao što su kod cijelih brojeva prosti brojevi i ireducibilni elementi ekvivalentni, u prstenu glavnih ideala ta su dva pojma također ekvivalentna, pa su i maksimalni i prosti ideali potpuno ekvivalentni.

???+ note "Teorem"
    Neka prsten glavnih ideala $R$ ima nenul ideal $I$. Tada je $I$ prosti ideal ako i samo ako je $I$ maksimalni ideal.

??? note "Dokaz"
    Dovoljno je dokazati da je svaki prosti ideal maksimalan. Neka prsten glavnih ideala $R$ ima nenul prosti ideal $(p)$ i ujedno ideal $(a)$ takav da je $(p)\subseteq(a)\subseteq R$. To znači da $a\mid p$, pa postoji $b\in R$ takav da je $p=ab$. No budući da je $(p)$ prosti ideal, iz $ab\in(p)$ slijedi $a\in(p)$ ili $b\in(p)$. Ako je $a\in(p)$, onda je $(a)\subseteq (p)$, pa je $(a)=(p)$; ako je $b\in(p)$, onda je $b=cp$, pa je $p=acp$, a budući da je $p\neq 0$, imamo $1=ac$, tj. $a$ ima inverz $c$, pa je $(a)=R$. To pokazuje da je $(p)$ maksimalni ideal.

???+ note "Korolar"
    Neka prsten glavnih ideala $R$ ima nenul element $r$. Tada je $r$ prosti element ako i samo ako je $r$ ireducibilni element.

Analiza Bézoutova teorema iz prethodnog odjeljka može se prenijeti na prstene glavnih ideala.

???+ note "Teorem"
    Neka je $R$ prsten glavnih ideala i neka su $a,b\in R$ nenul elementi. Neka je $d\in R$ generator ideala $(a,b)$. Tada je $d$ najveći zajednički djelitelj elemenata $a$ i $b$, jedinstven do na asociranost; štoviše, postoje $x,y\in R$ takvi da vrijedi $ax+by=d$.

Drugim riječima, u prstenu glavnih ideala i dalje vrijedi [Bézoutov teorem](../number-theory/bezouts.md). Iako najveći zajednički djelitelj postoji u oba slučaja, najveća je razlika između Euklidova prstena i prstena glavnih ideala u tome što se u prvome najveći zajednički djelitelj može učinkovito izračunati Euklidovim algoritmom, dok u prstenu glavnih ideala općenito nema takva učinkovitog algoritma.

### Faktorijalni prsteni

Pojam općenitiji od prstena glavnih ideala jest faktorijalni prsten. Teorem o jedinstvenom rastavu cijelih brojeva naziva se [osnovnim teoremom aritmetike](../number-theory/basic.md#osnovni-teorem-aritmetike). Sličan teorem o jedinstvenom rastavu zapravo vrijedi i u nekim integralnim domenama koje nisu prsteni glavnih ideala. Takve integralne domene nazivaju se faktorijalnim prstenima.

???+ abstract "Faktorijalni prsten"
    Za integralnu domenu $R$, ako se svaki nenul i neinvertibilan element $r$ može zapisati u obliku $r=p_1\cdots p_n$, gdje su $p_1,\cdots,p_n$ ireducibilni elementi koji se mogu ponavljati, i ako je takav rastav jedinstven do na asociranost i poredak, kažemo da je integralna domena $R$ **faktorijalni prsten** (unique factorization domain, UFD).

Osnovni teorem aritmetike kaže da je prsten cijelih brojeva $\mathbf Z$ faktorijalni prsten.

Prije smo dali protuprimjer ireducibilnog elementa koji nije prost; u integralnoj domeni $\mathbf Z[\sqrt{-5}]$ koja se u njemu pojavljuje teorem o jedinstvenom rastavu više ne vrijedi. No u svim faktorijalnim prstenima ireducibilni i prosti elementi ekvivalentni su.

???+ note "Teorem"
    Za faktorijalni prsten $R$ i njegov nenul element $a\in R$, $a$ je prosti element ako i samo ako je $a$ ireducibilni element.

??? note "Dokaz"
    Dovoljno je dokazati da je svaki ireducibilni element prost. Za ireducibilni element $r$, ako $r\mid ab$, onda postoji $c\in R$ takav da vrijedi $ab=rc$. Budući da je $R$ faktorijalni prsten, $a,b,c\in R$ mogu se rastaviti na umnožak ireducibilnih elemenata. Usporedbom lijeve i desne strane, iz jedinstvenosti rastava slijedi da je $r$ nužno asociran s nekim ireducibilnim faktorom elementa $a$ ili $b$, pa $r$ dijeli jedan od elemenata $a$ i $b$. To pokazuje da je $r$ i prost.

Svaki prsten glavnih ideala faktorijalni je prsten.

???+ note "Teorem"
    Svaki prsten glavnih ideala faktorijalni je prsten.

??? note "Dokaz"
    Neka je $R$ prsten glavnih ideala i neka $r\in R$ nije ni nula ni invertibilan. Da bismo pokazali da se $r$ može jedinstveno rastaviti na umnožak niza ireducibilnih elemenata, postupamo u dva koraka: najprije dokazujemo postojanje rastava, a zatim njegovu jedinstvenost.
    
    Postojanje rastava prilično je prirodno. Ako je $r$ već ireducibilan, nema ga potrebe dalje rastavljati; inače nužno postoje $r_1,r_2$ takvi da je $r=r_1r_2$ i da $r_1,r_2$ nisu invertibilni. Dalje, ako su i $r_1$ i $r_2$ ireducibilni, također nema potrebe dalje rastavljati; inače se onaj od $r_1$ i $r_2$ koji nije ireducibilan može dalje rastaviti, pa se $r$ može zapisati kao umnožak više elemenata. Dakle, dok god u umnošku nisu svi faktori ireducibilni, postupak rastavljanja može se nastaviti. Rastavljanje nužno završava nakon konačno mnogo koraka. U protivnom aksiom izbora jamči da se iz $R$ može izdvojiti beskonačan lanac elemenata $\{r_{(i)}\}_{i=0}^\infty$ takav da je $r_{(0)}=r$ i da $r_{(i+1)}\mid r_{(i)}$ vrijedi za sve $i\in\mathbf N$, pri čemu su sve te relacije djeljivosti stroge, tj. u lancu nema asociranih elemenata. U jeziku ideala to odgovara strogo rastućem beskonačnom nizu ideala $I_{0}\subset I_{1}\subset \cdots\subset I_{i}\subset\cdots\subset R$, gdje je $I_i=(r_{(i)})$. Lako se provjeri da je unija tih ideala $I=\bigcup_{i=0}^\infty I_i$ opet ideal, pa je nužno glavni. Neka je $a$ generator glavnog ideala $I$; tada postoji $n\in\mathbf N$ takav da je $a\in I_n$. Stoga je $I=(a)\subseteq I_n$. To pokazuje da takav strogo rastući beskonačan niz ideala ne postoji, pa gornji postupak rastavljanja nužno završava u konačno mnogo koraka.
    
    Zatim dokazujemo jedinstvenost rastava. Možemo provesti indukciju po broju faktora u rastavu. Ključni korak indukcije jest provjeriti da, ako je $r=p_1p_2\cdots p_n=q_1q_2\cdots q_m$ i $n\le m$, onda je $p_1$ nužno asociran s nekim $q_j$. Ovdje treba iskoristiti prethodni rezultat: u prstenu glavnih ideala svaki je ireducibilni element prost. Znamo da je $p_1$ ireducibilni element u $R$, pa je on i prost, te se za umnožak na desnoj strani induktivno može pokazati da nužno postoji neki element $q_j$ takav da $p_1\mid q_j$. Stoga postoji $c\in R$ takav da je $q_j=p_1c$, a budući da je $q_j$ ireducibilan i $p_1$ ireducibilan, prema definiciji $c$ može biti samo invertibilan, pa je $p_1$ asociran s $q_j$. Tada se pomoću zakona kraćenja na lijevoj odnosno desnoj strani mogu pokratiti $p_1$ i $q_j$, a invertibilni element za koji se oni razlikuju pomnožiti s bilo kojim preostalim elementom. Prema pretpostavci indukcije $p_2\cdots p_n$ i $q_1\cdots q_{j-1}q_{j+1}\cdots q_m$ nužno imaju jednak broj ireducibilnih elemenata, jednakih do na asociranost. Time je teorem dokazan.

Naposljetku, postojanje najvećeg zajedničkog djelitelja vrijedi i u faktorijalnim prstenima.

???+ note "Teorem"
    Neka faktorijalni prsten $R$ ima nenul elemente $a,b\in R$ koji se mogu rastaviti u obliku $a=up_1^{r_1}\cdots p_n^{r_n}$ i $b=vp_1^{s_1}\cdots p_n^{s_n}$, gdje su $u,v$ invertibilni elementi, $p_1,\cdots,p_n$ međusobno različiti ireducibilni elementi, a $r_i,s_i$ prirodni brojevi. Tada je jedan njihov najveći zajednički djelitelj $d=p_1^{\min\{r_1,s_1\}}\cdots p_n^{\min\{r_n,s_n\}}$.

To zapravo pokazuje da je svojstvo postojanja najvećeg zajedničkog djelitelja slabije od vrijeđenja teorema o jedinstvenom rastavu[^gcd-domain].

### Primjer: prsteni kvadratnih cijelih brojeva

Povezano štivo: [Kvadratna polja](../number-theory/quadratic.md)

Razumijevanje apstraktne algebre ne može bez primjera. Upravo zato što je istraživanje velikog Fermatova teorema zahtijevalo proučavanje svojstava jedne klase algebarskih cijelih brojeva postupno se razvila današnja teorija prstena[^ring-theory-history]. Ovdje raspravljamo o najjednostavnijim algebarskim cijelim brojevima, kvadratnim cijelim brojevima. Dokazi mnogih rezultata u ovom dijelu zahtijevaju složena znanja iz algebarske teorije brojeva, pa su izostavljeni.

**Kvadratni cijeli broj** (quadratic integer) kompleksan je korijen kvadratne jednadžbe $\alpha^2+b\alpha+c=0$ s cjelobrojnim koeficijentima i vodećim koeficijentom jedan. Svi kvadratni cijeli brojevi, i samo oni, imaju oblik

$$
\alpha=a+b\omega,~(a,b\in\mathbf Z)
$$

gdje je

$$
\omega=\begin{cases}
\dfrac{1+\sqrt{D}}{2},& D\equiv 1\pmod 4,\\
\sqrt D,& D\equiv 2,3\pmod 4,
\end{cases}
$$

pri čemu $D$ nema kvadratnih faktora.

??? note "Analiza"
    Prema formuli za rješenja kvadratne jednadžbe znamo da se korijen te jednadžbe nužno može zapisati kao
    
    $$
    \alpha=\frac{-b\pm\sqrt{b^2-4c}}{2}.
    $$
    
    Kad je $b=2k+1$ neparan, taj se korijen može zapisati kao
    
    $$
    \alpha=-k-\frac{1\pm\sqrt{4(k^2+k-c)+1}}{2}.
    $$
    
    Inače, kad je $b=2k$ paran, taj se korijen može zapisati kao
    
    $$
    \alpha=-k\pm\sqrt{k^2-c}.
    $$
    
    Odatle se zaključuje da kvadratni cijeli brojevi nužno imaju gornji oblik.

Lako se provjeri da za takav $\omega$ skup $\mathbf Z[\omega]=\{a+b\omega:a,b\in\mathbf Z\}$ čini prsten. On se naziva **prstenom kvadratnih cijelih brojeva** (quadratic integer ring), a njegovo polje razlomaka upravo je kvadratno polje $\mathbf Q(\sqrt D)$. Kad je $D>0$, svi su kvadratni cijeli brojevi realni, pa se on naziva i **realnim prstenom kvadratnih cijelih brojeva**; kad je $D<0$, svi kvadratni cijeli brojevi osim cijelih brojeva kompleksni su, pa se on naziva i **imaginarnim prstenom kvadratnih cijelih brojeva**.

Svi prsteni kvadratnih cijelih brojeva $\mathbf Z[\omega]$ integralne su domene. Među njima, za $D=-1$, $\mathbf Z[\sqrt{-1}]$ (ili u oznaci $\mathbf Z[\mathrm{i}]$) naziva se i prstenom Gaussovih cijelih brojeva; za $D=-3$, $\mathbf Z\left[\dfrac{1+\sqrt{-3}}{2}\right]$ naziva se prstenom Eisensteinovih cijelih brojeva.

Za kvadratni cijeli broj $a+b\omega$ može se definirati njegov **konjugat** (conjugate) kao $a+b\bar\omega$, gdje je

$$
\bar\omega=\begin{cases}
\dfrac{1-\sqrt{D}}{2},& D\equiv 1\pmod 4,\\
-\sqrt D,& D\equiv 2,3\pmod 4,
\end{cases}
$$

Napominjemo da su za $D>0$ kvadratni cijeli brojevi realni, pa se ovaj pojam konjugata ne podudara u potpunosti s pojmom konjugata kompleksnog broja, ali su oba posebni slučajevi pojma konjugata algebarskog elementa iz teorije polja. Konjugirani kvadratni cijeli brojevi korijeni su iste kvadratne jednadžbe s cjelobrojnim koeficijentima.

Na prstenu kvadratnih cijelih brojeva može se definirati **norma**

$$
\begin{aligned}
N(a+b\omega)&=(a+b\omega)(a+b\bar\omega)\\
&=\begin{cases}
a^2+ab+\dfrac{1-D}{4}b^2,& D\equiv 1\pmod 4,\\
a^2-Db^2,& D\equiv 2,3\pmod 4.
\end{cases}
\end{aligned}
$$

Norma kvadratnog cijelog broja uvijek je cijeli broj. Posebno, za $D<0$ norma je uvijek prirodan broj. Norma čuva multiplikativnu strukturu, tj. $N(ab)=N(a)N(b)$.

Invertibilni elementi (jedinice) prstena kvadratnih cijelih brojeva upravo su oni elementi čija je norma $\pm1$. Za $D>0$ to je isto što i promatranje rješenja [Pellove jednadžbe](../number-theory/pell-equation.md) $x^2-Dy^2=\pm1$ ili $x^2-Dy^2=\pm4$. Za $D<0$ lako se provjeri da su, osim dvaju posebnih slučajeva – u prstenu Gaussovih cijelih brojeva $\mathbf Z[\rm{i}]$ invertibilni su elementi $\{\pm1,\pm\rm{i}\}$, a u prstenu Eisensteinovih cijelih brojeva $\mathbf Z[\omega]$ invertibilni su elementi $\{\pm1,\pm\omega,\pm\omega^2\}$ – u svim ostalim slučajevima invertibilni elementi samo $\{\pm1\}$.

Norma $N(\alpha)$ definirana na prstenu kvadratnih cijelih brojeva može se upotrijebiti da se dokaže da je on Euklidov prsten. Za $D>0$ kao normu iz definicije Euklidova prstena treba uzeti njezinu apsolutnu vrijednost $|N(\alpha)|$. Pomoću tako dobivene norme može se dokazati da su, za $D<0$,

$$
D=-1,-2,-3,-7,-11
$$

odnosno, za $D>0$,

$$
D=2, 3, 5, 6, 7, 11, 13, 17, 19, 21, 29, 33, 37, 41, 57, 73
$$

prsteni kvadratnih cijelih brojeva koji odgovaraju tim cijelim brojevima Euklidovi prsteni s obzirom na normu $|N(\cdot)|$. No norma iz definicije Euklidova prstena ne mora biti gore definirana norma. Primjerice, za $D=14,69$ odgovarajući prsteni kvadratnih cijelih brojeva također su Euklidovi prsteni, ali treba upotrijebiti drugu normu. Za $D<0$ može se dokazati da su gore navedeni slučajevi svi Euklidovi prsteni među prstenima kvadratnih cijelih brojeva.

Složenijim metodama može se utvrditi i je li neki prsten kvadratnih cijelih brojeva prsten glavnih ideala. Može se dokazati da su za $D<0$ samo za

$$
D=-1,-2,-3,-7,-11,-19,-43,-67,-163
$$

odgovarajući prsteni kvadratnih cijelih brojeva prsteni glavnih ideala. Usporedbom s gornjim rezultatom vidimo da slučajevi poput $D=-19$ daju primjer prstena glavnih ideala koji nije Euklidov prsten. Za $D>0$ zasad nema potpunog rezultata.

Može se, međutim, dokazati da su u prstenima kvadratnih cijelih brojeva pojmovi faktorijalnog prstena i prstena glavnih ideala ekvivalentni. Gornji rezultat pokazuje da, primjerice, $\mathbf Z[\sqrt{-5}]$ nije prsten glavnih ideala, pa stoga nije ni faktorijalni prsten. Prije smo već primjerom izravno dokazali da u njemu nema jedinstvenog rastava, tj.

$$
9=3\times3=(2+\sqrt{-5})\times(2-\sqrt{-5}).
$$

Istim se primjerom može pokazati da ni ideal $(3,2+\sqrt{-5})$ nije glavni. Uskoro ćemo vidjeti da je jednostavan primjer faktorijalnog prstena koji nije prsten glavnih ideala prsten polinoma $\mathbf Z[x]$.

Iako mnogi prsteni kvadratnih cijelih brojeva nisu faktorijalni prsteni, svi su oni [Dedekindove domene](https://en.wikipedia.org/wiki/Dedekind_domain). To znači da se svaki netrivijalni ideal u svakom prstenu kvadratnih cijelih brojeva može jedinstveno rastaviti na umnožak niza prostih ideala. No ako sam prsten kvadratnih cijelih brojeva nije prsten glavnih ideala, ti prosti idealni faktori ne odgovaraju nužno prostim elementima, pa teorem o jedinstvenom rastavu (tj. rastavu brojeva na umnožak prostih brojeva) više ne vrijedi: to je i bio prvotni poticaj za proučavanje ideala umjesto brojeva.

## Prsten polinoma

Povezano štivo: [Uvod u tehnike s polinomima](../poly/intro.md)

U algoritamskim natjecanjima često se susreću razne operacije s polinomima. Množenje, invertiranje, dijeljenje s ostatkom i druge operacije s polinomima mogu se promatrati kao poopćenje operacija s brojevima na prsten polinoma. Jezikom apstraktne algebre svojstva odgovarajućih operacija u prstenu polinoma mogu se brže razumjeti.

???+ abstract "Polinom"
    Za nenul komutativan prsten s jedinicom $R$, **polinom** (polynomial) nad $R$ formalni je zbroj
    
    $$
    \sum_{k=0}^{n}a_kx^k = a_0+a_1x+\cdots+a_{n-1}x^{n-1}+a_nx^n,
    $$
    
    gdje je $n\in\mathbf N$ i za svaki $k$ vrijedi $a_k\in R$. Ti $a_k$ nazivaju se **koeficijentima** (coefficient) polinoma, a odgovarajući $a_kx^k$ **članovima** (term) polinoma. Broj $k$ u članu $a_kx^k$ naziva se **stupnjem** (degree) tog člana.
    
    Polinom čiji su svi koeficijenti nula (tj. nulelement) naziva se **nulpolinomom** (zero polynomial) i označava s $0$. Za ostale polinome bez smanjenja općenitosti neka je $a_n\neq 0$, tj. $a_nx^n$ je član najvišeg stupnja među članovima s nenul koeficijentom. Tada se prirodan broj $n$ naziva **stupnjem** (degree) polinoma, član $a_nx^n$ u kojem se nalazi naziva se **vodećim članom** (leading term), a $a_n$ se naziva i **vodećim koeficijentom** (leading coefficient). Polinom čiji je vodeći koeficijent jednak jedan (tj. jedinici) naziva se **normiranim** (monic) polinomom. Stupanj nulpolinoma ne određuje se ili se dogovorno stavlja $-\infty$.

Simbol $x$ koji se pojavljuje u zapisu polinoma naziva se **neodređenicom** (indeterminate) polinoma. Sam po sebi nema nikakvo značenje ni područje vrijednosti. Postoji samo zato da svojim eksponentom označi položaj koeficijenta. Stoga se polinom može zapisati i kao niz nad $R$

$$
(a_0,a_1,...,a_{n-1},a_n,0,0,\cdots).
$$

No takav niz može imati samo konačno mnogo članova različitih od nule. Ako su nizovi koeficijenata dvaju polinoma jednaki, kažemo da su polinomi jednaki. To znači da su im, nakon dopunjavanja članovima s koeficijentom nula, formalni zbrojevi potpuno jednaki. U nastavku više ne razlikujemo zapise formalnih zbrojeva jednakih polinoma: po potrebi čitatelj može sam dopuniti nule koje nedostaju među koeficijentima.

Ponekad treba element prstena uvrstiti umjesto neodređenice polinoma. Primjerice, neka je $f(x)$ polinom nad $R$ i $a\in R$; rezultat uvrštavanja $a$ u polinom $f(x)$ jest $f(a)$. Njegovo je značenje: zamijenimo li u formalnom zbroju polinoma $x$ s $a$, dobivamo aritmetički izraz u $R$, a $f(a)$ je rezultat izračuna tog izraza u $R$.

??? info "„Polinom” i „polinomijalna funkcija”"
    Čitatelj ne bi smio brkati ta dva pojma. Polinom je samo konačan niz koeficijenata i ne postaje automatski funkcija. Iako ovdje opisano uvrštavanje elemenata prstena umjesto neodređenice doista preslikava polinom u polinomijalnu funkciju, to preslikavanje ne mora biti injekcija. Primjerice, $f(x)=x^p-x$ kao polinom nad poljem $\mathbf F_p$ očito nije jednak nulpolinomu; ali $f(x)$ kao polinomijalna funkcija $\mathbf F_p\rightarrow \mathbf F_p$ identički je jednak nuli (to je mali Fermatov teorem). Iako su ta dva pojma različita, mnogi se pojmovi za polinomijalne funkcije mogu poopćiti na polinome; primjerice, po uzoru na derivaciju, neodređeni integral i kompoziciju polinomijalnih funkcija mogu se definirati (formalna) [derivacija](../poly/intro.md#derivacija), [neodređeni integral](../poly/intro.md#derivacija), [kompozicija](../poly/intro.md#kompozicija) itd. polinoma. Te formalne operacije ne ovise ni o kakvoj topološkoj strukturi, ali i dalje vrijede mnoga pravila računanja.

Za polinome

$$
\begin{aligned}
f(x)&=a_0+a_1x+\cdots+a_{n-1}x^{n-1}+a_nx^n,\\
g(x)&=b_0+b_1x+\cdots+b_{n-1}x^{n-1}+b_nx^n,
\end{aligned}
$$

zbrajanje polinoma definira se kao

$$
f(x)+g(x) = (a_0+b_0)+(a_1+b_1)x+\cdots+(a_{n-1}+b_{n-1})x^{n-1}+(a_n+b_n)x^n,
$$

a množenje polinoma kao

$$
f(x)g(x) = a_0b_0+(a_1b_0+a_0b_1)x+(a_2b_0+a_1b_1+a_0b_2)x^2+\cdots,
$$

gdje je koeficijent uz $x^k$ jednak $\sum_{i=0}^ka_{k-i}b_i$. Uz tako definirano zbrajanje i množenje može se dokazati da svi polinomi nad $R$ čine prsten, u oznaci $R[x]$.

Stupanj polinoma $f(x)$ označava se s $\deg f(x)$. Polinomi stupnja nula konstantni su polinomi; oni zajedno s nulpolinomom čine ulaganje prstena $R$ u $R[x]$. Očito $R$ ima djelitelje nule ako i samo ako $R[x]$ ima djelitelje nule.

???+ note "Teorem"
    Prsten polinoma $R[x]$ integralna je domena ako i samo ako je $R$ integralna domena.

U prstenu polinoma $R[x]$ nad integralnom domenom $R$ rezultati zbrajanja i množenja zadovoljavaju

$$
\begin{aligned}
\deg(f(x)+g(x)) &\le \max\{\deg f(x),\deg g(x)\},\\
\deg(f(x)g(x)) &= \deg f(x) + \deg g(x).
\end{aligned}
$$

Ovdje stavljamo $\deg 0 = -\infty$. Stoga su invertibilni elementi prstena polinoma nužno samo oni invertibilni elementi među njegovim konstantnim polinomima. Nijedan polinom stupnja jedan ili više nije invertibilan.

Daljnja je rasprava ograničena na polinome nad integralnim domenama.

???+ info "Dogovor"
    U nastavku ćemo bez razlikovanja upotrebljavati izraze „polinom nad prstenom $R$” i „polinom u prstenu polinoma $R[x]$”. Primjerice, da je polinom ireducibilan nad prstenom $R$ znači da je polinom ireducibilan u prstenu $R[x]$. Nadalje, ako je $R$ potprsten od $S$, polinom nad $R$ automatski je i polinom nad $S$; ni to više nećemo posebno naglašavati.

### Prsten polinoma nad poljem

Među prstenima polinoma nad integralnim domenama najjednostavnija svojstva ima, naravno, prsten polinoma nad poljem. U prstenu polinoma $F[x]$ nad poljem $F$ koeficijenti se mogu dijeliti, pa se može definirati dijeljenje s ostatkom. Neka je norma nenul polinoma $f(x)$ jednaka $N(f(x))=\deg f(x)$. Tada se za polinom $f(x)$ i nenul polinom $g(x)$ iz $F[x]$ očito može provesti dijeljenje s ostatkom

$$
f(x)=g(x)q(x)+r(x),
$$

gdje su $q(x),r(x)\in F[x]$ te $r(x)=0$ ili $\deg r(x)<\deg g(x)$. To pokazuje da je svaki prsten polinoma nad poljem Euklidov prsten.

???+ note "Teorem"
    Prsten polinoma $F[x]$ nad poljem $F$ Euklidov je prsten, dakle i prsten glavnih ideala i faktorijalni prsten.

U algoritamskim natjecanjima, zbog preciznosti računanja, često se promatra prsten polinoma $\mathbf F_p[x]=(\mathbf Z/p\mathbf Z)[x]$, pri čemu modul $p$ mora biti prost broj. Takav prsten dopušta Euklidov algoritam i slične operacije. No prsten polinoma $(\mathbf Z/n\mathbf Z)[x]$ za proizvoljan modul $n$ nije čak ni integralna domena.

Vrijeđenje dijeljenja s ostatkom znači da korijen polinoma uvijek odgovara njegovu linearnom faktoru.

???+ abstract "Korijen"
    **Korijen** (root) polinoma $f(x)$ element je $\xi\in F$ za koji vrijedi $f(\xi)=0$.

???+ note "Teorem"
    Za polinom $f(x)$ nad poljem $F$ i element polja $\xi\in F$, $\xi$ je korijen polinoma $f(x)$ ako i samo ako $f(x)$ ima linearni faktor $(x-\xi)$.

??? note "Dokaz"
    Prema dijeljenju s ostatkom postoje $q(x),r(x)$ takvi da vrijedi $f(x)=q(x)(x-\xi)+r(x)$ i $\deg r(x)<\deg(x-\xi)=1$. Stoga je $r(x)$ konstantan polinom ili nulpolinom; stavimo $r(x)=c$, pa nužno vrijedi $f(x)=q(x)(x-\xi)+c$. Uvrstimo $x=\xi$; tada je $0=f(\xi)=c$, tj. $f(x)=q(x)(x-\xi)$.

Pojam korijena može se poopćiti na višestruke korijene.

???+ abstract "Višestruki korijen"
    Ako polinom $f(x)$ ima faktor $(x-\xi)^k$, a $(x-\xi)^{k+1}$ ne dijeli $f(x)$, kažemo da je $\xi$ **korijen kratnosti $k$** (root of multiplicity $k$) polinoma $f(x)$. Ako je $k>1$, korijen $\xi$ naziva se **višestrukim korijenom** (multiple root) polinoma $f(x)$; ako je $k=1$, korijen $\xi$ naziva se **jednostrukim korijenom** (simple root) polinoma $f(x)$.

???+ note "Teorem"
    Ako polinom $f(x)$ nad poljem $F$ ima (moguće ponovljene) korijene $\xi_1,\cdots,\xi_k$, onda on nužno ima faktor $(x-\xi_1)\cdots(x-\xi_k)$. Nadalje, ako je polinom $f(x)$ nad poljem $F$ stupnja $n$, onda on ima najviše $n$ korijena (brojeći kratnosti).

??? note "Dokaz"
    Dovoljno je uočiti da je $F[x]$ faktorijalni prsten.

Iako za polinome nad poljem vrijedi teorem o jedinstvenom rastavu, ne postoji opći način da se utvrdi je li zadani polinom reducibilan. Slučajevi malog stupnja razmjerno su laki. Primjerice, svi polinomi prvog stupnja ireducibilni su. Nad posebnim poljima svi su ireducibilni polinomi prvog stupnja. Takva se polja nazivaju [algebarski zatvorenim poljima](./field-theory.md#algebarski-zatvorena-polja). Nad takvim poljem svaki polinom stupnja većeg od nula ima korijen, pa se svaki polinom stupnja većeg od jedan može dalje rastaviti. Jedan je takav primjer polje kompleksnih brojeva $\mathbf C$. Nad poljem realnih brojeva $\mathbf R$ pak postoje ireducibilni polinomi drugog stupnja; nad poljem racionalnih brojeva $\mathbf Q$ struktura ireducibilnih polinoma još je složenija. Stranica [Teorija polja](./field-theory.md) sadrži više rasprave o polinomima nad poljem racionalnih brojeva i nad konačnim poljima.

Svi gornji rezultati odnose se na polinome nad poljem. Polinomi nad općenitijim integralnim domenama često se mogu svesti na taj slučaj.

Promotrimo sada prsten polinoma $R[x]$ nad faktorijalnim prstenom $R$. Pri izravnom računanju u $R[x]$ mnoge su operacije ograničene jer se koeficijenti često ne mogu dijeliti. Razmotrimo stoga proširenje prstena $R$ do njegova polja razlomaka $F$ i rastavljanje polinoma $f(x)$ iz $R[x]$ u $F[x]$. Znamo da je $F[x]$ faktorijalni prsten, pa se iz rastava polinoma $f(x)$ u $F[x]$ može zaključiti rastav u $R[x]$. Srećom, takva je ideja uvijek provediva.

???+ note "Gaussova lema"
    Za faktorijalni prsten $R$ i njegovo polje razlomaka $F$, ako je $f(x)\in R[x]$ i ako u $F[x]$ vrijedi $f(x)=A(x)B(x)$, onda nužno postoje $s,t\in F$ takvi da je $a(x)=sA(x)\in R[x]$, $b(x)=tB(x)\in R[x]$ i $f(x)=a(x)b(x)$. Stoga, ako je $f(x)$ stupnja većeg od nula ireducibilan u $R[x]$, onda je ireducibilan i u $F[x]$.

??? note "Dokaz"
    Neka je $f(x)\in R[x]$ reducibilan u $F[x]$ i neka je $f(x)=A(x)B(x)$. Neka su $r_a$ i $r_b$ redom najmanji zajednički višekratnici nazivnika svih koeficijenata polinoma $A(x)$ odnosno $B(x)$; tada su $\tilde a(x)=r_aA(x)$ i $\tilde b(x)=r_bB(x)$ polinomi nad $R$. Stavimo $r=r_ar_b$; tada je $rf(x)=\tilde a(x)\tilde b(x)$. Ako je $r$ invertibilan u $R$, možemo uzeti rastav $f(x)=(r^{-1}\tilde a(x))\tilde b(x)$, koji očito zadovoljava zahtjeve leme.
    
    Inače, ako $r$ ima ireducibilni faktor $p$, treba dokazati da se taj faktor može pokratiti na objema stranama jednakosti tako da svi koeficijenti ostanu u integralnoj domeni $R$. Uočimo da je $p$ nužno i prost, pa je $(p)$ prosti ideal. Uzmemo li obje strane jednakosti modulo $p$, dobivamo polinom $0=\bar a(x)\bar b(x)$ nad $(R/(p))[x]$, gdje su $\bar a$ i $\bar b$ polinomi nakon uzimanja modula. Budući da je $R/(p)$ integralna domena, i $(R/(p))[x]$ integralna je domena, pa možemo pretpostaviti $\bar a(x)=0$. To znači da $p$ dijeli sve koeficijente polinoma $\tilde a(x)$. Stoga se na objema stranama jednakosti faktor $p$ može izravno pokratiti.
    
    Prema definiciji faktorijalnog prstena $r$ ima najviše konačno mnogo takvih ireducibilnih faktora, pa se nakon konačno mnogo kraćenja svodimo na slučaj u kojem je $r$ invertibilan u $R$. Time je lema dokazana.

???+ note "Korolar"
    Za faktorijalni prsten $R$ i njegovo polje razlomaka $F$, ako je $f(x)\in R[x]$ i svi su koeficijenti polinoma $f(x)$ relativno prosti (tj. njihov najveći zajednički djelitelj jedinica je u $R$), onda je $f(x)$ ireducibilan u $R[x]$ ako i samo ako je $f(x)$ ireducibilan u $F[x]$.

Drugim riječima, ireducibilni elementi prstena polinoma s cjelobrojnim koeficijentima $\mathbf Z[x]$ ireducibilni su elementi i u $\mathbf Q[x]$. Učinkovita metoda za provjeru ireducibilnosti polinoma s cjelobrojnim koeficijentima jest Eisensteinov kriterij. Prema Gaussovoj lemi on daje i metodu za provjeru ireducibilnosti polinoma s racionalnim koeficijentima.

???+ note "Eisensteinov kriterij"
    Neka je $f(x)=a_0+a_1x+\cdots+a_{n-1}x^{n-1}+a_nx^n$ polinom $n$-tog stupnja s cjelobrojnim koeficijentima. Ako postoji prost broj $p$ takav da $p\mid a_i$ vrijedi za sve $i=0,1,\cdots,n-1$, $p$ ne dijeli $a_n$ i $p^2$ ne dijeli $a_0$, onda je polinom $f(x)$ ireducibilan nad poljem racionalnih brojeva $\mathbf Q$. Ako je $\gcd(a_0,a_1,\cdots,a_n)=1$, polinom $f(x)$ ireducibilan je i nad prstenom cijelih brojeva $\mathbf Z$.

??? note "Dokaz"
    Prema Gaussovoj lemi, ako je polinom $f(x)$ reducibilan nad poljem racionalnih brojeva $\mathbf Q$, onda je reducibilan i nad prstenom cijelih brojeva $\mathbf Z$. Neka je $f(x)=b(x)c(x)$ njegov rastav u $\mathbf Z[x]$. Uzmemo li obje strane jednakosti modulo prost broj $p$, dobivamo rastav u $\mathbf F_p[x]$, $\overline{f}(x)=\overline{b}(x)\overline{c}(x)$. No uvjeti teorema kažu da je $\overline{f}(x)=x^n$, pa nužno postoji cijeli broj $m$ takav da je $\overline b(x)=x^m$ i $\overline c(x)=x^{n-m}$, gdje je $0<m<n$. Stoga su slobodni članovi $b_0$ i $c_0$ faktora $b(x)$ i $c(x)$ višekratnici broja $p$. Dakle, slobodni član $a_0=b_0c_0$ polinoma $f(x)$ nužno je višekratnik broja $p^2$. To je u suprotnosti sa zadanim uvjetom.

??? example "Primjeri"
    1.  Polinom $x^3-2$ ireducibilan je u $\mathbf Q[x]$. Dovoljno je primijeniti Eisensteinov kriterij za $p=2$.
    2.  Polinom $x^4+1$ ireducibilan je u $\mathbf Q[x]$. Inače bi i $(x+1)^4+1=x^4+4x^3+6x^2+4x+2$ bio reducibilan. No primjenom Eisensteinova kriterija za $p=2$ vidimo da potonji nije reducibilan.

Za faktorijalni prsten $R$, budući da je prsten polinoma nad odgovarajućim poljem razlomaka $F$ faktorijalni prsten, a Gaussova lema kaže da rastavi polinoma nad poljem razlomaka $F$ i nad izvornom integralnom domenom $R$ međusobno odgovaraju, i $R[x]$ je faktorijalni prsten. Stoga vrijedi sljedeći teorem:

???+ note "Teorem"
    Prsten polinoma $R[x]$ faktorijalni je prsten ako i samo ako je $R$ faktorijalni prsten.

Ovdje $\mathbf Z[x]$ daje primjer da faktorijalni prsten ne mora biti prsten glavnih ideala. Primjerice, u $\mathbf Z[x]$ ideal $(2,x)$ nije glavni.

Postoji mnogo načina da se prsten polinoma proširi do većeg skupa. Primjerice, prsten polinoma $R[x]$ nad integralnom domenom može se proširiti do svojeg polja razlomaka, u oznaci $R(x)$. To se polje razlomaka često naziva **poljem racionalnih funkcija** (field of rational fractions), a njegovi elementi u osnovi imaju oblik $\dfrac{f(x)}{g(x)}$, gdje su $f(x)$ i $g(x)$ polinomi.

### Prsten polinoma u više varijabli

Prsten polinoma može se poopćiti na slučaj s više neodređenica. Za komutativan prsten s jedinicom $R$ može se definirati prsten polinoma nad $R$, tj. prsten polinoma u jednoj varijabli $R[x]$. Dalje se može definirati prsten polinoma nad $R[x]$, $R[x][y]$, koji se može promatrati kao prsten polinoma u dvije varijable $R[x,y]$ nad $R$. Tako se induktivno može definirati prsten polinoma u $k$ varijabli $R[x_1,\cdots,x_k]$ nad $R$. Kad je $R$ integralna domena, svaki prsten polinoma u više varijabli nad njim integralna je domena; slično se i svojstvo faktorijalnog prstena prenosi na svaki prsten polinoma u više varijabli.

### Prsten formalnih redova potencija

Može se promatrati i slučaj u kojem u formalnom zbroju proizvoljno mnogo koeficijenata smije biti različito od nule. **Formalni red potencija** (formal power series) nad komutativnim prstenom s jedinicom $R$ definira se kao

$$
\sum_{k=0}^\infty a_kx^k=a_0+a_1x+a_2x^2+\cdots.
$$

Zbrajanje i množenje redova potencija može se definirati na isti način kao u prstenu polinoma $R[x]$. Pritom i formalni redovi potencija čine prsten, u oznaci $R[[x]]$. Za ove formalne redove potencija ne treba razmatrati konvergenciju, jer je zapravo svaki formalni red potencija samo svoj niz koeficijenata i nije mu pridana nikakva dodatna topološka struktura.

Struktura prstena formalnih redova potencija vrlo je zanimljiva. U prstenu polinoma nad integralnom domenom invertibilni elementi mogu biti samo konstante. No u prstenu formalnih redova potencija može vrijediti

$$
(1-x)^{-1}=\sum_{k=0}^\infty x^k=1+x+x^2+\cdots.
$$

Ta je pojava opća. Čim je slobodni član $a_0$ formalnog reda potencija invertibilan u $R$, i $\sum_{k=0}^\infty a_kx^k$ nužno je invertibilan. Naime, ako stavimo

$$
\left(\sum_{k=0}^\infty a_kx^k\right)\left(\sum_{k=0}^\infty b_kx^k\right)=1,
$$

onda se, ispišemo li sustav jednadžbi koje koeficijenti moraju zadovoljavati, izrazi za $b_k$ mogu rekurzivno odrediti, pri čemu se pojavljuje samo inverz od $a_0$.

Na prstenu formalnih redova potencija mogu se definirati razne operacije, poput inverza, dijeljenja, kompozicijskog inverza, formalne derivacije, elementarnih funkcija itd.; vidi [Uvod u tehnike s polinomima](../poly/intro.md).

### Prsten formalnih Laurentovih redova

Prsten formalnih redova potencija može se dodatno proširiti tako da dopušta članove negativnog stupnja. **Formalni Laurentov red** (formal Laurent series) nad komutativnim prstenom s jedinicom $R$ definira se kao

$$
\sum_{k=N}^\infty a_kx^k,
$$

gdje je $N\in\mathbf Z$. Formalni Laurentov red može, dakle, imati konačno mnogo članova negativnog stupnja. Proširimo li prethodno zbrajanje i množenje na formalne Laurentove redove, dobivamo prsten formalnih Laurentovih redova, u oznaci $R((x))$. Ako je $F$ polje, onda je i $F((x))$ polje.

Prsten formalnih Laurentovih redova ima primjenu u [Lagrangeovoj inverziji](../poly/lagrange-inversion.md).

## Kineski teorem o ostatcima

Povezano štivo: [Kineski teorem o ostatcima](../number-theory/crt.md)

U teoriji brojeva kineski teorem o ostatcima često se upotrebljava za rješavanje sustava kongruencija. Za opće komutativne prstene s jedinicom također se može uspostaviti kineski teorem o ostatcima. Svaka kongruencija zapravo zadaje sliku nepoznanice u nekom kvocijentnom prstenu, pa kineski teorem o ostatcima u komutativnom prstenu s jedinicom odgovara određivanju elementa prstena preko njegovih slika u tim kvocijentnim prstenima.

Ta se rasprava može pretočiti u formalni jezik. Za nenul komutativan prsten s jedinicom $R$ i njegove ideale $I_1,\cdots,I_n$ promotrimo homomorfizam prstena $\varphi:R\rightarrow R/I_1\times \cdots\times R/I_n$ koji $r$ preslikava u $(r+I_1,\cdots,r+I_n)$. Pritom je $r+I_i$ susjedna klasa, a $\times$ označava direktni produkt prstena:

???+ abstract "Direktni produkt"
    Za prstene $R_1$ i $R_2$ na direktnom produktu $R_1\times R_2$ njihovih aditivnih grupa može se definirati množenje po komponentama; tada $R_1\times R_2$ postaje prsten koji se naziva **direktnim produktom** (direct product) prstena $R_1$ i $R_2$ i i dalje označava s $R_1\times R_2$.

Jezgra homomorfizma $\varphi$ jest $\ker\varphi=I_1\cap\cdots\cap I_n$. Pitanje na koje kineski teorem o ostatcima odgovara jest uz koje je uvjete takvo preslikavanje surjekcija.

U slučaju teorije brojeva za vrijeđenje teorema potrebno je da moduli budu relativno prosti. Taj se uvjet može poopćiti na slučaj teorije prstena.

???+ abstract "Komaksimalnost"
    Neka prsten $R$ ima ideale $I$ i $J$. Ako je $I+J=R$, kažemo da su $I$ i $J$ **komaksimalni** (comaximal).

U slučaju prstena s jedinicom, promatramo li glavne ideale $(a)$ i $(b)$, taj je uvjet isto što i postojanje $x,y\in R$ takvih da je $ax+by=1$, što je slično Bézoutovu teoremu za relativno proste cijele brojeve. Pomoću te definicije može se, potpuno po uzoru na slučaj prstena cijelih brojeva, uspostaviti **kineski teorem o ostatcima** (Chinese remainder theorem) u komutativnom prstenu s jedinicom.

???+ note "Kineski teorem o ostatcima"
    Neka nenul komutativan prsten s jedinicom $R$ ima ideale $I_1,\cdots,I_n$. Ako su oni u parovima komaksimalni, onda je gore definirani homomorfizam prstena $\varphi$ surjekcija, a njegova je jezgra jednaka umnošku tih ideala, $\ker\varphi=I_1\cap\cdots\cap I_n=I_1\cdots I_n$, pa je
    
    $$
    R/(I_1\cdots I_n)=R/(I_1\cap\cdots\cap I_n)\cong R/I_1\times\cdots\times R/I_n.
    $$

??? note "Dokaz"
    Sadržaj teorema vrlo je bogat, ali treba dokazati samo dvije tvrdnje: da je $\varphi$ surjekcija i da je $I_1\cap\cdots\cap I_n=I_1\cdots I_n$. Ključno je dobro iskoristiti uvjet komaksimalnosti.
    
    Najprije dokazujemo slučaj $n=2$. Budući da su ideali $I_1$ i $I_2$ komaksimalni, tj. $I_1+I_2=R$, jedinica $1$ prstena $R$ može se zapisati u obliku $a_1+a_2$, gdje je $a_i\in I_i$. Budući da je $a_1\in I_1$ i $a_1=1-a_2\in 1+I_2$, vrijedi $\varphi(a_1)=(I_1,1+I_2)$; analogno, $\varphi(a_2)=(1+I_1,I_2)$. Stoga $(\varphi(a_2),\varphi(a_1))$ igra ulogu sličnu „bazi” u vektorskom prostoru. Dakle, za proizvoljnu sliku $(r_1+I_1,r_2+I_2)$ može se naći praslika $r_1a_2+r_2a_1$ pri homomorfizmu $\varphi$. To pokazuje da je $\varphi$ surjekcija.
    
    Treba još dokazati $I_1\cap I_2=I_1I_2$. Za opći prsten uvijek vrijedi $I_1I_2\subseteq I_1\cap I_2$; ključna je obratna inkluzija. Za proizvoljan $r\in I_1\cap I_2$ vrijedi $r=r(a_1+a_2)=ra_1+ra_2\in I_1I_2$. Stoga vrijedi i $I_1\cap I_2\subseteq I_1I_2$. Time je tražena tvrdnja dokazana.
    
    Za slučaj $n>2$ treba upotrijebiti matematičku indukciju. Ključ koraka indukcije jest dokazati da su za u parovima komaksimalne ideale $I_1,\cdots,I_n$ ideali $I_1$ i $I_2\cdots I_n$ uvijek komaksimalni. Budući da je $I_1$ komaksimalan sa svakim od $I_2,\cdots,I_n$, za svaki $i=2,\cdots,n$ postoje $a_i\in I_1$ i $b_i\in I_i$ takvi da vrijedi $1=a_i+b_i$. Stoga vrijedi $1=(a_2+b_2)\cdots(a_n+b_n)$. Dakle, $1\in (b_2\cdots b_n)+I_1\subseteq I_1+(I_2\cdots I_n)$. To pokazuje da su ideali $I_1$ i $I_2\cdots I_n$ komaksimalni.

### Primjena: Lagrangeova interpolacijska formula

Povezano štivo: [Lagrangeova interpolacija](../numerical/interp.md#lagrangeova-interpolacija), [Brza interpolacija polinoma](../poly/multipoint-eval-interpolation.md#brza-interpolacija-polinoma)

Problem interpolacije (interpolation) glasi: za zadani niz točaka $\{(x_i,y_i)\}_{i=1}^n$ naći polinom $f(x)$ nad poljem $F$ takav da $f(x_i)=y_i$ vrijedi za sve $i=1,\cdots,n$. Naravno, pretpostavlja se da su svi $x_i$ međusobno različiti. Lagrangeova interpolacijska formula daje opće rješenje te vrste problema.

Za polinom $f(x)$ nad poljem $F$ uvjet $f(x_i)=y_i$ ekvivalentan je tome da je $x_i$ korijen polinoma $f(x)-y_i$, dakle ekvivalentan s $(x-x_i)\mid(f(x)-y_i)$, tj. s $f(x)\equiv y_i\pmod{x-x_i}$. Stoga je problem interpolacije ekvivalentan rješavanju sustava kongruencija

$$
\begin{cases}
f(x)\equiv y_1&\pmod{x-x_1},\\
f(x)\equiv y_2&\pmod{x-x_2},\\
\cdots\\
f(x)\equiv y_n&\pmod{x-x_n}.
\end{cases}
$$

Ti linearni polinomi $\{x-x_i\}_{i=1}^n$ u parovima su relativno prosti. Prema kineskom teoremu o ostatcima rješenje problema treba imati oblik

$$
f(x)=\sum_{i=1}^ny_iM_i(x),
$$

gdje je $M_i(x)=m_i(x)\prod_{j\neq i}(x-x_j)$ i $M_i(x)\equiv 1\pmod{x-x_i}$. Prema prije izvedenoj ekvivalenciji to je ekvivalentno s $M_i(x_i)=1$, tj.

$$
m_i(x_i)\prod_{j\neq i}(x_i-x_j) = 1.
$$

Možemo uzeti da je $m_i(x)$ konstantan polinom, tj.

$$
m_i(x) = \frac{1}{\prod_{j\neq i}(x_i-x_j)}.
$$

Odatle dobivamo Lagrangeovu interpolacijsku formulu

$$
f(x)=\sum_{i=1}^ny_i\frac{\prod_{j\neq i}(x-x_j)}{\prod_{j\neq i}(x_i-x_j)}.
$$

Općenito, poopćenjem te metode može se izvesti i [Hermiteova interpolacijska formula](https://en.wikipedia.org/wiki/Hermite_interpolation), koja dopušta da se u pojedinim točkama propišu vrijednosti nekoliko derivacija polinoma.

### Primjena: multiplikativna grupa klasa ostataka cijelih brojeva

Povezano štivo: [Primitivni korijen](../number-theory/primitive-root.md), [Osnovni teorem o konačno generiranim Abelovim grupama](./group-theory.md#teorem-o-klasifikaciji)

Kao primjenu kineskog teorema o ostatcima i sadržaja iz teorije grupa ovdje raspravljamo o strukturi multiplikativne grupe cijelih brojeva modulo $n$. U ovom odjeljku izostavljamo crtu iznad oznaka klasa ostataka.

**Multiplikativna grupa cijelih brojeva modulo $n$** (multiplicative group of integers modulo $n$) jest $(\mathbf Z/n\mathbf Z)^\times$, tj. multiplikativna grupa invertibilnih elemenata kvocijentnog prstena $\mathbf Z/n\mathbf Z$ (naziva se i grupom jedinica). Red grupe $(\mathbf Z/n\mathbf Z)^\times$ jest $\varphi(n)$, jer je nužan i dovoljan uvjet za postojanje inverza relativna prostost s $n$. Ovdje je $\varphi(n)$ [Eulerova funkcija](../number-theory/euler-totient.md). Štoviše, grupa $(\mathbf Z/n\mathbf Z)^\times$ uvijek je Abelova.

Prema osnovnom teoremu aritmetike modul $n$ može se rastaviti na umnožak potencija različitih prostih brojeva:

$$
n=p_1^{\alpha_1}\cdots p_s^{\alpha_s}.
$$

Lako se provjeri da je za ideale prstena cijelih brojeva uvjet komaksimalnosti ideala ekvivalentan relativnoj prostosti njihovih generatora. Stoga primjenom kineskog teorema o ostatcima dobivamo

$$
\mathbf Z/n\mathbf Z\cong\mathbf Z/p_1^{\alpha_1}\mathbf Z\times\cdots\times\mathbf Z/p_s^{\alpha_s}\mathbf Z.
$$

Izomorfizam prstena znači da su i odgovarajuće multiplikativne strukture izomorfne, pa je

$$
(\mathbf Z/n\mathbf Z)^\times\cong(\mathbf Z/p_1^{\alpha_1}\mathbf Z)^\times\times\cdots\times(\mathbf Z/p_s^{\alpha_s}\mathbf Z)^\times.
$$

To pokazuje da je $\varphi(n)=\varphi(p_1^{\alpha_1})\cdots\varphi(p_s^{\alpha_s})$, tj. Eulerova je funkcija multiplikativna.

Stoga je za proučavanje slučaja općeg modula dovoljno promotriti slučaj u kojem je modul potencija prostog broja $p^k$. Za potencije prostog broja treba zasebno razmotriti dva slučaja, $p=2$ i $p$ neparan prost broj:

-   Za $p=2$ izravnom provjerom dobivamo $(\mathbf Z/2\mathbf Z)^\times\cong C_1$ i $(\mathbf Z/4\mathbf Z)^\times\cong C_2$. Za $k\ge3$ vrijedi $(\mathbf Z/2^k\mathbf Z)^\times\cong C_2\times C_{2^{k-2}}$.

    ??? note "Dokaz"
        Izravnim računom pomoću binomnog teorema dobivamo
        
        $$
        \begin{aligned}
        5^{2^{k-2}}=(1+2^2)^{2^{k-2}}&\equiv 1\pmod {2^k},\\
        5^{2^{k-3}}=(1+2^2)^{2^{k-3}}&\equiv 1+2^{k-1}\pmod {2^k}.
        \end{aligned}
        $$
        
        Stoga je $5$ element reda $2^{k-2}$ u $(\mathbf Z/2^k\mathbf Z)^\times$. Istodobno su $-1$ i $5^{2^{k-3}}$ dva različita elementa reda dva, pa je $-1\notin\langle 5\rangle$. Dakle, presjek podgrupa $\langle-1\rangle$ i $\langle 5\rangle$ trivijalan je, pa prema karakterizaciji direktnog produkta grupa vrijedi
        
        $$
        (\mathbf Z/2^k\mathbf Z)^\times\cong\langle-1\rangle\times\langle 5\rangle\cong C_2\times C_{2^{k-2}}.
        $$
-   Za neparan prost broj $p$ može se dokazati da je $(\mathbf Z/p^k\mathbf Z)^\times$ izomorfna cikličkoj grupi $C_{\varphi(p^k)}$.

    ??? note "Dokaz"
        Da bismo dokazali da je $(\mathbf Z/p^k\mathbf Z)^\times$ ciklička, prema osnovnom teoremu o konačnim Abelovim grupama dovoljno je dokazati da je svaka njezina Sylowljeva $q$‑podgrupa ciklička. Najprije, za Sylowljevu $p$‑podgrupu izravnim računom dobivamo
        
        $$
        \begin{aligned}
        (1+p)^{p^{k-1}} &\equiv 1\pmod{p^k},\\
        (1+p)^{p^{k-2}} &\equiv 1+p^{k-1}\pmod{p^k}.
        \end{aligned}
        $$
        
        Stoga je $(1+p)$ element reda $p^{k-1}$. Drugim riječima, jedina Sylowljeva $p$‑podgrupa grupe $(\mathbf Z/p^k\mathbf Z)^\times$ ciklička je grupa $\langle 1+p\rangle$.
        
        Ostale Sylowljeve $q$‑podgrupe ($q\neq p$) mogu se homomorfizmom grupa svesti na slučaj $k=1$. Promotrimo homomorfizam grupa $\varphi:(\mathbf Z/p^k\mathbf Z)^\times\rightarrow(\mathbf Z/p\mathbf Z)^\times$ koji susjednu klasu $r+p^k\mathbf Z$ preslikava u susjednu klasu $r+p\mathbf Z$. Jezgra tog preslikavanja ima $p^{k-1}$ elemenata, pa, ograničimo li preslikavanje $\varphi$ na Sylowljevu $q$‑podgrupu ($q\neq p$) grupe $(\mathbf Z/p^k\mathbf Z)^\times$, jezgra ograničenog preslikavanja trivijalna je, pa je ta Sylowljeva $q$‑podgrupa izomorfna slici preslikavanja, tj. Sylowljevoj $q$‑podgrupi grupe $(\mathbf Z/p\mathbf Z)^\times$. Stoga je dovoljno dokazati da su sve Sylowljeve $q$‑podgrupe grupe $(\mathbf Z/p\mathbf Z)^\times$ cikličke.
        
        Naposljetku dokazujemo da su sve Sylowljeve $q$‑podgrupe grupe $(\mathbf Z/p\mathbf Z)^\times$ cikličke. Budući da je $(\mathbf Z/p\mathbf Z)^\times$ konačna Abelova grupa, može se po invarijantnim faktorima rastaviti kao
        
        $$
        C_{n_1}\times\cdots\times C_{n_r}.
        $$
        
        Ovdje je $n_1\mid n_2\mid \cdots \mid n_r$. Stoga u svakom faktoru direktnog produkta postoji $n_1$ elemenata čiji red dijeli $n_1$. Ako je $r>1$, onda nužno strogo više od $n_1$ elemenata zadovoljava jednadžbu $x^{n_1}=1$. No $\mathbf Z/p\mathbf Z$ je polje, a polinom $n_1$-og stupnja nad poljem ima najviše $n_1$ korijena, pa je $r=1$. Drugim riječima, $(\mathbf Z/p\mathbf Z)^\times\cong C_{p-1}$.
        
        Time je dokazano $(\mathbf Z/p^k\mathbf Z)^\times\cong C_{p^{k-1}}\times C_{p-1}\cong C_{\varphi(p^{k})}$.

Time je određena i struktura multiplikativne grupe za opći modul. Iz dobivenih rezultata znamo da je multiplikativna grupa cijelih brojeva modulo $n$ ciklička ako i samo ako modul $n$ poprima vrijednost

$$
1,2,4,p^k,2p^k
$$

gdje je $p$ neparan prost broj; inače multiplikativna grupa cijelih brojeva modulo $n$ nužno ima podgrupu $C_2\times C_2$ i ne može biti ciklička. Kad je multiplikativna grupa ciklička, njezin generator naziva se **primitivnim korijenom** (primitive root) tog modula. Stoga ovdje navedeni teorem daje upravo nužan i dovoljan uvjet postojanja primitivnog korijena.

Naravno, analiza strukture multiplikativne grupe sadrži više informacija od samog uvjeta postojanja primitivnog korijena. Ona jasno odražava redove različitih elemenata multiplikativne grupe. Element $x$ grupe $(\mathbf Z/n\mathbf Z)^\times$ koji zadovoljava $x^k=1$, tj. rješenje kongruencije $x^k\equiv 1\pmod n$, naziva se **$k$-tim korijenom jedinice modulo $n$** ($k$-th root of unity modulo $n$); element reda točno $k$ naziva se **primitivnim $k$-tim korijenom jedinice modulo $n$** (primitive $k$-th root of unity modulo $n$). Pomoću strukture multiplikativne grupe postojanje i broj tih korijena jedinice mogu se točno izračunati. Naposljetku, najmanji zajednički višekratnik redova svih elemenata grupe $(\mathbf Z/n\mathbf Z)^\times$, tj. najmanji prirodan broj $k$ takav da $x^k=1$ vrijedi za sve $x\in (\mathbf Z/n\mathbf Z)^\times$, izražen kao funkcija od $n$, upravo je [Carmichaelova funkcija](../number-theory/primitive-root.md#carmichaelova-funkcija). Niz njezinih svojstava može se dobiti iz strukture multiplikativne grupe.

## Literatura i napomene

-   Dummit, D.S. and Foote, R.M. (2004) Abstract Algebra. 3rd Edition, John Wiley & Sons, Inc.
-   [Quadratic integer - Wikipedia](https://en.wikipedia.org/wiki/Quadratic_integer)
-   [Formal power series - Wikipedia](https://en.wikipedia.org/wiki/Formal_power_series)
-   [Multiplicative group of integers modulo $n$- Wikipedia](https://en.wikipedia.org/wiki/Multiplicative_group_of_integers_modulo_n)

[^ideal-history]: <https://en.wikipedia.org/wiki/Ideal_(ring_theory)#History>

[^simple-ring]: Kao i u slučaju grupa, takav se prsten naziva **jednostavnim prstenom** (simple ring). Komutativan jednostavan prsten može biti samo polje, dok je slučaj nekomutativnih jednostavnih prstena mnogo složeniji.

[^gcd-domain]: Integralna domena u kojoj postoji najveći zajednički djelitelj naziva se [GCD-domenom](https://en.wikipedia.org/wiki/GCD_domain).

[^ring-theory-history]: Kratka povijest teorije prstena može se pročitati [ovdje](https://mathshistory.st-andrews.ac.uk/HistTopics/Ring_theory/).
