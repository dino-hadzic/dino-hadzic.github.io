// B. Klikni krug
// Objekti: krug (točka + interval vremena), okvir (segment; "kapsula" polumjera r)
// i pokretni krug (po dijelovima linearno gibanje). Dva objekta se sijeku ako
// postoji t u presjeku intervala u kojem je udaljenost njihovih "jezgri" <= 2r.
// Sve provjere svode se na: min_{s in [0,len]} |P + w s|^2 <= R^2 (točka prema
// gibanju po pravcu) i na udaljenost segment-segment; sve u cijelim brojevima
// (skaliranje nazivnikom v-u, __int128), granice uključive.  O(n^2) parova.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef __int128 LL;

struct Pt { LL x, y; };
static Pt operator-(Pt a, Pt b) { return {a.x - b.x, a.y - b.y}; }
static Pt operator+(Pt a, Pt b) { return {a.x + b.x, a.y + b.y}; }
static Pt operator*(Pt a, LL k) { return {a.x * k, a.y * k}; }
static LL dot(Pt a, Pt b) { return a.x * b.x + a.y * b.y; }
static LL cross(Pt a, Pt b) { return a.x * b.y - a.y * b.x; }

// postoji li s u [0,len] s |P + w s|^2 <= R^2 ?
static bool near_origin(Pt P, Pt w, LL len, LL R) {
    LL R2 = R * R;
    if (dot(P, P) <= R2) return true;
    Pt Q = P + w * len;
    if (dot(Q, Q) <= R2) return true;
    LL A = dot(w, w);
    if (A == 0 || len == 0) return false;
    LL B = 2 * dot(P, w);
    if (B >= 0) return false;                 // minimum u s = 0
    if (-B >= 2 * A * len) return false;      // minimum u s = len
    LL C = dot(P, P);                         // C > R2
    return B * B >= 4 * A * (C - R2);         // vrijednost u tjemenu: C - B^2/(4A) <= R2
}

// udaljenost točke P od segmenta AB je <= R ?
static bool point_seg(Pt P, Pt A, Pt B, LL R) { return near_origin(A - P, B - A, 1, R); }

static int sgn(LL v) { return (v > 0) - (v < 0); }
static bool on_seg(Pt P, Pt A, Pt B) {        // P kolinearna s AB i unutar
    return cross(B - A, P - A) == 0 && dot(P - A, P - B) <= 0;
}
static bool seg_intersect(Pt A, Pt B, Pt C, Pt D) {
    int d1 = sgn(cross(B - A, C - A)), d2 = sgn(cross(B - A, D - A));
    int d3 = sgn(cross(D - C, A - C)), d4 = sgn(cross(D - C, B - C));
    if (d1 * d2 < 0 && d3 * d4 < 0) return true;
    return on_seg(C, A, B) || on_seg(D, A, B) || on_seg(A, C, D) || on_seg(B, C, D);
}
// udaljenost segmenata AB i CD je <= R ?  (degenerirani segmenti dopušteni)
static bool seg_seg(Pt A, Pt B, Pt C, Pt D, LL R) {
    if (seg_intersect(A, B, C, D)) return true;
    return point_seg(A, C, D, R) || point_seg(B, C, D, R) || point_seg(C, A, B, R) || point_seg(D, A, B, R);
}

struct Obj {
    int type;          // 0 krug, 1 okvir, 2 pokretni krug
    Pt c;              // krug: središte
    Pt S, T;           // klizač: početak i kraj
    ll u, v;           // klizač: početak i kraj gibanja
    ll lo, hi;         // interval prisutnosti
};

ll r, d;

// položaj pokretnog kruga u trenutku t (t stegnut na [u,v]), pomnožen s D = v-u
static Pt pos_scaled(const Obj& o, ll t) {
    t = max(o.u, min(o.v, t));
    LL D = o.v - o.u;
    return o.S * D + (o.T - o.S) * (LL)(t - o.u);
}

static bool intersects(const Obj& a, const Obj& b) {
    ll lo = max(a.lo, b.lo), hi = min(a.hi, b.hi);
    if (lo > hi) return false;
    if (a.type > b.type) return intersects(b, a);
    LL R = 2 * r;
    if (a.type == 0 && b.type == 0) return dot(a.c - b.c, a.c - b.c) <= R * R;
    if (a.type == 0 && b.type == 1) return point_seg(a.c, b.S, b.T, R);
    if (a.type == 1 && b.type == 1) return seg_seg(a.S, a.T, b.S, b.T, R);
    if (b.type == 2 && a.type != 2) {
        LL D = b.v - b.u;
        Pt P1 = pos_scaled(b, lo), P2 = pos_scaled(b, hi);    // prijeđeni dio putanje u presjeku vremena
        if (a.type == 0) return near_origin(P1 - a.c * D, P2 - P1, 1, R * D);
        return seg_seg(P1, P2, a.S * D, a.T * D, R * D);
    }
    // dva pokretna kruga: podijeli presjek vremena točkama u1,v1,u2,v2
    vector<ll> ts = {lo, hi};
    for (ll t : {a.u, a.v, b.u, b.v}) if (lo < t && t < hi) ts.push_back(t);
    sort(ts.begin(), ts.end()); ts.erase(unique(ts.begin(), ts.end()), ts.end());
    LL D1 = a.v - a.u, D2 = b.v - b.u, D = D1 * D2;
    for (size_t i = 0; i + 1 < ts.size() || (i == 0 && ts.size() == 1); ++i) {
        ll t0 = ts[i], t1 = (i + 1 < ts.size()) ? ts[i + 1] : ts[i];
        Pt P = pos_scaled(a, t0) * D2 - pos_scaled(b, t0) * D1;   // relativni položaj * D
        Pt w = {0, 0};
        if (a.u <= t0 && t0 < a.v) w = w + (a.T - a.S) * D2;       // brzina a * D
        if (b.u <= t0 && t0 < b.v) w = w - (b.T - b.S) * D1;
        if (near_origin(P, w, t1 - t0, R * D)) return true;
        if (ts.size() == 1) break;
    }
    return false;
}

int main() {
    int n;
    scanf("%d %lld %lld", &n, &r, &d);
    vector<Obj> objs;
    for (int i = 0; i < n; ++i) {
        int type; scanf("%d", &type);
        if (type == 1) {
            ll cx, cy, t; scanf("%lld %lld %lld", &cx, &cy, &t);
            Obj o; o.type = 0; o.c = {cx, cy}; o.S = o.T = o.c; o.u = o.v = t; o.lo = t - d; o.hi = t + d;
            objs.push_back(o);
        } else {
            ll sx, sy, tx, ty, u, v; scanf("%lld %lld %lld %lld %lld %lld", &sx, &sy, &tx, &ty, &u, &v);
            Obj f; f.type = 1; f.S = {sx, sy}; f.T = {tx, ty}; f.c = f.S; f.u = u; f.v = v; f.lo = u - d; f.hi = v + d;
            Obj m = f; m.type = 2;
            objs.push_back(f); objs.push_back(m);
        }
    }
    ll ans = 0;
    for (size_t i = 0; i < objs.size(); ++i)
        for (size_t j = i + 1; j < objs.size(); ++j)
            if (intersects(objs[i], objs[j])) ++ans;
    printf("%lld\n", ans);
    return 0;
}
