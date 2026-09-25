// UCup 1, Stage 16, zadatak C: Classical Data Structure Problem
// Niz duljine 2^m (do 2^30) predstavljamo kao slijed "elementarnih segmenata"
// na kojima su svi elementi jednaki. Segmenti su cvorovi treapa poredani po
// poziciji (implicitni treap po duljini). Upit [l, r]: rascijepi treap na
// pozicijama l i r+1 (pri cemu se najvise dva segmenta prepolove -> najvise
// 2 nova cvora po upitu, O(n) cvorova ukupno), lijeno dodaj i na srednji dio,
// pribroji njegov zbroj u x, spoji natrag. Treap odrzava ocekivanu dubinu
// O(log n) -- to je "segmentno stablo koje cijepa na granici upita + rotacije"
// iz sluzbenog rjesenja. Sve racunamo u uint32 (prirodno modulo 2^32, a 2^30 | 2^32).
#include <bits/stdc++.h>
using namespace std;
typedef unsigned int u32;

struct Cvor {
    u32 len, val;       // duljina segmenta i zajednicka vrijednost njegovih elemenata
    u32 sublen, subsum; // ukupna duljina i zbroj (mod 2^32) cijelog podstabla
    u32 lazy, pri;      // lijeni dodatak za djecu, prioritet treapa
    int lc, rc;
};
const int MAXN = 1000005;  // 1 pocetni + najvise 2 nova cvora po upitu
Cvor nd[MAXN];             // 32 B po cvoru, ~32 MB; nd[0] je prazno stablo
int cnt = 0;

static inline u32 citaj() {  // brzo citanje nenegativnog cijelog broja
    int c = getchar_unlocked();
    while (c < '0') c = getchar_unlocked();
    u32 x = 0;
    while (c >= '0') { x = x * 10 + (c - '0'); c = getchar_unlocked(); }
    return x;
}

static u32 rng() {  // xorshift, fiksno sjeme
    static u32 s = 2463534242u;
    s ^= s << 13; s ^= s >> 17; s ^= s << 5;
    return s;
}

static int noviCvor(u32 len, u32 val) {
    int t = ++cnt;
    nd[t] = {len, val, len, len * val, 0, rng(), 0, 0};
    return t;
}

static inline void dodaj(int t, u32 d) {  // svim elementima podstabla t dodaj d
    if (!t) return;
    nd[t].val += d;
    nd[t].subsum += d * nd[t].sublen;
    nd[t].lazy += d;
}

static inline void push(int t) {
    if (nd[t].lazy) {
        dodaj(nd[t].lc, nd[t].lazy);
        dodaj(nd[t].rc, nd[t].lazy);
        nd[t].lazy = 0;
    }
}

static inline void update(int t) {
    const Cvor &L = nd[nd[t].lc], &R = nd[nd[t].rc];
    nd[t].sublen = L.sublen + nd[t].len + R.sublen;
    nd[t].subsum = L.subsum + nd[t].len * nd[t].val + R.subsum;
}

static int merge(int a, int b) {  // svi segmenti od a su ispred segmenata od b
    if (!a) return b;
    if (!b) return a;
    if (nd[a].pri > nd[b].pri) {
        push(a);
        nd[a].rc = merge(nd[a].rc, b);
        update(a);
        return a;
    } else {
        push(b);
        nd[b].lc = merge(a, nd[b].lc);
        update(b);
        return b;
    }
}

// Rascijepi t tako da L pokriva tocno prvih k jedinica duljine, R ostatak.
static void split(int t, u32 k, int& L, int& R) {
    if (!t) { L = R = 0; return; }
    push(t);
    if (nd[nd[t].lc].sublen >= k) {
        split(nd[t].lc, k, L, nd[t].lc);
        update(t);
        R = t;
        return;
    }
    k -= nd[nd[t].lc].sublen;
    if (k < nd[t].len) {
        // granica pada strogo unutar segmenta t: prepolovimo ga na [.., k) i [k, ..)
        int d = noviCvor(nd[t].len - k, nd[t].val);
        nd[t].len = k;
        int desno = nd[t].rc;
        nd[t].rc = 0;
        update(t);
        L = t;
        R = merge(d, desno);  // novi cvor ima svjez slucajan prioritet
        return;
    }
    k -= nd[t].len;
    split(nd[t].rc, k, nd[t].rc, R);
    update(t);
    L = t;
}

int main() {
    int n = (int)citaj(), m = (int)citaj();
    u32 mask = (1u << m) - 1;
    int root = noviCvor(1u << m, 0);
    u32 x = 0;
    for (int i = 1; i <= n; ++i) {
        u32 p = citaj(), q = citaj();
        u32 l = (p + x) & mask, r = (q + x) & mask;  // (p + x) mod 2^m, jer 2^m | 2^32
        if (l > r) swap(l, r);
        int A, B, C;
        split(root, l, A, B);          // A = [0, l), B = [l, 2^m)
        split(B, r - l + 1, B, C);     // B = [l, r], C = (r, 2^m)
        dodaj(B, (u32)i);              // a_j += i za sve j u [l, r]
        x += nd[B].subsum;             // x += suma novih a_j
        root = merge(A, merge(B, C));
    }
    printf("%u\n", x & ((1u << 30) - 1));
    return 0;
}
