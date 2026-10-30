---
title: Uvod u modularnu aritmetiku
---

U algoritamskim natjecanjima važan dio teorije brojeva čini **modularna aritmetika** (modular arithmetic), tj. izvođenje raznih cjelobrojnih operacija pri nekom modulu. Osim osnovnih četiriju računskih operacija i potenciranja, u njoj se mogu zgodno računati i logaritmi, korijeni raznih redova, faktorijeli, binomni koeficijenti i druge operacije.

Modularna aritmetika česta je u raznim vrstama zadataka, a ne samo u dijelu o teoriji brojeva. Stvarni odgovor mnogih zadataka može biti vrlo velik i premašiti raspon uobičajenih cjelobrojnih tipova. Tada, kako bi se izbjeglo uvođenje aritmetike velikih brojeva i ispis dugačkih brojeva, zadatak često traži da se ispiše odgovor modulo neki broj. To zahtijeva dobro vladanje raznim tehnikama modularne aritmetike.

## Cjelobrojno dijeljenje i operacija modulo u C/C++-u

U C/C++-u cjelobrojno dijeljenje i operacija modulo ne poklapaju se s dijeljenjem i modulom uobičajenima u matematici.

Za sve standardne verzije C/C++-a propisano je da u cjelobrojnom dijeljenju:

1.  kad je djelitelj 0, ponašanje je nedefinirano;
2.  inače je rezultat izraza `(a / b) * b + a % b` jednak `a`.

Drugim riječima, predznak rezultata operacije modulo ovisi o tome kako se zaokružuje pri dijeljenju, a način zaokruživanja pri dijeljenju definiran je implementacijom (odlučuje prevoditelj).

Od verzija standarda [C99](https://en.cppreference.com/w/c/language/operator_arithmetic) i [C++11](https://en.cppreference.com/w/cpp/language/operator_arithmetic) propisano je da se **kvocijent zaokružuje prema nuli** (odbacuje se razlomljeni dio); predznak modula tada je jednak predznaku djeljenika. Otada su sljedeće tvrdnje zajamčeno istinite:

```c
assert(5 % 3 == 2);
assert(5 % -3 == 2);
assert(-5 % 3 == -2);
assert(-5 % -3 == -2);
```

## Klasa modularnih cijelih brojeva

Modularna aritmetika može se promatrati kao izvođenje raznih operacija nad [klasama kongruencije](./basic.md#klase-kongruencije-i-sustavi-ostataka) pri nekom modulu. Ako se klasa kongruencije predstavi strukturom, a zbrajanje, oduzimanje, množenje i druge operacije među klasama kongruencije enkapsuliraju kao metode strukture ili preopterećeni operatori, modularna aritmetika prirodno se može implementirati kao klasa modularnih cijelih brojeva. U nastavku je jednostavan primjer koji podržava zbrajanje, oduzimanje, množenje i brzo potenciranje $32$-bitnih predznačenih cijelih brojeva pri modulu $M < 2^{30}$:

???+ example "Jednostavna klasa modularnih cijelih brojeva"
    ```cpp
    --8<-- "docs/math/code/mod-arithmetic/mod-arithmetic.cpp:core"
    ```

Ova implementacija namjerno smanjuje broj operacija modulo jer je operacija modulo obično znatno skuplja od običnog zbrajanja, oduzimanja, množenja ili usporedbe. U komentarima koda dane su ekvivalentne i izravnije implementacije. Glavna je ideja tih jednostavnih optimizacija da pri zbrajanju ili oduzimanju dvaju cijelih brojeva iz $[0,M)$ rezultat sigurno pada u interval $(-M,2M)$, pa se jednim zbrajanjem ili oduzimanjem može vratiti u interval $[0,M)$. Potenciranje u ovoj implementaciji koristi tehniku [brzog potenciranja](../binary-exponentiation.md#模意义下取幂).

Osim tih osnovnih operacija, pri raznim modulima mogu se izvoditi i sljedeće operacije:

-   [inverz](./inverse.md)
-   [dijeljenje](./linear-equation.md)
-   [faktorijel](./factorial.md)
-   [binomni koeficijenti](./lucas.md)
-   [kvadratni korijen](./quad-residue.md#模意义下开平方)
-   [logaritam](./discrete-logarithm.md)
-   [korijen](./residue.md#模意义下开方)

Te su operacije obično lakše pri prostom modulu. Za složeni modul često su potrebne proširene verzije odgovarajućih algoritama i [kineski teorem o ostatcima](./crt.md). Većina tih operacija u modularnom smislu može se promatrati kao rješavanje neke vrste kongruencije. Za opće metode rješavanja kongruencija može se pogledati stranica [Kongruencije](./congruence-equation.md).

## Srodni algoritmi

U ovom odjeljku predstavljamo nekoliko metoda za optimiranje operacija modulo, množenja i brzog potenciranja u modularnom smislu. Za veliku većinu zadataka jednostavna implementacija iz prethodnog teksta dovoljno je učinkovita. Međutim, kad zadatak postavlja stroge zahtjeve na konstantu algoritma, te optimizacije mogu doći do izražaja: smanjenjem nepotrebnih izračuna i operacija modulo dodatno snižavaju vremenski trošak algoritma.

### Brzo množenje

Pri testiranju prostosti i faktorizaciji na proste faktore često se susreće množenje modulo modul u rasponu `long long`. Da bi se izbjegao problem cjelobrojnog prekoračenja u računu, u ovom odjeljku predstavljamo „brzo množenje” koje radi s modulom u rasponu `long long`, ne treba `__int128` i ima složenost $O(1)$. Ovaj algoritam zahtijeva da na sustavu za ocjenjivanje `long double` bude predstavljen barem kao $80$-bitni broj s pomičnim zarezom proširene preciznosti[^long-double-80bit].

Pretpostavimo da je $0 \le a, b < m$ i da treba izračunati $ab\bmod m$. Primijetimo:

$$
ab\bmod m=ab-\left\lfloor \dfrac{ab}m \right\rfloor m.
$$

Iskoristimo prirodno prekoračenje tipa `unsigned long long`:

$$
ab\bmod m=ab-\left\lfloor \dfrac{ab}m \right\rfloor m=\left(ab-\left\lfloor \dfrac{ab}m \right\rfloor m\right)\bmod 2^{64}.
$$

Čim možemo izračunati kvocijent $\left\lfloor\dfrac{ab}m\right\rfloor$, množenje i oduzimanje u krajnje desnom izrazu mogu se izravno izračunati u `unsigned long long`.

Dalje treba razmotriti samo kako izračunati $\left\lfloor\dfrac {ab}m\right\rfloor$. Rješenje je da se najprije u `long double` izračuna $\dfrac am$ pa pomnoži s $b$. Budući da koristimo `long double`, neizbježno dolazi do pogreške u preciznosti. Pretpostavimo da je `long double` predstavljen kao $80$-bitni broj s pomičnim zarezom proširene preciznosti (tj. predznak ima $1$ bit, eksponent $15$ bitova, a mantisa $64$ bita); tada `long double` može točno predstaviti najviše $64$ značajna bita[^floating-format]. Stoga $\dfrac am$ u najgorem slučaju griješi počevši od $65$. bita, a raspon pogreške[^ld-mul-err] je $\left(-2^{-64},2^{-64}\right)$. Nakon množenja s $b$, $64$-bitnim predznačenim cijelim brojem, raspon pogreške je $(-0.5,0.5)$. Radi pojednostavljenja daljnje rasprave možemo najprije dodati $0.5$ pa zaokružiti na cijeli broj; konačni raspon pogreške je $\{0,1\}$.

Naposljetku, pri uvrštavanju u gornju formulu treba pomnožiti s $-m$, pa je konačni raspon pogreške $\{0,-m\}$. Budući da je $m$ u rasponu `long long`, kad je rezultat $r\in[0,m)$, izravno vraćamo $r$, a inače vraćamo $r+m$.

Implementacija u kodu izgleda ovako:

???+ example "Referentna implementacija"
    ```cpp
    --8<-- "docs/math/code/mod-arithmetic/i64-mul.cpp:ld-mul"
    ```

Danas prevoditelji za C/C++ na velikoj većini sustava za ocjenjivanje već podržavaju tip `__int128`[^int128], pa se tip množitelja može i izravno proširiti na `__int128` i zatim računati modulo:

???+ example "Referentna implementacija"
    ```cpp
    --8<-- "docs/math/code/mod-arithmetic/i64-mul.cpp:i128-mul"
    ```

Dakako, operacija modulo nad `__int128` nije jeftina. Ako treba dodatno optimirati konstantu, mogu se razmotriti metode predstavljene u sljedeća dva odjeljka.

### Barrettova redukcija

Već je spomenuto da su dijeljenje i operacija modulo obično skuplji od ostalih osnovnih računskih operacija. Kako bi se smanjio trošak operacija modulo, postoje algoritmi koji daju isti rezultat bez izravnog računanja modula. Algoritam Barrettove redukcije (Barrett reduction) koji predstavljamo u ovom odjeljku jedan je od njih.

Neka je $m$ fiksni modul i pretpostavimo da za razne $a > 0$ treba više puta izračunati $a\bmod m$. Iz dijeljenja s ostatkom znamo

$$
z = a\bmod m = a - \left\lfloor\dfrac{a}{m}\right\rfloor m.
$$

Ključ je u izračunu kvocijenta $\left\lfloor\dfrac{a}{m}\right\rfloor$. Neka je $R$ neka konstanta; tada vrijedi[^floor-barrett]

$$
\left\lfloor\dfrac{a}{m}\right\rfloor = \left\lfloor a\dfrac{R}{m} / R\right\rfloor \approx \left\lfloor a\left\lfloor\dfrac{R}{m}\right\rfloor/R\right\rfloor.
$$

Ako odaberemo $R = 2^k$, tada se $\left\lfloor\dfrac{R}{m}\right\rfloor$ u desnom izrazu može unaprijed izračunati, a dijeljenje s $R$ može se obaviti posmakom. Stoga izračun kvocijenta desnim izrazom zahtijeva samo jedno množenje i jedan posmak. Uvrštavanjem u izraz za $a\bmod m$ dobivamo procjenu $z'$ traženog ostatka.

Sada analizirajmo pogrešku takvog postupka. [Funkcije pod i strop](./basic.md#funkcije-pod-i-strop) imaju svojstvo: za $x > y > 0$ vrijedi $\lfloor x\rfloor - \lfloor y\rfloor \le \lceil x - y\rceil$. Stoga je pogreška

$$
\begin{aligned}
\Delta &= |z' - z| = m\left|\left\lfloor\dfrac{a}{m}\right\rfloor - \left\lfloor a\left\lfloor\dfrac{R}{m}\right\rfloor/R\right\rfloor\right|\\
&\le m\left\lceil a\left(\dfrac{R}{m} - \left\lfloor\dfrac{R}{m}\right\rfloor\right) /R\right\rceil \le m\left\lceil\dfrac{a}{R}\right\rceil.
\end{aligned}
$$

Čim je $a \le R$, pogreška $\Delta$ ne premašuje $m$. Budući da je $z' \ge z$, procjena $z'$ može biti samo $z$ ili $z + m$. Dovoljno je nakon dobivanja procjene, kad je $z' \ge m$, oduzeti suvišni $m$ i odgovor je zajamčeno točan.

U postupku Barrettove redukcije cjelobrojni modul računa se samo s dva množenja, jednim posmakom i najviše dva oduzimanja. No povećanje učinkovitosti nije besplatno: zapravo su međuvarijable u Barrettovoj redukciji često dulje od ulaznih varijabli. Lako se vidi da je najdulja međuvarijabla u Barrettovoj redukciji $a\left\lfloor\dfrac{R}{m}\right\rfloor$. Neka $\ell(x)$ označava duljinu binarnog zapisa cijelog broja $x$. Tada vrijedi

$$
\ell\left(a\left\lfloor\dfrac{R}{m}\right\rfloor\right) \approx \ell(a) + \ell(R) - \ell(m).
$$

Budući da izbor $R$ mora zadovoljavati uvjet $a \le R$, ta je duljina barem $2\ell(a) - \ell(m)$. No kad je potrebno računati modulo, obično je $\ell(m)\le\ell(a)$, pa duljina te međuvarijable može biti veća od ulazne duljine $\ell(a)$. Na primjer, ako treba $64$-bitni cijeli broj računati modulo $32$-bitni cijeli broj, međuvarijabla zapravo treba $64 \times 2 - 32 = 96$-bitni cijeli broj.

Jedna od primjena Barrettove redukcije jest izračun ostatka umnoška $ab\bmod m$. Ako je jedan od množitelja fiksan, recimo $b$, tada se pomoću

$$
ab\bmod m = ab - \left\lfloor a\left\lfloor\dfrac{bR}{m}\right\rfloor/R\right\rfloor m
$$

može napraviti procjena slična gornjoj; dovoljno je unaprijed izračunati vrijednost $\left\lfloor\dfrac{bR}{m}\right\rfloor$. Ovaj slučaj s fiksnim $b$ ponekad se naziva i Shoupovo množenje[^shoup].

Češći je slučaj kad $a, b$ nisu fiksni. Tada treba najprije izračunati vrijednost $ab$, a zatim Barrettovom redukcijom dobiti $ab\bmod m$. Na primjer, pri implementaciji množenja u modularnom smislu treba za $0 \le a,b < m$ izračunati $ab\bmod m$. Tada odabrani $R$ mora zadovoljavati $ab \le R$. Prema prethodnoj analizi, najdulja međuvarijabla u izračunu ima duljinu $2\ell(ab)-\ell(m)$. Kad je $\ell(a)\approx\ell(b)\approx\ell(m)$, ta duljina iznosi $3\ell(m)$. Drugim riječima, ako se Barrettovom redukcijom želi implementirati modularno množenje $32$-bitnih cijelih brojeva, međuvarijable trebaju $96$-bitne cijele brojeve. To je jedno od ograničenja praktične primjene Barrettove redukcije u algoritamskim natjecanjima.

Kao primjer, referentna implementacija modularnog množenja $32$-bitnih predznačenih cijelih brojeva Barrettovom redukcijom izgleda ovako:

???+ example "Referentna implementacija"
    ```cpp
    --8<-- "docs/math/code/mod-arithmetic/i32-mul.cpp:barrett"
    ```

U implementaciji su potrebni $128$-bitni cijeli brojevi[^int128].

### Montgomeryjevo množenje

Algoritam Montgomeryjeva množenja (Montgomery multiplication) po funkciji je vrlo sličan Barrettovu algoritmu: i on može smanjiti trošak operacija modulo pri računanju s modularnim cijelim brojevima. Za razliku od prethodna dva algoritma, koji približno računaju kvocijent, Montgomeryjevo množenje preslikava sve cijele brojeve u Montgomeryjev prostor, u kojem su operacije razmjerno jednostavne, čime se snižava ukupni trošak računanja.

Neka je modul $m$ neparan i odaberimo $R = 2^k > m$. Tada je Montgomeryjev oblik koji odgovara klasi kongruencije $a \bmod m$

$$
aR\bmod m.
$$

Budući da je $R\perp m$, između klase kongruencije $a \bmod m$ i njezina Montgomeryjeva oblika $aR\bmod m$ postoji bijekcija. Stoga se cijeli brojevi mogu pretvoriti u Montgomeryjev oblik, zatim se izvede niz operacija modulo $m$, a dobiveni se Montgomeryjev oblik pretvori natrag u cijeli broj; rezultat je uvijek točan.

Montgomeryjev oblik omogućuje zgodno izvođenje mnogih operacija s modularnim cijelim brojevima. Upravo smo objasnili da je za usporedbu dviju klasa kongruencije dovoljno usporediti njihove Montgomeryjeve oblike. Nadalje, budući da je

$$
(a\pm b)R\bmod m = ((aR\bmod m)\pm(bR\bmod m)) \bmod{m},
$$

zbrajanje i oduzimanje klasa kongruencije odgovara zbrajanju i oduzimanju njihovih Montgomeryjevih oblika. Međutim, za množenje klasa kongruencije ne mogu se izravno pomnožiti dva Montgomeryjeva oblika. Budući da je

$$
(ab)R\bmod m =  ((aR\bmod m)(bR\bmod m)R^{-1}) \bmod{m},
$$

pri množenju dvaju Montgomeryjevih oblika nad njihovim umnoškom $x$ treba izvesti sljedeću operaciju **Montgomeryjeve redukcije** (Montgomery reduction):

$$
\operatorname{REDC}: x \mapsto xR^{-1}\bmod m.
$$

Pomoću te operacije Montgomeryjev oblik umnoška $ab$ jest $\operatorname{REDC}((aR\bmod m)(bR\bmod m))$. Montgomeryjeva redukcija središnja je operacija Montgomeryjeva množenja:

-   Pretvorba $a$ u njegov Montgomeryjev oblik jest $\operatorname{REDC}((a\bmod m)(R^2\bmod m))$.
-   Pretvorba Montgomeryjeva oblika od $a$ natrag u $a\bmod m$ jest $\operatorname{REDC}(aR\bmod m)$.
-   Montgomeryjev oblik koji odgovara modularnom inverzu $a^{-1}\bmod m$ jest $\operatorname{REDC}((aR\bmod m)^{-1}(R^3\bmod m))$.

Sada raspravimo kako implementirati operaciju Montgomeryjeve redukcije $\operatorname{REDC}$. Pri izračunu $\operatorname{REDC}(x)$ uvijek pretpostavljamo $0 \le x < m^2$, što vrijedi u svim gornjim slučajevima. Budući da je $R\perp m$, prema [Bézoutovu teoremu](./bezouts.md) postoje cijeli brojevi $R^{-1},m'$ takvi da je

$$
RR^{-1} + mm' = 1.
$$

Stoga, uz $q=\lfloor xm' / R\rfloor$, vrijedi

$$
\begin{aligned}
xR^{-1} &= x\dfrac{1 - mm'}{R} \equiv \dfrac{x-xmm' + qmR}{R} = \dfrac{x - m(xm'\bmod R)}{R} \pmod{m}.
\end{aligned}
$$

Budući da je $0 \le x < m^2 < mR$ i $0 \le xm'\bmod R < R$, vrijedi

$$
-m < \dfrac{x - m(xm'\bmod R)}{R} < m.
$$

Drugim riječima, taj se kvocijent od $xR^{-1}\bmod m$ razlikuje za najviše jedan $m$. Dovoljno je, kad je kvocijent manji od nule, dodati $m$ i dobiva se $\operatorname{REDC}(x)$. Za izračun tog kvocijenta potrebna su samo dva cjelobrojna množenja, jedno cjelobrojno oduzimanje i dvije bitovne operacije (redom modulo $R=2^k$ i dijeljenje s njim). Stoga se Montgomeryjeva redukcija može izvesti učinkovito.

Za izvođenje Montgomeryjeva množenja potrebno je unaprijed izračunati niz konstanti. Prvo, u Montgomeryjevoj redukciji koristi se $m' = m^{-1}\bmod R$, koji se može izračunati Newton–Henselovom metodom predstavljenom [u nastavku](#klasa-cijelih-brojeva-modulo-potencija-broja-2). Drugo, pri svođenju raznih operacija na Montgomeryjevu redukciju pojavljuju se i konstante poput $R^2\bmod m$. Da bismo je dobili, treba jednom izračunati $R\bmod m$, a zbrajanjem sa samim sobom dobiva se $2R\bmod m$. Zatim, promatrajući to kao Montgomeryjev oblik broja $2$ i izravno primjenjujući brzo potenciranje, dobiva se $2^kR\bmod m = R^2\bmod m$.

Kao primjer, implementacija Montgomeryjeva množenja $32$-bitnih predznačenih cijelih brojeva izgleda ovako:

???+ example "Referentna implementacija"
    ```cpp
    --8<-- "docs/math/code/mod-arithmetic/i32-mul.cpp:montgomery"
    ```

U usporedbi s implementacijom modularnog množenja Barrettovom redukcijom, izračun Montgomeryjevim množenjem uključuje više koraka: pretvorbu, množenje Montgomeryjevih oblika, inverznu pretvorbu itd. Stoga se trošak pretvorbe i inverzne pretvorbe može amortizirati, a time postići visoka ukupna učinkovitost, samo kad je broj modularnih operacija između pretvorbe i inverzne pretvorbe dovoljno velik. Međutim, budući da implementacija Montgomeryjeva množenja uključuje samo međuvarijable duljine $2\ell(m)$, implementacija je fleksibilnija. Na primjer, modularno množenje $32$-bitnih cijelih brojeva treba samo $64$-bitne međuvarijable. Stoga, ako treba implementirati klasu modularnih cijelih brojeva za razne teorijsko-brojevne izračune, Montgomeryjevo množenje prikladnije je.

### Klasa cijelih brojeva modulo potencija broja 2

U ovom odjeljku raspravljamo o implementaciji klase modularnih cijelih brojeva kad je modul potencija broja $2$. U tom posebnom slučaju dijeljenje i operacija modulo mogu se izvesti bitovnim operacijama, pa je računanje vrlo učinkovito. I Barrettova redukcija i Montgomeryjevo množenje iskorištavaju to svojstvo $2^e$ kao djelitelja i modula kako bi ubrzali račun. Posebno, kad je modul upravo neki od posebnih brojeva poput $2^{32}$ i $2^{64}$, klasa modularnih cijelih brojeva može se implementirati pomoću nepredznačenih cijelih brojeva odgovarajuće duljine i prirodnog prekoračenja, bez ikakve eksplicitne operacije modulo. Čak i kad modul nije točno takav, može se svesti na slučaj tih posebnih modula. Na primjer, kad je modul $2^{58}$, međuizračuni se mogu obaviti modulo $2^{64}$, a na kraju se rezultat uzme modulo $2^{58}$. Osim što je operacija modulo jednostavna, i druge operacije klase cijelih brojeva modulo $2^e$ imaju mnoge posebne implementacije. U ovom se odjeljku usredotočujemo na implementaciju inverza i potenciranja.

Prvo inverz: za zadani neparni $a$ i modul $m=2^e~(e > 2)$ treba naći $a^{-1}\bmod m$. Uobičajene metode za inverz uključuju prošireni Euklidov algoritam i metodu brzog potenciranja. Postupak proširenog Euklidova algoritma uključuje računanje modulo opći modul; obična metoda brzog potenciranja treba izračunati $a^{\varphi(m)-1}\bmod{m}$, što zahtijeva $\Theta(e)$ cjelobrojnih množenja. Učinkovitija je [Newton–Henselova metoda](../poly/newton.md). Konkretno, razmotrimo primjenu sljedećeg rezultata:[^newton-hensel]

$$
ax \equiv 1 \pmod{2^e} \implies ax(2 - ax) \equiv 1\pmod{2^{2e}}.
$$

Prema tom izrazu, dovoljno je krenuti od $x = 1$ i uzastopno primjenjivati $x \gets x(2-ax)$; nakon $\lceil\log_2 e\rceil$ iteracija dobiva se $a^{-1}\bmod m$.

Kao primjer, referentna implementacija inverza cijelih brojeva modulo $2^{32}$ izgleda ovako:

???+ example "Referentna implementacija"
    ```cpp
    --8<-- "docs/math/code/mod-arithmetic/mod-32-inv-pow.cpp:inv"
    ```

Zatim potenciranje: za zadane $x,a,b$ i modul $m=2^e~(e > 2)$ treba naći $xa^b\bmod m$, pri čemu je $a$ neparan. Prema [analizi](./primitive-root.md#递推公式) strukture množenja cijelih brojeva modulo $2^e$ znamo da se $a$ uvijek može zapisati u obliku $\pm g^{\ell}$[^mod-2-g], pri čemu se negativni predznak pojavljuje točno onda kad je $a\equiv 3\pmod 4$. U tom se slučaju $a$ može zamijeniti s $-a$, a konačni rezultat pomnožiti s $(-1)^b$. Stoga u nastavku bez smanjenja općenitosti pretpostavljamo da vrijedi $a\equiv 1\pmod 4$. Tada je središnja ideja algoritma zapisati $a$ u obliku $g^{L(a)}\bmod m$ i zatim traženu potenciju izračunati kao $xg^{bL(a)}\bmod m$.

Izračunati $L(a)$ znači izračunati diskretni logaritam $\operatorname{ind}_ga$. Primijetimo da se, čim je $a\equiv 1\pmod 4$, $a$ uvijek može zapisati u sljedećem obliku:

$$
a \equiv (2^{e_1}+1)(2^{e_2}+1)\cdots(2^{e_s}+1) \pmod{m},
$$

gdje je $1 < e_1 < e_2 < \cdots < e_s < e$. Naime, izravnim razvojem tog umnoška vidi se da je drugi najniži bit binarnog zapisa od $a$ koji je jednak $1$ upravo $e_1$. bit (indeksi počinju od $0$), pa se taj zapis može naći rekurzivno. Prema [svojstvima](./discrete-logarithm.md#性质) diskretnog logaritma vrijedi

$$
4L(a) \equiv 4L(2^{e_1}+1) + 4L(2^{e_2}+1) + \cdots + 4L(2^{e_s}+1) \pmod{m}. 
$$

Budući da je modul diskretnog logaritma jednak redu $\delta_m(g)=2^{e-2}=m/4$, ovdje smo cijelu kongruenciju izravno pomnožili s $4$ kako bi se račun mogao provoditi u klasama ostataka modulo $m$. Stoga je dovoljno za $1 < d < e$ unaprijed izračunati sve $4L(2^d+1)$ i vrijednost $4L(a)$ može se brzo izračunati.

Obratno, iz $L(a)$ lako se dobiva vrijednost $g^{L(a)}\bmod{m}$. Prema [binomnom teoremu](../combinatorics/combination.md#二项式定理) za $1 < d < e$ vrijedi

$$
\begin{aligned}
(2^d+1)^{2^{e-d}} \equiv 1 \pmod{m},\quad
(2^d+1)^{2^{e-d-1}} \equiv 1 + 2^{e-1} \pmod{m},
\end{aligned}
$$

pa je $\delta_m(2^d+1) = 2^{e-d}$. Prema svojstvima reda vrijedi

$$
\delta_m(2^d+1) = \dfrac{\delta_m(g)}{\gcd(\delta_m(g), \operatorname{ind}_g(2^d+1))}.
$$

Stoga je $\gcd(\delta_m(g), \operatorname{ind}_g(2^d+1)) = 2^{d-2}$. To pokazuje da je $L(2^d+1) = \operatorname{ind}_g(2^d+1) = 2^{d-2}r$, gdje je $2\nmid r$. Dakle, najniži bit binarnog zapisa od $4L(2^d+1)$ koji je jednak $1$ upravo je $d$. bit (indeksi počinju od $0$). Stoga se i $4L(a)$ može rekurzivno, preko binarnog zapisa, rastaviti na zbroj članova oblika $4L(2^d+1)$. Odatle se dobiva vrijednost $a$.

U konkretnoj implementaciji postoji nekoliko točaka koje se mogu dodatno optimirati. Prvo, pri rastavljanju $a$ u oblik umnoška i dalje je potrebno dijeljenje. Zgodnije je računati rastav od $a^{-1}$, tj. tražiti $1 < e_1 < e_2 < \cdots < e_s < e$ takve da vrijedi

$$
a(2^{e_1}+1)(2^{e_2}+1)\cdots(2^{e_s}+1) \equiv 1 \pmod{m}
$$

I ovdje se $e_1$ određuje traženjem drugog najnižeg bita jednakog $1$, ali da bi se u $a^{-1}$ poništio faktor $2^{e_1}+1$, dovoljno je $a$ pomnožiti s $2^{e_1}+1$, što se može obaviti bitovnim operacijama. Nadalje, budući da je $4L(a^{-1})=-4L(a)$, pri zbrajanju $4L(a)$ treba umjesto zbrajanja koristiti oduzimanje. Drugo, za posebno odabranu bazu $g$ iteracija ne mora ići do $d = e-1$, nego je dovoljno ići do $d = \lceil e/2\rceil - 1$. Za to treba odabrati $g$ tako da je

$$
4L(2^{\lceil e/2\rceil} + 1) = 2^{\lceil e/2\rceil}.
$$

Za $d \ge e / 2$ vrijedi

$$
(2^d+1)^2 = 2^{2d} + 2^{d+1} + 1 \equiv 2^{d+1} + 1 \pmod{m}.
$$

Stoga indukcijom od $d = \lceil e/2\rceil$ slijedi da $4L(2^d+1)=2^d$ vrijedi za sve $d \ge e/2$. Nadalje, čim je $e/2 \le e_1 < e_2 < \cdots < e_s < e$, vrijedi

$$
(2^{e_1}+1)(2^{e_2}+1)\cdots(2^{e_s}+1) \equiv 1 + 2^{e_1} + 2^{e_2} + \cdots + 2^{e_s} \pmod{m}
$$

te

$$
4L((2^{e_1}+1)(2^{e_2}+1)\cdots(2^{e_s}+1)) = 2^{e_1} + 2^{e_2} + \cdots + 2^{e_s}.
$$

Stoga se nakon obrade svih binarnih bitova s $d < e/2$ diskretni logaritam preostalog dijela može dobiti izravno, bez računanja bit po bit. Uz prvu optimizaciju cijelo potenciranje treba samo $O(e)$ zbrajanja, oduzimanja i bitovnih operacija te $1$ množenje; uz drugu optimizaciju može se uštedjeti otprilike polovica zbrajanja, oduzimanja i bitovnih operacija, ali je potrebno dodatno $1$ množenje.

Kao primjer, referentna implementacija potenciranja cijelih brojeva modulo $2^{32}$ izgleda ovako:

???+ example "Referentna implementacija"
    ```cpp
    --8<-- "docs/math/code/mod-arithmetic/mod-32-inv-pow.cpp:pow"
    ```

Predračun diskretnih logaritama može se obaviti Pohlig–Hellmanovim algoritmom, a baza $g$ može se odabrati kao

$$
5^{\operatorname{ind}_5(2^{\lceil e/2\rceil}+1)/2^{\lceil e/2\rceil - 2}}\bmod{2^e}.
$$

## Literatura i napomene

-   [Fast modular multiplication by orz - Codeforces](https://codeforces.com/blog/entry/96759)
-   [Barrett Reduction - Wikipedia](https://en.wikipedia.org/wiki/Barrett_reduction)
-   [Barrett Reduction - A41](https://encrypt.a41.io/primitives/modular-arithmetic/modular-reduction/barrett-reduction#cost-analysis-of-modular-multiplication)
-   [Barrett 约减原理及正确性证明 by Chen - 知乎专栏](https://zhuanlan.zhihu.com/p/690876166) (Načelo Barrettove redukcije i dokaz ispravnosti, Zhihu)
-   [Montgomery Multiplication - CP Algorithms](https://cp-algorithms.com/algebra/montgomery_multiplication.html)
-   [Montgomery 模乘 by Chen - 知乎专栏](https://zhuanlan.zhihu.com/p/645428404) (Montgomeryjevo množenje, Zhihu)
-   [Binary Exponentiation by Factoring - CP Algorithms](https://cp-algorithms.com/algebra/factoring-exp.html)
-   Barrett, Paul. "Implementing the Rivest Shamir and Adleman public key encryption algorithm on a standard digital signal processor." In Conference on the Theory and Application of Cryptographic Techniques, pp. 311-323. Berlin, Heidelberg: Springer Berlin Heidelberg, 1986.
-   Becker, Hanno, Vincent Hwang, Matthias J. Kannwischer, Bo-Yin Yang, and Shang-Yi Yang. "Neon NTT: Faster Dilithium, Kyber, and Saber on Cortex-A72 and Apple M1." IACR Transactions on Cryptographic Hardware and Embedded Systems (2022): 221-244.
-   Montgomery, Peter L. "Modular multiplication without trial division." Mathematics of computation 44, no. 170 (1985): 519-521.

[^long-double-80bit]: To vrijedi za prevoditelje GCC i Clang na većini 64-bitnih sustava.

[^floating-format]: Vidi [Extended precision - Wikipedia](https://en.wikipedia.org/wiki/Extended_precision).

[^ld-mul-err]: Ovdje se koristi uvjet $a < m$, tj. $a / m \in [0,1)$.

[^int128]: U današnjim glavnim prevoditeljskim okruženjima samo MSVC na platformi Windows ne podržava tip `__int128`. Ako treba napisati kod prenosiv na više platformi, MSVC-ovo okruženje može se otkriti makroom `_MSC_VER` i pod tim uvjetom uključiti zaglavlje [`<intrin.h>`](https://learn.microsoft.com/en-us/cpp/intrinsics/x64-amd64-intrinsics-list?view=msvc-170) te pomoću njegovih ugrađenih funkcija (npr. `_umul128`) neizravno ostvariti 128-bitnu cjelobrojnu aritmetiku (dostupno samo na 64-bitnim platformama).

[^floor-barrett]: Ovdje se $\left\lfloor\dfrac{R}{m}\right\rfloor$ može zamijeniti i drugom cjelobrojnom procjenom od $\dfrac{R}{m}$, npr. funkcijom strop $\left\lceil\dfrac{R}{m}\right\rceil$ ili zaokruživanjem na najbliži cijeli broj $\left\lfloor\dfrac{R}{m}\right\rceil$, uz odgovarajuću prilagodbu koraka ispravljanja pogreške procjene.

[^shoup]: Shoup je ovo proširenje Barrettove redukcije implementirao u svojoj biblioteci za teorijsko-brojevne izračune [NTL](https://libntl.org/), odakle i naziv.

[^newton-hensel]: Izravna provjera: iz $ax \equiv 1 \pmod{2^e}$ možemo staviti $ax = 1 + \lambda 2^e$, pa je $ax(2-ax) = (1+\lambda 2^e)(1-\lambda 2^e) = 1 - \lambda^2 2^{2e} \equiv 1\pmod{2^{2e}}$.

[^mod-2-g]: Na stranici na koju se tekst poziva dokazano je samo da se za $g$ može uzeti $5$. Zapravo, potpunim ponavljanjem tog dokaza može se pokazati da se za $g$ može uzeti bilo koji cijeli broj koji modulo $8$ daje $5$. Izbor $g$ raspravlja se u nastavku.
