---
title: Value segment tree nested in a Fenwick tree
---

The problem of the [static $k$-th smallest element in a range (POJ 2104 K-th Number)](http://poj.org/problem?id=2104) can be solved with a [value segment tree](./persistent-seg.md) in $O(n\log n)$ time.

What if the range becomes dynamic? That is, what if we also have to support one more operation: changing the value at a single position?

??? note "Example problem [二逼平衡树 (nested trees)](https://loj.ac/problem/106)"
    Maintain a sequence that supports the following operations:
    
    -   query the rank of $x$ in a range;
    -   query the value with rank $k$ in a range;
    -   change the value at some position;
    -   query the predecessor of $x$ in a range (the predecessor is the largest number smaller than $x$);
    -   query the successor of $x$ in a range (the successor is the smallest number larger than $x$).

??? note "Example problem [Luogu P2617 Dynamic Rankings](https://www.luogu.com.cn/problem/P2617)"
    Given a sequence $a_1,a_2 \dots a_n$ of $n$ numbers, support two operations:
    
    -   `Q l r k`: query the $k$-th smallest number among those with indices in $[l,r]$
    -   `C x y`: set $a_x$ to $y$

If, as described in [Balanced tree nested in a segment tree](./balanced-in-seg.md), we maintain a balanced tree for every node of a segment tree over the range the node represents and then binary search for the $k$-th smallest value, every query covers several ranges, i.e., several nodes, and a balanced tree cannot search several values at once, so the time complexity is $O(n\log^3 n)$, which is not optimal.

The idea of the optimization is to combine the binary search on the answer with the counting of elements smaller than a value, using a **segment tree whose nodes hold dynamically allocated value segment trees**. Since all the inner segment trees have the same structure, the binary search on a segment tree can be carried out on several trees simultaneously.

For an update we first walk down the outer segment tree from the root to the modified position; in the dynamic value segment tree of every visited node we delete the old value and insert the new one. We pass through $O(\log n)$ nodes of the outer tree, and one update of a dynamic value segment tree costs $O(\log n)$, so the time complexity of an update is $O(\log^2 n)$.

For a query we first collect all the nodes of the outer segment tree that cover the range, and then, similarly to the static $k$-th smallest problem, move all these nodes to their left or right children simultaneously. If the values stored in the left children of all these nodes sum to at least $k$, we go left, otherwise right. Since a range covers at most $O(\log n)$ nodes, at most that many nodes move down at a time, and the time complexity is $O(\log^2 n)$.

Since segment trees have a large constant factor, the outer tree is in practice often implemented with a **Fenwick tree**, which has a smaller constant and handles prefix sums more conveniently. The space complexity is $O(n\log^2 n)$, so **mind the memory limit**.

One implementation:

??? note "Implementation"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <cstring>
    #include <map>
    #include <set>
    #define LC o << 1
    #define RC o << 1 | 1
    using namespace std;
    constexpr int MAXN = 1000010;
    int n, m, a[MAXN], u[MAXN], x[MAXN], l[MAXN], r[MAXN], k[MAXN], cur, cur1, cur2,
        q1[MAXN], q2[MAXN], v[MAXN];
    char op[MAXN];
    set<int> ST;
    map<int, int> mp;
    
    struct segment_tree  // encapsulated dynamically allocated value segment tree
    {
      int cur, rt[MAXN * 4], sum[MAXN * 60], lc[MAXN * 60], rc[MAXN * 60];
    
      void build(int& o) { o = ++cur; }
    
      void print(int o, int l, int r) {
        if (!o) return;
        if (l == r && sum[o]) printf("%d ", l);
        int mid = (l + r) >> 1;
        print(lc[o], l, mid);
        print(rc[o], mid + 1, r);
      }
    
      void update(int& o, int l, int r, int x, int v) {
        if (!o) o = ++cur;
        sum[o] += v;
        if (l == r) return;
        int mid = (l + r) >> 1;
        if (x <= mid)
          update(lc[o], l, mid, x, v);
        else
          update(rc[o], mid + 1, r, x, v);
      }
    } st;
    
    // Fenwick tree implementation
    namepace fenwick_impl {
      int lowbit(int o) { return (o & (-o)); }
    
      void upd(int o, int x, int v) {
        for (; o <= n; o += lowbit(o)) st.update(st.rt[o], 1, n, x, v);
      }
    
      void gtv(int o, int* A, int& p) {
        p = 0;
        for (; o; o -= lowbit(o)) A[++p] = st.rt[o];
      }
    
      int qry(int l, int r, int k) {
        if (l == r) return l;
        int mid = (l + r) >> 1, siz = 0;
        for (int i = 1; i <= cur1; i++) siz += st.sum[st.lc[q1[i]]];
        for (int i = 1; i <= cur2; i++) siz -= st.sum[st.lc[q2[i]]];
        // printf("j %d %d %d %d\n",cur1,cur2,siz,k);
        if (siz >= k) {
          for (int i = 1; i <= cur1; i++) q1[i] = st.lc[q1[i]];
          for (int i = 1; i <= cur2; i++) q2[i] = st.lc[q2[i]];
          return qry(l, mid, k);
        } else {
          for (int i = 1; i <= cur1; i++) q1[i] = st.rc[q1[i]];
          for (int i = 1; i <= cur2; i++) q2[i] = st.rc[q2[i]];
          return qry(mid + 1, r, k - siz);
        }
      }
    }
    using namespace fenwick_impl;
    
    // segment tree implementation
    namespace segtree_impl {
    void build(int o, int l, int r) {
      st.build(st.rt[o]);
      if (l == r) return;
      int mid = (l + r) >> 1;
      build(LC, l, mid);
      build(RC, mid + 1, r);
    }
    
    void print(int o, int l, int r) {
      printf("%d %d:", l, r);
      st.print(st.rt[o], 1, n);
      printf("\n");
      if (l == r) return;
      int mid = (l + r) >> 1;
      print(LC, l, mid);
      print(RC, mid + 1, r);
    }
    
    void update(int o, int l, int r, int q, int x, int v) {
      st.update(st.rt[o], 1, n, x, v);
      if (l == r) return;
      int mid = (l + r) >> 1;
      if (q <= mid)
        update(LC, l, mid, q, x, v);
      else
        update(RC, mid + 1, r, q, x, v);
    }
    
    void getval(int o, int l, int r, int ql, int qr) {
      if (l > qr || r < ql) return;
      if (ql <= l && r <= qr) {
        q[++cur] = st.rt[o];
        return;
      }
      int mid = (l + r) >> 1;
      getval(LC, l, mid, ql, qr);
      getval(RC, mid + 1, r, ql, qr);
    }
    
    int query(int l, int r, int k) {
      if (l == r) return l;
      int mid = (l + r) >> 1, siz = 0;
      for (int i = 1; i <= cur; i++) siz += st.sum[st.lc[q[i]]];
      if (siz >= k) {
        for (int i = 1; i <= cur; i++) q[i] = st.lc[q[i]];
        return query(l, mid, k);
      } else {
        for (int i = 1; i <= cur; i++) q[i] = st.rc[q[i]];
        return query(mid + 1, r, k - siz);
      }
    }
    }  // namespace segtree_impl
    
    int main() {
      scanf("%d%d", &n, &m);
      for (int i = 1; i <= n; i++) scanf("%d", a + i), ST.insert(a[i]);
      for (int i = 1; i <= m; i++) {
        scanf(" %c", op + i);
        if (op[i] == 'C')
          scanf("%d%d", u + i, x + i), ST.insert(x[i]);
        else
          scanf("%d%d%d", l + i, r + i, k + i);
      }
      for (set<int>::iterator it = ST.begin(); it != ST.end(); it++)
        mp[*it] = ++cur, v[cur] = *it;
      for (int i = 1; i <= n; i++) a[i] = mp[a[i]];
      for (int i = 1; i <= m; i++)
        if (op[i] == 'C') x[i] = mp[x[i]];
      n += m;
      // build(1,1,n);
      for (int i = 1; i <= n; i++) upd(i, a[i], 1);
      // print(1,1,n);
      for (int i = 1; i <= m; i++) {
        if (op[i] == 'C') {
          upd(u[i], a[u[i]], -1);
          upd(u[i], x[i], 1);
          a[u[i]] = x[i];
        } else {
          gtv(r[i], q1, cur1);
          gtv(l[i] - 1, q2, cur2);
          printf("%d\n", v[qry(1, n, k[i])]);
        }
      }
      return 0;
    }
    ```
