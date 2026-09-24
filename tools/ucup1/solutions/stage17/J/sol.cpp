// UCup 1, Stage 17, J - Best Carry Player 3
// Neka je m najmanji broj s 2^m > K i B = 2^m. XOR s t <= K mijenja samo
// donjih m bitova, pa brojeve dijelimo u grupe po vrijednosti x / B.
// Unutar grupe: 0 poteza ako su brojevi jednaki, 1 ako je x^y <= K ili
// |x-y| = 1, inače točno 2 (d = x^y ima bit m-1, pa d = 2^(m-1) ^ (d bez tog
// bita), a oba dijela su <= K).
// Iz grupe g u g+1 može se prijeći JEDINO potezom +1 iz vrha grupe g*B+B-1
// u dno (g+1)*B. Zato je najkraći put: x -> vrh svoje grupe -> +1 -> dno ->
// vrh -> +1 -> ... -> dno grupe od y -> y, a svaki komad računamo formulom
// za istu grupu. Za međugrupe je cijena (dno -> vrh) + 1 uvijek ista.
#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;

ull K, B;

// najmanji broj poteza između dva broja u istoj grupi
int ista(ull x, ull y) {
    if (x == y) return 0;
    if ((x ^ y) <= K || x + 1 == y || y + 1 == x) return 1;
    return 2;
}

int main() {
    int T;
    scanf("%d", &T);
    while (T--) {
        ull X, Y;
        scanf("%llu %llu %llu", &X, &Y, &K);
        int m = 0;
        while ((1ULL << m) <= K) m++;
        B = 1ULL << m;
        if (X > Y) swap(X, Y);  // operacije su reverzibilne, cijena je simetrična
        ull gx = X / B, gy = Y / B;
        if (gx == gy) {
            printf("%d\n", ista(X, Y));
            continue;
        }
        ull ans = ista(X, gx * B + B - 1) + 1;          // do vrha grupe pa +1
        ull po_grupi = ista(0, B - 1) + 1;              // dno -> vrh -> +1
        ans += (gy - gx - 1) * po_grupi;                // međugrupe
        ans += ista(gy * B, Y);                         // od dna grupe y do y
        printf("%llu\n", ans);
    }
    return 0;
}
