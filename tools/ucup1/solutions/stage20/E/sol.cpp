// UCup 1, Stage 20 (India), E. Strange Keyboard
// Konacni T sastoji se od blokova: pritisnemo tipku S, od nje "prezivi" prefiks P (|P| = l >= 1),
// a visak od x = |S| - l znakova pobrisemo (uz eventualno dodavanje "smeca" da duljina bude visekratnik K).
// cost(x) = najmanji broj poteza da pobrisemo tocno x znakova: za x >= K brisemo odmah
// (cost(x) = 1 + cost(x-K)), a za ostatke r < K Dijkstra po ostacima:
//   r -> (r+L) mod K  s tezinom 1 + floor((r+L)/K), za svaku razlicitu duljinu L neke tipke.
// Trie svih S_i; val[u] = min_{S u podstablu u} cost(|S| - dubina(u)). Racunamo naivno:
// za svaki S i svaki njegov prefiks-cvor u azuriramo val[u] -> ukupno sum |S_i| koraka.
// dp[i] = najmanje poteza za tocno T[0..i); dp[i+l] = min(dp[i] + 1 + val[T[i..i+l)]) setnjom po trieu.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll INF = (ll)1e18;

int main() {
    int q;
    scanf("%d", &q);
    static char buf[1000006];
    while (q--) {
        int n, K;
        scanf("%d %d", &n, &K);
        vector<string> S(n);
        int maxL = 0;
        for (int i = 0; i < n; i++) {
            scanf("%s", buf);
            S[i] = buf;
            maxL = max(maxL, (int)S[i].size());
        }
        scanf("%s", buf);
        string T = buf;
        int m = T.size();

        // razlicite duljine tipki
        vector<char> jeDuljina(maxL + 1, 0);
        for (auto& s : S) jeDuljina[s.size()] = 1;
        vector<int> duljine;
        for (int L = 1; L <= maxL; L++) if (jeDuljina[L]) duljine.push_back(L);

        // cres[r] = najmanje poteza da pobrisemo tocno r (< K) znakova
        vector<ll> cres(K, INF);
        cres[0] = 0;
        priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<>> pq;
        pq.push({0, 0});
        // Trazimo udaljenosti SVIH ostataka do cilja 0, pa vrtimo Dijkstru od 0 po obrnutim
        // bridovima: iz r' = (r+L) mod K natrag u r = (r' - L) mod K, tezina 1 + floor((r+L)/K).
        while (!pq.empty()) {
            auto [d, r2] = pq.top(); pq.pop();
            if (d > cres[r2]) continue;
            for (int L : duljine) {
                int r = ((r2 - L) % K + K) % K;
                ll w = 1 + (r + L) / K;
                if (d + w < cres[r]) { cres[r] = d + w; pq.push({cres[r], r}); }
            }
        }
        auto cost = [&](int x) -> ll {       // x >= 0
            ll c = cres[x % K];
            return c >= INF ? INF : c + x / K;
        };

        // trie
        vector<array<int, 26>> nxt(1);
        nxt[0].fill(-1);
        vector<ll> val(1, INF);
        for (auto& s : S) {
            int u = 0;
            for (char ch : s) {
                int c = ch - 'a';
                if (nxt[u][c] < 0) {
                    nxt[u][c] = nxt.size();
                    nxt.push_back({});
                    nxt.back().fill(-1);
                    val.push_back(INF);
                }
                u = nxt[u][c];
            }
        }
        for (auto& s : S) {                  // val[u] = min cost(|S| - dubina(u)) po svim S kroz u
            int u = 0, d = s.size();
            for (int k = 0; k < d; k++) {
                u = nxt[u][s[k] - 'a'];
                val[u] = min(val[u], cost(d - (k + 1)));
            }
        }

        vector<ll> dp(m + 1, INF);
        dp[0] = 0;
        for (int i = 0; i < m; i++) {
            if (dp[i] >= INF) continue;
            int u = 0;
            for (int l = 1; i + l <= m; l++) {
                u = nxt[u][T[i + l - 1] - 'a'];
                if (u < 0) break;
                if (val[u] < INF) dp[i + l] = min(dp[i + l], dp[i] + 1 + val[u]);
            }
        }
        printf("%lld\n", dp[m] >= INF ? -1 : dp[m]);
    }
    return 0;
}
