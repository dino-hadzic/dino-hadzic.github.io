// E. Computational Geometry – rotirajući pokazivač po konveksnom poligonu, O(n)
// Za b = i, c = i+k površina Q = (površina lanca b..c, fiksna za i) + površina trokuta abc.
// Kako se b pomiče u smjeru suprotnom od kazaljke, najbolji a (najdalji vrh od pravca bc
// na "drugoj" strani) također se pomiče monotono – udaljenost vrhova konveksnog poligona
// od pravca bc je unimodalna duž lanca c..b.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef __int128 lll;

int main() {
    int T; scanf("%d", &T);
    while (T--) {
        int n, k; scanf("%d %d", &n, &k);
        vector<ll> x(n), y(n);
        for (int i = 0; i < n; i++) scanf("%lld %lld", &x[i], &y[i]);
        auto cross = [&](int i, int j) {   // vektorski produkt p_i x p_j (indeksi mod n)
            i %= n; j %= n;
            return (lll)x[i] * y[j] - (lll)x[j] * y[i];
        };
        // pre[i] = suma cross(p_j, p_{j+1}) za j < i  (indeksi 0..2n)
        vector<lll> pre(2 * n + 1, 0);
        for (int i = 0; i < 2 * n; i++) pre[i + 1] = pre[i] + cross(i, i + 1);
        // tri(b, c, a) = dvostruka površina trokuta koji zatvara lanac: cross(c,a) + cross(a,b)
        auto tri = [&](int b, int c, int a) { return cross(c, a) + cross(a, b); };
        lll best = 0;
        int a = k + 1;                       // kandidat za a, uvijek u (c, b + n)
        for (int b = 0; b < n; b++) {
            int c = b + k;
            if (a < c + 1) a = c + 1;
            while (a + 1 <= b + n - 1 && tri(b, c, a + 1) >= tri(b, c, a)) a++;
            lll area2 = pre[c] - pre[b] + tri(b, c, a);
            if (area2 > best) best = area2;
        }
        ll whole = (ll)(best / 2);
        printf("%lld.%s\n", whole, (best % 2) ? "500000000000" : "000000000000");
    }
    return 0;
}
