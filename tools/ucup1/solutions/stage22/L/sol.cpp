// L. Kvadrat
// Brojevi se slažu u trokut: redak r sadrži T(r-1)+1 .. T(r), T(r)=r(r+1)/2.
// Za x u retku r vrijedi floor(sqrt(2x)+1.5) = r+1, pa skok (r,c) -> (r+1,c+1)
// čuva razliku c-r, a x-1 ide (r,c) -> (r,c-1) odnosno (r,1) -> (r-1,r-1).
// y <= x: odgovor x-y.  Inače, s u = c-r:
//   u_x >= u_y : 2(r_y-r_x) + (c_x-c_y)          (skokovi, pa spuštanje u retku)
//   u_x <  u_y : c_x + (r_y-r_x+1) + (r_y-c_y)   (prvo do kraja prethodnog retka)
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

// redak u kojem se nalazi v: najmanji r s r(r+1)/2 >= v
ll row_of(ll v) {
    ll r = (ll)sqrtl(2.0L * (long double)v);
    while (r > 0 && (r - 1) * r / 2 >= v) --r;
    while (r * (r + 1) / 2 < v) ++r;
    return r;
}

int main() {
    int T;
    scanf("%d", &T);
    while (T--) {
        ll x, y;
        scanf("%lld %lld", &x, &y);
        if (y <= x) { printf("%lld\n", x - y); continue; }
        ll rx = row_of(x), ry = row_of(y);
        ll cx = x - (rx - 1) * rx / 2, cy = y - (ry - 1) * ry / 2;   // stupci (1-indeksirani)
        ll ans;
        if (cx - rx >= cy - ry) ans = 2 * (ry - rx) + (cx - cy);
        else                    ans = cx + (ry - rx + 1) + (ry - cy);
        printf("%lld\n", ans);
    }
    return 0;
}
