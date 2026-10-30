---
title: Prebrojavanje prostih brojeva
---

Ovaj članak predstavlja sublinearne algoritme za problem prebrojavanja prostih brojeva (prime counting). Problem prebrojavanja prostih brojeva sastoji se u izračunavanju broja prostih brojeva koji ne premašuju $n$, tj. $\pi(n)$. Za $n\sim 10^8$ to se može izračunati [sitom](./sieve.md) u vremenu $\tilde O(n)$. Međutim, kada je $n \sim 10^{10}$ ili čak veći, sito i drugi algoritmi temeljeni na nabrajanju teško su primjenjivi. Za tu situaciju ovaj članak predstavlja niz algoritama koje je razmjerno lako implementirati, a čija je vremenska složenost uglavnom između $\tilde O(n^{2/3})$ i $\tilde O(n^{3/4})$.

Problem prebrojavanja prostih brojeva poseban je slučaj problema prefiksnih suma potencija prostih brojeva. Lucyjev algoritam predstavljen u ovom članku može se izravno poopćiti na prefiksne sume potencija prostih brojeva, a to poopćenje čini dio algoritama za sumiranje multiplikativnih funkcija kao što je [Min\_25 sito](./min-25.md).

???+ tip "Savjet"
    Ovaj članak nudi mnogo algoritama za prebrojavanje prostih brojeva. Radi čitljivosti ni na jednom nije napravljeno mnogo optimizacija konstante. Ti se algoritmi razlikuju po vremenskim i prostornim performansama te težini implementacije, pa čitatelj može odabrati prikladan algoritam prema vlastitim potrebama. Za podatke u rasponu $10^{11}\sim 10^{13}$ algoritam iz odjeljka [Lehmerovo pravilo odsijecanja](#lehmerovo-pravilo-odsijecanja) često je već dovoljno učinkovit, a implementacija mu je razmjerno jednostavna; [optimizirani Lucyjev algoritam](#daljnje-optimizacije) nešto je složeniji za implementaciju, ali ima izvrsne vremenske i prostorne performanse. Za manje raspone podataka [izvorni Lucyjev algoritam](#lucyjev-algoritam) najjednostavniji je za implementaciju i ima širu primjenu u sumiranju multiplikativnih funkcija.

## Osnovni pojmovi i oznake

U ovom članku koristit će se sljedeće oznake:

-   $\mathbf P$ je skup (pozitivnih) prostih brojeva, a $p_a$ je $a$-ti najmanji prosti broj (indeksi počinju od $1$). Radi jednostavnosti izlaganja dodatno stavljamo $p_0=1$. U ovom članku slova $p$ i $q$ uvijek označavaju proste brojeve.
-   $\operatorname{lpf}(n)$ označava najmanji prosti faktor broja $n$. Dodatno stavljamo $\operatorname{lpf}(1)=+\infty$.
-   $D(x) = \{\lfloor x/i\rfloor : i = 1,2,\dots,\lfloor x\rfloor\}$. Njegova su svojstva detaljno opisana u odjeljku [Svojstva blokovskog dijeljenja po cjelobrojnom kvocijentu](./sqrt-decomposition.md#svojstva).
-   $\pi(x)$ je broj prostih brojeva koji ne premašuju $x$.
-   $\varphi(x,a)=\#\{n \in\mathbf N_+ : n \le x,~ (p\mid n \implies p > p_a)\}$ je broj pozitivnih cijelih brojeva koji ne premašuju $x$ i čiji su svi prosti faktori veći od $p_a$.
-   $P_k(x,a)=\#\{n\in\mathbf N_+ : n \le x,~ n = q_1q_2\cdots q_k,~ \forall i(q_i > p_a)\}$ je broj pozitivnih cijelih brojeva koji ne premašuju $x$, imaju točno $k$ prostih faktora (brojeći kratnost) i svi su im prosti faktori veći od $p_a$.
-   $S(x,a)$ je broj cijelih brojeva većih od $1$ i ne većih od $x$ koji u Eratostenovu situ preostaju nakon prosijavanja prvih $a$ prostih brojeva.

Te funkcije imaju sljedeća jednostavna svojstva:

-   $\varphi(x,0) = \lfloor x\rfloor$.
-   $S(x,a) = \varphi(x,a) + \min\{\pi(x),a\} - 1$.
-   $\varphi(x,a) = \sum_{k=0}^{\infty} P_k(x,a)$.
-   $P_0(x,a) = 1$.
-   $P_1(x,a) = \pi(x) - \min\{\pi(x),a\}$.
-   Za $x < p_{a+1}^k$ vrijedi $P_k(x,a) = 0$.

Sva se ta svojstva lako izvode iz definicija.

## Meissel–Lehmerov algoritam

Uvrštavanjem izraza za $P_0$ i $P_1$ u razvoj od $\varphi$ i jednostavnim sređivanjem dobiva se

$$
\pi(x) = \varphi(x,a) + a - 1 - P_2(x,a) - P_3(x,a) - \cdots.
$$

To znači da se $\pi(x)$ može dobiti izračunavanjem vrijednosti $\varphi(x,a)$, pri čemu je pogreška zadana nizom članova $P_k$. Kako vrijednost $a$ raste, broj članova pogreške postupno se smanjuje. Posebno, za $a = \pi(\sqrt{x})$ vrijedi $P_2(x,a)=P_3(x,a)=\cdots=0$, to jest

$$
\pi(x) = \varphi(x,\pi(\sqrt{x})) + \pi(\sqrt{x}) - 1.
$$

Za $\pi(x^{1/3}) \le a < \pi(\sqrt{x})$ član $P_2(x,a)$ nije nula, ali su svi sljedeći članovi i dalje nula, tj.

$$
\pi(x) = \varphi(x,a) + a - 1 - P_2(x,a).
$$

Slično, za $\pi(x^{1/4}) \le a < \pi(x^{1/3})$ oba su člana $P_2(x,a)$ i $P_3(x,a)$ različita od nule, i tako dalje. Ukratko, pomoću tih relacija izračunavanje $\pi(x)$ može se svesti na izračunavanje $\varphi(x,a)$ i članova $P_k(x,a)$. Svi algoritmi koji se oslanjaju na te relacije mogu se nazvati Meissel–Lehmerovim algoritmima.

Za $\varphi(x,a)$ vrijedi sljedeća rekurzivna relacija:

$$
\varphi(x,a) = \varphi(x,a - 1) - \varphi\left(\dfrac{x}{p_a},a-1\right).
$$

Prirodno, rubni je uvjet zadan s $\varphi(x,0) = \lfloor x\rfloor$.

???+ example "Primjer"
    Uzmimo za primjer $x=30,a=2$ ($p_a=3$); jedan korak rekurzije prikazan je na slici:
    
    ![](images/phi-recurrence.svg)
    
    Na slici zelena polja označavaju cijele brojeve čiji su svi prosti faktori veći od $p_a=3$ ($1$ nema prostih faktora, pa se također ubraja), a zelena i narančasta polja zajedno označavaju cijele brojeve čiji su svi prosti faktori veći od $2$. Prvih ima $\varphi(x,a)=\varphi(30,2)=10$, a drugih $\varphi(x,a-1)=\varphi(30,1)=15$.
    
    Razlika između njih upravo je narančasti dio: brojevi djeljivi s $3$ koji nemaju prostog faktora manjeg od $3$. Stoga su svi narančasti brojevi oblika $n=3k$. Budući da je svaki prosti faktor od $k$ ujedno i prosti faktor od $n$, ni $k$ nema prostog faktora manjeg od $3$, tj. i sam $k$ pada u zeleno ili narančasto polje; nadalje, iz $3k\le 30$ slijedi $k\le\lfloor x/p_a\rfloor=10$. Vrijedi i obrnuto: prosti faktori od $n=3k$ nisu ništa drugo nego $3$ i prosti faktori od $k$, pa čim je $k\le 10$ i nema prostog faktora manjeg od $3$, $n$ pada u narančasti dio. Stoga su oni u bijekciji.
    
    Tablica je namjerno složena u $30/3=10$ stupaca, tako da je prvi redak upravo $1,\dots,10$. Takvi $k$ upravo su zelena i narančasta polja unutar isprekidanog okvira, ukupno njih $\varphi(x/p_a,a-1)=\varphi(30/3,1)=5$; oznaka $3\times k$ u gornjem desnom kutu svakog narančastog polja pokazuje pripadni $k$. Stoga je
    
    $$
    \varphi(x,a) = \varphi(x,a-1) - \varphi\left(\left\lfloor\dfrac{x}{p_a}\right\rfloor,a-1\right).
    $$
    
    To jest, $\varphi(30,2)=\varphi(30,1)-\varphi(30/3,1)=15-5=10$.

Stablo rekurzije koje nastaje rekurzivnim računanjem po toj relaciji binarno je stablo. Potpunim razvojem dobiva se

$$
\varphi(x,a) = \sum_{n\mid p_1p_2\cdots p_a} \mu(n)\left\lfloor\dfrac{x}{n}\right\rfloor.
$$

Iz toga slijedi da je broj listova tog binarnog stabla jednak broju svih $p_a$-glatkih brojeva bez kvadratnih faktora (tj. cijelih brojeva koji nemaju prostog faktora većeg od $p_a$) koji ne premašuju $x$, a taj je broj $\Theta(x)$[^smooth]. To znači da je složenost izravnog rekurzivnog računanja i dalje $\Omega(x)$. Za brzo računanje to binarno stablo treba prikladno odsjeći (pruning). Glavna razlika među raznim Meissel–Lehmerovim algoritmima upravo je u načinu odsijecanja. U literaturi se oni nazivaju **pravilima odsijecanja** (truncation rule). U nastavku će ovaj odjeljak predstaviti nekoliko jednostavnih pravila odsijecanja.

Na kraju treba obraditi $P_k(x,a)$. Uzmimo za primjer $P_2(x,a)$:

$$
\begin{aligned}
P_2(x,a) &= \sum_{i,j:~p_a < p_i\le p_j\le x/p_i} 1 = \sum_{i = a+1}^{\pi(\sqrt{x})}\sum_{j=i}^{\pi(x/p_i)} 1 \\
&= \sum_{i = a+1}^{\pi(\sqrt{x})}\left(\pi\left(\dfrac{x}{p_i}\right) - i + 1\right)\\
&= \sum_{i = a+1}^{\pi(\sqrt{x})}\pi\left(\dfrac{x}{p_i}\right)-\dfrac{1}{2}\left(\pi(\sqrt{x})+a-1\right)\left(\pi(\sqrt{x}) - a\right).
\end{aligned}
$$

To znači da se izračunavanje $P_2(x,a)$ može svesti na izračunavanje nekoliko vrijednosti $\pi(x/p)$. Za $k>2$ i dalje postoje slični izrazi sa sumama, ali broj razina sumiranja raste, pa postupno prestaju biti praktični. Uobičajeni algoritmi većinom uzimaju $a\ge\pi(x^{1/3})$ kako bi izbjegli računanje daljnjih članova $P_k$. U praksi se vrijednosti $\pi(x/p)$ za ovaj dio obično predobrađuju sitom.

Matematičari su se vrlo rano bavili problemom izravnog računanja $\pi(x)$ bez nabrajanja. Legendre je dao gornji izraz za $a=\pi(\sqrt{x})$, ali potpuni razvoj od $\varphi(x,a)$ daje previše članova da bi se mogao stvarno upotrijebiti za računanje. Godine 1870. Meissel je predložio računanje pri $a=\pi(x^{1/3})$, čime se smanjuje broj članova u razvoju od $\varphi(x,a)$, a pogreška se i dalje lako računa. Godine 1959. Lehmer je taj postupak dodatno poboljšao i pojednostavnio. Godine 1985. pravilo odsijecanja koje su predložili Lagarias, Miller i Odlyzko prvi je put tu ideju dovelo do sublinearne složenosti, s vremenskom složenošću $\tilde O(x^{2/3})$ i prostornom složenošću $\tilde O(x^{1/3})$. Poslije su Deléglise i Rivat (1996), Gourdon (2001), Staple (2015) i drugi u tom smjeru napravili daljnje optimizacije i dodatno smanjili potenciju od $\log x$ u složenosti. Treba napomenuti da su ti algoritmi, kako bi zadržali dobru prostornu složenost i mogli obrađivati probleme veličine $x\sim 10^{26}$, obično prilično složeni. Ovaj će odjeljak znatno pojednostavniti detalje i predstaviti samo neke jednostavne ideje za optimizaciju. Time se žrtvuje nešto vremenske i prostorne složenosti, ali kôd je lakše implementirati. Čitatelji koje zanima izvorna obrada mogu je samostalno proučiti u literaturi navedenoj na kraju članka.

Osim toga, uz metode nabrajanja i kombinatorne metode predstavljene u ovom članku, $\pi(x)$ se može računati i analitičkim metodama, s vremenskom složenošću $\tilde O(\sqrt{x})$. No one se ne mogu primijeniti na algoritamskim natjecanjima, pa ih ovaj članak ne obrađuje.

### Lehmerovo pravilo odsijecanja

Lehmer (1959) predložio je jedno pravilo odsijecanja. U sljedeća dva slučaja $\varphi(u,b)$ se više ne razvija:

1.  kada je $u < p_b$;
2.  kada je $b = c$, gdje je $c$ unaprijed odabran mali pozitivan cijeli broj.

U prvom slučaju, prema prethodnoj raspravi, nužno je $\varphi(u,b)=1$, pa nema što računati. U drugom slučaju treba dodatno izračunati vrijednost $\varphi(u,c)$. Po definiciji je

$$
\varphi(u,c) = \sum_{n=1}^{u} \prod_{b=1}^{c} [p_b \nmid n].
$$

Budući da je relacija djeljivosti s $p_b$ periodična s periodom $p_b$, član sume $\prod_{b=1}^{c} [p_b \nmid n]$ periodičan je s periodom $p_c\# = \prod_{b=1}^{c}p_b$. Iskorištavanjem periodičnosti dobiva se

$$
\varphi(u,c) = \left\lfloor\dfrac{u}{p_c\#}\right\rfloor \varphi(p_c\#, c) + \varphi(u \bmod p_c\#, c).
$$

Stoga, čim se za $n=0,1,2,\dots,p_c\#$ rekurzivnom relacijom predobrade sve vrijednosti $\varphi(n,c)$, vrijednost $\varphi(u,c)$ u drugom slučaju može se brzo očitati.

Treba napomenuti da, iako ta dva pravila odsijecanja doista povećavaju učinkovitost računanja, asimptotska se složenost algoritma ne poboljšava značajno. Lagarias, Miller i Odlyzko (1985) dokazali su da je u Lehmerovu algoritmu broj listova stabla rekurzije $\Omega\left(\dfrac{x}{\log^4 x}\right)$, pa je vremenska složenost i dalje $\tilde\Theta(x)$.

Naravno, prvo Lehmerovo pravilo odsijecanja može se prikladno poboljšati:

$$
\varphi(u,b) = \begin{cases}
1,  & u \le p_b,\\
\pi(u) - b + 1, & p_b < u \le p_b^2,\\
\pi(u) -\dfrac{1}{2}\left(\pi(\sqrt{u})+b-2\right)\left(\pi(\sqrt{u}) - b+1\right) + \sum\limits_{i = b+1}^{\pi(\sqrt{u})}\pi\left(\dfrac{u}{p_i}\right), & p_b^2 < u \le p_b^3.
\end{cases}
$$

Posljednja dva slučaja koriste relacije izvedene ranije. To poboljšanje dodatno smanjuje veličinu stabla rekurzije, ali uvodi više članova $\pi(u/p)$ koje treba izračunati. Budući da $u/p$ može dosegnuti najviše $x/p_{c+1}$, kako bi se smanjilo neučinkovito odsijecanje, može se postaviti gornja granica $V$ za $u$ pri kojoj se to pravilo smije aktivirati i unaprijed predobraditi vrijednosti $\pi(u)$ za $[1,V]$; kada je $u > V$, i dalje se provodi uobičajena rekurzija.

U nastavku je dana implementacija poboljšanog Lehmerova pravila odsijecanja:

??? example "Referentna implementacija"
    ```cpp
    --8<-- "docs/math/code/prime-counting/lehmer.cpp:core"
    ```

Iako je teorijsku složenost te implementacije teško dokazati[^sgtlaugh], njezina je prednost vrlo mala konstanta i jednostavna implementacija, pa je kôd u praksi vrlo učinkovit. Vrijednosti konstanti $c,V,N$ i drugih u kodu mogu se prilagoditi stvarnim potrebama.

### LMO pravilo odsijecanja

Lagarias, Miller i Odlyzko (1985) predložili su drugo pravilo odsijecanja. Odabere se $y$ takav da je $x^{1/3} \le y \le x^{2/5}$ i uzme $a=\pi(y)$. Tada se u sljedeća dva slučaja $\varphi(x/n,b)$ više ne razvija:

1.  kada je $b=c$ i $n\le y$, gdje je $c$ unaprijed odabran mali prirodan broj;
2.  kada je $n > y$.

LMO prvi slučaj naziva običnim listovima, a drugi posebnim listovima.

Prednost je tog pravila odsijecanja u tome što je lako prebrojiti listove. Primijetimo da različiti listovi nužno imaju različite $n$. Obični listovi uvijek zadovoljavaju $n \le y$, pa ih ima $O(y)$. Posebni listovi uvijek zadovoljavaju $n > y$ i $\dfrac{n}{\operatorname{lpf}(n)} \le y$. Prema tome, posebni se listovi mogu podijeliti u dvije vrste: $\operatorname{lpf}(n) < \sqrt{y}$ i $\operatorname{lpf}(n) \ge \sqrt{y}$. Kod prve vrste nužno je $\operatorname{lpf}(n) < \sqrt{y}$, pa broj mogućih $\operatorname{lpf}(n)$ ne premašuje $\pi(\sqrt{y})$, a za $\dfrac{n}{\operatorname{lpf}(n)} \le y$ postoji najviše $y$ izbora, pa broj mogućih $n$ – tj. ukupan broj listova te vrste – ne premašuje $y\pi(\sqrt{y})$. Kod druge vrste nužno je $n=pq$ i $\sqrt{y} \le p < q \le y$, pa je broj takvih listova najviše $\dfrac{1}{2}\pi(y)^2$. Spajajući oba slučaja, ukupan je broj posebnih listova $O\left(\dfrac{y^2}{\log^2x}\right)$.

Za obične listove može se koristiti ista metoda predobrade kao i prije. Za posebne listove, da bi se izračunala vrijednost $\varphi(x/n,b)$, može se po definiciji shvatiti kao „broj pozitivnih cijelih brojeva ne većih od $x/n$ čiji je najmanji prosti faktor strogo veći od $p_b$”. (Podsjetimo da je ranije postavljeno $\operatorname{lpf}(1) = +\infty$.) Nakon te pretvorbe svi se upiti u posebnim listovima mogu obraditi offline: predobrade se i sortiraju vrijednosti $\operatorname{lpf}$ cijelih brojeva u $[1,x/y]$, a zatim se Fenwickovim stablom ažurira i odgovara na upite. Uzimajući u obzir sortiranje offline upita i operacije na Fenwickovu stablu, vremenska je složenost tog postupka

$$
O\left(\dfrac{y^2}{\log^2x}\log \dfrac{y^2}{\log^2x} + \left(\dfrac{x}{y} + \dfrac{y^2}{\log^2x}\right)\log\pi\left(\dfrac{x}{y}\right)\right) = O\left(\dfrac{x}{y}\log x + \dfrac{y^2}{\log x}\right).
$$

Osim izračunavanja $\varphi(x,a)$, koje je posebno, ostatak je izračuna sličan onome u prethodnom odjeljku. Dovoljno je predobraditi vrijednosti $\pi(u)$ za $[1,x/y]$, a zatim pomoću prethodne relacije izračunati $P_2(x,a)$; za slučaj $c > 0$ treba još predobraditi vrijednosti $\varphi(u,c)$. Napomenimo da, radi potreba offline upita, tijekom rekurzivnog pretraživanja listova treba zabilježiti i predznak ispred svakog lista, tj. vrijednost $\mu(n)$, kako bi se zbrojili doprinosi. Time se dobiva potpun algoritam.

Vremenska i prostorna složenost tog algoritma obje su $\tilde O(x^{2/3})$. Ako se uzme $c = 0$, složenost ostalih dijelova može se zanemariti, pa ukupna složenost algoritma dostiže minimum $O(x^{2/3}\log^{1/3}x)$ pri $y = x^{1/3}\log^{2/3}x$. Tada je prostorna složenost algoritma $O(x^{2/3}\log^{-2/3}x)$. Ako se za $c$ uzme mali pozitivan cijeli broj, treba uravnotežiti vremenske i prostorne troškove predobrade s poboljšanjem konstante kasnijih upita, ali ukupna se složenost ne mijenja.

U nastavku je dana referentna implementacija tog algoritma za $c=0$:

??? example "Referentna implementacija"
    ```cpp
    --8<-- "docs/math/code/prime-counting/lmo-offline.cpp:core"
    ```

Taj offline pristup ima visoku prostornu složenost i teško obrađuje probleme veličine $10^{13}$. Usko je grlo to što pri predobradi treba pohraniti informacije o $\operatorname{lpf}$ za $[1,x/y]$. Zapravo se te informacije koriste samo za kasnije offline upite, i to jednim sekvencijalnim prolazom, pa se sasvim mogu izračunati pri upitu [segmentiranim sitom](./sieve.md#blokovsko-prosijavanje).

Zapravo, izvorni rad nudi način implementacije u potpunosti temeljen na segmentiranom situ. Izračunavanje $P_2(x,a)$ i $\varphi(x,a)$ obavlja se unutar segmentiranog sita, čime se dobiva algoritam vremenske složenosti $\tilde O(x^{2/3})$ i prostorne složenosti $\tilde O(x^{1/3})$. To zahtijeva da se svi listovi na neki način izravno nabroje i da se offline algoritam preradi u online algoritam. U nastavku predstavljamo jedan jednostavan način implementacije.

Srž je implementacije segmentirano sito: nakon predobrade prostih brojeva u $[1,y]$, interval $[1,x/y]$ dijeli se na blokove duljine $y$ i na svaki se blok zasebno primjenjuje sito. Pri obradi svakog bloka treba zabilježiti vrijednosti $\pi(u)$ i $\varphi(u,b)$ u elementima tog bloka. Budući da su sve te vrijednosti brojači, lako ih je održavati tijekom obrade blokova. Zatim treba pronaći koji upiti padaju u raspon obrade tog bloka. U algoritmu opisanom ranije u ovom odjeljku neka je $y=\tilde O(x^{1/3})$ i $c=0$. Tada broj prostih brojeva $\pi(x)$ ima sljedeći izraz:

$$
\begin{aligned}
\pi(x) &= \dfrac{1}{2}\left(\pi(\sqrt{x})+a-2\right)\left(\pi(\sqrt{x}) - a + 1\right) - \sum_{y < p\le\sqrt{x}}\pi\left(\dfrac{x}{p}\right) \\
&\quad +\sum_{n\le y}\mu(n)\varphi\left(\dfrac{x}{n},0\right) + \sum_{n > y,~{n}/{\operatorname{lpf}(n)}\le y,~\operatorname{lpf}(n)\le y}\mu(n)\varphi\left(\dfrac{x}{n},\pi(\operatorname{lpf}(n))-1\right).
\end{aligned}
$$

Prvi član treba samo vrijednost $\pi(\sqrt{x})$, koja se može izračunati kada obrada blokova dođe do tog elementa. Drugi član zahtijeva nabrajanje prostih brojeva $p$ takvih da $x/p$ pada u trenutačno obrađivani blok; nakon što se odredi interval u kojem se nalazi $p$, odgovarajući niz prostih brojeva može se dobiti segmentiranim sitom. Budući da interval u kojem je $p$ ne sadrži elemente veće od $\sqrt{x}$, to unutarnje segmentirano sito treba samo proste brojeve unutar $[1,x^{1/4}]$. Za treći član dovoljno je nabrojiti elemente u $[1,y]$. Četvrti član zahtijeva nabrajanje prostih brojeva u $[1,y]$ kao $\operatorname{lpf}(n)$, zatim određivanje raspona vrijednosti $\dfrac{n}{\operatorname{lpf}(n)}$, pa nabrajanje onih elemenata u tom rasponu čiji prosti faktori nisu manji od $\operatorname{lpf}(n)$[^lmo-segsieve]; time se mogu izračunati vrijednosti tog dijela listova. Pri računanju doprinosa dijela u trenutačnom bloku može se koristiti Fenwickovo stablo. Tako se, uz zajamčenu prostornu složenost $\tilde O(x^{1/3})$, i dalje postiže vremenska složenost $\tilde O(x^{2/3})$. Naravno, implementacija je nešto zamršenija od offline algoritma.

??? example "Referentna implementacija"
    ```cpp
    --8<-- "docs/math/code/prime-counting/lmo-online.cpp:core"
    ```

Izvorni rad i kasniji radovi dodatno su klasificirali i razmatrali posebne listove te dalje optimizirali vremensku i prostornu složenost. Međutim, implementacija dana u ovom odjeljku dovoljna je za potrebe natjecanja, pa složenije ideje optimizacije Meissel–Lehmerova algoritma ovdje više ne razmatramo.

## Lucyjev algoritam

Pri primjeni Meissel–Lehmerova algoritma jedan je od ključnih problema koje treba riješiti prevelika veličina stabla rekurzije za $\varphi(x,a)$. Razlog je to što se uvjet zaustavljanja rekurzivne relacije za $\varphi(x,a)$ pojavljuje samo pri $a=0$. Razmotrimo zamjenu $\varphi(x,a)$ sa $S(x,a)$. Prednost je u tome što, ako je $p_a^2 > x$, prosijavanje prostim brojem $p_a$ u Eratostenovu situ ne izbacuje nijedan složen broj (jer oni nužno imaju manji prosti faktor), tj. $S(x,a)=S(x,a-1)$. To omogućuje rano zaustavljanje stabla rekurzije. Za slučaj $p_a^2\le x$ vrijedi $a\le\pi(x)$, pa je $S(x,a) = \varphi(x,a)+a-1$. Nadalje, iz $a-1\le\pi(x/p_a)$ svi se članovi u rekurzivnoj relaciji za $\varphi(x,a)$ mogu odgovarajuće zamijeniti sa $S(\cdot,\cdot)$, čime se dobiva rekurzivna relacija za $S(x,a)$. Spajajući oba slučaja, rekurzivna relacija za $S(x,a)$ može se zapisati kao

$$
S(x,a) = S(x,a-1) - [p_a^2 \le x]\left(S\left(\dfrac{x}{p_a},a-1\right)-(a-1)\right).
$$

Rubni je uvjet $S(x,0)=\lfloor x\rfloor -1$. Na kraju, iz relacije

$$
\pi(x) = S(x,\pi(\sqrt{x})),
$$

izravno se dobiva vrijednost funkcije prebrojavanja prostih brojeva $\pi(x)$.

???+ example "Primjer"
    Opet za slučaj $x=30,a=2$, rekurzivna relacija za $S(x,a)$ prikazana je na slici:
    
    ![](images/s-recurrence.svg)
    
    Početni je interval Eratostenova sita $[2,x] = [2,30]$, pa je polje $1$ nacrtano bijelo i ne sudjeluje u prebrojavanju. Siva su polja složeni brojevi koji su već ranije prosijani, narančasta su polja složeni brojevi prosijani u ovom krugu prostim brojem $p_a=3$; među preostalim poljima svijetloljubičasta označavaju prethodne proste brojeve, tamnoljubičasto trenutačni prosti broj $3$, a zelena cijele brojeve koji još nisu prosijani (mogu biti prosti, a mogu biti i složeni, npr. $25$). Stoga je $S(x,a-1)=S(30,1)=15$ zbroj narančastih, ljubičastih i zelenih polja, $S(x,a)=S(30,2)=11$ zbroj ljubičastih i zelenih polja, a njihova je razlika upravo ona $4$ narančasta polja.
    
    Slično kao kod $\varphi(x,a)$, ti su brojevi i dalje oblika $3k$, a iz $3k\le 30$ slijedi da $k$ pada u $[2,\lfloor x/p_a\rfloor] = [2,10]$ unutar isprekidanog okvira ($k=1$ nije u njemu, i upravo zato sam $3$ ostaje i ne postaje narančast). Razlika je u tome što $k$ sada prolazi samo kroz $3,5,7,9$ (označeno u gornjem desnom kutu svakog narančastog polja): $k$ mora biti preživjeli iz prethodnog kruga prosijavanja (inače bi $3k$ bio već odavno prosijan zajedno s $k$), tj. $2,3,5,7,9$ unutar okvira, ukupno njih $S(x/p_a,a-1)=S(10,1)=5$; od njih još treba ukloniti proste brojeve manje od $p_a$ – to su upravo prvih $a-1$ prostih brojeva, ovdje samo $k=2$ – jer je $3\times 2=6$ već odavno prosijan s $2$. Stoga je
    
    $$
    S(x,a) = S(x,a-1) - \left(S\left(\left\lfloor\dfrac{x}{p_a}\right\rfloor, a-1\right) - (a-1)\right).
    $$
    
    To jest $S(30,2)=S(30,1)-\bigl(S(10,1)-(2-1)\bigr)=15-(5-1)=11$.

Tu je rekurzivnu relaciju lako izračunati dinamičkim programiranjem. Budući da je $S(x,a)=S(\lfloor x\rfloor,a)$, sva se dijeljenja u rekurzivnoj relaciji mogu shvatiti kao cjelobrojna. Prema [svojstvima blokovskog dijeljenja po cjelobrojnom kvocijentu](./sqrt-decomposition.md#svojstva) vrijednosti prve dimenzije u dinamičkom programiranju nužno su u skupu $D(x)$, kojih ima samo $\Theta(\sqrt{x})$. Štoviše, zbog posebnog oblika rekurzivne relacije vrijednosti $S(\cdot,a)$ mogu se pohraniti u jednom polju duljine $|D(x)|$; za svaki $a$ prolaze se elementi skupa $D(x)$ od većih prema manjima i polje se ažurira prema rekurzivnoj relaciji, sve dok element ne postane strogo manji od $p_a^2$. Dovoljno je $\pi(\sqrt{x})$ ažuriranja da se dobije konačan rezultat.

Prostorna je složenost algoritma očito $O(x^{1/2})$. Što se tiče vremenske složenosti, složenost je predobrade $O(x^{1/2})$, a složenost dijela s dinamičkim programiranjem zadana je s

$$
I = \sum_{a=1}^{\pi(\sqrt{x})}|\{u\in D(x) : u \ge p_a^2\}|
$$

To se može procijeniti u dva dijela. Za $a\in[1,\pi(x^{1/4})]$ član sume ne premašuje $|D(x)|$, pa taj dio sume ne premašuje $\pi(x^{1/4})|D(x)|$, što je $O(x^{3/4}\log^{-1}x)$. Za $a\in(\pi(x^{1/4}),\pi(\sqrt{x})]$ vrijedi $p_a^2 > \sqrt{x}$; iz strukture skupa $D(x)$ vidi se da je tih elemenata točno $\lfloor x/p_a^2\rfloor$. Odatle, u kombinaciji s teoremom o prostim brojevima $p_a\sim a\log a$, dobiva se

$$
\sum_{a=\pi(x^{1/4})+1}^{\pi(\sqrt{x})}\dfrac{x}{p_a^2} \in O\left(\int_{\pi(x^{1/4})}^{+\infty}\dfrac{x}{a^2\log^2a}da\right) = O\left(\dfrac{x^{3/4}}{\log x}\right).
$$

Zbrajanjem obaju dijelova vidi se da je ukupna vremenska složenost algoritma $O(x^{3/4}\log^{-1}x)$.

U konkretnoj implementaciji korak predobrade prostih brojeva ne većih od $\sqrt{x}$ može se spojiti s postupkom dinamičkog programiranja. Dovoljno je od manjih prema većima nabrajati sve cijele brojeve $u$ u intervalu $[2,\sqrt{x}]$ i provjeravati uvjet $S(u,\pi(u-1)) \neq S(u-1,\pi(u-1))$ da bi se pronašli svi prosti brojevi u intervalu; kada je uvjet ispunjen, treba izvesti prijelaz stanja. Razlog je to što je, kada nabrajanje dođe do $u$, već obavljen prijelaz na $S(\cdot,\pi(u-1))$, pa je $\pi(u) = S(u,\pi(u-1))$ i $\pi(u-1) = S(u-1,\pi(u-1))$, a ispunjenost navedenog uvjeta nužno znači da je $u$ prost. Osim toga, vrijednost $a-1$ u jednadžbi prijelaza stanja također je dana sa $S(u-1,\pi(u-1))$, pa je nije potrebno zasebno održavati. Time se dobiva sljedeća implementacija:

??? example "Referentna implementacija"
    ```cpp
    --8<-- "docs/math/code/prime-counting/lucy.cpp:core"
    ```

Taj je algoritam jednostavan za implementaciju; iako mu je vremenska složenost nešto lošija, zbog vrlo male konstante izvrsno se ponaša za manje veličine podataka. Još je važnije da, budući da $\pi(x)=S(x,a)$ vrijedi za sve $a\ge \pi(\sqrt{x})$, algoritam kao nusproizvod zapravo dobiva vrijednosti $\pi(\cdot)$ u svim elementima skupa $D(x)$. To je svojstvo osobito važno u problemima sumiranja multiplikativnih funkcija; njegovo poopćenje i primjene razmatrat ćemo poslije.

### Optimizacija Fenwickovim stablom

Pomoću Fenwickova stabla lako je vremensku složenost Lucyjeva algoritma sniziti s $\tilde O(x^{3/4})$ na $\tilde O(x^{2/3})$.

U tu se svrhu uzme realan broj $y\in (\sqrt{x},x]$. Trenutačno stanje $S(\cdot,a)$ održava se u dva dijela: dio veći od $y$ i dalje se računa rekurzivno prema prethodnoj rekurzivnoj relaciji; dio ne veći od $y$ održava se Eratostenovim sitom, a Fenwickovim se stablom ažuriraju i očitavaju trenutačne vrijednosti $S(\cdot,a)$.

Prostorna je složenost algoritma očito $O(y)$. Za izračun vremenske složenosti treba razmotriti sljedeća tri dijela: u dijelu s Eratostenovim sitom svaki prosijani složen broj zahtijeva jedno ažuriranje Fenwickova stabla, ukupno $O(y)$ složenih brojeva, pa je ukupan vremenski trošak $O(y\log y)$; za $p_a^2 \le y$ prijelaz stanja u odgovarajućem krugu treba izvesti $O(x/y)$ puta, pri čemu je svaki upit pri prijelazu $O(\log y)$, a takvih je krugova ukupno $O(\pi(\sqrt{y}))$, pa je ukupan vremenski trošak

$$
O\left(\pi(\sqrt{y})\dfrac{x}{y}\log y\right) = O\left(\dfrac{x}{\sqrt{y}}\right)
$$

Na kraju, za $p_a^2 > y$ prijelaz stanja u odgovarajućem krugu treba izvesti $O(x/p_a^2)$ puta, pa je metodom iz prethodnog pododjeljka ukupan vremenski trošak

$$
O\left(\sum_{a=\pi(\sqrt{y})+1}^{\pi(\sqrt{x})}\dfrac{x}{p_a^2}\log y\right) = O\left(\dfrac{x}{\sqrt{y}}\right)
$$

Zbrajanjem triju dijelova i stavljanjem $y = x^{2/3}\log^{-2/3}x$ dobiva se ukupna vremenska složenost $O(x^{2/3}\log^{1/3}x)$. Tada je i prostorna složenost $\tilde O(x^{2/3})$.

??? example "Referentna implementacija"
    ```cpp
    --8<-- "docs/math/code/prime-counting/lucy-fenwick.cpp:core"
    ```

Treba napomenuti da, iako se teorijska vremenska složenost doista smanjuje, gubitak na konstanti koji uvodi Fenwickovo stablo čini algoritam pri manjim veličinama podataka zapravo sporijim, a pri većim veličinama podataka znatno pogoršana potrošnja memorije ograničava njegovu upotrebu. Stoga ta optimizacija nije osobito praktična.

### Daljnje optimizacije

Iako Fenwickovo stablo uspješno optimizira Lucyjev algoritam na $\tilde O(x^{2/3})$, stvarna učinkovitost i dalje nije visoka. Da bi se dobio učinkovit algoritam, Lucyjev se algoritam može dodatno optimizirati na sljedeće načine (neka je $z < w < y < x$ i sve su to potencije od $x$):

1.  U Lucyjevu algoritmu optimiziranom Fenwickovim stablom vremenski je trošak dijela s Eratostenovim sitom $O(y\log y)$. Zapravo se u prvih nekoliko krugova prijelaza stanja prosijava golem broj složenih brojeva, pa ih nije potrebno održavati Fenwickovim stablom. Stoga se može odabrati $z < y$. Kada je $p_a \le z$, koristi se samo jednadžba prijelaza stanja; kada je $p_a > z$, uvodi se Fenwickovo stablo za održavanje dijela $S(\cdot,a)$ koji ne premašuje $y$. Budući da su pri uvođenju Fenwickova stabla već prosijani svi cijeli brojevi koji sadrže prosti faktor ne veći od $z$, među preostalim brojevima – obično zvanima $z$-grubi brojevi (rough numbers) – onih koji ne premašuju $y$ ima samo $O\left(\dfrac{y}{\log z}\right)$[^rough]. Time se vremenski trošak dijela sa sitom snižava na $O(y)$. Vremenski trošak koji uvode ti početni krugovi prijelaza stanja iznosi $O(x^{1/2}z/\log x)$.

2.  Ranije opisani Lucyjev algoritam na kraju daje vrijednosti $\pi(\cdot)$ u svim elementima skupa $D(x)$. Ako želimo samo vrijednost $\pi(x)$, mnogi prijelazi stanja nisu potrebni. Na primjer, za izračun vrijednosti $S(x,a)$ dovoljno je znati vrijednosti $S(x,a-1)$ i $S\left(\dfrac{x}{p_a},a-1\right)$; a za izračun tih dviju vrijednosti dovoljno je znati vrijednosti

    $$
    S(x,a-2),~ S\left(\dfrac{x}{p_a},a-2\right),~ S\left(\dfrac{x}{p_{a-1}},a-2\right),~ S\left(\dfrac{x}{p_ap_{a-1}},a-2\right)
    $$

    Odatle se indukcijom vidi da je pri $i$-tom krugu prijelaza stanja $n$ u stanjima $S\left(\dfrac{x}{n},i\right)$ čije vrijednosti treba znati nužno $p_i$-grubi broj. Budući da su $p_i$-grubi brojevi zatvoreni na množenje, dovoljno je da se pri svakom prijelazu stanja obrade svi $p_i$-grubi brojevi (kao čvorovi-djelitelji) kako bi se osiguralo da su po završetku prijelaza stanja vrijednosti u svim čvorovima za $p_i$-grube brojeve ispravne.

    Naravno, skup $p_i$-grubih brojeva može se dinamički održavati tijekom prosijavanja[^lucy-rough]; ili se može ponovno iskoristiti prethodni skup $z$-grubih brojeva i njime zamijeniti sve skupove $p_i$-grubih brojeva. Naizgled drugi pristup obavlja nešto nepotrebnog posla, ali oba smanjuju složenost dijela s prijelazima stanja za jedan faktor $\log x$; razlika je samo u konstanti.

3.  Slično kao kod dijela sa sitom, i dio s prijelazima stanja ima problem dodatnog faktora $\log x$ koji uvodi Fenwickovo stablo. Da bi se smanjio broj upita na Fenwickovu stablu, dio Fenwickova stabla koji se više ne ažurira može se pohraniti u statičko polje. Konkretno, kada prijelazi stanja dođu do $i$-tog kruga, vrijednosti $S(u,i)$ za $u < p_i^2$ više se ne mijenjaju, pa se mogu očitati i pohraniti.

    Izračunajmo poboljšanje složenosti koje to donosi. Da bi se uključio utjecaj ostalih optimizacija, ovdje pretpostavljamo da se prijelazi stanja sa sitom na Fenwickovu stablu koriste samo za dio $z < p_i \le w$ i pretpostavljamo $y \ge w^2$, kako bi donje prebrojavanje bilo tijesno. Budući da $u$ za koje treba izvesti prijelaz stanja nužno imaju oblik $\lfloor x/j\rfloor$, dovoljno je prebrojiti odgovarajuće $j$. Radi jednostavnosti računa zanemarujemo raspravu o rubovima nejednakosti. Budući da je $u > y$, nužno je $j < x / y$. Ako je $jp_i < x / y$, Fenwickovo stablo nije uključeno; ako je $x / y < jp_i < \min\{x/p_i^2,p_ix/y\}$, upit se može izvesti samo na Fenwickovu stablu; ako je $\min\{x/p_i^3,x/y\} < j < x/y$, upit se može izvesti u statičkom polju ili na Fenwickovu stablu. Ukupan broj u prvom dijelu iznosi

    $$
    \sum_{z < p_i < w}\dfrac{x}{yp_i} = \dfrac{x}{y}\log\dfrac{\log w}{\log z} \in O\left(\dfrac{x}{y}\right).
    $$

    Ukupan broj u drugom dijelu iznosi

    $$
    \sum_{z < p_i < y^{1/3}}\dfrac{x}{y}\left(1-\dfrac{1}{p_i}\right) + \sum_{y^{1/3} < p_i < w}\left(\dfrac{x}{p_i^3} - \dfrac{x}{yp_i}\right) \le \dfrac{x}{y}\pi(y^{1/3}) + \dfrac{x}{y^{2/3}\log y} \in O\left(\dfrac{x}{y^{2/3}\log y}\right).
    $$

    Ukupan broj u trećem dijelu iznosi

    $$
    \sum_{y^{1/3} < p_i < w}\left(\dfrac{x}{y}-\dfrac{x}{p_i^3}\right) \le \pi(w)\dfrac{x}{y} \in O\left(\dfrac{xw}{y\log w}\right).
    $$

    Broj u prvom dijelu daleko je manji od ostalih dvaju i može se zanemariti. Kada je $w^2 \le y \ll w^3$, ukupan je broj u trećem dijelu daleko veći od onoga u drugom. Samo tada pohranjivanje tog dijela vrijednosti u statičko polje smanjuje ukupnu vremensku složenost dijela s prijelazima stanja za jedan faktor $\log x$; inače upiti u drugom dijelu postaju usko grlo. Ukratko, nakon uvođenja te optimizacije ukupna vremenska složenost dijela s prijelazima stanja iznosi

    $$
    O\left(\max\left\{\dfrac{x}{y^{2/3}},\dfrac{xw}{y\log x}\right\}\right).
    $$

    Primijetimo da je, budući da je raspodjela grubih brojeva približno jednolika, učinak druge optimizacije (tj. optimizacije grubim brojevima u dijelu s prijelazima stanja) neovisan o ovoj. Ako se istodobno primijeni optimizacija grubim brojevima, ovdje dobivena složenost može se smanjiti za još jedan $\log x$.

4.  Prijelazi stanja mogu se prekinuti ranije, ažurirajući samo do dijela $p_a\le w$, a preostali se dio rješava idejom Meissel–Lehmerova algoritma. Za razliku od Meissel–Lehmerova algoritma, koji se oslanja na $\varphi(x,a)$, $S(x,a)$ čuva vrijednosti $\pi(x)$ potrebne sve do $x \le p_a^2$, pa dodatna predobrada nije potrebna. No pri kombiniranju s prethodnim metodama optimizacije treba paziti na utjecaj optimizacije grubim brojevima u dijelu s dinamičkim programiranjem (tj. optimizacije 2) i ne koristiti vrijednosti koje nisu ispravno ažurirane. To poboljšava i vremensku i prostornu složenost algoritma, ali konkretan opseg poboljšanja uvelike ovisi o implementaciji ostalih dijelova, pa ovdje ne dajemo opću analizu. U nastavku ćemo taj dio referentne implementacije konkretno analizirati.

Spojimo te četiri male optimizacije. Za proizvoljan $w \le x^{1/3}$, za $z < w$ i $w^2 \le y < w^3$, ukupna vremenska složenost dijela sa sitom i dijela s prijelazima stanja iznosi

$$
O\left(y + \dfrac{z\sqrt{x}}{\log x} + \dfrac{xw}{y\log x}\right).
$$

Stoga pri $y=x^{5/8}\log^{-1}x$ i $z=w^{1/2}$ ukupna vremenska složenost dostiže $O\left(\dfrac{\sqrt{xw}}{\log x}\right)$. Pritom se $z$ uzima što veći, a da se ne poveća ukupna složenost, kako bi se smanjila gustoća $z$-grubih brojeva i snizila konstanta algoritma.

Ako se algoritam prekine ranije pri $w=x^{1/3}$, vremenska i prostorna složenost algoritma obje su barem[^complex-third] $O(x^{2/3}\log^{-1}x)$. U nastavku pokazujemo da se, prekine li se algoritam pri $w=x^{1/4}$, dobiva niža vremenska i prostorna složenost.

Neka je $w=x^{1/4}$. Budući da je algoritam prekinut ranije pri $a=\pi(x^{1/4})$, za dobivanje $\pi(x)$ treba iskoristiti relaciju:

$$
\pi(x) = S(x,a) - P_2(x,a) - P_3(x,a).
$$

Iz prethodne analize znamo

$$
P_2(x,a) = \sum_{i=a+1}^{\pi(\sqrt{x})}\pi\left(\dfrac{x}{p_i}\right) - \dfrac{1}{2}(\pi(\sqrt{x})+a-1)(\pi(\sqrt{x})-a).
$$

Budući da je već prosijano do $p_a$, $\pi(\sqrt{x})$ može se dobiti iz $S(\cdot,a)$. Međutim, budući da je $x/p_i\in[\sqrt{x},x^{3/4})$, $\pi(\cdot)$ u sumi i dalje se ne podudara sa $S(\cdot,a)$. Stoga daljnjim razvojem dobivamo

$$
\sum_{i=a+1}^{\pi(\sqrt{x})}\pi\left(\dfrac{x}{p_i}\right) = \sum_{i=a+1}^{\pi(\sqrt{x})}S\left(\dfrac{x}{p_i},a\right) - \sum_{i=a+1}^{\pi(\sqrt{x})}P_2\left(\dfrac{x}{p_i},a\right).
$$

Uvrštavanjem natrag u prethodnu formulu dobiva se

$$
\begin{aligned}
\pi(x) &= S(x,a) + \dfrac{1}{2}(\pi(\sqrt{x})+a-1)(\pi(\sqrt{x})-a) \\
&\quad - \sum_{i=a+1}^{\pi(\sqrt{x})}S\left(\dfrac{x}{p_i},a\right) + \underbrace{ \sum_{i=a+1}^{\pi(\sqrt{x})}P_2\left(\dfrac{x}{p_i},a\right) - P_3(x,a) }_{\Delta(x)}.
\end{aligned}
$$

Za izračun $\Delta(x)$ razmotrimo njegovo kombinatorno značenje. Iz definicija $P_2(x,a)$ i $P_3(x,a)$ slijedi

$$
\begin{aligned}
\sum_{i=a+1}^{\pi(\sqrt{x})}P_2\left(\dfrac{x}{p_i},a\right) &= \#\{p_ip_jp_k \le x : a < i,~ a < j \le k\},\\
P_3(x,a) &= \#\{p_ip_jp_k \le x : a < i \le j \le k\}.
\end{aligned}
$$

Oduzimanjem tih dvaju skupova dobiva se

$$
\Delta(x) = \#\{p_ip_jp_k \le x : a < j,~ j < i,~ j \le k\}.
$$

Za prebrojavanje i dalje razmatramo nabrajanje najmanjeg prostog faktora $p_j$ (jer mu je gornja granica nabrajanja najmanja); za fiksni $j$ ostali indeksi moraju zadovoljavati $i > j$ i $k \ge j$; stoga, izdvoji li se poseban slučaj $k=j$, u preostalim slučajevima vrijedi $i,k > j$, što se pomoću simetrije može dodatno pojednostavniti, pa se dobiva sljedeći izraz:

$$
\Delta(x) = \underbrace{\sum_{j=a+1}^{\pi(x^{1/3})}\left(\pi\left(\dfrac{x}{p_j^2}\right) - j\right)}_{i > j = k} + \underbrace{2\sum_{j=a+1}^{\pi(x^{1/3})}\left(\sum_{i=j+1}^{\pi(\sqrt{x/p_j})}\left(\pi\left(\dfrac{x}{p_ip_j}\right) - i\right) \right)}_{i > k > j \text{ or }k > i > j } + \underbrace{\sum_{j=a+1}^{\pi(x^{1/3})}\left(\pi\left(\sqrt{\dfrac{x}{p_j}}\right) - j\right)}_{i=k > j}.
$$

Sređivanjem suma dobiva se

$$
\Delta(x) = \sum_{j=a+1}^{\pi(x^{1/3})}\left(\pi\left(\dfrac{x}{p_j^2}\right) - j + 2 \sum_{i=j+1}^{\pi(\sqrt{x/p_j})}\pi\left(\dfrac{x}{p_ip_j}\right) - \left( \pi\left(\sqrt{\dfrac{x}{p_j}}\right) ^ 2 - j^2 \right) \right).
$$

Pomoću tog izraza složenost izračuna $\Delta(x)$ iznosi (za način procjene vidi raniji dio o složenosti Lucyjeva algoritma)

$$
O\left(\sum_{x^{1/4} < p \le x^{1/3}}\pi\left(\sqrt{\dfrac{x}{p}}\right)\right) = O\left(\dfrac{x^{2/3}}{\log^2 x}\right).
$$

To je ujedno složenost izračuna posljednjeg dijela. Jednostavnom se provjerom vidi da svi članovi $\pi(x/n)$ koji se pojavljuju pri izračunu $\Delta(x)$ zadovoljavaju $x/n\le\sqrt{x} < y$, pa se svi mogu izravno dobiti iz $S(\cdot,a)$ pohranjenih u Fenwickovu stablu (treba ih unaprijed pohraniti u statičko polje kako se ne bi uveli dodatni upiti složenosti $O(\log x)$).

U kombinaciji s prethodnom analizom, kada je $z=x^{1/8},~w=x^{1/4},~y=x^{5/8}\log^{-1}x$, ukupna vremenska složenost dijela sa sitom i dijela s dinamičkim programiranjem iznosi $O(x^{5/8}\log^{-1}x)$, pa je ukupna vremenska složenost algoritma $O(x^{2/3}\log^{-2}x)$. Prostorna je složenost duljina Fenwickova stabla $O(y)=O(x^{5/8}\log^{-1}x)$.

??? example "Referentna implementacija"
    ```cpp
    --8<-- "docs/math/code/prime-counting/lucy-opt.cpp:core"
    ```

U rasponima podataka uobičajenima na algoritamskim natjecanjima ($10^{10}\sim 10^{14}$) vremenski i prostorni troškovi te implementacije prilično su dobri. Treba napomenuti da, iako je u teorijskoj analizi složenosti posljednji dio usko grlo složenosti, zbog manjeg logaritamskog faktora i bolje konstante u njegovoj složenosti u navedenom su rasponu podataka stvarno usko grlo algoritma i dalje dio sa sitom i dio s dinamičkim programiranjem. Upravo je zato optimizacija njihove složenosti neophodna.

## Poopćenje: prefiksne sume potencija prostih brojeva

Općenitije, razmotrimo sljedeći problem:

$$
F_{\text{prime}}(x) = \sum_{p\in\mathbf P,~p\le x}f(p).
$$

Drugim riječima, treba izračunati zbroj vrijednosti teorijsko-brojevne funkcije $f(\cdot)$ u prostim brojevima koji ne premašuju $x$. Funkcija prebrojavanja prostih brojeva $\pi(x)$ poseban je slučaj za $f\equiv 1$.

Pretpostavimo da teorijsko-brojevna funkcija $f$ zadovoljava sljedeće uvjete:

1.  $f$ je potpuno multiplikativna funkcija, tj. $f(mn)=f(m)f(n)$ vrijedi za sve pozitivne cijele brojeve $m,n$;
2.  prefiksna suma $F(x)=\sum_{n \le x}f(n)$ lako se računa.

Uobičajene teorijsko-brojevne funkcije koje zadovoljavaju te uvjete uključuju potencije i [Dirichletove karaktere](https://en.wikipedia.org/wiki/Dirichlet_character) (npr. [Legendreov simbol](./quad-residue.md#legendreov-simbol)). Naravno, ako se neka funkcija može prikazati kao linearna kombinacija funkcija koje zadovoljavaju te uvjete, i njezina se prefiksna suma po prostim brojevima može izračunati. Stoga metoda iz ovog odjeljka može obraditi slučajeve kada je $f$ polinom ili kada je $f$ periodična funkcija[^periodic]. Drugi, sažetiji način obrade periodičnih funkcija opisan je u primjeru zadatka u nastavku.

Pod tim uvjetima može se poopćiti prethodna rekurzivna relacija. Definirajmo $S(x,a)$ kao zbroj vrijednosti $f(\cdot)$ u cijelim brojevima koji u intervalu $[2,x]$ preostaju nakon prosijavanja prvih $a$ prostih brojeva, tj.

$$
S(x,a) = \sum_{1 < n \le x,~ (n\in\mathbf P) \lor (\operatorname{lpf}(n) > p_a)} f(n).
$$

Tada se prethodna rekurzivna relacija za $S(x,a)$ može prepisati ovako:

$$
S(x,a) = S(x,a-1) - [p_a^2 \le x]f(p_a)\left(S\left(\dfrac{x}{p_a},a-1\right)-S(p_{a}-1,a-1)\right).
$$

Rubni je uvjet $S(x,0) = F(x) - 1$. Sadržaj te formule sličan je prethodnome: u Eratostenovu situ složeni brojevi prosijani s $p_a$ nužno su umnožak $p_a$ i nekog cijelog broja koji još nije prosijan prvih $a-1$ prostih brojeva. Međutim, među svim cijelim brojevima koji još nisu prosijani prvih $a-1$ prostih brojeva nalaze se i sami prvi $a-1$ prosti brojevi, koje treba dodatno izbaciti. Stoga se, da bi se dobio zbroj vrijednosti funkcije u tim složenim brojevima, pomoću **potpune multiplikativnosti** može izlučiti koeficijent $f(p_a)$, a preostali je zbroj $S(x/p_a,a-1)$ umanjen za doprinos prvih $(a-1)$ prostih brojeva $S(p_a-1,a-1)$. Primijetimo da se oduzeti član može zapisati i kao $S(p_{a-1},a-1)$; oni su jednaki.

Pomoću te rekurzivne relacije Lucyjevim se algoritmom vrijednost $F_{\text{prime}}(x)$ može izračunati u vremenu $O(x^{3/4}\log^{-1}x)$, uz prostornu složenost od samo $O(x^{1/2})$. Fenwickovim se stablom vremenska složenost može sniziti na $\tilde O(x^{2/3})$, ali to nije osobito praktično.

??? example "Referentna implementacija za zadatak-predložak [Luogu P5493 质数前缀统计 (prefiksna statistika prostih brojeva)](https://www.luogu.com.cn/problem/P5493)"
    ```cpp
    --8<-- "docs/math/code/prime-counting/prime-power-sum.cpp"
    ```

Načelno se za poopćeni Lucyjev algoritam preporučuje predobrada prostih brojeva umjesto spajanja s dinamičkim programiranjem. Razlog je to što kriterij $S(u,\pi(u-1))\neq S(u-1,\pi(u-1))$ za općenit $f$ ne mora vrijediti. Osim toga, iako je u ovom odjeljku razmotreno samo poopćenje Lucyjeva algoritma, i drugi se algoritmi mogu slično poopćiti; no Lucyjev algoritam može izračunati vrijednosti $F_\text{prime}$ u svim vrijednostima iz $D(x)$, što je korisnije za kasnije sumiranje multiplikativnih funkcija, pa ovaj odjeljak predstavlja samo njegovo poopćenje.

## Primjeri zadataka

???+ example "[Codeforces 665 F. Four Divisors](https://codeforces.com/problemset/problem/665/F)"
    Zadan je $n$; odredite broj cijelih brojeva u $[1,n]$ koji imaju točno $4$ djelitelja. Pritom je $1\le n\le 10^{11}$.

??? note "Rješenje"
    Cijeli broj s točno $4$ djelitelja nužno je oblika $p^3$ ili $pq$, gdje su $p,q$ prosti i $p < q$. U intervalu $[1,n]$ cijelih brojeva oblika $p^3$ ima ukupno $\pi(n^{1/3})$, a cijelih brojeva oblika $pq$ ima ukupno
    
    $$
    \sum_{p < \sqrt{n}}\left(\pi\left(\dfrac{n}{p}\right)-\pi(p)\right)
    $$
    
    Budući da se sve funkcije prebrojavanja prostih brojeva u gornjem izrazu mogu izračunati iz vrijednosti u skupu $D(n)$, dovoljno je jednom izvesti Lucyjev algoritam da bi se zadatak riješio. Vremenska je složenost $O(n^{3/4}\log^{-1}n)$, a prostorna $O(n^{1/2})$.

??? note "Referentna implementacija"
    ```cpp
    --8<-- "docs/math/code/prime-counting/prime-count-1.cpp"
    ```

???+ example "[LOJ 6028. „from CommonAnts” 质数计数 II (prebrojavanje prostih brojeva II)](https://loj.ac/p/6028)"
    Zadani su $n,m$; za svaki od ostataka $0,1,2,\dots,m-1$ odredite koliko prostih brojeva u $[1,n]$ daje taj ostatak pri dijeljenju s $m$. Pritom je $1\le n\le 3\times 10^{10}$, $1 < m\le 12$ i $n > m$.

??? note "Rješenje"
    Za bilo koji ostatak $r=0,1,2,\dots,m-1$ funkcija $[n\bmod m = r]$ očito je periodična. Ranije je rečeno da se takvi problemi mogu obraditi sumiranjem Dirichletovih karaktera, ali to je previše zamršeno i uključuje računanje s kompleksnim brojevima. Stoga ovaj zadatak rješavamo drugom metodom.
    
    Razmotrimo dodavanje jedne dimenzije u jednadžbu prijelaza stanja Lucyjeva algoritma. Neka $S(n,r,a)$ označava broj cijelih brojeva u $[2,n]$ koji nakon prosijavanja prvih $a$ prostih brojeva preostaju i daju ostatak $r$ pri dijeljenju s $m$. Slično kao u glavnom tekstu, dobiva se sljedeća rekurzivna relacija:
    
    $$
    S(n,rp_a\bmod m,a) = S(n,rp_a\bmod m,a-1) - [p_a^2 \le n]\left(S\left(\dfrac{n}{p_a},r,a-1\right)-S(p_{a}-1,r,a-1)\right).
    $$
    
    U rekurzivnoj formuli drugi argument funkcije koristi množenje umjesto dijeljenja, uzimajući u obzir mogućnost $p_a\mid m$. Rubni je uvjet $S(n,r,0) = \left\lfloor\dfrac{n-r}{m}\right\rfloor + [r> 1]$. Na temelju toga zadatak se rješava dinamičkim programiranjem. Vremenska je složenost $O(mn^{3/4}\log^{-1}n)$, a prostorna $O(mn^{1/2})$.

??? note "Referentna implementacija"
    ```cpp
    --8<-- "docs/math/code/prime-counting/prime-count-2.cpp"
    ```

## Zadaci za vježbu

-   [Counting Primes - Library Checker](https://judge.yosupo.jp/problem/counting_primes)
-   [Luogu P7884 【模板】Meissel-Lehmer (predložak)](https://www.luogu.com.cn/problem/P7884)
-   [SPOJ NTHPRIME - Nth Prime](https://www.spoj.com/problems/NTHPRIME/)
-   [SPOJ SUMPRIM1 - Sum of primes](https://www.spoj.com/problems/SUMPRIM1/)
-   [SPOJ BBAD - Breaking Math](https://www.spoj.com/problems/BBAD/)
-   [SPOJ APS2 - Amazing Prime Sequence (hard)](https://www.spoj.com/problems/APS2/)
-   [SPOJ DIVFACT4 - Divisors of factorial (extreme)](https://www.spoj.com/problems/DIVFACT4/)

## Literatura i napomene

-   [Meissel–Lehmer algorithm - Wikipedia](https://en.wikipedia.org/wiki/Meissel%E2%80%93Lehmer_algorithm)
-   [Lucy's Algorithm + Fenwick Trees - griff's math blog!](https://gbroxey.github.io/blog/2023/04/09/lucy-fenwick.html)
-   [Counting primes in $\tilde O(n^{2/3})$ by Maksim1744 - Codeforces](https://codeforces.com/blog/entry/91632)
-   [题解 P7884【模板】Meissel–Lehmer 算法 (rješenje zadatka P7884 „Meissel–Lehmerov algoritam”) by 渐变色 - Luogu](https://www.luogu.com.cn/article/q4d4jl20)
-   Lehmer, Derrick H. "On the exact number of primes less than a given limit." Illinois Journal of Mathematics 3, no. 3 (1959): 381-388.
-   Lagarias, Jeffrey C., Victor S. Miller, and Andrew M. Odlyzko. "Computing $\pi(x)$: the Meissel-Lehmer method." Mathematics of Computation 44.170 (1985): 537-560.
-   [Deléglise, Marc, and Joël Rivat. "Computing 𝜋 (𝑥): the Meissel, Lehmer, Lagarias, Miller, Odlyzko method." Mathematics of Computation 65.213 (1996): 235-245.](https://dl.acm.org/doi/abs/10.1090/s0025-5718-96-00674-6)
-   [Staple, Douglas B. "The combinatorial algorithm for computing $\pi(x)$." arXiv preprint arXiv:1503.01839 (2015).](https://arxiv.org/pdf/1503.01839)

[^lucy-rough]: Za implementaciju s dinamičkim održavanjem vidi [odjeljak o tehnikama optimizacije u griffovu blogu](https://gbroxey.github.io/blog/2023/04/09/lucy-fenwick.html#trick-for-further-optimization).

[^periodic]: Svaka teorijsko-brojevna funkcija s periodom $m$ koja poprima vrijednosti različite od nule samo u cijelim brojevima relativno prostima s $m$ može se prikazati kao linearna kombinacija nekoliko Dirichletovih karaktera modulo $m$. Budući da je pri računanju prefiksne sume po prostim brojevima uključeno samo konačno mnogo cijelih brojeva koji nisu relativno prosti s $m$, izvorna se periodična funkcija uvijek može prikladno prilagoditi tako da u tim cijelim brojevima poprima nulu, čime se može prikazati kao linearna kombinacija Dirichletovih karaktera modulo $m$.

[^rough]: Vidi [Buchstab function - Wikipedia](https://en.wikipedia.org/wiki/Buchstab_function#Applications).

[^complex-third]: Jednostavnom se analizom vidi da je vremenska i prostorna složenost algoritma zapravo točno $O(x^{2/3}\log^{-1}x)$.

[^sgtlaugh]: Iako je izvorni autor u kodu naznačio da je složenost približno $O(x^{2/3})$, stvarna mjerenja pokazuju da je za konstantan $V$ složenost približno $\Theta(x)$. Čak i ako se veličina $V$ prikladno prilagodi veličini problema, složenost je i dalje barem $\Omega(x^{0.8})$.

[^smooth]: Vidi [Smooth number - Wikipedia](https://en.wikipedia.org/wiki/Smooth_number#Distribution).

[^lmo-segsieve]: Ukupan broj $n$ nabrojenih u ovom koraku zapravo je veći od broja posebnih listova, ali to ne utječe na ukupnu složenost. Konkretan dokaz vidi u izvornom radu.
