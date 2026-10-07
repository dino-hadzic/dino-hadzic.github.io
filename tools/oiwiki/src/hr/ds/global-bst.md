---
title: Globalno balansirano binarno stablo
---

## Uvod

Predznanje: [heavy-light dekompozicija](../graph/hld.md)

Vremenska složenost heavy-light dekompozicije je $O(n\log^2 n)$, a dobro poznati LCT, iako ima složenost $O(n\log n)$, ima veliku konstantu i može biti čak sporiji od heavy-light dekompozicije. Postoji li onda metoda koja je i $O(n\log n)$ i ima razmjerno malu konstantu? Tu nastupa globalno balansirano binarno stablo.

Globalno balansirano binarno stablo zapravo je šuma binarnih stabala u kojoj svako binarno stablo održava jedan teški lanac. Binarna stabla u toj šumi međusobno su ipak povezana: korijen svakog binarnog stabla povezan je s roditeljem vrha pripadnog teškog lanca, baš kao u LCT-u. No globalno balansirano binarno stablo statično je stablo: za razliku od LCT-a, nakon izgradnje oblik stabla se ne mijenja.

Globalno balansirano binarno stablo struktura je podataka za promjene/upite na lancima u stablu i omogućuje:

-   promjenu cijelog lanca u $O(\log n)$;
-   upit nad cijelim lancem u $O(\log n)$;
-   pronalaženje najnižeg zajedničkog pretka (LCA), promjenu podstabla, upit nad podstablom itd. u $O(\log n)$; te su složenosti jednake kao kod heavy-light dekompozicije.

## Glavna svojstva

1.  Globalno balansirano binarno stablo sastoji se od mnogo binarnih stabala povezanih lakim bridovima; svako binarno stablo održava jedan teški lanac izvornog stabla, a njegov inorder obilazak odgovara redoslijedu rastuće dubine na tom teškom lancu. Svaki se čvor pojavljuje u točno jednom binarnom stablu.
2.  Bridovi se dijele na teške i lake. Teški bridovi su bridovi unutar binarnih stabala i održavaju se kao u običnom binarnom stablu: pamtimo lijevo i desno dijete te roditelja. Laki brid vodi od korijena binarnog stabla do roditelja vrha pripadnog teškog lanca. Laki bridovi održavaju se po načelu „dijete poznaje roditelja, roditelj ne poznaje dijete”, tj. iz djeteta se može doći do roditelja, ali ne i obrnuto. Napomena: bridovi globalno balansiranog binarnog stabla ne odgovaraju bridovima izvornog stabla.
3.  Računajući i teške i lake bridove, visina globalno balansiranog binarnog stabla je $O(\log n)$. Upravo to svojstvo jamči vremensku složenost.

Slijedi primjer izgradnje globalno balansiranog binarnog stabla. Prva slika prikazuje izvorno stablo s korijenom u čvoru 1. Pune linije su teški bridovi.

![global-bst-1](images/global-bst-1.svg)

Druga slika prikazuje izgrađeno globalno balansirano binarno stablo; isprekidane linije su laki bridovi, pune linije teški bridovi, a svako je binarno stablo označeno crvenom kružnicom.

![global-bst-2](images/global-bst-2.svg)

## Izgradnja stabla

Najprije, kao kod obične heavy-light dekompozicije, jednim DFS-om odredimo teško dijete svakog čvora. Zatim krenemo od korijena, pronađemo teški lanac koji sadrži korijen, za laku djecu čvorova tog lanca rekurzivno gradimo stabla i povezujemo ih lakim bridovima. Potom za čvorove teškog lanca trebamo izgraditi binarno stablo. Čvorove teškog lanca spremimo u niz i za svaki izračunamo zbroj veličina podstabala njegove lake djece plus jedan (tj. veličinu kojom sam čvor pridonosi). Prema tome odredimo težinsku sredinu lanca, uzmemo je za korijen binarnog stabla, rekurzivno izgradimo obje strane i povežemo ih teškim bridovima.

Kod je sljedeći:

???+ note "Implementacija"
    ```cpp
    std::vector<int> G[N];
    int n, fa[N], son[N], sz[N];
    
    void dfsS(int u) {
      sz[u] = 1;
      for (int v : G[u]) {
        dfsS(v);
        sz[u] += sz[v];
        if (sz[v] > sz[son[u]]) son[u] = v;
      }
    }
    
    int b[N], bs[N], l[N], r[N], f[N], ss[N];
    
    // gradi binarno stablo nad točkama b[bl,br) i vraća njegov korijen
    int cbuild(int bl, int br) {
      int x = bl, y = br;
      while (y - x > 1) {
        int mid = (x + y) >> 1;
        if (2 * (bs[mid] - bs[bl]) <= bs[br] - bs[bl])
          x = mid;
        else
          y = mid;
      }
      // binarnim pretraživanjem nađi težinsku sredinu prema bs
      y = b[x];
      ss[y] = br - bl;  // ss: veličina teškog podstabla u binarnom stablu
      if (bl < x) {
        l[y] = cbuild(bl, x);
        f[l[y]] = y;
      }
      if (x + 1 < br) {
        r[y] = cbuild(x + 1, br);
        f[r[y]] = y;
      }
      return y;
    }
    
    int build(int x) {
      int y = x;
      do
        for (int v : G[y])
          if (v != son[y])
            f[build(v)] =
                y;  // rekurzivno gradi stablo i spaja lake bridove; brid ide iz korijena binarnog stabla, ne iz djeteta
      while (y = son[y]);
      y = 0;
      do {
        b[y++] = x;                              // sprema točke teškog lanca
        bs[y] = bs[y - 1] + sz[x] - sz[son[x]];  // bs: zbroj veličina lake djece + 1, prefiksne sume
      } while (x = son[x]);
      return cbuild(0, y);
    }
    ```

Iz koda se vidi da je vremenska složenost izgradnje $O(n\log n)$. Dokažimo sada da je visina stabla $O(\log n)$: promotrimo skakanje po roditeljima od proizvoljnog čvora do korijena. Skok preko lakog brida odgovara prelasku na drugi teški lanac u izvornom stablu, pa po svojstvima heavy-light dekompozicije lakih bridova ima najviše $O(\log n)$. Budući da pri izgradnji binarnog stabla za korijen uzimamo težinsku sredinu koja uračunava laku djecu, svaki skok preko teškog brida barem udvostručuje veličinu (zajedno s lakom djecom), pa i teških bridova ima najviše $O(\log n)$. Ukupna je visina stabla stoga $O(\log n)$.

## Upiti

Toliko o samom globalno balansiranom binarnom stablu. Preostale operacije, promjene i upiti na lancima, razmjerno su jednostavne: krenemo od čvora nad kojim radimo i skačemo sve do korijena. Obraditi sve čvorove teškog lanca nekog čvora koji imaju manju dubinu od njega u biti znači obraditi sve čvorove lijevo od ciljnog čvora u binarnom stablu tog lanca. Te se operacije rastavljaju na niz operacija nad podstablima, slično održavanju običnog binarnog stabla, što uključuje održavanje zbroja podstabla i postavljanje oznaka na podstabla. Pritom se koristi permanentno označavanje (bez spuštanja oznaka). Moguće je i spuštati oznake pushdownom i održavati zbroj pushupom, ali to je složenije: binarno stablo obično obrađujemo odozgo prema dolje, a ovdje bismo najprije morali odrediti put skakanja pa tek onda odozgo prema dolje spuštati oznake, što može povećati konstantu.

Kod je sljedeći:

???+ note "Implementacija"
    ```cpp
    // a: oznaka dodavanja na podstablo
    // s: zbroj podstabla (bez oznake dodavanja)
    int a[N], s[N];
    
    void add(int x) {
      bool t = true;
      int z = 0;
      while (x) {
        s[x] += z;
        if (t) {
          a[x]++;
          if (r[x]) a[r[x]]--;
          z += 1 + ss[l[x]];
          s[x] -= ss[r[x]];
        }
        t = (x != l[f[x]]);
        if (t && x != r[f[x]]) z = 0;  // pri prelasku lakog brida treba poništiti
        x = f[x];
      }
    }
    
    int query(int x) {
      int ret = 0;
      bool t = true;
      int z = 0;
      while (x) {
        if (t) {
          ret += s[x] - s[r[x]];
          ret -= 1ll * ss[r[x]] * a[r[x]];
          z += 1 + ss[l[x]];
        }
        ret += 1ll * z * a[x];
        t = (x != l[f[x]]);
        if (t && x != r[f[x]]) z = 0;  // pri prelasku lakog brida treba poništiti
        x = f[x];
      }
      return ret;
    }
    ```

Za operacije nad podstablima treba uzeti u obzir i laku djecu, pa se dodatno održavaju zbroj i oznaka podstabla koji uključuju laku djecu; za vježbu riješite „[Luogu P3384 【模板】轻重链剖分](https://www.luogu.com.cn/problem/P3384)”.

## Primjer

??? note "[Luogu P4751 【模板】动态 DP & 动态树分治（加强版）](https://www.luogu.com.cn/problem/P4751)"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <cstring>
    constexpr int MAXN = 1000000;
    constexpr int MAXM = 3000000;
    constexpr int INF = 0x3FFFFFFF;
    using namespace std;
    
    struct edge {
      int to;
      edge *nxt;
    } edges[MAXN * 2 + 5];
    
    edge *ncnt = &edges[0], *Adj[MAXN + 5];
    int n, m;
    
    struct Matrix {
      int M[2][2];
    
      Matrix operator*(const Matrix &B) const {
        static Matrix ret;
        for (int i = 0; i < 2; i++)
          for (int j = 0; j < 2; j++) {
            ret.M[i][j] = -INF;
            for (int k = 0; k < 2; k++)
              ret.M[i][j] = max(ret.M[i][j], M[i][k] + B.M[k][j]);
          }
        return ret;
      }
    } matr1[MAXN + 5], matr2[MAXN + 5];  // svaki čvor održava dvije matrice
    
    int root;
    int w[MAXN + 5], dep[MAXN + 5], son[MAXN + 5], siz[MAXN + 5], lsiz[MAXN + 5];
    int g[MAXN + 5][2], f[MAXN + 5][2], trfa[MAXN + 5], bstch[MAXN + 5][2];
    int stk[MAXN + 5], tp;
    bool vis[MAXN + 5];
    
    void AddEdge(int u, int v) {
      edge *p = ++ncnt;
      p->to = v;
      p->nxt = Adj[u];
      Adj[u] = p;
    
      edge *q = ++ncnt;
      q->to = u;
      q->nxt = Adj[v];
      Adj[v] = q;
    }
    
    void DFS(int u, int fa) {
      siz[u] = 1;
      for (edge *p = Adj[u]; p != NULL; p = p->nxt) {
        int v = p->to;
        if (v == fa) continue;
        dep[v] = dep[u] + 1;
        DFS(v, u);
        siz[u] += siz[v];
        if (!son[u] || siz[son[u]] < siz[v]) son[u] = v;
      }
      lsiz[u] = siz[u] - siz[son[u]];  // zbroj siz lake djece + 1
    }
    
    void DFS2(int u, int fa) {
      f[u][1] = w[u], f[u][0] = 0;
      g[u][1] = w[u], g[u][0] = 0;
      if (son[u]) {
        DFS2(son[u], u);
        f[u][0] += max(f[son[u]][0], f[son[u]][1]);
        f[u][1] += f[son[u]][0];
      }
      for (edge *p = Adj[u]; p != NULL; p = p->nxt) {
        int v = p->to;
        if (v == fa || v == son[u]) continue;
        DFS2(v, u);
        f[u][0] += max(f[v][0], f[v][1]);  // f[][] je običan DP niz
        f[u][1] += f[v][0];
        g[u][0] += max(f[v][0], f[v][1]);  // niz g[][] uključuje samo čvor i njegovu laku djecu
        g[u][1] += f[v][0];
      }
    }
    
    void PushUp(int u) {
      matr2[u] = matr1[u];  // matr1 je čvor + informacije lake djece, matr2 je informacija intervala
      if (bstch[u][0]) matr2[u] = matr2[bstch[u][0]] * matr2[u];
      // pazi na smjer prijelaza; uz drukčiju definiciju množenja matrica smjer može biti drukčiji
      if (bstch[u][1]) matr2[u] = matr2[u] * matr2[bstch[u][1]];
    }
    
    int getmx2(int u) { return max(matr2[u].M[0][0], matr2[u].M[0][1]); }
    
    int getmx1(int u) { return max(getmx2(u), matr2[u].M[1][0]); }
    
    int SBuild(int l, int r) {
      if (l > r) return 0;
      int tot = 0;
      for (int i = l; i <= r; i++) tot += lsiz[stk[i]];
      for (int i = l, sumn = lsiz[stk[l]]; i <= r; i++, sumn += lsiz[stk[i]])
        if (sumn * 2 >= tot)  // ovo je težište
        {
          int lch = SBuild(l, i - 1), rch = SBuild(i + 1, r);
          bstch[stk[i]][0] = lch;
          bstch[stk[i]][1] = rch;
          trfa[lch] = trfa[rch] = stk[i];
          PushUp(stk[i]);  // skupi informacije intervala
          return stk[i];
        }
      return 0;
    }
    
    int Build(int u) {
      for (int pos = u; pos; pos = son[pos]) vis[pos] = true;
      for (int pos = u; pos; pos = son[pos])
        for (edge *p = Adj[pos]; p != NULL; p = p->nxt)
          if (!vis[p->to])  // lako dijete
          {
            int v = p->to, ret = Build(v);
            trfa[ret] = pos;  // spoji treefa[] lakog djeteta
          }
      tp = 0;
      for (int pos = u; pos; pos = son[pos]) stk[++tp] = pos;  // izdvoji teški lanac
      int ret = SBuild(1, tp);  // zasebni SBuild za teški lanac (valjda Special Build?)
      return ret;               // vrati korijen binarnog stabla trenutnog teškog lanca
    }
    
    void Modify(int u, int val) {
      matr1[u].M[1][0] += val - w[u];
      w[u] = val;
      for (int pos = u; pos; pos = trfa[pos])
        if (trfa[pos] && bstch[trfa[pos]][0] != pos && bstch[trfa[pos]][1] != pos) {
          matr1[trfa[pos]].M[0][0] -= getmx1(pos);
          matr1[trfa[pos]].M[0][1] = matr1[trfa[pos]].M[0][0];
          matr1[trfa[pos]].M[1][0] -= getmx2(pos);
          PushUp(pos);
          matr1[trfa[pos]].M[0][0] += getmx1(pos);
          matr1[trfa[pos]].M[0][1] = matr1[trfa[pos]].M[0][0];
          matr1[trfa[pos]].M[1][0] += getmx2(pos);
        } else
          PushUp(pos);
    }
    
    int read() {
      int ret = 0, f = 1;
      char c = 0;
      while (c < '0' || c > '9') {
        c = getchar();
        if (c == '-') f = -f;
      }
      ret = 10 * ret + c - '0';
      while (true) {
        c = getchar();
        if (c < '0' || c > '9') break;
        ret = 10 * ret + c - '0';
      }
      return ret * f;
    }
    
    void print(int x) {
      if (x == 0) return;
      print(x / 10);
      putchar(x % 10 + '0');
    }
    
    int main() {
      scanf("%d %d", &n, &m);
      for (int i = 1; i <= n; i++) w[i] = read();
      int u, v;
      for (int i = 1; i < n; i++) {
        u = read(), v = read();
        AddEdge(u, v);
      }
      DFS(1, -1);
      // odredi teško dijete
      DFS2(1, -1);
      // početne DP vrijednosti; moglo bi i u Build(), ali ovako je ujednačeno s HLD-om
      for (int i = 1; i <= n; i++) {
        matr1[i].M[0][0] = matr1[i].M[0][1] = g[i][0];
        matr1[i].M[1][0] = g[i][1], matr1[i].M[1][1] = -INF;  // inicijalizacija matrica
      }
      root = Build(1);  // root je težište teškog lanca koji sadrži korijen
      int lastans = 0;
      for (int i = 1; i <= m; i++) {
        u = read(), v = read();
        u ^= lastans;  // forsirano online
        Modify(u, v);
        lastans = getmx1(root);  // izravno očitaj vrijednost
        if (lastans == 0)
          putchar('0');
        else
          print(lastans);
        putchar('\n');
      }
      return 0;
    }
    ```

## Literatura

[P4211 \[LNOI2014\] LCA | 全局平衡二叉树](https://www.luogu.com.cn/blog/nederland/globalbst)
