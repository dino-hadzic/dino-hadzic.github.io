---
title: Topološko sortiranje
---

## Definicija

Topološko sortiranje (topological sorting) rješava problem kako poredati sve vrhove usmjerenog acikličkog grafa.

Postupak možemo opisati primjerom sastavljanja rasporeda kolegija po semestrima na fakultetu. Recimo da među kolegijima imamo: „Programiranje”, „Algoritamski jezici”, „Viša matematika”, „Diskretna matematika”, „Prevođenje programa”, „Opća fizika”, „Strukture podataka”, „Baze podataka” itd. Prema primjeru, kad želimo učiti „Strukture podataka”, najprije moramo položiti „Diskretnu matematiku”; nakon tog kolegija stekli smo preduvjet za „Prevođenje programa”. Naravno, „Prevođenje programa” ima i raniji preduvjet, „Algoritamske jezike”. Ti su kolegiji poput vrhova $u$, a usmjereni bridovi $(u,v)$ među njima poput redoslijeda učenja kolegija. Kad studentska služba rasporedi te kolegije tako da raspored poštuje logičke ovisnosti, to je upravo postupak topološkog sortiranja.

![topo](images/topo-example-1.svg)

No što ako jednog dana nastavnik koji slaže raspored zadrijema i kaže da za „Strukture podataka” treba prvo položiti „Operacijske sustave”, a preduvjet za „Operacijske sustave” su opet „Strukture podataka”: što onda učiti prvo (ne razmatramo istodobno učenje)? Između „Struktura podataka” i „Operacijskih sustava” pojavio se ciklus; studenti očito ne mogu odrediti što trebaju učiti prvo, pa topološko sortiranje nije moguće. Ako u usmjerenom grafu postoji ciklus, ne možemo ga topološki sortirati.

Stoga možemo reći: u [DAG-u (usmjerenom acikličkom grafu)](./dag.md) vrhove poredamo linearno tako da za svaki usmjereni brid $(u,v)$ od vrha $u$ do $v$ vrh $u$ dolazi prije $v$.

Također, za zadani DAG, ako postoji brid od $i$ do $j$, kažemo da $j$ ovisi o $i$. Ako postoji put od $i$ do $j$ ($j$ je dostižan iz $i$), kažemo da $j$ neizravno ovisi o $i$.

Cilj topološkog sortiranja jest poredati sve vrhove tako da vrhovi koji dolaze ranije ne ovise o vrhovima koji dolaze kasnije.

## AOV mreža

U svakodnevnom životu veliki projekt možemo promatrati kao skup nekoliko potprojekata među kojima nužno postoji određeni redoslijed: neki potprojekti mogu početi tek nakon što se drugi dovrše.

Redoslijed među potprojektima prikazujemo usmjerenim grafom; odnosi prethođenja među potprojektima usmjereni su bridovi. Takav usmjereni graf naziva se mreža aktivnosti na vrhovima, tj. **AOV mreža (Activity On Vertex Network)**. AOV mreža nužno je usmjereni aciklički graf, tj. nema ciklusa. Za razliku od DAG-a, aktivnosti AOV mreže predstavljene su na vrhovima. (Slika gore primjer je AOV mreže.)

U AOV mreži vrhovi predstavljaju aktivnosti, a lukovi odnose prioriteta među aktivnostima. U AOV mreži ne smije biti ciklusa; tada možemo naći niz vrhova u kojem su prethodne aktivnosti svake aktivnosti poredane ispred njezina vrha. Takav niz naziva se topološki niz (topološki niz AOV mreže nije jedinstven), a postupak konstrukcije topološkog niza iz AOV mreže naziva se topološko sortiranje. Stoga se topološko sortiranje može objasniti i kao poredak svih aktivnosti AOV mreže u niz tako da su prethodne aktivnosti svake aktivnosti poredane ispred nje (topološko sortiranje AOV mreže također nije jedinstveno).

-   Prethodna aktivnost: aktivnost na početku usmjerenog brida naziva se prethodnom aktivnošću aktivnosti na kraju (aktivnost se može izvesti tek kad su sve njezine prethodne aktivnosti dovršene).

-   Sljedeća aktivnost: aktivnost na kraju usmjerenog brida naziva se sljedećom aktivnošću aktivnosti na početku.

Postojanje ciklusa u AOV mreži provjeravamo konstrukcijom topološkog niza: gledamo sadrži li sve vrhove.

### Koraci konstrukcije topološkog niza

1.  Iz grafa odaberemo vrh ulaznog stupnja nula.
2.  Ispišemo taj vrh i iz grafa izbrišemo njega i sve njegove izlazne bridove.

Ponavljamo ta dva koraka dok ne ispišemo sve vrhove (topološko sortiranje je dovršeno) ili dok u grafu ne ostane vrh ulaznog stupnja nula; u tom slučaju graf ima ciklus, topološko sortiranje se ne može dovršiti i zapadamo u zastoj (deadlock).

## Kritični put i AOE mreža

AOV mreži odgovara **AOE mreža (Activity On Edge Network)**, tj. mreža u kojoj bridovi predstavljaju aktivnosti. AOE mreža je težinski usmjereni aciklički graf u kojem vrhovi predstavljaju događaje, a lukovi trajanje aktivnosti. AOE mreža obično služi za procjenu vremena dovršetka projekta. AOE mreža mora biti aciklička, imati jedinstveni početni vrh ulaznog stupnja nula (izvor) i jedinstveni završni vrh izlaznog stupnja nula (ponor).

![topo](images/topo-example-2.svg)

Neke aktivnosti u AOE mreži mogu se izvoditi paralelno, pa je najkraće vrijeme dovršetka cijelog projekta duljina najduljeg puta aktivnosti od početnog do završnog vrha (duljina puta ovdje znači zbroj trajanja aktivnosti na putu, tj. zbroj težina lukova, a ne broj lukova na putu). Budući da projekt zahtijeva dovršetak svih aktivnosti, najdulji put aktivnosti ujedno je kritični put i određuje ukupno vrijeme dovršetka projekta.

### Osnovni pojmovi AOE mreže

-   Aktivnost: u AOE mreži luk predstavlja aktivnost. Težina luka predstavlja trajanje aktivnosti; aktivnost počinje nakon što se pokrene njezin prethodni događaj (početak luka).

-   Događaj: u AOE mreži vrh predstavlja događaj; događaj se pokreće kad su dovršene sve njegove prethodne aktivnosti (lukovi koji ulaze u taj vrh).

-   Najranije vrijeme događaja (vrha) $v_i$: najranije moguće vrijeme nastupa tog događaja, označeno $ve(i)$; određuje najranije vrijeme početka aktivnosti koje počinju u tom vrhu; očito je najranije vrijeme izvora 0. Budući da događaj zahtijeva dovršetak svih prethodnih aktivnosti, jednako je maksimumu duljina putova od početnog vrha do tog vrha, rekurzivno: $ve(i) = \max\{ve(j) + val^j_i ~\vert~ j \in pre_i\}$, gdje je $val^j_i$ težina brida od j do i (tj. trajanje aktivnosti od j do i), a $pre_i$ skup svih prethodnih događaja od i.

-   Najkasnije vrijeme događaja (vrha) $v_i$: najkasnije vrijeme nastupa tog događaja koje ne odgađa cijeli projekt, označeno $vl(i)$; određuje najkasnije vrijeme početka svih aktivnosti koje završavaju u tom stanju; jednako je minimumu najkasnijih vremena početka svih sljedećih aktivnosti događaja, tj. $vl(i) = \min\{vl(j) - val^i_j ~\vert~ j \in nxt_i\}$, gdje je $val^i_j$ težina brida od i do j (tj. trajanje aktivnosti od i do j), a $nxt_i$ skup svih sljedećih događaja od i.

-   Najranije vrijeme početka aktivnosti (luka) $(u, v)$: najranije moguće vrijeme početka te aktivnosti, označeno $e(u,v)$; očito je jednako najranijem vremenu njezina prethodnog događaja, tj. $e(u,v)=ve(u)$.

-   Najkasnije vrijeme početka aktivnosti (luka) $(u, v)$: najkasnije vrijeme početka aktivnosti koje ne odgađa cijeli projekt, označeno $l(u,v)$; jednako je najkasnijem vremenu sljedećeg događaja minus trajanje aktivnosti (težina), tj. $l(u,v)=vl(v)-val^u_v$, gdje je $val^u_v$ težina brida od u do v (tj. trajanje aktivnosti od u do v).

-   Kritični put: duljina najduljeg puta od izvora do ponora u AOE mreži.

-   Kritična aktivnost: aktivnost na kritičnom putu; njezino najranije i najkasnije vrijeme početka su jednaki.

### Rekurzivno računanje najranijih i najkasnijih vremena

Računamo u topološkom poretku: najranija vremena rekurzivno od početka prema kraju, najkasnija vremena od kraja prema početku, prema formulama iz odjeljka **Osnovni pojmovi AOE mreže**.

## Kahnov algoritam

### Postupak

U početnom stanju skup $S$ sadrži sve vrhove ulaznog stupnja $0$, a $L$ je prazna lista.

Svaki put iz $S$ uzmemo vrh $u$ (bilo koji) i stavimo ga u $L$, zatim izbrišemo sve bridove $(u, v_1), (u, v_2), (u, v_3) \cdots$ iz $u$. Ako brisanjem brida $(u, v)$ ulazni stupanj vrha $v$ postane $0$, stavimo $v$ u $S$.

Ponavljamo postupak dok skup $S$ ne postane prazan. Provjerimo ima li u grafu još bridova: ako ima, graf sigurno ima ciklus; inače vraćamo $L$, a redoslijed vrhova u $L$ rezultat je konstrukcije topološkog niza.

Pogledajmo najprije pseudokod s [Wikipedije](https://en.wikipedia.org/wiki/Topological_sorting#Kahn's_algorithm)

???+ note "Implementacija"
    ```text
    L ← Empty list that will contain the sorted elements
    S ← Set of all nodes with no incoming edges
    while S is not empty do
        remove a node n from S
        insert n into L
        for each node m with an edge e from n to m do
            remove edge e from the graph
            if m has no other incoming edges then
                insert m into S
    if graph has edges then
        return error (graph has at least one cycle)
    else
        return L (a topologically sorted order)
    ```

Srž koda je održavanje skupa vrhova ulaznog stupnja 0.

Za ilustraciju pogledajte sliku

![topo](images/topo-example.svg)

Rezultat sortiranja je: 2 -> 8 -> 0 -> 3 -> 7 -> 1 -> 5 -> 6 -> 9 -> 4 -> 11 -> 10 -> 12

### Vremenska složenost

Za graf $G = (V, E)$ već pri inicijalizaciji skupa $S$ vrhova ulaznog stupnja $0$ moramo obići cijeli graf i provjeriti svaki brid, što je složenost $O(E+V)$. Zatim obrađujemo taj skup, što očito također zahtijeva $O(E+V)$ vremena.

Ukupna je vremenska složenost stoga $O(E+V)$

### Implementacija

=== "C++"
    ```cpp
    int n, m;
    vector<int> G[MAXN];
    int in[MAXN];  // ulazni stupanj svakog vrha
    
    bool toposort() {
      vector<int> L;
      queue<int> S;
      for (int i = 1; i <= n; i++)
        if (in[i] == 0) S.push(i);
      while (!S.empty()) {
        int u = S.front();
        S.pop();
        L.push_back(u);
        for (auto v : G[u]) {
          if (--in[v] == 0) {
            S.push(v);
          }
        }
      }
      if (L.size() == n) {
        for (auto i : L) cout << i << ' ';
        return true;
      }
      return false;
    }
    ```

=== "Python"
    ```python
    from collections import defaultdict, deque
    
    
    def topo_sort(graph):
        lst = []
        in_degree = defaultdict(int)
        for u in graph:
            for v in graph[u]:
                in_degree[v] += 1
    
        s = deque([u for u in graph if in_degree[u] == 0])
        while s:
            u = s.popleft()
            lst.append(u)
            for v in graph.get(u, []):
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    s.append(v)
    
        return None if any(in_degree.values()) else lst
    ```

## DFS algoritam

### Implementacija

=== "C++"
    ```cpp
    using Graph = vector<vector<int>>;  // lista susjedstva
    
    struct TopoSort {
      enum class Status : uint8_t { to_visit, visiting, visited };
    
      const Graph& graph;
      const int n;
      vector<Status> status;
      vector<int> order;
      vector<int>::reverse_iterator it;
    
      TopoSort(const Graph& graph)
          : graph(graph),
            n(graph.size()),
            status(n, Status::to_visit),
            order(n),
            it(order.rbegin()) {}
    
      bool sort() {
        for (int i = 0; i < n; ++i) {
          if (status[i] == Status::to_visit && !dfs(i)) return false;
        }
        return true;
      }
    
      bool dfs(const int u) {
        status[u] = Status::visiting;
        for (const int v : graph[u]) {
          if (status[v] == Status::visiting) return false;
          if (status[v] == Status::to_visit && !dfs(v)) return false;
        }
        status[u] = Status::visited;
        *it++ = u;
        return true;
      }
    };
    ```

=== "Python"
    ```python
    from enum import Enum, auto
    
    
    class Status(Enum):
        to_visit = auto()
        visiting = auto()
        visited = auto()
    
    
    def topo_sort(graph: list[list[int]]) -> list[int] | None:
        n = len(graph)
        status = [Status.to_visit] * n
        order = []
    
        def dfs(u: int) -> bool:
            status[u] = Status.visiting
            for v in graph[u]:
                if status[v] == Status.visiting:
                    return False
                if status[v] == Status.to_visit and not dfs(v):
                    return False
            status[u] = Status.visited
            order.append(u)
            return True
    
        for i in range(n):
            if status[i] == Status.to_visit and not dfs(i):
                return None
    
        return order[::-1]
    ```

Vremenska složenost: $O(E+V)$, prostorna složenost: $O(V)$

### Dokaz ispravnosti

Promotrimo graf: ako nakon brisanja nekog vrha ulaznog stupnja $0$ novi graf ima topološki poredak, onda ga sigurno ima i izvorni graf. Obratno, ako izvorni graf ima topološki poredak, ima ga i graf nakon brisanja.

### Primjene

Topološkim sortiranjem možemo provjeriti ima li graf ciklus, a i je li graf lanac. Topološko sortiranje služi i za nalaženje kritičnog puta u AOE mreži, tj. procjenu najkraćeg vremena dovršetka projekta.

### Leksikografski najveći/najmanji topološki poredak

Dovoljno je red u Kahnovu algoritmu zamijeniti prioritetnim redom implementiranim max-heapom/min-heapom; ukupna je vremenska složenost tada $O(E+V \log{V})$.

## Zadaci

[CF 1385E](https://codeforces.com/problemset/problem/1385/E): konstrukcija pomoću topološkog sortiranja.

[Luogu P1347](https://www.luogu.com.cn/problem/P1347): zadatak-predložak za topološko sortiranje.

## Literatura

1.  Discrete Mathematics and Its Applications (kinesko izdanje). ISBN:9787111555391
2.  [Topological sorting - Wikipedia](https://en.wikipedia.org/wiki/Topological_sorting)
3.  [数据结构第九讲（图：拓扑排序，关键路径，最短路径）- Zhihu](https://zhuanlan.zhihu.com/p/164751109) (Strukture podataka, 9. predavanje: grafovi – topološko sortiranje, kritični put, najkraći put)
