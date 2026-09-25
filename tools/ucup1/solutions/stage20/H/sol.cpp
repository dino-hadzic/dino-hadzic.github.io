// UCup 1, Stage 20 (India), H. Treelection
// f_t(x) = najmanji broj glasova koji iz podstabla od x moraju "izaci" prema strogim precima,
// ako svaki cvor smije dobiti najvise t glasova:  f_t(x) = [x != 1] + max(0, sum_{y dijete} f_t(y) - t).
// z = najmanji t s f_t(1) = 0 (binarna pretraga). Neka je S_x broj strogih potomaka od x.
//   S_x > z  -> x moze pobijediti (u glasanju s kapacitetom z sve potomke preusmjerimo na x),
//   S_x < z  -> ne moze (x dobije <= z-1, a netko mora dobiti >= z),
//   S_x = z  -> svi potomci glasaju za x, ostali smiju <= z-1. Uz kapacitet z-1 neka je
//               e(y) = max(0, sum f_{z-1}(djeca) - (z-1)) "visak" u y. Podstablo od x tada izvozi
//               [x != 1] umjesto [x != 1] + e(x); smanjenje za 1 putuje prema korijenu samo kroz
//               pretke s e(y) >= 1 i mora u korijenu spustiti f(1) = e(1) s 1 na 0.
//               Dakle uvjet: e(x) >= 1, e(y) >= 1 za sve prave pretke y, i e(1) = 1.
#include <bits/stdc++.h>
using namespace std;

int n;
vector<int> par, sz;
vector<long long> f, suma;

// vraca f_t(1); usput puni f (za t = z-1 trebamo i "viskove")
long long izracunaj(long long t) {
    fill(suma.begin(), suma.end(), 0);
    for (int x = n; x >= 1; x--) {                 // P_x < x pa su djeca vec obradjena
        f[x] = (x != 1) + max(0LL, suma[x] - t);
        if (x != 1) suma[par[x]] += f[x];
    }
    return f[1];
}

int main() {
    int T;
    scanf("%d", &T);
    while (T--) {
        scanf("%d", &n);
        par.assign(n + 1, 0); sz.assign(n + 1, 1); f.assign(n + 1, 0); suma.assign(n + 1, 0);
        for (int i = 2; i <= n; i++) scanf("%d", &par[i]);
        for (int i = n; i >= 2; i--) sz[par[i]] += sz[i];
        long long lo = 1, hi = n - 1;                // t = n-1 sigurno radi (svi glasaju za korijen)
        while (lo < hi) {
            long long mid = (lo + hi) / 2;
            if (izracunaj(mid) == 0) hi = mid; else lo = mid + 1;
        }
        long long z = lo;
        izracunaj(z - 1);
        vector<char> visak(n + 1), dobar(n + 1);     // visak = e(y) >= 1; dobar = svi preci (ukljucivo) imaju visak
        for (int x = 1; x <= n; x++) {
            visak[x] = suma[x] - (z - 1) >= 1;
            dobar[x] = visak[x] && (x == 1 || dobar[par[x]]);
        }
        bool korijen1 = (f[1] == 1);
        string ans(n, '0');
        for (int x = 1; x <= n; x++) {
            long long S = sz[x] - 1;
            if (S > z) ans[x - 1] = '1';
            else if (S == z && korijen1 && dobar[x]) ans[x - 1] = '1';
        }
        puts(ans.c_str());
    }
    return 0;
}
