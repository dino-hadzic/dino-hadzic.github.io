// J - Make Convex Sequence
// T = donja konveksna ljuska tocaka (i, R_i) je najveca konveksna funkcija
// ispod R; niz postoji tocno kada je L_i <= T_i za sve i.
// Usporedbe radimo u cijelim brojevima (bez dijeljenja).
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    int n;
    scanf("%d", &n);
    vector<ll> L(n), R(n);
    for (auto &x : L) scanf("%lld", &x);
    for (auto &x : R) scanf("%lld", &x);
    // Andrewov monotoni lanac za donju ljusku tocaka (i, R_i)
    vector<int> h;
    auto cross = [&](int a, int b, int c) {
        // orijentacija (a,b,c): >0 lijevi zavoj (konveksno za donju ljusku)
        return (ll)(b - a) * (R[c] - R[a]) - (ll)(c - a) * (R[b] - R[a]);
    };
    for (int i = 0; i < n; i++) {
        while (h.size() >= 2 && cross(h[h.size() - 2], h.back(), i) <= 0) h.pop_back();
        h.push_back(i);
    }
    // provjera L_i <= T_i po segmentima ljuske
    bool ok = true;
    for (size_t s = 0; s + 1 < h.size() && ok; s++) {
        int p = h[s], q = h[s + 1];
        for (int i = p; i <= q; i++) {
            // T_i = R_p + (R_q - R_p) * (i - p) / (q - p); mnozimo s (q - p) > 0
            ll lhs = L[i] * (q - p);
            ll rhs = R[p] * (q - p) + (R[q] - R[p]) * (i - p);
            if (lhs > rhs) { ok = false; break; }
        }
    }
    puts(ok ? "Yes" : "No");
}
