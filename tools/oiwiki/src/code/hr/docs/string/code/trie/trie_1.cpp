#include <cstdio>
using namespace std;
constexpr int N = 500010;

char s[N];
int n, m, ch[N][26], tag[N], tot = 1;

int main() {
  scanf("%d", &n);

  for (int i = 1; i <= n; ++i) {
    scanf("%s", s + 1);
    int u = 1;
    for (int j = 1; s[j]; ++j) {
      int c = s[j] - 'a';
      // ako među djecom ovog čvora nema tog znaka, dodaj ga i zabilježi broj čvora tog znaka kao ++tot
      if (!ch[u][c]) ch[u][c] = ++tot;
      u = ch[u][c];  // idi jednu razinu dublje
    }
    tag[u] = 1;  // ime čiji je zadnji znak čvor u još nije prozvano, zabilježi 1
  }

  scanf("%d", &m);

  while (m--) {
    scanf("%s", s + 1);
    int u = 1;
    for (int j = 1; s[j]; ++j) {
      int c = s[j] - 'a';
      u = ch[u][c];
      if (!u) break;  // nema izlaznog brida za taj znak, pa ime ne postoji
    }
    if (tag[u] == 1) {
      tag[u] = 2;  // ime čiji je zadnji znak čvor u već je prozvano
      puts("OK");
    } else if (tag[u] == 2)  // već prozvano, ponovljena prozivka
      puts("REPEAT");
    else
      puts("WRONG");
  }

  return 0;
}