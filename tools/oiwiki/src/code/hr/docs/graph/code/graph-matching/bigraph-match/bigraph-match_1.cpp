#include <algorithm>
#include <ctime>
#include <iostream>
#include <random>
#include <tuple>
#include <vector>

std::mt19937_64 rng(
    static_cast<std::mt19937_64::result_type>(std::time(nullptr)));

struct BipartiteGraph {
  int n1, n2;                       // broj vrhova u X odnosno Y
  std::vector<std::vector<int>> g;  // bridovi iz X u Y
  std::vector<int> ma, mb;  // sparivanja iz X u Y odnosno iz Y u X
  std::vector<bool> vis;    // oznake posjećenosti za DFS.

  BipartiteGraph(int n1, int n2)
      : n1(n1), n2(n2), g(n1), ma(n1, -1), mb(n2, -1) {}

  // Dodaj brid od u iz X do v iz Y.
  void add_edge(int u, int v) { g[u].emplace_back(v); }

  // Nađi uvećavajući put koji počinje u u.
  bool dfs(int u) {
    vis[u] = true;
    // Heuristika: kad god je moguće, traži nesparene vrhove.
    for (int v : g[u]) {
      if (mb[v] == -1) {
        ma[u] = v;
        mb[v] = u;
        return true;
      }
    }
    for (int v : g[u]) {
      if (!vis[mb[v]] && dfs(mb[v])) {
        ma[u] = v;
        mb[v] = u;
        return true;
      }
    }
    return false;
  }

  // Kuhnov algoritam za najveće sparivanje.
  std::vector<std::pair<int, int>> kuhn_maximum_matching() {
    // Nasumično promiješaj bridove.
    for (int u = 0; u < n1; ++u) {
      std::shuffle(g[u].begin(), g[u].end(), rng);
    }
    // U svakom krugu nađi maksimalan skup vršno disjunktnih uvećavajućih putova.
    while (true) {
      bool succ = false;
      vis.assign(n1, false);
      for (int u = 0; u < n1; ++u) {
        succ |= ma[u] == -1 && dfs(u);
      }
      if (!succ) break;
    }
    // Skupi sparene parove.
    std::vector<std::pair<int, int>> matches;
    matches.reserve(n1);
    for (int u = 0; u < n1; ++u) {
      if (ma[u] != -1) {
        matches.emplace_back(u, ma[u]);
      }
    }
    return matches;
  }
};

int main() {
  std::ios::sync_with_stdio(false), std::cin.tie(nullptr);
  int n1, n2, m;
  std::cin >> n1 >> n2 >> m;
  BipartiteGraph gr(n1, n2);
  for (int i = 0; i < m; ++i) {
    int u, v;
    std::cin >> u >> v;
    gr.add_edge(u, v);
  }
  auto res = gr.kuhn_maximum_matching();
  std::cout << res.size() << '\n';
  for (int i = 0; i < res.size(); ++i) {
    std::cout << res[i].first << ' ' << res[i].second << '\n';
  }
  return 0;
}
