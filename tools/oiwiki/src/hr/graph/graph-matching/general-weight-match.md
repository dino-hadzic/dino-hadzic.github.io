---
title: Najveće težinsko sparivanje u općem grafu
---

Ova stranica ide od najvećeg težinskog perfektnog sparivanja u općem grafu do najvećeg težinskog sparivanja u općem grafu (najveće težinsko sparivanje može se dodavanjem bridova težine nula pretvoriti u najveće težinsko perfektno sparivanje).

## Predznanje

### Cvijet (blossom)

Razlika između sparivanja u općem grafu i sparivanja u bipartitnom grafu jest u tome što graf može sadržavati neparne cikluse. Parne cikluse možemo promatrati kao bipartitni graf.

Algoritam cvjetova (Blossom Algorithm) postupa tako da svaki neparni ciklus na koji naiđe sažme u **cvijet (Blossom)** i sve vrhove cvijeta proglasi parnim vrhovima. Budući da svi vrhovi cvijeta mogu postati parni, cijeli cvijet možemo izravno sažeti u jedan parni vrh. Pazite: cvijet može sadržavati druge cvjetove.

I ovo se može pretvoriti u linearno programiranje i dualni problem, ali cvjetove treba posebno obraditi.

### Oznake vrhova (vertex labeling) i bridovi jednakosti (Equality Edge)

Definirajmo $z_u$ kao oznaku vrha $u$ (vertex labeling), s istim značenjem kao oznake vrhova u $KM$ algoritmu. Brid $e(u,v)$ zovemo „bridom jednakosti” ako i samo ako je zbroj oznaka vrhova $u$ i $v$ jednak težini brida $e$ ($z_u + z_v = w(e)$); tada je oznaka brida $z_e = z_u + z_v − w(e) = 0$.

## Linearni program najvećeg težinskog perfektnog sparivanja u općem grafu

### Definicije

Cvijet ima najmanje tri vrha, a nakon sažimanja postaje jedan vrh. Neka je $O$ skup svih skupova neparne veličine $≥3$ (sadrži sve cvjetove), a $\gamma(S)$ označava bridove unutar skupa $S$.

$$
\begin{aligned}
& \text{neka je } S\subseteq V \\
& \gamma(S)=\{(u,v)\in E:u\in S,v\in S\} \\
& O=\{B\subseteq V:|B|\text{ je neparan i }|B|\geq3\} \\
\end{aligned}
$$

### Dualni problem

???+ note "Primarni problem"
    $$
    \begin{aligned}
    & \max\sum_{e\in E}w(e)x_e \\
    & \text{uz ograničenja:} \\
    & x(\delta(u))=1:\forall u\in V \\
    & x(\gamma(B))\leq\lfloor\frac{|B|}{2}\rfloor:\forall B\in O \\
    & x_e\geq0:\forall e\in E \\
    \end{aligned}
    $$

Zatim primarno-dualnom metodom (Primal-Dual) problem pretvorimo u dualni.

???+ note "Dualni problem"
    $$
    \begin{aligned}
    & \min\sum_{u\in V}z_u+\sum_{B\in O}\left\lfloor\frac{|B|}{2}\right\rfloor z_B \\
    & \text{uz ograničenja:} \\
    & z_B\geq0:\forall B\in O \\
    & z_e\geq0:\forall e\in E \\
    & \text{neka je } e=(u,v),\text{ gdje je} \\
    & \begin{array}{lll}
    z_e & = & z_u + z_v - w(e) + \sum_{\substack{B \in O \\ u,v \in \gamma(B)}} z_B
    \end{array}
    \end{aligned}
    $$

Bridovi s $x_e=1$ su spareni, a bridovi s $x_e=0$ nespareni. Kao i u bipartitnom grafu, mora vrijediti $x_e\in\{0,1\}:\forall e\in E$. Stoga u najvećem težinskom perfektnom sparivanju svi spareni bridovi moraju biti **bridovi jednakosti**.

Za razliku od bipartitnog grafa, u općem grafu treba obraditi još i $z_B$. Razmotrimo kad je $z_B$ veće od $0$.

Vidi se da je najbolje nastojati držati $z_B=0$, ali kad nema drugog izbora, ipak treba dopustiti $z_B>0$. Dovoljno je dopustiti $z_B>0$ kad je $x(\gamma(B)) = \left\lfloor \dfrac{|B|}2 \right\rfloor \text{ i } x(\delta(B)) = 1$, jer izvan te situacije $z_B>0$ nema smisla.

Prema uvjetima komplementarne labavosti vrijede sljedeći odnosi:

-   Za odabrani brid $e$ nužno je $z_e=0$.

    $$
    x_e>0 \longrightarrow z_e=0,\quad \forall e\in E
    $$

-   Za odabrani skup *B*, $z_B>0 \longrightarrow x(\gamma(B))= \left\lfloor \dfrac{|B|}2 \right\rfloor$, tj. u svakom skupu $B$ sa $z_B>0$ odabrano je onoliko bridova koliko iznosi polovina veličine skupa, odnosno skup $B$ je cvijet, i uvećavamo odabirom jednog brida cvijeta. Istodobno dodajemo uvjet $x(\delta(B))=1$, tj. $z_B>0$ ima smisla samo kad iz cvijeta $B$ prema van vodi točno jedan brid.

    $$
    z_B>0 \longrightarrow x(\gamma(B))=\left\lfloor\frac{|B|}2\right\rfloor, x(\delta(B))=1\quad \forall B\in O
    $$

Pojam „**brida jednakosti**” spojimo s ranijim algoritmom cvjetova: neprekidno uvećavamo uvećavajućim putovima sastavljenima od „bridova jednakosti”; budući da su svi bridovi kojima uvećavamo „bridovi jednakosti”, i konačno najveće težinsko perfektno sparivanje sastoji se samo od „bridova jednakosti”.

### Obrada cvjetova

Kad naiđemo na cvijet, sažmemo ga u jedan parni vrh. Sve vrhove cvijeta proglasimo parnima i postavimo njegov $z_B=0$.

Budući da nakon sažimanja cvijet pamtimo i razvijamo ga tek kad su ispunjeni određeni uvjeti, cvjetove ne možemo bilježiti na raniji način.

Ako nije drugačije rečeno, prije spomenuti vrhovi uključuju i parne vrhove nastale sažimanjem cvjetova.

Budući da i cvjetovi mogu biti sažeti u vrh i dodani u red, a broj cvjetova nije fiksan, ne možemo kao prije prolaziti svaki vrh i provjeravati postoji li uvećavajući put. Zato pri pretraživanju u širinu (BFS) sve nesparene vrhove moramo odjednom staviti u red.

Tako istodobno nastaje više alternirajućih stabala.

### Četiri koraka algoritma

Algoritam se može podijeliti u četiri koraka.

1.  GROW (brid jednakosti): „bridovima jednakosti” gradimo alternirajuće stablo.
2.  AUGMENT (uvećanje): nađemo uvećavajući put i uvećamo sparivanje.
3.  SHRINK (sažimanje cvijeta): sažmemo cvijet u jedan vrh.
4.  EXPAND (razvijanje): razvijemo cvijet.

![general-weight-match-1](images/general-weight-match-1.png)

U fazi AUGMENT, budući da su svi nespareni vrhovi u različitim alternirajućim stablima, kad se pri uvećavanju spoje parni vrhovi dvaju alternirajućih stabala, to znači da smo našli uvećavajući put.

### Nema brida jednakosti za proširenje

Kao i u bipartitnom grafu, može se dogoditi da ne nađemo „brid jednakosti” za proširenje. Tada treba podesiti vertex labeling.

### Podešavanje VERTEX LABELINGA

Vertex labeling i dalje mora zadovoljavati svojstvo „veće ili jednako”, postojeći „bridovi jednakosti” ne smiju se promijeniti, a $z_B$ treba držati što manjim.

???+ note "Oznake za neparne i parne vrhove"
    $u^−$ označava da je $u$ neparni vrh u alternirajućem stablu.  
    $u^+$ označava da je $u$ parni vrh u alternirajućem stablu.  
    $u^\varnothing$ označava da $u$ nije ni u jednom alternirajućem stablu.  
    Svako $B$ u nastavku podrazumijeva se kao cvijet i ujedno označava vrh nastao sažimanjem cvijeta.  
    I cvjetovi mogu biti neparni ili parni, pa se i na njih primjenjuju oznake $B^+$, $B^−$, $B^\varnothing$ itd.

Neka trenutno imamo r alternirajućih stabala $T_i=(U_{t_i},V_{t_i}):1\leq i\leq r$; definirajmo

$$
\begin{aligned}
d1 &= \min(\{z_e : e = (u^+,v^\varnothing)\}) \\
d2 &= \min(\{z_e : e = (u^+,v^+), ~ u^+ \in T_i, ~ v^+ \in T_j, ~ i \neq j\}) / 2 \\
d3 &= \min(\{z_{B^-} : B^- \in O\}) / 2
\end{aligned}
$$

Uočite da je ovdje *B* vrh nastao sažimanjem cvijeta, pa ima parnost.

Neka je $d=min(d1,d2,d3)$ i postavimo

$$
\begin{aligned}
z_{u^+} - &= d \\
z_{v^-} + &= d \\
z_{B^+} + &= 2d \\
z_{B^-} - &= 2d \\
\end{aligned}
$$

Ako se dogodi $z_B=0(d=d3)$, da bismo spriječili $z_B<0$, taj cvijet treba razviti (EXPAND).
Nakon razvijanja ostaje samo alternirajući put unutar cvijeta, a vrhovi cvijeta koji nisu na alternirajućem putu postavljaju se na neposjećene ($\varnothing$).

Tako smo stvorili (barem) jedan novi brid jednakosti, postojeći bridovi jednakosti ostali su netaknuti, zadržano je svojstvo $z_e\geq0:\forall e\in E$ i $z_B$ je povećan u najmanjoj mogućoj mjeri, pa možemo nastaviti tražiti uvećavajući put.

## Najveće težinsko sparivanje u općem grafu

Dosad smo tražili najveće težinsko perfektno sparivanje; za najveće težinsko sparivanje vertex labelingu treba dodati još jedno ograničenje: za svaki spareni vrh $u$ vrijedi $z_u>0$.

Na početku postavimo sve $z_u=max(\{w(e):e\in E\})/2$.

Vrhovi čiji je vertex labeling $0$ na kraju postaju nespareni.

### Referentni kôd

Radi jednostavnije implementacije, $z_e$ računamo s težinama bridova pomnoženima s $2$, pa nema pogrešaka s decimalnim brojevima.

???+ note "Pohrana"
    ```cpp
    constexpr int INF = INT_MAX;
    constexpr int MAXN = 400;
    
    struct edge {
      int u, v, w;
    
      // (u,v) je brid težine w
      edge() {}
    
      edge(int u, int v, int w) : u(u), v(v), w(w) {}
    };
    
    int n, n_x;
    // ima n vrhova, numeriranih 1 ~ n
    // n_x je trenutni broj vrhova plus cvjetova; brojevi od n+1 do n_x su vrhovi cvjetova
    edge g[MAXN * 2 + 1][MAXN * 2 + 1];
    // graf je pohranjen matricom susjedstva; cvjetova je najviše n-1, pa je veličina MAXN*
    vector<int> flower[MAXN * 2 + 1];
    // flower[b] pamti koji su vrhovi u cvijetu b
    // vrhove cvijeta pamtimo tako da zapisujemo samo najvanjskije cvjetove unutar njega
    ```

Slijedi primjer ugniježđenih cvjetova.

![general-weight-match-2](images/general-weight-match-2.png)

Ovdje je $\{ 6, 5, 8\} \in b1,\{ b1, 4, 3, 2, 11, 10, 9\} \in b2$. Pohranjeno kao:

```text
flower[b2] = {b1, 4, 3, 2, 11, 10, 9} 
flower[b1] = {6, 5, 8}
```

![general-weight-match-3](images/general-weight-match-3.png)

```text
flower[b2] = {9, b1, 4, 3, 2, 11, 10} 
flower[b1] = {5, 8, 6}
```

```cpp
int lab[MAXN * 2 + 1];
// lab[u] pamti z_u, lab[b] pamti z_B
int match[MAXN * 2 + 1], slack[MAXN * 2 + 1], st[MAXN * 2 + 1],
    pa[MAXN * 2 + 1];
// match[x]=y znači da je (x,y) spareni brid; x i y mogu biti cvjetovi
// slack[x]=u znači da je z(x,u) najmanji među svim bridovima susjednima x
// st[x]=b znači da je cvijet u kojem je vrh x jednak b. Ako je x=b i b<=n, x je
// običan vrh (nije ni u jednom cvijetu); pa[v]=u znači da je u alternirajućem stablu roditelj vrha v jednak u
int flower_from[MAXN * 2 + 1][MAXN + 1], S[MAXN * 2 + 1], vis[MAXN * 2 + 1];
/*
flower_from[b][x]=xs znači da je najveći podcvijet cvijeta b koji sadrži x jednak xs
x je vrh unutar b, xs je cvijet ili vrh unutar b, pri čemu je x=xs ili je x jedan od vrhova u xs
*/
// S[u]={-1: neposjećen, 0: parni vrh, 1: neparni vrh}
// vis se koristi samo pri traženju lca za provjeru je li vrh već posjećen
queue<int> q;
// queue za BFS traženje uvećavajućeg puta
```

![general-weight-match-4](images/general-weight-match-4.png)

```text
flower_from[b2][6] = b1 
flower_from[b2][5] = b1 
flower_from[b2][9] = 9 
flower_from[b1][6] = 6 
i tako dalje
```

```cpp
int e_delta(const edge &e) {
  // računa ze; radi jednostavnosti sve su težine bridova prethodno pomnožene s dva
  // izravno računanje e_delta unutar cvijeta dalo bi pogrešan rezultat
  return lab[e.u] + lab[e.v] - g[e.u][e.v].w * 2;
}

void update_slack(int u, int x) {
  // ažurira slack[x] pomoću u
  if (!slack[x] || e_delta(g[u][x]) < e_delta(g[slack[x]][x])) {
    slack[x] = u;
  }
}

void set_slack(int x) {
  // računa slack[x]; slack[x]=0 znači da je x vrh alternirajućeg stabla
  slack[x] = 0;
  for (int u = 1; u <= n; ++u) {
    if (g[u][x].w > 0 && st[u] != x && S[st[u]] == 0) {
      update_slack(u, x);
    }
  }
}
```

```cpp
void q_push(int x) {
  // stavlja x u queue; dogovor je da se cvijet ne smije izravno staviti u queue
  if (x <= n)
    q.push(x);
  else {
    // ako treba staviti cvijet, u queue moramo dodati sve vrhove izvornog grafa unutar cvijeta
    for (size_t i = 0; i < flower[x].size(); i++) {
      q_push(flower[x][i]);
    }
  }
}

void set_st(int x, int b) {
  // postavlja cvijet u kojem je x na b
  st[x] = b;
  if (x > n) {
    // ako je i x cvijet, moramo i za vrhove unutar x postaviti cvijet na b
    for (size_t i = 0; i < flower[x].size(); ++i) {
      set_st(flower[x][i], b);
    }
  }
}
```

```cpp
int get_pr(int b, int xr) {
  // xr je vrh u flower[b]; povratna vrijednost pr je njegov položaj
  // da bi program radio ispravno, flower[b][0]~flower[b][pr] mora biti alternirajući put u cvijetu
  int pr = find(flower[b].begin(), flower[b].end(), xr) - flower[b].begin();
  if (pr % 2 == 1) {
    // provjeri položaj u cvijetu; ako flower[b][0]~flower[b][pr] nije alternirajući put
    // okreni cijeli cvijet i ponovno izračunaj pr
    // tako da flower[b][0]~flower[b][pr] bude alternirajući put u cvijetu
    reverse(flower[b].begin() + 1, flower[b].end());
    return (int)flower[b].size() - pr;
  } else
    return pr;
}
```

![general-weight-match-5](images/general-weight-match-5.png)

Ako pozovemo `get_pr(b2,11)`, `flower[b2]` postaje `{9,10,11,2,3,4,b1}` i vraća se 2.

Ako pozovemo `get_pr(b2,2)`, `flower[b2]` postaje `{9,b1,4,3,2,11,10}` i vraća se 4.

```cpp
void set_match(int u, int v) {
  // postavlja u i v kao spareni brid; u i v mogu biti cvjetovi
  match[u] = g[u][v].v;
  if (u > n) {
    // ako je u cvijet
    edge e = g[u][v];
    int xr = flower_from[u][e.u];  // nađi u kojem je cvijetu unutar flower[u] vrh e.u
    int pr = get_pr(u, xr);  // nađi položaj xr i učini 0~pr alternirajućim putem u cvijetu
    for (int i = 0; i < pr; ++i) {  // zamijeni sparene i nesparene bridove na alternirajućem putu u cvijetu
      set_match(flower[u][i], flower[u][i ^ 1]);
    }
    set_match(xr, v);  // postavi (xr,v) kao spareni brid
    rotate(flower[u].begin(), flower[u].begin() + pr, flower[u].end());
    // na kraju pr postaje baza cvijeta, jer po načinu pohrane flower[u][0] mora biti baza cvijeta u
    // pa flower[u][pr] rotiramo na početak
  }
}

void augment(int u, int v) {
  // uveća u i sve pretke vrha u te postavi (u,v) kao spareni brid
  for (;;) {
    int xnv = st[match[u]];
    set_match(u, v);
    if (!xnv) return;
    set_match(xnv, st[pa[xnv]]);
    u = st[pa[xnv]];
    v = xnv;
  }
}

int get_lca(int u, int v) {
  // nađi lca vrhova u,v u alternirajućem stablu
  static int t = 0;
  for (++t; u || v; swap(u, v)) {
    if (u == 0) continue;
    if (vis[u] == t) return u;
    vis[u] = t;  // ovako ne moramo brisati polje vis
    u = st[match[u]];
    if (u) u = st[pa[u]];
  }
  return 0;
}
```

???+ note "Dodavanje neparnog cvijeta"
    ```cpp
    void add_blossom(int u, int lca, int v) {
      // sažmi cvijet u,v,lca u jedan vrh b
      // lca vrhova u,v u alternirajućem stablu je baza cvijeta
      int b = n + 1;
      while (b <= n_x && st[b]) ++b;
      if (b > n_x) ++n_x;
      // nađi trenutno neiskorišten broj cvijeta
      lab[b] = 0;             // postavi zB=0
      S[b] = 0;               // cijeli cvijet je jedan parni vrh
      match[b] = match[lca];  // spareni brid cvijeta je spareni brid baze cvijeta
      flower[b].clear();
      flower[b].push_back(lca);
      for (int x = u, y; x != lca; x = st[pa[y]]) {
        flower[b].push_back(x);
        y = st[match[x]];
        flower[b].push_back(y);
        q_push(y);
      }
      reverse(flower[b].begin() + 1, flower[b].end());
      for (int x = v, y; x != lca; x = st[pa[y]]) {
        flower[b].push_back(x);
        y = st[match[x]];
        flower[b].push_back(y);
        q_push(y);
      }
      // svi vrhovi iz b dodani su u flower[b] kružnim redoslijedom, a baza cvijeta je prvi element
      set_st(b, b);  // za sve elemente unutar cvijeta postavi cvijet na b
      for (int x = 1; x <= n_x; ++x) {
        g[b][x].w = 0;
        g[x][b].w = 0;
      }
      for (int x = 1; x <= n; ++x) {
        flower_from[b][x] = 0;
      }
      for (size_t i = 0; i < flower[b].size(); ++i) {
        int xs = flower[b][i];
        for (int x = 1; x <= n_x; ++x) {
          // brid između b i x postavi na brid između x i nekog vrha iz b s najmanjim e_delta
          if (g[b][x].w == 0 || e_delta(g[xs][x]) < e_delta(g[b][x])) {
            g[b][x] = g[xs][x];
            g[x][b] = g[x][xs];
          }
        }
        for (int x = 1; x <= n; ++x) {
          if (flower_from[xs][x]) {
            // ako vrh xs unutar b sadrži x
            // tada je flower_from[b][x] jednak xs
            flower_from[b][x] = xs;
          }
        }
      }
      set_slack(b);
      // na kraju obavezno postavi slack vrijednost za b
    }
    ```

???+ note "Razvijanje cvijeta"
    ```cpp
    void expand_blossom(int b) {
      // kad je b neparni cvijet sa zB=0, b treba razviti
      // razvijamo samo b, pa ako b sadrži druge cvjetove
      // njih ne treba razvijati
      for (size_t i = 0; i < flower[b].size(); ++i) {
        set_st(flower[b][i], flower[b][i]);
        // najprije za svaki element flower[b] postavi cvijet na njega samog
      }
      int xr = flower_from[b][g[b][pa[b]].u];
      // xr je cvijet unutar flower[b] u kojem je roditelj vrha b na alternirajućem putu
      int pr = get_pr(b, xr);  // nađi položaj xr i učini 0~pr alternirajućim putem u cvijetu
      for (int i = 0; i < pr; i += 2) {
        // razvij alternirajući put u alternirajuće stablo
        // i stavi parne vrhove alternirajućeg puta u queue
        int xs = flower[b][i];
        int xns = flower[b][i + 1];
        pa[xs] = g[xns][xs].u;
        S[xs] = 1;
        S[xns] = 0;
        slack[xs] = 0;
        set_slack(xns);
        q_push(xns);
      }
      S[xr] = 1;  // xr je sada neparni vrh ili neparni cvijet
      pa[xr] = pa[b];
      for (size_t i = pr + 1; i < flower[b].size(); ++i) {
        // sve vrhove cvijeta koji nisu na alternirajućem putu postavi na neposjećene
        int xs = flower[b][i];
        S[xs] = -1;
        set_slack(xs);
      }
      st[b] = 0;
    }
    ```

???+ note "Pokušaj uvećanja bridom jednakosti"
    ```cpp
    bool on_found_edge(const edge &e) {
      // u BFS-u smo našli brid jednakosti e
      // s njim postupamo ovako
      // ovdje je u sigurno parni vrh
      int u = st[e.u], v = st[e.v];
      if (S[v] == -1) {
        // v je neposjećen vrh
        pa[v] = e.u;
        S[v] = 1;
        int nu = st[match[v]];
        slack[v] = 0;
        slack[nu] = 0;
        S[nu] = 0;
        q_push(nu);
      } else if (S[v] == 0) {
        // v je parni vrh
        int lca = get_lca(u, v);
        if (!lca) {  // lca=0 znači da su u,v u različitim alternirajućim stablima; postoji uvećavajući put
          augment(u, v);
          augment(v, u);
          return true;  // našli smo uvećavajući put
        } else
          add_blossom(u, lca, v);
        // inače su u,v u istom stablu, pa tvore cvijet koji treba sažeti
      }
      return false;
    }
    ```

???+ note "Uvećanje"
    ```cpp
    bool matching() {
      memset(S + 1, -1, sizeof(int) * n_x);
      memset(slack + 1, 0, sizeof(int) * n_x);
      q = queue<int>();  // isprazni queue
      for (int x = 1; x <= n_x; ++x) {
        if (st[x] == x && !match[x]) {
          // sve nesparene vrhove stavi u queue i postavi ih kao parne
          pa[x] = 0;
          S[x] = 0;
          q_push(x);
        }
      }
      if (q.empty()) return false;  // svi su vrhovi spareni
      for (;;) {
        while (q.size()) {
          // BFS
          int u = q.front();
          q.pop();
          if (S[st[u]] == 1) continue;
          for (int v = 1; v <= n; ++v) {
            if (g[u][v].w > 0 && st[u] != st[v]) {
              if (e_delta(g[u][v]) == 0) {
                if (on_found_edge(g[u][v])) return true;
              } else
                update_slack(u, st[v]);
            }
          }
        }
        // promijeni vrijednosti lab
        int d = INF;
        for (int u = 1; u <= n; ++u) {
          // ovo sprječava da se pojavi lab<0
          // čim je neki lab[u]=0, program završava
          if (S[st[u]] == 0) d = min(d, lab[u]);
        }
        for (int b = n + 1; b <= n_x; ++b) {
          if (st[b] == b && S[b] == 1) d = min(d, lab[b] / 2);
        }
        for (int x = 1; x <= n_x; ++x)
          if (st[x] == x && slack[x]) {
            if (S[x] == -1)
              d = min(d, e_delta(g[slack[x]][x]));
            else if (S[x] == 0)
              d = min(d, e_delta(g[slack[x]][x]) / 2);
          }
        for (int u = 1; u <= n; ++u) {
          if (S[st[u]] == 0) {
            if (lab[u] == d) return false;
            // ako je lab[u]=0, odmah završi program
            lab[u] -= d;
          } else if (S[st[u]] == 1)
            lab[u] += d;
        }
        for (int b = n + 1; b <= n_x; ++b) {
          if (st[b] == b) {
            if (S[st[b]] == 0)
              lab[b] += d * 2;
            else if (S[st[b]] == 1)
              lab[b] -= d * 2;
          }
        }
        q = queue<int>();  // isprazni queue
        for (int x = 1; x <= n_x; ++x) {
          // provjeri je li nastao uvećavajući put
          if (st[x] == x && slack[x] && st[slack[x]] != x &&
              e_delta(g[slack[x]][x]) == 0)
            if (on_found_edge(g[slack[x]][x])) return true;
        }
        for (int b = n + 1; b <= n_x; ++b) {
          // operacija EXPAND: razvij sve neparne cvjetove s lab[b]=0
          if (st[b] == b && S[b] == 1 && lab[b] == 0) expand_blossom(b);
        }
      }
      return false;
    }
    ```

???+ note "Glavna funkcija"
    ```cpp
    pair<long long, int> weight_blossom() {
      // glavna funkcija; na početku inicijalizacija
      memset(match + 1, 0, sizeof(int) * n);
      n_x = n;  // na početku nema cvjetova
      int n_matches = 0;
      long long tot_weight = 0;
      for (int u = 0; u <= n; ++u) {
        // najprije za svaki vrh postavi cvijet na njega samog
        st[u] = u;
        flower[u].clear();
      }
      int w_max = 0;
      for (int u = 1; u <= n; ++u)
        for (int v = 1; v <= n; ++v) {
          // kad je u vrh, jedini vrh koji sadrži je on sam
          flower_from[u][v] = (u == v ? u : 0);
          w_max = max(w_max, g[u][v].w);
          // nađi najveću težinu brida
        }
      for (int u = 1; u <= n; ++u) lab[u] = w_max;
      // postavi sve lab = najveća težina brida
      // budući da ovdje ze računamo s dvostrukim težinama, ne treba dijeliti s dva
      while (matching()) ++n_matches;
      for (int u = 1; u <= n; ++u)
        if (match[u] && match[u] < u) tot_weight += g[u][match[u]].w;
      return make_pair(tot_weight, n_matches);
    }
    ```

???+ note "Inicijalizacija"
    Vrlo važno: prije uporabe obavezno inicijalizirati.
    
    ```cpp
    void init_weight_graph() {
      // prije unosa bridova u graf obavezna je inicijalizacija
      // budući da je riječ o najvećem težinskom sparivanju, nepostojeće bridove postavljamo na 0
      for (int u = 1; u <= n; ++u)
        for (int v = 1; v <= n; ++v) g[u][v] = edge(u, v, 0);
    }
    ```

## Analiza složenosti

Svaki se cvijet u jednom BFS-u sažima ili razvija samo jednom. Svako sažimanje ili razvijanje cvijeta ima vremensku složenost $O(|V|)$. Ukupno ima najviše $O(|V|)$ cvjetova, pa obrada cvjetova traje $O(|V|^2)$. BFS ima vremensku složenost $O(|V| + |E|)$. Stoga traženje uvećavajućeg puta ima vremensku složenost $O(|V| + |E|) + O(|V|^2) = O(|V|^2)$.

BFS se izvodi najviše $|V|$ puta. Dakle, ukupna vremenska složenost je $O(|V|^3)$.

## Zadaci

-   [UOJ #81. 一般图最大权匹配](https://uoj.ac/problem/81)

## Literatura

1.  [Kolmogorov, Vladimir (2009), "Blossom V: A new implementation of a minimum cost perfect matching algorithm"](http://pub.ist.ac.at/~vnk/papers/BLOSSOM5.html)
2.  [从匈牙利算法到带权带花树——详解对偶问题在图匹配上的应用 (Od mađarskog algoritma do težinskog algoritma cvjetova – primjena dualnog problema na sparivanje u grafovima)](https://www.luogu.com.cn/blog/potassium/solution-p6699)
