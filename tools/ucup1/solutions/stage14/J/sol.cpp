// J. LaLa and Magical Beast Summoning
// Uz X = A+I, Y = A-I, Z = L valjana ćelija je projektivna točka (X:Y:Z) na
// eliptičkoj krivulji Y^2 Z = X^3 + E X Z^2 + V Z^3 nad Z_M, null-stanje je
// neutralni element O = (0:1:0), a Combine(C0, C1) je grupno ODUZIMANJE C0 - C1.
// Lijevo asocirani rezultat upita je zato C_l - (C_{l+1} + ... + C_{r-1}), gdje
// je + grupno zbrajanje (asocijativno) koje čuvamo u segmentnom stablu.
// Gustoća A*I/L^2 = (X^2 - Y^2) / (4 Z^2) ne ovisi o skaliranju reprezentanta.
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;

ll M, E, V;

inline ll md(ll x) { x %= M; if (x < 0) x += M; return x; }
inline ll mul(ll a, ll b) { return (ll)((ull)a * (ull)b % (ull)M); }
ll pw(ll b, ll e) { ll r = 1; b = md(b); while (e) { if (e & 1) r = mul(r, b); b = mul(b, b); e >>= 1; } return r; }

struct Pt { ll X, Y, Z; };          // projektivna točka; Z == 0 <=> O
const Pt O = {0, 1, 0};

Pt neg(Pt p) { return {p.X, md(-p.Y), p.Z}; }

// zbrajanje na krivulji u projektivnim koordinatama (bez dijeljenja)
Pt add(const Pt& p, const Pt& q) {
    if (p.Z == 0) return q;
    if (q.Z == 0) return p;
    ll B0 = mul(p.X, q.Z), B1 = mul(q.X, p.Z);   // x-koordinate skalirane sa Z0 Z1
    ll C0 = mul(p.Y, q.Z), C1 = mul(q.Y, p.Z);   // y-koordinate skalirane sa Z0 Z1
    if (B0 == B1) {
        if (md(C0 + C1) == 0) return O;          // q == -p
        // udvostručenje: lambda = (3x^2 + E) / (2y)
        ll B = md(3 * mul(p.X, p.X) + mul(E, mul(p.Z, p.Z)));
        ll C = mul(2, mul(p.Y, p.Z));
        ll C2 = mul(C, C), C3 = mul(C2, C);
        ll T = md(mul(mul(B, B), p.Z) - 2 * mul(p.X, C2));   // x3 * (C^2 Z)
        Pt r;
        r.X = mul(C, T);
        r.Y = md(mul(B, md(3 * mul(p.X, C2) - mul(mul(B, B), p.Z))) - mul(p.Y, C3));
        r.Z = mul(C3, p.Z);
        return r;
    }
    // opći slučaj: lambda = (y0 - y1) / (x0 - x1) = C / B
    ll B = md(B0 - B1), C = md(C0 - C1), D = mul(p.Z, q.Z);
    ll B2 = mul(B, B), B3 = mul(B2, B);
    ll Ex = md(mul(mul(C, C), D) - mul(B2, md(B0 + B1)));    // x3 * (B^2 D)
    Pt r;
    r.X = mul(B, Ex);
    r.Y = md(mul(C, md(mul(B0, B2) - Ex)) - mul(C0, B3));
    r.Z = mul(B3, D);
    return r;
}

Pt fromCell(ll L, ll A, ll I) {
    if (L == 0) return O;
    return {md(A + I), md(A - I), md(L)};
}

int n;
vector<Pt> seg;

void build(int v, int l, int r, const vector<Pt>& a) {
    if (l == r) { seg[v] = a[l]; return; }
    int m = (l + r) / 2;
    build(2 * v, l, m, a); build(2 * v + 1, m + 1, r, a);
    seg[v] = add(seg[2 * v], seg[2 * v + 1]);
}
void update(int v, int l, int r, int pos, const Pt& val) {
    if (l == r) { seg[v] = val; return; }
    int m = (l + r) / 2;
    if (pos <= m) update(2 * v, l, m, pos, val); else update(2 * v + 1, m + 1, r, pos, val);
    seg[v] = add(seg[2 * v], seg[2 * v + 1]);
}
Pt query(int v, int l, int r, int ql, int qr) {
    if (qr < l || r < ql) return O;
    if (ql <= l && r <= qr) return seg[v];
    int m = (l + r) / 2;
    return add(query(2 * v, l, m, ql, qr), query(2 * v + 1, m + 1, r, ql, qr));
}

int main() {
    scanf("%lld %lld %lld", &M, &E, &V);
    scanf("%d", &n);
    vector<Pt> a(n);
    for (int i = 0; i < n; i++) { ll L, A, I; scanf("%lld %lld %lld", &L, &A, &I); a[i] = fromCell(L, A, I); }
    seg.assign(4 * n + 4, O);
    build(1, 0, n - 1, a);
    int q; scanf("%d", &q);
    string out;
    while (q--) {
        int t; scanf("%d", &t);
        if (t == 1) {
            int i; ll L, A, I; scanf("%d %lld %lld %lld", &i, &L, &A, &I);
            a[i] = fromCell(L, A, I);
            update(1, 0, n - 1, i, a[i]);
        } else {
            int l, r; scanf("%d %d", &l, &r);
            Pt rest = (l + 1 <= r - 1) ? query(1, 0, n - 1, l + 1, r - 1) : O;
            Pt R = add(a[l], neg(rest));            // C_l - (C_{l+1} + ... + C_{r-1})
            if (R.Z == 0) { out += "-1\n"; continue; }
            ll num = md(mul(R.X, R.X) - mul(R.Y, R.Y));
            ll den = mul(4, mul(R.Z, R.Z));
            out += to_string(mul(num, pw(den, M - 2))) + "\n";
        }
    }
    fputs(out.c_str(), stdout);
    return 0;
}
