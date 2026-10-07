---
title: Tok minimalne cijene
---

Prije čitanja ovog članka pročitajte dio s definicijama u članku [Uvod u tokove u mrežama](../flow.md).

## Tok s cijenama

Zadana je mreža $G=(V,E)$ u kojoj svaki brid, osim ograničenja kapaciteta $c(u,v)$, ima i cijenu $w(u,v)$ po jedinici toka.

Kad je tok kroz $(u,v)$ jednak $f(u,v)$, treba platiti cijenu $f(u,v)\times w(u,v)$.

I $w$ zadovoljava antisimetričnost, tj. $w(u,v)=-w(v,u)$.

Maksimalni tok s najmanjom ukupnom cijenom u toj mreži zove se **maksimalni tok minimalne cijene** (min-cost max-flow), tj. uz uvjet da se maksimizira $\sum_{(s,v)\in E}f(s,v)$, minimizira se $\sum_{(u,v)\in E}f(u,v)\times w(u,v)$.

## Algoritam SSP

Algoritam SSP (Successive Shortest Path) greedy je algoritam. Ideja mu je da svaki put traži povećavajući put s najmanjom jediničnom cijenom i duž njega povećava tok, sve dok u grafu više nema povećavajućih putova.

Ako u grafu postoji ciklus negativne jedinične cijene, algoritam SSP ne može točno izračunati maksimalni tok minimalne cijene te mreže. Tada prvo treba algoritmom za uklanjanje ciklusa ukloniti negativne cikluse iz grafa.

### Dokaz

Ispravnost algoritma SSP dokazujemo matematičkom indukcijom i kontradikcijom.

Neka je $f_i$ minimalna cijena pri toku $i$. Pretpostavljamo da u početnoj mreži **nema negativnih ciklusa**; tada je $f_0=0$.

Pretpostavimo da je $f_i$ dobiven algoritmom SSP minimalna cijena; polazeći od $f_i$, nalazimo najkraći povećavajući put i tako dobivamo $f_{i+1}$. Tada je $f_{i+1}-f_i$ duljina tog najkraćeg povećavajućeg puta.

Pretpostavimo da postoji manji $f_{i+1}$, označimo ga $f'_{i+1}$. Budući da je $f_{i+1}-f_i$ već najkraći povećavajući put, $f'_{i+1}-f_i$ nužno odgovara povećavajućem putu koji prolazi **barem jednim negativnim ciklusom**.

Tu nastaje kontradikcija: ako postoji povećavajući put koji prolazi barem jednim negativnim ciklusom, onda $f_i$ nije minimalna cijena. Naime, dovoljno je tom negativnom ciklusu dodati tok pa da cijena koja odgovara $f_i$ postane manja, a da se tok koji izlazi iz $s$ ne poveća.

Zaključno, algoritam SSP ispravno računa maksimalni tok minimalne cijene za mreže bez negativnih ciklusa.

### Vremenska složenost

Ako za najkraće putove koristimo [Bellman–Fordov algoritam](../shortest-path.md#bellmanford-算法), svako traženje povećavajućeg puta ima složenost $O(nm)$. Neka je maksimalni tok mreže $f$; tada je najgora složenost $O(nmf)$. Zapravo, algoritam SSP radi u [pseudopolinomnom vremenu](../../misc/cc-basic.md#pseudo-polynomial-time-伪多项式时间).

???+ note "Zašto je algoritam SSP pseudopolinoman?"
    Vremenska složenost algoritma SSP ima gornju granicu $O(nmf)$, što je polinom u veličini vrijednosti, pa je riječ o pseudopolinomnom vremenu.
    
    Može se konstruirati mreža s $m=n^2,f=2^{n/2}$[^note1] na kojoj složenost algoritma SSP doseže $O(n^3 2^{n/2})$, pa algoritam SSP nije polinoman.

### Implementacija

Dovoljno je u algoritmu EK ili Dinicovu algoritmu postupak traženja povećavajućeg puta zamijeniti traženjem povećavajućeg puta s najmanjom jediničnom cijenom pomoću algoritma za najkraći put.

??? note "Implementacija zasnovana na algoritmu EK"
    ```cpp
    struct qxx {
      int nex, t, v, c;
    };
    
    qxx e[M];
    int h[N], cnt = 1;
    
    void add_path(int f, int t, int v, int c) {
      e[++cnt] = qxx{h[f], t, v, c}, h[f] = cnt;
    }
    
    void add_flow(int f, int t, int v, int c) {
      add_path(f, t, v, c);
      add_path(t, f, 0, -c);
    }
    
    int dis[N], pre[N], incf[N];
    bool vis[N];
    
    bool spfa() {
      memset(dis, 0x3f, sizeof(dis));
      queue<int> q;
      q.push(s), dis[s] = 0, incf[s] = INF, incf[t] = 0;
      while (q.size()) {
        int u = q.front();
        q.pop();
        vis[u] = false;
        for (int i = h[u]; i; i = e[i].nex) {
          const int &v = e[i].t, &w = e[i].v, &c = e[i].c;
          if (!w || dis[v] <= dis[u] + c) continue;
          dis[v] = dis[u] + c, incf[v] = min(w, incf[u]), pre[v] = i;
          if (!vis[v]) q.push(v), vis[v] = true;
        }
      }
      return incf[t];
    }
    
    int maxflow, mincost;
    
    void update() {
      maxflow += incf[t];
      for (int u = t; u != s; u = e[pre[u] ^ 1].t) {
        e[pre[u]].v -= incf[t], e[pre[u] ^ 1].v += incf[t];
        mincost += incf[t] * e[pre[u]].c;
      }
    }
    
    // Poziv: while(spfa())update();
    ```

??? note "Implementacija zasnovana na Dinicovu algoritmu"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <cstring>
    #include <queue>
    
    constexpr int N = 5e3 + 5, M = 1e5 + 5;
    constexpr int INF = 0x3f3f3f3f;
    int n, m, tot = 1, lnk[N], cur[N], ter[M], nxt[M], cap[M], cost[M], dis[N], ret;
    bool vis[N];
    
    void add(int u, int v, int w, int c) {
      ter[++tot] = v, nxt[tot] = lnk[u], lnk[u] = tot, cap[tot] = w, cost[tot] = c;
    }
    
    void addedge(int u, int v, int w, int c) { add(u, v, w, c), add(v, u, 0, -c); }
    
    bool spfa(int s, int t) {
      memset(dis, 0x3f, sizeof(dis));
      memcpy(cur, lnk, sizeof(lnk));
      std::queue<int> q;
      q.push(s), dis[s] = 0, vis[s] = true;
      while (!q.empty()) {
        int u = q.front();
        q.pop(), vis[u] = false;
        for (int i = lnk[u]; i; i = nxt[i]) {
          int v = ter[i];
          if (cap[i] && dis[v] > dis[u] + cost[i]) {
            dis[v] = dis[u] + cost[i];
            if (!vis[v]) q.push(v), vis[v] = true;
          }
        }
      }
      return dis[t] != INF;
    }
    
    int dfs(int u, int t, int flow) {
      if (u == t) return flow;
      vis[u] = true;
      int ans = 0;
      for (int &i = cur[u]; i && ans < flow; i = nxt[i]) {
        int v = ter[i];
        if (!vis[v] && cap[i] && dis[v] == dis[u] + cost[i]) {
          int x = dfs(v, t, std::min(cap[i], flow - ans));
          if (x) ret += x * cost[i], cap[i] -= x, cap[i ^ 1] += x, ans += x;
        }
      }
      vis[u] = false;
      return ans;
    }
    
    int mcmf(int s, int t) {
      int ans = 0;
      while (spfa(s, t)) {
        int x;
        while ((x = dfs(s, t, INF))) ans += x;
      }
      return ans;
    }
    
    int main() {
      int s, t;
      scanf("%d%d%d%d", &n, &m, &s, &t);
      while (m--) {
        int u, v, w, c;
        scanf("%d%d%d%d", &u, &v, &w, &c);
        addedge(u, v, w, c);
      }
      int ans = mcmf(s, t);
      printf("%d %d\n", ans, ret);
      return 0;
    }
    ```

### Primal-dual algoritam

Složenost traženja najkraćeg puta Bellman–Fordom je $O(nm)$, što je i na rijetkim i na gustim grafovima lošije od Dijkstrina algoritma[^note2]. No u mreži postoje bridovi negativne jedinične cijene, pa se Dijkstrin algoritam ne može izravno primijeniti.

Ideja primal-dual algoritma slična je [Johnsonovu algoritmu za najkraće putove među svim parovima](../shortest-path.md#johnson-全源最短路径算法): svakom vrhu dodijelimo potencijal tako da cijene svih bridova u mreži (dalje kratko: težine bridova) postanu nenegativne, pa se Dijkstrinim algoritmom može naći povećavajući put s najmanjom jediničnom cijenom.

Najprije jednom pokrenemo algoritam za najkraći put i izračunamo najkraću udaljenost od izvora do svakog vrha (ujedno početni potencijal tog vrha) $h_i$. Zatim, kao u Johnsonovu algoritmu, bridu od $u$ do $v$ s jediničnom cijenom $w$ težinu postavimo na $w+h_u-h_v$.

Može se uočiti da nakon ovakvog postavljanja potencijala najkraći putovi u novoj mreži nužno odgovaraju najkraćim putovima u izvornoj mreži. Dokaz je već dan pri opisu Johnsonova algoritma i ovdje ga ne ponavljamo.

Za razliku od običnog problema najkraćeg puta, nakon svakog povećanja toka oblik grafa se mijenja, pa potencijale vrhova treba ažurirati.

Kako ih ažurirati? Prvo zaključak: neka je nakon povećanja najkraća udaljenost od izvora do vrha $i$ jednaka $d'_i$ (udaljenost dobivena nakon ponovnog postavljanja težina svih bridova); dovoljno je $h_i$ uvećati za $d'_i$. Dokažimo da su nakon ovakvog ažuriranja težine svih bridova u grafu nenegativne.

Lako se vidi da nakon jedne runde povećanja, budući da su neki bridovi $(i,j)$ na povećavajućem putu, u rezidualnoj mreži nastaje odgovarajući broj novih bridova $(j,i)$, i za njih nužno vrijedi $d'_i+(w(i,j)+h_i-h_j)=d'_j$ (inače brid $(i,j)$ ne bi bio na povećavajućem putu). Malom preobrazbom dobivamo $w(j,i)+(h_j+d'_j)-(h_i+d'_i)=0$. Dakle, težine novonastalih bridova su nenegativne.

Za postojeće bridove prije povećanja vrijedi $d'_i+(w(i,j)+h_i-h_j) - d'_j \geq 0$, pa je $w(i,j)+(d'_i+h_i)-(d'_j+h_j) \geq 0$, tj. uzimanje $h_i+d'_i$ kao novog potencijala neće učiniti težinu brida $(i,j)$ negativnom.

Zaključno, nakon povećanja sve su težine bridova nenegativne i Dijkstrinim algoritmom ispravno nalazimo najkraći put u grafu.

??? note "Referentni kod"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <cstring>
    #include <queue>
    constexpr int INF = 0x3f3f3f3f;
    using namespace std;
    
    struct edge {
      int v, f, c, next;
    } e[100005];
    
    struct node {
      int v, e;
    } p[10005];
    
    struct mypair {
      int dis, id;
    
      bool operator<(const mypair& a) const { return dis > a.dis; }
    
      mypair(int d, int x) { dis = d, id = x; }
    };
    
    int head[5005], dis[5005], vis[5005], h[5005];
    int n, m, s, t, cnt = 1, maxf, minc;
    
    void addedge(int u, int v, int f, int c) {
      e[++cnt].v = v;
      e[cnt].f = f;
      e[cnt].c = c;
      e[cnt].next = head[u];
      head[u] = cnt;
    }
    
    bool dijkstra() {
      priority_queue<mypair> q;
      for (int i = 1; i <= n; i++) dis[i] = INF;
      memset(vis, 0, sizeof(vis));
      dis[s] = 0;
      q.push(mypair(0, s));
      while (!q.empty()) {
        int u = q.top().id;
        q.pop();
        if (vis[u]) continue;
        vis[u] = 1;
        for (int i = head[u]; i; i = e[i].next) {
          int v = e[i].v, nc = e[i].c + h[u] - h[v];
          if (e[i].f && dis[v] > dis[u] + nc) {
            dis[v] = dis[u] + nc;
            p[v].v = u;
            p[v].e = i;
            if (!vis[v]) q.push(mypair(dis[v], v));
          }
        }
      }
      return dis[t] != INF;
    }
    
    void spfa() {
      queue<int> q;
      memset(h, 63, sizeof(h));
      h[s] = 0, vis[s] = 1;
      q.push(s);
      while (!q.empty()) {
        int u = q.front();
        q.pop();
        vis[u] = 0;
        for (int i = head[u]; i; i = e[i].next) {
          int v = e[i].v;
          if (e[i].f && h[v] > h[u] + e[i].c) {
            h[v] = h[u] + e[i].c;
            if (!vis[v]) {
              vis[v] = 1;
              q.push(v);
            }
          }
        }
      }
    }
    
    int main() {
      scanf("%d%d%d%d", &n, &m, &s, &t);
      for (int i = 1; i <= m; i++) {
        int u, v, f, c;
        scanf("%d%d%d%d", &u, &v, &f, &c);
        addedge(u, v, f, c);
        addedge(v, u, 0, -c);
      }
      spfa();  // najprije izračunaj početne potencijale
      while (dijkstra()) {
        int minf = INF;
        for (int i = 1; i <= n; i++) h[i] += dis[i];
        for (int i = t; i != s; i = p[i].v) minf = min(minf, e[p[i].e].f);
        for (int i = t; i != s; i = p[i].v) {
          e[p[i].e].f -= minf;
          e[p[i].e ^ 1].f += minf;
        }
        maxf += minf;
        minc += minf * h[t];
      }
      printf("%d %d\n", maxf, minc);
      return 0;
    }
    ```

## Zadaci

-   [„Luogu 3381” [Predložak] Maksimalni tok minimalne cijene](https://www.luogu.com.cn/problem/P3381)
-   [„Luogu 4452” Raspored letova](https://www.luogu.com.cn/problem/P4452)
-   [„SDOI 2009” Jutarnje trčanje](https://www.luogu.com.cn/problem/P2153)
-   [„SCOI 2007” Popravak automobila](https://www.luogu.com.cn/problem/P2053)
-   [„HAOI 2010” Narudžbe](https://www.luogu.com.cn/problem/P2517)
-   [„NOI 2012” Festival hrane](https://loj.ac/problem/2674)

## Literatura i bilješke

[^note1]: Detaljan postupak konstrukcije vidi u [blogu min\_25](https://web.archive.org/web/20211009144446/https://min-25.hatenablog.com/entry/2018/03/19/235802).

[^note2]: Na rijetkim grafovima s optimizacijom gomilom postiže se složenost $O(m \log n)$, a na gustim grafovima bez gomile složenost $O(n^2)$.
