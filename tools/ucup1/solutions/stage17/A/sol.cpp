// UCup 1, Stage 17, A - Graph Partitioning
// Svaki brid (x, y) s x < y može biti ili "roditeljski brid vrha y u T1"
// (jer je par_T1(y) < y) ili "roditeljski brid vrha x u T2" (par_T2(x) > x).
// Uvedemo 2n-2 "mjesta": T1:y za y = 2..n i T2:x za x = 1..n-1. Svako mjesto
// mora dobiti točno jedan brid, svaki brid odlazi na točno jedno od svoja dva
// mjesta. Graf mjesta ima 2n-2 vrhova i 2n-2 bridova; rješenje postoji ako i
// samo ako svaka komponenta ima točno onoliko bridova koliko i vrhova
// (pseudošuma), a tada je odgovor 2^(broj komponenti).
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 998244353;

vector<int> par, cntV, cntE;

int nadji(int x) {
    while (par[x] != x) {
        par[x] = par[par[x]];
        x = par[x];
    }
    return x;
}

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    int m = 2 * n - 2;
    par.resize(m);
    cntV.assign(m, 1);
    cntE.assign(m, 0);
    for (int i = 0; i < m; i++) par[i] = i;
    bool ok = true;
    for (int i = 0; i < m; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        if (u > v) swap(u, v);
        if (u == v) { ok = false; continue; }  // petlja ne može biti ni u jednom stablu
        // mjesto T1:v ima indeks v-2 (v >= 2), mjesto T2:u ima indeks n-1 + (u-1)
        int a = nadji(v - 2), b = nadji(n - 1 + (u - 1));
        if (a == b) {
            cntE[a]++;
        } else {
            par[a] = b;
            cntV[b] += cntV[a];
            cntE[b] += cntE[a] + 1;
        }
    }
    if (!ok) { puts("0"); return 0; }
    long long ans = 1;
    for (int i = 0; i < m; i++) {
        if (nadji(i) != i) continue;
        if (cntV[i] != cntE[i]) { puts("0"); return 0; }
        ans = ans * 2 % MOD;  // ciklus komponente orijentiramo na 2 načina
    }
    printf("%lld\n", ans);
    return 0;
}
