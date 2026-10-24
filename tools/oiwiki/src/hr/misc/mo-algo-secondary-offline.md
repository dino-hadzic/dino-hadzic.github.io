---
title: Dvostruko offline Mo algoritam (Mo secondary offline)
---

## Pregled

Ponekad nailazimo na zadatke koji izgledaju vrlo pogodni za Mo algoritam (Mo's algorithm), ali pojedinačni prijelaz u njima nije $O(1)$; tada izravna primjena Mo algoritma, čak i uz podešavanje veličine bloka, daje neispravnu složenost.

Ako se u takvom slučaju doprinos svakog prijelaza odgovoru može zapisati kao razlika (diferencirati), te prijelaze možemo rastaviti, spremiti offline i skupno obraditi drugim algoritmom.

Označimo s $f(x, l, r)$ doprinos koji $x$ daje s obzirom na $[l, r]$.

Kad, primjerice, trenutni interval $[l, r]$ proširujemo na $[l, r + 1]$, tražimo $f(a_{r + 1}, l, r)$. Ako se to može diferencirati, možemo ga zapisati kao $f(a_{r + 1}, 1, r) - f(a_{r + 1}, 1, l - 1)$, pri čemu prvi član možemo pretprocesirati za svaki $r$, a svaki takav drugi član možemo offline spremiti na odgovarajući $l - 1$, a zatim ih obraditi prolaskom (sweep line) od manjih prema većima. Ostali smjerovi prijelaza obrađuju se analogno.

Taj algoritam, koji povrh Mo algoritma – koji je i sam offline algoritam – još jednom offline obrađuje prijelaze, zove se dvostruko offline Mo algoritam (Mo's algorithm with secondary offline).

Razumjet ćemo ga na konkretnim zadacima.

## Primjeri zadataka

???+ note "[Luogu P5047 \[Ynoi2019 模拟赛 (probno natjecanje)\] Yuno loves sqrt technology II](https://www.luogu.com.cn/problem/P5047)"
    Zadan je niz $a$ duljine $n$ i $m$ upita; svaki upit traži broj inverzija u nekom intervalu.
    
    Ograničenja: $1 \leq n,m \leq 10^5$, $0 \leq a_i \leq 10^9$.

Izravnim Mo algoritmom svaki prijelaz traje barem $O(\log n)$; uočavamo da je informacija koju pri svakom prijelazu trebamo „rang nekog broja unutar nekog intervala”, a ta se informacija s obzirom na interval može diferencirati, pa razmatramo dvostruki offline postupak.

Kad $[l, r]$ proširujemo na $[l, r + 1]$, tražimo koliko je brojeva u intervalu $[l, r]$ većih od $a_{r + 1}$.
Označimo s $f(x, r)$ broj brojeva u intervalu $[1, r]$ većih od $a_x$, a s $g(x, r)$ broj brojeva u intervalu $[1, r]$ manjih od $a_x$. Tada se promjena odgovora može zapisati kao $f(r + 1, r) - f(r + 1, l - 1)$.

Analogno, promjena pri smanjivanju $[l, r]$ na $[l, r - 1]$ može se zapisati kao $-f(r, r - 1) + f(r, l - 1)$; proširivanje $[l, r]$ na $[l - 1, r]$ kao $g(l - 1, r) - g(l - 1, l - 2)$, a smanjivanje $[l, r]$ na $[l + 1, r]$ kao $- g(l, r) + g(l, l - 1)$.

Članove $f(x, x - 1)$ i $g(x, x - 1)$ iz tih izraza možemo unaprijed pretprocesirati Fenwickovim stablom u $O(n \log n)$; za ostale članove $f(x, p)$ i $g(x, p)$ spremimo $x$ offline na $l$ radi skupne obrade.

Ovdje postoji trik za uštedu memorije: primjećujemo da su pri obradi svakog upita vrijednosti $x$ spremljene offline na $p$ uvijek jedan neprekinuti odsječak, pa ne moramo spremati svaki pomak, nego samo odsječak za koji se vrši prilagodba. Tako memorija s ukupnog broja pomaka $O(n\sqrt{m})$ pada na broj upita $O(m)$.

Sad obradimo problem koji smo spremili offline: dodavanje brojeva u skup i upit za rang broja u skupu. Ukupan broj pomaka krajeva u Mo algoritmu je $O(n\sqrt{m})$, a niz ima duljinu samo $O(n)$, pa problem rješavamo podjelom domene vrijednosti na blokove (value-range blocking) s umetanjem u $O(\sqrt{n})$ i upitom u $O(1)$.

Time smo zadatak riješili u vremenskoj složenosti $O(n \sqrt{m} + n \sqrt{n})$ i memorijskoj složenosti $O(n + m)$.

Na kraju valja napomenuti da smo izračunali promjene odgovora pri svakom koraku, a ne same odgovore, pa konačne odgovore dobivamo tek njihovim prefiksnim sumama.

??? note "Primjer koda"
    ```cpp
    --8<-- "docs/misc/code/mo-algo-secondary-offline/mo-algo-secondary-offline_1.cpp"
    ```

???+ note "[Luogu P5501 \[LnOI2019\] 来者不拒，去者不追 (Tko dođe, dobrodošao; tko ode, ne zadržavamo ga)](https://www.luogu.com.cn/problem/P5501)"
    Više puta se pita zbroj „Abbi vrijednosti” svih brojeva u intervalu $[l, r]$.
    
    Abbi vrijednost definira se ovako: ako je $a_i$ $k$-ti najmanji u intervalu upita $[l,r]$, njegova je „Abbi vrijednost” jednaka $ka_i$.

Neka je $f(x,r)$ zbroj brojeva u $[1,r]$ većih od $a_x$, a $g(x,r)$ broj brojeva u $[1,r]$ većih od $a_x$. Tada je doprinos pri pomicanju desnog kraja udesno $f(r,r-1)-f(r,l-1) + a_r(r-l+ 1-(g(r,r-1)-g(r,l-1)))$; ostali se smjerovi zapisuju analogno, pa ih ovdje ne navodimo.

Članovi $f(r, r - 1)$ i $g(r, r - 1)$ u gornjem izrazu i dalje se mogu pretprocesirati, a ostali se spremaju offline na drugi kraj i obrađuju prolaskom (sweep line). Lako se vidi da i dalje imamo problem s $O(n)$ umetanja i $O(n\sqrt{m})$ upita za rang, pa ga također rješavamo podjelom domene vrijednosti na blokove.

??? note "Primjer koda"
    ```cpp
    --8<-- "docs/misc/code/mo-algo-secondary-offline/mo-algo-secondary-offline_2.cpp"
    ```
