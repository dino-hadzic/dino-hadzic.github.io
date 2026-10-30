---
title: Kineski teorem o ostatcima
---

## Uvod

> Problem „nepoznatog broja stvari” (物不知数): Ima stvari, a ne zna se koliko ih je; broje li se po tri, ostanu dvije; broje li se po pet, ostanu tri; broje li se po sedam, ostanu dvije. Koliko je stvari?

Dakle, traži se cijeli broj koji zadovoljava sljedeće uvjete: pri dijeljenju s $3$ daje ostatak $2$, pri dijeljenju s $5$ daje ostatak $3$, a pri dijeljenju sa $7$ daje ostatak $2$.

Taj se problem prvi put pojavljuje u knjizi 《孙子算经》 (Sunzijev matematički priručnik), gdje je dan i konkretan postupak rješavanja. Matematičar Qin Jiushao iz dinastije Song dao je 1247. godine u prvom i drugom svesku, 《大衍类》 (Poglavlje o velikom proširenju), svoje knjige 《数书九章》 (Matematička rasprava u devet poglavlja) potpun i sustavan odgovor na problem „nepoznatog broja stvari”. Stihove s rješenjem gornjeg konkretnog problema dao je matematičar Cheng Dawei iz dinastije Ming u knjizi 《算法统宗》 (Sustavna rasprava o računanju):

> Tri čovjeka zajedno putuju – sedamdeset je rijetko; pet stabala šljive – dvadeset i jedna grana; sedam sinova na okupu – točno pola mjeseca; oduzmi sto i pet pa ćeš znati.

$2\times 70+3\times 21+2\times 15=233=2\times 105+23$, pa je odgovor $23$.

## Definicija

Kineski teorem o ostatcima (Chinese Remainder Theorem, CRT) omogućuje rješavanje sustava linearnih kongruencija s jednom nepoznanicom sljedećeg oblika (pri čemu su $n_1, n_2, \cdots, n_k$ u parovima relativno prosti):

$$
\begin{cases}
x &\equiv a_1 \pmod {n_1} \\
x &\equiv a_2 \pmod {n_2} \\
  &\vdots \\
x &\equiv a_k \pmod {n_k} \\
\end{cases}
$$

Gornji problem „nepoznatog broja stvari” primjer je takvog sustava linearnih kongruencija s jednom nepoznanicom.

## Postupak

1.  Izračunaj produkt $n$ svih modula;
2.  Za $i$-tu jednadžbu:
    1.  izračunaj $m_i=\frac{n}{n_i}$;
    2.  izračunaj [inverz](./inverse.md)  $m_i^{-1}$ broja $m_i$ modulo $n_i$;
    3.  izračunaj $c_i=m_im_i^{-1}$ (**bez uzimanja ostatka modulo $n_i$**).
3.  Jedinstveno rješenje sustava modulo $n$ jest: $x=\sum_{i=1}^k a_ic_i \pmod n$.

## Implementacija

=== "C++"
    ```cpp
    LL CRT(int k, LL* a, LL* r) {
      LL n = 1, ans = 0;
      for (int i = 1; i <= k; i++) n = n * r[i];
      for (int i = 1; i <= k; i++) {
        LL m = n / r[i], b, y;
        exgcd(m, r[i], b, y);  // b * m mod r[i] = 1
        ans = (ans + a[i] * m * b % n) % n;
      }
      return (ans % n + n) % n;
    }
    ```

=== "Python"
    ```python
    def CRT(k, a, r):
        n = 1
        ans = 0
        for i in range(1, k + 1):
            n = n * r[i]
        for i in range(1, k + 1):
            m = n // r[i]
            b = y = 0
            exgcd(m, r[i], b, y)  # b * m mod r[i] = 1
            ans = (ans + a[i] * m * b % n) % n
        return (ans % n + n) % n
    ```

## Dokaz

Trebamo dokazati da $x$ izračunat gornjim algoritmom za svaki $i=1,2,\cdots,k$ zadovoljava $x\equiv a_i \pmod {n_i}$.

Za $i\neq j$ vrijedi $m_j \equiv 0 \pmod {n_i}$, pa je $c_j \equiv m_j \equiv 0 \pmod {n_i}$. Osim toga, $c_i \equiv m_i \cdot (m_i^{-1} \bmod {n_i}) \equiv 1 \pmod {n_i}$, pa imamo:

$$
\begin{aligned}
x&\equiv \sum_{j=1}^k a_jc_j                      &\pmod {n_i} \\
 &\equiv a_ic_i                                   &\pmod {n_i} \\
 &\equiv a_i \cdot m_i \cdot (m^{-1}_i \bmod n_i) &\pmod {n_i} \\
 &\equiv a_i                                      &\pmod {n_i}
\end{aligned}
$$

Dakle, za svaki $i=1,2,\cdots,k$ $x$ dobiven gornjim algoritmom uvijek zadovoljava $x\equiv a_i \pmod{n_i}$, čime je dokazana ispravnost algoritma za rješavanje sustava kongruencija.

Budući da na ulazne $a_i$ nismo postavili nikakva posebna ograničenja, svakom ulazu $\{a_i\}$ odgovara jedno rješenje $x$. Osim toga, ako je $x\neq y$, uvijek postoji $i$ takav da $x$ i $y$ nisu kongruentni modulo $n_i$. Stoga je veza između niza koeficijenata $\{a_i\}$ i rješenja $x$ bijekcija, pa sustav uvijek ima jedinstveno rješenje.

## Objašnjenje

Pokažimo kako CRT rješava problem „nepoznatog broja stvari”.

1.  $n=3\times 5\times 7=105$;
2.  Tri čovjeka zajedno putuju – **sedamdeset** je rijetko: $n_1=3, m_1=n/n_1=35, m_1^{-1}\equiv 2\pmod 3$, pa je $c_1=35\times 2=70$;
3.  Pet stabala šljive – **dvadeset i jedna** grana: $n_2=5, m_2=n/n_2=21, m_2^{-1}\equiv 1\pmod 5$, pa je $c_2=21\times 1=21$;
4.  Sedam sinova na okupu – točno **pola mjeseca**: $n_3=7, m_3=n/n_3=15, m_3^{-1}\equiv 1\pmod 7$, pa je $c_3=15\times 1=15$;
5.  Stoga je jedinstveno rješenje sustava $x\equiv 2\times 70+3\times 21+2\times 15\equiv 233\equiv 23 \pmod {105}$. (Oduzmi **sto i pet** pa ćeš znati.)

## Garnerov algoritam

Druga je primjena CRT-a prikaz velikog cijelog broja pomoću skupa razmjerno malih prostih brojeva.

Na primjer, neka $a$ zadovoljava sljedeći sustav linearnih kongruencija i neka je $a < \prod_{i=1}^k p_i$ (gdje su $p_i$ prosti brojevi):

$$
\begin{cases}
a &\equiv a_1 \pmod {p_1} \\
a &\equiv a_2 \pmod {p_2} \\
  &\vdots \\
a &\equiv a_k \pmod {p_k} \\
\end{cases}
$$

Broj $a$ možemo prikazati izrazom sljedećeg oblika (koji se naziva prikaz broja $a$ u miješanoj bazi):

$$
a = x_1 + x_2 p_1 + x_3 p_1 p_2 + \ldots + x_k p_1 \ldots p_{k-1}
$$

**Garnerov algoritam** služi za računanje koeficijenata $x_1, \ldots, x_k$.

Neka je $r_{ij}$ [inverz](./inverse.md) broja $p_i$ modulo $p_j$:

$$
p_i \cdot r_{i,j} \equiv 1 \pmod{p_j}
$$

Uvrštavanjem $a$ u prvu jednadžbu dobivamo:

$$
a_1 \equiv x_1 \pmod{p_1}
$$

Uvrštavanjem u drugu jednadžbu dobivamo:

$$
a_2 \equiv x_1 + x_2 p_1 \pmod{p_2}
$$

Oduzimanjem $x_1$ od obiju strana i dijeljenjem s $p_1$ dobivamo

$$
\begin{aligned}
    a_2 - x_1           &\equiv x_2 p_1             &\pmod{p_2} \\
    (a_2 - x_1) r_{1,2} &\equiv x_2                 &\pmod{p_2} \\
    x_2                 &\equiv (a_2 - x_1) r_{1,2} &\pmod{p_2}
\end{aligned}
$$

Slično dobivamo:

$$
x_k=(\dots((a_k-x_1)r_{1,k}-x_2)r_{2,k})-\dots)r_{k-1,k} \bmod p_k
$$

??? note "Implementacija"
    === "C++"
        ```cpp
        for (int i = 0; i < k; ++i) {
          x[i] = a[i];
          for (int j = 0; j < i; ++j) {
            x[i] = r[j][i] * (x[i] - x[j]);
            x[i] = x[i] % p[i];
            if (x[i] < 0) x[i] += p[i];
          }
        }
        ```
    
    === "Python"
        ```python
        for i in range(0, k):
            x[i] = a[i]
            for j in range(0, i):
                x[i] = r[j][i] * (x[i] - x[j])
                x[i] = x[i] % p[i]
                if x[i] < 0:
                    x[i] = x[i] + p[i]
        ```

Vremenska složenost tog algoritma jest $O(k^2)$. Zapravo Garnerov algoritam ne zahtijeva da moduli budu prosti, nego samo da budu u parovima relativno prosti; imamo sljedeći pseudokod:

$$
\begin{array}{ll}
&\textbf{Chinese Remainder Algorithm }\operatorname{cra}(\mathbf{v}, \mathbf{m})\text{:} \\
&\textbf{Input}\text{: }\mathbf{m}=(m_0,m_1,\dots ,m_{n-1})\text{, }m_i\in\mathbb{Z}^+\land\gcd(m_i,m_j)=1\text{ for all } i\neq j\text{,} \\
&\qquad \mathbf{v}=(v_0,\dots ,v_{n-1}) \text{ where }v_i=x\bmod m_i\text{.} \\
&\textbf{Output}\text{: }x\bmod{\prod_{i=0}^{n-1} m_i}\text{.} \\
1&\qquad \textbf{for }i\text{ from }1\text{ to }(n-1)\textbf{ do} \\
2&\qquad \qquad C_i\gets \left(\prod_{j=0}^{i-1}m_j\right)^{-1}\bmod{m_i} \\
3&\qquad x\gets v_0 \\
4&\qquad \textbf{for }i\text{ from }1\text{ to }(n-1)\textbf{ do} \\
5&\qquad \qquad u\gets (v_i-x)\cdot C_i\bmod{m_i} \\
6&\qquad \qquad x\gets x+u\prod_{j=0}^{i-1}m_j \\
7&\qquad \textbf{return }(x)
\end{array}
$$

Može se primijetiti da račun u šestom retku odgovara gore opisanom prikazu u miješanoj bazi.

## Primjene

U nekim zadatcima prebrojavanja ili teorije brojeva, radi produljenja koda, povećanja težine ili iz nekih drugih razloga, zadani modul **nije prost broj**!

No rastavom na proste faktore vidi se da nema kvadratnih faktora, tj. da je taj modul produkt međusobno različitih prostih brojeva.

Tada možemo računati zasebno po svakom od tih modula i na kraju odgovore spojiti CRT-om.

Sljedeći je zadatak dobar primjer.

???+ note "[Luogu P2480 \[SDOI2010\] 古代猪文 (Drevni svinjski spisi)](https://www.luogu.com.cn/problem/P2480)"
    Zadani su $G,n$ ($1 \leq G,n \leq 10^9$); treba izračunati:
    
    $$
    G^{\sum_{k\mid n}\binom{n}{k}} \bmod 999~911~659
    $$

Najprije, kad je $G=999~911~659$, traženi je rezultat očito $0$.

Inače, prema [Eulerovu teoremu](./fermat.md), traženi je rezultat:

$$
G^{\sum_{k\mid n}\binom{n}{k} \bmod 999~911~658} \bmod 999~911~659
$$

Sada razmotrimo kako izračunati:

$$
\sum_{k\mid n}\binom{n}{k} \bmod 999~911~658
$$

Budući da $999~911~658$ nije prost broj, ne možemo jamčiti da $\forall x \in [1,999~911~657]$ postoji inverz od $x$, pa gornji izraz ne možemo izravno izračunati.

Uočimo da je $999~911~658=2 \times 3 \times 4679 \times 35617$, gdje se svaki prosti faktor pojavljuje s najvećim eksponentom jedan, pa možemo zasebno izračunati $\sum_{k\mid n}\binom{n}{k}$ modulo svaki od prostih brojeva $2$, $3$, $4679$, $35617$ i na kraju odgovore spojiti kineskim teoremom o ostatcima.

Drugim riječima, zapravo tražimo rješenje sljedećeg sustava linearnih kongruencija:

$$
\begin{cases}
x \equiv a_1 \pmod 2\\
x \equiv a_2 \pmod 3\\
x \equiv a_3 \pmod {4679}\\
x \equiv a_4 \pmod {35617}
\end{cases}
$$

A za računanje binomnog koeficijenta modulo manji prost broj može se iskoristiti [Lucasov teorem](./lucas.md).

## Proširenje: slučaj kad moduli nisu relativno prosti

### Dvije jednadžbe

Neka su dvije jednadžbe $x\equiv a_1 \pmod {m_1}$ i $x\equiv a_2 \pmod {m_2}$;

Pretvorimo ih u diofantsku jednadžbu: $x=m_1p+a_1=m_2q+a_2$, gdje su $p, q$ cijeli brojevi; tada je $m_1p-m_2q=a_2-a_1$.

Prema [Bézoutovu teoremu](./bezouts.md), kad $a_2-a_1$ nije djeljiv s $\gcd(m_1,m_2)$, rješenja nema;

Inače se [proširenim Euklidovim algoritmom](./gcd.md) može dobiti jedno rješenje $(p, q)$;

Tada je rješenje sustava sastavljenog od izvorne dvije kongruencije $x\equiv b\pmod M$, gdje je $b=m_1p+a_1$, a $M=\text{lcm}(m_1, m_2)$.

### Više jednadžbi

Dovoljno ih je gornjom metodom spajati dvije po dvije.

## Zadaci za vježbu

-   [【模板】中国剩余定理（CRT）/曹冲养猪 (Predložak: kineski teorem o ostatcima (CRT) / Cao Chong uzgaja svinje)](https://www.luogu.com.cn/problem/P1495)
-   [【模板】扩展中国剩余定理 (Predložak: prošireni kineski teorem o ostatcima)](https://www.luogu.com.cn/problem/P4777)
-   [「NOI2018」屠龙勇士 (Ubojica zmajeva)](https://uoj.ac/problem/396)
-   [「TJOI2009」猜数字 (Pogađanje brojeva)](https://www.luogu.com.cn/problem/P3868)

    **Ova je stranica dijelom prevedena iz članka [Китайская теорема об остатках](http://e-maxx.ru/algo/chinese_theorem) i njegova engleskog prijevoda [Chinese Remainder Theorem](https://cp-algorithms.com/algebra/chinese-remainder-theorem.html). Ruska je inačica objavljena pod licencijom Public Domain + Leave a Link, a engleska pod CC-BY-SA 4.0.**
