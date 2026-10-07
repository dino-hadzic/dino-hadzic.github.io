// --8<-- [start:full-text]
#include <iostream>
#include <tuple>

// Ovdje promijenite želite li drukčije strategije balansiranja i spajanja.
#define BALANCE_BY_ROTATING 0
#define ROTATE_BY_JOINING 1

constexpr int N = 2e5;
constexpr double ALPHA = 0.292;

int id, rt, ch[N][2], sz[N], val[N], lz[N];
int pool[N], top;

void push_up(int x) { sz[x] = sz[ch[x][0]] + sz[ch[x][1]]; }

void lazy_reverse(int x) {
  if (!x) return;
  std::swap(ch[x][0], ch[x][1]);
  lz[x] ^= 1;
}

void push_down(int x) {
  if (lz[x]) {
    lazy_reverse(ch[x][0]);
    lazy_reverse(ch[x][1]);
    lz[x] = 0;
  }
}

// Vrati novi prazan čvor.
int new_node() {
  int x = top ? pool[--top] : ++id;
  sz[x] = val[x] = ch[x][0] = ch[x][1] = 0;
  return x;
}

// Oslobodi čvor za kasniju upotrebu.
void del_node(int& x) {
  pool[top++] = x;
  x = 0;
}

// Vrati novi list s vrijednošću v.
int new_leaf(int v) {
  int x = new_node();
  val[x] = v;
  sz[x] = 1;
  return x;
}

// Vrati novi čvor s podstablima x i y.
int join(int x, int y) {
  int z = new_node();
  ch[z][0] = x;
  ch[z][1] = y;
  push_up(z);
  return z;
}

// Vrati podstabla čvora x i oslobodi x.
auto cut(int& x) {
  push_down(x);
  int y = ch[x][0];
  int z = ch[x][1];
  del_node(x);
  return std::make_pair(y, z);
}

// Provjeri je li podstablo težine SX preteško
//     u stablu težine SX + SY.
bool too_heavy(int sx, int sy) {
  // ili sx > sy * 3;
  return sy < ALPHA * (sx + sy);
}

#if BALANCE_BY_ROTATING

#if ROTATE_BY_JOINING

// Rotiraj podstablo u x tako da ch[x][r] postane novi korijen.
void rotate(int& x, bool r) {
  int a, b, c, d;
  std::tie(a, b) = cut(x);
  if (r) {
    std::tie(c, d) = cut(b);
    x = join(join(a, c), d);
  } else {
    std::tie(c, d) = cut(a);
    x = join(c, join(d, b));
  }
}

#else

// Rotiraj podstablo u x tako da ch[x][r] postane novi korijen.
void rotate(int& x, bool r) {
  int y = ch[x][r];
  ch[x][r] = ch[y][!r];
  ch[y][!r] = x;
  push_up(x);
  push_up(y);
  x = y;
}

#endif

// Provjeri je li ch[x][!r] pretežak pa je potrebna dvostruka rotacija.
bool need_double_rotation(int x, bool r) {
  // ili sz[ch[x][!r]] > sz[ch[x][r]] * 2;
  return sz[ch[x][!r]] > sz[x] / (2 - ALPHA);
}

// Balansiraj podstablo u x;
void balance(int& x) {
  if (sz[x] == 1) return;
  push_down(x);
  bool r = sz[ch[x][1]] > sz[ch[x][0]];
  if (!too_heavy(sz[ch[x][r]], sz[ch[x][!r]])) return;
  push_down(ch[x][r]);
  if (need_double_rotation(ch[x][r], r)) {
    push_down(ch[ch[x][r]][!r]);
    rotate(ch[x][r], !r);
  }
  rotate(x, r);
}

// Spoji dva podstabla.
int merge(int x, int y) {
  if (!x || !y) return x | y;
  int a, b;
  if (too_heavy(sz[x], sz[y])) {
    std::tie(a, b) = cut(x);
    int z = join(a, merge(b, y));
    balance(z);
    return z;
  } else if (too_heavy(sz[y], sz[x])) {
    std::tie(a, b) = cut(y);
    int z = join(merge(x, a), b);
    balance(z);
    return z;
  } else {
    return join(x, y);
  }
}

#else

// Spoji dva podstabla.
int merge(int x, int y) {
  if (!x || !y) return x | y;
  int a, b, c, d;
  if (too_heavy(sz[x], sz[y])) {
    std::tie(a, b) = cut(x);
    if (too_heavy(sz[b] + sz[y], sz[a])) {
      std::tie(c, d) = cut(b);
      return merge(merge(a, c), merge(d, y));
    } else {
      return merge(a, merge(b, y));
    }
  } else if (too_heavy(sz[y], sz[x])) {
    std::tie(a, b) = cut(y);
    if (too_heavy(sz[a] + sz[x], sz[b])) {
      std::tie(c, d) = cut(a);
      return merge(merge(x, c), merge(d, b));
    } else {
      return merge(merge(x, a), b);
    }
  } else {
    return join(x, y);
  }
}

// Balansiraj podstablo u x;
void balance(int& x) {
  if (sz[x] == 1) return;
  if (too_heavy(sz[ch[x][0]], sz[ch[x][1]]) ||
      too_heavy(sz[ch[x][1]], sz[ch[x][0]])) {
    int a, b;
    std::tie(a, b) = cut(x);
    x = merge(a, b);
  }
}

#endif

// --8<-- [start:split]
// Razdvoji podstablo u x.
// Lijeva polovica imat će k elemenata.
std::pair<int, int> split(int x, int k) {
  if (!x) return {0, 0};
  if (!k) return {0, x};
  if (k == sz[x]) return {x, 0};
  int a, b;
  std::tie(a, b) = cut(x);
  if (k <= sz[a]) {
    int ll, rr;
    std::tie(ll, rr) = split(a, k);
    return {ll, merge(rr, b)};
  } else {
    int ll, rr;
    std::tie(ll, rr) = split(b, k - sz[a]);
    return {merge(a, ll), rr};
  }
}

// --8<-- [end:split]
// Okreni interval [l, r].
void reverse(int l, int r) {
  int ll, rr;
  std::tie(rt, rr) = split(rt, r);
  std::tie(ll, rt) = split(rt, l - 1);
  lazy_reverse(rt);
  rt = merge(ll, merge(rt, rr));
}

// Ispiši podstablo u x.
void print(int x) {
  if (sz[x] == 1) {
    std::cout << val[x] << ' ';
  } else {
    push_down(x);
    print(ch[x][0]);
    print(ch[x][1]);
  }
}

// Ispiši stablo.
void print() {
  print(rt);
  std::cout << '\n';
}

// --8<-- [start:build]
// Izgradi stablo za interval [ll, rr].
int build(int ll, int rr) {
  if (ll == rr) return new_leaf(ll);
  int mm = (ll + rr) / 2;
  return join(build(ll, mm), build(mm + 1, rr));
}

// --8<-- [end:build]
int main() {
  int n, m;
  std::cin >> n >> m;
  rt = build(1, n);
  for (; m; --m) {
    int l, r;
    std::cin >> l >> r;
    reverse(l, r);
  }
  print();
  return 0;
}

// --8<-- [end:full-text]
