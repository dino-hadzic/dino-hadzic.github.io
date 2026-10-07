---
title: Stablo rastavljanja i spajanja (divide-combine tree)
---

## Problem o segmentima

Krenimo od jednog „svježeg” problema:

> Za permutaciju brojeva $1-n$ interval čiji je skup vrijednosti neprekinut nazivamo segmentom. Koliko segmenata ima zadana permutacija? Primjerice, segmenti permutacije $\{5 ,3 ,4, 1 ,2\}$ jesu: $[1,1],[2,2],[3,3],[4,4],[5,5],[2,3],[4,5],[1,3],[2,5],[1,5]$.

Na prvi pogled trebalo bi održavati skup vrijednosti intervala, a složenost ne izgleda prijateljski. Segment tree može provjeriti je li neki interval segment, ali teško može prebrojati segmente.

Ovdje uvodimo čudesnu strukturu podataka: stablo rastavljanja i spajanja (divide-combine tree)!

## Neprekinuti segmenti

Prije nego što opišemo samo stablo, uvedimo nekoliko preduvjeta. Budući da definicije iz LCA-ovih slajdova nisu lako razumljive, radi lakšeg praćenja dajemo neke manje stroge (ali razumljivije) definicije.

### Permutacija i neprekinuti segment

**Permutacija**: permutacija $P$ reda $n$ niz je veličine $n$ u kojem $P_i$ poprima sve vrijednosti $1,2,\cdots,n$. Formalnije, permutacija $P$ reda $n$ uređeni je skup koji zadovoljava:

1.  $|P|=n$.
2.  $\forall i,P_i\in[1,n]$.
3.  $\nexists i,j\in[1,n],P_i=P_j$.

    **Neprekinuti segment**: za permutaciju $P$ neprekinuti segment $(P,[l,r])$ označava interval $[l,r]$ takav da je skup vrijednosti $P_{l\sim r}$ neprekinut. Formalnije, za permutaciju $P$ neprekinuti segment je interval $[l,r]$ koji zadovoljava:

$$
(\nexists\ x,z\in[l,r],y\notin[l,r],\ P_x<P_y<P_z)
$$

Posebno, za $l>r$ smatramo da je riječ o praznom neprekinutom segmentu, koji označavamo $(P,\varnothing)$.

Skup svih neprekinutih segmenata permutacije $P$ označavamo $I_P$ i smatramo da je $(P,\varnothing)\in I_P$.

### Operacije nad neprekinutim segmentima

Neprekinuti segmenti definirani su intervalom i skupom vrijednosti, pa možemo definirati presjek, uniju i razliku neprekinutih segmenata.

Neka je $A=(P,[a,b]),B=(P,[x,y])$ i $A,B\in I_P$. Odnosi i operacije nad neprekinutim segmentima mogu se zapisati kao:

1.  $A\subseteq B\iff x\le a\wedge b\le y$.
2.  $A=B\iff a=x\wedge b=y$.
3.  $A\cap B=(P,[\max(a,x),\min(b,y)])$.
4.  $A\cup B=(P,[\min(a,x),\max(b,y)])$.
5.  $A\setminus B=(P,\{i|i\in[a,b]\wedge i\notin[x,y]\})$.

Te su operacije zapravo samo obični presjek, unija i razlika skupova primijenjeni na intervale.

### Svojstva neprekinutih segmenata

Neka očita svojstva neprekinutih segmenata. Ako je $A,B\in I_P,A \cap B \neq \varnothing,A \notin B,B \notin A$, onda vrijedi $A\cup B,A\cap B,A\setminus B,B\setminus A\in I_P$.

Dokaz? U biti se svodi na presjek, uniju i razliku skupova.

## Stablo rastavljanja i spajanja

Dobro, sada dolazimo do glavne stvari. Vjerojatno ste već pogodili: stablo rastavljanja i spajanja upravo je stablo sastavljeno od neprekinutih segmenata. No permutacija može imati čak $O(n^2)$ neprekinutih segmenata, pa moramo izdvojiti one osnovnije od kojih ćemo sastaviti stablo.

### Primitivni segmenti

Puni naziv ovog pojma je **primitivni neprekinuti segment**, ali autor smatra da je „primitivni segment” sažetije.

Za permutaciju $P$ primitivni segment $M$ označava neprekinuti segment iz skupa $I_P$ za koji ne postoji neprekinuti segment koji ga siječe, a ne sadrži ga i nije njime sadržan. Formalno, $X\in I_P$ takav da $\forall A\in I_P,\ X\cap A= (P,\varnothing)\vee X\subseteq A\vee A\subseteq X$.

Skup svih primitivnih segmenata označavamo $M_P$. Očito je $(P,\varnothing)\in M_P$.

Očito su primitivni segmenti međusobno ili disjunktni ili u odnosu sadržavanja. Također se može primijetiti da se **svaki neprekinuti segment može sastaviti od nekoliko međusobno disjunktnih primitivnih segmenata**. Najveći primitivni segment cijela je permutacija, koja sadrži sve ostale primitivne segmente, pa primitivni segmenti čine stablastu strukturu koju nazivamo **stablo rastavljanja i spajanja**. Strože rečeno, stablo rastavljanja i spajanja permutacije $P$ sastoji se od **svih primitivnih segmenata** permutacije $P$.

Nakon tolikih suhoparnih definicija nužna je slika. Promotrimo permutaciju $P=\{9,1,10,3,2,5,7,6,8,4\}$. Stablo rastavljanja i spajanja sastavljeno od njezinih primitivnih segmenata izgleda ovako:

![p1](./images/div-com1.png)

Na slici nismo označili same primitivne segmente, ali **svaki čvor predstavlja jedan primitivni segment**. Označen je samo skup vrijednosti svakog primitivnog segmenta. Primjerice, čvor $[5,8]$ predstavlja primitivni segment $(P,[6,9])=\{5,7,6,8\}$. Ostaje pitanje: **što su čvorovi rastavljanja i čvorovi spajanja?**

### Čvorovi rastavljanja i čvorovi spajanja

Dajemo izravno definicije, a o njihovoj ispravnosti raspravljamo poslije.

1.  **Interval vrijednosti**: za čvor $u$ s $[u_l,u_r]$ označavamo njegov interval vrijednosti.
2.  **Niz djece**: za čvor $u$ stabla pretpostavljamo da njegova djeca čine **uređeni** niz čiji su elementi intervali vrijednosti (pojedinačni broj $x$ shvaćamo kao interval $[x,x]$). Taj niz zovemo nizom djece i označavamo $S_u$.
3.  **Permutacija djece**: za niz djece $S_u$ permutacija dobivena diskretizacijom njegovih elemenata u pozitivne cijele brojeve naziva se permutacija djece. Primjerice, čvor $[5,8]$ ima niz djece $\{[5,5],[6,7],[8,8]\}$; ako intervale sortiramo i numeriramo, permutacija djece je $\{1,2,3\}$; slično je permutacija djece čvora $[4,8]$ jednaka $\{2,1\}$. Permutaciju djece čvora $u$ označavamo $P_u$.
4.  **Čvor spajanja**: čvor čija je permutacija djece rastuća ili padajuća nazivamo čvorom spajanja. Formalno, čvor koji zadovoljava $P_u=\{1,2,\cdots,|S_u|\}$ ili $P_u=\{|S_u|,|S_u-1|,\cdots,1\}$ nazivamo čvorom spajanja. **Listovi nemaju permutaciju djece i također ih smatramo čvorovima spajanja**.
5.  **Čvor rastavljanja**: svaki čvor koji nije čvor spajanja čvor je rastavljanja.

Sa slike se vidi da samo $[1,10]$ nije čvor spajanja, jer je permutacija djece čvora $[1,10]$ jednaka $\{3,1,4,2\}$.

### Svojstva čvorova rastavljanja i spajanja

Imena čvorova rastavljanja i spajanja potječu od njihovih svojstava. Prvo imamo vrlo očito svojstvo: za svaki čvor $u$ stabla unija intervala iz njegova niza djece jednaka je intervalu vrijednosti čvora $u$, tj. $\bigcup_{i=1}^{|S_u|}S_u[i]=[u_l,u_r]$.

Za čvor spajanja $u$: svaki **podinterval** njegova niza djece čini **neprekinuti segment**. Formalno, $\forall S_u[l\sim r]$ vrijedi $\bigcup_{i=l}^rS_u[i]\in I_P$.

Za čvor rastavljanja $u$: nijedan podinterval njegova niza djece **duljine veće od 1 (ovdje duljina znači broj elemenata u nizu djece, a ne duljinu intervala indeksa)** **ne** čini **neprekinuti segment**. Formalno, $\forall S_u[l\sim r],l<r$ vrijedi $\bigcup_{i=l}^rS_u[i]\notin I_P$.

Svojstvo čvora spajanja nije teško dokazati. Permutacija djece čvora spajanja ili je rastuća ili padajuća, a intervali vrijednosti nadovezuju se jedan na drugi, pa je svaki neprekinuti podniz (interval) neprekinuti segment.

Svojstvo čvora rastavljanja mnogim je čitateljima manje jasno: zašto **nijedan** podinterval duljine veće od $1$ ne čini neprekinuti segment?

Dokaz kontradikcijom. Pretpostavimo da za čvor $u$ postoji **najdulji** interval $S_u[l\sim r]$ u njegovu nizu djece koji čini neprekinuti segment. Tada je $A=\bigcup_{i=l}^rS_u[i]\in I_P$, što znači da je $A$ primitivni segment! (Budući da je $A$ najdulji takav u nizu djece, ne postoji neprekinuti segment koji ga siječe, a ne sadrži ga.) Dakle, stablo nije izgrađeno od svih primitivnih segmenata. Kontradikcija.

### Izgradnja stabla

Za konkretnu izgradnju stabla LCA je dao linearni algoritam[^ref1]; u nastavku dajemo lakše razumljiv algoritam složenosti $O(n\log n)$.

#### Inkrementalna metoda

Razmotrimo inkrementalnu metodu. Stogom održavamo šumu rastavljanja i spajanja prvih $i-1$ elemenata. Ovdje treba **posebno naglasiti** da šuma rastavljanja i spajanja znači da je u svakom trenutku svaki čvor na stogu ili čvor rastavljanja ili čvor spajanja. Promotrimo sada trenutačni čvor $P_i$.

1.  Najprije provjerimo može li postati dijete čvora na vrhu stoga; ako može, postaje dijete vrha stoga, zatim vrh skidamo sa stoga i on postaje trenutačni čvor. Postupak ponavljamo dok stog ne postane prazan ili čvor ne može postati dijete vrha stoga.
2.  Ako ne može postati dijete vrha stoga, provjerimo može li se nekoliko uzastopnih čvorova s vrha stoga spojiti u jedan čvor (način provjere opisan je poslije); spojeni čvor postaje trenutačni čvor.
3.  Ponavljamo gornji postupak dok je to moguće. Zatim završavamo ovaj korak i trenutačni čvor stavljamo na stog.

Objasnimo to detaljnije.

#### Konkretna strategija

Smatramo da, ako trenutačni čvor može postati dijete vrha stoga, vrh stoga mora biti čvor spajanja. Da je čvor rastavljanja, nakon spajanja taj bi čvor rastavljanja imao neprekinuti podsegment, što krši svojstvo čvora rastavljanja. Dakle, to je sigurno čvor spajanja.

Ako ne može postati dijete vrha stoga, provjeravamo može li se nekoliko uzastopnih čvorova s vrha stoga spojiti s trenutačnim čvorom. Neka je $l$ lijevi kraj intervala trenutačnog čvora. Računamo $L_i$: najveću vrijednost lijevog kraja $< l$ među neprekinutim segmentima čiji je desni kraj indeks $i$. Trenutačni čvor je $P_i$, a vrh stoga označavamo $t$.

1.  Ako $L_i$ ne postoji, trenutačni čvor očito se ne može spojiti.
2.  Ako je $t_l=L_i$, spajaju se dva čvora i rezultat je **čvor spajanja**.
3.  Inače na stogu sigurno postoji čvor $t'$ čiji je lijevi kraj ${t'}_l=L_i$ i tada se čvorovi od trenutačnog do $t'$ sigurno mogu spojiti u **čvor rastavljanja**.

#### Provjera mogućnosti spajanja

Na kraju razmotrimo kako obraditi $L_i$. Neprekinuti segment $(P,[l,r])$ ekvivalentan je tome da je raspon vrijednosti intervala jednak duljini intervala minus 1, tj.

$$
\max_{l\le i\le r}P_i-\min_{l\le i\le r}P_i=r-l
$$

Budući da je P permutacija, za svaki interval $[l,r]$ vrijedi

$$
\max_{l\le i\le r}P_i-\min_{l\le i\le r}P_i\ge r-l
$$

Stoga održavamo $\max_{l\le i\le r}P_i-\min_{l\le i\le r}P_i-(r-l)$, pa je pronalaženje neprekinutog segmenta ekvivalentno upitu za minimum!

S tom idejom lako dolazimo do sljedećeg algoritma. Za trenutačni $i$ u inkrementalnom postupku održavamo niz $Q$ koji predstavlja raspon minus duljina intervala $[j,i]$, tj.

$$
Q_j=\max_{j\le k\le i}P_k-\min_{j\le k\le i}P_k-(i-j),\ \ 0<j<i
$$

Sada želimo znati postoji li među $1\sim i-1$ najmanji $j$ takav da je $Q_j=0$. To je ekvivalentno traženju minimuma $Q_{1\sim i-1}$. Najmanji takav $j$ je $L_i$. Ako ne postoji, $L_i=i$.

No kad $i$-ti korak završi, moramo brzo ažurirati niz $Q$ na stanje za i+1. Interval se mijenja iz $[j,i]$ u $[j,i+1]$; ako je $P_{i+1}>\max$ ili $P_{i+1}<\min$, $Q_j$ se mijenja. Kako? Ako je $P_{i+1}>\max$, od $Q_j$ oduzmemo $\max$ i dodamo $P_{i+1}$ i ažuriranje $Q_j$ je gotovo; za $P_{i+1}<\min$ analogno, $Q_j=Q_j+\min-P_{i+1}$.

A što ako za interval $[x,y]$ intervali $P_{x\sim i},P_{x+1\sim i},P_{x+2\sim i},\cdots,P_{y\sim i}$ imaju isti $\max$? Već ste shvatili: tada radimo intervalno dodavanje; slično, kad $P_{x\sim i},P_{x+1\sim i},\cdots,P_{y\sim i}$ imaju isti $\min$, također je riječ o intervalnom dodavanju. Pritom su ažuriranja $\max$ i $\min$ međusobno neovisna, pa se mogu provoditi zasebno.

Održavanje $Q$ stoga možemo opisati ovako:

1.  Nađemo najveći $j$ takav da je $P_{j}>P_{i+1}$; očito su tada svi brojevi u $P_{j+1\sim i}$ manji od $P_{i+1}$, pa treba ažurirati maksimum za $Q_{j+1\sim i}$. Budući da je $P_{i},\max(P_i,P_{i-1}),\max(P_i,P_{i-1},P_{i-2}),\cdots,\max(P_i,P_{i-1},\cdots,P_{j+1})$ (nestrogo) monotono rastuće, za svaki odsječak s istim $\max$ možemo napraviti isto ažuriranje, tj. intervalno dodavanje.
2.  Ažuriranje $\min$ analogno.
3.  Svaki $Q_j$ umanjimo za $1$, jer se duljina intervala povećala za $1$.
4.  Upit za $L_i$: upit za **indeks** na kojem $Q$ postiže minimum.

Točno tako: $Q$ možemo održavati segment treeom! Ostaje još pitanje: kako pronaći odsječak u kojem su $\max/\min$ isti? Monotonim stogom! Održavamo dva monotona stoga, za $\max$ i za $\min$. Očito su $\max/\min$ intervala čiji su krajevi dva susjedna elementa stoga isti, pa pri održavanju monotonih stogova usput ažuriramo segment tree.

Konkretan način održavanja vidi u kodu.

Nakon toliko suhoparnog teksta vjerojatno ste zbunjeni, pa evo slike. Upozorenje: duga slika!

![p2](./images/div-com2.jpg)

### Implementacija

Na kraju dajemo implementaciju za referencu. Kod je preuzet s [bloga 大米饼](https://www.cnblogs.com/Paul-Guderian/p/11020708.html), uz dodane komentare.

```cpp
#include <algorithm>
#include <cstdio>
using namespace std;
constexpr int N = 200010;

int n, m, a[N], st1[N], st2[N], tp1, tp2, rt;
int L[N], R[N], M[N], id[N], cnt, typ[N], bin[20], st[N], tp;

// izvorni zadatak za ovaj kod je CERC2017 Intrinsic Interval
// niz a je permutacija iz zadatka
// st1 i st2 su dva monotona stoga, tp1 i tp2 njihovi vrhovi, rt je korijen stabla
// nizovi L i R su lijevi i desni kraj čvora stabla, uloga niza M opisana je pri izgradnji stabla
// id pamti indeks čvora koji odgovara položaju u permutaciji, typ označava je li čvor rastavljanja ili spajanja
// st je stog indeksa čvorova stabla, tp njegov vrh
struct RMQ {  // predobrada RMQ (Max & Min)
  int lg[N], mn[N][17], mx[N][17];

  void chkmn(int& x, int y) {
    if (x > y) x = y;
  }

  void chkmx(int& x, int y) {
    if (x < y) x = y;
  }

  void build() {
    for (int i = bin[0] = 1; i < 20; ++i) bin[i] = bin[i - 1] << 1;
    for (int i = 2; i <= n; ++i) lg[i] = lg[i >> 1] + 1;
    for (int i = 1; i <= n; ++i) mn[i][0] = mx[i][0] = a[i];
    for (int i = 1; i < 17; ++i)
      for (int j = 1; j + bin[i] - 1 <= n; ++j)
        mn[j][i] = min(mn[j][i - 1], mn[j + bin[i - 1]][i - 1]),
        mx[j][i] = max(mx[j][i - 1], mx[j + bin[i - 1]][i - 1]);
  }

  int ask_mn(int l, int r) {
    int t = lg[r - l + 1];
    return min(mn[l][t], mn[r - bin[t] + 1][t]);
  }

  int ask_mx(int l, int r) {
    int t = lg[r - l + 1];
    return max(mx[l][t], mx[r - bin[t] + 1][t]);
  }
} D;

// održavanje L_i

struct SEG {  // segment tree
#define ls (k << 1)
#define rs (k << 1 | 1)
  int mn[N << 1], ly[N << 1];  // intervalno dodavanje; intervalni minimum

  void pushup(int k) { mn[k] = min(mn[ls], mn[rs]); }

  void mfy(int k, int v) { mn[k] += v, ly[k] += v; }

  void pushdown(int k) {
    if (ly[k]) mfy(ls, ly[k]), mfy(rs, ly[k]), ly[k] = 0;
  }

  void update(int k, int l, int r, int x, int y, int v) {
    if (l == x && r == y) {
      mfy(k, v);
      return;
    }
    pushdown(k);
    int mid = (l + r) >> 1;
    if (y <= mid)
      update(ls, l, mid, x, y, v);
    else if (x > mid)
      update(rs, mid + 1, r, x, y, v);
    else
      update(ls, l, mid, x, mid, v), update(rs, mid + 1, r, mid + 1, y, v);
    pushup(k);
  }

  int query(int k, int l, int r) {  // upit za položaj nule
    if (l == r) return l;
    pushdown(k);
    int mid = (l + r) >> 1;
    if (!mn[ls])
      return query(ls, l, mid);
    else
      return query(rs, mid + 1, r);
    // ako nula ne postoji, automatski se vraća trenutačno traženi položaj
  }
} T;

int o = 1, hd[N], dep[N], fa[N][18];

struct Edge {
  int v, nt;
} E[N << 1];

void add(int u, int v) {  // dodavanje brida u stablo
  E[o] = Edge{v, hd[u]};
  hd[u] = o++;
}

void dfs(int u) {
  for (int i = 1; bin[i] <= dep[u]; ++i) fa[u][i] = fa[fa[u][i - 1]][i - 1];
  for (int i = hd[u]; i; i = E[i].nt) {
    int v = E[i].v;
    dep[v] = dep[u] + 1;
    fa[v][0] = u;
    dfs(v);
  }
}

int go(int u, int d) {
  for (int i = 0; i < 18 && d; ++i)
    if (bin[i] & d) d ^= bin[i], u = fa[u][i];
  return u;
}

int lca(int u, int v) {
  if (dep[u] < dep[v]) swap(u, v);
  u = go(u, dep[u] - dep[v]);
  if (u == v) return u;
  for (int i = 17; ~i; --i)
    if (fa[u][i] != fa[v][i]) u = fa[u][i], v = fa[v][i];
  return fa[u][0];
}

// provjera je li trenutačni interval neprekinuti segment
bool judge(int l, int r) { return D.ask_mx(l, r) - D.ask_mn(l, r) == r - l; }

// izgradnja stabla
void build() {
  for (int i = 1; i <= n; ++i) {
    // monotoni stog
    // minimum na intervalu [st1[tp1-1]+1,st1[tp1]] jest a[st1[tp1]]
    // sada ga skidamo sa stoga, što znači da previše oduzeti Min treba vratiti.
    // list segment treea na položaju j održava, od j do trenutačnog i,
    // Max{j,i}-Min{j,i}-(i-j)
    // intervalno dodavanje samo je oznaka (tag).
    // svrha monotonog stoga jest pomoći segment treeu pri ažuriranju s i-1 na i.
    // nakon ažuriranja na i dovoljno je upitati globalni minimum da bismo znali postoji li rješenje

    while (tp1 && a[i] <= a[st1[tp1]])  // monotono rastući stog, održava Min
      T.update(1, 1, n, st1[tp1 - 1] + 1, st1[tp1], a[st1[tp1]]), tp1--;
    while (tp2 && a[i] >= a[st2[tp2]])
      T.update(1, 1, n, st2[tp2 - 1] + 1, st2[tp2], -a[st2[tp2]]), tp2--;

    T.update(1, 1, n, st1[tp1] + 1, i, -a[i]);
    st1[++tp1] = i;
    T.update(1, 1, n, st2[tp2] + 1, i, a[i]);
    st2[++tp2] = i;

    id[i] = ++cnt;
    L[cnt] = R[cnt] = i;  // ovdje su L,R lijevi i desni kraj intervala koji odgovara čvoru
    int le = T.query(1, 1, n), now = cnt;
    while (tp && L[st[tp]] >= le) {
      if (typ[st[tp]] && judge(M[st[tp]], i)) {
        // provjera može li postati dijete; ako može, učinimo to
        R[st[tp]] = i, M[st[tp]] = L[now], add(st[tp], now), now = st[tp--];
      } else if (judge(L[st[tp]], i)) {
        typ[++cnt] = 1;  // čvor spajanja uvijek nastaje ovako
        L[cnt] = L[st[tp]], R[cnt] = i, M[cnt] = L[now];
        // niz M pamti lijevi kraj krajnjeg desnog djeteta čvora, za gornju provjeru može li postati dijete
        add(cnt, st[tp--]), add(cnt, now);
        now = cnt;
      } else {
        add(++cnt, now);  // stvaramo novi čvor i dodajemo now kao dijete
        // ako od trenutačnog čvora ne možemo dobiti neprekinuti segment, spajamo
        // sve dok ne nađemo čvor s kojim nastaje neprekinuti segment; takav
        // čvor sigurno postoji.
        do add(cnt, st[tp--]);
        while (tp && !judge(L[st[tp]], i));
        L[cnt] = L[st[tp]], R[cnt] = i, add(cnt, st[tp--]);
        now = cnt;
      }
    }
    st[++tp] = now;  // kraj koraka, trenutačni čvor stavljamo na stog

    T.update(1, 1, n, 1, i, -1);  // desni kraj intervala pomaknuo se za jedno mjesto, pa sve umanjujemo za 1
  }

  rt = st[1];  // čvor koji na kraju ostane na stogu je korijen
}

// razlikujemo je li lca čvor rastavljanja ili spajanja; listove smatramo čvorovima rastavljanja
void query(int l, int r) {
  int x = id[l], y = id[r];
  int z = lca(x, y);
  if (typ[z] & 1)
    l = L[go(x, dep[x] - dep[z] - 1)], r = R[go(y, dep[y] - dep[z] - 1)];
  // čvor spajanja posebno obrađujemo jer on nije nužno najmanji neprekinuti segment koji sadrži l i r;
  // naime, i podintervali intervala čvora spajanja neprekinuti su segmenti, a nama je dovoljan jedan od njih.
  else
    l = L[z], r = R[z];
  printf("%d %d\n", l, r);
}

int main() {
  scanf("%d", &n);
  for (int i = 1; i <= n; ++i) scanf("%d", &a[i]);
  D.build();
  build();
  dfs(rt);
  scanf("%d", &m);
  for (int i = 1; i <= m; ++i) {
    int x, y;
    scanf("%d%d", &x, &y);
    query(x, y);
  }
  return 0;
}

// 20190612
// stablo rastavljanja i spajanja
```

## Literatura i poveznice

[Blog 大米饼 - 【学习笔记】析合树](https://www.cnblogs.com/Paul-Guderian/p/11020708.html)

[^ref1]: 刘承奥. 简单的连续段数据结构. WC2019 营员交流.
