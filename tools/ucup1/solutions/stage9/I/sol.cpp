// UCup 1, Stage 9 (Qingdao 2018), I. Soldier Game
// Kandidati za minimalnu vrijednost tima su svih 2n-1 mogućih vrijednosti (a_i i a_i + a_{i+1}).
// Prolazimo kandidate rastuće; timove s vrijednošću < kandidata zabranjujemo (INF) i u segmentnom stablu
// održavamo najmanji mogući maksimum podjele. Čvor čuva f[l][r]: l/r = 1 ako lijevi/desni rubni vojnik
// pripada timu koji izlazi iz segmenta. Spajanje: f[i][j] = min_k max(L[i][k], R[k][j]).
#include <bits/stdc++.h>
using namespace std;

const long long INF = LLONG_MAX / 4;
int n;
vector<long long> a;
vector<array<array<long long, 2>, 2>> t;   // segmentno stablo
int sz;

array<array<long long, 2>, 2> spoji(const array<array<long long, 2>, 2> &L, const array<array<long long, 2>, 2> &R) {
    array<array<long long, 2>, 2> res;
    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 2; j++) {
            res[i][j] = INF;
            for (int k = 0; k < 2; k++) res[i][j] = min(res[i][j], max(L[i][k], R[k][j]));
        }
    return res;
}

int main() {
    int T;
    scanf("%d", &T);
    while (T--) {
        scanf("%d", &n);
        a.assign(n, 0);
        for (auto &x : a) scanf("%lld", &x);
        sz = 1; while (sz < n) sz <<= 1;
        array<array<long long, 2>, 2> prazno = {{{INF, INF}, {INF, INF}}};
        t.assign(2 * sz, prazno);
        // list i: [0][0] = sam (a_i), [0][1] = par s i+1 (trošak ovdje), [1][0] = desni dio para (trošak već plaćen), [1][1] = nemoguće
        for (int i = 0; i < n; i++) {
            t[sz + i][0][0] = a[i];
            t[sz + i][0][1] = (i + 1 < n) ? a[i] + a[i + 1] : INF;
            t[sz + i][1][0] = -INF;          // trošak para plaćen u lijevom listu: neutralno za max
            t[sz + i][1][1] = INF;
        }
        // prazni listovi iza kraja: neutralni element (identitet) da spajanje radi
        for (int i = n; i < sz; i++) { t[sz + i][0][0] = -INF; t[sz + i][1][1] = -INF; }
        for (int v = sz - 1; v >= 1; v--) t[v] = spoji(t[2 * v], t[2 * v + 1]);

        // kandidati: (vrijednost, list, koji element lista)
        vector<tuple<long long, int, int>> kand;
        for (int i = 0; i < n; i++) {
            kand.emplace_back(a[i], i, 0);
            if (i + 1 < n) kand.emplace_back(a[i] + a[i + 1], i, 1);
        }
        sort(kand.begin(), kand.end());
        long long best = INF;
        size_t p = 0;
        while (p < kand.size()) {
            long long v = get<0>(kand[p]);
            long long mx = t[1][0][0];           // trenutni najbolji maksimum uz dopuštene timove >= v
            if (mx < INF) best = min(best, mx - v);
            // zabrani sve timove vrijednosti točno v (za sljedeće, veće kandidate)
            while (p < kand.size() && get<0>(kand[p]) == v) {
                int i = get<1>(kand[p]), koji = get<2>(kand[p]);
                int node = sz + i;
                if (koji == 0) t[node][0][0] = INF; else t[node][0][1] = INF;
                for (node >>= 1; node >= 1; node >>= 1) t[node] = spoji(t[2 * node], t[2 * node + 1]);
                p++;
            }
        }
        printf("%lld\n", best);
    }
    return 0;
}
