// UCup 1, Stage 19 (NAC 2023), I. Power of Divisors
// Ako je n^f(n) = x, onda je x točna f(n)-ta potencija. Za n >= 2 vrijedi f(n) >= 2,
// pa je f(n) <= 60 (2^60 > 10^18). Za svaki kandidat tau = 1..60 izračunamo cjelobrojni
// tau-ti korijen n od x i provjerimo je li x = n^tau i f(n) = tau; uzmemo najmanji n.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;

// n^e, ali „zasićeno” na LIMIT+1 da nema prelijevanja.
const ull LIMIT = 2000000000000000000ULL;   // 2e18 > 10^18
ull potencija(ull n, int e) {
    ull r = 1;
    for (int i = 0; i < e; ++i) {
        if (r > LIMIT / n) return LIMIT + 1;
        r *= n;
    }
    return r;
}

// Najveći n s n^e <= x (binarno pretraživanje po n).
ull korijen(ull x, int e) {
    ull lo = 1, hi = 2000000000ULL;          // za e >= 2 korijen je < 2e9
    while (lo < hi) {
        ull mid = lo + (hi - lo + 1) / 2;
        if (potencija(mid, e) <= x) lo = mid; else hi = mid - 1;
    }
    return lo;
}

// Broj djelitelja probnim dijeljenjem, O(sqrt n).
ll brojDjelitelja(ull n) {
    ll d = 1;
    for (ull p = 2; p * p <= n; ++p) {
        if (n % p == 0) {
            int e = 0;
            while (n % p == 0) { n /= p; ++e; }
            d *= (e + 1);
        }
    }
    if (n > 1) d *= 2;
    return d;
}

int main() {
    ull x;
    if (scanf("%llu", &x) != 1) return 0;
    if (x == 1) { puts("1"); return 0; }    // 1^f(1) = 1^1 = 1
    ll najbolji = -1;
    for (int tau = 2; tau <= 60; ++tau) {
        ull n = korijen(x, tau);
        if (n < 2 || potencija(n, tau) != x) continue;     // x nije točna tau-ta potencija
        if (brojDjelitelja(n) == tau) {
            if (najbolji == -1 || (ll)n < najbolji) najbolji = n;
        }
    }
    printf("%lld\n", najbolji);
    return 0;
}
