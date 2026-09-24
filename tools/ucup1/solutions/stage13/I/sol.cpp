// UCup 1, Stage 13 (Um_nik mod 998244353 Contest), I. SPPPSPSS.
// Postoji optimalan niz operacija u kojem se P i S izmjenjuju, pa isprobamo oba izmjenicna niza.
// Faza 1 (koraci k <= (n+1)/2): prefiks i sufiks se ne sijeku, stanje = "sortiraj najveci prefiks
//   i najveci sufiks", a sortiranost provjeravamo u O(1) preko prefiksnih maksimuma / sufiksnih minimuma.
// Faza 2: niz je spoj dva rastuca bloka; drzimo ga kao
//   [tocan prefiks 1..L] [A: rastuci ostatak prvog bloka] [B: rastuci ostatak drugog bloka] [tocan sufiks]
//   i svaka operacija samo odsijeca prefikse (P) ili sufikse (S) od A i B  => ukupno O(n).
#include <bits/stdc++.h>
using namespace std;

int n;
vector<int> p, prefMax, sufMin, krivih;   // krivih[i] = broj pozicija j <= i s p[j] != j

// tip(k, c): true = P (prefiks), false = S (sufiks); c bira koji od dva izmjenicna niza.
inline bool jeP(int k, int c) { return ((k + c) & 1) == 1; }

// Vraca najmanji broj operacija za izmjenicni niz c.
int rijesi(int c) {
    int M1 = (n + 1) / 2;                  // zadnji korak u kojem se prefiks i sufiks jos ne sijeku
    int a = 0, b = 0;                      // najveci sortirani prefiks / sufiks do sada
    for (int m = 0; m <= M1; ++m) {
        if (m >= 1) { if (jeP(m, c)) a = m; else b = m; }
        bool okPref = (prefMax[a] == a);
        bool okSuf = (b == 0) || (sufMin[n - b + 1] == n - b + 1);
        bool okSredina = (krivih[n - b] - krivih[a] == 0);
        if (okPref && okSuf && okSredina) return m;
    }

    // Stanje nakon koraka M1: prefiks duljine a sortiran, sufiks duljine b sortiran (a + b <= n).
    vector<int> q(n + 1);
    vector<char> oznaka(n + 1, 0);
    for (int i = 1; i <= a; ++i) oznaka[p[i]] = 1;
    for (int v = 1, i = 1; v <= n; ++v) if (oznaka[v]) { q[i++] = v; oznaka[v] = 0; }
    for (int i = a + 1; i <= n - b; ++i) q[i] = p[i];
    for (int i = n - b + 1; i <= n; ++i) oznaka[p[i]] = 1;
    for (int v = 1, i = n - b + 1; v <= n; ++v) if (oznaka[v]) { q[i++] = v; oznaka[v] = 0; }

    // Korak M1 + 1: prvi put se sijeku; nakon njega imamo dva rastuca bloka duljina x i n - x.
    int k = M1 + 1;
    int x = jeP(k, c) ? k : n - k;
    vector<int> arr(n + 1);
    for (int i = 1; i <= x; ++i) oznaka[q[i]] = 1;
    for (int v = 1, i = 1, j = x + 1; v <= n; ++v) {
        if (oznaka[v]) arr[i++] = v; else arr[j++] = v;
    }
    int L = 0, R = 0;
    while (L < n && arr[L + 1] == L + 1) ++L;
    if (L == n) return k;
    while (arr[n - R] == n - R) ++R;
    int loA = L + 1, hiA = x, loB = x + 1, hiB = n - R;   // A = arr[loA..hiA], B = arr[loB..hiB]

    for (k = M1 + 2; ; ++k) {
        if (jeP(k, c)) {
            int duljinaA = hiA - loA + 1;
            int j = k - (L + duljinaA);               // koliko elemenata B ulazi u prefiks
            if (j <= 0) continue;
            if (j >= hiB - loB + 1) return k;          // cijeli B se spaja => sve sortirano
            int v = arr[loB + j];                      // najmanji element koji ostaje u B
            loB += j;
            while (loA <= hiA && arr[loA] < v) ++loA;  // ti elementi A postaju tocni
            L = v - 1;
        } else {
            int duljinaB = hiB - loB + 1;
            int j = k - (R + duljinaB);                // koliko elemenata A ulazi u sufiks
            if (j <= 0) continue;
            if (j >= hiA - loA + 1) return k;
            int v = arr[hiA - j];                      // najveci element koji ostaje u A
            hiA -= j;
            while (hiB >= loB && arr[hiB] > v) --hiB;
            R = n - v;
        }
    }
}

int main() {
    if (scanf("%d", &n) != 1) return 0;
    p.assign(n + 2, 0);
    for (int i = 1; i <= n; ++i) scanf("%d", &p[i]);
    prefMax.assign(n + 1, 0); sufMin.assign(n + 2, n + 1); krivih.assign(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        prefMax[i] = max(prefMax[i - 1], p[i]);
        krivih[i] = krivih[i - 1] + (p[i] != i);
    }
    for (int i = n; i >= 1; --i) sufMin[i] = min(sufMin[i + 1], p[i]);

    int m0 = rijesi(0), m1 = rijesi(1);
    int c = (m1 <= m0) ? 1 : 0;                        // c = 1: niz pocinje sa S (kao u primjerima)
    int m = min(m0, m1);
    string s;
    s.reserve(m + 1);
    for (int k = 1; k <= m; ++k) s += jeP(k, c) ? 'P' : 'S';
    s += '.';
    puts(s.c_str());
    return 0;
}
