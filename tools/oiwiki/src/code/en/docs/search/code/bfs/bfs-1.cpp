#include <iostream>
#include <queue>
using namespace std;

char a[110][110];    // maze map
bool vis[110][110];  // visited flags
int n, m;            // maze size

struct node {
  int x, y;
};  // coordinate struct

int dx[] = {0, 0, 1, -1}, dy[] = {1, -1, 0, 0};  // direction arrays (right, left, down, up)

// check whether a coordinate is valid
bool chk(int x, int y) {
  return (x >= 1 && x <= n && y >= 1 && y <= m  // bounds check
          && !vis[x][y]                         // not visited yet
          && a[x][y] != '#');                   // not an obstacle
}

bool bfs() {
  queue<node> q;
  q.push({1, 1});  // enqueue the start
  vis[1][1] = 1;   // mark the start as visited
  while (!q.empty()) {
    node p = q.front();  // take the coordinates at the front of the queue
    q.pop();
    int px = p.x, py = p.y;
    if (px == n && py == m) return true;  // reached the target – return immediately
    // expand in the four directions
    for (int i = 0; i < 4; ++i) {
      int nx = px + dx[i], ny = py + dy[i];
      if (chk(nx, ny)) {   // validity check
        q.push({nx, ny});  // enqueue the new coordinates
        vis[nx][ny] = 1;   // mark as visited
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
