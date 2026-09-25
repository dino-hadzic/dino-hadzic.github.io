// UCup 1, Stage 15 (ZJCPC 2023), C. Puzzle: Kusabi
// Brid (v, roditelj) koristi se točno onda kad podstablo od v ima neparan broj označenih vrhova,
// i tada iz podstabla „izlazi” točno jedan vrh. Pohlepno odozdo: u vrhu v skupimo kandidate
// (v ako je označen + po jedan iz svakog djeteta), Tongove sparimo po dubini, Chang/Duan sparimo
// sortirano; prema gore šaljemo najdublji zadrživi Chang / najplići zadrživi Duan / neparni Tong.
#include <bits/stdc++.h>
using namespace std;

int n;
vector<int> par, dep, tip;   // tip: 0 = neoznačen, 1 = Chang, 2 = Duan, 3 = Tong
vector<vector<int>> djeca;
vector<pair<int,int>> parovi;

void nemoguce() { puts("NO"); exit(0); }

// Vraća vrh koji se šalje prema gore iz podstabla od v (0 ako nijedan).
int obradi(int v, const vector<int>& kandidati) {
    vector<int> C, D;               // Chang, Duan (indeksi vrhova)
    map<int, vector<int>> T;        // Tong po dubini
    for (int u : kandidati) {
        if (tip[u] == 1) C.push_back(u);
        else if (tip[u] == 2) D.push_back(u);
        else T[dep[u]].push_back(u);
    }
    int gore = 0;
    for (auto& [d, vec] : T) {
        for (size_t i = 0; i + 1 < vec.size(); i += 2) parovi.push_back({vec[i], vec[i + 1]});
        if (vec.size() & 1) {
            if (gore) nemoguce();   // dva vrha bi morala izaći kroz isti brid
            gore = vec.back();
        }
    }
    auto poDubini = [&](int a, int b) { return dep[a] < dep[b]; };
    sort(C.begin(), C.end(), poDubini);
    sort(D.begin(), D.end(), poDubini);
    int c = C.size(), d = D.size();
    if (abs(c - d) > 1 || (abs(c - d) == 1 && gore)) nemoguce();
    if (c == d + 1) {
        // izbacujemo C_j; ostatak se sparuje sortirano: D_i-C_i (i<j), D_i-C_{i+1} (i>=j)
        // uvjet: dep(C_i) > dep(D_i) za i<j  i  dep(C_{i+1}) > dep(D_i) za i>=j
        vector<char> pref(c + 1, 1), suf(c + 1, 1);    // pref[j]: uvjet za sve i<j; suf[j]: za sve i>=j
        for (int i = 0; i < d; ++i) pref[i + 1] = pref[i] && dep[C[i]] > dep[D[i]];
        for (int i = d - 1; i >= 0; --i) suf[i] = suf[i + 1] && dep[C[i + 1]] > dep[D[i]];
        int j = -1;
        for (int cand = c - 1; cand >= 0; --cand)          // najdublji zadrživi Chang
            if (pref[cand] && suf[cand]) { j = cand; break; }
        if (j < 0) nemoguce();
        gore = C[j];
        C.erase(C.begin() + j);
    } else if (d == c + 1) {
        // izbacujemo D_j: C_i-D_i (i<j), C_i-D_{i+1} (i>=j)
        vector<char> pref(d + 1, 1), suf(d + 1, 1);
        for (int i = 0; i < c; ++i) pref[i + 1] = pref[i] && dep[C[i]] > dep[D[i]];
        for (int i = c - 1; i >= 0; --i) suf[i] = suf[i + 1] && dep[C[i]] > dep[D[i + 1]];
        int j = -1;
        for (int cand = 0; cand < d; ++cand)               // najplići zadrživi Duan
            if (pref[cand] && suf[cand]) { j = cand; break; }
        if (j < 0) nemoguce();
        gore = D[j];
        D.erase(D.begin() + j);
    }
    for (int i = 0; i < (int)C.size(); ++i) {
        if (dep[C[i]] <= dep[D[i]]) nemoguce();
        parovi.push_back({C[i], D[i]});
    }
    return gore;
}

int main() {
    scanf("%d", &n);
    par.assign(n + 1, 0); dep.assign(n + 1, 0); tip.assign(n + 1, 0); djeca.assign(n + 1, {});
    for (int i = 2; i <= n; ++i) {
        int v, p; char s[16];
        scanf("%d %d %s", &v, &p, s);
        par[v] = p; dep[v] = dep[p] + 1; djeca[p].push_back(v);
        if (s[0] == 'C') tip[v] = 1; else if (s[0] == 'D') tip[v] = 2; else if (s[0] == 'T') tip[v] = 3;
    }
    // p_i < i, pa je obrnuti redoslijed indeksa ujedno redoslijed „djeca prije roditelja”
    vector<int> gore(n + 1, 0);
    for (int v = n; v >= 1; --v) {
        vector<int> kandidati;
        if (tip[v]) kandidati.push_back(v);
        for (int u : djeca[v]) if (gore[u]) kandidati.push_back(gore[u]);
        gore[v] = obradi(v, kandidati);
    }
    if (gore[1]) nemoguce();     // korijen nije označen: ništa ne smije ostati nespareno
    puts("YES");
    for (auto [a, b] : parovi) printf("%d %d\n", a, b);
    return 0;
}
