---
title: WBLT
---

## Uvod

**Weight Balanced Leafy Tree**, u nastavku **WBLT**, vrsta je balansiranog stabla koja u odnosu na druga balansirana stabla ima prije svega prednosti jednostavne implementacije i male konstante. Podržava operacije nad intervalima i može se perzistentno implementirati.

Weight Balanced Leafy Tree, kako mu i ime kaže, kombinacija je Weight Balanced Tree (težinski balansiranog stabla) i Leafy Tree (lisnatog stabla).

U Weight Balanced Tree svaki čvor pohranjuje veličinu podstabla ispod sebe, a visina stabla jamči se održavanjem omjera veličina lijevog i desnog podstabla unutar određenog raspona.

U Leafy Tree izvorne se informacije pohranjuju samo u **listovima**, dok unutarnji čvorovi služe samo za održavanje informacija o djeci i oblika strukture podataka. Dobro poznato segmentno stablo također je vrsta Leafy Tree.

![](images/leafy-tree-1.svg)

Stabla u ovom tekstu uvijek označavaju binarno Leafy Tree, tj. svaki čvor ima ili $0$ ili $2$ djeteta. $n$ u ovom tekstu označava broj listova stabla. Stablo s $n$ listova ima ukupno $2n-1$ čvorova, pa je prostor koji WBLT zauzima $\Theta(n)$.

## Osnovna struktura i održavanje ravnoteže

Ovaj odjeljak predstavlja osnovnu strukturu WBLT-a, definira pojam $\alpha$‑ravnoteže stabla i objašnjava kako se ravnoteža stabla održava rotacijama ili spajanjem.

### Informacije u čvoru

Za implementaciju osnovnog WBLT-a dovoljno je u svakom čvoru zabilježiti sljedeće informacije:

-   `lc[x]`, `rc[x]`: lijevo i desno dijete;
-   `sz[x]`: broj listova u podstablu s korijenom $x$.

Za implementaciju balansiranog stabla WBLT-om u svakom čvoru treba zabilježiti i informacije vezane uz ključ:

-   `val[x]`: ključ u čvoru $x$.

Budući da samo listovi stvarno pohranjuju ključeve, informacije pohranjene u ostalim čvorovima dobivaju se spajanjem informacija njihove djece, radi lakših kasnijih upita.

Na primjer, jedan uobičajen način spajanja jest da se u čvor pohrani veći od ključeva dvaju djece. Tako svaki čvor pohranjuje maksimum ključeva svih listova u podstablu kojem je korijen. Na temelju toga ažuriranje informacija čvora izgleda ovako:

???+ example "Primjer koda"
    ```cpp
    --8<-- "docs/ds/code/wblt/wblt-1.cpp:push-up"
    ```

Naravno, po potrebi se može implementirati i odgovarajuća funkcija `push_down(x)`.

### Pomoćne funkcije

Osim osnovnog održavanja informacija u čvorovima, WBLT obično treba implementirati i sljedeće pomoćne funkcije za upravljanje memorijom:

-   `new_node()`: stvara novi čvor;
-   `del_node(x)`: briše čvor $x$;
-   `new_leaf(v)`: stvara novi list s ključem $v$;
-   `join(x, y)`: povezuje podstabla, tj. stvara novi čvor $z$ s $x$ i $y$ kao lijevim i desnim djetetom;
-   `cut(x)`: rastavlja podstablo, tj. dohvaća dvoje djece čvora $x$ i briše čvor $x$.

Ako se implementacija WBLT-a snažno oslanja na rastavljanje i povezivanje podstabala, stvara se mnogo novih čvorova i oslobađa jednak broj starih. Ako se stari nepotrebni čvorovi ne recikliraju na vrijeme, prostor više neće biti linearan. Slijedi implementacija tih pomoćnih funkcija pomoću polja:

???+ example "Primjer koda"
    ```cpp
    --8<-- "docs/ds/code/wblt/wblt-1.cpp:helper"
    ```

Nakon što su te pomoćne funkcije enkapsulirane, u daljnjim funkcijama nema razlike između implementacije poljima i implementacije pokazivačima.

### Pojam ravnoteže

Za stablo možemo definirati njegov **stupanj ravnoteže** u unutarnjem čvoru $x$ kao

$$
\rho(x) = \dfrac{\min\{w(T_{\operatorname{left}(x)}),w(T_{\operatorname{right}(x)})\}}{w(T_x)}.
$$

Pritom $T_x$ označava podstablo s korijenom $x$, $w(\cdot)$ težinu podstabla (broj njegovih listova), a $\operatorname{left}(x)$ i $\operatorname{right}(x)$ lijevo i desno dijete čvora $x$. Posebno, za listove propisujemo $\rho(x)=1/2$.

Za $\alpha\in(0,1/2]$, ako je stupanj ravnoteže $\rho(x)\ge\alpha$ u nekom čvoru $x$, kažemo da je taj čvor **$\alpha$‑uravnotežen**. Ako je stablo $\alpha$‑uravnoteženo u svakom čvoru, kažemo da je stablo **$\alpha$‑uravnoteženo**. Skup takvih stabala označavamo s $BB[\alpha]$. Stablo je **$\alpha$‑uravnoteženo** ako i samo ako je list, ili je $\alpha$‑uravnoteženo u korijenu i oba su mu podstabla $\alpha$‑uravnotežena.

Očita je prednost $\alpha$‑uravnoteženog stabla to što mu je visina $O(\log n)$. Naime, svakim korakom od lista prema korijenu broj listova u podstablu poveća se barem na $1/(1-\alpha)$ puta prethodni, pa je moguće napraviti samo $O(\log_{\frac{1}{1-\alpha}}n) = O(\log n)$ koraka. To jamči da je u $\alpha$‑uravnoteženom stablu složenost jednog upita uvijek strogo $O(\log n)$, a konstanta algoritma obrnuto je proporcionalna s $\log(1/(1-\alpha))$ (s bazom $2$). Kad je $\alpha$ u razumnom rasponu danom u nastavku, ta je konstanta otprilike $2\sim 3.5$.

Ravnoteža WBLT-a obično se može održavati rotacijama ili spajanjem. Kod WBLT-a implementiranog na bilo koji od ta dva načina složenost pojedinog umetanja, brisanja i sličnih operacija strogo je $O(\log n)$. Međutim, za razliku od [Treapa](./treap.md) s fiksnim prioritetima, struktura WBLT-a nije jedinstvena, pa se strukture stabala dobivenih tim dvama načinima održavanja razlikuju, iako to ne utječe na njihovu upotrebu. Naravno, ravnoteža se može održavati i strategijom sličnom [scapegoat stablu](./sgt.md), ponovnom izgradnjom uz amortiziranu složenost $O(\log n)$, ali se tako gube prednosti WBLT-a poput perzistentnosti i operacija nad intervalima, pa se to ne preporučuje.

U nastavku su redom predstavljeni načini održavanja ravnoteže rotacijama i spajanjem te su implementirane odgovarajuće funkcije za održavanje ravnoteže i spajanje. Nakon što su te funkcije enkapsulirane, dva načina održavanja ravnoteže više se ne razlikuju u daljnjoj konkretnoj implementaciji balansiranog stabla. Štoviše, bez obzira na odabrani način, vremenska složenost jedne operacije održavanja ravnoteže je $O(1)$, a složenost jednog spajanja stabala $T_1$ i $T_2$ je $O\left(\left|\log\dfrac{w(T_1)}{w(T_2)}\right|\right)$.

???+ info "Izostavljanje oznake težine"
    Za održavanje ravnoteže stabla dovoljno je zadržati informaciju o težini podstabala. Stoga, radi jednostavnijeg izražavanja, u sljedeća dva odjeljka o održavanju ravnoteže oznake stabla i njegove težine koristit će se naizmjenično. Na primjer, težina podstabla $x$ također se označava s $x$, a ne s $w(x)$. Slično, stablo dobiveno spajanjem podstabala $x$ i $y$ također se označava svojom težinom i piše izravno kao stablo $x+y$.

### Održavanje rotacijama

Rotacije u WBLT-u potpuno su jednake [rotacijama u Treapu](./treap.md#rotacija) i može se koristiti potpuno ista strategija rotiranja kao u Treapu. Naravno, i sama rotacija može se promatrati kao postupak preraspodjele težina podstabala, pa se može obaviti i rastavljanjem i povezivanjem podstabala. Rezultati obiju implementacija potpuno su jednaki, ali je druga implementacija pogodnija za perzistentni WBLT.

???+ example "Primjer koda"
    === "Bez oslanjanja na povezivanje"
        ```cpp
        --8<-- "docs/ds/code/wblt/wblt-1.cpp:rotate-not-by-joining"
        ```
    
    === "Oslanjanjem na povezivanje"
        ```cpp
        --8<-- "docs/ds/code/wblt/wblt-1.cpp:rotate-by-joining"
        ```

Pretpostavimo da nakon neke operacije izmjene stabla odozdo prema gore vraćamo ravnotežu stabla. Sada lijevo i desno podstablo $x$ i $y$ više nisu međusobno uravnoteženi, ali su svako za sebe uravnoteženi. Bez smanjenja općenitosti neka je desno podstablo $y$ prelagano, tj. $y<\alpha(x+y)$. Oblik stabla tada je kao kod lijevog stabla na slici.

![](images/wblt-balance.svg)

Naivna strategija održavanja ravnoteže jest rotirati $x$ do korijena; tako njegovo prijašnje desno dijete $w$ zajedno s $y$ postaje desno dijete novog stabla, a njegovo prijašnje lijevo dijete $z$ postaje lijevo dijete novog stabla. To odgovara premještanju težine $w$ s lijeve strane izvornog stabla na njegovu desnu stranu. Ako je težina $w$ prikladna, ta operacija vraća ravnotežu stabla. Tako dobiveno stablo prikazano je kao desno stablo na slici.

Međutim, ako je sam $w$ pretežak, ta operacija može premjestiti previše težine u desno podstablo, pa lijevo podstablo novog stabla postaje prelagano, tj. $z<\alpha(x+y)$. U tom slučaju, budući da su težine podstabala $z$ i $y$ premale, preostaje samo rastaviti $w$ na dva podstabla i povezati ih redom sa $z$ i $y$, tako da postanu dva podstabla novog stabla. To odgovara tome da najprije čvor $w$ rotiramo na mjesto čvora $x$, a zatim ga rotiramo do korijena. I ovdje se može očekivati da tako dobiveno stablo bude uravnoteženo; njegov je oblik kao kod srednjeg stabla na slici.

Te se dvije strategije rotiranja nazivaju jednostruka i dvostruka rotacija. Izbor između jednostruke i dvostruke rotacije ovisi uglavnom o udjelu podstabla $w$ u odnosu na podstablo $x$, tj. postoji prag $\beta$ takav da

-   kad je $w\le\beta x$, treba odabrati jednostruku rotaciju;
-   kad je $w>\beta x$, treba odabrati dvostruku rotaciju.

Teškoća je u izboru praga $\beta$, što zahtijeva nešto konkretnih računa. Blum i Mehlhorn dokazali su da za parametre[^wrong-range]

$$
\alpha\in\left(\dfrac{2}{11},1-\dfrac{\sqrt{2}}{2}\right]\approx(0.182,0.292],~\beta=\frac{1}{2-\alpha},
$$

gore opisana kombinacija jednostruke i dvostruke rotacije može održati ravnotežu WBLT-a koji je izgubio ravnotežu zbog jednog umetanja ili brisanja.

??? note "Dokaz"
    Treba dokazati da se, ako stablo nakon jednog umetanja ili brisanja izgubi ravnotežu, gore opisanom strategijom ravnoteža može vratiti. Uz gornju sliku, neka je
    
    $$
    \rho_1 = \dfrac{y}{x+y}, ~\rho_2 = \dfrac{w}{x}, ~\rho_3 = \dfrac{v}{w}.
    $$
    
    Tada vrijedi $\rho_1<\alpha\le\rho_2,\rho_3\le 1-\alpha$. Ovdje postoji i skriveni uvjet na raspon vrijednosti $\rho_1$:
    
    -   ako je gubitak ravnoteže uzrokovan umetanjem jednog elementa, mora vrijediti
    
        $$
        \dfrac{y}{x-1+y} \ge \alpha \implies \rho_1 \ge \dfrac{\alpha y}{y+\alpha} \ge \dfrac{\alpha}{1+\alpha}.
        $$
    -   ako je gubitak ravnoteže uzrokovan brisanjem jednog elementa, mora vrijediti
    
        $$
        \dfrac{y+1}{x+y+1} \ge \alpha \implies \rho_1 \ge \dfrac{\alpha y}{y+1-\alpha} \ge \dfrac{\alpha}{2-\alpha}.
        $$
    
    Budući da za $0<\alpha<1/2$ uvijek vrijedi $\alpha/(2-\alpha)<\alpha/(1+\alpha)$, brisanje elementa izaziva teži gubitak ravnoteže nego dodavanje elementa, osobito kad je stablo vrlo malo.
    
    Zatim se operacija vraćanja ravnoteže dijeli na dva slučaja:
    
    ??? note "Slučaj 1: $w$ nije pretežak, tj. $\rho_2\le\beta$, jednostruka rotacija"
        Najprije, $z$ i $w+y$ su uravnoteženi. Naime,
        
        $$
        \left(1-\dfrac{\alpha}{2-\alpha}\right)\alpha+\dfrac{\alpha}{2-\alpha} \le \dfrac{w+y}{x+y} = (1-\rho_1)\rho_2+\rho_1 < (1-\alpha)\dfrac{1}{2-\alpha}+\alpha.
        $$
        
        Lijevi izraz uvijek je veći od $\alpha$ za $\alpha\in(0,1)$, a desni izraz nikad nije veći od $(1-\alpha)$ za $\alpha\in(0,1-\sqrt{2}/2]$.
        
        Drugo, $w$ i $y$ su uravnoteženi. Slično, promotrimo
        
        $$
        \dfrac{y}{w+y} = \dfrac{\rho_1}{(1-\rho_1)\rho_2+\rho_1}.
        $$
        
        S jedne strane, za sve $\alpha\in(0,(3-\sqrt{5})/2)$ vrijedi
        
        $$
        \dfrac{y}{w+y} < \dfrac{\alpha}{(1-\alpha)\alpha+\alpha} < 1-\alpha.
        $$
        
        S druge strane, za sve $\alpha\in(0,1/3)$, osim u slučaju brisanja elementa uz $y=1$, vrijedi
        
        $$
        \rho_1 \ge \min\left\{\dfrac{\alpha}{1+\alpha},\dfrac{2\alpha}{3-\alpha}\right\} = \dfrac{2\alpha}{3-\alpha},
        $$
        
        pa je
        
        $$
        \dfrac{y}{w+y} \ge \dfrac{\dfrac{2\alpha}{3-\alpha}}{\left(1-\dfrac{2\alpha}{3-\alpha}\right)\dfrac{1}{2-\alpha}+\dfrac{2\alpha}{3-\alpha}} > \alpha.
        $$
        
        Na kraju promotrimo preostali slučaj, tj. brisanje elementa uz $y=1$. Najvjerojatniji gubitak ravnoteže nastaje kad je $x=\lfloor 2/\alpha\rfloor-2$ i $w=\lfloor\beta x\rfloor$. Stablo može vratiti ravnotežu ako i samo ako
        
        $$
        \dfrac{1}{1+\lfloor\beta x\rfloor}\ge\alpha \iff \lfloor\beta x\rfloor\le\dfrac{1}{\alpha}-1 \iff \beta x < \dfrac{1}{\alpha} \iff x < \dfrac{2}{\alpha}-1.
        $$
        
        A to uvijek vrijedi. Time je dokaz ovog slučaja dovršen. Primijetite da dokaz posljednjeg slučaja koristi činjenicu da su težine uvijek cijeli brojevi i ne može se spojiti s prethodnom raspravom.
    
    ??? note "Slučaj 2: $w$ je pretežak, tj. $\rho_2>\beta$, dvostruka rotacija"
        Najprije, $z+u$ i $v+y$ su uravnoteženi. Naime,
        
        $$
        \dfrac{\alpha}{2-\alpha}+\left(1-\dfrac{\alpha}{2-\alpha}\right)\dfrac{1}{2-\alpha}\alpha < \dfrac{v+y}{x+y} = \rho_1+(1-\rho_1)\rho_2\rho_3 <\alpha+(1-\alpha)^3
        $$
        
        Lijevi izraz uvijek je veći od $\alpha$ za $\alpha\in(0,1)$, a desni izraz uvijek je manji od $(1-\alpha)$ za $\alpha\in(0,(3-\sqrt{5})/2)$.
        
        Zatim, $z$ i $u$ su uravnoteženi. Naime, za $\alpha\in(0,1)$ uvijek vrijedi
        
        $$
        \alpha=\dfrac{\dfrac{1}{2-\alpha}\alpha}{1-\dfrac{1}{2-\alpha}(1-\alpha)}<\dfrac{u}{z+u} = \dfrac{\rho_2(1-\rho_3)}{1-\rho_2\rho_3} <\dfrac{(1-\alpha)^2}{1-(1-\alpha)\alpha} < 1-\alpha.
        $$
        
        Na kraju, $v$ i $y$ su uravnoteženi. Slično ostalim slučajevima, promotrimo
        
        $$
        \dfrac{y}{v+y} = \dfrac{\rho_1}{\rho_1+(1-\rho_1)\rho_2\rho_3}.
        $$
        
        S jedne strane, za sve $\alpha\in(0,1-\sqrt{2}/2]$ vrijedi
        
        $$
        \dfrac{y}{v+y} < \dfrac{\alpha}{\alpha+(1-\alpha)\dfrac{1}{2-\alpha}\alpha} \le 1-\alpha.
        $$
        
        S druge strane,
        
        $$
        \dfrac{y}{v+y} \ge \dfrac{\rho_1}{\rho_1+(1-\rho_1)(1-\alpha)^2}.
        $$
        
        Desni izraz nije manji od $\alpha$ ako i samo ako
        
        $$
        \rho_1 \ge \dfrac{\alpha(1-\alpha)}{1+\alpha(1-\alpha)}.
        $$
        
        Ako je gubitak ravnoteže uzrokovan umetanjem, tada je $\rho_1\ge \alpha/(1+\alpha)$, što očito vrijedi. Inače je situacija nešto složenija:
        
        -   kad je $y\ge 3$, vrijedi $\rho_1\ge 3\alpha/(4-\alpha)$, a $3\alpha/(4-\alpha)\ge\alpha(1-\alpha)/(1+\alpha(1-\alpha))$ vrijedi za sve $\alpha\in[1-\sqrt{3}/2,1)$;
        -   kad je $y=2$, najvjerojatniji gubitak ravnoteže nastaje kad je $x=\lfloor 3/\alpha\rfloor-3$, $w=\lfloor(1-\alpha)x\rfloor$ i $v=\lfloor(1-\alpha)w\rfloor$; tada $y/(v+y)\ge\alpha$ vrijedi za sve $\alpha\in(3/22,1)$;
        -   kad je $y=1$, najvjerojatniji gubitak ravnoteže nastaje kad je $x=\lfloor 2/\alpha\rfloor-2$, $w=\lfloor(1-\alpha)x\rfloor$ i $v=\lfloor(1-\alpha)w\rfloor$; tada $y/(v+y)\ge\alpha$ vrijedi za sve $\alpha\in(2/11,1)$.
        
        Rasprava o posljednja dva slučaja također koristi činjenicu da su težine svih čvorova cijeli brojevi.
    
    Objedinjujući oba slučaja, za $\alpha\in(2/11,1-\sqrt{2}/2]$ opisana kombinacija jednostruke i dvostruke rotacije jamči ravnotežu stabla.
    
    Iz ove analize vidi se da najteži slučaj za održavanje ravnoteže nastaje pri brisanju čvorova iz malih stabala. Osim za $\beta=1/(2-\alpha)$, dokaz ispravnosti za druge izbore parametara može se provesti ponavljanjem gornjeg postupka, samo što neke upotrijebljene nejednakosti treba odgovarajuće prilagoditi.

Poslije su Hirai i Yamamoto računalnim dokazom potpuno odredili raspon svih dopustivih parova $(\alpha,\beta)$; rezultat je prilično složen dvodimenzionalni lik:

![](images/wblt-param-range.svg)

U svom radu preporučuju sljedeću strategiju održavanja ravnoteže:

-   kad je $x>3y$, proglašava se gubitak ravnoteže;
-   kad je $w\le 2z$, bira se jednostruka rotacija, inače dvostruka.

Razlog je to što je to jedina strategija unutar dopustivog raspona parametara koja se može izraziti jednostavnim cijelim brojevima, čime se izbjegava gubitak učinkovitosti zbog računanja s brojevima s pomičnim zarezom. Njihova preporučena strategija odgovara izboru $(\alpha,\beta)=(1/4,2/3)$. U praksi se parametri mogu odabrati prema konkretnoj situaciji.

Primjer implementacije:

???+ example "Primjer koda"
    ```cpp
    --8<-- "docs/ds/code/wblt/wblt-1.cpp:too-heavy"
    --8<-- "docs/ds/code/wblt/wblt-1.cpp:balance"
    ```

Kad je strategija održavanja ravnoteže implementirana, algoritam spajanja dvaju stabala vrlo je jednostavan. Neka je i dalje $x>y$; strategija spajanja je sljedeća:

-   ako je desno podstablo $y$ prazno, izravno vratimo lijevo podstablo $x$;
-   ako su lijevo i desno podstablo $x$ i $y$ već uravnoteženi, tj. $y\ge\alpha(x+y)$, izravno povežemo oba podstabla;
-   inače spojimo desno podstablo $w$ od $x$ s $y$, povežemo lijevo podstablo $z$ s rezultatom tog spajanja i uravnotežimo novo stablo.

Primjer implementacije:

???+ example "Primjer koda"
    ```cpp
    --8<-- "docs/ds/code/wblt/wblt-1.cpp:merge-by-balancing"
    ```

Može se dokazati da se tako održava ravnoteža spojenog stabla i da je složenost te operacije $O(|\log(x/y)|)$.

??? note "Dokaz ravnoteže i složenosti"
    Dovoljno je razmotriti slučaj kad je $y$ prelagan, tj. $y<\alpha(x+y)$. Tada najprije spojimo $w$ i $y$, a zatim povežemo $z$ i $w+y$. Treba dokazati da je dovoljno uravnotežiti stablo u korijenu kako bi se zajamčila ravnoteža stabla. Neka su lijevo i desno podstablo stabla $w+y$ redom $c$ i $d$, a lijevo i desno podstablo od $c$ redom $a$ i $b$. Uravnoteženje u korijenu dijeli se na tri slučaja:
    
    ??? note "Slučaj 1: $z$ i $w+y$ već su uravnoteženi, nije potrebna daljnja prilagodba, tj. $z\ge\alpha(x+y)$"
        Prema definiciji ravnoteže podstabla $z$ i $w+y$ oba su uravnotežena i međusobno su uravnotežena, pa je i cijelo stablo uravnoteženo.
    
    ??? note "Slučaj 2: $z$ je prelagan, a $c$ nije pretežak, ravnoteža se može vratiti jednostrukom rotacijom, tj. $z<\alpha(x+y)$ i $c\le\beta(w+y)$"
        Tada, budući da su $z$ i $w$ uravnoteženi, ali je $y$ prelagan u odnosu na $x = z+w$, težina podstabla $z$ zadovoljava
        
        $$
        \alpha(1-\alpha)(x+y) <  \alpha(z+w) \le z \le \alpha(x+y) .
        $$
        
        Težina od $c$ pak zadovoljava
        
        $$
        \alpha(w+y) \le c \le \beta(w+y).
        $$
        
        Stoga su $z$ i $c$ međusobno uravnoteženi čim je
        
        $$
        \dfrac{\alpha}{1-\alpha}<\dfrac{1-\alpha}{\alpha}\alpha<\dfrac{c}{z}=\dfrac{w+y}{z}\dfrac{c}{w+y} < \dfrac{1-\alpha(1-\alpha)}{\alpha(1-\alpha)}\beta\le\dfrac{1-\alpha}{\alpha},
        $$
        
        što zahtijeva
        
        $$
        \beta\le \dfrac{(1-\alpha)^2}{1-\alpha(1-\alpha)}.
        $$
        
        Također, $z+c$ i $d$ međusobno su uravnoteženi čim je
        
        $$
        \alpha\le (1-\beta)(1-\alpha)\le \dfrac{d}{w+y}\dfrac{w+y}{x+y}  = \dfrac{d}{x+y} < \dfrac{d}{c+d} \le 1-\alpha,
        $$
        
        što zahtijeva
        
        $$
        \beta \le \dfrac{1-2\alpha}{1-\alpha}.
        $$
    
    ??? note "Slučaj 3: $z$ je prelagan i $c$ je pretežak, ravnoteža se može vratiti dvostrukom rotacijom, tj. $z<\alpha(x+y)$ i $c>\beta(w+y)$"
        Slično slučaju 2, vrijedi
        
        $$
        \begin{aligned}
        \alpha(1-\alpha)(x+y) < z &\le \alpha(x+y),\\
        \beta(w+y)<c &\le (1-\alpha)(w+y),\\
        \alpha c\le a,b &\le (1-\alpha)c.
        \end{aligned}
        $$
        
        Stoga su $z$ i $a$ međusobno uravnoteženi čim je
        
        $$
        \dfrac{\alpha}{1-\alpha}\le\dfrac{1-\alpha}{\alpha}\beta\alpha\le\dfrac{a}{z} = \dfrac{w+y}{z}\dfrac{a}{c+d} < \dfrac{1-\alpha(1-\alpha)}{\alpha(1-\alpha)}(1-\alpha)^2,
        $$
        
        što zahtijeva
        
        $$
        \beta\ge\dfrac{\alpha}{(1-\alpha)^2}.
        $$
        
        Drugo, $b$ i $d$ međusobno su uravnoteženi čim je
        
        $$
        \dfrac{\alpha}{1-\alpha}\le\dfrac{\beta}{1-\beta}\alpha \le \dfrac{b}{d} = \dfrac{c}{d}\dfrac{b}{c} \le \dfrac{1-\alpha}{\alpha}(1-\alpha) < \dfrac{1-\alpha}{\alpha},
        $$
        
        što zahtijeva
        
        $$
        \beta\ge\dfrac{1}{2-\alpha}.
        $$
        
        Na kraju, $z+a$ i $b+d$ međusobno su uravnoteženi čim je
        
        $$
        \alpha<(1-\alpha)(1-(1-\alpha)^2)\le\frac{b+d}{x+y} = \dfrac{w+y}{x+y}\dfrac{b+d}{w+y} < (1-\alpha(1-\alpha))(1-\beta\alpha) \le 1-\alpha,
        $$
        
        što zahtijeva
        
        $$
        \beta\ge\dfrac{\alpha}{1-\alpha+\alpha^2}.
        $$
    
    Objedinjujući sva tri slučaja, čim je
    
    $$
    0<\alpha\le 1-\dfrac{\sqrt{2}}{2},~\dfrac{1}{2-\alpha}\le\beta\le\dfrac{1-2\alpha}{1-\alpha},
    $$
    
    zajamčeno je da se spojeno stablo može dovesti u ravnotežu kombinacijom jednostruke i dvostruke rotacije. To očito uključuje raspon parametara dan u glavnom tekstu.
    
    Na kraju kratko objasnimo zašto je složenost ovog algoritma $O(|\log(x/y)|)$. U postupku spajanja, ako je $y$ prelagan u odnosu na $x$, pokušavamo ga spojiti s desnim podstablom od $x$; to se nastavlja sve dok podstablo s korijenom u nekom potomku od $x$ ne postane uravnoteženo s $y$. Budući da se svakim spuštanjem za jednu razinu težina podstabla smanji na najviše $(1-\alpha)$ puta prethodnu, potrebno je najviše $\log_{\frac{1}{1-\alpha}}(x/y)$ iteracija da se nađe podstablo uravnoteženo s $y$. Stoga algoritam spajanja poziva algoritam balansiranja $O(|\log(x/y)|)$ puta[^merge-complexity-cmp], pa je i složenost $O(|\log(x/y)|)$.
    
    Iako nije očito, ovo obrazloženje ovisi o sljedećem zaključku: tijekom uzastopnog uzimanja desnih podstabala $y$ ne može u jednoj iteraciji prijeći iz prelaganog u odnosu na podstablo s lijeve strane u preteškog u odnosu na njega. Naime, raspon težina podstabala koja mogu biti uravnotežena s $y$ nalazi se između $\alpha y/(1-\alpha)$ i $(1-\alpha)y/\alpha$. Stoga, kad bi se u jednoj iteraciji iz „$y$ prelagan” prešlo u „$y$ pretežak”, težina podstabla od $x$ u toj bi se iteraciji smanjila barem na $\alpha^2/(1-\alpha)^2$ puta prethodnu. Ali u jednoj se iteraciji težina podstabla može smanjiti najviše na $\alpha$ puta prethodnu, a u gornjem rasponu za $\alpha$ vrijedi $\alpha>\alpha^2/(1-\alpha)^2$. To pokazuje da je pretpostavljeni slučaj nemoguć i da nakon neke iteracije nužno nastupa slučaj u kojem je $y$ uravnotežen s nekim podstablom od $x$.

### Održavanje spajanjem

Spajanje dvaju podstabala znači da se, uz jamstvo da ključevi lijevog podstabla nisu veći od ključeva desnog podstabla, gradi novo stablo čije su informacije u listovima upravo unija informacija u listovima lijevog i desnog podstabla, pri čemu se jamči ravnoteža stabla.

Za to postoji sljedeća strategija[^more-join] (i dalje neka je $x\ge y$):

-   ako je desno podstablo $y$ prazno, izravno vratimo lijevo podstablo $x$;
-   ako su lijevo i desno podstablo $x$ i $y$ već uravnoteženi, tj. $y\ge\alpha(x+y)$, izravno povežemo oba podstabla;
-   inače je desno podstablo $y$ prelagano, ali ako lijevo podstablo $z$ od $x$ i $w+y$ mogu biti uravnoteženi, tj. $z\ge\alpha(x+y)$, najprije spojimo $w$ i $y$, a zatim spojimo $z$ i $w+y$;
-   inače su i $z$ i $y$ prelagani; tada najprije spojimo $z$ s lijevim podstablom $u$ od $w$, zatim spojimo desno podstablo $v$ od $w$ s $y$, a zatim rezultate tih dvaju spajanja **spojimo** u novo stablo.

Usporedimo li ovu strategiju s prethodnom strategijom balansiranja, vidimo da su načini kombiniranja čvorova u posljednja dva slučaja slični rezultatima jednostruke odnosno dvostruke rotacije iz prethodne strategije balansiranja, samo što je povezivanje podstabala zamijenjeno spajanjem.

Može se dokazati da je za

$$
0<\alpha \le 1-\dfrac{\sqrt{2}}{2}\approx 0.292
$$

tako dobiveno stablo uvijek uravnoteženo i da je složenost te operacije $O(|\log(x/y)|)$. Drugim riječima, trošak spajanja dvaju stabala ne ovisi o njihovoj apsolutnoj veličini, nego samo o njihovoj relativnoj veličini.

??? note "Dokaz ravnoteže i složenosti"
    Neka je $\tau(x,y)$ broj izravnih povezivanja dvaju podstabala pri spajanju podstabala težina $x$ i $y$. Strogo govoreći, treba dokazati da za $0<\alpha\le 1-\sqrt{2}/2$ postoji konstanta $C>0$ takva da za sve $x\ge y>0$ vrijedi
    
    $$
    \tau(x,y) \le 1+C\log^+\dfrac{\alpha x}{(1-\alpha)^2y},
    $$
    
    gdje je $\log^+ x = \max\{0,\log x\}$; štoviše, za sve $x/y\le(1-\alpha)/\alpha$ vrijedi $\tau(x,y)=1$. Zapravo, konstanta u formuli može se uzeti kao
    
    $$
    C = -\dfrac{2}{\log(1-\alpha)}.
    $$
    
    To pokazuje da je složenost algoritma spajanja $O(|\log(x/y)|)$.
    
    Da bismo dokazali da je stablo dobiveno algoritmom spajanja uvijek uravnoteženo i da gornji izraz za složenost vrijedi, koristimo indukciju. Sve točke rešetke u prvom kvadrantu $(x,y)\in\mathbf N^2_+$ možemo urediti leksikografski po $(x+y,|x-y|)$; to je očito dobar uredaj na tom skupu, pa po njemu možemo provoditi indukciju. Baza indukcije je $(x,y)=(1,1)$; tada oba podstabla imaju samo po jedan list, podstablo dobiveno izravnim povezivanjem nužno je uravnoteženo i $\tau(x,y)=1$, u skladu s gornjom formulom. Pretpostavimo sada da je indukcija stigla do $(x,y)$ i da tvrdnja vrijedi za sve točke prije $(x,y)$. Razlikujemo tri slučaja:
    
    ??? note "Slučaj 1: stabla $x$ i $y$ su uravnotežena, tj. $y\ge\alpha(x+y)$"
        Tada je stablo dobiveno izravnim povezivanjem također uravnoteženo i algoritam povezivanja poziva se samo jednom, pa je $\tau(x,y)=1$.
    
    ??? note "Slučaj 2: stablo $y$ je prelagano, ali $z$ nije prelagan, tj. $y<\alpha(x+y)\le z$"
        Tada najprije spojimo $w$ i $y$, a zatim spojimo $z$ i $w+y$, pa je
        
        $$
        \tau(x,y) = \tau(w,y) + \tau(z,w+y).
        $$
        
        Prema pretpostavci indukcije podstablo $w+y$ već je uravnoteženo. Za drugo spajanje zapravo se može izravno dokazati da su $z$ i $w+y$ uravnoteženi:
        
        $$
        \alpha \le \dfrac{z}{z+(w+y)} = \dfrac{z}{x+y} < \dfrac{z}{z+w} \le 1-\alpha.
        $$
        
        Stoga je spajanje $z$ i $w+y$ zapravo izravno povezivanje dvaju podstabala i vrijedi $\tau(z,w+y) = 1$. Dakle, konačno dobiveno stablo također je uravnoteženo.
        
        Sada procijenimo veličinu $\tau(w,y)$. Budući da je $y<(\alpha/(1-\alpha))x$ i $\alpha x\le w\le(1-\alpha)x$, ocjenom dobivamo
        
        $$
        \dfrac{\alpha}{1-\alpha}<1-\alpha=\dfrac{\alpha x}{(\alpha/(1-\alpha))x}< \dfrac{w}{y} \le \dfrac{(1-\alpha)x}{y}.
        $$
        
        To pokazuje da neuravnoteženost $w$ i $y$ nastupa samo kad je $w>y$, pa vrijedi
        
        $$
        \begin{aligned}
        \tau(w,y) &\le 1+C\log^+\dfrac{\alpha w}{(1-\alpha)^2y} \le 1+C\log^+\dfrac{\alpha x}{(1-\alpha)y} \\
        &= 1 + C\log(1-\alpha) + C\log^+\dfrac{\alpha x}{(1-\alpha)^2y}.
        \end{aligned}
        $$
        
        Jednakost u posljednjem koraku vrijedi jer je $x/y>(1-\alpha)/\alpha$.
        
        Stoga je
        
        $$
        \tau(x,y) \le 2 + C\log(1-\alpha) + C\log^+\dfrac{\alpha x}{(1-\alpha)^2y}.
        $$
    
    ??? note "Slučaj 3: stabla $y$ i $z$ oba su prelagana, tj. $y,z<\alpha(x+y)$"
        Tada najprije spojimo $z$ i $u$, zatim $v$ i $y$, a na kraju $z+u$ i $v+y$. Stoga je
        
        $$
        \tau(x,y) = \tau(z,u) + \tau(v,y) + \tau(z+u,v+y).
        $$
        
        Slično prethodnom slučaju možemo procijeniti omjer težina dvaju podstabala pri svakom spajanju.
        
        Budući da je $z,y<\alpha(x+y)$, vrijedi $w>(1-2\alpha)(x+y)$. Istodobno, iz uvjeta ravnoteže vrijedi $\alpha\le z/x,w/x,u/w,v/w\le 1-\alpha$. To pokazuje da je
        
        $$
        \begin{aligned}
        \dfrac{\alpha}{1-\alpha}<\dfrac{\alpha}{1-\alpha}\frac{1}{1-\alpha}\le \dfrac{z}{u} &= \dfrac{z}{w}\dfrac{w}{u} < \dfrac{\alpha}{1-2\alpha}\dfrac{1}{\alpha} \le \dfrac{1-\alpha}{\alpha},\\
        \dfrac{\alpha}{1-\alpha}\le\alpha\dfrac{1-2\alpha}{\alpha}< \dfrac{v}{y} &= \dfrac{v}{w}\dfrac{w}{y} \le (1-\alpha)\dfrac{(1-\alpha)x}{y} = (1-\alpha)^2\dfrac{x}{y}.
        \end{aligned}
        $$
        
        Za posljednji član vrijedi
        
        $$
        \dfrac{z+u}{v+y} = \dfrac{x+y}{v+y}-1 = \dfrac{x+y}{y}\dfrac{y}{v+y} - 1 < (1-\alpha)\left(\dfrac{x}{y}+1\right)-1 < (1-\alpha)\dfrac{x}{y}.
        $$
        
        Obratno, vrijedi
        
        $$
        \dfrac{z+u}{v+y} = \dfrac{x+y}{v+y}-1 \ge \dfrac{x+y}{(1-\alpha)^2x+y}-1 > \dfrac{1}{(1-\alpha)^3+\alpha}-1 > \dfrac{\alpha}{1-\alpha}.
        $$
        
        Pomoću tih nejednakosti može se pokazati da je konačno dobiveno stablo nužno uravnoteženo. Iz pretpostavke indukcije slijedi da spajanje $z$ i $u$ te spajanje $v$ i $y$ jamče uravnoteženost dobivenih stabala. Štoviše, prvi korak, spajanje $z$ i $u$, zapravo je izravno povezivanje dvaju stabala. Za spajanje stabala $z+u$ i $v+y$ postoje dva podslučaja:
        
        -   ako je $z+u\le v+y$, omjer njihovih težina strogo je veći od $\alpha/(1-\alpha)$, pa se mogu izravno povezati i rezultat je uravnotežen;
        -   inače je omjer njihovih težina nužno strogo manji od $x/y$, ali je $(z+u)+(v+y)=x+y$, pa je $|(z+u)-(v+y)|<|x-y|$; prema prije uvedenom leksikografskom uređaju i na ovaj se slučaj može primijeniti pretpostavka indukcije, pa je rezultat također uravnotežen.
        
        Daljnjom primjenom pretpostavke indukcije dobivamo:
        
        $$
        \begin{aligned}
        \tau(z,u) &= 1,\\
        \tau(v,y) &\le 1+C\log^+\dfrac{\alpha x}{y},\\
        \tau(z+u,v+y) &\le 1 + C\log^+\dfrac{\alpha x}{(1-\alpha)y}.
        \end{aligned}
        $$
        
        Izravno zbrajanje tih triju nejednakosti dovelo bi do koeficijenta $2C$ ispred logaritamskog člana, čime se indukcija ne bi mogla zatvoriti. Stoga je ovdje potrebna finija procjena.
        
        Kad je $\min\{v/y,(z+u)/(v+y)\}\le(1-\alpha)/\alpha$, jedan od $\tau(v,y)$ i $\tau(z+u,v+y)$ nužno je jednak $1$, pa vrijedi
        
        $$
        \begin{aligned}
        \tau(v,y) + \tau(z+u,v+y) &\le 2 + C\log^+\dfrac{\alpha x}{(1-\alpha)y}\\
        &= 2 + C\log(1-\alpha) + C\log^+\dfrac{\alpha x}{(1-\alpha)^2y}.
        \end{aligned}
        $$
        
        Inače mora vrijediti
        
        $$
        \begin{aligned}
        \tau(v,y) + \tau(z+u,v+y) 
        &\le 2 + C\log^+\dfrac{\alpha v}{(1-\alpha)^2y} + C\log^+\dfrac{\alpha(z+u)}{(1-\alpha)^2(v+y)}\\
        &= 2 + C\log\dfrac{\alpha}{(1-\alpha)^2} + C\log^+\dfrac{\alpha v(z+u)}{(1-\alpha)^2y(v+y)}.
        \end{aligned}
        $$
        
        Za $0<\alpha\le 1-\sqrt{2}/2$ vrijedi
        
        $$
        \dfrac{\alpha}{(1-\alpha)^2} < 1-\alpha.
        $$
        
        Osim toga, vrijedi
        
        $$
        \begin{aligned}
        \dfrac{v(z+u)}{y(v+y)} &= \left(\dfrac{v+y}{y}-1\right)\left(\dfrac{x+y}{y}\dfrac{y}{v+y} - 1\right) \\
        &= \dfrac{x+y}{y} + 1 -\dfrac{x+y}{y}\dfrac{y}{v+y}-\dfrac{v+y}{y} < \dfrac{x}{y}.
        \end{aligned}
        $$
        
        To pokazuje da i u ovom drugom slučaju vrijedi
        
        $$
        \tau(v,y) + \tau(z+u,v+y) < 2 + C\log(1-\alpha) + C\log^+\dfrac{\alpha x}{(1-\alpha)^2y}.
        $$
        
        Ukupna složenost spajanja je
        
        $$
        \tau(x,y) \le 3 + C\log(1-\alpha) + C\log^+\dfrac{\alpha x}{(1-\alpha)^2y}.
        $$
    
    Objedinjujući sve slučajeve, vrijedi
    
    $$
    \tau(x,y) \le 3 + C\log(1-\alpha) + C\log^+\dfrac{\alpha x}{(1-\alpha)^2y}.
    $$
    
    Stoga je dovoljno uzeti $2+C\log(1-\alpha)\le 0$ da se indukcija za složenost zatvori. Očit izbor je
    
    $$
    C = -\dfrac{2}{\log(1-\alpha)}.
    $$
    
    Ta konstanta pokazuje da pri spajanju dvaju stabala broj izravnih povezivanja podstabala otprilike ne premašuje dvostruku razliku visina stabala.

Primjer implementacije:

???+ example "Primjer koda"
    ```cpp
    --8<-- "docs/ds/code/wblt/wblt-1.cpp:merge"
    ```

Tom strategijom spajanja također se lako implementira održavanje ravnoteže stabla: pri gubitku ravnoteže dovoljno je izravno spojiti lijevo i desno podstablo.

???+ example "Primjer koda"
    ```cpp
    --8<-- "docs/ds/code/wblt/wblt-1.cpp:balance-by-merging"
    ```

Budući da su veličine dvaju stabala koja treba ponovno uravnotežiti uvijek gotovo uravnotežene, složenost održavanja ravnoteže je $O(1)$.

## Osnovne operacije balansiranog stabla

Pomoću prije implementiranih funkcija WBLT može podržati sve osnovne operacije balansiranog stabla. Ovaj odjeljak na primjeru multiskupa obrađuje kako WBLT-om implementirati balansirano stablo.

### Izgradnja stabla

Izgradnja stabla vrlo je slična segmentnom stablu: dovoljno je rekurzivno silaziti i raspolavljati interval dok mu duljina ne postane $1$, kad se informacija koju održavamo stavlja u list, a pri povratku iz rekurzije spajaju se informacije intervala.

???+ example "Primjer koda"
    ```cpp
    --8<-- "docs/ds/code/wblt/wblt-2.cpp:build"
    ```

Vremenska složenost je $O(n)$.

### Umetanje i brisanje

Za umetanje treba od korijena rekurzivno silaziti dok se ne nađe list s najmanjim ključem među listovima čiji je ključ veći ili jednak elementu koji se umeće, zatim stvoriti dva nova čvora, od kojih jedan pohranjuje novoumetnutu vrijednost, a drugi kao novi roditelj dvaju listova zamjenjuje mjesto tog najmanjeg lista, te oba lista povezati s tim roditeljem. Pri povratku treba održavati ravnotežu stabla.

![](./images/wblt-insert-delete.svg)

Kao na slici, u lijevo stablo želimo umetnuti element vrijednosti $4$. Najprije nađemo list vrijednosti $5$, zatim stvorimo list $4$ i unutarnji čvor $\text{d}$ te $4$ i $5$ povežemo s $\text{d}$. Tako dobivamo desno stablo.

Za brisanje promotrimo obrnuti postupak. Dakle, nađemo list čiji je ključ jednak vrijednosti koju brišemo, obrišemo njega i njegova roditelja, a drugo dijete roditelja stavimo na roditeljevo mjesto. Pri povratku također treba održavati ravnotežu stabla.

Primjer implementacije:

???+ example "Primjer koda"
    ```cpp
    --8<-- "docs/ds/code/wblt/wblt-1.cpp:insert-remove"
    ```

Pazite na obradu praznog stabla. Ako ne želite obrađivati prazno stablo, možete unaprijed umetnuti element $\infty$.

Vremenska složenost obiju operacija je $O(\log n)$.

### Upit ranga

Budući da je oblik WBLT-a vrlo sličan segmentnom stablu, upit ranga može se izvesti slično binarnom pretraživanju na segmentnom stablu: ako je maksimum lijevog podstabla veći ili jednak traženoj vrijednosti, skačemo u lijevo dijete; inače skačemo u desno dijete i odgovoru dodajemo težinu lijevog podstabla.

Primjer implementacije:

???+ example "Primjer koda"
    ```cpp
    --8<-- "docs/ds/code/wblt/wblt-1.cpp:rank"
    ```

Vremenska složenost je $O(\log n)$.

### Upit po rangu

I dalje koristimo ideju binarnog pretraživanja na segmentnom stablu, samo što ovdje uspoređujemo težine čvorova.

Primjer implementacije:

???+ example "Primjer koda"
    ```cpp
    --8<-- "docs/ds/code/wblt/wblt-1.cpp:kth-element"
    ```

Vremenska složenost je $O(\log n)$.

### Traženje prethodnika i sljedbenika

Dovoljno je kombinirati prethodne dvije funkcije.

Primjer implementacije:

???+ example "Primjer koda"
    ```cpp
    --8<-- "docs/ds/code/wblt/wblt-1.cpp:prev-next"
    ```

Ako ih želite implementirati izravno, pazite da čvorovi s jednakim ključem mogu biti pohranjeni u više listova.

### Razdvajanje

Razdvajanje WBLT-a slično je [Treapu bez rotacija](./treap.md#razdvajanje-split): prema veličini podstabla ili ključu odlučuje se hoće li se rekurzivno razdvajati lijevo ili desno podstablo. Razlika je u tome što WBLT razdvojena podstabla mora **spajati** kako bi održao ravnotežu konačno razdvojenih stabala.

Primjer implementacije razdvajanja prema veličini podstabla:

???+ example "Primjer koda"
    ```cpp
    --8<-- "docs/ds/code/wblt/wblt-2.cpp:split"
    ```

Vremenska složenost je $O(\log n)$.

??? note "Dokaz složenosti"
    Broj razina rekurzivnog silaska očito ne premašuje visinu stabla i iznosi $O(\log n)$. Treba dokazati da je složenost spajanja podstabala razdvojenih na lijevoj odnosno desnoj strani $O(\log n)$. Dovoljno je promotriti samo lijeva podstabla, jer je desna strana simetrična. Neka su podstabla razdvojena na lijevoj strani, odozdo prema gore, $T_1,T_2,\cdots,T_\ell$; njihov je broj $\ell\in O(\log n)$. Postupak spajanja može se opisati ovako: počevši od $T'_1=T_1$, spajamo $T'_{i-1}$ i $T_i$ u $T'_i$, rekurzivno dok sva podstabla nisu spojena. Ukupna složenost spajanja može se izraziti kao
    
    $$
    \sum_{i=2}^\ell \tau(T_i,T'_{i-1}),
    $$
    
    gdje je $\tau(T_i,T'_{i-1})$ složenost spajanja $T_i$ i $T'_{i-1}$.
    
    Kad bi uvijek vrijedilo $w(T_i)\ge w(T'_{i-1})$, prema izrazu za složenost spajanja dvaju podstabala imali bismo
    
    $$
    \tau(T_i,T'_{i-1}) \in O\left(\log\dfrac{w(T_i)}{w(T'_{i-1})}\right) \subseteq O\left(\log\dfrac{w(T'_i)}{w(T'_{i-1})}\right).
    $$
    
    Budući da su konstante u tim velikim $O$ oznakama jednake, mogu se izravno zbrojiti i teleskopski pokratiti.
    
    Međutim, treba primijetiti da $w(T_i)\ge w(T'_{i-1})$ ne vrijedi uvijek, jer je $T'_{i-1}$ razdvojen iz desnog podstabla koje odgovara $T_i$ u izvornom stablu, a to desno podstablo može biti veće od lijevog podstabla $T_i$. Unatoč tome, čak i kad je $T'_{i-1}$ veći od $T_i$, kao dio desnog podstabla težina $w(T'_{i-1})$ ne premašuje $(1-\alpha)/\alpha$ puta $w(T_i)$, što znači da su tada $T'_{i-1}$ i $T_i$ sigurno uravnoteženi i složenost spajanja je $O(1)$.
    
    Objedinjujući oba slučaja, složenost jednog spajanja može se zapisati kao
    
    $$
    \tau(T_i,T'_{i-1}) \in O\left(\log\dfrac{w(T'_i)}{w(T'_{i-1})}\right) + O(1).
    $$
    
    Stoga je ukupna složenost spajanja
    
    $$
    O\left(\sum_{i=2}^\ell\left( 1+\log\dfrac{w(T'_i)}{w(T'_{i-1})}\right) \right) \subseteq O(\ell+\log w(T'_\ell)) \subseteq O(\log n).
    $$
    
    To ujedno pokazuje da je ukupna složenost algoritma razdvajanja $O(\log n)$.

## Primjer implementacije

Ovaj je tekst predstavio kako WBLT-om obaviti osnovne operacije balansiranog stabla. Slijedi [predložak običnog balansiranog stabla](https://loj.ac/p/104) implementiran WBLT-om.

??? example "Primjer koda"
    ```cpp
    --8<-- "docs/ds/code/wblt/wblt-1.cpp:full-text"
    ```

Pomoću spajanja i razdvajanja može se implementirati i umjetničko balansirano stablo. Slijedi [predložak umjetničkog balansiranog stabla](https://loj.ac/p/105) implementiran WBLT-om; pri silaznom pristupu čvorovima treba spuštati lijene oznake.

??? example "Primjer koda"
    ```cpp
    --8<-- "docs/ds/code/wblt/wblt-2.cpp:full-text"
    ```

Pazite da WBLT treba dvostruko više prostora; kad su uključeni razdvajanje i spajanje, treba paziti na sakupljanje smeća i pravodobno reciklirati nepotrebne čvorove, inače prostor nije linearan.

## Literatura i napomene

-   [Weight-balanced tree - Wikipedia](https://en.wikipedia.org/wiki/Weight-balanced_tree)
-   Nievergelt, J.; Reingold, E. M. (1973). "Binary Search Trees of Bounded Balance". SIAM Journal on Computing. 2: 33–43.
-   Blum, Norbert; Mehlhorn, Kurt (1980). "On the average number of rebalancing operations in weight-balanced trees". Theoretical Computer Science. 11 (3): 303–320.
-   Hirai, Y.; Yamamoto, K. (2011). "Balancing weight-balanced trees". Journal of Functional Programming. 21 (3): 287.
-   Blelloch, Guy E.; Ferizovic, Daniel; Sun, Yihan (2016), "Just Join for Parallel Ordered Sets", Symposium on Parallel Algorithms and Architectures, Proc. of 28th ACM Symp. Parallel Algorithms and Architectures (SPAA 2016), ACM, pp. 253–264.
-   Straka, Milan. (2011). "Adams’Trees Revisited: Correctness Proof and Efficient Implementation." International Symposium on Trends in Functional Programming. Berlin, Heidelberg: Springer Berlin Heidelberg.

[^wrong-range]: Raspon parametara $\alpha < 1-\dfrac{\sqrt{2}}{2},~\beta=\dfrac{1-2\alpha}{1-\alpha}$ dan u izvornom radu Nievergelta i Reingolda pogrešan je. Rad Hiraija i Yamamota daje odgovarajuće protuprimjere; problem se javlja uglavnom kod nekih vrlo malih stabala, zbog čega cijeli induktivni dokaz propada. Naravno, na stvarnim algoritamskim natjecanjima teško je konstruirati podatke koji bi oborili te pogrešne parametre, pa u praksi to vjerojatno nema velik utjecaj.

[^merge-complexity-cmp]: Budući da jedna operacija balansiranja odgovara najviše dvama povezivanjima podstabala, a na kraju, kad su dva podstabla već uravnotežena, treba još jednom pozvati algoritam povezivanja podstabala, ako brojimo pozive algoritma povezivanja podstabala, konstante spajanja temeljenog na balansiranju i balansiranja izravnim spajanjem iz nastavka jednake su.

[^more-join]: Iz dokaza u nastavku vidi se da su u trećem slučaju $z$ i $w+y$ uvijek uravnoteženi, a u četvrtom slučaju $z$ i $u$ uvijek uravnoteženi. Oni se mogu izravno povezati, bez potrebe za spajanjem.
