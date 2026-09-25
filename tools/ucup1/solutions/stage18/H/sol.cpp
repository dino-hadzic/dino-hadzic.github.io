// UCup 1, Stage 18, H: Swapping Operation
// Prefiksni AND se mijenja u najviše ~31 "ključnoj" poziciji; isto za sufiksni AND.
// Uklanjanje neključnog elementa ne mijenja AND njegove strane, pa je zamjena dvaju
// neključnih elemenata beskorisna. Ostaju: zamjena ključ-ključ (31*31 parova po
// rezu k) i zamjena ključ s proizvoljnim elementom druge strane (za svaku od <= 31*31
// mogućih vrijednosti "AND bez ključa" tražimo najveći v & a_j na drugoj strani).
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    int T;
    if (scanf("%d", &T) != 1) return 0;
    while (T--) {
        int n;
        if (scanf("%d", &n) != 1) return 0;
        vector<int> a(n + 2, 0);
        for (int i = 1; i <= n; i++) if (scanf("%d", &a[i]) != 1) return 0;
        const int FULL = -1;  // sve jedinice; & s a_i daje a_i
        vector<int> pre(n + 2, FULL), suf(n + 2, FULL);
        for (int i = 1; i <= n; i++) pre[i] = pre[i - 1] & a[i];
        for (int i = n; i >= 1; i--) suf[i] = suf[i + 1] & a[i];
        vector<int> pk, sk;  // ključne pozicije prefiksa / sufiksa
        for (int i = 1; i <= n; i++) if (pre[i] != pre[i - 1]) pk.push_back(i);
        for (int i = n; i >= 1; i--) if (suf[i] != suf[i + 1]) sk.push_back(i);
        int P = pk.size(), S = sk.size();

        ll best = 0;
        // (a) bez zamjene
        for (int k = 1; k < n; k++) best = max(best, (ll)pre[k] + suf[k + 1]);

        // pa[k][t] = AND prefiksa 1..k bez elementa pk[t] (za pk[t] <= k)
        vector<vector<int>> pa(n + 1, vector<int>(P, FULL));
        vector<int> cur(P, FULL);  // cur[t] = f(pk[t]+1, k)
        for (int k = 1; k <= n; k++) {
            for (int t = 0; t < P; t++) {
                if (pk[t] > k) break;
                if (pk[t] < k) cur[t] &= a[k];
                pa[k][t] = pre[pk[t] - 1] & cur[t];
            }
        }
        // (b) ključ-ključ: prolaz s desna, sa[t] = AND sufiksa k+1..n bez elementa sk[t]
        {
            vector<int> scur(S, FULL);  // scur[t] = f(k+1, sk[t]-1)
            vector<int> sa(S, FULL);
            for (int k = n - 1; k >= 1; k--) {
                // element k+1 ulazi u sufiks
                for (int t = 0; t < S; t++) {
                    if (sk[t] < k + 1) break;
                    if (sk[t] > k + 1) scur[t] &= a[k + 1];
                    sa[t] = scur[t] & suf[sk[t] + 1];
                }
                for (int x = 0; x < P && pk[x] <= k; x++) {
                    int i = pk[x], vi = pa[k][x];
                    for (int y = 0; y < S && sk[y] > k; y++) {
                        int j = sk[y];
                        best = max(best, (ll)(vi & a[j]) + (sa[y] & a[i]));
                    }
                }
            }
        }
        // (c) ključ i u prefiksu, proizvoljan j > k: vrijednost (pa & a_j) + (suf[k+1] & a_i)
        for (int x = 0; x < P; x++) {
            int i = pk[x];
            int k = i;
            while (k <= n - 1) {
                int v = pa[k][x];
                int kend = k;
                while (kend + 1 <= n - 1 && pa[kend + 1][x] == v) kend++;
                // komad k..kend s konstantnim v: sufiksni maksimum v & a_j
                int sm = 0;
                for (int j = n; j >= k + 1; j--) {
                    sm = max(sm, v & a[j]);
                    if (j - 1 <= kend) best = max(best, (ll)sm + (suf[j] & a[i]));
                }
                k = kend + 1;
            }
        }
        // (c') ključ j u sufiksu, proizvoljan i <= k: vrijednost (pre[k] & a_j) + (sa & a_i)
        {
            // sa2[k][t] = AND sufiksa k+1..n bez elementa sk[t] (za sk[t] > k)
            vector<vector<int>> sa2(n + 1, vector<int>(S, FULL));
            vector<int> scur(S, FULL);
            for (int k = n - 1; k >= 0; k--) {
                for (int t = 0; t < S; t++) {
                    if (sk[t] < k + 1) break;
                    if (sk[t] > k + 1) scur[t] &= a[k + 1];
                    sa2[k][t] = scur[t] & suf[sk[t] + 1];
                }
            }
            for (int y = 0; y < S; y++) {
                int j = sk[y];
                int k = j - 1;
                while (k >= 1) {
                    int v = sa2[k][y];
                    int kstart = k;
                    while (kstart - 1 >= 1 && sa2[kstart - 1][y] == v) kstart--;
                    int pm = 0;
                    for (int i = 1; i <= k; i++) {
                        pm = max(pm, v & a[i]);
                        if (i >= kstart) best = max(best, (ll)pm + (pre[i] & a[j]));
                    }
                    k = kstart - 1;
                }
            }
        }
        printf("%lld\n", best);
    }
    return 0;
}
