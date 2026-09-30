// C. Connected Intervals – sweep po r + segmentno stablo (min, broj minimuma), O(n log n)
// Inducirani podgraf stabla na [l,r] je šuma s r-l+1 vrhova i e(l,r) bridova, pa je povezan
// točno kada je e(l,r) = r-l. Za fiksni r čuvamo d(l) = (r-l) - e(l,r) >= 0 za sve l <= r;
// prelazak r -> r+1 je: +1 na [1,r], a za svaki brid (u,r+1), u<r+1: -1 na [1,u].
// Odgovor se uvećava za broj l s d(l)=0, tj. broj minimuma ako je minimum 0.
#include <bits/stdc++.h>
using namespace std;

int N;
vector<int> mn, cnt, lz;
void build(int x, int l, int r) {
    mn[x] = 0; lz[x] = 0; cnt[x] = r - l + 1;
    if (l == r) return;
    int m = (l + r) / 2; build(2 * x, l, m); build(2 * x + 1, m + 1, r);
}
void apply(int x, int v) { mn[x] += v; lz[x] += v; }
void pull(int x) {
    mn[x] = min(mn[2 * x], mn[2 * x + 1]);
    cnt[x] = (mn[2 * x] == mn[x] ? cnt[2 * x] : 0) + (mn[2 * x + 1] == mn[x] ? cnt[2 * x + 1] : 0);
}
void add(int x, int l, int r, int ql, int qr, int v) {
    if (qr < l || r < ql) return;
    if (ql <= l && r <= qr) { apply(x, v); return; }
    if (lz[x]) { apply(2 * x, lz[x]); apply(2 * x + 1, lz[x]); lz[x] = 0; }
    int m = (l + r) / 2; add(2 * x, l, m, ql, qr, v); add(2 * x + 1, m + 1, r, ql, qr, v);
    pull(x);
}

int main() {
    int T; scanf("%d", &T);
    while (T--) {
        int n; scanf("%d", &n);
        vector<vector<int>> adj(n + 1);
        for (int i = 0; i < n - 1; i++) {
            int a, b; scanf("%d %d", &a, &b);
            adj[a].push_back(b); adj[b].push_back(a);
        }
        N = n; mn.assign(4 * n + 4, 0); cnt.assign(4 * n + 4, 0); lz.assign(4 * n + 4, 0);
        build(1, 1, n);
        long long ans = 0;
        for (int r = 1; r <= n; r++) {
            if (r > 1) add(1, 1, n, 1, r - 1, 1);          // r-l raste za sve l < r
            for (int u : adj[r]) if (u < r) add(1, 1, n, 1, u, -1);   // novi brid u [l,r] za l <= u
            // pozicije l > r nisu dirane i imaju d = 0, pa ih izuzmemo iz broja nula
            if (mn[1] == 0) ans += cnt[1] - (n - r);
        }
        printf("%lld\n", ans);
    }
    return 0;
}
