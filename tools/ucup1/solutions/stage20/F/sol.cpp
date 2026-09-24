// UCup 1, Stage 20 (India), F. Longest Strictly Increasing Sequence
// Nuzan uvjet: b_1 = 1 i b_{i+1} - b_i in {0, 1}. Ako vrijedi, a = b radi.
#include <bits/stdc++.h>
using namespace std;

// duljina najduljeg strogo rastuceg podniza svakog prefiksa (n <= 10, O(n^2))
vector<int> lisPrefiksa(const vector<int>& a) {
    int n = a.size();
    vector<int> dp(n), res(n);
    int best = 0;
    for (int i = 0; i < n; i++) {
        dp[i] = 1;
        for (int j = 0; j < i; j++)
            if (a[j] < a[i]) dp[i] = max(dp[i], dp[j] + 1);
        best = max(best, dp[i]);
        res[i] = best;
    }
    return res;
}

int main() {
    int t;
    scanf("%d", &t);
    while (t--) {
        int n;
        scanf("%d", &n);
        vector<int> b(n);
        for (int& x : b) scanf("%d", &x);
        // kandidat a = b; izravna provjera LIS-a svakog prefiksa
        if (lisPrefiksa(b) == b) {
            printf("YES\n");
            for (int i = 0; i < n; i++) printf("%d%c", b[i], i + 1 == n ? '\n' : ' ');
        } else {
            printf("NO\n");
        }
    }
    return 0;
}
