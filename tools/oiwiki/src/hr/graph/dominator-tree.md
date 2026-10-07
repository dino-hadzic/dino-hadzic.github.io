---
title: Stablo dominatora
---

## Uvod

Pojam „dominacije” uveo je 1959. Reese T. Prosser u [članku o tokovima u mrežama](http://portal.acm.org/ft_gateway.cfm?id=1460314&type=pdf&coll=GUIDE&dl=GUIDE&CFID=79528182&CFTOKEN=33765747), ali bez konkretnog algoritma za računanje; tek su 1969. Edward S. Lowry i C. W. Medlock prvi predložili [učinkovit algoritam](http://portal.acm.org/ft_gateway.cfm?id=362838&type=pdf&coll=GUIDE&dl=GUIDE&CFID=79528182&CFTOKEN=33765747). Danas najšire korišteni Lengauer–Tarjanov algoritam predložili su Lengauer i Tarjan 1979. u [članku](https://www.cs.princeton.edu/courses/archive/fall03/cs528/handouts/a%20fast%20algorithm%20for%20finding.pdf).

U natjecateljskom svijetu pojam stabla dominatora prvi se put pojavio u zadatku [ZJOI2012 Katastrofa](https://www.luogu.com.cn/problem/P2597), gdje se nazivalo i „stablom izumiranja”; Chen Sunli predstavio je ovaj algoritam i u radu za kinesku nacionalnu reprezentaciju 2020.

Stablo dominatora trenutno nije popularno u natjecateljskom programiranju i zadataka s njim nema mnogo, ali se u industriji, posebno u području prevoditelja (compilera), široko koristi.

Ovaj članak predstavlja pojam stabla dominatora i nekoliko metoda za njegovo računanje.

## Odnos dominacije

U proizvoljnom usmjerenom grafu odaberemo ulazni vrh $s$. Za vrh $u$, ako svaki put iz $s$ do $u$ prolazi kroz neki vrh $v$, kažemo da $v$ **dominira** $u$, odnosno da je $v$ **dominator** vrha $u$, i pišemo $v\ dom\ u$.

Za vrhove nedostižne iz $s$ nema smisla raspravljati o dominaciji, pa u ovom članku, ako nije drugačije rečeno, pretpostavljamo da $s$ može doseći svaki vrh grafa.

![](images/dom-tree1.png)

Na primjer, u ovom usmjerenom grafu $2$ dominira $1$, $3$ dominiraju $1, 2$, 4 dominiraju $1, 2, 3$, 5 dominiraju $1, 2$, itd.

### Leme

U lemama u nastavku pretpostavljamo $u, v, w\ne s$

**Lema 1:** $s$ je dominator svih vrhova; svaki vrh je dominator samog sebe.

**Dokaz:** Očito svaki put iz $s$ do $u$ mora proći kroz vrhove $s$ i $u$.

**Lema 2:** Odnos dominacije dobiven promatranjem samo jednostavnih puteva jednak je odnosu dobivenom promatranjem svih puteva.

**Dokaz:** Za put koji nije jednostavan, neka je $S$ skup vrhova kroz koje prolazimo između dvaju prolazaka kroz isti vrh; brisanjem vrhova iz $S$ svakom putu koji nije jednostavan možemo pridružiti jednostavan put.

Vrh iz $S$ koji je na nejednostavnom putu, a nije na jednostavnom, sigurno ne može biti dominator, jer barem jedan jednostavan put iz $s$ do $u$ ne sadrži taj vrh; za vrhove koji su i na jednostavnom i na nejednostavnom putu dovoljno je promatrati jednostavan put.

Dakle, odbacivanje nejednostavnih puteva ne utječe na odnos dominacije.

**Lema 3:** Ako $u$ $dom$ $v$ i $v$ $dom$ $w$, tada $u$ $dom$ $w$.

**Dokaz:** Put kroz $w$ nužno prolazi kroz $v$, a put kroz $v$ nužno prolazi kroz $u$, pa put kroz $w$ nužno prolazi kroz $u$, tj. $u \ dom \ w$.

**Lema 4:** Ako $u \ dom \ v$ i $v \ dom\ u$, tada $u=v$.

**Dokaz:** Pretpostavimo $u \ne v$; tada je svaki put koji dolazi do $v$ već prošao kroz $u$, a ujedno je svaki put koji dolazi do $u$ već prošao kroz $v$, što je kontradikcija.

**Lema 5:** Ako $u \ne v \ne w$, $u \ dom \ w$ i $v \ dom \ w$, tada vrijedi $u \ dom \ v$ ili $v \ dom \ u$.

**Dokaz:** Promotrimo put $s \rightarrow \dots \rightarrow u \rightarrow \dots \rightarrow v \rightarrow \dots \rightarrow w$. Ako između $u$ i $v$ nema odnosa dominacije, sigurno postoji put iz $s$ do $v$ koji ne prolazi kroz $u$, tj. postoji put $s \rightarrow \dots \rightarrow v \rightarrow \dots \rightarrow w$, što je u suprotnosti s $u\ dom\ w$.

### Računanje odnosa dominacije

#### Metoda brisanja vrhova

Tvrdnja ekvivalentna definiciji: ako nakon brisanja nekog vrha iz grafa neki vrhovi postanu nedostižni, tada izbrisani vrh dominira te vrhove koji su postali nedostižni.

Stoga je dovoljno pokušati izbrisati svaki vrh i zatim pokrenuti dfs; složenost je $O(n^3)$. U nastavku je ključni dio kôda.

```cpp
// pretpostavljamo da graf ima n vrhova, početni vrh s = 1
std::bitset<N> vis;
std::vector<int> edge[N];
std::vector<int> dom[N];

void dfs(int u, int del) {
  vis[u] = true;
  for (int v : edge[u]) {
    if (v == del or vis[v]) {
      continue;
    }
    dfs(v, del);
  }
}

void getdom() {
  for (int i = 2; i <= n; ++i) {
    vis.reset();
    dfs(1, i);
    for (int j = 1; j <= n; ++j) {
      if (!vis[j]) {
        dom[j].push_back(i);
      }
    }
  }
}
```

#### Iterativna metoda analize toka podataka

Iterativna metoda analize toka podataka također je tema rijetka u natjecateljskom programiranju, pa je najprije kratko predstavljamo.

Analiza toka podataka pojam je iz teorije prevoditelja i služi analizi toka podataka duž putova izvršavanja programa; iterativna metoda postavlja jednadžbe na vrhovima dijagrama toka programa i iterativno ih rješava kako bi se dobile vrijednosti toka podataka u određenim točkama programa. Ovdje usmjereni graf promatramo kao dijagram toka programa.

U ovom problemu jednadžba glasi:

$$
dom(u)=\{u\} \cup \left(\bigcap_{v\in pre(u)}{dom(v)}\right)
$$

gdje je $pre(u)$ skup prethodnika vrha $u$. Ova se jednadžba dobiva iz leme 3.

Riječima: skup dominatora vrha jednak je presjeku skupova dominatora svih njegovih prethodnika, uniji sa samim vrhom. Prema ovoj jednadžbi iterativno ažuriramo skup dominatora svakog vrha dok se odgovor više ne mijenja.

Radi učinkovitosti želimo da u svakoj iteraciji za vrh koji obrađujemo svi njegovi prethodnici po mogućnosti već budu obrađeni u toj iteraciji; stoga pomoću dubinskog obilaska odredimo obrnuti postorder grafa i iteriramo u tom poretku.

U nastavku je referentna implementacija ključnog dijela kôda. Potrebno je unaprijed izračunati skup prethodnika svakog vrha i obrnuti postorder grafa, ali to nije glavna tema ovog članka, pa za to ne dajemo implementaciju.

```cpp
std::vector<int> pre[N];  // prethodnici svakog vrha
std::vector<int> ord;     // obrnuti postorder grafa
std::bitset<N> dom[N];
std::vector<int> Dom[N];

void getdom() {
  dom[1][1] = true;
  flag = true;
  while (flag) {
    flag = false;
    for (int u : ord) {
      std::bitset<N> tmp;
      tmp[u] = true;
      for (int v : pre[u]) {
        tmp &= dom[v];
      }
      if (tmp != dom[u]) {
        dom[u] = tmp;
        flag = true;
      }
    }
  }
  for (int i = 2; i <= n; ++i) {
    for (int j = 1; j <= n; ++j) {
      if (dom[i][j]) {
        Dom[i].push_back(j);
      }
    }
  }
}
```

Lako se vidi da je složenost gornjeg algoritma $O(n^2)$.

## Stablo dominatora

U prethodnom odjeljku vidjeli smo da svaki vrh osim $s$ ima barem dva dominatora: $s$ i samog sebe.

Za proizvoljan vrh $u$, dominator $v$ koji je među njegovim dominatorima (osim njega samog) najbliži vrhu $u$ nazivamo neposrednim dominatorom vrha $u$ i pišemo $idom(u) = v$. Očito, osim $s$ koji nema neposrednog dominatora, svaki vrh ima točno jedan neposredni dominator.

Ako za svaki vrh $u$ osim $s$ povučemo brid od $idom(u)$ do $u$, dobivamo usmjereni graf s $n$ vrhova i $n - 1$ bridova. Prema lemama 3 i 4 znamo da odnos dominacije ne može biti cikličan, tj. ti bridovi sigurno ne tvore ciklus, pa je dobiveni graf zapravo stablo. To stablo nazivamo **stablom dominatora** izvornog grafa.

## Računanje stabla dominatora

### Računanje iz dom

Promotrimo skup dominatora nekog vrha $\{s_1, s_2, \dots, s_k\}$; tada sigurno postoji put $s \rightarrow \dots \rightarrow s_1 \rightarrow \dots \rightarrow s_2 \rightarrow \dots \rightarrow \dots \rightarrow s_k \rightarrow\dots \rightarrow u$. Očito je neposredni dominator vrha $u$ upravo $s_k$. Stoga je definicija neposrednog dominatora ekvivalentna sljedećoj:

Za skup dominatora $S$ vrha $u$, ako $v \in S$ zadovoljava $\forall w \in S\setminus\{u,v\}, w\ dom \ v$, tada je $idom(u)=v$.

Dakle, nakon što prethodno opisanim algoritmima dobijemo skup dominatora svakog vrha, prema gornjoj definiciji lako dobivamo neposredni dominator svakog vrha i tako gradimo stablo dominatora. U nastavku je referentni kôd.

```cpp
std::bitset<N> dom[N];
std::vector<int> Dom[N];
int idom[N];

void getidom() {
  for (int u = 2; u <= n; ++u) {
    for (int v : Dom[u]) {
      std::bitset<N> tmp = (dom[v] & dom[u]) ^ dom[u];
      if (tmp.count() == 1 and tmp[u]) {
        idom[u] = v;
        break;
      }
    }
  }
  for (int u = 2; u <= n; ++u) {
    e[idom[u]].push_back(u);
  }
}
```

### Poseban slučaj: stablo

Očito je stablo dominatora stablastog grafa on sam.

### Poseban slučaj: DAG

Uočavamo da DAG ima lijepo svojstvo: ako računamo po topološkom poretku, ranije dobivena rješenja ne utječu na kasnija. To svojstvo možemo iskoristiti za brzo računanje stabla dominatora DAG-a.

???+ warning "Napomena"
    Treba napomenuti da DAG ovdje smije imati samo jedan početni vrh; ako ih ima više, vrhovi dominirani početnim vrhovima imali bi u stablu dominatora više roditelja, pa se odnos dominacije ne bi mogao jednostavno izraziti stablom dominatora.

**Lema 6:** U usmjerenom grafu $v\ dom\ u$ ako i samo ako $\forall w \in pre(u), v\ dom \ w$.

**Dokaz:** Prvo dokažimo dostatnost. Svaki put iz $s$ do $u$ nužno prolazi kroz neki vrh $w \in pre(u)$, a $v$ dominira taj vrh, pa svaki put iz $s$ do $u$ nužno prolazi kroz $v$; dakle, $v \ dom \ u$.

Zatim nužnost. Ako $\exists w\in pre(u)$ takav da $v$ ne dominira $w$, tada sigurno postoji put $s \rightarrow \cdots \rightarrow w \rightarrow \cdots \rightarrow u$ koji ne prolazi kroz $v$, pa $v$ ne dominira $u$.

Uočavamo da je dominator vrha $u$ nužno zajednički predak svih njegovih prethodnika u stablu dominatora, pa je očito neposredni dominator vrha $u$ upravo LCA svih prethodnika u stablu dominatora. Računanje LCA binarnim skakanjem podržava dodavanje jednog vrha u svakom koraku, pa je gornji algoritam očito izvediv.

U nastavku je referentna implementacija:

```cpp
std::stack<int> sta;
std::vector<int> e[N], g[N], tree[N];  // g je obrnuti graf izvornog grafa, tree je stablo dominatora
int n, s, in[N], tpn[N], dep[N], idom[N];  // n je ukupan broj vrhova, s je početni vrh, in je ulazni stupanj
int fth[N][17];

void topo(int s) {
  sta.push(s);
  while (!sta.empty()) {
    int u = sta.top();
    sta.pop();
    tpn[++tot] = u;
    for (int v : e[u]) {
      --in[v];
      if (!in[v]) {
        sta.push(v);
      }
    }
  }
}

int lca(int u, int v) {
  if (dep[u] < dep[v]) {
    std::swap(u, v);
  }
  for (int i = 15; i >= 0; --i) {
    if (dep[fth[u][i]] >= dep[v]) {
      u = fth[u][i];
    }
  }
  if (u == v) {
    return u;
  }
  for (int i = 15; i >= 0; --i) {
    if (fth[u][i] != fth[v][i]) {
      u = fth[u][i];
      v = fth[v][i];
    }
  }
  return fth[u][0];
}

void build() {
  topo(s);
  for (int i = 1; i <= n; ++i)
    for (int j = 0; j <= 15; ++j) fth[i][j] = s;
  for (int i = 1; i <= n; ++i) {
    int u = tpn[i];
    if (g[u].size()) {
      int v = g[u][0];
      for (int j = 1, q = g[u].size(); j < q; ++j) {
        v = lca(v, g[u][j]);
      }
      tree[v].push_back(u);
      fth[u][0] = v;
      dep[u] = dep[v] + 1;
      for (int i = 1; i <= 15; ++i) {
        fth[u][i] = fth[fth[u][i - 1]][i - 1];
      }
    }
  }
}

```

### Lengauer–Tarjanov algoritam

Lengauer–Tarjanov algoritam jedan je od najpoznatijih algoritama za računanje stabla dominatora; stablo dominatora usmjerenog grafa računa u vremenskoj složenosti $O(n\alpha(n, m))$. Algoritam uvodi pojam **poludominatora** i pomoću poludominatora računa neposredne dominatore.

#### Dogovori

Najprije iz $s$ obavimo dfs usmjerenog grafa; posjećeni vrhovi i bridovi tvore stablo $T$. Prijeđene bridove nazivamo bridovima stabla, a ostale nestablastim bridovima; neka $dfn(u)$ označava redni broj posjeta vrha $u$; definiramo $u<v$ ako i samo ako $dfn(u) < dfn(v)$.

#### Poludominator

Poludominator vrha $u$ je najmanji među vrhovima $v$ takvima da iz $v$ postoji put do $u$ na kojem je svaki vrh osim $u, v$ veći od $u$. Formalno, poludominator $sdom(u)$ vrha $u$ definira se kao:

$sdom(u) = \min(v|\exists v=v_0 \rightarrow v_1 \rightarrow\dots \rightarrow v_k = u, \forall 1\le i\le k - 1, v_i > u)$

Poludominator ima nekoliko korisnih svojstava:

**Lema 7:** Za svaki vrh $u$ vrijedi $sdom(u) < u$.

**Dokaz:** Iz definicije se lako vidi da roditelj $fa(u)$ vrha $u$ u $T$ također zadovoljava uvjet za poludominatora, a $fa(u) < u$, pa nijedan vrh veći od $u$ ne može biti njegov poludominator.

**Lema 8:** Za svaki vrh $u$, $idom(u)$ je njegov predak u $T$.

**Dokaz:** Put u $T$ od $s$ do $u$ odgovara putu u izvornom grafu, pa $idom(u)$ nužno leži na tom putu.

**Lema 9:** Za svaki vrh $u$, $sdom(u)$ je njegov predak u $T$.

**Dokaz:** Pretpostavimo da $sdom(u)$ nije predak od $u$. Tada $sdom(u)$ ne može imati brid prema nijednom vrhu s $\mathrm{dfs}$ rednim brojem većim ili jednakim $u$ (inače bi taj vrh bio u podstablu od $sdom(u)$, a ne u drugom podstablu), što je kontradikcija.

**Lema 10:** Za svaki vrh $u$, $idom(u)$ je predak od $sdom(u)$.

**Dokaz:** Možemo iz $s$ doći do $sdom(u)$, a zatim putem iz definicije do $u$. Prema definiciji, vrhovi na putu od $sdom(u)$ do $u$ ne dominiraju $u$, pa $idom(u)$ mora biti predak od $sdom(u)$.

**Lema 11:** Za sve vrhove $u \ne v$ takve da je $v$ predak od $u$, vrijedi ili da je $v$ predak od $idom(u)$, ili da je $idom(u)$ predak od $idom(v)$.

**Dokaz:** Za svaki vrh $w$ između $v$ i $idom(v)$, prema definiciji neposrednog dominatora sigurno postoji put iz $s$ do $idom(v)$ pa do $v$ koji ne prolazi kroz $w$. Stoga ti vrhovi $w$ sigurno nisu $idom(u)$, pa je $idom(u)$ ili potomak od $v$, ili predak od $idom(v)$.

Iz gornjih lema dobivamo sljedeći teorem:

**Teorem 1:** Poludominator vrha $u$ je najmanji vrh među njegovim prethodnicima i poludominatorima svih predaka (u $T$) njegovih prethodnika koji su veći od $u$. Formalno, $sdom(u)=\min(\{v|\exists v \rightarrow u, v < u \} \cup \{sdom(w) | w > u\ and\ \exists w \rightarrow \dots \rightarrow v \rightarrow u \})$.

**Dokaz:** Neka je $x$ jednak desnoj strani gornjeg izraza.

Prvo dokažimo $sdom(u) \le x$. Prema lemi 7 znamo da je ta tvrdnja ekvivalentna tome da oba gornja slučaja zadovoljavaju uvjet za poludominatora. Slučaj kad je $x$ prethodnik od $u$ je očit; za drugi dio, spojimo put $x=v_0\rightarrow\dots\rightarrow v_j=w$ iz definicije poludominatora, put u $T$ $w=v_j \rightarrow\dots\rightarrow v_k=v$ koji zadovoljava $\forall i\in[j, k-1], v_i\ge w > u$, i put $v \rightarrow u$; tako konstruiramo put koji zadovoljava definiciju poludominatora.

Zatim dokažimo $sdom(u)\ge x$. Promotrimo put iz definicije poludominatora $sdom(u)=v_0\rightarrow v_1 \rightarrow\dots\rightarrow v_k=u$. Lako se vidi da $k=1$ i $k > 1$ odgovaraju dvama načinima izbora iz definicije. Ako je $k = 1$, postoji usmjereni brid $sdom(u) \rightarrow u$, pa tvrdnja slijedi iz leme 7; ako je $k>1$, neka je $j$ najmanji broj takav da $j \ge 1$ i da je $v_j$ predak od $v_{k-1}$ u $T$. Budući da $k$ zadovoljava taj uvjet, takav $j$ sigurno postoji.

Dokažimo da je $v_0 \rightarrow \dots \rightarrow v_j$ put koji zadovoljava uvjet za poludominatora vrha $v_j$, tj. da $\forall i \in [1, j), v_i>v_j$. Ako nije, neka je $i$ onaj broj s $v_i < v_j$ za koji je $v_i$ najmanji. Tada su svi vrhovi na putu $v_i\rightarrow\dots\rightarrow v_j$ barem $v_i$, pa je po svojstvu dfs stabla $v_i$ sigurno predak od $v_j$, a time i predak od $v_{k-1}$, što je u suprotnosti s minimalnošću $j$. Dakle, $sdom(v_j)\le sdom(u)$. Budući da je $x\le sdom(v_j)$, slijedi $sdom(u)\ge x$. Zajedno s ranije dokazanim $sdom(u) \le x$ dobivamo $x=sdom(u)$.

Prema teoremu 1 možemo izračunati poludominator svakog vrha. Lako se vidi da je usko mjesto složenosti računanja poludominatora drugi slučaj; optimiziramo ga strukturom disjunktnih skupova s težinama, ažurirajući minimum pri svakom sažimanju puta.

```cpp
void dfs(int u) {
  dfn[u] = ++dfc;
  pos[dfc] = u;
  for (int i = h[0][u]; i; i = e[i].x) {
    int v = e[i].v;
    if (!dfn[v]) {
      dfs(v);
      fth[v] = u;
    }
  }
}

int find(int x) {
  if (fa[x] == x) {
    return x;
  }
  int tmp = fa[x];
  fa[x] = find(fa[x]);
  if (dfn[sdm[mn[tmp]]] < dfn[sdm[mn[x]]]) {
    mn[x] = mn[tmp];
  }
  return fa[x];
}

void getsdom() {
  dfs(1);
  for (int i = 1; i <= n; ++i) {
    mn[i] = fa[i] = sdm[i] = i;
  }
  for (int i = dfc; i >= 2; --i) {
    int u = pos[i], res = INF;
    for (int j = h[1][u]; j; j = e[j].x) {
      int v = e[j].v;
      if (!dfn[v]) {
        continue;
      }
      find(v);
      if (dfn[v] < dfn[u]) {
        res = std::min(res, dfn[v]);
      } else {
        res = std::min(res, dfn[sdm[mn[v]]]);
      }
    }
    sdm[u] = pos[res];
    fa[u] = fth[u];
  }
}

```

#### Računanje neposrednog dominatora

##### Pretvorba u DAG

Ali još uvijek ne znam čemu služe poludominatori!

Dodajmo u $T$ za svaki $u$ usmjereni brid $sdom(u) \rightarrow u$. Prema lemi 9, novodobiveni graf $G$ sigurno je usmjereni aciklički graf; prema lemi 10 vidimo i da ovakvo dodavanje bridova ne mijenja odnos dominacije, pa smo izvorni graf pretvorili u DAG i možemo primijeniti gore opisani algoritam.

##### Računanje pomoću poludominatora

Graditi hrpu grafova previše je neelegantno!

**Teorem 2:** Za svaki vrh $u$, ako svaki vrh $v$ na putu u $T$ od $sdom(u)$ do $w$ zadovoljava $sdom(v)\ge sdom(w)$, tada je $idom(u) =sdom(u)$.

**Dokaz:** Prema lemi 10 znamo da je $idom(u)$ ili $sdom(u)$ ili njegov predak, pa je dovoljno dokazati $sdom(u) \ dom \ u$.

Promotrimo proizvoljan put $P$ iz $s$ do $u$; trebamo dokazati da $sdom(u)$ nužno leži na $P$. Neka je $v$ posljednji vrh na $P$ koji zadovoljava $v<sdom(u)$. Ako $v$ ne postoji, nužno je $sdom(u)=idom(u) =s$; inače neka je $w$ prvi vrh na $P$ nakon $v$ koji leži na putu u DFS stablu od $sdom(u)$ do $u$.

Dokažimo sada $sdom(w)\le v <sdom(v)$. Promotrimo put u $T$ od $v$ do $w$, $v = v_0 \rightarrow \dots v_k = w$. Ako tvrdnja ne vrijedi, postoji $i\in[1, k- 1], v_i < w$. Tada sigurno postoji neki $j\in [i, k - 1]$ takav da je $v_j$ predak od $w$. Iz izbora $v$ znamo da je $sdom(u)\le v_j$, pa i $v_j$ leži na putu u DFS stablu od $sdom(u)$ do $u$, što je u suprotnosti s definicijom $w$. Dakle, $sdom(w)\le v < sdom(v)$, a u kombinaciji s uvjetom teorema dobivamo $y=sdom(u)$, tj. put $P$ sadrži $sdom(u)$.

**Teorem 3:** Za svaki vrh $u$, vrh $v$ s najmanjim poludominatorom među svim vrhovima na putu u $T$ od $sdom(u)$ do $u$ sigurno zadovoljava $sdom(v)\le sdom(u)$ i $idom(v) = idom(u)$.

**Dokaz:** Budući da i sam $u$ zadovoljava uvjet za $v$, vrijedi $sdom(v)\le sdom(u)$.

Budući da je $idom(u)$ predak od $v$ u $T$, prema lemi 11 $idom(u)$ je i predak od $idom(v)$, pa je dovoljno dokazati da $idom(v)$ dominira $u$.

Promotrimo proizvoljan put $P$ iz $s$ do $u$; trebamo dokazati da $sdom(u)$ nužno leži na $P$. Neka je $x$ posljednji vrh na $P$ koji zadovoljava $x<sdom(u)$. Ako $x$ ne postoji, nužno je $sdom(u)=idom(u) =s$; inače neka je $y$ prvi vrh na $P$ nakon $x$ koji leži na putu u DFS stablu od $sdom(u)$ do $u$.

Analogno dokazu teorema 2 dobivamo $sdom(y) \le x$. Prema lemi 10 vrijedi $sdom(y)\le x<idom(v) \le sdom(v)$. Iz definicije $v$ sada znamo da $y$ ne može biti potomak od $sdom(u)$; s druge strane, $y$ ne može biti istodobno potomak od $idom(v)$ i predak od $v$, jer bi inače put koji ide DFS stablom od $s$ do $sdom(y)$, zatim po P do $y$, a na kraju DFS stablom do $v$, zaobišao $idom(v)$, što je u suprotnosti s definicijom dominatora. Dakle, $y=idom(v)$, tj. $P$ sadrži $idom(v)$.

Iz gornjih dvaju teorema dobivamo vezu između $sdom(u)$ i $idom(u)$.

Neka je $v$ vrh s najmanjim $sdom(v)$ među svim vrhovima između $sdom(u)$ i $u$. Tada:

$$
idom(u) =
\left\{ 
\begin{aligned} 
& sdom(u), &\text{ako}\ sdom(u) = sdom(v)
\\
&idom(v), &\text{inače}
\end{aligned}
\right.
$$

Dovoljno je malo izmijeniti gornji kôd za računanje poludominatora.

```cpp
struct E {
  int v, x;
} e[MAX * 4];

int h[3][MAX * 2];

int dfc, tot, n, m, u, v;
int fa[MAX], fth[MAX], pos[MAX], mn[MAX], idm[MAX], sdm[MAX], dfn[MAX],
    ans[MAX];

void add(int x, int u, int v) {
  e[++tot] = {v, h[x][u]};
  h[x][u] = tot;
}

void dfs(int u) {
  dfn[u] = ++dfc;
  pos[dfc] = u;
  for (int i = h[0][u]; i; i = e[i].x) {
    int v = e[i].v;
    if (!dfn[v]) {
      dfs(v);
      fth[v] = u;
    }
  }
}

int find(int x) {
  if (fa[x] == x) {
    return x;
  }
  int tmp = fa[x];
  fa[x] = find(fa[x]);
  if (dfn[sdm[mn[tmp]]] < dfn[sdm[mn[x]]]) {
    mn[x] = mn[tmp];
  }
  return fa[x];
}

void tar(int st) {
  dfs(st);
  for (int i = 1; i <= n; ++i) {
    fa[i] = sdm[i] = mn[i] = i;
  }
  for (int i = dfc; i >= 2; --i) {
    int u = pos[i], res = INF;
    for (int j = h[1][u]; j; j = e[j].x) {
      int v = e[j].v;
      if (!dfn[v]) {
        continue;
      }
      find(v);
      if (dfn[v] < dfn[u]) {
        res = std::min(res, dfn[v]);
      } else {
        res = std::min(res, dfn[sdm[mn[v]]]);
      }
    }
    sdm[u] = pos[res];
    fa[u] = fth[u];
    add(2, sdm[u], u);
    u = fth[u];
    for (int j = h[2][u]; j; j = e[j].x) {
      int v = e[j].v;
      find(v);
      if (sdm[mn[v]] == u) {
        idm[v] = u;
      } else {
        idm[v] = mn[v];
      }
    }
    h[2][u] = 0;
  }
  for (int i = 2; i <= dfc; ++i) {
    int u = pos[i];
    if (idm[u] != sdm[u]) {
      idm[u] = idm[idm[u]];
    }
  }
}

```

## Primjeri zadataka

### [Luogu P5180 【Predložak】Stablo dominatora](https://www.luogu.com.cn/problem/P5180)

Može se računati samo odnos dominacije i pri tome bilježiti koliko vrhova svaki vrh dominira, a može se i izgraditi stablo dominatora i izračunati veličina podstabla svakog vrha.

Ovdje dajemo kôd drugog pristupa.

??? note "Referentni kôd"
    ```cpp
    --8<-- "docs/graph/code/dom-tree/dom-tree_1.cpp"
    ```

### [ZJOI2012 Katastrofa](https://www.luogu.com.cn/problem/P2597)

Dovoljno je na DAG-u izračunati stablo dominatora i zatim veličine podstabala.

??? note "Referentni kôd"
    ```cpp
    --8<-- "docs/graph/code/dom-tree/dom-tree_2.cpp"
    ```
