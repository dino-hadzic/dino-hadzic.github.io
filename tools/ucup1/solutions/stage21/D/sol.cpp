// D. DS Team Selection 2 – offline: paralelno binarno pretraživanje + segmentno stablo, O((n+q) log q)
// Neka je cnt broj dosadašnjih upita tipa 2 i a_i = b_i + cnt*i. Tip 2 samo uveća cnt.
// Tip 1 (v) postaje b_i = min(b_i, v - cnt*i): pravac u varijabli i s nagibom -cnt.
// Dakle b_i = min(init_i, env(i)), env = donja ovojnica dosad dodanih pravaca. Nagibi su sve
// strmiji, pa je ovojnica stog pravaca; svaki novi pravac postane ovojnica na sufiksu [p, n]
// (range-assign aritmetičkog niza). Pozicija i "umire" u prvom trenutku T_i kad env(i) < init_i;
// T_i za sve i računamo offline paralelnim binarnim pretraživanjem (na svakoj razini gradimo
// ovojnicu pravaca iz intervala vremena i ispitujemo točke rastućim pokazivačem).
// Segmentno stablo čuva: zbroj init živih, broj i zbroj indeksa mrtvih te zbroj env po mrtvima
// (uz lazy assign pravca A + B*i). Upit tipa 3: zbroj živih + zbroj env mrtvih + cnt * sum(i).
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef __int128 lll;

int n, q;
vector<ll> init_;
struct Line { ll v, c; };                     // pravac  v - c*i
vector<Line> lines;                           // pravci upita tipa 1 redom
vector<int> T;                                // vrijeme smrti (indeks pravca) ili K

ll floordiv(ll a, ll b) { ll r = a / b; if ((a % b != 0) && ((a < 0) != (b < 0))) r--; return r; }

// paralelno binarno pretraživanje: I sortiran rastuće po i, T_i ∈ [lo, hi]
void solveT(vector<int> &I, int lo, int hi) {
    if (I.empty()) return;
    if (lo == hi) { for (int i : I) T[i] = lo; return; }
    int mid = (lo + hi) / 2;
    // donja ovojnica pravaca lo..mid (nagibi -c nerastući), upiti rastućim i
    vector<Line> hull;
    auto bad = [&](const Line &a, const Line &b, const Line &c) {
        // b nepotreban ako se a i c sijeku lijevo (ili na mjestu) od sjecišta a i b
        // sjecište(a,b): i = (b.v-a.v)/(b.c-a.c); sjecište(a,c): i = (c.v-a.v)/(c.c-a.c)
        return (lll)(c.v - a.v) * (b.c - a.c) <= (lll)(b.v - a.v) * (c.c - a.c);
    };
    for (int s = lo; s <= mid; s++) {
        Line L = lines[s];
        if (!hull.empty() && hull.back().c == L.c) { if (hull.back().v <= L.v) continue; hull.pop_back(); }
        while (hull.size() >= 2 && bad(hull[hull.size() - 2], hull.back(), L)) hull.pop_back();
        hull.push_back(L);
    }
    vector<int> left, right;
    int ptr = 0;
    for (int i : I) {
        while (ptr + 1 < (int)hull.size() && hull[ptr + 1].v - hull[ptr + 1].c * i <= hull[ptr].v - hull[ptr].c * i) ptr++;
        ll env = hull[ptr].v - hull[ptr].c * i;
        if (env < init_[i]) left.push_back(i); else right.push_back(i);
    }
    solveT(left, lo, mid);
    solveT(right, mid + 1, hi);
}

// segmentno stablo
struct Node { ll sumAlive, cntDead, sumIdxDead, sumEnvDead; ll A, B; bool has; };
vector<Node> tr;
void build(int x, int l, int r) {
    tr[x] = {0, 0, 0, 0, 0, 0, false};
    if (l == r) { tr[x].sumAlive = init_[l]; return; }
    int m = (l + r) / 2; build(2 * x, l, m); build(2 * x + 1, m + 1, r);
    tr[x].sumAlive = tr[2 * x].sumAlive + tr[2 * x + 1].sumAlive;
}
void applyLine(int x, ll A, ll B) {
    tr[x].A = A; tr[x].B = B; tr[x].has = true;
    tr[x].sumEnvDead = A * tr[x].cntDead + B * tr[x].sumIdxDead;
}
void push(int x) {
    if (tr[x].has) { applyLine(2 * x, tr[x].A, tr[x].B); applyLine(2 * x + 1, tr[x].A, tr[x].B); tr[x].has = false; }
}
void pull(int x) {
    tr[x].sumAlive = tr[2 * x].sumAlive + tr[2 * x + 1].sumAlive;
    tr[x].cntDead = tr[2 * x].cntDead + tr[2 * x + 1].cntDead;
    tr[x].sumIdxDead = tr[2 * x].sumIdxDead + tr[2 * x + 1].sumIdxDead;
    tr[x].sumEnvDead = tr[2 * x].sumEnvDead + tr[2 * x + 1].sumEnvDead;
}
void assign(int x, int l, int r, int ql, int qr, ll A, ll B) {
    if (qr < l || r < ql) return;
    if (ql <= l && r <= qr) { applyLine(x, A, B); return; }
    push(x); int m = (l + r) / 2;
    assign(2 * x, l, m, ql, qr, A, B); assign(2 * x + 1, m + 1, r, ql, qr, A, B);
    pull(x);
}
void kill(int x, int l, int r, int p) {
    if (l == r) {
        tr[x].sumAlive = 0; tr[x].cntDead = 1; tr[x].sumIdxDead = l;
        tr[x].sumEnvDead = tr[x].A + tr[x].B * l;   // pravac je već dodijeljen (list čuva svoj pravac)
        return;
    }
    push(x); int m = (l + r) / 2;
    if (p <= m) kill(2 * x, l, m, p); else kill(2 * x + 1, m + 1, r, p);
    pull(x);
}
ll query(int x, int l, int r, int ql, int qr) {
    if (qr < l || r < ql) return 0;
    if (ql <= l && r <= qr) return tr[x].sumAlive + tr[x].sumEnvDead;
    push(x); int m = (l + r) / 2;
    return query(2 * x, l, m, ql, qr) + query(2 * x + 1, m + 1, r, ql, qr);
}

int main() {
    scanf("%d %d", &n, &q);
    init_.assign(n + 1, 0);
    for (int i = 1; i <= n; i++) scanf("%lld", &init_[i]);
    vector<array<ll, 3>> qs(q);
    ll cnt = 0;
    for (auto &Q : qs) {
        int t; scanf("%d", &t); Q[0] = t;
        if (t == 1) { scanf("%lld", &Q[1]); lines.push_back({Q[1], cnt}); }
        else if (t == 2) cnt++;
        else scanf("%lld %lld", &Q[1], &Q[2]);
    }
    int K = lines.size();
    T.assign(n + 1, K);
    vector<int> all(n); iota(all.begin(), all.end(), 1);
    if (K > 0) solveT(all, 0, K);          // T_i = K znači "nikad"
    vector<vector<int>> dieAt(K + 1);
    for (int i = 1; i <= n; i++) dieAt[T[i]].push_back(i);

    tr.assign(4 * n + 4, Node());
    build(1, 1, n);
    vector<array<ll, 3>> st;               // stog ovojnice: (v, c, početak)
    cnt = 0; int s = 0;
    string out;
    for (auto &Q : qs) {
        if (Q[0] == 2) cnt++;
        else if (Q[0] == 1) {
            ll v = Q[1], c = cnt;
            ll p = 1; bool useless = false;
            while (!st.empty()) {
                auto [v2, c2, st2] = st.back();
                if (c == c2) { if (v < v2) { st.pop_back(); continue; } useless = true; break; }
                p = floordiv(v - v2, c - c2) + 1;   // najmanji i s  v - c*i < v2 - c2*i
                if (p <= st2) { st.pop_back(); continue; }
                if (p > n) useless = true;
                break;
            }
            if (st.empty()) p = 1;
            if (!useless) {
                st.push_back({v, c, p});
                assign(1, 1, n, (int)p, n, v, -c);
            }
            for (int i : dieAt[s]) kill(1, 1, n, i);
            s++;
        } else {
            int l = Q[1], r = Q[2];
            ll sumIdx = (ll)(l + r) * (r - l + 1) / 2;
            ll ans = query(1, 1, n, l, r) + cnt * sumIdx;
            out += to_string(ans); out += '\n';
        }
    }
    fputs(out.c_str(), stdout);
    return 0;
}
