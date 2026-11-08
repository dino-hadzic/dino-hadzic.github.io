---
title: Slučajne varijable
---

## Srodni pojmovi

### Slučajna varijabla

Zadan je vjerojatnosni prostor $(\Omega, \mathcal{F}, P)$. Ako funkcija $X : \Omega \to \mathbb{R}$ definirana na prostoru elementarnih događaja $\Omega$ zadovoljava: za svaki $t \in \mathbb{R}$ vrijedi

$$
\{ \omega \in \Omega : X(\omega) \le t \} \in \mathcal{F}
$$

onda $X$ nazivamo **slučajnom varijablom**.

### Indikatorska funkcija

Za događaj $A$ na prostoru elementarnih događaja $\Omega$ definiramo slučajnu varijablu

$$
I_A(\omega) = \begin{cases}
    1, & \omega \in A \\
    0, & \omega \notin A
\end{cases}
$$

i $I_A$ nazivamo **indikatorskom funkcijom** događaja $A$.

### Funkcija razdiobe

Za slučajnu varijablu $X$ funkciju

$$
F(x) = P( X \leq x )
$$

nazivamo **funkcijom razdiobe** slučajne varijable $X$. Pišemo $X \sim F(x)$.

Funkcija razdiobe ima sljedeća svojstva:

-   **neprekidnost zdesna**: $F(x) = F(x + 0)$
-   **monotonost**: na $\mathbb{R}$ je monotono rastuća (ne strogo)
-   $F(-\infty) = 0$,$F(+\infty) = 1$

Ujedno se može dokazati da je svaka funkcija koja zadovoljava gornje uvjete funkcija razdiobe neke slučajne varijable. Stoga funkcije razdiobe i slučajne varijable međusobno jednoznačno odgovaraju.

## Klasifikacija slučajnih varijabli

Slučajne varijable dijele se prema tome je li njihov skup vrijednosti (prema definiciji, slučajna varijabla je funkcija) prebrojiv na **diskretne** i **neprekidne**.

### Diskretne slučajne varijable

Neka je $X$ diskretna slučajna varijabla čije su sve moguće vrijednosti $x_1, x_2, \cdots$. Tada $X$ možemo opisati nizom jednakosti oblika $P\{ X = x_i \} = p_i$. To je **tablica razdiobe** (zakon razdiobe) koju smo učili u srednjoškolskim udžbenicima.

### Neprekidne slučajne varijable

Neka je $X$ neprekidna slučajna varijabla. Promatrati $P\{ X = x \}$ često je besmisleno (jer je ta vjerojatnost vrlo vjerojatno $0$).

??? note "Zašto kažemo da je vjerojatnost „vrlo vjerojatno” $0$"
    Promotrimo slučajnu varijablu $X$ koja s vjerojatnošću $\frac{1}{2}$ poprima vrijednost $0$, a s vjerojatnošću $\frac{1}{2}$ ima uniformnu razdiobu na otvorenom intervalu $(0, 1)$. Očito $X$ zadovoljava definiciju neprekidne slučajne varijable.
    
    Za svaki realni broj $r \in (0, 1)$ lako se dobiva $P\{ X = r \} = 0$, ali istodobno je $P\{ X = 0 \} = \frac{1}{2}$.

S druge strane, neka je $X \sim F(x)$; tada je

$$
P( l < x \leq l + \Delta x ) = F(l + \Delta x) - F(l)
$$

Prirodna je zamisao limesom $\lim\limits_{\Delta x \to 0^+} \frac{F(l + \Delta x) - F(l)}{\Delta x}$ opisati mogućnost da $X$ poprimi vrijednost $l$.

Taj je izraz dobro poznata derivacija, pa se problem svodi na traženje nenegativne funkcije $f(x)$ takve da je

$$
F(x) = \int_{-\infty}^{x} f(x) \text{d} x
$$

Ako takva $f(x)$ postoji, nazivamo je **funkcijom gustoće** slučajne varijable $X$.

## Nezavisnost slučajnih varijabli

Prije smo raspravljali o nezavisnosti slučajnih događaja. Budući da su slučajne varijable i slučajni događaji usko povezani, možemo analogno dati i definiciju nezavisnosti slučajnih varijabli.

### Definicija

Ako slučajne varijable $X, Y$ zadovoljavaju da za sve $x, y \in \mathbb{R}$ vrijedi

$$
P( X \leq x, Y \leq y ) = P( X \leq x ) P( Y \leq y )
$$

kažemo da su slučajne varijable $X, Y$ **nezavisne**.

??? note "Napomena"
    Neki su učenici možda primijetili da se u srednjoškolskim udžbenicima nezavisnost slučajnih varijabli definira pomoću vjerojatnosti oblika $P(X = \alpha)$, ali budući da je vjerojatnost da neprekidna slučajna varijabla poprimi određenu vrijednost obično $0$, u općenitijem je slučaju pametniji izbor definicija pomoću funkcije razdiobe.

### Svojstva

Ako su slučajne varijable $X$,$Y$ međusobno nezavisne, onda su za bilo koje funkcije $f, g$ slučajne varijable $f(X)$ i $g(Y)$ međusobno nezavisne.

??? warning "Upozorenje"
    Katkad proučavamo razdiobu neke funkcije $f(X, Y)$ (npr. $XY^2$) međusobno nezavisnih slučajnih varijabli $X$,$Y$.
    
    Iako su $X$ i $Y$ nezavisne, ne smije se olako pretpostaviti da za neku vrijednost $y$ varijable $Y$ varijable $f(X, y)$ i $f(X, Y)$ imaju istu razdiobu.
