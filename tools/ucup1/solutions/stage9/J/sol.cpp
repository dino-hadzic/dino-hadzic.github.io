// UCup 1, Stage 9 (Qingdao 2018), J. Books
// Knjige cijene 0 kupuju se uvijek. Ako je m = n -> Richman; ako je m < (broj nula) -> Impossible.
// Inače se kupuje prvih m - z knjiga pozitivne cijene (zbroj S); novac mora biti < najjeftinije
// preostale nekupljene knjige p, pa je najveći iznos S + p - 1.
#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    scanf("%d", &T);
    while (T--) {
        int n, m;
        scanf("%d %d", &n, &m);
        vector<long long> a(n);
        int nula = 0;
        for (auto &x : a) { scanf("%lld", &x); if (x == 0) nula++; }
        if (m == n) { puts("Richman"); continue; }
        if (m < nula) { puts("Impossible"); continue; }
        int treba = m - nula;                 // koliko knjiga pozitivne cijene kupuje
        long long S = 0, najmanja = LLONG_MAX;
        for (int i = 0; i < n; i++) {
            if (a[i] == 0) continue;
            if (treba > 0) { S += a[i]; treba--; }   // prvih m - z pozitivnih se kupuje
            else najmanja = min(najmanja, a[i]);    // ostale se ne smiju moći kupiti
        }
        printf("%lld\n", S + najmanja - 1);
    }
    return 0;
}
