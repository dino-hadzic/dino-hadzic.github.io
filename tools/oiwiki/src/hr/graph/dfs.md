---
title: DFS (teorija grafova)
---

## Uvod

DFS je kratica za [Depth First Search](https://en.wikipedia.org/wiki/Depth-first_search), hrvatski pretraživanje u dubinu; to je algoritam za obilazak ili pretraživanje stabla ili grafa. „U dubinu” znači da u svakom koraku pokušavamo ići prema dubljem vrhu.

Pri objašnjavanju se ovaj algoritam često stavlja uz bok BFS-u, ali osim što oba mogu obići komponente povezanosti grafa, njihove su namjene potpuno različite i rijetko se kada mogu međusobno zamijeniti.

Pojam DFS često se koristi za pretragu implementiranu rekurzivnom funkcijom, no to zapravo nije isto. O toj vrsti pretrage pogledajte [DFS (pretraživanje)](../search/dfs.md).

## Postupak

Najuočljivija značajka DFS-a jest to da **rekurzivno poziva samog sebe**. Ujedno, slično BFS-u, DFS označava vrhove koje je posjetio i pri obilasku grafa preskače već označene vrhove kako bi osigurao da se **svaki vrh posjeti točno jednom**. Funkcija koja zadovoljava ta dva pravila jest DFS u širem smislu.

Konkretno, DFS ima otprilike ovakvu strukturu:

    DFS(v) // v može biti vrh grafa, ali i apstraktan pojam, npr. stanje DP-a i sl.
      označi v kao posjećen
      for u in susjedi od v
        if u nije označen kao posjećen then
          DFS(u)
        end
      end
    end

Gornji kôd sadrži samo osnovnu strukturu nužnu za DFS. Stvarni DFS na tu osnovu dodaje još koda koji iskorištava svojstva DFS-a za druge operacije.

## Svojstva

Vremenska složenost algoritma obično je $O(n+m)$, a prostorna $O(n)$, gdje je $n$ broj vrhova, a $m$ broj bridova. Napomena: prostorna složenost uključuje i prostor na stogu, čija je prostorna složenost $O(n)$. Ta se vremenska složenost postiže samo ako se jedan brid u prosjeku obilazi u $O(1)$, npr. ako je graf pohranjen forward star zapisom ili listom susjedstva; s matricom susjedstva ta složenost nije nužno dostižna.

> Napomena: većina današnjih natjecanja (uključujući NOIP, većinu pokrajinskih izbornih natjecanja i natjecanja koja organizira CCF) podržava **neograničen prostor na stogu**, tj. stog se ne ograničava zasebno, ali ukupna memorija i dalje podliježe ograničenju iz teksta zadatka. Međutim, većina operacijskih sustava dodatno ograničava veličinu stoga, pa je pri lokalnom ispitivanju potrebno to ograničenje ukloniti.
>
> -   Na Windowsima se to obično čini dodavanjem `-Wl,--stack=1000000000` u **opcije prevođenja**, čime se ograničenje stoga postavlja na 1000000000 bajtova.
> -   Na Linuxu se obično prije pokretanja programa **u terminalu** izvrši `ulimit -s unlimited`, što znači neograničen stog. Dovoljno je to učiniti jednom po terminalu i vrijedi za sva kasnija pokretanja programa.

## Implementacija

### Implementacija stogom

DFS se može implementirati tako da se [stog (stack)](../ds/stack.md) koristi kao privremeni spremnik vrhova tijekom obilaska; to je u izravnoj analogiji s BFS-om implementiranim [redom (queue)](../ds/queue.md).

=== "C++"
    ```cpp
    vector<vector<int>> adj;  // lista susjedstva
    vector<bool> vis;         // bilježi je li vrh već obiđen
    
    void dfs(int s) {
      stack<int> st;
      st.push(s);
      vis[s] = true;
    
      while (!st.empty()) {
        int u = st.top();
        st.pop();
    
        for (int v : adj[u]) {
          if (!vis[v]) {
            vis[v] = true;  // osigurava da na stogu nema duplikata
            st.push(v);
          }
        }
      }
    }
    ```

=== "Python"
    ```python
    # adj : List[List[int]] lista susjedstva
    # vis : List[bool] bilježi je li vrh već obiđen
    
    
    def dfs(s: int) -> None:
        stack = [s]  # listom simuliramo stog, početni vrh stavljamo na stog
        vis[s] = True  # početni vrh je obiđen
    
        while stack:  # nastavljamo dok stog nije prazan
            u = (
                stack.pop()
            )  # uzmi i ukloni posljednji element (vrh stoga); to možemo shvatiti kao dolazak u u
    
            for v in adj[u]:  # za svaki element v susjedan vrhu u
                if not vis[v]:  # ako v prije nije posjećen
                    vis[v] = True  # osigurava da na stogu nema duplikata
                    stack.append(v)  # stavi v na stog
    ```

### Rekurzivna implementacija

Izvršavanje funkcija pri rekurzivnim pozivima slijedi redoslijed dodavanja i uklanjanja elemenata sa stoga, pa se virtualni adresni prostor koji zauzimaju pozivi funkcija naziva stog poziva (call stack); DFS se stoga može implementirati rekurzivno.

S [listom susjedstva (adjacency list)](./save.md#邻接表) kao načinom pohrane grafa:

=== "C++"
    ```cpp
    vector<vector<int>> adj;  // lista susjedstva
    vector<bool> vis;         // bilježi je li vrh već obiđen
    
    void dfs(const int u) {
      vis[u] = true;
      for (int v : adj[u])
        if (!vis[v]) dfs(v)
    }
    ```

=== "Python"
    ```python
    # adj : List[List[int]] lista susjedstva
    # vis : List[bool] bilježi je li vrh već obiđen
    
    
    def dfs(u: int) -> None:
        vis[u] = True
        for v in adj[u]:
            if not vis[v]:
                dfs(v)
    ```

Na primjeru [ulančanog forward star zapisa](./save.md#链式前向星):

=== "C++"
    ```cpp
    void dfs(int u) {
      vis[u] = 1;
      for (int i = head[u]; i; i = e[i].x) {
        if (!vis[e[i].t]) {
          dfs(v);
        }
      }
    }
    ```

=== "Java"
    ```Java
    public void dfs(int u) {
        vis[u] = true;
        for (int i = head[u]; i != 0; i = e[i].x) {
            if (!vis[e[i].t]) {
                dfs(v);
            }
        }
    }
    ```

=== "Python"
    ```python
    def dfs(u):
        vis[u] = True
        i = head[u]
        while i:
            if vis[e[i].t] == False:
                dfs(v)
            i = e[i].x
    ```

### DFS poredak

DFS poredak (DFS order) niz je indeksa vrhova u redoslijedu kojim ih DFS posjećuje.

Uočavamo da svako podstablo odgovara neprekinutom odsječku (intervalu) DFS poretka.

### Zagradni niz

Kada DFS uđe u neki vrh, zapišemo lijevu zagradu `(`, a kada iz vrha izađe, zapišemo desnu zagradu `)`.

Svaki se vrh pojavljuje dvaput. Dubine dvaju susjednih vrhova razlikuju se za 1.

### DFS na općem grafu

Na nepovezanom grafu može se posjetiti samo komponenta povezanosti u kojoj je početni vrh.

Na povezanom grafu DFS poredak u pravilu nije jedinstven.

Napomena: ni DFS poredak stabla nije jedinstven.

Ako tijekom DFS-a za svaki vrh zabilježimo iz kojeg smo vrha u njega došli, dobivamo strukturu stabla koja se zove DFS stablo. DFS stablo je razapinjuće stablo polaznog grafa.

[DFS stablo](./scc.md#dfs-生成树) ima mnoga svojstva; primjerice, pomoću njega se mogu naći [jako povezane komponente](./scc.md).
