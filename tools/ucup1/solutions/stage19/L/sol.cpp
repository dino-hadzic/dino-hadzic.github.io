// UCup 1, Stage 19 (NAC 2023), L. Splitting Pairs
// Neka je v(x) najveći p takav da 2^p | x. Za paran n stanje je gubitničko točno kad su sve
// hrpe neparne; za neparan n točno kad sve hrpe imaju istu vrijednost v(x). Ostala su
// stanja pobjednička (postoji potez u gubitničko stanje), pa je odgovor 1 upravo za njih.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int valuacija(ll x) {           // broj dvojki u rastavu od x
    int p = 0;
    while (x % 2 == 0) { x /= 2; ++p; }
    return p;
}

int main() {
    int t;
    if (scanf("%d", &t) != 1) return 0;
    while (t--) {
        int n;
        scanf("%d", &n);
        vector<ll> s(n);
        for (auto &x : s) scanf("%lld", &x);
        bool gubitnicko;
        if (n % 2 == 0) {
            gubitnicko = true;
            for (ll x : s) if (x % 2 == 0) gubitnicko = false;
        } else {
            int v0 = valuacija(s[0]);
            gubitnicko = true;
            for (ll x : s) if (valuacija(x) != v0) gubitnicko = false;
        }
        printf("%d\n", gubitnicko ? 0 : 1);
    }
    return 0;
}
