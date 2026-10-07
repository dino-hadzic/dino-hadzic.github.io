---
title: Top Tree
---

author: F7487

## Self-Adjusting Top Tree

### Uvod

Self-Adjusting Top Tree struktura je podataka za održavanje potpuno dinamičke šume, zasnovana na teoriji Top Treea, koju su Tarjan i Werneck predstavili 2005. godine u radu Self-Adjusting Top Trees; skraćeno SATT.

Self-Adjusting Top Tree omogućuje nad bilo kojim stablom šume operacije izmjene/upita na lancu, izmjene/upita na podstablu te nelokalno pretraživanje.

Splay Tree temelj je SATT-a, ali Splay Tree koji SATT koristi u detaljima se razlikuje od običnog Splaya (uz neka proširenja).

### Uvodni problem

Održavajte šumu uz sljedeće operacije:

-   Brisanje i dodavanje brida; zajamčeno je da je prije i poslije operacije i dalje riječ o šumi.

-   Izmjena težina na nekom jednostavnom putu u nekom stablu.

-   Izmjena težina u podstablu s korijenom u nekom vrhu.

-   Upit za zbroj težina na nekom jednostavnom putu u nekom stablu.

-   Upit za zbroj težina u podstablu s korijenom u nekom vrhu.

### Kontrakcija stabla

Svako stablo možemo teorijom **kontrakcije stabla** sažeti u jedan brid.

Konkretno, kontrakcija stabla ima dvije osnovne operacije: **Compress** i **Rake**. Operacija Compress odabire vrh $x$ stupnja $2$; dva vrha susjedna vrhu $x$ označimo $y$ i $z$, povučemo novi brid $yz$, podatke vrha $x$ te bridova $xz$ i $xy$ pohranimo u $yz$ i njih izbrišemo. Kao na slici.

![](./images/top-tree1.svg)

Operacija Rake odabire vrh $x$ stupnja $1$, pri čemu vrh $y$ susjedan vrhu $x$ mora imati stupanj veći od $1$; neka je $z$ drugi susjed vrha $y$. Podatke vrha $x$ i brida $xy$ pohranimo u brid $yz$ i njih izbrišemo. Kao na slici.

![](./images/top-tree2.svg)

Nije teško dokazati da se svako stablo može samo operacijama Compress i Rake sažeti u jedan brid, kao na slici.

![](./images/top-tree3.svg)

### Klasteri

Radi lakšeg izražavanja, izvorno stablo prije bilo kakvih operacija označavamo $T$. Stablo dobiveno iz $T$ nakon nekih operacija kontrakcije (moguće i nijedne) označavamo $T_x$.

Promotrimo koje podatke sadrži neki brid u nekom $T_x$.

Osim vlastitih podataka (naravno, ako taj brid ne postoji u $T$, nema vlastitih podataka) brid može sadržavati i podatke drugih vrhova i bridova koji su u njega spojeni operacijama Compress/Rake. Odaberimo jedan brid iz postupka kontrakcije na donjoj slici i pogledajmo koje vrhove i bridove u $T$ predstavljaju podaci koje sadrži.

![](./images/top-tree4.svg)

Na slici su odabrani brid i odgovarajući dio grafa zaokruženi crvenom.

Vidimo da su vrhovi i bridovi u $T$ koje predstavljaju podaci tog brida povezani. Općenito, podaci pohranjeni u bilo kojem bridu bilo kojeg $T_x$ u $T$ čine povezani podgraf. Takav povezani podgraf nazivamo **klaster (Cluster)**.

Međutim, klaster je **nepotpun podgraf**: neke krajnje točke bridova koje sadrži nisu u njemu samom. Te krajnje točke nazivamo **krajnjim točkama (Endpoint)** klastera, vrhove povezanog podgrafa koje sadrži nazivamo **unutarnjim vrhovima (Internal Node)**, a bridove povezanog podgrafa **unutarnjim bridovima (Internal Edge)**.

Svaki klaster ima sljedeća svojstva:

1.  Klaster pohranjuje i održava samo podatke unutarnjih vrhova i unutarnjih bridova.

2.  Klaster ima dvije krajnje točke. To su upravo dva vrha koja u $T_x$ spaja brid koji predstavlja taj klaster. Put između dviju krajnjih točaka nazivamo **putem klastera (Cluster Path)**; ako su krajnje točke klastera $x$ i $y$, klaster ćemo označavati $C(x,y)$.

3.  Unutarnji vrhovi spojeni su samo s krajnjim točkama ili unutarnjim vrhovima.

Posebno, svaki brid u $T$ sam je za sebe klaster (sadrži samo vlastite podatke); takav klaster nazivamo **baznim klasterom (Base Cluster)**. Za završno $T_x$, dobiveno kontrakcijom $T$ do jednog brida, klaster koji predstavlja taj brid sadrži podatke cijelog $T$ osim dviju krajnjih točaka; taj klaster nazivamo **korijenskim klasterom (Root Cluster)**.

![](./images/top-tree5.svg)

Na slici su gore spomenuti bazni klasteri označeni crvenom.

Promotrimo li operacije Compress/Rake iz perspektive klastera, vidimo da obje „spajaju dva u jedan” i ostavljaju jedan novi klaster, pa je postupak kontrakcije stabla ujedno postupak spajanja svih baznih klastera u jedan klaster.

Tako dobivamo i donju sliku, koja je drugi prikaz niza operacija kontrakcije.

![](./images/top-tree6.svg)

### Top Tree

Sada želimo prikazati cijeli postupak kontrakcije nekog stabla.

Mogli bismo ga prikazati na dva gore opisana načina, ali to je vrlo nezgodno: ako kontrakcija ima $n$ koraka, trebalo bi nam $n$ stabala da prikažemo cijelu kontrakciju.

Za jednostavniji prikaz jedne kontrakcije nekog stabla uvodimo **Top Tree**.

![](./images/top-tree7.jpg)

Na slici je Top Tree izgrađen na temelju gornjeg načina kontrakcije i izvornog stabla.

Top Tree ima sljedeća svojstva:

1.  Jedan Top Tree odgovara jednom izvornom stablu i jednom načinu njegove kontrakcije; svaki čvor Top Treea predstavlja neki brid u nekom $T_x$, tj. neki klaster nastao tijekom kontrakcije. Čvorovi oblika $N_x$ na slici predstavljaju klaster nastao operacijom `compress(x)`.

2.  Čvor Top Treea ima dva djeteta (svako predstavlja jedan klaster); klaster koji predstavlja taj čvor novi je klaster dobiven spajanjem tih dvaju klastera operacijom Compress ili Rake.

3.  Listovi Top Treea bazni su klasteri, a korijen je korijenski klaster. Stoga, ako Top Tree raslojimo po topološkom poretku, svaki sloj predstavlja jedno $T_x$.

### Održavanje podataka ternarnim Self-Adjusting Top Treeom

#### Princip

Golemo pojednostavljenje postupka kontrakcije pomoću Top Treea pokazuje nam mogućnost održavanja podataka na stablu održavanjem postupka kontrakcije; SATT upravo na tom principu održava podatke na stablu.

Primijetite da je postupak kontrakcije ujedno postupak postupnog dodavanja podataka na stablu: kad izvršimo `compress(x)`, podaci vrha $x$ od tog trenutka počinju se pojavljivati u nekom klasteru i utječu na rezultat.

Pretpostavimo da Top Treeom održavamo neko stablo $T$ u kojem svaki vrh i brid ima težinu, a želimo održavati zbroj težina u $T$.

Ako sada želimo izmijeniti težinu nekog vrha $x$ u $T$, očito moramo izmijeniti podatke svih čvorova Top Treea čiji klaster sadrži $x$, što bi po operaciji imalo složenost reda $O(n)$.

Međutim, ako odabrani vrh ima malo čvorova u Top Treeu čiji klaster sadrži $x$, tj. ako se njegovi podaci dodaju u klastere što kasnije, složenost jedne operacije znatno se smanjuje. Kao na slici.

![](./images/top-tree8.jpg)

SATT održava podatke na stablu tako da mijenja redoslijed u kojem se podaci **nekog vrha/nekog puta** tijekom kontrakcije dodaju u klastere (kako bi smanjio složenost pojedine izmjene).

### Stvarna struktura

Najprije izvorno stablo $T$ raslojimo i odaberemo korijen. Zatim promotrimo korijenski klaster Top Treea za neki redoslijed kontrakcije; on ima dvije krajnje točke. Neka je jedna od njih korijen izvornog stabla, a druga proizvoljna.

![](./images/top-tree9.jpg)

Na slici je korijenskom klasteru odabran par krajnjih točaka; ovdje su pri označavanju klastera zaokružene i krajnje točke.

Iz osnovnih operacija kontrakcije znamo da su vrhovi i bridovi na putu klastera $(j,h,c,jh,hc)$ na kraju dodani u $C(k,g)$ operacijom Compress, dok su vrhovi izvan puta klastera $(a,b,i,f,g,e,ig,\cdots)$ dodani u $C(k,g)$ operacijom Rake.

Izdvojimo put klastera; to je stablo posebnog oblika (lanac) i za njega izgradimo top tree (redoslijed kontrakcije koji predstavlja je proizvoljan).

![](./images/top-tree10.jpg)

Tu strukturu nazivamo **Compress Tree**, jer se u tom Top Treeu dva djeteta bilo kojeg čvora spajaju u roditelja operacijom Compress.

Čvorove Compress Treea nazivamo **Compress Node**. Promatramo li samo trenutačni put klastera, Compress Node koji nije list predstavlja jedan compress: podatke lijevog i desnog djeteta spojimo, a zatim dodamo podatke vrha $x$ koje pohranjuje sam `compress(x)`. Taj Compress Tree održava podatke puta klastera $C(k,g)$.

Osim toga, u Compress Treeu zapravo postavljamo i neka ograničenja na korišteni Top Tree. Primijetite da Compress Tree održava lanac u kojem su dubine vrhova u $T$ međusobno različite; zahtijevamo da redoslijed baznih klastera u inorder obilasku Compress Treea odgovara dubini pripadnih bridova u $T$, pri čemu manji inorder redni broj znači manju dubinu. Isto vrijedi i za `compress(x)` pridružen svakom vrhu $x$.

Sada održavamo podatke izvan puta klastera. Pretpostavimo da su vrhovi i bridovi izvan puta klastera već oblikovali maksimalne klastere, a ti su maksimalni klasteri nastali međusobnim Rakeom manjih klastera, zaokruženih plavom. Postupak spajanja nekoliko manjih klastera u jedan maksimalni klaster prikazujemo ternarnim stablom; analogno tu strukturu nazivamo **Rake Tree**, a njezine čvorove **Rake Node**. Svaki Rake Node predstavlja klaster nastao Rakeom lijevog i desnog djeteta na manji klaster koji predstavlja srednje dijete. Vidi donju sliku: svaki čvor Rake Treea predstavlja manje klastere u $T$ s istim krajnjim točkama.

![](./images/top-tree11.jpg)

Na slici su plavom zaokruženi maksimalni klasteri, a žutom manji klasteri.

Te manje klastere obradimo na isti način: odaberemo im put klastera, izgradimo Compress Tree, … i tako rekurzivno; time nastaje mnogo Compress Treeova i Rake Treeova koji prikazuju postupak kontrakcije.

![](./images/top-tree12.jpg)

Gornja slika prikazuje Rake-Compress Tree izvornog stabla (budući da je na svaki Rake Node spojen jedan Compress Tree, izgleda kao Rake Tree na koji je spojeno mnogo Compress Treeova) i Compress Tree koji predstavlja put korijenskog klastera.

Pokušajmo ta stabla na neki način spojiti u uređenu cjelinu. Neka je zajednička krajnja točka skupa najmanjih klastera koje predstavlja neki Rake Tree vrh $x$. Srednjoj djeci tih Rake Nodeova (skupu Compress Treeova) dodamo drugu krajnju točku, različitu od $x$, ali tako da se očuvaju inorder obilazak i osnovna svojstva Top Treea, kao na slici.

![](./images/top-tree13.jpg)

Ovaj korak zapravo znači da se dodavanje nekog vrha iz $T$ operacijom Rake događa izravno u Compress Treeu; to nam ne samo omogućuje ispravno održavanje podataka Rake Nodea (dovoljno je spojiti podatke troje djece), nego i čini strukturu Compress Treea potpunijom. U sljedećem koraku Compress Tree pretvaramo u ternarno stablo: ako je zajednička krajnja točka nekog Rake Treea vrh $x$, taj Rake Tree vješamo kao srednje dijete čvora `compress(x)`, kao na slici.

![](./images/top-tree14.jpg)

Značenje ternariziranog čvora `compress(x)` sada postaje: najprije srednje dijete Rakeom dodati na put klastera, a zatim zbrojiti podatke lijevog i desnog djeteta i vrha $x$.

Na kraju još obradimo Compress Tree puta korijenskog klastera: jednako kao kod svih ostalih Compress Treeova, po inorder obilasku dodamo mu obje krajnje točke, tako da njegov korijen pohranjuje podatke cijelog $T$.

Time smo ostvarili održavanje podataka stabla ternarnim Self-Adjusting Top Treeom.

![](./images/top-tree15.jpg)

Sažeto, SATT ima sljedeća svojstva:

1.  SATT se sastoji od Compress Treeova i Rake Treeova; Compress Tree poseban je Top Tree, a Rake Tree ternarno je stablo; oba odgovaraju postupku kontrakcije nekog stabla.

2.  Čvor Compress Treea ima najviše troje djece. Compress Tree podržava rotacije slične onima u Splay stablu (dovoljno je da inorder obilazak ostane nepromijenjen; pri rotaciji čvora njegovo srednje dijete ostaje na mjestu).

3.  Čvor Rake Treea sigurno ima srednje dijete. Rake Tree podržava rotacije slične onima u Splay stablu (dovoljno je da inorder obilazak ostane nepromijenjen; pri rotaciji čvora njegovo srednje dijete ostaje na mjestu).

4.  Topološki poredak SATT-a odražava redoslijed kontrakcije izvornog stabla $T$.

Može li SATT ostvariti gore spomenutu „izmjenu redoslijeda u kojem se podaci nekog vrha/nekog puta tijekom kontrakcije dodaju u klastere”? Odgovor je da.

U SATT-u postoji operacija `access(x)` koja čini vrh $x$ nekorijenskom krajnjom točkom korijenskog klastera i ujedno `compress(x)` čini korijenom SATT-a.

Operacijom `access(x)` u amortiziranom vremenu $O(\log n)$ čvor koji u SATT-u predstavlja `compress(x)` rotiramo do korijena cijelog SATT-a; prema četvrtom svojstvu SATT-a time smo promijenili redoslijed operacije `compress(x)` tako da se izvršava posljednja, pa se i podaci vrha $x$ dodaju posljednji; kad želimo izmijeniti podatke vrha $x$, dovoljno je ažurirati `compress(x)`.

### Implementacija

#### Funkcije tipa Push

Najprije razmotrimo prijenos podataka prema gore, tj. funkciju `Pushup(x)`. Pri održavanju podataka nekog čvora SATT-a najprije razlikujemo je li čvor u Compress Treeu ili u Rake Treeu; razlog je opisan gore i ne ponavljamo ga. Primjer: održavanje veličine podstabla nekog vrha.

```cpp
// ls(x) lijevo dijete od x
// rs(x) desno dijete od x
// ms(x) srednje dijete od x
// type==0 je Compress Node
// type==1 je Rake Node
void pushup(int x, int type) {
  if (type == 0)
    size[x] = size[rs(x)] + size[ms(x)] + 1;
  else
    size[x] = size[rs(x)] + size[ms(x)] + size[ls(x)];
  return;
}
```

Za upit veličine podstabla vrha $x$ napravimo Access do korijena SATT-a; odgovor je size srednjeg djeteta $+1$, jer je prema gornjem nakon Accessa upravo srednje dijete njegovo pravo podstablo.

Zatim razmotrimo prijenos podataka prema dolje, tj. funkciju `Pushdown(x)`. Ako želimo izmijeniti cijelo podstablo u izvornom stablu, prirodna je ideja: taj čvor izravno Accessamo do korijena SATT-a i njegovu srednjem djetetu postavimo oznaku. Slično, za upit nad podstablom nakon Accessa upitamo srednje dijete.

Ako želimo izmijeniti cijeli put u izvornom stablu, exposeamo obje krajnje točke puta, pri čemu `expose(x, y)` znači: vrh $x$ postaje korijen $T$, a vrh $y$ druga krajnja točka korijenskog klastera. U SATT-u je tada Compress Tree korijenskog klastera upravo put od $x$ do $y$. Dakle, dovoljno je Compress Treeu korijenskog klastera postaviti oznaku. Slično, za upit nad lancem nakon exposea upitamo korijen.

Time znamo kako riješiti uvodni problem.

```cpp
void pushdown(int x, int type) {
  if (type == 0) {
    // obrada lanca
    chain[ls(x)] += chain[x] chain[rs(x)] += chain[x];
    val[ls(x)] += chain[x];
    val[rs(x)] += chain[x];
    // obrada podstabla
    subtree[ls(x)] += subtree[x];
    subtree[rs(x)] += subtree[x];
    subtree[ms(x)] += subtree[x];
    val[ls(x)] += subtree[x];
    val[rs(x)] += subtree[x];
    val[ms(x)] += subtree[x];
    subtree[x] = 0;
  } else {
    subtree[ls(x)] += subtree[x];
    subtree[rs(x)] += subtree[x];
    subtree[ms(x)] += subtree[x];
    val[ls(x)] += subtree[x];
    val[rs(x)] += subtree[x];
    val[ms(x)] += subtree[x];
    subtree[x] = 0;
  }
  return;
}

// spuštanje oznaka
void pushall(int x, int type) {
  if (!isroot(x)) pushall(father[x], type);
  pushdown(x, type);
  return;
}
```

#### Funkcije tipa Splay

Znamo da se Rake Tree i Compress Tree u SATT-u mogu rotirati, tj. mogu se održavati Splayem. Stoga možemo napisati sljedeći kod:

```cpp
// je srednje dijete nekog čvora ili nema roditelja
// ls lijevo dijete čvora SATT-a
// rs desno dijete čvora SATT-a
// ms srednje dijete čvora SATT-a
// type==1 u Rake Treeu
// type==0 u Compress Treeu
bool isroot(int x) { return rs(father[x]) != x && ls(father[x]) != x; }

bool direction(int x) { return rs(father[x]) == x; }

void rotate(int x, int type) {
  int y = father[x], z = father[y], d = direction(x), w = son[x][d ^ 1];
  if (z) son[z][ms(z) == y ? 2 : direction(y)] = x;
  son[x][d ^ 1] = y;
  son[y][d] = w;
  if (w) father[w] = y;
  father[y] = x;
  father[x] = z;
  pushup(y, type);
  pushup(x, type);
  return;
}

void splay(int x, int type, int goal = 0) {
  pushall(x, ty);  // spuštanje oznaka
  for (int y; y = father[x], (!isroot(x)) && y != goal; rotate(x, ty)) {
    if (father[y] != goal && (!isroot(y))) {
      rotate(direction(x) ^ diretion(y) ? x : y, type);
    }
  }
  return;
}
```

Valja primijetiti da se funkcije `direction` i `isroot` razlikuju od onih u običnom Splayu, jer se, kako god čvor rotiramo, njegovo srednje dijete ne mijenja.

#### Funkcije tipa Access

Značenje `access(x)` jest: vrh $x$ rotirati do korijena cijelog SATT-a, tako da vrh $x$ postane jedna od dviju krajnjih točaka korijenskog klastera (druga je krajnja točka korijen $T$), a da se pri tome ne promijene struktura ni korijen izvornog stabla.

Da bismo ostvarili `access(x)`, najprije ga rotiramo do korijena Compress Treea u kojem se nalazi, a zatim uklonimo desno dijete vrha $x$, čime $x$ postaje krajnja točka klastera koji odgovara njegovu Compress Treeu.

```cpp
if (rs(x)) {
  int y = new_node();
  setfather(ms(x), y, 0);
  setfather(rs(x), y, 2);
  rs(x) = 0;
  setfather(y, x, 2);
  pushup(y, 1);
  pushup(x, 0);
}
```

Ako je vrh $x$ time već stigao do korijena, završavamo; ako nije, izvodimo sljedeće korake da bi preskočio Rake Tree iznad sebe:

1.  Njegova roditelja (sigurno Rake Node) splayamo do korijena njegova Rake Treea;

2.  Djeda vrha $x$ (sigurno Compress Node) splayamo do korijena njegova Compress Treea.

3.  Ako djed vrha $x$ ima desno dijete, zamijenimo vrh x i desno dijete djeda, ažuriramo podatke i završavamo.

4.  Ako djed nema desno dijete, vrh $x$ najprije učinimo desnim djetetom djeda; tada bivši roditelj vrha $x$ nema srednje dijete, a prema gore opisanom svojstvu Rake Nodea on ne može postojati. Stoga pozovemo funkciju `Delete`, izbrišemo ga i završavamo.

Koraci 1 i 2 zajedno se nazivaju **Local Splay**. Koraci 3 i 4 zajedno se nazivaju **Splice**. Radi praktičnosti sve ih pišemo u funkciji `Splice(x)`.

Gore spomenuta funkcija `Delete(x)` radi ovako:

1.  Provjeri ima li vrh $x$ koji brišemo lijevo dijete; ako ima, sljedbenika iz podstabla lijevog djeteta rotira pod vrh $x$ (postaje novo lijevo dijete), a zatim desno dijete (ako postoji) postaje desno dijete lijevog djeteta; tada lijevo dijete vrha $x$ zamjenjuje vrh $x$. To odgovara operaciji spajanja u Splayu.

2.  Ako nema lijevog djeteta, vrh $x$ izravno zamjenjuje njegovo desno dijete.

Nije teško primijetiti da `Splice(x)` mijenja odabir krajnjih točaka nekih klastera izvornog stabla. Nakon jednog splicea roditelja vrha $x$ uzimamo kao novi vrh $x$ i radimo sljedeći splice.

Na kraju ćemo otkriti da je vrh $x$ s kojim smo započeli sigurno na krajnjem desnom mjestu Compress Treea korijenskog klastera. Preostaje samo na kraju napraviti jedan **Global Splay** i rotirati ga do korijena SATT-a.

```cpp
// ls lijevo dijete čvora SATT-a
// rs desno dijete čvora SATT-a
// ms srednje dijete čvora SATT-a
// son[x][0] ls
// son[x][1] rs
// son[x][2] ms
// type==1 u Rake Treeu
// type==0 u Compress Treeu
int new_node() {
  if (top) {
    top--;
    return Stack[top + 1];
  }
  return ++tot;
}

void setfather(int x, int fa, int type) {
  if (x) father[x] = fa;
  son[fa][type] = x;
}

void Delete(int x) {
  setfather(ms(x), father[x], 1);
  if (ls(x)) {
    int p = ls(x);
    pushdown(p, 1);
    while (rs(p)) p = rs(p), pushdown(p, 1);
    splay(p, 1, x);
    setfather(rs(x), p, 1);
    setfather(p, father[x], 2);
    pushup(p, 1);
    pushup(father[x], 0);
  } else
    setfather(rs(x), father[x], 2);
  Clear(x);
}

void splice(int x) {
  // local splay
  splay(x, 1);
  int y = father[x];
  splay(y, 0);
  pushdown(x, 1);
  // splice
  if (rs(y)) {
    swap(father[ms(x)], father[rs(y)]);
    swap(ms(x), rs(y));
  } else
    Delete(x);
  pushup(x, 1);
  pushup(y, 0);
}

void access(int x) {
  splay(x, 0);
  if (rs(x)) {
    int y = new_node();
    setfather(ms(x), y, 0);
    setfather(rs(x), y, 2);
    rs(x) = 0;
    setfather(y, x, 2);
    pushup(y, 1);
    pushup(x, 0);
  }
  while (father[x]) {
    splice(father[x]);
    x = father[x];
    pushup(x, 0);
  }
  splay(x, 0)  // global splay
}
```

Ako želimo da neki vrh postane korijen izvornog stabla, vrh $x$ Accessamo do korijena SATT-a; tada je vrh $x$ već jedna krajnja točka završnog klastera. Iz svojstva inorder obilaska Compress Treea slijedi da zrcaljenjem Compress Treea u kojem je vrh $x$ (zamjenom lijevog i desnog djeteta svih čvorova) vrh $x$ postaje korijen izvornog stabla. U implementaciji to radimo tako da vrhu $x$ postavimo oznaku okretanja koju poslije spuštamo.

```cpp
void makeroot(int x) {
  access(x);
  push_rev(x);
}
```

Time se `expose(x, y)` nameće sam od sebe:

```cpp
void expose(int x, int y) {
  makeroot(x);
  access(y);
}
```

### Link & Cut

Sada želimo spojiti bridom dva nepovezana vrha izvornog stabla. Najprije jedan od njih, vrh $x$, učinimo korijenom izvornog stabla, a drugi vrh $y$ rotiramo do korijena; tada vrh $y$ treba postati desno dijete vrha $x$. Zatim na desno dijete vrha $y$ objesimo taj brid (u SATT-u koji održava samo vrhove ovaj se korak može preskočiti).

```cpp
void Link(int x, int y, int z) {
  // z predstavlja brid koji spaja x i y
  access(x);
  makeroot(y);
  setfather(y, x, 1);
  setfather(z, y, 0);
  pushup(x, 0);
  pushup(y, 0);
}
```

`Cut` radi na sličnom principu kao `Link`.

```cpp
void cut(int x, int y) {
  expose(x, y);
  clear(rs(x));  // brišemo bazni klaster xy
  father[x] = ls(y) = rs(x);
  pushup(y, 0);
}
```

### Potpuni kod

??? note "[Luogu P3690【模板】动态树](https://www.luogu.com.cn/problem/P3690)"
    ```cpp
    --8<-- "docs/ds/code/top-tree/top-tree_1.cpp"
    ```

### Dokaz vremenske složenosti SATT-a

Neka je u SATT-u (s $n$ čvorova) funkcija potencijala trenutačnog stanja $x$

$$
\varphi(x)= \sum_{i=1}^{n} r(i)
$$

gdje je $r(i) = \lceil \log_2 \text{siz}(i) \rceil$, a $\text{siz}(i)$ veličina podstabla s korijenom $i$.

Tada je amortizirana složenost splaya u SATT-u očito i dalje $3n\log n + 1$, iako je SATT ternarno stablo.

Stoga je za SATT dovoljno dokazati ispravnost složenosti funkcije Access da bismo dokazali vremensku složenost SATT-a.

Analizirajmo korak po korak amortiziranu složenost Accessa.

Najprije vrh $x$ rotiramo do korijena Compress Treea u kojem se nalazi; amortizirana složenost tog koraka je

$$
a \leq  3\log n +1
$$

Zatim vrhu $x$ uklanjamo desno dijete; amortizirana složenost tog koraka je

$$
a = 1 + r'(\gamma)- 0 \leq \log n +1
$$

![](./images/top-tree16.jpg)

Slika prikazuje postupak uklanjanja desnog djeteta vrha $x$.

Slijedi naizmjenično izvođenje Local Splaya i Splicea; nakon nekoliko Spliceova vrh $x$ rotiran je do korijena SATT-a. Analizirajmo jedan par Local Splay, Splice:

![](./images/top-tree17.jpg)

![](./images/top-tree18.jpg)

![](./images/top-tree19.jpg)

Slike prikazuju jedan Splice nad vrhom $x$, bez završnog dijela lijeve rotacije vrha $x$.

Radi lakšeg izražavanja, neka je $r_x(i)$ vrijednost $r$ vrha $i$ u stanju $x$.

Sa slike se lako vidi da je amortizirana složenost operacije iz stanja 1 u stanje 2 (Local Splay koji roditelja vrha $x$ rotira do korijena njegova Rake Treea)

$$
a \leq  3(r_2(\gamma)- r_1(\gamma))+1
$$

Sa slike se lako vidi da je amortizirana složenost operacije iz stanja 2 u stanje 3 (Local Splay koji djeda vrha $x$ rotira do korijena njegova Compress Treea)

$$
a \leq  3(r_3(B)- r_2(B))+1
$$

Ključna je analiza operacije iz stanja 3 u stanje 4 (Splice)

$$
a = r_4(\gamma) -r_3(\gamma) +1
$$

Nije teško primijetiti da je $r_4(\gamma) \leq r_3(B)$

pa je amortizirana složenost te operacije

$$
\begin{aligned}
a &\leq r_3(B)- r_3(\gamma)+1\\
&\leq 3(r_3(B)- r_3(\gamma))+1\\
\end{aligned}
$$

Zbrajanjem gornjih koraka složenost jednog Splicea je

$$
a\leq 3r_3(B)+3r_3(B)+3r_2(\gamma)-3r_3(\gamma)-3r_2(B)-3r_1(\gamma)+3
$$

Označimo $r'(X)$ vrijednost $r$ vrha $X$ sljedećeg Splicea (tj. vrha $B$ u stanju 4). Primijetimo da je $r_3(\gamma),r_1(\gamma) \ge r_1(X)$, $r_3(B),r_2(\gamma) \leq r'(X)$ i $r_3(B)=r_2(B)$, pa

$$
a\leq  9(r'(X)-r(X))+3
$$

Osim gornje složenosti, u Spliceu se može pojaviti i dodatna amortizirana složenost zbog `delete(x)`; taj dio označimo $a' \leq 3\log n +1$.

Zanemarimo načas $a'$. $r'(X)$ svakog Splicea jednak je $r(X)$ sljedećeg, a $r(X)$ prvog Splicea jednak je $r(X)$ u trenutku kad smo na početku vrh $x$ rotirali do korijena njegova Compress Treea; stoga za složenost jednog `access(x)` bez `delete(x)` imamo:

$$
a \leq 9(r'(x)-r(x))+ 3k + 1
$$

gdje je $k$ broj Spliceova.

Čini se da $a$ nosi član $3k+1$ koji onemogućuje amortiziranu analizu, ali s njime se možemo nositi. Primijetimo da se rotacije zig-zig/zig-zag mogu amortizirati ovako

$$
\begin{aligned}
a &\leq 3(r'(X)-r(X)) + q\\
&\leq 3(q-1)(r'(X)-r(X))
\end{aligned}
$$

Ako nađemo dovoljno operacija zig-zig i zig-zag, tih $3k+1$ možemo raspodijeliti na njih i time ga ukloniti.

Uočavamo da upravo Global Splay sadrži dovoljno zig-zig i zag-zig operacija koje možemo iskoristiti, jer je broj čvorova u Global Splayu sigurno veći od $k$, a broj čvorova na putu od vrha $x$ do korijena Global Splaya nije manji od $k$; drugim riječima, u jednom `access(x)` sigurno je barem $\dfrac k2$ operacija zig-zag. Uračunamo li amortiziranu složenost Global Splaya $a \leq 3\log n +1$, amortizirana složenost jednog `access(x)` bez `delete(x)` je

$$
\begin{aligned}
a&\leq 9(r'(X)-r(X)) + 3k + 1 + 18(r''(X)-r'(X)) -S+1 +3 \log n +1,S \ge 3k\\
a&\leq 18(r''(X)-r(X)) +2 +3\log n+1\\
a&\leq 21(r''(X)-r(X)) +3
\end{aligned}
$$

Sada uračunamo $a'$ i napišimo ukupnu formulu za $m$ operacija `access(x)`.

$$
\sum_{i=1}^m a_i' + \sum_{i=1}^m a_i = \sum_{i=1}^m c_i + \varphi(x_n) -\varphi(x_0)
$$

Tražimo stvarnu složenost

$$
\begin{aligned}
\sum_{i=1}^m c_i &= \sum_{i=1}^m a_i +\sum_{i=1}^m a_i' - \varphi(x_n) +\varphi(x_0)\\
&\le \sum_{i=1}^m a_i' + 21m\log n +n\log n +3m
\end{aligned}
$$

Primijetimo da je bit operacije `delete(x)` brisanje jednog Rake Nodea, a u $m$ operacija dodajemo najviše $m$ Rake Nodeova; prema definiciji Rake Nodea na početku ih je najviše $n$, pa ukupno radimo najviše $m+n$ operacija `delete(x)`. Iz $a' \leq 3\log n +1$ slijedi

$$
\sum_{i=1}^m c_i \leq 3(m+n)\log n + 21m\log n +n\log n +4m +n
$$

Time smo dokazali složenost Accessa, a ostale funkcije ili se temelje na Accessu ili imaju konstantnu složenost po operaciji, pa smo dokazali složenost SATT-a.

Usput, ako kao u LCT-u preskočimo Global Splay i umjesto toga pri svakom Spliceu izravno jednom rotiramo vrh koji Accessamo, vremenska je složenost i dalje ispravna (u praksi je inačica bez Global Splaya znatno brža i na Luogu P3690 ravnopravna s LCT-om).

### Primjeri

#### Primjer 1

???+ note "[CEOI 2019 Dynamic Diameter](https://loj.ac/p/3163)"
    Zadano je stablo s $n$ vrhova s težinama na bridovima i $q$ ažuriranja; svako mijenja težinu jednog brida, nakon čega treba ispisati promjer stabla. Obvezno online.

Za održavanje dinamičkog promjera, nakon izgradnje SATT-a, dovoljno je u `Pushup(x)` održavati odgovor za svaki čvor i na kraju upitati odgovor u korijenu (tj. promjer cijelog stabla).

```cpp
void pushup(int x, int op) {
  if (op == 0) {
    // Compress Node
    len[x] = len[ls(x)] + len[rs(x)];
    diam[x] = maxs[ls(x)][1] + maxs[rs(x)][0];
    diam[x] =
        max(diam[x], max(maxs[ls(x)][1], maxs[rs(x)][0]) + maxs[ms(x)][0]);
    diam[x] = max(diam[x], max(max(diam[ls(x)], diam[rs(x)]), diam[ms(x)]));
    maxs[x][0] =
        max(maxs[ls(x)][0], len[ls(x)] + max(maxs[ms(x)][0], maxs[rs(x)][0]));
    maxs[x][1] =
        max(maxs[rs(x)][1], len[rs(x)] + max(maxs[ms(x)][0], maxs[ls(x)][1]));
  } else {
    // Rake Node
    diam[x] = maxs[ls(x)][0] + maxs[rs(x)][0];
    diam[x] =
        max(diam[x], maxs[ms(x)][0] + max(maxs[ls(x)][0], maxs[rs(x)][0]));
    diam[x] = max(max(diam[x], diam[ms(x)]), max(diam[ls(x)], diam[rs(x)]));
    maxs[x][0] = max(maxs[ms(x)][0], max(maxs[ls(x)][0], maxs[rs(x)][0]));
  }
  return;
}
```

Ovdje je $diam$ odgovor trenutačnog čvora (promjer klastera koji taj čvor predstavlja). $len$ je duljina puta klastera u kojem je trenutačni Compress Node, a $maxs_{0/1}$ najveća udaljenost od Compress Nodea do unutarnjih vrhova i krajnjih točaka klastera bez odabira djeteta na putu klastera/bez odabira roditelja (ako je riječ o Rake Nodeu, pohranjuje se samo $maxs_0$, najveća udaljenost od gornje krajnje točke trenutačnog klastera do unutarnjih vrhova i krajnjih točaka). Pri svakom upitu dovoljno je pročitati diam u korijenu SATT-a; ispravnost je očita.

Pripazite na izmjene u `Pushrev(x)`.

```cpp
void pushrev(int x) {
  if (!x) return;
  r[x] ^= 1;
  swap(ls(x), rs(x));
  swap(maxs[x][0], maxs[x][1]);
}
```

#### Primjer 2

???+ note "[„CSP-S 2019” Težište stabla](https://loj.ac/p/3213)"
    Zadano je stablo. Za svaki brid zasebno izbrišemo taj brid i odredimo zbroj indeksa težišta dvaju nastalih podstabala; ispišite ukupni zbroj.

Ako bismo mogli dinamički u $O(\log n)$ održavati težište stabla, zadatak bi bio riješen.

SATT podržava dinamičko održavanje težišta u $O(\log n)$; za to je potrebno **nelokalno pretraživanje (Non-local Search)**.

Za neko svojstvo na stablu: ako vrh/brid koji ima to svojstvo u cijelom stablu ima to svojstvo i u svim podstablima koja ga sadrže, svojstvo nazivamo **lokalnim (Local)**; inače ga nazivamo **nelokalnim (Non-local)**. Lokalni se podaci obično mogu održavati funkcijom `pushup(x)`.

Primjerice, minimalna težina lokalna je: ako vrh/brid ima najmanju težinu u cijelom stablu, ima je i u svim podstablima koja ga sadrže; druga najmanja težina očito je nelokalna.

I gore održavani $diam$ lokalni je podatak.

Natrag na zadatak: težište je očito nelokalni podatak i ne može se održavati jednostavnim `pushup(x)`. Razmotrimo pretraživanje po SATT-u:

Pretraživanje počinje od korijena SATT-a, tj. od korijenskog klastera. Primijetite da težište ima lijepo svojstvo: ako je broj vrhova s jedne strane nekog brida veći ili jednak broju vrhova s druge strane, na toj se strani brida sigurno nalazi barem jedno težište (težišta mogu biti dva).

Neka $sum$ označava broj vrhova nekog klastera, a $maxs$ najveći $sum$ među srednjom djecom svih Rake Nodeova jednog Rake Treea.

```cpp
void pushup(int x, int op) {
  if (op == 0) {
    // Compress Node
    sum[x] = sum[ls(x)] + sum[rs(x)] + sum[ms(x)] + 1;
  } else {
    // Rake Node
    maxs[x] = max(maxs[ls(x)], max(maxs[rs(x)], sum[ms(x)]));
    sum[x] = sum[ls(x)] + sum[rs(x)] + sum[ms(x)];
  }
}
```

![](./images/top-tree20.jpg)

Slika prikazuje SATT tijekom Non-local Searcha i pripadno izvorno stablo $T$.

Uspoređujemo sljedeće:

1.  Usporedimo $sum$ klastera $compress(Y)$ sa $sum$ unije klastera $compress(Z)$, klastera $A$ i vrha $X$ (nazovimo je privremeno klaster $\alpha$). Ako je $sum$ klastera $compress(Y)$ veći ili jednak, barem jedno težište nalazi se u podstablu $compress(Y)$ i rekurzivno pretražujemo $compress(Y)$. (Ako vrijedi jednakost, i vrh $X$ je težište i treba ga zabilježiti.)

2.  Usporedimo $sum$ klastera $compress(Z)$ sa $sum$ unije klastera $compress(Y)$, klastera $A$ i vrha $X$ (nazovimo je privremeno klaster $\beta$). Ako je $sum$ klastera $compress(Z)$ veći ili jednak, barem jedno težište nalazi se u podstablu $compress(Z)$ i rekurzivno pretražujemo $compress(Z)$. (Ako vrijedi jednakost, i vrh $X$ je težište i treba ga zabilježiti.)

3.  Usporedimo $sum$ manjeg klastera s najvećim $sum$ u Rake Treeu srednjeg djeteta vrha $x$ sa $sum$ unije klastera $compress(Y)$, klastera $A$, vrha $X$ i ostalih manjih klastera (nazovimo je privremeno klaster $Y$). Ako je $sum$ tog manjeg klastera veći ili jednak, barem jedno težište nalazi se u podstablu tog manjeg klastera i rekurzivno ga pretražujemo. Ako vrijedi jednakost, i vrh $X$ je težište i treba ga zabilježiti.

4.  Ako nijedna usporedba ne vodi na rekurziju, vrh $X$ sigurno je težište; zabilježimo ga i završavamo.

Prvi korak pretraživanja očito je ispravan; kako nastaviti dalje?

Ako smo se spustili u $Y$, podaci pohranjeni u $Y$ nisu potpuni, jer $compress(Y)$ pohranjuje samo podatke vlastitog klastera, a mi tražimo težište cijelog stabla. Rješenje je zabilježiti podatke prethodnog klastera i pri usporedbi u vrhu $Y$ spojiti podatke prethodnog klastera s podacima vrha $Y$. Konkretna implementacija:

```cpp
void non_local_search(int x, int lv, int rv, int op) {
  // lv i rv su podaci prethodno pretraženog klastera
  if (!x) return;
  psd(x, 0);
  if (op == 0) {
    if (maxs[ms(x)] >=
        sum[ms(x)] - maxs[ms(x)] + sum[rs(x)] + sum[ls(x)] + lv + 1 + rv) {
      if (maxs[ms(x)] ==
          sum[ms(x)] - maxs[ms(x)] + sum[rs(x)] + sum[ls(x)] + lv + 1 + rv) {
        if (ans1)
          ans2 = x;
        else
          ans1 = x;
      }
      non_local_search(
          ms(x),
          sum[ms(x)] - maxs[ms(x)] + sum[rs(x)] + sum[ls(x)] + 1 + lv + rv, 0,
          1);
      return;
    }
    if (ss[rs(x)] + rv >= ss[ms(x)] + ss[ls(x)] + lv + 1) {
      if (ss[rs(x)] + rv == ss[ms(x)] + ss[ls(x)] + lv + 1) {
        if (ans1)
          ans2 = x;
        else
          ans1 = x;
      }
      non_local_search(rs(x), sum[ms(x)] + 1 + sum[ls(x)] + lv, rv, 0);
      return;
    }
    if (sum[ls(x)] + lv >= sum[ms(x)] + sum[rs(x)] + 1 + rv) {
      if (sum[ls(x)] + lv == sum[ms(x)] + sum[rs(x)] + 1 + rv) {
        if (ans1)
          ans2 = x;
        else
          ans1 = x;
      }
      non_local_search(ls(x), lv, rv + sum[ms(x)] + 1 + sum[rs(x)], 0);
      return;
    }
  } else {
    if (maxs[ls(x)] == maxs[x]) {
      non_local_search(ls(x), lv, rv, 1);
      return;
    }
    if (maxs[rs(x)] == maxs[x]) {
      non_local_search(rs(x), lv, rv, 1);
      return;
    }
    non_local_search(ms(x), lv, rv, 0);
    return;
  }
  if (ans1)
    ans2 = x;
  else
    ans1 = x;
}
```

??? note "Primjer koda"
    ```cpp
    --8<-- "docs/ds/code/top-tree/top-tree_2.cpp"
    ```

### Reference

1.  Robert E. Tarjan and Renato F. Werneck. 2005. Self-adjusting top trees. In Proceedings of the sixteenth annual ACM-SIAM symposium on Discrete algorithms (SODA '05). Society for Industrial and Applied Mathematics, USA, 813–822. DOI 10.5555/1070432.1070547

2.  [Blog negiizhao](https://negiizhao.blog.uoj.ac/blog/4912)
