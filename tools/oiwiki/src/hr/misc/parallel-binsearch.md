---
title: Paralelno binarno pretraživanje
---

## Uvod

Na natjecanjima iz informatike dio zadataka može se riješiti binarnim pretraživanjem. No kad takav zadatak ima više upita, a izravno binarno pretraživanje za svaki upit moglo bi dovesti do TLE-a, koristi se paralelno binarno pretraživanje (parallel binary search). Glavna je ideja paralelnog binarnog pretraživanja riješiti više upita zajedno. (Zato je ovo offline algoritam.)

Zadaci rješivi paralelnim binarnim pretraživanjem moraju zadovoljavati sljedeća svojstva[^ref1]:

1.  odgovor na upit može se binarno pretraživati;
2.  **doprinosi izmjena provjeri odgovora međusobno su neovisni**, izmjene ne utječu jedna na drugu;
3.  ako izmjena doprinosi provjeri odgovora, doprinos je određena vrijednost neovisna o kriteriju provjere;
4.  doprinosi zadovoljavaju komutativnost i asocijativnost te su aditivni;
5.  zadatak dopušta offline algoritam.

## Objašnjenje

Označimo s $[l,r]$ raspon vrijednosti odgovora, a s $[L,R]$ domenu odgovora. (Drugim riječima, pri računanju odgovora razmatraju se samo operacije i upiti s indeksima u intervalu $[L,R]$, a odgovori tih upita leže u $[l,r]$.)

-   Najprije sve operacije **kronološkim redoslijedom** spremimo u polje, a zatim započnemo podjelu.
-   Na svakoj razini podjele pomoću strukture podataka (najčešće Fenwick treeja) utvrdimo odnos između odgovora trenutnih upita i $mid$.
-   Prema odnosu utvrđenog odgovora i $mid$ (manji ili jednak $mid$, odnosno veći od $mid$) niz operacija koji trenutno obrađujemo podijelimo na dva dijela, $q1$ i $q2$, i svaki rekurzivno obradimo.
-   Kad je $l=r$, odgovor je pronađen; zabilježimo ga i vratimo se.

Valja uočiti da se tijekom paralelnog binarnog pretraživanja, ako je raspon vrijednosti koji trenutno obrađujemo $[l,r]$, upiti čiji konačni odgovor nije u $[l,r]$ obrađuju u nekom drugom trenutku.

## Postupak

???+ tip "Napomena"
    1.  Radi čitljivosti kôd u tekstu možda ne slijedi uobičajeni stil pisanja s pravih natjecanja.
    2.  Ako vam je neki dio koda teško razumljiv, najprije pogledajte objašnjenja prethodnih zadataka, jer se radi uštede prostora već objašnjeni sadržaj ne ponavlja.

Krenimo od običnog binarnog pretraživanja:

### Upit za globalno k-ti najmanji

???+ note "Zadatak 1"
    U nizu brojeva pronađite $k$-ti najmanji broj.

??? note "Rješenje"
    Naravno, može se izravno sortirati. A binarnim pretraživanjem? Strukturom podataka možemo zabilježiti koliko brojeva ima u svakom rasponu vrijednosti, zatim binarnim pretraživanjem pogađati, a strukturom podataka provjeravati.

???+ note "Zadatak 2"
    U nizu brojeva više puta pronađite $k$-ti najmanji broj.

??? note "Rješenje"
    Možemo za svaki upit provesti jedno binarno pretraživanje; ali možemo i sve upite zajedno binarno pretraživati.
    
    Razmotrimo najprije bit binarnog pretraživanja: pretpostavimo da treba pogoditi broj iz $[l,r]$ i da nakon pogađanja saznamo je li pogodak prevelik, premalen ili točan. Naravno, možemo iterirati od $l$ do $r$, ali bolja je metoda binarno pretraživanje: pogodimo da je odgovor $m = \lfloor\frac{l + r}{2}\rfloor$, zatim provjerimo ispravnost $m$ i prilagodimo granice. Tako je složenost svakog upita $O(\log n)$; ako je broj upita $q$, vremenska složenost je $O(q\log n)$.
    
    Vratimo se sada: za sve trenutne upite možemo pretpostaviti da je odgovor na svaki od njih $mid$, zatim redom za svaki upit provjeriti treba li odgovor biti manji ili jednak $mid$ ili veći od $mid$, podijeliti upite na dva dijela (ne veći/veći) i za svaki dio nastaviti binarno pretraživanje. Napomena: ako je odgovor na upit veći od $mid$, prije nego što ga prebacimo na desnu stranu treba ažurirati njegov $k$, tj. ako u trenutnom nizu ima $t$ brojeva manjih ili jednakih $mid$, tada nakon podjele upit u desnom intervalu zapravo traži $k - t$-ti najmanji broj. Ako za neki dio vrijedi $l = r$, binarno pretraživanje tog dijela završava. Služeći se znanjem o segment treeju: cijeli interval $[1,n]$ u kojem odgovor može biti (uz pretpostavku da je već diskretiziran) svaki put dijelimo na nekoliko dijelova, takvih podjela ima ukupno $O(\log n)$, a jedna podjela prolazi kroz cijeli niz operacija jednom. Ako obrada cijelog niza uz podršku odgovarajućih upita ima vremensku složenost $O(T)$, vremenska složenost paralelnog binarnog pretraživanja je $O(T\log n)$.

??? note "Primjer koda"
    ```cpp
    struct Query {
      int id, k;  // oznaka ovog upita, k ovog upita
    };
    
    int ans[N], a[N];  // ans[i] je odgovor na upit s oznakom i, a je izvorni niz
    int val[N], cnt[N];  // nakon diskretizacije, odgovarajuće vrijednosti i njihov broj (pretpostavlja se da su već izračunati)
    
    // vraća broj elemenata izvornog niza čija je vrijednost u [l,r]
    int check(int l, int r) {
      int res = 0;
      for (int i = l; i <= r; i++) {
        res += cnt[i];
      }
      return res;
    }
    
    // paralelno binarno pretraživanje
    void solve(int l, int r, vector<Query> q) {
      int m = (l + r) / 2;
      if (l == r) {
        for (unsigned i = 0; i < q.size(); i++) ans[q[i].id] = val[l];
        return;
      }
      vector<Query> q1, q2;
      int t = check(l, m);
      for (unsigned i = 0; i < q.size(); i++) {
        if (q[i].k <= t)
          q1.push_back(q[i]);
        else
          q[i].k -= t, q2.push_back(q[i]);
      }
      solve(l, m, q1), solve(m + 1, r, q2);
      return;
    }
    ```

### Upit za k-ti najmanji na intervalu

???+ note "Zadatak 3"
    U nizu brojeva više puta pronađite $k$-ti najmanji broj na intervalu.

??? note "Rješenje"
    Kad se upiti odnose na zadani interval, binarno pretraživanje po prethodnoj metodi dovelo bi do eksplozije vremenske složenosti funkcije `check`. I dalje razmatramo odnos upita i sredine raspona vrijednosti $m$: ako u intervalu upita ima $t$ brojeva manjih ili jednakih $m$, a traži se $k$-ti najmanji broj u intervalu, tada za $k \leq t$ odgovor mora biti manji ili jednak $m$; inače odgovor mora biti veći od $m$. (Pazite na rubne slučajeve.) Ovdje treba bilježiti broj elemenata u intervalu manjih ili jednakih zadanom broju, tj. dodavanje u točki i zbroj na intervalu, što se brzo obrađuje Fenwick treejem. Radi učinkovitosti brojimo samo elemente niza čija je vrijednost u rasponu $[l,r]$, tj. prije daljnje rekurzije ne dijelimo samo upite, nego i trenutno obrađivane brojeve dijelimo na dvije polovice prema rasponu vrijednosti.

??? note "Primjer koda (ključni dio)"
    ```cpp
    struct Num {
      int p, x;
    };  // broj na p-tom mjestu u nizu ima vrijednost x
    
    struct Query {
      int l, r, k, id;
    };  // upit s oznakom id koji traži k-ti najmanji broj u [l,r]
    
    int ans[N];
    void add(int p, int x);  // Fenwick tree, na poziciju p dodaj x
    int query(int p);        // Fenwick tree, zbroj na [1,p]
    void clear();            // Fenwick tree, isprazni
    
    void solve(int l, int r, vector<Num> a, vector<Query> q)
    // u a su brojevi zadanog niza čija je vrijednost u rasponu [l,r]
    {
      int m = (l + r) / 2;
      if (l == r) {
        for (unsigned i = 0; i < q.size(); i++) ans[q[i].id] = l;
        return;
      }
      vector<Num> a1, a2;
      vector<Query> q1, q2;
      for (unsigned i = 0; i < a.size(); i++)
        if (a[i].x <= m)
          a1.push_back(a[i]), add(a[i].p, 1);
        else
          a2.push_back(a[i]);
      for (unsigned i = 0; i < q.size(); i++) {
        int t = query(q[i].r) - query(q[i].l - 1);
        if (q[i].k <= t)
          q1.push_back(q[i]);
        else
          q[i].k -= t, q2.push_back(q[i]);
      }
      clear();
      solve(l, m, a1, q1), solve(m + 1, r, a2, q2);
      return;
    }
    ```

U nastavku dajemo natjecateljski stil implementacije paralelnog binarnog pretraživanja za zadatak [【模板】可持久化线段树 2 (Predložak: perzistentni segment tree 2)](https://www.luogu.com.cn/problem/P3834).

??? note "Primjer koda"
    ```cpp
    --8<-- "docs/misc/code/parallel-binsearch/parallel-binsearch_1.cpp"
    ```

### K-ti najmanji na intervalu s izmjenama

???+ note "Zadatak 4 ([Dynamic Rankings](https://www.luogu.com.cn/problem/P2617))"
    Zadan je niz brojeva; treba podržati izmjenu u točki i upit za $k$-ti najmanji na intervalu.

??? note "Rješenje"
    Operaciju izmjene možemo shvatiti kao brisanje jednog broja iz izvornog niza i dodavanje drugog; radi jednostavnosti upite i izmjene zajednički nazivamo „operacijama”. Budući da kasnije operacije ovise o prethodnima, ne možemo kao u zadatku 3 odvojiti brojanje od obrade upita, pa sve operacije spremamo u jedno polje, oznakom razlikujemo tip i obrađujemo operacije redom. Radi lakše obrade Fenwick treejem, operaciju izmjene možemo rastaviti na operaciju brisanja i operaciju umetanja.
    
    **Optimizacije**
    
    1.  Uočimo da se pri svakom razvrstavanju operacija mijenja samo njihov redoslijed, pa možemo raditi izravno na izvornom polju. Konkretno, pri binarnom pretraživanju polja $q, a$ u koja smo bilježili operacije zamijenimo jednim velikim globalnim poljem, a informacija koju bilježimo tijekom binarnog pretraživanja postaje $L, R$, tj. koji se interval globalnog polja trenutno obrađuje. Trenutno razvrstavanje bilježimo u privremeno polje, a prije daljnje rekurzije podatke iz privremenog polja prepišemo natrag u izvorno polje.
    2.  Pražnjenje Fenwick treeja pri svakom pozivu dovelo bi do eksplozije vremenske složenosti; umjesto toga pri svakoj upotrebi Fenwick treeja bilježimo trenutne pozicije izmjena (to je već ostvareno privremenim poljem iz točke 1) i nakon završetka operacije na istim pozicijama dodamo $-1$, čime se brzo vraća na nulu.
    3.  Početna inicijalizacija niza može se pojednostavniti na operacije umetanja.

??? note "Primjer koda (ključni dio)"
    ```cpp
    struct Opt {
      int x, y, k, type, id;
      // za upit: type = 1, x, y su lijeva i desna granica intervala, k znači da se traži k-ti najmanji
      // za izmjenu: type = 0, x je pozicija izmjene, y je vrijednost nakon izmjene,
      // k označava je li trenutna operacija umetanje (1) ili brisanje (-1), koristi se pri ažuriranju Fenwick treeja.
      // id pamti izvornu oznaku svake operacije, jer se tijekom binarnog pretraživanja redoslijed operacija ispremiješa
    };
    
    Opt q[N], q1[N], q2[N];
    // q su sve operacije,
    // tijekom binarnog pretraživanja operacije razvrstane ulijevo spremaju se u q1, a razvrstane udesno u q2.
    int ans[N];
    void add(int p, int x);
    int query(int p);  // funkcije Fenwick treeja, značenje vidi u zadatku 3
    
    void solve(int l, int r, int L, int R)
    // trenutni raspon vrijednosti je [l,r], interval obrađivanih operacija je [L,R]
    {
      if (l > r || L > R) return;
      int cnt1 = 0, cnt2 = 0, m = (l + r) / 2;
      // cnt1, cnt2 su redom broj operacija razvrstanih ulijevo i udesno
      if (l == r) {
        for (int i = L; i <= R; i++)
          if (q[i].type == 1) ans[q[i].id] = l;
        return;
      }
      for (int i = L; i <= R; i++)
        if (q[i].type == 1) {  // upit: razvrstaj
          int t = query(q[i].y) - query(q[i].x - 1);
          if (q[i].k <= t)
            q1[++cnt1] = q[i];
          else
            q[i].k -= t, q2[++cnt2] = q[i];
        } else
          // izmjena: ažuriraj Fenwick tree i razvrstaj
          if (q[i].y <= m)
            add(q[i].x, q[i].k), q1[++cnt1] = q[i];
          else
            q2[++cnt2] = q[i];
      for (int i = 1; i <= cnt1; i++)
        if (q1[i].type == 0) add(q1[i].x, -q1[i].k);  // isprazni Fenwick tree
      for (int i = 1; i <= cnt1; i++) q[L + i - 1] = q1[i];
      for (int i = 1; i <= cnt2; i++)
        q[L + cnt1 + i - 1] = q2[i];  // elemente privremenih polja spoji natrag u izvorno polje
      solve(l, m, L, L + cnt1 - 1), solve(m + 1, r, L + cnt1, R);
      return;
    }
    ```

### Optimizacija za statične nizove

???+ note "Zadatak 5 ([【模板】可持久化线段树 2 (Predložak: perzistentni segment tree 2)](https://www.luogu.com.cn/problem/P3834))"
    Zadan je niz; upit za $k$-ti najmanji na intervalu.

??? note "Rješenje"
    I ugniježđena stabla (tree-in-tree) i paralelno binarno pretraživanje rješavaju problem $k$-tog najmanjeg na intervalu s izmjenama u složenosti $O(n \log^2 n)$, ali statični problem $k$-tog najmanjeg na intervalu može se perzistentnim segment treejem riješiti u vremenskoj složenosti $O(n \log n)$, dok gotovo sve implementacije statičnog $k$-tog najmanjeg na intervalu paralelnim binarnim pretraživanjem imaju vremensku složenost $O(n \log^2 n)$ i pri velikim ograničenjima postoji rizik od TLE-a. (Ovdje se podrazumijeva da je raspon vrijednosti istog reda kao duljina niza; slučaj kad raspon vrijednosti i duljina niza nisu istog reda može se diskretizacijom svesti na slučaj istog reda.)
    
    **Optimizacije**
    
    1.  U svakoj rundi podjele, ako u trenutnom nizu ima $t$ brojeva manjih ili jednakih $mid$, upit nakon podjele u desnom intervalu zapravo traži $k - t$-ti najmanji broj, pa se upiti razvrstani u desni interval mijenjaju. Ako je izvorni raspon vrijednosti odgovora $[L,R]$, a raspon vrijednosti odgovora u nekoj podjeli $[l,r]$, tada je za upite koji sudjeluju u toj podjeli utjecaj svih vrijednosti iz $[L,l)$ na njih već ranije uklonjen.
    2.  Budući da svaka runda podjele mora ovisiti samo o trenutnom rasponu vrijednosti odgovora $[l,r]$, Fenwick tree treba više puta puniti i prazniti.
    
    Što ako podjela ne ovisi samo o trenutnom rasponu vrijednosti odgovora?
    
    Odatle se dobiva optimizacija povezana s globalnim nizom: održavamo pokazivač $pos$ koji prati $mid$ (središte podjele) svake runde podjele, indekse svih elemenata $\leq pos$ u Fenwick treeju postavimo na $1$, a ostale pozicije Fenwick treeja na $0$. Prije svake podjele pomaknemo $pos$ i ažuriramo Fenwick tree. Broj pomaka pokazivača $pos$ istog je reda kao $n \log n$. Pri podjeli za svaki upit upitamo vrijednost odgovarajućeg intervala u Fenwick treeju; ako uvjet vrijedi, upit razvrstavamo u lijevi interval, inače u desni, i **upite nije potrebno mijenjati**.
    
    Budući da pratimo središte podjele, $pos$ mora točno ažurirati Fenwick tree. Prije paralelnog binarnog pretraživanja niz sortiramo po veličini elemenata i zabilježimo indekse elemenata, a pri pomicanju pokazivača u Fenwick treeju odgovarajuće mijenjamo te indekse. Na veliku većinu **zadataka rješivih paralelnim binarnim pretraživanjem koji nemaju izmjene** može se primijeniti ova optimizacija kako bi se znatno smanjio broj upotreba strukture podataka.
    
    Budući da se uklanja mnogo operacija punjenja i pražnjenja Fenwick treeja, ova optimizacija u pravilu primjetno povećava učinkovitost paralelnog binarnog pretraživanja (iako je samo optimizacija konstante), a za statični problem $k$-tog najmanjeg na intervalu učinkovitost nije ništa lošija od perzistentnog segment treeja bolje vremenske složenosti. Vrijedi spomenuti da za statični problem $k$-tog najmanjeg na intervalu postoji i implementacija paralelnog binarnog pretraživanja vremenske složenosti $O(n \log n)$.

??? note "Primjer koda (ključni dio)"
    ```cpp
    struct Query {
      int i, l, r, k;
    };  // i-ti upit traži k-ti najmanji na intervalu [l,r]
    
    Query s[200005], t1[200005], t2[200005];
    int n, m, cnt, pos, p[200005], ans[200005];
    pair<int, int> a[200005];
    
    void add(int x, int y);  // Fenwick tree: na poziciju x dodaj y
    int sum(int x);          // Fenwick tree: prefiksni zbroj [1,x]
    
    // trenutno obrađivani upiti su [l,r], raspon vrijednosti odgovora je [ql,qr]
    void overall_binary(int l, int r, int ql, int qr) {
      if (l > r) return;
      if (ql == qr) {
        for (int i = l; i <= r; i++) ans[s[i].i] = ql;
        return;
      }
      int cnt1 = 0, cnt2 = 0, mid = (ql + qr) >> 1;
      // prati središte podjele; smatramo da su vrijednosti [1,pos] već učitane u Fenwick tree
      while (pos <= n - 1 && a[pos + 1].first <= mid)
        add(a[pos + 1].second, 1), ++pos;
      while (pos >= 1 && a[pos].first > mid) add(a[pos].second, -1), --pos;
    
      for (int i = l; i <= r; i++) {
        int now = sum(s[i].r) - sum(s[i].l - 1);
        if (s[i].k <= now)
          t1[++cnt1] = s[i];
        else
          t2[++cnt2] = s[i];  // pazite: podatke upita ne treba mijenjati
      }
      for (int i = 1; i <= cnt1; i++) s[l + i - 1] = t1[i];
      for (int i = 1; i <= cnt2; i++) s[l + cnt1 + i - 1] = t2[i];
    
      overall_binary(l, l + cnt1 - 1, ql, mid);
      overall_binary(l + cnt1, r, mid + 1, qr);
    }
    
    int main() {
      scanf("%d%d", &n, &m);
      for (int i = 1; i <= n; i++) {
        scanf("%d", &a[i].first);
        a[i].second = i;
        p[++cnt] = a[i].first;
      }
      sort(a + 1, a + n + 1);  // sortiraj niz, diskretizacija
      sort(p + 1, p + n + 1);
      cnt = unique(p + 1, p + n + 1) - p - 1;
      for (int i = 1; i <= n; i++)
        a[i].first = lower_bound(p + 1, p + cnt + 1, a[i].first) - p;
      // učitavanje upita je izostavljeno
      overall_binary(1, m, 1, cnt);
      for (int i = 1; i <= n; i++) printf("%d\n", p[ans[i]]);
      return 0;
    }
    ```

### Prethodnik i sljedbenik na intervalu

???+ note "Zadatak 6"
    U nizu brojeva više puta pronađite prethodnika broja $k$ u intervalu (najveći broj strogo manji od $k$) ili sljedbenika (najmanji broj strogo veći od $k$); zajamčeno je da takav broj postoji.

??? note "Rješenje"
    Uzmimo prethodnika kao primjer: ovakvi se problemi strukturama podataka obično rješavaju tako da se najprije upita koliko u intervalu ima brojeva strogo manjih od $k$ (neka ih je $x$), a zatim se upita $x$-ti najmanji broj u intervalu. Za sljedbenika se upita koliko u intervalu ima brojeva ne većih od $k$ (neka ih je $x$), a zatim $x+1$-vi najmanji broj u intervalu.
    
    Razmotrimo rješenje paralelnim binarnim pretraživanjem: paralelno binarno pretraživanje učinkovit je offline algoritam za $k$-ti najmanji na intervalu, a [CDQ podjela](./cdq-divide.md) može offline učinkovito izračunati rang unutar intervala. Najprije jednom pokrenemo CDQ podjelu da izračunamo rangove, a zatim paralelnim binarnim pretraživanjem dobijemo prethodnika i sljedbenika unutar intervala.
    
    Ovaj se problem može riješiti i jednim offline prolazom CDQ podjele u kombinaciji sa segment treejem, ali je učinkovitost znatno manja od dvaju prolaza: CDQ podjela + paralelno binarno pretraživanje.

### Konstrukcija monotonog niza

???+ note "Zadatak 7 ([Sequence](https://www.luogu.com.cn/problem/P4597))"
    Zadan je niz; svakom operacijom neki broj možemo povećati za $+1$ ili smanjiti za $−1$. Niz treba učiniti neopadajućim, a u izmijenjenom nizu smiju se pojaviti samo brojevi koji su postojali prije izmjena; ispišite najmanji broj operacija.

??? note "Rješenje"
    Ovakvi se zadaci mogu riješiti i dinamičkim programiranjem ili greedyjem s poništavanjem (regret greedy).
    
    Uz uvjet minimalnog broja operacija sigurno postoji rješenje u kojem je svaki broj konačnog niza postojao u nizu prije izmjena; ta se tvrdnja može dokazati matematičkom indukcijom. Budući da zadatak ne traži podatke o konačnom nizu, problem se svodi na određivanje najmanjeg broja operacija.
    
    Budući da konačni niz mora biti neopadajući, možemo upotrijebiti paralelno binarno pretraživanje. U svakoj rundi paralelnog binarnog pretraživanja određujemo raspon vrijednosti intervala $[l,r]$ konačnog niza, pri čemu je raspon vrijednosti odgovora $[ql,qr]$. Neka je $mid=\lfloor\frac{ql + qr}{2}\rfloor$; na početku svake runde sve brojeve podrazumijevano razvrstamo u $[mid+1,qr]$ (broj onih koji idu u $[ql,mid]$ postavimo na $0$), a početnu cijenu postavimo na broj operacija potreban da se cijeli interval $[l,r]$ niza postavi na $mid+1$. Redom prolazimo kroz brojeve $i$ intervala $[l,r]$ i računamo ukupan broj operacija kojima se $[l,i]$ postavlja na $mid$, a $[i+1,r]$ na $mid+1$; ako je bolji od prethodnog broja operacija, ažuriramo najmanji broj operacija i broj elemenata koji idu u $[ql,mid]$.
    
    Pri podjeli već je osigurano da se monotonost konačnog niza ne narušava, a budući da svaki put uzimamo najmanji broj operacija, za brojeve koji su na kraju razvrstani u lijevi interval vrijednost $mid$ sigurno je bolja od $mid+1$, pa je niz dobiven paralelnim binarnim pretraživanjem sigurno neopadajući i s najmanjim brojem operacija. Preostaje izračunati broj operacija i ispisati ga.

??? note "Primjer koda (ključni dio)"
    ```cpp
    int a[500005], ans[500005];  // a: izvorni niz, ans: konstruirani niz
    
    void overall_binary(int l, int r, int ql, int qr) {
      if (l > r) return;
      if (ql == qr) {
        for (int i = l; i <= r; i++) ans[i] = ql;
        return;
      }
      int cnt = 0,
          mid = ql + ((qr - ql) >> 1);  // podrazumijevano na početku sve postavljamo na mid+1 i razvrstavamo u desni interval
      long long res = 0ll, sum = 0ll;
      for (int i = l; i <= r; i++) sum += abs(a[i] - (mid + 1));
      res = sum;
      for (int i = l; i <= r;
           i++) {  // pokušaj [l,i] s mid+1 promijeniti na mid i razvrstati u lijevi interval
        sum -= abs(a[i] - (mid + 1));
        sum += abs(a[i] - mid);
        if (sum < res) cnt = i - l + 1, res = sum;  // [l,i] s vrijednošću mid je bolje, ažuriraj
      }
      overall_binary(l, l + cnt - 1, ql, mid);
      overall_binary(l + cnt, r, mid + 1, qr);
    }
    ```

### Zadaci za vježbu

-   [„国家集训队” 矩阵乘法 (nacionalni pripremni tim: Množenje matrica)](https://www.luogu.com.cn/problem/P1527)
-   [„POI2011 R3 Day2” 流星 Meteors (Meteori)](https://loj.ac/p/2169)
-   [二逼平衡树 (balansirano stablo s dvije razine, tree-in-tree)](https://loj.ac/p/106)
-   [\[BalticOI 2004\] Sequence 数字序列 (Niz brojeva)](https://www.luogu.com.cn/problem/P4331)

## Literatura i napomene

-   Xu Haoran (许昊然). 浅谈数据结构题的几个非经典解法 (Kratko o nekoliko neklasičnih rješenja zadataka sa strukturama podataka). [2013 年信息学奥林匹克中国国家队侯选队员论文集 (Zbornik radova kandidata za kinesku nacionalnu ekipu za informatičku olimpijadu 2013.)](https://github.com/OI-wiki/libs/blob/master/%E9%9B%86%E8%AE%AD%E9%98%9F%E5%8E%86%E5%B9%B4%E8%AE%BA%E6%96%87/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2013%E8%AE%BA%E6%96%87%E9%9B%86.pdf).

[^ref1]: Xu Haoran (许昊然). 浅谈数据结构题的几个非经典解法 (Kratko o nekoliko neklasičnih rješenja zadataka sa strukturama podataka). [2013 年信息学奥林匹克中国国家队侯选队员论文集 (Zbornik radova kandidata za kinesku nacionalnu ekipu za informatičku olimpijadu 2013.)](https://github.com/OI-wiki/libs/blob/master/%E9%9B%86%E8%AE%AD%E9%98%9F%E5%8E%86%E5%B9%B4%E8%AE%BA%E6%96%87/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2013%E8%AE%BA%E6%96%87%E9%9B%86.pdf).
