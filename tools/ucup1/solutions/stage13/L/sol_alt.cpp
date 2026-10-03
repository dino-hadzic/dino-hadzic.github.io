#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using Int = pair<int, int>;   // zatvoreni interval [l, r] brojeva k

// f[D'] = sortirani disjunktni intervali dostizivih k za razliku D = T - k, D' = D + z.
// Svaki je interval duljine barem o + 1 (izbor jedinica), a svi pocetci leze u rasponu
// duljine <= min(z + r, S - o) <= 4o, pa je intervala po indeksu najvise 4.
static vector<vector<Int>> f;

// f[i] |= (f[j] pomaknut za +w po k)
static void spoji(int i, int j, int w) {
    const vector<Int>& src = f[j];
    if (src.empty()) return;
    vector<Int>& dst = f[i];
    vector<Int> g;
    g.reserve(dst.size() + src.size());
    size_t p = 0, q = 0;
    auto gurni = [&](Int x) {
        if (!g.empty() && g.back().second + 1 >= x.first) g.back().second = max(g.back().second, x.second);
        else g.push_back(x);
    };
    while (p < dst.size() || q < src.size()) {
        if (q == src.size() || (p < dst.size() && dst[p].first <= src[q].first + w)) gurni(dst[p++]);
        else { gurni({src[q].first + w, src[q].second + w}); ++q; }
    }
    dst.swap(g);
}

int main() {
    int n, S;
    if (scanf("%d %d", &n, &S) != 2) return 0;
    vector<int> cnt(S + 1, 0);
    for (int i = 0; i < n; ++i) {
        int x; if (scanf("%d", &x) != 1) return 0;
        ++cnt[x];
    }
    int z = cnt[0], o = cnt[1];
    ll B = 0;
    for (int v = 2; v <= S; ++v) B += (ll)(v - 1) * cnt[v];
    int M = z + (int)B;            // D' = D + z in [0, z + B]
    f.assign(M + 1, {});
    // samo nule i jedinice: z' nula i j jedinica daje D = -z', k in [z', z' + o]
    for (int zp = 0; zp <= z; ++zp) f[z - zp].push_back({zp, zp + o});
    // veliki elementi v >= 2: jedan primjerak pomice D za v - 1 i k za 1; brojnost cijepamo binarno
    for (int v = 2; v <= S; ++v) {
        int m = cnt[v];
        for (int t = 1; m > 0; t <<= 1) {
            int k = min(t, m); m -= k;
            int d = (v - 1) * k;                 // pomak po D
            for (int i = M; i >= d; --i) spoji(i, i - d, k);
        }
    }
    ll ans = 0;
    for (int i = 0; i <= M; ++i)
        for (auto [l, r] : f[i]) ans += r - l + 1;
    printf("%lld\n", ans);
    return 0;
}
