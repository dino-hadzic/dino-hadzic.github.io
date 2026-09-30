// UCup 1, Stage 3 (AMPPZ 2022), M. Minor Evil
// Obrada susreta unatrag: osoba b_i koju jos treba ubiti gine na najkasnijem
// mogucem susretu, pod uvjetom da a_i tada ne mora biti mrtav.
#include <bits/stdc++.h>
using namespace std;

int main() {
    int z;
    scanf("%d", &z);
    while (z--) {
        int n, k;
        scanf("%d %d", &n, &k);
        vector<int> a(k), b(k);
        for (int i = 0; i < k; ++i) scanf("%d %d", &a[i], &b[i]);
        int s;
        scanf("%d", &s);
        vector<char> mora(n + 1, 0);           // mora[v] = v jos treba umrijeti na nekom ranijem susretu
        for (int i = 0; i < s; ++i) {
            int v;
            scanf("%d", &v);
            mora[v] = 1;
        }
        string odg(k, 'N');
        int preostalo = s;
        for (int i = k - 1; i >= 0; --i) {
            // b_i ubijamo ovdje ako to jos treba i ako a_i nije osoba koja mora umrijeti ranije
            if (mora[b[i]] && !mora[a[i]]) {
                mora[b[i]] = 0;
                odg[i] = 'T';
                --preostalo;
            }
        }
        if (preostalo == 0) printf("TAK\n%s\n", odg.c_str());
        else printf("NIE\n");
    }
    return 0;
}
