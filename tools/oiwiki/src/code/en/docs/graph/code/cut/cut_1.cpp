/*
Luogu P3388 [Template] Cut vertices (articulation points)
*/
#include <iostream>
#include <vector>
using namespace std;
int n, m;  // n: number of vertices, m: number of edges
int dfn[100001], low[100001], idx, res;
// dfn: timestamp (DFS order) of every vertex
// low: smallest index reachable without going through the parent, idx: timestamp counter, res: number of answers
bool vis[100001], flag[100001];  // flag: answer, vis: marks whether a vertex was already handled
vector<int> edge[100001];        // stores the graph

void Tarjan(int u, int fa) {  // u is the current vertex, fa is its parent
  vis[u] = true;              // mark
  low[u] = dfn[u] = ++idx;    // assign the timestamp
  int child = 0;              // number of children of the vertex
  for (const auto &v : edge[u]) {  // visit all neighbors of this vertex (C++11)
    if (!vis[v]) {
      child++;                       // one more child
      Tarjan(v, u);                  // continue
      low[u] = min(low[u], low[v]);  // update the smallest reachable index
      if (fa != u && low[v] >= dfn[u] && !flag[u]) {  // main part
        // if it is not the root itself, the smallest vertex reachable without the parent satisfies the cut-vertex condition, and it has not been marked yet
        // the condition: after deleting the parent nothing above is reachable, i.e. it reaches at most the parent
        flag[u] = true;
        res++;  // record the answer
      }
    } else if (v != fa) {
      // if this vertex is not the parent, update the smallest reachable index
      low[u] = min(low[u], dfn[v]);
    }
  }
  // main part: the root itself needs at least 2 children
  if (fa == u && child >= 2 && !flag[u]) {
    flag[u] = true;
    res++;  // record the answer
  }
}

int main() {
  cin >> n >> m;                  // read the input
  for (int i = 1; i <= m; i++) {  // note that vertices are numbered from 1
    int x, y;
    cin >> x >> y;
    edge[x].push_back(y);
    edge[y].push_back(x);
  }  // the graph is stored in vectors
  for (int i = 1; i <= n; i++)  // because the graph need not be connected
    if (!vis[i]) {
      idx = 0;       // the timestamp starts at 0
      Tarjan(i, i);  // start from vertex i, with itself as parent
    }
  cout << res << endl;
  for (int i = 1; i <= n; i++)
    if (flag[i]) cout << i << " ";  // print the result
  return 0;
}
