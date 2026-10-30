---
title: Faktorijel po modulu
---

## Uvod

U ovom se članku razmatraju rezultati vezani uz računanje faktorijela po zadanom modulu te se daje metoda računanja čija je vremenska složenost linearna u veličini modula, pa je ta metoda prikladna uglavnom kada modul nije prevelik ($\sim 10^6$). Osim metode opisane u ovom članku, ovisno o situaciji, za brzo računanje mogu se primijeniti i [polinomne tehnike](../poly/shift.md#faktorijel-modulo-prost-broj).

Prema [kineskom teoremu o ostatcima](./crt.md), problem računanja faktorijela po modulu može se svesti na slučaj u kojem je modul potencija prostog broja $p^\alpha$. Pri rješavanju takvih problema često je za prost broj $p$ i prirodan broj $n$ potrebno iz faktorijela $n!$ izdvojiti sve faktore $p$, čime se dobiva rastav:

$$
n! = p^{\nu_p(n!)}(n!)_p.
$$

Ovdje $\nu_p(n!)$ označava eksponent broja $p$ u rastavu faktorijela $n!$ na proste faktore, a $(n!)_p$ označava cijeli broj koji se dobije kada se iz vrijednosti faktorijela $n!$ uklone sve potencije broja $p$. U ovom se članku razmatra ostatak broja $(n!)_p$ po modulu koji je prost broj (ili njegova potencija) te konkretan način računanja eksponenta $\nu_p(n!)$.

Ovaj je rastav osobito koristan pri rješavanju problema u kojima se faktorijeli istodobno pojavljuju u brojniku i nazivniku traženog izraza, npr. pri [računanju binomnih koeficijenata po zadanom modulu](./lucas.md). Kod takvih problema eksponenti broja $p$ u brojniku i nazivniku mogu se izravno oduzeti, a dijelovi $(n!)_p$ relativno prosti s $p$ mogu se izračunati pomoću [modularnog inverza](./inverse.md).

U članku se također predstavljaju Wilsonov teorem i njegovo poopćenje, Legendreova formula i Kummerov teorem, koji su povezani s gornjim problemom.

## Wilsonov teorem

Wilsonov teorem daje nužan i dovoljan uvjet da prirodan broj bude prost.

???+ note "Wilsonov teorem"
    Za prirodan broj $n>1$ vrijedi $(n-1)!\equiv -1\pmod n$ ako i samo ako je $n$ prost.

??? note "Dokaz"
    Najprije dokažimo da za prost broj $p$ vrijedi $(p-1)!\equiv -1\pmod{p}$. Za to se pomoću [kongruencija](./congruence-equation.md#kongruencije-po-prostom-modulu) ili [primitivnih korijena](./primitive-root.md) mogu dobiti dva kratka dokaza, koja ovdje izostavljamo. U nastavku dajemo dokaz koji zahtijeva manje predznanja:
    
    Za $p=2$ tvrdnja očito vrijedi. Neka je dalje $p\geq 3$; treba dokazati da je umnožak svih nenul elemenata (tj. klasa ostataka) u $\mathbf{Z}_p$ jednak $\overline{-1}$. Budući da svaki nenul element $\overline{a}$ u $\mathbf{Z}_p$ ima inverz $\overline{a}^{-1}$, umnožak međusobno inverznih elemenata u $\mathbf{Z}_p$ jednak je $\overline{1}$. No treba paziti da $\overline{a}$ i $\overline{a}^{-1}$ mogu biti jednaki: $\overline{a}=\overline{a}^{-1}$ ako i samo ako je $a^2\equiv 1\pmod p$, tj.
    
    $$
    0\equiv a^2-1\equiv (a+1)(a-1)\pmod p,
    $$
    
    odakle je $a\equiv 1\pmod p$ ili $a\equiv -1\pmod p$. To pokazuje da je umnožak svih elemenata iz $\mathbf{Z}_p\setminus\{\overline{0},\overline{1},\overline{-1}\}$ jednak $\overline{1}$, pa je umnožak svih nenul elemenata u $\mathbf{Z}_p$ jednak $\overline{-1}$.
    
    Obratno, za složen broj $n$ treba dokazati da je $(n-1)!\not\equiv-1\pmod{n}$. Dokazujemo kontradikcijom: pretpostavimo da je $(n-1)!\equiv -1\pmod{n}$, tj. da postoji cijeli broj $k$ takav da je $(n-1)!=kn-1$. Budući da je $n$ složen, nužno postoji prost broj $p<n$ takav da je $n=pm$, pa je $(n-1)!=kpm-1\equiv -1\pmod{p}$. Međutim, $p$ se nužno već pojavljuje u umnošku $(n-1)!$, pa mora vrijediti $(n-1)!\equiv 0\pmod{p}$. Ta kontradikcija pokazuje da je $(n-1)!\not\equiv-1\pmod{n}$.

U oznakama ovog članka Wilsonov se teorem može zapisati kao $(p!)_p\equiv -1\pmod{p}$.

### Poopćenje

Wilsonov se teorem može poopćiti na slučaj općeg modula.

???+ note "Teorem (Gauss)"
    Za prirodan broj $m>1$ vrijedi
    
    $$
    \prod_{1\le k<m,\ k\perp m} k \equiv \pm 1 \pmod{m}.
    $$
    
    Štoviše, ostatak $\pm 1$ jednak je $-1$ ako i samo ako [postoji primitivni korijen](./primitive-root.md#teorem-o-postojanju-primitivnog-korijena) po modulu $m$, tj. kada je $m=2,4,p^\alpha,2p^\alpha$, gdje je $p$ neparan prost broj, a $\alpha$ prirodan broj.

??? note "Dokaz"
    Ovaj se teorem može jednostavno dokazati pomoću strukture [multiplikativne grupe cijelih brojeva po modulu $m$](../algebra/ring-theory.md#应用整数同余类的乘法群). Ovdje dajemo dokaz slične ideje, ali elementarniji.
    
    Za $m=2$ vrijedi $1!=1\equiv -1\pmod{2}$. Za ostale slučajeve u kojima postoji primitivni korijen, neka je $g$ primitivni korijen; tada se svaki prirodan broj $k$ manji od $m$ i relativno prost s njim može jednoznačno prikazati u obliku $g^i\bmod m$, gdje je $0\le i<\varphi(m)$, a $\varphi(m)$ je [Eulerova funkcija](./euler-totient.md). Izravnom provjerom vidi se da je $\varphi(m)$ nužno paran. Budući da su $g^i$ i $g^{\varphi(m)-i}$ međusobno multiplikativni inverzi, uparivanjem u umnošku dobivamo
    
    $$
    \prod_{1\le k<m,\ k\perp m} k \equiv \prod_{i=0}^{\varphi(m)-1}g^i = g^{\varphi(m)/2}\prod_{i=1}^{\varphi(m)/2-1}g^{i}g^{\varphi(m)-i} \equiv g^{\varphi(m)/2} \pmod{m}.
    $$
    
    Budući da je $g^{\varphi(m)/2}\bmod m$ jedini element različit od $1\bmod{m}$ koji je sam sebi multiplikativni inverz, on je jednak $-1\bmod{m}$. Time je pokazano da je u tom slučaju ostatak jednak $-1$.
    
    Za slučaj u kojem primitivni korijen po modulu $m$ ne postoji treba dokazati da je ostatak jednak $1$. U tu svrhu najprije napravimo rastav na proste faktore $m=p_1^{e_1}p_2^{e_2}\cdots p_s^{e_s}$, a zatim primjenom [kineskog teorema o ostatcima](./crt.md) vidimo da je dovoljno dokazati da
    
    $$
    \prod_{1\le k<m,\ k\perp m} k\equiv 1\pmod{p_j^{e_j}}
    $$
    
    vrijedi za sve faktore $p_j^{e_j}$. Kineski teorem o ostatcima kaže da svaka moguća kombinacija ostataka $(r_1,r_2,\cdots,r_s)$, gdje je $1\le r_j<p_j^{e_j}$ i $p_j\perp r_j$, jednoznačno odgovara točno jednom broju takvom da je $1\le k<m$, $k\perp m$ i $k\equiv r_j\pmod{p_j^{e_j}}$. Stoga za svaki ostatak $r_j$ postoji točno ${\varphi(m)}/{\varphi(p_j^{e_j})}$ brojeva $k$ za koje vrijedi $k\equiv r_j\pmod{p_j^{e_j}}$. Pomoću toga umnožak možemo grupirati, pa dobivamo
    
    $$
    \prod_{1\le k<m,\ k\perp m} k\equiv\left(\prod_{1\le r_j<p_j^{e_j},\ r_j\perp p_j} r_j\right)^{{\varphi(m)}/{\varphi(p_j^{e_j})}}\pmod{p_j^{e_j}}.
    $$
    
    Da bi ovdje eksponent ${\varphi(m)}/{\varphi(p_j^{e_j})}=\varphi(m/p_j^{e_j})$ bio neparan, nužno mora biti $m/p_j^{e_j}=1,2$, jer je Eulerova funkcija $\varphi(n)$ parna za sve $n\ge 3$. Ako je $p_j$ neparan prost broj, budući da primitivni korijen po modulu $m$ ne postoji, nužno je $m/p_j^{e_j}\neq 1,2$; ako je $p_j^{e_j}=2,4$, budući da primitivni korijen po modulu $m$ ne postoji, $m/p_j^{e_j}$ nužno sadrži neki neparan prost faktor, pa je veći od $2$: u oba je slučaja eksponent ${\varphi(m)}/{\varphi(p_j^{e_j})}$ paran. A za izraz u zagradi u gornjoj formuli već smo dokazali da daje ostatak $-1$ po modulu $p_j^{e_j}$, pa ostatak te potencije po modulu $p_j^{e_j}$ mora biti $1$. Preostaje samo slučaj $p_j=2$ i $e_j>2$, za koji se izravno može dokazati:
    
    $$
    \prod_{1\le r_j<2^{e_j},\ r_j\perp 2}r_j \equiv 1\pmod{2^{e_j}}.
    $$
    
    Slijedeći ideju prethodnog dokaza, sve neparne brojeve $r_j$ s $1\le r_j<2^{e_j}$ možemo upariti tako da se pokrate; oni koji se ne mogu upariti nužno su rješenja jednadžbe $x^2\equiv 1\pmod{2^{e_j}}$. Ta jednadžba znači $2^{e_j}\mid (x-1)(x+1)$. Stavimo li $x=2y+1$, nužno je $2^{e_j-2}\mid y(y+1)$, a od brojeva $y$ i $y+1$ jedan je neparan, a drugi paran, pa je $y=t2^{e_j-2}$ ili $y=t2^{e_j-2}-1$. Dakle, $x=t2^{e_j-1}\pm 1$, gdje je $t$ cijeli broj. Među ostatcima po modulu $2^{e_j}$ takva su samo četiri: $\pm 1$ i $2^{e_j-1}\pm 1$. Stoga vrijedi
    
    $$
    \prod_{1\le r_j<2^{e_j},\ r_j\perp 2}r_j \equiv (-1)(2^{e_j-1}-1)(2^{e_j-1}+1) \equiv 1\pmod{2^{e_j}}.
    $$
    
    Time je dokaz dovršen za sve slučajeve.

U računanju je osobito važan slučaj u kojem je modul potencija prostog broja:

???+ note "Korolar"
    Za prost broj $p$ i prirodan broj $\alpha$ vrijedi
    
    $$
    \prod_{1\le k<p^\alpha,\ k\perp p}k \equiv 
    \begin{cases}
    1, & p=2\text{ and }\alpha\ge3,\\
    -1, &\text{otherwise}
    \end{cases}
    \pmod{p^\alpha}.
    $$

Uočite da lijeva strana nije $(p^\alpha!)_p$, jer potonji izraz uključuje i doprinos višekratnika broja $p$.

## Računanje ostatka faktorijela

U ovom se odjeljku razmatra računanje ostatka $(n!)_p\bmod p^{\alpha}$.

### Slučaj prostog modula

Izraz $(n!)_p$ ima očitu rekurzivnu strukturu. Da bismo je uočili, najprije pogledajmo konkretan primjer:

???+ example "Primjer"
    Da bismo izračunali $(32!)_5 \bmod{5}$, možemo provesti sljedeći rekurzivni račun:
    
    $$
    \begin{aligned}
    (32!)_5 &= 1\times 2\times 3 \times 4\times \underbrace{1}_{5}\times 6 \times 7 \times 8\times 9 \times \underbrace{2}_{10} \\
    &\quad\times 11 \times 12 \times 13 \times 14\times \underbrace{3}_{15}\times 16 \times 17\times 18\times 19\times \underbrace{4}_{20} \\
    &\quad\times 21 \times 22 \times 23 \times 24\times \underbrace{1}_{25}\times 26 \times 27\times 28\times 29\times \underbrace{6}_{30} \times 31 \times 32 \\
    &\equiv 1\times 2\times 3 \times 4\times \underbrace{1}_{5}\times 1 \times 2 \times 3\times 4 \times \underbrace{2}_{10} \\
    &\quad\times 1 \times 2 \times 3 \times 4\times \underbrace{3}_{15}\times 1 \times 2\times 3\times 4\times \underbrace{4}_{20} \\
    &\quad\times 1 \times 2 \times 3 \times 4\times \underbrace{1}_{25}\times 1 \times 2\times 3\times 4\times \underbrace{1}_{30}\times 1\times 2\\
    &= (1\times 2\times 3\times 4)^{6}\times(1\times 2)\times(\underbrace{1}_{5}\times \underbrace{2}_{10}\times \underbrace{3}_{15} \times \underbrace{4}_{20}\times \underbrace{1}_{25}\times \underbrace{1}_{30}) \pmod{5}
    \end{aligned}
    $$
    
    Vidimo da se, zahvaljujući periodičnosti ostataka po modulu $5$, ovaj umnožak može podijeliti na nekoliko blokova duljine $5$, pri čemu je jedina razlika među blokovima ostatak posljednjeg elementa. Budući da dijeljenje $32$ s $5$ daje kvocijent $6$ i ostatak $2$, umnožak se može podijeliti na $6$ potpunih blokova i posljednji nepotpuni blok duljine $2$. Stoga iz prvih $6$ blokova možemo izdvojiti dio bez posljednjeg elementa (upravo taj dio rješava Wilsonov teorem), zatim pomnožiti s umnoškom posljednjeg nepotpunog bloka i na kraju pomnožiti s umnoškom posljednjih elemenata prvih $6$ blokova. Posljednji element svakog bloka višekratnik je broja $5$ pa je, nakon uklanjanja potencija broja $5$, njihov umnožak upravo $(6!)_{5}\pmod{5}$. Time je početni problem sveden na problem manje veličine.

Poopćavanjem rekurzivne strukture iz ovog primjera dobiva se sljedeća rekurzivna formula:

???+ note "Rekurzivna formula"
    Za prost broj $p$ i prirodan broj $n$ vrijedi
    
    $$
    (n!)_p \equiv (-1)^{\left\lfloor n/p\right\rfloor}\cdot (n\bmod p)!\cdot\left(\left\lfloor n/p\right\rfloor!\right)_p\pmod{p}.
    $$

??? note "Dokaz"
    Označimo s $(n)_p$ rezultat uklanjanja svih potencija broja $p$ iz rastava broja $n$ na proste faktore. Tada vrijedi
    
    $$
    \begin{aligned}
    (n!)_p &= \prod_{k=1}^n(k)_p = \left(\prod_{1\le k\le n,\ k\perp p}(k)_p\right)\left(\prod_{1\le k\le\lfloor n/p\rfloor}(pk)_p\right) \\
    &= \left(\prod_{i=0}^{\lfloor n/p\rfloor-1}\prod_{j=1}^{p-1}(ip+j)\right)\left(\prod_{j=1}^{n\bmod p}(\lfloor n/p\rfloor p+j)\right)\left(\prod_{1\le k\le\lfloor n/p\rfloor}(k)_p\right) \\
    &\equiv\left(\prod_{j=1}^{p-1}j\right)^{\lfloor n/p\rfloor}\left(\prod_{j=1}^{n\bmod p}j\right)(\lfloor n/p\rfloor!)_p \\
    &\equiv (-1)^{\lfloor n/p\rfloor}\cdot(n\bmod p)!\cdot(\lfloor n/p\rfloor!)_p \pmod p.
    \end{aligned}
    $$
    
    Time je dokaz dovršen. U nastavku dajemo konkretno objašnjenje ovog formalnog dokaza.
    
    Želimo izračunati vrijednost $(n!)_p\bmod p$. Po uzoru na gornji primjer imamo
    
    $$
    \begin{aligned}
    (n!)_p &= 1 \cdot 2 \cdot 3 \cdot \ldots \cdot (p-2) \cdot (p-1) \cdot \underbrace{1}_{p} \cdot (p+1) \cdot (p+2) \cdot \ldots \cdot (2p-1) \cdot \underbrace{2}_{2p} \\
    &\quad \cdot (2p+1) \cdot \ldots \cdot (p^2-1) \cdot \underbrace{1}_{p^2} \cdot (p^2 +1) \cdot \ldots \cdot n \\
    &\equiv 1 \cdot 2 \cdot 3 \cdot \ldots \cdot (p-2) \cdot (p-1) \cdot \underbrace{1}_{p} \cdot 1 \cdot 2 \cdot \ldots \cdot (p-1) \cdot \underbrace{2}_{2p} \cdot 1 \cdot 2 \\
    &\quad \cdot \ldots \cdot (p-1) \cdot \underbrace{1}_{p^2} \cdot 1 \cdot 2 \cdot \ldots \cdot (n \bmod p) \pmod{p}.
    \end{aligned}
    $$
    
    Jasno se vidi da je faktorijel, osim posljednjeg bloka, podijeljen na nekoliko potpunih blokova jednake duljine.
    
    $$
    \begin{aligned}
    (n!)_p&\equiv \underbrace{1 \cdot 2 \cdot 3 \cdot \ldots \cdot (p-2) \cdot (p-1) \cdot 1}_{1\text{st}} \cdot \underbrace{1 \cdot 2 \cdot 3 \cdot \ldots \cdot (p-2) \cdot (p-1) \cdot 2}_{2\text{nd}} \cdot \ldots \\
    &\quad \cdot \underbrace{1 \cdot 2 \cdot 3 \cdot \ldots \cdot (p-2) \cdot (p-1) \cdot 1}_{p\text{th}} \cdot \ldots \cdot \quad \underbrace{1 \cdot 2 \cdot \ldots \cdot (n \bmod p)}_{\text{tail}} \pmod{p}.
    \end{aligned}
    $$
    
    Glavni dio potpunog bloka, bez posljednjeg elementa, tj. $(p-1)!\bmod p$, lako je izračunati: primjenjuje se Wilsonov teorem:
    
    $$
    (p-1)!\equiv -1\pmod p.
    $$
    
    Ukupno ima $\left\lfloor \dfrac{n}{p} \right\rfloor$ potpunih blokova, pa $\left\lfloor \dfrac{n}{p} \right\rfloor$ treba staviti u eksponent broja $-1$.
    
    Vrijednost posljednjeg, nepotpunog bloka jest $(n\bmod p)!\bmod p$ i može se izračunati zasebno.
    
    Preostaju još posljednji elementi svakog bloka. Ako sakrijemo već obrađene elemente, vidimo sljedeći obrazac:
    
    $$
    (n!)_p = \underbrace{ \ldots \cdot 1 } \cdot \underbrace{ \ldots \cdot 2} \cdot \ldots \cdot \underbrace{ \ldots \cdot (p-1)} \cdot \underbrace{ \ldots \cdot 1 } \cdot \underbrace{ \ldots \cdot 1} \cdot \underbrace{ \ldots \cdot 2} \cdots
    $$
    
    I to je modificirani faktorijel, samo znatno kraći. On iznosi:
    
    $$
    \left(\left\lfloor \frac{n}{p} \right\rfloor !\right)_p.
    $$
    
    Množenjem svih dijelova dobiva se gornja rekurzivna formula.

Pri računanju po ovoj rekurzivnoj formuli dubina rekurzije iznosi $O(\log_p n)$. Ako se srednji član svaki put računa iznova, složenost računanja na svakoj razini iznosi $O(p)$, pa je ukupna vremenska složenost $O(p\log_p n)$; ako se za sve $n=1,2,\cdots,p-1$ unaprijed izračuna $n!\bmod p$, složenost pretprocesiranja iznosi $O(p)$, složenost računanja na svakoj razini iznosi $O(1)$, a ukupna vremenska složenost iznosi $O(p+\log_p n)$.

Budući da je rekurzija repna, implementacija može biti iterativna. Sljedeća implementacija unaprijed računa prvih $p-1$ faktorijela; ako je funkciju potrebno pozivati više puta, pretprocesiranje se može izdvojiti izvan funkcije.

??? example "Referentna implementacija"
    ```cpp
    --8<-- "docs/math/code/factorial/fact-mod-p.cpp:core"
    ```

Ako je prostor ograničen pa se ne mogu pohraniti svi faktorijeli, može se također izračunati sve vrijednosti $n$ iz faktorijela $n!\bmod p$ koji se stvarno koriste u pozivima funkcije, zatim ih sortirati i na kraju odjednom izračunati vrijednosti tih faktorijela te ih uvrstiti u konačni rezultat, čime se izbjegava pohranjivanje vrijednosti svih faktorijela.

### Slučaj modula koji je potencija prostog broja

Slučaj modula koji je potencija prostog broja može se riješiti po uzoru na slučaj prostog modula; dovoljno je Wilsonov teorem zamijeniti njegovim poopćenjem. U oba rezultata ovog odjeljka $\pm 1$ označava upravo sljedeće: za $p=2$ i $\alpha\ge 3$ uzima se $1$, a u ostalim slučajevima $-1$.

???+ note "Rekurzivna formula"
    Za prost broj $p$ i prirodne brojeve $\alpha,n$ vrijedi
    
    $$
    (n!)_{p} \equiv (\pm 1)^{\lfloor n/p^\alpha\rfloor}\cdot\left(\prod_{1\le j\le (n\bmod p^\alpha),\ j\perp p}j\right)\cdot(\lfloor n/p\rfloor!)_p\pmod{p^\alpha}.
    $$
    
    Ovdje se vrijednost $\pm 1$ određuje kao u [poopćenju Wilsonova teorema](#poopćenje).

??? note "Dokaz"
    Ideja dokaza potpuno je ista kao u slučaju prostog modula. Označimo s $(k)_p$ rezultat uklanjanja svih potencija broja $p$ iz rastava broja $k$ na proste faktore; tada je
    
    $$
    \begin{aligned}
    (n!)_p
    &= \prod_{1\le k\le n}(k)_p = \left(\prod_{1\le k\le n,\ k\perp p}(k)_p\right)\left(\prod_{1\le k\le\lfloor n/p\rfloor}(pk)_p\right) \\
    &= \left(\prod_{i=0}^{\lfloor n/p^\alpha\rfloor-1}\prod_{1\le j\le p^\alpha,\ j\perp p}(ip^\alpha+j)_p\right)\left(\prod_{1\le j\le (n\bmod p^\alpha),\ j\perp p}(\lfloor n/p^\alpha\rfloor p^\alpha+j)_p\right)\left(\prod_{1\le k\le\lfloor n/p\rfloor}(k)_p\right)\\
    &\equiv \left(\prod_{1\le j\le p^\alpha,\ j\perp p}j\right)^{\lfloor n/p^\alpha\rfloor}\cdot\left(\prod_{1\le j\le (n\bmod p^\alpha),\ j\perp p}j\right)\cdot(\lfloor n/p\rfloor!)_p\\
    &\equiv (\pm 1)^{\lfloor n/p^\alpha\rfloor}\cdot\left(\prod_{1\le j\le (n\bmod p^\alpha),\ j\perp p}j\right)\cdot(\lfloor n/p\rfloor!)_p \pmod{p^\alpha}.
    \end{aligned}
    $$

Osim toga što $-1$ možda treba zamijeniti s $\pm 1$, razlika u odnosu na slučaj prostog modula jest i u podatcima koji se pretprocesiraju. U slučaju modula koji je potencija prostog broja za sve prirodne brojeve $n$ koji ne premašuju $p^\alpha$ treba unaprijed izračunati umnožak svih cijelih brojeva od $1$ do $n$ koji nisu višekratnici broja $p$, tj.

$$
\prod_{1\le k\le n,\ k\perp p} k\bmod{p^\alpha}.
$$

U slučaju prostog modula, za $n<p$, taj se izraz svodi na $n!\bmod p$, ali u općem slučaju potencije prostog broja to više ne vrijedi.

U nastavku dajemo primjer računanja ostatka faktorijela po modulu koji je potencija prostog broja, radi lakšeg razumijevanja gornje metode:

???+ example "Primjer"
    Da bismo izračunali $(32!)_3\bmod 9$, možemo provesti sljedeći rekurzivni račun:
    
    $$
    \begin{aligned}
    (32!)_3 
    &= 1\times 2\times \underbrace{1}_{3} \times 4\times 5\times \underbrace{2}_{6}\times 7\times 8\times\underbrace{1}_{9}\\
    &\quad\times 10\times 11\times\underbrace{4}_{12}\times 13\times 14\times\underbrace{5}_{15}\times 16\times 17\times\underbrace{2}_{18}\\
    &\quad\times 19\times 20\times\underbrace{7}_{21}\times 22\times 23\times\underbrace{8}_{24}\times 25\times 26\times\underbrace{1}_{27}\\
    &\quad\times 28\times 29\times\underbrace{10}_{30}\times 31\times 32\\
    &\equiv 1\times 2\times \underbrace{1}_{3} \times 4\times 5\times \underbrace{2}_{6}\times 7\times 8\times\underbrace{1}_{9}\\
    &\quad\times 1\times 2\times\underbrace{4}_{12}\times 4\times 5\times\underbrace{5}_{15}\times 7\times 8\times\underbrace{2}_{18}\\
    &\quad\times 1\times 2\times\underbrace{7}_{21}\times 4\times 5\times\underbrace{8}_{24}\times 7\times 8\times\underbrace{1}_{27}\\
    &\quad\times 1\times 2\times\underbrace{1}_{30}\times 4\times 5\\
    &=(1\times 2\times 4\times 5\times 7\times 8)^{3}\times (1\times 2\times 4\times 5)\\
    &\quad\times\begin{pmatrix}\underbrace{1}_{3}\times\underbrace{2}_{6}\times\underbrace{1}_{9}\times\underbrace{4}_{12}\times\underbrace{5}_{15}\times\underbrace{2}_{18}\\\times\underbrace{7}_{21}\times\underbrace{8}_{24}\times\underbrace{1}_{27}\times\underbrace{1}_{30}\end{pmatrix}\pmod{9}.
    \end{aligned}
    $$
    
    Rastav izraza $(32!)_3\bmod 9$ također se može podijeliti na tri dijela:
    
    -   potpuni blokovi: umnožak svih cijelih brojeva u rasponu $1\sim 9$ koji nisu djeljivi s $3$, ukupno $\lfloor 32/9\rfloor=3$ bloka;
    -   nepotpuni blok na kraju: umnožak svih cijelih brojeva koji nisu djeljivi s $3$ od $1$ do $32\bmod 9$;
    -   umnožak svih cijelih brojeva djeljivih s $3$; usporedbom s rezultatom nakon pretposljednjeg znaka jednakosti vidi se da je to upravo prvih $\lfloor 32/3\rfloor=10$ članova, tj. $(\lfloor 32/3\rfloor!)_3\bmod 9$.
    
    Dio u posljednjoj zagradi rješava se rekurzivno; time je početni problem sveden na manji problem.

Odatle se dobiva sljedeći rekurzivni rezultat:

???+ note "Rekurzivni rezultat"
    Za prost broj $p$ i prirodne brojeve $\alpha,n$ vrijedi
    
    $$
    (n!)_p \equiv (\pm 1)^{\sum_{j\ge\alpha}\lfloor{n}/{p^j}\rfloor}\prod_{j\ge 0}F(\lfloor n/p^j\rfloor\bmod p^\alpha)\pmod{p^\alpha},
    $$
    
    gdje je $F(m) = \prod_{1\le k\le m,\ k\perp p} k\bmod{p^\alpha}$, a vrijednost $\pm 1$ određuje se kao gore.

Implementacija za slučaj modula koji je potencija prostog broja slična je onoj za slučaj prostog modula, razlikuje se samo u nekim detaljima. Kao i gore, pretprocesiranje se može izdvojiti izvan funkcije.

??? example "Referentna implementacija"
    ```cpp
    --8<-- "docs/math/code/factorial/fact-mod-pa.cpp:core"
    ```

Vremenska složenost pretprocesiranja iznosi $O(p^\alpha)$, a vremenska složenost jednog upita $O(\log_p n)$.

## Računanje eksponenta

U ovom se odjeljku razmatra računanje eksponenta $\nu_p(n!)$ broja $p$ u faktorijelu $n!$, koje se može iskoristiti za računanje ostatka binomnih koeficijenata. Naime, u binomnom koeficijentu faktorijeli se pojavljuju i u brojniku i u nazivniku, pa to hoće li se prost broj $p$ u brojniku i nazivniku međusobno pokratiti postaje ključan čimbenik koji određuje konačni ostatak.

### Legendreova formula

Eksponent prostog broja $p$ u faktorijelu $n!$ može se izračunati Legendreovom formulom i povezan je s prikazom broja $n$ u bazi $p$.

???+ note "Legendreova formula"
    Za prirodan broj $n$ eksponent $\nu_p(n!)$ prostog broja $p$ sadržanog u faktorijelu $n!$ iznosi
    
    $$
    \nu_p(n!) = \sum_{i=1}^{\infty} \left\lfloor \dfrac{n}{p^i} \right\rfloor = \dfrac{n-S_p(n)}{p-1},
    $$
    
    gdje je $S_p(n)$ zbroj znamenki broja $n$ u bazi $p$. Posebno, eksponent broja $2$ u faktorijelu iznosi $\nu_2(n!)=n-S_2(n)$.

??? note "Dokaz"
    Budući da je
    
    $$
    n! = 1\times 2\times \cdots \times p\times \cdots \times 2p\times \cdots \times \lfloor n/p\rfloor p\times \cdots \times n.
    $$
    
    Ovdje je umnožak višekratnika broja $p$ jednak $p\times 2p\times \cdots \times \lfloor n/p\rfloor p=p^{\lfloor n/p\rfloor }\lfloor n/p\rfloor !$, a u $\lfloor n/p\rfloor !$ mogu se i dalje pojavljivati višekratnici broja $p$. Stoga za eksponent vrijedi rekurzivna relacija:
    
    $$
    \nu_p(n!) = \lfloor n/p\rfloor + \nu_p(\lfloor n/p\rfloor!).
    $$
    
    Njezinim raspisivanjem dobiva se Legendreova formula.
    
    Da bismo dokazali drugu jednakost, najprije raspišimo $n$ u bazi $p$, što je isto kao zapisati ga kao sljedeću sumu:
    
    $$
    n = n_\ell p^{\ell} + \cdots + n_1 p + n_0 = \sum_{k=0}^\ell n_kp^k.
    $$
    
    Stoga vrijedi
    
    $$
    \begin{aligned}
    \nu_p(n!)
    &= \sum_{i=1}^{\ell}\left\lfloor\dfrac{n}{p^i}\right\rfloor 
    = \sum_{i=1}^\ell\sum_{k=i}^{\ell}n_kp^{k-i}
    = \sum_{k=1}^\ell n_k\sum_{i=1}^kp^{k-i} \\
    &= \sum_{k=1}^\ell n_k\dfrac{p^k-1}{p-1} 
    = \dfrac{\sum_{k=0}^\ell n_kp^k - \sum_{k=0}^\ell n_k}{p-1} 
    = \dfrac{n - S_p(n)}{p-1}.
    \end{aligned}
    $$

Referentna implementacija računanja eksponenta prostog broja u faktorijelu:

??? example "Referentna implementacija"
    ```cpp
    --8<-- "docs/math/code/factorial/multiplicity.cpp:core"
    ```

Njezina vremenska složenost iznosi $O(\log n)$.

### Kummerov teorem

Ostatci binomnih koeficijenata po nekom modulu često tvore fraktalnu strukturu; npr. trokut Sierpińskog može se dobiti iz binomnih koeficijenata po modulu $2$.

Pažljivom analizom vidi se da je pitanje dijeli li $p$ binomni koeficijent zapravo povezano s time je li pri oduzimanju gornjeg i donjeg indeksa u bazi $p$ potrebno posuđivanje. Odatle dolazi **Kummerov teorem**.

???+ note "Kummerov teorem"
    Eksponent prostog broja $p$ u binomnom koeficijentu $\dbinom{m}{n}$ jednak je upravo broju posuđivanja potrebnih pri oduzimanju $n$ od $m$ u bazi $p$, tj.
    
    $$
    \nu_p\left(\dbinom{m}{n}\right)=\frac{S_p(n)+S_p(m-n)-S_p(m)}{p-1}.
    $$
    
    Posebno, eksponent broja $2$ u binomnom koeficijentu iznosi $\nu_2\left(\dbinom{m}{n}\right)=S_2(n)+S_2(m-n)-S_2(m)$.

??? note "Dokaz"
    Najprije dokažimo donji izraz. Prema Legendreovoj formuli vrijedi
    
    $$
    \begin{aligned}
    \nu_p\left(\dbinom{m}{n}\right)
    &=\nu_p(m!)-\nu_p(n!)-\nu_p((m-n)!)\\
    &=\sum_{i=1}^\infty\left(\left\lfloor\dfrac{m}{p^i}\right\rfloor-\left\lfloor\dfrac{n}{p^i}\right\rfloor-\left\lfloor\dfrac{m-n}{p^i}\right\rfloor\right)\\
    &=\frac{S_p(n)+S_p(m-n)-S_p(m)}{p-1}.
    \end{aligned}
    $$
    
    Taj se izraz može shvatiti kao broj posuđivanja potrebnih pri oduzimanju $n$ od $m$ u bazi $p$. Naime, ako pri računanju $i$-te znamenke (najniža znamenka ima indeks $1$) oduzimanje nije moguće pa je potrebno posuđivanje, tada je broj koji u rezultatu oduzimanja čine znamenke iznad $i$-te, $\left\lfloor\dfrac{m-n}{p^i}\right\rfloor$, zapravo razlika koja se dobije kada se od broja koji čine znamenke iznad $i$-te u $m$, $\left\lfloor\dfrac{m}{p^i}\right\rfloor$, oduzme jedan (tj. posuđena jedinica) i zatim oduzme broj koji čine znamenke iznad $i$-te u $n$, $\left\lfloor\dfrac{n}{p^i}\right\rfloor$; stoga je razlika
    
    $$
    \left\lfloor\dfrac{m}{p^i}\right\rfloor-\left\lfloor\dfrac{n}{p^i}\right\rfloor-\left\lfloor\dfrac{m-n}{p^i}\right\rfloor = 1
    $$
    
    ako i samo ako je došlo do posuđivanja; inače je ta razlika $0$. Stoga se suma u gornjem izrazu može shvatiti kao broj posuđivanja. Time je dobivena riječima iskazana formulacija Kummerova teorema.

## Primjer zadatka

???+ example "Primjer zadatka [HDU 2973 - YAPTCHA](https://acm.hdu.edu.cn/showproblem.php?pid=2973)"
    Za zadani $n$ izračunajte
    
    $$
    \sum_{k=1}^n\left\lfloor\frac{(3k+6)!+1}{3k+7}-\left\lfloor\frac{(3k+6)!}{3k+7}\right\rfloor\right\rfloor
    $$

??? note "Ideja rješenja"
    Ako je $3k+7$ prost broj, tada je
    
    $$
    (3k+6)!\equiv-1\pmod{3k+7}
    $$
    
    Stavimo $(3k+6)!+1=m(3k+7)$
    
    Tada je
    
    $$
    \left\lfloor\frac{(3k+6)!+1}{3k+7}-\left\lfloor\frac{(3k+6)!}{3k+7}\right\rfloor\right\rfloor=\left\lfloor m-\left\lfloor m-\frac{1}{3k+7}\right\rfloor\right\rfloor=1
    $$
    
    Ako $3k+7$ nije prost broj, tada je on složen broj veći od $4$ pa vrijedi $(3k+7)\mid(3k+6)!$, tj.
    
    $$
    (3k+6)!\equiv 0\pmod{3k+7}
    $$
    
    Stavimo $(3k+6)!=m(3k+7)$; tada je
    
    $$
    \left\lfloor\frac{(3k+6)!+1}{3k+7}-\left\lfloor\frac{(3k+6)!}{3k+7}\right\rfloor\right\rfloor=\left\lfloor m+\frac{1}{3k+7}-m\right\rfloor=0
    $$
    
    Stoga je
    
    $$
    \sum_{k=1}^n\left\lfloor\frac{(3k+6)!+1}{3k+7}-\left\lfloor\frac{(3k+6)!}{3k+7}\right\rfloor\right\rfloor=\sum_{k=1}^n[3k+7\text{ is prime}]
    $$

??? example "Referentni kod"
    ```cpp
    --8<-- "docs/math/code/factorial/wilson_1.cpp"
    ```

## Literatura

-   冯克勤 (Feng Keqin). „初等数论及其应用” (Elementarna teorija brojeva i njezine primjene).
-   [Wilson's theorem - Wikipedia](https://en.wikipedia.org/wiki/Wilson%27s_theorem)
-   [Legendre's formula - Wikipedia](https://en.wikipedia.org/wiki/Legendre%27s_formula)

**Ova je stranica uglavnom prevedena iz članka [Вычисление факториала по модулю](http://e-maxx.ru/algo/modular_factorial) i njegova engleskog prijevoda [Factorial modulo p](https://cp-algorithms.com/algebra/factorial-modulo.html). Ruska je inačica objavljena pod licencijom Public Domain + Leave a Link, a engleska pod CC-BY-SA 4.0. Sadržaj je izmijenjen.**
