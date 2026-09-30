// UCup 1, Stage 9 (Qingdao 2018), D. Magic Multiplication
// Fiksiramo prvu znamenku a_1 (1..9). Tada je svaki umnožak a_1 * b_j jednoznačno "odgrizen" s početka C:
// ako je znamenka 0 -> b_j = 0; ako je jedna znamenka djeljiva s a_1 -> jednoznamenkasti umnožak
// (tada dvoznamenkasti nije moguć jer 10x > 9a_1); inače dvije znamenke. Tako dobijemo B,
// pa iz b_1 na isti način svaku a_i, a ostatak samo provjerimo. Najmanji a_1 koji uspije daje odgovor.
#include <bits/stdc++.h>
using namespace std;

// Odgrize umnožak d * y s pozicije pos u C; vraća y (0..9) ili -1 ako nije moguće.
int odgrizi(const string &c, int &pos, int d) {
    if (pos >= (int)c.size()) return -1;
    int x = c[pos] - '0';
    if (x == 0) { pos++; return 0; }
    if (x % d == 0) { pos++; return x / d; }      // x/d <= 9 uvijek jer x <= 9
    if (pos + 1 >= (int)c.size()) return -1;
    int xx = x * 10 + (c[pos + 1] - '0');
    if (xx % d == 0 && xx / d <= 9) { pos += 2; return xx / d; }
    return -1;
}

int main() {
    int T;
    scanf("%d", &T);
    while (T--) {
        int n, m;
        static char buf[200005];
        scanf("%d %d %s", &n, &m, buf);
        string c(buf);
        bool nadjeno = false;
        for (int a1 = 1; a1 <= 9 && !nadjeno; a1++) {
            int pos = 0;
            vector<int> A(n), B(m);
            A[0] = a1;
            bool ok = true;
            for (int j = 0; j < m && ok; j++) {
                B[j] = odgrizi(c, pos, a1);
                if (B[j] < 0) ok = false;
            }
            if (!ok || B[0] == 0) continue;          // B nema vodeću nulu
            for (int i = 1; i < n && ok; i++) {
                A[i] = odgrizi(c, pos, B[0]);        // prvi umnožak retka određuje a_i
                if (A[i] < 0) { ok = false; break; }
                for (int j = 1; j < m && ok; j++) {  // ostale umnoške samo provjeri
                    string s = to_string(A[i] * B[j]);
                    if (c.compare(pos, s.size(), s) != 0) ok = false;
                    else pos += s.size();
                }
            }
            if (!ok || pos != (int)c.size()) continue;
            nadjeno = true;
            for (int x : A) printf("%d", x);
            printf(" ");
            for (int x : B) printf("%d", x);
            printf("\n");
        }
        if (!nadjeno) puts("Impossible");
    }
    return 0;
}
