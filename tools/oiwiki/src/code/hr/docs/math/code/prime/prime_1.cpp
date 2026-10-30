#include <iostream>
constexpr int p[15] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47};
// produkt prostih brojeva u p premašuje 1e18

int n;
long long ans = 2e18;

// u: indeks prostog broja u p koji trenutno razmatramo
// num: trenutno sastavljena vrijednost
// cnt: broj djelitelja trenutne vrijednosti
// pre: eksponent prethodnog faktora, ograničava eksponent koji sada biramo
void dfs(int u, long long num, long long cnt, int pre) {
  if (cnt > n || u >= 15) return;
  if (cnt == n) return ans = std::min(ans, num), void();
  for (int i = 1; i <= pre; ++i) {
    if (num * p[u] > ans) break;  // odsijecanje
    dfs(u + 1, num *= p[u], cnt * (i + 1), i);
  }
}

int main() {
  std::cin >> n;
  dfs(0, 1, 1, 59);  // floor(log2(1e18))=19
  std::cout << ans << std::endl;
  return 0;
}
