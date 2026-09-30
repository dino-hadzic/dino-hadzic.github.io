#include <bits/stdc++.h>
using namespace std;
using u32 = unsigned int;
using u64 = unsigned long long;
using u128 = __uint128_t;

// Barrettova redukcija: modul P je poznat tek u vrijeme izvođenja.
struct Barrett {
    u64 b, m;
    Barrett() : b(), m() {}
    explicit Barrett(u64 _b) : b(_b), m(-1ULL / _b) {}
    u32 reduce(u64 x) const {
        u64 q = (u64)((u128(m) * x) >> 64), r = x - q * b;
        return (u32)(r - b * (r >= b));
    }
} BA;

u32 P;
u32 mul(u32 x, u32 y) { return BA.reduce((u64)x * y); }
u32 add(u32 x, u32 y) { u32 r = x + y; return r >= P ? r - P : r; }
u32 sub(u32 x, u32 y) { return x >= y ? x - y : x + P - y; }
u32 pw(u32 b, u64 e) {
    u32 r = 1;
    while (e) { if (e & 1) r = mul(r, b); b = mul(b, b); e >>= 1; }
    return r;
}

// Najmanji primitivni korijen prostog broja P.
u32 primitivniKorijen() {
    u32 phi = P - 1;
    vector<u32> fakt;
    u32 x = phi;
    for (u32 d = 2; (u64)d * d <= x; ++d)
        if (x % d == 0) { fakt.push_back(d); while (x % d == 0) x /= d; }
    if (x > 1) fakt.push_back(x);
    for (u32 g = 2;; ++g) {
        bool ok = true;
        for (u32 f : fakt) if (pw(g, phi / f) == 1) { ok = false; break; }
        if (ok) return g;
    }
}

const int LOG = 15, M = 1 << LOG;   // stupanj H_v je C(v,2) <= 31125 < 32768
u32 omega[M];                        // omega[t] = w^t, w = primitivni korijen reda M
vector<u32> rev(M);

// NTT duljine M (P ≡ 1 mod 2^16, pa korijen reda 2^15 postoji).
void ntt(vector<u32> &a, bool inv) {
    for (int i = 0; i < M; ++i) if (i < (int)rev[i]) swap(a[i], a[rev[i]]);
    for (int len = 2; len <= M; len <<= 1) {
        int korak = M / len;
        for (int i = 0; i < M; i += len)
            for (int j = 0; j < len / 2; ++j) {
                u32 w = omega[inv ? (M - (u64)j * korak) & (M - 1) : (u64)j * korak];
                u32 u = a[i + j], v = mul(a[i + j + len / 2], w);
                a[i + j] = add(u, v);
                a[i + j + len / 2] = sub(u, v);
            }
    }
    if (inv) {
        u32 invM = pw(M % P, P - 2);
        for (auto &x : a) x = mul(x, invM);
    }
}

int main() {
    int N;
    if (scanf("%d %u", &N, &P) != 2) return 0;
    BA = Barrett(P);
    u32 g = primitivniKorijen();
    u32 w = pw(g, (P - 1) / M);
    omega[0] = 1;
    for (int t = 1; t < M; ++t) omega[t] = mul(omega[t - 1], w);
    for (int i = 0; i < M; ++i) rev[i] = (rev[i >> 1] >> 1) | ((i & 1) << (LOG - 1));

    // Inverzi 1..M (P > M jer P ≡ 1 mod 2^16 i P > 2).
    vector<u32> inv(M + 2, 1);
    for (int i = 2; i <= M + 1; ++i) inv[i] = mul(P - (P / i), inv[P % i]);

    // vals[v][j] = H_v(w^j), gdje je H_v(u) = G_v(1-u); G_v(x) = integral po
    // vremenima bridova staze na v vrhova (sva < x) od produkta (1 - max na putu)
    // po svim ne-stablovnim bridovima. Rekurzija po položaju najkasnijeg brida p:
    //   G_v(x) = sum_p int_0^x (1-t)^{p(v-p)-1} G_p(t) G_{v-p}(t) dt.
    vector<vector<u32>> vals(N + 1);
    vals[1].assign(M, 1);
    vector<u32> S(M), koef(M);
    u32 fakt = 1, inv2 = pw(2, P - 2);
    for (int v = 2; v <= N; ++v) {
        fill(S.begin(), S.end(), 0);
        // vrijednosti sum_p u^{p(v-p)-1} H_p(u) H_{v-p}(u) u točkama u = w^j
        for (int p = 1; 2 * p <= v; ++p) {
            int k = p * (v - p) - 1;
            const u32 *A = vals[p].data(), *B = vals[v - p].data();
            bool dvostruko = (2 * p != v);
            for (int j = 0; j < M; ++j) {
                u64 prod = (u64)mul(A[j], B[j]) * omega[((u64)j * k) & (M - 1)];
                u32 r = BA.reduce(prod);
                if (dvostruko) r = add(r, r);
                S[j] = add(S[j], r);
            }
        }
        ntt(S, true);   // koeficijenti od S(u), stupanj C(v,2)-1
        // H_v(u) = Hi(1) - Hi(u), Hi = primitivna funkcija od S
        u32 hi1 = 0;
        fill(koef.begin(), koef.end(), 0);
        int stup = v * (v - 1) / 2;
        for (int kk = 0; kk < stup; ++kk) {
            u32 c = mul(S[kk], inv[kk + 1]);   // koeficijent uz u^{kk+1} u Hi
            hi1 = add(hi1, c);
            koef[kk + 1] = sub(0, c);
        }
        koef[0] = hi1;   // H_v(0) = G_v(1)
        fakt = mul(fakt, v % P);
        printf("%u\n", mul(mul(fakt, inv2), koef[0]));
        ntt(koef, false);
        vals[v] = koef;
    }
    return 0;
}
