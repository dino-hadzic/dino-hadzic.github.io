---
title: Verižni razlomci
---

## Uvod

Verižni razlomci omogućuju da se realan broj prikaže kao limes konvergentnog niza racionalnih brojeva. Racionalni brojevi u tom nizu lako se računaju i ujedno daju najbolje aproksimacije tog realnog broja, pa se verižni razlomci često koriste na algoritamskim natjecanjima. Osim toga, verižni razlomci usko su povezani s Euklidovim algoritmom, pa se mogu primijeniti na čitav niz problema iz teorije brojeva.

???+ info "O implementacijama algoritama vezanih uz verižne razlomke"
    U ovom se članku daje niz implementacija algoritama s verižnim razlomcima; za neke od njih nije moguće jamčiti da svi cijeli brojevi koji se pojavljuju u međukoracima stanu u 32-bitne ili 64-bitne cjelobrojne varijable. U takvim slučajevima pogledajte odgovarajuću implementaciju u Pythonu ili u C++ implementaciji cjelobrojne varijable zamijenite [klasom za aritmetiku velikih brojeva](../bignum.md). Radi preglednosti, dio koda u ovom članku poziva funkcije implementirane ranije u tekstu, a da se njihova implementacija ne ponavlja.

## Verižni razlomci

**Verižni razlomak** (continued fraction) sam po sebi samo je formalna oznaka.

???+ abstract "Konačni verižni razlomak"
    Za niz $\{a_k\}_{k=0}^n$ verižni razlomak $[a_0,a_1,\ldots,a_n]$ označava razvoj
    
    $$
    x = a_0+\dfrac{1}{a_1+\dfrac{1}{a_2+\dfrac{1}{\cdots+\dfrac{1}{a_n}}}}.
    $$
    
    Verižni razlomak ima smisla ako i samo ako odgovarajući razvoj ima smisla. Brojevi $a_k$ nazivaju se **članovi** (terms) ili **koeficijenti** (coefficients) verižnog razlomka.

???+ info "Oznake"
    Općenitiji verižni razlomci dopuštaju da brojnici u razvoju ne budu stalno jednaki $1$; tada se mora prilagoditi i oznaka verižnog razlomka, što izlazi iz okvira ovog članka. Osim toga, u nekoj se literaturi prvi zarez „$,$” piše kao točka sa zarezom „$;$”; značenjem se to ne razlikuje od oznaka u ovom članku.

Dakako, verižni razlomci mogu se poopćiti i na beskonačne nizove.

???+ abstract "Beskonačni verižni razlomak"
    Za beskonačan niz $\{a_k\}_{k=0}^\infty$ verižni razlomak $[a_0,a_1,\ldots]$ označava limes
    
    $$
    x = \lim_{k\rightarrow\infty} x_k = \lim_{k\rightarrow\infty} [a_0,a_1,\ldots,a_k].
    $$
    
    Verižni razlomak ima smisla ako i samo ako odgovarajući limes postoji. Pritom se $x_k=[a_0,a_1,\ldots,a_k]$ naziva $k$-ta **konvergenta** (convergent) ili **približni razlomak** broja $x$, a $r_k=[a_k,a_{k+1},\ldots]$ naziva se $k$-ti **ostatak** ili **potpuni kvocijent** (complete quotient) broja $x$. U skladu s tim, član $a_k$ ponekad se naziva i $k$-ti **parcijalni kvocijent** (partial quotient).

### Jednostavni verižni razlomci

U teoriji brojeva uglavnom se promatra slučaj u kojem su svi članovi verižnog razlomka cijeli brojevi.

???+ abstract "Jednostavni verižni razlomak"
    Ako je u verižnom razlomku $[a_0,a_1,\ldots]$ broj $a_0$ cijeli, a $a_1,a_2,\ldots$ pozitivni cijeli brojevi, on se naziva **jednostavni verižni razlomak** (simple continued fraction), ili kraće samo **verižni razlomak**. Ako je niz $\{a_i\}$ konačan, naziva se **konačni (jednostavni) verižni razlomak**; inače se naziva **beskonačni (jednostavni) verižni razlomak**. Nadalje, $a_0$ se naziva njegov **cijeli dio** (integer part).

Ako nije drukčije rečeno, svi verižni razlomci spomenuti u ovom članku jednostavni su verižni razlomci. Može se dokazati da beskonačni jednostavni verižni razlomak nužno konvergira te da su ostatci jednostavnog verižnog razlomka uvijek pozitivni.

Verižni razlomci imaju sljedeća osnovna svojstva:

???+ note "Svojstva"
    Neka je realan broj $x=[a_0,a_1,a_2,\ldots]$. Tada vrijedi:
    
    1.  za svaki $k\in\mathbf Z$ vrijedi $x+k=[a_0+k,a_1,a_2,\ldots]$;
    2.  za realan broj $x>1$ vrijedi $a_0>0$, a njegova recipročna vrijednost je $x^{-1}=[0,a_0,a_1,a_2,\ldots]$.

Konačni verižni razlomci odgovaraju racionalnim brojevima. Svaki racionalni broj može se prikazati verižnim razlomkom na točno dva načina, pri čemu je duljina jednog prikaza nužno neparna, a drugog parna. Jedina je razlika između ta dva načina to je li posljednji član jednak $1$, tj.

$$
x = [a_0,a_1,\ldots,a_n] = [a_0,a_1,\ldots,a_n-1,1].
$$

Ta se dva verižna razlomka nazivaju **prikazi verižnim razlomkom** (continued fraction representation) racionalnog broja $x$. Onaj čiji posljednji član nije jedan naziva se standardni prikaz, a onaj čiji je posljednji član jedan naziva se nestandardni prikaz.[^one-representation]

??? example "Primjer"
    Prikazi racionalnog broja $x=\dfrac{5}{3}$ verižnim razlomkom jesu
    
    $$
    \begin{aligned}
    x = [1,1,1,1] &= 1+\dfrac{1}{1+\dfrac{1}{1+\dfrac{1}{1}}},\\
    x = [1,1,2] &= 1+\dfrac{1}{1+\dfrac{1}{2}}.
    \end{aligned}
    $$

Beskonačni verižni razlomci odgovaraju iracionalnim brojevima. Štoviše, svaki iracionalni broj može se prikazati verižnim razlomkom na jedinstven način, koji se naziva prikaz iracionalnog broja verižnim razlomkom.

### Određivanje prikaza verižnim razlomkom

Da bismo odredili prikaz nekog realnog broja $x$ verižnim razlomkom, dovoljno je primijetiti da njegov ostatak $r_k$, ako nije cijeli broj, nužno zadovoljava

$$
r_k = [a_k,a_{k+1},\ldots] = [a_k,r_{k+1}] = a_k + \dfrac{1}{r_{k+1}}.
$$

Pritom je $r_{k+1}>1$. Stoga se, počevši od $r_0=x$, može rekurzivno računati

$$
a_k = \lfloor r_k\rfloor,\ r_{k+1} = \dfrac{1}{r_k-a_k}.
$$

Niz $\{a_k\}$ koji nastaje tim postupkom uvijek je jednoznačno određen, osim ako neki ostatak $r_k$ postane cijeli broj. Ako se dogodi da je $r_k$ cijeli broj, postupak treba završiti, a može se po izboru ispisati odgovarajući standardni ili nestandardni prikaz.

Na algoritamskim natjecanjima najčešće se radi s racionalnim brojem $x=\dfrac{p}{q}$. Tada je svaki ostatak $r_k$ racionalan broj $\dfrac{p_k}{q_k}$, a za $k>0$, budući da je $r_k>1$, uvijek vrijedi $p_k>q_k$. Raspisivanjem gornje rekurzije dobiva se

$$
a_k = \left\lfloor\frac{p_k}{q_k}\right\rfloor,\ r_{k+1} = \dfrac{1}{r_k-a_k} = \dfrac{q_k}{p_k-a_kq_k} = \dfrac{q_k}{p_k\bmod q_k}.
$$

Taj je postupak zapravo [Euklidov algoritam](./gcd.md#欧几里得算法) primijenjen na $p$ i $q$. To također pokazuje da je za racionalan broj $x=\dfrac{p}{q}$ duljina prikaza verižnim razlomkom $O(\log\min\{p, q\})$. Složenost računanja prikaza racionalnog broja $\dfrac{p}{q}$ također je $O(\log\min\{p, q\})$.

???+ example "Referentna implementacija"
    Za zadani brojnik $p$ i nazivnik $q$ razlomka ispisati niz koeficijenata verižnog razlomka $[a_0,a_1,\ldots,a_n]$.
    
    === "C++"
        ```cpp
        --8<-- "docs/math/code/continued-fraction/diophantine.cpp:fraction"
        ```
    
    === "Python"
        ```py
        --8<-- "docs/math/code/continued-fraction/diophantine.py:fraction"
        ```

## Konvergente

U definiciji verižnog razlomka uveden je pojam konvergente. Konvergente realnog broja upravo su konvergente njegova prikaza verižnim razlomkom: ako se u prikazu realnog broja $x$ verižnim razlomkom zadrži samo prvih $k$ članova, dobiveni verižni razlomak $x_k$ naziva se $k$-ta konvergenta realnog broja $x$. Konvergente $x_k$ realnog broja $x$ racionalni su brojevi, a niz $\{x_k\}$ konvergira realnom broju $x$.

??? example "Primjer: konvergente zlatnog reza"
    Prvih nekoliko konvergenti verižnog razlomka $x=[1,1,1,1,\ldots]$ jesu
    
    $$
    \begin{aligned}
    x_0 &= [1]=1,\\
    x_1 &= [1,1]=2,\\
    x_2 &= [1,1,1]=\dfrac{3}{2},\\
    x_3 &= [1,1,1,1]=\dfrac{5}{3},\\
    x_4 &= [1,1,1,1,1]=\dfrac{8}{5}.
    \end{aligned}
    $$
    
    Indukcijom se može dokazati
    
    $$
    x_k = \frac{F_{k+2}}{F_{k+1}},
    $$
    
    gdje je $\{F_k\}$ [Fibonaccijev niz](../combinatorics/fibonacci.md). Iz formule za njegov opći član slijedi
    
    $$
    x_k = \frac{\phi^{k+2}-(-\phi)^{-(k+2)}}{\phi^{k+1}-(-\phi)^{-(k+1)}},
    $$
    
    gdje je $\phi=\dfrac{1+\sqrt{5}}{2}$ zlatni rez. Kad $k$ teži u beskonačnost, vrijedi
    
    $$
    x=\lim_{k\rightarrow\infty}x_k=\phi.
    $$
    
    Dakle, verižni razlomak $x=[1,1,1,1,\ldots]$ prikazuje zlatni rez $\phi$.

Te konvergente teže odgovarajućem realnom broju, pa se mogu upotrijebiti za njegovu aproksimaciju. Zbog toga je potrebno upoznati svojstva konvergenti.

### Rekurzivne relacije

Najprije treba riješiti problem računanja konvergenti. Iako se konvergenta uvijek dobiva dodavanjem jednog člana na kraj verižnog razlomka, nije potrebno svaki put iznova računati njezinu vrijednost. Naime, konvergente zadovoljavaju sljedeću rekurzivnu relaciju:

???+ note "Rekurzivna formula"
    Neka se za verižni razlomak $x=[a_0,a_1,a_2,\ldots]$ njegova $k$-ta konvergenta $x_k=[a_0,a_1,\ldots,a_k]$ jednoznačno zapiše kao neskrativi razlomak $\dfrac{p_k}{q_k}$. Tada vrijedi
    
    $$
    \begin{aligned}
    p_k &= a_kp_{k-1}+p_{k-2},\\
    q_k &= a_kq_{k-1}+q_{k-2}.
    \end{aligned}
    $$
    
    Početne vrijednosti rekurzije (formalni) su razlomci
    
    $$
    x_{-1}=\frac{p_{-1}}{q_{-1}}=\frac{1}{0},\ x_{-2}=\frac{p_{-2}}{q_{-2}}=\frac{0}{1}.
    $$

??? note "Dokaz"
    Svaka je konvergenta konačni verižni razlomak. Već je spomenuto da je računanje konačnog verižnog razlomka zapravo isto što i provođenje Euklidova algoritma. No Euklidov algoritam daje sufiks verižnog razlomka, dok je za konvergente potreban njegov prefiks. Da bismo dobili taj prefiks, treba promotriti kako se verižni razlomak mijenja kad mu se doda jedan korak. U tu svrhu jedan korak Euklidova algoritma možemo prikazati množenjem matrica:
    
    $$
    M(a)=\begin{pmatrix} a & 1 \\ 1 & 0 \end{pmatrix},\qquad
    M(a)\begin{pmatrix} u\\ v \end{pmatrix}=\begin{pmatrix} au+v\\u \end{pmatrix},\qquad
    \frac{au+v}{u}=a+\frac{1}{u/v}.
    $$
    
    Vektor $(a_k,1)^{\mathrm{T}}$ predstavlja konačni verižni razlomak $[a_k]$; uzastopno množenje matricama slijeva odgovara uzastopnom dopisivanju koeficijenata verižnog razlomka s lijeve strane. Dopunjavanjem tog verižnog razlomka do konvergente $x_k=\dfrac{p_k}{q_k}=[a_0,a_1,\ldots,a_k]$ dobiva se jednakost
    
    $$
    M(a_0)M(a_1)M(a_2)\cdots M(a_{k-1})\begin{pmatrix}a_k\\1\end{pmatrix}=\begin{pmatrix}p_k\\q_k\end{pmatrix}.
    $$
    
    Iz $\det(M(a_0)M(a_1)\cdots M(a_{k-1}))=(-1)^{k}$ slijedi da ta matrična transformacija primitivni vektor $(a_k,1)^{\mathrm{T}}$ preslikava u $(p_k,q_k)^{\mathrm{T}}$, pa su $p_k$ i $q_k$ nužno relativno prosti. Drugi stupac matrice $M(a_k)$ jest $(1,0)^{\mathrm{T}}$, a $M(a_{k-1})(1,0)^{\mathrm{T}}=(a_{k-1},1)^{\mathrm{T}}$, pa se umnožak za taj stupac dobiva rekurzivnim uvrštavanjem. Dopunimo li taj stupac, dobivamo
    
    $$
    M(a_0)M(a_1)M(a_2)\cdots M(a_k)=\begin{pmatrix}p_k & p_{k-1}\\q_k & q_{k-1}\end{pmatrix}.
    $$
    
    Sada je dovoljno uvrstiti prvih $k$ faktora matričnog umnoška i lako se dobiva rekurzivna formula za konvergente:
    
    $$
    \begin{aligned}
    \begin{pmatrix}p_{k-1} & p_{k-2}\\q_{k-1} & q_{k-2}\end{pmatrix}M(a_k)
    &=\begin{pmatrix}p_k & p_{k-1}\\q_k & q_{k-1}\end{pmatrix}\\
    \Rightarrow\quad p_k&=a_k p_{k-1}+p_{k-2},\qquad q_k=a_k q_{k-1}+q_{k-2}.
    \end{aligned}
    $$

???+ info "Oznake"
    Kad se u ovom članku konvergenta $x_k$ zapisuje kao $\dfrac{p_k}{q_k}$, uvijek se podrazumijeva da su brojnik $p_k$ i nazivnik $q_k$ zadani gornjom rekurzivnom relacijom. Prethodni dokaz pokazuje da se tako uvijek dobiva neskrativi prikaz konvergente.

Iz te rekurzije slijedi da se

$$
x_k=\dfrac{a_kp_{k-1}+p_{k-2}}{a_kq_{k-1}+q_{k-2}}
$$

nalazi između $x_{k-1}$ i $x_{k-2}$.

Na temelju rekurzivne relacije iz ovog odjeljka dobiva se sljedeći algoritam za računanje konvergenti:

???+ example "Referentna implementacija"
    Za zadane koeficijente verižnog razlomka $a_0,a_1,\ldots,a_n$ odrediti niz brojnika i nazivnika konvergenti $(p_0,q_0),(p_1,q_1),\ldots,(p_n,q_n)$.
    
    === "C++"
        ```cpp
        --8<-- "docs/math/code/continued-fraction/diophantine.cpp:convergents"
        ```
    
    === "Python"
        ```py
        --8<-- "docs/math/code/continued-fraction/diophantine.py:convergents"
        ```

### Kontinuante

**Kontinuanta** (continuant) potječe od međuveličina u rekurzivnoj relaciji za konvergente.[^continuant]

???+ abstract "Kontinuanta"
    Za svaki konačni niz kontinuanta se rekurzivno definira ovako:
    
    -   $K(\varnothing)=1,\, K(a)=a$;
    -   za $n\ge 1$, $K(a_0,\ldots,a_n)=a_n K(a_0,\ldots,a_{n-1})+K(a_0,\ldots,a_{n-2})$.

Iz rekurzije za konvergente lako se vidi da se za $x=[a_0,a_1,a_2,\ldots]$ njegova konvergenta $\dfrac{p_k}{q_k}=[a_0,a_1,\ldots,a_k]$ može izraziti kontinuantama:

$$
p_k=K(a_0,a_1,\ldots,a_k),\quad q_k=K(a_1,\ldots,a_k).
$$

Drugim riječima, kontinuantama se mogu prikazati konačni verižni razlomci:

$$
\frac{K(a_0,a_1,\ldots,a_k)}{K(a_1,\ldots,a_k)}=[a_0,a_1,\ldots,a_k].
$$

I prethodni matrični prikaz lako se zapisuje pomoću kontinuanti. Za $k\ge 1$ vrijedi

$$
M(a_0)\cdots M(a_k)=
\begin{pmatrix}
K(a_0,\ldots,a_k)&K(a_0,\ldots,a_{k-1})\\
K(a_1,\ldots,a_k)&K(a_1,\ldots,a_{k-1})
\end{pmatrix}.
$$

Najvažnije svojstvo kontinuante njezina je simetričnost.

???+ note "Simetričnost kontinuante"
    Za svaki konačni niz $(a_0,\ldots,a_n)$ vrijedi
    
    $$
    K(a_0,\ldots,a_n)=K(a_n,\ldots,a_0).
    $$

??? note "Dokaz"
    Budući da je svaka matrica $M(a)$ simetrična, transponiranjem njihova umnoška dobivamo
    
    $$
    (M(a_0)\cdots M(a_n))^{\mathrm{T}}=M(a_n)^{\mathrm{T}}\cdots M(a_0)^{\mathrm{T}}=M(a_n)\cdots M(a_0).
    $$
    
    Usporedbom gornjih lijevih elemenata dvaju umnožaka odmah slijedi tvrdnja.

Zbog simetričnosti rekurzija za kontinuante može se zapisati i u obrnutom smjeru:

$$
K(a_0,\ldots,a_n)=a_0 K(a_1,\ldots,a_n)+K(a_2,\ldots,a_n).
$$

??? info "Prikaz kontinuante determinantom"
    Kontinuanta se može zapisati kao determinanta:
    
    $$
    K(a_0,\ldots,a_k)=\det
    \begin{pmatrix}
    a_0 & 1 & 0 & \cdots & 0 \\
    -1 & a_1 & 1 & \ddots & \vdots \\
    0 & -1 & a_2 & \ddots & 0 \\
    \vdots & \ddots & \ddots & \ddots & 1 \\
    0 & \cdots & 0 & -1 & a_k
    \end{pmatrix}.
    $$
    
    To je determinanta [tridijagonalne matrice](https://en.wikipedia.org/wiki/Tridiagonal_matrix); razvojem od gornjeg lijevog kuta dobiva se obrnuta rekurzija, a razvojem od donjeg desnog kuta dobiva se rekurzija iz definicije.

Još jedno zanimljivo svojstvo kontinuante jest svojstvo spajanja.

???+ note "Spajanje kontinuanti"
    Za dva neprazna niza $(a_1,\ldots,a_m)$ i $(b_1,\ldots,b_n)$ vrijedi
    
    $$
    K(a_1,\ldots,a_m,b_1,\ldots,b_n)=K(a_1,\ldots,a_m)K(b_1,\ldots,b_n)+K(a_1,\ldots,a_{m-1})K(b_2,\ldots,b_n).
    $$

??? note "Dokaz"
    Dovoljno je matrični umnožak asocijativnošću razdvojiti na dva dijela. Neka je
    
    $$
    P=M(a_1)\cdots M(a_m),\quad Q=M(b_1)\cdots M(b_n),
    $$
    
    tada vrijedi
    
    $$
    (PQ)_{1,1}=P_{1,1}Q_{1,1}+P_{1,2}Q_{2,1}.
    $$
    
    To je upravo identitet iz svojstva spajanja.

To se svojstvo može iskoristiti za proučavanje međuveličina Euklidova algoritma. Na primjer, Heilbronn ga je upotrijebio za procjenu prosječnog broja koraka Euklidova algoritma[^heilbronn]. U nastavku je natjecateljski zadatak u kojem se tim svojstvom rješava jedan problem sumiranja.

???+ example "[Luogu P17229 \[Math×Girl²\] 英雄变奏曲 (Herojske varijacije)](https://www.luogu.com.cn/problem/P17229)"
    Zadani su pozitivan cijeli broj $N$ i vrijednosti dviju cjelobrojnih funkcija $g,h:\{1,2,\ldots,N\}\to\mathbf{Z}$ u svim točkama.
    
    Za cijele brojeve $x,y$ takve da je $1\le y<x\le N$ neka je $z=x\bmod y$ i rekurzivno definirajmo
    
    $$
    f(x,y)=
    \begin{cases}
    0, & z=0,\\
    g\!\left(\left\lfloor\dfrac{x}{y}\right\rfloor\right)
    h\!\left(\left\lfloor\dfrac{y}{z}\right\rfloor\right)
    +f(y,z), & z>0.
    \end{cases}
    $$
    
    Izračunajte
    
    $$
    S(N)=
    \sum_{\substack{1\le b<a\le N\\\gcd(a,b)=1}}f(a,b).
    $$

??? note "Ideja"
    Definicija funkcije $f(x,y)$ u zadatku odgovara tijeku Euklidova algoritma. Prikažimo Euklidov algoritam verižnim razlomkom: neka je $\dfrac{x}{y}=[a_0,a_1,\ldots,a_k]$ standardni prikaz konačnog verižnog razlomka. Tada je
    
    $$
    f(x,y)=\sum_{i=0}^{k-1}g(a_i)h(a_{i+1}).
    $$
    
    Primjenom svojstva spajanja kontinuanti, razrežemo li kontinuantu na mjestu $a_i$, dobivamo
    
    $$
    K(a_0,a_1,\ldots,a_k)=K(a_0,\ldots,a_i)K(a_{i+1},\ldots,a_k)+K(a_0,\ldots,a_{i-1})K(a_{i+2},\ldots,a_k).
    $$
    
    Neka je
    
    $$
    \begin{aligned}
    X&=K(a_0,\ldots,a_i),\quad Y=K(a_0,\ldots,a_{i-1}),\\
    Z&=K(a_{i+1},\ldots,a_k),\quad W=K(a_{i+2},\ldots,a_k).
    \end{aligned}
    $$
    
    Iz svojstva da kontinuante prikazuju konačne verižne razlomke dobivamo
    
    $$
    \frac{X}{Y}=[a_i,a_{i-1},\ldots,a_0],\quad \frac{Z}{W}=[a_{i+1},a_{i+2},\ldots,a_k].
    $$
    
    Uvjeti koje treba zadovoljiti jesu $\gcd(X,Y)=\gcd(Z,W)=1$, $1\le Y\le X$, $1\le W\le Z$, $XZ+YW=x\le N$. Čini se da smo konstruirali bijekciju između $(x,y,i)$ i $(X,Y,Z,W)$. No treba primijetiti da, budući da $a_0$ može biti $1$, verižni razlomak koji odgovara $\dfrac{X}{Y}$ može biti nestandardni prikaz, dok je verižni razlomak koji odgovara $\dfrac{Z}{W}$ nužno standardni prikaz (pa stoga ne može biti $Z=W=1$).
    
    Izračunajmo sada doprinos četvorke $(X,Y,Z,W)$ izvornoj sumi nakon ove transformacije. Zaokruživanjem razlomka nadolje dobiva se prvi član verižnog razlomka, čime dobivamo argumente funkcija. Zatim razlikujemo slučajeve za $(X,Y)$:
    
    1.  $Y>1$: i standardni i nestandardni prikaz od $\dfrac{X}{Y}$ odgovaraju po jednoj trojci $(x,y,i)$, pa je doprinos $2g\left(\left\lfloor\dfrac{X}{Y}\right\rfloor\right)h\left(\left\lfloor\dfrac{Z}{W}\right\rfloor\right)$;
    2.  $Y=1,X\ge2$: $\dfrac{X}{Y}=X$ odgovara prikazima $[X]$ i $[X-1,1]$; pazite da je doprinos potonjeg drukčiji, pa je ukupni doprinos $(g(X)+g(X-1))h\left(\left\lfloor\dfrac{Z}{W}\right\rfloor\right)$;
    3.  $X=Y=1$: doprinos je $g(1)h\left(\left\lfloor\dfrac{Z}{W}\right\rfloor\right)$.
    
    Time smo vrlo nezgodnu sumu $S(N)$ pretvorili u sljedeću sumu po $X,Y,Z,W$ (uz dodatnu definiciju $g(0)=2g(1)$):
    
    $$
    \begin{aligned}
    S(N)={}&2\sum_{\substack{XZ+YW\le N\\X>Y\ge 1,\, Z>W\ge 1\\ \gcd(X,Y)=\gcd(Z,W)=1}}g(\lfloor X/Y\rfloor)h(\lfloor Z/W\rfloor) \\
    &+\sum_{\substack{XZ+W\le N\\X\ge 1,\, Z>W\ge 1\\\gcd(Z,W)=1}}(g(X-1)-g(X))h(\lfloor Z/W\rfloor).
    \end{aligned}
    $$
    
    Ta se suma razmjerno lako obrađuje uobičajenim alatima, pa to ovdje ne raspisujemo.

Kao posljedice rekurzivne relacije za konvergente i svojstava kontinuanti vrijede sljedeći teorem o obrnutom poretku i teorem o recipročnoj vrijednosti:

???+ note "Teorem o obrnutom poretku"
    Neka je $\dfrac{p_k}{q_k}$ $k$-ta konvergenta realnog broja $x=[a_0,a_1,a_2,\ldots]>0$. Tada su omjeri brojnika odnosno nazivnika dviju susjednih konvergenti
    
    $$
    \begin{aligned}
    \frac{p_k}{p_{k-1}}&=[a_k,a_{k-1},\ldots,a_1,a_0],\\
    \frac{q_k}{q_{k-1}}&=[a_k,a_{k-1},\ldots,a_1].
    \end{aligned}
    $$
    
    Ako je $a_0=0$ i $k\ge 2$, prvi verižni razlomak treba shvatiti kao odrezan na pretposljednjem članu, tj. $[a_k,a_{k-1},\ldots,a_2]$.

??? note "Dokaz"
    Iz prikaza kontinuantama slijedi
    
    $$
    \frac{q_k}{q_{k-1}}=\frac{K(a_1,\ldots,a_{k-1},a_k)}{K(a_1,\ldots,a_{k-1})}=\frac{K(a_k,a_{k-1},\ldots,a_1)}{K(a_{k-1},\ldots,a_1)}=[a_k,a_{k-1},\ldots,a_1].
    $$
    
    Ako je $a_0\neq 0$, tada je
    
    $$
    \frac{p_k}{p_{k-1}}=\frac{K(a_0,\ldots,a_{k-1},a_k)}{K(a_0,\ldots,a_{k-1})}=\frac{K(a_k,a_{k-1},\ldots,a_0)}{K(a_{k-1},\ldots,a_0)}=[a_k,a_{k-1},\ldots,a_0].
    $$
    
    Ako je $a_0=0$, iz rekurzije za kontinuante vrijedi $K(0,a_1,a_2,\ldots,a_k)=K(a_2,\ldots,a_k)$, pa je
    
    $$
    \frac{p_k}{p_{k-1}}=\frac{K(a_2,\ldots,a_{k-1},a_k)}{K(a_2,\ldots,a_{k-1})}=\frac{K(a_k,a_{k-1},\ldots,a_2)}{K(a_{k-1},\ldots,a_2)}=[a_k,a_{k-1},\ldots,a_2].
    $$

???+ note "Teorem o recipročnoj vrijednosti"
    Recipročne vrijednosti konvergenti realnog broja $x>0$ konvergente su broja $x^{-1}$.

??? note "Dokaz"
    Bez smanjenja općenitosti neka je $x>1$ s prikazom $[a_0,a_1,a_2,\ldots]$; tada je prikaz broja $x^{-1}$ verižnim razlomkom $[0,a_0,a_1,a_2,\ldots]$. Njihove konvergente dobivaju se iz rekurzivne relacije. Pritom za $x$ vrijede početni uvjeti $x_{-2}=\dfrac{0}{1}$ i $x_{-1}=\dfrac{1}{0}$, a za $y=x^{-1}$ početni uvjeti $y_{-1}=\dfrac{1}{0}$ i $y_{0}=\dfrac{0}{1}$. Stoga je $x_{-2}=(y_{-1})^{-1}$ i $x_{-1}=(y_0)^{-1}$. Iz rekurzivne relacije slijedi $x_k=y_{k+1}^{-1}$. To pokazuje da su recipročne vrijednosti konvergenti broja $x$ konvergente broja $y=x^{-1}$. Slučaj $0<x\le 1$ razmatra se analogno.

### Procjena pogreške

Pomoću rekurzivne formule za konvergente može se procijeniti pogreška koja nastaje aproksimiranjem realnog broja konvergentom.

Najprije izračunajmo razliku susjednih konvergenti:

???+ note "Razlika konvergenti"
    Neka je $x_k=\dfrac{p_k}{q_k}$ $k$-ta konvergenta realnog broja $x$. Tada vrijedi
    
    $$
    p_{k+1}q_k - p_kq_{k+1} = (-1)^k.
    $$
    
    Stoga je razlika dviju susjednih konvergenti
    
    $$
    x_{k+1} - x_k = \dfrac{(-1)^k}{q_{k+1}q_k}.
    $$

??? note "Dokaz"
    Iz rekurzivne relacije slijedi
    
    $$
    \begin{aligned}
    \det\begin{pmatrix}
    p_{k+1} & p_k \\
    q_{k+1} & q_k 
    \end{pmatrix}
    &=
    \det\begin{pmatrix}
    a_{k+1}p_{k}+p_{k-1} & p_k \\
    a_{k+1}q_{k}+q_{k-1} & q_k 
    \end{pmatrix}
    =
    \det\begin{pmatrix}
    p_{k-1} & p_k\\
    q_{k-1} & q_k
    \end{pmatrix}
    \\
    &=
    -
    \det\begin{pmatrix}
    p_k & p_{k-1}\\
    q_k & q_{k-1}
    \end{pmatrix}
    =
    (-1)^{k+2}
    \det\begin{pmatrix}
    1 & 0\\
    0 & 1
    \end{pmatrix}
    =(-1)^k.
    \end{aligned}
    $$
    
    To je upravo $p_{k+1}q_k - p_kq_{k+1} = (-1)^k$. Dijeljenjem obiju strana s $q_{k+1}q_k$ dobiva se tvrdnja o $x_{k+1}-x_k$.

Prema tome, konvergente s neparnim indeksom uvijek su veće od obiju susjednih, a konvergente s parnim indeksom uvijek su manje od obiju susjednih: konvergente se mijenjaju alternirajuće.

Promatramo li samo konvergente s parnim (neparnim) indeksom, taj je niz monotono rastući (padajući). Naime,

$$
x_{k+2}-x_k = \dfrac{(-1)^{k+1}}{q_{k+2}q_{k+1}}+\dfrac{(-1)^{k}}{q_{k+1}q_{k}} = \dfrac{(-1)^k(q_{k+2}-q_k)}{q_{k+2}q_{k+1}q_k} = \dfrac{(-1)^ka_{k+2}}{q_{k+2}q_k}
$$

pozitivno je (negativno) kad je $k$ paran (neparan). Istodobno, zbog rekurzije $q_{k}=a_kq_{k-1}+q_{k-2}$ nazivnici $q_k$ ne rastu sporije od Fibonaccijeva niza. Stoga razlika dviju susjednih konvergenti nužno teži nuli. To pokazuje da se konvergente s parnim indeksom odozdo, a one s neparnim indeksom odozgo približavaju istom limesu. Time je dokazano da beskonačni jednostavni verižni razlomak uvijek konvergira. Kako se konvergente približavaju odgovarajućem realnom broju prikazano je na sljedećoj slici:

![](./images/golden-ratio-convergents.svg)

???+ abstract "Gornja (donja) konvergenta"
    Za realan broj $x$ i njegovu konvergentu $x_k$: ako je $x_k>x$ ($x_k<x$), $x_k$ se naziva **gornja (donja) konvergenta** (upper (lower) convergent) broja $x$.

Već je pokazano da su gornje konvergente upravo konvergente s neparnim indeksom, a donje konvergente one s parnim indeksom.

Pomoću formule za razliku realan broj $x$ može se zapisati kao alternirajući red:

$$
x = a_0+\sum_{k=0}^{\infty}\dfrac{(-1)^k}{q_{k+1}q_k}.
$$

Konvergente i ostatci iz definicije verižnog razlomka upravo su parcijalne sume i ostatci tog reda.

Pomoću formule za razliku može se i izravno procijeniti pogreška aproksimacije realnog broja konvergentom:

???+ note "Pogreška"
    Neka je $x_k=\dfrac{p_k}{q_k}\neq x$ $k$-ta konvergenta realnog broja $x$. Tada vrijedi
    
    $$
    x_k - x = \dfrac{(-1)^k}{q_k\left(r_{k+1}q_k+q_{k-1}\right)},
    $$
    
    gdje je $r_{k+1}$ $k+1$-vi ostatak realnog broja $x$. Nadalje, vrijedi
    
    $$
    \dfrac{1}{2q_{k+1}^2} \le \dfrac{1}{q_k(q_k+q_{k+1})} \le \left|x-\frac{p_k}{q_k}\right| \le \dfrac{1}{q_kq_{k+1}} \le \dfrac{1}{q_k^2}.
    $$

??? note "Dokaz"
    Budući da je $x=[a_0,a_1,\ldots,a_k,r_{k+1}]$ i da formula za razliku konvergenti vrijedi i za formalne verižne razlomke, imamo
    
    $$
    x-x_k = \dfrac{(-1)^k}{q_k\left(r_{k+1}q_k+q_{k-1}\right)},
    $$
    
    gdje je $r_{k+1}q_k+q_{k-1}$ upravo nazivnik $k+1$-ve konvergente tog formalnog verižnog razlomka dobiven rekurzivnom formulom.
    
    Da bismo dovršili procjenu nejednakostima, dovoljno je uočiti da za $x_k\neq x$ uvijek vrijedi
    
    $$
    1\le a_{k+1}\le r_{k+1} \le a_{k+1}+1,
    $$
    
    pa je
    
    $$
    q_{k+1}=a_{k+1}q_k+q_{k-1}\le r_{k+1}q_k+q_{k-1} \le q_k+(a_{k+1}q_k+q_{k-1}) = q_k+q_{k+1}.
    $$
    
    Odatle slijedi nejednakost
    
    $$
    \dfrac{1}{q_k(q_k+q_{k+1})} \le \left|x-\frac{p_k}{q_k}\right| = \dfrac{1}{q_k\left(r_{k+1}q_k+q_{k-1}\right)} \le \dfrac{1}{q_kq_{k+1}}.
    $$
    
    Za vanjske ocjene dovoljno je još primijetiti da je $q_k\le q_{k+1}$.

Formula za razliku iz ovog odjeljka ima još jednu jednostavnu posljedicu: konvergente $\dfrac{p_k}{q_k}$ uvijek su neskrativi razlomci.

???+ note "Korolar"
    Za svaki realan broj $x$, ako su brojnik i nazivnik konvergente $x_k=\dfrac{p_k}{q_k}$ zadani rekurzivnom formulom, $\dfrac{p_k}{q_k}$ je neskrativ razlomak, tj. $\gcd(p_k,q_k)=1$.

??? note "Dokaz"
    Dovoljno je na formulu za razliku primijeniti [Bézoutov teorem](./bezouts.md).

Zapravo se i rješenja linearne diofantske jednadžbe s dvije nepoznanice mogu dobiti metodom verižnih razlomaka.

???+ example "Rješavanje linearne diofantske jednadžbe s dvije nepoznanice"
    Zadani su $A, B, C \in \mathbf Z$. Pronađite $x, y \in \mathbf Z$ takve da vrijedi $Ax + By = C$.

??? note "Rješenje"
    Iako se taj problem obično rješava [proširenim Euklidovim algoritmom](./bezouts.md#两个变量的情形), jednako se može riješiti i verižnim razlomcima.
    
    Neka je $\dfrac{A}{B}=[a_0, a_1, \ldots, a_k]$. Gore je dokazano $p_k q_{k-1} - p_{k-1} q_k = (-1)^{k-1}$. Zamijenimo li $p_k$ i $q_k$ s $A$ i $B$, dobivamo
    
    $$
    Aq_{k-1} - Bp_{k-1} = (-1)^{k-1} g,
    $$
    
    gdje je $g = \gcd(A, B)$. Ako $g$ dijeli $C$, jedno je rješenje $x = (-1)^{k-1}\dfrac{C}{g} q_{k-1}$ i $y = (-1)^{k}\dfrac{C}{g} p_{k-1}$; inače rješenja nema.
    
    === "C++"
        ```cpp
        --8<-- "docs/math/code/continued-fraction/diophantine.cpp:dio"
        ```
    
    === "Python"
        ```py
        --8<-- "docs/math/code/continued-fraction/diophantine.py:dio"
        ```

## Diofantska aproksimacija

Važna primjena teorije verižnih razlomaka jest teorija diofantske aproksimacije. Diofantska aproksimacija (Diophantine approximation) označava aproksimiranje realnih brojeva racionalnima. Dakako, zbog gustoće racionalnih brojeva, bez ikakvih ograničenja mogu se dobiti aproksimacije s proizvoljno malom pogreškom. Zato je potrebno ograničiti racionalne brojeve koji se smiju upotrijebiti, primjerice dopustiti samo racionalne brojeve s nazivnikom manjim od neke vrijednosti. U ovom se odjeljku razmatra veza između najboljih aproksimacija uz takvo ograničenje i verižnih razlomaka.

### Aproksimacija realnih brojeva konvergentama

Najprije, iz procjene pogreške konvergenti odmah slijedi sljedeći rezultat:

???+ note "Teorem (Dirichlet)"
    Za iracionalan broj $x$ postoji beskonačno mnogo neskrativih razlomaka $\dfrac{p}{q}$ za koje vrijedi
    
    $$
    \left|x-\dfrac{p}{q}\right| < \dfrac{1}{q^2} 
    $$

??? note "Dokaz"
    Prema procjeni pogreške konvergenti, za $k$-tu konvergentu $x_k=\dfrac{p_k}{q_k}$ iracionalnog broja $x$ vrijedi
    
    $$
    \left|x-\dfrac{p_k}{q_k}\right|\le\frac{1}{q_k^2}.
    $$
    
    Pregledom dokaza formule za pogrešku vidi se da za iracionalan broj $x$ jednakost nikad ne nastupa. Stoga brojnici i nazivnici svih njegovih konvergenti zadovoljavaju traženi uvjet.

Taj se teorem može smatrati i posljedicom [Dirichletova teorema o aproksimaciji](https://en.wikipedia.org/wiki/Dirichlet%27s_approximation_theorem). To je gotovo najbolji mogući rezultat. Eksponent $2$ u nazivniku na desnoj strani nejednakosti ne može se više poboljšati, ali konstanta može. Hurwitzov teorem kaže da se desna strana nejednakosti može smanjiti na $\dfrac{1}{\sqrt{5}q^2}$ i da je to najbolja moguća granica.

???+ note "Hurwitzov teorem"
    Za iracionalan broj $x$ postoji beskonačno mnogo neskrativih razlomaka $\dfrac{p}{q}$ za koje vrijedi
    
    $$
    \left|x-\dfrac{p}{q}\right| < \dfrac{1}{\sqrt{5}q^2} 
    $$
    
    i pritom se $\sqrt{5}$ na desnoj strani nejednakosti ne može zamijeniti većim realnim brojem.

??? note "Dokaz (Borel)"
    Borel je zapravo dokazao da među svake tri uzastopne konvergente iracionalnog broja $x$ barem jedna zadovoljava gornji uvjet. Budući da konvergenti ima beskonačno mnogo i sve su neskrativi razlomci, prvi dio Hurwitzova teorema nužno vrijedi.
    
    Dokazujemo kontradikcijom. Pretpostavimo da postoje iracionalan broj $x$ i njegove konvergente $x_{k-1},x_k,x_{k+1}$ takve da vrijedi
    
    $$
    \left|x-\dfrac{p_{k-1}}{q_{k-1}}\right|\ge\dfrac{1}{\sqrt{5}q_{k-1}^2},\ 
    \left|x-\dfrac{p_{k}}{q_{k}}\right|\ge\dfrac{1}{\sqrt{5}q_{k}^2},\ 
    \left|x-\dfrac{p_{k+1}}{q_{k+1}}\right|\ge\dfrac{1}{\sqrt{5}q_{k+1}^2}
    $$
    
    Budući da susjedne konvergente nužno leže s različitih strana od $x$, iz formule za razliku slijedi
    
    $$
    \dfrac{1}{q_{k-1}q_{k}}=\left|\dfrac{p_{k-1}}{q_{k-1}}-\dfrac{p_{k}}{q_{k}}\right|=\left|x-\dfrac{p_{k-1}}{q_{k-1}}\right|+\left|x-\dfrac{p_{k}}{q_{k}}\right|\ge\dfrac{1}{\sqrt{5}q_{k-1}^2}+\dfrac{1}{\sqrt{5}q_{k}^2}.
    $$
    
    To se može zapisati kao nejednakost za kvocijent $\dfrac{q_{k}}{q_{k-1}}$:
    
    $$
    \dfrac{q_k}{q_{k-1}}+\dfrac{q_{k-1}}{q_k}\le\sqrt 5.
    $$
    
    Budući da je lijeva strana racionalna, a desna iracionalna, jednakost se ne može postići. Kako je još $q_k\ge q_{k-1}$, rješavanjem dobivamo
    
    $$
    1\le \dfrac{q_{k}}{q_{k-1}} < \dfrac{\sqrt{5}+1}{2}.
    $$
    
    Analogno se dokazuje
    
    $$
    1\le \dfrac{q_{k+1}}{q_{k}} < \dfrac{\sqrt{5}+1}{2}.
    $$
    
    No prema rekurzivnoj formuli i kombiniranjem tih dviju nejednakosti slijedi
    
    $$
    a_{k+1} = \frac{q_{k+1}}{q_k}-\frac{q_{k-1}}{q_k} < \dfrac{\sqrt{5}+1}{2}-\dfrac{\sqrt{5}-1}{2} = 1
    $$
    
    što je u suprotnosti s definicijom jednostavnog verižnog razlomka. Dakle, Borelova tvrdnja vrijedi.
    
    Da bismo pokazali da je tako dobivena granica najbolja, dovoljno je pronaći $x$ takav da za svaki $C>\sqrt{5}$ postoji samo konačno mnogo neskrativih razlomaka $\dfrac{p}{q}$ koji zadovoljavaju nejednakost
    
    $$
    \left|x-\dfrac{p}{q}\right| < \dfrac{1}{Cq^2} 
    $$
    
    U nastavku dokazujemo da je $\phi=\dfrac{\sqrt{5}+1}{2}$ takav $x$.[^sqrt5]
    
    Neka je $\phi'=\dfrac{-\sqrt{5}+1}{2}$ konjugirani korijen od $\phi$. Oba su korijeni jednadžbe $x^2-x-1=0$. Stoga za svaki realan $x$ vrijedi
    
    $$
    x^2-x-1 = (x-\phi)(x-\phi').
    $$
    
    Uvrštavanjem neskrativog razlomka $\dfrac{p}{q}$ dobivamo
    
    $$
    \dfrac{1}{q^2}\le\frac{|p^2-pq-q^2|}{q^2}=\left|\dfrac{p}{q}-\phi\right|\left|\dfrac{p}{q}-\phi'\right|\le\left|\dfrac{p}{q}-\phi\right|\left(\left|\dfrac{p}{q}-\phi\right|+|\phi-\phi'|\right)<\dfrac{1}{Cq^2}\left(\dfrac{1}{Cq^2}+\sqrt{5}\right).
    $$
    
    Za $C>\sqrt{5}$ odatle se izravno dobiva $q<\dfrac{1}{\sqrt{C(C-\sqrt{5})}}$, pa ne može postojati beskonačno mnogo rješenja gornje nejednakosti.

Dokazi tih teorema pokazuju da konvergente daju vrlo dobre diofantske aproksimacije. No to ne moraju biti najbolje aproksimacije. Da bismo govorili o najboljim aproksimacijama, moramo precizirati mjeru kvalitete aproksimacije. Za to obično postoje dva izbora.

???+ warning "Mogući slučajevi u kojima tvrdnje o najboljim aproksimacijama ne vrijede"
    U sljedeća dva odjeljka iznose se rezultati o najboljim aproksimacijama. Ti rezultati možda ne vrijede u pojedinim nezanimljivim slučajevima. Na primjer, obje definicije najbolje aproksimacije zahtijevaju strogu nejednakost, ali za polucijeli broj $x=n+\dfrac12$, $n\in\mathbf Z$, njegov verižni razlomak može imati oblik $[n,1,1]$. Tada njegove prve dvije konvergente $x_0=n$ i $x_1=n+1$ imaju nazivnik $1$ i jednako su udaljene od $x$. To znači da nijedna od njih nije najbolja aproksimacija. Pri čitanju tvrdnji u ovom odjeljku čitatelj treba podrazumijevati da su takvi slučajevi isključeni. Ako čitatelja ne zanima posljednjih nekoliko konvergenti ili ga zanima samo aproksimacija iracionalnih brojeva, na te dodatne komplikacije ne mora obraćati pozornost.

### Najbolja aproksimacija prve vrste: međurazlomci

Najbolja aproksimacija prve vrste kvalitetu aproksimacije mjeri veličinom

$$
\left|x-\dfrac{p}{q}\right|
$$

???+ abstract "Najbolja aproksimacija prve vrste"
    Za realan broj $x$ i racionalan broj $\dfrac{p}{q}$: ako za svaki $\dfrac{p'}{q'}\neq \dfrac{p}{q}$ s $0<q'\le q$ vrijedi
    
    $$
    \left|x-\dfrac{p}{q}\right|<\left|x-\dfrac{p'}{q'}\right|,
    $$
    
    racionalan broj $\dfrac{p}{q}$ naziva se **najbolja aproksimacija prve vrste** (best approximation of the first kind) realnog broja $x$.

Najbolja aproksimacija prve vrste ne mora biti konvergenta; riječ je o široj klasi razlomaka.

???+ abstract "Međurazlomak"
    Neka realan broj $x$ ima konvergentu $x_{k+1}=[a_0,a_1,\ldots,a_k,a_{k+1}]$ i neka je $t$ cijeli broj takav da je $0\le t\le a_{k+1}$[^semi-range]. Tada se razlomak $x_{k,t}=[a_0,a_1,\ldots,a_{k},t]$ naziva **međurazlomak** (intermediate fraction), **polukonvergenta** (semiconvergent) ili **sekundarna konvergenta** (secondary convergent) broja $x$.[^semiconvergent]
    
    Slično kao kod konvergenti, međurazlomak veći (manji) od $x$ naziva se **gornji (donji) međurazlomak** (upper (lower) semiconvergent).

Prema rekurzivnoj formuli međurazlomak se može zapisati kao

$$
x_{k,t} = \frac{tp_{k}+p_{k-1}}{tq_{k}+q_{k-1}}.
$$

On je nužno neskrativ razlomak i leži između konvergenti $x_{k-1}$ i $x_{k+1}$. S porastom $t$ postupno se približava $x_{k+1}$ (na primjeru parnog $k$):

$$
x_{k-1} = x_{k,0} < x_{k,1} < x_{k,2} < \cdots < x_{k,a_{k+1}} = x_{k+1}.
$$

Budući da brojnici i nazivnici konvergenti rastu, brojnik i nazivnik međurazlomka $x_{k,t}$ ($t\neq 0$) leže između onih od $x_{k}$ i $x_{k+1}$. Poredamo li te razlomke po veličini nazivnika, međurazlomci su upravo razlomci koji se nalaze između susjednih konvergenti.

Sve najbolje aproksimacije prve vrste međurazlomci su, ali nisu svi međurazlomci najbolje aproksimacije prve vrste.

???+ note "Teorem"
    Sve najbolje aproksimacije prve vrste međurazlomci su.

??? note "Dokaz"
    Budući da je $a_0\le x\le a_0+1$, najbolja aproksimacija prve vrste nužno leži između $x_{1,0}=a_0$ i $x_{0,1}=a_0+1$. Svi se međurazlomci od najmanjeg prema najvećem mogu poredati ovako:
    
    $$
    x_{1,0}<x_{1,1}< \cdots < x_{1,a_2}=x_{3,0}<\cdots<x<\cdots<x_{2,0}=x_{0,a_1}<\cdots<x_{0,1}.
    $$
    
    Međurazlomci istog reda pojavljuju se uzastopno, a između međurazlomaka različitih redova nema praznina. To znači da svaki racionalan broj $\dfrac{p}{q}$ između $x_{1,0}=a_0$ i $x_{0,1}=a_0+1$ nužno pada između dvaju međurazlomaka istog reda $x_{k,t}$ i $x_{k,t+1}$. Bez smanjenja općenitosti pretpostavimo da on nije međurazlomak i da je manji od $x$, pa vrijedi
    
    $$
    x_{k,t}<\dfrac{p}{q}<x_{k,t+1}<x.
    $$
    
    Tada s jedne strane imamo
    
    $$
    \left|x_{k,t}-\dfrac{p}{q}\right| < \left|x_{k,t}-x_{k,t+1}\right| = \dfrac{1}{((t+1)q_k+q_{k-1})(tq_k+q_{k-1})}.
    $$
    
    S druge strane vrijedi
    
    $$
    \left|x_{k,t}-\dfrac{p}{q}\right| = \dfrac{|q(tp_k+p_{k-1})-p(tq_k+q_{k-1})|}{q(tq_k+q_{k-1})}\ge\dfrac{1}{q(tq_k+q_{k-1})}.
    $$
    
    Stoga nužno vrijedi
    
    $$
    q>(t+1)q_k+q_{k-1}.
    $$
    
    Drugim riječima, nazivnik racionalnog broja $\dfrac{p}{q}$ sigurno je veći od nazivnika od $x_{k,t+1}$, ali on nije bolja aproksimacija:
    
    $$
    \left|x-\dfrac{p}{q}\right|>\left|x-x_{k,t+1}\right|
    $$
    
    Stoga ne može biti najbolja aproksimacija prve vrste. To pokazuje da ono što nije međurazlomak nije ni najbolja aproksimacija prve vrste; dakle, sve su najbolje aproksimacije prve vrste međurazlomci.

Obratno, ne može se tvrditi da su svi međurazlomci najbolje aproksimacije prve vrste. Ipak, može se dati uvjet pod kojim međurazlomak jest najbolja aproksimacija prve vrste.

???+ note "Teorem"
    Sve su konvergente najbolje aproksimacije prve vrste. Osim toga, neka je $0<t<a_{k+1}$; tada je međurazlomak $x_{k,t}$ najbolja aproksimacija prve vrste ako i samo ako je $t>\dfrac{a_{k+1}}{2}$ ili je $t=\dfrac{a_{k+1}}{2}$ i $r_{k+2}>\dfrac{q_k}{q_{k-1}}$.

??? note "Dokaz"
    U nastavku će se dokazati da su sve konvergente najbolje aproksimacije druge vrste, pa su stoga nužno i najbolje aproksimacije prve vrste. Ključni su međurazlomci koji nisu konvergente.
    
    Već je rečeno da nazivnik međurazlomka $x_{k,t}$ leži između nazivnika od $x_k$ i $x_{k+1}$ i raste s porastom $t$, dok se $x_{k,t}$ pritom približava $x_{k+1}$, a time i $x$. Na primjeru $x_{k,t}<x$, njegov međusobni položaj sa susjednim međurazlomcima zadovoljava:
    
    $$
    x_{k-1} < x_{k,t} < x_{k+1} < x < x_{k}.
    $$
    
    Budući da je nazivnik od $x_k$ manji od nazivnika od $x_{k,t}$, nužan uvjet da $x_{k,t}$ bude najbolja aproksimacija prve vrste jest da je bliži $x$ nego $x_k$. To je ujedno i dovoljan uvjet: kao konvergenta, $x_k$ nema konkurenta s manjim nazivnikom a manjom udaljenošću, dok su međurazlomci s nazivnikom većim od nazivnika od $x_k$ nužno istog reda kao $x_{k,t}$, ali s manjim nazivnikom, pa su nužno udaljeniji od $x$. Za pogreške konvergente i međurazlomka računom se dobiva
    
    $$
    \begin{aligned}
    \left|x_k-x\right| &= \dfrac{1}{q_k(r_{k+1}q_k+q_{k-1})},\\
    \left|x_{k,t}-x\right| &= \left|\dfrac{tp_{k}+p_{k-1}}{tq_{k}+q_{k-1}}-\dfrac{r_{k+1}p_{k}+p_{k-1}}{r_{k+1}q_{k}+q_{k-1}}\right| \\
    &=\dfrac{r_{k+1}-t}{(tq_{k}+q_{k-1})(r_{k+1}q_{k}+q_{k-1})}.
    \end{aligned}
    $$
    
    Pritom je iskorišteno $r_{k+1}\ge a_{k+1}>t$. Stoga je $x_{k,t}$ bliži $x$ nego $x_k$, odnosno najbolja aproksimacija prve vrste, ako i samo ako
    
    $$
    \dfrac{r_{k+1}-t}{tq_{k}+q_{k-1}}<\dfrac{1}{q_k} \iff r_{k+1}<2t+\dfrac{q_{k-1}}{q_k}.
    $$
    
    Tada postoje tri moguća slučaja:
    
    1.  Ako je $t<\dfrac{a_{k+1}}{2}$, tada je $2t<a_{k+1}$. Budući da su obje strane cijeli brojevi, vrijedi $2t\le a_{k+1}-1$, pa je $2t+\dfrac{q_{k-1}}{q_k}\le 2t+1\le a_{k+1}\le r_{k+1}$. Tada $x_{k,t}$ nije najbolja aproksimacija prve vrste;
    2.  Ako je $t>\dfrac{a_{k+1}}{2}$, tada je $2t>a_{k+1}$. Budući da su obje strane cijeli brojevi, vrijedi $2t\ge a_{k+1}+1>r_{k+1}$. Tada $x_{k,t}$ jest najbolja aproksimacija prve vrste;
    3.  Ako je $a_{k+1}$ paran, postoji i treći slučaj, $t=\dfrac{a_{k+1}}{2}$. Gornji je uvjet tada ekvivalentan s $\dfrac{1}{r_{k+2}}=r_{k+1}-a_{k+1}<\dfrac{q_{k-1}}{q_k}$, odnosno s $r_{k+2}>\dfrac{q_k}{q_{k-1}}$.

Prema tome, poredamo li sve najbolje aproksimacije prve vrste realnog broja $x$ po veličini nazivnika od najmanjeg prema najvećem, one se prema odnosu veličine prema $x$ dijele na nekoliko segmenata. Svaki se segment uvijek sastoji od nekoliko (moguće i nijednog) uzastopnih međurazlomaka istog reda i uvijek završava konvergentom. Unutar segmenta svi su s iste strane realnog broja $x$, a segmenti se izmjenjuju s obiju strana od $x$.

??? example "Primjer: najbolje aproksimacije prve vrste broja $\pi$"
    Broj $\pi=[3,7,15,1,292,\ldots]$, pa je njegovih prvih 15 najboljih aproksimacija prve vrste s najmanjim nazivnicima:
    
    $$
    \begin{aligned}
    &x_0 = \dfrac{3}{1},\
    x_{0,4} = \dfrac{13}{4},\
    x_{0,5} = \dfrac{16}{5},\
    x_{0,6} = \dfrac{19}{6},\
    x_1 = \dfrac{22}{7},\\
    &x_{1,8} = \dfrac{179}{57},\
    x_{1,9} = \dfrac{201}{64},\
    x_{1,10} = \dfrac{223}{71},\
    x_{1,11} = \dfrac{245}{78},\
    x_{1,12} = \dfrac{267}{85},\\
    &x_{1,13} = \dfrac{289}{92},\ 
    x_{1,14} = \dfrac{311}{99},\
    x_2 = \dfrac{333}{106},\
    x_3 = \dfrac{355}{113},\
    x_{3,146} = \dfrac{52163}{16604}.
    \end{aligned}
    $$

### Najbolja aproksimacija druge vrste

Najbolja aproksimacija druge vrste kvalitetu aproksimacije mjeri veličinom $|qx-p|$.

???+ abstract "Najbolja aproksimacija druge vrste"
    Za realan broj $x$ i racionalan broj $\dfrac{p}{q}$: ako za svaki $\dfrac{p'}{q'}\neq \dfrac{p}{q}$ s $0<q'\le q$ vrijedi
    
    $$
    \left|qx-p\right|<\left|q'x-p'\right|,
    $$
    
    racionalan broj $\dfrac{p}{q}$ naziva se **najbolja aproksimacija druge vrste** (best approximation of the second kind) realnog broja $x$.

Uvjet najbolje aproksimacije druge vrste ekvivalentan je s

$$
\left|x-\dfrac{p}{q}\right|<\dfrac{q'}{q}\left|x-\dfrac{p'}{q'}\right|.
$$

Budući da je $q'\le q$, uvjet najbolje aproksimacije druge vrste stroži je od uvjeta najbolje aproksimacije prve vrste.

Najbolje aproksimacije druge vrste mogu biti samo konvergente i upravo su one.

???+ note "Teorem"
    Sve najbolje aproksimacije druge vrste nužno su konvergente, a sve su konvergente nužno najbolje aproksimacije druge vrste.

??? note "Dokaz"
    Za dokaz prvog dijela, budući da je najbolja aproksimacija druge vrste ujedno i najbolja aproksimacija prve vrste, dovoljno je dokazati da međurazlomak koji nije konvergenta ne može biti najbolja aproksimacija druge vrste. U tu svrhu neka je $x_{k,t}=\dfrac{p}{q}$ međurazlomak koji nije konvergenta; uz $x_{k,t}<x$ vrijedi
    
    $$
    x_{k-1} < x_{k,t} < x_{k+1} < x < x_{k}.
    $$
    
    Budući da je pogreška između $x_{k,t}$ i $x$
    
    $$
    |x_{k,t}-x|\ge |x_{k,t}-x_{k+1}|=\left|\dfrac{p}{q}-\dfrac{p_{k+1}}{q_{k+1}}\right|=\dfrac{|pq_{k+1}-p_{k+1}q|}{qq_{k+1}}\ge\dfrac{1}{qq_{k+1}},
    $$
    
    primjenom procjene pogreške konvergenti uvijek vrijedi
    
    $$
    |qx_{k,t}-p| \ge \dfrac{1}{q_{k+1}} \ge |q_kx_k-p_k|,
    $$
    
    tj. $x_{k,t}$ ne aproksimira bolje od $x_k$, koji ima manji nazivnik, pa ne može biti najbolja aproksimacija druge vrste.
    
    Obratno, za dokaz drugog dijela treba pokazati da je svaka konvergenta $x_k=\dfrac{p_k}{q_k}$ najbolja aproksimacija druge vrste. Dakle, treba pokazati da za sve razlomke $\dfrac{p}{q}$ s $q\le q_k$ vrijedi $|q_kx-p_k|<|qx-p|$. Ne razmatrajući slučaj polucijelih brojeva, možemo pretpostaviti $k>0$. Najprije, prema procjeni pogreške aproksimacije realnog broja konvergentama, vrijedi
    
    $$
    |q_{k-1} x-p_{k-1}| \ge \frac{1}{q_{k-1}+q_{k}} \ge \dfrac{1}{q_{k+1}}\ge |q_kx-p_k|.
    $$
    
    Jednakost vrijedi u svim nejednakostima ako i samo ako je $a_{k+1}=1$ i to je posljednji član verižnog razlomka. Ne razmatrajući takav slučaj, $x_{k-1}=\dfrac{p_{k-1}}{q_{k-1}}$ strogo je lošiji od $x_k=\dfrac{p_k}{q_k}$.
    
    Uzmimo proizvoljan razlomak $\dfrac{p}{q}\neq x_k$ s $0<q\le q_k$. Budući da vrijedi formula za razliku $p_{k}q_{k-1} - p_{k-1}q_{k} = (-1)^{k-1}$, prema Cramerovu pravilu sustav linearnih jednadžbi
    
    $$
    \begin{cases}
    \lambda p_k+\mu p_{k-1} = p,\\
    \lambda q_k+\mu q_{k-1} = q
    \end{cases}
    $$
    
    nužno ima jedinstveno cjelobrojno rješenje $(\lambda,\mu)$. Ako je $\lambda\mu>0$, tada je $q>|\lambda|q_k\ge q_k$, što je kontradikcija. Inače je $\lambda\mu\le 0$, tj. $\lambda$ i $\mu$ suprotnih su predznaka; kako su i $q_{k-1}x-p_{k-1}$ i $q_kx-p_k$ suprotnih predznaka, $\lambda(q_{k-1}x-p_{k-1})$ i $\mu(q_kx-p_k)$ istog su predznaka, pa je
    
    $$
    |qx-p|=|\lambda||q_kx-p_k|+|\mu||q_{k-1}x-p_{k-1}|>|q_{k}x-p_{k}|.
    $$
    
    Posljednja je nejednakost stroga jer je $x_{k-1}$ strogo lošiji od $x_k$ i $\dfrac{p}{q}\neq x_k$. To pokazuje da je $x_k$ najbolja aproksimacija druge vrste.

To svojstvo pokazuje da su konvergente doista vrlo dobre diofantske aproksimacije.

### Prepoznavanje konvergenti

Najbolja aproksimacija druge vrste daje nužan i dovoljan uvjet za to je li neki razlomak konvergenta. To znači da se provjerom relativne kvalitete aproksimacije može utvrditi je li razlomak konvergenta. Legendreov kriterij daje način prepoznavanja konvergenti prema apsolutnoj kvaliteti aproksimacije. Izvorna formulacija Legendreova kriterija daje nužan i dovoljan uvjet, ali njezin oblik nije praktičan. U ovom se odjeljku daje pojednostavljena verzija Legendreova kriterija i pokazuje da ona ne propušta previše konvergenti.

???+ note "Teorem (Legendre)"
    Za realan broj $x$ i razlomak $\dfrac{p}{q}$: ako vrijedi
    
    $$
    \left|x-\dfrac{p}{q}\right|<\dfrac{1}{2q^2}
    $$
    
    tada je $\dfrac{p}{q}$ nužno konvergenta broja $x$.

??? note "Dokaz"
    Neka su $\epsilon\in\{-1,1\}$ i $\theta\in(0,1/2)$ konstante za koje vrijedi
    
    $$
    x-\dfrac{p}{q} = \dfrac{\epsilon\theta}{q^2}
    $$
    
    Razvijmo racionalan broj $\dfrac{p}{q}$ u verižni razlomak $[a_0,a_1,\ldots,a_n]$. Racionalan broj ima dva prikaza verižnim razlomkom čiji se $n$ razlikuju točno za jedan, pa možemo odabrati prikaz takav da je $(-1)^n=\epsilon$; konvergente tog prikaza označimo s $\dfrac{p_k}{q_k}$. Neka realan broj $\omega$ zadovoljava
    
    $$
    x = \dfrac{\omega p_n+p_{n-1}}{\omega q_n+q_{n-1}}.
    $$
    
    Tada nužno vrijedi
    
    $$
    \dfrac{\epsilon\theta}{q^2} = x-\dfrac{p}{q} = x-\dfrac{p_n}{q_n} = \dfrac{p_{n-1}q_n-p_nq_{n-1}}{(\omega q_n+q_{n-1})q_n} = \dfrac{(-1)^n}{(\omega q_n+q_{n-1})q_n}.
    $$
    
    Stoga je
    
    $$
    \theta = \dfrac{q_n}{\omega q_n+q_{n-1}}.
    $$
    
    To pokazuje da je
    
    $$
    \omega=\dfrac{1}{\theta}-\dfrac{q_{n-1}}{q_n}>1.
    $$
    
    Razvijemo li i $\omega$ u verižni razlomak $[b_0,b_1,\ldots]$, dobivamo
    
    $$
    x = \dfrac{\omega p_n+p_{n-1}}{\omega q_n+q_{n-1}} = [a_0,a_1,\ldots,a_n,\omega] = [a_0,a_1,\ldots,a_n,b_0,b_1,\ldots].
    $$
    
    To je valjan jednostavni verižni razlomak, pa je $\dfrac{p}{q}$ konvergenta broja $x$.
    
    Taj dokaz zapravo pokazuje da je nužan i dovoljan uvjet da $\dfrac{p}{q}$ bude konvergenta upravo $\omega>1$ iz gornjeg dokaza; to je izvorni oblik Legendreova kriterija.

Taj kriterij pokazuje da je razlomak sigurno konvergenta čim je aproksimacija dovoljno dobra. Sljedeći teorem pokazuje da je tako dobrih konvergenti dovoljno mnogo: barem polovica konvergenti zadovoljava taj uvjet.

???+ note "Teorem (Vahlen)"
    Od dviju susjednih konvergenti realnog broja $x$ barem jedna zadovoljava
    
    $$
    \left|x-\dfrac{p}{q}\right|<\dfrac{1}{2q^2}.
    $$

??? note "Dokaz"
    Pretpostavimo suprotno. Postoji realan broj $x$ s dvjema susjednim konvergentama $x_k$ i $x_{k+1}$ takvima da je
    
    $$
    \left|x-\dfrac{p_k}{q_k}\right|\ge \dfrac{1}{2q_{k}^2},\ \left|x-\dfrac{p_{k+1}}{q_{k+1}}\right|\ge \dfrac{1}{2q_{k+1}^2}.
    $$
    
    Budući da $x$ leži između $x_k$ i $x_{k+1}$, vrijedi
    
    $$
    \dfrac{1}{2q_{k}^2} + \dfrac{1}{2q_{k+1}^2} \le \left|x-\dfrac{p_k}{q_k}\right| + \left|x-\dfrac{p_{k+1}}{q_{k+1}}\right| = \left|\dfrac{p_k}{q_k}-\dfrac{p_{k+1}}{q_{k+1}}\right| = \dfrac{1}{q_kq_{k+1}}.
    $$
    
    To pokazuje da je $q_k=q_{k+1}$. Stoga nužno vrijedi $k=0$ i $a_1=1$. Tada su prve dvije konvergente $x_0=a_0$ i $x_1=a_0+1$. Dakle, jedini su protuprimjeri tvrdnji polucijeli brojevi, a prema ranijoj napomeni taj se slučaj u ovom članku ne razmatra.

## Geometrijska interpretacija

Teorija verižnih razlomaka ima lijepu geometrijsku interpretaciju.

![](./images/continued-convergents-geometry.svg)

Kao na slici, za realan broj $\xi>0$ pravac $y=\xi x$ dijeli cjelobrojne točke (lattice points) prvog kvadranta (uključujući točke na koordinatnim osima $x$ i $y$, ali bez ishodišta; isto vrijedi u nastavku) na gornji i donji dio. Za racionalan $\xi$ točke na pravcu $y=\xi x$ ubrajaju se i u točke iznad pravca i u točke ispod pravca. Promotrimo konveksne ljuske tih dvaju skupova točaka. Tada su konvergente s neparnim indeksom vrhovi konveksne ljuske gornjeg dijela, a konvergente s parnim indeksom vrhovi konveksne ljuske donjeg dijela. Cjelobrojne točke na spojnici dvaju susjednih vrhova konveksne ljuske upravo su međurazlomci. Na slici su prikazane konvergente i međurazlomci (sive točke) za $\xi=\dfrac{9}{7}$.

Većina prethodnih zaključaka o verižnim razlomcima ima odgovarajuću geometrijsku interpretaciju:

??? note "Geometrijska interpretacija"
    -   Svakom razlomku $\nu=\dfrac{p}{q}$ odgovara cjelobrojna točka $\vec\nu=(q,p)$ u prvom kvadrantu, a veličini razlomka odgovara nagib spojnice s ishodištem.
    -   Vektor smjera pravca $y=\xi x$ jest $\vec\xi=(1,\xi)$. Pomoću pojma [vektorskog produkta](../linear-algebra/product.md#二维向量的情形) $(x_1,y_1)\times(x_2,y_2)=x_1y_2-x_2y_1$ po predznaku od $\vec\xi\times\vec\nu=p-q\xi$ može se odrediti leži li točka iznad ili ispod pravca. Stoga točkama iznad pravca odgovaraju razlomci veći ili jednaki $\xi$, a točkama ispod pravca razlomci manji ili jednaki $\xi$. Apsolutna vrijednost produkta $|\vec\xi\times\vec\nu|$ proporcionalna je udaljenosti točke $\vec\nu$ od pravca $y=\xi x$
    
        $$
        \dfrac{|p-q\xi|}{\sqrt{1+\xi^2}},
        $$
    
        što odgovara kvaliteti aproksimacije realnog broja $\xi$ razlomkom $\nu$.
    -   Označimo li točku koja odgovara konvergenti $\xi_k=\dfrac{p_k}{q_k}$ s $\vec\xi_k=(q_k,p_k)$, rekurzivna se formula može zapisati kao
    
        $$
        \vec\xi_k = a_k\vec\xi_{k-1} + \vec\xi_{k-2}.
        $$
    
        Početak rekurzije čine $\vec\xi_{-2} = (1,0)$ i $\vec\xi_{-1} = (0,1)$.
    -   Za cijeli broj $t$ takav da je $0\le t\le a_k$ točka
    
        $$
        \vec\xi_{k-1,t} = t\vec\xi_{k-1} + \vec\xi_{k-2}
        $$
    
        leži na dužini koja spaja točke $\vec\xi_{k-2}$ i $\vec\xi_k$. Te točke odgovaraju međurazlomcima $\xi_{k-1,t}$.
    -   Geometrijskom se metodom mogu konstruirati sve konvergente i međurazlomci. Krenimo od točaka $\vec\xi_{-2}=(1,0)$ i $\vec\xi_{-1}=(0,1)$; one leže s različitih strana pravca $y=\xi x$, što znači da $\vec\xi\times\vec\xi_{-2}$ i $\vec\xi\times\vec\xi_{-1}$ imaju suprotne predznake. Dodajemo $\vec\xi_{-1}$ zbrajanjem vektora na $\vec\xi_{-2}$ sve dok daljnje dodavanje ne bi prešlo pravac $y=\xi x$; rezultat označimo s $\vec\xi_0$, koji je i dalje s druge strane od $\vec\xi_{-1}$. Zatim dodajemo $\vec\xi_0$ na $\vec\xi_{-1}$ sve dok daljnje dodavanje ne bi prešlo pravac $y=\xi x$; rezultat označimo s $\vec\xi_1$, koji je i dalje s druge strane od $\vec\xi_0$. Taj se postupak može nastaviti u beskonačnost, osim ako u konačno mnogo koraka neki $\vec\xi_n$ padne točno na pravac $y=\xi x$. Potonje znači da su vektori $\vec\xi$ i $\vec\xi_n$ kolinearni, tj. $\xi=\dfrac{p_n}{q_n}$ racionalna je točka. Tim se postupkom dobiva slika s prethodnog crteža. Boris Delaunay slikovito je nazvao taj postupak algoritmom istezanja nosa (nose-stretching algorithm)[^nose-stretching].
    -   Ako je potrebno brzo izračunati koliko se puta u svakom koraku $\vec\xi_{k-1}$ dodaje na $\vec\xi_{k-2}$, može se iskoristiti vektorski produkt. Budući da $\vec\xi\times\vec\xi_{k-1}$ i $\vec\xi\times\vec\xi_{k-2}$ imaju suprotne predznake, ako s $\vec\xi_{k-1,t}=t\vec\xi_{k-1}+\vec\xi_{k-2}$ označimo rezultat $t$-strukog dodavanja $\vec\xi_{k-1}$ na $\vec\xi_{k-2}$, tada $\vec\xi\times\vec\xi_{k-1,t}=t(\vec\xi\times\vec\xi_{k-1})+(\vec\xi\times\vec\xi_{k-2})$ ne mijenja predznak upravo kad pravac nije prijeđen. Prije promjene predznaka apsolutna vrijednost $\vec\xi\times\vec\xi_{k-1,t}$ postupno pada. Označimo
    
        $$
        r_{k} = \left|\dfrac{\vec\xi\times\vec\xi_{k-2}}{\vec\xi\times\vec\xi_{k-1}}\right| = -\dfrac{\vec\xi\times\vec\xi_{k-2}}{\vec\xi\times\vec\xi_{k-1}}.
        $$
    
        Tada je najveći mogući broj koraka pada
    
        $$
        a_{k} = \lfloor r_{k}\rfloor = \left\lfloor\left|\dfrac{q_{k-1}\xi-p_{k-1}}{q_{k-2}\xi-p_{k-2}}\right|\right\rfloor.
        $$
    
        To je upravo $k$-ti član razvoja u verižni razlomak. Štoviše, $r_k$ upravo je ostatak razvoja u verižni razlomak i zadovoljava relaciju:
    
        $$
        r_k = -\dfrac{q_{k-1}\xi-p_{k-1}}{q_{k-2}\xi-p_{k-2}} \iff \xi = \dfrac{p_{k-1}r_k + p_{k-2}}{q_{k-1}r_k+q_{k-2}}.
        $$
    
        To je upravo relacija verižnog razlomka $\xi = [a_0,a_1,\ldots,a_{k-1},r_k]$.
    -   Budući da je korak promjene $\vec\xi\times\vec\xi_{k-1,t}$ pri svakom dodavanju vektora jednak $|\vec\xi\times\vec\xi_{k-1}|$, preostala udaljenost $|\vec\xi\times\vec\xi_k|$ na kraju nužno je strogo manja od $|\vec\xi\times\vec\xi_{k-1}|$. To pokazuje da kvaliteta aproksimacije konvergentama (mjerena s $|qx-p|$) strogo raste s porastom $k$.
    -   Prema pravilima računanja s vektorskim produktom vrijedi
    
        $$
        \vec\xi_{k}\times\vec\xi_{k+1} = \vec\xi_{k}\times(a_{k+1}\vec\xi_k+\vec\xi_{k-1}) = \vec\xi_{k}\times\vec\xi_{k-1} = -\vec\xi_{k-1}\times\vec\xi_{k}.
        $$
    
        Indukcijom slijedi
    
        $$
        \vec\xi_{k}\times\vec\xi_{k+1} = (-1)^{k+2}\vec\xi_{k-2}\times\vec\xi_{k-1} = (-1)^{k}.
        $$
    
        To je upravo formula za razliku konvergenti $p_{k+1}q_k-p_kq_{k+1}=(-1)^k$.
    -   Područje između gornje i donje konveksne ljuske može se razrezati na nekoliko (možda beskonačno mnogo) trokuta čiji su vrhovi redom $\vec\xi_{k-2}$, $\vec\xi_k$ i $\vec 0$. Površina takvog trokuta jest
    
        $$
        \dfrac12|\vec\xi_{k-2}\times\vec\xi_k| = \dfrac12|\vec\xi_{k-2}\times(a_k\vec\xi_{k-1}+\vec\xi_{k-2})| = \dfrac{a_k}{2}|\vec\xi_{k-2}\times\vec\xi_{k-1}| = \dfrac{a_k}{2}.
        $$
    
        Prema [Pickovu teoremu](../../geometry/pick.md) to znači da, označimo li s $I$ i $B$ redom broj cjelobrojnih točaka u unutrašnjosti i na rubu trokuta, vrijedi
    
        $$
        I + \dfrac{B}{2} - 1 = \dfrac{a_k}{2}.
        $$
    
        Već znamo da se na rubu trokuta nalaze cjelobrojne točke $\{\vec 0\}\cup\{\vec\xi_{k-1,t}:0\le t\le a_k\}$, njih ukupno $a_k+2$. To pokazuje da nužno vrijedi $I=0$ i $B=a_k+2$. Stoga na stranicama trokuta nema drugih cjelobrojnih točaka, a nema ih ni u unutrašnjosti trokuta. Drugim riječima, $q_k$ i $p_k$ relativno su prosti, međurazlomci su sve cjelobrojne točke na stranici koja spaja $\vec\xi_{k-2}$ i $\vec\xi_k$, a sve cjelobrojne točke prvog kvadranta leže unutar gornje ili donje konveksne ljuske.

Tako dobivene gornja i donja konveksna ljuska nazivaju se Kleinovi poligoni. Slična se definicija može dati i u višedimenzionalnom prostoru, čime se dobiva [Kleinov poliedar](https://en.wikipedia.org/wiki/Klein_polyhedron) (Klein polyhedron), kojim se pojam verižnog razlomka poopćuje na više dimenzije.

## Stablo verižnih razlomaka

Glavni članak: [Stern–Brocotovo stablo i Fareyev niz](./stern-brocot.md)

Stern–Brocotovo stablo [binarno je stablo pretraživanja](../../ds/bst.md) koje sadrži sve razlomke iz $[0,\infty]$. Konačni verižni razlomak zapravo kodira put u Stern–Brocotovu stablu od korijena do položaja nekog razlomka. Drugim riječima, prikaz racionalnog broja $x$ verižnim razlomkom $[a_0,a_1,\ldots,a_{n-1},1]$ znači da se od korijena $\dfrac{1}{1}$ najprije $a_0$ puta pomaknemo u desno dijete, zatim $a_1$ puta u lijevo dijete, i tako naizmjence mijenjamo smjer sve dok se u nekom smjeru ne pomaknemo $a_{n-1}$ puta. Valja uočiti da se ovdje smije koristiti samo prikaz verižnim razlomkom koji završava s $1$.

Shvatimo li prikaz verižnim razlomkom kao put u Stern–Brocotovu stablu, dobivamo algoritam za usporedbu verižnih razlomaka po veličini.

???+ example "Usporedba verižnih razlomaka"
    Zadani su verižni razlomci $\alpha=[\alpha_0,\alpha_1,\ldots,\alpha_n]$ i $\beta=[\beta_0,\beta_1,\ldots,\beta_m]$; usporedite ih po veličini.

??? note "Rješenje"
    Najprije oba prikaza verižnim razlomkom pretvorimo u oblik koji završava s $1$. Bez smanjenja općenitosti pretpostavimo da su zadani verižni razlomci već takvog oblika, tj. $\alpha_n=\beta_m=1$. Budući da parne pozicije (indeksi počinju od $0$) označavaju broj koraka udesno, a neparne pozicije broj koraka ulijevo, vrijedi $\alpha<\beta$ ako i samo ako pri usporedbi u [leksikografskom poretku](../../string/basic.md#leksikografski-poredak) vrijedi
    
    $$
    (\alpha_0,-\alpha_1,\alpha_2,\ldots,(-1)^{n-1}\alpha_{n-1},0,\ldots)<(\beta_0,-\beta_1,\beta_2,\ldots,(-1)^{m-1}\beta_{m-1},0,\ldots).
    $$
    
    U odnosu na prikaz verižnim razlomkom, naizmjence dodajemo predznake, brišemo završnu $1$ i pozicije koje nedostaju popunjavamo s $0$.
    
    === "C++"
        ```cpp
        --8<-- "docs/math/code/continued-fraction/compare.cpp:core"
        ```
    
    === "Python"
        ```py
        --8<-- "docs/math/code/continued-fraction/compare.py:core"
        ```

???+ example "Najbolja unutarnja točka"
    Za $\dfrac{0}{1}\le\dfrac{p_0}{q_0}<\dfrac{p_1}{q_1}\le\dfrac{1}{0}$ pronađite racionalan broj $\dfrac{p}{q}$ takav da vrijedi $\dfrac{p_0}{q_0}<\dfrac{p}{q}<\dfrac{p_1}{q_1}$ i da je $(q,p)$ najmanji.

??? note "Rješenje"
    Budući da je Stern–Brocotovo stablo istodobno binarno stablo pretraživanja za razlomke iz $[0,\infty]$ i [kartezijevo stablo](../../ds/cartesian-tree.md) za parove $(q,p)$, zadatak se gotovo može svesti na traženje LCA (najnižeg zajedničkog pretka) dvaju čvorova u Stern–Brocotovu stablu. Međutim, LCA obrađuje samo slučaj zatvorenog intervala; LCA može biti i sam krajnji čvor. Da bismo izbjegli dodatno razlikovanje slučajeva, možemo najprije konstruirati $\dfrac{p_0}{q_0}+\varepsilon$ i $\dfrac{p_1}{q_1}-\varepsilon$ pa zatim izračunati LCA. Kad su putevi od korijena do čvorova već izračunati verižnim razlomcima, za LCA je dovoljno uzeti najdulji zajednički put.
    
    Da bismo konstruirali $x\pm\varepsilon$, dovoljno je u čvoru $x$ najprije se jednom pomaknuti udesno (ulijevo), a zatim $\infty$ puta ulijevo (udesno). U jeziku verižnih razlomaka, za razlomak $x=[a_0,a_1,\ldots,a_{n-1},1]$ znamo da su $x\pm\varepsilon$ nužno $[a_0,a_1,\ldots,a_{n-1}+1,\infty]$ i $[a_0,a_1,\ldots,a_{n-1},1,\infty]$, pa je dovoljno usporediti ta dva verižna razlomka i veći (manji) definirati kao $x\pm\varepsilon$.
    
    === "C++"
        ```cpp
        --8<-- "docs/math/code/continued-fraction/inner-point.cpp:core"
        ```
    
    === "Python"
        ```py
        --8<-- "docs/math/code/continued-fraction/inner-point.py:core"
        ```

???+ example "[GCJ 2019, Round 2 - New Elements: Part 2](https://github.com/google/coding-competitions-archive/blob/main/codejam/2019/round_2/new_elements_part_2/statement.pdf)"
    Zadano je $N$ parova pozitivnih cijelih brojeva $(C_i,J_i)$; pronađite par pozitivnih cijelih brojeva $(x,y)$ takav da je $\{C_ix+J_iy\}$ strogo rastući. Među svim parovima koji zadovoljavaju uvjet ispišite leksikografski najmanji.

??? note "Rješenje"
    Neka je $A_i=C_i-C_{i-1}$ i $B_i=J_i-J_{i-1}$. Problem se svodi na traženje $(x,y)$ takvog da su svi $A_ix+B_iy$ pozitivni. Ti se parovi mogu podijeliti u četiri slučaja:
    
    1.  slučaj $A_i,B_i>0$ može se zanemariti jer je već pretpostavljeno $(x,y)>0$;
    2.  u slučaju $A_i,B_i\le 0$ odmah ispisujemo „IMPOSSIBLE”;
    3.  slučaj $A_i>0,B_i\le 0$ odgovara ograničenju $\dfrac{y}{x}<\dfrac{A_i}{-B_i}$;
    4.  slučaj $A_i\le 0,B_i>0$ odgovara ograničenju $\dfrac{y}{x}>\dfrac{-A_i}{B_i}$.
    
    Stoga za $\dfrac{p_0}{q_0}$ uzmemo najveći $\dfrac{-A_i}{B_i}$ iz četvrtog slučaja, a za $\dfrac{p_1}{q_1}$ najmanji $\dfrac{A_i}{-B_i}$ iz trećeg slučaja. Izvorni problem postaje pronalaženje leksikografski najmanjeg $(q,p)$ takvog da vrijedi $\dfrac{p_0}{q_0}<\dfrac{p}{q}<\dfrac{p_1}{q_1}$.
    
    === "C++"
        ```cpp
        --8<-- "docs/math/code/continued-fraction/gcj-2019.cpp:core"
        ```
    
    === "Python"
        ```py
        --8<-- "docs/math/code/continued-fraction/gcj-2019.py:core"
        ```

Za više svojstava i primjena Stern–Brocotova stabla pogledajte njegov glavni članak.

## Razlomljene linearne transformacije

Još jedan važan pojam povezan s verižnim razlomcima jest takozvana razlomljena linearna transformacija.

???+ abstract "Razlomljena linearna transformacija"
    **Razlomljena linearna transformacija** (fractional linear transformation) funkcija je $L:\mathbf R\rightarrow\mathbf R$ oblika
    
    $$
    L(x) = \dfrac{ax+b}{cx+d},
    $$
    
    gdje su $a,b,c,d\in\mathbf R$ i $ad-bc\neq 0$.

???+ info "O uvjetu $ad-bc\neq 0$"
    Lako se provjeri da za $ad-bc=0$ funkcija može biti nedefinirana ili konstantna.

Razlomljene linearne transformacije imaju sljedeća svojstva:

???+ note "Svojstva razlomljenih linearnih transformacija"
    Neka su $L_1,L_2,L_3$ razlomljene linearne transformacije i neka je matrica koeficijenata od $L_i$
    
    $$
    M_i=\begin{pmatrix}a_i & b_i \\ c_i & d_i\end{pmatrix}
    $$
    
    Tada vrijede sljedeća svojstva:[^pgl2]
    
    1.  Kompozicija $L_1\circ L_2$ i inverz $L_1^{-1}$ razlomljenih linearnih transformacija opet su razlomljene linearne transformacije, tj. sve razlomljene linearne transformacije čine [grupu](../algebra/basic.md#群);
    2.  Razlomljena linearna transformacija ne mijenja se ako se svi koeficijenti pomnože istom konstantom različitom od nule, tj. za svaki $\lambda\neq 0$, ako je $M_2=\lambda M_1$, tada je $L_2=L_1$;
    3.  Matrica koeficijenata kompozicije razlomljenih linearnih transformacija odgovara umnošku matrica koeficijenata, tj. ako je $M_1M_2=M_3$, tada je $L_1\circ L_2=L_3$;
    4.  Matrica koeficijenata inverza razlomljene linearne transformacije odgovara inverzu matrice koeficijenata, tj. ako je $M_1^{-1}=M_2$, tada je $L_1^{-1}=L_2$.

??? note "Dokaz"
    Ovdje dajemo samo oblik kompozicije i inverza razlomljenih linearnih transformacija. Kad se taj oblik dobije, sva se svojstva lako provjere.
    
    Kompozicija razlomljenih linearnih transformacija $L_1$ i $L_2$:
    
    $$
    \begin{aligned}
    L_1\circ L_2 &= \dfrac{a_1\dfrac{a_2x+b_2}{c_2x+d_2}+b_1}{c_1\dfrac{a_2x+b_2}{c_2x+d_2}+d_1} = \dfrac{(a_1a_2+b_1c_2)x+(a_1b_2+b_1d_2)}{(c_1a_2+d_1c_2)x+(c_1b_2+d_1d_2)}.
    \end{aligned}
    $$
    
    Inverz razlomljene linearne transformacije $L_1(x)$:
    
    $$
    y = L_1(x) = \dfrac{a_1x+b_1}{c_1x+d_1} \iff x = L_1^{-1}(y) = \dfrac{d_1y - b_1}{-c_1y + a_1}.
    $$

Konačni verižni razlomak $[a_0,a_1,\ldots,a_n]$ može se shvatiti kao rezultat kompozicije niza razlomljenih linearnih transformacija. Neka je

$$
L_i(x) = \dfrac{a_ix+1}{x} = [a_i,x]. 
$$

Tada je konačni verižni razlomak

$$
[a_0,a_1,\ldots,a_n] = L_0\circ L_1\circ\cdots\circ L_n(\infty).
$$

Pritom je vrijednost razlomljene linearne transformacije $L(x)=\dfrac{ax+b}{cx+d}$ u $x=\infty$ jednaka $\dfrac{a}{c}$, što je limes funkcije kad $x\rightarrow\pm\infty$.

Za opći verižni razlomak, neka je $r_{k+1}$ ostatak realnog broja $x$, tj. $x=[a_0,\ldots,a_k,r_{k+1}]$; tada vrijedi

$$
x = L_0\circ L_1\circ\cdots\circ L_k(r_{k+1}) = \dfrac{p_kr_{k+1}+p_{k-1}}{q_kr_{k+1}+q_{k-1}}.
$$

To ujedno daje i oblik razlomljene linearne transformacije $L_0\circ L_1\circ\cdots\circ L_k$.

Dakako, taj se izraz može i izravno provjeriti. Na početku je

$$
x=\dfrac{x+0}{0x+1}=\dfrac{p_{-1}x+p_{-2}}{q_{-1}x+q_{-2}}.
$$

Zatim, ako $L_0\circ L_1\circ\cdots\circ L_{k-1}$ ima oblik

$$
\dfrac{p_{k-1}x+p_{k-2}}{q_{k-1}x+q_{k-2}}
$$

tada prema formuli za kompoziciju razlomljenih linearnih transformacija vrijedi

$$
L_0\circ L_1\circ\cdots\circ L_{k-1}\circ L_k = \dfrac{(p_{k-1}a_k+p_{k-2})x+p_{k-1}}{(q_{k-1}a_k+q_{k-2})x+q_{k-1}} = \dfrac{p_kx+p_{k-1}}{q_kx+q_{k-1}}.
$$

Time se gornji oblik dobiva induktivno. Razlomljene linearne transformacije daju i drugi pogled na razumijevanje rekurzivne formule i početnih uvjeta.

???+ example "[DMOPC '19 Contest 7 P4 - Bob and Continued Fractions](https://dmoj.ca/problem/dmopc19c7p4)"
    Zadani su niz pozitivnih cijelih brojeva $a_1,\ldots,a_n$ i $m$ upita; u svakom su upitu zadani $l\le r$ i treba izračunati vrijednost $[a_l,\ldots,a_r]$.

??? note "Rješenje"
    Shvatimo li verižni razlomak kao vrijednost kompozicije niza razlomljenih linearnih transformacija u $x=\infty$, dovoljno je moći više puta upitati kompoziciju jednog odsječka razlomljenih linearnih transformacija. Budući da svaka razlomljena linearna transformacija ima inverz, mogu se predizračunati prefiksni umnošci pa upite rješavati metodom razlika, uz složenost $O(n+m)$; ako su potrebne i izmjene, mogu se koristiti strukture poput segmentnog stabla.
    
    === "C++"
        ```cpp
        --8<-- "docs/math/code/continued-fraction/flt-presum.cpp"
        ```
    
    === "Python"
        ```py
        --8<-- "docs/math/code/continued-fraction/flt-presum.py"
        ```

### Aritmetičke operacije s verižnim razlomcima

Pomoću razlomljenih linearnih transformacija mogu se izvoditi četiri osnovne aritmetičke operacije s verižnim razlomcima. Taj je algoritam prvi predložio Gosper.

Temelj algoritma jest računanje razlomljene linearne transformacije verižnog razlomka. U ovom se odjeljku kao primjer uzimaju konačni verižni razlomci, ali budući da algoritam za ispis svake znamenke treba pročitati samo konačno mnogo članova verižnog razlomka, primjenjiv je i na beskonačne verižne razlomke i može računati do proizvoljne preciznosti. U kombinaciji s ranije opisanim algoritmom za usporedbu verižnih razlomaka mogu se točno uspoređivati razlike realnih brojeva proizvoljne preciznosti.

???+ example "Razlomljena linearna transformacija verižnog razlomka"
    Zadani su razlomljena linearna transformacija $L(x)=\dfrac{ax+b}{cx+d}$ i verižni razlomak $\alpha=[\alpha_0,\alpha_1,\ldots,\alpha_n]$; odredite prikaz $\beta=L(\alpha)$ verižnim razlomkom $[\beta_0,\beta_1,\ldots,\beta_m]$.

??? note "Rješenje"
    Osnovna je ideja algoritma redom određivati vrijednosti $\beta_i$. Označimo
    
    $$
    L_\gamma(x) = \gamma+\dfrac{1}{x} = \dfrac{\gamma x+1}{x}.
    $$
    
    Budući da je verižni razlomak
    
    $$
    L(\alpha) = L\circ L_{\alpha_0}\circ L_{\alpha_1}\circ\cdots\circ L_{\alpha_n}(\infty),
    $$
    
    vrijednost $L(\alpha)$ može se izračunati postupnim komponiranjem $L_{\alpha_k}$ na $L$. Međutim, želimo li dobiti prikaz $L(\alpha)$ verižnim razlomkom, nije potrebno najprije u potpunosti izračunati vrijednost $L(\alpha)$ pa tek onda odrediti prikaz. Vrijednosti $\beta_0,\beta_1,\ldots$ mogu se odrediti već tijekom komponiranja $L_{\alpha_i}$.
    
    Pretpostavimo, na primjer, da smo došli do
    
    $$
    L\circ L_{\alpha_0}\circ L_{\alpha_1}\circ\cdots\circ L_{\alpha_k}(x) = \dfrac{a_kx+b_k}{c_kx+d_k}
    $$
    
    i da su $c_k,d_k$ istog predznaka. Tada je $L\circ L_{\alpha_0}\circ L_{\alpha_1}\circ\cdots\circ L_{\alpha_k}(x)$ monotona na $[0,\infty]$ i vrijednosti su joj nužno između $\dfrac{a_k}{c_k}$ i $\dfrac{b_k}{d_k}$. Stoga, ako je
    
    $$
    \left\lfloor\dfrac{a_k}{c_k}\right\rfloor = \left\lfloor\dfrac{b_k}{d_k}\right\rfloor,
    $$
    
    možemo zaključiti da je to upravo cijeli dio $\beta_0$ od $L\circ L_{\alpha_0}\circ L_{\alpha_1}\circ\cdots\circ L_{\alpha_k}(x)$. Tada komponiranjem $L_{\beta_0}^{-1}$ slijeva dobivamo
    
    $$
    L_{\beta_0}^{-1}\circ L\circ L_{\alpha_0}\circ L_{\alpha_1}\circ\cdots\circ L_{\alpha_k}.
    $$

    
    Zatim daljnjim dodavanjem $L_{\alpha_{k+1}},L_{\alpha_{k+2}},\ldots$ možemo odrediti novi cijeli dio, tj. $\beta_1$. Tako računamo dalje dok ne odredimo vrijednosti svih $\beta_j$.
    
    Algoritam zahtijeva da $c$ i $d$ budu istog predznaka kako bi se osiguralo da točka prekida funkcije ne leži u $[0,\infty]$. To je uvijek moguće jer definicija jednostavnog verižnog razlomka zahtijeva da svi koeficijenti (osim $\alpha_0$) budu pozitivni cijeli brojevi. Odatle se može dokazati da će $c$ i $d$ nužno u konačno mnogo koraka postati istog predznaka i nakon toga to ostati.
    
    U konkretnoj implementaciji dovoljno je održavati matricu koeficijenata trenutačne razlomljene linearne transformacije $\begin{pmatrix}a&b\\c&d\end{pmatrix}$ i provjeravati jesu li $c$ i $d$ istog predznaka te imaju li $\dfrac{a}{c}$ i $\dfrac{b}{d}$ isti cijeli dio. Pri komponiranju $L_{\alpha_i}$ zdesna dobivamo $\begin{pmatrix}a\alpha_i+b&a\\ c\alpha_i+d&c\end{pmatrix}$. Ako je zajednički cijeli dio jednak $\beta_j$, u rezultirajući verižni razlomak dodajemo $\beta_j$ i slijeva komponiramo $L_{\beta_j}^{-1}$, što odgovara računanju $\begin{pmatrix}c&d\\ a\bmod c & b \bmod d \end{pmatrix}$.

Razlomljena linearna transformacija verižnog razlomka već se može upotrijebiti za aritmetičke operacije između razlomaka i verižnih razlomaka:

$$
\dfrac{p}{q}\pm x = \dfrac{\pm qx+p}{0x+q},\ \dfrac{p}{q}x = \dfrac{px+0}{0x+q},\ \frac{p}{q}/x = \dfrac{0x+p}{qx+0}.
$$

Za aritmetičke operacije između općih verižnih razlomaka potrebne su razlomljene bilinearne transformacije:

$$
x+y = \dfrac{0xy+x+y+0}{0xy+0x+0y+1},\ xy = \dfrac{1xy+0x+0y+0}{0xy+0x+0y+1},\ \dfrac{x}{y} = \dfrac{0xy+x+0y+0}{0xy+0x+y+0}.
$$

???+ example "Razlomljena bilinearna transformacija verižnih razlomaka"
    Zadani su razlomljena bilinearna transformacija $L(x,y)=\dfrac{axy+bx+cy+d}{exy+fx+gy+h}$ i verižni razlomci $\alpha=[\alpha_0,\alpha_1,\ldots,\alpha_n]$ i $\beta=[\beta_0,\beta_1,\ldots,\beta_m]$; odredite prikaz $\gamma=L(\alpha,\beta)$ verižnim razlomkom $[\gamma_0,\gamma_1,\ldots,\gamma_\ell]$.

??? note "Rješenje"
    Slično kao kod razlomljene linearne transformacije jedne varijable, za određivanje cijelog dijela dovoljno je osigurati da cijeli dio trenutačne transformacije ostaje nepromijenjen za $(x,y)\in[0,\infty]\times[0,\infty]$, tj. da su $e,f,g,h$ svi istog predznaka i da vrijedi
    
    $$
    \left\lfloor\dfrac{a}{e}\right\rfloor = \left\lfloor\dfrac{b}{f}\right\rfloor = \left\lfloor\dfrac{c}{g}\right\rfloor = \left\lfloor\dfrac{d}{h}\right\rfloor.
    $$
    
    Komponiranje zdesna zamjenjuje se računanjem $L(x,y)\mapsto L(L_{\alpha_i}(x),y)$ i $L(x,y)\mapsto L(x,L_{\beta_j}(y))$, što se također izražava kao linearna transformacija koeficijenata. Komponiranje slijeva potpuno je isto kao u slučaju jedne varijable: dovoljno je računati ostatke pri dijeljenju.
    
    U odnosu na slučaj jedne varijable, u slučaju dviju varijabli treba odlučiti hoće li se najprije komponirati $L_{\alpha_i}$ ili $L_{\beta_j}$. Budući da redoslijed komponiranja ne utječe na konačni rezultat, redoslijed se može slobodno birati, primjerice naizmjence komponirati $L_{\alpha_i}$ i $L_{\beta_j}$. Ili se može primijeniti heuristika da se prednost daje dimenziji s većom razlikom omjera: ako je $\left|\dfrac{b}{f}-\dfrac{d}{h}\right|>\left|\dfrac{c}{g}-\dfrac{d}{h}\right|$, najprije komponiramo $L_{\alpha_i}$; inače najprije komponiramo $L_{\beta_j}$.

## Periodični verižni razlomci

Slično pojmu periodičnog decimalnog zapisa, ako koeficijenti verižnog razlomka postanu periodični, on se naziva periodični verižni razlomak.

???+ abstract "Periodični verižni razlomak"
    Neka je $x=[a_0,a_1,a_2,\ldots]$ verižni razlomak i neka postoje prirodan broj $K$ i pozitivan cijeli broj $L$ takvi da za svaki $k\ge K$ vrijedi $a_k=a_{k+L}$; tada se verižni razlomak $x$ naziva **periodični verižni razlomak** (periodic continued fraction). Najmanji $L$ koji zadovoljava taj uvjet naziva se njegov najmanji pozitivni period, a niz $a_{k},\ldots,a_{k+L-1}$ koji se ponavlja u verižnom razlomku naziva se njegov period. Pomoću perioda periodični se verižni razlomak može zapisati kao $x=[a_0,\ldots,a_{k-1},\overline{a_k,\ldots,a_{k+L-1}}]$. Ako se za $K$ može uzeti $0$, tj. $x=[\overline{a_0,\ldots,a_{L-1}}]$, naziva se **čisto periodični verižni razlomak** (purely periodic continued fraction), a inače **mješovito periodični verižni razlomak** (eventually periodic continued fraction).

### Kvadratni iracionalni brojevi

Pojam usko povezan s periodičnim verižnim razlomcima jest [(realni) kvadratni iracionalni broj](./quadratic.md) (quadratic irrational), tj. iracionalno rješenje kvadratne jednadžbe s cjelobrojnim koeficijentima. Svi se kvadratni iracionalni brojevi mogu prikazati u obliku

$$
a+b\sqrt D
$$

gdje su $a,b$ racionalni brojevi, a $D$ je pozitivan cijeli broj bez kvadratnih faktora. Kvadratni iracionalni brojevi spomenuti u ovom članku podrazumijevaju se realnima. Nadalje, konjugat od $a+b\sqrt D$ jest $a-b\sqrt{D}$.

Eulerov rezultat pokazuje da su svi periodični verižni razlomci kvadratni iracionalni brojevi.

???+ note "Teorem (Euler)"
    Periodični verižni razlomci prikazuju kvadratne iracionalne brojeve.

??? note "Dokaz"
    Za opći periodični verižni razlomak $x=[a_0,\ldots,a_{k-1},\overline{a_k,\ldots,a_{k+L-1}}]$ stavimo $y=[\overline{a_k,\ldots,a_{k+L-1}}]$; tada je
    
    $$
    \begin{aligned}
    x&=[a_0,\ldots,a_{k-1},y] = L_0(y),\\
    y&=[a_k,\ldots,a_{k+L-1},y] = L_1(y),
    \end{aligned}
    $$
    
    gdje su $L_0(\cdot)$ i $L_1(\cdot)$ razlomljene linearne transformacije. Tako dobivamo jednadžbu koju $x$ zadovoljava:
    
    $$
    x = L_0\circ L_1\circ L_0^{-1}(x). 
    $$
    
    Neka je razlomljena linearna transformacija $L_0\circ L_1\circ L_0^{-1}(x) = \dfrac{ax+b}{cx+d}$; tada $x$ zadovoljava jednadžbu
    
    $$
    cx^2+(d-a)x-b=0.
    $$
    
    Stoga su svi periodični verižni razlomci rješenja kvadratne jednadžbe s cjelobrojnim koeficijentima. Budući da su beskonačni verižni razlomci iracionalni, periodični verižni razlomci prikazuju kvadratne iracionalne brojeve.

Lagrangeov rezultat pokazuje da vrijedi i obrat, pa su kvadratni iracionalni brojevi i periodični verižni razlomci ekvivalentni.

???+ note "Teorem (Lagrange)"
    Kvadratni iracionalni brojevi mogu se prikazati periodičnim verižnim razlomcima.

??? note "Dokaz"
    Ideja je dokazati da se ostatci ponavljaju. Neka se kvadratni iracionalni broj $x$ može zapisati u obliku
    
    $$
    x = \dfrac{P_0+\sqrt{D}}{Q_0}
    $$
    
    gdje su $P_0,Q_0,D$ cijeli brojevi i $Q_0\mid D-P_0^2$. To je uvijek moguće; na primjer, kvadratni iracionalni broj $x$ uvijek se može zapisati kao
    
    $$
    a+b\sqrt{D'} = \dfrac{p_a}{q_a}+\dfrac{p_b}{q_b}\sqrt{D'} = \dfrac{p_aq_b+\sqrt{p_b^2q_a^2D'}}{q_aq_b} = \dfrac{p_aq_aq_b^2+\sqrt{(q_aq_b)^2p_b^2q_a^2D'}}{(q_aq_b)^2}
    $$
    
    pa je dovoljno staviti $P=p_aq_aq_b^2$, $Q=(q_aq_b)^2$ i $D=Qp_b^2q_a^2D'$ (ovdje je pretpostavljeno $b>0$; za $b<0$ dovoljno je istodobno promijeniti predznak $P$ i $Q$).
    
    Prednost je takvog zapisa što se može dokazati da svi ostatci imaju sličan oblik:
    
    $$
    r_k=\dfrac{P_k+\sqrt D}{Q_k},
    $$
    
    gdje su $P_k,Q_k$ cijeli brojevi i $Q_k\mid D-P_k^2$. Uvjet $Q_k\mid D-P_k^2$ osigurava da je u brojnicima svih ostataka koeficijent uz $\sqrt{D}$ jednak $1$.
    
    Oblik ostataka dobiva se matematičkom indukcijom. Za $k=0$ tvrdnja je očita. Pretpostavimo da smo već dobili oblik od $r_k$ i neka je $a_k=\lfloor r_k\rfloor$; tada je
    
    $$
    r_k = a_k+\dfrac{1}{r_{k+1}}.
    $$
    
    Pretpostavimo da i $r_{k+1}$ ima sličan oblik te ga zajedno s $r_k$ uvrstimo u gornju jednakost:
    
    $$
    \dfrac{P_k+\sqrt D}{Q_k} = a_k + \dfrac{Q_{k+1}}{P_{k+1}+\sqrt{D}} = a_k + \dfrac{Q_{k+1}P_{k+1}-Q_{k+1}\sqrt{D}}{P_{k+1}^2-D}.
    $$
    
    Budući da je prikaz kvadratnog iracionalnog broja u obliku $a+b\sqrt{D}$ jedinstven, usporedbom koeficijenata na objema stranama dobivamo
    
    $$
    \dfrac{P_k}{Q_k} = a_k+\dfrac{Q_{k+1}P_{k+1}}{P_{k+1}^2-D},\ \dfrac{1}{Q_k}=-\dfrac{Q_{k+1}}{P_{k+1}^2-D}.
    $$
    
    Uvrštavanjem druge jednakosti u prvu može se izračunati $P_{k+1}$:
    
    $$
    \dfrac{P_k}{Q_k} = a_k-\dfrac{P_{k+1}}{Q_k} \iff P_{k+1} = a_kQ_k-P_k.
    $$
    
    Ponovnim uvrštavanjem u drugu jednakost dobiva se $Q_{k+1}$:
    
    $$
    Q_{k+1} = \dfrac{D-P_{k+1}^2}{Q_k} = \dfrac{D-(a_kQ_k-P_k)^2}{Q_k} = -a_k^2Q_k+2a_kP_k+\dfrac{D-P_k^2}{Q_k}.
    $$
    
    Prema pretpostavci indukcije $Q_k\mid D-P_k^2$, pa su $P_{k+1}$ i $Q_{k+1}$ doista cijeli brojevi, tj. i $r_{k+1}$ ima traženi oblik.
    
    Na kraju dokazujemo da ostatci mogu poprimiti samo konačno mnogo vrijednosti, pa se nužno ponavljaju. Ranije smo za ostatak dobili
    
    $$
    \dfrac{P_k+\sqrt{D}}{Q_k} = r_k = -\dfrac{q_{k-2}x-p_{k-2}}{q_{k-1}x-p_{k-1}}
    $$
    
    i za iracionalan broj uvijek je $r_k>1$. Istodobno njegov konjugat
    
    $$
    \dfrac{P_k-\sqrt{D}}{Q_k} = r_k^* = -\dfrac{q_{k-2}x^*-p_{k-2}}{q_{k-1}x^*-p_{k-1}} = -\dfrac{q_{k-2}}{q_{k-1}}\dfrac{x^*-\dfrac{p_{k-2}}{q_{k-2}}}{x^*-\dfrac{p_{k-1}}{q_{k-1}}}
    $$
    
    za dovoljno velik $k$ nužno je manji od $0$, jer je
    
    $$
    \dfrac{q_{k-2}}{q_{k-1}}>0,\ \lim_{k\rightarrow\infty}\dfrac{x^*-\dfrac{p_{k-2}}{q_{k-2}}}{x^*-\dfrac{p_{k-1}}{q_{k-1}}}=\dfrac{x^*-x}{x^*-x}=1.
    $$
    
    To pokazuje da je
    
    $$
    \dfrac{2\sqrt{D}}{Q_k} = r_k-r_k^*>1 \iff 0<Q_k\le 2\sqrt{D}.
    $$
    
    Stoga $Q_k$ može poprimiti samo konačno mnogo vrijednosti. Nadalje,
    
    $$
    D-P_{k}^2=Q_kQ_{k-1}>0 \iff |P_k|<\sqrt{D},
    $$
    
    pa i $P_k$ može poprimiti samo konačno mnogo vrijednosti. Prema tome, ostatak $r_k$ ima samo konačno mnogo mogućih vrijednosti, pa se u beskonačno mnogo članova nužno ponavlja.

Dokaz teorema ujedno daje rekurzivnu formulu za računanje ostataka kvadratnog iracionalnog broja:

???+ note "Rekurzivna formula za ostatke kvadratnog iracionalnog broja"
    Kvadratni iracionalni broj uvijek se može prikazati u obliku
    
    $$
    x=\dfrac{P_0+\sqrt{D}}{Q_0}
    $$
    
    uz $Q_0\mid D-P^2_0$. U njegovim ostatcima
    
    $$
    r_{k}=\dfrac{P_k+\sqrt{D}}{Q_k}
    $$
    
    $P_k,Q_k$ cijeli su brojevi i zadovoljavaju rekurzivnu relaciju
    
    $$
    \begin{aligned}
    P_{k+1} &= a_kQ_k-P_k,\\
    Q_{k+1} &= \dfrac{D-P_{k+1}^2}{Q_k}.
    \end{aligned}
    $$

Ta se rekurzivna formula može izravno upotrijebiti za računanje verižnog razlomka kvadratnog iracionalnog broja, a prema dokazu teorema vrijedi $|P_k|<\sqrt{D}$ i $Q_k\le 2\sqrt{D}$. Složenost tog algoritma ovisi o duljini perioda, a za nju se može dokazati da je $O(\sqrt{D}\log D)$[^period-surd].

???+ example "Kvadratni iracionalni broj"
    Zadan je kvadratni iracionalni broj $\alpha=\dfrac{x+y\sqrt{n}}{z}$; odredite njegov prikaz verižnim razlomkom. Pritom su $x,y,z,n\in\mathbf Z$ i $n>0$ nije potpuni kvadrat.

??? note "Rješenje"
    Najprije kvadratni iracionalni broj prikažemo u gore opisanom obliku, a zatim računamo rekurzivnom formulom. Članovi verižnog razlomka dani su s $a_k=\lfloor r_k\rfloor$. Da bismo odredili period, treba pamtiti indeks prvog pojavljivanja para $(P_k,Q_k)$.
    
    === "C++"
        ```cpp
        --8<-- "docs/math/code/continued-fraction/quadratic-irrational.cpp:core"
        ```
    
    === "Python"
        ```py
        --8<-- "docs/math/code/continued-fraction/quadratic-irrational.py:core"
        ```

???+ example "[Tavrida NU Akai Contest - Continued Fraction](https://timus.online/problem.aspx?space=1&num=1814)"
    Zadani su $x$ i $k$, pri čemu $x$ nije potpuni kvadrat i $0\le k\le 10^9$. Odredite $k$-tu konvergentu $x_k$ broja $\sqrt{x}$.

??? note "Rješenje"
    Najprije gore opisanim algoritmom odredimo period od $\sqrt{x}$, period prikažemo razlomljenom linearnom transformacijom, pa [brzim potenciranjem](../binary-exponentiation.md) dobijemo vrijednost $x_k$. Dakako, dio prije ulaska u period i dio kraći od jednog perioda treba obraditi zasebno.
    
    === "C++"
        ```cpp
        --8<-- "docs/math/code/continued-fraction/surd-convergent.cpp"
        ```
    
    === "Python"
        ```py
        --8<-- "docs/math/code/continued-fraction/surd-convergent.py"
        ```

### Čisto periodični verižni razlomci

Biti kvadratni iracionalan broj nužan je i dovoljan uvjet za postojanje prikaza periodičnim verižnim razlomkom, a razmatranje u ovom odjeljku daje nužan i dovoljan uvjet da realan broj ima prikaz čisto periodičnim verižnim razlomkom.

Najprije, budući da čisto periodični verižni razlomak ima oblik sličan konačnom verižnom razlomku, na njemu se može provesti operacija „obrtanja poretka”. Slično teoremu o obrnutom poretku, tako dobiveni prikaz verižnim razlomkom i izvorni prikaz u točno su određenom odnosu.

???+ note "Teorem (Galois)"
    Za čisto periodični verižni razlomak
    
    $$
    x = \left[\overline{a_0,a_1,\ldots,a_{\ell}}\right],
    $$
    
    označimo
    
    $$
    x' = \left[\overline{a_{\ell},\ldots,a_1,a_0}\right].
    $$
    
    Tada su $x$ i $x'$ međusobno „negativni recipročni konjugati”, tj. $x'$ je suprotna vrijednost recipročne vrijednosti konjugata od $x$.

??? note "Dokaz"
    Budući da se ne zahtijeva da $\ell+1$ bude najmanji pozitivni period, bez smanjenja općenitosti neka je $\ell>0$. Prema teoremu o obrnutom poretku vrijedi
    
    $$
    \begin{aligned}
    \dfrac{p_\ell}{p_{\ell-1}} &= [a_\ell,\ldots,a_1,a_0] = \dfrac{p'_\ell}{q'_\ell},\\
    \dfrac{q_\ell}{q_{\ell-1}} &= [a_\ell,\ldots,a_1] = \dfrac{p'_{\ell-1}}{q'_{\ell-1}}.
    \end{aligned}
    $$
    
    Budući da su obje strane jednakosti neskrativi razlomci, vrijedi
    
    $$
    p'_\ell = p_\ell,\ q'_\ell = p_{\ell-1},\ p'_{\ell-1}=q_\ell,\ q'_{\ell-1} = q_{\ell-1}.
    $$
    
    Za čisto periodični verižni razlomak $x$ njegov je $\ell+1$-vi ostatak upravo $x$, pa vrijedi
    
    $$
    x = \dfrac{xp_\ell+p_{\ell-1}}{xq_\ell+q_{\ell-1}}.
    $$
    
    Stoga zadovoljava kvadratnu jednadžbu
    
    $$
    q_\ell x^2+(q_{\ell-1}-p_\ell)x-p_{\ell-1} = 0.
    $$
    
    Analogno, $x'$ zadovoljava kvadratnu jednadžbu
    
    
    $$
    q'_\ell(x')^2+(q'_{\ell-1}-p'_\ell)x'-p'_{\ell-1} = 0.
    $$
    
    Prema odnosima koeficijenata ta se jednadžba može zapisati kao
    
    $$
    p_{\ell-1}(x')^2+(q_{\ell-1}-p_\ell)x'-q_\ell = 0.
    $$
    
    Stavimo $y=-\dfrac{1}{x'}$; tada $x$ i $y$ zadovoljavaju istu jednadžbu. No $x>0>y$, pa oni nisu isti korijen, nego su međusobno konjugirani, čime je izvorna tvrdnja dokazana.

Galois je tim opažanjem dalje dao nužan i dovoljan uvjet da kvadratni iracionalni broj ima prikaz čisto periodičnim verižnim razlomkom.

???+ note "Teorem (Galois)"
    Kvadratni iracionalni broj $x$ može se prikazati čisto periodičnim verižnim razlomkom ako i samo ako je $x>1$ i za njegov konjugat vrijedi $-1<x^*<0$.

??? note "Dokaz"
    Ako je $x$ čisto periodični verižni razlomak, tada uz ranije oznake vrijedi $a_0=a_{\ell+1}\ge 1$, pa je $x>1$. Budući da je i njegov negativni recipročni konjugat periodični verižni razlomak, njegov konjugat $x^*$ zadovoljava $-\dfrac{1}{x^*}>1$, tj. $-1<x^*<0$. Time je dokazano da svi čisto periodični verižni razlomci zadovoljavaju taj uvjet.
    
    Obratno, neka je $x>1$ kvadratni iracionalni broj s $-1<x^*<0$. Za ostatke $r_k$ broja $x$ vrijedi rekurzivna relacija
    
    $$
    r_k = a_k+\dfrac{1}{r_{k+1}}.
    $$
    
    Obje su strane jednakosti kvadratni iracionalni brojevi, pa konjugiranjem dobivamo
    
    $$
    r_{k}^* = a_k+\dfrac{1}{r_{k+1}^*}.
    $$
    
    Pomoću te rekurzivne relacije može se dokazati da $-1<r_{k}^*<0$ vrijedi za sve $k\ge 0$.
    
    Najprije, za $k=0$ vrijedi $-1<r_0^*=x^*<0$, što je očito. Za $k\ge 0$ iz definicije jednostavnog verižnog razlomka i $x>1$ slijedi $a_k\ge 1$. Stoga, pretpostavimo li $-1<r_k^*<0$, imamo
    
    $$
    -1<-\dfrac{1}{a_k}< r_{k+1}^* = \dfrac{1}{r_k^*-a_k} < -\dfrac{1}{1+a_k} < 0.
    $$
    
    Time je indukcijom dokazano da $-1<r_{k}^*<0$ vrijedi za sve $k\ge 0$. Stoga vrijedi
    
    $$
    a_k = -\dfrac{1}{r_{k+1}^*}+r_k^* = \left\lfloor-\dfrac{1}{r_{k+1}^*}\right\rfloor.
    $$
    
    Budući da je kvadratni iracionalni broj nužno periodični verižni razlomak, postoje pozitivan cijeli broj $L$ i barem neki dovoljno velik $k$ takvi da je $r_{k}=r_{k+L}$. No tada nužno vrijedi i
    
    $$
    a_{k-1} = \left\lfloor-\dfrac{1}{r_{k}^*}\right\rfloor = \left\lfloor-\dfrac{1}{r_{k+L}^*}\right\rfloor = a_{k+L-1}.
    $$
    
    Stoga je
    
    $$
    r_{k-1} = a_{k-1}+\dfrac{1}{r_k} = a_{k+L-1}+\dfrac{1}{r_{k+L}} = r_{k+L-1}.
    $$
    
    To znači da najmanji $k$ za koji vrijedi $r_{k}=r_{k+L}$ nužno mora biti $0$. Drugim riječima, $x$ se može prikazati čisto periodičnim verižnim razlomkom.

Galoisov teorem otkriva pravilnost prikaza verižnim razlomkom čistih kvadratnih korijena (pure quadratic surd), tj. kvadratnih iracionalnih brojeva oblika $\sqrt{r}$.

???+ note "Korolar"
    Za racionalan broj $r>1$, ako je $\sqrt{r}$ iracionalan, tada je
    
    $$
    \sqrt{r} = [\lfloor\sqrt{r}\rfloor,\overline{a_1,\ldots,a_{\ell},2\lfloor\sqrt{r}\rfloor}]
    $$
    
    i za svaki $1\le k\le\ell$ vrijedi $a_k = a_{\ell+1-k}$.

??? note "Dokaz"
    Za kvadratni iracionalni broj $\sqrt{r}$, budući da je $\lfloor\sqrt{r}\rfloor+\sqrt{r}>1$ i $-1<\lfloor\sqrt{r}\rfloor-\sqrt{r}<0$, $\lfloor\sqrt{r}\rfloor+\sqrt{r}$ čisto je periodični verižni razlomak:
    
    $$
    \lfloor\sqrt{r}\rfloor+\sqrt{r} = [\overline{2\lfloor\sqrt{r}\rfloor,a_1,\ldots,a_\ell}].
    $$
    
    Prema gornjem teoremu njegov negativni recipročni konjugat ima oblik
    
    $$
    \dfrac{1}{\sqrt{r}-\lfloor\sqrt{r}\rfloor} = [\overline{a_\ell,\ldots,a_1,2\lfloor\sqrt{r}\rfloor}].
    $$
    
    Iz osnovnih svojstava verižnih razlomaka slijedi
    
    $$
    \sqrt{r}=\lfloor\sqrt{r}\rfloor+\dfrac{1}{\dfrac{1}{\sqrt{r}-\lfloor\sqrt{r}\rfloor}}=[\lfloor\sqrt{r}\rfloor,\overline{a_\ell,\ldots,a_1,2\lfloor\sqrt{r}\rfloor}].
    $$
    
    No iz prikaza $\lfloor\sqrt{r}\rfloor+\sqrt{r}$ verižnim razlomkom također slijedi
    
    $$
    \sqrt{r} = -\lfloor\sqrt{r}\rfloor+\left(\lfloor\sqrt{r}\rfloor+\sqrt{r}\right) = [\lfloor\sqrt{r}\rfloor,\overline{a_1,\ldots,a_\ell,2\lfloor\sqrt{r}\rfloor}].
    $$
    
    Budući da je prikaz iracionalnog broja verižnim razlomkom jedinstven, usporedbom srednjih koeficijenata vidimo da $a_k=a_{\ell+1-k}$ vrijedi za sve $1\le k\le\ell$.

??? example "Primjer: razvoj $\sqrt{74}$ u verižni razlomak"
    Verižni razlomak od $\sqrt{74}$ može se izračunati ovako (ovdje samo radi ilustracije; za programsko računanje treba koristiti ranije spomenuti rekurzivni algoritam):
    
    $$
    \begin{aligned}
    \sqrt{74}&=8+(-8)+\sqrt{74}=\left[8,\frac{8+\sqrt{74}}{10}\right]\\
    &=\left[8,1+\frac{-2+\sqrt{74}}{10}\right]=\left[8,1,\frac{2+\sqrt{74}}{7}\right]\\
    &=\left[8,1,1+\frac{-5+\sqrt{74}}{7}\right]=\left[8,1,1,\frac{5+\sqrt{74}}{7}\right]\\
    &=\left[8,1,1,1+\frac{-2+\sqrt{74}}{7}\right]=\left[8,1,1,1,\frac{2+\sqrt{74}}{10}\right]\\
    &=\left[8,1,1,1,1+\frac{-8+\sqrt{74}}{10}\right]=\left[8,1,1,1,1,8+\sqrt{74}\right]\\
    &=\left[8,1,1,1,1,16+(-8)+\sqrt{74}\right]=\left[8,\overline{1,1,1,1,16}\right]
    \end{aligned}
    $$
    
    Pojedini ostatci redom su:
    
    $$
    \begin{alignedat}{3}
    r_1&=\frac{8+\sqrt{74}}{10}&&=\left[\overline{1,1,1,1,16}\right]\\
    r_2&=\frac{2+\sqrt{74}}{7}&&=\left[\overline{1,1,1,16,1}\right]\\
    r_3&=\frac{5+\sqrt{74}}{7}&&=\left[\overline{1,1,16,1,1}\right]\\
    r_4&=\frac{2+\sqrt{74}}{10}&&=\left[\overline{1,16,1,1,1}\right]\\
    r_5&=8+\sqrt{74}&&=\left[\overline{16,1,1,1,1}\right]
    \end{alignedat}
    $$
    
    Prema Galoisovu zaključku, periodični dijelovi ostataka $r_k$ i $r_{L+1-k}$ upravo su obrnuti, pa su oni međusobno negativni recipročni konjugati. Ako je duljina perioda $L$ od $\sqrt{D}$ neparna, srednji je član negativni recipročni konjugat samoga sebe; ako je duljina perioda $L$ parna, takav član ne postoji. Razmatranje u odjeljku o Pellovoj jednadžbi pokazat će da parnost duljine perioda određuje ima li jednadžba $x^2-Dy^2=-1$ rješenja.

Razvoj kvadratnog iracionalnog broja $\sqrt{D}$ u verižni razlomak uglavnom se primjenjuje pri rješavanju [Pellove jednadžbe](./pell-equation.md).

## Primjeri zadataka

Nakon svladavanja osnovnih pojmova potrebno je proučiti nekoliko konkretnih zadataka kako bi se razumjelo kako se metoda verižnih razlomaka primjenjuje na algoritamskim natjecanjima.

???+ example "Konveksna ljuska ispod pravca"
    Zadan je $r=[a_0,a_1,\ldots,a_n]$; odredite konveksnu ljusku skupa cjelobrojnih točaka $(x,y)$ koje zadovoljavaju $0\le x\le N$ i $0\le y\le rx$.

??? note "Rješenje"
    Za neograničeni skup $x\ge 0$ gornja je ljuska sam pravac $y=rx$. Međutim, kao što prikazuje sljedeća slika, ako se dodatno zahtijeva $x\le N$, gornja ljuska na kraju odstupa od pravca.
    
    ![](./images/lattice-hull.svg)
    
    
    Počevši od $(0,0)$, sve cjelobrojne točke gornje ljuske mogu se odrediti slijeva nadesno. Pretpostavimo da je posljednja dosad određena cjelobrojna točka gornje ljuske $(x,y)$. Sada treba odrediti sljedeću cjelobrojnu točku $(x',y')$. Vrh $(x',y')$ nalazi se gore desno od $(x,y)$; označimo s $(\Delta x,\Delta y)=(x'-x,y'-y)$ njihovu razliku. Tada nužno vrijedi
    
    $$
    0<\Delta x\le N-x,\ 0\le \Delta y\le r\Delta x.
    $$
    
    Druga nejednakost vrijedi jer bi uvjet $\Delta y>r\Delta x$ bio u suprotnosti s time da je $(x,y)$ već na gornjoj ljusci. Promotrimo li uvjete koje $(\Delta x,\Delta y)$ mora zadovoljavati, za različite točke $(x,y)$ mijenja se samo gornja granica za $\Delta x$. Stoga, riješimo li taj potproblem, sve cjelobrojne točke izvornog problema mogu se odrediti rekurzivno.
    
    Razmotrimo zatim rješenje potproblema. U usporedbi s izvornim problemom, potproblem odgovara promjeni gornje granice za $x$ u $N'$ i traženju prve cjelobrojne točke gornje ljuske susjedne ishodištu. Označimo rješenje potproblema s $(q,p)$. Tada su $p$ i $q$ nužno relativno prosti (inače to nije prva cjelobrojna točka), a nagib spojnice s ishodištem $\dfrac{p}{q}$ najveći je među svim cjelobrojnim točkama ispod pravca $y=rx$ s apscisom ne većom od $N'$ (inače točka nije na konveksnoj ljusci). U kombinaciji s ranijom [geometrijskom interpretacijom](#geometrijska-interpretacija) slijedi da takva točka $(x,y)$ nužno odgovara nekom donjem međurazlomku od $r$. Budući da je donji međurazlomak s većim nazivnikom bliži $r$, rješenje potproblema $(q,p)$ odgovara donjem međurazlomku s najvećim nazivnikom među svima s nazivnikom ne većim od $N'$.
    
    Dakako, pri stvarnom rješavanju nije potrebno za svaki potproblem iznova tražiti takav donji međurazlomak. Najprije treba odrediti sve konvergente, što ujedno daje način obilaska svih donjih međurazlomaka. Zatim obilazimo donje međurazlomke od najvećeg nazivnika prema najmanjem i svaki put pokušavamo dodati ga na prethodnu cjelobrojnu točku $(x,y)$ sve dok dodavanje više nije moguće, pa tek tada prelazimo na sljedeći donji međurazlomak.
    
    Ovdje postoje neke očite optimizacije. Prvo, za donji međurazlomak $(q,p)$ nužno postoje neparan $k$ i $0\le t<a_{k+1}$ takvi da je $(q,p)=(q_{k-1},p_{k-1})+t(q_k,p_k)$. Dovoljno je pronaći najveći $t$ za koji vrijedi $q_{k-1}+tq_k+x\le N$, tj. $t=\left\lfloor\dfrac{N-q_{k-1}-x}{q_k}\right\rfloor$. Ne treba brinuti da $t$ izađe izvan granica jer je veća donja konvergenta $(q_{k+1},p_{k+1})$ već dodana do kraja. A pri svakom određivanju broja dodavanja dovoljno je izravno izračunati $\left\lfloor\dfrac{N-x}{q}\right\rfloor$, bez pokušavanja jedan po jedan.
    
    Složenost optimiziranog algoritma jest $O(n)$. Iako cjelobrojnih točaka koje odgovaraju donjim međurazlomcima može biti mnogo, malo ih doista postaje prirast. U nastavku pokazujemo da se među svim donjim međurazlomcima $(q,p)=(q_{k-1},p_{k-1})+t(q_k,p_k)$ s $0\le t<a_{k+1}$ pojavljuju najviše dva prirasta. Pretpostavimo da se među tim donjim međurazlomcima doista pojavi prirast; tada nužno vrijedi $q_{k-1}\le N-x<q_{k+1}$. Neka je $t=\left\lfloor\dfrac{N-q_{k-1}-x}{q_k}\right\rfloor$. Ako je $t=0$, prirast ima $\Delta x=q_{k-1}$, pa nakon dodavanja prirasta vrijedi $N-x'<q_{k-1}$ i među tim donjim međurazlomcima više se neće pojaviti novi prirast; ako je $t>0$, nakon dodavanja prirasta nužno vrijedi $N-x'=(N-q_{k-1}-x)\bmod q_k<q_k$, pa čak i ako se u istom odsječku donjih međurazlomaka pojavi novi prirast, sljedeći put može biti samo $t'=0$. Stoga se u jednom takvom odsječku donjih međurazlomaka mogu pojaviti najviše dva prirasta. To pokazuje da je ukupna vremenska složenost $O(n)$.
    
    === "C++"
        ```cpp
        --8<-- "docs/math/code/continued-fraction/hull-under-line.cpp:core"
        ```
    
    === "Python"
        ```py
        --8<-- "docs/math/code/continued-fraction/hull-under-line.py:core"
        ```

???+ example "[Timus - Crime and Punishment](https://timus.online/problem.aspx?space=1&num=1430)"
    Zadani su pozitivni cijeli brojevi $A,B,N \le 2\times 10^9$; pronađite $x,y\ge 0$ takve da je $Ax+By\le N$ i da je $Ax+By$ što veći.

??? note "Rješenje"
    Ovaj zadatak ima rješenje složenosti $O(\sqrt N)$: neka je $A\ge B$; budući da je $A(B+x)+By=Ax+B(A+y)$, dovoljno je tražiti odgovor među $x\le\min\{N/A, B\}$. To je dovoljno za prolaz zadatka. No primijenimo li metodu verižnih razlomaka, vremenska se složenost može smanjiti na $O(\log N)$.
    
    Radi jednostavnijeg razmatranja najprije zamjenom $x\mapsto\left\lfloor N/A\right\rfloor-x$ promijenimo predznak od $x$. Neka je $C=N\bmod A$ i $M=\left\lfloor N/A\right\rfloor$; tada se izvorni problem pretvara u traženje optimalnog $(x,y)$ koji maksimizira $By-Ax$ uz uvjete $0\le x\le M$ i $By-Ax\le C$. Za svaki fiksni $x$ optimalna je vrijednost $y$ jednaka $\left\lfloor\dfrac{Ax+C}{B}\right\rfloor$.
    
    U nastavku pokazujemo da ovaj problem ima rješenje slično prethodnom primjeru. No za razliku od prethodnog primjera, u kojem su se donji međurazlomci koristili za udaljavanje od pravca, ovdje se gornjim međurazlomcima treba približavati pravcu. Konkretno, vrijednost $C-(By-Ax)$ proporcionalna je udaljenosti točke $(x,y)$ od pravca $By-Ax=C$. Maksimizirati $By-Ax$ ekvivalentno je minimiziranju te udaljenosti. Cilj je algoritma pronaći dopustivu cjelobrojnu točku ispod pravca $By-Ax=C$ koja mu je najbliža. Ideja je algoritma krenuti od krajnje lijeve točke i pretraživati duž gornje konveksne ljuske tih cjelobrojnih točaka, postupno smanjujući udaljenost od pravca, dok se ne dobije optimalno rješenje.
    
    U koordinatnom sustavu $(x,y)$ algoritam kreće od $(0,\lfloor C/B\rfloor)$ te rekurzivno traži i dodaje optimalni prirast $(\Delta x,\Delta y)$, pri čemu osigurava da je točka nakon dodavanja bliža pravcu $By-Ax=C$ nego prije, ali ne smije prijeći na drugu stranu pravca niti apscisa smije postati veća od $M$. Neka je već dobivena točka $(x,y)$; tada prirast $(\Delta x,\Delta y)$ zadovoljava uvjete
    
    $$
    0<B\Delta y-A\Delta x\le C-(By-Ax),\ 0<\Delta x\le M-x.
    $$
    
    Prema ideji pretraživanja duž donje konveksne ljuske, dovoljno je među točkama koje zadovoljavaju te uvjete pronaći onu s najmanjim $\Delta x$. Prvu nejednakost prepišimo kao
    
    $$
    \Delta y \le \dfrac{A}{B}\Delta x+\dfrac{C-(By-Ax)}{B}.
    $$
    
    U kombinaciji s ranijom [geometrijskom interpretacijom](#geometrijska-interpretacija) slijedi da, čim je konstantni član na kraju manji od $1$, cjelobrojna točka $(\Delta x,\Delta y)$ s najmanjom apscisom koja zadovoljava tu nejednakost sigurno odgovara nekom gornjem međurazlomku. Naime, ona je među svim razlomcima s nazivnikom ne većim od njezina nazivnika najbolja aproksimacija nekog realnog broja odozgo, a to može biti samo gornji međurazlomak. A nakon svakog dodavanja prirasta gornja granica za $\Delta y$ postaje stroža, što znači da treba promatrati gornje međurazlomke s većim nazivnikom.
    
    Postupamo po uzoru na prethodni primjer. Promatramo sve gornje međurazlomke od najmanjeg nazivnika prema najvećem; ako pronađemo gornji međurazlomak kod kojeg ni apscisa ni ordinata ne izlaze izvan granica, dodajemo ga i ažuriramo odgovarajuće gornje granice. Kad su dodani svi dopustivi gornji međurazlomci, dobiveno je optimalno rješenje. Za razliku od prije, u ovom zadatku treba istodobno paziti da ni apscisa ni ordinata ne izađu izvan granica, na što treba obratiti posebnu pozornost. Razmatranjem sličnim onome u prethodnom primjeru, ali ovaj put s $B\Delta y-A\Delta x$ umjesto ranijeg $\Delta x$, može se pokazati da je složenost ovog algoritma $O(\log\min\{A,B\})$.
    
    === "C++"
        ```cpp
        --8<-- "docs/math/code/continued-fraction/closest-dio.cpp:core"
        ```
    
    === "Python"
        ```py
        --8<-- "docs/math/code/continued-fraction/closest-dio.py:core"
        ```

???+ example "[June Challenge 2017 - Euler Sum](https://www.codechef.com/problems/ES)"
    Izračunajte vrijednost $\sum\limits_{x=1}^N \lfloor \mathrm{e}x \rfloor$, gdje je $\mathrm{e}$ baza prirodnog logaritma.
    
    Uputa: $\mathrm{e} = [2,1,2,1,1,4,1,1,6,1,\ldots,1,2n,1, \ldots]$.[^continued-fraction-of-e]

??? note "Rješenje"
    Ta je suma jednaka broju cjelobrojnih točaka u skupu $\{(x,y):1\le x\le N,1\le y\le\mathrm{e}x\}$. Nakon konstrukcije konveksne ljuske cjelobrojnih točaka ispod pravca $y=\mathrm{e}x$ broj cjelobrojnih točaka može se izračunati [Pickovim teoremom](../../geometry/pick.md). Vremenska složenost jest $O(\log N)$.
    
    Izvorni zadatak zahtijeva $N \le 10^{4000}$. Ovdje je C++ kod samo ilustrativan i ne implementira klasu za aritmetiku velikih brojeva.
    
    === "C++"
        ```cpp
        --8<-- "docs/math/code/continued-fraction/sum-floor.cpp:core"
        ```
    
    === "Python"
        ```py
        --8<-- "docs/math/code/continued-fraction/sum-floor.py:core"
        ```

???+ example "[NAIPC 2019 - It's a Mod, Mod, Mod, Mod World](https://open.kattis.com/problems/itsamodmodmodmodworld)"
    Zadani su pozitivni cijeli brojevi $p,q,n$; izračunajte vrijednost $\sum\limits_{i=1}^n [pi \bmod q]$.

??? note "Rješenje"
    Budući da se suma može preoblikovati u
    
    $$
    \sum_{i=1}^n [pi \bmod q] 
    =\sum_{i=1}^n\left(pi - q\left\lfloor\dfrac{pi}{q}\right\rfloor\right) = \dfrac{pn(n+1)}{2} - q\sum_{i=1}^n\left\lfloor\dfrac{p}{q}i\right\rfloor,
    $$
    
    ovaj se problem može svesti na prethodni; dovoljno je $\mathrm{e}$ zamijeniti s $\dfrac{p}{q}$. Vremenska složenost jednog upita jest $O(\log\min\{p,q\})$.
    
    === "C++"
        ```cpp
        --8<-- "docs/math/code/continued-fraction/mod-mod-mod.cpp:core"
        ```
    
    === "Python"
        ```py
        --8<-- "docs/math/code/continued-fraction/mod-mod-mod.py:core"
        ```

???+ example "[Library Checker - Sum of Floor of Linear](https://judge.yosupo.jp/problem/sum_of_floor_of_linear)"
    Zadani su pozitivni cijeli brojevi $N,M,A,B$; izračunajte vrijednost $\displaystyle\sum_{i=0}^{N-1} \left\lfloor \dfrac{A \cdot i + B}{M} \right\rfloor$.

??? note "Rješenje"
    Ovo je dosad najsloženiji zadatak. Može se izračunati [algoritmom nalik Euklidovu](./euclidean.md). Ovdje dajemo algoritam zasnovan na verižnim razlomcima, vremenske složenosti $O(\log\min\{A,M\})$.
    
    Može se konstruirati konveksna ljuska svih cjelobrojnih točaka ispod pravca $y=\dfrac{Ax+B}{M}$ s $0\le x< N$ i broj cjelobrojnih točaka izračunati Pickovim teoremom. Slučaj $B=0$ već je riješen. Opći se slučaj može obraditi u dva koraka. Najprije se dodavanjem gornjih međurazlomaka postupno približavamo pravcu (tj. drugi primjer) dok ne pronađemo točku najbližu pravcu, a zatim se dodavanjem donjih međurazlomaka postupno udaljavamo od pravca (tj. prvi primjer).
    
    === "C++"
        ```cpp
        --8<-- "docs/math/code/continued-fraction/sum-floor-axbc.cpp:core"
        ```
    
    === "Python"
        ```py
        --8<-- "docs/math/code/continued-fraction/sum-floor-axbc.py:core"
        ```

???+ example "[OKC 2 - From Modular to Rational](https://codeforces.com/gym/102354/problem/I)"
    Postoji nepoznati racionalan broj $\dfrac{p}{q}$ s $1\le p, q\le 10^9$; smijete upitati vrijednost $pq^{-1}$ modulo neki prost broj $m\in[10^9,10^{12}]$. Odredite $p$ i $q$ s najviše deset upita.
    
    Ovaj je problem ekvivalentan traženju $x$ iz $[1,n]$ koji minimizira $rx\bmod m$, gdje je $r$ rezultat $pq^{-1}$ modulo $m$, a $n=10^9$.

??? note "Rješenje"
    Prema [kineskom teoremu o ostatcima](./crt.md), upiti o rezultatima modulo više prostih brojeva ekvivalentni su upitu o rezultatu modulo umnožak tih prostih brojeva. Stoga se ovaj zadatak može shvatiti kao upit o razlomku modulo dovoljno velik modul $m$, pri čemu treba odrediti brojnik i nazivnik razlomka.
    
    Za neki modul $m$ par $(p,q)$ za koji vrijedi $qr\equiv p\pmod m$ ne mora biti jedinstven. Pretpostavimo da i $(p_1,q_1)$ i $(p_2,q_2)$ zadovoljavaju tu jednakost; tada nužno vrijedi $(p_1q_2-p_2q_1)r\equiv 0\pmod m$. Prema konstrukciji od $r$, $r$ i $m$ relativno su prosti, pa je $p_1q_2-p_2q_1\equiv 0\pmod m$, tj. $m\mid(p_1q_2-p_2q_1)$. Ako $p_1q_2-p_2q_1$ nije nula, njegova je apsolutna vrijednost barem $m$. U zadatku je ograničeno $p,q\in[1,10^9]$, što znači da ta razlika ne bi smjela premašiti $10^{18}$, pa je dovoljno uzeti $m>10^{18}$ kako bi dobiveni $(p,q)$ bio jedinstven.
    
    Problem se sada svodi na sljedeće: za zadani modul $m$ i ostatak $r$ pronaći par pozitivnih cijelih brojeva $(p,q)$ ne većih od $n$ takav da je $qr\equiv p\pmod m$. Kad znamo da je takvo rješenje jedinstveno, zapravo je dovoljno pronaći među $q\in[1,n]$ onaj $q$ koji minimizira $qr\bmod m$, jer tada postoji točno jedan $q$ za koji ostatak ne premašuje $n$. To je upravo ranije spomenuta ekvivalentna formulacija.
    
    U koordinatnom sustavu ravnine $(q,k)$ to odgovara traženju cjelobrojne točke s $q\in[1,n]$ ispod pravca $qr-km=0$ koja mu je najbliža, jer je ostatak $qr\bmod m$ upravo proporcionalan udaljenosti cjelobrojne točke od pravca. U kombinaciji s ranijom [geometrijskom interpretacijom](#geometrijska-interpretacija) slijedi da takva cjelobrojna točka nužno odgovara nekom donjem međurazlomku racionalnog razlomka $\dfrac{r}{m}$. Složenost algoritma jest $O(\log\min\{r,m\})$.
    
    === "C++"
        ```cpp
        --8<-- "docs/math/code/continued-fraction/recover-fraction.cpp:core"
        ```
    
    === "Python"
        ```py
        --8<-- "docs/math/code/continued-fraction/recover-fraction.py:core"
        ```

## Zadaci za vježbu

-   [UVa OJ - Continued Fractions](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=775)
-   [ProjectEuler+ #64: Odd period square roots](https://www.hackerrank.com/contests/projecteuler/challenges/euler064/problem)
-   [「LibreOJ NOI Round #2」单枪匹马 (Sam samcat)](https://loj.ac/p/573)
-   [Codeforces Round #184 (Div. 2) - Continued Fractions](https://codeforces.com/contest/305/problem/B)
-   [Codeforces Round #201 (Div. 1) - Doodle Jump](https://codeforces.com/contest/346/problem/E)
-   [Codeforces Round #325 (Div. 1) - Alice, Bob, Oranges and Apples](https://codeforces.com/contest/585/problem/C)
-   [POJ Founder Monthly Contest 2008.03.16 - A Modular Arithmetic Challenge](http://poj.org/problem?id=3530)
-   [2019 Multi-University Training Contest 5 - fraction](http://acm.hdu.edu.cn/showproblem.php?pid=6624)
-   [SnackDown 2019 Elimination Round - Election Bait](https://www.codechef.com/SNCKEL19/problems/EBAIT)
-   [Luogu P5179. Fraction](https://www.luogu.com.cn/problem/P5179)
-   [Luogu P7739. \[NOI2021\] 密码箱 (Sef s lozinkom)](https://www.luogu.com.cn/problem/P7739)

## Literatura i dodatno čitanje

-   Hardy, G. H., Wright, E. M., Heath-Brown, R., & Silverman, J. (2008). An Introduction to the Theory of Numbers. Oxford Mathematics.
-   朱尧辰, 王连祥 《丢番图逼近引论》 (Zhu Yaochen, Wang Lianxiang, Uvod u diofantsku aproksimaciju)
-   [FatFish 的博客 - 连分数入门 (FatFishov blog - Uvod u verižne razlomke)](https://chaoli.club/index.php/2756)
-   [Simple continued fraction - Wikipedia](https://en.wikipedia.org/wiki/Simple_continued_fraction)
-   [Periodic continued fraction - Wikipedia](https://en.wikipedia.org/wiki/Periodic_continued_fraction)
-   [Gosper's original notes on continued fraction arithmetic algorithms](https://perl.plover.com/yak/cftalk/INFO/gosper.txt)
-   [Understanding Bill Gosper's continued fraction arithmetic (implemented in Python)](https://hsinhaoyu.github.io/cont_frac/)

**Glavnina sadržaja ove stranice prevedena je iz članka [Continued fractions](https://cp-algorithms.com/algebra/continued-fractions.html), licenciranog pod CC-BY-SA 4.0, uz izmjene sadržaja.**

[^one-representation]: Prirodan broj $1$ ima samo nestandardne prikaze: $1=[1]=[0,1]$.

[^continuant]: Kineski naziv potječe iz prijevoda knjige „Konkretna matematika” (《具体数学》) Zhanga Mingyaoa i Zhanga Fana, odjeljak 6.7.

[^heilbronn]: [H. Heilbronn, On the Average Length of a Class of Finite Continued Fractions, 1969.](https://link.springer.com/chapter/10.1007/978-1-4615-4819-5_7)

[^sqrt5]: Ovdje se ne smije unaprijed pretpostaviti da je neskrativi razlomak $\dfrac{p}{q}$ nužno konvergenta, iako Legendreov teorem pokazuje da $\dfrac{p}{q}$ doista može biti samo neka konvergenta. Za slučaj konvergenti tvrdnja se može dokazati polazeći od pogreške aproksimacije realnog broja konvergentama.

[^semi-range]: Različiti izvori mogu različito tretirati uključuje li raspon vrijednosti $t$ ovdje krajnje točke.

[^semiconvergent]: Za $t=0$ to treba shvatiti kao formalni verižni razlomak, što odgovara odrezivanju verižnog razlomka na pretposljednjem članu.

[^nose-stretching]: Taj naziv nije stručni termin. Vjerojatno je preveden iz ruske literature [ЦЕПНЫЕ ДРОБИ](https://old.mccme.ru/free-books/mmmf-lectures/book.14-full.pdf), odjeljak Алгоритм «вытягивания носов».

[^pgl2]: Ta svojstva pokazuju da je grupa svih razlomljenih linearnih transformacija izomorfna [projektivnoj linearnoj grupi](https://en.wikipedia.org/wiki/Projective_linear_group)  $PGL_2(\mathbf R)$.

[^period-surd]: Dokaz se nalazi u literaturi navedenoj na [stranici Wikipedije](https://en.wikipedia.org/wiki/Periodic_continued_fraction#Length_of_the_repeating_block).

[^continued-fraction-of-e]: Dokaz razvoja baze prirodnog logaritma $\mathrm{e}$ u verižni razlomak može se pronaći [ovdje](https://proofwiki.org/wiki/Continued_Fraction_Expansion_of_Euler%27s_Number).
