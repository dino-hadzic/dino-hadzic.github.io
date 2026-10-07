---
title: Kartezijevo stablo
---

## Uvod

Kartezijevo stablo (Cartesian tree) binarno je stablo u kojem se svaki čvor sastoji od uređenog para ključeva $(k,w)$. Zahtijeva se da $k$ zadovoljava svojstvo binarnog stabla pretraživanja (BST), a $w$ svojstvo heapa. Ako su ključevi $k,w$ Kartezijeva stabla zadani, pri čemu su svi $k$ međusobno različiti i svi $w$ međusobno različiti, struktura tog Kartezijeva stabla je jedinstvena. Primjer je na slici:

![eg](./images/cartesian-tree1.png)

(Slika je preuzeta s Wikipedije.)

Gornje Kartezijevo stablo odgovara tome da vrijednosti elemenata niza uzmemo kao ključ $w$, a indekse niza kao ključ $k$. Vidimo da ključevi $k$ ovog stabla zadovoljavaju svojstvo BST-a, a ključevi $w$ svojstvo min-heapa. Ujedno, prema svojstvu binarnog stabla pretraživanja, vidimo da u ovakvom posebnom Kartezijevu stablu indeksi unutar jednog podstabla čine neprekinuti interval.

Kad se Kartezijevo stablo koristi na natjecanjima, kao ključ $k$ para obično se uzima indeks u nizu; indeksi $k$ zadovoljavaju svojstvo BST-a.

U nastavku, kad pišemo $k,w$, podrazumijevamo da $k$ zadovoljava svojstvo BST-a, a $w$ svojstvo heapa.

## Izgradnja Kartezijeva stabla monotonim stogom

### Postupak

Promotrimo umetanje elemenata u trenutačno Kartezijevo stablo redom po rastućem $k$.

Za Kartezijevo stablo definirajmo „desni lanac” kao lanac koji nastaje tako da od korijena stalno idemo u desno dijete, sve dok ne dođemo do čvora bez desnog djeteta. Nakon umetanja novi se čvor sigurno nalazi na desnom lancu. Budući da umećemo po rastućem $k$, koji zadovoljava svojstvo BST-a, novoumetnuti čvor nužno je na **krajnjem desnom** kraju stabla. Taj čvor ne može biti lijevo dijete, a nema ni desno dijete.

Stoga provodimo sljedeći postupak: odozdo prema gore uspoređujemo $w$ čvorova na desnom lancu s $w$ trenutačnog čvora $u$; čim nađemo čvor $x$ na desnom lancu za koji vrijedi $w_x<w_u$, čvor $u$ pripojimo kao desno dijete čvora $x$, a dotadašnje desno podstablo čvora $x$ postaje lijevo podstablo čvora $u$.

Crveni okvir na slici označava desni lanac koji cijelo vrijeme održavamo:

![build](./images/cartesian-tree2.png)

Očito svaki broj najviše jednom uđe u desni lanac i najviše jednom iz njega izađe (drugim riječima, svaki je čvor na desnom lancu tijekom jednog neprekinutog vremenskog odsječka). Taj se postupak može održavati monotonim stogom: u stogu čuvamo čvorove koji su trenutačno na desnom lancu Kartezijeva stabla. Čim neki čvor više nije na desnom lancu, izbacimo ga. Tako svaki čvor najviše jednom uđe i izađe, pa je složenost $O(n)$.

???+ note "Kartezijevo stablo i Treap"
    Zapravo je Treap vrsta Kartezijeva stabla, samo što su u Treapu vrijednosti $w$ potpuno nasumične. Treap ima linearni algoritam izgradnje: ako su ključevi $k$ unaprijed sortirani, izgradnju možemo obaviti gore opisanim algoritmom s monotonim stogom, iako se to rijetko tako radi.

### Implementacija u C++-u

```cpp
// stk čuva indekse u nizu koji odgovaraju čvorovima Kartezijeva stabla
for (int i = 1; i <= n; i++) {
  int k = top;  // top je vrh stoga prije operacije, k je trenutačni vrh stoga
  while (k > 0 && w[stk[k]] > w[i]) k--;  // održavamo čvorove na desnom lancu
  if (k) rs[stk[k]] = i;  // vrh stoga.desno dijete := trenutačni element
  if (k < top) ls[i] = stk[k + 1];  // trenutačni element.lijevo dijete := posljednji izbačeni element
  stk[++k] = i;                     // trenutačni element ide na stog
  top = k;
}
```

## Primjer zadatka

???+ note "[HDU 1506. Largest Rectangle in a Histogram](https://acm.hdu.edu.cn/showproblem.php?pid=1506)"
    Zadano je $n$ pozicija, na svakoj je visina $h_i$; treba naći najveći podpravokutnik. Kao na slici:
    
    ![eg](./images/cartesian-tree3.png)
    
    Osjenčani dio na slici je najveći podpravokutnik.

??? note "Ideja rješenja"
    Konkretno, indeks uzimamo kao ključ $k$, a $h_i$ kao ključ $w$ koji zadovoljava svojstvo min-heapa, i izgradimo Kartezijevo stablo od parova $(i,h_i)$.
    
    Zatim prolazimo po svim čvorovima $u$ i uzimamo $w_u$ (tj. visinu $h$ čvora $u$) kao visinu najvećeg podpravokutnika. Budući da izgrađeno Kartezijevo stablo zadovoljava svojstvo min-heapa, visine svih čvorova u podstablu čvora $u$ veće su ili jednake visini čvora $u$. Također znamo da indeksi u podstablu čvora $u$ čine neprekinuti interval. Dakle, dovoljno je znati veličinu podstabla pa možemo izračunati površinu najvećeg podpravokutnika na tom intervalu. Vrijednošću izračunatom za svaki čvor ažuriramo odgovor. Očito se to može obaviti jednim DFS-om, pa je složenost $O(n)$.

??? note "Primjer implementacije"
    ```cpp
    --8<-- "docs/ds/code/cartesian-tree/cartesian-tree_1.cpp"
    ```

## Literatura

[Cartesian tree – Wikipedia](https://en.wikipedia.org/wiki/Cartesian_tree)
