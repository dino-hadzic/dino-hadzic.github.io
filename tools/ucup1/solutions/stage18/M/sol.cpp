// UCup 1, Stage 18, M: Canvas
// Gledamo operacije u obrnutom redoslijedu: prva operacija koja dotakne poziciju
// određuje joj konačnu vrijednost. Operacije (2,2) idu prve, (1,1) posljednje.
// Miješana operacija (u dobiva 1, v dobiva 2) je usmjereni brid u -> v. DFS iz vrha s
// koji ispisuje bridove redom obilaska daje svim dosegnutim vrhovima 2, a samo s dobiva 1
// (ako nije već "zaključan" na 2). Minimalan broj startova = broj izvorišnih SCC-ova bez
// zaključanog vrha; vrh s najvećim vremenom završetka u DFS-u uvijek leži u izvorišnom
// SCC-u preostalog grafa (Kosarajuov poredak), pa ne treba eksplicitno računati SCC-ove.
#include <bits/stdc++.h>
using namespace std;

static char buf[1 << 25];
int bufLen, bufPos;
inline int readChar() {
    if (bufPos == bufLen) {
        bufLen = fread(buf, 1, sizeof(buf), stdin);
        bufPos = 0;
        if (bufLen <= 0) return -1;
    }
    return buf[bufPos++];
}
inline int readInt() {
    int c = readChar();
    while (c != -1 && (c < '0' || c > '9')) c = readChar();
    int x = 0;
    while (c >= '0' && c <= '9') {
        x = x * 10 + (c - '0');
        c = readChar();
    }
    return x;
}

int main() {
    int T = readInt();
    string out;
    while (T--) {
        int n = readInt(), m = readInt();
        vector<int> L(m), X(m), R(m), Y(m);
        vector<int> ops22, ops11;
        vector<vector<pair<int, int>>> adj(n + 1);  // (odredište, indeks operacije)
        vector<char> locked(n + 1, 0);
        for (int i = 0; i < m; i++) {
            L[i] = readInt();
            X[i] = readInt();
            R[i] = readInt();
            Y[i] = readInt();
            if (X[i] == 2 && Y[i] == 2) {
                ops22.push_back(i);
                locked[L[i]] = locked[R[i]] = 1;
            } else if (X[i] == 1 && Y[i] == 1) {
                ops11.push_back(i);
            } else if (X[i] == 1) {
                adj[L[i]].push_back({R[i], i});  // L dobiva 1, R dobiva 2
            } else {
                adj[R[i]].push_back({L[i], i});  // R dobiva 1, L dobiva 2
            }
        }
        // 1) redoslijed završetka DFS-a na cijelom grafu (iterativno)
        vector<int> finish;
        finish.reserve(n);
        vector<char> vis(n + 1, 0);
        vector<int> it(n + 1, 0);
        vector<int> st;
        for (int s = 1; s <= n; s++) {
            if (vis[s]) continue;
            vis[s] = 1;
            st.push_back(s);
            while (!st.empty()) {
                int v = st.back();
                if (it[v] < (int)adj[v].size()) {
                    int z = adj[v][it[v]++].first;
                    if (!vis[z]) {
                        vis[z] = 1;
                        st.push_back(z);
                    }
                } else {
                    finish.push_back(v);
                    st.pop_back();
                }
            }
        }
        // 2) DFS-ovi koji ispisuju bridove: prvo iz zaključanih vrhova, zatim iz
        //    nepohođenih vrhova po padajućem vremenu završetka
        vector<int> mixedOrder;  // u obrnutom (vremenskom) redoslijedu
        mixedOrder.reserve(m);
        fill(vis.begin(), vis.end(), 0);
        fill(it.begin(), it.end(), 0);
        auto dfsOut = [&](int s) {
            vis[s] = 1;
            st.push_back(s);
            while (!st.empty()) {
                int v = st.back();
                if (it[v] < (int)adj[v].size()) {
                    auto [z, id] = adj[v][it[v]++];
                    mixedOrder.push_back(id);
                    if (!vis[z]) {
                        vis[z] = 1;
                        st.push_back(z);
                    }
                } else {
                    st.pop_back();
                }
            }
        };
        for (int v = 1; v <= n; v++)
            if (locked[v] && !vis[v]) dfsOut(v);
        for (int k = n - 1; k >= 0; k--)
            if (!vis[finish[k]]) dfsOut(finish[k]);
        // 3) stvarni redoslijed = obrat: (1,1), miješane obrnuto, (2,2)
        vector<int> order;
        order.reserve(m);
        for (int id : ops11) order.push_back(id);
        for (int k = (int)mixedOrder.size() - 1; k >= 0; k--) order.push_back(mixedOrder[k]);
        for (int id : ops22) order.push_back(id);
        // simulacija radi zbroja
        vector<int> a(n + 1, 0);
        for (int id : order) {
            a[L[id]] = X[id];
            a[R[id]] = Y[id];
        }
        long long sum = 0;
        for (int i = 1; i <= n; i++) sum += a[i];
        out += to_string(sum);
        out += '\n';
        for (int k = 0; k < m; k++) {
            out += to_string(order[k] + 1);
            out += (k + 1 < m ? ' ' : '\n');
        }
    }
    fwrite(out.data(), 1, out.size(), stdout);
    return 0;
}
