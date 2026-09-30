// UCup 1, Stage 17, D - Flower's Land 2
// Brisanje susjednih jednakih znakova je poništavanje para g * g^{-1}.
// Službena konstrukcija: tri slučajne invertibilne 2x2 matrice M_0, M_1, M_2
// modulo 2^61-1; znak s_i na PARNOJ poziciji postaje A_i = M_{s_i}, a na
// NEPARNOJ A_i = M_{s_i}^{-1}. Susjedni jednaki znakovi su uvijek različitog
// pariteta, pa se brišu kao M M^{-1} = I ili M^{-1} M = I. Izbrisiv interval
// zato uvijek daje produkt I; neizbrisiv daje I samo uz zanemarivu
// vjerojatnost (hash u nekomutativnoj grupi).
// Operacija +1 mod 3 rotira znakove 0->1->2->0, pa u čvoru segmentnog stabla
// čuvamo produkt za sva tri pomaka; lijeni pomak samo rotira ta tri produkta.
#include <bits/stdc++.h>
using namespace std;

typedef unsigned long long ull;
const ull MOD = (1ULL << 61) - 1;

inline ull mulm(ull a, ull b) {
    __uint128_t c = (__uint128_t)a * b;
    ull r = (ull)(c & MOD) + (ull)(c >> 61);
    if (r >= MOD) r -= MOD;
    return r;
}
inline ull addm(ull a, ull b) { ull r = a + b; return r >= MOD ? r - MOD : r; }
inline ull subm(ull a, ull b) { return a >= b ? a - b : a + MOD - b; }

struct Mat {
    ull a[4];  // [0 1; 2 3]
};
inline Mat mul(const Mat &x, const Mat &y) {
    Mat r;
    r.a[0] = addm(mulm(x.a[0], y.a[0]), mulm(x.a[1], y.a[2]));
    r.a[1] = addm(mulm(x.a[0], y.a[1]), mulm(x.a[1], y.a[3]));
    r.a[2] = addm(mulm(x.a[2], y.a[0]), mulm(x.a[3], y.a[2]));
    r.a[3] = addm(mulm(x.a[2], y.a[1]), mulm(x.a[3], y.a[3]));
    return r;
}
inline bool isId(const Mat &x) { return x.a[0] == 1 && x.a[1] == 0 && x.a[2] == 0 && x.a[3] == 1; }

ull pw(ull a, ull e) {
    ull r = 1;
    while (e) { if (e & 1) r = mulm(r, a); a = mulm(a, a); e >>= 1; }
    return r;
}
// inverz 2x2 matrice: det^{-1} * [d -b; -c a]
Mat inverse(const Mat &m) {
    ull det = subm(mulm(m.a[0], m.a[3]), mulm(m.a[1], m.a[2]));
    ull id = pw(det, MOD - 2);
    return {{mulm(m.a[3], id), mulm(subm(0, m.a[1]), id), mulm(subm(0, m.a[2]), id), mulm(m.a[0], id)}};
}

const int MAXN = 500005;
int n, q;
char s[MAXN];
Mat M[3], Minv[3];          // M_c i M_c^{-1} za znakove c = 0, 1, 2
Mat tr[1 << 20][3];         // tr[v][k] = produkt segmenta s pomakom k
unsigned char lz[1 << 20];  // lijeni pomak (0,1,2)

void build(int v, int l, int r) {
    lz[v] = 0;
    if (l == r) {
        int c = s[l] - '0';
        // parna pozicija -> M, neparna -> M^{-1}
        for (int k = 0; k < 3; k++) tr[v][k] = (l % 2 == 0) ? M[(c + k) % 3] : Minv[(c + k) % 3];
        return;
    }
    int m = (l + r) / 2;
    build(2 * v, l, m);
    build(2 * v + 1, m + 1, r);
    for (int k = 0; k < 3; k++) tr[v][k] = mul(tr[2 * v][k], tr[2 * v + 1][k]);
}
inline void applyShift(int v, int d) {
    if (d == 0) return;
    // novi produkt s pomakom k = stari s pomakom k+d
    Mat t[3];
    for (int k = 0; k < 3; k++) t[k] = tr[v][(k + d) % 3];
    for (int k = 0; k < 3; k++) tr[v][k] = t[k];
    lz[v] = (lz[v] + d) % 3;
}
inline void push(int v) {
    if (lz[v]) { applyShift(2 * v, lz[v]); applyShift(2 * v + 1, lz[v]); lz[v] = 0; }
}
void update(int v, int l, int r, int ql, int qr) {
    if (qr < l || r < ql) return;
    if (ql <= l && r <= qr) { applyShift(v, 1); return; }
    push(v);
    int m = (l + r) / 2;
    update(2 * v, l, m, ql, qr);
    update(2 * v + 1, m + 1, r, ql, qr);
    for (int k = 0; k < 3; k++) tr[v][k] = mul(tr[2 * v][k], tr[2 * v + 1][k]);
}
Mat query(int v, int l, int r, int ql, int qr) {
    if (ql <= l && r <= qr) return tr[v][0];
    push(v);
    int m = (l + r) / 2;
    if (qr <= m) return query(2 * v, l, m, ql, qr);
    if (ql > m) return query(2 * v + 1, m + 1, r, ql, qr);
    return mul(query(2 * v, l, m, ql, qr), query(2 * v + 1, m + 1, r, ql, qr));
}

int main() {
    mt19937_64 rng(chrono::steady_clock::now().time_since_epoch().count());
    for (int c = 0; c < 3; c++) {
        // slučajna invertibilna matrica (ponavljaj dok determinanta nije 0)
        do {
            for (int t = 0; t < 4; t++) M[c].a[t] = rng() % MOD;
        } while (subm(mulm(M[c].a[0], M[c].a[3]), mulm(M[c].a[1], M[c].a[2])) == 0);
        Minv[c] = inverse(M[c]);
    }
    scanf("%d %d", &n, &q);
    scanf("%s", s + 1);
    build(1, 1, n);
    string out;
    while (q--) {
        int t, l, r;
        scanf("%d %d %d", &t, &l, &r);
        if (t == 1) update(1, 1, n, l, r);
        else out += isId(query(1, 1, n, l, r)) ? "Yes\n" : "No\n";
    }
    fputs(out.c_str(), stdout);
    return 0;
}
