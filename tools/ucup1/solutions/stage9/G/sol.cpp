// UCup 1, Stage 9 (Qingdao 2018), G. Repair the Artwork
// Uključivanje-isključivanje po skupu S dvojki koje "smiju ostati neobrisane" -> tretiramo ih kao 1
// (blokirane) s predznakom (-1)^|S|; ostale dvojke postaju 0. Za niz od 0 i 1 broj načina je k^m,
// k = broj intervala bez jedinica. DP f[i][j][par]: i = zadnja blokirana pozicija, j = broj intervala
// do sada, par = parnost |S|. Prijelaz na sljedeću blokiranu poziciju i' preskače samo nule i dvojke.
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007LL;

long long power(long long b, long long e) {
    long long r = 1; b %= MOD; if (b < 0) b += MOD;
    while (e) { if (e & 1) r = r * b % MOD; b = b * b % MOD; e >>= 1; }
    return r;
}

int main() {
    int T;
    scanf("%d", &T);
    while (T--) {
        int n; long long m;
        scanf("%d %lld", &n, &m);
        vector<int> a(n + 2, 1);           // a[0] = a[n+1] = 1 (rubne "blokade")
        for (int i = 1; i <= n; i++) scanf("%d", &a[i]);
        int J = n * (n + 1) / 2 + 1;       // najveći mogući broj intervala + 1
        // f[i][par][j]
        vector<array<vector<long long>, 2>> f(n + 2);
        for (int i = 0; i <= n + 1; i++) { f[i][0].assign(J, 0); f[i][1].assign(J, 0); }
        f[0][0][0] = 1;
        for (int i = 0; i <= n; i++) {
            int jmax = i * (i + 1) / 2;    // do pozicije i ne može biti više intervala
            for (int par = 0; par < 2; par++) {
                for (int j = 0; j <= jmax; j++) {
                    long long val = f[i][par][j];
                    if (!val) continue;
                    // sljedeća blokirana pozicija ip; između smiju biti samo 0 i 2 (2 -> 0)
                    for (int ip = i + 1; ip <= n + 1; ip++) {
                        int g = ip - i - 1;                 // duljina praznine
                        int nj = j + g * (g + 1) / 2;
                        if (a[ip] == 1) {                   // prava jedinica: parnost ista
                            f[ip][par][nj] = (f[ip][par][nj] + val) % MOD;
                            break;                          // preko jedinice se ne može
                        }
                        if (a[ip] == 2) {                   // dvojka u S: blokirana, predznak se mijenja
                            f[ip][par ^ 1][nj] = (f[ip][par ^ 1][nj] + val) % MOD;
                        }
                    }
                }
            }
        }
        long long ans = 0;
        for (int j = 0; j < J; j++) {
            long long d = (f[n + 1][0][j] - f[n + 1][1][j] + MOD) % MOD;
            if (d) ans = (ans + d * power(j, m)) % MOD;
        }
        printf("%lld\n", ans);
    }
    return 0;
}
