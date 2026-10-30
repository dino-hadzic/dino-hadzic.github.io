---
title: Blokovsko dijeljenje po cjelobrojnom kvocijentu
---

Blokovsko dijeljenje po cjelobrojnom kvocijentu (number-theoretic blocking) omogućuje brzo računanje suma oblika

$$
\sum_{i=1}^nf(i)g\left(\left\lfloor\dfrac ni\right\rfloor\right)
$$

Ako se $\sum_{i=l}^{r}f(i)$ može izračunati u vremenu $O(1)$ ili su prefiksne sume (prefix sums) funkcije $f$ već predračunate, blokovsko dijeljenje po cjelobrojnom kvocijentu može izračunati vrijednost gornje sume u vremenu $O(\sqrt{n})$.

Blokovsko dijeljenje po cjelobrojnom kvocijentu često se kombinira s tehnikama poput [Möbiusove inverzije](./mobius.md).

## Ideja

Najprije ćemo ideju blokovskog dijeljenja po cjelobrojnom kvocijentu objasniti na jednostavnom primjeru. Pretpostavimo da treba prebrojati cjelobrojne točke ispod hiperbole prikazane na slici:

![Cjelobrojne točke ispod hiperbole](./images/sqrt-decomposition.svg)

To je isto što i računanje sume:

$$
\sum_{i=1}^{11}\left\lfloor\dfrac{11}{i}\right\rfloor.
$$

To je poseban slučaj gore navedene sume uz $f(k)=1,~g(k)=k$.

Najjednostavniji je postupak, dakako, računati stupac po stupac i zbrajati, ali tada treba izračunati broj cjelobrojnih točaka u svakom od stupaca $i=1,2,\cdots,11$. Promatranjem slike može se uočiti da se ti stupci točaka mogu podijeliti u $5$ blokova, a unutar svakog bloka stupci točaka imaju jednaku visinu i tvore pravokutnu rešetku točaka. Stoga, ako znamo širine tih blokova, prebrojavanje možemo brzo dovršiti računajući veličine tih pravokutnih blokova.

To je osnovna ideja blokovskog dijeljenja po cjelobrojnom kvocijentu.

## Svojstva

U ovom odjeljku razmatramo nekoliko tvrdnji o podjeli cjelobrojnih točaka ispod hiperbole $y = \dfrac{n}{x}$ u blokove. Konkretno, cijele brojeve između $1\sim n$ treba podijeliti u blokove prema vrijednosti $\left\lfloor\dfrac{n}{i}\right\rfloor$. Neka je

$$
D(n) = \left\{\left\lfloor\dfrac{n}{i}\right\rfloor : 1 \le i \le n,~i\in\mathbf N_+\right\}.
$$

To je skup svih mogućih vrijednosti izraza $\left\lfloor\dfrac{n}{i}\right\rfloor$.

Prvo, takvih različitih vrijednosti ima samo $O(\sqrt{n})$. Stoga blokovsko dijeljenje po cjelobrojnom kvocijentu daje samo $O(\sqrt{n})$ blokova.

???+ note "Svojstvo 1"
    $|D(n)|\le 2\sqrt{n}$.

??? note "Dokaz"
    Razlikujemo dva slučaja:
    
    -   Kad je $i\le\sqrt{n}$, $i$ poprima najviše $\sqrt{n}$ vrijednosti, pa i $\left\lfloor\dfrac{n}{i}\right\rfloor$ poprima najviše $\sqrt{n}$ vrijednosti.
    -   Kad je $i>\sqrt{n}$, $\left\lfloor\dfrac{n}{i}\right\rfloor \le\dfrac{n}{i} < \sqrt{n}$ također poprima najviše $\sqrt{n}$ vrijednosti.
    
    Dakle, ukupan broj svih mogućih vrijednosti je $|D(n)|\le 2\sqrt{n}$.

Pažljivijom analizom skup $D(n)$ i njegova veličina mogu se zapravo precizno opisati.

???+ note "Svojstvo 2"
    Neka je $s = \lfloor\sqrt{n}\rfloor$. Elementi skupa $D(n)$, poredani od najmanjeg prema najvećem, jesu
    
    $$
    1 < 2 < \cdots < s-1 < s \le \left\lfloor\dfrac{n}{s}\right\rfloor < \left\lfloor\dfrac{n}{s-1}\right\rfloor < \cdots < \left\lfloor\dfrac{n}{2}\right\rfloor < \left\lfloor\dfrac{n}{1}\right\rfloor = n.
    $$
    
    Nadalje, $|D(n)| = \lfloor \sqrt{4n+1}\rfloor - 1$.

??? note "Dokaz"
    Najprije, za $1 \le i \le s$ može se dokazati $\left\lfloor\dfrac{n}{\lfloor n/i\rfloor}\right\rfloor = i$. Neka je $d = \left\lfloor\dfrac{n}{i}\right\rfloor$; treba dokazati $\left\lfloor\dfrac{n}{d}\right\rfloor = i$. Zapisano nejednakostima, to znači da iz poznatog $d \le \dfrac{n}{i} < d + 1$ treba dokazati $i \le \dfrac{n}{d} < i + 1$. Poznati se uvjet može zapisati kao $i\le\dfrac{n}{d} < i + \dfrac{i}{d}$, pa je dovoljno dokazati $\dfrac{i}{d} \le 1$, tj. $i \le d = \left\lfloor\dfrac{n}{i}\right\rfloor$. To je ekvivalentno s $i \le \dfrac{n}{i}$, što vrijedi za sve $1 \le i \le s \le \sqrt{n}$.
    
    Taj rezultat zapravo pokazuje da preslikavanje $i \mapsto \left\lfloor\dfrac{n}{i}\right\rfloor$ čini bijekciju između skupa $\{i:1\le i \le s\}$ i skupa $\left\{\left\lfloor\dfrac{n}{i}\right\rfloor: 1\le i\le s\right\}$. Budući da su svi $i$ međusobno različiti, i vrijednosti $\left\lfloor\dfrac{n}{i}\right\rfloor$ međusobno su različite. Jedini elementi tih dvaju skupova koji se mogu podudarati jesu $s$ i $\left\lfloor\dfrac{n}{s}\right\rfloor$. Stoga je $|D(n)|=2s - \left[s = \lfloor n/s\rfloor\right]$.
    
    Da bismo dobili konačni izraz za $|D(n)|$, treba ispitati kada vrijedi $s = \left\lfloor\dfrac{n}{s}\right\rfloor$.
    
    -   Kad je $s = \left\lfloor\dfrac{n}{s}\right\rfloor$, uvijek vrijedi $s \le \dfrac{n}{s} < s + 1$, tj. $s^2 \le n < s^2+s$. Tada je $4s^2 + 1 \le 4n + 1 < 4s^2+4s+1 = (2s+1)^2$. Budući da je $4n+1$ nužno neparan, lijeva se strana može ekvivalentno olabaviti na $4s^2$, pa je taj uvjet ekvivalentan s $2s \le \sqrt{4n+1} < 2s+1$, tj. $\lfloor \sqrt{4n+1}\rfloor = 2s$.
    -   Kad je $s < \left\lfloor\dfrac{n}{s}\right\rfloor$, uvijek vrijedi $s + 1 \le \dfrac{n}{s}$, tj. $s^2 + s\le n$. Budući da je još $n < (s+1)^2$, imamo $s^2 + s\le n < (s+1)^2$. To je ekvivalentno s $(2s+1)^2\le 4n+1 < 4(s+1)^2+1$. Ponovno iskoristivši to da je $4n+1$ neparan, desna se strana može ekvivalentno pooštriti na $4(s+1)^2$, pa je taj uvjet ekvivalentan s $2s+1\le\sqrt{4n+1} < 2s+2$, tj. $\lfloor \sqrt{4n+1}\rfloor = 2s+1$.
    
    Objedinjavanjem tih dvaju slučajeva dobivamo da vrijedi $|D(n)| = \lfloor \sqrt{4n+1}\rfloor - 1$.

Zatim, lijevi i desni kraj pojedinog bloka lako je odrediti.

???+ note "Svojstvo 3"
    Za $d\in D(n)$, svi cijeli brojevi $i$ koji zadovoljavaju $\left\lfloor\dfrac{n}{i}\right\rfloor=d$ nalaze se u rasponu
    
    $$
    \left\lfloor\dfrac{n}{d+1}\right\rfloor + 1\le i \le \left\lfloor\dfrac{n}{d}\right\rfloor.
    $$

??? note "Dokaz"
    Budući da je $\left\lfloor\dfrac{n}{i}\right\rfloor=d$ isto što i nejednakost
    
    $$
    d\le \dfrac{n}{i} < d+1.
    $$
    
    To je nadalje ekvivalentno s
    
    $$
    \dfrac{n}{d+1} < i\le \dfrac{n}{d}.
    $$
    
    Iskoristivši to da je $i\in\mathbf N_+$, na tu nejednakost možemo primijeniti zaokruživanje na cijeli broj, pa je ona ekvivalentna s
    
    $$
    \left\lfloor\dfrac{n}{d+1}\right\rfloor + 1 \le i\le \left\lfloor\dfrac{n}{d}\right\rfloor.
    $$

To svojstvo odražava i simetriju slike: skup desnih krajeva svih blokova (zelene točke na gornjoj slici) upravo je $D(n)$. To je lako razumjeti jer je cijela slika simetrična s obzirom na pravac $y=x$.

Osim tih svojstava, skup $D(n)$ ima i lijepo rekurzivno svojstvo:

???+ note "Svojstvo 4"
    Za $m\in D(n)$ vrijedi $D(m)\subseteq D(n)$.

??? note "Dokaz"
    Neka je $m = \left\lfloor\dfrac{n}{k}\right\rfloor$. Tada, budući da za sve $i\in\mathbf N_+$ vrijedi
    
    $$
    \left\lfloor\dfrac{m}{i}\right\rfloor = \left\lfloor\dfrac{\lfloor n/k\rfloor}{i}\right\rfloor = \left\lfloor\dfrac{n}{ki}\right\rfloor \in D(n),
    $$
    
    slijedi $D(m)\subseteq D(n)$. Pritom druga jednakost koristi svojstvo [funkcije zaokruživanja](./basic.md#funkcije-pod-i-strop) za ugniježđene razlomke.

Već je spomenuto da je $D(n)$ i skup vrijednosti $\left\lfloor\dfrac{n}{i}\right\rfloor$ po blokovima i skup desnih krajeva blokova. To znači da, ako blokovsko dijeljenje po cjelobrojnom kvocijentu primjenjujemo rekurzivno (tj. vrijednost funkcije u $n$ ovisi o njezinim vrijednostima u $m\in D(n)\setminus\{n\}$), skup vrijednosti i skup desnih krajeva koji se pojavljuju tijekom cijelog računanja zapravo su upravo $D(n)$. Tipičan je primjer [Du sito](./hyperbola.md#du-sito).

## Postupak

Iz tvrdnji iz prethodnog odjeljka dobiva se konkretan postupak blokovskog dijeljenja po cjelobrojnom kvocijentu.

Da bismo izračunali vrijednost sume

$$
\sum_{i=1}^nf(i)g\left(\left\lfloor\dfrac ni\right\rfloor\right)
$$

indekse $i=1,2,\cdots,n$ možemo podijeliti u blokove prema vrijednosti $\left\lfloor\dfrac ni\right\rfloor$. Budući da indeksi s istom vrijednošću $\left\lfloor\dfrac ni\right\rfloor$ čine segment uzastopnih cijelih brojeva $[l,r]$, vrijednost sume na tom bloku iznosi

$$
\left(\sum_{i=l}^rf(i)\right)\cdot g\left(\left\lfloor\dfrac nl\right\rfloor\right).
$$

Da bi se ta suma brzo izračunala, obično je potrebno moći brzo izračunati lijevu sumu po $f$. Ponekad je izraz za tu sumu poznat, pa se jedno računanje obavi u vremenu $O(1)$; ponekad se mogu predračunati njezine prefiksne sume, pa se jedan upit i dalje obavi u vremenu $O(1)$.

Pri redom računanju lijevih i desnih krajeva svakog bloka, lijevi kraj $l$ trenutnog bloka jednak je desnom kraju prethodnog bloka uvećanom za $1$, a desni kraj trenutnog bloka jednak je $\left\lfloor\dfrac n{\lfloor n/l\rfloor}\right\rfloor$. Iz toga se dobiva sljedeći pseudokod:

$$
\begin{array}{l}
\textbf{Algorithm }\text{Sum}(f,g,n):\\
\textbf{Input. }n,~s(k)=\sum_{i=1}^kf(i),~g(k).\\
\textbf{Output. }S(n) = \sum_{i=1}^nf(i)g(\lfloor n/i\rfloor).\\
\textbf{Method.}\\
\begin{array}{ll}
1 & l \gets 1\\
2 & \textit{result} \gets 0 \\
3 & \textbf{while } l \leq n \textbf{ do}\\
4 & \qquad r \gets \left\lfloor \dfrac{n}{\lfloor n/l \rfloor} \right\rfloor\\
5 & \qquad \textit{result} \gets \textit{result} + (s(r)-s(l-1))\cdot g\left(\left\lfloor \dfrac{n}{l} \right\rfloor\right)\\
6 & \qquad l \gets r+1\\
7 & \textbf{end while}\\
8 & \textbf{return }\textit{result}
\end{array}
\end{array}
$$

Pretpostavimo li da je vremenska složenost jednog računanja $s(\cdot)$ jednaka $O(1)$, vremenska je složenost cijelog postupka $O(\sqrt{n})$.

## Proširenja

Dosad smo razmatrali najčešći i najosnovniji oblik blokovskog dijeljenja po cjelobrojnom kvocijentu. U ovom odjeljku razmatramo njegove proširene oblike.

### Blokovsko dijeljenje s gornjim cijelim dijelom

Blokovsko dijeljenje po cjelobrojnom kvocijentu može se koristiti i za računanje suma koje sadrže gornji cijeli dio (zaokruživanje naviše):

$$
\sum_{i=1}^nf(i)g\left(\left\lceil\dfrac ni\right\rceil\right).
$$

Budući da je $\left\lceil\dfrac ni\right\rceil = \left\lfloor\dfrac {n-1}i\right\rfloor + 1$, ta se suma može svesti na slučaj s donjim cijelim dijelom:

$$
f(n)g(1) + \sum_{i=1}^{n-1}f(i)g\left(\left\lfloor\dfrac {n-1}i\right\rfloor + 1\right).
$$

Uočite da se gornja granica sumacije promijenila te da se član za $i=n$ pojavljuje zasebno.

### Višedimenzionalno blokovsko dijeljenje

Blokovsko dijeljenje po cjelobrojnom kvocijentu može se koristiti i za sume koje sadrže više od jednog izraza s cijelim dijelom:

$$
\sum_{i=1}^{n}f(i)g\left(\left\lfloor\dfrac {n_1}i\right\rfloor,\left\lfloor\dfrac {n_2}i\right\rfloor,\cdots,\left\lfloor\dfrac {n_m}i\right\rfloor\right).
$$

Pritom obično vrijedi $n\le\min\{n_1,n_2,\cdots,n_m\}$; inače treba zasebno obraditi slučaj kad je neki $\lfloor n_j/i\rfloor=0$. Da bismo primijenili ideju blokovskog dijeljenja, treba osigurati da se unutar svakog bloka vrijednosti svih izraza $\left\lfloor\dfrac {n_1}i\right\rfloor,\left\lfloor\dfrac {n_2}i\right\rfloor,\cdots,\left\lfloor\dfrac {n_m}i\right\rfloor$ ne mijenjaju, odnosno višedimenzionalni blok treba biti presjek svih jednodimenzionalnih blokova. Zato je za poznati lijevi kraj $l$ pripadni desni kraj

$$
\min\left\{\left\lfloor\dfrac {n_1}{\lfloor n_1/l\rfloor}\right\rfloor,\left\lfloor\dfrac {n_2}{\lfloor n_2/l\rfloor}\right\rfloor,\cdots,\left\lfloor\dfrac {n_m}{\lfloor n_m/l\rfloor}\right\rfloor\right\}.
$$

Drugim riječima, kao desni kraj višedimenzionalnog bloka uzima se minimum desnih krajeva svih jednodimenzionalnih blokova. To se može razumjeti pomoću sljedeće slike:

![Ilustracija višedimenzionalnog blokovskog dijeljenja](./images/n-dimension-sqrt-decomposition.svg)

Najčešći je dvodimenzionalni oblik; tada se u gornjem pseudokodu $r \gets \left\lfloor \dfrac{n}{\lfloor n/l \rfloor}\right\rfloor$ zamjenjuje s

$$
r \gets \min\left\{\left\lfloor \dfrac{n_1}{\lfloor n_1/l \rfloor}\right\rfloor,\left\lfloor \dfrac{n_2}{\lfloor n_2/l \rfloor}\right\rfloor\right\}.
$$

### Blokovsko dijeljenje s proizvoljnim eksponentima

Blokovsko dijeljenje po cjelobrojnom kvocijentu može se koristiti za računanje suma s izrazima s cijelim dijelom koji sadrže proizvoljne eksponente:

$$
\sum_{i=1}^{\lfloor n^{\alpha/\beta}\rfloor}f(i)g\left(\left\lfloor\dfrac {n^\alpha}{i^\beta}\right\rfloor\right).
$$

Pritom su $\alpha,\beta$ pozitivni realni brojevi. U osnovnom obliku razmatranom u ovom tekstu vrijedi $\alpha=\beta=1$.

???+ note "Svojstvo"
    Za pozitivan cijeli broj $n$ i pozitivne realne brojeve $\alpha, \beta$ neka je
    
    $$
    D(n,\alpha,\beta) = \left\{\left\lfloor\dfrac{n^\alpha}{i^\beta}\right\rfloor: i=1,2,\cdots,\lfloor n^{\alpha/\beta}\rfloor\right\}.
    $$
    
    Tada vrijedi
    
    1.  $|D(n,\alpha,\beta)|\le 2n^{\alpha/(1+\beta)}$.
    2.  Za $d\in D(n,\alpha,\beta)$, vrijednosti $i$ za koje vrijedi $\left\lfloor\dfrac{n^\alpha}{i^\beta}\right\rfloor=d$ nalaze se u rasponu
    
        $$
        \left\lfloor\dfrac{n^{\alpha/\beta}}{(d+1)^{1/\beta}}\right\rfloor + 1\le i \le \left\lfloor\dfrac{n^{\alpha/\beta}}{d^{1/\beta}}\right\rfloor.
        $$

??? note "Dokaz"
    Za prvu tvrdnju razlikujemo dva slučaja:
    
    -   Kad je $i\le \dfrac{n^\alpha}{i^\beta}$, vrijedi $i\le n^{\alpha/(1+\beta)}$, pa $\left\lfloor\dfrac{n^\alpha}{i^\beta}\right\rfloor$ poprima najviše $n^{\alpha/(1+\beta)}$ vrijednosti.
    -   Kad je $i > \dfrac{n^\alpha}{i^\beta}$, vrijedi $i> n^{\alpha/(1+\beta)}$, a odatle $\dfrac{n^\alpha}{i^\beta} < n^{\alpha/(1+\beta)}$, pa i $\left\lfloor\dfrac{n^\alpha}{i^\beta}\right\rfloor$ poprima najviše $n^{\alpha/(1+\beta)}$ vrijednosti.
    
    Objedinjavanjem obaju slučajeva dobivamo $|D(n,\alpha,\beta)|\le 2n^{\alpha/(1+\beta)}$.
    
    Za drugu tvrdnju, $\left\lfloor\dfrac{n^\alpha}{i^\beta}\right\rfloor=d$ ekvivalentno je s
    
    $$
    d \le \dfrac{n^\alpha}{i^\beta} < d+1 \iff \dfrac{n^{\alpha/\beta}}{(d+1)^{1/\beta}} < i \le \dfrac{n^{\alpha/\beta}}{d^{1/\beta}}.
    $$
    
    Zaokruživanjem te nejednakosti na cijele brojeve dobiva se druga tvrdnja.

Pomoću tih svojstava blokovsko dijeljenje po cjelobrojnom kvocijentu s proizvoljnim eksponentima može se provesti u vremenskoj složenosti $O(n^{\alpha/(1+\beta)})$.

???+ example "Primjer"
    Na primjer, sljedeća suma za $\alpha=\beta=1/2$
    
    $$
    \sum_{i=1}^nf(i)g\left(\left\lfloor\sqrt{\dfrac {n}{i}}\right\rfloor\right),
    $$
    
    može se blokovskim dijeljenjem riješiti u vremenu $O(n^{1/3})$. Kad je poznat lijevi kraj bloka $l$, desni se kraj može izračunati kao $r=\left\lfloor\dfrac{n}{\lfloor\sqrt{n/l}\rfloor^2}\right\rfloor$.

## Primjeri zadataka

???+ example "[UVa11526 H(n)](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=27&page=show_problem&problem=2521)"
    Zadano je $T$ skupova podataka, u svakom po jedan cijeli broj $n$. Za svaki skup podataka ispišite $\sum_{i=1}^n\left\lfloor\dfrac ni\right\rfloor$.

??? note "Rješenje"
    Prema prethodnoj analizi, svaki blok s jednakom vrijednošću $\left\lfloor\dfrac ni\right\rfloor$ može se izračunati odjednom. Vremenska složenost je $O(T\sqrt n)$.

??? note "Implementacija"
    ```cpp
    --8<-- "docs/math/code/sqrt-decomposition/sqrt-decomposition_1.cpp"
    ```

???+ example "[Codeforces 1954E Chain Reaction](https://codeforces.com/contest/1954/problem/E)"
    U redu stoji $n$ čudovišta, a početno zdravlje svakog čudovišta je $a_i$. Jedan napad smanjuje zdravlje neprekinutog niza živih čudovišta za $k$; čudovište sa zdravljem ne većim od $0$ smatra se mrtvim. Za svaki $k$ odredite broj napada potrebnih da se ubiju sva čudovišta. Pritom je $n,a_i\leq 10^5$.

??? note "Rješenje"
    Neka je $a_0=0$. Pretpostavimo da je za ubijanje svih prvih $(i-1)$ čudovišta potrebno $T(k,i-1)$ napada, a zdravlje $i$-tog čudovišta je $a_i$. Budući da je pri ubijanju $(i-1)$-og čudovišta potrebno napasti ga $\lceil a_{i-1}/k\rceil$ puta, a svi se ti napadi mogu protegnuti i na $i$-to čudovište, za ubijanje $i$-tog čudovišta potrebno je još samo $\max\{0,\lceil a_i/k\rceil-\lceil a_{i-1}/k\rceil\}$ napada. Stoga je ukupan broj napada
    
    $$
    T(k,n)=\sum_{i=1}^n\max\left\{0,\left\lceil\dfrac{a_i}{k}\right\rceil-\left\lceil\dfrac{a_{i-1}}{k}\right\rceil\right\}.
    $$
    
    Budući da su $n,k$ u zadatku prilično veliki, računanje te sume zasebno za svaki $k$ nije izvedivo. Možemo za svaki $i=1,2,\cdots,n$ održavati niz $\{T(k,i)\}_k$. Početno neka je $T(k,0)\equiv 0$. Pretpostavimo da je niz $\{T(k,i-1)\}_k$ poznat i razmotrimo kako ga izmijeniti da bismo dobili niz $\{T(k,i)\}_k$. Prema prethodnoj analizi, dovoljno je $k$-ti član niza uvećati za $\max\left\{0,\left\lceil\dfrac{a_i}{k}\right\rceil-\left\lceil\dfrac{a_{i-1}}{k}\right\rceil\right\}$. Pomoću dvodimenzionalnog blokovskog dijeljenja ta se izmjena može rastaviti na $O(\sqrt{a_{i-1}}+\sqrt{a_i})$ izmjena na intervalima, pri čemu je vrijednost koja se dodaje na svakom intervalu konstantna. Konačno dobiveni niz $\{T(k,n)\}_k$ je odgovor.
    
    Budući da se u zadatku pojavljuje niz operacija dodavanja na intervalu, a upiti se događaju tek nakon što su sve izmjene gotove, dodavanje na intervalu može se provoditi održavanjem niza razlika (difference array), a traženi se niz na kraju dobiva računanjem prefiksnih suma. Ukupna vremenska složenost je $O(\max_i a_i+\sum_i\sqrt{a_i})$. Zadatak ima i druga rješenja.

??? note "Implementacija"
    ```cpp
    --8<-- "docs/math/code/sqrt-decomposition/sqrt-decomposition_2.cpp"
    ```

## Zadaci za vježbu

-   [UVa11526 H(n)](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=27&page=show_problem&problem=2521)
-   [Luogu P2261 CQOI2007 余数求和 (Zbroj ostataka)](https://www.luogu.com.cn/problem/P2261)
-   [Luogu P3455 POI2007 ZAP-Queries](https://www.luogu.com.cn/problem/P3455)

## Literatura i napomene

-   [杜教筛的时空复杂度分析 by riteme (Analiza vremenske i prostorne složenosti Du sita)](https://riteme.site/blog/2018-9-11/time-space-complexity-dyh-algo.html)
