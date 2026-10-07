---
title: Minimalno razapinjuće stablo
---

## Definicija

Prije čitanja obvezno pročitajte [Osnovne pojmove teorije grafova](./concept.md) i [Osnove stabala](./tree-basic.md) te se upoznajte sa sljedećim definicijama:

1.  razapinjući podgraf
2.  razapinjuće stablo

**Minimalno razapinjuće stablo** (Minimum Spanning Tree, MST) neusmjerenog povezanog grafa definiramo kao razapinjuće stablo s najmanjim zbrojem težina bridova.

Napomena: razapinjuće stablo postoji samo za povezane grafove; nepovezani graf ima samo razapinjuću šumu.

## Kruskalov algoritam

Kruskalov algoritam uobičajen je i jednostavan algoritam za minimalno razapinjuće stablo koji je izumio Kruskal. Osnovna je ideja dodavati bridove od najmanjeg prema najvećem; to je greedy algoritam.

### Predznanje

[DSU](../ds/dsu.md), [greedy](../basic/greedy.md), [spremanje grafa](./save.md).

### Implementacija

Ilustracija:

![](./images/mst-2.apng)

Pseudokod:

<!--
```pseudo
\begin{algorithm}
\caption{Kruskal}
\begin{algorithmic}
\INPUT{ The edges of the graph $e$ where each element in $e$ is $(u, v, w)$ denoting that there is an edge between $u$ and $v$ weighted $w$. }
\OUTPUT The edges of the MST of the input graph
\STATE $result \gets \varnothing$
\STATE sort $e$ into nondecreasing order by weight $w$
\FOR{each $(u, v, w)$ in the sorted $e$}
    \IF{$u$ \AND $v$ are not connected in the union-find set}
        \STATE connect $u$ \AND $v$ in the union-find set
        \STATE $result \gets result \bigcup (u, v, w)$
    \ENDIF
\ENDFOR
\RETURN $result$
\end{algorithmic}
\end{algorithm}
```
-->

$$
\begin{array}{ll}
1 &  \textbf{Input. } \text{The edges of the graph } e , \text{ where each element in } e \text{ is } (u, v, w) \\
  &  \text{ denoting that there is an edge between } u \text{ and } v \text{ weighted } w . \\
2 &  \textbf{Output. } \text{The edges of the MST of the input graph}.\\
3 &  \textbf{Method. } \\ 
4 &  result \gets \varnothing \\
5 &  \text{sort } e \text{ into nondecreasing order by weight } w \\ 
6 &  \textbf{for} \text{ each } (u, v, w) \text{ in the sorted } e \\ 
7 &  \qquad \textbf{if } u \text{ and } v \text{ are not connected in the union-find set } \\
8 &  \qquad\qquad \text{connect } u \text{ and } v \text{ in the union-find set} \\
9 &  \qquad\qquad  result \gets result\;\bigcup\ \{(u, v, w)\} \\
10 &  \textbf{return }  result
\end{array}
$$

Algoritam je jednostavan, ali treba odgovarajuću strukturu podataka koja ga podržava… Konkretno, održavamo šumu, pitamo jesu li dva vrha u istom stablu i spajamo dva stabla.

Apstraktnije rečeno, održavamo hrpu **skupova**, pitamo pripadaju li dva elementa istom skupu i spajamo dva skupa.

Provjeru povezanosti dvaju vrhova i njihovo spajanje možemo održavati DSU-om.

Ako upotrijebimo sortiranje u $O(m\log m)$ i DSU u $O(m\alpha(m, n))$ ili $O(m\log n)$, dobivamo Kruskalov algoritam vremenske složenosti $O(m\log m)$.

### Dokaz

Ideja je jednostavna: da bismo izgradili minimalno razapinjuće stablo, krećemo od brida najmanje težine i dodajemo bridove redom po rastućoj težini; ako bi dodavanje brida stvorilo ciklus, taj brid odbacimo, sve dok ne dodamo $n-1$ bridova, tj. dok ne nastane stablo.

Dokaz: indukcijom dokazujemo da je skup bridova koje K algoritam odabere u svakom trenutku sadržan u nekom MST-u.

Baza: na samom početku algoritma tvrdnja očito vrijedi (minimalno razapinjuće stablo postoji).

Korak: pretpostavimo da tvrdnja vrijedi u nekom trenutku, da je trenutačni skup bridova $F$ i da je $T$ taj MST; promotrimo sljedeći dodani brid $e$.

Ako $e$ pripada $T$, tvrdnja vrijedi.

Inače, u $T+e$ sigurno postoji ciklus; promotrimo na tom ciklusu drugi brid $f$ koji ne pripada $F$ (postoji barem jedan).

Prvo, težina od $f$ sigurno nije manja od težine od $e$, inače bi $f$ bio odabran prije $e$.

Zatim, težina od $f$ sigurno nije veća od težine od $e$, inače bi $T+e-f$ bilo razapinjuće stablo bolje od $T$.

Dakle, $T+e-f$ sadrži $F$ i također je minimalno razapinjuće stablo, pa indukcija vrijedi.

### Primjer

???+ note "[Luogu P1195 Nebo u džepu](https://www.luogu.com.cn/problem/P1195)"
    Zadano je $n$ oblaka koje treba povezati u $k$ komada šećerne vune; povezivanje oblaka $X_i$ i $Y_i$ košta $L_i$. Nađi najmanji trošak.

??? note "Kôd primjera"
    === "C++"
        ```cpp
        --8<-- "docs/graph/code/mst/mst_3.cpp"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/graph/code/mst/mst_3.py"
        ```
    
    === "Java"
        ```java
        --8<-- "docs/graph/code/mst/mst_3.java"
        ```

## Primov algoritam

Primov algoritam drugi je uobičajen i jednostavan algoritam za minimalno razapinjuće stablo. Osnovna je ideja krenuti od jednog vrha i stalno dodavati vrhove (umjesto bridova kao u Kruskalovu algoritmu).

### Implementacija

Ilustracija:

![](./images/mst-3.apng)

Konkretno, u svakom koraku biramo vrh najmanje udaljenosti i novim bridovima ažuriramo udaljenosti ostalih vrhova.

Zapravo, kao i u Dijkstrinu algoritmu, svaki put tražimo vrh najmanje udaljenosti; to se može raditi grubom silom ili održavati hrpom.

Optimizacija hrpom slična je optimizaciji hrpom u Dijkstri, ali ako se koristi binarna hrpa ili druga hrpa koja ne podržava decrease-key u $O(1)$, složenost nije bolja od Kruskalove, a konstanta je veća od Kruskalove. Zato se u pravilu koristi Kruskalov algoritam; na gustim grafovima, posebno potpunim, složenost grubog Prima bolja je od Kruskalove, ali u praksi **ne mora** biti brža.

Gruba sila: $O(n^2+m)$.

Binarna hrpa: $O((n+m) \log n)$.

Fibonaccijeva hrpa: $O(n \log n + m)$.

Pseudokod:

$$
\begin{array}{ll}
1 &  \textbf{Input. } \text{The nodes of the graph }V\text{ ; the function }g(u, v)\text{ which}\\
  &  \text{means the weight of the edge }(u, v)\text{; the function }adj(v)\text{ which}\\
  &  \text{means the nodes adjacent to }v.\\
2 &  \textbf{Output. } \text{The sum of weights of the MST of the input graph.} \\
3 &  \textbf{Method.} \\
4 &  result \gets 0 \\
5 & \text{choose an arbitrary node in }V\text{ to be the }root \\
6 &  dis(root)\gets 0 \\
7 &  \textbf{for } \text{each node }v\in(V-\{root\}) \\
8 &  \qquad  dis(v)\gets\infty \\
9 &  rest\gets V \\
10 &  \textbf{while }  rest\ne\varnothing \\
11 &  \qquad cur\gets \text{the node with the minimum }dis\text{ in }rest \\
12 &  \qquad  result\gets result+dis(cur) \\
13 &  \qquad  rest\gets rest-\{cur\} \\
14 &  \qquad  \textbf{for}\text{ each node }v\in adj(cur) \\
15 &  \qquad\qquad  dis(v)\gets\min(dis(v), g(cur, v)) \\
16 &  \textbf{return }  result 
\end{array}
$$

Napomena: gornji kôd računa samo težinu minimalnog razapinjućeg stabla; želimo li ispisati i samo stablo, treba za svaki vrh zabilježiti koji brid predstavlja njegov $dis$.

??? note "Implementacija"
    ```cpp
    // Primov algoritam optimiran binarnom hrpom.
    #include <cstring>
    #include <iostream>
    #include <queue>
    using namespace std;
    constexpr int N = 5050, M = 2e5 + 10;
    
    struct E {
      int v, w, x;
    } e[M * 2];
    
    int n, m, h[N], cnte;
    
    void adde(int u, int v, int w) { e[++cnte] = E{v, w, h[u]}, h[u] = cnte; }
    
    struct S {
      int u, d;
    };
    
    bool operator<(const S &x, const S &y) { return x.d > y.d; }
    
    priority_queue<S> q;
    int dis[N];
    bool vis[N];
    
    int res = 0, cnt = 0;
    
    void Prim() {
      memset(dis, 0x3f, sizeof(dis));
      dis[1] = 0;
      q.push({1, 0});
      while (!q.empty()) {
        if (cnt >= n) break;
        int u = q.top().u, d = q.top().d;
        q.pop();
        if (vis[u]) continue;
        vis[u] = true;
        ++cnt;
        res += d;
        for (int i = h[u]; i; i = e[i].x) {
          int v = e[i].v, w = e[i].w;
          if (w < dis[v]) {
            dis[v] = w, q.push({v, w});
          }
        }
      }
    }
    
    int main() {
      cin >> n >> m;
      for (int i = 1, u, v, w; i <= m; ++i) {
        cin >> u >> v >> w, adde(u, v, w), adde(v, u, w);
      }
      Prim();
      if (cnt == n)
        cout << res;
      else
        cout << "No MST.";
      return 0;
    }
    ```

### Dokaz

Krenimo od proizvoljnog vrha i podijelimo vrhove u dvije skupine: dodane i nedodane.

U svakom koraku među nedodanim vrhovima nađemo onaj čiji je najmanji brid prema dodanim vrhovima najmanji.

Zatim taj vrh dodamo i povežemo ga tim bridom najmanje težine.

Ponovimo $n-1$ puta.

Dokaz: opet pokazujemo da u svakom koraku postoji minimalno razapinjuće stablo koje sadrži odabrani skup bridova.

Baza: s jednim vrhom tvrdnja očito vrijedi.

Korak: ako tvrdnja vrijedi u nekom koraku, trenutačni skup bridova $F$ pripada MST-u $T$ i sljedeći dodajemo brid $e$.

Ako $e$ pripada $T$, tvrdnja vrijedi.

Inače promotrimo na ciklusu u $T+e$ drugi brid $f$ koji se mogao dodati trenutačnom skupu bridova.

Prvo, težina od $f$ sigurno nije manja od težine od $e$, inače bismo odabrali $f$, a ne $e$.

Zatim, težina od $f$ sigurno nije veća od težine od $e$, inače bi $T+e-f$ bilo manje razapinjuće stablo.

Dakle, $e$ i $f$ imaju jednaku težinu, pa je $T+e-f$ također minimalno razapinjuće stablo i sadrži $F$.

## Borůvkin algoritam

Predstavljamo još jedan algoritam za minimalno razapinjuće stablo — Borůvkin algoritam. Njegova je ideja spoj prethodnih dvaju algoritama. Može se koristiti za traženje minimalne razapinjuće šume neusmjerenog grafa (za neusmjeren povezan graf to je minimalno razapinjuće stablo).

Borůvkin algoritam ima prednost u zadacima u kojima bridovi imaju mnogo posebnih svojstava, npr. u zadatku s potpunim grafom [CF888G](https://codeforces.com/problemset/problem/888/G).

Za opis algoritma trebamo nekoliko definicija:

1.  Neka je $E'$ skup bridova dosad pronađene minimalne razapinjuće šume. Tijekom algoritma postupno dodajemo bridove u $E'$; **povezana komponenta** je skup vrhova $V'\subseteq V$ takav da su bilo koja dva vrha $u$, $v$ tog skupa povezana (međusobno dostižna) u podgrafu sastavljenom od bridova iz $E'$.
2.  **Najmanji brid** povezane komponente je brid najmanje težine među bridovima koji je spajaju s drugim povezanim komponentama.

Na početku je $E'=\varnothing$ i svaki je vrh zasebna povezana komponenta:

1.  Izračunaj kojoj povezanoj komponenti pripada svaki vrh. Svakoj povezanoj komponenti postavi „nema najmanjeg brida”.
2.  Prođi sve bridove $(u, v)$; ako $u$ i $v$ nisu u istoj povezanoj komponenti, težinom tog brida ažuriraj najmanji brid komponenata u kojima su $u$ odnosno $v$.
3.  Ako nijedna povezana komponenta nema najmanjeg brida, završi; tadašnji $E'$ skup je bridova minimalne razapinjuće šume izvornog grafa. Inače dodaj u $E'$ najmanji brid svake povezane komponente koja ga ima i vrati se na prvi korak.

Evo primjera prikazanog animacijom (slika s [Wikipedije](https://en.wikipedia.org/wiki/Bor%C5%AFvka%27s_algorithm)):

![eg](./images/mst-1.apng)

Kad je izvorni graf povezan, broj povezanih komponenata u svakoj se iteraciji barem prepolovi, pa algoritam napravi najviše $O(\log V)$ iteracija; kad izvorni graf nije povezan, to je kao više potproblema, pa je složenost algoritma $O(E\log V)$. Pseudokod algoritma (prilagođeno s [Wikipedije](https://en.wikipedia.org/wiki/Bor%C5%AFvka%27s_algorithm)):

$$
\begin{array}{ll}
1 &  \textbf{Input. } \text{A graph }G\text{ whose edges have distinct weights. } \\
2 &  \textbf{Output. } \text{The minimum spanning forest of }G .  \\
3 &  \textbf{Method. }  \\
4 & \text{Initialize a forest }F\text{ to be a set of one-vertex trees} \\
5 &  \textbf{while } \text{True} \\
6 &  \qquad \text{Find the components of }F\text{ and label each vertex of }G\text{ by its component } \\
7 &  \qquad \text{Initialize the cheapest edge for each component to "None"} \\
8 &  \qquad  \textbf{for } \text{each edge }(u, v)\text{ of }G  \\
9 &  \qquad\qquad  \textbf{if }  u\text{ and }v\text{ have different component labels} \\
10 &  \qquad\qquad\qquad  \textbf{if }  (u, v)\text{ is cheaper than the cheapest edge for the component of }u  \\
11 &  \qquad\qquad\qquad\qquad\text{ Set }(u, v)\text{ as the cheapest edge for the component of }u \\
12 &  \qquad\qquad\qquad  \textbf{if }  (u, v)\text{ is cheaper than the cheapest edge for the component of }v  \\
13 &  \qquad\qquad\qquad\qquad\text{ Set }(u, v)\text{ as the cheapest edge for the component of }v  \\
14 &  \qquad  \textbf{if }\text{ all components'cheapest edges are "None"} \\
15 &  \qquad\qquad  \textbf{return }  F \\
16 &  \qquad  \textbf{for }\text{ each component whose cheapest edge is not "None"} \\
17 &  \qquad\qquad\text{ Add its cheapest edge to }F \\
\end{array}
$$

Treba paziti da usporedba bridova obično zahtijeva drugi ključ (npr. sortiranje po indeksu) kako bi se bridovi jednake težine mogli razlikovati.

## Zadaci za vježbu

-   [„HAOI2006” Pametni majmuni](https://www.luogu.com.cn/problem/P2504)
-   [„SCOI2005” Prometni grad](https://loj.ac/problem/2149)

## Jedinstvenost minimalnog razapinjućeg stabla

Razmotrimo jedinstvenost minimalnog razapinjućeg stabla. Ako neki brid **nije u skupu bridova minimalnog razapinjućeg stabla**, a može zamijeniti drugi brid **iste težine koji jest u skupu bridova minimalnog razapinjućeg stabla**, tada minimalno razapinjuće stablo nije jedinstveno.

Za Kruskalov algoritam dovoljno je izračunati koliko se bridova trenutačne težine može dodati i koliko ih je stvarno dodano; ako se te dvije vrijednosti razlikuju, ti bridovi s prethodnima tvore ciklus (u tom ciklusu postoje barem dva brida trenutačne težine, inače se prema DSU-u taj brid ne bi mogao dodati), tj. minimalno razapinjuće stablo nije jedinstveno.

Da bismo pronašli bridove iste težine kao trenutačni, dovoljno je pamtiti pokazivače na početak i kraj; monotonim redom to se rješava u vremenu $O(\alpha(m))$ (m je broj bridova), što je praktički jednako vremenu izvornog algoritma.

??? note "Primjer: [POJ 1679](http://poj.org/problem?id=1679)"
    ```cpp
    --8<-- "docs/graph/code/mst/mst_1.cpp"
    ```

## Drugo najmanje razapinjuće stablo

### Nestrogo drugo najmanje razapinjuće stablo

#### Definicija

U neusmjerenom grafu, razapinjuće stablo s najmanjim zbrojem težina bridova među onima čiji je zbroj težina **veći ili jednak** zbroju težina minimalnog razapinjućeg stabla.

#### Postupak rješavanja

-   Nađi minimalno razapinjuće stablo $T$ neusmjerenog grafa i neka je njegov zbroj težina $M$.
-   Prođi svaki neodabrani brid $e = (u,v,w)$, nađi brid najveće težine $e' = (s,t,w')$ na putu od $u$ do $v$ u $T$; zamjenom $e'$ s $e$ u $T$ dobivamo razapinjuće stablo $T'$ sa zbrojem težina $M' = M + w - w'$.
-   Uzmi minimum svih tako dobivenih $M'$.

Kako naći najveću težinu brida na putu između $u,v$?

Možemo to održavati binary liftingom: unaprijed izračunamo $2^i$-tog pretka svakog vrha i najveću težinu brida na putu do njegova $2^i$-tog pretka, pa to izravno dobivamo tijekom računanja LCA binary liftingom.

### Strogo drugo najmanje razapinjuće stablo

#### Definicija

U neusmjerenom grafu, razapinjuće stablo s najmanjim zbrojem težina bridova među onima čiji je zbroj težina **strogo veći** od zbroja težina minimalnog razapinjućeg stabla.

#### Postupak rješavanja

Promotrimo upravo opisani postupak za nestrogo drugo najmanje razapinjuće stablo: zašto je dobiveno rješenje nestrogo?

Zato što minimalno razapinjuće stablo jamči da najveća težina brida na putu od $u$ do $v$ u stablu sigurno **nije veća** od najveće težine brida na bilo kojem drugom putu od $u$ do $v$. Drugim riječima, kad je težina brida kojim zamjenjujemo jednaka težini zamijenjenog brida u izvornom stablu, dobiveno drugo najmanje razapinjuće stablo je nestrogo.

Rješenje se nameće samo: uz najveću težinu brida na putu do $2^i$-tog pretka održavamo i **strogo drugu najveću težinu brida**; kad je težina brida kojim zamjenjujemo jednaka najvećoj težini na putu u izvornom stablu, zamjenjujemo strogo drugom najvećom vrijednošću.

Taj se postupak može izvesti binary liftingom, složenost $O(m \log m)$.

??? note "Implementacija"
    ```cpp
    #include <algorithm>
    #include <iostream>
    
    constexpr int INF = 0x3fffffff;
    constexpr long long INF64 = 0x3fffffffffffffffLL;
    
    struct Edge {
      int u, v, val;
    
      bool operator<(const Edge &other) const { return val < other.val; }
    };
    
    Edge e[300010];
    bool used[300010];
    
    int n, m;
    long long sum;
    
    class Tr {
     private:
      struct Edge {
        int to, nxt, val;
      } e[600010];
    
      int cnt, head[100010];
    
      int pnt[100010][22];
      int dpth[100010];
      // brid najveće težine na putu do pretka
      int maxx[100010][22];
      // brid druge najveće težine na putu do pretka, -INF ako ne postoji
      int minn[100010][22];
    
     public:
      void addedge(int u, int v, int val) {
        e[++cnt] = Edge{v, head[u], val};
        head[u] = cnt;
      }
    
      void insedge(int u, int v, int val) {
        addedge(u, v, val);
        addedge(v, u, val);
      }
    
      void dfs(int now, int fa) {
        dpth[now] = dpth[fa] + 1;
        pnt[now][0] = fa;
        minn[now][0] = -INF;
        for (int i = 1; (1 << i) <= dpth[now]; i++) {
          pnt[now][i] = pnt[pnt[now][i - 1]][i - 1];
          int kk[4] = {maxx[now][i - 1], maxx[pnt[now][i - 1]][i - 1],
                       minn[now][i - 1], minn[pnt[now][i - 1]][i - 1]};
          // od četiriju vrijednosti uzmi najveću
          std::sort(kk, kk + 4);
          maxx[now][i] = kk[3];
          // uzmi strogo drugu najveću
          int ptr = 2;
          while (ptr >= 0 && kk[ptr] == kk[3]) ptr--;
          minn[now][i] = (ptr == -1 ? -INF : kk[ptr]);
        }
    
        for (int i = head[now]; i; i = e[i].nxt) {
          if (e[i].to != fa) {
            maxx[e[i].to][0] = e[i].val;
            dfs(e[i].to, now);
          }
        }
      }
    
      int lca(int a, int b) {
        if (dpth[a] < dpth[b]) std::swap(a, b);
    
        for (int i = 21; i >= 0; i--)
          if (dpth[pnt[a][i]] >= dpth[b]) a = pnt[a][i];
    
        if (a == b) return a;
    
        for (int i = 21; i >= 0; i--) {
          if (pnt[a][i] != pnt[b][i]) {
            a = pnt[a][i];
            b = pnt[b][i];
          }
        }
        return pnt[a][0];
      }
    
      int query(int a, int b, int val) {
        int res = -INF;
        for (int i = 21; i >= 0; i--) {
          if (dpth[pnt[a][i]] >= dpth[b]) {
            if (val != maxx[a][i])
              res = std::max(res, maxx[a][i]);
            else
              res = std::max(res, minn[a][i]);
            a = pnt[a][i];
          }
        }
        return res;
      }
    } tr;
    
    int fa[100010];
    
    int find(int x) { return fa[x] == x ? x : fa[x] = find(fa[x]); }
    
    void Kruskal() {
      int tot = 0;
      std::sort(e + 1, e + m + 1);
      for (int i = 1; i <= n; i++) fa[i] = i;
    
      for (int i = 1; i <= m; i++) {
        int a = find(e[i].u);
        int b = find(e[i].v);
        if (a != b) {
          fa[a] = b;
          tot++;
          tr.insedge(e[i].u, e[i].v, e[i].val);
          sum += e[i].val;
          used[i] = true;
        }
        if (tot == n - 1) break;
      }
    }
    
    int main() {
      std::ios::sync_with_stdio(false);
      std::cin.tie(nullptr);
    
      std::cin >> n >> m;
      for (int i = 1; i <= m; i++) {
        int u, v, val;
        std::cin >> u >> v >> val;
        e[i] = Edge{u, v, val};
      }
    
      Kruskal();
      long long ans = INF64;
      tr.dfs(1, 0);
    
      for (int i = 1; i <= m; i++) {
        if (!used[i]) {
          int _lca = tr.lca(e[i].u, e[i].v);
          // nađi najveću težinu brida na putu različitu od e[i].val
          long long tmpa = tr.query(e[i].u, _lca, e[i].val);
          long long tmpb = tr.query(e[i].v, _lca, e[i].val);
          // takav brid ne mora postojati; odgovor ažuriraj samo ako postoji
          if (std::max(tmpa, tmpb) > -INF)
            ans = std::min(ans, sum - std::max(tmpa, tmpb) + e[i].val);
        }
      }
      // ako drugo najmanje razapinjuće stablo ne postoji, ispiši -1
      std::cout << (ans == INF64 ? -1 : ans) << '\n';
      return 0;
    }
    ```

## Razapinjuće stablo uskog grla

### Definicija

Razapinjuće stablo uskog grla (bottleneck spanning tree) neusmjerenog grafa $G$ je razapinjuće stablo čija je najveća težina brida najmanja među svim razapinjućim stablima grafa $G$.

### Svojstva

**Biti minimalno razapinjuće stablo dovoljan je, ali ne i nužan uvjet za razapinjuće stablo uskog grla.** Drugim riječima, minimalno razapinjuće stablo nužno je razapinjuće stablo uskog grla, ali razapinjuće stablo uskog grla ne mora biti minimalno razapinjuće stablo.

Tvrdnju da je minimalno razapinjuće stablo nužno razapinjuće stablo uskog grla možemo dokazati kontradikcijom: neka je najveća težina brida u minimalnom razapinjućem stablu $w$. Ako minimalno razapinjuće stablo nije razapinjuće stablo uskog grla, onda su sve težine bridova razapinjućeg stabla uskog grla manje od $w$; dovoljno je iz izvornog minimalnog razapinjućeg stabla obrisati najdulji brid i jednim bridom razapinjućeg stabla uskog grla spojiti dva stabla nastala brisanjem; novo razapinjuće stablo sigurno ima manji zbroj težina od izvornog minimalnog razapinjućeg stabla, što je kontradikcija.

### Primjer

???+ note "POJ 2395 Out of Hay"
    Zadano je n farmi i m cesta; farme su numerirane od 1 do n. Čovjek kreće s farme 1 i obilazi ostale farme; traži se najveća težina vode koju će usput morati nositi, pri čemu na svakoj farmi može dopuniti vodu, a ukupna duljina puta treba biti najmanja.
    Traži se najveći brid stabla uskog grla, što se može riješiti traženjem minimalnog razapinjućeg stabla.

## Put minimalnog uskog grla

### Definicija

Put minimalnog uskog grla od x do y u neusmjerenom grafu $G$ jednostavan je put na kojem je najveća težina brida najmanja među svim jednostavnim putovima od x do y.

### Svojstva

Prema definiciji minimalnog razapinjućeg stabla, najveća težina brida na putu minimalnog uskog grla od x do y jednaka je najvećoj težini brida na putu od x do y u minimalnom razapinjućem stablu. Iako minimalno razapinjuće stablo nije jedinstveno, najveća težina brida na putu od x do y jednaka je u svakom minimalnom razapinjućem stablu i minimalna je. Drugim riječima, put od x do y u svakom minimalnom razapinjućem stablu put je minimalnog uskog grla.

Međutim, ne postoji za svaki put minimalnog uskog grla minimalno razapinjuće stablo u kojem je on jednostavan put od x do y.

Na primjer, na sljedećoj slici:

![](./images/mst5.png)

putovi minimalnog uskog grla od 1 do 4 očito su ova dva: 1-2-3-4 i 1-3-4.

No brid 1-2 ne pojavljuje se ni u jednom minimalnom razapinjućem stablu.

### Primjena

Budući da put minimalnog uskog grla nije jedinstven, obično se pita najveća težina brida na putu minimalnog uskog grla.

Drugim riječima, trebamo max na putu u minimalnom razapinjućem stablu.

To rješavaju i binary lifting i heavy-light dekompozicija, pa ovdje ne ulazimo u detalje.

## Kruskalovo rekonstruirano stablo

### Definicija

Tijekom izvođenja Kruskalova algoritma dodajemo bridove od najmanjeg prema najvećem. Zadržimo taj redoslijed.

Prvo napravimo $n$ skupova, svaki s točno jednim vrhom težine $0$.

Svako dodavanje brida spaja dva skupa; tada napravimo novi vrh čija je težina jednaka težini dodanog brida, a korijene dvaju skupova postavimo za lijevo odnosno desno dijete novog vrha. Zatim oba skupa i novi vrh spojimo u jedan skup i novi vrh postavimo za korijen.

Lako se vidi da nakon $n-1$ koraka dobivamo binarno stablo s točno $n$ listova u kojem svaki unutarnji vrh ima točno dvoje djece. To se stablo zove Kruskalovo rekonstruirano stablo.

Primjer:

![](./images/mst5.png)

Kruskalovo rekonstruirano stablo ovog grafa izgleda ovako:

![](./images/mst6.png)

### Svojstva

Lako se vidi: minimum najveće težine brida po svim jednostavnim putovima između dvaju vrhova izvornog grafa = najveća težina na jednostavnom putu između tih vrhova u minimalnom razapinjućem stablu = težina LCA tih dvaju vrhova u Kruskalovu rekonstruiranom stablu.

Drugim riječima, svi vrhovi $y$ za koje je minimum najveće težine brida na jednostavnom putu do vrha $x$ $\leq val$ nalaze se u nekom podstablu Kruskalova rekonstruiranog stabla i upravo su svi listovi tog podstabla.

U Kruskalovu rekonstruiranom stablu nađemo najplići vrh težine $\leq val$ na putu od $x$ do korijena. To je očito korijen podstabla u kojem su svi vrhovi koji zadovoljavaju uvjet.

Ako treba naći maksimum najmanje težine brida po svim jednostavnim putovima između dvaju vrhova izvornog grafa, u Kruskalovu algoritmu dodajemo bridove po padajućoj težini.

??? note "[„LOJ 137” Put minimalnog uskog grla, pojačana verzija](https://loj.ac/problem/137)"
    ```cpp
    --8<-- "docs/graph/code/mst/mst_2.cpp"
    ```

??? note "[NOI 2018 Povratak kući](https://uoj.ac/problem/393)"
    Prvo unaprijed izračunamo najkraći put od svakog vrha do korijena.
    
    Zatim izgradimo maksimalno razapinjuće stablo prema nadmorskoj visini. Očito su vrhovi dostižni u pojedinom upitu oni kojima je najmanja težina brida na putu do upitnog vrha u maksimalnom razapinjućem stablu $> p$.
    
    Prema svojstvima Kruskalova rekonstruiranog stabla, ti su vrhovi svi u jednom podstablu i upravo su svi njegovi listovi.
    
    Drugim riječima, dovoljno je za svako podstablo Kruskalova rekonstruiranog stabla izračunati min težina listova da bismo podržali upite na podstablu.
    
    Korijen za upit možemo naći binary liftingom na Kruskalovu rekonstruiranom stablu.
    
    Vremenska složenost $O((n+m+Q) \log n)$.
