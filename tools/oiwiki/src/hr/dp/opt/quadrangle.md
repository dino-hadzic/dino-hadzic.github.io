---
title: Optimizacija nejednakošću četverokuta
---

Optimizacija nejednakošću četverokuta (quadrangle inequality) iskorištava monotonost odluka u jednadžbi prijelaza stanja, pa se često naziva i **optimizacija DP-a monotonošću odluka**.

## Osnove

Promotrimo najjednostavniji slučaj: trebamo riješiti sljedeći niz optimizacijskih problema:

$$
f(i) = \min_{1 \leq j \leq i} w(j,i) \qquad \left(1 \leq i \leq n\right) \tag{1}
$$

Pretpostavljamo da se funkcija cijene $w(j,i)$ može izračunati u vremenu $O(1)$.

???+ info "Dogovor"
    Jednadžba prijelaza stanja dinamičkog programiranja često se može zapisati kao niz optimizacijskih problema. Uzmimo za primjer jednadžbu (1): ti problemi imaju parametar $i$, a i funkcija cilja i dopustivo područje mogu ovisiti o $i$. Svaki je problem, za zadani parametar $i$, odabir dopustivog rješenja $j$ koje minimizira vrijednost funkcije cilja. Radi jednostavnosti izražavanja, optimizacijski problem s parametrom $i$ u nastavku kratko zovemo „problem $i$”, dopustivo rješenje $j$ tog problema „odluka $j$”, a vrijednost funkcije cilja u optimalnom rješenju „stanje $f(i)$”. Uz to, najmanju optimalnu odluku problema $i$ označavamo s $\operatorname{opt}(i)$.

U općem slučaju ukupna vremenska složenost ovih problema je $O(n^2)$, jer za problem $i$ moramo razmotriti sve moguće odluke $j$. No kad vrijedi monotonost odluka, prostor odluka može se učinkovito suziti i ukupna složenost optimizirati.

-   **Monotonost odluka**: za svaki $i_1 < i_2$ nužno vrijedi $\operatorname{opt}(i_1) \leq \operatorname{opt}(i_2)$.

??? note "Napomena"
    Za problem $i$ skup optimalnih odluka ne mora biti interval. Monotonost odluka zapravo se može definirati na skupovima optimalnih odluka. Za skupove $A$ i $B$ možemo definirati $A \leq B$ ako i samo ako za svaki $a\in A$ i $b\in B$ vrijedi $\min\{a,b\}\in A$ i $\max\{a,b\}\in B$. To povlači monotonost najmanje (najveće) optimalne odluke, što je definicija koju ovdje usvajamo. Rezultati koje ovaj tekst iskazuje za najmanju optimalnu odluku jednako vrijede i za najveću optimalnu odluku. Međutim, postoje situacije u kojima je najmanja optimalna odluka nekog većeg problema strogo manja od najveće optimalne odluke nekog manjeg problema, tj. za neke $i_1 < i_2$ može vrijediti $\mathop{\mathrm{optmax}}(i_1) > \mathop{\mathrm{optmin}}(i_2)$, pa pri pisanju koda treba paziti da se uvijek računa najmanja ili uvijek najveća optimalna odluka.
    
    S druge strane, problemi s istom najmanjom optimalnom odlukom čine interval. Taj interval, kao funkcija najmanje optimalne odluke, mora biti strogo rastuć. Drugim riječima, ako je $j_1 = \operatorname{opt}(i_1)$, $j_2 = \operatorname{opt}(i_2)$ i $j_1 < j_2$, tada nužno $i_1 < i_2$. Ekvivalentno, ako su intervali problema u kojima odluke $j_1 < j_2$ mogu biti najmanje optimalne redom $[l_{j_1},r_{j_1}]$ i $[l_{j_2},r_{j_2}]$, tada nužno $r_{j_1} < l_{j_2}$.

Najčešći način utvrđivanja monotonosti odluka jest nejednakost četverokuta (quadrangle inequality). U različitim se kontekstima to svojstvo naziva i Mongeovo svojstvo (za opis matrica $A_{j,i}$) ili submodularnost (submodularity, za opis funkcija $f([j,i])$ čiji je argument interval).

-   **Nejednakost četverokuta**: ako za sve $a\leq b\leq c\leq d$ vrijedi

    $$
    w(a,c)+w(b,d) \leq w(a,d)+w(b,c),
    $$

    kažemo da funkcija $w$ zadovoljava nejednakost četverokuta (kratko: „ukršteno je manje od ugniježđenog”). Ako uvijek vrijedi jednakost, kažemo da funkcija $w$ zadovoljava **jednakost četverokuta**.

Ako nije drugačije rečeno, u nastavku uvijek pretpostavljamo $a\leq b\leq c\leq d$. Nejednakost četverokuta daje dovoljan, ali ne i nužan uvjet za monotonost odluka.

???+ note "Teorem 1"
    Ako $w$ zadovoljava nejednakost četverokuta, tada problem (1) ima monotonost odluka.

??? note "Dokaz"
    Dokazujemo kontradikcijom. Pretpostavimo da za neke $c < d$ vrijedi $a = \operatorname{opt}(d) < \operatorname{opt}(c) = b$. Tada je $a < b \leq c < d$. Iz uvjeta optimalnosti, $w(a,d) \leq w(b,d)$ i $w(b,c) < w(a,c)$, pa je $w(a,d) - w(b,d) \leq 0 < w(a,c) - w(b,c)$, što je u suprotnosti s nejednakošću četverokuta.

Nejednakost četverokuta možemo shvatiti tako da je, na razumnoj domeni, mješovita diferencija drugog reda $\Delta_i\Delta_jw(j,i)$ funkcije $w$ nepozitivna.

Pomoću monotonosti odluka mnogi se uobičajeni algoritmi mogu optimizirati na složenost $O(n\log n)$. Ti se algoritmi razlikuju po području primjene, težini implementacije i učinkovitosti, pa prikladan algoritam treba izabrati prema konkretnoj situaciji. To uglavnom ovisi o svojstvima $w(j,i)$. Ako nije drugačije rečeno, u ovom tekstu pretpostavljamo da $w(j,i)$ dopušta **nasumični pristup**, tj. da se $w(j,i)$ može dohvatiti ili izračunati u vremenu $O(1)$. No nije u svim zadacima $w(j,i)$ tako lako izračunati. Zato, osim osnovnog slučaja, ovaj tekst razmatra i metode optimizacije DP-a monotonošću odluka kad $w(j,i)$ ima samo sljedeća svojstva:

-   **Pomični pristup**: $w(j,i)$ se u vremenu $O(1)$ može dobiti iz $w(j\pm 1,i)$ ili $w(j,i\pm 1)$. (Slično situaciji u [Moovu algoritmu](../../misc/mo-algo.md).)
-   **Dinamičko računanje**: izračun $w(j,i)$ ovisi o $\{f(j'):j' < j\}$. To znači da se $f$ i $w$ mogu računati samo redom. Problem rastavljanja intervala bez ograničenja na broj intervala, opisan u nastavku, pripada ovoj situaciji.

Ta se dva svojstva međusobno ne isključuju; moguće je da $w(j,i)$ treba računati dinamički, a dopušta samo pomični pristup.

### Podijeli pa vladaj

Za rješavanje svih stanja dovoljno je odrediti sve optimalne odluke. Da bismo odredili $\operatorname{opt}(i)$ za sve $1 \leq i \leq n$, najprije izračunamo $\operatorname{opt}(n/2)$, a zatim zasebno izračunamo $\operatorname{opt}(i)$ za $1 \leq i < n/2$ i za $n/2 < i \leq n$; pritom znamo da $\operatorname{opt}(i)$ u prvoj polovici nužno leži između $1$ i $\operatorname{opt}(n/2)$ (uključivo), a u drugoj polovici između $\operatorname{opt}(n/2)$ i $n$ (uključivo). Dva podintervala obrađujemo analogno, dok ne izračunamo optimalnu odluku svakog problema. Ako tijekom podjele bilježimo donju i gornju granicu pretraživanja, složenost algoritma ostaje $O(n\log n)$. Stablo rekurzije ima $O(\log n)$ razina, a na svakoj se razini svaka odluka izračuna najviše dvaput, pa je ukupan broj izračuna $O(n\log n)$.

???+ example "Primjer implementacije"
    ```cpp
    --8<-- "docs/dp/code/opt/quadrangle/quadrangle-divide-conquer.cpp:core"
    ```

Osim osnovnog slučaja s nasumičnim pristupom, algoritam podjele može se primijeniti i kad $w(j,i)$ dopušta samo pomični pristup. Dovoljno je tijekom izračuna održavati pokazivač $(j,i)$ i pripadnu vrijednost $w(j,i)$ te, kad zatreba nova vrijednost, pokazivač grubom silom pomaknuti na trenutni položaj i ažurirati vrijednost funkcije. Vremenska složenost i dalje je $O(n\log n)$. Detaljnija rasprava nalazi se u odjeljku [Pojednostavljeni algoritam LARSCH](#pojednostavljeni-algoritam-larsch) u nastavku. No algoritam podjele ne može riješiti slučaj kad $w(j,i)$ treba računati dinamički, jer ne može izračunati najmanju optimalnu odluku $\operatorname{opt}(n/2)$ u sredini intervala prije nego što su riješeni problemi lijeve polovice.

### Red s binarnim pretraživanjem

Uočimo da za svaku odluku $j$ problemi $i$ kojima je ona najmanja optimalna odluka nužno čine interval. Monotonim redom možemo bilježiti interval problema koje svaka dosad viđena odluka rješava; tako se optimalno rješenje problema prirodno dobiva iz odluka zabilježenih u redu.

Konkretno, algoritam redom prolazi odluke. Kad dođe do odluke $k$, red mora sadržavati **trojke** sastavljene od svake dosad moguće odluke $j$ i lijevog i desnog ruba $l_j$ i $r_j$ intervala problema koje ona rješava. Za probleme u zadanom intervalu $[l_j,r_j]$, $j$ mora biti najmanja optimalna među dosad razmotrenim odlukama (tj. među odlukama iz intervala $[1,k]$). U svakom trenutku odluke pohranjene u redu ne moraju biti uzastopne, ali još neriješeni problemi $[k,n]$ moraju biti disjunktna unija intervala problema pohranjenih u redu.

Da bismo pokazali da tijekom ažuriranja reda problemi $i$ kojima je odluka $j$ najmanja optimalna uvijek čine neprekinuti interval, trebamo malo pojačati prethodni rezultat:

???+ note "Korolar 1"
    Neka je $\operatorname{opt}_k(i)$ najmanja optimalna odluka problema $i$ kad se razmatraju samo odluke iz $[1,k]$. Ako $w$ zadovoljava nejednakost četverokuta, tada za svaki $i_1 < i_2$ nužno vrijedi $\operatorname{opt}_k(i_1) \leq \operatorname{opt}_k(i_2)$.

??? note "Dokaz"
    Neka je $M$ dovoljno velik pozitivan realan broj. Funkcija $w'(j,i) = w(j,i) + M[j > k]$ i dalje zadovoljava nejednakost četverokuta; ovdje je $[\cdot]$ Iversonova zagrada. Promotrimo pomoćni DP s funkcijom cijene $w'$. U pomoćnom DP-u ni za jedan problem $i$ odluka $j > k$ ne može biti najmanja optimalna, tj. $\operatorname{opt}'(i) = \operatorname{opt}'_k(i) = \operatorname{opt}_k(i)$. Primjenom teorema 1 na pomoćni DP dobivamo korolar.

Algoritam teče ovako:[^cmp-min-opt]

-   Na početku je red prazan. Slično monotonom redu, pri razmatranju svake sljedeće odluke $j$ obavljamo izbacivanje iz reda i ubacivanje u red.
-   **Izbacivanje**: najprije iz reda uklonimo prethodni problem $j-1$. Ako je desni rub intervala problema koje rješava odluka na početku reda upravo $j-1$, izbacimo početak reda; inače lijevi rub intervala problema te odluke postavimo na $j$.
-   **Ubacivanje**: pri ubacivanju odluke $j$ najprije je usporedimo s odlukom $j'$ na kraju reda.
    -   Ako je za problem $l_{j'}$ odluka $j$ koju ubacujemo strogo bolja od postojeće odluke $j'$, tj. $w(j,l_{j'}) < w(j',l_{j'})$, izbacujemo odluku $j'$ s kraja reda. To ponavljamo dok red ne postane prazan ili dok odluka $j'$ na kraju reda ne bude bolja od $j$ za problem $l_{j'}$.
    -   Ako je red prazan, ubacujemo $(j,j,n)$, tj. smatramo da je odluka $j$ optimalna za sve još neriješene probleme.
    -   Ako odluka $j'$ na kraju reda ni za problem $r_{j'}$ nije lošija od odluke $j$ koju ubacujemo, tada za $r_{j'} < n$ ubacujemo $(j,r_{j'}+1,n)$, što znači da je $j$ najmanja optimalna odluka za probleme $[r_{j'}+1,n]$; inače $j$ ne treba ubaciti, jer nije bolja od postojećih odluka.
    -   Preostaje slučaj da je odluka $j'$ na kraju reda strogo bolja od odluke $j$ za problem $l_{j'}$, a strogo lošija za problem $r_{j'}$. To znači da postoji problem $i\in(l_{j'},r_{j'}]$ takav da je najmanja optimalna odluka problema $[l_{j'},i-1]$ jednaka $j'$, a problema $[i,r_{j'}]$ jednaka $j$. Zato **binarnim pretraživanjem** nalazimo najmanji $i\in[l_{j'},r_{j'}]$ takav da je $w(j,i) < w(j',i)$, desni rub $r_{j'}$ intervala na kraju reda mijenjamo u $i-1$ i ubacujemo $(j,i,n)$.
-   Nakon obrade odluke $j$ obrađene su sve odluke do $j$. Tada je odluka na početku reda najmanja optimalna odluka problema $j$, pa možemo zabilježiti pripadno optimalno rješenje.

???+ example "Primjer implementacije"
    ```cpp
    --8<-- "docs/dp/code/opt/quadrangle/quadrangle-monotone-queue.cpp:core"
    ```

Slično monotonom redu, svaka odluka ulazi u red najviše jednom i izlazi najviše jednom. Izbacivanje je $O(1)$, a ubacivanje $O(\log n)$ (može trebati binarno pretraživanje), pa je ukupna vremenska složenost $O(n\log n)$.

Budući da algoritam s redom i binarnim pretraživanjem probleme i odluke razmatra redom, može se primijeniti kad $w(j,i)$ treba računati dinamički. To je njegova prednost pred algoritmom podjele. No kako korak binarnog pretraživanja ovisi o nasumičnom pristupu $w(j,i)$, ne može se primijeniti kad $w(j,i)$ dopušta samo pomični pristup.

???+ example "Primjer 1: [„POI2011” Lightning Conductor](https://loj.ac/problem/2157)"
    Zadan je niz $a_1,a_2,\cdots,a_n$ duljine $n$. Za svaki $1 \leq i \leq n$ treba pronaći najmanji nenegativan cijeli broj $f_i$ takav da vrijedi
    
    $$
    \forall j\in\left[1,n\right]:a_j \leq a_i + f_i - \sqrt{|i-j|}.
    $$

??? note "Ideja rješenja"
    Očito, preoblikovanjem nejednakosti dobivamo traženi cijeli broj $f_i = \max_{j}\{a_j+\sqrt{|i-j|}-a_i\}$. Razmotrimo najprije slučaj $j \leq i$ (drugi je slučaj analogan); tada dobivamo jednadžbu prijelaza stanja:
    
    $$
    f_i = -\min_{j\le i}\{-a_j-\sqrt{i-j}+a_i\}.
    $$
    
    Iz konveksnosti funkcije $-\sqrt{x}$ lako se vidi (detalji slijede kasnije) da funkcija $w(j,i) = -a_j-\sqrt{i-j}+a_i$ zadovoljava nejednakost četverokuta, pa primjenom gornjeg algoritma zadatak rješavamo u vremenu $O(n\log n)$.

??? note "Implementacija"
    ```cpp
    --8<-- "docs/dp/code/opt/quadrangle/quadrangle_1.cpp"
    ```

### Pojednostavljeni algoritam LARSCH

Nijedan od prethodna dva algoritma ne može obraditi slučaj kad $w(j,i)$ treba računati dinamički, a dopušta samo pomični pristup. U ovom odjeljku predstavljamo algoritam koji istodobno svladava obje poteškoće. To je pojednostavljena inačica algoritma LARSCH koji su Larmore i Schieber predložili 1991. godine[^larsch], pa se naziva **pojednostavljeni algoritam LARSCH**. Izvorna inačica algoritma rješava DP s monotonošću odluka u vremenu $O(n)$, ali je implementacija složena i ovdje je ne opisujemo.

I dalje razmatramo rješavanje podjelom. Pri rješavanju problema u intervalu $(l,r]$ pretpostavljamo da su poznati:

-   najmanje optimalne odluke $\operatorname{opt}(i)$ i optimalne vrijednosti problema $i$ iz intervala $[1,l]$, te
-   najmanja optimalna odluka $\operatorname{opt}_l(r)$ i optimalna vrijednost problema $r$ kad se razmatraju samo odluke iz intervala $[1,l]$.

Po završetku rješavanja problema u intervalu $(l,r]$ trebamo dobiti najmanje optimalne odluke i optimalne vrijednosti problema u intervalu $(l,r]$.

Neka je $\textit{mid}$ sredina intervala $(l,r]$. Postupak rješavanja je sljedeći:

1.  Prođi odluke $j\in[\operatorname{opt}(l),\operatorname{opt}_l(r)]$ i ažuriraj najmanju optimalnu odluku i optimalnu vrijednost problema $\textit{mid}$.
2.  Rekurzivno riješi probleme u intervalu $(l,\textit{mid}]$.
3.  Prođi odluke $j\in(l,\textit{mid}]$ i ažuriraj najmanju optimalnu odluku i optimalnu vrijednost problema $r$.
4.  Rekurzivno riješi probleme u intervalu $(\textit{mid},r]$.

Prije pokretanja rekurzije na cijelom intervalu $[1,n]$ najprije treba odlukom $j=1$ ažurirati probleme $i\in\{1,n\}$. Algoritam staje kad rekurzija dođe do $l=r$.

???+ example "Primjer implementacije"
    ```cpp
    --8<-- "docs/dp/code/opt/quadrangle/quadrangle-simplified-larsch.cpp:core"
    ```

Najprije pokažimo ispravnost algoritma. Dovoljno je provjeriti da su prije svakog koraka rekurzivnog rješavanja (tj. koraka 2 i 4) ispunjeni gore navedeni preduvjeti. Prema korolaru 1 iz prethodnog odjeljka vrijedi $\operatorname{opt}(l)=\operatorname{opt}_l(l)\le\operatorname{opt}_l(\textit{mid})\le\operatorname{opt}_l(r)$, pa je nakon koraka 1 poznat $\operatorname{opt}_l(\textit{mid})$, čime je prije koraka 2 ispunjen preduvjet za rekurzivno rješavanje problema u intervalu $(l,\textit{mid}]$. Budući da je $\{\operatorname{opt}(i):i\in[1,l]\}$ već bio poznat, a korak 2 daje vrijednosti $\{\operatorname{opt}(i):i\in(l,\textit{mid}]\}$, nakon toga su poznati svi $\{\operatorname{opt}(i):i\in[1,\textit{mid}]\}$; ujedno, kako je $\operatorname{opt}_l(r)$ već bio poznat, nakon koraka 3 poznat je i $\operatorname{opt}_\textit{mid}(r)$. Stoga je i prije koraka 4 ispunjen preduvjet za rekurzivno rješavanje problema u intervalu $(\textit{mid},r]$.

Zatim treba pokazati da je složenost algoritma i dalje $O(n\log n)$. Stablo rekurzije ima $O(\log n)$ razina. Za svaki čvor iste razine stabla rekurzije prolaze se odluke iz intervala $[\operatorname{opt}(l),\operatorname{opt}_l(r)]$ i $(l,\textit{mid}]$. Budući da je $\operatorname{opt}(l)\le\operatorname{opt}_l(r)\le\operatorname{opt}(r)$, na istoj se razini svaka odluka prođe samo $O(1)$ puta. Dakle, ukupan broj prolazaka na svakoj razini stabla rekurzije je $O(n)$. Ako je složenost jednog pristupa ili izračuna $w(j,i)$ jednaka $O(1)$, vremenska složenost algoritma je $O(n\log n)$.

U nekim slučajevima kad $w(j,i)$ dopušta samo pomični pristup, složenost ovog algoritma i dalje je $O(n\log n)$. Tada za korake 1 i 3 algoritma zasebno održavamo pokazivač $(j,i)$ i trenutnu vrijednost $w(j,i)$. Kad god trebamo pristupiti novoj vrijednosti, pokazivač $(j,i)$ grubom silom pomaknemo s položaja pri prethodnom pristupu na trenutni položaj i pritom prenosimo vrijednost funkcije $w(j,i)$. Lako se provjerava da je pri obilasku stabla rekurzije ukupan broj tih pomaka $O(n\log n)$. Stoga je vremenska složenost algoritma i dalje $O(n\log n)$.

??? note "Dokaz složenosti bez nasumičnog pristupa"
    Dovoljno je dokazati da je ukupan broj pomaka pokazivača $O(n\log n)$. Neka su $A$ i $B$ pokazivači koji pripadaju koracima 1 i 3. Zapravo se može osigurati sljedeće: prije rješavanja problema u intervalu $(l,r]$ pokazivač $A$ je na položaju $(\operatorname{opt}(l),l)$, a pokazivač $B$ na položaju $(l,l)$; nakon toga je pokazivač $A$ na položaju $(\operatorname{opt}(r),r)$, a pokazivač $B$ na položaju $(r,r)$.
    
    Konstruirajmo sljedeće pravilo pomicanja pokazivača. U koraku 1 pokazivač $A$ neka se kreće putem
    
    $$
    (\operatorname{opt}(l),l)\to(\operatorname{opt}(l),\textit{mid})\to(\operatorname{opt}_l(r),\textit{mid})\to(\operatorname{opt}(l),\textit{mid})\to(\operatorname{opt}(l),l)
    $$
    
    Tada su pokazivači $A$ i $B$ na propisanim položajima prije rješavanja problema u intervalu $(l,\textit{mid}]$. U koraku 2, po pravilu, pokazivač $A$ prelazi na $(\operatorname{opt}(\textit{mid}),\textit{mid})$, a pokazivač $B$ na $(\textit{mid},\textit{mid})$. U koraku 3 pokazivač $B$ neka se kreće putem
    
    $$
    (\textit{mid},\textit{mid}) \to (l,\textit{mid}) \to (l, r) \to (\textit{mid},r) \to (\textit{mid},\textit{mid})
    $$
    
    Tada su pokazivači $A$ i $B$ na propisanim položajima prije rješavanja problema u intervalu $(\textit{mid},r]$. U koraku 4, po pravilu, pokazivač $A$ prelazi na $(\operatorname{opt}(r),r)$, a pokazivač $B$ na $(r,r)$. Oba su pokazivača na propisanim položajima po završetku rješavanja problema u intervalu $(l,r]$. Dakle, ovo pravilo pomicanja zadovoljava gornji zahtjev. Štoviše, ono je dovoljno za sve izračune u koracima 1 i 3. Izravnim prebrojavanjem pomaka pokazivača po ovom pravilu vidimo da korak 1 zahtijeva
    
    $$
    2(\operatorname{opt}_l(r) - \operatorname{opt}(l)) + 2(\textit{mid} - l)
    $$
    
    pomaka, a korak 3
    
    $$
    2(\textit{mid}-l)+2(r-\textit{mid}) = 2(r-l)
    $$
    
    pomaka. Zbrojimo li te brojeve pomaka po svim čvorovima stabla rekurzije i iskoristimo svojstvo da se na istoj razini svi $[l,r]$ i svi $[\operatorname{opt}(l),\operatorname{opt}_l(r)]$ preklapaju najviše u krajnjim točkama, dobivamo da je ukupan broj pomaka $O(n\log n)$.
    
    Budući da gornje pravilo pomicanja uvodi više međutočaka nego što ih pokazivači stvarno prođu tijekom izračuna, stvarni broj pomaka pokazivača ne premašuje procjenu broja pomaka po tom pravilu. Dakle, i stvarni broj pomaka pokazivača je $O(n\log n)$.

Budući da ovaj algoritam prije rješavanja problema u intervalu $(l,r]$ već ima izračunata optimalna rješenja $f(i)$ u intervalu $[1,l]$, može se primijeniti i kad $w(j,i)$ treba računati dinamički.

## Problem rastavljanja intervala

Promotrimo problem rastavljanja intervala na nekoliko podintervala. Formalno, zadani interval $[1,n]$ rastavljamo na $[a_1,b_1],\cdots,[a_k,b_k]$, pri čemu je $a_1=1$, $b_k=n$ i $b_{i}+1=a_{i+1}$ za svaki $i < k$. Cijena zadanog rastavljanja je $\sum_{i=1}^kw(a_i,b_i)$. Problem traži minimizaciju te cijene. Možemo napisati sljedeću 1D1D jednadžbu prijelaza stanja.

$$
f(i) = \min_{1\leq j\leq i} f(j-1)+w(j,i) \qquad (1\leq i\leq n)
$$

Ovdje je $f(0)=0$. Uočimo da, čim $w(j,i)$ zadovoljava nejednakost četverokuta, i $f(j-1)+w(j,i)$ nužno zadovoljava nejednakost četverokuta, jer prvi član ne sadrži ukršteni član $j$ i $i$ te se pri mješovitoj diferenciji poništava. No kako funkcija cijene ovisi o prethodnim potproblemima, ovaj se prijelaz može računati samo redom, pa se prvi algoritam podjele opisan ranije ne može primijeniti; obično su prikladni samo algoritam reda s binarnim pretraživanjem ili pojednostavljeni algoritam LARSCH. Složenost algoritma je $O(n\log n)$.

### Slučaj s ograničenim brojem intervala

Gornji se problem može pojačati ograničenjem broja intervala, tj. problem propisuje da se interval rastavi na točno $m$ podintervala. Tada broj podintervala nakon rastavljanja treba dodati kao jednu dimenziju stanja prijelaza. Pripadna 2D1D jednadžba prijelaza stanja glasi:

$$
f(k,i) = \min_{1\leq j\leq i} f(k-1,j-1)+w(j,i) \qquad (1\leq k\leq m,\ 1\leq i\leq n) \tag{2}
$$

Ovdje je $f(0,0)=0$ te $f(0,i)=f(k,0)=\infty$ za sve $1\leq k\leq m$ i $1\leq i\leq n$. Kao i prije, $f(k-1,j-1)+w(j,i)$ nužno zadovoljava nejednakost četverokuta. Sada izračun $k$-tog sloja više ne ovisi o rezultatima tog sloja, pa se svaki sloj može izračunati bilo kojim algoritmom iz prethodnog odjeljka, uz složenost $O(mn\log n)$.

Za ovaj problem, iskorištavanjem monotonosti odluka, postoje i drugi optimizacijski algoritmi. Druga ideja optimizacije oslanja se na sljedeći rezultat. Taj je algoritam vrlo sličan Knuthovoj optimizaciji, detaljno opisanoj u nastavku.

???+ note "Teorem 2"
    Ako $w$ zadovoljava nejednakost četverokuta, tada za problem (2) vrijedi $\operatorname{opt}(k-1,i) \leq \operatorname{opt}(k,i) \leq \operatorname{opt}(k,i+1)$.

??? note "Dokaz"
    Druga nejednakost samo je monotonost odluka $k$-tog sloja. Ključna je prva nejednakost.
    
    Dokazujemo $\operatorname{opt}(k,i) \leq \operatorname{opt}(k+1,i)$. Pretpostavimo da imamo sljedeće dvije podjele intervala $[1,i]$ (indeksirane obrnutim redoslijedom): $[a_{k},d_{k}],\cdots,[a_1,d_1]$ i $[b_{k+1},c_{k+1}],\cdots,[b_1,c_1]$. Pritom je lijevi rub svakog intervala najmanja optimalna odluka problema koji pripada njegovu desnom rubu; isto tako, promatramo li sve moguće podjele zdesna nalijevo, desni je rub najmanja optimalna odluka problema koji pripada lijevom rubu. Na primjer, $d_j$ i $c_j$ su redom najmanje optimalne odluke za desni rub prvog intervala slijeva pri podjeli $[a_j,i]$ odnosno $[b_j,i]$ na $j$ dijelova. Prema monotonosti odluka, ako je $a_{j-1} > b_{j-1}$, tj. $d_j > c_j$, tada nužno $a_j > b_j$. Stoga, ako tvrdnja ne vrijedi, tada je $a_1 > b_1$. Odatle se indukcijom dokazuje $a_{k} > b_{k}$, što je očito u suprotnosti s pretpostavkom. Time je tvrdnja dokazana.
    
    Prva se nejednakost može dokazati i ovako. Opet promotrimo dvije podjele iz gornjeg dokaza. Ako tvrdnja ne vrijedi, tada je $a_1 > b_1$; no kako je $a_{k} < b_{k}$, možemo naći najmanji $j>1$ takav da je $a_j \leq b_j$. Tada je $a_{j-1} > b_{j-1}$, pa je $d_j>c_j$. Našli smo intervale za koje vrijedi $a_j \leq b_j \leq c_j < d_j$. Promotrimo rezultate rekombinacije tih dviju podjela. Podjela $[b_{k+1},c_{k+1}],\cdots,[b_{j+1},c_{j+1}],[b_j,d_j],[a_{j-1},d_{j-1}],\cdots,[a_1,d_1]$ ima $(k+1)$ dijelova, pa iz pretpostavljene optimalnosti slijedi
    
    $$
    \begin{aligned}
    &w(b_{k+1},c_{k+1})+\cdots+w(b_{j+1},c_{j+1})+w(b_j,c_j)+w(b_{j-1},c_{j-1})+\cdots+w(b_1,c_1) \\
    &\qquad \leq w(b_{k+1},c_{k+1})+\cdots+w(b_{j+1},c_{j+1})+w(b_j,d_j)+w(a_{j-1},d_{j-1})+\cdots+w(a_1,d_1).
    \end{aligned}
    $$
    
    Isto tako, podjela $[a_{k},d_{k}],\cdots,[a_{j+1},d_{j+1}],[a_j,c_j],[b_{j-1},c_{j-1}],\cdots,[b_1,c_1]$ ima $k$ dijelova, pa vrijedi
    
    $$
    \begin{aligned}
    &w(a_{k},d_{k})+\cdots+w(a_{j+1},d_{j+1})+w(a_j,d_j)+w(a_{j-1},d_{j-1})+\cdots+w(a_1,d_1) \\
    &\qquad < w(a_{k},d_{k})+\cdots+w(a_{j+1},d_{j+1})+w(a_j,c_j)+w(b_{j-1},c_{j-1})+\cdots+w(b_1,c_1).
    \end{aligned}
    $$
    
    Ovdje je nejednakost stroga jer je $a_1 > b_1$, a po pretpostavci je $a_1$ najmanja optimalna među lijevim rubovima posljednjeg dijela svih podjela na $k$ dijelova. Zbrajanjem dviju nejednakosti dobivamo $w(b_j,c_j) + w(a_j,d_j) < w(b_j,d_j) + w(a_j,c_j)$, što proturječi nejednakosti četverokuta. Time je tvrdnja dokazana.

Pomoću ovog rezultata možemo ograničiti područje pretraživanja odluke $j$. U implementaciji $k$ prolazimo uzlazno, $i$ silazno i $j$ pretražujemo grubom silom unutar ranije određenih donje i gornje granice; time osiguravamo složenost $O(n(n+m))$.

??? warning "Napomena"
    Složenost ovog algoritma nije $O(nm)$. Ispravan izračun složenosti mora uzeti u obzir matricu stanja dimenzija $n\times m$. Budući da za problem $(k,i)$ treba razmotriti samo odluke $\operatorname{opt}(k-1,i) \leq j \leq \operatorname{opt}(k,i+1)$, ukupan broj odluka koje treba proći za probleme na jednoj sporednoj dijagonali (tj. s fiksnim $i-k$) je $O(n)$. Takvih je dijagonala ukupno $(n+m)$, pa je ukupna vremenska složenost $O(n(n+m))$.

Posljednja metoda optimizacije potječe iz sljedećeg opažanja.

???+ note "Teorem 3"
    Ako $w$ zadovoljava nejednakost četverokuta, tada je optimalno rješenje problema (2), $g(k):=f(k,n)$, konveksna funkcija od $k$.

??? note "Dokaz"
    Dokazujemo $g(k-1) + g(k+1) \ge 2g(k)$. Promotrimo optimalne podjele na $(k-1)$ odnosno $(k+1)$ dijelova: $[a_1,d_1],\cdots,[a_{k-1},d_{k-1}]$ i $[b_1,c_1],\cdots,[b_{k+1},c_{k+1}]$. Uzmimo najmanji $1 \leq j \leq k-1$ takav da je $c_{j+1} \leq d_j$; postojanje slijedi iz $c_{k} < n = d_{k-1}$. Iz minimalnosti slijedi $b_{j+1} > a_j$. Dakle, $a_j < b_{j+1} \leq c_{j+1} \leq d_j$. Slično kao gore, zamjenom stražnjih dijelova dviju postojećih podjela dobivamo sljedeće dvije podjele intervala:
    
    $$
    \begin{aligned}
    & [a_1,d_1],\cdots,[a_{j-1},d_{j-1}],[a_j,c_{j+1}],[b_{j+2},c_{j+2}],\cdots,[b_{k+1},c_{k+1}], \\
    & [b_1,c_1],\cdots,[b_j,c_j],[b_{j+1},d_j],[a_{j+1},d_{j+1}],\cdots,[a_{k-1},d_{k-1}].
    \end{aligned}
    $$
    
    Obje dobivene podjele imaju $k$ dijelova, pa iz uvjeta optimalnosti slijedi
    
    $$
    \begin{aligned}
    2g(k) &\le w(a_1,d_1) + \cdots + w(a_{j-1},d_{j-1}) + w(a_j,c_{j+1}) + w(b_{j+2},c_{j+2}) + \cdots + w(b_{k+1},c_{k+1}) \\
    &\quad + w(b_1,c_1) + \cdots + w(b_j,c_j) + w(b_{j+1},d_j) + w(a_{j+1},d_{j+1}) + \cdots + w(a_{k-1},d_{k-1}) \\
    &\le w(a_1,d_1) + \cdots + w(a_{j-1},d_{j-1}) + w(a_j,d_j) + w(a_{j+1},d_{j+1}) + \cdots + w(a_{k-1},d_{k-1}) \\
    &\quad + w(b_1,c_1) + \cdots + w(b_j,c_j) + w(b_{j+1},c_{j+1}) + w(b_{j+2},c_{j+2}) + \cdots + w(b_{k+1},c_{k+1}) \\
    &= g(k-1) + g(k+1).
    \end{aligned}
    $$
    
    Druga je nejednakost upravo nejednakost četverokuta. Time je tražena konveksnost dokazana.

Ovaj rezultat jamči da se problem može riješiti WQS binarnim pretraživanjem (u inozemstvu poznatim kao Aliens trick). Konkretno, promotrimo parametriziranu funkciju cijene $w_c(j,i):=w(j,i)+c$, riješimo problem bez ograničenja na broj intervala i dobijemo optimalno rješenje $f_c(n)$. Kako realni $c$ raste, broj intervala u pripadnom optimalnom rješenju monotono pada, pa binarnim pretraživanjem možemo naći parametar $c$ pri kojem je broj optimalnih intervala točno $m$; optimalno rješenje izvornog problema tada je $f(m,n) = f_c(n)-cm$. Realni broj $c$ može se shvatiti kao Lagrangeov multiplikator ograničenja na broj intervala. Implementacija ovog algoritma ima mnogo detalja; pogledajte stranicu [WQS binarno pretraživanje](./wqs-binary-search.md). Vremenska složenost ovog algoritma je $O(n\log n\log C)$, gdje je $C$ veličina raspona vrijednosti parametra $c$.

Tri algoritma za problem rastavljanja intervala s ograničenim brojem intervala imaju različite prednosti i mane pri različitim veličinama ulaza, pa prikladan algoritam treba odabrati prema konkretnom zadatku.

???+ example "Primjer 3: [P4767 \[IOI2000\] Poštanski uredi, pojačano](https://www.luogu.com.cn/problem/P4767)  [P6246 \[IOI2000\] Poštanski uredi, dvostruko pojačano](https://www.luogu.com.cn/problem/P6246)"
    Uz autocestu se nalazi nekoliko sela. Autocesta je predstavljena brojevnim pravcem s cijelim brojevima, a položaj svakog sela zadan je jednom cjelobrojnom koordinatom. Nema dvaju sela na istom mjestu. Udaljenost između dvaju položaja je apsolutna vrijednost razlike njihovih cjelobrojnih koordinata.
    
    Poštanski uredi gradit će se u nekima, ali ne nužno svima, od sela. Mjesta gradnje treba odabrati tako da zbroj udaljenosti svakog sela do njemu najbližeg poštanskog ureda bude najmanji mogući.
    
    Napišite program koji za zadane položaje sela i broj poštanskih ureda računa najmanji mogući zbroj udaljenosti svakog sela do najbližeg poštanskog ureda.

??? note "Ideja rješenja"
    Svako selo ima najbliži poštanski ured, pa i svaki poštanski ured ima sela koja pokriva; lako se vidi da ona čine interval.
    
    Podijelimo tih $n$ sela na $m$ intervala i u svakom intervalu odredimo jedan poštanski ured.
    
    Matematički se zna da za interval $[i,j]$ poštanski ured treba izgraditi u $\left\lfloor\dfrac{i+j}2\right\rfloor$-tom selu. Prefiksnim sumama lako računamo $w(i,j)$.
    
    Problem se svodi na problem rastavljanja intervala s ograničenim brojem intervala. Može se dokazati da funkcija $w$ zadovoljava nejednakost četverokuta. Dovoljno je izravno primijeniti gornje metode optimizacije.

??? note "Implementacija 1, druga optimizacija iz teksta, složenost $O(n(n+m))$"
    ```cpp
    --8<-- "docs/dp/code/opt/quadrangle/quadrangle_2.cpp"
    ```

??? note "Implementacija 2, WQS binarno pretraživanje, složenost $O(n\log n\log C)$"
    ```cpp
    --8<-- "docs/dp/code/opt/quadrangle/quadrangle_3.cpp"
    ```

## Problem spajanja intervala

Druga klasa problema dinamičkog programiranja koja se može optimizirati nejednakošću četverokuta jest problem spajanja intervala: $n$ intervala $[i,i]$ duljine jedan treba spajati po dva dok se ne dobije interval $[1,n]$. Svako spajanje $[j,k]$ i $[k+1,i]$ košta $w(j,i)$. Traži se način spajanja najmanje cijene. Za takve probleme imamo sljedeću 2D1D jednadžbu prijelaza stanja:

$$
f(j,i) = \min_{j \leq k < i} f(j,k) + f(k+1,i) + w(j,i) \qquad (1\le j< i\le n) \tag{3}
$$

Ovdje je početna cijena $f(i,i)=0$. Ukupna složenost algoritma grubom silom je $O(n^3)$, a kad postoji monotonost odluka, može se optimizirati na $O(n^2)$. Taj je algoritam prvi predložio Knuth pri rješavanju problema optimalnog binarnog stabla pretraživanja, a dalje ga je proučio i sažeo Yao; u inozemstvu je poznat kao Knuth's optimization ili Knuth–Yao speedup.

Osim nejednakosti četverokuta, monotonost odluka u problemu spajanja intervala zahtijeva i da funkcija cijene bude monotona s obzirom na uključivanje intervala.

-   **Monotonost s obzirom na uključivanje intervala**: ako za sve $a \leq b \leq c \leq d$ vrijedi

    $$
    w(b,c) \leq w(a,d),
    $$

    kažemo da je funkcija $w$ monotona s obzirom na relaciju uključivanja intervala.

To je zapravo uvjet prvog reda na funkciju cijene: $w(j,i)$ pada po $j$, a raste po $i$.

???+ note "Lema 1"
    Ako $w$ zadovoljava monotonost s obzirom na uključivanje intervala i nejednakost četverokuta, tada stanje $f(j,i)$ zadovoljava nejednakost četverokuta.

??? note "Dokaz"
    Neka je $a \leq b \leq c \leq d$. Dokazujemo $f(a,d) + f(b,c) \geq f(a,c) + f(b,d)$ indukcijom po $d-a$. Kad je $a=b$ ili $c=d$, tražena je tvrdnja jednakost. U općem slučaju razlikujemo slučajeve prema položaju $d'=\operatorname{opt}(a,d)$.
    
    Prvi slučaj: $c \leq d'$ ili $d' < b$, tj. $[b,c]$ je sadržan u $[a,d']$ ili u $[d'+1,d]$.
    
    Bez smanjenja općenitosti neka je $c \leq d'$; drugi je slučaj analogan. Tada vrijedi
    
    $$
    \begin{aligned}
    f(a,d) + f(b,c)
    & = f(a,d') + f(d'+1,d) + w(a,d) + f(b,c) \\
    & \geq f(a,c) + f(b,d') + f(d'+1,d) + w(a,d) \\
    & \geq f(a,c) + f(b,d') + f(d'+1,d) + w(b,d) \\
    & \geq f(a,c) + f(b,d).
    \end{aligned}
    $$
    
    Ovdje prva nejednakost slijedi iz pretpostavke indukcije $f(a,c) + f(b,d') \leq f(a,d') + f(b,c)$, druga iz monotonosti s obzirom na uključivanje intervala $w(b,d) \leq w(a,d)$, a treća iz uvjeta optimalnosti $f(b,d) \leq f(b,d') + f(d'+1,d) + w(b,d)$.
    
    Drugi slučaj: $b \leq d' < c$, tj. $d'$ leži u $[b,c]$. Tada promatramo položaj $c'=\operatorname{opt}(b,c)$.
    
    Bez smanjenja općenitosti neka je $c' \leq d'$, tj. $[b,c']$ je sadržan u $[a,d']$; drugi je slučaj analogan. Tada vrijedi
    
    $$
    \begin{aligned}
    f(a,d) + f(b,c)
    & = f(a,d') + f(d'+1,d) + w(a,d) + f(b,c') + f(c'+1,c) + w(b,c) \\
    & \geq f(a,c') + f(c'+1,c) + w(b,c) + f(b,d') + f(d'+1,d) + w(a,d) \\
    & \geq f(a,c') + f(c'+1,c) + w(a,c) + f(b,d') + f(d'+1,d) + w(b,d) \\
    & \geq f(a,c) + f(b,d).
    \end{aligned}
    $$
    
    Ovdje prva nejednakost slijedi iz pretpostavke indukcije $f(a,c') + f(b,d') \leq f(a,d') + f(b,c')$, druga iz nejednakosti četverokuta $w(a,c) + w(b,d) \leq w(a,d) + w(b,c)$, a treća iz uvjeta optimalnosti za $f(a,c)$ i $f(b,d)$.

???+ note "Teorem 4"
    Ako $w$ zadovoljava monotonost s obzirom na uključivanje intervala i nejednakost četverokuta, tada najmanja optimalna odluka $\operatorname{opt}(j,i)$ u problemu (3) zadovoljava
    
    $$
    \operatorname{opt}(j,i-1) \leq \operatorname{opt}(j,i) \leq \operatorname{opt}(j+1,i). \qquad (j + 1 < i)
    $$

??? note "Dokaz"
    Lema 1 već daje da $f(j,i)$ zadovoljava nejednakost četverokuta, pa funkcija cilja $f(j,k) + f(k+1,i) + w(j,i)$ za fiksni $j$, kao funkcija od $(k,i)$, zadovoljava nejednakost četverokuta; prema teoremu 1 slijedi $\operatorname{opt}(j,i-1) \leq \operatorname{opt}(j,i)$. Uočimo da članovi koji ne sadrže istodobno $(k,i)$ ne utječu na valjanost nejednakosti četverokuta. Slično, za fiksni $i$ ona kao funkcija od $(j,k)$ također zadovoljava nejednakost četverokuta, pa je $\operatorname{opt}(j,i) \leq \operatorname{opt}(j+1,i)$. Time je tvrdnja dokazana.

Ovim rezultatom također možemo ograničiti područje pretraživanja odluke $k$. Ovdje duljinu intervala $i-j+1$ prolazimo uzlazno, zatim sve intervale $[j,i]$ iste duljine, grubom silom pretražujemo sve $k$ između $\operatorname{opt}(j,i-1)$ i $\operatorname{opt}(j+1,i)$, dobivamo optimalno rješenje $f(j,i)$ i bilježimo najmanju optimalnu odluku $\operatorname{opt}(j,i)$. Za sve intervale iste duljine ukupna duljina prostora odluka u ovom algoritmu je $O(n)$, a broj mogućih duljina intervala također je $O(n)$, pa je ukupna složenost algoritma $O(n^2)$.

???+ example "Primjer implementacije"
    ```cpp
    --8<-- "docs/dp/code/opt/quadrangle/quadrangle-knuth-optimization.cpp:core"
    ```

## Klase funkcija koje zadovoljavaju nejednakost četverokuta

Da bismo lakše dokazali da funkcija zadovoljava nejednakost četverokuta, imamo sljedećih nekoliko svojstava:

**Svojstvo 1**: ako funkcije $w_1(j,i)$ i $w_2(j,i)$ obje zadovoljavaju nejednakost četverokuta (ili monotonost s obzirom na uključivanje intervala), tada za sve $c_1,c_2\geq 0$ i funkcija $c_1w_1+c_2w_2$ zadovoljava nejednakost četverokuta (ili monotonost s obzirom na uključivanje intervala).

**Svojstvo 2**: ako postoje funkcije $f(x)$ i $g(x)$ takve da je $w(j,i) = f(j)-g(i)$, tada funkcija $w$ zadovoljava jednakost četverokuta. Ako su funkcije $f$ i $g$ monotono rastuće, funkcija $w$ zadovoljava i monotonost s obzirom na uključivanje intervala.

**Svojstvo 3**: neka je $h(x)$ monotono rastuća konveksna funkcija. Ako funkcija $w(j,i)$ zadovoljava nejednakost četverokuta i monotona je s obzirom na uključivanje intervala, tada i kompozicija $h(w(j,i))$ zadovoljava nejednakost četverokuta i monotonost s obzirom na uključivanje intervala.

**Svojstvo 4**: neka je $h(x)$ konveksna funkcija. Ako funkcija $w(j,i)$ zadovoljava jednakost četverokuta i monotona je s obzirom na uključivanje intervala, tada i kompozicija $h(w(j,i))$ zadovoljava nejednakost četverokuta.

Najprije jedno pojašnjenje: definicija konveksne funkcije (convex function) u kineskim se udžbenicima razlikuje; ovdje konveksna funkcija znači funkciju konveksnu prema dolje, tj. (ako je derivabilna) funkciju čija je prva derivacija monotono rastuća.

??? note "Dokaz"
    Prva dva svojstva lako se dokazuju iz definicije; dokazujemo treće, a dokaz svojstva 4 je sličan. Budući da je $h(x)$ monotona, $h(w(j,i))$ očito čuva monotonost s obzirom na uključivanje intervala. Ključan je dokaz nejednakosti četverokuta.
    
    U tu svrhu promotrimo mješovitu diferenciju drugog reda na $a \leq j \leq b \leq c \leq i \leq d$.
    
    $$
    \begin{aligned}
    \Delta_i\Delta_j h\left(w(j,i)\right)
    &= h\left(w(b,d)\right) - h\left(w(a,c) + \Delta_jw(j,c) + \Delta_iw(a,i)\right) \\
    &\quad + h\left(w(a,c) + \Delta_jw(j,c) + \Delta_iw(a,i)\right) - h\left(w(a,c) + \Delta_jw(j,c)\right) \\
    &\quad - h\left(w(a,c) + \Delta_iw(a,i)\right) + h\left(w(a,c)\right).
    \end{aligned}
    $$
    
    Ovdje je, prema intervalnoj monotonosti, $\Delta_iw(a,i) := w(a,d) - w(a,c) \geq 0$ i $\Delta_jw(j,c) := w(b,c) - w(a,c) \leq 0$. Zbog konveksnosti $h(x)$ za $t_1,t_2\geq 0$ vrijedi $h(x + t_1 - t_2) - h(x + t_1) \leq h(x - t_2) - h(x)$, pa je zbroj posljednjih dvaju redaka nužno nepozitivan. Ujedno, zbog nejednakosti četverokuta, $w(b,d) \leq w(a,c) + \Delta_jw(j,c) + \Delta_iw(a,i) = w(b,c) + w(a,d) - w(a,c)$, pa je, budući da je $h(x)$ monotono rastuća, i razlika u prvom retku nužno nepozitivna. Dakle, ukupna mješovita diferencija drugog reda je nepozitivna. To je upravo nejednakost četverokuta.
    
    Ovaj je dokaz zapravo diskretna inačica sljedećeg dokaza derivacijama.
    
    $$
    \frac{\partial^2}{\partial x\partial y}h(w(x,y)) = h''(w(x,y))\frac{\partial }{\partial x}w(x,y)\frac{\partial}{\partial y}w(x,y) + h'(w(x,y))\frac{\partial^2}{\partial x\partial y}w(x,y) \leq 0.
    $$
    
    To očito vrijedi uz uvjete $h' \geq 0$, $h'' \geq 0$, $w_x \leq 0$, $w_y \geq 0$ i $w_{xy} \leq 0$. Pritom monotonost s obzirom na uključivanje intervala daje uvjet prvog reda na $w$, a nejednakost četverokuta uvjet drugog reda.

## Zadaci

-   [Codeforces - Ciel and Gondolas](https://codeforces.com/contest/321/problem/E)(Oprez s ulazom/izlazom!)
-   [SPOJ - LARMY](https://www.spoj.com/problems/LARMY/)
-   [Codechef - CHEFAOR](https://www.codechef.com/problems/CHEFAOR)
-   [Hackerrank - Guardians of the Lunatics](https://www.hackerrank.com/contests/ioi-2014-practice-contest-2/challenges/guardians-lunatics-ioi14)
-   [ACM ICPC World Finals 2017 - Money](https://open.kattis.com/problems/money)

## Literatura i bilješke

-   [Quora Answer by Michael Levin](https://www.quora.com/What-is-divide-and-conquer-optimization-in-dynamic-programming)
-   [Video Tutorial by "Sothe" the Algorithm Wolf](https://www.youtube.com/watch?v=wLXEWuDWnzI)
-   [Divide and Conquer DP](https://cp-algorithms.com/dynamic_programming/divide-and-conquer-dp.html)
-   [Knuth's Optimization](https://cp-algorithms.com/dynamic_programming/knuth-optimization.html)
-   [Quadrangle Inequality Properties](https://codeforces.com/blog/entry/86306)
-   [Wang Qinshi, „Analiza jedne klase metoda binarnog pretraživanja” (王钦石《浅析一类二分方法》)](https://github.com/hzwer/shareOI/blob/master/%E5%9F%BA%E7%A1%80%E7%AE%97%E6%B3%95/%E6%B5%85%E6%9E%90%E4%B8%80%E7%B1%BB%E4%BA%8C%E5%88%86%E6%96%B9%E6%B3%95_%E7%8E%8B%E9%92%A6%E7%9F%B3.pdf)
-   [簡易版 LARSCH Algorithm by noshi91](https://noshi91.hatenablog.com/entry/2023/02/18/005856)
-   [Nejednakost četverokuta i monotonost odluka by b6e0\_ - Luogu kolumna](https://www.luogu.com.cn/article/h81hh5lk)
-   [Jednostavna inačica algoritma LARSCH za online monotonost odluka by Register\_int - Luogu kolumna](https://www.luogu.com.cn/article/vqf42hah)

[^cmp-min-opt]: „Lošije” i „bolje” u opisu algoritma treba shvatiti kao leksikografsku usporedbu u kojoj se najprije uspoređuje vrijednost funkcije, a zatim odluka. U tom leksikografskom poretku „bolje” znači da je ili vrijednost funkcije manja, ili je vrijednost jednaka, a odluka manja.

[^larsch]: Larmore, Lawrence L., and Baruch Schieber. "On-line dynamic programming with applications to the prediction of RNA secondary structure." Journal of Algorithms 12, no. 3 (1991): 490-515.
