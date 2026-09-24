// UCup 1, Stage 15 (ZJCPC 2023), B. Equation Discovering
// Gradimo sve izraze po složenosti c = 0..9 odozdo prema gore:
//   f[c] <- sin/cos(f[c-1]),  f[c] <- f[i] op f[j] za i + j + 2 = c.
// Svaki izraz pamtimo kao vektor vrijednosti u zadanim točkama x_1..x_n (i kao tekst);
// izraz koji negdje dijeli s |nazivnik| < 0.01 odbacujemo. Prvi izraz koji odgovara svim y ispisujemo.
#include <bits/stdc++.h>
using namespace std;

int n;
vector<double> X, Y;

struct Izraz {
    vector<double> v;   // vrijednosti u točkama
    string s;           // tekst
    bool binarni;       // je li korijen binarni operator (treba zagrade kad je operand)
};
vector<vector<Izraz>> f;

bool odgovara(const vector<double>& v) {
    for (int i = 0; i < n; ++i)
        if (fabs(v[i] - Y[i]) > 1e-3 * max(1.0, fabs(Y[i]))) return false;
    return true;
}

// operand u zagradama ako mu je korijen binarni operator (tako su prioritet i asocijativnost sigurni)
string operand(const Izraz& e) { return e.binarni ? "(" + e.s + ")" : e.s; }

// dodaj kandidata: ako odgovara podacima ispiši i završi; inače spremi u f[c] (za c < 9)
void kandidat(int c, Izraz&& e) {
    if (odgovara(e.v)) {
        puts(e.s.c_str());
        exit(0);
    }
    if (c < 9) f[c].push_back(move(e));
}

int main() {
    scanf("%d", &n);
    X.resize(n); Y.resize(n);
    for (int i = 0; i < n; ++i) scanf("%lf %lf", &X[i], &Y[i]);
    f.resize(10);
    kandidat(0, Izraz{X, "x", false});
    for (int c = 1; c <= 9; ++c) {
        // unarni: sin, cos nad izrazima složenosti c-1
        for (const Izraz& a : f[c - 1]) {
            Izraz s{vector<double>(n), "sin(" + a.s + ")", false};
            Izraz k{vector<double>(n), "cos(" + a.s + ")", false};
            for (int i = 0; i < n; ++i) { s.v[i] = sin(a.v[i]); k.v[i] = cos(a.v[i]); }
            kandidat(c, move(s));
            kandidat(c, move(k));
        }
        // binarni: f[i] op f[j], i + j + 2 = c
        for (int i = 0; i + 2 <= c; ++i) {
            int j = c - 2 - i;
            for (const Izraz& a : f[i])
                for (const Izraz& b : f[j]) {
                    const char* ops = "+-*/";
                    for (int o = 0; o < 4; ++o) {
                        Izraz e{vector<double>(n), operand(a) + ops[o] + operand(b), true};
                        bool ok = true;
                        for (int t = 0; t < n && ok; ++t) {
                            double p = a.v[t], q = b.v[t];
                            switch (o) {
                                case 0: e.v[t] = p + q; break;
                                case 1: e.v[t] = p - q; break;
                                case 2: e.v[t] = p * q; break;
                                default:
                                    if (fabs(q) < 0.01) ok = false;   // nedopušteno dijeljenje
                                    else e.v[t] = p / q;
                            }
                        }
                        if (ok) kandidat(c, move(e));
                    }
                }
        }
    }
    return 0;   // po uvjetu zadatka rješenje uvijek postoji
}
