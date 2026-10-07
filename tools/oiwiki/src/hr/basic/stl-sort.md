---
title: Sortiranje u standardnoj biblioteci
---

Ova stranica kratko predstavlja algoritme sortiranja implementirane u standardnim bibliotekama C-a i C++-a.

Osim gdje je navedeno drugačije, funkcije na ovoj stranici definirane su u zaglavlju `<algorithm>`.

## qsort

Vidi: [`qsort`](https://en.cppreference.com/w/c/algorithm/qsort), [`std::qsort`](https://en.cppreference.com/w/cpp/algorithm/qsort)

Ova je funkcija opća funkcija za sortiranje nizova u standardnoj biblioteci C-a; konkretan algoritam određuje implementacija biblioteke. Definirana je u `<stdlib.h>`, a u standardnoj biblioteci C++-a u `<cstdlib>`.

???+ warning "Napomena[^note2]"
    Iako se funkcija zove `qsort`, ni C ni POSIX standard ne zahtijevaju da koristi [quick sort](./quick-sort.md), niti jamče bilo kakvu složenost ili stabilnost.

### Funkcija usporedbe za qsort i bsearch

Funkcija qsort ima četiri parametra: ime niza, broj elemenata, veličinu elementa i pravilo usporedbe. Pravilo usporedbe zadaje se funkcijom usporedbe; različite funkcije usporedbe daju različite redoslijede sortiranja.

Funkcija usporedbe mora imati dva parametra tipa `const void *`. Vraća pozitivan broj, negativan broj ili 0.

Primjer funkcije usporedbe:

```c
int compare(const void* p1, const void* p2)  // funkcija usporedbe za niz tipa int
{
  int* a = (int*)p1;
  int* b = (int*)p2;
  if (*a > *b)
    return 1;  // pozitivan broj znači da je a veći od b
  else if (*a < *b)
    return -1;  // negativan broj znači da je a manji od b
  else
    return 0;  // 0 znači da su a i b ekvivalentni
}
```

Napomena: vraćanje razlike dvaju elemenata umjesto pozitivnog/negativnog broja tipična je pogreška, jer može dovesti do prekoračenja (overflow).

Primjer sortiranja struktura:

```c
struct eg  // primjer strukture
{
  int e;
  int g;
};

// funkcija usporedbe za niz tipa struct eg: sortiranje po članu e
int compare(const void* p1, const void* p2) {
  struct eg* a = (struct eg*)p1;
  struct eg* b = (struct eg*)p2;
  if (a->e > b->e)
    return 1;  // pozitivan broj znači da je a veći od b
  else if (a->e < b->e)
    return -1;  // negativan broj znači da je a manji od b
  else
    return 0;  // 0 znači da su a i b ekvivalentni
}
```

Ovdje se vidi i da ekvivalentnost ne znači jednakost, nego samo da su dva elementa ekvivalentna prema ovom pravilu usporedbe.

## std::sort

Vidi: [`std::sort`](https://en.cppreference.com/w/cpp/algorithm/sort)

Uporaba:

```cpp
// a[0] .. a[n - 1] je niz koji treba sortirati
// sortira a u mjestu, uzlazno
std::sort(a, a + n);

// cmp je vlastita funkcija usporedbe
std::sort(a, a + n, cmp);
```

Napomena: funkcija usporedbe za sort vraća `true` ili `false`, čime izražava odnos (redoslijed) dvaju elemenata; to je potpuno drugačija semantika od trovrijednosne funkcije usporedbe za qsort. Detalji su u gore navedenoj dokumentaciji za sort.

Ako `cmp` definira strogi slabi uređaj, pri pretvorbi u trovrijednosno pravilo za `qsort` treba vratiti `cmp(a,b) ? -1 : cmp(b,a) ? 1 : 0`; za ekvivalentne elemente mora se vratiti nula.

`std::sort` češće je korištena funkcija sortiranja u C++ biblioteci. Posljednji joj je parametar binarna funkcija usporedbe; ako `cmp` nije zadan, sortira uzlazno.

Stariji C++ standardi zahtijevali su samo **prosječnu** vremensku složenost $O(n\log n)$. C++11 i kasniji standardi zahtijevaju **najgoru** vremensku složenost $O(n\log n)$.

C++ standard ne propisuje algoritam; konkretna implementacija ovisi o standardnoj biblioteci. Primjerice, implementacije u [libstdc++ 14.2.0](https://github.com/gcc-mirror/gcc/blob/releases/gcc-14.2.0/libstdc%2B%2B-v3/include/bits/stl_algo.h#L1876-L1908) i [libc++ 20.1.8](https://github.com/llvm/llvm-project/blob/llvmorg-20.1.8/libcxx/include/__algorithm/sort.h#L709-L727) koriste [introsort](./quick-sort.md#introsort).

## std::nth\_element

Vidi: [`std::nth_element`](https://en.cppreference.com/w/cpp/algorithm/nth_element)

Uporaba:

```cpp
std::nth_element(first, nth, last);
std::nth_element(first, nth, last, cmp);
```

Preslaguje elemente u `[first, last)` tako da element na koji pokazuje `nth` postane onaj koji bi se na tom mjestu nalazio nakon sortiranja `[first, last)`. Svi elementi ispred novog `nth` elementa manji su ili jednaki svim elementima iza njega.

Konkretnu implementaciju određuje standardna biblioteka; uobičajene implementacije koriste [quickselect](https://en.wikipedia.org/wiki/Quickselect) ili [introselect](https://en.wikipedia.org/wiki/Introselect), koji nakon svakog particioniranja nastavljaju samo na strani koja sadrži ciljno mjesto.

Za oba oblika C++ standard zahtijeva prosječnu vremensku složenost $O(n)$, gdje je n jednako `std::distance(first, last)`.

Često se koristi pri izgradnji [k-d stabla](../ds/kdt.md).

## std::stable\_sort

Vidi: [`std::stable_sort`](https://en.cppreference.com/w/cpp/algorithm/stable_sort)

Uporaba:

```cpp
std::stable_sort(first, last);
std::stable_sort(first, last, cmp);
```

Stabilno sortiranje: jamči da jednaki elementi nakon sortiranja zadržavaju međusobni redoslijed iz izvornog niza.

Vremenska složenost je $O(n\log^2 n)$, a ako je dostupna dodatna memorija, $O(n\log n)$.

## std::partial\_sort

Vidi: [`std::partial_sort`](https://en.cppreference.com/w/cpp/algorithm/partial_sort)

Uporaba:

```cpp
// mid = first + k
std::partial_sort(first, mid, last);
std::partial_sort(first, mid, last, cmp);
```

Iz `[first,last)` izabere `k` elemenata koji su po `cmp` najmanji, sortira ih i smjesti u `[first,mid)`; redoslijed ostatka nije zajamčen. Ako `cmp` nije zadan, sortira uzlazno.

Složenost: približno $(\textit{last}-\textit{first})\log(\textit{mid}-\textit{first})$ primjena `cmp`.

Načelo rada:

Ideja `std::partial_sort` je sljedeća: nad elementima u `[first, mid)` izvede `make_heap()` i izgradi max-heap; zatim svaki element iz `[mid, last)` usporedi s `first`, pri čemu `first` sadrži najveći element gomile. Ako je element manji od tog maksimuma, zamijeni ih i prilagodi elemente u `[first, mid)` tako da ostanu max-heap. Nakon svih usporedbi nad `[first, mid)` izvede `sort_heap()` i tako ih poreda uzlazno. Napomena: heap-redoslijed i uzlazni redoslijed nisu isto.

## Vlastita usporedba

Vidi: [Preopterećenje operatora](https://en.cppreference.com/w/cpp/language/operators)

Za ugrađene tipove (npr. `int`) i korisnički definirane strukture može se prilagoditi funkcija usporedbe koju STL funkcije sortiranja koriste. Pri pozivu se kao posljednji parametar preda funkcija koja implementira binarnu usporedbu.

Za korisničke strukture prije uporabe STL funkcija sortiranja treba definirati barem jedan relacijski operator ili pri pozivu predati binarnu funkciju usporedbe. Obično se preporučuje definirati `operator<`.[^note1]

Primjer:

```cpp
int a[1009], n = 10;
// ...
std::sort(a + 1, a + 1 + n);                  // uzlazno
std::sort(a + 1, a + 1 + n, greater<int>());  // silazno
```

```cpp
struct data {
  int a, b;

  bool operator<(const data rhs) const {
    return (a == rhs.a) ? (b < rhs.b) : (a < rhs.a);
  }
} da[1009];

bool cmp(const data u1, const data u2) {
  return (u1.a == u2.a) ? (u1.b > u2.b) : (u1.a > u2.a);
}

// ...
std::sort(da + 1, da + 1 + 10);  // operator < definiran u strukturi, uzlazno
std::sort(da + 1, da + 1 + 10, cmp);  // usporedba funkcijom cmp, silazno
```

### Strogi slabi uređaj

Vidi i: [Primjena u C++-u – Teorija uređaja](../math/order-theory.md#c-中的应用)

Operator po kojem se sortira mora zadovoljavati [strogi slabi uređaj](../math/order-theory.md#二元关系), inače nastaju nepredvidive situacije (npr. greške pri izvođenju, netočno sortiranje).

Česte pogreške:

-   definiranje operatora „manje” za sortiranje pomoću `<=`;
-   čitanje vanjskog niza čije se vrijednosti mogu mijenjati tijekom poziva operatora sortiranja (često u algoritmima najkraćeg puta);
-   korištenje rezultata usporedbe maksimuma/minimuma više brojeva kao operatora sortiranja (klasična pogreška u zadacima poput „皇后游戏” (Igra kraljica) / „加工生产调度” (Raspoređivanje proizvodnje)).

## Vanjske poveznice

-   [O primjeni sortiranja zamjenom susjeda i na što treba paziti (kineski)](https://ouuan.github.io/浅谈邻项交换排序的应用以及需要注意的问题/)

## Literatura i bilješke

[^note1]: Jer većina STL funkcija prema zadanim postavkama koristi `operator<` za usporedbu.

[^note2]: [qsort, qsort\_s - cppreference.com](https://en.cppreference.com/c/algorithm/qsort)
