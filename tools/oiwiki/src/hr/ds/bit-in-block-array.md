---
title: Fenwick tree u dekompoziciji na blokove
---

## Uvod

Fenwick tree u dekompoziciji na blokove pod određenim uvjetima može obaviti dio posla koji inače rade ugniježđena stabla, ali je u usporedbi s njima kod znatno kraći i lakši za implementaciju.

## Jednostavan primjer

Jednostavan je primjer upit o broju točaka unutar pravokutnog područja u ravnini.

???+ note "Upit o pravokutnom području"
    Zadano je $n$ točaka $(x_i, y_i)$ u ravnini, gdje je $1 \le i \le n, 1 \le x_i, y_i \le n, 1 \le n \le 10^5$. Treba podržati sljedeće operacije:
    
    1.  Za zadane $a, b, c, d$ odgovoriti koliko točaka leži u pravokutniku s gornjim lijevim kutom $(a, b)$ i donjim desnim kutom $(c, d)$.
    2.  Za zadane $x, y$ promijeniti ordinatu točke s apscisom $x$ na $y$.
    
    Zadatak je **forsirano online**, a garantira se $x_i \ne x_j(1 \le i, j \le n, i \ne j)$.

Operaciju 1 možemo uključenjem-isključenjem na pravokutniku svesti na 4 upita dvodimenzionalnog dominiranja. Budući da je zadatak forsirano online, offline algoritmi poput CDQ divide and conquera ne pomažu, pa se nameću ugniježđena stabla, npr. treap u Fenwick treeu. To doista rješava zadatak, ali kod je predugačak i nije ga baš jednostavno napisati.

Primijetimo da zadatak dodatno garantira $x_i \ne x_j(1 \le i, j \le n, i \ne j)$; upravo tada možemo upotrijebiti Fenwick tree u dekompoziciji na blokove.

### Inicijalizacija

Prvo, svakom $x$ odgovara točno jedan $y$, pa to preslikavanje možemo zapisati u niz: neka $Y_i$ označava ordinatu točke s apscisom $i$.

Zatim apscise podijelimo na blokove veličine $\sqrt n$. Za svaki blok izgradimo Fenwick tree po vrijednostima. Neka je $T_i$ Fenwick tree $i$-tog bloka, a $T_{i, j}$ broj točaka u bloku $i$ čija je ordinata u $(j - lowbit(j), j]$.

### Upit

Operaciju 1 svedemo na 4 upita dvodimenzionalnog dominiranja. Sada samo treba, za zadane $a, b$, odgovoriti koliko točaka zadovoljava $1 \le x_i \le a, 1\le y_i \le b$.

Raspon apscisa koji ispitujemo je $[1, a]$. Budući da krajnji desni dio raspona možda nije cijeli blok, taj dio prođemo grubom silom i za svaku točku provjerimo vrijedi li $Y_i \le b$ te prebrojimo one koje zadovoljavaju uvjet.

Preostaju samo cijeli blokovi. Grubom silom prođemo sve prethodne blokove, u Fenwick treeu svakog bloka upitamo broj vrijednosti manjih od $b$ i to pribrojimo odgovoru.

I to je sve? Nije: primijetimo da je obrada cijelih blokova zapravo upit prefiksne sume nad $T$, pa ako i pri promjeni $T$ obrađujemo Fenwick-tehnikom, upit će imati manju složenost.

### Promjena

Uobičajeni je postupak najprije pronaći blok u kojem se nalazi točka $x$, zatim napraviti jedno oduzimanje i jedno dodavanje, tj. dvije promjene u jednoj točki Fenwick treea po vrijednostima, i na kraju postaviti $Y_x$ na $y$.

Ako koristimo gore opisanu optimizaciju, onda i po $T$ prolazimo kao pri promjeni u Fenwick treeu, a svaka promjena opet znači jedno oduzimanje i jedno dodavanje, tj. dvije promjene u jednoj točki Fenwick treea po vrijednostima.

Malom izmjenom gornjih koraka, npr. ako umjesto oduzimanja i dodavanja radimo samo oduzimanje, dobivamo brisanje točke; ako radimo samo dodavanje, dobivamo dodavanje točke. Pritom treba paziti da jednom $x$ smije odgovarati samo jedan $y$.

### Prostorna složenost

Imamo $\sqrt n$ blokova, a Fenwick tree svakog bloka zauzima $O(n)$ prostora, pa je prostorna složenost $O(n \sqrt n)$.

### Vremenska složenost

Pri upitu prolazak necijelog bloka košta $O(\sqrt n)$. Zatim po $T$ radimo upit kao u Fenwick treeu, a za svaki posjećeni $T_i$ također radimo upit u Fenwick treeu, što ukupno košta $O(\log (\sqrt n) \log n)$. Vremenska je složenost upita stoga $O (\sqrt n + \log (\sqrt n) \log n)$.

Promjena ima istu složenost kao upit, $O (\sqrt n + \log (\sqrt n) \log n)$.

## Primjer 1

???+ note "[Intersection of Permutations](https://codeforces.com/problemset/problem/1093/E)"
    Zadane su dvije permutacije $a$ i $b$; treba podržati sljedeće dvije operacije:
    
    1.  Za zadane $l_a, r_a, l_b, r_b$ odgovoriti koliko elemenata se pojavljuje i u $a[l_a ... r_a]$ i u $b[l_b ... r_b]$.
    2.  Za zadane $x, y$ izvršiti $swap(b_x, b_y)$.
    
    Duljina niza $n$ zadovoljava $2 \le n \le 2 \cdot 10^5$, a broj operacija $q$ zadovoljava $1 \le q \le 2 \cdot 10^5$.

Za svaku vrijednost $i$ neka je $x_i$ njezin indeks u permutaciji $b$, a $y_i$ njezin indeks u permutaciji $a$. Tako operacija 1 postaje upit o broju točaka u pravokutnom području, a operaciju 2 možemo promatrati kao dvije promjene. Budući da su u pitanju permutacije, jednom $x$ odgovara točno jedan $y$, pa se zadatak može riješiti Fenwick treeom u dekompoziciji na blokove.

??? note "Primjer koda (Fenwick tree u dekompoziciji na blokove – 1 s)"
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

??? note "Primjer koda (treap u Fenwick treeu – TLE)"
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

## Primjer 2

???+ note "[Complicated Computations](https://codeforces.com/contest/1436/problem/E)"
    Zadan je niz $a$. Neka je $b$ niz sastavljen od MEX-ova svih uzastopnih podnizova niza $a$; traži se MEX niza $b$. MEX niza najmanji je **pozitivan cijeli broj** koji se u nizu ne pojavljuje.
    
    Duljina niza $n$ zadovoljava $1 \le n \le 10^5$.

**Opažanje**: MEX niza jednak je $mex$ ako i samo ako niz sadrži sve brojeve od $1$ do $mex-1$, ali ne sadrži $mex$.

Redom provjeravamo postoji li uzastopni podniz s MEX-om jednakim $1, \dots, n+1$. Ako ne postoji uzastopni podniz s MEX-om $i$, odgovor je $i$. Ako svi postoje, odgovor je $n + 2$.

Pri provjeri za $i$ promatramo niz kao više segmenata razdvojenih s nula ili više pojavljivanja vrijednosti $i$. Ako postoji segment koji sadrži sve brojeve od $1$ do $i - 1$, a ne sadrži $i$, onda postoji uzastopni podniz s MEX-om $i$.

Nizom $Y_j$ pamtimo poziciju prethodnog elementa s vrijednošću $a_j$; $j$ uzmemo kao $x$, $Y_j$ kao $y$, a $a_j$ kao $z$. Tako provjera sadrži li segment sve brojeve od $1$ do $i - 1$ postaje problem trodimenzionalnog dominiranja. Formalno, provjeriti je li MEX segmenta $[l, r]$ jednak $i$ znači provjeriti je li broj točaka koje zadovoljavaju $l \le j \le r, Y_j \le l - 1, a_j \le i - 1$ jednak $i-1$.

Ako točke koje odgovaraju vrijednosti $i$ umetnemo tek nakon što smo za $i$ obavili provjeru, tada u $[l, r]$ postoje samo elementi s $a_j \le i - 1$, pa se gornji trodimenzionalni problem svodi na dvodimenzionalni.

??? note "Primjer koda (Fenwick tree u dekompoziciji na blokove – 78 ms)"
    ```cpp
    #include <cmath>
    #include <cstdio>
    #include <vector>
    using namespace std;
    constexpr int N = 1e5 + 5;
    constexpr int M = 316 + 5;  // sqrt(N) + 5
    
    // dekompozicija na blokove
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
    
    // d = 1: dodaj točku (p, v)
    // d = -1: ukloni točku (p, v)
    void add(int p, int v, int d) {
      for (int i = block_id[p]; i <= block_cnt; i += lb(i))
        for (int j = v; j <= nn; j += lb(j)) T[i][j] += d;
    }
    
    // upit: koliko točaka u [1, r] ima ordinatu <= val
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
    
    // upit: koliko točaka u [l, r] ima ordinatu <= val
    int query(int l, int r, int val) {
      if (l > r) return -1;
      int res = getsum(r, val) - getsum(l - 1, val);
      return res;
    }
    
    // dodaj točku (p, v)
    void update(int p, int v) {
      b[p] = v;
      add(p, v, 1);
    }
    
    int n, a[N];
    vector<int> g[N];
    
    int main() {
      scanf("%d", &n);
    
      // radi manje razlikovanja slučajeva dodani su granični (sentinel) elementi
      // indeks 0 bi pri dodavanju u Fenwick tree uzrokovao beskonačnu petlju, pa je sve pomaknuto za jedno mjesto udesno
      // a_1 i a_{n+2} su granični elementi
      for (int i = 2; i <= n + 1; ++i) scanf("%d", &a[i]);
      for (int i = 2; i <= n + 1; ++i) g[a[i]].push_back(i);
    
      // dekompozicija na blokove
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

??? note "Primjer koda (treap u segment treeu – 468 ms)"
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
    
      // a_0 i a_{n+1} su granični elementi
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
