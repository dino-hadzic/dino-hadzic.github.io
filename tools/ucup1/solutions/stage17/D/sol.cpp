// UCup 1, Stage 17, D - Flower's Land 2
// Brisanje susjednih jednakih znakova je redukcija riječi u grupi
// Z2 * Z2 * Z2 (slobodni produkt): svaki znak je involucija (x^2 = 1), a
// reducirana riječ je jedinstvena (sustav je konfluentan). Niz se može
// izbrisati točno kad je produkt jednak jedinici grupe. Grupu "hashiramo"
// slučajnim 2x2 matricama A_c s A_c^2 = I (npr. [[a,b],[c,-a]] s a^2+bc=1)
// modulo 2^61-1: izbrisiv niz uvijek daje I, a neizbrisiv daje I samo uz
// zanemarivu vjerojatnost.
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
const Mat ID = {{1, 0, 0, 1}};
inline bool isId(const Mat &x) { return x.a[0] == 1 && x.a[1] == 0 && x.a[2] == 0 && x.a[3] == 1; }

ull pw(ull a, ull e) {
    ull r = 1;
    while (e) { if (e & 1) r = mulm(r, a); a = mulm(a, a); e >>= 1; }
    return r;
}

const int MAXN = 500005;
int n, q;
char s[MAXN];
Mat gen[3];                 // matrice znakova 0,1,2
Mat tr[1 << 20][3];         // tr[v][k] = produkt segmenta s pomakom k
unsigned char lz[1 << 20];  // lijeni pomak (0,1,2)

void build(int v, int l, int r) {
    lz[v] = 0;
    if (l == r) {
        int c = s[l] - '0';
        for (int k = 0; k < 3; k++) tr[v][k] = gen[(c + k) % 3];
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
        // A = [[a, b], [cc, -a]] s a^2 + b*cc = 1  =>  A^2 = I
        ull a = rng() % MOD, b = rng() % (MOD - 1) + 1;
        ull cc = mulm((1 + MOD - mulm(a, a)) % MOD, pw(b, MOD - 2));
        gen[c] = {{a, b, cc, (MOD - a) % MOD}};
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
