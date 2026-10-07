---
title: Segment tree po vrijednostima u Fenwick treeu
---

Problem [statičkog $k$-tog najmanjeg na intervalu (POJ 2104 K-th Number)](http://poj.org/problem?id=2104) može se riješiti [segment treeom po vrijednostima](./persistent-seg.md) u vremenu $O(n\log n)$.

Što ako interval postane dinamičan? Odnosno, što ako treba podržati još jednu operaciju: promjenu vrijednosti na jednoj poziciji?

??? note "Primjer zadatka [二逼平衡树 (ugniježđena stabla)](https://loj.ac/problem/106)"
    Održavajte niz u kojem treba podržati sljedeće operacije:
    
    -   upit ranga vrijednosti $x$ na intervalu;
    -   upit vrijednosti s rangom $k$ na intervalu;
    -   promjena vrijednosti na nekoj poziciji;
    -   upit prethodnika vrijednosti $x$ na intervalu (prethodnik je najveći broj manji od $x$);
    -   upit sljedbenika vrijednosti $x$ na intervalu (sljedbenik je najmanji broj veći od $x$).

??? note "Primjer zadatka [Luogu P2617 Dynamic Rankings](https://www.luogu.com.cn/problem/P2617)"
    Zadan je niz $a_1,a_2 \dots a_n$ od $n$ brojeva; treba podržati dvije operacije:
    
    -   `Q l r k`: upit $k$-tog najmanjeg među brojevima s indeksima u intervalu $[l,r]$
    -   `C x y`: postavi $a_x$ na $y$

Ako, kako je opisano u članku [Balansirano stablo u segment treeu](./balanced-in-seg.md), za svaki čvor segment treea održavamo balansirano stablo nad intervalom koji taj čvor predstavlja i $k$-ti najmanji tražimo binarnim pretraživanjem, svaki upit pokriva više intervala, tj. više čvorova, a balansirano stablo ne može istodobno pretraživati više vrijednosti, pa je složenost $O(n\log^3 n)$, što nije optimalno.

Ideja optimizacije jest spojiti binarno pretraživanje po odgovoru i brojanje elemenata manjih od zadane vrijednosti u jedno: koristimo **segment tree u čijim su čvorovima dinamički segment treeovi po vrijednostima**. Budući da svi unutarnji segment treeovi imaju istu strukturu, binarno pretraživanje po segment treeu možemo provoditi na više stabala istodobno.

Pri promjeni se u vanjskom segment treeu spuštamo od korijena do mijenjane pozicije; u dinamičkom segment treeu po vrijednostima svakog posjećenog čvora obrišemo staru vrijednost i umetnemo novu. Prolazimo kroz $O(\log n)$ čvorova vanjskog stabla, a jedna promjena u dinamičkom segment treeu po vrijednostima košta $O(\log n)$, pa je složenost promjene $O(\log^2 n)$.

Pri upitu najprije izdvojimo sve čvorove vanjskog segment treea koji pokrivaju traženi interval, a zatim, slično kao kod statičkog $k$-tog najmanjeg, sve te čvorove istodobno spuštamo u lijevo ili desno dijete. Ako je zbroj vrijednosti u lijevoj djeci svih tih čvorova barem $k$, idemo ulijevo, inače udesno. Interval pokriva najviše $O(\log n)$ čvorova, pa se istodobno spušta najviše toliko čvorova; vremenska složenost je $O(\log^2 n)$.

Budući da segment tree ima veliku konstantu, u implementaciji se vanjsko stablo često zamjenjuje **Fenwick treeom**, koji ima manju konstantu i zgodnije barata prefiksnim sumama. Prostorna složenost je $O(n\log^2 n)$, pa **pazite na memorijsko ograničenje**.

Evo jedne implementacije:

??? note "Implementacija"
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
    
    struct segment_tree  // enkapsulirani dinamički segment tree po vrijednostima
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
    
    // implementacija Fenwick treeom
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
    
    // implementacija segment treeom
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
