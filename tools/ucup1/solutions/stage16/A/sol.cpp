// UCup 1, Stage 16, zadatak A: Classical A+B Problem
// n = a + b, a i b repdigiti. Uz a >= b vrijedi |n| - 1 <= |a| <= |n|,
// pa postoji samo 18 kandidata za a; za svaki izračunamo b = n - a
// oduzimanjem nizova znamenki i provjerimo je li b repdigit.
#include <bits/stdc++.h>
using namespace std;

// Je li niz znamenki (bez vodećih nula) pozitivan repdigit?
static bool jeRepdigit(const string& s) {
    if (s.empty() || s[0] == '0') return false;
    for (char c : s)
        if (c != s[0]) return false;
    return true;
}

// Usporedba brojeva zapisanih kao nizovi znamenki bez vodećih nula: a < b ?
static bool manji(const string& a, const string& b) {
    if (a.size() != b.size()) return a.size() < b.size();
    return a < b;
}

// n - a za nizove znamenki, uz pretpostavku a <= n; rezultat bez vodećih nula.
static string oduzmi(const string& n, const string& a) {
    string r(n.size(), '0');
    int posudba = 0;
    for (int i = (int)n.size() - 1, j = (int)a.size() - 1; i >= 0; --i, --j) {
        int d = (n[i] - '0') - posudba - (j >= 0 ? a[j] - '0' : 0);
        if (d < 0) { d += 10; posudba = 1; } else posudba = 0;
        r[i] = char('0' + d);
    }
    size_t p = r.find_first_not_of('0');
    return p == string::npos ? "0" : r.substr(p);
}

int main() {
    int t;
    if (scanf("%d", &t) != 1) return 0;
    static char buf[5005];
    while (t--) {
        scanf("%s", buf);
        string n(buf);
        int L = (int)n.size();
        bool gotovo = false;
        // duljina od a: |n| ili |n| - 1
        for (int len = L; len >= max(1, L - 1) && !gotovo; --len) {
            for (int d = 1; d <= 9 && !gotovo; ++d) {
                string a(len, char('0' + d));
                if (!manji(a, n)) continue;      // treba a < n da bi b bio pozitivan
                string b = oduzmi(n, a);
                if (jeRepdigit(b)) {
                    printf("%s %s\n", a.c_str(), b.c_str());
                    gotovo = true;
                }
            }
        }
        // Po uvjetu zadatka rješenje uvijek postoji, pa se ovdje nikad ne dolazi.
    }
    return 0;
}
