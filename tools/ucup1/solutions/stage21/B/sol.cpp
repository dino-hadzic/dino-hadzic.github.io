// B. Be Careful 2 – uključivanje-isključivanje po krajnjim točkama, O(k^2)
// odgovor = sum_S (-1)^|S| f(S), f(S) = zbroj d^2 po kvadratima koji strogo sadrže S.
// Grupiramo S po (L, R) = točkama s najmanjim i najvećim x (uz fiksan poredak za jednake
// koordinate). Za |S| >= 2 zbroj predznaka po svim S s istim (L,R) i istim kvadratom iznosi
// [nijedna "srednja" točka (x strogo između L i R) nije u kvadratu], pa je
//   odgovor = (svi kvadrati) - sum_L f({L}) + sum_{L<R} sum_{kvadrat strogo sadrži L,R,
//             ne sadrži srednju točku} d^2 .
// Za par (L,R) su relevantne samo srednje točke najbliže ispod/iznad y-raspona [yLo,yHi];
// ako je neka srednja točka po y unutar [yLo,yHi], par ne doprinosi. Za fiksni L obrađujemo R
// u padajućem x uz dvostruko povezanu listu po y (brisanje O(1)) -> O(k^2) parova.
// Broj kvadrata stranice d s x-rasponom koji strogo sadrži [a,b] unutar [A,B] je trapezna
// funkcija od d (po dijelovima linearna), pa je zbroj d^2 * tx(d) * ty(d) po dijelovima
// polinom stupnja 4 -> Faulhaberove formule, O(1) po paru.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
const ull MOD = 998244353;

ull pw(ull b, ull e) { ull r = 1; b %= MOD; while (e) { if (e & 1) r = r * b % MOD; b = b * b % MOD; e >>= 1; } return r; }
ull inv6, inv30;
// prefiksne sume potencija 1..t (mod p)
ull P2(ll t) { if (t <= 0) return 0; ull x = t % MOD; return x * ((x + 1) % MOD) % MOD * ((2 * x + 1) % MOD) % MOD * inv6 % MOD; }
ull P3(ll t) { if (t <= 0) return 0; ull x = t % MOD; ull s = x * ((x + 1) % MOD) % MOD * ((MOD + 1) / 2) % MOD; return s * s % MOD; }
ull P4(ll t) {
    if (t <= 0) return 0; ull x = t % MOD;
    ull a = x * ((x + 1) % MOD) % MOD * ((2 * x + 1) % MOD) % MOD;
    ull b = ((3 * x % MOD * x + 3 * x + MOD - 1) % MOD);
    return a * b % MOD * inv30 % MOD;
}

struct Piece { ll l, r; ll al, be; };   // na [l,r] vrijednost = al*d + be  (>= 1)

// tau(d) = #{u : max(A, b-d+1) <= u <= min(a-1, B-d)}  -- broj položaja 1D prozora duljine d
// unutar [A,B] koji strogo sadrži [a,b];  A < a <= b < B.  Vraća <= 3 linearna dijela s tau >= 1.
int trapez(ll a, ll b, ll A, ll B, Piece *out) {
    ll t1 = b - A + 1, t2 = B - a + 1;          // od t1: donja granica = A; od t2: gornja = B-d
    ll lo = min(t1, t2), hi = max(t1, t2);
    Piece cand[3] = {
        {1, lo - 1, 1, -(b - a + 1)},            // (a-1) - (b-d+1) + 1
        {lo, hi - 1, 0, (t1 <= t2) ? (a - A) : (B - b)},
        {hi, LLONG_MAX / 4, -1, B - A + 1}       // (B-d) - A + 1
    };
    int cnt = 0;
    for (auto p : cand) {
        // ograniči na tau >= 1
        if (p.al == 1) p.l = max(p.l, 1 - p.be);
        else if (p.al == -1) p.r = min(p.r, p.be - 1);
        else if (p.be < 1) continue;
        p.l = max(p.l, 1LL);
        if (p.l <= p.r) out[cnt++] = p;
    }
    return cnt;
}

// zbroj d^2 * tx(d) * ty(d) po svim d
ull F(ll ax, ll bx, ll Ax, ll Bx, ll ay, ll by, ll Ay, ll By) {
    Piece X[3], Y[3];
    int nx = trapez(ax, bx, Ax, Bx, X), ny = trapez(ay, by, Ay, By, Y);
    ull res = 0;
    for (int i = 0; i < nx; i++)
        for (int j = 0; j < ny; j++) {
            ll l = max(X[i].l, Y[j].l), r = min(X[i].r, Y[j].r);
            if (l > r) continue;
            ull s2 = (P2(r) + MOD - P2(l - 1)) % MOD, s3 = (P3(r) + MOD - P3(l - 1)) % MOD, s4 = (P4(r) + MOD - P4(l - 1)) % MOD;
            ll c4 = X[i].al * Y[j].al;                        // ∈ {-1,0,1}
            ll c3 = X[i].al * Y[j].be + X[i].be * Y[j].al;    // |c3| <= 2e9
            ll c2 = X[i].be * Y[j].be;                        // |c2| <= 1e18
            ull m4 = (c4 % (ll)MOD + MOD) % MOD, m3 = (c3 % (ll)MOD + MOD) % MOD, m2 = (c2 % (ll)MOD + MOD) % MOD;
            res = (res + m4 * s4 + m3 * s3 + m2 * s2) % MOD;
        }
    return res;
}

int main() {
    inv6 = pw(6, MOD - 2); inv30 = pw(30, MOD - 2);
    ll n, m; int k;
    scanf("%lld %lld %d", &n, &m, &k);
    vector<ll> x(k), y(k);
    for (int i = 0; i < k; i++) scanf("%lld %lld", &x[i], &y[i]);
    // poredak po x (jednaki x: po indeksu) i po y (jednaki y: po indeksu) -> sve "koordinate" različite
    vector<int> ox(k), oy(k), rx(k), ry(k);
    iota(ox.begin(), ox.end(), 0); iota(oy.begin(), oy.end(), 0);
    sort(ox.begin(), ox.end(), [&](int a, int b) { return x[a] != x[b] ? x[a] < x[b] : a < b; });
    sort(oy.begin(), oy.end(), [&](int a, int b) { return y[a] != y[b] ? y[a] < y[b] : a < b; });
    for (int i = 0; i < k; i++) { rx[ox[i]] = i; ry[oy[i]] = i; }

    // 1) svi kvadrati: tau_x = n-d+1, tau_y = m-d+1  (prozor [0,n] bez unutarnjeg intervala)
    //    izravno: sum_{d=1}^{min(n,m)} d^2 (n+1-d)(m+1-d)
    ull ans = 0;
    {
        ll D = min(n, m);
        ull s2 = P2(D), s3 = P3(D), s4 = P4(D);
        ull n1 = (n + 1) % MOD, m1 = (m + 1) % MOD;
        ans = (n1 * m1 % MOD * s2 + (MOD - (n1 + m1) % MOD) * s3 + s4) % MOD;
    }
    // 2) - sum_L f({L})
    for (int i = 0; i < k; i++) ans = (ans + MOD - F(x[i], x[i], 0, n, y[i], y[i], 0, m)) % MOD;
    // 3) parovi (L,R)
    vector<int> prv(k), nxt(k);
    for (int li = 0; li < k; li++) {
        int L = ox[li];
        // dvostruko povezana lista točaka s x-rangom >= li, po y
        int last = -1, head = -1;
        for (int t = 0; t < k; t++) {
            int p = oy[t];
            if (rx[p] < li) continue;
            prv[p] = last; nxt[p] = -1;
            if (last >= 0) nxt[last] = p; else head = p;
            last = p;
        }
        (void)head;
        for (int ri = k - 1; ri > li; ri--) {
            int R = ox[ri];
            int lowN = ry[L] < ry[R] ? L : R, highN = lowN == L ? R : L;
            if (nxt[lowN] == highN) {              // nijedna srednja točka po y između L i R
                int p = prv[lowN], q = nxt[highN];
                ll Yp = p < 0 ? 0 : y[p], Yq = q < 0 ? m : y[q];
                ans = (ans + F(x[L], x[R], 0, n, y[lowN], y[highN], Yp, Yq)) % MOD;
            }
            // izbaci R iz liste
            if (prv[R] >= 0) nxt[prv[R]] = nxt[R];
            if (nxt[R] >= 0) prv[nxt[R]] = prv[R];
        }
    }
    printf("%llu\n", ans);
    return 0;
}
