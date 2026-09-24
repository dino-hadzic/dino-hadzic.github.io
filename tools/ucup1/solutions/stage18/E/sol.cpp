// E - Not Another Linear Algebra Problem
// AB = A  <=>  A(B - I) = 0  <=>  svaki redak matrice A lezi u lijevoj jezgri od B - I,
// pa je f(B) = q^{n*k}, gdje je k = dim ker(B - I) (dimenzija prostora fiksnih vektora od B).
// Trazimo dakle  sum_{k=0}^{n} N_k * 3^{q^{n k}},  gdje je N_k broj matrica B u GL_n(F_q)
// s tocno k-dimenzionalnim prostorom fiksnih vektora.
//
// Brojanje N_k: za fiksni k-dimenzionalni potprostor W broj B iz GL_n koje fiksiraju W po tockama
// jednak je q^{k(n-k)} |GL_{n-k}|, a takvih potprostora ima [n k]_q, pa je
//     sum_B [dimFix(B) k]_q = |GL_n| / |GL_k|.
// q-binomna inverzija daje
//     N_k = (|GL_n| / |GL_k|) * U_k,   U_k = sum_{i=0}^{n-k} q^{-k i} / (q;q)_i,
// gdje je (q;q)_i = prod_{j=1}^{i} (1 - q^j).  Sve U_k racunamo u O(n) rekurzijom
//     U_k = ( U_{k-1} - q^{-k(n-k+1)} / (q;q)_{n-k+1} ) / (1 - q^{-k}),
// koja slijedi iz identiteta E(qx) = (1-x) E(x) za E(x) = sum x^i/(q;q)_i, primijenjenog
// na odrezane sume.
//
// Pretpostavka (kao i u sluzbenim rjesenjima): q^j != 1 (mod p) za 1 <= j <= n, tj. red od q
// modulo p veci je od n, pa svi (q^j - 1) imaju inverz.
#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;
typedef long long ll;

static ull P;

static inline ull mul(ull a, ull b) { return a * b % P; }
static inline ull add(ull a, ull b) { a += b; return a >= P ? a - P : a; }
static inline ull sub(ull a, ull b) { return a >= b ? a - b : a + P - b; }
static ull pw(ull b, ull e, ull m) {
    ull r = 1 % m;
    b %= m;
    while (e) {
        if (e & 1) r = (unsigned __int128)r * b % m;
        b = (unsigned __int128)b * b % m;
        e >>= 1;
    }
    return r;
}

int main() {
    ll n, q, p;
    if (scanf("%lld %lld %lld", &n, &q, &p) != 3) return 0;
    P = p;
    ull qq = q % P;
    ull qinv = pw(qq, P - 2, P);

    // qk[i] = q^i, tez[i] = 1 / (q^i - 1) (za i >= 1), a[i] = 1 / (q;q)_i.
    vector<ull> qk(n + 2), tez(n + 2), a(n + 2);
    qk[0] = 1;
    for (ll i = 1; i <= n + 1; i++) qk[i] = mul(qk[i - 1], qq);

    // Skupni inverz svih (q^i - 1), i = 1..n+1, te svih (q;q)_i.
    {
        vector<ull> pre(n + 2);
        pre[0] = 1;
        for (ll i = 1; i <= n + 1; i++) pre[i] = mul(pre[i - 1], sub(qk[i], 1));
        ull inv = pw(pre[n + 1], P - 2, P);
        for (ll i = n + 1; i >= 1; i--) {
            tez[i] = mul(inv, pre[i - 1]);       // 1/(q^i - 1)
            inv = mul(inv, sub(qk[i], 1));
        }
        // (q;q)_i = prod (1 - q^j) = (-1)^i prod (q^j - 1)  =>  a[i] = (-1)^i * prod tez[j]
        a[0] = 1;
        for (ll i = 1; i <= n + 1; i++) {
            a[i] = mul(a[i - 1], tez[i]);
            a[i] = sub(0, a[i]);
        }
    }

    // Tezine w_k = 3^{q^{n k}} mod p.  Eksponent racunamo modulo p-1 (mali Fermatov teorem).
    // 3^e racunamo u O(1) preko dvije tablice (e < 2^30).
    const int B = 15;
    vector<ull> lo(1 << B), hi(1 << B);
    lo[0] = 1;
    for (int i = 1; i < (1 << B); i++) lo[i] = mul(lo[i - 1], 3);
    ull step = mul(lo[(1 << B) - 1], 3);  // 3^{2^B}
    hi[0] = 1;
    for (int i = 1; i < (1 << B); i++) hi[i] = mul(hi[i - 1], step);
    auto pow3 = [&](ull e) { return mul(lo[e & ((1 << B) - 1)], hi[e >> B]); };

    ull M1 = P - 1;
    ull r = pw(q % M1, (ull)n, M1);  // q^n mod (p-1)
    ull rk = 1 % M1;                  // q^{n k} mod (p-1)

    // U_0 = sum_{i=0}^{n} a[i].
    ull U = 0;
    for (ll i = 0; i <= n; i++) U = add(U, a[i]);

    // ratio = |GL_n| / |GL_k| = q^{C(n,2) - C(k,2)} * prod_{i=k+1}^{n} (q^i - 1);
    // krenemo od k = 0 (|GL_n|) i dijelimo dok k raste.
    ull ratio = pw(qq, (ull)n * (n - 1) / 2, P);
    for (ll i = 1; i <= n; i++) ratio = mul(ratio, sub(qk[i], 1));

    ull ans = 0;
    // qe = q^{-k(n-k+1)}, z = q^{-(n-2k+2)} (razlika uzastopnih eksponenata k(n-k+1)).
    ull qe = 1;
    ull z = pw(qinv, (ull)n, P);   // za k = 1: eksponent n - 2 + 2 = n
    ull q2 = mul(qq, qq);
    ull qinvpow = 1;  // q^{-(k-1)}
    for (ll k = 0; k <= n; k++) {
        if (k > 0) {
            // U_k = (U_{k-1} - a[n-k+1] * q^{-k(n-k+1)}) / (1 - q^{-k}),
            // 1/(1 - q^{-k}) = q^k / (q^k - 1).
            qe = mul(qe, z);
            z = mul(z, q2);
            U = sub(U, mul(a[n - k + 1], qe));
            U = mul(U, mul(qk[k], tez[k]));
            // |GL_k| = |GL_{k-1}| * q^{k-1} * (q^k - 1)
            ratio = mul(ratio, tez[k]);
            ratio = mul(ratio, qinvpow);
            qinvpow = mul(qinvpow, qinv);
            rk = (unsigned __int128)rk * r % M1;
        }
        ull Nk = mul(ratio, U);
        ans = add(ans, mul(Nk, pow3(rk)));
    }
    printf("%llu\n", ans);
    return 0;
}
