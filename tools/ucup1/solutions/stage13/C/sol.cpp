// UCup 1, Stage 13 (Um_nik mod 998244353 Contest), C. Record Parity
// Odgovor: (-1)^k * C(m, k), gdje je m broj sufiksnih minimuma permutacije.
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 998244353;

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

int main() {
    int n, k;
    if (scanf("%d %d", &n, &k) != 2) return 0;
    vector<int> p(n);
    for (int &x : p) scanf("%d", &x);

    // Element ostaje nakon svih izbacivanja ako i samo ako je manji od svega desno od sebe.
    int m = 0;
    int minDesno = INT_MAX;
    for (int i = n - 1; i >= 0; --i) {
        if (p[i] < minDesno) {
            ++m;
            minDesno = p[i];
        }
    }

    if (k > m) {
        printf("0\n");
        return 0;
    }

    // C(m, k) preko faktorijela i inverza (m <= 10^6).
    vector<long long> fakt(m + 1, 1);
    for (int i = 1; i <= m; ++i) fakt[i] = fakt[i - 1] * i % MOD;
    long long binom = fakt[m] * potencija(fakt[k], MOD - 2) % MOD * potencija(fakt[m - k], MOD - 2) % MOD;

    long long odgovor = (k % 2 == 0) ? binom : (MOD - binom) % MOD;
    printf("%lld\n", odgovor);
    return 0;
}
