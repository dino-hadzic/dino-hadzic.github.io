---
title: Napredni DP ruksaka
---

## Trikovi vezani uz ruksak

### Ruksak s generaliziranim predmetima

U ovoj vrsti ruksaka pojedini predmet $i$ nema fiksnu cijenu i vrijednost; njegova vrijednost ovisi o cijeni koja mu je dodijeljena. U problemu ruksaka s kapacitetom $V$, kad je predmetu $i$ dodijeljena cijena $v_i$, dobivena vrijednost je $h_i\left(v_i\right)$.

Nabrajamo, dakle, težinu $w'$ dodijeljenu $i$-tom predmetu; vrijednost predmeta tada je $h_i(w')$, a trenutna vrijednost je $f_{i - 1, w - w'} + h_i(w')$. Jednadžba prijelaza stanja stoga glasi $f_{i, j} = \max \limits_{0 \le k \le j}(f_{i - 1, j - k} + h_i(k))$. Zapravo, sve gore opisano upravo je $(\max, +)$ konvolucija.

### Grupni ruksak

???+ note "[„Luogu P1757” Grupni ruksak do neba](https://www.luogu.com.cn/problem/P1757)"
    Zadano je $n$ predmeta i ruksak veličine $m$; $i$-ti predmet ima vrijednost $w_i$ i volumen $v_i$. Osim toga, svaki predmet pripada jednoj grupi, a iz iste grupe može se odabrati najviše jedan predmet. Treba pronaći najveću ukupnu vrijednost predmeta koje ruksak može nositi.

Takvi zadaci zapravo samo „odaberi jedan među svim predmetima” mijenjaju u „odaberi jedan iz trenutne grupe”, pa je dovoljno za svaku grupu provesti jedan 0-1 ruksak.

Recimo još nešto o spremanju. Neka $t_{k,i}$ označava indeks $i$-tog predmeta $k$-te grupe, a $\mathit{cnt}_k$ broj predmeta u $k$-toj grupi.

#### Implementacija

=== "C++"
    ```cpp
    --8<-- "docs/dp/code/knapsack/knapsack_4.cpp:core"
    ```

=== "Python"
    ```python
    for k in range(1, ts + 1):  # petlja po grupama
        for i in range(m, -1, -1):  # petlja po kapacitetu ruksaka
            for j in range(1, cnt[k] + 1):  # petlja po predmetima grupe
                if i >= w[t[k][j]]:  # kapacitet ruksaka je dovoljan
                    dp[i] = max(
                        dp[i], dp[i - w[t[k][j]]] + c[t[k][j]]
                    )  # prijelaz stanja kao kod 0-1 ruksaka
    ```

Ovdje treba pripaziti: **nikako se ne smije pobrkati redoslijed petlji**; samo tako se jamči ispravnost.

### Ruksak s povlačenjem

Za brojanje načina u običnom 0-1 ruksaku dovoljan je izravan DP, no ponekad se pojavljuju situacije oblika „svi se predmeti smiju odabrati osim nekoliko”, i to obično tako da se u istoj grupi predmeta više puta pojavljuju različiti predmeti koji se ne smiju odabrati, npr. u nekim složenijim ruksacima na stablu. Izravan DP tada može dati TLE, pa za takve situacije treba uvesti ruksak s povlačenjem.

Uočimo da su predmeti u ruksaku neuređeni: za dva predmeta nije važno koji se stavlja prvi, pa možemo smatrati da je **svaki predmet upravo onaj posljednji stavljeni**. Zato možemo najprije predizračunati DP za sve predmete, a zatim poništiti doprinos pojedinog predmeta. Odnosno:

$$
dp_j \gets dp_j - dp_{j - w_i}
$$

Pripazite da petlja ide od manjeg prema većem; inače bi doprinos odgovarao načinu neograničenog ruksaka.

## Razno o ruksaku

### Ispis rješenja

Ispis rješenja zapravo znači zapisati kako je neko stanje ruksaka izvedeno. Neka $g_{i,v}$ označava je li, kad $i$-ti predmet zauzima prostor $v$, taj predmet odabran. Zatim pri prijelazu zapišemo koja je strategija upotrijebljena (odabran ili ne). Pseudokod ispisa:

```cpp
int v = V;  // zapisuje trenutni prostor

// budući da posljednji predmet čuva konačno stanje, petlja kreće od posljednjeg predmeta
for (od posljednjeg predmeta do prvog) {
  if (g[i][v]) {
    predmet i je odabran;
    v -= težina predmeta i;
  } else {
    predmet i nije odabran;
  }
}
```

### Brojanje optimalnih rješenja

Za brojanje optimalnih rješenja malo mijenjamo definiciju niza $\mathit{dp}$ iz 0-1 ruksaka: DP stanje $f_{i,j}$ najveća je ukupna vrijednost koju može postići ruksak kapaciteta $j$ koji je „točno napunjen”, ako se smiju stavljati samo prvih $i$ predmeta.

Nakon te izmjene svakom DP stanju možemo pridružiti $g_{i,j}$ koji označava broj načina.

$f_{i,j}$ označava najveću vrijednost kad se razmatraju samo prvih $i$ predmeta, a volumen ruksaka je „točno” $j$.

$g_{i,j}$ označava broj načina kad se razmatraju samo prvih $i$ predmeta, a volumen ruksaka je „točno” $j$.

Jednadžba prijelaza:

Ako je $f_{i,j} = f_{i-1,j}$ i $f_{i,j} \neq f_{i-1,j-v}+w$, bolje je ne staviti predmet u ruksak, pa broj načina dolazi iz $g_{i-1,j}$;

ako je $f_{i,j} \neq f_{i-1,j}$ i $f_{i,j} = f_{i-1,j-v}+w$, bolje je staviti predmet u ruksak, pa broj načina dolazi iz $g_{i-1,j-v}$;

ako je $f_{i,j} = f_{i-1,j}$ i $f_{i,j} = f_{i-1,j-v}+w$, optimum se postiže i stavljanjem i nestavljanjem, pa broj načina dolazi iz $g_{i-1,j}$ i $g_{i-1,j-v}$.

Početni uvjeti:

```cpp
memset(f, 0xcf, sizeof(f));
// budući da tražimo maksimum, inicijaliziramo na minus beskonačno, da ne bi došlo do prijelaza iz nenapunjenog stanja
// ako tražimo minimum, inicijaliziramo na plus beskonačno 0x3f
f[0] = 0;
g[0] = 1;  // ne staviti ništa jedan je od načina
```

Budući da se najveći volumen ruksaka možda ne može napuniti, optimalno rješenje nije nužno $f_{m}$.

Na kraju pronađemo vrijednost optimalnog rješenja i zbrojimo brojeve načina iz niza $g_{j}$ za sve one koji postižu optimum.

???+ note "Implementacija"
    ```cpp
    for (int i = 0; i < N; i++) {
      for (int j = V; j >= v[i]; j--) {
        int tmp = std::max(dp[j], dp[j - v[i]] + w[i]);
        int c = 0;
        if (tmp == dp[j]) c += cnt[j];                       // ako je prijelaz iz dp[j]
        if (tmp == dp[j - v[i]] + w[i]) c += cnt[j - v[i]];  // ako je prijelaz iz dp[j-v[i]]
        dp[j] = tmp;
        cnt[j] = c;
      }
    }
    int max = 0;  // traženje optimalnog rješenja
    for (int i = 0; i <= V; i++) {
      max = std::max(max, dp[i]);
    }
    int res = 0;
    for (int i = 0; i <= V; i++) {
      if (dp[i] == max) {
        res += cnt[i];  // zbroji brojeve načina za optimalno rješenje
      }
    }
    ```

### k-to najbolje rješenje ruksaka

Obični 0-1 ruksak traži optimalno rješenje; malom izmjenom uobičajene DP metode za ruksak, dodavanjem jedne dimenzije koja pamti prvih k najboljih rješenja u trenutnom stanju, dobivamo algoritam za $k$-to najbolje rješenje 0-1 ruksaka.
Konkretno: $f_{i,j,k}$ pamti $k$-ti najveći zbroj vrijednosti koji se može dobiti među prvih $i$ predmeta kad je ukupni volumen odabranih predmeta $j$. To stanje možemo shvatiti kao proširenje $f_{i,j}$ običnog 0-1 ruksaka, koje pamti samo jedan podatak, na uređeni niz najboljih rješenja. Pri prijelazu, u običnom ruksaku optimum se računa kao $f_{i,j}=\max(f_{i-1,j},f_{i-1,j-v_i}+w_i)$; sad pak trebamo spojiti dva padajuća niza veličine $k$, $f_{i-1,j}$ i $f_{i-1,j-v_i}+w_i$, i prvih $k$ najvećih vrijednosti nakon spajanja zapisati u $f_{i,j}$. Taj se korak izvodi metodom dvaju pokazivača u složenosti $O(k)$, pa je ukupna vremenska složenost $O(nmk)$. Prostorno se, kao i kod običnog ruksaka, prva dimenzija može sažeti, pa je složenost $O(mk)$.

??? note "Primjer [HDU 2639 Bone Collector II](https://acm.hdu.edu.cn/showproblem.php?pid=2639)"
    Treba pronaći strogo $k$-to najbolje rješenje 0-1 ruksaka. $n \leq 100,v \leq 1000,k \leq 30$

??? note "Implementacija"
    ```cpp
    --8<-- "docs/dp/code/knapsack/knapsack_3.cpp:core"
    ```

## Problemi vezani uz ruksak

### Miješani ruksak

Miješani ruksak kombinacija je 0-1 ruksaka, neograničenog ruksaka i ograničenog ruksaka: neki se predmeti mogu uzeti samo jednom, neki neograničeno mnogo puta, a neki najviše $k$ puta.

Takvi zadaci izgledaju teško, no odabir svake vrste predmeta i dalje je neovisan, pa je dovoljno utvrditi kojoj vrsti ruksaka trenutni predmet pripada i primijeniti rješenje za tu vrstu.

#### Primjer

???+ note "[„Luogu P1833” Trešnjin cvijet](https://www.luogu.com.cn/problem/P1833)"
    Zadano je $n$ vrsta stabala trešnje i vrijeme duljine $T$; neka se stabla mogu pogledati samo jednom, neka najviše $A_{i}$ puta, a neka neograničeno mnogo puta. Svako stablo trešnje ima estetsku vrijednost $C_{i}$. Treba odrediti koja stabla pogledati u vremenu $T$ da estetska vrijednost bude najveća.

??? note "Ključni kôd"
    ```cpp
    --8<-- "docs/dp/code/knapsack/knapsack_5.cpp:core"
    ```

Zadatak za vježbu: [HDU 5410 CRB and His Birthday](https://acm.hdu.edu.cn/showproblem.php?pid=5410)

### Ruksak s dvodimenzionalnom cijenom

???+ note "[„Luogu P1855” Iscijediti kkksc03](https://www.luogu.com.cn/problem/P1855)"
    Treba obaviti $n$ zadataka; obavljanje $i$-tog zadatka traži $t_i$ minuta i stvara trošak od $c_i$ juana.
    
    Na raspolaganju je $T$ minuta i $W$ juana za obradu tih zadataka. Treba pronaći najveći broj zadataka koji se mogu obaviti.

Ovaj je zadatak očito 0-1 problem ruksaka, ali s razlikom da odabir jednog predmeta troši dvije vrste cijene (novac i vrijeme); dovoljno je stanju dodati jednu dimenziju za drugu cijenu. Jednadžba prijelaza stanja tada postaje $f_{i, j, k} = \max(f_{i - 1, j, k}, f_{i - 1, j - t_i, k - c_i} + w_i)$. U ovom zadatku svi su $w_i$ jednaki $1$.

Ovdje treba pripaziti da više nije prikladno otvarati još jednu dimenziju za indeks predmeta, jer lako dolazi do MLE-a.

#### Implementacija

=== "C++"
    ```cpp
    --8<-- "docs/dp/code/knapsack/knapsack_6.cpp:core"
    ```

=== "Python"
    ```python
    for k in range(1, n + 1):
        for i in range(m, mi - 1, -1):  # razina nabrajanja po novcu
            for j in range(t, ti - 1, -1):  # razina nabrajanja po vremenu
                dp[i][j] = max(dp[i][j], dp[i - mi][j - ti] + 1)
    ```

### Ruksak s ovisnostima

???+ note "[„Luogu P1064” Jin Mingov plan proračuna](https://www.luogu.com.cn/problem/P1064)"
    Jin Ming ima $n$ juana i želi kupiti $m$ predmeta; $i$-ti predmet ima cijenu $v_i$ i važnost $p_i$. Neki su predmeti dodaci nekog glavnog predmeta; da bi se kupio takav predmet, mora se kupiti i njegov glavni predmet.
    
    Cilj je maksimizirati zbroj $v_i \times p_i$ svih kupljenih predmeta.

Dovoljno je to obraditi kao [ruksak na stablu](../tree.md#树上背包). Pripazite da na kraju spojite sve ruksake.

## Literatura i bilješke

-   [Devet predavanja o problemu ruksaka – Cui Tianyi (kineski)](https://github.com/tianyicui/pack).
