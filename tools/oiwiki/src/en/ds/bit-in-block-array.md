---
title: Fenwick tree nested in sqrt decomposition
---

## Introduction

Under certain conditions, a Fenwick tree nested in sqrt decomposition can do some of the things that nested trees can do, but compared with nested trees the code is much shorter and easier to implement.

## A simple example

A simple example is counting the points inside a rectangular region of the plane.

???+ note "Rectangle query"
    Given $n$ points $(x_i, y_i)$ in the plane, where $1 \le i \le n, 1 \le x_i, y_i \le n, 1 \le n \le 10^5$, support the following operations:
    
    1.  Given $a, b, c, d$, report the number of points inside the rectangle with upper-left corner $(a, b)$ and lower-right corner $(c, d)$.
    2.  Given $x, y$, change the y-coordinate of the point with x-coordinate $x$ to $y$.
    
    The problem is **forced online**, and it is guaranteed that $x_i \ne x_j(1 \le i, j \le n, i \ne j)$.

Operation 1 can be turned into 4 two-dimensional dominance queries by inclusion-exclusion on the rectangle. Since the problem is forced online, offline algorithms such as CDQ divide and conquer cannot be used, which leads to nested trees, e.g. a treap nested in a Fenwick tree. This does solve the problem, but the code is too long and not particularly easy to write.

Note that the problem additionally guarantees $x_i \ne x_j(1 \le i, j \le n, i \ne j)$; this is exactly when a Fenwick tree nested in sqrt decomposition can be used.

### Initialization

First, each $x$ corresponds to exactly one $y$, so this mapping can be stored in an array: let $Y_i$ be the y-coordinate of the point with x-coordinate $i$.

Then split the x-coordinates into blocks of size $\sqrt n$. Build a value Fenwick tree for every block. Let $T_i$ be the Fenwick tree of the $i$-th block, and $T_{i, j}$ the number of points in block $i$ whose y-coordinate lies in $(j - lowbit(j), j]$.

### Query

Turn operation 1 into 4 two-dimensional dominance queries. Now we only need to answer, for given $a, b$, how many points satisfy $1 \le x_i \le a, 1\le y_i \le b$.

The range of x-coordinates to query is $[1, a]$. Since the rightmost part of the range may not be a complete block, scan this part by brute force, check whether $Y_i \le b$, and count the points in this part that satisfy the condition.

Now only the complete blocks remain. Scan the preceding blocks by brute force, query the number of values smaller than $b$ in the Fenwick tree of each block, and add it to the answer.

Is that all? No: note that processing the complete blocks is really a prefix-sum query on $T$, so if we also handle $T$ with the Fenwick tree technique during updates, the query complexity gets lower.

### Update

The plain approach is to first find the block containing point $x$, then do one subtraction and one addition, i.e. two point updates in value Fenwick trees, and finally set $Y_x$ to $y$.

With the optimization described above, we also walk through $T$ as in a Fenwick tree update, and each update is again one subtraction and one addition, i.e. two point updates in value Fenwick trees.

Slightly changing the steps above, e.g. doing only the subtraction instead of a subtraction and an addition, gives point deletion; doing only the addition gives point insertion. But keep in mind that each $x$ may correspond to only one $y$.

### Space complexity

There are $\sqrt n$ blocks, and the Fenwick tree of each block takes $O(n)$ space, so the space complexity is $O(n \sqrt n)$.

### Time complexity

For a query, scanning the incomplete block costs $O(\sqrt n)$. Then we do a Fenwick tree query on $T$, and for each visited $T_i$ another Fenwick tree query, which costs $O(\log (\sqrt n) \log n)$. So the time complexity of a query is $O (\sqrt n + \log (\sqrt n) \log n)$.

An update has the same complexity as a query, $O (\sqrt n + \log (\sqrt n) \log n)$.

## Example 1

???+ note "[Intersection of Permutations](https://codeforces.com/problemset/problem/1093/E)"
    Given two permutations $a$ and $b$, support the following two operations:
    
    1.  Given $l_a, r_a, l_b, r_b$, report the number of elements that appear both in $a[l_a ... r_a]$ and in $b[l_b ... r_b]$.
    2.  Given $x, y$, perform $swap(b_x, b_y)$.
    
    The length $n$ of the sequences satisfies $2 \le n \le 2 \cdot 10^5$, and the number of operations $q$ satisfies $1 \le q \le 2 \cdot 10^5$.

For every value $i$, let $x_i$ be its index in permutation $b$ and $y_i$ its index in permutation $a$. Then operation 1 becomes a query for the number of points in a rectangle, and operation 2 can be seen as two updates. Moreover, since these are permutations, each $x$ corresponds to exactly one $y$, so this problem can be solved with a Fenwick tree nested in sqrt decomposition.

??? note "Sample code (Fenwick tree in sqrt decomposition – 1 s)"
    ```cpp
    #include <cmath>
    #include <cstdio>
    using namespace std;
    constexpr int N = 2e5 + 5;
    constexpr int M = 447 + 5;  // sqrt(N) + 5
    
    int n, m, pa[N], pb[N];
    
    int nn, block_size, block_cnt, block_id[N], L[N], R[N], T[M][N];
    
    void build(int n) {
      nn = n;
      block_size = sqrt(nn);
      block_cnt = nn / block_size;
      for (int i = 1; i <= block_cnt; ++i) {
        L[i] = R[i - 1] + 1;
        R[i] = i * block_size;
      }
      if (R[block_cnt] < nn) {
        ++block_cnt;
        L[block_cnt] = R[block_cnt - 1] + 1;
        R[block_cnt] = nn;
      }
      for (int j = 1; j <= block_cnt; ++j)
        for (int i = L[j]; i <= R[j]; ++i) block_id[i] = j;
    }
    
    int lb(int x) { return x & -x; }
    
    void add(int p, int v, int d) {
      for (int i = block_id[p]; i <= block_cnt; i += lb(i))
        for (int j = v; j <= nn; j += lb(j)) T[i][j] += d;
    }
    
    int getsum(int p, int v) {
      if (!p) return 0;
      int res = 0;
      int id = block_id[p];
      for (int i = L[id]; i <= p; ++i)
        if (pb[i] <= v) ++res;
      for (int i = id - 1; i; i -= lb(i))
        for (int j = v; j; j -= lb(j)) res += T[i][j];
      return res;
    }
    
    void update(int x, int y) {
      add(x, pb[x], -1);
      add(y, pb[y], -1);
      swap(pb[x], pb[y]);
      add(x, pb[x], 1);
      add(y, pb[y], 1);
    }
    
    int query(int la, int ra, int lb, int rb) {
      int res = getsum(rb, ra) - getsum(rb, la - 1) - getsum(lb - 1, ra) +
                getsum(lb - 1, la - 1);
      return res;
    }
    
    int main() {
      scanf("%d %d", &n, &m);
      int v;
      for (int i = 1; i <= n; ++i) scanf("%d", &v), pa[v] = i;
      for (int i = 1; i <= n; ++i) scanf("%d", &v), pb[i] = pa[v];
    
      build(n);
      for (int i = 1; i <= n; ++i) add(i, pb[i], 1);
    
      int op, la, lb, ra, rb, x, y;
      for (int i = 1; i <= m; ++i) {
        scanf("%d", &op);
        if (op == 1) {
          scanf("%d %d %d %d", &la, &ra, &lb, &rb);
          printf("%d\n", query(la, ra, lb, rb));
        } else if (op == 2) {
          scanf("%d %d", &x, &y);
          update(x, y);
        }
      }
      return 0;
    }
    ```

??? note "Sample code (treap in a Fenwick tree – TLE)"
    ```cpp
    #include <cstdio>
    #include <random>
    using namespace std;
    constexpr int N = 2e5 + 5;
    mt19937 rng(random_device{}());
    
    int n, m, pa[N], pb[N];
    
    // Treap
    struct Treap {
      struct node {
        node *l, *r;
        int sz, rnd, v;
    
        node(int _v) : l(NULL), r(NULL), sz(1), rnd(rng()), v(_v) {}
      };
    
      int get_size(node*& p) { return p ? p->sz : 0; }
    
      void push_up(node*& p) {
        if (!p) return;
        p->sz = get_size(p->l) + get_size(p->r) + 1;
      }
    
      node* root;
    
      node* merge(node* a, node* b) {
        if (!a) return b;
        if (!b) return a;
        if (a->rnd < b->rnd) {
          a->r = merge(a->r, b);
          push_up(a);
          return a;
        } else {
          b->l = merge(a, b->l);
          push_up(b);
          return b;
        }
      }
    
      void split_val(node* p, const int& k, node*& a, node*& b) {
        if (!p)
          a = b = NULL;
        else {
          if (p->v <= k) {
            a = p;
            split_val(p->r, k, a->r, b);
            push_up(a);
          } else {
            b = p;
            split_val(p->l, k, a, b->l);
            push_up(b);
          }
        }
      }
    
      void split_size(node* p, int k, node*& a, node*& b) {
        if (!p)
          a = b = NULL;
        else {
          if (get_size(p->l) <= k) {
            a = p;
            split_size(p->r, k - get_size(p->l), a->r, b);
            push_up(a);
          } else {
            b = p;
            split_size(p->l, k, a, b->l);
            push_up(b);
          }
        }
      }
    
      void ins(int val) {
        node *a, *b;
        split_val(root, val, a, b);
        a = merge(a, new node(val));
        root = merge(a, b);
      }
    
      void del(int val) {
        node *a, *b, *c, *d;
        split_val(root, val, a, b);
        split_val(a, val - 1, c, d);
        delete d;
        root = merge(c, b);
      }
    
      int qry(int val) {
        node *a, *b;
        split_val(root, val, a, b);
        int res = get_size(a);
        root = merge(a, b);
        return res;
      }
    
      int qry(int l, int r) { return qry(r) - qry(l - 1); }
    };
    
    // Fenwick Tree
    Treap T[N];
    
    int lb(int x) { return x & -x; }
    
    void ins(int x, int v) {
      for (; x <= n; x += lb(x)) T[x].ins(v);
    }
    
    void del(int x, int v) {
      for (; x <= n; x += lb(x)) T[x].del(v);
    }
    
    int qry(int x, int mi, int ma) {
      int res = 0;
      for (; x; x -= lb(x)) res += T[x].qry(mi, ma);
      return res;
    }
    
    int main() {
      scanf("%d %d", &n, &m);
      int v;
      for (int i = 1; i <= n; ++i) scanf("%d", &v), pa[v] = i;
      for (int i = 1; i <= n; ++i) scanf("%d", &v), pb[i] = pa[v];
      for (int i = 1; i <= n; ++i) ins(i, pb[i]);
    
      int op, la, lb, ra, rb, x, y;
      for (int i = 1; i <= m; ++i) {
        scanf("%d", &op);
        if (op == 1) {
          scanf("%d %d %d %d", &la, &ra, &lb, &rb);
          printf("%d\n", qry(rb, la, ra) - qry(lb - 1, la, ra));
        } else if (op == 2) {
          scanf("%d %d", &x, &y);
          del(x, pb[x]);
          del(y, pb[y]);
          swap(pb[x], pb[y]);
          ins(x, pb[x]);
          ins(y, pb[y]);
        }
      }
      return 0;
    }
    ```

## Example 2

???+ note "[Complicated Computations](https://codeforces.com/contest/1436/problem/E)"
    Given a sequence $a$, let $b$ be the array consisting of the MEX of every contiguous subsequence of $a$; find the MEX of $b$. The MEX of a sequence is the smallest **positive integer** that does not appear in it.
    
    The length $n$ of the sequence satisfies $1 \le n \le 10^5$.

**Observation**: the MEX of a sequence is $mex$ if and only if the sequence contains all of $1$ to $mex-1$ but does not contain $mex$.

Check in turn whether there is a contiguous subsequence with MEX equal to $1, \dots, n+1$. If there is no contiguous subsequence with MEX $i$, the answer is $i$. If all of them exist, the answer is $n + 2$.

When checking $i$, view the sequence as several segments separated by zero or more occurrences of $i$. If there is a segment that contains all of $1$ to $i - 1$ but does not contain $i$, then there is a contiguous subsequence with MEX $i$.

Use an array $Y_j$ to record the position of the previous element with value $a_j$; take $j$ as $x$, $Y_j$ as $y$ and $a_j$ as $z$. Then deciding whether a segment contains all of $1$ to $i - 1$ becomes a three-dimensional dominance problem. Formally, deciding whether the MEX of the segment $[l, r]$ is $i$ means checking whether the number of points satisfying $l \le j \le r, Y_j \le l - 1, a_j \le i - 1$ equals $i-1$.

If the points corresponding to value $i$ are inserted only after the check for $i$ is done, then $[l, r]$ contains only elements with $a_j \le i - 1$, so the three-dimensional dominance problem above reduces to a two-dimensional one.

??? note "Sample code (Fenwick tree in sqrt decomposition – 78 ms)"
    ```cpp
    #include <cmath>
    #include <cstdio>
    #include <vector>
    using namespace std;
    constexpr int N = 1e5 + 5;
    constexpr int M = 316 + 5;  // sqrt(N) + 5
    
    // sqrt decomposition
    int nn, b[N], block_size, block_cnt, block_id[N], L[N], R[N], T[M][N];
    
    void build(int n) {
      nn = n;
      block_size = sqrt(nn);
      block_cnt = nn / block_size;
      for (int i = 1; i <= block_cnt; ++i) {
        L[i] = R[i - 1] + 1;
        R[i] = i * block_size;
      }
      if (R[block_cnt] < nn) {
        ++block_cnt;
        L[block_cnt] = R[block_cnt - 1] + 1;
        R[block_cnt] = nn;
      }
      for (int j = 1; j <= block_cnt; ++j)
        for (int i = L[j]; i <= R[j]; ++i) block_id[i] = j;
    }
    
    int lb(int x) { return x & -x; }
    
    // d = 1: add point (p, v)
    // d = -1: remove point (p, v)
    void add(int p, int v, int d) {
      for (int i = block_id[p]; i <= block_cnt; i += lb(i))
        for (int j = v; j <= nn; j += lb(j)) T[i][j] += d;
    }
    
    // query: how many points in [1, r] have y-coordinate <= val
    int getsum(int p, int v) {
      if (!p) return 0;
      int res = 0;
      int id = block_id[p];
      for (int i = L[id]; i <= p; ++i)
        if (b[i] && b[i] <= v) ++res;
      for (int i = id - 1; i; i -= lb(i))
        for (int j = v; j; j -= lb(j)) res += T[i][j];
      return res;
    }
    
    // query: how many points in [l, r] have y-coordinate <= val
    int query(int l, int r, int val) {
      if (l > r) return -1;
      int res = getsum(r, val) - getsum(l - 1, val);
      return res;
    }
    
    // add point (p, v)
    void update(int p, int v) {
      b[p] = v;
      add(p, v, 1);
    }
    
    int n, a[N];
    vector<int> g[N];
    
    int main() {
      scanf("%d", &n);
    
      // sentinel elements were added to reduce the case analysis
      // adding at index 0 of a Fenwick tree may loop forever, so everything is shifted right by one
      // a_1 and a_{n+2} are sentinels
      for (int i = 2; i <= n + 1; ++i) scanf("%d", &a[i]);
      for (int i = 2; i <= n + 1; ++i) g[a[i]].push_back(i);
    
      // sqrt decomposition
      build(n + 2);
    
      int ans = n + 2, lst, ok;
      for (int i = 1; i <= n + 1; ++i) {
        g[i].push_back(n + 2);
    
        lst = 1;
        ok = 0;
        for (int pos : g[i]) {
          if (query(lst + 1, pos - 1, lst) == i - 1) {
            ok = 1;
            break;
          }
          lst = pos;
        }
    
        if (!ok) {
          ans = i;
          break;
        }
    
        lst = 1;
        g[i].pop_back();
        for (int pos : g[i]) {
          update(pos, lst);
          lst = pos;
        }
      }
      printf("%d\n", ans);
      return 0;
    }
    ```

??? note "Sample code (treap in a segment tree – 468 ms)"
    ```cpp
    #include <cstdio>
    #include <random>
    #include <vector>
    using namespace std;
    constexpr int N = 1e5 + 5;
    
    vector<int> g[N];
    int n, a[N];
    
    mt19937 rng(random_device{}());
    
    struct Treap {
      struct node {
        node *l, *r;
        unsigned rnd;
        int sz, v;
    
        node(int _v) : l(NULL), r(NULL), rnd(rng()), sz(1), v(_v) {}
      };
    
      int get_size(node*& p) { return p ? p->sz : 0; }
    
      void push_up(node*& p) {
        if (!p) return;
        p->sz = get_size(p->l) + get_size(p->r) + 1;
      }
    
      node* root;
    
      node* merge(node* a, node* b) {
        if (!a) return b;
        if (!b) return a;
        if (a->rnd < b->rnd) {
          a->r = merge(a->r, b);
          push_up(a);
          return a;
        } else {
          b->l = merge(a, b->l);
          push_up(b);
          return b;
        }
      }
    
      void split_val(node* p, const int& k, node*& a, node*& b) {
        if (!p)
          a = b = NULL;
        else {
          if (p->v <= k) {
            a = p;
            split_val(p->r, k, a->r, b);
            push_up(a);
          } else {
            b = p;
            split_val(p->l, k, a, b->l);
            push_up(b);
          }
        }
      }
    
      void split_size(node* p, int k, node*& a, node*& b) {
        if (!p)
          a = b = NULL;
        else {
          if (get_size(p->l) <= k) {
            a = p;
            split_size(p->r, k - get_size(p->l), a->r, b);
            push_up(a);
          } else {
            b = p;
            split_size(p->l, k, a, b->l);
            push_up(b);
          }
        }
      }
    
      void insert(int val) {
        node *a, *b;
        split_val(root, val, a, b);
        a = merge(a, new node(val));
        root = merge(a, b);
      }
    
      int query(int val) {
        node *a, *b;
        split_val(root, val, a, b);
        int res = get_size(a);
        root = merge(a, b);
        return res;
      }
    
      int qry(int l, int r) { return query(r) - query(l - 1); }
    };
    
    // Segment Tree
    Treap T[N << 2];
    
    void insert(int x, int l, int r, int p, int val) {
      T[x].insert(val);
      if (l == r) return;
      int mid = (l + r) >> 1;
      if (p <= mid)
        insert(x << 1, l, mid, p, val);
      else
        insert(x << 1 | 1, mid + 1, r, p, val);
    }
    
    int query(int x, int l, int r, int L, int R, int val) {
      if (l == L && r == R) return T[x].query(val);
      int mid = (l + r) >> 1;
      if (R <= mid) return query(x << 1, l, mid, L, R, val);
      if (L > mid) return query(x << 1 | 1, mid + 1, r, L, R, val);
      return query(x << 1, l, mid, L, mid, val) +
             query(x << 1 | 1, mid + 1, r, mid + 1, R, val);
    }
    
    int query(int l, int r, int val) {
      if (l > r) return -1;
      return query(1, 1, n, l, r, val);
    }
    
    int main() {
      scanf("%d", &n);
      for (int i = 1; i <= n; ++i) scanf("%d", &a[i]);
      for (int i = 1; i <= n; ++i) g[a[i]].push_back(i);
    
      // a_0 and a_{n+1} are sentinels
      int ans = n + 2, lst, ok;
      for (int i = 1; i <= n + 1; ++i) {
        g[i].push_back(n + 1);
    
        lst = 0;
        ok = 0;
        for (int pos : g[i]) {
          if (query(lst + 1, pos - 1, lst) == i - 1) {
            ok = 1;
            break;
          }
          lst = pos;
        }
    
        if (!ok) {
          ans = i;
          break;
        }
    
        lst = 0;
        g[i].pop_back();
        for (int pos : g[i]) {
          insert(1, 1, n, pos, lst);
          lst = pos;
        }
      }
      printf("%d\n", ans);
      return 0;
    }
    ```
