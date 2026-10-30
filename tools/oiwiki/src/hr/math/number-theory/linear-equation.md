---
title: Linearne kongruencije
---

U ovom se članku razmatra rješavanje linearnih kongruencija.

## Osnovni pojmovi

Neka su $a,b,n$ cijeli brojevi, a $x$ nepoznanica. Tada se jednadžba oblika

$$
ax\equiv b\pmod n
$$

naziva **linearna kongruencija** (linear congruence equation).

Riješiti linearnu kongruenciju znači naći sva rješenja $x$ u intervalu $[0,n-1]$. Dakako, dodavanjem ili oduzimanjem proizvoljnog višekratnika od $n$ i dalje dobivamo rješenja jednadžbe. Modulo $n$ to su sva rješenja te jednadžbe.

U nastavku članka predstavljamo dva pristupa rješavanju linearnih kongruencija, koji redom koriste inverze i diofantske jednadžbe. U općem slučaju i računanje inverza i rješavanje diofantskih jednadžbi zahtijevaju [prošireni Euklidov algoritam](./gcd.md#prošireni-euklidov-algoritam), pa su ta dva pristupa zapravo jednaka.

## Rješavanje pomoću inverza

Najprije promotrimo slučaj kad su $a$ i $n$ relativno prosti, tj. slučaj $\gcd(a,n)=1$. Tada možemo izračunati [inverz](./inverse.md)  $a^{-1}$ broja $a$ i pomnožiti obje strane jednadžbe s $a^{-1}$, čime dobivamo jedinstveno rješenje jednadžbe:

$$
x \equiv ba^{-1} \pmod n.
$$

Zatim promotrimo slučaj kad $a$ i $n$ nisu relativno prosti, tj. slučaj $\gcd(a,n)=d>1$. Tada izvorna jednadžba ne mora imati rješenje. Na primjer, $2x\equiv 1\pmod 4$ nema rješenja. Stoga treba razmotriti dva slučaja:

-   Kad $d$ ne dijeli $b$, jednadžba nema rješenja. Za svaki $x$ lijeva strana $ax$ višekratnik je od $d$, ali desna strana $b$ nije višekratnik od $d$. Stoga se ne mogu razlikovati za višekratnik od $n$, jer je svaki višekratnik od $n$ ujedno višekratnik od $d$. Dakle, jednadžba nema rješenja.

-   Kad $d$ dijeli $b$, parametre $a,b,n$ jednadžbe možemo podijeliti s $d$ i dobiti novu jednadžbu:

    $$
    a'x \equiv b'\pmod{n'}.
    $$

    Pritom je $\gcd(a',n')=1$, tj. $a'$ i $n'$ relativno su prosti. Taj je slučaj već riješen gore, pa računanjem inverza možemo dobiti najmanje nenegativno cjelobrojno rješenje $x'$ te jednadžbe.

    Očito je $x'$ ujedno rješenje izvorne jednadžbe. No to nije jedino rješenje izvorne jednadžbe. Budući da je skup svih rješenja transformirane jednadžbe

    $$
    \{x' + kn' : k\in\mathbf Z\}.
    $$

    ona od tih rješenja koja padaju u interval $[0,n-1]$ upravo su sva rješenja izvorne jednadžbe u intervalu $[0,n-1]$:

    $$
    x \equiv (x' + kn')\pmod{n},\quad k = 0, 1, \cdots, d-1.
    $$

Sažimajući oba slučaja, **broj rješenja** linearne kongruencije jednak je $d=\gcd(a,n)$ ili $0$.

## Rješavanje pomoću diofantske jednadžbe

Linearna kongruencija ekvivalentna je [linearnoj diofantskoj jednadžbi s dvije nepoznanice](./bezouts.md#slučaj-dviju-varijabli) $x,y$:

$$
ax + ny = b.
$$

Prema razmatranju na navedenoj stranici, jednadžba ima rješenje ako i samo ako $\gcd(a,n)\mid b$, a njezino je opće rješenje

$$
\begin{aligned}
x &= x_0 + t\dfrac{n}{d},\\
y &= y_0 - t\dfrac{a}{d},
\end{aligned}
$$

gdje je $d=\gcd(a,n)$ njihov najveći zajednički djelitelj, a $t$ proizvoljan cijeli broj.

Stoga je opće rješenje linearne kongruencije

$$
x \equiv \left(x_0+t\dfrac{n}{d}\right)\pmod{n},\quad t\in\mathbf Z.
$$

Uzimanjem $x_0$ modulo $n/d$ dobivamo najmanje (nenegativno) cjelobrojno rješenje kongruencije, tj. gore spomenuti $x'$.

## Referentna implementacija

Referentna implementacija u ovom odjeljku daje najmanje nenegativno cjelobrojno rješenje kongruencije. Ako rješenje ne postoji, ispisuje $-1$.

???+ example "Referentna implementacija"
    === "C++"
        ```cpp
        --8<-- "docs/math/code/linear-equation/linear-equation.cpp:core"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/math/code/linear-equation/linear-equation.py:core"
        ```

## Zadaci za vježbu

-   [「NOIP2012」同余方程 (Kongruencija)](https://loj.ac/problem/2605)

**Ova je stranica uglavnom prevedena iz članka [Модульное линейное уравнение первого порядка](http://e-maxx.ru/algo/diofant_1_equation) i njegova engleskog prijevoda [Linear Congruence Equation](https://cp-algorithms.com/algebra/linear_congruence_equation.html). Ruska je inačica objavljena pod licencijom Public Domain + Leave a Link, a engleska pod CC-BY-SA 4.0. Sadržaj je izmijenjen.**
