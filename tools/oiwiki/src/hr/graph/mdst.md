---
title: Razapinjuće stablo minimalnog promjera
---

Prije učenja razapinjućeg stabla minimalnog promjera (Minimum Diameter Spanning Tree) preporučujemo pročitati [Promjer stabla](./tree-diameter.md).

## Definicija

Među svim razapinjućim stablima neusmjerenog grafa, ono s najmanjim promjerom je razapinjuće stablo minimalnog promjera.

## Apsolutni centar grafa

Da bismo našli razapinjuće stablo minimalnog promjera, prvo moramo naći **apsolutni centar grafa**. **Apsolutni centar grafa** može se nalaziti na nekom bridu ili u nekom vrhu; to je točka za koju je maksimum najkraćih udaljenosti do svih vrhova najmanji.

Iz definicije **apsolutnog centra grafa** slijedi da postoje barem dva vrha najudaljenija od apsolutnog centra.

Neka je $d(i,j)$ duljina najkraćeg puta između vrhova $i,j$; najkraće putove između svih vrhova izračunamo algoritmom za najkraće putove iz više izvora.

$\textit{rk}(i,j)$ bilježi $j$-ti najbliži vrh vrhu $i$ među svim ostalim vrhovima.

Apsolutni centar grafa može biti na nekom bridu: prolazimo kroz sve bridove $w=(u,v)$ i pretpostavljamo da je apsolutni centar $c$ upravo na tom bridu. Tada je udaljenost do $u$ jednaka $x$ ($x \leq w$), a udaljenost do $v$ jednaka $w - x$.

Za proizvoljan vrh $i$ grafa udaljenost od apsolutnog centra $c$ do $i$ iznosi $d(c,i)=\min(d(u,i) + x, d(v,i) + (w - x))$.

Uzmimo za primjer vrh $i$; odnos položaja tog vrha i apsolutnog centra grafa prikazan je na slici.

![mdst1](./images/mdst-graph.svg)

Kako se apsolutni centar $c$ pomiče po bridu, dobivamo graf funkcije udaljenosti u ovisnosti o položaju $c$. Očito je graf funkcije $d(c,i)$ izlomljena linija sastavljena od dvaju segmenata jednakog nagiba.

![mdst2](./images/mdst-plot1.svg)

Za proizvoljan vrh grafa, funkcija udaljenosti od apsolutnog centra do najudaljenijeg vrha zapisuje se kao $f = \max\{ d(c,i)\},i \in[1,n]$, a njezin graf izgleda ovako.

![mdst3](./images/mdst-plot2.svg)

Apscisa najniže točke među sjecištima tih izlomljenih linija položaj je apsolutnog centra grafa.

Apsolutni centar grafa može biti i u nekom vrhu; tada ažuriramo pomoću vrha najudaljenijeg od kandidata, tj. $\textit{ans}\leftarrow \min(\textit{ans},d(i,\textit{rk}(i,n))\times 2)$.

### Postupak

1.  Algoritmom za najkraće putove iz više izvora ([Floyd](./shortest-path.md#floyd-算法), [Johnson](./shortest-path.md#johnson-全源最短路径算法) i sl.) izračunaj niz $d$;

2.  Izračunaj $\textit{rk}(i,j)$ i sortiraj ga uzlazno;

3.  Apsolutni centar grafa može biti u nekom vrhu: ažuriraj pomoću vrha najudaljenijeg od kandidata, prođi sve vrhove i minimum ažuriraj s $\textit{ans}\leftarrow \min(\textit{ans},d(i,\textit{rk}(i,n)) \times 2)$.

4.  Apsolutni centar grafa može biti na nekom bridu: prođi sve bridove. Za brid $w(u,v)$ kreni od vrha najudaljenijeg od $u$. Kad nastupi $d(v,\textit{rk}(u,i)) > \max_{j=i+1}^n d(v,\textit{rk}(u,j))$, ažuriraj s $\textit{ans}\leftarrow  \min(\textit{ans}, d(u,\textit{rk}(u,i))+\max_{j=i+1}^n d(v,\textit{rk}(u,j))+w(u,v))$, jer se u tom slučaju apsolutni centar grafa mijenja.

??? note "Implementacija"
    ```cpp
    bool cmp(int a, int b) { return val[a] < val[b]; }
    
    void Floyd() {
      for (int k = 1; k <= n; k++)
        for (int i = 1; i <= n; i++)
          for (int j = 1; j <= n; j++) d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
    }
    
    void solve() {
      Floyd();
      for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
          rk[i][j] = j;
          val[j] = d[i][j];
        }
        sort(rk[i] + 1, rk[i] + 1 + n, cmp);
      }
      int ans = INF;
      // apsolutni centar grafa može biti u vrhu
      for (int i = 1; i <= n; i++) ans = min(ans, d[i][rk[i][n]] * 2);
      // apsolutni centar grafa može biti na bridu
      for (int i = 1; i <= m; i++) {
        int u = a[i].u, v = a[i].v, w = a[i].w;
        for (int p = n, i = n - 1; i >= 1; i--) {
          if (d[v][rk[u][i]] > d[v][rk[u][p]]) {
            ans = min(ans, d[u][rk[u][i]] + d[v][rk[u][p]] + w);
            p = i;
          }
        }
      }
    }
    ```

### Primjer

-   [CodeForce 266D BerDonalds](https://codeforces.com/contest/266/problem/D)

## Razapinjuće stablo minimalnog promjera

Iz definicije apsolutnog centra grafa lako se vidi da je apsolutni centar grafa polovište promjera razapinjućeg stabla minimalnog promjera.

Da bismo našli razapinjuće stablo minimalnog promjera, prvo nađemo apsolutni centar grafa. Iz apsolutnog centra kao početnog vrha izgradimo stablo najkraćih putova i to je razapinjuće stablo minimalnog promjera.

??? note "Implementacija"
    ```cpp
    #include <algorithm>
    #include <climits>
    #include <iostream>
    #include <vector>
    using namespace std;
    constexpr int MAXN = 502;
    using ll = long long;
    using pii = pair<int, int>;
    ll d[MAXN][MAXN], dd[MAXN][MAXN], rk[MAXN][MAXN], val[MAXN];
    constexpr ll INF = 1e17;
    int n, m;
    
    bool cmp(int a, int b) { return val[a] < val[b]; }
    
    void floyd() {
      for (int k = 1; k <= n; k++)
        for (int i = 1; i <= n; i++)
          for (int j = 1; j <= n; j++) d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
    }
    
    struct node {
      ll u, v, w;
    } a[MAXN * (MAXN - 1) / 2];
    
    void solve() {
      // traženje apsolutnog centra grafa
      floyd();
      for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
          rk[i][j] = j;
          val[j] = d[i][j];
        }
        sort(rk[i] + 1, rk[i] + 1 + n, cmp);
      }
      ll P = 0, ansP = INF;
      // u vrhu
      for (int i = 1; i <= n; i++) {
        if (d[i][rk[i][n]] * 2 < ansP) {
          ansP = d[i][rk[i][n]] * 2;
          P = i;
        }
      }
      // na bridu
      int f1 = 0, f2 = 0;
      ll disu = INT_MIN, disv = INT_MIN, ansL = INF;
      for (int i = 1; i <= m; i++) {
        ll u = a[i].u, v = a[i].v, w = a[i].w;
        for (int p = n, i = n - 1; i >= 1; i--) {
          if (d[v][rk[u][i]] > d[v][rk[u][p]]) {
            if (d[u][rk[u][i]] + d[v][rk[u][p]] + w < ansL) {
              ansL = d[u][rk[u][i]] + d[v][rk[u][p]] + w;
              f1 = u, f2 = v;
              disu = (d[u][rk[u][i]] + d[v][rk[u][p]] + w) / 2 - d[u][rk[u][i]];
              disv = w - disu;
            }
            p = i;
          }
        }
      }
      cout << min(ansP, ansL) / 2 << '\n';
      // stablo najkraćih putova
      vector<pii> pp;
      for (int i = 1; i <= 501; ++i)
        for (int j = 1; j <= 501; ++j) dd[i][j] = INF;
      for (int i = 1; i <= 501; ++i) dd[i][i] = 0;
      if (ansP <= ansL) {
        for (int j = 1; j <= n; j++) {
          for (int i = 1; i <= m; ++i) {
            ll u = a[i].u, v = a[i].v, w = a[i].w;
            if (dd[P][u] + w == d[P][v] && dd[P][u] + w < dd[P][v]) {
              dd[P][v] = dd[P][u] + w;
              pp.push_back({u, v});
            }
            u = a[i].v, v = a[i].u, w = a[i].w;
            if (dd[P][u] + w == d[P][v] && dd[P][u] + w < dd[P][v]) {
              dd[P][v] = dd[P][u] + w;
              pp.push_back({u, v});
            }
          }
        }
        for (auto [x, y] : pp) cout << x << ' ' << y << '\n';
      } else {
        d[n + 1][f1] = disu;
        d[f1][n + 1] = disu;
        d[n + 1][f2] = disv;
        d[f2][n + 1] = disv;
        a[m + 1].u = n + 1, a[m + 1].v = f1, a[m + 1].w = disu;
        a[m + 2].u = n + 1, a[m + 2].v = f2, a[m + 2].w = disv;
        n += 1;
        m += 2;
        floyd();
        P = n;
        for (int j = 1; j <= n; j++) {
          for (int i = 1; i <= m; ++i) {
            ll u = a[i].u, v = a[i].v, w = a[i].w;
            if (dd[P][u] + w == d[P][v] && dd[P][u] + w < dd[P][v]) {
              dd[P][v] = dd[P][u] + w;
              pp.push_back({u, v});
            }
            u = a[i].v, v = a[i].u, w = a[i].w;
            if (dd[P][u] + w == d[P][v] && dd[P][u] + w < dd[P][v]) {
              dd[P][v] = dd[P][u] + w;
              pp.push_back({u, v});
            }
          }
        }
        cout << f1 << ' ' << f2 << '\n';
        for (auto [x, y] : pp)
          if (x != n && y != n) cout << x << ' ' << y << '\n';
      }
    }
    
    void init() {
      for (int i = 1; i <= 501; ++i)
        for (int j = 1; j <= 501; ++j) d[i][j] = INF;
      for (int i = 1; i <= 501; ++i) d[i][i] = 0;
    }
    
    int main() {
      init();
      cin >> n >> m;
      for (int i = 1; i <= m; ++i) {
        ll u, v, w;
        cin >> u >> v >> w;
        w *= 2;
        d[u][v] = w, d[v][u] = w;
        a[i].u = u, a[i].v = v, a[i].w = w;
      }
      solve();
      return 0;
    }
    ```

### Primjeri

[SPOJ MDST](https://www.spoj.com/problems/MDST/)

[timus 1569. Networking the "Iset"](https://acm.timus.ru/problem.aspx?space=1&num=1569)

[SPOJ PT07C - The GbAaY Kingdom](https://www.spoj.com/problems/PT07C)

## Literatura

[Play with Trees Solutions The GbAaY Kingdom](https://adn.botao.hu/adn-backup/blog/attachments/month_0705/32007531153238.pdf)
