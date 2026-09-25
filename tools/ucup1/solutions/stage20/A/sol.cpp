// UCup 1, Stage 20 (India), A. Maximum bitwise OR
// Potez na x: ako je bit i postavljen, x -> 2^i; inace x -> blok jedinica [i, j], gdje je j najnizi
// postavljeni bit iznad i. Rezultat poteza je uvijek blok jedinica [i, j] s j postavljenim u x i bez
// postavljenih bitova x strogo izmedu i i j.  Neka je k najvisi bit u OR-u raspona: maksimum je 2^{k+1}-1
// (dva poteza na elementu s bitom k: x -> 2^k -> 2^{k+1}-1).  Broj poteza: 0 ako je OR vec pun; inace
// neka su l, r najnizi i najvisi bit koji nedostaju. Jedan potez na x uspijeva ako i samo ako
//   (a) x nema bitova u [l, r] i ima neki bit iznad r (x >= 2^{r+1}); potez i = l daje blok [l, j],
//       j = najnizi bit x iznad r, koji pokriva sve bitove koji nedostaju;
//   (b) svaki "posebni" bit x (bit koji u rasponu ima samo x) jednak je j (inace ga izgubimo).
// Posebnih elemenata ima najvise 31 (po jedan za svaki bit s brojem pojavljivanja 1); nalazimo ih preko
// nxt[b][i] = prva pozicija >= i s bitom b. Neposebne kandidate brojimo: za svaki r cuvamo pozicije
// elemenata >= 2^{r+1} grupirane po najvisem bitu <= r (uvjet (a) <=> taj bit je < l), pa binarnim
// pretrazivanjem prebrojimo pozicije u [L, R]. Slozenost O(N * 31 + Q * 31 * log N) po testu.
#include <bits/stdc++.h>
using namespace std;
const int B = 31;

int main() {
    int T;
    scanf("%d", &T);
    while (T--) {
        int n, q;
        scanf("%d %d", &n, &q);
        vector<int> a(n + 1);
        for (int i = 1; i <= n; i++) scanf("%d", &a[i]);
        // cnt[b][i]: koliko od a[1..i] ima bit b; nxt[b][i]: prva pozicija >= i s bitom b
        vector<vector<int>> cnt(B, vector<int>(n + 1, 0)), nxt(B, vector<int>(n + 2, n + 1));
        for (int b = 0; b < B; b++) {
            for (int i = 1; i <= n; i++) cnt[b][i] = cnt[b][i - 1] + (a[i] >> b & 1);
            for (int i = n; i >= 1; i--) nxt[b][i] = (a[i] >> b & 1) ? i : nxt[b][i + 1];
        }
        // grupa[r][v+1] = pozicije i s a[i] >= 2^{r+1} i najvisim bitom <= r jednakim v (v = -1 ako ga nema)
        vector<vector<vector<int>>> grupa(B, vector<vector<int>>(B + 1));
        for (int r = 0; r < B; r++)
            for (int i = 1; i <= n; i++) {
                if (a[i] < (1LL << (r + 1))) continue;
                int v = -1;
                for (int b = r; b >= 0; b--) if (a[i] >> b & 1) { v = b; break; }
                grupa[r][v + 1].push_back(i);
            }
        while (q--) {
            int L, R;
            scanf("%d %d", &L, &R);
            int O = 0, k = -1;
            for (int b = 0; b < B; b++)
                if (cnt[b][R] - cnt[b][L - 1] > 0) { O |= 1 << b; k = b; }
            long long full = (1LL << (k + 1)) - 1;
            if (O == full) { printf("%lld 0\n", full); continue; }
            int l = -1, r = -1;
            for (int b = 0; b < k; b++)
                if (!(O >> b & 1)) { if (l < 0) l = b; r = b; }
            // posebni elementi: pozicije koje jedine drze neki bit
            vector<int> pos;
            for (int b = 0; b < B; b++)
                if (cnt[b][R] - cnt[b][L - 1] == 1) pos.push_back(nxt[b][L]);
            sort(pos.begin(), pos.end());
            pos.erase(unique(pos.begin(), pos.end()), pos.end());
            int maska = (1 << (r + 1)) - (1 << l);   // bitovi [l, r]
            bool jedan = false;
            int posebnihKandidata = 0;
            for (int p : pos) {
                int x = a[p];
                if (x >= (1 << (r + 1)) && (x & maska) == 0) {
                    posebnihKandidata++;
                    int j = r + 1;
                    while (!(x >> j & 1)) j++;
                    bool ok = true;
                    for (int b = 0; b < B && ok; b++)
                        if ((x >> b & 1) && cnt[b][R] - cnt[b][L - 1] == 1 && b != j) ok = false;
                    if (ok) jedan = true;
                }
            }
            // neposebni kandidat (uvjet (a)): bilo koji takav radi
            long long kandidata = 0;
            for (int v = -1; v < l; v++) {
                auto& g = grupa[r][v + 1];
                kandidata += upper_bound(g.begin(), g.end(), R) - lower_bound(g.begin(), g.end(), L);
            }
            if (kandidata - posebnihKandidata > 0) jedan = true;
            printf("%lld %d\n", full, jedan ? 1 : 2);
        }
    }
    return 0;
}
