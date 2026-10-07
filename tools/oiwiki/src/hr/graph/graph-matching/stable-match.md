---
title: Stabilno sparivanje
---

## Uvod

**Problem stabilnog sparivanja** (stable matching problem) klasičan je problem kombinatorne optimizacije i kooperativne teorije igara. U odnosu na tradicionalne probleme sparivanja u teoriji grafova, stabilno sparivanje uvodi preferencije pojedinaca i uvjet stabilnosti, pa se dizajn algoritma više oslanja na redoslijed preferencija nego na samu strukturu grafa. U modelu problema stabilnog sparivanja svaki pojedinac ima preferencije prema potencijalnim partnerima, a cilj je među njima uspostaviti stabilno sparivanje. U stabilnom sparivanju ne postoji skupina pojedinaca koja bi se, zato što može dobiti bolji izbor, urotila i odstupila od trenutnog rezultata sparivanja. Stabilno sparivanje i srodni problemi široko se primjenjuju na tržištu rada, pri upisu u škole, raspodjeli medicinskih resursa i sl.

U natjecateljskom programiranju najčešće se pojavljuje stabilno sparivanje jedan-na-jedan na dvostranom tržištu, tj. problem stabilnog braka. Ovaj se članak usredotočuje na problem stabilnog braka i algoritme za njega.

## Problem stabilnog braka

Problem stabilnog braka najranije je proučavani problem stabilnog sparivanja. Slično sparivanju u bipartitnom grafu, može se opisati kao problem sparivanja na bračnom tržištu: pretpostavimo da imamo određen broj muškaraca i žena, svaka osoba ima redoslijed preferencija prema suprotnom spolu, a cilj je naći sparivanje u kojem nijedan par muškarca i žene ne bi radije napustio svoje partnere i odabrao jedno drugo.

### Opis problema

Tržište sparivanja čini skup muškaraca $M$ i skup žena $W$. Svaka osoba ima strogi redoslijed preferencija prema suprotnom spolu:

-   za svakog muškarca $m\in M$ postoji strogi potpuni uređaj $\preceq_m$ na skupu $W\cup\{m\}$;
-   za svaku ženu $w\in W$ postoji strogi potpuni uređaj $\preceq_w$ na skupu $M\cup\{w\}$.

Osim što međusobno uspoređuje osobe suprotnog spola, svaka osoba u taj redoslijed preferencija uključuje i sebe. To znači da osoba prihvaća samo one osobe suprotnog spola koje preferira više od samaštva; takve osobe zovemo **prihvatljivima** (acceptable). Očito je redoslijed preferencija među neprihvatljivim osobama nebitan; u načelu je dovoljno zadati redoslijed preferencija samo među prihvatljivim osobama. Zato se preferencije u kojima postoje neprihvatljive osobe zovu i preferencijama s nepotpunim listama (preferences with incomplete lists).

???+ example "Primjer"
    Neka je $m$ muškarac, $w_1,w_2,w_3$ tri žene i neka vrijedi $w_1\prec_m m \prec_m w_2\prec_m w_3$. Tada muškarac $m$ radije ostaje sam nego da bude spojen s $w_1$; radije je spojen s $w_2$ nego da ostane sam; radije je spojen s $w_3$ nego s $w_2$. Za muškarca $m$ žena $w_1$ je neprihvatljiva, a žene $w_2,w_3$ su prihvatljive.

**Sparivanje** $\mu:M\cup W\rightarrow M\cup W$ na tržištu mora zadovoljavati sljedeća svojstva:

-   Svaka osoba može biti sparena samo s osobom suprotnog spola ili sa sobom, tj. za sve $m\in M$ vrijedi $\mu(m)\in W\cup\{m\}$ i za sve $w\in W$ vrijedi $\mu(w)\in M\cup\{w\}$.
-   Sparivanje je uzajamno, tj. za sve $i\in M\cup W$ vrijedi $i = \mu(\mu(i))$.

U sparivanju $\mu$ mogu postojati dva izvora nestabilnosti:

-   Ako postoji pojedinac $i\in M\cup W$ takav da je $\mu(i)\prec_i i$, tj. pojedinac $i$ radije bi ostao sam nego sa svojim trenutnim partnerom, kažemo da je $i$ **blokirajući pojedinac** (blocking individual) sparivanja $\mu$.
-   Ako postoji par $m\in M$ i $w\in W$ takav da je $\mu(m)\prec_m w$ i $\mu(w)\prec_w m$, tj. muškarac $m$ i žena $w$ radije bi bili jedno s drugim nego sa svojim trenutnim partnerima, kažemo da je $(m,w)$ **blokirajući par** (blocking pair) sparivanja $\mu$.

Ako sparivanje $\mu$ nema ni blokirajućih pojedinaca ni blokirajućih parova, kažemo da je sparivanje $\mu$ **stabilno** (stable). U stabilnom sparivanju nitko ne može narušiti trenutno stanje: samci ne mogu naći nikoga tko bi htio biti s njima; oni u braku niti žele razvod niti mogu naći nekoga tko bi s njima pobjegao.

Problem stabilnog sparivanja pita: postoji li za svaki zadani skup redoslijeda preferencija stabilno sparivanje? Ako da, kako ga naći?

### Gale–Shapleyjev algoritam

Gale i Shapley predložili su 1962. **algoritam odgođenog prihvaćanja** (deferred acceptance algorithm), koji za svaki zadani skup redoslijeda preferencija nalazi stabilno sparivanje. Stoga stabilno sparivanje uvijek postoji.

Gale–Shapleyjev algoritam ima dvije simetrične inačice: u jednoj prose muškarci, u drugoj žene. Uzmimo za primjer Gale–Shapleyjev algoritam u kojem prose muškarci; tijek je sljedeći:

1.  Na početku algoritma smatramo da svaka žena drži prosidbu same sebe, a svaki je muškarac označen kao aktivan.
2.  Aktivni muškarac prosi onu ženu koju najviše voli među prihvatljivima koje još nije prosio; ako takva žena ne postoji, ne čini ništa. Neovisno o tome je li prosio, sve muškarce označimo kao neaktivne.
3.  Žena koja je primila nove prosidbe uspoređuje ih s prosidbom koju je dotad držala, zadržava samo onu koju najviše voli (moguće i samu sebe) i odbija sve ostale. Odbijene muškarce ponovno označimo kao aktivne.
4.  Ponavljamo prethodna dva koraka dok više nema aktivnih muškaraca. Tada žene prihvaćaju prosidbe koje trenutno drže. Tako dobiveno sparivanje je stabilno sparivanje.

Budući da svaki muškarac svaku ženu prosi najviše jednom, algoritam sigurno završava u vremenu $O(|M||W|)$.

Referentna implementacija:

??? example "Ogledni zadatak [SPOJ STABLEMP - Stable Marriage Problem](https://www.spoj.com/problems/STABLEMP/) – referentna implementacija"
    ```cpp
    --8<-- "docs/graph/code/graph-matching/stable-match/stable-match.cpp"
    ```

### Svojstva stabilnog sparivanja

Stabilno sparivanje ima lijepa teorijska svojstva. Prije svega, Gale–Shapleyjev algoritam konstruktivno dokazuje da stabilno sparivanje uvijek postoji.

???+ note "Teorem 1 (Gale and Shapley, 1962)"
    Gale–Shapleyjev algoritam daje stabilno sparivanje. Stoga stabilno sparivanje postoji.

??? note "Dokaz"
    Muškarac ne prosi ženu koja mu nije prihvatljiva, a žena odmah odbija prosidbu muškarca koji joj nije prihvatljiv. Stoga su muškarac i žena koji su na kraju spareni sigurno uzajamno prihvatljivi i blokirajući pojedinci ne mogu postojati. Da bismo dokazali da je sparivanje stabilno, dovoljno je pokazati da nema blokirajućih parova.
    
    Pretpostavimo suprotno: neka je $(m,w)$ blokirajući par. Tada je, zbog $\mu(m)\prec_m w$, muškarac $m$ sigurno već prosio $w$. No budući da je žena $w$ odbila $m$, sigurno je primila prosidbu muškarca $m'$ koji joj je draži. Ako je $m'\neq \mu(w)$, žena $w$ u odnosu na $m'$ može samo još više voljeti $\mu(w)$. Dakle, u odnosu na $m$, žena $w$ sigurno više voli svog konačnog partnera $\mu(w)$. To proturječi tome da je $(m,w)$ blokirajući par. Stoga je sparivanje stabilno.

???+ note "Korolar"
    Ako je $|M|=|W|$ i sve su osobe suprotnog spola prihvatljive, postoji stabilno perfektno sparivanje.

U Gale–Shapleyjevu algoritmu mogu prositi muškarci, a mogu i žene. U općem slučaju te dvije inačice Gale–Shapleyjeva algoritma daju različita stabilna sparivanja. Štoviše, stabilno sparivanje dobiveno Gale–Shapleyjevim algoritmom u kojem prose muškarci najpovoljnije je za muškarce među svim stabilnim sparivanjima, i obratno.

???+ note "Teorem 2 (Gale and Shapley, 1962)"
    Neka su $\mu_M$ i $\mu_W$ stabilna sparivanja dobivena Gale–Shapleyjevim algoritmom u kojem prose muškarci odnosno žene. Za svako stabilno sparivanje $\mu$ vrijedi $\mu(m)\preceq_m\mu_M(m)$ za sve $m\in M$ i $\mu(w)\preceq_w\mu_W(w)$ za sve $w\in W$.

??? note "Dokaz"
    Zbog simetrije dovoljno je dokazati da $\mu(m)\preceq_m\mu_M(m)$ vrijedi za sve $m\in M$. Promotrimo opet Gale–Shapleyjev algoritam u kojem prose muškarci i označimo s $k(m,w)$ krug algoritma u kojem žena $w$ odbija prosidbu muškarca $m$. Taj je krug dobro definiran za sve $(m,w)$ za koje je $\mu_M(m)\prec_m w$.
    
    Pretpostavimo da $\mu_M$ nije najpovoljnije za sve muškarce, tj. da postoje stabilno sparivanje $\mu$ i muškarac $m\in M$ takvi da je $\mu_M(m)\prec_m\mu(m)$. Budući da je sparivanje $\mu_M$ stabilno, vrijedi $m\preceq_m\mu_M(m)\prec_m\mu(m)$, pa je $\mu(m)$ žena i $k(m,\mu(m))$ je sigurno dobro definiran. Bez smanjenja općenitosti neka je $m$ upravo onaj među svim takvim muškarcima za kojeg je $k(m,\mu(m))$ najmanji. Neka je u tijeku algoritma žena $w=\mu(m)$, u trenutku kad je odbila muškarca $m$, držala prosidbu muškarca $m'$, tj. $m=\mu(w)\prec_w m'$. Budući da je $\mu$ stabilno sparivanje, $(m',w)$ ne može biti blokirajući par, a $\mu(m')\neq w$, pa je $w\prec_{m'}\mu(m')$. Budući da u Gale–Shapleyjevu algoritmu žena $w$ ne mora zadržati prosidbu muškarca $m'$ do kraja, vrijedi $\mu_M(m')\preceq_{m'}w\prec_{m'}\mu(m')$. Tada je $k(m',\mu(m'))$ dobro definiran. Štoviše, zbog $w\prec_{m'}\mu(m')$, žena $w$ drži prosidbu muškarca $m'$ tek nakon što je žena $\mu(m')$ odbila prosidbu muškarca $m'$, tj. $k(m',\mu(m')) < k(m,\mu(m))$. To proturječi izboru muškarca $m$. Dakle, po kontradikciji, $\mu_M$ je stabilno sparivanje najpovoljnije za sve muškarce.

Tržište sparivanja može imati eksponencijalno mnogo stabilnih sparivanja. Neka je $\mathcal S$ skup svih stabilnih sparivanja. Na tom skupu možemo definirati dva parcijalna uređaja:

-   $\mu_1\preceq_M\mu_2$ ako i samo ako $\mu_1(m)\preceq_m\mu_2(m)$ vrijedi za sve $m\in M$;
-   $\mu_1\preceq_W\mu_2$ ako i samo ako $\mu_1(w)\preceq_w\mu_2(w)$ vrijedi za sve $w\in W$.

Ta dva parcijalna uređaja znače da je rezultat sparivanja bolji za sve muškarce odnosno za sve žene. Općenito, dva stabilna sparivanja ne moraju biti usporediva. No svaka dva stabilna sparivanja induciraju dekompoziciju prikazanu na slici, tako da u trima dobivenim dijelovima vrijedi redom $\mu_1\preceq_M\mu_2$, $\mu_1=\mu_2$ i $\mu_2\preceq_M\mu_1$. Uočite da dio s $\mu_1=\mu_2$, iako nije izravno nacrtan, zapravo uključuje i slučaj sparivanja sa samim sobom (tj. nesparenosti).

![](./images/stable-match-decompose.svg)

Ta se dekompozicija oslanja na sljedeću lemu:

???+ note "Lema (Knuth, 1976)"
    Neka su $\mu_1$ i $\mu_2$ dva stabilna sparivanja. Neka su $M(\mu_i)=\{m\in M : \mu_j(m)\prec_m\mu_i(m)\}$ i $W(\mu_i)=\{w\in W:\mu_j(w)\prec_w\mu_i(w)\}$ skupovi muškaraca odnosno žena koji preferiraju rezultat sparivanja $\mu_i$, pri čemu je $i,j=1,2$ i $i\neq j$. Tada su $\mu_1$ i $\mu_2$ obje bijekcije između $M(\mu_1)$ i $W(\mu_2)$ te bijekcije između $M(\mu_2)$ i $W(\mu_1)$.

??? note "Dokaz"
    Neka je $m\in M(\mu_1)$. Budući da je $m\preceq_m \mu_2(m)\prec_m\mu_1(m)$, vrijedi $\mu_1(m)\in W$. Neka je $w=\mu_1(m)$. Budući da je $\mu_2(w)\neq m$, a $\mu_2(w)\prec_w m$ bi značilo da je $(m,w)$ blokirajući par sparivanja $\mu_2$, vrijedi $\mu_1(w)=m\prec_w\mu_2(w)$. Drugim riječima, $w\in W(\mu_2)$. To pokazuje $\mu_1(M(\mu_1))\subseteq W(\mu_2)$. Zbog simetrije dobivamo i $\mu_2(W(\mu_2))\subseteq M(\mu_1)$. Budući da su $\mu_1$ i $\mu_2$ injekcije, vrijedi $|M(\mu_1)|=|W(\mu_2)|$ i oba su preslikavanja surjekcije. To pokazuje da su $\mu_1$ i $\mu_2$ bijekcije između $M(\mu_1)$ i $W(\mu_2)$. Analogno su obje i bijekcije između $M(\mu_2)$ i $W(\mu_1)$.

Ova lema pokazuje da su parcijalno uređeni skupovi $(\mathcal S,\preceq_M)$ i $(\mathcal S,\preceq_W)$ međusobno [dualni](../../math/order-theory.md#对偶). Štoviše, pod svakim od tih uređaja skup $\mathcal S$ čini [rešetku](../../math/order-theory.md#有向集与格). Budući da je $\mathcal S$ konačan, obje rešetke sigurno imaju najveći i najmanji element. Ta dva ekstremna elementa upravo su stabilna sparivanja dobivena dvjema spomenutim inačicama Gale–Shapleyjeva algoritma.

???+ note "Teorem 3 (Conway and Knuth, 1976)"
    Parcijalno uređeni skupovi $(\mathcal S,\preceq_M)$ i $(\mathcal S,\preceq_W)$ međusobno su dualne rešetke. Štoviše, $\mu_M$ i $\mu_W$ redom su najveći i najmanji element rešetke $(\mathcal S,\preceq_M)$, odnosno najmanji i najveći element rešetke $(\mathcal S,\preceq_W)$.

??? note "Dokaz"
    Iz leme se lako pokazuje da su dva parcijalno uređena skupa dualna. Ako je $\mu_1\preceq_M\mu_2$, to znači $M(\mu_1)=\varnothing$; po lemi je $W(\mu_2)=\varnothing$, što je upravo $\mu_2\preceq_W\mu_1$. I obratno. To pokazuje da su međusobno dualni. U kombinaciji s Teoremom 2 dobivamo da su $\mu_M$ i $\mu_W$ ekstremni elementi obaju parcijalno uređenih skupova. Preostaje dokazati da su ti parcijalno uređeni skupovi rešetke. Zbog simetrije dovoljno je dokazati da je $(\mathcal S,\preceq_M)$ rešetka. Zbog simetrije operacija infimuma i supremuma dovoljno je dokazati da je supremum dvaju stabilnih sparivanja opet stabilno sparivanje. Formalno, za proizvoljne $\mu_1,\mu_2\in\mathcal S$ treba dokazati da je sparivanje $\mu=\mu_1\lor_M\mu_2$ koje za sve $m\in M$ zadovoljava $\mu(m)=\mu_1(m)\lor_m\mu_2(m)$ stabilno sparivanje, gdje je $\lor_m$ operacija supremuma u potpunom uređaju $\preceq_m$ (tj. ona od dviju koju $m$ više voli).
    
    Koristimo oznake iz leme. Za $i\in M(\mu_1)\cup W(\mu_2)$ stavimo $\mu(i)=\mu_1(i)$; inače $\mu(i)=\mu_2(i)$. Po lemi, $\mu_1$ i $\mu_2$ preslikavaju skup $M(\mu_1)\cup W(\mu_2)$ na njega samog, pa je $\mu$ dobro definirano sparivanje. Budući da su $\mu_1$ i $\mu_2$ stabilna i nemaju blokirajućih pojedinaca, nema ih ni $\mu$. Pretpostavimo da je $(m,w)$ blokirajući par sparivanja $\mu$. Ako je $m\in M(\mu_1)$, tada je $\mu_2(m)\prec_m\mu_1(m)=\mu(m)\prec_m w$. Ako je pritom $w\in W(\mu_2)$, tada je $\mu_1(w)=\mu(w)\prec_w m$, pa je $(m,w)$ blokirajući par sparivanja $\mu_1$, kontradikcija; inače je $w\in W\setminus W(\mu_2)$ i $\mu_2(w)=\mu(w)\prec_w m$, pa je $(m,w)$ blokirajući par sparivanja $\mu_2$, također kontradikcija. Slično i slučaj $m\in M\setminus M(\mu_1)$ vodi samo na kontradikciju. Po kontradikciji, takav blokirajući par ne postoji. Dakle $\mu_1\lor_M\mu_2$ je stabilno sparivanje. Tvrdnja je dokazana.

Konačno, u svim stabilnim sparivanjima skupovi nesparenih muškaraca i žena su isti.

???+ note "Teorem 4 (McVitie and Wilson, 1970)"
    Neka su $\mu_1$ i $\mu_2$ dva stabilna sparivanja. Tada $\mu_1$ i $\mu_2$ imaju isti skup fiksnih točaka.

??? note "Dokaz"
    Pretpostavimo da postoji $m\in M$ takav da je $\mu_1(m)=m$ i $\mu_2(m)\neq m$ za neke $\mu_1,\mu_2\in\mathcal S$. Tada je $m\in M(\mu_2)$. Po lemi je $m=\mu_1(m)\in W(\mu_1)$, što proturječi $m\in M$. Dakle takav $m\in M$ ne postoji. Analogno ne postoji ni takva $w\in W$. Stoga svaka dva stabilna sparivanja nužno imaju isti skup fiksnih točaka.

Osim svojstava razmotrenih u ovom odjeljku, stabilno sparivanje ima i lijepa strateška svojstva. O tome vidi literaturu na kraju članka.

## Srodni problemi

Stabilno sparivanje i slični problemi pojavljuju se i u mnogim drugim situacijama.

### Problem upisa na fakultete

Ako u problemu stabilnog braka ublažimo ograničenje sparivanja jedan-na-jedan i dopustimo sparivanje više-na-jedan, dobivamo **problem upisa na fakultete** (college admissions problem). Tada fakultet može upisati više studenata, dok god ne prelazi upisnu kvotu; no student i dalje može upisati najviše jedan fakultet. Slične situacije pojavljuju se pri zapošljavanju u tvrtkama, primanju liječnika stažista u bolnice i sl.

Za takve probleme Gale–Shapleyjev algoritam i dalje vrijedi. Primjerice, u Gale–Shapleyjevu algoritmu u kojem se studenti prijavljuju, fakultet može održavati listu kandidata (waitlist) duljine najviše jednake kvoti i svaki put kad broj prijava prijeđe kvotu odbiti prijavu najlošijeg studenta. Prethodna rasprava o svojstvima stabilnog sparivanja i dalje vrijedi za ovu situaciju. Posebno, inačica Teorema 4 glasi: u svim stabilnim sparivanjima broj studenata koje fakultet može upisati je isti. To se zove i **teorem o seoskim bolnicama** (rural hospitals theorem), jer znači da, kako god mijenjali mehanizam sparivanja, dokle god je rezultat stabilan, seoske bolnice koje ne mogu popuniti mjesta za liječnike nikada ih neće popuniti.

### Problem stabilnih sustanara

Ako u problemu stabilnog braka ublažimo uvjet da se sparuju samo osobe suprotnog spola, dobivamo **problem stabilnih sustanara** (stable roommates problem). Tada na početku imamo samo određen broj studenata koje treba spariti u parove sustanara. Za takve probleme stabilno sparivanje ne mora postojati. Irving je 1985. predložio algoritam koji ovaj problem rješava u vremenu $O(n^2)$.

### Problem tržišta stanova

U problemu stabilnog braka dvije skupine pojedinaca imaju preferencije jedna prema drugoj, pa je to problem dvostranog sparivanja. Osim toga, mogu se razmatrati i problemi jednostranog sparivanja. Čest primjer je **problem tržišta stanova** (housing market problem). Ima $n$ stanara, svaki posjeduje jedan stan. Svaka osoba ima strogu preferenciju prema svim stanovima. Stanove treba preraspodijeliti stanarima tako da nijedan stanar ne dobije stan lošiji od početnog i da ne postoji skupina stanara bilo koje veličine koja bi međusobnom razmjenom nekretnina postigla zadovoljavajući ishod. Taj se problem rješava algoritmom Top Trading Cycle u vremenu $O(n^2)$. Takvi se problemi pojavljuju i pri transplantaciji bubrega i sl.

## Zadaci

-   [UOJ 41.【清华集训 2014】矩阵变换](https://uoj.ac/problem/41)
-   [Codeforces 1147 F. Zigzag Game](https://codeforces.com/problemset/problem/1147/F)

## Literatura i napomene

-   [什么是算法：如何寻找稳定的婚姻搭配 (Što je algoritam: kako naći stabilne bračne parove) - Matrix67](https://matrix67.com/blog/archives/2976)
-   [Gale–Shapley 算法：在二分图中寻找稳定匹配 (Gale–Shapleyjev algoritam: traženje stabilnog sparivanja u bipartitnom grafu)](https://reimuyk.github.io/2021-03-24-Gale-Shapley-Algorithm/)
-   [Stable matching problem - Wikipedia](https://en.wikipedia.org/wiki/Stable_matching_problem)
-   [Lattice of stable matchings - Wikipedia](https://en.wikipedia.org/wiki/Lattice_of_stable_matchings)
-   [Stable roommates problem - Wikipedia](https://en.wikipedia.org/wiki/Stable_roommates_problem)
-   [Top trading cycle - Wikipedia](https://en.wikipedia.org/wiki/Top_trading_cycle)
-   [Stable matching: Theory, evidence, and practical design - the 2012 Nobel Prize in Economics](https://www.nobelprize.org/uploads/2018/06/popular-economicsciences2012.pdf)
-   [Notes on Matching and Market Design by Xiang Sun](https://www.xiangsun.org/wp-content/uploads/2013/02/notes-2015-matching.pdf)
-   Gale, David, and Lloyd S. Shapley. "College admissions and the stability of marriage." The American Mathematical Monthly 69, no. 1 (1962): 9-15.
-   Irving, Robert W. "An efficient algorithm for the stable roommates problem." Journal of Algorithms 6, no. 4 (1985): 577-595.
-   Knuth, Donald Ervin. "Mariages stables et leurs relations avec d'autres problèmes combinatoires." Les Presses de l'Université de Montréal (1976).
-   McVitie, David G., and Leslie B. Wilson. "Stable marriage assignment for unequal sets." BIT Numerical Mathematics 10, no. 3 (1970): 295-309.
-   Roth, Alvin E., and Marilda Sotomayor. "Two-sided matching." Handbook of game theory with economic applications 1 (1992): 485-541.
-   Roth, Alvin E. "Deferred acceptance algorithms: History, theory, practice, and open questions." International Journal of Game Theory 36, no. 3-4 (2008): 537-569.
