---
title: Osnove teorije brojeva
---

Ovaj članak daje kratak uvod u početni dio teorije brojeva.

## Djeljivost

???+ note "Definicija"
    Neka su $a,b\in\mathbf{Z}$, $a\ne 0$. Ako $\exists q\in\mathbf{Z}$ takav da je $b=aq$, kažemo da je $b$ **djeljiv** s $a$ i pišemo $a\mid b$; ako $b$ nije djeljiv s $a$, pišemo $a\nmid b$.

Svojstva djeljivosti:

-   $a\mid b\iff-a\mid b\iff a\mid-b\iff|a|\mid|b|$
-   $a\mid b\land b\mid c\implies a\mid c$
-   $a\mid b\land a\mid c\iff\forall x,y\in\mathbf{Z}, a\mid(xb+yc)$
-   $a\mid b\land b\mid a\implies b=\pm a$
-   Neka je $m\ne0$; tada $a\mid b\iff ma\mid mb$.
-   Neka je $b\ne0$; tada $a\mid b\implies|a|\le|b|$.
-   Neka je $a\ne0,b=qa+c$; tada $a\mid b\iff a\mid c$.

### Djelitelji

???+ note "Definicija"
    Ako $a\mid b$, kažemo da je $b$ **višekratnik** od $a$, a $a$ **djelitelj** od $b$.

$0$ je višekratnik svakog cijelog broja različitog od $0$. Za cijeli broj $b\ne0$, $b$ ima samo konačno mnogo djelitelja.

Trivijalni djelitelji (trivijalni faktori): za cijeli broj $b\ne0$, $\pm1$ i $\pm b$ trivijalni su djelitelji od $b$. Kada je $b=\pm1$, $b$ ima samo dva trivijalna djelitelja.

Za cijeli broj $b\ne 0$, ostali djelitelji od $b$ nazivaju se pravi djelitelji (pravi faktori, netrivijalni djelitelji, netrivijalni faktori).

Svojstva djelitelja:

-   Neka je cijeli broj $b\ne0$. Kada $d$ prolazi svim djeliteljima od $b$, tada i $\dfrac{b}{d}$ prolazi svim djeliteljima od $b$.
-   Neka je cijeli broj $b\gt 0$; tada kada $d$ prolazi svim pozitivnim djeliteljima od $b$, i $\dfrac{b}{d}$ prolazi svim pozitivnim djeliteljima od $b$.

U konkretnim zadacima, **ako nije drukčije rečeno, djelitelj uvijek znači pozitivan djelitelj.**

## Dijeljenje s ostatkom

???+ note "Ostatak"
    Neka su $a,b$ dva zadana cijela broja, $a\ne0$. Neka je $d$ zadani cijeli broj. Tada sigurno postoji jedinstven par cijelih brojeva $q$ i $r$ takav da je $b=qa+r,d\le r<|a|+d$.

Bez obzira na to koju vrijednost cijeli broj $d$ poprima, $r$ se općenito naziva ostatak. $a\mid b$ ekvivalentno je s $a\mid r$.

U pravilu se za $d$ uzima $0$; tada se jednakost $b=qa+r,0\le r<|a|$ naziva dijeljenje s ostatkom. Ostatak $r$ ovdje se naziva najmanji nenegativni ostatak.

Ostatak se često uzima i na dva druga uobičajena načina:

-   apsolutno najmanji ostatak: $d$ je suprotan broj polovine apsolutne vrijednosti od $a$, tj. $b=qa+r,-\dfrac{|a|}{2}\le r<|a|-\dfrac{|a|}{2}$;
-   najmanji pozitivni ostatak: $d$ je $1$, tj. $b=qa+r,1\le r<|a|+1$.

Ostatak pri dijeljenju s ostatkom samo je najmanji nenegativni ostatak. **Ako nije drukčije rečeno, ostatak uvijek znači najmanji nenegativni ostatak.**

Svojstva ostatka:

-   Pri dijeljenju bilo kojeg cijelog broja pozitivnim cijelim brojem $a$ ostatak je sigurno jedan i samo jedan od ovih $a$ brojeva: od $0$ do $(a-1)$.
-   Pri dijeljenju $a$ uzastopnih cijelih brojeva pozitivnim cijelim brojem $a$ dobiva se točno gore navedenih $a$ ostataka. Posebno, sigurno postoji jedan i samo jedan među njima koji je djeljiv s $a$.

## Najveći zajednički djelitelj i najmanji zajednički višekratnik

Definicije četiriju pojmova – zajednički djelitelj, zajednički višekratnik, najveći zajednički djelitelj i najmanji zajednički višekratnik – vidi u članku [Najveći zajednički djelitelj](./gcd.md).

???+ warning "Upozorenje"
    Neki autori smatraju da najveći zajednički djelitelj brojeva $0$ i $0$ nije definiran, dok ga ostali autori u pravilu smatraju jednakim $0$. Implementacija u C++ STL-u koristi potonje, tj. smatra da je najveći zajednički djelitelj brojeva $0$ i $0$ jednak $0$[^gcdcpp].

Najveći zajednički djelitelj ima sljedeća svojstva:

-   $(a_1,\dots,a_n)=(|a_1|,\dots,|a_n|)$;
-   $(a,b)=(b,a)$;
-   ako je $a\ne 0$, tada je $(a,0)=(a,a)=|a|$;
-   $(bq+r,b)=(r,b)$;
-   $(a_1,\dots,a_n)=((a_1,a_2),a_3,\dots,a_n)$. Štoviše, $\forall 1<k<n-1,~(a_1,\dots,a_n)=((a_1,\dots,a_k),(a_{k+1},\dots,a_n))$;
-   za cijele brojeve $a_1,\dots,a_n$ koji nisu svi jednaki $0$ i cijeli broj $m$ različit od nule vrijedi $(ma_1,\dots,ma_n)=|m|(a_1,\dots,a_n)$;
-   za cijele brojeve $a_1,\dots,a_n$ koji nisu svi jednaki $0$, ako je $(a_1,\dots,a_n)=d$, tada je $(a_1/d,\dots,a_n/d)=1$;
-   $(a^n,b^n)=(a,b)^n$.

Najveći zajednički djelitelj ima i sljedeća svojstva povezana s relativnom prostošću:

-   ako $b|ac$ i $(a,b)=1$, tada $b\mid c$;
-   ako $b|c$, $a|c$ i $(a,b)=1$, tada $ab\mid c$;
-   ako je $(a,b)=1$, tada je $(a,bc)=(a,c)$;
-   ako je $(a_i,b_j)=1,~\forall 1\leq i\leq n,1\leq j\leq m$, tada je $\left(\prod_i a_i,\prod_j b_j\right)=1$. Posebno, ako je $(a,b)=1$, tada je $(a^n,b^m)=1$;
-   za cijele brojeve $a_1,\dots,a_n$, ako $\exists v\in \mathbf{Z},~\prod_i a_i=v^m$ i $(a_i,a_j)=1,~\forall i\ne j$, tada $\forall 1\leq i\leq n,~\sqrt[m]{a_i}\in\mathbf{Z}$.

Najmanji zajednički višekratnik ima sljedeća svojstva:

-   $[a_1,\dots,a_n]=[|a_1|,\dots,|a_n|]$;
-   $[a,b]=[b,a]$;
-   ako je $a\ne 0$, tada je $[a,1]=[a,a]=|a|$;
-   ako $a\mid b$, tada je $[a,b]=|b|$;
-   $[a_1,\dots,a_n]=[[a_1,a_2],a_3,\dots,a_n]$. Štoviše, $\forall 1<k<n-1,~[a_1,\dots,a_n]=[[a_1,\dots,a_k],[a_{k+1},\dots,a_n]]$;
-   ako $a_i\mid m,~\forall 1\leq i\leq n$, tada $[a_1,\dots,a_n]\mid m$;
-   $[ma_1,\dots,ma_n]=|m|[a_1,\dots,a_n]$;
-   $[a,b,c][ab,bc,ca]=[a,b][b,c][c,a]$;
-   $[a^n,b^n]=[a,b]^n$.

Najveći zajednički djelitelj i najmanji zajednički višekratnik mogu se kombinirati u mnoge zanimljive jednakosti, npr.:

-   $(a,b)[a,b]=|ab|$;
-   $(ab,bc,ca)[a,b,c]=|abc|$;
-   $\dfrac{(a,b,c)^2}{(a,b)(b,c)(a,c)}=\dfrac{[a,b,c]^2}{[a,b][b,c][a,c]}$.

Sva se ta svojstva mogu dokazati iz definicije ili pomoću [teorema o jedinstvenoj faktorizaciji](#osnovni-teorem-aritmetike), pri čemu su dokazi koji koriste teorem o jedinstvenoj faktorizaciji lakši za razumijevanje.

### Relativno prosti brojevi

???+ note "Definicija"
    Ako je $(a_1,a_2)=1$, kažemo da su $a_1$ i $a_2$ **relativno prosti** (**uzajamno prosti**).
    
    Ako je $(a_1,\ldots,a_k)=1$, kažemo da su $a_1,\ldots,a_k$ **relativno prosti** (**uzajamno prosti**).

Ako je više cijelih brojeva relativno prosto, nisu nužno relativno prosti u parovima. Na primjer, $6$, $10$ i $15$ relativno su prosti, ali nikoja dva od njih nisu relativno prosta.

Svojstva relativno prostih brojeva i teorija najvećeg zajedničkog djelitelja: Bézoutov teorem (Bézout's identity). Vidi [Bézoutov teorem](./bezouts.md).

### Euklidov algoritam

Algoritam uzastopnog dijeljenja jest algoritam koji se naziva i Euklidov algoritam. Vidi [Najveći zajednički djelitelj](./gcd.md).

## Prosti i složeni brojevi

Algoritme vezane uz proste brojeve vidi u članku [Prosti brojevi](./prime.md).

???+ note "Definicija"
    Neka je cijeli broj $p\ne0,\pm1$. Ako $p$ osim trivijalnih djelitelja nema drugih djelitelja, kažemo da je $p$ **prost broj** (**ireducibilan broj**).
    
    Ako je cijeli broj $a\ne0,\pm 1$ i $a$ nije prost, kažemo da je $a$ **složen broj**.

$p$ i $-p$ uvijek su ili oba prosta ili oba složena. **Ako nije drukčije rečeno, prost broj uvijek znači pozitivan prost broj.**

Ako je faktor cijelog broja prost broj, taj se prost broj naziva prosti faktor (prosti djelitelj) tog cijelog broja.

Jednostavna svojstva prostih i složenih brojeva:

-   Cijeli broj $a$ veći od $1$ složen je ako i samo ako se $a$ može prikazati kao umnožak cijelih brojeva $d$ i $e$ ($1<d,e<a$).
-   Ako prost broj $p$ ima djelitelj $d$ veći od $1$, tada je $d=p$.
-   Cijeli broj $a$ veći od $1$ sigurno se može prikazati kao umnožak prostih brojeva.
-   Za složen broj $a$ sigurno postoji prost broj $p\le\sqrt{a}$ takav da $p\mid a$.
-   Prostih brojeva ima beskonačno mnogo.
-   Svi prosti brojevi veći od $3$ mogu se prikazati u obliku $6n\pm 1$[^ref1].

## Osnovni teorem aritmetike

???+ note "Osnovna lema aritmetike"
    Neka je $p$ prost broj i $p\mid a_1a_2$. Tada vrijedi barem jedno od $p\mid a_1$ i $p\mid a_2$.

Malo izmijenjen obrat osnovne leme aritmetike daje još jednu definiciju prostog broja.

???+ note "Druga definicija prostog broja"
    Za cijeli broj $p\ne 0,\pm 1$, ako za sve cijele brojeve $a_1,a_2$ koji zadovoljavaju $p\mid a_1a_2$ vrijedi $p\mid a_1$ ili $p\mid a_2$, kažemo da je $p$ prost broj.

??? tip "Savjet"
    Motivacija za ovu definiciju može se pronaći u članku o [prostim idealima](../algebra/ring-theory.md#素理想).

???+ note "Osnovni teorem aritmetike (teorem o jedinstvenoj faktorizaciji)"
    Neka je $a$ pozitivan cijeli broj. Tada nužno postoji prikaz
    
    $$
    a=p_1p_2\cdots p_s
    $$
    
    gdje su $p_j(1\le j\le s)$ prosti brojevi. Štoviše, taj je prikaz jedinstven do na poredak faktora.

???+ note "Kanonski rastav na proste faktore"
    Spojimo li u gornjem prikazu jednake proste brojeve, dobivamo
    
    $$
    a={p_1}^{\alpha_1}{p_2}^{\alpha_2}\cdots{p_s}^{\alpha_s},p_1<p_2<\cdots<p_s
    $$
    
    što se naziva kanonski rastav pozitivnog cijelog broja $a$ na proste faktore.

Osnovni teorem aritmetike i osnovna lema aritmetike dva su ekvivalentna teorema.

## Kongruencija

???+ note "Definicija"
    Neka je cijeli broj $m\ne0$. Ako $m\mid(a-b)$, $m$ nazivamo **modul** (**modulom**), kažemo da je $a$ kongruentan $b$ modulo $m$, a $b$ je **ostatak** od $a$ modulo $m$. Pišemo $a\equiv b\pmod m$.
    
    Inače $a$ nije kongruentan $b$ modulo $m$ i $b$ nije ostatak od $a$ modulo $m$. Pišemo $a\not\equiv b\pmod m$.
    
    Takva se jednakost naziva kongruencija modulo $m$, kraće **kongruencija**.

Prema svojstvima djeljivosti, gornja je kongruencija ekvivalentna i s $a\equiv b\pmod{(-m)}$.

U nastavku je, ako nije drukčije rečeno, modul uvijek **pozitivan cijeli broj**.

$b$ u kongruenciji ostatak je od $a$ modulo $m$; taj se pojam potpuno podudara s ostatkom pri dijeljenju. Ograničavanjem raspona od $b$ dobivaju se, redom, najmanji nenegativni ostatak, apsolutno najmanji ostatak i najmanji pozitivni ostatak od $a$ modulo $m$.

Svojstva kongruencije:

-   Kongruencija je [relacija ekvivalencije](../order-theory.md#二元关系), tj. kongruencija ima svojstva
    -   refleksivnosti: $a\equiv a\pmod m$;
    -   simetričnosti: ako je $a\equiv b\pmod m$, tada je $b\equiv a\pmod m$;
    -   tranzitivnosti: ako je $a\equiv b\pmod m,b\equiv c\pmod m$, tada je $a\equiv c\pmod m$.
-   Linearne operacije: ako su $a,b,c,d\in\mathbf{Z},m\in\mathbf{N}^*,a\equiv b\pmod m,c\equiv d\pmod m$, tada vrijedi:
    -   $a\pm c\equiv b\pm d\pmod m$;
    -   $a\times c\equiv b\times d\pmod m$.
-   Neka su $f(x)=\sum_{i=0}^n a_ix^i$ i $g(x)=\sum_{i=0}^n b_ix^i$ dva polinoma s cjelobrojnim koeficijentima, $m\in\mathbf{N}^*$ i $a_i\equiv b_i\pmod m,~0\leq i\leq n$; tada za svaki cijeli broj $x$ vrijedi $f(x)\equiv g(x)\pmod m$. Štoviše, ako je $s\equiv t\pmod m$, tada je $f(s)\equiv g(t)\pmod m$.
-   Ako su $a,b\in\mathbf{Z},k,m\in\mathbf{N}^*,a\equiv b\pmod m$, tada je $ak\equiv bk\pmod{mk}$.
-   Ako su $a,b\in\mathbf{Z},d,m\in\mathbf{N}^*,d\mid a,d\mid b,d\mid m$, tada kad vrijedi $a\equiv b\pmod m$, vrijedi i $\dfrac{a}{d}\equiv\dfrac{b}{d}\left(\bmod\;{\dfrac{m}{d}}\right)$.
-   Ako su $a,b\in\mathbf{Z},d,m\in\mathbf{N}^*,d\mid m$, tada kad vrijedi $a\equiv b\pmod m$, vrijedi i $a\equiv b\pmod d$.
-   Ako su $a,b\in\mathbf{Z},d,m\in\mathbf{N}^*$, tada kad vrijedi $a\equiv b\pmod m$, vrijedi $(a,m)=(b,m)$. Ako $d$ dijeli $m$ i jedan od brojeva $a,b$, tada $d$ nužno dijeli i drugi od brojeva $a,b$.

Postoji još jedno svojstvo – multiplikativni inverz. Vidi [Modularni inverz](./inverse.md).

## Klase kongruencije i sustavi ostataka

Radi lakšeg izlaganja, za skupove $A,B$ i element $r$ uvodimo sljedeće oznake:

-   $r+A:=\{r+a:a\in A\}$;
-   $rA:=\{ra:a\in A\}$;
-   $A+B:=\{a+b:a\in A,b\in B\}$;
-   $AB:=\{ab:a\in A,b\in B\}$.

???+ note "Klasa kongruencije"
    Za cijeli broj $m$ različit od nule podijelimo sve cijele brojeve u $|m|$ u parovima disjunktnih skupova tako da su bilo koja dva broja iz istog skupa kongruentna modulo $m$; svaki od tih $|m|$ skupova nazivamo **klasa kongruencije** ili **klasa ostataka** modulo $m$. S $r\bmod m$ označavamo klasu kongruencije modulo $m$ koja sadrži cijeli broj $r$.
    
    Nije teško dokazati da za svaki cijeli broj $m$ različit od nule takva podjela sigurno postoji i da je jedinstvena.

Iz definicije klase kongruencije slijedi:

-   $r\bmod m=\{r+km:k\in\mathbf{Z}\}$;
-   $r\bmod m=s\bmod m\iff r\equiv s\pmod m$;
-   za sve $r,s\in\mathbf{Z}$ vrijedi ili $r\bmod m=s\bmod m$ ili $(r\bmod m)\cap (s\bmod m)=\varnothing$;
-   ako $m_1\mid m$, tada za svaki cijeli broj $r$ vrijedi $r+m\mathbf{Z}\subseteq r+m_1\mathbf{Z}$.

Uočimo da je kongruencija relacija ekvivalencije, pa su klase kongruencije upravo klase ekvivalencije relacije kongruencije.

Skup svih klasa kongruencije modulo $m$ označavamo sa $\mathbf{Z}_m$, tj.

$$
\mathbf{Z}_m:=\{r\bmod m:0\leq r<m\}
$$

Lako se vidi:

-   za svaki cijeli broj $a$ vrijedi $a+\mathbf{Z}_m=\mathbf{Z}_m$;
-   za svaki cijeli broj $b$ relativno prost s $m$ vrijedi $b\mathbf{Z}_m=\mathbf{Z}_m$.

Iz definicije [kvocijentne grupe](../algebra/group-theory.md#商群) slijedi $\mathbf{Z}_m=\mathbf{Z}/m\mathbf{Z}$, pa se $\mathbf{Z}_m$ ponekad označava i sa $\mathbf{Z}/m\mathbf{Z}$.

Iz [Dirichletova principa](../combinatorics/drawer-principle.md) slijedi:

-   Među bilo kojih $m+1$ cijelih brojeva sigurno postoje dva kongruentna modulo $m$.
-   Postoji $m$ cijelih brojeva koji u parovima nisu kongruentni modulo $m$.

Na temelju toga dajemo definiciju potpunog sustava ostataka:

???+ note "(Potpuni) sustav ostataka"
    Za $m$ cijelih brojeva $a_1,a_2,\dots,a_m$, ako za svaki broj $x$ postoji jedan i samo jedan $a_i$ takav da su $x$ i $a_i$ kongruentni modulo $m$, tih $m$ cijelih brojeva $a_1,a_2,\dots,a_m$ nazivamo **potpuni sustav ostataka** modulo $m$, kraće **sustav ostataka**.

Također možemo definirati sljedeće sustave modulo $m$:

-   najmanji nenegativni (potpuni) sustav ostataka: $0,\dots,m-1$;
-   najmanji pozitivni (potpuni) sustav ostataka: $1,\dots,m$;
-   apsolutno najmanji (potpuni) sustav ostataka: $-\lfloor m/2\rfloor,\dots,-\lfloor -m/2\rfloor-1$;
-   najveći nepozitivni (potpuni) sustav ostataka: $-m+1,\dots,0$;
-   najveći negativni (potpuni) sustav ostataka: $-m,\dots,-1$.

Ako nije drukčije rečeno, u pravilu koristimo samo najmanji nenegativni sustav ostataka.

Uočimo da vrijedi sljedeća tvrdnja:

-   U bilo kojoj klasi kongruencije modulo $m$, za bilo koja dva cijela broja $a_1,a_2$ iz nje vrijedi $(a_1,m)=(a_2,m)$.

Promotrimo klasu kongruencije $r\bmod m$; ako je $(r,m)=1$, tada su svi elementi te klase relativno prosti s $m$, što upućuje na to da bismo na sličan način mogli upoznati strukturu skupa svih cijelih brojeva relativno prostih s $m$.

???+ note "Reducirana klasa kongruencije"
    Za klasu kongruencije $r\bmod m$, ako je $(r,m)=1$, tu klasu nazivamo **reducirana klasa kongruencije** ili **reducirana klasa ostataka**.
    
    Broj reduciranih klasa ostataka modulo $m$ označavamo s $\varphi(m)$ i nazivamo ga [Eulerova funkcija](./euler-totient.md).

Skup svih reduciranih klasa kongruencije modulo $m$ označavamo sa $\mathbf{Z}_m^*$, tj.

$$
\mathbf{Z}_m^*:=\{r\bmod m:0\leq r<m,(r,m)=1\}
$$

???+ warning "Upozorenje"
    Za svaki cijeli broj $a$ i cijeli broj $b$ relativno prost s $m$ vrijedi $b\mathbf{Z}_m^*=\mathbf{Z}_m^*$, ali $a+\mathbf{Z}_m^*$ nije nužno jednako $\mathbf{Z}_m^*$. Po tome se razlikuje od $\mathbf{Z}_m$.

Iz [Dirichletova principa](../combinatorics/drawer-principle.md) slijedi:

-   Među bilo kojih $\varphi(m)+1$ cijelih brojeva relativno prostih s $m$ sigurno postoje dva kongruentna modulo $m$.
-   Postoji $\varphi(m)$ cijelih brojeva relativno prostih s $m$ koji u parovima nisu kongruentni modulo $m$.

Na temelju toga dajemo definiciju reduciranog sustava ostataka:

???+ note "Reducirani sustav ostataka"
    Za $t=\varphi(m)$ cijelih brojeva $a_1,a_2,\dots,a_t$, ako je $(a_i,m)=1,~\forall 1\leq i\leq t$ i ako za svaki broj $x$ koji zadovoljava $(x,m)=1$ postoji jedan i samo jedan $a_i$ takav da su $x$ i $a_i$ kongruentni modulo $m$, tih $t$ cijelih brojeva $a_1,a_2,\dots,a_t$ nazivamo **reducirani sustav ostataka**, **suženi sustav ostataka** ili **pojednostavljeni sustav ostataka** modulo $m$.

Slično možemo definirati i pojmove kao što je najmanji nenegativni reducirani sustav ostataka.

Ako nije drukčije rečeno, u pravilu koristimo samo najmanji nenegativni reducirani sustav ostataka.

### Sastavljanje sustava ostataka

Za pozitivan cijeli broj $m$ vrijedi sljedeći teorem:

-   Ako je $m=m_1m_2,~1\leq m_1,m_2$ i ako su $Z_{m_1},Z_{m_2}$ redom **potpuni** sustavi ostataka modulo $m_1,m_2$, tada za svaki $a$ relativno prost s $m_1$ vrijedi da je

    $$
    Z_m=aZ_{m_1}+m_1Z_{m_2}.
    $$

    **potpuni** sustav ostataka modulo $m$. Štoviše, ako je $m=\prod_{i=1}^k m_i,~1\leq m_1,m_2,\dots,m_k$ i ako su $Z_{m_1},\dots,Z_{m_k}$ redom **potpuni** sustavi ostataka modulo $m_1,\dots,m_k$, tada je

    $$
    Z_m=\sum_{i=1}^k\left(\prod_{j=1}^{i-1}m_j\right)Z_{m_i}.
    $$

    **potpuni** sustav ostataka modulo $m$.

???+ note "Dokaz"
    Dovoljno je dokazati da za sve $x,x'\in Z_{m_1}$, $y,y'\in Z_{m_2}$ koji zadovoljavaju $ax+m_1y\equiv ax'+m_1y'\pmod{m_1m_2}$ vrijedi
    
    $$
    ax+m_1y=ax'+m_1y'.
    $$
    
    Doista, iz $m_1\mid m_1m_2$ imamo $ax+m_1y\equiv ax'+m_1y'\pmod{m_1}$, dakle $ax\equiv ax'\pmod{m_1}$, a iz $(a,m_1)=1$ slijedi $x\equiv x'\pmod{m_1}$, pa je $x=x'$.
    
    Nadalje, $m_1y\equiv m_1y'\pmod{m_1m_2}$, pa je $y\equiv y'\pmod{m_2}$, tj. $y=y'$.
    
    Stoga je
    
    $$
    ax+m_1y=ax'+m_1y'.
    $$

-   Ako je $m=m_1m_2,~1\leq m_1,m_2,(m_1,m_2)=1$ i ako su $Z_{m_1}^*,Z_{m_2}^*$ redom **reducirani** sustavi ostataka modulo $m_1,m_2$, tada je

    $$
    Z_m^*=m_2Z_{m_1}^*+m_1Z_{m_2}^*.
    $$

    **reducirani** sustav ostataka modulo $m$.

???+ tip "Savjet"
    Taj je teorem ekvivalentan dokazu da je Eulerova funkcija [multiplikativna funkcija](#multiplikativne-funkcije).

???+ note "Dokaz"
    Neka su $Z_{m_1},Z_{m_2}$ redom potpuni sustavi ostataka modulo $m_1,m_2$; već smo dokazali da je
    
    $$
    Z_m=m_2Z_{m_1}+m_1Z_{m_2}
    $$
    
    potpuni sustav ostataka modulo $m$. Neka je $M=\{a\in Z_m:(a,m)=1\}\subseteq Z_m$; očito je $M$ reducirani sustav ostataka modulo $m$, pa je dovoljno dokazati $M=Z_m^*$.
    
    Očito je $Z_m^*\subseteq Z_m$.
    
    Uzmimo bilo koji $m_2x+m_1y\in M$, gdje je $x\in Z_{m_1}$ i $y\in Z_{m_2}$; vrijedi $(m_2x+m_1y,m_1m_2)=1$, a iz $(m_1,m_2)=1$ dobivamo
    
    $$
    1=(m_2x+m_1y,m_1)=(m_2x,m_1)=(x,m_1),
    $$
    
    $$
    1=(m_2x+m_1y,m_2)=(m_1y,m_2)=(y,m_2).
    $$
    
    Stoga je $x\in Z_{m_1}^*$ i $y\in Z_{m_2}^*$, tj. $M\subseteq Z_m^*$.
    
    Uzmimo bilo koji $m_2x+m_1y\in Z_m^*$, gdje je $x\in Z_{m_1}^*$ i $y\in Z_{m_2}^*$; vrijedi $(x,m_1)=1$ i $(y,m_2)=1$, a iz $(m_1,m_2)=1$ dobivamo
    
    $$
    (m_2x+m_1y,m_1)=(m_2x,m_1)=(x,m_1)=1,
    $$
    
    $$
    (m_2x+m_1y,m_2)=(m_1y,m_2)=(x,m_2)=1,
    $$
    
    pa slijedi $(m_2x+m_1y,m_1m_2)=1$, tj. $Z_m^*\subseteq M$.
    
    Zaključno,
    
    $$
    Z_m^*=m_2Z_{m_1}^*+m_1Z_{m_2}^*.
    $$
    
    jest **reducirani** sustav ostataka modulo $m$.

## Teorijsko-brojevne funkcije

Teorijsko-brojevna funkcija (zvana i aritmetička funkcija) jest funkcija kojoj je domena skup pozitivnih cijelih brojeva. Teorijsko-brojevna funkcija može se promatrati i kao niz.

### Multiplikativne funkcije

???+ note "Definicija"
    U teoriji brojeva, ako funkcija $f(n)$ zadovoljava $f(1)=1$ i $f(xy)=f(x)f(y)$ za sve relativno proste $x, y \in\mathbf{N}^*$, tada je $f(n)$ **multiplikativna funkcija**.
    
    U teoriji brojeva, ako funkcija $f(n)$ zadovoljava $f(1)=1$ i $f(xy)=f(x)f(y)$ za sve $x, y \in\mathbf{N}^*$, tada je $f(n)$ **potpuno multiplikativna funkcija**.

#### Svojstva

Ako su $f(x)$ i $g(x)$ multiplikativne funkcije, tada su i sljedeće funkcije multiplikativne:

$$
\begin{aligned}
h(x)&=f(x^p)\\
h(x)&=f^p(x)\\
h(x)&=f(x)g(x)\\
h(x)&=\sum_{d\mid x}f(d)g\left(\dfrac{x}{d}\right)
\end{aligned}
$$

Za pozitivan cijeli broj $x$ neka je njegov jedinstveni rastav na proste faktore $x=\prod p_i^{k_i}$, gdje su $p_i$ prosti brojevi.

Ako je $F(x)$ multiplikativna funkcija, tada je $F(x)=\prod F(p_i^{k_i})$.

Ako je $F(x)$ potpuno multiplikativna funkcija, tada je $F(x)=\prod F(p_i^{k_i})=\prod F(p_i)^{k_i}$.

#### Primjeri

-   Jedinična funkcija: $\varepsilon(n)=[n=1]$. (potpuno multiplikativna)
-   Funkcija identiteta: $\operatorname{id}_k(n)=n^k$; $\operatorname{id}_{1}(n)$ obično se kraće piše $\operatorname{id}(n)$. (potpuno multiplikativna)
-   Konstantna funkcija: $1(n)=1$. (potpuno multiplikativna)
-   Funkcija djelitelja: $\sigma_{k}(n)=\sum_{d\mid n}d^{k}$. $\sigma_{0}(n)$ obično se kraće piše $d(n)$ ili $\tau(n)$, a $\sigma_{1}(n)$ obično se kraće piše $\sigma(n)$.
-   Eulerova funkcija: $\varphi(n)=\sum_{i=1}^n[(i,n)=1]$.
-   Möbiusova funkcija: $\mu(n)=\begin{cases}1&n=1\\0&\exists d>1,d^{2}\mid n\\(-1)^{\omega(n)}&\text{otherwise}\end{cases}$, gdje $\omega(n)$ označava broj različitih prostih faktora od $n$.

### Aditivne funkcije

???+ note "Definicija"
    U teoriji brojeva, ako funkcija $f(n)$ zadovoljava $f(1)=0$ i $f(xy)=f(x)+f(y)$ za sve relativno proste $x, y \in\mathbf{N}^*$, tada je $f(n)$ **aditivna funkcija**.
    
    U teoriji brojeva, ako funkcija $f(n)$ zadovoljava $f(1)=0$ i $f(xy)=f(x)+f(y)$ za sve $x, y \in\mathbf{N}^*$, tada je $f(n)$ **potpuno aditivna funkcija**.

???+ warning "Aditivna funkcija"
    Aditivna funkcija u ovom odjeljku odnosi se na aditivnu funkciju u teoriji brojeva (additive function) i treba je razlikovati od aditivnog preslikavanja (additive map) u algebri.

#### Svojstva

Za pozitivan cijeli broj $x$ neka je njegov jedinstveni rastav na proste faktore $x=\prod p_i^{k_i}$, gdje su $p_i$ prosti brojevi.

Ako je $F(x)$ aditivna funkcija, tada je $F(x)=\sum F(p_i^{k_i})$.

Ako je $F(x)$ potpuno aditivna funkcija, tada je $F(x)=\sum F(p_i^{k_i})=\sum F(p_i)\cdot k_i$.

#### Primjeri

Radi jednostavnosti izlaganja, neka je $\mathbf P$ skup svih prostih brojeva.

-   Kratnost od $p$ u rastavu na proste faktore: $\nu_p(n) = \max\{k\in\mathbf N: p^k\mid n\}$, gdje je $p\in\mathbf P$. (potpuno aditivna)
-   Broj svih prostih faktora: $\Omega(n)=\sum_{p \in\mathbf P} \nu_p(n)$. (potpuno aditivna)
-   Broj različitih prostih faktora: $\omega(n)=\sum_{p \in\mathbf P} [p \mid n]$.
-   Zbroj svih prostih faktora: $a_0(n)=\sum_{p \in\mathbf P} \nu_p(n)\cdot p$. (potpuno aditivna)
-   Zbroj različitih prostih faktora: $a_1(n)=\sum_{p \in\mathbf P} [p \mid n] \cdot p$.

## Funkcije pod i strop

Za realan broj $x$ definiramo **funkciju pod** (floor function, najveće cijelo) i **funkciju strop** (ceiling function) redom kao

$$
\lfloor x\rfloor = \max\{k\in\mathbf Z:k\le x\},~\lceil x\rceil = \min\{k\in\mathbf Z:k\ge x\}.
$$

Pomoću funkcije pod realan se broj može rastaviti na cijeli i razlomljeni dio: $x = \lfloor x\rfloor + \{x\}$. Pritom $\{x\}$ označava razlomljeni dio od $x$.

Funkcije pod i strop imaju sljedeća osnovna svojstva ($x\in\mathbf R,~n\in\mathbf Z$):

-   $x\in\mathbf Z \iff x = \lfloor x\rfloor = \lceil x\rceil$.
-   $\lceil x\rceil - \lfloor x\rfloor = [x\notin\mathbf Z]$.
-   $x - 1 < \lfloor x\rfloor \le x \le \lceil x\rceil < x + 1$.
-   $\lfloor -x\rfloor = -\lceil x\rceil,~\lceil -x\rceil = -\lfloor x\rfloor$.
-   $\lfloor x + n\rfloor = \lfloor x\rfloor + n,~\lceil x + n\rceil = \lceil x \rceil + n$.
-   $\lfloor x\rfloor$ i $\lceil x\rceil$ monotono su neopadajuće funkcije od $x$.

Pri dokazivanju jednakosti s funkcijom pod (strop) često se koriste sljedeći ekvivalentni oblici ($x\in\mathbf R,~n\in\mathbf Z$):

-   $\lfloor x\rfloor = n \iff n \le x < n + 1 \iff x - 1 < n \le x$.
-   $\lceil x\rceil = n \iff n - 1 < x \le n \iff x \le n < x + 1$.

Pri dokazivanju nejednakosti s funkcijom pod (strop) često se koriste sljedeći ekvivalentni oblici ($x\in\mathbf R,~n\in\mathbf Z$):

-   $x < n \iff \lfloor x\rfloor < n$.
-   $n < x \iff n < \lceil x\rceil$.
-   $x \le n \iff \lceil x\rceil \le n$.
-   $n \le x \iff n \le \lfloor x\rfloor$.

Svojstva koja se odnose na zbroj i razliku ($x,y\in\mathbf R$):

-   $\lfloor x\rfloor + \lfloor y\rfloor \le \lfloor x + y\rfloor \le \lfloor x\rfloor + \lfloor y\rfloor + 1$, pri čemu vrijedi točno jedna jednakost.
-   $\lceil x\rceil +\lceil y\rceil -1\leq \lceil x+y\rceil \leq \lceil x\rceil +\lceil y\rceil$, pri čemu vrijedi točno jedna jednakost.
-   $\lfloor|x - y|\rfloor \le |\lfloor x\rfloor - \lfloor y\rfloor| \le \lceil|x - y|\rceil$.
-   $\lfloor|x - y|\rfloor \le |\lceil x\rceil - \lceil y\rceil| \le \lceil|x-y|\rceil$.

Svojstva koja se odnose na kvocijent ($x\in\mathbf R,~n\in\mathbf Z,~m\in\mathbf Z_+$):

-   $\left\lceil\dfrac{n}{m}\right\rceil = \left\lfloor\dfrac{n+m-1}{m}\right\rfloor,~\left\lfloor\dfrac{n}{m}\right\rfloor = \left\lceil\dfrac{n-m+1}{m}\right\rceil$.
-   $\left\lfloor\dfrac{x + n}{m} \right\rfloor = \left\lfloor\dfrac{\lfloor x\rfloor + n}{m} \right\rfloor,~\left\lceil\dfrac{x + n}{m} \right\rceil = \left\lceil\dfrac{\lceil x\rceil + n}{m} \right\rceil$.
-   $\left\lfloor\dfrac{\lfloor x/n\rfloor}{m}\right\rfloor = \left\lfloor\dfrac{x}{nm}\right\rfloor,~\left\lceil\dfrac{\lceil x/n\rceil}{m}\right\rceil = \left\lceil\dfrac{x}{nm}\right\rceil$.
-   Za $x > 0$ vrijedi $\displaystyle\left\lfloor\dfrac{x}{m}\right\rfloor = \sum_{k=1}^{\lfloor x\rfloor}[m\mid k]$.

Pritom se drugo i treće svojstvo mogu smatrati izravnim posljedicama sljedećeg rezultata:

-   Neka je $f$ neprekidna strogo rastuća funkcija takva da, čim je $f(x)\in\mathbf Z$, vrijedi $x\in\mathbf Z$. Tada je

    $$
    \lfloor f(x)\rfloor = \lfloor f(\lfloor x\rfloor)\rfloor,~ \lceil f(x)\rceil = \lceil f(\lceil x\rceil)\rceil.
    $$

    ??? note "Dokaz"
        Zbog simetrije dovoljno je dokazati prvu jednakost. Ako je $x$ cijeli broj, tvrdnja je očita. Inače je $\lfloor x\rfloor < x$. Iz monotonosti funkcije $f$ i funkcije pod slijedi $\lfloor f(x)\rfloor \ge \lfloor f(\lfloor x\rfloor)\rfloor$. Ako jednakost ne vrijedi, neka je $y = \lfloor f(x)\rfloor$; on zadovoljava $\lfloor f(\lfloor x\rfloor)\rfloor < y \le \lfloor f(x)\rfloor$, što je ekvivalentno s $f(\lfloor x\rfloor) < y \le f(x)$. Iz neprekidnosti funkcije $f$ slijedi da postoji $\lfloor x\rfloor < x_0 \le x$ takav da je $f(x_0)=y$. Budući da je $y\in\mathbf Z$, vrijedi $x_0\in\mathbf Z$, što je u suprotnosti s definicijom $\lfloor x\rfloor$. Stoga jednakost vrijedi, tj. $\lfloor f(x)\rfloor = \lfloor f(\lfloor x\rfloor)\rfloor$.

Na kraju, skupina rezultata o sumama koje sadrže funkcije pod i strop ($x\in\mathbf R,~n\in\mathbf Z,~m\in\mathbf Z_+$):

-   $n = \left\lfloor\dfrac{n}{2}\right\rfloor + \left\lceil\dfrac{n}{2}\right\rceil$.
-   $n = \left\lfloor\dfrac{n}{m} \right\rfloor + \left\lfloor\dfrac{n+1}{m} \right\rfloor + \cdots + \left\lfloor\dfrac{n+m-1}{m} \right\rfloor$.
-   $n = \left\lceil\dfrac{n}{m} \right\rceil + \left\lceil\dfrac{n-1}{m} \right\rceil + \cdots + \left\lceil\dfrac{n-m+1}{m} \right\rceil$.
-   $\lfloor mx\rfloor = \lfloor x\rfloor + \left\lfloor x+\dfrac{1}{m}\right\rfloor + \cdots + \left\lfloor x+\dfrac{m-1}{m}\right\rfloor$.
-   $\lceil mx\rceil = \lceil x\rceil + \left\lceil x - \dfrac{1}{m}\right\rceil + \cdots + \left\lceil x - \dfrac{m-1}{m}\right\rceil$.
-   Kada je $m\perp n$, vrijedi $\displaystyle\sum_{k=1}^{m-1}\left\lfloor\dfrac{kn}{m}\right\rfloor=\dfrac{1}{2}(n-1)(m-1)$.
-   Kada je $m\perp n$, vrijedi $\displaystyle\sum_{k=1}^{m-1}\left\lceil\dfrac{kn}{m}\right\rceil=\dfrac{1}{2}(n+1)(m-1)$.

Izvod tih, pa i općenitijih suma sličnog oblika može se pogledati na stranici [Algoritam nalik Euklidovu](./euclidean.md).

Više svojstava i primjena funkcija pod i strop može se pogledati na sljedećim stranicama:

-   Operacija modulo: $n\bmod m = n - \left\lfloor\dfrac{n}{m}\right\rfloor m$. Može se iskoristiti za [optimizaciju cjelobrojne operacije modulo](./mod-arithmetic.md#srodni-algoritmi).
-   Dokaz [zakona kvadratnog reciprociteta](./quad-residue.md#kvadratni-zakon-reciprociteta) pomoću Gaussove leme.
-   [Blokovsko dijeljenje po cjelobrojnom kvocijentu](./sqrt-decomposition.md), osobito dio s dokazima njegovih svojstava.
-   [Legendreova formula](./factorial.md#legendreova-formula) za računanje eksponenta prostog faktora u faktorijelu.
-   [Beattyjevi nizovi](../game-theory/impartial-game.md#wythoff-游戏), Rayleighov teorem i Wythoffova igra.

## Literatura i napomene

-   潘承洞，潘承彪．初等数论．北京大学出版社．(Pan Chengdong, Pan Chengbiao. Elementarna teorija brojeva. Peking University Press.)
-   [Floor and ceiling functions - Wikipedia](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions)
-   Graham, Ronald L., Donald E. Knuth, and Oren Patashnik. "Concrete mathematics: a foundation for computer science." (1989).

[^ref1]: [Are all primes (past 2 and 3) of the forms 6n+1 and 6n-1?](https://primes.utm.edu/notes/faq/six.html)

[^gcdcpp]: [std::gcd - cppreference.com](https://en.cppreference.com/w/cpp/numeric/gcd)
