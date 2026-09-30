// UCup 1, Stage 9 (Qingdao 2018), A. Sequence and Sequence
// Q(n) = sum_{i<=n} Q(P(i)). Abelovom (parcijalnom) sumacijom s težinskim polinomom f i njegovom
// prefiksnom sumom F dobivamo   g(f, n) = F(n) * Q(P(n)) - g(f', P(n)),   f'(x) = F(x(x+1)/2 - 1),
// pa se n svaki put smanji na P(n) ~ sqrt(2n). Nakon 4 koraka n <= ~605 i vrijednosti čitamo iz tablice.
// Polinomi F^{(d)} zadani su vrijednostima u 0..deg i evaluiraju se Lagrangeovom interpolacijom
// u točnoj cjelobrojnoj (velikoj) aritmetici.
#include <bits/stdc++.h>
using namespace std;

#ifndef MAXLEN
#define MAXLEN 2000      // granica ispod koje g(d, n) čitamo iz tablice (za testiranje se može smanjiti)
#endif
const int MAXD = 6;      // dubine 0..5 (dovoljno i s vrlo malom tablicom)
const int TAB = MAXLEN > 70 ? MAXLEN : 70;   // veličina tablica (>= najveći stupanj F^{(d)})

// ---------- jednostavni veliki cijeli brojevi s predznakom, baza 1e9 ----------
struct Big {
    bool neg = false;
    vector<uint32_t> d;                          // little-endian, bez vodećih nula; nula = prazan vektor
    static const uint32_t B = 1000000000u;
    Big() {}
    Big(long long v) { if (v < 0) { neg = true; v = -v; } while (v) { d.push_back(v % B); v /= B; } }
    static Big fromString(const string &s) {
        Big r; int start = 0;
        if (s[0] == '-') { r.neg = true; start = 1; }
        for (int i = (int)s.size(); i > start; i -= 9) {
            int l = max(start, i - 9);
            r.d.push_back(stoul(s.substr(l, i - l)));
        }
        r.trim(); return r;
    }
    void trim() { while (!d.empty() && d.back() == 0) d.pop_back(); if (d.empty()) neg = false; }
    bool isZero() const { return d.empty(); }
    string toString() const {
        if (d.empty()) return "0";
        string s = neg ? "-" : "";
        s += to_string(d.back());
        char buf[16];
        for (int i = (int)d.size() - 2; i >= 0; i--) { snprintf(buf, sizeof buf, "%09u", d[i]); s += buf; }
        return s;
    }
    static int cmpAbs(const Big &a, const Big &b) {
        if (a.d.size() != b.d.size()) return a.d.size() < b.d.size() ? -1 : 1;
        for (int i = (int)a.d.size() - 1; i >= 0; i--) if (a.d[i] != b.d[i]) return a.d[i] < b.d[i] ? -1 : 1;
        return 0;
    }
    static Big addAbs(const Big &a, const Big &b) {
        Big r; uint64_t c = 0;
        for (size_t i = 0; i < max(a.d.size(), b.d.size()) || c; i++) {
            if (i < a.d.size()) c += a.d[i];
            if (i < b.d.size()) c += b.d[i];
            r.d.push_back(c % B); c /= B;
        }
        return r;
    }
    static Big subAbs(const Big &a, const Big &b) {   // |a| >= |b|
        Big r; int64_t c = 0;
        for (size_t i = 0; i < a.d.size(); i++) {
            c += (int64_t)a.d[i] - (i < b.d.size() ? b.d[i] : 0);
            if (c < 0) { r.d.push_back(c + B); c = -1; } else { r.d.push_back(c); c = 0; }
        }
        r.trim(); return r;
    }
    friend Big operator+(const Big &a, const Big &b) {
        Big r;
        if (a.neg == b.neg) { r = addAbs(a, b); r.neg = a.neg; }
        else if (cmpAbs(a, b) >= 0) { r = subAbs(a, b); r.neg = a.neg; }
        else { r = subAbs(b, a); r.neg = b.neg; }
        r.trim(); return r;
    }
    friend Big operator-(const Big &a, const Big &b) { Big nb = b; if (!nb.isZero()) nb.neg = !nb.neg; return a + nb; }
    friend Big operator*(const Big &a, const Big &b) {
        Big r;
        if (a.isZero() || b.isZero()) return r;
        vector<uint64_t> t(a.d.size() + b.d.size() + 1, 0);
        for (size_t i = 0; i < a.d.size(); i++) {
            uint64_t c = 0;
            for (size_t j = 0; j < b.d.size(); j++) {
                uint64_t cur = t[i + j] + (uint64_t)a.d[i] * b.d[j] + c;
                t[i + j] = cur % B; c = cur / B;
            }
            size_t k = i + b.d.size();
            while (c) { uint64_t cur = t[k] + c; t[k] = cur % B; c = cur / B; k++; }
        }
        r.d.assign(t.begin(), t.end());
        r.neg = a.neg != b.neg; r.trim(); return r;
    }
    Big divSmall(uint32_t v) const {          // egzaktno ili s odbacivanjem ostatka
        Big r = *this; uint64_t rem = 0;
        for (int i = (int)r.d.size() - 1; i >= 0; i--) {
            uint64_t cur = r.d[i] + rem * B;
            r.d[i] = cur / v; rem = cur % v;
        }
        r.trim(); return r;
    }
    long double toLD() const {
        long double x = 0;
        for (int i = (int)d.size() - 1; i >= 0; i--) x = x * B + d[i];
        return neg ? -x : x;
    }
    bool operator<=(const Big &o) const { return (*this - o).neg || (*this - o).isZero(); }
    bool operator<(const Big &o) const { return (*this - o).neg; }
};

// P(n) = najveći k s k(k+1)/2 <= n
Big Pbig(const Big &n) {
    long double est = sqrtl(2.0L * n.toLD());
    Big k = Big::fromString(to_string((unsigned long long)min(est, 1.8e19L)));
    if (est >= 1.8e19L) {                      // ne stane u 64 bita: složi iz string zapisa long double procjene
        char buf[64]; snprintf(buf, sizeof buf, "%.0Lf", est); k = Big::fromString(buf);
    }
    auto tri = [](const Big &x) { return (x * (x + Big(1))).divSmall(2); };
    while (!(tri(k) <= n)) k = k - Big(1);
    while (tri(k + Big(1)) <= n) k = k + Big(1);
    return k;
}

int Psmall(long long n) { long long k = (long long)sqrtl(2.0L * n); while (k * (k + 1) / 2 > n) k--; while ((k + 1) * (k + 2) / 2 <= n) k++; return k; }

// Lagrangeova interpolacija: polinom stupnja K zadan vrijednostima y[0..K] u točkama 0..K, evaluacija u x.
Big evalPoly(const vector<Big> &y, const Big &x) {
    int K = (int)y.size() - 1;
    if (!x.neg && x.d.size() <= 1 && (x.isZero() ? 0 : (long long)x.d[0]) <= K) return y[x.isZero() ? 0 : x.d[0]];
    vector<Big> pre(K + 2), suf(K + 2);
    pre[0] = Big(1);
    for (int j = 0; j <= K; j++) pre[j + 1] = pre[j] * (x - Big(j));
    suf[K + 1] = Big(1);
    for (int j = K; j >= 0; j--) suf[j] = suf[j + 1] * (x - Big(j));
    // y_i * prod_{j != i} (x - j) / prod_{j != i} (i - j),  prod_{j != i}(i - j) = i! (K-i)! (-1)^{K-i}
    // zajednički nazivnik K!: koeficijent uz y_i je C(K,i) (-1)^{K-i}
    vector<Big> binom(K + 1); binom[0] = Big(1);
    for (int i = 1; i <= K; i++) binom[i] = (binom[i - 1] * Big(K - i + 1)).divSmall(i);
    Big sum;
    for (int i = 0; i <= K; i++) {
        if (y[i].isZero()) continue;
        Big t = y[i] * pre[i] * suf[i + 1] * binom[i];
        if ((K - i) & 1) sum = sum - t; else sum = sum + t;
    }
    for (int i = 2; i <= K; i++) sum = sum.divSmall(i);   // dijeljenje s K! (egzaktno: F je cjelobrojan)
    return sum;
}

vector<Big> Qs;                    // Q(i), i <= TAB
vector<int> Ps;                    // P(i)
vector<vector<Big>> fval(MAXD);    // f^{(d)}(i), i <= TAB
vector<vector<Big>> Fpts(MAXD);    // F^{(d)} u točkama 0..deg
vector<vector<Big>> S(MAXD);       // S[d][n] = g(d, n) za n <= TAB

int main() {
    // Q i P za male indekse
    Qs.assign(TAB + 1, Big()); Ps.assign(TAB + 1, 0);
    for (int i = 1; i <= TAB; i++) Ps[i] = Psmall(i);
    Qs[1] = Big(1);
    for (int i = 2; i <= TAB; i++) Qs[i] = Qs[i - 1] + Qs[Ps[i]];
    // f^{(0)} = 1, F^{(d)} stupnja 2^{d+1} - 1, f^{(d+1)}(x) = F^{(d)}(x(x+1)/2 - 1)
    for (int d = 0; d < MAXD; d++) {
        fval[d].assign(TAB + 1, Big());
        if (d == 0) for (int i = 0; i <= TAB; i++) fval[d][i] = Big(1);
        else for (int i = 0; i <= TAB; i++) fval[d][i] = evalPoly(Fpts[d - 1], Big((long long)i * (i + 1) / 2 - 1));
        int deg = (1 << (d + 1)) - 1;
        Fpts[d].assign(deg + 1, Big());
        for (int x = 1; x <= deg; x++) Fpts[d][x] = Fpts[d][x - 1] + fval[d][x];
        S[d].assign(TAB + 1, Big());
        for (int nn = 1; nn <= TAB; nn++) S[d][nn] = S[d][nn - 1] + fval[d][nn] * Qs[Ps[nn]];
    }

    int T;
    if (scanf("%d", &T) != 1) return 0;
    char buf[128];
    while (T--) {
        scanf("%s", buf);
        // lanac n_0 = n, n_{l+1} = P(n_l) dok n_L <= MAXLEN
        vector<Big> lanac = {Big::fromString(buf)};
        while (!(lanac.back() <= Big(MAXLEN))) lanac.push_back(Pbig(lanac.back()));
        int L = (int)lanac.size() - 1;
        // G[d] = g(d, n_L) iz tablice, zatim g(d, n_l) = F^{(d)}(n_l) g(0, n_{l+1}) - g(d+1, n_{l+1})
        long long nL = lanac[L].isZero() ? 0 : lanac[L].d[0];
        vector<Big> G(L + 2);
        for (int d = 0; d <= L; d++) G[d] = S[d][nL];
        for (int l = L - 1; l >= 0; l--) {
            vector<Big> nG(L + 2);
            for (int d = 0; d <= l; d++) nG[d] = evalPoly(Fpts[d], lanac[l]) * G[0] - G[d + 1];
            G = nG;
        }
        puts(G[0].toString().c_str());
    }
    return 0;
}
