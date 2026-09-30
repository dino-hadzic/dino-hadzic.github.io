// J. Listovi
// Dvostruka zamjena u istom vrhu je identitet, pa je dovoljno odabrati skup F
// zamijenjenih vrhova s |F| <= m i |F| ≡ m (mod 2).  DP po podstablima:
// S[v][j] = leksikografski najmanji niz listova podstabla v uz točno j zamjena
// unutar podstabla.  Spajanje: bez zamjene S[l][a] ++ S[r][j-a], sa zamjenom
// S[r][a] ++ S[l][j-1-a]; kandidate uspoređujemo izravno.  Tablice djece se
// oslobađaju čim je roditelj gotov (memorijsko ograničenje 64 MiB).
#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<int> L, R, lab;
vector<int> inner;                 // broj unutarnjih vrhova u podstablu

typedef vector<vector<int>> Table;  // Table[j] = niz za točno j zamjena

// konkatenacija a ++ b
static vector<int> cat(const vector<int>& a, const vector<int>& b) {
    vector<int> c(a);
    c.insert(c.end(), b.begin(), b.end());
    return c;
}

Table solve(int v) {
    if (L[v] == 0) {                              // list
        inner[v] = 0;
        return Table{ vector<int>{lab[v]} };
    }
    Table tl = solve(L[v]);
    Table tr = solve(R[v]);
    int il = inner[L[v]], ir = inner[R[v]];
    inner[v] = il + ir + 1;
    int lim = min(inner[v], m);
    Table res(lim + 1);
    for (int j = 0; j <= lim; ++j) {
        vector<int> best;
        bool has = false;
        auto consider = [&](vector<int> cand) {
            if (!has || cand < best) { best = move(cand); has = true; }
        };
        // bez zamjene u v: a zamjena lijevo, j-a desno
        for (int a = max(0, j - ir); a <= min(j, il); ++a)
            consider(cat(tl[a], tr[j - a]));
        // sa zamjenom u v: a zamjena u (sada prvom) desnom podstablu, j-1-a u lijevom
        for (int a = max(0, j - 1 - il); a <= min(j - 1, ir); ++a)
            consider(cat(tr[a], tl[j - 1 - a]));
        res[j] = move(best);
    }
    return res;
}

int main() {
    scanf("%d %d", &n, &m);
    L.assign(n + 1, 0); R.assign(n + 1, 0); lab.assign(n + 1, 0); inner.assign(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        int type; scanf("%d", &type);
        if (type == 1) scanf("%d %d", &L[i], &R[i]);
        else scanf("%d", &lab[i]);
    }
    Table root = solve(1);
    vector<int> best; bool has = false;
    for (int j = 0; j < (int)root.size(); ++j) {
        if ((m - j) % 2 != 0) continue;           // višak zamjena trošimo u parovima
        if (!has || root[j] < best) { best = root[j]; has = true; }
    }
    for (size_t i = 0; i < best.size(); ++i) printf("%d%c", best[i], i + 1 < best.size() ? ' ' : '\n');
    return 0;
}
