// K - Count Arithmetic Progression
// Za fiksnu razliku d, A_1 mora biti u [lo(d), hi(d)],
//   lo(d) = max_i (L_i - i d)  (konveksna, gornja ovojnica pravaca),
//   hi(d) = min_i (R_i - i d)  (konkavna, donja ovojnica pravaca).
// Ovojnice gradimo trikom konveksne ljuske (nagibi su razliciti: -i),
// zatim po komadima na kojima su oba aktivna pravca fiksna zbrajamo
// max(0, hi(d) - lo(d) + 1) po cijelim d aritmetickim nizom.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef __int128 lll;

const ll MOD = 998244353;
const ll INF = (ll)4e18;

struct Line { ll a, b; };  // y = a*d + b

// floor(p/q) za q > 0
ll floordiv(lll p, lll q) {
    lll r = p / q;
    if ((p % q != 0) && ((p < 0) != (q < 0))) r--;
    return (ll)r;
}
ll ceildiv(lll p, lll q) { return -floordiv(-p, q); }

// gornja ovojnica (max) pravaca s razlicitim nagibima;
// vraca komade (s, e, pravac) koji pokrivaju sve cijele d, s <= e
vector<tuple<ll, ll, Line>> upperEnvelope(vector<Line> ls) {
    sort(ls.begin(), ls.end(), [](const Line &x, const Line &y) { return x.a < y.a; });
    vector<Line> h;
    for (const Line &l3 : ls) {
        while (h.size() >= 2) {
            const Line &l1 = h[h.size() - 2], &l2 = h.back();
            // l2 je nepotreban ako se l1 i l3 sijeku prije (ili tocno gdje) l1 i l2:
            // (b1-b3)/(a3-a1) <= (b1-b2)/(a2-a1)
            if ((lll)(l1.b - l3.b) * (l2.a - l1.a) <= (lll)(l1.b - l2.b) * (l3.a - l1.a)) h.pop_back();
            else break;
        }
        h.push_back(l3);
    }
    vector<tuple<ll, ll, Line>> res;
    ll start = -INF;
    for (size_t k = 0; k < h.size(); k++) {
        ll end = INF;
        if (k + 1 < h.size()) {
            // sjeciste h[k] i h[k+1]: d = (b_k - b_{k+1}) / (a_{k+1} - a_k)
            ll x = ceildiv((lll)h[k].b - h[k + 1].b, (lll)h[k + 1].a - h[k].a);
            end = x - 1;
        }
        if (start <= end) res.push_back({start, end, h[k]});
        start = end + 1;
    }
    return res;
}

int main() {
    int n;
    scanf("%d", &n);
    vector<ll> L(n), R(n);
    for (auto &x : L) scanf("%lld", &x);
    for (auto &x : R) scanf("%lld", &x);
    vector<Line> lo, hiNeg;
    for (int i = 0; i < n; i++) {
        lo.push_back({-(ll)i, L[i]});      // L_i - i d
        hiNeg.push_back({(ll)i, -R[i]});   // -(R_i - i d): min preko max negacije
    }
    auto A = upperEnvelope(lo), B = upperEnvelope(hiNeg);
    // moguce d: iz uvjeta za i = 0 i i = 1
    ll dmin = L[1] - R[0], dmax = R[1] - L[0];
    ll ans = 0;
    size_t p = 0, q = 0;
    ll cur = dmin;
    while (cur <= dmax) {
        while (get<1>(A[p]) < cur) p++;
        while (get<1>(B[q]) < cur) q++;
        ll end = min({dmax, get<1>(A[p]), get<1>(B[q])});
        Line la = get<2>(A[p]), lb = get<2>(B[q]);
        // broj(d) = hi(d) - lo(d) + 1 = (-lb.a - la.a) d + (-lb.b - la.b + 1) = c*d + e
        ll c = -lb.a - la.a, e = -lb.b - la.b + 1;
        // rjesavamo c*d + e >= 1  <=>  c*d >= -e + 1 na [cur, end]
        ll s = cur, t = end;
        if (c == 0) { if (e < 1) s = t + 1; }
        else if (c > 0) s = max(s, ceildiv((lll)1 - e, c));
        else t = min(t, floordiv((lll)e - 1, -c));  // dijeljenje negativnim okrece znak
        if (s <= t) {
            lll cnt = (lll)t - s + 1;
            lll sumd = (lll)(s + t) * cnt / 2;  // suma d po [s,t]
            ll term = (ll)((sumd % MOD + MOD) % MOD) * ((c % MOD + MOD) % MOD) % MOD;
            term = (term + (ll)(cnt % MOD) * ((e % MOD + MOD) % MOD)) % MOD;
            ans = (ans + term) % MOD;
        }
        cur = end + 1;
    }
    printf("%lld\n", ans);
}
