---
title: Dinamički DP
---

Preduvjeti: [Matrice](../math/linear-algebra/matrix.md), [Heavy-light dekompozicija](../graph/hld.md).

Dinamički DP (dynamic DP) tehnika je koju je autor „猫锟” predstavio na WC2018; obično se koristi za DP probleme na stablu u kojima se mijenjaju težine vrhova (bridova).

## Primjer

Postupak dinamičkog DP-a objasnit ćemo na ovom oglednom zadatku.

???+ note "Primjer [Luogu P4719 【Predložak】Dinamički DP](https://www.luogu.com.cn/problem/P4719)"
    Zadano je stablo s $n$ vrhova; vrhovi imaju težine. Slijedi $m$ operacija; u svakoj su zadani $x,y$ i treba težinu vrha $x$ promijeniti na $y$. Nakon svake operacije treba ispisati težinu najtežeg nezavisnog skupa tog stabla.

### Poopćeno množenje matrica

Poopćeno množenje matrica $A\times B=C$ definiramo ovako:

$$
C_{i,j}=\max_{k=1}^{n}(A_{i,k}+B_{k,j})
$$

To je kao obično množenje matrica u kojem je množenje zamijenjeno zbrajanjem, a zbrajanje operacijom $\max$.

Poopćeno množenje matrica također je asocijativno, pa se može koristiti brzo potenciranje matrica.

### Bez operacija izmjene

Neka $f_{i,0}$ označava najbolji odgovor kad $i$ nije odabran, a $f_{i,1}$ najbolji odgovor kad je $i$ odabran.

DP jednadžba je:

$$
\begin{cases}f_{i,0}=\sum_{son}\max(f_{son,0},f_{son,1})\\f_{i,1}=w_i+\sum_{son}f_{son,0}\end{cases}
$$

Odgovor je $\max(f_{root,0},f_{root,1})$.

### S operacijama izmjene

Najprije stablo rastavimo heavy-light dekompozicijom; pretpostavimo da imamo ovakav teški lanac:

![](./images/dynamic.png)

Neka $g_{i,0}$ označava najbolji odgovor kad $i$ nije odabran i smiju se birati samo vrhovi iz podstabala lake djece vrha $i$, a $g_{i,1}$ najbolji odgovor kad je $i$ odabran, bez uzimanja u obzir $son_i$; $son_i$ označava teško dijete vrha $i$.

Ako su $g_{i,0/1}$ poznati, DP jednadžba je:

$$
\begin{cases}f_{i,0}=g_{i,0}+\max(f_{son_i,0},f_{son_i,1})\\f_{i,1}=g_{i,1}+f_{son_i,0}\end{cases}
$$

Odgovor je $\max(f_{root,0},f_{root,1})$.

Možemo konstruirati matricu:

$$
\begin{bmatrix}
g_{i,0} & g_{i,0}\\
g_{i,1} & -\infty
\end{bmatrix}\times 
\begin{bmatrix}
f_{son_i,0}\\f_{son_i,1}
\end{bmatrix}=
\begin{bmatrix}
f_{i,0}\\f_{i,1}
\end{bmatrix}
$$

Pazite: ovdje koristimo pravilo poopćenog množenja.

Uočimo da pri izmjeni treba promijeniti samo $g_{i,1}$ i svaki teški lanac na putu prema gore.

### Konkretan postupak

1.  DFS-om unaprijed izračunamo $f_{i,0/1}$ i $g_{i,0/1}$.

2.  Stablo rastavimo heavy-light dekompozicijom (pazite: budući da za upit o vrhu trebamo izračunati umnožak matrica na intervalu od tog vrha do kraja njegova teškog lanca, za svaki vrh pamtimo $End_i$, indeks posljednjeg vrha teškog lanca u kojem se nalazi $i$); za svaki teški lanac izgradimo segment tree koji čuva matrice $g$ i umnoške matrica $g$ na intervalima.

3.  Pri izmjeni najprije promijenimo $g_{i,1}$ i matricu vrha $i$ u segment treeu, izračunamo promjenu matrice vrha $top_i$ i unesemo je u matricu vrha $fa_{top_i}$.

4.  Upit je umnožak na intervalu od vrha 1 do kraja njegova teškog lanca; na kraju uzmemo $\max$.

??? note "Implementacija"
    ```cpp
    --8<-- "docs/dp/code/dynamic/dynamic_1.cpp"
    ```

## Zadaci za vježbu

-   [SPOJ GSS3 - Can you answer these queries III](https://www.spoj.com/problems/GSS3/)
-   [„NOIP2018” Obrana kraljevstva](https://loj.ac/p/2955)
-   [„SDOI2017” Igra rezanja stabla](https://loj.ac/p/2269)
