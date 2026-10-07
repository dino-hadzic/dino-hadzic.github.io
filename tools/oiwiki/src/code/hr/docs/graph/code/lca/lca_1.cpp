#include <cstring>
#include <iostream>
#include <vector>

constexpr int MXN = 40005;
using namespace std;
vector<int> v[MXN];
vector<int> w[MXN];

int fa[MXN][31], cost[MXN][31], dep[MXN];
int n, m;
int a, b, c;

// dfs koji priprema podatke za algoritam lca. Prima dva argumenta: početni čvor dfs-a i njegova roditelja.
void dfs(int root, int fno) {
  // Inicijalizacija: 2^0 = 1. predak je upravo roditelj, a dep je za 1 veći nego kod roditelja.
  fa[root][0] = fno;
  dep[root] = dep[fa[root][0]] + 1;
  // Inicijalizacija ostalih predaka: 2^i-ti predak je 2^(i-1)-ti predak
  // 2^(i-1)-tog pretka.
  for (int i = 1; i < 31; ++i) {
    fa[root][i] = fa[fa[root][i - 1]][i - 1];
    cost[root][i] = cost[fa[root][i - 1]][i - 1] + cost[root][i - 1];
  }
  // Prođi po djeci i nastavi dfs.
  int sz = v[root].size();
  for (int i = 0; i < sz; ++i) {
    if (v[root][i] == fno) continue;
    cost[v[root][i]][0] = w[root][i];
    dfs(v[root][i], root);
  }
}

// lca. Binary liftingom računa lca čvorova x i y.
int lca(int x, int y) {
  // Neka y bude dublji od x.
  if (dep[x] > dep[y]) swap(x, y);
  // Dovedi y na istu dubinu kao x.
  int tmp = dep[y] - dep[x], ans = 0;
  for (int j = 0; tmp; ++j, tmp >>= 1)
    if (tmp & 1) ans += cost[y][j], y = fa[y][j];
  // Ako je sada y = x, onda su x i y sami sebi predak.
  if (y == x) return ans;
  // Inače pronađi prva dva čvora koji nisu njihov zajednički predak.
  for (int j = 30; j >= 0 && y != x; --j) {
    if (fa[x][j] != fa[y][j]) {
      ans += cost[x][j] + cost[y][j];
      x = fa[x][j];
      y = fa[y][j];
    }
  }
  // Vrati rezultat.
  ans += cost[x][0] + cost[y][0];
  return ans;
}

void Solve() {
  cin.tie(nullptr)->sync_with_stdio(false);
  // Inicijaliziraj polje predaka fa, cijene cost i dubine dep.
  memset(fa, 0, sizeof(fa));
  memset(cost, 0, sizeof(cost));
  memset(dep, 0, sizeof(dep));
  // Učitaj stablo: ukupno n čvorova i m upita, u svakom se traži lca dvaju čvorova.
  cin >> n >> m;
  // inicijaliziraj bridove stabla i njihove težine
  for (int i = 1; i <= n; ++i) {
    v[i].clear();
    w[i].clear();
  }
  for (int i = 1; i < n; ++i) {
    cin >> a >> b >> c;
    v[a].push_back(b);
    v[b].push_back(a);
    w[a].push_back(c);
    w[b].push_back(c);
  }
  // Pokreni dfs radi računanja lca.
  dfs(1, 0);
  for (int i = 0; i < m; ++i) {
    cin >> a >> b;
    cout << lca(a, b) << '\n';
  }
}

int main() {
  cin.tie(nullptr)->sync_with_stdio(false);
  int T;
  cin >> T;
  while (T--) Solve();
  return 0;
}
