#include <cstring>
constexpr int MAXN = 100000;  // MAXN je ovdje granica apsolutne vrijednosti elemenata niza

int solve(int n, int a[]) {
  bool met[MAXN * 2 + 1];  // košara (bucket) koja prima vrijednosti iz [-MAXN, MAXN]
  memset(met, 0, sizeof(met));
  int ans = 0;
  for (int i = 0; i < n; ++i) {
    if (met[MAXN - a[i]]) ++ans;  // ako je traženi element već u košari, uvećaj odgovor
    met[MAXN + a[i]] = true;  // u svakom slučaju stavi trenutni element u košaru
  }
  return ans * 2;
}
