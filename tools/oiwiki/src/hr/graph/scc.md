---
title: Jako povezane komponente
---

## Uvod

Prije čitanja obvezno se upoznajte s osnovnim dijelom [Osnovnih pojmova teorije grafova](./concept.md).

Definicija jake povezanosti: usmjeren graf G jako je povezan ako su svaka dva vrha grafa G međusobno dostižna.

Definicija jako povezane komponente (Strongly Connected Component, SCC): maksimalan jako povezan podgraf.

Ovdje opisujemo kako naći jako povezane komponente.

## Tarjanov algoritam

### Uvod

Robert E. Tarjan (1948.–), rođen u Pomoni u Kaliforniji (SAD), računalni je znanstvenik.

Tarjan je izumio mnoge algoritme i strukture podataka. Mnogi od njih nose njegovo ime, pa se različiti algoritmi katkad brkaju: npr. Tarjanov algoritam za razne vrste povezanih komponenata i Tarjanov algoritam za LCA (Lowest Common Ancestor, najniži zajednički predak). Tarjan je izumio i DSU (union-find), splay stablo i top tree.

Ovdje opisujemo Tarjanov algoritam za traženje jako povezanih komponenata u usmjerenom grafu.

### DFS razapinjuće stablo

Prije opisa algoritma upoznajmo **DFS razapinjuće stablo** na primjeru sljedećeg usmjerenog grafa:

![DFS razapinjuće stablo](./images/dfs-tree.svg)

Kad na usmjerenom grafu $G$ pokrenemo DFS, zbog usmjerenosti bridova iz jednog vrha možda nećemo moći posjetiti sve vrhove grafa. Zato moramo proći cijeli skup vrhova: za svaki još neposjećeni vrh pokrećemo novi DFS. Stablasti bridovi (vidi dolje) kroz koje prolazi svaki pojedini DFS pokrenut iz nekog početnog vrha tvore stablo koje zovemo **DFS razapinjuće stablo**. Kad su svi vrhovi posjećeni, sva dobivena DFS razapinjuća stabla zajedno tvore **DFS razapinjuću šumu** usmjerenog grafa.

Napomena: konkretan oblik razapinjućeg stabla (i šume), kao i klasifikacija bridova u nastavku, ovise o izboru početnog vrha DFS-a i o redoslijedu obilaska susjeda.

Bridovi usmjerenog grafa $G$ dijele se u četiri vrste:

1.  Stablasti bridovi (tree edge): na slici crni; stablasti brid nastaje svaki put kad pretraga nađe još neposjećen vrh. Svi susjedni stablasti bridovi tvore DFS razapinjuće stablo.
2.  Povratni bridovi (back edge): na slici crveni (tj. $7 \rightarrow 1$); nestablasti brid koji tijekom pretrage vodi iz nekog vrha u njegova pretka.
3.  Prednji bridovi (forward edge): na slici zeleni (tj. $3 \rightarrow 6$); nestablasti brid koji tijekom pretrage vodi iz nekog vrha u njegova potomka u podstablu.
4.  Poprečni bridovi (cross edge): na slici plavi (tj. $9 \rightarrow 7$); brid koji tijekom pretrage vodi iz nekog vrha u već posjećen vrh koji mu nije ni predak ni potomak, tj. brid koji ne pripada nijednoj od triju prethodnih vrsta.

Razmotrimo odnos DFS razapinjućeg stabla i jako povezanih komponenata.

Ako je vrh $u$ prvi vrh neke jako povezane komponente na koji smo naišli u stablu pretrage, onda su ostali vrhovi te komponente sigurno u podstablu s korijenom $u$. Vrh $u$ zove se korijen te jako povezane komponente.

Dokaz kontradikcijom: pretpostavimo da postoji vrh $v$ u toj jako povezanoj komponenti koji nije u podstablu s korijenom $u$. Tada na putu od $u$ do $v$ sigurno postoji brid koji napušta podstablo. No takav brid može biti samo poprečni ili povratni, a oba zahtijevaju da je vrh u koji vode već posjećen, što je u suprotnosti s time da $v$ nije u podstablu s korijenom $u$. Time je dokaz završen.

### Tarjanov algoritam za jako povezane komponente

Tarjanov algoritam temelji se na [pretraživanju u dubinu](./dfs.md) grafa. Svaku povezanu komponentu promatramo kao podstablo stabla pretrage; tijekom pretrage održavamo stog, na njega stavljamo još neobrađene vrhove stabla pretrage, a s njega skidamo vrhove za koje je odgovor utvrđen.

U Tarjanovu algoritmu za svaki vrh $u$ održavamo sljedeće varijable:

1.  $\textit{dfn}_u$: redni broj kojim je vrh $u$ posjećen tijekom pretraživanja u dubinu.
2.  $\textit{low}_u$: najraniji vrh koji je još na stogu, a do kojeg se može vratiti iz podstabla vrha $u$. Neka je $\textit{Subtree}_u$ podstablo stabla pretrage s korijenom $u$. $\textit{low}_u$ definira se kao najmanji $\textit{dfn}$ sljedećih vrhova: vrhova na stogu do kojih se iz $\textit{Subtree}_u$ može doći jednim bridom koji nije u stablu pretrage.

Vrijednosti dfn svih vrhova u podstablu nekog vrha veće su od dfn tog vrha.

Na putu od korijena dfn strogo raste, a low je nepadajuće.

Sve vrhove grafa pretražujemo redoslijedom pretraživanja u dubinu, održavamo varijable `dfn` i `low` svakog vrha i posjećene vrhove stavljamo na stog. Svaki put kad nađemo jako povezanu komponentu, sa stoga skinemo onoliko elemenata koliko ona ima vrhova. Tijekom pretrage, za vrh $u$ i njegova susjeda $v$ ($v$ nije roditelj vrha $u$) razlikujemo 3 slučaja:

1.  $v$ nije posjećen: nastavi pretraživanje u dubinu iz $v$. Pri povratku ažuriraj $\textit{low}_u$ pomoću $\textit{low}_v$. Budući da postoji izravan put od $u$ do $v$, do vrha na stogu do kojeg se može vratiti $v$ može se vratiti i $u$.
2.  $v$ je posjećen i još je na stogu: prema definiciji vrijednosti low ažuriraj $\textit{low}_u$ pomoću $\textit{dfn}_v$.
3.  $v$ je posjećen i više nije na stogu: to znači da je pretraga iz $v$ završena i da je njegova komponenta već obrađena, pa ništa ne radimo.

Za graf koji je jedna povezana komponenta lako je uočiti da u njemu postoji točno jedan vrh $u$ za koji vrijedi $\textit{dfn}_u=\textit{low}_u$. To je nužno vrh te komponente koji je u pretraživanju u dubinu posjećen prvi, jer su mu dfn i low najmanji i ostali vrhovi komponente ne mogu na njih utjecati.

Stoga pri povratku iz rekurzije provjeravamo vrijedi li $\textit{dfn}_u=\textit{low}_u$; ako vrijedi, vrh $u$ i vrhovi iznad njega na stogu tvore jednu SCC.

Gornji algoritam zapisan pseudokodom:

???+ note "Implementacija"
    ```text
    TARJAN_SEARCH(int u)
        vis[u]=true
        low[u]=dfn[u]=++dfncnt
        push u to the stack
        for each (u,v) then do
            if v hasn't been searched then
                TARJAN_SEARCH(v) // pretraži
                low[u]=min(low[u],low[v]) // povratak iz rekurzije
            else if v has been in the stack then
                low[u]=min(low[u],dfn[v])
        if dfn[u] equal to low[u] then
            ++scccnt
            while top of stack not equal to u then
                scc[top of stack] = scccnt
                pop stack
            scc[u] = scccnt
            pop stack // obradi i skini preostali u
    ```

### Implementacija

=== "C++"
    ```cpp
    int dfn[N], low[N], dfncnt, s[N], in_stack[N], tp;
    int scc[N], sc;  // oznaka SCC-a kojem pripada vrh i
    int sz[N];       // veličina jako povezane komponente i
    
    void tarjan(int u) {
      low[u] = dfn[u] = ++dfncnt, s[++tp] = u, in_stack[u] = 1;
      for (int i = h[u]; i; i = e[i].nex) {
        const int &v = e[i].t;
        if (!dfn[v]) {
          tarjan(v);
          low[u] = min(low[u], low[v]);
        } else if (in_stack[v]) {
          low[u] = min(low[u], dfn[v]);
        }
      }
      if (dfn[u] == low[u]) {
        ++sc;
        do {
          scc[s[tp]] = sc;
          sz[sc]++;
          in_stack[s[tp]] = 0;
        } while (s[tp--] != u);
      }
    }
    ```

=== "Python"
    ```python
    dfn = [0] * N
    low = [0] * N
    dfncnt = 0
    s = [0] * N
    in_stack = [0] * N
    tp = 0
    scc = [0] * N
    sc = 0  # oznaka SCC-a kojem pripada vrh i
    sz = [0] * N  # veličina jako povezane komponente i
    
    
    def tarjan(u):
        low[u] = dfn[u] = dfncnt
        s[tp] = u
        in_stack[u] = 1
        dfncnt = dfncnt + 1
        tp = tp + 1
        i = h[u]
        while i:
            v = e[i].t
            if dfn[v] == False:
                tarjan(v)
                low[u] = min(low[u], low[v])
            elif in_stack[v]:
                low[u] = min(low[u], dfn[v])
            i = e[i].nex
        if dfn[u] == low[u]:
            sc = sc + 1
            while s[tp] != u:
                scc[s[tp]] = sc
                sz[sc] = sz[sc] + 1
                in_stack[s[tp]] = 0
                tp = tp - 1
            scc[s[tp]] = sc
            sz[sc] = sz[sc] + 1
            in_stack[s[tp]] = 0
            tp = tp - 1
    ```

Vremenska složenost $O(n + m)$.

### Odnos oznaka komponenata i topološkog poretka

Tarjanov algoritam tijekom rada zapravo otkriva jako povezane komponente u nekom **obrnutom topološkom poretku**, jer tijekom pretraživanja u dubinu prvo dovršava vrhove koji nemaju izlaznih bridova, što je suprotno postupku topološkog sortiranja.

Ako sve jako povezane komponente grafa sažmemo u pojedinačne vrhove, topološko sortiranje DAG-a koji tvore ti sažeti vrhovi daje poredak suprotan redoslijedu oznaka jako povezanih komponenata koje daje Tarjanov algoritam.

Stoga možemo reći da je u sažetom DAG-u **redoslijed oznaka jako povezanih komponenata (nakon sažimanja) obrnut njihovu topološkom poretku**. Treba napomenuti da to vrijedi samo kad promatramo ovisnosti između jako povezanih komponenata (tj. usmjerene bridove iz jedne jako povezane komponente u drugu). Vrhovi unutar jedne jako povezane komponente zbog ciklusa ne zadovoljavaju definiciju topološkog poretka.

## Kosarajuov algoritam

### Uvod

Kosarajuov algoritam prvi je 1978. predložio S. Rao Kosaraju u neobjavljenom radu, a prvi ga je objavio Micha Sharir.

### Postupak

Algoritam se oslanja na dva jednostavna DFS-a:

U prvom DFS-u biramo proizvoljan vrh kao početni, obilazimo sve neposjećene vrhove i vrhove numeriramo prije povratka iz rekurzije, tj. u postorder redoslijedu.

U drugom DFS-u, na obrnutom grafu, pokrećemo DFS iz vrha s najvećom oznakom. Skup tako posjećenih vrhova jedna je jako povezana komponenta. Među svim neposjećenim vrhovima ponovno biramo onaj s najvećom oznakom i ponavljamo postupak.

Nakon dvaju DFS-ova jako povezane komponente su pronađene; vremenska složenost Kosarajuova algoritma je $O(n+m)$.

### Implementacija

=== "C++"
    ```cpp
    // g je izvorni graf, g2 je obrnuti graf
    
    void dfs1(int u) {
      vis[u] = true;
      for (int v : g[u])
        if (!vis[v]) dfs1(v);
      s.push_back(u);
    }
    
    void dfs2(int u) {
      color[u] = sccCnt;
      for (int v : g2[u])
        if (!color[v]) dfs2(v);
    }
    
    void kosaraju() {
      sccCnt = 0;
      for (int i = 1; i <= n; ++i)
        if (!vis[i]) dfs1(i);
      for (int i = n - 1; i >= 0; --i)
        if (!color[s[i]]) {
          ++sccCnt;
          dfs2(s[i]);
        }
    }
    ```

=== "Python"
    ```python
    def dfs1(u):
        vis[u] = True
        for v in g[u]:
            if vis[v] == False:
                dfs1(v)
        s.append(u)
    
    
    def dfs2(u):
        color[u] = sccCnt
        for v in g2[u]:
            if color[v] == False:
                dfs2(v)
    
    
    def kosaraju(u):
        sccCnt = 0
        for i in range(1, n + 1):
            if vis[i] == False:
                dfs1(i)
        for i in range(n - 1, -1, -1):
            if color[s[i]] == False:
                sccCnt = sccCnt + 1
                dfs2(s[i])
    ```

## Gabowov algoritam

### Postupak

Gabowov algoritam druga je implementacija Tarjanova algoritma. Tarjanov algoritam korijen jako povezane komponente određuje pomoću dfn i low, a Gabow održava stog vrhova i drugi stog kojim određuje kada s prvog stoga treba skinuti vrhove koji pripadaju istoj jako povezanoj komponenti. Tijekom DFS-a iz vrha $w$, kad neki put pokaže da skupina vrhova pripada istoj jako povezanoj komponenti, s drugog stoga skidamo vrhove dok god je vrijeme posjeta vrha na vrhu stoga veće od vremena posjeta korijena $w$, tako da na kraju ostane samo korijen $w$. Svi vrhovi skinuti u tom postupku pripadaju istoj jako povezanoj komponenti.

Kad se vratimo u neki vrh $w$ i on je na vrhu drugog stoga, znači da je $w$ početni vrh jako povezane komponente, a vrhovi pretraženi nakon njega pripadaju istoj komponenti; tada ih skidamo s prvog stoga i oni tvore jako povezanu komponentu.

### Implementacija

=== "C++"
    ```cpp
    int garbow(int u) {
      stack1[++p1] = u;
      stack2[++p2] = u;
      low[u] = ++dfs_clock;
      for (int i = head[u]; i; i = e[i].next) {
        int v = e[i].to;
        if (!low[v])
          garbow(v);
        else if (!sccno[v])
          while (low[stack2[p2]] > low[v]) p2--;
      }
      if (stack2[p2] == u) {
        p2--;
        scc_cnt++;
        do {
          sccno[stack1[p1]] = scc_cnt;
          // all_scc[scc_cnt] ++;
        } while (stack1[p1--] != u);
      }
      return 0;
    }
    
    void find_scc(int n) {
      dfs_clock = scc_cnt = 0;
      p1 = p2 = 0;
      memset(sccno, 0, sizeof(sccno));
      memset(low, 0, sizeof(low));
      for (int i = 1; i <= n; i++)
        if (!low[i]) garbow(i);
    }
    ```

=== "Python"
    ```python
    def garbow(u):
        stack1[p1] = u
        stack2[p2] = u
        p1 = p1 + 1
        p2 = p2 + 1
        low[u] = dfs_clock
        dfs_clock = dfs_clock + 1
        i = head[u]
        while i:
            v = e[i].to
            if low[v] == False:
                garbow(v)
            elif sccno[v] == False:
                while low[stack2[p2]] > low[v]:
                    p2 = p2 - 1
        if stack2[p2] == u:
            p2 = p2 - 1
            scc_cnt = scc_cnt + 1
            while stack1[p1] != u:
                p1 = p1 - 1
                sccno[stack1[p1]] = scc_cnt
    
    
    def find_scc(n):
        dfs_clock = scc_cnt = 0
        p1 = p2 = 0
        sccno = []
        low = []
        for i in range(1, n + 1):
            if low[i] == False:
                garbow(i)
    ```

## Primjene

Svaku jako povezanu komponentu grafa možemo sažeti u jedan vrh.

Graf tada postaje DAG, na kojem možemo provesti topološko sortiranje i mnoge druge operacije.

Jednostavan primjer: nađi put koji smije ponavljati vrhove, a prolazi kroz najveći mogući broj različitih vrhova.

## Zadaci za vježbu

[USACO Fall/HAOI 2006 Popularne krave](https://loj.ac/problem/10091)

[POJ1236 Network of Schools](http://poj.org/problem?id=1236)
