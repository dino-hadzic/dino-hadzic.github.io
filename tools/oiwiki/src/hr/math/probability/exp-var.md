---
title: Numeričke karakteristike slučajnih varijabli
---

U ovom se članku predstavljaju očekivanje, varijanca i druge numeričke karakteristike slučajnih varijabli.

## Očekivanje

### Definicija

#### Diskretne slučajne varijable

Neka je razdioba diskretne slučajne varijable $X$ dana s $p_i = P\{ X = x_i \}$. Ako suma

$$
\sum x_i p_i
$$

apsolutno konvergira, njezina se vrijednost naziva **očekivanjem** (expected value) varijable $X$ i označava $EX$.

#### Neprekidne slučajne varijable

Neka je funkcija gustoće neprekidne slučajne varijable $X$ jednaka $f(x)$. Ako integral

$$
\int_{\mathbb{R}} xf(x) \text{d} x
$$

apsolutno konvergira, njegova se vrijednost naziva **očekivanjem** varijable $X$ i označava $EX$.

#### Jedinstvena definicija

Neka je funkcija razdiobe slučajne varijable $X$ jednaka $F(x)$. Ako [Stieltjesov integral](https://en.wikipedia.org/wiki/Riemann%E2%80%93Stieltjes_integral)

$$
\int_{\mathbb{R}} x \text{d} F(x)
$$

apsolutno konvergira, njegova se vrijednost naziva **očekivanjem** varijable $X$ i označava $EX$.

??? example "Primjer slučajne varijable bez očekivanja"
    Promotrimo diskretnu slučajnu varijablu $X$ sa sljedećom razdiobom
    
    $$
    P\left\{ X = (-1)^k \frac{2^k}{k} \right\} = \frac{1}{2^k}, \quad k = 1, 2, \cdots
    $$
    
    Iako suma $\sum x_i p_i$ konvergira prema $- \ln 2$, ona ne konvergira apsolutno, pa očekivanje varijable $X$ ne postoji.
    
    Promotrimo zatim neprekidnu slučajnu varijablu $Y$ sa sljedećom funkcijom gustoće
    
    $$
    f(y) = \frac{1}{\pi} \cdot \frac{1}{1 + y^2}, \quad y \in (-\infty, +\infty)
    $$
    
    Lako se provjeri da ni očekivanje varijable $Y$ ne postoji.

### Svojstva očekivanja

#### Linearnost

Ako očekivanja slučajnih varijabli $X, Y$ postoje, tada

-   za bilo koje realne brojeve $a, b$ vrijedi $E(aX + b) = a \cdot EX + b$;
-   $E(X + Y) = EX + EY$.

#### Očekivanje produkta slučajnih varijabli

Ako očekivanja slučajnih varijabli $X$, $Y$ postoje te su $X$, $Y$ međusobno nezavisne, tada vrijedi

$$
E(XY) = EX \cdot EY
$$

Napomena: nezavisnost u gornjem svojstvu **nije** nužan uvjet.

??? example "Protuprimjer"
    Promotrimo slučajne varijable $X$ i $Y$, gdje $X$ ima uniformnu razdiobu na $[-1, 1]$, a $Y = X^2$.

### Pretvaranje očekivanja u vjerojatnost i obratno

Za slučajni događaj $A$ promotrimo njegovu indikatorsku funkciju $I_A$:

$$
I_A(\omega) = \begin{cases}
    1, & \omega \in A \\
    0, & \omega \notin A
\end{cases}
$$

Iz definicije se dobiva njezino očekivanje $EI_A = P(A)$. Ta je pretvorba u praktičnim primjenama vrlo česta.

??? example "Primjer"
    Pretpostavimo da za niz $\{ a_i \}$ duljine $n$ član $a_k$ s vjerojatnošću $p_k$ poprima vrijednost $k$, a s vjerojatnošću $1 - p_k$ vrijednost $0$. Razmotrimo kako izračunati očekivanje od $S = \sum_{i=1}^{n} a_i$.
    
    Ako bismo računali izravno po definiciji, trebalo bi odrediti vjerojatnost svake moguće vrijednosti od $S$; taj je postupak prilično zamoran i ovdje ga nećemo razrađivati.
    
    S druge strane, ako s $I_k$ označimo indikatorsku funkciju slučajnog događaja $a_k = k$, vrijedi
    
    $$
    S = \sum_{k=1}^{n} k \cdot I_k
    $$
    
    pa se lako dobiva
    
    $$
    ES = E \left( \sum_{k=1}^{n} k \cdot I_k \right) = \sum_{k=1}^{n} k \cdot E[I_k] = \sum_{k=1}^{n} k \cdot p_k
    $$

## Uvjetna razdioba i uvjetno očekivanje

Ranije smo proučavali uvjetnu vjerojatnost; analogno se može uvesti i pojam uvjetnog očekivanja.

### Definicija

Za dvije slučajne varijable $X$, $Y$ razdioba (funkcija gustoće) varijable $X$ uz uvjet $Y = y$ naziva se **uvjetnom razdiobom (uvjetnom gustoćom)** i označava se redom

$$
P( X = x_i | Y = y ) \qquad f_{X|Y}(x|y)
$$

Očekivanje varijable $X$ uz taj uvjet naziva se **uvjetnim očekivanjem** (conditional expectation) i označava $E[X|Y=y]$.

### Svojstva uvjetnog očekivanja

Mnoga svojstva uvjetnog očekivanja izvode se iz svojstava uvjetne vjerojatnosti i ovdje ih ne ponavljamo.

Vrijedi spomenuti da je $E[X | Y]$ općenito funkcija slučajne varijable $Y$, i to obično nelinearna. No zapravo vrijedi

$$
E[E[X|Y]] = EX
$$

Gornja se formula naziva **formulom potpunog očekivanja** (law of total expectation).

### Primjena

???+ example "[HDU 5984 Pocky](https://acm.hdu.edu.cn/showproblem.php?pid=5984)"
    Imamo štapić Pocky duljine $L$ koji svaki put nasumično lomimo na dva dijela. Ako duljina desnog dijela nije veća od $d$, stajemo; inače na desnom dijelu ponavljamo gornji postupak. Odredite očekivani broj ponavljanja.

??? note "Rješenje"
    Neka $f(x)$ označava očekivani broj ponavljanja za duljinu $x$. Slučaj $x \leq d$ je trivijalan.
    
    Kad je $x > d$, neka je udaljenost mjesta loma od desnog kraja jednaka $k$; očito je $k \sim U[0, x]$, a očekivani broj ponavljanja tada iznosi
    
    $$
    g(k) = \begin{cases}
        1, & k \leq d \\
        1 + f(k), & k > d
    \end{cases}
    $$
    
    Iz formule potpunog očekivanja slijedi
    
    $$
    f(x) = Eg(k) = 1 + \frac{1}{x} \cdot \int_{d}^{x} f(t) \text{d} t
    $$
    
    Rješavanjem gornje integralne jednadžbe i uvrštavanjem početnog uvjeta dobiva se
    
    $$
    f(x) = 1 + \ln \frac{x}{d}
    $$

## Varijanca

### Definicija

Neka očekivanje $EX$ slučajne varijable $X$ postoji i neka postoji i očekivanje

$$
E(X - EX)^2
$$

Tada se vrijednost gornjeg izraza naziva **varijancom** (variance) slučajne varijable $X$ i označava $DX$ ili $Var(x)$. Aritmetički drugi korijen varijance naziva se **standardnom devijacijom** i označava $\sigma(X) = \sqrt{DX}$.

### Svojstva varijance

Ako varijanca slučajne varijable $X$ postoji, tada

-   za bilo koje konstante $a, b$ vrijedi $D(aX + b) = a^2 \cdot DX$
-   $DX = E(X^2) - (EX)^2$

## Kovarijanca i koeficijent korelacije

Općenito jednakost $D(X + Y) = DX + DY$ ne vrijedi, pa se prirodno nameću dva pitanja:

-   Što je točno razlika između $D(X + Y)$ i $DX + DY$?
-   Kad su $D(X + Y)$ i $DX + DY$ jednaki?

Kao odgovor na prvo pitanje uvodimo kovarijancu.

### Definicija kovarijance

Za slučajne varijable $X, Y$ izraz

$$
E((X - EX)(Y - EY))
$$

naziva se **kovarijancom** (covariance) varijabli $X$ i $Y$ i označava $\operatorname{Cov}(X, Y)$.

### Svojstva kovarijance

Za slučajne varijable $X, Y, Z$ vrijedi

-   $\operatorname{Cov}(X, Y) = \operatorname{Cov}(Y, X)$
-   za bilo koje konstante $a, b$ vrijedi $\operatorname{Cov}(aX + bY, Z) = a \cdot \operatorname{Cov}(X, Z) + b \cdot \operatorname{Cov}(Y, Z)$

Ujedno su kovarijanca i varijanca povezane na sljedeći način:

-   $DX = \operatorname{Cov}(X, X)$
-   $D(X + Y) = DX + 2 \operatorname{Cov}(X, Y) + DY$

??? note "O kovarijanci"
    Možda ste primijetili da se svojstva kovarijance formalno u potpunosti podudaraju sa svojstvima skalarnog produkta vektora.
    
    Iz perspektive funkcionalne analize, za zadani vjerojatnosni prostor sve slučajne varijable na njemu čine linearni prostor, kovarijanca je skalarni produkt na tom prostoru, a standardna devijacija je norma inducirana tim skalarnim produktom.

Što se tiče maloprije postavljenog drugog pitanja, lako se vidi da $D(X + Y) = DX + DY$ vrijedi ako i samo ako je $\operatorname{Cov}(X, Y) = 0$. Intuitivan dovoljan uvjet jest da su $X$ i $Y$ nezavisne, jer tada vrijedi

$$
\operatorname{Cov}(X, Y) = E((X - EX)(Y - EY)) = E(X - EX) E(Y - EY) = 0
$$

No taj uvjet nije nužan. Kako bismo opisali odnos između slučajnih varijabli $X$, $Y$ koje zadovoljavaju $\operatorname{Cov}(X, Y) = 0$, uvodimo koeficijent korelacije.

### Koeficijent korelacije

Za slučajne varijable $X, Y$ izraz

$$
\frac{ \operatorname{Cov}(X, Y)}{ \sigma(X)\sigma(Y) }
$$

naziva se **Pearsonovim koeficijentom korelacije** varijabli $X$ i $Y$ i označava $\rho_{X,Y}$.

Pearsonov koeficijent korelacije opisuje koliko je jaka linearna povezanost dviju slučajnih varijabli. Što je $|\rho_{X,Y}|$ veći, to je linearna povezanost između $X$ i $Y$ jača. Lako se dokaže da je $|\rho_{X,Y}| \leq 1$ te da se $|\rho_{X,Y}| = 1$ može pojaviti samo u sljedeća dva slučaja:

-   kad postoje realan broj $a$ i pozitivan realan broj $b$ takvi da je $P(X = a + bY) = 1$, vrijedi $\rho_{X,Y} = 1$;
-   kad postoje realan broj $a$ i negativan realan broj $b$ takvi da je $P(X = a + bY) = 1$, vrijedi $\rho_{X,Y} = -1$.

Kad je $\rho_{X,Y} = 0$, kažemo da su slučajne varijable $X$ i $Y$ **nekorelirane**; tada između $X$ i $Y$ ne postoji linearna veza.

??? note "„Nekoreliranost” i „nezavisnost”"
    Nekoreliranost dviju slučajnih varijabli znači samo da među njima nema linearne povezanosti, a ne da nema veze drugog oblika.
    
    Stoga je nekoreliranost dviju slučajnih varijabli $X, Y$ **nužan, ali ne i dovoljan** uvjet njihove nezavisnosti.

Za drugo pitanje postavljeno na početku ovog odjeljka dajemo zaključak: nužan i dovoljan uvjet za $\operatorname{Cov}(X, Y) = 0$ jest da jedna od varijabli $X$, $Y$ s vjerojatnošću $1$ poprima konstantnu vrijednost ili da su $X, Y$ nekorelirane.
