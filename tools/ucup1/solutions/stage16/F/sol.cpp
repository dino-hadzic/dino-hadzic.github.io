// UCup 1, Stage 16, zadatak F: Classical Geometry Problem
// Rang tocke = broj koordinata strogo izmedu 0 i 255. Tocka ranga 0 je vrh kocke
// (jedan pritisak). Za rang >= 1: uzmemo vrh v kocke koji se od p razlikuje samo
// u "slobodnim" koordinatama (tamo je v = 0), povucemo polupravac iz v kroz p do
// ruba lica/kocke: tocka q = v + s(p - v), s = min 255 / p_i po slobodnim i.
// q ima strogo manji rang; rekurzivno dodemo do q, a zatim pritisnemo v tocno
// |q - p| sekundi, jer p lezi na segmentu od q prema v. Najvise 4 pritiska.
#include <bits/stdc++.h>
using namespace std;
typedef long double ld;

struct Potez { int c[3]; ld d; };

static bool rubna(ld x) { return x == 0 || x == 255; }

static ld udalj(const ld* a, const ld* b) {
    ld s = 0;
    for (int i = 0; i < 3; ++i) s += (a[i] - b[i]) * (a[i] - b[i]);
    return sqrtl(s);
}

// Vraca niz pritisaka koji iz crne (0,0,0) dovodi lampu tocno u p.
static void rijesi(const ld* p, vector<Potez>& out) {
    int rang = 0;
    for (int i = 0; i < 3; ++i) rang += !rubna(p[i]);
    if (rang == 0) {
        Potez m; ld nula[3] = {0, 0, 0};
        for (int i = 0; i < 3; ++i) m.c[i] = (int)p[i];
        m.d = udalj(nula, p);
        if (m.d > 0) out.push_back(m);  // za crnu nije potreban nijedan pritisak
        return;
    }
    // vrh v: rubne koordinate iste kao u p, slobodne postavljene na 0
    ld v[3], q[3];
    ld s = 1e18;
    for (int i = 0; i < 3; ++i) {
        v[i] = rubna(p[i]) ? p[i] : 0;
        if (!rubna(p[i])) s = min(s, (ld)255 / p[i]);
    }
    for (int i = 0; i < 3; ++i) q[i] = v[i] + s * (p[i] - v[i]);
    // numericki "zalijepi" koordinate koje su postale 255
    for (int i = 0; i < 3; ++i)
        if (fabsl(q[i] - 255) < 1e-9L) q[i] = 255;
    rijesi(q, out);          // q ima manji rang
    Potez m;
    for (int i = 0; i < 3; ++i) m.c[i] = (int)v[i];
    m.d = udalj(q, p);       // od q krecemo prema v i stanemo tocno u p
    out.push_back(m);
}

int main() {
    int t;
    if (scanf("%d", &t) != 1) return 0;
    while (t--) {
        int r, g, b;
        scanf("%d %d %d", &r, &g, &b);
        ld p[3] = {(ld)r, (ld)g, (ld)b};
        vector<Potez> potezi;
        rijesi(p, potezi);
        printf("%d\n", (int)potezi.size());
        for (const Potez& m : potezi)
            printf("%d %d %d %.12Lf\n", m.c[0], m.c[1], m.c[2], m.d);
    }
    return 0;
}
