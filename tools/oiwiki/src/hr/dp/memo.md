---
title: Memoizirano pretraživanje
---

## Definicija

Memoizirano pretraživanje način je implementacije pretraživanja koji zapisuje informacije o već obiđenim stanjima i tako izbjegava ponovno obilaženje istog stanja.

Budući da memoizirano pretraživanje osigurava da se svako stanje posjeti samo jednom, ono je ujedno i uobičajen način implementacije dinamičkog programiranja.

## Uvod

???+ note "[\[NOIP2005\] Skupljanje ljekovitog bilja](https://www.luogu.com.cn/problem/P1048)"
    U špilji raste $M$ različitih ljekovitih biljaka; skupljanje svake traži neko vrijeme $t_i$, a svaka ima i svoju vrijednost $v_i$. Zadano vam je vrijeme $T$ u kojem možete skupiti neke biljke. Treba maksimizirati ukupnu vrijednost skupljenih biljaka.
    
    $1 \leq T \leq 10^3$, $1 \leq t_i,v_i,M \leq 100$

### Naivni pristup [DFS-om](../search/dfs.md)

Lako je implementirati ovakvo naivno pretraživanje: tijekom pretraživanja pamtimo tri parametra — koji predmet trenutno razmatramo, koliko je vremena preostalo i koliku smo vrijednost već skupili — a zatim nabrajamo je li trenutni predmet odabran i prelazimo u odgovarajuće stanje.

???+ note "Implementacija"
    === "C++"
        ```cpp
        int n, t;
        int tcost[103], mget[103];
        int ans = 0;
        
        void dfs(int pos, int tleft, int tans) {
          if (tleft < 0) return;
          if (pos == n + 1) {
            ans = max(ans, tans);
            return;
          }
          dfs(pos + 1, tleft, tans);
          dfs(pos + 1, tleft - tcost[pos], tans + mget[pos]);
        }
        
        int main() {
          cin >> t >> n;
          for (int i = 1; i <= n; i++) cin >> tcost[i] >> mget[i];
          dfs(1, t, 0);
          cout << ans << endl;
          return 0;
        }
        ```
    
    === "Python"
        ```python
        tcost = [0] * 103
        mget = [0] * 103
        ans = 0
        
        
        def dfs(pos, tleft, tans):
            global ans
            if tleft < 0:
                return
            if pos == n + 1:
                ans = max(ans, tans)
                return
            dfs(pos + 1, tleft, tans)
            dfs(pos + 1, tleft - tcost[pos], tans + mget[pos])
        
        
        t, n = map(lambda x: int(x), input().split())
        for i in range(1, n + 1):
            tcost[i], mget[i] = map(lambda x: int(x), input().split())
        dfs(1, t, 0)
        print(ans)
        ```

Vremenska složenost ovog pristupa eksponencijalna je i njime se ovaj zadatak ne može riješiti.

### Optimizacija

Zašto je gornji pristup neučinkovit? Zato što se isto stanje posjećuje više puta.

Ako nakon obrade svakog stanja spremimo njegove informacije, pri sljedećem posjetu tom stanju možemo izravno iskoristiti prije izračunate informacije i tako izbjeći ponovno računanje. To u potpunosti iskorištava činjenicu da mnogi problemi dinamičkog programiranja imaju velik broj preklapajućih potproblema i pripada ideji „memoizacije”: zamjeni vremena prostorom.

Konkretno, u ovom zadatku naivnom DFS-u dodajemo niz `mem` u koji zapisujemo povratnu vrijednost svakog `dfs(pos,tleft)`. Na početku sve vrijednosti u `mem` postavimo na `-1` (što znači „još nije riješeno”). Svaki put kad trebamo posjetiti neko stanje, ako je njegova vrijednost u `mem` jednaka `-1`, rekurzivno ga posjetimo. Inače izravno upotrijebimo već spremljenu vrijednost iz `mem`.

Takvom obradom osiguravamo da se svako stanje posjeti samo jednom, pa je vremenska složenost algoritma $O(TM)$.

???+ note "Implementacija"
    === "C++"
        ```cpp
        int n, t;
        int tcost[103], mget[103];
        int mem[103][1003];
        
        int dfs(int pos, int tleft) {
          if (mem[pos][tleft] != -1)
            return mem[pos][tleft];  // već posjećeno stanje: odmah vrati prije zapisanu vrijednost
          if (pos == n + 1) return mem[pos][tleft] = 0;
          int dfs1, dfs2 = -INF;
          dfs1 = dfs(pos + 1, tleft);
          if (tleft >= tcost[pos])
            dfs2 = dfs(pos + 1, tleft - tcost[pos]) + mget[pos];  // prijelaz stanja
          return mem[pos][tleft] = max(dfs1, dfs2);  // na kraju spremi vrijednost trenutnog stanja
        }
        
        int main() {
          memset(mem, -1, sizeof(mem));
          cin >> t >> n;
          for (int i = 1; i <= n; i++) cin >> tcost[i] >> mget[i];
          cout << dfs(1, t) << endl;
          return 0;
        }
        ```
    
    === "Python"
        ```python
        tcost = [0] * 103
        mget = [0] * 103
        mem = [[-1 for i in range(1003)] for j in range(103)]
        
        
        def dfs(pos, tleft):
            if mem[pos][tleft] != -1:
                return mem[pos][tleft]
            if pos == n + 1:
                mem[pos][tleft] = 0
                return mem[pos][tleft]
            dfs1 = dfs2 = -INF
            dfs1 = dfs(pos + 1, tleft)
            if tleft >= tcost[pos]:
                dfs2 = dfs(pos + 1, tleft - tcost[pos]) + mget[pos]
            mem[pos][tleft] = max(dfs1, dfs2)
            return mem[pos][tleft]
        
        
        t, n = map(lambda x: int(x), input().split())
        for i in range(1, n + 1):
            tcost[i], mget[i] = map(lambda x: int(x), input().split())
        print(dfs(1, t))
        ```

## Veza i razlika u odnosu na iterativni pristup

Pri rješavanju problema dinamičkog programiranja kôd memoiziranog pretraživanja i kôd iterativnog (rekurentnog) pristupa oblikom su vrlo slični. Razlog je to što koriste isti način prikaza stanja i slične prijelaze stanja. Upravo zato su, općenito, vremenske složenosti obiju implementacija jednake.

U nastavku je kôd iterativne implementacije (radi lakše usporedbe bez optimizacije kružnim nizom); usporedbom se lako uočava sličnost u obliku.

```cpp
int n, t, w[105], v[105], f[105][1005];

int main() {
  cin >> n >> t;
  for (int i = 1; i <= n; i++) cin >> w[i] >> v[i];
  for (int i = 1; i <= n; i++)
    for (int j = 0; j <= t; j++) {
      f[i][j] = f[i - 1][j];
      if (j >= w[i])
        f[i][j] = max(f[i][j], f[i - 1][j - w[i]] + v[i]);  // jednadžba prijelaza stanja
    }
  cout << f[n][t];
  return 0;
}
```

Pri rješavanju problema dinamičkog programiranja i memoizirano pretraživanje i iterativni pristup osiguravaju da se isto stanje riješi najviše jednom. Način na koji to postižu ipak se malo razlikuje: iterativni pristup izbjegava ponovne posjete propisivanjem jasnog redoslijeda posjeta, dok memoizirano pretraživanje, iako ne propisuje redoslijed posjeta, isti cilj postiže označavanjem već posjećenih stanja.

U usporedbi s iterativnim pristupom, memoizirano pretraživanje ne mora propisivati redoslijed posjeta, pa je ponekad lakše za implementaciju i prikladno rješava rubne slučajeve; to mu je velika prednost. S druge strane, u memoiziranom pretraživanju teško je primijeniti optimizacije poput kružnog niza, a zbog rekurzije izvođenje je sporije nego kod iterativnog pristupa. Zato prikladniji način implementacije treba birati ovisno o zadatku.

## Kako napisati memoizirano pretraživanje

### Metoda 1

1.  Napiši DP stanja i jednadžbu za zadatak
2.  po njima napiši funkciju dfs
3.  dodaj niz za memoizaciju

Primjer:

$dp_{i} = \max\{dp_{j}+1\}\quad (1 \leq j < i \land a_{j}<a_{i})$ (najdulji rastući podniz)

postaje

=== "C++"
    ```cpp
    int dfs(int i) {
      if (mem[i] != -1) return mem[i];
      int ret = 1;
      for (int j = 1; j < i; j++)
        if (a[j] < a[i]) ret = max(ret, dfs(j) + 1);
      return mem[i] = ret;
    }
    
    int main() {
      memset(mem, -1, sizeof(mem));
      // učitavanje izostavljeno
      int ret = 0;
      for (int j = 1; j <= n; j++) {
        ret = max(ret, dfs(j));
      }
      cout << ret << endl;
    }
    ```

=== "Python"
    ```python
    def dfs(i):
        if mem[i] != -1:
            return mem[i]
        ret = 1
        for j in range(1, i):
            if a[j] < a[i]:
                ret = max(ret, dfs(j) + 1)
        mem[i] = ret
        return mem[i]
    ```

### Metoda 2

1.  Napiši program grube sile za zadatak (najbolje [dfs](../search/dfs.md))
2.  pretvori taj dfs u dfs „bez vanjskih varijabli”
3.  dodaj niz za memoizaciju

Primjer: primjer „Skupljanje ljekovitog bilja” iz ovog članka
