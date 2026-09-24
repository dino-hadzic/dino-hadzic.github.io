// UCup 1, Stage 13 (Um_nik mod 998244353 Contest), K. 4  -- brojanje podgrafova K4
// Ideja: poredamo vrhove po stupnju i svaki brid usmjerimo od "manjeg" prema "vecem" vrhu.
// Tada svaki vrh ima najvise sqrt(2m) izlaznih susjeda. Za fiksni najmanji vrh u klike K4
// gradimo mali graf na njegovim izlaznim susjedima (brid = trokut s u) i brojimo trokute
// u tom malom grafu bitsetima. Ukupno O(m * sqrt(m) / w).
#include <bits/stdc++.h>
using namespace std;

const int MAXD = 512;   // gornja granica broja izlaznih susjeda (sqrt(2*10^5) < 448)

int main() {
    int n, m;
    if (scanf("%d %d", &n, &m) != 2) return 0;
    vector<pair<int, int>> bridovi(m);
    vector<int> stupanj(n + 1, 0);
    for (auto &[a, b] : bridovi) {
        scanf("%d %d", &a, &b);
        ++stupanj[a];
        ++stupanj[b];
    }

    // Poredak: po stupnju, a zatim po indeksu (da bude strog totalni poredak).
    vector<int> rang(n + 1);
    {
        vector<int> vrhovi(n);
        iota(vrhovi.begin(), vrhovi.end(), 1);
        sort(vrhovi.begin(), vrhovi.end(), [&](int x, int y) {
            return make_pair(stupanj[x], x) < make_pair(stupanj[y], y);
        });
        for (int i = 0; i < n; ++i) rang[vrhovi[i]] = i;
    }

    // Izlazni susjedi: od vrha manjeg ranga prema vecem.
    vector<vector<int>> van(n + 1);
    for (auto [a, b] : bridovi) {
        if (rang[a] > rang[b]) swap(a, b);
        van[a].push_back(b);
    }

    vector<int> pozicija(n + 1, -1);       // indeks vrha unutar malog grafa za trenutni u, ili -1
    long long odgovor = 0;
    vector<bitset<MAXD>> mali;             // matrica susjedstva malog grafa

    for (int u = 1; u <= n; ++u) {
        const vector<int> &sus = van[u];
        int d = sus.size();
        if (d < 3) continue;
        for (int i = 0; i < d; ++i) pozicija[sus[i]] = i;
        mali.assign(d, bitset<MAXD>());

        // Brid (x, y) u malom grafu <=> x, y izlazni susjedi od u i (x, y) brid u pocetnom grafu,
        // tj. (u, x, y) je trokut. Pregledavamo izlazne bridove od x (rang x < rang y).
        for (int i = 0; i < d; ++i) {
            int x = sus[i];
            for (int y : van[x]) {
                int j = pozicija[y];
                if (j >= 0) {
                    mali[i].set(j);
                    mali[j].set(i);
                }
            }
        }

        // Trokuti malog grafa: za svaki brid (i, j) prebrojimo zajednicke susjede.
        // Svaki trokut se broji tri puta (jednom po bridu).
        long long trostruko = 0;
        for (int i = 0; i < d; ++i) {
            for (int j = mali[i]._Find_next(i); j < MAXD; j = mali[i]._Find_next(j)) {
                trostruko += (mali[i] & mali[j]).count();
            }
        }
        odgovor += trostruko / 3;

        for (int x : sus) pozicija[x] = -1;
    }
    printf("%lld\n", odgovor);
    return 0;
}
