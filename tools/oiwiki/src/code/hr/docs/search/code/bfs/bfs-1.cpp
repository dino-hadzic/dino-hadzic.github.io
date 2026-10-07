#include <iostream>
#include <queue>
using namespace std;

char a[110][110];    // karta labirinta
bool vis[110][110];  // oznake posjećenosti
int n, m;            // dimenzije labirinta

struct node {
  int x, y;
};  // struktura za koordinate

int dx[] = {0, 0, 1, -1}, dy[] = {1, -1, 0, 0};  // smjerovi (desno, lijevo, dolje, gore)

// provjera je li koordinata dopuštena
bool chk(int x, int y) {
  return (x >= 1 && x <= n && y >= 1 && y <= m  // unutar granica
          && !vis[x][y]                         // još nije posjećena
          && a[x][y] != '#');                   // nije prepreka
}

bool bfs() {
  queue<node> q;
  q.push({1, 1});  // početak u red
  vis[1][1] = 1;   // označi početak posjećenim
  while (!q.empty()) {
    node p = q.front();  // uzmi koordinate s početka reda
    q.pop();
    int px = p.x, py = p.y;
    if (px == n && py == m) return true;  // stigli smo do cilja – odmah vrati
    // proširi u četiri smjera
    for (int i = 0; i < 4; ++i) {
      int nx = px + dx[i], ny = py + dy[i];
      if (chk(nx, ny)) {   // provjera dopuštenosti
        q.push({nx, ny});  // nove koordinate u red
        vis[nx][ny] = 1;   // označi posjećenim
      }
    }
  }
  return false;
}

int main() {
  cin >> n >> m;
  for (int i = 1; i <= n; ++i)
    for (int j = 1; j <= m; ++j) cin >> a[i][j];
  cout << (bfs() ? "Yes" : "No") << endl;
  return 0;
}
