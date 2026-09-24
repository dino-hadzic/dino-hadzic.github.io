// UCup 1, Stage 20 (India), C. Exam Requirements
// 2-SAT: varijabla x_i = "polazem ispit i". Uvjeti (x_A or x_B) i, za svaki par ispita koji se
// preklapaju, (not x_i or not x_j). Parova moze biti O(N^2), pa uvodimo pomocne varijable
// segmentnog stabla nad ispitima sortiranima po pocetku: U_cvor = "nijedan ispit iz raspona
// cvora se ne polaze". Klauzule: (not x_i or U_v) za O(log N) cvorova v koji pokrivaju ispite j
// s S_i <= S_j <= E_i (bez samog i), (not U_v or U_dijete), (not U_list or not x_j).
// Prosirena formula je ekvizadovoljiva izvornoj; rjesavamo je Tarjanovim SCC (iterativno).
#include <bits/stdc++.h>
using namespace std;

struct TwoSat {
    int n;                                   // broj varijabli; literal 2v = istina, 2v+1 = laz
    vector<vector<int>> g;
    TwoSat(int n) : n(n), g(2 * n) {}
    void klauzula(int a, int b) {            // (a or b): not a -> b, not b -> a
        g[a ^ 1].push_back(b);
        g[b ^ 1].push_back(a);
    }
    bool rjesivo() {
        int N = 2 * n, timer = 0;
        vector<int> idx(N, -1), low(N), comp(N, -1), st, poz(N, 0);
        vector<char> naStogu(N, 0);
        int brojKomp = 0;
        for (int s = 0; s < N; s++) {
            if (idx[s] != -1) continue;
            vector<int> put = {s};
            idx[s] = low[s] = timer++; st.push_back(s); naStogu[s] = 1;
            while (!put.empty()) {
                int v = put.back();
                if (poz[v] < (int)g[v].size()) {
                    int w = g[v][poz[v]++];
                    if (idx[w] == -1) {
                        idx[w] = low[w] = timer++; st.push_back(w); naStogu[w] = 1; put.push_back(w);
                    } else if (naStogu[w]) low[v] = min(low[v], idx[w]);
                } else {
                    if (low[v] == idx[v]) {
                        while (true) {
                            int w = st.back(); st.pop_back(); naStogu[w] = 0; comp[w] = brojKomp;
                            if (w == v) break;
                        }
                        brojKomp++;
                    }
                    put.pop_back();
                    if (!put.empty()) low[put.back()] = min(low[put.back()], low[v]);
                }
            }
        }
        for (int v = 0; v < n; v++) if (comp[2 * v] == comp[2 * v + 1]) return false;
        return true;
    }
};

int main() {
    int t;
    scanf("%d", &t);
    while (t--) {
        int n, m;
        scanf("%d %d", &n, &m);
        vector<long long> S(n), E(n);
        for (int i = 0; i < n; i++) scanf("%lld %lld", &S[i], &E[i]);
        vector<int> red(n);                  // ispiti sortirani po pocetku
        iota(red.begin(), red.end(), 0);
        sort(red.begin(), red.end(), [&](int a, int b) { return S[a] < S[b]; });
        vector<int> poz(n);
        for (int i = 0; i < n; i++) poz[red[i]] = i;
        vector<long long> pocetci(n);
        for (int i = 0; i < n; i++) pocetci[i] = S[red[i]];

        int sz = 1;
        while (sz < n) sz <<= 1;             // segmentno stablo: cvorovi 1..2sz-1, list k -> sz+k
        TwoSat ts(n + 2 * sz);               // varijable: 0..n-1 ispiti, n + v -> cvor v stabla
        auto X = [&](int i) { return 2 * i; };            // literal "polazem i"
        auto U = [&](int v) { return 2 * (n + v); };      // literal "U_v = nitko iz raspona"
        for (int v = 1; v < sz; v++) {                    // U_v -> U_djeca
            ts.klauzula(U(v) ^ 1, U(2 * v));
            ts.klauzula(U(v) ^ 1, U(2 * v + 1));
        }
        for (int k = 0; k < n; k++) ts.klauzula(U(sz + k) ^ 1, X(red[k]) ^ 1);   // U_list -> not x_j
        auto dodajRaspon = [&](int i, int l, int r) {     // x_i -> U_v za cvorove koji pokrivaju [l, r]
            if (l > r) return;
            for (l += sz, r += sz + 1; l < r; l >>= 1, r >>= 1) {
                if (l & 1) ts.klauzula(X(i) ^ 1, U(l++));
                if (r & 1) ts.klauzula(X(i) ^ 1, U(--r));
            }
        };
        for (int i = 0; i < n; i++) {
            int lo = lower_bound(pocetci.begin(), pocetci.end(), S[i]) - pocetci.begin();
            int hi = upper_bound(pocetci.begin(), pocetci.end(), E[i]) - pocetci.begin() - 1;
            dodajRaspon(i, lo, poz[i] - 1);
            dodajRaspon(i, poz[i] + 1, hi);
        }
        for (int j = 0; j < m; j++) {
            int a, b;
            scanf("%d %d", &a, &b);
            ts.klauzula(X(a - 1), X(b - 1));
        }
        puts(ts.rjesivo() ? "YES" : "NO");
    }
    return 0;
}
