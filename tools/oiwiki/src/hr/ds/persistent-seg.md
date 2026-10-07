---
title: Perzistentni segment tree
---

## Chairman tree

Puni naziv strukture chairman tree jest perzistentni segment tree nad vrijednostima; vidi [raspravu na Zhihuu](https://www.zhihu.com/question/59195374).

???+ warning "O funkcijskom segment treeju"
    **Funkcijski segment tree** jest segment tree koji koristi ideje funkcijskog programiranja. U funkcijskom programiranju računalni se izračuni promatraju kao matematičke funkcije i izbjegavaju se promjenjiva stanja i varijable. Lako je uočiti da je funkcijski segment tree [potpuno perzistentan](persistent.md#potpuna-perzistentnost-fully-persistent).

## Uvodni problem

Počnimo zadatkom: zadan je niz $a$ od $n$ cijelih brojeva. Za zadani zatvoreni interval $[l, r]$ treba pronaći $k$-tu najmanju vrijednost u tom intervalu.

Kako biste to riješili?

Jedno je moguće rješenje chairman tree.
Glavna je ideja chairman treeja sačuvati prethodne verzije pri svakom umetanju kako bismo mogli tražiti $k$-tu najmanju vrijednost u intervalu.

Kako ih sačuvati? Najjednostavnije, grubom silom: svaki put stvorimo novi segment tree.  
Ali zar time nećemo potrošiti previše memorije?

## Objašnjenje

Analizom primjećujemo da svaka izmjena mijenja isti broj čvorova.  
(Primjerice, na donjoj slici mijenjamo čvor za vrijednost 1 u intervalu $[1,8]$; crveni čvorovi označavaju promijenjene čvorove.)  
![](./images/persistent-seg.png)

Mijenja se samo $O(\log{n})$ čvorova koji tvore jedan lanac, odnosno broj promijenjenih čvorova pri svakoj izmjeni jednak je visini stabla.  
Chairman tree ne može koristiti pohranu poput hrpe: lijevo i desno dijete ne možemo označavati s $x\times 2$ i $x\times 2+1$. Umjesto toga čvorove treba stvarati dinamički te za svaki čuvati indekse lijevog i desnog djeteta.  
Zato, osim lijevog i desnog djeteta, trebamo sačuvati samo korijen nakon umetanja svakog broja kako bismo dobili perzistentnost.

Pojednostavimo problem: svaki put tražimo $k$-tu najmanju vrijednost u intervalu $[1,r]$.  
Kako to učiniti? Pronađemo verziju korijena pri umetanju r, a zatim postupimo kao u običnom segment treeju nad vrijednostima (koji se naziva i segment tree nad ključevima ili domenom vrijednosti).

To je vjerojatno jasno, pa se vratimo izvornom problemu: traženju $k$-te najmanje vrijednosti u intervalu $[l,r]$.  
Povežimo to s još jednim pojmom: **prefiksnim sumama**.  
One vješto koriste svojstvo oduzimanja intervala kako bi nakon prethodne obrade odgovarale na svaki upit u $O(1)$.

Primjećujemo da i podaci koje čuva chairman tree zadovoljavaju to svojstvo.  
Stoga, ako trebamo podatke za $[l,r]$, dovoljno je od podataka za $[1,r]$ oduzeti podatke za $[1,l - 1]$.

Time je problem riješen!

Analizirajmo memoriju: zbog dinamičkog stvaranja čvorova jedan segment tree sadrži samo $2n-1$ čvorova.  
Zatim izvodimo $n$ izmjena, od kojih svaka dodaje najviše $\lceil\log_2{n}\rceil+1$ čvorova. Zato u najgorem slučaju nakon $n$ izmjena ukupan broj čvorova doseže $2n-1+n(\lceil\log_2{n}\rceil+1)$.
U ovom je zadatku $n \leq 10^5$, pa jedna izmjena dodaje najviše $\lceil\log_2{10^5}\rceil+1 = 18$ čvorova. Nakon $n$ izmjena ukupno ih je $2\times 10^5-1+18\times 10^5$; zanemarimo li $-1$, to je približno $20\times 10^5$.

Za kraj savjet: nemojte pretjerano štedjeti memoriju (u većini zadataka memorijsko je ograničenje dovoljno veliko pa se obično ne morate bojati prekoračenja)! Slobodno rezervirajte $2^5\times 10^5$, gotovo dvostruko više od prvotne procjene (odnosno `n << 5`).

## Implementacija

```cpp
#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;
constexpr int MAXN = 1e5;  // Raspon ulaznih podataka
int tot, n, m;
int sum[(MAXN << 5) + 10], rt[MAXN + 10], ls[(MAXN << 5) + 10],
    rs[(MAXN << 5) + 10];
int a[MAXN + 10], ind[MAXN + 10], len;

int getid(const int &val) {  // Kompresija koordinata
  return lower_bound(ind + 1, ind + len + 1, val) - ind;
}

int build(int l, int r) {  // Izgradi stablo
  int root = ++tot;
  if (l == r) return root;
  int mid = l + r >> 1;
  ls[root] = build(l, mid);
  rs[root] = build(mid + 1, r);
  return root;  // Vrati korijen ovog podstabla
}

int update(int k, int l, int r, int root) {  // Operacija umetanja
  int dir = ++tot;
  ls[dir] = ls[root], rs[dir] = rs[root], sum[dir] = sum[root] + 1;
  if (l == r) return dir;
  int mid = l + r >> 1;
  if (k <= mid)
    ls[dir] = update(k, l, mid, ls[dir]);
  else
    rs[dir] = update(k, mid + 1, r, rs[dir]);
  return dir;
}

int query(int u, int v, int l, int r, int k) {  // Operacija upita
  int mid = l + r >> 1,
      x = sum[ls[v]] - sum[ls[u]];  // Oduzimanjem intervala dobij broj vrijednosti u lijevom djetetu
  if (l == r) return l;
  if (k <= x)  // Ako je k manji ili jednak x, k-ti najmanji broj nalazi se u lijevom djetetu
    return query(ls[u], ls[v], l, mid, k);
  else  // Inače se nalazi u desnom djetetu
    return query(rs[u], rs[v], mid + 1, r, k - x);
}

void init() {
  scanf("%d%d", &n, &m);
  for (int i = 1; i <= n; ++i) scanf("%d", a + i);
  memcpy(ind, a, sizeof ind);
  sort(ind + 1, ind + n + 1);
  len = unique(ind + 1, ind + n + 1) - ind - 1;
  rt[0] = build(1, len);
  for (int i = 1; i <= n; ++i) rt[i] = update(getid(a[i]), 1, len, rt[i - 1]);
}

int l, r, k;

void work() {
  while (m--) {
    scanf("%d%d%d", &l, &r, &k);
    printf("%d\n", ind[query(rt[l - 1], rt[r], 1, len, k)]);  // Odgovori na upit
  }
}

int main() {
  init();
  work();
  return 0;
}
```

## Proširenje: perzistentni DSU pomoću chairman treeja

Chairman tree praktičan je način implementacije perzistentnog DSU-a. Ovdje je i primjer takve implementacije.

```cpp
--8<-- "docs/ds/code/persistent-seg/persistent-seg_1.cpp"
```

## Literatura

<https://en.wikipedia.org/wiki/Persistent_data_structure>

<https://www.cnblogs.com/zinthos/p/3899565.html>
