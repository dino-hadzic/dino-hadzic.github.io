#include <algorithm>
#include <iostream>
#include <numeric>
#include <vector>

struct DSU {
  size_t id;
  std::vector<size_t> pa, size;

  explicit DSU(size_t size_, size_t m)
      : id(size_ * 2), pa(size_ * 2 + m), size(size_ * 2 + m, 1) {
    // prva polovica size zapravo se ne koristi, samo pojednostavljuje računanje indeksa
    std::iota(pa.begin(), pa.begin() + size_,
              size_);  // i pokazuje na virtualni čvor i + size_
    std::iota(pa.begin() + size_, pa.end(), size_);  // svi virtualni čvorovi pokazuju sami na sebe
  }

  size_t find(size_t x) { return pa[x] == x ? x : pa[x] = find(pa[x]); }

  void unite(size_t x, size_t y) {
    x = find(x), y = find(y);
    if (x == y) return;
    if (size[x] < size[y]) std::swap(x, y);
    pa[y] = x;
    size[x] += size[y];
  }

  void erase(size_t x) {
    size_t y = find(x);
    --size[y];
    pa[x] = id++;
  }
};

int main() {
  int n, m, case_id = 0;
  while ((std::cin >> n >> m), n) {
    DSU dsu(n, m);
    for (; m; --m) {
      char ch;
      std::cin >> ch;
      if (ch == 'M') {
        int x, y;
        std::cin >> x >> y;
        dsu.unite(x, y);
      } else if (ch == 'S') {
        int x;
        std::cin >> x;
        dsu.erase(x);
      }
    }
    int res = 0;
    for (int i = n; i < dsu.id; ++i) {
      if (dsu.size[i] && i == dsu.find(i)) {
        ++res;
      }
    }
    std::cout << "Case #" << (++case_id) << ": " << res << '\n';
  }
  return 0;
}
