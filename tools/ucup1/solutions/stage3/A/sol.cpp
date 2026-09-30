// UCup 1, Stage 3 (AMPPZ 2022), A. Aliases
// c <= 6 uvijek dostaje (10^6 >= n), pa je a+b+c <= 6: za svaku trojku po rastucem zbroju
// provjerimo je li najveca skupina jednakih slovnih prefiksa najvise 10^c.
#include <bits/stdc++.h>
using namespace std;

int main() {
    int z;
    scanf("%d", &z);
    static char b1[1500005], b2[1500005];
    while (z--) {
        int n;
        scanf("%d", &n);
        vector<string> ime(n), prez(n);
        for (int i = 0; i < n; ++i) {
            scanf("%s %s", b1, b2);
            ime[i] = b1; prez[i] = b2;
        }
        vector<unsigned long long> kljuc(n);
        long long pot10[8] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000};
        // najveca skupina za slovni dio (a,b): kodiramo do 6 slova kao broj u bazi 27 (tocno, bez hashiranja)
        auto najveca = [&](int a, int b) {
            for (int i = 0; i < n; ++i) {
                unsigned long long k = 0;
                int la = min<int>(a, ime[i].size()), lb = min<int>(b, prez[i].size());
                for (int j = 0; j < la; ++j) k = k * 27 + (ime[i][j] - 'a' + 1);
                for (int j = 0; j < lb; ++j) k = k * 27 + (prez[i][j] - 'a' + 1);
                kljuc[i] = k;
            }
            sort(kljuc.begin(), kljuc.end());
            long long best = 1, cur = 1;
            for (int i = 1; i < n; ++i) {
                cur = (kljuc[i] == kljuc[i - 1]) ? cur + 1 : 1;
                best = max(best, cur);
            }
            return best;
        };
        bool gotovo = false;
        for (int s = 1; s <= 7 && !gotovo; ++s)
            for (int a = 0; a <= s && !gotovo; ++a)
                for (int b = 0; a + b <= s && !gotovo; ++b) {
                    int c = s - a - b;
                    if (najveca(a, b) <= pot10[c]) {
                        printf("%d %d %d\n", a, b, c);
                        gotovo = true;
                    }
                }
    }
    return 0;
}
