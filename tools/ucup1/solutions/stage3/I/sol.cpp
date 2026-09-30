// UCup 1, Stage 3 (AMPPZ 2022), I. Investors
// Svaku operaciju smijemo prosiriti do kraja niza (sufiks), a sufiksne operacije s velikim
// prirastom dijele niz na <= k+1 blokova bez inverzija medu blokovima. Odgovor: podjela na
// K = min(k+1, n) blokova s najmanjim zbrojem inverzija unutar blokova -> DP s
// optimizacijom "podijeli pa vladaj" (cijena bloka zadovoljava nejednakost cetverokuta).
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int n;
vector<int> a;
vector<int> inv;                       // inv[l*(n+1)+r] = broj inverzija u a[l..r], 1-indeksirano
vector<ll> prev_dp, cur_dp;

inline int cost(int l, int r) { return inv[(size_t)l * (n + 1) + r]; }

// cur_dp[i] za i u [lo,hi], optimalni prijelaz p (blok p+1..i) u [optlo, opthi]
void rijesi(int lo, int hi, int optlo, int opthi) {
    if (lo > hi) return;
    int mid = (lo + hi) / 2;
    ll best = LLONG_MAX; int bp = -1;
    for (int p = optlo; p <= min(opthi, mid - 1); ++p) {
        if (prev_dp[p] == LLONG_MAX) continue;
        ll v = prev_dp[p] + cost(p + 1, mid);
        if (v < best) { best = v; bp = p; }
    }
    cur_dp[mid] = best;
    if (bp < 0) bp = optlo;
    rijesi(lo, mid - 1, optlo, bp);
    rijesi(mid + 1, hi, bp, opthi);
}

int main() {
    int z;
    scanf("%d", &z);
    while (z--) {
        int k;
        scanf("%d %d", &n, &k);
        a.assign(n + 1, 0);
        for (int i = 1; i <= n; ++i) scanf("%d", &a[i]);
        int K = min(k + 1, n);                   // broj blokova
        if (K == n) { printf("0\n"); continue; }
        inv.assign((size_t)(n + 1) * (n + 1), 0);
        // inv[l][r] = inv[l][r-1] + #{i u [l, r-1] : a_i > a_r}, brojac ide od r-1 prema dolje
        for (int r = 1; r <= n; ++r) {
            int c = 0;
            for (int l = r - 1; l >= 1; --l) {
                if (a[l] > a[r]) ++c;
                inv[(size_t)l * (n + 1) + r] = inv[(size_t)l * (n + 1) + r - 1] + c;
            }
        }
        prev_dp.assign(n + 1, LLONG_MAX);
        cur_dp.assign(n + 1, LLONG_MAX);
        prev_dp[0] = 0;                          // 0 blokova pokriva prefiks duljine 0
        for (int j = 1; j <= K; ++j) {
            fill(cur_dp.begin(), cur_dp.end(), LLONG_MAX);
            rijesi(j, n, j - 1, n - 1);
            swap(prev_dp, cur_dp);
        }
        printf("%lld\n", prev_dp[n]);
    }
    return 0;
}
