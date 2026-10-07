---
title: Steinerovo stablo
---

Problem Steinerova stabla problem je kombinatorne optimizacije, srodan minimalnom razapinjućem stablu, i jedan je od problema najkraće mreže. Minimalno razapinjuće stablo traži, u zadanom skupu vrhova i bridova, najkraću mrežu koja povezuje sve vrhove. Minimalno Steinerovo stablo dopušta dodavanje dodatnih vrhova izvan zadanih kako bi ukupni trošak dobivene najkraće mreže bio najmanji.

## Uvod u problem

Početkom 19. stoljeća Steiner, poznati geometar sa Sveučilišta u Berlinu, proučavao je vrlo jednostavan, ali poučan problem: tri sela povezati cestama najmanje ukupne duljine. Matematički rečeno, za tri zadane točke $A$, $B$, $C$ u ravnini treba naći četvrtu točku $P$ u ravnini tako da zbroj $a+b+c$ bude najmanji, pri čemu $a$, $b$, $c$ označavaju udaljenosti od $P$ do $A$, $B$, $C$.

Odgovor glasi: ako je svaki kut trokuta $\textit{ABC}$ manji od $120^{\circ}$, tada je $P$ točka iz koje se stranice $\textit{AB}$, $\textit{BC}$, $\textit{AC}$ vide pod kutom od $120^{\circ}$. Ako trokut $\textit{ABC}$ ima kut, recimo kut $C$, veći od ili jednak $120^{\circ}$, tada se točka $P$ podudara s vrhom $C$.

### Poopćenja problema

1.  U Steinerovu problemu zadane su tri fiksne točke $A,B,C$. Prirodno je poopćiti problem na $n$ zadanih točaka $A_1,A_2,\dots,A_n$: tražimo točku $P$ u ravnini za koju je zbroj udaljenosti $a_1+a_2+\dots+a_n$ najmanji, gdje je $a_i$ udaljenost $PA_i$.

2.  Uzimajući u obzir druge čimbenike vezane uz točke, uvode se težine. Ostali se čimbenici $n$ točaka mogu pretvoriti u težine; tražimo točku $P$ u ravnini za koju je zbroj umnožaka udaljenosti i težina $a_1\cdot w_1+a_2\cdot w_2+\dots+a_n\cdot w_n$ najmanji, gdje je $w_i$ težina pojedine točke.

3.  Courant (R. Courant) i Robbins (H. Robbins) istaknuli su da je prvo poopćenje površno. Da bi se dobilo zaista vrijedno poopćenje Steinerova problema, treba odustati od traženja jedne točke $P$ i umjesto nje tražiti „cestovnu mrežu” najmanje ukupne duljine. Matematički: za zadanih $n$ točaka $A_1,A_2,\cdots,A_n$ naći sustav dužina najmanje ukupne duljine koji povezuje tih $n$ točaka tako da su svake dvije točke povezane izlomljenom crtom sastavljenom od dužina sustava. Taj su novi problem nazvali **problem Steinerova stabla**. Za $n$ zadanih točaka postoji najviše $n-2$ dodatnih točaka grananja (Steinerovih točaka). Kroz svaku Steinerovu točku prolaze najviše tri brida. Ako su tri, oni se međusobno sijeku pod kutom od $120^{\circ}$; ako su dva, tada je ta Steinerova točka nužno jedna od zadanih točaka, a kut između ta dva brida veći je od ili jednak $120^{\circ}$.

Najkraća mreža koja povezuje više od tri točke

![steiner-tree1](./images/steiner-tree-1.svg)

U prvom se slučaju rješenje sastoji od pet dužina s dvije Steinerove točke (crvene $s_1,s_2$), u kojima se sastaju tri dužine pod međusobnim kutovima od $120^{\circ}$. Rješenje u drugom slučaju sadrži tri Steinerove točke. U trećem slučaju jedna ili više Steinerovih točaka može degenerirati, odnosno biti zamijenjena jednom ili više zadanih točaka.

Model problema Steinerova stabla prikazat ćemo u obliku teorije grafova.

![steiner-tree2](./images/steiner-tree-2.svg)

U prvom obliku, ako su ključni vrhovi $\{1,2,3,4\}$, vidimo da je najmanji zbroj težina bridova kad izravno povežemo ta četiri ključna vrha jednak 12, što očito nije optimalno. Uzmemo li u obzir vrh 5, najmanji zbroj težina postaje 9, što je bolji odgovor.

U drugom obliku, ako su ključni vrhovi $\{1,2,3,4\}$, vidimo da neki od tih ključnih vrhova čak nisu izravno povezani bridom, pa je nužno upotrijebiti dodatne točke grananja (Steinerove točke). Uključimo li vrh 5, dobivamo najmanji zbroj težina 9.

Također primjećujemo da su u obje slike Steinerove točke kod vrhova 1 i 4 degenerirane, odnosno zamijenjene vrhovima 1 i 4.

## Primjeri

Prvo ćemo se upoznati s problemom minimalnog Steinerova stabla na zadatku-predlošku. Vidi [\[Predložak\] Minimalno Steinerovo stablo](https://www.luogu.com.cn/problem/P6192).

Zadatak je jasan: u povezanom grafu $G$ s $n$ vrhova zadano je $k$ ključnih vrhova; treba povezati tih $k$ ključnih vrhova tako da zbroj težina svih bridova dobivenog stabla bude najmanji.

Iz prethodnog znamo da zbroj težina pri izravnom povezivanju tih $k$ ključnih vrhova ne mora biti najmanji, ili da tih $k$ ključnih vrhova uopće nije izravno (susjedno) povezano. Zato treba iskoristiti preostalih $n-k$ vrhova.

Rješavamo dinamičkim programiranjem s bitmaskom. Neka $f(i,S)$ označava najmanji zbroj težina bridova stabla s korijenom $i$ koje sadrži sve vrhove iz skupa $S$.

Prijelazi stanja:

-   Prvo prijelaz po povezanim podskupovima: $f(i,S)\leftarrow \min(f(i,S),f(i,T)+f(i,S-T))$.

-   Zatim, za trenutno stanje povezanosti podskupa, relaksacija po bridovima: $f(i,S)\leftarrow \min(f(i,S),f(j,S)+w(j,i))$. U kodu niže `tree[tot]` čuva podatke o dvama susjednim vrhovima $i,j$.

??? note "Referentna implementacija"
    ```cpp
    --8<-- "docs/graph/code/steiner-tree/steiner-tree_1.cpp"
    ```

Još jedan klasičan primjer: [\[WC2008\] Plan razgledavanja](https://www.luogu.com.cn/problem/P4294).

Ovdje tražimo Steinerovo stablo s najmanjim zbrojem težina vrhova; $f(i,S)$ označava najmanji zbroj težina vrhova stabla s korijenom $i$ koje sadrži sve vrhove skupa $S$, a $a_i$ je težina vrha.

Prijelazi stanja:

-   $f(i,S)\leftarrow \min(f(i,S),f(i,T)+f(i,S-T)-a_i)$. Pri spajanju bi se težina $a_i$ istog vrha zbrojila dvaput, pa je oduzimamo.

-   $f(i,S)\leftarrow \min(f(i,S),f(j,S)+w(j,i))$.

Vidimo da su prijelazi slični onima u zadatku-predlošku; teži je dio ispis rješenja, jer tijekom DP-a treba pamtiti i put.

Niz `pre[i][s]` pamti iz kojeg je vrha i skupa izveden prijelaz u stanje s korijenom $i$ i skupom povezanosti $s$. Nakon DP-a krećemo od `pre[root][S]`, tražimo vrhove povezane s vrhovima skupa i postupno rastavljamo skup $S$; niz ans bilježi iskorištene vrhove, a pretraga završava kad je skup rastavljen do kraja.

??? note "Referentna implementacija"
    ```cpp
    --8<-- "docs/graph/code/steiner-tree/steiner-tree_2.cpp"
    ```

## Zadaci za vježbu

-   [\[Predložak\] Minimalno Steinerovo stablo](https://www.luogu.com.cn/problem/P6192)
-   [\[WC2008\] Plan razgledavanja](https://www.luogu.com.cn/problem/P4294)
-   [\[JLOI2015\] Spajanje cjevovoda](https://loj.ac/problem/2110)
-   [\[APIO2013\] Roboti](https://www.luogu.com.cn/problem/P3638)
