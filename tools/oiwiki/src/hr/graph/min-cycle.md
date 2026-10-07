---
title: Najmanji ciklus
---

## Uvod

???+ question "Problem"
    Zadan je graf; kolika je najmanja suma težina bridova ciklusa koji se sastoji od $n$ vrhova $(n\ge 3)$?

Najmanji ciklus grafa zove se i struk (girth) grafa.

## Postupak

### Rješenje grubom silom

Neka između $u$ i $v$ postoji brid duljine $w$, a $dis(u,v)$ neka označava najkraći put između $u$ i $v$ nakon što se obriše brid između $u$ i $v$.

Tada je najmanji ciklus u neusmjerenom grafu $dis(u,v)+w$.

Pazi: ako najmanji ciklus tražimo u usmjerenom grafu, formulu treba prilagoditi – najmanji ciklus je $dis(v,u)+w$.

Ukupna vremenska složenost $O(n^2m)$.

### Dijkstra

Povezano: [Najkraći put/Dijkstra](./shortest-path.md#dijkstrin-algoritam)

#### Postupak

Prolazimo po svim bridovima; za svaki obrišemo taj brid i iz njegova početnog vrha pokrenemo Dijkstru, po istom načelu kao gore.

#### Svojstva

Vremenska složenost $O(m(n+m)\log n)$.

### Floyd

Povezano: [Najkraći put/Floyd](./shortest-path.md#floydov-algoritam)

#### Postupak

Težinu brida između $u,v$ u izvornom grafu označimo s $val\left(u,v\right)$.

Primijetimo svojstvo Floydova algoritma: kad vanjska petlja dođe do vrha $k$ (prije nego što $k$-ta iteracija počne), u polju najkraćih putova $dis$ vrijednost $dis_{u,v}$ predstavlja najkraći put od $u$ do $v$ koji prolazi samo kroz vrhove s indeksima u intervalu $\left[1, k\right)$.

Po definiciji najmanji ciklus ima barem tri vrha; neka je $w$ njegov vrh s najvećim indeksom, a $u,v$ dva vrha susjedna vrhu $w$ na ciklusu. Tada, kad vanjska petlja dođe do $k=w$, duljina tog ciklusa iznosi $dis_{u,v}+val\left(v,w\right)+val\left(w,u\right)$.

Stoga u petlji za svaki $k$ prolazimo po parovima $(i,j)$ s $i<k,j<k$ i ažuriramo odgovor.

#### Zapisivanje puta

Sada znamo da ciklus ima oblik $u\to k\to v$, pa se iz $v$ vraća u $u$ (prolazeći samo kroz vrhove s indeksima $<k$).

Problem se svodi na traženje puta $v\leadsto u$. Iz nejednakosti trokuta $dis_{u,v}\le dis_{u,i}+dis_{i,v}$ pamtimo $pos_{u,v}=j$, vrh za koji vrijedi $dis_{u,v}=dis_{u,j}+dis_{j,v}$. Očito je $j$ na putu $v\leadsto u$.

Put se tako dijeli na dva dijela, $v\leadsto j$ i $j\leadsto u$, koje obrađujemo rekurzivno.

???+ note "Dokaz da rekurzija ne upada u beskonačnu petlju"
    Dokazujemo kontradikcijom.
    
    Pretpostavimo da ciklus prolazi kroz neki vrh $u$ dvaput. Tada na ciklusu postoji dio koji iz $u$ nakon nekoliko bridova opet dolazi u $u$, a to je novi ciklus.
    
    Budući da u grafu nema negativnih ciklusa (da ih ima, najmanji ciklus ne bi postojao), suma težina novog ciklusa nužno je manja ili jednaka sumi izvornog.
    
    Dakle, dovoljno je uzeti samo taj ciklus, i tada se vrh $u$ ne ponavlja; pretpostavka ne vrijedi, pa ciklus ne prolazi dvaput kroz isti vrh.
    
    Zato, kad rekurzija dođe do vrhova $u,v$, njihov $pos_{u,v}$ sigurno nije jednak ni jednom od njih, tj. dodaje se novi vrh.
    
    Posebno, ako su $u$ i $v$ susjedni, odmah se vraćamo.
    
    Kako je ukupan broj vrhova $n$, broj dodavanja (tj. rekurzivnih poziva) ne premašuje $n$, pa rekurzija ne upada u beskonačnu petlju.

#### Svojstva

Vremenska složenost: $O(n^3)$.

#### Implementacija

Referentne implementacije u C++-u i Pythonu (sa zapisivanjem puta):

=== "C++"
    ```cpp
    // graf ima n vrhova
    int val[MAXN + 1][MAXN + 1];  // matrica susjedstva izvornog grafa
    int cnt, path[MAXN + 5];      // put i duljina najmanjeg ciklusa
    
    void get_path(int u, int v) {  // dohvaća put od u do v
      if (pos[u][v] == 0) return;
    
      int k = pos[u][v];
      get_path(u, k);
      path[++cnt] = k;
      get_path(k, v);
    }
    
    void Floyd(const int &n) {
      static int dis[MAXN + 1][MAXN + 1];  // matrica najkraćih putova
      static int pos[MAXN + 1][MAXN + 1];
      memcpy(dis, val, sizeof(val));
      memset(pos, 0, sizeof(pos));
      for (int k = 1; k <= n; ++k) {
        for (int i = 1; i < k; ++i)
          for (int j = 1; j < i; ++j)
            if (ans >
                (long long)val[i][k] + val[k][j] + dis[i][j]) {  // pronađen kraći ciklus
              // Budući da je ovdje osigurano j<i<k, tri su vrha različita i nema ciklusa duljine nula.
              ans = val[i][k] + val[k][j] + dis[i][j], cnt = 0;
              path[++cnt] = i, path[++cnt] = k,
              path[++cnt] = j;  // redom dodajemo vrhove i,k,j
              get_path(j, i);   // dodajemo put od j do i
            }
    
        for (int i = 1; i <= n; ++i)  // uobičajeno Floydovo ažuriranje najkraćih putova
          for (int j = 1; j <= n; ++j) {
            if (dis[i][j] > dis[i][k] + dis[k][j]) {
              dis[i][j] = dis[i][k] + dis[k][j];
              pos[i][j] = k;  // trenutni put dobiven je preko k
            }
          }
      }
    }
    ```

=== "Python"
    ```python
    # Dovoljno velika vrijednost koja predstavlja beskonačnost
    INF = sys.maxsize
    
    
    def get_path(i, j, pos, path, cnt):
        """
        Rekurzivno dohvaća međuvrhove na najkraćem putu od vrha i do vrha j.
    
        Args:
            i (int): početni vrh (0-based index).
            j (int): završni vrh (0-based index).
            pos (list[list[int]]): matrica međuvrhova najkraćih putova. pos[i][j] = k znači da najkraći put od i do j prolazi kroz k.
            path (list[int]): lista u koju se spremaju vrhovi puta (0-based index).
            cnt (int): trenutni broj vrhova na putu.
    
        Returns:
            int: ažurirani broj vrhova na putu.
        """
        # Ako je pos[i][j] jednak -1, između i i j nema međuvrhova
        if pos[i][j] == -1:
            return cnt
    
        # Dohvati međuvrh k
        k = pos[i][j]
        # Rekurzivno dohvati put od i do k
        cnt = get_path(i, k, pos, path, cnt)
        # Dodaj međuvrh k na put
        path[cnt] = k
        cnt += 1
        # Rekurzivno dohvati put od k do j
        cnt = get_path(k, j, pos, path, cnt)
        return cnt
    
    
    def find_minimum_cycle_undirected(n, edges):
        """
        Pronalazi najmanji ciklus u neusmjerenom grafu Floyd–Warshallovim algoritmom.
    
        Args:
            n (int): broj vrhova grafa (1 do n).
            edges (list[tuple]): lista bridova; svaki je element (u, v, w) i znači da između vrhova u i v postoji brid težine w.
                                 Indeksi vrhova su od 1 do n.
    
        Returns:
            tuple: duljina i put najmanjeg ciklusa.
                   Ako ciklus ne postoji, vraća (INF, []).
                   Put je lista indeksa vrhova (1-based index).
        """
        # Interno koristimo 0-based indeksiranje
        N = n
        # Inicijaliziraj matricu susjedstva g s težinama izvornih bridova
        g = [[INF for _ in range(N)] for _ in range(N)]
        # Inicijaliziraj matricu najkraćih putova dis, u početku jednaku g
        dis = [[INF for _ in range(N)] for _ in range(N)]
        # Inicijaliziraj matricu pos s međuvrhovima najkraćih putova
        pos = [[-1 for _ in range(N)] for _ in range(N)]
    
        # Dijagonalu postavi na 0 (udaljenost vrha do samog sebe)
        for i in range(N):
            g[i][i] = 0
            dis[i][i] = 0
    
        # Izgradi matricu susjedstva iz ulaznih bridova (neusmjereni graf)
        for u, v, w in edges:
            # Pretvori 1-based indekse u 0-based
            u -= 1
            v -= 1
            # U neusmjerenom grafu bridovi su dvosmjerni
            g[u][v] = min(g[u][v], w)
            g[v][u] = min(g[v][u], w)
            dis[u][v] = min(dis[u][v], w)
            dis[v][u] = min(dis[v][u], w)
    
        # Duljinu najmanjeg ciklusa postavi na beskonačno
        min_cycle_len = INF
        # Inicijaliziraj put najmanjeg ciklusa
        min_cycle_path = []
    
        # Glavni dio Floyd–Warshallova algoritma
        # k je međuvrh (0-based index)
        for k in range(N):
            # Prije ažuriranja dis[i][j] provjeri daje li vrh k manji ciklus
            # Ciklus je oblika i -> k -> j -> ... -> i
            # Ovdje je dis[i][j] najkraći put koji kao međuvrhove koristi samo vrhove 0 do k-1
            # C++ kôd koristi petlje s i < k i j < i; ovdje slijedimo istu logiku (0-based)
            for i in range(k):  # 0 <= i < k
                for j in range(i):  # 0 <= j < i
                    # Provjeri tvore li i, k, j ciklus zatvoren preko dis[i][j]
                    # Izvorni bridovi g[i][k] i g[k][j] moraju postojati (nisu INF)
                    # i najkraći put dis[i][j] od i do j mora postojati (nije INF)
                    if g[i][k] != INF and g[k][j] != INF and dis[i][j] != INF:
                        current_cycle_len = g[i][k] + g[k][j] + dis[i][j]
                        if current_cycle_len < min_cycle_len:
                            min_cycle_len = current_cycle_len
                            # Rekonstruiraj put
                            path = [0] * (N + 5)  # privremeni niz za put, dovoljno velik
                            cnt = 0
                            # Dodaj na put redom i, k, j
                            path[cnt] = i
                            cnt += 1
                            path[cnt] = k
                            cnt += 1
                            path[cnt] = j
                            cnt += 1
                            # Dohvati međuvrhove najkraćeg puta od j do i (iz već izračunatih dis i pos)
                            cnt = get_path(j, i, pos, path, cnt)
                            # Izdvoji stvarne vrhove puta (odbaci neiskorišteni dio)
                            # Pretvori 0-based indekse u 1-based
                            min_cycle_path = [node + 1 for node in path[:cnt]]
    
            # Standardno Floyd–Warshallovo ažuriranje najkraćih putova
            for i in range(N):
                for j in range(N):
                    if (
                        dis[i][k] != INF
                        and dis[k][j] != INF
                        and dis[i][j] > dis[i][k] + dis[k][j]
                    ):
                        dis[i][j] = dis[i][k] + dis[k][j]
                        # Zabilježi da najkraći put od i do j prolazi kroz k
                        pos[i][j] = k
    
        return min_cycle_len, min_cycle_path
    ```

## Predložak zadatka

??? note "[AcWing 344 Turistički obilazak](https://www.acwing.com/problem/content/346)"
    Zadan je neusmjereni graf s $n$ vrhova; nađi u njemu ciklus s barem $3$ vrha, bez ponavljanja vrhova, čija je suma duljina bridova najmanja.
    
    Taj se problem zove problem najmanjeg ciklusa u neusmjerenom grafu.
    
    Treba ispisati sam najmanji ciklus; ako nije jedinstven, može se ispisati bilo koji.
    
    $n \le 100$

Vremenska složenost dopušta $O(n^3)$, pa izravno primjenjujemo Floydovo traženje najmanjeg ciklusa.

=== "C++"
    ```cpp
    #include <bits/stdc++.h>
    using lint = long long;
    // Dovoljno velika konstanta za najveći broj vrhova grafa
    const int MAXN = 110;
    
    // Dovoljno velika vrijednost za beskonačnost; početna duljina najmanjeg ciklusa
    lint ans = 1e9;  // lint je alias za long long
    
    // broj vrhova n i broj bridova m grafa
    // cnt je broj vrhova na putu najmanjeg ciklusa
    // path sprema vrhove puta najmanjeg ciklusa
    int n, m, cnt, path[MAXN];
    
    // g je matrica susjedstva izvornog grafa
    // dis je matrica najkraćih putova (ažurira se tijekom Floyd–Warshallova algoritma)
    // pos bilježi međuvrhove najkraćih putova; pos[i][j] = k znači da najkraći put od i do j prolazi kroz k
    int g[MAXN][MAXN], dis[MAXN][MAXN], pos[MAXN][MAXN];
    
    // Rekurzivna funkcija: dohvaća međuvrhove najkraćeg puta od vrha u do vrha v
    // Rekonstruira put prema matrici pos
    void get_path(int u, int v) {
      // Ako je pos[u][v] jednak 0, između u i v nema međuvrhova; odmah se vraćamo
      if (pos[u][v] == 0) return;
    
      // Dohvati međuvrh k
      int k = pos[u][v];
      // Rekurzivno dohvati put od u do k
      get_path(u, k);
      // Dodaj međuvrh k na put
      path[++cnt] = k;
      // Rekurzivno dohvati put od k do v
      get_path(k, v);
    }
    
    // Funkcija Floyd–Warshallova algoritma: traži najmanji ciklus u grafu
    void Floyd() {
      // Vanjska petlja: k je međuvrh (1 do n)
      for (int k = 1; k <= n; ++k) {
        // Unutarnje petlje: i i j, provjeravamo daje li vrh k manji ciklus
        // Petlje idu i od 1 do k-1, j od 1 do i-1
        // Tako provjeravamo cikluse oblika i -> k -> j -> ... -> i
        for (int i = 1; i < k; ++i)
          for (int j = 1; j < i; ++j)
            // Provjeri daje li spajanje i i j preko vrha k manji ciklus
            // Duljina ciklusa je težina izvornog brida od i do k, g[i][k], + težina izvornog brida od k do j, g[k][j]
            // + trenutni najkraći put od i do j, dis[i][j]
            if (ans > (long long)g[i][k] + g[k][j] + dis[i][j]) {
              // Pronađen manji ciklus
              ans = g[i][k] + g[k][j] + dis[i][j];  // ažuriraj duljinu najmanjeg ciklusa
              cnt = 0;                              // resetiraj brojač puta
              // Dodaj na put redom i, k, j
              path[++cnt] = i, path[++cnt] = k, path[++cnt] = j;
              // Dohvati međuvrhove najkraćeg puta od j do i i dodaj ih na put
              get_path(j, i);
            }
    
        // Standardno Floyd–Warshallovo ažuriranje najkraćih putova
        // i od 1 do n, j od 1 do n
        for (int i = 1; i <= n; ++i)
          for (int j = 1; j <= n; ++j) {
            // Ako preko međuvrha k dobivamo kraći put od i do j
            if (dis[i][j] > dis[i][k] + dis[k][j]) {
              // Ažuriraj najkraći put
              dis[i][j] = dis[i][k] + dis[k][j];
              // Zabilježi da najkraći put od i do j prolazi kroz k
              pos[i][j] = k;
            }
          }
      }
    }
    
    // Glavna funkcija
    int main() {
      // Učitaj broj vrhova n i broj bridova m
      std::cin >> n >> m;
      // Inicijaliziraj izvornu matricu susjedstva g: sve težine na beskonačno (0x3f obično predstavlja vrlo velik broj)
      memset(g, 0x3f, sizeof(g));
      // Udaljenost vrha do samog sebe postavi na 0
      for (int i = 1; i <= n; ++i) g[i][i] = 0;
      // Učitaj m bridova i izgradi izvornu matricu susjedstva g
      // U neusmjerenom grafu bridovi su dvosmjerni; uzimamo manju težinu
      for (int i = 0, u, v, w; i < m; ++i) {
        std::cin >> u >> v >> w;
        g[u][v] = g[v][u] = std::min(g[u][v], w);
      }
      // Kopiraj izvornu matricu susjedstva g u matricu najkraćih putova dis
      memcpy(dis, g, sizeof(g));
      // Pozovi Floydov algoritam za traženje najmanjeg ciklusa
      Floyd();
      // Prema duljini najmanjeg ciklusa odluči postoji li ciklus
      if (ans == 1e9) {  // Ako je duljina najmanjeg ciklusa i dalje beskonačna, ciklusa nema
        puts("No solution.");
      } else {
        // Ako ciklus postoji, ispiši vrhove puta
        // std::cout << "ans = " << ans << std::endl; // ispis duljine najmanjeg ciklusa (zakomentirano)
        // Ispiši vrhove puta odvojene razmacima
        for (int i = 1; i <= cnt; ++i)
          std::cout << path[i]
                    << (i == cnt ? "" : " ");  // nakon posljednjeg vrha nema razmaka
        std::cout << std::endl;                // novi red nakon ispisa puta
      }
      return 0;
    }
    ```

=== "Python"
    ```python
    import copy
    import sys
    
    # Dovoljno velika vrijednost koja predstavlja beskonačnost
    INF = sys.maxsize
    
    
    def get_path(i, j, pos, path, cnt):
        """
        Rekurzivno dohvaća međuvrhove na najkraćem putu od vrha i do vrha j.
    
        Args:
            i (int): početni vrh (0-based index).
            j (int): završni vrh (0-based index).
            pos (list[list[int]]): matrica međuvrhova najkraćih putova. pos[i][j] = k znači da najkraći put od i do j prolazi kroz k.
            path (list[int]): lista u koju se spremaju vrhovi puta (0-based index).
            cnt (int): trenutni broj vrhova na putu.
    
        Returns:
            int: ažurirani broj vrhova na putu.
        """
        # Ako je pos[i][j] jednak -1, između i i j nema međuvrhova
        if pos[i][j] == -1:
            return cnt
    
        # Dohvati međuvrh k
        k = pos[i][j]
        # Rekurzivno dohvati put od i do k
        cnt = get_path(i, k, pos, path, cnt)
        # Dodaj međuvrh k na put
        path[cnt] = k
        cnt += 1
        # Rekurzivno dohvati put od k do j
        cnt = get_path(k, j, pos, path, cnt)
        return cnt
    
    
    def find_minimum_cycle_undirected(n, edges):
        """
        Pronalazi najmanji ciklus u neusmjerenom grafu Floyd–Warshallovim algoritmom.
    
        Args:
            n (int): broj vrhova grafa (1 do n).
            edges (list[tuple]): lista bridova; svaki je element (u, v, w) i znači da između vrhova u i v postoji brid težine w.
                                 Indeksi vrhova su od 1 do n.
    
        Returns:
            tuple: duljina i put najmanjeg ciklusa.
                   Ako ciklus ne postoji, vraća (INF, []).
                   Put je lista indeksa vrhova (1-based index).
        """
        # Interno koristimo 0-based indeksiranje
        N = n
        # Inicijaliziraj matricu susjedstva g s težinama izvornih bridova
        g = [[INF for _ in range(N)] for _ in range(N)]
        # Inicijaliziraj matricu najkraćih putova dis, u početku jednaku g
        dis = [[INF for _ in range(N)] for _ in range(N)]
        # Inicijaliziraj matricu pos s međuvrhovima najkraćih putova
        pos = [[-1 for _ in range(N)] for _ in range(N)]
    
        # Dijagonalu postavi na 0 (udaljenost vrha do samog sebe)
        for i in range(N):
            g[i][i] = 0
            dis[i][i] = 0
    
        # Izgradi matricu susjedstva iz ulaznih bridova (neusmjereni graf)
        for u, v, w in edges:
            # Pretvori 1-based indekse u 0-based
            u -= 1
            v -= 1
            # U neusmjerenom grafu bridovi su dvosmjerni
            g[u][v] = min(g[u][v], w)
            g[v][u] = min(g[v][u], w)
            dis[u][v] = min(dis[u][v], w)
            dis[v][u] = min(dis[v][u], w)
    
        # Duljinu najmanjeg ciklusa postavi na beskonačno
        min_cycle_len = INF
        # Inicijaliziraj put najmanjeg ciklusa
        min_cycle_path = []
    
        # Glavni dio Floyd–Warshallova algoritma
        # k je međuvrh (0-based index)
        for k in range(N):
            # Prije ažuriranja dis[i][j] provjeri daje li vrh k manji ciklus
            # Ciklus je oblika i -> k -> j -> ... -> i
            # Ovdje je dis[i][j] najkraći put koji kao međuvrhove koristi samo vrhove 0 do k-1
            # C++ kôd koristi petlje s i < k i j < i; ovdje slijedimo istu logiku (0-based)
            for i in range(k):  # 0 <= i < k
                for j in range(i):  # 0 <= j < i
                    # Provjeri tvore li i, k, j ciklus zatvoren preko dis[i][j]
                    # Izvorni bridovi g[i][k] i g[k][j] moraju postojati (nisu INF)
                    # i najkraći put dis[i][j] od i do j mora postojati (nije INF)
                    if g[i][k] != INF and g[k][j] != INF and dis[i][j] != INF:
                        current_cycle_len = g[i][k] + g[k][j] + dis[i][j]
                        if current_cycle_len < min_cycle_len:
                            min_cycle_len = current_cycle_len
                            # Rekonstruiraj put
                            path = [0] * (N + 5)  # privremeni niz za put, dovoljno velik
                            cnt = 0
                            # Dodaj na put redom i, k, j
                            path[cnt] = i
                            cnt += 1
                            path[cnt] = k
                            cnt += 1
                            path[cnt] = j
                            cnt += 1
                            # Dohvati međuvrhove najkraćeg puta od j do i (iz već izračunatih dis i pos)
                            cnt = get_path(j, i, pos, path, cnt)
                            # Izdvoji stvarne vrhove puta (odbaci neiskorišteni dio)
                            # Pretvori 0-based indekse u 1-based
                            min_cycle_path = [node + 1 for node in path[:cnt]]
    
            # Standardno Floyd–Warshallovo ažuriranje najkraćih putova
            for i in range(N):
                for j in range(N):
                    if (
                        dis[i][k] != INF
                        and dis[k][j] != INF
                        and dis[i][j] > dis[i][k] + dis[k][j]
                    ):
                        dis[i][j] = dis[i][k] + dis[k][j]
                        # Zabilježi da najkraći put od i do j prolazi kroz k
                        pos[i][j] = k
    
        return min_cycle_len, min_cycle_path
    
    
    # --- Glavni program ---
    if __name__ == "__main__":
        # Učitaj broj vrhova n i broj bridova m
        n, m = map(int, sys.stdin.readline().split())
    
        # Učitaj bridove
        edges = []
        for _ in range(m):
            u, v, w = map(int, sys.stdin.readline().split())
            edges.append((u, v, w))
    
        # Pronađi najmanji ciklus
        min_len, path = find_minimum_cycle_undirected(n, edges)
    
        # Ispiši rezultat
        if min_len == INF:
            print("No solution.")
        else:
            # Ispiši vrhove puta (1-based index) odvojene razmacima
            print(" ".join(map(str, path)))
    ```

## Primjer 2

GDOI2018 Day2 Patrola

Zadan je neusmjereni graf s $n$ vrhova bez bridova negativne težine; treba izvršiti $q$ operacija triju vrsta:

1.  obriši vrh grafa i sve bridove uz njega;
2.  vrati obrisani vrh i sve bridove uz njega;
3.  upit: koliki je najmanji ciklus koji sadrži vrh $x$.

Za $50\%$ testova vrijedi $n,q \le 100$.

Za svaki jednostavan ciklus koji sadrži vrh $x$ postoje dva brida susjedna vrhu $x$; brišemo li bilo koji od njih, jednostavan ciklus postaje jednostavan put.

Dakle, prolazimo po svim bridovima susjednima vrhu $x$, svaki put obrišemo jedan od njih i pokrenemo Dijkstru.

Ili za svaki upit izravno pokrenemo Floydovo traženje najmanjeg ciklusa, $O(qn^3)$.

Za $100\%$ testova vrijedi $n,q \le 400$.

Opet koristimo Floydov algoritam za najmanji ciklus.

Kad ne bi bilo brisanja, brisanje upitnog vrha razbija jednostavan ciklus u jednostavan put.

No drugi korak računamo Floydom.

Odgovor je, dakle, udaljenost između bilo koja dva vrha pod uvjetom da se ne prolazi kroz upitni vrh $x$.

Kako to raditi online?

Idemo nasilu offline i offline pristupom izbjegavamo operacije brisanja.

Upite poredamo vremenski i nad njima izgradimo segment tree.

Vrijeme postojanja svakog vrha pokriva sve upite osim onih u kojima se pita za taj vrh; ako se neki vrh pita $x$ puta, njegovo vrijeme postojanja može se promatrati kao $x + 1$ intervala koje ubacujemo u segment tree.

Zatim obiđemo cijeli segment tree: pri ulasku u čvor spremimo kopiju Floydova polja, dodamo sve vrhove ubačene u taj interval, a pri izlasku se vratimo na spremljenu kopiju.

Vremenska složenost ovog pristupa je $O(qn^2\log q)$.

Postoji i online pristup s boljom vremenskom složenošću.

Za upit o vrhu $x$ pokrenemo najkraće putove iz $x$, izgradimo stablo najkraćih putova i usput za svaki vrh odredimo u kojem je podstablu vrha $x$.

Tada sigurno postoji nestablasti brid čiji su krajevi u različitim podstablima korijena, takav da taj brid $+$ putovi od njegovih krajeva do korijena čine najmanji ciklus.

Dokaz:

Očito najmanji ciklus sadrži barem jedan nestablasti brid čiji su krajevi u različitim podstablima korijena.

Neka je to brid $(u,v)$; put od $x$ do $u$ u stablu najkraćih putova najkraći je od svih putova od $x$ do $u$, a isto vrijedi i za put od $x$ do $v$, pa ciklus $x\to u\to v\to x$ sigurno nije dulji od najmanjeg ciklusa.

Dakle, prolazimo po svim nestablastim bridovima i ažuriramo odgovor.

Složenost svakog upita jednaka je složenosti jednog traženja najkraćih putova iz jednog izvora, $O(n^2)$.

Ukupna vremenska složenost je $O(qn^2)$.
