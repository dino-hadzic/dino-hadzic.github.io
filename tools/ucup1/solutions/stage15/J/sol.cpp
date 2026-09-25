// UCup 1, Stage 15 (ZJCPC 2023), J. Master of Polygon
// Podijeli pa vladaj po x-koordinati. U pojasu [l,r]:
//  * bridovi koji sijeku obje granice („raspinjući”) su međusobno uređeni po y na cijelom pojasu,
//    pa za svaki upit binarnim pretraživanjem usporedimo položaj njegovih krajeva među njima;
//  * raspinjući upit (pravac kroz pojas) protiv ostalih bridova: ostatak ruba unutar pojasa su
//    izlomljene linije s krajevima na granicama. Ako y upita na granici padne u [ymin,ymax]
//    dodira neke linije -> sijeku se; inače linija „iznad” upita siječe pravac točno kada ima
//    vrh na ili ispod pravca -> offline min linearne funkcije po točkama (Li Chao stablo nad
//    nagibima upita). Četiri simetrične varijante (lijevo/desno, iznad/ispod).
//  * ostali parovi idu u djecu [l,mid], [mid,r]; vertikalni brid i vertikalni upit na istom x
//    obrađuju se zasebno.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef __int128 lll;

struct Fr {                       // razlomak n/d, d > 0
    ll n, d;
    Fr(ll n_ = 0, ll d_ = 1) : n(n_), d(d_) { if (d < 0) { n = -n; d = -d; } }
};
inline int cmp(const Fr& a, const Fr& b) { lll x = (lll)a.n * b.d, y = (lll)b.n * a.d; return x < y ? -1 : x > y ? 1 : 0; }
inline bool operator<(const Fr& a, const Fr& b) { return cmp(a, b) < 0; }
inline Fr neg(const Fr& a) { return Fr(-a.n, a.d); }

struct Pt { ll x; Fr y; };
struct Seg { ll x1, y1, x2, y2; };  // uvijek x1 <= x2

Fr yAt(const Seg& s, ll X) {        // y na x = X (nevertikalan segment)
    return Fr(s.y1 * (s.x2 - s.x1) + (s.y2 - s.y1) * (X - s.x1), s.x2 - s.x1);
}

int n, q;
vector<ll> vx, vy;
vector<Seg> edge, qs;
vector<char> ans;

// ----- Li Chao stablo nad diskretiziranim nagibima t = dy/dx (dx > 0) -----
// pravac točke p: g_p(t) = y_p - x_p * t; tražimo min po umetnutim točkama
struct LiChao {
    vector<Fr> ts; vector<int> has; vector<Pt> pt; int znak = 1;   // znak=-1: održava maksimum
    void init(const vector<Fr>& t, int z = 1) { ts = t; znak = z; has.assign(4 * max<size_t>(1, ts.size()), 0); pt.resize(has.size()); }
    // g_p(t) - g_q(t) predznak
    static int razlika(const Pt& p, const Pt& q, const Fr& t) {
        lll a = ((lll)p.y.n * q.y.d - (lll)q.y.n * p.y.d) * t.d;
        lll b = (lll)(p.x - q.x) * t.n * p.y.d * q.y.d;
        lll r = a - b; return r < 0 ? -1 : r > 0 ? 1 : 0;
    }
    void umetni(int nd, int lo, int hi, Pt p) {
        if (!has[nd]) { has[nd] = 1; pt[nd] = p; return; }
        int mid = (lo + hi) / 2;
        if (znak * razlika(p, pt[nd], ts[mid]) < 0) swap(p, pt[nd]);
        if (lo == hi) return;
        if (znak * razlika(p, pt[nd], ts[lo]) < 0) umetni(2 * nd, lo, mid, p);
        else if (znak * razlika(p, pt[nd], ts[hi]) < 0) umetni(2 * nd + 1, mid + 1, hi, p);
    }
    void umetni(const Pt& p) { umetni(1, 0, (int)ts.size() - 1, p); }
    // postoji li umetnuta točka s g_p(t_i) <= g_P(t_i) (za znak=-1: >=)?
    bool upit(int i, const Pt& P) {
        int nd = 1, lo = 0, hi = (int)ts.size() - 1;
        while (true) {
            if (has[nd] && znak * razlika(pt[nd], P, ts[i]) <= 0) return true;
            if (lo == hi) return false;
            int mid = (lo + hi) / 2;
            if (i <= mid) { nd = 2 * nd; hi = mid; } else { nd = 2 * nd + 1; lo = mid + 1; }
        }
    }
} lichao;

struct Piece { vector<Pt> pts; };

// jedna strana: linije s dodirom na granici x = L (nakon transformacije), upiti raspinjući
void strana(const vector<Piece>& pieces, const vector<int>& Qs, ll L, bool negX, bool negY, ll l, ll r) {
    auto tr = [&](const Pt& p) { Pt t; t.x = negX ? -p.x : p.x; t.y = negY ? neg(p.y) : p.y; return t; };
    auto trSeg = [&](const Seg& s) {
        Seg t = s;
        if (negX) { t.x1 = -s.x2; t.y1 = s.y2; t.x2 = -s.x1; t.y2 = s.y1; }
        if (negY) { t.y1 = -t.y1; t.y2 = -t.y2; }
        return t;
    };
    struct Q { int id; Fr yq; Fr t; Seg s; };
    vector<Q> Q_;
    for (int id : Qs) if (!ans[id]) { Seg s = trSeg(qs[id]); Q_.push_back({id, yAt(s, L), Fr(s.y2 - s.y1, s.x2 - s.x1), s}); }
    if (Q_.empty()) return;
    struct Interval { Fr lo, hi; int piece; };
    vector<Interval> iv;
    for (int i = 0; i < (int)pieces.size(); ++i) {
        Pt a = tr(pieces[i].pts.front()), b = tr(pieces[i].pts.back());
        bool ca = a.x == L, cb = b.x == L;
        if (!ca && !cb) continue;
        Fr lo, hi;
        if (ca && cb) { lo = min(a.y, b.y); hi = max(a.y, b.y); }
        else { lo = hi = ca ? a.y : b.y; }
        iv.push_back({lo, hi, i});
    }
    if (iv.empty()) return;
    // 1) pokrivenost: yq unutar nekog [lo,hi]
    sort(iv.begin(), iv.end(), [](const Interval& a, const Interval& b) { return a.lo < b.lo; });
    sort(Q_.begin(), Q_.end(), [](const Q& a, const Q& b) { return a.yq < b.yq; });
    {
        size_t p = 0; bool ima = false; Fr mx;
        for (auto& qq : Q_) {
            while (p < iv.size() && cmp(iv[p].lo, qq.yq) <= 0) { if (!ima || mx < iv[p].hi) { mx = iv[p].hi; ima = true; } ++p; }
            if (ima && cmp(mx, qq.yq) >= 0) ans[qq.id] = 1;
        }
    }
    // 2) linije s dodirom iznad upita: siječe ako neka točka leži na ili ispod pravca
    vector<Fr> ts;
    for (auto& qq : Q_) ts.push_back(qq.t);
    sort(ts.begin(), ts.end());
    ts.erase(unique(ts.begin(), ts.end(), [](const Fr& a, const Fr& b) { return cmp(a, b) == 0; }), ts.end());
    lichao.init(ts);
    int p = (int)iv.size() - 1;                         // intervali po lo silazno
    for (int i = (int)Q_.size() - 1; i >= 0; --i) {
        auto& qq = Q_[i];
        while (p >= 0 && cmp(iv[p].lo, qq.yq) > 0) {
            for (const Pt& pt : pieces[iv[p].piece].pts) lichao.umetni(tr(pt));
            --p;
        }
        if (ans[qq.id]) continue;
        int ti = lower_bound(ts.begin(), ts.end(), qq.t) - ts.begin();
        Pt P; P.x = qq.s.x1; P.y = Fr(qq.s.y1, 1);
        if (lichao.upit(ti, P)) ans[qq.id] = 1;
    }
    (void)l; (void)r;
}

// zatvorena linija (cijeli poligon strogo unutar pojasa): pravac je siječe ako ima vrhova na ili
// ispod I na ili iznad pravca
void zatvorena(const Piece& pc, const vector<int>& Qs) {
    struct Q { int id; Fr t; Seg s; };
    vector<Q> Q_;
    for (int id : Qs) if (!ans[id]) { const Seg& s = qs[id]; Q_.push_back({id, Fr(s.y2 - s.y1, s.x2 - s.x1), s}); }
    if (Q_.empty()) return;
    vector<Fr> ts;
    for (auto& qq : Q_) ts.push_back(qq.t);
    sort(ts.begin(), ts.end());
    ts.erase(unique(ts.begin(), ts.end(), [](const Fr& a, const Fr& b) { return cmp(a, b) == 0; }), ts.end());
    vector<char> ispod(Q_.size(), 0), iznad(Q_.size(), 0);
    for (int prolaz = 0; prolaz < 2; ++prolaz) {
        lichao.init(ts, prolaz ? -1 : 1);
        for (const Pt& p : pc.pts) lichao.umetni(p);
        for (size_t i = 0; i < Q_.size(); ++i) {
            int ti = lower_bound(ts.begin(), ts.end(), Q_[i].t) - ts.begin();
            Pt P; P.x = Q_[i].s.x1; P.y = Fr(Q_[i].s.y1, 1);
            (prolaz ? iznad : ispod)[i] = lichao.upit(ti, P);
        }
    }
    for (size_t i = 0; i < Q_.size(); ++i) if (ispod[i] && iznad[i]) ans[Q_[i].id] = 1;
}

vector<int> mark; int stamp = 0;
inline int nxt(int i) { return i + 1 == n ? 0 : i + 1; }
inline int prv(int i) { return i == 0 ? n - 1 : i - 1; }

void solve(ll l, ll r, vector<int>& E, vector<int>& Q) {
    if (E.empty() || Q.empty()) return;
    vector<int> Es, En, Qs, Qn;
    for (int e : E) (edge[e].x1 <= l && edge[e].x2 >= r ? Es : En).push_back(e);
    for (int id : Q) if (!ans[id]) (qs[id].x1 <= l && qs[id].x2 >= r ? Qs : Qn).push_back(id);
    // --- raspinjući bridovi protiv svih upita ---
    if (!Es.empty()) {
        sort(Es.begin(), Es.end(), [&](int a, int b) {
            int c = cmp(yAt(edge[a], l), yAt(edge[b], l));
            if (c) return c < 0;
            return yAt(edge[a], r) < yAt(edge[b], r);
        });
        auto polozaj = [&](ll X, const Fr& y, bool& dodir) {
            int lo = 0, hi = Es.size();
            while (lo < hi) { int mid = (lo + hi) / 2; if (yAt(edge[Es[mid]], X) < y) lo = mid + 1; else hi = mid; }
            dodir = lo < (int)Es.size() && cmp(yAt(edge[Es[lo]], X), y) == 0;
            return lo;
        };
        for (int id : Q) {
            if (ans[id]) continue;
            const Seg& s = qs[id];
            ll X1, X2; Fr y1, y2;
            if (s.x1 == s.x2) { X1 = X2 = s.x1; y1 = Fr(min(s.y1, s.y2)); y2 = Fr(max(s.y1, s.y2)); }
            else { X1 = max(s.x1, l); X2 = min(s.x2, r); y1 = yAt(s, X1); y2 = yAt(s, X2); }
            bool d1, d2;
            int p1 = polozaj(X1, y1, d1), p2 = polozaj(X2, y2, d2);
            if (d1 || d2 || p1 != p2) ans[id] = 1;
        }
    }
    // --- raspinjući upiti protiv ostalih bridova (izlomljene linije) ---
    if (!Qs.empty() && !En.empty()) {
        ++stamp;
        for (int e : En) mark[e] = stamp;
        auto uEn = [&](int e) { return mark[e] == stamp; };
        auto unutra = [&](int v) { return vx[v] > l && vx[v] < r; };
        auto tocka = [&](int e, bool kraj) {
            int a = e, b = nxt(e);            // vrhovi brida e: v[e] -> v[e+1]
            ll ax = vx[a], ay = vy[a], bx = vx[b], by = vy[b];
            ll X = kraj ? bx : ax, Y = kraj ? by : ay;
            Pt p; p.x = X; p.y = Fr(Y);
            if (ax != bx && (X < l || X > r)) { p.x = X < l ? l : r; p.y = yAt(edge[e], p.x); }
            return p;
        };
        vector<Piece> pieces;
        vector<char> posjecen(En.size(), 0);
        sort(En.begin(), En.end());
        auto idx = [&](int e) { return lower_bound(En.begin(), En.end(), e) - En.begin(); };
        auto pocetak = [&](int e) { return !(uEn(prv(e)) && unutra(e)); };
        bool imaPocetak = false;
        for (int e : En) if (pocetak(e)) { imaPocetak = true; break; }
        for (size_t k = 0; k < En.size(); ++k) {
            int e = En[k];
            if (posjecen[k] || (imaPocetak && !pocetak(e))) continue;
            Piece pc; pc.pts.push_back(tocka(e, false));
            int j = e;
            while (true) {
                posjecen[idx(j)] = 1;
                pc.pts.push_back(tocka(j, true));
                int nj = nxt(j);
                if (!uEn(nj) || !unutra(nj) || posjecen[idx(nj)]) break;
                j = nj;
            }
            pieces.push_back(move(pc));
        }
        if (!imaPocetak) { for (auto& pc : pieces) zatvorena(pc, Qs); }
        strana(pieces, Qs, l, false, false, l, r);
        strana(pieces, Qs, l, false, true, l, r);
        strana(pieces, Qs, -r, true, false, l, r);
        strana(pieces, Qs, -r, true, true, l, r);
    }
    if (r - l <= 1) return;
    ll mid = (l + r) / 2;
    vector<int> E1, E2, Q1, Q2;
    for (int e : En) { if (edge[e].x1 <= mid) E1.push_back(e); if (edge[e].x2 >= mid) E2.push_back(e); }
    for (int id : Qn) if (!ans[id]) { if (qs[id].x1 <= mid) Q1.push_back(id); if (qs[id].x2 >= mid) Q2.push_back(id); }
    vector<int>().swap(Es); vector<int>().swap(Qs); vector<int>().swap(En); vector<int>().swap(Qn);
    solve(l, mid, E1, Q1);
    solve(mid, r, E2, Q2);
}

int main() {
    scanf("%d %d", &n, &q);
    vx.resize(n); vy.resize(n);
    for (int i = 0; i < n; ++i) scanf("%lld %lld", &vx[i], &vy[i]);
    edge.resize(n);
    for (int i = 0; i < n; ++i) {
        int j = nxt(i);
        edge[i] = { vx[i], vy[i], vx[j], vy[j] };
        if (edge[i].x1 > edge[i].x2) swap(edge[i].x1, edge[i].x2), swap(edge[i].y1, edge[i].y2);
    }
    qs.resize(q); ans.assign(q, 0);
    for (int i = 0; i < q; ++i) {
        scanf("%lld %lld %lld %lld", &qs[i].x1, &qs[i].y1, &qs[i].x2, &qs[i].y2);
        if (qs[i].x1 > qs[i].x2) swap(qs[i].x1, qs[i].x2), swap(qs[i].y1, qs[i].y2);
    }
    // vertikalni bridovi protiv vertikalnih upita na istom x
    {
        map<ll, vector<pair<ll, ll>>> vert;
        for (int i = 0; i < n; ++i) if (edge[i].x1 == edge[i].x2) vert[edge[i].x1].push_back({min(edge[i].y1, edge[i].y2), max(edge[i].y1, edge[i].y2)});
        for (auto& kv : vert) sort(kv.second.begin(), kv.second.end());
        for (int i = 0; i < q; ++i) if (qs[i].x1 == qs[i].x2) {
            auto it = vert.find(qs[i].x1);
            if (it == vert.end()) continue;
            ll lo = min(qs[i].y1, qs[i].y2), hi = max(qs[i].y1, qs[i].y2);
            auto& v = it->second;
            // prvi interval s gornjim krajem >= lo (intervali su disjunktni i sortirani)
            int a = 0, b = v.size();
            while (a < b) { int m = (a + b) / 2; if (v[m].second < lo) a = m + 1; else b = m; }
            if (a < (int)v.size() && v[a].first <= hi) ans[i] = 1;
        }
    }
    // pojas proširimo za 1 sa svake strane da jedinični pojasi uz rub poligona postoje
    ll xl = *min_element(vx.begin(), vx.end()) - 1, xr = *max_element(vx.begin(), vx.end()) + 1;
    mark.assign(n, 0);
    vector<int> E(n), Q;
    iota(E.begin(), E.end(), 0);
    for (int i = 0; i < q; ++i) if (!ans[i] && qs[i].x2 >= xl && qs[i].x1 <= xr) Q.push_back(i);
    solve(xl, xr, E, Q);
    string out;
    for (int i = 0; i < q; ++i) out += ans[i] ? "YES\n" : "NO\n";
    fputs(out.c_str(), stdout);
    return 0;
}
