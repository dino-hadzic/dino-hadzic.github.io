// UCup 1, Stage 18, F: X Equals Y
// Po duljini zajedničkog zapisa: duljina 1 -> x = y (a = b = 2);
// duljina 2 -> x = t*a + d, y = t*b + d; enumeriramo vodeću znamenku t <= sqrt(x),
// tada b - a = (y - x)/t pa a mora biti u presjeku nekoliko intervala;
// duljina >= 3 -> a <= sqrt(x), b <= sqrt(y): izračunamo sve zapise i tražimo jednake.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;

vector<int> digitsOf(ll x, ll base) {
    vector<int> d;
    while (x > 0) {
        d.push_back(x % base);
        x /= base;
    }
    return d;
}

ull hashDigits(const vector<int>& d) {
    ull h = 1469598103934665603ULL;
    for (int v : d) {
        h ^= (ull)v + 0x9e3779b97f4a7c15ULL;
        h *= 1099511628211ULL;
        h ^= h >> 29;
    }
    return h ^ (ull)d.size();
}

int main() {
    int T;
    if (scanf("%d", &T) != 1) return 0;
    while (T--) {
        ll x, y, A, B;
        if (scanf("%lld %lld %lld %lld", &x, &y, &A, &B) != 4) return 0;
        if (x == y) {
            puts("YES\n2 2");
            continue;
        }
        bool found = false;
        ll ansA = 0, ansB = 0;
        // duljina 2: vodeća znamenka t, t*t < x i t*t < y
        for (ll t = 1; t * t < x && t * t < y && !found; t++) {
            if ((y - x) % t != 0) continue;
            ll delta = (y - x) / t;  // b = a + delta
            // uvjeti na a: t*a <= x < (t+1)*a, a > t, 2 <= a <= A
            ll lo = max({x / (t + 1) + 1, t + 1, 2LL});
            ll hi = min(x / t, A);
            // uvjeti na b: t*b <= y < (t+1)*b, b > t, 2 <= b <= B  ->  na a = b - delta
            lo = max(lo, max({y / (t + 1) + 1, t + 1, 2LL}) - delta);
            hi = min(hi, min(y / t, B) - delta);
            if (lo <= hi) {
                found = true;
                ansA = lo;
                ansB = lo + delta;
            }
        }
        if (!found) {
            // duljina >= 3: a*a <= x, b*b <= y
            unordered_map<ull, ll> seen;
            seen.reserve(1 << 16);
            for (ll a = 2; a * a <= x && a <= A; a++) {
                vector<int> d = digitsOf(x, a);
                seen.emplace(hashDigits(d), a);
            }
            for (ll b = 2; b * b <= y && b <= B && !found; b++) {
                vector<int> d = digitsOf(y, b);
                auto it = seen.find(hashDigits(d));
                if (it != seen.end() && digitsOf(x, it->second) == d) {
                    found = true;
                    ansA = it->second;
                    ansB = b;
                }
            }
        }
        if (found) printf("YES\n%lld %lld\n", ansA, ansB);
        else puts("NO");
    }
    return 0;
}
