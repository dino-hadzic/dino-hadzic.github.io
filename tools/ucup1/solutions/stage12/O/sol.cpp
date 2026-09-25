// O - Jewel Game
// Stanje: (maska preostalih dragulja, tko je na potezu, pozicija Alice, pozicija Boba).
// Potezi koji uzimaju dragulj vode u manju masku (vrijednost vec poznata),
// ostali ostaju u istoj maski i tvore ciklicki graf. Za fiksnu masku radimo
// retrogradnu analizu:
//  (a) stanje cija su sva sljedeca stanja odredena dobiva max/min od njih;
//  (b) inace, medu neodredenim stanjima uzmemo ono s najvecom apsolutnom
//      vrijednoscu vec odredene opcije (pozitivnom za Alice, negativnom za Boba)
//      i njome ga odredimo;
//  (c) kad vise nema kandidata, sva preostala stanja imaju vrijednost 0
//      (nitko ne moze prisiliti dobitak; ponavljanje zavrsava igru s 0).
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int n, m, A0, B0, K;
vector<vector<int>> g, rg;
int jewelAt[31];  // indeks dragulja na vrhu ili -1
ll W[10];

int main() {
    scanf("%d %d %d %d", &n, &m, &A0, &B0);
    g.assign(n + 1, {}); rg.assign(n + 1, {});
    for (int i = 0; i < m; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        g[u].push_back(v); rg[v].push_back(u);
    }
    scanf("%d", &K);
    for (int v = 1; v <= n; v++) jewelAt[v] = -1;
    for (int i = 0; i < K; i++) {
        int x;
        scanf("%d %lld", &x, &W[i]);
        jewelAt[x] = i;
    }
    int S = 2 * (n + 1) * (n + 1);
    auto id = [&](int turn, int pa, int pb) { return (turn * (n + 1) + pa) * (n + 1) + pb; };
    // val[mask][stanje]
    vector<vector<ll>> val(1 << K, vector<ll>(S, 0));
    // maske po rastucem broju bitova (masku 0 = kraj igre, vrijednost 0)
    vector<int> masks;
    for (int mk = 1; mk < (1 << K); mk++) masks.push_back(mk);
    sort(masks.begin(), masks.end(), [](int a, int b) {
        int ca = __builtin_popcount(a), cb = __builtin_popcount(b);
        return ca != cb ? ca < cb : a < b;
    });
    vector<ll> best(S);
    vector<int> cnt(S);
    vector<char> done(S);
    for (int mk : masks) {
        // je li na vrhu v dragulj koji je jos u igri
        auto hasJewel = [&](int v) { return jewelAt[v] >= 0 && (mk >> jewelAt[v] & 1); };
        fill(done.begin(), done.end(), 0);
        deque<int> q;  // stanja odredena pravilom (a)
        priority_queue<pair<ll, int>> cand;  // (|vrijednost|, stanje) za pravilo (b)
        // inicijalizacija: broj unutarnjih sljedbenika i najbolja izlazna opcija
        for (int turn = 0; turn < 2; turn++)
            for (int pa = 1; pa <= n; pa++)
                for (int pb = 1; pb <= n; pb++) {
                    int s = id(turn, pa, pb);
                    int from = turn == 0 ? pa : pb;
                    ll b = turn == 0 ? LLONG_MIN : LLONG_MAX;
                    int c = 0;
                    for (int v : g[from]) {
                        if (hasJewel(v)) {
                            int j = jewelAt[v];
                            int nm = mk ^ (1 << j);
                            ll ex;
                            if (turn == 0) ex = W[j] + val[nm][id(1, v, pb)];
                            else ex = -W[j] + val[nm][id(0, pa, v)];
                            b = turn == 0 ? max(b, ex) : min(b, ex);
                        } else c++;
                    }
                    cnt[s] = c; best[s] = b;
                    if (c == 0) q.push_back(s);
                    else if (turn == 0 && b != LLONG_MIN && b > 0) cand.push({b, s});
                    else if (turn == 1 && b != LLONG_MAX && b < 0) cand.push({-b, s});
                }
        auto settle = [&](int s, ll v) {
            done[s] = 1; val[mk][s] = v;
            int turn = s / ((n + 1) * (n + 1));
            int pa = s / (n + 1) % (n + 1), pb = s % (n + 1);
            // prethodnici: protivnik je upravo dosao na svoj vrh (bez dragulja)
            int arrived = turn == 0 ? pb : pa;  // ako je sada Alice na potezu, Bob je dosao na pb
            if (hasJewel(arrived)) return;      // takvo stanje nije unutarnji sljedbenik nikome
            for (int u : rg[arrived]) {
                int p = turn == 0 ? id(1, pa, u) : id(0, u, pb);
                if (done[p]) continue;
                int pt = 1 - turn;
                bool improved = false;
                if (pt == 0) { if (best[p] == LLONG_MIN || v > best[p]) { best[p] = v; improved = true; } }
                else { if (best[p] == LLONG_MAX || v < best[p]) { best[p] = v; improved = true; } }
                if (--cnt[p] == 0) q.push_back(p);
                else if (improved && pt == 0 && best[p] > 0) cand.push({best[p], p});
                else if (improved && pt == 1 && best[p] < 0) cand.push({-best[p], p});
            }
        };
        while (true) {
            if (!q.empty()) {
                int s = q.front(); q.pop_front();
                if (done[s]) continue;
                ll b = best[s];
                settle(s, b);
            } else if (!cand.empty()) {
                auto [mag, s] = cand.top(); cand.pop();
                if (done[s]) continue;
                ll b = best[s];
                if (llabs(b) != mag) continue;  // zastarjeli unos
                settle(s, b);
            } else break;
        }
        // preostala (neodredena) stanja: vrijednost 0 (val je vec 0)
    }
    printf("%lld\n", val[(1 << K) - 1][id(0, A0, B0)]);
}
