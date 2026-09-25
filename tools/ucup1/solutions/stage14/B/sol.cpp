// B. LaLa and Magic Circle (LaLa Version)
// Oblik konačnog konveksnog poligona: multiskup vektora bridova se ne mijenja,
// pa ih samo sortiramo po kutu. Položaj: najveća y-koordinata konačnog poligona
// je Y + U, gdje je Y trenutni maksimum, a U zbroj visina ograničenih trapeza
// horizontalne trapezne dekompozicije vanjštine iz kojih se do beskonačnosti
// izlazi "prema gore". Trapez između lijevog zida e (brid ide gore) i desnog
// zida f (brid ide dolje) je "gore" točno kad se f obilazi prije e (gledano od
// vrha ljuske). Isto u zarotiranim koordinatama daje najveći x.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

struct Edge {
    ll lx, ly, hx, hy;   // donja i gornja točka (hy > ly)
    bool up;             // ide li brid prema gore u smjeru obilaska
    int idx;             // redni broj brida od vrha konveksne ljuske
};

// usporedba po x na sredini zajedničkog raspona visina (bridovi se ne sijeku)
struct Cmp {
    bool operator()(const Edge& e, const Edge& f) const {
        ll lo = max(e.ly, f.ly), hi = min(e.hy, f.hy), ym2 = lo + hi;
        ll dye = e.hy - e.ly, dyf = f.hy - f.ly;
        ll A = 2 * e.lx * dye * dyf + (ym2 - 2 * e.ly) * (e.hx - e.lx) * dyf;
        ll B = 2 * f.lx * dye * dyf + (ym2 - 2 * f.ly) * (f.hx - f.lx) * dye;
        if (A != B) return A < B;
        return e.idx < f.idx;
    }
};

// zbroj visina "gornjih" ograničenih trapeza + najveći y = konačni najveći y
ll finalMaxY(vector<pair<ll, ll>> P) {
    int n = P.size();
    int s = min_element(P.begin(), P.end()) - P.begin();   // vrh na ljusci
    rotate(P.begin(), P.begin() + s, P.end());
    vector<Edge> E;
    for (int i = 0; i < n; i++) {
        auto a = P[i], b = P[(i + 1) % n];
        if (a.second == b.second) continue;                 // horizontalni ne utječu
        bool up = b.second > a.second;
        if (!up) swap(a, b);
        E.push_back({a.first, a.second, b.first, b.second, up, i});
    }
    vector<ll> ys;
    for (auto& p : P) ys.push_back(p.second);
    sort(ys.begin(), ys.end()); ys.erase(unique(ys.begin(), ys.end()), ys.end());
    vector<vector<int>> startAt(ys.size()), endAt(ys.size());
    auto id = [&](ll y) { return int(lower_bound(ys.begin(), ys.end(), y) - ys.begin()); };
    for (int i = 0; i < (int)E.size(); i++) { startAt[id(E[i].ly)].push_back(i); endAt[id(E[i].hy)].push_back(i); }

    set<Edge, Cmp> S;
    ll cnt = 0, U = 0;
    auto contrib = [&](set<Edge, Cmp>::iterator a, set<Edge, Cmp>::iterator b) -> ll {
        if (a == S.end() || b == S.end()) return 0;
        return (a->up && !b->up && b->idx < a->idx) ? 1 : 0;
    };
    auto prevIt = [&](set<Edge, Cmp>::iterator it) { return it == S.begin() ? S.end() : prev(it); };
    for (size_t k = 0; k < ys.size(); k++) {
        for (int i : endAt[k]) {
            auto it = S.find(E[i]);
            auto p = prevIt(it), q = next(it);
            cnt -= contrib(p, it) + contrib(it, q);
            S.erase(it);
            cnt += contrib(p, q);
        }
        for (int i : startAt[k]) {
            auto it = S.insert(E[i]).first;
            auto p = prevIt(it), q = next(it);
            cnt -= contrib(p, q);
            cnt += contrib(p, it) + contrib(it, q);
        }
        if (k + 1 < ys.size()) U += (ys[k + 1] - ys[k]) * cnt;
    }
    return ys.back() + U;
}

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    vector<pair<ll, ll>> P(n);
    for (auto& p : P) scanf("%lld %lld", &p.first, &p.second);

    ll Yf = finalMaxY(P);
    vector<pair<ll, ll>> R(n);                      // rotacija za +90°: (x,y) -> (-y,x)
    for (int i = 0; i < n; i++) R[i] = {-P[i].second, P[i].first};
    ll Xf = finalMaxY(R);

    // oblik: vektori bridova sortirani po kutu, spojeni istosmjerni
    vector<pair<ll, ll>> d(n);
    for (int i = 0; i < n; i++) d[i] = {P[(i + 1) % n].first - P[i].first, P[(i + 1) % n].second - P[i].second};
    auto half = [](const pair<ll, ll>& v) { return (v.second < 0 || (v.second == 0 && v.first < 0)) ? 1 : 0; };
    sort(d.begin(), d.end(), [&](const pair<ll, ll>& a, const pair<ll, ll>& b) {
        if (half(a) != half(b)) return half(a) < half(b);
        return a.first * b.second - a.second * b.first > 0;
    });
    vector<pair<ll, ll>> m;
    for (auto& v : d) {
        if (!m.empty() && m.back().first * v.second - m.back().second * v.first == 0 &&
            m.back().first * v.first + m.back().second * v.second > 0) {
            m.back().first += v.first; m.back().second += v.second;
        } else m.push_back(v);
    }
    int M = m.size();
    vector<pair<ll, ll>> V(M);
    V[0] = {0, 0};
    for (int i = 1; i < M; i++) V[i] = {V[i - 1].first + m[i - 1].first, V[i - 1].second + m[i - 1].second};
    ll mx = LLONG_MIN, my = LLONG_MIN;
    for (auto& v : V) { mx = max(mx, v.first); my = max(my, v.second); }
    for (auto& v : V) { v.first += Xf - mx; v.second += Yf - my; }
    int s = min_element(V.begin(), V.end()) - V.begin();
    rotate(V.begin(), V.begin() + s, V.end());
    printf("%d\n", M);
    for (auto& v : V) printf("%lld %lld\n", v.first, v.second);
    return 0;
}
