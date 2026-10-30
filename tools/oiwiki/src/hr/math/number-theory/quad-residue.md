---
title: Kvadratni ostatak
---

## Uvod

Kvadratni ostatci mogu se shvatiti kao rasprava o izvedivosti operacije **vađenja kvadratnog korijena** u modularnoj aritmetici. Za korijene višeg reda vidi [k-ti ostatak](./residue.md).

## Definicija

???+ abstract "Kvadratni ostatak"
    Neka su $a$ i $p$ cijeli brojevi takvi da je $(a,p)=1$. Ako postoji cijeli broj $x$ takav da je
    
    $$
    x^2\equiv a\pmod p,
    $$
    
    kažemo da je $a$ kvadratni ostatak modulo $p$; u suprotnom kažemo da je $a$ kvadratni neostatak modulo $p$. U nastavku, kad je modul $p$ očit, možemo kratko pisati kvadratni (ne)ostatak.

## Eulerov kriterij

Kad je modul neparan prost broj, vrijedi sljedeći teorem:

???+ abstract "Eulerov kriterij"
    Za neparan prost broj $p$ i cijeli broj $a$ takav da je $(a,p)=1$ vrijedi
    
    $$
    a^{\frac{p-1}{2}}\equiv\begin{cases}
        1 \pmod p,  & (\exists x\in\mathbf{Z}),~~a\equiv x^2\pmod p,\\
        -1 \pmod p, & \text{otherwise}.\\
    \end{cases}
    $$
    
    Drugim riječima, za gornje $p$ i $a$:
    
    1.  $a$ je kvadratni ostatak modulo $p$ ako i samo ako je $a^{\frac{p-1}{2}}\equiv 1 \pmod p$.
    2.  $a$ je kvadratni neostatak modulo $p$ ako i samo ako je $a^{\frac{p-1}{2}}\equiv -1 \pmod p$.

??? note "Dokaz"
    Prvo, prema [malom Fermatovu teoremu](./fermat.md#mali-fermatov-teorem) vrijedi $a^{p-1}\equiv 1\pmod p$, pa je
    
    $$
    \left(a^{\frac{p-1}{2}}+1\right)\left(a^{\frac{p-1}{2}}-1\right)\equiv 0\pmod p,
    $$
    
    odakle za svaki $a$ s $(a,p)=1$ vrijedi $a^{(p-1)/2}\equiv \pm 1\pmod p.$
    
    Osim toga, budući da je $p$ neparan prost broj, imamo:
    
    $$
    x^{p-1}-a^{\frac{p-1}{2}}={\left(x^2\right)}^{\frac{p-1}{2}}-a^{\frac{p-1}{2}}=(x^2-a)P(x),
    $$
    
    gdje je $P(x)$ neki polinom s cjelobrojnim koeficijentima, pa dalje:
    
    $$
    \begin{aligned}
        x^p-x&=x\left(x^{p-1}-a^{\frac{p-1}{2}}\right)+x\left(a^{\frac{p-1}{2}}-1\right)\\
        &=(x^2-a)xP(x)+\left(a^{\frac{p-1}{2}}-1\right)x.\\
    \end{aligned}
    $$
    
    Prema [teoremu 5 o kongruencijskim jednadžbama](./congruence-equation.md#kongruencije-po-prostom-modulu), $a$ je kvadratni ostatak modulo $p$ ako i samo ako je $a^{(p-1)/2}\equiv 1\pmod p$. Stoga je $a$ kvadratni neostatak modulo $p$ ako i samo ako je $a^{(p-1)/2}\equiv -1\pmod p$.

Na temelju Eulerova kriterija dobivamo sljedeću posljedicu:

???+ note "Broj kvadratnih ostataka"
    Za neparan prost broj $p$ modulo $p$ postoji po $\dfrac{p-1}{2}$ kvadratnih ostataka i kvadratnih neostataka.

??? note "Dokaz"
    Prema Eulerovu kriteriju promatramo $a^{\frac{p-1}{2}}\equiv 1\pmod p.$
    
    Uočimo da $\dfrac{p-1}{2}\mid (p-1)$, pa prema [teoremu 6 o kongruencijskim jednadžbama](./congruence-equation.md#kongruencije-po-prostom-modulu) kongruencija $a^{\frac{p-1}{2}}\equiv 1\pmod p$ ima $\dfrac{p-1}{2}$ rješenja. Dakle, modulo $p$ postoji po $\dfrac{p-1}{2}$ kvadratnih ostataka i kvadratnih neostataka.

## Legendreov simbol

Radi lakše daljnje rasprave uvodimo sljedeću oznaku:

???+ abstract "Legendreov simbol"
    Za **neparan prost broj** $p$ i cijeli broj $a$ Legendreov simbol definira se ovako:
    
    $$
    \left(\frac{a}{p}\right)=\begin{cases}
        0,  & p\mid a,\\
        1,  & (p\nmid a) \land ((\exists x\in\mathbf{Z}),~~a\equiv x^2\pmod p),\\
        -1, & \text{otherwise}.\\
    \end{cases}
    $$

Drugim riječima, za $a$ s $(a,p)=1$:

-   $a$ je kvadratni ostatak modulo $p$ ako i samo ako je $\left(\dfrac{a}{p}\right)=1.$
-   $a$ je kvadratni neostatak modulo $p$ ako i samo ako je $\left(\dfrac{a}{p}\right)=-1.$

Sljedeća tablica prikazuje neke vrijednosti Legendreova simbola (izvor: [Wikipedia](https://en.wikipedia.org/wiki/Legendre_symbol#Table_of_values)).

![](./images/quad_residue.png)

### Svojstva

1.  Za svaki cijeli broj $a$,

    $$
    a^{\frac{p-1}{2}}\equiv \left(\frac{a}{p}\right)\pmod p.
    $$

    Nadalje, imamo posljedice:

    -   $$
        \left(\dfrac{1}{p}\right)=1.
        $$
    -   $$
        \left(\dfrac{-1}{p}\right)=(-1)^{\frac{p-1}{2}}=\begin{cases}
            1,  & p\equiv 1\pmod 4,\\
            -1, & p\equiv 3\pmod 4.
            \end{cases}
        $$

2.  $a_1\equiv a_2\pmod p\implies \left(\dfrac{a_1}{p}\right)=\left(\dfrac{a_2}{p}\right).$

3.  ([Potpuna multiplikativnost](./basic.md#multiplikativne-funkcije)) Za sve cijele brojeve $a_1,a_2$,

    $$
    \left(\frac{a_1a_2}{p}\right)=\left(\frac{a_1}{p}\right)\left(\frac{a_2}{p}\right).
    $$

    Imamo posljedicu: za cijele brojeve $a,b$ takve da $p\nmid b$ vrijedi

    $$
    \left(\frac{ab^2}{p}\right)=\left(\frac{a}{p}\right).
    $$

4.  $$
    \left(\frac{2}{p}\right)=(-1)^{\frac{p^2-1}{8}}=\begin{cases}
            1,  & p\equiv \pm 1\pmod 8, \\
            -1, & p\equiv \pm 3\pmod 8. \\
        \end{cases}
    $$

??? note "Dokaz"
    1.  Slijedi izravno iz [definicije Legendreova simbola](#legendreov-simbol) i [Eulerova kriterija](#eulerov-kriterij).
    2.  Uočimo da
    
        $$
        a_1\equiv a_2\pmod p\implies \left(\frac{a_1}{p}\right)\equiv\left(\frac{a_2}{p}\right)\pmod p,
        $$
    
        a kako je $\left|\left(\dfrac{a_1}{p}\right)-\left(\dfrac{a_2}{p}\right)\right|\leq 2$ i $p>2$, slijedi:
    
        $$
        a_1\equiv a_2\pmod p\implies \left(\frac{a_1}{p}\right)=\left(\frac{a_2}{p}\right).
        $$
    3.  Iz 1 dobivamo
    
        $$
        \left(\frac{a_1a_2}{p}\right)\equiv a_1^{\frac{p-1}{2}}a_2^{\frac{p-1}{2}}\equiv\left(\frac{a_1}{p}\right)\left(\frac{a_2}{p}\right)\pmod p.
        $$
    
        a kako je $\left|\left(\dfrac{a_1a_2}{p}\right)-\left(\dfrac{a_1}{p}\right)\left(\dfrac{a_2}{p}\right)\right|\leq 2$ i $p>2$, slijedi
    
        $$
        \left(\frac{a_1a_2}{p}\right)=\left(\frac{a_1}{p}\right)\left(\frac{a_2}{p}\right).
        $$
    4.  Vidi [kvadratni zakon reciprociteta](#kvadratni-zakon-reciprociteta).

Na temelju gornjih svojstava, ako za bilo koja dva neparna prosta broja $p$ i $q$ možemo izračunati vrijednost $\left(\dfrac{p}{q}\right)$, onda možemo izračunati vrijednost Legendreova simbola u svakom dopuštenom slučaju. Slijedi elegantan teorem koji vješto uspostavlja vezu između $\left(\dfrac{p}{q}\right)$ i $\left(\dfrac{q}{p}\right)$ te nam omogućuje da računanje dovršimo idejom sličnom [Euklidovu algoritmu](./gcd.md#euklidov-algoritam).

### Kvadratni zakon reciprociteta

???+ note "Kvadratni zakon reciprociteta"
    Neka su $p$ i $q$ dva različita neparna prosta broja. Tada je
    
    $$
    \left(\frac{p}{q}\right)\left(\frac{q}{p}\right)=(-1)^{\frac{p-1}{2}\frac{q-1}{2}}.
    $$

Postoji mnogo načina dokazivanja[^ref5]. Jedan se dokaz temelji na sljedećoj lemi[^ref6]:

???+ note "Gaussova lema"
    Neka je $p$ neparan prost broj, $(n,p)=1$, i za cijele brojeve $k~\left(1\leq k\leq (p-1)/2\right)$ neka je $r_k=nk\bmod p$. Neka je $A=\{r_k:r_k < p/2\}$ i $B=\{r_k:r_k > p/2\}$. Tada je
    
    $$
    \left(\frac{n}{p}\right)=(-1)^{|B|}.
    $$

??? note "Dokaz"
    Neka je $\lambda=|A|$ i $\mu=|B|$; očito je $\lambda+\mu=(p-1)/2$. Tada je
    
    $$
    n^{\frac{p-1}{2}}\left(\frac{p-1}{2}\right)!=\prod_{k=1}^{\frac{p-1}{2}} nk\equiv\prod_{a\in A}a\prod_{b\in B}b\pmod{p}.
    $$
    
    Znamo da za svaki element $b$ iz $B$ vrijedi $\dfrac{p}{2} < b < p$, pa je $0 < p-b < \dfrac{p}{2}$. Nadalje, za svaki element $b$ iz $B$ vrijedi $p-b\notin A$; u protivnom, kad bi u $A,B$ redom postojali elementi $a,b$ takvi da je $a=p-b$, postojali bi cijeli brojevi $0 < k_1,k_2 < (p-1)/2$ takvi da je $a=nk_1$, $b=nk_2$ i $p\mid n(k_1+k_2)$; budući da je $(n,p)=1$, slijedi $p\mid (k_1+k_2)$, a kako je $0 < k_1+k_2 < p$, dobivamo kontradikciju. Stoga je
    
    $$
    n^{\frac{p-1}{2}}\left(\frac{p-1}{2}\right)!\equiv(-1)^{\mu}\prod_{a\in A}a\prod_{b\in B}(p-b)=(-1)^{\mu}\left(\frac{p-1}{2}\right)!\pmod{p},
    $$
    
    odnosno
    
    $$
    n^{\frac{p-1}{2}}\equiv(-1)^{\mu}\pmod{p}.
    $$
    
    Tvrdnja sada slijedi iz [svojstva 1](#svojstva) Legendreova simbola.

??? tip "Poopćenje"
    Gaussova lema može se poopćiti na sljedeći način[^ref7]:
    
    Neka je $p$ neparan prost broj i neka $I\subset\mathbf{Z}_p^*$ zadovoljava $I\cup -I=\mathbf{Z}_p^*$ i $I\cap -I=\varnothing$, gdje je $-I:=\{-i:i\in I\}$. Tada za svaki cijeli broj $n$ relativno prost s $p$ vrijedi
    
    $$
    \left(\frac{n}{p}\right)=(-1)^{|J|},
    $$
    
    gdje je $J=\{j\in I:nj\in -I\}$.
    
    Lako se vidi da se izborom $I=\{1,2,\dots,(p-1)/2\}$ dobiva Gaussova lema. Dokaz je u osnovi isti kao dokaz Gaussove leme, pa ga izostavljamo.

Lako se dobiva sljedeća posljedica:

???+ note "Posljedica"
    Za neparan prost broj $p$ vrijedi
    
    $$
    \left(\frac{2}{p}\right)=(-1)^{\frac{p^2-1}{8}}=\begin{cases}
            1,  & p\equiv \pm 1\pmod 8, \\
            -1, & p\equiv \pm 3\pmod 8. \\
        \end{cases}
    $$
    
    Za neparan prost broj $p$ i neparan broj $n$ takav da je $(n,p)=1$ vrijedi
    
    $$
    \left(\frac{n}{p}\right)=(-1)^{\sum_{i=1}^{(p-1)/2}\lfloor ni/p \rfloor}.
    $$

??? note "Dokaz"
    Za $n,k,r_k,A,B,\lambda,\mu$ iz Gaussove leme vrijedi $nk=p\left\lfloor\dfrac{nk}{p}\right\rfloor+r_k$, pa dalje
    
    $$
    \begin{aligned}
        n\cdot\frac{p^2-1}{8}=\sum_{k=1}^{\frac{p-1}{2}}nk&=p\sum_{k=1}^{\frac{p-1}{2}}\left\lfloor\dfrac{nk}{p}\right\rfloor+\sum_{a\in A}a+\sum_{b\in B}b\\
        &=p\sum_{k=1}^{\frac{p-1}{2}}\left\lfloor\dfrac{nk}{p}\right\rfloor+\sum_{a\in A}a+\sum_{b\in B}(p-b)+2\sum_{b\in B}b-p\mu\\
        &=p\sum_{k=1}^{\frac{p-1}{2}}\left\lfloor\dfrac{nk}{p}\right\rfloor+\sum_{k=1}^{\frac{p-1}{2}}k+2\sum_{b\in B}b-p\mu\\
        &=p\sum_{k=1}^{\frac{p-1}{2}}\left\lfloor\dfrac{nk}{p}\right\rfloor+\frac{p^2-1}{8}+2\sum_{b\in B}b-p\mu,
    \end{aligned}
    $$
    
    dakle
    
    $$
    (n-1)\frac{p^2-1}{8}=p\sum_{k=1}^{\frac{p-1}{2}}\left\lfloor\dfrac{nk}{p}\right\rfloor+2\sum_{b\in B}b-p\mu.
    $$
    
    Ako je $n=2$, onda je $0 < \dfrac{nk}{p}\leq\dfrac{p-1}{p} < 1$, odakle slijedi
    
    $$
    \frac{p^2-1}{8}\equiv\mu\pmod{2}.
    $$
    
    Ako $2\nmid n$, onda je
    
    $$
    \sum_{k=1}^{\frac{p-1}{2}}\left\lfloor\dfrac{nk}{p}\right\rfloor\equiv\mu\pmod{2}.
    $$

Prema gornjoj posljedici, za dokaz kvadratnog zakona reciprociteta dovoljno je provjeriti

$$
\frac{p-1}{2}\frac{q-1}{2}=\sum_{k=1}^{\frac{p-1}{2}}\left\lfloor\dfrac{qk}{p}\right\rfloor+\sum_{k=1}^{\frac{q-1}{2}}\left\lfloor\dfrac{pk}{q}\right\rfloor.
$$

Promotrimo skup $S$ koji čine točke $(px,qy)$, $1\leq x\leq \dfrac{q-1}{2},1\leq y\leq \dfrac{p-1}{2}$, i podijelimo ga na dva dijela prema odnosu veličina $px$ i $qy$ (očito je $px\neq qy$); dovoljno je provjeriti veličine tih triju skupova.

Kvadratni zakon reciprociteta ne služi samo za odlučivanje je li broj $n$ kvadratni ostatak modulo $p$, nego i za određivanje strukture modula za koje je broj $n$ kvadratni ostatak.

???+ example "Primjer"
    -   Neparni prosti brojevi $p$ za koje je $5$ kvadratni ostatak zadovoljavaju $p\equiv \pm 1\pmod 5.$
    -   Neparni prosti brojevi $p$ za koje je $-3$ kvadratni ostatak zadovoljavaju $p\equiv 1\pmod 3.$
    -   Neparni prosti brojevi $p$ za koje su $-2$ i $3$ istodobno kvadratni ostatci zadovoljavaju $p\equiv 11\pmod{24}.$

Osim toga, možemo dokazati i tvrdnje poput „postoji beskonačno mnogo prostih brojeva oblika $4k+1$”; takve su tvrdnje zapravo jednostavne posljedice [Dirichletova teorema](https://en.wikipedia.org/wiki/Dirichlet%27s_theorem_on_arithmetic_progressions).

## Jacobijev simbol

Prema kvadratnom zakonu reciprociteta sasvim se prirodno nameće jedan način poopćenja Legendreova simbola:

???+ abstract "Jacobijev simbol"
    Za **pozitivan neparan broj** $m=p_1^{\alpha_1}\dots p_k^{\alpha_k}$ i cijeli broj $a$, gdje su $p_1,\dots,p_k$ prosti brojevi, a $\alpha_1,\dots,\alpha_k$ pozitivni cijeli brojevi, Jacobijev simbol definira se ovako:
    
    $$
    \left(\frac{a}{m}\right):=\prod_{i=1}^k\left(\frac{a}{p_i}\right)^{\alpha_i}.
    $$
    
    Pri tome su $\left(\frac{a}{p_i}\right)$ na desnoj strani jednakosti [Legendreovi simboli](#legendreov-simbol). Osim toga, za cijeli broj $a$ vrijedi $\left(\dfrac{a}{1}\right)=1.$

???+ warning "Upozorenje"
    Obično ne razlikujemo Legendreov i Jacobijev simbol jer iz potpune multiplikativnosti slijedi da Jacobijev simbol ima ista svojstva kao Legendreov, pa se oba simbola računaju na isti način. Ipak, treba paziti na jedno: kad $m$ **nije neparan prost broj**, vrijednost $\left(\dfrac{a}{m}\right)$ **nije povezana** s tim je li $a$ kvadratni ostatak modulo $m$; no ako je $\left(\dfrac{a}{m}\right)=-1$, onda $m$ ima barem jedan (zapravo neparan broj) prosti faktor $p$ za koji je $a$ kvadratni neostatak modulo $p$, pa je tada $a$ kvadratni neostatak modulo $m$.

Modul možemo dalje poopćiti na **cijele brojeve** (treba samo dopuniti definicije $\left(\dfrac{a}{-1}\right)$, $\left(\dfrac{a}{0}\right)$ i $\left(\dfrac{a}{2}\right)$); tako dobivamo [Kroneckerov simbol](https://en.wikipedia.org/wiki/Kronecker_symbol).

## Kvadratni korijen u modularnoj aritmetici

U ovom odjeljku razmatramo algoritme za vađenje kvadratnog korijena u modularnoj aritmetici. Posebno, odjeljak se uglavnom bavi slučajem prostog modula. Za slučaj općeg modula vidi raspravu u [korijeni višeg reda u modularnoj aritmetici](./residue.md#vađenje-korijena-u-modularnoj-aritmetici).

### Algoritam za posebne slučajeve

Za kongruenciju $x^2\equiv a\pmod p$, gdje je $p$ neparan prost broj i $a$ kvadratni ostatak, u slučaju $p\bmod 4=3$ postoji jednostavnije rješenje; promotrimo

$$
\begin{aligned}
\left(a^{(p+1)/4}\right)^2&\equiv a^{(p+1)/2}&\pmod p\\
&\equiv x^{p+1}&\pmod p\\
&\equiv \left(x^2\right)\left(x^{p-1}\right)&\pmod p\\
&\equiv x^2&\pmod p&\quad (\because{\text{Fermat's little theorem}})
\end{aligned}
$$

Tada je $a^{(p+1)/4}\bmod p$ jedno rješenje.

#### Atkinov algoritam

Promatramo i dalje gornju kongruenciju, sada uz $p\bmod 8=5$. Neka je $b\equiv (2a)^{(p-5)/8}\pmod p$ i $\mathrm{i}\equiv 2ab^2\pmod p$. Tada je $\mathrm{i}^2\equiv -1\pmod p$, a $ab(\mathrm{i}-1)\bmod p$ jedno je rješenje.

???+ note "Dokaz"
    $$
    \begin{aligned}
    \mathrm{i}^2&\equiv\left(2ab^2\right)^2&\pmod p\\
    &\equiv \left(2a\cdot \left(2a\right)^{(p-5)/4}\right)^2&\pmod p\\
    &\equiv \left(\left(2a\right)^{(p-1)/4}\right)^2&\pmod p\\
    &\equiv \left(2a\right)^{\frac{p-1}{2}}&\pmod p\\
    &\equiv -1&\pmod p
    \end{aligned}
    $$
    
    Tada je
    
    $$
    \begin{aligned}
    \left(ab(\mathrm{i}-1)\right)^2&\equiv a^2\cdot \left(2a\right)^{(p-5)/4}\cdot (-2\mathrm{i})&\pmod p\\
    &\equiv a\cdot (-\mathrm{i})\cdot \left(2a\right)^{(p-1)/4}&\pmod p\\
    &\equiv a&\pmod p
    \end{aligned}
    $$

### Cipolla algoritam

Cipolla algoritam služi za rješavanje kongruencije $y^2\equiv a\pmod p$, gdje je $p$ neparan prost broj i $a$ kvadratni ostatak.

U ovom odjeljku razmatramo računanje u $\mathbf{F}_p\lbrack x\rbrack /(x^2-g)$, gdje je $g \in \mathbf{F}_p$.

??? note "Način računanja"
    Čitatelji koji nisu upoznati s [prstenima polinoma](../algebra/ring-theory.md#多项式环) mogu to jednostavno shvatiti ovako: elementi tog skupa imaju oblik $a_0+a_1x$ s $a_0,a_1\in\mathbf F_p$ i podliježu sljedećim pravilima računanja:
    
    $$
    \begin{aligned}
    (a_0+a_1x)+(b_0+b_1x) &\equiv (a_0+b_0)+(a_1+b_1)x &\pmod{(x^2-g)}\\
    (a_0+a_1x)(b_0+b_1x) &\equiv (a_0b_0+a_1b_1g)+(a_1b_0+a_0b_1)x &\pmod{(x^2-g)}
    \end{aligned}
    $$
    
    Treba napomenuti da $x$ ovdje nije konkretan broj, nego formalna oznaka u polinomu. Ključna je točka računanja da se pomoću $x^2 \equiv g \pmod{(x^2-g)}$ kvadratni član pretvara u linearni i konstantni član. Osim toga, sve se cjelobrojne operacije rade modulo $p$.
    
    Više o toj strukturi potražite na stranicama [Polinomi](../poly/intro.md), [Teorija polja](../algebra/field-theory.md) i dr.

Prvi je korak algoritma pronaći $r$ takav da je $r^2-a$ kvadratni neostatak. Naravno, za $a \equiv 0 \pmod p$ takav $r$ nije moguće pronaći, pa taj slučaj treba obraditi posebno. U nastavku razmatramo samo slučaj $a \not\equiv 0 \pmod p$. Tada možemo nasumce izabrati $r$ i provjeriti ga; u očekivanju ga nalazimo u $2$ koraka. Tada je $(r-x)^{\frac{p+1}{2}}\bmod (x^2-(r^2-a))$ jedno rješenje, a može se izračunati brzim potenciranjem.

??? note "Zašto su u očekivanju potrebna samo dva koraka"
    Promotrimo slučaj kad je $r^2-a$ kvadratni ostatak. Tada postoji $x$ takav da je $r^2-a \equiv x^2 \pmod p$; prebacivanjem članova dobivamo $(r+x)(r-x) \equiv a \pmod p$. Lako se vidi da svaki $(r+x) \in [1, p-1]$ jednoznačno odgovara jednom paru rješenja $(r,x)$, pa izvorna jednadžba ima ukupno $p-1$ rješenja. Razlikujemo dva slučaja: $x \equiv 0$ i $x \not\equiv 0$. Za $x \equiv 0$, budući da je $a$ kvadratni ostatak, odgovaraju $2$ vrijednosti $r$; za $x \not\equiv 0$ postoji $p-1-2$ slučajeva, a svakom $r$ odgovaraju dva od njih, pa ukupno ima $\dfrac{p-3}{2}$ vrijednosti $r$. Sveukupno, postoji $2+\dfrac{p-3}{2}=\dfrac{p+1}{2}$ slučajeva u kojima je $r^2-a$ kvadratni ostatak, pa je vjerojatnost da u jednom pokušaju dobijemo kvadratni neostatak $\dfrac{p-1}{2p}$, a očekivani broj koraka $\dfrac{2p}{p-1} \approx 2$.

???+ note "Dokaz"
    Radi jednostavnosti, neka je $f(x)=x^2-(r^2-a)\in\mathbf{F}_p\lbrack x\rbrack$.
    
    Treba dokazati da je $(r-x)^{\frac{p+1}{2}} \bmod f(x)$ rješenje izvorne jednadžbe i da pripada $\mathbf{F}_p$. Prvo dokazujemo prvu tvrdnju, tj. da je $(r-x)^{p+1}\equiv a\pmod {f(x)}$. Za to nam prvo trebaju dvije leme:
    
    **Lema 1:** $x^p \equiv -x \pmod {f(x)}$
    
    Dokaz:
    
    $$
    \begin{aligned}
    x^p&= x(x^2)^{\frac{p-1}{2}}\\
    &\equiv x(r^2-a)^{\frac{p-1}{2}}&\pmod{f(x)}&\quad (\because{x^2\equiv r^2-a\pmod{f(x)}})\\
    &\equiv -x&\pmod{f(x)}&\quad (\because{r^2-a}\text{ is quadratic non-residue})
    \end{aligned}
    $$
    
    **Lema 2:** $(a+b)^p \equiv a^p+b^p \pmod p$
    
    Pomoću binomnog teorema lako se vidi da se, osim u prvom i posljednjem članu, $p$ u brojniku ne može pokratiti, pa ostaje samo $a^p+b^p$.
    
    $$
    \begin{aligned}
    (a+b)^p&=\sum_{i=0}^p\binom{p}{i}a^ib^{p-i}\\
    &=\sum_{i=0}^p\frac{p!}{i!(p-i)!}a^ib^{p-i}\\
    &\equiv a^p+b^p\pmod p
    \end{aligned}
    $$
    
    S tim dvjema lemama vratimo se dokazu izvorne tvrdnje:
    
    $$
    \begin{aligned}
    (r-x)^{p+1}
    &= (r-x)^p(r-x)\\
    &\equiv (r^p-x^p)(r-x)&\pmod{f(x)}\\
    &\equiv (r+x)(r-x)&\pmod{f(x)}\\
    &= r^2-x^2\\
    &\equiv r^2-(r^2-a)&\pmod{f(x)}\\
    &= a\\
    \end{aligned}
    $$
    
    Sada kontradikcijom dokazujemo da dobiveno rješenje pripada $\mathbf{F}_p$, tj. da mu je koeficijent uz $x$ jednak $0$.
    
    Pretpostavimo da postoji $(a_0+a_1x)^2 \equiv a \pmod {f(x)}$ s $a_1 \not\equiv 0 \pmod p$, tj. $a_0^2+2a_0a_1x+a_1^2x^2 \equiv a \pmod {f(x)}$; prebacivanjem članova i sređivanjem dobivamo:
    
    $$
    a_0^2+a_1^2(r^2-a)-a \equiv -2a_0a_1x \pmod {f(x)}
    $$
    
    Koeficijent uz $x$ na lijevoj strani jednak je $0$, pa je i koeficijent uz $x$ na desnoj strani $0$, tj. $a_0a_1 \equiv 0 \pmod p$. Budući da smo pretpostavili $a_1 \not\equiv 0 \pmod p$, nužno je $a_0 \equiv 0 \pmod p$, pa je $(a_1x)^2 \equiv a \pmod {f(x)}$, tj. $r^2-a \equiv aa_1^{-2} \pmod p$.
    
    Kako su $a$ i $a_1^{-2}$ kvadratni ostatci, prema multiplikativnosti Legendreova simbola i $aa_1^{-2}$ je kvadratni ostatak, što je u kontradikciji s tim da je $r^2-a$ kvadratni neostatak. Dakle, izvorna jednadžba nema rješenja s koeficijentom uz $x$ različitim od $0$, pa je i koeficijent uz $x$ u našem rješenju nužno $0$.

??? example "Zadatak-predložak [Luogu P5491【模板】二次剩余 (predložak: kvadratni ostatak)](https://www.luogu.com.cn/problem/P5491)"
    ```cpp
    --8<-- "docs/math/code/quad-residue/quad-residue_1.cpp"
    ```

### Bostan–Mori algoritam

Taj se algoritam temelji na Cipolla algoritmu: problem pretvaramo u [homogenu linearnu rekurziju s konstantnim koeficijentima](../poly/linear-recurrence.md) i zatim primjenjujemo Bostan–Mori algoritam. Promotrimo drugi uobičajeni opis Cipolla algoritma: $b=x^{\left(p+1\right)/2}\bmod{\left(x^2-tx+a\right)}$ jedno je rješenje koje zadovoljava $b^2\equiv a\pmod{p}$[^ref3], gdje je $x^2-tx+a\in \mathbf{F}_p\lbrack x\rbrack$ nesvodljiv polinom. Koeficijent $t$ također se bira nasumce. Dokaz izostavljamo. Prema algoritmu iz rada Bostana i Morija[^ref4] vidimo da se problem može svesti na računanje jednog koeficijenta multiplikativnog inverza formalnog reda potencija:

$$
b=\left\lbrack x^{(p+1)/2}\right\rbrack\dfrac{1}{1-tx+ax^2}
$$

i

$$
\left\lbrack x^n\right\rbrack\dfrac{k_0+k_1x}{1+k_2x+k_3x^2}=
\begin{cases}
\left\lbrack x^{(n-1)/2}\right\rbrack\dfrac{k_1-k_0k_2+k_1k_3x}{1+(2k_3-k_2^2)x+k_3^2x^2},&\text{if }n\bmod 2=1\\
\left\lbrack x^{n/2}\right\rbrack\dfrac{k_0+(k_0k_3-k_1k_2)x}{1+(2k_3-k_2^2)x+k_3^2x^2},&\text{else if }n\neq 0
\end{cases}
$$

a za $n=0$ očito je $\left\lbrack x^0\right\rbrack\dfrac{k_0+k_1x}{1+k_2x+k_3x^2}=k_0$. Taj algoritam ima manje množenja nego Cipolla algoritam. Drugi srodni algoritmi s malim brojem množenja mogu se naći u Müllerovu članku[^ref2].

### Legendreov algoritam

Za kongruenciju $x^2\equiv a\pmod p$, gdje je $p$ neparan prost broj i $a$ kvadratni ostatak, Legendreov se algoritam može opisati ovako: nađemo $r$ takav da je $r^2-a$ kvadratni neostatak i stavimo $a_0+a_1x=(r-x)^{\frac{p-1}{2}}\bmod (x^2-a)$; tada je $a_0\equiv 0\pmod p$ i $a_1^{-2}\equiv a\pmod p$.

???+ note "Dokaz"
    Izaberimo $b$ takav da je $b^2\equiv a\pmod p$. Tada je $(r-b)(r+b)=r^2-a$ kvadratni neostatak, pa je
    
    $$
    (r-b)^{\frac{p-1}{2}}(r+b)^{\frac{p-1}{2}}\equiv -1\pmod p
    $$
    
    Postoji homomorfizam prstena
    
    $$
    \begin{aligned}
    \phi:\mathbf{F}_p\lbrack x\rbrack/(x^2-a)&\to \mathbf{F}_p\times \mathbf{F}_p\\
    x&\mapsto (b,-b)
    \end{aligned}
    $$
    
    Tada je
    
    $$
    \begin{aligned}
    (a_0+a_1b,a_0-a_1b)&=\phi(a_0+a_1x)\\
    &=\phi(r-x)^{\frac{p-1}{2}}\\
    &=((r-b)^{\frac{p-1}{2}},(r+b)^{\frac{p-1}{2}})\\
    &=(\pm 1,\mp 1)
    \end{aligned}
    $$
    
    pa je $2a_0=(\pm 1)+(\mp 1)=0$ i $2a_1b=(\pm 1)-(\mp 1)=\pm 2$.

### Tonelli–Shanksov algoritam

Tonelli–Shanksov algoritam algoritam je za rješavanje kongruencije $x^2\equiv a\pmod p$ temeljen na diskretnom logaritmu[^ref1], gdje je $p$ neparan prost broj i $a$ kvadratni ostatak modulo $p$.

Neka je $p-1=m2^n$, gdje je $m$ neparan. I dalje nasumce tražimo $r\in\mathbf{F}_p$ takav da je $r$ kvadratni neostatak. Neka je $g\equiv r^m\pmod p$ i $b\equiv a^{(m-1)/2}\pmod p$. Tada postoji cijeli broj $e\in\lbrace 0,1,2,\dots ,2^n-1\rbrace$ takav da je $ab^2\equiv g^e\pmod p$. Ako je $a$ kvadratni ostatak, onda je $e$ paran i $\left(abg^{-e/2}\right)^2\equiv a\pmod p$.

???+ note "Dokaz"
    Prema malom Fermatovu teoremu vrijedi
    
    $$
    g^{2^n} \equiv r^{m2^n} = r^{p-1} \equiv 1 \pmod p.
    $$
    
    Budući da je $r$ kvadratni neostatak, vrijedi i
    
    $$
    g^{2^{n-1}} \equiv r^{m2^{n-1}} = r^{\frac{p-1}{2}} \equiv -1 \pmod p.  
    $$
    
    Dakle, red elementa $g$ modulo $p$ jest $2^n$. Nadalje, budući da je $ab^2\equiv a^m\pmod p$ rješenje jednadžbe $x^{2^n}\equiv 1\pmod p$, $a^m$ je potencija od $g$. Pišimo $a^m\equiv g^e\pmod p$.
    
    Budući da je $a$ kvadratni ostatak, vrijedi
    
    $$
    g^{e2^{n-1}} \equiv a^{m2^{n-1}} = a^{\frac{p-1}{2}} \equiv 1 \pmod p.
    $$
    
    Prema svojstvima reda elementa vrijedi $2^n\mid e2^{n-1}$, pa je $e$ paran. Stoga je $abg^{-e/2}\bmod p$ dobro definirano i
    
    $$
    \left(abg^{-e/2}\right)^2 = a^2b^2g^{-e} \equiv a^{m+1}g^{-e} \equiv a \pmod p.
    $$

Preostaje pitanje kako izračunati $e$. Tonelli i Shanks predložili su određivanje jedne binarne znamenke od $e$ odjednom. Zapišimo $e$ u binarnom obliku $e=e_0+2e_1+4e_2+\cdots$, gdje je $e_k\in\lbrace 0,1\rbrace$. Budući da je $a$ kvadratni ostatak, na početku je $e_0=0$, a zatim se vrijednosti $e_k$ određuju znamenku po znamenku pomoću sljedećeg svojstva:

$$
\left(g^eg^{-(e\bmod 2^k)}\right)^{2^{n-1-k}}\equiv g^{2^{n-1}\cdot e_k}\equiv 
\begin{cases}
1\pmod p,&\text{if }e_k=0\\
-1\pmod p,&\text{if }e_k=1
\end{cases}
$$

Pri tome je $g^e\equiv ab^2\pmod p$ poznato, a vrijednost $e\bmod 2^k$ može se izračunati iz prethodnih znamenki $e_0,e_1,\cdots,e_{k-1}$. Naravno, pri implementaciji algoritma dovoljno je izravno održavati umnožak $g^eg^{-(e\bmod 2^k)}\bmod p$.

## Zadaci za vježbu

-   [Luogu P5491【模板】二次剩余 (predložak: kvadratni ostatak)](https://www.luogu.com.cn/problem/P5491)
-   [„Timus 1132” Square Root](https://acm.timus.ru/problem.aspx?space=1&num=1132)

## Literatura i bilješke

1.  [Quadratic residue - Wikipedia](https://en.wikipedia.org/wiki/Quadratic_residue)
2.  [Euler's criterion - Wikipedia](https://en.wikipedia.org/wiki/Euler%27s_criterion)

[^ref1]: Daniel. J. Bernstein. Faster Square Roots in Annoying Finite Fields.

[^ref2]: S. Müller, On the computation of square roots in finite fields, Design, Codes and Cryptography, Vol.31, pp. 301-312, 2004.

[^ref3]: A. Menezes, P. van Oorschot and S. Vanstone. Handbook of Applied Cryptography, 1996.

[^ref4]: Alin Bostan, Ryuhei Mori. A Simple and Fast Algorithm for Computing the N-th Term of a Linearly Recurrent Sequence. Available at <https://arxiv.org/abs/2008.08822>.

[^ref5]: [Proofs of quadratic reciprocity - Wikipedia](https://en.wikipedia.org/wiki/Proofs_of_quadratic_reciprocity)

[^ref6]: Carl Friedrich Gauss. Untersuchungen über höhere Arithmetik, 1965. Page 458-462.

[^ref7]: Kobi Kremnizer.[Lectures in number theory 2022](https://courses.maths.ox.ac.uk/pluginfile.php/29788/mod_resource/content/1/numbertheory-2022.pdf). Proposition 4.3.
