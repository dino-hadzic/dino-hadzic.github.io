// UCup 1, Stage 17, F - Chase Game 3
// Progonitelj (kreće se po lancu L2 = p_1 ... p_n) pobjeđuje iz svakog
// početnog stanja ako i samo ako su za svaki i vrhovi i i i+1 (susjedi na L1)
// udaljeni najviše 2 na lancu L2.
//  - Ako su i, i+1 udaljeni >= 3 na L2, njihova zatvorena L2-susjedstva su
//    disjunktna, pa bjegunac koji stoji na i uvijek može stati na onaj od
//    vrhova i, i+1 koji nije u susjedstvu progonitelja - nikad ne bude uhvaćen.
//  - Inače progonitelj svaki potez korakne za 1 prema bjeguncu po L2. Neka je
//    D = razlika L2-položaja (bjegunac - progonitelj) > 0. Bjegunac promijeni D
//    za najviše 2; ako D padne na -1, 0 ili 1, progonitelj ga odmah uhvati,
//    inače D ostaje >= 2 i progonitelj ga smanji za 1. Položaj progonitelja
//    na L2 tako strogo raste dok ne dođe do hvatanja, a ograničen je s n,
//    pa se hvatanje dogodi u konačno mnogo poteza.
#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    scanf("%d", &T);
    while (T--) {
        int n;
        scanf("%d", &n);
        vector<int> pos(n + 1);
        for (int i = 1; i <= n; i++) {
            int p;
            scanf("%d", &p);
            pos[p] = i;  // položaj vrha p na lancu L2
        }
        bool ok = true;
        for (int i = 1; i < n; i++)
            if (abs(pos[i] - pos[i + 1]) > 2) ok = false;
        puts(ok ? "Yes" : "No");
    }
    return 0;
}
