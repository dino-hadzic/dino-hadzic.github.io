// UCup 1, Stage 13 (Um_nik mod 998244353 Contest), H. Exact Subsequences
// Niz s tocno n razlicitih nepraznih podnizova <-> par (x, y), x + y = n + 2, gcd(x, y) = 1;
// leksikografski poredak = rastuci y. k-ti koprosti y nalazimo binarnim pretrazivanjem
// i ukljucivanjem-iskljucivanjem, a blokove ispisuje Euklidov algoritam.
#include <bits/stdc++.h>
using namespace std;

// Broj brojeva u [1, v] koprostih s brojem cijih su prosti djelitelji u 'prosti'.
long long koprostihDo(long long v, const vector<long long> &prosti) {
    int p = prosti.size();
    long long uk = 0;
    for (int maska = 0; maska < (1 << p); ++maska) {
        long long d = 1;
        int bitova = 0;
        for (int i = 0; i < p; ++i)
            if (maska >> i & 1) { d *= prosti[i]; ++bitova; }
        uk += (bitova % 2 == 0 ? 1 : -1) * (v / d);
    }
    return uk;
}

int main() {
    int t;
    if (scanf("%d", &t) != 1) return 0;
    while (t--) {
        long long n, k;
        scanf("%lld %lld", &n, &k);
        long long N = n + 2;

        // Faktorizacija N u O(sqrt N).
        vector<long long> prosti;
        long long tmp = N;
        for (long long d = 2; d * d <= tmp; ++d)
            if (tmp % d == 0) {
                prosti.push_back(d);
                while (tmp % d == 0) tmp /= d;
            }
        if (tmp > 1) prosti.push_back(tmp);

        // Valjanih nizova ima phi(N) = broj y u [1, N-1] koprostih s N.
        if (koprostihDo(N - 1, prosti) < k) {
            printf("-1\n");
            continue;
        }

        // Najmanji y takav da je u [1, y] barem k koprostih s N.
        long long lo = 1, hi = N - 1;
        while (lo < hi) {
            long long mid = (lo + hi) / 2;
            if (koprostihDo(mid, prosti) >= k) hi = mid;
            else lo = mid + 1;
        }
        long long y = lo, x = N - y;

        // Euklid: x > y  ->  blok nula duljine x / y (ostatak je >= 1 jer su koprosti), osim kad je y = 1.
        vector<long long> blokovi;
        int prvi = (x > y) ? 0 : 1;
        while (!(x == 1 && y == 1)) {
            if (x > y) {
                if (y == 1) { blokovi.push_back(x - 1); x = 1; }
                else { blokovi.push_back(x / y); x %= y; }
            } else {
                if (x == 1) { blokovi.push_back(y - 1); y = 1; }
                else { blokovi.push_back(y / x); y %= x; }
            }
        }
        printf("%d %d\n", (int)blokovi.size(), prvi);
        for (size_t i = 0; i < blokovi.size(); ++i)
            printf("%lld%c", blokovi[i], i + 1 == blokovi.size() ? '\n' : ' ');
    }
    return 0;
}
