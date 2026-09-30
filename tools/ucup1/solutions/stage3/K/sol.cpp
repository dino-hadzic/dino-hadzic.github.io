// UCup 1, Stage 3 (AMPPZ 2022), K. Kooky Tic-Tac-Toe
// Zavrsna pozicija je moguca ako: |#x-#o|<=1; nitko ne pobjeduje i ploca je puna (remi),
// ili pobjeduje tocno jedan igrac P, P je odigrao zadnji potez (#P >= #Q) i postoji
// P-ovo polje koje lezi na SVIM pobjednickim linijama P-a (to je zadnji potez).
#include <bits/stdc++.h>
using namespace std;

int n, k;
vector<string> b;

// vraca skup polja (bitmaska) koja su na svim linijama simbola c; broj linija u cnt
long long presjek(char c, int &cnt) {
    int dx[4] = {0, 1, 1, 1}, dy[4] = {1, 0, 1, -1};
    long long all = (1LL << (n * n)) - 1, res = all;
    cnt = 0;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            for (int d = 0; d < 4; ++d) {
                int ei = i + (k - 1) * dx[d], ej = j + (k - 1) * dy[d];
                if (ei < 0 || ei >= n || ej < 0 || ej >= n) continue;
                long long m = 0; bool ok = true;
                for (int t = 0; t < k; ++t) {
                    int x = i + t * dx[d], y = j + t * dy[d];
                    if (b[x][y] != c) { ok = false; break; }
                    m |= 1LL << (x * n + y);
                }
                if (ok) { ++cnt; res &= m; }
            }
    return cnt ? res : 0;
}

int main() {
    int z;
    scanf("%d", &z);
    while (z--) {
        scanf("%d %d", &n, &k);
        b.assign(n, "");
        static char buf[16];
        for (int i = 0; i < n; ++i) { scanf("%s", buf); b[i] = buf; }
        int cx = 0, co = 0;
        for (auto &r : b) for (char c : r) { cx += c == 'x'; co += c == 'o'; }
        int lx, lo;
        long long px = presjek('x', lx), po = presjek('o', lo);
        char zadnji = 0; int last = -1;          // simbol i polje zadnjeg poteza
        bool ok = abs(cx - co) <= 1 && cx + co > 0;
        if (ok) {
            if (lx && lo) ok = false;                          // oba pobjeduju - nemoguce
            else if (!lx && !lo) {
                if (cx + co != n * n) ok = false;              // remi samo na punoj ploci
                else zadnji = (cx >= co) ? 'x' : 'o';          // pocinje onaj s vise znakova (ili bilo tko)
            } else {
                char P = lx ? 'x' : 'o';
                int cP = lx ? cx : co, cQ = lx ? co : cx;
                long long pres = lx ? px : po;
                if (cP < cQ || pres == 0) ok = false;
                else { zadnji = P; last = __builtin_ctzll(pres); }
            }
        }
        if (!ok) { printf("NIE\n"); continue; }
        // redoslijed: naizmjence, zadnji potez = 'zadnji' (za pobjednika bas polje last)
        vector<int> X, O;
        for (int i = 0; i < n * n; ++i) {
            if (i == last) continue;
            if (b[i / n][i % n] == 'x') X.push_back(i);
            else if (b[i / n][i % n] == 'o') O.push_back(i);
        }
        if (last >= 0) (zadnji == 'x' ? X : O).push_back(last);   // zadnji potez na kraj svog niza
        // ako je zadnji 'x', x-ovi zauzimaju pozicije ..., a prvi je onaj s vise znakova
        vector<int> red;
        char prvi = (cx > co) ? 'x' : (co > cx ? 'o' : (zadnji == 'x' ? 'o' : 'x'));
        size_t ix = 0, io = 0;
        for (int t = 0; t < cx + co; ++t) {
            char c = ((t % 2 == 0) == (prvi == 'x')) ? 'x' : 'o';
            red.push_back(c == 'x' ? X[ix++] : O[io++]);
        }
        printf("TAK\n");
        for (int c : red) printf("%d %d\n", c / n + 1, c % n + 1);
    }
    return 0;
}
