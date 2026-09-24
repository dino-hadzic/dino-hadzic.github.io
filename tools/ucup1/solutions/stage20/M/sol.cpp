// UCup 1, Stage 20 (India), M. Graphs and Colors
// Svaka boja mora biti povezana na svih N vrhova => barem N-1 bridova po boji,
// pa je K <= N/2 nuzno. Konstrukcija za K0 = floor(N/2) boja (0-indeksirano):
//  - vrhovi 2k, 2k+1 su "predstavnici" boje k, brid (2k,2k+1) ima boju k;
//  - za i < j: (2i,2j) i (2i+1,2j+1) boje i, a (2i,2j+1) i (2i+1,2j) boje j.
// U boji i svaki je vrh susjedan s 2i ili 2i+1, a oni su susjedni => dijametar <= 3.
// Neparni N: zadnji vrh N-1 spojimo s vrhom v bojom floor(v/2).
// Manji K: boje >= K prebojimo u boju 0 (dodavanje bridova ne kvari dijametar).
#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    scanf("%d", &t);
    while (t--) {
        int n, k;
        scanf("%d %d", &n, &k);
        if (k > n / 2) {
            puts("NO");
            continue;
        }
        vector<vector<int>> boja(n, vector<int>(n, 0));
        int m = n / 2 * 2;   // parni dio
        for (int i = 0; i < m; i++)
            for (int j = i + 1; j < m; j++) {
                int a = i / 2, b = j / 2;
                if (a == b) boja[i][j] = a;
                else if (i % 2 == j % 2) boja[i][j] = a;   // "paralelni" brid -> manja grupa
                else boja[i][j] = b;                        // "ukrizeni" brid -> veca grupa
            }
        if (n % 2 == 1)
            for (int v = 0; v < n - 1; v++) boja[v][n - 1] = v / 2;
        puts("YES");
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                int c = boja[j][i];
                if (c >= k) c = 0;
                printf("%d%c", c + 1, j + 1 == i ? '\n' : ' ');
            }
        }
    }
    return 0;
}
