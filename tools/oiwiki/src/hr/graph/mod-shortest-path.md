---
title: Najkraći put po kongruencijama
---

Kad se pojave zadaci oblika „zadano je $n$ cijelih brojeva; koliko se drugih cijelih brojeva može složiti od tih $n$ brojeva (svaki od $n$ brojeva smije se uzeti više puta)”, zatim „zadano je $n$ cijelih brojeva; nađi najmanji (najveći) cijeli broj koji se od njih ne može složiti” ili „koliko najmanje pribrajanja treba da bi se dobio broj koji pri dijeljenju s $K$ daje ostatak $p$”, može se upotrijebiti metoda najkraćeg puta po kongruencijama (modular shortest path).

Najkraći put po kongruencijama koristi kongruencije za konstrukciju stanja, čime se može smanjiti prostorna složenost.

Po analogiji s [diferencijskim ograničenjima](./diff-constraints.md), stanja konstruirana pomoću kongruencija možemo promatrati kao vrhove u problemu najkraćeg puta iz jednog izvora. Prijelaz stanja u najkraćem putu po kongruencijama obično je oblika $f(i+y) = f(i) + y$, slično kao $f(v) = f(u) +edge(u,v)$ kod najkraćeg puta iz jednog izvora.

## Primjeri

### Primjer 1

???+ note "[P3403 Dizalo](https://www.luogu.com.cn/problem/P3403)"
    Sažetak zadatka: zadani su $x，y，z，h$; za koliko $k \in [1,h]$ postoje $a, b, c$ takvi da je $ax+by+cz=k$? ($0\leq a,b,c$, $1\le x,y,z\le 10^5$, $h\le 2^{63}-1$)

Bez smanjenja općenitosti pretpostavimo $x < y < z$.

Neka je $d_i$ najniži kat $p$ koji se može dosegnuti samo **operacijom 2** i **operacijom 3** uz uvjet $p\bmod x = i$, tj. najmanji broj kongruentan s $i$ modulo $x$ koji se može dobiti **operacijama 2** i **3**; njime računamo koliko brojeva iz te klase ostataka zadovoljava uvjet.

Dobivamo dva prijelaza:

-   $i \xrightarrow{y} (i+y) \bmod x$

-   $i \xrightarrow{z} (i+z) \bmod x$

Napomena: obično se za modul uzima najmanji od brojeva $a_i$, ovdje $x$, kako bi prostorna složenost bila što manja (najmanji sustav ostataka).

To zapravo odgovara dodavanju bridova u grafu za najkraći put:

`add(i, (i+y) % x, y)`

`add(i, (i+z) % x, z)`

Zatim treba samo izračunati $d_0, d_1, d_2, \dots, d_{x-1}$, a za to je dovoljan jedan prolaz algoritma najkraćeg puta.

??? example "Implementacija zasnovana na najkraćem putu"
    ```cpp
    --8<-- "docs/graph/code/mod-shortest-path/mod-shortest-path_1.cpp"
    ```

No zapravo nije nužno rješavati običan problem najkraćeg puta; uočimo dva posebna svojstva:

Prvo, postoje samo dvije težine bridova, a za svaki put, zbog komutativnosti zbrajanja, redoslijed kojim prolazimo bridove dviju težina nije bitan. Stoga možemo pokrenuti najkraći put dvaput, svaki put gradeći samo bridove jedne težine.

Drugo, u grafu sa samo jednom težinom bridova svaki vrh $u$ ima točno jedan ulazni brid (iz $(u-y) \bmod x$) i jedan izlazni brid (u $(u+y) \bmod x$), pa se cijeli graf nužno sastoji od nekoliko ciklusa. Štoviše, može se dokazati da ima točno $\gcd(x,y)$ ciklusa jednake duljine.

???+ note "Dokaz"
    Neka je $d=\gcd(x,y)$ te $x=da,y=db$, pa je $\gcd(a,b)=1$.
    
    Krenemo li iz $u$ i napravimo $k$ koraka, dolazimo u $(u+ky) \bmod x$. Ako se ciklus zatvori, tada je $ky \equiv 0 \pmod x$, odnosno $kb \equiv 0 \pmod a$.
    
    Budući da je $\gcd(a,b)=1$, najmanji je takav $k=a$, pa je duljina ciklusa $a = \dfrac{x}{d}$. Kako smo krenuli iz proizvoljnog vrha, svi ciklusi imaju jednaku duljinu, a ima ih $d$.

Osim toga, težine su pozitivne, pa nakon dva obilaska ciklusa više nije moguće relaksirati. Dovoljno je dakle jednostavno proći ciklus u petlji i ažurirati vrijednosti. Tako nismo ograničeni složenošću algoritma najkraćeg puta i postižemo $O(x)$.

Kao i kod diferencijskih ograničenja, ako je $\{a_1,a_2,\cdots,a_n\}$ rješenje, onda je i $\{a_1+d,a_2+d,\cdots,a_n+d\}$ rješenje; zato u ovom zadatku za izvor uzimamo $i=1$, jer je tada $dis_{1}=1$ u izvoru najmanja vrijednost u dopuštenom rasponu, pa je dobiveno rješenje također najmanje.

Odgovor je:

$$
\sum_{i=0}^{x-1}\left(\frac{h-d_i}{x} + 1\right)
$$

Pribrajamo 1 jer se i kat $d_i$ računa.

Pri implementaciji treba paziti da je raspon $h \leq 2^{63}-1$, pa početna vrijednost $d_i$ prije računanja najkraćeg puta mora biti barem $2^{63}$, što premašuje najveću vrijednost tipa `long long` u C++-u. Zato se može upotrijebiti `unsigned long long` ili prvo postaviti $h \gets h - 1$ i najniži kat označiti kao kat $0$; ostatak koda ne mijenja se.

??? example "Implementacija zasnovana na optimizaciji ciklusima"
    ```cpp
    --8<-- "docs/graph/code/mod-shortest-path/mod-shortest-path_2.cpp"
    ```

### Primjer 2

???+ note "[ARC084B Small Multiple](https://atcoder.jp/contests/arc084/tasks/arc084_b)"
    Sažetak zadatka: zadan je $n$; među višekratnicima broja $n$ nađi najmanji zbroj znamenki. ($1\le n\le 10^5$)

Zadatak se može riješiti potpunim ruksakom (unbounded knapsack) optimiranim cikličkom konvolucijom u vremenu $O(n\log^2 n)$, ali želimo linearni algoritam.

Uočimo da se svaki pozitivan cijeli broj može dobiti polazeći od $1$ i izvodeći, u nekom redoslijedu, operacije „pomnoži s $10$” i „dodaj $1$”, pri čemu je broj operacija „dodaj $1$” upravo zbroj znamenki tog broja. To upućuje na najkraći put.

Za sve $0\le k\le n-1$ povucimo brid težine $0$ iz $k$ u $10k$ i brid težine $1$ iz $k$ u $k+1$ (oznake vrhova uzimaju se modulo $n$).

Svaki višekratnik broja $n$ odgovara u ovom grafu nekom putu od vrha $1$ do vrha $0$, pa je dovoljno naći najkraći put od $1$ do $0$. Neki putovi nisu valjani (npr. $10$ uzastopnih bridova težine $1$), ali odgovori koje oni daju sigurno nisu bolji, pa ne utječu na rezultat.

Vremenska složenost je $O(n)$.

## Zadaci za vježbu

[Luogu P3403 Dizalo](https://www.luogu.com.cn/problem/P3403)

[Luogu P2662 Ograda za stoku](https://www.luogu.com.cn/problem/P2662)

[\[Nacionalni trening-tim\] Momoova jednadžba](https://www.luogu.com.cn/problem/P2371)

[„NOIP2018” Monetarni sustav](https://loj.ac/problem/2951)

[AGC057D - Sum Avoidance](https://atcoder.jp/contests/agc057/tasks/agc057_d)

[„THUPC 2023 kvalifikacije” Ruksak](https://loj.ac/p/6872)
