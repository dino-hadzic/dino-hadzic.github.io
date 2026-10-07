---
title: Minimalni rez
---

## Pojmovi

### Rez

Za mrežu $G=(V,E)$ rez je definiran kao **particija skupa vrhova**: svi se vrhovi podijele u dva skupa, $S$ i $T=V-S$, pri čemu je izvor $s\in S$, a ponor $t\in T$.

### Kapacitet reza

Kapacitet reza $(S,T)$, u oznaci $c(S,T)$, definiramo kao zbroj kapaciteta svih bridova koji idu iz $S$ u $T$, tj. $c(S,T)=\sum_{u\in S,v\in T}c(u,v)$. Naravno, $c(S,T)$ možemo označavati i s $c(s,t)$.

### Minimalni rez

Minimalni rez (min cut) znači pronaći rez $(S,T)$ čiji je kapacitet $c(S,T)$ najmanji.

## Dokaz

### Teorem o maksimalnom toku i minimalnom rezu

Vidi odjeljak o teoremu o maksimalnom toku i minimalnom rezu na stranici [Maksimalni tok](max-flow.md).

## Kôd

### Minimalni rez

Po **teoremu o maksimalnom toku i minimalnom rezu** izravno dobivamo sljedeći kôd:

??? note "Primjer koda"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <cstring>
    #include <queue>
    
    constexpr int N = 1e4 + 5, M = 2e5 + 5;
    int n, m, s, t, tot = 1, lnk[N], ter[M], nxt[M], val[M], dep[N], cur[N];
    
    void add(int u, int v, int w) {
      ter[++tot] = v, nxt[tot] = lnk[u], lnk[u] = tot, val[tot] = w;
    }
    
    void addedge(int u, int v, int w) { add(u, v, w), add(v, u, 0); }
    
    int bfs(int s, int t) {
      memset(dep, 0, sizeof(dep));
      memcpy(cur, lnk, sizeof(lnk));
      std::queue<int> q;
      q.push(s), dep[s] = 1;
      while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int i = lnk[u]; i; i = nxt[i]) {
          int v = ter[i];
          if (val[i] && !dep[v]) q.push(v), dep[v] = dep[u] + 1;
        }
      }
      return dep[t];
    }
    
    int dfs(int u, int t, int flow) {
      if (u == t) return flow;
      int ans = 0;
      for (int &i = cur[u]; i && ans < flow; i = nxt[i]) {
        int v = ter[i];
        if (val[i] && dep[v] == dep[u] + 1) {
          int x = dfs(v, t, std::min(val[i], flow - ans));
          if (x) val[i] -= x, val[i ^ 1] += x, ans += x;
        }
      }
      if (ans < flow) dep[u] = -1;
      return ans;
    }
    
    int dinic(int s, int t) {
      int ans = 0;
      while (bfs(s, t)) {
        int x;
        while ((x = dfs(s, t, 1 << 30))) ans += x;
      }
      return ans;
    }
    
    int main() {
      scanf("%d%d%d%d", &n, &m, &s, &t);
      while (m--) {
        int u, v, w;
        scanf("%d%d%d", &u, &v, &w);
        addedge(u, v, w);
      }
      printf("%d\n", dinic(s, t));
      return 0;
    }
    ```

### Rekonstrukcija rješenja

Sve vrhove skupa $S$ možemo pronaći tako da iz izvora $s$ pokrenemo DFS i svaki put prolazimo samo bridovima čiji je preostali kapacitet veći od $0$.

```cpp
void dfs(int u) {
  vis[u] = 1;
  for (int i = lnk[u]; i; i = nxt[i]) {
    int v = ter[i];
    if (!vis[v] && val[i]) dfs(v);
  }
}
```

### Broj bridova u rezu

Ako tražimo rez s najmanjim brojem bridova, jednostavno postavimo kapacitete svih bridova na $1$ i jednom izračunamo minimalni rez. Ako tražimo minimalni rez s najmanjim brojem bridova, postoje dva pristupa:

1.  Kapacitet svakog brida $c(u,v)$ zamijenimo s $c(u,v)(|E| + 1) + 1$ i na novom grafu izračunamo minimalni rez; to je minimalni rez izvornog grafa s najmanje bridova. Kapacitet minimalnog reza novog grafa podijeljen s $|E| + 1$ i zaokružen nadolje daje minimalni rez izvornog grafa, a ostatak je broj bridova u rezu.

    To odgovara traženju leksikografski najmanjeg reza u kojem je veličina reza prvi, a broj bridova u rezu drugi ključ. Budući da je koeficijent $|E| + 1$ strogo veći od ukupnog broja bridova, a broj bridova u rezu ne premašuje ukupni broj bridova, broj bridova u rezu ne može, kakav god bio, poništiti utjecaj veličine reza, pa je dobiveni rez sigurno minimalni rez izvornog grafa; među minimalnim rezovima izvornog grafa onaj s najmanje bridova postaje minimalni rez novog grafa.

    Uočite da ispravnost ovog pristupa počiva na pretpostavci da su svi kapaciteti cijeli brojevi: samo tada broj bridova u rezu $k\le|E|<|E|+1$ sigurno ne „prenosi” u viši razred. Ako su kapaciteti racionalni, najprije ih pomnožimo zajedničkim nazivnikom da postanu cijeli; ako su kapaciteti proizvoljni realni brojevi ili bi cjelobrojni tip prelio, kapacitet jednostavno uzmemo kao uređeni par $(c(u,v),1)$, zbrajamo po komponentama, a uspoređujemo leksikografski. Tada svi algoritmi temeljeni na povećavajućim putovima koji se oslanjaju samo na zbrajanje, oduzimanje i uspoređivanje kapaciteta (npr. Dinicov algoritam) rade bez izmjena.

2.  Najprije izračunamo maksimalni tok grafa, a zatim gradimo novi graf: za svaki luk **rezidualne mreže** (tj. za luk u smjeru brida koji nije zasićen i za obrnuti luk brida koji nosi tok) dodamo brid kapaciteta $\infty$, a za svaki zasićeni brid dodamo brid kapaciteta $1$; ponovnim računanjem minimalnog reza dobivamo najmanji broj bridova u rezu.

    Bridovi minimalnog reza novog grafa sigurno ne uključuju bridove kapaciteta $\infty$, tj. nijedan rezidualni luk ne ide iz $S$ u $T$. Stoga su u minimalnom rezu novog grafa svi prednji bridovi izvornog grafa zasićeni, a svi stražnji bridovi bez toka, što znači da je njegov kapacitet jednak maksimalnom toku pa je sigurno minimalni rez izvornog grafa. Obrnuto, prednji bridovi svakog minimalnog reza izvornog grafa su zasićeni, pa je njegov kapacitet u novom grafu upravo broj njegovih bridova. Dakle, minimalni rez novog grafa je minimalni rez izvornog grafa s najmanje bridova.

    ??? warning "Česta pogreška: „postaviti na $\infty$ samo kapacitete nezasićenih bridova”"
        Ovaj pristup ima čestu pogrešnu inačicu: nakon računanja maksimalnog toka kapacitete zasićenih bridova postaviti na $1$, a nezasićenih na $\infty$, i izravno izračunati minimalni rez. To se čini intuitivnim, ali je zapravo pogrešno. Protuprimjer je na slici dolje.
        
        ![](images/min-cut-1.svg)
        
        Kao na slici, maksimalni tok iznosi $16$ (tj. svi izlazni bridovi iz $s$ su zasićeni), maksimalni tok je jedinstven, a jedino brid $A\to B$ nije zasićen. Svaki minimalni rez izvornog grafa ima $3$ brida, ali nakon pogrešnog postavljanja kapaciteta minimalni rez novog grafa iznosi $2$ i postiže se za $S = \{s,x,y,B\}$. Kapacitet tog reza je $20$, pa to nije minimalni rez izvornog grafa: njegovi prednji bridovi $s\to A$ i $B\to t$ jesu zasićeni, ali brid $A\to B$, koji nosi tok, ide sa strane $T$ natrag na stranu $S$, a pogrešna inačica taj slučaj ne isključuje. U ispravnom pristupu $A\to B$ nosi tok, pa se dodaje obrnuti brid $B\to A$ kapaciteta $\infty$, koji sprječava pojavu tog pogrešnog minimalnog reza.

## Model problema 1

Zadano je $n$ predmeta i dva skupa $A,B$. Ako predmet nije stavljen u skup $A$, to stoji $a_i$, a ako nije stavljen u skup $B$, stoji $b_i$; uz to postoji nekoliko ograničenja oblika $u_i,v_i,w_i$ koja znače da stoji $w_i$ ako $u_i$ i $v_i$ nisu u istom skupu. Svaki predmet mora pripadati točno jednom skupu; treba odrediti najmanji trošak.

Ovo je klasičan zadatak s minimalnim rezom tipa **izbor jedne od dviju mogućnosti**. Za dva skupa postavimo izvor $s$ i ponor $t$; iz $s$ u $i$-ti vrh povučemo brid kapaciteta $a_i$, a iz $i$-tog vrha u $t$ brid kapaciteta $b_i$. Za ograničenje $u,v,w$ između $u$ i $v$ povučemo dvosmjerni brid kapaciteta $w$.

Uočimo da, kad izvor i ponor nisu povezani, to znači da je svaki vrh izabrao jedan od skupova. Prerezati brid prema $s$ ili $t$ znači ne staviti predmet u $A$ odnosno $B$, a prerezati brid između dvaju predmeta znači da ta dva predmeta nisu u istom skupu.

Minimalni rez je najmanji trošak.

## Model problema 2

Zatvoreni podgraf maksimalne težine: zadan je usmjereni graf u kojem svaki vrh ima težinu (pozitivnu, negativnu ili $0$); treba odabrati podgraf najveće ukupne težine takav da su svi sljedbenici svakog vrha podgrafa također u podgrafu.

Postupak: uvedemo superizvor $s$ i superponor $t$. Ako vrh $u$ ima pozitivnu težinu, iz $s$ u $u$ povučemo usmjereni brid čija je težina jednaka težini vrha; ako vrh $u$ ima negativnu težinu, iz $u$ u $t$ povučemo usmjereni brid čija je težina suprotna težini vrha. Težine svih bridova izvornog grafa postavimo na $\infty$. Izračunamo maksimalni tok; odgovor je zbroj svih pozitivnih težina umanjen za maksimalni tok.

Nekoliko kratkih tvrdnji za dokaz:

1.  Svaki dopustivi podgraf odgovara jednom rezu u mreži. Svaki rez dijeli mrežu na dva dijela, a iz dijela povezanog sa $s$ nijedan brid ne vodi u drugi dio, pa je gornji uvjet zadovoljen. Ova je tvrdnja i nužna i dovoljna.
2.  Bridovi koje minimalni rez uklanja moraju biti incidentni s $s$ ili s $t$, jer bi im inače težina bila $\infty$ i ne bi mogli biti u minimalnom rezu.
3.  Za odabrani podgraf vrijedi: ukupna težina $=$ zbroj svih pozitivnih težina $-$ zbroj težina neodabranih vrhova pozitivne težine $+$ zbroj težina odabranih vrhova negativne težine. Kad ne odaberemo vrh pozitivne težine, prekida se njegov brid prema $s$; kad odaberemo vrh negativne težine, prekida se njegov brid prema $t$. Zbroj težina prekinutih bridova je kapacitet reza. Stoga gornja formula postaje: ukupna težina $=$ zbroj svih pozitivnih težina $-$ kapacitet reza.
4.  Zaključak: maksimalna ukupna težina $=$ zbroj svih pozitivnih težina $-$ minimalni rez $=$ zbroj svih pozitivnih težina $-$ maksimalni tok.

## Zadaci za vježbu

-   [„USACO 4.4” Pollutant Control](https://www.luogu.com.cn/problem/P1344)
-   [„USACO 5.4” Telecowmunication](https://www.luogu.com.cn/problem/P1345)
-   [„Luogu 1361” Usjevi malog M](https://www.luogu.com.cn/problem/P1361)
-   [„SHOI 2007” Dobronamjerno glasanje](https://www.luogu.com.cn/problem/P2057)
-   [Plan svemirskih letova](https://www.luogu.com.cn/problem/P2762)
