// UCup 1, Stage 11 (EC-Final 2022), A. Coloring
// Funkcijski graf: boja teče od a_i prema i, tj. s ciklusa prema listovima i oko ciklusa. Na ciklusu
// jedinice uvijek čine jedan blok koji se vrti "naprijed"; čvor ciklusa doživi k_i izmjena boje.
// Stabla: f_v[k] = najbolji doprinos podstabla ako v ima točno k izmjena boje (0,1,0,1,...);
//         g_v[K] = max_{k <= K} f_v[k] -- dijete čvora s K "raspoloživih faza" smije imati <= K izmjena.
// Ciklus: parametri (q, r, r') opisuju koliko je puta prednji/stražnji kraj bloka obišao ciklus i gdje su
//         stali; za fiksni q sve položaje obradimo prefiksnim zbrojevima u O(L). Ukupno O(n^2).
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll NEG = LLONG_MIN / 4;

int n, s;
vector<ll> w, p;
vector<int> a;
vector<vector<int>> ch;          // djeca u stablima (bez bridova ciklusa)
vector<char> onCycle;
vector<vector<ll>> g;            // g[v][K] za K = 0..h_v+1 (dalje konstantno)

ll G(int v, ll K) {              // g_v(K) uz "zasićenje"
    if (K < 0) return NEG;
    size_t idx = min<ll>(K, (ll)g[v].size() - 1);
    return g[v][idx];
}

// DP po stablu (iterativno, po redoslijedu "djeca prije roditelja")
void treeDP(const vector<int> &order) {
    for (int v : order) {
        int h = 0;                                   // visina podstabla
        for (int c : ch[v]) h = max(h, (int)g[c].size() - 1);   // g[c] ima h_c + 2 elemenata
        // f_v[k] za k = 0..h+1  (h = max_c (h_c + 1), leaf: h = 0)
        vector<ll> f(h + 2);
        for (int k = 0; k <= h + 1; k++) {
            ll val = -(ll)k * p[v] + ((k & 1) ? w[v] : 0);
            for (int c : ch[v]) val += G(c, k);
            f[k] = val;
        }
        g[v].assign(h + 2, NEG);
        ll best = NEG;
        for (int k = 0; k <= h + 1; k++) { best = max(best, f[k]); g[v][k] = best; }
        for (int c : ch[v]) { g[c].clear(); g[c].shrink_to_fit(); }
    }
}

int main() {
    scanf("%d %d", &n, &s);
    w.resize(n + 1); p.resize(n + 1); a.resize(n + 1);
    for (int i = 1; i <= n; i++) scanf("%lld", &w[i]);
    for (int i = 1; i <= n; i++) scanf("%lld", &p[i]);
    for (int i = 1; i <= n; i++) scanf("%d", &a[i]);

    // pronađi ciklus komponente koja sadrži s (hodanjem po pokazivačima iz s)
    onCycle.assign(n + 1, 0);
    vector<int> cyc;
    {
        vector<int> vis(n + 1, 0);
        int u = s;
        while (!vis[u]) { vis[u] = 1; u = a[u]; }
        int start = u;
        do { onCycle[u] = 1; cyc.push_back(u); u = a[u]; } while (u != start);
    }
    // cyc[j+1] = a[cyc[j]], tj. boja teče cyc[j+1] -> cyc[j]; želimo redoslijed po toku: obrnuto
    reverse(cyc.begin(), cyc.end());
    int L = cyc.size();

    ch.assign(n + 1, {});
    for (int i = 1; i <= n; i++) if (!onCycle[i]) ch[a[i]].push_back(i);
    g.assign(n + 1, {});

    if (!onCycle[s]) {
        // samo podstablo od s; s počinje s bojom 1 i može najviše jednom preuzeti 0 od a_s
        vector<int> order, st = {s};
        while (!st.empty()) { int v = st.back(); st.pop_back(); order.push_back(v); for (int c : ch[v]) st.push_back(c); }
        reverse(order.begin(), order.end());
        // ne želimo DP za s (on je poseban), pa ga izbacimo iz reda i obradimo ručno
        order.erase(find(order.begin(), order.end(), s));
        treeDP(order);
        ll best = NEG;
        for (int ks = 0; ks <= 1; ks++) {
            ll val = -(ll)ks * p[s] + (ks == 0 ? w[s] : 0);
            for (int c : ch[s]) val += G(c, ks + 1);
            best = max(best, val);
        }
        printf("%lld\n", best);
        return 0;
    }

    // s je na ciklusu: DP po svim stablima nakačenim na ciklus
    {
        vector<int> order, st;
        for (int v : cyc) for (int c : ch[v]) st.push_back(c);
        while (!st.empty()) { int v = st.back(); st.pop_back(); order.push_back(v); for (int c : ch[v]) st.push_back(c); }
        reverse(order.begin(), order.end());
        treeDP(order);
    }
    // rotiraj tako da je cyc[0] = s
    { int pos = find(cyc.begin(), cyc.end(), s) - cyc.begin(); rotate(cyc.begin(), cyc.begin() + pos, cyc.end()); }

    int Kmax = 2;                                   // najveća korisna "kapaciteta"
    for (int v : cyc) for (int c : ch[v]) Kmax = max(Kmax, (int)g[c].size() + 1);
    // Gs(i, K) = suma g_c(K) po djeci čvora cyc[i] u stablima
    auto Gs = [&](int i, ll K) { ll r = 0; for (int c : ch[cyc[i]]) r += G(c, K); return r; };
    // vrijednost čvora cyc[i] s k izmjena, završnom bojom col i kapacitetom K za djecu
    auto val = [&](int i, ll k, int col, ll K) { return (col ? w[cyc[i]] : 0) - k * p[cyc[i]] + Gs(i, K); };

    ll best = NEG;
    if (L == 2) {
        // Blok duljine 1 na ciklusu duljine 2: svaki potez odmah daje "sve jedinice" ili "sve nule",
        // nakon čega se ništa više ne mijenja -> samo tri završna stanja.
        best = max(best, val(0, 0, 1, 1) + val(1, 0, 0, 0));   // ništa
        best = max(best, val(0, 0, 1, 1) + val(1, 1, 1, 1));   // v_1 preuzme 1
        best = max(best, val(0, 1, 0, 2) + val(1, 0, 0, 0));   // v_0 preuzme 0
        printf("%lld\n", best);
        return 0;
    }
    vector<ll> PA(L), PB(L), PC(L);
    for (int q = 0; 2 * q - 1 <= Kmax + 2; q++) {
        // Slučaj A: k_0 = 2q+1 (završna boja 0, K_0 = 2q+2); za i >= 1: i <= r' -> 2q+2 (boja 0),
        //           r' < i <= r -> 2q+1 (boja 1), i > r -> 2q (boja 0); 0 <= r' <= r <= L-1.
        {
            ll base = val(0, 2 * q + 1, 0, 2 * q + 2);
            ll sA = 0, sB = 0, sC = 0;
            for (int i = 1; i < L; i++) {
                sA += val(i, 2 * q + 2, 0, 2 * q + 2); PA[i] = sA;
                sB += val(i, 2 * q + 1, 1, 2 * q + 1); PB[i] = sB;
                sC += val(i, 2 * q, 0, 2 * q);         PC[i] = sC;
            }
            PA[0] = PB[0] = PC[0] = 0;
            ll totalC = PC[L - 1];
            ll bestPre = NEG;                          // max_{r' <= r} (PA[r'] - PB[r'])
            for (int r = 0; r < L; r++) {
                bestPre = max(bestPre, PA[r] - PB[r]);
                best = max(best, base + bestPre + PB[r] + (totalC - PC[r]));
            }
        }
        // Slučaj B: k_0 = 2q (boja 1, K_0 = 2q+1); za i >= 1: i <= r -> 2q+1 (boja 1),
        //           r < i <= r' -> 2q (boja 0), i > r' -> 2q-1 (boja 1); 0 <= r <= r' <= L-1;
        //           za q = 0 dopušteno je samo r' = L-1.
        {
            ll base = val(0, 2 * q, 1, 2 * q + 1);
            ll sD = 0, sE = 0, sF = 0;
            for (int i = 1; i < L; i++) {
                sD += val(i, 2 * q + 1, 1, 2 * q + 1); PA[i] = sD;
                sE += val(i, 2 * q, 0, 2 * q);         PB[i] = sE;
                sF += (q >= 1) ? val(i, 2 * q - 1, 1, 2 * q - 1) : 0; PC[i] = sF;
            }
            PA[0] = PB[0] = PC[0] = 0;
            ll totalF = PC[L - 1];
            // vrijednost = PA[r] + (PB[r'] - PB[r]) + (totalF - PC[r']); max po r' >= r
            ll bestSuf = NEG;                          // max_{r' >= r} (PB[r'] - PC[r'])
            for (int r = L - 1; r >= 0; r--) {
                if (q >= 1 || r == L - 1) bestSuf = max(bestSuf, PB[r] - PC[r]);
                best = max(best, base + PA[r] - PB[r] + bestSuf + totalF);
            }
        }
    }
    printf("%lld\n", best);
    return 0;
}
