// G. Teleport
// f_{2j}(x,y) = (x+j, y+j),  f_{2j+1}(x,y) = (y+j+1, x+j): ciljevi teleporta su
// prefiksi dviju dijagonala (glavna kroz (x,y) i "zrcalna" kroz (y+1,x)).
// BFS po udaljenosti; unutar dijagonale preskačemo već posjećene ćelije
// strukturom "sljedeća neposjećena" (union-find s kompresijom putova), pa se
// svaka ćelija posjeti jednom: O(n^2 alpha).
#include <bits/stdc++.h>
using namespace std;

int n, k;
vector<char> vis;           // vis[(x-1)*n + (y-1)] = 1 ako je ćelija posjećena ili neprohodna (red-major, brzi susjedi)
vector<int> nxt;            // union-find po dijagonalama: sljedeća neposjećena pozicija (samo za teleporte)
vector<int> base;           // početak dijagonale d u polju nxt (dijagonala d = x-y+n-1, sa stražarom na kraju)

inline int diag_len(int d) { return n - abs(d - (n - 1)); }
inline int pos_of(int x, int y) { return base[x - y + n - 1] + min(x, y) - 1; }

int find(int p) {           // prva neposjećena pozicija >= p (stražar je uvijek "neposjećen")
    int r = p;
    while (nxt[r] != r) r = nxt[r];
    while (nxt[p] != r) { int q = nxt[p]; nxt[p] = r; p = q; }
    return r;
}

int main() {
    scanf("%d %d", &n, &k);
    vis.assign((size_t)n * n, 0);
    static char buf[5005];
    for (int i = 0; i < n; ++i) {
        scanf("%s", buf);
        for (int j = 0; j < n; ++j) vis[(size_t)i * n + j] = (buf[j] == '*');
    }
    base.resize(2 * n);
    int total = 0;
    for (int d = 0; d < 2 * n - 1; ++d) { base[d] = total; total += diag_len(d) + 1; }
    base[2 * n - 1] = total;
    nxt.resize(total);
    for (int p = 0; p < total; ++p) nxt[p] = p;
    // neprohodne ćelije označi kao posjećene
    for (int x = 1; x <= n; ++x)
        for (int y = 1; y <= n; ++y)
            if (vis[(size_t)(x - 1) * n + (y - 1)]) { int p = pos_of(x, y); nxt[p] = p + 1; }

    vector<int> q; q.reserve((size_t)n * n);
    auto visit = [&](int x, int y) {           // označi (x,y) posjećenim i stavi u red
        int p = pos_of(x, y); nxt[p] = p + 1;
        vis[(size_t)(x - 1) * n + (y - 1)] = 1;
        q.push_back((x - 1) * n + (y - 1));
    };
    // obilazak dijagonale d na pozicijama [t1, t2] (u koordinatama duž dijagonale)
    auto sweep = [&](int d, int t1, int t2) {
        int len = diag_len(d);
        if (t1 < 0) t1 = 0;
        if (t2 > len - 1) t2 = len - 1;
        if (t1 > t2) return;
        int p = base[d] + t1, hi = base[d] + t2;
        if (nxt[p] != p) p = find(p);          // brzi put: prva ćelija još neposjećena
        while (p <= hi) {
            int t = p - base[d];
            int x, y;
            if (d >= n - 1) { y = t + 1; x = y + (d - (n - 1)); }
            else            { x = t + 1; y = x - (d - (n - 1)); }
            visit(x, y);
            p = (nxt[p + 1] == p + 1) ? p + 1 : find(p + 1);
        }
    };

    visit(1, 1);
    size_t head = 0;
    int dist = 0;
    const int target = (n - 1) * n + (n - 1);
    while (head < q.size()) {
        size_t end = q.size();
        for (; head < end; ++head) {
            int c = q[head];
            if (c == target) { printf("%d\n", dist); return 0; }
            int x = c / n + 1, y = c % n + 1;
            const int dx[4] = {1, -1, 0, 0}, dy[4] = {0, 0, 1, -1};
            for (int dir = 0; dir < 4; ++dir) {
                int nx = x + dx[dir], ny = y + dy[dir];
                if (nx < 1 || ny < 1 || nx > n || ny > n) continue;
                if (!vis[(size_t)(nx - 1) * n + (ny - 1)]) visit(nx, ny);
            }
            if (k >= 2) {                    // f_2, f_4, ...: (x+j, y+j), j = 1..k/2
                int d = x - y + n - 1, t = min(x, y) - 1;
                sweep(d, t + 1, t + k / 2);
            }
            if (k >= 1) {                    // f_1, f_3, ...: (y+1+j, x+j), j = 0..(k-1)/2
                int d = (y + 1) - x + n - 1, t = min(y + 1, x) - 1;
                if (y + 1 <= n) sweep(d, t, t + (k - 1) / 2);
            }
        }
        ++dist;
    }
    printf("-1\n");
    return 0;
}
