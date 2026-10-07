---
title: Segment tree u segment treeu
---

## Uobičajena primjena

Na natjecanjima ponekad treba održavati informacije u više dimenzija. U takvim situacijama često posežemo za ugniježđenim stablima (tree of trees, „stablo u stablu”).

## Princip implementacije

Razmotrimo kako ugniježđenim stablima izvesti promjenu u točki i upit na području u dvodimenzionalnoj ravnini. Promotrimo vanjski segment tree: podstabla njegovih $n$ listova, od $1$ do $n$, predstavljaju segment treeove redaka $1$ do $n$. Roditelj dvaju takvih čvorova tada predstavlja područje koje pokrivaju podstabla njegovo dvoje djece.

## Svojstva

### Prostorna složenost

U pravilu si ne možemo priuštiti da za svaki čvor vanjskog segment treea izgradimo potpun unutarnji segment tree, jer bi memorijski zahtjevi bili preveliki. Ugniježđena stabla zato obično koriste dinamičko stvaranje čvorova. Jedna promjena dotiče $\log{n}$ čvorova vanjskog segment treea, a u podstablu svakog od njih $\log{n}$ čvorova, pa jedna promjena stvara najviše $\log^2{n}$ novih čvorova.

### Vremenska složenost

Za upit radimo $\log{n}$ operacija na vanjskom segment treeu, a svaka od njih radi $\log{n}$ operacija na jednom unutarnjem segment treeu, pa je vremenska složenost $\log^2{n}$.
Promjena ima istu složenost kao i upit, također $\log^2{n}$.

## Klasični primjer

[Luogu P3810 陌上花开](https://www.luogu.com.cn/problem/P3810): prvu dimenziju obradimo sortiranjem, a drugu i treću održavamo ugniježđenim stablima.

## Primjer koda

Upit po drugoj dimenziji

```cpp
int tree_query(int k, int l, int r, int x) {
  if (k == 0) return 0;
  if (1 <= l && r <= sec[x].y) return vec_query(ou_root[k], 1, p, 1, sec[x].z);
  int mid = l + r >> 1, res = 0;
  if (1 <= mid) res += tree_query(ou_ch[k][0], l, mid, x);
  if (sec[x].y > mid) res += tree_query(ou_ch[k][1], mid + 1, r, x);
  return res;
}
```

Promjena po drugoj dimenziji

```cpp
void tree_insert(int &k, int l, int r, int x) {
  if (k == 0) k = ++ou_tot;
  vec_insert(ou_root[k], 1, p, sec[x].z);
  if (l == r) return;
  int mid = l + r >> 1;
  if (sec[x].y <= mid)
    tree_insert(ou_ch[k][0], l, mid, x);
  else
    tree_insert(ou_ch[k][1], mid + 1, r, x);
}
```

Upit po trećoj dimenziji

```cpp
int vec_query(int k, int l, int r, int x, int y) {
  if (k == 0) return 0;
  if (x <= l && r <= y) return data[k];
  int mid = l + r >> 1, res = 0;
  if (x <= mid) res += vec_query(ch[k][0], l, mid, x, y);
  if (y > mid) res += vec_query(ch[k][1], mid + 1, r, x, y);
  return res;
}
```

Promjena po trećoj dimenziji

```cpp
void vec_insert(int &k, int l, int r, int loc) {
  if (k == 0) k = ++tot;
  data[k]++;
  if (l == r) return;
  int mid = l + r >> 1;
  if (loc <= mid) vec_insert(ch[k][0], l, mid, loc);
  if (loc > mid) vec_insert(ch[k][1], mid + 1, r, loc);
}
```

## Srodni algoritmi

Kad zadatak s višedimenzionalnim informacijama ne zahtijeva rad online, umjesto naprednih struktura podataka možemo razmotriti i algoritme tipa podijeli pa vladaj poput **CDQ podjele** (CDQ divide and conquer) ili **paralelnog binarnog pretraživanja**, čime se smanjuje težina implementacije.
