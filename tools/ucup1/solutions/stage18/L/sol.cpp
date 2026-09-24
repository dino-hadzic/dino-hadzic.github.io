// UCup 1, Stage 18, L: New Houses
// Neka k ljudi ima susjede (k = 0 ili k >= 2), ostali su izolirani. Sve ljude sa
// susjedima smjestimo u jedan blok, pa treba 2n-k <= m kuća (za k = 0: 2n-1 <= m).
// Za fiksan k najbolje je "susjedima" proglasiti k osoba s najvećim a_i - b_i.
#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    if (scanf("%d", &T) != 1) return 0;
    while (T--) {
        int n;
        long long m;
        if (scanf("%d %lld", &n, &m) != 2) return 0;
        vector<long long> d(n);
        long long base = 0;  // svi izolirani: suma b_i
        for (int i = 0; i < n; i++) {
            long long a, b;
            if (scanf("%lld %lld", &a, &b) != 2) return 0;
            base += b;
            d[i] = a - b;
        }
        sort(d.rbegin(), d.rend());  // silazno
        long long best = LLONG_MIN;
        if (2LL * n - 1 <= m) best = max(best, base);  // k = 0, svi izolirani
        long long pref = 0;
        for (int k = 1; k <= n; k++) {
            pref += d[k - 1];
            if (k >= 2 && 2LL * n - k <= m) best = max(best, base + pref);
        }
        printf("%lld\n", best);
    }
    return 0;
}
