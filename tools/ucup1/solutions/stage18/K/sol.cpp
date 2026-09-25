// UCup 1, Stage 18, K: Final Defense Line
// Apolonijev problem: tražena kružnica (x, y, R) zadovoljava (x-x_i)^2 + (y-y_i)^2 = (R-d_i)^2
// uz R >= max d_i. Razlike jednadžbi su linearne, pa su x i y linearne funkcije od R;
// uvrštavanjem u prvu jednadžbu dobivamo kvadratnu jednadžbu po R s CJELOBROJNIM
// koeficijentima (sve nazivnike pomnožimo). Broj rješenja odlučujemo egzaktno (__int128),
// a sam polumjer računamo u long double.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef __int128 lll;
typedef long double ld;

int sgn(lll v) { return v < 0 ? -1 : (v > 0 ? 1 : 0); }

// Broj korijena a*R^2 + b*R + c = 0 (a != 0, D >= 0) koji su >= M, egzaktno.
// Supstitucija S = R - M: a S^2 + b' S + c' = 0, brojimo korijene S >= 0.
int countRootsGE(lll a, lll b, lll c, lll D, ll M) {
    lll b2 = 2 * a * M + b;
    lll c2 = a * M * M + b * M + c;
    if (D == 0) return sgn(-b2) * sgn(a) >= 0 ? 1 : 0;  // jedan korijen -b'/(2a)
    // D > 0: dva različita korijena; umnožak = c'/a, zbroj = -b'/a
    int prod = sgn(c2) * sgn(a), sum = sgn(-b2) * sgn(a);
    if (prod == 0) return 1 + (sum > 0 ? 1 : 0);  // korijeni 0 i -b'/a
    if (prod < 0) return 1;
    return sum > 0 ? 2 : 0;
}

// Najmanji korijen >= M (znamo da ih je cnt >= 1); korijeni se računaju stabilno.
ld smallestRoot(lll a, lll b, lll c, lll D, int cnt) {
    ld A = (ld)a, B = (ld)b, C = (ld)c;
    ld sq = sqrtl((ld)D);
    ld q = -(B + (B >= 0 ? sq : -sq)) / 2;
    ld r1 = q / A, r2 = (q != 0) ? C / q : r1;
    if (cnt == 2) return min(r1, r2);
    return max(r1, r2);  // ako samo jedan korijen zadovoljava R >= M, to je veći
}

int main() {
    int T;
    if (scanf("%d", &T) != 1) return 0;
    string out;
    char buf[64];
    while (T--) {
        ll xa, ya, da, xb, yb, db, xc, yc, dc;
        if (scanf("%lld %lld %lld %lld %lld %lld %lld %lld %lld", &xa, &ya, &da, &xb, &yb, &db, &xc, &yc, &dc) != 9) return 0;
        ll M = max({da, db, dc});
        // x = (P1 + Q1 R) / D1   (iz jednadžbe B minus jednadžba A)
        ll D1 = 2 * (xb - xa);
        ll P1 = xb * xb - xa * xa + da * da - db * db;
        ll Q1 = 2 * (db - da);
        // C minus A: 2(xc-xa) x + 2 yc y = K2 + Q2 R
        ll K2 = xc * xc + yc * yc - xa * xa + da * da - dc * dc;
        ll Q2 = 2 * (dc - da);
        int cnt = 0;
        ld best = 0;
        bool infinite = false;
        if (yc != 0) {
            // y = (P2 + Q2p R) / D2, D2 = 2 yc D1
            ll D2 = 2 * yc * D1;
            ll P2 = -2 * (xc - xa) * P1 + D1 * K2;
            ll Q2p = -2 * (xc - xa) * Q1 + D1 * Q2;
            // x - xa = (X0 + X1 R) / D2
            ll X0 = P1 * 2 * yc - xa * D2, X1 = Q1 * 2 * yc;
            // (X0 + X1 R)^2 + (P2 + Q2p R)^2 = D2^2 (R - da)^2
            lll a = (lll)X1 * X1 + (lll)Q2p * Q2p - (lll)D2 * D2;
            lll b = 2 * ((lll)X0 * X1 + (lll)P2 * Q2p + (lll)D2 * D2 * da);
            lll c = (lll)X0 * X0 + (lll)P2 * P2 - (lll)D2 * D2 * da * da;
            if (a == 0 && b == 0 && c == 0) infinite = true;
            else if (a == 0 && b == 0) cnt = 0;
            else if (a == 0) {
                // R = -c/b >= M  <=>  sgn(-c - bM) * sgn(b) >= 0
                lll num = -c - b * M;
                if (sgn(num) * sgn(b) >= 0) {
                    cnt = 1;
                    best = -(ld)c / (ld)b;
                }
            } else {
                lll D = b * b - 4 * a * c;
                if (D >= 0) {
                    cnt = countRootsGE(a, b, c, D, M);
                    if (cnt > 0) best = smallestRoot(a, b, c, D, cnt);
                }
            }
        } else {
            // sva tri središta na osi x: linearan sustav po (x, R)
            //   D1 x - Q1 R = P1
            //   E1 x - Q2 R = K2,  E1 = 2(xc - xa)
            ll E1 = 2 * (xc - xa);
            lll det = (lll)D1 * (-Q2) - (lll)(-Q1) * E1;
            if (det != 0) {
                lll Rn = (lll)D1 * K2 - (lll)E1 * P1;  // R = Rn / det
                lll Xn = (lll)P1 * (-Q2) - (lll)(-Q1) * K2;  // x = Xn / det
                if (det < 0) { det = -det; Rn = -Rn; Xn = -Xn; }
                if (Rn >= (lll)M * det) {
                    // y^2 = (R - da)^2 - (x - xa)^2, pomnoženo s det^2
                    lll u = Rn - (lll)da * det, v = Xn - (lll)xa * det;
                    lll y2 = u * u - v * v;
                    if (y2 > 0) cnt = 2;
                    else if (y2 == 0) cnt = 1;
                    if (cnt) best = (ld)Rn / (ld)det;
                }
            } else {
                // paralelne jednadžbe: nekonzistentne (0) ili identične (obitelj rješenja)
                lll cons = (lll)D1 * K2 - (lll)E1 * P1;
                if (cons != 0) cnt = 0;
                else {
                    // G(R) = D1^2 (R-da)^2 - (P1 + Q1 R - xa D1)^2 >= 0 uz R >= M
                    lll W0 = P1 - (lll)xa * D1, W1 = Q1;
                    lll al = (lll)D1 * D1 - W1 * W1;
                    lll be = -2 * (lll)D1 * D1 * da - 2 * W0 * W1;
                    lll ga = (lll)D1 * D1 * da * da - W0 * W0;
                    if (al == 0 && be == 0 && ga == 0) infinite = true;
                    else if (al > 0) infinite = true;
                    else if (al == 0) {
                        if (be > 0) infinite = true;
                        else if (be == 0) infinite = (ga > 0);  // konstanta: > 0 beskonačno, < 0 ništa
                        else {
                            // korijen r0 = -ga/be; pozitivno lijevo od r0
                            lll num = -ga, den = -be;  // r0 = num/den, den > 0
                            lll cmp = num - (lll)M * den;
                            if (cmp > 0) infinite = true;
                            else if (cmp == 0) { cnt = 1; best = (ld)M; }
                        }
                    } else {
                        // al < 0: G > 0 između korijena
                        lll D = be * be - 4 * al * ga;
                        if (D > 0) {
                            // G > 0 na (r1, r2); postoji pozitivan dio na [M, inf) <=> M < r2.
                            // Egzaktno: G(M) > 0 znači r1 < M < r2; G(M) == 0 znači M je korijen,
                            // a M < vrh (= -be/(2al)) razlikuje r1 od r2.
                            lll GM = al * M * M + be * M + ga;
                            lll vertexCmp = -be - 2 * al * M;  // < 0  <=>  M < vrh (jer 2al < 0)
                            if (GM > 0) infinite = true;
                            else if (GM == 0) {
                                if (vertexCmp < 0) infinite = true;  // M je manji korijen
                                else { cnt = 1; best = (ld)M; }
                            } else {
                                // G(M) < 0: M je lijevo od r1 ili desno od r2
                                if (vertexCmp < 0) infinite = true;  // M < r1 -> (r1,r2) desno od M
                                else cnt = 0;
                            }
                        } else if (D == 0) {
                            // dvostruki korijen r0 = -be/(2al) >= M ?
                            lll t = -be - 2 * al * M;  // sgn(r0 - M) = sgn(t) * sgn(2al) = -sgn(t)
                            if (t <= 0) { cnt = 1; best = -(ld)be / (2 * (ld)al); }
                        }
                    }
                }
            }
        }
        if (infinite) out += "-1\n";
        else if (cnt == 0) out += "0\n";
        else {
            snprintf(buf, sizeof(buf), "%d %.12Lf\n", cnt, best);
            out += buf;
        }
    }
    fputs(out.c_str(), stdout);
    return 0;
}
