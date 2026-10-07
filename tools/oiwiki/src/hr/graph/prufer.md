---
title: Prüferov niz
---

???+ note "Napomena"
    Ovaj je članak prijevod [e-maxx Prüfer Code](https://github.com/e-maxx-eng/e-maxx-eng/blob/master/src/graph/pruefer_code.md). Napomena: u izvorniku su vrhovi numerirani od $0$, a ovdje smo, u skladu s uobičajenom praksom, prešli na numeriranje od $1$.

Ovaj članak predstavlja Prüferov niz (Prüfer code), način da se označeno stablo prikaže jedinstvenim nizom cijelih brojeva.

Prüferovim nizom može se dokazati [Cayleyjeva formula](#cayleyjeva-formula-cayleys-formula) (Cayley's formula). Objasnit ćemo i kako izbrojiti načine dodavanja bridova u graf tako da postane povezan.

**Napomena**: ne razmatramo stabla s $1$ vrhom.

## Prüferov niz

### Uvod

Prüferov niz prikazuje označeno stablo s $n$ vrhova pomoću $n-2$ cijela broja iz $[1,n]$. Možete ga shvatiti i kao bijekciju između razapinjućih stabala potpunog grafa i nizova. Često se koristi u problemima kombinatornog prebrojavanja.

Heinz Prüfer izumio je ovaj niz 1918. godine da bi dokazao [Cayleyjevu formulu](#cayleyjeva-formula-cayleys-formula).

### Građenje Prüferova niza za stablo

Prüferov niz gradi se ovako: svaki put odaberemo list s najmanjim brojem i izbrišemo ga, a u niz zapišemo vrh s kojim je bio povezan. Nakon $n-2$ ponavljanja ostaju samo dva vrha i algoritam završava.

Očito se pomoću hrpe (heap) može postići složenost $O(n\log n)$.

???+ note "Implementacija"
    === "C++"
        ```cpp
        // kôd preuzet iz izvornika, vrhovi su numerirani od 0
        vector<vector<int>> adj;
        
        vector<int> pruefer_code() {
          int n = adj.size();
          set<int> leafs;
          vector<int> degree(n);
          vector<bool> killed(n);
          for (int i = 0; i < n; i++) {
            degree[i] = adj[i].size();
            if (degree[i] == 1) leafs.insert(i);
          }
        
          vector<int> code(n - 2);
          for (int i = 0; i < n - 2; i++) {
            int leaf = *leafs.begin();
            leafs.erase(leafs.begin());
            killed[leaf] = true;
            int v;
            for (int u : adj[leaf])
              if (!killed[u]) v = u;
            code[i] = v;
            if (--degree[v] == 1) leafs.insert(v);
          }
          return code;
        }
        ```
    
    === "Python"
        ```python
        # vrhovi su numerirani od 0
        adj = [[]]
        
        
        def pruefer_code():
            n = len(adj)
            leafs = set()
            degree = [0] * n
            killed = [False] * n
            for i in range(1, n):
                degree[i] = len(adj[i])
                if degree[i] == 1:
                    leafs.intersection(i)
            code = [0] * (n - 2)
            for i in range(1, n - 2):
                leaf = leafs[0]
                leafs.pop()
                killed[leaf] = True
                for u in adj[leaf]:
                    if killed[u] == False:
                        v = u
                code[i] = v
                if degree[v] == 1:
                    degree[v] = degree[v] - 1
                    leafs.intersection(v)
            return code
        ```

Primjerice, ovo je postupak građenja Prüferova niza za stablo sa 7 vrhova:

![Prüfer](./images/prufer1.png)

Konačni niz je $2,2,3,3,2$.

Naravno, postoji i linearni algoritam građenja.

### Linearni algoritam građenja Prüferova niza

Bit linearnog građenja jest održavanje pokazivača na vrh koji ćemo sljedeći izbrisati. Najprije uočimo da je broj listova nestrogo monotono padajući: brisanjem jednog lista ukupan broj listova ili ostaje isti ili se smanji za 1.

Zato razmotrimo sljedeći postupak: održavamo pokazivač $p$. Na početku $p$ pokazuje na list s najmanjim brojem. Istodobno održavamo stupanj svakog vrha, kako bismo pri brisanju vrha znali nastaje li novi list. Postupak je sljedeći:

1.  Izbrišemo vrh na koji pokazuje $p$ i provjerimo nastaje li novi list.
2.  Ako nastane novi list, recimo s brojem $x$, usporedimo $p$ i $x$. Ako je $x>p$, ne činimo ništa; inače odmah izbrišemo $x$, zatim provjerimo nastaje li brisanjem $x$ novi list i ponavljamo korak $2$ dok ne prestanu nastajati novi listovi ili dok novi list nema broj $>p$.
3.  Pokazivač $p$ povećavamo dok ne naiđemo na neizbrisani list.

#### Ispravnost

Ponavljanjem gornjih operacija $n-2$ puta niz je izgrađen. Razmotrimo sada ispravnost algoritma.

$p$ je trenutni list s najmanjim brojem. Ako brisanjem $p$ ne nastane list, možemo samo potražiti sljedeći list; ako nastane list $x$:

-   ako je $x>p$, $p$ će ga pri daljnjem pomicanju svakako dosegnuti, pa ne činimo ništa;
-   ako je $x<p$, budući da je $p$ bio list s najmanjim brojem, a $x$ je još manji od $p$, $x$ je sada list s najmanjim brojem i brišemo ga prvog. Nakon brisanja $x$ nastavljamo isto razmatranje dok više nema manjih listova.

Analiza složenosti: svaki se brid posjeti najviše jednom (pri smanjivanju stupnja), a pokazivač prođe svaki vrh najviše jednom, pa je složenost $O(n)$.

#### Implementacija

=== "C++"
    ```cpp
    // kôd preuzet iz izvornika, također s numeriranjem od 0
    vector<vector<int>> adj;
    vector<int> parent;
    
    void dfs(int v) {
      for (int u : adj[v]) {
        if (u != parent[v]) parent[u] = v, dfs(u);
      }
    }
    
    vector<int> pruefer_code() {
      int n = adj.size();
      parent.resize(n), parent[n - 1] = -1;
      dfs(n - 1);
    
      int ptr = -1;
      vector<int> degree(n);
      for (int i = 0; i < n; i++) {
        degree[i] = adj[i].size();
        if (degree[i] == 1 && ptr == -1) ptr = i;
      }
    
      vector<int> code(n - 2);
      int leaf = ptr;
      for (int i = 0; i < n - 2; i++) {
        int next = parent[leaf];
        code[i] = next;
        if (--degree[next] == 1 && next < ptr) {
          leaf = next;
        } else {
          ptr++;
          while (degree[ptr] != 1) ptr++;
          leaf = ptr;
        }
      }
      return code;
    }
    ```

=== "Python"
    ```python
    # također s numeriranjem od 0
    adj = [[]]
    parent = [0] * n
    
    
    def dfs(v):
        for u in adj[v]:
            if u != parent[v]:
                parent[u] = v
                dfs(u)
    
    
    def pruefer_code():
        n = len(adj)
        parent[n - 1] = -1
        dfs(n - 1)
    
        ptr = -1
        degree = [0] * n
        for i in range(0, n):
            degree[i] = len(adj[i])
            if degree[i] == 1 and ptr == -1:
                ptr = i
    
        code = [0] * (n - 2)
        leaf = ptr
        for i in range(0, n - 2):
            next = parent[leaf]
            code[i] = next
            if degree[next] == 1 and next < ptr:
                degree[next] = degree[next] - 1
                leaf = next
            else:
                ptr = ptr + 1
                while degree[ptr] != 1:
                    ptr = ptr + 1
                leaf = ptr
        return code
    ```

### Svojstva Prüferova niza

1.  Nakon građenja Prüferova niza u izvornom stablu ostaju dva vrha, od kojih je jedan sigurno vrh s najvećim brojem $n$.
2.  Svaki se vrh u nizu pojavljuje onoliko puta koliki mu je stupanj umanjen za $1$. (Oni koji se ne pojavljuju su listovi.)

### Rekonstrukcija stabla iz Prüferova niza

Rekonstrukcija stabla ide slično. Iz svojstava Prüferova niza možemo dobiti stupanj svakog vrha izvornog stabla. Zatim možemo odrediti i list s najmanjim brojem, a taj je vrh sigurno povezan s vrhom koji odgovara prvom broju Prüferova niza. Potom obama vrhovima smanjimo stupanj za jedan.

Vjerojatno već znate kako dalje. Svaki put odaberemo vrh stupnja $1$ s najmanjim brojem, povežemo ga s vrhom Prüferova niza na koji smo trenutno došli i obama vrhovima smanjimo stupanj. Na kraju ostaju dva vrha stupnja $1$, od kojih je jedan vrh $n$. Povežemo ih. Postupak održavamo hrpom: kad se pri smanjivanju stupnja nekog vrha stupanj spusti na $1$, dodamo taj vrh u hrpu; složenost je $O(n\log n)$.

???+ note "Implementacija"
    ```cpp
    // kôd preuzet iz izvornika
    vector<pair<int, int>> pruefer_decode(vector<int> const& code) {
      int n = code.size() + 2;
      vector<int> degree(n, 1);
      for (int i : code) degree[i]++;
    
      set<int> leaves;
      for (int i = 0; i < n; i++)
        if (degree[i] == 1) leaves.insert(i);
    
      vector<pair<int, int>> edges;
      for (int v : code) {
        int leaf = *leaves.begin();
        leaves.erase(leaves.begin());
    
        edges.emplace_back(leaf, v);
        if (--degree[v] == 1) leaves.insert(v);
      }
      edges.emplace_back(*leaves.begin(), n - 1);
      return edges;
    }
    ```

### Rekonstrukcija stabla u linearnom vremenu

Isto kao kod linearnog građenja Prüferova niza. Pri smanjivanju stupnja nastaju novi listovi, pa usporedimo taj list s pokazivačem $p$ i, ako je manji, njega obradimo prvog.

#### Implementacija

```cpp
// kôd preuzet iz izvornika
vector<pair<int, int>> pruefer_decode(vector<int> const& code) {
  int n = code.size() + 2;
  vector<int> degree(n, 1);
  for (int i : code) degree[i]++;

  int ptr = 0;
  while (degree[ptr] != 1) ptr++;
  int leaf = ptr;

  vector<pair<int, int>> edges;
  for (int v : code) {
    edges.emplace_back(leaf, v);
    if (--degree[v] == 1 && v < ptr) {
      leaf = v;
    } else {
      ptr++;
      while (degree[ptr] != 1) ptr++;
      leaf = ptr;
    }
  }
  edges.emplace_back(leaf, n - 1);
  return edges;
}
```

Iz ovih je postupaka jasno da Prüferov niz uspostavlja bijekciju s označenim nekorijenskim stablima.

## Cayleyjeva formula (Cayley's formula)

Potpuni graf $K_n$ ima $n^{n-2}$ razapinjućih stabala.

Kako to dokazati? Postoji mnogo načina, ali dokaz Prüferovim nizom vrlo je jednostavan. Svaki niz cijelih brojeva duljine $n-2$ s vrijednostima iz $[1,n]$ bijektivno odgovara, preko Prüferova niza, jednom razapinjućem stablu, pa je broj načina $n^{n-2}$.

## Broj načina da graf postane povezan

Prüferov niz možda je moćniji nego što mislite. Pomoću njega dobivamo formule općenitije od [Cayleyjeve formule](#cayleyjeva-formula-cayleys-formula). Primjerice, sljedeći problem:

> Označeni neusmjereni graf s $n$ vrhova i $m$ bridova ima $k$ komponenata povezanosti. Želimo dodati $k-1$ bridova tako da cijeli graf postane povezan. Odredite broj načina.

### Dokaz

Neka $s_i$ označava broj vrhova u $i$-toj komponenti. Razmotrimo građenje Prüferova niza za $k$ komponenata. Budući da postoji mnogo načina spajanja dviju komponenata, to nije običan Prüferov niz. Neka je stoga $d_i$ stupanj $i$-te komponente. Budući da je zbroj stupnjeva dvostruki broj bridova, vrijedi $\sum_{i=1}^kd_i=2k-2$. Tada je za zadani niz $d$ broj načina građenja Prüferova niza

$$
\binom{k-2}{d_1-1,d_2-1,\cdots,d_k-1}=\frac{(k-2)!}{(d_1-1)!(d_2-1)!\cdots(d_k-1)!}
$$

Za $i$-tu komponentu postoji ${s_i}^{d_i}$ načina spajanja, pa je za zadani niz $d$ broj načina da graf postane povezan

$$
\binom{k-2}{d_1-1,d_2-1,\cdots,d_k-1}\cdot \prod_{i=1}^k{s_i}^{d_i}
$$

Sada treba proći sve nizove $d$, pa izraz postaje

$$
\sum_{d_i\ge 1，\sum_{i=1}^kd_i=2k-2}\binom{k-2}{d_1-1,d_2-1,\cdots,d_k-1}\cdot \prod_{i=1}^k{s_i}^{d_i}
$$

Dobro, ovo je vrlo neugodan izraz. Ali bez panike! Imamo multinomni teorem:

$$
(x_1 + \dots + x_m)^p = \sum_{\substack{c_i \ge 0 ,\  \sum_{i=1}^m c_i = p}} \binom{p}{c_1, c_2, \cdots ,c_m}\cdot \prod_{i=1}^m{x_i}^{c_i}
$$

Uvedimo zamjenu u izvorni izraz: neka je $e_i=d_i-1$; očito je $\sum_{i=1}^ke_i=k-2$, pa izvorni izraz postaje

$$
\sum_{e_i\ge 0，\sum_{i=1}^ke_i=k-2}\binom{k-2}{e_1,e_2,\cdots,e_k}\cdot \prod_{i=1}^k{s_i}^{e_i+1}
$$

Pojednostavljivanjem dobivamo

$$
(s_1+s_2+\cdots+s_k)^{k-2}\cdot \prod_{i=1}^ks_i
$$

tj.

$$
n^{k-2}\cdot\prod_{i=1}^ks_i
$$

što je odgovor.

## Zadaci

-   [Luogu P6086【模板】Prüfer 序列](https://www.luogu.com.cn/problem/P6086) (ogledni zadatak)
-   [Luogu P11039【MX-X3-T6】「RiOI-4」TECHNOPOLIS 2085](https://www.luogu.com.cn/problem/P11039)
-   [UVa #10843 - Anne's game](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=20&page=show_problem&problem=1784)
-   [Timus #1069 - Prufer Code](http://acm.timus.ru/problem.aspx?space=1&num=1069)
-   [Codeforces - Clues](http://codeforces.com/contest/156/problem/D)
-   [Topcoder - TheCitiesAndRoadsDivTwo](https://archive.topcoder.com/ProblemStatement/pm/10774)
