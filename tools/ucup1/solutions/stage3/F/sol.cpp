// UCup 1, Stage 3 (AMPPZ 2022), F. Flower Garden
// Uvjet "[a,b] sve ruze ILI [c,d] sve ljubicice" = implikacija: ljubicica bilo gdje u [a,b]
// => ljubicice na cijelom [c,d]. Graf implikacija gradimo preko dva segmentna stabla
// (O((n+q) log n) bridova), skupimo jako povezane komponente (iterativni Tarjan) i trazimo
// zatvoren skup komponenti (zatvoren prema sljedbenicima) tezine (broj gredica) u [n, 2n].
#include <bits/stdc++.h>
using namespace std;

int main() {
    int z;
    scanf("%d", &z);
    while (z--) {
        int n, q;
        scanf("%d %d", &n, &q);
        int N = 3 * n;
        // vrhovi: 0..N-1 gredice; ulazno stablo IN (list = gredica), izlazno stablo OUT (list = gredica)
        int sz = 1; while (sz < N) sz <<= 1;
        int IN = N, OUT = N + 2 * sz, AUX = N + 4 * sz;      // pocetni indeksi
        int V = AUX + q;
        vector<vector<int>> g(V);
        // IN stablo: dijete -> roditelj (iz gredice se dolazi do svakog cvora koji je pokriva)
        // OUT stablo: roditelj -> dijete (iz cvora se dolazi do svih gredica u njemu)
        for (int i = 1; i < sz; ++i) {
            g[IN + 2 * i].push_back(IN + i); g[IN + 2 * i + 1].push_back(IN + i);
            g[OUT + i].push_back(OUT + 2 * i); g[OUT + i].push_back(OUT + 2 * i + 1);
        }
        for (int i = 0; i < N; ++i) {
            g[i].push_back(IN + sz + i);       // gredica -> IN list
            g[OUT + sz + i].push_back(i);      // OUT list -> gredica
        }
        for (int t = 0; t < q; ++t) {
            int a, b, c, d;
            scanf("%d %d %d %d", &a, &b, &c, &d);
            int aux = AUX + t;
            // svaki IN cvor koji pokriva dio [a,b] -> aux -> svaki OUT cvor koji pokriva dio [c,d]
            for (int l = a - 1 + sz, r = b - 1 + sz + 1; l < r; l >>= 1, r >>= 1) {
                if (l & 1) g[IN + l].push_back(aux), ++l;
                if (r & 1) --r, g[IN + r].push_back(aux);
            }
            for (int l = c - 1 + sz, r = d - 1 + sz + 1; l < r; l >>= 1, r >>= 1) {
                if (l & 1) g[aux].push_back(OUT + l), ++l;
                if (r & 1) --r, g[aux].push_back(OUT + r);
            }
        }
        // iterativni Tarjan; komponente dobivamo u obrnutom topoloskom redu (ponor prvi)
        vector<int> idx(V, -1), low(V), comp(V, -1), st, it(V, 0);
        vector<char> onst(V, 0);
        int timer = 0, C = 0;
        for (int s = 0; s < V; ++s) {
            if (idx[s] != -1) continue;
            vector<int> call; call.push_back(s);
            idx[s] = low[s] = timer++; st.push_back(s); onst[s] = 1;
            while (!call.empty()) {
                int v = call.back();
                if (it[v] < (int)g[v].size()) {
                    int w = g[v][it[v]++];
                    if (idx[w] == -1) { idx[w] = low[w] = timer++; st.push_back(w); onst[w] = 1; call.push_back(w); }
                    else if (onst[w]) low[v] = min(low[v], idx[w]);
                } else {
                    if (low[v] == idx[v]) {
                        while (true) {
                            int w = st.back(); st.pop_back(); onst[w] = 0; comp[w] = C;
                            if (w == v) break;
                        }
                        ++C;
                    }
                    call.pop_back();
                    if (!call.empty()) low[call.back()] = min(low[call.back()], low[v]);
                }
            }
        }
        vector<int> tez(C, 0);                  // broj gredica u komponenti
        for (int i = 0; i < N; ++i) ++tez[comp[i]];
        vector<vector<int>> cg(C);              // graf komponenti (moguci duplikati - nije bitno)
        for (int v = 0; v < V; ++v) for (int w : g[v]) if (comp[v] != comp[w]) cg[comp[v]].push_back(comp[w]);
        vector<char> uzeto(N, 0);
        bool nasao = false;
        // 1) velika komponenta (tezina >= n): njezino zatvaranje mora imati tezinu <= 2n
        auto zatvaranje = [&](int c0, vector<char> &mark) {
            // vraca tezinu zatvaranja; mark oznacava komponente u zatvaranju
            long long w = 0; vector<int> stk = {c0}; mark[c0] = 1;
            while (!stk.empty()) {
                int c = stk.back(); stk.pop_back(); w += tez[c];
                for (int d : cg[c]) if (!mark[d]) { mark[d] = 1; stk.push_back(d); }
            }
            return w;
        };
        for (int c = 0; c < C && !nasao; ++c) {
            if (tez[c] < n) continue;
            vector<char> mark(C, 0);
            long long w = zatvaranje(c, mark);
            if (w <= 2 * n) {
                nasao = true;
                for (int i = 0; i < N; ++i) uzeto[i] = mark[comp[i]];
            }
        }
        if (!nasao) {
            // 2) komponente iz kojih se dolazi do neke velike su zabranjene; ostale (tezine < n)
            //    dodajemo u obrnutom topoloskom redu (indeks komponente raste = ponori prvi)
            vector<char> los(C, 0);
            for (int c = 0; c < C; ++c) {
                if (tez[c] >= n) los[c] = 1;
                for (int d : cg[c]) if (los[d]) los[c] = 1;   // sljedbenici imaju manji indeks
            }
            long long w = 0;
            vector<char> mark(C, 0);
            for (int c = 0; c < C && w < n; ++c)
                if (!los[c]) { mark[c] = 1; w += tez[c]; }
            if (w >= n && w <= 2 * n) {
                nasao = true;
                for (int i = 0; i < N; ++i) uzeto[i] = mark[comp[i]];
            }
        }
        if (!nasao) { printf("NIE\n"); continue; }
        string s(N, 'R');
        for (int i = 0; i < N; ++i) if (uzeto[i]) s[i] = 'F';
        printf("TAK\n%s\n", s.c_str());
    }
    return 0;
}
