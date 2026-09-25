// UCup 1, Stage 17, L - Completely Multiplicative Function
// f je određena vrijednostima na prostim brojevima. Zbroj k znači da je
// (n+k)/2 vrijednosti +1, pa n+k mora biti paran.
// Veliki n (n >= 200): svim prostima p <= sqrt(n) dodijelimo +1. Tada je
// f(i) = +1 za sve i bez prostog faktora > sqrt(n), a prosti p > sqrt(n)
// dijeli točno floor(n/p) brojeva do n (p*m, m < sqrt(n)), i svaki takav broj
// ima f = f(p). Postaviti f(p) = -1 smanjuje zbroj za 2*floor(n/p). Treba
// smanjiti broj jedinica za D = (n-k)/2: greedy po prostima silaznog
// floor(n/p) ("uzmi ako stane"). Uspjeh je zajamčen: ukupni kapacitet
// (broj brojeva s velikim prostim faktorom) je > n/2 >= D, a nakon prvog
// preskočenog primjerka težine w ostatak je < w <= sqrt(n), što pokrivaju
// prosti u (n/2, n] težine 1 (ima ih više od sqrt(n) za n >= 200).
// Mali n (n < 200): iscrpno probamo svih 2^6 dodjela za proste 2..13, a za
// svaki veći prosti p vrijednost f(p) bira predznak doprinosa S(n/p),
// S(x) = f(1)+...+f(x); dostižne zbrojeve nađemo bitset-DP-om (subset sum).
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1000000;
const int SMALL = 200;
int lp[MAXN + 1];
vector<int> primes;
int fval[MAXN + 1];

// za male n: koja dodjela malih prostih (maska) daje zbroj k; -1 ako nijedna
signed char smallSol[SMALL][SMALL + 1];
const int SP[6] = {2, 3, 5, 7, 11, 13};

// izgradi f za mali n uz masku malih prostih; vrati doprinose velikih prostih
void buildSmall(int n, int mask, vector<int> &bigp, vector<int> &contrib, int &base) {
    fval[1] = 1;
    for (int i = 2; i <= n; i++) {
        int p = lp[i];
        if (i == p) {
            int idx = -1;
            for (int t = 0; t < 6; t++) if (SP[t] == p) idx = t;
            fval[i] = (idx >= 0) ? ((mask >> idx & 1) ? -1 : 1) : 1;  // veliki prosti privremeno +1
        } else fval[i] = fval[p] * fval[i / p];
    }
    // prefiksni zbrojevi S(x) za x < 17 (svi takvi brojevi su "mali")
    int S[20];
    S[0] = 0;
    for (int x = 1; x < 20 && x <= n; x++) S[x] = S[x - 1] + fval[x];
    base = 0;
    for (int i = 1; i <= n; i++) {
        bool hasBig = false;  // ima li i prosti faktor >= 17 (najviše jedan, jer je 17^2 > n)
        for (int j = i; j > 1; j /= lp[j]) if (lp[j] >= 17) hasBig = true;
        if (!hasBig) base += fval[i];
    }
    bigp.clear(); contrib.clear();
    for (int p : primes) {
        if (p > n) break;
        if (p >= 17) { bigp.push_back(p); contrib.push_back(S[n / p]); }
    }
}

void precomputeSmall() {
    for (int n = 1; n < SMALL; n++) {
        for (int k = 0; k <= n; k++) smallSol[n][k] = -1;
        for (int mask = 0; mask < 64; mask++) {
            vector<int> bigp, contrib; int base;
            buildSmall(n, mask, bigp, contrib, base);
            // dostižni zbrojevi: base + sum ±contrib, pomak +n za nenegativne indekse... koristimo bitset s pomakom 2n
            bitset<1024> reach;
            reach[base + 2 * n] = 1;
            for (int c : contrib) {
                int a = abs(c);
                reach = (reach << a) | (reach >> a);
            }
            for (int k = 0; k <= n; k++)
                if (smallSol[n][k] < 0 && reach[k + 2 * n]) smallSol[n][k] = mask;
        }
    }
}

void solveSmall(int n, int k) {
    int mask = smallSol[n][k];
    vector<int> bigp, contrib; int base;
    buildSmall(n, mask, bigp, contrib, base);
    // rekonstrukcija subset-suma: DP unaprijed po prostima, pa unatrag
    int m = bigp.size();
    vector<bitset<1024>> reach(m + 1);
    reach[0][base + 2 * n] = 1;
    for (int i = 0; i < m; i++) {
        int a = abs(contrib[i]);
        reach[i + 1] = (reach[i] << a) | (reach[i] >> a);
    }
    int cur = k + 2 * n;
    for (int i = m - 1; i >= 0; i--) {
        int c = contrib[i];
        // f(p) = +1 daje doprinos +c, f(p) = -1 daje -c
        if (cur - c >= 0 && cur - c < 1024 && reach[i][cur - c]) { fval[bigp[i]] = 1; cur -= c; }
        else { fval[bigp[i]] = -1; cur += c; }
    }
    // ponovno izračunaj f na složenim brojevima (sada s pravim f na velikim prostima)
    for (int i = 2; i <= n; i++) if (lp[i] != i) fval[i] = fval[lp[i]] * fval[i / lp[i]];
}

void solveBig(int n, int k) {
    long long D = (n - k) / 2;  // koliko jedinica treba pretvoriti u -1
    int s = 1;
    while ((long long)(s + 1) * (s + 1) <= n) s++;  // s = floor(sqrt(n))
    for (int p : primes) {
        if (p > n) break;
        fval[p] = 1;
    }
    // prosti > sqrt(n) silazno po težini floor(n/p) = uzlazno po p
    for (int p : primes) {
        if (p > n) break;
        if (p <= s) continue;
        int w = n / p;
        if (w <= D) { fval[p] = -1; D -= w; }
    }
    assert(D == 0);
    fval[1] = 1;
    for (int i = 2; i <= n; i++) if (lp[i] != i) fval[i] = fval[lp[i]] * fval[i / lp[i]];
}

int main() {
    for (int i = 2; i <= MAXN; i++) {
        if (!lp[i]) { lp[i] = i; primes.push_back(i); }
        for (int p : primes) {
            if (p > lp[i] || (long long)p * i > MAXN) break;
            lp[p * i] = p;
        }
    }
    precomputeSmall();
    int T;
    scanf("%d", &T);
    string out;
    char buf[8];
    while (T--) {
        int n, k;
        scanf("%d %d", &n, &k);
        if ((n + k) % 2 != 0 || (n < SMALL && smallSol[n][k] < 0)) {
            out += "-1\n";
            continue;
        }
        if (n < SMALL) solveSmall(n, k);
        else solveBig(n, k);
        for (int i = 1; i <= n; i++) {
            snprintf(buf, sizeof buf, "%d", fval[i]);
            out += buf;
            out += (i == n ? '\n' : ' ');
        }
    }
    fputs(out.c_str(), stdout);
    return 0;
}
