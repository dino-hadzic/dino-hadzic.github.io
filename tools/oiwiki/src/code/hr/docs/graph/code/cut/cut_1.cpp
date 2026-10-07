/*
Luogu P3388 [Predložak] Artikulacijski vrhovi (rezni vrhovi)
*/
#include <iostream>
#include <vector>
using namespace std;
int n, m;  // n: broj vrhova, m: broj bridova
int dfn[100001], low[100001], idx, res;
// dfn: vremenska oznaka (DFS redni broj) svakog vrha
// low: najmanja oznaka dohvatljiva bez prolaska kroz roditelja, idx: brojač vremena, res: broj rješenja
bool vis[100001], flag[100001];  // flag: odgovor, vis: označava je li vrh već obrađen
vector<int> edge[100001];        // za pohranu grafa

void Tarjan(int u, int fa) {  // u je trenutni vrh, fa je njegov roditelj
  vis[u] = true;              // označi
  low[u] = dfn[u] = ++idx;    // dodijeli vremensku oznaku
  int child = 0;              // broj djece vrha
  for (const auto &v : edge[u]) {  // obiđi sve susjede ovog vrha (C++11)
    if (!vis[v]) {
      child++;                       // još jedno dijete
      Tarjan(v, u);                  // nastavi
      low[u] = min(low[u], low[v]);  // ažuriraj najmanju dohvatljivu oznaku
      if (fa != u && low[v] >= dfn[u] && !flag[u]) {  // glavni dio
        // ako vrh nije korijen, najmanji vrh dohvatljiv bez roditelja zadovoljava uvjet za artikulacijski vrh i vrh još nije označen
        // uvjet: nakon brisanja roditelja ne može se doći više, tj. doseže najviše do roditelja
        flag[u] = true;
        res++;  // zabilježi odgovor
      }
    } else if (v != fa) {
      // ako ovaj vrh nije roditelj, ažuriraj najmanju dohvatljivu oznaku
      low[u] = min(low[u], dfn[v]);
    }
  }
  // glavni dio: korijen treba barem 2 djeteta
  if (fa == u && child >= 2 && !flag[u]) {
    flag[u] = true;
    res++;  // zabilježi odgovor
  }
}

int main() {
  cin >> n >> m;                  // učitaj podatke
  for (int i = 1; i <= m; i++) {  // vrhovi su numerirani od 1
    int x, y;
    cin >> x >> y;
    edge[x].push_back(y);
    edge[y].push_back(x);
  }  // graf pohranjen u vectorima
  for (int i = 1; i <= n; i++)  // jer graf ne mora biti povezan
    if (!vis[i]) {
      idx = 0;       // početna vremenska oznaka je 0
      Tarjan(i, i);  // kreni od vrha i, roditelj je on sam
    }
  cout << res << endl;
  for (int i = 1; i <= n; i++)
    if (flag[i]) cout << i << " ";  // ispiši rezultat
  return 0;
}
