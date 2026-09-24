// E - Five Med Sum
// Sortiramo svih 5N brojeva s oznakom niza. Broj x iz niza t je medijan
// tocno onda kada su dva od preostala cetiri niza dala manji element, a
// dva veci. Prebrojimo to prefiksnim brojacima za svaki od 6 parova nizova.
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 998244353;

int main() {
    int n;
    scanf("%d", &n);
    vector<pair<long long, int>> f;  // (vrijednost, oznaka niza)
    f.reserve(5 * n);
    for (int t = 0; t < 5; t++)
        for (int i = 0; i < n; i++) {
            long long x;
            scanf("%lld", &x);
            f.push_back({x, t});
        }
    // stabilan poredak: jednake vrijednosti dobivaju proizvoljan, ali fiksan
    // redoslijed, medijan (treci po redu) time ne mijenja vrijednost
    sort(f.begin(), f.end());
    long long less[5] = {0, 0, 0, 0, 0};  // koliko je elemenata niza t vec proslo
    long long ans = 0;
    for (int k = 0; k < 5 * n; k++) {
        int t = f[k].second;
        long long cnt = 0;
        // biramo dva niza p<q koja daju manje elemente; ostala dva daju vece
        for (int p = 0; p < 5; p++) {
            if (p == t) continue;
            for (int q = p + 1; q < 5; q++) {
                if (q == t) continue;
                long long term = less[p] % MOD * (less[q] % MOD) % MOD;
                for (int r = 0; r < 5; r++)
                    if (r != t && r != p && r != q) term = term * ((n - less[r]) % MOD) % MOD;
                cnt = (cnt + term) % MOD;
            }
        }
        ans = (ans + f[k].first % MOD * cnt) % MOD;
        less[t]++;
    }
    printf("%lld\n", ans);
}
