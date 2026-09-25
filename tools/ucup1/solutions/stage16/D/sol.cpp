// UCup 1, Stage 16, zadatak D: Classical DP Problem
// Obrnemo a tako da je a_1 >= a_2 >= ... >= a_n. Neka je k stranica najveceg
// kvadrata u dijagramu (a_k >= k, a_{k+1} <= k). Najmanji broj topova je r = k.
// Broj rasporeda = (#rasporedi u kojima svaki od prvih k redaka ima topa)
//                + (isto za stupce, tj. na transponiranom dijagramu) - k!.
// Prvi pribrojnik: t = a_{k+1} stupaca mora dobiti topa; f(i, j) = broj nacina
// da se topovi stave u prvih i redaka tako da tocno j od prvih t stupaca ima topa.
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 998244353;

// Broj nacina da se u svaki od k redaka sirina a_1 >= ... >= a_k stavi po jedan top
// tako da svaki od prvih t stupaca (t <= a_k) sadrzi bar jednog topa.
static long long prebroji(const vector<int>& a, int k, int t) {
    vector<long long> f(t + 1, 0), g(t + 1);
    f[0] = 1;
    for (int i = 0; i < k; ++i) {
        fill(g.begin(), g.end(), 0);
        for (int j = 0; j <= t; ++j) {
            if (!f[j]) continue;
            // top u jedan od t - j jos nepokrivenih obveznih stupaca
            if (j < t) g[j + 1] = (g[j + 1] + f[j] * (t - j)) % MOD;
            // top u bilo koji od preostalih a_i - (t - j) stupaca
            g[j] = (g[j] + f[j] * (a[i] - (t - j))) % MOD;
        }
        swap(f, g);
    }
    return f[t];
}

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    vector<int> a(n);
    for (int& v : a) scanf("%d", &v);
    reverse(a.begin(), a.end());  // sada a_0 >= a_1 >= ... >= a_{n-1}

    // k = najveci indeks (1-bazirano) s a_k >= k
    int k = 0;
    while (k < n && a[k] >= k + 1) ++k;
    int t = (k < n) ? a[k] : 0;  // a_{k+1} u 1-baziranom zapisu

    // transponirani dijagram: b_j = broj redaka sirine >= j (vec je nerastuci)
    vector<int> b(n);
    for (int j = 0, c = n; j < n; ++j) {
        while (c > 0 && a[c - 1] < j + 1) --c;
        b[j] = c;
    }
    // najveci kvadrat je simetrican, pa transponirani dijagram ima isti k
    int t2 = (k < n) ? b[k] : 0;

    long long fakt = 1;
    for (int i = 1; i <= k; ++i) fakt = fakt * i % MOD;

    long long w = (prebroji(a, k, t) + prebroji(b, k, t2) - fakt + MOD) % MOD;
    printf("%d %lld\n", k, w);
    return 0;
}
