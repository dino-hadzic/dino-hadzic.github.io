// K. water235
// Donja granica: opseg skupa ispunjenih ćelija nikad ne raste (nova ćelija ima
// >= 2 ispunjena susjeda pa mijenja opseg za 4 - 2*(broj susjeda) <= 0), na kraju
// je opseg 2(N+M), a na početku najviše 4c  =>  c >= ceil((N+M)/2).
// Konstrukcija: dijagonala kvadrata s x s (s = min(N,M)), a u zadnjem retku
// (ili stupcu) svaka druga ćelija počevši od kraja.
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    vector<string> a(n, string(m, '0'));
    int s = min(n, m), cnt = 0;
    for (int i = 0; i < s; ++i) { a[i][i] = '1'; ++cnt; }
    if (n <= m) {
        for (int j = m - 1; j >= s; j -= 2) { a[n - 1][j] = '1'; ++cnt; }
    } else {
        for (int i = n - 1; i >= s; i -= 2) { a[i][m - 1] = '1'; ++cnt; }
    }
    // cnt == ceil((n+m)/2)
    string out;
    out.reserve((size_t)n * (2 * m) + 16);
    out += to_string(cnt); out += '\n';
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) { out += a[i][j]; out += (j + 1 < m ? ' ' : '\n'); }
    }
    fwrite(out.data(), 1, out.size(), stdout);
    return 0;
}
