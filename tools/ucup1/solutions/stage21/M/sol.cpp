// M. Trie – rangiranje podstabala po dubini odozdo, O(n log n)
// Niz stringova podstabla x (relativno prema x) je: [prazan string ako je x ključ] pa redom
// za djecu po slovima: slovo + niz djeteta. Djecu treba poredati po "rangu" njihovih nizova,
// gdje se nizovi uspoređuju leksikografski uz pravilo da je pravi PREFIKS VEĆI (dulji niz
// ide prije). Rang čvora određujemo iz vektora [0 ako je ključ] + sortirani rangovi djece,
// razinu po razinu od najdublje. Slova: djeca sortirana po (rang, indeks) dobivaju a, b, c, ...
#include <bits/stdc++.h>
using namespace std;

int main() {
    int T; scanf("%d", &T);
    while (T--) {
        int n, m; scanf("%d %d", &n, &m);
        vector<int> par(n + 1, -1), dep(n + 1, 0);
        vector<vector<int>> ch(n + 1);
        for (int i = 1; i <= n; i++) { scanf("%d", &par[i]); ch[par[i]].push_back(i); dep[i] = dep[par[i]] + 1; }
        vector<char> key(n + 1, 0);
        for (int i = 0; i < m; i++) { int k; scanf("%d", &k); key[k] = 1; }
        int D = *max_element(dep.begin(), dep.end());
        vector<vector<int>> byDepth(D + 1);
        for (int v = 0; v <= n; v++) byDepth[dep[v]].push_back(v);
        vector<int> rk(n + 1, 0);
        vector<vector<int>> vec(n + 1);
        // usporedba nizova: leksikografski, pravi prefiks je veći (kao da na kraju stoji +inf)
        auto less = [&](const vector<int> &a, const vector<int> &b) {
            int L = min(a.size(), b.size());
            for (int i = 0; i < L; i++) if (a[i] != b[i]) return a[i] < b[i];
            return a.size() > b.size();
        };
        for (int d = D; d >= 0; d--) {
            for (int v : byDepth[d]) {
                vector<int> &w = vec[v];
                if (key[v]) w.push_back(0);
                vector<int> r; for (int c : ch[v]) r.push_back(rk[c]);
                sort(r.begin(), r.end());
                w.insert(w.end(), r.begin(), r.end());
            }
            vector<int> ord = byDepth[d];
            sort(ord.begin(), ord.end(), [&](int a, int b) { return less(vec[a], vec[b]); });
            int cur = 0;
            for (int i = 0; i < (int)ord.size(); i++) {
                if (i == 0 || less(vec[ord[i - 1]], vec[ord[i]])) cur++;
                rk[ord[i]] = cur;
            }
        }
        string ans(n, 'a');
        for (int v = 0; v <= n; v++) {
            vector<int> c = ch[v];
            sort(c.begin(), c.end(), [&](int a, int b) { return rk[a] != rk[b] ? rk[a] < rk[b] : a < b; });
            for (int i = 0; i < (int)c.size(); i++) ans[c[i] - 1] = 'a' + i;
        }
        puts(ans.c_str());
    }
    return 0;
}
