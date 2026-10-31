---
title: Eksponencijalna funkcija izvodnica
---

Eksponencijalna funkcija izvodnica (exponential generating function, EGF) niza $a$ definira se kao formalni red potencija:

$$
\hat{F}(x)=\sum_{n}a_n \frac{x^n}{n!}
$$

## Osnovne operacije

Zbrajanje i oduzimanje eksponencijalnih funkcija izvodnica isto je kao kod običnih funkcija izvodnica: zbrajaju se odgovarajući koeficijenti.

Promotrimo množenje eksponencijalnih funkcija izvodnica. Za dva niza $a,b$ neka su njihove eksponencijalne funkcije izvodnice $\hat{F}(x),\hat{G}(x)$; tada je

$$
\begin{aligned}
\hat{F}(x)\hat{G}(x)
&=\sum_{i\ge 0}a_i\frac{x^i}{i!}\sum_{j\ge 0}b_j\frac{x^j}{j!}\\
&=\sum_{n\ge 0}x^{n}\sum_{i=0}^na_ib_{n-i}\frac{1}{i!(n-i)!}\\
&=\sum_{n\ge 0}\frac{x^{n}}{n!}\sum_{i=0}^n\binom{n}{i}a_ib_{n-i}
\end{aligned}
$$

Stoga je za niz

$$
\left\langle \sum_{i=0}^n \binom{n}{i}a_ib_{n-i} \right\rangle
$$

eksponencijalna funkcija izvodnica upravo $\hat{F}(x)\hat{G}(x)$.

## Zatvoreni oblik

I za eksponencijalne funkcije izvodnice promatramo zatvoreni oblik.

Eksponencijalna funkcija izvodnica niza $\langle 1,1,1,\cdots\rangle$ je:

$$
\hat{F}(x) = \sum_{n \ge 0}\frac{x^n}{n!} = \mathrm{e}^x
$$

jer Taylorovim razvojem $\mathrm{e}^x$ oko $x = 0$ dobivamo upravo taj beskonačni red.

Slično, eksponencijalna funkcija izvodnica geometrijskog niza $\langle 1,p,p^2,\cdots\rangle$ je:

$$
\hat{F}(x) = \sum_{n\ge 0}\frac{p^nx^n}{n!}=\mathrm{e}^{px}
$$

## Eksponencijalna i obična funkcija izvodnica

Kako razumjeti eksponencijalnu funkciju izvodnicu? Eksponencijalnu funkciju izvodnicu niza $a$ definirali smo kao:

$$
F(x)=\sum_{n\ge 0}a_n\frac{x^n}{n!}
$$

No $F(x)$ je zapravo i obična funkcija izvodnica niza $\left\langle \dfrac{a_n}{n!} \right\rangle$.

Oba su tumačenja posve ispravna. Drugim riječima, različite funkcije izvodnice samo su različiti načini gledanja na problem.

## Kombinatorno značenje polinomnog exp u EGF-u

Ako još niste učili polinomni exp, preskočite ovaj dio; riječ je o značenju koje proizlazi iz razumijevanja exp-a i koje u nekom smislu produbljuje razumijevanje EGF-a.

U EGF-u je $f$ u $f^n(x)$ po pretpostavci EGF, pa najprije promotrimo umnožak dvaju proizvoljnih EGF-ova

$$
\hat{H}(x) = \hat{F}(x)\hat{G}(x) = \sum_{n\geq 0} \left[ \sum_{i = 0}^n\binom {n}{i}f_ig_{n-i} \right] \frac{x^n}{n!}
$$

Koeficijent $[x^k]\hat{H}(x)$ umnoška dvaju EGF-ova zapravo je konvolucija. Promotrimo li $[x^k]\hat{H}(x)$ umnoška više EGF-ova, to je zapravo zbroj koeficijenata po svim načinima da se iz svakog EGF-a odabere jedan član $x^{a_i}$ tako da je $\sum_ia_i=k$.
Gledano skupovno, to je broj načina da se $n$ označenih elemenata podijeli na $k>0$ označenih skupova.

> Ako je $k=0$, koeficijent je očito umnožak konstantnih članova izvornih EGF-ova, no određeni zahtjevi polinomnog $\exp$-a nalažu da slobodni član od $f(x)$ u $\exp$-u mora biti $0$; konkretni razlozi objašnjeni su u nastavku.

U definiciji multinomnog koeficijenta (vidi kombinatorno značenje multinomnih koeficijenata u odjeljku o permutacijama i kombinacijama) skupovi su po pretpostavci uređeni, ali u $\exp(f(x))$ za $f^k(x)$ svih $k$ faktora $f(x)$ daje isti EGF, a particija skupa očito je neuređena, pa koeficijent treba pomnožiti s $\dfrac{1}{k!}$.

Neka $F_k(n)$ označava broj načina da se $n$ označenih elemenata podijeli na $k$ nepraznih neuređenih skupova (zbog $\exp$-a zahtijeva se nepraznost), a $f_i$ broj određenih kombinatornih struktura na konačnom skupu od $i$ elemenata kad tih $i$ elemenata čini jedan skup (to je izvorni EGF; način brojanja elemenata tog jednog skupa ovisi samo o veličini skupa). Tada je $F_k(n)$

$$
F_k(n)=\frac{n!}{k!}\sum_{\sum_{i}^ka_i=n}\prod_{j=1}^{k}\frac{f_{a_j}}{a_j!}
$$

Neka je EGF niza $f_n$ jednak $\hat{F}(x)$, tj.:

$$
\hat{F}(x) = \sum_{n \geq 0} f_n\frac{x^n}{n!}
$$

Neka je EGF od $F_k(n)$ jednak $G_k(x)$; tada je:

$$
\begin{aligned}
G_k(x)&=\sum_{n \geq 0} F_k(n)\frac{x^n}{n!}\\
&=\sum_{n \geq 0} x^n\frac{1}{k!}\sum_{\sum_i^k a_i=n}\prod_{j=1}^{k}\frac{f_{a_j}}{a_j!}\\
&=\frac{1}{k!}\sum_{n \geq 0}\sum_{\sum_i^k a_i=n}\prod_{j=1}^{k}\frac{f_{a_j}x^{a_j}}{a_j!}\\
&=\frac{1}{k!}\hat{F}^k(x)
\end{aligned}
$$

Za sve $k \geq 0$:

$$
\sum_{k \geq 0}G_k(x) = \sum_{k \geq 0}\frac{\hat{F}^k(x)}{k!} = \exp{\hat{F}(x)}
$$

Gore smo odnos izravno zapisali iz kombinatornog kuta; vezu između $\exp(f(x))$ i $f(x)$ možemo dokazati i preko rekurzije.

Neka ponovno $F_k(n)$ označava broj načina da se $n$ označenih elemenata podijeli na $k$ nepraznih (neoznačenih) skupova, $g_i$ broj unutarnjih rasporeda skupa od $i$ elemenata (isto značenje kao $f_i$ gore), neka je $G(x)$ EGF od $\{g_i\}$, a $H_k(x)$ EGF od $\{F_k(n)\}$.

Od $n$ elemenata izdvojimo $i$ elemenata kao jedan zasebno odvojeni skup: za to postoji $g_i$ načina, a preostalih $n-i$ elemenata čini $k-1$ skupova na $F_{k-1}(n-i)$ načina. No u konačnoj particiji svaki je skup jednom bio izabran kao zasebno odvojeni skup, pa je svaka particija izbrojena $k$ puta i treba još podijeliti s $k$.

$$
\begin{aligned}
H_k(x) &= \sum_{n\ge 0}\cfrac{x^n}{n!}F_k(n)\\
&=\sum_{n\ge 0}\cfrac{x^n}{n!}\sum_{i=1}^{n-k+1}\binom n {i} F_{k-1}(n-i)\times g_i\times \cfrac{1}{k}\\
&=\cfrac{1}{k}\sum_{n\ge 0}\cfrac{x^n}{n!}\sum_{i=0}^{n}\binom n {i}F_{k-1}(n-i)\times g_i\\
&=\cfrac{1}{k}\cdot  H_{k-1}(x)G(x)
\end{aligned}
$$

Gornja granica slijedi iz particije na neprazne skupove: $n-(k-1)\geq i$ (svaki od prvih $k-1$ skupova ima barem jedan element), no ako vrijednosti $F_{k-1}(n-i)$ izvan gornje granice stavimo na $0$, ništa se ne mijenja.

Dobivenu rekurziju možemo rekurzivno razviti; rubni je slučaj $k=1$, kada je $H_1(x)=G(x)$.

$$
\begin{aligned}
H_k(x) &= \cfrac{1}{k}\cdot   H_{k-1}(x)G(x)\\
&= \cfrac{1}{k}\cdot\cfrac{1}{k-1}\cdot   H_{k-2}(x)G^2(x)\\
&=\cdots \\
&= \cfrac{1}{k}\cdot\cfrac{1}{k-1} \cdots\cfrac{1}{2}\cdot H_{1}(x)G^{k-1}(x)\\
&= \cfrac{1}{k!}G^{k}(x)\\
\end{aligned}
$$

Isto tako vrijedi:

$$
\begin{aligned}
\sum_{k\ge 0}H_k(x)=\sum_{k\ge 0}\cfrac{G^k(x)}{k!}=\exp G(x)
\end{aligned}
$$

Očito je **definicija preko particije na neprazne skupove** ($g_0=0$) u skladu sa samim značenjem; ako bismo **dopustili prazan skup** ($g_0=1$), u $[x^n]G^k$ pojavili bi se doprinosi iz $[x^n]G^y,y>k$ (odabir slobodnog člana u barem jednom $G$), došlo bi do višestrukog brojanja i ne bismo dobili traženu veličinu.

Gledano preko rekurzije, umnožak više EGF-ova može se shvatiti i kao kombiniranje nalik naprtnjači (knapsack), tj. kao postupak spajanja dviju skupina brojenih objekata.

Ukratko, značenje polinomnog $\exp$-a jest: **koliko ima familija skupova izvedenih iz skupa označenih elemenata**, odnosno ukupan broj načina da se skup podijeli na proizvoljan broj nepraznih podskupova.

## Permutacije i kružne permutacije

Eksponencijalna funkcija izvodnica broja permutacija duljine $n$ je

$$
\hat{P}(x)=\sum_{n\ge 0}\frac{n!x^n}{n!}=\sum_{n\ge 0}x^n=\frac{1}{1-x}
$$

Kružna permutacija definira se kao raspored brojeva $1,2,\cdots,n$ u krug; rasporedi koji se dobivaju rotacijom smatraju se jednakima (ali zrcaljenje se ne smatra jednakim).

Broj kružnih permutacija $n$ brojeva očito je $(n-1)!$. Stoga je eksponencijalna funkcija izvodnica broja kružnih permutacija $n$ brojeva

$$
\hat{Q}(x)=\sum_{n\ge 1}\frac{(n-1)!x^n}{n!}=\sum_{n\ge 1}\frac{x^n}{n}=-\ln(1-x)=\ln\left( \frac{1}{1-x} \right)
$$

Drugim riječima, $\exp \hat{Q}(x)=\hat{P}(x)$. No to je samo matematički izvod. Kako to intuitivno razumjeti: $\exp$ EGF-a broja kružnih permutacija je EGF broja permutacija?

Permutacija se sastoji od nekoliko ciklusa. Na primjer, $p=[4,3,2,5,1]$ ima dva ciklusa:

![](./images/p1.png)

(dakle, povlačimo usmjereni brid od $p_i$ prema $i$)

Različiti ciklusi daju različite permutacije. Na primjer, promijenimo li drugi ciklus u

![](./images/p2.png)

dobivamo permutaciju $[5,3,2,1,4]$.

Drugim riječima, broj permutacija duljine $n$ jednak je broju načina da se

1.  $1,2,\cdots,n$ podijeli na nekoliko skupova
2.  od svakog skupa napravi jedan ciklus.

A broj načina da brojevi jednog skupa čine ciklus očito je broj kružnih permutacija veličine tog skupa. Stoga je broj permutacija duljine $n$ jednak: podijelimo $1,2,\cdots,n$ na nekoliko skupova i pomnožimo brojeve kružnih permutacija pojedinih skupova.

To je intuitivno značenje polinomnog $\exp$-a.

Poopćenje:

-   Ako je EGF broja **označenih** razapinjućih stabala na $n$ vrhova jednak $\hat{F}(x)$, onda je EGF broja **označenih** razapinjućih šuma na $n$ vrhova jednak $\exp \hat{F}(x)$; intuitivno, podijelimo $n$ vrhova na nekoliko skupova i pomnožimo brojeve načina da svaki skup čini jedno razapinjuće stablo.
-   Ako je EGF broja označenih povezanih neusmjerenih grafova na $n$ vrhova jednak $\hat{F}(x)$, onda je EGF broja označenih neusmjerenih grafova na $n$ vrhova jednak $\exp \hat{F}(x)$, a potonji se lako izračuna:

    $$
    \exp \hat{F}(x)=\sum_{n\ge 0}2^{\binom{n}{2}}\frac{x^n}{n!}
    $$

    Dakle, za izračun prvoga dovoljan je jedan polinomni $\ln$.

Pogledajmo sada neke primjene eksponencijalnih funkcija izvodnica.

## Primjene

### Broj deranžmana

???+ note "Broj deranžmana"
    Deranžman duljine $n$ definira se kao permutacija koja zadovoljava $p_i\ne i$.
    
    Odredite eksponencijalnu funkciju izvodnicu broja deranžmana.

Gledano preko ciklusa, deranžman je permutacija čiji ciklusi ne sadrže petlje, tj. nema ciklusa duljine $1$. Eksponencijalna funkcija izvodnica potonjih je

$$
\sum_{n\ge 2}\frac{x^n}{n}=-\ln\left(1-x\right)-x
$$

pa je eksponencijalna funkcija izvodnica broja deranžmana $\exp(-\ln(1-x)-x)$.

### 不动点 (Fiksna točka)

???+ note "[不动点 (Fiksna točka)](https://www.51nod.com/Html/Challenge/Problem.html#problemId=1728)"
    Zadatak: odredite koliko ima preslikavanja $f:\{1,2,\cdots,n\}\to \{1,2,\cdots,n\}$ takvih da je
    
    $$
    \underbrace{f\circ f\circ\cdots\circ f}_{k}=\underbrace{f\circ f\circ\cdots\circ f}_{k-1}
    $$
    
    $nk\le 2\times 10^6,1\le k\le 3$.

Povucimo brid od $i$ prema $f(i)$. Uvjet znači da iz bilo kojeg $i$ nakon $k$ koraka i nakon $k-1$ koraka stižemo u isti vrh. Drugim riječima, ciklus svakog stabla s jednim ciklusom (pseudostabla) je petlja, a dubina ne prelazi $k$ (korijen ima dubinu $1$). Takvo pseudostablo možemo promatrati kao korijensko stablo. Problem se stoga svodi na: prebrojati šume korijenskih stabala na $n$ označenih vrhova dubine najviše $k$.

Promotrimo korijenska stabla na $n$ označenih vrhova dubine najviše $k$ i pretpostavimo da je njihova funkcija izvodnica:

$$
\hat{F_k}(x)=\sum_{n\ge 0}f_{n,k}\frac{x^n}{n!}
$$

Računajmo $\hat{F_k}(x)$ rekurzivno. Korijensko stablo dubine najviše $k$ zapravo je nekoliko korijenskih stabala dubine najviše $k-1$ čiji su korijeni svi spojeni na jedan vrh. Stoga je

$$
\hat{F_k}(x)=x\exp \hat{F}_{k-1}(x)
$$

Eksponencijalna funkcija izvodnica odgovora je tada $\exp \hat{F}_k(x)$; treba izračunati njezin $n$-ti član.

### Lust

???+ note "[Lust](https://codeforces.com/contest/891/problem/E)"
    Zadan je niz od $n$ brojeva $a_1,a_2,\cdots,a_n$ i varijabla $s$ s početnom vrijednošću $0$. Sljedeći postupak ponavlja se $k$ puta:
    
    -   Iz $1,2,\cdots,n$ jednoliko slučajno odabere se $x$.
    -   Varijabli $s$ doda se $\prod_{i\ne x}a_i$.
    -   $a_x$ se smanji za jedan.
    
    Odredite očekivanu vrijednost $s$ nakon $k$ operacija.
    
    $1\le n\le 5000,1\le k\le 10^9,0\le a_i\le 10^9$.

Pretpostavimo da se nakon $k$ operacija $a_i$ smanjio za $b_i$; tada je zapravo

$$
s=\prod_{i=1}^n a_i-\prod_{i=1}^n(a_i- b_i)
$$

pa se problem zapravo svodi na određivanje očekivane vrijednosti $\prod_{i=1}^n (a_i- b_i)$ nakon $k$ operacija.

Računajmo zbroj vrijednosti $\prod_{i=1}^n (a_i- b_i)$ po svim mogućnostima, a na kraju podijelimo s $n^k$.

Broj nizova od $k$ operacija u kojima se $i$ pojavljuje $b_i$ puta je

$$
\frac{k!}{b_1!b_2!\cdots b_n!}
$$

što nalikuje koeficijentima pri množenju eksponencijalnih funkcija izvodnica.

Neka je eksponencijalna funkcija izvodnica za $a_j$

$$
F_j(x)=\sum_{i\ge 0}(a_j-i)\frac{x^i}{i!}
$$

Tada je odgovor

$$
[x^k]\prod_{j=1}^nF_j(x)
$$

Da bismo odgovor brzo izračunali, $F_j(x)$ pretvaramo u zatvoreni oblik:

$$
\begin{aligned}
F_j(x)&=\sum_{i\ge 0}a_j\frac{x^i}{i!}-\sum_{i\ge 1}\frac{x^i}{(i-1)!}\\
&=a_j\mathrm{e}^x-x\mathrm{e}^x\\
&=(a_j-x)\mathrm{e}^x
\end{aligned}
$$

Dakle,

$$
\prod_{j=1}^nF_j(x)=\mathrm{e}^{nx}\prod_{j=1}^n(a_j-x)
$$

gdje je $\prod_{j=1}^n(a_j-x)$ polinom stupnja $n$ koji se može izračunati grubom silom. Neka je njegov razvoj $\sum_{i=0}^nc_ix^i$; tada je

$$
\begin{aligned}
\prod_{j=1}^nF_j(x)
&=\left(\sum_{i\ge 0} \frac{n^ix^i}{i!}\right)\left(\sum_{i=0}^nc_ix^i\right)\\
&=\sum_{i\ge 0}\sum_{j=0}^i c_jx^j\frac{n^{i-j}x^{i-j}}{(i-j)!}\\
&=\sum_{i\ge 0}\frac{x^{i}}{i!}\sum_{j=0}^i n^{i-j}i^{\underline{j}}c_j
\end{aligned}
$$

Dovoljno je izračunati koeficijent uz $x^k$ u tom polinomu.
