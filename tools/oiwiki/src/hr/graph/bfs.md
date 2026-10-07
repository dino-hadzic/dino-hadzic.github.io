---
title: BFS (teorija grafova)
---

BFS je kratica za [Breadth First Search](https://en.wikipedia.org/wiki/Breadth-first_search), hrvatski pretraživanje u širinu.

To je jedan od najosnovnijih i najvažnijih algoritama pretraživanja na grafovima.

„U širinu” znači da u svakom koraku pokušavamo posjetiti vrhove iste razine.
Tek kad je cijela razina posjećena, prelazimo na sljedeću.

Posljedica je toga da je put koji BFS pronađe **najkraći** dopušteni put od početnog vrha. Drugim riječima, taj put sadrži najmanji broj bridova.

Kad BFS završi, svaki je vrh posjećen najkraćim putem od početnog vrha do njega.

Tijek algoritma možemo zamisliti kao širenje požara po grafu: na početku gori samo početni vrh, a u svakom trenutku svaki zapaljeni vrh prenosi vatru na sve svoje susjede.

## Implementacija

Implementacije u C++-u i Pythonu u nastavku temelje se na pohrani grafa ulančanim forward star zapisom; o toj implementaciji vidi stranicu [Pohrana grafa](./save.md).

=== "Pseudokod"
    ```text
    bfs(s) {
      q = new queue()
      q.push(s), visited[s] = true
      while (!q.empty()) {
        u = q.pop()
        for each edge(u, v) {
          if (!visited[v]) {
            q.push(v)
            visited[v] = true
          }
        }
      }
    }
    ```

=== "C++"
    ```cpp
    void bfs(int u) {
      while (!Q.empty()) Q.pop();
      Q.push(u);
      vis[u] = 1;
      d[u] = 0;
      p[u] = -1;
      while (!Q.empty()) {
        u = Q.front();
        Q.pop();
        for (int i = head[u]; i; i = e[i].nxt) {
          if (!vis[e[i].to]) {
            Q.push(e[i].to);
            vis[e[i].to] = 1;
            d[e[i].to] = d[u] + 1;
            p[e[i].to] = u;
          }
        }
      }
    }
    
    void restore(int x) {
      vector<int> res;
      for (int v = x; v != -1; v = p[v]) {
        res.push_back(v);
      }
      std::reverse(res.begin(), res.end());
      for (int i = 0; i < res.size(); ++i) printf("%d", res[i]);
      puts("");
    }
    ```

=== "Python"
    ```python
    from queue import Queue
    
    
    def bfs(u):
        Q = Queue()
        Q.put(u)
        vis[u] = True
        d[u] = 0
        p[u] = -1
        while Q.qsize() != 0:
            u = Q.get()
            i = head[u]
            while i:
                if vis[e[i].to] == False:
                    Q.put(e[i].to)
                    vis[e[i].to] = True
                    d[e[i].to] = d[u] + 1
                    p[e[i].to] = u
                i = e[i].nxt
    
    
    def restore(x):
        res = []
        v = x
        while v != -1:
            res.append(v)
            v = p[v]
        res.reverse()
        for i in range(0, len(res)):
            print(res[i])
    ```

Konkretno, redom Q bilježimo vrhove koje treba obraditi, a booleovim poljem `vis[]` označavamo je li neki vrh već posjećen.

Na početku svim vrhovima postavimo `vis` na 0, što znači da nisu posjećeni; zatim početni vrh s stavimo u red Q i postavimo `vis[s]` na 1.

Nakon toga u svakom koraku iz reda Q uzimamo vrh u s početka reda, a sve vrhove v susjedne vrhu u označimo kao posjećene i stavimo u red Q.

Petlja se ponavlja dok red Q ne postane prazan, čime BFS završava.

Tijekom BFS-a možemo bilježiti i dodatne podatke. Primjerice, u gornjem kodu polje d bilježi najkraću udaljenost od početnog vrha do pojedinog vrha (najmanji broj bridova koje treba prijeći), a polje p bilježi iz kojeg smo vrha došli u trenutačni vrh.

S poljem d lako dobivamo udaljenost od početnog vrha do nekog vrha.

S poljem p lako rekonstruiramo najkraći put od početnog vrha do nekog vrha. Funkcija `restore` u gornjem kodu pomoću tog polja redom ispisuje vrhove na najkraćem putu od početnog vrha do vrha x.

Vremenska složenost: $O(n + m)$

Prostorna složenost: $O(n)$ (polje `vis` i red)

## Open-closed tablica

Pri implementaciji BFS-a u biti neposjećene vrhove držimo u spremniku koji se zove open, a već posjećene vrhove u spremniku koji se zove closed.

## BFS na stablu/grafu

### BFS poredak

Slično DFS poretku, BFS poredak je niz indeksa vrhova u redoslijedu kojim ih BFS posjećuje.

### BFS na općem grafu

Ako polazni graf nije povezan, mogu se posjetiti samo vrhovi dostižni iz početnog vrha.

Ni BFS poredak u pravilu nije jedinstven.

Analogno možemo definirati i BFS stablo: ako tijekom BFS-a za svaki vrh zabilježimo iz kojeg smo vrha u njega došli, dobivamo strukturu stabla, a to je BFS stablo.

## Primjene

-   Pronalaženje najkraćih puteva od početnog vrha do svih ostalih vrhova u netežinskom grafu.
-   Pronalaženje svih komponenata povezanosti u vremenu $O(n+m)$. (Dovoljno je pokrenuti BFS iz svakog još neposjećenog vrha; očito svaki BFS obiđe točno jednu komponentu povezanosti.)
-   Ako potez u igri shvatimo kao brid (prijelaz) u grafu stanja, BFS-om možemo naći najmanji broj poteza potreban da se iz jednog stanja igre dođe u drugo.
-   Pronalaženje najkraćeg ciklusa u usmjerenom netežinskom grafu. (Pokrenemo BFS iz svakog vrha; kad smo pred time da ponovno dođemo u već posjećeni vrh iz kojeg smo krenuli, znamo da smo naišli na ciklus. Najkraći ciklus grafa je najmanji od ciklusa dobivenih pojedinim BFS-ovima.)
-   Pronalaženje bridova koji sigurno leže na najkraćem putu $(a, b)$. (Pokrenemo BFS redom iz a i iz b i dobijemo dva polja d. Zatim za svaki brid $(u, v)$: ako je $d_a[u]+1+d_b[v]=d_a[b]$, brid leži na najkraćem putu.)
-   Pronalaženje vrhova koji sigurno leže na najkraćem putu $(a, b)$. (Pokrenemo BFS redom iz a i iz b i dobijemo dva polja d. Zatim za svaki vrh v: ako je $d_a[v]+d_b[v]=d_a[b]$, vrh leži na nekom najkraćem putu.)
-   Pronalaženje najkraćeg puta parne duljine. (Trebamo konstruirati novi graf u kojem svaki vrh razdvojimo na dva nova vrha, a brid $(u, v)$ polaznog grafa postaje $((u, 0), (v, 1))$ i $((u, 1), (v, 0))$. Pokrenemo BFS na novom grafu; najkraći put između $(s, 0)$ i $(t, 0)$ traženi je put.)
-   Pronalaženje najkraćih puteva u grafu s težinama bridova 0/1, vidi BFS s dvostranim redom u nastavku.

## BFS s dvostranim redom

Ako niste upoznati s dvostranim redom `deque`, pogledajte [odjeljak o deque](../lang/csl/sequence-container.md#deque).

BFS s dvostranim redom naziva se i 0-1 BFS.

### Područje primjene

Problemi najkraćeg puta u kojima brid može, ali i ne mora imati težinu (budući da je BFS primjenjiv na grafove s težinom 1, težine su obično 0 ili 1), ili koji se mogu svesti na takve težine bridova.

Primjerice, u zadatku s labirintom možete za 1 novčić napraviti 5 koraka ili bez novčića 1 korak; to se može riješiti 0-1 BFS-om.

### Implementacija

U pravilu vrhove do kojih dolazimo bridom bez težine stavljamo na početak reda, a vrhove do kojih dolazimo bridom s težinom na kraj reda. Tako se, kao i kod običnog BFS-a, jamči da su težine od početka do kraja reda monotono neopadajuće.

Slijedi pseudokod:

```cpp
while (red nije prazan) {
  int u = početak reda;
  izbaci početak reda;
  for (prođi po susjedima od u) {
    ažuriraj podatke
    if (...)
      dodaj na početak reda;
    else
      dodaj na kraj reda;
  }
}
```

### Primjer zadatka

### [Codeforces 173B](http://codeforces.com/problemset/problem/173/B)

Zadana je mreža $n \times m$. Laserska zraka ulazi iz gornjeg lijevog kuta i kreće se udesno; na svakom znaku '#' možete odabrati da se zraka raspršuje u sva četiri smjera ili ne učiniti ništa. Pitanje je koliko najmanje znakova '#' treba raspršivati zraku u sva četiri smjera da bi zraka izašla udesno u $n$-tom retku.

Službeno rješenje ovog zadatka nije 0-1 BFS, ali 0-1 BFS je primjenjiv i smanjuje količinu razmišljanja; mnogi su ga jaki natjecatelji na natjecanju tako riješili.

Postupak je jednostavan: izlazak zrake u jednom smjeru ne košta ništa (0), a raspršivanje u četiri smjera košta (1); nakon toga samo primijenimo algoritam.

#### Kôd

```cpp
--8<-- "docs/graph/code/bfs/bfs_1.cpp"
```

## BFS s prioritetnim redom

Prioritetni red odgovara binarnoj hrpi (heap); STL nudi [`std::priority_queue`](../lang/csl/container-adapter.md), koji nam olakšava rad s prioritetnim redom.

U BFS-u temeljenom na prioritetnom redu u svakom koraku s početka reda uzimamo vrh najmanje cijene i iz njega nastavljamo pretragu. Lako se dokazuje da je ta greedy ideja ispravna, jer pretraga koja se širi iz tog vrha sigurno neće ažurirati vrhove s većom cijenom. Drugim riječima, ostale vrhove s većom cijenom ne razmatramo ponovno radi ažuriranja.

Naravno, isti vrh može ući u red više puta, svaki put s različitom cijenom. Kad se taj vrh prvi put izvadi iz prioritetnog reda, dalje iz njega više ne treba pretraživati nego ga jednostavno ignoriramo. Stoga se u BFS-u s prioritetnim redom svaki vrh obrađuje samo jednom.

U odnosu na BFS s običnim redom vremenska je složenost veća za faktor $\log n$, jer ipak treba održavati prioritetni red. No obični BFS može svaki vrh više puta staviti u red i izvaditi iz njega, pa vremenska složenost može doseći $O(n^2)$, a ne $O(n)$. Zato je BFS s prioritetnim redom u pravilu ipak brži.

Hm? Ne zvuči li to vrlo slično [Dijkstrinu](./shortest-path.md#dijkstrin-algoritam) algoritmu s hrpom? Zapravo, Dijkstra optimiziran hrpom upravo jest BFS s prioritetnim redom.

## Zadaci za vježbu

-   [„NOIP2017” Sir (Cheese)](https://uoj.ac/problem/332)

BFS s dvostranim redom:

-   [CF1063B. Labyrinth](https://codeforces.com/problemset/problem/1063/B)
-   [CF173B. Chamber of Secrets](https://codeforces.com/problemset/problem/173/B)
-   [„BalticOI 2011 Day1” Switch the Lamp On](https://loj.ac/p/2632)

## Literatura

<https://cp-algorithms.com/graph/breadth-first-search.html>
