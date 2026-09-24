// UCup 1, Stage 18, B: Path Planning
// Binarno pretraživanje odgovora: mex >= x je moguć točno onda kada sve ćelije
// s vrijednostima 0..x-1 leže na jednom monotonom (desno/dolje) putu, a to
// vrijedi ako i samo ako, gledano po redovima odozgo prema dolje, stupci tih
// ćelija nikad ne padaju.
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
        // provjera: mogu li vrijednosti 0..x-1 sve biti na jednom monotonom putu
        vector<int> lo(n), hi(n);
        auto ok = [&](int x) {
            fill(lo.begin(), lo.end(), INT_MAX);
            fill(hi.begin(), hi.end(), INT_MIN);
            for (int v = 0; v < x; v++) {
                lo[posR[v]] = min(lo[posR[v]], posC[v]);
                hi[posR[v]] = max(hi[posR[v]], posC[v]);
            }
            int last = 0;  // najveći stupac posjećen u prethodnim redovima
            for (int i = 0; i < n; i++) {
                if (lo[i] == INT_MAX) continue;
                if (lo[i] < last) return false;
                last = hi[i];
            }
            return true;
        };
        // ok je monoton: ako x radi, radi i svako manje x
        int L = 0, R = N;  // ok(0) uvijek vrijedi; tražimo najveći x s ok(x)
        while (L < R) {
            int mid = (L + R + 1) / 2;
            if (ok(mid)) L = mid;
            else R = mid - 1;
        }
        printf("%d\n", L);
    }
    return 0;
}
