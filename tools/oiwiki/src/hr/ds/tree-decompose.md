---
title: Blokovna dekompozicija stabla
---

## Načini blokovne dekompozicije stabla

Može se pogledati [Pravi Moov algoritam na stablu](../misc/mo-algo-on-tree.md).

Također se može pogledati [ouuanov blog / Detaljno o Moovu algoritmu, Moovu algoritmu s izmjenama i Moovu algoritmu na stablu / Moov algoritam na stablu](https://ouuan.github.io/莫队、带修莫队、树上莫队详解/#树上莫队).

Za Moov algoritam na stablu također se mogu pogledati ta dva članka.

## Primjene blokovne dekompozicije stabla

Osim u Moovu algoritmu, blokovna dekompozicija stabla može se fleksibilno primijeniti i u nekim drugim problemima na stablima. No zadaci koji se mogu riješiti blokovnom dekompozicijom stabla obično imaju i bolja rješenja, pa je takvih zadataka razmjerno malo.

Usput, rješenje zadatka „gty 的妹子树” blokovnom dekompozicijom stabla može se oboriti zvijezdom (star graph).

### [BZOJ4763 雪辉](https://hydro.ac/p/bzoj-P4763)

Najprije napravimo blokovnu dekompoziciju stabla, a zatim za ključni vrh svakog bloka unaprijed izračunamo bitset boja na putu do svakog ključnog vrha među njegovim precima, kao i najbliži ključni predak svakog ključnog vrha; složenost je $O(n\sqrt n+\frac{nc}{32})$, gdje je $n\sqrt n$ složenost grubog skakanja prema gore iz svakog ključnog vrha, a $\frac{nc}{32}$ složenost pohrane $O(n)$ `bitset`-a.

Pri odgovaranju na upit najprije od krajnje točke puta grubom silom skačemo do ključnog vrha njezina bloka, zatim od ključnog vrha bloka skačemo blok po blok prema gore dok ne dođemo do bloka u kojem je $lca$, a potom grubom silom skačemo do $lca$. `bitset`-i između ključnih vrhova već su unaprijed izračunati, a ostatak računamo tijekom grubog skakanja. Složenost jednog upita je $O(\sqrt n+\frac c{32})$, gdje je $\sqrt n$ složenost grubog skakanja unutar bloka i skakanja blok po blok prema gore, a $O(\frac c{32})$ složenost spajanja unaprijed izračunatih rezultata s rezultatima grubog skakanja. Broj boja dobiva se pomoću `count()` na `bitset`-u, a $\operatorname{mex}$ pomoću `_Find_first()` na `bitset`-u.

Ukupna je složenost stoga $O((n+m)(\sqrt n+\frac c{32}))$.

??? note "Referentni kôd"
    ```cpp
    --8<-- "docs/ds/code/tree-decompose/tree-decompose_1.cpp"
    ```

### [BZOJ4812 由乃打扑克](https://hydro.ac/p/bzoj-P4812)

Ovaj je zadatak gotovo isti kao prethodni; jedina je razlika kako iz dobivenog `bitset`-a izračunati odgovor.

~~Budući da BZOJ računa ukupno vremensko ograničenje za sve testne podatke, teško ga je oboriti, pa se može proći s `_Find_next()`.~~

Pravo je rješenje računati po $16$ bitova odjednom: unaprijed za svih $2^{16}$ mogućih stanja izračunamo broj uzastopnih jedinica na visokim bitovima, broj uzastopnih jedinica na niskim bitovima i doprinos sredine. Samo što tada treba ručno napisati `bitset`, jer `bitset` iz standardne biblioteke ne može izdvojiti određenih $16$ bitova…

Kôd se može pogledati u [ovom blogu](https://www.cnblogs.com/FallDream/p/bzoj4763.html).
