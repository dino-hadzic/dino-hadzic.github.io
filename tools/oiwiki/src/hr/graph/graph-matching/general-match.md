---
title: Najveće sparivanje u općem grafu
---

## Algoritam cvjetova (Blossom Algorithm)

Algoritam cvjetova (Blossom Algorithm, poznat i kao algoritam stabla s cvjetovima) rješava problem najvećeg sparivanja u općem grafu (maximum cardinality matching). Predložio ga je Jack Edmonds 1961. godine.
Uz određene izmjene može riješiti i problem najvećeg težinskog sparivanja u općem grafu.
Ovaj je algoritam prvi dokazao da najveće sparivanje ima polinomnu složenost.

Razlika između sparivanja u općem grafu i sparivanja u bipartitnom grafu (bipartite matching) jest u tome što graf može sadržavati neparne cikluse.

![general-matching-1](./images/general-matching-1.png)

Uzmimo ovaj graf za primjer: ako izravno invertiramo (zamijenimo sparene i nesparene bridove), dobiveni $M$ nije valjan, jer se neki vrhovi pojavljuju u dva sparena brida, a uzrok je upravo neparni ciklus.

Razmotrimo sada algoritam uvećavanja za opće grafove.
Gledano iz perspektive bipartitnog grafa, svaki put uzmemo jedan nespareni vrh, proglasimo ga korijenom i označimo ga **„o”**, a zatim naizmjence označavamo **„o”** i **„i”**; lako se vidi da su bridovi od **„i”** prema **„o”** spareni bridovi.

Neka je trenutni vrh $v$, a susjedni vrh $u$; razlikujemo dva slučaja:

1.  $u$ još nije posjećen: ako je $u$ nespareni vrh, našli smo uvećavajući put; inače tražimo uvećavajući put od partnera vrha $u$.
2.  $u$ je već posjećen: ako nosi oznaku „o”, treba **sažeti cvijet**; inače smo naišli na parni ciklus i preskačemo ga.

Slučaj parnog ciklusa možemo tretirati kao bipartitni graf, pa ga smijemo zanemariti. Nakon **sažimanja cvijeta** nastavljamo tražiti uvećavajući put u novom grafu.

![general-matching-2](./images/general-matching-2.png)

Neka je izvorni graf $G$, a graf nakon **sažimanja cvijeta** $G'$; dovoljno je dokazati:

1.  ako u $G$ postoji uvećavajući put, postoji i u $G'$;
2.  ako u $G'$ postoji uvećavajući put, postoji i u $G$.

![general-matching-3](./images/general-matching-3.png)

Neka je nestablovni brid (onaj koji zatvara ciklus) $(u,v)$ i definirajmo korijen cvijeta $h=LCA(u,v)$.
Neparni ciklus je alternirajući i jedino su dva brida uz $h$ istog tipa – oba su nespareni bridovi.
Tada je stablovni brid koji ulazi u $h$ sigurno spareni brid, a bridovi iz svih ostalih vrhova ciklusa (osim $h$) prema van su nespareni.

Promatranjem vidimo da se iz ciklusa prema van može izaći na dva načina: u smjeru kazaljke na satu ili obrnuto.

![general-matching-4](./images/general-matching-4.png)

Stoga ni **sažimanje cvijeta** ni **nesažimanje** ne utječu na ispravnost.

U implementaciji, nakon što nađemo **cvijet**, ne moramo ga zaista **sažeti**; dovoljno je poljem pamtiti u kojem je cvijetu (s kojim korijenom) svaki vrh.

### Analiza složenosti (Complexity Analysis)

Svako traženje uvećavajućeg puta prolazi sve bridove, a pri nailasku na **cvijet** održava vrhove **cvijeta**: $O(|E|^2)$.

Prolazimo sve nesparene vrhove i za svaki tražimo uvećavajući put, ukupno $O(|V||E|^2)$.

### Referentni kôd

??? note "Referentni kôd"
    ```cpp
    // graph
    template <typename T>
    class graph {
     public:
      struct edge {
        int from;
        int to;
        T cost;
      };
    
      vector<edge> edges;
      vector<vector<int>> g;
      int n;
    
      graph(int _n) : n(_n) { g.resize(n); }
    
      virtual int add(int from, int to, T cost) = 0;
    };
    
    // undirectedgraph
    template <typename T>
    class undirectedgraph : public graph<T> {
     public:
      using graph<T>::edges;
      using graph<T>::g;
      using graph<T>::n;
    
      undirectedgraph(int _n) : graph<T>(_n) {}
    
      int add(int from, int to, T cost = 1) {
        assert(0 <= from && from < n && 0 <= to && to < n);
        int id = (int)edges.size();
        g[from].push_back(id);
        g[to].push_back(id);
        edges.push_back({from, to, cost});
        return id;
      }
    };
    
    // blossom / find_max_unweighted_matching
    template <typename T>
    vector<int> find_max_unweighted_matching(const undirectedgraph<T> &g) {
      std::mt19937 rng(std::random_device{}());
      vector<int> match(g.n, -1);   // sparivanje
      vector<int> aux(g.n, -1);     // vremenska oznaka
      vector<int> label(g.n);       // „o” ili „i”
      vector<int> orig(g.n);        // korijen cvijeta
      vector<int> parent(g.n, -1);  // roditelj
      queue<int> q;
      int aux_time = -1;
    
      auto lca = [&](int v, int u) {
        aux_time++;
        while (true) {
          if (v != -1) {
            if (aux[v] == aux_time) {  // našli smo već posjećen vrh, tj. LCA
              return v;
            }
            aux[v] = aux_time;
            if (match[v] == -1) {
              v = -1;
            } else {
              v = orig[parent[match[v]]];  // nastavljamo od roditelja sparenog vrha
            }
          }
          swap(v, u);
        }
      };  // lca
    
      auto blossom = [&](int v, int u, int a) {
        while (orig[v] != a) {
          parent[v] = u;
          u = match[v];
          if (label[u] == 1) {  // početni vrh označimo „o” i tražimo uvećavajući put
            label[u] = 0;
            q.push(u);
          }
          orig[v] = orig[u] = a;  // sažimanje cvijeta
          v = parent[u];
        }
      };  // blossom
    
      auto augment = [&](int v) {
        while (v != -1) {
          int pv = parent[v];
          int next_v = match[pv];
          match[v] = pv;
          match[pv] = v;
          v = next_v;
        }
      };  // augment
    
      auto bfs = [&](int root) {
        fill(label.begin(), label.end(), -1);
        iota(orig.begin(), orig.end(), 0);
        while (!q.empty()) {
          q.pop();
        }
        q.push(root);
        // početni vrh označimo „o”; ovdje „0” zamjenjuje „o”, a „1” zamjenjuje „i”
        label[root] = 0;
        while (!q.empty()) {
          int v = q.front();
          q.pop();
          for (int id : g.g[v]) {
            auto &e = g.edges[id];
            int u = e.from ^ e.to ^ v;
            if (label[u] == -1) {  // našli smo neposjećen vrh
              label[u] = 1;        // označimo ga „i”
              parent[u] = v;
              if (match[u] == -1) {  // našli smo nespareni vrh
                augment(u);          // uvećavamo duž uvećavajućeg puta
                return true;
              }
              // našli smo spareni vrh; njegovog partnera stavimo u queue i proširimo alternirajuće stablo
              label[match[u]] = 0;
              q.push(match[u]);
              continue;
            } else if (label[u] == 0 && orig[v] != orig[u]) {
              // našli smo posjećen vrh s oznakom „o”, dakle našli smo „cvijet”
              int a = lca(orig[v], orig[u]);
              // nađemo LCA, a zatim sažmemo cvijet
              blossom(u, v, a);
              blossom(v, u, a);
            }
          }
        }
        return false;
      };  // bfs
    
      auto greedy = [&]() {
        vector<int> order(g.n);
        // nasumično promiješamo order
        iota(order.begin(), order.end(), 0);
        shuffle(order.begin(), order.end(), rng);
    
        // sparimo vrhove koje je moguće spariti
        for (int i : order) {
          if (match[i] == -1) {
            for (auto id : g.g[i]) {
              auto &e = g.edges[id];
              int to = e.from ^ e.to ^ i;
              if (match[to] == -1) {
                match[i] = to;
                match[to] = i;
                break;
              }
            }
          }
        }
      };  // greedy
    
      // na početku nasumično sparimo
      greedy();
      // za nesparene vrhove tražimo uvećavajući put
      for (int i = 0; i < g.n; i++) {
        if (match[i] == -1) {
          bfs(i);
        }
      }
      return match;
    }
    ```

??? note "[UOJ #79. 一般图最大匹配](https://uoj.ac/problem/79)"
    ```cpp
    --8<-- "docs/graph/code/graph-matching/general-match/general-match_1.cpp"
    ```

## Algoritam za sparivanje u općem grafu zasnovan na Gaussovoj eliminaciji

???+ tip "Savjet"
    Prije čitanja ovog dijela možda ćete trebati pročitati sadržaj o matricama iz poglavlja „Linearna algebra”:
    
    -   [Matrice](../../math/linear-algebra/matrix.md)
    -   [Determinanta](../../math/linear-algebra/determinant.md)
    -   [Gaussova eliminacija](../../math/numerical/gauss.md)

U ovom dijelu predstavljamo algoritam za sparivanje u općem grafu zasnovan na Gaussovoj eliminaciji. U odnosu na klasični algoritam cvjetova, prednost mu je što ga je lakše razumjeti i napisati, a ujedno olakšava rješavanje problema poput „obveznih vrhova najvećeg sparivanja”; nedostatak mu je velika konstanta, jer se $O(n^3)$ Gaussove eliminacije u pravilu u potpunosti iscrpi, dok algoritam cvjetova obično ne dosegne svoju najgoru složenost.

### Predznanje: Tutteova matrica

**Definicija**: Za neusmjereni graf $G = (V, E)$ s $n$ vrhova, njegova Tutteova matrica $\tilde{A}(G)$ je matrica $n \times n$ u kojoj:

$$
\tilde{A}(G)_{i,j} = \begin{cases}
x_{i,j}, & i<j,\; (v_i, v_j)\in E \\
-x_{i,j}, & i > j,\; (v_i, v_j) \in E \\
0, & \text{otherwise}
\end{cases}
$$

Ovdje je $x_{i, j}$ varijabla, pa $\tilde{A}(G)$ sadrži ukupno $|E|$ varijabli.

Kad nema dvosmislenosti, $\tilde{A}(G)$ ćemo dalje kratko pisati $\tilde{A}$.

**Teorem** (Tutteov teorem): $G$ ima perfektno sparivanje ako i samo ako je $\det \tilde{A} \ne 0$.

??? note "Dokaz"
    Uvedimo pojam „pokrivača parnim ciklusima”: pokrivač parnim ciklusima neusmjerenog grafa $G$ je pokrivanje svih vrhova nekoliko parnih ciklusa (uključujući cikluse duljine dva), bez preklapanja i bez propusta.
    
    Lako se dokazuje da $G$ ima perfektno sparivanje ako i samo ako $G$ ima pokrivač parnim ciklusima.
    
    -   Ako $G$ ima pokrivač parnim ciklusima, dovoljno je u svakom ciklusu uzeti svaki drugi brid i dobivamo perfektno sparivanje.
    -   Ako $G$ ima perfektno sparivanje, dovoljno je uzeti cikluse duljine dva koji odgovaraju sparenim bridovima i dobivamo pokrivač parnim ciklusima.
    
    Zatim dokazujemo da $G$ ima pokrivač parnim ciklusima ako i samo ako je $\tilde{A} \ne 0$.
    
    Promotrimo definiciju determinante
    
    $$
    \det A = \sum_{\pi} (-1)^{\pi} \prod_{i} A_{i, \pi_i}
    $$
    
    gdje je $\pi$ proizvoljna permutacija, a $(-1)^{\pi}$ je $-1$ ako $\pi$ ima neparan broj inverzija, a inače $1$.
    
    Lako se vidi da se svaka permutacija može shvatiti kao pokrivač grafa $G$ ciklusima. Ako taj pokrivač sadrži neparni ciklus, zbroj s pokrivačem u kojem je taj ciklus okrenut nužno je $0$; dakle samo pokrivači parnim ciklusima mogu determinantu učiniti različitom od $0$. Time je dokaz završen.

**Teorem**: $\operatorname{rank}\tilde{A}$ je uvijek paran, a veličina najvećeg sparivanja grafa $G$ jednaka je polovini $\operatorname{rank}\tilde{A}$.

??? note "Dokaz"
    Rang antisimetrične matrice može biti samo paran; drugi dio ostavljamo čitatelju za razmišljanje.

U praksi je nemoguće računati s $|E|$ varijabli, ali možemo odabrati neko polje, npr. sustav ostataka $\mathcal{Z}_p$ po nekom prostom broju $p$, varijable nasumično zamijeniti brojevima iz $\mathcal{Z}_p$ i zatim računati. Radi jednostavnosti, kad nema dvosmislenosti, $\tilde{A}$ dalje označava matricu nakon zamjene.

**Teorem**: $\operatorname{rank}\tilde{A}$ je najviše dvostruka veličina najvećeg sparivanja grafa $G$, a vjerojatnost da su jednaki je barem $1 - \frac n p$.

Budući da $n$ u problemima najvećeg sparivanja u općem grafu u pravilu ne prelazi $10^3$, u praksi je dovoljno za $p$ uzeti prost broj reda veličine $10^9$.

Iz teorema slijedi: ako trebamo samo veličinu najvećeg sparivanja, a ne i samo sparivanje, dovoljno je jednom Gaussovom eliminacijom izračunati $\operatorname{rank}\tilde{A}$, što je znatno jednostavnije od algoritma cvjetova. Ako pak treba ispisati sparivanje, stvar je malo složenija i treba algoritam opisan u nastavku.

### Konstrukcija perfektnog sparivanja

Iz Tutteova teorema i gornjeg teorema slijedi: ako $G$ ima perfektno sparivanje, $\tilde{A}$ je s velikom vjerojatnošću punog ranga. Radi jednostavnosti u nastavku izostavljamo „s velikom vjerojatnošću”.

Označimo vrh grafa $G$ s oznakom $i$ kao $v_i$; tada vrijedi sljedeći teorem:

**Teorem**: $\tilde{A}^{-1}_{j,i} \ne 0 \iff G - \{v_i, v_j\}$ ima perfektno sparivanje.

???+ tip "Inverzna i adjungirana matrica"
    Za proizvoljnu kvadratnu matricu $A$ reda $n$ njezina adjungirana matrica definirana je s $A^*_{i, j} = (-1)^{i + j} M_{j, i}$, gdje je $M_{j, i}$ minora dobivena brisanjem $j$-tog retka i $i$-tog stupca. Drugim riječima, ako je $M$ matrica algebarskih komplemenata matrice $A$, tada je $A^* = M^T$.
    
    **Teorem**: Ako je $A$ invertibilna, tada je $A^{-1} = \frac 1 {\det A} A^*$.
    
    Dakle ovdje $A^{-1}_{j, i} \ne 0 \iff M_{i, j} \ne 0$, tj. dio matrice $A$ koji ostaje nakon brisanja $i$-tog retka i $j$-tog stupca ima puni rang.

Drugim riječima, ako je $(v_i, v_j) \in E$ i $\tilde{A}^{-1}_{j, i} \ne 0$, postoji perfektno sparivanje koje sadrži brid $(v_i, v_j)$. Takve bridove u nastavku zovemo **dopustivim bridovima**.

Iz gornjeg teorema za neusmjereni graf $G$ s perfektnim sparivanjem dobivamo prilično očit grubi algoritam za nalaženje perfektnog sparivanja: svaki put prođemo sve $i, j$, i ako je $(v_i, v_j)$ dopustiv brid (brid postoji i $\tilde{A}^{-1}_{j, i} \ne 0$), dodamo $(v_i, v_j)$ u sparivanje, izbrišemo oba vrha iz $G$ i ponovno izračunamo novu $\tilde{A}^{-1}$.

Ukupno treba $\frac n 2$ krugova, svaki je $O(n^3)$, pa je ukupna složenost $O(n ^ 4)$, što je pomalo sporo. Zapravo, pri ponovnom računanju $\tilde{A}^{-1}$ ne moramo svaki put iznova Gaussovom eliminacijom računati inverz, nego možemo iskoristiti sljedeći teorem:

**Teorem** (teorem o eliminaciji): Neka je

$$
A = \begin{bmatrix}
  a_{1, 1} & v^T \\
  u & B
\end{bmatrix} \quad A^{-1} = \begin{bmatrix}
  \hat a^{1, 1} & \hat v^T \\
  \hat u & \hat B
\end{bmatrix}
$$

i $\hat a_{1, 1} \ne 0$; tada je

$$
B^{-1} = \hat B - \frac {\hat u \hat v^T} {\hat a_{1, 1}}
$$

Teorem opisuje eliminaciju prvog retka i prvog stupca. Zapravo se vrlo očito poopćuje na eliminaciju proizvoljnog retka i stupca, pa je dovoljno na samom početku algoritma jednom izračunati $\tilde{A}^{-1}$, a zatim pri svakom brisanju dvaju vrhova izvesti samo dva postupka eliminacije složenosti $O(n^2)$.

??? note "Opis je pomalo apstraktan; pogledajte C++ kôd"
    ```cpp
    void eliminate(int A[][MAXN], int r, int c) {  // eliminiraj r-ti redak i c-ti stupac
      row_marked[r] = col_marked[c] = true;        // već eliminirano
    
      int inv = quick_power(A[r][c], p - 2);  // inverz
    
      for (int i = 1; i <= n; i++)
        if (!row_marked[i] && A[i][c]) {
          int tmp = (long long)A[i][c] * inv % p;
    
          for (int j = 1; j <= n; j++)
            if (!col_marked[j] && A[r][j])
              A[i][j] = (A[i][j] - (long long)tmp * A[r][j]) % p;
        }
    }
    ```

Ukupno treba $\frac n 2$ krugova, svaki složenosti $O(n^2)$, pa gornji algoritam nalazi perfektno sparivanje u vremenu $O(n^3)$.

### Konstrukcija najvećeg sparivanja

Upravo smo riješili problem konstrukcije perfektnog sparivanja, ali u zadacima obično treba najveće sparivanje.

Već smo spomenuli da je veličina najvećeg sparivanja grafa $G$ jednaka polovini $\operatorname{rank}\tilde{A}$. Ako nađemo najveću kvadratnu podmatricu punog ranga matrice $\tilde{A}$, dovoljno je naći perfektno sparivanje induciranog podgrafa koji odgovara toj podmatrici i dobivamo najveće sparivanje grafa $G$.

Gledano iz drugog kuta: ako $G$ ima perfektno sparivanje, $\tilde{A}$ je punog ranga, odnosno $\tilde{A}$ je linearno nezavisna. Ako $\tilde{A}$ nije punog ranga, možemo odrediti linearnu bazu matrice $\tilde{A}$ i zadržati samo retke i stupce koji joj odgovaraju; tako dobivamo najveću kvadratnu podmatricu punog ranga matrice $\tilde{A}$.

Nakon što nađemo najveću kvadratnu podmatricu punog ranga, gornjim algoritmom nađemo perfektno sparivanje induciranog podgrafa i dobivamo najveće sparivanje izvornog grafa. Pazite: budući da Gaussova eliminacija može zamjenjivati retke, u implementaciji treba pažljivo održavati oznake vrhova.

??? note "[UOJ #79. 一般图最大匹配](https://uoj.ac/problem/79)"
    ```cpp
    --8<-- "docs/graph/code/graph-matching/general-match/general-match_2.cpp"
    ```

## Zadaci

-   [UOJ #79. 一般图最大匹配](https://uoj.ac/problem/79)
-   [UOJ#171.【WC2016】挑战 NPC](https://uoj.ac/problem/171)

## Literatura

1.  Mucha M, Sankowski P.[Maximum matchings via Gaussian elimination](http://web.eecs.umich.edu/~pettie/matching/Mucha-Sankowski-maximum-matching-matrix-multiplication.pdf)
2.  周子鑫，杨家齐 (Zhou Zixin, Yang Jiaqi), „基于线性代数的一般图匹配” (Sparivanje u općem grafu zasnovano na linearnoj algebri)
3.  ZYQN [„基于线性代数的一般图匹配算法” (Algoritam za sparivanje u općem grafu zasnovan na linearnoj algebri)](https://oi.cyo.ng/wp-content/uploads/2017/02/maximum_matchings_via_gaussian_elimination.pdf)
