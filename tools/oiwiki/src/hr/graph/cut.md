---
title: Artikulacijski vrhovi i mostovi
---

Srodno štivo: [Dvostruko povezane komponente](./bcc.md)

Strože definicije artikulacijskih vrhova i mostova vidi u [Osnovni pojmovi teorije grafova](./concept.md).

## Artikulacijski vrhovi

> Ako se u neusmjerenom grafu brisanjem nekog vrha poveća broj maksimalnih povezanih komponenata, taj je vrh artikulacijski vrh (cut vertex, naziva se i rezni vrh) grafa.

### Postupak

Kad bismo pokušali obrisati svaki vrh i provjeriti povezanost grafa, složenost bi bila vrlo velika. Zato predstavljamo često korišten algoritam: Tarjanov.

Prvo, evo grafa:

![](./images/cut1.svg)

Lako se vidi da je artikulacijski vrh 2 i da je to jedini artikulacijski vrh grafa.

Prvo vrhovima dodijelimo vremenske oznake prema DFS redoslijedu (redoslijedu posjećivanja).

![](./images/cut2.svg)

Te podatke spremamo u niz koji zovemo `dfn`.

Treba nam još jedan niz, `low`, u kojem čuvamo najmanju vremensku oznaku do koje se može doći ne prolazeći kroz roditelja.

Na primjer, `low[2]` je 1, a `low[5]` i `low[6]` su 3.

Zatim pokrećemo DFS. Kriterij po kojem odlučujemo je li neki vrh artikulacijski glasi: za vrh $u$, ako postoji barem jedan vrh $v$ (dijete vrha $u$) takav da je $low_v \geq dfn_u$, tj. $v$ se ne može vratiti do pretka, tada je $u$ artikulacijski vrh.

Taj kriterij ne vrijedi jedino za početni vrh pretrage, koji treba razmotriti posebno: ako taj vrh nije artikulacijski, onda se do svih vrhova može doći i drugim putovima, pa iz početnog vrha „pretražujemo prema dolje samo jednom”, tj. on u stablu pretrage ima samo jedno dijete. Ako u stablu pretrage ima dvoje ili više djece, sigurno je artikulacijski vrh (zamislimo da na gornjoj slici krenemo od vrha 2: u stablu pretrage imao bi dvoje djece, 3 ili 4 te 5 ili 6). Ako ima samo jedno dijete, njegovo brisanje nema nikakva utjecaja. Primjerice, u sljedećem grafu nastao je ciklus.

![](./images/cut3.svg)

Kad obilazimo djecu vrha 1, recimo da DFS prvo dođe do 2, označi ga kao posjećen, zatim rekurzivno ide dalje do 4, pa od 4 do 3; pri povratku iz rekurzije ustanovit ćemo da je 3 već posjećen, pa 1 nije artikulacijski vrh.

Pseudokod za ažuriranje niza `low`:

$$
\begin{array}{ll}
1 & \textbf{if } v \text{ is a son of } u \\
2 & \qquad \text{low}_u = \min(\text{low}_u, \text{low}_v) \\
3 & \textbf{else} \\
4 & \qquad \text{low}_u = \min(\text{low}_u, \text{dfn}_v) \\
\end{array}
$$

### Primjer

[Luogu P3388 \[Predložak\] Artikulacijski vrhovi (rezni vrhovi)](https://www.luogu.com.cn/problem/P3388)

??? note "Kôd primjera"
    ```cpp
    --8<-- "docs/graph/code/cut/cut_1.cpp"
    ```

## Rezni bridovi (bez višestrukih bridova)

Slično artikulacijskim vrhovima; zovu se mostovi.

> Ako se u neusmjerenom grafu brisanjem nekog brida poveća broj povezanih komponenata, taj se brid zove most ili rezni brid. Strože: neka je $G=\{V,E\}$ povezan graf i $e$ jedan njegov brid (tj. $e \in E$); ako je $G-e$ nepovezan, brid $e$ je rezni brid (most) grafa $G$.

Na primjer, u sljedećem grafu

![primjer reznog brida](./images/bridge1.svg)

crveni je brid rezni brid.

### Postupak

Gotovo isto kao kod artikulacijskih vrhova, mijenja se samo jedno mjesto: dovoljno je $low_v>dfn_u$, a slučaj korijena ne treba posebno razmatrati.

Rezni bridovi nemaju veze s time je li vrh korijen. Kod artikulacijskih vrhova uvjet je značio da se vrh $v$ ne može vratiti do pretka (uključujući roditelja) a da ne prođe kroz roditelja $u$, pa je vrh $u$ artikulacijski. Ako je $low_v=dfn_u$, znači da se još uvijek može vratiti do roditelja; ako se vrh $v$ ne može vratiti do pretka niti postoji drugi put natrag do roditelja, tada je brid $u-v$ rezni brid.

### Implementacija

Sljedeći kôd traži rezne bridove u neusmjerenom grafu **bez višestrukih bridova**; kad je `isbridge[x]` istinito, `(father[x],x)` je rezni brid.

=== "C++"
    ```cpp
    int low[MAXN], dfn[MAXN], idx;
    bool isbridge[MAXN];
    vector<int> G[MAXN];
    int cnt_bridge;
    int father[MAXN];
    
    void tarjan(int u, int fa) {
      father[u] = fa;
      low[u] = dfn[u] = ++idx;
      for (const auto &v : G[u]) {
        if (!dfn[v]) {
          tarjan(v, u);
          low[u] = min(low[u], low[v]);
          if (low[v] > dfn[u]) {
            isbridge[v] = true;
            ++cnt_bridge;
          }
        } else if (v != fa) {
          low[u] = min(low[u], dfn[v]);
        }
      }
    }
    ```

=== "Python"
    ```python
    low = [0] * MAXN
    dfn = [0] * MAXN
    idx = 0
    isbridge = [False] * MAXN
    G = [[0 for i in range(MAXN)] for j in range(MAXN)]
    cnt_bridge = 0
    father = [0] * MAXN
    
    
    def tarjan(u, fa):
        father[u] = fa
        idx = idx + 1
        low[u] = dfn[u] = idx
        for i in range(0, len(G[u])):
            v = G[u][i]
            if dfn[v] == False:
                tarjan(v, u)
                low[u] = min(low[u], low[v])
                if low[v] > dfn[u]:
                    isbridge[v] = True
                    cnt_bridge = cnt_bridge + 1
            elif v != fa:
                low[u] = min(low[u], dfn[v])
    ```

## Rezni bridovi (s višestrukim bridovima)

Međutim, gornji postupak za grafove bez višestrukih bridova ne radi ispravno na neusmjerenim grafovima s višestrukim bridovima.

Između dvaju vrhova može biti više od jednog brida, a tada nijedan od njih nije most.

### Postupak

Jedna je ideja da parametar `fa` zamijenimo oznakom brida kojim smo upravo došli (oba smjera istog brida imaju istu oznaku), tj. da „ne ažuriraj preko roditelja” zamijenimo s „ne ažuriraj preko brida kojim smo došli”.

Druga, jednostavnija ideja jest postaviti zastavicu koja označava je li već jedan brid prema roditelju iskorišten; nakon što je zastavica postavljena, pri sljedećem posjetu roditelju ažuriramo normalno.

Sljedeći kôd traži rezne bridove u neusmjerenom grafu koji **može imati višestruke bridove**.

=== "C++"
    ```cpp
    int low[MAXN], dfn[MAXN], idx;
    bool isbridge[MAXN];
    vector<int> G[MAXN];
    int cnt_bridge;
    int father[MAXN];
    
    void tarjan(int u, int fa) {
      bool flag = false;
      father[u] = fa;
      low[u] = dfn[u] = ++idx;
      for (const auto &v : G[u]) {
        if (!dfn[v]) {
          tarjan(v, u);
          low[u] = min(low[u], low[v]);
          if (low[v] > dfn[u]) {
            isbridge[v] = true;
            ++cnt_bridge;
          }
        } else {
          if (v != fa || flag)
            low[u] = min(low[u], dfn[v]);
          else
            flag = true;
        }
      }
    }
    ```

## Zadaci za vježbu

-   [P3388 \[Predložak\] Artikulacijski vrhovi (rezni vrhovi)](https://www.luogu.com.cn/problem/P3388)
-   [POJ2117 Electricity](http://poj.org/problem?id=2117)
-   [HDU4738 Caocao's Bridges](https://acm.hdu.edu.cn/showproblem.php?pid=4738)
-   [HDU2460 Network](https://acm.hdu.edu.cn/showproblem.php?pid=2460)
-   [POJ1523 SPF](http://poj.org/problem?id=1523)

Tarjanov algoritam ima još mnogo primjena; često se koristi za traženje jako povezanih komponenata, sažimanje komponenata, rješavanje 2-SAT-a itd.
