// UCup 1, Stage 17, C - DFS Order 3
// Lema 1: posljednji vrh u DFS poretku je list.
// Lema 2: drugi vrh u DFS poretku susjed je prvoga (korijena).
// Zato: uzmemo posljednji još neuklonjeni vrh v iz D_1 (list preostalog
// stabla), njegov susjed je prvi neuklonjeni vrh iza v u D_v, ispišemo brid
// i uklonimo v. Kako obrisani vrhovi ne mijenjaju valjanost preostalih
// poredaka, postupak ponavljamo n-1 puta. Pokazivači se samo pomiču
// naprijed, pa je ukupno O(n^2) po testu.
#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    scanf("%d", &T);
    while (T--) {
        int n;
        scanf("%d", &n);
        vector<vector<int>> D(n + 1, vector<int>(n));
        for (int i = 1; i <= n; i++)
            for (int j = 0; j < n; j++) scanf("%d", &D[i][j]);
        vector<char> uklonjen(n + 1, 0);
        vector<int> pok(n + 1, 1);  // pok[v]: sljedeći kandidat za susjeda u D_v
        int kraj = n - 1;           // pokazivač na kraj D_1
        for (int korak = 0; korak < n - 1; korak++) {
            while (uklonjen[D[1][kraj]]) kraj--;
            int v = D[1][kraj];
            while (uklonjen[D[v][pok[v]]]) pok[v]++;
            int u = D[v][pok[v]];
            printf("%d %d\n", v, u);
            uklonjen[v] = 1;
        }
    }
    return 0;
}
