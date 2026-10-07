---
title: Blokovna vezana lista
---

![./images/kuaizhuanglianbiao.png](./images/kuaizhuanglianbiao.png "./images/kuaizhuanglianbiao.png")

Blokovna vezana lista (unrolled linked list) izgleda otprilike ovako…

Lako je uočiti da je blokovna vezana lista zapravo vezana lista u kojoj svaki čvor pokazuje na jedan niz.
Izvorni niz duljine n podijelimo na $\sqrt{n}$ čvorova, a niz koji pripada svakom čvoru ima veličinu $\sqrt{n}$.
Zato strukturu definiramo ovako, kôd je u nastavku.
Pritom `sqn` označava `sqrt(n)`, tj. $\sqrt{n}$, a `pb` označava `push_back`, tj. dodavanje jednog elementa u ovaj `node`.

???+ note "Implementacija"
    ```cpp
    struct node {
      node* nxt;
      int size;
      char d[(sqn << 1) + 5];
    
      node() { size = 0, nxt = NULL, memset(d, 0, sizeof(d)); }
    
      void pb(char c) { d[size++] = c; }
    };
    ```

Blokovna vezana lista mora podržavati barem: dijeljenje, umetanje i pretraživanje.
Što je dijeljenje? Dijeljenje znači da se jedan `node` razdvoji na dva manja `node`-a kako bi veličina svakog `node`-a ostala blizu $\sqrt{n}$ (inače se struktura može degenerirati u običan niz). Dijeljenje se izvodi kad veličina nekog `node`-a premaši $2\times \sqrt{n}$.

Kako se izvodi dijeljenje? Najprije napravimo novi čvor, zatim zadnjih $\sqrt{n}$ vrijednosti čvora koji dijelimo kopiramo (`copy`) u novi čvor, potom tih zadnjih $\sqrt{n}$ vrijednosti obrišemo iz čvora koji dijelimo (`size--`) i na kraju novi čvor umetnemo iza čvora koji smo podijelili.

Složenost svih operacija blokovne vezane liste je $\sqrt{n}$.

Treba spomenuti još nešto.
Kako se elementi umeću (ili brišu), $n$ se mijenja, pa se mijenja i $\sqrt{n}$. Time se mijenja i veličina bloka – moramo li onda svaki put iznova održavati veličinu bloka?

Zapravo ne: dovoljno je $\sqrt{n}$ postaviti na fiksnu vrijednost. Primjerice, ako je ograničenje u zadatku $10^6$, onda $\sqrt{n}$ postavimo kao konstantu $10^3$ i više je ne mijenjamo.

```cpp
list<vector<char>> orz_list;
```

## `rope` u libstdc++

### Uvod

`rope` iz libstdc++ također igra ulogu blokovne vezane liste; implementiran je perzistentnim balansiranim stablom i omogućuje slučajan pristup te umetanje i brisanje elemenata.

Budući da `rope` zapravo nije implementiran blokovnom vezanom listom, njegova vremenska složenost nije jednaka složenosti blokovne vezane liste, nego odgovara složenosti perzistentnog balansiranog stabla (tj. $O(\log n)$).

Uključuje se ovako:

```cpp
#include <ext/rope>
using namespace __gnu_cxx;
```

???+ warning "O bibliotečnim funkcijama koje počinju dvostrukom donjom crtom"
    U OI-ju dugo nije bilo jasno smiju li se koristiti bibliotečne funkcije koje počinju dvostrukom donjom crtom; CCF je 2021. objavio [Dopunsko objašnjenje o ograničenjima uporabe programskih jezika na natjecanjima serije NOI](https://www.noi.cn/xw/2021-09-01/735729.shtml) u kojem stoji: „Dopuštena je uporaba bibliotečnih funkcija i makroa koji počinju donjom crtom, osim onih koji izvode izričito zabranjene operacije.” Stoga se `rope` danas na OI natjecanjima može normalno koristiti.

### Osnovne operacije

|          Operacija          |                              Učinak                              |
| :-------------------------: | :--------------------------------------------------------------: |
|        `rope<int> a`        | inicijalizira `rope` (vrlo slično spremnicima poput `vector`-a) |
|       `a.push_back(x)`      |                   dodaje element `x` na kraj `a`                  |
|      `a.insert(pos, x)`     |              dodaje element `x` na položaj `pos` u `a`            |
|      `a.erase(pos, x)`      |            briše `x` elemenata počevši od položaja `pos` u `a`    |
|     `a.at(x)` ili `a[x]`    |                  pristupa `x`-tom elementu od `a`                 |
| `a.length()` ili `a.size()` |                        vraća veličinu od `a`                      |

## Primjer zadatka

[POJ2887 Big String](http://poj.org/problem?id=2887)

Rješenje:
Vrlo jednostavan šablonski zadatak. Kôd slijedi:

```cpp
--8<-- "docs/ds/code/block-list/block-list_1.cpp"
```
