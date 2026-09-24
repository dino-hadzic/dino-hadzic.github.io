// UCup 1, Stage 20 (India), K. XOR Dice
// d < 64 stane u 6 bitova. Promatramo brojeve d*(a0 + a1*2^6 + a2*2^12), a_i in {0,1}:
// svaki 6-bitni blok je ili 0 ili d, pa je skup tih 8 brojeva zatvoren na XOR
// (blok po blok: d^d = 0, d^0 = d) i svi su visekratnici d. Svaka kockica dobije
// bilo kojih 6 od tih 8 brojeva; najveci je d*4161 <= 249660 < 10^6.
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, d;
    scanf("%d %d", &n, &d);
    vector<int> v;
    for (int m = 0; m < 8; m++) {
        int x = 0;
        for (int b = 0; b < 3; b++)
            if (m >> b & 1) x |= d << (6 * b);   // blok b = d
        v.push_back(x);
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 6; j++) printf("%d%c", v[j], j == 5 ? '\n' : ' ');
    }
    return 0;
}
