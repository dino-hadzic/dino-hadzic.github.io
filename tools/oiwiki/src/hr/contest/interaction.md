---
title: Interaktivni zadaci
---

Interaktivni zadaci pojavljivali su se na IOI-ju još u prošlom stoljeću. Iako se posljednjih godina nisu pojavljivali na natjecanjima ispod razine pokrajinskog izbora, 2019. su se na natjecanjima NOI serije zaredom pojavila dva interaktivna zadatka, „P5208 [WC2019] I 君的商店” i „P5473 [NOI2019] I 君的探险”, što možda znači da se interaktivni zadaci vraćaju u natjecanja NOI serije.

Interaktivni zadaci nemaju velike zahtjeve u pogledu prethodnog znanja algoritama i obično nemaju stroga vremenska ograničenja; kvaliteta programa često ovisi samo o ograničenju broja interakcija. Zato se pri učenju interaktivnih zadataka preporučuje napredovati postupno prema težini. Ako želite vježbati algoritamsko razmišljanje, a ne samo učiti algoritme, rješavanje interaktivnih zadataka vrlo je dobar način. Iako interaktivni zadaci obično ne zahtijevaju mnogo već usvojenih algoritama, ipak se preporučuje da ih počnete rješavati tek nakon što svladate određeni broj algoritama naprednije razine (NOIP senior i pokrajinski izbor), jer su tada vaše algoritamsko razmišljanje i širina znanja već na određenoj razini. Osnovni uvod u interaktivne zadatke možete pronaći u odjeljku **OI Wikija** [Vrste zadataka – interaktivni zadaci](./problems.md#交互题).

Posebne greške kod interaktivnih zadataka:

-   Natjecatelj nakon svakog ispisa mora isprazniti međuspremnik (flush), inače dolazi do greške Idleness limit exceeded. Osim toga, ako zadatak ima više testnih skupina i program može znati odgovor prije nego što učita sve podatke, svejedno mora učitati sve podatke, jer će inače zbog pomiješanog učitavanja također nastati ILE (može se postaviti više upita odjednom i zatim odjednom primiti odgovore na sve upite). Također, po mogućnosti nemojte koristiti brzo učitavanje.
-   Ako program postavi previše upita, Codeforces daje presudu Wrong Answer (ali sustav za ocjenjivanje navodi razlog za Wrong Answer), dok UVa daje presudu Protocol Limit Exceeded (PLE).
-   Ako je format interakcije programa pogrešan, UVa daje presudu Protocol Violation (PV).

Budući da su ulaz i izlaz u interaktivnim zadacima prilično zamršeni, preporučuje se zasebno enkapsulirati funkcije za učitavanje i ispis.

Ako na natjecanju autor zadatka priloži grader zaglavlje (za ispravljanje grader interaktivnih zadataka) ili checker program (za ispravljanje stdio interaktivnih zadataka), ispravljanje interaktivnog zadatka razmjerno je jednostavno, jer je stress testiranje interaktivnih zadataka mnogo teže od stress testiranja običnih zadataka. Bez `testlib.h` stdio interaktivna biblioteka za zadatak s mnogo detalja interakcije obično ima oko 3k koda, a uz još 3k za stress tester, za implementaciju treba barem sat vremena. No bez obzira na to postoji li program za ispravljanje, pri ispravljanju koda interaktivnog zadatka natjecatelj obično mora sam simulirati proces interakcije s programom; zato interaktivni zadaci zahtijevaju da natjecatelj zna osmisliti kvalitetan program, da ga po mogućnosti napiše točno iz prvog pokušaja te da ima dobru sposobnost statičkog traženja pogrešaka.

Primjeri zadataka:

-   [CF679A Bear and Prime 100](https://codeforces.com/problemset/problem/679/A)
-   [CF843B Interactive LowerBound](https://codeforces.com/problemset/problem/843/B)
-   [UOJ206\[APIO2016\]Gap](http://uoj.ac/problem/206)
-   [CF750F New Year and Finding Roots](https://codeforces.com/problemset/problem/750/F)
-   [UVa12731 Mysterious Space Station](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=823&page=show_problem&problem=4584)

## CF679A Bear and Prime 100

Svaki prost broj ima točno dva djelitelja, pa izravno nabrajamo djelitelje traženog broja. Ograničenje je najviše 20 upita, a pri pokušaju rastavljanja većih brojeva (npr. 92) na proste faktore vidimo da treba nabrojati proste brojeve najviše do $\lfloor\frac{n}{2}\rfloor$. Zato najprije sitom izdvojimo proste brojeve do 50 i svaki put upitamo za sve njih.

Budući da je stress testiranje u ovom zadatku jednostavno, možemo isprobati sve brojeve iz raspona. Primijetit ćemo da program ne obrađuje ispravno kvadrate prostih brojeva. Zato dodajemo i kvadrate brojeva 2, 3, 5, 7, tj. 4, 9, 25, 49 – ukupno 19 brojeva, što zadovoljava uvjete zadatka.

??? note "Referentni kod"
    ```cpp
    #include <cstdio>
    constexpr int prime[] = {2,  3,  4,  5,  7,  9,  11, 13, 17, 19,
                             23, 25, 29, 31, 37, 41, 43, 47, 49};
    int cnt = 0;
    char res[5];
    
    int main() {
      for (int i : prime) {
        printf("%d\n", i);
        fflush(stdout);
        scanf("%s", res);
        if (res[0] == 'y' && ++cnt == 2) return printf("composite"), 0;
      }
      printf("prime");
      return 0;
    }
    ```

## CF843B Interactive LowerBound

Vezana lista ima najviše $5 \times 10 ^ 4$ elemenata, ali smijemo postaviti samo $1999$ upita i možemo dobiti samo sljedbenika elementa, pa obični obilazak cijele liste ne dolazi u obzir. Postoji samo jedan način da se izravno približimo položaju traženog elementa: nasumično odabrati točke.

Za $n < 2000$ izravno nabrajamo; za $n \ge 2000$ nasumično odaberemo 1000 točaka – tada je očekivana udaljenost među tim točkama vrlo mala, pa možemo krenuti od najveće vrijednosti manje od $x$ i obilaziti dalje; može se dokazati da ćemo dobiti odgovor prije nego što stignemo do sljedeće odabrane točke. Čim tijekom obilaska nađemo element veći ili jednak $x$, možemo odmah izaći.

Iako je ukupna ideja jednostavna, u praksi, ako niste učili nesavršene randomizirane algoritme poput simuliranog kaljenja, do nje je vjerojatno teže doći.

Istodobno, budući da Codeforces ima mehanizam hackanja, mnogi namjerno ruše kod koji ne inicijalizira sjeme generatora slučajnih brojeva, pa prije poziva `random_shuffle()` treba staviti `srand((size_t)new char)`.

??? note "Referentni kod"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <cstdlib>
    constexpr int N = 50005;
    int n, start, x;
    int a[N];
    
    int main() {
      scanf("%d%d%d", &n, &start, &x);
      if (n < 2000) {
        int ans = 2e9;
        for (int i = 1; i <= n; i++) {
          printf("? %d\n", i), fflush(stdout);
          int val, next;
          scanf("%d%d", &val, &next);
          if (val >= x) ans = std::min(ans, val);
        }
        if (ans == 2e9) ans = -1;
        printf("! %d", ans), fflush(stdout);
      } else {
        srand((size_t) new char);
        int p = start, ans = 0;
        for (int i = 1; i <= n; i++) a[i] = i;
        std::random_shuffle(a + 1, a + n + 1);
        for (int i = 1; i <= 1000; i++) {
          printf("? %d\n", a[i]), fflush(stdout);
          int val, next;
          scanf("%d%d", &val, &next);
          if (val < x && val > ans) p = a[i], ans = val;
        }
        while (p != -1 && ans < x) {
          printf("? %d\n", p), fflush(stdout);
          int val, next;
          scanf("%d%d", &val, &next);
          ans = val;
          p = next;
        }
        if (ans < x) ans = -1;
        printf("! %d", ans), fflush(stdout);
      }
      return 0;
    }
    ```

## UOJ206\[APIO2016]Gap

Razmatramo dva podzadatka:

1.  Ograničenje broja upita.

    Razmotrimo prvi upit. Budući da na početku ne znamo nijedan broj, moramo upitati za raspon $[1, 10 ^ {18}]$ i dobiti najveću i najmanju vrijednost.

    Budući da je ograničenje broja upita točno $\frac{N + 1}{2}$, razmišljamo kako svakim upitom dobiti vrijednosti koje još nismo dobili, tako da otprilike unutar dopuštenog broja upita dobijemo sve brojeve niza. Metoda je jednostavna: nakon svakog upita $[s, t]$, ako su dobivene vrijednosti $mn, mx$, sljedeći je upit $[mn + 1, mx - 1]$.

2.  Ograničenje veličine upitnih intervala.

    Budući da zadatak traži da zbroj broja brojeva unutar upitnih intervala ne prelazi $3N$, razmišljamo o minimiziranju upitnih intervala. Gornja metoda više nije upotrebljiva jer je zbroj broja brojeva u njezinim upitnim intervalima reda $O(N ^ 2)$. Mogli bismo razmotriti binarno dijeljenje raspona vrijednosti, ali ta metoda nije pouzdana – u najgorem slučaju može biti srušena na $O(N ^ 2)$. Zato nam treba učinkovitiji način podjele raspona vrijednosti koji izbjegava ponovno upitivanje točaka iz već upitanih intervala i time rasipanje prilika.

    Budući da odgovor nije manji od $\lfloor\frac{a_n - a_1}{N - 1}\rfloor$, možemo raspon vrijednosti dijeliti prema toj vrijednosti: neka je $i$ na početku 0, a $ans$ na početku jednak gornjoj vrijednosti; svaki put upitamo $[i, i + ans]$ i ažuriramo $ans$, a zatim povećamo $i$ s korakom $ans$.

    No ni ta se metoda ne može dobro primijeniti na podzadatak 1, jer u najgorem slučaju mnogi upiti u svom rasponu možda ne sadrže nijedan broj.

??? note "Referentni kod"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    
    #include "gap.h"
    
    long long findGap(int T, int N) {
      static long long a[100005] = {}, ans = 0;
      long long s = 0, t = 1e18, s1, t1;
      if (T == 1) {
        int l = 1, r = N;
        while (l <= r) {
          MinMax(s, t, &s1, &t1);
          a[l++] = s1, a[r--] = t1;
          s = s1 + 1, t = t1 - 1;
        }
        for (int i = 2; i <= N; i++) ans = std::max(ans, a[i] - a[i - 1]);
      } else if (T == 2) {
        MinMax(s, t, &s1, &t1);
        ans = (t1 - s1) / (N - 1);
        long long l = s1 + 1, r = t1, last = s1;
        for (long long i = l; i <= r;) {
          MinMax(i, i + ans, &s1, &t1);
          i += ans + 1;
          if (s1 != -1) ans = std::max(ans, s1 - last), last = t1;
        }
      }
      return ans;
    }
    ```

## CF750F New Year and Finding Roots

Vidjevši stroge uvjete $h \le 7$ i broj upita $\le 16$, moramo vrlo strogo maksimalno iskoristiti informacije dobivene pristupima.

Za $h \le 4$ možemo izravno upotrijebiti grubu silu. No za $h > 4$ treba vrlo učinkovit algoritam obilaska.

Nasumično odabiranje točaka nije dobra metoda, jer njime ne možemo utvrditi jesmo li dovoljno blizu korijena, a pri čistom nasumičnom odabiru vjerojatnost da barem jednom pogodimo korijen iznosi $1 - (\frac{2 ^ h - 2}{2 ^ h - 1})$; čak i ako isključimo ponavljanje istih točaka, vjerojatnost da pogodimo korijen i dalje je vrlo mala.

Budući da je $1 \le k \le 3$ i ne znamo koja je strana bliža korijenu, razmatramo najgori slučaj: kad je $k = 3$, prva dva smjera obilaska udaljavaju se od korijena, a tek treći se približava korijenu. Zato moramo obići sva tri smjera.

Razmotrimo dvije metode obilaska, BFS i DFS. Budući da stablo pretraživanja BFS-a može biti vrlo veliko, prednost dajemo DFS-u. Naravno, ako znamo trenutačnu dubinu i ona je toliko mala da je veličina stabla pretraživanja unutar tog raspona dubina manja ili jednaka preostalom broju upita, možemo izravno upotrijebiti BFS.

Poznavanje dubine trenutačnog vrha i smjera trenutačnog obilaska daje veliku prednost. No vrlo je teško znati idemo li trenutačno prema korijenu ili prema listovima. Ako koristimo DFS, smjer saznajemo tek kad obilazak dođe do korijena ($k = 2$) ili do lista ($k = 1$). Zato moramo što je više moguće znati dubinu trenutačnog vrha i ne smijemo koristiti metode poput iterativnog produbljivanja koje se zaustavljaju usred obilaska.

Razmotrimo nasumičan početni vrh; krenuvši od njega možemo naići na gore opisani najgori slučaj.

Ako je $k = 1$, odmah znamo dubinu trenutačnog vrha.

Ako je $k = 2$, trenutačni je vrh korijen.

Ako je $k = 3$, izravno razmatramo DFS u sva tri smjera. Dva od tih smjerova vode izravno prema listovima i duljine su im putova jednake; treći smjer vodi prema korijenu, ali usput možda nehotice skrene prema listovima, pa će put obilaska biti dulji. Tada možemo izračunati dubinu trenutačnog vrha.

Kad je $k = 1$ ili $k = 3$, moramo razmotriti dulji put obilaska. Možemo odrediti vrh najmanje dubine na tom putu (sigurno je manje dubine od početnog vrha). Ako posjećene vrhove označimo i više ih ne obilazimo, od tog vrha postoji samo jedan put obilaska. Iako taj put možda i dalje vodi prema listovima, na njemu također nužno postoji vrh dubine manje od polazišta, pa od tog vrha možemo ponavljati gornje korake.

Naravno, promotrimo li najgori slučaj za $h = 7$ (svaki put napravimo samo jedan korak prema korijenu, a zatim odmah krenemo prema listovima), vidjet ćemo da je samo s DFS-om u najgorem slučaju potrebno $\frac{(1 + 7) \times 7}{2} = 28$ upita. No već znamo dubinu početnog vrha, pa možemo izračunati dubine svih obiđenih vrhova i, prema našem početnom razmatranju o BFS-u, provjeriti možemo li od vrha najmanje dubine izravno krenuti s BFS-om.

Tada izračunamo da je u najgorem slučaju potrebno 17 upita. Zato razmatramo kako iz stabla pretraživanja ukloniti jedan vrh (budući da DFS može samo slijepo obilaziti, razmatramo BFS): kad radimo BFS dubine $k$, stablo pretraživanja u najgorem slučaju ima $2 ^ k - 1$ vrhova i možda treba $2 ^ k - 1$ upita da utvrdimo koji vrh ima točno 2 susjeda. No ako smo već upitali $2 ^ k - 2$ od tih vrhova, znamo da posljednji vrh sigurno mora biti korijen.

Optimalno rješenje u najgorem slučaju tada je: za $h = 7$ krećemo DFS-om od lista, svaki put napravimo samo jedan korak prema korijenu i zatim odmah krenemo prema listovima; nakon 10 upita trenutačno poznati vrh najmanje dubine ima dubinu 4, a budući da mu znamo roditelja, od roditelja izravno krećemo s BFS-om (dubina stabla pretraživanja je 3, broj vrhova $2 ^ 3 - 1 = 7$). Nakon $2 ^ 3 - 2 = 6$ upita u BFS-u utvrdimo da je posljednji vrh u BFS stablu pretraživanja korijen.

Tako naš algoritam u najgorem slučaju stane točno u 16 upita.

??? note "Referentni kod"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <queue>
    #include <vector>
    using namespace std;
    constexpr int N = 256 + 5;
    int T, h, chance;
    bool ok;
    vector<int> to[N], path;
    
    bool read(int x) {
      if (to[x].empty()) {
        printf("? %d\n", x), fflush(stdout);
        int k, t;
        scanf("%d", &k);
        if (k == 0) exit(0);
        for (int i = 0; i < k; i++) {
          scanf("%d", &t);
          to[x].push_back(t);
        }
        if (k == 2) {
          printf("! %d\n", x), fflush(stdout);
          return ok = true;
        }
        chance--;
      }
      return false;
    }
    
    bool dfs(int x) {
      if (to[x].empty()) path.push_back(x);
      if (read(x)) return true;
      for (int i : to[x])
        if (to[i].empty()) return dfs(i);
      return false;
    }
    
    void bfs(int s, int k) {
      queue<int> q;
      for (int i : to[s])
        if (to[i].empty()) q.push(i);
      for (int i = 1; i < k; i++) {
        int x = q.front();
        q.pop();
        if (read(x)) return;
        for (int j : to[x])
          if (to[j].empty()) q.push(j);
      }
      for (int i = 1; i < k; i++) {
        int x = q.front();
        q.pop();
        if (read(x)) return;
      }
      printf("! %d\n", q.front()), fflush(stdout);
    }
    
    int main() {
      for (scanf("%d", &T); T--;) {
        ok = false;
        for (int i = 0; i < N; i++) to[i].clear();
        chance = 16;
        scanf("%d", &h);
        if (h == 0) exit(0);
        vector<int> long_path;
        if (read(1)) continue;
        int root, dep;
        if (to[1].size() == 1)
          root = 1, dep = h;
        else {
          for (int i : to[1]) {
            path.clear();
            if (dfs(i)) break;
            if (path.size() > long_path.size()) swap(path, long_path);
          }
          if (ok) continue;
          dep = h - (path.size() + long_path.size()) / 2;
          root = long_path.at((long_path.size() - (h - dep)) - 1);
        }
        while ((1 << (dep - 1)) - 2 > chance) {
          path.clear();
          if (dfs(root)) break;
          dep = h - (h - dep + path.size()) / 2;
          root = path.at((path.size() - (h - dep)) - 1);
        }
        if (!ok) bfs(root, 1 << (dep - 2));
      }
      return 0;
    }
    ```

## UVa12731 Mysterious Space Station

Budući da je jedina povratna informacija to jesmo li pri pomicanju udarili u zid, trebamo razmotriti kako, pod uvjetom da se robot ne izgubi, hodati što bliže zidu; to ima nekoliko prednosti:

-   Hodajući uz zid lako znamo hoćemo li udariti u zid, pa dobivamo što više informacija.
-   Polja uz zid nikad ne sadrže teleporte, pa izbjegavamo da se robot izgubi.

Dakle, ako znamo da bi robot mogao biti na nekom položaju uz zid, a želimo utvrditi je li doista ondje, možemo to učiniti [„pravilom jedne ruke na zidu”](https://en.wikipedia.org/wiki/Maze_solving_algorithm). Prema topološkom načelu, u labirintu u kojem su s obje strane zidovi, ako uđemo na ulaz i stalno jednom rukom dodirujemo isti zid, sigurno ćemo pronaći izlaz. Budući da je zid u ovom zadatku zatvoren, dovoljno je hodati stazom uz zid da bismo se sigurno vratili u polazište bez udaranja u zid. Osim toga, budući da je staza uz zid najveći zatvoreni krug na karti, u stvarnom kodu ne treba namjerno udarati u zid da bismo osigurali da je robot uz zid; stazu uz zid možemo označiti na karti. A čim udarimo u zid, trebamo se brzo vratiti istim putem – time izbjegavamo gubitak robota i smanjujemo broj koraka.

Iz toga izvodimo metodu pokušaja i pogreške za utvrđivanje je li robot na određenom polju: robota, ne stupajući na nepoznata polja ni na poznate teleporte, dovedemo na stazu uz zid, a zatim obiđemo krug stazom uz zid. Ako pritom ne udarimo u zid, možemo biti sigurni da je robot doista na određenom polju.

Gornjom metodom možemo na početku označiti sva nepoznata polja na karti, a zatim odozgo prema dolje i slijeva nadesno redom provjeravati je li svako nepoznato polje teleport. Najprije dođemo iznad nepoznatog polja, zatim se pomaknemo dolje pa lijevo. Gornjom metodom provjerimo je li robot lijevo od nepoznatog polja. Ako nije, robot nije ondje gdje bi trebao biti, tj. nepoznato polje je teleport.

Nakon što pronađemo nepoznata polja, treba utvrditi uparivanje 2k nepoznatih polja; metoda je jednostavna: dovoljno je uparivati grubom silom. Budući da je $k \le 5$, potrebno je najviše $9 + 7 + 5 + 3$ pokušaja. Za usporedbu, provjera svih nepoznatih polja na karti zahtijeva najviše $121 - 40$ pokušaja.

Donji kod trenutačno prolazi samo zrcalni zadatak na UOJ-u: [#247.【Rujia Liu's Present 7】Mysterious Space Station](http://uoj.ac/problem/247), a ne prolazi izvorni zadatak na UVa. Ni nakon izmjene službenog rješenja Rujie Liua s UOJ-a nije prošao, a Rujiu Liua zasad nije moguće kontaktirati. Zato se donji kod ravna prema UOJ-u.

Ipak, službeno rješenje Rujie Liua znatno je kvalitetnije od donjeg koda; na UOJ-u se može pogledati [službeno rješenje koje prolazi zrcalni zadatak na UOJ-u](http://uoj.ac/submission/105789). Na istim podacima službeno rješenje koristi vrlo malo poteza.

??? note "Referentni kod"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <cstring>
    #include <iostream>
    #include <queue>
    #include <stack>
    
    #define Wall 0
    #define Unknown 1
    #define Space 2
    #define Gate 3
    #define Path 4
    
    const int N = 20;
    const int dir[8][2] = {{0, 1},  {1, 0}, {0, -1}, {-1, 0},
                           {-1, 1}, {1, 1}, {1, -1}, {-1, -1}};
    const char dirs[5] = "ESWN";
    int n, m, k;
    int a[N][N], id[N][N];
    
    struct point {
      int x, y;
    
      point(int x = 0, int y = 0) : x(x), y(y) {}
    
      bool operator==(const point& tmp) const { return x == tmp.x && y == tmp.y; }
    
      bool operator!=(const point& tmp) const { return !(*this == tmp); }
    
      point side(int d) const { return point(x + dir[d][0], y + dir[d][1]); }
    
      int check(int d) { return a[x + dir[d][0]][y + dir[d][1]]; }
    
      int id() { return ::id[x][y]; }
    } start;
    
    std::vector<std::pair<point, int>> path;
    std::pair<point, point> ans[N];
    std::pair<point, bool> vis[N];
    
    bool walk(int d) {
      printf("MoveRobot %c\n", dirs[d]);
      fflush(stdout);
      int ret;
      scanf("%d", &ret);
      return ret;
    }
    
    bool walk(int d, std::stack<int>& st) {
      if (walk(d)) {
        st.push(d);
        return true;
      }
      return false;
    }
    
    bool read() {
      if (scanf("%d%d%d", &n, &m, &k) != 3) return false;
      if (n == 0) return false;
      memset(a, 0, sizeof(a));
      for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) {
          char c;
          std::cin >> c;
          if (c == 'S') start = point(i, j);
          if (c == '*')
            a[i][j] = Wall;
          else
            a[i][j] = Unknown;
        }
      return true;
    }
    
    void answer() {
      for (int i = 0; i < k; i++)
        printf("Answer %d %d\n", ans[i].first.id(), ans[i].second.id());
      fflush(stdout);
    }
    
    // Pravilo jedne ruke na zidu: budući da je Path uz zid najveći zatvoreni krug,
    // dovoljno je da pri hodu duž Path ne naiđemo na prepreku
    void wall_follower_init(point x, int last, int wallside, point s) {
      if (x == s && !path.empty()) return;
      if (x.check(wallside) == Path) {
        path.push_back(std::make_pair(x, wallside));
        wall_follower_init(x.side(wallside), wallside, last ^ 2, s);
      } else if (x.check(last) == Wall) {
        for (int i = 0; i < 4; i++)
          if (i != (last ^ 2) && x.check(i) != Wall) {
            path.push_back(std::make_pair(x, i));
            wall_follower_init(x.side(i), i, last, s);
            return;
          }
      } else {
        path.push_back(std::make_pair(x, last));
        wall_follower_init(x.side(last), last, wallside, s);
      }
    }
    
    void init() {
      int cnt = 1;
      for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) {
          if (a[i][j] == Unknown) {
            id[i][j] = cnt++;
            for (int k = 0; k < 8; k++)
              if (point(i, j).check(k) == Wall) {
                a[i][j] = Path;
                break;
              }
          } else
            id[i][j] = 0;
        }
      path.clear();
      int wallside = 0, last = 0;
      for (int i = 0; i < 4; i++)
        if (start.check(i) == Wall) {
          wallside = i;
          break;
        }
      for (int i = 0; i < 4; i++)
        if (start.check(i) == Path && i != (wallside ^ 2)) {
          last = i;
          break;
        }
      wall_follower_init(start, last, wallside, start);
    }
    
    void undo(std::stack<int>& st) {
      while (!st.empty()) walk(st.top() ^ 2), st.pop();
    }
    
    bool wall_follower(point x) {
      std::stack<int> st;
      bool ok = true;
      int i = 0;
      while (i < path.size() && path[i].first != x) i++;
      for (int j = i; ok && j < path.size(); j++) {
        if (walk(path[j].second))
          st.push(path[j].second);
        else
          ok = false;
      }
      for (int j = 0; ok && j < i; j++) {
        if (walk(path[j].second))
          st.push(path[j].second);
        else
          ok = false;
      }
      if (!ok) undo(st);
      return ok;
    }
    
    // Utvrđuje da smo trenutačno na x: metodom „korak po korak” dovoljno je
    // smjerovima koji izbjegavaju prepreke, nepoznata polja i teleporte doći do
    // Path. Koristi se pri traženju teleporta i njihovu uparivanju
    void bfs(point s, point t, std::vector<int>& v) {
      static int map[N][N] = {};
      memset(map, -1, sizeof(map));
      std::queue<point> q;
      map[s.x][s.y] = 4;
      q.push(s);
      while (!q.empty()) {
        point x = q.front();
        q.pop();
        if (x == t) break;
        for (int i = 0; i < 4; i++) {
          point y = x.side(i);
          if ((x.check(i) == Path || x.check(i) == Space) && map[y.x][y.y] == -1) {
            map[y.x][y.y] = i;
            q.push(y);
          }
        }
      }
      for (point x = t; x != s; x = x.side(map[x.x][x.y] ^ 2)) {
        v.push_back(map[x.x][x.y]);
      }
      std::reverse(v.begin(), v.end());
    }
    
    bool move(point s, point t, std::stack<int>& st) {  // koristi se blizu teleporta
      static std::vector<int> v;
      v.clear();
      bfs(s, t, v);
      for (int i : v)
        if (!walk(i, st)) return false;
      return true;
    }
    
    // što brže se pomakni prema zidu
    bool make_sure(point x, int last) {
      if (a[x.x][x.y] == Path) return wall_follower(x);
      for (int i = 0; i < 4; i++)
        if ((x.check(i) == Path || x.check(i) == Space) && i != (last ^ 2)) {
          if (!walk(i)) return false;
          bool ret = make_sure(x.side(i), i);
          walk(i ^ 2);
          return ret;
        }
      return false;
    }
    
    void find_gate() {
      int cnt = 0;
      std::stack<int> st;
      for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
          if (cnt == k * 2 && a[i][j] == Unknown)
            a[i][j] = Space;
          else if (a[i][j] == Unknown) {
            bool ok = true;
            if (!move(start, point(i - 1, j), st))
              ok = false;
            else if (!walk(1, st))
              ok = false;
            else if (!walk(2, st))
              ok = false;
            else if (!make_sure(point(i, j - 1), -1))
              ok = false;
            if (!ok) {
              vis[cnt++] = std::make_pair(point(i, j), false);
              a[i][j] = Gate;
              for (int k = 0; k < 8; k++) {
                point y = point(i, j).side(k);
                if (point(i, j).check(k) == Unknown) a[y.x][y.y] = Space;
              }
            } else
              a[i][j] = Space;
            undo(st);
          }
    }
    
    void make_gate_pair() {
      int cnt = 0;
      std::stack<int> st;
      for (int i = 0; i < k * 2; i++)
        if (!vis[i].second)
          for (int j = 0; !vis[i].second && j < k * 2; j++)
            if (j != i && !vis[j].second) {
              bool ok = true;
              if (!move(start, vis[i].first.side(2), st))
                ok = false;
              else if (!walk(0, st))
                ok = false;
              else if (!make_sure(vis[j].first.side(0), -1))
                ok = false;
              if (ok) {
                ans[cnt++] = std::make_pair(vis[i].first, vis[j].first);
                vis[i].second = vis[j].second = true;
              }
              undo(st);
            }
    }
    
    int main() {
      while (read()) {
        init();
        find_gate();
        make_gate_pair();
        answer();
      }
      return 0;
    }
    ```

## Zadaci za vježbu

-   [Natjecanje Rujie Liua posvećeno interaktivnim zadacima, Rujia Liu's Present 7, vrlo je kvalitetno i preporučuje se.](https://onlinejudge.org/contests/328-9976a2e2/)
-   [P5473\[NOI2019\]I 君的探险](https://www.luogu.com.cn/problem/P5473)
-   [P5208\[WC2019\]I 君的商店](https://www.luogu.com.cn/problem/P5208)

## Reference i daljnje čitanje

-   [Implementacija interaktivnih zadataka za online judge pomoću Linux cijevi (kineski)](https://www.cnblogs.com/tsreaper/p/pipe-interactive.html)
