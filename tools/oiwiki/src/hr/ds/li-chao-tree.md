---
title: Li Chao tree
---

## Uvod

???+ note "[Luogu 4097 \[HEOI2013\]Segment](https://www.luogu.com.cn/problem/P4097)"
    U ravnini s pravokutnim koordinatnim sustavom treba podržati dvije operacije (prisilno online):
    
    1.  Dodaj dužinu u ravninu. Oznaka $i$-te umetnute dužine je $i$, a njezini su krajevi $(x_0,y_0)$ i $(x_1,y_1)$.
    2.  Za zadani broj $k$ odgovori koja dužina među onima koje sijeku pravac $x = k$ ima sjecište s najvećom ordinatom (ako više dužina ima jednako najveću ordinatu sjecišta, ispiši onu s najmanjom oznakom). Posebno, ako nijedna dužina ne siječe zadani pravac, ispiši $0$.
    
    Ograničenja: ukupan broj operacija $1 \leq n \leq 10^5$, $1 \leq k, x_0, x_1 \leq 39989$, $1 \leq y_0, y_1 \leq 10^9$.

Uočavamo da klasični segment tree ne može dobro održavati ovakve informacije. U takvim situacijama nastaje **Li Chao tree** (Li Chao segment tree).

## Postupak

Zadatak možemo preoblikovati u održavanje sljedećih operacija:

-   dodaj linearnu funkciju s domenom $[l,r]$;
-   za zadani $k$, među svim linearnim funkcijama čija domena sadrži $k$ nađi onu s najvećom vrijednošću u $x=k$; ako više funkcija ima istu vrijednost, uzmi onu s najmanjom oznakom.

???+ warning "Napomena"
    Kad je dužina okomita na os $x$, dolazi do dijeljenja nulom. Ako su krajevi dužine $(x,y_0)$ i $(x,y_1)$, $y_0<y_1$, umetnemo linearnu funkciju $f(x)=0\cdot x+y_1$ s domenom $[x,x]$.

Budući da se radi o intervalnoj izmjeni, prema uobičajenom načinu na koji segment tree rješava intervalne probleme svakom čvoru dajemo lijenu oznaku. Lijena oznaka svakog čvora $i$ jedna je dužina, označimo je $l_i$; znači da cijeli interval koji čvor predstavlja treba ažurirati dužinom $l_i$.

Sada treba umetnuti dužinu $f$. Promotrimo neki interval segment treea koji nova dužina $f$ potpuno pokriva. Ako taj interval nema oznaku, izravno mu postavimo oznaku da ga treba ažurirati tom dužinom.

Ako interval već ima oznaku, budući da je oznake teško spojiti, možemo je samo spustiti. Ali i djeca imaju svoje oznake, pa opet može doći do sukoba; zato oznake spuštamo rekurzivno.

![](images/li-chao-tree-1.png)

Kao na slici, prema tome je li vrijednost nove dužine $f$ veća od izvorne oznake $g$, trenutni interval možemo podijeliti na dva podintervala. Pri tome je **jedan od njih sigurno potpuno sadržan u lijevom ili desnom intervalu**; drugim riječima, od dviju dužina jedna sigurno može biti odgovor samo za lijevi interval ili samo za desni interval. Tom dužinom rekurzivno ažuriramo odgovarajuće podstablo, a drugom kao lijenom oznakom ažuriramo cijeli interval; to jamči složenost rekurzivnog spuštanja. Dužina se spušta samo kad može biti odgovor samo za lijevi ili samo za desni interval, pa se ne treba brinuti da će neka dužina biti propuštena.

Konkretno, neka je $m$ sredina trenutnog intervala; usporedimo vrijednost nove dužine $f$ u sredini s vrijednošću dosadašnje najbolje dužine $g$ u sredini.

Ako je nova dužina $f$ bolja, zamijenimo $f$ i $g$. Sada promotrimo slučaj kad $f$ u sredini nije bolja od $g$:

1.  Ako je u lijevom kraju $f$ bolja, onda se $f$ i $g$ sigurno sijeku u lijevoj polovici; $f$ može biti bolja od $g$ samo u lijevom intervalu, pa je rekurzivno spuštamo u lijevo dijete.
2.  Ako je u desnom kraju $f$ bolja, onda se $f$ i $g$ sigurno sijeku u desnoj polovici; $f$ može biti bolja od $g$ samo u desnom intervalu, pa je rekurzivno spuštamo u desno dijete.
3.  Ako je u oba kraja $g$ bolja, $f$ ne može biti odgovor i ne treba je dalje spuštati.

Osim tih slučajeva, postoji i slučaj kad se $f$ i $g$ sijeku upravo u sredini; u implementaciji ga možemo svrstati u slučaj kad $f$ u sredini nije bolja od $g$, pa će se rekurzivno spustiti prema kraju u kojem je $f$ bolja.

Na kraju $g$ postaje lijena oznaka trenutnog intervala.

Spuštanje oznake:

???+ note "Implementacija"
    ```cpp
    constexpr double eps = 1e-9;
    
    int cmp(double x, double y) {  // zbog brojeva s pomičnim zarezom postoji pogreška preciznosti
      if (x - y > eps) return 1;
      if (y - x > eps) return -1;
      return 0;
    }
    
    //...
    
    void upd(int root, int cl, int cr, int u) {  // izmijeni interval koji dužina potpuno pokriva
      int &v = s[root], mid = (cl + cr) >> 1;
      int bmid = cmp(calc(u, mid), calc(v, mid));
      if (bmid == 1 || (!bmid && u < v))  // u ovom zadatku ne zaboravi usporediti oznake dužina
        swap(u, v);
      int bl = cmp(calc(u, cl), calc(v, cl)), br = cmp(calc(u, cr), calc(v, cr));
      if (bl == 1 || (!bl && u < v)) upd(root << 1, cl, mid, u);
      if (br == 1 || (!br && u < v)) upd(root << 1 | 1, mid + 1, cr, u);
      // najviše jedan od gornja dva uvjeta može vrijediti, što jamči složenost Li Chao treea
    }
    ```

Rastavljanje dužine:

???+ note "Implementacija"
    ```cpp
    void update(int root, int cl, int cr, int l, int r,
                int u) {  // pronađi intervale koje umetnuta dužina potpuno pokriva
      if (l <= cl && cr <= r) {
        upd(root, cl, cr, u);  // potpuno pokriva trenutni interval, ažuriraj njegovu oznaku
        return;
      }
      int mid = (cl + cr) >> 1;
      if (l <= mid) update(root << 1, cl, mid, l, r, u);  // rekurzivno rastavi interval
      if (mid < r) update(root << 1 | 1, mid + 1, cr, l, r, u);
    }
    ```

Pazite: lijena oznaka nije isto što i dužina s najvećom vrijednošću u sredini intervala.

![](images/li-chao-tree-2.png)

Kao na slici, nakon dodavanja žute dužine ažurirana je samo oznaka crvenog čvora, a oznake zelenih čvorova nisu se promijenile. Ali u sredinama drugog, trećeg i četvrtog zelenog intervala očito žuta dužina ima najveću vrijednost.

Pri upitu možemo iskoristiti ideju trajnih oznaka: među oznakama (dužinama) svih intervala segment treea koji sadrže $x$ (najviše $O(\log n)$ njih) usporedbom dobijemo konačan odgovor.

Upit:

???+ note "Implementacija"
    ```cpp
    pdi query(int root, int l, int r, int d) {  // upit
      if (r < d || d < l) return {0, 0};
      int mid = (l + r) >> 1;
      double res = calc(s[root], d);
      if (l == r) return {res, s[root]};
      return pmax({res, s[root]}, pmax(query(root << 1, l, mid, d),
                                       query(root << 1 | 1, mid + 1, r, d)));
    }
    ```

Prema gornjem opisu vremenska složenost upita očito je $O(\log n)$, a pri umetanju izvornu dužinu treba rastaviti na $O(\log n)$ intervala i za svaki od njih potrošiti $O(\log n)$ na rekurzivno spuštanje, pa je vremenska složenost umetanja $O(\log^2 n)$.

??? note "Referentni kod za [\[HEOI2013\]Segment](https://www.luogu.com.cn/problem/P4097)"
    ```cpp
    --8<-- "docs/ds/code/li-chao-tree/li-chao-tree_1.cpp"
    ```

## Spajanje

Slično spajanju običnih segment treeova, definiramo sljedeći postupak za spajanje dvaju čvorova Li Chao treea $u,v$, pri čemu $u$ postaje novi korijen.

1.  Ako je $v$ prazan, postupak završava.

2.  Ako je $u$ prazan, kopiraj $v$ u $u$.

3.  Umetni dužinu koja odgovara $v$ u podstablo s korijenom $u$.

4.  Rekurzivno spoji lijeva odnosno desna podstabla od $u$ i $v$.

Ako je ukupan broj čvorova u svim Li Chao treeovima koji se spajaju $n$, složenost je tog postupka $O(n\log n)$: za čvor koji odgovara bilo kojoj dužini, svaki put kad ga pomičemo ili mu se dubina poveća za $1$ ili ga izravno brišemo iz stabla, a obje operacije stoje $O(1)$; dubina svakog čvora najviše je $O(\log n)$, odakle slijedi složenost.

???+ note "Implementacija"
    ```cpp
    void upd(int &root, int cl, int cr,
             int u) {  // spaja se više Li Chao treeova, koristi se dinamičko stvaranje čvorova
      static int idx = 0;
      if (!root) {
        s[root = ++idx] = u;
        return;
      }
      int &v = s[root], mid = (cl + cr) >> 1;
      int bmid = cmp(calc(u, mid), calc(v, mid));
      if (bmid == 1 || (!bmid && u < v)) swap(u, v);
      int bl = cmp(calc(u, cl), calc(v, cl)), br = cmp(calc(u, cr), calc(v, cr));
      if (bl == 1 || (!bl && u < v)) upd(ls[root], cl, mid, u);
      if (br == 1 || (!br && u < v)) upd(rs[root], mid + 1, cr, u);
    }
    
    int merge(int &u, int &v, int l, int r) {
      if (!u || !v) {
        return u + v;
      }
      if (l == r) {
        int b = cmp(calc(s[v], l), calc(s[u], l));
        if (b == 1 || (!b && s[v] < s[u])) return v;
        return u;
      }
      upd(u, l, r, s[v]);
      int mid = (l + r) >> 1;
      ls[u] = merge(ls[u], ls[v], l, mid);
      rs[u] = merge(rs[u], rs[v], mid + 1, r);
      return u;
    }
    ```

## Zadaci za vježbu

[「JSOI2008」Blue Mary 开公司](https://www.luogu.com.cn/problem/P4254)

[「CodeChef」TSUM2 Sum on Tree](https://www.codechef.com/problems/TSUM2)

[「USACO13MAR」Hill Walk G](https://www.luogu.com.cn/problem/P3081)

[「CF932F」Escape Through Leaf](https://codeforces.com/problemset/problem/932/F)
