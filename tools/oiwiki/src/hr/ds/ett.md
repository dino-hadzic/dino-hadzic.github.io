---
title: Euler Tour Tree
---

author: Backl1ght

Euler Tour Tree (stablo Eulerova obilaska, stablo Eulerove ture; dalje kratko ETT) struktura je podataka kojom se mogu rješavati problemi **dinamičkih stabala**. ETT operacije nad dinamičkim stablom pretvara u intervalne operacije nad njegovim DFS nizom, a te intervalne operacije nad nizom održava nekom drugom strukturom podataka i tako održava operacije nad dinamičkim stablom. Primjerice, ETT dodavanje brida u dinamičko stablo pretvara u više operacija razdvajanja i spajanja nizova; ako znamo održavati razdvajanje i spajanje nizova, znamo održavati i dodavanje brida u dinamičko stablo.

LCT je također struktura podataka za probleme dinamičkih stabala i u odnosu na ETT znatno je češći. LCT je zapravo prikladniji za održavanje informacija o lancima u stablu, dok je ETT prikladniji za održavanje informacija o **podstablima**. Primjerice, ETT može održavati minimum podstabla, a LCT ne može.

ETT se može održavati bilo kojom strukturom podataka, pod uvjetom da ta struktura podržava odgovarajuće intervalne operacije nad nizom i da zadovoljava zahtjeve složenosti. Obično se niz održava balansiranim binarnim stablima pretraživanja kao što su Splay ili Treap; složenost intervalnih operacija u tim strukturama iznosi $O(\log n)$, pa se i operacije nad dinamičkim stablom mogu održavati u vremenu $O(\log n)$. Ako se intervalne operacije održavaju višestrukim balansiranim stablima pretraživanja, npr. B-stablom, može se postići i bolja složenost.

ETT se zapravo može shvatiti kao ideja: održavanjem nekog niza koji je u bijekciji s izvornim stablom postiže se održavanje izvornog stabla; ovaj članak opisuje samo neke izvedive implementacije i primjene te ideje.

## Prikaz stabla Eulerovom turom

Ako svaki brid stabla promatramo kao dva usmjerena brida, stablo se može prikazati kao Eulerova tura usmjerenog grafa; to se naziva prikaz stabla Eulerovom turom (Euler tour representation, ETR).

Niz koji ćemo kasnije održavati zapravo je inačica ETR-a u koju su kao petlje dodani i vrhovi stabla, ali budući da joj autori izvornog rada nisu dali novo ime, i dalje ćemo je zvati ETR.

Prikaz stabla $T$ Eulerovom turom dobiva se sljedećim algoritmom:

$$
\begin{array}{ll}
1 & \textbf{Input. } \text{A rooted tree }T\\
2 & \textbf{Output. } \text{The dfs sequence of rooted tree }T\\
3 & \operatorname{ET}(u)\\
4 & \qquad \text{visit vertex }u\\
5 & \qquad \text{for all child } v \text{ of } u\\
6 & \qquad \qquad \text{visit directed edge } u \to v\\
7 & \qquad \qquad \operatorname{ET}(v)\\
8 & \qquad \qquad \text{visit directed edge } v \to u\\
\end{array}
$$

Prikaz stabla $T$ Eulerovom turom $\operatorname{ETR}(T)$ početno je prazan; tijekom DFS-a pri svakom posjetu vrha ili usmjerenog brida dodamo ga na kraj $\operatorname{ETR}(T)$ i tako dobijemo $\operatorname{ETR}(T)$.

Ako $T$ sadrži $n$ vrhova, sadrži $2n - 2$ usmjerenih bridova, a tijekom DFS-a svaki vrh i svaki usmjereni brid posjećuje se točno jednom, pa je duljina $\operatorname{ETR}(T)$ jednaka $3n - 2$.

Ako vrh $u$ promatramo kao petlju, $\operatorname{ETR}(T)$ možemo smatrati Eulerovom turom u usmjerenom grafu. Eulerovu turu možemo prekinuti na nekom mjestu i promatrati je kao lanac bridova spojenih kraj uz početak; takav lanac možemo na mjestu prekida ponovno zalijepiti u Eulerovu turu; a dodavanjem nekoliko bridova možemo dva takva lanca spojiti u novu Eulerovu turu.

U nastavku, ako nije drugačije rečeno, održavani niz je prikaz stabla Eulerovom turom.

## Osnovne operacije ETT-a

Sljedeće tri operacije smatraju se osnovnim operacijama ETT-a; sve se mogu pretvoriti u konstantan broj operacija nad nizom, pa je njihova složenost istog reda kao i složenost operacija nad nizom.

Ovdje je dana samo jedna izvediva implementacija; dovoljno je da se konstantnim brojem operacija nad nizom može sastaviti niz koji odgovara izmijenjenom stablu.

### MakeRoot(u)

Odnosno promjena korijena. Promjena korijena u ETT-u pretvara se u jedno razdvajanje i jedno spajanje niza, što se može shvatiti i kao jedan ciklički pomak intervala.

Neka je $T$ stablo koje sadrži vrh $u$, neka je njegov trenutačni korijen $r$ i neka korijen želimo promijeniti na $u$. Niz koji odgovara stablu $T$ označimo s $L$. Razdvojimo $L$ na mjestu $(u, u)$ na nizove $L^1$ i $L^2$, pri čemu prvi sadrži elemente $L$ ispred $(u, u)$ zajedno s $(u, u)$, a drugi preostale elemente. Tada niz dobiven spajanjem $L^2$ i $L^1$ tim redom odgovara stablu nakon promjene korijena.

To se može shvatiti kao rotacija Eulerove ture: Eulerova tura je ciklus, a rotacija ne mijenja strukturu Eulerove ture, dakle ni strukturu stabla, nego samo zarotira vrh $u$ na položaj korijena.

### Insert(u, v)

Odnosno dodavanje brida. Dodavanje brida u ETT-u pretvara se u dva razdvajanja i pet spajanja niza.

Neka je $T_1$ stablo koje sadrži vrh $u$, $T_2$ stablo koje sadrži vrh $v$, a nakon dodavanja brida ta se dva stabla spoje u jedno stablo $T$. Niz koji odgovara stablu $T_1$ označimo s $L_1$, a niz koji odgovara stablu $T_2$ s $L_2$.

Razdvojimo $L_1$ na mjestu $(u, u)$ na nizove $L_1^1$ i $L_1^2$, pri čemu prvi sadrži elemente $L_1$ ispred $(u, u)$ zajedno s $(u, u)$, a drugi preostale elemente. Slično razdvojimo $L_2$ na mjestu $(v, v)$ na nizove $L_2^1$ i $L_2^2$. Spajanjem $L_1^2, L_1^1, [(u, v)], L_2^2, L_2^1,  [(v, u)]$ tim redom dobivamo niz $L$ koji odgovara stablu $T$.

To se može shvatiti kao dvije promjene korijena, nakon čega se dvije Eulerove ture prekinu na položaju trenutačnog korijena i pomoću dva nova usmjerena brida spoje u novu Eulerovu turu.

### Delete(u, v)

Odnosno brisanje brida. Brisanje brida u ETT-u pretvara se u četiri razdvajanja i jedno spajanje niza.

Neka je $T$ stablo koje sadrži bridove $(u, v)$ i $(v, u)$, a $L$ njegov odgovarajući niz. Nakon brisanja brida $T$ se raspada na dva stabla.

Razdvojimo $L$ na $L_1, [(u, v)], L_2, [(v, u)], L_3$; nizovi koji odgovaraju dvama stablima nastalima brisanjem brida jesu $L_2$ odnosno $L_1, L_3$. Pazite: u nizu $L$ $[(u, v)]$ se može pojaviti iza $[(v, u)]$; u tom slučaju najprije zamijenimo vrijednosti $u$ i $v$, a zatim provedemo operaciju.

To se može shvatiti kao prekidanje Eulerove ture na dva usmjerena brida u dva lanca, nakon čega se svaki lanac sam spoji kraj uz početak u novu Eulerovu turu.

## Implementacija

U nastavku opisujemo implementaciju ETT-a na primjeru Treapa bez rotacija; čitatelj bi prethodno trebao poznavati održavanje intervalnih operacija Treapom bez rotacija.

`Split` i `Merge` osnovne su operacije Treapa bez rotacija i ovdje ih ne ponavljamo.

### SplitUp2(u)

Neka je $L$ niz u kojem se nalazi $u$; razdvojimo $L$ na mjestu $u$ na nizove $L^1$ i $L^2$, pri čemu prvi sadrži elemente $L$ ispred $u$ zajedno s $u$, a drugi preostale elemente.

Ako svaki čvor Treapa dodatno pamti svog roditelja, položaj elementa koji odgovara čvoru Treapa u nizu može se izračunati u vremenu $O(\log n)$, a zatim prema položaju napraviti `Split` i tako ostvariti traženu funkcionalnost.

Isto se može postići i razdvajanjem odozdo prema gore, što je učinkovitije od gornje metode. Konkretno, dok se od čvora koji odgovara $u$ penjemo prema korijenu, prema svojstvu binarnog stabla pretraživanja za svaki čvor možemo odrediti nalazi li se u $L$ ispred ili iza $u$; po tome možemo izračunati položaj $u$ u nizu i odrediti kojem od dvaju stabala nakon razdvajanja pripada svaki čvor.

```cpp
/*
 * Bottom up split treap p into 2 treaps a and b.
 *   - a: a treap containing nodes with position less than or equal to p.
 *   - b: a treap containing nodes with postion greater than p.
 *
 * In the other word, split sequence containning p into two sequences, the first
 * one contains elements before p and element p, the second one contains
 * elements after p.
 */
static std::pair<Node*, Node*> SplitUp2(Node* p) {
  Node *a = nullptr, *b = nullptr;
  b = p->right_;
  if (b) b->parent_ = nullptr;
  p->right_ = nullptr;

  bool is_p_left_child_of_parent = false;
  bool is_from_left_child = false;
  while (p) {
    Node* parent = p->parent_;

    if (parent) {
      is_p_left_child_of_parent = (parent->left_ == p);
      if (is_p_left_child_of_parent) {
        parent->left_ = nullptr;
      } else {
        parent->right_ = nullptr;
      }
      p->parent_ = nullptr;
    }

    if (!is_from_left_child) {
      a = Merge(p, a);
    } else {
      b = Merge(b, p);
    }

    is_from_left_child = is_p_left_child_of_parent;
    p->Maintain();
    p = parent;
  }

  return {a, b};
}
```

### SplitUp3(u)

Neka je $L$ niz u kojem se nalazi $u$; razdvojimo $L$ na mjestu $u$ na nizove $L^1$, $u$ i $L^2$, pri čemu prvi sadrži elemente $L$ ispred $u$, a drugi preostale elemente.

Dovoljno je malo izmijeniti `SplitUp2`.

### MakeRoot(u)

Lako se dobiva iz `SplitUp2` i `Merge`.

```cpp
void MakeRoot(int u) {
  Node* vertex_u = vertices_[u];
  auto [L1, L2] = Treap::SplitUp2(vertex_u);
  Treap::Merge(L2, L1);
}
```

### Insert(u, v)

Lako se dobiva iz `SplitUp2` i `Merge`.

```cpp
void Insert(int u, int v) {
  Node* vertex_u = vertices_[u];
  Node* vertex_v = vertices_[v];

  Node* edge_uv = AllocateNode(u, v);
  Node* edge_vu = AllocateNode(v, u);
  tree_edges_[u][v] = edge_uv;
  tree_edges_[v][u] = edge_vu;

  auto [L11, L12] = Treap::SplitUp2(vertex_u);
  auto [L21, L22] = Treap::SplitUp2(vertex_v);

  Node* L = L12;
  L = Treap::Merge(L, L11);
  L = Treap::Merge(L, edge_uv);
  L = Treap::Merge(L, L22);
  L = Treap::Merge(L, L21);
  L = Treap::Merge(L, edge_vu);
}
```

### Delete(u, v)

Lako se dobiva iz `SplitUp3` i `Merge`.

```cpp
void Delete(int u, int v) {
  Node* edge_uv = tree_edges_[u][v];
  Node* edge_vu = tree_edges_[v][u];
  tree_edges_[u].erase(v);
  tree_edges_[v].erase(u);

  int position_uv = Treap::GetPosition(edge_uv);
  int position_vu = Treap::GetPosition(edge_vu);
  if (position_uv > position_vu) {
    std::swap(edge_uv, edge_vu);
    std::swap(position_uv, position_vu);
  }

  auto [L1, uv, _] = Treap::SplitUp3(edge_uv);
  auto [L2, vu, L3] = Treap::SplitUp3(edge_vu);
  Treap::Merge(L1, L3);

  FreeNode(edge_uv);
  FreeNode(edge_vu);
}
```

## Održavanje povezanosti

Vrhovi $u$ i $v$ povezani su ako i samo ako pripadaju istom stablu $T$, tj. $(u, u)$ i $(v, v)$ pripadaju $\operatorname{ETR}(T)$; to se može provjeriti tako da se usporedi jesu li korijeni Treapova u kojima se nalaze čvorovi Treapa koji odgovaraju vrhovima $u$ i $v$ isti.

### Primjer [P2147 \[SDOI2008\] 洞穴勘测](https://www.luogu.com.cn/problem/P2147)

Ogledni zadatak za održavanje povezanosti.

??? note "Ogledni kod"
    ```cpp
    --8<-- "docs/ds/code/ett/ett_connectivity.cpp"
    ```

## Održavanje informacija o podstablu

U nastavku kao primjer uzimamo broj vrhova u podstablu.

Svakom elementu $\operatorname{ETR}(T)$ koji odgovara vrhu stabla dodijelimo težinu $1$, a svakom elementu koji odgovara bridu stabla težinu $0$. Sada se broj vrhova stabla $T$ može promatrati kao zbroj težina elemenata u $\operatorname{ETR}(T)$, pa je za održavanje broja vrhova podstabla dovoljno dodatno održavati zbroj težina niza. Održavanje zbroja težina niza klasična je operacija Treapa bez rotacija.

Slično se operacije poput minimuma podstabla mogu pretvoriti u klasične operacije balansiranih stabala kao što je minimum niza i tako održavati.

### Primjer [LOJ #2230. „BJOI2014” 大融合](https://loj.ac/p/2230)

??? note "Ogledni kod"
    ```cpp
    --8<-- "docs/ds/code/ett/ett_subtree_size.cpp"
    ```

## Održavanje informacija o lancima

Može se primijeniti prilično uobičajen trik: pomoću svojstava zagradnog niza informacije o lancu pretvorimo u intervalne informacije, a zatim pomoću strukture podataka koja održava niz održavamo i informacije o lancu. Taj trik, međutim, zahtijeva da održavana informacija bude **oduzimljiva** (invertibilna).

Operacije nad nizom koje odgovaraju prethodno opisanim operacijama dinamičkog stabla mogu desnu zagradu zagradnog niza premjestiti ispred lijeve zagrade, pa pri održavanju informacija poput zbroja težina vrhova na lancu treba dodatno paziti da operacije ne mijenjaju redoslijed odgovarajućih lijevih i desnih zagrada; zbog toga možda treba ponovno promisliti koje operacije nad nizom odgovaraju operacijama dinamičkog stabla, pa čak i koji se DFS niz održava.

Osim toga, ETT-om je vrlo teško održavati izmjene na lancima.

### Primjer [„星际探索”](https://hydro.ac/p/bzoj-P3786)

Jedina operacija dinamičkog stabla u ovom zadatku jest promjena roditelja, što se može promatrati kao brisanje brida i dodavanje brida, ali bi to moglo promijeniti redoslijed odgovarajućih zagrada.

Težine vrhova možemo pretvoriti u težine bridova, održavati zagradni niz stabla, a promjenu roditelja pretvoriti u pomicanje zagradnog niza cijelog podstabla neposredno iza lijeve zagrade roditelja.

??? note "Ogledni kod"
    ```cpp
    --8<-- "docs/ds/code/ett/ett_1.cpp"
    ```

## Literatura

-   Dynamic trees as search trees via euler tours, applied to the network simplex algorithm - Robert E. Tarjan
-   Randomized fully dynamic graph algorithms with polylogarithmic time per operation - Henzinger et al.
