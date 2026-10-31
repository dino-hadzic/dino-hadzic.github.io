---
title: Newtonova iteracija za polinome
---

## Opis

Zadan je polinom $G\left(x, y\right)$ i poznato je da polinom $f\left(x\right)$ zadovoljava:

$$
G\left(x, f\left(x\right)\right)\equiv 0\pmod{x^{n}}
$$

te da postoji vrijednost $f_1$ takva da $G\left(x, y\right)$ zadovoljava sljedeće uvjete:

-   $G(0, f_1) = 0$;
-   $\dfrac{\partial G}{\partial y}(0, f_1) \neq 0$.

Treba odrediti $f\left(x\right)$ modulo $x^{n}$.

## Newtonova metoda

Razmotrimo udvostručavanje.

Najprije, za $n=1$ rješenje jednadžbe $\left[x^{0}\right]G\left(x, f\left(x\right)\right)=0$ treba odrediti zasebno; $f_1$ iz pretpostavke upravo je jedno takvo rješenje.

Pretpostavimo da smo već dobili rješenje $f_{\left\lceil\frac{n}{2}\right\rceil}\left(x\right)$ modulo $x^{\left\lceil\frac{n}{2}\right\rceil}$ i da tražimo rješenje $f\left(x\right) = f_n\left(x\right)$ modulo $x^{n}$.

Razvijemo li $G\left(x, f(x)\right)$ u Taylorov red po $f(x)$ oko $f(x)=f_{\left\lceil\frac{n}{2}\right\rceil}\left(x\right)$, dobivamo:

$$
\sum_{i=0}^{+\infty}\frac{\frac{\partial^i G}{\partial y^i}\left(x, f_{\left\lceil\frac{n}{2}\right\rceil}\left(x\right)\right)}{i!}\left(f\left(x\right)-f_{\left\lceil\frac{n}{2}\right\rceil}\left(x\right)\right)^{i}\equiv 0\pmod{x^{n}}
$$

Budući da je stupanj najnižeg nenul člana polinoma $f\left(x\right)-f_{\left\lceil\frac{n}{2}\right\rceil}\left(x\right)$ barem $\left\lceil\frac{n}{2}\right\rceil$, vrijedi:

$$
\forall 2\leqslant i:\left(f\left(x\right)-f_{\left\lceil\frac{n}{2}\right\rceil}\left(x\right)\right)^{i}\equiv 0\pmod{x^{n}}
$$

Stoga:

$$
\begin{aligned}
\sum_{i=0}^{+\infty}\frac{\frac{\partial^i G}{\partial y^i}\left(x, f_{\left\lceil\frac{n}{2}\right\rceil}\left(x\right)\right)}{i!}\left(f\left(x\right)-f_{\left\lceil\frac{n}{2}\right\rceil}\left(x\right)\right)^{i}&\equiv G\left(x, f_{\left\lceil\frac{n}{2}\right\rceil}\left(x\right)\right)+\frac{\partial G}{\partial y}\left(x, f_{\left\lceil\frac{n}{2}\right\rceil}\left(x\right)\right)\left[f\left(x\right)-f_{\left\lceil\frac{n}{2}\right\rceil}\left(x\right)\right]\\
&\equiv 0\pmod{x^{n}}
\end{aligned}
$$

$$
f_n\left(x\right)\equiv f_{\left\lceil\frac{n}{2}\right\rceil}\left(x\right)-\frac{G\left(x, f_{\left\lceil\frac{n}{2}\right\rceil}\left(x\right)\right)}{\frac{\partial G}{\partial y}\left(x, f_{\left\lceil\frac{n}{2}\right\rceil}\left(x\right)\right)}\pmod{x^{n}}
$$

odnosno

$$
f_{2n}\left(x\right)\equiv f_n\left(x\right)-\frac{G\left(x, f_n\left(x\right)\right)}{\frac{\partial G}{\partial y}\left(x, f_n\left(x\right)\right)}\pmod{x^{2n}}
$$

## Primjeri zadataka

### [Inverz polinoma](./elementary-func.md#inverz-polinoma)

Neka je zadana funkcija $h\left(x\right)$; imamo:

$$
G\left(x, y\right)=\frac{1}{y}-h\left(x\right)
$$

Primjenom Newtonove metode dobivamo:

$$
\begin{aligned}
    f_{2n}\left(x\right)&\equiv f_{n}\left(x\right)-\frac{1/f_{n}\left(x\right)-h\left(x\right)}{-1/f_{n}^{2}\left(x\right)}&\pmod{x^{2n}}\\
    &\equiv 2f_{n}\left(x\right)-f_{n}^{2}\left(x\right)h\left(x\right)&\pmod{x^{2n}}
\end{aligned}
$$

Vremenska složenost

$$
T\left(n\right)=T\left(\frac{n}{2}\right)+O\left(n\log{n}\right)=O\left(n\log{n}\right)
$$

### [Korijen polinoma](./elementary-func.md#korijen-polinoma)

Neka je zadana funkcija $h\left(x\right)$; imamo:

$$
G\left(x, y\right)=y^{2}-h\left(x\right)\equiv 0
$$

Primjenom Newtonove metode dobivamo:

$$
\begin{aligned}
    f_{2n}\left(x\right)&\equiv f_{n}\left(x\right)-\frac{f_{n}^{2}\left(x\right)-h\left(x\right)}{2f_{n}\left(x\right)}&\pmod{x^{2n}}\\
    &\equiv\frac{f_{n}^{2}\left(x\right)+h\left(x\right)}{2f_{n}\left(x\right)}&\pmod{x^{2n}}
\end{aligned}
$$

Vremenska složenost

$$
T\left(n\right)=T\left(\frac{n}{2}\right)+O\left(n\log{n}\right)=O\left(n\log{n}\right)
$$

### [Eksponencijal polinoma](./elementary-func.md#logaritam-i-eksponencijalna-funkcija-polinoma)

Neka je zadana funkcija $h\left(x\right)$; imamo:

$$
G\left(x, y\right)=\ln{y}-h\left(x\right)
$$

Primjenom Newtonove metode dobivamo:

$$
\begin{aligned}
    f_{2n}\left(x\right)&\equiv f_{n}\left(x\right)-\frac{\ln{f_{n}\left(x\right)}-h\left(x\right)}{1/f_{n}\left(x\right)}&\pmod{x^{2n}}\\
    &\equiv f_{n}\left(x\right)\left(1-\ln{f_{n}\left(x\right)+h\left(x\right)}\right)&\pmod{x^{2n}}
\end{aligned}
$$

Vremenska složenost

$$
T\left(n\right)=T\left(\frac{n}{2}\right)+O\left(n\log{n}\right)=O\left(n\log{n}\right)
$$

## Demonstracija ručnog računanja

Radi lakšeg razumijevanja, ovdje na nekoliko primjera demonstriramo tijek algoritma.

### Kvadratni korijen kompleksnog polinoma modulo polinom

Pretpostavimo da je $h$ kompleksni polinom koji nije djeljiv s $x$ (ima slobodni član) i da tražimo njegov kvadratni korijen modulo $x^n$.

Imamo jednadžbu:

$$
G\left(f(x)\right) = f^2(x)-h(x) \equiv 0\pmod{x^{n}}
$$

Taylorovim razvojem $G$ dobivamo sljedeći izraz. Uočimo da je ovo razvoj po $f$, pa su sve derivacije parcijalne derivacije po $f$, a $x$ se ovdje tretira kao konstanta.

$$
G(f(x)) = \sum_{i=0}^{+\infty}\frac{G^{\left(i\right)}\left(f_{0}(x)\right)}{i!}\left(f(x)-f_{0}(x)\right)^{i}
= G(f_0(x)) + 2f_0(x)(f(x)-f_0(x)) + (f(x)-f_0(x))^2
$$

Računamo udvostručavanjem. Pretpostavimo da su međurezultati udvostručavanja $f_0(x), f_1(x), \ldots, f_j(x)$, ili, matematički strogo, da je $f_j(x)$ kompleksni polinom koji zadovoljava $G(f_j(x))\equiv 0\pmod{x^{2^j}}$ te, radi jedinstvenosti, istodobno zadovoljava sljedeća dva uvjeta:

-   stupanj $f_{j}(x)$ ne prelazi $x^{2^j}$;
-   $f_{j+k}(x)-f_j(x)\equiv 0\pmod{x^{2^j}}$ za sve $k$.

Uvrštavanjem $f_{j+1}(x)$ i $f_j(x)$ u gornji izraz dobivamo:

$$
G(f_{j+1}(x)) = G(f_j(x)) + 2f_j(f_{j+1}(x)-f_j(x)) + (f_{j+1}(x)-f_{j}(x))^2  \equiv 0 \pmod{x^{2^{j+1}}}
$$

Očito $f_{j+1}(x)-f_j(x)$ mora biti višekratnik od $x^{2^j}$. Tako dobivamo

$$
f_{j+1}(x) \equiv f_j(x) - \frac{f_j^2(x)-h(x)}{2f_j(x)} \equiv \frac{f_j(x)^2 + h(x)}{2f_j(x)} \pmod{x^{2^{j+1}}}
$$

Ako $f_j(x)$ postoji, tada $2f_j(x)$ nije djeljiv s $x$ (ima slobodni član), pa nužno ima inverz modulo $x^{2^{j+1}}$. Stoga niz $f_0,f_1\ldots,f_j$ postoji ako i samo ako postoji $f_0$. Kvadratni korijen kompleksnog polinoma $h(x)$ koji nije djeljiv s $x$ modulo $x$ sigurno postoji, jer je $h(x)$ modulo $x$ obični kompleksni broj različit od nule, koji sigurno ima dva kvadratna korijena. Zato se ovaj algoritam može primijeniti na sve $h(x)$ sa slobodnim članom.

Za primjer uzmimo $h(x)=x+1$; računanje izgleda ovako:

-   $f_0(x)=1$,$f_1(x)=\dfrac{1^2+x+1}{2\times 1}\mod x^2 = \dfrac{1}{2}x+1$,$f_2(x)=\dfrac{\left(\dfrac{1}{2}x+1\right)^2+x+1}{2\times \left(\dfrac{1}{2}x+1\right)}\mod x^4 = \dfrac{1}{16}x^3-\dfrac{1}{8}x^2+\dfrac{1}{2}x+1$,$\ldots$
-   $f_0(x)=-1$,$f_1(x)=\dfrac{(-1)^2+x+1}{2\times (-1)}\mod x^2 = -\dfrac{1}{2}x-1$,$\ldots$ (jednako prethodnom s promijenjenim predznakom)

Može se provjeriti da su oba niza ispravni nizovi polinoma modularnih kvadratnih korijena.

### Kvadratni korijen cijelog broja modulo potencija prostog broja

Algoritam Newtonove iteracije može se prenijeti i na slučaj cijelih brojeva modulo potencija prostog broja.
Pretpostavimo da je $h$ „zgodan” cijeli broj koji nije djeljiv s 3. („Zgodan” znači „sigurno ima rješenje”; točan uvjet navodimo kasnije.) Pretpostavimo da želimo izračunati kvadratni korijen $f$ od $h$ modulo $3^n$. Imamo jednadžbu:

$$
G\left(f\right) = f^2-h \equiv 0\pmod{3^{n}}
$$

Taylorovim razvojem $G$ dobivamo:

$$
G(f) = \sum_{i=0}^{+\infty}\frac{G^{\left(i\right)}\left(f_{0}\right)}{i!}\left(f-f_{0}\right)^{i}
= G(f_0) + 2f_0(f-f_0) + (f-f_0)^2
$$

Računamo udvostručavanjem. Pretpostavimo da su međurezultati dobiveni udvostručavanjem $f_0, f_1, \ldots, f_j$, ili, strogo rečeno, da je $f_j$ cijeli broj koji zadovoljava $G(f_j)\equiv 0\pmod{3^{2^j}}$ te, radi jedinstvenosti, istodobno zadovoljava sljedeća dva uvjeta:

-   $0 < f_{j} < 3^{2^j}$;
-   $f_{j+k}-f_j\equiv 0\pmod{3^{2^j}}$ za sve $k$.

Uvrštavanjem $f_{j+1}$ i $f_j$ u gornji izraz dobivamo:

$$
G(f_{j+1}) = G(f_j) + 2f_j(f_{j+1}-f_j) + (f_{j+1}-f_{j})^2  \equiv 0 \pmod{3^{2^{j+1}}}
$$

Očito $f_{j+1}-f_j$ mora biti višekratnik od $3^{2^j}$. Tako dobivamo

$$
f_{j+1} \equiv f_j - \frac{f_j^2-h}{2f_j} \equiv \frac{f_j^2 + h}{2f_j} \pmod{3^{2^{j+1}}}
$$

Ako $f_j$ postoji, tada $2f_j$ nije djeljiv s $3$, pa nužno ima inverz modulo $3^{2^{j+1}}$. Stoga niz $f_0,f_1\ldots,f_j$ postoji ako i samo ako postoji $f_0$. Kvadratni korijen cijelog broja $h$ koji nije djeljiv s 3 modulo $3$ ili ne postoji ili ih ima dva. Dakle, jedini uvjet da cijeli algoritam radi jest da $h$ ima kvadratni korijen modulo $3$.

Ovdje za konkretan primjer računanja uzimamo $h=46$.

-   $f_0=1$,$f_1=\dfrac{1^2+46}{2\times 1}\mod 9 = 1$,$f_2=\dfrac{1^2+46}{2\times 1}\mod 81 = 64$,$f_3=\dfrac{64^2+46}{2\times 64}\mod 6561 = 955$,$\ldots$
-   $f_0=2$,$f_1=\dfrac{2^2+46}{2\times 2}\mod 9 = 8$,$f_2=\dfrac{8^2+46}{2\times 8}\mod 81 = 17$,$f_3=\dfrac{17^2+46}{2\times 17}\mod 6561 = 5606$,$\ldots$ (jednako prethodnom s promijenjenim predznakom)

Može se provjeriti da su oba niza ispravni nizovi modularnih kvadratnih korijena.

## Algebarski dokaz

Ovaj odjeljak proširuje prethodni tekst: jezikom apstraktne algebre dokazujemo da, čim $f$ zadovoljava uvjet početnog rješenja, Newtonova metoda daje rješenje za svaki $n$ i da se njome mogu dobiti sva rješenja.

### Dokaz postojanja rješenja

???+ note "Lema 1"
    Neka [integralna domena](../algebra/ring-theory.md#整环) $R$ ima polinom ili [formalni red potencija](../algebra/ring-theory.md#形式幂级数环) $f(X) = \sum_{i\geq 0}a_iX^i$ te $r,p\in R$ takve da je $f(r)\in Rp$ (tj. $r$ je korijen od $f(X)$ modulo $p$) i da je $f'(r)\in R$ invertibilan modulo $p$. Ovdje je $f'(X) := \sum_{i\geq 0}(i+1)a_{i+1}X^i$ **formalna derivacija** od $f(X)$. Tada je $f\left(r-\dfrac{f(r)}{f'(r)}\right) \equiv 0\pmod {p^2}$.

??? note "Dokaz"
    Za svaki $s\in R$,
    
    $$
    \begin{aligned}
    f(r+sp) &= \sum_{i\geq 0}a_i(r+sp)^i \\
    &= \sum_{i\geq 0}a_ir^i + sp\sum_{i\geq 1}ia_ir^{i-1} + s^2p^2\left(\ldots\right) \\
    &= f(r) + spf'(r) + s^2p^2\left(\frac{f''(r)}{2!} + \cdots\right),
    \end{aligned}
    $$
    
    pa je
    
    $$
    f(r+sp) \in Rp^2 \iff f(r)+f'(r)sp \in Rp^2
    $$
    
    Budući da je $f(r)\in Rp$ i da je $f'(r)$ invertibilan, dovoljno je uzeti $sp = -\dfrac{f(r)}{f'(r)}$, gdje je $\dfrac{1}{f'(r)}$ inverz modulo $p^2$. Kako je $f'(r)$ invertibilan modulo $p$, nužno ima inverz i modulo $p^2$: neka su $a,b,c\in R$ takvi da je $af'(r) = bp+1$ i $f(r)=cp$; tada je $\left(a^2f'(r)-2\right)f'(r) = b^2p^2+1$, pa možemo uzeti $s=c(2-a^2f'(r))$.

Za prsten polinoma $k[X]$ nad poljem $k$, neka su $G(X, Y)\in k[X, Y]$ i $f_n\in k[X]$ takvi da je $G(X, f_n(X))\in k[X]X^n$; primjenom leme 1 dobivamo

$$
G\left(X, f_n(X) - \frac{G(X, f_n(X))}{\frac{\partial G}{\partial Y}(X, f_n(X))} \right)\equiv 0 \pmod {X^{2n}}
$$

Za početni uvjet udvostručavanja dovoljno je da postoji $f_1\in k$ takav da je $G(X, f_1)\equiv 0\pmod X$ i $\dfrac{\partial G}{\partial Y}(X, f_1)\not\equiv 0\pmod X$. Potonji uvjet osigurava da $\dfrac{\partial G}{\partial Y}$ ima nenul slobodni član, a budući da $X\left| \dfrac{G(X, f_n(X))}{\frac{\partial G}{\partial Y}(X, f_n(X))} \right.$, za svaki $n$ je $\dfrac{\partial G}{\partial Y}(X, f_n)$ uvijek invertibilan modulo $X^n$, čime je ispunjen i uvjet za sljedeću iteraciju.

### Dokaz da se dobivaju sva rješenja

???+ note "Lema 2"
    Neka je $R$ [UFD](../algebra/ring-theory.md#唯一分解整环), a $f,r,p$ definirani kao u lemi 1. Tada je $r-\dfrac{f(r)}{f'(r)}$ iz leme 1 jedinstvena vrijednost $x$ modulo $p^{2}$ koja zadovoljava sljedeća dva uvjeta:
    
    -   $f(x)\in Rp^{2}$
    -   $x-r\in Rp$
    
    tj.
    
    $$
    \forall x\in R,\qquad p^2\mid f(x)\wedge p\mid (x-r) \implies x\equiv r-\dfrac{f(r)}{f'(r)} \pmod {p^2}
    $$

??? note "Dokaz"
    Stavimo $s = -\dfrac{f(r)}{f'(r)p}$ i $u = r+sp$; lema 1 jamči da $u$ zadovoljava oba uvjeta i da je $f(r) + f'(r)sp \in Rp^{2}$.
    Neka je $v$ vrijednost koja zadovoljava gornje uvjete; tada je $v = r+tp$ i $f(r) + f'(r)tp \in Rp^{2}$.
    Odatle je $f'(r)(t-s)p\in Rp^{2}$ i $v-u\in Rp^{2}$.

Newtonova metoda jamči da se dobivaju sva rješenja modulo $X^{2^n}$. Pretpostavimo da je $G(X, h)\equiv 0\pmod {X^{2^n}}$; stavimo $h_{2^i} := h\pmod {X^{2^i}}$, zatim uzmimo $f_1 = h_1$ i primijenimo Newtonovu metodu; prema lemi 2 dobivamo $f_{2^i} \equiv h_{2^i}\pmod {X^{2^i}}$, pa je nužno $f_{2^n} = h$.

Gornje razmatranje pokazuje i da je, kad je $\dfrac{\partial G}{\partial y}(0, y)$ uvijek invertibilan, broj rješenja jednadžbe $G(X, f)\equiv 0\pmod {X^n}$ jednak broju rješenja jednadžbe $G(0, f)\equiv 0\pmod X$. Taj zaključak nije trivijalan. Pogledajmo sljedeći primjer.

??? example "Primjer u kojem Newtonova metoda ne vrijedi, a broj rješenja raste sa stupnjem"
    Modulo $X$ jedini kvadratni korijen od $X^2$ je $0$, ali modulo $X^4$ kvadratni korijeni od $X^2$ su $X, -X, X^3+X, \ldots$
