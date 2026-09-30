// UCup 1, Stage 3 (AMPPZ 2022), G. Great Chase
// Igra traje dok se ne sretnu najblizi lijevi i desni policajac; lopov cijelo
// vrijeme trci brzinom v, pa je odgovor v*T. Vrijeme T nalazimo binarnim pretrazivanjem.
#include <bits/stdc++.h>
using namespace std;

int main() {
    int z;
    scanf("%d", &z);
    while (z--) {
        int n;
        long long v;
        scanf("%d %lld", &n, &v);
        vector<long long> lp, lv, rp, rv;      // lijevi (p<0) i desni (p>0) policajci
        for (int i = 0; i < n; ++i) {
            long long p, s;
            scanf("%lld %lld", &p, &s);
            if (p < 0) { lp.push_back(p); lv.push_back(s); }
            else { rp.push_back(p); rv.push_back(s); }
        }
        // u trenutku t lopov je jos slobodan ako je max(lijevi) < min(desni)
        auto slobodan = [&](long double t) {
            long double L = -1e30L, R = 1e30L;
            for (size_t i = 0; i < lp.size(); ++i) L = max(L, (long double)lp[i] + (long double)lv[i] * t);
            for (size_t i = 0; i < rp.size(); ++i) R = min(R, (long double)rp[i] - (long double)rv[i] * t);
            return L < R;
        };
        long double lo = 0, hi = 2e12L;        // sigurno se sretnu do 2e12 (brzine >= 1, razmak <= 2e12)
        for (int it = 0; it < 100; ++it) {
            long double mid = (lo + hi) / 2;
            if (slobodan(mid)) lo = mid; else hi = mid;
        }
        printf("%.9Lf\n", (long double)v * lo);
    }
    return 0;
}
