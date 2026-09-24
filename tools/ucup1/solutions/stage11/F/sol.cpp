// UCup 1, Stage 11 (EC-Final 2022), F. Inversion (interaktivni)
// [p_l > p_r] = f(l,r) - f(l+1,r) - f(l,r-1) + f(l+1,r-1) (mod 2). Sortiranje umetanjem s binarnim
// pretraživanjem: pri umetanju p_i poredak prefiksa p_1..p_{i-1} je poznat, pa parnosti f(., i-1)
// računamo sami (BIT), a pitamo samo f(j, i) i f(j+1, i) -> ukupno <= 2 * sum ceil(log2 i) <= 39906.
//
// Lokalni način rada: ako prvi redak ulaza uz n sadrži i skrivenu permutaciju, program sam
// simulira suca (i broji upite); inače komunicira sa sucem standardnim protokolom.
#include <bits/stdc++.h>
using namespace std;

int n;
vector<int> hidden;           // prazno = pravi interaktivni način
vector<vector<char>> invpar;  // lokalni sudac: invpar[l][r] = parnost inverzija u p_l..p_r
long long queries = 0;

int ask(int l, int r) {
    if (l >= r) return 0;
    queries++;
    if (!hidden.empty()) {
        if (queries > 40000) { fprintf(stderr, "previše upita\n"); exit(1); }
        return invpar[l][r];
    }
    printf("? %d %d\n", l, r);
    fflush(stdout);
    int x; if (scanf("%d", &x) != 1) exit(0);
    return x;
}

int main() {
    // prvi redak: "n" ili "n p_1 ... p_n" (lokalna simulacija)
    string line;
    while (getline(cin, line) && line.find_first_not_of(" \t\r") == string::npos) {}
    { stringstream ss(line); ss >> n; int x; while (ss >> x) hidden.push_back(x); }
    if (!hidden.empty()) {
        hidden.insert(hidden.begin(), 0);   // 1-indeksiranje
        invpar.assign(n + 1, vector<char>(n + 1, 0));
        for (int l = 1; l <= n; l++) {      // za fiksni l širimo r i brojimo koliko je p_m > p_r, m u [l, r)
            vector<int> b(n + 1, 0);
            int cur = 0;
            for (int r = l; r <= n; r++) {
                int greaterCnt = r - l;
                for (int x = hidden[r]; x > 0; x -= x & -x) greaterCnt -= b[x];
                cur ^= (greaterCnt & 1);
                invpar[l][r] = cur;
                for (int x = hidden[r]; x <= n; x += x & -x) b[x]++;
            }
        }
    }

    vector<int> order;                  // indeksi prefiksa sortirani po vrijednosti (rastuće)
    vector<int> rk(n + 1);              // rang (1..i-1) indeksa unutar prefiksa
    vector<int> par(n + 2), cache(n + 2), bit(n + 2);

    for (int i = 1; i <= n; i++) {
        // par[l] = parnost broja inverzija unutar p_l..p_{i-1}, iz poznatog poretka prefiksa
        for (int j = 0; j < (int)order.size(); j++) rk[order[j]] = j + 1;
        fill(bit.begin(), bit.end(), 0);
        par[i] = 0;
        for (int l = i - 1; l >= 1; l--) {
            int smaller = 0;                                    // koliko je p_m < p_l za m u (l, i-1]
            for (int x = rk[l] - 1; x > 0; x -= x & -x) smaller += bit[x];
            for (int x = rk[l]; x <= n; x += x & -x) bit[x]++;
            par[l] = par[l + 1] ^ (smaller & 1);
        }
        fill(cache.begin(), cache.end(), -1);
        cache[i] = 0;                                           // f(i, i) = 0
        auto f_i = [&](int l) { if (cache[l] < 0) cache[l] = ask(l, i); return cache[l]; };
        // greater(j) = [p_j > p_i]
        auto greater = [&](int j) { return (f_i(j) ^ f_i(j + 1) ^ par[j] ^ par[j + 1]) & 1; };

        int lo = 0, hi = order.size();                          // p_i ide na poziciju lo u order
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (greater(order[mid])) hi = mid; else lo = mid + 1;
        }
        order.insert(order.begin() + lo, i);
    }

    vector<int> p(n + 1);
    for (int j = 0; j < n; j++) p[order[j]] = j + 1;
    if (!hidden.empty()) {
        for (int j = 1; j <= n; j++) printf("%d%c", p[j], j == n ? '\n' : ' ');
        fprintf(stderr, "upita: %lld\n", queries);
    } else {
        printf("!");
        for (int j = 1; j <= n; j++) printf(" %d", p[j]);
        printf("\n");
        fflush(stdout);
    }
    return 0;
}
