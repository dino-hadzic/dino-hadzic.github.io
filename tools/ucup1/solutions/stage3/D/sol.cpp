// UCup 1, Stage 3 (AMPPZ 2022), D. Dazzling Mountain
// d je dobar ako vidikovci (vrhovi s velicinom podstabla d) pokrivaju sve listove:
// podstabla iste velicine su disjunktna, pa zbrojimo listove po velicini podstabla.
#include <bits/stdc++.h>
using namespace std;

int main() {
    int z;
    scanf("%d", &z);
    while (z--) {
        int n;
        scanf("%d", &n);
        vector<int> head(n + 1, -1), nxt(2 * (n - 1)), to(2 * (n - 1));
        for (int i = 0; i < n - 1; ++i) {
            int a, b;
            scanf("%d %d", &a, &b);
            to[2 * i] = b; nxt[2 * i] = head[a]; head[a] = 2 * i;
            to[2 * i + 1] = a; nxt[2 * i + 1] = head[b]; head[b] = 2 * i + 1;
        }
        // BFS redoslijed od korijena 1, zatim obrada unatrag (bez rekurzije, n do 1e6)
        vector<int> red, par(n + 1, 0);
        red.reserve(n);
        red.push_back(1);
        par[1] = -1;
        for (size_t i = 0; i < red.size(); ++i) {
            int v = red[i];
            for (int e = head[v]; e != -1; e = nxt[e])
                if (to[e] != par[v]) { par[to[e]] = v; red.push_back(to[e]); }
        }
        vector<int> sz(n + 1, 1), listova(n + 1, 0);
        vector<long long> pokriveno(n + 1, 0);  // pokriveno[d] = listova u svim podstablima velicine d
        int ukupno = 0;
        for (int i = n - 1; i >= 0; --i) {
            int v = red[i];
            if (v != 1 && sz[v] == 1) { listova[v] = 1; ++ukupno; }
            pokriveno[sz[v]] += listova[v];
            if (v != 1) { sz[par[v]] += sz[v]; listova[par[v]] += listova[v]; }
        }
        vector<int> odg;
        for (int d = 1; d <= n; ++d)
            if (pokriveno[d] == ukupno) odg.push_back(d);
        printf("%d\n", (int)odg.size());
        for (size_t i = 0; i < odg.size(); ++i) printf("%d%c", odg[i], i + 1 == odg.size() ? '\n' : ' ');
    }
    return 0;
}
