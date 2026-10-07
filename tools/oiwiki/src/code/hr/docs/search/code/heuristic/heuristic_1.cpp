#include <algorithm>
#include <iostream>
using namespace std;
constexpr int N = 105;
int n, m, ans;

struct Node {
  int a, b;  // a je vrijeme, b je vrijednost
  double f;
} node[N];

bool operator<(Node p, Node q) { return p.f > q.f; }

int f(int t, int v) {  // najveća vrijednost preostalih predmeta u preostalom vremenu
  int tot = 0;
  for (int i = 1; t + i <= n; i++)
    if (v >= node[t + i].a) {
      v -= node[t + i].a;
      tot += node[t + i].b;
    } else
      return (int)(tot + v * node[t + i].f);
  return tot;
}

void work(int t, int p, int v) {
  ans = max(ans, v);
  if (t > n) return;                         // rubni uvjet: postoji samo n vrsta predmeta
  if (f(t, p) + v > ans) work(t + 1, p, v);  // rezanje po optimalnosti
  if (node[t].a <= p) work(t + 1, p - node[t].a, v + node[t].b);  // rezanje po izvedivosti
}

int main() {
  cin.tie(nullptr)->sync_with_stdio(false);
  cin >> m >> n;
  for (int i = 1; i <= n; i++) {
    cin >> node[i].a >> node[i].b;
    node[i].f = 1.0 * node[i].b / node[i].a;  // f je omjer vrijednosti i vremena
  }
  sort(node + 1, node + n + 1);  // sortiraj po tom omjeru
  work(1, m, 0);
  cout << ans << '\n';
  return 0;
}
