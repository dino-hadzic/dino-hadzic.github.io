// UCup 1, Stage 18, B: Path Planning – 2. rješenje (inkrementalno, bez binarnog pretraživanja)
// Ćelije dodajemo redom vrijednosti 0, 1, 2, ... u uređeni skup poredan po (redak, stupac).
// Skup ćelija leži na jednom monotonom putu akko su u tom poretku stupci nepadajući;
// pri umetanju nove ćelije dovoljno je usporediti je sa susjedima u skupu.
// Odgovor je broj ćelija koje smo uspjeli dodati prije prvog kršenja uvjeta.
#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    if (scanf("%d", &T) != 1) return 0;
    while (T--) {
        int n, m;
        if (scanf("%d %d", &n, &m) != 2) return 0;
        int N = n * m;
        vector<int> posR(N), posC(N);  // pozicija svake vrijednosti
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++) {
                int a;
                if (scanf("%d", &a) != 1) return 0;
                posR[a] = i;
                posC[a] = j;
            }
        set<pair<int, int>> s;  // dosad dodane ćelije, poredane po (redak, stupac)
        int ans = 0;
        for (int v = 0; v < N; v++) {
            pair<int, int> cur(posR[v], posC[v]);
            auto it = s.lower_bound(cur);  // prvi element veći od cur (cur još nije u skupu)
            // sljedbenik: mora imati stupac >= posC[v] (u istom retku to vrijedi automatski)
            if (it != s.end() && it->second < cur.second) break;
            // prethodnik: mora imati stupac <= posC[v]
            if (it != s.begin() && prev(it)->second > cur.second) break;
            s.insert(it, cur);
            ans = v + 1;
        }
        printf("%d\n", ans);
    }
    return 0;
}
