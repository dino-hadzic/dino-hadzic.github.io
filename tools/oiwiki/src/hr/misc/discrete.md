---
title: Diskretizacija
---

## Uvod

Diskretizacija je tehnika obrade podataka koja se u suštini može promatrati kao vrsta [hasha](../string/hash.md#ideja-hashiranja) koja jamči da podaci nakon hashiranja i dalje zadržavaju izvorni [potpuni/parcijalni uređaj](../math/order-theory.md#偏序集).

Jednostavno rečeno, kad se neki podaci, zato što su sami po sebi veliki ili zato što im tip to ne podržava, ne mogu izravno upotrijebiti kao indeksi niza radi praktične obrade, a na konačan rezultat utječu samo odnosi relativne veličine među elementima, možemo problem obraditi tako da izvorne podatke zamijenimo njihovim rangom, što se zove diskretizacija.

Diskretizirati se mogu veliki cijeli brojevi, brojevi s pomičnim zarezom, stringovi itd.

## Implementacija

Diskretizacija niza i zatim upiti nad njim razmjerno je čest scenarij primjene.

### Prva metoda

Obično u izvornom nizu postoje ponovljeni elementi i jednaki se elementi u pravilu diskretiziraju u istu vrijednost.

Postupak je sljedeći:

1.  Napravi kopiju izvornog niza.

2.  Sortiraj vrijednosti u kopiji od najmanje do najveće.

3.  Iz sortirane kopije ukloni duplikate.

4.  Za svaki element izvornog niza pronađi njegov položaj u kopiji; položaj je rang, koji postaje diskretizirana vrijednost.

```cpp
// arr[i] je početni niz, raspon indeksa je [1, n]

for (int i = 1; i <= n; ++i)  // korak 1
  tmp[i] = arr[i];
std::sort(tmp + 1, tmp + n + 1);                          // korak 2
int len = std::unique(tmp + 1, tmp + n + 1) - (tmp + 1);  // korak 3
for (int i = 1; i <= n; ++i)                              // korak 4
  arr[i] = std::lower_bound(tmp + 1, tmp + len + 1, arr[i]) - tmp;
```

Za STL algoritme upotrijebljene u referentnoj implementaciji pogledajte [STL algoritme](../lang/csl/algorithm.md).

Na isti način možemo diskretizirati i [std::vector](../lang/csl/sequence-container.md#vector):

```cpp
// std::vector<int> arr;
std::vector<int> tmp(arr);  // tmp je kopija niza arr
std::sort(tmp.begin(), tmp.end());
tmp.erase(std::unique(tmp.begin(), tmp.end()), tmp.end());
for (int i = 0; i < n; ++i)
  arr[i] = std::lower_bound(tmp.begin(), tmp.end(), arr[i]) - tmp.begin();
```

### Druga metoda

Ovisno o zahtjevima zadatka, jednaki se elementi ponekad diskretiziraju u različite vrijednosti prema redoslijedu unosa.

Tada je implementacija funkcijom `std::lower_bound()` nešto teža i treba promijeniti pristup:

1.  Napravi kopiju izvornog niza i ujedno zabilježi položaj pojavljivanja svakog elementa.

2.  Sortiraj kopiju po vrijednosti od najmanje do najveće; kad su vrijednosti jednake, sortiraj po redoslijedu pojavljivanja od manjeg do većeg.

3.  Vrati diskretizirane brojeve u izvorni niz.

```cpp
struct Data {
  int idx, val;

  bool operator<(const Data& o) const {
    if (val == o.val)
      return idx < o.idx;  // kad su vrijednosti jednake, element koji se pojavio ranije dobiva manju diskretiziranu vrijednost
    return val < o.val;
  }
} tmp[MAXN];  // može se upotrijebiti i std::pair

for (int i = 1; i <= n; ++i) tmp[i] = Data{i, arr[i]};
std::sort(tmp + 1, tmp + n + 1);
for (int i = 1; i <= n; ++i) arr[tmp[i].idx] = i;
```

### Složenost

Kod prve metode složenost uklanjanja duplikata je $O(n)$, složenost sortiranja je $O(n \log n)$, a složenost završnih $n$ pretraživanja je $O(n \log n)$.

Kod druge metode složenost sortiranja je $O(n \log n)$.

Stoga je ukupna vremenska složenost obiju metoda $O(n \log n)$.

Prostorna složenost je $O(n)$.

## Zadaci za vježbu

-   [\[HAOI2014\] 贴海报 (Lijepljenje plakata)](https://www.luogu.com.cn/problem/P3740)
-   [\[NOI2015\] 程序自动分析 (Automatska analiza programa)](https://www.luogu.com.cn/problem/P1955)
