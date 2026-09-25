// N - XOR Reachable
// (C xor D) < K  <=>  postoji bit b s K_b = 1 takav da se D i P = C xor K
// podudaraju iznad bita b, a D_b = C_b (= P_b xor 1). Zato radimo
// "podijeli pa vladaj" po bitovima D (binarno stablo/trie prefiksa D):
// u cvoru za bit b, ako je K_b = 1, bridovi cija staza P ide u dijete 1
// aktivni su u CIJELOM podstablu djeteta 0 (i obratno) -> spojimo ih u DSU
// s vracanjem, rekurzivno obradimo dijete, vratimo. Svaki brid se u svakoj
// razini obradi najvise jednom: O((M log N + Q) * 30).
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int n;
vector<int> par, sz;
vector<pair<int, int>> hist;  // (korijen pripojen, prethodni korijen) za rollback
ll pairs = 0;

int find(int x) { while (par[x] != x) x = par[x]; return x; }
void unite(int a, int b) {
    a = find(a); b = find(b);
    if (a == b) { hist.push_back({-1, -1}); return; }
    if (sz[a] < sz[b]) swap(a, b);
    par[b] = a; sz[a] += sz[b];
    pairs += (ll)sz[b] * (sz[a] - sz[b]);
    hist.push_back({b, a});
}
void rollback(size_t to) {
    while (hist.size() > to) {
        auto [b, a] = hist.back(); hist.pop_back();
        if (b < 0) continue;
        pairs -= (ll)sz[b] * (sz[a] - sz[b]);
        sz[a] -= sz[b]; par[b] = b;
    }
}

int K;
vector<int> A, B, P;      // bridovi; P = C xor K
vector<pair<int, int>> qs;  // (D, indeks upita), sortirano po D
vector<ll> ans;

void solve(int b, const vector<int> &edges, int ql, int qr) {
    if (ql >= qr) return;
    if (b < 0) {  // svi upiti u [ql,qr) imaju isti D: trenutni DSU je tocan
        for (int i = ql; i < qr; i++) ans[qs[i].second] = pairs;
        return;
    }
    // podjela upita po bitu b (sortirani su, isti prefiks iznad b)
    int mid = ql;
    while (mid < qr && !((qs[mid].first >> b) & 1)) mid++;
    vector<int> e0, e1;
    for (int id : edges) ((P[id] >> b) & 1 ? e1 : e0).push_back(id);
    bool kb = (K >> b) & 1;
    // dijete 0: D_b = 0; ako je K_b = 1 aktivni su bridovi s P_b = 1 (C_b = 0)
    if (ql < mid) {
        size_t save = hist.size();
        if (kb) for (int id : e1) unite(A[id], B[id]);
        solve(b - 1, e0, ql, mid);
        rollback(save);
    }
    if (mid < qr) {
        size_t save = hist.size();
        if (kb) for (int id : e0) unite(A[id], B[id]);
        solve(b - 1, e1, mid, qr);
        rollback(save);
    }
}

int main() {
    int m;
    scanf("%d %d %d", &n, &m, &K);
    A.resize(m); B.resize(m); P.resize(m);
    for (int i = 0; i < m; i++) {
        int c;
        scanf("%d %d %d", &A[i], &B[i], &c);
        P[i] = c ^ K;
    }
    int q;
    scanf("%d", &q);
    qs.resize(q); ans.assign(q, 0);
    for (int i = 0; i < q; i++) { scanf("%d", &qs[i].first); qs[i].second = i; }
    sort(qs.begin(), qs.end());
    par.resize(n + 1); sz.assign(n + 1, 1);
    iota(par.begin(), par.end(), 0);
    vector<int> all(m);
    iota(all.begin(), all.end(), 0);
    solve(29, all, 0, q);
    for (int i = 0; i < q; i++) printf("%lld\n", ans[i]);
}
