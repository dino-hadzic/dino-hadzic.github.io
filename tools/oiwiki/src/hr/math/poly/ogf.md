---
title: Obična funkcija izvodnica
---

Obična funkcija izvodnica (ordinary generating function, OGF) niza $a$ definira se kao formalni red potencija:

$$
F(x)=\sum_{n}a_n x^n
$$

Niz $a$ može biti konačan ili beskonačan. Česti primjeri (pretpostavljamo da $a$ počinje indeksom $0$):

1.  Obična funkcija izvodnica niza $a=\langle 1,2,3\rangle$ je $1+2x+3x^2$.
2.  Obična funkcija izvodnica niza $a=\langle 1,1,1,\cdots\rangle$ je $\sum_{n\ge 0}x^n$.
3.  Funkcija izvodnica niza $a=\langle 1,2,4,8,16,\cdots\rangle$ je $\sum_{n\ge 0}2^nx^n$.
4.  Funkcija izvodnica niza $a=\langle 1,3,5,7,9,\cdots\rangle$ je $\sum_{n\ge 0}(2n+1)x^n$.

Drugim riječima, ako niz $a$ ima formulu za opći član, koeficijenti njegove obične funkcije izvodnice upravo su ta formula.

## Osnovne operacije

Promotrimo dva niza $a,b$ s običnim funkcijama izvodnicama $F(x),G(x)$. Tada je

$$
F(x)\pm G(x)=\sum_n (a_n\pm b_n)x^n
$$

pa je $F(x)\pm G(x)$ obična funkcija izvodnica niza $\langle a_n\pm b_n\rangle$.

Promotrimo množenje, odnosno konvoluciju:

$$
F(x)G(x)=\sum_n x^n \sum_{i=0}^na_ib_{n-i}
$$

pa je $F(x)G(x)$ obična funkcija izvodnica niza $\langle \sum_{i=0}^n a_ib_{n-i} \rangle$.

## Zatvoreni oblik

Pri radu s funkcijama izvodnicama ne koristimo stalno oblik formalnog reda potencija, nego ga u pogodnom trenutku pretvaramo u zatvoreni oblik radi lakšeg pojednostavljivanja.

Na primjer, za običnu funkciju izvodnicu $F(x)=\sum_{n\ge 0}x^n$ niza $\langle 1,1,1,\cdots\rangle$ primjećujemo da vrijedi

$$
F(x)x+1=F(x)
$$

Rješavanjem te jednadžbe dobivamo

$$
F(x)=\frac{1}{1-x}
$$

To je zatvoreni oblik od $\sum_{n\ge 0}x^n$.

Promotrimo funkciju izvodnicu $F(x)=\sum_{n\ge 0}p^nx^n$ geometrijskog niza $\langle 1,p,p^2,p^3,p^4,\cdots\rangle$; vrijedi

$$
\begin{aligned}F(x)px+1 &=F(x)\\F(x) &=\frac{1}{1-px}\end{aligned}
$$

Prijelaz između zatvorenog i razvijenog oblika geometrijskog niza često je korišten alat.

???+ note "Mala vježba"
    Odredite obične funkcije izvodnice (u obliku formalnog reda potencija i u zatvorenom obliku) sljedećih nizova. Težina postupno raste.
    
    1.  $a=\langle 0,1,1,1,1,\cdots\rangle$.
    2.  $a=\langle 1,0,1,0,1,\cdots \rangle$.
    3.  $a=\langle 1,2,3,4,\cdots \rangle$.
    4.  $a_n=\binom{m}{n}$ ($m$ je konstanta, $n\ge 0$).
    5.  $a_n=\binom{m+n}{n}$ ($m$ je konstanta, $n\ge 0$).

??? note "Rješenja"
    Prvi:
    
    $$
    F(x)=\sum_{n\ge 1}x^n=\dfrac{x}{1-x}
    $$
    
    Drugi:
    
    $$
    \begin{aligned}
    F(x)&=\sum_{n\ge 0}x^{2n}\\
    &=\sum_{n\ge 0}(x^2)^{n}\\
    &=\frac{1}{1-x^2}
    \end{aligned}
    $$
    
    Treći (deriviranje):
    
    $$
    \begin{aligned}F(x)&=\sum_{n\ge 0}(n+1)x^n\\&=\sum_{n\ge 1}nx^{n-1}\\&=\sum_{n\ge 0}(x^n)'\\&=\left(\frac{1}{1-x}\right)'\\&=\frac{1}{(1-x)^2}\end{aligned}
    $$
    
    Četvrti (binomni teorem):
    
    $$
    F(x)=\sum_{n\ge 0}\binom{m}{n}x^n=(1+x)^m
    $$
    
    Peti:
    
    $$
    F(x)=\sum_{n\ge 0}\binom{m+n}{n}x^n=\frac{1}{(1-x)^{m+1}}
    $$
    
    Može se dokazati indukcijom.
    
    Najprije, za $m=0$ vrijedi $F(x)=\dfrac{1}{1-x}$.
    
    A za $m>0$ vrijedi
    
    $$
    \begin{aligned}
    \frac{1}{(1-x)^{m+1}}
    &=\frac{1}{(1-x)^m}\frac{1}{1-x}\\
    &=\left(\sum_{n\ge 0}\binom{m+n-1}{n}x^n \right)\left(\sum_{n\ge 0}x^n \right)\\
    &=\sum_{n\ge 0} x^n\sum_{i=0}^n \binom{m+i-1}{i}\\
    &=\sum_{n\ge 0}\binom{m+n}{n}x^n
    \end{aligned}
    $$

## Funkcija izvodnica Fibonaccijeva niza

Izvedimo sada funkciju izvodnicu Fibonaccijeva niza.

Fibonaccijev niz definiran je s $a_0=0,a_1=1,a_n=a_{n-1}+a_{n-2}\;(n>1)$. Neka je njegova obična funkcija izvodnica $F(x)$; tada prema rekurziji možemo na sličan način postaviti jednadžbu za $F(x)$:

$$
F(x)=xF(x)+x^2F(x)-a_0x+a_1x+a_0
$$

Rješavanjem dobivamo

$$
F(x)=\frac{x}{1-x-x^2}
$$

Sljedeće je pitanje: kako odrediti njezin razvijeni oblik?

### Prvi način razvoja

Promatrajmo $x+x^2$ kao cjelinu; tada dobivamo

$$
\begin{aligned}
F(x) &= \dfrac{x}{1-(x+x^2)} \\
&= x\sum_{k=0}^{\infty}(x+x^2)^k \\
&= x\sum_{k=0}^{\infty}\sum_{i=0}^k\binom{k}{i}x^{k-i}(x^2)^i \\
&= \sum_{k=0}^{\infty}\sum_{i=0}^k\binom{k}{i}x^{k+i+1} \\
&= \sum_{n=1}^{\infty}\sum_{i=0}^{\lfloor(n-1)/2\rfloor}\binom{n-i-1}{i}x^n.
\end{aligned}
$$

U posljednjem koraku stavili smo $n=k+i+1$ i zamijenili redoslijed sumiranja. Odatle dobivamo formulu za opći član:

$$
a_n = \sum_{i=0}^{\lfloor(n-1)/2\rfloor}\binom{n-i-1}{i}.
$$

To nije dobro poznati oblik sa zlatnim rezom.

### Drugi način razvoja

Rješavamo jednadžbu s neodređenim koeficijentima:

$$
\frac{A}{1-ax}+\frac{B}{1-bx}= \frac{x}{1-x-x^2}
$$

Svođenjem na zajednički nazivnik dobivamo

$$
\frac{A-Abx+B-aBx}{(1-ax)(1-bx)} = \frac{x}{1-x-x^2}
$$

Izjednačavanjem koeficijenata dobivamo

$$
\begin{cases}
A+B=0\\
-Ab-aB=1\\
a+b=1\\
ab=-1
\end{cases}
$$

Rješenje je

$$
\begin{cases}
A=\frac{1}{\sqrt{5}}\\
B=-\frac{1}{\sqrt{5}}\\
a=\frac{1+\sqrt{5}}{2}\\
b=\frac{1-\sqrt{5}}{2}
\end{cases}
$$

Tada prema razvoju geometrijskog niza dobivamo formulu za opći član Fibonaccijeva niza:

$$
\frac{x}{1-x-x^2}=\sum_{n\ge 0}x^n
\frac{1}{\sqrt{5}}\left( \left(\frac{1+\sqrt{5}}{2}\right)^n-\left(\frac{1-\sqrt{5}}{2}\right)^n \right)
$$

To se također naziva drugim zatvorenim oblikom Fibonaccijeva niza ($\frac{x}{1-x-x^2}$ je jedan zatvoreni oblik).

Za proizvoljne polinome $P(x),Q(x)$ razvoj funkcije izvodnice $\dfrac{P(x)}{Q(x)}$ može se dobiti gornjom metodom. U praksi obično najprije nađemo korijene od $Q(x)$, nazivnik zapišemo u obliku $\prod (1-p_ix)^{d_i}$, a zatim odredimo brojnike.

Kada pri faktorizaciji nazivnika postoje višestruki korijeni, za svaku višestrukost treba dodati još jedan razlomak. Na primjer, promotrimo formulu za opći član koeficijenata funkcije izvodnice

$$
G(x)=\frac{1}{(1-x)(1-2x)^2}
$$

Tada je

$$
G(x)=\frac{c_0}{1-x}+\frac{c_1}{1-2x}+\frac{c_2}{(1-2x)^2}
$$

Rješenje je

$$
\begin{cases}
c_0&=1\\
c_1&=-2\\
c_2&=2
\end{cases}
$$

pa je

$$
[x^n]G(x)=1-2^{n+1}+(n+1)\cdot 2^{n+1}
$$

## Newtonov binomni teorem

Iznova definiramo binomni koeficijent:

$$
\binom{r}{k}=\frac{r^{\underline{k}}}{k!}\quad(r\in\mathbf{C},k\in\mathbf{N})
$$

Uočite da $r$ pripada polju kompleksnih brojeva. U tom slučaju za $\alpha\in\mathbf{C}$ vrijedi

$$
(1+x)^{\alpha}=\sum_{n\ge 0}\binom{\alpha}{n}x^n
$$

Binomni teorem zapravo je poseban slučaj Newtonova binomnog teorema.

## Funkcija izvodnica Catalanovih brojeva

Vidi [algebarski izvod Catalanovih brojeva](../combinatorics/catalan.md#代数推演).

## Primjene

U nastavku dajemo nekoliko primjera zadataka koji pokazuju konkretne primjene funkcija izvodnica u OI-ju.

### 食物 (Hrana)

???+ note "[食物 (Hrana)](https://hydro.ac/p/bzoj-P3028)"
    Među mnogo različitih vrsta hrane treba odabrati $n$ komada, uz sljedeća ograničenja za pojedine vrste:
    
    1.  hamburger iz Chengdea: paran broj
    2.  kola: 0 ili 1 komad
    3.  pileći batak: 0, 1 ili 2 komada
    4.  sok od breskve: neparan broj
    5.  pileći medaljoni: broj djeljiv s 4
    6.  baozi (punjena peciva): 0, 1, 2 ili 3 komada
    7.  krumpir s mesom: najviše jedan.
    8.  kruh: broj djeljiv s 3
    
    Svaka se vrsta hrane broji „po komadu”; svaki odabir čiji je ukupan broj komada $n$ računa se kao jedan način. Za zadani $n$ izračunajte broj načina modulo $10007$.

Ovo je klasičan zadatak s funkcijama izvodnicama. Za jednu vrstu hrane možemo označiti s $a_n$ broj načina da se odabere $n$ komada te hrane i odrediti njezinu funkciju izvodnicu. Funkcija izvodnica broja načina da se od dviju vrsta hrane ukupno odabere $n$ komada upravo je konvolucija njihovih funkcija izvodnica. I funkcija izvodnica broja načina da se od više vrsta hrane odabere $n$ komada konvolucija je njihovih funkcija izvodnica.

Kad smo shvatili da se broj načina može izraziti konvolucijom, možemo konstruirati funkcije izvodnice (brojevi odgovaraju brojevima vrsta hrane u zadatku):

1.  $\displaystyle\sum_{n\ge 0}x^{2n}=\dfrac{1}{1-x^2}$.
2.  $1+x$.
3.  $1+x+x^2=\dfrac{1-x^3}{1-x}$.
4.  $\dfrac{x}{1-x^2}$.
5.  $\displaystyle \sum_{n\ge 0}x^{4n}=\dfrac{1}{1-x^4}$.
6.  $1+x+x^2+x^3=\dfrac{1-x^4}{1-x}$.
7.  $1+x$.
8.  $\dfrac{1}{1-x^3}$.

Pomnožimo li sve, dobivamo funkciju izvodnicu odgovora:

$$
F(x)=\frac{(1+x)(1-x^3)x(1-x^4)(1+x)}{(1-x^2)(1-x)(1-x^2)(1-x^4)(1-x)(1-x^3)}
=\frac{x}{(1-x)^4}
$$

Zatim je pretvaramo u razvijeni oblik (pomoću petog zadatka iz vježbe o zatvorenom obliku):

$$
F(x)=\sum_{n\ge 1}\binom{n+2}{n-1}x^n
$$

Odgovor je dakle $\dbinom{n+2}{n-1}=\dbinom{n+2}{3}$.

### Sweet

???+ note "[[CEOI2004] Sweet](https://hydro.ac/p/bzoj-P3027)"
    Zadano je $n$ hrpa slatkiša. Slatkiši u različitim hrpama različitih su vrsta (tj. slatkiši u istoj hrpi iste su vrste, a slatkiši u različitim hrpama različitih su vrsta). U $i$-toj hrpi nalazi se $m_i$ slatkiša. Treba pojesti barem $a$, ali najviše $b$ slatkiša. Koliko ima načina?
    
    Dva se načina razlikuju ako i samo ako se razlikuje broj pojedenih slatkiša ili se za neku vrstu slatkiša razlikuje broj pojedenih slatkiša te vrste.
    
    $n\le 10,0\le a\le b\le 10^7,m_i\le 10^6$.

Funkcija izvodnica broja načina da se iz $i$-te hrpe pojede $j$ slatkiša (očito 1) je

$$
F_i(x)=\sum_{j=0}^{m_i}x^j=\frac{1-x^{m_i+1}}{1-x}
$$

pa je funkcija izvodnica broja načina da se ukupno pojede $i$ slatkiša

$$
G(x)=\prod_{i=1}^n F_i(x)=(1-x)^{-n}\prod_{i=1}^n(1-x^{m_i+1})
$$

Tražimo $\sum_{i=a}^b[x^i]G(x)$.

Budući da je $n\le 10$, možemo grubom silom razviti $\prod_{i=1}^n(1-x^{m_i+1})$ (najviše $2^n$ članova).

Zatim na $(1-x)^{-n}$ primijenimo Newtonov binomni teorem:

$$
\begin{aligned}
(1-x)^{-n}
&=\sum_{i\ge 0}\binom{-n}{i}(-x)^i\\
&=\sum_{i\ge 0}\binom{n-1+i}{i}x^i
\end{aligned}
$$

Prolazimo po koeficijentima uz $x^k$ u $\prod_{i=1}^n(1-x^{m_i+1})$; označimo ih s $c_k$. Nakon množenja s $(1-x)^{-n}$ doprinos odgovoru je

$$
c_k\sum_{i=a-k}^{b-k}\binom{n-1+i}{i}=c_k\left(
\binom{n+b-k}{b-k}-
\binom{n+a-k-1}{a-k-1}
\right)
$$

Tako odgovor možemo izračunati u $O(b)$.

Vremenska složenost je $O(2^n+b)$.
