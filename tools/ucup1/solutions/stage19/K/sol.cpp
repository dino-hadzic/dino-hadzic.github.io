// UCup 1, Stage 19 (NAC 2023), K. Space Alignment
// Za svaki redak izračunamo dubinu p, broj tabulatora t i razmaka s. Za fiksni broj razmaka
// po tabulatoru k redak zahtijeva t*k + s = p*i za zajednički cijeli i > 0. Isprobamo
// k = 1, 2, ..., KMAX: ako je k određen dvama retcima, k = (p1*s2 - p2*s1)/(p2*t1 - p1*t2),
// pa je |k| <= 49*999 < 50000; inače zadovoljava neki k <= 49.
#include <bits/stdc++.h>
using namespace std;

const int KMAX = 50000;

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    vector<long long> t(n), s(n), p(n);
    int dubina = 0;
    char buf[2005];
    for (int j = 0; j < n; ++j) {
        if (scanf("%s", buf) != 1) return 0;
        int len = strlen(buf);
        t[j] = s[j] = 0;
        for (int q = 0; q + 1 < len; ++q) {
            if (buf[q] == 't') ++t[j]; else ++s[j];
        }
        if (buf[len - 1] == '{') { p[j] = dubina; ++dubina; }
        else { --dubina; p[j] = dubina; }   // zatvarajuća zagrada je na dubini bloka koji zatvara
    }
    for (int k = 1; k <= KMAX; ++k) {
        long long i = -1;                    // zajednička veličina uvlake, još nepoznata
        bool ok = true;
        for (int j = 0; j < n && ok; ++j) {
            long long uvlaka = t[j] * k + s[j];
            if (p[j] == 0) { ok = (uvlaka == 0); continue; }
            if (uvlaka % p[j] != 0) { ok = false; break; }
            long long kandidat = uvlaka / p[j];
            if (kandidat <= 0) { ok = false; break; }
            if (i == -1) i = kandidat;
            else if (i != kandidat) ok = false;
        }
        if (ok) { printf("%d\n", k); return 0; }
    }
    puts("-1");
    return 0;
}
