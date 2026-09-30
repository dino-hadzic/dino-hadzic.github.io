// A. Moniphantov san
// Stanje jednog Moniphanta: razina L i najmanja ljuta razina m (ili nema, ⊥);
// nakon 4. operacije ostaje samo m, pa je (L, m) dovoljno. Sve operacije su
// invarijantne na pomak, a "umiru" (gube m) točno elementi s delta = L-m < K,
// pri čemu su svi ikad umrli elementi uvijek u istom relativnom stanju.
// Zato se kompozicija bilo kojeg niza operacija zapisuje kao oznaka s tri
// grane (⊥ / delta<K / delta>=K) i lijeno propagira u segmentnom stablu.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const ll NONE = LLONG_MIN;   // nema ljutog Mofunfuna

struct Tag {
    // ⊥ elementi:               L' = L + a,  m' = bm ? L + b : ⊥
    // živi s delta < K:          L' = L + c,  m' = bd ? L + d : ⊥
    // živi s delta >= K:  op4=0: L' = L + e,  m' = m
    //                     op4=1: L' = m + e,  m' = bf ? m + f : ⊥
    ll a = 0, b = 0, c = 0, d = 0, e = 0, f = 0, K = 0;
    bool bm = false, bd = false, op4 = false, bf = false;
    bool empty() const { return !bm && K == 0 && !op4 && a == 0 && e == 0; }
};

// primjena oznake na simboličko stanje (off, has, moff) relativno prema nekoj bazi B:
// L = B + off, m = has ? B + moff : ⊥.  Vraća novo simboličko stanje relativno prema B.
static void sym_apply(const Tag& t, ll& off, bool& has, ll& moff) {
    if (!has) { ll L = off; off = L + t.a; has = t.bm; moff = L + t.b; return; }
    ll delta = off - moff;
    if (delta < t.K) { ll L = off; off = L + t.c; has = t.bd; moff = L + t.d; }
    else if (!t.op4) { off = off + t.e; }
    else { ll m = moff; off = m + t.e; has = t.bf; moff = m + t.f; }
}

// kompozicija: prvo t1, zatim t2
static Tag compose(const Tag& t1, const Tag& t2) {
    Tag r;
    // grana ⊥
    { ll off = t1.a; bool has = t1.bm; ll moff = t1.b; sym_apply(t2, off, has, moff); r.a = off; r.bm = has; r.b = moff; }
    if (t1.op4) {
        // preživjeli t1 su svi u istom stanju relativno prema m
        r.K = t1.K;
        if (t1.K > 0) { ll off = t1.c; bool has = t1.bd; ll moff = t1.d; sym_apply(t2, off, has, moff); r.c = off; r.bd = has; r.d = moff; }
        ll off = t1.e; bool has = t1.bf; ll moff = t1.f; sym_apply(t2, off, has, moff);
        r.op4 = true; r.e = off; r.bf = has; r.f = moff;
    } else {
        // preživjeli t1: (L + e1, m), delta' = delta + e1; u t2 umiru oni s delta + e1 < K2
        ll K2 = t2.K - t1.e;
        r.K = max(t1.K, K2);
        if (K2 > t1.K) {          // mrtvi iz t2 (svi ikad umrli dijele stanje)
            r.c = t1.e + t2.c; r.bd = t2.bd; r.d = t1.e + t2.d;
        } else if (t1.K > 0) {    // mrtvi iz t1 provučeni kroz t2
            ll off = t1.c; bool has = t1.bd; ll moff = t1.d; sym_apply(t2, off, has, moff); r.c = off; r.bd = has; r.d = moff;
        }
        if (!t2.op4) { r.op4 = false; r.e = t1.e + t2.e; }
        else { r.op4 = true; r.e = t2.e; r.bf = t2.bf; r.f = t2.f; }
    }
    return r;
}

int n, q;
vector<Tag> tag;

void apply_range(int node, int lo, int hi, int l, int r, const Tag& t) {
    if (r < lo || hi < l) return;
    if (l <= lo && hi <= r) { tag[node] = compose(tag[node], t); return; }
    if (!tag[node].empty()) {              // spusti oznaku djeci
        tag[2 * node] = compose(tag[2 * node], tag[node]);
        tag[2 * node + 1] = compose(tag[2 * node + 1], tag[node]);
        tag[node] = Tag();
    }
    int mid = (lo + hi) / 2;
    apply_range(2 * node, lo, mid, l, r, t);
    apply_range(2 * node + 1, mid + 1, hi, l, r, t);
}

ll query(int node, int lo, int hi, int pos) {
    // oznake od lista prema korijenu primjenjujemo redom (dublje = ranije)
    ll off = 500000; bool has = false; ll moff = 0;
    vector<const Tag*> path;
    while (true) {
        path.push_back(&tag[node]);
        if (lo == hi) break;
        int mid = (lo + hi) / 2;
        if (pos <= mid) { node = 2 * node; hi = mid; } else { node = 2 * node + 1; lo = mid + 1; }
    }
    for (int i = (int)path.size() - 1; i >= 0; --i) sym_apply(*path[i], off, has, moff);
    return off;
}

int main() {
    scanf("%d %d", &n, &q);
    tag.assign(4 * n + 4, Tag());
    Tag ops[5];
    ops[1].a = 1; ops[1].e = 1;                                  // san
    ops[2].a = -1; ops[2].K = 1; ops[2].c = -1; ops[2].e = -1;   // buđenje: delta = 0 umire
    ops[3].bm = true; ops[3].b = 0;                              // uvreda: ⊥ -> m = L
    ops[4].op4 = true;                                           // odmazda: L = m, ⊥
    string out;
    while (q--) {
        int op, l, r; scanf("%d %d %d", &op, &l, &r);
        if (op == 5) { out += to_string(query(1, 1, n, l)); out += '\n'; }
        else apply_range(1, 1, n, l, r, ops[op]);
    }
    fputs(out.c_str(), stdout);
    return 0;
}
