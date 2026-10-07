---
title: Minimalna arborescencija
---

## Definicija

Minimalno razapinjuće stablo na usmjerenom grafu (Directed Minimum Spanning Tree) naziva se minimalna arborescencija (minimalno usmjereno razapinjuće stablo).

Uobičajeni je algoritam Chu–Liuov algoritam (poznat i kao Edmondsov algoritam), koji rješava problem minimalne arborescencije u vremenu $O(nm)$.

## Postupak

1.  Za svaki vrh odaberi ulazni brid najmanje težine.
2.  Ako nema ciklusa, algoritam završava; inače sažmi ciklus i ažuriraj udaljenosti ostalih vrhova do ciklusa.

## Implementacija

```cpp
bool solve() {
  ans = 0;
  int u, v, root = 0;
  for (;;) {
    f(i, 0, n) in[i] = 1e100;
    f(i, 0, m) {
      u = e[i].s;
      v = e[i].t;
      if (u != v && e[i].w < in[v]) {
        in[v] = e[i].w;
        pre[v] = u;
      }
    }
    f(i, 0, m) if (i != root && in[i] > 1e50) return 0;
    int tn = 0;
    memset(id, -1, sizeof id);
    memset(vis, -1, sizeof vis);
    in[root] = 0;
    f(i, 0, n) {
      ans += in[i];
      v = i;
      while (vis[v] != i && id[v] == -1 && v != root) {
        vis[v] = i;
        v = pre[v];
      }
      if (v != root && id[v] == -1) {
        for (int u = pre[v]; u != v; u = pre[u]) id[u] = tn;
        id[v] = tn++;
      }
    }
    if (tn == 0) break;
    f(i, 0, n) if (id[i] == -1) id[i] = tn++;
    f(i, 0, m) {
      u = e[i].s;
      v = e[i].t;
      e[i].s = id[u];
      e[i].t = id[v];
      if (e[i].s != e[i].t) e[i].w -= in[v];
    }
    n = tn;
    root = id[root];
  }
  return ans;
}
```

## Tarjanov algoritam za DMST

Tarjan je predložio algoritam koji problem minimalne arborescencije rješava u vremenu $O(m+n\log n)$.

Opis algoritma i referentni kôd ovdje se temelje na bilješkama s predavanja profesora Urija Zwicka; više pojedinosti potražite u izvorniku.

### Postupak

Tarjanov algoritam sastoji se od dvaju postupaka: **sažimanja** i **razvijanja**. Prvo opisujemo postupak **sažimanja**.

Pretpostavljamo da je ulazni graf jako povezan; ako nije, dodamo $O(n)$ bridova beskonačne težine da bi to postao.

Trebamo hrpu (heap) koja za vrhove čuva oznake ulaznih bridova, njihove težine, ukupni trošak vrha i srodne podatke; budući da ćemo kasnije spajati hrpe, implementiramo je pomoću [ljevostranog stabla](../ds/leftist-tree.md) i [DSU-a](../ds/dsu.md). U svakom koraku algoritam odabire proizvoljan vrh $v$ koji nije korijen i čiji ulazni brid još nije u hrpi, te dodaje najmanji ulazni brid vrha $v$ u hrpu. Ako novododani brid s bridovima u hrpi zatvara ciklus, vrhove tog ciklusa sažimamo; sažete vrhove nazvat ćemo **supervrhovima** i nastavljamo postupak. Kad se svi vrhovi sažmu u jedan supervrh, sažimanje je gotovo. Nakon cijelog postupka sažimanja dobivamo stablo sažimanja, nad kojim zatim provodimo razvijanje.

Bridovi u hrpi uvijek tvore put $v_0\leftarrow v_1\leftarrow \dots\leftarrow v_k$; kako je graf jako povezan, taj put nužno postoji, a $v_i$ može biti bilo izvorni pojedinačni vrh bilo sažeti supervrh.

Na početku je $v_o=a$, gdje je $a$ proizvoljan vrh grafa. Svaki put biramo najmanji ulazni brid $v_k\leftarrow u$; ako $u$ nije jedan od vrhova $v_0,v_1,\dots,v_k$, proširujemo put s $v_{k+1}=u$. Ako je $u$ jedan od tih vrhova, recimo $v_i$, pronašli smo ciklus $v_i\leftarrow\dots\leftarrow v_k\leftarrow v_i$ i sažimamo ga u jedan supervrh $c$.

U red $P$ stavimo sve vrhove ili supervrhove i na početku odaberemo proizvoljan vrh $a$; dok god red nije prazan, izvodimo sljedeće korake:

1.  Odaberi najmanji ulazni brid vrha $a$, pazeći da ne bude petlja, i nađi vrh $b$ na drugom kraju. Ako vrh $b$ još nije zabilježen, ciklus nije nastao; postavi $a\leftarrow b$ i nastavi tražiti ciklus.

2.  Ako je $b$ već zabilježen, nastao je ciklus. Ukupni broj vrhova povećaj za jedan, prenumeriraj sve vrhove na ciklusu, spoji hrpe i ažuriraj ukupne težine vrhova/supervrhova. Ažuriranje težina znači da skupimo sve ulazne bridove vrhova na ciklusu i od njih oduzmemo težinu ulaznog brida na ciklusu.

![dmst1](./images/dmst1.png)

Na slici, jako povezani graf lijevo nakon sažimanja daje stablo sažimanja desno, pri čemu je $a$ supervrh nastao sažimanjem vrhova 1 i 2, $b$ supervrh nastao sažimanjem vrhova 3, 4 i 5, a $A$ je nastao sažimanjem supervrhova $a$ i $b$.

Postupak razvijanja razmjerno je jednostavan: polazeći od izvorno traženog korijena $r$, razvijamo svaki ciklus na putu od $r$ do korijena stabla sažimanja. Zatim polazimo od pretka $f_r$ vrha $r$ i razvijamo cikluse na njegovu putu do korijena, i tako dalje dok ne obiđemo sve vrhove.

### Implementacija

```cpp
#include <cstdio>
#include <cstring>
#include <queue>
#include <vector>
using namespace std;

using ll = long long;
constexpr int MAXN = 102;
constexpr int INF = 0x3f3f3f3f;

struct UnionFind {
  int fa[MAXN << 1];

  UnionFind() { memset(fa, 0, sizeof(fa)); }

  void clear(int n) { memset(fa + 1, 0, sizeof(int) * n); }

  int find(int x) { return fa[x] ? fa[x] = find(fa[x]) : x; }

  int operator[](int x) { return find(x); }
};

struct Edge {
  int u, v, w, w0;
};

struct Heap {
  Edge *e;
  int rk, constant;
  Heap *lch, *rch;

  Heap(Edge *_e) : e(_e), rk(1), constant(0), lch(NULL), rch(NULL) {}

  void push() {
    if (lch) lch->constant += constant;
    if (rch) rch->constant += constant;
    e->w += constant;
    constant = 0;
  }
};

Heap *merge(Heap *x, Heap *y) {
  if (!x) return y;
  if (!y) return x;
  if (x->e->w + x->constant > y->e->w + y->constant) swap(x, y);
  x->push();
  x->rch = merge(x->rch, y);
  if (!x->lch || x->lch->rk < x->rch->rk) swap(x->lch, x->rch);
  if (x->rch)
    x->rk = x->rch->rk + 1;
  else
    x->rk = 1;
  return x;
}

Edge *extract(Heap *&x) {
  Edge *r = x->e;
  x->push();
  x = merge(x->lch, x->rch);
  return r;
}

vector<Edge> in[MAXN];
int n, m, fa[MAXN << 1], nxt[MAXN << 1];
Edge *ed[MAXN << 1];
Heap *Q[MAXN << 1];
UnionFind id;

void contract() {
  bool mark[MAXN << 1];
  // Za svaki vrh grafa zabilježi vrhove koji su s njim povezani.
  for (int i = 1; i <= n; i++) {
    queue<Heap *> q;
    for (int j = 0; j < in[i].size(); j++) q.push(new Heap(&in[i][j]));
    while (q.size() > 1) {
      Heap *u = q.front();
      q.pop();
      Heap *v = q.front();
      q.pop();
      q.push(merge(u, v));
    }
    Q[i] = q.front();
  }
  mark[1] = true;
  for (int a = 1, b = 1, p; Q[a]; b = a, mark[b] = true) {
    // Nađi najmanji ulazni brid i njegov krajnji vrh, pazeći da nema petlje.
    do {
      ed[a] = extract(Q[a]);
      a = id[ed[a]->u];
    } while (a == b && Q[a]);
    if (a == b) break;
    if (!mark[a]) continue;
    // Sažmi pronađeni ciklus, prenumeriraj vrhove u ciklusu i ažuriraj ukupne težine.
    for (a = b, n++; a != n; a = p) {
      id.fa[a] = fa[a] = n;
      if (Q[a]) Q[a]->constant -= ed[a]->w;
      Q[n] = merge(Q[n], Q[a]);
      p = id[ed[a]->u];
      nxt[p == n ? b : p] = a;
    }
  }
}

ll expand(int x, int r);

ll expand_iter(int x) {
  ll r = 0;
  for (int u = nxt[x]; u != x; u = nxt[u]) {
    if (ed[u]->w0 >= INF)
      return INF;
    else
      r += expand(ed[u]->v, u) + ed[u]->w0;
  }
  return r;
}

ll expand(int x, int t) {
  ll r = 0;
  for (; x != t; x = fa[x]) {
    r += expand_iter(x);
    if (r >= INF) return INF;
  }
  return r;
}

void link(int u, int v, int w) { in[v].push_back({u, v, w, w}); }

int main() {
  int rt;
  scanf("%d %d %d", &n, &m, &rt);
  for (int i = 0; i < m; i++) {
    int u, v, w;
    scanf("%d %d %d", &u, &v, &w);
    link(u, v, w);
  }
  // osiguraj jaku povezanost
  for (int i = 1; i <= n; i++) link(i > 1 ? i - 1 : n, i, INF);
  contract();
  ll ans = expand(rt, n);
  if (ans >= INF)
    puts("-1");
  else
    printf("%lld\n", ans);
  return 0;
}
```

## Literatura

Uri Zwick. (2013),[Directed Minimum Spanning Trees](http://www.cs.tau.ac.il/~zwick/grad-algo-13/directed-mst.pdf), Lecture notes on "Analysis of Algorithms"

<https://riteme.site/blog/2018-6-18/mdst.html#_3>
