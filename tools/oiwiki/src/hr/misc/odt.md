---
title: Chtholly stablo / amortizirani segmenti boja
---

## Uvod

Chtholly stablo (Chtholly Tree), poznato i kao stablo starog vozača, ODT (Old Driver Tree). Potječe iz zadatka [CF896C](https://codeforces.com/problemset/problem/896/C).

Taj naziv označava tehniku „održavanja segmenata boja amortizirano pomoću balansiranog stabla (`std::set`, `std::map` itd.) ili vezane liste (`std::list`, ručno napisana lista itd.)”, a ne neku određenu strukturu podataka. Njezina je osnovna ideja spojiti interval jednakih vrijednosti u jedan čvor i obrađivati ga kao cjelinu. U usporedbi s tradicionalnim strukturama podataka poput segment treea, kod zadataka s operacijama prekrivanja intervala Chtholly stablo može mnogo jednostavnije održavati vrijednost svakog prekrivenog intervala.

## Implementacija (std::set)

### Tip čvora

```cpp
struct Node_t {
  int l, r;
  mutable int v;

  Node_t(const int &il, const int &ir, const int &iv) : l(il), r(ir), v(iv) {}

  bool operator<(const Node_t &o) const { return l < o.l; }
};
```

Pri tome je `int v` dodatni podatak koji sami određujete.

???+ note "Što znači ključna riječ `mutable`?"
    `mutable` znači „promjenjiv” i omogućuje nam da u kasnijim operacijama mijenjamo vrijednost `v`. U C++-u `mutable` služi za zaobilaženje ograničenja koja nameće `const`. Varijabla označena s `mutable` (`mutable` se smije primijeniti samo na nestatičke podatkovne članove klase) uvijek je u promjenjivom stanju, čak i unutar `const` funkcije.
    
    To znači da možemo izravno mijenjati vrijednost `v` elementa koji je već umetnut u `set`, a da ga ne moramo izvaditi i ponovno umetnuti u `set`.

### Pohrana čvorova

Želimo održavati sve čvorove tako da lijevi krajevi intervala koje ti čvorovi predstavljaju rastu monotono i da su intervali u parovima disjunktni; najbolje je ako možemo jamčiti da je unija svih intervala jedan maksimalan neprekinut raspon. Ovdje za primjer uzimamo `std::set` i sve čvorove održavamo u jednom `set<Node_t> odt;`.

Pri inicijalizaciji u Chtholly stablo umetnemo jedan vrlo dugačak interval (npr. ako zadatak traži održavanje podataka za pozicije od $1$ do $n$, umetnemo interval $[1,n+1]$).

### Operacija split

Operacija `split` srž je Chtholly stabla. Prima poziciju $x$, interval koji izvorno sadrži točku $x$ (označimo ga $[l, r]$) razdvaja na dva intervala $[l, x)$ i $[x, r]$ te vraća iterator na potonji.

Referentni kôd je sljedeći:

```cpp
auto split(int x) {
  auto it = odt.lower_bound(Node_t(x, 0, 0));
  if (it != odt.end() && it->l == x) return it;
  --it;
  int l = it->l, r = it->r, v = it->v;
  odt.erase(it);
  odt.insert(Node_t(l, x - 1, v));
  return odt.insert(Node_t(x, r, v)).first;
}
```

Na prevoditeljima koji ne podržavaju izvođenje tipa povratne vrijednosti pomoću `auto`, tip povratne vrijednosti funkcije može se promijeniti u `set<Node_t>::iterator`.

### Operacija assign

Druga je važna operacija `assign`. Služi za pridruživanje vrijednosti cijelom intervalu. Neka intervalu $[l,r]$ treba pridružiti vrijednost $v$.

Najprije izrežemo interval $[l, r]$. Redom pozovemo `split(r + 1), split(l)`; iteratore koje oni vraćaju označimo $itr, itl$. Tada raspon iteratora $[itl, itr)$ pokazuje na sve intervale Chtholly stabla sadržane u $[l,r]$.

Zatim izbrišemo stare podatke. `std::set` ima metodu `erase` s potpisom `iterator erase( const_iterator first, const_iterator last );`, koja uklanja elemente iz raspona `[first; last)`. Stoga pozovemo `odt.erase(itl, itr);` da izbrišemo stare podatke.

Na kraju umetnemo novu vrijednost intervala $[l,r]$. Dovoljno je pozvati `odt.insert(Node_t(l, r, v))`.

Referentni kôd je sljedeći:

```cpp
void assign(int l, int r, int v) {
  auto itr = split(r + 1), itl = split(l);
  odt.erase(itl, itr);
  odt.insert(Node_t(l, r, v));
}
```

???+ note "Zašto treba najprije `split(r + 1)`, a tek onda `split(l)`?"
    1.  Metoda `std::set::erase` poništava reference i iteratore koji pokazuju na izbrisane elemente. Ostale reference i iteratori ostaju valjani.
    2.  Metoda `std::set::insert` ne poništava nijedan iterator ni referencu.
    3.  Operacija `split` razdvaja interval. Nakon poziva `split(r + 1)` $r + 1$ postaje lijevi kraj desnog od dvaju novih intervala; kad zatim razdvajamo lijevi interval, sigurno nećemo pristupiti intervalu čiji je lijevi kraj $r + 1$, pa ga nećemo ni razdvojiti, ni izbrisati interval s lijevim krajem $r + 1$, ni poništiti iterator. Obrnuto, ako najprije pozovemo `split(l)`, a zatim `split(r + 1)`, mogli bismo izbrisati interval čiji je lijevi kraj $l$ i time poništiti iterator.

### Operacija perform

Izdvajamo interval Chtholly stabla i izvršavamo operacije na njemu. Slično operaciji `assign`, samo što umjesto brisanja intervala prolazimo kroz njih.

Referentni kôd je sljedeći:

```cpp
void perform(int l, int r) {
  auto itr = split(r + 1), itl = split(l);
  for (; itl != itr; ++itl) {
    // Perform Operations here
  }
}
```

Pazite da takvo izdvajanje ne zloupotrebljavate, jer vremenska složenost može postati pogrešna. Vidi odjeljak „Analiza složenosti” u nastavku.

## Implementacija (std::map)

U usporedbi s implementacijom pomoću `std::set`, u implementaciji pomoću `std::map` operacija `split` piše se jednostavnije. Osim toga, ostale se operacije ne razlikuju od onih sa `std::set`.

### Pohrana čvorova

Budući da su intervali pohranjeni u Chtholly stablu uzastopni, ne moramo nužno pamtiti desni kraj. Možemo sve intervale pohraniti u `map<int, int> mp;`, čiji ključ čuva lijevi kraj, a vrijednost čuva vrijednost od tog lijevog kraja do mjesta ispred sljedećeg lijevog kraja.

Pri inicijalizaciji, ako zadatak traži održavanje podataka za pozicije od $1$ do $n$, pozovemo `mp[1] = -1, mp[n + 1] = -1`, što znači da cijeli $[1,n+1)$, tj. $[1, n]$, postavljamo na posebnu vrijednost $-1$; interval $[n+1, +\infty)$ služi kao stražar (sentinel), a može se i inicijalizirati.

### Operacija split

Referentni kôd (prva inačica):

```cpp
void split(int x) {
  auto it = prev(mp.upper_bound(x));  // nalazimo interval čiji je lijevi kraj manji ili jednak x.
  mp[x] = it->second;  // stvaramo novi interval i u njega kopiramo vrijednost prethodnog intervala.
}
```

Referentni kôd (druga inačica):

```cpp
auto split(int pos) {
  auto it = prev(mp.upper_bound(pos));  // nalazimo interval čiji je lijevi kraj manji ili jednak x.
  return mp.insert(it, make_pair(pos, it->second));
  // stvaramo novi interval i u njega kopiramo vrijednost prethodnog intervala.
}
```

Ovdje je upotrijebljeno preopterećenje `iterator insert( const_iterator pos, const value_type& value );` metode `std::map::insert`, koje umeće `value` što je moguće bliže mjestu neposredno ispred `pos`. Ako se umetanje dogodi upravo na mjestu neposredno ispred `pos`, složenost je amortizirano konstantna; inače je logaritamska u veličini spremnika.

### Operacija assign

Za operaciju `assign` moramo izbrisati lijeve krajeve svih intervala unutar $[l,r−1]$ i zatim stvoriti novi interval.

```cpp
void assign(int l, int r, int v) {  // pozor: ovdje je r desni kraj intervala + 1
  split(l);
  split(r);
  auto it = mp.find(l);
  while (it->first != r) {
    it = mp.erase(it);
  }
  mp[l] = v;
}
```

### Operacija perform

```cpp
void perform(int l, int r) {  // pozor: ovdje je r desni kraj intervala + 1
  split(l);
  split(r);
  auto it = mp.find(l);
  while (it->first != r) {
    // Perform Operations here
    it = next(it);
  }
}
```

## Implementacija (vezana lista)

Trenutačno prevladava implementacija koja čvorove održava pomoću `set`, ali budući da je prosječan broj održavanih intervala vrlo malen, prednost `set`-a nije izražena. Nasuprot tome, vezana lista (ili niz) može sažetije održavati operacije razdvajanja i spajanja.

### Pohrana čvorova

```cpp
using i64 = int64_t;

struct Block {
  Block *next;  // sljedeći čvor liste
  int l, r;     // raspon intervala
  i64 val;      // vrijednost na intervalu

  Block(Block *next, int l, int r, i64 val)
      : next(next), l(l), r(r), val(val) {}

  bool operator<(const Block &b) const { return val < b.val; }
} *root;
```

### Operacija split

```cpp
// vraća interval čiji je lijevi kraj mid+1
Block *split(int mid) {
  for (Block *b = root; b; b = b->next) {  // prolazimo listom
    if (b->l == mid + 1) {                 // lijevi kraj je mid+1
      return b;
    }
    // tražimo interval [l, r] koji sadrži i mid i mid+1 te ga razdvajamo na [l, mid] i [mid+1,
    // r]
    if (b->l <= mid && mid + 1 <= b->r) {
      b->next = new Block(b->next, mid + 1, b->r, b->val);
      b->r = mid;
      return b->next;
    }
  }
  return nullptr;  // nije pronađen, vraćamo nullptr
}
```

Budući da pri radu s intervalima ne možemo održavati samo dio intervala, prije svake od sljedećih operacija treba unaprijed razdvojiti intervale, a tek onda obaviti odgovarajuću operaciju.

```cpp
Block *lb, *rb;

// prethodno razdvajanje, jamči da se daljnje operacije odvijaju unutar [l, r]
void prepare(int l, int r) {
  lb = split(l - 1);
  rb = split(r);
}
```

### Operacija assign

```cpp
void assign(int l, int r, i64 val) {
  prepare(l, r);
  lb->r = r;  // interval [lb.l, lb.r] mijenjamo u [lb.l, r]
  lb->val = val;
  lb->next = rb;  // [lb.l, r] povezujemo s njemu desnim susjednim intervalom
}

// napomena: ovdje se ne oslobađa memorija izbrisanih čvorova; po potrebi to dodajte sami
```

### Operacija perform

```cpp
void perform(int l, int r) {
  prepare(l, r);
  for (Block *b = lb; b != rb; b = b->next) {
    // Perform Operations here
  }
}
```

## Analiza složenosti

### Poziv assign na istom intervalu odmah nakon perform

U tom slučaju uočavamo da dvije operacije `split` dodaju najviše dva intervala; jedan `assign` briše sve intervale u rasponu i dodaje jedan interval, pri čemu prolazi kroz izbrisane intervale. Dakle, broj intervala kroz koje prolazimo linearan je u broju izbrisanih intervala, a svaka operacija dodaje samo $O(1)$ intervala, pa je broj intervala s kojima radimo linearan u broju operacija (uključujući inicijalizaciju); vremenska je složenost amortizirano $O(m\log n)$, gdje je $m$ broj operacija, a $n$ najveći broj intervala u Chtholly stablu (možemo uzeti $n\leq m$).

### Bez assign nakon perform

Ako su dopušteni posebno konstruirani testni podaci, to se sigurno može srušiti: dovoljno je da u Chtholly stablu bude dovoljno mnogo različitih intervala i da se kroz njih uzastopno prolazi, pa složenost Chtholly stabla doseže kvadratnu razinu ili je čak premašuje.

Da bi složenost bila ispravna, podaci moraju biti slučajni. Detalje vidi u [dokazu složenosti Chtholly stabla na Codeforcesu](http://codeforces.com/blog/entry/56135?#comment-398940). Detaljniji strogi dokaz nalazi se u [珂朵莉树的复杂度分析 (Analiza složenosti Chtholly stabla)](https://zhuanlan.zhihu.com/p/102786071). Zaključak dokaza: složenost Chtholly stabla implementiranog pomoću `std::set` iznosi $O(n \log \log n)$, a implementiranog pomoću vezane liste $O(n \log n)$.

## Zadaci za vježbu

-   [「Luogu 1840」Color the Axis](https://www.luogu.com.cn/problem/P1840)
-   ~~[「SCOI2010」序列操作 (Operacije na nizu)](https://www.luogu.com.cn/problem/P2572)~~ (izvoru tog zadatka dodani su hack-podaci)
-   [「SHOI2015」脑洞治疗仪 (Uređaj za liječenje rupa u mozgu)](https://loj.ac/problem/2037)
-   [「Luogu 4979」矿洞：坍塌 (Rudnik: urušavanje)](https://www.luogu.com.cn/problem/P4979)
-   [「Luogu 8146」risrqnis](https://www.luogu.com.cn/problem/P8146)

## Dodatna literatura

[ODT 的映射思想的推广 (Poopćenje ideje preslikavanja u ODT-u) - Luogu članci (luogu.com.cn)](https://www.luogu.com.cn/article/0mys9qkh)

## Literatura i napomene

-   [Problem - 896C - Codeforces](https://codeforces.com/problemset/problem/896/C) (podrijetlo Chtholly stabla)
-   [CF896C Willem, Chtholly and Seniorious 题解 (rješenje) - Luogu članci (luogu.com.cn)](https://www.luogu.com.cn/article/gyxbe23s) (referenca za implementaciju pomoću `std::set`)
-   [珂朵莉树的 map 实现 (Implementacija Chtholly stabla pomoću map) - Zhihu (zhihu.com)](https://zhuanlan.zhihu.com/p/469794466) (referenca za implementaciju pomoću `std::map`)
-   [题解 CF896C【Willem, Chtholly and Seniorious】(rješenje CF896C) - Luogu članci (luogu.com.cn)](https://www.luogu.com.cn/article/umiw1fwp) (referenca za implementaciju pomoću vezane liste)
-   [Codeforces Round #449 Editorial - Codeforces](https://codeforces.com/blog/entry/56135?#comment-398940) (o dokazu složenosti Chtholly stabla)
-   [珂朵莉树的复杂度分析 (Analiza složenosti Chtholly stabla) - Zhihu (zhihu.com)](https://zhuanlan.zhihu.com/p/102786071) (analiza složenosti Chtholly stabla)
