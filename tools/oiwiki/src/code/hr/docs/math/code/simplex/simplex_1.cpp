#include <cmath>
#include <cstring>
#include <iostream>
using namespace std;
constexpr int M = 10005, N = 1005, INF = 1e9;

int n, m;
double a[M][N], b[M], c[N], v;

void pivot(int l, int e) {  // funkcija pivotiranja
  b[l] /= a[l][e];
  for (int j = 1; j <= n; j++)
    if (j != e) a[l][j] /= a[l][e];
  a[l][e] = 1 / a[l][e];

  for (int i = 1; i <= m; i++)
    if (i != l && fabs(a[i][e]) > 0) {
      b[i] -= a[i][e] * b[l];
      for (int j = 1; j <= n; j++)
        if (j != e) a[i][j] -= a[i][e] * a[l][j];
      a[i][e] = -a[i][e] * a[l][e];
    }

  v += c[e] * b[l];
  for (int j = 1; j <= n; j++)
    if (j != e) c[j] -= c[e] * a[l][j];
  c[e] = -c[e] * a[l][e];

  // swap(B[l],N[e])
}

double simplex() {
  while (true) {
    int e = 0, l = 0;
    for (e = 1; e <= n; e++)
      if (c[e] > (double)0) break;
    if (e == n + 1) return v;  // v je sada optimalna vrijednost
    double mn = INF;
    for (int i = 1; i <= m; i++) {
      if (a[i][e] > (double)0 && mn > b[i] / a[i][e]) {
        mn = b[i] / a[i][e];  // nađi l koji najstrože ograničava ovaj e
        l = i;
      }
    }
    if (mn == INF) return INF;  // unbounded
    pivot(l, e);                // pivotiraj l,e
  }
}

int main() {
  cin.tie(nullptr)->sync_with_stdio(false);
  cin >> n >> m;
  for (int i = 1; i <= n; i++) cin >> c[i];
  for (int i = 1; i <= m; i++) {
    int s, t;
    cin >> s >> t;
    for (int j = s; j <= t; j++) a[i][j] = 1;  // volonteri i-te vrste mogu raditi u vremenu j
    cin >> b[i];
  }
  cout << (int)(simplex() + 0.5);
}
