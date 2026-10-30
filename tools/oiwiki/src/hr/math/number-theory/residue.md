---
title: Ostatci višeg reda & korijeni jedinice
---

Predznanje: [Diskretni logaritam](./discrete-logarithm.md)

U ovom se tekstu razmatraju ostatci višeg reda (higher-order residues) i korijeni jedinice (roots of unity) u modularnoj aritmetici te se predstavljaju algoritmi za vađenje korijena po modulu.

## Ostatci višeg reda

Ostatke višeg reda u modularnoj aritmetici možemo shvatiti kao pitanje izvedivosti vađenja korijena višeg reda po modulu. To je poopćenje [kvadratnih ostataka](./quad-residue.md).

???+ abstract "$k$-ti ostatak"
    Neka je $k\geq 2$ cijeli broj te neka su cijeli broj $a$ i pozitivan cijeli broj $m$ relativno prosti. Ako postoji cijeli broj $x$ takav da je
    
    $$
    x^k\equiv a\pmod m,
    $$
    
    tada se $a$ naziva **$k$-ti ostatak** ($k$-th residue) modulo $m$, a $x$ **$k$-ti korijen** ($k$-th root) od $a$ modulo $m$; inače se $a$ naziva **$k$-ti neostatak** ($k$-th nonresidue) modulo $m$.

Drugim riječima, $k$-ti korijen od $a$ modulo $m$ postoji ako i samo ako je $a$ $k$-ti ostatak modulo $m$.

### Svojstva

Slično kvadratnim ostatcima, možemo razmatrati pitanja određivanja $k$-tih ostataka, broja korijena te broja klasa $k$-tih ostataka. Kao i kod drugih problema s [kongruencijama](./congruence-equation.md), pomoću [kineskog teorema o ostatcima](./crt.md) oni se mogu svesti na slučaj modula koji je potencija prostog broja. Ovisno o tome postoji li primitivni korijen, to se dalje dijeli na slučaj potencije neparnog prostog broja i slučaj modula koji je potencija broja $2$.

Slučaj potencije neparnog prostog broja razmjerno je jednostavan. Zapravo, za sve slučajeve u kojima postoji primitivni korijen vrijedi sljedeći zaključak:

???+ note "Teorem"
    Neka je $k\geq 2$ cijeli broj te neka su cijeli broj $a$ i pozitivan cijeli broj $m$ relativno prosti. Pretpostavimo da primitivni korijen modulo $m$ postoji i da je $g$ jedan primitivni korijen modulo $m$. Označimo $d=\gcd(k,\varphi(m))$ i $d'=\dfrac{\varphi(m)}{d}$, gdje je $\varphi(m)$ [Eulerova funkcija](./euler-totient.md). Tada vrijedi:
    
    1.  $a$ je $k$-ti ostatak modulo $m$ ako i samo ako je
    
        $$
        a^{d'} \equiv 1 \pmod m.
        $$
    2.  Kad je $a$ $k$-ti ostatak modulo $m$, $a$ ima, u smislu kongruencije, točno $d$ međusobno različitih $k$-tih korijena modulo $m$, i oni su oblika
    
        $$
        x \equiv g^{y_0+id'}\pmod m,~0\le y_0 < d',~i=0,1,\cdots,d-1.
        $$
    3.  Broj klasa $k$-tih ostataka modulo $m$ je $d'$, a sve one zajedno čine skup
    
        $$
        \{g^{di}\bmod m : 0 \le i < d'\}.
        $$

??? note "Dokaz"
    Budući da je $a\perp m$, vrijedi $x\perp m$. Budući da je $g$ primitivni korijen modulo $m$, i $x$ i $a$ kongruentni su nekoj potenciji od $g$. Neka je $x\equiv g^y\pmod m$; jednadžba $x^k\equiv a\pmod m$ tada je ekvivalentna s
    
    $$
    g^{ky} \equiv g^{\operatorname{ind}_g a}\pmod m.
    $$
    
    Pritom je $\operatorname{ind}_g a$ diskretni logaritam. Prema [svojstvima reda](./primitive-root.md#幂的循环结构) i $\delta_m(g)=\varphi(m)$, to je ekvivalentno kongruenciji
    
    $$
    ky \equiv \operatorname{ind}_g a \pmod{\varphi(m)}.
    $$
    
    To je [linearna kongruencija](./linear-equation.md) po $y$. Primjenom analize strukture rješenja s te stranice zaključujemo da jednadžba ima rješenje ako i samo ako $d\mid\operatorname{ind}_g a$, a opće je rješenje oblika
    
    $$
    y \equiv y_0 + id' \pmod{\varphi(m)},~0\le y_0 < d',~i=0,1,\cdots,d-1.
    $$
    
    Odatle se dobiva gotovo cijeli sadržaj teorema; jedino što još treba objasniti jest kriterij $a^{d'} \equiv 1 \pmod m$. Prema [svojstvu reda 3](./primitive-root.md#幂的循环结构) vrijedi
    
    $$
    \delta_m(a) = \delta_m(g^{\operatorname{ind}_g a}) = \dfrac{\varphi(m)}{\gcd(\varphi(m),\operatorname{ind}_g a)}.
    $$
    
    Već znamo da jednadžba ima rješenje ako i samo ako $d\mid \operatorname{ind}_g a$, odnosno $\delta_m(a)\mid d'$. Prema [svojstvu reda 2](./primitive-root.md#幂的循环结构), to je ekvivalentno tom kriteriju.

Slučaj modula koji je potencija broja $2$ nešto je posebniji. Za obradu tog slučaja potreban je jedan [rezultat](./primitive-root.md#递推公式) o strukturi reduciranog sustava ostataka modulo $2^e$: svaki neparan broj $a$ na jedinstven je način kongruentan nekom cijelom broju oblika $(-1)^s5^r\bmod 2^e$, gdje je $s\in\{0,1\}$ i $0\le r < 2^{e-2}$. Pomoću tog rezultata dobiva se sljedeći zaključak:

???+ note "Teorem"
    Neka je $k\ge 2$ cijeli broj, $a$ neparan broj i $m=2^e$ pozitivan cijeli broj uz $e \ge 2$. Tada, kad je $k$ neparan, vrijedi:
    
    1.  $a$ je uvijek $k$-ti ostatak modulo $m$.
    2.  $a$ ima točno jedan $k$-ti korijen modulo $m$.
    3.  Broj klasa $k$-tih ostataka modulo $m$ je $2^{e-1}$, i to su upravo sve reducirane klase ostataka.
    
    Kad je $k$ paran, označimo $d=\gcd(k,2^{e-2})$ i $d'=\dfrac{2^{e-2}}{d}$; tada vrijedi:
    
    1.  $a$ je $k$-ti ostatak modulo $m$ ako i samo ako je $a\equiv 1\pmod 4$ i $a^{d'}\equiv 1\pmod m$.
    2.  Kad je $a$ $k$-ti ostatak modulo $m$, $a$ ima, u smislu kongruencije, točno $2d$ međusobno različitih $k$-tih korijena modulo $m$, i oni su oblika
    
        $$
        x \equiv \pm 5^{y_0 + id'} \pmod{2^e},~ 0 \le y_0 < d',~i = 0, 1,\cdots,d-1. 
        $$
    3.  Broj klasa $k$-tih ostataka modulo $m$ je $d'$, a sve one zajedno čine skup
    
        $$
        \{5^{di}\bmod m : 0 \le i < d'\}.
        $$

??? note "Dokaz"
    Budući da je $a\perp m$, vrijedi $x\perp m$. Budući da su $x$ i $a$ neparni, prema gornjem rezultatu možemo pisati $a\equiv (-1)^s5^r\pmod{2^e}$ i $x\equiv(-1)^z5^{y}\pmod{2^e}$. Budući da je prikaz jedinstven, kongruencija $x^k\equiv a\pmod{2^e}$ ekvivalentna je sustavu [linearnih kongruencija](./linear-equation.md)
    
    $$
    \begin{aligned}
    kz &\equiv s \pmod{2},\\
    ky &\equiv r \pmod{2^{e-2}}.
    \end{aligned}
    $$
    
    U kombinaciji s analizom rješenja linearnih kongruencija s te stranice dobiva se struktura rješenja kongruencije $x^k\equiv a\pmod{2^e}$. Ovisno o parnosti broja $k$ razlikujemo dva slučaja:
    
    -   Kad je $k$ neparan, budući da je $\gcd(k,2)=\gcd(k,2^{e-2})=1$, obje linearne kongruencije imaju rješenje za sve $s,r$, pa polazna kongruencija uvijek ima rješenje za sve neparne $a$.
    -   Kad je $k$ paran, prva jednadžba ima rješenje ako i samo ako $2\mid s$, a druga ima rješenje ako i samo ako $d=\gcd(k,2^{e-2})\mid r$. Spajanjem toga dvoga dobiva se oblik svih klasa $k$-tih ostataka. Izravnim računom vidi se da je prvi uvjet ekvivalentan s $a\equiv 1\pmod 4$; ponavljanjem analize iz slučaja potencije neparnog prostog broja vidi se da je drugi uvjet ekvivalentan s $a^{d'}\equiv 1\pmod m$. Spajanjem tih dviju točaka dobiva se kriterij iz teorema. Opća rješenja obiju linearnih kongruencija također su poznata:
    
        $$
        \begin{aligned}
        z &\equiv0,1\pmod 2, \\
        y &\equiv y_0 + id' \pmod{2^{e-2}},~ 0\le y_0 < d',~i=0,1,\cdots,d-1.
        \end{aligned}
        $$
    
        Njihovim spajanjem dobiva se opće rješenje polazne jednadžbe.

Time je problem određivanja $k$-tih ostataka za različite module potpuno riješen. Legendreov simbol i zakon kvadratnog reciprociteta iz teorije kvadratnih ostataka također se mogu poopćiti na ostatke višeg reda, ali to nije jednostavno i zahtijeva pojmove poput [ciklotomskih polja](../algebra/field-theory.md#分圆域). U algebarskoj teoriji brojeva zakon kvadratnog reciprociteta u konačnici se poopćuje do [Artinova zakona reciprociteta](https://en.wikipedia.org/wiki/Artin_reciprocity).

## Korijeni jedinice

Kao poseban slučaj $k$-tih korijena, u ovom odjeljku razmatramo pojam $k$-tog (primitivnog) korijena jedinice. Možemo ga shvatiti kao pandan pojma $k$-tog [korijena jedinice](../complex.md#单位根) u polju kompleksnih brojeva $\mathbf C$ unutar reduciranog sustava ostataka $\mathbf Z_m^*$ modulo $m$. Kad je modul $m$ prikladan, zamjena kompleksnog korijena $\omega_k$ $k$-tim primitivnim korijenom jedinice modulo $m$ može ubrzati računanje.

Slično kao u polju kompleksnih brojeva, imamo sljedeću definiciju:

???+ abstract "$k$-ti korijen jedinice modulo $m$"
    Za modul $m$, $k$-ti korijen elementa $1$ naziva se **$k$-ti korijen jedinice modulo $m$** ($k$-th root of unity modulo $m$). Posebno, ako je $x$ $k$-ti korijen jedinice modulo $m$ i nije korijen jedinice modulo $m$ ni za koji red $k' < k$, tada se $x$ naziva i **$k$-ti primitivni korijen jedinice modulo $m$** ($k$-th primitive root of unity modulo $m$).

Usporedbom s [definicijom primitivnog korijena](./primitive-root.md#原根) vidi se da je primitivni korijen $g$ upravo $\varphi(m)$-ti primitivni korijen jedinice modulo $m$, gdje je $\varphi(m)$ [Eulerova funkcija](./euler-totient.md).

Kad $k$-ti primitivni korijen jedinice modulo $m$ postoji, njegova su algebarska svojstva jednaka svojstvima $k$-tog primitivnog kompleksnog korijena jedinice $\omega_k$, pa može zamijeniti $\omega_k$ u raznim izračunima. Na primjer, primjenom u [brzoj Fourierovoj transformaciji](../poly/fft.md) dobiva se [brza teorijsko-brojevna transformacija](../poly/ntt.md) nad konačnim poljem[^fnnt].

### Svojstva

U polju kompleksnih brojeva (primitivni) korijeni jedinice postoje za svaki red. U teoriji brojeva, međutim, s (primitivnim) korijenima jedinice nije tako.

???+ note "Svojstva"
    Za modul $m$ neka je $\lambda(m)$ njegova [Carmichaelova funkcija](./primitive-root.md#carmichael-函数). Tada vrijedi:
    
    1.  Svaki cijeli broj $a$ relativno prost s $m$ jest $\delta_m(a)$-ti primitivni korijen jedinice modulo $m$, gdje je $\delta_m(a)$ [red](./primitive-root.md#阶) od $a$ modulo $m$.
    2.  Ako je element $a$ $k$-ti korijen jedinice modulo $m$ i $k'$ je bilo koji višekratnik od $k$, tada je $a$ i $k'$-ti korijen jedinice modulo $m$.
    3.  Ako je element $a$ $k$-ti (primitivni) korijen jedinice modulo $m$, tada je element $a^{\ell}$ $\dfrac{k}{\gcd(k,\ell)}$-ti (odgovarajuće, primitivni) korijen jedinice modulo $m$.
    4.  Kad $k'$ prolazi djeliteljima od $k$, svi $k'$-ti primitivni korijeni jedinice modulo $m$ čine particiju skupa $k$-tih korijena jedinice modulo $m$. Štoviše, za $\ell\perp k$ preslikavanje $x\mapsto x^\ell$ daje bijekciju među $k$-tim korijenima jedinice koja čuva tu particiju: primitivne korijene jedinice reda $k'\mid k$ preslikava ponovno u $k'$-te primitivne korijene jedinice.
    5.  $k$-ti primitivni korijen jedinice modulo $m$ postoji ako i samo ako $k\mid\lambda(m)$. Posebno, $\lambda(m)$-ti primitivni korijen jedinice modulo $m$ postoji i naziva se **$\lambda$‑primitivni korijen modulo $m$**.
    6.  Element $a$ je $k$-ti primitivni korijen jedinice modulo $m$ ako i samo ako je $a^k\equiv 1\pmod{m}$ i za svaki prosti faktor $p\mid k$ vrijedi $a^{k/p}\not\equiv 1\pmod{m}$.

??? note "Dokaz"
    Prema definiciji reda, svaki cijeli broj $a$ relativno prost s $m$ jest $\delta_m(a)$-ti primitivni korijen jedinice modulo $m$, gdje je $\delta_m(a)$ red od $a$ modulo $m$. Obratno, ako je $a$ $k$-ti korijen jedinice modulo $m$, tada je $\gcd(a^k,m)=1$, pa je $\gcd(a,m)=1$. Dakle, $a$ je (primitivni) korijen jedinice modulo $m$ ako i samo ako je $a$ relativno prost s $m$. To je svojstvo 1.
    
    Izravnom provjerom definicije vidi se da se, čim $k\mid k'$, iz $a^k\equiv 1\pmod m$ može izvesti $a^{k'}\equiv 1\pmod m$; to je svojstvo 2. Prema [svojstvima reda](./primitive-root.md#幂的循环结构) vrijedi
    
    $$
    \delta_m(a^\ell) = \dfrac{\delta_m(a)}{\gcd(\delta_m(a),\ell)}.
    $$
    
    Ako je $a$ $k$-ti primitivni korijen jedinice modulo $m$, tada je $\delta_m(a)=k$, pa izravnim uvrštavanjem u gornju formulu dobivamo da je $a^\ell$ $\dfrac{k}{\gcd(k,\ell)}$-ti primitivni korijen jedinice modulo $m$. Ako je $a$ samo $k$-ti korijen jedinice modulo $m$, neka je on primitivni korijen jedinice reda $k'\mid k$; tada je $a^\ell$ $\dfrac{k'}{\gcd(k',\ell)}$-ti primitivni korijen jedinice modulo $m$. Budući da $k'\mid k$, vrijedi
    
    $$
    \dfrac{k'}{\gcd(k',\ell)} \mid \dfrac{k}{\gcd(k,\ell)},
    $$
    
    pa prema svojstvu 2 dobivamo da je $a^\ell$ $\dfrac{k}{\gcd(k,\ell)}$-ti korijen jedinice modulo $m$. To je svojstvo 3.
    
    Za $k'\mid k$, prema svojstvu 2, $k'$-ti primitivni korijen jedinice modulo $m$ nužno je $k$-ti korijen jedinice modulo $m$; obratno, svaki $k$-ti korijen jedinice $a$ modulo $m$ jest $\delta_m(a)$-ti primitivni korijen jedinice, pri čemu $\delta_m(a)\mid k$. Ti su skupovi u parovima disjunktni, pa čine particiju. Nadalje, za $\ell\perp k$ uvijek je $\ell\perp k'$, pa je za $k'$-ti primitivni korijen jedinice $a$ modulo $m$ i $a^\ell$ uvijek $k'$-ti primitivni korijen jedinice modulo $m$. Uzmemo li $\ell'=\ell^{-1}\bmod k$, može se provjeriti da su $x\mapsto x^\ell$ i $x\mapsto x^{\ell'}$ međusobno inverzna preslikavanja, pa je $x\mapsto x^\ell$ bijekcija. To je svojstvo 4.
    
    Prema svojstvima Carmichaelove funkcije, $\lambda(m)$-ti primitivni korijen jedinice modulo $m$ uvijek postoji; označimo ga s $a$, tako da je $\delta_m(a)=\lambda(m)$. Za $k\mid\lambda(m)$ neka je $k'=\dfrac{\lambda(m)}{k}$; uvijek vrijedi
    
    $$
    \delta_m(a^{k'}) = \dfrac{\lambda(m)}{\gcd(\lambda(m),k')} = \dfrac{\lambda(m)}{k'} = k.
    $$
    
    Dakle, $a^{k'}$ je $k$-ti primitivni korijen jedinice. S druge strane, prema definiciji Carmichaelove funkcije, red svakog $x\perp m$ djelitelj je od $\lambda(m)$. Time dobivamo svojstvo 5.
    
    Gotovo doslovnim ponavljanjem dokaza [kriterija za primitivni korijen](./primitive-root.md#原根判定定理) dobiva se svojstvo 6. Taj kriterij zapravo provjerava $\delta_m(a)=k$.

Iz tih se svojstava vidi da $\lambda$‑primitivni korijen modulo $m$ ima sličnu temeljnu ulogu kao primitivni korijen u slučaju kad on postoji. Za razliku od primitivnog korijena, potencijama $\lambda$‑primitivnog korijena ne mogu se generirati svi korijeni jedinice modulo $m$. Unatoč tome, budući da gustoća $\lambda$‑primitivnih korijena nije mala[^lambda-density], ako doista treba pronaći $k$-ti primitivni korijen jedinice, možemo najprije nasumičnim pretraživanjem pronaći $\lambda$‑primitivni korijen, a zatim potenciranjem dobiti $k$-ti primitivni korijen jedinice.

Ako je poznat jedan $k$-ti korijen od $a$ modulo $m$, pomoću svih $k$-tih korijena jedinice modulo $m$ mogu se generirati svi $k$-ti korijeni od $a$ modulo $m$.

???+ note "Teorem"
    Neka je $x$ jedan $k$-ti korijen od $a$ modulo $m$. Kad $r$ prolazi svim $k$-tim korijenima jedinice modulo $m$, $xr$ prolazi svim $k$-tim korijenima od $a$ modulo $m$.

??? note "Dokaz"
    Za dva $k$-ta korijena $x,y$ od $a$ modulo $m$ neka je $r=x^{-1}y\bmod m$; tada $r$ zadovoljava $r^k\equiv 1\pmod m$, pa je $k$-ti korijen jedinice modulo $m$. Obratno, čim je $r$ $k$-ti korijen jedinice modulo $m$, vrijedi $(xr)^{k}= x^kr^k\equiv a\pmod m$, odnosno $xr$ je $k$-ti korijen od $a$ modulo $m$.

Generiranje svih $k$-tih korijena pomoću $k$-tih korijena jedinice slično je generiranju općeg rješenja nehomogenog sustava linearnih jednadžbi pomoću rješenja homogenog sustava.

Dosad smo razmatrali opći slučaj. Samo u slučaju kad primitivni korijen postoji struktura korijena jedinice je jednostavnija:

???+ note "Teorem"
    Za modul $m$ pretpostavimo da primitivni korijen modulo $m$ postoji i da je $a$ $k$-ti primitivni korijen jedinice modulo $m$. Tada je $b$ $k$-ti korijen jedinice modulo $m$ ako i samo ako se može prikazati kao potencija od $a$.

??? note "Dokaz"
    Neka je $g$ primitivni korijen modulo $m$; tada se svaki element relativno prost s $m$ može prikazati kao potencija od $g$. Tada je $a$ $k$-ti primitivni korijen jedinice modulo $m$ ako i samo ako je
    
    $$
    \delta_m(a) = \delta_m(g^{\operatorname{ind}_ga}) = \dfrac{\varphi(m)}{\gcd(\varphi(m),\operatorname{ind}_ga)} = k.
    $$
    
    Slično, $b$ je $k$-ti korijen jedinice modulo $m$ ako i samo ako je
    
    $$
    \delta_m(b) = \delta_m(g^{\operatorname{ind}_gb}) = \dfrac{\varphi(m)}{\gcd(\varphi(m),\operatorname{ind}_gb)} = k' \mid k.
    $$
    
    Stoga vrijedi
    
    $$
    \gcd(\varphi(m),\operatorname{ind}_ga) \mid \gcd(\varphi(m),\operatorname{ind}_gb)\mid \operatorname{ind}_gb.
    $$
    
    Prema [analizi](./linear-equation.md) linearnih kongruencija, taj je uvjet ekvivalentan tome da jednadžba
    
    $$
    (\operatorname{ind}_ga) x \equiv \operatorname{ind}_gb \pmod{\varphi(m)}
    $$
    
    ima rješenje. Potenciramo li $g$ tim uvjetom, dobivamo $a^x\equiv b\pmod{m}$, odnosno $b$ se može prikazati kao potencija od $a$.

Taj teorem pokazuje da, kad primitivni korijen postoji, svi $k$-ti korijeni jedinice imaju strukturu [cikličke grupe](../algebra/group-theory.md#循环群), a $k$-ti primitivni korijeni jedinice generatori su te cikličke grupe. Kasnije ćemo vidjeti da upravo to iskorištava Tonelli–Shanksov algoritam kako bi ubrzao računanje diskretnog logaritma pri vađenju korijena.

## Vađenje korijena u modularnoj aritmetici

Na kraju razmatramo kako izračunati $k$-ti korijen. Za slučaj $k=2$ postoji [mnogo učinkovitih algoritama](./quad-residue.md#模意义下开平方) za vađenje kvadratnog korijena po modulu. Za opći $k$, međutim, nije poznat algoritam polinomnog vremena. U ovom odjeljku predstavljamo dva uobičajena algoritma, koji $k$-ti korijen pronalaze u vremenu $O(m^{1/2})$ odnosno $O(m^{1/4+\varepsilon})$. Pomoću kineskog teorema o ostatcima problem se uvijek može svesti na slučaj modula koji je potencija prostog broja, pa se u ovom odjeljku uglavnom razmatra rješavanje za takve module.

### Naivni algoritam

Prethodna [analiza](#svojstva) svojstava $k$-tih ostataka zapravo već ukazuje na jedan način računanja $k$-tog korijena modulo potencija prostog broja. Strogo govoreći, prethodno je riješen slučaj u kojem su radikand $a$ i modul $m$ relativno prosti. Postupak algoritma sažeto glasi:

-   Kad je $m=p^e$ potencija neparnog prostog broja, neka je $g$ jedan primitivni korijen modulo $m$. Tada se jednadžba $x^k\equiv a\pmod m$ može svesti na linearnu kongruenciju

    $$
    ky \equiv \operatorname{ind}_g a \pmod{\varphi(m)}.
    $$

    Pritom se $\operatorname{ind}_g a$ može izračunati [BSGS algoritmom](./discrete-logarithm.md#大步小步算法), a sva rješenja [linearne kongruencije](./linear-equation.md) lako je pronaći. Odatle dobivamo sve $k$-te korijene $x\equiv g^y\pmod m$ od $a$.

    Osim toga, postoji i sličan alternativni pristup. Ponovno uz $x\equiv g^y\pmod m$, preoblikovanjem

    $$
    x^k \equiv (g^k)^y \equiv a \pmod m
    $$

    problem se svodi na računanje diskretnog logaritma od $a$ s bazom $g^k$. I to se može riješiti BSGS algoritmom, čime se dobiva jedno partikularno rješenje. Opće se rješenje može dobiti iz prethodno navedenog izraza za rješenja, odnosno množenjem partikularnog rješenja redom sa svim $k$-tim korijenima jedinice.

    Koji god pristup odabrali, uz poznat primitivni korijen složenost pronalaženja jednog rješenja tim algoritmom iznosi $O(m^{1/2})$. Budući da se primitivni korijen može pronaći u vremenu $o(m^{1/2})$, ukupna vremenska složenost i dalje je $O(m^{1/2})$.

-   Kad je $m=2^e$ uz $e\in\mathbf N_+$, možemo najprije odrediti $s,r$ u $a\equiv (-1)^s5^r\pmod m$. Od tih dvaju eksponenata, $s$ se može odrediti u vremenu $O(1)$:

    $$
    s = \begin{cases}0, & a\equiv 1\pmod 4, \\ 1, & a\equiv 3\pmod 4.\end{cases}
    $$

    A $r=\operatorname{ind}_5((-1)^sa)$ može se BSGS algoritmom izračunati u vremenu $O(m^{1/2})$. Zatim treba samo riješiti sustav linearnih kongruencija:

    $$
    \begin{aligned}
    kz &\equiv s \pmod{2},\\
    ky &\equiv r \pmod{2^{e-2}}.
    \end{aligned}
    $$

    Opće rješenje $(z,y)$ tog sustava linearnih kongruencija lako je pronaći, a $x=(-1)^z5^y$ je traženi korijen. Složenost pronalaženja jednog rješenja tim algoritmom također je $O(m^{1/2})$.

Dakako, za slučaj kad rješenja nema, to se zapravo može brzo utvrditi u vremenu $O(\log m)$ pomoću prethodno opisanog kriterija, pa to nije potrebno provjeravati tijekom samog rješavanja.

Referentna implementacija računanja $k$-tog korijena modulo prost broj glasi: (kôd služi samo kao ilustracija; zbog previsoke vremenske složenosti ne prolazi ovaj zadatak)

??? example "Referentna implementacija za ogledni zadatak [Library Checker - Kth Root (Mod)](https://judge.yosupo.jp/problem/kth_root_mod)"
    ```cpp
    --8<-- "docs/math/code/residue/bsgs-mod-p.cpp"
    ```

### Poboljšani Tonelli–Shanksov algoritam

Prikladnim poopćenjem [Tonelli–Shanksova algoritma](./quad-residue.md#tonellishanks-算法) za vađenje kvadratnog korijena po modulu može se riješiti vađenje korijena modulo potencija prostog broja. Jedan razmjerno izravan način poopćenja jest Adleman–Manders–Millerov algoritam[^amm], ali njegova složenost još uvijek nije dovoljno dobra[^amm-comp]. U ovom odjeljku predstavljamo poboljšani Tonelli–Shanksov algoritam koji su predložili sugarknri, Min\_25, 37zigen i drugi. On pronalazi jedan $k$-ti korijen u vremenu $O(m^{1/4+\varepsilon})$.

Ključna je ideja Tonelli–Shanksova algoritma prebaciti računanje diskretnog logaritma u grupu reda $2^e$ i time smanjiti vremensku složenost. Slično, diskretni logaritam u grupi čiji je red bilo koja potencija prostog broja $p^e$ također se može razmjerno učinkovito izračunati, ali složenost algoritma iznosi $\Omega\left(\sqrt{p}\right)$. Adleman–Manders–Millerov algoritam rastavlja računanje $k$-tog korijena na više računanja diskretnih logaritama u grupama reda potencije prostog broja, ali je ograničen veličinom najvećeg prostog faktora $p_\text{max}(k)$ broja $k$, pa složenost algoritma i dalje iznosi $\Omega\left(\sqrt{p_\text{max}(k)}\right)$. Algoritam iz ovog odjeljka dodatno poboljšava taj postupak izbjegavajući računanje diskretnih logaritama za veće proste faktore, čime se ukupna složenost svodi na $O(m^{1/4+\varepsilon})$.

#### Postupak

Razmatramo računanje $k$-tog korijena od $a$ modulo potencija prostog broja $m$, tj. rješavanje kongruencije:

$$
x^k \equiv a \pmod m.
$$

Posebno, za slučaj $m=2^e$ treba još osigurati $a\equiv 1\pmod{4}$, tako da se $a$ može zapisati kao potencija od $g=5$. Slično prethodnoj raspravi, računanje $k$-tog korijena modulo $2^e$ uvijek se može svesti na takav slučaj. Pri obradi slučaja modulo $2^e$ svaki $\varphi(m)$ spomenut u ovom odjeljku treba zamijeniti s $\delta_m(5)=2^{e-2}$.

Najprije, problem se može svesti na slučaj u kojem red korijena dijeli $\varphi(m)$. Neka je $d=\gcd(k,\varphi(m))$. Tada, prema svojstvima $k$-tih ostataka, kad je $a$ $k$-ti ostatak modulo $m$, $a$ je uvijek $\dfrac{\varphi(m)}{d}$-ti korijen jedinice modulo $m$. Prema svojstvima korijena jedinice, za svaki $\ell\perp\dfrac{\varphi(m)}{d}$ preslikavanje $x\mapsto x^{\ell}$ bijekcija je na skupu $\dfrac{\varphi(m)}{d}$-tih korijena jedinice. Stoga možemo uzeti

$$
\ell = \left(\dfrac{k}{d}\right)^{-1}\bmod\dfrac{\varphi(m)}{d}.
$$

Potenciranjem obiju strana polazne kongruencije na $\ell$-tu potenciju dobivamo

$$
x^d\equiv x^{k\ell} \equiv a^{\ell} =: b \pmod{m}.
$$

Krajnja lijeva kongruencija koristi [Eulerov teorem](./fermat.md#欧拉定理) i sljedeću relaciju kongruencije: ($c\in\mathbf Z$)

$$
k\ell = d\left(\frac{k}{d}\ell\right) = d\left(c\dfrac{\varphi(m)}{d}+1\right) \equiv d \pmod{\varphi(m)}.
$$

Za transformirani problem razmotrimo rastav broja $d$ na proste faktore:

$$
d = \prod_{p\in\mathbf P}p^e.
$$

Počevši od $b=a^\ell$, za svaki $p^e\neq 1$ redom vadimo $p^e$-ti korijen, i na kraju dobivamo $d$-ti korijen od $b$, odnosno $k$-ti korijen od $a$.

Konačno, problem se svodi na to kako pronaći rješenje sljedeće jednadžbe:

$$
x^{p^e} \equiv b \pmod m.
$$

Bez smanjenja općenitosti neka je $\varphi(m)=p^sr$ uz $p\perp r$. Neka je $q\in\mathbf N_+$ rješenje jednadžbe $qr\equiv -1\pmod{p^e}$. Tada, budući da je $b$ $rp^{s-e}$-ti korijen jedinice, $b^{qr}$ nužno je $p^{s-e}$-ti korijen jedinice. Neka je nadalje $\zeta$ $p^s$-ti primitivni korijen jedinice modulo $m$. Tada je $\zeta^{p^e}$ $p^{s-e}$-ti primitivni korijen jedinice, pa postoji $h\in\mathbf N$ takav da je $b^{qr}\equiv \zeta^{hp^{e}}\pmod{m}$. Stoga se izravnom provjerom vidi da je

$$
x\equiv b^{(qr+1)/p^e}\zeta^{-h} \pmod{m}
$$

$p^e$-ti korijen od $b$ modulo $m$.

Da bismo izračunali $x$, treba pronaći jedan $p$-ti neostatak $\eta$ modulo $m$. Za to je, prema prethodnim svojstvima, dovoljno nasumično birati $\eta\perp m$ i provjeriti $\eta^{\varphi(m)/p}\bmod{m}\neq 1$. Gustoća takvih brojeva iznosi

$$
\dfrac{\varphi(m)}{m}\left(1-\dfrac{1}{p}\right) \ge \dfrac{1}{4}.
$$

Dakle, očekivano je dovoljno nasumično izabrati najviše $4$ cijela broja da bismo ga pronašli. Uočimo da je $\eta^{rp^{s-1}}\not\equiv 1\pmod m$ i $\eta^{rp^s}\equiv 1\pmod m$, pa ako stavimo $\zeta=\eta^r\bmod m$ i $\xi=\eta^{rp^{s-1}}\bmod m$, oni su redom $p^s$-ti i $p$-ti primitivni korijen jedinice.

Na kraju treba izračunati $h\in\mathbf N$. Očito možemo uzeti $h < p^{s-e}$. Razmotrimo zapis broja $h$ u bazi $p$:

$$
h = \sum_{j=0}^{s-e-1}h_jp^j = h_0 + h_1p + h_2p^2 +\cdots.
$$

Te znamenke računamo jednu po jednu. Kad je prvih $j$ znamenki izračunato, nužno vrijedi

$$
\left(b^{qr}\zeta^{-p^e(h_0+h_1p+\cdots + h_{j-1}p^{j-1})}\right)^{p^{s-e-j-1}} \equiv \zeta^{h_jp^{s-1}} \equiv \xi^{h_j} \pmod{m}.
$$

Stoga se $h_j$ može dobiti računanjem diskretnog logaritma s obzirom na $\xi$. Za bolju vremensku složenost treba koristiti BSGS algoritam. Ukupno treba izračunati $(s-e)$ diskretnih logaritama; ako predračunamo $B$ potencija od $\xi$, vremenska složenost jednog računanja diskretnog logaritma iznosi $O(p/B)$, a ukupna vremenska složenost je

$$
O\left(B+(s-e)\dfrac{p}{B}\right).
$$

Uz $B=\sqrt{(s-e)p}$ ukupna je vremenska složenost najmanja i iznosi $O\left(\sqrt{(s-e)p}\right)$. Nakon što dobijemo $h$, uvrštavanjem u gornji izraz za $x$ pronalazimo jedno partikularno rješenje.

#### Vremenska složenost

Vremenska složenost ovog algoritma iznosi $O(m^{1/4+\varepsilon})$. Pri razmatranju složenosti u ovom odjeljku uvijek pretpostavljamo da jedno množenje traje $O(1)$ i da se pri računanju potencija uvijek primjenjuje Eulerov teorem za smanjenje eksponenta, pa se svaka pojedina potencija može izračunati u vremenu $O(\log m)$.

Razmotrimo najprije računanje jednog $p^e$-tog korijena. Za pronalaženje $p$-tog neostatka treba provjeriti očekivano $O(1)$ brojeva, pa je ukupna vremenska složenost $O(\log m)$. Računanje svakog od $s,r,\zeta,\eta,b^{qr}$ traje $O(\log m)$. Pri računanju $h$ za svaku znamenku treba $O(\log m)$ vremena za računanje potencija, a znamenki je ukupno $(s-e)$, pa je ukupna vremenska složenost $O((s-e)\log m)$. Već je objašnjeno da predobrada i $(s-e)$ upita u dijelu s računanjem diskretnih logaritama ukupno traju $O\left(\sqrt{(s-e)p}\right)$. Budući da je $s-e\in O(\log m)$, vremenska složenost računanja jednog $p^e$-tog korijena iznosi $O(p^{1/2+\varepsilon})$. Posebno, kad je $s=e$, vremenska se složenost dodatno smanjuje na $O(\log m)$.

Sada možemo razmotriti ukupnu vremensku složenost algoritma. Vremenska složenost računanja $\varphi(m),d,\ell$ iznosi $O(\log m)$ za svaki. Zatim treba napraviti rastav na proste faktore $d=\prod_p{p^e}$; taj se korak pomoću [Pollardova rho algoritma](./pollard-rho.md#pollard-rho-算法) može obaviti u vremenu $O(m^{1/4})$. Konačno, ukupna vremenska složenost uzastopnog računanja $p^e$-tih korijena iznosi

$$
O\left(\sum_{e < s}p^{1/2+\varepsilon}\right).
$$

Budući da se prosti faktor $p$ koji zadovoljava $e < s$ u $\varphi(m)$ pojavljuje barem $2$ puta, nužno je $p < m^{1/2}$. Stoga je ukupna vremenska složenost $O(m^{1/4+\varepsilon})$.

Zapravo, u ovoj situaciji nije nužno koristiti Pollardov rho algoritam za rastav na proste faktore, a vremenska složenost $O(m^{1/4+\varepsilon})$ i dalje se može postići. Konkretno, dovoljno je $d$ rastaviti grubom silom pokusnim dijeljenjem i pritom ispitivati samo proste faktore koji ne premašuju $m^{1/4}$. Neka je $z$ cijeli broj koji ostaje nakon uklanjanja tih malih prostih faktora. Tada za prosti faktor $p > m^{1/4}$ broja $z$ nužno vrijedi $\nu_p(\varphi(m)) < 4$, gdje $\nu_p(n)$ označava eksponent od $p$ u rastavu broja $n$ na proste faktore. Budući da treba razmatrati samo slučaj

$$
1 \le e = \nu_p(d) < s = \nu_p(\varphi(m)) < 4
$$

prostih faktora $p$ koji zadovoljavaju taj uvjet može biti najviše jedan; inače bi njihovi eksponenti u $\varphi(m)$ svi bili barem $2$, pa bi ukupni umnožak nužno premašio $m$. Da bismo izdvojili taj (moguće postojeći) jedinstveni veliki prosti faktor, dovoljno je izračunati

$$
p^\star=\gcd\left(z,\dfrac{\varphi(m)}{z}\right) = \prod_{p\mid z,~\nu_p(d) < \nu_p(\varphi(m))}p^{\min\{\nu_p(d),\nu_p(\varphi(m))-\nu_p(d)\}}.
$$

Ispitivanjem svih mogućnosti za $\nu_p(d),\nu_p(\varphi(m))$ vidi se da je eksponent od $p$ u tom umnošku nužno $1$, pa je tako izračunata vrijednost upravo jedinstveni veliki prosti faktor $p^\star$ (ako postoji). Što se tiče preostalog dijela $z/p^\star$, budući da on može sadržavati samo proste faktore koji zadovoljavaju $e=s$, nije ga potrebno dalje rastavljati.

Referentna implementacija računanja $k$-tog korijena modulo prost broj glasi:

??? example "Referentna implementacija za ogledni zadatak [Library Checker - Kth Root (Mod)](https://judge.yosupo.jp/problem/kth_root_mod)"
    ```cpp
    --8<-- "docs/math/code/residue/tonelli-shanks-mod-p.cpp"
    ```

### Obrada općeg slučaja

Razmotrimo opći slučaj: modul $m$ i dalje je potencija prostog broja $p^e$, ali je $\gcd(a,m)>1$. Ako je $a\equiv 0\pmod{m}$, tada su

$$
x \equiv p^{\lceil e/k \rceil}\ell\pmod{p^e},~\ell=0,1,\cdots,p^{e-\lceil e/k\rceil}-1
$$

sva rješenja polazne jednadžbe. Razmotrimo sada slučaj $a\not\equiv 0\pmod{m}$. Neka je $a = p^sa'$ uz $p\perp a'$. Stavimo li $x=p^zx'$ uz $p\perp x'$, imamo

$$
x^k = p^{kz}(x')^k\equiv p^sa'\pmod{p^e}.
$$

Budući da je $(x')^k\perp p$, ta jednakost vrijedi ako i samo ako je $kz = s$ i $(x')^k\equiv a'\pmod{p^{e-s}}$. Prva jednadžba ima rješenje $z=\dfrac{s}{k}$ ako i samo ako $k\mid s$; a rješavanje druge jednadžbe već je riješeno. Treba pripaziti da se modul općeg rješenja druge jednadžbe razlikuje od modula općeg rješenja polazne jednadžbe, pa svakom rješenju $x'$ druge jednadžbe odgovara više rješenja polazne jednadžbe:

$$
x \equiv p^{s/k}(x' + \ell p^{e-s})\pmod{p^e},~\ell = 0,1,\cdots, p^{s-s/k}-1.
$$

Referentna implementacija pronalaženja svih $k$-tih korijena modulo proizvoljan modul glasi:

??? example "Referentni kôd za ogledni zadatak [Luogu P5668【模板】N 次剩余 (Predložak: N-ti ostatak)](https://www.luogu.com.cn/problem/P5668)"
    === "Naivni algoritam"
        ```cpp
        --8<-- "docs/math/code/residue/bsgs.cpp"
        ```
    
    === "Poboljšani Tonelli–Shanksov algoritam"
        ```cpp
        --8<-- "docs/math/code/residue/tonelli-shanks.cpp"
        ```

## Literatura i napomene

-   冯克勤．初等数论及其应用．(Feng Keqin. Elementarna teorija brojeva i njezine primjene.)
-   [Root of unity modulo n - Wikipedia](https://en.wikipedia.org/wiki/Root_of_unity_modulo_n)
-   [No.981 一般冪乗根 解説 by 37zigen (Opći korijeni potencija, objašnjenje)](https://yukicoder.me/problems/no/981/editorial)

[^fnnt]: Zapravo, modul $m$ ne mora biti prost. Čim je $a$ $k=2^e$-ti primitivni korijen jedinice modulo $m$, može se koristiti za brzu teorijsko-brojevnu transformaciju modulo $m$. Međutim, budući da je $2^e$ koji obično treba obraditi razmjerno velik, to znači da je svaki prosti faktor modula $m$ oblika $c2^e+1$. Stoga je već pojedini prosti faktor velik, a modul $m$ obično je još veći, pa se slučaj općeg modula ne koristi tako često kao slučaj prostog modula.

[^lambda-density]: Prema [rezultatu o broju primitivnih korijena](./primitive-root.md#原根个数), broj $\lambda$‑primitivnih korijena točno je $\varphi(\lambda(m))$, gdje su $\varphi(\cdot)$ i $\lambda(\cdot)$ redom Eulerova funkcija i Carmichaelova funkcija. Budući da za gotovo sve cijele brojeve $m$ vrijedi $\lambda(m)/m = \exp(-(1+o(1))\log\log m\log\log\log m)$, a postoji $C > 0$ takav da za cijele brojeve $m > 2$ vrijedi $\varphi(m)/m \ge C / \log\log m$, za gotovo sve cijele brojeve $m$ vrijedi $\varphi(\lambda(m))/m = \exp(-(1+o(1))\log\log m\log\log\log m)$. Pritom $o(1)$ u koeficijentu eksponenta apsorbira doprinos faktora $\varphi(\lambda(m))/\lambda(m)$. Stoga se $\lambda$‑primitivni korijen može pronaći u očekivano $\exp((1+o(1))\log\log m\log\log\log m)$ pokušaja. Za ocjenu Eulerove funkcije vidi rad Rosser, J. Barkley, and Lowell Schoenfeld. "Approximate formulas for some functions of prime numbers." Illinois Journal of Mathematics 6, no. 1 (1962): 64-94. Za ocjenu Carmichaelove funkcije vidi rad Erdos, Paul, Carl Pomerance, and Eric Schmutz. "Carmichael’s lambda function." Acta Arith 58, no. 4 (1991): 363-385.

[^amm]: Izvorni rad: Adleman, Leonard, Kenneth Manders, and Gary Miller. "On taking roots in finite fields." In 18th Annual Symposium on Foundations of Computer Science (sfcs 1977), pp. 175-178. IEEE Computer Society, 1977. Čitljiviji uvod može se naći u Cao, Zhengjun, Qian Sha, and Xiao Fan. "Adleman-Manders-Miller root extraction method revisited." In International Conference on Information Security and Cryptology, pp. 77-85. Berlin, Heidelberg: Springer Berlin Heidelberg, 2011.

[^amm-comp]: Budući da taj algoritam zahtijeva da $k$ bude prost, u najgorem slučaju treba za najveći prosti faktor $p$ broja $\varphi(m)$ izračunati $p$-ti korijen od $a$ modulo $m$. Pritom treba izračunati diskretni logaritam od $a$ modulo $m$ s obzirom na $p$-ti primitivni korijen jedinice. Čak i uz primjenu BSGS algoritma taj postupak traje $O(\sqrt{p})$. Međutim, rad Fouvry, Étienne. "Theoreme de Brun-Titchmarsh; application au theoreme de Fermat." Inventiones mathematicae 79, no. 2 (1985): 383-407 pokazuje da postoji skup prostih brojeva $m$ pozitivne gustoće za koje je najveći prosti faktor od $\varphi(m)=m-1$ jednak $p=\Omega(m^{2/3})$. To znači da je složenost tog algoritma barem $\Omega(m^{1/3})$, što je lošije od poboljšanog Tonelli–Shanksova algoritma opisanog u tekstu.
