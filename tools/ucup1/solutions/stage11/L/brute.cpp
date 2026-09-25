// Brute force za male ploče: enumeracija redaka bez 4 jednake uzastopne, provjera stupaca i povezanosti.
#include <bits/stdc++.h>
using namespace std;
int n, m, best; vector<int> rows, cur, bestRows;
bool badRun(int a, int b, int c, int d) { return a == b && b == c && c == d; }
bool connectedOnes() {
    vector<vector<int>> vis(n, vector<int>(m, 0)); int total = 0, sx = -1, sy = -1;
    for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) if (cur[i] >> j & 1) { total++; sx = i; sy = j; }
    if (!total) return false;
    queue<pair<int,int>> q; q.push({sx, sy}); vis[sx][sy] = 1; int seen = 1;
    while (!q.empty()) { auto [x, y] = q.front(); q.pop();
        int dx[4] = {0,0,1,-1}, dy[4] = {1,-1,0,0};
        for (int d = 0; d < 4; d++) { int a = x+dx[d], b = y+dy[d];
            if (a<0||b<0||a>=n||b>=m||!(cur[a]>>b&1)||vis[a][b]) continue; vis[a][b]=1; seen++; q.push({a,b}); } }
    return seen == total;
}
void rec(int i, int ones) {
    if (ones + (n - i) * m <= best) return;
    if (i == n) { if (connectedOnes()) { best = ones; bestRows = cur; } return; }
    for (int r : rows) {
        if (i >= 3) { bool ok = true;
            for (int j = 0; j < m && ok; j++) if (badRun(cur[i-3]>>j&1, cur[i-2]>>j&1, cur[i-1]>>j&1, r>>j&1)) ok = false;
            if (!ok) continue; }
        cur[i] = r; rec(i + 1, ones + __builtin_popcount(r));
    }
}
int main() {
    int T; scanf("%d", &T);
    while (T--) {
        scanf("%d %d", &n, &m); rows.clear(); best = -1; cur.assign(n, 0);
        for (int r = 0; r < (1 << m); r++) { bool ok = true;
            for (int j = 0; j + 3 < m && ok; j++) if (badRun(r>>j&1, r>>(j+1)&1, r>>(j+2)&1, r>>(j+3)&1)) ok = false;
            if (ok) rows.push_back(r); }
        sort(rows.begin(), rows.end(), [](int a, int b) { return __builtin_popcount(a) > __builtin_popcount(b); });
        rec(0, 0);
        printf("%d\n", best);
        for (int i = 0; i < n; i++) { for (int j = 0; j < m; j++) putchar((bestRows[i]>>j&1) ? '1' : '0'); putchar('\n'); }
    }
}
