---
title: Dancing Links
---

Ova stranica predstavlja problem točnog pokrivanja, problem ponovljenog pokrivanja, algoritam koji ih rješava („algoritam X”) te dvostruko povezanu križnu listu Dancing Links kojom se algoritam X optimizira. Također se objašnjava kako se, uz odgovarajuće modeliranje, DLX-om rješavaju neki zadaci iz pretraživanja.

## Problem točnog pokrivanja

### Definicija

Problem točnog pokrivanja (engl. Exact Cover Problem) glasi: zadano je mnogo skupova $S_i (1 \le i \le n)$ i skup $X$; treba pronaći neuređenu $m$-torku $(T_1, T_2, \cdots , T_m)$ koja zadovoljava sljedeće uvjete:

1.  $\forall i, j \in [1, m],T_i\bigcap T_j = \varnothing (i \neq j)$
2.  $X = \bigcup\limits_{i = 1}^{m}T_i$
3.  $\forall i \in[1, m], T_i \in \{S_1, S_2, \cdots, S_n\}$

### Objašnjenje

Na primjer, ako je zadano

$$
\begin{aligned}
  & S_1 = \{5, 9, 17\} \\
  & S_2 = \{1, 8, 119\} \\
  & S_3 = \{3, 5, 17\} \\
  & S_4 = \{1, 8\} \\
  & S_5 = \{3, 119\} \\
  & S_6 = \{8, 9, 119\} \\
  & X = \{1, 3, 5, 8, 9, 17, 119\}
\end{aligned}
$$

onda je $(S_1, S_4, S_5)$ jedno valjano rješenje.

### Preoblikovanje problema

Diskretiziramo li sve brojeve iz $\bigcup\limits_{i = 1}^{n}S_i$, dobivamo ovakav model:

> Zadana je 01-matrica; možete odabrati neke retke (row) tako da na kraju svaki stupac (column)[^note1] ima točno jednu jedinicu.
> Na primjer, modeliramo li gornji primjer, dobivamo ovakvu matricu:

$$
\begin{pmatrix}
0 & 0 & 1 & 0 & 1 & 1 & 0 \\
1 & 0 & 0 & 1 & 0 & 0 & 1 \\
0 & 1 & 1 & 0 & 0 & 1 & 0 \\
1 & 0 & 0 & 1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 & 0 & 1 \\
0 & 0 & 0 & 1 & 1 & 0 & 1
\end{pmatrix}
$$

> Pritom $i$-ti redak predstavlja $S_i$, a brojevi u tom retku redom označavaju $[1 \in S_i],[3 \in S_i],[5 \in S_i],\cdots,[119 \in S_i]$.

### Implementacija

#### Gruba sila 1

Jedan je način nabrojati koje retke odabiremo i na kraju provjeriti je li odabir valjan.

Budući da svaki redak ima dva stanja (odabran ili ne), vremenska složenost nabrajanja redaka je $O(2^n)$;

a svaka provjera traži $O(nm)$ vremena. Ukupna je složenost stoga $O(nm\cdot2^n)$.

??? note "Implementacija"
    ```cpp
    int ok = 0;
    for (int state = 0; state < 1 << n; ++state) {  // nabroji je li svaki redak odabran
      for (int i = 1; i <= n; ++i)
        if ((1 << i - 1) & state)
          for (int j = 1; j <= m; ++j) a[i][j] = 1;
      int flag = 1;
      for (int j = 1; j <= m; ++j)
        for (int i = 1, bo = 0; i <= n; ++i)
          if (a[i][j]) {
            if (bo)
              flag = 0;
            else
              bo = 1;
          }
      if (!flag)
        continue;
      else {
        ok = 1;
        for (int i = 1; i <= n; ++i)
          if ((1 << i - 1) & state) printf("%d ", i);
        puts("");
      }
      memset(a, 0, sizeof(a));
    }
    if (!ok) puts("No solution.");
    ```

#### Gruba sila 2

Uzmemo li u obzir posebno svojstvo 01-matrice, svaki se redak može promatrati kao $m$-bitni binarni broj.

Izvorni problem tako postaje:

> Zadano je $n$ $m$-bitnih binarnih brojeva; treba odabrati neke od njih tako da je AND svaka dva odabrana broja jednak 0, a OR svih odabranih brojeva jednak $2^m - 1$. `tmp` označava OR dosad odabranih binarnih brojeva.

Budući da svaki redak ima dva stanja (odabran ili ne), vremenska složenost nabrajanja redaka je $O(2^n)$;

a svako računanje `tmp` traži $O(n)$ vremena. Ukupna je složenost stoga $O(n\cdot2^n)$.

??? note "Implementacija"
    ```cpp
    int ok = 0;
    for (int i = 1; i <= n; ++i)
      for (int j = m; j >= 1; --j) num[i] = num[i] << 1 | a[i][j];
    for (int state = 0; state < 1 << n; ++state) {
      int tmp = 0;
      bool flag = true;
      for (int i = 1; i <= n; ++i)
        if ((1 << i - 1) & state) {
          if (tmp & num[i]) {
            flag = false;
            break;
          }
          tmp |= num[i];
        }
      if (flag && tmp == (1 << m) - 1) {
        ok = 1;
        for (int i = 1; i <= n; ++i)
          if ((1 << i - 1) & state) printf("%d ", i);
        puts("");
      }
    }
    if (!ok) puts("No solution.");
    ```

## Problem ponovljenog pokrivanja

Problem ponovljenog pokrivanja sličan je problemu točnog pokrivanja, ali bez ograničenja na preklapanje elemenata. [Algoritam X](#algoritam-x) opisan u nastavku izvorno je namijenjen točnom pokrivanju, no uz nekoliko izmjena i optimizacija (označenih u tekstu) jednako učinkovito rješava i problem ponovljenog pokrivanja.

## Algoritam X

Donald E. Knuth predložio je algoritam X (Algorithm X); ideja mu je slična upravo opisanoj gruboj sili, ali ga je lako optimizirati.

### Postupak

Nastavljamo s primjerom iz gornjeg teksta i dobivamo ovakvu 01-matricu:

$$
\begin{pmatrix}
  0 & 0 & 1 & 0 & 1 & 1 & 0 \\
  1 & 0 & 0 & 1 & 0 & 0 & 1 \\
  0 & 1 & 1 & 0 & 0 & 1 & 0 \\
  1 & 0 & 0 & 1 & 0 & 0 & 0 \\
  0 & 1 & 0 & 0 & 0 & 0 & 1 \\
  0 & 0 & 0 & 1 & 1 & 0 & 1
\end{pmatrix}
$$

1.  Prvi redak sad ima $3$ jedinice, drugi $3$, treći $3$, četvrti $2$, peti $2$, a šesti $3$. Odaberemo prvi redak, izbrišemo ga i označimo sve stupce u kojima ima $1$;

    $$
    \begin{pmatrix}
      \color{Blue}0 & \color{Blue}0 & \color{Blue}1 & \color{Blue}0 & \color{Blue}1 & \color{Blue}1 & \color{Blue}0 \\
      1 & 0 & \color{Red}0 & 1 & \color{Red}0 & \color{Red}0 & 1 \\
      0 & 1 & \color{Red}1 & 0 & \color{Red}0 & \color{Red}1 & 0 \\
      1 & 0 & \color{Red}0 & 1 & \color{Red}0 & \color{Red}0 & 0 \\
      0 & 1 & \color{Red}0 & 0 & \color{Red}0 & \color{Red}0 & 1 \\
      0 & 0 & \color{Red}0 & 1 & \color{Red}1 & \color{Red}0 & 1
      \end{pmatrix}
    $$

2.  Odaberemo sve označene stupce, izbrišemo ih i označimo retke koji u tim stupcima imaju $1$ (kod problema ponovljenog pokrivanja označavanje nije potrebno);

    $$
    \begin{pmatrix}
      \color{Blue}0 & \color{Blue}0 & \color{Blue}1 & \color{Blue}0 & \color{Blue}1 & \color{Blue}1 & \color{Blue}0 \\
      1 & 0 & \color{Blue}0 & 1 & \color{Blue}0 & \color{Blue}0 & 1 \\
      \color{Red}0 & \color{Red}1 & \color{Blue}1 & \color{Red}0 & \color{Blue}0 & \color{Blue}1 & \color{Red}0 \\
      1 & 0 & \color{Blue}0 & 1 & \color{Blue}0 & \color{Blue}0 & 0 \\
      0 & 1 & \color{Blue}0 & 0 & \color{Blue}0 & \color{Blue}0 & 1 \\
      \color{Red}0 & \color{Red}0 & \color{Blue}0 & \color{Red}1 & \color{Blue}1 & \color{Blue}0 & \color{Red}1
    \end{pmatrix}
    $$

3.  Odaberemo sve označene retke i izbrišemo ih;

    $$
    \begin{pmatrix}
      \color{Blue}0 & \color{Blue}0 & \color{Blue}1 & \color{Blue}0 & \color{Blue}1 & \color{Blue}1 & \color{Blue}0 \\
      1 & 0 & \color{Blue}0 & 1 & \color{Blue}0 & \color{Blue}0 & 1 \\
      \color{Blue}0 & \color{Blue}1 & \color{Blue}1 & \color{Blue}0 & \color{Blue}0 & \color{Blue}1 & \color{Blue}0 \\
      1 & 0 & \color{Blue}0 & 1 & \color{Blue}0 & \color{Blue}0 & 0 \\
      0 & 1 & \color{Blue}0 & 0 & \color{Blue}0 & \color{Blue}0 & 1 \\
      \color{Blue}0 & \color{Blue}0 & \color{Blue}0 & \color{Blue}1 & \color{Blue}1 & \color{Blue}0 & \color{Blue}1
    \end{pmatrix}
    $$

    **To znači da je taj redak odabran i da u stupcima u kojima on ima $1$ više ne smije biti drugih jedinica**.

    Tako dobivamo novu malu 01-matricu:

    $$
    \begin{pmatrix}
      1 & 0 & 1 & 1 \\
      1 & 0 & 1 & 0 \\
      0 & 1 & 0 & 1
    \end{pmatrix}
    $$

4.  Sad prvi redak (izvorno drugi) ima $3$ jedinice, drugi (izvorno četvrti) $2$, a treći (izvorno peti) $2$. Odaberemo prvi redak (izvorno drugi), izbrišemo ga i označimo sve stupce u kojima ima $1$;

    $$
    \begin{pmatrix}
      \color{Blue}1 & \color{Blue}0 & \color{Blue}1 & \color{Blue}1 \\
      \color{Red}1 & 0 & \color{Red}1 & \color{Red}0 \\
      \color{Red}0 & 1 & \color{Red}0 & \color{Red}1
    \end{pmatrix}
    $$

5.  Odaberemo sve označene stupce, izbrišemo ih i označimo retke koji u tim stupcima imaju $1$;

    $$
    \begin{pmatrix}
      \color{Blue}1 & \color{Blue}0 & \color{Blue}1 & \color{Blue}1 \\
      \color{Blue}1 & \color{Red}0 & \color{Blue}1 & \color{Blue}0 \\
      \color{Blue}0 & \color{Red}1 & \color{Blue}0 & \color{Blue}1
    \end{pmatrix}
    $$

6.  Odaberemo sve označene retke i izbrišemo ih;

    $$
    \begin{pmatrix}
      \color{Blue}1 & \color{Blue}0 & \color{Blue}1 & \color{Blue}1 \\
      \color{Blue}1 & \color{Blue}0 & \color{Blue}1 & \color{Blue}0 \\
      \color{Blue}0 & \color{Blue}1 & \color{Blue}0 & \color{Blue}1
    \end{pmatrix}
    $$

    Tako dobivamo praznu matricu. Ali posljednji izbrisani redak `1 0 1 1` nije sav od jedinica, što znači da je odabir bio pogrešan;

    $$
    \begin{pmatrix}
    \end{pmatrix}
    $$

7.  Vraćamo se na 4. korak i razmatramo odabir drugog retka (izvorno četvrtog): izbrišemo ga i označimo sve stupce u kojima ima $1$;

    $$
    \begin{pmatrix}
      \color{Red}1 & 0 & \color{Red}1 & 1 \\
      \color{Blue}1 & \color{Blue}0 & \color{Blue}1 & \color{Blue}0 \\
      \color{Red}0 & 1 & \color{Red}0 & 1
    \end{pmatrix}
    $$

8.  Odaberemo sve označene stupce, izbrišemo ih i označimo retke koji u tim stupcima imaju $1$;

    $$
    \begin{pmatrix}
      \color{Blue}1 & \color{Red}0 & \color{Blue}1 & \color{Red}1 \\
      \color{Blue}1 & \color{Blue}0 & \color{Blue}1 & \color{Blue}0 \\
      \color{Blue}0 & 1 & \color{Blue}0 & 1
    \end{pmatrix}
    $$

9.  Odaberemo sve označene retke i izbrišemo ih;

    $$
    \begin{pmatrix}
      \color{Blue}1 & \color{Blue}0 & \color{Blue}1 & \color{Blue}1 \\
      \color{Blue}1 & \color{Blue}0 & \color{Blue}1 & \color{Blue}0 \\
      \color{Blue}0 & 1 & \color{Blue}0 & 1
      \end{pmatrix}
    $$

    Tako dobivamo ovakvu matricu:

    $$
    \begin{pmatrix}
      1 & 1
    \end{pmatrix}
    $$

10. Sad prvi redak (izvorno peti) ima $2$ jedinice; sve ih izbrišemo i dobijemo praznu matricu:

    $$
    \begin{pmatrix}
    \end{pmatrix}
    $$

11. Pri posljednjem brisanju izbrisan je redak sav od jedinica, pa je postupak uspio i algoritam završava.

    Odgovor su tri izbrisana retka: $1, 4, 5$.

Toplo preporučujemo da sami simulirate postupak brisanja, vraćanja i backtrackinga u matrici prije nego što nastavite čitati.

Iz gornjih koraka tijek algoritma X može se sažeti ovako:

1.  U trenutnoj matrici $M$ odaberi i označi redak $r$ te dodaj $r$ u $S$;
2.  ako su isprobani svi $r$, a rješenja nema, algoritam završava i ispisuje da rješenja nema;
3.  označi retke $r_i$ i stupce $c_i$ povezane s $r$ (povezani reci i stupci definirani su kao u 2. koraku [algoritma X](#postupak); isto vrijedi dalje);
4.  izbriši sve označene retke i stupce i dobij novu matricu $M'$;
5.  ako je $M'$ prazna, a $r$ sav od jedinica, algoritam završava i ispisuje skup $S$ izbrisanih redaka;

    ako je $M'$ prazna, a $r$ nije sav od jedinica, vrati retke $r_i$ i stupce $c_i$ povezane s $r$ i skoči na 1. korak;

    ako $M'$ nije prazna, skoči na 1. korak.

Lako se vidi da algoritam X zahtijeva velik broj operacija „brisanja retka”, „brisanja stupca”, „vraćanja retka” i „vraćanja stupca”.

Naivna je ideja matricu čuvati u dvodimenzionalnom nizu i uz to u četiri niza čuvati, za svaki redak, brojeve susjednih redaka; svako brisanje i vraćanje tada traži ažuriranje elemenata samo u ta četiri niza. No budući da u matricama uobičajenih problema nula ima daleko više nego jedinica, prostorna složenost takvog pristupa teško je prihvatljiva.

Donald E. Knuth smislio je te operacije održavati dvostruko povezanom križnom listom.

Neprestano skakanje po toj listi slikovito je nazvano „plesom”, pa se dvostruko povezana križna lista kojom se optimizira algoritam X naziva i „Dancing Links”.

## Algoritam X optimiziran Dancing Linksom

### Predprocesorska naredba

```cpp
#define IT(i, A, x) for (i = A[x]; i != x; i = A[i])
```

### Definicija

U dvostruko povezanoj križnoj listi postoje četiri polja pokazivača, koja pokazuju na gornji, donji, lijevi i desni element; osim toga, svaki element $i$ u cijelom sustavu liste odgovara jednom polju matrice, pa treba zapisati i stupac i redak u kojem se $i$ nalazi, kao na slici:

![dlx-1.svg](./images/dlx-1.svg)

Velika dvostruko povezana lista složenija je:

![dlx-2.svg](./images/dlx-2.svg)

Svaki redak ima pokazivač na početak retka, a svaki stupac ima oznaku stupca.

Pokazivači na početke redaka su `first[]`, a oznake stupaca su $c + 1$ novostvorenih čvorova-stražara. Vrijedi istaknuti da **pokazivač na početak retka nije čvor-stražar u listi**. On je virtualan, nalik nizu `first[]` u listi susjedstva, i **izravno pokazuje** na prvi element tog retka.

Uz to, svaki stupac ima `siz[]` koji označava broj elemenata u tom stupcu.

Posebno, ako čvor $0$ nema desnog čvora, to znači da je ovaj Dancing Links prazan.

```cpp
constexpr int MS = 1e5 + 5;
int n, m, idx, first[MS], siz[MS];
int L[MS], R[MS], U[MS], D[MS];
int col[MS], row[MS];
```

### Postupak

#### Operacija remove

`remove(c)` označava brisanje stupca $c$ iz Dancing Linksa, zajedno s njim povezanim recima i stupcima.

Najprije izbrišemo $c$; tada:

-   desni čvor čvora lijevo od $c$ treba biti desni čvor od $c$.
-   lijevi čvor čvora desno od $c$ treba biti lijevi čvor od $c$.

Odnosno `L[R[c]] = L[c], R[L[c]] = R[c];`.

![dlx-3.svg](./images/dlx-3.svg)

Zatim se spuštamo duž tog stupca i brišemo svaki redak kroz koji prođemo.

Kako izbrisati redak? Nabrajamo pokazivač $j$ trenutnog retka; tada:

-   donji čvor čvora iznad $j$ treba biti donji čvor od $j$.
-   gornji čvor čvora ispod $j$ treba biti gornji čvor od $j$.

Pripazite da treba ažurirati i broj elemenata svakog stupca.

Odnosno `U[D[j]] = U[j], D[U[j]] = D[j], --siz[col[j]];`.

![dlx-4.svg](./images/dlx-4.svg)

Implementacija funkcije `remove` glasi:

???+ note "Implementacija"
    ```cpp
    void remove(const int &c) {
      int i, j;
      L[R[c]] = L[c], R[L[c]] = R[c];
      // prođi ovim stupcem odozgo prema dolje
      IT(i, D, c)
      // prođi ovim retkom slijeva nadesno
      IT(j, R, i)
      U[D[j]] = U[j], D[U[j]] = D[j], --siz[col[j]];
    }
    ```

#### Operacija recover

`recover(c)` označava vraćanje stupca $c$ u Dancing Links, zajedno s njim povezanim recima i stupcima.

`recover(c)` je inverzna operacija od `remove(c)`, pa je ovdje ne objašnjavamo ponovno.

**Vrijedi istaknuti da je** redoslijed svih operacija u `recover(c)` **točno obrnut od** redoslijeda u `remove(c)`**.**

Implementacija `recover(c)` glasi:

???+ note "Implementacija"
    ```cpp
    void recover(const int &c) {
      int i, j;
      IT(i, U, c) IT(j, L, i) U[D[j]] = D[U[j]] = j, ++siz[col[j]];
      L[R[c]] = R[L[c]] = c;
    }
    ```

#### Operacija build

`build(r, c)` označava stvaranje novog Dancing Linksa veličine $r \times c$, tj. s $r$ redaka i $c$ stupaca.

Stvorimo $c + 1$ čvorova kao oznake stupaca.

Lijevi čvor $i$-tog čvora je $i - 1$, desni je $i + 1$, gornji je $i$, a donji je $i$. Posebno, lijevi čvor čvora $0$ je $c$, a desni čvor čvora $c$ je $0$.

Tako dobivamo kružnu dvostruko povezanu listu:

![dlx-5.svg](./images/dlx-5.svg)

Time je Dancing Links inicijaliziran.

Implementacija `build(r, c)` glasi:

???+ note "Implementacija"
    ```cpp
    void build(const int &r, const int &c) {
      n = r, m = c;
      for (int i = 0; i <= c; ++i) {
        L[i] = i - 1, R[i] = i + 1;
        U[i] = D[i] = i;
      }
      L[0] = c, R[c] = 0, idx = c;
      memset(first, 0, sizeof(first));
      memset(siz, 0, sizeof(siz));
    }
    ```

#### Operacija insert

`insert(r, c)` označava umetanje čvora u redak $r$ i stupac $c$.

Umetanje ima dva slučaja:

-   Ako redak $r$ nema elemenata, jednostavno umetnemo element i usmjerimo `first[r]` na njega.

    To se postiže s `first[r] = L[idx] = R[idx] = idx;`.

-   Ako redak $r$ ima elemenata, novi element na poseban način povežemo s $c$ i $first(r)$.

    Neka je novi element $idx$; tada:

    -   Umetnemo $idx$ točno ispod $c$; tada:

        -   čvor ispod $idx$ je prijašnji donji čvor od $c$;
        -   gornji čvor čvora ispod $idx$ (tj. prijašnjeg donjeg čvora od $c$) je $idx$;
        -   gornji čvor od $idx$ je $c$;
        -   donji čvor od $c$ je $idx$.

        Pripazite da zapišete stupac i redak u kojem je $idx$ te ažurirate broj elemenata tog stupca.

        ```cpp
        col[++idx] = c, row[idx] = r, ++siz[c];
        U[idx] = c, D[idx] = D[c], U[D[c]] = idx, D[c] = idx;
        ```

        **Toplo preporučujemo da čitatelj potpuno ovlada redoslijedom ovih koraka prije nego što nastavi čitati.**

    -   Umetnemo $idx$ točno desno od $first(r)$; tada:

        -   čvor desno od $idx$ je prijašnji desni čvor od $first(r)$;
        -   lijevi čvor prijašnjeg desnog čvora od $first(r)$ je $idx$;
        -   lijevi čvor od $idx$ je $first(r)$;
        -   desni čvor od $first(r)$ je $idx$.

        ```cpp
        L[idx] = first[r], R[idx] = R[first[r]];
        L[R[first[r]]] = idx, R[first[r]] = idx;
        ```

        **Toplo preporučujemo da čitatelj potpuno ovlada redoslijedom ovih koraka prije nego što nastavi čitati.**

Operaciju `insert(r, c)` lakše je razumjeti uz sliku:

![dlx-6.svg](./images/dlx-6.svg)

Obratite pažnju na smjer zakrivljenih strelica.

Implementacija `insert(r, c)` glasi:

???+ note "Implementacija"
    ```cpp
    void insert(const int &r, const int &c) {
      row[++idx] = r, col[idx] = c, ++siz[c];
      U[idx] = c, D[idx] = D[c], U[D[c]] = idx, D[c] = idx;
      if (!first[r])
        first[r] = L[idx] = R[idx] = idx;
      else {
        L[idx] = first[r], R[idx] = R[first[r]];
        L[R[first[r]]] = idx, R[first[r]] = idx;
      }
    }
    ```

#### Operacija dance

`dance()` je postupak rekurzivnog brisanja i vraćanja redaka i stupaca.

1.  Ako čvor $0$ nema desnog čvora, matrica je prazna; zapiši odgovor i vrati se;
2.  odaberi stupac s najmanjim brojem elemenata i izbriši ga;
3.  prođi sve retke koji u tom stupcu imaju $1$ i nabroji je li svaki od njih odabran;
4.  rekurzivno pozovi `dance()`; ako je izvedivo, vrati se; ako nije, vrati odabrani redak;
5.  ako rješenja nema, vrati se.

Implementacija `dance()` glasi:

???+ note "Implementacija"
    ```cpp
    bool dance(int dep) {
      int i, j, c = R[0];
      if (!R[0]) {
        ans = dep;
        return true;
      }
      IT(i, R, 0) if (siz[i] < siz[c]) c = i;
      remove(c);
      IT(i, D, c) {
        stk[dep] = row[i];
        IT(j, R, i) remove(col[j]);
        if (dance(dep + 1)) return true;
        IT(j, L, i) recover(col[j]);
      }
      recover(c);
      return false;
    }
    ```

Pritom `stk[]` služi za zapisivanje odgovora.

Uočite da za brisanje uvijek prvo biramo stupac s najmanjim brojem elemenata; to programu daje određenu heurističnost i čini stablo pretraživanja što manje razgranatim.

Kod problema ponovljenog pokrivanja pri pretraživanju se može odsijecati funkcijom procjene (slično kao u [A\*](astar.md)): ako broj odabranih redaka u trenutno najboljem slučaju premašuje dosad najbolje rješenje, možemo se odmah vratiti.

## Predložak

??? note "[Kod predloška](https://www.luogu.com.cn/problem/P4929)"
    ```cpp
    --8<-- "docs/search/code/dlx/dlx_1.cpp"
    ```

## Svojstva

Broj rekurzija i backtrackinga u DLX-u ovisi o broju jedinica u matrici, a ne o parametrima $r, c$ i sl. Zato je njegova vremenska složenost **eksponencijalna**; teorijska je složenost otprilike $O(c^n)$, gdje je $c$ neka konstanta vrlo blizu $1$, a $n$ broj jedinica u matrici.

U praksi se DLX ipak ponaša dobro i obično rješava većinu zadataka.

## Modeliranje

Težina DLX-a nije samo u izgradnji liste, nego u modeliranju.

Nastavite čitati tek kad potpuno ovladate predloškom DLX-a.

Kad dobijemo zadatak, treba razmisliti što predstavljaju reci i stupci:

-   reci predstavljaju *odluke*, jer svaki redak odgovara jednom skupu, dakle odabiru/neodabiru;

-   stupci predstavljaju *stanja*, jer $i$-ti stupac odgovara nekom uvjetu $P_i$.

Za pojedini redak, budući da vrijednosti u različitim stupcima nisu jednake, **iz različitih stanja definiramo jednu odluku**.

### Primjer 1 [P1784 Sudoku](https://www.luogu.com.cn/problem/P1784)

??? note "Ideja rješenja"
    Najprije razmotrimo što je odluka.
    
    U ovom zadatku svaka se odluka može prikazati uređenom trojkom oblika $(r, c, w)$.
    
    Uočite da „blok” nije parametar odluke, jer **se može izraziti svakim određenim $(r, c)$**.
    
    Zato imamo $9 \times 9 \times 9 = 729$ redaka.
    
    Zatim razmotrimo što je stanje.
    
    Razmislimo kakve posljedice ima odluka $(r, c, w)$. Neka je $b$ blok u kojem se nalazi $(r, c)$.
    
    1.  U retku $r$ iskorišten je jedan $w$ (prikazano s $9 \times 9 = 81$ stupcem);
    2.  u stupcu $c$ iskorišten je jedan $w$ (prikazano s $9 \times 9 = 81$ stupcem);
    3.  u bloku $b$ iskorišten je jedan $w$ (prikazano s $9 \times 9 = 81$ stupcem);
    4.  u $(r, c)$ upisan je broj (prikazano s $9 \times 9 = 81$ stupcem).
    
    Zato imamo $81 \times 4 = 324$ stupca i ukupno $729 \times 4 = 2916$ jedinica.
    
    Time smo sudoku $9 \times 9$ uspješno pretvorili u problem točnog pokrivanja **sa $729$ redaka, $324$ stupca i ukupno $2916$ jedinica**.

??? note "Primjer rješenja"
    ```cpp
    --8<-- "docs/search/code/dlx/dlx_2.cpp"
    ```

### Primjer 2 [Sudoku s metom](https://www.luogu.com.cn/problem/P1074)

??? note "Ideja rješenja"
    Model ovog zadatka **potpuno je jednak** modelu [sudokua](https://www.luogu.com.cn/problem/P1784); glavna je razlika u ažuriranju odgovora.
    
    Možemo uvesti niz težina i svaki put kad nađemo rješenje sudokua
    
    broj na svakom mjestu pomnožiti pripadnom težinom i pribrojiti odgovoru.

??? note "Primjer rješenja"
    ```cpp
    --8<-- "docs/search/code/dlx/dlx_3.cpp"
    ```

### Primjer 3 [„NOI2005” Igra pametnih perli](https://www.luogu.com.cn/problem/P4205)

??? note "Ideja rješenja"
    Definicija: oblik perle kako je zadan u zadatku zovemo *standardnim oblikom* te perle.
    
    Očito oblik perle možemo mijenjati pomoću dvaju parametara: $d$ (broj rotacija za $90^{\circ}$ u smjeru kazaljke na satu) i $f$ (je li vodoravno zrcaljena).
    
    Opet najprije razmotrimo što je odluka.
    
    U ovom zadatku svaka se odluka može prikazati uređenom četvorkom oblika $(v, d, f, i)$.
    
    Ona označava da je $i$-ta perla u *standardnom obliku* postavljena tako da joj je gornji lijevi kut na položaju $v$, nakon $d$ rotacija za $90^{\circ}$ u smjeru kazaljke na satu.
    
    Prikladno je uzeti da $f = 1$ znači bez vodoravnog zrcaljenja, a $f = -1$ s vodoravnim zrcaljenjem, što pojednostavnjuje kod.
    
    Zato imamo $55 \times 4 \times 2 \times 12 = 5280$ redaka.
    
    Treba imati na umu da zbog nekih nevaljanih postavljanja, npr. $(1, 0, 1, 4)$,
    
    **u praksi za praznu ploču treba izgraditi samo $2730$ redaka.**
    
    Zatim razmotrimo što je stanje.
    
    Stanje je u ovom zadatku razmjerno jednostavno.
    
    Razmislimo kakve posljedice ima odluka $(v, d, f, i)$.
    
    1.  Neka su polja zauzeta (prikazano s $55$ stupaca);
    2.  $i$-ta perla je iskorištena (prikazano s $12$ stupaca).
    
    Zato imamo $55 + 12 = 67$ stupaca i ukupno $5280 \times (5 + 1) = 31680$ jedinica.
    
    Time smo igru pametnih perli uspješno pretvorili u problem točnog pokrivanja **s $5280$ redaka, $67$ stupaca i ukupno $31680$ jedinica**.

??? note "Primjer rješenja"
    ```cpp
    --8<-- "docs/search/code/dlx/dlx_4.cpp"
    ```

## Zadaci za vježbu

-   [SUDOKU - Sudoku](https://www.spoj.com/problems/SUDOKU/)
-   [„kuangbin” – tema 3: Dancing Links](https://vjudge.net/contest/65998#overview)

## Vanjske poveznice

-   [Plesač koji skače: algoritam Dancing Links za problem točnog pokrivanja – 万仓一黍 (kineski)](https://www.cnblogs.com/grenet/p/3145800.html)
-   [Pretraživanje: algoritam DLX – 静听风吟 (kineski)](https://www.cnblogs.com/aininot260/p/9629926.html)
-   [*Training Guide for Beginners in Algorithm Competitions* (《算法竞赛入门经典 - 训练指南》)](https://book.douban.com/subject/35431537/)

## Bilješke

[^note1]: (Razlika u nazivlju između kontinentalne Kine i Tajvana) Tajvan: 直行 (column), 橫列 (row)
