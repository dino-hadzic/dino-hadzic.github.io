// UCup 1, Stage 11 (EC-Final 2022), M. Dining Professors
// Doprinos svakog jela je neovisan: neljuto jelo daje 3, ljuto jelo na poziciji i
// daje c_i = b_{i-1} + b_i + b_{i+1} (ciklički). Ljuta jela stavljamo na a pozicija s najvećim c_i.
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, a;
    scanf("%d %d", &n, &a);
    vector<int> b(n);
    for (int &x : b) scanf("%d", &x);

    int cnt[4] = {0, 0, 0, 0};             // koliko pozicija ima c_i = 0, 1, 2, 3
    for (int i = 0; i < n; i++) {
        int c = b[(i + n - 1) % n] + b[i] + b[(i + 1) % n];
        cnt[c]++;
    }

    long long ans = 3LL * (n - a);         // neljuta jela zadovoljavaju sva tri profesora
    int left = a;                          // ljuta jela dijelimo od najvećeg c prema manjem
    for (int c = 3; c >= 0 && left > 0; c--) {
        int take = min(left, cnt[c]);
        ans += 1LL * take * c;
        left -= take;
    }
    printf("%lld\n", ans);
    return 0;
}
