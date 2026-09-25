// UCup 1, Stage 19 (NAC 2023), G. Frequent Flier
// Prozore obrađujemo po desnom kraju i = 1..n+m-1 (prozori koji počinju prije prvog i
// završavaju nakon zadnjeg mjeseca također vrijede, s 0 letova izvan [1, n]). Prozor
// [l, r] zahtijeva barem min(k, letovi u prozoru) plaćenih letova. Kad prozoru nedostaje
// plaćenih letova, plaćamo najnovije neplaćene letove u prozoru (argument zamjene:
// kasniji plaćeni let pokriva sve buduće prozore koje pokriva i raniji). Neplaćene letove
// držimo na stogu (mjesec, broj); vrh stoga je najnoviji mjesec.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    int n, m;
    ll k;
    if (scanf("%d %d %lld", &n, &m, &k) != 3) return 0;
    vector<ll> f(n + 1, 0), placeno(n + 1, 0);
    for (int i = 1; i <= n; ++i) if (scanf("%lld", &f[i]) != 1) return 0;

    vector<pair<int, ll>> stog;          // (mjesec, neplaćeni letovi), mjeseci rastu prema vrhu
    ll letoviProzor = 0, placenoProzor = 0, ukupno = 0;
    for (int i = 1; i <= n + m - 1; ++i) {
        if (i <= n) {
            letoviProzor += f[i];
            stog.push_back({i, f[i]});
        }
        if (i - m >= 1) {                // mjesec i-m izlazi iz prozora
            letoviProzor -= f[i - m];
            placenoProzor -= placeno[i - m];
        }
        ll potrebno = min(k, letoviProzor) - placenoProzor;
        while (potrebno > 0) {
            // vrh stoga je najnoviji neplaćeni let; on je sigurno unutar prozora,
            // jer bi inače svi letovi u prozoru već bili plaćeni i potrebno bi bilo 0
            auto &vrh = stog.back();
            int mj = vrh.first;
            ll uzmi = min(potrebno, vrh.second);
            vrh.second -= uzmi;
            placeno[mj] += uzmi;
            placenoProzor += uzmi;
            ukupno += uzmi;
            potrebno -= uzmi;
            if (vrh.second == 0) stog.pop_back();
        }
    }
    printf("%lld\n", ukupno);
    return 0;
}
