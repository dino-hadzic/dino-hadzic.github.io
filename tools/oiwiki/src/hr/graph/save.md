---
title: Pohrana grafa
---

Da bismo u natjecateljskom programiranju mogli raditi s grafovima, prvo moramo naučiti kako se graf pohranjuje.

## Dogovor

Pretpostavljamo da je čitatelj već pročitao i razumio osnovne dijelove stranice [Osnovni pojmovi teorije grafova](./concept.md); ako pri čitanju naiđete na poteškoće, pojmove možete potražiti na toj stranici.

U ovom tekstu $n$ označava broj vrhova grafa, $m$ broj bridova, a $d^+(u)$ izlazni stupanj vrha $u$, tj. broj bridova koji izlaze iz $u$.

## Izravna pohrana bridova

### Postupak

Bridove pohranjujemo u niz čiji svaki element sadrži početni i završni vrh jednog brida (u težinskom grafu i težinu brida). (Ili koristimo više nizova, zasebno za početke, krajeve i težine.)

??? note "Primjer koda"
    === "C++"
        ```cpp
        #include <iostream>
        #include <vector>
        
        using namespace std;
        
        struct Edge {
          int u, v;
        };
        
        int n, m;
        vector<Edge> e;
        vector<bool> vis;
        
        bool find_edge(int u, int v) {
          for (int i = 1; i <= m; ++i) {
            if (e[i].u == u && e[i].v == v) {
              return true;
            }
          }
          return false;
        }
        
        void dfs(int u) {
          if (vis[u]) return;
          vis[u] = true;
          for (int i = 1; i <= m; ++i) {
            if (e[i].u == u) {
              dfs(e[i].v);
            }
          }
        }
        
        int main() {
          cin >> n >> m;
        
          vis.resize(n + 1, false);
          e.resize(m + 1);
        
          for (int i = 1; i <= m; ++i) cin >> e[i].u >> e[i].v;
        
          return 0;
        }
        ```
    
    === "Python"
        ```python
        class Edge:
            def __init__(self, u=0, v=0):
                self.u = u
                self.v = v
        
        
        n, m = map(int, input().split())
        
        e = [Edge() for _ in range(m)]
        vis = [False] * n
        
        for i in range(m):
            e[i].u, e[i].v = map(int, input().split())
        
        
        def find_edge(u, v):
            for i in range(m):
                if e[i].u == u and e[i].v == v:
                    return True
            return False
        
        
        def dfs(u):
            if vis[u]:
                return
            vis[u] = True
            for i in range(m):
                if e[i].u == u:
                    dfs(e[i].v)
        ```

### Složenost

Upit postoji li određeni brid: $O(m)$.

Obilazak svih izlaznih bridova jednog vrha: $O(m)$.

Obilazak cijelog grafa: $O(nm)$.

Prostorna složenost: $O(m)$.

### Primjena

Budući da je obilazak pri izravnoj pohrani bridova neučinkovit, ovaj se način u pravilu ne koristi za obilazak grafa.

U [Kruskalovom algoritmu](./mst.md#kruskal-算法) bridove treba sortirati po težini, pa ih je potrebno pohraniti izravno.

U nekim zadacima graf treba izgraditi više puta (npr. jednom izvorni graf, jednom obrnuti graf); tada možemo ili koristiti više drugih struktura podataka za istodobnu pohranu više grafova, ili izravno pohraniti bridove i iz njih ponovno izgraditi graf kad je to potrebno.

## Matrica susjedstva

### Postupak

Bridove pohranjujemo u dvodimenzionalni niz `adj`, gdje `adj[u][v]` jednako 1 znači da postoji brid od $u$ do $v$, a 0 da ne postoji. U težinskom grafu u `adj[u][v]` možemo pohraniti težinu brida od $u$ do $v$.

??? note "Primjer koda"
    === "C++"
        ```cpp
        #include <iostream>
        #include <vector>
        
        using namespace std;
        
        int n, m;
        vector<bool> vis;
        vector<vector<bool>> adj;
        
        bool find_edge(int u, int v) { return adj[u][v]; }
        
        void dfs(int u) {
          if (vis[u]) return;
          vis[u] = true;
          for (int v = 1; v <= n; ++v) {
            if (adj[u][v]) {
              dfs(v);
            }
          }
        }
        
        int main() {
          cin >> n >> m;
        
          vis.resize(n + 1);
          adj.resize(n + 1, vector<bool>(n + 1));
        
          for (int i = 1; i <= m; ++i) {
            int u, v;
            cin >> u >> v;
            adj[u][v] = true;
          }
        
          return 0;
        }
        ```
    
    === "Python"
        ```python
        vis = [False] * (n + 1)
        adj = [[False] * (n + 1) for _ in range(n + 1)]
        
        for i in range(1, m + 1):
            u, v = map(lambda x: int(x), input().split())
            adj[u][v] = True
        
        
        def find_edge(u, v):
            return adj[u][v]
        
        
        def dfs(u):
            if vis[u]:
                return
            vis[u] = True
            for v in range(1, n + 1):
                if adj[u][v]:
                    dfs(v)
        ```

### Složenost

Upit postoji li određeni brid: $O(1)$.

Obilazak svih izlaznih bridova jednog vrha: $O(n)$.

Obilazak cijelog grafa: $O(n^2)$.

Prostorna složenost: $O(n^2)$.

### Primjena

Matrica susjedstva prikladna je samo kad nema višestrukih bridova (ili ih se može zanemariti).

Njezina je najveća prednost upit o postojanju brida u $O(1)$.

Budući da je na rijetkim grafovima matrica susjedstva vrlo neučinkovita (osobito kad je vrhova mnogo, memorija to ne može podnijeti), obično se koristi samo na gustim grafovima.

## Lista susjedstva

### Postupak

Bridove pohranjujemo u niz struktura podataka koje podržavaju dinamičko dodavanje elemenata, npr. `vector<int> adj[n + 1]`, gdje `adj[u]` čuva podatke o svim izlaznim bridovima vrha $u$ (završni vrh, težina itd.).

??? note "Primjer koda"
    === "C++"
        ```cpp
        #include <iostream>
        #include <vector>
        
        using namespace std;
        
        int n, m;
        vector<bool> vis;
        vector<vector<int>> adj;
        
        bool find_edge(int u, int v) {
          for (int i = 0; i < adj[u].size(); ++i) {
            if (adj[u][i] == v) {
              return true;
            }
          }
          return false;
        }
        
        void dfs(int u) {
          if (vis[u]) return;
          vis[u] = true;
          for (int i = 0; i < adj[u].size(); ++i) dfs(adj[u][i]);
        }
        
        int main() {
          cin >> n >> m;
        
          vis.resize(n + 1);
          adj.resize(n + 1);
        
          for (int i = 1; i <= m; ++i) {
            int u, v;
            cin >> u >> v;
            adj[u].push_back(v);
          }
        
          return 0;
        }
        ```
    
    === "Python"
        ```python
        vis = [False] * (n + 1)
        adj = [[] for _ in range(n + 1)]
        
        for i in range(1, m + 1):
            u, v = map(lambda x: int(x), input().split())
            adj[u].append(v)
        
        
        def find_edge(u, v):
            for i in range(0, len(adj[u])):
                if adj[u][i] == v:
                    return True
            return False
        
        
        def dfs(u):
            if vis[u]:
                return
            vis[u] = True
            for i in range(0, len(adj[u])):
                dfs(adj[u][i])
        ```

### Složenost

Upit postoji li brid od $u$ do $v$: $O(d^+(u))$ (ako su bridovi prethodno sortirani, [binarnim pretraživanjem](../basic/binary.md) može se postići $O(\log(d^+(u)))$).

Obilazak svih izlaznih bridova vrha $u$: $O(d^+(u))$.

Obilazak cijelog grafa: $O(n+m)$.

Prostorna složenost: $O(m)$.

### Primjena

Prikladna je za pohranu svih vrsta grafova, osim ako postoje posebni zahtjevi (npr. kad treba brzo provjeravati postoji li brid, a vrhova je malo, može se koristiti matrica susjedstva).

Osobito je prikladna kad treba sortirati sve izlazne bridove nekog vrha.

## Ulančana lista susjedstva (forward star)

### Postupak

U biti je to lista susjedstva ostvarena vezanom listom; ključni kôd glasi:

=== "C++"
    ```cpp
    // početne vrijednosti head[u] i cnt su -1
    void add(int u, int v) {
      nxt[++cnt] = head[u];  // sljedbenik trenutnog brida
      head[u] = cnt;         // prvi brid iz vrha u
      to[cnt] = v;           // završni vrh trenutnog brida
    }
    
    // obilazak izlaznih bridova vrha u
    for (int i = head[u]; ~i; i = nxt[i]) {  // ~i znači i != -1
      int v = to[i];
    }
    ```

=== "Python"
    ```python
    # početne vrijednosti head[u] i cnt su -1
    def add(u, v):
        cnt = cnt + 1
        nex[cnt] = head[u]  # sljedbenik trenutnog brida
        head[u] = cnt  # prvi brid iz vrha u
        to[cnt] = v  # završni vrh trenutnog brida
    
    
    # obilazak izlaznih bridova vrha u
    i = head[u]
    while ~i:  # ~i znači i != -1
        v = to[i]
        i = nxt[i]
    ```

??? note "Primjer koda"
    ```cpp
    #include <iostream>
    #include <vector>
    
    using namespace std;
    
    int n, m;
    vector<bool> vis;
    vector<int> head, nxt, to;
    
    void add(int u, int v) {
      nxt.push_back(head[u]);
      head[u] = to.size();
      to.push_back(v);
    }
    
    bool find_edge(int u, int v) {
      for (int i = head[u]; ~i; i = nxt[i]) {  // ~i znači i != -1
        if (to[i] == v) {
          return true;
        }
      }
      return false;
    }
    
    void dfs(int u) {
      if (vis[u]) return;
      vis[u] = true;
      for (int i = head[u]; ~i; i = nxt[i]) dfs(to[i]);
    }
    
    int main() {
      cin >> n >> m;
    
      vis.resize(n + 1, false);
      head.resize(n + 1, -1);
    
      for (int i = 1; i <= m; ++i) {
        int u, v;
        cin >> u >> v;
        add(u, v);
      }
    
      return 0;
    }
    ```

### Složenost

Upit postoji li brid od $u$ do $v$: $O(d^+(u))$.

Obilazak svih izlaznih bridova vrha $u$: $O(d^+(u))$.

Obilazak cijelog grafa: $O(n+m)$.

Prostorna složenost: $O(m)$.

### Primjena

Prikladna je za pohranu svih vrsta grafova, ali ne omogućuje brzu provjeru postoji li brid niti jednostavno sortiranje izlaznih bridova vrha.

Prednost je što bridovi imaju indekse, što je ponekad vrlo korisno; osim toga, ako je početna vrijednost `cnt` neparna, pri pohrani dvosmjernih bridova `i ^ 1` je upravo suprotni brid od `i` (često se koristi u [mrežnim tokovima](./flow.md)).
