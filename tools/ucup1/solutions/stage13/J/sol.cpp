// UCup 1, Stage 13 (Um_nik mod 998244353 Contest), J. Kth Lex Min Min Min Subpalindromes
// m >= 3: optimalni nizovi su tocno oni u kojima se svaki element razlikuje od dva prethodna
//         (P = n), ima ih m(m-1)(m-2)^(n-2); k-ti se cita kao broj u mjesovitoj bazi.
// m = 2:  P = 2n-2; za n < 10 iscrpno, za n >= 10 tocno 12 nizova s periodom 6.
// m = 1:  jedini niz je 1 1 ... 1.
#include <bits/stdc++.h>
using namespace std;

const long long KAPA = 2000000000000000000LL;   // > 10^18, sve iznad toga tretiramo jednako

long long mnoziKapa(long long a, long long b) {
    __int128 p = (__int128)a * b;
    return p > KAPA ? KAPA : (long long)p;
}

int brojPalindroma(const string &s) {
    int n = s.size(), c = 0;
    for (int sr = 0; sr < n; ++sr) {                       // neparne duljine
        for (int l = sr, r = sr; l >= 0 && r < n && s[l] == s[r]; --l, ++r) ++c;
    }
    for (int sr = 0; sr + 1 < n; ++sr) {                   // parne duljine
        for (int l = sr, r = sr + 1; l >= 0 && r < n && s[l] == s[r]; --l, ++r) ++c;
    }
    return c;
}

void ispisi(const vector<int> &a) {
    string out;
    for (size_t i = 0; i < a.size(); ++i) {
        out += to_string(a[i]);
        out += (i + 1 == a.size() ? '\n' : ' ');
    }
    fputs(out.c_str(), stdout);
}

int main() {
    long long n, m, k;
    if (scanf("%lld %lld %lld", &n, &m, &k) != 3) return 0;

    if (m == 1) {
        if (k == 1) ispisi(vector<int>(n, 1));
        else printf("-1\n");
        return 0;
    }

    if (m == 2) {
        vector<string> kandidati;
        if (n < 10) {
            // Iscrpno: svih 2^n nizova, zadrzi one s najmanjim brojem palindroma.
            int best = INT_MAX;
            for (int maska = 0; maska < (1 << n); ++maska) {
                string s(n, '0');
                for (int i = 0; i < n; ++i) if (maska >> i & 1) s[i] = '1';
                int c = brojPalindroma(s);
                if (c < best) { best = c; kandidati.clear(); }
                if (c == best) kandidati.push_back(s);
            }
        } else {
            // 12 nizova s periodom 6: rotacije rijeci 001011 i njihovi komplementi.
            const string baza = "001011";
            for (int r = 0; r < 6; ++r) {
                string w = baza.substr(r) + baza.substr(0, r);
                string komplement = w;
                for (char &ch : komplement) ch = (ch == '0') ? '1' : '0';
                for (const string &per : {w, komplement}) {
                    string s;
                    while ((long long)s.size() < n) s += per;
                    s.resize(n);
                    kandidati.push_back(s);
                }
            }
        }
        sort(kandidati.begin(), kandidati.end());
        if (k > (long long)kandidati.size()) { printf("-1\n"); return 0; }
        vector<int> a(n);
        for (long long i = 0; i < n; ++i) a[i] = kandidati[k - 1][i] - '0' + 1;
        ispisi(a);
        return 0;
    }

    // m >= 3. Broj optimalnih nizova: m * (m-1) * (m-2)^(n-2), s kapom.
    long long ukupno = m;
    if (n >= 2) ukupno = mnoziKapa(ukupno, m - 1);
    for (long long i = 3; i <= n && ukupno < KAPA; ++i) ukupno = mnoziKapa(ukupno, m - 2);
    if (k > ukupno) { printf("-1\n"); return 0; }

    // pot[j] = (m-2)^j s kapom, za brojanje nastavaka.
    vector<long long> pot(n + 1, 1);
    for (long long j = 1; j <= n; ++j) pot[j] = mnoziKapa(pot[j - 1], m - 2);

    vector<int> a(n);
    k -= 1;                                                 // 0-indeksirano
    for (long long i = 0; i < n; ++i) {
        long long preostalo = n - 1 - i;                    // pozicija iza i-te
        long long nastavaka;                                // broj nastavaka za svaki dopusteni izbor na i
        if (i == 0) nastavaka = (n >= 2) ? mnoziKapa(m - 1, pot[preostalo - 1]) : 1;
        else nastavaka = pot[preostalo];
        long long idx = k / nastavaka;                      // redni broj medju dopustenim vrijednostima
        k -= idx * nastavaka;

        // Dopustene vrijednosti: sve osim a[i-1] i a[i-2] (koje su medusobno razlicite).
        int z1 = INT_MAX, z2 = INT_MAX;                     // zabranjene, z1 < z2
        if (i >= 1) z1 = a[i - 1];
        if (i >= 2) z2 = a[i - 2];
        if (z1 > z2) swap(z1, z2);
        long long v = idx + 1;
        if (v >= z1) ++v;
        if (v >= z2) ++v;
        a[i] = (int)v;
    }
    ispisi(a);
    return 0;
}
