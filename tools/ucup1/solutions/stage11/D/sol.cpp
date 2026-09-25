// UCup 1, Stage 11 (EC-Final 2022), D. Minimum Suffix
// p_n je početak posljednjeg Lyndonovog faktora, p_{p_n - 1} početak pretposljednjeg itd. -> granice faktora.
// Unutar faktora w (Lyndonove riječi) vrijednosti q_m = p_m - b + 1 opisuju tok Duvalova algoritma bez
// zatvaranja: q_m = q_{m-P} + P znači w[m] = w[m-P] ("kopija"), q_m = 1 znači w[m] > w[m-P] ("veće",
// novi period P = m); sve ostalo je proturječje. Sve relacije pokazuju unaprijed, pa se najmanja riječ
// gradi greedy slijeva nadesno. Između faktora vrijedi w_a >= w_{a+1}: faktore obrađujemo zdesna nalijevo
// i za svaki gradimo najmanju riječ koja zadovoljava relacije i >= od sljedeće (usporedba uz vraćanje na
// posljednju "slobodnu" poziciju). Ukupno O(n).
#include <bits/stdc++.h>
using namespace std;

static char ibuf[1 << 25];
int ilen = 0, ipos = 0;
inline int gc() {
    if (ipos == ilen) { ilen = fread(ibuf, 1, sizeof(ibuf), stdin); ipos = 0; if (ilen <= 0) return -1; }
    return ibuf[ipos++];
}
inline int readInt() {
    int c = gc();
    while (c != '-' && (c < '0' || c > '9')) c = gc();
    int sgn = 1; if (c == '-') { sgn = -1; c = gc(); }
    int x = 0;
    while (c >= '0' && c <= '9') { x = x * 10 + (c - '0'); c = gc(); }
    return x * sgn;
}
string out;
inline void writeInt(int x) {
    char tmp[12]; int k = 0;
    if (x < 0) { out.push_back('-'); x = -x; }
    do { tmp[k++] = '0' + x % 10; x /= 10; } while (x);
    while (k) out.push_back(tmp[--k]);
}

int n;
vector<int> p, s, ref_;      // ref_[m] = pozicija s kojom se uspoređuje w[m]; free_[m] = relacija "veće"
vector<char> free_;

// relacije unutar faktora [b, e] (1-indeksirano, globalno); vraća false ako je proturječno
bool buildRelations(int b, int e) {
    if (p[b] != b) return false;
    free_[b] = 1; ref_[b] = 0;
    int P = 1;
    for (int m = b + 1; m <= e; m++) {
        if (p[m] < b) return false;
        if (p[m] == b) { free_[m] = 1; ref_[m] = m - P; P = m - b + 1; }
        else if (p[m] == p[m - P] + P) { free_[m] = 0; ref_[m] = m - P; }
        else return false;
    }
    return true;
}

// najmanja dopuštena vrijednost na poziciji m uz već određene ranije pozicije
inline int minimal(int m) { return free_[m] ? (ref_[m] ? s[ref_[m]] + 1 : 1) : s[ref_[m]]; }

// popuni [from, e] najmanjim dopuštenim vrijednostima
void fillMin(int from, int e) { for (int m = from; m <= e; m++) s[m] = minimal(m); }

// izgradi najmanju riječ na [b, e] koja zadovoljava relacije i >= v = s[vb, ve] (ve < b); ako vb > ve, bez uvjeta
void buildFactor(int b, int e, int vb, int ve) {
    if (vb > ve) { fillMin(b, e); return; }
    int L = e - b + 1, Lv = ve - vb + 1;
    int lastFree = -1;                                   // posljednja slobodna pozicija na kojoj je s[m] == v[m]
    for (int m = b; m <= e; m++) {
        int idx = m - b;
        if (idx >= Lv) { fillMin(m, e); return; }        // v je pravi prefiks od w -> w > v
        int vm = s[vb + idx];
        int lo = minimal(m);
        if (free_[m]) {
            if (lo > vm) { s[m] = lo; fillMin(m + 1, e); return; }   // w > v
            s[m] = vm; lastFree = m;
        } else {
            if (lo > vm) { s[m] = lo; fillMin(m + 1, e); return; }   // w > v
            if (lo < vm) {                                            // neuspjeh: vrati se na posljednju slobodnu
                s[lastFree] = s[vb + (lastFree - b)] + 1;
                fillMin(lastFree + 1, e);
                return;
            }
            s[m] = vm;
        }
    }
    if (L < Lv) {                                        // w je pravi prefiks od v -> w < v, moramo povećati
        s[lastFree] = s[vb + (lastFree - b)] + 1;
        fillMin(lastFree + 1, e);
    }
    // inače L == Lv i w == v
}

int main() {
    int T = readInt();
    out.reserve(1 << 24);
    while (T--) {
        n = readInt();
        p.assign(n + 1, 0); s.assign(n + 1, 0); ref_.assign(n + 1, 0); free_.assign(n + 1, 0);
        for (int i = 1; i <= n; i++) p[i] = readInt();

        // granice faktora zdesna nalijevo
        vector<pair<int, int>> fac;                       // (b, e), od posljednjeg prema prvom
        int e = n;
        while (e >= 1) { int b = p[e]; fac.push_back({b, e}); e = b - 1; }
        bool ok = true;
        for (auto [b, e2] : fac) if (!buildRelations(b, e2)) { ok = false; break; }
        if (!ok) { out += "-1\n"; continue; }

        int vb = 1, ve = 0;                               // prazan v za posljednji faktor
        for (auto [b, e2] : fac) { buildFactor(b, e2, vb, ve); vb = b; ve = e2; }
        for (int i = 1; i <= n; i++) { writeInt(s[i]); out.push_back(i == n ? '\n' : ' '); }
        if (out.size() > (1 << 23)) { fwrite(out.data(), 1, out.size(), stdout); out.clear(); }
    }
    fwrite(out.data(), 1, out.size(), stdout);
    return 0;
}
