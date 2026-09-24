// UCup 1, Stage 17, E - CCPC String
// CCPC niz c^{2t} p c^t ima točno jedno 'p'. Fiksiramo poziciju i tog 'p'
// (znak je 'p' ili '?'). Lijevo od i mora biti 2t znakova koji nisu 'p',
// desno t takvih. Ako je dl duljina maksimalnog bloka ne-'p' znakova
// neposredno lijevo od i, a dr desno, t može biti 1..min(dl/2, dr), pa je
// doprinos pozicije i jednak min(floor(dl/2), dr). Sve u O(|S|).
#include <bits/stdc++.h>
using namespace std;

static char buf[1000006];

int main() {
    int T;
    scanf("%d", &T);
    while (T--) {
        scanf("%s", buf);
        int n = strlen(buf);
        vector<int> L(n), R(n);  // duljina bloka ne-'p' znakova lijevo/desno od i
        for (int i = 0; i < n; i++)
            L[i] = (i > 0 && buf[i - 1] != 'p') ? L[i - 1] + 1 : 0;
        for (int i = n - 1; i >= 0; i--)
            R[i] = (i + 1 < n && buf[i + 1] != 'p') ? R[i + 1] + 1 : 0;
        long long ans = 0;
        for (int i = 0; i < n; i++)
            if (buf[i] != 'c') ans += min(L[i] / 2, R[i]);
        printf("%lld\n", ans);
    }
    return 0;
}
