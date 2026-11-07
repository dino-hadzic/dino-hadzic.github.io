---
title: Vjerojatnosne nejednakosti
---

Na algoritamskim natjecanjima ponekad se koriste [randomizirani algoritmi](../../misc/rand-technique.md), čija ispravnost te vremenska i prostorna složenost obično ovise o pretpostavci da je „vjerojatnost nekih slučajnih događaja vrlo mala”. Primjerice, složenost quick sorta ovisi o tome da se događaj „odabrani `pivot` element gotovo je najmanji ili najveći element” rijetko dogodi.

U ovom se članku kratko predstavljaju neki alati za analizu randomiziranih algoritama i daje nekoliko primjera jednostavnih primjena.

## Union Bound

Neka su $A_1, \cdots, A_m$ slučajni događaji. Tada je

$$
P\left\{ \bigcup_{i=1}^m A_i \right\} \leq \sum_{i=1}^m P\{A_i\}
$$

tj. vjerojatnost da se dogodi barem jedan od skupine događaja ne premašuje zbroj vjerojatnosti pojedinih događaja.

Zapravo, ovaj se rezultat može još malo pojačati:

-   Vjerojatnost da se dogodi barem jedan od skupine događaja **nije manja** od zbroja vjerojatnosti pojedinih događaja umanjenog za zbroj vjerojatnosti da se istodobno dogode svaka dva.
-   Vjerojatnost da se dogodi barem jedan od skupine događaja **ne premašuje** zbroj vjerojatnosti pojedinih događaja, umanjen za zbroj vjerojatnosti da se istodobno dogode svaka dva i uvećan za zbroj vjerojatnosti da se istodobno dogode svaka tri.
-   …

Sa sve više razina naizmjenične gornje i donje ograde postaju sve oštrije. Ovaj je niz rezultata po obliku sličan formuli uključivanja-isključivanja, a i dokaz je sličan dokazu formule uključivanja-isključivanja, pa ga ovdje izostavljamo.

## Markovljeva nejednakost

Neka je $X$ slučajna varijabla koja poprima nenegativne vrijednosti. Tada za svaki pozitivan realan broj $a$ vrijedi

$$
P\{ X \geq a \} \leq \frac{EX}{a}
$$

Zapravo, budući da Markovljeva nejednakost sama ne koristi nikakvu informaciju o razdiobi slučajne varijable osim očekivanja, ograda dobivena izravnom primjenom te nejednakosti obično je vrlo labava.

### Dokaz

Neka je $I$ indikatorska funkcija događaja $X \geq a$. Tada je

$$
I \leq \frac{X}{a}
$$

pa slijedi

$$
P\{ X \geq a \} = EI \leq E \left[ \frac{X}{a} \right] = \frac{EX}{a}
$$

## Čebiševljeva nejednakost

Neka je $X$ slučajna varijabla. Tada za svaki $a > 0$ vrijedi

$$
P \{ |X - EX| \geq a \} \leq \frac{DX}{a^2}
$$

Posebno, za $a$ jednako $k\sigma$ vrijedi

$$
P \{ |X - EX| \geq k\sigma \} \leq \frac{1}{k^2}
$$

gdje je $\sigma$ standardna devijacija varijable $X$.

### Dokaz

Iz pretpostavki vrijedi

$$
P \{ |X - EX| \geq a \} = P \{ (X - EX)^2 \geq a^2 \}
$$

Primijetimo da je $(X - EX)^2$ nenegativno, pa iz Markovljeve nejednakosti slijedi

$$
P \{ (X - EX)^2 \geq a^2 \} \leq \frac{E(X - EX)^2}{a^2} = \frac{DX}{a^2}
$$

## Chernoffova nejednakost

Opća Chernoffova nejednakost može se dobiti izravnom primjenom Markovljeve nejednakosti na slučajnu varijablu $\mathrm{e}^{tX}$:

Neka je $X$ slučajna varijabla. Tada za svaki $t > 0$ vrijedi

$$
P\{ X \geq a \} = P\{ \mathrm{e}^{tX} > \mathrm{e}^{ta} \} \leq \frac{E \mathrm{e}^{tX}}{\mathrm{e}^{ta}}
$$

Analogno, za $t < 0$ vrijedi

$$
P\{ X \leq a \} = P\{ \mathrm{e}^{tX} > \mathrm{e}^{ta} \} \leq \frac{E \mathrm{e}^{tX}}{\mathrm{e}^{ta}}
$$

### Chernoffova nejednakost za zbroj Poissonovih pokusa

Slučajne varijable koje se pojavljuju na algoritamskim natjecanjima obično nisu tako „opće”; možemo ih opisati Poissonovim pokusima iz teorije vjerojatnosti.

Poissonov pokus (Poisson trial) slučajni je pokus sa samo dva moguća ishoda.

Ishod jednog Poissonova pokusa može se opisati slučajnom varijablom $X$ koja poprima vrijednost $0$ ili $1$, s razdiobom

$$
P\{ X = i \} = \begin{cases}
    p_i, & i = 1 \\
    1 - p_1, & i = 0
\end{cases}
$$

Za Poissonove pokuse vrijedi sljedeći rezultat:

Za $n$ nezavisnih Poissonovih pokusa $X_1, X_2, \cdots, X_n$ označimo $X = \sum_{i=1}^{n} X_i$ i $\mu = EX$. Tada za svaki $0 < \epsilon < 1$ vrijedi

$$
P\left\{ |X - \mu| \geq \epsilon \mu \right\} \leq 2 \exp\left( - \frac{1}{3} \mu \epsilon^2 \right)
$$

## Hoeffdingova nejednakost

Ako su $X_1, \cdots, X_n$ međusobno nezavisne realne slučajne varijable takve da je $X_i\in [a_i,b_i]$, i označimo slučajnu varijablu $X=\sum\limits_{i=1}^n X_i$, tada

$$
P\{ |X - EX| \geq \epsilon \} \leq 2\exp \left( \frac {-2\epsilon^2}{\sum\limits_{i=1}^n (b_i-a_i)^2} \right)
$$

I Chernoffova i Hoeffdingova nejednakost ograničavaju koliko slučajna varijabla odstupa od svog očekivanja. Dokazi tih dviju nejednakosti prilično su dugi; zainteresirani mogu pogledati odgovarajuća poglavlja knjige Probability and Computing.

Iskustveno, ako $EX$ nije previše blizu $a_1+\cdots+a_n$, ograda koju daje ova nejednakost obično je relativno oštra; ako je pak vrlo blizu (primjerice u [UOJ #72 全新做法 (Potpuno novi pristup)](https://matthew99.blog.uoj.ac/blog/5511)), dobivena je ograda obično vrlo labava, pa je tada bolje upotrijebiti Chernoffovu nejednakost.

## Primjeri primjene

### Primjer: procjena broja π nasumičnim bacanjem točaka

Promotrimo sljedeći algoritam za procjenu točne vrijednosti broja $\pi$:

U kvadratu $[-1, 1]^2$ nasumično generiramo $n$ točaka i označimo s $m$ broj točaka koje padnu u jedinični krug $x^2 + y^2 \leq 1$; tada se $\dfrac{4m}{n}$ može uzeti kao približna vrijednost broja $\pi$.

Pitanje: kako odabrati $n$ da bi gornji algoritam s vjerojatnošću barem $(1 - \delta)$ vratio rezultat s relativnom pogreškom najviše $\epsilon$?

??? note "Rješenje"
    Neka $X_i$ označava događaj „nasumično generirana $i$-ta točka leži u jediničnom krugu”; tada je ukupan broj točaka u krugu $X = \sum_{i=1}^{n} X_i$. Trebamo pronaći prikladan $n$ takav da
    
    $$
    P\left\{ \left| \frac{4X}{n} - \pi \right| \geq \epsilon \pi \right\} \leq \delta
    $$
    
    Gornji je izraz ekvivalentan s
    
    $$
    P\left\{ \left| X - \frac{\pi}{4}n \right| \geq \epsilon \cdot \frac{\pi}{4}n  \right\} \leq \delta
    $$
    
    Prema Chernoffovoj nejednakosti dovoljno je zahtijevati
    
    $$
    2 \exp\left( - \frac{1}{3} \epsilon^2 \cdot \frac{\pi}{4}n \right) \leq \delta
    $$
    
    odakle se dobiva
    
    $$
    n \geq \frac{12}{\pi} \epsilon^{-2} \ln \frac{2}{\delta}
    $$
    
    tj. za $n = \Omega(\epsilon^{-2} \ln \frac{1}{\delta})$ postiže se tražena točnost.

### Primjer: problem nagradne igre

U kutiji je $n$ kuglica, od kojih točno $k$ odgovara glavnim nagradama. Izvodite niz nezavisnih, jednako vjerojatnih nasumičnih izvlačenja, a nakon svakog izvlačenja kuglicu vraćate u kutiju. Koliko puta treba izvlačiti da bi s vjerojatnošću barem $(1 - \epsilon)$ **svaka** nagradna kuglica bila izvučena barem jednom?

??? note "Rješenje"
    Kad bi postojala samo jedna nagradna kuglica, dovoljno bi bilo $M=n\log\epsilon^{-1}$ izvlačenja, jer je vjerojatnost da je u svih $M$ izvlačenja promašimo
    
    $$
    \Big(1-\dfrac 1n\Big)^{n\log\epsilon^{-1}}\leq e^{\log\epsilon}=\epsilon
    $$
    
    Sad imamo $k>1$ nagradnih kuglica, pa je prema Union Boundu dovoljno osigurati da vjerojatnost propuštanja svake pojedine nagradne kuglice ne premašuje $\dfrac \epsilon k$. Odgovor je stoga $n \log \dfrac{k}{\epsilon}$.

### Primjer: nasumičan odabir polovice elemenata

Zadajte algoritam koji iz $n$ elemenata jednako vjerojatno nasumično bira podskup veličine $\dfrac{n}{2}$; zajamčeno je da je $n$ paran. Jedini izvor slučajnosti koji smijete koristiti je pošten novčić, a broj bacanja novčića pokušajte što više smanjiti (ne traži se minimum).

??? note "Rješenje"
    Prvo se može zamisliti ovakav algoritam:
    
    -   Bacanjem novčića $n$ puta možemo jednako vjerojatno nasumično odabrati jedan od svih podskupova.
    -   Postupak ponavljamo dok veličina odabranog podskupa ne bude točno $\dfrac n2$.
        -   Primijetimo da podskupovi veličine $\dfrac n2$ čine barem $\dfrac 1n$ svih podskupova, pa je očekivani broj ponavljanja $\leq n$.
    
    Ovaj algoritam u očekivanju treba $n^2$ bacanja novčića.
    
    Drugi algoritam:
    
    -   Nasumičan odabir 1 od $n$ možemo ostvariti s očekivano $2\lceil\log_2 n\rceil$ bacanja novčića.
        -   Konkretno: nasumično generiramo binarni broj s $\lceil\log_2 n\rceil$ znamenki; ako je veći ili jednak $n$, ponavljamo, a inače biramo element s odgovarajućim indeksom (indeksi počinju od 0) i završavamo.
    -   Zatim iz svih elemenata biramo jedan, pa iz preostalih još jedan, i tako dalje, dok ne odaberemo $\dfrac n2$ elemenata.
    
    Ovaj algoritam u očekivanju treba $n\lceil\log_2 n\rceil$ bacanja novčića.
    
    Spojimo oba algoritma:
    
    -   Prvo prvim algoritmom nasumično dobijemo jedan podskup.
    -   Ako je veličina tog podskupa manja od $\dfrac n2$, drugim algoritmom dodajemo elemente dok veličinu ne dopunimo do $\dfrac n2$.
    -   Ako veličina tog podskupa premašuje $\dfrac n2$, drugim algoritmom uklanjamo elemente dok veličinu ne smanjimo na $\dfrac n2$.
    
    Pokušajmo analizirati broj operacija potrebnih u drugom i trećem koraku (tj. broj dodavanja/uklanjanja elemenata):
    
    -   Neka 01-slučajna varijabla $X_i$ označava je li $i$ odabran u početni podskup i neka $X:=X_1+\cdots+X_n$ označava veličinu podskupa; tada je broj operacija u drugom i trećem koraku jednak $\big|X-\mathrm{E}[X]\big|$. Uzmemo li u Hoeffdingovoj nejednakosti $t=c\cdot\sqrt n$ (gdje je $c$ proizvoljna konstanta), dobivamo $\mathrm{Pr}\Big[\big|X-\mathrm{E}[X]\big|\geq t\Big]\leq 2\mathrm{e}^{-c^2}$. Drugim riječima, dopuštajući odstupanje reda $\Theta(\sqrt n)$ možemo dobiti po volji malu konstantnu vjerojatnost neuspjeha.
    
    Time smo pokazali: ovaj algoritam s velikom vjerojatnošću jamči da broj bacanja novčića ne premašuje $n+\Theta(\sqrt n\log n)$.
    
    -   Pri tome $n$ dolazi od bacanja novčića za dobivanje početnog podskupa, a $\Theta(\sqrt n\log n)$ je ukupni trošak $\Theta(\sqrt n)$ dodavanja/uklanjanja elemenata.
    
    ??? note "Računanje očekivane složenosti"
        Analizirajmo još iz drugog kuta i pokušajmo izračunati očekivani broj bacanja novčića ovog algoritma.
        
        Hoeffdingovom nejednakošću odredimo gornju ogradu očekivanog broja operacija u drugom i trećem koraku:
        
        $$
        E|X - EX| = \int_0^\infty P\{ |X - E[X]| \geq t \} \mathrm{d}t \leq 
        2 \int_0^\infty \exp \left(-\frac {t^2}{n}\right) \mathrm{d}t=\sqrt{\pi n}
        $$
        
        Stoga je očekivani broj bacanja novčića potrebnih u drugom i trećem koraku $\sqrt{\pi n}\cdot2\lceil\log_2 n\rceil$.
        
        Ukupno, ovaj algoritam u očekivanju treba $n+2\sqrt{\pi n}\lceil\log_2 n\rceil$ bacanja novčića.

### Vježba: Balls and Bins

$n$ kuglica nezavisno i nasumično bacamo u $n$ kutija. Dokažite: broj kuglica u kutiji s najviše kuglica s vjerojatnošću $1 - \dfrac{1}{n}$ nije manji od $\Omega \left( \dfrac{\log n}{\log \log n} \right)$.
