---
title: Najmanja obuhvatna kružnica
---

## Uvod

Za $n~(n\ge 1)$ točaka $P_1,P_2,\cdots,P_n$ u ravnini treba pronaći kružnicu najmanjeg polumjera takvu da nijedna točka ne leži izvan nje. Ta se kružnica zove **najmanja obuhvatna kružnica** (Minimum Enclosing Circle, MEC) tih točaka.

U ovom članku dopuštamo kružnice polumjera $0$: kad se sve točke podudaraju u jednoj točki $P$, smatramo da je najmanja obuhvatna kružnica tih $n$ točaka kružnica sa središtem $P$ i polumjerom $0$.

Lako se vidi da je najmanja obuhvatna kružnica jedinstvena.

??? note "Dokaz"
    Pretpostavimo da postoje dvije različite najmanje obuhvatne kružnice sa središtima $O_1,O_2$ i jednakim polumjerom $r$. Neka je $M$ polovište dužine $O_1O_2$; tada za svaku točku $P$ vrijedi
    
    $$
    \begin{aligned}
        |P-M|^2&=\frac{|P-O_1|^2+|P-O_2|^2}{2}-\frac{|O_1-O_2|^2}{4}\\
        &\le r^2-\frac{|O_1-O_2|^2}{4}<r^2.
    \end{aligned}
    $$
    
    Dakle, sa središtem u $M$ možemo konstruirati obuhvatnu kružnicu manjeg polumjera, što je kontradikcija.
    
    ![](./images/smallest-enclosing-circle3.svg)

## Postupak

Uobičajen način rješavanja problema najmanje obuhvatne kružnice je Welzlov algoritam[^welzl], zasnovan na [randomiziranom inkrementalnom algoritmu](random-incremental.md). Ključna je operacija algoritma: točke najprije nasumično promiješamo, zatim održavamo najmanju obuhvatnu kružnicu skupa točaka i redom dodajemo nove točke u skup. Iako algoritam sadrži tri razine petlji, očekivana vremenska složenost mu je $O(n)$.

### Dodavanje jedne točke

Najprije razmotrimo što se događa kad u skup točaka koji trenutačno održavamo dodamo novu točku. Neka je trenutačna kružnica $C$ najmanja obuhvatna kružnica već obrađenog skupa točaka, a sad dodajemo točku $P$.

-   Ako je $P$ unutar $C$ ili na njezinu obodu, $C$ je i dalje najmanja obuhvatna kružnica.
-   Ako je $P$ izvan $C$, tada $P$ sigurno leži na obodu nove najmanje obuhvatne kružnice, pa problem možemo svesti na potproblem: uz poznato da je $P$ na obodu, pronaći najmanju obuhvatnu kružnicu.

??? tip "Zašto nova točka izvan kružnice sigurno leži na obodu nove kružnice"
    Neka su središta stare i nove kružnice $O_0,O_1$, a polumjeri $r_0,r_1$; tada je $r_0\le r_1$. Pretpostavimo da je $P$ strogo unutar nove kružnice. Za $0<t<1$ promotrimo kružnicu $(O_t,r_t)$ za koju vrijedi
    
    $$
    O_t=(1-t)O_1+tO_0,\qquad r_t^2=(1-t)r_1^2+tr_0^2-t(1-t)|O_1-O_0|^2<r_1^2,
    $$
    
    i uzmimo dovoljno mali $t$ da $P$ i dalje bude unutar kružnice $(O_t,r_t)$. Za svaku točku $Q$ imamo
    
    $$
    |Q-O_t|^2-r_t^2=(1-t)(|Q-O_1|^2-r_1^2)+t(|Q-O_0|^2-r_0^2).
    $$
    
    Dakle, točke starog skupa i dalje su obuhvaćene kružnicom $(O_t,r_t)$, a točke koje su prije bile istodobno fiksirane na obodu kružnice $(O_0,r_0)$ i na obodu kružnice $(O_1,r_1)$ i dalje su na obodu kružnice $(O_t,r_t)$. Budući da je $P$ unutar kružnice $(O_t,r_t)$, kružnica $(O_t,r_t)$ valjana je obuhvatna kružnica, ali vrijedi $r_t<r_1$, što je u kontradikciji s optimalnošću nove kružnice.
    
    ![](./images/smallest-enclosing-circle4.svg)

Gornji zaključak vrijedi i u slučaju kad dodajemo novu točku dok su jedna ili dvije točke već fiksirane na obodu.

### Tri razine petlji

Razmotrimo sada glavni dio Welzlova algoritma. Ulazne točke nasumično promiješamo s jednakim vjerojatnostima, i dalje ih označavamo $P_1,P_2,\cdots,P_n$ te stavljamo $S_i=\{P_1,\cdots,P_i\}$, $S_0=\varnothing$. Održavamo trenutačnu kružnicu $C$; na početku joj je središte $P_1$, polumjer $0$ i nema fiksiranih točaka na obodu.

1.  (Prva razina petlje) Bez fiksiranih točaka na obodu: redom prolazimo $i=2,\cdots,n$. Ako je $P_i$ već unutar $C$, nastavljamo; inače fiksiramo $P_i$ na obodu i ponovno tražimo najmanju kružnicu koja obuhvaća $S_{i-1}$.
2.  (Druga razina petlje) S jednom fiksiranom točkom oboda $P_i$: najprije $C$ postavimo na kružnicu s promjerom $P_iP_1$, a zatim redom prolazimo $j=2,\cdots,i-1$. Ako je $P_j$ već unutar $C$, nastavljamo; inače na obodu fiksiramo još i $P_j$ te ponovno tražimo najmanju kružnicu koja obuhvaća $S_{j-1}$.
3.  (Treća razina petlje) S dvjema fiksiranim točkama oboda $P_i,P_j$: najprije $C$ postavimo na kružnicu s promjerom $P_iP_j$, a zatim redom prolazimo $k=1,\cdots,j-1$. Ako je $P_k$ već unutar $C$, nastavljamo; inače $C$ ažuriramo na opisanu kružnicu trokuta $\triangle P_iP_jP_k$.

Ovdje „unutar kružnice” uvijek uključuje i obod, a trenutačna kružnica u svakom retku **najmanja** je kružnica koja zadovoljava odgovarajuća ograničenja. Na kraju treće razine petlje obuhvaćen je $S_{j-1}$, a uz $P_j$ na obodu to je upravo odgovor koji treba drugoj razini petlje; na kraju druge razine petlje analogno dobivamo odgovor koji treba prvoj razini. Izvedivost unutarnjih petlji jamče vanjske petlje, a lako se vidi i da pri ažuriranju u trećoj razini petlje tri točke $P_iP_jP_k$ nisu kolinearne, pa je algoritam ispravan.

??? tip "Zašto pri ažuriranju najmanje kružnice u trećoj razini petlje tri točke nisu kolinearne"
    Budući da je $P_j$ bio izvan kružnice koja prolazi kroz $P_i$, vrijedi $P_i\ne P_j$. Ako su $P_i,P_j,P_k$ kolinearne i $P_k$ je izvan trenutačne kružnice $C$, tada $P_k$ mora biti izvan dužine $P_iP_j$. Razlikujemo dva slučaja:
    
    -   Ako je $P_j$ između $P_i,P_k$, tada je u trenutku kad druga razina petlje dođe do $P_j$ trenutačna najmanja kružnica prolazila kroz $P_i$ i obuhvaćala $P_k$ iz $S_{j-1}$, pa je obuhvaćala i $P_j$ na dužini $P_iP_k$. To je u kontradikciji s time da je $P_j$ pokrenuo treću razinu petlje.
    -   Ako je $P_i$ između $P_j,P_k$, tada je u trenutku kad prva razina petlje dođe do $P_i$ trenutačna najmanja kružnica obuhvaćala $P_j,P_k$ iz $S_{i-1}$, pa je obuhvaćala i $P_i$ na dužini $P_jP_k$. To je u kontradikciji s time da je $P_i$ pokrenuo drugu razinu petlje.
    
    ![](./images/smallest-enclosing-circle5.svg)

### Računanje opisane kružnice

Operacije računalne geometrije u Welzlovu algoritmu prilično su standardne: uglavnom su to određivanje položaja točke u odnosu na kružnicu, kružnica kojoj je promjer zadan dvjema točkama i kružnica opisana trima točkama. Prve dvije preskačemo, a usredotočimo se na treću.

Za tri nekolinearne točke $A=(x_A,y_A), B=(x_B,y_B), C=(x_C,y_C)$ središte opisane kružnice sjecište je simetrala dužina $AB$ i $AC$ i može se izračunati metodom iz odjeljka [Sjecište dvaju pravaca](./2d.md#sjecište-dvaju-pravaca).

Možemo i izravno postaviti i riješiti jednadžbe. Neka je središte opisane kružnice $O=(x,y)$; tada

$$
\begin{cases}
(x-x_A)^2+(y-y_A)^2=(x-x_B)^2+(y-y_B)^2,\\
(x-x_A)^2+(y-y_A)^2=(x-x_C)^2+(y-y_C)^2,
\end{cases}
$$

Označimo

$$
\begin{aligned}
A_1&=2(x_B-x_A),&B_1&=2(y_B-y_A),&C_1&=x_B^2+y_B^2-x_A^2-y_A^2,\\
A_2&=2(x_C-x_A),&B_2&=2(y_C-y_A),&C_2&=x_C^2+y_C^2-x_A^2-y_A^2,
\end{aligned}
$$

pa vrijedi

$$
x=\frac{C_1B_2-C_2B_1}{A_1B_2-A_2B_1},\quad y=\frac{A_1C_2-A_2C_1}{A_1B_2-A_2B_1}.
$$

Kad izračunamo središte, uzmemo $r=|O-A|$. Nazivnik $A_1B_2-A_2B_1$ različit od nule odgovara tomu da tri točke nisu kolinearne. Kad su tri točke gotovo kolinearne, pogreška zaokruživanja ove metode može se jako povećati, pa u praksi treba posebno pripaziti.

### Primjer

Neka su točke $P_1=(-2,0)$, $P_2=(2,0)$, $P_3=(0,1)$, $P_4=(0,3)$. Označimo s $C_i$ najmanju obuhvatnu kružnicu nakon obrade prvih $i$ točaka; slika dolje prikazuje rezultate vanjske petlje. Puna plava linija označava trenutačnu kružnicu, siva isprekidana linija kružnicu prije ažuriranja, narančasta puna točka točku dodanu u ovom koraku, a siva prazna točka točku koja još nije dodana.

![](./images/smallest-enclosing-circle1.svg)

Na početku je polumjer $0$. Nakon dodavanja $P_2$ trenutačna obuhvatna kružnica ima promjer $P_1P_2$. $P_3$ je unutar kružnice, pa se pri njezinu dodavanju kružnica ne mijenja. $P_4$ je izvan kružnice, pa je potrebno ponovno računanje. Nakon ponovnog računanja središte je $(0,5/6)$, polumjer $13/6$, točke $P_1,P_2,P_4$ su na obodu, a $P_3$ je unutar kružnice.

U nastavku raščlanjujemo postupak ponovnog računanja za $i=4$. Narančasta točka označava točku koja se trenutačno provjerava, ljubičasti vanjski prsten označava točke oboda fiksirane u ovoj razini petlje, a njihov skup označavamo s $R$. Puna plava linija i siva isprekidana linija označavaju trenutačnu kružnicu odnosno kružnicu iz prethodnog koraka.

![](./images/smallest-enclosing-circle2.svg)

1.  $P_4$ je izvan stare kružnice $C_3$, ulazimo u drugu razinu petlje.
2.  Fiksiramo $P_4$ i najprije uzmemo kružnicu s promjerom $P_4P_1$. Pri provjeri $j=2$ ustanovimo da je $P_2$ izvan te kružnice, ulazimo u treću razinu petlje.
3.  Fiksiramo $P_4,P_2$ i trenutačnu kružnicu postavimo na kružnicu s promjerom $P_4P_2$. Pri provjeri $k=1$ ustanovimo da je $P_1$ i dalje izvan kružnice.
4.  Ažuriramo na opisanu kružnicu trokuta $\triangle P_4P_2P_1$ i završavamo treću razinu petlje. Po povratku u drugu razinu petlje točka $P_3$ koja odgovara $j=3$ već je unutar kružnice, pa je preskačemo i dobivamo $C_4$.

Privremene kružnice tijekom ponovnog računanja moraju zadovoljavati samo ograničenja trenutačnog potproblema, pa ne obuhvaćaju nužno sve točke već obrađene na višoj razini. Na primjer, kružnica na drugoj podslici još ne obuhvaća $P_2$, a kružnica na trećoj podslici još ne obuhvaća $P_1$ — upravo je to razlog ulaska u sljedeću razinu ili ažuriranja opisane kružnice.

### Analiza složenosti

Prema tijeku algoritma gornja je granica vremenske složenosti u najgorem slučaju $O(n^3)$, no nasumično miješanje smanjuje vjerojatnost ulaska u unutarnje petlje, pa očekivana vremenska složenost pada na $O(n)$.

Najmanju obuhvatnu kružnicu određuju najviše tri točke: kad postoji samo jedna različita točka, polumjer je $0$; inače je najmanja obuhvatna kružnica određena parom krajnjih točaka promjera ili trima nekolinearnim točkama. Nakon fiksiranja jedne točke oboda dovoljne su još najviše dvije točke da bi se odredilo optimalno rješenje.

??? tip "Zašto su nakon fiksiranja jedne točke oboda potrebne još najviše dvije točke"
    Translatiramo fiksiranu točku u ishodište. Neka je vektor središta $\vec{u}$; tada je polumjer te kružnice $|\vec{u}|$. Uvjet da je točka $x$ obuhvaćena ekvivalentan je uvjetu
    
    $$
    |\vec{x}-\vec{u}|^2\le |\vec{u}|^2\iff 2\vec{u}\cdot \vec{x}\ge |\vec{x}|^2.
    $$
    
    Svaka točka osim ishodišta nameće središtu jedno ograničenje u obliku poluravnine; dopustiva središta leže u [presjeku tih poluravnina](./half-plane.md), a optimalno je središte točka tog presjeka najbliža ishodištu. U dvodimenzionalnom prostoru dovoljno je zadržati najviše dva aktivna ograničenja da ta najbliža točka ostane nepromijenjena.[^note1] Dakle, osim fiksirane točke dovoljno je zadržati najviše još dvije ulazne točke da optimalno rješenje ostane isto.
    
    Na slici dolje plavo područje $H$ označava sva dopustiva središta, a narančasta točka $\vec{u}_*$ točka je tog područja najbliža ishodištu. Uklanjanje ograničenja koja odgovaraju sivim rubovima ne mijenja optimalno središte.
    
    ![](./images/smallest-enclosing-circle6.svg)

Stoga točka čije bi uklanjanje promijenilo optimalnu kružnicu sigurno pripada svakom takvom skupu određujućih točaka. Bez fiksiranih točaka oboda takvih točaka ima najviše tri; s jednom fiksiranom točkom oboda najviše dvije.

Provedimo sada analizu unatrag (backward analysis). Fiksirajmo najprije $P_i$ i neuređeni skup točaka $S_j$ u nekom koraku druge razine petlje. Budući da je početni redoslijed slučajan, $P_j$ je zapravo točka odabrana iz $S_j$ s jednakom vjerojatnošću. Dodavanje $P_j$ pokreće treću razinu petlje samo ako bi uklanjanje $P_j$ promijenilo ograničenu optimalnu kružnicu, pa je vjerojatnost pokretanja najviše $\min(1,2/j)$. Prolazak treće razine petlje traje $O(j)$, pa je očekivano vrijeme cijele druge razine petlje

$$
O(1)+\sum_{j=2}^{i-1}\left(O(1)+\frac{2}{j}\cdot O(j)\right)=O(i).
$$

Slično, fiksirajmo neuređeni skup točaka $S_i$ prve razine petlje; točaka koje pokreću ponovno računanje u drugoj razini petlje ima najviše tri, pa je vjerojatnost najviše $\min(1,3/i)$. Nakon fiksiranja te točke relativni redoslijed prethodnih točaka i dalje je slučajan, pa je uvjetno očekivano vrijeme tog ponovnog računanja $O(i)$. Dodamo li trošak svake provjere i trošak početnog miješanja, ukupna je očekivana vremenska složenost

$$
O(n)+\sum_{i=2}^{n}\left(O(1)+\min\left(1,\frac{3}{i}\right)\cdot O(i)\right)=O(n).
$$

## Primjer zadatka

???+ note "[Luogu P1742 最小圆覆盖 (Najmanja obuhvatna kružnica)](https://www.luogu.com.cn/problem/P1742)"
    Zadano je $N$ točaka; treba pronaći najmanju kružnicu koja sadrži sve točke te ispisati njezin polumjer i koordinate središta.

Sljedeća implementacija izravno održava središte i polumjer, a redoslijed točaka miješa pomoću `std::shuffle`. Tri razine petlji redom odgovaraju potproblemima s nula, jednom i dvije fiksirane točke oboda iz prethodnog teksta, a `geto` računa središte opisane kružnice triju točaka.

??? note "Referentna implementacija"
    ```cpp
    --8<-- "docs/geometry/code/smallest-enclosing-circle/smallest-enclosing-circle_1.cpp"
    ```

## Zadaci za vježbu

-   [「POI 2011」WYK-Plot](https://www.luogu.com.cn/problem/P3517)
-   [Library Checker - Minimum Enclosing Circle](https://judge.yosupo.jp/problem/minimum_enclosing_circle)

## Literatura i napomene

-   [Smallest-circle problem - Wikipedia](https://en.wikipedia.org/wiki/Smallest-circle_problem)
-   [Minimum Enclosing Circle - Algorithms for Competitive Programming](https://cp-algorithms.com/geometry/enclosing-circle.html)
-   [Computational Geometry Lecture 4: Smallest enclosing circles and more - University of Florida](https://www.cise.ufl.edu/~sitharam/COURSES/CG/kreveldnbhd.pdf)

[^welzl]: Welzl, E. (1991). Smallest enclosing disks (balls and ellipsoids). In: Maurer, H. (eds) New Results and New Trends in Computer Science. Lecture Notes in Computer Science, vol 555. Springer, Berlin, Heidelberg.

[^note1]: Vidi odgovarajući sadržaj u članku [Linearno programiranje](../math/linear-programming.md).
