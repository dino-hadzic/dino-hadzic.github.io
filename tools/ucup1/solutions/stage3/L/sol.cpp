// UCup 1, Stage 3 (AMPPZ 2022), L. Line Replacements
// Opterecenja c_e se mogu rastaviti na linije (jednostavne putove medu petljama) <=> u svakom
// vrhu bez petlje zbroj S_v opterecenja aktivnih bridova je paran i 2*max <= S_v (lokalno sparivanje).
// Obrnemo proces: krenemo od suma nakon svih krada i DODAJEMO ukradene bridove; brid tezine c smije
// se dodati u vrh bez petlje cim je c paran i c <= S_v. Dodavanje samo povecava S_v, pa pohlepno
// dodajemo bilo koji trenutno dopusten brid; redoslijed krada je obrnuti redoslijed dodavanja.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    int z;
    scanf("%d", &z);
    while (z--) {
        int n, p;
        scanf("%d %d", &n, &p);
        vector<char> petlja(n + 1, 0);
        for (int i = 0; i < p; ++i) { int v; scanf("%d", &v); petlja[v] = 1; }
        vector<int> eu(n), ev(n); vector<ll> ec(n);
        for (int i = 1; i < n; ++i) scanf("%d %d %lld", &eu[i], &ev[i], &ec[i]);
        int k;
        scanf("%d", &k);
        vector<int> kr(k);
        vector<char> ukraden(n, 0);
        for (int i = 0; i < k; ++i) { scanf("%d", &kr[i]); ukraden[kr[i]] = 1; }
        // stanje nakon svih krada: S_v i max po vrhu
        vector<ll> S(n + 1, 0), mx(n + 1, 0);
        for (int i = 1; i < n; ++i) if (!ukraden[i]) {
            S[eu[i]] += ec[i]; S[ev[i]] += ec[i];
            mx[eu[i]] = max(mx[eu[i]], ec[i]); mx[ev[i]] = max(mx[ev[i]], ec[i]);
        }
        bool ok = true;
        for (int v = 1; v <= n && ok; ++v)
            if (!petlja[v] && (S[v] % 2 != 0 || 2 * mx[v] > S[v])) ok = false;
        // ukradeni bridovi po vrhovima, sortirani po tezini
        vector<vector<int>> kod(n + 1);
        vector<int> treba(n, 0);                  // koliko krajeva bez petlje jos ceka dopustenje
        for (int e : kr) {
            for (int v : {eu[e], ev[e]}) if (!petlja[v]) {
                if (ec[e] % 2 != 0) ok = false;   // neparna tezina bi pokvarila parnost
                kod[v].push_back(e); ++treba[e];
            }
        }
        vector<int> red;                          // redoslijed dodavanja
        if (ok) {
            for (int v = 1; v <= n; ++v) sort(kod[v].begin(), kod[v].end(), [&](int a, int b) { return ec[a] < ec[b]; });
            vector<int> ptr(n + 1, 0), q;
            auto otvori = [&](int v) {            // dopusti bridove tezine <= S[v]
                while (ptr[v] < (int)kod[v].size() && ec[kod[v][ptr[v]]] <= S[v]) {
                    int e = kod[v][ptr[v]++];
                    if (--treba[e] == 0) q.push_back(e);
                }
            };
            for (int e : kr) if (treba[e] == 0) q.push_back(e);   // oba kraja imaju petlje
            for (int v = 1; v <= n; ++v) otvori(v);
            for (size_t i = 0; i < q.size(); ++i) {
                int e = q[i];
                red.push_back(e);
                S[eu[e]] += ec[e]; S[ev[e]] += ec[e];
                otvori(eu[e]); otvori(ev[e]);
            }
            if ((int)red.size() != k) ok = false;
        }
        if (!ok) { printf("NIE\n"); continue; }
        printf("TAK\n");
        for (int i = k - 1; i >= 0; --i) printf("%d%c", red[i], i == 0 ? '\n' : ' ');
    }
    return 0;
}
