// UCup 1, Stage 19 (NAC 2023), J. Repetitive String Invention
// Neka je T = X Y spoj dvaju podnizova. Ako je |X| = |Y|, mora biti X = Y. Ako su duljine
// različite, duži podniz ima oblik A B A, a kraći je B (u oba redoslijeda). Uz tablicu
// lcp[i][j] (najdulji zajednički prefiks sufiksa i i j): slučaj jednakih duljina brojimo
// po parovima početaka u O(n^2); u drugom slučaju fiksiramo B = s[a..b] unutar dužeg
// podniza, prefiksnim sumama prebrojimo početke c kraćeg podniza (lcp[a][c] >= |B|) i
// prolazimo po početku d dužeg podniza (uvjet lcp[d][b+1] >= a-d). Ukupno O(n^3).
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int MAXN = 805;
int lcp[MAXN][MAXN];
int pre[MAXN];

int main() {
    static char buf[MAXN];
    if (scanf("%s", buf) != 1) return 0;
    int n = strlen(buf);
    for (int i = n - 1; i >= 0; --i)
        for (int j = n - 1; j >= 0; --j)
            lcp[i][j] = (buf[i] == buf[j]) ? lcp[i + 1][j + 1] + 1 : 0;

    ll odgovor = 0;
    // 1) jednake duljine: X = Y, X počinje na a, Y na c > a, duljina h <= min(lcp, c-a)
    for (int a = 0; a < n; ++a)
        for (int c = a + 1; c < n; ++c)
            odgovor += min(lcp[a][c], c - a);

    // 2) različite duljine: duži podniz je A B A, kraći je B = s[a..b]
    for (int a = 0; a < n; ++a) {
        for (int b = a; b < n; ++b) {
            int duljB = b - a + 1;
            // pre[c] = broj početaka c' < c na kojima počinje kopija od B
            pre[0] = 0;
            for (int c = 0; c < n; ++c) pre[c + 1] = pre[c] + (lcp[a][c] >= duljB ? 1 : 0);
            // d = početak dužeg podniza, |A| = a - d, kraj e = b + (a - d)
            for (int d = a - 1; d >= 0; --d) {
                int duljA = a - d;
                int e = b + duljA;
                if (e >= n) break;
                if (lcp[d][b + 1] < duljA) continue;   // s[d..a-1] != s[b+1..e]
                // duži prvi: kraći počinje na c > e  ->  c u [e+1, n-1]
                odgovor += pre[n] - pre[e + 1];
                // kraći prvi: kraći završava prije d  ->  c u [0, d - duljB]
                if (d - duljB >= 0) odgovor += pre[d - duljB + 1];
            }
        }
    }
    printf("%lld\n", odgovor);
    return 0;
}
