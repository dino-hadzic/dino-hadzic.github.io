// I. Heap – obrnuto poništavanje umetanja, O(n log n)
// Zadnje umetnuti v_n završio je na putu od pozicije n do korijena; svi elementi koje je
// "preskočio" strogo se razlikuju od njega (jednakost zaustavlja penjanje), pa je njegova
// pozicija p NAJDUBLJA pozicija na putu s vrijednošću v_n. Preskočeni elementi (ispod p na
// putu) morali su biti svi > v_n (min-hrpa, b=0) ili svi < v_n (max-hrpa, b=1), a roditelj od p
// mora zadovoljiti uvjet zaustavljanja. Stanje polja prije umetanja ne ovisi o izboru b_n,
// pa za svaki i neovisno biramo '0' ako je moguće.
#include <bits/stdc++.h>
using namespace std;

int main() {
    int T; scanf("%d", &T);
    while (T--) {
        int n; scanf("%d", &n);
        vector<long long> v(n + 1), a(n + 1);
        for (int i = 1; i <= n; i++) scanf("%lld", &v[i]);
        for (int i = 1; i <= n; i++) scanf("%lld", &a[i]);
        string b(n, '0');
        bool possible = true;
        for (int i = n; i >= 1 && possible; i--) {
            // put od i do korijena
            vector<int> path;
            for (int x = i; x >= 1; x /= 2) path.push_back(x);
            int pi = -1;                         // indeks u path najdublje pozicije s a = v_i
            for (int t = 0; t < (int)path.size(); t++) if (a[path[t]] == v[i]) { pi = t; break; }
            if (pi < 0) { possible = false; break; }
            int p = path[pi];
            bool canMin = true, canMax = true;   // b_i = '0' odnosno '1'
            for (int t = 0; t < pi; t++) {       // preskočeni elementi
                if (a[path[t]] <= v[i]) canMin = false;
                if (a[path[t]] >= v[i]) canMax = false;
            }
            if (p > 1) {                         // uvjet zaustavljanja kod roditelja
                if (a[p / 2] > v[i]) canMin = false;
                if (a[p / 2] < v[i]) canMax = false;
            }
            if (!canMin && !canMax) { possible = false; break; }
            b[i - 1] = canMin ? '0' : '1';
            // poništi umetanje: vrijednosti ispod p na putu pomaknemo za jedno gore
            for (int t = pi; t > 0; t--) a[path[t]] = a[path[t - 1]];
            a[i] = 0;                            // pozicija i više ne postoji
        }
        puts(possible ? b.c_str() : "Impossible");
    }
    return 0;
}
