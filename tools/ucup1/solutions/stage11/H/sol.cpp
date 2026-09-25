// UCup 1, Stage 11 (EC-Final 2022), H. Chinese Checker
// Ploča: 17 redaka s 1,2,3,4,13,12,11,10,9,10,11,12,13,4,3,2,1 polja. Polje predstavljamo
// parom (redak, x) gdje je x vodoravna koordinata u "pola koraka": polja retka duljine c imaju
// x = -(c-1), -(c-3), ..., c-1. Tri osi ploče su tada smjerovi (0,2), (1,1) i (1,-1).
// Za svaku figuru a BFS-om obiđemo sva polja do kojih može doći nizom skokova; svaki novi
// položaj (osim početnog) jedan je različit potez, a različite figure daju različite skupove.
#include <bits/stdc++.h>
using namespace std;

const int ROWS = 17;
const int LEN[ROWS + 1] = {0, 1, 2, 3, 4, 13, 12, 11, 10, 9, 10, 11, 12, 13, 4, 3, 2, 1};
const int DR[6] = {0, 0, 1, 1, -1, -1};
const int DX[6] = {2, -2, 1, -1, 1, -1};

bool onBoard(int r, int x) {
    if (r < 1 || r > ROWS) return false;
    int c = LEN[r];
    return abs(x) <= c - 1 && ((x + c - 1) % 2 == 0);
}

int main() {
    int T;
    scanf("%d", &T);
    while (T--) {
        int n;
        scanf("%d", &n);
        vector<pair<int, int>> ch(n);
        set<pair<int, int>> occ;
        for (auto &[r, x] : ch) {
            int row, col;
            scanf("%d %d", &row, &col);
            r = row; x = -(LEN[row] - 1) + 2 * (col - 1);
            occ.insert({r, x});
        }
        long long ans = 0;
        for (int i = 0; i < n; i++) {
            pair<int, int> start = ch[i];
            occ.erase(start);                       // figura a napušta svoje početno polje
            set<pair<int, int>> vis;
            queue<pair<int, int>> q;
            vis.insert(start); q.push(start);
            while (!q.empty()) {
                auto [r, x] = q.front(); q.pop();
                for (int d = 0; d < 6; d++) {
                    // idemo uzduž osi dok ne naiđemo na prvu figuru (pivot b)
                    int k = 1, br = r + DR[d], bx = x + DX[d];
                    while (onBoard(br, bx) && !occ.count({br, bx})) { k++; br += DR[d]; bx += DX[d]; }
                    if (!onBoard(br, bx)) continue;
                    // ciljno polje je simetrično: još k koraka iza pivota; sva polja između moraju biti prazna
                    int tr = br, tx = bx; bool ok = true;
                    for (int s = 0; s < k && ok; s++) {
                        tr += DR[d]; tx += DX[d];
                        if (!onBoard(tr, tx) || occ.count({tr, tx})) ok = false;
                    }
                    if (!ok) continue;
                    pair<int, int> tgt = {tr, tx};
                    if (tgt == start) continue;         // povratak na početno polje nije dopušten
                    if (vis.insert(tgt).second) q.push(tgt);
                }
            }
            ans += (long long)vis.size() - 1;
            occ.insert(start);
        }
        printf("%lld\n", ans);
    }
    return 0;
}
