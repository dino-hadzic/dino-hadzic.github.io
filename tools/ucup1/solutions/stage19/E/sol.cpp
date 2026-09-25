// UCup 1, Stage 19 (NAC 2023), E. First Last
// Slova (najviše 3) su vrhovi, riječ je usmjereni brid prvo -> zadnje slovo. Igrač na potezu u
// vrhu x bira neiskorišten brid iz x; tko nema brida gubi. Redukcije koje ne mijenjaju ishod:
//   (1) dvije petlje na istom vrhu smijemo ukloniti (pobjednik zrcali: na protivničku petlju
//       odgovori drugom petljom i vrati isto stanje),
//   (2) par bridova u->v i v->u smijemo ukloniti (isti argument zrcaljenja).
// Nakon redukcije svaki vrh ima <=1 petlju i između svaka dva vrha bridovi idu samo u jednom
// smjeru, pa je graf ili 3-ciklus s petljama ili acikličan. Iz bilo kojeg stanja dostižno je
// samo O(n) stanja (obilazak ciklusa troši bridove ravnomjerno), pa memoizirani minimax prolazi.
#include <bits/stdc++.h>
using namespace std;

int cnt[3][3];
map<array<int, 10>, bool> memo;

array<int, 10> kljuc(int x) {
    array<int, 10> k;
    k[0] = x;
    for (int i = 0; i < 3; ++i) for (int j = 0; j < 3; ++j) k[1 + 3 * i + j] = cnt[i][j];
    return k;
}

// pobjeđuje li igrač na potezu u vrhu x uz trenutne (reducirane) brojeve bridova
bool pobjeda(int x) {
    array<int, 10> k = kljuc(x);
    auto it = memo.find(k);
    if (it != memo.end()) return it->second;
    bool w = false;
    for (int y = 0; y < 3 && !w; ++y) {
        if (cnt[x][y] == 0) continue;
        --cnt[x][y];
        if (!pobjeda(y)) w = true;
        ++cnt[x][y];
    }
    memo[k] = w;
    return w;
}

void reduciraj() {
    for (int i = 0; i < 3; ++i) cnt[i][i] %= 2;
    for (int i = 0; i < 3; ++i)
        for (int j = i + 1; j < 3; ++j) {
            int m = min(cnt[i][j], cnt[j][i]);
            cnt[i][j] -= m;
            cnt[j][i] -= m;
        }
}

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    vector<pair<char, char>> rijeci(n);
    char buf[32];
    set<char> slova;
    for (int i = 0; i < n; ++i) {
        if (scanf("%31s", buf) != 1) return 0;
        rijeci[i] = {buf[0], buf[strlen(buf) - 1]};
        slova.insert(rijeci[i].first);
        slova.insert(rijeci[i].second);
    }
    map<char, int> idx;
    for (char c : slova) idx[c] = (int)idx.size();
    int poc[3][3] = {};
    for (auto &r : rijeci) ++poc[idx[r.first]][idx[r.second]];

    // Alice pobjeđuje riječju u->v točno kad je Bob u vrhu v (bez te riječi) u gubitničkom stanju.
    // Riječi iste klase (u, v) su ekvivalentne, pa svaku klasu ispitujemo jednom.
    long long odgovor = 0;
    for (int u = 0; u < 3; ++u)
        for (int v = 0; v < 3; ++v) {
            if (poc[u][v] == 0) continue;
            for (int i = 0; i < 3; ++i) for (int j = 0; j < 3; ++j) cnt[i][j] = poc[i][j];
            --cnt[u][v];
            reduciraj();
            if (!pobjeda(v)) odgovor += poc[u][v];
        }
    printf("%lld\n", odgovor);
    return 0;
}
