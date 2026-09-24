// UCup 1, Stage 19 (NAC 2023), A. Allergen Testing
// Odgovor: najmanji k takav da (d+1)^k >= n.
#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    scanf("%d", &t);
    while (t--) {
        long long n, d;
        scanf("%lld %lld", &n, &d);
        int k = 0;
        __int128 moc = 1;                  // (d+1)^k, do 1e36 stane u __int128
        while (moc < n) {
            moc *= (__int128)(d + 1);
            ++k;
        }
        printf("%d\n", k);
    }
    return 0;
}
