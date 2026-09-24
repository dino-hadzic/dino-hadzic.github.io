// UCup 1, Stage 15 (ZJCPC 2023), A. Turn on the Light  (interaktivni zadatak)
// Binarno pretraživanje intervala [l, r] uz brojače cl / cr upaljenih lampica lijevo od l,
// odnosno desno od r. Ako je cl != cr, upit u sredini m razlikuje sve tri mogućnosti
// (s < m, s = m, s > m); ako je cl == cr, prvo upitom na r „pokvarimo” ravnotežu.
//
// Lokalni način (samo za testiranje): ako prva linija ulaza sadrži i drugi broj s,
// program sam glumi suca; s >= 1 ispisuje transkript, s = 0 provjerava sve skrivene lampice.
#include <bits/stdc++.h>
using namespace std;

int n;
// --- lokalni sudac ---
bool lokalno = false;
int skriveno, brojUpita, lijevoUp, desnoUp;
vector<char> upaljena;
vector<int> upaljenePozicije;
bool transkript;

int upit(int x) {
    if (!lokalno) {
        printf("? %d\n", x);
        fflush(stdout);
        int odgovor;
        if (scanf("%d", &odgovor) != 1) exit(0);
        return odgovor;
    }
    ++brojUpita;
    if (!upaljena[x]) {
        upaljena[x] = 1;
        upaljenePozicije.push_back(x);
        if (x < skriveno) ++lijevoUp;
        else if (x > skriveno) ++desnoUp;
    }
    int odgovor = abs(lijevoUp - desnoUp);
    if (transkript) printf("? %d\n%d\n", x, odgovor);
    return odgovor;
}

int pronadji() {
    int l = 1, r = n, cl = 0, cr = 0;
    while (l < r) {
        if (cl == cr) {
            // upit na desnom kraju: 0 znači s = r, inače je s u [l, r-1] i cr raste
            if (upit(r) == 0) return r;
            --r; ++cr;
            continue;
        }
        int m = (l + r) / 2, d = cl - cr;  // d != 0 pa su |d-1|, |d|, |d+1| međusobno različiti
        int res = upit(m);
        if (res == abs(d)) return m;                 // s = m
        if (res == abs(d - 1)) { r = m - 1; ++cr; }  // s < m: m je upaljena desno od s
        else { l = m + 1; ++cl; }                    // s > m
    }
    return l;
}

int main() {
    char linija[64];
    if (!fgets(linija, sizeof linija, stdin)) return 0;
    int s = 0;
    int k = sscanf(linija, "%d %d", &n, &s);
    lokalno = (k == 2);
    if (!lokalno) {
        printf("! %d\n", pronadji());
        fflush(stdout);
        return 0;
    }
    if (s >= 1) {
        transkript = true;
        skriveno = s; upaljena.assign(n + 1, 0); brojUpita = lijevoUp = desnoUp = 0;
        printf("! %d\n", pronadji());
    } else {
        // provjeri sve skrivene lampice 1..n; ispiši najveći broj upita
        transkript = false;
        int maks = 0, krivo = 0;
        upaljena.assign(n + 1, 0);
        for (skriveno = 1; skriveno <= n; ++skriveno) {
            for (int x : upaljenePozicije) upaljena[x] = 0;
            upaljenePozicije.clear(); brojUpita = lijevoUp = desnoUp = 0;
            if (pronadji() != skriveno) ++krivo;
            maks = max(maks, brojUpita);
        }
        printf("sve %d krivo %d maksupita %d\n", n, krivo, maks);
    }
    return 0;
}
