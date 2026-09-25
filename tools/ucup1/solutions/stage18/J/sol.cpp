// UCup 1, Stage 18, J: Escape Plan
// Dijkstra unatrag iz svih izlaza. Vrh v s d_v čudovišta dobiva konačnu udaljenost tek
// kad ga (d_v+1)-vi put izvadimo iz reda: prvih d_v kandidata (najkraćih puteva)
// čudovišta u najgorem slučaju blokiraju. Izlazi imaju udaljenost 0 odmah.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

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
    while (T--) {
        int n = readInt(), m = readInt(), k = readInt();
        vector<char> isExit(n + 1, 0);
        for (int i = 0; i < k; i++) isExit[readInt()] = 1;
        vector<int> d(n + 1);
        for (int i = 1; i <= n; i++) d[i] = readInt();
        // CSR reprezentacija grafa (brzo za m do 10^6)
        vector<int> deg(n + 2, 0), ex(m), ey(m), ew(m);
        for (int i = 0; i < m; i++) {
            ex[i] = readInt();
            ey[i] = readInt();
            ew[i] = readInt();
            deg[ex[i]]++;
            deg[ey[i]]++;
        }
        vector<int> start(n + 2, 0);
        for (int i = 1; i <= n; i++) start[i + 1] = start[i] + deg[i];
        vector<int> to(2 * m), wt(2 * m), fillp(start.begin(), start.end());
        for (int i = 0; i < m; i++) {
            to[fillp[ex[i]]] = ey[i]; wt[fillp[ex[i]]++] = ew[i];
            to[fillp[ey[i]]] = ex[i]; wt[fillp[ey[i]]++] = ew[i];
        }
        vector<ll> dist(n + 1, -1);
        vector<int> cnt(n + 1, 0);
        priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<pair<ll, int>>> pq;
        for (int v = 1; v <= n; v++)
            if (isExit[v]) pq.push({0, v});
        while (!pq.empty()) {
            auto [dv, v] = pq.top();
            pq.pop();
            if (dist[v] != -1) continue;
            if (!isExit[v]) {
                cnt[v]++;
                if (cnt[v] <= d[v]) continue;  // ovaj kandidat čudovišta blokiraju
            }
            dist[v] = dv;
            for (int e = start[v]; e < start[v + 1]; e++) {
                int u = to[e];
                if (dist[u] == -1) pq.push({dv + wt[e], u});
            }
        }
        printf("%lld\n", dist[1]);
    }
    return 0;
}
