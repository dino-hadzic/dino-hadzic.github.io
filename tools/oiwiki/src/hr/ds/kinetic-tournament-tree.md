---
title: Kinetic Tournament Tree
---

Preduvjeti: [segment tree](./seg.md)

## Uvod u problem

Zadan je niz linearnih funkcija jedne varijable $F=\{f_1,\dots,f_n\}$, $f_i: \mathbf{R} \rightarrow \mathbf{R}$, gdje je $f_i(x)=k_ix+b_i$ i $k_i,b_i \in \mathbf{R}$. Treba održavati sljedeće operacije:

-   $\operatorname{QueryMax}(l,r)$: za zadane $l$ i $r$ vrati $\max_{i=l}^r{f_i(0)}$.
-   $\operatorname{TranslateLeft}(l,r,\delta)$: za zadane $l$, $r$ i $\delta$, za sve $i\in[l,r]$ izvedi $f_i(x) \leftarrow f_i(x+\delta)$; ta je operacija ekvivalentna s $b_i\leftarrow b_i+k_i\delta$. Pri tome je $\delta > 0$.

Radi jednostavnosti pretpostavljamo da su sve funkcije međusobno različite.

Pomak linearnih funkcija intervala ulijevo u biti je $b_i \leftarrow k_i\cdot \delta$, tj. slobodnom članu $b_i$ dodaje se nagib $k_i$ pomnožen s pomakom apscise $\delta$; ta je operacija ekvivalentna „intervalnom zbrajanju s težinama ovisnima o položaju”, koje susrećemo u mnogim zadacima o strukturama podataka: svakom indeksu $i$ u intervalu $[l, r]$ vrijednost se uveća za fiksan broj $\delta$ pomnožen koeficijentom $k_i$ svojstvenim tom položaju. Dakle, pomak linearnih funkcija intervala u biti je tzv. intervalno zbrajanje s težinama ovisnima o položaju.

Da bismo pokazali jedinstvenu strukturu binarnog „podijeli pa vladaj” stabla KTT-a, krenut ćemo izravno od pomaka intervala.

## Kinetic Data Structures

Kinetic Data Structures skraćeno se zovu KDS. KDS služe za održavanje svojstava sustava geometrijskih objekata tijekom neprekidnog gibanja.

### Red događaja

Pretpostavljamo da svaka točka ima poznat plan gibanja, koji daje potpunu ili djelomičnu informaciju o njezinu gibanju; primjerice, krivulja ili pravac koji tvori funkcija $f_i(x)$ dobro opisuje putanju gibajuće točke $i$. Plan gibanja može se promijeniti u bilo kojem trenutku, zbog sudara ili interakcije s okolinom; uzrok promjene plana gibanja zovemo događajem. Red događaja daje događaje kronološkim redom.

Ključan je aspekt KDS-a da događaji moraju biti lako održivi, tj. vrste događaja u redu događaja odgovaraju mogućim kombinatornim promjenama koje uključuju konstantan i obično malen broj objekata. Primjerice, u održavanju iz ovog problema jedna je vrsta događaja koju koristimo „odnos veličina funkcija $f_i(0)$ i $f_{j}(0)$ se promijenio”.

Red događaja može se održavati implicitno.

### Certifikati

Ti bi događaji trebali biti ekvivalentni jamstvu danom presjekom niza algebarskih uvjeta niskog stupnja, od kojih svaki uključuje konačan broj objekata. Te uvjete zovemo certifikatima KDS-a. Primjerice $[f_i(0) > f_j(0)]$.

## Kinetic Tournament Tree

### Pregled

Kinetic Tournament Tree (skraćeno KTT) pripada kinetičkim strukturama podataka; prvi se put pojavio 1999. u radu [Data Structures for Mobile Data](https://www.sciencedirect.com/science/article/pii/S0196677498909889) i služi za održavanje neprekidno promjenjivih podataka. Općenitije, svaka struktura koja koristi sljedeću strategiju kinetizacije (kinetization strategy) može se nazvati Kinetic Tournament:

-   Za ključne operacije statičnog algoritma (npr. usporedbe) generiraju se certifikati ispravnosti, svaki se certifikat povezuje s globalnim redom događaja i bilježi se trenutak u kojem bi certifikat mogao prestati vrijediti.
-   Kad neki certifikat prestane vrijediti, možemo učinkovito ažurirati izlaz algoritma i održavati skup certifikata.

U zajednici natjecateljskog programiranja popularnost je stekao radom kineske nacionalne pripremne ekipe iz 2020. „[浅谈函数最值的动态维护](https://github.com/OI-wiki/libs/blob/master/%E9%9B%86%E8%AE%AD%E9%98%9F%E5%8E%86%E5%B9%B4%E8%AE%BA%E6%96%87/IOI2020%E4%B8%AD%E5%9B%BD%E5%9B%BD%E5%AE%B6%E5%80%99%E9%80%89%E9%98%9F%E8%AE%BA%E6%96%87%E9%9B%86%20%E9%9D%9E%E6%AD%A3%E5%BC%8F%E7%89%88.pdf)” (O dinamičkom održavanju ekstrema funkcija). Akademski KTT i KTT iz natjecateljskog programiranja razlikuju se u području primjene i implementaciji, pa ćemo prikazati KTT optimiziran za natjecateljsko programiranje.

### Osnovna struktura

Prvo razmotrimo dizajn strukture slične segment treeu za održavanje statičnog maksimuma. Izgradimo strukturu segment treea; svaki unutarnji čvor ima vrijednost jednaku većoj od vrijednosti svoje dvoje djece. Nakon $O(n)$ usporedbi vrijednost korijena je globalni maksimum. Sada se vrijednosti počinju mijenjati. Ako KTT može detektirati svaku promjenu izvora maksimuma u čvoru stabla, možemo održavati globalni maksimum.

Da bi KTT mogao detektirati svaku promjenu izvora maksimuma u stablu, za čvor stabla $x$ i funkcije $f_L$ i $f_R$ koje daju njegovo lijevo odnosno desno dijete definiramo certifikat „odnos veličina $f_L$ i $f_R$ ostaje nepromijenjen”. Kad certifikat prestane vrijediti, trebamo putem u stablu doći do čvora čiji je certifikat prestao vrijediti i ažurirati njegovu informaciju. Za održavanje trenutka u kojem svaki certifikat prestaje vrijediti uočavamo da je to upravo trenutak u kojem dvije funkcije imaju istu vrijednost; problem se tako svodi na nalaženje apscise sjecišta dviju linearnih funkcija, što se rješava u $O(1)$.

Za svaki čvor stabla održavamo funkciju koja u $0$ postiže maksimum, trenutak kad trenutni certifikat prestaje vrijediti i najraniji trenutak prestanka valjanosti certifikata u cijelom podstablu; tada za svaki čvor u trenutku prestanka valjanosti njegova certifikata možemo taj čvor pronaći i ažurirati mu informaciju. Te informacije bilježe podatke o samim funkcijama. Dalje razmatramo održavanje operacije pomaka intervala: budući da se pomaci jednostavno zbrajaju, možemo ih obraditi lijenim oznakama.

Definiramo lijenu oznaku $\Delta_v$ koja znači da funkcije u svim ostalim čvorovima podstabla čvora $v$ treba pomaknuti ulijevo za $\Delta_v$ jedinica. Sada za čvor stabla $v$ nova operacija treba sve funkcije u njegovu podstablu pomaknuti ulijevo za $\delta$, tj. $f(x)\leftarrow f(x+\delta)$. Trebamo ažurirati lijenu oznaku: $\Delta_v\leftarrow \Delta_v + \delta$, tj. akumulirati pomak za sve ostale čvorove podstabla. Istodobno pomak ulijevo znači i promjenu vrijednosti funkcija u točki $0$. Uočavamo da, ako je apscisa prestanka valjanosti certifikata $t$, nakon pomaka ona postaje $t-\delta$; ako $t-\delta$ prijeđe preko točke $0$, certifikat je prestao vrijediti, pa trebamo rekurzivno prema dolje pronaći čvor u kojem se taj certifikat nalazi, ažurirati ga i novu informaciju ažurirati prema gore do korijena. Taj se postupak može izvoditi zajedno s izmjenom.

Tako dobivamo jednostavnu implementaciju.

???+ example "Referentna implementacija"
    ```cpp
    --8<-- "docs/ds/code/ktt/ktt_1.cpp:core"
    ```

### Analiza složenosti

Dokaz vremenske složenosti KTT-a koristi analizu potencijala.

Neka je $d(x)$ dubina čvora $x$ u segment treeu, pri čemu korijen ima dubinu $1$. Potencijal čvora $x$ u segment treeu definiramo kao:

$$
\alpha(x) = \begin{cases}
d(x) & \text{if the lower slope function has larger value}  \\
0    & \text{otherwise}\\
\end{cases}
$$

Dakle, ako od dviju funkcija koje se uspoređuju u $x$ ona s manjim nagibom ima veću vrijednost u točki $0$, potencijal je trenutnog čvora $d(x)$, inače $0$.

Potencijal cijelog KTT-a definiramo kao zbroj potencijala svih čvorova:

$$
\Phi = \sum_x \alpha(x)
$$

Promotrimo jedno ažuriranje čvora $x$ i njegova roditelja $p$ sa stvarnim troškom $c=1$ te potencijale $\Phi$ i $\Phi'$ prije i poslije ažuriranja. Izračunajmo amortizirani trošak ažuriranja čvora $x$. Budući da se čvor $x$ ažurira, njegov potencijal u tom trenutku sigurno pada s $d(x)$ na $0$. Za $p$ potencijal u najgorem slučaju može porasti s $0$ na $d(p)$:

$$
\begin{aligned}
\hat{c} &= 1 + \Phi' - \Phi\\
    &= 1 + (\alpha'(p) + \alpha'(x)) - (\alpha(p) + \alpha(x))\\
    &= 1 + (\alpha'(p) - \alpha(p)) + (\alpha'(x) - \alpha(x))\\
    &\leq 1 + d(p) - d(x)\\
    &= 0
\end{aligned}
$$

Zbrojimo stvarne troškove, s početnim potencijalom $\Phi_s$ i konačnim potencijalom $\Phi_t$:

$$
\begin{aligned}
\sum c  &= \sum \hat{c} + \Phi_{s} - \Phi_{t}\\
    &\leq \Phi_{s} - \Phi_{t}\\
    &=O(n\log n)
\end{aligned}
$$

To je broj ažuriranja koje KTT izvede dok obradi sve prestanke valjanosti certifikata u slučaju kad postoje samo globalne izmjene.

Dodatno promotrimo utjecaj pomaka intervala na potencijal. Za jedan pomak intervala čvorovi koje treba razmotriti oni su u čijem podstablu postoje čvorovi nad kojima se izvodi pomak, ali ne svi. Takvi su čvorovi upravo oni kroz koje prolazimo u stablu pri izvođenju izmjene; ima ih najviše $O(\log n)$, a u najgorem slučaju potencijal svakog od njih poraste za $d(x)\le \log n$, pa svaka operacija povećava potencijal za $O(\log^2 n)$.

Za održavanje pomaka intervala operacija ažuriranja certifikata izvodi se $O(n\log n + m\log^2 n)$ puta. Pri svakom ažuriranju certifikata trebamo putem u stablu doći do čvora s nevažećim certifikatom, što je $O(\log n)$. Ukupna je vremenska složenost stoga $O(n\log^2 n+ m\log^3 n)$.

Odlika je ove metode da već doseže donju granicu vremenske složenosti problema $O(\lambda_{s}(n)\log^2 n)$. $\lambda_{s}(n)$ označava najveću duljinu (n, s) Davenport–Schinzelova niza; linearnim funkcijama odgovara $s=1$ i $\lambda_1(n)=n$. To pripada računskoj geometriji i ovdje nećemo ulaziti u detalje.

### Slučaj višeg stupnja

Što ako ne održavamo linearne funkcije, nego polinome ili još složenije funkcije? Dvije složene funkcije mogu imati više sjecišta. Zadan je niz neprekidnih, posvuda definiranih funkcija jedne varijable $F=\{f_1,\dots,f_n\}$, $f_i: \mathbf{R} \rightarrow \mathbf{R}$, pri čemu se grafovi svakog para funkcija sijeku u najviše $s$ točaka. Reprezentativan je primjer skup polinoma stupnja $s$.

Za isti problem koristimo analizu potencijala.

$d(x)$ je dubina čvora $x$ u segment treeu, korijen ima dubinu $1$. Definiramo $I(x)$ kao broj sjecišta nakon točke $0$ dviju funkcija koje se uspoređuju u čvoru $x$. Potencijal čvora $x$ u segment treeu definiramo kao:

$$
\alpha(x)=d(x)^{\log_2(s+1)}I(x)
$$

Potencijal cijelog KTT-a definiramo kao zbroj potencijala svih čvorova:

$$
\Phi = \sum_x \alpha(x)
$$

Promotrimo jedno ažuriranje čvora $x$ i njegova roditelja $p$ sa stvarnim troškom $c=1$ te potencijale $\Phi$ i $\Phi'$ prije i poslije ažuriranja. Izračunajmo amortizirani trošak ažuriranja čvora $x$. Budući da se čvor $x$ ažurira, njegov potencijal u tom trenutku sigurno pada s $d(x)^{\log_2(s+1)}I(x)$ na $d(x)^{\log_2(s+1)}(I(x)-1)$. Za $p$ potencijal u najgorem slučaju može porasti s $0$ na $d(p)^{\log_2(s+1)}$:

$$
\begin{aligned}
        \hat{c} &= 1 + \Phi' - \Phi\\
                &= 1 + (\alpha'(x) - \alpha(x)) + (\alpha'(p) - \alpha(p))\\
                &\leq 1 - d(x)^{\log_2{(s+1)}} + s(d(x)-1)^{\log_2{(s+1)}}\\
                &\leq 0
    \end{aligned}
$$

Pri prijelazu iz trećeg u četvrti redak iskoristili smo da je $d(x)$ pozitivan cijeli broj.

Zbrojimo stvarne troškove, s početnim potencijalom $\Phi_s$ i konačnim potencijalom $\Phi_t$:

$$
\begin{aligned}
    \sum c  &= \sum \hat{c} - \Phi_t + \Phi_s\\
            &\leq \Phi_s - \Phi_t\\
            &= O(ns (\log n)^{\log_2{(s+1)}})
\end{aligned}
$$

Dobivamo gornju granicu složenosti $O(ns (\log n)^{1+\log_2{(s+1)}} + ms (\log n)^{2+\log_2{(s+1)}})$.[^ref1]

### Aproksimativni slučaj

Za zadani niz neprekidnih, posvuda definiranih funkcija jedne varijable $F=\{f_1,\dots,f_n\}$ definiramo $\mathfrak U_F(x)$, $\mathfrak L_F(x)$ i $\mathfrak E_F(x)$ kao gornju ovojnicu, donju ovojnicu i raspon:

$$
\begin{aligned}
    \mathfrak U_F(x) & = \max\{f_i(x) \mid f_i \in F\} \\
    \mathfrak L_F(x) & = \min\{f_i(x) \mid f_i \in F\} \\
    \mathfrak E_F(x) & = \mathfrak U_F(x) - \mathfrak L_F(x)
\end{aligned}
$$

Ako od programa tražimo samo da vrati $\tilde{\mathfrak U}_F(x)$ koje zadovoljava

$$
\mathfrak U_F(x) \geq \tilde{\mathfrak U}_F(x) \geq \mathfrak U_F(x) - \epsilon \mathfrak E_F(x)
$$

onda u složenom slučaju možemo postići $O((1/\epsilon^2)n\log^3 n)$, neovisno o stupnju polinoma, a dopušteni su i istodobni pomaci intervala funkcija ulijevo ili udesno.

## Literatura i bilješke

[^ref1]: Treba napomenuti da je ovo samo gornja granica; donja bi granica složenosti trebala biti $O(\lambda_{s}(n)\log n)$. Autor pretpostavlja da bi se konstrukcija analize potencijala ovdje trebala osloniti na opću formulu za $\lambda_{s}(n)$ Davenport–Schinzelovih nizova kako bi se dobila čvršća gornja granica.

-   P. K. Agarwal, S. Har-Peled, and K. R. Varadarajan. Approximating extent measures of points. J. ACM, 51(4):606–635, July 2004.
-   J. Basch, L. J. Guibas, and J. Hershberger. Data structures for mobile data. Journal of Algorithms, 31(1):1–28, 1999.
-   G. Alexandron, H. Kaplan, and M. Sharir. Kinetic and dynamic data structures for convex hulls and upper envelopes. Computational Geometry, 36(2):144–158, 2007.
