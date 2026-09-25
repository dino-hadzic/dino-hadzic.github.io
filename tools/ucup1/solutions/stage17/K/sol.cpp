// UCup 1, Stage 17, K - Balancing Sequences
// Ključne činjenice:
//  * minimum stupca može se samo smanjivati (u stupac ulazi nova vrijednost samo
//    na mjesto maksimuma), a element koji je minimum ne miče se dok je minimum;
//  * ako se minimumi stupaca (vrijednost i redak) u a i b podudaraju, maksimume
//    uvijek možemo preurediti: "sigurna" zamjena (obje nove vrijednosti ostaju
//    veće od minimuma) je reverzibilna, a iz svakog stanja sortiranjem tipa
//    "k-ti najmanji minimum dobiva k-ti najmanji maksimum" dolazimo u isto
//    kanonsko stanje -> a -> kanon -> b (unatrag).
//  * Faza 1: stupce s m_i > m'_i obrađujemo po rastućem m'_i; tada je m'_i uvijek
//    maksimum svog stupca. Ako je ciljni redak suprotan trenutnom minimumu,
//    jedna zamjena; ako je isti, treba posrednik x u (m'_i, m_i) koji nije
//    "zaključani" minimum (stupac s a-min = b-min), i tada dvije zamjene.
//  Nemoguće: m_i < m'_i; m_i = m'_i u različitim recima; istostrani stupac bez
//  posrednika. Ukupno <= 2n + 2(n-1) < 5n operacija.
#include <bits/stdc++.h>
using namespace std;

int n;
int a[3][2005], b[3][2005];
int pr[4005], pc[4005];  // položaj vrijednosti u trenutnom a
vector<array<int, 4>> ops;

int rowMax(int c) { return a[1][c] > a[2][c] ? 1 : 2; }
int mn(int c) { return min(a[1][c], a[2][c]); }
void swapMax(int c1, int c2) {  // zamijeni maksimume stupaca c1 i c2 u a
    int r1 = rowMax(c1), r2 = rowMax(c2);
    ops.push_back({r1, c1, r2, c2});
    swap(a[r1][c1], a[r2][c2]);
    pr[a[r1][c1]] = r1; pc[a[r1][c1]] = c1;
    pr[a[r2][c2]] = r2; pc[a[r2][c2]] = c2;
}

// niz sigurnih zamjena koje dovode 2xn tablicu t u kanonski oblik
vector<array<int, 4>> toCanon(int t[3][2005]) {
    vector<array<int, 4>> res;
    vector<int> cols(n), mx;
    iota(cols.begin(), cols.end(), 1);
    sort(cols.begin(), cols.end(), [&](int x, int y) { return min(t[1][x], t[2][x]) < min(t[1][y], t[2][y]); });
    for (int c = 1; c <= n; c++) mx.push_back(max(t[1][c], t[2][c]));
    sort(mx.begin(), mx.end());
    vector<int> where(2 * n + 1);
    for (int c = 1; c <= n; c++) where[max(t[1][c], t[2][c])] = c;
    for (int k = 0; k < n; k++) {
        int c = cols[k], want = mx[k];
        int j = where[want];
        if (j == c) continue;
        int r1 = t[1][c] > t[2][c] ? 1 : 2, r2 = t[1][j] > t[2][j] ? 1 : 2;
        res.push_back({r1, c, r2, j});
        swap(t[r1][c], t[r2][j]);
        where[t[r1][c]] = c; where[t[r2][j]] = j;
    }
    return res;
}

bool solve() {
    ops.clear();
    for (int c = 1; c <= n; c++) for (int r = 1; r <= 2; r++) { pr[a[r][c]] = r; pc[a[r][c]] = c; }
    vector<int> bm(n + 1), bs(n + 1);  // ciljni minimum i njegov redak
    vector<char> locked(2 * n + 1, 0);
    vector<int> pending;
    for (int c = 1; c <= n; c++) {
        bs[c] = b[1][c] < b[2][c] ? 1 : 2;
        bm[c] = b[bs[c]][c];
        int m = mn(c), s = (a[1][c] < a[2][c]) ? 1 : 2;
        if (m < bm[c]) return false;
        if (m == bm[c]) {
            if (s != bs[c]) return false;
            locked[m] = 1;
        } else pending.push_back(c);
    }
    sort(pending.begin(), pending.end(), [&](int x, int y) { return bm[x] < bm[y]; });
    for (int c : pending) {
        int m = mn(c), s = (a[1][c] < a[2][c]) ? 1 : 2;
        int tgt = bm[c];
        // ciljna vrijednost je maksimum svog stupca (svi manji ciljevi već su obrađeni)
        assert(rowMax(pc[tgt]) == pr[tgt] && pc[tgt] != c);
        if (bs[c] != s) {
            swapMax(c, pc[tgt]);
        } else {
            int x = -1;
            for (int v = tgt + 1; v < m; v++)
                if (!locked[v] && rowMax(pc[v]) == pr[v]) { x = v; break; }
            if (x < 0) return false;
            swapMax(c, pc[x]);    // x postaje minimum stupca c u suprotnom retku
            swapMax(c, pc[tgt]);  // m izlazi, cilj ulazi u traženi redak
        }
        assert(mn(c) == tgt && (a[1][c] < a[2][c] ? 1 : 2) == bs[c]);
    }
    // faza 2: a -> kanon, zatim unatrag kanon -> b
    int tb[3][2005];
    for (int c = 1; c <= n; c++) { tb[1][c] = b[1][c]; tb[2][c] = b[2][c]; }
    vector<array<int, 4>> fromB = toCanon(tb);
    for (auto &o : toCanon(a)) ops.push_back(o);
    for (int i = (int)fromB.size() - 1; i >= 0; i--) ops.push_back(fromB[i]);
    return true;
}

int main() {
    int T;
    scanf("%d", &T);
    string out;
    char buf[64];
    while (T--) {
        scanf("%d", &n);
        for (int r = 1; r <= 2; r++) for (int c = 1; c <= n; c++) scanf("%d", &a[r][c]);
        for (int r = 1; r <= 2; r++) for (int c = 1; c <= n; c++) scanf("%d", &b[r][c]);
        if (!solve()) { out += "-1\n"; continue; }
        snprintf(buf, sizeof buf, "%d\n", (int)ops.size());
        out += buf;
        for (auto &o : ops) {
            snprintf(buf, sizeof buf, "%d %d %d %d\n", o[0], o[1], o[2], o[3]);
            out += buf;
        }
    }
    fputs(out.c_str(), stdout);
    return 0;
}
