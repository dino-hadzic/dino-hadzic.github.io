---
title: Teorija polja
---

Predznanje: [Osnovni pojmovi apstraktne algebre](./basic.md), [Teorija grupa](./group-theory.md), [Teorija prstena](./ring-theory.md)

## Uvod

**Teorija polja** (field theory) je teorija o poljima.

Teorija polja o kojoj govori ovaj članak uglavnom je teorija proširenja polja. Polje je algebarska struktura zatvorena na zbrajanje, oduzimanje, množenje i dijeljenje; u algoritamskim natjecanjima često se računa modulo prost broj $p$, što je zapravo računanje u konačnom polju $\mathbf F_p$. Slično kao u slučaju polja realnih brojeva $\mathbf R$, neke je probleme pogodnije rješavati računanjem u većem polju (tj. u polju kompleksnih brojeva $\mathbf C$); uobičajen je primjer ubrzavanje množenja polinoma s realnim koeficijentima pomoću [brze Fourierove transformacije](../poly/fft.md). Slično se može postupiti i s konačnim poljima. Većini su čitatelja proširenja konačnih polja relativno nepoznata, pa je korisno upoznati opću teoriju proširenja polja. Na kraju članka navedene su neke algoritamske primjene u kojima je potrebno proširiti konačno polje, a ukratko su obrađena i proširenja prstena cijelih brojeva koja bi mogla biti potrebna u nekim od tih primjena.

S teorijom polja usko je povezana Galoisova teorija. Ona povezuje proširenja polja s njihovim grupama automorfizama, pa se svojstva proširenja polja mogu razumjeti alatima teorije grupa. Iako je i ta teorija često središnji sadržaj odgovarajućih kolegija iz algebre, vrlo je daleko od sadržaja algoritamskih natjecanja, pa je ovaj članak ne obrađuje podrobnije. Zainteresirani čitatelji trebali bi posegnuti za odgovarajućom stručnom literaturom.

???+ info "Oznake"
    Kad to ne izaziva dvosmislenost, u ovom se članku može izostaviti znak množenja u prstenima i poljima, a prsten $(R,+,\cdot)$ zapisuje se kao prsten $R$, a polje $(F,+,\cdot)$ kao polje $F$. Neutralni element zbrajanja u prstenu i polju naziva se nula, a neutralni element množenja jedinica. Osim toga, $p$ u ovom članku uvijek označava prost broj, a $q$ uvijek označava potenciju prostog broja i može se zapisati kao $p^n$, gdje je $n$ prirodan broj.

## Proširenja polja

Slično kao za grupe i prstene, mogu se uvesti pojmovi potpolja i homomorfizma polja.

???+ abstract "Potpolje"
    Ako je potprsten $E$ polja $F$ također polje, kaže se da je $E$ **potpolje** (subfield) polja $F$.

Pritom, bez obzira na to kako definicija prstena i potprstena tretira jedinicu, potpolje $E$ nužno sadrži jedinicu polja $F$[^subfield-one].

???+ abstract "Homomorfizam polja"
    Homomorfizam prstena $\varphi:F\rightarrow E$ iz polja $F$ u polje $E$ naziva se i **homomorfizam polja** (field homomorphism) iz polja $F$ u polje $E$.

??? info "Kako homomorfizam polja tretira jedinicu"
    Ako, drugačije nego u definiciji iz ovog članka, homomorfizam prstena zahtijeva da se jedinica preslika u jedinicu, onda to prirodno zahtijeva i homomorfizam polja. U suprotnom se jedinica može preslikati i u nulu.

Budući da polje ima samo trivijalne ideale, homomorfizam polja ili preslikava cijelo polje u nulu ili je nužno ulaganje (embedding). To znači da se rasprava o homomorfizmima polja može svesti na raspravu o potpoljima.

U slučaju polja, manje je polje često ono poznatije, pa se veće polje obično promatra polazeći od potpolja kao ishodišta. To je pojam proširenja polja.

???+ abstract "Proširenje polja"
    Za polje $F$, ako je $F$ potpolje polja $E$, kaže se da je polje $E$ **proširenje** (extension) polja $F$, ili **polje proširenja**, i piše se $E/F$.

???+ info "Oznaka za proširenje polja"
    Iako je zapis formalno isti, pojam proširenja polja nema nikakve veze s kvocijentnim prstenom i ne treba ih miješati.

???+ example "Primjer"
    Polje kompleksnih brojeva $\mathbf C$ proširenje je polja realnih brojeva $\mathbf R$, a polje realnih brojeva $\mathbf R$ pak je proširenje polja racionalnih brojeva $\mathbf Q$.

### Stupanj proširenja polja

Za proširenje polja $E/F$, polje $E$ uvijek je [vektorski prostor](../linear-algebra/vector-space.md) nad poljem $F$. Dimenzija tog vektorskog prostora je stupanj proširenja polja.

???+ abstract "Stupanj proširenja polja"
    **Stupanj** (degree) proširenja polja $E/F$ dimenzija je polja $E$ promatranog kao vektorski prostor nad poljem $F$, tj. $\dim_F(E)$, i označava se $[E:F]$. Ako je stupanj proširenja polja konačan, proširenje se naziva **konačno proširenje** (finite extension); u suprotnom se naziva **beskonačno proširenje** (infinite extension).

???+ example "Primjer"
    Stupanj $[\mathbf C:\mathbf R]$ proširenja polja $\mathbf C/\mathbf R$ jednak je $2$, pa je to konačno proširenje. Proširenje polja $\mathbf R/\mathbf Q$ beskonačno je proširenje.

Stupnjevi proširenja polja su multiplikativni.

???+ note "Teorem"
    Neka su $F\subseteq K\subseteq E$ polja. Tada stupnjevi proširenja među njima zadovoljavaju $[E:F]=[E:K][K:F]$.

??? note "Dokaz"
    Za slučaj beskonačnog stupnja proširenja tvrdnja je očita; u suprotnom, ako je $\{\alpha_i\}$ baza polja $E$ kao vektorskog prostora nad $K$, a $\{\beta_j\}$ baza polja $K$ kao vektorskog prostora nad $F$, lako se provjeri da je $\{\alpha_i\beta_j\}$ baza polja $E$ kao vektorskog prostora nad $F$.

Ovaj se članak uglavnom bavi konačnim proširenjima polja.

### Karakteristika polja

Proučavanje proširenja polja ima prirodnu polaznu točku: najmanje potpolje koje sadrži jedinicu polja $F$. To se polje naziva i **prosto potpolje** (prime subfield) polja $F$.

Struktura prostog potpolja jednoznačno je određena svojstvima jedinice polja. Karakteristika polja sažima upravo ta svojstva.

???+ abstract "Karakteristika polja"
    **Karakteristika** (characteristic) polja $F$ najmanji je prirodan broj $n$ za koji vrijedi $n\cdot 1=0$; ako takav $n$ ne postoji, kaže se da je karakteristika polja $F$ jednaka $0$. Pritom $n\cdot 1$ označava zbroj $n$ jedinica $1$. Ako karakteristika polja $F$ nije $0$, kaže se da polje $F$ ima **konačnu karakteristiku** (finite characteristic).

Karakteristika polja može se razumjeti pomoću homomorfizma prstena. Prsten cijelih brojeva $\mathbf Z$ zatvorena je struktura dobivena iz $0$ i $1$ uzastopnim primjenjivanjem zbrajanja, oduzimanja i množenja. Može se shvatiti kao svojevrsni „prototip”: svi prsteni s jedinicom trebali bi „naslijediti” dio strukture prstena cijelih brojeva[^initial-object-ring]. Stoga se za polje $F$ može promatrati homomorfizam prstena $\varphi:\mathbf Z\rightarrow F$ uz zahtjev $\varphi(1)=1$. Takav je homomorfizam prstena jednoznačno određen: on $n\in\mathbf N_+$ preslikava u $n\cdot 1$, tj. u zbroj $n$ jedinica $1$. Slika $\varphi(\mathbf Z)$ tog homomorfizma uložena je u polje $F$, pa nužno ima jedinicu, komutativna je i bez djelitelja nule, dakle integralna je domena. Zato je jezgra $\ker\varphi$ homomorfizma nužno prost ideal. Prosti ideali prstena cijelih brojeva $\mathbf Z$ mogu biti samo oblika $(n)$, gdje je $n=0$ ili je $n$ prost broj. Tako dobiveni $n$ upravo je karakteristika tog polja.

Karakteristika polja određuje strukturu prostog potpolja:

1.  Kad je karakteristika $0$, homomorfizam $\varphi$ je injektivan, pa je prsten cijelih brojeva $\mathbf Z$ uložen u polje $F$. Polje racionalnih brojeva $\mathbf Q$, kao najmanje polje koje sadrži prsten cijelih brojeva, također se nužno može uložiti u polje $F$ i ono je prosto potpolje polja $F$;
2.  Kad je karakteristika prost broj $p$, slika $\mathbf Z/p\mathbf Z$ homomorfizma $\varphi$ uložena je u polje $F$. Pritom je $\mathbf Z/p\mathbf Z$ već polje, označava se $\mathbf F_p$ i ono je prosto potpolje polja $F$.

Ova rasprava zapravo pokazuje sljedeću tvrdnju:

???+ note "Teorem"
    Karakteristika polja $F$ može biti samo $0$ ili prost broj $p$. Prosto potpolje polja karakteristike $0$ je $\mathbf Q$, a prosto potpolje polja karakteristike $p$ je $\mathbf F_p$.

Polja $\mathbf Q$ i $\mathbf F_p$ iz teorema nazivaju se i **prosta polja** (prime field), tj. polja čije je jedino potpolje ono samo. Konačno polje nužno ima konačnu karakteristiku, jer polje karakteristike $0$ sadrži barem potpolje $\mathbf Q$.

Svojstva polja konačne karakteristike i polja karakteristike nula često se razlikuju. Primjerice, polja konačne karakteristike imaju sljedeća svojstva:

???+ note "Teorem"
    Neka je karakteristika polja $F$ jednaka $p$. Tada vrijedi:
    
    1.  U aditivnoj grupi polja $F$ svi elementi različiti od nule imaju red $p$, tj. za sve $x\in F$ vrijedi $px=0$;
    2.  „San brucoša” (freshman's dream), tj. za sve $x,y\in F$ vrijedi $(x+y)^p=x^p+y^p$. Štoviše, preslikavanje $x\mapsto x^p$ injektivni je endomorfizam polja $F$, koji se naziva **Frobeniusov endomorfizam** (Frobenius endomorphism).

??? note "Dokaz"
    Za prvo svojstvo dovoljno je uočiti da je $px=(p1)x=0x=0$. Za drugo svojstvo dovoljno je uočiti da su u binomnom razvoju od $(x+y)^p$ koeficijenti svih članova osim $x^p$ i $y^p$ višekratnici od $p$, pa prema prvom svojstvu vrijedi $(x+y)^p=x^p+y^p$. Da bi se provjerilo da je $x\mapsto x^p$ endomorfizam, treba još provjeriti $(xy)^p=x^py^p$, što vrijedi jer je množenje u polju komutativno. Naposljetku, homomorfizam prstena među poljima koji jedinicu preslikava u jedinicu nužno je injekcija.

Naravno, za konačna polja Frobeniusov endomorfizam nužno je i surjektivan, pa je automorfizam polja.

### Jednostavna proširenja

Slično kao pri proširivanju polja realnih brojeva do polja kompleksnih brojeva, mnoga se proširenja mogu izvesti dodavanjem dodatnih elemenata polju i propisivanjem njihovih računskih svojstava. U općem slučaju, da bi se izbjegle poteškoće koje nastaju propisivanjem računskih svojstava, može se promatrati proširenje polja $E/F$ i polju $F$ pridodavati elemente iz $E\setminus F$; tada su pravila računanja tih dodatnih elemenata s elementima polja $F$ već određena u većem polju $E$.

???+ abstract "Proširenje polja generirano podskupom"
    Neka je $E/F$ proširenje polja i $S\subseteq E$. Tada je **proširenje polja $F$ generirano skupom $S$** (extension generated by $S$ over $F$) najmanje potpolje polja $E$ koje sadrži i $F$ i $S$; označava se $F(S)$.

Najjednostavniji je, naravno, slučaj kad skup $S$ ima vrlo malo elemenata.

???+ abstract "Konačno generirano proširenje"
    Neka je $E/F$ proširenje polja. Ako postoji konačan skup $S=\{\alpha_1,\cdots,\alpha_n\}\subseteq E$ takav da vrijedi $E=F(S)$, kaže se da je $E$ **konačno generirano proširenje** (finitely generated extension) polja $F$, i piše se također $F(\alpha_1,\cdots,\alpha_n)$.

???+ abstract "Jednostavno proširenje"
    Neka je $E/F$ proširenje polja. Ako postoji $\alpha\in E$ takav da vrijedi $E=F(\alpha)$, kaže se da je polje $E$ **jednostavno proširenje** (simple extension) polja $F$. Pritom se element $\alpha$ naziva **primitivni element** (primitive element) tog jednostavnog proširenja.

???+ example "Primjeri"
    Svi ovi primjeri dobiveni su dodavanjem elemenata iz $\mathbf C$ polju $\mathbf Q$.
    
    1.  Za cijeli broj $D\neq 0,1$ bez kvadratnih faktora, kvadratno polje $\mathbf Q(\sqrt D)$ jednostavno je proširenje dobiveno dodavanjem $\sqrt D\in\mathbf C\setminus\mathbf Q$ polju $\mathbf Q$. Njegov je stupanj $2$, jer $\{1,\sqrt D\}$ čini bazu.
    2.  Polje $\mathbf Q(\sqrt 2,\sqrt 3)$ proširenje je dobiveno dodavanjem $\sqrt 2$ i $\sqrt 3$ polju $\mathbf Q$. Naravno, vrijedi $\mathbf Q(\sqrt 2,\sqrt 3)=\mathbf Q(\sqrt 2)(\sqrt 3)=\mathbf Q(\sqrt 3)(\sqrt 2)$, tj. konačno proširenje ne ovisi o redoslijedu i načinu dodavanja elemenata. To je također jednostavno proširenje, jer je $\mathbf Q(\sqrt 2,\sqrt 3)=\mathbf Q(\sqrt 2+\sqrt 3)$. Njegov je stupanj $4$, jer $\{1,\sqrt 2,\sqrt 3,\sqrt 6\}$ čini bazu.
    3.  Polje $\mathbf Q(\pi)$ također je jednostavno proširenje, gdje je $\pi$ Ludolfov broj. Ono je beskonačno proširenje, jer već $\mathbf Q[\pi]\subseteq \mathbf Q(\pi)$ ima bazu $\{1,\pi,\pi^2,\cdots\}$.
    4.  Konačno generirano proširenje ne mora biti jednostavno. Primjerice, neka su $x,y$ dvije neodređenice; tada je polje racionalnih funkcija $\mathbf Q(x,y)$ konačno generirano proširenje polja $\mathbf Q$, ali je njegov stupanj transcendentnosti $2$, pa nije jednostavno proširenje.

Ovi primjeri pokazuju da se svojstva jednostavnih proširenja mogu silno razlikovati. To ovisi o svojstvima dodanog elementa.

### Algebarska proširenja

Da bi se analizirali svi slučajevi koji mogu nastati dodavanjem elementa polju, može se, po uzoru na raniju raspravu o karakteristici polja, promatrati homomorfizam prstena iz prstena polinoma $F[x]$ u proširenje $E/F$. Ovdje $F[x]$ igra ulogu koju je ranije imao prsten cijelih brojeva $\mathbf Z$: on je upravo „prototip” strukture koja nastaje dodavanjem neodređenice $x$ polju $F$ i zatvaranjem na zbrajanje, oduzimanje i množenje[^polynomial-universal].

Neka homomorfizam prstena $\varphi:F[x]\rightarrow E$ zadovoljava da je restrikcija $\varphi$ na $F$ identiteta te da je $\varphi(x)=\alpha$, tj. neodređenica se preslikava u neki element proširenja $E$. Budući da je slika $\varphi(F[x])=F[\alpha]$ nužno integralna domena, jezgra $\ker\varphi$ homomorfizma nužno je prost ideal prstena polinoma $F[x]$. Prsten polinoma nad poljem prsten je glavnih ideala, pa jezgra nužno ima oblik $(f(x))$, gdje je $f(x)=0$ ili je $f(x)$ nesvodiv element u $F[x]$. O tome se može reći sljedeće:

1.  Kad je jezgra homomorfizma $\ker\varphi=\{0\}$, prsten polinoma $F[x]$ uložen je u $E$ i njegova slika $F[\alpha]$ integralna je domena. Stoga je najmanje polje u $E$ koje sadrži i $F$ i $\alpha$ polje razlomaka od $F[\alpha]$, tj. $F(\alpha)$. Ta se oznaka može tumačiti i kao rezultat uvrštavanja $\alpha$ umjesto neodređenice u polje racionalnih funkcija $F(x)$, i kao jednostavno proširenje polja $F$ generirano elementom $\alpha$: u ovom kontekstu oba tumačenja daju isti rezultat;

2.  Kad je jezgra homomorfizma $\ker\varphi=(f(x))$ i $f(x)$ je nesvodiv element, vrijedi $\varphi(f(x))=f(\alpha)=0$, tj. $\alpha\in E$ je korijen polinoma $f(x)$ nad $F$. Budući da je $F$ polje, bez smanjenja općenitosti možemo pretpostaviti da je $f(x)$ normiran polinom. Tada je slika homomorfizma $\varphi$ polje $F(\alpha)$, pa vrijedi

    $$
    F[x]/(f(x))\cong F(\alpha).
    $$

    Tu se opet razlikuju dva slučaja:

    1.  Ako je $f(x)$ polinom prvog stupnja, tj. $f(x)=x-\alpha$, onda je $\alpha\in F$, pa je proširenje $F(\alpha)=F$ trivijalno;
    2.  U preostalim je slučajevima $f(x)$ nesvodiv polinom stupnja većeg od jedan i $\alpha\in E\setminus F$; tada je slika $F[\alpha]$ već polje koje sadrži $F$ i $\alpha$, pa je ona upravo $F(\alpha)$, tj. proširenje polja $F$ generirano elementom $\alpha$, i $F(\alpha)\supset F$ nije trivijalno.

Ova rasprava motivira sljedeće definicije:

???+ abstract "Algebarski i transcendentni elementi"
    Za proširenje $E/F$, ako je element $\alpha\in E$ korijen nekog nenul polinoma $f(x)$ nad $F$, kaže se da je $\alpha$ **algebarski element** (algebraic element) nad $F$; u suprotnom se kaže da je element $\alpha$ **transcendentni element** (transcendental element) nad $F$.

???+ abstract "Minimalni polinom"
    Za algebarski element $\alpha$ nad poljem $F$, normirani polinom $f(x)$ najmanjeg stupnja kojemu je $\alpha$ korijen naziva se njegov **minimalni polinom** (minimal polynomial).

Minimalni polinom ovdje je upravo nesvodivi polinom $f(x)$ iz prethodne analize. Naravno, može se i izravno dokazati da su minimalni polinomi nesvodivi. Minimalnost minimalnog polinoma $f(x)$ znači da se iz svakog polinoma nad poljem $F$ kojemu je $\alpha$ korijen nužno može izlučiti faktor $f(x)$.

???+ example "Primjeri"
    1.  $\sqrt 2$ je algebarski element nad $\mathbf Q$, s minimalnim polinomom $x^2-2$.
    2.  $\sqrt 2$ je algebarski element nad $\mathbf R$, s minimalnim polinomom $x-\sqrt 2$.
    3.  $\pi$ je transcendentni element nad $\mathbf Q$.
    4.  Općenito, algebarski elementi nad $\mathbf Q$ nazivaju se **algebarski brojevi** (algebraic number), a transcendentni elementi **transcendentni brojevi** (transcendental number). Posebno, ako je minimalni polinom algebarskog broja polinom s cjelobrojnim koeficijentima, taj se broj naziva **algebarski cijeli broj** (algebraic integer). Svi algebarski cijeli brojevi u algebarskom proširenju čine prsten. Primjerice, algebarski cijeli brojevi u kvadratnom polju $\mathbf Q(\sqrt{D})$ čine prsten kvadratnih cijelih brojeva $\mathbf Z[\omega]$. Značenje te oznake vidi na stranici [prsten kvadratnih cijelih brojeva](./ring-theory.md#例子二次整数环).

???+ abstract "Algebarska i transcendentna proširenja"
    Za proširenje $E/F$, ako su svi elementi polja $E$ algebarski nad $F$, kaže se da je polje $E$ **algebarsko proširenje** (algebraic extension) polja $F$; u suprotnom se kaže da je polje $E$ **transcendentno proširenje** (transcendental extension) polja $F$.

Rezultat jednostavnog proširenja, ovisno o svojstvima dodanog elementa, može biti dviju vrsta. Kad je dodani element transcendentan, jednostavno proširenje uvijek je izomorfno polju racionalnih funkcija. Tada nema nikakve mogućnosti daljnjeg pojednostavljivanja. No kad je dodani element algebarski, jednostavno proširenje zapravo je $F[\alpha]$, tj. rezultat izravne zamjene neodređenice $x$ u prstenu polinoma $F[x]$ elementom $\alpha$. S elementarnog gledišta, u usporedbi sa slučajem transcendentnog elementa, elementi polja proširenja tada mogu biti bez nazivnika; to znači da je u jednostavnom algebarskom proširenju uvijek izvediv postupak sličan „racionalizaciji nazivnika” iz elementarne aritmetike. Budući da su proširenja polja koja se pojavljuju u algoritamskim natjecanjima uglavnom jednostavna algebarska proširenja, u sljedećem odjeljku podrobnije ćemo razmotriti računanje u njima.

Važnost jednostavnih algebarskih proširenja odražava se i u sljedećem teoremu:

???+ note "Teorem"
    Proširenje polja konačno je ako i samo ako je konačno generirano algebarsko proširenje.

??? note "Dokaz"
    Neka je $F$ polje, a $E=F(\alpha_1,\cdots,\alpha_n)$ konačno generirano algebarsko proširenje polja, tj. svi $\alpha_i$ algebarski su elementi nad $F$. Neka je $E_i=F(\alpha_1,\cdots,\alpha_i)$; tada je $E_0=F$ i $E_n=E$. Uočimo da je $\alpha_i$ nužno algebarski element nad $E_{i-1}$, jer je minimalni polinom od $\alpha_i$ nad poljem $F$ također polinom nad $E_{i-1}$; štoviše, stupanj minimalnog polinoma od $\alpha_i$ nad $E_{i-1}$ nužno ne prelazi stupanj minimalnog polinoma od $\alpha_i$ nad poljem $F$. Stoga je $[E_i:E_{i-1}]$ nužno konačan, a prema multiplikativnosti stupnjeva proširenja polja i $[E:F]=\prod_{i=1}^n[E_i:E_{i-1}]$ je konačan. Obratno, počevši od $E_0=F$, za već konstruirano $E_i$ može se svaki put odabrati element $\alpha_{i+1}$ iz $E\setminus E_i$ i dodati ga u $E_i$, čime se dobiva polje proširenja $E_{i+1}=E_i(\alpha_{i+1})$, sve dok se ne dobije $E_n=E$. Budući da se stupanj proširenja stalno smanjuje, taj postupak nužno završava u konačno mnogo koraka. Prema tome, konačno proširenje nužno je konačno generirano algebarsko proširenje.

To znači da je za razumijevanje svojstava konačnih proširenja dovoljno razumjeti jednostavna algebarska proširenja, jer se konačno proširenje uvijek može dobiti konačno mnogo jednostavnih algebarskih proširenja.

### Struktura i računanje u jednostavnim algebarskim proširenjima

U ovom odjeljku neka je $F$ polje, $E$ njegovo polje proširenja i $\alpha\in E\setminus F$ algebarski element nad poljem $F$. Neka je minimalni polinom od $\alpha$ polinom $f(x)$, pri čemu je $f(x)$ normiran polinom stupnja $n$, tj.

$$
f(x)=x^n+a_{n-1}x^{n-1}+\cdots+a_1x+a_0,
$$

gdje su $a_0,a_1,\cdots,a_{n-1}\in F$ i $f(x)$ je nesvodiv nad $F$.

Izomorfizam $F(\alpha)\cong F[x]/(f(x))$ pokazuje da je računanje u polju proširenja $F(\alpha)$ upravo računanje s polinomima modulo $f(x)$. Prema dijeljenju polinoma s ostatkom, dovoljno je promatrati klase kongruencije svih polinoma stupnja manjeg od $n=\deg f(x)$. Prirodna baza za te polinome je $\{1,\alpha,\cdots,\alpha^{n-1}\}$. Stoga vrijedi sljedeće:

???+ note "Teorem"
    Uz pretpostavke ovog odjeljka, polje proširenja $F(\alpha)$ može se zapisati kao
    
    $$
    F(\alpha)=\{\lambda(\alpha)=\lambda_0+\lambda_1\alpha+\cdots+\lambda_{n-1}\alpha^{n-1}:\lambda_0,\lambda_1,\cdots,\lambda_{n-1}\in F\}.
    $$
    
    Pritom $\lambda(x)$ prolazi svim polinomima stupnja manjeg od $n$. Stoga je stupanj proširenja $[F(\alpha):F]=n$, tj. jednak stupnju minimalnog polinoma od $\alpha$. U polju proširenja zbrajanje elemenata $\lambda(\alpha)$ i $\mu(\alpha)$ upravo je zbrajanje polinoma, tj. zbrajanje koeficijenata na odgovarajućim mjestima; umnožak elemenata $\lambda(\alpha)$ i $\mu(\alpha)$ može se zapisati kao $\rho(\alpha)$, gdje je $\rho(x)$ ostatak pri dijeljenju umnoška $\lambda(x)\mu(x)$ polinomom $f(x)$.

Naravno, budući da je $F(\alpha)$ polje, u njemu se elementi mogu i dijeliti. Prema opisu množenja u teoremu, to odgovara rješavanju [linearne kongruencije](../number-theory/linear-equation.md) u prstenu polinoma. Analogno postupku za cijele brojeve, da bi se izračunao kvocijent $\lambda(\alpha)/\mu(\alpha)$, može se prvo odrediti multiplikativni inverz od $\mu(\alpha)$ i zatim ga pomnožiti s $\lambda(\alpha)$. Da bi se izračunao multiplikativni inverz od $\mu(\alpha)$, dovoljno je riješiti kongruenciju $\mu(x)\xi(x)\equiv 1\pmod{f(x)}$. To se može učiniti proširenim Euklidovim algoritmom.

U nastavku ćemo na nekoliko konkretnih primjera razjasniti detalje računanja.

???+ example "Primjer"
    Promotrimo polje proširenja $\mathbf Q(\alpha)$, gdje je $\alpha$ jedan korijen jednadžbe $x^3-2x-2=0$. Treba izračunati vrijednost izraza
    
    $$
    \frac{1+\alpha}{1+\alpha+\alpha^2}
    $$
    
    u tom polju.
    
    Prvi je korak izračunati inverz od $1+\alpha+\alpha^2$, tj. izračunati rješenje kongruencije
    
    $$
    (x^2+x+1)\xi(x)+(x^3-2x-2)\nu(x)=1
    $$
    
    Na nju primjenjujemo prošireni Euklidov algoritam. Najprije provedemo Euklidov algoritam uzastopnog dijeljenja, što daje sljedeći postupak:
    
    $$
    \begin{aligned}
    x^3-2x-2 &= (x-1)(x^2+x+1)+(-2x-1),\\
    x^2+x+1 &= \left(-\frac12x-\frac14\right)(-2x-1)+\frac34,\\
    -2x-1 &= \left(-\frac{8}{3}x-\frac{4}{3}\right)\frac{3}{4}.
    \end{aligned}
    $$
    
    Zatim izračunamo koeficijente u kongruenciji:
    
    $$
    \begin{aligned}
    \frac{3}{4}
    &=(x^2+x+1)+\left(\frac12x+\frac14\right)(-2x-1)\\
    &=(x^2+x+1)+\left(\frac12x+\frac14\right)\left((x^3-2x-2)-(x-1)(x^2+x+1)\right)\\
    &=\left(-\frac12x^2+\frac14x+\frac54\right)(x^2+x+1)+\left(\frac12x+\frac14\right)(x^3-2x-2).
    \end{aligned}
    $$
    
    Stoga je rješenje jednadžbe
    
    $$
    \xi(x)=-\frac23x^2+\frac13x+\frac53,\ \nu(x)=\frac23x+\frac13.
    $$
    
    To pokazuje da je inverz od $1+\alpha+\alpha^2$ jednak
    
    $$
    -\frac23\alpha^2+\frac13\alpha+\frac53.
    $$
    
    Drugi je korak izračunati umnožak inverza i $1+\alpha$. Za njega vrijedi
    
    $$
    \begin{aligned}
    (1+\alpha)\left(-\frac23\alpha^2+\frac13\alpha+\frac53\right)
    &=-\frac23\alpha^3-\frac13\alpha^2+2\alpha+\frac53\\
    &=-\frac23(2\alpha+2)-\frac13\alpha^2+2\alpha+\frac53\\
    &=-\frac13\alpha^2+\frac23\alpha+\frac13.
    \end{aligned}
    $$
    
    To je konačan odgovor.

U primjeru je upotrijebljen samo uvjet da je $\alpha$ jedan korijen jednadžbe, a nije određeno koji je to konkretan korijen. Polinom $x^3-2x-2=0$ u polju kompleksnih brojeva $\mathbf C$ ima jedan realan korijen i par konjugirano kompleksnih korijena, a polja proširenja dobivena dodavanjem bilo kojeg od njih polju racionalnih brojeva $\mathbf Q$ međusobno su izomorfna. Drugim riječima, ta tri različita korijena s algebarskog su gledišta nerazlučiva.

Općenito, za nesvodiv polinom $f(x)$ nad poljem $F$ s različitim korijenima $\alpha\neq\beta$ u polju proširenja, ti korijeni pri jednostavnom proširenju polja $F$ pokazuju ista algebarska svojstva i međusobno se nazivaju **konjugiranima** (conjugate). Uobičajena konjugacija u polju kompleksnih brojeva poseban je slučaj tog pojma za proširenje polja $\mathbf C/\mathbf R$.

???+ example "Primjer"
    Promotrimo polje proširenja $\mathbf F_2(\alpha)$, gdje je $\alpha$ jedan korijen jednadžbe $x^2+x+1=0$. Općenito, za $a+b\alpha$ i $c+d\alpha$ vrijede pravila računanja
    
    $$
    \begin{aligned}
    (a+b\alpha)+(c+d\alpha)&=(a+c)+(b+d)\alpha,\\
    (a+b\alpha)(c+d\alpha)&=ac+(ad+bc)\alpha+bd\alpha^2\\
    &=(ac+bd)+(ad+bc+bd)\alpha.
    \end{aligned}
    $$
    
    To daje pravila računanja slična onima u polju kompleksnih brojeva. Većini čitatelja takav je korijen $\alpha$ zacijelo nepoznat, ali to ne smeta računanju s elementima takvog polja. Zapravo vrijedi $[\mathbf F_2(\alpha):\mathbf F_2]=2$, pa je, kao vektorski prostor, $|\mathbf F_2(\alpha)|=4$, tj. tako je dobiveno konačno polje veličine $4$. Poslije ćemo vidjeti da se sva konačna polja konstruiraju na ovaj način.

Pri računanju manjeg opsega, računanje modulo normirani polinom $f(x)$ obično se može provesti uvrštavanjem

$$
x^n=-a_{n-1}x^{n-1}-\cdots-a_1x-a_0
$$

radi snižavanja stupnja ciljnog polinoma. Štoviše, za proširenja niskog stupnja često se pravila računanja s koeficijentima mogu izravno izračunati i upotrijebiti implementacija slična klasi kompleksnih brojeva, bez računanja ostatka pri svakom koraku.

Kao primjer jednostavnog algebarskog proširenja može poslužiti [referentna implementacija](#referentna-implementacija) konačnog polja u nastavku.

Algoritmi opisani ovdje u praksi mogu obraditi samo slučajeve relativno niskog stupnja proširenja, što je dovoljno za veliku većinu primjena u algoritamskim natjecanjima. Za slučajeve u kojima je stupanj proširenja toliko velik da postaje usko grlo složenosti, treba upotrijebiti odgovarajuće polinomske tehnike ([brzu Fourierovu transformaciju](../poly/fft.md), [brzu teorijsko-brojevnu transformaciju](../poly/ntt.md), [brzo računanje ostatka polinoma](../poly/elementary-func.md#dijeljenje-i-ostatak-polinoma), [Euklidov algoritam za polinome](../poly/intro.md#faktorizacija-i-euklidov-algoritam) itd.) za ubrzavanje računanja.

### Polje razlaganja

Prethodni tekst iscrpno je obradio strukturu jednostavnih algebarskih proširenja. No takva proširenja često nisu dovoljna:

???+ example "Primjer"
    Promotrimo proširenje $\mathbf Q(\sqrt[3]{2})/\mathbf Q$. Minimalni polinom algebarskog elementa $\sqrt[3]{2}$ nad poljem $\mathbf Q$ je $x^3-2$. U polju kompleksnih brojeva $\mathbf C$ polinom $x^3-2$ ima tri korijena, naime $\sqrt[3]{2},\sqrt[3]{2}\omega,\sqrt[3]{2}\omega^2$, gdje je $\omega=\mathrm{e}^{2\pi\mathrm{i}/3}$ primitivni treći korijen od $1$. Iako je $\mathbf Q(\sqrt[3]{2})\cong\mathbf Q(\sqrt[3]{2}\omega)\cong\mathbf Q(\sqrt[3]{2}\omega^2)$, polje $\mathbf Q(\sqrt[3]{2})$ ne sadrži druga dva korijena, pa već računanje poput $\sqrt[3]{2}+\sqrt[3]{2}\omega$ u njemu nije izvedivo. Ako se želi potpuno obuhvatiti sva tri korijena, polje $\mathbf Q(\sqrt[3]{2})$ treba dalje proširiti, i to do $\mathbf Q(\sqrt[3]{2},\sqrt[3]{2}\omega,\sqrt[3]{2}\omega^2)$.
    
    Ranije je objašnjeno da je za takvo proširenje dovoljno redom provoditi jednostavna proširenja element po element. Treba uočiti da minimalni polinom od $\sqrt[3]{2}\omega$ nad poljem $\mathbf Q$ nije isti kao nad poljem $\mathbf Q(\sqrt[3]{2})$: prvi je $x^3-2\in\mathbf Q[x]$, a drugi $x^2+\sqrt[3]{2}x+\sqrt[3]{4}\in \mathbf Q(\sqrt[3]{2})[x]$, jer vrijedi
    
    $$
    x^3-2 = (x-\sqrt[3]{2})(x^2+\sqrt[3]{2}x+\sqrt[3]{4}).
    $$
    
    Iz izvornog minimalnog polinoma nakon proširenja polja izlučuje se linearni faktor, pa je stupanj minimalnog polinoma preostalih korijena manji od stupnja minimalnog polinoma nad izvornim poljem. Postupak uzastopnog proširivanja polja upravo je postupak uzastopnog „razlaganja” polinoma. Zato pri svakom jednostavnom proširenju treba ponovno odrediti minimalni polinom.

Dodamo li polju sve korijene polinoma, dobivamo polje razlaganja tog polinoma.

???+ abstract "Razlaganje"
    Neka je $F$ polje. Ako se polinom $f(x)$ u $F[x]$ može rastaviti na umnožak linearnih faktora, kaže se da se polinom $f(x)$ **razlaže** (split) u polju $F$.

???+ abstract "Polje razlaganja"
    Za polinom $f(x)$ nad poljem $F$, ako proširenje $E/F$ zadovoljava da se $f(x)$ razlaže u polju $E$, ali se ne razlaže ni u jednom pravom potpolju polja $E$, kaže se da je polje $E$ **polje razlaganja** (splitting field) polinoma $f(x)$.

Može se dokazati da je, kao i jednostavno proširenje, polje razlaganja zadanog polinoma jednoznačno određeno do na izomorfizam i ne ovisi o konkretnom načinu konstrukcije. Polje razlaganja uvijek je konačno proširenje.

???+ abstract "Normalno proširenje"
    Za algebarsko proširenje $E/F$, ako se za svaki $\alpha\in E$ minimalni polinom od $\alpha$ razlaže u $E$, kaže se da je polje $E$ **normalno proširenje** (normal extension) polja $F$.

Normalna proširenja imaju temeljnu ulogu u Galoisovoj teoriji.

### Algebarski zatvorena polja

Većinu ranije spomenutih pojmova vezanih uz proširenja u načelu treba promatrati unutar polja većeg od samog proširenja. Iako se u slučaju jednostavnog proširenja proširenje polja može konstruirati pomoću prstena polinoma bez oslanjanja na veće polje, u općem slučaju takvog sredstva nema. Za polje racionalnih brojeva $\mathbf Q$ i polje realnih brojeva $\mathbf R$ uvijek se može pretpostaviti da su algebarska proširenja sadržana u polju kompleksnih brojeva $\mathbf C$. Za konačna polja nema sličnog poznatog polja. Zapravo, za svako polje postoji algebarski zatvarač, tako da se za sva algebarska proširenja tog polja može pretpostaviti da se nalaze unutar algebarskog zatvarača. Time je taj problem potpuno riješen.

???+ abstract "Algebarski zatvarač"
    Za polje $F$, ako je polje $\overline F$ algebarsko proširenje polja $F$ i svi se $f(x)\in F[x]$ razlažu u $\overline F$, kaže se da je polje $\overline F$ **algebarski zatvarač** (algebraic closure) polja $F$.

Algebarski zatvarač normalno je proširenje polja. Njegova se konstrukcija u osnovi sastoji od dodavanja polju korijena svih mogućih polinoma. Štoviše, kao i polje razlaganja, algebarski zatvarač nekog polja jedinstven je do na izomorfizam.

???+ note "Teorem"
    Svako polje $F$ ima algebarski zatvarač.

??? note "Dokaz"
    Teškoća dokaza dolazi iz teorije skupova. Ovdje navodimo Artinov dokaz.
    
    U prvom dijelu dokaza, polazeći od $F$, konstruira se proširenje $K_1/F$ takvo da svi polinomi nad $F$ imaju barem jedan korijen u $K_1$. Za polje $F$ promotrimo prsten polinoma u više neodređenica[^multi-poly-ring] $R=F[\cdots,x_f,\cdots]$, u kojemu indeks neodređenice $x_f$ prolazi svim normiranim polinomima nad $F$. Neka je $I$ ideal generiran svim $f(x_f)$. Najprije, $I\neq R$, pa postoji maksimalni ideal $M\supseteq I$. Naime, kad bi bilo $1\in I$, nužno bi postojalo konačno mnogo normiranih polinoma $f_i$ nad poljem $F$ i odgovarajućih elemenata $g_i$ prstena $R$ takvih da vrijedi $g_1f_1(x_{f_1})+\cdots+g_kf_k(x_{f_k})=1$. Neka je $F(\alpha_1,\cdots,\alpha_k)$ algebarsko proširenje dobiveno dodavanjem korijena $\alpha_i$ polinoma $f_i(x)$ polju $F$. Uvrstimo li u $F(\alpha_1,\cdots,\alpha_k)$ u gornji identitet $\alpha_i$ umjesto svakog $x_{f_i}$, a $0$ umjesto svih ostalih neodređenica $x_f$ koje se pojavljuju u pojedinim $g_i$, dobivamo u $F(\alpha_1,\cdots,\alpha_k)$ jednakost $0=1$, što je kontradikcija. Dakle $I\neq R$ i konstrukcija maksimalnog ideala $M$ opravdana je. Tada je kvocijentni prsten $R/M$ polje, označimo ga $K_1$, i svaki normirani polinom $f(x)$ nad $F$ ima u $K_1$ korijen $\overline{x_f}$.
    
    U drugom dijelu dokaza induktivno se dobiva algebarski zatvoreno polje $K$ (definicija je u nastavku) koje sadrži $F$. Ponavljanjem gornje konstrukcije iz polja $K_i$ može se konstruirati polje $K_{i+1}$ takvo da svi polinomi nad $K_i$ imaju u $K_{i+1}$ barem jedan korijen. Štoviše, $K_i$ se prirodno ulaže u $K_{i+1}$, pa se može definirati njihova unija $K=\bigcup_{i=1}^\infty K_i$. Lako se provjeri da je i to polje, a koeficijenti svakog polinoma nad $K$ nužno su svi sadržani u nekom $K_i$, pa se jedan njegov korijen nužno pojavljuje u $K_{i+1}\subseteq K$. To pokazuje da svi polinomi nad $K$ imaju u $K$ barem jedan korijen, pa je $K$ algebarski zatvoreno polje.
    
    Naposljetku, neka $\overline F$ označava skup svih elemenata polja $K$ koji su algebarski nad $F$. On je očito polje, jer za sve $\alpha,\beta\in\overline F$ vrijedi $\alpha\pm\beta,\alpha\beta,\alpha/\beta\in F(\alpha,\beta)\subseteq\overline F$. On je i algebarsko proširenje polja $F$, jer su svi njegovi elementi algebarski nad $F$. Za polinom $f(x)$ nad $F$ svi su njegovi korijeni algebarski nad $F$, pa su i u $\overline F$, te se stoga polinom nužno razlaže na umnožak linearnih faktora. To pokazuje da je $\overline F$ algebarski zatvarač polja $F$.

???+ example "Primjeri"
    1.  Algebarski zatvarač polja realnih brojeva $\mathbf R$ je polje kompleksnih brojeva $\mathbf C$.
    2.  Algebarski zatvarač polja racionalnih brojeva $\mathbf Q$ je skup svih algebarskih brojeva (tj. algebarskih elemenata u proširenju polja $\mathbf C/\mathbf Q$); označava se $\overline{\mathbf Q}$.

Sva algebarska proširenja algebarskog zatvarača trivijalna su. Takva se polja nazivaju algebarski zatvorenima.

???+ abstract "Algebarski zatvoreno polje"
    Ako svaki nekonstantni polinom $f(x)$ nad poljem $F$ ima barem jedan korijen $\alpha\in F$, polje $F$ naziva se **algebarski zatvoreno polje** (algebraically closed field).

Zapravo, ono ima sljedeće ekvivalentne definicije:

???+ note "Teorem"
    Za polje $F$ sljedeća su svojstva ekvivalentna:
    
    1.  Polje $F$ algebarski je zatvoreno;
    2.  Svi polinomi $f(x)$ nad poljem $F$ razlažu se;
    3.  Jedini nesvodivi polinomi nad poljem $F$ polinomi su prvog stupnja;
    4.  Polje $F$ nema netrivijalnih algebarskih proširenja;
    5.  Polje $F$ nema netrivijalnih konačnih proširenja;
    6.  Polje $F$ algebarski je zatvarač nekog polja.

??? note "Dokaz"
    Ekvivalentnost prvih pet svojstava očita je, dovoljno je pogledati definicije. Za šesto svojstvo, algebarski zatvoreno polje očito je samo sebi algebarski zatvarač, jer nema netrivijalnih algebarskih proširenja; obratno, treba dokazati da je algebarski zatvarač polja $F$ nužno algebarski zatvoreno polje. Neka je $\overline F$ algebarski zatvarač polja $F$ i neka je $f(x)$ polinom nad $\overline F$. Neka je $\alpha$ jedan korijen polinoma $f(x)$ u polju razlaganja polinoma $f(x)$ i neka je $S\subseteq\overline F$ skup nenul koeficijenata polinoma $f(x)$. Tada je, budući da je $F(S)(\alpha)=F(S\cup\{\alpha\})$ konačno proširenje, $\alpha$ nužno algebarski element nad $F$, pa se prema definiciji algebarskog zatvarača minimalni polinom od $\alpha$ nad $F$ razlaže u polju $\overline F$, odakle je $\alpha\in\overline F$. To pokazuje da svaki polinom nad $\overline F$ ima barem jedan korijen.

Naposljetku, [osnovni teorem algebre](../poly/fundamental.md) [^fundamental-algebra] kaže da je $\mathbf C$ algebarski zatvoreno polje. Nesvodivi polinomi nad poljem realnih brojeva $\mathbf R$ najviše su drugog stupnja, ili, ekvivalentno, algebarska proširenja nad njim najviše su kvadratna proširenja, upravo zato što je najveće polje koje se može dobiti algebarskim proširenjem polje $\mathbf C$.

### Separabilna proširenja

Pojam polja razlaganja jamči da za svaki polinom nad poljem postoji polje proširenja koje sadrži sve njegove korijene, a polje razlaganja precizno daje najmanje takvo polje proširenja. Svojstva polinoma i svojstva njegova polja razlaganja usko su povezana. No ako se svojstva polinoma žele proučavati pomoću njegova polja razlaganja, prvi je problem s kojim se treba suočiti to da polje razlaganja polinoma ne ovisi o kratnostima korijena polinoma. Stoga bi, ako je moguće, trebalo promatrati nekakav „najjednostavniji prikaz” polinoma. Potaknuti time, polinome koji ni u algebarskom zatvaraču polja nemaju višestrukih korijena nazivamo separabilnim polinomima.

???+ abstract "Separabilni polinom"
    Za polinom $f(x)$ nad poljem $F$, ako $f(x)$ u algebarskom zatvaraču $\overline F$ polja $F$ nema višestrukih korijena, tj. ako pri rastavu na umnožak linearnih faktora nema ponovljenih faktora, polinom $f(x)$ naziva se **separabilnim** (separable).

Budući da se rasprava uvijek vodi u algebarskom zatvaraču polja $F$, odluka o separabilnosti polinoma zapravo ne ovisi o izboru polja $F$. No budući da su koeficijenti polinoma u $F$, trebalo bi dati kriterij kojim se separabilnost polinoma može provjeriti već u polju $F$, bez eksplicitne konstrukcije polja proširenja.

Čitatelji upoznati s analizom znaju da se postojanje višestrukih korijena polinomske funkcije može provjeriti pomoću njezine derivacije: višestruki korijen polinomske funkcije korijen je i njezine derivacije. Iako polinom i polinomska funkcija nisu isti pojam, metoda provjere višestrukih korijena polinomske funkcije može se analogno prenijeti na polinome. Derivacija polinoma može se formalno definirati ovako:

???+ abstract "Formalna derivacija"
    Za polinom
    
    $$
    f(x)=a_0+a_1x+a_2x^2+\cdots+a_{n-1}x^{n-1}+a_nx^n=\sum_{i=0}^na_ix^i
    $$
    
    nad poljem $F$, njegova **(formalna) derivacija** (derivative), u oznaci $Df(x)$, definira se kao polinom
    
    $$
    Df(x)=a_1+2a_2x+\cdots+(n-1)a_{n-1}x^{n-2}+na_nx^{n-1}=\sum_{i=1}^nia_ix^{i-1}.
    $$

Ta definicija vrijedi za polinome nad svim poljima i ne ovisi ni o kakvoj topološkoj strukturi; operator derivacije $D$ ovdje samo preslikava jedan polinom u drugi. Štoviše, usporedbom koeficijenata može se provjeriti da uobičajena pravila deriviranja, poput $D(f(x)g(x))=(Df(x))g(x)+f(x)(Dg(x))$ i sl., i dalje vrijede za formalnu derivaciju.

Nadalje, da bi se provjerilo imaju li polinom $f(x)$ i njegova derivacija $Df(x)$ zajednički korijen u polju razlaganja, nije potrebno eksplicitno konstruirati to polje razlaganja, nego se to može ustanoviti pomoću njihova najvećeg zajedničkog djelitelja; naime, korijen polinoma uvijek se pojavljuje u svom minimalnom polinomu, a ponovljeni korijen znači da se i odgovarajući faktor minimalnog polinoma ponavlja. Stoga kriterij za višestruke korijene glasi ovako:

???+ note "Teorem"
    Za polinom $f(x)$ nad poljem $F$, ako $f(x)$ ima višestruki korijen $\alpha$, onda i derivacija $Df(x)$ ima isti korijen $\alpha$. Nadalje, polinom $f(x)$ separabilan je ako i samo ako su $f(x)$ i njegova derivacija $Df(x)$ relativno prosti, tj. $\gcd(f(x),Df(x))=1$.

??? note "Dokaz"
    Najprije, budući da se dijeljenje s ostatkom čuva i u polju proširenja, rezultat Euklidova algoritma ne ovisi o izboru polja proširenja, pa je dovoljno njihove zajedničke djelitelje promatrati u polju razlaganja. Neka je stoga $\alpha$ korijen od $f(x)$ kratnosti $k>1$; tada u polju razlaganja postoji rastav $f(x)=(x-\alpha)^kg(x)$, pa i njegova derivacija $Df(x)=k(x-\alpha)^{k-1}g(x)+(x-\alpha)^kDg(x)$ nužno ima korijen $\alpha$. Obratno, ako i $f(x)$ i $Df(x)$ imaju korijen $\alpha$, onda za rastav $f(x)=(x-\alpha)g(x)$ u polju razlaganja vrijedi $Df(x)=(x-\alpha)Dg(x)+g(x)$, pa je $\alpha$ korijen i od $g(x)$, dakle $\alpha$ je višestruki korijen od $f(x)$. Time je dokazan prvi dio teorema. Nadalje, to da polinom $f(x)$ ima višestruki korijen $\alpha$ ekvivalentno je tome da je $x-\alpha$ faktor od $\gcd(f(x),Df(x))$. Stoga je to da polinom $f(x)$ nije separabilan ekvivalentno tome da je stupanj od $\gcd(f(x),Df(x))$ barem jedan.

Polinom nad poljem uvijek se može rastaviti na umnožak nekoliko nesvodivih polinoma. Budući da (do na asociranost) različiti nesvodivi polinomi uvijek imaju različite korijene, ponavljanje korijena prirodno je povezano s ponavljanjem odgovarajućih polinomskih faktora. Može li se onda iz toga da u rastavu polinoma nema ponovljenih nesvodivih faktora zaključiti da je polinom separabilan? Drugim riječima, jesu li svi nesvodivi polinomi separabilni? Nažalost, u općem slučaju odgovor nije pozitivan. Problem se pojavljuje u poljima konačne karakteristike.

Za nesvodiv polinom $f(x)$ nad poljem $F$, polinom $\gcd(f(x),Df(x))$, kao faktor od $f(x)$, može biti samo dvojak: $1$ ili $f(x)$. U prvom je slučaju polinom $f(x)$ očito separabilan; problem se pojavljuje u drugom slučaju. No budući da definicija derivacije već jamči $Df(x)=0$ ili $\deg Df(x)<\deg f(x)$, to da je $f(x)$ faktor od $Df(x)$ može značiti samo $Df(x)=0$. To je u poljima konačne karakteristike moguće.

Za polje $F$ karakteristike $p$, ako je $Df(x)=0$, svi nenul koeficijenti polinoma mogu se pojaviti samo uz članove čiji je stupanj višekratnik od $p$, tj. polinom $f(x)$ može se zapisati kao

$$
f(x)=a_0+a_px^p+a_{2p}x^{2p}+\cdots+a_{(k-1)p}x^{(k-1)p}+a_{kp}x^{kp}.
$$

Ako doista postoji polinom $f(x)$ nad poljem $F$ koji je nesvodiv i nije separabilan, on može imati samo ovaj oblik. No ako svi elementi polja $F$ uvijek imaju $p$-ti korijen, tj. ako za svaki koeficijent $a_{jp}$ postoji $b_j\in F$ takav da se $a_{jp}$ može zapisati u obliku $b_j^p$, onda prema Frobeniusovu endomorfizmu uvijek vrijedi

$$
\begin{aligned}
f(x)&=a_0+a_px^p+a_{2p}x^{2p}+\cdots+a_{(k-1)p}x^{(k-1)p}+a_{kp}x^{kp}\\
&=b_0^p+b_1^px^p+b_2^px^{2p}+\cdots+b_{k-1}^px^{(k-1)p}+b_k^px^{kp}\\
&=\left(b_0+b_1x+b_2x^2+\cdots+b_{k-1}x^{k-1}+b_kx^k\right)^p.
\end{aligned}
$$

Stoga nad takvim poljem $F$ ne postoje nesvodivi polinomi tog oblika. Prema tome, nad takvim poljem svi su nesvodivi polinomi separabilni. Takva se polja nazivaju perfektnim poljima.

???+ abstract "Perfektno polje"
    Ako su svi nesvodivi polinomi nad poljem $F$ separabilni polinomi, ono se naziva **perfektno polje** (perfect field).

Za perfektna polja pojam separabilnog polinoma podudara se s pojmom polinoma bez kvadratnih faktora u jedinstvenoj faktorizaciji.

???+ note "Teorem"
    Neka je polje $F$ perfektno. Tada je polinom nad $F$ separabilan ako i samo ako se može zapisati kao umnožak nekoliko (do na asociranost) različitih nesvodivih polinoma.

Rasprava u ovom odjeljku zapravo je već dovoljna da se dobije postupak uklanjanja ponovljenih faktora iz polinoma, što je ključni korak u algoritmima za faktorizaciju polinoma. No to prelazi okvire ovog članka; zainteresirani čitatelji mogu pogledati literaturu navedenu na kraju.

Ova rasprava zapravo daje i karakterizaciju perfektnih polja:

???+ note "Teorem"
    Polje $F$ perfektno je ako i samo ako je karakteristika polja $F$ nula, ili je karakteristika polja $F$ jednaka $p$ i svaki element $x\in F$ ima $p$-ti korijen (tj. Frobeniusov endomorfizam ujedno je automorfizam).

Polje racionalnih brojeva $\mathbf Q$ i konačna polja $\mathbf F_q$ o kojima će biti riječi u nastavku perfektna su polja.

Kad polje nije perfektno, doista postoje nesvodivi polinomi koji nisu separabilni.

??? example "Primjer"
    Promotrimo polinom $x^2-t$ nad poljem racionalnih funkcija $\mathbf F_2(t)$ polja $\mathbf F_2$. Budući da je $\mathbf F_2(t)$ polje razlomaka faktorijalnog prstena $\mathbf F_2[t]$ i $t$ je prost element u $\mathbf F_2[t]$, primjenom Eisensteinova kriterija na prost element $t$ dobiva se da je $x^2-t$ nesvodiv u $\mathbf F_2[t]$, pa je nesvodiv i u $\mathbf F_2(t)$. No njegova je derivacija $0$, pa $x^2-t$ nije separabilan. Zapravo, u polju proširenja $\mathbf F_2(t)(\sqrt t)$ on ima dvostruki korijen $\sqrt t$.

Vratimo se naposljetku raspravi o proširenjima polja.

???+ abstract "Separabilno proširenje"
    Za algebarsko proširenje $E/F$, ako je za svaki $\alpha\in E$ minimalni polinom od $\alpha$ separabilan polinom, kaže se da je polje $E$ **separabilno proširenje** (separable extension) polja $F$.

Sva algebarska proširenja perfektnog polja separabilna su proširenja. To se također može uzeti kao ekvivalentna definicija perfektnog polja.

Ako je algebarsko proširenje i normalno i separabilno, naziva se i Galoisovim proširenjem. U Galoisovu proširenju nijedan nesvodiv polinom nema višestrukih korijena, a broj korijena točno je jednak stupnju polinoma, pa permutacije korijena potpuno odražavaju svojstva proširenja polja i polinoma. Takva proširenja temelj su na kojem se gradi Galoisova teorija. Zainteresirani čitatelji mogu pogledati literaturu navedenu na kraju.

## Ciklotomska polja

Kao jednostavan primjer proširenja polja, u ovom odjeljku razmatramo ciklotomska polja. Drugi jednostavan primjer proširenja polja su [kvadratna polja](../number-theory/quadratic.md).

### Grupa korijena jedinice

U polju kompleksnih brojeva $\mathbf C$ korijeni polinoma $x^n-1$ nazivaju se **$n$-ti korijeni jedinice** ($n$-th root of unity). Označimo $\zeta_n=\mathrm{e}^{2\pi\mathrm{i}/n}$. Tada je skup svih $n$-tih korijena jedinice $C_n=\{\zeta_n^k:k\in\mathbf Z\}$. S obzirom na množenje, $C_n$ čini cikličku grupu reda $n$, koja se može označiti $\langle\zeta_n\rangle$ i naziva se grupa $n$-tih korijena jedinice. Generatori grupe $C_n$, tj. elementi čiji je red točno $n$, nazivaju se **primitivni $n$-ti korijeni jedinice** (primitive $n$-th root of unity). Skup primitivnih $n$-tih korijena jedinice $P_n=\{\zeta_n^k:k\in\mathbf Z,k\perp n\}$ ima točno $\varphi(n)$ elemenata, gdje je $\varphi(n)$ [Eulerova funkcija](../number-theory/euler-totient.md). Razvrstaju li se elementi grupe korijena jedinice $C_n$ prema njihovu redu, dobiva se sljedeći rastav:

$$
C_n=\bigcup_{d|n}P_d.
$$

Prebrojavanjem elemenata na obje strane dobiva se identitet $n=\sum_{d\mid n}\varphi(d)$.

### Ciklotomsko polje

Ciklotomsko polje jest polje proširenja dobiveno dodavanjem korijena jedinice polju racionalnih brojeva.

???+ abstract "Ciklotomsko polje"
    Polje proširenja $\mathbf Q(\zeta_n)$ dobiveno dodavanjem $n$-tog kompleksnog korijena jedinice $\zeta_n=\mathrm{e}^{2\pi\mathrm{i}/n}$ polju racionalnih brojeva $\mathbf Q$ naziva se **$n$-to ciklotomsko polje** ($n$-th cyclotomic field).

Budući da svi $n$-ti korijeni jedinice s obzirom na množenje čine cikličku grupu $\langle\zeta_n\rangle$, ciklotomsko polje $\mathbf Q(\zeta_n)$ sadrži i sve te $n$-te korijene jedinice. Zapravo, $\mathbf Q(\zeta_n)$ upravo je polje razlaganja polinoma $x^n-1$ nad poljem $\mathbf Q$.

???+ note "Teorem"
    Ciklotomsko polje $\mathbf Q(\zeta_n)$ polje je razlaganja polinoma $x^n-1$ nad poljem racionalnih brojeva $\mathbf Q$.

??? note "Dokaz"
    Neka je $F$ polje razlaganja polinoma $x^n-1$ nad poljem racionalnih brojeva $\mathbf Q$. Budući da $\mathbf Q(\zeta_n)$ sadrži sve kompleksne korijene polinoma $x^n-1$, vrijedi $F\subseteq\mathbf Q(\zeta_n)$. Obratno, budući da je $\zeta_n\in F$, nužno je $\mathbf Q(\zeta_n)=F$. To pokazuje $F=\mathbf Q(\zeta_n)$.

To se može uzeti kao ekvivalentna definicija ciklotomskog polja. Zapravo, dodavanjem bilo kojeg primitivnog $n$-tog korijena jedinice polju racionalnih brojeva dobiva se $\mathbf Q(\zeta_n)$.

### Ciklotomski polinomi

Ciklotomsko polje $\mathbf Q(\zeta_n)$ jednostavno je algebarsko proširenje polja racionalnih brojeva $\mathbf Q$. Prema prethodnoj analizi, takvo je polje uvijek izomorfno kvocijentnom prstenu nekog prstena polinoma. Da bi se dobio taj izomorfizam, treba analizirati minimalni polinom $f(x)$ od $\zeta_n$. Budući da je $\zeta_n$ korijen od $x^n-1$, $f(x)$ je nužno neki faktor od $x^n-1$. To znači da treba promotriti faktorizaciju polinoma $x^n-1$ u $\mathbf Q[x]$. Prema Gaussovoj lemi, on se nužno može u $\mathbf Z[x]$ rastaviti na umnožak nekoliko nesvodivih normiranih polinoma.

Budući da je $\mathbf Q(\zeta_n)$ polje razlaganja, polinom $x^n-1$ ima rastav:

$$
x^n-1=\prod_{\zeta\in C_n}(x-\zeta)=\prod_{d\mid n}\prod_{\zeta\in P_d}(x-\zeta).
$$

Budući da korijeni jedinice različitih redova imaju različita algebarska svojstva, oni zasigurno nisu korijeni istog nesvodivog polinoma. Stoga je za proučavanje minimalnog polinoma od $\zeta_n$ dovoljno promotriti faktor

$$
\Phi_n(x)=\prod_{\zeta\in P_n}(x-\zeta)
$$

iz gornjeg rastava. Minimalni polinom korijena jedinice $\zeta_n$ nužno je faktor od $\Phi_n(x)$. Štoviše, tako definiran $\Phi_n(x)$ ima sljedeće svojstvo:

???+ note "Teorem"
    $\Phi_n(x)$ je normiran polinom s cjelobrojnim koeficijentima i nesvodiv je u $\mathbf Z[x]$.

??? note "Dokaz"
    Po definiciji je $\Phi_n(x)$ očito normiran polinom. Najprije treba dokazati da je $\Phi_n(x)\in\mathbf Z[x]$. Prema Gaussovoj lemi, polinom $x^n-1$ ima isti rastav u $\mathbf Z[x]$ i u $\mathbf Q[x]$, a svaki je faktor normiran polinom s cjelobrojnim koeficijentima. U tom je rastavu svaki faktor $f(x)$ nesvodiv u $\mathbf Q[x]$ i razlaže se u $\mathbf Q(\zeta_n)$; svi su njegovi korijeni $n$-ti korijeni jedinice i nužno imaju isti red, pa ti korijeni nužno svi pripadaju jednom te istom $P_d$, a ne mogu biti raspodijeljeni po različitim $P_d$. To znači da je svaki faktor $f(x)$ faktor nekog $\Phi_d(x)$. Stoga se $\Phi_n(x)$ može zapisati kao umnožak nekoliko normiranih polinoma s cjelobrojnim koeficijentima, pa je nužno i sam normiran polinom s cjelobrojnim koeficijentima.
    
    Zatim treba dokazati da je $\Phi_n(x)$ nesvodiv u $\mathbf Z[x]$. Neka ima rastav $f(x)g(x)$, pri čemu je $f(x)$ nesvodiv u $\mathbf Z[x]$; tada je dovoljno dokazati da $f(x)$ sadrži sve primitivne $n$-te korijene jedinice. Drugim riječima, neka je $\zeta$ jedan korijen od $f(x)$; treba dokazati da je za sve $k\perp n$ i $\zeta^k$ korijen od $f(x)$. Budući da se $k$ uvijek može rastaviti na umnožak prostih brojeva, dovoljno je dokazati da je za sve proste brojeve $p\perp n$ i $\zeta^p$ korijen od $f(x)$. Pretpostavimo suprotno, da je $\zeta^p$ korijen od $g(x)$. Tada je $\zeta$ zajednički korijen polinoma $f(x)$ i $g(x^p)$ iz $\mathbf Z[x]$. Budući da je $f(x)$ minimalni polinom od $\zeta$ nad $\mathbf Q$, nužno $f(x)$ dijeli $g(x^p)$; tj. postoji $h(x)\in\mathbf Z[x]$ takav da je $g(x^p)=f(x)h(x)$. Reduciramo li obje strane jednakosti modulo $p$, dobivamo jednakost $\overline{g}(x^p)=\overline{f}(x)\overline{h}(x)$ u $\mathbf F_p[x]$. Pomoću Frobeniusova endomorfizma zaključujemo $\overline{g}(x)^p=\overline{f}(x)\overline{h}(x)$. Budući da je i $\mathbf F_p[x]$ faktorijalni prsten, $\overline{g}(x)$ i $\overline{f}(x)$ nužno imaju netrivijalan zajednički faktor, pa $x^n-\overline 1=\overline{f}(x)\overline{g}(x)$ nije separabilan nad $\mathbf F_p$. No budući da je $p\perp n$, njegova formalna derivacija $nx^{n-1}$ relativno je prosta s njim samim, što je u kontradikciji s tim da nije separabilan. Stoga je dokazano da je $\zeta^p$ nužno također korijen od $f(x)$, pa $f(x)$ sadrži sve primitivne $n$-te korijene jedinice i upravo je $\Phi_n(x)$.

To pokazuje da je on upravo minimalni polinom od $\zeta_n$; naziva se i **$n$-ti ciklotomski polinom** ($n$-th cyclotomic polynomial). Gornja definicijska formula pokazuje da on ima $\varphi(n)$ kompleksnih korijena i da su ti kompleksni korijeni upravo svi primitivni $n$-ti korijeni jedinice, gdje je $\varphi(n)$ [Eulerova funkcija](../number-theory/euler-totient.md). To također pokazuje da je $\mathbf Q(\zeta_n)/\mathbf Q$ proširenje stupnja $\varphi(n)$.

Prsten algebarskih cijelih brojeva u ciklotomskom polju $\mathbf Q(\zeta_n)$ je $\mathbf Z[\zeta_n]$. Osim toga, kad je $\varphi(n)=2$, ciklotomsko polje je [kvadratno proširenje](../number-theory/quadratic.md). Konkretno, $\mathbf Q(\zeta_4)$ je kvadratno polje $\mathbf Q(\sqrt{-1})$; $\mathbf Q(\zeta_3)$ i $\mathbf Q(\zeta_6)$ podudaraju se i oba su kvadratno polje $\mathbf Q(\sqrt{-3})$.

Pomoću ciklotomskih polinoma polinom $x^n-1$ ima u $\mathbf Z[x]$ jedinstvenu faktorizaciju

$$
x^n-1=\prod_{d\mid n}\Phi_d(x).
$$

Stoga $(x^d-1)\mid(x^n-1)$ ako i samo ako $d\mid n$. Štoviše, primjenom [Möbiusove inverzije](../number-theory/mobius.md) na tu formulu dobiva se

$$
\Phi_n(x)=\prod_{d\mid n}(x^d-1)^{\mu(n/d)}.
$$

Pomoću tog izraza mogu se rekurzivno izračunati svi ciklotomski polinomi. Ovdje su radi upoznavanja navedeni primjeri prvih nekoliko ciklotomskih polinoma.

???+ example "Ciklotomski polinomi"
    Prvih $10$ ciklotomskih polinoma glasi:
    
    $$
    \begin{aligned}
    \Phi_1(x) &= x-1,\\
    \Phi_2(x) &= x+1,\\
    \Phi_3(x) &= x^2+x+1,\\
    \Phi_4(x) &= x^2+1,\\
    \Phi_5(x) &= x^4+x^3+x^2+x+1,\\
    \Phi_6(x) &= x^2-x+1,\\
    \Phi_7(x) &= x^6+x^5+x^4+x^3+x^2+x+1,\\
    \Phi_8(x) &= x^4+1,\\
    \Phi_9(x) &= x^6+x^3+1,\\
    \Phi_{10}(x) &= x^4-x^3+x^2-x+1.
    \end{aligned}
    $$
    
    Zanimljivo je da, iako se čini da koeficijenti ciklotomskih polinoma mogu biti samo $0$ i $\pm1$, za općenit $n$ to ne vrijedi. Prvi se protuprimjer pojavljuje kod $\Phi_{105}(x)$, a može se dokazati da s rastom $n$ koeficijenti mogu poprimiti po volji velike vrijednosti.

Pomoću gornje Möbiusove inverzijske formule mogu se izvesti sljedeća svojstva koja pojednostavljuju računanje $\Phi_n(x)$:

???+ note "Svojstva"
    Za ciklotomski polinom $\Phi_n(x)$ vrijedi:
    
    1.  Za prost $p\mid n$ vrijedi $\Phi_{pn}(x)=\Phi_n(x^p)$;
    2.  Za prost $p\perp n$ vrijedi $\Phi_{pn}(x)=\dfrac{\Phi_n(x^p)}{\Phi_n(x)}$;
    3.  Posebno, ako je $n>1$ neparan, onda je $\Phi_{2n}(x)=\Phi_n(-x)$;
    4.  Za prost broj $p$ vrijedi $\Phi_{p}(x)=1+x+\cdots+x^{p-1}$;
    5.  Posebno, $\Phi_{2^k}(x)=x^{2^{k-1}}+1$.

Ta svojstva pokazuju da je pri računanju ciklotomskih polinoma težište na slučaju kad je indeks neparan broj bez kvadratnih faktora. U tom se slučaju proste faktore može dodavati jedan po jedan pomoću drugog svojstva; za dodavanje svakog prostog faktora potrebno je samo jedno dijeljenje polinoma.

Ciklotomski polinomi imaju još mnogo drugih svojstava.

???+ note "Teorem"
    Neka je $\Phi_n(x)$ ciklotomski polinom reda $n>1$ i neka je njegov stupanj $\varphi(n)$. Tada vrijedi:
    
    1.  Polinom $\Phi_n(x)$ palindromni je polinom: koeficijent uz član stupnja $j$ jednak je koeficijentu uz član stupnja $\varphi(n)-j$, tj. $\Phi_n(x)=x^{\varphi(n)}\Phi_n(1/x)$;
    2.  Koeficijent polinoma uz član stupnja $\varphi(n)-1$ jednak je Möbiusovoj funkciji $-\mu(n)$;
    3.  Ako je $n$ potencija prostog broja $p^k$, onda je $\Phi_n(1)=p$; u suprotnom je $\Phi_n(1)=1$;
    4.  Neka je $b>1$ i $p$ prost faktor od $\Phi_n(b)$. Tada $p\mid n$ ili je $n$ red elementa $b$ u multiplikativnoj grupi $(\mathbf Z/p\mathbf Z)^\times$, a ta se dva slučaja ne mogu dogoditi istodobno.

??? note "Dokaz"
    Za prva tri svojstva dovoljno je upotrijebiti Möbiusovu inverziju. Za 1 izravno promotrimo Möbiusov inverzijski oblik od $\Phi_n(x)$, tj. $\Phi_n(x)=\prod_{d\mid n}(x^d-1)^{\mu(n/d)}$; za 2 označimo koeficijent od $\Phi_n(x)$ uz član stupnja $\varphi(n)-1$ s $f(n)$; usporedbom koeficijenata uz član stupnja $n-1$ na objema stranama jednakosti $x^n-1=\prod_{d\mid n}\Phi_d(x)$ dobivamo $\sum_{d\mid n}f(d)=-[n=1]$, a zatim primijenimo Möbiusovu inverziju; za 3 obje strane jednakosti $x^n-1=\prod_{d\mid n}\Phi_d(x)$ podijelimo s $\Phi_1(x)=x-1$ i uvrstimo $x=1$, čime dobivamo $n=\prod_{d\mid n,d\neq 1}\Phi_d(1)$, a zatim primijenimo Möbiusovu inverziju.
    
    Dokažimo sada četvrto svojstvo. Najprije, ako je $n$ red elementa $b$ u multiplikativnoj grupi $(\mathbf Z/p\mathbf Z)^\times$, onda je $n$ najmanji prirodan broj za koji $p\mid b^n-1$, pa $p\mid\Phi_n(b)$. Obratno, ako $p\mid\Phi_n(b)$, onda je $b^n\equiv 1\pmod p$; no ako $n$ nije red elementa $b$ u multiplikativnoj grupi $(\mathbf Z/p\mathbf Z)^\times$, označimo taj red s $k$; nužno je $k\mid n$ i $p\mid\Phi_k(b)$. Tada $\Phi_k(x)$ i $\Phi_n(x)$ imaju u polju $\mathbf F_p$ zajednički korijen $b$, što znači da $x^n-1$ ima višestruki korijen $b$. To pokazuje $p\mid n$; inače bi $x^n-1$ bio relativno prost sa svojom derivacijom, dakle separabilan nad $\mathbf F_p$, pa ne bi mogao imati višestrukih korijena. Prema tome, za prost faktor $p$ od $\Phi_n(b)$ postoje samo dvije mogućnosti: $p\mid n$ ili je $n$ red elementa $b$ u multiplikativnoj grupi $(\mathbf Z/p\mathbf Z)^\times$. Ta se dva slučaja međusobno isključuju, jer drugi povlači $n\mid p-1$.

Ciklotomski polinomi mogu se upotrijebiti i za rješavanje nekih problema iz teorije brojeva i algebre. Primjerice, duljina perioda zapisa razlomka u nekoj bazi usko je povezana s ciklotomskim polinomima. Za te konkretne primjene zainteresirani čitatelji mogu pogledati literaturu na kraju članka.

## Konačna polja

**Konačno polje** (finite field), koje se naziva i **Galoisovo polje** (Galois field), polje je sa samo konačno mnogo elemenata. Struktura konačnog polja jednoznačno je određena brojem njegovih elemenata, a broj elemenata nužno je potencija prostog broja.

???+ note "Teorem"
    Polje veličine $q$ postoji ako i samo ako je $q$ oblika $p^n$, tj. potencija prostog broja. Štoviše, takvo je polje jedinstveno do na izomorfizam i označava se $\mathbf F_q$. Prost broj $p$ karakteristika je polja $\mathbf F_q$, a prirodan broj $n$ stupanj je proširenja polja $\mathbf F_q/\mathbf F_p$. Naposljetku, $\mathbf F_q$ je polje razlaganja polinoma $x^q-x$ nad $\mathbf F_p$ i sadrži točno $q$ međusobno različitih korijena polinoma $x^q-x$.

??? note "Dokaz"
    Neka je polje $F$ konačno. Karakteristika polja $F$ nužno je konačna; označimo je $p$. Stoga polje $F$ ima prosto potpolje $\mathbf F_p$. Štoviše, polje $F$ nužno je konačno proširenje polja $\mathbf F_p$; označimo stupanj proširenja s $n$. Kao $n$-dimenzionalni vektorski prostor nad $\mathbf F_p$, polje $F$ ima $q=p^n$ elemenata. Svi nenul elementi polja $F$ čine grupu $F^\times$ reda $q-1$, pa vrijedi $x^{q-1}=1$. Stoga svi elementi od $F=F^\times\cup\{0\}$ zadovoljavaju $x^q=x$, tj. oni su $q$ međusobno različitih korijena polinoma $x^q-x$. Prema tome, u polju $F$ polinom $x^q-x$ ima faktor $\prod_{\alpha\in F}(x-\alpha)$, no stupanj je tog faktora već $q$, a vodeći koeficijent jednak je $1$, pa vrijedi $x^q-x=\prod_{\alpha\in F}(x-\alpha)$. To pokazuje da se $x^q-x$ razlaže u $F$. Svako polje u kojem se $x^q-x$ razlaže, budući da $x^q-x$ ima $q$ različitih korijena, nužno ima barem $q$ elemenata. To pokazuje da je $F$ najmanje polje u kojem se $x^q-x$ razlaže, tj. polje razlaganja od $x^q-x$. Ukratko, konačno polje veličine $q$ nužno je polje razlaganja polinoma $x^q-x$ nad svojim prostim potpoljem. Budući da je polje razlaganja jedinstveno do na izomorfizam, polje veličine $q$ nužno je također jedinstveno.
    
    Obratno, za zadani prost broj $p$ i njegovu potenciju $q=p^n$ treba pokazati da polje razlaganja polinoma $x^q-x$ nad $\mathbf F_p$ ima točno $q$ elemenata; time se pokazuje da postoje polja reda $q$ za sve potencije prostih brojeva. Budući da polje razlaganja polinoma $x^q-x$ nad $\mathbf F_p$ uvijek postoji, neka je $F$ skup svih korijena polinoma $x^q-x$ u tom polju razlaganja. Treba dokazati da je $F$ polje, pa je onda ono upravo samo polje razlaganja polinoma $x^q-x$. No iteriranjem Frobeniusova endomorfizma $n$ puta vidi se da je i $x\mapsto x^q$ endomorfizam, pa za sve $\alpha,\beta\in F$ vrijedi $(\alpha\pm\beta)^q=\alpha^q\pm\beta^q$, $(\alpha\beta)^q=\alpha^q\beta^q$ i $(\alpha^{-1})^q=(\alpha^q)^{-1}$. Stoga je skup $F$ zatvoren na zbrajanje, oduzimanje, množenje i dijeljenje, pa je polje. To pokazuje da je $F$ upravo polje razlaganja polinoma $x^q-x$ nad $\mathbf F_p$.

???+ note "Korolar"
    U konačnom polju $\mathbf F_q$ ($q>2$) zbroj svih nenul elemenata jednak je $0$, a umnožak $-1$.

??? note "Dokaz"
    Svi nenul elementi konačnog polja upravo su $q-1$ korijena polinoma $x^{q-1}-1$; dovoljno je primijeniti Vièteove formule.

U prostom polju $\mathbf F_p$ tvrdnja ovog korolara o umnošku upravo je (dio) [Wilsonova teorema](../number-theory/factorial.md#wilsonov-teorem) iz teorije brojeva.

### Multiplikativna struktura

Multiplikativna grupa $\mathbf F_q^\times=\mathbf F_q\setminus\{0\}$ konačnog polja uvijek je ciklička grupa.

???+ note "Teorem"
    Svaka konačna podgrupa multiplikativne grupe polja $F$ ciklička je grupa.

??? note "Dokaz"
    Neka je $G$ podgrupa multiplikativne grupe polja $F$ i $|G|=n$. Tada je $G$ konačna Abelova grupa. Prema osnovnom teoremu o konačnim Abelovim grupama, grupa $G$ ima rastav na invarijantne faktore $C_{n_1}\times\cdots\times C_{n_s}$ uz $n_1\mid\cdots\mid n_s$. Stoga za sve elemente $x$ grupe $G$ vrijedi $x^{n_s}=1$. Drugim riječima, svi su elementi grupe $G$ korijeni polinoma $x^{n_s}-1$ nad poljem $F$. No polinom $x^{n_s}-1$ ima najviše $n_s$ različitih korijena, tj. $n\le n_s$. No $n_s\le n$, pa je zapravo $n_s=n$. To pokazuje $G\cong C_{n_s}$, tj. grupa $G$ ciklička je.

???+ note "Korolar"
    Za multiplikativnu grupu konačnog polja $\mathbf F_q$ vrijedi $\mathbf F_q^\times\cong C_{q-1}$.

Ciklička grupa $\mathbf F_q^\times$ ima $\varphi(q-1)$ generatora, koji se nazivaju primitivnim elementima konačnog polja; pritom je $\varphi(n)$ [Eulerova funkcija](../number-theory/euler-totient.md).

???+ abstract "Primitivni element"
    Generator multiplikativne grupe konačnog polja $\mathbf F_q$ naziva se **primitivni element** (primitive element) polja $\mathbf F_q$.

??? warning "Primitivni element jednostavnog proširenja i primitivni element konačnog polja nisu isto"
    Iako se primitivni element jednostavnog proširenja i primitivni element konačnog polja jednako nazivaju, to nije isto. Primitivni element jednostavnog proširenja generator je odgovarajućeg jednostavnog proširenja, dok je primitivni element konačnog polja generator odgovarajuće multiplikativne grupe (kao cikličke grupe). Primitivni element konačnog polja kao jednostavnog proširenja svog prostog potpolja ne mora biti primitivni element samog konačnog polja. Primjerice, u $\mathbf F_{25}\cong\mathbf F_5[x]/(x^2+x+1)$ element $\overline x$ primitivni je element proširenja polja, ali nije primitivni element polja $\mathbf F_{25}$, jer je njegov red $3$.

??? warning "Primitivni element u $\mathbf F_{q}$ i primitivni korijen modulo $q$ također nisu isto"
    Za konačno polje $\mathbf F_{q}$ neparne karakteristike uvijek postoji [primitivni korijen](./ring-theory.md#应用整数同余类的乘法群) (primitive root) modulo $q$. No ne treba ga miješati s primitivnim elementom (primitive element) konačnog polja $\mathbf F_{q}$. Iako su oba generatori odgovarajuće multiplikativne strukture promatrane kao cikličke grupe, $(\mathbf Z/q\mathbf Z)^\times$ i $\mathbf F_q$ nisu isto kad $q$ sam nije prost broj. Primjerice, red prve grupe je $\varphi(q)$, a druge $q-1$, pa se već veličine tih dviju multiplikativnih grupa razlikuju.

Neka je $\alpha$ primitivni element konačnog polja $\mathbf F_q$. Tada za svaki nenul element $x\in\mathbf F_q^\times$ postoji jedinstven prirodan broj $k<q-1$ takav da je $x=\alpha^k$; taj se $k$ naziva **diskretni logaritam** (discrete logarithm) elementa $x$ iz $\mathbf F_q$ s obzirom na bazu $\alpha$. Kao i u slučaju $\mathbf F_p$, [algoritmi za diskretni logaritam](../number-theory/discrete-logarithm.md) razmjerno su visoke složenosti.

Množenjem primitivni element već generira sve nenul elemente polja. To pokazuje da je konačno polje, kao proširenje svojih potpolja, uvijek jednostavno proširenje.

???+ note "Teorem"
    Za konačno polje $\mathbf F_q$, neka je $F$ potpolje polja $\mathbf F_q$. Tada je $\mathbf F_q$ jednostavno algebarsko proširenje polja $F$; nadalje, neka je $\alpha$ primitivni element polja $\mathbf F_q$; tada je $\mathbf F_q=F(\alpha)$.

Minimalni polinom primitivnog elementa nesvodiv je polinom nad potpoljem konačnog polja.

### Odnosi sadržavanja

Potpolja konačnog polja također su konačna polja. Odnosi sadržavanja među konačnim poljima također su potpuno određeni njihovim redovima.

???+ note "Teorem"
    Neka su $\mathbf F_q$ i $\mathbf F_r$ konačna polja. Tada je $\mathbf F_r$ potpolje polja $\mathbf F_q$ ako i samo ako postoji $k$ takav da je $q=r^k$. Drugim riječima, $\mathbf F_{p^d}$ je potpolje polja $\mathbf F_{p^n}$ ako i samo ako $d\mid n$.

??? note "Dokaz"
    Ako je $\mathbf F_r$ potpolje polja $\mathbf F_q$, onda oba nužno imaju istu karakteristiku $p$. Proširenja polja $\mathbf F_q/\mathbf F_r$, $\mathbf F_r/\mathbf F_p$ i $\mathbf F_q/\mathbf F_p$ sva su jednostavna algebarska proširenja; označimo njihove stupnjeve redom $k,d,n$. Tada stupnjevi nužno zadovoljavaju $n=kd$. Štoviše, $r=p^d$ i $q=p^n$, pa vrijedi $q=p^n=p^{kd}=(p^d)^k=r^k$.
    
    Obratno, treba dokazati da je za sve $d\mid n$ polje $\mathbf F_{p^d}$ potpolje polja $\mathbf F_{p^n}$. Označimo $r=p^d$ i $q=p^n$. Neka je $F$ skup svih korijena jednadžbe $x^r-x=0$ u konačnom polju $\mathbf F_q$. Pomoću Frobeniusova endomorfizma može se dokazati da skup $F$ nužno čini polje; ključno je dokazati da takvih korijena ima točno $r$, jer tek tada vrijedi $F\cong\mathbf F_r$. Budući da $d\mid n$, vrijedi $(p^d-1)\mid(p^n-1)$, pa $(x^{p^d-1}-1)\mid(x^{p^n-1}-1)$, tj. $(x^r-x)\mid (x^q-x)$. Stoga se $x^r-x$ razlaže nad $\mathbf F_q$, pa u $\mathbf F_q$ ima $r$ različitih korijena. To pokazuje da je $F\cong\mathbf F_r$ potpolje polja $\mathbf F_q$.

Ovaj teorem pokazuje da odnosi sadržavanja među konačnim poljima $\mathbf F_{p^n}$ odgovaraju odnosima djeljivosti među eksponentima $n$ u redu polja $p^n$. Rešetka koju čine sva konačna polja $\mathbf F_{p^n}$ karakteristike $p$ izomorfna je rešetki koju čine prirodni brojevi $n$ s obzirom na relaciju djeljivosti. Naravno, da bi operacije kao što je presjek konačnih polja $\mathbf F_{p^n}$ imale smisla, sva polja karakteristike $p$ treba uložiti u algebarski zatvarač polja $\mathbf F_p$.

???+ note "Teorem"
    Neka je $F$ algebarski zatvarač polja $\mathbf F_p$. Tada skup korijena polinoma $x^{p^n}-x$ u polju $F$ čini konačno polje $\mathbf F_{p^n}$. Vrijedi:
    
    1.  $F=\bigcup_{n=1}^\infty\mathbf F_{p^n}$, tj. algebarski zatvarač polja $\mathbf F_p$ unija je svih konačnih polja karakteristike $p$;
    2.  Rešetka koju sva konačna polja $\mathbf F_{p^n}$ karakteristike $p$ čine s obzirom na sadržavanje izomorfna je rešetki koju prirodni brojevi $n$ čine s obzirom na djeljivost. Posebno, presjek polja $\mathbf F_{p^n}$ i $\mathbf F_{p^m}$ je $\mathbf F_{p^n}\cap\mathbf F_{p^m}=\mathbf F_{p^{\gcd(n,m)}}$, a najmanje polje koje sadrži i $\mathbf F_{p^n}$ i $\mathbf F_{p^m}$ je $\mathbf F_{p^n}\mathbf F_{p^m}=\mathbf F_{p^{\operatorname{lcm}(n,m)}}$.

??? note "Dokaz"
    Ključno je dokazati prvi dio, tj. da je $\bigcup_{n=1}^\infty\mathbf F_{p^n}$ algebarski zatvarač polja $\mathbf F_p$. Drugi je dio jednostavna posljedica prethodnog teorema o potpoljima konačnih polja.
    
    Uočimo da za svaki $\alpha\in\bigcup_{n=1}^\infty\mathbf F_{p^n}$ nužno postoji $n\in\mathbf N_+$ takav da je $\alpha\in\mathbf F_{p^n}$, pa je $\alpha$ algebarski element nad $\mathbf F_p$; stoga je $\bigcup_{n=1}^\infty\mathbf F_{p^n}$ algebarsko proširenje polja $\mathbf F_p$. Svaki polinom $f(x)$ stupnja $m$ nad $\mathbf F_p$ ima u algebarskom zatvaraču $F$ najviše $m$ različitih korijena $\{\alpha_i\}_{i=1}^m$. Neka je stupanj minimalnog polinoma korijena $\alpha_i$ jednak $n_i$; tada je $\alpha_i$ nužno sadržan u polju $\mathbf F_{p^{n_i}}$. Stoga su svi korijeni od $f(x)$ u $\bigcup_{n=1}^\infty\mathbf F_{p^n}$, tj. $f(x)$ se razlaže nad $\bigcup_{n=1}^\infty\mathbf F_{p^n}$. Prema definiciji algebarskog zatvarača, $\bigcup_{n=1}^\infty\mathbf F_{p^n}$ upravo je algebarski zatvarač polja $\mathbf F_p$.

### Grupa automorfizama

Sva potpolja konačnog polja $\mathbf F_q$ skupovi su korijena polinoma oblika $x^r-x$. Drugim riječima, sva su ona skupovi fiksnih točaka nekog preslikavanja $x\mapsto x^r$. To zapravo otkriva duboku vezu između potpolja konačnog polja i podgrupa njegove grupe automorfizama.

Svako polje karakteristike $p$ ima Frobeniusov endomorfizam $\sigma_p:x\mapsto x^p$. U slučaju konačnog polja $\mathbf F_q$ to je ujedno automorfizam; to pokazuje da su sva konačna polja $\mathbf F_q$ perfektna polja. Grupa automorfizama polja $\mathbf F_q$ ciklička je grupa $\langle \sigma_p\rangle$ reda $n$, a jedan je njezin generator Frobeniusov endomorfizam $\sigma_p$.

???+ note "Teorem"
    Grupa automorfizama $\operatorname{Aut}(\mathbf F_q)=\langle\sigma_p\rangle$ konačnog polja $\mathbf F_q$ ciklička je grupa reda $n$, a generator $\sigma_p$ Frobeniusov je endomorfizam $x\mapsto x^p$.

??? note "Dokaz"
    Najprije, Frobeniusov endomorfizam $\sigma_p$ automorfizam je konačnog polja $\mathbf F_q$, jer je injekcija na konačnom skupu nužno i surjekcija. Stoga je $\sigma_p\in\operatorname{Aut}(\mathbf F_q)$.
    
    Zatim, red od $\sigma_p$ jednak je $n$. Naime, za sve $x\in\mathbf F_q$ vrijedi $\sigma_p^n(x)=x^{p^n}=x$, pa je $\sigma_p^n$ identiteta; a za svaki $k<n$ preslikavanje $\sigma_p^k$ nije identiteta, jer bi inače svi elementi polja $\mathbf F_q$ morali biti korijeni polinoma $x^{p^k}-x$, što je nemoguće.
    
    Naposljetku, $\operatorname{Aut}(\mathbf F_q)$ ima najviše $n$ elemenata. Neka je $\alpha$ primitivni element polja $\mathbf F_q$; tada je automorfizam $\sigma\in \operatorname{Aut}(\mathbf F_q)$ jednoznačno određen svojom vrijednošću $\sigma(\alpha)$ u $\alpha$. No $\sigma$ mora preslikati $\alpha$ u njemu konjugirani element; inače $\alpha$ i $\sigma(\alpha)$ više ne bi bili korijeni istog minimalnog polinoma. Takvih konjugiranih elemenata ima samo $n$, što pokazuje da i $\operatorname{Aut}(\mathbf F_q)$ ima najviše $n$ elemenata.
    
    Prema tome, $n$ elemenata grupe $\operatorname{Aut}(\mathbf F_q)$ upravo su elementi od $\langle\sigma_p\rangle$. Teorem je dokazan.

Podgrupe grupe automorfizama $\operatorname{Aut}(\mathbf F_q)$ u bijektivnoj su korespondenciji s potpoljima konačnog polja $\mathbf F_q$.

???+ note "Teorem"
    Neka je $\mathbf F_q$ konačno polje, $\mathcal F$ skup svih njegovih potpolja, a $\mathcal G$ skup svih podgrupa njegove grupe automorfizama $\operatorname{Aut}(\mathbf F_q)$. Tada vrijedi:
    
    1.  Za $F\in\mathcal F$, neka je $\operatorname{Aut}(\mathbf F_q/F)$ skup automorfizama iz $\operatorname{Aut}(\mathbf F_q)$ koji fiksiraju $F$, tj. $\operatorname{Aut}(\mathbf F_q/F)=\{\sigma\in\operatorname{Aut}(\mathbf F_q):\forall x\in F(\sigma(x)=x)\}$; tada je $\operatorname{Aut}(\mathbf F_q/F)\le\operatorname{Aut}(\mathbf F_q)$;
    2.  Za $G\in\mathcal G$, neka je $F^G$ presjek skupova fiksnih točaka svih automorfizama iz $G$, tj. $F^G=\{x\in\mathbf F_q:\forall\sigma\in G(\sigma(x)=x)\}$; tada je $F^G$ potpolje polja $\mathbf F_q$;
    3.  Preslikavanja $F\rightarrow\operatorname{Aut}(\mathbf F_q/F)$ i $G\rightarrow F^G$ međusobno su inverzna i bijekcija su između $\mathcal F$ i $\mathcal G$;
    4.  Ta bijekcija odnos proširenja među potpoljima preslikava u odnos sadržavanja među podgrupama, tj. za sve $F_1\subseteq F_2$ vrijedi $\operatorname{Aut}(\mathbf F_q/F_2)\le\operatorname{Aut}(\mathbf F_q/F_1)$.

Ova je tvrdnja poseban slučaj osnovnog teorema opće Galoisove teorije; ona povezuje proširenja polja sa sadržajem teorije grupa, pa se problemi o proširenjima polja mogu rješavati metodama teorije grupa.

### Nesvodivi polinomi

Nesvodive polinome nad konačnim poljem $\mathbf F_q$ vrlo je lako odrediti. Budući da svaki nesvodiv polinom stupnja $n$ nad konačnim poljem $\mathbf F_q$ odgovara algebarskom proširenju stupnja $n$, a takvo je proširenje jedinstveno, korijeni svih nesvodivih polinoma stupnja $n$ mogu se naći u $\mathbf F_{q^n}$. To pokazuje da je nesvodiv polinom stupnja $n$ nad $\mathbf F_q$ nužno faktor od $x^{q^n}-x$. Da bi se odredili svi nesvodivi polinomi stupnja $n$ nad konačnim poljem $\mathbf F_q$, treba promotriti faktorizaciju od $x^{q^n}-x$ nad $\mathbf F_q$. To je vrlo slično slučaju ciklotomskih polinoma.

Algebarski elementi nad konačnim poljem $\mathbf F_q$ mogu se razvrstati prema stupnju svog minimalnog polinoma. Neka je $P_n$ skup algebarskih elemenata čiji je minimalni polinom stupnja točno $n$; tada je

$$
\mathbf F_{q^n} = \bigcup_{d\mid n}P_d.
$$

To odgovara faktorizaciji

$$
x^{q^n}-x = \prod_{d|n}\prod_{\zeta\in P_d}(x-\zeta).
$$

Budući da nesvodiv polinom stupnja $n$ ima $n$ korijena, a minimalni polinomi tih korijena svi su stupnja $n$, nesvodiv polinom stupnja $n$ nužno je faktor polinoma

$$
\prod_{\zeta\in P_n}(x-\zeta) = \prod_{d\mid n}\left(x^{q^d}-x\right)^{\mu(n/d)}
$$

Taj je izraz dobiven primjenom [Möbiusove inverzije](../number-theory/mobius.md) na prethodnu faktorizaciju. Budući da je stupanj tog polinoma

$$
\sum_{d\mid n}\mu(d)q^{n/d},
$$

nesvodivih normiranih polinoma stupnja $n$ nad $\mathbf F_q$ ima ukupno

$$
\frac1n\sum_{d\mid n}\mu(d)q^{n/d}
$$

To je upravo broj aperiodičnih ogrlica duljine $n$ koje se mogu složiti od kuglica $q$ boja, ne razlikujući ogrlice do na rotaciju ([dokaz](../combinatorics/polya.md#ciklička-grupa)), pa se taj polinom naziva i polinom ogrlica (necklace polynomial).

???+ note "Teorem"
    Nad konačnim poljem $\mathbf F_q$ postoje nesvodivi polinomi svakog stupnja.

Budući da nesvodivi polinomi nad konačnim poljem imaju jednostavnu strukturu, faktorizacija polinoma nad konačnim poljem vrlo je laka. Primjerice, da bi se odredili svi nesvodivi faktori stupnja $n$ zadanog polinoma, dovoljno je izračunati najveći zajednički djelitelj zadanog polinoma i $x^{q^n}-x$[^ddf]. Slično, ako je polinom stupnja $n$ relativno prost s polinomom $x^{q^k}-x$ za sve $k<n$, može se zaključiti da je taj polinom stupnja $n$ nesvodiv nad $\mathbf F_q$.

Ranije je istaknuto da korijen nesvodivog polinoma nad konačnim poljem ne mora biti primitivni element odgovarajućeg polja proširenja kao konačnog polja. Minimalni polinom primitivnog elementa konačnog polja $\mathbf F_q$ nad njegovim prostim potpoljem $\mathbf F_p$ naziva se i **primitivni polinom**[^prim-poly] (primitive polynomial) nad poljem $\mathbf F_p$. Implementira li se polje proširenja pomoću takvog polinoma, zajamčeno je da je $\overline x$ nužno primitivni element polja proširenja. Primitivni polinomi stupnja $n$ nad poljem $\mathbf F_p$ mogu se dobiti faktorizacijom ciklotomskog polinoma $\Phi_{p^n-1}(x)$ nad $\mathbf F_p$.

???+ note "Teorem"
    Neka je $p$ prost broj, $n$ prirodan broj i $p\perp n$. Neka je nadalje $d$ red elementa $p$ u multiplikativnoj grupi $(\mathbf Z/n\mathbf Z)^\times$. Tada se ciklotomski polinom $\Phi_n(x)$ nad poljem $\mathbf F_p$ rastavlja na umnožak $\dfrac{\varphi(n)}{d}$ nesvodivih polinoma stupnja $d$ nad $\mathbf F_p$; štoviše, ti su faktori primitivni polinomi ako i samo ako je $n=p^d-1$. Posebno, ciklotomski polinom $\Phi_n(x)$ nesvodiv je nad poljem $\mathbf F_p$ ako i samo ako je $p$ primitivni korijen modulo $n$.

??? note "Dokaz"
    Uočimo li da su korijeni $n$-tog ciklotomskog polinoma svi primitivni $n$-ti korijeni jedinice nad $\mathbf F_p$, a stupanj $d$ minimalnog polinoma primitivnog $n$-tog korijena jedinice jednak je broju njegovih konjugata (uključujući njega samog), što je pak jednako duljini njegove orbite pod grupom automorfizama $\langle\sigma_p\rangle$, vidimo da je $d$ duljina orbite cikličke podgrupe generirane preslikavanjem $\zeta^i\mapsto\zeta^{ip}$ na skupu $\{\zeta^i:i\perp n\}$, tj. red elementa $p$ u multiplikativnoj grupi $(\mathbf Z/n\mathbf Z)^\times$. Ako se ne želi oslanjati na Galoisovu teoriju, to se može dokazati i tako da se pokaže da je $d$ najmanji prirodan broj za koji vrijedi $(x^n-1)\mid(x^{p^d-1}-1)$. Ostale su tvrdnje očite.

Iako su nesvodivi polinomi važni za implementaciju konačnih polja, ne postoji dobra deterministička metoda za pronalaženje nesvodivog polinoma stupnja $n$ nad konačnim poljem $\mathbf F_q$. U općem se slučaju takav nesvodiv polinom može generirati randomiziranom metodom. Budući da među svim normiranim polinomima stupnja $n$ nesvodivi čine udio $\Theta(1/n)$, može se nasumce generirati normiran polinom stupnja $n$ i zatim provjeriti je li svodiv. Na taj se način nesvodiv polinom pronalazi nakon generiranja očekivano $\Theta(n)$ normiranih polinoma. Naravno, tako generiran nesvodiv polinom ne mora biti primitivan, a ni koeficijenti mu ne moraju biti jednostavni. U praksi, ako je veličina konačnog polja unaprijed zadana, često se pretraživanjem tablice[^list-prim-poly] može naći primitivni polinom s jednostavnim koeficijentima, što olakšava daljnje računanje.

### Referentna implementacija

U ovom odjeljku dana je naivna implementacija konačnog polja, samo kao referenca. U kodu je implementirana randomizirana metoda generiranja nesvodivog polinoma.

??? example "Referentna implementacija"
    ```cpp
    --8<-- "docs/math/code/finite-field/finite-field_1.cpp"
    ```

U kriptografiji se najviše upotrebljavaju konačna polja karakteristike $2$. Za takva se konačna polja elementi polja mogu pohraniti kao nizovi nula i jedinica, a operacije u polju implementirati bitovnim operacijama.

## Primjene

U ovom odjeljku navodimo neke primjene proširenja polja u algoritamskim natjecanjima. Najvažniji je slučaj onaj u kojem je pri računanju aritmetičkog izraza nad poljem u međukoracima potrebno uvesti elemente koji u izvornom polju ne postoje, čime izravno računanje postaje moguće. Čitatelji su zacijelo upoznati s rješavanjem problema o realnim brojevima pomoću kompleksnih brojeva, što je primjer proširenja polja realnih brojeva; manje su im poznata, vjerojatno, proširenja konačnih polja. Zato se ovdje uglavnom razmatraju proširenja konačnih polja, osobito proširenja prostog polja $\mathbf F_p$.

U nekim slučajevima proširenje polja smanjuje složenost računanja, pa je nužno, primjerice [brza Fourierova transformacija](../poly/fft.md) nad poljem realnih brojeva; u drugim je slučajevima proširenje polja samo jedna od mnogih metoda rješavanja problema, a obično postoje metode slične složenosti koje proširenje polja izbjegavaju, primjerice računanje Fibonaccijeva niza o kojem će odmah biti riječi. Pri upoznavanju ovih primjena čitatelji bi trebali usporediti prednosti i nedostatke različitih metoda, kako bi pri rješavanju problema mogli odabrati prikladnu metodu.

### Fibonaccijev niz

Za računanje [Fibonaccijeva niza](../combinatorics/fibonacci.md) uobičajene su metode linearna rekurzija u $O(n)$ i brzo potenciranje matrica u $O(\log n)$. Zapravo se on može izračunati i metodom proširenja polja, također u vremenskoj složenosti $O(\log n)$. Fibonaccijev niz ima formulu za opći član:

$$
f(n) = \frac{1}{\sqrt{5}}\left(\left(\frac{1+\sqrt{5}}{2}\right)^n-\left(\frac{1-\sqrt{5}}{2}\right)^n\right).
$$

Želimo izračunati vrijednost $f(n)$ modulo prost broj $p\neq 5$[^fib-p5]. Da bi se taj problem sveo na računanje u konačnom polju $\mathbf F_p$, najprije treba razjasniti značenje $\sqrt 5$ u $\mathbf F_p$. S algebarskog gledišta, to je kvadratni korijen elementa $5$. Stoga, ako u $\mathbf F_p$ postoji kvadratni korijen od $5$, tj. ako je $5$ kvadratni ostatak modulo $p$, može se izravno izračunati taj kvadratni korijen i uvrstiti ga u račun; u suprotnom treba računati u polju proširenja $\mathbf F_p(\sqrt 5)\cong\mathbf F_p[x]/(x^2-5)$.

Naravno, pri računanju u polju proširenja nije nužno dodati baš $\sqrt 5$. Primjerice, za Fibonaccijev niz može se uzeti da je $\phi$ korijen polinoma $x^2-x-1$, pa se $f(n)$ može zapisati kao

$$
f(n)=\frac{\phi^n-(-\phi)^{-n}}{2\phi-1}=\frac{\phi^n-(1-\phi)^n}{2\phi-1}.
$$

Ako $5$ nije kvadratni ostatak modulo $p$, polinom $x^2-x-1$ nesvodiv je. Tada se može računati u polju proširenja $\mathbf F_p(\phi)\cong\mathbf F_p[x]/(x^2-x-1)$ i dobiti isti rezultat kao gore.

Metoda računanja Fibonaccijeva niza može se, naravno, poopćiti i na druge slučajeve. No treba paziti na jedno: nesvodivost polinoma nad konačnim poljem ne podudara se s onom nad poljem racionalnih brojeva. Primjerice, $x^4-10x^2+1$ nesvodiv je nad $\mathbf Q$, a odgovarajuće polje razlaganja je $\mathbf Q(\sqrt 2+\sqrt 3)=\mathbf Q(\sqrt 2,\sqrt 3)$; no u $\mathbf F_p$, ako ni $2$ ni $3$ nisu kvadratni ostatci modulo $p$, on je umnožak dvaju nesvodivih polinoma, tj. već u polju proširenja $\mathbf F_p(\sqrt 2)$ postoji kvadratni korijen $\sqrt{3}$ i daljnje proširenje nije potrebno.

### Poopćenje na „proširenja” prstena

Kao što je pokazano u prethodnom odjeljku, proširenja polja imaju razna ograničenja. Za računanje Fibonaccijeva niza samo metodom proširenja polja može se riješiti jedino slučaj kad je modul $p$ prost broj i $5$ nije kvadratni ostatak modulo $p$. No treba uočiti da izlaganje u odjeljku [Algebarska proširenja](#algebarska-proširenja) pokazuje da se, ako se u proširenoj strukturi ne zahtijeva dijeljenje, mogu proširivati i prsteni[^ring-extension]. U ovom odjeljku na primjeru računanja Fibonaccijeva niza modulo proizvoljan $m$ ukratko razmatramo tu metodu. I u drugim uobičajenim situacijama koje ne uključuju mnogo dijeljenja, poput računanja determinante, brze Fourierove transformacije i sl., može se po potrebi pokušati primijeniti ta metoda.

Neka je $m$ proizvoljan prirodan broj, a $f(n)$ $n$-ti član Fibonaccijeva niza. Problem je izračunati vrijednost $f(n)\bmod m$. U načelu treba računati u $\mathbf Z/m\mathbf Z$. No, kao što je pokazano u prethodnom odjeljku, za različite module svodivost polinoma $x^2-x-1$ i postojanje višestrukih korijena nisu jednaki, pa se formula za opći član Fibonaccijeva niza može znatno razlikovati. Štoviše, ako $\mathbf Z/m\mathbf Z$ sam nije polje, elementi nakon proširenja često nemaju valjan inverz (primjerice, modulo $5$ nazivnik $\sqrt 5$ jednostavno je nula). Unatoč tim brojnim problemima, zapravo je dovoljno, uz koeficijente reducirane modulo $m$, izračunati konstantni član ostatka

$$
(1-x)^n-x^n\mod{x^2-x-1}
$$

Usporedbom s gornjom formulom za opći član opravdanost tog postupka očita je: to je, čini se, upravo računanje vrijednosti

$$
f(n)=\frac{(1-\phi)^n-\phi^n}{1-2\phi}
$$

u „proširenju” $(\mathbf Z/m\mathbf Z)[x]/(x^2-x-1)$, gdje je $\phi$ korijen od $x^2-x-1$.

Iako nije tako očito, taj je postupak također opravdan. Uočimo da u proširenju $\mathbf Q(\phi)\cong\mathbf Q[x]/(x^2-x-1)$ polja racionalnih brojeva vrijedi formula za opći član. To pokazuje da u $\mathbf Q[x]$ vrijedi

$$
(1-x)^n-x^n \equiv f(n)(1-2x) \pmod{x^2-x-1}
$$

To uključuje samo polinome s cjelobrojnim koeficijentima, pa vrijedi i u $\mathbf Z[x]$. Zapišemo li to kao dijeljenje s ostatkom i reduciramo koeficijente na obje strane jednakosti modulo $m$, dobivamo identitet u $(\mathbf Z/m\mathbf Z)[x]$. Taj zaključak vrijedi za svaki $m$.

Općenito, ako se neki izraz može izračunati u polju proširenja polja racionalnih brojeva $\mathbf Q$, onda se uklanjanjem nazivnika sigurno može dobiti tvrdnja u $\mathbf Z[x]$, a redukcijom modulo $m$ tvrdnja u $(\mathbf Z/m\mathbf Z)[x]$. Ključ uspjeha tog pristupa jest da korak uklanjanja nazivnika ne smije imati „nepopravljive” posljedice. Primjerice, pri računanju Fibonaccijeva niza, ako se umjesto konstantnog člana upotrijebi koeficijent uz linearni član, onda, budući da taj koeficijent ima faktor $2$, broj $2$ nema inverz kad je modul $m$ paran i vrijednost $f(n)$ ne može se rekonstruirati; isto tako, pri računanju Fibonaccijeva niza, upotrijebi li se formula za opći član s članom $(-\phi)^{-n}$, korak uklanjanja nazivnika uvodi teško obradive faktore, pa se iz rezultata nakon redukcije ne može izvesti zaključak. Stoga je izbor postupka računanja ključan za primjenjivost ove tehnike.

### Cipolla algoritam

Ovo je tipičan primjer računanja u proširenju konačnog polja. Za kvadratni ostatak $a$ modulo $p\neq 2$ treba naći njegov kvadratni korijen, tj. $x$ za koji vrijedi $x^2\equiv a\pmod p$. Iako je to problem nad $\mathbf F_p$, [Cipolla algoritam](../number-theory/quad-residue.md#cipolla-algoritam) računa u konačnom polju $\mathbf F_{p^2}$. U ovom odjeljku taj algoritam objašnjavamo jezikom teorije polja. Dokaz iz elementarne teorije brojeva može se pogledati na navedenoj poveznici.

Konkretno, Cipolla algoritam najprije odabire $r$ takav da je $r^2-a$ kvadratni neostatak modulo $p$, što znači da je $x^2-(r^2-a)$ nesvodiv polinom. Stoga se, uz $u=r^2-a$, može promatrati polje proširenja $\mathbf F_p(\sqrt u)$. Budući da Frobeniusov endomorfizam element može preslikati samo u njemu konjugirani element, a takav je konjugat u kvadratnom proširenju jedinstven, vrijedi $(r-\sqrt u)^p=r+\sqrt u$. Stoga je $(r-\sqrt u)^{p+1}=(r+\sqrt u)(r-\sqrt u)=r^2-u=a$. Dakle, za određivanje kvadratnog korijena dovoljno je izračunati $(r-\sqrt u)^{(p+1)/2}$. Ta se vrijednost nužno nalazi u $\mathbf F_p$, jer je polje razlaganja od $x^2-a$ sam $\mathbf F_p$.

## Zadaci za vježbu

Naposljetku navodimo nekoliko zadataka u kojima se sadržaj ovog članka izravno primjenjuje, radi boljeg razumijevanja. No treba imati na umu da mnogo toga nije uobičajena tema algoritamskih natjecanja.

-   Ciklotomski polinomi:
    -   [Luogu P1520 因式分解 (Faktorizacija)](https://www.luogu.com.cn/problem/P1520)
    -   [Gym102114C Call It What You Want](https://codeforces.com/gym/102114/problem/C)
-   Konačna polja:
    -   [Luogu P3923 大学数学题 (Zadatak iz sveučilišne matematike)](https://www.luogu.com.cn/problem/P3923)
    -   [\[COTS 2021\] 菜 Jelo](https://www.luogu.com.cn/problem/P11192)
    -   [CF1310F. Bad Cryptography](https://codeforces.com/problemset/problem/1310/F)
    -   [LOJ 178. 多项式求根 (Korijeni polinoma)](https://loj.ac/p/178)
-   Proširenja polja:
    -   [\[Oleksandr Kulkov Contest 2\] Problem A. Square Root Partitioning](https://codeforces.com/gym/102354/problem/A)
    -   [CF1103E. Radix Sum](https://codeforces.com/problemset/problem/1103/E)

## Literatura i bilješke

-   Dummit, D.S. and Foote, R.M. (2004) Abstract Algebra. 3rd Edition, John Wiley & Sons, Inc.
-   [Milne, J.S. Fields and Galois Theory.](https://www.jmilne.org/math/CourseNotes/FT.pdf)
-   [Factorization of polynomials - Wikipedia](https://en.wikipedia.org/wiki/Factorization_of_polynomials)
-   [Factorization of polynomials over finite fields - Wikipedia](https://en.wikipedia.org/wiki/Factorization_of_polynomials_over_finite_fields)
-   [Cyclotomic Polynomial - Wikipedia](https://en.wikipedia.org/wiki/Cyclotomic_polynomial)
-   [Brett Porter's Notes on Cyclotomic Polynomials](https://www.whitman.edu/documents/academics/majors/mathematics/2015/Final%20Project%20-%20Porter%2C%20Brett.pdf)
-   [Jordan Bell's Notes on Cyclotomic Polynomials](https://jordanbell.info/LaTeX/mathematics/cyclotomic/cyclotomic.pdf)
-   [Michel Waldschmidt. An introduction to the theory of finite fields](https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/FiniteFields.pdf)
-   [Finite Field Arithmetic - Wikipedia](https://en.wikipedia.org/wiki/Finite_field_arithmetic)

[^subfield-one]: Naime, jedinica $1_E$ polja $E$ nužno zadovoljava relaciju $x^2-x=0$ nad $F$, a ta u polju $F$ ima samo dva korijena, $0_F$ i $1_F$; budući da definicija polja zahtijeva $1_E\neq 0_E$, nužno je $1_E=1_F$ i $0_E=0_F$.

[^initial-object-ring]: Jezikom teorije kategorija, $\mathbf Z$ je [inicijalni objekt](https://en.wikipedia.org/wiki/Initial_and_terminal_objects) kategorije prstena s jedinicom.

[^polynomial-universal]: Strogo govoreći, ovdje je riječ o [univerzalnom svojstvu](https://en.wikipedia.org/wiki/Polynomial_ring#Polynomial_evaluation) (universal property) prstena polinoma $R[x]$.

[^multi-poly-ring]: Ovaj prsten polinoma ima beskonačno mnogo neodređenica. Da bi se takav prsten polinoma definirao, najprije treba definirati monome. Neka je $X$ skup neodređenica; monomi nad njim sve su funkcije $\alpha:X\rightarrow\mathbf N$ koje poprimaju vrijednost različitu od nule samo u konačno mnogo neodređenica, a mogu se zapisati kao $x_{i_1}^{\alpha(i_1)}\cdots x_{i_k}^{\alpha(i_k)}$, gdje su $i_1,\cdots,i_k$ indeksi svih neodređenica u kojima $\alpha$ poprima vrijednost različitu od nule. Polinomi su sve linearne kombinacije konačno mnogo monoma. S odgovarajuće definiranim zbrajanjem i množenjem oni čine prsten. Za slučaj konačno mnogo neodređenica može se dokazati da se ta definicija podudara s rezultatom rekurzivne definicije iz odjeljka [prsten polinoma u više varijabli](./ring-theory.md#多元多项式环).

[^fundamental-algebra]: Iako se zove osnovni teorem algebre, ta tvrdnja nije čisto algebarska, jer se polje realnih brojeva konstruira pomoću topološke strukture.

[^ddf]: Ta formulacija nije sasvim stroga, jer se dobivaju i nesvodivi faktori stupnja $d\mid n$. No budući da se pri implementaciji algoritma obično faktori odvajaju počevši od manjih stupnjeva, pri odvajanju nesvodivih faktora stupnja $n$ manji su faktori već odvojeni, pa je i ta formulacija prihvatljiva.

[^prim-poly]: Ovaj naziv ne treba miješati s primitivnim polinomom iz teorije polinoma (tj. polinomom čiji je najveći zajednički djelitelj svih koeficijenata jednak jedan).

[^list-prim-poly]: Primjerice, takav popis daje dodatak rada [Hansen, T., & Mullen, G. L. (1992). Primitive polynomials over finite fields. Mathematics of computation, 59(200), 639-643](https://www.ams.org/journals/mcom/1992-59-200/S0025-5718-1992-1134730-7/S0025-5718-1992-1134730-7.pdf).

[^fib-p5]: Kad je $p=5$, karakteristična jednadžba $x^2-x-1=0$ Fibonaccijeva niza ima dvostruki korijen $x=3$, pa u $\mathbf F_5$ formula za opći član Fibonaccijeva niza glasi $f(n)=n3^{n-1}$.

[^ring-extension]: Takozvano proširenje prstena obično ima dva značenja: jedno je [poopćenje proširenja grupe](https://en.wikipedia.org/wiki/Algebra_extension), a drugo [poopćenje proširenja polja](https://en.wikipedia.org/wiki/Subring#Ring_extensions). U ovom se članku misli na drugo značenje. Konkretnije, sva proširenja u ovom odjeljku [cijela su proširenja](https://en.wikipedia.org/wiki/Integral_element#Integral_extensions) komutativnih prstena s jedinicom, što je poopćenje pojma algebarskog proširenja polja na komutativne prstene s jedinicom.
