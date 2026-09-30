// UCup 1, Stage 11 (EC-Final 2022), B. Binary String
// Službeni pristup preko "blokova": maksimalni segmenti duljine >= 2 su blokovi, sve ostalo je izmjenična
// pozadina 0101... Blok nula svake sekunde putuje ulijevo, blok jedinica udesno (duljina im se ne mijenja);
// kad blok jedinica sustigne blok nula, oba se svake sekunde skrate za 1 dok kraći ne nestane (postane
// duljine 1, tj. dio pozadine). "Masa" bloka duljine L je L - 1. BSO ukupna masa blokova jedinica je
// veća ili jednaka od mase blokova nula (inače komplement + obrat, što komutira s procesom); tada svi
// blokovi nula nestanu. Biramo početak tako da je masa jedinica u svakom prefiksu >= mase nula, pa se
// sudari odvijaju po stogu (kao zagrade): blok nula uvijek udara u najbliži živi blok jedinica lijevo.
// Trenutak dodira para (P, Q) čita se iz početnih položaja i dosad izgubljenih masa:
//     T = (razmak(P, Q) u t = 0 + izgubljeno_P + izgubljeno_Q) / 2 .
// Kad nestane posljednji blok nula (t*), niz se samo ciklički pomiče udesno; odgovor = t* + period(a(t*)).
#include <bits/stdc++.h>
using namespace std;

static char buf[1 << 25];
int bufLen = 0, bufPos = 0;
inline int gc() {
    if (bufPos == bufLen) { bufLen = fread(buf, 1, sizeof(buf), stdin); bufPos = 0; if (bufLen <= 0) return -1; }
    return buf[bufPos++];
}
bool readToken(string &s) {
    s.clear();
    int c = gc();
    while (c != -1 && (c == ' ' || c == '\n' || c == '\r' || c == '\t')) c = gc();
    if (c == -1) return false;
    while (c != -1 && c != ' ' && c != '\n' && c != '\r' && c != '\t') { s.push_back((char)c); c = gc(); }
    return true;
}

const long long MOD = 998244353;

struct Block {
    int start, len;                         // početni položaj i duljina u t = 0 (linearne koordinate)
    int lost;                               // masa izgubljena u dosadašnjim sudarima
};

long long solve(string &s) {
    int n = s.size();
    int m = count(s.begin(), s.end(), '1');
    if (m == 0 || m == n) return 1;                        // konstantan niz: ništa se ne mijenja

    // Rotiramo niz tako da na položaju 0 počinje segment (rotacija komutira s procesom).
    {
        int i = 1;
        while (s[i] == s[i - 1]) i++;
        rotate(s.begin(), s.begin() + i, s.end());
    }
    auto runs = [&](vector<Block> &bl, long long &mass1, long long &mass0) {
        bl.clear(); mass1 = mass0 = 0;
        for (int i = 0; i < n;) {
            int j = i;
            while (j < n && s[j] == s[i]) j++;
            if (j - i >= 2) {
                bl.push_back({i, j - i, 0});
                (s[i] == '1' ? mass1 : mass0) += j - i - 1;
            }
            i = j;
        }
    };
    vector<Block> bl;
    long long mass1, mass0;
    runs(bl, mass1, mass0);
    if (mass1 < mass0) {                                    // komplement + obrat: uloge 0 i 1 se zamjenjuju
        reverse(s.begin(), s.end());
        for (char &c : s) c ^= 1;
        runs(bl, mass1, mass0);
    }
    int k = bl.size();

    // Početak: nakon najmanjeg prefiksnog zbroja (+masa za blok jedinica, -masa za blok nula)
    // svaki prefiks ima masu jedinica >= masi nula, pa je stog uvijek dovoljno "težak".
    int k0 = 0;
    {
        long long pref = 0, best = 0;
        for (int i = 0; i < k; i++) {
            pref += (s[bl[i].start] == '1' ? 1 : -1) * (long long)(bl[i].len - 1);
            if (pref < best) { best = pref; k0 = i + 1; }
        }
        if (k0 == k) k0 = 0;
    }

    long long tstar = 0;
    vector<Block> st; st.reserve(k);                        // stog živih blokova jedinica
    for (int idx = 0; idx < k; idx++) {
        Block b = bl[(k0 + idx) % k];
        if (k0 + idx >= k) b.start += n;                    // blokovi "iza" početka: linearne koordinate
        if (s[bl[(k0 + idx) % k].start] == '1') { st.push_back(b); continue; }
        int bcur = b.len - 1;                               // preostala masa bloka nula Q
        while (bcur > 0) {
            Block &p = st.back();                           // najbliži živi blok jedinica lijevo
            int pcur = p.len - 1 - p.lost;
            long long gap = (long long)b.start - (p.start + p.len - 1) - 1;   // polja između P i Q u t = 0
            long long T = (gap + p.lost + b.lost) / 2;      // trenutak dodira (uvijek cijeli broj)
            int d = min(pcur, bcur);
            p.lost += d; b.lost += d; bcur -= d;
            if (p.lost == p.len - 1) st.pop_back();
            if (bcur == 0) tstar = max(tstar, T + d);       // Q nestaje u trenutku T + d
        }
    }

    // Niz u trenutku t*: preživjeli blokovi jedinica pomaknuti za t*, između njih izmjenična pozadina.
    string fin(n, '?');
    for (const Block &p : st) {
        int L = p.len - p.lost;                             // trenutna duljina bloka
        long long x = (p.start + tstar) % n;
        for (int c = 0; c < L; c++) fin[(x + c) % n] = '1';
    }
    if (st.empty()) {                                       // sve mase su se poništile: čisti 0101... (n paran)
        for (int i = 0; i < n; i++) fin[i] = (i & 1) ? '1' : '0';
    } else {
        for (const Block &p : st) {                         // praznina iza bloka: 0 1 0 1 ... 0 (neparna)
            long long x = (p.start + tstar + p.len - p.lost) % n;
            char v = '0';
            while (fin[x] == '?') { fin[x] = v; v ^= 1; x = (x + 1) % n; }
        }
    }

    // najmanji ciklički period niza fin (prefiksna funkcija)
    vector<int> pi(n, 0);
    for (int i = 1; i < n; i++) {
        int j = pi[i - 1];
        while (j > 0 && fin[i] != fin[j]) j = pi[j - 1];
        if (fin[i] == fin[j]) j++;
        pi[i] = j;
    }
    int per = n - pi[n - 1];
    if (n % per != 0) per = n;
    return (tstar + per) % MOD;
}

int main() {
    string tok;
    readToken(tok);
    int T = stoi(tok);
    string out;
    string s;
    while (T-- && readToken(s)) {
        out += to_string(solve(s));
        out.push_back('\n');
        if (out.size() > (1 << 22)) { fwrite(out.data(), 1, out.size(), stdout); out.clear(); }
    }
    fwrite(out.data(), 1, out.size(), stdout);
    return 0;
}
