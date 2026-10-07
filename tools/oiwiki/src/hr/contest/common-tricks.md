---
title: Mali trikovi
---

Ova stranica navodi nekoliko malih trikova korisnih na natjecanjima.

## Iskoristi lokalnost

Lokalnost znači da program teži pristupati podacima koji su blizu nedavno korištenih podataka ili samim nedavno korištenim podacima. Dijeli se na vremensku i prostornu lokalnost.

Više u odjeljcima [Odmatanje petlji (Loop Unroll)](../lang/optimizations.md#循环展开-loop-unroll), [Optimizacija rasporeda koda (Code Layout Optimizations)](../lang/optimizations.md#代码布局优化-code-layout-optimizations) i dr.

## Makro za petlje

Sljedeći se kod može skratiti makroom:

```cpp
for (int i = 0; i < N; i++) {
  // tijelo petlje izostavljeno
}

// Skraćivanje makroom
#define f(x, y, z) for (int x = (y), __ = (z); x < __; ++x)

// Petlja se tada piše kao `f(i, 0, N)`. Primjer:
// a is a STL container
f(i, 0, a.size()) { ... }
```

Još jedan koristan makro:

```cpp
#define _rep(i, a, b) for (int i = (a); i <= (b); ++i)
```

## Koristi namespace

Uporaba namespacea čini program čitljivijim i lakšim za otklanjanje grešaka.

??? note "Primjer: NOI 2018 屠龙勇士"
    ```cpp
    // NOI 2018 屠龙勇士 – kod za 40 % djelomičnih bodova
    #include <algorithm>
    #include <cmath>
    #include <cstring>
    #include <iostream>
    using namespace std;
    long long n, m, a[100005], p[100005], aw[100005], atk[100005];
    
    namespace one_game {
    // u namespaceu se mogu deklarirati i varijable
    void solve() {
      for (int y = 0;; y++)
        if ((a[1] + p[1] * y) % atk[1] == 0) {
          cout << (a[1] + p[1] * y) / atk[1] << endl;
          return;
        }
    }
    }  // namespace one_game
    
    namespace p_1 {
    void solve() {
      if (atk[1] == 1) {  // solve 1-2
        sort(a + 1, a + n + 1);
        cout << a[n] << endl;
        return;
      } else if (m == 1) {  // solve 3-4
        long long k = atk[1], kt = ceil(a[1] * 1.0 / k);
        for (int i = 2; i <= n; i++)
          k = aw[i - 1], kt = max(kt, (long long)ceil(a[i] * 1.0 / k));
        cout << k << endl;
      }
    }
    }  // namespace p_1
    
    int main() {
      int T;
      cin >> T;
      while (T--) {
        memset(a, 0, sizeof(a));
        memset(p, 0, sizeof(p));
        memset(aw, 0, sizeof(aw));
        memset(atk, 0, sizeof(atk));
        cin >> n >> m;
        for (int i = 1; i <= n; i++) cin >> a[i];
        for (int i = 1; i <= n; i++) cin >> p[i];
        for (int i = 1; i <= n; i++) cin >> aw[i];
        for (int i = 1; i <= m; i++) cin >> atk[i];
        if (n == 1 && m == 1)
          one_game::solve();  // solve 8-13
        else if (p[1] == 1)
          p_1::solve();  // solve 1-4 or 14-15
        else
          cout << -1 << endl;
      }
      return 0;
    }
    ```

## Debugiranje makroima

Pri lokalnom testiranju programer često dodaje ispise za debugiranje. Pri slanju na OJ sve ih treba ukloniti da ne utječu na ocjenjivanje izlaza, što oduzima vrijeme. Tu vrijeme štedi definiranje makroa. Okvirna struktura programa:

```cpp
#define DEBUG
#ifdef DEBUG
// do something when DEBUG is defined
#endif
// or
#ifndef DEBUG
// do something when DEBUG isn't defined
#endif
```

`#ifdef` provjerava je li u programu `#define`-om definiran odgovarajući identifikator; ako jest, izvršava se kod koji slijedi. `#ifndef` izvršava kod koji slijedi ako identifikator nije definiran.

Tako je dovoljno u `#ifdef DEBUG` napisati kod za debugiranje, a u `#ifndef DEBUG` pravi kod za slanje, pa je lokalno testiranje jednostavno. Pri slanju samo zakomentiramo redak `#define DEBUG`. Identifikator se može i ne definirati u programu, nego pri prevođenju opcijom `-DDEBUG`; tada pri slanju program uopće ne treba mijenjati.

Mnogi OJ-evi prevode s opcijom `-DONLINE_JUDGE`; pametno korištenje te značajke štedi puno vremena.

## Stress testiranje (对拍)

Stress testiranje je način provjere ili debugiranja u kojem se ispravnost programa provjerava usporedbom izlaza dvaju programa. Izlaz vlastitog programa usporedimo s izlazom drugog programa i tako zaključimo je li naš program ispravan.

Postupak se ponavlja mnogo puta, pa ga treba automatizirati skriptom.

Konkretno, potrebni su [generator podataka](../tools/testlib/generator.md) i dva programa čije izlaze uspoređujemo.

Pri svakom pokretanju generator zapisuje podatke u ulaznu datoteku; preusmjeravanjem oba programa čitaju te podatke i pišu izlaz u zadane datoteke; na kraju se datoteke uspoređuju naredbom `fc` na Windowsu (`diff` na Linuxu). Ako se otkrije greška, upravo generirani podaci odmah služe za debugiranje.

Okvirni program za stress testiranje:

```cpp
#include <cstdio>
#include <cstdlib>

int main() {
  // For Windows
  // pri stress testiranju ne koristi datotečni ulaz/izlaz
  // naravno, ovaj se program može napisati i kao batch skripta
  while (true) {
    system("gen > test.in");  // generator zapisuje podatke u ulaznu datoteku
    system("test1.exe < test.in > a.out");  // izlaz programa 1
    system("test2.exe < test.in > b.out");  // izlaz programa 2
    if (system("fc a.out b.out")) {
      // ovaj redak uspoređuje izlaze
      // fc vraća 0 ako su izlazi jednaki, inače postoji razlika
      system("pause");  // da se razlike mogu pogledati
      return 0;
      // ulazni podaci su u datoteci test.in i mogu se izravno koristiti za debugiranje
    }
  }
}
```

## Memory pool

Pri dinamičkoj alokaciji često pozivanje `new`/`malloc` troši puno vremena i prostora, a može i fragmentirati memoriju i tako smanjiti performanse, pa inače ispravan program dobije TLE/MLE.

Tada pomaže tehnika „memory pool”: prije stvarne uporabe unaprijed alociramo memoriju određene veličine kao rezervu, a pri dinamičkoj alokaciji samo uzmemo blok iz rezerve.

U većini OI zadataka najveća potrebna memorija može se izračunati unaprijed i alocirati odjednom.

Primjer:

```cpp
// dinamička alokacija niza 32-bitnih cijelih brojeva s predznakom:
int* newarr(int sz) {
  static int pool[MAXN], *allocp = pool;
  return allocp += sz, allocp - sz;
}

// dinamičko stvaranje čvorova segmentnog stabla:
Node* newnode() {
  static Node pool[MAXN << 1], *allocp = pool - 1;
  return ++allocp;
}
```

## Literatura

[洛谷日报 #86 (kineski)](https://studyingfather.blog.luogu.org/some-coding-tips-for-oiers)

《算法竞赛入门经典 习题与解答》
