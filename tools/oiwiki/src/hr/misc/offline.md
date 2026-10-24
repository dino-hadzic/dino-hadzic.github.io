---
title: Uvod u offline algoritme
---

Ovo poglavlje predstavlja ideju offline algoritama (offline algorithm), uobičajene algoritme i optimizacije.

Offline algoritmi oblikuju se na temelju pretpostavke da su **svi podaci poznati prije rješavanja** i primjenjivi su na zadatke s više upita. Suprotno njima postoje [online algoritmi](https://en.wikipedia.org/wiki/Online_algorithm) (online algorithm).

Primjerice, [sortiranje izborom](../basic/selection-sort.md) ne može se izvesti dok nije poznat globalno najmanji element niza, pa je to offline algoritam, dok [sortiranje umetanjem](../basic/insertion-sort.md) može dinamički primati podatke i sortirati ih, ne zahtijevajući da svi podaci budu poznati prije izvođenja, pa je to online algoritam.

Za isti problem offline algoritmi često su bolji od online algoritama, među ostalim i po težini oblikovanja. Da bi natjecatelje spriječili u upotrebi offline algoritama, zadaci ponekad „prisiljavaju na online” (force online); uobičajen je način da se parametri sljedećeg upita mogu dobiti tek iz odgovora na prethodni upit ([interaktivni zadaci](../contest/problems.md#interaktivni-zadaci) i [komunikacijski zadaci](../contest/problems.md#komunikacijski-zadaci) također pripadaju ovoj vrsti).

Uobičajene ideje offline algoritama uključuju zajedničko rješavanje svih upita (npr. [CDQ podjela](./cdq-divide.md) (CDQ divide and conquer)), dobivanje odgovora na druge slične upite iz odgovora na jedan upit (npr. [paralelno binarno pretraživanje](./parallel-binsearch.md) (parallel binary search) i [Mo algoritam](./mo-algo-intro.md)) itd.

Budući da je offline algoritam ideja, a ne neki konkretan algoritam, upotrebljava se u kombinaciji s najrazličitijim strukturama podataka ili algoritmima, pa su i vrste zadataka povezanih s njim raznovrsnije.
