// UCup 1, Stage 16, zadatak B: Classical Counting Problem
// Sortiramo a_1 >= ... >= a_n. Za podskup S neka je x najmanji indeks izvan S,
// y najveci indeks u S. S je moguc ako i samo ako a_y + m >= a_x te
//   sum l_i <= m*v <= sum r_i,
// gdje su l_i / r_i najmanji / najveci dopusteni broj glasova zadatku i.
// Kako je l_i <= r_i, oba uvjeta ne mogu istodobno pasti, pa je
//   odgovor = #{S : a_y + m >= a_x} - #{sum l > mv} - #{sum r < mv}.
// l_i ovise samo o x (ruksak unaprijed), r_i samo o y (ruksak unatrag): O(n^3 a).
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 998244353;

int main() {
    int t;
    if (scanf("%d", &t) != 1) return 0;
    while (t--) {
        int n, m, v;
        scanf("%d %d %d", &n, &m, &v);
        vector<int> a(n + 1);
        for (int i = 1; i <= n; ++i) scanf("%d", &a[i]);
        sort(a.begin() + 1, a.end(), greater<int>());

        long long ans = n;  // svi prefiksi {1..y} (uklj. S = svi zadaci) uvijek su moguci

        // 1) fiksiraj x (zadaci 1..x-1 u S, x nije). Clanovi S iza x su iz
        //    {x+1..Y}, gdje je a_Y >= a_x - m; svaki i u S doprinosi l_i = a_x - a_i.
        //    Brojimo neprazne podskupove sa sum l <= m*v.
        {
            int cap = m * v;  // zbrojeve vece od cap ne trebamo razlikovati
            vector<long long> f(cap + 2);
            for (int x = 1; x <= n; ++x) {
                fill(f.begin(), f.end(), 0);
                f[0] = 1;
                for (int i = x + 1; i <= n && a[i] + m >= a[x]; ++i) {
                    int w = a[x] - a[i];  // 0 <= w <= m
                    for (int s = cap + 1; s >= 0; --s) {
                        if (!f[s]) continue;
                        int ns = min(cap + 1, s + w);
                        f[ns] = (f[ns] + f[s]) % MOD;
                    }
                }
                long long cnt = 0;
                for (int s = 0; s <= cap; ++s) cnt += f[s];
                ans = (ans + cnt - 1) % MOD;  // -1: prazan podskup (y ne bi postojao)
            }
        }

        // 2) fiksiraj y (y u S, zadaci iza y nisu). Izbaceni zadaci ispred y su iz
        //    {X..y-1}, gdje je a_X <= a_y + m; sum r = n*m - sum_{i izbacen, i<y} (a_i - a_y).
        //    Uvjet sum r < m*v  <=>  sum (a_i - a_y) > m*(n - v). Ti su skupovi
        //    zadovoljavali a_y + m >= a_x, a sum l > mv ne mogu (l_i <= r_i), pa ih oduzimamo.
        {
            int cap = m * (n - v);
            vector<long long> f(cap + 2);
            for (int y = 1; y <= n; ++y) {
                fill(f.begin(), f.end(), 0);
                f[0] = 1;
                for (int i = y - 1; i >= 1 && a[i] <= a[y] + m; --i) {
                    int w = a[i] - a[y];  // 0 <= w <= m
                    for (int s = cap + 1; s >= 0; --s) {
                        if (!f[s]) continue;
                        int ns = min(cap + 1, s + w);
                        f[ns] = (f[ns] + f[s]) % MOD;
                    }
                }
                ans = (ans - f[cap + 1] + MOD) % MOD;
            }
        }
        printf("%lld\n", (ans % MOD + MOD) % MOD);
    }
    return 0;
}
