---
title: Mo algoritam na stablu
---

## Mo algoritam na stablu preko zagradnog niza

Obični Mo algoritam (Mo's algorithm) može rješavati samo linearne probleme, pa stablo moramo „na silu” spljoštiti u niz.

Možemo izračunati zagradni niz (bracket sequence) stabla, podijeliti ga na blokove i na njemu pokrenuti Mo algoritam.

Kako to konkretno izvesti?

### Postupak

DFS-om gradimo zagradni niz stabla (pri ulasku u čvor $x$ dodajemo $x$ u niz, pri izlasku iz čvora $x$ ponovno dodajemo $x$ u niz; ukupna duljina niza je $2N$).

Neka je $st_x$ vrijeme ulaska u $x$, a $ed_x$ vrijeme izlaska iz $x$.

Prema svojstvima zagradnog niza, za put $u \to v$ u stablu (bez smanjenja općenitosti neka je $st_u \le st_v$) vrijedi:

-   Ako je $\text{LCA}(u, v) = u$, čvorovi na putu pojavljuju se u intervalu $[st_u, st_v]$ točno 1 put, a čvorovi koji nisu na putu pojavljuju se 0 ili 2 puta.
-   Ako je $\text{LCA}(u, v) \neq u$, čvorovi na putu osim $\text{LCA}(u, v)$ pojavljuju se u intervalu $[ed_u, st_v]$ točno 1 put, a čvorovi koji nisu na putu pojavljuju se 0 ili 2 puta. Pazite da $\text{LCA}(u, v)$ treba posebno razmotriti: on se pojavljuje 0 puta.

Stoga, dok izvodimo Mo algoritam, bez obzira na to je li čvor na koji naiđemo ulazak ili izlazak, u biti se mijenja broj pojavljivanja tog čvora u trenutnom intervalu. Dovoljno je održavati koliko se puta svaki čvor $x$ pojavio: čvorovi s 0 ili 2 pojavljivanja nisu u skupu čvorova puta koji trenutno održavamo, a čvorovi s 1 pojavljivanjem jesu. Zato, kad pokazivači Mo algoritma dođu na $[st_u, st_v]$, dobivamo gotovo točno skup čvorova puta $u \to v$ u stablu.

U stvarnoj implementaciji možemo održavati broj pojavljivanja svakog čvora $x$ modulo 2; to pokazuje je li se čvor $x$ pojavio ili nije. Tada je pri pomicanju pokazivača svako ažuriranje, bilo dodavanje bilo brisanje, zapravo promjena (flip) stanja pojavljivanja tog čvora $x$.

Pazite: pri obradi upita s $\text{LCA} \neq u$, nakon što pokazivači Mo algoritma dođu na mjesto, moramo privremeno ručno dodati $\text{LCA}(u, v)$ u skup (promijeniti mu stanje), izračunati i zabilježiti odgovor na taj upit, a zatim $\text{LCA}(u, v)$ opet izbaciti iz skupa (ponovno promijeniti stanje), kako ne bi ometao daljnje pomicanje pokazivača.

### Primjer zadatka

???+ note "Primjer zadatka [「WC2013」糖果公园 (Park slatkiša)](https://uoj.ac/problem/58)"
    Zadatak: zadano je stablo u kojem $i$-ti čvor ima boju $c_i$; svaki upit zadaje put $u_i$, $v_i$ i za taj put traži se
    
    $\sum_{c}val_c\sum_{i=1}^{cnt_c}w_i$
    
    pri čemu je $val$ vrijednost te boje, $cnt$ broj pojavljivanja boje, a $w$ vrijednost koju boja daje kad se pojavi $i$-ti put.

#### Postupak

Najprije stablo pretvorimo u niz; zatim pri svakom dodavanju/brisanju čvora njegov doprinos odgovoru možemo dobiti u vremenu $O(1)$, tj. $val_c\times w_{cnt_{c+1}}$.

Primjećujemo da će se pritom prijeći i podstablo početnog čvora, što daje suvišan doprinos. Što učiniti?

Budući da će čvorovi u podstablu početnog čvora tijekom prolaska sigurno biti prijeđeni dvaput, njihov je doprinos 0.

Zato možemo uvesti niz $vis$ i svaki put kad prijeđemo čvor x napraviti XOR vrijednosti $vis_x$ s 1.

Ako je $vis_x=0$, doprinos tog čvora ne računamo.

Dakle, zadatak se može riješiti Mo algoritmom na stablu.

Za izmjene je dovoljno dodati vremensku dimenziju, čime dobivamo Mo algoritam na stablu s izmjenama.

Zatim, budući da obuhvaćeni interval možda ne sadrži LCA, u tom slučaju treba ukloniti suvišan doprinos – i to je sve.

#### Implementacija

??? note "Referentni kôd"
    ```cpp
    #include <algorithm>
    #include <cmath>
    #include <cstdio>
    using namespace std;
    
    constexpr int MAXN = 200010;
    
    int f[MAXN], g[MAXN], id[MAXN], head[MAXN], cnt, last[MAXN], dep[MAXN],
        fa[MAXN][22], v[MAXN], w[MAXN];
    int block, index, n, m, q;
    int pos[MAXN], col[MAXN], app[MAXN];
    bool vis[MAXN];
    long long ans[MAXN], cur;
    
    struct edge {
      int to, nxt;
    } e[MAXN];
    
    int cnt1 = 0, cnt2 = 0;  // vremenske oznake
    
    struct query {
      int l, r, t, id;
    
      bool operator<(const query &b) const {
        return (pos[l] < pos[b.l]) || (pos[l] == pos[b.l] && pos[r] < pos[b.r]) ||
               (pos[l] == pos[b.l] && pos[r] == pos[b.r] && t < b.t);
      }
    } a[MAXN], b[MAXN];
    
    void addedge(int x, int y) {
      e[++cnt] = edge{y, head[x]};
      head[x] = cnt;
    }
    
    void dfs(int x) {
      id[f[x] = ++index] = x;
      for (int i = head[x]; i; i = e[i].nxt) {
        if (e[i].to != fa[x][0]) {
          fa[e[i].to][0] = x;
          dep[e[i].to] = dep[x] + 1;
          dfs(e[i].to);
        }
      }
      id[g[x] = ++index] = x;  // zagradni niz
    }
    
    int lca(int x, int y) {
      if (dep[x] < dep[y]) swap(x, y);
      if (dep[x] != dep[y]) {  // popni se na istu dubinu
        int dis = dep[x] - dep[y];
        for (int i = 20; i >= 0; i--)
          if (dis >= (1 << i)) dis -= 1 << i, x = fa[x][i];
      }
      if (x == y) return x;
      for (int i = 20; i >= 0; i--) {
        if (fa[x][i] != fa[y][i]) x = fa[x][i], y = fa[y][i];
      }
      return fa[x][0];
    }
    
    void add(int x) {
      if (vis[x])
        cur -= (long long)v[col[x]] * w[app[col[x]]--];
      else
        cur += (long long)v[col[x]] * w[++app[col[x]]];
      vis[x] ^= 1;
    }
    
    // pomicanje u vremenskoj dimenziji
    void modify(int x, int t) {
      if (vis[x]) {
        add(x);
        col[x] = t;
        add(x);
      } else
        col[x] = t;
    }
    
    int main() {
      scanf("%d%d%d", &n, &m, &q);
      for (int i = 1; i <= m; i++) scanf("%d", &v[i]);
      for (int i = 1; i <= n; i++) scanf("%d", &w[i]);
      for (int i = 1; i < n; i++) {
        int x, y;
        scanf("%d%d", &x, &y);
        addedge(x, y);
        addedge(y, x);
      }
      for (int i = 1; i <= n; i++) {
        scanf("%d", &last[i]);
        col[i] = last[i];
      }
      dfs(1);
      for (int j = 1; j <= 20; j++)
        for (int i = 1; i <= n; i++)
          fa[i][j] = fa[fa[i][j - 1]][j - 1];  // pretprocesiranje predaka
      int block = pow(index, 2.0 / 3);
      for (int i = 1; i <= index; i++) {
        pos[i] = (i - 1) / block;
      }
      while (q--) {
        int opt, x, y;
        scanf("%d%d%d", &opt, &x, &y);
        if (opt == 0) {
          b[++cnt2].l = x;
          b[cnt2].r = last[x];
          last[x] = b[cnt2].t = y;
        } else {
          if (f[x] > f[y]) swap(x, y);
          a[++cnt1] = query{lca(x, y) == x ? f[x] : g[x], f[y], cnt2, cnt1};
        }
      }
      sort(a + 1, a + cnt1 + 1);
      int L, R, T;  // položaji pokazivača
      L = R = 0;
      T = 1;
      for (int i = 1; i <= cnt1; i++) {
        while (T <= a[i].t) {
          modify(b[T].l, b[T].t);
          T++;
        }
        while (T > a[i].t) {
          modify(b[T].l, b[T].r);
          T--;
        }
        while (L > a[i].l) {
          L--;
          add(id[L]);
        }
        while (L < a[i].l) {
          add(id[L]);
          L++;
        }
        while (R > a[i].r) {
          add(id[R]);
          R--;
        }
        while (R < a[i].r) {
          R++;
          add(id[R]);
        }
        int x = id[L], y = id[R];
        int llca = lca(x, y);
        if (x != llca && y != llca) {
          add(llca);
          ans[a[i].id] = cur;
          add(llca);
        } else
          ans[a[i].id] = cur;
      }
      for (int i = 1; i <= cnt1; i++) {
        printf("%lld\n", ans[i]);
      }
      return 0;
    }
    ```

## Pravi Mo algoritam na stablu

Gore opisani Mo algoritam na stablu samo pretvara stablo u lanac; ono što slijedi pravi je Mo algoritam na stablu.

Budući da su zadaci vezani uz Mo algoritam zadaci-predlošci, implementaciju nećemo previše objašnjavati.

### Sortiranje upita

Najprije, znamo da je Mo algoritam zasnovan na podjeli na blokove, pa moramo pronaći način podjele stabla na blokove koji jamči vremensku složenost.

Uvjeti:

-   udaljenost između čvorova koji pripadaju istom bloku ne prelazi zadanu veličinu bloka;
-   u svakom bloku ne smije biti ni previše ni premalo čvorova;
-   svaki čvor mora pripadati nekom bloku;
-   udaljenost između blokova susjednih indeksa ne smije biti prevelika.

Kad smo upoznali te uvjete, pogledajmo ovaj zadatak: [「SCOI2005」王室联邦 (Kraljevska federacija)](https://loj.ac/problem/2152).

Na temelju tog zadatka dovoljno je osigurati još posljednji uvjet i problem podjele na blokove je riješen.

??? note "Ideja"
    Neka je lim željena veličina bloka. Najprije napravimo DFS cijelog stabla; kad veličina podstabla premaši lim, te čvorove stavimo u jedan blok. Lako je uočiti da za korijen može ostati nekoliko čvorova, pa njih stavimo u posljednji blok.

Postupak: stogom održavamo čvorove dok trenutni čvor kao roditelj posjećuje svoju djecu; kad udaljenost od vrha stoga do roditelja premaši željenu veličinu bloka, taj dio elemenata izbacimo i proglasimo jednim blokom; ono što na kraju ostane čini zaseban blok.

Konačni način sortiranja: ako je vremenska oznaka prve dimenzije veća od druge, zamijenimo ih; sortiramo s blokom kojem pripada prva dimenzija kao prvim ključem i vremenskom oznakom druge dimenzije kao drugim ključem.

### Pomicanje pokazivača

#### Postupak

Lako se dosjetiti: možemo označavati čvorove koji ulaze u odgovor, pomicati pokazivač izravno prema cilju i pritom invertirati čvorove na putu.

No tu nastaje problem: ako su na početku oba pokazivača na x, x je očito označen; kad se oba pokazivača pomaknu prema istom djetetu (a ima i mnogo drugih slučajeva), x ne bi trebao biti označen, ali u stvarnosti je označen, jer su ga oba pokazivača označila po jednom i to se poništilo.

Kako to riješiti?

Postoji očito svojstvo: ti su čvorovi sigurno neki LCA-ovi, jer samo kod LCA može doći do dvostrukog poništavanja zbog kojeg poništavanje ne uspije.

Zato LCA nikad ne označavamo tijekom pomicanja, nego ga označimo tek kad treba odgovoriti na upit, a zatim označavanje poništimo.

#### Implementacija

```cpp
// invertiraj sve čvorove na putu osim LCA
void move(int x, int y) {
  if (dp[x] < dp[y]) swap(x, y);
  while (dp[x] > dp[y]) update(x), x = fa[x];
  while (x != y) update(x), update(y), x = fa[x], y = fa[y];
  // x!=y jamči da LCA nije invertiran
}
```

Za računanje LCA možemo upotrijebiti heavy-light dekompoziciju (HLD); tada korak podjele na blokove možemo smjestiti u prvi DFS dekompozicije, a kao vremenske oznake izravno uzeti DFS redoslijed iz drugog DFS-a.

```cpp
int bl[100002], bls = 0;  // blok kojem čvor pripada, broj blokova
unsigned step;            // veličina bloka
int fa[100002], dp[100002], hs[100002] = {0}, sz[100002] = {0};
// roditelj, dubina, teško dijete, veličina
stack<int> sta;

void dfs1(int x) {
  sz[x] = 1;
  unsigned ss = sta.size();
  for (int i = head[x]; i; i = nxt[i])
    if (ver[i] != fa[x]) {
      fa[ver[i]] = x;
      dp[ver[i]] = dp[x] + 1;
      dfs1(ver[i]);
      sz[x] += sz[ver[i]];
      if (sz[ver[i]] > sz[hs[x]]) hs[x] = ver[i];
      if (sta.size() - ss >= step) {
        bls++;
        while (sta.size() != ss) bl[sta.top()] = bls, sta.pop();
      }
    }
  sta.push(x);
}

// main
if (!sta.empty()) {
  bls++;  // ovaj redak može se napisati, a i ne mora
  while (!sta.empty()) bl[sta.top()] = bls, sta.pop();
}
```

### Vremenska složenost

Došli smo do ključnog dijela: ovdje se radi o izboru veličine bloka.

Neka je veličina bloka $unit$:

-   Za pokazivač x: budući da je udaljenost čvorova unutar bloka oko $unit$, u svakom se bloku pokazivač x pomiče $unit^2$ puta ($unit\times dis_{\max}$), ukupno $n\times unit$ puta ($unit^2 \times (\frac{n}{unit})$);
-   Za pokazivač y: u svakom se bloku pomiče najviše $O(n)$ puta, ukupno $\frac{n^2}{unit}$ puta ($n \times (\frac{n}{unit})$).

Zbroj poprima minimum otprilike kod korijena (budući da veličina bloka u Mo algoritmu na stablu nije fiksna, toga se ne treba strogo držati).

### Primjer zadatka 「WC2013」糖果公园

Budući da imamo dodatnu vremensku dimenziju, veličina bloka oko $n^{0.6}$ sasvim je dobra.

??? note "Referentni kôd"
    ```cpp
    #include <algorithm>
    #include <cmath>
    #include <cstdio>
    #include <stack>
    using namespace std;
    
    int gi() {
      int x, c, op = 1;
      while (c = getchar(), c < '0' || c > '9')
        if (c == '-') op = -op;
      x = c ^ 48;
      while (c = getchar(), c >= '0' && c <= '9')
        x = (x << 3) + (x << 1) + (c ^ 48);
      return x * op;
    }
    
    int head[100002], nxt[200004], ver[200004], tot = 0;
    
    void add(int x, int y) {
      ver[++tot] = y, nxt[tot] = head[x], head[x] = tot;
      ver[++tot] = x, nxt[tot] = head[y], head[y] = tot;
    }
    
    int bl[100002], bls = 0;
    unsigned step;
    int fa[100002], dp[100002], hs[100002] = {0}, sz[100002] = {0}, top[100002],
                                id[100002];
    stack<int> sta;
    
    void dfs1(int x) {
      sz[x] = 1;
      unsigned ss = sta.size();
      for (int i = head[x]; i; i = nxt[i])
        if (ver[i] != fa[x]) {
          fa[ver[i]] = x, dp[ver[i]] = dp[x] + 1;
          dfs1(ver[i]);
          sz[x] += sz[ver[i]];
          if (sz[ver[i]] > sz[hs[x]]) hs[x] = ver[i];
          if (sta.size() - ss >= step) {
            bls++;
            while (sta.size() != ss) bl[sta.top()] = bls, sta.pop();
          }
        }
      sta.push(x);
    }
    
    int cnt = 0;
    
    void dfs2(int x, int hf) {
      top[x] = hf, id[x] = ++cnt;
      if (!hs[x]) return;
      dfs2(hs[x], hf);
      for (int i = head[x]; i; i = nxt[i])
        if (ver[i] != fa[x] && ver[i] != hs[x]) dfs2(ver[i], ver[i]);
    }
    
    int lca(int x, int y) {
      while (top[x] != top[y]) {
        if (dp[top[x]] < dp[top[y]]) swap(x, y);
        x = fa[top[x]];
      }
      return dp[x] < dp[y] ? x : y;
    }
    
    struct qu {
      int x, y, t, id;
    
      bool operator<(const qu a) const {
        return bl[x] == bl[a.x] ? (bl[y] == bl[a.y] ? t < a.t : bl[y] < bl[a.y])
                                : bl[x] < bl[a.x];
      }
    } q[100001];
    
    int qs = 0;
    
    struct ch {
      int x, y, b;
    } upd[100001];
    
    int ups = 0;
    long long ans[100001];
    int b[100001] = {0};
    int a[100001];
    long long w[100001];
    long long v[100001];
    long long now = 0;
    bool vis[100001] = {false};
    
    void back(int t) {
      if (vis[upd[t].x]) {
        now -= w[b[upd[t].y]--] * v[upd[t].y];
        now += w[++b[upd[t].b]] * v[upd[t].b];
      }
      a[upd[t].x] = upd[t].b;
    }
    
    void change(int t) {
      if (vis[upd[t].x]) {
        now -= w[b[upd[t].b]--] * v[upd[t].b];
        now += w[++b[upd[t].y]] * v[upd[t].y];
      }
      a[upd[t].x] = upd[t].y;
    }
    
    void update(int x) {
      if (vis[x])
        now -= w[b[a[x]]--] * v[a[x]];
      else
        now += w[++b[a[x]]] * v[a[x]];
      vis[x] ^= 1;
    }
    
    void move(int x, int y) {
      if (dp[x] < dp[y]) swap(x, y);
      while (dp[x] > dp[y]) update(x), x = fa[x];
      while (x != y) update(x), update(y), x = fa[x], y = fa[y];
    }
    
    int main() {
      int n = gi(), m = gi(), k = gi();
      step = (int)pow(n, 0.6);
      for (int i = 1; i <= m; i++) v[i] = gi();
      for (int i = 1; i <= n; i++) w[i] = gi();
      for (int i = 1; i < n; i++) add(gi(), gi());
      for (int i = 1; i <= n; i++) a[i] = gi();
      for (int i = 1; i <= k; i++)
        if (gi())
          q[++qs].x = gi(), q[qs].y = gi(), q[qs].t = ups, q[qs].id = qs;
        else
          upd[++ups].x = gi(), upd[ups].y = gi();
      for (int i = 1; i <= ups; i++) upd[i].b = a[upd[i].x], a[upd[i].x] = upd[i].y;
      for (int i = ups; i; i--) back(i);
      fa[1] = 1;
      dfs1(1), dfs2(1, 1);
      if (!sta.empty()) {
        bls++;
        while (!sta.empty()) bl[sta.top()] = bls, sta.pop();
      }
      for (int i = 1; i <= n; i++)
        if (id[q[i].x] > id[q[i].y]) swap(q[i].x, q[i].y);
      sort(q + 1, q + qs + 1);
      int x = 1, y = 1, t = 0;
      for (int i = 1; i <= qs; i++) {
        if (x != q[i].x) move(x, q[i].x), x = q[i].x;
        if (y != q[i].y) move(y, q[i].y), y = q[i].y;
        int f = lca(x, y);
        update(f);
        while (t < q[i].t) change(++t);
        while (t > q[i].t) back(t--);
        ans[q[i].id] = now;
        update(f);
      }
      for (int i = 1; i <= qs; i++) printf("%lld\n", ans[i]);
      return 0;
    }
    ```
