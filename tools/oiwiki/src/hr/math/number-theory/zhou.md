---
title: Zhou sito
---

## Predznanje

-   [Multiplikativne funkcije](./basic.md#multiplikativne-funkcije)

## Definicija

Zhou sito (洲阁筛, Zhou's sieve) jest metoda sita koja u sublinearnoj vremenskoj složenosti može izračunati prefiksne sume većine multiplikativnih funkcija.

U nastavku ćemo na primjeru računanja $\displaystyle\sum_{i=1}^nf(i)$ detaljno objasniti princip Zhou sita.

## Oznake

-   $\mathbb P$ označava skup prostih brojeva, a $p_i$ označava $i$-ti prost broj.
-   $m$ označava broj prostih brojeva koji ne prelaze $\sqrt n$.

## Zahtjevi

Za $p\in\mathbb P,c\in\mathbb N$ vrijednost $f(p^c)$ polinom je niskog stupnja u $p$.

## Ideja

-   Svaki cijeli broj iz $[1,n]$ ima najviše jedan prost faktor $>\sqrt n$.
-   Iskorištava se svojstvo da $\left\lfloor\dfrac ni\right\rfloor(i\in[1,n]\cap\mathbb N)$ poprima samo oko $\sqrt n$ različitih vrijednosti, čime se smanjuje vremenska složenost.

## Postupak

Sve cijele brojeve iz $[1,n]$ podijelimo u dvije klase prema tome imaju li prost faktor $>\sqrt n$:

$$
\sum_{i=1}^nf(i)=\sum_{i=1}^n\left[\exists d\in(\sqrt n,n]\cap\mathbb P,d\mid i\right]f(i)+\sum_{i=1}^n\left[\forall d\in(\sqrt n,n]\cap\mathbb P,d\nmid i\right]f(i)
$$

Za prvi dio nabrajamo najveći faktor te ga, prema svojstvima multiplikativnih funkcija, možemo preoblikovati:

$$
\sum_{i=1}^nf(i)=\sum_{i=1}^{\sqrt n}f(i)\cdot\left(\sum_{d=\lfloor\sqrt n\rfloor+1}^{\lfloor\frac ni\rfloor}[d\in\mathbb P]f(d)\right)+\sum_{i=1}^n\left[\forall d\in(\sqrt n,n]\cap\mathbb P,d\nmid i\right]f(i)
$$

Prvi i drugi dio mogu se računati odvojeno.

### Dio 1

> Izračunati $\displaystyle\sum_{i=1}^{\sqrt n}f(i)\cdot\left(\sum_{d=\lfloor\sqrt n\rfloor+1}^{\lfloor\frac ni\rfloor}[d\in\mathbb P]f(d)\right)$.

Nabrajamo $i$, a zatim u $O(1)$ računamo dio u zagradi.

Označimo $\displaystyle g(t,l)=\sum_{i=1}^l[\forall j\in[1,t],\gcd(i,p_j)=1]f(i)$, tj. zbroj vrijednosti $f$ svih brojeva iz $[1,l]$ koji su relativno prosti sa svakim od $p_1,p_2,\dots,p_t$.

Tako se računanje Dijela 1 svodi na $\displaystyle\sum_{i=1}^{\sqrt n}f(i)\cdot g\left(m,\left\lfloor\frac ni\right\rfloor\right)$.

Rubni je uvjet $g(0,l)=\sum_{i=1}^lf(i)$, a prijelaz $g(t,l)=g(t-1,l)-f(p_t)\cdot g\left(t-1,\left\lfloor\frac l{p_t}\right\rfloor\right)$.

$l$ poprima oko $\sqrt n$ različitih vrijednosti, a za svaku od njih treba nabrojiti proste brojeve, pa je složenost $\displaystyle O\left(\frac{\sqrt n}{\ln\sqrt n}\cdot\sqrt n\right)= O\left(\frac n{\log n}\right)$, što treba optimizirati.

Uočimo da kada je $p_{t+1}^2>l$, jedini broj koji zadovoljava uvjet jest $1$, pa je tada $g(t,l)=f(1)=1$.

Uvrštavanjem u rekurziju dobivamo: kada je $p_t^2>l$, vrijedi $g(t,l)=g(t-1,l)-f(p_t)$.

Stoga, čim ustanovimo $p_t^2>l$, prestajemo s prijelazima; označimo tadašnji $t$ s $t_l$, pa je $\forall t>t_l,g(t,l)=g(t_l,l)-\sum_{i=t_l}^{t-1}f(p_i)$.

Predračunom prefiksnih suma vrijednosti $f$ na prostim brojevima možemo brzo izračunati $g$, a vremenska složenost smanjuje se na $O\left(\dfrac{n^{\frac34}}{\log n}\right)$.

### Dio 2

> Izračunati $\displaystyle\sum_{i=1}^n\left[\forall d\in(\sqrt n,n]\cap\mathbb P,d\nmid i\right]f(i)$.

Označimo $\displaystyle h(t,l)=\sum_{i=1}^l\left[i=\prod_{j=t}^mp_j^{c_j},c_j\in\mathbb N\right]f(i)$, tj. zbroj vrijednosti $f$ svih brojeva iz $[1,l]$ koji sadrže samo proste faktore $p_t,p_{t+1},\dots,p_m$.

Dio 2 upravo je $h(0,n)$.

Rubni je uvjet $h(m+1,l)=1$, a prijelaz $\displaystyle h(t,l)=h(t+1,l)+\sum_{c\in\mathbb N^*}f(p_t^c)\cdot h\left(t+1,\left\lfloor\frac l{p_t^c}\right\rfloor\right)$.

$l$ poprima oko $\sqrt n$ različitih vrijednosti, pa je složenost izravnih prijelaza $\displaystyle O\left(\sqrt n\cdot\frac{\sqrt n}{\ln\sqrt n}\right)= O\left(\frac n{\log n}\right)$, što treba optimizirati.

Slično optimizaciji za $g$, uočimo da kada je $p_t>l$, jedini broj koji se može sastaviti od $p_t,p_{t+1},\dots,p_m$ jest $1$, pa je tada $h(t,l)=f(1)=1$.

Analogno izvodimo $\forall p_t^2>l,h(t,l)=h(t+1,l)+f(p_t)$.

Stoga, čim ustanovimo $p_t^2>l$, prestajemo s prijelazima; označimo tadašnji $t$ s $t_l$, a kad kasnije trebamo $h$, tadašnjoj vrijednosti $h$ dodamo $\displaystyle\sum_{i=p_{t_l}}^{\min(l,\sqrt n)}[i\in\mathbb P]f(i)$.

Vremenska složenost smanjuje se na $O\left(\dfrac{n^{\frac34}}{\log n}\right)$.

### Zbrajanje

Kad izračunamo odgovore Dijela 1 i Dijela 2, njihov je zbroj upravo $\displaystyle\sum_{i=1}^nf(i)$.

## Literatura

[积性函数线性筛/杜教筛/洲阁筛学习笔记 (Bilješke o linearnom situ, Du situ i Zhou situ za multiplikativne funkcije) | Bill Yang's Blog](https://blog.bill.moe/multiplicative-function-sieves-notes)
