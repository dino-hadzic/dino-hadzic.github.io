---
title: Osnove DP-a ruksaka
---

Preduvjeti: [Uvod u dinamičko programiranje](../index.md).

## Uvod

Prije nego što konkretno objasnimo što je „DP ruksaka”, pogledajmo sljedeći primjer:

???+ note "[„USACO07 DEC” Charm Bracelet](https://www.luogu.com.cn/problem/P2871)"
    Sažetak zadatka: zadano je $n$ predmeta i ruksak kapaciteta $W$; svaki predmet ima dva svojstva, težinu $w_{i}$ i vrijednost $v_{i}$. Treba odabrati neke predmete i staviti ih u ruksak tako da ukupna vrijednost predmeta u ruksaku bude najveća, a ukupna težina predmeta u ruksaku ne premašuje njegov kapacitet.

U gornjem primjeru svaki predmet ima samo dva moguća stanja (uzet ili ne), što odgovara binarnim $0$ i $1$, pa se takvi problemi nazivaju „0-1 problem ruksaka”.

## 0-1 ruksak

### Objašnjenje

U primjeru su poznati težina $w_{i}$ i vrijednost $v_{i}$ $i$-tog predmeta te ukupni kapacitet ruksaka $W$.

Neka je DP stanje $f_{i,j}$ najveća ukupna vrijednost koju može postići ruksak kapaciteta $j$ ako se smiju stavljati samo prvih $i$ predmeta.

Razmotrimo prijelaz. Pretpostavimo da su već obrađena sva stanja za prvih $i-1$ predmeta. Za $i$-ti predmet: ako ga ne stavimo u ruksak, preostali kapacitet ruksaka se ne mijenja, kao ni ukupna vrijednost predmeta u ruksaku, pa je najveća vrijednost u tom slučaju $f_{i-1,j}$; ako ga stavimo u ruksak, preostali kapacitet smanjuje se za $w_{i}$, a ukupna vrijednost predmeta u ruksaku raste za $v_{i}$, pa je najveća vrijednost u tom slučaju $f_{i-1,j-w_{i}}+v_{i}$.

Odatle dobivamo jednadžbu prijelaza stanja:

$$
f_{i,j}=\max(f_{i-1,j},f_{i-1,j-w_{i}}+v_{i})
$$

Ako bismo stanja izravno zapisivali u dvodimenzionalni niz, dobili bismo MLE. Možemo razmotriti optimizaciju kružnim nizom.

Budući da na $f_i$ utječe samo $f_{i-1}$, možemo izbaciti prvu dimenziju i s $f_{i}$ izravno označavati najveću vrijednost ruksaka kapaciteta $i$ pri obradi trenutnog predmeta, čime dobivamo jednadžbu:

$$
f_j=\max \left(f_j,f_{j-w_i}+v_i\right)
$$

**Obavezno zapamtite i shvatite ovu jednadžbu prijelaza, jer su jednadžbe prijelaza većine problema ruksaka izvedene iz nje.**

### Implementacija

Treba pripaziti na još jednu stvar: lako je napisati ovakav **pogrešan ključni kôd**:

=== "C++"
    ```cpp
    for (int i = 1; i <= n; i++)
      for (int l = 0; l <= W - w[i]; l++)
        f[l + w[i]] = max(f[l] + v[i], f[l + w[i]]);
    // pojednostavljeno iz f[i][l + w[i]] = max(max(f[i - 1][l + w[i]], f[i - 1][l] + v[i]),
    // f[i][l + w[i]]);
    ```

=== "Python"
    ```python
    for i in range(1, n + 1):
        for l in range(0, W - w[i] + 1):
            f[l + w[i]] = max(f[l] + v[i], f[l + w[i]])
    # pojednostavljeno iz f[i][l + w[i]] = max(max(f[i - 1][l + w[i]], f[i - 1][l] + v[i]),
    # f[i][l + w[i]])
    ```

Gdje je greška u ovom kodu? Pogrešan je redoslijed nabrajanja.

Pažljivim promatranjem koda vidimo: za trenutno obrađivani predmet $i$ i trenutno stanje $f_{i,j}$, kad je $j\geqslant w_{i}$, na $f_{i,j}$ utječe $f_{i,j-w_{i}}$. To znači da se predmet $i$ može više puta staviti u ruksak, što ne odgovara zadatku. (Zapravo, upravo je to rješenje neograničenog problema ruksaka.)

Da to izbjegnemo, možemo promijeniti redoslijed nabrajanja: nabrajamo od $W$ do $w_{i}$. Tada se gornja greška ne pojavljuje, jer se $f_{i,j}$ uvijek ažurira prije $f_{i,j-w_{i}}$.

Stoga je stvarni ključni kôd:

=== "C++"
    ```cpp
    for (int i = 1; i <= n; i++)
      for (int l = W; l >= w[i]; l--) f[l] = max(f[l], f[l - w[i]] + v[i]);
    ```

=== "Python"
    ```python
    for i in range(1, n + 1):
        for l in range(W, w[i] - 1, -1):
            f[l] = max(f[l], f[l - w[i]] + v[i])
    ```

??? note "Kôd primjera"
    ```cpp
    --8<-- "docs/dp/code/knapsack/knapsack_1.cpp"
    ```

## Neograničeni ruksak

### Objašnjenje

Model neograničenog ruksaka sličan je 0-1 ruksaku; razlika je samo u tome što se jedan predmet može odabrati neograničeno mnogo puta, a ne samo jednom.

Možemo posuditi ideju 0-1 ruksaka za definiciju stanja: neka je $f_{i,j}$ najveća vrijednost koju može postići ruksak kapaciteta $j$ ako se smiju birati samo prvih $i$ predmeta.

Treba imati na umu da je, iako je definicija slična 0-1 ruksaku, jednadžba prijelaza stanja drugačija.

### Postupak

Razmotrimo naivni pristup: za $i$-ti predmet nabrajamo koliko ga je komada odabrano i prelazimo. Vremenska složenost takvog pristupa je $O(nW^2)$, gdje je $n$ ukupan broj predmeta, a $W$ kapacitet ruksaka.

Jednadžba prijelaza stanja glasi:

$$
f_{i,j}=\max_{k=0}^{\lfloor j/w_i\rfloor}(f_{i-1,j-k\times w_i}+v_i\times k)
$$

Razmotrimo jednostavnu optimizaciju. Uočavamo da je za $f_{i,j}$ dovoljan prijelaz iz $f_{i,j-w_i}$. Jednadžba prijelaza stanja stoga je:

$$
f_{i,j}=\max(f_{i-1,j},f_{i,j-w_i}+v_i)
$$

Razlog je u tome što je pri takvom prijelazu $f_{i,j-w_i}$ već ažuriran iz $f_{i,j-2\times w_i}$, pa je $f_{i,j-w_i}$ optimalan rezultat koji već u potpunosti uzima u obzir broj odabranih komada $i$-tog predmeta. Drugim riječima, svojstvom lokalno optimalne podstrukture ponovno smo iskoristili prethodni postupak nabrajanja i optimizirali složenost nabrajanja.

Kao i kod 0-1 ruksaka, možemo izbaciti prvu dimenziju i tako optimizirati prostornu složenost. Ako ste shvatili optimizaciju 0-1 ruksaka, nije teško vidjeti da je petlja nakon sažimanja usmjerena prema naprijed (upravo ona gore spomenuta pogrešna optimizacija).

??? note "[„Luogu P1616” Ludo skupljanje ljekovitog bilja](https://www.luogu.com.cn/problem/P1616)"
    Sažetak zadatka: zadano je $n$ vrsta predmeta i ruksak kapaciteta $W$; svaka vrsta predmeta ima dva svojstva, težinu $w_{i}$ i vrijednost $v_{i}$. Treba odabrati neke predmete i staviti ih u ruksak tako da ukupna vrijednost predmeta u ruksaku bude najveća, a ukupna težina predmeta u ruksaku ne premašuje njegov kapacitet.

??? note "Kôd primjera"
    ```cpp
    --8<-- "docs/dp/code/knapsack/knapsack_2.cpp"
    ```

## Ograničeni ruksak

Ograničeni ruksak također je varijanta 0-1 ruksaka. Razlika u odnosu na 0-1 ruksak je u tome što svake vrste predmeta ima $k_i$ komada, a ne jedan.

Vrlo naivna ideja: „svaku vrstu predmeta odabrati $k_i$ puta” ekvivalentno pretvorimo u „postoji $k_i$ jednakih predmeta, svaki se odabire jednom”. Tako dobivamo model 0-1 ruksaka i rješavamo ga gore opisanom metodom. Jednadžba prijelaza stanja glasi:

$$
f_{i,j}=\max_{k=0}^{k_i}(f_{i-1,j-k\times w_i}+v_i\times k)
$$

Vremenska složenost je $O(W\sum_{i=1}^nk_i)$.

??? note "Ključni kôd"
    ```cpp
    for (int i = 1; i <= n; i++) {
      for (int weight = W; weight >= w[i]; weight--) {
        // dodatna razina petlje po broju komada predmeta
        for (int k = 1; k * w[i] <= weight && k <= cnt[i]; k++) {
          dp[weight] = max(dp[weight], dp[weight - k * w[i]] + k * v[i]);
        }
      }
    }
    ```

### Optimizacija binarnim grupiranjem

Razmotrimo optimizaciju. I dalje ograničeni ruksak pretvaramo u model 0-1 ruksaka.

### Objašnjenje

Očito se dio složenosti $O(nW)$ više ne može optimizirati, pa možemo zahvatiti samo $O(\sum k_i)$. Radi lakšeg izražavanja, s $A_{i,j}$ označavamo $j$-ti predmet dobiven razdvajanjem $i$-te vrste predmeta.

U naivnom pristupu, $\forall j\le k_i$, svi $A_{i,j}$ označavaju isti predmet. Glavni uzrok niske učinkovitosti jest to što obavljamo mnogo posla koji se ponavlja. Na primjer, razmatrali smo dva potpuno ekvivalentna slučaja: „istodobno odabrati $A_{i,1},A_{i,2}$” i „istodobno odabrati $A_{i,2},A_{i,3}$”. Takav ponovljeni posao obavili smo mnogo puta. Optimizacija načina razdvajanja stoga postaje ključ rješenja problema.

### Postupak

„Binarnim grupiranjem” razdvajanje možemo učiniti učinkovitijim.

Konkretno, neka $A_{i,j}\left(j\in\left[0,\lfloor \log_2(k_i+1)\rfloor-1\right]\right)$ redom označava veliki predmet „svezan” od $2^{j}$ pojedinačnih predmeta. Posebno, ako $k_i+1$ nije cjelobrojna potencija broja $2$, na kraju treba dodati veliki predmet „svezan” od $k_i-2^{\lfloor \log_2(k_i+1)\rfloor}+1$ pojedinačnih predmeta kao nadopunu.

Nekoliko primjera:

-   $6=1+2+3$
-   $8=1+2+4+1$
-   $18=1+2+4+8+3$
-   $31=1+2+4+8+16$

Očito se gornjim razdvajanjem može prikazati ekvivalentan odabir bilo kojeg broja $\le k_i$ predmeta. Nakon što svaku vrstu predmeta razdvojimo na opisani način, dovoljno je riješiti problem metodom 0-1 ruksaka.

Vremenska složenost je $O(W\sum_{i=1}^n\log_2k_i)$

### Implementacija

??? note "Kôd binarnog grupiranja"
    === "C++"
        ```cpp
        index = 0;
        for (int i = 1; i <= m; i++) {
          int c = 1, p, h, k;
          cin >> p >> h >> k;
          while (k > c) {
            k -= c;
            list[++index].w = c * p;
            list[index].v = c * h;
            c *= 2;
          }
          list[++index].w = p * k;
          list[index].v = h * k;
        }
        ```
    
    === "Python"
        ```python
        index = 0
        for i in range(1, m + 1):
            c = 1
            p, h, k = map(int, input().split())
            while k > c:
                k -= c
                index += 1
                list[index].w = c * p
                list[index].v = c * h
                c *= 2
            index += 1
            list[index].w = p * k
            list[index].v = h * k
        ```

### Optimizacija monotonim redom

Vidi [Optimizacija monotonim redom/monotonim stogom](../opt/monotonic-queue-stack.md).

Zadatak za vježbu: [„Luogu P1776” Odabir blaga\_NOI Daokan 2010 Tigao (02)](https://www.luogu.com.cn/problem/P1776)

## Brojanje načina

Za zadani kapacitet ruksaka, cijene predmeta, druge odnose i sl., traži se ukupan broj načina da se napuni određeni kapacitet.

Kod takvih problema dovoljno je traženje maksimuma zamijeniti zbrajanjem.

Na primjer, jednadžba prijelaza 0-1 problema ruksaka postaje:

$$
\mathit{dp}_j \leftarrow \mathit{dp}_j + \mathit{dp}_{j-c_i} \qquad (j \ge c_i)
$$

Početni uvjet: $\mathit{dp}_0=1$

Naime, i za kapacitet $0$ postoji jedan način: ne staviti ništa.

## Literatura i bilješke

-   [Devet predavanja o problemu ruksaka – Cui Tianyi (kineski)](https://github.com/tianyicui/pack).
