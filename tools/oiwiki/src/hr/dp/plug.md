---
title: Plug DP
---

## Definicija

Neki problemi [DP-a s bitmaskama](./state.md) zahtijevaju da u stanju pamtimo podatke o povezanosti; takvi se problemi slikovito nazivaju plug DP (DP s „utikačima”) ili DP sa sažimanjem stanja povezanosti. Primjeri su prebrojavanje Hamiltonovih putova u rešetkastom grafu, prebrojavanje crno-bijelih bojanja ploče u kojima polja iste boje čine jednu komponentu povezanosti, prebrojavanje razapinjućih stabala posebnih grafova itd. Ti problemi obično zahtijevaju da kodiramo povezanost stanja i razmatramo kako se povezanost mijenja tijekom prijelaza stanja.

## Uvod

### Popločavanje dominama i DP po konturi

Ponavljanje je majka znanja: prije nego što počnemo učiti plug DP, prisjetimo se jednog klasičnog problema.

???+ note "Primjer [„HDU 1400” Mondriaan’s Dream](https://acm.hdu.edu.cn/showproblem.php?pid=1400)"
    Sažetak zadatka: ploču $N\times M$ treba potpuno popločati dominama $1\times 2$ ili $2\times 1$; odredi broj načina.

Kad $n$ ili $m$ nisu veliki, ovakvi se problemi rješavaju [DP-om s bitmaskama](./state.md). Faze dijelimo po redcima; neka $dp(i,s)$ označava broj načina kad smo razmotrili prvih $i$ redaka, a stanje $i$-tog retka je $s$. Svaki bit stanja $s$ označava je li to polje već pokriveno iz prethodnog retka.

![domino](./images/domino.svg)

Drugi je način podjele na faze DP polje po polje, odnosno DP po konturi (contour-line DP). $dp(i,j,s)$ označava broj načina kad smo razmotrili polja do $i$-tog retka i $j$-tog stupca, a stanje na trenutnoj konturi je $s$.

Iako u DP-u polje po polje stanje dobiva jednu dimenziju više, vremenska se složenost prijelaza smanjuje na $O(1)$, pa ukupna vremenska složenost ostaje ista. Neka $f_0$ označava stanja trenutne faze, $f_1$ stanja sljedeće faze, a $u = f_0(s)$ vrijednost funkcije koju trenutno prolazimo; jednadžba prijelaza stanja glasi:

```cpp
if (s >> j & 1) {       // ako je polje već pokriveno
  f1[s ^ 1 << j] += u;  // ne stavljamo
} else {                // ako polje nije pokriveno
  if (j != m - 1 && (!(s >> j + 1 & 1))) f1[s ^ 1 << j + 1] += u;  // vodoravno
  f1[s ^ 1 << j] += u;                                             // okomito
}
```

Uočimo da se ovdje jednadžbe za „ne stavljamo” i „okomito” mogu spojiti.

??? note "Implementacija"
    ```cpp
    #include <algorithm>
    #include <iostream>
    using namespace std;
    constexpr int N = 11;
    long long f[2][1 << N], *f0, *f1;
    int n, m;
    
    int main() {
      while (cin >> n >> m && n) {
        f0 = f[0];
        f1 = f[1];
        fill(f1, f1 + (1 << m), 0);
        f1[0] = 1;
        for (int i = 0; i < n; ++i) {
          for (int j = 0; j < m; ++j) {
            swap(f0, f1);
            fill(f1, f1 + (1 << m), 0);
    #define u f0[s]
            for (int s = 0; s < 1 << m; ++s)
              if (u) {
                if (j != m - 1 && (!(s >> j & 3))) f1[s ^ 1 << j + 1] += u;  // vodoravno
                f1[s ^ 1 << j] += u;  // okomito ili ne stavljamo
              }
          }
        }
        cout << f1[0] << endl;
      }
    }
    ```

??? note "Zadatak [„SRM 671. Div 1 900” BearDestroys](https://archive.topcoder.com/ProblemStatement/pm/14069)"
    Sažetak zadatka: zadana je matrica $n\times m$ u kojoj je svako polje `E` ili `S`.
    Za matricu je definiran način bodovanja. Polja se obilaze redak po redak; ako je polje već zauzeto dominom, preskače se.
    Inače se pokušava postaviti domino. Ako smjer postavljanja izlazi iz matrice ili je zauzet drugom dominom, postavljanje ne uspijeva pa se prelazi na drugi način ili se polje preskače.
    Ako je polje `E`, prednost ima domino $1\times 2$,
    ako je `S`, prednost ima domino $2\times 1$.
    Rezultat matrice je konačan broj postavljenih domina.
    Odredi zbroj rezultata svih $2^{nm}$ matrica.

### Pojmovi

Faza: redoslijed izvođenja dinamičkog programiranja; rezultati kasnijih faza ovise samo o rezultatima ranijih faza (odsutnost naknadnog utjecaja). Mnogi DP problemi dopuštaju više načina podjele na faze. Primjerice, u problemu ruksaka faze obično možemo dijeliti i po predmetima i po kapacitetu ruksaka (što prolazi vanjska petlja). U problemu domina faze možemo dijeliti po redcima, stupcima, poljima, dijagonalama itd.

Kontura: granica između već odlučenih i još neodlučenih stanja.

![contour line](./images/contour_line.svg)

Utikač: postojanje utikača polja u nekom smjeru znači da je polje u tom smjeru spojeno sa susjednim poljem.

![plug](./images/plug.svg)

## Model putova

### Više ciklusa

#### Primjer

???+ note "Primjer [„HDU 1693” Eat the Trees](https://acm.hdu.edu.cn/showproblem.php?pid=1693)"
    Sažetak zadatka: odredi broj načina da se ploča $N\times M$ pokrije s nekoliko ciklusa; neka polja su prepreke.

Strogo govoreći, problem s više ciklusa ne pripada plug DP-u, jer je, kao i u gornjem problemu popločavanja dominama, dovoljno pamtiti postoji li utikač te utikače spajati i stvarati u parovima.

Uočite da za ploču širine $m$ kontura ima širinu $m+1$, jer sadrži $m$ gornjih utikača i $1$ lijevi utikač. Kad se završi iteracija po jednom retku, krajnji desni lijevi utikač u pravilu je nevaljano stanje, a istodobno treba dodati prvi lijevi utikač sljedećeg retka; zato treba prilagoditi stanje trenutne konture, obično pomakom svih stanja ulijevo. Tu operaciju zovemo kotrljanjem, `roll()`.

??? note "Kôd primjera"
    ```cpp
    --8<-- "docs/dp/code/plug/plug_1.cpp"
    ```

#### Zadaci za vježbu

??? note "Zadatak [„ZOJ 3466” The Hive II](https://pintia.cn/problem-sets/91827364500/exam/problems/type/7?problemSetProblemId=91827368730)"
    Sažetak zadatka: kao prethodni zadatak, ali polja su šesterokuti.

### Jedan ciklus

#### Primjer

???+ note "Primjer [„Andrew Stankevich Contest 16 - Problem F” Pipe Layout](https://codeforces.com/gym/100220)"
    Sažetak zadatka: odredi broj načina da se ploča $N\times M$ pokrije jednim ciklusom.

U gornjem prikazu stanja svako spajanje para povezanih utikača stvara jedan zaseban ciklus; zato u ovom zadatku moramo još razlikovati povezanost među utikačima (tu smo!). To zahtijeva dodatno kodiranje stanja.

#### Kodiranje stanja

Uobičajeni su načini kodiranja zagradni prikaz i minimalni prikaz; ovdje se usredotočujemo na općenitiji minimalni prikaz. Cjelobrojnim nizom duljine $m+1$ pamtimo stanje svakog utikača na konturi; $0$ znači da utikača nema, a dogovorno povezane utikače označavamo istim brojem.

Tako sljedeća dva kodiranja predstavljaju isto stanje:

-   `0 3 1 0 1 3`
-   `0 1 2 0 2 1`

Sva jednaka stanja preslikavamo u leksikografski najmanji prikaz; primjerice, u gornjem je primjeru `0 1 2 0 2 1` minimalni prikaz.

Nizom `b[]` označavamo stanje utikača na konturi. `bb[]` označava najmanji broj u koji se svaki broj preslikava tijekom kodiranja minimalnim prikazom. Pazite: $0$ znači da utikača nema i ne smije se preslikati u drugu vrijednost.

??? note "Implementacija"
    ```cpp
    int b[M + 1], bb[M + 1];
    
    int encode() {
      int s = 0;
      memset(bb, -1, sizeof(bb));
      int bn = 1;
      bb[0] = 0;
      for (int i = m; i >= 0; --i) {
    #define bi bb[b[i]]
        if (!~bi) bi = bn++;
        s <<= offset;
        s |= bi;
      }
      return s;
    }
    
    void decode(int s) {
      REP(i, m + 1) {
        b[i] = s & mask;
        s >>= offset;
      }
    }
    ```

Uočimo da se utikači uvijek pojavljuju i nestaju u parovima. Zato je stanje poput `0 1 2 0 1 2` nevaljano. Valjana stanja čine niz zagrada, a u praksi valjana stanja mogu biti vrlo rijetka.

#### Ručno pisana hash tablica

U nekim problemima [DP-a s bitmaskama](./state.md) valjana stanja mogu biti rijetka (npr. u ovom zadatku); radi optimizacije vremenske i prostorne složenosti valjana DP stanja možemo pohranjivati u hash tablici. Natjecatelji u C++-u mogu koristiti [std::unordered\_map](http://www.cplusplus.com/reference/unordered_map/unordered_map/), a mogu je, naravno, i sami napisati, čime se u nju fleksibilno može ugraditi i funkcija prijelaza stanja.

???+ note "Implementacija"
    ```cpp
    constexpr int MaxSZ = 16796, Prime = 9973;
    
    struct hashTable {
      int head[Prime], next[MaxSZ], sz;
      int state[MaxSZ];
      long long key[MaxSZ];
    
      void clear() {
        sz = 0;
        memset(head, -1, sizeof(head));
      }
    
      void push(int s) {
        int x = s % Prime;
        for (int i = head[x]; ~i; i = next[i]) {
          if (state[i] == s) {
            key[i] += d;
            return;
          }
        }
        state[sz] = s, key[sz] = d;
        next[sz] = head[x];
        head[x] = sz++;
      }
    
      void roll() { REP(i, sz) state[i] <<= offset; }
    } H[2], *H0, *H1;
    ```

U gornjem kodu:

-   `MaxSZ` je gornja granica broja valjanih stanja; može se procijeniti ili unaprijed točnije izračunati.
-   `Prime` je veliki prosti broj manji od `MaxSZ`.
-   `head[]` su pokazivači na čvorove zaglavlja.
-   `next[]` su pokazivači na sljedeća stanja.
-   `state[]` je stanje čvora.
-   `key[]` je ključ čvora, u ovom zadatku broj načina.
-   `clear()` je funkcija inicijalizacije; kao i kod ručno pisane liste susjedstva, dovoljno je inicijalizirati pokazivače zaglavlja.
-   `push()` je funkcija prijelaza stanja, pri čemu je `d` globalna varijabla (iz lijenosti) koja označava prirast koji donosi svaki prijelaz stanja. Ako je stanje pronađeno, radimo `+=`, a inače stvaramo novi čvor sa stanjem `s` i ključem `d`.
-   `roll()` kotrlja konturu nakon završene iteracije po cijelom retku.

O analizi složenosti hash tablica te o razlici između otvorenog i zatvorenog hashiranja vidi odgovarajuća poglavlja o hash tablicama u [„Introduction to Algorithms”](../contest/resources.md#书籍).

#### Prijelaz stanja

???+ note "Implementacija"
    ```cpp
    REP(ii, H0->sz) {
      decode(H0->state[ii]);                  // dohvati stanje i dekodiraj ga
      d = H0->key[ii];                        // dobij prirast delta
      int lt = b[j], up = b[j + 1];           // lijevi utikač, gornji utikač
      bool dn = i != n - 1, rt = j != m - 1;  // donji utikač, desni utikač
      if (lt && up) {                         // ako postoje i lijevi i gornji utikač
        if (lt == up) {                       // iz iste komponente povezanosti
          if (i == n - 1 &&
              j == m - 1) {  // spajanje je dopušteno samo na posljednjem polju; zatvara ciklus.
            push(j, 0, 0);
          }
        } else {  // inače te dvije komponente moramo spojiti, jer zadatak traži pokrivanje ciklusom
          REP(i, m + 1) if (b[i] == lt) b[i] = up;
          push(j, 0, 0);
        }
      } else if (lt || up) {  // ako postoji samo jedan od lijevog i gornjeg utikača
        int t = lt | up;      // dohvati taj utikač
        if (dn) {             // ako se može produljiti prema dolje
          push(j, t, 0);
        }
        if (rt) {  // ako se može produljiti udesno
          push(j, 0, t);
        }
      } else {           // ako nema ni lijevog ni gornjeg utikača
        if (dn && rt) {  // stvori par novih utikača
          push(j, m, m);
        }
      }
    }
    ```

??? note "Kôd primjera"
    ```cpp
    --8<-- "docs/dp/code/plug/plug_2.cpp"
    ```

#### Zadaci za vježbu

??? note "Zadatak [„Ural 1519” Formula 1](https://acm.timus.ru/problem.aspx?space=1&num=1519)"
    Sažetak zadatka: odredi broj načina da se ploča $N\times M$ pokrije jednim ciklusom; neka polja su prepreke.

??? note "Zadatak [„USACO 5.4.4” Betsy's Tours](https://hydro.ac/d/USACO/p/USACO544)"
    Sažetak zadatka: za kvadratnu ploču $N\times N$ ($N\le 7$) odredi ukupan broj putova koji počinju u gornjem lijevom kutu, završavaju u donjem lijevom kutu i prolaze svakim poljem. Iako je riječ o putu, zbog fiksnog početka i kraja može se pretvoriti u problem jednog ciklusa.

??? note "Zadatak [„POJ 1739” Tony's Tour](http://poj.org/problem?id=1739)"
    Sažetak zadatka: za ploču $N\times M$ odredi ukupan broj putova koji počinju u donjem lijevom kutu, završavaju u donjem desnom kutu i prolaze svakim poljem; neka polja su prepreke.

??? note "Zadatak [„USACO 6.1.1” Postal Vans](https://vjudge.net/problem/UVALive-2738)"
    Sažetak zadatka: odredi broj načina da se ploča $4\times N$ pokrije jednim usmjerenim ciklusom; potrebna je aritmetika velikih brojeva.

??? note "Zadatak [„HNOI 2007” Čarobni zabavni park](https://www.luogu.com.cn/problem/P3190)"
    Sažetak zadatka: zadana je rešetka $n\times m$ s težinom u svakom polju; odredi proizvoljan ciklus koji maksimizira zbroj težina polja kroz koja prolazi.

??? note "Zadatak [„ProjectEuler 393” Migrating ants](https://projecteuler.net/problem=393)"
    Sažetak zadatka: kvadratna ploča $n\times n$ pokriva se s više ciklusa; svaki raspored s $m$ ciklusa doprinosi odgovoru $2^m$. Odredi zbroj doprinosa svih rasporeda.

### Jedan put

#### Primjer

???+ note "Primjer [„ZOJ 3213” Beautiful Meadow](https://pintia.cn/problem-sets/91827364500/exam/problems/type/7?page=22&problemSetProblemId=91827367895)"
    Sažetak zadatka: za kvadratnu ploču $N\times M$ ($N,M\le 8$) s težinom u svakom polju odredi put koji maksimizira zbroj težina polja koja pokriva.

Ovo je standardni problem jednog puta. U problemima jednog puta u kodiranom stanju postoje i nesparivi samostalni utikači. U funkciji prijelaza stanja treba dodatno razmotriti stvaranje, spajanje i nestajanje samostalnih utikača. Stvaranje i nestajanje samostalnog utikača odgovara jednom kraju puta, pa se takvi događaji ne mogu dogoditi više od dva puta (jedno stvaranje i jedno nestajanje, ili dva stvaranja i jedno spajanje); inače bi u konačnom rezultatu sigurno bilo više komponenata povezanosti.

U stanju moramo dodatno pamtiti ukupan broj takvih događaja; taj se podatak može kodirati u stanje (pazite: ovakvi se dodatni podaci pri prilagodbi konture ne kotrljaju), a može se i dodati dimenzija izvan niza `hashTable`. U oglednom programu dolje odabrali smo potonje.

#### Prijelaz stanja

???+ note "Implementacija"
    ```cpp
    REP(i, n) {
      REP(j, m) {
        checkMax(ans, A[i][j]);  // slučaj jednog polja treba obraditi posebno
        if (!A[i][j]) continue;  // ako je prepreka, preskoči; pazite, niz stanja tada ne treba kotrljati
        swap(H0, H1);
        REP(c, 3)
        H1[c].clear();  // c je ukupan broj događaja stvaranja i nestajanja, najviše 2
        REP(c, 3) REP(ii, H0[c].sz) {
          decode(H0[c].state[ii]);
          d = H0[c].key[ii] + A[i][j];
          int lt = b[j], up = b[j + 1];
          bool dn = A[i + 1][j], rt = A[i][j + 1];
          if (lt && up) {
            if (lt == up) {  // u problemu jednog puta ne smijemo spajati jednake utikače.
              // Cannot deploy here...
            } else {  // među dvama utikačima koji se spajaju može biti samostalni, ali to obrađuje isti odsječak koda
              REP(i, m + 1) if (b[i] == lt) b[i] = up;
              push(c, j, 0, 0);
            }
          } else if (lt || up) {
            int t = lt | up;
            if (dn) {
              push(c, j, t, 0);
            }
            if (rt) {
              push(c, j, 0, t);
            }
            // slučaj nestajanja utikača: ako je samostalan, nestaje; ako je iz para, to je kao stvaranje samostalnog utikača;
            // u oba slučaja treba c + 1.
            if (c < 2) {
              push(c + 1, j, 0, 0);
            }
          } else {
            d -= A[i][j];
            H1[c].push(H0[c].state[ii]);
            d += A[i][j];    // preskoči stvaranje utikača; zadatak ne traži potpuno pokrivanje
            if (dn && rt) {  // stvori par utikača
              push(c, j, m, m);
            }
            if (c < 2) {  // stvori samostalni utikač
              if (dn) {
                push(c + 1, j, m, 0);
              }
              if (rt) {
                push(c + 1, j, 0, m);
              }
            }
          }
        }
      }
      REP(c, 3) H1[c].roll();  // kraj retka, prilagodi konturu
    }
    ```

??? note "Kôd primjera"
    ```cpp
    --8<-- "docs/dp/code/plug/plug_3.cpp"
    ```

#### Zadaci za vježbu

??? note "Zadatak [„BZOJ 2310” ParkII](https://hydro.ac/p/bzoj-P2310)"
    Sažetak zadatka: ploča $m\times n$ s težinom u svakom polju; odredi pokrivanje jednim putem koje maksimizira zbroj težina polja kroz koja put prolazi.

??? note "Zadatak [„NOI 2010 Day2” Plan putovanja](https://www.luogu.com.cn/problem/P1933)"
    Sažetak zadatka: ploča $n\times m$ u kojoj svako polje ima težinu 0 ili 1, T\[x]\[y]; treba pronaći pokrivanje putem takvo da:
    
    -   i-to posjećeno polje (x, y) zadovoljava T\[x]\[y]= L\[i]
    -   jedan kraj puta leži na rubu ploče
    
    Odredi broj mogućih rasporeda.

## Model bojanja

Osim modela putova postoji još jedna česta vrsta modela, u kojoj ploču bojamo, a susjedna polja iste boje smatraju se povezanima. U problemima s putovima pri prijelazu stanja prolazimo po smjeru trenutnog puta, a u problemima bojanja prolazimo po boji kojom bojamo trenutno polje. U modelu bojanja u stanju može biti više od dva polja iste povezanosti. No u cjelini je sve vrlo slično. Pogledajmo klasičan primjer.

### Primjer „UVa 10572” Black & White

???+ note "Primjer [„UVa 10572” Black & White](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=1513)"
    Sažetak zadatka: na ploči $N\times M$ neobojana polja treba obojiti crno i bijelo tako da su sva crna područja i sva bijela područja povezana, a nijedan podpravokutnik $2\times 2$ nije jednobojan (npr. slučaj na slici dolje je nevaljan). Odredi broj valjanih bojanja i konstruiraj jedno valjano bojanje.
    
    ![black\_and\_white1](./images/black_and_white1.svg)

### Kodiranje stanja

Najprije razmotrimo kodiranje stanja. Bez povezanosti to je zadatak [SGU 197. Nice Patterns Strike Back](https://codeforces.com/problemsets/acmsguru/problem/99999/197), koji se izravno rješava [DP-om s bitmaskama](./state.md). Sada u stanju treba istodobno izraziti boju i povezanost; promatramo stanje svakog položaja na konturi, pri čemu svakih `Offset` bitova opisuje jedan položaj na konturi. Budući da postoje samo dvije boje, crna i bijela, boju označavamo parnošću najnižeg bita, a ostatak označava povezanost.

Za polja iznad prvog retka i lijevo od prvog stupca, ako želimo izbjeći posebne slučajeve, možemo uvesti treću boju; ovdje uočavamo da je povezanost tih rubnih stanja sigurno 0, pa treću boju ne treba dodatno kodirati.

U problemima s putovima kontura se sastoji od $m$ gornjih utikača i $1$ lijevog utikača. U ovom zadatku trebamo još provjeriti je li podpravokutnik $2\times 2$ čiji je donji desni kut trenutno polje valjan, pa pamtimo i boju gornjeg lijevog polja; stoga je duljina konture i dalje $m+1$.

Ovakvo kodiranje i dalje čuva mnogo suvišnih podataka (povezana područja sigurno su iste boje, a za gornje lijevo polje treba samo boja, ne i povezanost), ali budući da već koristimo hash tablicu i minimalni prikaz, utjecaj na vremensku složenost je malen, pa radi manjeg opterećenja pri programiranju nećemo dalje profinjivati.

U najgorem slučaju (npr. prvi redak naizmjence crn i bijel) povezanost svakog utikača je različita, pa za povezanost trebamo $4$ bita; uz bit za boju `Offset` u ovom zadatku iznosi $5$ bitova.

???+ note "Implementacija"
    ```cpp
    constexpr int Offset = 5, Mask = (1 << Offset) - 1;
    int c[N + 2];
    int b[N + 2], bb[N + 3];
    
    T_state encode() {
      T_state s = 0;
      memset(bb, -1, sizeof(bb));
      int bn = 1;
      bb[0] = 0;
      for (int i = m; i >= 0; --i) {
    #define bi bb[b[i]]
        if (!~bi) bi = bn++;
        s <<= Offset;
        s |= (bi << 1) | c[i];
      }
      return s;
    }
    
    void decode(T_state s) {
      REP(i, m + 1) {
        b[i] = s & Mask;
        c[i] = b[i] & 1;
        b[i] >>= 1;
        s >>= Offset;
      }
    }
    ```

### Ručno pisana hash tablica

Budući da treba konstruirati neko valjano bojanje, u hash tablicu dodajemo polje `pre[]` koje za svako stanje pamti proizvoljnog prethodnika iz prethodne faze.

???+ note "Implementacija"
    ```cpp
    constexpr int Prime = 9979, MaxSZ = 1 << 20;
    
    template <class T_state, class T_key>
    struct hashTable {
      int head[Prime];
      int next[MaxSZ], sz;
      T_state state[MaxSZ];
      T_key key[MaxSZ];
      int pre[MaxSZ];
    
      void clear() {
        sz = 0;
        memset(head, -1, sizeof(head));
      }
    
      void push(T_state s, T_key d, T_state u) {
        int x = s % Prime;
        for (int i = head[x]; ~i; i = next[i]) {
          if (state[i] == s) {
            key[i] += d;
            return;
          }
        }
        state[sz] = s, key[sz] = d, pre[sz] = u;
        next[sz] = head[x], head[x] = sz++;
      }
    
      void roll() { REP(ii, sz) state[ii] <<= Offset; }
    };
    
    hashTable<T_state, T_key> _H, H[N][N], *H0, *H1;
    ```

### Konstrukcija rješenja

S gornjim podacima lako konstruiramo rješenje. Najprije prođemo stanja u trenutnoj hash tablici; ako broj komponenata povezanosti nije veći od $2$, pribrojimo ga broju načina. Ako broj načina nije $0$, rješenje konstruiramo unatrag pomoću niza `pre`; pazite da na kraju svakog retka, zbog izvedene operacije `Roll()`, boju treba uzeti iz `c[j+1]`.

???+ note "Implementacija"
    ```cpp
    void print() {
      T_key z = 0;
      int u;
      REP(i, H1->sz) {
        decode(H1->state[i]);
        if (*max_element(b + 1, b + m + 1) <= 2) {
          z += H1->key[i];
          u = i;
        }
      }
      cout << z << endl;
      if (z) {
        DWN(i, n, 0) {
          B[i][m] = 0;
          DWN(j, m, 0) {
            decode(H[i][j].state[u]);
            int cc = j == m - 1 ? c[j + 1] : c[j];
            B[i][j] = cc ? 'o' : '#';
            u = H[i][j].pre[u];
          }
        }
        REP(i, n) puts(B[i]);
      }
      puts("");
    }
    ```

### Prijelaz stanja

Označimo:

-   `cc` boja polja koje trenutno bojamo
-   `lf` boja lijevog polja
-   `up` boja gornjeg polja
-   `lu` boja gornjeg lijevog polja

S $-1$ označavamo nepostojanje boje. Razmotrimo sada prijelaz stanja; postoje tri slučaja: spajanje, nasljeđivanje i stvaranje:

???+ note "Prijelaz stanja – kôd"
    ```cpp
    void trans(int i, int j, int u, int cc) {
      decode(H0->state[u]);
      int lf = j ? c[j - 1] : -1, lu = b[j] ? c[j] : -1,
          up = b[j + 1] ? c[j + 1] : -1;  // i nepostojanje boje je boja!
      if (lf == cc && up == cc) {         // spajanje
        if (lu == cc) return;             // slučaj jednobojnog podpravokutnika 2x2
        int lf_b = b[j - 1], up_b = b[j + 1];
        REP(i, m + 1) if (b[i] == up_b) { b[i] = lf_b; }
        b[j] = lf_b;
      } else if (lf == cc || up == cc) {  // nasljeđivanje
        if (lf == cc)
          b[j] = b[j - 1];
        else
          b[j] = b[j + 1];
      } else {                                             // stvaranje
        if (i == n - 1 && j == m - 1 && lu == cc) return;  // poseban slučaj
        b[j] = m + 2;
      }
      c[j] = cc;
      if (!ok(i, j, cc)) return;  // provjeri postaje li stanje nevaljano zbog stvaranja zatvorene komponente povezanosti
      H1->push(encode(), H0->key[u], u);
    }
    ```

Za posljednji slučaj treba paziti: ako je već stvoreno zatvoreno povezano područje, više ne smijemo bojati njegovom bojom, jer bi se inače ta boja pojavila u dvjema komponentama povezanosti. Čini se da bi takav događaj trebalo dodatno pamtiti; može se slijediti postupak iz [„ZOJ 3213” Beautiful Meadow](#primjer_2) i otvoriti još jednu dimenziju za taj događaj. No zbog posebnosti ovog zadatka možemo ga riješiti i posebnim slučajem.

???+ note "Poseban slučaj – kôd"
    ```cpp
    bool ok(int i, int j, int cc) {
      if (cc == c[j + 1]) return true;
      int up = b[j + 1];
      if (!up) return true;
      int c1 = 0, c2 = 0;
      REP(i, m + 1) if (i != j + 1) {
        if (b[i] == b[j + 1]) {  // ista povezanost, boja je sigurno ista
          assert(c[i] == c[j + 1]);
        }
        if (c[i] == c[j + 1] && b[i] == b[j + 1]) ++c1;
        if (c[i] == c[j + 1]) ++c2;
      }
      if (!c1) {               // ako bi nastala nova zatvorena komponenta povezanosti
        if (c2) return false;  // ako na konturi još postoji ista boja
        if (i < n - 1 || j < m - 2) return false;
      }
      return true;
    }
    ```

Razmotrimo još nestajanje komponente povezanosti. Nakon što obojimo neko polje, ako nijedno drugo polje nije povezano s poljem iznad njega, nastaje zatvorena komponenta povezanosti. Taj se događaj može dogoditi samo u posljednja dva stupca posljednjeg retka; inače bi se, da ne bi nastala jednobojna komponenta $2\times 2$, ta boja kasnije sigurno ponovno pojavila, osim u sljedećem slučaju:

    2 2
    o#
    #o

Taj slučaj obradimo posebno; tako u ovom zadatku možemo iz lijenosti ne pamtiti je li prije već nastala zatvorena komponenta povezanosti.

??? note "Kôd primjera"
    ```cpp
    --8<-- "docs/dp/code/plug/plug_4.cpp"
    ```

### Zadaci za vježbu

??? note "Zadatak [„Topcoder SRM 312. Div1 Hard” CheapestIsland](https://archive.topcoder.com/ProblemStatement/pm/6482)"
    Sažetak zadatka: zadana je ploča s težinom u svakom polju; odredi komponentu povezanosti s najmanjim zbrojem težina.

??? note "Zadatak [„JLOI 2009” Tajanstveno biće](https://www.luogu.com.cn/problem/P3886)"
    Sažetak zadatka: zadana je ploča s težinom u svakom polju; odredi komponentu povezanosti s najvećim zbrojem težina.

??? note "Zadatak [„AtCoder Beginner Contest 211. Problem E” Red Polyomino](https://atcoder.jp/contests/abc211/tasks/abc211_e)"
    Sažetak zadatka: zadana je ploča $N\times N$ u kojoj je svako polje na početku crno ili bijelo. Među bijelim poljima odabereš točno $K$ i obojiš ih crveno. Koliko ima bojanja u kojima crvena polja čine jednu komponentu povezanosti?

## Grafovski model

???+ note "Primjer [„NOI 2007 Day2” Prebrojavanje razapinjućih stabala](https://www.luogu.com.cn/problem/P2109)"
    Sažetak zadatka: prebrojavanje razapinjućih stabala posebne vrste grafa u kojem je svaki vrh spojen bridom s točno $k$ prethodnih vrhova.

???+ note "Primjer [„2015 ACM-ICPC Asia Shenyang Regional Contest - Problem E” Efficient Tree](https://acm.hdu.edu.cn/showproblem.php?pid=5513)"
    Sažetak zadatka: zadana je rešetka $N\times M$ i težine bridova između susjednih (četverosmjerno povezanih) polja.
    Za razapinjuće stablo rezultat svakog vrha je 1+\[postoji brid prema gore]+\[postoji brid ulijevo].
    Rezultat razapinjućeg stabla umnožak je rezultata svih vrhova.
    
    Treba odrediti: zbroj težina bridova minimalnog razapinjućeg stabla i zbroj rezultata svih minimalnih razapinjućih stabala.
    ($n\le 800,m\le 7$)

## Praksa

### Primjer

???+ note "Primjer [„HDU 4113” Construct the Great Wall](https://acm.hdu.edu.cn/showproblem.php?pid=4113)"
    Sažetak zadatka: na ploči $N\times M$ konstruiraj ciklus koji razdvaja sve `x` od svih `o`.

Postoji vrsta plug DP problema u kojima na ploči treba izgraditi zidove koji razdvajaju neke elemente ploče. Nazovimo ih problemima gradnje zidova; mogu se promatrati i kao model bojanja i kao model putova.

![greatwall](./images/greatwall.svg)

Ako ovaj zadatak promatramo kao model bojanja, treba ne samo dodatno razmatrati opseg obojanog područja, nego i prepoznavati nevaljane slučajeve dodira u kutu (slika 2). Osim toga, za razliku od [„UVa 10572” Black & White](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=1513), ovdje zid mora biti jednostavan poligon, pa je sljedeći prstenasti slučaj u ovom zadatku nevaljan.

    3 3
    ooo
    oxo
    ooo

Zato koristimo model putova i svodimo zadatak na [jedan ciklus](#jedan-ciklus).

DP izvodimo po sjecištima rešetke (pa duljinu i širinu treba uvećati za $1$); pri svakom prijelazu treba osigurati da su svi `x` izvan ciklusa, a `o` unutar ciklusa. Zato moramo održavati i je li trenutni položaj unutar ciklusa. Taj podatak možemo dodati kao dimenziju, a možemo i izravno brojati parnost broja donjih utikača na konturi ispred tog položaja (metoda zrake).

??? note "Kôd primjera"
    ```cpp
    #include <cstring>
    #include <iostream>
    using namespace std;
    #define REP(i, n) for (int i = 0; i < n; ++i)
    
    template <class T>
    bool checkMin(T &a, const T b) {
      return b < a ? a = b, true : false;
    }
    
    constexpr int N = 10, M = N;
    constexpr int offset = 3, mask = (1 << offset) - 1;
    int n, m;
    int d;
    constexpr int INF = 0x3f3f3f3f;
    int b[M + 1], bb[M + 1];
    
    int encode() {
      int s = 0;
      memset(bb, -1, sizeof(bb));
      int bn = 1;
      bb[0] = 0;
      for (int i = m; i >= 0; --i) {
    #define bi bb[b[i]]
        if (!~bi) bi = bn++;
        s <<= offset;
        s |= bi;
      }
      return s;
    }
    
    void decode(int s) {
      REP(i, m + 1) {
        b[i] = s & mask;
        s >>= offset;
      }
    }
    
    constexpr int MaxSZ = 16796, Prime = 9973;
    
    struct hashTable {
      int head[Prime], next[MaxSZ], sz;
      int state[MaxSZ];
      int key[MaxSZ];
    
      void clear() {
        sz = 0;
        memset(head, -1, sizeof(head));
      }
    
      void push(int s) {
        int x = s % Prime;
        for (int i = head[x]; ~i; i = next[i]) {
          if (state[i] == s) {
            checkMin(key[i], d);
            return;
          }
        }
        state[sz] = s, key[sz] = d;
        next[sz] = head[x];
        head[x] = sz++;
      }
    
      void roll() { REP(i, sz) state[i] <<= offset; }
    } H[2], *H0, *H1;
    
    char A[N + 1][M + 1];
    
    void push(int i, int j, int dn, int rt) {
      b[j] = dn;
      b[j + 1] = rt;
      if (A[i][j] != '.') {
        bool bad = A[i][j] == 'o';
        REP(jj, j + 1) if (b[jj]) bad ^= 1;
        if (bad) return;
      }
      H1->push(encode());
    }
    
    int solve() {
      cin >> n >> m;
      int ti, tj;
      REP(i, n) {
        scanf("%s", A[i]);
        REP(j, m) if (A[i][j] == 'o') ti = i, tj = j;
        A[i][m] = '.';
      }
      REP(j, m + 1) A[n][j] = '.';
      ++n, ++m, ++ti, ++tj;
      H0 = H, H1 = H + 1;
      H1->clear();
      d = 0;
      H1->push(0);
      int z = INF;
      REP(i, n) {
        REP(j, m) {
          swap(H0, H1);
          H1->clear();
          REP(ii, H0->sz) {
            decode(H0->state[ii]);
            d = H0->key[ii] + 1;
            int lt = b[j], up = b[j + 1];
            bool dn = i != n - 1, rt = j != m - 1;
            if (lt && up) {
              if (lt == up) {
                int cnt = 0;
                REP(i, m + 1) if (b[i])++ cnt;
                if (cnt == 2 && i == ti && j == tj) {
                  checkMin(z, d);
                }
              } else {
                REP(i, m + 1) if (b[i] == lt) b[i] = up;
                push(i, j, 0, 0);
              }
            } else if (lt || up) {
              int t = lt | up;
              if (dn) {
                push(i, j, t, 0);
              }
              if (rt) {
                push(i, j, 0, t);
              }
            } else {
              --d;
              push(i, j, 0, 0);
              ++d;
              if (dn && rt) {
                push(i, j, m, m);
              }
            }
          }
        }
        H1->roll();
      }
      if (z == INF) z = -1;
      return z;
    }
    
    int main() {
      int T;
      cin >> T;
      for (int Case = 1; Case <= T; ++Case) {
        printf("Case #%d: %d\n", Case, solve());
      }
    }
    ```

### Zadaci za vježbu

??? note "Zadatak [„SCOI 2011” Pod](https://www.luogu.com.cn/problem/P3272)"
    Sažetak zadatka: na ploči $r\times c$ neka su polja prepreke; na koliko se načina sva polja bez prepreka mogu popločati pločicama oblika L?

??? note "Zadatak [„HDU 4796” Winter's Coming](https://acm.hdu.edu.cn/showproblem.php?pid=4796)"
    Sažetak zadatka: na ploči $N\times M$ neobojana polja treba obojiti crno, bijelo i sivo tako da su sva crna i sva bijela područja povezana, da su crno i bijelo područje svako za sebe povezani s gornjim i donjim rubom ploče te da crno i bijelo područje nisu susjedni. Svako polje ima cijenu; odredi bojanje koje minimizira cijenu sivog područja.
    
    ![4796](./images/4796.jpg)

??? note "Zadatak [„ZOJ 2125” Rocket Mania](https://pintia.cn/problem-sets/91827364500/exam/problems/type/7?page=11&problemSetProblemId=91827365624)"
    Sažetak zadatka: na karti $9\times6$ u svakom je polju neka vrsta cijevi (oblika `-`,`T`,`L`,`+` ili je polje prazno); cijevi se mogu zakretati za 0°,90°,180°,270°. Koliko najviše redaka može desnim rubom biti cijevima spojeno s lijevim rubom retka X?

??? note "Zadatak [„ZOJ 2126” Rocket Mania Plus](https://pintia.cn/problem-sets/91827364500/exam/problems/type/7?page=11&problemSetProblemId=91827365625)"
    Sažetak zadatka: na karti $9\times6$ u svakom je polju neka vrsta cijevi (oblika `-`,`T`,`L`,`+` ili je polje prazno); cijevi se mogu zakretati za 0°,90°,180°,270°. Koliko najviše redaka može desnim rubom biti cijevima spojeno s lijevim rubom?

??? note "Zadatak [„World Finals 2009/2010 Harbin” Channel](https://qoj.ac/problem/13134)"
    Sažetak zadatka: na kvadratnoj karti `.` označava prazno polje, a `#` kamen; pronađi najdulji put takav da:
    
    1.  počinje u gornjem lijevom kutu, a završava u donjem desnom kutu;
    2.  ne prolazi kroz kamenje;
    3.  put sam sa sobom ne tvori ciklus u smislu osmosmjerne povezanosti (tj. ne smije se dodirivati ni u kutovima).

??? note "Zadatak [„HDU 3958” Tower Defence](https://acm.hdu.edu.cn/showproblem.php?pid=3958)"
    Sažetak zadatka: svodi se na traženje najduljeg puta od $\mathit{S}$ do $\mathit{T}$ koji se ne smije sam dodirivati, osim u kutovima.

??? note "Zadatak [„UVa 10531” Maze Statistics](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=1472)"
    Sažetak zadatka: zadana je karta $N\times M$ u kojoj svako polje nezavisno s vjerojatnošću $\mathit{p}$ postaje prepreka. Treba doći iz gornjeg lijevog kuta labirinta u donji desni kut. Za svako polje odredi vjerojatnost da je prepreka u **rješivom labirintu (tj. početak i kraj četverosmjerno su povezani)**. ($N \le 5$, $M \le 6$)

??? note "Zadatak [„Aizu 2452” Pipeline Plans](https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2452)"
    Sažetak zadatka: postoji ukupno 12 vrsta uzoraka pločica, a broj pločica svake vrste je zadan. Treba ih postaviti na pravokutni pod koji se može promatrati kao rešetka $R\times C$, po jednu pločicu na polje, tako da su središte gornjeg lijevog polja i središte donjeg desnog polja povezani crtama na uzorcima pločica. $(2 \le R \times C \le 15)$
    
    ![plug2](./images/plug2.png)

??? note "Zadatak [„SDOI 2014” Tiskana pločica](https://www.luogu.com.cn/problem/P3314)"
    Sažetak zadatka: tiskana pločica $N\times M$ na kojoj su neka polja prepreke kroz koje vodiči ne smiju prolaziti; zadano je $K$ parova polja i svaki par treba spojiti vodičem, a vodiči se međusobno ne smiju križati (dopušteno je da jedan vodič uđe u polje kroz gornji rub i izađe kroz lijevi, a drugi uđe kroz donji rub i izađe kroz desni). Vodiče promatramo kao neusmjerene bridove; odredi najmanju ukupnu duljinu vodiča koja zadovoljava uvjete i broj takvih rasporeda.

??? note "Zadatak [„SPOJ CAKE3” Delicious Cake](https://www.spoj.com/problems/CAKE3)"
    Sažetak zadatka: tortu koja se može promatrati kao rešetka $N\times M$ režemo duž linija rešetke na više komada; koliko ima različitih načina rezanja? Dva su načina jednaka ako i samo ako su svi komadi istog oblika i na istim položajima. ($\min(N,M) \le 5, \max(N,M) \le 130$)

## Bilješke uz poglavlje

Problemi plug DP-a obično su zahtjevni za kodiranje i složeni za analizu, pa pripadaju razmjerno [rubnom području](https://github.com/OI-wiki/libs/blob/master/topic/7-%E7%8E%8B%E5%A4%A9%E6%87%BF-%E8%AE%BA%E5%81%8F%E9%A2%98%E7%9A%84%E5%8D%B1%E5%AE%B3.ppt) OI/ACM natjecanja. Najklasičniji materijal o toj temi rad je [Danqi Chen](https://www.cs.princeton.edu/~danqic/) za kinesku reprezentaciju iz 2008. – [Problemi dinamičkog programiranja temeljeni na sažimanju stanja povezanosti](https://github.com/AngelKitty/review_the_national_post-graduate_entrance_examination/tree/master/books_and_notes/professional_courses/data_structures_and_algorithms/sources/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F%E8%AE%BA%E6%96%87/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2008%E8%AE%BA%E6%96%87%E9%9B%86/%E9%99%88%E4%B8%B9%E7%90%A6%E3%80%8A%E5%9F%BA%E4%BA%8E%E8%BF%9E%E9%80%9A%E6%80%A7%E7%8A%B6%E6%80%81%E5%8E%8B%E7%BC%A9%E7%9A%84%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E9%97%AE%E9%A2%98%E3%80%8B). Nadalje, notonlysuccess s HDU-a 2011. je na blogu napisao dva uzastopna tematska članka od jednostavnijeg prema složenijem; i to je rijetko dobar materijal, no danas ga treba iskopati iz Web Archivea.

-   [notonlysuccess, 【Zbirka】Plug DP](https://web.archive.org/web/20110815044829/http://www.notonlysuccess.com/?p=625)
-   [notonlysuccess, 【Potpuna inačica】Plug DP](https://web.archive.org/web/20111007185146/http://www.notonlysuccess.com/?p=931)

### Popločavanje dominama

[„HDU 1400” Mondriaan’s Dream](https://acm.hdu.edu.cn/showproblem.php?pid=1400) pojavljuje se i u knjizi [„Training Guide for Algorithm Contests”](../contest/resources.md#书籍) kao primjer u odjeljku „Dinamičko programiranje po konturi”. [Popločavanje dominama (Domino tiling)](https://en.wikipedia.org/wiki/Domino_tiling) klasična je skupina matematičkih problema; malom promjenom ograničenja dobivaju se potproblemi različite težine koji zahtijevaju različite algoritme.

Za $m=2$ popločavanje dominama ekvivalentno je Fibonaccijevu nizu. Knjiga [„Concrete Mathematics”](https://www.csie.ntu.edu.tw/~r97002/temp/Concrete%20Mathematics%202e.pdf) tim problemom uvodi Fibonaccijev niz i na više načina izvodi njegovo rješenje u zatvorenom obliku.

Za $m\le 10,n\le 10^9$ jednadžbu prijelaza možemo unaprijed zapisati u obliku matrice i [ubrzati množenjem matrica](http://www.matrix67.com/blog/archives/276).

![domino\_v2\_transform\_matrix](./images/domino_v2_transform_matrix.svg)

Za $n,m\le 100$ broj savršenih sparivanja odgovarajućeg planarnog grafa možemo izračunati [FKT algoritmom](https://en.wikipedia.org/wiki/FKT_algorithm).

-   [„51nod 1031” Popločavanje dominama](https://www.51nod.com/Html/Challenge/Problem.html#problemId=1031)
-   [„51nod 1033” Popločavanje dominama V2](https://www.51nod.com/Html/Challenge/Problem.html#problemId=1033)|[„Vijos 1194” Domino](https://vijos.org/p/1194)
-   [„51nod 1034” Popločavanje dominama V3](https://www.51nod.com/Html/Challenge/Problem.html#problemId=1034)|[„Ural 1594” Aztec Treasure](https://acm.timus.ru/problem.aspx?space=1&num=1594)
-   [Wolfram MathWorld, Chebyshev Polynomial of the Second Kind](https://mathworld.wolfram.com/ChebyshevPolynomialoftheSecondKind.html)

### Jedan put

„Jedan put” poseban je slučaj problema [Hamiltonova puta (Hamiltonian Path)](https://en.wikipedia.org/wiki/Hamiltonian_path) u [rešetkastom grafu (Grid Graph)](https://mathworld.wolfram.com/GridGraph.html). Problem odluke o postojanju Hamiltonova puta važan je član obitelji [NP-potpunih](https://en.wikipedia.org/wiki/NP-completeness) problema.
