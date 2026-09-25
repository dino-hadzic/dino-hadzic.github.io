// UCup 1, Stage 14, D: LaLa and Magic Stone
// Broj particija slobodnih ćelija na U-komade (3x3 bez dvije susjedne ćelije
// sredine jedne stranice). Pohlepno: uvijek pokrivamo leksikografski najmanju
// slobodnu ćeliju (i, j); komad koji je pokriva ima gornji-lijevi kut kutije
// upravo u (i, j). Kad je izbor lokalno dvoznačan, analiza slučajeva iz
// službenog rješenja daje jedinstvenu odluku ili prepoznaje „spojeni komad”
// (dva isprepletena U-komada, 14 ćelija) koji ima točno 2 unutarnje podjele.
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 998244353;

int N, M;
vector<string> g;               // '1' = nedostupno ili već pokriveno

// Orijentacije U-komada u kutiji 3x3 s kutom (a, b): koje dvije ćelije nedostaju.
// 0 = otvor gore (nedostaju (a,b+1),(a+1,b+1)), 1 = otvor dolje ((a+1,b+1),(a+2,b+1)),
// 2 = otvor lijevo ((a+1,b),(a+1,b+1)), 3 = otvor desno ((a+1,b+1),(a+1,b+2)).
const int MISS[4][2][2] = {{{0, 1}, {1, 1}}, {{1, 1}, {2, 1}}, {{1, 0}, {1, 1}}, {{1, 1}, {1, 2}}};
enum { UP = 0, DOWN = 1, LEFT = 2, RIGHT = 3 };

bool freeCell(int r, int c) {
    return r >= 0 && r < N && c >= 0 && c < M && g[r][c] == '0';
}
bool blockedCell(int r, int c) {           // izvan ploče ili nedostupno/pokriveno
    return !freeCell(r, c);
}
bool inPiece(int o, int dr, int dc) {
    for (int k = 0; k < 2; k++)
        if (MISS[o][k][0] == dr && MISS[o][k][1] == dc) return false;
    return true;
}
// Stane li komad orijentacije o s kutom (a, b)?
bool fits(int o, int a, int b) {
    for (int dr = 0; dr < 3; dr++)
        for (int dc = 0; dc < 3; dc++)
            if (inPiece(o, dr, dc) && !freeCell(a + dr, b + dc)) return false;
    return true;
}
void place(int o, int a, int b) {
    for (int dr = 0; dr < 3; dr++)
        for (int dc = 0; dc < 3; dc++)
            if (inPiece(o, dr, dc)) g[a + dr][b + dc] = '1';
}

// Spojeni komad A: kutija 4x4 s kutom (i, j) bez (i, j+3) i (i+3, j)
//   = RIGHT(i,j) + LEFT(i+1,j+1) = DOWN(i,j) + UP(i+1,j+1).
// Spojeni komad B: kutija 4x4 s kutom (i, j-1) bez (i, j-1) i (i+3, j+2)
//   = DOWN(i,j) + UP(i+1,j-1) = LEFT(i,j) + RIGHT(i+1,j-1).
bool fitsMerged(char which, int i, int j) {
    int b = (which == 'A') ? j : j - 1;
    for (int dr = 0; dr < 4; dr++)
        for (int dc = 0; dc < 4; dc++) {
            bool skip = (which == 'A') ? ((dr == 0 && dc == 3) || (dr == 3 && dc == 0))
                                       : ((dr == 0 && dc == 0) || (dr == 3 && dc == 3));
            if (!skip && !freeCell(i + dr, b + dc)) return false;
        }
    return true;
}
void placeMerged(char which, int i, int j) {
    if (which == 'A') { place(RIGHT, i, j); place(LEFT, i + 1, j + 1); }
    else              { place(DOWN, i, j);  place(UP, i + 1, j - 1); }
}

int main() {
    scanf("%d %d", &N, &M);
    g.resize(N);
    char buf[1105];
    for (int i = 0; i < N; i++) { scanf("%s", buf); g[i] = buf; }

    long long ans = 1;
    for (int i = 0; i < N; i++)
        for (int j = 0; j < M; j++) {
            if (g[i][j] != '0') continue;
            // (i, j) je leksikografski najmanja slobodna ćelija.
            int cnt = 0, only = -1;
            for (int o = 0; o < 4; o++)
                if (fits(o, i, j)) { cnt++; only = o; }
            if (cnt == 0) { puts("0"); return 0; }
            if (cnt == 1) { place(only, i, j); continue; }

            // Bar dvije orijentacije stanu => svih 8 ćelija kutije 3x3 osim središta je slobodno.
            if (freeCell(i + 1, j + 1)) {
                // Slučaj 1: kutija 3x3 je potpuno slobodna -> (i, j) pokriva spojeni komad A ili B.
                bool vA = fitsMerged('A', i, j), vB = fitsMerged('B', i, j);
                if (!vA && !vB) { puts("0"); return 0; }
                char pick;
                if (vA != vB) pick = vA ? 'A' : 'B';
                else {
                    // Oba stanu. A je moguć jedino uz prisilnu podjelu:
                    // DOWN(i+1, j-3) i UP(i+3, j-2), a (i+2, j-2) i (i+4, j-1) blokirane;
                    // tada B ne može pokriti (i+1, j-2) ili (i+2, j-3). Inače je A nemoguć.
                    bool special = fits(DOWN, i + 1, j - 3) && fits(UP, i + 3, j - 2) &&
                                   blockedCell(i + 2, j - 2) && blockedCell(i + 4, j - 1);
                    pick = special ? 'A' : 'B';
                }
                placeMerged(pick, i, j);
                ans = ans * 2 % MOD;
            } else {
                // Slučaj 2: središte blokirano. Četiri konfiguracije (crveni + plavi komad + nužno
                // blokirana ćelija): L = LEFT(i,j)+RIGHT(i+1,j-2), (i+2,j-1) blokirana;
                // BL = DOWN(i,j)+UP(i+2,j-1), (i+3,j) blokirana; R = RIGHT(i,j)+LEFT(i+1,j+2),
                // (i+2,j+3) blokirana; BR = DOWN(i,j)+UP(i+2,j+1), (i+3,j+2) blokirana.
                bool L  = fits(LEFT, i, j)  && fits(RIGHT, i + 1, j - 2) && blockedCell(i + 2, j - 1);
                bool BL = fits(DOWN, i, j)  && fits(UP, i + 2, j - 1)    && blockedCell(i + 3, j);
                bool R  = fits(RIGHT, i, j) && fits(LEFT, i + 1, j + 2)  && blockedCell(i + 2, j + 3);
                bool BR = fits(DOWN, i, j)  && fits(UP, i + 2, j + 1)    && blockedCell(i + 3, j + 2);
                int valid = L + BL + R + BR;
                if (valid == 0) { puts("0"); return 0; }
                if (valid >= 2 && !(BL && BR)) { puts("0"); return 0; }   // L&R, L&BR, R&BL su nemogući
                if (BL && BR) {
                    // (i+1, j-1) slobodna -> uz BL bi ostala nepokrivena -> BR.
                    // Inače BR zahtijeva prisilnu podjelu DOWN(i+2, j-3) + UP(i+4, j-2)
                    // s blokiranim (i+3, j-2) i (i+5, j-1); ako je ona moguća, BL propada, inače BR.
                    if (freeCell(i + 1, j - 1)) BL = false;
                    else {
                        bool special = fits(DOWN, i + 2, j - 3) && fits(UP, i + 4, j - 2) &&
                                       blockedCell(i + 3, j - 2) && blockedCell(i + 5, j - 1);
                        if (special) BL = false; else BR = false;
                    }
                }
                if (L)       { place(LEFT, i, j);  place(RIGHT, i + 1, j - 2); }
                else if (BL) { place(DOWN, i, j);  place(UP, i + 2, j - 1); }
                else if (R)  { place(RIGHT, i, j); place(LEFT, i + 1, j + 2); }
                else         { place(DOWN, i, j);  place(UP, i + 2, j + 1); }
            }
        }
    printf("%lld\n", ans);
    return 0;
}
