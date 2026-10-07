---
title: Usmjereni aciklički graf
---

## Definicija

Bridovi su usmjereni, a ciklusa nema.

Engleski naziv je Directed Acyclic Graph, skraćeno DAG.

## Svojstva

-   Graf koji se može [topološki sortirati](./topo.md) sigurno je usmjereni aciklički graf;

    Ako postoji ciklus, bilo koja dva vrha na ciklusu ne mogu zadovoljiti uvjet ni u jednom poretku.

-   Usmjereni aciklički graf sigurno se može topološki sortirati;

    (Indukcijom.) Pretpostavimo da se svaki usmjereni aciklički graf s manje od $k$ vrhova može topološki sortirati; za graf s točno $k$ vrhova dovoljno je promotriti situaciju nakon prvog koraka topološkog sortiranja.

## Provjera

Kako provjeriti je li graf usmjereni aciklički graf?

Dovoljno je provjeriti može li se [topološki sortirati](./topo.md).

Naravno, postoji i drugi način: napravimo jedan [DFS](../search/dfs.md) po grafu i u dobivenom DFS stablu pogledamo postoji li nestablasti brid koji vodi prema pretku (povratni brid). Ako postoji, graf ima ciklus.

## Primjene

### Najdulji (najkraći) put pomoću DP-a

U općem grafu najbolja vremenska složenost za najdulji (najkraći) put iz jednog izvora je $O(nm)$ ([Bellman–Fordov algoritam](./shortest-path.md#bellmanfordov-algoritam), radi i s negativnim težinama) ili $O(m \log m)$ ([Dijkstrin algoritam](./shortest-path.md#dijkstrin-algoritam), bez negativnih težina).

No u DAG-u najdulji (najkraći) put možemo tražiti DP-om i složenost spustiti na $O(n+m)$. Prijelaz stanja je $dis_v = min(dis_v, dis_u + w_{u,v})$ odnosno $dis_v = max(dis_v, dis_u + w_{u,v})$.

Nakon topološkog sortiranja obilazimo vrhove u topološkom poretku i trenutnim vrhom ažuriramo vrhove nakon njega.

```cpp
struct edge {
  int v, w;
};

int n, m;
vector<edge> e[MAXN];
vector<int> L;                               // rezultat topološkog sortiranja
int max_dis[MAXN], min_dis[MAXN], in[MAXN];  // in čuva ulazni stupanj svakog vrha

void toposort() {  // topološko sortiranje
  queue<int> S;
  memset(in, 0, sizeof(in));
  for (int i = 1; i <= n; i++) {
    for (int j = 0; j < e[i].size(); j++) {
      in[e[i][j].v]++;
    }
  }
  for (int i = 1; i <= n; i++)
    if (in[i] == 0) S.push(i);
  while (!S.empty()) {
    int u = S.front();
    S.pop();
    L.push_back(u);
    for (int i = 0; i < e[u].size(); i++) {
      if (--in[e[u][i].v] == 0) {
        S.push(e[u][i].v);
      }
    }
  }
}

void dp(int s) {  // najdulji (najkraći) put iz jednog izvora s
  toposort();     // najprije topološko sortiranje
  memset(min_dis, 0x3f, sizeof(min_dis));
  memset(max_dis, 0, sizeof(max_dis));
  min_dis[s] = 0;
  for (int i = 0; i < L.size(); i++) {
    int u = L[i];
    for (int j = 0; j < e[u].size(); j++) {
      min_dis[e[u][j].v] = min(min_dis[e[u][j].v], min_dis[u] + e[u][j].w);
      max_dis[e[u][j].v] = max(max_dis[e[u][j].v], max_dis[u] + e[u][j].w);
    }
  }
}
```

Vidi i: [DP na DAG-u](../dp/dag.md).
