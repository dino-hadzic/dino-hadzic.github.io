// M. Izbriši stablo
// Centroidna dekompozicija: vrh dobiva razinu = dubina u centroidnom stablu
// (najviše floor(log2 n)+1 = 9 razina za n <= 500). Brišemo razine od najdublje
// prema korijenu. Nakon brisanja skupa S, u grafu su spojeni x,y točno ako put
// x..y u stablu ima sve unutarnje vrhove u S; dva vrha iste razine razdvaja vrh
// manje razine koji još nije izbrisan, pa je svaka razina nezavisan skup.
#include <bits/stdc++.h>
using namespace std;

int n;
vector<vector<int>> adj;
vector<int> sz, lvl;
vector<bool> removed;

int calc_size(int v, int p) {
    sz[v] = 1;
    for (int w : adj[v]) if (w != p && !removed[w]) sz[v] += calc_size(w, v);
    return sz[v];
}

int find_centroid(int v, int p, int total) {
    for (int w : adj[v]) if (w != p && !removed[w] && sz[w] * 2 > total) return find_centroid(w, v, total);
    return v;
}

void decompose(int v, int depth) {
    int total = calc_size(v, -1);
    int c = find_centroid(v, -1, total);
    lvl[c] = depth;
    removed[c] = true;
    for (int w : adj[c]) if (!removed[w]) decompose(w, depth + 1);
}

int main() {
    scanf("%d", &n);
    adj.assign(n + 1, {}); sz.assign(n + 1, 0); lvl.assign(n + 1, 0); removed.assign(n + 1, false);
    for (int i = 0; i < n - 1; ++i) {
        int x, y; scanf("%d %d", &x, &y);
        adj[x].push_back(y); adj[y].push_back(x);
    }
    decompose(1, 0);
    int maxl = *max_element(lvl.begin() + 1, lvl.end());
    printf("%d\n", maxl + 1);
    for (int d = maxl; d >= 0; --d) {          // od najdublje razine prema korijenu
        vector<int> v;
        for (int i = 1; i <= n; ++i) if (lvl[i] == d) v.push_back(i);
        printf("%d", (int)v.size());
        for (int x : v) printf(" %d", x);
        printf("\n");
    }
    return 0;
}
