---
title: Najkraći put
---

## Definicija

(Sjećate li se ovih definicija? Prije čitanja obvezno upoznajte osnovni dio stranice [Pojmovi teorije grafova](./concept.md).)

-   put
-   najkraći put
-   najkraći put u usmjerenom grafu, najkraći put u neusmjerenom grafu
-   najkraći put iz jednog izvora, najkraći putovi između svih parova vrhova

## Oznake

Radi lakšeg izlaganja, najprije dajemo značenje oznaka koje ćemo rabiti u nastavku.

-   $n$ je broj vrhova grafa, $m$ broj bridova grafa;
-   $s$ je izvor najkraćeg puta;
-   $D(u)$ je **stvarna** duljina najkraćeg puta od $s$ do $u$;
-   $dis(u)$ je **procijenjena** duljina najkraćeg puta od $s$ do $u$. U svakom trenutku vrijedi $dis(u) \geq D(u)$. Posebno, kad algoritam najkraćeg puta završi, treba vrijediti $dis(u)=D(u)$.
-   $w(u,v)$ je težina brida $(u,v)$.

## Svojstva

U grafu s pozitivnim težinama bridova najkraći put između bilo koja dva vrha ne prolazi istim vrhom dvaput.

U grafu s pozitivnim težinama bridova najkraći put između bilo koja dva vrha ne prolazi istim bridom dvaput.

U grafu s pozitivnim težinama bridova nijedan najkraći put između bilo koja dva vrha nema više od $n$ vrhova ni više od $n-1$ bridova.

## Floydov algoritam

Služi za nalaženje najkraćih putova između svih parova vrhova.

Složenost je prilično visoka, ali je konstanta mala i lako se implementira (samo tri `for` petlje).

Primjenjiv je na svaki graf, usmjeren ili neusmjeren, s pozitivnim ili negativnim težinama, ali najkraći put mora postojati. (Ne smije biti negativnog ciklusa.)

### Implementacija

Definiramo polje `f[k][x][y]`, duljinu najkraćeg puta od vrha $x$ do vrha $y$ ako je dopušteno prolaziti samo vrhovima $1$ do $k$ (tj. put u podgrafu $V'={1, 2, \ldots, k}$; pozor, $x$ i $y$ ne moraju biti u tom podgrafu).

Očito je `f[n][x][y]` duljina najkraćeg puta od vrha $x$ do vrha $y$ (jer je $V'={1, 2, \ldots, n}$ upravo $V$, pa je najkraći put koji predstavlja upravo traženi put).

Razmotrimo kako izračunati vrijednosti polja `f`.

`f[0][x][y]`: težina brida između $x$ i $y$, ili $0$, ili $+\infty$ (kad `f[0][x][y]` treba biti $+\infty$? Kad su $x$ i $y$ izravno povezani bridom, to je težina tog brida; kad je $x = y$, nula, jer je udaljenost do samog sebe nula; kad $x$ i $y$ nisu izravno povezani bridom, $+\infty$).

`f[k][x][y] = min(f[k-1][x][y], f[k-1][x][k]+f[k-1][k][y])` (`f[k-1][x][y]` je najkraći put koji ne prolazi vrhom $k$, a `f[k-1][x][k]+f[k-1][k][y]` najkraći put koji prolazi vrhom $k$).

Oba su gornja retka očito ispravna, pa ovaj pristup troši $O(N^3)$ memorije; redom povećavamo veličinu problema ($k$ od $1$ do $n$) i određujemo najkraći put između svaka dva vrha za trenutnu veličinu problema.

=== "C++"
    ```cpp
    for (k = 1; k <= n; k++) {
      for (x = 1; x <= n; x++) {
        for (y = 1; y <= n; y++) {
          f[k][x][y] = min(f[k - 1][x][y], f[k - 1][x][k] + f[k - 1][k][y]);
        }
      }
    }
    ```

=== "Python"
    ```python
    for k in range(1, n + 1):
        for x in range(1, n + 1):
            for y in range(1, n + 1):
                f[k][x][y] = min(f[k - 1][x][y], f[k - 1][x][k] + f[k - 1][k][y])
    ```

Budući da prva dimenzija ne utječe na rezultat, uočavamo da se prva dimenzija polja može izostaviti, pa možemo izravno pisati `f[x][y] = min(f[x][y], f[x][k]+f[k][y])`.

???+ note "Dokaz da prva dimenzija ne utječe na rezultat"
    Za zadani `k`, pri ažuriranju `f[k][x][y]` uključeni elementi uvijek dolaze iz `k`-tog retka i `k`-tog stupca polja `f[k-1]`. Nadalje uočavamo da se za zadani `k` pri ažuriranju `f[k][k][y]` ili `f[k][x][k]` vrijednost nikad ne mijenja, jer je prema formuli `f[k][k][y] = min(f[k-1][k][y], f[k-1][k][k]+f[k-1][k][y])` vrijednost `f[k-1][k][k]` jednaka 0, pa je ta vrijednost uvijek `f[k-1][k][y]`; dokaz za `f[k][x][k]` je analogan.
    
    Dakle, ako izostavimo prvu dimenziju, za zadani `k` nijedan element korišten pri ažuriranju nekog elementa nije ažuriran u ovoj iteraciji, pa izostavljanje prve dimenzije ne utječe na rezultat.

=== "C++"
    ```cpp
    for (k = 1; k <= n; k++) {
      for (x = 1; x <= n; x++) {
        for (y = 1; y <= n; y++) {
          f[x][y] = min(f[x][y], f[x][k] + f[k][y]);
        }
      }
    }
    ```

=== "Python"
    ```python
    for k in range(1, n + 1):
        for x in range(1, n + 1):
            for y in range(1, n + 1):
                f[x][y] = min(f[x][y], f[x][k] + f[k][y])
    ```

Ukupno je vremenska složenost $O(N^3)$, a prostorna $O(N^2)$.

### Primjene

???+ question "Zadan je neusmjereni graf s pozitivnim težinama; pronađite ciklus najmanjeg zbroja težina."
    Prvo, to je sigurno jednostavni ciklus.
    
    Razmislimo kako je taj ciklus sastavljen.
    
    Promotrimo vrh $u$ s najvećim indeksom na ciklusu.
    
    `f[u-1][x][y]` te $(u,x)$, $(u,y)$ zajedno čine ciklus.
    
    Tijekom Floydova algoritma prolazimo po $u$ i računamo minimum tog zbroja.
    
    Vremenska složenost je $O(n^3)$.
    
    Više u odjeljku [Najmanji ciklus](./min-cycle.md).

???+ question "Za usmjereni graf znamo postoji li brid između svaka dva vrha; treba odrediti jesu li svaka dva vrha povezana."
    Taj je problem nalaženje **tranzitivnog zatvorenja grafa**.
    
    Dovoljno je slijediti Floydov postupak i dodavati vrhove jedan po jedan.
    
    Samo što su težine bridova sada $1/0$, a $\min$ postaje operacija **ili**.
    
    Daljnjom optimizacijom bitsetom složenost može biti $O(\frac{n^3}{w})$.
    
    ```cpp
    // std::bitset<SIZE> f[SIZE];
    for (k = 1; k <= n; k++)
      for (i = 1; i <= n; i++)
        if (f[i][k]) f[i] = f[i] | f[k];
    ```

## Bellman–Fordov algoritam

Bellman–Fordov algoritam algoritam je najkraćeg puta zasnovan na operaciji relaksacije (relax); može naći najkraći put u grafu s negativnim težinama i prepoznati slučaj kad najkraći put ne postoji.

„SPFA”, za koji ste možda čuli u kineskoj OI zajednici, jedna je implementacija Bellman–Fordova algoritma.

### Postupak

Najprije predstavljamo operaciju relaksacije koju Bellman–Fordov algoritam koristi (koristi je i Dijkstrin algoritam).

Za brid $(u,v)$ relaksacija odgovara formuli: $dis(v) = \min(dis(v), dis(u) + w(u, v))$.

Značenje je očito: pokušavamo putem $S \to u \to v$ (gdje je za $S \to u$ uzet najkraći put) ažurirati duljinu najkraćeg puta do vrha $v$; ako je taj put bolji, ažuriramo.

Bellman–Fordov algoritam neprestano pokušava relaksirati svaki brid grafa. U svakom krugu petlje pokušamo relaksirati sve bridove grafa; kad u jednom krugu nema uspješne relaksacije, algoritam staje.

Svaki krug je $O(m)$; koliko najviše krugova može biti?

Ako najkraći put postoji, jedna relaksacija povećava broj bridova najkraćeg puta barem za $1$, a najkraći put ima najviše $n-1$ bridova, pa cijeli algoritam izvodi najviše $n-1$ krugova relaksacije. Ukupna vremenska složenost je $O(nm)$.

Postoji još jedan slučaj: ako iz $S$ dosegnemo negativni ciklus, relaksacije se nastavljaju beskonačno. Uočimo da smo već pokazali da se, ako najkraći put postoji, relaksacija izvodi najviše $n-1$ krugova; dakle ako u $n$-tom krugu još postoji brid koji se može relaksirati, iz $S$ se može doseći negativni ciklus.

???+ warning "Česta zabluda pri provjeri negativnog ciklusa"
    Treba paziti: ako Bellman–Fordov algoritam pokrenut s izvorom $S$ ne javi postojanje negativnog ciklusa, to znači samo da se iz $S$ ne može doseći negativni ciklus, a ne da u grafu nema negativnog ciklusa.
    
    Stoga, ako treba provjeriti ima li u cijelom grafu negativni ciklus, najstroži je način napraviti superizvor, iz njega povući brid težine 0 u svaki vrh grafa i pokrenuti Bellman–Fordov algoritam sa superizvorom kao početkom.

### Implementacija

??? note "Referentna implementacija"
    === "C++"
        ```cpp
        struct Edge {
          int u, v, w;
        };
        
        vector<Edge> edge;
        
        int dis[MAXN], u, v, w;
        constexpr int INF = 0x3f3f3f3f;
        
        bool bellmanford(int n, int s) {
          memset(dis, 0x3f, (n + 1) * sizeof(int));
          dis[s] = 0;
          bool flag = false;  // je li u ovom krugu petlje došlo do relaksacije
          for (int i = 1; i <= n; i++) {
            flag = false;
            for (int j = 0; j < edge.size(); j++) {
              u = edge[j].u, v = edge[j].v, w = edge[j].w;
              if (dis[u] == INF) continue;
              // beskonačno plus/minus konstanta i dalje je beskonačno
              // pa bridovi iz vrha s duljinom najkraćeg puta INF ne mogu relaksirati
              if (dis[v] > dis[u] + w) {
                dis[v] = dis[u] + w;
                flag = true;
              }
            }
            // kad nema brida koji se može relaksirati, zaustavi algoritam
            if (!flag) {
              break;
            }
          }
          // ako se u n-tom krugu još može relaksirati, iz s se može doseći negativni ciklus
          return flag;
        }
        ```
    
    === "Python"
        ```python
        class Edge:
            def __init__(self, u=0, v=0, w=0):
                self.u = u
                self.v = v
                self.w = w
        
        
        INF = 0x3F3F3F3F
        edge = []
        
        
        def bellmanford(n, s):
            dis = [INF] * (n + 1)
            dis[s] = 0
            for i in range(1, n + 1):
                flag = False
                for e in edge:
                    u, v, w = e.u, e.v, e.w
                    if dis[u] == INF:
                        continue
                    # beskonačno plus/minus konstanta i dalje je beskonačno
                    # pa bridovi iz vrha s duljinom najkraćeg puta INF ne mogu relaksirati
                    if dis[v] > dis[u] + w:
                        dis[v] = dis[u] + w
                        flag = True
                # kad nema brida koji se može relaksirati, zaustavi algoritam
                if not flag:
                    break
            # ako se u n-tom krugu još može relaksirati, iz s se može doseći negativni ciklus
            return flag
        ```

### Optimizacija redom: SPFA

Tj. Shortest Path Faster Algorithm.

Često nam ne treba toliko beskorisnih relaksacija.

Očito samo bridovi iz vrhova relaksiranih u prethodnom koraku mogu izazvati sljedeću relaksaciju.

Ako redom održavamo „koji vrhovi mogu izazvati relaksaciju”, obilazimo samo potrebne bridove.

SPFA može poslužiti i za provjeru može li se iz $s$ doseći negativni ciklus: dovoljno je pamtiti koliko bridova najkraći put prolazi; kad prođe barem $n$ bridova, iz $s$ se može doseći negativni ciklus.

??? note "Implementacija"
    === "C++"
        ```cpp
        struct edge {
          int v, w;
        };
        
        vector<edge> e[MAXN];
        int dis[MAXN], cnt[MAXN], vis[MAXN];
        queue<int> q;
        
        bool spfa(int n, int s) {
          memset(dis, 0x3f, (n + 1) * sizeof(int));
          dis[s] = 0, vis[s] = 1;
          q.push(s);
          while (!q.empty()) {
            int u = q.front();
            q.pop(), vis[u] = 0;
            for (auto ed : e[u]) {
              int v = ed.v, w = ed.w;
              if (dis[v] > dis[u] + w) {
                dis[v] = dis[u] + w;
                cnt[v] = cnt[u] + 1;  // broj bridova na najkraćem putu
                if (cnt[v] >= n) return false;
                // bez negativnog ciklusa najkraći put ima najviše n - 1 bridova
                // pa ako ima više od n bridova, sigurno prolazi negativnim ciklusom
                if (!vis[v]) q.push(v), vis[v] = 1;
              }
            }
          }
          return true;
        }
        ```
    
    === "Python"
        ```python
        from collections import deque
        
        
        class Edge:
            def __init__(self, v=0, w=0):
                self.v = v
                self.w = w
        
        
        e = [[Edge() for i in range(MAXN)] for j in range(MAXN)]
        INF = 0x3F3F3F3F
        
        
        def spfa(n, s):
            dis = [INF] * (n + 1)
            cnt = [0] * (n + 1)
            vis = [False] * (n + 1)
            q = deque()
        
            dis[s] = 0
            vis[s] = True
            q.append(s)
            while q:
                u = q.popleft()
                vis[u] = False
                for ed in e[u]:
                    v, w = ed.v, ed.w
                    if dis[v] > dis[u] + w:
                        dis[v] = dis[u] + w
                        cnt[v] = cnt[u] + 1  # broj bridova na najkraćem putu
                        if cnt[v] >= n:
                            return False
                        # bez negativnog ciklusa najkraći put ima najviše n - 1 bridova
                        # pa ako ima više od n bridova, sigurno prolazi negativnim ciklusom
                        if not vis[v]:
                            q.append(v)
                            vis[v] = True
        ```

Iako je SPFA u većini slučajeva vrlo brz, njegova je najgora vremenska složenost $O(nm)$ i nije teško sastaviti test koji ga dovede do te složenosti, pa ga na natjecanjima treba koristiti oprezno (bez negativnih bridova najbolje je koristiti Dijkstrin algoritam; s negativnim bridovima i bez posebnih svojstava grafa, ako je SPFA dio službenog rješenja, zadatak ne bi smio imati ograničenja koja Bellman–Fordov algoritam ne može proći).

???+ note "Ostale optimizacije Bellman–Forda"
    Osim optimizacije redom (SPFA), Bellman–Ford ima i druge oblike optimizacije; na nekim grafovima daju izražen učinak, ali na određenim posebnim grafovima najgora složenost može biti eksponencijalna.
    
    -   Optimizacija heapom: red zamijenimo heapom; razlika u odnosu na Dijkstru jest da vrh može ući u red više puta. Na grafu s negativnim bridovima može se natjerati na eksponencijalnu složenost.
    -   Optimizacija stogom: red zamijenimo stogom (tj. izvorni BFS postaje DFS); pri traženju negativnog ciklusa može biti učinkovitija, ali najgora vremenska složenost i dalje je eksponencijalna.
    -   LLL optimizacija: obični red zamijenimo dvostranim redom; pri svakom ulasku udaljenost vrha usporedimo s prosjekom udaljenosti u redu: ako je veća, ubacimo ga na kraj, inače na početak.
    -   SLF optimizacija: obični red zamijenimo dvostranim redom; pri svakom ulasku udaljenost vrha usporedimo s početkom reda: ako je veća, ubacimo ga na kraj, inače na početak.
    -   D´Esopo–Pape algoritam: obični red zamijenimo dvostranim redom; ako vrh prije nije bio u redu, ubacimo ga na kraj, inače na početak.
    
    Više optimizacija i načina kako ih „hackati” možete pročitati u [odgovoru fstqwq-a na Zhihuu](https://www.zhihu.com/question/292283275/answer/484871888).

## Dijkstrin algoritam

Dijkstrin (/ˈdikstrɑ/ ili /ˈdɛikstrɑ/) algoritam otkrio je nizozemski računalni znanstvenik E. W. Dijkstra 1956., a objavio ga 1959. To je algoritam za najkraći put iz jednog izvora u **grafu s nenegativnim težinama**.

### Postupak

Vrhove podijelimo u dva skupa: vrhove s određenom duljinom najkraćeg puta (skup $S$) i vrhove s još neodređenom duljinom najkraćeg puta (skup $T$). Na početku svi vrhovi pripadaju skupu $T$.

Inicijaliziramo $dis(s)=0$, a $dis$ svih ostalih vrhova na $+\infty$.

Zatim ponavljamo sljedeće:

1.  Iz skupa $T$ odaberemo vrh s najmanjom duljinom najkraćeg puta i premjestimo ga u skup $S$.
2.  Nad svim izlaznim bridovima vrha koji je upravo dodan u $S$ izvedemo relaksaciju.

Algoritam završava kad skup $T$ postane prazan.

### Vremenska složenost

Naivna implementacija nakon svake operacije 2 izravno brute-force traži vrh s najmanjom duljinom najkraćeg puta u skupu $T$. Ukupna složenost operacije 2 je $O(m)$, operacije 1 $O(n^2)$, a cijelog postupka $O(n^2 + m) = O(n^2)$.

Postupak možemo optimizirati heapom: pri svakoj uspješnoj relaksaciji brida $(u,v)$ ubacimo $v$ u heap (ako je $v$ već u heapu, izravno izvedemo Decrease-key), a u operaciji 1 uzimamo vrh s vrha heapa. Ukupno je $O(m)$ Decrease-key operacija i $O(n)$ pop operacija; različitim heapovima dobivamo različite složenosti, vidi stranicu [Heap](../ds/heap.md). Najbolja složenost koju heap optimizacija postiže jest $O(n\log n+m)$, a postižu je npr. Fibonaccijevi heapovi.

Posebno, možemo koristiti prioritetni red; tada se Decrease-key ne može izvesti, ali možemo pri svakoj relaksaciji ponovno ubaciti vrh, a pri vađenju provjeriti je li već relaksiran i, ako jest, preskočiti ga; složenost je $O(m\log n)$, a prednost je jednostavnija implementacija.

Heap se ovdje može implementirati i segment tree-om, složenosti $O(m\log n)$; u nekim posebnim nerekurzivnim implementacijama segment tree-a konstanta je manja nego kod heapa. Osim toga, segment tree podržava više operacija, pa se neki posebni problemi na grafovima mogu održavati samo segment tree-om.

U rijetkim grafovima, $m = O(n)$, Dijkstrin algoritam s heapom ima znatnu prednost u učinkovitosti; u gustim grafovima, $m = O(n^2)$, bolja je naivna implementacija.

### Dokaz ispravnosti

Matematičkom indukcijom dokazujemo ispravnost Dijkstrina algoritma uz pretpostavku da su **sve težine bridova nenegativne**[^1].

Jednostavno rečeno, treba dokazati da je pri izvođenju operacije 1 najkraći put izvađenog vrha $u$ već određen, tj. da vrijedi $D(u) = dis(u)$.

Na početku je $S = \varnothing$ i tvrdnja vrijedi.

Nastavljamo kontradikcijom.

Neka je $u$ prvi vrh u algoritmu za koji pri dodavanju u $S$ ne vrijedi $D(u) = dis(u)$. Budući da za $s$ sigurno vrijedi $D(u)=dis(u)=0$ i da je $s$ sigurno prvi vrh dodan u $S$, prije dodavanja $u$ u $S$ vrijedi $S \neq \varnothing$; ako ne postoji put od $s$ do $u$, onda je $D(u) = dis(u) = +\infty$, što proturječi pretpostavci.

Dakle sigurno postoji put $s \to x \to y \to u$, gdje je $y$ prvi vrh na putu $s \to u$ koji pripada skupu $T$, a $x$ prethodnik vrha $y$ (očito $x \in S$). Napomenimo da je moguće $s = x$ ili $y = u$, tj. $s \to x$ ili $y \to u$ može biti prazan put.

Budući da svi vrhovi dodani prije $u$ zadovoljavaju $D(u) = dis(u)$, pri dodavanju $x$ u $S$ vrijedi $D(x) = dis(x)$ i tada se brid $(x,y)$ relaksira, pa možemo dokazati da pri dodavanju $u$ u $S$ sigurno vrijedi $D(y)=dis(y)$.

Dokažimo da vrijedi $D(u) = dis(u)$. Na putu $s \to x \to y \to u$ sve su težine bridova nenegativne, pa je $D(y) \leq D(u)$. Stoga $dis(y) = D(y) \leq D(u)\leq dis(u)$. No kad je vrh $u$ u operaciji 1 izvađen iz skupa $T$, vrh $y$ još nije bio izvađen iz $T$, pa tada vrijedi $dis(u)\leq dis(y)$; dobivamo $dis(y) = D(y) = D(u) = dis(u)$, što proturječi pretpostavci $D(u)\neq dis(u)$, pa pretpostavka ne vrijedi.

Time smo dokazali da je najkraći put svakog vrha izvađenog u operaciji 1 već određen. Tvrdnja je dokazana.

Uočimo da je ključna nejednakost $D(y) \leq D(u)$ u dokazu izvedena uz pretpostavku da su sve težine bridova nenegativne. Kad u grafu postoje negativni bridovi, ta nejednakost više ne vrijedi, ispravnost Dijkstrina algoritma nije zajamčena i algoritam može dati pogrešan rezultat.

### Implementacija

Dajemo i brute-force implementaciju složenosti $O(n^2)$ i implementaciju s prioritetnim redom složenosti $O(m \log m)$.

???+ note "Naivna implementacija"
    === "C++"
        ```cpp
        struct edge {
          int v, w;
        };
        
        vector<edge> e[MAXN];
        int dis[MAXN], vis[MAXN];
        
        void dijkstra(int n, int s) {
          memset(dis, 0x3f, (n + 1) * sizeof(int));
          dis[s] = 0;
          for (int i = 1; i <= n; i++) {
            int u = 0, mind = 0x3f3f3f3f;
            for (int j = 1; j <= n; j++)
              if (!vis[j] && dis[j] < mind) u = j, mind = dis[j];
            vis[u] = true;
            for (auto ed : e[u]) {
              int v = ed.v, w = ed.w;
              if (dis[v] > dis[u] + w) dis[v] = dis[u] + w;
            }
          }
        }
        ```
    
    === "Python"
        ```python
        class Edge:
            def __init__(self, v=0, w=0):
                self.v = v
                self.w = w
        
        
        e = [[Edge() for i in range(MAXN)] for j in range(MAXN)]
        INF = 0x3F3F3F3F
        
        
        def dijkstra(n, s):
            dis = [INF] * (n + 1)
            vis = [0] * (n + 1)
        
            dis[s] = 0
            for i in range(1, n + 1):
                u = 0
                mind = INF
                for j in range(1, n + 1):
                    if not vis[j] and dis[j] < mind:
                        u = j
                        mind = dis[j]
                vis[u] = True
                for ed in e[u]:
                    v, w = ed.v, ed.w
                    if dis[v] > dis[u] + w:
                        dis[v] = dis[u] + w
        ```

???+ note "Implementacija s prioritetnim redom"
    === "C++"
        ```cpp
        struct edge {
          int v, w;
        };
        
        struct node {
          int dis, u;
        
          bool operator>(const node& a) const { return dis > a.dis; }
        };
        
        vector<edge> e[MAXN];
        int dis[MAXN], vis[MAXN];
        priority_queue<node, vector<node>, greater<node>> q;
        
        void dijkstra(int n, int s) {
          memset(dis, 0x3f, (n + 1) * sizeof(int));
          memset(vis, 0, (n + 1) * sizeof(int));
          dis[s] = 0;
          q.push({0, s});
          while (!q.empty()) {
            int u = q.top().u;
            q.pop();
            if (vis[u]) continue;
            vis[u] = 1;
            for (auto ed : e[u]) {
              int v = ed.v, w = ed.w;
              if (dis[v] > dis[u] + w) {
                dis[v] = dis[u] + w;
                q.push({dis[v], v});
              }
            }
          }
        }
        ```
    
    === "Python"
        ```python
        def dijkstra(e, s):
            """
            Ulaz:
            e: lista susjedstva
            s: početni vrh
            Vraća:
            dis: duljine najkraćih putova od s do svakog vrha
            """
            dis = defaultdict(lambda: float("inf"))
            dis[s] = 0
            q = [(0, s)]
            vis = set()
            while q:
                _, u = heapq.heappop(q)
                if u in vis:
                    continue
                vis.add(u)
                for v, w in e[u]:
                    if dis[v] > dis[u] + w:
                        dis[v] = dis[u] + w
                        heapq.heappush(q, (dis[v], v))
            return dis
        ```

## Johnsonov algoritam za najkraće putove između svih parova vrhova

Johnsonov algoritam, kao i Floydov, nalazi najkraće putove između svih parova vrhova u grafu bez negativnih ciklusa. Algoritam je 1977. predložio Donald B. Johnson.

Najkraće putove između svih parova vrhova možemo naći tako da prođemo po svim izvorima i pokrenemo $n$ puta Bellman–Fordov algoritam, složenosti $O(n^2m)$, ili izravno Floydovim algoritmom, složenosti $O(n^3)$.

Uočimo da Dijkstrin algoritam s heapom ima bolju vremensku složenost za najkraći put iz jednog izvora od Bellman–Forda; ako prođemo po svim izvorima i pokrenemo Dijkstrin algoritam $n$ puta, problem rješavamo u vremenu $O(nm\log m)$ (ovisno o implementaciji Dijkstrina algoritma), što je bolje od $n$ pokretanja Bellman–Forda, a na rijetkim grafovima bolje i od Floydova algoritma.

No Dijkstrin algoritam ne može ispravno naći najkraći put s negativnim bridovima, pa bridove izvornog grafa moramo predobraditi tako da sve težine budu nenegativne.

Ideja koja se lako nameće jest svim bridovima dodati isti pozitivan broj $x$, čime sve težine postaju nenegativne. Ako najkraći put od početka do kraja u novom grafu prolazi $k$ bridova, oduzimanjem $kx$ od najkraćeg puta dobivamo stvarni najkraći put.

No takav je postupak pogrešan. Promotrimo sljedeći graf:

![](./images/shortest-path1.svg)

Najkraći put $1 \to 2$ je $1 \to 5 \to 3 \to 2$, duljine $−2$.

A što ako svakom bridu dodamo $5$?

![](./images/shortest-path2.svg)

Najkraći put $1 \to 2$ u novom grafu je $1 \to 4 \to 2$, što više nije stvarni najkraći put.

Johnsonov algoritam težine bridova ponovno označava drugim načinom.

Dodamo virtualni vrh (ovdje mu dajemo indeks $0$). Iz njega povučemo brid težine $0$ u sve ostale vrhove.

Zatim Bellman–Fordovim algoritmom nađemo najkraće putove od vrha $0$ do svih ostalih vrhova; označimo ih $h_i$.

Ako postoji brid od $u$ do $v$ težine $w$, njegovu težinu ponovno postavimo na $w+h_u-h_v$.

Zatim iz svakog vrha kao izvora pokrenemo $n$ krugova Dijkstrina algoritma i dobivamo najkraće putove između svih parova vrhova.

Početni Bellman–Fordov algoritam nije vremensko usko grlo; ako Dijkstrin algoritam implementiramo s `priority_queue`, vremenska složenost algoritma je $O(nm\log m)$.

### Dokaz ispravnosti

Zašto je takvo ponovno označavanje težina ispravno?

Prije rasprave o tome razmotrimo jedan pojam iz fizike — potencijalnu energiju.

Potencijalne energije poput gravitacijske ili električne imaju svojstvo da promjena potencijalne energije ovisi samo o relativnom položaju početne i krajnje točke, a ne o putu od početne do krajnje točke.

Potencijalna energija ima još jedno svojstvo: njezina apsolutna vrijednost ovisi o odabranoj nultoj točki, ali bez obzira na to gdje je nulta točka, razlika potencijalnih energija dviju točaka je stalna.

Vratimo se na temu.

U ponovno označenom grafu duljina puta $s \to p_1 \to p_2 \to \dots \to p_k \to t$ od $s$ do $t$ glasi:

$(w(s,p_1)+h_s-h_{p_1})+(w(p_1,p_2)+h_{p_1}-h_{p_2})+ \dots +(w(p_k,t)+h_{p_k}-h_t)$

Pojednostavnjeno:

$w(s,p_1)+w(p_1,p_2)+ \dots +w(p_k,t)+h_s-h_t$

Kojim god putem išli od $s$ do $t$, vrijednost $h_s-h_t$ se ne mijenja, što se točno slaže sa svojstvom potencijalne energije!

Radi jednostavnosti, $h_i$ ćemo zvati potencijalom vrha $i$.

Izraz za duljinu najkraćeg puta $s \to t$ u novom grafu sastoji se od dva dijela: prvi, zbroj težina bridova, najkraći je put $s \to t$ u izvornom grafu, a drugi je razlika potencijala dvaju vrhova. Budući da je razlika potencijala stalna, najkraći put $s \to t$ u izvornom grafu odgovara najkraćem putu $s \to t$ u novom grafu.

Time je dokaz ispravnosti napola gotov — dokazali smo da je najkraći put u grafu s ponovno označenim težinama i dalje izvorni najkraći put. Preostaje dokazati da su sve težine bridova u novom grafu nenegativne, jer u grafu s nenegativnim težinama Dijkstrin algoritam jamči ispravan rezultat.

Po nejednakosti trokuta, za svaki brid $(u,v)$ grafa vrijedi $h_v \leq h_u + w(u,v)$. Ponovno označena težina tog brida je $w'(u,v)=w(u,v)+h_u-h_v \geq 0$. Time smo dokazali da su težine bridova novog grafa nenegativne.

Tako smo dokazali ispravnost Johnsonova algoritma.

## Usporedba metoda

| Algoritam najkraćeg puta | Floyd | Bellman–Ford | Dijkstra | Johnson |
| ------- | ---------- | ------------ | ------------ | ------------- |
| Vrsta najkraćeg puta | svi parovi vrhova | iz jednog izvora | iz jednog izvora | svi parovi vrhova |
| Primjenjiv na | svaki graf | svaki graf | graf s nenegativnim težinama | svaki graf |
| Otkriva negativni ciklus? | da | da | ne | da |
| Vremenska složenost | $O(N^3)$ | $O(NM)$ | $O(M\log M)$ | $O(NM\log M)$ |

Napomena: složenost Dijkstrina algoritma u tablici odnosi se na implementaciju s `priority_queue`.

## Ispis rješenja

Napravimo polje `pre` i pri ažuriranju udaljenosti zabilježimo odakle je sljedeći vrh dosegnut; prije kraja algoritma rekurzivno ispišemo put.

Primjerice, Floyd bilježi `pre[i][j] = k;`, a Bellman–Ford i Dijkstra obično bilježe `pre[v] = u`.

## Neki posebni slučajevi

-   Najkraći put u grafu s težinama samo $0$ i $1$: [0-1 BFS](./bfs.md#bfs-s-dvostranim-redom);
-   Najkraći put kad je dopušteno najviše $k$ puta promijeniti cijenu puta i slično: [Najkraći put u slojevitom grafu](./node.md#najkraći-put-u-slojevitom-grafu).

## Literatura i napomene

[^1]: Introduction to Algorithms (3. izdanje, kineski prijevod), China Machine Press, 2013., str. 384–385.
