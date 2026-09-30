// UCup 1, Stage 9 (Qingdao 2018), F. Tournament
// Uvjet je ekvivalentan komutiranju svih k savršenih sparivanja; orbite su velicine potencije 2,
// pa rjesenje postoji ako i samo ako je k < lowbit(n). Leksikografski najmanji raspored:
// u i-toj rundi vitez j (0-indeksirano) igra protiv j XOR i.
#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    scanf("%d", &T);
    while (T--) {
        int n, k;
        scanf("%d %d", &n, &k);
        int lowbit = n & (-n);
        if (k >= lowbit) { puts("Impossible"); continue; }
        string out;
        for (int i = 1; i <= k; i++) {
            for (int j = 0; j < n; j++) {
                if (j) out += ' ';
                out += to_string((j ^ i) + 1);
            }
            out += '\n';
        }
        fputs(out.c_str(), stdout);
    }
    return 0;
}
