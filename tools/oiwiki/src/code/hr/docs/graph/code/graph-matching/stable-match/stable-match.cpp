#include <iostream>
#include <queue>
#include <vector>

// Rješavač problema stabilnog braka.
// Pretpostavljamo stroge preferencije s nepotpunim listama.
struct StableMatching {
  int nx, ny;
  std::vector<std::vector<int>> pref_x,
      pref_y;  // Preferencije: draži prvi, samo prihvatljivi.
  std::vector<int> match_x, match_y;  // Sparivanje: -1 znači nesparen.

  StableMatching(int nx, int ny)
      : nx(nx),
        ny(ny),
        pref_x(nx),
        pref_y(ny),
        match_x(nx, -1),
        match_y(ny, -1) {}

  // Gale–Shapleyjev algoritam.
  // Složenost: O(nx * ny).
  void solve() {
    // Izračunaj rangove kojima Y rangira X.
    std::vector<std::vector<int>> ranks(ny, std::vector<int>(nx));
    for (int j = 0; j != ny; ++j) {
      for (int i = 0; i != (int)pref_y[j].size(); ++i) {
        ranks[j][pref_y[j][i]] = nx - i;
      }
    }
    // Inicijalizacija.
    std::vector<int> waitlist(ny);  // Rang najbolje prosidbe za j iz Y.
    std::vector<int> ids(nx);       // Sljedeći j iz Y kojeg će i iz X zaprositi.
    std::queue<int> q;              // Trenutno aktivni i iz X.
    for (int i = 0; i != nx; ++i) q.push(i);
    // Petlja.
    while (!q.empty()) {
      auto i = q.front();
      q.pop();
      if (ids[i] == (int)pref_x[i].size()) continue;  // Lista je iscrpljena.
      auto j = pref_x[i][ids[i]++];
      if (ranks[j][i] > waitlist[j]) {
        if (waitlist[j]) q.push(pref_y[j][nx - waitlist[j]]);
        waitlist[j] = ranks[j][i];
      } else {
        q.push(i);
      }
    }
    // Ispis.
    for (int j = 0; j != ny; ++j) {
      if (waitlist[j]) {
        int i = pref_y[j][nx - waitlist[j]];
        match_x[i] = j;
        match_y[j] = i;
      }
    }
  }
};

void solve() {
  // Unos.
  int n;
  std::cin >> n;
  StableMatching solver(n, n);
  for (int j = 0, x; j < n; ++j) {
    auto& cur = solver.pref_y[j];
    std::cin >> x;
    for (int i = 0; i < n; ++i) {
      std::cin >> x;
      cur.push_back(x - 1);
    }
  }
  for (int i = 0, y; i < n; ++i) {
    auto& cur = solver.pref_x[i];
    std::cin >> y;
    for (int j = 0; j < n; ++j) {
      std::cin >> y;
      cur.push_back(y - 1);
    }
  }
  // Riješi problem.
  solver.solve();
  // Ispis.
  for (int i = 0; i < n; ++i) {
    std::cout << (i + 1) << ' ' << (solver.match_x[i] + 1) << '\n';
  }
}

int main() {
  std::ios::sync_with_stdio(false), std::cin.tie(nullptr);
  int t;
  std::cin >> t;
  for (; t; --t) {
    solve();
  }
  return 0;
}
