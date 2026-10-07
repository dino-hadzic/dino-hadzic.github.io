---
title: Balansirano stablo u segment treeu
---

## Uobičajena primjena

Na natjecanjima ponekad treba održavati informacije u više dimenzija. U takvim situacijama često posežemo za ugniježđenim stablima. Kad treba održavati prethodnika, sljedbenika, $k$-ti najveći element, rang nekog broja ili podržati umetanje i brisanje, obično nam treba balansirano stablo, pa koristimo segment tree u čijim su čvorovima balansirana stabla.

## Postupak

Princip implementacije objasnit ćemo na primjeru zadatka **二逼平衡树** (LOJ 106).

Ugniježđeno stablo gradimo tako da vanjski segment tree izgradimo na uobičajen način, a za svaki njegov čvor izgradimo balansirano stablo koje sadrži dio niza što ga taj čvor pokriva. U praksi elemente niza umećemo jedan po jedan: pri prolasku kroz svaki čvor segment treea element dodamo u balansirano stablo tog čvora.

Operacija 1, rang zadane vrijednosti na intervalu: vanjski segment tree obrađujemo uobičajeno, a za balansirano stablo svakog čvora unutar intervala vraćamo broj elemenata manjih od zadane vrijednosti; pri spajanju intervala te brojeve zbrajamo. Rezultat uvećan za $1$ je rang vrijednosti na intervalu.

Operacija 2, vrijednost s rangom $k$ na intervalu: možemo primijeniti binarno pretraživanje. Element se može pojaviti više puta, pa je njegov rang zapravo interval, a neki se elementi u nizu uopće ne pojavljuju. Zato razmišljamo slično kao kod operacije 1: binarno pretražujemo po broju elemenata manjih od zadane vrijednosti i tako dobivamo rješenje.

Operacija 3, zamjena jednog broja drugim: iz svih balansiranih stabala koja sadrže stari broj taj broj obrišemo i zatim umetnemo novi. Vanjski segment tree obrađujemo uobičajeno.

Operacija 4, prethodnik zadane vrijednosti na intervalu: vanjski segment tree obrađujemo uobičajeno, a za balansirano stablo svakog čvora unutar intervala vraćamo prethodnika zadane vrijednosti u tom stablu; pri spajanju intervala uzimamo maksimum.

## Svojstva

### Prostorna složenost

Svaki element dodajemo u $O(\log n)$ balansiranih stabala, pa je prostorna složenost $O((n + q)\log{n})$.

### Vremenska složenost

-   Za operacije 1, 3 i 4 radimo $O(\log{n})$ operacija na vanjskom segment treeu, a svaka od njih radi $O(\log{n})$ operacija na unutarnjem balansiranom stablu, pa je vremenska složenost $O(\log^2{n})$.
-   Operacija 2 ima dodatno binarno pretraživanje, pa je $O(\log^3{n})$.

## Klasični primjer

[LOJ 106 二逼平衡树](https://loj.ac/problem/106): vanjski segment tree, unutarnja balansirana stabla.

## Implementacija

Za kôd balansiranog stabla pogledajte [Splay](./splay.md) i druge članke.

Operacija 1:

```cpp
int vec_rank(int k, int l, int r, int x, int y, int t) {
  if (x <= l && r <= y) {
    return spy[k].chk_rank(t);
  }
  int mid = l + r >> 1;
  int res = 0;
  if (x <= mid) res += vec_rank(k << 1, l, mid, x, y, t);
  if (y > mid) res += vec_rank(k << 1 | 1, mid + 1, r, x, y, t);
  if (x <= mid && y > mid) res--;
  return res;
}
```

Operacija 2:

```cpp
int el = 0, er = 100000001, emid;
while (el != er) {
  emid = el + er >> 1;
  if (vec_rank(1, 1, n, tl, tr, emid) - 1 < tk)
    el = emid + 1;
  else
    er = emid;
}
printf("%d\n", el - 1);
```

Operacija 3:

```cpp
void vec_chg(int k, int l, int r, int loc, int x) {
  int t = spy[k].find(dat[loc]);
  spy[k].dele(t);
  spy[k].insert(x);
  if (l == r) return;
  int mid = l + r >> 1;
  if (loc <= mid) vec_chg(k << 1, l, mid, loc, x);
  if (loc > mid) vec_chg(k << 1 | 1, mid + 1, r, loc, x);
}
```

Operacija 4:

```cpp
int vec_front(int k, int l, int r, int x, int y, int t) {
  if (x <= l && r <= y) return spy[k].chk_front(t);
  int mid = l + r >> 1;
  int res = 0;
  if (x <= mid) res = max(res, vec_front(k << 1, l, mid, x, y, t));
  if (y > mid) res = max(res, vec_front(k << 1 | 1, mid + 1, r, x, y, t));
  return res;
}
```

## Srodni algoritmi

Kad zadatak s višedimenzionalnim informacijama ne zahtijeva rad online, umjesto naprednih struktura podataka možemo razmotriti i algoritme tipa podijeli pa vladaj poput [CDQ podjele](../misc/cdq-divide.md) ili [paralelnog binarnog pretraživanja](../misc/parallel-binsearch.md), čime se smanjuje težina implementacije.
