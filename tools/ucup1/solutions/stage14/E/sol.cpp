// E. LaLa and Monster Hunting (Part 1)
// Ishodište je u konveksnoj ljusci krugova ako ga neki krug sadrži ili ako
// tangentne zrake iz ishodišta na sve krugove ne stanu u jednu (zatvorenu)
// poluravninu, tj. ako između susjednih kutova zraka nema praznine >= pi.
#include <bits/stdc++.h>
using namespace std;

static char buf[1 << 25];
int pos = 0, len = 0;
inline int gc() {
    if (pos == len) { len = (int)fread(buf, 1, sizeof(buf), stdin); pos = 0; if (len <= 0) return -1; }
    return buf[pos++];
}
inline long long readInt() {
    int c = gc();
    while (c != '-' && (c < '0' || c > '9')) c = gc();
    bool neg = false;
    if (c == '-') { neg = true; c = gc(); }
    long long x = 0;
    while (c >= '0' && c <= '9') { x = x * 10 + (c - '0'); c = gc(); }
    return neg ? -x : x;
}

int main() {
    int n = (int)readInt();
    vector<double> ang;
    ang.reserve(2 * n);
    const double PI = acos(-1.0);
    for (int i = 0; i < n; i++) {
        long long x = readInt(), y = readInt(), r = readInt();
        // krug sadrži ishodište (uključivo rub) -> ljuska ga sigurno sadrži
        if (x * x + y * y <= r * r) { puts("Yes"); return 0; }
        double d = sqrt((double)(x * x + y * y));
        double t = atan2((double)y, (double)x);      // smjer prema središtu
        double a = asin((double)r / d);                // polukut vidnog stošca
        ang.push_back(t - a);                          // dvije tangentne zrake
        ang.push_back(t + a);
    }
    // normaliziraj kutove u [0, 2pi) i sortiraj
    for (double& t : ang) {
        while (t < 0) t += 2 * PI;
        while (t >= 2 * PI) t -= 2 * PI;
    }
    sort(ang.begin(), ang.end());
    // najveća kružna praznina između susjednih zraka
    double gap = ang.front() + 2 * PI - ang.back();
    for (size_t i = 1; i < ang.size(); i++) gap = max(gap, ang[i] - ang[i - 1]);
    // praznina >= pi  <=>  sve zrake (pa i svi krugovi) su u jednoj poluravnini
    puts(gap >= PI ? "No" : "Yes");
    return 0;
}
