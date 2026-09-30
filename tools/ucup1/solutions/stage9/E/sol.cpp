// UCup 1, Stage 9 (Qingdao 2018), E. Plants vs. Zombies
// Binarno pretraživanje odgovora x: možemo li u m koraka svaku biljku dovesti na obranu >= x?
// Provjera je pohlepna slijeva nadesno: na biljci i (obrana d_i) treba t = ceil((x - d_i)/a_i)
// zalijevanja; prvo dobijemo dolaskom, svako sljedeće košta 2 koraka (i+1 pa natrag) i usput
// zalije biljku i+1. Ukupno 2t - 1 koraka. Ako biljci i ne treba ništa, samo prijeđemo (1 korak).
#include <bits/stdc++.h>
using namespace std;

int n;
long long m;
vector<long long> a;

bool moguce(long long x) {
    vector<long long> d(n + 1, 0);       // trenutna obrana (d[n] je "iza kraja")
    long long koraka = 0;
    for (int i = 0; i < n; i++) {
        if (d[i] >= x) {
            // ako sve iza već zadovoljava, ne moramo dalje; inače korak udesno
            koraka++;
            continue;
        }
        long long t = (x - d[i] + a[i] - 1) / a[i];    // potrebno zalijevanja na i
        koraka += 2 * t - 1;
        if (koraka > m) return false;
        if (i + 1 < n) d[i + 1] += (t - 1) * a[i + 1];  // svaki odlazak udesno zalije i+1
    }
    return true;
}

int main() {
    int T;
    scanf("%d", &T);
    while (T--) {
        scanf("%d %lld", &n, &m);
        a.assign(n, 0);
        for (auto &v : a) scanf("%lld", &v);
        long long lo = 0, hi = 2000000000000000000LL / 2;   // gornja granica: m*max(a) <= 1e17
        while (lo < hi) {
            long long mid = lo + (hi - lo + 1) / 2;
            if (moguce(mid)) lo = mid; else hi = mid - 1;
        }
        printf("%lld\n", lo);
    }
    return 0;
}
