#include <cstdio>
#include <cstring>
#include <queue>
using namespace std;

constexpr int N = 2e5 + 6;
constexpr int LEN = 2e6 + 6;
constexpr int SIZE = 2e5 + 6;

int n;

namespace AC {
struct Node {
  int son[26];  // djeca
  int ans;      // brojač podudaranja
  int fail;     // fail pokazivač
  int du;       // ulazni stupanj
  int idx;

  void init() {  // inicijalizacija čvora
    memset(son, 0, sizeof(son));
    ans = fail = idx = 0;
  }
} tr[SIZE];

int tot;  // ukupan broj čvorova
int ans[N], pidx;

void init() {
  tot = pidx = 0;
  tr[0].init();
}

void insert(char s[], int &idx) {
  int u = 0;
  for (int i = 1; s[i]; i++) {
    int &son = tr[u].son[s[i] - 'a'];  // referenca na sljedeće dijete
    if (!son) son = ++tot, tr[son].init();  // ako ne postoji, umetni novi čvor i inicijaliziraj ga
    u = son;                                // nastavi od sljedećeg čvora
  }
  // uzorci se mogu ponavljati, pa jednake preslikavamo na isti indeks
  if (!tr[u].idx) tr[u].idx = ++pidx;  // prvo pojavljivanje, dodijeli novi indeks
  idx = tr[u].idx;  // indeks ovog uzorka odgovara indeksu ovog čvora
}

void build() {
  queue<int> q;
  for (int i = 0; i < 26; i++)
    if (tr[0].son[i]) q.push(tr[0].son[i]);
  while (!q.empty()) {
    int u = q.front();
    q.pop();
    for (int i = 0; i < 26; i++) {
      if (tr[u].son[i]) {                               // odgovarajuće dijete postoji
        tr[tr[u].son[i]].fail = tr[tr[u].fail].son[i];  // dovoljan je jedan skok po fail pokazivaču
        tr[tr[tr[u].fail].son[i]].du++;                 // brojanje ulaznog stupnja
        q.push(tr[u].son[i]);                           // i dodaj u red
      } else
        tr[u].son[i] =
            tr[tr[u].fail]
                .son[i];  // nepostojeće stanje trieja povezujemo s odgovarajućim stanjem fail pokazivača
    }
  }
}

void query(char t[]) {
  int u = 0;
  for (int i = 1; t[i]; i++) {
    u = tr[u].son[t[i] - 'a'];  // prijelaz
    tr[u].ans++;
  }
}

void topu() {
  queue<int> q;
  for (int i = 0; i <= tot; i++)
    if (tr[i].du == 0) q.push(i);
  while (!q.empty()) {
    int u = q.front();
    q.pop();
    ans[tr[u].idx] = tr[u].ans;
    int v = tr[u].fail;
    tr[v].ans += tr[u].ans;
    if (!--tr[v].du) q.push(v);
  }
}
}  // namespace AC

char s[LEN];
int idx[N];

int main() {
  AC::init();
  scanf("%d", &n);
  for (int i = 1; i <= n; i++) {
    scanf("%s", s + 1);
    AC::insert(s, idx[i]);
    AC::ans[i] = 0;
  }
  AC::build();
  scanf("%s", s + 1);
  AC::query(s);
  AC::topu();
  for (int i = 1; i <= n; i++) {
    printf("%d\n", AC::ans[idx[i]]);
  }
  return 0;
}
