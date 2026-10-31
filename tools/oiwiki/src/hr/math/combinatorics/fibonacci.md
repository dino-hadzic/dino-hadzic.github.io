---
title: Fibonaccijev niz
---

Fibonaccijev niz (The Fibonacci sequence, [OEIS A000045](http://oeis.org/A000045)) definiran je ovako:

$$
F_0 = 0, F_1 = 1, F_n = F_{n-1} + F_{n-2}
$$

Prvih nekoliko članova niza:

$$
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, \dots
$$

## Lucasov niz

Lucasov niz (The Lucas sequence, [OEIS A000032](http://oeis.org/A000032)) definiran je ovako:

$$
L_0 = 2, L_1 = 1, L_n = L_{n-1} + L_{n-2}
$$

Prvih nekoliko članova niza:

$$
2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, \dots
$$

Pri proučavanju Fibonaccijeva niza često je kao alat potreban Lucasov niz.

## Formula za opći član Fibonaccijeva niza

$n$-ti Fibonaccijev broj može se rekurzivnom formulom izračunati u vremenu $\Theta (n)$. No postoje i brži načini računanja.

### Analitičko rješenje

Analitičko rješenje je rješenje u obliku formule. Za Fibonaccijev niz imamo formulu za opći član (Binetova formula, Binet's Formula):

$$
F_n = \frac{\left(\frac{1 + \sqrt{5}}{2}\right)^n - \left(\frac{1 - \sqrt{5}}{2}\right)^n}{\sqrt{5}}
$$

Ova se formula lako dokazuje indukcijom, a naravno može se izvesti i pomoću pojma funkcije izvodnice ili rješavanjem jedne jednadžbe.

Možda ste primijetili da je drugi član u brojniku ove formule uvijek manji od $1$ i da eksponencijalno brzo opada. Stoga formulu možemo zapisati kao

$$
F_n = \left[\frac{\left(\frac{1 + \sqrt{5}}{2}\right)^n}{\sqrt{5}}\right]
$$

gdje uglate zagrade označavaju zaokruživanje na najbliži cijeli broj.

Ove dvije formule pri računanju zahtijevaju iznimno visoku preciznost, pa se u praksi rijetko koriste. No nemojte ih zanemariti! U kombinaciji s pojmovima kvadratnog ostatka i inverza po modulu, ova formula i dalje može biti korisna u natjecateljskom programiranju (OI).

### Formula za opći član Lucasova niza

Za Lucasov niz imamo formulu za opći član:

$$
L_n = \left(\frac{1 + \sqrt{5}}{2}\right)^n + \left(\frac{1 - \sqrt{5}}{2}\right)^n
$$

Vrlo je slična onoj za Fibonaccijev niz. Zapravo vrijedi:

$$
\frac{L_n + F_n\sqrt{5}}{2} = \left(\frac{1 + \sqrt{5}}{2}\right)^n
$$

Drugim riječima, $L_n$ i $F_n$ upravo su koeficijenti u brojniku koji se dobiju kad se $\left(\frac{1 + \sqrt{5}}{2}\right)^n$ razvije binomnim teoremom i saberu slični članovi. To znači da sva rješenja Pellove jednadžbe

$$
x^2-5y^2=-4
$$

čine upravo

$$
\frac{x_n + y_n\sqrt{5}}{2} = \frac{L_n + F_n\sqrt{5}}{2}
$$

tj. upravo Lucasov i Fibonaccijev niz. Stoga vrijedi

$$
{L_n}^2-5{F_n}^2=-4
$$

### Matrični oblik

Rekurzija Fibonaccijeva niza može se izraziti u obliku množenja matrica:

$$
\begin{bmatrix}F_{n-1} & F_{n} \cr\end{bmatrix} = \begin{bmatrix}F_{n-2} & F_{n-1} \cr\end{bmatrix} \begin{bmatrix}0 & 1 \cr 1 & 1 \cr\end{bmatrix}
$$

Označimo $P = \begin{bmatrix}0 & 1 \cr 1 & 1 \cr\end{bmatrix}$; dobivamo

$$
\begin{bmatrix}F_n & F_{n+1} \cr\end{bmatrix} = \begin{bmatrix}F_0 & F_1 \cr\end{bmatrix} P^n
$$

Tako množenjem matrica možemo izračunati Fibonaccijev niz u vremenu $\Theta(\log n)$. Osim toga, formula iz prethodnog odjeljka može se dobiti i tehnikom dijagonalizacije matrice.

### Metoda brzog udvostručavanja

Gornjom metodom možemo dobiti sljedeće jednakosti:

$$
\begin{aligned}
F_{2k} &= F_k (2 F_{k+1} - F_{k}) \\
F_{2k+1} &= F_{k+1}^2 + F_{k}^2
\end{aligned}
$$

Na taj način brzo računamo dva susjedna Fibonaccijeva broja (s manjom konstantom nego množenjem matrica). Kôd slijedi; povratna je vrijednost uređeni par $(F_n,F_{n+1})$.

```cpp
pair<int, int> fib(int n) {
  if (n == 0) return {0, 1};
  auto p = fib(n >> 1);
  int c = p.first * (2 * p.second - p.first);
  int d = p.first * p.first + p.second * p.second;
  if (n & 1)
    return {d, c + d};
  else
    return {c, d};
}
```

## Svojstva

Fibonaccijev niz ima mnogo zanimljivih svojstava; ovdje navodimo neka od jednostavnijih:

1.  Cassinijev identitet (Cassini's identity): $F_{n-1} F_{n+1} - F_n^2 = (-1)^n$.
2.  Adicijsko svojstvo: $F_{n+k} = F_k F_{n+1} + F_{k-1} F_n$.
3.  Uvrstimo li $k = n$ u prethodno svojstvo, dobivamo $F_{2n} = F_n (F_{n+1} + F_{n-1})$.
4.  Iz prethodnog se svojstva indukcijom može dokazati $\forall k\in \mathbb{N},F_n|F_{nk}$.
5.  Vrijedi i obrat: $\forall F_a|F_b,a|b$.
6.  Svojstvo najvećeg zajedničkog djelitelja (GCD): $(F_m, F_n) = F_{(m, n)}$.
7.  Dva susjedna člana Fibonaccijeva niza kao ulaz za Euklidov algoritam daju njegovu najgoru složenost (vidi [Wikipedia – Lamé](https://en.wikipedia.org/wiki/Gabriel_Lam%C3%A9)).

### Veza Fibonaccijeva i Lucasova niza

Lako je uočiti da su jednakosti koje povezuju Lucasov i Fibonaccijev niz vrlo slične formulama za trigonometrijske funkcije. Primjerice:

$$
\frac{L_n + F_n\sqrt{5}}{2} = \left(\frac{1 + \sqrt{5}}{2}\right)^n
$$

vrlo je slično s

$$
\cos nx + i\sin nx = \left(\cos x + i\sin x\right)^n
$$

Isto tako

$$
{L_n}^2-5{F_n}^2=-4
$$

vrlo je slično s

$$
\cos^2 x + \sin^2 x = 1
$$

Stoga Lucasov niz nalikuje kosinusu, a Fibonaccijev niz sinusu. Primjerice, iz

$$
\left(\frac{1 + \sqrt{5}}{2}\right)^m\left(\frac{1 + \sqrt{5}}{2}\right)^n = \left(\frac{1 + \sqrt{5}}{2}\right)^{m+n}
$$

dobivamo jednakosti za zbroj indeksa:

$$
2L_{m+n}=5F_mF_n+L_mL_n
$$

$$
2F_{m+n}=F_mL_n+L_mF_n
$$

a kao posljedicu i jednakosti za dvostruki indeks:

$$
L_{2n}={L_n}^2-2{\left(-1\right)}^n
$$

$$
F_{2n}=F_nL_n
$$

I to je jedan način brzog udvostručavanja indeksa. Jednako tako, po uzoru na trigonometrijske formule (parnost, pretvaranje zbroja u umnožak i umnoška u zbroj, formule polovičnog kuta, univerzalna supstitucija itd.) mogu se izvesti i mnoge druge odgovarajuće jednakosti za Lucasov i Fibonaccijev niz.

## Fibonaccijevo kodiranje

Fibonaccijev niz možemo iskoristiti za kodiranje pozitivnih cijelih brojeva. Prema [Zeckendorfovu teoremu](https://en.wikipedia.org/wiki/Zeckendorf%27s_theorem), svaki se prirodni broj $n$ može na jedinstven način prikazati kao zbroj nekih Fibonaccijevih brojeva:

$$
N = F_{k_1} + F_{k_2} + \ldots + F_{k_r}
$$

pri čemu je $k_1 \ge k_2 + 2,\ k_2 \ge k_3 + 2,\  \ldots,\  k_r \ge 2$ (tj. ne smiju se upotrijebiti dva susjedna Fibonaccijeva broja).

Stoga pozitivni cijeli broj možemo prikazati kodom $d_0 d_1 d_2 \dots d_s 1$, gdje $d_i=1$ znači da je upotrijebljen $F_{i+2}$. Na kraj koda obvezno dodajemo još jednu jedinicu (čime nastaju dvije susjedne jedinice), što označava kraj koda. Nekoliko primjera:

$$
\begin{aligned}
1 &=& 1 &=& F_2 &=& (11)_F \\
2 &=& 2 &=& F_3 &=& (011)_F \\
6 &=& 5 + 1 &=& F_5 + F_2 &=& (10011)_F \\
8 &=& 8 &=& F_6 &=& (000011)_F \\
9 &=& 8 + 1 &=& F_6 + F_2 &=& (100011)_F \\
19 &=& 13 + 5 + 1 &=& F_7 + F_5 + F_2 &=& (1001011)_F
\end{aligned}
$$

Kodiranje broja $n$ može se obaviti pohlepnim algoritmom (greedy):

1.  Prolazimo Fibonaccijeve brojeve $F_i$ od većih prema manjima dok ne nađemo $F_i\le n$.
2.  Od $n$ oduzmemo $F_i$ i na poziciju $i-2$ u kodu stavimo 1 (pozicije u kodu broje se slijeva nadesno počevši od 0).
3.  Ako je $n$ pozitivan, vraćamo se na korak 1.
4.  Na kraju na kraj koda dodamo 1, što označava završetak koda.

Dekodiranje je analogno: najprije uklonimo zadnju jedinicu, a zatim za svaku poziciju $i$ na kojoj je u kodu 1 (pozicije se broje slijeva nadesno počevši od 0) rezultatu pribrojimo $F_{i+2}$. Konačni je rezultat izvorni broj.

## Periodičnost po modulu

Za Fibonaccijev niz po modulu $m$ lako se Dirichletovim principom (principom pretinaca) dokaže da je periodičan. Budući da računanje svakog člana Fibonaccijeva niza ovisi o vrijednostima prethodnih dvaju članova, trenutno stanje niza treba opisati parom susjednih Fibonaccijevih brojeva. Promotrimo prvih $m^2+1$ parova Fibonaccijevih brojeva po modulu:

$$
(F_0,\ F_1),\ (F_1,\ F_2),\ \ldots,\ (F_{m^2},\ F_{m^2 + 1})
$$

Sustav ostataka po modulu $m$ ima $m$ elemenata, što znači da postoji najviše $m^2$ međusobno različitih parova. Stoga među prvih $m^2+1$ parova nužno postoje dva jednaka para, a iz ta se dva para dalje generira jednak Fibonaccijev niz. Dakle, Fibonaccijev niz je periodičan, a (najmanji pozitivni) period ne premašuje $m^2$.

### Pisanov period

Najmanji pozitivni period Fibonaccijeva niza po modulu $m$ naziva se **Pisanov period** (Pisano period, [OEIS A001175](http://oeis.org/A001175)). U ovom članku Pisanov period po modulu $m$ označavamo $\pi(m)$.

Ovo se opažanje može iskoristiti za računanje $n$-tog Fibonaccijeva broja po modulu $m$. Ako je $n$ vrlo velik, treba izračunati period Fibonaccijeva niza po modulu $m$. Naravno, dovoljno je izračunati bilo koji period, ne nužno najmanji pozitivni.

U tu svrhu vrijede sljedeći rezultati:

1.  Za relativno proste module $m_1,m_2$ vrijedi $\pi(m_1m_2)=\operatorname{lcm}(\pi(m_1),\pi(m_2))$.
2.  Za prost broj $p$ i pozitivni cijeli broj $e$ vrijedi $\pi(p^{e})\mid p^{e-1}\pi(p)$.
3.  Za $m=2^e~(e\in\mathbf N_+)$ vrijedi $\pi(m)=3\cdot 2^{e-1}$.
4.  Za $m=5^e~(e\in\mathbf N_+)$ vrijedi $\pi(m)=4\cdot 5^e$.
5.  Naposljetku, za prost broj $p\equiv\pm1\pmod{10}$ vrijedi $\pi(p)\mid(p-1)$, a za prost broj $p\equiv\pm3\pmod{10}$ vrijedi $\pi(p)\mid 2(p+1)$.

Kombiniranjem ovih slučajeva može se pokazati da Pisanov period po modulu $m$ ne premašuje $6m$, pri čemu se jednakost postiže ako i samo ako je $m = 2\times 5^e~(e\in\mathbf N_+)$.

Na temelju gornjih rezultata i algoritma za rastav na proste faktore dobivamo sljedeću metodu brzog računanja Pisanova perioda:

??? example "Referentni kôd"
    ```cpp
    --8<-- "docs/math/code/combinatorics/fibonacci/pisano_estimate.cpp:pisano"
    ```

Tako dobiveni period može biti tek višekratnik Pisanova perioda. Da bismo dobili točan Pisanov period, možemo dodatno ispitati djelitelje tog perioda; ili ga pak možemo izravno izračunati [BSGS algoritmom](../number-theory/discrete-logarithm.md#algoritam-baby-step-giant-step) u vremenskoj složenosti $O(\sqrt{m})$.

### Dokaz

Na kraju ukratko dokazujemo gornje rezultate o Pisanovu periodu. Vrijedi napomenuti da se metodom opisanom u nastavku slični rezultati mogu poopćiti na proizvoljne homogene linearne rekurzivne nizove drugog reda s konstantnim koeficijentima. Iako se konkretne konstante razlikuju, Pisanov period tih nizova po modulu $m$ uvijek je $O(m)$.

Prvo opažanje: pomoću [kineskog teorema o ostatcima](../number-theory/crt.md) razmatranje se može ograničiti na slučaj modula koji je potencija prostog broja. Neka su $m_1,m_2$ dva relativno prosta modula. Periodi Fibonaccijeva niza po modulu $m_1$ su $\pi(m_1)$ i njegovi višekratnici, a po modulu $m_2$ su $\pi(m_2)$ i njegovi višekratnici, pa je njegov najmanji pozitivni period po modulu $m_1m_2$ upravo najmanji zajednički višekratnik od $\pi(m_1)$ i $\pi(m_2)$. To je rezultat 1 iz prethodnog teksta.

Drugo opažanje: Pisanov period po modulu $m$ zapravo je najmanji pozitivni cijeli broj $k$ takav da

$$
A^k = \begin{pmatrix} 1&1\\1&0 \end{pmatrix}^k \equiv I \pmod{m}.
$$

Drugim riječima, to je zapravo [red](../algebra/group-theory.md#阶) matrice $A$ po modulu $m$[^mod-m].

Slučaj modula $m=p^e$ koji je potencija prostog broja može se klasičnim argumentom podizanja eksponenta povezati sa slučajem odgovarajućeg prostog modula. Neka je $k=\pi(p^e)$; tada postoji kvadratna matrica $\Lambda$ reda 2 takva da vrijedi

$$
A^k = p^e\Lambda + I 
$$

Stoga, prema [binomnom teoremu](./combination.md#binomni-teorem), vrijedi

$$
A^{kp} = (p^e\Lambda + I)^p = I + \sum_{i=1}^p\binom{p}{i}(p^e\Lambda)^i \equiv I\pmod{p^{e+1}}. 
$$

Dakle, prema [svojstvima reda](../number-theory/primitive-root.md#ciklička-struktura-potencija), vrijedi $\pi(p^{e+1})\mid kp = p\pi(p^e)$. Indukcijom po $e$ slijedi da uvijek vrijedi $\pi(p^e)\mid p^{e-1}\pi(p)$.

Za slučaj prostog modula $p$ u ovom članku razmatramo dva načina dokazivanja.

=== "Pomoću formule za opći član"
    Jedan način koristi formulu za opći član Fibonaccijeva niza:
    
    $$
    F_n = \dfrac{1}{\sqrt{5}}\left(\dfrac{1+\sqrt{5}}{2}\right)^n - \dfrac{1}{\sqrt{5}}\left(\dfrac{1-\sqrt{5}}{2}\right)^n.
    $$
    
    Razvijemo je binomnim teoremom i poništimo članove s korijenima:
    
    $$
    F_n = \dfrac{1}{2^{n-1}}\sum_{i=0}^{\lfloor(n-1)/2\rfloor}\binom{n}{2i+1}5^i.
    $$
    
    Za $p=2$ ovaj se izraz ne može izravno uzeti po modulu, ali se može provjeriti da je odgovarajući Pisanov period $\pi(2)=3$. Za $p=5$ vrijedi $F_n\equiv n\cdot 3^{n-1}\pmod{p}$, pa se izravno može provjeriti da je odgovarajući Pisanov period $\pi(5)=20$. Preostali neparni prosti moduli dijele se na dva slučaja:
    
    -   Ako je $p\equiv 1,4\pmod{5}$, vrijedi
    
        $$
        \begin{aligned}
        F_{p} &\equiv \dfrac{1}{2^{p-1}}\binom{p}{p}5^{(p-1)/2} \equiv 1 \pmod{p},\\
        F_{p+1} &\equiv \dfrac{1}{2^p}\left(\binom{p+1}{1} + \binom{p+1}{p}5^{(p-1)/2}\right) \equiv 1 \pmod{p}.
        \end{aligned}
        $$
    
        Pri pojednostavljivanju korišteni su sljedeći rezultati: prema [Lucasovu teoremu](../number-theory/lucas.md), za $0 < k < p$ vrijedi $\dbinom{p}{k}\equiv 0\pmod{p}$, a za $1 < k < p$ vrijedi $\dbinom{p+1}{k}\equiv 0\pmod{p}$; prema [malom Fermatovu teoremu](../number-theory/fermat.md#mali-fermatov-teorem) vrijedi $2^{p-1}\equiv 5^{p-1}\equiv 1\pmod{p}$; za $p\equiv 1,4\pmod{5}$ broj $p$ je kvadratni ostatak po modulu $5$, pa je prema [kvadratnom zakonu reciprociteta](../number-theory/quad-residue.md#kvadratni-zakon-reciprociteta) i $5$ kvadratni ostatak po modulu $p$, odakle $5^{(p-1)/2} \equiv 1\pmod{p}$. Iz toga slijedi $(F_p,F_{p+1}) \equiv (F_1,F_2) \pmod{p}$, pa je $(p-1)$ jedan period po modulu $p$. Dakle, $\pi(p)\mid(p-1)$.
    -   Ako je $p\equiv 2,3\pmod{5}$, vrijedi
    
        $$
        \begin{aligned}
        F_{2p} &\equiv \dfrac{1}{2^{2p-1}}\binom{2p}{p}5^{(p-1)/2} \equiv -1 \pmod{p},\\
        F_{2p+1} &\equiv \dfrac{1}{2^{2p}}\left(\binom{2p+1}{1} + \binom{2p+1}{p}5^{(p-1)/2} + \binom{2p+1}{2p+1}5^p\right) \equiv -1\pmod{p}.
        \end{aligned}
        $$
    
        Pri pojednostavljivanju korišteni su sljedeći rezultati: prema Lucasovu teoremu, za $0 < k < p$ i $p < k < 2p$ vrijedi $\dbinom{p}{k}\equiv 0\pmod{p}$ te $\dbinom{2p}{p}\equiv 2\pmod{p}$, a za $1 < k < p$ i $p + 1 < k < 2p$ vrijedi $\dbinom{p}{k}\equiv 0\pmod{p}$ te $\dbinom{2p+1}{p}\equiv 2\pmod{p}$; prema malom Fermatovu teoremu vrijedi $2^{p-1}\equiv 5^{p-1}\equiv 1\pmod{p}$; za $p\equiv 2,3\pmod{5}$ broj $p$ je kvadratni neostatak po modulu $5$, pa je prema kvadratnom zakonu reciprociteta i $5$ kvadratni neostatak po modulu $p$, odakle $5^{(p-1)/2} \equiv -1\pmod{p}$. Iz toga slijedi $(F_{2p},F_{2p+1}) \equiv (F_{-2},F_{-1}) \pmod{p}$, pa je $2(p+1)$ jedan period po modulu $p$. Dakle, $\pi(p)\mid 2(p+1)$.
    
    Time je dokaz dovršen. Ograničenje je ove metode što se uvelike oslanja na formulu za opći član Fibonaccijeva niza, pa ju je teže izravno poopćiti na općeniti slučaj.

=== "Pomoću proširenja polja"
    Drugi način dokazivanja pokušava izravno izračunati red matrice $A=\begin{pmatrix}1&1\\1&0\end{pmatrix}$. Njezin je [karakteristični polinom](../linear-algebra/char-poly.md) $f(x) = x^2-x-1$, s diskriminantom $\Delta = 5$. Za modul $p=5$ vrijedi $\Delta\equiv 0\pmod{5}$, matrica $A$ ima dvije jednake svojstvene vrijednosti $\lambda=3$ i ne može se dijagonalizirati, pa taj slučaj treba izračunati zasebno. Za modul $p\equiv 1,4\pmod{5}$, prema kvadratnom zakonu reciprociteta diskriminanta $\Delta=5$ kvadratni je ostatak po modulu $p$, matrica $A$ u polju $\mathbf F_p$ ima dvije različite svojstvene vrijednosti $\lambda_1\neq\lambda_2$, a red matrice $A$ jednak je $\operatorname{lcm}(\operatorname{ord}(\lambda_1),\operatorname{ord}(\lambda_2))$ i nužno dijeli $|\mathbf F_p^\times|=p-1$. Za modul $p\equiv 2,3\pmod{5}$, prema kvadratnom zakonu reciprociteta diskriminanta $\Delta=5$ kvadratni je neostatak po modulu $p$, matrica $A$ u polju $\mathbf F_p$ nema svojstvenih vrijednosti, nego tek u [proširenju polja](../algebra/field-theory.md#域的扩张) $\mathbf F_p[\sqrt{5}]$ ima dvije različite svojstvene vrijednosti $\lambda_1\neq\lambda_2$; budući da Frobeniusov endomorfizam $x\mapsto x^p$ zamjenjuje ta dva korijena, vrijedi $\lambda_2=\lambda_1^p$, pa je $\lambda_1^{p+1}=\lambda_2^{p+1}=\lambda_1\lambda_2=-1$, odnosno $\lambda_1^{2(p+1)}=\lambda_2^{2(p+1)}=1$; stoga je red matrice $A$ jednak $\operatorname{lcm}(\operatorname{ord}(\lambda_1),\operatorname{ord}(\lambda_2))$ i nužno dijeli $2(p+1)$. Time se dobiva isti zaključak kao i prethodnom metodom.

Ukupno, za pojedine slučajeve redom vrijedi:

-   $\pi(2^e)=\dfrac{3}{2}\cdot 2^e,~\dfrac{1}{4}\pi(5^e)=5^e$.
-   Za $p\equiv\pm1\pmod{10}$ vrijedi $\pi(p^e) \mid (p-1)p^{e-1}$, pa je $\pi(p^e)\le p^e$.
-   Za $p\equiv\pm3\pmod{10}$ vrijedi $\dfrac{1}{4}\pi(p^e) \mid \dfrac{p+1}{2}p^{e-1}$, pa je $\dfrac{1}{4}\pi(p^e)\le p^e$.

Stoga, prema rezultatu 1, za općeniti modul $m=\prod_i p_i^{e_i}$ vrijedi

$$
\begin{aligned}
\pi(m)&=\operatorname{lcm}\{\pi(p_i^{e_i}):p_i\in\mathbf P\} \\
&\le \operatorname{lcm}\{\pi(p_i^{e_i}):p_i=2\text{ or }p_i\equiv\pm1~(\operatorname{mod}{10})\}\\
&\quad \cdot 4\cdot\operatorname{lcm}\{\pi(p_i^{e_i})/4:p_i=5\text{ or }p_i\equiv\pm3~(\operatorname{mod}{10})\}\\
&\le \prod\{\pi(p_i^{e_i}):p_i=2\text{ or }p_i\equiv\pm1~(\operatorname{mod}{10})\}\\
&\quad \cdot 4\cdot\prod\{\pi(p_i^{e_i})/4:p_i=5\text{ or }p_i\equiv\pm3~(\operatorname{mod}{10})\}\\
&\le \dfrac{3}{2}\cdot\prod\{p_i^{e_i}:p_i=2\text{ or }p_i\equiv\pm1~(\operatorname{mod}{10})\}\\
&\quad \cdot 4\cdot\prod\{p_i^{e_i}:p_i=5\text{ or }p_i\equiv\pm3~(\operatorname{mod}{10})\}\\
&= 6m.
\end{aligned}
$$

To pokazuje da Pisanov period Fibonaccijeva niza po modulu $m$ nikad ne premašuje $6m$, a jednakost se postiže ako i samo ako je $m=2\cdot 5^e$.

## Zadaci za vježbu

-   [SPOJ - Euclid Algorithm Revisited](http://www.spoj.com/problems/MAIN74/)
-   [SPOJ - Fibonacci Sum](http://www.spoj.com/problems/FIBOSUM/)
-   [HackerRank - Is Fibo](https://www.hackerrank.com/challenges/is-fibo/problem)
-   [Project Euler - Even Fibonacci numbers](https://www.hackerrank.com/contests/projecteuler/challenges/euler002/problem)
-   [Luogu P4000 斐波那契数列 (Fibonaccijev niz)](https://www.luogu.com.cn/problem/P4000)

## Literatura i bilješke

-   [Fibonacci sequence - Wikipedia](https://en.wikipedia.org/wiki/Fibonacci_sequence)
-   [Zeckendorf's theorem - Wikipedia](https://en.wikipedia.org/wiki/Zeckendorf%27s_theorem)
-   [Pisano period - Wikipedia](https://en.wikipedia.org/wiki/Pisano_period)

**Ova je stranica većim dijelom prevedena iz blog-zapisa [Числа Фибоначчи](http://e-maxx.ru/algo/fibonacci_numbers) i njegova engleskog prijevoda [Fibonacci Numbers](https://cp-algorithms.com/algebra/fibonacci-numbers.html). Ruska je inačica objavljena pod licencijom Public Domain + Leave a Link, a engleska pod licencijom CC-BY-SA 4.0. Sadržaj je izmijenjen.**

[^mod-m]: Strogo govoreći, to je red matrice $A$ u općoj linearnoj grupi $GL_2(\mathbf Z_m)$.
