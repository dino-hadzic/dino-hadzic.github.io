---
title: Stablo blokova (round-square tree)
---

Prije čitanja obvezno se upoznajte s [Osnovnim pojmovima teorije grafova](./concept.md).

Srodno štivo: [Artikulacijski vrhovi i mostovi](./cut.md).

## Uvod

Dobro je poznato da stabla (ili šume) imaju vrlo lijepa svojstva i da se lako održavaju mnogim uobičajenim strukturama podataka.

Opći grafovi nemaju tako lijepa svojstva, ali srećom katkad možemo neke probleme na općem grafu prevesti na stablo.

Stablo blokova (block forest ili round-square tree, „stablo okruglih i kvadratnih vrhova”)[^ref1] upravo je jedan način da graf pretvorimo u stablo. U ovom članku opisujemo izgradnju, svojstva i neke primjene stabla blokova.

Zbog ograničenog prostora neke tvrdnje u članku nisu dokazane; čitatelj ih može sam razumjeti ili dokazati.

## Definicija

Stablo blokova izvorno je bilo alat za obradu „kaktusa” (neusmjerenih grafova u kojima je svaki brid u najviše jednom jednostavnom ciklusu), no istražujući njegova daljnja svojstva, katkad ga možemo koristiti i na općim neusmjerenim grafovima.

Da bismo uveli stablo blokova, prvo moramo uvesti **vršno dvostruko povezane komponente**.

Jedna definicija **vršno dvostruko povezanog grafa** glasi: između svaka dva različita vrha grafa postoje barem dva puta koji ne dijele vrhove.  
„Ne dijele vrhove” znači i da se vrhovi na putu ne ponavljaju (jednostavan put) i da je presjek dvaju putova prazan (naravno, oba puta nužno prolaze kroz početni i završni vrh, što ovdje ne uzimamo u obzir).

Vidimo da je za graf s jednim vrhom teško definirati je li vršno dvostruko povezan, pa grafove s $1$ vrhom zasad ne razmatramo.

Gotovo ekvivalentna definicija glasi: graf bez artikulacijskih vrhova.  
Ta definicija zakazuje samo kad graf ima samo dva vrha i jedan brid koji ih spaja. Takav graf nema artikulacijskih vrhova, ali se ne mogu naći dva disjunktna puta jer postoji samo jedan put.  
(Može se shvatiti i tako da se taj jedan put računa dvaput; presjek je doista prazan jer ne prolazi kroz druge vrhove.)

Iako je izvorna definicija zaista prva, radi jednostavnosti za vršno dvostruko povezan graf uzimamo drugu definiciju.

**Vršno dvostruko povezana komponenta** grafa je **maksimalni vršno dvostruko povezani podgraf**.  
Za razliku od jako povezanih komponenata i sl., vrh može pripadati više v-BCC-ova, ali brid pripada točno jednom v-BCC-u (ako bismo uzeli prvu definiciju, mogao bi ne pripadati nijednom).

U stablu blokova svakom izvornom vrhu odgovara jedan **okrugli vrh**, a svakom v-BCC-u jedan **kvadratni vrh**.  
Ukupno dakle ima $n+c$ vrhova, gdje je $n$ broj vrhova izvornog grafa, a $c$ broj vršno dvostruko povezanih komponenata izvornog grafa.

Za svaku vršno dvostruko povezanu komponentu njezin kvadratni vrh spojimo bridom sa svakim vrhom te komponente.  
Svaki v-BCC tvori jednu „zvijezdu”, a više „zvijezda” povezano je artikulacijskim vrhovima izvornog grafa (jer su vrhovi koji razdvajaju v-BCC-ove upravo artikulacijski vrhovi).

Očito svaki brid stabla blokova spaja jedan okrugli i jedan kvadratni vrh.

Slike dolje prikazuju v-BCC-ove jednog grafa i oblik njegova stabla blokova.[^ref2]

![](./images/block-forest1.svg)![](./images/block-forest2.svg)![](./images/block-forest3.svg)

Broj vrhova stabla blokova manji je od $2n$, jer je broj artikulacijskih vrhova manji od $n$; zato pazite da sve nizove dimenzionirate dvostruko.

Zapravo je „stablo blokova” stablo samo ako je izvorni graf povezan; ako izvorni graf ima $k$ povezanih komponenata, njegovo stablo blokova je šuma od $k$ stabala.

Ako neka povezana komponenta izvornog grafa ima samo jedan vrh, treba je razmotriti zasebno; u daljnjem razmatranju izolirane vrhove ne uzimamo u obzir.

## Postupak

Kako za zadani graf izgraditi stablo blokova? Prvo uočimo da nepovezan graf možemo rastaviti na povezane podgrafove i svaki razmatrati zasebno, pa promatramo samo povezane grafove.

Budući da se stablo blokova temelji na vršno dvostruko povezanim komponentama, a one na artikulacijskim vrhovima, dovoljno je upotrijebiti metodu sličnu traženju artikulacijskih vrhova.

Uobičajeni algoritam za traženje artikulacijskih vrhova je Tarjanov algoritam; ako ga znate, ono što slijedi bit će vam jednostavno, a ako ne znate, ni to nije problem.

Preskačemo Tarjanovo traženje artikulacijskih vrhova i izravno opisujemo algoritam za stablo blokova (zapravo inačicu Tarjanova algoritma):

Na grafu izvodimo DFS i pritom koristimo dva ključna niza, `dfn` i `low` (slično Tarjanu).

`dfn[u]` čuva DFS redni broj vrha $u$, tj. koji je po redu posjećen pri prvom posjetu.  
`low[u]` čuva **najmanji** DFS redni broj vrha do kojeg neki vrh $v$ iz podstabla vrha $u$ u DFS stablu može doći **najviše jednim povratnim bridom ili stablastim bridom prema roditelju**.  
Ako niste čuli za Tarjanov algoritam, možda je to malo teže razumjeti, pa evo primjera:

![](./images/block-forest4.svg)

(Uočite da je ovaj graf zapravo ekvivalentan grafu na gornjim slikama.)  
Stablasti bridovi nacrtani su ravnim linijama odozgo prema dolje, a povratni bridovi krivuljama odozdo prema gore. Oznaka vrha ujedno je njegov DFS redni broj.

Niz `low` tada glasi:

|        $i$        | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ |
| :---------------: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| $\mathrm{low}[i]$ | $1$ | $1$ | $1$ | $3$ | $3$ | $4$ | $3$ | $3$ | $7$ |

Nije teško, zar ne? Uočite da je `low` vrha $9$ ovdje $7$, što se razlikuje od nekih postupaka za artikulacijske vrhove, jer smo radi jednostavnosti dopustili prelazak prema gore roditeljskim bridom; osnovna je ideja ipak ista.

Lako možemo napisati DFS funkciju koja računa `dfn` i `low` (niz `dfn` na početku je nula):

???+ note "Implementacija"
    === "C++"
        ```cpp
        void Tarjan(int u) {
          low[u] = dfn[u] = ++dfc;                // low se inicijalizira na dfn trenutačnog vrha
          for (int v : G[u]) {                    // obiđi susjede vrha u
            if (!dfn[v]) {                        // ako još nije posjećen
              Tarjan(v);                          // rekurzija
              low[u] = std::min(low[u], low[v]);  // za neposjećene uzmi min s low
            } else
              low[u] = std::min(low[u], dfn[v]);  // za posjećene uzmi min s dfn
          }
        }
        ```
    
    === "Python"
        ```python
        def Tarjan(u):
            low[u] = dfn[u] = dfc  # low se inicijalizira na dfn trenutačnog vrha
            dfc = dfc + 1
            for v in G[u]:  # obiđi susjede vrha u
                if dfn[v] == False:  # ako još nije posjećen
                    Tarjan(v)  # rekurzija
                    low[u] = min(low[u], low[v])  # za neposjećene uzmi min s low
                else:
                    low[u] = min(low[u], dfn[v])  # za posjećene uzmi min s dfn
        ```

Zatim razmotrimo vezu između v-BCC-ova, DFS stabla i tih dvaju nizova.

Vidimo da je svaki v-BCC u DFS stablu povezano podstablo s barem dva vrha; posebno, najviši vrh prema dolje ima samo jedno dijete unutar komponente.

Također vidimo da je svaki stablasti brid u točno jednom v-BCC-u.

Promotrimo najviši vrh $u$ nekog v-BCC-a u DFS stablu; taj v-BCC prepoznajemo u vrhu $u$, jer podstablo vrha $u$ sadrži sve podatke o toj komponenti.

Budući da ima barem dva vrha, promotrimo sljedeći vrh $v$ te komponente; između $u$ i $v$ postoji stablasti brid.

Lako se vidi da tada nužno vrijedi $\mathrm{low}[v]=\mathrm{dfn}[u]$.  
Preciznije: za stablasti brid $u\to v$, vrhovi $u,v$ su u istom v-BCC-u i $u$ je vrh najmanje dubine u tom v-BCC-u **ako i samo ako** $\mathrm{low}[v]=\mathrm{dfn}[u]$.

Tako tijekom DFS-a možemo utvrditi gdje postoje v-BCC-ovi, ali još ne možemo točno odrediti skup vrhova pojedinog v-BCC-a.

To nije teško riješiti: tijekom DFS-a održavamo stog u kojem su vrhovi čiji v-BCC (možda ih je više) još nije utvrđen.

Kad nađemo v-BCC, svi njegovi vrhovi osim $u$ nalaze se na vrhu stoga; dovoljno je skidati sa stoga dok ne skinemo $v$.

Pritom skinute vrhove možemo odmah obraditi: samo ih spojimo bridom s novim kvadratnim vrhom. Na kraju i $u$ spojimo s kvadratnim vrhom.

Time je izgradnja stabla blokova prirodno dovršena; kvadratne vrhove numeriramo cijelim brojevima od $n+1$ nadalje, čime se okrugli i kvadratni vrhovi jasno razlikuju.

Ovaj je dio možda opisan nedovoljno jasno, pa dolje prilažemo kôd s iscrpnim komentarima, ispisima koji pomažu razumijevanju i jednim test-primjerom; preporučujemo da kopirate kôd i sami ga isprobate, jer kôd najbolje pomaže razumijevanju (ne zaboravite uključiti `c++11`).

???+ note "Implementacija"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <vector>
    
    constexpr int MN = 100005;
    
    int N, M, cnt;
    std::vector<int> G[MN], T[MN * 2];
    
    int dfn[MN], low[MN], dfc;
    int stk[MN], tp;
    
    void Tarjan(int u) {
      printf("  Enter : #%d\n", u);
      low[u] = dfn[u] = ++dfc;                // low se inicijalizira na dfn trenutačnog vrha
      stk[++tp] = u;                          // stavi na stog
      for (int v : G[u]) {                    // obiđi susjede vrha u
        if (!dfn[v]) {                        // ako još nije posjećen
          Tarjan(v);                          // rekurzija
          low[u] = std::min(low[u], low[v]);  // za neposjećene uzmi min s low
          if (low[v] == dfn[u]) {  // znači da smo našli v-BCC s korijenom u
            ++cnt;                 // povećaj broj kvadratnih vrhova
            printf("  Found a New BCC #%d.\n", cnt - N);
            // skini sa stoga vrhove v-BCC-a osim u i spoji ih bridom u stablu blokova
            for (int x = 0; x != v; --tp) {
              x = stk[tp];
              T[cnt].push_back(x);
              T[x].push_back(cnt);
              printf("    BCC #%d has vertex #%d\n", cnt - N, x);
            }
            // i sam u treba spojiti (ali ne skidati sa stoga)
            T[cnt].push_back(u);
            T[u].push_back(cnt);
            printf("    BCC #%d has vertex #%d\n", cnt - N, u);
          }
        } else
          low[u] = std::min(low[u], dfn[v]);  // za posjećene uzmi min s dfn
      }
      printf("  Exit : #%d : low = %d\n", u, low[u]);
      printf("  Stack:\n    ");
      for (int i = 1; i <= tp; ++i) printf("%d, ", stk[i]);
      puts("");
    }
    
    int main() {
      scanf("%d%d", &N, &M);
      cnt = N;  // oznake v-BCC-ova / kvadratnih vrhova počinju od N
      for (int i = 1; i <= M; ++i) {
        int u, v;
        scanf("%d%d", &u, &v);
        G[u].push_back(v);  // dodaj brid u oba smjera
        G[v].push_back(u);
      }
      // obrada nepovezanog grafa
      for (int u = 1; u <= N; ++u)
        if (!dfn[u]) Tarjan(u), --tp;
      // uoči da pri izlasku iz Tarjana na stogu ostaje još jedan element, korijen; skini ga
      return 0;
    }
    ```

Evo jednog test-primjera:

```text
13 15
1 2
2 3
1 3
3 4
3 5
4 5
5 6
4 6
3 7
3 8
7 8
7 9
10 11
11 10
11 12
```

Graf koji odgovara tom primjeru (uključuje višestruke bridove i izolirani vrh):

![](./images/block-forest5.svg)

## Primjeri

Prikazujemo nekoliko zadataka koji se mogu riješiti stablom blokova.

???+ note "[„APIO2018” Duatlon](https://loj.ac/p/2587)"
    ??? note "Sažetak zadatka"
        Zadan je jednostavan neusmjeren graf; koliko ima uređenih trojki $\langle s, c, f \rangle$ ($s, c, f$ međusobno različiti) takvih da postoji jednostavan put koji kreće iz $s$, prolazi kroz $c$ i stiže u $f$?
    
    ??? note "Rješenje"
        Kad govorimo o jednostavnim putovima, moramo spomenuti jedno vrlo lijepo svojstvo v-BCC-ova: za dva vrha u istom v-BCC-u unija svih jednostavnih putova između njih točno je jednaka tom v-BCC-u.  
        Drugim riječima, između dvaju različitih vrhova $u,v$ istog v-BCC-a sigurno postoji jednostavan put koji prolazi kroz zadani treći vrh $w$ istog v-BCC-a.
        
        Dokaz tog svojstva:
        
        -   Očito, ako jednostavan put napusti v-BCC, više se ne može vratiti u njega, jer bi to proturječilo definiciji v-BCC-a.
        -   Stoga je dovoljno dokazati da za bilo koja tri različita vrha $u,v,c$ vršno dvostruko povezanog grafa postoji jednostavan put od $u$ do $v$ koji prolazi kroz $c$.
        -   Prvo isključimo slučaj s $2$ vrha: on zadovoljava svojstvo, ali se ne mogu odabrati $3$ različita vrha.
        -   U preostalim slučajevima izgradimo model protoka u mreži: izvor spojimo s $c$ bridom kapaciteta $2$, a $u$ i $v$ s ponorom bridovima kapaciteta $1$.
        -   Dvosmjerni brid $\langle x,y\rangle$ izvornog grafa postaje brid od $x$ do $y$ kapaciteta $1$ i brid od $y$ do $x$ kapaciteta $1$.
        -   Na kraju svakom vrhu osim izvora, ponora i $c$ dodijelimo kapacitet $1$, što se postiže razdvajanjem vrhova.
        -   Budući da brid od izvora do $c$ ima kapacitet $2$, ako je maksimalni protok te mreže $2$, dokazano je da postoji put kroz $c$.
        -   Prema teoremu o maksimalnom protoku i minimalnom rezu, minimalni rez očito je najviše $2$; preostaje dokazati da je minimalni rez veći od $1$.
        -   To je ekvivalentno dokazu da rezanje bilo kojeg jednog brida kapaciteta $1$ ne može razdvojiti izvor i ponor.
        -   Ako režemo brid koji $u$ ili $v$ spaja s ponorom, prema prvoj definiciji v-BCC-a sigurno postoji jednostavan put od $c$ do drugog, neodrezanog vrha.
        -   Ako režemo brid nastao razdvajanjem nekog vrha, to je ekvivalentno brisanju vrha; prema drugoj definiciji v-BCC-a preostali graf ostaje povezan.
        -   Ako režemo brid nastao iz izvornog brida, to je ekvivalentno brisanju brida, što je slabije od brisanja vrha, pa put očito postoji.
        -   Time smo dokazali da je minimalni rez veći od $1$, tj. maksimalni protok jednak je $2$. Q.E.D.
        
        Što nam ta tvrdnja govori? Govori nam: ako promatramo put između dvaju okruglih vrhova u stablu blokova, skup okruglih vrhova susjednih kvadratnim vrhovima na tom putu jednak je skupu vrhova na jednostavnim putovima između ta dva vrha u izvornom grafu.
        
        Vratimo se zadatku: fiksirajmo $s$ i $f$ i tražimo broj valjanih $c$; očito je broj valjanih $c$ jednak broju vrhova u uniji jednostavnih putova između $s,f$ minus $2$ (bez samih $s,f$).
        
        Nakon što izgradimo stablo blokova izvornog grafa, broj vrhova na jednostavnim putovima između dvaju vrhova ovisi o broju kvadratnih (v-BCC) i okruglih vrhova na njihovu putu u stablu blokova.
        
        Slijedi uobičajen trik sa stablom blokova: pri brojanju putova vrhovima dodijelimo prikladne težine.  
        U ovom zadatku težina svakog kvadratnog vrha jednaka je veličini pripadnog v-BCC-a, a težina svakog okruglog vrha je $-1$.
        
        S takvim težinama zbroj težina vrhova na putu između dvaju okruglih vrhova u stablu blokova točno je jednak veličini unije jednostavnih putova u izvornom grafu minus $2$.
        
        Problem se svodi na računanje $\sum$ zbrojeva težina na putovima između svih parova okruglih vrhova u stablu blokova.
        
        Pogledajmo iz drugog kuta: računajmo doprinos svakog vrha odgovoru, tj. njegovu težinu pomnoženu s brojem putova koji kroz njega prolaze; to se dobiva jednostavnim DP-om na stablu.
        
        Na kraju, ne zaboravite obraditi slučaj nepovezanog grafa. Evo pripadnog koda:
    
    ??? note "Referentni kôd"
        ```cpp
        --8<-- "docs/graph/code/block-forest/block-forest_1.cpp"
        ```
    
    Usput, odgovor za maloprijašnji test-primjer u ovom zadatku je $212$.

???+ note "[Codeforces #487 E. Tourists](https://codeforces.com/contest/487/problem/E)"
    ??? note "Sažetak zadatka"
        Zadan je jednostavan neusmjeren povezan graf; treba podržati dvije vrste operacija:
        
        1.  Promijeni težinu nekog vrha.
        
        2.  Upit: minimum težina vrhova na svim jednostavnim putovima između dvaju vrhova.
    
    ??? note "Rješenje"
        Jednako tako izgradimo stablo blokova izvornog grafa, težinu kvadratnog vrha postavimo na minimum težina susjednih okruglih vrhova i problem se svodi na minimum na putu.
        
        Minimum na putu može se održavati heavy-light dekompozicijom i segment treeom, ali što s promjenama?
        
        Promjena težine jednog okruglog vrha zahtijeva promjenu svih susjednih kvadratnih vrhova, što se lako svede na $O(n)$ promjena.
        
        Ovdje iskoristimo to što je stablo blokova stablo: težinu kvadratnog vrha postavimo na minimum težina njegove djece okruglih vrhova; tada pri promjeni treba ažurirati samo roditeljski kvadratni vrh.
        
        Za održavanje kvadratnih vrhova dovoljno je za svaki kvadratni vrh držati jedan `multiset` sa skupom težina.
        
        Treba paziti da pri upitu, ako je LCA kvadratni vrh, treba uzeti u obzir i težinu roditeljskog okruglog vrha tog LCA.
        
        Napomena: broj vrhova stabla blokova treba dimenzionirati na dvostruki broj vrhova izvornog grafa, inače će niz prekoračiti granice.
    
    ??? note "Referentni kôd"
        ```cpp
        --8<-- "docs/graph/code/block-forest/block-forest_2.cpp"
        ```

???+ note "[„SDOI2018” Strateška igra](https://loj.ac/p/2562)"
    ??? note "Sažetak zadatka"
        Zadan je jednostavan neusmjeren povezan graf. Postavlja se $q$ upita:
        
        u svakom je zadan skup vrhova $S$ ($2 \le |S| \le n$); koliko ima vrhova $u$ takvih da $u \notin S$ i da nakon brisanja $u$ vrhovi iz $S$ nisu svi u istoj povezanoj komponenti?
        
        Svaka test-točka ima više skupova podataka.
    
    ??? note "Rješenje"
        Prvo izgradimo stablo blokova; upit postaje: broj okruglih vrhova u povezanom podgrafu stabla blokova koji odgovara skupu $S$, minus $|S|$.
        
        Kako izračunati broj okruglih vrhova u povezanom podgrafu? Jedan način:
        
        težinu okruglog vrha stavimo na brid između njega i njegova roditeljskog kvadratnog vrha; problem se svodi na zbroj težina bridova, za što se može pogledati jedno rješenje zadatka [„SDOI2015” Potraga za blagom](https://loj.ac/p/2182).  
        Naime, vrhove iz $S$ sortiramo po DFS redoslijedu, zbrojimo udaljenosti između susjednih vrhova u tom poretku (uključujući udaljenost između prvog i posljednjeg); odgovor je polovica tog zbroja, jer se svaki brid prijeđe točno dvaput.
        
        Na kraju, ako je vrh najmanje dubine u podgrafu okrugli, odgovoru treba dodati $1$, jer ga nismo prebrojali.
        
        Zbog više skupova podataka pazite na inicijalizaciju nizova.
    
    ??? note "Referentni kôd"
        ```cpp
        --8<-- "docs/graph/code/block-forest/block-forest_3.cpp"
        ```

## Zadaci za vježbu

-   [UVa 1464 Traffic Real Time Query](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=447&page=show_problem&problem=4210)
-   [Luogu P4320 Susret na cesti](https://www.luogu.com.cn/problem/P4320)
-   [Luogu P10517 Prostorno planiranje](https://www.luogu.com.cn/problem/P10517)

## Vanjske poveznice

immortalCO, [Stablo blokova — moćan alat za kaktuse](https://immortalco.blog.uoj.ac/blog/1955), Universal OJ.

## Literatura i bilješke

[^ref1]: Godine 2017. Chen Junkun definirao je i imenovao strukturu stabla blokova u svom radu za kineski IOI2017 nacionalni pripremni tim, „Izvještaj o zadatku 'Čudesni podgraf' i proširenja”.

[^ref2]: Chen Junkun, „Obično stablo blokova i čudesno (~~dinamičko~~) dinamičko programiranje”, zimski kamp NOI2018, str. 4.
