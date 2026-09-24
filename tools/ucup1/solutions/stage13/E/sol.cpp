// UCup 1, Stage 13 (Um_nik mod 998244353 Contest), E. Egor Has a Problem
// Checker usporedjuje cjelobrojne kvocijente a[q]/a[p] i a[j]/a[i].
// Za n >= 63 sigurno postoje dva disjunktna susjedna para s kvocijentom 1;
// za n <= 62 iscrpno provjerimo sve cetvorke.
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    vector<long long> a(n);
    for (auto &x : a) scanf("%lld", &x);

    const int PRAG = 63;   // log2(1e18) + 3, zaokruzeno gore
    if (n >= PRAG) {
        // Susjedni par (t, t+1) ima kvocijent 1 tocno kad je a[t+1] < 2*a[t].
        // Udvostrucenja ima najvise 59, pa parova s kvocijentom 1 ima barem n-1-59 >= 3;
        // medju tri takva para dva su sigurno disjunktna.
        int prvi = -1;
        for (int t = 0; t + 1 < n; ++t) {
            if (a[t + 1] / a[t] == 1) {
                if (prvi == -1) {
                    prvi = t;
                } else if (t > prvi + 1) {
                    printf("YES\n%d %d %d %d\n", prvi + 1, prvi + 2, t + 1, t + 2);
                    return 0;
                }
            }
        }
        // Po dokazu se ovdje ne moze doci, ali za svaki slucaj padamo na iscrpnu pretragu.
    }

    for (int i = 0; i < n; ++i)
        for (int j = i + 1; j < n; ++j) {
            long long lijevo = a[j] / a[i];
            for (int p = j + 1; p < n; ++p)
                for (int q = p + 1; q < n; ++q)
                    if (a[q] / a[p] == lijevo) {
                        printf("YES\n%d %d %d %d\n", i + 1, j + 1, p + 1, q + 1);
                        return 0;
                    }
        }
    printf("NO\n");
    return 0;
}
