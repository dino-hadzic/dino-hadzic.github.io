// UCup 1, Stage 11 (EC-Final 2022), K. Magic
// Granica na poziciji x (između a_{x-1} i a_x) "vidljiva" je točno kad je interval čiji je x krajnja točka
// izveden nakon svih intervala koji strogo sadrže x. Za intervale koji se križaju, l_a < l_b < r_a < r_b,
// ne mogu biti vidljivi i r_a i l_b (zahtijevali bi b prije a i a prije b); sve ostale kombinacije su
// dopustive i skup bez takvih parova uvijek je ostvariv (graf ograničenja je acikličan).
// Odgovor = najveći neovisan skup bipartitnog grafa (desni krajevi vs. lijevi krajevi) = 2n - najveće sparivanje.
// Sparivanje: Kuhnov algoritam; susjede desnog kraja r_a tražimo segmentnim stablom nad intervalima
// sortiranima po l (raspon l_b u (l_a, r_a), uvjet r_b > r_a), pa nema eksplicitne liste bridova
// (memorijsko ograničenje 16 MB). Složenost O(n^2 log n).
#include <bits/stdc++.h>
using namespace std;

int n;
vector<int> L, R, ord, rankL, seg, matchOf;   // matchOf[b] = a spojen s b (b = lijevi kraj, a = desni kraj)
int sz;

void build() {
    for (int i = 0; i < sz; i++) seg[sz + i] = (i < n) ? R[ord[i]] : -1;
    for (int i = sz - 1; i >= 1; i--) seg[i] = max(seg[2 * i], seg[2 * i + 1]);
}
void remove(int pos) {
    int i = sz + pos; seg[i] = -1;
    for (i >>= 1; i >= 1; i >>= 1) seg[i] = max(seg[2 * i], seg[2 * i + 1]);
}
// bilo koja pozicija u [lo, hi] s vrijednošću > val, ili -1
int find(int node, int nl, int nr, int lo, int hi, int val) {
    if (nr < lo || hi < nl || seg[node] <= val) return -1;
    if (nl == nr) return nl;
    int mid = (nl + nr) / 2;
    int res = find(2 * node, nl, mid, lo, hi, val);
    if (res < 0) res = find(2 * node + 1, mid + 1, nr, lo, hi, val);
    return res;
}

bool dfs(int a) {
    // susjedi: b s l_a < l_b < r_a i r_b > r_a  ->  pozicije u sortiranom poretku po l
    int lo = rankL[a] + 1;
    int hi = int(lower_bound(ord.begin(), ord.end(), R[a], [&](int idx, int v) { return L[idx] < v; }) - ord.begin()) - 1;
    while (true) {
        int pos = find(1, 0, sz - 1, lo, hi, R[a]);
        if (pos < 0) return false;
        remove(pos);                                  // posjećen u ovoj fazi
        int b = ord[pos];
        if (matchOf[b] < 0 || dfs(matchOf[b])) { matchOf[b] = a; return true; }
    }
}

int main() {
    scanf("%d", &n);
    L.resize(n); R.resize(n);
    for (int i = 0; i < n; i++) scanf("%d %d", &L[i], &R[i]);
    ord.resize(n); iota(ord.begin(), ord.end(), 0);
    sort(ord.begin(), ord.end(), [&](int x, int y) { return L[x] < L[y]; });
    rankL.resize(n);
    for (int i = 0; i < n; i++) rankL[ord[i]] = i;
    sz = 1; while (sz < n) sz <<= 1;
    seg.assign(2 * sz, -1);
    matchOf.assign(n, -1);

    int matching = 0;
    for (int a = 0; a < n; a++) {
        build();
        if (dfs(a)) matching++;
    }
    printf("%d\n", 2 * n - matching);
    return 0;
}
