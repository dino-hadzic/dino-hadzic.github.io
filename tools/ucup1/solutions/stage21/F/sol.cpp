// F. Puzzle: Sashigane – konstrukcija u O(n)
// Ideja: krenemo od kvadrata 1x1 koji sadrži crno polje i u svakom koraku
// kvadrat s x s proširimo u (s+1) x (s+1) jednim L-oblikom: novi red i novi
// stupac zajedno čine točno jedan L (ugao im je u zajedničkom polju).
// Smjer proširenja biramo tako da ostanemo unutar mreže. Uvijek postoji rješenje.
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, bi, bj;
    scanf("%d %d %d", &n, &bi, &bj);
    int U = bi, D = bi, L = bj, R = bj;   // trenutni kvadrat [U,D] x [L,R]
    vector<array<int, 4>> ans;
    while (D - U + 1 < n) {
        int s = D - U + 1;                // trenutna veličina kvadrata
        bool down = D < n, right = R < n; // gdje ima mjesta za rast
        int r = down ? D + 1 : U - 1;     // novi red
        int c = right ? R + 1 : L - 1;    // novi stupac
        // krak po stupcu c pokriva sve stare retke (duljina s), krak po retku r sve stare stupce
        int h = down ? -s : s;
        int w = right ? -s : s;
        ans.push_back({r, c, h, w});
        if (down) D++; else U--;
        if (right) R++; else L--;
    }
    printf("Yes\n%d\n", (int)ans.size());
    for (auto &a : ans) printf("%d %d %d %d\n", a[0], a[1], a[2], a[3]);
    return 0;
}
