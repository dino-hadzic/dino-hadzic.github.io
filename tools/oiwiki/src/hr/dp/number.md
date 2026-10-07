---
title: Znamenkasti DP
---

Ova stranica kratko predstavlja znamenkasti DP (digit DP).

## Uvod

Znamenke su ono što dobijemo kad broj rastavimo mjesto po mjesto na jedinice, desetice, stotice, tisućice itd., pa promatramo znamenku na svakom mjestu. Ako rastavljamo dekadski broj, svaka je znamenka 0\~9; za druge baze vrijedi analogno.

Znamenkasti DP služi za rješavanje posebne klase problema koji se razmjerno lako prepoznaju; obično imaju ova obilježja:

1.  traži se broj brojeva koji zadovoljavaju određene uvjete (tj. krajnji je cilj prebrojavanje);

2.  ti se uvjeti nakon pretvorbe mogu razumjeti i provjeravati idejom „znamenki”;

3.  ulaz zadaje interval brojeva (katkad samo gornju granicu) kao ograničenje prebrojavanja;

4.  gornja je granica velika (npr. $10^{18}$), pa bi provjera grubom silom prekoračila vremensko ograničenje.

Osnovno načelo znamenkastog DP-a:

Promotrimo kako ljudi broje: najjednostavnije je brojanje od manjeg prema većem, dodajući po jedan. No uočavamo da se za brojeve s mnogo znamenaka u tom postupku mnogo toga ponavlja. Primjerice, brojanje od 7000 do 7999, od 8000 do 8999 i od 9000 do 9999 vrlo je slično: u svima se posljednje tri znamenke mijenjaju od 000 do 999, a razlikuje se samo znamenka tisućica. Zato te postupke možemo objediniti, a odgovore dobivene u njima pohraniti u zajednički niz. Stanja tog niza postavljaju se prema konkretnim zahtjevima zadatka, a prijelazi se izvode rekurzijom ili DP-om.

U znamenkastom DP-u obično se koriste uobičajene tehnike problema prebrojavanja, npr. rastavljanje odgovora za interval na razliku dvaju dijelova (tj. $\mathit{ans}_{[l, r]} = \mathit{ans}_{[0, r]}-\mathit{ans}_{[0, l - 1]}$)

Kad imamo zajednički niz odgovora, slijedi prebrojavanje odgovora. Za to možemo odabrati memoizirano pretraživanje ili iterativnu rekurziju petljom. Da bismo bez ponavljanja i propusta prebrojali sve odgovore koji ne prelaze gornju granicu, prolazimo znamenke od najviše prema najnižoj, razmatramo koje se znamenke mogu upisati na svako mjesto i na kraju pomoću zajedničkog niza odgovora prebrojimo odgovore.

Pogledajmo sada konkretno nekoliko zadataka.

## Primjer 1

???+ note "Primjer 1 [Luogu P2602 Brojanje znamenaka](https://www.luogu.com.cn/problem/P2602)"
    Sažetak zadatka: zadana su dva pozitivna cijela broja $a,b$; za sve cijele brojeve u $[a,b]$ odredi koliko se puta pojavljuje svaka znamenka (digit).

### Metoda 1

#### Objašnjenje

Uočavamo da se za puni $\mathit{i}$-znamenkasti broj sve znamenke pojavljuju jednako često, pa neka niz $\mathit{dp}_i$ označava koliko se puta svaka znamenka pojavljuje među punim $i$-znamenkastim brojevima; vodeće nule za sada ne obrađujemo. Tada je $\mathit{dp}_i=10 \times \mathit{dp}_{i−1}+10^{i−1}$; prvi dio dolazi od doprinosa prvih $i-1$ znamenaka, a drugi od doprinosa $i$-te znamenke.

Kad imamo niz $\mathit{dp}$, razmotrimo kako prebrojati odgovore. Gornju granicu rastavimo na znamenke i prolazimo od najviše prema najnižoj; kad nismo priljubljeni uz gornju granicu, ostatak može poprimiti bilo koju vrijednost. Kad smo priljubljeni uz gornju granicu, ostatak može ići samo od $0$ do gornje granice; doprinose računamo odvojeno u dva dijela. Na kraju razmotrimo vodeće nule: ako je $i$-ta znamenka vodeća $0$, tada su i znamenke od $1$ do $\mathit{i-1}$ jednake $0$, pa smo višak izbrojili odgovore za popunjenih $i-1$ znamenaka i to treba dodatno oduzeti.

#### Implementacija

???+ note "Primjer rješenja"
    ```cpp
    #include <cstdio>
    using namespace std;
    constexpr int N = 15;
    using ll = long long;
    ll l, r, dp[N], mi[N];
    ll ans1[N], ans2[N];
    int a[N];
    
    void solve(ll n, ll *ans) {
      ll tmp = n;
      int len = 0;
      while (n) a[++len] = n % 10, n /= 10;
      for (int i = len; i >= 1; --i) {
        for (int j = 0; j < 10; j++) ans[j] += dp[i - 1] * a[i];
        for (int j = 0; j < a[i]; j++) ans[j] += mi[i - 1];
        tmp -= mi[i - 1] * a[i], ans[a[i]] += tmp + 1;
        ans[0] -= mi[i - 1];
      }
    }
    
    int main() {
      scanf("%lld%lld", &l, &r);
      mi[0] = 1ll;
      for (int i = 1; i <= 13; ++i) {
        dp[i] = dp[i - 1] * 10 + mi[i - 1];
        mi[i] = 10ll * mi[i - 1];
      }
      solve(r, ans1), solve(l - 1, ans2);
      for (int i = 0; i < 10; ++i) printf("%lld ", ans1[i] - ans2[i]);
      return 0;
    }
    ```

### Metoda 2

#### Objašnjenje

Zadatak se može riješiti i memoiziranim pretraživanjem. $\mathit{dp}_i$ označava odgovor za $i$ znamenaka kad nismo priljubljeni uz gornju granicu i nema vodećih nula.

Detalji su u komentarima koda.

#### Postupak

???+ note "Primjer rješenja"
    ```cpp
    #include <cstdio>
    #include <cstring>
    #include <iostream>
    using namespace std;
    using ll = long long;
    constexpr int N = 50005;
    ll a, b;
    ll f[15], ksm[15], p[15], now[15];
    
    ll dfs(int u, int x, bool f0,
           bool lim) {  // u je broj znamenaka, f0 ima li vodećih nula, lim jesmo li priljubljeni uz gornju granicu
      if (!u) {
        if (f0) f0 = false;
        return 0;
      }
      if (!lim && !f0 && (~f[u])) return f[u];
      ll cnt = 0;
      int lst = lim ? p[u] : 9;
      for (int i = 0; i <= lst; i++) {  // prolazimo znamenku koju upisujemo na ovo mjesto
        if (f0 && i == 0)
          cnt += dfs(u - 1, x, 1, lim && i == lst);  // obrada vodećih nula
        else if (i == x && lim && i == lst)
          cnt += now[u - 1] + 1 +
                 dfs(u - 1, x, 0,
                     lim && i == lst);  // sve dosad odabrane znamenke priljubljene su uz zadanu gornju granicu.
        else if (i == x)
          cnt += ksm[u - 1] + dfs(u - 1, x, 0, lim && i == lst);
        else
          cnt += dfs(u - 1, x, 0, lim && i == lst);
      }
      if ((!lim) && (!f0)) f[u] = cnt;  // memoiziramo samo ako nismo priljubljeni uz granicu i nema vodećih nula
      return cnt;
    }
    
    ll gans(ll d, int dig) {
      int len = 0;
      memset(f, -1, sizeof(f));
      while (d) {
        p[++len] = d % 10;
        d /= 10;
        now[len] = now[len - 1] + p[len] * ksm[len - 1];
      }
      return dfs(len, dig, 1, 1);
    }
    
    int main() {
      scanf("%lld%lld", &a, &b);
      ksm[0] = 1;
      for (int i = 1; i <= 12; i++) ksm[i] = ksm[i - 1] * 10ll;
      for (int i = 0; i < 9; i++) printf("%lld ", gans(b, i) - gans(a - 1, i));
      printf("%lld\n", gans(b, 9) - gans(a - 1, 9));
      return 0;
    }
    ```

## Primjer 2

???+ note "Primjer 2 [HDU 2089 Bez 62](https://acm.hdu.edu.cn/showproblem.php?pid=2089)"
    Sažetak zadatka: prebroj brojeve u intervalu koji među znamenkama nemaju 4 ni uzastopno 62.

### Objašnjenje

Za uvjet bez 4 dovoljno je provjeriti pri prolasku: ako ne prolazimo 4, stanje je valjano, pa to ograničenje nije potrebno memoizirati. Za 62 su uključene dvije znamenke; broj načina razlikuje se ovisno o tome je li prethodna znamenka 6 ili nije, pa stanjem treba zabilježiti različite brojeve načina. $\mathit{dp}_{\mathit{pos},\mathit{sta}}$ označava trenutno $\mathit{pos}$-to mjesto i je li prethodna znamenka 6; ovdje $\mathit{sta}$ treba samo stanja 0 i 1, a sve znamenke različite od 6 mogu se smatrati istim slučajem jer ne utječu na brojanje.

### Implementacija

???+ note "Primjer rješenja"
    ```cpp
    #include <cstdio>
    #include <cstring>
    #include <iostream>
    using namespace std;
    int x, y, dp[15][3], p[50];
    
    void pre() {
      memset(dp, 0, sizeof(dp));
      dp[0][0] = 1;
      for (int i = 1; i <= 10; i++) {
        dp[i][0] = dp[i - 1][0] * 9 - dp[i - 1][1];
        dp[i][1] = dp[i - 1][0];
        dp[i][2] = dp[i - 1][2] * 10 + dp[i - 1][1] + dp[i - 1][0];
      }
    }
    
    int cal(int x) {
      int cnt = 0, ans = 0, tmp = x;
      while (x) {
        p[++cnt] = x % 10;
        x /= 10;
      }
      bool flag = false;
      p[cnt + 1] = 0;
      for (int i = cnt; i; i--) {  // prolazimo znamenke od najviše prema najnižoj
        ans += p[i] * dp[i - 1][2];
        if (flag)
          ans += p[i] * dp[i - 1][0];
        else {
          if (p[i] > 4) ans += dp[i - 1][0];
          if (p[i] > 6) ans += dp[i - 1][1];
          if (p[i] > 2 && p[i + 1] == 6) ans += dp[i][1];
          if (p[i] == 4 || (p[i] == 2 && p[i + 1] == 6)) flag = true;
        }
      }
      return tmp - ans;
    }
    
    int main() {
      pre();
      while (~scanf("%d%d", &x, &y)) {
        if (!x && !y) break;
        if (x > y) swap(x, y);
        printf("%d\n", cal(y + 1) - cal(x));
      }
      return 0;
    }
    ```

## Primjer 3

???+ note "Primjer 3 [SCOI2009 Windy brojevi](https://loj.ac/problem/10165)"
    Sažetak zadatka: zadan je interval $[l,r]$; odredi broj brojeva u njemu koji zadovoljavaju uvjet **nemaju vodeću $0$ i svake dvije susjedne znamenke razlikuju se za barem $2$**.

### Objašnjenje

Najprije problem pretvorimo u jednostavniji oblik. Neka $\mathit{ans}_i$ označava broj brojeva u intervalu $[1,i]$ koji zadovoljavaju uvjet; traženi je odgovor $\mathit{ans}_r-\mathit{ans}_{l-1}$.

Za broj manji od $n$ sigurno postoji neko mjesto, gledano od najviše znamenke, na kojem je njegova znamenka manja od odgovarajuće znamenke broja $n$, dok su sve prethodne znamenke jednake znamenkama broja $n$.

S tim svojstvom možemo definirati $f(i,st,op)$ kao broj brojeva kad razmatramo $i$-to mjesto od najvišeg, trenutno stanje prefiksa je $st$, a odnos prefiksa prema broju koji rješavamo je $op$ ($op=1$ znači jednak, $op=0$ znači manji). U ovom zadatku stanje prefiksa je vrijednost prethodne znamenke, jer koje znamenke trenutno mjesto ne smije poprimiti ovisi samo o prethodnoj znamenci. U drugim zadacima ta vrijednost može biti: zbroj znamenaka prefiksa, $\gcd$ svih znamenaka prefiksa, ostatak prefiksa modulo neki broj, a moguće su i kombinacije dvaju ili više takvih podataka.

Zapišimo **jednadžbu prijelaza stanja**: $f(i,st,op)=\sum_{k=1}^{\mathit{maxx}} f(i+1,k,op=1~ \operatorname{and}~ k=\mathit{maxx} )\quad (|\mathit{st}-k|\ge 2)$

Ovdje je $k$ vrijednost sljedeće znamenke koju prolazimo, a $\mathit{maxx}$ najveća znamenka koju trenutno smijemo uzeti. Naime, ako je $\mathit{op}=1$, vrijednost na ovom mjestu ne smije biti veća od odgovarajuće znamenke broja koji rješavamo; inače nema ograničenja.

Uočavamo da je odgovor jednak kad god su tri parametra $f$ jednaka, čak i ako je prefiks odabran drukčije. Da se taj odgovor ne bi računao više puta, možemo koristiti [memoizirano pretraživanje](./memo.md).

### Implementacija

???+ note "Primjer rješenja"
    ```cpp
    int dfs(int x, int st, int op)  // op=1 =; op=0 <
    {
      if (!x) return 1;
      if (!op && ~f[x][st]) return f[x][st];
      int maxx = op ? dim[x] : 9, ret = 0;
      for (int i = 0; i <= maxx; i++) {
        if (abs(st - i) < 2) continue;
        if (st == 11 && i == 0)
          ret += dfs(x - 1, 11, op & (i == maxx));
        else
          ret += dfs(x - 1, i, op & (i == maxx));
      }
      if (!op) f[x][st] = ret;
      return ret;
    }
    
    int solve(int x) {
      memset(f, -1, sizeof f);
      dim.clear();
      dim.push_back(-1);
      int t = x;
      while (x) {
        dim.push_back(x % 10);
        x /= 10;
      }
      return dfs(dim.size() - 1, 11, 1);
    }
    ```

## Primjer 4

???+ note "Primjer 4. [SPOJMYQ10](https://www.spoj.com/problems/MYQ10/en/)"
    Sažetak zadatka: ako rukom ispišemo sve cijele brojeve iz $[n,m]$, koliko ih izgleda jednako kao njihov odraz u zrcalu? ($n,m<10^{44}, T<10^5$)

### Objašnjenje

Napomena: s obzirom na zrcaljenje, samo su $0,1,8$ sami sebi zrcalni odraz. Zato „jednako” ovdje nije palindrom u uobičajenom smislu, nego palindrom koji sadrži samo $0,1,8$.

Prvo, u znamenkastom DP-u očito se smiju birati samo $0,1,8$.

Drugo, budući da vrijednosti prelaze raspon tipa long long, $[n,m]=[1,m]-[1,n-1]$ više nije primjenjivo (aritmetika velikih brojeva bila bi zamorna), nego treba provjeriti je li $n$ valjan i dobiti: $[n,m]=[1,m]-[1,n]+\mathrm{check}(n)$.

Zrcaljenje smo riješili; kako provjeriti palindrom?

Malim nizom pamtimo prethodne vrijednosti. Dok nismo prešli polovinu duljine, dovoljno je ne prijeći gornju granicu; nakon što prijeđemo polovinu, treba još provjeriti je li znamenka jednaka svojoj „zrcalno simetričnoj” znamenci.

Dodatno treba paziti da se u memoizaciji u ovom zadatku ne smije koristiti `memset`, jer bi inače došlo do prekoračenja vremena.

### Implementacija

???+ note "Primjer rješenja"
    ```cpp
    int check(char cc[]) {  // posebna provjera za n
      int strc = strlen(cc);
      for (int i = 0; i < strc; ++i) {
        if (!(cc[i] == cc[strc - i - 1] &&
              (cc[i] == '1' || cc[i] == '8' || cc[i] == '0')))
          return 0ll;
      }
      return 1ll;
    }
    
    // now: trenutno mjesto, eff: broj značajnih mjesta, fulc: jesmo li svugdje na gornjoj granici, ful0: jesu li sve nule
    int dfs(int now, int eff, bool ful0, bool fulc) {
      if (now == 0) return 1ll;
      if (!fulc && f[now][eff][ful0] != -1)  // memoizacija
        return f[now][eff][ful0];
    
      int res = 0, maxk = fulc ? dig[now] : 9;
      for (int i = 0; i <= maxk; ++i) {
        if (i != 0 && i != 1 && i != 8) continue;
        b[now] = i;
        if (ful0 && i == 0)  // same vodeće nule
          res += dfs(now - 1, eff - 1, 1, 0);
        else if (now > eff / 2)                                  // nismo prešli polovinu
          res += dfs(now - 1, eff, 0, fulc && (dig[now] == i));  // prešli smo polovinu
        else if (b[now] == b[eff - now + 1])
          res += dfs(now - 1, eff, 0, fulc && (dig[now] == i));
      }
      if (!fulc) f[now][eff][ful0] = res;
      return res;
    }
    
    char cc1[100], cc2[100];
    int strc, ansm, ansn;
    
    int get(char cc[]) {  // omotač za obradu
      strc = strlen(cc);
      for (int i = 0; i < strc; ++i) dig[strc - i] = cc[i] - '0';
      return dfs(strc, strc, 1, 1);
    }
    
    scanf("%s%s", cc1, cc2);
    printf("%lld\n", get(cc2) - get(cc1) + check(cc1));
    ```

## Primjer 5

???+ note "Primjer 5. [P3311 Brojanje](https://www.luogu.com.cn/problem/P3311)"
    Zadatak: pozitivan cijeli broj $x$ zovemo sretnim ako i samo ako njegov dekadski zapis ne sadrži nijedan element skupa znamenkastih nizova $S$ kao podniz uzastopnih znamenaka. Primjerice, za $S = \{22, 333, 0233\}$ broj $233233$ je sretan, a $23332333$, $2023320233$, $32233223$ nisu. Zadani su $n$ i $S$; izračunaj broj sretnih brojeva koji nisu veći od $n$. Odgovor treba dati modulo $10^9 + 7$.
    
    $1 \leq n<10^{1201}，1 \leq m \leq 100，1 \leq \sum_{i = 1}^m |s_i| \leq 1500，\min_{i = 1}^m |s_i| \geq 1$, gdje $|s_i|$ označava duljinu niza $s_i$. $n$ nema vodeću $0$, ali $s_i$ može imati vodeću $0$.

### Objašnjenje

Čitajući zadatak uočavamo da, ako brojeve promatramo kao nizove znakova, treba obaviti višestruko podudaranje uzoraka, pa se prirodno nameće AC automat (Aho–Corasick). U običnom znamenkastom DP-u prolazimo mjesta od najvišeg prema najnižem, a zatim što upisati na svako mjesto; u ovom zadatku to prirodno postaje prolazak po broju već upisanih mjesta, zatim po čvoru AC automata u kojem se trenutno nalazimo, a potom prijelaz iz trenutnog čvora u njegovo dijete u AC automatu.

Neka $f(i,j,0/1)$ označava da je od najvišeg mjesta upisano $i$ znamenaka (tj. prošli smo $i$ bridova AC automata), trenutno smo u čvoru s oznakom $j$, te jesmo li trenutno točno priljubljeni uz gornju granicu.

Što se tiče uvjeta „ne sadrži”, dovoljno je u AC automatu označiti završne čvorove svih uzoraka i tijekom DP-a te čvorove preskakati.

Prijelaz se lako izvodi; detalji su u glavnoj funkciji koda.

### Implementacija

???+ note "Primjer rješenja"
    ```cpp
    #include <cstdio>
    #include <cstring>
    #include <queue>
    using namespace std;
    using ll = long long;
    constexpr int N = 1505;
    constexpr int mod = 1000000007;
    int n, m;
    char s[N], c[N];
    int ch[N][10], fail[N], ed[N], tot, len;
    
    void insert() {
      int now = 0;
      int L = strlen(s);
      for (int i = 0; i < L; ++i) {
        if (!ch[now][s[i] - '0']) ch[now][s[i] - '0'] = ++tot;
        now = ch[now][s[i] - '0'];
      }
      ed[now] = 1;
    }
    
    queue<int> q;
    
    void build() {
      for (int i = 0; i < 10; ++i)
        if (ch[0][i]) q.push(ch[0][i]);
      while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int i = 0; i < 10; ++i) {
          if (ch[u][i]) {
            fail[ch[u][i]] = ch[fail[u]][i], q.push(ch[u][i]),
            ed[ch[u][i]] |= ed[fail[ch[u][i]]];
          } else
            ch[u][i] = ch[fail[u]][i];
        }
      }
      ch[0][0] = 0;
    }
    
    ll f[N][N][2], ans;
    
    void add(ll &x, ll y) { x = (x + y) % mod; }
    
    int main() {
      scanf("%s", c);
      n = strlen(c);
      scanf("%d", &m);
      for (int i = 1; i <= m; ++i) scanf("%s", s), insert();
      build();
      f[0][0][1] = 1;
      for (int i = 0; i < n; ++i) {
        for (int j = 0; j <= tot; ++j) {
          if (ed[j]) continue;
          for (int k = 0; k < 10; ++k) {
            if (ed[ch[j][k]]) continue;
            add(f[i + 1][ch[j][k]][0], f[i][j][0]);
            if (k < c[i] - '0') add(f[i + 1][ch[j][k]][0], f[i][j][1]);
            if (k == c[i] - '0') add(f[i + 1][ch[j][k]][1], f[i][j][1]);
          }
        }
      }
      for (int j = 0; j <= tot; ++j) {
        if (ed[j]) continue;
        add(ans, f[n][j][0]);
        add(ans, f[n][j][1]);
      }
      printf("%lld\n", ans - 1);
      return 0;
    }
    ```

Ovaj zadatak dobro pomaže u razumijevanju načela znamenkastog DP-a.

## Zadaci za vježbu

[Ahoi2009 self Raspodjela iste vrste](https://www.luogu.com.cn/problem/P4127)

[Luogu P3413 SAC#1 - Slatki brojevi](https://www.luogu.com.cn/problem/P3413)

[HDU 6148 Valley Number](https://acm.hdu.edu.cn/showproblem.php?pid=6148)

[CF55D Beautiful numbers](http://codeforces.com/problemset/problem/55/D)

[CF628D Magic Numbers](http://codeforces.com/problemset/problem/628/D)
