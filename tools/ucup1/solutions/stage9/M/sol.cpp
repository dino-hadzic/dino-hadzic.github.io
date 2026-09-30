// UCup 1, Stage 9 (Qingdao 2018), M. Function and Function
// f(x) je zbroj "rupa" u znamenkama. Nakon najviše nekoliko primjena vrijednost padne na 0 ili 1,
// a f(0) = 1, f(1) = 0 se izmjenjuju, pa preostali broj koraka odlučuje samo parnošću.
#include <bits/stdc++.h>
using namespace std;

const int rupe[10] = {1, 0, 0, 0, 1, 0, 1, 0, 2, 1};

long long f(long long x) {
    if (x == 0) return 1;               // znamenka 0 ima jednu rupu
    long long r = 0;
    while (x) { r += rupe[x % 10]; x /= 10; }
    return r;
}

int main() {
    int T;
    scanf("%d", &T);
    while (T--) {
        long long x, k;
        scanf("%lld %lld", &x, &k);
        while (k > 0 && x > 1) { x = f(x); k--; }   // brzo padne na 0 ili 1
        if (k > 0 && (k & 1)) x = 1 - x;            // 0 <-> 1 izmjena, bitna je samo parnost
        printf("%lld\n", x);
    }
    return 0;
}
