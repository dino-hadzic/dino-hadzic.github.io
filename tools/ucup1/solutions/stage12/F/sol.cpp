// F - Forestry (službeni pristup)
// Svaki brid neovisno režemo s vjerojatnošću 1/2; tražimo očekivani zbroj
// minimuma po komponentama, pomnožen s 2^(N-1).
// Ukorijenimo stablo. Za vrh v neka je Y_v = minimum komponente koja sadrži v
// unutar podstabla vrha v; dp[v][x] = P(Y_v = x). Nenulte vrijednosti x su samo
// vrijednosti A u podstablu, pa dp[v] držimo u dinamičkom segmentnom stablu
// nad komprimiranim vrijednostima (zbroj vjerojatnosti + zbroj x*p, lijeno
// množenje). Djecu spajamo "segment tree mergeom": ako su Y_1, Y_2 neovisni,
//   P(min = x) = P(Y_1 = x) P(Y_2 >= x) + P(Y_2 = x) P(Y_1 > x),
// što se u spuštanju po stablu izvodi kao množenje podstabla skalarom.
// Odgovor: E[zbroj minimuma] = sum_v P(v je najplići vrh svoje komponente) E[Y_v].
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int MOD = 998244353;

ll power(ll b, ll e) {
    ll r = 1; b %= MOD;
    for (; e; e >>= 1, b = b * b % MOD) if (e & 1) r = r * b % MOD;
    return r;
}

int K;                 // broj različitih vrijednosti
vector<int> vals;      // sortirane različite vrijednosti (mod p)
// čvorovi dinamičkog segmentnog stabla; indeks 0 je prazan čvor
vector<int> lc, rc, sm, sx, lz;  // sm = zbroj p, sx = zbroj x*p, lz = lijeni množitelj

int newNode() {
    lc.push_back(0); rc.push_back(0); sm.push_back(0); sx.push_back(0); lz.push_back(1);
    return (int)lc.size() - 1;
}
void apply(int t, int m) {
    if (!t || m == 1) return;
    sm[t] = (ll)sm[t] * m % MOD;
    sx[t] = (ll)sx[t] * m % MOD;
    lz[t] = (ll)lz[t] * m % MOD;
}
void push(int t) {
    if (lz[t] != 1) { apply(lc[t], lz[t]); apply(rc[t], lz[t]); lz[t] = 1; }
}
void pull(int t) {
    sm[t] = (sm[lc[t]] + sm[rc[t]]) % MOD;
    sx[t] = (sx[lc[t]] + sx[rc[t]]) % MOD;
}
// postavi vjerojatnost u točki pos na val (stvara put do lista)
int setPoint(int t, int l, int r, int pos, int val) {
    if (!t) t = newNode();
    if (l == r) {
        sm[t] = val;
        sx[t] = (ll)val * vals[pos] % MOD;
        return t;
    }
    push(t);
    int mid = (l + r) / 2;
    if (pos <= mid) lc[t] = setPoint(lc[t], l, mid, pos, val);
    else rc[t] = setPoint(rc[t], mid + 1, r, pos, val);
    pull(t);
    return t;
}
// zbroj vjerojatnosti na pozicijama < pos
int prefix(int t, int l, int r, int pos) {
    if (!t || pos <= l) return 0;
    if (r < pos) return sm[t];
    push(t);
    int mid = (l + r) / 2;
    return (prefix(lc[t], l, mid, pos) + prefix(rc[t], mid + 1, r, pos)) % MOD;
}
// izbaci sve pozicije > pos
int cut(int t, int l, int r, int pos) {
    if (!t || r <= pos) return t;
    if (l > pos) return 0;
    push(t);
    int mid = (l + r) / 2;
    if (pos <= mid) { lc[t] = cut(lc[t], l, mid, pos); rc[t] = 0; }
    else rc[t] = cut(rc[t], mid + 1, r, pos);
    pull(t);
    return t;
}
// spoji distribucije neovisnih Y_a i Y_b u distribuciju min(Y_a, Y_b);
// ta = P(Y_a > r), tb = P(Y_b > r) (masa desno od trenutnog intervala,
// uključivo "beskonačno" = prazna komponenta)
int mergeTrees(int a, int b, int l, int r, int ta, int tb) {
    if (!a && !b) return 0;
    if (!b) { apply(a, tb); return a; }
    if (!a) { apply(b, ta); return b; }
    if (l == r) {
        // P(min = x) = p_a(x) (p_b(x) + P(Y_b > x)) + p_b(x) P(Y_a > x)
        ll p = ((ll)sm[a] * ((sm[b] + tb) % MOD) + (ll)sm[b] * ta) % MOD;
        sm[a] = (int)p;
        sx[a] = (ll)p * vals[l] % MOD;
        return a;
    }
    push(a); push(b);
    int mid = (l + r) / 2;
    int ra = sm[rc[a]], rb = sm[rc[b]];  // masa desne polovice prije spajanja
    rc[a] = mergeTrees(rc[a], rc[b], mid + 1, r, ta, tb);
    lc[a] = mergeTrees(lc[a], lc[b], l, mid, (ta + ra) % MOD, (tb + rb) % MOD);
    pull(a);
    return a;
}

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    vector<ll> A(n + 1);
    for (int i = 1; i <= n; i++) scanf("%lld", &A[i]);
    vector<vector<int>> g(n + 1);
    for (int i = 0; i < n - 1; i++) {
        int u, v; scanf("%d %d", &u, &v);
        g[u].push_back(v); g[v].push_back(u);
    }
    // kompresija vrijednosti
    vector<ll> srt(A.begin() + 1, A.end());
    sort(srt.begin(), srt.end());
    srt.erase(unique(srt.begin(), srt.end()), srt.end());
    K = (int)srt.size();
    vals.resize(K);
    for (int i = 0; i < K; i++) vals[i] = (int)(srt[i] % MOD);
    vector<int> idx(n + 1);
    for (int v = 1; v <= n; v++) idx[v] = (int)(lower_bound(srt.begin(), srt.end(), A[v]) - srt.begin());

    // BFS redoslijed (bez rekurzije po stablu)
    vector<int> order, par(n + 1, 0);
    order.reserve(n);
    order.push_back(1); par[1] = -1;
    for (size_t i = 0; i < order.size(); i++) {
        int v = order[i];
        for (int w : g[v]) if (w != par[v]) { par[w] = v; order.push_back(w); }
    }

    lc.reserve(20 * n + 5); rc.reserve(20 * n + 5); sm.reserve(20 * n + 5);
    sx.reserve(20 * n + 5); lz.reserve(20 * n + 5);
    newNode();  // čvor 0 = prazno stablo

    const int INV2 = (MOD + 1) / 2;
    vector<int> root(n + 1, 0), inf(n + 1, 1);  // inf[v] = P(komponenta iz djece je prazna)
    ll ans = 0;
    for (int i = n - 1; i >= 0; i--) {
        int v = order[i];
        // spoji djecu: dijete c ulazi s vjerojatnošću 1/2 (brid zadržan)
        for (int c : g[v]) if (c != par[v]) {
            apply(root[c], INV2);
            int infc = INV2;  // masa "beskonačno" djeteta: brid prerezan
            root[v] = mergeTrees(root[v], root[c], 0, K - 1, inf[v], infc);
            inf[v] = (ll)inf[v] * INV2 % MOD;
        }
        // minimum s vlastitom vrijednošću A_v: sve > A_v postaje A_v
        int pLess = prefix(root[v], 0, K - 1, idx[v]);   // P(min djece < A_v)
        root[v] = cut(root[v], 0, K - 1, idx[v]);
        root[v] = setPoint(root[v], 0, K - 1, idx[v], (1 - pLess + MOD) % MOD);
        // v je najplići vrh svoje komponente ako je brid prema roditelju prerezan
        ll pTop = (par[v] == -1) ? 1 : INV2;
        ans = (ans + pTop * sx[root[v]]) % MOD;
    }
    ans = ans * power(2, n - 1) % MOD;
    printf("%lld\n", ans);
    return 0;
}
