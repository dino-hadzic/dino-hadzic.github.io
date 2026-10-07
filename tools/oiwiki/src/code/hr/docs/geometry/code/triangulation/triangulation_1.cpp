// --8<-- [start:delaunay]
#include <algorithm>
#include <cmath>
#include <limits>
#include <utility>
#include <vector>

using data_t = double;

struct Point {
  data_t x, y;
  int id;
};

class Delaunay {
  // Svaki neusmjereni brid sastoji se od četiri mjesta (slota)
  // Parna mjesta predstavljaju dva smjera u izvornom grafu, neparna dualne bridove
  // Sve veze čuvaju indekse, da iteratori ne postanu nevažeći
  struct Edge {
    int origin, next;
  };

  std::vector<Point> p;
  std::vector<Edge> edges;
  std::vector<int> free_edges;

  // Približno određivanje predznaka s relativnom tolerancijom
  static int sign(data_t value, data_t scale) {
    const data_t tolerance =
        16 * std::numeric_limits<data_t>::epsilon() * scale;
    return (value > tolerance) - (value < -tolerance);
  }

  static int cross(const Point& a, const Point& b, const Point& c) {
    data_t u = (b.x - a.x) * (c.y - a.y);
    data_t v = (b.y - a.y) * (c.x - a.x);
    return sign(u - v, std::abs(u) + std::abs(v));
  }

  // Ako su a, b, c poredani suprotno od kazaljke na satu, provjerava je li d unutar opisane kružnice
  static bool in_circle(const Point& a, const Point& b, const Point& c,
                        const Point& d) {
    data_t ax = a.x - d.x, ay = a.y - d.y;
    data_t bx = b.x - d.x, by = b.y - d.y;
    data_t cx = c.x - d.x, cy = c.y - d.y;
    data_t a2 = ax * ax + ay * ay, b2 = bx * bx + by * by,
           c2 = cx * cx + cy * cy;
    data_t bc1 = bx * cy, bc2 = by * cx;
    data_t ca1 = cx * ay, ca2 = cy * ax;
    data_t ab1 = ax * by, ab2 = ay * bx;
    data_t det = a2 * (bc1 - bc2) + b2 * (ca1 - ca2) + c2 * (ab1 - ab2);
    // Apsolutne vrijednosti zbrajamo prije oduzimanja, da zbog kraćenja ne podcijenimo pogrešku zaokruživanja
    data_t scale = a2 * (std::abs(bc1) + std::abs(bc2)) +
                   b2 * (std::abs(ca1) + std::abs(ca2)) +
                   c2 * (std::abs(ab1) + std::abs(ab2));
    return sign(det, scale) > 0;
  }

  static int rot(int e) { return (e & ~3) | ((e + 1) & 3); }

  static int rev(int e) { return e ^ 2; }

  int org(int e) const { return edges[e].origin; }

  int dest(int e) const { return org(rev(e)); }

  // Bridovi s istim početkom čine kružnu vezanu listu u smjeru suprotnom od kazaljke na satu
  int onext(int e) const { return edges[e].next; }

  int oprev(int e) const { return rot(onext(rot(e))); }

  // Pomak za jedan brid naprijed duž ruba strane lijevo od e
  int lnext(int e) const { return rot(onext(rev(rot(e)))); }

  bool left_of(int v, int e) const {
    return cross(p[org(e)], p[dest(e)], p[v]) > 0;
  }

  bool right_of(int v, int e) const {
    return cross(p[org(e)], p[dest(e)], p[v]) < 0;
  }

  int make_edge(int u, int v) {
    int e;
    if (free_edges.empty()) {
      e = (int)edges.size();
      edges.resize(edges.size() + 4);
    } else {
      e = free_edges.back();
      free_edges.pop_back();
    }
    edges[e] = {u, e};
    edges[e + 1] = {-1, e + 3};
    edges[e + 2] = {v, e + 2};
    edges[e + 3] = {-1, e + 1};
    return e;
  }

  // Zamjenjuje sljedbenike dvaju bridova i istodobno ažurira veze u dualnom grafu
  void splice(int a, int b) {
    int alpha = rot(onext(a)), beta = rot(onext(b));
    std::swap(edges[a].next, edges[b].next);
    std::swap(edges[alpha].next, edges[beta].next);
  }

  void delete_edge(int e) {
    splice(e, oprev(e));
    splice(rev(e), oprev(rev(e)));
    e &= ~3;
    edges[e].origin = edges[e + 2].origin = -1;
    free_edges.push_back(e);
  }

  // Dodaje brid od kraja brida a do početka brida b
  int connect(int a, int b) {
    int e = make_edge(dest(a), org(b));
    splice(e, lnext(a));
    splice(rev(e), b);
    return e;
  }

  // Vraća bridove ljuske koji kreću iz najljevijeg odnosno najdesnijeg vrha, tako da je vanjska strana redom desno odnosno lijevo
  // Interval je [l, r); rekurzija obrađuje samo slučajeve s barem dvije točke
  std::pair<int, int> divide(int l, int r) {
    if (r - l == 2) {
      int a = make_edge(l, l + 1);
      return {a, rev(a)};
    }
    if (r - l == 3) {
      int a = make_edge(l, l + 1), b = make_edge(l + 1, l + 2);
      splice(rev(a), b);
      int turn = cross(p[l], p[l + 1], p[l + 2]);
      if (turn == 0) return {a, rev(b)};  // kolinearne točke: zadržavamo samo bridove između susjednih točaka
      int c = connect(b, a);
      if (turn > 0) return {a, rev(b)};
      return {rev(c), c};
    }

    int m = l + (r - l) / 2;
    auto left = divide(l, m), right = divide(m, r);
    int ldo = left.first, ldi = left.second;
    int rdi = right.first, rdo = right.second;
    // Od bridova ljuske vraćenih iz rekurzije krećemo se duž ljuske tražeći donju zajedničku tangentu
    while (true) {
      if (left_of(org(rdi), ldi)) {
        ldi = lnext(ldi);
      } else if (right_of(org(ldi), rdi)) {
        rdi = onext(rev(rdi));
      } else {
        break;
      }
    }
    int base = connect(rev(rdi), ldi);  // base ide s desne strane prema lijevoj
    if (org(ldi) == org(ldo)) ldo = rev(base);
    if (org(rdi) == org(rdo)) rdo = base;

    while (true) {
      // Kandidati dolaze iz uređene kružne liste susjeda, pa je dovoljno pogledati prethodnika ili sljedbenika trenutnog brida
      int lcand = onext(rev(base));
      if (right_of(dest(lcand), base)) {
        while (in_circle(p[dest(base)], p[org(base)], p[dest(lcand)],
                         p[dest(onext(lcand))])) {
          int next = onext(lcand);
          delete_edge(lcand);
          lcand = next;
        }
      }
      int rcand = oprev(base);
      if (right_of(dest(rcand), base)) {
        while (in_circle(p[dest(base)], p[org(base)], p[dest(rcand)],
                         p[dest(oprev(rcand))])) {
          int prev = oprev(rcand);
          delete_edge(rcand);
          rcand = prev;
        }
      }
      bool lvalid = right_of(dest(lcand), base);
      bool rvalid = right_of(dest(rcand), base);
      if (!lvalid && !rvalid) break;  // stigli smo do gornje zajedničke tangente
      if (!lvalid || (rvalid && in_circle(p[dest(lcand)], p[org(lcand)],
                                          p[org(rcand)], p[dest(rcand)]))) {
        base = connect(rcand, rev(base));
      } else {
        base = connect(rev(base), rev(lcand));
      }
    }
    return {ldo, rdo};
  }

 public:
  // Točke moraju biti međusobno različite, a id-ovi jedinstveni
  void init(std::vector<Point> points) {
    p = std::move(points);
    edges.clear();
    free_edges.clear();
    std::sort(p.begin(), p.end(), [](const Point& a, const Point& b) {
      return a.x < b.x || (a.x == b.x && a.y < b.y);
    });
    if (p.size() >= 2) divide(0, (int)p.size());
  }

  // Svaki neusmjereni brid vraća se samo jednom; krajevi su označeni izvornim ulaznim id-ovima
  std::vector<std::pair<int, int>> getEdge() const {
    std::vector<std::pair<int, int>> result;
    for (int e = 0; e < (int)edges.size(); e += 4) {
      if (org(e) != -1) result.emplace_back(p[org(e)].id, p[dest(e)].id);
    }
    return result;
  }
};

// --8<-- [end:delaunay]

#include <iostream>

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);
  int n;
  if (!(std::cin >> n)) return 0;
  std::vector<Point> points(n);
  for (int i = 0; i < n; ++i) {
    std::cin >> points[i].x >> points[i].y;
    points[i].id = i;
  }
  Delaunay dt;
  dt.init(std::move(points));
  auto edges = dt.getEdge();
  for (auto& edge : edges) {
    if (edge.first > edge.second) std::swap(edge.first, edge.second);
  }
  std::sort(edges.begin(), edges.end());
  std::cout << edges.size() << '\n';
  for (const auto& edge : edges) {
    std::cout << edge.first << ' ' << edge.second << '\n';
  }
}
