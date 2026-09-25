// H - Expanded Hull
// Broj cjelobrojnih tocaka u K*P je Ehrhartov polinom L(K) stupnja 3
// (P je cjelobrojni politop). Znamo L(0) = 1, a po Ehrhart-Macdonaldovoj
// reciprocnosti L(-1) = -I(1), gdje je I(1) broj strogo unutarnjih tocaka.
// Izracunamo L(1), I(1) i L(2) skeniranjem po stupcima (x,y) uz ravnine
// stranica ljuske (O(N^4) nalazenje ravnina), pa Lagrangeom interpoliramo u K.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const ll MOD = 998244353;

ll power(ll b, ll e) {
    ll r = 1; b %= MOD; if (b < 0) b += MOD;
    while (e) { if (e & 1) r = r * b % MOD; b = b * b % MOD; e >>= 1; }
    return r;
}

struct Plane { ll a, b, c, d; };  // sve tocke zadovoljavaju a x + b y + c z <= d

ll floordiv(ll p, ll q) {  // q > 0
    ll r = p / q;
    if (p % q != 0 && p < 0) r--;
    return r;
}
ll ceildiv(ll p, ll q) { return -floordiv(-p, q); }

int main() {
    int n;
    ll K;
    scanf("%d %lld", &n, &K);
    vector<array<ll, 3>> P(n);
    for (auto &p : P) scanf("%lld %lld %lld", &p[0], &p[1], &p[2]);

    // ravnine stranica: za svaku nekolinearnu trojku provjeri jesu li sve
    // tocke s iste strane; normaliziraj (gcd, orijentacija) i ukloni duplikate
    set<array<ll, 4>> planes;
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++)
            for (int k = j + 1; k < n; k++) {
                ll ux = P[j][0] - P[i][0], uy = P[j][1] - P[i][1], uz = P[j][2] - P[i][2];
                ll vx = P[k][0] - P[i][0], vy = P[k][1] - P[i][1], vz = P[k][2] - P[i][2];
                ll a = uy * vz - uz * vy, b = uz * vx - ux * vz, c = ux * vy - uy * vx;
                if (a == 0 && b == 0 && c == 0) continue;  // kolinearne
                ll d = a * P[i][0] + b * P[i][1] + c * P[i][2];
                bool pos = false, neg = false;
                for (int t = 0; t < n; t++) {
                    ll v = a * P[t][0] + b * P[t][1] + c * P[t][2] - d;
                    if (v > 0) pos = true;
                    if (v < 0) neg = true;
                }
                if (pos && neg) continue;
                if (pos) { a = -a; b = -b; c = -c; d = -d; }
                ll g = __gcd(__gcd(llabs(a), llabs(b)), __gcd(llabs(c), llabs(d)));
                planes.insert({a / g, b / g, c / g, d / g});
            }
    vector<Plane> F;
    for (auto &q : planes) F.push_back({q[0], q[1], q[2], q[3]});

    ll X = 0;
    for (auto &p : P) X = max({X, llabs(p[0]), llabs(p[1]), llabs(p[2])});

    // prebroji tocke u k*P; strict = samo strogo unutarnje
    auto count = [&](ll k, bool strict) {
        ll B = X * k, total = 0;
        for (ll x = -B; x <= B; x++)
            for (ll y = -B; y <= B; y++) {
                ll lo = -B, hi = B;
                bool ok = true;
                for (auto &f : F) {
                    // f.a x + f.b y + f.c z <= k f.d  (odnosno < za strogo)
                    ll rhs = k * f.d - f.a * x - f.b * y;
                    if (strict) rhs -= 1;  // cijeli brojevi: < r  <=>  <= r-1
                    if (f.c == 0) { if (rhs < 0) { ok = false; break; } }
                    else if (f.c > 0) hi = min(hi, floordiv(rhs, f.c));
                    else lo = max(lo, ceildiv(-rhs, -f.c));  // c z <= rhs, c<0
                    if (lo > hi) { ok = false; break; }
                }
                if (ok) total += hi - lo + 1;
            }
        return total;
    };
    // vrijednosti L u tockama -1, 0, 1, 2
    ll xs[4] = {-1, 0, 1, 2};
    ll ys[4] = {-count(1, true), 1, count(1, false), count(2, false)};
    // Lagrangeova interpolacija u K (mod p)
    ll Km = K % MOD, ans = 0;
    for (int i = 0; i < 4; i++) {
        ll num = 1, den = 1;
        for (int j = 0; j < 4; j++) {
            if (i == j) continue;
            num = num * ((Km - xs[j]) % MOD + MOD) % MOD;
            den = den * ((xs[i] - xs[j]) % MOD + MOD) % MOD;
        }
        ll yi = (ys[i] % MOD + MOD) % MOD;
        ans = (ans + yi * num % MOD * power(den, MOD - 2)) % MOD;
    }
    printf("%lld\n", ans);
}
