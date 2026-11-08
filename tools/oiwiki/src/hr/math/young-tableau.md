---
title: Youngov tablo
---

## Uvod

**Youngov tablo** (Young tableau; u kineskoj se literaturi naziva i „Youngova matrica”, 杨氏矩阵), kraće Youngova tablica, kombinatorni je objekt koji se često koristi u teoriji reprezentacija i Schubertovu računu.

Youngov tablo posebna je vrsta matrice. Pogodan je za proučavanje reprezentacija i svojstava simetrične grupe i opće linearne grupe. Youngov tablo prvi je uveo matematičar s Cambridgea Alfred Young 1900. godine, a 1903. ga je njemački matematičar Ferdinand Georg Frobenius primijenio u proučavanju simetričnih grupa.

???+ note "Napomena"
    **Teorija reprezentacija** (representation theory) grana je matematike. Ona proučava apstraktne algebarske strukture tako da njihove elemente prikazuje kao linearne transformacije vektorskih prostora. **Schubertov račun** (Schubert calculus) grana je algebarske geometrije koju je u 19. stoljeću uveo Hermann Schubert radi rješavanja problema prebrojavanja u projektivnoj geometriji.

## Definicije

### Youngov dijagram

**Youngov dijagram** (Young diagram; kad se crta točkama, naziva se i [Ferrersov dijagram](https://en.wikipedia.org/wiki/Partition_%28number_theory%29#Ferrers_diagram), o čemu se govori u odjeljku [Particije broja](./combinatorics/partition.md#ferrersov-dijagram)) konačan je skup kvadratića ili ćelija poravnatih ulijevo, pri čemu su duljine redaka poredane nerastuće. Ispišemo li broj kvadratića u svakom retku Youngova dijagrama, dobivamo **particiju** (integer partition) $\lambda$ nenegativnog cijelog broja $n$ (ukupnog broja kvadratića). Stoga oblik Youngova dijagrama možemo poistovjetiti s $\lambda$, jer nosi istu informaciju kao i ta particija.

Relacija sadržavanja među Youngovim dijagramima definira [parcijalni uređaj](../math/order-theory.md#parcijalno-uređen-skup) na particijama; taj uređaj ima strukturu [rešetke](../math/order-theory.md#usmjereni-skupovi-i-rešetke) i naziva se **Youngova rešetka** (Young's lattice). Ispišemo li broj kvadratića u svakom stupcu Youngova dijagrama, dobivamo „konjugiranu particiju” ili „transponiranu particiju” particije $\lambda$; njoj pripadni Youngov dijagram dobiva se zrcaljenjem izvornog dijagrama s obzirom na glavnu dijagonalu.

Položaj svakog kvadratića Youngova dijagrama određen je dvjema koordinatama koje predstavljaju **redak** i **stupac**. Stupci se broje slijeva nadesno, a retci u smjeru od većeg broja kvadratića prema manjem. Ovdje treba paziti da, ovisno o konvenciji, postoje dva različita načina crtanja Youngova dijagrama: u prvom se retci s manje kvadratića crtaju ispod redaka s više kvadratića, a u drugom se retci slažu od najvećeg prema najmanjem sloj po sloj prema gore. Budući da prvi način uglavnom koriste zemlje engleskog govornog područja, a drugi obično zemlje francuskog govornog područja, uobičajeno ih nazivamo engleskom i francuskom notacijom.

U tablici dolje prikazani su različiti načini crtanja Youngova dijagrama koji odgovara particiji $(5,4,1)$:

-   engleska notacija: ![](./images/young-diagram-1.svg)
-   francuska notacija: ![](./images/young-diagram-2.svg)

### Youngov tablo

#### Definicija

**Youngov tablo** (Young tableau) dobiva se popunjavanjem kvadratića Youngova dijagrama simbolima iz nekog alfabeta, koji obično mora biti totalno uređen skup. Upisane elemente zapisujemo kao $x_{1}$, $x_{2}$, $x_{3}$, $\ldots$. Radi jednostavnosti, međutim, upisujemo izravno pozitivne cijele brojeve.

Kad su Youngovi tabloi prvi put primijenjeni u teoriji reprezentacija simetrične grupe, u $n$ kvadratića Youngova dijagrama smjeli su se proizvoljno upisati međusobno različiti pozitivni cijeli brojevi od $1$ do $n$. Danas se, međutim, u istraživanjima većinom koriste „standardni” Youngovi tabloi, tj. oni u kojima su, uz gornje uvjete, brojevi u svakom retku i u svakom stupcu strogo rastući. Brojevi različitih Youngovih tabloa s $n$ kvadratića čine [brojeve involucija](https://en.wikipedia.org/wiki/Telephone_number_%28mathematics%29):

???+ note "Napomena"
    **Brojevi involucija** (involution number / telephone number) cjelobrojni su niz u matematici koji broji načine na koje se $n$ telefonskih linija može međusobno povezati ako se svaka linija može spojiti s najviše jednom drugom. Oni također opisuju broj sparivanja u potpunom grafu s $n$ vrhova, broj permutacija $n$ elemenata koje su involucije, zbroj apsolutnih vrijednosti koeficijenata Hermiteovih polinoma, broj standardnih Youngovih tabloa s $n$ kvadratića te zbroj stupnjeva ireducibilnih reprezentacija simetrične grupe.

$1, 1, 2, 4, 10, 26, 76, 232, 764, 2620, 9496, \ldots$ (niz [A000085](https://oeis.org/A000085) u [OEIS-u](https://en.wikipedia.org/wiki/On-Line_Encyclopedia_of_Integer_Sequences))

U drugim primjenama u Youngov dijagram mogu se upisivati i jednaki brojevi. Ako su pri popunjavanju brojevi u istom stupcu strogo rastući, a u istom retku monotono rastući (neopadajući), taj se Youngov tablo naziva **polustandardnim** (Semistandard Young Tableaux, ponekad i stupčano strogim). Niz koji dobijemo bilježeći koliko se puta svaki broj pojavljuje u Youngovu tablou naziva se **težinom** Youngova tabloa. Stoga je težina standardnog Youngova tabloa nužno $(1,1,\ldots,1)$, jer se u standardnom Youngovu tablou svaki pozitivan cijeli broj od $1$ do $n$ pojavljuje točno jednom.

#### Algoritam umetanja u standardni Youngov tablo

Svojstva permutacija mogu se zorno prikazati Youngovim tabloima. **RSK algoritam umetanja** daje način da se Youngovi tabloi povežu s permutacijama. Predložili su ga Robinson, Schensted i Knuth.

Neka je $S$ Youngov tablo; definiramo $S \leftarrow x$ kao umetanje elementa $x$ u Youngov tablo počevši od prvog retka, i to ovako:

1.  U trenutnom retku pronađi najmanji broj $y$ koji je veći od $x$.
2.  Ako je pronađen, zamijeni $y$ s $x$, prijeđi u sljedeći redak, stavi $x \leftarrow y$ i ponovi korak 1.
3.  Ako nije pronađen, stavi $x$ na kraj tog retka i završi. Neka je $x$ u $s$-tom retku i $t$-tom stupcu; $(s, t)$ nužno je kutno polje. Polje $(s, t)$ kutno je ako i samo ako ne postoje ni polje $(s + 1, t)$ ni polje $(s, t + 1)$.

Na primjer, koraci umetanja broja $3$ u Youngov tablo $(2, 5, 9)(6, 7)(8)$ jesu:

![](./images/young-tableau-insert.svg)

### Varijante

Postoje mnoge varijante (variations) Youngovih tabloa koji nisu potpuno strogo standardni. Na primjer, retčano strogi Youngov tablo zahtijeva da brojevi u istom retku budu strogo rastući, a u istom stupcu monotono rastući, tj. on je konjugat stupčano strogog Youngova tabloa. Osim toga, u teoriji ravninskih particija (plane partitions) uobičajeno je da se „rastući” u gornjoj definiciji zamijeni s „padajući”. Druge varijante, primjerice vrpčasti Youngovi tabloi, najprije grupiraju neke kvadratiće u skupine, a zatim zahtijevaju da se u kvadratiće iste skupine upiše jednak broj.

### Kosi Youngov tablo

Zadana su dva Youngova dijagrama $\lambda = (\lambda{1}, \lambda{2} \ldots)$ i $\mu = (\mu{1}, \mu{2},\ldots)$ takva da $\lambda$ sadrži $\mu$, tj. $\mu{i} \leq \mu{i}$ za sve $i$. Definiramo „kosi Youngov dijagram” $\lambda/\mu$ kao skup svih kvadratića dijagrama $\lambda$ bez svih kvadratića dijagrama $\mu$, tj. kao razliku skupova $\lambda$ i $\mu$. Upišemo li elemente u kvadratiće kosog Youngova dijagrama, dobivamo **kosi Youngov tablo** (skew tableaux).

Na primjer, slika dolje prikazuje jedan standardni kosi Youngov tablo koji odgovara particiji $(5,4,1)$:

![](./images/skew-tableau.svg)

Analogno, ako su brojevi u istom stupcu strogo rastući, a u istom retku monotono rastući, kosi Youngov tablo naziva se **polustandardnim kosim Youngovim tabloom**; ako su u polustandardnom kosom Youngovu tablou u kvadratiće bez ponavljanja upisani brojevi od $1$ do $n$ (ukupnog broja kvadratića), kosi Youngov tablo naziva se **standardnim kosim Youngovim tabloom**. Uočimo da različiti $\lambda$ i $\mu$ mogu dati isti $\lambda/\mu$. Iako većina svojstava kosih Youngovih tabloa ovisi samo o kvadratićima preostalim nakon oduzimanja, neke operacije ipak ovise o izboru $\lambda$ i $\mu$. Stoga $\lambda/\mu$ treba shvaćati kao da sadrži informaciju o dvama elementima: $\lambda$ i $\mu$. Kad je $\mu$ prazna particija (jedina particija broja $0$), kosi Youngov tablo $\lambda/\mu$ postaje Youngov tablo $\lambda$.

## Primjene

Youngovi tabloi često se koriste u kombinatorici, teoriji reprezentacija i algebarskoj geometriji, gdje se raznim načinima prebrojavanja Youngovih tabloa dobivaju definicija Schurovih funkcija i s njima povezani identiteti. Na informatičkim natjecanjima često se pojavljuju zadaci koji ispituju formulu duljine kuke za Youngove tabloe.

### Duljina kuke

Zadan je Youngov tablo $\pi_{\lambda}$ s ukupno $n$ kvadratića; brojeve od $1$ do $n$, njih $n$, upisujemo u tablo tako da su rastući u svakom retku slijeva nadesno i u svakom stupcu odozdo prema gore. Broj takvih popunjavanja označavamo $dim_{\pi_{\lambda}}$.

Za kvadratić $v$ Youngova tabloa definiramo njegovu **duljinu kuke** $\mathrm{hook}(v)$ kao broj kvadratića desno od njega u istom retku plus broj kvadratića iznad njega u istom stupcu, plus 1 (sam kvadratić).

### Formula duljine kuke

Ako broj takvih popunjavanja označimo $dim_{\lambda}$, **formula duljine kuke** kaže da je broj popunjavanja jednak $n!$ podijeljenom s umnoškom duljina kuka svih kvadratića.

$$
\dim \pi _{\lambda}={\frac {n!}{\prod_{{x\in Y(\lambda)}}{\mathrm {hook}}(x)}}.
$$

![](./images/young-tableau-2.svg)

Stoga za Youngov tablo particije $10 = 5 + 4 + 1$, prikazan na slici gore, imamo

$$
\dim \pi _{\lambda }={\frac  {10!}{7\cdot 5\cdot 4\cdot 3\cdot 1\cdot 5\cdot 3\cdot 2\cdot 1\cdot 1}}=288.
$$

popunjavanja.

## Primjeri zadataka

### Zadaci o podnizovima

Za Youngov tablo $P$ definiran za permutaciju $X = x_{1}, \ldots , x_{n}$ brojeva od $1$ do $n$ vrijedi:

1.  Duljina prvog retka tabloa $P_{X}$ jednaka je duljini **najduljeg rastućeg podniza (LIS)** permutacije $X$. Uočimo da prvi redak tabloa $P$ ne mora biti sam LIS, pa se svojstva Youngova tabloa ne mogu izravno koristiti za rješavanje zadataka poput „podjele na LIS-ove”.

2.  Za permutaciju $X$ i Youngov tablo $P_{X}$ koji ona daje, ako je $X^R$ obrat permutacije $X$, Youngov tablo $P_{X^R}$ koji daje $X^R$ dobiva se iz $P_{X}$ zamjenom redaka i stupaca.

    Na primjer, za permutacije $X = 1, 5, 7, 2, 8, 6, 3, 4$ i $X^R = 4, 3, 6, 8, 2, 7, 5, 1$ dobivamo sljedeći Youngov tablo $P_{X}$:

    ![](./images/young-tableau-LIS.svg)

3.  Duljina prvog stupca Youngova tabloa $P_{X}$ jednaka je duljini **najduljeg padajućeg podniza (LDS)** permutacije $X$.

Definiramo $LIS/LDS$ duljine najviše $k$ kao $k-LIS$ i $k-LDS$; i takve zadatke možemo rješavati Youngovim tabloima. Za $1-LIS$ očito je najdulji $1-LIS$ podniz upravo $LDS$ tog niza, a to je upravo prvi stupac Youngova tabloa; slično dobivamo da je duljina prvih $k$ stupaca Youngova tabloa jednaka duljini najduljeg $k-LIS$ podniza. Dokaz slijedi:

Za permutaciju $X$ i njezin Youngov tablo $P$ s $m$ redaka neka je permutacija $X^∗$ jednaka $(P_{m,1}\ldots,P_{m,λ_{m}},P_{m−1,1}\ldots,P_{1,1}\ldots P_{1,λ_{1}})$ (tj. retke Youngova tabloa odozdo prema gore redom zapišemo jedan za drugim). Tada se $X$ zamjenama sigurno može pretvoriti u $X^*$.

Stoga se duljina najduljeg $k-LIS$ podniza može izraziti kao $F(k)=\sum_{i=1}^{m} \min(k,\lambda_{i})$, tj. kao zbroj duljina prvih $k$ stupaca.

???+ note "[CTSC2017 最长上升子序列 (Najdulji rastući podniz)](https://uoj.ac/problem/301)"
    Zadan je niz $b$ duljine $n$. Za niz $B_{m} = (b_{1}, b_{2},\ldots, b_{m})$ neka je $C$ podniz niza $B_{m}$ takav da duljina najduljeg rastućeg podniza niza $C$ ne prelazi $k$; traži se najveća moguća duljina niza $C$.

??? note "Ideja rješenja"
    Zbog više upita razmotrimo metodu sweep linea. Tada moramo održavati Youngov tablo svakog prefiksa. Uporabom gornjih zaključaka vidimo da se problem svodi na brzo održavanje zbroja duljina prvih $k$ stupaca Youngova tabloa. Održavamo li ga izravno, složenost je $O(n^2 \log n)$, što je neprihvatljivo. Razmotrimo održavanje prvih $\sqrt{n}$ stupaca i prvih $\sqrt{n}$ redaka.
    
    Može se uočiti da Youngov tablo sigurno ne pokriva potpuno taj pravokutnik $W \times H$. Ako je $K \leq W$, odgovor dobivamo izravno; ako je $K > W$, dio veći od $W$ sigurno se nalazi unutar $H$ redaka. Stoga možemo razmotriti kako istodobno održavati prvih $\sqrt{n}$ stupaca i prvih $\sqrt{n}$ redaka. Obratom permutacije dobivamo obrat Youngova tabloa, pa je dovoljno istodobno održavati još i $-A_{i}$; složenost je $O(n \sqrt{n} \log n)$.

???+ note "[BJWC2018 最长上升子序列 (Najdulji rastući podniz)](https://www.luogu.com.cn/problem/P4484)"
    Zadana je slučajna permutacija duljine $n$; odredite očekivanu duljinu njezina najduljeg rastućeg podniza.

???+ note "[CF1268B 杨氏多米诺骨牌 (Domine u Youngovu dijagramu)](https://codeforces.com/problemset/problem/1268/B)"
    Zadan je histogram s $n$ stupaca duljina $a_{1} ,a_{2},\ldots,a_{n}\,(a_{1} \geq a_{2} \geq \ldots \geq a_{n} \geq 1)$, tj. Youngov dijagram za $a=[3,2,2,2,1]$. Odredite najveći broj domina (pravokutnika $1 \times 2$ ili $2 \times 1$) koje se bez preklapanja mogu nacrtati u tom histogramu.

## Literatura i dodatno štivo

1.  [Young Tableau - from Wolfram MathWorld](https://mathworld.wolfram.com/YoungTableau.html)
2.  [Young tableau - Wikipedia](https://en.wikipedia.org/wiki/Young_tableau)
3.  [Hook length formula - Wikipedia](https://en.wikipedia.org/wiki/Hook_length_formula)
4.  Yuan Fangzhou, [《浅谈杨氏矩阵在信息学竞赛中的应用》(O primjeni Youngovih tabloa na informatičkim natjecanjima) IOI2019](https://github.com/OI-wiki/libs/blob/master/%E9%9B%86%E8%AE%AD%E9%98%9F%E5%8E%86%E5%B9%B4%E8%AE%BA%E6%96%87/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2019%E8%AE%BA%E6%96%87%E9%9B%86.pdf), zbornik radova kineske nacionalne kandidatske ekipe, 202–229
