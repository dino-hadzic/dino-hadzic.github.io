// UCup 1, Stage 17, H - This is not an Abnormal Team!
// Timovi = bridovi (par) ili "centar + 2 partnera" (trojka). Unija bridova
// svih timova je podgraf F u kojem svaki vrh ima stupanj <= 2; obratno, svaki
// takav F se rastavlja na parove i trojke (put s v vrhova -> v mod 2 trojki,
// ciklus -> 0 trojki). Ako C = broj pokrivenih vrhova, d2 = broj vrhova
// stupnja 2, tada je |F| = (C + d2)/2. Tok minimalne cijene s cijenama -M za
// prvu i +1 za drugu jedinicu kroz vrh minimizira -M*C + d2, tj. najprije
// maksimizira C, a zatim minimizira |F|.
// Uzastopni najkraći putovi imaju cijene -2M (savršeno sparivanje: nu puta),
// zatim -M+1 (pokrij jedan novi vrh, jedan stari dobije stupanj 2), a put
// cijene +2 se ne isplati. Zato: C* = 2*nu + (broj putova cijene -M+1),
// broj trojki = d2 = 2|F| - C* = C* - 2*nu, broj samaca = n1 + n2 - C*.
// Putovi cijene -M+1 su, uz potencijale d(v) (udaljenosti od izvora nakon
// sparivanja), točno dva odvojena tipa: (A) od nepokrivenih dječaka
// alternirajućim putovima do pokrivenih djevojaka (skup R dosegnutih vrhova,
// d = -M), (B) od pokrivenih dječaka izvan R do nepokrivenih djevojaka izvan
// R (d = 1). Dva su tipa na disjunktnim vrhovima pa oba rješavamo Dinicem.
#include <bits/stdc++.h>
using namespace std;

struct Dinic {
    struct E { int to, cap; };
    vector<E> e;
    vector<vector<int>> g;
    vector<int> lvl, it;
    int n, S, T;
    Dinic(int n_) : g(n_), lvl(n_), it(n_), n(n_) {}
    int add(int u, int v, int c) {
        g[u].push_back(e.size()); e.push_back({v, c});
        g[v].push_back(e.size()); e.push_back({u, 0});
        return e.size() - 2;
    }
    bool bfs() {
        fill(lvl.begin(), lvl.end(), -1);
        queue<int> q; q.push(S); lvl[S] = 0;
        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (int id : g[u]) if (e[id].cap > 0 && lvl[e[id].to] < 0) {
                lvl[e[id].to] = lvl[u] + 1; q.push(e[id].to);
            }
        }
        return lvl[T] >= 0;
    }
    int dfs(int u, int f) {
        if (u == T) return f;
        for (int &i = it[u]; i < (int)g[u].size(); i++) {
            int id = g[u][i], v = e[id].to;
            if (e[id].cap > 0 && lvl[v] == lvl[u] + 1) {
                int d = dfs(v, min(f, e[id].cap));
                if (d > 0) { e[id].cap -= d; e[id ^ 1].cap += d; return d; }
            }
        }
        return 0;
    }
    long long maxflow(int s, int t) {
        S = s; T = t;
        long long fl = 0;
        while (bfs()) {
            fill(it.begin(), it.end(), 0);
            while (int f = dfs(S, INT_MAX)) fl += f;
        }
        return fl;
    }
};

int main() {
    int n1, n2, m;
    scanf("%d %d %d", &n1, &n2, &m);
    vector<int> eu(m), ev(m);
    for (int i = 0; i < m; i++) { scanf("%d %d", &eu[i], &ev[i]); eu[i]--; ev[i]--; }

    // Faza 1: maksimalno sparivanje (Dinic na jediničnoj mreži)
    // čvorovi: 0..n1-1 dječaci, n1..n1+n2-1 djevojke, S, T
    int S = n1 + n2, T = S + 1;
    Dinic d1(T + 1);
    for (int b = 0; b < n1; b++) d1.add(S, b, 1);
    for (int g = 0; g < n2; g++) d1.add(n1 + g, T, 1);
    vector<int> eid(m);
    for (int i = 0; i < m; i++) eid[i] = d1.add(eu[i], n1 + ev[i], 1);
    long long nu = d1.maxflow(S, T);

    vector<int> matchB(n1, -1), matchG(n2, -1);  // partner u sparivanju ili -1
    vector<char> used(m, 0);
    for (int i = 0; i < m; i++) if (d1.e[eid[i]].cap == 0) {
        used[i] = 1; matchB[eu[i]] = ev[i]; matchG[ev[i]] = eu[i];
    }

    // R: vrhovi dosegnuti alternirajućim putovima iz nepokrivenih dječaka
    // (neiskorišten brid dječak->djevojka, iskorišten brid djevojka->dječak)
    vector<vector<int>> adjB(n1);
    for (int i = 0; i < m; i++) if (!used[i]) adjB[eu[i]].push_back(i);
    vector<char> inRB(n1, 0), inRG(n2, 0);
    queue<int> q;
    for (int b = 0; b < n1; b++) if (matchB[b] < 0) { inRB[b] = 1; q.push(b); }
    while (!q.empty()) {
        int b = q.front(); q.pop();
        for (int i : adjB[b]) {
            int g = ev[i];
            if (inRG[g]) continue;
            inRG[g] = 1;
            int b2 = matchG[g];  // nakon maksimalnog sparivanja svaka takva djevojka je pokrivena
            if (b2 >= 0 && !inRB[b2]) { inRB[b2] = 1; q.push(b2); }
        }
    }

    // Tip A: izvor -> nepokriveni dječaci (u R), neiskorišteni bridovi b->g,
    // iskorišteni bridovi g->b, pokrivene djevojke u R -> ponor.
    Dinic dA(T + 1);
    for (int b = 0; b < n1; b++) if (matchB[b] < 0) dA.add(S, b, 1);
    for (int g = 0; g < n2; g++) if (inRG[g]) dA.add(n1 + g, T, 1);
    for (int i = 0; i < m; i++) {
        if (!inRB[eu[i]] || !inRG[ev[i]]) continue;
        if (used[i]) dA.add(n1 + ev[i], eu[i], 1);
        else dA.add(eu[i], n1 + ev[i], 1);
    }
    long long fA = dA.maxflow(S, T);

    // Tip B: izvor -> pokriveni dječaci izvan R, bridovi samo među vrhovima
    // izvan R (neiskorišteni b->g, iskorišteni g->b), nepokrivene djevojke -> ponor.
    Dinic dB(T + 1);
    for (int b = 0; b < n1; b++) if (!inRB[b]) dB.add(S, b, 1);  // svi izvan R su pokriveni
    for (int g = 0; g < n2; g++) if (matchG[g] < 0) dB.add(n1 + g, T, 1);
    for (int i = 0; i < m; i++) {
        if (inRB[eu[i]] || inRG[ev[i]]) continue;
        if (used[i]) dB.add(n1 + ev[i], eu[i], 1);
        else dB.add(eu[i], n1 + ev[i], 1);
    }
    long long fB = dB.maxflow(S, T);

    long long C = 2 * nu + fA + fB;
    printf("%lld %lld\n", (long long)n1 + n2 - C, fA + fB);
    return 0;
}
