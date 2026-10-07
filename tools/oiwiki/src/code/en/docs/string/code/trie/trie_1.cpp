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
      // if none of this node's children has this character, add it and record the node number of this character as ++tot
      if (!ch[u][c]) ch[u][c] = ++tot;
      u = ch[u][c];  // go one level deeper
    }
    tag[u] = 1;  // the name whose last character is node u has not been visited yet, record 1
  }

  scanf("%d", &m);

  while (m--) {
    scanf("%s", s + 1);
    int u = 1;
    for (int j = 1; s[j]; ++j) {
      int c = s[j] - 'a';
      u = ch[u][c];
      if (!u) break;  // no outgoing edge for this character, so the name does not exist
    }
    if (tag[u] == 1) {
      tag[u] = 2;  // the name whose last character is node u has already been visited
      puts("OK");
    } else if (tag[u] == 2)  // already visited, repeated visit
      puts("REPEAT");
    else
      puts("WRONG");
  }

  return 0;
}