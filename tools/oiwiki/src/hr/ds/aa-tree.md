---
title: AA stablo
---

AA stablo balansirana je struktura stabla za učinkovitu pohranu i dohvat uređenih podataka. Profesor Arne Andersson predstavio ju je 1993. u radu „Balanced search trees made simple”, s ciljem smanjenja broja različitih slučajeva koje razmatra crveno-crno stablo. AA stablo podržava pretraživanje, umetanje i brisanje u vremenu $O(\log N)$. Slijedi primjer AA stabla.

![aa-tree-1](images/aa-tree-1.jpg)

AA stablo inačica je crveno-crnog stabla, ali njegovi crveni čvorovi mogu biti samo desna djeca. Zbog toga AA stablo simulira 2-3 stablo, a ne 2-3-4 stablo, što znatno pojednostavnjuje održavanje. Algoritmi održavanja crveno-crnog stabla moraju razmotriti sedam različitih slučajeva kako bi ispravno uravnotežili stablo.

![red-black tree](images/aa-tree-2.svg)

Budući da crveni čvorovi mogu biti samo desna djeca, AA stablo treba razmotriti samo dva slučaja.

![aa-tree](images/aa-tree-3.svg)

## Definicija

AA stablo slijedi ista pravila kao crveno-crno stablo, uz dodatno pravilo: **crveni čvorovi ne smiju biti lijeva djeca**.

1.  Svaki čvor može biti crven ili crn.
2.  Korijen je uvijek crn.
3.  Listovi (NULL) uvijek su crni.
4.  Oba djeteta crvenog čvora moraju biti crna; nema dvaju susjednih crvenih čvorova.
5.  Svaki put od korijena do NULL čvora ima jednak broj crnih čvorova.
6.  Crveni čvorovi mogu biti samo desna djeca.

## Održavanje ravnoteže

Svaki čvor AA stabla održava polje **level**, slično polju color („RED” ili „BLACK”) u crveno-crnom stablu. Vrijednosti level zadovoljavaju sljedećih 5 uvjeta:

1. Level svakog lista iznosi 1.

2. Level svakog lijevog djeteta za 1 je manji od levela njegova roditelja.

3. Level svakog desnog djeteta jednak je levelu njegova roditelja ili je za 1 manji.

4. Level svakog desnog unuka strogo je manji od levela njegova djeda.

5. Svaki čvor s levelom većim od 1 ima dvoje djece.

![aa-tree-4](images/aa-tree-4.jpg)

### Horizontalna veza (Horizontal Link)

Vezu u kojoj dijete ima isti level kao roditelj nazivamo **horizontalnom vezom**, slično crvenoj vezi u crveno-crnom stablu. Dopuštena je pojedinačna desna horizontalna veza, ali ne i uzastopne desne horizontalne veze; lijeve horizontalne veze nisu dopuštene. Ta su ograničenja stroža od onih u crveno-crnom stablu, pa je postupak balansiranja AA stabla programski znatno jednostavniji.

![aa-tree-5](images/aa-tree-5.jpg)

Umetanje i brisanje mogu privremeno narušiti ravnotežu AA stabla (odnosno njegove invarijante). Za obnovu ravnoteže potrebne su samo dvije operacije: **skew** (ukošavanje) i **split** (razdvajanje). Skew desnom rotacijom pretvara podstablo s lijevom horizontalnom vezom u podstablo s desnom horizontalnom vezom. Split izvodi lijevu rotaciju i povećava level, pretvarajući podstablo s dvjema ili više uzastopnih desnih horizontalnih veza u podstablo s dvije takve veze manje. Implementacije umetanja i brisanja dodatno se pojednostavnjuju tako što same operacije skew i split mijenjaju stablo samo kada je potrebno, umjesto da pozivatelj odlučuje treba li ih izvesti.

### split (lijeva rotacija)

Pojavljuje se niz uzastopnih desnih horizontalnih veza (tri uzastopna čvora udesno imaju isti level, a čvorovi R i X crveni su).

Tada rotiramo čvor *T* ulijevo, promatrajući čvorove čiji je level manji ili jednak tom levelu kao jedno podstablo.

1.  Desno dijete korijena podstabla postaje novi korijen podstabla;
2.  Stari korijen postaje lijevo dijete novog korijena;
3.  Level novog korijena povećava se za 1.

![aa-tree-split](images/aa-tree-split.svg)

???+ note "Implementacija u pseudokodu"
    $$
    \begin{array}{ll}
    1 & \textbf{function } \text{split}(\text{root}) \\
    2 & \qquad \textbf{if } \text{root}\rightarrow\text{right}\rightarrow\text{right}\rightarrow\text{level} == \text{root}\rightarrow\text{level} \\
    3 & \qquad\qquad \text{rotate\_left}(\text{root}) \\
    4 & \textbf{end function}
    \end{array}
    $$

### skew (desna rotacija)

Pojavljuje se lijeva horizontalna veza (dva uzastopna čvora ulijevo imaju isti level).

Rotiramo čvor *T* udesno, promatrajući čvorove čiji je level manji ili jednak tom levelu kao jedno podstablo.

1.  Lijevo dijete korijena podstabla postaje novi korijen podstabla;
2.  Stari korijen postaje desno dijete novog korijena.

![aa-tree-skew](images/aa-tree-skew.svg)

???+ note "Implementacija u pseudokodu"
    $$
    \begin{array}{ll}
    1 & \textbf{function } \text{skew}(\text{root}) \\
    2 & \qquad \textbf{if } \text{root}\rightarrow\text{left}\rightarrow\text{level} == \text{root}\rightarrow\text{level} \\
    3 & \qquad\qquad \text{rotate\_right}(\text{root}) \\
    4 & \textbf{end function}
    \end{array}
    $$

## Operacije AA stabla

AA stablo ujedno je binarno stablo pretraživanja, pa je pretraživanje isto kao u drugim binarnim stablima pretraživanja. Umetanje i brisanje slični su onima u *AVL* stablu: najprije umetnemo ili izbrišemo ključ, a zatim se vraćamo duž puta pretraživanja prema korijenu i pritom preoblikujemo stablo.

### Umetanje

???+ note "Implementacija u pseudokodu"
    $$
    \begin{array}{ll}
    1 & \textbf{function } \text{insert}(\text{root}, \text{add}) \\
    2 & \qquad \textbf{if } \text{root} == \text{NULL} \\
    3 & \qquad\qquad \text{root} \gets \text{add} \\
    4 & \qquad \textbf{else if } \text{add}\rightarrow\text{key} < \text{root}\rightarrow\text{key} \qquad //Ako su ponavljanja dopuštena<= \\ 
    5 & \qquad\qquad \text{insert}(\text{root}\rightarrow\text{left}, \text{add}) \\
    6 & \qquad \textbf{else if } \text{add}\rightarrow\text{key} > \text{root}\rightarrow\text{key} \\
    7 & \qquad\qquad \text{insert}(\text{root}\rightarrow\text{right}, \text{add}) \\
    8 & \qquad \textbf{end if} \\
    9 & \qquad \text{//Ako ponavljanja nisu dopuštena, izvedi skew i split na svakoj razini} \\
    10 & \qquad \text{skew}(\text{root}); \\
    11 & \qquad \text{split}(\text{root}); \\
    12 & \textbf{end function}
    \end{array}
    $$

### Brisanje

Brisanje je slično onome u drugim balansiranim binarnim stablima: brisanje unutarnjeg čvora najprije svodimo na brisanje lista. Unutarnji čvor zamijenimo njegovim najbližim prethodnikom ili sljedbenikom. Budući da u AA stablu svi čvorovi s levelom većim od 1 imaju dvoje djece, prethodnik ili sljedbenik bit će na levelu 1, gdje je brisanje jednostavnije.

???+ note "Implementacija u pseudokodu"
    $$
    \begin{array}{ll}
    1 &  \text{//To rebalance the tree} \\
    2 &  \textbf{if} \ \text{root->left->level} < \text{root->level} -1 \ \textbf{or} \ \text{root->right->level} < \text{root->level} -1 \\
    3 &  \{ \\
    4 & \qquad \textbf{if} \ \text{root->right->level} > \text{--root->level} \\
    5 & \qquad \{ \\
    6 & \qquad\qquad \text{root->right->level} \gets \text{root->level} \\
    7 & \qquad \} \\
    8 & \qquad \text{skew}(\text{root}) \\
    9 & \qquad \text{skew}(\text{root->right}) \\
    10 & \qquad \text{skew}(\text{root->right->right}) \\
    11 & \qquad \text{split}(\text{root}) \\
    12 & \qquad \text{split}(\text{root->right}) \\
    13 &  \} \\
    \end{array}
    $$

## Učinkovitost

Učinkovitost AA stabla usporediva je s učinkovitošću crveno-crnog stabla. Iako AA stablo izvodi više rotacija, njegovi su algoritmi jednostavniji, pa je konačna učinkovitost slična. Crveno-crna stabla u različitim slučajevima imaju ujednačeniju učinkovitost, dok su AA stabla obično plića, što im daje nešto brže pretraživanje.

## Literatura

1.  [AA tree - Wikipedia](https://en.wikipedia.org/wiki/AA_tree)
2.  [Introduction to AA trees](https://iq.opengenus.org/aa-trees/)
3.  [AA tree - Visualization](https://kubokovac.eu/gnarley-trees/AAtree.html)
4.  [CMSC 420 Lecture 6: 2-3, Red-black, and AA trees](https://www.cs.umd.edu/class/fall2019/cmsc420-0201/Lects/lect06-aa.pdf)
