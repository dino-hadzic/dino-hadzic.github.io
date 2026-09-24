// UCup 1, Stage 11 (EC-Final 2022), B. Binary String
// Jedinice su "čestice" koje se pomiču ulijevo ako je lijevo polje prazno (paralelni TASEP / pravilo 184).
// Ako jedinica ima najviše koliko i nula (inače primijenimo komplement + obrat, što komutira s procesom),
// položaji čestica zadovoljavaju max-plus rekurziju y_j(t+1) = max(y_j(t) - 1, y_{j-1}(t) + 1), čije je
// rješenje y_j(t) = -t + 2j + max_{j-t <= i <= j} W_i, gdje je W_i = Y_i - 2i, a Y_i početni položaj
// i-te čestice (indeksi se produžuju ciklički: Y_{i-m} = Y_i - n).
// Proces postane čisto ciklički pomak u trenutku t* = max_i nxt_i - 1, gdje je nxt_i najmanji d >= 1 s
// W_{i+d} >= W_i. Odgovor = t* + (najmanji period niza u trenutku t*).
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

long long solve(string &s) {
    int n = s.size();
    int m = count(s.begin(), s.end(), '1');
    if (m == 0 || m == n) return 1;                        // konstantan niz: ništa se ne mijenja
    if (2 * m > n) {                                        // komplement + obrat: uloge 0 i 1 se zamjenjuju
        reverse(s.begin(), s.end());
        for (char &c : s) c ^= 1;
        m = n - m;
    }
    vector<int> q; q.reserve(m);
    for (int i = 0; i < n; i++) if (s[i] == '1') q.push_back(i);

    // W na indeksima [-m, m) -> pohranjeno kao W[i + m]
    vector<long long> W(2 * m);
    W[m] = q[0];                                            // W_0 = Y_0 - 0
    for (int i = 1; i < m; i++) W[m + i] = W[m + i - 1] + (q[i] - q[i - 1]) - 2;
    for (int i = 0; i < m; i++) W[i] = W[i + m] - (n - 2 * m); // W_{i-m} = W_i - (n - 2m)

    // nxt_i: prvi indeks desno s W >= W_i (postoji unutar m koraka jer je W_{i+m} >= W_i);
    // računamo za i u [-m, 0) po kopiji [0, m) -> potrebni indeksi u [-m, m)
    long long tstar = 0;
    {
        vector<int> st; st.reserve(2 * m);
        for (int i = 2 * m - 1; i >= 0; i--) {
            while (!st.empty() && W[st.back()] < W[i]) st.pop_back();
            if (i < m) tstar = max(tstar, (long long)(st.back() - i) - 1);
            st.push_back(i);
        }
    }

    // položaji u trenutku t*: y_j = -t* + 2j + max W na [j - t*, j], j u [0, m) -> indeksi [m - t*, 2m)
    string fin(n, '0');
    {
        deque<int> dq;
        int t = (int)tstar;
        for (int idx = m - t; idx < 2 * m; idx++) {
            while (!dq.empty() && W[dq.back()] <= W[idx]) dq.pop_back();
            dq.push_back(idx);
            int j = idx - m;                                // prozor [j - t, j] završava u idx
            if (j >= 0) {
                while (dq.front() < idx - t) dq.pop_front();
                long long y = -tstar + 2LL * j + W[dq.front()];
                y %= n; if (y < 0) y += n;
                fin[y] = '1';
            }
        }
    }

    // najmanji ciklički period niza fin (prefiksna funkcija)
    vector<int> pi(n, 0);
    for (int i = 1; i < n; i++) {
        int k = pi[i - 1];
        while (k > 0 && fin[i] != fin[k]) k = pi[k - 1];
        if (fin[i] == fin[k]) k++;
        pi[i] = k;
    }
    int p = n - pi[n - 1];
    if (n % p != 0) p = n;
    return (tstar + p) % MOD;
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
