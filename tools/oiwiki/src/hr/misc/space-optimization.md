---
title: Uvod u optimizaciju prostora
---

Tehnike optimizacije prostora (memorije) u algoritamskim natjecanjima nisu osobito česte, no ipak ih vrijedi razmotriti.

## Informacijska entropija

Informacijska entropija opisuje donju granicu prostora potrebnog za pohranu podataka; ako je stvarno raspoloživi prostor manji od te granice, informacija se nužno gubi.

???+ note "Definicija"
    Za slučajnu varijablu $X$ informacijska entropija definira se kao
    
    $$
    H(X)=-\sum_{x}P(X=x)\log_2 P(X=x).
    $$

Baza logaritma u definiciji je $2$ zato što svaki bit informacije pohranjene u računalu ima samo $2$ moguće vrijednosti: $0$ i $1$.

Na primjer, neka $X$ ima uniformnu distribuciju na $\{1,2,\dots,n\}$; tada je njegova informacijska entropija

$$
H(X)=-\sum_{i=1}^n\frac{1}{n}\log_2\frac{1}{n}=\log_2 n,
$$

pa nam za pohranu cijelog broja od $1$ do $n$ treba barem $\log_2 n$ bitova.

### Primjer zadatka

???+ note "[\[WC2022\] 猜词 (Pogađanje riječi)](https://www.luogu.com.cn/problem/P8079)"
    Interaktivni zadatak: u ograničenom broju pokušaja trebate pogoditi riječ od 5 slova. Svaki pokušaj mora biti riječ koja postoji u zadanom rječniku. Ako pogodite, igra završava; nakon svakog pogrešnog pokušaja interaktor vraća koja su slova na ispravnom položaju te koja se slova pojavljuju u traženoj riječi, ali na pogrešnom položaju.
    
    ??? note "Rješenje"
        Vidi [Rješavanje Wordlea pomoću teorije informacija - 3Blue1Brown](https://www.bilibili.com/video/BV1zZ4y1k7Jw).
        
        Razmotrimo računanje informacijske entropije: očito, ako pri svakom pogađanju biramo riječ s visokom informacijskom entropijom, očekivani broj pokušaja bit će što manji.
        
        Budući da je u ovom zadatku prije pogađanja zadano prvo slovo odgovora, za svako početno slovo možemo unaprijed izračunati optimalan pokušaj.
        
        Osim toga, ako je preostalo malo riječi, možemo prednost dati riječima koje bi mogle biti odgovor, čime smanjujemo broj pokušaja.

## Uobičajene tehnike

### Izbjegavanje pohrane nepotrebnih podataka

Na primjer:

-   U [perzistentnom segment treeu](../ds/persistent-seg.md) jedna izmjena stvara samo $O(\log n)$ novih čvorova, pa ne moramo cijeli segment tree svake verzije pohraniti u potpunosti, nego je dovoljno zabilježiti nove čvorove.
-   Razmotrimo [pohranu grafa](../graph/save.md): za rijetke grafove matrica susjedstva pohranjuje mnoštvo beskorisnih vrijednosti $0$, pa se rijetki grafovi obično pohranjuju listama susjedstva.
-   Svaki element polja tipa `bool` zauzima jedan bajt; po potrebi ga možemo zamijeniti s `std::vector<bool>` ili [bitsetom](../lang/csl/bitset.md), u kojima svaki element zauzima samo jedan bit.
-   U [DP-u za ruksak](../dp/knapsack/basic.md), kod 0-1 ruksaka svako računanje DP vrijednosti koristi samo podatke iz prethodnog računanja, pa prostor možemo optimizirati rolajućim poljem (rolling array) i pamtiti samo trenutačne DP vrijednosti.

### Iskorištavanje svojstava podataka

Razmotrimo [strukturu disjunktnih skupova (DSU)](../ds/dsu.md) s kompresijom putova i heurističkim spajanjem (union by size); tradicionalno su potrebna dva polja: jedno za indeks roditelja, drugo za veličinu podstabla.

Uočimo:

1.  Uz kompresiju putova, za svako stablo u DSU-u trebamo pamtiti samo veličinu podstabla korijena.
2.  Roditelj korijena nužno je on sam.

Možemo iskoristiti svojstva predznačenih cijelih brojeva: negativnim brojevima označavamo korijene, a pozitivnima nekorijenske čvorove, pa nam je za DSU s kompresijom putova i heurističkim spajanjem dovoljno samo jedno polje.

???+ note "Implementacija"
    ```cpp
    --8<-- "docs/misc/code/space-optimization/space-optimization_1.cpp"
    ```

## Zadaci za vježbu

-   [QOJ 6669 Mapa](https://qoj.ac/problem/6669)
-   [\[SDOI/SXOI2022\] 无处存储 (Nema gdje pohraniti)](https://www.luogu.com.cn/problem/P8353)

## Literatura i dodatno čitanje

1.  Chen Zhixuan (陈知轩). 《浅谈信息学竞赛中的空间优化问题》 (O problemima optimizacije prostora u informatičkim natjecanjima). Rad kineskog nacionalnog pripremnog tima (国家集训队), 2022.
2.  [Information theory - Wikipedia](https://en.wikipedia.org/wiki/Information_theory)
3.  [浅谈信息论 (Kratko o teoriji informacija) - Luogu kolumna](https://www.luogu.com.cn/article/i65ca8i5)
