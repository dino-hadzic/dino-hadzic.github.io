// UCup 1, Stage 18, C: New but Nostalgic Problem
// Trie + pohlepno određivanje odgovora slovo po slovo. Za kandidat v (čvor trie-a)
// najveći broj odabranih nizova s parnim lcp-om <= v računa se duž puta od korijena:
// u svakom čvoru puta sva podstabla djece s manjim slovom ulaze cijela, iz podstabla
// svakog djeteta s većim slovom smije se uzeti najviše jedan niz, a nizovi koji
// završavaju u čvoru ulaze svi. U završnom čvoru v iz svakog djeteta ide najviše jedan.
#include <bits/stdc++.h>
using namespace std;

static const int MAXN = 1000005;
int ch[MAXN][26];
int cntEnd[MAXN], sz[MAXN];
int tot;

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

int newNode() {
    int u = tot++;
    memset(ch[u], 0, sizeof(ch[u]));
    cntEnd[u] = sz[u] = 0;
    return u;
}

int main() {
    int T = readInt();
    while (T--) {
        int n = readInt(), k = readInt();
        tot = 0;
        int root = newNode();
        for (int i = 0; i < n; i++) {
            int c = readChar();
            while (c < 'a' || c > 'z') c = readChar();
            int u = root;
            sz[u]++;
            while (c >= 'a' && c <= 'z') {
                int d = c - 'a';
                if (!ch[u][d]) ch[u][d] = newNode();
                u = ch[u][d];
                sz[u]++;
                c = readChar();
            }
            cntEnd[u]++;
        }
        // pohlepno spuštanje
        string ans;
        int u = root;
        long long acc = 0;  // doprinos čvorova iznad trenutnog (već fiksiran)
        while (true) {
            int deg = 0;
            for (int d = 0; d < 26; d++) if (ch[u][d]) deg++;
            // kandidat v = trenutni prefiks
            if (acc + cntEnd[u] + deg >= k) break;
            // inače odgovor ima još barem jedno slovo; pronađi najmanje moguće
            long long smaller = 0;  // suma veličina podstabala djece s manjim slovom
            int chosen = -1;
            for (int d = 0; d < 26; d++) {
                if (!ch[u][d]) continue;
                int larger = 0;
                for (int e = d + 1; e < 26; e++) if (ch[u][e]) larger++;
                // gornja granica za sve v s prefiksom (prefiks + d): cijelo podstablo d
                if (acc + cntEnd[u] + smaller + larger + sz[ch[u][d]] >= k) {
                    chosen = d;
                    acc += cntEnd[u] + smaller + larger;
                    break;
                }
                smaller += sz[ch[u][d]];
            }
            // chosen mora postojati: uz najveće dijete granica je acc+cntEnd+sz(u) >= k
            ans.push_back('a' + chosen);
            u = ch[u][chosen];
        }
        if (ans.empty()) puts("EMPTY");
        else puts(ans.c_str());
    }
    return 0;
}
