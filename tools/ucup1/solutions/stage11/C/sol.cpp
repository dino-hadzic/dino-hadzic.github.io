// UCup 1, Stage 11 (EC-Final 2022), C. Best Carry Player 2
// DP po znamenkama od najniže prema najvišoj: dp[j][c][nz] = najmanji broj sastavljen od dosad
// obrađenih znamenaka y-a uz j prijenosa, prijenos c prema sljedećoj poziciji i nz = "y > 0".
// Na svakoj poziciji dovoljno je isprobati najmanju znamenku bez prijenosa i najmanju s prijenosom.
// Odgovor može imati do ~36 znamenaka (npr. x = 10^17, k = 18), zato __int128.
#include <bits/stdc++.h>
using namespace std;
typedef __int128 lll;

const int POS = 37;                 // 18 znamenaka x-a + do 18 prijenosa kroz vodeće nule (10^37 stane u __int128)
const lll INF = (lll)1 << 125;

void print128(lll v) {
    if (v == 0) { puts("0"); return; }
    string s;
    while (v > 0) { s += char('0' + (int)(v % 10)); v /= 10; }
    reverse(s.begin(), s.end());
    puts(s.c_str());
}

int main() {
    int T;
    scanf("%d", &T);
    while (T--) {
        long long x; int k;
        scanf("%lld %d", &x, &k);
        int dig[POS] = {0};
        { long long t = x; for (int i = 0; i < POS && t > 0; i++, t /= 10) dig[i] = t % 10; }

        static lll dp[2][19][2][2];
        for (int j = 0; j <= k; j++) for (int c = 0; c < 2; c++) for (int z = 0; z < 2; z++) dp[0][j][c][z] = INF;
        dp[0][0][0][0] = 0;
        lll pw = 1;                                   // 10^i
        int cur = 0;
        for (int i = 0; i < POS; i++, pw *= 10, cur ^= 1) {
            int nxt = cur ^ 1;
            for (int j = 0; j <= k; j++) for (int c = 0; c < 2; c++) for (int z = 0; z < 2; z++) dp[nxt][j][c][z] = INF;
            for (int j = 0; j <= k; j++) for (int c = 0; c < 2; c++) for (int z = 0; z < 2; z++) {
                lll v = dp[cur][j][c][z];
                if (v >= INF) continue;
                int s = dig[i] + c;
                if (s < 10) {
                    // bez prijenosa: znamenka 0
                    dp[nxt][j][0][z] = min(dp[nxt][j][0][z], v);
                    // bez prijenosa, ali y postaje pozitivan: znamenka 1 (ako ne izaziva prijenos)
                    if (!z && s <= 8) dp[nxt][j][0][1] = min(dp[nxt][j][0][1], v + pw);
                    // s prijenosom: najmanja znamenka 10 - s (<= 9 jer je s >= 1 ili s = 0 -> 10, nemoguće)
                    if (j < k && 10 - s <= 9) {
                        lll nv = v + (lll)(10 - s) * pw;
                        dp[nxt][j + 1][1][1] = min(dp[nxt][j + 1][1][1], nv);
                    }
                } else {
                    // s = 10 (x_i = 9, c = 1): prijenos nastaje i sa znamenkom 0
                    if (j < k) dp[nxt][j + 1][1][z] = min(dp[nxt][j + 1][1][z], v);
                }
            }
        }
        lll best = min(dp[cur][k][0][1], dp[cur][k][1][1]);
        if (best >= INF) puts("-1"); else print128(best);
    }
    return 0;
}
