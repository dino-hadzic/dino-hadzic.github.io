// UCup 1, Stage 17, I - Not Another Range Query Problem
// Korak f briše prvi znak svakog maksimalnog bloka. Simuliramo proces na
// CIJELOM nizu s: element x umire u koraku d(x) (svaki korak briše sve
// početke blokova; novi počeci mogu biti samo sljedbenici izbrisanih, pa je
// simulacija O(n) uz dvostruko povezanu listu). Neka je S_j skup preživjelih
// nakon j koraka.
// Ključno: podniz t = s[l..r] se od s razlikuje samo na "glavi". Ako je
// T_j = S_j ∩ [h_j, r] uz h_j ∈ S_j, u t se glava h_j sigurno briše (početak
// je), a ostali elementi imaju iste prethodnike kao u s. Zato
//   T_{j+1} = S_{j+1} ∩ [h_{j+1}, r],  h_{j+1} = sljedbenik od h_j u S_{j+1}.
// Umjesto pozicije glave čuvamo njen rang u S_j:
//   rang_{j+1}(h_{j+1}) = rang_j(h_j) + 1 - #{p izbrisan u koraku j+1 : p <= h_j}.
// Glave su monotone po l, pa upite sortiramo po l; brisanje p smanjuje rang
// sufiksu upita čiji je rang >= rang_j(p) (nađemo ga spustom po segmentnom
// stablu s max). Odgovor za (l, r, k) je max(0, rang_k(r) - rang_k(h_k) + 1),
// gdje je rang_k(r) = |S_k ∩ [1, r]| iz Fenwickova stabla.
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 500005;
int n, q;
char s[MAXN];
int d[MAXN], nxt[MAXN], prv[MAXN], stampA[MAXN];

// Fenwick nad pozicijama: 1 ako je element živ
int fw[MAXN];
void fadd(int i, int v) { for (; i <= n; i += i & -i) fw[i] += v; }
int fsum(int i) { int r = 0; for (; i > 0; i -= i & -i) r += fw[i]; return r; }

// segmentno stablo nad upitima (sortiranim po l): max + dodavanje na raspon
int Q;
vector<long long> mx, lz;
void sbuild(int v, int l, int r, const vector<long long> &init) {
    lz[v] = 0;
    if (l == r) { mx[v] = init[l]; return; }
    int m = (l + r) / 2;
    sbuild(2 * v, l, m, init);
    sbuild(2 * v + 1, m + 1, r, init);
    mx[v] = max(mx[2 * v], mx[2 * v + 1]);
}
void sadd(int v, int l, int r, int ql, int qr, long long x) {
    if (qr < l || r < ql) return;
    if (ql <= l && r <= qr) { mx[v] += x; lz[v] += x; return; }
    int m = (l + r) / 2;
    sadd(2 * v, l, m, ql, qr, x);
    sadd(2 * v + 1, m + 1, r, ql, qr, x);
    mx[v] = max(mx[2 * v], mx[2 * v + 1]) + lz[v];
}
// prvi indeks s vrijednošću >= t (niz je monoton), ili Q ako ga nema
int sfirst(int v, int l, int r, long long t, long long acc) {
    if (mx[v] + acc < t) return Q;
    if (l == r) return l;
    acc += lz[v];
    int m = (l + r) / 2;
    if (mx[2 * v] + acc >= t) return sfirst(2 * v, l, m, t, acc);
    return sfirst(2 * v + 1, m + 1, r, t, acc);
}
long long sget(int v, int l, int r, int i) {
    if (l == r) return mx[v];
    int m = (l + r) / 2;
    return lz[v] + (i <= m ? sget(2 * v, l, m, i) : sget(2 * v + 1, m + 1, r, i));
}

int main() {
    scanf("%d %d", &n, &q);
    scanf("%s", s + 1);

    // 1) simulacija na cijelom nizu: vrijeme smrti d(x)
    for (int i = 1; i <= n; i++) { nxt[i] = i + 1; prv[i] = i - 1; d[i] = 0; }
    nxt[0] = 1; prv[n + 1] = n;
    vector<int> starts, del;
    for (int i = 1; i <= n; i++) if (i == 1 || s[i] != s[i - 1]) starts.push_back(i);
    vector<vector<int>> byStep(n + 2);
    for (int step = 1; !starts.empty(); step++) {
        for (int p : starts) {
            d[p] = step;
            nxt[prv[p]] = nxt[p];
            prv[nxt[p]] = prv[p];
        }
        byStep[step] = starts;
        // nxt izbrisanih preusmjeri na prvi živi sljedbenik (silazno, put je već sažet)
        for (int t = (int)starts.size() - 1; t >= 0; t--) {
            int p = starts[t];
            if (nxt[p] <= n && d[nxt[p]] == step) nxt[p] = nxt[nxt[p]];
        }
        vector<int> ns;
        for (int p : starts) {
            int x = nxt[p];
            if (x > n || stampA[x] == step) continue;
            if (prv[x] == 0 || s[prv[x]] != s[x]) { stampA[x] = step; ns.push_back(x); }
        }
        sort(ns.begin(), ns.end());
        starts.swap(ns);
    }
    for (int i = 1; i <= n; i++) if (d[i] == 0) d[i] = n + 1;  // ne događa se, sigurnosno

    // 2) upiti
    vector<int> ql(q), qr(q), qk(q), ord(q);
    for (int i = 0; i < q; i++) scanf("%d %d %d", &ql[i], &qr[i], &qk[i]);
    iota(ord.begin(), ord.end(), 0);
    sort(ord.begin(), ord.end(), [&](int a, int b) { return ql[a] < ql[b]; });
    vector<int> posInOrd(q);
    for (int i = 0; i < q; i++) posInOrd[ord[i]] = i;
    vector<vector<int>> byK(n + 1);
    for (int i = 0; i < q; i++) byK[qk[i]].push_back(i);

    Q = q;
    mx.assign(4 * q + 4, 0); lz.assign(4 * q + 4, 0);
    // čuvamo rang_j(h_j) - j  (svaki korak svima +1)
    vector<long long> init(q);
    for (int i = 0; i < q; i++) init[i] = ql[ord[i]];
    sbuild(1, 0, q - 1, init);
    for (int i = 1; i <= n; i++) fadd(i, 1);

    vector<long long> ans(q);
    auto record = [&](int j) {
        for (int i : byK[j]) {
            long long rh = sget(1, 0, q - 1, posInOrd[i]) + j;  // rang_j(h_j)
            long long rr = fsum(qr[i]);                        // rang_j(r)
            ans[i] = max(0LL, rr - rh + 1);
        }
    };
    record(0);
    for (int j = 1; j <= n; j++) {
        vector<int> &dl = byStep[j];
        // rangovi izbrisanih u S_{j-1}, obrađujemo silazno po poziciji
        for (int t = (int)dl.size() - 1; t >= 0; t--) {
            int p = dl[t];
            long long rp = fsum(p);  // rang_{j-1}(p)
            int idx = sfirst(1, 0, q - 1, rp - (j - 1), 0);  // vrijednost + (j-1) >= rp
            if (idx < q) sadd(1, 0, q - 1, idx, q - 1, -1);
        }
        for (int p : dl) fadd(p, -1);
        record(j);
    }

    string out;
    char buf[24];
    for (int i = 0; i < q; i++) { snprintf(buf, sizeof buf, "%lld\n", ans[i]); out += buf; }
    fputs(out.c_str(), stdout);
    return 0;
}
