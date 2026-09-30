// UCup 1, Stage 17, G - Recover the String
// Vrhovi ulaznog stupnja 0 su pojedinačna slova (dodijelimo ih proizvoljno),
// jedini vrh izlaznog stupnja 0 je cijeli niz; duljine slijede topološki.
// Svaki vrh u ima najviše dva prethodnika: L(u) (bez zadnjeg znaka) i R(u)
// (bez prvog znaka). Tvrdnja iz službenog rješenja: niz vrha je određen do na
// obrat, S(u) ili rev(S(u)); jedino što treba znati jest ORIJENTACIJA – koji
// je prethodnik L(u), a koji R(u). Tri tipa vrhova:
//  * tip 1: jedan prethodnik  -> niz od jednog slova, orijentacija nebitna;
//  * tip 2: dva prethodnika s istim skupom prethodnika -> alternirajući niz;
//    slova su međusobno zamjenjiva (S(u) ili flip(S(u)));
//  * tip 3: ostali; L(u) i R(u) imaju točno jednog zajedničkog prethodnika
//    c = sredina niza, i vrijedi R(L(u)) = c = L(R(u)).
// Uvjet "R(L(u)) = L(R(u))" je uvjet PARITETA između orijentacija vrhova, pa
// sve uvjete skupljamo u DSU s paritetom (umjesto eksplicitnog čuvanja S(u),
// što bi bilo prekvadratno). Kod tipa 3 orijentacija je time određena do na
// globalni obrat; kod tipa 2 svaka dosljedna orijentacija daje isti niz do
// na flip. Iz orijentacije čitamo prvi/zadnji znak svakog vrha, a niz se
// čita duž lanca L(korijen), L(L(korijen)), ... Dva kandidata (S i rev S)
// preimenujemo po redoslijedu prvog pojavljivanja i uzmemo manjega. O(n+m).
#include <bits/stdc++.h>
using namespace std;

static char buf[1 << 25];
int bufpos = 0, buflen = 0;
inline int gc() {
    if (bufpos == buflen) { buflen = fread(buf, 1, sizeof(buf), stdin); bufpos = 0; if (buflen <= 0) return -1; }
    return buf[bufpos++];
}
inline int readInt() {
    int c = gc();
    while (c != '-' && (c < '0' || c > '9')) c = gc();
    int x = 0;
    while (c >= '0' && c <= '9') { x = x * 10 + (c - '0'); c = gc(); }
    return x;
}

const int MAXN = 1000005, MAXM = 2000005;
int n, m;
int eu[MAXM], ev[MAXM];
int indeg[MAXN], outdeg[MAXN], pred[MAXN][2];
int adjStart[MAXN], adjList[MAXM];  // sljedbenici (CSR)
int order_[MAXN];                    // topološki poredak
int dsuP[MAXN], dsuX[MAXN];          // DSU s paritetom: dsuX = paritet prema roditelju
int ori[MAXN];                       // 1 = pred[u][0] je L(u), 0 = pred[u][1] je L(u)
int firstC[MAXN], lastC[MAXN];

int findp(int x, int &par) {
    // iterativno nalaženje korijena s kompresijom puta i paritetom
    int r = x, p = 0;
    while (dsuP[r] != r) { p ^= dsuX[r]; r = dsuP[r]; }
    // kompresija
    int cur = x, cp = p;
    while (dsuP[cur] != r) {
        int nxt = dsuP[cur], nx = dsuX[cur];
        dsuP[cur] = r; dsuX[cur] = cp;
        cp ^= nx; cur = nxt;
    }
    par = p;
    return r;
}
// uvjet ori[a] xor ori[b] = d
void unite(int a, int b, int d) {
    int pa, pb;
    int ra = findp(a, pa), rb = findp(b, pb);
    if (ra == rb) { assert((pa ^ pb) == d); return; }
    dsuP[ra] = rb;
    dsuX[ra] = pa ^ pb ^ d;
}

inline int Lp(int u) { return indeg[u] == 1 ? pred[u][0] : (ori[u] ? pred[u][0] : pred[u][1]); }
inline int Rp(int u) { return indeg[u] == 1 ? pred[u][0] : (ori[u] ? pred[u][1] : pred[u][0]); }

string canon(const string &s) {
    int mp[26];
    memset(mp, -1, sizeof mp);
    int nxt = 0;
    string r = s;
    for (char &ch : r) {
        int c = ch - 'a';
        if (mp[c] < 0) mp[c] = nxt++;
        ch = 'a' + mp[c];
    }
    return r;
}

string out;

void solve() {
    n = readInt(); m = readInt();
    for (int i = 1; i <= n; i++) { indeg[i] = outdeg[i] = 0; dsuP[i] = i; dsuX[i] = 0; ori[i] = 0; }
    for (int i = 0; i < m; i++) {
        eu[i] = readInt(); ev[i] = readInt();
        outdeg[eu[i]]++;
        pred[ev[i]][indeg[ev[i]]++] = eu[i];
    }
    // CSR sljedbenika
    adjStart[1] = 0;
    for (int i = 1; i <= n; i++) adjStart[i + 1] = adjStart[i] + outdeg[i];
    {
        static int fillp[MAXN];
        for (int i = 1; i <= n; i++) fillp[i] = adjStart[i];
        for (int i = 0; i < m; i++) adjList[fillp[eu[i]]++] = ev[i];
    }
    // topološki poredak (Kahn); izvori dobivaju slova a, b, c, ...
    int qh = 0, qt = 0, letters = 0, sink = -1;
    static int rem[MAXN];
    for (int i = 1; i <= n; i++) {
        rem[i] = indeg[i];
        if (indeg[i] == 0) { order_[qt++] = i; firstC[i] = lastC[i] = letters++; }
        if (outdeg[i] == 0) sink = i;
    }
    while (qh < qt) {
        int u = order_[qh++];
        for (int e = adjStart[u]; e < adjStart[u + 1]; e++) {
            int v = adjList[e];
            if (--rem[v] == 0) order_[qt++] = v;
        }
    }
    // uvjeti pariteta
    for (int idx = 0; idx < n; idx++) {
        int u = order_[idx];
        if (indeg[u] != 2) continue;
        int p0 = pred[u][0], p1 = pred[u][1];
        // zajednički prethodnici od p0 i p1
        int common = 0, c = -1;
        for (int a = 0; a < indeg[p0]; a++)
            for (int b = 0; b < indeg[p1]; b++)
                if (pred[p0][a] == pred[p1][b]) { common++; c = pred[p0][a]; }
        if (common == 1) {
            // tip 3: c = R(L(u)) = L(R(u)).
            // ako je p0 = L(u): c je R-prethodnik od p0 i L-prethodnik od p1
            if (indeg[p0] == 2) unite(p0, u, pred[p0][0] == c ? 1 : 0);
            if (indeg[p1] == 2) unite(p1, u, pred[p1][0] == c ? 0 : 1);
        } else if (common == 2) {
            // tip 2: R(p0) = L(p1)  (ekvivalentno L(p0) = R(p1)), neovisno o ori[u]
            int e = (pred[p0][0] == pred[p1][0]) ? 1 : 0;
            unite(p0, p1, e);
        }
        // common == 0: duljina 2, dva različita slova – bez uvjeta
    }
    // orijentacija: korijeni komponenata dobivaju 0
    for (int i = 1; i <= n; i++)
        if (indeg[i] == 2) { int p; findp(i, p); ori[i] = p; }
    // prvi i zadnji znak svakog vrha
    for (int idx = 0; idx < n; idx++) {
        int u = order_[idx];
        if (indeg[u] == 0) continue;
        firstC[u] = firstC[Lp(u)];
        lastC[u] = lastC[Rp(u)];
    }
    // niz duž lanca L-prethodnika od korijena
    int len = 0;
    for (int u = sink; ; u = Lp(u)) { len++; if (indeg[u] == 0) break; }
    string s(len, 'a');
    {
        int u = sink;
        for (int k = len - 1; k >= 0; k--) { s[k] = 'a' + lastC[u]; if (k) u = Lp(u); }
    }
    string a = canon(s);
    reverse(s.begin(), s.end());
    string b = canon(s);
    out += min(a, b);
    out += '\n';
}

int main() {
    int T = readInt();
    while (T--) solve();
    fwrite(out.data(), 1, out.size(), stdout);
    return 0;
}
