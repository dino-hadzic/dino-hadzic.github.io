// UCup 1, Stage 9 (Qingdao 2018), C. Flippy Sequence
// Razlika d = s XOR t. Broj maksimalnih blokova jedinica u d odlučuje sve:
//   0 blokova -> n(n+1)/2  (dvaput isti interval)
//   1 blok    -> 2(n-1)    (blok se reže na dva dijela ili produžuje pa "odreže")
//   2 bloka   -> 6         (tri načina da dva intervala daju dva bloka, puta 2 poretka)
//   >= 3      -> 0
#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    scanf("%d", &T);
    static char s[1000005], t[1000005];
    while (T--) {
        int n;
        scanf("%d %s %s", &n, s, t);
        int blokova = 0;
        for (int i = 0; i < n; i++) {
            bool razl = s[i] != t[i];
            bool prije = i > 0 && s[i - 1] != t[i - 1];
            if (razl && !prije) blokova++;
        }
        long long ans;
        if (blokova == 0) ans = 1LL * n * (n + 1) / 2;
        else if (blokova == 1) ans = 2LL * (n - 1);
        else if (blokova == 2) ans = 6;
        else ans = 0;
        printf("%lld\n", ans);
    }
    return 0;
}
