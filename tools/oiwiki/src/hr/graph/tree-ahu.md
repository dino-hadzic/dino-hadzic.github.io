---
title: AHU algoritam
---

AHU algoritam služi za provjeru jesu li dva korijenska stabla izomorfna.

Osim njega, čest način provjere izomorfizma stabala jest [hash stabla](tree-hash.md).

Preduvjeti: [Osnove stabala](tree-basic.md), [Centroid stabla](tree-centroid.md)

Preporučujemo čitanje uz primjere iz literature navedene na kraju.

## Definicija izomorfizma stabala

### Izomorfizam korijenskih stabala

Za dva korijenska stabla $T_1(V_1,E_1,r_1)$ i $T_2(V_2,E_2,r_2)$, ako postoji bijekcija $\varphi: V_1 \rightarrow V_2$ takva da

$$
\forall u,v \in V_1,(u,v) \in E_1 \iff (\varphi(u),\varphi(v))  \in E_2
$$

**i** $\varphi(r_1)=r_2$, kažemo da su korijenska stabla $T_1(V_1,E_1,r_1)$ i $T_2(V_2,E_2,r_2)$ izomorfna.

### Izomorfizam nekorijenskih stabala

Za dva nekorijenska stabla $T_1(V_1,E_1)$ i $T_2(V_2,E_2)$, ako postoji bijekcija $\varphi: V_1 \rightarrow V_2$ takva da

$$
\forall u,v \in V_1,(u,v) \in E_1 \iff (\varphi(u),\varphi(v))  \in E_2
$$

kažemo da su nekorijenska stabla $T_1(V_1,E_1)$ i $T_2(V_2,E_2)$ izomorfna.

Jednostavno rečeno: ako se prenumeriranjem svih vrhova stabla $T_1$ može postići da stabla $T_1$ i $T_2$ budu **potpuno jednaka**, ta su dva stabla izomorfna.

## Svođenje problema

Problem izomorfizma nekorijenskih stabala može se svesti na problem izomorfizma korijenskih stabala. Postupak je sljedeći:

Za nekorijenska stabla $T_1(V_1, E_1)$ i $T_2(V_2,E_2)$ najprije u svakom pronađemo **sve** centroide.

-   Ako stabla imaju različit broj centroida, nisu izomorfna.
-   Ako oba stabla imaju po $1$ centroid, označimo ih $c_1$ i $c_2$; tada su nekorijenska stabla $T_1(V_1, E_1)$ i $T_2(V_2,E_2)$ izomorfna ako i samo ako su korijenska stabla $T_1(V_1,E_1,c_1)$ i $T_2(V_2,E_2,c_2)$ izomorfna.
-   Ako oba stabla imaju po $2$ centroida, označimo ih $c_1,c'_1$ odnosno $c_2,c'_2$; tada su nekorijenska stabla $T_1(V_1, E_1)$ i $T_2(V_2,E_2)$ izomorfna ako i samo ako su korijenska stabla $T_1(V_1,E_1,c_1)$ i $T_2(V_2,E_2,c_2)$ izomorfna **ili** su korijenska stabla $T_1(V_1,E_1,c'_1)$ i $T_2(V_2,E_2,c_2)$ izomorfna.

Dakle, čim riješimo problem izomorfizma korijenskih stabala, gornjim postupkom možemo problem izomorfizma nekorijenskih stabala svesti na njega i tako ga riješiti.

Ako postoji algoritam koji izomorfizam korijenskih stabala rješava u $O(\left|V\right|)$, gornjim postupkom i izomorfizam nekorijenskih stabala rješavamo u $O(\left|V\right|)$.

## Naivni AHU algoritam

Naivni AHU algoritam temelji se na zagradnom zapisu stabla.

### Načelo 1

Znamo da valjani niz zagrada jednoznačno odgovara korijenskom stablu i da je zagradni zapis stabla nastao spajanjem zagradnih zapisa njegovih podstabala. Ako promjenom redoslijeda spajanja zapisa podstabala dobijemo novi zagradni zapis, stablo koje mu odgovara izomorfno je stablu izvornog zapisa.

### Načelo 2

Izomorfizam stabala je tranzitivan: ako su $T_1$ i $T_2$ izomorfna te $T_2$ i $T_3$ izomorfna, onda su i $T_1$ i $T_3$ izomorfna.

### Posljedica

Promotrimo rekurzivni algoritam za zagradni zapis stabla, u kojem pri povratku iz rekurzije spajamo zapise podstabala. Pri spajanju najprije stavljamo leksikografski manje nizove, a konačni rezultat označimo $NAME$.

Ako $NAME$ podstabla s korijenom $r$ uzmemo kao $NAME$ vrha $r$ i označimo ga $NAME(r)$, tada za korijenska stabla $T_1(V_1,E_1,r_1)$ i $T_2(V_2,E_2,r_2)$ vrijedi: ako je $NAME(r_1)=NAME(r_2)$, stabla $T_1$ i $T_2$ su izomorfna.

### Algoritam imenovanja

???+ note "Implementacija"
    $$
    \begin{array}{ll}
    1 & \textbf{Input. } \text{A rooted tree }T\\
    2 & \textbf{Output. } \text{The name of rooted tree }T\\
    3 & \text{ASSIGN-NAME(u)}\\
    4 & \qquad \text{if  } u \text{  is a leaf}\\
    5 & \qquad \qquad \text{NAME(} u \text{) = (0)}\\
    6 & \qquad \text{else }\\
    7 & \qquad \qquad \text{for all child } v \text{ of } u\\
    8 & \qquad \qquad \qquad \text{ASSIGN-NAME(}v\text{)}\\
    9 & \qquad \text{sort the names of the children of }u\\
    10 & \qquad \text{concatenate the names of all children }u\text{ to temp}\\
    11 & \qquad \text{NAME(} u \text{) = (temp)}
    \end{array}
    $$

### AHU algoritam

???+ note "Implementacija"
    $$
    \begin{array}{ll}
    1 & \textbf{Input. } \text{Two rooted trees }T_1(V_1,E_1,r_1)\text{ and }T_2(V_2,E_2,r_2) \\
    2 & \textbf{Output. } \text{Whether these two trees are isomorphic}\\
    3 & \text{AHU}(T_1(V_1,E_1,r_1), T_2(V_2,E_2,r_2))\\
    4 & \qquad \text{ASSIGN-NAME(}r_1\text{)}\\
    5 & \qquad \text{ASSIGN-NAME(}r_2\text{)}\\
    6 & \qquad \text{if  NAME}(r_1) = \text{NAME}(r_2)\\
    7 & \qquad \qquad \text{return true}\\
    8 & \qquad \text{else}\\
    10 & \qquad \qquad \text{return false}
    \end{array}
    $$

### Dokaz složenosti

Za korijensko stablo s $n$ vrhova koje je lanac, duljina imena vrha može biti do $n$, pa je složenost algoritma ASSIGN-NAME konstantni višekratnik od $1+2+\cdots+n$, tj. $\Theta(n^2)$. Stoga je složenost naivnog AHU algoritma $O(n^2)$.

## Optimizirani AHU algoritam

Nedostatak naivnog AHU algoritma jest to što $NAME$ stabla može biti predugačak; upravo to možemo optimizirati.

### Načelo 1

Podijelimo stablo na razine: vrhovi $i$-te razine na najkraćoj su udaljenosti $i$ od korijena. $NAME$ vrha na $i$-toj razini može se dobiti **samo** spajanjem $NAME$-ova vrhova na razini $i+1$.

### Načelo 2

Unutar iste razine $NAME$ vrha jednoznačno je određen njegovim rangom unutar razine.

**Pozor**: rang se ovdje računa nad oba stabla. Ako je vrh $u$ na $i$-toj razini, njegov je rang jednak broju vrhova na $i$-toj razini stabala $T_1$ i $T_2$ čiji je $NAME$ manji od $NAME(u)$.

### Posljedica

Izvorni $NAME$ vrha možemo zamijeniti njegovim rangom unutar razine, a spajanje $NAME$-ova zamijeniti dodavanjem elemenata u niz.

Zamjena stringova cijelim brojevima i nizovima ne narušava ispravnost algoritma, a znatno smanjuje njegovu složenost.

### Dokaz složenosti

Najprije uočimo da je ukupna duljina spojenih $NAME$-ova na $i$-toj razini jednaka zbroju stupnjeva vrhova $i$-te razine, tj. broju vrhova razine $i+1$; označimo ga $L_i$. U sljedećem koraku algoritam te $NAME$-ove promatra kao stringove (nizove), sortira ih i zamjenjuje rangom unutar razine (tj. preslikava ih u broj). Sljedeće leme daju složenost sortiranja $m$ stringova ukupne duljine $L$:

1.  Radix sortom možemo sortirati u $O(L+|\Sigma|)$, gdje je $|\Sigma|$ veličina alfabeta. (Postoje neki detalji implementacije, vidi literaturu.)
2.  Quick sortom možemo sortirati u $O(L \log m)$. Skica dokaza: visina rekurzivnog stabla quick sorta je $O(\log m)$, a izravna usporedba dvaju stringova duljina $\ell_1$ i $\ell_2$ stoji $O(\min\{\ell_1,\ell_2\})$.

U AHU algoritmu veličina alfabeta stringova $i$-te razine najviše je broj vrhova razine $i+1$, tj. $L_i$, pa je radix sort linearan. Zbog $\sum_i L_i=O(n)$, zbrajanjem složenosti svih razina vidimo da je, uz radix sort stringova, ukupna složenost algoritma $T(n)=O(n)$. Analogno, ako stringove sortiramo quick sortom, $T(n)=O(n \log n)$.

## Primjer

[SPOJ-TREEISO](https://www.spoj.com/problems/TREEISO/en/)

Sažetak zadatka: zadana su dva nekorijenska stabla; odredite jesu li izomorfna.

???+ note "Referentni kod"
    ```cpp
    --8<-- "docs/graph/code/tree-ahu/tree-ahu_1.cpp"
    ```

## Literatura

Većina ovog članka prevedena je iz [članka](http://wwwmayr.in.tum.de/konferenzen/Jass08/courses/1/smal/Smal_Paper.pdf) i [prezentacije](https://logic.pdmi.ras.ru/~smal/files/smal_jass08_slides.pdf). Dokazi u literaturi potpuniji su i strože provedeni; ovaj ih članak donekle pojednostavnjuje.

Za analizu složenosti AHU algoritma i linearni radix sort stringova vidi odjeljak 3.2 Radix sorting u knjizi The Design and Analysis of Computer Algorithms, posebno Example 3.2.
