---
title: Dirichletova metoda hiperbole i Du sito
---

Predznanje: [Dirichletova konvolucija](./dirichlet.md), [blokovsko dijeljenje po cjelobrojnom kvocijentu](./sqrt-decomposition.md)

Ovaj članak predstavlja Dirichletovu metodu hiperbole, kojom se u sublinearnoj vremenskoj složenosti može izračunati prefiksna suma Dirichletove konvolucije dviju teorijsko-brojevnih funkcija. Analizom tog algoritma dolazi se do pojma blokovskog sita; na temelju toga članak dalje predstavlja metodu brzog računanja konvolucije blokovskih sita. Na kraju članak predstavlja Du sito, kojim se može izračunati prefiksna suma kvocijenta dviju teorijsko-brojevnih funkcija u smislu Dirichletove konvolucije.

## Dirichletova metoda hiperbole

Dirichletova metoda hiperbole može se koristiti za računanje prefiksne sume Dirichletove konvolucije dviju teorijsko-brojevnih funkcija.

Neka su $f,g,h$ teorijsko-brojevne funkcije i $h = f\ast g$. Tada je, prema definiciji Dirichletove konvolucije, prefiksna suma $h$

$$
H(n) = \sum_{k=1}^nh(k) = \sum_{k=1}^n\sum_{xy=k}f(x)g(y).
$$

Skup točaka po kojima suma prolazi upravo je skup cjelobrojnih točaka u prvom kvadrantu (bez koordinatnih osi) ispod hiperbole $xy=n$. Pridružimo li cjelobrojnoj točki $(x,y)$ težinu $f(x)g(y)$, onda je $H(n)$ zbroj tih težina.

![](./images/dirichlet-hyperbola.svg)

Kao što slika pokazuje, taj se zbroj težina može izračunati načelom uključivanja-isključivanja:

$$
H(n) = \sum_{x=1}^{\lfloor x_0\rfloor}f(x)G\left(\left\lfloor\dfrac{n}{x}\right\rfloor\right) + \sum_{y=1}^{\lfloor y_0\rfloor}F\left(\left\lfloor\dfrac{n}{y}\right\rfloor\right)g(y) - F(\lfloor x_0\rfloor)G(\lfloor y_0\rfloor).
$$

Pritom su $F,G$ redom funkcije prefiksnih suma od $f,g$, a $(x_0,y_0)$ je proizvoljna točka na hiperboli $xy=n$. U izrazu prvi član predstavlja zbroj težina zelenog područja na slici, drugi član zbroj težina narančastog područja, a treći član zbroj težina presjeka tih dvaju područja. Taj izraz ima samo $\lfloor x_0\rfloor + \lfloor y_0\rfloor + 1$ članova. Za razumno odabranu točku $(x_0,y_0)$ njegova je složenost računanja znatno bolja od izravnog (brute-force) računanja prefiksne sume $h(n)$. To je **Dirichletova metoda hiperbole** (Dirichlet hyperbola method).

### Računanje vrijednosti prefiksne sume konvolucije

Najosnovnija primjena Dirichletove metode hiperbole jest računanje vrijednosti $H(n)$ funkcije prefiksnih suma u jednoj točki.

Ako su vrijednosti $F,G$ poznate (ili se mogu izračunati u $O(1)$), a time su poznate i vrijednosti $f,g$, onda se svaki član u izrazu Dirichletove metode hiperbole može izračunati u $O(1)$, pa je ukupna vremenska složenost $O(x_0+y_0)$. Budući da je $x_0y_0=n$, iz nejednakosti između aritmetičke i geometrijske sredine slijedi da se za $x_0=y_0=\sqrt{n}$ dobiva najmanja vremenska složenost $O(\sqrt{n})$.

To nije novi rezultat. Stavimo li u izrazu Dirichletove metode hiperbole $x_0 > n$, dobivamo

$$
H(n) = \sum_{x=1}^nf(x)G\left(\left\lfloor\dfrac{n}{x}\right\rfloor\right).
$$

Tehnikom [blokovskog dijeljenja po cjelobrojnom kvocijentu](./sqrt-decomposition.md) taj se izraz, kad su vrijednosti $F,G$ poznate, može izračunati u vremenu $O(\sqrt{n})$. To je zapravo gotovo ekvivalentno algoritmu dobivenom u ovom odjeljku: obje metode zahtijevaju u osnovi iste poznate informacije, a izrazi koje računaju otprilike su isti.

??? note "Objašnjenje ekvivalentnosti"
    Pažljivijim promatranjem postupka računanja blokovskim dijeljenjem vidi se da se zapravo računa izraz
    
    $$
    H(n) = \sum_{y\in D(n)}\left(F\left(\left\lfloor\dfrac{n}{y}\right\rfloor\right)-F\left(\left\lfloor\dfrac{n}{y+1}\right\rfloor\right)\right)G(y).
    $$
    
    Pritom je $D(n) = \left\{\left\lfloor\dfrac{n}{x}\right\rfloor : 1 \le x \le n,~x\in\mathbf N_+\right\}$ skup ključnih točaka blokovskog dijeljenja.
    
    Prema svojstvima blokovskog dijeljenja, za $x\le\sqrt{n}$ visine odgovarajućih blokova $y = \lfloor n/x\rfloor$ međusobno su različite, pa su duljine tih blokova sve jednake $1$, tj.
    
    $$
    \left\lfloor\dfrac{n}{y+1}\right\rfloor + 1 = x = \left\lfloor\dfrac{n}{y}\right\rfloor.
    $$
    
    Stoga je suma koja odgovara tim blokovima
    
    $$
    I_1 = \sum_{x=1}^{\lfloor\sqrt{n}\rfloor}\left(F(x)-F(x-1)\right)G\left(\left\lfloor\dfrac{n}{x}\right\rfloor\right) = \sum_{x=1}^{\lfloor\sqrt{n}\rfloor}f(x)G\left(\left\lfloor\dfrac{n}{x}\right\rfloor\right).
    $$
    
    Za preostale blokove visina $y$ prolazi $1,2,\cdots,y^*= \left\lfloor\dfrac{n}{\lfloor\sqrt{n}\rfloor + 1}\right\rfloor$. Primjenom [Abelove transformacije](https://en.wikipedia.org/wiki/Summation_by_parts) (tj. sumacijskog oblika parcijalne integracije) na preostalu sumu dobivamo
    
    $$
    \begin{aligned}
    I_2 &= \sum_{y=1}^{y^*}\left(F\left(\left\lfloor\dfrac{n}{y}\right\rfloor\right)-F\left(\left\lfloor\dfrac{n}{y+1}\right\rfloor\right)\right)G(y) \\
    &= \sum_{y=1}^{y^*}F\left(\left\lfloor\dfrac{n}{y}\right\rfloor\right)g(y) - F\left(\left\lfloor\dfrac{n}{y^*+1}\right\rfloor\right)G(y^*).
    \end{aligned}
    $$
    
    Svojstva blokovskog dijeljenja kažu da je $\lfloor n/\lfloor \sqrt{n}\rfloor\rfloor \ge \lfloor \sqrt{n}\rfloor$. Razlikujemo dva slučaja:
    
    -   Kada je $\lfloor n/\lfloor \sqrt{n}\rfloor\rfloor = \lfloor \sqrt{n}\rfloor$, nužno je $y^* < \lfloor \sqrt{n}\rfloor$. Budući da je taj blok susjedan bloku u kojem je $x = \lfloor \sqrt{n}\rfloor$, visine blokova mogu se razlikovati samo za točno jedan, tj. $y^* = \lfloor \sqrt{n}\rfloor - 1$. Tada vrijedi
    
        $$
        \begin{aligned}
        I_2 &= \sum_{y=1}^{\lfloor\sqrt{n}\rfloor-1}F\left(\left\lfloor\dfrac{n}{y}\right\rfloor\right)g(y) - F(\lfloor\sqrt{n}\rfloor)G(\lfloor\sqrt{n}\rfloor-1)\\
        &= \sum_{y=1}^{\lfloor\sqrt{n}\rfloor-1}F\left(\left\lfloor\dfrac{n}{y}\right\rfloor\right)g(y) -  F(\lfloor\sqrt{n}\rfloor)\left(G(\lfloor\sqrt{n}\rfloor) - g(\lfloor\sqrt{n}\rfloor)\right) \\
        &= \sum_{y=1}^{\lfloor\sqrt{n}\rfloor}F\left(\left\lfloor\dfrac{n}{y}\right\rfloor\right)g(y) - F(\lfloor\sqrt{n}\rfloor)G(\lfloor\sqrt{n}\rfloor).
        \end{aligned}
        $$
    
    -   Kada je $\lfloor n/\lfloor \sqrt{n}\rfloor\rfloor > \lfloor \sqrt{n}\rfloor$, nužno je $y^* = \lfloor \sqrt{n}\rfloor$. Izravnim uvrštavanjem u sumu dobivamo
    
        $$
        I_2 = \sum_{y=1}^{\lfloor\sqrt{n}\rfloor}F\left(\left\lfloor\dfrac{n}{y}\right\rfloor\right)g(y) - F(\lfloor\sqrt{n}\rfloor)G(\lfloor\sqrt{n}\rfloor).
        $$
    
    Ukupno, osim jedne Abelove transformacije, postupak računanja blokovskim dijeljenjem zapravo računa sljedeći izraz:
    
    $$
    H(n) = \sum_{x=1}^{\lfloor\sqrt{n}\rfloor}f(x)G\left(\left\lfloor\dfrac{n}{x}\right\rfloor\right) + \sum_{y=1}^{\lfloor\sqrt{n}\rfloor}F\left(\left\lfloor\dfrac{n}{y}\right\rfloor\right)g(y) - F(\lfloor\sqrt{n}\rfloor)G(\lfloor\sqrt{n}\rfloor).
    $$
    
    To je upravo izraz Dirichletove metode hiperbole za $(x_0,y_0)=(\sqrt{n},\sqrt{n})$. Stoga možemo reći da su postupci računanja obaju algoritama gotovo ekvivalentni. Štoviše, budući da Dirichletova metoda hiperbole koristi više svojstava blokovskog dijeljenja i izbjegava nepotrebna računanja naivnog blokovskog dijeljenja, ima nešto manju konstantu.

Pri rješavanju stvarnih problema uvjet da su vrijednosti $F,G$ poznate može biti prejak. Međutim, Dirichletova metoda hiperbole (ili odgovarajuće blokovsko dijeljenje) zapravo ne zahtijeva informacije o svim vrijednostima $F,G$. Promotrimo li izraz za sumu, vidimo da su zapravo potrebne samo vrijednosti $F$ i $G$ na skupu ključnih točaka blokovskog dijeljenja

$$
D(n) = \left\{\left\lfloor\dfrac{n}{x}\right\rfloor : 1 \le x \le n,~x\in\mathbf N_+\right\}
$$

To je ujedno skup svih visina blokova i skup svih desnih krajeva blokova. Uočimo da prema [svojstvima](./sqrt-decomposition.md#svojstva) blokovskog dijeljenja taj skup sadrži sve cijele brojeve $1\le x\le\sqrt{n}$, pa je poznavanje vrijednosti $F,G$ na $D(n)$ ekvivalentno poznavanju vrijednosti $f,g$ u svim točkama $1\le x\le\sqrt{n}$. Veličina tog skupa je $\Theta(\sqrt{n})$, pa je pri računanju $H(n)$ dovoljno znati vrijednosti $F,G$ na rijetkom skupu točaka. To je opažanje ključno za optimizaciju računanja prefiksnih suma teorijsko-brojevnih funkcija.

## Blokovsko sito i njegova konvolucija

Ponekad $h=f\ast g$ nije funkcija čiju prefiksnu sumu na kraju treba izračunati, nego samo jedan od međukoraka. Prema prethodnoj analizi, za daljnje računanje treba odrediti vrijednosti funkcije prefiksnih suma $H$ na skupu $D(n)$. To nazivamo **blokovskim sitom** (block sieve) teorijsko-brojevne funkcije $h$:

$$
\mathcal S_h(n) = \left\{H(x) : x \in D(n)\right\}.
$$

Ovaj odjeljak razmatra metode računanja problema **konvolucije blokovskih sita**: za poznata blokovska sita $f,g$ odrediti blokovsko sito njihove Dirichletove konvolucije $h = f\ast g$.

### Naivni algoritam

Naivni algoritam promatra računanje blokovskog sita kao $|D(n)|$ računanja vrijednosti prefiksne sume. Ukupna je vremenska složenost tog pristupa

$$
\begin{aligned}
O\left(\sum_{d\in D(n)}\sqrt{d}\right) &= O\left(\sum_{x=1}^{\lfloor\sqrt{n}\rfloor}\sqrt{x} + \sum_{x=1}^{\lfloor\sqrt{n}\rfloor}\sqrt{\dfrac{n}{x}}\right) \\
&= O\left(\int_1^{\sqrt{n}}\sqrt{x}\mathrm{d}x + \int_1^{\sqrt{n}}\sqrt{\dfrac{n}{x}}\mathrm{d}x\right)\\
&= O(n^{3/4}).
\end{aligned}
$$

Upravo zato što je blokovsko sito rijetko, cijelo se blokovsko sito može izračunati u sublinearnom vremenu.

Ipak, taj je algoritam očito previše grub. Manji elementi skupa $D(n)$ relativno su gusti, pa se susjedne prefiksne sume u blokovskom situ ne razlikuju mnogo; sasvim je moguće izravno izračunati vrijednosti konvolucije $h$ i zatim njihovu prefiksnu sumu. To je brže nego za svaku točku zasebno računati vrijednost prefiksne sume. Primjerice, računanje vrijednosti prefiksne sume zasebno za $x = 1,2,\cdots,\lfloor\sqrt{n}\rfloor$ zahtijeva

$$
O\left(\sum_{x=1}^{\lfloor\sqrt{n}\rfloor}\sqrt{x}\right) = O(n^{3/4})
$$

vremena; no izravno računanje vrijednosti $h$ u tim točkama i zatim zbrajanje zahtijeva samo $O(n^{1/2}\log n)$ vremena. Unatoč tome, ako su poznata samo blokovska sita $f,g$ i ništa više, tom se idejom složenost algoritma ne može dalje optimizirati. Naime, blokovsko sito sadrži informacije o vrijednostima samo za $x \le \sqrt{n}$, pa se vrijednosti $h$ mogu izračunati najviše u točkama $1\le x\le\sqrt{n}$, dok računanje preostalih vrijednosti prefiksne sume i dalje zahtijeva $O(n^{3/4})$ vremena.

### Optimizacija pomoću informacija o vrijednostima

Ako poznate informacije osim blokovskih sita $f,g$ uključuju i više njihovih vrijednosti, složenost se tog algoritma doista može poboljšati. U praksi se taj algoritam obično primjenjuje kad se vrijednosti $f,g$ mogu brzo predračunati.

Odaberimo $z \ge \sqrt{n}$. Blokovsko sito konvolucije $h$ dijelimo na dva dijela:

-   Izračunamo vrijednosti konvolucije $h$ od $f\ast g$ u točkama $1\le x \le z$, a zatim izravnim zbrajanjem dobijemo vrijednosti $H$ u točkama $1\le x\le z$.
-   Za $x\in D(n)$ takve da je $x > z$ vrijednost $H$ u točki $x$ računamo Dirichletovom metodom hiperbole.

U općem slučaju vremenska je složenost tog pristupa

$$
\begin{aligned}
O\left(z\log z + \sum_{d\in D(n),~d\ge z}\sqrt{d}\right) &= O\left(z\log z + \sum_{x=1}^{n/z}\sqrt{\dfrac{n}{x}}\right)\\
&= O\left(z\log z + \int_1^{n/z}\sqrt{\dfrac{n}{x}}\mathrm{d}x\right)\\
&= O\left(z\log z + \dfrac{n}{\sqrt{z}}\right).
\end{aligned}
$$

Za $z=\left(\dfrac{n}{\log n}\right)^{2/3}$ ukupna vremenska složenost je najmanja i iznosi $O\left(n^{2/3}(\log n)^{1/3}\right)$.

Naravno, složenost [računanja vrijednosti](./dirichlet.md#računanje-dirichletove-konvolucije) Dirichletove konvolucije ovisi o svojstvima $f,g,h$. Kad $f,g,h$ imaju posebna svojstva, optimalna točka podjele i složenost malo se razlikuju:

-   Ako je $f$ ili $g$ multiplikativna, onda je za $z=\left(\dfrac{n}{\log\log n}\right)^{2/3}$ ukupna vremenska složenost najmanja i iznosi $O\left(n^{2/3}(\log\log n)^{1/3}\right)$.
-   Ako je $h$ multiplikativna, onda je za $z=n^{2/3}$ ukupna vremenska složenost najmanja i iznosi $O(n^{2/3})$.

Za primjenu ove optimizacije nisu potrebne sve vrijednosti $f,g$, nego samo njihove vrijednosti u točkama $1\le x\le z$. Budući da ovaj algoritam daje i vrijednosti $h$ u točkama $1\le x\le z$, kad je $h$ međurezultat, i vrijednosti $h$ mogu se iskoristiti za optimizaciju daljnjeg računanja. Blokovsko sito teorijsko-brojevne funkcije zajedno s tim vrijednostima čini pojačanu verziju blokovskog sita: to su sve informacije potrebne za računanje prefiksne sume konvolucije u vremenu $O(n^{2/3+\varepsilon})$.

### Brza konvolucija blokovskih sita

Predznanje: [brza Fourierova transformacija](../poly/fft.md)

???+ warning "Napomena"
    Početnici mogu preskočiti ovaj odjeljak.

Ovaj odjeljak razmatra algoritam brze konvolucije blokovskih sita koji je Zhou Kangyang predložio u radu za kineski nacionalni pripremni tim 2024. godine. On u vremenu $O(\sqrt{n}\log^2n)$ iz blokovskih sita $\mathcal S_f$ i $\mathcal S_g$ računa vrijednosti $\mathcal S_h$ njihove konvolucije. Taj algoritam ne ovisi o dodatnim informacijama o vrijednostima ni o multiplikativnosti teorijsko-brojevnih funkcija, ali je implementacija složenija.

Problem konvolucije blokovskih sita traži da se izračunaju prefiksne sume

$$
h(z) = \sum_{xy=z} f(x)g(y)
$$

na blokovskom situ $D(n) = \{\left\lfloor n / t\right\rfloor : 1\le t \le n\}$. Za taj se problem pojedinačni doprinos može označiti trojkom $(x,y,t)$, tj. postupkom pribrajanja člana $f(x)g(y)$ prefiksnoj sumi u točki $\left\lfloor n / t\right\rfloor$. Algoritam te doprinose obrađuje podijeljene u nekoliko skupina.

Prvo razmotrimo doprinose svih točaka s $x > \sqrt{n}$ ovom nizu prefiksnih suma; doprinosi s $y > \sqrt{n}$ obrađuju se analogno. Budući da svi doprinosi moraju zadovoljavati $xy \le \lfloor n / t\rfloor$, tj. $xyt \le n$, dovoljno je nabrojiti sve moguće $t,y$ i pomoću tehnike prefiksnih suma te informacija iz blokovskog sita $\mathcal S_f$ taj se dio doprinosa može izračunati u vremenu $O(\sum_{t,y: ty\le\sqrt{n}} 1) = O(\sqrt{n}\log n)$.

Zatim razmotrimo dio doprinosa za koje je $\left\lfloor n / t\right\rfloor\le\sqrt{n}$. Taj se dio također može obaviti izravnim nabrajanjem svih mogućih $x,y$, a vremenska je složenost i dalje $O(\sum_{x,y:xy\le\sqrt{n}}1) = O(\sqrt{n}\log n)$. Tim se dijelom zapravo dobivaju prve $\lfloor\sqrt{n}\rfloor$ vrijednosti funkcije $h$ na $D(n)$.

Razmotrimo preostale doprinose, tj. one za koje je $x,y\le\sqrt{n}$ i $\left\lfloor n / t\right\rfloor > \sqrt{n}$. Svi doprinosi moraju zadovoljavati $xyt\le n$, tj. $\ln x + \ln y \le \ln(n/t)$. Uzmimo pozitivan broj $S$; taj se uvjet može približno procijeniti pomoću $\lceil S\ln x\rceil + \lceil S\ln y\rceil \le S\ln(n/t)$. Definirajmo polinome $\sigma_f(u)$ i $\sigma_g(u)$ tako da su njihovi koeficijenti $[u^k]\sigma_f$ i $[u^k]\sigma_g$ redom jednaki zbroju vrijednosti $f(x)$ za koje je $\lceil S\ln x\rceil = k$ i zbroju vrijednosti $g(y)$ za koje je $\lceil S\ln y\rceil = k$ (promatramo samo dio s $x,y\le\sqrt{n}$). Brzom Fourierovom transformacijom (FFT) možemo dobiti njihov umnožak $\sigma_f\sigma_g$, čiji koeficijent $[u^k](\sigma_f\sigma_g)$ predstavlja zbroj $f(x)g(y)$ za koje je $\lceil S\ln x\rceil + \lceil S\ln y\rceil = k$. Stoga je za svaki preostali $\lfloor n/t\rfloor$ u $D(n)$ dovoljno pronaći najveću vrijednost $k$ koja zadovoljava $k \le S\ln(n/t)$ i dobivamo procjenu tog dijela doprinosa.

Naposljetku za taj dio doprinosa provodimo ispravak pogreške. Prethodno smo uvjet $\ln x + \ln y \le \ln(n/t)$ pokušali aproksimirati jačim uvjetom $\lceil S\ln x\rceil + \lceil S\ln y\rceil \le S\ln(n/t)$, čime je dio doprinosa možda propušten. To se može dogoditi samo kada je $\lceil S\ln x\rceil + \lceil S\ln y\rceil > S\ln(n/t)$, pa vrijedi

$$
S\ln x + 1 +  S\ln y + 1 \ge \lceil S\ln x\rceil + \lceil S\ln y\rceil >  S\ln(n/t) \ge S\ln x + S\ln y.
$$

To je ekvivalentno s

$$
xyt \in (n\mathrm{e}^{-2/S},n].
$$

To je interval duljine $O(n/S)$. Nabrajanjem svih mogućih doprinosa $(x,y,t)$ unutar intervala i provjerom jednog po jednog je li propušten dovršavamo ispravak pogreške. Da bismo brzo nabrojili sve doprinose unutar intervala, možemo najprije prosijati sve proste brojeve koji ne prelaze $\sqrt{n}$, a zatim tim prostim brojevima dijeliti cijele brojeve u intervalu; preostali faktor nužno je prost broj veći od $\sqrt{n}$, čime dobivamo rastav na proste faktore svih cijelih brojeva u intervalu, a potom možemo brzo nabrojiti sve moguće $(x,y,t)$.

Promotrimo vremensku složenost računanja ovog posljednjeg dijela doprinosa. Pri procjeni doprinosa treba pomnožiti polinome duljine $S\log n$, što ima vremensku složenost $O(S\log n\log(S\log n))$. Pri ispravku pogreške vremenska složenost predračuna rastava na proste faktore iznosi $O(\sqrt{n}+(n/S)\log\log n)$, a vremenska složenost nabrajanja svih doprinosa u intervalu iznosi $O(\sum_{k\in(n\mathrm{e}^{-2/S},n]}d_3(k))$, gdje $d_3(n)$ označava broj načina da se $n$ zapiše kao umnožak triju uređenih cijelih brojeva. Rezultat analitičke teorije brojeva[^piltz] kaže:

$$
\sum_{k\le n}d_3(k) = nP(\log n) + O(n^{43/96+\varepsilon}),
$$

gdje je $P(\cdot)$ polinom drugog stupnja. Budući da je vremenska složenost prvih dvaju koraka već $O(\sqrt{n}\log n)$, zanemarimo li sve članove $o(\sqrt{n}\log n)$, vremenska složenost računanja ovog posljednjeg dijela doprinosa iznosi

$$
O\left(S\log n\log(S\log n) + \dfrac{n}{S} \log^2n\right).
$$

Uzmemo li $S = \sqrt{n}$, dobivamo vremensku složenost $O(\sqrt{n}\log^2n)$. To je ujedno ukupna vremenska složenost algoritma.

??? example "Referentna implementacija"
    ```cpp
    --8<-- "docs/math/code/hyperbola/fast_bs_conv.cpp:core"
    ```

## Du sito

Prethodno smo raspravili kako izračunati prefiksnu sumu Dirichletove konvolucije teorijsko-brojevnih funkcija. Ovaj odjeljak razmatra obratni postupak: neka je $f \ast g = h$ i neka su $f,h$ poznate; izračunati prefiksnu sumu $g$

$$
G(n) = \sum_{x=1}^ng(x).
$$

Drugim riječima, ovaj odjeljak razmatra računanje prefiksne sume kvocijenta dviju teorijsko-brojevnih funkcija u smislu Dirichletove konvolucije. U ovom odjeljku uvijek pretpostavljamo $f(1)\neq 0$, kako bi $f$ bila invertibilna.

U tu svrhu u izrazu Dirichletove metode hiperbole stavimo $x_0 > n$ i dobivamo

$$
H(n) = \sum_{x=1}^{n}f(x)G\left(\left\lfloor\dfrac{n}{x}\right\rfloor\right).
$$

Izravnim rješavanjem po $G(n)$ dobivamo

$$
G(n) = \dfrac{1}{f(1)}\left(H(n)-\sum_{x=2}^nf(x)G\left(\left\lfloor\dfrac{n}{x}\right\rfloor\right)\right).
$$

To je izraz Du sita. Zapravo, za $x_0 \ge 1$ uvijek vrijedi

$$
G(n) = \dfrac{1}{f(1)}\left(H(n)-\sum_{x=2}^{\lfloor x_0\rfloor}f(x)G\left(\left\lfloor\dfrac{n}{x}\right\rfloor\right) - \sum_{y=1}^{\lfloor y_0\rfloor}F\left(\left\lfloor\dfrac{n}{y}\right\rfloor\right)g(y) + F(\lfloor x_0\rfloor)G(\lfloor y_0\rfloor)\right).
$$

U bilo kojem obliku to je rekurzivna relacija za $G(n)$. Da bismo izračunali vrijednost $G(n)$, treba izračunati vrijednosti $G$ na $D(n)\setminus\{n\}$. Budući da $D(n)$ ima [rekurzivnu strukturu](./sqrt-decomposition.md#svojstva), tj. za $m\in D(n)$ uvijek vrijedi $D(m)\subseteq D(n)$, u cijelom rekurzivnom postupku dovoljno je vrijednost $G$ u svakom elementu $D(n)$ izračunati samo jedanput. Drugim riječima, računajući $G(n)$ zapravo dobivamo blokovsko sito $\mathcal S_g(n)$ funkcije $g$.

U konkretnoj implementaciji može se upotrijebiti rekurzija uz memoizaciju radi izbjegavanja ponovljenih računanja. Naravno, može se koristiti i iterativna metoda, računajući vrijednosti $G$ u točkama $D(n)$ redom od najmanje prema najvećoj. Pritom se suma u izrazu može računati i blokovskim dijeljenjem i Dirichletovom metodom hiperbole.

Složenost je tih implementacija jednaka. Budući da Du sito uvijek daje blokovsko sito, složenost Du sita zapravo odgovara složenosti računanja blokovskog sita. Ako su poznata samo blokovska sita $F,H$, složenost Du sita je $O(n^{3/4})$; ako se za neki $z\ge\sqrt{n}$ vrijednosti $g$ u točkama $1\le x \le z$ mogu predračunati u vremenu $T_0(z)$, složenost Du sita je

$$
O\left(T_0(z) + \dfrac{n}{\sqrt{z}}\right).
$$

Kad je $g$ multiplikativna funkcija, može se primijeniti linearno sito, tj. $T_0(z)=\Theta(z)$, pa je optimalno predračunati do $z = n^{2/3}$, a ukupna vremenska složenost iznosi $O(n^{2/3})$; u općenitijem slučaju ukupna je vremenska složenost $O(n^{2/3}(\log n)^{1/3})$. Sve se to u potpunosti slaže s analizom u dijelu o blokovskim sitima.

??? warning "Rekurzivna implementacija bez memoizacije daje pogrešnu složenost"
    U izrazu Du sita računanje vrijednosti $G(n)$ ovisi o vrijednostima $G$ na $D(n)\setminus\{n\}$. Ključ za jamstvo složenosti jest uočiti rekurzivnu strukturu skupa $D(n)$: kad je $m\in D(n)$, vrijedi $D(m)\subseteq D(n)$. Pomoću tog svojstva računanje se može ubrzati memoizacijom. Uz memoizaciju, kao što je prethodno pokazano, složenost je algoritma $O(n^{3/4})$. Ovdje želimo pokazati da je bez memoizacije složenost algoritma pogrešna.
    
    Neka je $T(n)$ složenost rekurzivnog računanja $G(n)$ bez memoizacije. Tada vrijedi
    
    $$
    \begin{aligned}
    T(n) &= \Theta(\sqrt{n}) + \sum_{d\in D(n),~d\neq n}T(d)\\
    &= \Theta(\sqrt{n}) + \sum_{x=1}^{\lfloor n/\lfloor\sqrt{n}\rfloor\rfloor - 1} T(x) + \sum_{x = 2}^{\lfloor\sqrt{n}\rfloor}T\left(\left\lfloor\dfrac{n}{x}\right\rfloor\right).
    \end{aligned}
    $$
    
    Idejom dokaza sličnom onoj za [glavni teorem](../../basic/complexity.md#glavni-teorem) može se pokazati da posljednji član dominira rastom tog izraza i da je $T(n)\in\Theta(n^\alpha)$, gdje je $\alpha\approx 1.73$ korijen jednadžbe $\zeta(\alpha)=2$.

Pri primjeni Du sita za računanje prefiksne sume teorijsko-brojevne funkcije $g$ ključno je pronaći prikladne $f,h$ takve da je $h=f\ast g$ i da se blokovska sita $f,h$ lako računaju. Ponekad su takve $f,h$ očite; drugi ih put treba izvesti pomoću svojstava Dirichletove konvolucije, a odgovarajući se rastav može pronaći i računanjem pripadnih Dirichletovih funkcija izvodnica ili Bellovih redova (kad vrijedi multiplikativnost). Primjeri u nastavku prikazuju te situacije.

## Primjeri zadataka

Ovaj odjeljak predstavlja nekoliko zadataka o računanju prefiksnih suma teorijsko-brojevnih funkcija.

???+ example "[AtCoder Regular Contest 116 C - Multiple Sequences](https://atcoder.jp/contests/arc116/tasks/arc116_c)"
    Zadani su pozitivni cijeli brojevi $N$ i $M$. Treba izračunati koliko nizova $A$ duljine $N$ zadovoljava $1 \le A_i \le M$ i $A_i$ dijeli $A_{i+1}$. Odgovor treba dati modulo $998244353$. Ograničenja: $1 \le N, M \le 2\times 10^5$.

??? note "Rješenje"
    Neka je $f_n(m)$ broj nizova duljine $n$ s $A_n=m$. Tada je konačni odgovor $\sum_{m=1}^M f_N(m)$. Za računanje $f_n(m)$ primijenimo dinamičko programiranje. Jednadžba prijelaza je:
    
    $$
    f_n(m) = \sum_{k\mid m}f_{n-1}(k).
    $$
    
    U zapisu Dirichletove konvolucije to se može pisati kao $f_n = f_{n-1}\ast 1$, gdje je $1$ konstantna teorijsko-brojevna funkcija. Uočimo da je $f_1 = 1$, pa indukcijom slijedi $f_n = 1 ^{\ast n}$. Drugim riječima, $f_n$ je konvolucija $n$ konstantnih funkcija. Konačni je odgovor prefiksna suma $f_N$. Budući da se u postupku pojavljuju samo multiplikativne funkcije, prema prethodno opisanoj metodi računanja prefiksne sume Dirichletove konvolucije jedno računanje prefiksne sume konvolucije traje samo $O(M^{2/3})$ vremena; uz metodu [brzog potenciranja](../binary-exponentiation.md) dovoljno je $O(\log N)$ puta izračunati prefiksnu sumu konvolucije da bismo dobili vrijednost prefiksne sume konvolucije $f_N$. Ukupna vremenska složenost je $O(M^{2/3}\log N)$.

??? note "Referentna implementacija"
    ```cpp
    --8<-- "docs/math/code/hyperbola/hyperbola.cpp"
    ```

???+ example "[P4213【模板】杜教筛（Sum） (Predložak: Du sito (Sum))](https://www.luogu.com.cn/problem/P4213)"
    Neka su $\mu$ i $\varphi$ redom Möbiusova funkcija i Eulerova funkcija. Izračunajte vrijednosti $S_1(n)= \sum_{i=1}^{n} \mu(i)$ i $S_2(n)= \sum_{i=1}^{n} \varphi(i)$. Ograničenja: $1\leq n<2^{31}$.

??? note "Rješenje"
    Uočimo relacije Dirichletove konvolucije:
    
    $$
    \varepsilon = \mu \ast 1,~ \operatorname{id} = \varphi \ast 1.
    $$
    
    Pritom je $\varepsilon(n) = [n=1]$ jedinična funkcija za Dirichletovu konvoluciju, $\operatorname{id}(n) = n$ je funkcija identiteta, a $1(n) = 1$ je konstantna funkcija. Budući da se prefiksne sume svih triju funkcija mogu izračunati u $O(1)$ i da su sve multiplikativne, prethodno opisanom metodom Du sita možemo ih izračunati u vremenu $O(n^{2/3})$.
    
    Za računanje prefiksne sume Eulerove funkcije druga je metoda korištenje [Möbiusove inverzije](./mobius.md). Uočimo
    
    $$
    \begin{aligned}
    S_2(n) &= \sum_{i=1}^n\varphi(i) = \sum_{i=1}^n\sum_{j=1}^i[i\perp j] \\
    &= \sum_{i=1}^n\sum_{j=1}^i\sum_d\mu(d)[d\mid i][d\mid j] \\
    &= \sum_d\mu(d)\dfrac{1}{2}\left\lfloor\dfrac{n}{d}\right\rfloor\left(\left\lfloor\dfrac{n}{d}\right\rfloor+1\right).
    \end{aligned}
    $$
    
    U postupku blokovskog dijeljenja potrebna je prefiksna suma $\mu(d)$, a nju možemo predračunati Du sitom. Vremenska složenost i dalje je $O(n^{2/3})$.

??? note "Referentna implementacija"
    ```cpp
    --8<-- "docs/math/code/du/du_1.cpp"
    ```

???+ example "[„Luogu P3768” 简单的数学题 (Jednostavan matematički zadatak)](https://www.luogu.com.cn/problem/P3768)"
    Zadani su $p,n$; izračunajte
    
    $$
    \sum_{i=1}^n\sum_{j=1}^nij\cdot\gcd(i,j)\pmod p.
    $$
    
    Ograničenja: $n\leq 10^{10}$, $5\times 10^8\leq p\leq 1.1\times 10^9$ i $p$ je prost.

??? note "Rješenje"
    Pomoću svojstava [Eulerove funkcije](./euler-totient.md) provodimo sljedeću inverziju:
    
    $$
    \begin{aligned}
    T(n) &= \sum_{i=1}^n\sum_{j=1}^nij\cdot\gcd(i,j)\\
    &= \sum_{i=1}^n\sum_{j=1}^nij\sum_d\varphi(d)[d\mid i][d\mid j]\\
    &= \sum_d\varphi(d)\left(\sum_{i=1}^{\lfloor n/d\rfloor}id\right)\left(\sum_{j=1}^{\lfloor n/d\rfloor}jd\right)\\
    &= \sum_d d^2\varphi(d) F\left(\left\lfloor\dfrac{n}{d}\right\rfloor\right)^2.
    \end{aligned}
    $$
    
    Pritom je $F(n) = \dfrac{1}{2}n(n+1)$. Taj se izraz može izračunati blokovskim dijeljenjem, ali treba predračunati prefiksnu sumu $d^2\varphi(d)$.
    
    U tu svrhu možemo iskoristiti Du sito. Označimo $f(n)=(\operatorname{id}^2\varphi)(n)$ i $S(n)=\sum_{i=1}^n f(i)$. Ključ primjene Du sita jest konstruirati funkciju $g$ takvu da se i $f\ast g$ i $g$ mogu brzo sumirati. Prethodno smo već raspravili metodu predračuna prefiksne sume $\varphi$ Du sitom, za što je dovoljno iskoristiti relaciju $\operatorname{id} = \varphi\ast 1$. U odnosu na $\varphi$, ovdje $f$ ima dodatni faktor $\operatorname{id}^2$. Budući da je $\operatorname{id}$ potpuno multiplikativna funkcija, prema [svojstvima](./dirichlet.md#svojstva) Dirichletove konvolucije dovoljno je analogno svaki član pomnožiti s $\operatorname{id}^2$ i dobivamo
    
    $$
    \operatorname{id}^3 = f \ast \operatorname{id}^2.
    $$
    
    Budući da se prefiksne sume $\operatorname{id}^2(n)=n^2$ i $\operatorname{id}^3(n)=n^3$ mogu izračunati u $O(1)$, prefiksna suma $f$ može se predračunati u vremenu $O(n^{2/3})$. Zajedno s blokovskim dijeljenjem ukupna vremenska složenost i dalje je $O(n^{2/3})$.
    
    Drugi način da se slična multiplikativna funkcija prikaže kao kvocijent (u smislu Dirichletove konvolucije) dviju funkcija jest pomoću [Dirichletovih funkcija izvodnica](./dirichlet.md#dirichletova-funkcija-izvodnica).

??? note "Referentna implementacija"
    ```cpp
    --8<-- "docs/math/code/du/du_2.cpp"
    ```

## Zadaci za vježbu

-   [AtCoder Xmas Contest 2019 D - Sum of (-1)^f(n)](https://atcoder.jp/contests/xmascon19/tasks/xmascon19_d)

## Literatura i bilješke

-   Ren Zhizhou. 2016. 《积性函数求和的几种方法》 (Nekoliko metoda sumacije multiplikativnih funkcija). Rad kandidata za kinesku nacionalnu reprezentaciju u informatici 2016.
-   Zhou Kangyang. 2024. 《关于积性函数求和问题的一些进展》 (Neki napredci u problemu sumacije multiplikativnih funkcija). Rad kandidata za kinesku nacionalnu reprezentaciju u informatici 2024.
-   [Dirichlet hyperbola method - Wikipedia](https://en.wikipedia.org/wiki/Dirichlet_hyperbola_method)
-   [杜教筛的时空复杂度分析 (Analiza vremenske i prostorne složenosti Du sita) - riteme.site](https://riteme.site/blog/2018-9-11/time-space-complexity-dyh-algo.html)
-   [OI 中常用数论函数求和法的简化陈述 (Pojednostavljeni prikaz uobičajenih metoda sumacije teorijsko-brojevnih funkcija u OI) by negiizhao - UOJ](https://negiizhao.blog.uoj.ac/blog/7165)
-   [Dirichlet 積と、数論関数の累積和 (Dirichletov produkt i prefiksne sume teorijsko-brojevnih funkcija) by maspy](https://maspypy.com/dirichlet-%e7%a9%8d%e3%81%a8%e3%80%81%e6%95%b0%e8%ab%96%e9%96%a2%e6%95%b0%e3%81%ae%e7%b4%af%e7%a9%8d%e5%92%8c)
-   [Dirichlet convolution. Part 1: Fast prefix sum computations by adamant - Codeforces](https://codeforces.com/blog/entry/117635)

[^piltz]: [Piltz divisor problem - Divisor summatory function - Wikipedia](https://en.wikipedia.org/wiki/Divisor_summatory_function#Piltz_divisor_problem)
