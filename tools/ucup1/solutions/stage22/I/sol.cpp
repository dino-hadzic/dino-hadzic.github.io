// I. Znamenka
// Stanja su brojevi n * 2^a 3^b 5^c 7^d <= N (7-glatki višekratnici od n), ima
// ih malo (~5*10^4).  Ako n ima k znamenki od kojih z nula:
//   E(n) = 1 + (1/k) ( z E(n) + sum_{d != 0} E(n(d+1)) )
//   =>  E(n) = ( k + sum_{d != 0} E(n(d+1)) ) / (k - z),   E(n) = 0 za n > N.
// Memoizacija po eksponentima (a,b,c,d) u 4D polju s "pečatom" testa.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
const ll MOD = 998244353;

ll mpow(ll b, ll e) { ll r = 1; b %= MOD; while (e) { if (e & 1) r = r * b % MOD; b = b * b % MOD; e >>= 1; } return r; }

const int MA = 61, MB = 39, MC = 27, MD = 23;
static ll memo[MA][MB][MC][MD];
static int stamp[MA][MB][MC][MD];
int cur;
ull N;
ll inv[20];

// eksponenti (2,3,5,7) faktora d+1 za d = 1..9
const int EX[10][4] = {{0,0,0,0},{1,0,0,0},{0,1,0,0},{2,0,0,0},{0,0,1,0},{1,1,0,0},{0,0,0,1},{3,0,0,0},{0,2,0,0},{1,0,1,0}};

ll E(ull n, int a, int b, int c, int d) {
    if (stamp[a][b][c][d] == cur) return memo[a][b][c][d];
    int k = 0, z = 0;
    ll sum = 0;
    for (ull t = n; t > 0; t /= 10) {
        int dig = (int)(t % 10);
        ++k;
        if (dig == 0) { ++z; continue; }
        ull mul = dig + 1;
        if (n > N / mul) continue;                    // n*(d+1) > N  =>  E = 0
        sum += E(n * mul, a + EX[dig][0], b + EX[dig][1], c + EX[dig][2], d + EX[dig][3]);
    }
    ll res = (k + sum) % MOD * inv[k - z] % MOD;
    stamp[a][b][c][d] = cur; memo[a][b][c][d] = res;
    return res;
}

int main() {
    for (int i = 1; i < 20; ++i) inv[i] = mpow(i, MOD - 2);
    int T; scanf("%d", &T);
    for (cur = 1; cur <= T; ++cur) {
        ull n; scanf("%llu %llu", &n, &N);
        printf("%lld\n", E(n, 0, 0, 0, 0));
    }
    return 0;
}
