---
title: Perzistentni spojivi heap
---

Perzistentni spojivi heap (persistent mergeable heap) obično se koristi za rješavanje problema $k$ najkraćih putova.

Ako vremenska složenost nekog spojivog heapa nije amortizirana, tada je nakon perzistentizacije složenost pojedine operacije zajamčeno $O(\log n)$, tj. složenost se ne može pokvariti na posebno konstruiranim podacima.

## Perzistentno lijevo stablo

Prije ovog gradiva upoznajte se s [lijevim stablom](./leftist-tree.md) (leftist tree).

### Postupak

Prisjetimo se spajanja lijevih stabala. Neka želimo spojiti dva lijeva stabla s korijenima $x$ i $y$ koja zadovoljavaju svojstvo min-heapa:

1.  Ako je jedan od čvorova $x,y$ prazan, vrati $x+y$.

2.  Od čvorova $x,y$ odaberi onaj s manjom vrijednošću; on postaje korijen spojenog lijevog stabla.

3.  Rekurzivno spoji desno podstablo od $x$ s $y$ i korijen rezultata postavi za desno dijete od $x$.

4.  Održi svojstvo „lijevosti” spojenog stabla, ažuriraj vrijednost `dist` i vrati odabrani korijen.

Budući da svaki rekurzivni poziv smanjuje `dist[x]+dist[y]` za jedan, a `dist[x]` je $O(\log n)$, u jednoj se operaciji mijenja najviše $O(\log n)$ čvorova, pa je vremenska složenost $O(\log n)$.

Perzistentnost zahtijeva čuvanje povijesti kako bi se kasnije mogle dohvatiti ranije verzije. Da bismo lijevo stablo učinili perzistentnim, moramo kopirati put koji se pri spajanju mijenja.

Spajanje perzistentnih lijevih stabala stoga izgleda ovako:

1.  Ako je jedan od čvorova $x,y$ prazan, vrati $x+y$.

2.  Od čvorova $x,y$ odaberi onaj s manjom vrijednošću i napravi njegovu kopiju $p$; ona postaje korijen spojenog lijevog stabla.

3.  Rekurzivno spoji desno podstablo od $p$ s $y$ i korijen rezultata postavi za desno dijete od $p$.

4.  Održi svojstvo lijevosti stabla s korijenom $p$, ažuriraj njegovu vrijednost `dist` i vrati $p$.

Budući da se u jednoj operaciji mijenja i stvara najviše $O(\log n)$ čvorova, uz $m$ operacija vremenska i prostorna složenost perzistentnog lijevog stabla iznose $O(m\log n)$.

### Referentna implementacija

```cpp
int merge(int x, int y) {
  if (!x || !y) return x + y;
  if (v[x] > v[y]) swap(x, y);
  int p = ++cnt;
  lc[p] = lc[x];
  v[p] = v[x];
  rc[p] = merge(rc[x], y);
  if (dist[lc[p]] < dist[rc[p]]) swap(lc[p], rc[p]);
  dist[p] = dist[rc[p]] + 1;
  return p;
}
```
