// G. LaLa and Divination
// Literal 2j = "E_j spašen" (bit 1), 2j+1 = "E_j katastrofa" (bit 0).
// Implikacija L -> K smije biti klauzula ako vrijedi u svakom danom retku:
// rows(L) podskup rows(K). Uzmemo SVE takve klauzule; formula je najjača
// moguća, pa ako njezin skup rješenja nije točno zadani skup, odgovor je -1.
// Relacija "podskup" je tranzitivna, pa je imp[L] odmah i zatvorenje L-a.
// Rješenja nabrajamo grananjem: djelomično zadovoljenje koje je konzistentno i
// zatvoreno na implikacije uvijek se proširuje do rješenja (2-SAT), pa je broj
// listova rekurzije jednak broju rješenja i stajemo čim ih ima više od N.
#include <bits/stdc++.h>
using namespace std;

typedef unsigned long long ull;

int N, M, L;              // L = 2M literala
int W;                    // riječi po bitsetu literala
vector<ull> rowsBits;     // rowsBits[lit * RW + w]
vector<ull> imp;          // imp[lit * W + w]: bit K = (rows(lit) podskup rows(K))
int RW;

inline bool getBit(const vector<ull>& v, size_t base, int i) { return (v[base + i / 64] >> (i % 64)) & 1ULL; }

vector<vector<ull>> Tstack;   // T na svakoj dubini rekurzije
long long cnt = 0;
long long limitCnt;

// vraća false ako je broj rješenja premašio granicu
bool rec(int depth, int from) {
    vector<ull>& T = Tstack[depth];
    int j = from;
    while (j < M && (getBit(T, 0, 2 * j) || getBit(T, 0, 2 * j + 1))) j++;
    if (j == M) { cnt++; return cnt <= limitCnt; }
    for (int lit = 2 * j; lit <= 2 * j + 1; lit++) {
        // konzistentnost: reach(lit) ne smije sadržavati negaciju nečega u T ni ~lit
        bool ok = !getBit(imp, (size_t)lit * W, lit ^ 1);
        if (ok) {
            for (int w = 0; w < W && ok; w++) {
                ull r = imp[(size_t)lit * W + w];
                // negacije bitova iz T: zamjena susjednih bitova
                ull t = T[w];
                ull negT = ((t & 0x5555555555555555ULL) << 1) | ((t & 0xAAAAAAAAAAAAAAAAULL) >> 1);
                if (r & negT) ok = false;
            }
        }
        if (!ok) continue;
        vector<ull>& T2 = Tstack[depth + 1];
        for (int w = 0; w < W; w++) T2[w] = T[w] | imp[(size_t)lit * W + w];
        if (!rec(depth + 1, j + 1)) return false;
    }
    return true;
}

int main() {
    if (scanf("%d %d", &N, &M) != 2) return 0;
    L = 2 * M; W = (L + 63) / 64; RW = (N + 63) / 64;
    rowsBits.assign((size_t)L * RW, 0);
    static char buf[2105];
    for (int i = 0; i < N; i++) {
        scanf("%s", buf);
        for (int j = 0; j < M; j++) {
            int lit = (buf[j] == '1') ? 2 * j : 2 * j + 1;
            rowsBits[(size_t)lit * RW + i / 64] |= 1ULL << (i % 64);
        }
    }
    imp.assign((size_t)L * W, 0);
    for (int a = 0; a < L; a++) {
        for (int b = 0; b < L; b++) {
            bool sub = true;
            for (int w = 0; w < RW && sub; w++)
                if (rowsBits[(size_t)a * RW + w] & ~rowsBits[(size_t)b * RW + w]) sub = false;
            if (sub) imp[(size_t)a * W + b / 64] |= 1ULL << (b % 64);
        }
    }
    // nabrajanje rješenja
    Tstack.assign(M + 2, vector<ull>(W, 0));
    limitCnt = N;
    bool okCount = rec(0, 0);
    if (!okCount || cnt != N) { puts("-1"); return 0; }
    // rješenja formule su točno zadani reci (svaki redak zadovoljava sve klauzule,
    // a rješenja ima točno N i reci su različiti) -> ispis klauzula
    // klauzula (~a ili b) za svaku implikaciju a -> b, a != b; kanonski oblik:
    // par literala {p, q} = {~a, b} s p <= q, tautologije {p, ~p} preskačemo.
    vector<pair<int, int>> cl;
    for (int a = 0; a < L; a++)
        for (int b = 0; b < L; b++) {
            if (a == b || !getBit(imp, (size_t)a * W, b)) continue;
            int p = a ^ 1, q = b;
            if (p > q) swap(p, q);
            if (p == q && a == b) continue;     // ne može se dogoditi, sigurnosno
            if ((p ^ 1) == q) continue;         // tautologija
            if (p < q || (p == q)) cl.push_back({p, q});
        }
    sort(cl.begin(), cl.end());
    cl.erase(unique(cl.begin(), cl.end()), cl.end());
    // literal p: varijabla p/2, vrijednost (p % 2 == 0) -> "spašen"
    // t: 1 = (~i ili ~j), 2 = (~i ili j), 3 = (i ili ~j), 4 = (i ili j)
    string out;
    out.reserve(cl.size() * 14 + 16);
    out += to_string(cl.size()); out += '\n';
    char tmp[32];
    for (auto [p, q] : cl) {
        int i = p / 2, j = q / 2;
        bool pi = (p % 2 == 0), pj = (q % 2 == 0);
        int t = pi ? (pj ? 4 : 2) : (pj ? 3 : 1);
        int len = snprintf(tmp, sizeof tmp, "%d %d %d\n", i, j, t);
        out.append(tmp, len);
    }
    fwrite(out.data(), 1, out.size(), stdout);
    return 0;
}
