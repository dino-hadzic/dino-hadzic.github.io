---
title: AVL stablo
---

AVL stablo vrsta je balansiranog binarnog stabla pretraživanja. Vrlo opširna objašnjenja AVL stabala u udžbenicima algoritama kod mnogih stvaraju dojam da su složena i nepraktična. No načelo rada AVL stabla zapravo je jednostavno, a ni implementacija nije složena.

## Svojstva

1.  Prazno binarno stablo jest AVL stablo.
2.  Ako je T AVL stablo, njegova su lijeva i desna podstabla također AVL stabla i vrijedi $|h(ls) - h(rs)| \leq 1$, gdje h označava visinu podstabla.
3.  Visina stabla je $O(\log n)$.

Faktor ravnoteže: visina desnog podstabla - visina lijevog podstabla.

???+ note "Dokaz visine stabla"
    Neka je $f_n$ najmanji broj čvorova u AVL stablu visine $n$. Tada vrijedi
    
    $$
    f_n=
    \begin{cases}
    1&(n=1)\\
    2&(n=2)\\
    f_{n-1}+f_{n-2}+1& (n>2)
    \end{cases}
    $$
    
    Prema rješenju nehomogene linearne diferencijske jednadžbe s konstantnim koeficijentima, $\{f_n+1\}$ je Fibonaccijev niz. Opći član niza $f_n$ glasi:
    
    $$
    f_n=\frac{5+2\sqrt{5}}{5}\left(\frac{1+\sqrt{5}}{2}\right)^n+\frac{5-2\sqrt{5}}{5}\left(\frac{1-\sqrt{5}}{2}\right)^n-1
    $$
    
    Fibonaccijev niz raste eksponencijalno, pa za visinu stabla $n$ vrijedi:
    
    $$
    n<\log_{\frac{1+\sqrt{5}}{2}} (f_n+1)<\frac{3}{2}\log_2 (f_n+1)
    $$
    
    Stoga je visina AVL stabla $O(\log f_n)$, gdje je $f_n$ broj čvorova.

## Postupak

### Umetanje čvora

Kao i u BST-u (binarnom stablu pretraživanja), najprije neuspješnim pretraživanjem određujemo mjesto umetanja. Nakon umetanja čvora prema faktoru ravnoteže odlučujemo treba li stablo prilagoditi.

### Brisanje čvora

Brisanje je slično onome u BST-u: zamijenimo čvor s njegovim sljedbenikom, a zatim ga izbrišemo.

Brisanje mijenja visinu stabla i faktore ravnoteže. Te promjene treba ispraviti duž puta od izbrisanog čvora do korijena.

### Održavanje ravnoteže

Umetanje ili brisanje čvora može narušiti svojstvo 2 AVL stabla. Zato treba održavati stablo duž puta od umetnutog/izbrisanog čvora do korijena. Ako za neki čvor svojstvo 2 više ne vrijedi, apsolutna vrijednost njegova faktora ravnoteže iznosi najviše 2, jer smo umetnuli/izbrisali samo jedan čvor, što visinu može promijeniti za najviše 1. Zbog simetrije razmatramo samo slučaj u kojem je lijevo podstablo za 2 više od desnog, odnosno $h(B)-h(E)=2$ na donjoj slici. Taj slučaj dodatno dijelimo na dva prema odnosu $h(A)$ i $h(C)$. Budući da ravnotežu održavamo odozdo prema gore, svojstvo 2 i dalje vrijedi za sve potomke čvora D.

![](./images/avl1.svg)

#### Slučaj 1: podstablo u A nije niže od podstabla u C

Neka je $h(E)=x$. Tada vrijedi

$$
\begin{cases}
    h(B)=x+2\\
    h(A)=x+1\\
    x\leq h(C)\leq x+1
\end{cases}
$$

Ovdje $h(C)\geq x$ vrijedi jer čvor B zadovoljava svojstvo 2, pa se $h(C)$ i $h(A)$ razlikuju za najviše 1. Sada izvedemo desnu rotaciju oko čvora D (rotacije su iste kao u drugim vrstama balansiranih binarnih stabala pretraživanja), kao na donjoj slici.

![](./images/avl2.svg)

Očito se visine čvorova A, C i E ne mijenjaju te vrijedi

$$
\begin{cases}
    0\leq h(C)-h(E)\leq 1\\
    x+1\leq h'(D)=\max(h(C),h(E))+1=h(C)+1\leq x+2\\
    0\leq h'(D)-h(A)\leq 1
\end{cases}
$$

Stoga i čvorovi B i D nakon rotacije zadovoljavaju svojstvo 2.

#### Slučaj 2: podstablo u A niže je od podstabla u C

Neka je $h(E)=x$. Slično prethodnom slučaju vrijedi

$$
\begin{cases}
    h(B)=x+2\\
    h(C)=x+1\\
    h(A)=x
\end{cases}
$$

Sada najprije izvedemo lijevu rotaciju oko čvora B, a zatim desnu oko čvora D, kao na donjoj slici.

![](./images/avl3.svg)

Očito se visine čvorova A i E ne mijenjaju. Novo desno dijete čvora B i novo lijevo dijete čvora D redom su izvorno lijevo i desno dijete čvora C, pa vrijedi

$$
\begin{cases}
    x-1\leq h'(rs_B),h'(ls_D)\leq x\\
    0\leq h(A)-h'(rs_B)\leq 1\\
    0\leq h(E)-h'(ls_D)\leq 1\\
    h'(B)=\max(h(A),h'(rs_B))+1=x+1\\
    h'(D)=\max(h(E),h'(ls_D))+1=x+1\\
    h'(B)-h'(D)=0
\end{cases}
$$

Stoga i čvorovi B, C i D nakon rotacija zadovoljavaju svojstvo 2.

???+ note "Održavanje ravnoteže: pseudokod"
    $$
    \begin{array}{ll}
    1 &  \textbf{function } \mathrm{MaintainBalance}(p) \\
    2 &  \qquad l \gets ls_p, r \gets rs_p \\
    3 &  \qquad \textbf{if } h(l)-h(r)=2 \\
    4 &  \qquad\qquad \textbf{if } h(ls_l) \ge h(rs_l) \\
    5 &  \qquad\qquad\qquad \mathrm{RightRotate}(p) \\
    6 &  \qquad\qquad \textbf{else} \\
    7 &  \qquad\qquad\qquad \mathrm{LeftRotate}(l) \\
    8 &  \qquad\qquad\qquad \mathrm{RightRotate}(p) \\
    9 &  \qquad \textbf{else if } h(l)-h(r)=-2 \\
    10 &  \qquad\qquad \textbf{if } h(ls_r) \le h(rs_r) \\
    11 &  \qquad\qquad\qquad \mathrm{LeftRotate}(p) \\
    12 &  \qquad\qquad \textbf{else} \\
    13 &  \qquad\qquad\qquad \mathrm{RightRotate}(r) \\
    14 &  \qquad\qquad\qquad \mathrm{LeftRotate}(p) \\
    \end{array}
    $$

Kao i kod drugih balansiranih binarnih stabala pretraživanja, pri rotacijama u AVL stablu treba ažurirati visinu čvora, veličinu podstabla i slične podatke.

## Ostale operacije

Ostale operacije AVL stabla (Predecessor, Successor, Select, Rank itd.) jednake su onima u običnom binarnom stablu pretraživanja.

## Referentni kod

Sljedeći kod implementira `Map`, odnosno uređeno preslikavanje bez ponovljenih ključeva, pomoću AVL stabla:

??? note "Referentni kod"
    ```cpp
    --8<-- "docs/ds/code/avl-tree/AvlTreeMap.hpp"
    ```

## Dodatni materijali

Postupak održavanja ravnoteže AVL stabla možete promatrati na stranici [AVL Tree Visualization](https://www.cs.usfca.edu/~galles/visualization/AVLtree.html).

[Wikipedia — AVL stablo](https://en.wikipedia.org/wiki/AVL_tree)
