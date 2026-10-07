---
title: Binarni heap
---

## Struktura

Krenimo od strukture binarnog heapa: to je binarno stablo, i to potpuno binarno stablo, u čijem je svakom čvoru pohranjen jedan element (odnosno, svaki čvor ima težinu).

Svojstvo heapa: težina roditelja nije manja od težine djeteta (max-heap). Analogno možemo definirati min-heap. U ovom tekstu kao primjer uzimamo max-heap.

Zbog svojstva heapa korijen sadrži najveću vrijednost (time je operacija getmax riješena).

## Postupak

### Umetanje

Umetanje znači ubaciti element u binarni heap tako da on i nakon umetanja ostane potpuno binarno stablo.

Najjednostavniji je način umetnuti ga iza krajnjeg desnog lista u najdonjoj razini.

Ako je najdonja razina puna, dodaje se nova razina.

Nakon umetanja svojstvo heapa možda više ne vrijedi?

**Prilagodba prema gore**: ako je težina tog čvora veća od težine njegova roditelja, zamijenimo ih i postupak ponavljamo dok uvjet ne prestane vrijediti ili dok ne dođemo do korijena.

Može se dokazati da nakon umetanja i prilagodbe prema gore nijedan drugi čvor ne krši svojstvo heapa.

Vremenska složenost prilagodbe prema gore je $O(\log n)$.

![Umetanje u binarni heap](./images/binary_heap_insert.svg)

### Brisanje

Brisanje znači izbrisati najveći element heapa, tj. izbrisati korijen.

No ako ga izravno izbrišemo, dobivamo dva heapa, s čime je teško raditi.

Zato razmotrimo obrnuti postupak od umetanja: pokušajmo korijen premjestiti na mjesto posljednjeg čvora i zatim ga jednostavno izbrisati.

U praksi to nije lako izvesti, pa obično postupamo ovako: korijen i posljednji čvor izravno zamijenimo.

Tada izravno izbrišemo korijen (koji je sada na mjestu posljednjeg čvora), ali novi korijen možda ne zadovoljava svojstvo heapa...

**Prilagodba prema dolje**: među djecom tog čvora nađemo najveće, zamijenimo ga s čvorom i postupak ponavljamo do najdonje razine.

Može se dokazati da nakon brisanja i prilagodbe prema dolje nijedan drugi čvor ne krši svojstvo heapa.

Vremenska složenost je $O(\log n)$.

### Povećanje težine nekog čvora

Očito: nakon izravne izmjene dovoljna je jedna prilagodba prema gore, vremenska složenost $O(\log n)$.

## Implementacija

Vidimo da se gore opisane operacije oslanjaju na dvije ključne stvari: prilagodbu prema gore i prilagodbu prema dolje.

Heap prikazujemo nizom $h$. Djeca čvora $h_i$ su $h_{2i}$ i $h_{2i+1}$, a $1$ je korijen:

![Struktura heapa u nizu h](./images/binary-heap-array.svg)

Referentni kôd:

```cpp
void up(int x) {
  while (x > 1 && h[x] > h[x / 2]) {
    std::swap(h[x], h[x / 2]);
    x /= 2;
  }
}

void down(int x) {
  while (x * 2 <= n) {
    t = x * 2;
    if (t + 1 <= n && h[t + 1] > h[t]) t++;
    if (h[t] <= h[x]) break;
    std::swap(h[x], h[t]);
    x = t;
  }
}
```

### Izgradnja heapa

Razmotrimo sljedeći problem: krećemo od praznog heapa i umećemo $n$ elemenata, pri čemu redoslijed nije bitan.

Umetanje jednog po jednog traje $O(n \log n)$; postoji li bolji način?

#### Prvi način: prilagodba prema gore

Krenemo od korijena i idemo u BFS poretku.

```cpp
void build_heap_1() {
  for (i = 1; i <= n; i++) up(i);
}
```

Ovaj je postupak i dalje ekvivalentan umetanju jednog po jednog, samo što su elementi unaprijed smješteni u niz, što poboljšava konstantu. U najgorem slučaju vremenska složenost zadovoljava rekurziju $T(n) = T(n - 1) + \Theta(\log n)$, pa zbrajanjem dobivamo $T(n) = \Theta(n \log n)$.

#### Drugi način: prilagodba prema dolje

Promijenimo pristup: krenemo od listova i redom radimo prilagodbu prema dolje.

```cpp
void build_heap_2() {
  for (i = n; i >= 1; i--) down(i);
}
```

Drukčije rečeno, svaki put „spajamo” dva već uređena heapa, što objašnjava ispravnost.

Uočimo da listove ne treba prilagođavati, pa možemo krenuti od otprilike $n/2$-tog mjesta u nizu, što poboljšava konstantu. Prema tumačenju da svaki put spajamo dva heapa možemo napisati rekurziju za vremensku složenost $T(n) = 2T(\dfrac{n}{2}) + O(\log n)$, a iz glavnog teorema slijedi $T(n) = \Theta(n)$.

Heap se može izgraditi u $\Theta(n)$ zato što je svojstvo heapa vrlo slabo: binarni heap nije jedinstven.

Uz jak uvjet poput sortiranosti to ne bi bilo moguće.

## Primjene

### Dvostruki heap

??? note "[SPOJ RMID2 - Running Median Again](https://www.spoj.com/problems/RMID2/)"
    Održavajte niz uz dvije vrste operacija:
    
    1.  umetni element u niz
    2.  ispiši i izbriši trenutni medijan niza (ako je duljina niza parna, ispiši manji medijan)

Problem se može dalje poopćiti: dinamički održavati $k$-ti najveći broj u nizu, pri čemu se $k$ može mijenjati.

Za takve probleme možemo upotrijebiti tehniku **dvostrukog heapa** (two heaps) (izbjegavajući zamorno pisanje segment treea po vrijednostima ili BST-a).

Dvostruki heap sastoji se od jednog max-heapa i jednog min-heapa: min-heap čuva velike vrijednosti, tj. $k$ najvećih (uključujući $k$-ti), a max-heap čuva male vrijednosti, tj. sve ostale, manje od $k$-tog najvećeg.

Struktura sastavljena od ta dva heapa podržava sljedeće operacije:

-   održavanje: dok je veličina min-heapa manja od $k$, uzimaj vrh max-heapa i umeći ga u min-heap dok veličina min-heapa ne postane $k$; dok je veličina min-heapa veća od $k$, uzimaj vrh min-heapa i umeći ga u max-heap dok veličina min-heapa ne postane $k$;
-   umetanje elementa: ako je element veći ili jednak vrhu min-heapa, umetni ga u min-heap, inače u max-heap, a zatim održavaj dvostruki heap;
-   upit za $k$-ti najveći element: traženi element je vrh min-heapa;
-   brisanje $k$-tog najvećeg elementa: izbriši vrh min-heapa, a zatim održavaj dvostruki heap;
-   $k$ $+1/-1$: izravno održavaj dvostruki heap prema novoj vrijednosti $k$.

Očito je složenost upita za $k$-ti najveći element $O(1)$. Budući da se nakon umetanja, brisanja ili promjene $k$ veličina min-heapa od željenog $k$ razlikuje najviše za $1$, svako održavanje zahtijeva najviše jedno premještanje elementa između max-heapa i min-heapa, pa je složenost svih tih operacija $O(\log n)$.

??? note "Referentni kôd"
    ```cpp
    --8<-- "docs/ds/code/binary-heap/binary-heap_1.cpp"
    ```

### Zadaci

-   [SPOJ RMID - Running Median](https://www.spoj.com/problems/RMID)
-   [Luogu P1801 Crna kutija](https://www.luogu.com.cn/problem/P1801)
