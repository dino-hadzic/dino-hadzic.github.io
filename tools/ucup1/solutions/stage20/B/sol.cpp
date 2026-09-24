// UCup 1, Stage 20 (India), B. Minimize Median
// 1) Binarna pretraga po odgovoru x: medijan <= x  <=>  barem k+1 = (N+1)/2 elemenata <= x.
//    Jeftinije je spustati manje elemente (potrebni djelitelj raste s A_i), pa gledamo
//    k+1 najmanjih. Da bi A_i pao na <= x, ukupni umnozak djelitelja mora biti
//    y_i >= floor(A_i/(x+1)) + 1, jer floor(floor(A/a)/b) = floor(A/(ab)).
// 2) f(y) = najmanja cijena da umnozak djelitelja bude tocno y (sito, O(M log M)),
//    racunamo do 2M+2 jer se moze isplatiti "preskociti" M (npr. 2*2 > M).
//    Zatim F(y) = min_{y' >= y} f(y') (dijeljenje vecim brojem nikad ne skodi).
//    Uz cost zamijenjen sufiksnim minimumom dovoljni su umnosci <= 2M+2 (vidi editorijal).
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll INF = (ll)4e18;

int main() {
    int t;
    scanf("%d", &t);
    while (t--) {
        int n, m;
        ll K;
        scanf("%d %d %lld", &n, &m, &K);
        vector<ll> a(n);
        for (auto& x : a) scanf("%lld", &x);
        vector<ll> cost(m + 1);
        for (int i = 1; i <= m; i++) scanf("%lld", &cost[i]);
        for (int i = m - 1; i >= 1; i--) cost[i] = min(cost[i], cost[i + 1]);   // veci djelitelj nije losiji

        int L = 2 * m + 2;
        vector<ll> f(L + 1, INF);
        f[1] = 0;                                   // "dijeljenje s 1" = bez poteza
        for (int y = 2; y <= m; y++) f[y] = cost[y];
        for (int y = 2; y <= L; y++) {              // f[y] je konacan kad dodjemo do y
            if (f[y] >= INF) continue;
            for (int d = 2; d <= m && (ll)y * d <= L; d++)
                f[y * d] = min(f[y * d], f[y] + cost[d]);
        }
        for (int y = L - 1; y >= 1; y--) f[y] = min(f[y], f[y + 1]);   // F = sufiksni minimum

        sort(a.begin(), a.end());
        int k = n / 2;                              // treba k+1 elemenata <= x
        auto moguce = [&](ll x) {
            ll uk = 0;
            for (int i = 0; i <= k; i++) {
                ll y = a[i] / (x + 1) + 1;          // najmanji dovoljan umnozak
                if (y > L) return false;
                uk += f[y];
                if (uk > K) return false;
            }
            return true;
        };
        ll lo = 0, hi = a[k];                       // hi je uvijek moguc (bez poteza)
        while (lo < hi) {
            ll mid = (lo + hi) / 2;
            if (moguce(mid)) hi = mid; else lo = mid + 1;
        }
        printf("%lld\n", lo);
    }
    return 0;
}
