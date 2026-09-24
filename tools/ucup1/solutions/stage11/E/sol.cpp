// UCup 1, Stage 11 (EC-Final 2022), E. Map
// Optimalan put: i puta f^{-1} (park -> karta) iz s, hodanje, j puta f (karta -> park) do t.
// Ekvivalentno: hodamo od f^{-i}(s) do f^{-j}(t), ukupno (i + j) k + |f^{-i}(s) - f^{-j}(t)|.
// Sličnost zapisujemo kompleksno: f(z) = A z + b (čuva orijentaciju) ili f(z) = A conj(z) + b.
#include <bits/stdc++.h>
using namespace std;
typedef long double ld;
typedef complex<ld> C;

C rd() { long long x, y; scanf("%lld %lld", &x, &y); return C((ld)x, (ld)y); }
ld cross(C a, C b) { return imag(conj(a) * b); }

int main() {
    int T;
    scanf("%d", &T);
    while (T--) {
        C P[4], M[4];
        for (auto &p : P) p = rd();
        for (auto &m : M) m = rd();
        C s = rd(), t = rd();
        long long k; int n;
        scanf("%lld %d", &k, &n);

        // orijentacija: isti predznak vektorskih produkata -> f(z) = A z + b, inače zrcalna
        bool mirror = (cross(P[1] - P[0], P[2] - P[0]) > 0) != (cross(M[1] - M[0], M[2] - M[0]) > 0);
        C A, b;
        if (!mirror) { A = (P[1] - P[0]) / (M[1] - M[0]); b = P[0] - A * M[0]; }
        else         { A = (P[1] - P[0]) / conj(M[1] - M[0]); b = P[0] - A * conj(M[0]); }
        // inverz: f^{-1}(w) = (w - b) / A, odnosno conj((w - b) / A) u zrcalnom slučaju
        auto finv = [&](C w) { C z = (w - b) / A; return mirror ? conj(z) : z; };

        vector<C> S(n + 1), Tt(n + 1);
        S[0] = s; Tt[0] = t;
        for (int i = 1; i <= n; i++) { S[i] = finv(S[i - 1]); Tt[i] = finv(Tt[i - 1]); }

        ld best = abs(s - t);
        for (int i = 0; i <= n; i++)
            for (int j = 0; i + j <= n; j++)
                best = min(best, (ld)(i + j) * k + abs(S[i] - Tt[j]));
        printf("%.10Lf\n", best);
    }
    return 0;
}
