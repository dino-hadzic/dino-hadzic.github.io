---
title: Osnovni pojmovi
---

## Uvod

Pri proučavanju konkretne slučajne pojave obično se usredotočujemo na sljedeće elemente:

-   prostor elementarnih događaja $\Omega$, koji navodi sve moguće ishode slučajne pojave;
-   σ-algebru događaja $\mathcal{F}$, koja predstavlja sve događaje koji nas zanimaju;
-   vjerojatnost $P$, koja opisuje koliko je vjerojatno da se pojedini događaj dogodi.

## Prostor elementarnih događaja, slučajni događaji

### Definicija

Ishod slučajne pojave koji se više ne može dalje razdijeliti naziva se **elementarnim događajem** (sample point). Skup svih elementarnih događaja naziva se **prostorom elementarnih događaja** (sample space) i obično se označava $\Omega$.

**Slučajni događaj** podskup je prostora elementarnih događaja $\Omega$; sastoji se od nekoliko elementarnih događaja i označava se velikim slovima $A, B, C, \cdots$.

Za ishod $\omega$ slučajne pojave i slučajni događaj $A$ kažemo da se događaj $A$ **dogodio** ako i samo ako je $\omega \in A$.

Primjerice, broj dobiven jednim bacanjem kockice slučajna je pojava, a njezin se prostor elementarnih događaja može zapisati kao $\Omega=\{1,2,3,4,5,6\}$. Neka je slučajni događaj $A$ „dobiveni je broj veći od $4$”; tada je $A = \{ 5, 6 \}$. Ako je u nekom bacanju kockice dobiven broj $\omega = 3$, budući da je $\omega \notin A$, događaj $A$ nije se dogodio.

### Operacije s događajima

Budući da smo slučajne događaje definirali kao podskupove prostora elementarnih događaja $\Omega$, operacije sa skupovima (presjek, unija, komplement itd.) možemo prenijeti na slučajne događaje. Oznake su jednake oznakama skupovnih operacija.

Posebno, unija događaja $A \cup B$ može se zapisati i kao $A + B$, a presjek događaja $A \cap B$ kao $AB$; tada ih redom nazivamo i **zbrojem događaja** i **umnoškom događaja**.

## σ-algebra događaja

Pri proučavanju konkretne slučajne pojave moramo odrediti koji nas događaji zanimaju. Prema definiciji slučajnog događaja očito je $\mathcal{F} \subset 2^{\Omega}$ (oznaka $2^{\Omega}$ označava partitivni skup skupa $\Omega$), ali $\mathcal{F} = 2^{\Omega}$ nije nužno. To može biti pomalo teško razumjeti kad je prostor elementarnih događaja $\Omega$ konačan, jer je $2^{\Omega}$, iako veći, ipak konačan. No kad je $\Omega$ beskonačan skup, kardinalnost skupa $2^{\Omega}$ postaje još veća i u njemu se neizbježno pojavljuju neki događaji „ne baš lijepih svojstava” koji nas ne zanimaju; tada se ne isplati odreći se nekih svojstava samo zato da bismo obuhvatili i te događaje.

Iako $\mathcal{F} = 2^{\Omega}$ nije nužno, to ne znači da bilo koji podskup skupa $2^{\Omega}$ može biti σ-algebra događaja. Obično nas zanimaju vjerojatnosti događaja dobivenih operacijama s nekim događajima, pa želimo da σ-algebra događaja $\mathcal{F}$ zadovoljava sljedeće uvjete:

-   $\varnothing \in \mathcal{F}$;
-   ako je $A \in \mathcal{F}$, onda je i suprotni događaj $\bar{A} \in \mathcal{F}$;
-   ako je zadan niz događaja $A_n \in \mathcal{F}, n = 1, 2, 3\dots$, onda je $\bigcup A_n \in \mathcal{F}$.

Ukratko, σ-algebra događaja $\mathcal{F}$ zatvorena je na komplementiranje i na prebrojive unije te sadrži element $\varnothing$.

Može se dokazati da je σ-algebra događaja $\mathcal{F}$ koja zadovoljava gornja tri uvjeta zatvorena i na prebrojive presjeke.

Na primjeru bacanja kockice, kad prostor elementarnih događaja zapišemo kao $\Omega=\{1,2,3,4,5,6\}$, sljedeća dva skupa mogu biti σ-algebre događaja:

-   $\mathcal{F}_1 = \{ \varnothing, \Omega \}$
-   $\mathcal{F}_2 = \{ \varnothing, \{1, 3, 5\}, \{2, 4, 6\}, \Omega \}$

dok sljedeća dva skupa ne mogu:

-   $\mathcal{F}_3 = \{ \varnothing, \{1\}, \Omega \}$ (nije zatvoren na komplementiranje)
-   $\mathcal{F}_4 = \{ \{1, 3, 5\}, \{2, 4, 6\} \}$ (ne sadrži $\varnothing$ i nije zatvoren na uniju)

## Vjerojatnost

### Definicija

#### Klasična definicija

U ranoj praksi teorije vjerojatnosti slučajne pojave koje su se razmatrale bile su prilično jednostavne: konkretno, prostor elementarnih događaja $\Omega$ bio je konačan skup, a intuitivno su svi elementarni događaji bili jednako mogući. Zato su ljudi došli do sljedeće definicije:

Ako slučajna pojava zadovoljava:

-   ima samo konačno mnogo osnovnih ishoda;
-   svaki osnovni ishod jednako je moguć;

onda za svaki događaj $A$ njegovu vjerojatnost definiramo kao

$$
P(A)=\frac{\#(A)}{\#(\Omega)}
$$

gdje $\#(\cdot)$ označava mjeru veličine slučajnog događaja (skupa).

Kasnije se pokazalo da se ta definicija može izravno poopćiti na dio situacija u kojima je $\Omega$ beskonačan, pa je nastala takozvana [geometrijska vjerojatnost](https://en.wikipedia.org/wiki/Geometric_probability).

#### Aksiomatska definicija

Gornja definicija utemeljena na intuitivnom shvaćanju ima velik logički nedostatak: pri definiranju pojma „vjerojatnost” koristi se izraz „mogućnost”, što dovodi do problema kružne definicije. Osim toga, „jednako moguće” postaje dvosmisleno kad je prostor elementarnih događaja beskonačan, iz čega proizlazi niz problema, uključujući [Bertrandov paradoks](https://en.wikipedia.org/wiki/Bertrand_paradox_(probability)).

Nakon dugotrajnih istraživanja, sovjetski matematičar Kolmogorov 1933. godine u svojoj knjizi „Osnove teorije vjerojatnosti” prvi je put dao aksiomatsku definiciju vjerojatnosti:

Funkcija vjerojatnosti $P$ preslikavanje je sa σ-algebre događaja $\mathcal{F}$ u zatvoreni interval $[0, 1]$ koje zadovoljava:

-   **normiranost**: vjerojatnost događaja $\Omega$ jednaka je $1$, tj. $P(\Omega)=1$;
-   **prebrojivu aditivnost**: ako su događaji u nizu $A_1, A_2, \cdots$ u parovima disjunktni, onda je $P\left( \bigcup_{i \geq 1} A_i \right) = \sum_{i \geq 1} P(A_i)$.

### Svojstva funkcije vjerojatnosti

Za proizvoljne slučajne događaje $A, B \in \mathcal{F}$ vrijedi:

-   **monotonost**: ako je $A \subset B$, onda je $P(A) \leq P(B)$;
-   **formula uključivanja-isključivanja**: $P(A+B) = P(A) + P(B) - P(AB)$;
-   $P(A - B) = P(A) - P(AB)$, gdje $A - B$ označava razliku skupova.

## Vjerojatnosni prostor

Na početku smo spomenuli da se pri proučavanju konkretne slučajne pojave obično usredotočujemo na prostor elementarnih događaja $\Omega$, σ-algebru događaja $\mathcal{F}$ i funkciju vjerojatnosti $P$. Uređenu trojku $(\Omega, \mathcal{F}, P)$ nazivamo vjerojatnosnim prostorom.

O vjerojatnosti ima smisla govoriti samo u okviru određenog vjerojatnosnog prostora. Bertrandov paradoks koji smo prije spomenuli u konačnici nastaje zbog nejasne definicije prostora elementarnih događaja $\Omega$.

## Literatura i napomene

-   [概率论（数学分支）\_百度百科 (Teorija vjerojatnosti (grana matematike) – Baidu Baike)](https://baike.baidu.com/item/概率论/829122)
-   [Probability - Wikipedia](https://en.wikipedia.org/wiki/Probability)
