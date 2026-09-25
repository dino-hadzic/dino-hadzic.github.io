// UCup 1, Stage 15 (ZJCPC 2023), G. Game: Celeste
// f_i = leksikografski najveći multiskup (sortiran nerastuće) na putu 1 -> i; f_i = max_j f_j + {a_i}
// po j s x_i-R <= x_j <= x_i-L. Multiskupove čuvamo u perzistentnom segmentnom stablu nad
// vrijednostima s slučajnim hashevima: usporedba = spust do najveće vrijednosti gdje se brojnosti
// razlikuju (O(log n)). Prozor za j klizi udesno -> monotoni deque, svaki f_j uđe/izađe jednom.
#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;

static char buf[1 << 25];
int bufLen = 0, bufPos = 0;
inline int citaj() {
    if (bufPos == bufLen) { bufLen = fread(buf, 1, sizeof(buf), stdin); bufPos = 0; if (bufLen <= 0) return -1; }
    return buf[bufPos++];
}
inline int citajInt() {
    int c = citaj(); while (c != '-' && (c < '0' || c > '9')) c = citaj();
    int s = 1; if (c == '-') { s = -1; c = citaj(); }
    int x = 0; while (c >= '0' && c <= '9') { x = x * 10 + (c - '0'); c = citaj(); }
    return x * s;
}

// čvorovi perzistentnog stabla: lijevi/desni sin i hash; u listu polje L čuva brojnost
vector<int> Lc, Rc;
vector<ull> H;
int cvorova = 0, n;

int umetni(int prev, int lo, int hi, int v, ull hv) {
    int nov = cvorova++;
    Lc[nov] = Lc[prev]; Rc[nov] = Rc[prev]; H[nov] = H[prev] + hv;
    if (lo == hi) { Lc[nov] = Lc[prev] + 1; return nov; }
    int mid = (lo + hi) / 2;
    if (v <= mid) Lc[nov] = umetni(Lc[prev], lo, mid, v, hv);
    else Rc[nov] = umetni(Rc[prev], mid + 1, hi, v, hv);
    return nov;
}
// usporedba multiskupova u korijenima u i v: -1 ako je u manji, 0 jednaki, 1 ako je u veći
int usporedi(int u, int v) {
    int lo = 1, hi = n;
    while (true) {
        if (H[u] == H[v]) return 0;
        if (lo == hi) return Lc[u] < Lc[v] ? -1 : 1;
        int mid = (lo + hi) / 2;
        if (H[Rc[u]] != H[Rc[v]]) { u = Rc[u]; v = Rc[v]; lo = mid + 1; }
        else { u = Lc[u]; v = Lc[v]; hi = mid; }
    }
}
string izlaz;
void ispisi(int u, int lo, int hi) {
    if (!u) return;
    if (lo == hi) { for (int k = 0; k < Lc[u]; ++k) { izlaz += to_string(lo); izlaz += ' '; } return; }
    int mid = (lo + hi) / 2;
    ispisi(Rc[u], mid + 1, hi);    // prvo veće vrijednosti (nerastući ispis)
    ispisi(Lc[u], lo, mid);
}

int main() {
    int T = citajInt();
    mt19937_64 rng(20230507);
    while (T--) {
        n = citajInt(); long long L = citajInt(), R = citajInt();
        vector<long long> x(n + 1); vector<int> a(n + 1);
        for (int i = 1; i <= n; ++i) x[i] = citajInt();
        for (int i = 1; i <= n; ++i) a[i] = citajInt();
        int dubina = 1; while ((1 << dubina) < n) ++dubina;
        size_t potrebno = (size_t)n * (dubina + 2) + 2;
        if (Lc.size() < potrebno) { Lc.assign(potrebno, 0); Rc.assign(potrebno, 0); H.assign(potrebno, 0); }
        cvorova = 1;                               // čvor 0 = prazan
        vector<ull> hv(n + 1);
        for (int v = 1; v <= n; ++v) hv[v] = rng() | 1;
        vector<int> korijen(n + 1, -1);           // -1: stup nedostižan
        korijen[1] = umetni(0, 1, n, a[1], hv[a[1]]);
        deque<int> dq; int ptr = 1;               // sljedeći j koji ulazi u prozor
        for (int i = 2; i <= n; ++i) {
            while (ptr < i && x[ptr] <= x[i] - L) {
                if (korijen[ptr] >= 0) {
                    while (!dq.empty() && usporedi(korijen[dq.back()], korijen[ptr]) <= 0) dq.pop_back();
                    dq.push_back(ptr);
                }
                ++ptr;
            }
            while (!dq.empty() && x[dq.front()] < x[i] - R) dq.pop_front();
            if (!dq.empty()) korijen[i] = umetni(korijen[dq.front()], 1, n, a[i], hv[a[i]]);
        }
        if (korijen[n] < 0) { puts("-1"); continue; }
        // broj skupljenih jagoda = duljina puta = broj ispisanih brojeva
        izlaz.clear();
        ispisi(korijen[n], 1, n);
        int k = 0; for (size_t i = 0; i < izlaz.size(); ++i) k += izlaz[i] == ' ';
        izlaz.pop_back();
        printf("%d\n%s\n", k, izlaz.c_str());
        izlaz.clear();
    }
    return 0;
}
