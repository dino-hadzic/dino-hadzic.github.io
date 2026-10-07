---
title: Link Cut Tree
---

## Uvod

Link/Cut Tree struktura je podataka kojom rješavamo **problem dinamičkog stabla**.

Link/Cut Tree naziva se i Link-Cut Tree, skraćeno LCT, ali ne zove se „dinamičko stablo”; dinamičko stablo naziv je za klasu problema.

Splay Tree temelj je LCT-a, no Splay Tree koji LCT koristi u detaljima se razlikuje od običnog Splaya (ima nekoliko proširenja).

## Uvodni problem

Održavajte stablo uz sljedeće operacije:

-   promjena težina na putu između dvaju čvorova;
-   upit zbroja težina na putu između dvaju čvorova;
-   promjena težina u podstablu nekog čvora;
-   upit zbroja težina u podstablu nekog čvora.

To je ogledni zadatak za heavy-light dekompoziciju.

Dodajmo još jednu operaciju:

-   odspoji i spoji neke bridove tako da rezultat i dalje bude stablo.

Odgovore treba davati online.

Time problem postaje problem dinamičkog stabla, koji se može riješiti LCT-om.

## Problem dinamičkog stabla

Održavamo **šumu** uz brisanje bridova i dodavanje bridova, pri čemu se jamči da nakon dodavanja i brisanja rezultat ostaje šuma. Želimo održavati neke informacije o toj šumi.

Uobičajene su operacije: povezanost dvaju čvorova, zbroj težina na putu između dvaju čvorova, spajanje dvaju čvorova i rezanje brida, promjena informacija itd.

### Pogled na heavy-light dekompoziciju iz perspektive LCT-a

-   Cijelo stablo dekomponiramo prema veličinama podstabala i čvorove prenumeriramo.
-   Primjećujemo da se nakon prenumeracije na stablu pojavljuju uzastopni intervali po lancima, nad kojima možemo raditi intervalne operacije segment treeom.

### Prelazak na problem dinamičkog stabla

Dekompozicija koju smo upravo opisali koristi veličinu podstabla kao kriterij podjele. Možemo li definirati drukčiju dekompoziciju, prikladniju za problem dinamičkog stabla?

Razmislimo kakvi lanci trebaju problemu dinamičkog stabla.

Budući da dinamički održavamo šumu, očito želimo da lance biramo sami, kako bismo ih mogli iskoristiti za rješavanje.

## Dekompozicija na odabrane lance

Među bridovima od čvora prema njegovoj djeci sami odaberemo jedan brid po kojem dekomponiramo; odabrani brid nazivamo punim bridom, a ostale virtualnim bridovima. Dijete povezano punim bridom nazivamo punim djetetom. Lanac sastavljen od punih bridova nazivamo punim lancem. Zapamtite najvažniji razlog zašto biramo ovu dekompoziciju: lance biramo sami, pa je fleksibilna i promjenjiva. Upravo zbog te fleksibilnosti pune lance održavamo Splay Treeom.

## LCT

LCT možemo jednostavno shvatiti kao skup Splayeva koji održavaju dinamičku dekompoziciju stabla na lance, radi intervalnih operacija na dinamičkom stablu. Za svaki puni lanac gradimo jedan Splay koji održava informacije cijelog lanca kao intervala.

## Pomoćno stablo

Pogledajmo najprije svojstva pomoćnog stabla, a zatim na slici konkretnu strukturu pomoćnog stabla.

U ovom članku možete smatrati da skup Splayeva čini pomoćno stablo, svako pomoćno stablo održava jedno stablo, a skup pomoćnih stabala čini LCT, koji održava cijelu šumu.

1.  Pomoćno stablo sastoji se od više Splayeva; svaki Splay održava jedan put u izvornom stablu, a niz čvorova dobiven inorder obilaskom tog Splaya od početka do kraja odgovara putu „odozgo prema dolje” u izvornom stablu.
2.  Čvorovi izvornog stabla i čvorovi Splayeva pomoćnog stabla u bijekciji su.
3.  Splayevi pomoćnog stabla nisu međusobno neovisni. Roditelj korijena svakog Splaya trebao bi biti prazan, no u LCT-u roditelj korijena svakog Splaya pokazuje na roditelja **tog lanca** u izvornom stablu (tj. na roditelja najvišeg čvora lanca). Takva roditeljska veza razlikuje se od uobičajene roditeljske veze u Splayu po tome što dijete poznaje roditelja, a roditelj ne poznaje dijete; ona odgovara **virtualnom bridu** izvornog stabla. Stoga u svakoj komponenti povezanosti točno jedan čvor ima prazan roditelj.
4.  Zbog navedenih svojstava pomoćnog stabla ni za jednu operaciju ne trebamo održavati izvorno stablo: iz pomoćnog stabla uvijek možemo jednoznačno izvući izvorno stablo, pa je dovoljno održavati samo pomoćno stablo.

Neka je zadano izvorno stablo kao na slici. (Podebljani bridovi su puni, isprekidani su virtualni.)

![tree](images/lct-atree-1.svg)

Prema upravo danoj definiciji struktura pomoćnog stabla izgleda ovako.

![auxtree](images/lct-atree-2.svg)

### Odnos strukture izvornog i pomoćnog stabla

-   Puni lanac u izvornom stablu: u pomoćnom stablu svi su njegovi čvorovi u istom Splayu.
-   Virtualni lanac u izvornom stablu: u pomoćnom stablu Father Splaya u kojem je dijete pokazuje na roditelja, ali nijedno od dvoje djece roditelja ne pokazuje na dijete.
-   Napomena: korijen izvornog stabla nije isto što i korijen pomoćnog stabla.
-   Father u izvornom stablu nije isto što i Father u pomoćnom stablu.
-   Pomoćnom stablu može se proizvoljno mijenjati korijen dok god vrijede svojstva pomoćnog stabla i Splaya.
-   Pretvaranje virtualnih lanaca u pune i obrnuto lako se izvodi na pomoćnom stablu, čime je ostvareno dinamičko održavanje dekompozicije na lance.

### Deklaracije varijabli koje slijede

-   `ch[N][2]` lijevo i desno dijete
-   `f[N]` pokazivač na roditelja
-   `sum[N]` zbroj težina na putu
-   `val[N]` težina čvora
-   `tag[N]` oznaka obrtanja
-   `laz[N]` oznaka težina
-   `siz[N]` veličina podstabla u pomoćnom stablu
-   Other\_Vars

### Deklaracije funkcija

#### Uobičajene funkcije struktura podataka (doslovno značenje)

1.  `PushUp(x)`
2.  `PushDown(x)`

#### Funkcije Splay Treea

Slijede funkcije koje se koriste u Splay Treeu; detalje potražite u članku [Splay Tree](./splay.md).

1.  `Get(x)` vraća koje je dijete $x$ svog roditelja.
2.  `Splay(x)` zajedno s operacijom Rotate rotira $x$ do **korijena trenutnog Splaya**.
3.  `Rotate(x)` rotira $x$ za jednu razinu prema gore.

#### Nove operacije

1.  `Access(x)` stavlja sve čvorove od korijena do $x$ u isti puni lanac, tako da put od korijena do $x$ postane puni put i nađe se u istom Splayu. **Samo je ovu operaciju nužno implementirati; ostale se implementiraju prema potrebama zadatka.**
2.  `IsRoot(x)` provjerava je li $x$ korijen stabla u kojem se nalazi.
3.  `Update(x)` nakon operacije `Access` rekurzivno odozgo prema dolje izvodi `PushDown` i ažurira informacije.
4.  `MakeRoot(x)` čini $x$ korijenom stabla u kojem se nalazi.
5.  `Link(x, y)` spaja čvorove $x, y$ bridom.
6.  `Cut(x, y)` briše brid između čvorova $x, y$.
7.  `Find(x)` vraća indeks korijena stabla u kojem se nalazi $x$.
8.  `Fix(x, v)` mijenja težinu čvora $x$ u $v$.
9.  `Split(x, y)` izdvaja put između $x, y$ radi intervalnih operacija.

### Makro-definicije

-   `#define ls ch[p][0]`
-   `#define rs ch[p][1]`

## Objašnjenje funkcija

### `PushUp()`

```cpp
void PushUp(int p) {
  // maintain other variables
  siz[p] = siz[ls] + siz[rs] + 1;
}
```

### `PushDown()`

```cpp
void PushDown(int p) {
  if (tag[p] != std_tag) {
    // pushdown the tag
    tag[p] = std_tag;
  }
}
```

### `Splay() && Rotate()`

Ovdje se `Splay()` i `Rotate()` malo razlikuju od implementacije u Splay Treeu.

```cpp
#define Get(x) (ch[f[x]][1] == x)

void Rotate(int x) {
  int y = f[x], z = f[y], k = Get(x);
  if (!isRoot(y)) ch[z][ch[z][1] == y] = x;
  // gornji redak mora biti na početku; običnom Splayu ne treba, zbog isRoot  (objašnjeno kasnije)
  ch[y][k] = ch[x][!k], f[ch[x][!k]] = y;
  ch[x][!k] = y, f[y] = x, f[x] = z;
  PushUp(y), PushUp(x);
}

void Splay(int x) {
  Update(
      x);  // odmah ćemo vidjeti; prije Splaya treba PushDown na svim čvorovima puta kroz koji rotacije prolaze
  for (int fa; fa = f[x], !isRoot(x); Rotate(x)) {
    if (!isRoot(fa)) Rotate(Get(fa) == Get(x) ? fa : x);
  }
}
```

Za gornje funkcije pogledajte članak [Splay Tree](./splay.md).

Slijede funkcije specifične za LCT.

### `isRoot()`

```cpp
// kao što smo rekli, LCT ima svojstvo: ako dijete nije puno dijete, roditelj ga ne može pronaći
// stoga, ako čvor nije ni lijevo ni desno dijete svog roditelja, on je korijen trenutnog Splaya
#define isRoot(x) (ch[f[x]][0] != x && ch[f[x]][1] != x)
```

### `Access()`

```cpp
// Access je ključna operacija LCT-a;
// zamislite da želimo obraditi put, a taj je put upravo jedan naš trenutni Splay:
// dovoljno je izravno upotrijebiti njegove informacije. Pogledajmo kod, a zatim postupak uz slike
int Access(int x) {
  int p;
  for (p = 0; x; p = x, x = f[x]) {
    Splay(x), ch[x][1] = p, PushUp(x);
  }
  return p;
}
```

-   Imamo ovakvo stablo; pune linije su puni bridovi, isprekidane virtualni.

    ![initial tree](images/lct-access-1.svg)

-   Njegovo pomoćno stablo moglo bi izgledati ovako (uz drukčiji način izgradnje struktura LCT-a može biti drukčija).

    ![initial auxtree](images/lct-access-2.svg)

-   Sada želimo izvesti `Access(N)`: sve bridove na putu od $A$ do $N$ učiniti punima i rastegnuti ih u jedan Splay.

    ![access tree](images/lct-access-3.svg)

-   Implementacija postupno ažurira Splayeve odozdo prema gore.

-   Najprije $N$ rotiramo do korijena trenutnog Splaya.

-   Da bismo očuvali svojstva AuxTreea (pomoćnog stabla), dosadašnji puni brid od $N$ do $O$ mora postati virtualan.

-   Zbog svojstva „dijete poznaje roditelja, roditelj ne poznaje dijete” možemo jednostrano postaviti dijete od $N$ na `NULL`.

-   Tako dosadašnji AuxTree iz donje slike prelazi u sliku ispod nje.

    ![step 1 auxtree](images/lct-access-4.svg)

-   U sljedećem koraku i Father od $N$, čvor $I$, rotiramo do korijena Splaya u kojem je $I$.

-   Dosadašnji puni brid $I$—$K$ treba ukloniti; desno dijete od $I$ postavimo na $N$ i dobivamo Splay $I$—$L$.

    ![step 2 auxtree](images/lct-access-5.svg)

-   Dalje, po istom postupku: budući da Father od $I$ pokazuje na $H$, rotiramo $H$ do korijena njegova Splay Treea, a zatim rs od $H$ postavimo na $I$.

-   Stablo tada izgleda ovako.

    ![step 3 auxtree](images/lct-access-6.svg)

-   Analogno izvedemo `Splay(A)` i desno dijete od $A$ postavimo na $H$.

-   Tako dobivamo ovakav AuxTree i vidimo da je cijeli put $A$—$N$ sada u istom Splayu.

    ![step final auxtree](images/lct-access-7.svg)

```cpp
// pogledajmo kod još jednom
int Access(int x) {
  int p;
  for (p = 0; x; p = x, x = f[x]) {
    Splay(x), ch[x][1] = p, PushUp(x);
  }
  return p;
}
```

Vidimo da je `Access()` zapravo vrlo jednostavan; sastoji se od sljedeća četiri koraka:

1.  Rotiraj trenutni čvor do korijena.
2.  Zamijeni mu dijete prethodnim čvorom.
3.  Ažuriraj informacije trenutnog čvora.
4.  Prijeđi na roditelja trenutnog čvora i nastavi.

Ovdje dani Access ima i povratnu vrijednost. Ona odgovara indeksu roditeljskog čvora virtualnog brida pri posljednjoj zamjeni virtualnog i punog lanca. Ta vrijednost ima dva značenja:

-   Pri dvama uzastopnim pozivima Accessa povratna vrijednost drugog poziva jednaka je LCA-u tih dvaju čvorova.
-   Predstavlja korijen Splay Treea u kojem se nalazi lanac od $x$ do korijena. Taj je čvor sigurno već rotiran do korijena i roditelj mu je sigurno prazan.

### `Update()`

```cpp
// dovoljno je pushDown razinu po razinu odozgo prema dolje
void Update(int p) {
  if (!isRoot(p)) Update(f[p]);
  pushDown(p);
}
```

### `makeRoot()`

-   `Make_Root()` nije ništa manje važan od `Access()`. Kad trebamo održavati informacije o putu, nužno se pojavljuju putovi čija dubina nije strogo rastuća, a po svojstvima AuxTreea takav se put ne može nalaziti u jednom Splayu.
-   Tada nam treba `Make_Root()`.
-   `Make_Root()` čini zadani čvor korijenom izvornog stabla; razmotrimo kako to izvesti.
-   Neka je povratna vrijednost `Access(x)` jednaka $y$; tada put od $x$ do trenutnog korijena čini točno jedan Splay, a korijen tog Splaya je $y$.
-   Prikažimo stablo usmjerenim grafom, gdje svakom bridu dajemo smjer od djeteta prema roditelju. Lako se vidi da promjena korijena odgovara obrtanju smjera svih bridova na putu od $x$ do korijena (dobro promislite).
-   Stoga je dovoljno obrnuti put od $x$ do trenutnog korijena.
-   Budući da je $y$ korijen Splaya koji predstavlja put od $x$ do trenutnog korijena, dovoljno je obrnuti interval u Splay Treeu s korijenom $y$.

```cpp
void makeRoot(int p) {
  p = Access(p);
  swap(ch[p][0], ch[p][1]);
  tag[p] ^= 1;
}
```

### `Link()`

-   Link dvaju čvorova zapravo je jednostavan: najprije `Make_Root(x)`, zatim roditelja od $x$ usmjerimo na $y$. Jasno, ta se operacija ne smije izvesti unutar istog stabla, pa to najprije provjerite.

```cpp
void Link(int x, int p) {
  makeRoot(x);
  splay(x);
  f[x] = p;
}
```

### `Split()`

-   Značenje operacije `Split` jednostavno je: izdvojiti Splay koji održava put od $x$ do $y$.
-   Najprije `MakeRoot(x)`, zatim `Access(y)`. Ako želimo da $y$ bude korijen, još i `Splay(y)`.
-   Ta tri koraka Splita izravno izdvajaju traženi put u podstablo čvora $y$, nad kojim onda možemo raditi druge operacije.

### `Cut()`

-   `Cut` ima dva slučaja: kad je zajamčeno da je operacija valjana i kad nije.
-   Ako je valjanost zajamčena, izravno `Split(x, y)`; tada je $y$ korijen, a $x$ je sigurno njegovo dijete, pa vezu prekinemo u oba smjera. Ovako:

```cpp
void Cut(int x, int p) { makeRoot(x), Access(p), Splay(p), ls = f[x] = 0; }
```

Ako valjanost nije zajamčena, moramo provjeriti postoji li brid; ovdje bismo mogli bridove spremiti u `map`, ali postoji i metoda koja koristi svojstva strukture:

Da bismo obrisali brid, moraju vrijediti sljedeća tri uvjeta:

1.  $x,y$ su povezani.
2.  Na putu između $x,y$ nema drugih lanaca.
3.  $x$ nema desno dijete.

Ukratko, gornje tri rečenice znače jedno: između $x,y$ postoji brid.

Konkretnu implementaciju ostavljamo za razmišljanje. Za provjeru povezanosti treba kasnije opisani `Find`; za preostala dva uvjeta malo promislite o strukturi i bit će jasno kako ih provjeriti.

### `Find()`

-   `Find()` traži korijen **izvornog stabla** u kojem je $x$; nemojte pobrkati korijen izvornog i pomoćnog stabla. Nakon `Access(p)` izvedemo `Splay(p)`. Tada je korijen čvor najmanje dubine u stablu: idemo stalno u lijevo dijete i usput izvodimo `PushDown`.
-   Idemo dok više nema ls; vrlo jednostavno.
-   Napomena: nakon svakog upita pronađeni čvor s odgovorom treba izvesti `Splay` radi očuvanja složenosti.

```cpp
int Find(int p) {
  Access(p);
  Splay(p);
  pushDown(p);
  while (ls) p = ls, pushDown(p);
  Splay(p);
  return p;
}
```

### Napomene

-   Prije svake operacije dobro razmislite treba li `PushUp` ili `PushDown`; LCT je iznimno fleksibilan, pa jedan izostavljeni `Pushdown` ili `Pushup` može promjenu primijeniti na krivi čvor!
-   `Rotate` u LCT-u razlikuje se od onog u Splayu: `if (z)` mora stajati na početku.
-   `Splay` u LCT-u rotira do korijena; nema rotiranja do „djeteta nekog čvora”, jer to nije potrebno.

## Vremenska složenost

Većina operacija LCT-a temelji se na `Access`; vremenska složenost ostalih operacija je konstantna, pa je dovoljno analizirati složenost operacije `Access`.

Složenost `Access`-a potječe uglavnom od višestrukih splay operacija i od obilaska virtualnih bridova na putu; analizirajmo ta dva dijela zasebno.

1.  splay

    -   Definiramo $w(x) = \log size(x)$, gdje $size(x)$ označava ukupan broj virtualnih i punih bridova u podstablu s korijenom $x$.

    -   Definiramo funkciju potencijala $\Phi = \sum_{x \in T} w(x)$, gdje je $T$ skup svih čvorova.

    Iz analize [vremenske složenosti Splaya](./splay.md#vremenska-složenost) lako slijedi da je amortizirana složenost splay operacije $O(\log n)$.

2.  obilazak virtualnih bridova

    Prema [heavy-light dekompoziciji](../graph/hld.md#heavy-light-dekompozicija) definiramo dvije vrste virtualnih bridova:

    -   **teški virtualni brid**: virtualni brid od čvora $v$ do njegova roditelja za koji je $size(v) > \frac{1}{2} size(parent(v))$;

    -   **laki virtualni brid**: virtualni brid od čvora $v$ do njegova roditelja za koji je $size(v) \leq \frac{1}{2} size(parent(v))$.

    Za virtualne bridove koristimo analizu potencijala: funkcija potencijala $\Phi$ je broj svih teških virtualnih bridova, a amortizirani trošak $c_i = t_i + \Delta \Phi_i$, gdje je $t_i$ stvarni trošak operacije, a $\Delta \Phi_i$ promjena potencijala.

    -   Nakon prelaska teškog virtualnog brida on postaje puni brid, čime se potencijal smanjuje za $1$, jer se struktura stabla poboljšava jačanjem važnih veza. Stvarni trošak te operacije je $O(1)$ i poništen je smanjenjem potencijala, pa ne povećava amortizirani trošak; sav amortizirani trošak koncentriran je na obradu lakih virtualnih bridova.

    -   Svaki `Access` prelazi najviše $O(\log n)$ lakih virtualnih bridova, pa troši najviše $O(\log n)$ stvarnog rada i stvara $O(\log n)$ teških virtualnih bridova, tj. potencijal raste uz cijenu $O(\log n)$.

    Konačna amortizirana složenost obilaska virtualnih bridova zbroj je stvarnog troška i promjene potencijala, dakle $O(\log n)$.

Zaključno, vremenska složenost operacije `Access` u LCT-u zbroj je složenosti splaya i obilaska virtualnih bridova, pa je konačna amortizirana složenost $O(\log n)$; drugim riječima, LCT s n čvorova izvodi m operacija `Access` u vremenu $O(n \log n + m \log n)$, pa je i amortizirana složenost operacija `Cut`, `Link`, `Findroot` itd., koje se temelje na `Access`, jednaka $O(\log n)$.

## Zadaci

-   [BZOJ 3282 Tree](https://hydro.ac/p/bzoj-P3282)
-   [HNOI2010 弹飞绵羊](https://www.luogu.com.cn/problem/P3203)

## Održavanje informacija o putu

Operacijom `Split(x,y)` LCT izdvaja put od čvora $x$ do čvora $y$ u Splay s korijenom $y$, pa se promjene i upiti nad informacijama o putu svode na operacije nad balansiranim stablom; to LCT-u daje prednost pri održavanju informacija o putu. Osim toga, binarno pretraživanje po putu pomoću LCT-a ima za faktor $O(\log n)$ manju složenost nego s heavy-light dekompozicijom.

???+ note "Primjer [国家集训队 Tree II](https://www.luogu.com.cn/problem/P1501)"
    Zadano je stablo s $n$ čvorova; početna težina svakog čvora je $1$. Slijedi $q$ operacija, svaka jednog od četiri tipa:
    
    1.  `- u1 v1 u2 v2`: obriši brid između čvorova $u_1,v_1$ i spoji čvorove $u_2,v_2$; jamči se da je operacija valjana i da je rezultat i dalje stablo.
    2.  `+ u v c`: težine svih čvorova na putu između $u,v$ povećaj za $c$.
    3.  `* u v c`: težine svih čvorova na putu između $u,v$ pomnoži s $c$.
    4.  `/ u v`: ispiši zbroj težina čvorova na putu između $u,v$ modulo $51061$.
    
        $1\le n,q\le 10^5,0\le c\le 10^4$
    
        Operacija `-` izvodi se izravno kao `Cut(u1,v1),Link(u2,v2)`.

Pri promjeni na putu između čvorova $u,v$ najprije izvedemo `Split(u,v)`.

Zadatak traži dodavanje na podstablo, množenje podstabla i zbroj podstabla u pomoćnom stablu, pa uz oznaku obrtanja podstabla koju LCT ionako održava trebamo održavati i oznaku dodavanja te oznaku množenja na podstablu. Oznake obrađujemo jednako kao u Splayu.

Pri postavljanju i spuštanju oznake dodavanja promjena zbroja podstabla ovisi o broju čvorova u podstablu, pa moramo održavati i veličinu podstabla `siz`.

Pri spuštanju oznaka pazimo na redoslijed: najprije spuštamo oznaku množenja, zatim oznaku dodavanja. Oznaka obrtanja podstabla i oznake dodavanja/množenja nisu u sukobu.

??? note "Primjer koda"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <cstring>
    using namespace std;
    constexpr long long MAXN = 100010;
    constexpr long long mod = 51061;
    long long n, q, u, v, c;
    char op;
    
    struct Splay {
      long long ch[MAXN][2], fa[MAXN], siz[MAXN], val[MAXN], sum[MAXN], rev[MAXN],
          add[MAXN], mul[MAXN];
    
      void clear(long long x) {
        ch[x][0] = ch[x][1] = fa[x] = siz[x] = val[x] = sum[x] = rev[x] = add[x] =
            0;
        mul[x] = 1;
      }
    
      long long getch(long long x) { return (ch[fa[x]][1] == x); }
    
      long long isroot(long long x) {
        clear(0);
        return ch[fa[x]][0] != x && ch[fa[x]][1] != x;
      }
    
      void maintain(long long x) {
        clear(0);
        siz[x] = (siz[ch[x][0]] + 1 + siz[ch[x][1]]) % mod;
        sum[x] = (sum[ch[x][0]] + val[x] + sum[ch[x][1]]) % mod;
      }
    
      void pushdown(long long x) {
        clear(0);
        if (mul[x] != 1) {
          if (ch[x][0])
            mul[ch[x][0]] = (mul[x] * mul[ch[x][0]]) % mod,
            val[ch[x][0]] = (val[ch[x][0]] * mul[x]) % mod,
            sum[ch[x][0]] = (sum[ch[x][0]] * mul[x]) % mod,
            add[ch[x][0]] = (add[ch[x][0]] * mul[x]) % mod;
          if (ch[x][1])
            mul[ch[x][1]] = (mul[x] * mul[ch[x][1]]) % mod,
            val[ch[x][1]] = (val[ch[x][1]] * mul[x]) % mod,
            sum[ch[x][1]] = (sum[ch[x][1]] * mul[x]) % mod,
            add[ch[x][1]] = (add[ch[x][1]] * mul[x]) % mod;
          mul[x] = 1;
        }
        if (add[x]) {
          if (ch[x][0])
            add[ch[x][0]] = (add[ch[x][0]] + add[x]) % mod,
            val[ch[x][0]] = (val[ch[x][0]] + add[x]) % mod,
            sum[ch[x][0]] = (sum[ch[x][0]] + add[x] * siz[ch[x][0]] % mod) % mod;
          if (ch[x][1])
            add[ch[x][1]] = (add[ch[x][1]] + add[x]) % mod,
            val[ch[x][1]] = (val[ch[x][1]] + add[x]) % mod,
            sum[ch[x][1]] = (sum[ch[x][1]] + add[x] * siz[ch[x][1]] % mod) % mod;
          add[x] = 0;
        }
        if (rev[x]) {
          if (ch[x][0]) rev[ch[x][0]] ^= 1, swap(ch[ch[x][0]][0], ch[ch[x][0]][1]);
          if (ch[x][1]) rev[ch[x][1]] ^= 1, swap(ch[ch[x][1]][0], ch[ch[x][1]][1]);
          rev[x] = 0;
        }
      }
    
      void update(long long x) {
        if (!isroot(x)) update(fa[x]);
        pushdown(x);
      }
    
      void print(long long x) {
        if (!x) return;
        pushdown(x);
        print(ch[x][0]);
        printf("%lld ", x);
        print(ch[x][1]);
      }
    
      void rotate(long long x) {
        long long y = fa[x], z = fa[y], chx = getch(x), chy = getch(y);
        fa[x] = z;
        if (!isroot(y)) ch[z][chy] = x;
        ch[y][chx] = ch[x][chx ^ 1];
        fa[ch[x][chx ^ 1]] = y;
        ch[x][chx ^ 1] = y;
        fa[y] = x;
        maintain(y);
        maintain(x);
        maintain(z);
      }
    
      void splay(long long x) {
        update(x);
        for (long long f = fa[x]; f = fa[x], !isroot(x); rotate(x))
          if (!isroot(f)) rotate(getch(x) == getch(f) ? f : x);
      }
    
      void access(long long x) {
        for (long long f = 0; x; f = x, x = fa[x])
          splay(x), ch[x][1] = f, maintain(x);
      }
    
      void makeroot(long long x) {
        access(x);
        splay(x);
        swap(ch[x][0], ch[x][1]);
        rev[x] ^= 1;
      }
    
      long long find(long long x) {
        access(x);
        splay(x);
        while (ch[x][0]) x = ch[x][0];
        splay(x);
        return x;
      }
    } st;
    
    main() {
      scanf("%lld%lld", &n, &q);
      for (long long i = 1; i <= n; i++) st.val[i] = 1, st.maintain(i);
      for (long long i = 1; i < n; i++) {
        scanf("%lld%lld", &u, &v);
        if (st.find(u) != st.find(v)) st.makeroot(u), st.fa[u] = v;
      }
      while (q--) {
        scanf(" %c%lld%lld", &op, &u, &v);
        if (op == '+') {
          scanf("%lld", &c);
          st.makeroot(u), st.access(v), st.splay(v);
          st.val[v] = (st.val[v] + c) % mod;
          st.sum[v] = (st.sum[v] + st.siz[v] * c % mod) % mod;
          st.add[v] = (st.add[v] + c) % mod;
        }
        if (op == '-') {
          st.makeroot(u);
          st.access(v);
          st.splay(v);
          if (st.ch[v][0] == u && !st.ch[u][1]) st.ch[v][0] = st.fa[u] = 0;
          scanf("%lld%lld", &u, &v);
          if (st.find(u) != st.find(v)) st.makeroot(u), st.fa[u] = v;
        }
        if (op == '*') {
          scanf("%lld", &c);
          st.makeroot(u), st.access(v), st.splay(v);
          st.val[v] = st.val[v] * c % mod;
          st.sum[v] = st.sum[v] * c % mod;
          st.mul[v] = st.mul[v] * c % mod;
        }
        if (op == '/')
          st.makeroot(u), st.access(v), st.splay(v), printf("%lld\n", st.sum[v]);
      }
      return 0;
    }
    ```

### Zadaci

-   [Luogu P3690【模板】Link Cut Tree（动态树）](https://www.luogu.com.cn/problem/P3690)
-   [SDOI2011 染色](https://www.luogu.com.cn/problem/P2486)
-   [SHOI2014 三叉神经树](https://loj.ac/problem/2187)

## Održavanje povezanosti

### Provjera povezanosti

Funkcijom `Find()` LCT-a možemo provjeriti jesu li dva čvora dinamičke šume povezana. Ako je `Find(x)==Find(y)`, čvorovi $x,y$ nalaze se u istom stablu, tj. povezani su.

???+ note "Primjer [SDOI2008 洞穴勘测](https://www.luogu.com.cn/problem/P2147)"
    Na početku imamo $n$ izoliranih čvorova i $m$ operacija. Svaka je operacija jedna od sljedećih:
    
    1.  `Connect u v`: spoji čvorove $u,v$ bridom.
    2.  `Destroy u v`: obriši brid između čvorova $u,v$; jamči se da takav brid postoji.
    3.  `Query u v`: jesu li čvorovi $u,v$ povezani?
    
    Jamči se da je graf u svakom trenutku šuma.
    
    $n\le 10^4, m\le 2\times 10^5$

??? note "Primjer koda"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <cstring>
    using namespace std;
    constexpr int MAXN = 10010;
    
    struct Splay {
      int ch[MAXN][2], fa[MAXN], tag[MAXN];
    
      void clear(int x) { ch[x][0] = ch[x][1] = fa[x] = tag[x] = 0; }
    
      int getch(int x) { return ch[fa[x]][1] == x; }
    
      int isroot(int x) { return ch[fa[x]][0] != x && ch[fa[x]][1] != x; }
    
      void pushdown(int x) {
        if (tag[x]) {
          if (ch[x][0]) swap(ch[ch[x][0]][0], ch[ch[x][0]][1]), tag[ch[x][0]] ^= 1;
          if (ch[x][1]) swap(ch[ch[x][1]][0], ch[ch[x][1]][1]), tag[ch[x][1]] ^= 1;
          tag[x] = 0;
        }
      }
    
      void update(int x) {
        if (!isroot(x)) update(fa[x]);
        pushdown(x);
      }
    
      void rotate(int x) {
        int y = fa[x], z = fa[y], chx = getch(x), chy = getch(y);
        fa[x] = z;
        if (!isroot(y)) ch[z][chy] = x;
        ch[y][chx] = ch[x][chx ^ 1];
        fa[ch[x][chx ^ 1]] = y;
        ch[x][chx ^ 1] = y;
        fa[y] = x;
      }
    
      void splay(int x) {
        update(x);
        for (int f = fa[x]; f = fa[x], !isroot(x); rotate(x))
          if (!isroot(f)) rotate(getch(x) == getch(f) ? f : x);
      }
    
      void access(int x) {
        for (int f = 0; x; f = x, x = fa[x]) splay(x), ch[x][1] = f;
      }
    
      void makeroot(int x) {
        access(x);
        splay(x);
        swap(ch[x][0], ch[x][1]);
        tag[x] ^= 1;
      }
    
      int find(int x) {
        access(x);
        splay(x);
        while (ch[x][0]) x = ch[x][0];
        splay(x);
        return x;
      }
    } st;
    
    int n, q, x, y;
    char op[MAXN];
    
    int main() {
      scanf("%d%d", &n, &q);
      while (q--) {
        scanf("%s%d%d", op, &x, &y);
        if (op[0] == 'Q') {
          if (st.find(x) == st.find(y))
            printf("Yes\n");
          else
            printf("No\n");
        }
        if (op[0] == 'C')
          if (st.find(x) != st.find(y)) st.makeroot(x), st.fa[x] = y;
        if (op[0] == 'D') {
          st.makeroot(x);
          st.access(y);
          st.splay(y);
          if (st.ch[y][0] == x && !st.ch[x][1]) st.ch[y][0] = st.fa[x] = 0;
        }
      }
      return 0;
    }
    ```

### Održavanje bridno dvostruko povezanih komponenti

Ako treba bridno dvostruko povezane komponente sažeti u čvorove: pri svakom dodavanju brida, ako su dva čvora stabla koje spaja već povezana, svi čvorovi na tom putu sažimaju se u jedan čvor.

???+ note "Primjer [AHOI2005 航线规划](https://www.luogu.com.cn/problem/P2542)"
    Zadano je $n$ čvorova, na početku $m$ neusmjerenih bridova i $q$ operacija. Svaka je operacija jedna od sljedećih:
    
    1.  `0 u v`: obriši brid između $u,v$; jamči se da takav brid tada postoji.
    2.  `1 u v`: upit koliko bridova u tom trenutku moraju sadržavati svi mogući putovi između čvorova $u,v$.
    
    Jamči se da je graf u svakom trenutku povezan.
    
    $1<n<3\times 10^4,1<m<10^5,0\le q\le 4\times 10^4$

Može se primijetiti da je broj bridova koje moraju sadržavati svi mogući putovi između $u,v$ jednak broju čvorova na putu između čvora koji sadrži $u$ i čvora koji sadrži $v$ nakon sažimanja svih bridno dvostruko povezanih komponenti, umanjenom za $1$.

Budući da je brisanje bridova iz zadatka teško izvesti, operacije obrađujemo offline u obrnutom redoslijedu, pa brisanje bridova postaje dodavanje bridova.

Pri dodavanju brida, ako dva čvora prije toga nisu bila povezana, spojimo ih u LCT-u; inače izdvojimo put između tih dvaju čvorova u LCT-u prije dodavanja brida, obiđemo to podstablo pomoćnog stabla, što odgovara obilasku tog puta, i spojimo te čvorove, a informacije o spajanju održavamo union-findom.

Predstavnik iz union-finda nakon spajanja zamjenjuje dotadašnji put u stablu. Pazite da pri svakoj sljedećoj operaciji treba najprije pronaći predstavnika čvora u union-findu i raditi s njim.

??? note "Primjer koda"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <cstring>
    #include <map>
    using namespace std;
    constexpr int MAXN = 200010;
    int f[MAXN];
    
    int findp(int x) { return f[x] ? f[x] = findp(f[x]) : x; }
    
    void merge(int x, int y) {
      x = findp(x);
      y = findp(y);
      if (x != y) f[x] = y;
    }
    
    struct Splay {
      int ch[MAXN][2], fa[MAXN], tag[MAXN], siz[MAXN];
    
      void clear(int x) { ch[x][0] = ch[x][1] = fa[x] = tag[x] = siz[x] = 0; }
    
      int getch(int x) { return ch[findp(fa[x])][1] == x; }
    
      int isroot(int x) {
        return ch[findp(fa[x])][0] != x && ch[findp(fa[x])][1] != x;
      }
    
      void maintain(int x) {
        clear(0);
        if (x) siz[x] = siz[ch[x][0]] + 1 + siz[ch[x][1]];
      }
    
      void pushdown(int x) {
        if (tag[x]) {
          if (ch[x][0]) tag[ch[x][0]] ^= 1, swap(ch[ch[x][0]][0], ch[ch[x][0]][1]);
          if (ch[x][1]) tag[ch[x][1]] ^= 1, swap(ch[ch[x][1]][0], ch[ch[x][1]][1]);
          tag[x] = 0;
        }
      }
    
      void print(int x) {
        if (!x) return;
        pushdown(x);
        print(ch[x][0]);
        printf("%d ", x);
        print(ch[x][1]);
      }
    
      void update(int x) {
        if (!isroot(x)) update(findp(fa[x]));
        pushdown(x);
      }
    
      void rotate(int x) {
        x = findp(x);
        int y = findp(fa[x]), z = findp(fa[y]), chx = getch(x), chy = getch(y);
        fa[x] = z;
        if (!isroot(y)) ch[z][chy] = x;
        ch[y][chx] = ch[x][chx ^ 1];
        fa[ch[x][chx ^ 1]] = y;
        ch[x][chx ^ 1] = y;
        fa[y] = x;
        maintain(y);
        maintain(x);
        if (z) maintain(z);
      }
    
      void splay(int x) {
        x = findp(x);
        update(x);
        for (int f = findp(fa[x]); f = findp(fa[x]), !isroot(x); rotate(x))
          if (!isroot(f)) rotate(getch(x) == getch(f) ? f : x);
      }
    
      void access(int x) {
        for (int f = 0; x; f = x, x = findp(fa[x]))
          splay(x), ch[x][1] = f, maintain(x);
      }
    
      void makeroot(int x) {
        x = findp(x);
        access(x);
        splay(x);
        tag[x] ^= 1;
        swap(ch[x][0], ch[x][1]);
      }
    
      int find(int x) {
        x = findp(x);
        access(x);
        splay(x);
        while (ch[x][0]) x = ch[x][0];
        splay(x);
        return x;
      }
    
      void dfs(int x) {
        pushdown(x);
        if (ch[x][0]) dfs(ch[x][0]), merge(ch[x][0], x);
        if (ch[x][1]) dfs(ch[x][1]), merge(ch[x][1], x);
      }
    } st;
    
    int n, m, q, x, y, cur, ans[MAXN];
    
    struct oper {
      int op, a, b;
    } s[MAXN];
    
    map<pair<int, int>, int> mp;
    
    int main() {
      scanf("%d%d", &n, &m);
      for (int i = 1; i <= n; i++) st.maintain(i);
      for (int i = 1; i <= m; i++)
        scanf("%d%d", &x, &y), mp[{x, y}] = mp[{y, x}] = 1;
      while (scanf("%d", &s[++q].op)) {
        if (s[q].op == -1) {
          q--;
          break;
        }
        scanf("%d%d", &s[q].a, &s[q].b);
        if (!s[q].op) mp[{s[q].a, s[q].b}] = mp[{s[q].b, s[q].a}] = 0;
      }
      reverse(s + 1, s + q + 1);
      for (map<pair<int, int>, int>::iterator it = mp.begin(); it != mp.end(); it++)
        if (it->second) {
          mp[{it->first.second, it->first.first}] = 0;
          x = findp(it->first.first);
          y = findp(it->first.second);
          if (st.find(x) != st.find(y))
            st.makeroot(x), st.fa[x] = y;
          else {
            if (x == y) continue;
            st.makeroot(x);
            st.access(y);
            st.splay(y);
            st.dfs(y);
            int t = findp(y);
            st.fa[t] = findp(st.fa[y]);
            st.ch[t][0] = st.ch[t][1] = 0;
            st.maintain(t);
          }
        }
      for (int i = 1; i <= q; i++) {
        if (s[i].op == 0) {
          x = findp(s[i].a);
          y = findp(s[i].b);
          st.makeroot(x);
          st.access(y);
          st.splay(y);
          st.dfs(y);
          int t = findp(y);
          st.fa[t] = st.fa[y];
          st.ch[t][0] = st.ch[t][1] = 0;
          st.maintain(t);
        }
        if (s[i].op == 1) {
          x = findp(s[i].a);
          y = findp(s[i].b);
          st.makeroot(x);
          st.access(y);
          st.splay(y);
          ans[++cur] = st.siz[y] - 1;
        }
      }
      for (int i = cur; i >= 1; i--) printf("%d\n", ans[i]);
      return 0;
    }
    ```

### Zadaci

-   [Luogu P3950 部落冲突](https://www.luogu.com.cn/problem/P3950)
-   [BZOJ 4998 星球联盟](https://hydro.ac/p/bzoj-P4998)
-   [BZOJ 2959 长跑](https://hydro.ac/p/bzoj-P2959)

## Održavanje težina bridova

LCT ne može izravno raditi s težinama bridova; tada za svaki brid stvorimo odgovarajući čvor, što olakšava upite o bridovima na putu. Tim se trikom može dinamički održavati razapinjuće stablo.

???+ note "Primjer [Luogu P4234 最小差值生成树](https://www.luogu.com.cn/problem/P4234)"
    Zadan je težinski neusmjereni graf s $n$ čvorova i $m$ bridova. Pronađite razapinjuće stablo s najmanjom razlikom između najveće i najmanje težine brida i ispišite tu razliku.
    
    Jamči se da postoji barem jedno razapinjuće stablo.
    
    $1\le n\le 5\times 10^4,1\le m\le 2\times 10^5,1\le w_i\le 10^4$

Sortiramo bridove po težini uzlazno i iteriramo po krajnjem desnom odabranom bridu; za optimalno rješenje treba težina najlakšeg brida biti što veća.

Bridove dodajemo redom; ako su dva čvora koja brid spaja već povezana, obrišemo brid najmanje težine na putu između njih. Ako je cijeli graf već povezan u stablo, odgovor ažuriramo razlikom trenutne težine i najmanje težine. Najmanju težinu možemo ažurirati metodom dvaju pokazivača.

U LCT-u ne postoji fiksan odnos roditelj–dijete, pa težine bridova ne možemo spremiti u težine čvorova.

Informacije o bridovima na putu možemo pamtiti **razdvajanjem bridova**: za svaki brid stvorimo odgovarajući čvor i povežemo ga s oba krajnja čvora; dotadašnje spajanje i brisanje brida postaju po dvije operacije.

??? note "Primjer koda"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <cstring>
    #include <set>
    using namespace std;
    constexpr int MAXN = 5000010;
    
    struct Splay {
      int ch[MAXN][2], fa[MAXN], tag[MAXN], val[MAXN], minn[MAXN];
    
      void clear(int x) {
        ch[x][0] = ch[x][1] = fa[x] = tag[x] = val[x] = minn[x] = 0;
      }
    
      int getch(int x) { return ch[fa[x]][1] == x; }
    
      int isroot(int x) { return ch[fa[x]][0] != x && ch[fa[x]][1] != x; }
    
      void maintain(int x) {
        if (!x) return;
        minn[x] = x;
        if (ch[x][0]) {
          if (val[minn[ch[x][0]]] < val[minn[x]]) minn[x] = minn[ch[x][0]];
        }
        if (ch[x][1]) {
          if (val[minn[ch[x][1]]] < val[minn[x]]) minn[x] = minn[ch[x][1]];
        }
      }
    
      void pushdown(int x) {
        if (tag[x]) {
          if (ch[x][0]) tag[ch[x][0]] ^= 1, swap(ch[ch[x][0]][0], ch[ch[x][0]][1]);
          if (ch[x][1]) tag[ch[x][1]] ^= 1, swap(ch[ch[x][1]][0], ch[ch[x][1]][1]);
          tag[x] = 0;
        }
      }
    
      void update(int x) {
        if (!isroot(x)) update(fa[x]);
        pushdown(x);
      }
    
      void print(int x) {
        if (!x) return;
        pushdown(x);
        print(ch[x][0]);
        printf("%d ", x);
        print(ch[x][1]);
      }
    
      void rotate(int x) {
        int y = fa[x], z = fa[y], chx = getch(x), chy = getch(y);
        fa[x] = z;
        if (!isroot(y)) ch[z][chy] = x;
        ch[y][chx] = ch[x][chx ^ 1];
        fa[ch[x][chx ^ 1]] = y;
        ch[x][chx ^ 1] = y;
        fa[y] = x;
        maintain(y);
        maintain(x);
        if (z) maintain(z);
      }
    
      void splay(int x) {
        update(x);
        for (int f = fa[x]; f = fa[x], !isroot(x); rotate(x))
          if (!isroot(f)) rotate(getch(x) == getch(f) ? f : x);
      }
    
      void access(int x) {
        for (int f = 0; x; f = x, x = fa[x]) splay(x), ch[x][1] = f, maintain(x);
      }
    
      void makeroot(int x) {
        access(x);
        splay(x);
        tag[x] ^= 1;
        swap(ch[x][0], ch[x][1]);
      }
    
      int find(int x) {
        access(x);
        splay(x);
        while (ch[x][0]) x = ch[x][0];
        splay(x);
        return x;
      }
    
      void link(int x, int y) {
        makeroot(x);
        fa[x] = y;
      }
    
      void cut(int x, int y) {
        makeroot(x);
        access(y);
        splay(y);
        ch[y][0] = fa[x] = 0;
        maintain(y);
      }
    } st;
    
    constexpr int inf = 2e9 + 1;
    int n, m, ans, nww, x, y;
    
    struct Edge {
      int u, v, w;
    
      bool operator<(Edge x) const { return w < x.w; };
    } s[MAXN];
    
    multiset<int> mp;
    
    int main() {
      scanf("%d%d", &n, &m);
      for (int i = 1; i <= n; i++) st.val[i] = inf, st.maintain(i);
      for (int i = 1; i <= m; i++) scanf("%d%d%d", &s[i].u, &s[i].v, &s[i].w);
      sort(s + 1, s + m + 1);
      for (int i = 1; i <= m; i++) st.val[n + i] = s[i].w, st.maintain(n + i);
      for (int i = 1; i <= m; i++) {
        x = s[i].u;
        y = s[i].v;
        if (x == y) continue;
        if (st.find(x) != st.find(y)) {
          nww++;
          st.link(x, n + i);
          st.link(n + i, y);
          mp.insert(s[i].w);
          if (nww == n - 1) ans = s[i].w - (*(mp.begin()++));
        } else {
          st.makeroot(x);
          st.access(y);
          st.splay(y);
          int t = st.minn[y] - n;
          st.cut(s[t].u, t + n);
          st.cut(t + n, s[t].v);
          mp.erase(mp.find(s[t].w));
          st.link(x, n + i);
          st.link(n + i, y);
          mp.insert(s[i].w);
          if (nww == n - 1) ans = min(ans, s[i].w - (*(mp.begin()++)));
        }
      }
      printf("%d\n", ans);
      return 0;
    }
    ```

### Zadaci

-   [WC2006 水管局长](https://www.luogu.com.cn/problem/P4172)
-   [BJWC2010 严格次小生成树](https://www.luogu.com.cn/problem/P4180)
-   [NOI2014 魔法森林](https://uoj.ac/problem/3)

## Održavanje informacija o podstablu

LCT nije pogodan za održavanje informacija o podstablu. Zbrajanjem informacija svih virtualnih podstabala nekog čvora može se dobiti informacija o cijelom stablu.

???+ note "Primjer [BJOI2014 大融合](https://loj.ac/problem/2230)"
    Zadano je $n$ čvorova i $q$ operacija, svaka sljedećeg oblika:
    
    1.  `A x y` spoji čvorove $x$ i $y$ bridom.
    2.  `Q x y` za zadani postojeći brid $(x,y)$ odredi koliko jednostavnih putova sadrži brid $(x,y)$.
    
    Jamči se da je graf u svakom trenutku šuma.
    
    $1\le n,q,x,y\le 10^5$

Preformulirajmo upit `Q`: odgovor je umnožak broja čvorova na strani $x$ i broja čvorova na strani $y$ brida $(x,y)$, tj. brojeva čvorova stabala koja nakon rezanja brida $(x,y)$ sadrže $x$ odnosno $y$. Da poništimo učinak rezanja, nakon upita ponovno spojimo brid $(x,y)$.

Zadatak ima i spajanje i brisanje bridova te jamči da je graf u svakom trenutku šuma, pa se nameće LCT. No ovdje LCT održava veličinu podstabla, a ne, kako smo navikli, informacije o lancu, a LCT je građen tako da **dijete poznaje roditelja, ali roditelj ne poznaje dijete**, što otežava izravno zbrajanje po podstablu. Što učiniti?

Rješenje je zbrojiti doprinose podstabala koja predstavljaju sva virtualna djeca čvora $x$ (tj. čvorove kojima je roditelj $x$, ali ih lijevo i desno dijete od $x$ u Splayu ne uključuju).

Definirajmo $siz2[x]$ kao broj čvorova u podstablima koja predstavljaju sva virtualna djeca čvora $x$, a $siz[x]$ kao broj čvorova u podstablu čvora $x$.

Za razliku od dosadašnjeg načina održavanja broja čvorova podstabla u Splayu, pri računanju broja čvorova u podstablu čvora $x$ dodajemo i $siz2[x]$, tj.

```cpp
void maintain(int x) {
  clear(0);
  if (x) siz[x] = siz[ch[x][0]] + 1 + siz[ch[x][1]] + siz2[x];
}
```

Osim toga, kad **mijenjamo oblik Splaya** (tj. mijenjamo lijevo ili desno dijete nekog čvora u Splayu), moramo odmah ažurirati vrijednost $siz2[x]$.

U operacijama `Rotate(),Splay()` mijenjamo samo relativni položaj čvorova unutar Splaya, a ne mijenjamo je li ijedan brid virtualan ili pun, pa $siz2[x]$ ne mijenjamo.

U operaciji `access` nakon svakog splaya mijenja se desno dijete upravo splayanog čvora, tj. mijenja se status (virtualan/pun) brida prema dotadašnjem desnom djetetu i brida prema novom desnom djetetu; moramo dodati doprinos podstabla koje je brid upravo postao virtualan i oduzeti doprinos podstabla čiji je brid upravo postao pun. Kod je sljedeći:

```cpp
void access(int x) {
  for (int f = 0; x; f = x, x = fa[x])
    splay(x), siz2[x] += siz[ch[x][1]] - siz[f], ch[x][1] = f, maintain(x);
}
```

U operacijama `MakeRoot(),Find()` samo pozivamo prethodne funkcije ili se krećemo po Splayu, pa ništa ne treba mijenjati.

Pri spajanju dvaju čvorova mijenjamo roditelja jednog čvora. Vrijednosti $siz2$ roditeljskog čvora moramo dodati doprinos veličine podstabla novog djeteta.

```cpp
st.makeroot(x);
st.makeroot(y);
st.fa[x] = y;
st.siz2[y] += st.siz[x];
```

Pri rezanju brida samo brišemo jedan puni brid u Splayu; operacija `Maintain` održava te informacije, pa ništa ne treba mijenjati.

To su detalji izmjena u kodu; za kraj sažmimo zahtjeve i metodu održavanja informacija o podstablu LCT-om:

1.  Informacija koju održavamo mora biti **invertibilna (oduzimljiva)**, npr. broj čvorova podstabla ili zbroj težina podstabla; ne može se izravno održavati maksimum/minimum podstabla, jer pri pretvaranju virtualnog brida u puni treba izuzeti doprinos dotadašnjeg virtualnog brida.
2.  Uvodimo dodatnu vrijednost za doprinos virtualnih podstabala, pri zbrajanju je dodajemo odgovoru čvora, a pri promjeni statusa brida odmah je ažuriramo.
3.  Ostalo je kao kod običnog LCT-a; pri skupljanju informacija o podstablu čvor obvezno učinimo korijenom.
4.  Ako informacija nije invertibilna, npr. maksimum na intervalu, za svaki čvor možemo otvoriti balansirano stablo koje održava ekstreme u njegovim virtualnim podstablima.

??? note "Primjer koda"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <cstring>
    using namespace std;
    constexpr int MAXN = 100010;
    using ll = long long;
    
    struct Splay {
      int ch[MAXN][2], fa[MAXN], siz[MAXN], siz2[MAXN], tag[MAXN];
    
      void clear(int x) {
        ch[x][0] = ch[x][1] = fa[x] = siz[x] = siz2[x] = tag[x] = 0;
      }
    
      int getch(int x) { return ch[fa[x]][1] == x; }
    
      int isroot(int x) { return ch[fa[x]][0] != x && ch[fa[x]][1] != x; }
    
      void maintain(int x) {
        clear(0);
        if (x) siz[x] = siz[ch[x][0]] + 1 + siz[ch[x][1]] + siz2[x];
      }
    
      void pushdown(int x) {
        if (tag[x]) {
          if (ch[x][0]) swap(ch[ch[x][0]][0], ch[ch[x][0]][1]), tag[ch[x][0]] ^= 1;
          if (ch[x][1]) swap(ch[ch[x][1]][0], ch[ch[x][1]][1]), tag[ch[x][1]] ^= 1;
          tag[x] = 0;
        }
      }
    
      void update(int x) {
        if (!isroot(x)) update(fa[x]);
        pushdown(x);
      }
    
      void rotate(int x) {
        int y = fa[x], z = fa[y], chx = getch(x), chy = getch(y);
        fa[x] = z;
        if (!isroot(y)) ch[z][chy] = x;
        ch[y][chx] = ch[x][chx ^ 1];
        fa[ch[x][chx ^ 1]] = y;
        ch[x][chx ^ 1] = y;
        fa[y] = x;
        maintain(y);
        maintain(x);
        maintain(z);
      }
    
      void splay(int x) {
        update(x);
        for (int f = fa[x]; f = fa[x], !isroot(x); rotate(x))
          if (!isroot(f)) rotate(getch(x) == getch(f) ? f : x);
      }
    
      void access(int x) {
        for (int f = 0; x; f = x, x = fa[x])
          splay(x), siz2[x] += siz[ch[x][1]] - siz[f], ch[x][1] = f, maintain(x);
      }
    
      void makeroot(int x) {
        access(x);
        splay(x);
        swap(ch[x][0], ch[x][1]);
        tag[x] ^= 1;
      }
    
      int find(int x) {
        access(x);
        splay(x);
        while (ch[x][0]) x = ch[x][0];
        splay(x);
        return x;
      }
    } st;
    
    int n, q, x, y;
    char op;
    
    int main() {
      scanf("%d%d", &n, &q);
      while (q--) {
        scanf(" %c%d%d", &op, &x, &y);
        if (op == 'A') {
          st.makeroot(x);
          st.makeroot(y);
          st.fa[x] = y;
          st.siz2[y] += st.siz[x];
        }
        if (op == 'Q') {
          st.makeroot(x);
          st.access(y);
          st.splay(y);
          st.ch[y][0] = st.fa[x] = 0;
          st.maintain(x);
          st.makeroot(x);
          st.makeroot(y);
          printf("%lld\n", (ll)(st.siz[x] * st.siz[y]));
          st.makeroot(x);
          st.makeroot(y);
          st.fa[x] = y;
          st.siz2[y] += st.siz[x];
        }
      }
      return 0;
    }
    ```

### Zadaci

-   [Luogu P4299 首都](https://www.luogu.com.cn/problem/P4299)
-   [SPOJ QTREE5 - Query on a tree V](https://www.spoj.com/problems/QTREE5)
