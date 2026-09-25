// UCup 1, Stage 13 (Um_nik mod 998244353 Contest), D. XOR Determinant
// rank(A) <= 61 (60 bitova + vektor jedinica), pa je za n > 61 determinanta 0;
// inace Gaussova eliminacija modulo 998244353 u O(n^3).
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 998244353;
const int BITOVA = 60;

long long potencija(long long b, long long e) {
    long long r = 1;
    b %= MOD;
    while (e > 0) {
        if (e & 1) r = r * b % MOD;
        b = b * b % MOD;
        e >>= 1;
    }
    return r;
}

long long determinanta(vector<vector<long long>> a) {
    int n = a.size();
    long long det = 1;
    for (int stup = 0; stup < n; ++stup) {
        int piv = -1;
        for (int r = stup; r < n; ++r)
            if (a[r][stup] != 0) { piv = r; break; }
        if (piv == -1) return 0;
        if (piv != stup) {
            swap(a[piv], a[stup]);
            det = (MOD - det) % MOD;          // zamjena redaka mijenja predznak
        }
        det = det * a[stup][stup] % MOD;
        long long inv = potencija(a[stup][stup], MOD - 2);
        for (int r = stup + 1; r < n; ++r) {
            if (a[r][stup] == 0) continue;
            long long f = a[r][stup] * inv % MOD;
            for (int c = stup; c < n; ++c)
                a[r][c] = ((a[r][c] - f * a[stup][c]) % MOD + MOD) % MOD;
        }
    }
    return det;
}

int main() {
    int t;
    if (scanf("%d", &t) != 1) return 0;
    while (t--) {
        int n;
        scanf("%d", &n);
        vector<unsigned long long> b(n), c(n);
        for (auto &x : b) scanf("%llu", &x);
        for (auto &x : c) scanf("%llu", &x);
        if (n > BITOVA + 1) {                 // rang je najvise 61 < n
            printf("0\n");
            continue;
        }
        vector<vector<long long>> a(n, vector<long long>(n));
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                a[i][j] = (long long)((b[i] ^ c[j]) % MOD);
        printf("%lld\n", determinanta(a));
    }
    return 0;
}
