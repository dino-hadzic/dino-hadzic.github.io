// UCup 1, Stage 20 (India), J. Talk That Talk
// g_i = Legendreov simbol (i/p) in {-1, 0, 1}, g_0 = 0. Za trojku (i, i+d, i+2d):
//   4 h_i = g_i g_{i+d} + g_{i+d} g_{i+2d} + g_{i+2d} g_i + 1  = 4 ako su sva tri w jednaka, inace 0.
// Zbroj po SVIM i = 1..p-1 (indeksi mod p) racuna se algebarski: sum_i g_i g_{i+d} = -1 (tocno!),
// sum_i g_i g_{i+2d} = -1, sum_i g_{i+d} g_{i+2d} = -1 - g_d g_{2d}   =>  4 total_d = p - 4 - g_d g_{2d}.
// Zatim oduzmemo doprinos "namotanih" i (i + 2d >= p): to su i in [p-2d, p-1]; svi potrebni g-ovi
// zive u prozoru od 4t indeksa (A_{2t-i} = g_{p-i}, A_{2t+i} = g_i), a dvostruka suma po (d, i)
// svodi se na tri sume oblika sum_x A_x * (raspon-suma A) uz prefiksne sume po parnosti indeksa -> O(t).
// Legendreov simbol racunamo Jacobijevim algoritmom (O(log p) 64-bitnih operacija) za i <= 2t.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;

int jacobi(ull a, ull n) {                    // n neparan > 0
    a %= n;
    int r = 1;
    while (a) {
        while ((a & 1) == 0) {
            a >>= 1;
            ull m = n & 7;
            if (m == 3 || m == 5) r = -r;
        }
        swap(a, n);
        if ((a & 3) == 3 && (n & 3) == 3) r = -r;
        a %= n;
    }
    return n == 1 ? r : 0;
}

int main() {
    int T;
    scanf("%d", &T);
    vector<ll> A, P0, P1;                     // A = prozor, P0/P1 prefiksne sume po parnosti indeksa
    while (T--) {
        ll p, t0;
        scanf("%lld %lld", &p, &t0);
        ll tt = min(t0, (p - 2) / 2);          // za d > (p-2)/2 nema trojki (i + 2d <= p - 1 nemoguce)
        if (tt <= 0) { puts("0"); continue; }
        int t = tt;
        int n = 4 * t + 1;                    // indeksi 0..4t (A_{4t} = g_{2t} treba za d = t)
        A.assign(n, 0);
        int gm1 = ((p - 1) / 2) % 2 == 0 ? 1 : -1;   // g_{-1} = (-1)^{(p-1)/2}
        for (int i = 1; i <= 2 * t; i++) {
            int g = jacobi(i, p);
            A[2 * t + i] = g;                 // A_{2t+i} = g_i
            A[2 * t - i] = gm1 * g;           // A_{2t-i} = g_{p-i} = g_{-1} g_i
        }
        A[2 * t] = 0;                         // g_0
        // prefiksne sume: P[k] = sum A_x za x < k, odvojeno po parnosti x
        P0.assign(n + 1, 0); P1.assign(n + 1, 0);
        for (int x = 0; x < n; x++) {
            P0[x + 1] = P0[x] + (x % 2 == 0 ? A[x] : 0);
            P1[x + 1] = P1[x] + (x % 2 == 1 ? A[x] : 0);
        }
        auto suma = [&](int l, int r, int par) -> ll {   // sum A_x, l <= x <= r, x % 2 == par (par < 0: svi)
            if (l > r) return 0;
            if (par < 0) return P0[r + 1] - P0[l] + P1[r + 1] - P1[l];
            return par == 0 ? P0[r + 1] - P0[l] : P1[r + 1] - P1[l];
        };
        // W = sum_{d=1..t} sum_{a=2t-2d}^{2t-1} (A_a A_{a+d} + A_{a+d} A_{a+2d} + A_{a+2d} A_a + 1)
        ll W = (ll)t * (t + 1);                   // clan "+1": po d ima 2d vrijednosti a
        for (int b = 2 * t; b < 4 * t; b++) { // b = a + 2d <= 4t - 1
            if (A[b] == 0) continue;
            // A_a A_{a+2d}: a = b - 2d, d in [1,t], a <= 2t-1, a ≡ b (mod 2)
            W += A[b] * suma(max(0, b - 2 * t), min(2 * t - 1, b - 2), b % 2);
            // A_{a+d} A_{a+2d}: c = a + d, a = 2c - b in [0, 2t-1], d = b - c in [1, t]
            int lo = max(b - t, (b + 1) / 2), hi = min(b - 1, (b + 2 * t - 1) / 2);
            W += A[b] * suma(lo, hi, -1);
        }
        for (int c = 1; c < 4 * t; c++) {      // A_a A_{a+d}: c = a + d, a in [max(0,c-t), min(2t-1, c-1, 2c-2t)]
            if (A[c] == 0) continue;
            int lo = max(0, c - t), hi = min({2 * t - 1, c - 1, 2 * c - 2 * t});
            W += A[c] * suma(lo, hi, -1);
        }
        // 4 * total = sum_d (p - 4 - g_d g_{2d})
        ll total4 = 0;
        for (int d = 1; d <= t; d++) total4 += p - 4 - (ll)A[2 * t + d] * A[2 * t + 2 * d];
        ll ans4 = total4 - W;
        assert(ans4 % 4 == 0);
        printf("%lld\n", ans4 / 4);
    }
    return 0;
}
