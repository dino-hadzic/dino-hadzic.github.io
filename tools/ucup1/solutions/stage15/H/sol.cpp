// UCup 1, Stage 15 (ZJCPC 2023), H. Classic: N Real DNA Pots
// Binarno pretraživanje po odgovoru w; provjera = najdulji neopadajući podniz niza y_i - w x_i.
#include <bits/stdc++.h>
using namespace std;
typedef long double ld;

int n, k;
vector<long long> x, y;

// Može li se odabrati k točaka tako da je svaki nagib >= w?
bool moguce(ld w) {
    vector<ld> kraj;  // kraj[len-1] = najmanja završna vrijednost neopadajućeg podniza duljine len
    kraj.reserve(n);
    for (int i = 0; i < n; ++i) {
        ld z = (ld)y[i] - w * (ld)x[i];
        auto it = upper_bound(kraj.begin(), kraj.end(), z);  // jednaki su dopušteni
        if (it == kraj.end()) kraj.push_back(z);
        else *it = z;
        if ((int)kraj.size() >= k) return true;
    }
    return false;
}

int main() {
    scanf("%d %d", &n, &k);
    x.resize(n); y.resize(n);
    for (int i = 0; i < n; ++i) scanf("%lld %lld", &x[i], &y[i]);
    ld lo = -1e9 - 1, hi = 1e9 + 1;   // |nagib| <= 1e9 jer je |dy| <= 1e9, dx >= 1
    for (int it = 0; it < 100; ++it) {  // fiksan broj iteracija, ne uvjet hi - lo < eps
        ld mid = (lo + hi) / 2;
        if (moguce(mid)) lo = mid; else hi = mid;
    }
    printf("%.9Lf\n", lo);
    return 0;
}
