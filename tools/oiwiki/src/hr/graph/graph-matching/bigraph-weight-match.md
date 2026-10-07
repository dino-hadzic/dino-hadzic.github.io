---
title: Najveće težinsko sparivanje u bipartitnom grafu
---

Najveće težinsko sparivanje (maximum weight matching) bipartitnog grafa je sparivanje s najvećim zbrojem težina bridova.

## Mađarski algoritam (Kuhn–Munkresov algoritam)

Mađarski algoritam, poznat i kao **KM** algoritam, nalazi **najveće težinsko perfektno sparivanje** bipartitnog grafa u vremenu $O(n^3)$.

Budući da dva dijela bipartitnog grafa nemaju uvijek jednak broj vrhova, prije primjene KM algoritma na najveće težinsko sparivanje treba napraviti sljedeće: manjem dijelu dodamo vrhove tako da obje strane imaju jednako vrhova, a težine nepostojećih bridova postavimo na $0$. Problem se tako pretvara u **problem najvećeg težinskog perfektnog sparivanja**, koji KM algoritam može riješiti.

???+ note "Dopustive oznake vrhova"
    Svakom vrhu $i$ pridružimo težinu $l(i)$ tako da za sve bridove $(u,v)$ vrijedi $w(u,v) \leq l(u) + l(v)$.

???+ note "Podgraf jednakosti"
    Razapinjući podgraf izvornog grafa uz zadane dopustive oznake koji sadrži sve vrhove, ali samo one bridove $(u,v)$ za koje je $w(u,v) = l(u) + l(v)$.

???+ note "Teorem 1: Ako za neke dopustive oznake vrhova podgraf jednakosti ima perfektno sparivanje, to je sparivanje najveće težinsko perfektno sparivanje izvornog bipartitnog grafa."
    Dokaz 1.
    
    Promotrimo proizvoljno perfektno sparivanje $M$ izvornog bipartitnog grafa; zbroj težina njegovih bridova je
    
    $val(M) = \sum_{(u,v)\in M} {w(u,v)} \leq \sum_{(u,v)\in M} {l(u) + l(v)} \leq \sum_{i=1}^{n} l(i)$
    
    Zbroj težina bridova perfektnog sparivanja $M'$ podgrafa jednakosti za proizvoljne dopustive oznake je
    
    $val(M') = \sum_{(u,v)\in M} {l(u) + l(v)} = \sum_{i=1}^{n} l(i)$
    
    Dakle zbroj težina bridova bilo kojeg perfektnog sparivanja nije veći od $val(M')$, pa je $M'$ najveće težinsko sparivanje.

Uz Teorem 1 cilj nam je neprekidnim podešavanjem dopustivih oznaka postići da podgraf jednakosti ima perfektno sparivanje.

Budući da obje strane imaju jednak broj vrhova, neka je taj broj $n$; $lx(i)$ označava oznaku $i$-tog lijevog vrha, $ly(i)$ oznaku $i$-tog desnog vrha, a $w(u,v)$ težinu brida između $u$-tog lijevog i $v$-tog desnog vrha.

Najprije inicijaliziramo dopustive oznake, npr.

$lx(i) = \max_{1\leq j\leq n} \{ w(i, j)\},\, ly(i) = 0$

Zatim odaberemo nespareni vrh i, kao kod najvećeg sparivanja, tražimo uvećavajući put. Ako ga nađemo, uvećamo sparivanje; inače dobivamo alternirajuće stablo.

Neka $S$ i $T$ označavaju lijeve odnosno desne vrhove bipartitnog grafa koji su u alternirajućem stablu, a $S'$ i $T'$ one koji nisu.

![bigraph-weight-match-1](./images/bigraph-weight-match-1.png)

U podgrafu jednakosti:

-   bridovi $S-T'$ ne postoje, inače bi alternirajuće stablo raslo;
-   bridovi $S'-T$ sigurno su nespareni, inače bi vrh pripadao $S$.

Pretpostavimo da oznakama vrhova u $S$ dodamo $-a$, a oznakama u $T$ dodamo $+a$. Tada:

-   bridovi $S-T$ i dalje ostaju u podgrafu jednakosti;
-   bridovi $S'-T'$ se ne mijenjaju;
-   za bridove $S-T'$ zbroj $lx + ly$ se smanjuje, pa mogu ući u podgraf jednakosti;
-   za bridove $S'-T$ zbroj $lx + ly$ raste, pa ne mogu ući u podgraf jednakosti.

Stoga za $a$ očito treba uzeti najmanju vrijednost među bridovima $S-T'$:

$a = \min \{ lx(u) + ly(v) - w(u,v) | u\in{S} , v\in{T'} \}$.

Kad novi brid $(u,v)$ uđe u podgraf jednakosti, moguća su dva slučaja:

-   $v$ je nesparen; tada smo našli uvećavajući put;
-   $v$ je već sparen s vrhom iz $S'$.

Tako nakon najviše $n$ promjena oznaka nalazimo uvećavajući put.

Pri svakoj promjeni oznaka bridovi alternirajućeg stabla ne napuštaju podgraf jednakosti, pa stablo možemo izravno održavati.

Za svaki vrh $v$ iz $T$ održavamo

$slack(v) = \min \{ lx(u) + ly(v) - w(u,v) | u\in{S} \}$.

Tako vrijednost $a$ za promjenu oznaka računamo u $O(n)$:

$a = \min \{ slack(v) | v\in{T'} \}$

Kad u alternirajuće stablo uđe novi vrh u $S$, treba $O(n)$ za ažuriranje $slack(v)$. Promjena oznaka traži $O(n)$ da bi se od svakog $slack(v)$ oduzelo $a$. Čim alternirajuće stablo dosegne nespareni vrh, našli smo uvećavajući put.

Na početku prolazimo $n$ vrhova tražeći uvećavajuće putove; za svaki treba $n$ proširenja alternirajućeg stabla, a svako proširenje $n$ koraka održavanja, ukupno $O(n^3)$.

??? note "Referentni kôd"
    ```cpp
    template <typename T>
    struct hungarian {  // km
      int n;
      vector<int> matchx;  // spareni vrhovi lijevog skupa
      vector<int> matchy;  // spareni vrhovi desnog skupa
      vector<int> pre;     // lijevi vrh povezan s desnim skupom
      vector<bool> visx;   // polje posjećenosti, lijevo
      vector<bool> visy;   // polje posjećenosti, desno
      vector<T> lx;
      vector<T> ly;
      vector<vector<T>> g;
      vector<T> slack;
      T inf;
      T res;
      queue<int> q;
      int org_n;
      int org_m;
    
      hungarian(int _n, int _m) {
        org_n = _n;
        org_m = _m;
        n = max(_n, _m);
        inf = numeric_limits<T>::max();
        res = 0;
        g = vector<vector<T>>(n, vector<T>(n));
        matchx = vector<int>(n, -1);
        matchy = vector<int>(n, -1);
        pre = vector<int>(n);
        visx = vector<bool>(n);
        visy = vector<bool>(n);
        lx = vector<T>(n, -inf);
        ly = vector<T>(n);
        slack = vector<T>(n);
      }
    
      void addEdge(int u, int v, int w) {
        g[u][v] = max(w, 0);  // negativna vrijednost je lošija od nesparivanja, pa postavljanje na 0 ništa ne mijenja
      }
    
      bool check(int v) {
        visy[v] = true;
        if (matchy[v] != -1) {
          q.push(matchy[v]);
          visx[matchy[v]] = true;  // in S
          return false;
        }
        // nađen novi nespareni vrh; ažuriramo sparivanje, polje pre pamti vrh povezan "nesparenim bridom"
        while (v != -1) {
          matchy[v] = pre[v];
          swap(v, matchx[pre[v]]);
        }
        return true;
      }
    
      void bfs(int i) {
        while (!q.empty()) {
          q.pop();
        }
        q.push(i);
        visx[i] = true;
        while (true) {
          while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (int v = 0; v < n; v++) {
              if (!visy[v]) {
                T delta = lx[u] + ly[v] - g[u][v];
                if (slack[v] >= delta) {
                  pre[v] = u;
                  if (delta) {
                    slack[v] = delta;
                  } else if (check(v)) {  // delta=0 znači da brid može ući u podgraf jednakosti; tražimo uvećavajući put
                                          // ako ga nađemo, return i ponovno gradimo alternirajuće stablo
                    return;
                  }
                }
              }
            }
          }
          // nema uvećavajućeg puta, mijenjamo oznake vrhova
          T a = inf;
          for (int j = 0; j < n; j++) {
            if (!visy[j]) {
              a = min(a, slack[j]);
            }
          }
          for (int j = 0; j < n; j++) {
            if (visx[j]) {  // S
              lx[j] -= a;
            }
            if (visy[j]) {  // T
              ly[j] += a;
            } else {  // T'
              slack[j] -= a;
            }
          }
          for (int j = 0; j < n; j++) {
            if (!visy[j] && slack[j] == 0 && check(j)) {
              return;
            }
          }
        }
      }
    
      void solve() {
        // početne oznake vrhova
        for (int i = 0; i < n; i++) {
          for (int j = 0; j < n; j++) {
            lx[i] = max(lx[i], g[i][j]);
          }
        }
    
        for (int i = 0; i < n; i++) {
          fill(slack.begin(), slack.end(), inf);
          fill(visx.begin(), visx.end(), false);
          fill(visy.begin(), visy.end(), false);
          bfs(i);
        }
    
        // custom
        for (int i = 0; i < n; i++) {
          if (g[i][matchx[i]] > 0) {
            res += g[i][matchx[i]];
          } else {
            matchx[i] = -1;
          }
        }
        cout << res << "\n";
        for (int i = 0; i < org_n; i++) {
          cout << matchx[i] + 1 << " ";
        }
        cout << "\n";
      }
    };
    ```

## Dinamički mađarski algoritam

Izvorni članak: [The Dynamic Hungarian Algorithm for the Assignment Problem with Changing Costs](https://www.ri.cmu.edu/publications/the-dynamic-hungarian-algorithm-for-the-assignment-problem-with-changing-costs/)

Članak s jasnijim pseudokodom: [A Fast Dynamic Assignment Algorithm for Solving Resource Allocation Problems](https://www.researchgate.net/publication/352490780_A_Fast_Dynamic_Assignment_Algorithm_for_Solving_Resource_Allocation_Problems)

Povezani zadatak na OJ-u: [DAP](https://www.spoj.com/problems/DAP/)

???+ note "Ideja algoritma"
    1.  Promjena težina između jednog vrha $u_i$ i svih $v_j$, tj. jednog retka matrice težina
        -   promijeni oznaku $lx(u_i) = max(w_{ij} - v_{j}), \forall j$
        -   ukloni sparivanje vrha $u_i$
    2.  Promjena težina između svih $u_i$ i jednog vrha $v_j$, tj. jednog stupca matrice težina
        -   promijeni oznaku $ly(v_j) = max(w_{ij} - u_{i}), \forall i$
        -   ukloni sparivanje vrha $v_j$
    3.  Promjena težine između jednog vrha $u_i$ i jednog vrha $v_j$, tj. jednog elementa matrice težina
        -   dovoljno je napraviti jednu od operacija 1 ili 2
    4.  Dodavanje jednog vrha $u_i$ ili jednog vrha $v_j$, tj. dodavanje ili uklanjanje jednog retka ili stupca matrice težina
        -   odgovarajuće napravi 1 ili 2; uočite da je dodavanje vrha ovdje samo dodavanje vrha, bez zadavanja težina – težine novog vrha prema ostalima su 0.

???+ note "Dokaz algoritma"
    -   Neka je izvorni graf G, oznake lijevih i desnih vrhova $\alpha^{i}$ i $\beta^{j}$, a dopustive oznake l; tada je $G_l$ podgraf grafa G koji sadrži vrhove i bridove grafa G za koje je $w_{ij} = alpha_{i}+beta_{j}$.
    -   U gornjem dijelu o mađarskom algoritmu Teorem 1 dokazuje: ako za neke dopustive oznake podgraf jednakosti ima perfektno sparivanje, to je sparivanje najveće težinsko perfektno sparivanje izvornog bipartitnog grafa.
    -   Pretpostavimo da je izvorno optimalno sparivanje $M^*$. Kad se dogodi promjena, dopustive oznake ažuriramo prema pravilima; ažurirane oznake označimo $\alpha^{i^*}$ odnosno $\beta^{j^*}$. Mogući su sljedeći slučajevi:
        1.  Promijenjen je cijeli redak matrice težina; neka je to redak $i^*$, tj. promijenjeni su svi bridovi vrha $v_{i^*}$, pa stara oznaka vrha $v_{i^*}$ možda ne zadovoljava uvjet, jer trebamo $w_{i^{*}j} \leq alpha_{i^*}+beta_{j}$. Za ostale vrhove $u_j$ težine bridova, osim onih povezanih s $i^*$, nisu se promijenile, pa su njihove oznake i dalje valjane. Zato algoritam mijenja oznaku vrha $v_{i^*}$ tako da oznake ponovno budu dopustive.
        2.  Promijenjen je cijeli stupac matrice težina; analogno, algoritam mijenja oznake tako da budu dopustive.
        3.  Promijenjen je jedan element matrice težina; dovoljno je promijeniti bilo koju od dviju oznaka da bi uvjet bio zadovoljen.
    -   Svaka promjena matrice težina odnosi se na jedan određeni vrh, koji može biti lijevi ili desni, pa ga označimo jednostavno $x$; taj je vrh u izvornom optimalnom sparivanju bio sparen s nekim vrhom $y$. Svaka promjena najviše rastavlja (unpair) taj par vrhova, pa je dovoljno pokrenuti jedan krug pretraživanja mađarskog algoritma da bismo dobili novo sparivanje (match), a prema Teoremu 1 novo je sparivanje optimalno.

Sljedeći kôd vjerojatno je kôd koji je predao autor članka 2 (ovo je inačica koja maksimizira težinu; u izvornom se članku minimizira cijena).

??? note "Referentni kôd dinamičkog mađarskog algoritma"
    ```cpp
    --8<-- "docs/graph/code/graph-matching/bigraph-weight-match/bigraph-weight-match_1.cpp"
    ```

## Pretvorba u model toka najmanje cijene

Slično kao [najveće sparivanje u bipartitnom grafu](./bigraph-match.md), i najveće težinsko sparivanje u bipartitnom grafu može se pretvoriti u problem mrežnog toka.

Najprije u graf dodamo izvor i ponor.

Iz izvora do svakog lijevog vrha bipartitnog grafa povučemo brid kapaciteta $1$ i cijene $0$; iz svakog desnog vrha bipartitnog grafa do ponora povučemo brid kapaciteta $1$ i cijene $0$.

Zatim za svaki brid bipartitnog grafa koji spaja lijevi vrh $u$ i desni vrh $v$ s težinom $w$ povučemo brid od $u$ do $v$ kapaciteta $1$ i cijene $w$.

Osim toga, budući da broj bridova u najvećem težinskom sparivanju ne mora biti jednak broju bridova najvećeg sparivanja, iz svakog lijevog vrha povučemo još i brid do ponora kapaciteta $1$ i cijene $0$.

Odgovor dobivamo računanjem [najvećeg toka najveće cijene](../flow/min-cost.md) u toj mreži. Najveći tok mreže tada je nužno jednak broju lijevih vrhova, a najveća cijena uz najveći tok odgovara najvećem težinskom sparivanju.

## Zadaci

??? note "[UOJ #80. 二分图最大权匹配](https://uoj.ac/problem/80)"
    Ogledni zadatak
    
    ```cpp
    --8<-- "docs/graph/code/graph-matching/bigraph-weight-match/bigraph-weight-match_2.cpp"
    ```
