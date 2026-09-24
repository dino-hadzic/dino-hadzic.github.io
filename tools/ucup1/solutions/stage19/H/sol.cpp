// UCup 1, Stage 19 (NAC 2023), H. Game Show Elimination
// Ključno: natjecatelj i sigurno pobjeđuje svakog j <= i-k, pa drugoplasirani (onaj koji
// ispada) uvijek leži u (j-k, j] ∪ {M}, gdje su M > j dva najviša preostala. Zato su svi
// natjecatelji <= j-k uvijek još prisutni, a stanje lanca je (j, mask, above):
//   mask  - prisutnost natjecatelja j-k+1 .. j-1 (k-1 bitova),
//   above - M - j; ako je above >= k, M pobjeđuje svaki tjedan pa stanja stapamo u above = k
//           (M tada odmah dobiva rang 1).
// Prolazimo stanja po padajućem j (i padajućoj maski) i propagiramo vjerojatnosti.
// Razdioba drugoplasiranog ovisi samo o relativnom rasporedu ljudi u (j-2k, j] ∪ {M}, pa
// je računamo lijeno po ključu (mask, above, brojDolje) DP-om po „kantama”: floor rezultata
// natjecatelja i je uniforman na {i, ..., i+k-1}, a unutar iste kante svi su poredci jednako
// vjerojatni. Osoba p je druga ako je u najvišoj kanti s x >= 1 drugih (šansa 1/(x+1)) ili
// je točno jedna osoba iznad nje, a u njezinoj kanti je x drugih (šansa 1/(x+1)).
#include <bits/stdc++.h>
using namespace std;

int n, k, K1, FULL;
vector<double> distCache;     // [(brojDolje*k + above-1) * 2^K1 + mask] * (k+1)
vector<char> distReady;

// Vjerojatnost da je natjecatelj s indeksom p drugoplasiran među ljudima na pozicijama pos.
double vjerDrugi(const vector<int> &pos, int p) {
    int t = pos.size();
    double ukupno = 0;
    vector<double> dp0(t + 1), dp1(t + 1), n0(t + 1), n1(t + 1);
    for (int b = pos[p]; b <= pos[p] + k - 1; ++b) {
        // dp[a][x]: a = koliko je drugih iznad kante b (0/1), x = koliko ih je točno u kanti b
        fill(dp0.begin(), dp0.end(), 0.0);
        fill(dp1.begin(), dp1.end(), 0.0);
        dp0[0] = 1;
        int cnt = 0;
        for (int r = 0; r < t; ++r) {
            if (r == p) continue;
            int lo = pos[r], hi = pos[r] + k - 1;      // moguće kante osobe r
            double pIznad = (double)max(0, min(k, hi - b)) / k;
            double pU = (lo <= b && b <= hi) ? 1.0 / k : 0.0;
            double pIspod = (double)max(0, min(k, b - lo)) / k;
            fill(n0.begin(), n0.begin() + cnt + 2, 0.0);
            fill(n1.begin(), n1.begin() + cnt + 2, 0.0);
            for (int x = 0; x <= cnt; ++x) {
                if (dp0[x] != 0) {
                    n0[x] += dp0[x] * pIspod;
                    n0[x + 1] += dp0[x] * pU;
                    n1[x] += dp0[x] * pIznad;
                }
                if (dp1[x] != 0) {
                    n1[x] += dp1[x] * pIspod;
                    n1[x + 1] += dp1[x] * pU;
                }
            }
            ++cnt;
            swap(dp0, n0);
            swap(dp1, n1);
        }
        double s = 0;
        for (int x = 1; x <= cnt; ++x) s += dp0[x] / (x + 1);   // p u najvišoj kanti s x drugih
        for (int x = 0; x <= cnt; ++x) s += dp1[x] / (x + 1);   // točno jedan iznad, p prvi u svojoj kanti
        ukupno += s / k;                                        // P(floor(p) = b) = 1/k
    }
    return ukupno;
}

// Razdioba drugoplasiranog: indeksi 0..k-2 su bitovi maske, k-1 je j, k je M.
const double *razdioba(int mask, int above, int brojDolje) {
    int key = (brojDolje * k + (above - 1)) * (FULL + 1) + mask;
    double *out = &distCache[(size_t)key * (k + 1)];
    if (distReady[key]) return out;
    distReady[key] = 1;
    vector<int> pos;
    vector<int> idx;              // idx[i] = indeks u razdiobi ili -1 (osobe „dolje” nisu kandidati)
    for (int i = 0; i < brojDolje; ++i) { pos.push_back(-k - i); idx.push_back(-1); }
    for (int i = 0; i < K1; ++i)
        if (mask >> i & 1) { pos.push_back(-(k - 1) + i); idx.push_back(i); }
    pos.push_back(0); idx.push_back(k - 1);
    pos.push_back(above); idx.push_back(k);
    for (int i = 0; i <= k; ++i) out[i] = 0;
    for (int r = 0; r < (int)pos.size(); ++r) {
        if (idx[r] < 0) continue;
        if (idx[r] == k && above >= k) continue;   // stopljeni M nikad nije drugi
        out[idx[r]] = vjerDrugi(pos, r);
    }
    return out;
}

int main() {
    if (scanf("%d %d", &n, &k) != 2) return 0;
    K1 = k - 1;
    FULL = (1 << K1) - 1;
    distCache.assign((size_t)k * k * (FULL + 1) * (k + 1), 0.0);
    distReady.assign((size_t)k * k * (FULL + 1), 0);

    // prob[j][above-1][mask]
    auto id = [&](int j, int above, int mask) {
        return ((size_t)j * k + (above - 1)) * (FULL + 1) + mask;
    };
    vector<double> prob((size_t)n * k * (FULL + 1), 0.0);
    vector<double> E(n + 1, 0.0);

    int j0 = n - 1, mask0 = 0;
    for (int i = 0; i < K1; ++i)
        if (j0 - k + 1 + i >= 1) mask0 |= 1 << i;
    prob[id(j0, 1, mask0)] = 1.0;

    for (int j = n - 1; j >= 1; --j) {
        int dolje = max(0, j - k);                 // svi <= j-k su prisutni
        int brojDolje = min(K1, dolje);            // koliko ih utječe na razdiobu
        for (int above = 1; above <= k; ++above) {
            for (int mask = FULL; mask >= 0; --mask) {
                double pr = prob[id(j, above, mask)];
                if (pr == 0) continue;
                int S = dolje + __builtin_popcount(mask) + 2;   // broj preostalih = rang onoga koji ispada
                const double *d = razdioba(mask, above, brojDolje);
                bool stopljeno = (above == k);
                int M = j + above;
                // sljedeći najviši ispod j (ako j ili M ispadne)
                int jNovi = mask ? j - k + 1 + (31 - __builtin_clz(mask)) : j - k;
                for (int c = 0; c <= k; ++c) {
                    double q = d[c];
                    if (q == 0) continue;
                    double w = pr * q;
                    if (c < K1) {
                        int osoba = j - k + 1 + c;
                        E[osoba] += w * S;
                        prob[id(j, above, mask ^ (1 << c))] += w;
                        continue;
                    }
                    int osoba = (c == K1) ? j : M;
                    E[osoba] += w * S;
                    if (S == 2) {                      // ostaje jedan: on dobiva rang 1
                        if (!stopljeno) E[(c == K1) ? M : j] += w;
                        continue;
                    }
                    int dlt = j - jNovi;
                    int maskNovi = (mask << dlt) & FULL;
                    for (int i = 0; i < dlt && i < K1; ++i)
                        if (jNovi - k + 1 + i >= 1) maskNovi |= 1 << i;
                    int aboveNovi = (c == K1) ? above + dlt : dlt;
                    int MNovi = (c == K1) ? M : j;
                    if (aboveNovi >= k) {
                        if (!stopljeno) E[MNovi] += w;  // M od sada uvijek pobjeđuje: rang 1
                        aboveNovi = k;
                    }
                    prob[id(jNovi, aboveNovi, maskNovi)] += w;
                }
            }
        }
    }
    for (int i = 1; i <= n; ++i) printf("%.9f\n", E[i]);
    return 0;
}
