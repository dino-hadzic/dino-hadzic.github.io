---
title: Monotoni stog
---

## Uvod

Što je monotoni stog? Kako mu i ime kaže, monotoni stog (monotonic stack) je stog koji zadovoljava svojstvo monotonosti. Za razliku od monotonog reda, elementi ulaze i izlaze samo na jednom kraju.

Radi jednostavnijeg opisa, primjeri i pseudokod u nastavku održavaju monotono rastući stog cijelih brojeva.

## Postupak

### Umetanje

Kad element umećemo u monotoni stog, da bismo očuvali monotonost stoga, moramo izbaciti najmanji broj elemenata uz uvjet da cijeli stog ostane monoton nakon što taj element stavimo na vrh.

Primjerice, neka su elementi stoga od vrha prema dnu $\{0,11,45,81\}$.

![](images/monotonic-stack-before.svg)

Pri umetanju elementa $14$, radi očuvanja monotonosti moramo redom izbaciti elemente $0,11$; nakon te operacije stog postaje $\{14,45,81\}$.

![](images/monotonic-stack-after.svg)

Pseudokodom se to opisuje ovako:

???+ note "Implementacija"
    ```text
    insert x
    while !sta.empty() && sta.top()<x
        sta.pop()
    sta.push(x)
    ```

### Uporaba

Naravno, s vrha stoga čitamo jedan element; taj je element jedan od ekstrema s obzirom na monotonost.

U gornjem primjeru tako dohvaćamo minimum stoga.

## Primjene

??? note "[POJ3250 Bad Hair Day](http://poj.org/problem?id=3250)"
    $N$ krava stoji u redu slijeva nadesno; svaka krava ima visinu $h_i$. Neka se između $i$-te krave slijeva i „prve krave desno od nje visine $≥h_i$” nalazi $c_i$ krava. Izračunajte $\sum_{i=1}^{N} c_i$.

Osnovna je primjena ovaj zadatak – jednostavna uporaba monotonog stoga: za svaku kravu zabilježimo položaj na kojem je izbačena iz stoga (ako nikad nije izbačena, uzimamo krajnji desni kraj), a zatim uz malo obrade izračunamo traženi rezultat.

Osim toga, monotoni stog može se koristiti i za offline rješavanje problema RMQ.

Sve upite sortiramo po desnom kraju, a zatim svaki put u nizu skeniramo slijeva nadesno do desnog kraja trenutnog upita i skenirane elemente umećemo u monotoni stog. Tako su pri svakom odgovaranju na upit vrijednosti pohranjene u monotonom stogu upravo kandidati na položajima $\le r$ koji mogu biti odgovor, a ti elementi zadovoljavaju svojstvo monotonosti. Tada je prvi element u monotonom stogu čiji je položaj $\ge l$ odgovor na trenutni upit, a taj se korak može izvesti binarnim pretraživanjem. Vremenska složenost rješavanja RMQ-a monotonim stogom je $O(q\log q + q\log n)$, a prostorna $O(n)$.

## Zadaci za vježbu

-   [Luogu P5788 【模板】单调栈](https://www.luogu.com.cn/problem/P5788)
-   [Luogu P1901 发射站](https://www.luogu.com.cn/problem/P1901)
