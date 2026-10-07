#include <algorithm>
#include <iostream>
using namespace std;

int fa[1010];  // polje roditelja (DSU)
int n, m, k;

struct edge {
  int u, v, w;
};

int l;
edge g[10010];

void add(int u, int v, int w) {
  l++;
  g[l].u = u;
  g[l].v = v;
  g[l].w = w;
}

// standardni DSU (union-find)
int findroot(int x) { return fa[x] == x ? x : fa[x] = findroot(fa[x]); }

void Merge(int x, int y) {
  x = findroot(x);
  y = findroot(y);
  fa[x] = y;
}

bool cmp(edge A, edge B) { return A.w < B.w; }

// Kruskalov algoritam
void kruskal() {
  int tot = 0;  // broj odabranih bridova
  int ans = 0;  // ukupni trošak
  for (int i = 1; i <= m; i++) {
    int xr = findroot(g[i].u), yr = findroot(g[i].v);
    if (xr != yr) {        // ako su predstavnici različiti
      Merge(xr, yr);       // spoji
      tot++;               // još jedan brid
      ans += g[i].w;       // dodaj trošak
      if (tot == n - k) {  // provjeri daje li broj odabranih bridova k šećernih vuna
        cout << ans << '\n';
        return;
      }
    }
  }
  cout << "No Answer\n";  // ne može se povezati
}

int main() {
  cin >> n >> m >> k;
  if (n == k) {  // poseban rubni slučaj
    cout << "0\n";
    return 0;
  }
  for (int i = 1; i <= n; i++) {  // inicijalizacija
    fa[i] = i;
  }
  for (int i = 1; i <= m; i++) {
    int u, v, w;
    cin >> u >> v >> w;
    add(u, v, w);  // dodaj brid
  }
  sort(g + 1, g + m + 1, cmp);  // prvo sortiraj po težini brida
  kruskal();
  return 0;
}
