---
title: Red elementa & primitivni korijen
---

Predznanje: [mali Fermatov teorem](./fermat.md#mali-fermatov-teorem), [Eulerov teorem](./fermat.md#eulerov-teorem), [Lagrangeov teorem](./congruence-equation.md#kongruencije-po-prostom-modulu)

Red elementa i primitivni korijen važni su alati za razumijevanje multiplikativne strukture [reduciranog sustava ostataka](./basic.md#klase-kongruencije-i-sustavi-ostataka) $\mathbf Z_m^*$ modulo $m$. Na njima se temelje pojmovi poput [diskretnog logaritma](./discrete-logarithm.md). Općenitija rasprava može se naći u odgovarajućim poglavljima stranica o [teoriji grupa](../algebra/group-theory.md#阶) i [teoriji prstena](../algebra/ring-theory.md#应用整数同余类的乘法群) u dijelu o apstraktnoj algebri.

## Red

U ovom odjeljku uvijek pretpostavljamo da su modul $m\in\mathbf N_+$ i baza $a\in\mathbf Z$ relativno prosti, tj. $(a,m)=1$, što zapisujemo i kao $a\perp m$.

Za $n\in\mathbf Z$ potencije $a^n\bmod m$ pokazuju cikličku strukturu. Najmanja duljina tog ciklusa upravo je red elementa $a$ modulo $m$. Red se definira kao eksponent pri kojem se potencija $a^n \bmod m$ prvi put vraća na početak $a^0\bmod m = 1$:

???+ abstract "Red"
    Za $a\in\mathbf Z,m\in\mathbf N_+$ takve da je $a\perp m$, najmanji pozitivni cijeli broj $n$ koji zadovoljava kongruenciju $a^n \equiv 1 \pmod m$ naziva se **red elementa $a$ modulo $m$** (engl. the order of $a$ modulo $m$) i označava se $\delta_m(a)$ ili $\operatorname{ord}_m(a)$.

???+ tip "Napomena"
    U [apstraktnoj algebri](../algebra/group-theory.md#阶) ovaj je „red” upravo red elementa $a$ u grupi koju reducirani sustav ostataka modulo $m$ tvori s obzirom na množenje. Oznaka $\delta$ za red koristi se samo za tu posebnu grupu. Mnoga od svojstava u nastavku mogu se izravno poopćiti na svojstva reda elementa grupe u apstraktnoj algebri.
    
    Postoji i pojam „polureda” (half-order), koji se u teoriji brojeva označava $\delta^-$. To je najmanji pozitivni cijeli broj koji zadovoljava kongruenciju $a^n \equiv -1 \pmod m$. Polured nije pojam iz teorije grupa. Red uvijek postoji, a polured ne mora postojati.

### Ciklička struktura potencija

Pomoću reda može se opisati ciklička struktura potencija. Za potenciju $a^n\bmod m$ eksponent $n$ možemo podijeliti s ostatkom redom $\delta_m(a)$:

$$
n = \delta_m(a)q + r, ~ 0\le r < \delta_m(a). 
$$

Zatim, prema pravilima potenciranja, dobivamo

$$
a^n = a^{\delta_m(a)q + r} = (a^{\delta_m(a)})^q \cdot a^r \equiv a^r \pmod m.
$$

To pokazuje da se potencija s bilo kojim eksponentom može pomaknuti u prvi nenegativni ciklus. Iz toga se dobiva niz svojstava reda.

???+ note "Svojstvo 1"
    Za $a\in\mathbf Z,m\in\mathbf N_+$ takve da je $a\perp m$, potencije $a^0(=1),a,a^2,\cdots,a^{\delta_m(a)-1}$ međusobno su nekongruentne modulo $m$.

??? note "Dokaz"
    Dokazujemo kontradikcijom. Pretpostavimo da postoje dva broja $0\le i< j<\delta_m(a)$ takva da je $a^i\equiv a^j\pmod m$; tada vrijedi $a^{j - i}\equiv 1\pmod m$. No $0 < j - i < \delta_m(a)$. To je u suprotnosti s minimalnošću reda, pa tvrdnja vrijedi.

???+ note "Svojstvo 2"
    Za $a,n\in\mathbf Z,m\in\mathbf N_+$ takve da je $a\perp m$, kongruencija $a^n \equiv 1 \pmod m$ vrijedi ako i samo ako $\delta_m(a)\mid n$.

??? note "Dokaz"
    Kao što je gore rečeno, $a^{n}\equiv a^{n\bmod\delta_m(a)}\pmod m$. Prema svojstvu 1, jedini $r$ u rasponu $0\le r < \delta_m(a)$ za koji vrijedi $a^r\equiv 1\pmod m$ jest $r=0$. Stoga $a^n \equiv 1 \pmod m$ vrijedi ako i samo ako je $n\bmod \delta_m(a) = 0$, tj. $\delta_m(a)\mid n$.

Prema [Eulerovu teoremu](./fermat.md#eulerov-teorem) kongruencija $a^{\varphi(m)}\equiv 1\pmod m$ vrijedi za sve $a\perp m$. U kombinaciji sa svojstvom 2 to znači da za sve $a\perp m$ vrijedi $\delta_m(a)\mid\varphi(m)$. Drugim riječima, $\varphi(m)$ je zajednički višekratnik redova svih $a\perp m$. Za pozitivni cijeli broj $m$ najmanji zajednički višekratnik redova $\delta_m(a)$ svih $a\perp m$, označen $\lambda(m)$, upravo je [Carmichaelova funkcija](#carmichaelova-funkcija) broja $m$. Njezina se svojstva detaljno razmatraju u nastavku.

Slično kao i kod drugih cikličkih struktura, iz reda elementa $a$ može se izračunati red elementa $a^k$.

???+ note "Svojstvo 3"
    Za $k,a\in\mathbf Z,m\in\mathbf N_+$ takve da je $a\perp m$ vrijedi
    
    $$
    \delta_m(a^k) = \dfrac{\delta_m(a)}{(\delta_m(a),k)}.
    $$

??? note "Dokaz"
    Prema svojstvu 2, kongruencija $(a^k)^n = a^{kn} \equiv 1\pmod m$ vrijedi ako i samo ako $\delta_m(a) \mid kn$. Taj je uvjet ekvivalentan uvjetu
    
    $$
    \dfrac{\delta_m(a)}{\left(\delta_m(a),k\right)} \mid n.
    $$
    
    Najmanji pozitivni cijeli broj koji zadovoljava taj uvjet upravo je
    
    $$
    \delta_m(a^k)=\dfrac{\delta_m(a)}{\left(\delta_m(a),k\right)}.
    $$

### Red umnoška

Neka su $a,b$ različiti cijeli brojevi relativno prosti s $m$. Ako su poznati redovi $\delta_m(a)$ i $\delta_m(b)$, tada se također mogu dobiti neke informacije o redu $\delta_{m}(ab)$ njihova umnoška $ab$.

???+ note "Svojstvo 4"
    Za $a,b\in\mathbf Z,m\in\mathbf N_+$ takve da je $a,b\perp m$ vrijedi
    
    $$
    \dfrac{[\delta_m(a),\delta_m(b)]}{(\delta_m(a),\delta_m(b))} \mid \delta_m(ab) \mid [\delta_m(a),\delta_m(b)].
    $$

??? note "Dokaz"
    Budući da je $[\delta_m(a),\delta_m(b)]$ višekratnik i od $\delta_m(a)$ i od $\delta_m(b)$, prema svojstvu 2 vrijedi
    
    $$
    (ab)^{[\delta_m(a),\delta_m(b)]} = a^{[\delta_m(a),\delta_m(b)]} b^{[\delta_m(a),\delta_m(b)]} \equiv 1 \pmod m.
    $$
    
    Ponovnom primjenom svojstva 2 dobivamo
    
    $$
    \delta_m(ab) \mid [\delta_m(a),\delta_m(b)].
    $$
    
    Time je dobivena desna relacija djeljivosti.
    
    Obrnuto, budući da je
    
    $$
    1 \equiv (ab)^{\delta_m(ab)\delta_m(b)} \equiv a^{\delta_m(ab)\delta_m(b)} \pmod m,
    $$
    
    primjenom svojstva 2 dobivamo $\delta_m(a)\mid\delta_m(ab)\delta_m(b)$. Kraćenjem obiju strana s $(\delta_m(a),\delta_m(b))$ dobivamo
    
    $$
    \dfrac{\delta_m(a)}{(\delta_m(a),\delta_m(b))}\mid\delta_m(ab)\dfrac{\delta_m(b)}{(\delta_m(a),\delta_m(b))}.
    $$
    
    Nakon kraćenja zajedničkog faktora ta su dva razlomka relativno prosta, pa dobivamo
    
    $$
    \dfrac{\delta_m(a)}{(\delta_m(a),\delta_m(b))}\mid\delta_m(ab).
    $$
    
    Analogno vrijedi i
    
    $$
    \dfrac{\delta_m(b)}{(\delta_m(a),\delta_m(b))}\mid\delta_m(ab).
    $$
    
    Budući da su lijeve strane tih dviju relacija djeljivosti relativno proste, vrijedi
    
    $$
    \dfrac{[\delta_m(a),\delta_m(b)]}{(\delta_m(a),\delta_m(b))} =\dfrac{\delta_m(a)\delta_m(b)}{(\delta_m(a),\delta_m(b))^2}\mid\delta_m(ab).
    $$
    
    Time je dobivena lijeva relacija djeljivosti.

U slučaju kada su redovi elemenata $a$ i $b$ relativno prosti, ovaj zaključak ima jednostavniji oblik.

???+ note "Svojstvo 4'"
    Za $a,b\in\mathbf Z,m\in\mathbf N_+$ takve da je $a,b\perp m$ vrijedi
    
    $$
    \delta_m(ab) = \delta_m(a)\delta_m(b) \iff \delta_m(a)\perp\delta_m(b).
    $$

??? note "Dokaz"
    Ako je $\delta_m(a)\perp\delta_m(b)$, tada su sve relacije djeljivosti u svojstvu 4 jednakosti, pa vrijedi
    
    $$
    \delta_m(ab) = [\delta_m(a),\delta_m(b)] = \delta_m(a)\delta_m(b).
    $$
    
    Obrnuto, ako je $\delta_m(ab)=\delta_m(a)\delta_m(b)$, tada prema svojstvu 4 vrijedi
    
    $$
    \delta_m(a)\delta_m(b) = \delta_m(ab) \mid [\delta_m(a),\delta_m(b)].
    $$
    
    Iz toga odmah slijedi $(\delta_m(a),\delta_m(b))=1$, tj. $\delta_m(a)\perp\delta_m(b)$.

U općem slučaju ograda dobivena u svojstvu 4 već je najbolja moguća. Slučaj u kojem red umnoška postiže donju ogradu lako je konstruirati: na primjer, za $(a,b,m)=(3,5,7)$ vrijedi $\delta_m(a)=\delta_m(b)=6$, ali red njihova umnoška je $\delta_m(ab)=1$.

Iako u općem slučaju red umnoška $ab$ ne mora biti najmanji zajednički višekratnik njihovih redova, uvijek se može pronaći element čiji je red jednak tom najmanjem zajedničkom višekratniku.

???+ note "Svojstvo 5"
    Za $a,b\in\mathbf Z,m\in\mathbf N_+$ takve da je $a,b\perp m$ uvijek postoji $c\in\mathbf Z$ takav da je $c\perp m$ i
    
    $$
    \delta_m(c) = [\delta_m(a),\delta_m(b)].
    $$

??? note "Dokaz"
    Promotrimo rastave na proste faktore:
    
    $$
    \delta_m(a) = \prod_p p^{\alpha_p},~ \delta_m(b) = \prod_p p^{\beta_p}.
    $$
    
    Prema odnosu veličina $\alpha_p$ i $\beta_p$ svi se prosti faktori mogu podijeliti u dvije klase:
    
    $$
    A = \{p : \alpha_p \ge \beta_p\}, ~ B = \{p : \alpha_p < \beta_p\}.
    $$
    
    U skladu s tim označimo redom
    
    $$
    \gamma_A = \prod_{p\in A}p^{\alpha_p},~\gamma_B = \prod_{p\in B}p^{\alpha_p},~\eta_A = \prod_{p\in A}p^{\beta_p},~\eta_B = \prod_{p\in B}p^{\beta_p},
    $$
    
    pa vrijedi $\delta_m(a) = \gamma_A\gamma_B$ i $\delta_m(b)=\eta_A\eta_B$. Prema svojstvu 3 vrijedi
    
    $$
    \begin{aligned}
    \delta_m(a^{\gamma_B}) &= \dfrac{\delta_m(a)}{(\delta_m(a),\gamma_B)} = \dfrac{\delta_m(a)}{\gamma_B} = \gamma_A,\\
    \delta_m(b^{\eta_A}) &= \dfrac{\delta_m(b)}{(\delta_m(b),\eta_A)} = \dfrac{\delta_m(b)}{\eta_A} = \eta_B.
    \end{aligned}
    $$
    
    Budući da je $\gamma_A\perp\eta_B$, prema svojstvu 4' vrijedi
    
    $$
    \delta_m(a^{\gamma_B}b^{\eta_A}) = \gamma_A\eta_B = \prod_p p^{\max\{\alpha_p,\beta_p\}} = [\delta_m(a),\delta_m(b)].
    $$
    
    Dakle, $c=a^{\gamma_B}b^{\eta_A}$ upravo je element reda $[\delta_m(a),\delta_m(b)]$.

Ovaj se zaključak često koristi za konstrukciju elemenata zadanog reda.

## Primitivni korijen

Primitivni korijeni posebni su elementi – njihov je red jednak broju elemenata reduciranog sustava ostataka modulo $m$.

???+ abstract "Primitivni korijen"
    Za $m\in\mathbf N_+$, ako postoji $g\in\mathbf Z$ takav da je $g\perp m$ i $\delta_m(g)=|\mathbf Z_m^*|=\varphi(m)$, tada se $g$ naziva **primitivni korijen modulo $m$** (engl. primitive root modulo $m$). Pritom je $\varphi(m)$ [Eulerova funkcija](./euler-totient.md).

Primitivni korijen modulo $m$ ne postoji za svaki pozitivni cijeli broj $m$. Prema gornjem [svojstvu 1](#ciklička-struktura-potencija), ako primitivni korijen $g$ modulo $m$ postoji, tada su klase kongruencije kojima pripadaju $g,g^2,\cdots,g^{\varphi(m)}$ međusobno različite i tvore reducirani sustav ostataka modulo $m$. Posebno, za prost broj $p$ ostatci $g^i\bmod p$ za $i=1,2,\cdots,p-1$ međusobno su različiti.

???+ tip "Napomena"
    U [apstraktnoj algebri](../algebra/ring-theory.md#应用整数同余类的乘法群) primitivni korijen upravo je generator cikličke grupe. Taj pojam nosi naziv „primitivni korijen” samo u grupi koju reducirani sustav ostataka modulo $m$ tvori s obzirom na množenje; u općim cikličkim grupama govori se o „generatoru”. Nije svaka grupa koju reducirani sustav ostataka modulo $m$ tvori s obzirom na množenje ciklička: postojanje primitivnog korijena znači da je ona izomorfna cikličkoj grupi, a nepostojanje da nije.

Kada je modul $1$, multiplikativna grupa cijelih brojeva modulo $1$ jest $\{0\}$. Ona je očito ciklička, pa je primitivni korijen $0$.

### Kriterij za primitivni korijen

Ako su poznati svi prosti faktori broja $\varphi(m)$, lako je provjeriti je li zadani $g$ primitivni korijen modulo $m$.

???+ note "Teorem"
    Za cijeli broj $m\ge 3$ i $g\perp m$, $g$ je primitivni korijen modulo $m$ ako i samo ako za svaki prosti faktor $p$ broja $\varphi(m)$ vrijedi
    
    $$
    g^{\frac{\varphi(m)}{p}}\not\equiv 1 \pmod m.
    $$

??? note "Dokaz"
    Nužnost je očita. Za dokaz dovoljnosti koristimo kontradikciju. Ako $g$ nije primitivni korijen modulo $m$, tada nužno vrijedi $\delta_m(g)< \varphi(m)$. Prema [svojstvu 2](#ciklička-struktura-potencija) i Eulerovu teoremu, $\delta_m(g)\mid\varphi(m)$. Neka je stoga $p$ neki prosti faktor broja $\dfrac{\varphi(m)}{\delta_m(g)}$; tada vrijedi $\delta_m(g)\mid\dfrac{\varphi(m)}{p}$. Ponovnom primjenom svojstva 2 dobivamo
    
    $$
    g^{\frac{\varphi(m)}{p}} \equiv 1 \pmod m.
    $$
    
    No $p$ je ujedno prosti faktor broja $\varphi(m)$, što je u suprotnosti s pretpostavkom teorema. Time je dokazana dovoljnost.

### Broj primitivnih korijena

Primitivni korijen, ako postoji, ne mora biti jedinstven. Općenito, o mogućim redovima svih elemenata reduciranog sustava ostataka modulo $m$ i o broju elemenata određenog reda vrijedi sljedeći zaključak:

???+ note "Teorem"
    Ako pozitivni cijeli broj $m$ ima primitivni korijen $g$, tada element reda $d$ modulo $m$ postoji ako i samo ako $d\mid\varphi(m)$, i tada takvih elemenata ima točno $\varphi(d)$. Posebno, broj primitivnih korijena modulo $m$ jest $\varphi(\varphi(m))$.

??? note "Dokaz"
    Prema definiciji primitivnog korijena, sve reducirane klase kongruencije modulo $m$ mogu se zapisati u obliku $g^k\bmod m$, pri čemu je $k$ jedan od brojeva $1,2,\cdots,\varphi(m)$. Prema [svojstvu 3](#ciklička-struktura-potencija) red tih elemenata jednak je
    
    $$
    \delta_m(g^k) = \dfrac{\varphi(m)}{(\varphi(m),k)}.
    $$
    
    Dakle, element reda $d$ postoji ako i samo ako $d\mid\varphi(m)$. Štoviše, za $d\mid\varphi(m)$, uz oznaku $d'=\varphi(m)/d$, skup tih elemenata jest
    
    $$
    \begin{aligned}
    A &= \{g^k : (\varphi(m),k)=d',~1\le k \le\varphi(m)\} \\
    &= \{g^k : d'\mid k,~ (d, k/d') = 1,~ 1 \le k/d' \le d\}.
    \end{aligned}
    $$
    
    Brojevi $k'=k/d'$ koji odgovaraju tim elementima upravo su pozitivni cijeli brojevi koji ne premašuju $d$ i relativno su prosti s $d$. Prema definiciji Eulerove funkcije, njih je $\varphi(d)$.

### Teorem o postojanju primitivnog korijena

U ovom odjeljku dokazujemo sljedeći teorem o postojanju primitivnog korijena:

???+ note "Teorem"
    Primitivni korijen modulo $m$ postoji ako i samo ako je $m=1,2,4,p^e,2p^e$, gdje je $p$ neparan prost broj i $e\in\mathbf N_+$.

Za dokaz ove tvrdnje treba zasebno razmotriti sljedeća četiri slučaja:

1.  $m=1,2,4$: primitivni korijeni su redom $g=0,1,3$ i očito postoje.

2.  $m=p^{e}$ je potencija neparnog prostog broja, gdje je $p$ neparan prost broj, $e\in\mathbf N_+$.

    ???+ note "Lema 1"
        Za neparan prost broj $p$ postoji primitivni korijen modulo $p$.

    ??? note "Dokaz"
        Dokaz se sastoji od dva koraka.
        
        **Prvi korak**: za $d\mid(p-1)$ kongruencija $x^d\equiv 1\pmod p$ ima točno $d$ međusobno različitih rješenja.
        
        Neka je $p-1=kd$ i promotrimo polinom
        
        $$
        f(x) = x^{d(k-1)} + x^{d(k-2)} + \cdots + x^d + 1. 
        $$
        
        Prema [Eulerovu teoremu](./fermat.md#eulerov-teorem) kongruencija $(x^d-1)f(x)=x^{p-1}-1\equiv 0\pmod{p}$ ima točno $p-1$ međusobno različitih rješenja. Ta su rješenja redom nultočke polinoma $x^d-1$ odnosno $f(x)$. Prema [Lagrangeovu teoremu](./congruence-equation.md#kongruencije-po-prostom-modulu) oni mogu imati najviše $d$ odnosno $d(k-1)$ međusobno različitih nultočaka. Budući da je $d+d(k-1)=p-1$, prvi od njih mora imati točno $d$ međusobno različitih nultočaka. To pokazuje da kongruencija $x^d\equiv 1\pmod p$ ima točno $d$ međusobno različitih rješenja.
        
        **Drugi korak**: za $d\mid(p-1)$ postoji točno $\varphi(d)$ elemenata reda $d$.
        
        Poredamo sve djelitelje broja $p-1$ i primijenimo indukciju. Budući da element reda $1$ može biti samo $1$, takav je element samo jedan, pa baza indukcije vrijedi. Za $d\mid(p-1)$, prema gornjem [svojstvu 2](#ciklička-struktura-potencija), rješenja kongruencije $x^d\equiv 1\pmod p$ nužno zadovoljavaju $\delta_p(x)\mid d$. Stoga je broj elemenata reda $d$ među njima jednak
        
        $$
        N(d) = d - \sum_{e\mid d,~e\neq d} N(e) = d - \sum_{e\mid d,~e\neq d} \varphi(e) = \varphi(d).
        $$
        
        Druga jednakost je pretpostavka indukcije, a treća je svojstvo Eulerove funkcije. Matematičkom indukcijom zaključujemo da za sve $d\mid(p-1)$ postoji točno $\varphi(d)$ elemenata reda $d$.
        
        Posebno, za $d=p-1$ postoji točno $\varphi(p-1)$ elemenata reda $(p-1)$. Dakle, primitivni korijen modulo $p$ postoji.

    ???+ note "Lema 2"
        Za neparan prost broj $p$ i $e \in \mathbf{N}_+$ postoji primitivni korijen modulo $p^e$.

    ??? note "Dokaz"
        Dokaz se sastoji od tri koraka.
        
        **Prvi korak**: postoji primitivni korijen $g$ modulo $p$ takav da je $g^{p-1}\not\equiv 1\pmod{p^2}$.
        
        Uzmimo bilo koji primitivni korijen $g$ modulo $p$. Ako on ne zadovoljava uvjet, tj. ako je $g^{p-1}\equiv 1\pmod{p^2}$, tada se može pokazati da $g+p$ zadovoljava uvjet: $g+p$ je također primitivni korijen modulo $p$ i vrijedi
        
        $$
        \begin{aligned}
        (g+p)^{p-1} &\equiv \binom{p-1}{0}g^{p-1} + \binom{p-1}{1}g^{p-2}p \\
        &= g^{p-1} + g^{p-2}p(p-1) \\ 
        &\equiv 1 - pg^{p-2} \not\equiv 1 \pmod{p^2}.
        \end{aligned}
        $$
        
        **Drugi korak**: za gore odabrani $g$ i svaki $e\ge 1$ vrijedi $g^{\varphi(p^e)}\not\equiv 1\pmod{p^{e+1}}$.
        
        Izbor $g$ jamči da tvrdnja vrijedi za $e=1$. Pretpostavimo da tvrdnja vrijedi za $e$; dokazujemo da vrijedi i za $e+1$. Za svaki $e \ge 1$, prema Eulerovu teoremu, postoji cijeli broj $t$ takav da vrijedi
        
        $$
        g^{\varphi(p^e)} = 1 + t p^e
        $$
        
        Prema pretpostavci indukcije, $t\perp p$. Budući da je $\varphi(p^{e+1})=p\varphi(p^e)$, vrijedi
        
        $$
        g^{\varphi(p^{e+1})} = \left(g^{\varphi(p^{e})}\right)^p = (1 + t p^e)^p \equiv 1 + t p^{e+1} \pmod{p^{e+2}}.
        $$
        
        Zajedno s $t\perp p$ zaključujemo da je $g^{\varphi(p^{e+1})}\not\equiv 1\pmod{p^{e+2}}$. Matematičkom indukcijom tvrdnja vrijedi.
        
        **Treći korak**: gore odabrani $g$ primitivni je korijen modulo $p^e$ za svaki $e\ge 1$.
        
        Izbor $g$ jamči da tvrdnja vrijedi za $e=1$. Pretpostavimo da tvrdnja vrijedi za $e$; dokazujemo da vrijedi i za $e+1$. Označimo kraće $\delta_{p^{e+1}}(g)$ s $\delta$. Budući da je $g^\delta\equiv 1\pmod{p^{e+1}}$, nužno vrijedi i $g^\delta\equiv 1\pmod{p^e}$. Prema pretpostavci indukcije $\delta_{p^e}(g) = \varphi(p^e)$. Stoga prema gornjem [svojstvu 2](#ciklička-struktura-potencija) reda vrijedi $\varphi(p^e)\mid\delta$. Prema Eulerovu teoremu vrijedi $\delta\mid\varphi(p^{e+1})$. No $\varphi(p^{e+1})=p\varphi(p^e)$. Stoga postoje samo dvije mogućnosti: $\delta=\varphi(p^e)$ ili $\delta=\varphi(p^{e+1})$. Međutim, zaključak drugog koraka pokazuje da je $g^{\varphi(p^e)}\not\equiv 1\pmod{p^{e+1}}$. Dakle, mogućnost $\delta=\varphi(p^e)$ otpada. Jedina je mogućnost $\delta=\varphi(p^{e+1})$. To pokazuje da je $g$ primitivni korijen modulo $p^{e+1}$. Matematičkom indukcijom tvrdnja vrijedi za sve $e\ge 1$.

3.  $m=2p^{e}$, gdje je $p$ neparan prost broj, $e\in\mathbf N_+$.

    ???+ note "Lema 3"
        Za neparan prost broj $p$ i $e \in \mathbf{N}_+$ postoji primitivni korijen modulo $2p^e$.

    ??? note "Dokaz"
        Neka je $g$ primitivni korijen modulo $p^{e}$; tada je i $g+p^e$ primitivni korijen modulo $p^{e}$. Jedan od njih nužno je neparan; bez smanjenja općenitosti neka je to $g$. Očito je $(g,2p^e)=1$. Neka je $\delta=\delta_{2p^e}(g)$; treba dokazati da je $\delta=\varphi(2p^e)$. Prema Eulerovu teoremu, $\delta\mid\varphi(2p^e)$. Istodobno, po definiciji je $g^\delta\equiv 1\pmod{2p^e}$, pa je $g^\delta\equiv 1\pmod{p^e}$; stoga prema [svojstvu 2](#ciklička-struktura-potencija) reda i izboru $g$ vrijedi $\delta_{p^e}(g)=\varphi(p^e)\mid \delta$. Iz izraza za Eulerovu funkciju slijedi $\varphi(2p^e) = \varphi(p^e)$. Dakle, $\delta=\delta_{2p^e}(g)=\varphi(p^e)=\varphi(2p^e)$. To pokazuje da je $g$ primitivni korijen modulo $2p^e$.

4.  $m\ne 1,2,4,p^{e},2p^{e}$, gdje je $p$ neparan prost broj, $e\in\mathbf N_+$.

    ???+ note "Lema 4"
        Pretpostavimo da je $m\neq 1,2,4$ i da ne postoje neparan prost broj $p$ i pozitivni cijeli broj $e$ takvi da je $m=p^e$ ili $m=2p^e$. Tada primitivni korijen modulo $m$ ne postoji.

    ??? note "Dokaz"
        Za $m=2^e$ uz $e\ge 3$ pretpostavimo da primitivni korijen $g$ modulo $m$ postoji. Budući da je $g\perp m$, on je nužno neparan. Neka je $g=2k+1$ uz $k\in\mathbf N$; tada vrijedi
        
        $$
        \begin{aligned}
        g^{2^{e-2}}
        &=(2k+1)^{2^{e-2}} \\
        &\equiv 1 + \binom{2^{e-2}}{1}(2k) + \binom{{2^{e-2}}}{2}(2k)^2 \\
        &= 1 + 2^{e-1}k + 2^{e-1}(2^{e-2}-1)k^2 \\
        &= 1 + 2^{e-1}(k + (2^{e-2}-1)k^2) \\
        &\equiv 1 \pmod{2^{e}}.
        \end{aligned}
        $$
        
        U pretposljednjem retku, budući da $k$ i $(2^{e-2}-1)k^2$ imaju istu parnost, njihov je zbroj paran. Prema definiciji reda, $\delta_{2^{e}}(g)\le 2^{e-2}< \varphi(2^{e}) = 2^{e-1}$. To je u suprotnosti s pretpostavkom da je $g$ primitivni korijen. Kontradikcijom zaključujemo da takav primitivni korijen ne postoji.
        
        Pretpostavimo da $m$ zadovoljava navedene uvjete i da nije potencija broja $2$; tada nužno postoje $2 < m_1 < m_2$ takvi da je $m_1\perp m_2$ i $m=m_1m_2$. Pretpostavimo da primitivni korijen $g$ modulo $m$ postoji. Budući da je $g\perp m$, za $i=1,2$ vrijedi $g\perp m_i$. Prema Eulerovu teoremu,
        
        $$
        g^{\varphi(m_i)} \equiv 1 \pmod{m_i}.
        $$
        
        Budući da je $m_i > 2$, broj $\varphi(m_i)$ je paran, pa za $i=1,2$ vrijedi
        
        $$
        g^{\frac{1}{2}\varphi(m_1)\varphi(m_2)} \equiv 1 \pmod{m_i}.
        $$
        
        Prema [kineskom teoremu o ostatcima](./crt.md) vrijedi
        
        $$
        g^{\frac{1}{2}\varphi(m_1)\varphi(m_2)} \equiv 1 \pmod{m}.
        $$
        
        Budući da je još $\varphi(m)=\varphi(m_1)\varphi(m_2)$, prema definiciji reda vrijedi
        
        $$
        \delta_m(g) \le \frac{1}{2}\varphi(m_1)\varphi(m_2) = \dfrac{1}{2}\varphi(m) < \varphi(m).
        $$
        
        To je u suprotnosti s pretpostavkom da je $g$ primitivni korijen modulo $m$. Stoga, kontradikcijom, primitivni korijen modulo $m$ ne postoji.

Objedinjujući ova četiri slučaja, dobili smo nužan i dovoljan uvjet da broj ima primitivni korijen.

### Algoritam za pronalaženje primitivnog korijena

Za svaki modul $m$ za koji primitivni korijen postoji, da bismo našli njegov primitivni korijen $g$, dovoljno je nabrajati moguće pozitivne cijele brojeve i za svaki redom provjeriti je li primitivni korijen. Pri nabrajanju obično postoje dva pristupa: nabrajanje redom od manjih prema većima ili slučajno generiranje pozitivnih cijelih brojeva. Stvarna učinkovitost tih dvaju pristupa podjednaka je.

Pri nabrajanju redom od manjih prema većima dobiva se najmanji primitivni korijen $g_m$ modulo $m$, pa složenost dijela s nabrajanjem ovisi o veličini $g_m$. O tome postoje sljedeće ocjene:

-   Ocjena gornje ograde: Wang Yuan[^yuan1959note] i Burgess[^burgess1962character] dokazali su da za najmanji primitivni korijen prostog broja $p$ vrijedi $g_p=O\left(p^{0.25+\epsilon}\right)$, gdje je $\epsilon>0$. Cohen, Odoni i Stothers[^cohen1974least] te Elliott i Murata[^elliott1998least] dokazali su da ta ocjena vrijedi i za module $p^2$ odnosno $2p^2$, gdje je $p$ neparan prost broj. Budući da je za $e>2$ primitivni korijen modulo $p^2$ (odnosno $2p^2$) ujedno primitivni korijen modulo $p^e$ (odnosno $2p^e$), gornja ograda $O\left(p^{0.25+\epsilon}\right)$ za najmanji primitivni korijen vrijedi u svim slučajevima.
-   Ocjena donje ograde: Fridlender[^fridlender1949least] i Salié[^salie1949kleinsten] dokazali su da postoji $C>0$ takav da za beskonačno mnogo prostih brojeva $p$ najmanji primitivni korijen zadovoljava $g_p > C\log p$.
-   Ocjena prosječnog slučaja: Burgess i Elliott[^burgess1968average] dokazali su da je u prosječnom slučaju najmanji primitivni korijen prostog broja $p$ jednak $g_p=O((\log p)^2(\log\log p)^4)$. Elliott i Murata[^elliott1997average] nadalje su postavili slutnju da je prosječna vrijednost najmanjeg primitivnog korijena prostog broja $p$ konstanta te su numeričkom provjerom[^more-evidence] dobili da iznosi približno $4.926$. Potom su Elliott i Murata[^elliott1998least] tu slutnju proširili na slučaj modula $2p^2$.

Prema tim analizama, pri pronalaženju najmanjeg primitivnog korijena grubom silom složenost dijela s nabrajanjem $O(g_m(\log m)^2)$ prihvatljiva je.

Osim nabrajanja od manjih prema većima, primitivni korijen može se tražiti i slučajnim generiranjem pozitivnih cijelih brojeva i njihovom provjerom. Gustoća primitivnih korijena nije mala:[^density-prim-root]

$$
\dfrac{\varphi(\varphi(m))}{m} = \Omega\left(\dfrac{1}{\log\log m}\right).
$$

Stoga je pri traženju primitivnog korijena slučajnom metodom očekivana složenost dijela s nabrajanjem $O((\log m)^2\log\log m)$.

Treba napomenuti da je za provjeru primitivnog korijena potrebno poznavati rastav broja $\varphi(m)$ na proste faktore. Među [uobičajenim algoritmima za faktorizaciju](./pollard-rho.md) u algoritamskim natjecanjima i Pollardov rho algoritam, koji ima najbolju složenost, treba $O(m^{1/4+\epsilon})$ vremena. Stoga, dok god rastav broja $\varphi(m)$ na proste faktore nije poznat, bez obzira na način nabrajanja usko grlo složenosti pronalaženja primitivnog korijena jest korak faktorizacije, a ne dio s nabrajanjem i provjerom.

## Carmichaelova funkcija

Za razliku od reda elementa modulo $m$, koji je lokalan pojam, Carmichaelova funkcija globalan je pojam. Ona je najmanji zajednički period potencija svih cijelih brojeva relativno prostih s $m$.

???+ abstract "Carmichaelova funkcija"
    Za $m\in\mathbf N_+$ definiramo $\lambda(m)$ kao najmanji pozitivni cijeli broj $n$ za koji kongruencija $a^n\equiv 1\pmod m$ vrijedi za sve $a\perp m$. Funkcija $\lambda:\mathbf N_+\to\mathbf N_+$ naziva se **Carmichaelova funkcija**.

Prema [svojstvu 2](#ciklička-struktura-potencija), to da $a^n\equiv 1\pmod m$ vrijedi za sve $a\perp m$ znači da $\delta_m(a)\mid n$ vrijedi za sve $a\perp m$. Drugim riječima, pozitivni cijeli broj $n$ koji zadovoljava taj uvjet nužno je zajednički višekratnik svih $\delta_m(a)$. Stoga je najmanji takav $n$ upravo njihov najmanji zajednički višekratnik:

$$
\lambda(m) = \operatorname{lcm}\{\delta_m(a) : a\perp m\}.
$$

To se često koristi i kao ekvivalentna definicija Carmichaelove funkcije.

Uzastopnom primjenom [svojstva 5](#red-umnoška) zaključujemo da nužno postoji neki element $a\perp m$ takav da je $\delta_m(a)=\lambda(m)$. Stoga se gornji izraz može zapisati i kao

$$
\lambda(m) = \max\{\delta_m(a) : a\perp m\}.
$$

Element $a\perp m$ koji postiže taj maksimum naziva se i **$\lambda$‑primitivni korijen** modulo $m$. On postoji za svaki modul $m$.

### Rekurzivna formula

Carmichaelova funkcija jest [aritmetička funkcija](./basic.md#teorijsko-brojevne-funkcije). U ovom odjeljku razmatramo jednu njezinu rekurzivnu formulu i iz nje izvodimo još jedan dokaz teorema o postojanju primitivnog korijena.

Iako nije multiplikativna funkcija, pri računanju Carmichaelove funkcije relativno prosti faktori također se mogu obraditi zasebno.

???+ note "Lema"
    Za relativno proste pozitivne cijele brojeve $m_1,m_2$ vrijedi $\lambda(m_1m_2)=[\lambda(m_1),\lambda(m_2)]$.

??? note "Dokaz"
    Neka su $a_1$ i $a_2$ redom $\lambda$‑primitivni korijeni modulo $m_1$ i modulo $m_2$. Neka je $m=m_1m_2$; prema [kineskom teoremu o ostatcima](./crt.md) postoji $a\perp m$ takav da $a\equiv a_i\pmod{m_i}$ vrijedi za $i=1,2$. Budući da je $a^{\lambda(m)}\equiv 1\pmod m$, za $i=1,2$ vrijedi $a_i^{\lambda(m)} \equiv 1\pmod{m_i}$, pa prema [svojstvu 2](#ciklička-struktura-potencija) i izboru $a_i$ vrijedi $\lambda(m_i)=\delta_{m_i}(a_i)\mid \lambda(m)$. To pokazuje da $[\lambda(m_1),\lambda(m_2)]\mid\lambda(m)$.
    
    Obrnuto, za svaki $a\perp m$ i $i=1,2$ vrijedi $a^{[\lambda(m_1),\lambda(m_2)]} \equiv 1 \pmod{m_i}$. Primjenom kineskog teorema o ostatcima dobivamo da $a^{[\lambda(m_1),\lambda(m_2)]} \equiv 1 \pmod{m}$ vrijedi za sve $a\perp m$. Prema definiciji Carmichaelove funkcije, $\lambda(m)\mid [\lambda(m_1),\lambda(m_2)]$.
    
    Time vrijedi jednakost iz tvrdnje.

Stoga u nastavku treba samo izračunati vrijednosti Carmichaelove funkcije u potencijama prostih brojeva. Najprije obrađujemo slučaj potencija broja $2$.

???+ note "Lema"
    Za $m=2^e$ uz $e\in\mathbf N_+$ vrijedi $\lambda(2)=1$, $\lambda(4)=2$, a za $e\ge 3$ vrijedi $\lambda(m)=2^{e-2}$.

??? note "Dokaz"
    Slučajeve $m=2,4$ dovoljno je provjeriti zasebno. Za $m=2^e$ uz $e\ge 3$ najprije ponovimo prvi dio dokaza gornje [leme 4](#teorem-o-postojanju-primitivnog-korijena), čime dobivamo $\lambda(m)\le 2^{e-2}$. Zatim je dovoljno dokazati da postoji element reda $2^{e-2}$. U tu svrhu vrijedi
    
    $$
    5^{2^{e-3}} = (1 + 2^2)^{2^{e-3}} \equiv 1 + 2^2\times 2^{e-3} = 1 + 2^{e-1} \not\equiv 1 \pmod{2^e}.
    $$
    
    To pokazuje da $\delta_m(5)\nmid 2^{e-3}$, a budući da $\delta_m(5) \mid 2^{e-2}$, $5$ može biti jedino element reda $2^{e-2}$. To pokazuje da je $\lambda(m)=2^{e-2}$.

U dokazu ove leme zapravo smo dobili opis strukture reduciranog sustava ostataka modulo $2^e$:

???+ note "Korolar"
    Neka je modul $2^e$ uz $e \ge 2$. Tada je svaki neparan broj kongruentan točno jednom cijelom broju oblika $\pm 5^k$, gdje je $k\in\mathbf N$ i $k < 2^{e-2}$. Drugim riječima, brojevi $\pm 1,\pm 5,\cdots,\pm 5^{2^{e-2}-1}$ međusobno su nekongruentni i tvore reducirani sustav ostataka.

??? note "Dokaz"
    Lako se provjerava da tvrdnja vrijedi za $e=2$. Za $e \ge 3$, budući da smo u prethodnom dokazu već dobili da je red broja $5$ modulo $2^e$ jednak $2^{e-2}$, brojevi $1,5,\cdots,5^{2^{e-2}-1}$ međusobno su nekongruentni. Budući da svi ti cijeli brojevi daju ostatak $1$ modulo $4$, a njihovi suprotni brojevi daju ostatak $3$ modulo $4$, brojevi $\pm 1,\pm 5,\cdots,\pm 5^{2^{e-2}-1}$ međusobno su nekongruentni modulo $2^e$. Budući da ih ima ukupno $2^{e-1}$, što je upravo veličina reduciranog sustava ostataka modulo $2^{e}$, oni tvore sam reducirani sustav ostataka.

Zatim obrađujemo slučaj potencija neparnih prostih brojeva.

???+ note "Lema"
    Za $m=p^e$, gdje je $p$ neparan prost broj i $e\in\mathbf N_+$, vrijedi $\lambda(m)=p^{e-1}(p-1)$.

??? note "Dokaz"
    Najprije dokazujemo da tvrdnja vrijedi za $e=1$, tj. kada je $m=p$ neparan prost broj. U tu svrhu, prema definiciji Carmichaelove funkcije, svi cijeli brojevi $a$ relativno prosti s $p$ rješenja su kongruencije $x^{\lambda(p)}\equiv 1\pmod{p}$. Modulo $p$ ta kongruencija ima ukupno $p-1$ međusobno različitih rješenja. Prema [Lagrangeovu teoremu](./congruence-equation.md#kongruencije-po-prostom-modulu) vrijedi $p-1\le\lambda(p)$. Istodobno, Eulerov teorem zahtijeva $\lambda(p)\mid\varphi(p)=p-1$. Dakle, $\lambda(p)=p-1$.
    
    Za $m=p^e$ uz $e> 1$ možemo početi dokazom da je $1+p$ element reda $p^{e-1}$. U tu svrhu vrijedi
    
    $$
    (1+p)^{p^{e-1}} \equiv 1,\quad (1+p)^{p^{e-2}} \equiv 1 + p^{e-1} \not\equiv 1 \pmod{p^e}.
    $$
    
    Dakle, $\delta_m(1+p)=p^{e-1}$. Nadalje, neka je $g$ primitivni korijen modulo $p$; tada, budući da je $g^{\delta_m(g)}\equiv 1 \pmod{p}$, prema [svojstvu 2](#ciklička-struktura-potencija) reda vrijedi $p-1\mid\delta_m(g)$. Prema definiciji Carmichaelove funkcije i Eulerovu teoremu vrijedi
    
    $$
    p^{e-1}(p-1) \mid [\delta_m(1+p),\delta_m(g)] \mid \lambda(m) \mid \varphi(m) = p^{e-1}(p-1).
    $$
    
    Dakle, $\lambda(m)=p^{e-1}(p-1)$.

Jednostavnim sažimanjem rezultata ovog odjeljka dobivamo rekurzivnu formulu za Carmichaelovu funkciju:

???+ note "Teorem"
    Za svaki pozitivni cijeli broj $m$ vrijedi
    
    $$
    \lambda(m) = \begin{cases}
    \varphi(m), & \text{if }m=1,2,4,p^e\text{ for odd prime }p\text{ and }e \ge 1,\\
    \frac{1}{2}\varphi(m), &\text{if }m=2^e,~e\ge 3,\\
    \operatorname{lcm}\{\lambda(p_1^{e_1}),\lambda(p_2^{e_2}),\cdots,\lambda(p_s^{e_s})\}, &\text{if }m = p_1^{e_1}p_2^{e_2}\cdots p_s^{e_s}\text{ for distinct }p_1,p_2,\cdots,p_s.
    \end{cases}
    $$

Pomoću te rekurzivne formule može se pojačati prethodni rezultat:

???+ note "Korolar"
    Za pozitivne cijele brojeve $m_1,m_2$ vrijedi $\lambda([m_1,m_2])=[\lambda(m_1),\lambda(m_2)]$.

Usporedbom definicija primitivnog korijena i Carmichaelove funkcije vidimo da primitivni korijen modulo $m$ postoji ako i samo ako je $\lambda(m)=\varphi(m)$. Iz rekurzivne formule za Carmichaelovu funkciju lako se indukcijom izvodi sljedeći rezultat:

???+ note "Korolar"
    Primitivni korijen modulo $m$ postoji ako i samo ako je $m=1,2,4,p^e,2p^e$, gdje je $p$ neparan prost broj i $e\in\mathbf N_+$.

Budući da se u dokazu rekurzivne formule u ovom odjeljku nije koristio teorem o postojanju primitivnog korijena, ovo predstavlja još jedan dokaz tog teorema.

### Carmichaelovi brojevi

Pomoću Carmichaelove funkcije mogu se razmatrati svojstva i raspodjela Carmichaelovih brojeva (OEIS: [A002997](https://oeis.org/A002997)). To su složeni brojevi koje [Fermatov test prostosti](./prime.md#fermatov-test-prostosti) nikada ne može ispravno isključiti.

???+ abstract "Carmichaelov broj"
    Za složeni broj $n$, ako za sve cijele brojeve $a\perp n$ vrijedi kongruencija $a^{n-1} \equiv 1 \pmod n$, tada se $n$ naziva **Carmichaelov broj**.

Najmanji Carmichaelov broj jest $561 = 3 \times 11 \times 17$.

Prema definiciji Carmichaelove funkcije, složeni broj $n$ Carmichaelov je broj ako i samo ako $\lambda(n)\mid n-1$, gdje je $\lambda(n)$ Carmichaelova funkcija. Nadalje, dobiva se sljedeći način provjere je li složeni broj $n$ Carmichaelov broj:

???+ note "Korseltov kriterij[^korselt1899probleme]"
    Složeni broj $n$ Carmichaelov je broj ako i samo ako $n$ nema kvadratnih faktora i za svaki prosti faktor $p$ broja $n$ vrijedi $(p-1) \mid (n-1)$.

??? note "Dokaz"
    Najprije dokazujemo nužnost uvjeta. Pretpostavimo da $\lambda(n)\mid (n-1)$. Pregledom rekurzivne formule za Carmichaelovu funkciju vidimo da, ako $n$ ima kvadratni faktor $p^2$, nužno vrijedi $p\mid \lambda(n)$. No $p\nmid (n-1)$, što je kontradikcija. Slično, za svaki prosti faktor $p$ broja $n$ rekurzivna formula za Carmichaelovu funkciju pokazuje da $(p-1)\mid \lambda(n)$, pa vrijedi i $(p-1) \mid (n-1)$.
    
    Zatim dokazujemo dovoljnost uvjeta. Budući da je $n$ složen broj bez kvadratnih faktora, ima barem dva različita prosta faktora, među kojima je nužno i neki neparan prosti faktor $p$; iz $(p-1)\mid(n-1)$ slijedi da je $n-1$ paran, pa je $n$ nužno neparan. Za neparan složen broj $n$ bez kvadratnih faktora, prema rekurzivnoj formuli za Carmichaelovu funkciju, vrijedi $\lambda(n)=\operatorname{lcm}\{p-1:p\mid n\}$. Stoga, čim $(p-1) \mid (n-1)$ vrijedi za sve proste faktore $p$, nužno vrijedi $\lambda(n)\mid (n-1)$.

Polazeći od tog kriterija, mogu se izvesti neka jednostavna svojstva Carmichaelovih brojeva:

???+ note "Korolar"
    Carmichaelovi brojevi neparni su, nemaju kvadratnih faktora i imaju barem $3$ različita prosta faktora.

??? note "Dokaz"
    Prva dva svojstva izravno slijede iz Korseltova kriterija i njegova dokaza. Za treće svojstvo dovoljno je još dokazati da umnožak $n=p_1p_2$ dvaju različitih prostih brojeva $p_1,p_2$ nikada nije Carmichaelov broj. Pretpostavimo da je $n=p_1p_2$ Carmichaelov broj. Prema Korseltovu kriteriju, $(p_i-1)\mid (n-1)$. No vrijedi
    
    $$
    n-1=p_1p_2-1\equiv p_2-1 \pmod{p_1-1}.
    $$
    
    Dakle, $(p_1-1)\mid(p_2-1)$. Analogno, $(p_2-1)\mid(p_1-1)$. Drugim riječima, $p_1=p_2$. To je u suprotnosti s pretpostavkom. Stoga Carmichaelov broj $n$ ima barem $3$ različita prosta faktora.

Pomoću analitičke teorije brojeva mogu se dobiti i neka svojstva raspodjele Carmichaelovih brojeva. Neka je $C(n)$ broj Carmichaelovih brojeva manjih ili jednakih $n$. Alford, Granville i Pomerance[^alford1994infinitely] dokazali su da za dovoljno velik $n$ vrijedi $C(n)>n^{2/7}$. Iz toga slijedi da Carmichaelovih brojeva ima beskonačno mnogo. Prije toga je Erdős[^erdos1956pseudoprimes] već dokazao da je $C(n) < n\exp\left(-c\dfrac{\ln n\ln\ln\ln n}{\ln\ln n}\right)$, gdje je $c$ konstanta. Stoga je raspodjela Carmichaelovih brojeva (u usporedbi s prostim brojevima) vrlo rijetka. Zapravo vrijedi[^pinchcarmichael] $C(10^9)=646$, $C(10^{18})=1~401~644$.

## Literatura i napomene

-   [Primitive root modulo n - Wikipedia](https://en.wikipedia.org/wiki/Primitive_root_modulo_n)
-   [The order of a unit - Course Notes](https://crypto.stanford.edu/pbc/notes/numbertheory/order.html)
-   [The primitive root theorem - Amin Witno's notes](http://witno.com/philadelphia/notes/won5.pdf)
-   [Carmichael function - Wikipedia](https://en.wikipedia.org/wiki/Carmichael_function)
-   [Carmichael's Lambda Function - Brilliant Math & Science Wiki](https://brilliant.org/wiki/carmichaels-lambda-function/)
-   [Carmichael number - Wikipedia](https://en.wikipedia.org/wiki/Carmichael_number)
-   [Carmichael Number - Wolfram MathWorld](https://mathworld.wolfram.com/CarmichaelNumber.html)

[^yuan1959note]: Wang Y. "On the least primitive root of a prime." (in Chinese). Acta Math Sinica, 1959, 4: 432–441; English transl. in*Sci. Sinica*, 1961, 10: 1–14.

[^burgess1962character]: BURGESS, David A. "On character sums and primitive roots." Proceedings of the London Mathematical Society, 1962, 3.1: 179-192.

[^cohen1974least]: Cohen, S. D., R. W. K. Odoni, and W. W. Stothers. "On the least primitive root modulo $p^2$." Bulletin of the London Mathematical Society 6, no. 1 (1974): 42-46.

[^elliott1998least]: Elliott, P. D. T. A., and L. Murata. "The least primitive root mod $2p^2$." Mathematika 45, no. 2 (1998): 371-379.

[^fridlender1949least]: FRIDLENDER, V. R. "On the least n-th power non-residue." Dokl. Akad. Nauk SSSR. 1949. p. 351-352.

[^salie1949kleinsten]: SALIÉ, Hans. "Über den kleinsten positiven quadratischen Nichtrest nach einer Primzahl." Mathematische Nachrichten, 1949, 3.1: 7-8.

[^burgess1968average]: Burgess, D. A., and P. D. T. A. Elliott. "The average of the least primitive root." Mathematika 15, no. 1 (1968): 39-50.

[^elliott1997average]: Elliott, Peter DTA, and Leo Murata. "On the average of the least primitive root modulo p." Journal of The London Mathematical Society 56, no. 3 (1997): 435-454.

[^more-evidence]: Više rezultata može se naći na stranici [Least prime primitive root of prime numbers](https://sweet.ua.pt/tos/p_roots.html).

[^density-prim-root]: Ako primitivni korijen modulo $m$ postoji, tada je $\varphi(m)\ge\dfrac{1}{3}m$, pri čemu se jednakost postiže samo za $m=2\times 3^e~(e\in\mathbf N_+)$. Nadalje, za $m > 2$ za Eulerovu funkciju $\varphi(m)$ vrijedi ocjena $\varphi(m)>\dfrac{m}{e^{\gamma}\log\log m+\frac{3}{\log\log m}}$. Kombiniranjem tih dviju činjenica dobiva se izraz iz teksta. O toj ocjeni Eulerove funkcije vidi rad Rosser, J. Barkley, and Lowell Schoenfeld. "Approximate formulas for some functions of prime numbers." Illinois Journal of Mathematics 6, no. 1 (1962): 64-94.

[^korselt1899probleme]: Korselt, A. R. (1899). "Problème chinois." L'Intermédiaire des Mathématiciens. 6: 142–143.

[^alford1994infinitely]: W. R. Alford; Andrew Granville; Carl Pomerance (1994). "There are Infinitely Many Carmichael Numbers." Annals of Mathematics. 140 (3): 703–722.

[^erdos1956pseudoprimes]: Erdős, P. (1956). "On pseudoprimes and Carmichael numbers." Publ. Math. Debrecen. 4 (3–4): 201–206.

[^pinchcarmichael]: PINCH, Richard GE. The Carmichael numbers up to ${10}^{20}$.
