---
title: Lucasov teorem
---

Predznanje: [Faktorijel po modulu](./factorial.md)

## Uvod

U ovom se članku razmatra računanje velikih binomnih koeficijenata po modulu. Binomni koeficijent (broj kombinacija) jest izraz:

$$
\binom{n}{k} = \dfrac{n!}{k!(n-k)!}.
$$

Kada veličina problema nije velika, binomni se koeficijent može izračunati [rekurzivnom formulom](../combinatorics/combination.md#组合数性质--二项式推论) u vremenskoj složenosti $O(nk)$; po dovoljno velikom prostom modulu $p>n$ može se izračunati i u vremenu $O(n)$ računanjem faktorijela u brojniku i nazivniku. No kada je veličina problema vrlo velika ($n\sim 10^{18}$), te metode više nisu primjenjive.

Na temelju Lucasova teorema i njegova poopćenja u ovom se članku razmatra metoda kojom se binomni koeficijent može izračunati kada modul nije prevelik ($m \sim 10^6$). Preciznije, metoda se može primijeniti čim je zbroj svih potencija prostih brojeva u jedinstvenom rastavu modula $m=\prod p_i^{e_i}$ (tj. $\sum p_i^{e_i}$) reda veličine $10^6$, jer pretprocesiranje algoritma odgovara otprilike toj veličini.

## Lucasov teorem

Najprije razmotrimo slučaj u kojem je modul prost broj $p$. Tada vrijedi Lucasov teorem:

???+ note "Lucasov teorem"
    Za prost broj $p$ vrijedi
    
    $$
    \binom{n}{k}\equiv \binom{\lfloor n/p\rfloor}{\lfloor k/p\rfloor}\binom{n\bmod p}{k\bmod p}\pmod p.
    $$
    
    Pritom se za $n<k$ binomni koeficijent $\dbinom{n}{k}$ po dogovoru definira kao $0$.

??? note "Dokaz pomoću funkcija izvodnica"
    Promotrimo vrijednost $\displaystyle\binom{p}{n} \bmod p$. Budući da je
    
    $$
    \binom{p}{n} = \frac{p!}{n!(p-n)!},
    $$
    
    za $n\neq 0,p$ nazivnik ne sadrži faktor $p$, a brojnik sadrži faktor $p$, pa je razlomak nužno višekratnik broja $p$ i njegov je ostatak po modulu $p$ jednak $0$; za $n=0,p$ razlomak je jednak $1$. Stoga je
    
    $$
    \binom{p}{n} \equiv [n=0\lor n=p] \pmod p.
    $$
    
    Neka je $f(x) = ax^n + bx^m$. Općenito, prema [binomnom teoremu](../combinatorics/combination.md#二项式定理) i [malom Fermatovu teoremu](./fermat.md#费马小定理) vrijedi
    
    $$
    \begin{aligned}
    (f(x))^p 
    &= \left(ax^n + bx^m\right)^p \\
    &= \sum_{k=0}^p\binom{p}{k}(ax^n)^k(bx^m)^{p-k}\\
    &\equiv a^px^{pn} + b^px^{pm} \\
    &\equiv a(x^p)^n+b(x^p)^m\\
    &= f(x^p) \pmod p.
    \end{aligned}
    $$
    
    Ovdje kongruencija u trećem retku koristi prethodno pokazani zaključak da binomni koeficijent nije višekratnik broja $p$ samo za $k=0,p$.
    
    Pomoću tog zaključka promotrimo binomni razvoj:
    
    $$
    \begin{aligned}
    (1+x)^n &= (1+x)^{p\lfloor n/p\rfloor}(1+x)^{n\bmod p} \\
    &\equiv (1+x^p)^{\lfloor n/p\rfloor}(1+x)^{n\bmod p} \pmod p.
    \end{aligned}
    $$
    
    Na lijevoj strani jednakosti koeficijent uz član $x^k$ iznosi
    
    $$
    \binom{n}{k}\bmod p.
    $$
    
    Izračunajmo sada koeficijent uz član $x^k$ na desnoj strani. Stupnjevi članova prvog faktora nužno su višekratnici broja $p$, a stupnjevi članova drugog faktora nužno su manji od $p$; način da se $k$ rastavi na zbroj dvaju takvih dijelova jedinstven je, a daje ga dijeljenje s ostatkom: $k=p\lfloor k/p\rfloor +(k\bmod p)$. Stoga prvi faktor može pridonijeti samo svojim članom stupnja $p\lfloor k/p\rfloor$, a drugi faktor samo svojim članom stupnja $k\bmod p$. Dakle, koeficijent uz $x^k$ na desnoj strani jednak je umnošku koeficijenata članova kojima pridonose ta dva faktora:
    
    $$
    \binom{\lfloor n/p\rfloor}{\lfloor k/p\rfloor}\binom{n\bmod p}{k\bmod p}\bmod p.
    $$
    
    Izjednačavanjem koeficijenata obiju strana dobiva se Lucasov teorem.

??? note "Dokaz pomoću rezultata o faktorijelu po modulu"
    Ovdje dajemo dokaz temeljen na rezultatima o [faktorijelu po modulu](./factorial.md#slučaj-prostog-modula), kako bismo uspostavili vezu s metodom iz odjeljka o algoritmu exLucas u nastavku. Znamo da je binomni koeficijent
    
    $$
    \binom{n}{k} = \dfrac{n!}{k!(n-k)!}.
    $$
    
    Odvajanjem potencija broja $p$ u faktorijelu $n!$ od ostalih faktora dobiva se rastav:
    
    $$
    n! = p^{\nu_p(n!)}(n!)_p.
    $$
    
    Odatle dobivamo izraz za binomni koeficijent:
    
    $$
    \binom{n}{k} = p^{\nu_p(n!)-\nu_p(k!)-\nu_p((n-k)!)}\dfrac{(n!)_p}{(k!)_p((n-k)!)_p}.
    $$
    
    I eksponent $\nu_p(n!)$ i ostatak faktorijela $(n!)_p\bmod p$ zadovoljavaju rekurzivne formule:
    
    $$
    \begin{aligned}
    \nu_p(n!) &= \lfloor n/p\rfloor+\nu_p( \lfloor n/p\rfloor!),\\
    (n!)_p &\equiv (-1)^{\lfloor n/p\rfloor}\cdot (n\bmod p)!\cdot (\lfloor n/p\rfloor!)_p\pmod p.
    \end{aligned}
    $$
    
    Prva je posljedica Legendreove formule, a druga posljedica Wilsonova teorema.
    
    Uvrštavanjem rekurzivnih formula u izraz za binomni koeficijent i sređivanjem dobiva se:
    
    $$
    \begin{aligned}
    \binom{n}{k} &\equiv (-p)^{\lfloor n/p\rfloor-\lfloor k/p\rfloor-\lfloor(n-k)/p\rfloor}\cdot\dfrac{(n\bmod p)!}{(k\bmod p)!((n-k)\bmod p)!} \\
    &\quad \cdot p^{\nu_p(\lfloor n/p\rfloor!)-\nu_p(\lfloor k/p\rfloor!)-\nu_p(\lfloor(n-k)/p\rfloor!)}\dfrac{(\lfloor n/p\rfloor!)_p}{(\lfloor k/p\rfloor!)_p(\lfloor(n-k)/p\rfloor!)_p} \pmod p.
    \end{aligned}
    $$
    
    Promotrimo sada vrijednost izraza $\lfloor n/p\rfloor-\lfloor k/p\rfloor-\lfloor(n-k)/p\rfloor$. Budući da vrijedi
    
    $$
    \begin{aligned}
    n &= \lfloor n/p\rfloor p + (n\bmod p),\\
    k &= \lfloor k/p\rfloor p + (k\bmod p),\\
    n-k &= \lfloor (n-k)/p\rfloor p + ((n-k)\bmod p),\\
    \end{aligned}
    $$
    
    oduzimanjem druge i treće jednakosti od prve dobivamo
    
    $$
    (\lfloor n/p\rfloor-\lfloor k/p\rfloor-\lfloor(n-k)/p\rfloor)p = (k\bmod p)+((n-k)\bmod p)-(n\bmod p).
    $$
    
    Na desnoj strani zbroj prvih dvaju članova strogo je manji od $2p$, a treći član $n\bmod p$ upravo je ostatak zbroja prvih dvaju članova, pa desna strana mora biti nenegativna, ali manja od $2p$; budući da mora biti višekratnik broja $p$, ona je $0$ ili $p$. To znači da $\lfloor n/p\rfloor-\lfloor k/p\rfloor-\lfloor(n-k)/p\rfloor$ može biti samo $0$ ili $1$:
    
    -   Ako je $0$, tada vrijedi i $(n\bmod p) = (k\bmod p)+((n-k)\bmod p)$. Stoga je eksponent prvog faktora u gornjem izrazu $0$, pa je taj faktor jednak jedan; drugi je faktor upravo $\dbinom{n\bmod p}{k\bmod p}$; a za treći se faktor iz prethodnog razvoja (uočite da je sada $\lfloor(n-k)/p\rfloor=\lfloor n/p\rfloor-\lfloor k/p\rfloor$) vidi da je jednak $\dbinom{\lfloor n/p\rfloor}{\lfloor k/p\rfloor}$. U tom slučaju Lucasov teorem vrijedi;
    -   Ako je $1$, tada je eksponent prvog faktora $1$, pa je taj faktor jednak nuli, a time je i ostatak binomnog koeficijenta nula. Istodobno je i $\dbinom{n\bmod p}{k\bmod p}$ na desnoj strani jednakosti koju Lucasov teorem tvrdi nužno nula, jer tada nužno vrijedi $(n\bmod p)<(k\bmod p)$; u suprotnom bismo imali
    
        $$
        ((n-k)\bmod p) = p + (n\bmod p) - (k\bmod p) \ge p.
        $$
    
        To je očito u suprotnosti s definicijom ostatka.
    
    Objedinjavanjem obaju slučajeva dobiva se traženi Lucasov teorem. Ovaj dokaz pokazuje da su pri računanju binomnih koeficijenata po prostom modulu rezultati dobiveni Lucasovim teoremom i algoritmom exLucas ekvivalentni.

Lucasov teorem kaže da se, kada je modul prost broj $p$, računanje velikih binomnih koeficijenata može svesti na računanje binomnih koeficijenata manje veličine. Na desnoj strani prvi se binomni koeficijent može dalje rekurzivno računati sve dok ne bude $k=0$; drugi se binomni koeficijent može izračunati izravno ili unaprijed pretprocesirati. Zapisano u obliku koda:

???+ example "Skica"
    ```cpp
    long long Lucas(long long n, long long k, long long p) {
      if (k == 0) return 1;
      return (C(n % p, k % p, p) * Lucas(n / p, k / p, p)) % p;
    }
    ```

Ovdje `C(n, k, p)` služi za računanje binomnih koeficijenata male veličine.

Rekurzija se izvodi najviše $O(\log_p n)$ puta, pa je složenost algoritma $O(f(p)+g(p)\log_p n)$, gdje je $f(p)$ složenost pretprocesiranja binomnih koeficijenata, a $g(p)$ složenost računanja jednog binomnog koeficijenta.

### Referentna implementacija

Ovdje dana referentna implementacija u vremenu $O(p)$ pretprocesira faktorijele do $p$ i njihove inverze, nakon čega svaki binomni koeficijent računa u vremenu $O(1)$:

??? example "Referentna implementacija"
    ```cpp
    --8<-- "docs/math/code/lucas/lucas.cpp"
    ```

Vremenska složenost ove implementacije iznosi $O(p+T\log_p n)$, gdje je $T$ broj upita.

## Algoritam exLucas

Lucasov teorem zahtijeva da modul $p$ bude prost; za slučaj u kojem modul nije prost potreban je algoritam exLucas (prošireni Lucasov teorem). Unatoč imenu, taj algoritam u stvarnosti ne koristi Lucasov teorem. Njegov je ključni korak [računanje faktorijela po modulu koji je potencija prostog broja](./factorial.md). Drugi dokaz gore ukazao je na njegovu vezu s Lucasovim teoremom.

### Slučaj modula koji je potencija prostog broja

Najprije razmotrimo slučaj u kojem je modul potencija prostog broja $p^\alpha$. Odvajanjem potencija broja $p$ u faktorijelu $n!$ od ostalih faktora dobiva se rastav:

$$
n! = p^{\nu_p(n!)}(n!)_p.
$$

Ovdje je $\nu_p(n!)$ eksponent broja $p$ u rastavu $n!$ na proste faktore, a $(n!)_p$ je očito relativno prost s $p$. Stoga se binomni koeficijent može zapisati kao:

$$
\binom{n}{k} = p^{\nu_p(n!)-\nu_p(k!)-\nu_p((n-k)!)}\dfrac{(n!)_p}{(k!)_p((n-k)!)_p}.
$$

Vrijednosti $\nu_p(n!)$ i slične u formuli mogu se izračunati [Legendreovom formulom](./factorial.md#legendreova-formula), a $(n!)_p$ i slične [rekurzivnom relacijom](./factorial.md#slučaj-modula-koji-je-potencija-prostog-broja). Budući da su potonje relativno proste s $p^\alpha$, inverz umnoška u nazivniku može se izračunati [proširenim Euklidovim algoritmom](./inverse.md#扩展欧几里得算法). Time je problem riješen.

Uočite: ako je eksponent $\nu_p(n!)-\nu_p(k!)-\nu_p((n-k)!)\ge\alpha$, ostatak je nužno nula i nije potrebno dalje računati.

### Slučaj općeg modula

Za slučaj u kojem je $m$ opći složen broj dovoljno ga je najprije [rastaviti na proste faktore](./pollard-rho.md):

$$
m = p_1^{\alpha_1}p_2^{\alpha_2}\cdots p_s^{\alpha_s}.
$$

Zatim se zasebno izračunaju ostatci binomnog koeficijenta $\dbinom{n}{k}$ po modulima $p_i^{\alpha_i}$, čime se dobiva $s$ kongruencija:

$$
\begin{cases}
\dbinom{n}{k} \equiv r_1 &\pmod{p_1^{\alpha_1}}, \\
\dbinom{n}{k} \equiv r_2 &\pmod{p_2^{\alpha_2}}, \\
\quad\quad\cdots\\
\dbinom{n}{k} \equiv r_s &\pmod{p_s^{\alpha_s}}.
\end{cases}
$$

Na kraju se [kineskim teoremom o ostatcima](./crt.md) dobije ostatak po modulu $m$.

### Referentna implementacija

Na kraju dajemo referentnu implementaciju za ogledni zadatak [二项式系数 (Binomni koeficijent)](https://loj.ac/p/181).

??? example "Referentna implementacija"
    ```cpp
    --8<-- "docs/math/code/lucas/exlucas.cpp"
    ```

Ovaj algoritam pri pretprocesiranju rastavlja modul $m$ na potencije prostih brojeva, a zatim za svaki $p^\alpha$ pretprocesira umnožak svih prirodnih brojeva od $1$ do $p^\alpha$ koji nisu višekratnici broja $p$, kao i pripadni koeficijent za spajanje rezultata kineskim teoremom o ostatcima. Vremenska složenost pretprocesiranja iznosi $O(\sqrt{m}+\sum_ip_i^{\alpha_i})$. Složenost svakog upita iznosi $O(\log m+\sum_i\log_{p_i}n)$, pri čemu su dva člana složenosti redom složenost računanja inverza te složenost računanja eksponenta i ostatka faktorijela.

## Zadaci

-   [Luogu P3807【模板】卢卡斯定理 (Predložak: Lucasov teorem)](https://www.luogu.com.cn/problem/P3807)
-   [SDOI2010 古代猪文 (Drevni svinjski zapisi) – Lucasov teorem](https://loj.ac/problem/10229)
-   [Luogu P4720【模板】扩展卢卡斯 (Predložak: prošireni Lucasov teorem)](https://www.luogu.com.cn/problem/P4720)
-   [Ceizenpok’s formula](http://codeforces.com/gym/100633/problem/J)
